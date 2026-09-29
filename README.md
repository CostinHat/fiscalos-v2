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

## Pasul 6 — deciziile C23–C29 (`intrebari/v5/`, `propuneri/v6/`)

Structura răspunsului final validată (C23), „răspuns gol" verificat întotdeauna (C24), operanzi
FAPT_CAZ / VALOARE_LEGALĂ (C25), anexele ca structură proprie în atomizare (C26), data de referință
pentru faptul întrebat (C27), comparatorul reparat și calculul afișat pas cu pas (C28), 20 de pași (C29).

| Motor (scor INDICATIV) | CORECT | GREȘIT | NU POT | Greșeli de fond | Cost |
|---|---|---|---|---|---|
| Navigare v5 | 34 | 3 | 13 | 1 | $9,88 |
| Navigare v4 (C28 + C24) | 20 | 12 | 18 | — | $7,86 |

Deciziile deschise (C30–C33) sunt în `intrebari/v5/RAPORT.md`, secțiunea 0.

```sh
venv/bin/python -m fiscalos.navigare          # reluabil: fiecare raspuns se salveaza imediat
python3 -m fiscalos.raport_intrebari_v5
python3 -m fiscalos.masoara_C33               # efectul C33, fara apel
```

## Pasul 7 — deciziile C30–C33 (`intrebari/v6/`, `propuneri/v7/`)

Fără rulare plătită (decizia 5). Comparatorul reparat (C30) și decodarea `\uXXXX` (C33), măsurate pe
ieșirile salvate: navigare v5 34/3/13 → **37/2/11**. Codul muncii și alte 46 de acte găsite stricate de
detectorul de structură (`detector_structura.py`) aduse din sursa oficială (C31), cu trei defecte de
conversie a portalului reparate; propunerea v7 (aceleași clasificări, atomi la locul lor). `termen_efectiv`
în calcul, din atomii citați (C32), cu Codul de procedură civilă adus pentru regula prelungirii.
Efectul lui C31 și C32 se măsoară pe setul nou. De decis: C34–C37.

```sh
python3 -m fiscalos.detector_structura        # clasa "articole atomizate sub alt articol", pe tot corpusul
venv/bin/python -m fiscalos.surse_oficiale_c31   # rezolvarea in portal + aducere incrementala (retea)
python3 -m fiscalos.raport_v6
```

## Pasul 8 — deciziile C34–C37 (`intrebari/v7/`, `propuneri/v8/`)

Fără apel la model. Art. 139 din Codul muncii, verificat în textul oficial: două sărbători chiar nu au
dată, deci `termen_efectiv` se abține (C34); „...” din liste era forma restrânsă ascunsă a portalului,
scoasă ca clasă. Conversia oficială reparată pe șase clase (textul citat după `S_CIT`, cu adâncimea
citării; exponenți și litere în numere; text reprodus din alt act → notă), iar detectorul iese curat pe
stratul oficial (C36). Ordinul 1099/2016 identificat după antetul lui (C37). De decis: C38, C39.

## Măsurătoarea finală — setul 2 (`intrebari/final/`)

Versiunea 485ffc3, neschimbată; răspunsurile comise (8b3269f) înainte de citirea cheii; comparator
neschimbat; nicio reparație după comparație. Scor pe fond: **28/7/15**; **2 greșeli de fond** (Q2-TVA-05
temei alăturat; Q2-CTB-05 termen efectiv necalculat). Cost $8,76. Defectele, ca cerințe: C40–C46.

## Pasul 9 — deciziile C40–C46 (`intrebari/v8/`)

Fără rulare plătită. Termenele prin `termen_efectiv` (C40); temeiul alăturat justificat, cu geamenii
arătați de `deschide` (C41); comparatorul pentru zero și an relativ (C42: setul 2 re-notat 30/5/15, scorul
oficial rămâne 28/7/15); consecința cuantificată în prompt (C43); răspunsul final pe ieșire structurată, într-o
tură fără unelte (C44); numeralele în litere (C45). Pe propunerile salvate ale setului 2, verificarea nouă
prinde ambele greșeli de fond. De decis: C47, C48.

## Măsurătoarea pe setul 3 (`intrebari/set3/`)

Versiunea b6a2d04 (C40–C48), neschimbată; răspunsurile comise (024fab8) înainte de citirea cheii. Scor pe
fond: **18/1/31**; **1 greșeală de fond** (Q3-TVA-09: procentul împărțit de două ori). C47: 12 abțineri din
C40/C41 — 9 ar fi fost corecte, 1 a prevenit o greșeală (Q3-SAL-07). Cost $0,310/întrebare (setul 2:
$0,175). De decis: C49–C53.

## Pasul 10 — deciziile C49–C53 (`intrebari/v9/`)

Fără rulare plătită. C49 justificarea geamănului numai pentru atomul decisiv (faptul principal, ancora
valorii); C50 procentul împărțit la 100 respins; C51 ordinale și cifră + unitate; C52 o tură de reparație
pentru cifrele respinse. Pe propunerile salvate ale setului 3: re-notare 24/1/25 (oficial 18/1/31); 5 din
cele 9 răspunsuri corecte pierdute trec, Q3-TVA-09 e prins de C50. Corecție: la Q3-SAL-07, C41 nu prinsese
greșeala. De decis: C54, C55, instantaneul iConta (modificat după inventar).

## Pasul 11 — C41 ca avertisment, C54, C55, iConta din starea comisă (`intrebari/v10/`)

FiscalOS citește iConta numai din git HEAD (`iconta_head.py`); instantaneul și inventarul refăcute de pe HEAD
(propunerea v9: aceleași clasificări). Geamănul nejustificat e avertisment, nu respingere; `deschide` arată
geamenii ca id + temei; operanzii legali poartă valabilitatea, iar una care nu acoperă data aplicării e
respinsă. Re-notarea setului 3 pe propunerile salvate: 28/3/19 (oficial 18/1/31). De decis: C56.

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
