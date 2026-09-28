# -*- coding: utf-8 -*-
"""OP8 — PACHETUL DE PROPUNERE v4 (peste v3: stratul de surse oficiale, C12): JSON pentru masina, raport pentru om, doua livrabile pentru iConta.

v1 si v2 RĂMÂN NEATINSE (propuneri/v1/, propuneri/v2/); probe le ingheata. v3 aplica, peste deciziile
C1-C7 ale v2, deciziile C8-C11:
  C8   o nota sau un pliant scris de iConta nu poate verifica iConta (ratificat, aplicat din v2)
  C9   d394.TIPURI rămâne DIFERA, cu mentiunea VERBATIM a dezacordului declarat de iConta
  C10  temeiul candidat e actul de BAZA consolidat; actul modificator e atom-valabilitate; cand
       actul de baza lipseste din corpus (sau e acolo fara valoare), se scrie explicit
  C11  unitatea citita din folosire e marcata "unitate dedusa"; R-UNIT intra in cerinte

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
VERSIUNE = "v4"
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
    unit = [p for p in P if p.get("unitate_dedusa")]
    if unit:
        cer.append({"id": "R-UNIT", "decizie": "C11",
                    "ce": "Unitatea declarata explicit pentru constantele-rata nesursate.",
                    "de_ce": ("Registrul COTE tine ratele ca fractii (0.21 = 21%%), dar %d constante "
                              "nesursate sunt procente literale (0.3 = 0,3%%) - FiscalOS le-a dedus "
                              "unitatea din folosire (`NUME / 100`): %s."
                              % (len(unit), ", ".join(p["parametru"] for p in unit))),
                    "propunere": "Un tip sau o conventie declarata (ex. `Procent(\"0.3\")` fata de "
                                 "`Fractie(\"0.003\")`), ca unitatea sa nu mai fie dedusa."})
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
    # ── C12: actele aduse din sursa oficiala - lista e LIVRABIL pentru iConta (anaf_surse) ───────
    from fiscalos import potrivire as _pot
    man_of = json.load(open(os.path.join(_RAD, "surse_oficiale", "MANIFEST.json"), encoding="utf-8"))
    corp_ = _pot.Corpus()
    acte_aduse = []
    for act, v in man_of["acte"].items():
        sa = corp_.sursa_act.get(act, {})
        acte_aduse.append({
            "act_in_anaf_surse": act, "id_portal": v["id_portal"], "de_ce": v["de_ce"],
            "data_formei_consolidate": v["data_formei_consolidate"],
            "folosit_de_FiscalOS": sa.get("sursa", "").startswith("oficial"),
            "motiv_nefolosire": sa.get("oficial_neaplicat"),
            "atomi_oficial": sa.get("atomi_oficial"), "atomi_instantaneu": sa.get("atomi_instantaneu"),
            "fisiere": [{k: x[k] for k in ("fisier", "url", "id_portal", "consolidare", "sha256",
                                         "octeti", "articole")} for x in v["fisiere"]]})
    with open(os.path.join(dest, "acte_aduse.json"), "w", encoding="utf-8") as f:
        json.dump({"_ce": "Consolidatele la zi aduse de FiscalOS din legislatie.just.ro (C12), cu "
                          "provenienta, data formei consolidate si SHA256. Livrabil pentru iConta: "
                          "le poate prelua in anaf_surse. Fisierele sunt in surse_oficiale/.",
                   "sursa": man_of["sursa"], "adus_la": man_of["adus_la"],
                   "cum_se_ajunge_la_text": "Pentru actele mari, pagina actului de aprobare e un ciot "
                   "cu o trimitere S_REF catre documentul care conţine codul/normele "
                   "(DetaliiDocumentAfis/<id>). Raspunde limitei notate in PORTAL_IDS.json.",
                   "acte": acte_aduse}, f, ensure_ascii=False, indent=1)
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
            "decizii_aplicate": ["C1", "C2", "C3", "C4", "C5", "C7", "C8", "C9", "C10", "C11", "C12"],
            "acte_aduse_din_sursa_oficiala": acte_aduse,
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
      "Versiunile anterioare, `propuneri/v1/`–`propuneri/v3/`, rămân neatinse." % time.strftime("%d.%m.%Y %H:%M"))
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
    A(CERINTE_NOI.strip() and CERINTE_NOI.strip() % {
        "n_scris": sum(1 for p in P if p.get("clasificare_initiala")),
        "n_cand": len(candidate), "n_nemarcate": inv["conturi_nemarcate"]["n_simboluri"],
        "n_module": inv["conturi_nemarcate"]["n_module"],
        "n_rest": sum(1 for p in P if p["clasificare"] == "NEVERIFICAT"
                      and not p.get("temei_candidat") and not p.get("clasificare_initiala"))})
    A("")
    A("---")
    A("")

    A("## Actele aduse din sursa oficială (C12)")
    A("")
    A("Stratul `surse_oficiale/`, separat de instantaneul iConta (care rămâne neatins). Lista e "
      "**livrabil pentru iConta** — `acte_aduse.json`, cu URL, data formei consolidate și SHA256 — "
      "ca să le poată prelua în `anaf_surse`.")
    A("")
    A(_tabel([[x["act_in_anaf_surse"], x["id_portal"], x["data_formei_consolidate"],
               "%s → %s" % (x["atomi_instantaneu"], x["atomi_oficial"]),
               "da" if x["folosit_de_FiscalOS"] else "**nu** — %s" % x["motiv_nefolosire"]]
              for x in acte_aduse],
             ["Act", "Id portal", "Forma consolidată din", "Atomi (instantaneu → oficial)",
              "Folosit"]))
    A("")
    A("**Pentru iConta, și dincolo de lista aceasta:** la actele mari (Codul fiscal, Codul de "
      "procedură fiscală, normele), pagina de pe portal a actului de aprobare e un ciot, iar textul "
      "stă într-un document separat, legat prin trimiterea `S_REF` (`DetaliiDocumentAfis/<id>`). "
      "E răspunsul la limita notată în `PORTAL_IDS.json` (*forma consolidată la alt id, negăsit*).")
    A("")
    A("**Candidații pentru plafoanele de numerar** trimit acum la actul de bază consolidat — Legea "
      "70/2015 art. 3–4 —, cum cere C10. Litera din articol e aleasă prin potrivire pe frază, iar "
      "două atribuiri arată greșit la citire: `casa.PLAFON_PLATA_PJ` (plăți) primește lit. a), care "
      "e despre încasări; `casa.PLAFON_PF` primește art. 3 alin. (2), deși regula pentru persoane "
      "fizice pare să fie art. 4. De verificat la aprobare.")
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
        dz = p.get("dezacord_declarat_de_iconta")
        if dz:
            A("- **iConta declară ea însăși** (`%s`, verbatim, C9):" % dz["unde"])
            A("  > %s" % dz["ce"])
            A("  > *Consecința declarată:* %s" % dz["consecinta"])
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
        A("C10: temeiul candidat e **actul de bază consolidat**; actul modificator care a introdus "
          "valoarea apare în coloana de valabilitate, nu ca temei.")
        A("")
        A(_tabel([[p["parametru"] + (" ⚠ unitate dedusă" if p.get("unitate_dedusa") else ""),
                   p["valoare_cod"], p["temei_candidat"]["atom"], _scurt(p["valoare_lege"], 14),
                   ((p.get("atom_valabilitate") or {}).get("atom") or "—")
                   if not (p.get("atom_valabilitate") or {}).get("acelasi_cu_atomul_valorii")
                   else "același atom (%s)" % p["atom_valabilitate"]["valabil_din"]]
                  for p in din_cand],
                 ["Parametru", "Cod", "Temei candidat (act de bază)", "În text",
                  "Atom-valabilitate"]))
        A("")
    rest = [p for p in nv if p not in din_decl and p not in din_cand]
    if rest:
        A("**c) Fără temei candidat (%d)** — valoarea apare numai într-un act modificator, iar C10 "
          "interzice propunerea lui ca temei. Pentru fiecare, actul de bază pe care îl modifică "
          "(citit din textul modificatorului) și dacă e în corpus:" % len(rest))
        A("")
        A(_tabel([[p["parametru"] + (" ⚠ unitate dedusă" if p.get("unitate_dedusa") else ""),
                   p["valoare_cod"],
                   (p.get("act_de_baza") or {}).get("citit_din_modificator") or "necitibil",
                   ("`%s` — **e în corpus, valoarea negăsită lângă fraza-subiect: de verificat**"
                    % p["act_de_baza"]["in_corpus"]) if (p.get("act_de_baza") or {}).get("in_corpus")
                   else "**LIPSEȘTE din corpus**",
                   ((p.get("atom_valabilitate") or {}).get("atom") or "—")]
                  for p in rest],
                 ["Parametru", "Cod", "Actul de bază modificat", "În corpus?",
                  "Atom-valabilitate (modificator)"]))
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
| **C8** | o notă sau un pliant scris de iConta nu poate verifica iConta | §6 a) — aplicat din v2, acum ratificat |
| **C9** | `d394.TIPURI` rămâne DIFERĂ, cu mențiunea că iConta declară Î1/Î2 neconstruite | §5 — mențiunea e obiectul `Dezacord` al iConta, citat verbatim, nu parafrazat |
| **C10** | temeiul candidat = actul de bază consolidat; modificatorul = atom-valabilitate; lipsa se scrie | §6 b) și c) |
| **C11** | unitatea din folosire se acceptă, marcată „unitate dedusă"; R-UNIT în cerințe | §6, §10 |
| **C12** | consolidatele la zi ale actelor de bază, aduse din legislatie.just.ro, într-un strat propriu | secțiunea „Actele aduse", `acte_aduse.json`, `surse_oficiale/MANIFEST.json` |
| **C6** | motorul de întrebări | livrat separat, în `intrebari/` |
"""

CERINTE_NOI = """
### Cerințe noi, de decis

**C18 — Litera aleasă prin potrivire pe frază, în candidații din Legea 70/2015.** Cu actul de bază
consolidat în corpus (C12), toți cei cinci candidați pentru plafoanele de numerar trimit la articolul
corect, dar litera o alege potrivirea pe frază, iar două atribuiri arată greșit la citire. *De decis:*
se lasă verificarea literei la aprobarea umană (cum e acum), sau candidatul se propune la nivel de
articol când mai multe litere ale lui poartă valoarea?

**C19 — OPANAF 3769/2015 de pe portal e mai sărac decât instantaneul.** Portalul are textul
ordinului (consolidat la 17.09.2025), dar nu și anexele cu instrucțiunile D394 - 25 de atomi față de
104. FiscalOS nu l-a folosit (regula: un act oficial înlocuiește instantaneul numai dacă nu e mai
sărac). *De decis:* anexele se caută în altă sursă oficială (static.anaf.ro), sau rămâne instantaneul?
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

- [ ] Am citit §0 și am răspuns la C18–C19.
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
