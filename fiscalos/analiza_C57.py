# -*- coding: utf-8 -*-
"""C57 (PROPUNERE, neimplementata): "orice valoare numerica din raspuns trebuie sprijinita de un atom citat
care o contine". Analiza pe raspunsurile ACCEPTATE salvate - ce ar fi schimbat regula, fara niciun apel.

Ce exista azi (semantic.verifica): o valoare legala (C13) trebuie sa apara intr-un citat; orice alta cifra,
in citate SAU in intrebare - iar comparatia e pe SUBSIR ("5" trece daca citatul are "4.325").
Regula propusa, in doua variante masurate:
  (a) STRICTA - fiecare numar din raspuns apare, ca numar INTREG (granite de cifra), intr-un fragment citat,
      sau e rezultatul unui calcul evaluat de cod; un numar luat numai din intrebare NU e sprijinit;
  (b) cu exceptia faptelor cazului - ca (a), dar un numar aflat literal in intrebare e permis (FAPT_CAZ)."""
import json
import os
import re

from fiscalos import comparatie, semantic

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETURI = {"set3": ("intrebari/set3/raspunsuri_set3.json", "/home/costin/ghid_incoming/FiscalOS_intrebari_set3_50.csv"),
          "set4": ("intrebari/set4/raspunsuri_set4.json", "/home/costin/ghid_incoming/FiscalOS_intrebari_set4_50.csv")}


def _intreg(num, text):
    return re.search(r"(?<![\d.,])%s(?![\d]|[.,]\d)" % re.escape(num), text) is not None


def nesprijinite(r):
    corp = re.split(r"  \[(?:calcul|avertisment|data de referință)", r["raspuns"])[0]
    corp = semantic._ID_ACT.sub(" ", semantic._TRIMITERE.sub(" ", corp))
    citate = " ".join(semantic._n(a["verbatim"]) for a in r.get("argument") or [])
    rezultate = {d["rezultat"] for d in r.get("calcule") or []}
    q = semantic._n(r["intrebare"])
    strict, cu_fapte = [], []
    for m in semantic._CIFRA.finditer(corp):
        n = m.group(0).rstrip(".,")
        if n in rezultate or _intreg(n, citate):
            continue
        strict.append(n)
        if not _intreg(n, q):
            cu_fapte.append(n)
    return sorted(set(strict)), sorted(set(cu_fapte))


def analizeaza(nume):
    fis, csv = SETURI[nume]
    d = json.load(open(os.path.join(_RAD, fis), encoding="utf-8"))
    C = {x["id"]: x["verdict_pe_fond"] for x in comparatie.compara(os.path.join(_RAD, fis), csv_cheie=csv)["comparatii"]}
    ies = []
    for r in d["raspunsuri"]:
        if r["stare"] != "RASPUNS":
            continue
        a, b = nesprijinite(r)
        if a:
            ies.append({"id": r["id"], "verdict": C[r["id"]], "nesprijinite_strict": a, "nesprijinite_fara_fapte": b})
    return ies


if __name__ == "__main__":
    import sys
    for n in sys.argv[1:] or ["set3"]:
        rez = analizeaza(n)
        print(n, len(rez))
        for x in rez:
            print("  ", x["id"], x["verdict"], "| strict:", x["nesprijinite_strict"], "| fara fapte:", x["nesprijinite_fara_fapte"])
