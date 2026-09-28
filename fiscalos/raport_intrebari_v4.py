# -*- coding: utf-8 -*-
"""Livrabilul motorului de intrebari v4: navigarea structurala (decizia 6) si calculul evaluat de cod
(decizia 7). intrebari/v1..v3 raman neatinse. Scor INDICATIV: setul de 50 e expus.

Raportate SEPARAT (decizia 8):
  - abtinerile de REGASIRE eliminate: abtinerile semantice v3 al caror motiv spune ca atomii primiti
    nu contin regula ("atomii primiti nu contin", "niciun atom primit") si care in v4 sunt raspunsuri;
  - intrebarile CALCUL rezolvate: raspunse, cu calcul evaluat de cod, si notate pe fond;
  - erorile NOI: GRESIT in v4 care nu erau GRESIT in v3;
  - costul si numarul mediu de pasi de navigare.
"""
import json
import os
import re
import time

from fiscalos import comparatie, intrebari, potrivire

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(_RAD, "intrebari", "v4")
ZIP = "/home/costin/ghid_incoming/fiscalos_intrebari_v4_rezultat.zip"
ET = {"CORECT": "CORECT", "GRESIT": "GREȘIT", "NU_POT": "NU POT"}
_REGASIRE = re.compile(r"atomii primi|niciun(ul)? (dintre )?atom|atomul primit|nu am reg[aă]sit", re.I)


def _s(t, n=140):
    t = " ".join(str(t or "").split())
    return (t[:n] + "…") if len(t) > n else t


def _j(p):
    return json.load(open(p, encoding="utf-8"))


def _scrie(obj, p):
    json.dump(obj, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)


def e_abtinere_de_regasire(r):
    return r["stare"] != "RASPUNS" and r.get("tip_abtinere") != "INCOMPLET" and \
        "VERIFICAREA" not in (r.get("motiv") or "") and bool(_REGASIRE.search(r.get("motiv") or ""))


def construieste():
    os.makedirs(os.path.join(DEST, "raspunsuri"), exist_ok=True)
    t0 = time.time()
    nav = _j(os.path.join(_RAD, "artefacte", "intrebari", "raspunsuri_navigare.json"))
    _scrie(nav, os.path.join(DEST, "raspunsuri_navigare.json"))
    sem3 = _j(os.path.join(_RAD, "intrebari", "v3", "raspunsuri_semantic.json"))
    lex = _j(os.path.join(_RAD, "artefacte", "intrebari", "raspunsuri_lexical_v4.json"))
    _scrie(lex, os.path.join(DEST, "raspunsuri_lexical.json"))
    CN = comparatie.compara(os.path.join(DEST, "raspunsuri_navigare.json"))
    CL = comparatie.compara(os.path.join(DEST, "raspunsuri_lexical.json"))
    C3 = _j(os.path.join(_RAD, "intrebari", "v3", "comparatie_semantic.json"))
    _scrie(CN, os.path.join(DEST, "comparatie_navigare.json"))
    _scrie(CL, os.path.join(DEST, "comparatie_lexical.json"))
    corp = potrivire.Corpus()

    RN = {r["id"]: r for r in nav["raspunsuri"]}
    R3 = {r["id"]: r for r in sem3["raspunsuri"]}
    RL = {r["id"]: r for r in lex["raspunsuri"]}
    VN = {c["id"]: c for c in CN["comparatii"]}
    V3 = {c["id"]: c for c in C3["comparatii"]}
    VL = {c["id"]: c for c in CL["comparatii"]}
    qs = intrebari.incarca_intrebari()

    # ── cele patru masuratori separate ──
    regasire_v3 = [q["id"] for q in qs if e_abtinere_de_regasire(R3[q["id"]])]
    eliminate = [i for i in regasire_v3 if RN[i]["stare"] == "RASPUNS"]
    ramase = [i for i in regasire_v3 if RN[i]["stare"] != "RASPUNS"]
    calcul = [q["id"] for q in qs if q["tip"] == "CALCUL"]
    calc_rasp = [i for i in calcul if RN[i]["stare"] == "RASPUNS"]
    calc_cu_formula = [i for i in calc_rasp if RN[i].get("calcule")]
    calc_corecte = [i for i in calc_rasp if VN[i]["verdict_pe_fond"] == "CORECT"]
    erori_noi = [i for i in VN if VN[i]["verdict_pe_fond"] == "GRESIT" and V3[i]["verdict_pe_fond"] != "GRESIT"]
    erori_disparute = [i for i in VN if V3[i]["verdict_pe_fond"] == "GRESIT" and VN[i]["verdict_pe_fond"] != "GRESIT"]
    raspunse_retrase = [i for i in VN if R3[i]["stare"] == "RASPUNS" and RN[i]["stare"] != "RASPUNS"]
    respinse_calc = [r["id"] for r in nav["raspunsuri"] if "VERIFICAREA CALCULULUI" in (r.get("motiv") or "")]
    la_limita = [r["id"] for r in nav["raspunsuri"] if r["apel"]["pasi_navigare"] >= nav["max_pasi"]]
    # V2 (C22): cate raspunsuri citeaza o nota tranzitorie in locul articolului
    cit_note = [(r["id"], a["atom"]) for r in nav["raspunsuri"] for a in r.get("argument") or []
                if (corp.dupa_id.get(a["atom"]) or {}).get("nota_tranzitorie")]
    cit_note_v3 = [(r["id"], a["atom"]) for r in sem3["raspunsuri"] for a in r.get("argument") or []
                   if re.search(r"cod_fiscal_227_2015_consolidat#art[IVXLCDM]+", a["atom"])]
    unelte = {}
    for r in nav["raspunsuri"]:
        for p in r["apel"]["pasi"]:
            unelte[p["unealta"]] = unelte.get(p["unealta"], 0) + 1
    masuri = {"abtineri_de_regasire_v3": regasire_v3, "eliminate": eliminate, "ramase": ramase,
              "eliminate_pe_fond": {i: VN[i]["verdict_pe_fond"] for i in eliminate},
              "calcul": calcul, "calcul_raspunse": calc_rasp, "calcul_cu_formula_evaluata": calc_cu_formula,
              "calcul_corecte_pe_fond": calc_corecte, "erori_noi": erori_noi,
              "erori_disparute": erori_disparute, "raspunsuri_v3_retrase": raspunse_retrase,
              "respinse_de_verificarea_calculului": respinse_calc, "la_limita_de_pasi": la_limita,
              "citeaza_note_tranzitorii_v4": cit_note, "citeaza_articole_romane_CF_v3": cit_note_v3,
              "unelte_folosite": unelte}
    _scrie(masuri, os.path.join(DEST, "masuratori.json"))

    for q in qs:
        r, c, r3, c3 = RN[q["id"]], VN[q["id"]], R3[q["id"]], V3[q["id"]]
        L = ["# %s — %s" % (q["id"], q["tip"]), "", "**Întrebarea:** %s" % q["intrebare"], "",
             "## Stratul de navigare (v4) — %s" % ("RĂSPUNS" if r["stare"] == "RASPUNS" else "NU POT RĂSPUNDE"),
             "", "*%s*" % (r.get("declaratie") or "—"), ""]
        if r["stare"] == "RASPUNS":
            L += ["> **%s**" % _s(r["raspuns"], 1200), ""]
            if r.get("citat_decisiv"):
                L += ["Citatul decisiv (`%s`):" % r["citat_decisiv"]["atom"],
                      "> %s" % _s(r["citat_decisiv"]["fragment"], 600), ""]
        L += ["Motiv: %s" % _s(r["motiv"], 900), ""]
        if r.get("calcule"):
            L += ["### Calculul — evaluat de cod, nu de model", ""]
            for d in r["calcule"]:
                L += ["- `%s = %s` → **%s**" % (d["nume"], d["formula"], d["rezultat"])]
                for o in d["operanzi"]:
                    L += ["  - `%s` = %s — din %s: „%s”" % (
                        o["nume"], o["valoare"], "`%s`" % o["atom"] if o["sursa"] == "atom" else "întrebare",
                        _s(o["fragment"], 300))]
            L += [""]
        for a in r.get("argument") or []:
            L += ["- **%s** — `%s` · valabil din %s" % (
                a["temei"], a["atom"], a["valabilitate"].get("valabil_din") or "nedovedit"),
                  "  > %s" % _s(a["verbatim"], 500)]
        for d in r.get("derogari_tratate") or []:
            L += ["- derogare tratată: `%s` — %s" % (d["atom"], _s(d["cum"], 300))]
        ap = r["apel"]
        L += ["", "### Navigarea (%d pași, %d ture)" % (ap["pasi_navigare"], ap["tururi"]), ""]
        for i, p in enumerate(ap["pasi"], 1):
            L += ["%d. `%s` %s" % (i, p["unealta"], json.dumps(p["intrare"], ensure_ascii=False))]
        L += ["", "Apel: `%s`%s, %s tokeni, $%.4f, %.0f s" % (
            ap["model"], " — **MODELUL DE REZERVĂ (C15)**" if ap.get("fallback") else "",
            ap["tokeni"], ap["cost_usd"], ap["secunde"]),
              "", "Pe fond: **%s** — %s" % (ET[c["verdict_pe_fond"]], _s(c["de_ce"], 300)), "",
              "## Stratul semantic v3 (context dat de căutare) — %s, pe fond %s" % (
                  "RĂSPUNS" if r3["stare"] == "RASPUNS" else "NU POT", ET[c3["verdict_pe_fond"]]), "",
              "> %s" % _s(r3.get("raspuns") or r3["motiv"], 500), "",
              "## Cheia", "", "- %s" % c["raspuns_asteptat"], "- temei: %s" % c["temei_asteptat"]]
        open(os.path.join(DEST, "raspunsuri", "%s.md" % q["id"]), "w", encoding="utf-8").write(
            "\n".join(L) + "\n")

    sn, s3, sl = CN["scor_referinta_pe_fond"], C3["scor_referinta_pe_fond"], CL["scor_referinta_pe_fond"]
    L = []
    A = L.append
    A("# FiscalOS v2 — Motorul de întrebări v4: navigare structurală și calcul evaluat de cod")
    A("")
    A("Generat %s · ZIP: `%s`" % (time.strftime("%d.%m.%Y %H:%M"), ZIP))
    A("")
    A("> **Scor INDICATIV** — setul de 50 e expus. Măsurătoarea finală va fi pe setul nou.")
    A("")
    A("## Scorul pe fond")
    A("")
    A("| Motor | CORECT | GREȘIT | NU POT | Cost / rulare | Pași medii |")
    A("|---|---|---|---|---|---|")
    A("| **Stratul de navigare v4** | **%d** | **%d** | **%d** | **$%.4f** | **%.1f** |"
      % (sn["CORECT"], sn["GRESIT"], sn["NU_POT"], nav["cost_usd"], nav["pasi_medii"]))
    A("| Stratul semantic v3 (context dat de căutare) | %d | %d | %d | $%.4f | — |"
      % (s3["CORECT"], s3["GRESIT"], s3["NU_POT"], sem3["cost_usd"]))
    A("| Motorul lexical (referință $0, C21; corpusul de acum, cu V2) | %d | %d | %d | $0 | — |"
      % (sl["CORECT"], sl["GRESIT"], sl["NU_POT"]))
    A("")
    A("Tokeni stratul de navigare: %s. Verificarea mecanică a respins %d propuneri (%d la verificarea "
      "calculului: %s). Model de rezervă folosit (C15): %s. Întrebări oprite la limita de %d pași: %d (%s)."
      % (nav["tokeni"], nav["respinse_de_verificare"], len(respinse_calc), ", ".join(respinse_calc) or "—",
         ", ".join(nav["de_la_modelul_de_rezerva"]) or "niciodată", nav["max_pasi"], len(la_limita),
         ", ".join(la_limita) or "—"))
    A("")
    A("## Raportate separat (decizia 8)")
    A("")
    A("### 1. Abțineri de regăsire eliminate")
    A("")
    A("Abțineri v3 al căror motiv spune că atomii primiți nu conțin regula (esec de regăsire, nu de "
      "judecată): **%d**. În v4 au devenit răspunsuri: **%d** — pe fond: %s. Au rămas abțineri: %d (%s)."
      % (len(regasire_v3), len(eliminate),
         ", ".join("%s %s" % (i, ET[VN[i]["verdict_pe_fond"]]) for i in eliminate) or "—",
         len(ramase), ", ".join(ramase) or "—"))
    A("")
    A("### 2. Întrebările CALCUL")
    A("")
    A("%d întrebări CALCUL. Răspunse: **%d** (%s), din care cu calcul evaluat de cod: %d; corecte pe "
      "fond: **%d** (%s). În v3: %d răspunse, %d corecte."
      % (len(calcul), len(calc_rasp), ", ".join(calc_rasp) or "—", len(calc_cu_formula),
         len(calc_corecte), ", ".join(calc_corecte) or "—",
         sum(1 for i in calcul if R3[i]["stare"] == "RASPUNS"),
         sum(1 for i in calcul if V3[i]["verdict_pe_fond"] == "CORECT")))
    A("")
    for i in calc_rasp:
        A("- **%s** (%s): %s" % (i, ET[VN[i]["verdict_pe_fond"]], _s(RN[i]["raspuns"], 260)))
    A("")
    A("### 3. Erori noi")
    A("")
    A("GREȘIT în v4 care nu erau GREȘIT în v3: **%d**%s" % (len(erori_noi), ":" if erori_noi else "."))
    A("")
    for i in erori_noi:
        A("- **%s** (%s; v3: %s): motorul — %s · cheia — %s" % (
            i, VN[i]["tip"], ET[V3[i]["verdict_pe_fond"]], _s(RN[i]["raspuns"], 200),
            _s(VN[i]["raspuns_asteptat"], 200)))
    A("")
    A("GREȘIT în v3 care nu mai sunt GREȘIT în v4: %d (%s). Răspunsuri v3 retrase în v4: %d (%s)."
      % (len(erori_disparute), ", ".join("%s→%s" % (i, ET[VN[i]["verdict_pe_fond"]]) for i in erori_disparute)
         or "—", len(raspunse_retrase), ", ".join("%s (v3 %s)" % (i, ET[V3[i]["verdict_pe_fond"]])
                                                  for i in raspunse_retrase) or "—"))
    A("")
    A("### 4. Costul și pașii de navigare")
    A("")
    A("Cost: **$%.4f** pentru 50 de întrebări ($%.4f / întrebare; v3: $%.4f). Pași de navigare: **%.1f** "
      "în medie pe întrebare (limita %d). Unelte folosite: %s."
      % (nav["cost_usd"], nav["cost_usd"] / nav["n"], sem3["cost_usd"], nav["pasi_medii"], nav["max_pasi"],
         ", ".join("%s %d" % kv for kv in sorted(unelte.items(), key=lambda kv: -kv[1]))))
    A("")
    A("### Efectul V2 (C22), măsurat în această rulare")
    A("")
    A("Răspunsuri care citează o notă tranzitorie citată în consolidat în loc de articol: v3 — %d (%s); "
      "v4 — %d (%s). Q-TVA-03 (cazul care a descoperit V2): v3 %s, v4 **%s**."
      % (len(cit_note_v3), ", ".join("%s `%s`" % x for x in cit_note_v3) or "—", len(cit_note),
         ", ".join("%s `%s`" % x for x in cit_note) or "—", ET[V3["Q-TVA-03"]["verdict_pe_fond"]],
         ET[VN["Q-TVA-03"]["verdict_pe_fond"]]))
    A("")
    A("### Cele %d GREȘIT ale stratului de navigare — de citit" % sn["GRESIT"])
    A("")
    for c in CN["comparatii"]:
        if c["verdict_pe_fond"] == "GRESIT":
            A("- **%s** (%s): motorul — %s · cheia — %s" % (c["id"], c["tip"], _s(RN[c["id"]]["raspuns"], 160),
                                                           _s(c["raspuns_asteptat"], 160)))
    A("")
    A("Fapt corect, articol diferit (C2): %s." % (", ".join(x["id"] for x in CN["fapt_corect_articol_diferit"])
                                                   or "—"))
    A("Abțineri pe INCOMPLETA (C1): %s." % "; ".join(
        "%s — %s" % (x["id"], "incompletitudine detectată" if x["incompletitudine_detectata"] else "alt motiv")
        for x in CN["abtineri_pe_INCOMPLETA"]))
    A("")
    A("---")
    A("")
    A(open(os.path.join(_RAD, "fiscalos", "cerinte_v4.md"), encoding="utf-8").read().strip())
    A("")
    A("---")
    A("")
    A("## Operațiile, cu durata și costul măsurate")
    A("")
    A("| Operație | Durată | Cost |")
    A("|---|---|---|")
    A("| Stratul de navigare: 50 de întrebări, %d ture la `%s` | %.1f s | $%.4f |"
      % (sum(r["apel"]["tururi"] for r in nav["raspunsuri"]), nav["model"], nav["secunde_total"], nav["cost_usd"]))
    prob = os.path.join(_RAD, "artefacte", "intrebari", "raspunsuri_navigare_proba.json")
    if os.path.exists(prob):
        p = _j(prob)
        A("| Proba de cost înainte de rulare: %d întrebări (%s) | %.1f s | $%.4f |"
          % (p["n"], ", ".join(r["id"] for r in p["raspunsuri"]), p["secunde_total"], p["cost_usd"]))
    A("| Motorul lexical, referință (index + 50 de întrebări) | %.1f s | $0 |" % lex.get("secunde_total", 0))
    A("| Comparații, măsurători, raport | %.1f s | $0 |" % (time.time() - t0))
    A("")
    A("## Cele 50 de întrebări")
    A("")
    A("| Id | Tip | Navigare v4 | Semantic v3 | Lexical | Pași | Răspunsul v4 |")
    A("|---|---|---|---|---|---|---|")
    for q in qs:
        r = RN[q["id"]]
        A("| %s | %s | %s | %s | %s | %d | %s |" % (
            q["id"], q["tip"], ET[VN[q["id"]]["verdict_pe_fond"]], ET[V3[q["id"]]["verdict_pe_fond"]],
            ET[VL[q["id"]]["verdict_pe_fond"]], r["apel"]["pasi_navigare"],
            _s(r["raspuns"], 70) if r["stare"] == "RASPUNS" else "*%s*" % _s(r["motiv"], 60)))
    open(os.path.join(DEST, "RAPORT.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    return sn, s3, sl, masuri


if __name__ == "__main__":
    sn, s3, sl, m = construieste()
    print("navigare v4:", sn, "| semantic v3:", s3, "| lexical:", sl)
    print(json.dumps({k: v for k, v in m.items() if k != "unelte_folosite"}, ensure_ascii=False)[:2500])
