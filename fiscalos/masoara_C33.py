# -*- coding: utf-8 -*-
"""C33 (gasit la citirea rularii v5, NEAPLICAT): la reemiterea ceruta de C23, modelul scrie diacriticele
ca secvente literale "\\u0103". Masuratoarea: aceleasi propuneri salvate, cu secventele decodate, trecute
prin ACEEASI verificare - fara niciun apel. Navigarea se reia determinist din pasii salvati, ca
verificarea sa vada exact atomii aratati modelului. Scorul raportat ramane cel masurat; asta e doar
efectul unei reparatii de decis."""
import json
import os
import re

from fiscalos import comparatie, intrebari, navigare, semantic

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_ESC = re.compile(r"\\u([0-9a-fA-F]{4})")


def _decodeaza(x):
    if isinstance(x, str):
        return _ESC.sub(lambda m: chr(int(m.group(1), 16)), x)
    if isinstance(x, dict):
        return {k: _decodeaza(v) for k, v in x.items()}
    if isinstance(x, list):
        return [_decodeaza(v) for v in x]
    return x


def masoara():
    fis = os.path.join(_RAD, "intrebari", "v5", "raspunsuri_navigare.json")
    d = json.load(open(fis, encoding="utf-8"))
    idx = intrebari.Index()
    Q = {q["id"]: q for q in intrebari.incarca_intrebari()}
    afectate, ies = [], []
    for r in d["raspunsuri"]:
        p = r.get("propunerea_modelului")
        if not p or not _ESC.search(json.dumps(p, ensure_ascii=False)):
            ies.append(r)
            continue
        afectate.append(r["id"])
        nav = navigare.Navigator(idx, idx.rel, max([x[0] for x in r["date_din_intrebare"]] or
                                                   [intrebari.DATA_INTREBARII]))
        for pas in r["apel"]["pasi"]:
            nav.executa(pas["unealta"], pas["intrare"])
        final = _decodeaza(p)
        baza = {k: r[k] for k in ("id", "tip", "intrebare", "date_din_intrebare", "strat")}
        baza["data_referinta"] = final["data_referinta"]
        rez = semantic.finalizeaza(baza, final, list(nav.vazuti.values()), Q[r["id"]],
                                   final["data_referinta"], nav.relatie, r["apel"])
        if final.get("calcule") and rez["stare"] == "RASPUNS":
            valori, gr, det = navigare.evalueaza_calcule(final["calcule"], nav.vazuti, r["intrebare"])
            if gr:
                rez = dict(rez, stare="NU_POT_RASPUNDE", raspuns=None, motiv="calcul: " + "; ".join(gr))
            else:
                t = rez["raspuns"]
                for k, v in valori.items():
                    t = t.replace("{%s}" % k, v)
                rez["raspuns"] = t + "  [calcul: " + "; ".join(navigare.pas_cu_pas(det)) + "]"
        ies.append(rez)
    dest = os.path.join(_RAD, "intrebari", "v5", "masura_C33_raspunsuri.json")
    json.dump(dict(d, raspunsuri=ies), open(dest, "w", encoding="utf-8"), ensure_ascii=False, indent=1,
              default=str)
    inainte = comparatie.compara(fis)
    dupa = comparatie.compara(dest)
    V = {c["id"]: c["verdict_pe_fond"] for c in dupa["comparatii"]}
    rez = {"afectate": afectate, "inainte": inainte["scor_referinta_pe_fond"],
           "dupa": dupa["scor_referinta_pe_fond"], "verdict_dupa": {i: V[i] for i in afectate},
           "motiv_dupa": {r["id"]: (r.get("motiv") or "")[:200] for r in ies if r["id"] in afectate}}
    json.dump(rez, open(os.path.join(_RAD, "intrebari", "v5", "masura_C33.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    return rez


if __name__ == "__main__":
    print(json.dumps(masoara(), ensure_ascii=False, indent=1))
