# FiscalOS v2

Atomizează corpusul de acte fiscale românești și confruntă cu el parametrii fiscali folosiți de
iConta. Rezultatul e o **propunere** cu aprobare umană — niciodată o aplicare automată.

Regulile proiectului sunt în [`CLAUDE.md`](CLAUDE.md). Ele nu sunt decor: fiecare e verificată de
o probă care rulează pe corpus.

## Primul livrabil

[`propuneri/v1/RAPORT.md`](propuneri/v1/RAPORT.md) — raportul lizibil, cu secțiunea *0. CERINȚE*
în față. Partea mecanică e în `propuneri/v1/propunere.json`.

| | |
|---|---|
| CONCORDĂ | **202** |
| DIFERĂ | **0** |
| NEGĂSIT | **29** |
| Parametri inventariați | 231 |
| Citări declarate de iConta / rezolvate în corpus | 40 / 40 |
| Atomi în corpus | 46.559 din 269 acte |
| Probe pe corpus | 29, toate trec |

**Zero DIFERĂ** nu e o afirmație despre lume, ci despre ce s-a putut dovedi. Verdictul *legea spune
altceva* se pronunță numai când citarea declarată de iConta duce la actul corect și atomul de acolo
poartă un alt număr. Pentru cei 40 parametri cu temei declarat, citarea s-a rezolvat în toate
cazurile și valoarea s-a confirmat. Parametrii pe care iConta nu-i sursează deloc nu pot produce o
divergență *dovedită*: ei ies NEGĂSIT, cu motivul scris. Detaliile, în §5 și §6 ale raportului.

## Cum se rulează

```sh
python3 ruleaza_tot.py    # lanțul întreg (OP2→OP7) + probele, cu durata măsurată a fiecărui pas
python3 probe.py          # numai probele
python3 -m fiscalos.propunere   # regenerează pachetul de propunere
```

Fără dependențe în afara bibliotecii standard, plus `pdftotext` (poppler-utils) pentru actele PDF.
`ruleaza_tot.py` durează ~19 s pe corpusul întreg.

## Cum e construit

| Pas | Ce face |
|---|---|
| `fiscalos/corpus_snapshot.py` | instantaneu al corpusului + manifest SHA256; gardul care refuză orice scriere în iConta |
| `fiscalos/strat_text.py` | redare în text simplu: `.txt` ca atare, `.html` → text, `.pdf` → `pdftotext`; ce nu e extractibil primește un **motiv** |
| `fiscalos/atomizare.py` | act → articol → alineat → literă/punct, id stabil, text verbatim, valabilitate din notele `(la DD-MM-YYYY, …)` |
| `fiscalos/inventar_iconta.py` | inventarul parametrilor iConta, prin AST — niciun import, ca să nu se scrie bytecode în arborele lor |
| `fiscalos/potrivire.py` | potrivirea pe niveluri de probă și clasificarea CONCORDĂ / DIFERĂ / NEGĂSIT |
| `fiscalos/propunere.py` | pachetul versionat: JSON + raport + formular de aprobare |

Corpusul (`corpus/`, 130 MB de acte publice) **nu e versionat aici**: e reproductibil din sursă,
iar proba durabilă e `corpus_manifest.json`. Vezi cerința C1 din raport.

## Ce nu face

Nu scrie nimic în iConta și nu are cale spre el. Aplicarea oricărui rând din propunere e un pas
uman, separat de generarea ei.
