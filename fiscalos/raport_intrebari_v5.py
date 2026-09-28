# -*- coding: utf-8 -*-
"""Livrabilul motorului de intrebari v5: deciziile C23-C29 aplicate, rulat pe cele 50 (INDICATIV).
intrebari/v1..v4 raman neatinse.

Raportate SEPARAT:
  - C28: scorul inainte si dupa repararea comparatorului, pe fiecare rulare (v2, v3, v4, lexical);
  - C24: efectul repararii verificatorului pe v4 - exact, fara apel: aceleasi propuneri, verificarea noua;
  - C29: cate intrebari ating inca limita de pasi si costul;
  - GRESELILE DE FOND ramase (cifra principala, decizia 8): fiecare GRESIT al comparatorului, cu
    separarea mecanica "fapt gresit / fapt corect, articol diferit" si citirea pe fond, intrebare cu
    intrebare, marcata ca lectura (de verificat de om).
"""
import json
import os
import re
import time

from fiscalos import comparatie, intrebari, semantic

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(_RAD, "intrebari", "v5")
ZIP = "/home/costin/ghid_incoming/fiscalos_intrebari_v5_rezultat.zip"
ET = {"CORECT": "CORECT", "GRESIT": "GREȘIT", "NU_POT": "NU POT"}


def _s(t, n=140):
    t = " ".join(str(t or "").split())
    return (t[:n] + "…") if len(t) > n else t


def _j(p):
    return json.load(open(p, encoding="utf-8"))


def _scrie(obj, p):
    json.dump(obj, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)


def efect_C24_pe_v4(nav4):
    """Aceleasi propuneri v4, verificarea "raspuns gol" de acum. Celelalte verificari sunt neschimbate,
    deci diferenta e exact efectul C24."""
    return [r["id"] for r in nav4["raspunsuri"] if r["stare"] == "RASPUNS" and "raspuns gol" in
            semantic.verifica(dict(r["propunerea_modelului"], citate=[]), [], r["intrebare"], None)]


def construieste():
    os.makedirs(os.path.join(DEST, "raspunsuri"), exist_ok=True)
    t0 = time.time()
    from fiscalos import _comparatie_inainte_C28 as vechi
    nav = _j(os.path.join(_RAD, "artefacte", "intrebari", "raspunsuri_navigare_v5.json"))
    _scrie(nav, os.path.join(DEST, "raspunsuri_navigare.json"))
    lex = _j(os.path.join(_RAD, "artefacte", "intrebari", "raspunsuri_lexical_v5.json"))
    _scrie(lex, os.path.join(DEST, "raspunsuri_lexical.json"))
    nav4 = _j(os.path.join(_RAD, "intrebari", "v4", "raspunsuri_navigare.json"))
    sem3 = _j(os.path.join(_RAD, "intrebari", "v3", "raspunsuri_semantic.json"))

    # ── C28: inainte / dupa, pe fiecare rulare ──
    rulari = [("navigare v4", "intrebari/v4/raspunsuri_navigare.json"),
              ("semantic v3", "intrebari/v3/raspunsuri_semantic.json"),
              ("semantic v2", "intrebari/v2/raspunsuri_semantic.json"),
              ("lexical v4", "intrebari/v4/raspunsuri_lexical.json")]
    c28 = []
    for n, f in rulari:
        a, b = vechi.compara(os.path.join(_RAD, f)), comparatie.compara(os.path.join(_RAD, f))
        A = {c["id"]: c["verdict_pe_fond"] for c in a["comparatii"]}
        B = {c["id"]: c["verdict_pe_fond"] for c in b["comparatii"]}
        c28.append({"rulare": n, "inainte": a["scor_referinta_pe_fond"], "dupa": b["scor_referinta_pe_fond"],
                    "schimbari": [(i, A[i], B[i]) for i in A if A[i] != B[i]]})
    CN = comparatie.compara(os.path.join(DEST, "raspunsuri_navigare.json"))
    CL = comparatie.compara(os.path.join(DEST, "raspunsuri_lexical.json"))
    C4 = comparatie.compara(os.path.join(_RAD, "intrebari", "v4", "raspunsuri_navigare.json"))
    C3 = comparatie.compara(os.path.join(_RAD, "intrebari", "v3", "raspunsuri_semantic.json"))
    _scrie(CN, os.path.join(DEST, "comparatie_navigare.json"))
    _scrie(CL, os.path.join(DEST, "comparatie_lexical.json"))
    goale_v4 = efect_C24_pe_v4(nav4)
    s4 = dict(C4["scor_referinta_pe_fond"])
    VC4 = {c["id"]: c["verdict_pe_fond"] for c in C4["comparatii"]}
    s4_c24 = dict(s4)
    for i in goale_v4:
        s4_c24[VC4[i]] -= 1
        s4_c24["NU_POT"] += 1

    RN = {r["id"]: r for r in nav["raspunsuri"]}
    R4 = {r["id"]: r for r in nav4["raspunsuri"]}
    VN = {c["id"]: c for c in CN["comparatii"]}
    V4 = {c["id"]: c for c in C4["comparatii"]}
    V3 = {c["id"]: c for c in C3["comparatii"]}
    VL = {c["id"]: c for c in CL["comparatii"]}
    qs = intrebari.incarca_intrebari()
    lectura = json.load(open(os.path.join(_RAD, "fiscalos", "lectura_v5.json"), encoding="utf-8"))

    gresite = [c for c in CN["comparatii"] if c["verdict_pe_fond"] == "GRESIT"]
    fapt_gresit = [c["id"] for c in gresite if not c.get("valoare_ok")]
    art_diferit = [c["id"] for c in gresite if c.get("valoare_ok")]
    de_fond = [i for i, v in lectura.items() if v["fel"] == "fond"]
    calcul = [q["id"] for q in qs if q["tip"] == "CALCUL"]
    calc_r = [i for i in calcul if RN[i]["stare"] == "RASPUNS"]
    multi_date = [(r["id"], [d[0] for d in r.get("date_din_intrebare") or []], r.get("data_referinta"),
                   r["stare"]) for r in nav["raspunsuri"] if len(r.get("date_din_intrebare") or []) > 1]
    unelte = {}
    for r in nav["raspunsuri"]:
        for p in r["apel"]["pasi"]:
            unelte[p["unealta"]] = unelte.get(p["unealta"], 0) + 1
    masuri = {"C28": c28, "C24_goale_v4": goale_v4, "scor_v4_dupa_C28": s4, "scor_v4_dupa_C28_C24": s4_c24,
              "gresite_fapt_gresit": fapt_gresit, "gresite_articol_diferit": art_diferit,
              "greseli_de_fond_lectura": de_fond, "calcul_raspunse": calc_r,
              "calcul_corecte": [i for i in calc_r if VN[i]["verdict_pe_fond"] == "CORECT"],
              "C29_la_limita": nav["la_limita_de_pasi_C29"], "C23_abtineri": nav["abtineri_C23"],
              "C23_reincercari": nav["reincercari_C23"], "C27_intrebari_cu_mai_multe_date": multi_date,
              "anexe_citate": sorted({(r["id"], a["atom"]) for r in nav["raspunsuri"]
                                      for a in r.get("argument") or [] if "#anexa" in a["atom"]}),
              "unelte": unelte}
    _scrie(masuri, os.path.join(DEST, "masuratori.json"))

    for q in qs:
        r, c, r4 = RN[q["id"]], VN[q["id"]], R4[q["id"]]
        L = ["# %s — %s" % (q["id"], q["tip"]), "", "**Întrebarea:** %s" % q["intrebare"], "",
             "## Stratul de navigare v5 — %s" % ("RĂSPUNS" if r["stare"] == "RASPUNS" else "NU POT RĂSPUNDE"),
             "", "*%s*" % (r.get("declaratie") or "—"), "",
             "Datele din întrebare: %s · data de referință aleasă: **%s** — %s" % (
                 ", ".join(d[0] for d in r.get("date_din_intrebare") or []) or "niciuna (ziua întrebării)",
                 r.get("data_referinta") or "—", _s(r.get("data_referinta_motiv"), 300)), ""]
        if r["stare"] == "RASPUNS":
            L += ["> **%s**" % _s(r["raspuns"].split("  [calcul:")[0].split("  [data de referință")[0], 1500), ""]
            if r.get("citat_decisiv"):
                L += ["Citatul decisiv (`%s`):" % r["citat_decisiv"]["atom"],
                      "> %s" % _s(r["citat_decisiv"]["fragment"], 600), ""]
        L += ["Motiv: %s" % _s(r["motiv"], 1500), ""]
        if r.get("calcule"):
            L += ["### Calculul, pas cu pas — evaluat de cod, nu de model", ""]
            for d in r["calcule"]:
                for z in d.get("zile") or []:
                    L += ["- `%s`" % z]
                L += ["- `%s = %s` = %s = **%s**" % (d["nume"], d["formula"], d.get("cu_valori", ""), d["rezultat"])]
                for o in d["operanzi"]:
                    L += ["  - `%s` = %s — %s%s: „%s”" % (
                        o["nume"], o["valoare"], o.get("eticheta", ""),
                        " din `%s`" % o["atom"] if o.get("atom") else " (din întrebare)", _s(o["fragment"], 300))]
            L += [""]
        for a in r.get("argument") or []:
            L += ["- **%s** — `%s` · valabil din %s" % (
                a["temei"], a["atom"], a["valabilitate"].get("valabil_din") or "nedovedit"),
                  "  > %s" % _s(a["verbatim"], 500)]
        for d in r.get("derogari_tratate") or []:
            L += ["- derogare tratată: `%s` — %s" % (d["atom"], _s(d["cum"], 300))]
        ap = r["apel"]
        L += ["", "### Navigarea (%d pași, %d ture%s)" % (
            ap["pasi_navigare"], ap["tururi"], ", %d reîncercare C23" % ap["reincercari_C23"]
            if ap.get("reincercari_C23") else ""), ""]
        for i, p in enumerate(ap["pasi"], 1):
            L += ["%d. `%s` %s" % (i, p["unealta"], json.dumps(p["intrare"], ensure_ascii=False))]
        L += ["", "Apel: `%s`%s, %s tokeni, $%.4f, %.0f s" % (
            ap["model"], " — **MODELUL DE REZERVĂ (C15)**" if ap.get("fallback") else "",
            ap["tokeni"], ap["cost_usd"], ap["secunde"]),
              "", "Pe fond (comparator): **%s** — %s" % (ET[c["verdict_pe_fond"]], _s(c["de_ce"], 300))]
        if q["id"] in lectura:
            L += ["", "Lectura pe fond (de verificat de om): **%s** — %s" % (
                lectura[q["id"]]["fel"], lectura[q["id"]]["de_ce"])]
        L += ["", "## v4 — %s, pe fond %s" % ("RĂSPUNS" if r4["stare"] == "RASPUNS" else "NU POT",
                                             ET[V4[q["id"]]["verdict_pe_fond"]]),
              "", "> %s" % _s(r4.get("raspuns") or r4["motiv"], 500), "",
              "## Cheia", "", "- %s" % c["raspuns_asteptat"], "- temei: %s" % c["temei_asteptat"]]
        open(os.path.join(DEST, "raspunsuri", "%s.md" % q["id"]), "w", encoding="utf-8").write(
            "\n".join(L) + "\n")

    sn, sl, s3 = CN["scor_referinta_pe_fond"], CL["scor_referinta_pe_fond"], C3["scor_referinta_pe_fond"]
    L = []
    A = L.append
    A("# FiscalOS v2 — Motorul de întrebări v5: deciziile C23–C29")
    A("")
    A("Generat %s · ZIP: `%s`" % (time.strftime("%d.%m.%Y %H:%M"), ZIP))
    A("")
    A("> **Scor INDICATIV** — setul de 50 e expus. Măsurătoarea finală va fi pe setul nou.")
    A("")
    A("## Cifra principală: greșelile de fond rămase (decizia 8)")
    A("")
    A("**%d** răspunsuri greșite pe fond, din %d GREȘIT ale comparatorului (lectura mea, întrebare cu "
      "întrebare, de verificat de om; lista completă mai jos). Separarea mecanică a celor %d GREȘIT: "
      "faptul principal al cheii lipsește/e altul — %d (%s); faptul e corect, articolul diferă — %d (%s)."
      % (len(de_fond), sn["GRESIT"], sn["GRESIT"], len(fapt_gresit), ", ".join(fapt_gresit) or "—",
         len(art_diferit), ", ".join(art_diferit) or "—"))
    A("")
    for i, v in lectura.items():
        if v["fel"] == "fond":
            A("- **%s** (%s): %s" % (i, VN[i]["tip"], v["de_ce"]))
    A("")
    A("Celelalte GREȘIT, citite pe fond:")
    A("")
    for i, v in lectura.items():
        if v["fel"] != "fond":
            A("- **%s** — %s: %s" % (i, v["fel"], v["de_ce"]))
    A("")
    A("## Scorul pe fond (comparatorul reparat, C28)")
    A("")
    A("| Motor | CORECT | GREȘIT | NU POT | Cost | Pași medii |")
    A("|---|---|---|---|---|---|")
    A("| **Navigare v5** | **%d** | **%d** | **%d** | **$%.4f** | **%.1f** |"
      % (sn["CORECT"], sn["GRESIT"], sn["NU_POT"], nav["cost_usd"], nav["pasi_medii"]))
    A("| Navigare v4, comparator reparat (C28) și verificator reparat (C24) | %d | %d | %d | $%.4f | %.1f |"
      % (s4_c24["CORECT"], s4_c24["GRESIT"], s4_c24["NU_POT"], nav4["cost_usd"], nav4["pasi_medii"]))
    A("| Semantic v3 | %d | %d | %d | $%.4f | — |" % (s3["CORECT"], s3["GRESIT"], s3["NU_POT"], sem3["cost_usd"]))
    A("| Lexical (referință $0, C21; corpusul de acum, cu C26) | %d | %d | %d | $0 | — |"
      % (sl["CORECT"], sl["GRESIT"], sl["NU_POT"]))
    A("")
    A("Tokeni: %s. Verificarea mecanică a respins %d propuneri. Model de rezervă (C15): %s."
      % (nav["tokeni"], nav["respinse_de_verificare"], ", ".join(nav["de_la_modelul_de_rezerva"]) or "niciodată"))
    A("")
    A("## Deciziile, fiecare cu efectul ei măsurat")
    A("")
    A("**C23 — structura răspunsului final.** Reîncercări cerute: %d (%s). Abțineri după a doua structură "
      "invalidă: %d (%s). În v4 defectul lovise 7 întrebări."
      % (len(nav["reincercari_C23"]), ", ".join(nav["reincercari_C23"]) or "—", len(nav["abtineri_C23"]),
         ", ".join(nav["abtineri_C23"]) or "—"))
    A("")
    A("**C24 — „răspuns gol\" verificat întotdeauna.** Măsurat exact pe propunerile v4, fără niciun apel: "
      "%d răspunsuri goale ar fi fost respinse (%s). Scorul v4 (comparatorul reparat): %d/%d/%d → "
      "**%d/%d/%d**. Probe în ambele direcții: `test_semantic.test_C24_*` (golul și „x\" se resping cu și "
      "fără derogări; „Nu.\" și „21%%\" trec; abținerea fără răspuns nu e „răspuns gol\")."
      % (len(goale_v4), ", ".join(goale_v4), s4["CORECT"], s4["GRESIT"], s4["NU_POT"],
         s4_c24["CORECT"], s4_c24["GRESIT"], s4_c24["NU_POT"]))
    A("")
    A("**C25 — etichete FAPT_CAZ / VALOARE_LEGALĂ.** Respinse la verificarea calculului: %s."
      % (", ".join(r["id"] for r in nav["raspunsuri"] if "VERIFICAREA CALCULULUI" in (r.get("motiv") or ""))
         or "niciuna"))
    A("Q-CTB-03 (respinsă în v4 pentru „valoare fiscală 100.000\"): v5 **%s**." % ET[VN["Q-CTB-03"]["verdict_pe_fond"]])
    A("")
    A("**C26 — anexele.** Atomi citați din anexe: %d (%s). Temeiul le numește ca atare (de ex. „OMFP "
      "1802/2014 anexa, pct. 238 alin. (2)\"). Efectul asupra propunerii: `propuneri/v6/` — aceleași "
      "clasificări (94/1/26/26), 23 de parametri cu atomul mutat la anexa lui, 2 temeiuri candidate false "
      "retrase." % (len(masuri["anexe_citate"]), ", ".join("%s `%s`" % x for x in masuri["anexe_citate"][:12])
                     or "—"))
    A("")
    A("**C27 — data de referință pentru faptul întrebat.** Întrebări cu mai multe date: %d." % len(multi_date))
    A("")
    for i, dd, ales, st in multi_date:
        A("- %s: datele %s → aleasă **%s** (%s)" % (i, ", ".join(dd), ales or "— (INCOMPLET/abținere)",
                                                     ET["NU_POT" if st != "RASPUNS" else VN[i]["verdict_pe_fond"]]))
    A("")
    A("**C28 — comparatorul, defect de clasă, scorul înainte și după:**")
    A("")
    A("| Rulare | Înainte | După | Schimbări |")
    A("|---|---|---|---|")
    for x in c28:
        A("| %s | %d/%d/%d | %d/%d/%d | %s |" % (
            x["rulare"], x["inainte"]["CORECT"], x["inainte"]["GRESIT"], x["inainte"]["NU_POT"],
            x["dupa"]["CORECT"], x["dupa"]["GRESIT"], x["dupa"]["NU_POT"],
            ", ".join("%s %s→%s" % (i, ET[a], ET[b]) for i, a, b in x["schimbari"]) or "—"))
    A("")
    A("Reparațiile: sumele se compară ca numere (2.020 = 2020; 1.031,25 = 1031,25; 0,5% = 0.5%); faptul "
      "dintr-o propoziție negată a cheii („Nu 25% × … = 540,63 lei, ci …\", „(nu 25 martie)\") nu e faptul "
      "ei principal; paranteza de proveniență („(mod. OUG 89/2025)\") nu e temei; o bucată de temei fără act "
      "(„; art. 298 alin. (1)-(3)\") continuă actul bucății dinainte. Nicio notă nu a devenit mai severă. "
      "Calculul se afișează pas cu pas: fiecare formulă cu valorile puse în ea, fiecare `zile(a, b)`, "
      "numerele în stilul sursei (un an nu mai iese „2.027\").")
    A("")
    A("**C29 — 20 de pași.** Întrebări care ating încă limita: **%d** (%s) — abținere, cu traseul "
      "navigării în motiv. Pași medii: %.1f. Cost: $%.4f ($%.4f / întrebare; v4: $%.4f la 12 pași)."
      % (len(nav["la_limita_de_pasi_C29"]), ", ".join(nav["la_limita_de_pasi_C29"]) or "—", nav["pasi_medii"],
         nav["cost_usd"], nav["cost_usd"] / nav["n"], nav4["cost_usd"]))
    A("")
    A("### Întrebările CALCUL")
    A("")
    A("Răspunse: %d din %d (%s); corecte pe fond: %d (%s)." % (
        len(calc_r), len(calcul), ", ".join(calc_r) or "—", len(masuri["calcul_corecte"]),
        ", ".join(masuri["calcul_corecte"]) or "—"))
    A("")
    A("Unelte folosite: %s." % ", ".join("%s %d" % kv for kv in sorted(unelte.items(), key=lambda kv: -kv[1])))
    A("")
    A("---")
    A("")
    A(open(os.path.join(_RAD, "fiscalos", "cerinte_v5.md"), encoding="utf-8").read().strip())
    A("")
    A("---")
    A("")
    A("## Operațiile, cu durata și costul măsurate")
    A("")
    A("| Operație | Durată | Cost |")
    A("|---|---|---|")
    A("| Stratul de navigare v5: 50 de întrebări, %d ture la `%s` | %.1f s | $%.4f |"
      % (sum(r["apel"]["tururi"] for r in nav["raspunsuri"]), nav["model"], nav["secunde_total"], nav["cost_usd"]))
    prob = os.path.join(_RAD, "artefacte", "intrebari", "raspunsuri_navigare_v5_proba.json")
    if os.path.exists(prob):
        p = _j(prob)
        A("| Proba de cost: %d întrebări (%s) | %.1f s | $%.4f |"
          % (p["n"], ", ".join(r["id"] for r in p["raspunsuri"]), p["secunde_total"], p["cost_usd"]))
    for k, v in json.load(open(os.path.join(_RAD, "fiscalos", "durate_v5.json"), encoding="utf-8")).items():
        A("| %s | %.1f s | $0 |" % (k, v))
    A("| Motorul lexical, referință (index + 50 de întrebări) | %.1f s | $0 |" % lex.get("secunde_total", 0))
    A("| Comparații (inclusiv C28 înainte/după pe 4 rulări), măsurători, raport | %.1f s | $0 |" % (time.time() - t0))
    A("")
    A("## Cele 50 de întrebări")
    A("")
    A("| Id | Tip | v5 | v4 | Lexical | Pași | Data | Răspunsul v5 |")
    A("|---|---|---|---|---|---|---|---|")
    for q in qs:
        r = RN[q["id"]]
        A("| %s | %s | %s | %s | %s | %d | %s | %s |" % (
            q["id"], q["tip"], ET[VN[q["id"]]["verdict_pe_fond"]], ET[V4[q["id"]]["verdict_pe_fond"]],
            ET[VL[q["id"]]["verdict_pe_fond"]], r["apel"]["pasi_navigare"], r.get("data_referinta") or "—",
            _s(r["raspuns"], 70) if r["stare"] == "RASPUNS" else "*%s*" % _s(r["motiv"], 60)))
    open(os.path.join(DEST, "RAPORT.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    return sn, masuri


if __name__ == "__main__":
    sn, m = construieste()
    print("navigare v5:", sn)
    print(json.dumps({k: v for k, v in m.items() if k not in ("unelte", "C28")}, ensure_ascii=False)[:3000])
