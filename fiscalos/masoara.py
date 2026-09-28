# -*- coding: utf-8 -*-
"""Masurarea unei versiuni a motorului: ruleaza TOATE cele 50 de intrebari, compara, scrie scorul.

Folosit la fiecare reparaţie de CLASA: scorul inainte si dupa se masoara pe acelasi set intreg, nu pe
intrebarea care a sugerat reparaţia. `artefacte/intrebari/istoric_scor.json` pastreaza sirul.
"""
import json
import os
import shutil
import sys
import time

from fiscalos import comparatie, intrebari

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_D = os.path.join(_RAD, "artefacte", "intrebari")


def masoara(eticheta, descriere):
    t0 = time.time()
    r = intrebari.ruleaza()
    t_motor = time.time() - t0
    fis = os.path.join(_D, "raspunsuri_%s.json" % eticheta)
    shutil.copy(os.path.join(_D, "raspunsuri.json"), fis)
    t1 = time.time()
    c = comparatie.compara(fis)
    t_comp = time.time() - t1
    with open(os.path.join(_D, "comparatie_%s.json" % eticheta), "w", encoding="utf-8") as f:
        json.dump(c, f, ensure_ascii=False, indent=1)
    ist_f = os.path.join(_D, "istoric_scor.json")
    ist = json.load(open(ist_f, encoding="utf-8")) if os.path.exists(ist_f) else []
    ist = [x for x in ist if x["eticheta"] != eticheta]
    ist.append({"eticheta": eticheta, "descriere": descriere, "scor": c["scor"],
                "raspunse": r["raspunse"], "nu_pot_motor": r["nu_pot"],
                "corecte": sorted(x["id"] for x in c["comparatii"] if x["verdict"] == "CORECT"),
                "secunde_motor": round(t_motor, 2), "secunde_comparatie": round(t_comp, 2),
                "masurat_la": time.strftime("%Y-%m-%dT%H:%M:%S")})
    with open(ist_f, "w", encoding="utf-8") as f:
        json.dump(ist, f, ensure_ascii=False, indent=1)
    return c["scor"], ist[-1]


if __name__ == "__main__":
    s, x = masoara(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "")
    print("%-10s %s | corecte: %s | motor %.1fs" % (sys.argv[1], s, x["corecte"], x["secunde_motor"]))
