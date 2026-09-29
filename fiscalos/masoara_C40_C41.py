# -*- coding: utf-8 -*-
"""Efectul verificarilor C40 (termene) si C41 (temeiul alaturat) pe propunerile SALVATE ale setului 2 -
fara niciun apel. Navigarea se reia determinist din pasii salvati (corpusul e acelasi ca la 485ffc3), ca
verificarea sa vada exact atomii aratati modelului. LIMITA SUPERIOARA a abtinerilor noi: propunerile vechi
nu aveau campul `alegeri_temei`, iar promptul nu cerea termen_efectiv - un model care stie regulile ar
raspunde altfel. Scorul oficial al setului 2 nu se schimba."""
import json
import os

from fiscalos import intrebari, navigare

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def masoara():
    d = json.load(open(os.path.join(_RAD, "intrebari", "final", "raspunsuri_set2.json"), encoding="utf-8"))
    idx = intrebari.Index()
    ies = {}
    for r in d["raspunsuri"]:
        if r["stare"] != "RASPUNS":
            continue
        nav = navigare.Navigator(idx, idx.rel, max([x[0] for x in r["date_din_intrebare"]] or
                                                   [intrebari.DATA_INTREBARII]))
        for p in r["apel"]["pasi"]:
            nav.executa(p["unealta"], p["intrare"])
        p = r["propunerea_modelului"]
        corp = r["raspuns"].split("  [calcul:")[0]
        ok = {c["rezultat"] for c in r.get("calcule") or [] if "termen_efectiv" in c["formula"]}
        c40 = navigare.verifica_termene(corp, r["intrebare"], ok)
        c41 = navigare.verifica_alegeri_temei(dict(p, alegeri_temei=p.get("alegeri_temei") or []), nav.vazuti)
        if c40 or c41:
            ies[r["id"]] = {"C40": c40, "C41": c41}
    return ies


if __name__ == "__main__":
    print(json.dumps(masoara(), ensure_ascii=False, indent=1))
