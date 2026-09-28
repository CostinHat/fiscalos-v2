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
# `valoare` = valoarea GREȘITA injectata. `lege` = ce trebuie sa raporteze detectorul din text.
MUTATII = [
    {
        "nume": "dividende 10% in loc de 16%",
        "parametru": "cote/impozit_dividend@2026-01-01",
        "schimba": {"valoare_cod": "0.10", "procent_cod": "10"},
        "de_ce": "cota reala din 2025 (OUG 156/2024), rămasa in cod dupa ce Legea 141/2025 a urcat-o "
                 "la 16% de la 01.01.2026 - clasa 'cota veche rămasa in cod'",
        "aștept": "DIFERA", "lege_conţine": "16",
    },
    {
        "nume": "TVA standard 19% in loc de 21%",
        "parametru": "cote/tva_standard@2025-08-01",
        "schimba": {"valoare_cod": "0.19", "procent_cod": "19"},
        "de_ce": "cota de dinainte de 01.08.2025; exact greșeala pe care Legea 141/2025 a produs-o "
                 "in orice sistem care n-a fost actualizat",
        "aștept": "DIFERA", "lege_conţine": "21",
    },
    {
        "nume": "salariu minim 4050 pe o data din semestrul 2 2026",
        "parametru": "cote/salariu_minim@2026-07-01",
        "schimba": {"valoare_cod": "4050"},
        "de_ce": "valoarea HG 1506/2024, aplicata unei perioade guvernate de HG 146/2026 (4.325) - "
                 "clasa 'plafon vechi aplicat unei perioade noi'",
        "aștept": "DIFERA", "lege_conţine": "4.325",
    },
    {
        "nume": "cota micro 5% - valoare care nu exista in niciun act",
        "parametru": "cote/impozit_micro@2023-01-01",
        "schimba": {"valoare_cod": "0.05", "procent_cod": "5"},
        "de_ce": "nu e o cota istorica, e o valoare pur greșita; testeaza daca detectorul cere "
                 "potrivirea valorii sau se mulţumeşte cu subiectul",
        "aștept": "DIFERA", "lege_conţine": "1",
    },
    {
        "nume": "citare spre actul greșit (CAS 25% cu temei HG 146/2026)",
        "parametru": "cote/cas@2018-01-01",
        "schimba": {"_temei": {"url": "anaf_surse/hg_146_2026_salariu_minim.html",
                               "art": "1", "alin": None}},
        "de_ce": "valoarea din cod e CORECTA (25%), dar temeiul declarat trimite la o hotarare de "
                 "salariu minim. Intrebarea nu e 'ce valoare', ci 'proba duce unde spune?'",
        "aștept": "de_raportat", "lege_conţine": None,
    },
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
            "mutaţie": mut["nume"], "de_ce": mut["de_ce"], "parametru": mut["parametru"],
            "aștept": mut["aștept"], "lege_conţine": mut["lege_conţine"],
            "valoare_reala_in_cod": original["valoare_cod"],
            "valoare_injectata": mutant["valoare_cod"],
            "original": {"clasificare": r_orig["clasificare"], "atom": r_orig["atom"],
                         "valoare_lege": r_orig["valoare_lege"],
                         "citare_rezolvata": r_orig["citare_rezolvata"]},
            "mutant": {"clasificare": r_mut["clasificare"], "atom": r_mut["atom"],
                       "valoare_lege": r_mut["valoare_lege"],
                       "citare_rezolvata": r_mut["citare_rezolvata"],
                       "ancora": r_mut.get("ancora"), "motiv": r_mut["motiv"],
                       "verbatim": (r_mut["atom_verbatim"] or "")[:400]},
        })
    return ies


def verdict(ies):
    """(trecute, picate) - o mutaţie trece daca iese cum s-a cerut, cu valoarea legii alaturi."""
    trecute, picate = [], []
    for x in ies:
        m = x["mutant"]
        if x["aștept"] == "DIFERA":
            ok = (m["clasificare"] == "DIFERA"
                  and x["lege_conţine"] in str(m["valoare_lege"] or ""))
        else:
            ok = m["citare_rezolvata"] is False        # citarea greșita trebuie SEMNALATA
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
        print("      cod real %s -> injectat %s | aștept %s"
              % (x["valoare_reala_in_cod"], x["valoare_injectata"], x["aștept"]))
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
