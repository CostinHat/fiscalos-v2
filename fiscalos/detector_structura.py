# -*- coding: utf-8 -*-
"""C31 - detectorul mecanic pentru clasa de defect "articole atomizate sub alt articol".

Defectul care l-a aratat: in instantaneul iConta al Codului muncii, textul art. 122 sta sub
`legea_53_2003_codul_muncii#art281/alin7~6`. Marcajele de articol nu s-au recunoscut, iar corpul
articolelor urmatoare s-a lipit, ca alineate, de ultimul articol recunoscut.

TREI SEMNALE, toate mecanice, pe atomii unui act:
  S1 alineate DUPLICATE direct sub acelasi articol (`art281/alin7~6`): un articol nu are doua alineate
     (7); al doilea e al altui articol, inghitit.
  S2 ACOPERIREA numerotarii: articolele arabe distincte recunoscute / cel mai mare numar de articol.
     Un cod cu art. 281 si 40 de articole recunoscute a pierdut restul.
  S3 articol imbricat sub alt articol intr-un act de BAZA (intr-un act modificator, articolul citat
     sub un punct de interventie e legitim si nu se numara).
  S4 articole INGHITITE INTR-O NOTA: textul de dupa marcajul de nota (V2) contine un marcaj de articol
     ("⟦NOTĂ⟧ Notă ... + Articolul 122 (1) ..."). Gasit dupa primul detector: in Codul muncii oficial,
     o nota goala `<span .../>` numarata ca deschisa a inghitit art. 122-124 - S1-S3 nu o vedeau.
Un act e STRICAT daca S1 >= 3, sau S2 < 0.8 cu cel mai mare articol >= 10, sau S3 >= 1, sau S4 >= 1.
"""
import json
import os
import re

from fiscalos import potrivire, surse

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_EXTRAS = re.compile(r"_art_?\d+|_art\d+_", re.I)
_ISTORIC = re.compile(r"forma_initiala|_pre_|istoric|^GRESIT_", re.I)


def _numar(cheie):
    m = re.match(r"^(\d+)", str(cheie))
    return int(m.group(1)) if m else None


def semnale(ats, e_modificator, extras=False):
    ids = {a["id"]: a for a in ats}
    s1 = [a["id"] for a in ats if a["nivel"] == "alineat" and re.search(r"/alin[^/]*~\d+$", a["id"])
          and ids.get(a["parinte"], {}).get("nivel") == "articol"]
    arabe = {_numar(a["cheie"]) for a in ats if a["nivel"] == "articol" and a.get("anexa") is None
             and a["parinte"] is None and _numar(a["cheie"]) is not None}
    maxim = max(arabe) if arabe else 0
    # S2 are sens numai pentru un act de baza INTREG: un act modificator numara roman (arabele lui sunt
    # citate), iar un extras deliberat ("..._art_1616_1623_...") nu are cum sa acopere actul
    acoperire = round(len(arabe) / float(maxim), 3) if maxim and not e_modificator and not extras else None
    s3 = [] if e_modificator else [
        a["id"] for a in ats if a["nivel"] == "articol" and a["parinte"]
        and not ids.get(a["parinte"], {}).get("interventie") and ids.get(a["parinte"], {}).get("nivel") != "anexa"]
    s4 = [a["id"] for a in ats if "⟦NOTĂ⟧" in a["text"]
          and re.search(r"\+\s*Articolul\s+\d", a["text"].split("⟦NOTĂ⟧", 1)[1])]
    return {"S4_articole_in_nota": len(s4), "S4_exemple": s4[:5], "S1_alineate_duplicate": len(s1), "S1_exemple": s1[:5], "S2_articole_recunoscute": len(arabe),
            "S2_cel_mai_mare_articol": maxim, "S2_acoperire": acoperire, "S3_articole_imbricate": len(s3),
            "S3_exemple": s3[:5]}


def e_stricat(s):
    return (s["S1_alineate_duplicate"] >= 3
            or (s["S2_acoperire"] is not None and s["S2_acoperire"] < 0.8 and s["S2_cel_mai_mare_articol"] >= 10)
            or s["S3_articole_imbricate"] >= 1 or s["S4_articole_in_nota"] >= 1)


def detecteaza(corp=None):
    corp = corp or potrivire.Corpus()
    rez = {}
    for act, ats in sorted(corp.pe_act.items()):
        if not any(a["nivel"] == "articol" for a in ats):
            continue                                    # F4 (fragmente): fara structura de articol
        s = semnale(ats, act in corp.modificatoare, extras=bool(_EXTRAS.search(act)))
        if not e_stricat(s):
            continue
        normativ = surse.e_act_normativ(act)[0]
        sursa = corp.sursa_act.get(act, {}).get("sursa", "")
        if not normativ:
            categ = "nenormativ - numai raportat"
        elif _ISTORIC.search(act):
            categ = "redare istorica - nu se inlocuieste cu consolidatul curent"
        elif sursa.startswith(("oficial", "compus")):
            categ = "deja din sursa oficiala - defect al conversiei portalului"
        else:
            categ = "de adus din sursa oficiala"
        rez[act] = dict(s, sursa=sursa, categorie=categ, modificator=act in corp.modificatoare)
    return rez


if __name__ == "__main__":
    r = detecteaza()
    json.dump(r, open(os.path.join(_RAD, "artefacte", "detector_structura.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    from collections import Counter
    print(Counter(v["categorie"] for v in r.values()))
    for a, v in r.items():
        print("%-60s S1=%-3d S2=%s/%s (%.2f) S3=%d | %s" % (a[:60], v["S1_alineate_duplicate"],
              v["S2_articole_recunoscute"], v["S2_cel_mai_mare_articol"], v["S2_acoperire"] or 0,
              v["S3_articole_imbricate"], v["categorie"]))
