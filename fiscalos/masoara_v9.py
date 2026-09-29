# -*- coding: utf-8 -*-
"""Efectul C49 (justificarea geamanului numai pentru atomul decisiv), C50 (procentul impartit la 100) si
C51 (ordinale, cifra + unitate) pe propunerile SALVATE ale seturilor 2 si 3 - fara niciun apel.

Navigarea se reia determinist din pasii salvati; fiecare propunere trece prin `verifica_propunerea`
(verificarea de acum), apoi prin comparatorul neschimbat. C52 (tura de reparatie) cere modelul si NU se
poate masura aici. Scorurile oficiale ale seturilor nu se schimba: rezultatul e o RE-NOTARE."""
import json
import os
import time

from fiscalos import comparatie, intrebari, navigare

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETURI = {"set2": ("intrebari/final/raspunsuri_set2.json", "/home/costin/ghid_incoming/FiscalOS_intrebari_set2_50.csv"),
          "set3": ("intrebari/set3/raspunsuri_set3.json", "/home/costin/ghid_incoming/FiscalOS_intrebari_set3_50.csv")}


def reverifica(nume, idx):
    fis, csv = SETURI[nume]
    d = json.load(open(os.path.join(_RAD, fis), encoding="utf-8"))
    Q = {q["id"]: q for q in intrebari.incarca_intrebari(csv)}
    ies = []
    for r in d["raspunsuri"]:
        p = r.get("propunerea_modelului")
        if not p:
            ies.append(r)
            continue
        date = r["date_din_intrebare"]
        admise = [x[0] for x in date] or [intrebari.DATA_INTREBARII]
        nav = navigare.Navigator(idx, idx.rel, max(admise))
        for pas in r["apel"]["pasi"]:
            nav.executa(pas["unealta"], pas["intrare"])
        # propunerile setului 2 nu aveau campul C41; lipsa lui = nicio justificare
        p = dict(p, alegeri_temei=p.get("alegeri_temei") or [])
        baza = {k: r[k] for k in ("id", "tip", "intrebare", "date_din_intrebare", "strat")}
        ies.append(navigare.verifica_propunerea(p, baza, Q[r["id"]], nav, admise, max(admise), r["apel"],
                                                r.get("traseu", "")))
    dest = os.path.join(_RAD, "intrebari", "v9", "reverificat_%s.json" % nume)
    json.dump(dict(d, raspunsuri=ies), open(dest, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
    return d, ies, dest, csv


def masoara():
    os.makedirs(os.path.join(_RAD, "intrebari", "v9"), exist_ok=True)
    t0 = time.time()
    idx = intrebari.Index()
    rez = {}
    for nume in ("set2", "set3"):
        d, ies, dest, csv = reverifica(nume, idx)
        inainte = comparatie.compara(os.path.join(_RAD, SETURI[nume][0]), csv_cheie=csv)
        dupa = comparatie.compara(dest, csv_cheie=csv)
        A = {x["id"]: x["verdict_pe_fond"] for x in inainte["comparatii"]}
        B = {x["id"]: x["verdict_pe_fond"] for x in dupa["comparatii"]}
        R = {r["id"]: r for r in ies}
        rez[nume] = {"inainte": inainte["scor_referinta_pe_fond"], "dupa": dupa["scor_referinta_pe_fond"],
                     "schimbari": [(i, A[i], B[i], (R[i].get("motiv") or "")[:220]) for i in A if A[i] != B[i]]}
    rez["secunde"] = round(time.time() - t0, 1)
    json.dump(rez, open(os.path.join(_RAD, "intrebari", "v9", "masura_C49_C51.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    return rez


if __name__ == "__main__":
    r = masoara()
    for n in ("set2", "set3"):
        print(n, r[n]["inainte"], "->", r[n]["dupa"])
        for x in r[n]["schimbari"]:
            print("   ", x[0], x[1], "->", x[2], "|", x[3][:150])
    print(r["secunde"], "s")
