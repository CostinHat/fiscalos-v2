# -*- coding: utf-8 -*-
"""OP8 — PACHETUL DE PROPUNERE v2: JSON pentru masina, raport pentru om, doua livrabile pentru iConta.

v1 RĂMÂNE NEATINS (propuneri/v1/), cu o singura exceptie ceruta de arhitect: textul C7, care nu
ajunsese in fisier. v2 aplica deciziile C1-C7 si nu rescrie istoria.

CE E NOU IN v2, fiecare din o decizie:
  C2  NEVERIFICAT e stare separata. Sumarul de pe prima pagina numara CONCORDA NUMAI pe temei
      declarat si verificat. Constantele fara temei primesc un TEMEI CANDIDAT - numai din act normativ -
      intr-un fisier separat, livrabil pentru iConta, care NU se aplica.
  C3  conturile se culeg numai din containerele numite CONT de iConta; restul devine CERINTA.
  C4  perechea (atom-valoare, atom-valabilitate); lipsa celui de-al doilea se declara.
  C7  bancul de mutaţii acopera fiecare clasa.

FiscalOS nu are cale de scriere spre iConta (CLAUDE.md §3). Fiecare fisier de aici e o propunere.
"""
import json
import os
import time

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSIUNE = "v2"
STARI = ("CONCORDA", "DIFERA", "NEVERIFICAT", "NEGASIT")
ETICHETA = {"CONCORDA": "CONCORDĂ", "DIFERA": "DIFERĂ", "NEVERIFICAT": "NEVERIFICAT",
            "NEGASIT": "NEGĂSIT"}


def _citeste(nume):
    return json.load(open(os.path.join(_RAD, "artefacte", nume), encoding="utf-8"))


def _tabel(randuri, capete):
    lat = [max([len(str(c))] + [len(str(r[i])) for r in randuri]) for i, c in enumerate(capete)]
    out = ["| " + " | ".join(str(c).ljust(lat[i]) for i, c in enumerate(capete)) + " |",
           "|" + "|".join("-" * (x + 2) for x in lat) + "|"]
    for r in randuri:
        out.append("| " + " | ".join(str(x).ljust(lat[i]) for i, x in enumerate(r)) + " |")
    return "\n".join(out)


def _scurt(t, n=150):
    t = " ".join(str(t or "").split())
    return (t[:n] + "…") if len(t) > n else t


def _valab(p):
    v = p.get("atom_valabilitate")
    if v:
        s = "`%s` din **%s** (%s)" % (v["atom"], v["valabil_din"], v.get("sursa_datei", ""))
        if v.get("nota_data"):
            s += " — ⚠ " + v["nota_data"]
        return s
    if p.get("valabilitate_lipsa"):
        return "**LIPSĂ** — " + p["valabilitate_lipsa"]
    return "—"


def _cerinte_iconta(inv, P):
    """Ce ar trebui sa schimbe iConta ca FiscalOS sa poata verifica mai mult. Nu se aplica nimic."""
    cn = inv.get("conturi_nemarcate", {})
    cer = [{
        "id": "R-CONT-1",
        "decizie": "C3",
        "ce": "Marcarea explicita a simbolurilor de cont.",
        "de_ce": ("%d simboluri de 3-4 cifre, in %d module din core/, nu stau in niciun container "
                  "numit CONT. Multe sunt conturi reale folosite ca literale directe "
                  "(`startswith(\"401\")`, tuple pozitionale), dar nu se pot distinge de un an sau de "
                  "un rand de formular fara o modificare in iConta. De aceea NU sunt in propunere."
                  % (cn.get("n_simboluri", 0), cn.get("n_module", 0))),
        "propunere": ("Un container sau un tip numit (ca `Temei`) pentru conturi - de ex. "
                      "`CONTURI_<scop> = (...)` sau `Cont(\"4426\")` -, ca inventarul sa le culeaga "
                      "mecanic, fara euristica."),
        "exemple": cn.get("exemple", [])[:15],
    }]
    for p in P:
        if p["clasa"] == "cont" and p["clasificare"] == "NEGASIT":
            cer.append({"id": "R-CONT-%s" % p["valoare_cod"], "decizie": "C3",
                        "ce": "Contul %s nu exista in niciun plan de conturi din corpus."
                              % p["valoare_cod"],
                        "de_ce": p["motiv"], "unde": p["unde_in_cod"],
                        "propunere": "De clarificat: alt nomenclator (cod de cont bugetar?) sau "
                                     "cont inexistent in plan."})
    n_cand = sum(1 for p in P if p.get("temei_candidat"))
    cer.append({"id": "R-TEMEI-1", "decizie": "C2",
                "ce": "Temei structurat (`Temei(...)`) pentru constantele nesursate.",
                "de_ce": ("Pentru %d constante fara temei, FiscalOS propune un TEMEI CANDIDAT din "
                          "act normativ (temeiuri_candidate.json). E o propunere de aprobat uman, "
                          "nu o verificare." % n_cand),
                "propunere": "Dupa aprobare, iConta scrie temeiul in cod, ca obiect `Temei`."})
    for p in P:
        if p.get("clasificare_initiala"):
            cer.append({"id": "R-SURSA-%s" % p["parametru"].split("/")[-1], "decizie": "C2",
                        "ce": "Temei declarat pe o sursa care nu e act normativ: %s."
                              % p["parametru"],
                        "de_ce": p["motiv"],
                        "propunere": "Inlocuirea citarii cu actul normativ (MO) care stabileste "
                                     "valoarea."})
    return cer


def construieste():
    man = json.load(open(os.path.join(_RAD, "corpus_manifest.json"), encoding="utf-8"))
    strat = _citeste("strat_text.json")
    atomi = _citeste("atomi_raport.json")
    inv = _citeste("inventar_iconta.json")
    pot = _citeste("potriviri.json")
    durate = _citeste("durate.json")
    banc = _citeste("banc_mutatii.json")

    dest = os.path.join(_RAD, "propuneri", VERSIUNE)
    os.makedirs(dest, exist_ok=True)
    P = pot["potriviri"]
    n = {k: sum(1 for p in P if p["clasificare"] == k) for k in STARI}
    candidate = [p for p in P if p.get("temei_candidat")]
    cerinte = _cerinte_iconta(inv, P)

    # ── livrabilele pentru iConta ────────────────────────────────────────────────────────────────
    with open(os.path.join(dest, "temeiuri_candidate.json"), "w", encoding="utf-8") as f:
        json.dump({
            "_ce": "TEMEIURI CANDIDATE pentru constantele pe care iConta nu le sursează. Livrabil "
                   "pentru iConta, DE APROBAT UMAN. NU se aplica. Fiecare candidat vine dintr-un act "
                   "normativ (decizia C2: un formular, o structura de declaratie sau un pliant ANAF "
                   "nu poate fi temei), si e gasit prin potrivire pe fraza-subiect, nu verificat.",
            "versiune": VERSIUNE, "aprobare": "NEAPROBAT",
            "candidati": [{"parametru": p["parametru"], "valoare_cod": p["valoare_cod"],
                           "unde_in_cod": p["unde_in_cod"], "atom": p["temei_candidat"]["atom"],
                           "act": p["temei_candidat"]["act"], "valoare_in_text": p["valoare_lege"],
                           "verbatim": p["atom_verbatim"],
                           "valabilitate": p.get("atom_valabilitate") or p.get("valabilitate_lipsa")}
                          for p in candidate]}, f, ensure_ascii=False, indent=1)
    with open(os.path.join(dest, "cerinte_iconta.json"), "w", encoding="utf-8") as f:
        json.dump({"_ce": "Cerinte pentru iConta, rezultate din propunerea %s. Nu se aplica nimic "
                          "automat." % VERSIUNE, "cerinte": cerinte}, f, ensure_ascii=False, indent=1)

    # ── JSON-ul propunerii ───────────────────────────────────────────────────────────────────────
    with open(os.path.join(dest, "propunere.json"), "w", encoding="utf-8") as f:
        json.dump({
            "_ce": "PROPUNERE FiscalOS v2. NU se aplica automat in iConta (CLAUDE.md §3).",
            "versiune": VERSIUNE, "generat_la": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "aprobare": {"stare": "NEAPROBAT", "de_cine": None, "la": None},
            "decizii_aplicate": ["C1", "C2", "C3", "C4", "C5", "C7"],
            "corpus": {"sursa": man["sursa"], "luat_la": man["luat_la"],
                       "n_fisiere": man["n_fisiere"], "manifest": "corpus_manifest.json"},
            "sumar": {**n, "citari_declarate_de_iconta": pot["citari_declarate"],
                      "citari_rezolvate_in_corpus": pot["citari_rezolvate"],
                      "temeiuri_candidate": len(candidate)},
            "parametri": P, "cerinte_iconta": cerinte,
            "durate_masurate": durate, "dovada_inversa": banc,
        }, f, ensure_ascii=False, indent=1, sort_keys=True)

    # ── raportul ─────────────────────────────────────────────────────────────────────────────────
    L = []
    A = L.append
    A("# FiscalOS v2 — PROPUNERE %s: parametrii fiscali ai iConta confruntați cu corpusul"
      % VERSIUNE)
    A("")
    A("Generat %s · **NEAPROBAT** · nu se aplică automat în iConta (CLAUDE.md §3). "
      "Versiunea anterioară, `propuneri/v1/`, rămâne neatinsă." % time.strftime("%d.%m.%Y %H:%M"))
    A("")
    A("| | |")
    A("|---|---|")
    A("| **CONCORDĂ** — pe temei declarat și verificat | **%d** |" % n["CONCORDA"])
    A("| **DIFERĂ** | **%d** |" % n["DIFERA"])
    A("| NEVERIFICAT — *gri: nu e verdict, e probă de aprobat* | %d |" % n["NEVERIFICAT"])
    A("| **NEGĂSIT** | **%d** |" % n["NEGASIT"])
    A("| Parametri inventariați | %d |" % len(P))
    A("| Citări declarate de iConta / rezolvate în corpus | %d / %d |"
      % (pot["citari_declarate"], pot["citari_rezolvate"]))
    A("| Temeiuri candidate propuse (din act normativ, de aprobat) | %d |" % len(candidate))
    A("| Dovada inversă — greșeli injectate care ies DIFERĂ/NEGĂSIT | %d / %d |"
      % (banc["n_trec"], banc["n_trec"] + banc["n_pica"]))
    A("")
    A("---")
    A("")
    A("## 0. CERINȚE")
    A("")
    A(CERINTE_RATIFICATE.strip())
    A("")
    A(CERINTE_NOI.strip() % {
        "n_scris": sum(1 for p in P if p.get("clasificare_initiala")),
        "n_cand": len(candidate), "n_nemarcate": inv["conturi_nemarcate"]["n_simboluri"],
        "n_module": inv["conturi_nemarcate"]["n_module"]})
    A("")
    A("---")
    A("")

    A("## 1. Operațiile rulate, cu durata măsurată")
    A("")
    A(_tabel([[d["operatie"], "%.2f s" % d["secunde"],
               _scurt(json.dumps(d["rezumat"], ensure_ascii=False), 80)] for d in durate["pasi"]],
             ["Operație", "Durată", "Rezultat"]))
    A("")
    A("Total măsurat: **%.2f s** (din `artefacte/durate.json`, scris de `ruleaza_tot.py`)."
      % durate["total_secunde"])
    A("")

    A("## 2. Corpusul")
    A("")
    A("Instantaneu din `%s`, doar citire, %d fișiere, manifest SHA256 în `corpus_manifest.json` "
      "(C1: corpusul rămâne în `.gitignore`, manifestul e proba). %s atomi în %d acte; "
      "%d acte normative, %d surse care nu pot fi temei (formulare, structuri de declarație, "
      "pliante ANAF, note redactate de iConta)."
      % (man["sursa"], man["n_fisiere"], format(atomi["n_atomi"], ",").replace(",", "."),
         atomi["n_acte"], pot.get("n_acte_normative", 0), pot.get("n_acte_nenormative", 0)))
    A("")

    A("## 3. Rezultatul, pe clase")
    A("")
    clase = sorted({p["clasa"] for p in P})
    A(_tabel([[c] + [sum(1 for p in P if p["clasa"] == c and p["clasificare"] == k) for k in STARI]
              for c in clase], ["Clasă"] + [ETICHETA[k] for k in STARI]))
    A("")

    A("## 4. Registrul `COTE` al iConta — valoare și valabilitate, în pereche")
    A("")
    A("C4: fiecare verdict citează **atomul valorii** și **atomul valabilității**. Când al doilea "
      "lipsește, se spune. O dată de consolidare e data ultimei modificări a *textului*, nu neapărat "
      "a valorii — nepotrivirile de dată se arată (⚠), nu se clasifică.")
    A("")
    for p in sorted((x for x in P if x["parametru"].startswith("cote/")),
                    key=lambda x: (x["nume"], x["valabil_din_cod"] or "")):
        A("### `%s` — **%s**" % (p["parametru"], ETICHETA[p["clasificare"]]))
        A("")
        A("- **cod iConta:** `%s` din %s — %s" % (p["valoare_cod"], p["valabil_din_cod"],
                                                 p["unde_in_cod"]))
        A("- **temei declarat:** %s" % (p["temei_declarat_de_iconta"] or "—"))
        if p["atom"]:
            A("- **atom-valoare:** `%s` → `%s`" % (p["atom"], p["valoare_lege"]))
            A("- **atom-valabilitate:** %s" % _valab(p))
            A("")
            A("  > %s" % _scurt(p["atom_verbatim"], 420))
        if p["clasificare"] in ("NEVERIFICAT", "NEGASIT") or p.get("nota"):
            A("")
            A("  *%s*" % _scurt(p.get("nota") or p["motiv"], 300))
        A("")

    A("## 5. DIFERĂ — ambele părți")
    A("")
    dif = [p for p in P if p["clasificare"] == "DIFERA"]
    if not dif:
        A("Niciun parametru.")
    for p in dif:
        A("### `%s`" % p["parametru"])
        A("")
        A("- **cod iConta:** `%s` — %s" % (p["valoare_cod"], p["unde_in_cod"]))
        A("- **textul legii:** `%s` — atom `%s`" % (p["valoare_lege"], p["atom"]))
        if p.get("doar_in_cod") is not None:
            A("- **numai în cod:** %s · **numai în act:** %s"
              % (p["doar_in_cod"] or "—", p["doar_in_act"] or "—"))
        A("")
        A("  > %s" % _scurt(p["atom_verbatim"], 500))
        A("")
        A("  *%s*" % _scurt(p["motiv"], 300))
        A("")

    A("## 6. NEVERIFICAT — probă de aprobat, nu verdict")
    A("")
    nv = [p for p in P if p["clasificare"] == "NEVERIFICAT"]
    din_decl = [p for p in nv if p.get("clasificare_initiala")]
    din_cand = [p for p in nv if p.get("temei_candidat")]
    A("**%d** parametri. Două feluri, cu motive diferite:" % len(nv))
    A("")
    A("**a) Temei declarat de iConta, dar pe o sursă care nu e act normativ (%d).** Verificarea s-a "
      "făcut, dar pe o notă redactată de iConta sau pe un pliant — deci nu e o verificare pe lege. "
      "Rezultatul inițial e păstrat." % len(din_decl))
    A("")
    if din_decl:
        A(_tabel([[p["parametru"], p["valoare_cod"], ETICHETA[p["clasificare_initiala"]],
                   p["atom"].split("#")[0]] for p in din_decl],
                 ["Parametru", "Cod", "Inițial", "Sursa citată"]))
        A("")
    A("**b) Constantă fără temei, cu TEMEI CANDIDAT dintr-un act normativ (%d).** Lista completă, "
      "cu fragmentul verbatim, e în `temeiuri_candidate.json` — livrabil pentru iConta, **de aprobat "
      "uman, nu se aplică**." % len(din_cand))
    A("")
    if din_cand:
        A(_tabel([[p["parametru"], p["valoare_cod"], p["temei_candidat"]["atom"],
                   _scurt(p["valoare_lege"], 14)] for p in din_cand],
                 ["Parametru", "Cod", "Temei candidat", "În text"]))
        A("")
    rest = [p for p in nv if p not in din_decl and p not in din_cand]
    if rest:
        A("**c) Fără temei și fără candidat (%d)** — valoarea apare doar în surse care nu pot fi "
          "temei:" % len(rest))
        A("")
        for p in rest:
            A("- `%s` = `%s` — %s" % (p["parametru"], p["valoare_cod"], _scurt(p["motiv"], 160)))
        A("")

    A("## 7. NEGĂSIT — și de ce")
    A("")
    grupe = {}
    for p in (x for x in P if x["clasificare"] == "NEGASIT"):
        m = p["motiv"]
        g = ("parametru operațional, fără act normativ de citat" if "OPERATIONAL" in m else
             "normă deschisă — nu există enumerare de confirmat" if "nu inchide lista" in m else
             "cont folosit de iConta, absent din planurile de conturi din corpus"
             if p["clasa"] == "cont" else
             "potrivire prea slabă ca să susțină un verdict" if "prea slab" in m else
             "altul")
        grupe.setdefault(g, []).append(p)
    for g in sorted(grupe):
        A("**%s** (%d):" % (g, len(grupe[g])))
        A("")
        for p in sorted(grupe[g], key=lambda x: x["parametru"]):
            A("- `%s` = `%s` — %s" % (p["parametru"], _scurt(p["valoare_cod"], 30),
                                     _scurt(p["unde_in_cod"], 90)))
        A("")

    A("## 8. Termene și nomenclatoare")
    A("")
    for p in sorted((x for x in P if x["clasa"] in ("termen", "nomenclator")),
                    key=lambda x: x["parametru"]):
        A("- **`%s`** = `%s` → **%s** · atom `%s`"
          % (p["parametru"], _scurt(p["valoare_cod"], 40), ETICHETA[p["clasificare"]],
             p["atom"] or "—"))
        if p.get("doar_in_act"):
            A("  - numai în act: %s — numai în cod: %s" % (p["doar_in_act"], p["doar_in_cod"] or "—"))
        if p["atom_verbatim"]:
            A("  > %s" % _scurt(p["atom_verbatim"], 220))
    A("")

    A("## 9. Conturi")
    A("")
    A("C3: se culeg **numai** simbolurile din containerele pe care iConta le numește CONT "
      "(`CONTURI_TVA`, `CONT_AVANS`, `cont_imo`…). Confruntate cu planurile de conturi din corpus: "
      "OMFP 1802/2014 (entități economice) și OMFP 3103/2017 (entități fără scop patrimonial) — "
      "%d simboluri citite." % pot["n_conturi_in_plan_din_corpus"])
    A("")
    ct = sorted((p for p in P if p["clasa"] == "cont"), key=lambda x: x["valoare_cod"])
    A(_tabel([[p["valoare_cod"], ETICHETA[p["clasificare"]],
               _scurt(p["valoare_lege"] or "—", 58),
               "; ".join(x.split(" (")[0] for x in (p.get("planuri") or []))] for p in ct],
             ["Cont", "Stare", "Denumire în plan", "Plan"]))
    A("")

    A("## 10. Cerințe pentru iConta")
    A("")
    A("Ce ar trebui schimbat în iConta ca FiscalOS să poată verifica mai mult. **Nu se aplică "
      "nimic** — lista e și în `cerinte_iconta.json`.")
    A("")
    for c in cerinte:
        A("- **%s** (%s) — %s %s" % (c["id"], c["decizie"], c["ce"], _scurt(c.get("de_ce", ""), 220)))
    A("")

    A("## 11. Dovada în cealaltă direcție — bancul de mutații, pe fiecare clasă")
    A("")
    A("C7: cel puțin o mutație pe fiecare clasă, care trebuie să iasă DIFERĂ sau NEGĂSIT cu motivul "
      "corect. Injectate pe o **copie în memorie** a inventarului — niciodată în iConta.")
    A("")
    A("**Rezultat: %d din %d trec.**" % (banc["n_trec"], banc["n_trec"] + banc["n_pica"]))
    A("")
    A(_tabel([[x["clasa"], x["mutaţie"], "%s → %s" % (_scurt(x["valoare_reala_in_cod"], 14),
                                                     _scurt(x["valoare_injectata"], 14)),
               ETICHETA.get(x["mutant"]["clasificare"], x["mutant"]["clasificare"]),
               _scurt(x["mutant"]["valoare_lege"] or (x["mutant"].get("doar_in_act") or "")
                      or x["mutant"]["motiv"], 40)]
              for x in banc["mutaţii"]],
             ["Clasă", "Mutație", "Cod → injectat", "Ieșit", "Lege / motiv"]))
    A("")
    A("La **citarea greșită** (CAS 25%, corect, dar cu temei HG 146/2026): `NEGĂSIT` cu "
      "`citare_rezolvata=False`. Nu CONCORDĂ, deși valoarea e corectă — întrebarea e și *duce proba "
      "unde spune?* Nu DIFERĂ, fiindcă actul citat nu spune altceva: nu spune nimic despre CAS.")
    A("")
    A("---")
    A("")
    A("## Aprobare")
    A("")
    A("Propunerea e **NEAPROBATĂ**. Se aprobă în `propuneri/%s/APROBARE.md`. FiscalOS nu are cale "
      "de scriere spre iConta." % VERSIUNE)
    with open(os.path.join(dest, "RAPORT.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")

    with open(os.path.join(dest, "APROBARE.md"), "w", encoding="utf-8") as f:
        f.write(APROBARE % dict(versiune=VERSIUNE, data=time.strftime("%d.%m.%Y"),
                                **{k.lower(): n[k] for k in STARI}, cand=len(candidate)))
    return {"dest": dest, "sumar": n, "n_parametri": len(P), "candidate": len(candidate)}


CERINTE_RATIFICATE = """
### Deciziile arhitectului, aplicate în v2

| | Decizie | Cum e aplicată |
|---|---|---|
| **C1** | corpusul rămâne în `.gitignore`, manifestul SHA e proba | neschimbat |
| **C2** | ancora slabă nu intră în CONCORDĂ: stare separată **NEVERIFICAT**; constantele fără temei primesc un **temei candidat** numai din act normativ, livrabil pentru iConta, neaplicat | §6, `temeiuri_candidate.json`; clasificatorul de surse e `fiscalos/surse.py` |
| **C3** | conturile se culeg numai de unde iConta le folosește ca conturi; restul devine cerință pentru iConta | §9, §10 (R-CONT-1) |
| **C4** | perechea (atom-valoare, atom-valabilitate); lipsa se declară | §4 |
| **C5** | inventarul nu se extinde | neschimbat |
| **C7** | regula ratificată; bancul acoperă fiecare clasă | §11 |
| **C6** | motorul de întrebări | pasul următor, livrat separat |
"""

CERINTE_NOI = """
### Cerințe noi, de decis

**C8 — Am aplicat C2 și temeiurilor DECLARATE, nu doar celor candidate.** C2 spune că un formular
sau un pliant nu poate fi temei. Aplicată consecvent, regula lovește și %(n_scris)d intrări din
registrul `COTE`: cotele reduse de TVA din 2016 citează nota `cf_art291_2016_forma_initiala`, pe care
`PROVENIENTA.json` a iConta o clasifică ea însăși `SCRIS` (redactată de ei), iar tichetele de masă din
2025 citează pliantul `anaf_limite_2025`. O valoare „verificată" pe o notă scrisă de cel verificat e o
tautologie. Ele ies acum NEVERIFICAT, cu rezultatul inițial păstrat în `clasificare_initiala`.
*De decis:* extensia se ratifică, sau C2 se aplică numai temeiurilor candidate?

**C9 — Un nomenclator care e o submulțime strictă a normei iese DIFERĂ.** `d394.TIPURI`: OPANAF
2194/2025 enumeră `L/A/LS/AS/AÎ/V/C/N/Î1/Î2`, codul are aceleași opt fără `Î1/Î2`. iConta scrie în
`nomenclatoare.py` că `Î1/Î2` sunt secțiunile de încasări prin AMEF, neconstruite încă — deci nu e o
valoare greșită, ci o acoperire incompletă, declarată. Vechiul prag de 80%% o ascundea.
*De decis:* rămâne DIFERĂ (cu ambele părți, cum e acum), sau o acoperire incompletă declarată de
iConta e o stare separată?

**C10 — Temeiurile candidate sunt găsite prin potrivire pe frază, nu verificate.** %(n_cand)d
candidați, toți din acte normative, fiecare cu fragmentul verbatim. Frazele-subiect le-am scris citind
ce face fiecare modul iConta (de ex. `casa.py` spune în antet că plafoanele sunt din Legea 70/2015).
Doi candidați pentru plafoanele de numerar trimit la actele care au *modificat* Legea 70/2015 (OUG
115/2023, Legea 296/2023), nu la Legea 70/2015 însăși. *De decis:* un candidat poate fi actul
modificator, sau trebuie să fie întotdeauna actul de bază, consolidat?

**C11 — Unitatea unei constante nesursate se citește din folosirea ei.** `d216.COTA_IMPOZIT = 0.3`
e folosită ca `baza * COTA_IMPOZIT / 100`, deci înseamnă 0,3%%, nu 30%% (cum stă în registrul `COTE`,
unde ratele sunt fracții). Fără această citire, potrivirea îi găsea un „temei" în normele despre
impozitul pe clădiri. Regula e: `NUME / 100` în modul ⇒ procent literal. *De decis:* se acceptă, sau
iConta își declară unitatea explicit (cerință R-UNIT)?
"""

APROBARE = """# APROBARE — propunere %(versiune)s

`propuneri/%(versiune)s/` — `propunere.json`, `RAPORT.md`, `temeiuri_candidate.json`,
`cerinte_iconta.json` — generate la %(data)s:

- CONCORDĂ (pe temei declarat verificat): **%(concorda)d**
- DIFERĂ: **%(difera)d**
- NEVERIFICAT: **%(neverificat)d**
- NEGĂSIT: **%(negasit)d**
- Temeiuri candidate propuse: **%(cand)d**

FiscalOS **nu are cale de scriere spre iConta**. Aplicarea oricărui rând — inclusiv a unui temei
candidat — e un pas uman, separat.

## Semnătură

- [ ] Am citit §0 și am răspuns la C8–C11.
- [ ] Am verificat prin eșantion fragmentele verbatim la id-ul de atom indicat.
- [ ] Aprob propunerea în întregime.
- [ ] Aprob parțial — rândurile refuzate, cu motiv:

```
(rândurile refuzate)
```

- [ ] Aprob temeiurile candidate: toate / numai cele de mai jos:

```
(parametru → temei aprobat)
```

Aprobat de: ______________________  Data: ____________

Stare: **NEAPROBAT**
"""


if __name__ == "__main__":
    t0 = time.time()
    r = construieste()
    print("propunere %s: %s | %d parametri | %d candidati | %.1f s"
          % (VERSIUNE, r["sumar"], r["n_parametri"], r["candidate"], time.time() - t0))
