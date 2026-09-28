# -*- coding: utf-8 -*-
"""Livrabilul motorului de intrebari v3: stratul oficial (C12), relatia C17, C13-C15.
intrebari/v1 si intrebari/v2 raman neatinse. Scor INDICATIV: setul de 50 e expus.

ATRIBUIREA (decizia 7: "raportezi separat cate abtineri au disparut prin consolidatele noi si cate
prin relatia de derogare").
  motorul lexical  - determinist, deci ABLATIE exacta: L0 -> L1 (+ oficiale) -> L2 (+ C17).
  stratul semantic - NU e determinist: doua rulari pe aceleasi date dau raspunsuri usor diferite, deci
                     diferenta dintre rulari nu e o cauza. Atribuirea e CAUZALA, pe citate: o abţinere
                     din v2 care devine raspuns in v3 se datoreaza consolidatelor noi daca raspunsul
                     citeaza un atom NOU sau SCHIMBAT fata de instantaneu; relatiei de derogare daca
                     citeaza sau trateaza un atom adus de relatie; altfel "variatie intre rulari".
"""
import json
import os
import time

from fiscalos import comparatie, intrebari, potrivire

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(_RAD, "intrebari", "v3")
ZIP = "/home/costin/ghid_incoming/fiscalos_intrebari_v3_rezultat.zip"
ET = {"CORECT": "CORECT", "GRESIT": "GREȘIT", "NU_POT": "NU POT"}


def _s(t, n=140):
    t = " ".join(str(t or "").split())
    return (t[:n] + "…") if len(t) > n else t


def atribuie(sem_v2, sem_v3, corp_nou, corp_vechi):
    """Tranzitiile NU POT (v2) -> RASPUNS (v3) si RASPUNS (v2) -> NU POT (v3), cu cauza lor."""
    V2 = {r["id"]: r for r in sem_v2["raspunsuri"]}
    ies = {"disparute": [], "aparute": []}
    for r in sem_v3["raspunsuri"]:
        a = V2[r["id"]]
        if a["stare"] != "RASPUNS" and r["stare"] == "RASPUNS":
            citati = [x["atom"] for x in r.get("argument") or []]
            noi = [i for i in citati if corp_nou.sursa_act.get(i.split("#")[0], {}).get(
                "sursa", "").startswith("oficial") and (
                i not in corp_vechi.dupa_id
                or " ".join(corp_vechi.dupa_id[i]["text"].split())
                != " ".join(corp_nou.dupa_id[i]["text"].split()))]
            rel = set((r.get("relatii_in_context") or {}).keys())
            prin_rel = [i for i in citati + [d["atom"] for d in r.get("derogari_tratate") or []]
                        if i in rel]
            cauze = (["consolidate noi"] if noi else []) + (["relatia de derogare"] if prin_rel else [])
            ies["disparute"].append({"id": r["id"], "cauze": cauze or ["variatie intre rulari"],
                                     "atomi_noi_citati": noi, "atomi_din_relatie": prin_rel})
        elif a["stare"] == "RASPUNS" and r["stare"] != "RASPUNS":
            inc = (r.get("verificare") or {}).get("incalcari", [])
            cauza = ("C17 (b): derogare netratata" if any("C17" in g for g in inc) else
                     "C13: valoare legala nedovedita din atom" if any("C13" in g for g in inc) else
                     "verificarea mecanica" if inc else "modelul s-a abţinut")
            ies["aparute"].append({"id": r["id"], "cauza": cauza})
    return ies


def construieste():
    os.makedirs(os.path.join(DEST, "raspunsuri"), exist_ok=True)
    t0 = time.time()
    abl = json.load(open(os.path.join(_RAD, "artefacte", "intrebari", "ablatie_lexical.json"),
                         encoding="utf-8"))
    sem2 = json.load(open(os.path.join(_RAD, "intrebari", "v2", "raspunsuri_semantic.json"),
                          encoding="utf-8"))
    sem3 = json.load(open(os.path.join(_RAD, "artefacte", "intrebari", "raspunsuri_semantic_v3.json"),
                          encoding="utf-8"))
    json.dump(sem3, open(os.path.join(DEST, "raspunsuri_semantic.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    lex = json.load(open(os.path.join(_RAD, "artefacte", "intrebari", "raspunsuri_lexical_L2.json"),
                         encoding="utf-8"))
    json.dump(lex, open(os.path.join(DEST, "raspunsuri_lexical.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    CS = comparatie.compara(os.path.join(DEST, "raspunsuri_semantic.json"))
    CL = comparatie.compara(os.path.join(DEST, "raspunsuri_lexical.json"))
    for n, C in (("semantic", CS), ("lexical", CL)):
        json.dump(C, open(os.path.join(DEST, "comparatie_%s.json" % n), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
    corp_nou, corp_vechi = potrivire.Corpus(True), potrivire.Corpus(False)
    atr = atribuie(sem2, sem3, corp_nou, corp_vechi)
    json.dump(atr, open(os.path.join(DEST, "atribuire_semantic.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    t_comp = time.time() - t0
    C2 = comparatie.compara(os.path.join(_RAD, "intrebari", "v2", "raspunsuri_semantic.json"))

    RS = {r["id"]: r for r in sem3["raspunsuri"]}
    RL = {r["id"]: r for r in lex["raspunsuri"]}
    VS = {c["id"]: c for c in CS["comparatii"]}
    VL = {c["id"]: c for c in CL["comparatii"]}
    qs = intrebari.incarca_intrebari()
    for q in qs:
        L = ["# %s — %s" % (q["id"], q["tip"]), "", "**Întrebarea:** %s" % q["intrebare"], ""]
        for titlu, R, V in (("Stratul semantic", RS, VS), ("Motorul lexical", RL, VL)):
            r, c = R[q["id"]], V[q["id"]]
            L += ["## %s — %s" % (titlu, "RĂSPUNS" if r["stare"] == "RASPUNS" else "NU POT RĂSPUNDE"),
                  "", "*%s*" % (r.get("declaratie") or "—"), ""]
            if r["stare"] == "RASPUNS":
                L += ["> **%s**" % _s(r["raspuns"], 700), ""]
                if r.get("citat_decisiv"):             # C14
                    L += ["Citatul decisiv (`%s`):" % r["citat_decisiv"]["atom"],
                          "> %s" % _s(r["citat_decisiv"]["fragment"], 600), ""]
            L += ["Motiv: %s" % _s(r["motiv"], 700), ""]
            for a in r.get("argument") or []:
                L += ["- **%s** — `%s` · valabil din %s" % (
                    a["temei"], a["atom"], a["valabilitate"].get("valabil_din") or "nedovedit"),
                      "  > %s" % _s(a["verbatim"], 500)]
            for d in r.get("derogari_tratate") or []:
                L += ["- derogare tratată: `%s` — %s" % (d["atom"], _s(d["cum"], 300))]
            if r.get("apel"):
                ap = r["apel"]
                L += ["", "Apel: `%s`%s, %s tokeni, $%.4f" % (
                    ap["model"], " — **MODELUL DE REZERVĂ (C15)**" if ap.get("fallback") else "",
                    ap["tokeni"], ap["cost_usd"])]
            L += ["", "Pe fond: **%s** — %s" % (ET[c["verdict_pe_fond"]], _s(c["de_ce"], 300)), ""]
        c = VL[q["id"]]
        L += ["## Cheia", "", "- %s" % c["raspuns_asteptat"], "- temei: %s" % c["temei_asteptat"]]
        open(os.path.join(DEST, "raspunsuri", "%s.md" % q["id"]), "w", encoding="utf-8").write(
            "\n".join(L) + "\n")

    s3, s2 = CS["scor_referinta_pe_fond"], C2["scor_referinta_pe_fond"]
    sl = CL["scor_referinta_pe_fond"]
    disp = atr["disparute"]
    n_cons = sum(1 for x in disp if "consolidate noi" in x["cauze"])
    n_rel = sum(1 for x in disp if "relatia de derogare" in x["cauze"])
    n_var = sum(1 for x in disp if x["cauze"] == ["variatie intre rulari"])
    L = []
    A = L.append
    A("# FiscalOS v2 — Motorul de întrebări v3: consolidatele oficiale și relația de derogare")
    A("")
    A("Generat %s · ZIP: `%s`" % (time.strftime("%d.%m.%Y %H:%M"), ZIP))
    A("")
    A("> **Scor INDICATIV** — setul de 50 e expus. Măsurătoarea finală va fi pe setul nou.")
    A("")
    A("## Scorul pe fond")
    A("")
    A("| Motor | CORECT | GREȘIT | NU POT | Cost / rulare |")
    A("|---|---|---|---|---|")
    A("| **Stratul semantic v3** | **%d** | **%d** | **%d** | **$%.4f** |"
      % (s3["CORECT"], s3["GRESIT"], s3["NU_POT"], sem3["cost_usd"]))
    A("| Stratul semantic v2 (rularea precedentă) | %d | %d | %d | $%.4f |"
      % (s2["CORECT"], s2["GRESIT"], s2["NU_POT"], sem2["cost_usd"]))
    A("| Motorul lexical v3 (L2) | %d | %d | %d | $0 |" % (sl["CORECT"], sl["GRESIT"], sl["NU_POT"]))
    for k in ("L0", "L1"):
        x = abl["config"][k]["scor_pe_fond"]
        A("| Motorul lexical %s — %s | %d | %d | %d | $0 |"
          % (k, abl["config"][k]["descriere"], x["CORECT"], x["GRESIT"], x["NU_POT"]))
    A("")
    A("Tokeni stratul semantic v3: %s. Verificarea mecanică a respins %d propuneri — din care %d "
      "pentru o derogare netratată (C17 b: %s) și %d pentru o valoare legală nedovedită din atom "
      "(C13: %s). Model de rezervă folosit (C15): %s."
      % (sem3["tokeni"], sem3["respinse_de_verificare"], len(sem3["respinse_C17"]),
         ", ".join(sem3["respinse_C17"]) or "—", len(sem3["respinse_C13"]),
         ", ".join(sem3["respinse_C13"]) or "—", ", ".join(sem3["de_la_modelul_de_rezerva"]) or
         "niciodată"))
    A("")
    A("## Abțineri dispărute — separat, pe cauze (decizia 7)")
    A("")
    A("**Stratul semantic** (v2 → v3), atribuire cauzală pe citate — vezi antetul "
      "`raport_intrebari_v3.py`:")
    A("")
    A("| Cauza | Câte | Întrebări |")
    A("|---|---|---|")
    A("| **prin consolidatele noi** (citează un atom nou/schimbat față de instantaneu) | **%d** | %s |"
      % (n_cons, ", ".join(x["id"] for x in disp if "consolidate noi" in x["cauze"]) or "—"))
    A("| **prin relația de derogare** (citează/tratează un atom adus de relație) | **%d** | %s |"
      % (n_rel, ", ".join(x["id"] for x in disp if "relatia de derogare" in x["cauze"]) or "—"))
    A("| variație între rulări (nicio citare nouă, nicio derogare) | %d | %s |"
      % (n_var, ", ".join(x["id"] for x in disp if x["cauze"] == ["variatie intre rulari"]) or "—"))
    A("")
    A("Abțineri apărute (răspunsuri v2 retrase în v3): %s."
      % ("; ".join("%s — %s" % (x["id"], x["cauza"]) for x in atr["aparute"]) or "niciuna"))
    A("")
    t = abl["tranzitii"]
    A("**Motorul lexical**, ablație exactă (e determinist):")
    A("")
    A("| Pas | Abțineri dispărute | Abțineri apărute | Răspunsuri retrase greșite / corecte |")
    A("|---|---|---|---|")
    for k, et in (("L0->L1", "prin consolidatele noi"), ("L1->L2", "prin relația de derogare (b)")):
        x = t[k]
        A("| %s — %s | %d %s | %d | %d / %d |"
          % (k, et, len(x["abtineri_disparute"]), x["abtineri_disparute"] or "",
             len(x["abtineri_aparute"]), len(x["raspunsuri_retrase_care_erau_gresite"]),
             len(x["raspunsuri_retrase_care_erau_corecte"])))
    A("")
    A("La motorul lexical, relația nu poate *elimina* abțineri — el nu tratează derogări, doar se "
      "abține în fața lor. Calea (a) contează numai pentru stratul semantic.")
    A("")
    A("### Efectul relației de derogare asupra GREȘELILOR (nu asupra abținerilor)")
    A("")
    A("Atribuirea pe abțineri nu vede efectul principal al relației. Cele două greșeli reale de fond "
      "din v2 — regula generală citată în locul celei speciale — **nu mai sunt răspunsuri greșite pe "
      "regulă**, și amândouă au derogările aduse de relație tratate explicit în răspuns:")
    A("")
    for k in ("Q-PRF-09", "Q-SAL-04"):
        r = RS[k]
        A("- **%s** — v2: GREȘIT (regula generală). v3: %s. Derogări tratate de model: %s."
          % (k, ("răspuns cu regula specială (CF art. 41 alin. (10^1)) — *%s*; notat **%s** pe fond, "
                 "fiindcă nu conține cifra de 16%% din cheie (cota stă în CF art. 17, necitat)"
                 % (_s(r["raspuns"], 160), ET[VS[k]["verdict_pe_fond"]]))
                if r["stare"] == "RASPUNS" else "abținere — modelul a găsit derogările și a refuzat "
                "să răspundă cu valorile din 2025",
             ", ".join("`%s`" % d["atom"].split("#")[1] for d in r.get("derogari_tratate") or []) or "—"))
    A("")
    A("### Defecte de clasă găsite după comparație (decizia: raportate cu scorul înainte și după)")
    A("")
    A("**V1 — verificatorul trata identificatorul unui act („OPANAF 587/2016\") ca pe o valoare.** "
      "Reparat. Măsurat EXACT, fără niciun apel nou: propunerile salvate ale modelului au fost "
      "re-verificate (`semantic.reverifica`, contextul se reconstruiește determinist). Scor semantic "
      "pe fond: **10/7/33 → %d/%d/%d**. Q-PRF-09 trece verificarea; notat GREȘIT de comparatorul "
      "strict, din motivul de mai sus." % (s3["CORECT"], s3["GRESIT"], s3["NU_POT"]))
    A("")
    A("**V2 — notele cu dispoziții tranzitorii citate devin pseudo-articole ale Codului.** "
      "Forma consolidată oficială pune, după unele alineate, note care citează textul actului "
      "modificator („Articolul III din OG 22/2025 prevede: (6) …\"). Conversia mea le atomizează ca "
      "articole romane ale Codului fiscal (`cod_fiscal…#artIII~2/alin6~2`). La Q-TVA-03, modelul a "
      "citat nota în locul art. 310 alin. (6), cu același text — răspuns corect pe fond, notat GREȘIT "
      "pentru articol (din CORECT în v2). Tot de aici vin sursele de derogare din C20 („Art. VIII\"). "
      "**Nereparat** — vezi C22.")
    A("")
    A("### Cele %d GREȘIT ale stratului semantic v3 — de citit" % s3["GRESIT"])
    A("")
    for c in CS["comparatii"]:
        if c["verdict_pe_fond"] == "GRESIT":
            r = RS[c["id"]]
            A("- **%s** (%s): motorul — %s · cheia — %s" % (c["id"], c["tip"], _s(r["raspuns"], 140),
                                                           _s(c["raspuns_asteptat"], 140)))
    A("")
    A("Fapt corect, articol diferit (C2): %s." % (", ".join(x["id"] for x in CS["fapt_corect_articol_diferit"])
                                                   or "—"))
    A("Abțineri pe INCOMPLETA (C1): %s." % "; ".join(
        "%s — %s" % (x["id"], "incompletitudine detectată" if x["incompletitudine_detectata"] else "alt motiv")
        for x in CS["abtineri_pe_INCOMPLETA"]))
    A("")
    A("---")
    A("")
    A(CERINTE.strip())
    A("")
    A("---")
    A("")
    A("## Operațiile, cu durata și costul măsurate")
    A("")
    A("| Operație | Durată | Cost |")
    A("|---|---|---|")
    man = json.load(open(os.path.join(_RAD, "surse_oficiale", "MANIFEST.json"), encoding="utf-8"))
    A("| Aducerea celor 6 acte din legislatie.just.ro | %.1f s | $0 |"
      % sum(v["secunde"] for v in man["acte"].values()))
    A("| Stratul semantic v3: 50 de apeluri la `%s` | %.1f s | $%.4f |"
      % (sem3["model"], sem3["secunde_total"] - sem3["secunde_index"], sem3["cost_usd"]))
    for k in ("L0", "L1", "L2"):
        A("| Motorul lexical %s (index + 50 de întrebări + comparație) | %.1f s | $0 |"
          % (k, abl["config"][k]["secunde"]))
    A("| Comparații, atribuire, raport | %.1f s | $0 |" % (time.time() - t0))
    A("")
    A("## Cele 50 de întrebări")
    A("")
    A("| Id | Tip | Semantic | Lexical | Răspunsul semantic |")
    A("|---|---|---|---|---|")
    for q in qs:
        r = RS[q["id"]]
        A("| %s | %s | %s | %s | %s |" % (q["id"], q["tip"], ET[VS[q["id"]]["verdict_pe_fond"]],
                                          ET[VL[q["id"]]["verdict_pe_fond"]],
                                          _s(r["raspuns"], 70) if r["stare"] == "RASPUNS"
                                          else "*%s*" % _s(r["motiv"], 60)))
    open(os.path.join(DEST, "RAPORT.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    return s3, sl, atr


CERINTE = """
## 0. CERINȚE — decizii de arhitect

### Aplicate în acest pas

| | Decizia | Cum e aplicată |
|---|---|---|
| **C12** | consolidatele la zi, din legislatie.just.ro, într-un strat propriu, cu proveniență, dată și SHA | `surse_oficiale/` + `MANIFEST.json`; instantaneul iConta neatins; lista în `propuneri/v4/acte_aduse.json` |
| **C13** | cifrele din întrebare numai ca fapte ale cazului; o valoare legală se dovedește din atom | `semantic.e_valoare_legala()` + verificare |
| **C14** | lângă orice Da/Nu, citatul decisiv | `citat_decisiv`, în fiecare fișier per întrebare |
| **C15** | fallback-ul se păstrează; răspunsul de la modelul de rezervă e marcat | `apel.fallback`; lista din tabelul de scor |
| **C16** | luat la cunoștință | — |
| **C17** | relația „modifică / derogă / prin excepție", extrasă din text; (a) în context, (b) plasa de siguranță | `fiscalos/relatii.py`: 883 de muchii (543 excepții, 338 derogări, 2 modificări neîncorporate), 234 de trimiteri nerezolvabile, numărate |

### De decis

**C20 — Dispozițiile tranzitorii citate în consolidat.** Forma consolidată oficială a Codului fiscal
conține dispoziții tranzitorii citate din OUG-uri („Art. VIII … prin derogare de la art. 41 alin.
(8)"), fără dată de expirare în text. Relația le tratează ca derogări valabile, deci plasa de siguranță
(b) poate produce abțineri în plus — o eroare în direcția sigură. *De decis:* se caută data de
expirare a fiecărei dispoziții tranzitorii (în actul-sursă), sau abținerea în plus e acceptată?

**C22 — Notele tranzitorii din consolidatul oficial (V2).** Repararea — atomii unui articol roman
dintr-un cod cu articole arabe marcați „notă: dispoziție tranzitorie citată", penalizați la căutare
și numiți ca atare în temei — schimbă contextul modelului, deci efectul ei pe stratul semantic se
măsoară numai cu o rulare nouă (~$3,3, cu variația de la o rulare la alta). *De decis:* se repară și
se măsoară acum, sau odată cu setul nou?

**C21 — Plasa de siguranță costă răspunsuri corecte la motorul lexical.** L1 → L2 a retras 7
răspunsuri: 5 greșite, 2 corecte. Motorul lexical nu poate trata o derogare, doar se poate abține. *De
decis:* motorul lexical rămâne cu plasa (mai puține greșeli), sau ea se aplică numai stratului semantic?
"""


if __name__ == "__main__":
    s3, sl, atr = construieste()
    print("semantic v3 pe fond:", s3, "| lexical v3:", sl)
    print("disparute:", json.dumps(atr["disparute"], ensure_ascii=False)[:800])
    print("aparute:", atr["aparute"])
