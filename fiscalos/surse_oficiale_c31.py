# -*- coding: utf-8 -*-
"""C31 - actele gasite STRICATE de detector se aduc din sursa oficiala, ca la C12.

Numele actului din instantaneu ("legea_53_2003_codul_muncii", "oug_44_2008") da tipul, numarul si
anul; cautarea portalului (tip + numar + an) da id-ul. Rezolvarea se scrie, cu motivul, in
`surse_oficiale/C31_rezolvare.json` - un act nerezolvat nu se ghiceste, se raporteaza.

Doua reguli, ca sa nu apara acelasi act de doua ori in corpus:
  - daca actul (tip, numar, an) exista deja in stratul oficial sub alt nume, NU se aduce din nou;
  - mai multe redari din instantaneu ale aceluiasi act (legea_165_2018_anaf / _mf_2024) -> se aduce o
    singura data, sub numele canonic (cel "_consolidat", altfel cel mai scurt); celelalte se listeaza.
"""
import json
import os
import re
import time

from fiscalos import detector_structura, portal, surse_oficiale

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TIP = {"legea": ("1", "LEGE"), "lege": ("1", "LEGE"), "oug": ("18", "OUG"), "og": ("13", "ORDONANȚĂ"),
       "hg": ("2", "HOTĂRÂRE"), "omfp": ("5", "ORDIN"), "omf": ("5", "ORDIN"), "opanaf": ("5", "ORDIN"),
       "oms": ("5", "ORDIN"), "ordin": ("5", "ORDIN")}
EMITENT = {"omfp": r"FINAN", "omf": r"FINAN", "opanaf": r"ADMINISTRARE FISCAL", "oms": r"S[AĂ]N[AĂ]T"}


def cheie(act):
    m = re.match(r"^([a-z]+)_(\d+)_(\d{4})", act.lower())
    return (m.group(1).replace("lege", "legea").replace("legeaa", "legea"), m.group(2), m.group(3)) \
        if m and m.group(1) in TIP else None


def rezolva(p, act):
    k = cheie(act)
    if k is None:
        return None, "numele nu da tip/numar/an"
    tip, nr, an = k
    cod, _et = TIP[tip]
    hit = [(i, t) for i, t in p.cauta(tip=cod, numar=nr, an=an)
           if re.search(r"\b%s\s+\d{2}/\d{2}/%s\b" % (nr, an), t)]
    if not hit:
        return None, "portalul nu are rezultat pentru tip %s nr. %s/%s" % (cod, nr, an)
    if tip in EMITENT:
        buni = []
        for i, t in hit:
            corp, _info = p.act(i)
            if re.search(EMITENT[tip], corp.decode("utf-8", "replace")[:200000].upper()):
                buni.append((i, t))
        hit = buni
        if not hit:
            return None, "niciun ordin %s/%s al emitentului asteptat" % (nr, an)
    if len({i for i, _t in hit}) > 1 and tip in ("omfp", "omf", "opanaf", "oms", "ordin"):
        return None, "ambiguu: %s" % hit[:4]
    return hit[0], "cautare tip %s, nr. %s, an %s -> %s" % (cod, nr, an, hit[0][1])


def ruleaza():
    t0 = time.time()
    det = detector_structura.detecteaza()
    de_adus = sorted(a for a, v in det.items() if v["categorie"] == "de adus din sursa oficiala")
    man = json.load(open(os.path.join(surse_oficiale.DIR, "MANIFEST.json"), encoding="utf-8"))
    oficiale = {cheie(a): a for a in man["acte"] if cheie(a)}
    grupe = {}
    for a in de_adus:
        grupe.setdefault(cheie(a), []).append(a)
    p = portal.Portal()
    rez, acte = {}, []
    for k, nume in sorted(grupe.items(), key=lambda kv: str(kv[0])):
        if k is None:
            for a in nume:
                rez[a] = {"stare": "nerezolvat", "motiv": "numele nu da tip/numar/an"}
            continue
        if k in oficiale:
            for a in nume:
                rez[a] = {"stare": "acelasi act exista deja in stratul oficial", "ca": oficiale[k]}
            continue
        canonic = sorted(nume, key=lambda a: ("consolidat" not in a, len(a)))[0]
        hit, motiv = rezolva(p, canonic)
        for a in nume:
            if a != canonic:
                rez[a] = {"stare": "varianta a aceluiasi act", "ca": canonic}
        if hit is None:
            rez[canonic] = {"stare": "nerezolvat", "motiv": motiv}
            continue
        rez[canonic] = {"stare": "adus", "id_portal": hit[0], "titlu": hit[1], "motiv": motiv}
        acte.append((canonic, hit[0], "C31: structura stricata in instantaneu (detector_structura)"))
    surse_oficiale.aduce(acte, incremental=True)
    out = {"_ce": "C31: rezolvarea actelor stricate spre sursa oficiala.", "facut_la": time.strftime(
        "%Y-%m-%dT%H:%M:%S"), "secunde": round(time.time() - t0, 1), "acte": rez}
    json.dump(out, open(os.path.join(surse_oficiale.DIR, "C31_rezolvare.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    r = ruleaza()
    from collections import Counter
    print(Counter(v["stare"] for v in r["acte"].values()), r["secunde"], "s")
    for a, v in r["acte"].items():
        if v["stare"] != "adus":
            print("  ", a, v)
