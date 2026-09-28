# -*- coding: utf-8 -*-
"""Masurarea separata a celor doua cauze (decizia 7), pe motorul LEXICAL: e determinist si gratuit,
deci efectul fiecarei schimbari se masoara exact, prin ablatie pe aceleasi 50 de intrebari:
  L0  instantaneul iConta, fara relatia C17        (starea de dinainte)
  L1  + stratul de surse oficiale (C12)
  L2  + relatia de derogare C17 (plasa de siguranta b)
"""
import json
import os
import time

from fiscalos import comparatie, intrebari, potrivire

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(_RAD, "artefacte", "intrebari")
CONFIG = [("L0", False, False, "instantaneul iConta, fara relatia C17"),
          ("L1", True, False, "+ consolidatele oficiale (C12)"),
          ("L2", True, True, "+ relatia de derogare C17 (b)")]


def ruleaza():
    qs = intrebari.incarca_intrebari()
    ies = {}
    for et, oficiale, rel, desc in CONFIG:
        t0 = time.time()
        idx = intrebari.Index(potrivire.Corpus(oficiale=oficiale), relatii_c17=rel)
        R = [intrebari.raspunde(q, idx) for q in qs]
        f = os.path.join(DEST, "raspunsuri_lexical_%s.json" % et)
        json.dump({"config": desc, "raspunsuri": R}, open(f, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        C = comparatie.compara(f)
        ies[et] = {"descriere": desc, "scor_pe_fond": C["scor_referinta_pe_fond"],
                   "secunde": round(time.time() - t0, 2),
                   "stare": {r["id"]: r["stare"] for r in R},
                   "verdict": {c["id"]: c["verdict_pe_fond"] for c in C["comparatii"]}}
        print("%s %-42s %s  %.1fs" % (et, desc, C["scor_referinta_pe_fond"], ies[et]["secunde"]))
    tranz = {}
    for a, b in (("L0", "L1"), ("L1", "L2")):
        sa, sb, vb = ies[a]["stare"], ies[b]["stare"], ies[b]["verdict"]
        tranz["%s->%s" % (a, b)] = {
            "abtineri_disparute": sorted(k for k in sa if sa[k] != "RASPUNS" and sb[k] == "RASPUNS"),
            "abtineri_aparute": sorted(k for k in sa if sa[k] == "RASPUNS" and sb[k] != "RASPUNS"),
            "din_care_corecte_acum": sorted(k for k in sa if sa[k] != "RASPUNS" and sb[k] == "RASPUNS"
                                            and vb[k] == "CORECT"),
            "raspunsuri_retrase_care_erau_gresite": sorted(
                k for k in sa if sa[k] == "RASPUNS" and sb[k] != "RASPUNS"
                and ies[a]["verdict"][k] == "GRESIT"),
            "raspunsuri_retrase_care_erau_corecte": sorted(
                k for k in sa if sa[k] == "RASPUNS" and sb[k] != "RASPUNS"
                and ies[a]["verdict"][k] == "CORECT")}
    rez = {"config": {k: {x: v[x] for x in ("descriere", "scor_pe_fond", "secunde")}
                      for k, v in ies.items()}, "tranzitii": tranz}
    json.dump(rez, open(os.path.join(DEST, "ablatie_lexical.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    return rez


if __name__ == "__main__":
    r = ruleaza()
    print(json.dumps(r["tranzitii"], ensure_ascii=False, indent=1))
