# -*- coding: utf-8 -*-
"""Lanţul intreg, cu DURATA MASURATA a fiecarei operatii: `python3 ruleaza_tot.py`.

Duratele nu se scriu de mana in raport - se masoara aici si raportul le citeste din `durate.json`.
Un numar scris de mana intr-un raport e o afirmaţie; unul masurat de scriptul care a facut lucrarea
e o observaţie.
"""
import json
import os
import time

_RAD = os.path.dirname(os.path.abspath(__file__))

PASI = [
    ("OP2 instantaneu corpus + manifest SHA", "fiscalos.corpus_snapshot", "instantaneu"),
    ("OP3 strat de text (txt/html/pdf)", "fiscalos.strat_text", "construieste"),
    ("OP4 atomizare structurala", "fiscalos.atomizare", "atomizeaza_tot"),
    ("OP5 inventar parametri iConta (citire)", "fiscalos.inventar_iconta", "inventariaza"),
    ("OP6+OP7 potrivire si clasificare", "fiscalos.potrivire", "potriveste_tot"),
    ("OP7b banc de mutatii (dovada inversa)", "fiscalos.banc_mutatii", "_ca_raport"),
]


def ruleaza():
    import importlib
    durate = []
    for eticheta, modul, functie in PASI:
        m = importlib.import_module(modul)
        t0 = time.time()
        rez = getattr(m, functie)()
        d = time.time() - t0
        rezumat = {k: v for k, v in rez.items()
                   if k in ("n_trec", "n_pica", "n_fisiere", "octeti_total", "n_acte_cu_text", "n_neextractibile",
                            "n_acte", "n_atomi", "n_acte_pe_articole", "n_acte_pe_fragmente",
                            "n_parametri", "pe_clasa", "sumar", "citari_declarate",
                            "citari_rezolvate", "n_conturi_in_plan_din_corpus")}
        durate.append({"operatie": eticheta, "secunde": round(d, 2), "rezumat": rezumat})
        print("%-42s %6.2f s  %s" % (eticheta, d, rezumat))

    t0 = time.time()
    import probe
    cod = probe.ruleaza()
    durate.append({"operatie": "Probe pe corpus", "secunde": round(time.time() - t0, 2),
                   "rezumat": {"cod_ieșire": cod}})

    with open(os.path.join(_RAD, "artefacte", "durate.json"), "w", encoding="utf-8") as f:
        json.dump({"masurat_la": time.strftime("%Y-%m-%dT%H:%M:%S"),
                   "total_secunde": round(sum(d["secunde"] for d in durate), 2),
                   "pasi": durate}, f, ensure_ascii=False, indent=1)
    return durate


if __name__ == "__main__":
    ruleaza()
