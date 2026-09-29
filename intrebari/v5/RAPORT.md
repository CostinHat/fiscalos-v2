# FiscalOS v2 — Motorul de întrebări v5: deciziile C23–C29

Generat 29.09.2026 07:40 · ZIP: `/home/costin/ghid_incoming/fiscalos_intrebari_v5_rezultat.zip`

> **Scor INDICATIV** — setul de 50 e expus. Măsurătoarea finală va fi pe setul nou.

## Cifra principală: greșelile de fond rămase (decizia 8)

Greșeli de fond: **1**, din 3 GREȘIT ale comparatorului (lectura mea, întrebare cu întrebare, de verificat de om; lista completă mai jos). Separarea mecanică a celor 3 GREȘIT: faptul principal al cheii lipsește/e altul — 2 (Q-TVA-07, Q-CPF-09); faptul e corect, articolul diferă — 1 (Q-SAL-10).

- **Q-TVA-07** (PROCEDURA): Răspunsul dă termenul nominal (28 februarie 2026) și regula corectă (D394 se depune și fără operațiuni), dar nu aplică amânarea pentru zi nelucrătoare: 28.02.2026 cade sâmbătă, termenul efectiv e luni, 02.03.2026 (CPF art. 75 → Codul de procedură civilă). Un contabil care urmează răspunsul depune corect, dar i se spune un termen mai scurt decât cel legal; răspunsul e incomplet pe fond.

Celelalte GREȘIT, citite pe fond:

- **Q-SAL-10** — articol, nu fond: Faptele coincid cu cheia (90 de zile calendaristice, spor de minimum 75%). Citatul e verbatim din Codul muncii din instantaneul iConta, unde textul art. 122 apare atomizat sub `art281/alin7~6`: structura instantaneului Codului muncii e greșită, nu răspunsul (vezi C31).
- **Q-CPF-09** — comparator, nu fond: Răspunsul spune „Nu datorează nimic”, cu temeiul exact al cheii (CPF art. 173 alin. (2)). Comparatorul caută faptul „0 lei” și nu recunoaște „nimic” ca zero (vezi C30).

## Scorul pe fond (comparatorul reparat, C28)

| Motor | CORECT | GREȘIT | NU POT | Cost | Pași medii |
|---|---|---|---|---|---|
| **Navigare v5** | **34** | **3** | **13** | **$9.8792** | **8.3** |
| Navigare v4, comparator reparat (C28) și verificator reparat (C24) | 20 | 12 | 18 | $7.8643 | 7.5 |
| Semantic v3 | 10 | 8 | 32 | $3.2538 | — |
| Lexical (referință $0, C21; corpusul de acum, cu C26) | 3 | 13 | 34 | $0 | — |

Tokeni: {'intrare': 630, 'iesire': 200974, 'cache_scriere': 474478, 'cache_citire': 3772373}. Verificarea mecanică a respins 9 propuneri. Model de rezervă (C15): niciodată.

## Deciziile, fiecare cu efectul ei măsurat

**C23 — structura răspunsului final.** Reîncercări cerute: 10 (Q-TVA-03, Q-TVA-06, Q-TVA-09, Q-PRF-06, Q-PRF-09, Q-SAL-02, Q-SAL-03, Q-CPF-07, Q-CPF-08, Q-CTB-04). Abțineri după a doua structură invalidă: 2 (Q-TVA-06, Q-SAL-02). În v4 defectul lovise 7 întrebări.

**C24 — „răspuns gol" verificat întotdeauna.** Măsurat exact pe propunerile v4, fără niciun apel: 3 răspunsuri goale ar fi fost respinse (Q-PRF-02, Q-PRF-03, Q-CTB-08). Scorul v4 (comparatorul reparat): 20/15/15 → **20/12/18**. Probe în ambele direcții: `test_semantic.test_C24_*` (golul și „x" se resping cu și fără derogări; „Nu." și „21%" trec; abținerea fără răspuns nu e „răspuns gol").

**C25 — etichete FAPT_CAZ / VALOARE_LEGALĂ.** Respinse la verificarea calculului: Q-SAL-04.
Q-CTB-03 (respinsă în v4 pentru „valoare fiscală 100.000"): v5 **CORECT**.

**C26 — anexele.** Atomi citați din anexe: 12 (Q-CTB-04 `omfp_1802_2014#anexa/pct238/alin2`, Q-CTB-05 `omfp_1802_2014#anexa/pct54/alin3`, Q-CTB-05 `omfp_1802_2014#anexa/pct67/alin2`, Q-CTB-05 `omfp_1802_2014#anexa/pct67/alin3`, Q-CTB-06 `omfp_1802_2014#anexa/pct372/alin1`, Q-CTB-06 `omfp_1802_2014#anexa/pct372/alin2`, Q-PRF-01 `opanaf_587_2016_aprobarea_modelului_continutului_formularelor_utilizate#anexa3`, Q-PRF-01 `opanaf_587_2016_aprobarea_modelului_continutului_formularelor_utilizate#anexa3/pct5`, Q-PRF-09 `opanaf_587_2016_aprobarea_modelului_continutului_formularelor_utilizate#anexa4/pct3`, Q-TVA-04 `hg_1_2016_norme_cod_fiscal#anexa/pct103/alin2`, Q-TVA-07 `opanaf_2194_2025_d394#anexa2/pct1/lita`, Q-TVA-07 `opanaf_2194_2025_d394#anexa2/pct2`). Temeiul le numește ca atare (de ex. „OMFP 1802/2014 anexa, pct. 238 alin. (2)"). Efectul asupra propunerii: `propuneri/v6/` — aceleași clasificări (94/1/26/26), 23 de parametri cu atomul mutat la anexa lui, 2 temeiuri candidate false retrase.

**C27 — data de referință pentru faptul întrebat.** Întrebări cu mai multe date: 12.

- Q-TVA-04: datele 2025-12-31, 2026-09-28 → aleasă **2026-09-28** (CORECT)
- Q-PRF-04: datele 2025-12-31, 2026-09-28 → aleasă **2026-09-28** (CORECT)
- Q-PRF-06: datele 2024-12-31, 2026-09-28 → aleasă **2026-09-28** (NU POT)
- Q-PRF-10: datele 2025-12-31, 2026-09-28 → aleasă **2026-09-28** (NU POT)
- Q-SAL-08: datele 2026-09-30, 2026-10-07 → aleasă **2026-10-07** (CORECT)
- Q-CPF-02: datele 2026-03-25, 2026-04-24 → aleasă **2026-04-24** (CORECT)
- Q-CPF-03: datele 2025-07-25, 2026-03-10, 2026-04-03 → aleasă **2026-04-03** (NU POT)
- Q-CPF-08: datele 2024-03-31, 2026-09-28, 2001-12-31 → aleasă **2026-09-28** (NU POT)
- Q-CTB-02: datele 2025-12-31, 2024-12-31, 2026-09-28 → aleasă **2026-09-28** (CORECT)
- Q-CTB-05: datele 2026-09-28, 2024-12-31 → aleasă **2026-09-28** (CORECT)
- Q-CTB-06: datele 2026-12-31, 2026-09-28 → aleasă **2026-12-31** (CORECT)
- Q-CTB-08: datele 2025-12-31, 2026-09-28 → aleasă **2026-09-28** (CORECT)

**C28 — comparatorul, defect de clasă, scorul înainte și după:**

| Rulare | Înainte | După | Schimbări |
|---|---|---|---|
| navigare v4 | 18/17/15 | 20/15/15 | Q-TVA-08 GREȘIT→CORECT, Q-PRF-05 GREȘIT→CORECT |
| semantic v3 | 10/8/32 | 10/8/32 | — |
| semantic v2 | 11/8/31 | 11/8/31 | — |
| lexical v4 | 2/13/35 | 2/13/35 | — |

Reparațiile: sumele se compară ca numere (2.020 = 2020; 1.031,25 = 1031,25; 0,5% = 0.5%); faptul dintr-o propoziție negată a cheii („Nu 25% × … = 540,63 lei, ci …", „(nu 25 martie)") nu e faptul ei principal; paranteza de proveniență („(mod. OUG 89/2025)") nu e temei; o bucată de temei fără act („; art. 298 alin. (1)-(3)") continuă actul bucății dinainte. Nicio notă nu a devenit mai severă. Calculul se afișează pas cu pas: fiecare formulă cu valorile puse în ea, fiecare `zile(a, b)`, numerele în stilul sursei (un an nu mai iese „2.027").

**C29 — 20 de pași.** Întrebări care ating încă limita: **0** (—) — abținere, cu traseul navigării în motiv. Pași medii: 8.3. Cost: $9.8792 ($0.1976 / întrebare; v4: $7.8643 la 12 pași).

### Întrebările CALCUL

Răspunse: 7 din 12 (Q-TVA-08, Q-PRF-05, Q-PRF-07, Q-SAL-03, Q-CPF-02, Q-CTB-03, Q-CTB-07); corecte pe fond: 7 (Q-TVA-08, Q-PRF-05, Q-PRF-07, Q-SAL-03, Q-CPF-02, Q-CTB-03, Q-CTB-07).

Unelte folosite: deschide 241, cauta 95, cuprins 78.

---

## 0. CERINȚE — decizii de arhitect

### Aplicate în acest pas

| | Decizia | Cum e aplicată | Dovada |
|---|---|---|---|
| **C23** | `raspuns` obligatoriu și validat structural (nu gol, nu „x"/„-", nu conținutul altor câmpuri); la eșec o singură reîncercare, apoi abținere cu motivul scris | `navigare.valideaza_structura`: substituent/gol, marcaj de parametri scurs în orice câmp, `raspuns` care repetă alt câmp; reîncercarea primește problemele scrise; a doua = NU POT cu `tip_abtinere: C23` | `test_navigare.test_C23_*` (5), inclusiv forma exactă din v4 |
| **C24** | „răspuns gol" verificat întotdeauna; repararea unei găuri în verificator, cu dovadă în ambele direcții | `semantic.verifica`: verificarea iese din ramura C17 (b); gol = mai puțin de 2 caractere-cuvânt | `test_semantic.test_C24_*` (4): se resping „", „x", „-", „." cu și fără derogări; „Nu." și „21%" trec; abținerea nu e „gol" |
| **C25** | fiecare operand: FAPT_CAZ (din întrebare, literal) sau VALOARE_LEGALĂ (din atom) | câmpul `eticheta` în schema calculului; euristica C13 pe operanzi a fost înlocuită de etichetă | `test_navigare.test_C25_*` (3), inclusiv „valoare fiscală 100.000 lei" (Q-CTB-03 din v4) |
| **C26** | anexele, structură proprie (anexă → punct/secțiune), id-uri proprii; temeiul „anexa, pct. 238" | `atomizare.py`: nivelul `anexa`; punctul de anexă (forma portalului „238." / „- (1) …"); anexele „la norme" sub norme; titlul normelor în temei; lista anexelor și anexa citată într-un punct de intervenție nu deschid anexe; un articol care continuă numerotarea actului închide anexa | `test_c12_c17.test_C26_*` (4); `propuneri/v6/` |
| **C27** | data de referință pentru faptul întrebat, declarată în răspuns; mai multe date fără legătură clară → INCOMPLET | `navigare.date_din_intrebare` (toate datele, nu prima); modelul alege una și o motivează (`data_referinta`, `data_referinta_motiv`); verificatorul cere ca ea să fie una dintre datele întrebării și citatele să fie în vigoare la ea; data e scrisă la finalul răspunsului | `test_navigare.test_C27_*` (3) |
| **C28** | comparatorul reparat ca defect de clasă, scor înainte/după; calculul afișat pas cu pas | `comparatie.py`: sume ca numere, fapt negat, paranteza de proveniență, actul bucății anterioare; `navigare.pas_cu_pas` | `test_intrebari.test_C28_*` (4), `test_navigare.test_C28_*` (2); tabelul „înainte/după" |
| **C29** | 20 de pași; la limită abținere cu traseul | `MAX_PASI = 20`; fiecare rezultat de unealtă spune câți pași au rămas; o cerere peste limită = NU POT cu traseul în motiv | `test_navigare.test_C29_*`; secțiunea C29 |

### De decis (găsite la citirea celor 3 GREȘIT; nereparate — pasul se oprește după rulare)

**C30 — Comparatorul: zero spus în cuvinte și data în litere față de data numerică.** Q-CPF-09
(„Nu datorează nimic", temeiul exact al cheii) e notat GREȘIT pentru că faptul cheii e „0 lei". La
Q-TVA-07, „28 februarie 2026" nu se potrivește cu „28.02.2026" din cheie (comparatorul le reține în
forme diferite: zi + lună, respectiv data numerică). Ambele sunt defecte de clasă ale **scorului**, nu
ale motorului. *De decis:* se repară înainte de setul nou (ca C28, cu scorul înainte/după), sau
notarea rămâne strictă și cazurile se rejudecă de om?

**C31 — Codul muncii din instantaneu are structura stricată.** Textul art. 122 („compensare prin
ore libere plătite în următoarele 90 de zile") e atomizat sub `legea_53_2003_codul_muncii#art281/alin7~6`:
instantaneul iConta al Codului muncii include lanțuri de modificări care rup ierarhia. Faptul e corect,
temeiul e greșit (Q-SAL-10). *De decis:* Codul muncii se aduce consolidat din legislatie.just.ro, în
stratul oficial (ca C12), sau se repară atomizarea instantaneului?

**C32 — Termenul care cade în zi nelucrătoare.** Q-TVA-07 dă termenul nominal (28.02.2026, sâmbătă),
nu pe cel efectiv (02.03.2026). Regula e în lege (CPF art. 75 → Codul de procedură civilă), dar
aplicarea ei cere un calendar: ce zi a săptămânii e o dată și care sunt sărbătorile legale. Modelul
nu calculează (decizia 7), iar calculul nu are azi o funcție pentru asta. *De decis:* se adaugă în
calcul o funcție `termen_efectiv(data)` (sâmbătă/duminică + sărbătorile legale, cu lista sărbătorilor
luată dintr-un atom — Codul muncii art. 139), sau termenul efectiv rămâne în afara motorului?

**C33 — Reemiterea după C23 scrie diacriticele ca `ă`.** Toate cele 10 reîncercări C23 au fost
scurgeri reale de marcaj (niciuna falsă). Dar la reemitere, în 3 cazuri (Q-TVA-09, Q-CPF-08, Q-CTB-04),
modelul a scris diacriticele ca secvențe literale (`imobilizărilor`), iar verificatorul a respins,
corect, citatele: ca șir, nu sunt verbatim. Măsurat EXACT, fără niciun apel (`fiscalos/masoara_C33.py`:
navigarea reluată determinist din pașii salvați, aceleași propuneri cu secvențele decodate, aceeași
verificare): Q-TVA-09 și Q-CTB-04 ar trece și ar fi CORECT, Q-CPF-08 rămâne respins (C13). Scor:
**34/3/13 → 36/3/11**. *De decis:* decodarea secvențelor `\uXXXX` din intrarea uneltei (transformare
deterministă, fără schimbare de conținut) se aplică înainte de verificare, sau C23 tratează o
asemenea secvență ca defect de structură și cere reemiterea încă o dată?

---

## Operațiile, cu durata și costul măsurate

| Operație | Durată | Cost |
|---|---|---|
| Stratul de navigare v5: 50 de întrebări, 315 ture la `claude-opus-5` | 2937.7 s | $9.8792 |
| Proba de cost: 3 întrebări (Q-PRF-03, Q-PRF-04, Q-CPF-03) | 282.0 s | $0.8545 |
| Prima rulare, oprită de creditul API epuizat după 14 întrebări (răspunsuri pierdute: se salvau numai la final; de atunci rularea e reluabilă) | — | $2.6603 |
| Două apeluri de control al creditului (unul refuzat, unul de 8+5 tokeni) | — | ~$0.0002 |
| Măsurarea C33, fără apel (`masoara_C33.py`) | — | $0 |
| Re-atomizarea instantaneului (C26) | 1.6 s | $0 |
| Re-atomizarea actelor oficiale (C26) | 1.4 s | $0 |
| Potrivirea parametrilor iConta pe corpusul nou | 6.8 s | $0 |
| Bancul de mutatii (dovada inversa, 9/9) | 3.8 s | $0 |
| Propunerea v6 | 3.1 s | $0 |
| Motorul lexical, referință (index + 50 de întrebări) | 13.7 s | $0 |
| Comparații (inclusiv C28 înainte/după pe 4 rulări), măsurători, raport | 37.0 s | $0 |

## Cele 50 de întrebări

| Id | Tip | v5 | v4 | Lexical | Pași | Data | Răspunsul v5 |
|---|---|---|---|---|---|---|---|
| Q-TVA-01 | PARAMETRU | CORECT | CORECT | GREȘIT | 3 | 2026-09-28 | Cota standard de TVA este 21%, aplicabilă bazei de impozitare pentru o… |
| Q-TVA-02 | PARAMETRU | CORECT | CORECT | NU POT | 4 | 2026-09-28 | Plafonul este de 395.000 lei cifră de afaceri anuală, declarată sau re… |
| Q-TVA-03 | REGULA | CORECT | NU POT | NU POT | 4 | 2026-05-14 | Trebuie să solicite înregistrarea în scopuri de TVA cel târziu la data… |
| Q-TVA-04 | REGULA | CORECT | NU POT | NU POT | 12 | 2026-09-28 | Perioada fiscală în 2026 este trimestrul calendaristic, atât timp cât … |
| Q-TVA-05 | CAPCANA | CORECT | CORECT | NU POT | 6 | 2026-09-28 | Nu. Livrarea utilajului (activ corporal fix) nu se cuprinde în cifra d… |
| Q-TVA-06 | CAPCANA | NU POT | GREȘIT | NU POT | 6 | — | *C23: structura răspunsului final a fost invalidă de două ori…* |
| Q-TVA-07 | PROCEDURA | GREȘIT | GREȘIT | GREȘIT | 7 | 2026-01-31 | Da, declarația 394 se depune și pentru o lună fără operațiuni (se bife… |
| Q-TVA-08 | CALCUL | CORECT | CORECT | NU POT | 4 | 2026-09-28 | Dreptul de deducere este limitat la 50% din TVA aferentă achiziției. T… |
| Q-TVA-09 | CALCUL | NU POT | NU POT | NU POT | 6 | 2026-09-28 | *VERIFICAREA MECANICA a respins propunerea modelului: citatul…* |
| Q-TVA-10 | INCOMPLETA | NU POT | NU POT | NU POT | 4 | 2026-09-28 | *INCOMPLET: intrebarea nu da faptele de care depinde raspunsu…* |
| Q-PRF-01 | PARAMETRU | CORECT | NU POT | GREȘIT | 15 | 2026-09-28 | Cota este de 1% — Codul fiscal prevede o cotă unică pentru veniturile … |
| Q-PRF-02 | REGULA | CORECT | GREȘIT | NU POT | 14 | 2026-05-31 | Plafonul este echivalentul în lei a 100.000 euro. Se verifică pe baza … |
| Q-PRF-03 | CAPCANA | CORECT | GREȘIT | GREȘIT | 8 | 2026-09-28 | Declarația anuală privind impozitul pe profit (D101) pentru anul fisca… |
| Q-PRF-04 | CAPCANA | CORECT | GREȘIT | NU POT | 10 | 2026-09-28 | Societatea datorează impozit pe profit la nivelul impozitului minim pe… |
| Q-PRF-05 | CALCUL | CORECT | CORECT | NU POT | 10 | 2026-09-28 | Din veniturile trimestrului I se scad dividendele primite de la o pers… |
| Q-PRF-06 | CALCUL | NU POT | CORECT | NU POT | 6 | 2026-09-28 | *VERIFICAREA MECANICA a respins propunerea modelului: citatul…* |
| Q-PRF-07 | CALCUL | CORECT | CORECT | NU POT | 3 | 2026-09-28 | Cheltuielile de protocol sunt deductibile în limita a 2% aplicată asup… |
| Q-PRF-08 | REGULA | CORECT | CORECT | NU POT | 8 | 2026-03-10 | Condiția de a avea cel puțin un salariat trebuie îndeplinită în termen… |
| Q-PRF-09 | PROCEDURA | CORECT | GREȘIT | NU POT | 16 | 2026-09-28 | Pentru trimestrul I 2026 nu se aplică regula generală a pătrimii din i… |
| Q-PRF-10 | INCOMPLETA | NU POT | GREȘIT | NU POT | 9 | 2026-09-28 | *VERIFICAREA MECANICA a respins propunerea modelului: valoare…* |
| Q-SAL-01 | PARAMETRU | CORECT | CORECT | CORECT | 5 | 2026-09-28 | Cota contribuției asiguratorii pentru muncă (CAM) este de 2,25%, aplic… |
| Q-SAL-02 | PROCEDURA | NU POT | NU POT | NU POT | 10 | — | *C23: structura răspunsului final a fost invalidă de două ori…* |
| Q-SAL-03 | CALCUL | CORECT | NU POT | NU POT | 19 | 2026-09-30 | CAS reținut salariatului = 2.500 lei; CASS reținută = 1.000 lei; baza … |
| Q-SAL-04 | CALCUL | NU POT | NU POT | NU POT | 19 | 2026-09-30 | *VERIFICAREA CALCULULUI a respins propunerea: operand nenumer…* |
| Q-SAL-05 | CAPCANA | CORECT | NU POT | NU POT | 13 | 2026-10-31 | Nu. Tichetele de masă nu se iau în calcul la verificarea plafonului de… |
| Q-SAL-06 | CAPCANA | CORECT | GREȘIT | NU POT | 12 | 2026-09-30 | CAS datorat pentru septembrie 2026 este 1.031,25 lei (înainte de rotun… |
| Q-SAL-07 | REGULA | CORECT | CORECT | GREȘIT | 12 | 2026-09-28 | Se aplică procentul de 65% asupra bazei de calcul, întrucât certificat… |
| Q-SAL-08 | CAPCANA | CORECT | CORECT | GREȘIT | 4 | 2026-10-07 | Procentul se stabilește pe total episod de boală: zilele din certifica… |
| Q-SAL-09 | INCOMPLETA | NU POT | NU POT | NU POT | 10 | 2026-09-30 | *INCOMPLET: intrebarea nu da faptele de care depinde raspunsu…* |
| Q-SAL-10 | REGULA | GREȘIT | GREȘIT | GREȘIT | 15 | 2026-09-30 | Munca suplimentară trebuie compensată prin ore libere plătite în următ… |
| Q-CPF-01 | PARAMETRU | CORECT | CORECT | GREȘIT | 4 | 2026-09-28 | Dobânda este de 0,02% pentru fiecare zi de întârziere, iar penalitatea… |
| Q-CPF-02 | CALCUL | CORECT | NU POT | NU POT | 10 | 2026-04-24 | Se datorează dobânzi de întârziere de 0,02% pentru fiecare zi de întâr… |
| Q-CPF-03 | CALCUL | NU POT | GREȘIT | NU POT | 15 | 2026-04-03 | *VERIFICAREA MECANICA a respins propunerea modelului: cifra '…* |
| Q-CPF-04 | REGULA | CORECT | CORECT | GREȘIT | 4 | 2021-12-31 | Termenul de prescripție a dreptului organului fiscal de a stabili crea… |
| Q-CPF-05 | PARAMETRU | CORECT | CORECT | GREȘIT | 6 | 2026-09-28 | Contestația se depune în termen de 45 de zile de la data comunicării d… |
| Q-CPF-06 | PROCEDURA | CORECT | CORECT | GREȘIT | 9 | 2026-09-28 | Regula generală: cererea (decontul cu opțiune de rambursare) se soluți… |
| Q-CPF-07 | REGULA | CORECT | NU POT | GREȘIT | 7 | 2026-09-28 | Durata inspecției fiscale se stabilește de organul de inspecție în fun… |
| Q-CPF-08 | CAPCANA | NU POT | NU POT | NU POT | 8 | 2026-09-28 | *VERIFICAREA MECANICA a respins propunerea modelului: citatul…* |
| Q-CPF-09 | CAPCANA | GREȘIT | CORECT | NU POT | 5 | 2026-09-28 | Nu datorează nimic: pentru sumele datorate cu titlu de amenzi de orice… |
| Q-CPF-10 | INCOMPLETA | CORECT | CORECT | NU POT | 11 | 2026-09-28 | Depunerea cu întârziere a decontului de TVA (formularul 300) este cont… |
| Q-CTB-01 | PARAMETRU | CORECT | CORECT | CORECT | 5 | 2026-09-28 | Valoarea fiscală la data intrării în patrimoniu trebuie să fie egală s… |
| Q-CTB-02 | CAPCANA | CORECT | GREȘIT | NU POT | 6 | 2026-09-28 | Nu. Pentru mijloacele fixe cu valoare fiscală de intrare cuprinsă într… |
| Q-CTB-03 | CALCUL | CORECT | NU POT | CORECT | 4 | 2026-04-30 | Pentru primul an de utilizare, amortizarea fiscală nu poate depăși 65%… |
| Q-CTB-04 | REGULA | NU POT | GREȘIT | NU POT | 3 | 2026-03-15 | *VERIFICAREA MECANICA a respins propunerea modelului: citatul…* |
| Q-CTB-05 | PROCEDURA | CORECT | GREȘIT | NU POT | 5 | 2026-09-28 | Eroarea fiind aferentă unui exercițiu financiar precedent (2024), core… |
| Q-CTB-06 | CAPCANA | CORECT | GREȘIT | NU POT | 3 | 2026-12-31 | Nu. Pentru pierderile viitoare din exploatare estimate pentru 2027 nu … |
| Q-CTB-07 | CALCUL | CORECT | CORECT | GREȘIT | 5 | 2026-04-10 | Cota de impozit pe dividende este 16%, deci se reține un impozit de 8.… |
| Q-CTB-08 | CAPCANA | CORECT | GREȘIT | NU POT | 4 | 2026-09-28 | Nu. Pentru dividendele distribuite în baza situațiilor financiare inte… |
| Q-CTB-09 | CALCUL | NU POT | NU POT | NU POT | 19 | 2026-09-28 | *VERIFICAREA MECANICA a respins propunerea modelului: valoare…* |
| Q-CTB-10 | REGULA | NU POT | CORECT | NU POT | 7 | 2026-09-28 | *VERIFICAREA MECANICA a respins propunerea modelului: C17: at…* |
