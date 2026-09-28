# -*- coding: utf-8 -*-
"""BANC DE MUTATII — dovada in CEALALTA direcţie: detectorul chiar prinde o divergenta reala?

DE CE EXISTA. "0 DIFERA" e o afirmaţie fara valoare daca detectorul nu poate produce un DIFERA
niciodata. Un clasificator care spune mereu CONCORDA da acelasi zero, si arata la fel in raport.
Deci se injecteaza greșeli CUNOSCUTE - luate din istoria fiscala reala a iConta, nu inventate - si se
cere ca fiecare sa iasa DIFERA, cu temeiul CORECT alaturi.

UNDE se injecteaza: pe o COPIE in memorie a inventarului. Nimic nu se scrie in iConta si nimic nu se
scrie nici in `artefacte/inventar_iconta.json` - bancul nu atinge inventarul real, il citeste.

CE NU dovedeste bancul: ca detectorul prinde ORICE divergenta. Dovedeste ca prinde exact aceste
cinci clase, care sunt clasele pe care legislaţia romaneasca le-a produs efectiv in ultimii doi ani:
o cota schimbata de o lege noua, o cota veche rămasa in cod, un plafon vechi aplicat unei perioade
noi, o cota inventata care nu exista in nicio forma a actului, si o citare care duce la alt act.
"""
import copy
import json
import os

from fiscalos import potrivire

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── mutaţiile, fiecare cu ce trebuie sa iasa ─────────────────────────────────────────────────────
# DECIZIA C7 (Costin): bancul acopera FIECARE clasa - cota, plafon, termen, nomenclator, cont -, cu
# cel puţin o mutaţie pe clasa care trebuie sa iasa DIFERA sau NEGASIT cu motivul corect.
# `aștept`       clasificarea cerută
# `lege_conţine` ce trebuie sa raporteze detectorul din textul legii (pentru DIFERA)
# `motiv_conţine` un fragment pe care motivul trebuie sa-l conţina (pentru NEGASIT: motivul CORECT)
MUTATII = [
    # ── cota ──────────────────────────────────────────────────────────────────────────────────
    {"clasa": "cota", "nume": "dividende 10% in loc de 16%",
     "parametru": "cote/impozit_dividend@2026-01-01",
     "schimba": {"valoare_cod": "0.10", "procent_cod": "10"},
     "de_ce": "cota reala din 2025 (OUG 156/2024), rămasa in cod dupa ce Legea 141/2025 a urcat-o "
              "la 16% de la 01.01.2026 - clasa 'cota veche rămasa in cod'",
     "aștept": "DIFERA", "lege_conţine": "16"},
    {"clasa": "cota", "nume": "TVA standard 19% in loc de 21%",
     "parametru": "cote/tva_standard@2025-08-01",
     "schimba": {"valoare_cod": "0.19", "procent_cod": "19"},
     "de_ce": "cota de dinainte de 01.08.2025; exact greșeala pe care Legea 141/2025 a produs-o in "
              "orice sistem care n-a fost actualizat",
     "aștept": "DIFERA", "lege_conţine": "21"},
    {"clasa": "cota", "nume": "cota micro 5% - valoare care nu exista in niciun act",
     "parametru": "cote/impozit_micro@2023-01-01",
     "schimba": {"valoare_cod": "0.05", "procent_cod": "5"},
     "de_ce": "nu e o cota istorica, e o valoare pur greșita; testeaza daca detectorul cere "
              "potrivirea valorii sau se mulţumeşte cu subiectul",
     "aștept": "DIFERA", "lege_conţine": "1"},
    # ── plafon ────────────────────────────────────────────────────────────────────────────────
    {"clasa": "plafon", "nume": "salariu minim 4050 pe o data din semestrul 2 2026",
     "parametru": "cote/salariu_minim@2026-07-01",
     "schimba": {"valoare_cod": "4050"},
     "de_ce": "valoarea HG 1506/2024, aplicata unei perioade guvernate de HG 146/2026 (4.325) - "
              "clasa 'plafon vechi aplicat unei perioade noi'",
     "aștept": "DIFERA", "lege_conţine": "4.325"},
    # ── termen ────────────────────────────────────────────────────────────────────────────────
    {"clasa": "termen", "nume": "decontul de TVA (D300) scadent pe 20 in loc de 25",
     "parametru": "termen/d300",
     "schimba": {"valoare_cod": "20"},
     "de_ce": "o zi greșita de scadenta - clasa pe care vechiul detector de termene NU o putea "
              "prinde: cauta fraza construita din ziua din cod, deci pentru 20 nu gasea nimic si "
              "iesea NEGASIT, nu DIFERA",
     "aștept": "DIFERA", "lege_conţine": "25"},
    # ── nomenclator ───────────────────────────────────────────────────────────────────────────
    {"clasa": "nomenclator", "nume": "D390 cu un tip de operaţiune inventat (X)",
     "parametru": "nomenclator/d390.TIPURI",
     "schimba": {"valoare_cod": "L,T,A,P,S,R,X"},
     "de_ce": "o valoare IN PLUS in cod. Vechiul prag (>=80% din valori prezente) o lasa sa treaca: "
              "6 din 7 = 86%",
     "aștept": "DIFERA", "doar_in_cod": ["x"], "doar_in_act": []},
    {"clasa": "nomenclator", "nume": "D390 fara tipul R",
     "parametru": "nomenclator/d390.TIPURI",
     "schimba": {"valoare_cod": "L,T,A,P,S"},
     "de_ce": "o valoare pe care norma o enumera, dar codul n-o are - invizibila pentru un detector "
              "care verifica doar ce e in cod",
     "aștept": "DIFERA", "doar_in_cod": [], "doar_in_act": ["r"]},
    # ── cont ──────────────────────────────────────────────────────────────────────────────────
    {"clasa": "cont", "nume": "cont TVA deductibila scris 4262 in loc de 4426",
     "parametru": "cont/4426",
     "schimba": {"valoare_cod": "4262"},
     "de_ce": "cifre inversate intr-un simbol de cont - contul nu exista in niciun plan",
     "aștept": "NEGASIT", "motiv_conţine": "nu apare in niciun plan de conturi"},
    # ── citare ────────────────────────────────────────────────────────────────────────────────
    {"clasa": "citare", "nume": "citare spre actul greșit (CAS 25% cu temei HG 146/2026)",
     "parametru": "cote/cas@2018-01-01",
     "schimba": {"_temei": {"url": "anaf_surse/hg_146_2026_salariu_minim.html",
                            "art": "1", "alin": None}},
     "de_ce": "valoarea din cod e CORECTA (25%), dar temeiul declarat trimite la o hotarare de "
              "salariu minim. Intrebarea nu e 'ce valoare', ci 'proba duce unde spune?'",
     "aștept": "NEGASIT", "motiv_conţine": "Nu se caută in alte acte",
     "citare_rezolvata": False},
]


def _aplica(p, mut):
    q = copy.deepcopy(p)
    for cheie, val in mut["schimba"].items():
        if cheie == "_temei":
            q["temei_declarat"] = dict(q["temei_declarat"] or {})
            q["temei_declarat"].update(val)
        else:
            q[cheie] = val
    return q


def ruleaza(corp=None, plan=None):
    inv = json.load(open(os.path.join(_RAD, "artefacte", "inventar_iconta.json"), encoding="utf-8"))
    dupa_id = {p["id"]: p for p in inv["parametri"]}
    corp = corp or potrivire.Corpus()
    plan = plan if plan is not None else potrivire.plan_de_conturi(corp)

    ies = []
    for mut in MUTATII:
        original = dupa_id[mut["parametru"]]
        mutant = _aplica(original, mut)
        r_orig = potrivire.potriveste(copy.deepcopy(original), corp, plan)
        r_mut = potrivire.potriveste(mutant, corp, plan)
        ies.append({
            "clasa": mut["clasa"],
            "mutaţie": mut["nume"], "de_ce": mut["de_ce"], "parametru": mut["parametru"],
            "aștept": mut["aștept"], "lege_conţine": mut.get("lege_conţine"),
            "motiv_conţine": mut.get("motiv_conţine"),
            "doar_in_cod": mut.get("doar_in_cod"), "doar_in_act": mut.get("doar_in_act"),
            **({"citare_rezolvata": mut["citare_rezolvata"]} if "citare_rezolvata" in mut else {}),
            "valoare_reala_in_cod": original["valoare_cod"],
            "valoare_injectata": mutant["valoare_cod"],
            "original": {"clasificare": r_orig["clasificare"], "atom": r_orig["atom"],
                         "valoare_lege": r_orig["valoare_lege"],
                         "citare_rezolvata": r_orig["citare_rezolvata"]},
            "mutant": {"clasificare": r_mut["clasificare"], "atom": r_mut["atom"],
                       "valoare_lege": r_mut["valoare_lege"],
                       "doar_in_cod": r_mut.get("doar_in_cod"),
                       "doar_in_act": r_mut.get("doar_in_act"),
                       "citare_rezolvata": r_mut["citare_rezolvata"],
                       "ancora": r_mut.get("ancora"), "motiv": r_mut["motiv"],
                       "verbatim": (r_mut["atom_verbatim"] or "")[:400]},
        })
    return ies


def verdict(ies):
    """(trecute, picate) - o mutaţie trece daca iese cum s-a cerut, cu valoarea legii sau motivul corect."""
    trecute, picate = [], []
    for x in ies:
        m = x["mutant"]
        ok = m["clasificare"] == x["aștept"]
        if ok and x.get("lege_conţine") is not None:
            ok = x["lege_conţine"] in str(m["valoare_lege"] or "").lower() + str(
                m.get("doar_in_act") or "") + str(m.get("doar_in_cod") or "")
        if ok and x.get("motiv_conţine"):
            ok = x["motiv_conţine"] in (m["motiv"] or "")
        # la nomenclatoare conteaza PARTEA diferenţei: o valoare in plus in cod nu e acelasi defect
        # cu una lipsa din cod, si detectorul trebuie sa spuna care din ele
        if ok and x.get("doar_in_cod") is not None:
            ok = (m.get("doar_in_cod") == x["doar_in_cod"]
                  and m.get("doar_in_act") == x["doar_in_act"])
        if ok and "citare_rezolvata" in x:
            ok = m["citare_rezolvata"] is x["citare_rezolvata"]
        (trecute if ok else picate).append(x)
    return trecute, picate


def _ca_raport():
    """Contractul pe care `ruleaza_tot.py` il asteapta de la fiecare pas: un dict cu rezumat.

    Scrie si `artefacte/banc_mutatii.json`, pe care raportul il citeste la §9.
    """
    ies = ruleaza()
    trecute, picate = verdict(ies)
    rap = {"_ce": "OP7b dovada in cealalta direcţie: greșeli cunoscute injectate pe o COPIE a "
                  "inventarului (niciodata in iConta), pentru a arata ca detectorul poate produce "
                  "DIFERA.",
           "n_trec": len(trecute), "n_pica": len(picate), "mutaţii": ies}
    with open(os.path.join(_RAD, "artefacte", "banc_mutatii.json"), "w", encoding="utf-8") as f:
        json.dump(rap, f, ensure_ascii=False, indent=1)
    return rap


if __name__ == "__main__":
    import time
    t0 = time.time()
    ies = ruleaza()
    tr, pi = verdict(ies)
    for x in ies:
        m = x["mutant"]
        stare = "TRECE" if x in tr else "PICĂ"
        print("[%s] %s" % (stare, x["mutaţie"]))
        print("      [%s] cod real %s -> injectat %s | aștept %s"
              % (x["clasa"], x["valoare_reala_in_cod"], x["valoare_injectata"], x["aștept"]))
        print("      ieșit: %s | lege=%s | citare_rezolvata=%s"
              % (m["clasificare"], m["valoare_lege"], m["citare_rezolvata"]))
        print("      atom: %s" % m["atom"])
        print("      motiv: %s" % m["motiv"][:160])
        print()
    print("%d trec / %d pică  (%.1f s)" % (len(tr), len(pi), time.time() - t0))
    with open(os.path.join(_RAD, "artefacte", "banc_mutatii.json"), "w", encoding="utf-8") as f:
        json.dump({"n_trec": len(tr), "n_pica": len(pi), "mutaţii": ies}, f,
                  ensure_ascii=False, indent=1)
    raise SystemExit(1 if pi else 0)
