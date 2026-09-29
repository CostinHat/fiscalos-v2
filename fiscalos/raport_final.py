# -*- coding: utf-8 -*-
"""Masuratoarea finala: setul 2 (50 de intrebari noi), versiunea 485ffc3, comparator neschimbat.

Raspunsurile au fost comise (8b3269f) INAINTE de orice citire a cheii. Nimic nu s-a reparat dupa
comparatie; defectele sunt cerinte (fisierul cerinte_final.md). Lectura pe fond a fiecarui GRESIT e in
lectura_final.json, marcata ca lectura (de verificat de om)."""
import json
import os
import time
from collections import Counter

from fiscalos import intrebari

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(_RAD, "intrebari", "final")
ZIP = "/home/costin/ghid_incoming/fiscalos_masuratoare_finala.zip"
SET2 = "/home/costin/ghid_incoming/FiscalOS_intrebari_set2_50.csv"
ET = {"CORECT": "CORECT", "GRESIT": "GREȘIT", "NU_POT": "NU POT"}


def _s(t, n=140):
    t = " ".join(str(t or "").split())
    return (t[:n] + "…") if len(t) > n else t


def construieste():
    t0 = time.time()
    os.makedirs(os.path.join(DEST, "raspunsuri"), exist_ok=True)
    nav = json.load(open(os.path.join(DEST, "raspunsuri_set2.json"), encoding="utf-8"))
    C = json.load(open(os.path.join(DEST, "comparatie_set2.json"), encoding="utf-8"))
    lec = json.load(open(os.path.join(_RAD, "fiscalos", "lectura_final.json"), encoding="utf-8"))
    R = {r["id"]: r for r in nav["raspunsuri"]}
    V = {c["id"]: c for c in C["comparatii"]}
    s = C["scor_referinta_pe_fond"]
    fond = [i for i, v in lec.items() if v["fel"] == "fond"]
    qs = intrebari.incarca_intrebari(SET2)
    for q in qs:
        r, c = R[q["id"]], V[q["id"]]
        L = ["# %s — %s" % (q["id"], q["tip"]), "", "**Întrebarea:** %s" % q["intrebare"], "",
             "## Răspunsul — %s" % ("RĂSPUNS" if r["stare"] == "RASPUNS" else "NU POT RĂSPUNDE"), "",
             "*%s*" % (r.get("declaratie") or "—"), ""]
        if r["stare"] == "RASPUNS":
            L += ["> **%s**" % _s(r["raspuns"], 2000), ""]
        L += ["Motiv: %s" % _s(r["motiv"], 1200), ""]
        for d in r.get("calcule") or []:
            for z in d.get("zile") or []:
                L += ["- `%s`" % z]
            L += ["- `%s = %s` = %s = **%s**" % (d["nume"], d["formula"], d.get("cu_valori", ""), d["rezultat"])]
        for a in r.get("argument") or []:
            L += ["- **%s** — `%s`" % (a["temei"], a["atom"]), "  > %s" % _s(a["verbatim"], 500)]
        ap = r["apel"]
        L += ["", "Navigare: %d pași; `%s`; %s tokeni; $%.4f; %.0f s" % (
            ap["pasi_navigare"], ap["model"], ap["tokeni"], ap["cost_usd"], ap["secunde"]), "",
              "Pe fond (comparator): **%s** — %s" % (ET[c["verdict_pe_fond"]], _s(c["de_ce"], 300))]
        if q["id"] in lec:
            L += ["", "Lectura pe fond: **%s** (%s) — %s" % (lec[q["id"]]["fel"], lec[q["id"]]["clasa"],
                                                             lec[q["id"]]["de_ce"])]
        L += ["", "## Cheia", "", "- %s" % c["raspuns_asteptat"], "- temei: %s" % c["temei_asteptat"]]
        open(os.path.join(DEST, "raspunsuri", "%s.md" % q["id"]), "w", encoding="utf-8").write("\n".join(L) + "\n")

    L = []
    A = L.append
    A("# FiscalOS v2 — Măsurătoarea finală, setul 2")
    A("")
    A("Generat %s · ZIP: `%s`" % (time.strftime("%d.%m.%Y %H:%M"), ZIP))
    A("")
    A("Versiunea motorului: **485ffc3**, neschimbată (după, s-au schimbat numai probele). Răspunsurile au "
      "fost comise (**8b3269f**) înainte de orice citire a cheii. Comparatorul, neschimbat. Nicio reparație "
      "după comparație.")
    A("")
    A("## Cifra principală: greșelile de fond")
    A("")
    A("**%d** din 50 (din %d răspunsuri date). Fiecare, citită (lectura mea, de verificat de om):" % (
        len(fond), nav["raspunse"]))
    A("")
    for i in fond:
        A("- **%s** (%s) — *%s*. %s" % (i, V[i]["tip"], lec[i]["clasa"], lec[i]["de_ce"]))
    A("")
    A("## Scorul pe fond (cifra finală)")
    A("")
    A("| | CORECT | GREȘIT | NU POT |")
    A("|---|---|---|---|")
    A("| **Setul 2 (nou), comparator neschimbat** | **%d** | **%d** | **%d** |" % (s["CORECT"], s["GRESIT"], s["NU_POT"]))
    A("")
    A("Cele %d GREȘIT ale comparatorului, citite pe fond: %d greșeli de fond; %d corecte pe fond, notate GREȘIT "
      "de comparator (C42: %s); %d corecte la întrebarea pusă, fără faptul pe care cheia îl pune primul (C43: %s). "
      "Scorul **nu** a fost ajustat pe baza lecturii." % (
          s["GRESIT"], len(fond),
          sum(1 for v in lec.values() if v["fel"].startswith("comparator")),
          ", ".join(i for i, v in lec.items() if v["fel"].startswith("comparator")),
          sum(1 for v in lec.values() if v["fel"].startswith("incomplet")),
          ", ".join(i for i, v in lec.items() if v["fel"].startswith("incomplet"))))
    A("")
    A("Pe tipuri:")
    A("")
    A("| Tip | CORECT | GREȘIT | NU POT |")
    A("|---|---|---|---|")
    for t in ("PARAMETRU", "REGULA", "CALCUL", "CAPCANA", "PROCEDURA", "INCOMPLETA"):
        cc = Counter(c["verdict_pe_fond"] for c in C["comparatii"] if c["tip"] == t)
        A("| %s | %d | %d | %d |" % (t, cc["CORECT"], cc["GRESIT"], cc["NU_POT"]))
    A("")
    A("**INCOMPLETA** (C1: orice abținere e NU POT în scorul pe fond; se raportează separat): %s." % "; ".join(
        "%s — %s" % (x["id"], "incompletitudine detectată" if x["incompletitudine_detectata"] else "respins de verificare")
        for x in C["abtineri_pe_INCOMPLETA"]))
    A("")
    A("**Abțineri (NU POT), pe cauze:**")
    A("")
    for r in nav["raspunsuri"]:
        if r["stare"] != "RASPUNS" and r["tip"] != "INCOMPLETA":
            A("- %s (%s): %s" % (r["id"], r["tip"], _s(r["motiv"], 220)))
    A("")
    A("## Chei care par greșite")
    A("")
    A("Niciuna. Cheile celor 7 GREȘIT au fost confruntate cu atomii: Q2-TVA-05 (CF art. 319 alin. (3) — "
      "confirmat de atom), Q2-CTB-05 (31.05.2026 duminică, 01.06.2026 = 1 iunie și a doua zi de Rusalii — "
      "confirmat de calendarul C32/C38), celelalte pe temeiul pe care îl citează și răspunsul.")
    A("")
    A("## Setul 1, pentru comparație")
    A("")
    A("Scorul setului 1 cu **aceeași** versiune (485ffc3) nu se poate obține fără o rulare plătită: ieșirile "
      "salvate ale setului 1 sunt produse de versiunea v5 (778e826), iar între timp s-au schimbat corpusul "
      "(C31, C36 — 48 de acte oficiale, conversia) și calculul (C32, C38). Cel mai apropiat scor din ieșirile "
      "salvate, fără apel: **37/2/11** (v5 + decodarea C33 + comparatorul C30, fiecare pe corpusul rulării).")
    A("")
    A("| | CORECT | GREȘIT | NU POT |")
    A("|---|---|---|---|")
    A("| Setul 1 (expus), v5 + C33 + C30, din ieșirile salvate | 37 | 2 | 11 |")
    A("| **Setul 2 (nou), 485ffc3** | **%d** | **%d** | **%d** |" % (s["CORECT"], s["GRESIT"], s["NU_POT"]))
    A("")
    A("---")
    A("")
    A(open(os.path.join(_RAD, "fiscalos", "cerinte_final.md"), encoding="utf-8").read().strip())
    A("")
    A("---")
    A("")
    A("## Operațiile, cu durata și costul măsurate")
    A("")
    A("| Operație | Durată | Cost |")
    A("|---|---|---|")
    A("| Setul 2: 50 de întrebări, %d ture la `%s` (%s tokeni) | %.1f s | $%.4f |" % (
        sum(r["apel"]["tururi"] for r in nav["raspunsuri"]), nav["model"], nav["tokeni"], nav["secunde_total"],
        nav["cost_usd"]))
    A("| Apeluri de control al creditului (2 × 8+5 tokeni) | — | ~$0.0004 |")
    A("| Prima pornire, oprită: fișierul setului 2 lipsea (niciun apel) | — | $0 |")
    A("| Comparația, lectura, raportul | %.1f s | $0 |" % (time.time() - t0))
    A("")
    A("Pași de navigare: %.1f în medie; la limita de 20: %d; reîncercări C23: %d (%s); model de rezervă: %s." % (
        nav["pasi_medii"], len(nav["la_limita_de_pasi_C29"]), len(nav["reincercari_C23"]),
        ", ".join(nav["reincercari_C23"]), ", ".join(nav["de_la_modelul_de_rezerva"]) or "niciodată"))
    A("")
    A("## Cele 50 de întrebări")
    A("")
    A("| Id | Tip | Pe fond | Lectura | Răspunsul |")
    A("|---|---|---|---|---|")
    for q in qs:
        r = R[q["id"]]
        A("| %s | %s | %s | %s | %s |" % (q["id"], q["tip"], ET[V[q["id"]]["verdict_pe_fond"]],
                                          lec.get(q["id"], {}).get("fel", ""),
                                          _s(r["raspuns"], 80) if r["stare"] == "RASPUNS" else "*%s*" % _s(r["motiv"], 70)))
    open(os.path.join(DEST, "RAPORT.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    return s, fond


if __name__ == "__main__":
    print(construieste())
