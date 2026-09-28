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
| CONCORDĂ | **200** — din care 177 cu temei declarat de iConta și verificat, 23 pe ancoră slabă |
| DIFERĂ | **0** |
| NEGĂSIT | **31** |
| Parametri inventariați | 231 |
| Citări declarate de iConta / rezolvate în corpus | 40 / 40 |
| Atomi în corpus | 46.559 din 269 acte |
| Probe pe corpus | 38, toate trec |
| Dovada inversă (greșeli injectate → DIFERĂ) | 5 / 5 |

### De ce 0 DIFERĂ nu e o afirmație goală

Un detector care nu poate contrazice niciodată dă exact același zero. Așa că `banc_mutatii.py`
injectează, pe o copie în memorie a inventarului, greșeli luate din istoria fiscală reală — dividende
10% în loc de 16%, TVA 19% în loc de 21%, salariu minim 4.050 aplicat unei date din semestrul 2 al
2026, o cotă care nu există în niciun act, și o citare care trimite la actul greșit — și cere ca
fiecare să iasă DIFERĂ, cu temeiul corect alături.

**Prima rulare a picat 5 din 5.** Toate cele cinci greșeli ieșeau CONCORDĂ, fiindcă valoarea era
căutată până la ultimul atom din corpus, iar legislația fiscală conține aproape orice procent pe
undeva. Regula de acum: *când iConta declară un temei, verdictul se ia din actul acela.* Detaliile și
celelalte patru defecte găsite astfel sunt în §9 și în cerința C7 din raport.

## Al doilea livrabil — motorul de întrebări

[`intrebari/v1/RAPORT.md`](intrebari/v1/RAPORT.md) — 50 de întrebări de test, fiecare cu răspuns din
atomi (temei + fragment verbatim + valabilitate la data întrebării) sau „nu pot răspunde" cu motivul.
Niciodată un răspuns fără atom. Răspunsurile per întrebare sunt în `intrebari/v1/raspunsuri/`.

| | |
|---|---|
| CORECT | **8** — din care **4 pe fond**, 4 abțineri pe întrebări INCOMPLETA (vezi C1 în raport) |
| GREȘIT | **17** |
| NU POT RĂSPUNDE | **25** |

Motorul a fost **orb la cheie, mecanic**, iar răspunsurile v0 au fost comise (`f1997a8`) înainte ca
modulul de comparație să existe. Linia de bază v0 cinstită a fost 3/33/14; fiecare reparație ulterioară
e o clasă de defect măsurată pe toate cele 50 — istoricul complet, inclusiv o regresie și o ipoteză
infirmată, e în §3 al raportului.

```sh
python3 -m fiscalos.intrebari          # raspunde la cele 50 (orb la cheie)
python3 -m fiscalos.comparatie         # compara cu cheia - singurul modul care o citeste
python3 -m fiscalos.raport_intrebari   # lantul final cronometrat + raportul
```

## Al treilea livrabil — motorul de întrebări v2, stratul semantic ancorat pe atomi

[`intrebari/v2/RAPORT.md`](intrebari/v2/RAPORT.md). Un model (`claude-opus-5`) propune răspunsul
numai din atomii găsiți de căutarea mecanică; un verificator **fără model** respinge orice citat care
nu e literal în atom și orice cifră care nu e literală într-un citat sau în întrebare. Ce nu trece
devine abținere. Scor **indicativ** (setul de 50 e expus), pe fond:

| Motor | CORECT | GREȘIT | NU POT | Cost / rulare |
|---|---|---|---|---|
| Stratul semantic | **12** | 7 | 31 | $2,51 |
| Motorul lexical | 4 | 17 | 29 | $0 |

Cheia API se citește numai din `~/.fiscalos/api_keys.env` (mod 600), niciodată din iConta.

```sh
venv/bin/python -m fiscalos.semantic --simulare   # marimea contextului, fara niciun apel
venv/bin/python -m fiscalos.semantic              # cele 50 de apeluri, cost masurat
python3 -m fiscalos.raport_intrebari_v2           # comparatia pe fond + raportul
```

## Pasul 4 — consolidatele oficiale (C12) și relația de derogare (C17)

- [`intrebari/v3/RAPORT.md`](intrebari/v3/RAPORT.md) — ambele motoare, rerulate (scor indicativ).
- [`propuneri/v4/RAPORT.md`](propuneri/v4/RAPORT.md) + `acte_aduse.json` — propunerea cu actele aduse.
- `surse_oficiale/` — 6 acte consolidate la zi, aduse de FiscalOS din legislatie.just.ro, cu
  `MANIFEST.json` (URL, data formei consolidate, SHA256). Instantaneul iConta rămâne neatins.
- `fiscalos/relatii.py` — relația „derogă de la / prin excepție de la / modifică", extrasă din text.

| Motor | CORECT | GREȘIT | NU POT | Cost |
|---|---|---|---|---|
| Stratul semantic v3 | 10 | 8 | 32 | $3,25 |
| Motorul lexical v3 | 2 | 12 | 36 | $0 |

```sh
venv/bin/python -m fiscalos.surse_oficiale --aduce   # aduce din nou actele (retea)
python3 -m fiscalos.ablatie_lexical                  # L0 / L1 / L2, ablatie exacta
python3 -m fiscalos.raport_intrebari_v3
```

## Pasul 5 — navigare structurală și calcul evaluat de cod (`intrebari/v4/`)

Stratul semantic nu mai primește un context gata ales de căutare: navighează singur prin structura
actelor (`cuprins` → `deschide` → copii → relații de derogare/modificare), cu cel mult 12 pași;
căutarea lexicală e doar punct de intrare. Verificarea mecanică a citatelor și cifrelor e cea din v3.
Modelul nu calculează: propune o formulă cu operanzi, fiecare cu sursa literală (atom sau întrebare),
iar codul o evaluează (`navigare.evalueaza_calcule`).

| Motor (scor INDICATIV, setul e expus) | CORECT | GREȘIT | NU POT | Cost |
|---|---|---|---|---|
| Navigare v4 | 18 | 17 | 15 | $7,86 |
| Semantic v3 | 10 | 8 | 32 | $3,25 |
| Lexical (referință) | 2 | 13 | 35 | $0 |

Defectele găsite după comparație (C23–C29) sunt în `intrebari/v4/RAPORT.md`, secțiunea 0, nereparate.

```sh
venv/bin/python -m fiscalos.navigare [Q-ID ...]   # stratul de navigare (apeluri API, cost)
python3 -m fiscalos.raport_intrebari_v4
```

## Cum se rulează

```sh
python3 ruleaza_tot.py        # lanțul întreg + bancul de mutații + probele, cu durata fiecărui pas
python3 probe.py              # numai probele
python3 -m fiscalos.banc_mutatii   # numai dovada inversă
python3 -m fiscalos.propunere      # regenerează pachetul de propunere
```

Fără dependențe în afara bibliotecii standard, plus `pdftotext` (poppler-utils) pentru actele PDF.
`ruleaza_tot.py` durează ~24 s pe corpusul întreg.

## Cum e construit

| Pas | Ce face |
|---|---|
| `fiscalos/corpus_snapshot.py` | instantaneu al corpusului + manifest SHA256; gardul care refuză orice scriere în iConta |
| `fiscalos/strat_text.py` | redare în text simplu: `.txt` ca atare, `.html` → text, `.pdf` → `pdftotext`; ce nu e extractibil primește un **motiv** |
| `fiscalos/atomizare.py` | act → articol → alineat → literă/punct, id stabil, text verbatim, valabilitate din notele `(la DD-MM-YYYY, …)` |
| `fiscalos/inventar_iconta.py` | inventarul parametrilor iConta, prin AST — niciun import, ca să nu se scrie bytecode în arborele lor |
| `fiscalos/potrivire.py` | potrivirea pe niveluri de probă și clasificarea CONCORDĂ / DIFERĂ / NEGĂSIT |
| `fiscalos/banc_mutatii.py` | dovada în cealaltă direcție: greșeli cunoscute injectate, care **trebuie** să iasă DIFERĂ |
| `fiscalos/propunere.py` | pachetul versionat: JSON + raport + formular de aprobare |

Corpusul (`corpus/`, 130 MB de acte publice) **nu e versionat aici**: e reproductibil din sursă,
iar proba durabilă e `corpus_manifest.json`. Vezi cerința C1 din raport.

## Ce nu face

Nu scrie nimic în iConta și nu are cale spre el. Aplicarea oricărui rând din propunere e un pas
uman, separat de generarea ei.
