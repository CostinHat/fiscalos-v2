# -*- coding: utf-8 -*-
"""Livrabilul motorului de intrebari v2: motorul lexical (mecanic) si stratul semantic ancorat pe
atomi, alaturi, notate pe fond (decizia C1), cu costul masurat. intrebari/v1/ rămâne neatins.

Scorul pe cele 50 de intrebari e INDICATIV, nu masuratoare finala (decizia 12): setul e expus - l-am
vazut, am reparat clase de defecte pe el. Masuratoarea finala va fi pe un set nou, primit la final.
"""
import json
import os
import time

from fiscalos import comparatie, intrebari

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(_RAD, "intrebari", "v2")
ZIP = "/home/costin/ghid_incoming/fiscalos_intrebari_v2_rezultat.zip"
ET = {"CORECT": "CORECT", "GRESIT": "GREȘIT", "NU_POT": "NU POT"}


def _s(t, n=140):
    t = " ".join(str(t or "").split())
    return (t[:n] + "…") if len(t) > n else t


def construieste(sem=None, durate_sem=None):
    durate = []
    os.makedirs(os.path.join(DEST, "raspunsuri"), exist_ok=True)
    t0 = time.time()
    idx = intrebari.Index()
    durate.append(("Index BM25 (%d atomi din acte normative)" % idx.N, time.time() - t0))
    t0 = time.time()
    qs = intrebari.incarca_intrebari()
    lex = [intrebari.raspunde(q, idx) for q in qs]
    durate.append(("Motorul lexical: 50 de intrebari", time.time() - t0))
    f_lex = os.path.join(DEST, "raspunsuri_lexical.json")
    json.dump({"raspunsuri": lex}, open(f_lex, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    t0 = time.time()
    C_lex = comparatie.compara(f_lex)
    durate.append(("Comparatia - motorul lexical", time.time() - t0))
    C_sem = None
    if sem:
        f_sem = os.path.join(DEST, "raspunsuri_semantic.json")
        json.dump(sem, open(f_sem, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        durate += durate_sem or []
        t0 = time.time()
        C_sem = comparatie.compara(f_sem)
        durate.append(("Comparatia - stratul semantic", time.time() - t0))
    for nume, C in (("lexical", C_lex), ("semantic", C_sem)):
        if C:
            json.dump(C, open(os.path.join(DEST, "comparatie_%s.json" % nume), "w", encoding="utf-8"),
                      ensure_ascii=False, indent=1)

    RL = {r["id"]: r for r in lex}
    RS = {r["id"]: r for r in (sem or {}).get("raspunsuri", [])}
    CL = {c["id"]: c for c in C_lex["comparatii"]}
    CS = {c["id"]: c for c in (C_sem or {}).get("comparatii", [])}

    # ── fisierele per intrebare: DECLARATIA intai (C5), apoi raspunsul, argumentul, comparatia ─────
    for q in qs:
        L = ["# %s — %s" % (q["id"], q["tip"]), "", "**Întrebarea:** %s" % q["intrebare"], ""]
        for titlu, R, C in (("Stratul semantic (motorul nou)", RS, CS),
                            ("Motorul lexical", RL, CL)):
            r = R.get(q["id"])
            if not r:
                continue
            c = C[q["id"]]
            L += ["## %s — %s" % (titlu, "RĂSPUNS" if r["stare"] == "RASPUNS" else "NU POT RĂSPUNDE"),
                  "", "*%s*" % (r.get("declaratie") or "—"), ""]
            if r["stare"] == "RASPUNS":
                L += ["> **%s**" % _s(r["raspuns"], 700), ""]
            L += ["Motiv: %s" % _s(r["motiv"], 600), ""]
            for a in r.get("argument") or []:
                v = a["valabilitate"]
                L += ["- **%s** — `%s` · valabil din %s" % (a["temei"], a["atom"],
                                                           v.get("valabil_din") or "nedovedit"),
                      "  > %s" % _s(a["verbatim"], 600)]
            if r.get("apel"):
                ap = r["apel"]
                L += ["", "Apel: `%s`, %s tokeni, $%.4f, %.1f s"
                      % (ap["model"], ap["tokeni"], ap["cost_usd"], ap["secunde"])]
                if r.get("verificare") and not r["verificare"]["trece"]:
                    L += ["", "**Propunerea modelului, respinsă de verificare:** %s"
                          % _s(json.dumps(r["propunerea_modelului"], ensure_ascii=False), 700)]
            L += ["", "Pe fond: **%s** — %s" % (ET[c["verdict_pe_fond"]], _s(c["de_ce"], 300)), ""]
        c = CL[q["id"]]
        L += ["## Cheia", "", "- răspuns așteptat: %s" % c["raspuns_asteptat"],
              "- temei așteptat: %s" % c["temei_asteptat"], ""]
        open(os.path.join(DEST, "raspunsuri", "%s.md" % q["id"]), "w", encoding="utf-8").write(
            "\n".join(L) + "\n")

    # ── raportul ─────────────────────────────────────────────────────────────────────────────────
    L = []
    A = L.append
    A("# FiscalOS v2 — Motorul de întrebări v2: stratul semantic ancorat pe atomi")
    A("")
    A("Generat %s · data întrebărilor: **%s** · ZIP: `%s`"
      % (time.strftime("%d.%m.%Y %H:%M"), intrebari.DATA_INTREBARII, ZIP))
    A("")
    A("> **Scor INDICATIV, nu măsurătoare finală** (decizia 12): setul de 50 e expus — l-am văzut și "
      "am reparat clase de defecte pe el. Măsurătoarea finală va fi pe un set nou.")
    A("")
    A("## Scorul de referință — pe fond (decizia C1)")
    A("")
    A("| Motor | CORECT | GREȘIT | NU POT | Cost / rulare |")
    A("|---|---|---|---|---|")
    sl = C_lex["scor_referinta_pe_fond"]
    if C_sem:
        ss = C_sem["scor_referinta_pe_fond"]
        A("| **Stratul semantic (nou)** | **%d** | **%d** | **%d** | **$%.4f** (%s tokeni) |"
          % (ss["CORECT"], ss["GRESIT"], ss["NU_POT"], sem["cost_usd"], sem["tokeni"]))
    A("| Motorul lexical (v1, cu C5) | %d | %d | %d | $0 |" % (sl["CORECT"], sl["GRESIT"], sl["NU_POT"]))
    A("")
    if C_sem:
        A("Stratul semantic: modelul a propus un răspuns la %d întrebări; **verificarea mecanică a "
          "respins %d** propuneri (citat neliteral sau cifră neliterală), iar acestea au devenit "
          "abțineri. A detectat incompletitudinea la %d întrebări."
          % (sem["raspunse"] + sem["respinse_de_verificare"], sem["respinse_de_verificare"],
             sem["incomplete_detectate"]))
        A("")
    A("### Abținerile pe întrebările INCOMPLETA — separat (C1)")
    A("")
    A("| Id | Motor | Incompletitudine detectată? | Ce lipsește, după motor | Cheia spune că lipsesc date? |")
    A("|---|---|---|---|---|")
    for nume, C in (("semantic", C_sem), ("lexical", C_lex)):
        for x in (C or {}).get("abtineri_pe_INCOMPLETA", []):
            A("| %s | %s | %s | %s | %s |" % (x["id"], nume, "**da**" if x["incompletitudine_detectata"]
                                             else "nu — alt motiv", _s("; ".join(x["ce_lipseste_dupa_motor"]), 90) or "—",
                                             "da" if x["cheia_spune_ca_lipsesc_date"] else "nu"))
    A("")
    A("### Fapt corect, articol diferit de al cheii — de judecat de om (C2)")
    A("")
    for nume, C in (("semantic", C_sem), ("lexical", C_lex)):
        for x in (C or {}).get("fapt_corect_articol_diferit", []):
            A("- **%s** (%s): răspuns `%s` · articolul motorului %s · al cheii %s — *%s*"
              % (x["id"], nume, _s(x["raspuns_motor"], 60), x["articol_motor"], x["articole_cheie"],
                 _s(x["temei_asteptat"], 120)))
    A("")
    if C_sem:
        A(ANALIZA.strip())
        A("")
    A("---")
    A("")
    A(CERINTE.strip())
    A("")
    A("---")
    A("")
    A("## 1. Operațiile, cu durata măsurată")
    A("")
    A("| Operație | Durată |")
    A("|---|---|")
    for et, d in durate:
        A("| %s | %.2f s |" % (et, d))
    A("| **Total** | **%.2f s** |" % sum(d for _e, d in durate))
    A("")
    A("## 2. Cele 50 de întrebări")
    A("")
    A("Fiecare are fișierul ei în `intrebari/v2/raspunsuri/<id>.md` — declarația de dată și perimetru "
      "(C5), răspunsul, citatele verbatim, costul apelului și comparația.")
    A("")
    A("| Id | Tip | Semantic | Lexical | Răspunsul semantic |")
    A("|---|---|---|---|---|")
    for q in qs:
        rs = RS.get(q["id"])
        A("| %s | %s | %s | %s | %s |"
          % (q["id"], q["tip"], ET[CS[q["id"]]["verdict_pe_fond"]] if rs else "—",
             ET[CL[q["id"]]["verdict_pe_fond"]],
             (_s(rs["raspuns"], 70) if rs and rs["stare"] == "RASPUNS"
              else "*%s*" % _s(rs["motiv"], 60) if rs else "—")))
    A("")
    open(os.path.join(DEST, "RAPORT.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    json.dump({"pasi": [{"operatie": e, "secunde": round(d, 2)} for e, d in durate]},
              open(os.path.join(DEST, "durate.json"), "w", encoding="utf-8"), ensure_ascii=False,
              indent=1)
    return C_lex, C_sem, durate


ANALIZA = """
### Cele 7 GREȘIT ale stratului semantic — citite una câte una

Toate au **trecut** verificarea mecanică: citatele sunt literale, cifrele sunt literale. Niciuna nu e o
invenție. Categoriile de mai jos sunt citirea mea, nu un verdict mecanic — de aceea sunt separate de
scor.

| Categorie | Întrebări | Ce s-a întâmplat |
|---|---|---|
| **Regulă generală în loc de regula specială / mai nouă** | Q-PRF-09, Q-SAL-04 | Modelul a citat o regulă încă prezentă în text, dar înlocuită pentru 2026 de una specială: plata anticipată după CF art. 41 alin. (8) în loc de alin. (10^1); facilitatea pentru salariul minim din CF art. 146 (300 lei / 4.300 lei, valorile din 2025) în loc de OUG 89/2025 art. III (200 lei / 4.600 lei, septembrie 2026). **Singura clasă de greșeală reală de fond** — și exact cea pe care verificarea literală nu o poate prinde: citatul e adevărat, doar nu e cel aplicabil. Vezi C17. |
| **Calcul descris în loc de abținere** | Q-CPF-03 | Regula 3 cerea abținere la un calcul; modelul a descris calculul fără rezultat. |
| **Corect pe fond, fără cifra cheii** | Q-CTB-03, Q-CPF-09 | „maximum 65% din cei 100.000 lei" — modelul a refuzat să înmulțească, cum cere decizia C3 (calculatoarele sunt varianta b). „Nu datorează nimic" în loc de „0 lei". |
| **Fapt corect, articol diferit** | Q-SAL-10, Q-CTB-06 | Listate separat, cum cere C2. |

**Un al treilea defect de comparator**, reparat și raportat ca atare: datele scrise în litere („25 iunie
2027") nu erau recunoscute ca fapte, iar la Q-PRF-03 „faptul principal" al cheii devenea data unei
note (03.08.2026). Scorul semantic pe fond: **11 → 12** după reparație; motorul lexical neschimbat
(4 → 4) — deci reparația nu a avut efecte asupra altor chei.

**Incompletitudine detectată**: Q-SAL-09 (INCOMPLETA) — corect, cu faptele care lipsesc: numărul
persoanelor în întreținere, funcția de bază, vârsta. Și Q-SAL-02 (PROCEDURA) — din prudență,
fiindcă termenul depinde de periodicitatea angajatorului, pe care întrebarea nu o spune. La Q-TVA-10 și
Q-PRF-10 modelul s-a abținut spunând că **atomii primiți nu conțin regula** — o limită a căutării, nu
detectarea incompletitudinii.
"""


CERINTE = """
## 0. CERINȚE — decizii de arhitect

### Aplicate în acest pas

| | Decizia | Cum e aplicată |
|---|---|---|
| **C1** | scorul de referință e cel pe fond; abținerile pe INCOMPLETA separat; detectarea incompletitudinii devine capacitate proprie | tabelele de mai sus; capacitatea e în stratul semantic (`stare INCOMPLET`, cu faptele lipsă și atomul care arată dependența) |
| **C2** | notarea rămâne strictă; „fapt corect, articol diferit" listat separat | lista de mai sus |
| **C3 (a)** | model Anthropic ancorat pe atomi; citatele și cifrele verificate mecanic; eșecul devine abținere | `fiscalos/semantic.py`, `verifica()` — probat pe 10 propuneri construite să-l păcălească |
| **C4** | Da/Nu permis când atomul citat conține literal răspunsul | regula 5 din promptul modelului + verificarea literală a citatului decisiv |
| **C5** | fiecare răspuns începe cu data și perimetrul presupus | câmpul `declaratie`, primul în fiecare fișier per întrebare |
| **C6, C7** | luat la cunoștință / ratificat | — |

### De decis

**C13 — Cifrele din întrebare sunt permise în răspuns.** Verificatorul acceptă o cifră care apare
literal în întrebare, chiar dacă nu apare în niciun atom (ex. „cel târziu la 14.05.2026" — data e a
cazului, nu a legii). Consecința: la o întrebare-capcană, modelul poate repeta o cifră greșită din
enunț și verificarea o lasă să treacă. Alternativa strictă — nicio cifră în afara atomilor — ar
transforma în abținere orice răspuns care numește data cazului. *De decis.*

**C14 — „Conține literal răspunsul" (C4), interpretat mecanic.** Codul poate verifica numai că citatul
decisiv e literal în atom; nu poate verifica că acel citat *decide* Da-ul sau Nu-ul — asta rămâne
judecata modelului. *De ratificat sau de strâns.*

**C15 — Fallback server-side la refuz.** Apelurile au `fallbacks: "default"` (recomandarea pentru
`claude-opus-5`): dacă modelul refuză o cerere, API-ul o rulează pe modelul de rezervă ales de
Anthropic. Modelul care a răspuns efectiv e înregistrat la fiecare apel (`apel.model`). *Îl păstrăm?*

**C17 — Regula specială / mai nouă, necontrolată mecanic.** Singura clasă de greșeală reală a
stratului semantic (Q-PRF-09, Q-SAL-04): un atom valabil și citat literal, dar înlocuit, pentru cazul
din întrebare, de o regulă specială (o derogare dintr-o OUG, un alineat nou introdus pentru anul
fiscal). Verificarea literală nu o poate prinde. Două căi, de decis: (a) căutarea aduce în context,
lângă atomul găsit, derogările și alineatele „prin excepție" care îl vizează, iar modelul primește
regula să le verifice; (b) o probă mecanică: dacă în context există un atom mai nou care derogă de la
cel citat, răspunsul devine abținere.

**C16 — Cheia API.** FiscalOS citește numai `~/.fiscalos/api_keys.env` (mod 600) și trece cheia
explicit clientului; nu folosește cheia iConta și nu cade pe variabile de mediu. Valoarea nu apare în
niciun artefact.
"""


if __name__ == "__main__":
    import sys
    sem = None
    f = os.path.join(_RAD, "artefacte", "intrebari", "raspunsuri_semantic.json")
    if os.path.exists(f) and "--fara-semantic" not in sys.argv:
        sem = json.load(open(f, encoding="utf-8"))
    dur = [("Stratul semantic: 50 de apeluri la %s" % sem["model"], sem["secunde_total"] - sem["secunde_index"])] if sem else None
    cl, cs, d = construieste(sem, dur)
    print("lexical pe fond:", cl["scor_referinta_pe_fond"], "| semantic pe fond:",
          cs["scor_referinta_pe_fond"] if cs else "—")
