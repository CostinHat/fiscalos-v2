# FiscalOS v2 — PROPUNERE v1: parametrii fiscali ai iConta confruntați cu corpusul

Generat 28.09.2026 16:13 · **NEAPROBAT** · nu se aplică automat în iConta (CLAUDE.md §3).

| | |
|---|---|
| **CONCORDĂ** | **200** |
| **DIFERĂ** | **0** |
| **NEGĂSIT** | **31** |
| Total parametri inventariați | 231 |
| Citări declarate de iConta / rezolvate în corpus | 40 / 40 |
| Atomi în corpus | 46.559 din 269 acte |

---

## 0. CERINȚE — decizii de arhitect

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

---

## 1. Operațiile rulate, cu durata măsurată

| Operație                               | Durată | Rezultat                                                                                    |
|----------------------------------------|--------|---------------------------------------------------------------------------------------------|
| OP2 instantaneu corpus + manifest SHA  | 0.49 s | {"n_fisiere": 726, "octeti_total": 130006698}                                               |
| OP3 strat de text (txt/html/pdf)       | 2.13 s | {"n_acte_cu_text": 269, "n_neextractibile": 4}                                              |
| OP4 atomizare structurala              | 2.15 s | {"n_acte": 269, "n_atomi": 46559, "n_acte_pe_articole": 201, "n_acte_pe_fragmente": 68}     |
| OP5 inventar parametri iConta (citire) | 1.81 s | {"n_parametri": 231, "pe_clasa": {"cota": 38, "plafon": 38, "termen": 5, "nomenclator": 4,… |
| OP6+OP7 potrivire si clasificare       | 9.59 s | {"n_parametri": 231, "sumar": {"CONCORDA": 200, "NEGASIT": 31}, "citari_declarate": 40, "c… |
| OP7b banc de mutatii (dovada inversa)  | 3.88 s | {"n_trec": 5, "n_pica": 0}                                                                  |
| Probe pe corpus                        | 4.19 s | {"cod_ieșire": 0}                                                                           |

Total măsurat: **24.24 s**. Duratele sunt citite din `artefacte/durate.json`, scris de `ruleaza_tot.py` — nu sunt estimări.

## 2. Corpusul

Instantaneu copiat din `/home/costin/iconta_nou/anaf_surse`, **doar citire**, la 2026-09-28T16:12:51: **726 fișiere, 130.0 MB**. Manifest SHA256 per fișier în `corpus_manifest.json`.

Toate cele 277 de amprente `.sha256` pe care ANAF/iConta le-au pus lângă acte confirmă hash-urile calculate aici — zero divergențe. Copierea e dovedită de două ori, nu presupusă.

**Garanția de citire (CLAUDE.md §1).** `_refuza_scrierea` respinge mecanic orice cale sub `~/iconta_nou`, inclusiv prin legătură simbolică, iar inventarul nu importă niciodată cod iConta — citește sursa și o trece prin `ast.parse`, tocmai ca să nu poată scrie bytecode în arborele lor. Cele trei fișiere citite (`core/common.py`, `core/scadente.py`, `core/nomenclatoare.py`) sunt neatinse, și un eșantion de 25 de fișiere din corpus dă încă hash-urile din manifest. Ambele sunt verificate de `fiscalos/test_read_only.py`.

Ce **nu** se poate afirma este că nimic nu s-a schimbat în `~/iconta_nou`: serviciul iConta rulează (systemd `iconta-nou`, activ) și își scrie singur jurnalele. În timpul generării a apărut acolo și un `.pyc` nou — un cache de **pytest**, pentru un modul pe care nu l-am deschis niciodată; `pytest` nu există în interpretorul folosit aici, ci doar în `iconta_nou/venv`. Nu e al nostru, și se scrie aici ca să nu fie citit greșit mai târziu.

Atomizare: **46.559 atomi**, 201 acte pe structură de articol, 68 pe fragmente (acte fără articole: pliante ANAF, structuri de formular).

**Neextractibile (4)** — limită a uneltei, nu absență din lege:

- `D112_XML_2026_0726_050826` — formular XFA: pdftotext a scos numai placeholderul Acrobat, nu corpul formularului (676 caractere)
- `D311_XML_2021_290121` — formular XFA: pdftotext a scos numai placeholderul Acrobat, nu corpul formularului (676 caractere)
- `d402_surse_sha256` — fisier .txt aproape gol (176 caractere)
- `pdf_original/structura_D301` — pdftotext a intors 0 caractere - probabil formular XFA sau scan fara OCR

## 3. Rezultatul, pe clase de parametri

| Clasă       | CONCORDĂ | DIFERĂ | NEGĂSIT |
|-------------|----------|--------|---------|
| cont        | 135      | 0      | 11      |
| cota        | 30       | 0      | 8       |
| nomenclator | 2        | 0      | 2       |
| plafon      | 28       | 0      | 10      |
| termen      | 5        | 0      | 0       |

### CONCORDĂ nu e un singur lucru — ancora contează

| Fel de ancoră | Câți | Ce înseamnă |
|---|---|---|
| **Temei declarat de iConta, verificat în actul declarat** | 177 | Citarea lor duce la actul corect, iar atomul de acolo poartă valoarea. Verdict verificat. |
| **Ancoră slabă** | 23 | Parametri pe care iConta **nu-i sursează deloc**. Tot ce s-a putut face e o căutare pe cuvinte în corpus, cu cerința ca valoarea să stea lângă fraza-subiect. E **probă de confirmat de arhitect**, nu verdict verificat — vezi C2. |

Cei cu ancoră slabă, fiecare cu atomul lui, ca să poată fi confirmați sau respinși unul câte unul:

| Parametru                                      | Cod      | Atom din corpus                                                                 | În lege    |
|------------------------------------------------|----------|---------------------------------------------------------------------------------|------------|
| nesursat/bacsis.COTA_IMPOZIT=10                | 10       | cod_fiscal_227_2015_consolidat#art64/alin1                                      | 10%        |
| nesursat/casa.PLAFON_INCASARE_PJ=5000          | 5000     | oug_115_2023_consolidat#artLXIV                                                 | 5.000      |
| nesursat/casa.PLAFON_INCASARE_PJ_CC=10000      | 10000    | legea_296_2023_masuri_fiscal_bugetare_asigurarea_sustenabilitatii#art4~2/alin1  | 10.000     |
| nesursat/casa.PLAFON_PF=10000                  | 10000    | d394_struct_anaf#frag229                                                        | 10000      |
| nesursat/casa.PLAFON_PLATA_PJ=5000             | 5000     | oug_115_2023_consolidat#artLXIV                                                 | 5.000      |
| nesursat/casa.PLAFON_PLATA_PJ_TOTAL=10000      | 10000    | hg_1_2016_norme_cod_fiscal#artV~18/alin7/litc~2                                 | 10.000     |
| nesursat/casa.PLAFON_SOLD_ZI_CC=500000         | 500000   | oug_115_2023_consolidat#art31/alin2^3                                           | 500.000    |
| nesursat/cote_tva.COTA_REDUSA=11               | 11       | legea_141_2025#artII/pct42/alin2                                                | 11%        |
| nesursat/cote_tva.COTA_STANDARD=21             | 21       | cod_fiscal_227_2015_consolidat#art291/alin1                                     | 21%        |
| nesursat/d100_pozitia_116.PRAG_BRENT_USD=70    | 70       | oug_24_2026_contributie_solidaritate#art9/alin6                                 | 70         |
| nesursat/d101.COTA_STANDARD=16                 | 16       | pdf_original/structura_D101G_2025_260126#frag178                                | 16%        |
| nesursat/d101.PRAG_IMCA_EUR=50000000           | 50000000 | legea_296_2023_masuri_fiscal_bugetare_asigurarea_sustenabilitatii#art18^1/alin8 | 50.000.000 |
| nesursat/d101g.COTA_STANDARD=16                | 16       | pdf_original/structura_D101G_2025_260126#frag178                                | 16%        |
| nesursat/d216.COTA_IMPOZIT=0.3                 | 0.3      | hg_1_2016_norme_cod_fiscal#artV~19/alin1~264/litb~3                             | 30%        |
| nesursat/d394.COTE=11                          | 11       | d300_struct_anaf#frag85                                                         | 11%        |
| nesursat/d394.COTE=19                          | 19       | pdf_original/structura_D300_v12.0.0_10022026#frag336                            | 19%        |
| nesursat/d394.COTE=20                          | 20       | oug_138_2024#artIX/alin1/litb                                                   | 20%        |
| nesursat/d394.COTE=21                          | 21       | d300_struct_anaf#frag82                                                         | 21%        |
| nesursat/d394.COTE=24                          | 24       | d394_struct_anaf#frag304                                                        | 24%        |
| nesursat/d394.COTE=5                           | 5        | pdf_original/structura_D300_v12.0.0_10022026#frag366                            | 5%         |
| nesursat/d394.COTE=9                           | 9        | pdf_original/structura_D300_v12.0.0_10022026#frag514                            | 9%         |
| nesursat/salarizare.PRAG_VENIT_DEDUCERE=2000   | 2000     | cod_fiscal_227_2015_consolidat#art77/alin3                                      | 2.000      |
| nesursat/taxare_inversa.PRAG_ELECTRONICE=22500 | 22500    | cod_fiscal_227_2015_consolidat#art331/alin7                                     | 22.500     |

## 4. Registrul `COTE` al iConta — partea cu temei declarat

Acestea sunt cele 35 intrări (20 chei, cu versiunile lor în timp) pe care iConta le declară cu temei și citat. Pentru fiecare: valoarea din cod, atomul din corpus care o stabilește, fragmentul verbatim și data de intrare.

### `cote/cam@2018-01-01` — **CONCORDA**

- **cod iConta:** `0.0225` din 2018-01-01 — core/common.py:667 (registrul COTE)
- **temei declarat:** CF
- **atom din corpus:** `cod_fiscal_227_2015_consolidat#art220^3/alin1`
- **valoare în textul legii:** 2,25%
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > Cota contribuției asiguratorii pentru muncă este de 2,25%. Notă ... Reproducem mai jos prevederile art. 19 din LEGEA nr. 369 din 19 decembrie 2022, publicată în MONITORUL OFICIAL nr. 1215 din 19 decembrie 2022: Articolul 19 În anul 2023, cota contribuției pentru persoanele prevăzute la art. 20 alin. (1) din Legea nr. 76/2002 privind sistemul asigurărilor pentru șomaj și stimularea ocupării forței de muncă, cu modificările și completările ulterioare, este de 17% din contribuția asiguratorie pentru muncă prevăzută la art. 220^3 alin. (1) din Legea nr. 227/2015 privind Codul fiscal, cu modificări…

### `cote/cas@2018-01-01` — **CONCORDA**

- **cod iConta:** `0.25` din 2018-01-01 — core/common.py:658 (registrul COTE)
- **temei declarat:** CF
- **atom din corpus:** `cod_fiscal_227_2015_consolidat#art138`
- **valoare în textul legii:** 25%
- **valabil din (corpus):** 2018-01-01
- **act modificator:** Articolul 138 din Sectiunea a 2-a , Capitolul II , Titlul V a fost modificat de Punctul 42, Articolul I din ORDONANȚA DE URGENȚĂ nr. 79 din 8 noiembrie 2017, publicată în MONITORUL…
- **verbatim:**

  > Cotele de contribuții de asigurări sociale Cotele de contribuții de asigurări sociale sunt următoarele: a) 25% datorată de către persoanele fizice care au calitatea de angajați sau pentru care există obligația plății contribuției de asigurări sociale, potrivit prezentei legi; ... b) 4% datorată în cazul condițiilor deosebite de muncă, astfel cum sunt prevăzute în Legea nr. 263/2010 privind sistemul unitar de pensii publice, cu modificările și completările ulterioare, de către persoanele fizice și juridice care au calitatea de angajatori sau sunt asimilate acestora; ... c) 8% datorată în cazul …

### `cote/cass@2018-01-01` — **CONCORDA**

- **cod iConta:** `0.10` din 2018-01-01 — core/common.py:661 (registrul COTE)
- **temei declarat:** CF
- **atom din corpus:** `cod_fiscal_227_2015_consolidat#art156~2`
- **valoare în textul legii:** 10%
- **valabil din (corpus):** 2021-12-18
- **act modificator:** Articolul 156 din Sectiunea a 2-a , Capitolul III , Titlul V a fost modificat de Punctul 69, Articolul I din ORDONANȚA DE URGENȚĂ nr. 79 din 8 noiembrie 2017, publicată în MONITORU…
- **verbatim:**

  > Cota de contribuție de asigurări sociale de sănătate: Cota de contribuție de asigurări sociale de sănătate este de 10% și se datorează de către persoanele fizice care au calitatea de angajați sau pentru care există obligația plății contribuției de asigurări sociale de sănătate, potrivit prezentei legi. + Secţiunea a 3-a Baza de calcul al contribuției de asigurări sociale de sănătate datorate în cazul persoanelor care realizează venituri din salarii sau asimilate salariilor, venituri din pensii, precum și în cazul persoanelor aflate sub protecția sau în custodia statului Notă ... Prin DECIZIA C…

### `cote/facilitate_salariu_minim@2025-01-01` — **CONCORDA**

- **cod iConta:** `300` din 2025-01-01 — core/common.py:675 (registrul COTE)
- **temei declarat:** OUG 156 2024
- **atom din corpus:** `oug_156_2024#artLXVI/alin1`
- **valoare în textul legii:** 300
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > Prin derogare de la prevederile art. 78, art. 139 alin. (1), art. 140, art. 157 alin. (1) şi ale art. 2204 alin. (1) din Legea nr. 227/2015, cu modificările şi completările ulterioare, începând cu data de 1 ianuarie 2025, în cazul salariaţilor care desfăşoară activitate în baza contractului individual de muncă, încadraţi cu normă întreagă, la locul unde se află funcţia de bază, nu se datorează impozit pe venit şi nu se cuprinde în baza lunară de calcul al contribuţiilor sociale obligatorii suma de 300 lei/lună, reprezentând venituri din salarii şi asimilate salariilor, dacă sunt îndeplinite cu…

### `cote/facilitate_salariu_minim@2026-07-01` — **CONCORDA**

- **cod iConta:** `200` din 2026-07-01 — core/common.py:674 (registrul COTE)
- **temei declarat:** OUG 89 2025
- **atom din corpus:** `oug_89_2025#artIII~2/alin1`
- **valoare în textul legii:** 200
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > Prin derogare de la prevederile art. 78 , art. 139 alin. (1) , art. 140 , art. 157 alin. (1) și ale art. 220^4 alin. (1) din Legea nr. 227/2015 , cu modificările și completările ulterioare, în cazul salariaților care desfășoară activitate în baza contractului individual de muncă, încadrați cu normă întreagă, la locul unde se află funcția de bază, pentru suma de 300 lei/lună din veniturile din salarii și asimilate salariilor aferente perioadei 1 ianuarie-30 iunie 2026, respectiv pentru suma de 200 lei/lună, din veniturile din salarii și asimilate salariilor aferente perioadei 1 iulie-31 decembr…

### `cote/impozit_dividend@2016-01-01` — **CONCORDA**

- **cod iConta:** `0.05` din 2016-01-01 — core/common.py:618 (registrul COTE)
- **temei declarat:** OUG 50 2015
- **atom din corpus:** `oug_50_2015_consolidat#artI~2/pct17`
- **valoare în textul legii:** 5%
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > La articolul 133, după alineatul (7) se introduce un nou alineat, alineatul (8), cu următorul cuprins: "(8) Cota de impozit de 5% se aplică asupra veniturilor din dividende distribuite începând cu data de 1 ianuarie 2016."

### `cote/impozit_dividend@2023-01-01` — **CONCORDA**

- **cod iConta:** `0.08` din 2023-01-01 — core/common.py:617 (registrul COTE)
- **temei declarat:** OG 16 2022
- **atom din corpus:** `og_16_2022_consolidat#artI/alin4`
- **valoare în textul legii:** 8%
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > În cazul contribuabililor prevăzuți la art. 47 care devin plătitori de impozit pe profit în conformitate cu prevederile art. 52, pentru aplicarea facilității se ia în considerare profitul contabil brut cumulat de la începutul trimestrului respectiv investit în activele prevăzute la alin. (1), puse în funcțiune începând cu trimestrul în care aceștia au devenit plătitori de impozit pe profit. ... 2. La articolul 24 alineatul (1) litera a), punctul 1 se modifică și va avea următorul cuprins: 1. este constituită ca o «societate pe acțiuni», «societate în comandită pe acțiuni», «societate cu răspun…

### `cote/impozit_dividend@2025-01-01` — **CONCORDA**

- **cod iConta:** `0.10` din 2025-01-01 — core/common.py:616 (registrul COTE)
- **temei declarat:** OUG 156 2024
- **atom din corpus:** `oug_156_2024#artLXIV/pct9`
- **valoare în textul legii:** 10%
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > La articolul 97, alineatul (7) se modifică şi va avea următorul cuprins: "(7) Veniturile sub formă de dividende, inclusiv câştigul obţinut ca urmare a deţinerii de titluri de participare definite de legislaţia în materie la organisme de plasament colectiv, se impozitează cu o cotă de 10% din suma acestora, impozitul fiind final. Obligaţia calculării şi reţinerii impozitului pe veniturile sub formă de dividende revine persoanelor juridice, odată cu plata dividendelor/sumelor reprezentând câştigul obţinut ca urmare a deţinerii de titluri de participare de către acţionari/asociaţi/investitori. Te…

### `cote/impozit_dividend@2026-01-01` — **CONCORDA**

- **cod iConta:** `0.16` din 2026-01-01 — core/common.py:615 (registrul COTE)
- **temei declarat:** Legea 141 2025
- **atom din corpus:** `legea_141_2025_consolidat#artII`
- **valoare în textul legii:** 16%
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > Legea nr. 227/2015 privind Codul fiscal , publicată în Monitorul Oficial al României, Partea I, nr. 688 din 10 septembrie 2015, cu modificările și completările ulterioare, se modifică și se completează după cum urmează: 1. La articolul 43, alineatul (2) se modifică și va avea următorul cuprins: (2) Impozitul pe dividende se stabilește prin aplicarea unei cote de impozit de 16% asupra dividendului brut plătit unei persoane juridice române. Impozitul pe dividende se declară și se plătește la bugetul de stat, până la data de 25 inclusiv a lunii următoare celei în care se plătește dividendul. ... …

### `cote/impozit_micro@2023-01-01` — **CONCORDA**

- **cod iConta:** `0.01` din 2023-01-01 — core/common.py:652 (registrul COTE)
- **temei declarat:** CF
- **atom din corpus:** `cod_fiscal_227_2015_consolidat#art51/alin1`
- **valoare în textul legii:** 1%
- **valabil din (corpus):** 2026-01-01
- **act modificator:** Alineatul (1) , Articolul 51 , Titlul III a fost modificat de Punctul 4. , Articolul I din ORDONANȚA DE URGENȚĂ nr. 89 din 23 decembrie 2025, publicată în MONITORUL OFICIAL nr. 120…
- **verbatim:**

  > Cota de impozit pe veniturile microîntreprinderilor este de 1%.

### `cote/impozit_profit@2018-01-01` — **CONCORDA**

- **cod iConta:** `0.16` din 2018-01-01 — core/common.py:655 (registrul COTE)
- **temei declarat:** CF
- **atom din corpus:** `cod_fiscal_227_2015_consolidat#art17`
- **valoare în textul legii:** 16%
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > Cota de impozitare Cota de impozit pe profit care se aplică asupra profitului impozabil este de 16%. +

### `cote/impozit_venit@2018-01-01` — **CONCORDA**

- **cod iConta:** `0.10` din 2018-01-01 — core/common.py:664 (registrul COTE)
- **temei declarat:** CF
- **atom din corpus:** `cod_fiscal_227_2015_consolidat#art78/alin2`
- **valoare în textul legii:** 10%
- **valabil din (corpus):** 2026-03-01
- **act modificator:** Partea introductivă a literei a) din Alineatul (2) , Articolul 78 , Capitolul III , Titlul IV a fost modificată de Punctul 23, Articolul I din ORDONANȚA DE URGENȚĂ nr. 79 din 8 noi…
- **verbatim:**

  > Impozitul lunar prevăzut la alin. (1) se determină astfel: a) la locul unde se află funcția de bază, prin aplicarea cotei de 10% asupra bazei de calcul determinată ca diferență între venitul net din salarii calculat prin deducerea din venitul brut a contribuțiilor sociale obligatorii aferente unei luni, datorate potrivit legii în România sau în conformitate cu instrumentele juridice internaționale la care România este parte, precum și, după caz, a contribuției individuale la bugetul de stat datorată potrivit legii, și următoarele: ... (i) deducerea personală acordată pentru luna respectivă; ..…

### `cote/plafon_avans_decontare@2023-12-15` — **CONCORDA**

- **cod iConta:** `5000` din 2023-12-15 — core/common.py:647 (registrul COTE)
- **temei declarat:** OUG 115 2023
- **atom din corpus:** `oug_115_2023_consolidat#artLXIV`
- **valoare în textul legii:** 5.000
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > …publicată, cu modificările și completările ulterioare; ... e) hipermagazin - structură de vânzare, astfel cum este definit la art. 4 lit. s) din Ordonanța Guvernului nr. 99/2000, republicată , cu modificările și completările ulterioare. ... ... 2. La articolul 3 alineatul (1), litera e) se modifică și va avea următorul cuprins: e) plăți din avansuri spre decontare, în limita unui plafon zilnic de 5.000 lei, stabilit pentru fiecare persoană care a primit avansuri spre decontare. ... ... 3. La articolul 4, alineatele (1) și (4) se modifică și vor avea următorul cuprins: (1) Operațiunile de înca…

### `cote/plafon_facilitate_salariu_minim@2025-01-01` — **CONCORDA**

- **cod iConta:** `4300` din 2025-01-01 — core/common.py:680 (registrul COTE)
- **temei declarat:** OUG 156 2024
- **atom din corpus:** `oug_156_2024#artLXVI/alin1/litb`
- **valoare în textul legii:** 4.300
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > venitul brut realizat din salarii şi asimilate salariilor, astfel cum este definit la art. 76 alin. (1) - (3) din Legea nr. 227/2015, cu modificările şi completările ulterioare, fără a include contravaloarea tichetelor de masă, voucherelor de vacanţă, respectiv indemnizaţia de hrană, după caz, acordate potrivit legii, în baza aceluiaşi contract individual de muncă, pentru aceeaşi lună, nu depăşeşte nivelul de 4.300 lei inclusiv.

### `cote/plafon_facilitate_salariu_minim@2026-01-01` — **CONCORDA**

- **cod iConta:** `4300` din 2026-01-01 — core/common.py:679 (registrul COTE)
- **temei declarat:** OUG 89 2025
- **atom din corpus:** `oug_89_2025#artIII~2/alin1/litb`
- **valoare în textul legii:** 4.300
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > venitul brut realizat din salarii și asimilate salariilor, astfel cum este definit la art. 76 alin. (1 )-( 3) din Legea nr. 227/2015 , cu modificările și completările ulterioare, fără a include contravaloarea tichetelor de masă, voucherelor de vacanță, respectiv indemnizația de hrană, după caz, acordate potrivit legii, în baza aceluiași contract individual de muncă, pentru aceeași lună, nu depășește nivelul de 4.300 lei inclusiv în perioada cuprinsă între 1 ianuarie 2026-30 iunie 2026, respectiv nivelul de 4.600 lei inclusiv în perioada cuprinsă între 1 iulie 2026-31 decembrie 2026. ...

### `cote/plafon_facilitate_salariu_minim@2026-07-01` — **CONCORDA**

- **cod iConta:** `4600` din 2026-07-01 — core/common.py:678 (registrul COTE)
- **temei declarat:** OUG 89 2025
- **atom din corpus:** `oug_89_2025#artIII~2/alin1/litb`
- **valoare în textul legii:** 4.600
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > venitul brut realizat din salarii și asimilate salariilor, astfel cum este definit la art. 76 alin. (1 )-( 3) din Legea nr. 227/2015 , cu modificările și completările ulterioare, fără a include contravaloarea tichetelor de masă, voucherelor de vacanță, respectiv indemnizația de hrană, după caz, acordate potrivit legii, în baza aceluiași contract individual de muncă, pentru aceeași lună, nu depășește nivelul de 4.300 lei inclusiv în perioada cuprinsă între 1 ianuarie 2026-30 iunie 2026, respectiv nivelul de 4.600 lei inclusiv în perioada cuprinsă între 1 iulie 2026-31 decembrie 2026. ...

### `cote/plafon_intrastat@2026-01-01` — **CONCORDA**

- **cod iConta:** `1000000` din 2026-01-01 — core/common.py:641 (registrul COTE)
- **temei declarat:** Ordin 1604 2025
- **atom din corpus:** `ordin_1604_2025_intrastat_mo#frag3`
- **valoare în textul legii:** 1.000.000
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > …terioare, având în vedere Nota de prezentare și motivare nr. 97.674/2025 a direcției generale de statistică economică din cadrul Institutului Național de Statistică, președintele Institutului Național de Statistică emite următorul ordin: Art. 1. — Se aprobă următoarele praguri valorice Intrastat pentru colectarea informațiilor statistice de comerț intra-UE cu bunuri pentru anul de referință 2026: 1.000.000 lei pentru expedieri de bunuri și, respectiv, 1.000.000 lei pentru introduceri de bunuri. Art. 2. — Operatorii economici care în cursul anului 2025 au efectuat schimburi de bunuri cu statel…

### `cote/plafon_mijloc_fix@2015-01-01` — **CONCORDA**

- **cod iConta:** `2500` din 2015-01-01 — core/common.py:629 (registrul COTE)
- **temei declarat:** HG 276 2013
- **atom din corpus:** `hg_276_2013#art1~2/alin1`
- **valoare în textul legii:** 2.500
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > Începând cu data intrării în vigoare a prezentei hotărâri, valoarea minimă de intrare a mijloacelor fixe stabilită în condiţiile art. 3 alin. 2 lit. a) din Legea nr. 15/1994 privind amortizarea capitalului imobilizat în active corporale şi necorporale, republicată, cu modificările şi completările ulterioare, este de 2.500 lei. ...

### `cote/plafon_mijloc_fix@2026-01-01` — **CONCORDA**

- **cod iConta:** `5000` din 2026-01-01 — core/common.py:628 (registrul COTE)
- **temei declarat:** OUG 8 2026
- **atom din corpus:** `oug_8_2026#art20^1/alin15`
- **valoare în textul legii:** 5.000
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > …t care se încheie în anul 2026. În situația în care rezervele fiscale respective sunt menținute până la lichidare, acestea nu sunt luate în calcul pentru determinarea rezultatului fiscal al lichidării. ... 7. La articolul 28 alineatul (2), litera b) se modifică și va avea următorul cuprins: b) la data intrării în patrimoniul contribuabilului, are o valoare fiscală egală sau mai mare decât suma de 5.000 lei; această limită se actualizată anual, în funcție de indicele de inflație, prin hotărâre a Guvernului; ... ... 8. La articolul 28, după alineatul (8) se introduc trei noi alineate, alin. (8^…

### `cote/plafon_sold_casa@2015-05-09` — **CONCORDA**

- **cod iConta:** `50000` din 2015-05-09 — core/common.py:644 (registrul COTE)
- **temei declarat:** Legea 70 2015
- **atom din corpus:** `legea_70_2015_consolidat#art18`
- **valoare în textul legii:** 50.000
- **valabil din (corpus):** 2019-01-06
- **act modificator:** Art. 4^1 a fost introdus de pct. 1 al art. IV din ORDONANȚA DE URGENȚĂ nr. 32 din 28 iunie 2016, publicată în MONITORUL OFICIAL nr. 488 din 30 iunie 2016.
- **verbatim:**

  > … de plată autorizate de Banca Națională a României sau autorizate în alt stat membru al Uniunii Europene și notificate către Banca Națională a României, potrivit legii, efectuate ca urmare a transferului dreptului de proprietate asupra unor bunuri sau drepturi, a prestării de servicii, precum și cele reprezentând acordarea/restituirea de împrumuturi, se pot efectua în limita unui plafon zilnic de 50.000 lei/tranzacție. Sunt interzise încasările și plățile fragmentate în numerar pentru tranzacțiile mai mari de 50.000 lei, precum și fragmentarea unei tranzacții mai mari de 50.000 lei. + Articol…

### `cote/plafon_tva_incasare@2021-01-01` — **CONCORDA**

- **cod iConta:** `4500000` din 2021-01-01 — core/common.py:625 (registrul COTE)
- **temei declarat:** Legea 296 2020
- **atom din corpus:** `legea_296_2020_consolidat#art231/alin1`
- **valoare în textul legii:** 4.500.000
- **valabil din (corpus):** 2022-01-01
- **act modificator:** Punctul 160. din Articolul I a fost abrogat de Litera a), Alineatul (1), Articolul XLVIII din ORDONANȚA DE URGENȚĂ nr. 130 din 17 decembrie 2021, publicată în MONITORUL OFICIAL nr.…
- **verbatim:**

  > …eea ce privește ajustarea dreptului de deducere prevăzută de lege. ... 158. La articolul 282 alineatul (3), litera a) se modifică și va avea următorul cuprins: a) persoanele impozabile înregistrate în scopuri de TVA conform art. 316, care au sediul activității economice în România conform art. 266 alin. (2) lit. a), a căror cifră de afaceri în anul calendaristic precedent nu a depășit plafonul de 4.500.000 lei. Persoana impozabilă care în anul precedent nu a aplicat sistemul TVA la încasare, dar a cărei cifră de afaceri pentru anul respectiv este inferioară plafonului de 4.500.000 lei și care…

### `cote/plafon_tva_incasare@2026-03-01` — **CONCORDA**

- **cod iConta:** `5000000` din 2026-03-01 — core/common.py:624 (registrul COTE)
- **temei declarat:** OUG 8 2026
- **atom din corpus:** `oug_8_2026#art20^1/alin5^1/litg^2`
- **valoare în textul legii:** 5.000.000
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > … (3) Prin excepție de la prevederile alin. (1) și alin. (2) lit. a), exigibilitatea taxei intervine la data încasării contravalorii integrale sau parțiale a livrării de bunuri ori a prestării de servicii, în cazul persoanelor impozabile care optează în acest sens, denumite în continuare persoane care aplică sistemul TVA la încasare. Plafonul pentru aplicarea sistemului TVA la încasare este de: a) 5.000.000 lei, în perioada 1 martie-31 decembrie 2026; ...…

### `cote/plafon_tva_incasare@2027-01-01` — **CONCORDA**

- **cod iConta:** `5500000` din 2027-01-01 — core/common.py:623 (registrul COTE)
- **temei declarat:** OUG 8 2026
- **atom din corpus:** `oug_8_2026#art20^1/alin5^1/litb`
- **valoare în textul legii:** 5.500.000
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > 5.500.000 lei, începând cu data de 1 ianuarie 2027. ... ... 39. La articolul 282, după alineatul (3) se introduce un nou alineat, alin. (3^1), cu următorul cuprins: (3^1) Sunt eligibile pentru aplicarea sistemului TVA la încasare: a) persoanele impozabile înregistrate în scopuri de TVA conform art. 316, care au sediul activității economice în România conform art. 266 alin. (2) lit. a), a căror cifră de afaceri în anul calendaristic precedent nu a depășit plafonul pentru aplicarea sistemului TVA la încasare prevăzut pentru anul respectiv. Persoana impozabilă care în anul precedent nu a aplicat …

### `cote/salariu_minim@2025-01-01` — **CONCORDA**

- **cod iConta:** `4050` din 2025-01-01 — core/common.py:671 (registrul COTE)
- **temei declarat:** HG 1506 2024
- **atom din corpus:** `hg_1506_2024_salariu_minim#art1`
- **valoare în textul legii:** 4.050
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > Începând cu data de 1 ianuarie 2025, salariul de bază minim brut pe țară garantat în plată se stabilește în bani, fără a include sporuri și alte adaosuri, la suma de 4.050 lei lunar, pentru un program normal de lucru în medie de 165,334 ore pe lună, reprezentând 24,496 lei/oră. +

### `cote/salariu_minim@2026-07-01` — **CONCORDA**

- **cod iConta:** `4325` din 2026-07-01 — core/common.py:670 (registrul COTE)
- **temei declarat:** HG 146 2026
- **atom din corpus:** `hg_146_2026_salariu_minim#art1`
- **valoare în textul legii:** 4.325
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > Începând cu data de 1 iulie 2026, salariul de bază minim brut pe țară garantat în plată, prevăzut la art. 164 alin. (1) din Legea nr. 53/2003 - Codul muncii, republicată , cu modificările și completările ulterioare, se stabilește în bani, fără a include sporuri și alte adaosuri, la suma de 4.325 lei lunar, pentru un program normal de lucru în medie de 166,667 ore pe lună, reprezentând 25,949 lei/oră. +

### `cote/tichet_masa_plafon@2025-01-01` — **CONCORDA**

- **cod iConta:** `40.04` din 2025-01-01 — core/common.py:685 (registrul COTE)
- **temei declarat:** Ordin 4679 2024
- **atom din corpus:** `anaf_limite_2025#frag24`
- **valoare în textul legii:** 40,04
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > 6 prevederi nu poate depăşi suma Începând cu data de 1 OUG nr. 69/2023 pentru de 40 lei ianuarie 2024 şi pentru lunile modificarea art. 14 din Legea august şi septembrie 2024 nr. 165/2018 privind acordarea biletelor de valoare, precum şi pentru stabilirea unor măsuri pentru aplicarea acestor prevederi nu poate depăși cuantumul Semestrul II al anului 2024, Ordinul MF nr. 4.679/2024 pen- de 40,04 lei începând cu luna octombrie tru stabilirea valorii nominale 2024, și pentru primele două indexate a unui tichet de masă luni ale semestrului I al anului pentru semestrul II al anului 2025, respectiv …

### `cote/tichet_masa_plafon@2025-04-01` — **CONCORDA**

- **cod iConta:** `40.18` din 2025-04-01 — core/common.py:684 (registrul COTE)
- **temei declarat:** Ordin 484 2025
- **atom din corpus:** `anaf_limite_2025#frag24`
- **valoare în textul legii:** 40,18
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > 6 prevederi nu poate depăşi suma Începând cu data de 1 OUG nr. 69/2023 pentru de 40 lei ianuarie 2024 şi pentru lunile modificarea art. 14 din Legea august şi septembrie 2024 nr. 165/2018 privind acordarea biletelor de valoare, precum şi pentru stabilirea unor măsuri pentru aplicarea acestor prevederi nu poate depăși cuantumul Semestrul II al anului 2024, Ordinul MF nr. 4.679/2024 pen- de 40,04 lei începând cu luna octombrie tru stabilirea valorii nominale 2024, și pentru primele două indexate a unui tichet de masă luni ale semestrului I al anului pentru semestrul II al anului 2025, respectiv …

### `cote/tichet_masa_plafon@2025-11-01` — **CONCORDA**

- **cod iConta:** `45` din 2025-11-01 — core/common.py:683 (registrul COTE)
- **temei declarat:** Legea 201 2025
- **atom din corpus:** `legea_201_2025#art14`
- **valoare în textul legii:** 45
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > Valoarea nominală a unui tichet de masă nu poate depăși suma de 45 lei. ... 2. După articolul 20 se introduce un nou articol, art. 20^1, cu următorul cuprins: +
- ⚠ **notă:** valoarea NU s-a gasit la nivelul cel mai tare de proba (ancora pe articolul din Temei (legea_201_2025#artI)), ci la citatul declarat de iConta, gasit verbatim in actul declarat - citarea iConta duce la actul corect, dar nu exact la unitatea care stabileste valoarea

### `cote/tva_redusa@2025-08-01` — **CONCORDA**

- **cod iConta:** `0.11` din 2025-08-01 — core/common.py:590 (registrul COTE)
- **temei declarat:** Legea 141 2025
- **atom din corpus:** `legea_141_2025_consolidat#art291/alin2`
- **valoare în textul legii:** 11%
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > Cota redusă de 11% se aplică asupra bazei de impozitare pentru următoarele prestări de servicii și/sau livrări de bunuri: a) livrarea de medicamente de uz uman; ...

### `cote/tva_redusa_5@2016-01-01` — **CONCORDA**

- **cod iConta:** `0.05` din 2016-01-01 — core/common.py:605 (registrul COTE)
- **temei declarat:** Legea 227 2015
- **atom din corpus:** `cf_art291_2016_forma_initiala#art291/alin3/litc/pct3`
- **valoare în textul legii:** 5%
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > …epaseste suprafata de 250 m2, inclusiv amprenta la sol a locuintei, in cazul caselor de locuit individuale. In cazul imobilelor care au mai mult de doua locuinte, cota indiviza a terenului aferent fiecarei locuinte nu poate depasi suprafata de 250 m2, inclusiv amprenta la sol aferenta fiecarei locuinte. Orice persoana necasatorita sau familie poate achizitiona o singura locuinta cu cota redusa de 5%, respectiv: (i) In cazul persoanelor necasatorite, sa nu fi detinut si sa nu detina nicio locuinta in proprietate pe care au achizitionat-o cu cota de 5%; (ii) In cazul familiilor, sotul sau sotia…

### `cote/tva_redusa_5@2025-08-01` — **CONCORDA**

- **cod iConta:** `0.11` din 2025-08-01 — core/common.py:604 (registrul COTE)
- **temei declarat:** Legea 141 2025
- **atom din corpus:** `legea_141_2025_consolidat#art291/alin2`
- **valoare în textul legii:** 11%
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > Cota redusă de 11% se aplică asupra bazei de impozitare pentru următoarele prestări de servicii și/sau livrări de bunuri: a) livrarea de medicamente de uz uman; ...

### `cote/tva_redusa_9@2016-01-01` — **CONCORDA**

- **cod iConta:** `0.09` din 2016-01-01 — core/common.py:601 (registrul COTE)
- **temei declarat:** Legea 227 2015
- **atom din corpus:** `cf_art291_2016_forma_initiala#art291/alin2`
- **valoare în textul legii:** 9%
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > Cota redusa de 9% se aplica asupra bazei de impozitare pentru urmatoarele prestari de servicii si/sau livrari de bunuri:

### `cote/tva_redusa_9@2025-08-01` — **CONCORDA**

- **cod iConta:** `0.11` din 2025-08-01 — core/common.py:600 (registrul COTE)
- **temei declarat:** Legea 141 2025
- **atom din corpus:** `legea_141_2025_consolidat#art291/alin2`
- **valoare în textul legii:** 11%
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > Cota redusă de 11% se aplică asupra bazei de impozitare pentru următoarele prestări de servicii și/sau livrări de bunuri: a) livrarea de medicamente de uz uman; ...

### `cote/tva_standard@2017-01-01` — **CONCORDA**

- **cod iConta:** `0.19` din 2017-01-01 — core/common.py:587 (registrul COTE)
- **temei declarat:** Legea 227 2015
- **atom din corpus:** `cf_2015_forma_initiala#art291/alin1/litb`
- **valoare în textul legii:** 19%
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > 19% începând cu data de 1 ianuarie 2017. ...

### `cote/tva_standard@2025-08-01` — **CONCORDA**

- **cod iConta:** `0.21` din 2025-08-01 — core/common.py:586 (registrul COTE)
- **temei declarat:** Legea 141 2025
- **atom din corpus:** `legea_141_2025_consolidat#art291/alin1`
- **valoare în textul legii:** 21%
- **valabil din (corpus):** — (atomul nu poartă notă de intrare în vigoare)
- **verbatim:**

  > Cota standard se aplică asupra bazei de impozitare pentru operațiunile impozabile care nu sunt scutite de taxă sau care nu sunt supuse cotei reduse, iar nivelul acesteia este 21%.

## 5. DIFERĂ — ambele părți

**Niciun parametru nu iese DIFERĂ.**

Asta nu e o afirmație despre lume, ci una despre ce s-a putut dovedi, și are un motiv care trebuie citit: un verdict *legea spune altceva* se pronunță numai când citarea declarată de iConta duce la actul corect, iar atomul de acolo poartă un alt număr. Pentru cei 42 de parametri cu temei declarat, citarea s-a rezolvat în toate cazurile și valoarea s-a confirmat — deci registrul `COTE` al iConta e, pe corpusul acesta, corect. Pentru parametrii pe care iConta nu-i sursează deloc, o divergență nu se poate DOVEDI: ei ies NEGĂSIT, nu DIFERĂ (vezi §0, cerința C2).

## 6. NEGĂSIT — și de ce

**altul** (2):

- `nomenclator/d301.VALUTE` = `None` — core/nomenclatoare.py:143 (ANCORE_NORMA)
- `nomenclator/d390.TARI_UE` = `None` — core/nomenclatoare.py:124 (ANCORE_NORMA)

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

**potrivire prea slabă ca să susțină un verdict (fără temei declarat de iConta)** (9):

- `nesursat/beneficii_api.PLAFON_CADOU=300` = `300` — core/beneficii_api.py:22
- `nesursat/d108.IMPOZIT_ANUAL=18000` = `18000` — core/d108.py:58
- `nesursat/ong.PLAFON_EUR=15000` = `15000` — core/ong.py:23
- `nesursat/salarizare.DEDUCERE_COPIL_SCOALA=100` = `100` — core/salarizare.py:28
- `nesursat/salarizare._PCT_DEDUCERE_BAZA=0.20` = `0.20` — core/salarizare.py:23
- `nesursat/salarizare._PCT_DEDUCERE_BAZA=0.25` = `0.25` — core/salarizare.py:23
- `nesursat/salarizare._PCT_DEDUCERE_BAZA=0.30` = `0.30` — core/salarizare.py:23
- `nesursat/salarizare._PCT_DEDUCERE_BAZA=0.35` = `0.35` — core/salarizare.py:23
- `nesursat/salarizare._PCT_DEDUCERE_BAZA=0.45` = `0.45` — core/salarizare.py:23

**simbol de cont care nu apare în planul OMFP 1802/2014** (11):

- `cont/100` = `100` — core/ in 7 locuri: d398.py:121, d398.py:264, d401.py:233, d406.py:166
- `cont/102` = `102` — core/ in 4 locuri: control_incrucisat.py:1659, d100.py:212, d101.py:135, d107.py:50
- `cont/2015` = `2015` — core/ in 9 locuri: ghid_poarta.py:79, ghid_poarta.py:80, ghid_poarta.py:81, ghid_poarta.py:82
- `cont/282` = `282` — core/ in 3 locuri: common.py:623, common.py:624, scan_pereche_act_articol.py:57
- `cont/412` = `412` — core/ in 3 locuri: control_incrucisat.py:397, d112.py:630, salarii_contare.py:57
- `cont/432` = `432` — core/ in 3 locuri: control_incrucisat.py:398, d112.py:631, salarii_contare.py:58
- `cont/459` = `459` — core/ in 3 locuri: control_incrucisat.py:398, d112.py:634, salarii_contare.py:61
- `cont/480` = `480` — core/ in 3 locuri: control_incrucisat.py:399, d112.py:632, salarii_contare.py:59
- `cont/5000` = `5000` — core/ in 4 locuri: casa.py:22, casa.py:24, common.py:628, common.py:647
- `cont/731` = `731` — core/ in 3 locuri: ong.py:20, ong.py:20, plan_omfp.py:124
- `cont/733` = `733` — core/ in 3 locuri: ong.py:20, ong.py:21, plan_omfp.py:126

## 7. Termene, nomenclatoare

- **`nomenclator/d301.VALUTE`** = `` → NEGASIT · atom `—`
- **`nomenclator/d390.TARI_UE`** = `` → NEGASIT · atom `—`
- **`nomenclator/d390.TIPURI`** = `L,T,A,P,S,R` → CONCORDA · atom `opanaf_705_2020_d390#art10/alin8`
  > lit. c) şi d) din Codul fiscal. Coloana "Tipul operaţiunii": L - pentru livrări intracomunitare de bunuri către alte state membre; T - pentru livrări în cadrul unei operaţiuni triunghiulare; A - pentru achiziţii intracomunitare de bunuri, achiziţii care urmeaz…
- **`nomenclator/d394.TIPURI`** = `L,A,LS,AS,AI,V,C,N` → CONCORDA · atom `opanaf_2194_2025_d394#artIV/pct2/pct7/pct2`
  > Coloana "Tip L/A/LS/AS/AÎ/V/C/N/Î1/Î2" de la lit. C, D, E, F, G - se înscrie tipul operaţiunii efectuate, şi anume: - L - livrări de bunuri/prestări de servicii pentru care au fost emise facturi, cu excepţia facturilor simplificate; - A - achiziţii de bunuri/s…
- **`termen/d300`** = `25` → CONCORDA · atom `cod_fiscal_227_2015_consolidat#art323/alin1`
  > Persoanele înregistrate conform art. 316 trebuie să depună la organele fiscale competente, pentru fiecare perioadă fiscală, un decont de taxă, până la data de 25 inclusiv a lunii următoare celei în care se încheie perioada fiscală respectivă.
- **`termen/d301`** = `25` → CONCORDA · atom `cod_fiscal_227_2015_consolidat#art324/alin2`
  > Decontul special de taxă trebuie întocmit potrivit modelului stabilit prin ordin al președintelui A.N.A.F. și se depune până la data de 25 inclusiv a lunii următoare celei în care ia naștere exigibilitatea operațiunilor menționate la alin. (1) . Decontul speci…
- **`termen/d390`** = `25` → CONCORDA · atom `opanaf_705_2020_d390#art10/pct3/pct3/pct6/pct1/pct1`
  > 1. Declaraţia recapitulativă se depune lunar, până la data de 25 inclusiv a lunii următoare unei luni calendaristice, de către persoanele impozabile înregistrate în scopuri de TVA conform art. 316 sau 317 din Codul fiscal.
- **`termen/d394`** = `30` → CONCORDA · atom `opanaf_2194_2025_d394#artIV/pct1/pct7/pct2/pct2`
  > Declaraţia se depune la organul fiscal competent până în data de 30 inclusiv a lunii următoare încheierii perioadei de raportare, declarate pentru depunerea decontului (luna, trimestrul etc.), inclusiv dacă în această perioadă nu au fost realizate operaţiuni d…
- **`termen/d406`** = `ultima_zi_luna` → CONCORDA · atom `opanaf_1783_2021_saft_d406#art8/pct6/pct8/pct29/pct1`
  > Declaraţia informativă D406 se transmite în format electronic, data-limită de transmitere fiind: - ultima zi calendaristică a lunii următoare perioadei de raportare, respectiv luna/trimestrul calendaristic, după caz, pentru alte informaţii decât cele privind s…

## 8. Conturi — confruntate cu planul de conturi din OMFP 1802/2014

Planul citit din corpus: **583 simboluri**. Un simbol de cont nu e o valoare numerică — ce se confirmă e existența lui în nomenclator, cu denumirea din act.

| Cont | Denumire în OMFP 1802/2014                                              |
|------|-------------------------------------------------------------------------|
| 101  | 101 Capital*4)                                                          |
| 1012 | 1012 Capital subscris vărsat (P)                                        |
| 103  | 103 Alte elemente de capitaluri proprii                                 |
| 104  | 104 Prime de capital                                                    |
| 105  | 105 Rezerve din reevaluare (P)                                          |
| 1061 | 1061 Rezerve legale (P)                                                 |
| 117  | 117 Rezultatul reportat                                                 |
| 1171 | 1171 Rezultatul reportat reprezentând profitul nerepartizat sau pierde… |
| 121  | 121 Profit sau pierdere (A/P)                                           |
| 129  | 129 Repartizarea profitului (A)                                         |
| 167  | 167 Alte împrumuturi și datorii asimilate (P)                           |
| 201  | 201 Cheltuieli de constituire (A)                                       |
| 203  | 203 Cheltuieli de dezvoltare (A)                                        |
| 205  | 205 Concesiuni, brevete, licențe, mărci comerciale, drepturi și active… |
| 207  | 207 Fond comercial                                                      |
| 208  | 208 Alte imobilizări necorporale (A)                                    |
| 211  | 211 Terenuri și amenajări de terenuri (A)                               |
| 212  | 212 Construcții (A)                                                     |
| 213  | 213 Instalații tehnice și mijloace de transport                         |
| 2131 | 2131 Echipamente tehnologice (mașini, utilaje și instalații de lucru) … |
| 2133 | 2133 Mijloace de transport (A)                                          |
| 227  | 227 Active biologice productive în curs de aprovizionare (A)            |
| 2805 | 2805 Amortizarea concesiunilor, brevetelor, licențelor, mărcilor comer… |
| 2813 | 2813 Amortizarea instalațiilor și mijloacelor de transport (P)          |
| 291  | 291 Ajustări pentru deprecierea imobilizărilor corporale                |
| 301  | 301 Materii prime (A)                                                   |
| 302  | 302 Materiale consumabile                                               |
| 303  | 303 Materiale de natura obiectelor de inventar (A)                      |
| 322  | 322 Materiale consumabile în curs de aprovizionare (A)                  |
| 331  | 331 Produse în curs de execuție (A)                                     |
| 345  | 345 Produse finite (A)                                                  |
| 348  | 348 Diferențe de preț la produse (A/P)                                  |
| 371  | 371 Mărfuri (A)                                                         |
| 378  | 378 Diferențe de preț la mărfuri (A/P)                                  |
| 381  | 381 Ambalaje (A)                                                        |
| 397  | 397 Ajustări pentru deprecierea mărfurilor (P)                          |
| 401  | 401 Furnizori (P)                                                       |
| 404  | 404 Furnizori de imobilizări (P)                                        |
| 4091 | 4091 Furnizori - debitori pentru cumpărări de bunuri de natura stocuri… |
| 4092 | 4092 Furnizori - debitori pentru prestări de servicii (A)               |

(135 conturi confirmate; tabelul arată primele 40. Lista completă în `propunere.json`.)

## 9. Dovada în cealaltă direcție — detectorul poate produce DIFERĂ?

**Un *0 DIFERĂ* nu spune nimic dacă detectorul nu poate contrazice niciodată.** Un clasificator care răspunde mereu CONCORDĂ dă exact același zero și arată la fel în raport. Deci pe o **copie în memorie** a inventarului (niciodată în iConta, niciodată în `artefacte/inventar_iconta.json`) se injectează greșeli luate din istoria fiscală reală, și se cere ca fiecare să iasă DIFERĂ, cu temeiul corect alături.

**Rezultat: 5 din 5 trec.**

### dividende 10% in loc de 16%

- *de ce această greșeală:* cota reala din 2025 (OUG 156/2024), rămasa in cod dupa ce Legea 141/2025 a urcat-o la 16% de la 01.01.2026 - clasa 'cota veche rămasa in cod'
- cod real `0.16` → injectat `0.10`
- **ieșit: DIFERA** · în lege: `16` · `citare_rezolvata=True`
- atom: `legea_141_2025_consolidat#artII`

  > Legea nr. 227/2015 privind Codul fiscal , publicată în Monitorul Oficial al României, Partea I, nr. 688 din 10 septembrie 2015, cu modificările și completările ulterioare, se modifică și se completează după cum urmează: 1. La articolul 43, alineatul (2) se modifică și va avea următorul cuprins: (2) …

### TVA standard 19% in loc de 21%

- *de ce această greșeală:* cota de dinainte de 01.08.2025; exact greșeala pe care Legea 141/2025 a produs-o in orice sistem care n-a fost actualizat
- cod real `0.21` → injectat `0.19`
- **ieșit: DIFERA** · în lege: `21` · `citare_rezolvata=True`
- atom: `legea_141_2025_consolidat#art291/alin1`

  > Cota standard se aplică asupra bazei de impozitare pentru operațiunile impozabile care nu sunt scutite de taxă sau care nu sunt supuse cotei reduse, iar nivelul acesteia este 21%.

### salariu minim 4050 pe o data din semestrul 2 2026

- *de ce această greșeală:* valoarea HG 1506/2024, aplicata unei perioade guvernate de HG 146/2026 (4.325) - clasa 'plafon vechi aplicat unei perioade noi'
- cod real `4325` → injectat `4050`
- **ieșit: DIFERA** · în lege: `['4.325', '949']` · `citare_rezolvata=True`
- atom: `hg_146_2026_salariu_minim#art1`

  > Începând cu data de 1 iulie 2026, salariul de bază minim brut pe țară garantat în plată, prevăzut la art. 164 alin. (1) din Legea nr. 53/2003 - Codul muncii, republicată , cu modificările și completările ulterioare, se stabilește în bani, fără a include sporuri și alte adaosuri, la suma de 4.325 lei…

### cota micro 5% - valoare care nu exista in niciun act

- *de ce această greșeală:* nu e o cota istorica, e o valoare pur greșita; testeaza daca detectorul cere potrivirea valorii sau se mulţumeşte cu subiectul
- cod real `0.01` → injectat `0.05`
- **ieșit: DIFERA** · în lege: `1` · `citare_rezolvata=True`
- atom: `cod_fiscal_227_2015_consolidat#art51/alin1`

  > Cota de impozit pe veniturile microîntreprinderilor este de 1%.

### citare spre actul greșit (CAS 25% cu temei HG 146/2026)

- *de ce această greșeală:* valoarea din cod e CORECTA (25%), dar temeiul declarat trimite la o hotarare de salariu minim. Intrebarea nu e 'ce valoare', ci 'proba duce unde spune?'
- cod real `0.25` → injectat `0.25`
- **ieșit: NEGASIT** · în lege: `None` · `citare_rezolvata=False`
- atom: `hg_146_2026_salariu_minim#art1`

  > Începând cu data de 1 iulie 2026, salariul de bază minim brut pe țară garantat în plată, prevăzut la art. 164 alin. (1) din Legea nr. 53/2003 - Codul muncii, republicată , cu modificările și completările ulterioare, se stabilește în bani, fără a include sporuri și alte adaosuri, la suma de 4.325 lei…

**Ce iese la citarea greșită** (valoarea din cod e corectă, dar temeiul trimite la alt act): `NEGĂSIT` cu `citare_rezolvata=False`. Nu CONCORDĂ — chiar dacă valoarea *este* corectă — fiindcă întrebarea la care răspunde acest livrabil nu e doar *ce valoare*, ci **duce proba unde spune?**. Și nu DIFERĂ, fiindcă actul declarat nu spune altceva: nu spune nimic despre acest parametru.

Prima rulare a bancului a picat **5 din 5** — toate cele cinci greșeli ieșeau CONCORDĂ. Defectele găsite astfel, și reparate, sunt scrise în §0 la cerința C7.

---

## Aprobare

Această propunere e **NEAPROBATĂ**. Se aprobă completând `propuneri/v1/APROBARE.md`. FiscalOS nu are cale de scriere spre iConta; aplicarea e un pas uman, separat.
