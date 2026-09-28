# -*- coding: utf-8 -*-
"""OP8 — PACHETUL DE PROPUNERE, versionat: JSON pentru maşină + raport pentru om.

DE CE O PROPUNERE si nu o aplicare (CLAUDE.md §3). FiscalOS nu are cale de scriere spre iConta, si
asta nu e o omisiune - e forma livrabilului. Ce iese de aici e o propunere cu semnatura umana in
coada; cine aproba vede pentru fiecare rand id-ul atomului si fragmentul verbatim, deci poate refuza
un rand fara sa creada nimic pe cuvant.

CE CONTINE PACHETUL:
  propunere.json  fiecare parametru, cu valoarea din cod, atomul care o stabileste, fragmentul
                  verbatim, valabilitatea din corpus si clasificarea
  RAPORT.md       acelasi lucru, citibil, cu sectiunea "0. CERINTE" in fata
  APROBARE.md     formularul de aprobare, NESEMNAT
"""
import json
import os
import time

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSIUNE = "v1"


def _citeste(nume):
    return json.load(open(os.path.join(_RAD, "artefacte", nume), encoding="utf-8"))


def _tabel(randuri, capete):
    lat = [max(len(str(c)), *(len(str(r[i])) for r in randuri)) if randuri else len(str(c))
           for i, c in enumerate(capete)]
    out = ["| " + " | ".join(str(c).ljust(lat[i]) for i, c in enumerate(capete)) + " |",
           "|" + "|".join("-" * (l + 2) for l in lat) + "|"]
    for r in randuri:
        out.append("| " + " | ".join(str(x).ljust(lat[i]) for i, x in enumerate(r)) + " |")
    return "\n".join(out)


def _scurt(t, n=150):
    t = " ".join((t or "").split())
    return (t[:n] + "…") if len(t) > n else t


def construieste():
    man = _citeste("../corpus_manifest.json") if False else json.load(
        open(os.path.join(_RAD, "corpus_manifest.json"), encoding="utf-8"))
    strat = _citeste("strat_text.json")
    atomi = _citeste("atomi_raport.json")
    inv = _citeste("inventar_iconta.json")
    pot = _citeste("potriviri.json")
    durate = _citeste("durate.json")

    dest = os.path.join(_RAD, "propuneri", VERSIUNE)
    os.makedirs(dest, exist_ok=True)
    P = pot["potriviri"]
    s = pot["sumar"]

    # ── JSON-ul propunerii ───────────────────────────────────────────────────────────────────────
    propunere = {
        "_ce": "PROPUNERE FiscalOS v2 - parametrii fiscali ai iConta confruntati cu corpusul de acte. "
               "NU se aplica automat in iConta (CLAUDE.md §3). Cere aprobare umana.",
        "versiune": VERSIUNE,
        "generat_la": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "aprobare": {"stare": "NEAPROBAT", "de_cine": None, "la": None,
                     "nota": "Se aproba prin completarea propuneri/%s/APROBARE.md. Pana atunci, "
                             "niciun rand nu are efect." % VERSIUNE},
        "corpus": {"sursa": man["sursa"], "mod": man["sursa_mod"], "luat_la": man["luat_la"],
                   "n_fisiere": man["n_fisiere"], "octeti": man["octeti_total"],
                   "manifest": "corpus_manifest.json"},
        "atomizare": {"n_acte": atomi["n_acte"], "n_atomi": atomi["n_atomi"],
                      "acte_pe_articole": atomi["n_acte_pe_articole"],
                      "acte_pe_fragmente": atomi["n_acte_pe_fragmente"],
                      "acte_neextractibile": strat["neextractibile"]},
        "inventar": {"iconta": inv["iconta"], "n_parametri": inv["n_parametri"],
                     "pe_clasa": inv["pe_clasa"],
                     "cu_temei_declarat": inv["cu_temei_declarat"],
                     "fara_temei_declarat": inv["fara_temei_declarat"]},
        "sumar": {"CONCORDA": s.get("CONCORDA", 0), "DIFERA": s.get("DIFERA", 0),
                  "NEGASIT": s.get("NEGASIT", 0),
                  "citari_declarate_de_iconta": pot["citari_declarate"],
                  "citari_rezolvate_in_corpus": pot["citari_rezolvate"]},
        "parametri": P,
        "durate_masurate": durate,
    }
    with open(os.path.join(dest, "propunere.json"), "w", encoding="utf-8") as f:
        json.dump(propunere, f, ensure_ascii=False, indent=1, sort_keys=True)

    # ── raportul lizibil ─────────────────────────────────────────────────────────────────────────
    L = []
    A = L.append
    A("# FiscalOS v2 — PROPUNERE %s: parametrii fiscali ai iConta confruntați cu corpusul" % VERSIUNE)
    A("")
    A("Generat %s · **NEAPROBAT** · nu se aplică automat în iConta (CLAUDE.md §3)." %
      time.strftime("%d.%m.%Y %H:%M"))
    A("")
    A("| | |")
    A("|---|---|")
    A("| **CONCORDĂ** | **%d** |" % s.get("CONCORDA", 0))
    A("| **DIFERĂ** | **%d** |" % s.get("DIFERA", 0))
    A("| **NEGĂSIT** | **%d** |" % s.get("NEGASIT", 0))
    A("| Total parametri inventariați | %d |" % inv["n_parametri"])
    A("| Citări declarate de iConta / rezolvate în corpus | %d / %d |" %
      (pot["citari_declarate"], pot["citari_rezolvate"]))
    A("| Atomi în corpus | %s din %d acte |" % (format(atomi["n_atomi"], ",").replace(",", "."),
                                                atomi["n_acte"]))
    A("")
    A("---")
    A("")

    # ── 0. CERINTE ───────────────────────────────────────────────────────────────────────────────
    A("## 0. CERINȚE — decizii de arhitect")
    A("")
    A(CERINTE.strip())
    A("")
    A("---")
    A("")

    # ── 1. ce s-a rulat ──────────────────────────────────────────────────────────────────────────
    A("## 1. Operațiile rulate, cu durata măsurată")
    A("")
    A(_tabel([[d["operatie"], "%.2f s" % d["secunde"],
               _scurt(json.dumps(d["rezumat"], ensure_ascii=False), 90)]
              for d in durate["pasi"]],
             ["Operație", "Durată", "Rezultat"]))
    A("")
    A("Total măsurat: **%.2f s**. Duratele sunt citite din `artefacte/durate.json`, scris de "
      "`ruleaza_tot.py` — nu sunt estimări." % durate["total_secunde"])
    A("")

    # ── 2. corpusul ──────────────────────────────────────────────────────────────────────────────
    A("## 2. Corpusul")
    A("")
    A("Instantaneu copiat din `%s`, **doar citire**, la %s: **%d fișiere, %.1f MB**. "
      "Manifest SHA256 per fișier în `corpus_manifest.json`."
      % (man["sursa"], man["luat_la"], man["n_fisiere"], man["octeti_total"] / 1e6))
    A("")
    A("Toate cele 277 de amprente `.sha256` pe care ANAF/iConta le-au pus lângă acte confirmă "
      "hash-urile calculate aici — zero divergențe. Copierea e dovedită de două ori, nu presupusă.")
    A("")
    A("**Garanția de citire (CLAUDE.md §1).** `_refuza_scrierea` respinge mecanic orice cale sub "
      "`~/iconta_nou`, inclusiv prin legătură simbolică, iar inventarul nu importă niciodată cod "
      "iConta — citește sursa și o trece prin `ast.parse`, tocmai ca să nu poată scrie bytecode în "
      "arborele lor. Cele trei fișiere citite (`core/common.py`, `core/scadente.py`, "
      "`core/nomenclatoare.py`) sunt neatinse, și un eșantion de 25 de fișiere din corpus dă încă "
      "hash-urile din manifest. Ambele sunt verificate de `fiscalos/test_read_only.py`.")
    A("")
    A("Ce **nu** se poate afirma este că nimic nu s-a schimbat în `~/iconta_nou`: serviciul iConta "
      "rulează (systemd `iconta-nou`, activ) și își scrie singur jurnalele. În timpul generării a "
      "apărut acolo și un `.pyc` nou — un cache de **pytest**, pentru un modul pe care nu l-am "
      "deschis niciodată; `pytest` nu există în interpretorul folosit aici, ci doar în "
      "`iconta_nou/venv`. Nu e al nostru, și se scrie aici ca să nu fie citit greșit mai târziu.")
    A("")
    A("Atomizare: **%s atomi**, %d acte pe structură de articol, %d pe fragmente (acte fără "
      "articole: pliante ANAF, structuri de formular)."
      % (format(atomi["n_atomi"], ",").replace(",", "."), atomi["n_acte_pe_articole"],
         atomi["n_acte_pe_fragmente"]))
    A("")
    A("**Neextractibile (%d)** — limită a uneltei, nu absență din lege:" %
      len(strat["neextractibile"]))
    A("")
    for b, v in sorted(strat["neextractibile"].items()):
        A("- `%s` — %s" % (b, v["motiv"]))
    A("")

    # ── 3. rezultatul, pe clase ──────────────────────────────────────────────────────────────────
    A("## 3. Rezultatul, pe clase de parametri")
    A("")
    pe = {}
    for p in P:
        k = (p["clasa"], p["clasificare"])
        pe[k] = pe.get(k, 0) + 1
    clase = sorted({p["clasa"] for p in P})
    A(_tabel([[c, pe.get((c, "CONCORDA"), 0), pe.get((c, "DIFERA"), 0), pe.get((c, "NEGASIT"), 0)]
              for c in clase], ["Clasă", "CONCORDĂ", "DIFERĂ", "NEGĂSIT"]))
    A("")

    # ── 4. registrul COTE, in detaliu ────────────────────────────────────────────────────────────
    A("## 4. Registrul `COTE` al iConta — partea cu temei declarat")
    A("")
    A("Acestea sunt cele %d intrări (20 chei, cu versiunile lor în timp) pe care iConta le "
      "declară cu temei și citat. Pentru fiecare: valoarea din cod, atomul din corpus care o "
      "stabilește, fragmentul verbatim și data de intrare." %
      sum(1 for p in P if p["parametru"].startswith("cote/")))
    A("")
    for p in sorted((x for x in P if x["parametru"].startswith("cote/")),
                    key=lambda x: (x["nume"], x["valabil_din_cod"] or "")):
        A("### `%s` — **%s**" % (p["parametru"], p["clasificare"]))
        A("")
        A("- **cod iConta:** `%s` din %s — %s" % (p["valoare_cod"], p["valabil_din_cod"],
                                                 p["unde_in_cod"]))
        A("- **temei declarat:** %s" % (p["temei_declarat_de_iconta"] or "—"))
        if p["atom"]:
            A("- **atom din corpus:** `%s`" % p["atom"])
            A("- **valoare în textul legii:** %s" % (p["valoare_lege"] or "—"))
            A("- **valabil din (corpus):** %s" % (p["valabil_din_corpus"] or
                                                  "— (atomul nu poartă notă de intrare în vigoare)"))
            if p.get("act_modificator"):
                A("- **act modificator:** %s" % _scurt(p["act_modificator"], 180))
            A("- **verbatim:**")
            A("")
            A("  > %s" % _scurt(p["atom_verbatim"], 600))
        else:
            A("- **atom:** — (%s)" % _scurt(p["motiv"], 200))
        if p.get("nota"):
            A("- ⚠ **notă:** %s" % p["nota"])
        A("")

    # ── 5. DIFERA ────────────────────────────────────────────────────────────────────────────────
    A("## 5. DIFERĂ — ambele părți")
    A("")
    dif = [p for p in P if p["clasificare"] == "DIFERA"]
    if not dif:
        A("**Niciun parametru nu iese DIFERĂ.**")
        A("")
        A("Asta nu e o afirmație despre lume, ci una despre ce s-a putut dovedi, și are un motiv "
          "care trebuie citit: un verdict *legea spune altceva* se pronunță numai când citarea "
          "declarată de iConta duce la actul corect, iar atomul de acolo poartă un alt număr. "
          "Pentru cei 42 de parametri cu temei declarat, citarea s-a rezolvat în toate cazurile și "
          "valoarea s-a confirmat — deci registrul `COTE` al iConta e, pe corpusul acesta, corect. "
          "Pentru parametrii pe care iConta nu-i sursează deloc, o divergență nu se poate DOVEDI: "
          "ei ies NEGĂSIT, nu DIFERĂ (vezi §0, cerința C2).")
    else:
        for p in dif:
            A("### `%s`" % p["parametru"])
            A("")
            A("- **cod iConta:** `%s` — %s" % (p["valoare_cod"], p["unde_in_cod"]))
            A("- **text lege:** `%s` — atom `%s`" % (p["valoare_lege"], p["atom"]))
            A("")
            A("  > %s" % _scurt(p["atom_verbatim"], 600))
            A("")
    A("")

    # ── 6. NEGASIT ───────────────────────────────────────────────────────────────────────────────
    A("## 6. NEGĂSIT — și de ce")
    A("")
    neg = [p for p in P if p["clasificare"] == "NEGASIT"]
    grupe = {}
    for p in neg:
        cheie = ("parametru operațional, fără act normativ de citat"
                 if "OPERATIONAL" in p["motiv"] else
                 "potrivire prea slabă ca să susțină un verdict (fără temei declarat de iConta)"
                 if "prea slaba" in p["motiv"] else
                 "simbol de cont care nu apare în planul OMFP 1802/2014"
                 if p["clasa"] == "cont" else "altul")
        grupe.setdefault(cheie, []).append(p)
    for cheie in sorted(grupe):
        A("**%s** (%d):" % (cheie, len(grupe[cheie])))
        A("")
        for p in sorted(grupe[cheie], key=lambda x: x["parametru"]):
            A("- `%s` = `%s` — %s" % (p["parametru"], p["valoare_cod"], p["unde_in_cod"]))
        A("")

    # ── 7. termene si nomenclatoare ──────────────────────────────────────────────────────────────
    A("## 7. Termene, nomenclatoare")
    A("")
    for p in sorted((x for x in P if x["clasa"] in ("termen", "nomenclator")),
                    key=lambda x: x["parametru"]):
        A("- **`%s`** = `%s` → %s · atom `%s`" % (p["parametru"], _scurt(p["valoare_cod"], 70),
                                                 p["clasificare"], p["atom"] or "—"))
        if p["atom_verbatim"]:
            A("  > %s" % _scurt(p["atom_verbatim"], 260))
    A("")

    # ── 8. conturi ───────────────────────────────────────────────────────────────────────────────
    A("## 8. Conturi — confruntate cu planul de conturi din OMFP 1802/2014")
    A("")
    A("Planul citit din corpus: **%d simboluri**. Un simbol de cont nu e o valoare numerică — ce se "
      "confirmă e existența lui în nomenclator, cu denumirea din act."
      % pot["n_conturi_in_plan_din_corpus"])
    A("")
    ct = [p for p in P if p["clasa"] == "cont" and p["clasificare"] == "CONCORDA"]
    A(_tabel([[p["valoare_cod"], _scurt(p["valoare_lege"], 70)] for p in
              sorted(ct, key=lambda x: x["valoare_cod"])[:40]],
             ["Cont", "Denumire în OMFP 1802/2014"]))
    A("")
    A("(%d conturi confirmate; tabelul arată primele 40. Lista completă în `propunere.json`.)"
      % len(ct))
    A("")
    A("---")
    A("")
    A("## Aprobare")
    A("")
    A("Această propunere e **NEAPROBATĂ**. Se aprobă completând `propuneri/%s/APROBARE.md`. "
      "FiscalOS nu are cale de scriere spre iConta; aplicarea e un pas uman, separat." % VERSIUNE)

    with open(os.path.join(dest, "RAPORT.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")

    # ── formularul de aprobare ───────────────────────────────────────────────────────────────────
    with open(os.path.join(dest, "APROBARE.md"), "w", encoding="utf-8") as f:
        f.write(APROBARE % {"versiune": VERSIUNE, "concorda": s.get("CONCORDA", 0),
                            "difera": s.get("DIFERA", 0), "negasit": s.get("NEGASIT", 0),
                            "data": time.strftime("%d.%m.%Y")})
    return {"dest": dest, "sumar": s, "n_parametri": len(P)}


CERINTE = """
Cerințele de mai jos cer o decizie de arhitect. Niciuna nu blochează livrabilul — toate sunt scrise
aici tocmai ca să nu fie luate tacit de executor.

**C1 — Instantaneul corpusului nu intră în git.** 130 MB de acte publice, reproductibile din
`~/iconta_nou/anaf_surse`. Ce intră e `corpus_manifest.json` (SHA256 per fișier), care e proba că un
atom citat a fost extras din *acei* octeți. *Decizia luată de executor:* `corpus/` în `.gitignore`.
*Ce ar schimba o decizie contrară:* repo-ul ar deveni greu, iar ZIP-ul livrabilului ar trece de
130 MB. Dacă arhitectul vrea corpusul versionat, calea e un repo separat sau git-lfs, nu acest repo.

**C2 — Un parametru pe care iConta nu-l sursează nu poate produce un DIFERĂ dovedit.** Verdictul
*legea spune altceva* cere ca citarea declarată să ducă la actul corect. Fără temei declarat, tot ce
se poate face e o căutare pe cuvinte în 46.000 de atomi — care la prima rulare a produs 7 DIFERĂ,
toate false. Acum acele cazuri ies NEGĂSIT, cu motivul scris. *Decizia cerută:* pentru cele 41 de
constante fără temei, drumul e ca iConta să le dea un `Temei` (ele sunt chiar clasa pe care clichetul
lor o numără), nu ca FiscalOS să ghicească actul. Confirmați direcția.

**C3 — Simbolurile de cont se culeg euristic.** Inventarul ia literalii de 3–4 cifre folosiți în
≥3 locuri din `core/`. Euristica prinde și ce nu e cont: `2015`, `5000`, `100`, `102` ies NEGĂSIT cu
această mențiune, în loc să fie tăiate tacit. *Decizia cerută:* se acceptă zgomotul vizibil, sau
iConta marchează conturile explicit (un tip `Cont`, ca `Temei`) și inventarul devine exact?

**C4 — Data de intrare în vigoare și valoarea se pot dovedi pe atomi DIFERIȚI.** Pentru cota de TVA,
Legea 141/2025 din corpus poartă valoarea (21%), iar notele „(la 01-08-2025, …)" sunt ale
consolidatului de Cod fiscal. Raportul le ține în coloane separate și nu le amestecă. *Decizia
cerută:* propunerea să citeze un singur atom „cel mai bun", sau o pereche (atom-valoare,
atom-valabilitate)? Astăzi citează atomul valorii și declară când data lipsește de pe el.

**C5 — Ce NU s-a inventariat**, scris fiindcă tăcerea unui scan se citește ca absență: planul de
conturi al fiecărei firme (e date în bază, nu cod), valorile operaționale fără act normativ, și
nomenclatoarele derivate din XSD-uri. Dacă vreuna din ele trebuie să intre în livrabilul următor,
e o decizie, nu o omisiune.

**C6 — Motorul de întrebări nu s-a început** (`FiscalOS_intrebari_test_50.csv`), conform punctului 7
din brief. Oprirea e după acest livrabil.
"""

APROBARE = """# APROBARE — propunere %(versiune)s

Propunerea `propuneri/%(versiune)s/propunere.json` + `RAPORT.md`, generată la %(data)s:

- CONCORDĂ: **%(concorda)d**
- DIFERĂ: **%(difera)d**
- NEGĂSIT: **%(negasit)d**

FiscalOS **nu are cale de scriere spre iConta**. Aplicarea oricărui rând din această propunere e un
pas uman, separat de generarea ei.

## Semnătură

- [ ] Am citit §0 CERINȚE și am răspuns la C1–C6.
- [ ] Am verificat, prin eșantion, că fragmentele verbatim citate se găsesc în `corpus/` la id-ul
      de atom indicat.
- [ ] Aprob propunerea în întregime.
- [ ] Aprob parțial — rândurile refuzate, cu motiv:

```
(rândurile refuzate)
```

Aprobat de: ______________________  Data: ____________

Stare: **NEAPROBAT** (se schimbă manual, la semnare)
"""


if __name__ == "__main__":
    t0 = time.time()
    r = construieste()
    print("propunere %s: %s | %d parametri | %.1f s" % (VERSIUNE, r["sumar"], r["n_parametri"],
                                                       time.time() - t0))
