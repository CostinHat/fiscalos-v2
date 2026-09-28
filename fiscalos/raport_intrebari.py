# -*- coding: utf-8 -*-
"""Livrabilul motorului de intrebari: raport, raspunsurile per intrebare, scorul, duratele MASURATE.

Ruleaza lanţul final (index -> raspunsuri -> comparatie) cronometrat, si scrie intrebari/v1/.
Duratele nu se scriu de mana: se masoara aici.
"""
import json
import os
import time

from fiscalos import comparatie, intrebari

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(_RAD, "intrebari", "v1")
ZIP = "/home/costin/ghid_incoming/fiscalos_intrebari_rezultat.zip"
ET = {"CORECT": "CORECT", "GRESIT": "GREȘIT", "NU_POT": "NU POT RĂSPUNDE"}


def _s(t, n=140):
    t = " ".join(str(t or "").split())
    return (t[:n] + "…") if len(t) > n else t


def construieste():
    durate = []
    t0 = time.time()
    idx = intrebari.Index()
    durate.append(("Index BM25 peste atomii din acte normative (%d atomi)" % idx.N, time.time() - t0))
    t0 = time.time()
    qs = intrebari.incarca_intrebari()
    R = [intrebari.raspunde(q, idx) for q in qs]
    durate.append(("Raspuns la cele %d intrebari" % len(qs), time.time() - t0))
    os.makedirs(os.path.join(DEST, "raspunsuri"), exist_ok=True)
    fis_r = os.path.join(DEST, "raspunsuri.json")
    with open(fis_r, "w", encoding="utf-8") as f:
        json.dump({"_ce": "Raspunsurile finale ale motorului (dupa reparatiile de clasa D4..D15c).",
                   "data_intrebarii": intrebari.DATA_INTREBARII, "raspunsuri": R},
                  f, ensure_ascii=False, indent=1)
    t0 = time.time()
    C = comparatie.compara(fis_r)
    durate.append(("Comparatia cu cheia", time.time() - t0))
    with open(os.path.join(DEST, "comparatie.json"), "w", encoding="utf-8") as f:
        json.dump(C, f, ensure_ascii=False, indent=1)
    ist = json.load(open(os.path.join(_RAD, "artefacte", "intrebari", "istoric_scor.json"),
                         encoding="utf-8"))
    RR = {r["id"]: r for r in R}
    CC = {c["id"]: c for c in C["comparatii"]}

    # ── raspunsurile per intrebare ───────────────────────────────────────────────────────────────
    t0 = time.time()
    for q in qs:
        r, c = RR[q["id"]], CC[q["id"]]
        L = ["# %s — %s" % (q["id"], q["tip"]), "", "**Întrebarea:** %s" % q["intrebare"], "",
             "**Data de referință:** %s (%s)" % (r.get("data_referinta"), r.get("precizie_data")), "",
             "## Răspunsul motorului — %s" % ("RĂSPUNS" if r["stare"] == "RASPUNS"
                                              else "NU POT RĂSPUNDE"), ""]
        if r["stare"] == "RASPUNS":
            L += ["> %s" % _s(r["raspuns"], 900), ""]
        L += ["*Motiv:* %s" % r["motiv"], ""]
        for titlu, lista in (("Argument (atomul care răspunde)", r.get("argument") or []),
                             ("Material (regula cea mai apropiată — NU e răspuns)",
                              r.get("candidati") or [])):
            if not lista:
                continue
            L += ["### %s" % titlu, ""]
            for a in lista:
                v = a["valabilitate"]
                L += ["- **%s** — `%s`" % (a["temei"], a["atom"]),
                      "  - valabil din: %s · la data întrebării: %s%s"
                      % (v.get("valabil_din") or "nedovedit", v.get("la_data_intrebarii"),
                         (" · " + v["nota"]) if v.get("nota") else ""),
                      "  > %s" % _s(a["verbatim"], 700), ""]
        L += ["## Comparația cu cheia — **%s**" % ET[c["verdict"]], "",
              "- *de ce:* %s" % c["de_ce"],
              "- *răspunsul așteptat:* %s" % c["raspuns_asteptat"],
              "- *temeiul așteptat:* %s" % c["temei_asteptat"], ""]
        with open(os.path.join(DEST, "raspunsuri", "%s.md" % q["id"]), "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
    durate.append(("Scrierea celor %d fisiere per intrebare" % len(qs), time.time() - t0))

    s = C["scor"]
    pe_fond = [c for c in C["comparatii"] if c["verdict"] == "CORECT" and c["stare_motor"] == "RASPUNS"]
    abt_inc = [c for c in C["comparatii"] if c["verdict"] == "CORECT" and c["stare_motor"] != "RASPUNS"]
    abt_motive = {c["id"]: RR[c["id"]]["motiv"][:60] for c in abt_inc}

    # ── raportul ─────────────────────────────────────────────────────────────────────────────────
    L = []
    A = L.append
    A("# FiscalOS v2 — Motorul de întrebări: 50 de întrebări, răspunsuri din atomi")
    A("")
    A("Generat %s. Data la care se pun întrebările: **%s**. ZIP: `%s`."
      % (time.strftime("%d.%m.%Y %H:%M"), intrebari.DATA_INTREBARII, ZIP))
    A("")
    A("## Scorul")
    A("")
    A("| | |")
    A("|---|---|")
    A("| **CORECT** | **%d** |" % s["CORECT"])
    A("| **GREȘIT** | **%d** |" % s["GRESIT"])
    A("| **NU POT RĂSPUNDE** | **%d** |" % s["NU_POT"])
    A("")
    A("**Citit corect, cele %d CORECT sunt două lucruri diferite:**" % s["CORECT"])
    A("")
    A("- **%d răspunsuri corecte pe fond** — faptul cerut și articolul corect: %s."
      % (len(pe_fond), ", ".join(c["id"] for c in pe_fond)))
    A("- **%d abțineri pe întrebări INCOMPLETA** — %s. Regula de notare (fixată înainte de "
      "comparație) creditează o abținere pe INCOMPLETA dacă și cheia spune că lipsesc date. Dar "
      "**motorul nu detectează incompletitudinea**: s-a abținut din alt motiv (forma faptului "
      "nerecunoscută, sau judecată Da/Nu). Corecte după regulă, nu după merit. Vezi C1."
      % (len(abt_inc), ", ".join(c["id"] for c in abt_inc)))
    A("")
    A("Pe fond, deci: **%d din 50**. Motorul e un extractor lexical care știe să se abțină: din "
      "50, a dat %d răspunsuri, iar %d dintre ele sunt greșite." %
      (len(pe_fond), s["CORECT"] - len(abt_inc) + s["GRESIT"], s["GRESIT"]))
    A("")
    A("---")
    A("")
    A(CERINTE.strip() % {"n_abt": len(abt_inc), "n_fond": len(pe_fond)})
    A("")
    A("---")
    A("")
    A("## 1. Operațiile rulate, cu durata măsurată")
    A("")
    A("| Operație | Durată |")
    A("|---|---|")
    for et, d in durate:
        A("| %s | %.2f s |" % (et, d))
    A("| **Total rularea finală** | **%.2f s** |" % sum(d for _e, d in durate))
    A("")
    A("Fiecare reparație de clasă a rulat din nou toate cele 50 de întrebări și comparația; "
      "timpul motorului pe fiecare e în tabelul din §3.")
    A("")
    A("## 2. Protocolul — de ce scorul e o măsurătoare, nu o ajustare")
    A("")
    A(PROTOCOL.strip())
    A("")
    A("## 3. Istoricul scorului — fiecare reparație e o clasă, măsurată pe toate 50")
    A("")
    A("| Pas | CORECT | GREȘIT | NU POT | Δ CORECT | Motor | Clasa de defect |")
    A("|---|---|---|---|---|---|---|")
    prev = None
    for x in ist:
        sc = x["scor"]
        d = "" if prev is None else "%+d" % (sc["CORECT"] - prev)
        A("| %s | %d | %d | %d | %s | %s | %s |"
          % (x["eticheta"], sc["CORECT"], sc["GRESIT"], sc["NU_POT"], d,
             ("%.1f s" % x["secunde_motor"]) if x.get("secunde_motor") else "—",
             _s(x["descriere"], 120)))
        prev = sc["CORECT"]
    A("")
    A(ISTORIC_NOTE.strip())
    A("")
    A("## 4. Cele 50 de întrebări")
    A("")
    A("Fiecare are fișierul ei în `intrebari/v1/raspunsuri/<id>.md`: răspunsul, atomul, fragmentul "
      "verbatim, valabilitatea la data întrebării, și comparația cu cheia.")
    A("")
    A("| Id | Tip | Verdict | Răspunsul motorului | Atomul |")
    A("|---|---|---|---|---|")
    for q in qs:
        r, c = RR[q["id"]], CC[q["id"]]
        A("| %s | %s | %s | %s | %s |"
          % (q["id"], q["tip"], ET[c["verdict"]],
             _s(r["raspuns"], 60) if r["stare"] == "RASPUNS" else "*nu pot — %s*" % _s(r["motiv"], 45),
             ("`%s`" % _s(r["argument"][0]["atom"], 55)) if r.get("argument") else "—"))
    A("")
    A("## 5. Unde greșește motorul — clasele rămase")
    A("")
    gr = [c for c in C["comparatii"] if c["verdict"] == "GRESIT"]
    art_ok = [c["id"] for c in gr if c.get("temei_ok") and not c.get("valoare_ok")]
    fapt_ok = [c["id"] for c in gr if c.get("valoare_ok") and c.get("temei_ok") is False]
    A("- **Articolul corect, fraza sau numărul greșit (%d):** %s. Motorul găsește locul, nu "
      "propoziția: un extractor lexical nu știe care dintre alineatele unui articol răspunde la "
      "întrebare. Aceasta e clasa cea mai mare și e un plafon de capacitate, nu un defect de reglaj "
      "— vezi C3." % (len(art_ok), ", ".join(art_ok)))
    A("- **Faptul corect, articolul altul decât al cheii (%d):** %s. Notarea cere ambele; un om "
      "poate rejudeca." % (len(fapt_ok), ", ".join(fapt_ok) or "—"))
    A("- **Restul (%d):** articol și fapt greșite — căutarea lexicală a găsit un loc învecinat "
      "(ex. art. 310^1 în loc de art. 310; bugetele locale în loc de bugetul de stat)."
      % (len(gr) - len(art_ok) - len(fapt_ok)))
    A("")
    with open(os.path.join(DEST, "RAPORT.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    json.dump({"pasi": [{"operatie": e, "secunde": round(d, 2)} for e, d in durate],
               "total_secunde": round(sum(d for _e, d in durate), 2)},
              open(os.path.join(_RAD, "artefacte", "intrebari", "durate.json"), "w",
                   encoding="utf-8"), ensure_ascii=False, indent=1)
    return s, len(pe_fond), len(abt_inc), durate


CERINTE = """
## 0. CERINȚE — decizii de arhitect

**C1 — Cum se numără abținerile pe INCOMPLETA.** Toate cele %(n_abt)d întrebări INCOMPLETA ies
CORECT, fiindcă motorul s-a abținut și cheia spune că lipsesc date. Dar motorul **nu detectează
incompletitudinea** — s-a abținut fiindcă nu recunoaște forma faptului cerut, sau fiindcă întrebarea
cere o judecată. Regula de notare a fost fixată înainte de comparație, deci n-am schimbat-o după.
*De decis:* scorul de referință e cel după regulă (CORECT include abținerile), sau cel pe fond
(%(n_fond)d)? Și: detectarea incompletitudinii intră în motor ca o capacitate de sine stătătoare?
Nu am folosit coloana `tip` ca s-o simulez — o întrebare etichetată INCOMPLETA spune singură ce se
așteaptă, iar folosirea etichetei ar fi fost citirea răspunsului.

**C2 — Notarea cere și faptul, și articolul.** Un răspuns corect în fond, citat de pe alt articol
decât cheia, iese GREȘIT. E sever intenționat: numai valoarea poate fi o coincidență (lecția bancului
de mutații), numai articolul poate fi un extras care nu răspunde. *De decis:* rămâne așa?

**C3 — Plafonul motorului.** Motorul e un extractor lexical (BM25 peste atomi, plus reguli de
structură, vigoare și ierarhie). Nu compune reguli, nu aplică o regulă la fapte, nu calculează decât
„o bază × o cotă". Clasa cea mai mare de greșeli rămase — articolul corect, fraza greșită — e
limita acestui fel de motor. Următorul pas e o decizie de arhitectură: (a) extragere semantică
**ancorată pe atomi** — un model care propune răspunsul, dar orice cifră și orice citat trebuie să
existe verbatim într-un atom, verificat mecanic, ca acum; (b) calculatoare pe clase de calcul
(contribuții salariale, accesorii, TVA dedus), cu parametrii luați din atomi; (c) motorul rămâne un
extractor care se abține des. Nu am început niciuna.

**C4 — Compromisuri ale regulilor de certitudine (D15).** Regula „o judecată Da/Nu nu se dă" a
costat un răspuns corect: Q-CTB-08, unde extrasul era exact regula (dividendele interimare din 2025
rămân la 10%%). A convertit în schimb 10 răspunsuri greșite în abțineri. *De decis:* motorul are voie
să răspundă la o judecată atunci când extrasul conține literal răspunsul?

**C5 — Data întrebării.** O întrebare fără dată e datată la ziua rulării (**2026-09-28**); „în 2026"
înseamnă sfârșitul anului, dar nu după ziua întrebării; o lună înseamnă ultima ei zi. *De decis:*
convenția se păstrează? Alternativa e ca întrebările să-și poarte data explicit.

**C6 — Expunere declarată.** La inspectarea structurii CSV-ului, înainte de instrucțiunea de
orbire, am văzut răspunsurile așteptate pentru Q-TVA-01…04. Motorul nu conține nicio regulă pentru
ele; dintre cele patru, niciuna nu iese CORECT pe fond.

**C7 — Două defecte ale comparatorului, reparate după prima comparație.** Ambele l-au făcut mai
strict: un temei de cheie necitibil trecea drept „îndeplinit" (3 CORECT false), iar articolele
romane nu se citeau. Scorul v0 pe aceleași răspunsuri comise: 5/31/14 cu notarea inițială, 3/33/14
cu cea reparată. *De ratificat.*
"""

PROTOCOL = """
1. Regulile de clasă ale motorului (R-DATA, R-SURSA, R-VERS, R-VALAB, R-PRAG, R-CALC) au fost scrise
   înainte de prima rulare pe întrebări.
2. Motorul e **orb la cheie, mecanic**: citește numai coloanele `id`, `tip`, `intrebare`; numele
   coloanelor cu răspunsul așteptat nu apar în modul (verificat prin AST în `test_intrebari.py`).
3. Răspunsurile v0 au fost **comise înainte ca modulul de comparație să existe**: commit `f1997a8`,
   `artefacte/intrebari/raspunsuri_v0.json`, sha256 `c9af0408…6f9`.
4. Regulile de notare au fost comise **înainte ca comparatorul să citească cheia**.
5. După prima comparație, fiecare reparație a fost o **clasă de defect**, re-rulată pe toate cele
   50 de întrebări; istoricul e în `artefacte/intrebari/istoric_scor.json` și în §3, inclusiv
   reparațiile care n-au schimbat scorul și una care l-a scăzut.
6. Niciun răspuns fără atom: verificat la rulare (`assert`) și în probe; fragmentul citat e verificat
   literal în textul atomului.
"""

ISTORIC_NOTE = """
**Ce nu apare în cifre, dar contează:**

- **D9 a regresat (5 → 4)** și e păstrat în istoric. Extinderea codurilor de formular („D100" →
  „declarație privind obligațiile de plată…") trăgea întrebările de fond spre atomii formularului.
  D9a păstrează numai abrevierile de concepte (TVA, CAS, CAM).
- **D3, D7, D12, D1, D14 n-au schimbat scorul** și sunt păstrate: fiecare a mutat răspunsuri pe atomi
  mai buni, sau a fost condiția pentru altă reparație (D12 a făcut eligibil atomul pe care D13 l-a
  găsit apoi).
- **D11 a fost o ipoteză infirmată de măsurătoare**: presupunerea că Codul fiscal consolidat e depășit
  era falsă — are note până la 01.07.2026. Defectul real era D12.
- **D5 a scăzut scorul (7 → 5) și e corect să-l scadă**: cele două „victorii" pe care le pierde erau
  refuzuri pentru lipsa datei pe întrebări care nu aveau nevoie de dată.
- **Două defecte în propriile mele reparații**, prinse înainte de măsurătoarea următoare: D13 ocolea
  regula de vigoare la coborârea în copii; D1 folosea cuvintele neextinse ale întrebării.
"""


if __name__ == "__main__":
    s, f, a, d = construieste()
    print("scor %s | pe fond %d | abtineri INCOMPLETA %d | %.1f s" % (s, f, a, sum(x for _e, x in d)))
