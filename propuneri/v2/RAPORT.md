# FiscalOS v2 — PROPUNERE v2: parametrii fiscali ai iConta confruntați cu corpusul

Generat 28.09.2026 16:59 · **NEAPROBAT** · nu se aplică automat în iConta (CLAUDE.md §3). Versiunea anterioară, `propuneri/v1/`, rămâne neatinsă.

| | |
|---|---|
| **CONCORDĂ** — pe temei declarat și verificat | **94** |
| **DIFERĂ** | **1** |
| NEVERIFICAT — *gri: nu e verdict, e probă de aprobat* | 25 |
| **NEGĂSIT** | **27** |
| Parametri inventariați | 147 |
| Citări declarate de iConta / rezolvate în corpus | 40 / 40 |
| Temeiuri candidate propuse (din act normativ, de aprobat) | 21 |
| Dovada inversă — greșeli injectate care ies DIFERĂ/NEGĂSIT | 9 / 9 |

---

## 0. CERINȚE

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

### Cerințe noi, de decis

**C8 — Am aplicat C2 și temeiurilor DECLARATE, nu doar celor candidate.** C2 spune că un formular
sau un pliant nu poate fi temei. Aplicată consecvent, regula lovește și 4 intrări din
registrul `COTE`: cotele reduse de TVA din 2016 citează nota `cf_art291_2016_forma_initiala`, pe care
`PROVENIENTA.json` a iConta o clasifică ea însăși `SCRIS` (redactată de ei), iar tichetele de masă din
2025 citează pliantul `anaf_limite_2025`. O valoare „verificată" pe o notă scrisă de cel verificat e o
tautologie. Ele ies acum NEVERIFICAT, cu rezultatul inițial păstrat în `clasificare_initiala`.
*De decis:* extensia se ratifică, sau C2 se aplică numai temeiurilor candidate?

**C9 — Un nomenclator care e o submulțime strictă a normei iese DIFERĂ.** `d394.TIPURI`: OPANAF
2194/2025 enumeră `L/A/LS/AS/AÎ/V/C/N/Î1/Î2`, codul are aceleași opt fără `Î1/Î2`. iConta scrie în
`nomenclatoare.py` că `Î1/Î2` sunt secțiunile de încasări prin AMEF, neconstruite încă — deci nu e o
valoare greșită, ci o acoperire incompletă, declarată. Vechiul prag de 80% o ascundea.
*De decis:* rămâne DIFERĂ (cu ambele părți, cum e acum), sau o acoperire incompletă declarată de
iConta e o stare separată?

**C10 — Temeiurile candidate sunt găsite prin potrivire pe frază, nu verificate.** 21
candidați, toți din acte normative, fiecare cu fragmentul verbatim. Frazele-subiect le-am scris citind
ce face fiecare modul iConta (de ex. `casa.py` spune în antet că plafoanele sunt din Legea 70/2015).
Doi candidați pentru plafoanele de numerar trimit la actele care au *modificat* Legea 70/2015 (OUG
115/2023, Legea 296/2023), nu la Legea 70/2015 însăși. *De decis:* un candidat poate fi actul
modificator, sau trebuie să fie întotdeauna actul de bază, consolidat?

**C11 — Unitatea unei constante nesursate se citește din folosirea ei.** `d216.COTA_IMPOZIT = 0.3`
e folosită ca `baza * COTA_IMPOZIT / 100`, deci înseamnă 0,3%, nu 30% (cum stă în registrul `COTE`,
unde ratele sunt fracții). Fără această citire, potrivirea îi găsea un „temei" în normele despre
impozitul pe clădiri. Regula e: `NUME / 100` în modul ⇒ procent literal. *De decis:* se acceptă, sau
iConta își declară unitatea explicit (cerință R-UNIT)?

---

## 1. Operațiile rulate, cu durata măsurată

| Operație                               | Durată  | Rezultat                                                                          |
|----------------------------------------|---------|-----------------------------------------------------------------------------------|
| OP2 instantaneu corpus + manifest SHA  | 0.56 s  | {"n_fisiere": 726, "octeti_total": 130006698}                                     |
| OP3 strat de text (txt/html/pdf)       | 2.02 s  | {"n_acte_cu_text": 269, "n_neextractibile": 4}                                    |
| OP4 atomizare structurala              | 2.24 s  | {"n_acte": 269, "n_atomi": 46559, "n_acte_pe_articole": 201, "n_acte_pe_fragment… |
| OP5 inventar parametri iConta (citire) | 2.82 s  | {"n_parametri": 147, "pe_clasa": {"cota": 38, "plafon": 38, "termen": 5, "nomenc… |
| OP6+OP7 potrivire si clasificare       | 9.06 s  | {"n_parametri": 147, "sumar": {"CONCORDA": 94, "NEVERIFICAT": 25, "DIFERA": 1, "… |
| OP7b banc de mutatii (dovada inversa)  | 5.05 s  | {"n_trec": 9, "n_pica": 0}                                                        |
| Probe pe corpus                        | 12.86 s | {"cod_ieșire": 0}                                                                 |

Total măsurat: **34.61 s** (din `artefacte/durate.json`, scris de `ruleaza_tot.py`).

## 2. Corpusul

Instantaneu din `/home/costin/iconta_nou/anaf_surse`, doar citire, 726 fișiere, manifest SHA256 în `corpus_manifest.json` (C1: corpusul rămâne în `.gitignore`, manifestul e proba). 46.559 atomi în 269 acte; 212 acte normative, 57 surse care nu pot fi temei (formulare, structuri de declarație, pliante ANAF, note redactate de iConta).

## 3. Rezultatul, pe clase

| Clasă       | CONCORDĂ | DIFERĂ | NEVERIFICAT | NEGĂSIT |
|-------------|----------|--------|-------------|---------|
| cont        | 57       | 0      | 0           | 5       |
| cota        | 15       | 0      | 15          | 8       |
| nomenclator | 1        | 1      | 0           | 2       |
| plafon      | 16       | 0      | 10          | 12      |
| termen      | 5        | 0      | 0           | 0       |

## 4. Registrul `COTE` al iConta — valoare și valabilitate, în pereche

C4: fiecare verdict citează **atomul valorii** și **atomul valabilității**. Când al doilea lipsește, se spune. O dată de consolidare e data ultimei modificări a *textului*, nu neapărat a valorii — nepotrivirile de dată se arată (⚠), nu se clasifică.

### `cote/cam@2018-01-01` — **CONCORDĂ**

- **cod iConta:** `0.0225` din 2018-01-01 — core/common.py:667 (registrul COTE)
- **temei declarat:** CF
- **atom-valoare:** `cod_fiscal_227_2015_consolidat#art220^3/alin1` → `2,25%`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > Cota contribuției asiguratorii pentru muncă este de 2,25%. Notă ... Reproducem mai jos prevederile art. 19 din LEGEA nr. 369 din 19 decembrie 2022, publicată în MONITORUL OFICIAL nr. 1215 din 19 decembrie 2022: Articolul 19 În anul 2023, cota contribuției pentru persoanele prevăzute la art. 20 alin. (1) din Legea nr. 76/2002 privind sistemul asigurărilor pentru șomaj și stimularea ocupării forței de muncă, cu modific…

### `cote/cas@2018-01-01` — **CONCORDĂ**

- **cod iConta:** `0.25` din 2018-01-01 — core/common.py:658 (registrul COTE)
- **temei declarat:** CF
- **atom-valoare:** `cod_fiscal_227_2015_consolidat#art138` → `25%`
- **atom-valabilitate:** `cod_fiscal_227_2015_consolidat#art138` din **2018-01-01** (nota de consolidare)

  > Cotele de contribuții de asigurări sociale Cotele de contribuții de asigurări sociale sunt următoarele: a) 25% datorată de către persoanele fizice care au calitatea de angajați sau pentru care există obligația plății contribuției de asigurări sociale, potrivit prezentei legi; ... b) 4% datorată în cazul condițiilor deosebite de muncă, astfel cum sunt prevăzute în Legea nr. 263/2010 privind sistemul unitar de pensii p…

### `cote/cass@2018-01-01` — **CONCORDĂ**

- **cod iConta:** `0.10` din 2018-01-01 — core/common.py:661 (registrul COTE)
- **temei declarat:** CF
- **atom-valoare:** `cod_fiscal_227_2015_consolidat#art156~2` → `10%`
- **atom-valabilitate:** `cod_fiscal_227_2015_consolidat#art156~2` din **2021-12-18** (nota de consolidare) — ⚠ codul dateaza valoarea din 2018-01-01; corpusul arata 2021-12-18. O nota de consolidare e data ultimei modificari a TEXTULUI, nu neaparat a valorii - de citit, nu de clasificat.

  > Cota de contribuție de asigurări sociale de sănătate: Cota de contribuție de asigurări sociale de sănătate este de 10% și se datorează de către persoanele fizice care au calitatea de angajați sau pentru care există obligația plății contribuției de asigurări sociale de sănătate, potrivit prezentei legi. + Secţiunea a 3-a Baza de calcul al contribuției de asigurări sociale de sănătate datorate în cazul persoanelor care…

### `cote/facilitate_salariu_minim@2025-01-01` — **CONCORDĂ**

- **cod iConta:** `300` din 2025-01-01 — core/common.py:675 (registrul COTE)
- **temei declarat:** OUG 156 2024
- **atom-valoare:** `oug_156_2024#artLXVI/alin1` → `300`
- **atom-valabilitate:** `oug_156_2024#artLXVI/alin1` din **2025-01-01** (textul atomului (Incepand cu data de ...))

  > Prin derogare de la prevederile art. 78, art. 139 alin. (1), art. 140, art. 157 alin. (1) şi ale art. 2204 alin. (1) din Legea nr. 227/2015, cu modificările şi completările ulterioare, începând cu data de 1 ianuarie 2025, în cazul salariaţilor care desfăşoară activitate în baza contractului individual de muncă, încadraţi cu normă întreagă, la locul unde se află funcţia de bază, nu se datorează impozit pe venit şi nu …

### `cote/facilitate_salariu_minim@2026-07-01` — **CONCORDĂ**

- **cod iConta:** `200` din 2026-07-01 — core/common.py:674 (registrul COTE)
- **temei declarat:** OUG 89 2025
- **atom-valoare:** `oug_89_2025#artIII~2/alin1` → `200`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > Prin derogare de la prevederile art. 78 , art. 139 alin. (1) , art. 140 , art. 157 alin. (1) și ale art. 220^4 alin. (1) din Legea nr. 227/2015 , cu modificările și completările ulterioare, în cazul salariaților care desfășoară activitate în baza contractului individual de muncă, încadrați cu normă întreagă, la locul unde se află funcția de bază, pentru suma de 300 lei/lună din veniturile din salarii și asimilate sal…

### `cote/impozit_dividend@2016-01-01` — **CONCORDĂ**

- **cod iConta:** `0.05` din 2016-01-01 — core/common.py:618 (registrul COTE)
- **temei declarat:** OUG 50 2015
- **atom-valoare:** `oug_50_2015_consolidat#artI~2/pct17` → `5%`
- **atom-valabilitate:** `oug_50_2015_consolidat#artI~2/pct17` din **2016-01-01** (textul atomului (Incepand cu data de ...))

  > La articolul 133, după alineatul (7) se introduce un nou alineat, alineatul (8), cu următorul cuprins: "(8) Cota de impozit de 5% se aplică asupra veniturilor din dividende distribuite începând cu data de 1 ianuarie 2016."

### `cote/impozit_dividend@2023-01-01` — **CONCORDĂ**

- **cod iConta:** `0.08` din 2023-01-01 — core/common.py:617 (registrul COTE)
- **temei declarat:** OG 16 2022
- **atom-valoare:** `og_16_2022_consolidat#artI/alin4` → `8%`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > În cazul contribuabililor prevăzuți la art. 47 care devin plătitori de impozit pe profit în conformitate cu prevederile art. 52, pentru aplicarea facilității se ia în considerare profitul contabil brut cumulat de la începutul trimestrului respectiv investit în activele prevăzute la alin. (1), puse în funcțiune începând cu trimestrul în care aceștia au devenit plătitori de impozit pe profit. ... 2. La articolul 24 ali…

### `cote/impozit_dividend@2025-01-01` — **CONCORDĂ**

- **cod iConta:** `0.10` din 2025-01-01 — core/common.py:616 (registrul COTE)
- **temei declarat:** OUG 156 2024
- **atom-valoare:** `oug_156_2024#artLXIV/pct9` → `10%`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > La articolul 97, alineatul (7) se modifică şi va avea următorul cuprins: "(7) Veniturile sub formă de dividende, inclusiv câştigul obţinut ca urmare a deţinerii de titluri de participare definite de legislaţia în materie la organisme de plasament colectiv, se impozitează cu o cotă de 10% din suma acestora, impozitul fiind final. Obligaţia calculării şi reţinerii impozitului pe veniturile sub formă de dividende revine…

### `cote/impozit_dividend@2026-01-01` — **CONCORDĂ**

- **cod iConta:** `0.16` din 2026-01-01 — core/common.py:615 (registrul COTE)
- **temei declarat:** Legea 141 2025
- **atom-valoare:** `legea_141_2025_consolidat#artII` → `16%`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > Legea nr. 227/2015 privind Codul fiscal , publicată în Monitorul Oficial al României, Partea I, nr. 688 din 10 septembrie 2015, cu modificările și completările ulterioare, se modifică și se completează după cum urmează: 1. La articolul 43, alineatul (2) se modifică și va avea următorul cuprins: (2) Impozitul pe dividende se stabilește prin aplicarea unei cote de impozit de 16% asupra dividendului brut plătit unei per…

### `cote/impozit_micro@2023-01-01` — **CONCORDĂ**

- **cod iConta:** `0.01` din 2023-01-01 — core/common.py:652 (registrul COTE)
- **temei declarat:** CF
- **atom-valoare:** `cod_fiscal_227_2015_consolidat#art51/alin1` → `1%`
- **atom-valabilitate:** `cod_fiscal_227_2015_consolidat#art51/alin1` din **2026-01-01** (nota de consolidare) — ⚠ codul dateaza valoarea din 2023-01-01; corpusul arata 2026-01-01. O nota de consolidare e data ultimei modificari a TEXTULUI, nu neaparat a valorii - de citit, nu de clasificat.

  > Cota de impozit pe veniturile microîntreprinderilor este de 1%.

### `cote/impozit_profit@2018-01-01` — **CONCORDĂ**

- **cod iConta:** `0.16` din 2018-01-01 — core/common.py:655 (registrul COTE)
- **temei declarat:** CF
- **atom-valoare:** `cod_fiscal_227_2015_consolidat#art17` → `16%`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > Cota de impozitare Cota de impozit pe profit care se aplică asupra profitului impozabil este de 16%. +

### `cote/impozit_venit@2018-01-01` — **CONCORDĂ**

- **cod iConta:** `0.10` din 2018-01-01 — core/common.py:664 (registrul COTE)
- **temei declarat:** CF
- **atom-valoare:** `cod_fiscal_227_2015_consolidat#art78/alin2` → `10%`
- **atom-valabilitate:** `cod_fiscal_227_2015_consolidat#art78/alin2` din **2026-03-01** (nota de consolidare) — ⚠ codul dateaza valoarea din 2018-01-01; corpusul arata 2026-03-01. O nota de consolidare e data ultimei modificari a TEXTULUI, nu neaparat a valorii - de citit, nu de clasificat.

  > Impozitul lunar prevăzut la alin. (1) se determină astfel: a) la locul unde se află funcția de bază, prin aplicarea cotei de 10% asupra bazei de calcul determinată ca diferență între venitul net din salarii calculat prin deducerea din venitul brut a contribuțiilor sociale obligatorii aferente unei luni, datorate potrivit legii în România sau în conformitate cu instrumentele juridice internaționale la care România est…

### `cote/plafon_avans_decontare@2023-12-15` — **CONCORDĂ**

- **cod iConta:** `5000` din 2023-12-15 — core/common.py:647 (registrul COTE)
- **temei declarat:** OUG 115 2023
- **atom-valoare:** `oug_115_2023_consolidat#artLXIV` → `5.000`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > …publicată, cu modificările și completările ulterioare; ... e) hipermagazin - structură de vânzare, astfel cum este definit la art. 4 lit. s) din Ordonanța Guvernului nr. 99/2000, republicată , cu modificările și completările ulterioare. ... ... 2. La articolul 3 alineatul (1), litera e) se modifică și va avea următorul cuprins: e) plăți din avansuri spre decontare, în limita unui plafon zilnic de 5.000 lei, stabilit…

### `cote/plafon_facilitate_salariu_minim@2025-01-01` — **CONCORDĂ**

- **cod iConta:** `4300` din 2025-01-01 — core/common.py:680 (registrul COTE)
- **temei declarat:** OUG 156 2024
- **atom-valoare:** `oug_156_2024#artLXVI/alin1/litb` → `4.300`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > venitul brut realizat din salarii şi asimilate salariilor, astfel cum este definit la art. 76 alin. (1) - (3) din Legea nr. 227/2015, cu modificările şi completările ulterioare, fără a include contravaloarea tichetelor de masă, voucherelor de vacanţă, respectiv indemnizaţia de hrană, după caz, acordate potrivit legii, în baza aceluiaşi contract individual de muncă, pentru aceeaşi lună, nu depăşeşte nivelul de 4.300 l…

### `cote/plafon_facilitate_salariu_minim@2026-01-01` — **CONCORDĂ**

- **cod iConta:** `4300` din 2026-01-01 — core/common.py:679 (registrul COTE)
- **temei declarat:** OUG 89 2025
- **atom-valoare:** `oug_89_2025#artIII~2/alin1/litb` → `4.300`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > venitul brut realizat din salarii și asimilate salariilor, astfel cum este definit la art. 76 alin. (1 )-( 3) din Legea nr. 227/2015 , cu modificările și completările ulterioare, fără a include contravaloarea tichetelor de masă, voucherelor de vacanță, respectiv indemnizația de hrană, după caz, acordate potrivit legii, în baza aceluiași contract individual de muncă, pentru aceeași lună, nu depășește nivelul de 4.300 …

### `cote/plafon_facilitate_salariu_minim@2026-07-01` — **CONCORDĂ**

- **cod iConta:** `4600` din 2026-07-01 — core/common.py:678 (registrul COTE)
- **temei declarat:** OUG 89 2025
- **atom-valoare:** `oug_89_2025#artIII~2/alin1/litb` → `4.600`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > venitul brut realizat din salarii și asimilate salariilor, astfel cum este definit la art. 76 alin. (1 )-( 3) din Legea nr. 227/2015 , cu modificările și completările ulterioare, fără a include contravaloarea tichetelor de masă, voucherelor de vacanță, respectiv indemnizația de hrană, după caz, acordate potrivit legii, în baza aceluiași contract individual de muncă, pentru aceeași lună, nu depășește nivelul de 4.300 …

### `cote/plafon_intrastat@2026-01-01` — **CONCORDĂ**

- **cod iConta:** `1000000` din 2026-01-01 — core/common.py:641 (registrul COTE)
- **temei declarat:** Ordin 1604 2025
- **atom-valoare:** `ordin_1604_2025_intrastat_mo#frag3` → `1.000.000`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > …terioare, având în vedere Nota de prezentare și motivare nr. 97.674/2025 a direcției generale de statistică economică din cadrul Institutului Național de Statistică, președintele Institutului Național de Statistică emite următorul ordin: Art. 1. — Se aprobă următoarele praguri valorice Intrastat pentru colectarea informațiilor statistice de comerț intra-UE cu bunuri pentru anul de referință 2026: 1.000.000 lei pentr…

### `cote/plafon_mijloc_fix@2015-01-01` — **CONCORDĂ**

- **cod iConta:** `2500` din 2015-01-01 — core/common.py:629 (registrul COTE)
- **temei declarat:** HG 276 2013
- **atom-valoare:** `hg_276_2013#art1~2/alin1` → `2.500`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > Începând cu data intrării în vigoare a prezentei hotărâri, valoarea minimă de intrare a mijloacelor fixe stabilită în condiţiile art. 3 alin. 2 lit. a) din Legea nr. 15/1994 privind amortizarea capitalului imobilizat în active corporale şi necorporale, republicată, cu modificările şi completările ulterioare, este de 2.500 lei. ...

### `cote/plafon_mijloc_fix@2026-01-01` — **CONCORDĂ**

- **cod iConta:** `5000` din 2026-01-01 — core/common.py:628 (registrul COTE)
- **temei declarat:** OUG 8 2026
- **atom-valoare:** `oug_8_2026#art20^1/alin15` → `5.000`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > …t care se încheie în anul 2026. În situația în care rezervele fiscale respective sunt menținute până la lichidare, acestea nu sunt luate în calcul pentru determinarea rezultatului fiscal al lichidării. ... 7. La articolul 28 alineatul (2), litera b) se modifică și va avea următorul cuprins: b) la data intrării în patrimoniul contribuabilului, are o valoare fiscală egală sau mai mare decât suma de 5.000 lei; această …

### `cote/plafon_sold_casa@2015-05-09` — **CONCORDĂ**

- **cod iConta:** `50000` din 2015-05-09 — core/common.py:644 (registrul COTE)
- **temei declarat:** Legea 70 2015
- **atom-valoare:** `legea_70_2015_consolidat#art18` → `50.000`
- **atom-valabilitate:** `legea_70_2015_consolidat#art18` din **2019-01-06** (nota de consolidare) — ⚠ codul dateaza valoarea din 2015-05-09; corpusul arata 2019-01-06. O nota de consolidare e data ultimei modificari a TEXTULUI, nu neaparat a valorii - de citit, nu de clasificat.

  > … de plată autorizate de Banca Națională a României sau autorizate în alt stat membru al Uniunii Europene și notificate către Banca Națională a României, potrivit legii, efectuate ca urmare a transferului dreptului de proprietate asupra unor bunuri sau drepturi, a prestării de servicii, precum și cele reprezentând acordarea/restituirea de împrumuturi, se pot efectua în limita unui plafon zilnic de 50.000 lei/tranzacț…

### `cote/plafon_tva_incasare@2021-01-01` — **CONCORDĂ**

- **cod iConta:** `4500000` din 2021-01-01 — core/common.py:625 (registrul COTE)
- **temei declarat:** Legea 296 2020
- **atom-valoare:** `legea_296_2020_consolidat#art231/alin1` → `4.500.000`
- **atom-valabilitate:** `legea_296_2020_consolidat#art231/alin1` din **2022-01-01** (nota de consolidare) — ⚠ codul dateaza valoarea din 2021-01-01; corpusul arata 2022-01-01. O nota de consolidare e data ultimei modificari a TEXTULUI, nu neaparat a valorii - de citit, nu de clasificat.

  > …eea ce privește ajustarea dreptului de deducere prevăzută de lege. ... 158. La articolul 282 alineatul (3), litera a) se modifică și va avea următorul cuprins: a) persoanele impozabile înregistrate în scopuri de TVA conform art. 316, care au sediul activității economice în România conform art. 266 alin. (2) lit. a), a căror cifră de afaceri în anul calendaristic precedent nu a depășit plafonul de 4.500.000 lei. Pers…

### `cote/plafon_tva_incasare@2026-03-01` — **CONCORDĂ**

- **cod iConta:** `5000000` din 2026-03-01 — core/common.py:624 (registrul COTE)
- **temei declarat:** OUG 8 2026
- **atom-valoare:** `oug_8_2026#art20^1/alin5^1/litg^2` → `5.000.000`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > … (3) Prin excepție de la prevederile alin. (1) și alin. (2) lit. a), exigibilitatea taxei intervine la data încasării contravalorii integrale sau parțiale a livrării de bunuri ori a prestării de servicii, în cazul persoanelor impozabile care optează în acest sens, denumite în continuare persoane care aplică sistemul TVA la încasare. Plafonul pentru aplicarea sistemului TVA la încasare este de: a) 5.000.000 lei, în p…

### `cote/plafon_tva_incasare@2027-01-01` — **CONCORDĂ**

- **cod iConta:** `5500000` din 2027-01-01 — core/common.py:623 (registrul COTE)
- **temei declarat:** OUG 8 2026
- **atom-valoare:** `oug_8_2026#art20^1/alin5^1/litb` → `5.500.000`
- **atom-valabilitate:** `oug_8_2026#art20^1/alin5^1/litb` din **2027-01-01** (textul atomului (Incepand cu data de ...))

  > 5.500.000 lei, începând cu data de 1 ianuarie 2027. ... ... 39. La articolul 282, după alineatul (3) se introduce un nou alineat, alin. (3^1), cu următorul cuprins: (3^1) Sunt eligibile pentru aplicarea sistemului TVA la încasare: a) persoanele impozabile înregistrate în scopuri de TVA conform art. 316, care au sediul activității economice în România conform art. 266 alin. (2) lit. a), a căror cifră de afaceri în anu…

### `cote/salariu_minim@2025-01-01` — **CONCORDĂ**

- **cod iConta:** `4050` din 2025-01-01 — core/common.py:671 (registrul COTE)
- **temei declarat:** HG 1506 2024
- **atom-valoare:** `hg_1506_2024_salariu_minim#art1` → `4.050`
- **atom-valabilitate:** `hg_1506_2024_salariu_minim#art1` din **2025-01-01** (textul atomului (Incepand cu data de ...))

  > Începând cu data de 1 ianuarie 2025, salariul de bază minim brut pe țară garantat în plată se stabilește în bani, fără a include sporuri și alte adaosuri, la suma de 4.050 lei lunar, pentru un program normal de lucru în medie de 165,334 ore pe lună, reprezentând 24,496 lei/oră. +

### `cote/salariu_minim@2026-07-01` — **CONCORDĂ**

- **cod iConta:** `4325` din 2026-07-01 — core/common.py:670 (registrul COTE)
- **temei declarat:** HG 146 2026
- **atom-valoare:** `hg_146_2026_salariu_minim#art1` → `4.325`
- **atom-valabilitate:** `hg_146_2026_salariu_minim#art1` din **2026-07-01** (textul atomului (Incepand cu data de ...))

  > Începând cu data de 1 iulie 2026, salariul de bază minim brut pe țară garantat în plată, prevăzut la art. 164 alin. (1) din Legea nr. 53/2003 - Codul muncii, republicată , cu modificările și completările ulterioare, se stabilește în bani, fără a include sporuri și alte adaosuri, la suma de 4.325 lei lunar, pentru un program normal de lucru în medie de 166,667 ore pe lună, reprezentând 25,949 lei/oră. +

### `cote/tichet_masa_plafon@2025-01-01` — **NEVERIFICAT**

- **cod iConta:** `40.04` din 2025-01-01 — core/common.py:685 (registrul COTE)
- **temei declarat:** Ordin 4679 2024
- **atom-valoare:** `anaf_limite_2025#frag24` → `40,04`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > 6 prevederi nu poate depăşi suma Începând cu data de 1 OUG nr. 69/2023 pentru de 40 lei ianuarie 2024 şi pentru lunile modificarea art. 14 din Legea august şi septembrie 2024 nr. 165/2018 privind acordarea biletelor de valoare, precum şi pentru stabilirea unor măsuri pentru aplicarea acestor prevederi nu poate depăși cuantumul Semestrul II al anului 2024, Ordinul MF nr. 4.679/2024 pen- de 40,04 lei începând cu luna o…

  *CONCORDA pe o sursa care NU e act normativ (pliant sau ghid ANAF - material de informare, nu act normativ). Decizia C2: un temei se ia numai din act normativ. Rezultatul initial (CONCORDA) se pastreaza in `clasificare_initiala`.*

### `cote/tichet_masa_plafon@2025-04-01` — **NEVERIFICAT**

- **cod iConta:** `40.18` din 2025-04-01 — core/common.py:684 (registrul COTE)
- **temei declarat:** Ordin 484 2025
- **atom-valoare:** `anaf_limite_2025#frag24` → `40,18`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > 6 prevederi nu poate depăşi suma Începând cu data de 1 OUG nr. 69/2023 pentru de 40 lei ianuarie 2024 şi pentru lunile modificarea art. 14 din Legea august şi septembrie 2024 nr. 165/2018 privind acordarea biletelor de valoare, precum şi pentru stabilirea unor măsuri pentru aplicarea acestor prevederi nu poate depăși cuantumul Semestrul II al anului 2024, Ordinul MF nr. 4.679/2024 pen- de 40,04 lei începând cu luna o…

  *CONCORDA pe o sursa care NU e act normativ (pliant sau ghid ANAF - material de informare, nu act normativ). Decizia C2: un temei se ia numai din act normativ. Rezultatul initial (CONCORDA) se pastreaza in `clasificare_initiala`.*

### `cote/tichet_masa_plafon@2025-11-01` — **CONCORDĂ**

- **cod iConta:** `45` din 2025-11-01 — core/common.py:683 (registrul COTE)
- **temei declarat:** Legea 201 2025
- **atom-valoare:** `legea_201_2025#art14` → `45`
- **atom-valabilitate:** `legea_165_2018_consolidat#art14` din **2025-12-01** (nota de consolidare, pe acelasi articol/alineat) — ⚠ codul dateaza valoarea din 2025-11-01; corpusul arata 2025-12-01. O nota de consolidare e data ultimei modificari a TEXTULUI, nu neaparat a valorii - de citit, nu de clasificat.

  > Valoarea nominală a unui tichet de masă nu poate depăși suma de 45 lei. ... 2. După articolul 20 se introduce un nou articol, art. 20^1, cu următorul cuprins: +

  *valoarea NU s-a gasit la nivelul cel mai tare de proba (ancora pe articolul din Temei (legea_201_2025#artI)), ci la citatul declarat de iConta, gasit verbatim in actul declarat - citarea iConta duce la actul corect, dar nu exact la unitatea care stabileste valoarea*

### `cote/tva_redusa@2025-08-01` — **CONCORDĂ**

- **cod iConta:** `0.11` din 2025-08-01 — core/common.py:590 (registrul COTE)
- **temei declarat:** Legea 141 2025
- **atom-valoare:** `legea_141_2025_consolidat#art291/alin2` → `11%`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > Cota redusă de 11% se aplică asupra bazei de impozitare pentru următoarele prestări de servicii și/sau livrări de bunuri: a) livrarea de medicamente de uz uman; ...

### `cote/tva_redusa_5@2016-01-01` — **NEVERIFICAT**

- **cod iConta:** `0.05` din 2016-01-01 — core/common.py:605 (registrul COTE)
- **temei declarat:** Legea 227 2015
- **atom-valoare:** `cf_art291_2016_forma_initiala#art291/alin3/litc/pct3` → `5%`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > …epaseste suprafata de 250 m2, inclusiv amprenta la sol a locuintei, in cazul caselor de locuit individuale. In cazul imobilelor care au mai mult de doua locuinte, cota indiviza a terenului aferent fiecarei locuinte nu poate depasi suprafata de 250 m2, inclusiv amprenta la sol aferenta fiecarei locuinte. Orice persoana necasatorita sau familie poate achizitiona o singura locuinta cu cota redusa de 5%, respectiv: (i) …

  *CONCORDA pe o sursa care NU e act normativ (nota redactata de iConta (PROVENIENTA: SCRIS - nota proprie despre forma initiala a CF art. 291 la 01.01.2016, cu sursa si observatiile c), nu act normativ). Decizia C2: un temei se ia numai din act normativ. Rezultatul initial (CONCORDA) se pastreaza in `…*

### `cote/tva_redusa_5@2025-08-01` — **CONCORDĂ**

- **cod iConta:** `0.11` din 2025-08-01 — core/common.py:604 (registrul COTE)
- **temei declarat:** Legea 141 2025
- **atom-valoare:** `legea_141_2025_consolidat#art291/alin2` → `11%`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > Cota redusă de 11% se aplică asupra bazei de impozitare pentru următoarele prestări de servicii și/sau livrări de bunuri: a) livrarea de medicamente de uz uman; ...

### `cote/tva_redusa_9@2016-01-01` — **NEVERIFICAT**

- **cod iConta:** `0.09` din 2016-01-01 — core/common.py:601 (registrul COTE)
- **temei declarat:** Legea 227 2015
- **atom-valoare:** `cf_art291_2016_forma_initiala#art291/alin2` → `9%`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > Cota redusa de 9% se aplica asupra bazei de impozitare pentru urmatoarele prestari de servicii si/sau livrari de bunuri:

  *CONCORDA pe o sursa care NU e act normativ (nota redactata de iConta (PROVENIENTA: SCRIS - nota proprie despre forma initiala a CF art. 291 la 01.01.2016, cu sursa si observatiile c), nu act normativ). Decizia C2: un temei se ia numai din act normativ. Rezultatul initial (CONCORDA) se pastreaza in `…*

### `cote/tva_redusa_9@2025-08-01` — **CONCORDĂ**

- **cod iConta:** `0.11` din 2025-08-01 — core/common.py:600 (registrul COTE)
- **temei declarat:** Legea 141 2025
- **atom-valoare:** `legea_141_2025_consolidat#art291/alin2` → `11%`
- **atom-valabilitate:** **LIPSĂ** — niciun atom din corpus nu poarta data de intrare in vigoare pentru aceasta valoare pe acelasi articol si alineat - valabilitatea NU e dovedita, doar valoarea

  > Cota redusă de 11% se aplică asupra bazei de impozitare pentru următoarele prestări de servicii și/sau livrări de bunuri: a) livrarea de medicamente de uz uman; ...

### `cote/tva_standard@2017-01-01` — **CONCORDĂ**

- **cod iConta:** `0.19` din 2017-01-01 — core/common.py:587 (registrul COTE)
- **temei declarat:** Legea 227 2015
- **atom-valoare:** `cf_2015_forma_initiala#art291/alin1/litb` → `19%`
- **atom-valabilitate:** `cf_2015_forma_initiala#art291/alin1/litb` din **2017-01-01** (textul atomului (Incepand cu data de ...))

  > 19% începând cu data de 1 ianuarie 2017. ...

### `cote/tva_standard@2025-08-01` — **CONCORDĂ**

- **cod iConta:** `0.21` din 2025-08-01 — core/common.py:586 (registrul COTE)
- **temei declarat:** Legea 141 2025
- **atom-valoare:** `legea_141_2025_consolidat#art291/alin1` → `21%`
- **atom-valabilitate:** `cod_fiscal_227_2015_consolidat#art291/alin1` din **2025-08-01** (nota de consolidare, pe acelasi articol/alineat)

  > Cota standard se aplică asupra bazei de impozitare pentru operațiunile impozabile care nu sunt scutite de taxă sau care nu sunt supuse cotei reduse, iar nivelul acesteia este 21%.

## 5. DIFERĂ — ambele părți

### `nomenclator/d394.TIPURI`

- **cod iConta:** `L,A,LS,AS,AI,V,C,N` — core/nomenclatoare.py:103 (ANCORE_NORMA)
- **textul legii:** `a/ai/as/c/i1/i2/l/ls/n/v` — atom `opanaf_2194_2025_d394#artIV/pct2/pct7/pct2`
- **numai în cod:** — · **numai în act:** ['i1', 'i2']

  > Coloana "Tip L/A/LS/AS/AÎ/V/C/N/Î1/Î2" de la lit. C, D, E, F, G - se înscrie tipul operaţiunii efectuate, şi anume: - L - livrări de bunuri/prestări de servicii pentru care au fost emise facturi, cu excepţia facturilor simplificate; - A - achiziţii de bunuri/servicii pentru care au fost primite facturi, cu excepţia facturilor simplificate; - LS - livrări de bunuri/prestări de servicii pentru care au fost emise facturi de către persoanele impozabile care aplică regimul special pentru agenţiile de…

  *enumerarea actului nu e aceeasi cu a codului: numai in cod -, numai in act ['i1', 'i2'] (actul declarat (opanaf_2194_2025_d394))*

## 6. NEVERIFICAT — probă de aprobat, nu verdict

**25** parametri. Două feluri, cu motive diferite:

**a) Temei declarat de iConta, dar pe o sursă care nu e act normativ (4).** Verificarea s-a făcut, dar pe o notă redactată de iConta sau pe un pliant — deci nu e o verificare pe lege. Rezultatul inițial e păstrat.

| Parametru                          | Cod   | Inițial  | Sursa citată                  |
|------------------------------------|-------|----------|-------------------------------|
| cote/tva_redusa_9@2016-01-01       | 0.09  | CONCORDĂ | cf_art291_2016_forma_initiala |
| cote/tva_redusa_5@2016-01-01       | 0.05  | CONCORDĂ | cf_art291_2016_forma_initiala |
| cote/tichet_masa_plafon@2025-04-01 | 40.18 | CONCORDĂ | anaf_limite_2025              |
| cote/tichet_masa_plafon@2025-01-01 | 40.04 | CONCORDĂ | anaf_limite_2025              |

**b) Constantă fără temei, cu TEMEI CANDIDAT dintr-un act normativ (21).** Lista completă, cu fragmentul verbatim, e în `temeiuri_candidate.json` — livrabil pentru iConta, **de aprobat uman, nu se aplică**.

| Parametru                                      | Cod      | Temei candidat                                                                              | În text    |
|------------------------------------------------|----------|---------------------------------------------------------------------------------------------|------------|
| nesursat/bacsis.COTA_IMPOZIT=10                | 10       | cod_fiscal_227_2015_consolidat#art64/alin1                                                  | 10%        |
| nesursat/casa.PLAFON_INCASARE_PJ=5000          | 5000     | oug_115_2023_consolidat#artLXIV                                                             | 5.000      |
| nesursat/casa.PLAFON_INCASARE_PJ_CC=10000      | 10000    | legea_296_2023_masuri_fiscal_bugetare_asigurarea_sustenabilitatii#art4~2/alin1              | 10.000     |
| nesursat/casa.PLAFON_PLATA_PJ=5000             | 5000     | oug_115_2023_consolidat#artLXIV                                                             | 5.000      |
| nesursat/casa.PLAFON_PLATA_PJ_TOTAL=10000      | 10000    | legea_296_2023_masuri_fiscal_bugetare_asigurarea_sustenabilitatii#art4~2/alin1              | 10.000     |
| nesursat/cote_tva.COTA_STANDARD=21             | 21       | cod_fiscal_227_2015_consolidat#art291/alin1                                                 | 21%        |
| nesursat/cote_tva.COTA_REDUSA=11               | 11       | cod_fiscal_227_2015_consolidat#art291/alin2                                                 | 11%        |
| nesursat/d100_pozitia_116.PRAG_BRENT_USD=70    | 70       | oug_24_2026_contributie_solidaritate#art9/alin6                                             | 70         |
| nesursat/d101.COTA_STANDARD=16                 | 16       | cod_fiscal_227_2015_consolidat#art17                                                        | 16%        |
| nesursat/d101.PRAG_IMCA_EUR=50000000           | 50000000 | cod_fiscal_227_2015_consolidat#art18^1/alin8                                                | 50.000.000 |
| nesursat/d101g.COTA_STANDARD=16                | 16       | cod_fiscal_227_2015_consolidat#art17                                                        | 16%        |
| nesursat/d216.COTA_IMPOZIT=0.3                 | 0.3      | legea_296_2023_masuri_fiscal_bugetare_asigurarea_sustenabilitatii#art500^2                  | 0,3%       |
| nesursat/d394.COTE=5                           | 5        | og_16_2022_consolidat#artIII/alin4/litb                                                     | 5%         |
| nesursat/d394.COTE=9                           | 9        | cod_fiscal_227_2015_consolidat#art291/alin3~2/litc                                          | 9%         |
| nesursat/d394.COTE=11                          | 11       | opanaf_2194_2025_d394#artIV/pct1/pct7/pct2/pct5/pct4/pct3/pct17/pct10/pct10/pct10/pct4/pct3 | 11%        |
| nesursat/d394.COTE=19                          | 19       | opanaf_77_2022#artIII/pct2/alin6~2/pct4/pct3                                                | 19%        |
| nesursat/d394.COTE=20                          | 20       | opanaf_3769_2015_d394_baza#art12/alin21~2/pct5/pct2                                         | 20%        |
| nesursat/d394.COTE=21                          | 21       | opanaf_2194_2025_d394#artIV/pct1/pct7/pct2/pct5/pct4/pct3/pct17/pct10/pct10/pct10/pct4/pct3 | 21%        |
| nesursat/d394.COTE=24                          | 24       | opanaf_77_2022#artIII/pct2/alin6~2/pct4/pct3                                                | 24%        |
| nesursat/salarizare.PRAG_VENIT_DEDUCERE=2000   | 2000     | cod_fiscal_227_2015_consolidat#art77/alin3                                                  | 2.000      |
| nesursat/taxare_inversa.PRAG_ELECTRONICE=22500 | 22500    | cod_fiscal_227_2015_consolidat#art331/alin7                                                 | 22.500     |

## 7. NEGĂSIT — și de ce

**cont folosit de iConta, absent din planurile de conturi din corpus** (5):

- `cont/412` = `412` — core/ in 2 locuri: control_incrucisat.py:397 COD_CONT_D112, salarii_contare.py:57 CONT_D11…
- `cont/432` = `432` — core/ in 2 locuri: control_incrucisat.py:398 COD_CONT_D112, salarii_contare.py:58 CONT_D11…
- `cont/459` = `459` — core/ in 2 locuri: control_incrucisat.py:398 COD_CONT_D112, salarii_contare.py:61 CONT_D11…
- `cont/480` = `480` — core/ in 2 locuri: control_incrucisat.py:399 COD_CONT_D112, salarii_contare.py:59 CONT_D11…
- `cont/739` = `739` — core/ in 1 locuri: ong.py:22 CONT_VENIT

**normă deschisă — nu există enumerare de confirmat** (2):

- `nomenclator/d301.VALUTE` = `` — core/nomenclatoare.py:143 (ANCORE_NORMA)
- `nomenclator/d390.TARI_UE` = `` — core/nomenclatoare.py:124 (ANCORE_NORMA)

**parametru operațional, fără act normativ de citat** (9):

- `nesursat/control_fiscal_api.PRAG_URMARIT_ZILE=7` = `7` — core/control_fiscal_api.py:31
- `nesursat/curs_bnr.PRAG_VECHIME_ZILE=5` = `5` — core/curs_bnr.py:51
- `nesursat/intrastat.PRAG_ATENTIE=0.80` = `0.80` — core/intrastat.py:19
- `nesursat/notificari_scadenta.PRAGURI=-3` = `-3` — core/notificari_scadenta.py:23
- `nesursat/notificari_scadenta.PRAGURI=7` = `7` — core/notificari_scadenta.py:23
- `nesursat/registru_evidenta_fiscala.DOAR_VENITURI=3` = `3` — core/registru_evidenta_fiscala.py:258
- `nesursat/scadentar.PRAG_ZILE=7` = `7` — core/scadentar.py:19
- `nesursat/stare_partajata.PRAG_ESECURI=5` = `5` — core/stare_partajata.py:65
- `nesursat/stare_partajata.PRAG_RITM=5` = `5` — core/stare_partajata.py:71

**potrivire prea slabă ca să susțină un verdict** (11):

- `nesursat/beneficii_api.PLAFON_CADOU=300` = `300` — core/beneficii_api.py:22
- `nesursat/casa.PLAFON_PF=10000` = `10000` — core/casa.py:26
- `nesursat/casa.PLAFON_SOLD_ZI_CC=500000` = `500000` — core/casa.py:21
- `nesursat/d108.IMPOZIT_ANUAL=18000` = `18000` — core/d108.py:58
- `nesursat/ong.PLAFON_EUR=15000` = `15000` — core/ong.py:23
- `nesursat/salarizare.DEDUCERE_COPIL_SCOALA=100` = `100` — core/salarizare.py:28
- `nesursat/salarizare._PCT_DEDUCERE_BAZA=0.20` = `0.20` — core/salarizare.py:23
- `nesursat/salarizare._PCT_DEDUCERE_BAZA=0.25` = `0.25` — core/salarizare.py:23
- `nesursat/salarizare._PCT_DEDUCERE_BAZA=0.30` = `0.30` — core/salarizare.py:23
- `nesursat/salarizare._PCT_DEDUCERE_BAZA=0.35` = `0.35` — core/salarizare.py:23
- `nesursat/salarizare._PCT_DEDUCERE_BAZA=0.45` = `0.45` — core/salarizare.py:23

## 8. Termene și nomenclatoare

- **`nomenclator/d301.VALUTE`** = `` → **NEGĂSIT** · atom `—`
- **`nomenclator/d390.TARI_UE`** = `` → **NEGĂSIT** · atom `—`
- **`nomenclator/d390.TIPURI`** = `L,T,A,P,S,R` → **CONCORDĂ** · atom `opanaf_705_2020_d390#art10/alin8`
  > lit. c) şi d) din Codul fiscal. Coloana "Tipul operaţiunii": L - pentru livrări intracomunitare de bunuri către alte state membre; T - pentru livrări în cadrul unei operaţiuni triunghiulare; A - pentru achiziţii intracom…
- **`nomenclator/d394.TIPURI`** = `L,A,LS,AS,AI,V,C,N` → **DIFERĂ** · atom `opanaf_2194_2025_d394#artIV/pct2/pct7/pct2`
  - numai în act: ['i1', 'i2'] — numai în cod: —
  > Coloana "Tip L/A/LS/AS/AÎ/V/C/N/Î1/Î2" de la lit. C, D, E, F, G - se înscrie tipul operaţiunii efectuate, şi anume: - L - livrări de bunuri/prestări de servicii pentru care au fost emise facturi, cu excepţia facturilor s…
- **`termen/d300`** = `25` → **CONCORDĂ** · atom `cod_fiscal_227_2015_consolidat#art323/alin1`
  > Persoanele înregistrate conform art. 316 trebuie să depună la organele fiscale competente, pentru fiecare perioadă fiscală, un decont de taxă, până la data de 25 inclusiv a lunii următoare celei în care se încheie perioa…
- **`termen/d301`** = `25` → **CONCORDĂ** · atom `cod_fiscal_227_2015_consolidat#art324/alin2`
  > Decontul special de taxă trebuie întocmit potrivit modelului stabilit prin ordin al președintelui A.N.A.F. și se depune până la data de 25 inclusiv a lunii următoare celei în care ia naștere exigibilitatea operațiunilor …
- **`termen/d390`** = `25` → **CONCORDĂ** · atom `opanaf_705_2020_d390#art10/pct3/pct3/pct6/pct1/pct1`
  > 1. Declaraţia recapitulativă se depune lunar, până la data de 25 inclusiv a lunii următoare unei luni calendaristice, de către persoanele impozabile înregistrate în scopuri de TVA conform art. 316 sau 317 din Codul fisca…
- **`termen/d394`** = `30` → **CONCORDĂ** · atom `opanaf_2194_2025_d394#artIV/pct1/pct7/pct2/pct2`
  > Declaraţia se depune la organul fiscal competent până în data de 30 inclusiv a lunii următoare încheierii perioadei de raportare, declarate pentru depunerea decontului (luna, trimestrul etc.), inclusiv dacă în această pe…
- **`termen/d406`** = `ultima_zi_luna` → **CONCORDĂ** · atom `opanaf_1783_2021_saft_d406#art8/pct6/pct8/pct29/pct1`
  > Declaraţia informativă D406 se transmite în format electronic, data-limită de transmitere fiind: - ultima zi calendaristică a lunii următoare perioadei de raportare, respectiv luna/trimestrul calendaristic, după caz, pen…

## 9. Conturi

C3: se culeg **numai** simbolurile din containerele pe care iConta le numește CONT (`CONTURI_TVA`, `CONT_AVANS`, `cont_imo`…). Confruntate cu planurile de conturi din corpus: OMFP 1802/2014 (entități economice) și OMFP 3103/2017 (entități fără scop patrimonial) — 655 simboluri citite.

| Cont | Stare    | Denumire în plan                                            | Plan                           |
|------|----------|-------------------------------------------------------------|--------------------------------|
| 1621 | CONCORDĂ | 1621 Credite bancare pe termen lung (P)                     | OMFP 1802/2014; OMFP 3103/2017 |
| 1622 | CONCORDĂ | 1622 Credite bancare pe termen lung nerambursate la scaden… | OMFP 1802/2014; OMFP 3103/2017 |
| 1682 | CONCORDĂ | 1682 Dobânzi aferente creditelor bancare pe termen lung (P… | OMFP 1802/2014; OMFP 3103/2017 |
| 213  | CONCORDĂ | 213 Instalații tehnice și mijloace de transport             | OMFP 1802/2014; OMFP 3103/2017 |
| 2131 | CONCORDĂ | 2131 Echipamente tehnologice (mașini, utilaje și instalați… | OMFP 1802/2014; OMFP 3103/2017 |
| 301  | CONCORDĂ | 301 Materii prime (A)                                       | OMFP 1802/2014; OMFP 3103/2017 |
| 302  | CONCORDĂ | 302 Materiale consumabile                                   | OMFP 1802/2014; OMFP 3103/2017 |
| 303  | CONCORDĂ | 303 Materiale de natura obiectelor de inventar (A)          | OMFP 1802/2014; OMFP 3103/2017 |
| 371  | CONCORDĂ | 371 Mărfuri (A)                                             | OMFP 1802/2014; OMFP 3103/2017 |
| 401  | CONCORDĂ | 401 Furnizori (P)                                           | OMFP 1802/2014; OMFP 3103/2017 |
| 404  | CONCORDĂ | 404 Furnizori de imobilizări (P)                            | OMFP 1802/2014; OMFP 3103/2017 |
| 409  | CONCORDĂ | 409 Furnizori - debitori                                    | OMFP 1802/2014; OMFP 3103/2017 |
| 4091 | CONCORDĂ | 4091 Furnizori - debitori pentru cumpărări de bunuri de na… | OMFP 1802/2014; OMFP 3103/2017 |
| 4092 | CONCORDĂ | 4092 Furnizori - debitori pentru prestări de servicii (A)   | OMFP 1802/2014; OMFP 3103/2017 |
| 4093 | CONCORDĂ | 4093 Avansuri acordate pentru imobilizări corporale (A)     | OMFP 1802/2014; OMFP 3103/2017 |
| 4094 | CONCORDĂ | 4094 Avansuri acordate pentru imobilizări necorporale (A)   | OMFP 1802/2014; OMFP 3103/2017 |
| 4111 | CONCORDĂ | 4111 Clienți (A)                                            | OMFP 1802/2014; OMFP 3103/2017 |
| 4118 | CONCORDĂ | 4118 Clienți incerți sau în litigiu (A)                     | OMFP 1802/2014; OMFP 3103/2017 |
| 412  | NEGĂSIT  | —                                                           |                                |
| 419  | CONCORDĂ | 419 Clienți - creditori (P)                                 | OMFP 1802/2014; OMFP 3103/2017 |
| 421  | CONCORDĂ | 421 Personal - salarii datorate (P)                         | OMFP 1802/2014; OMFP 3103/2017 |
| 4282 | CONCORDĂ | 4282 Alte creanțe în legătură cu personalul (A)             | OMFP 1802/2014; OMFP 3103/2017 |
| 4315 | CONCORDĂ | 4315 Contribuția de asigurări sociale (P)                   | OMFP 1802/2014                 |
| 4316 | CONCORDĂ | 4316 Contribuția de asigurări sociale de sănătate (P)       | OMFP 1802/2014                 |
| 432  | NEGĂSIT  | —                                                           |                                |
| 436  | CONCORDĂ | 436 Contribuția asiguratorie pentru muncă (P)               | OMFP 1802/2014                 |
| 441  | CONCORDĂ | 441 Impozitul pe profit și alte impozite                    | OMFP 1802/2014; OMFP 3103/2017 |
| 4411 | CONCORDĂ | 4411 Impozitul pe profit (P)                                | OMFP 1802/2014; OMFP 3103/2017 |
| 4423 | CONCORDĂ | 4423 TVA de plată (P)                                       | OMFP 1802/2014; OMFP 3103/2017 |
| 4424 | CONCORDĂ | 4424 TVA de recuperat (A)                                   | OMFP 1802/2014; OMFP 3103/2017 |
| 4426 | CONCORDĂ | 4426 TVA deductibilă (A)                                    | OMFP 1802/2014; OMFP 3103/2017 |
| 4427 | CONCORDĂ | 4427 TVA colectată (P)                                      | OMFP 1802/2014; OMFP 3103/2017 |
| 4428 | CONCORDĂ | 4428 TVA neexigibilă (A/P)                                  | OMFP 1802/2014; OMFP 3103/2017 |
| 444  | CONCORDĂ | 444 Impozitul pe venituri de natura salariilor (P)          | OMFP 1802/2014; OMFP 3103/2017 |
| 458  | CONCORDĂ | 458 Decontări din operațiuni în participație                | OMFP 1802/2014; OMFP 3103/2017 |
| 459  | NEGĂSIT  | —                                                           |                                |
| 461  | CONCORDĂ | 461 Debitori diverși (A)                                    | OMFP 1802/2014; OMFP 3103/2017 |
| 480  | NEGĂSIT  | —                                                           |                                |
| 5121 | CONCORDĂ | 5121 Conturi la bănci în lei (A)                            | OMFP 1802/2014; OMFP 3103/2017 |
| 5191 | CONCORDĂ | 5191 Credite bancare pe termen scurt (P)                    | OMFP 1802/2014; OMFP 3103/2017 |
| 5192 | CONCORDĂ | 5192 Credite bancare pe termen scurt nerambursate la scade… | OMFP 1802/2014; OMFP 3103/2017 |
| 5198 | CONCORDĂ | 5198 Dobânzi aferente creditelor bancare pe termen scurt (… | OMFP 1802/2014; OMFP 3103/2017 |
| 5311 | CONCORDĂ | 5311 Casa în lei (A)                                        | OMFP 1802/2014; OMFP 3103/2017 |
| 542  | CONCORDĂ | 542 Avansuri de trezorerie*18) (A)                          | OMFP 1802/2014; OMFP 3103/2017 |
| 581  | CONCORDĂ | 581 Viramente interne (A/P)                                 | OMFP 1802/2014; OMFP 3103/2017 |
| 602  | CONCORDĂ | 602 Cheltuieli cu materialele consumabile                   | OMFP 1802/2014; OMFP 3103/2017 |
| 621  | CONCORDĂ | 621 Cheltuieli cu colaboratorii                             | OMFP 1802/2014; OMFP 3103/2017 |
| 641  | CONCORDĂ | 641 Cheltuieli cu salariile personalului                    | OMFP 1802/2014; OMFP 3103/2017 |
| 6451 | CONCORDĂ | 6451 Cheltuieli privind contribuția unității la asigurăril… | OMFP 1802/2014; OMFP 3103/2017 |
| 6453 | CONCORDĂ | 6453 Cheltuieli privind contribuția angajatorului pentru a… | OMFP 1802/2014; OMFP 3103/2017 |
| 646  | CONCORDĂ | 646 Cheltuieli privind contribuția asiguratorie pentru mun… | OMFP 1802/2014                 |
| 691  | CONCORDĂ | 691 Cheltuieli cu impozitul pe profit                       | OMFP 1802/2014; OMFP 3103/2017 |
| 704  | CONCORDĂ | 704 Venituri din servicii prestate                          | OMFP 1802/2014; OMFP 3103/2017 |
| 707  | CONCORDĂ | 707 Venituri din vânzarea mărfurilor                        | OMFP 1802/2014; OMFP 3103/2017 |
| 731  | CONCORDĂ | 731 Venituri din cotizaţiile membrilor, contribuţiile băne… | OMFP 3103/2017                 |
| 733  | CONCORDĂ | 733 Venituri din donaţii, sume sau bunuri primite prin spo… | OMFP 3103/2017                 |
| 734  | CONCORDĂ | 734 Venituri financiare rezultate din activităţile fără sc… | OMFP 3103/2017                 |
| 736  | CONCORDĂ | 736 Venituri din subvenţii de exploatare                    | OMFP 3103/2017                 |
| 738  | CONCORDĂ | 738 Alte venituri din activităţile fără scop patrimonial    | OMFP 3103/2017                 |
| 739  | NEGĂSIT  | —                                                           |                                |
| 8011 | CONCORDĂ | 8011 Giruri și garanții acordate                            | OMFP 1802/2014; OMFP 3103/2017 |
| 8021 | CONCORDĂ | 8021 Giruri și garanții primite                             | OMFP 1802/2014; OMFP 3103/2017 |

## 10. Cerințe pentru iConta

Ce ar trebui schimbat în iConta ca FiscalOS să poată verifica mai mult. **Nu se aplică nimic** — lista e și în `cerinte_iconta.json`.

- **R-CONT-1** (C3) — Marcarea explicita a simbolurilor de cont. 364 simboluri de 3-4 cifre, in 66 module din core/, nu stau in niciun container numit CONT. Multe sunt conturi reale folosite ca literale directe (`startswith("401")`, tuple pozitionale), dar nu se pot distinge de un an …
- **R-CONT-412** (C3) — Contul 412 nu exista in niciun plan de conturi din corpus. iConta foloseste 412 ca CONT (core/ in 2 locuri: control_incrucisat.py:397 COD_CONT_D112, salarii_contare.py:5), dar simbolul nu apare in niciun plan de conturi din corpus (OMFP 1802/2014, OMFP 3103/2017; 655 simboluri c…
- **R-CONT-432** (C3) — Contul 432 nu exista in niciun plan de conturi din corpus. iConta foloseste 432 ca CONT (core/ in 2 locuri: control_incrucisat.py:398 COD_CONT_D112, salarii_contare.py:5), dar simbolul nu apare in niciun plan de conturi din corpus (OMFP 1802/2014, OMFP 3103/2017; 655 simboluri c…
- **R-CONT-459** (C3) — Contul 459 nu exista in niciun plan de conturi din corpus. iConta foloseste 459 ca CONT (core/ in 2 locuri: control_incrucisat.py:398 COD_CONT_D112, salarii_contare.py:6), dar simbolul nu apare in niciun plan de conturi din corpus (OMFP 1802/2014, OMFP 3103/2017; 655 simboluri c…
- **R-CONT-480** (C3) — Contul 480 nu exista in niciun plan de conturi din corpus. iConta foloseste 480 ca CONT (core/ in 2 locuri: control_incrucisat.py:399 COD_CONT_D112, salarii_contare.py:5), dar simbolul nu apare in niciun plan de conturi din corpus (OMFP 1802/2014, OMFP 3103/2017; 655 simboluri c…
- **R-CONT-739** (C3) — Contul 739 nu exista in niciun plan de conturi din corpus. iConta foloseste 739 ca CONT (core/ in 1 locuri: ong.py:22 CONT_VENIT), dar simbolul nu apare in niciun plan de conturi din corpus (OMFP 1802/2014, OMFP 3103/2017; 655 simboluri citite). De clarificat de iConta: alt nome…
- **R-TEMEI-1** (C2) — Temei structurat (`Temei(...)`) pentru constantele nesursate. Pentru 21 constante fara temei, FiscalOS propune un TEMEI CANDIDAT din act normativ (temeiuri_candidate.json). E o propunere de aprobat uman, nu o verificare.
- **R-SURSA-tva_redusa_9@2016-01-01** (C2) — Temei declarat pe o sursa care nu e act normativ: cote/tva_redusa_9@2016-01-01. CONCORDA pe o sursa care NU e act normativ (nota redactata de iConta (PROVENIENTA: SCRIS - nota proprie despre forma initiala a CF art. 291 la 01.01.2016, cu sursa si observatiile c), nu act normativ). Decizia C2: un tem…
- **R-SURSA-tva_redusa_5@2016-01-01** (C2) — Temei declarat pe o sursa care nu e act normativ: cote/tva_redusa_5@2016-01-01. CONCORDA pe o sursa care NU e act normativ (nota redactata de iConta (PROVENIENTA: SCRIS - nota proprie despre forma initiala a CF art. 291 la 01.01.2016, cu sursa si observatiile c), nu act normativ). Decizia C2: un tem…
- **R-SURSA-tichet_masa_plafon@2025-04-01** (C2) — Temei declarat pe o sursa care nu e act normativ: cote/tichet_masa_plafon@2025-04-01. CONCORDA pe o sursa care NU e act normativ (pliant sau ghid ANAF - material de informare, nu act normativ). Decizia C2: un temei se ia numai din act normativ. Rezultatul initial (CONCORDA) se pastreaza in `clasificare_in…
- **R-SURSA-tichet_masa_plafon@2025-01-01** (C2) — Temei declarat pe o sursa care nu e act normativ: cote/tichet_masa_plafon@2025-01-01. CONCORDA pe o sursa care NU e act normativ (pliant sau ghid ANAF - material de informare, nu act normativ). Decizia C2: un temei se ia numai din act normativ. Rezultatul initial (CONCORDA) se pastreaza in `clasificare_in…

## 11. Dovada în cealaltă direcție — bancul de mutații, pe fiecare clasă

C7: cel puțin o mutație pe fiecare clasă, care trebuie să iasă DIFERĂ sau NEGĂSIT cu motivul corect. Injectate pe o **copie în memorie** a inventarului — niciodată în iConta.

**Rezultat: 9 din 9 trec.**

| Clasă       | Mutație                                                 | Cod → injectat              | Ieșit   | Lege / motiv                              |
|-------------|---------------------------------------------------------|-----------------------------|---------|-------------------------------------------|
| cota        | dividende 10% in loc de 16%                             | 0.16 → 0.10                 | DIFERĂ  | 16                                        |
| cota        | TVA standard 19% in loc de 21%                          | 0.21 → 0.19                 | DIFERĂ  | 21                                        |
| cota        | cota micro 5% - valoare care nu exista in niciun act    | 0.01 → 0.05                 | DIFERĂ  | 1                                         |
| plafon      | salariu minim 4050 pe o data din semestrul 2 2026       | 4325 → 4050                 | DIFERĂ  | ['4.325', '949']                          |
| termen      | decontul de TVA (D300) scadent pe 20 in loc de 25       | 25 → 20                     | DIFERĂ  | 25                                        |
| nomenclator | D390 cu un tip de operaţiune inventat (X)               | L,T,A,P,S,R → L,T,A,P,S,R,X | DIFERĂ  | a/l/p/r/s/t                               |
| nomenclator | D390 fara tipul R                                       | L,T,A,P,S,R → L,T,A,P,S     | DIFERĂ  | a/l/p/r/s/t                               |
| cont        | cont TVA deductibila scris 4262 in loc de 4426          | 4426 → 4262                 | NEGĂSIT | iConta foloseste 4262 ca CONT (core/ in … |
| citare      | citare spre actul greșit (CAS 25% cu temei HG 146/2026) | 0.25 → 0.25                 | NEGĂSIT | atomii gasiti prin temeiul declarat nu p… |

La **citarea greșită** (CAS 25%, corect, dar cu temei HG 146/2026): `NEGĂSIT` cu `citare_rezolvata=False`. Nu CONCORDĂ, deși valoarea e corectă — întrebarea e și *duce proba unde spune?* Nu DIFERĂ, fiindcă actul citat nu spune altceva: nu spune nimic despre CAS.

---

## Aprobare

Propunerea e **NEAPROBATĂ**. Se aprobă în `propuneri/v2/APROBARE.md`. FiscalOS nu are cale de scriere spre iConta.
