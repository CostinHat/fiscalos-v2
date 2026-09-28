# FiscalOS v2 — Motorul de întrebări v4: navigare structurală și calcul evaluat de cod

Generat 28.09.2026 20:30 · ZIP: `/home/costin/ghid_incoming/fiscalos_intrebari_v4_rezultat.zip`

> **Scor INDICATIV** — setul de 50 e expus. Măsurătoarea finală va fi pe setul nou.

## Scorul pe fond

| Motor | CORECT | GREȘIT | NU POT | Cost / rulare | Pași medii |
|---|---|---|---|---|---|
| **Stratul de navigare v4** | **18** | **17** | **15** | **$7.8643** | **7.5** |
| Stratul semantic v3 (context dat de căutare) | 10 | 8 | 32 | $3.2538 | — |
| Motorul lexical (referință $0, C21; corpusul de acum, cu V2) | 2 | 13 | 35 | $0 | — |

Tokeni stratul de navigare: {'intrare': 536, 'iesire': 156803, 'cache_scriere': 412332, 'cache_citire': 2728920}. Verificarea mecanică a respins 8 propuneri (1 la verificarea calculului: Q-CTB-03). Model de rezervă folosit (C15): niciodată. Întrebări oprite la limita de 12 pași: 9 (Q-PRF-01, Q-PRF-05, Q-PRF-09, Q-SAL-03, Q-SAL-04, Q-CPF-03, Q-CPF-08, Q-CTB-02, Q-CTB-09).

## Raportate separat (decizia 8)

### 1. Abțineri de regăsire eliminate

Abțineri v3 al căror motiv spune că atomii primiți nu conțin regula (esec de regăsire, nu de judecată): **29**. În v4 au devenit răspunsuri: **20** — pe fond: Q-TVA-05 CORECT, Q-TVA-06 GREȘIT, Q-TVA-07 GREȘIT, Q-TVA-08 GREȘIT, Q-PRF-04 GREȘIT, Q-PRF-05 GREȘIT, Q-PRF-06 CORECT, Q-PRF-07 CORECT, Q-PRF-10 GREȘIT, Q-SAL-06 GREȘIT, Q-SAL-07 CORECT, Q-CPF-01 CORECT, Q-CPF-05 CORECT, Q-CPF-06 CORECT, Q-CPF-10 CORECT, Q-CTB-02 GREȘIT, Q-CTB-04 GREȘIT, Q-CTB-05 GREȘIT, Q-CTB-07 CORECT, Q-CTB-10 CORECT. Au rămas abțineri: 9 (Q-TVA-04, Q-TVA-09, Q-TVA-10, Q-PRF-01, Q-SAL-03, Q-SAL-04, Q-CPF-02, Q-CPF-08, Q-CTB-09).

### 2. Întrebările CALCUL

12 întrebări CALCUL. Răspunse: **6** (Q-TVA-08, Q-PRF-05, Q-PRF-06, Q-PRF-07, Q-CPF-03, Q-CTB-07), din care cu calcul evaluat de cod: 6; corecte pe fond: **3** (Q-PRF-06, Q-PRF-07, Q-CTB-07). În v3: 2 răspunse, 0 corecte.

- **Q-TVA-08** (GREȘIT): Poate deduce doar 50% din TVA aferentă achiziției, adică 10.500 lei (TVA facturată de 21.000 lei la cota standard de 21%). [calcul: tva_facturata = baza * cota / 100 = 21.000; tva_deductibila = tva_facturata * procent_limitare / 100 = 10.500]
- **Q-PRF-05** (GREȘIT): Baza impozabilă a T1 2026 este 202.000 lei (200.000 lei venituri din vânzări + 2.000 lei reduceri comerciale primite din contul 609; dividendele de la SRL română și veniturile din diferențe de curs valutar nu se includ în T1), iar impozitul datorat este 2.020 …
- **Q-PRF-06** (CORECT): Pierderea din 2024 se recuperează în limita a 70% din profitul impozabil, adică 84.000 lei; profitul impozabil rămas este 36.000 lei, iar impozitul pe profit datorat, la cota de 16%, este 5.760 lei. Pierderea rămasă de recuperat (în cadrul celor 5 ani consecut…
- **Q-PRF-07** (CORECT): Cheltuielile de protocol sunt deductibile în limita de 2% aplicată asupra bazei formate din profitul contabil + cheltuiala cu impozitul pe profit + cheltuielile de protocol, adică 2.600 lei deductibili, iar restul de 7.400 lei se adaugă ca cheltuială nededucti…
- **Q-CPF-03** (GREȘIT): Datorează dobânzi de 0,02% pentru fiecare zi de întârziere și penalitate de nedeclarare de 0,08% pentru fiecare zi, ambele calculate de la ziua imediat următoare scadenței inițiale până la data stingerii sumei, inclusiv; penalitatea de întârziere de 0,01% NU s…
- **Q-CTB-07** (CORECT): Se reține impozit pe dividende de 8.000 lei (cotă 16%, impozit final), asociatul primește net 42.000 lei, iar impozitul se virează integral la bugetul de stat până la data de 25 inclusiv a lunii următoare celei în care se face plata. [calcul: impozit = baza * …

### 3. Erori noi

GREȘIT în v4 care nu erau GREȘIT în v3: **13**:

- **Q-TVA-06** (CAPCANA; v3: NU POT): motorul — Nu. Declarația recapitulativă 390 se depune lunar, până la data de 25 inclusiv a lunii următoare lunii calendaristice în care a intervenit operațiunea, indiferent de faptul că perioada fiscală pentru … · cheia — Nu. D390 se depune lunar, pentru luna în care a luat naștere exigibilitatea, nu trimestrial cu D300. Exigibilitatea la livrarea intracomunitară = data facturii sau, dacă factura nu s-a emis până atunc…
- **Q-TVA-07** (PROCEDURA; v3: NU POT): motorul — Da, declarația 394 trebuie depusă și pentru perioada în care nu au fost realizate operațiuni de natura celor care fac obiectul declarației, la organul fiscal competent până în data de 25 inclusiv a lu… · cheia — Da, se depune și fără operațiuni. Termen nominal 28.02.2026, care cade sâmbătă → termen efectiv luni, 02.03.2026.
- **Q-TVA-08** (CALCUL; v3: NU POT): motorul — Poate deduce doar 50% din TVA aferentă achiziției, adică 10.500 lei (TVA facturată de 21.000 lei la cota standard de 21%). [calcul: tva_facturata = baza * cota / 100 = 21.000; tva_deductibila = tva_fa… · cheia — 10.500 lei (TVA 21.000 lei × 50%)
- **Q-PRF-02** (REGULA; v3: CORECT): motorul — - · cheia — Plafon 100.000 euro; curs valabil la închiderea exercițiului financiar precedent (31.12.2025); impozit pe profit începând cu trimestrul în care s-a depășit limita, adică trimestrul II 2026 (calculat p…
- **Q-PRF-03** (CAPCANA; v3: CORECT): motorul — x [calcul: anul_urmator = anul_fiscal + 1 = 2.027] · cheia — 25 iunie 2027 inclusiv (nu 25 martie). Notă: validatorul DUKIntegrator testat la 03.08.2026 încă cere martie pentru an 2026 — termenul legal e totuși iunie
- **Q-PRF-04** (CAPCANA; v3: NU POT): motorul — Impozitul minim pe cifra de afaceri este 2.700.000 lei, mai mare decât impozitul pe profit calculat, deci societatea datorează pentru 2026 impozit pe profit la nivelul impozitului minim: 2.700.000 lei… · cheia — 1.350.000 lei — IMCA = 0,5% × (300.000.000 − 20.000.000 − 0 − 10.000.000) = 1.350.000 > 1.000.000, deci plătește la nivelul IMCA (nu 1%, care ar da 2.700.000)
- **Q-PRF-05** (CALCUL; v3: NU POT): motorul — Baza impozabilă a T1 2026 este 202.000 lei (200.000 lei venituri din vânzări + 2.000 lei reduceri comerciale primite din contul 609; dividendele de la SRL română și veniturile din diferențe de curs va… · cheia — 2.020 lei (bază 202.000 = 235.000 − 30.000 dividende − 5.000 dif. curs + 2.000 cont 609; × 1%)
- **Q-PRF-10** (INCOMPLETA; v3: NU POT): motorul — Da, din perspectiva plafonului și a salariatului: pentru 2026 limita veniturilor este echivalentul în lei a 100.000 euro, verificată pe baza veniturilor de la 31 decembrie 2025, iar 90.000 euro se înc… · cheia — Depinde — trebuie clarificat: (1) dacă există întreprinderi legate (deținere/control >25% direct sau indirect, inclusiv asociat >25% cu PFA/II/IF), ale căror cifre de afaceri se cumulează la plafonul …
- **Q-SAL-06** (CAPCANA; v3: NU POT): motorul — CAS datorat (înainte de rotunjire) = 1.031,25 lei, întrucât CAS calculat asupra salariului brut este sub nivelul minim aferent salariului minim brut diminuat. [calcul: baza_minima = salariu_minim - di… · cheia — Nu 25% × 2.162,50 = 540,63 lei, ci minimul: 25% × (4.325 − 200) = 1.031,25 lei; diferența de 490,63 lei o suportă angajatorul în numele salariatului (analog CASS: minim 10% × 4.125 = 412,50 lei)
- **Q-CTB-02** (CAPCANA; v3: NU POT): motorul — Nu. Condiția de valoare (limita stabilită prin hotărâre a Guvernului) se apreciază la data intrării în patrimoniu, așa că echipamentul rămâne mijloc fix amortizabil, iar valoarea rămasă neamortizată s… · cheia — Nu. Valoarea fiscală rămasă neamortizată a mijloacelor fixe cu valoare de intrare între 2.500 și 5.000 lei existente la 31.12.2025 se recuperează în continuare pe durata normală de utilizare rămasă.
- **Q-CTB-04** (REGULA; v3: NU POT): motorul — Amortizarea contabilă se calculează începând cu luna următoare punerii în funcțiune, deci din aprilie 2026. · cheia — Din aprilie 2026 (luna următoare punerii în funcțiune), până la recuperarea integrală a valorii.
- **Q-CTB-05** (PROCEDURA; v3: NU POT): motorul — Fiind o eroare aferentă unui exercițiu financiar precedent (2024), corectarea se face pe seama rezultatului reportat, în contul 1174 „Rezultatul reportat provenit din corectarea erorilor contabile" (o… · cheia — DEPINDE dacă eroarea e semnificativă și de politica contabilă aprobată — trebuie clarificat. Semnificativă: pe rezultatul reportat, cont 1174. Nesemnificativă: tot pe 1174, sau pe contul de profit și …
- **Q-CTB-08** (CAPCANA; v3: CORECT): motorul —  · cheia — Nu. Pentru dividendele distribuite pe baza situațiilor interimare din 2025 cota rămâne 10%, fără recalculare după regularizare. (Cota se stabilește după data distribuirii, nu a plății sau a aprobării …

GREȘIT în v3 care nu mai sunt GREȘIT în v4: 4 (Q-TVA-03→NU POT, Q-SAL-08→CORECT, Q-CPF-09→CORECT, Q-CTB-03→NU POT). Răspunsuri v3 retrase în v4: 4 (Q-TVA-03 (v3 GREȘIT), Q-SAL-05 (v3 CORECT), Q-CPF-07 (v3 CORECT), Q-CTB-03 (v3 GREȘIT)).

### 4. Costul și pașii de navigare

Cost: **$7.8643** pentru 50 de întrebări ($0.1573 / întrebare; v3: $3.2538). Pași de navigare: **7.5** în medie pe întrebare (limita 12). Unelte folosite: deschide 205, cauta 102, cuprins 68.

### Efectul V2 (C22), măsurat în această rulare

Răspunsuri care citează o notă tranzitorie citată în consolidat în loc de articol: v3 — 2 (Q-TVA-03 `cod_fiscal_227_2015_consolidat#artIII~2/alin6~2`, Q-TVA-03 `cod_fiscal_227_2015_consolidat#artIII~2/alin6~2`); v4 — 0 (—). Q-TVA-03 (cazul care a descoperit V2): v3 GREȘIT, v4 **NU POT**.

### Cele 17 GREȘIT ale stratului de navigare — de citit

- **Q-TVA-06** (CAPCANA): motorul — Nu. Declarația recapitulativă 390 se depune lunar, până la data de 25 inclusiv a lunii următoare lunii calendaristice în care a intervenit operațiunea, indifere… · cheia — Nu. D390 se depune lunar, pentru luna în care a luat naștere exigibilitatea, nu trimestrial cu D300. Exigibilitatea la livrarea intracomunitară = data facturii …
- **Q-TVA-07** (PROCEDURA): motorul — Da, declarația 394 trebuie depusă și pentru perioada în care nu au fost realizate operațiuni de natura celor care fac obiectul declarației, la organul fiscal co… · cheia — Da, se depune și fără operațiuni. Termen nominal 28.02.2026, care cade sâmbătă → termen efectiv luni, 02.03.2026.
- **Q-TVA-08** (CALCUL): motorul — Poate deduce doar 50% din TVA aferentă achiziției, adică 10.500 lei (TVA facturată de 21.000 lei la cota standard de 21%). [calcul: tva_facturata = baza * cota … · cheia — 10.500 lei (TVA 21.000 lei × 50%)
- **Q-PRF-02** (REGULA): motorul — - · cheia — Plafon 100.000 euro; curs valabil la închiderea exercițiului financiar precedent (31.12.2025); impozit pe profit începând cu trimestrul în care s-a depășit limi…
- **Q-PRF-03** (CAPCANA): motorul — x [calcul: anul_urmator = anul_fiscal + 1 = 2.027] · cheia — 25 iunie 2027 inclusiv (nu 25 martie). Notă: validatorul DUKIntegrator testat la 03.08.2026 încă cere martie pentru an 2026 — termenul legal e totuși iunie
- **Q-PRF-04** (CAPCANA): motorul — Impozitul minim pe cifra de afaceri este 2.700.000 lei, mai mare decât impozitul pe profit calculat, deci societatea datorează pentru 2026 impozit pe profit la … · cheia — 1.350.000 lei — IMCA = 0,5% × (300.000.000 − 20.000.000 − 0 − 10.000.000) = 1.350.000 > 1.000.000, deci plătește la nivelul IMCA (nu 1%, care ar da 2.700.000)
- **Q-PRF-05** (CALCUL): motorul — Baza impozabilă a T1 2026 este 202.000 lei (200.000 lei venituri din vânzări + 2.000 lei reduceri comerciale primite din contul 609; dividendele de la SRL român… · cheia — 2.020 lei (bază 202.000 = 235.000 − 30.000 dividende − 5.000 dif. curs + 2.000 cont 609; × 1%)
- **Q-PRF-09** (PROCEDURA): motorul — Pentru trimestrul I 2026, plata anticipată NU se stabilește ca o pătrime din impozitul anului precedent, ci prin aplicarea cotei de impozit asupra profitului co… · cheia — 16% × profitul contabil al trimestrului I 2026 (NU 1/4 din impozitul anului precedent actualizat cu IPC); D100, cod obligație 103; termen nominal 25.04.2026 (sâ…
- **Q-PRF-10** (INCOMPLETA): motorul — Da, din perspectiva plafonului și a salariatului: pentru 2026 limita veniturilor este echivalentul în lei a 100.000 euro, verificată pe baza veniturilor de la 3… · cheia — Depinde — trebuie clarificat: (1) dacă există întreprinderi legate (deținere/control >25% direct sau indirect, inclusiv asociat >25% cu PFA/II/IF), ale căror ci…
- **Q-SAL-06** (CAPCANA): motorul — CAS datorat (înainte de rotunjire) = 1.031,25 lei, întrucât CAS calculat asupra salariului brut este sub nivelul minim aferent salariului minim brut diminuat. [… · cheia — Nu 25% × 2.162,50 = 540,63 lei, ci minimul: 25% × (4.325 − 200) = 1.031,25 lei; diferența de 490,63 lei o suportă angajatorul în numele salariatului (analog CAS…
- **Q-SAL-10** (REGULA): motorul — Orele suplimentare prestate în septembrie 2026 se compensează prin ore libere plătite în următoarele 90 de zile calendaristice după efectuarea lor; dacă această… · cheia — Ore libere plătite în următoarele 90 de zile calendaristice; altfel se plătesc cu spor negociat de minim 75% din salariul de bază (în luna următoare)
- **Q-CPF-03** (CALCUL): motorul — Datorează dobânzi de 0,02% pentru fiecare zi de întârziere și penalitate de nedeclarare de 0,08% pentru fiecare zi, ambele calculate de la ziua imediat următoar… · cheia — 252 zile (26.07.2025–03.04.2026 inclusiv). Penalitate de nedeclarare 20.000 × 0,08% × 252 = 4.032 lei, redusă cu 75% (plată până la 05.04.2026, termenul art. 15…
- **Q-CTB-02** (CAPCANA): motorul — Nu. Condiția de valoare (limita stabilită prin hotărâre a Guvernului) se apreciază la data intrării în patrimoniu, așa că echipamentul rămâne mijloc fix amortiz… · cheia — Nu. Valoarea fiscală rămasă neamortizată a mijloacelor fixe cu valoare de intrare între 2.500 și 5.000 lei existente la 31.12.2025 se recuperează în continuare …
- **Q-CTB-04** (REGULA): motorul — Amortizarea contabilă se calculează începând cu luna următoare punerii în funcțiune, deci din aprilie 2026. · cheia — Din aprilie 2026 (luna următoare punerii în funcțiune), până la recuperarea integrală a valorii.
- **Q-CTB-05** (PROCEDURA): motorul — Fiind o eroare aferentă unui exercițiu financiar precedent (2024), corectarea se face pe seama rezultatului reportat, în contul 1174 „Rezultatul reportat proven… · cheia — DEPINDE dacă eroarea e semnificativă și de politica contabilă aprobată — trebuie clarificat. Semnificativă: pe rezultatul reportat, cont 1174. Nesemnificativă: …
- **Q-CTB-06** (CAPCANA): motorul — Nu. Nu se recunosc provizioane pentru pierderile viitoare din exploatare, deoarece acestea nu corespund definiției unei datorii și nu îndeplinesc criteriile de … · cheia — Nu. Nu se recunosc provizioane pentru pierderi viitoare din exploatare (nu corespund definiției unei datorii); activele de exploatare se testează pentru depreci…
- **Q-CTB-08** (CAPCANA): motorul —  · cheia — Nu. Pentru dividendele distribuite pe baza situațiilor interimare din 2025 cota rămâne 10%, fără recalculare după regularizare. (Cota se stabilește după data di…

Fapt corect, articol diferit (C2): Q-TVA-08, Q-PRF-05, Q-PRF-10, Q-SAL-10, Q-CTB-04, Q-CTB-05, Q-CTB-06.
Abțineri pe INCOMPLETA (C1): Q-TVA-10 — incompletitudine detectată; Q-SAL-09 — incompletitudine detectată.

---

## 0. CERINȚE — decizii de arhitect

### Aplicate în acest pas

| | Decizia | Cum e aplicată |
|---|---|---|
| **C18** | candidatul, la nivelul cel mai fin neambiguu; mai multe litere cu valoarea → articolul, cu literele ca opțiuni | `potrivire.potriveste`: strămoșul comun + `optiuni`; `propuneri/v5/temeiuri_candidate.json` (`ambiguu`, `optiuni`) |
| **C19** | anexele din instantaneu, textul ordinului din sursa oficială, fiecare parte cu data ei | `potrivire.COMPUSE`: OPANAF 3769/2015 = atomii oficiali ai ordinului + 91 de atomi ANEXA din instantaneu, fiecare cu `parte` și `data_formei` |
| **C20** | abținerea în plus e acceptată; datele de expirare nu se caută acum | neschimbat: plasa (b) rămâne pe dispozițiile tranzitorii citate |
| **C21** | motorul lexical păstrează plasa și rămâne doar referință de $0 | rulat o dată pe corpusul de acum, fără nicio optimizare |
| **C22** | V2 reparat acum, efectul măsurat în rularea de la punctul 8 | `surse_oficiale._aplatizeaza_note` (nota ⟦NOTĂ⟧ lipită de alineatul-gazdă) + `nota_tranzitorie` pe articolele romane din codurile arabe (281, 0 în CF); efectul — în secțiunea „Efectul V2" |
| **6** | stratul semantic trece la navigare structurală, cu pași limitați; căutarea lexicală doar punct de intrare; verificarea mecanică neschimbată | `fiscalos/navigare.py`: unelte `cauta` / `cuprins` / `deschide` (structură + relații de derogare/modificare în ambele sensuri) / `raspunde`; limită 12 pași; modelul poate cita numai atomi arătați de unelte; `semantic.verifica` neschimbat |
| **7** | modelul nu calculează: formulă + operanzi cu sursă literală; codul evaluează; operand fără sursă → respins | `navigare.evalueaza_calcule`: numai `+ - * /`, `min`, `max`, `zile(a,b)`; fiecare operand — valoare literală în fragment, fragment verbatim în atom arătat sau în întrebare; C13: o valoare legală nu vine din întrebare; constantele permise fără sursă: 1 și 100; 14 probe adversariale în `test_navigare.py` |

### Defecte de clasă găsite după comparație — NEREPARATE (pasul se oprește după rulare, decizia 8)

Scorul de mai sus e cel măsurat, fără nicio reparație. Citirea celor 17 GREȘIT, întrebare cu
întrebare (lectura mea, de verificat): **6 sunt greșeli de fond ale răspunsului** (Q-PRF-04 cota 1%
în loc de 0,5%; Q-TVA-06 și Q-TVA-07 fără data concretă și amânarea de weekend; Q-PRF-09 fără cota de
16%; Q-PRF-10 răspunde „Da" la o întrebare INCOMPLETA; Q-CTB-02 concluzie corectă pe alt temei), iar
**11 vin din defectele de mai jos**, nu din răspunsul pe fond.

**C23 — Parametrii scurși în apelul final (N1).** La 7 din 50 de întrebări (Q-TVA-03, Q-PRF-02,
Q-PRF-03, Q-CPF-01, Q-CPF-07, Q-CTB-03, Q-CTB-08), modelul a scris în câmpul `declaratie` al uneltei
`raspunde` textul celorlalte câmpuri, cu marcaj de parametri (`</declaratie><parameter
name="raspuns">…`), iar `raspuns` a rămas `"x"`, `"-"`, `""` sau `"."`. În 5 dintre ele textul scurs
conține faptul din cheie; 3 au ieșit GREȘIT (răspuns gol), 2 NU POT („nicio citare"). *De decis:*
răspunsul final trece pe ieșire structurată (`output_config.format`, ca în v3 — acolo defectul nu a
apărut în 100 de apeluri), într-o tură finală fără unelte; sau se păstrează unealta și orice marcaj
`<parameter` într-un câmp respinge propunerea și cere reemiterea (o tură în plus, cost).

**C24 — Gaură în verificator: răspunsul gol trecea (N2).** Verificarea „răspuns gol" din
`semantic.verifica` stătea în ramura C17 (b), deci rula numai când contextul avea derogări. 3
răspunsuri cu `raspuns` = `"x"` / `"-"` / `""` au trecut ca RĂSPUNS (cu atomi citați verbatim, dar
fără conținut). Nu a afectat v2/v3 (ieșirea structurată nu a produs niciodată un răspuns gol).
*Recomandare:* reparat necondiționat, cu probă adversarială. Cere autorizare, fiindcă atinge
verificatorul „neschimbat" din decizia 6.

**C25 — C13 pe operanzii din întrebare, prea larg (N3).** „valoare fiscală 100.000 lei" din
întrebare a fost tratat ca valoare legală (cuvântul „valoare" din euristica C13), iar Q-CTB-03 —
corect în v3, 65.000 lei — a fost respins. *De decis:* pentru operanzii din întrebare, valoare
legală = procent sau termen (zile/luni/ani); o sumă în lei/euro din întrebare e fapt al cazului.

**C26 — Anexele actelor oficiale, atomizate sub ultimul articol (N4).** Reglementările contabile
din OMFP 1802/2014 (pct. 67, 238, 372…), anexele OPANAF 3769/2015 și 705/2020 ajung, în forma
oficială, copii ale ultimului articol: temeiul iese „OMFP 1802/2014 art. 12 alin. (2)" în loc de
„pct. 238 alin. (2)". Faptul e corect, articolul greșit: Q-CTB-04, Q-CTB-05, Q-CTB-06 (și același
defect de structură la Codul muncii din instantaneu, Q-SAL-10: `art281/alin7~6`). *De decis:* nivel
`anexa → punct` în atomizarea oficială (afectează și potrivirea din propunere, deci v6).

**C27 — Data de referință a unei întrebări cu doi ani (N7).** Q-PRF-04 („cifra de afaceri 2025 …
cât impozit datorează pentru 2026?") a primit data 31.12.2025, deci R-VALAB a ascuns CF art. 18^1
alin. (16) („Pentru anul fiscal 2026 … cota … este 0,5%", valabil din 01.01.2026) — de aici 1% în
loc de 0,5%. La fel Q-CTB-08. *De decis:* când întrebarea numește mai mulți ani, data de referință e
cea a perioadei *despre care se întreabă* („pentru 2026", „datorează"), nu cea mai veche.

**C28 — Comparatorul (numai scor, nu motor) (N6).** Q-TVA-08 (10.500 lei, corect) și Q-PRF-05
(2.020 lei, corect) sunt GREȘIT pentru articol: cheia „art. 51 alin. (1) (mod. OUG 89/2025)" e citită
ca articol al OUG-ului, iar „; art. 298 alin. (1)-(3)" pierde actul. Q-SAL-06 (1.031,25 lei, corect)
e GREȘIT fiindcă primul fapt al cheii ales e „25%". Q-CPF-03 (1.008 / 4.032 / 1.008 lei, corecte) e
GREȘIT fiindcă „252 zile" e calculat în formulă, dar valoarea intermediară `zile(...)` nu e afișată
(defect de prezentare al calculului, N5; tot N5: un an calculat, 2027, e afișat „2.027", Q-PRF-03). *De decis:* comparatorul se repară înainte de setul nou
(altfel scorul final e subestimat), iar calculul afișează fiecare sub-expresie.

**C29 — Costul navigării.** $7,86 pentru 50 de întrebări ($0,157 / întrebare), de 2,4× costul v3
($3,25); 9 întrebări s-au oprit la limita de 12 pași. *De decis:* limita rămâne 12, sau crește
(mai puține abțineri de regăsire, cost mai mare)?

---

## Operațiile, cu durata și costul măsurate

| Operație | Durată | Cost |
|---|---|---|
| Stratul de navigare: 50 de întrebări, 268 ture la `claude-opus-5` | 2418.7 s | $7.8643 |
| Proba de cost înainte de rulare: 3 întrebări (Q-TVA-08, Q-PRF-01, Q-SAL-03) | 233.9 s | $0.7048 |
| Motorul lexical, referință (index + 50 de întrebări) | 12.7 s | $0 |
| Comparații, măsurători, raport | 9.2 s | $0 |

## Cele 50 de întrebări

| Id | Tip | Navigare v4 | Semantic v3 | Lexical | Pași | Răspunsul v4 |
|---|---|---|---|---|---|---|
| Q-TVA-01 | PARAMETRU | CORECT | CORECT | GREȘIT | 3 | Cota standard de TVA este 21%. |
| Q-TVA-02 | PARAMETRU | CORECT | CORECT | NU POT | 4 | Plafonul este de 395.000 lei cifră de afaceri anuală, declarată sau re… |
| Q-TVA-03 | REGULA | NU POT | GREȘIT | NU POT | 4 | *VERIFICAREA MECANICA a respins propunerea modelului: nicio c…* |
| Q-TVA-04 | REGULA | NU POT | NU POT | NU POT | 11 | *VERIFICAREA MECANICA a respins propunerea modelului: C17: at…* |
| Q-TVA-05 | CAPCANA | CORECT | NU POT | NU POT | 6 | Nu. Livrarea utilajului (activ fix corporal) nu se cuprinde în cifra d… |
| Q-TVA-06 | CAPCANA | GREȘIT | NU POT | NU POT | 4 | Nu. Declarația recapitulativă 390 se depune lunar, până la data de 25 … |
| Q-TVA-07 | PROCEDURA | GREȘIT | NU POT | GREȘIT | 7 | Da, declarația 394 trebuie depusă și pentru perioada în care nu au fos… |
| Q-TVA-08 | CALCUL | GREȘIT | NU POT | NU POT | 5 | Poate deduce doar 50% din TVA aferentă achiziției, adică 10.500 lei (T… |
| Q-TVA-09 | CALCUL | NU POT | NU POT | NU POT | 6 | *VERIFICAREA MECANICA a respins propunerea modelului: valoare…* |
| Q-TVA-10 | INCOMPLETA | NU POT | NU POT | NU POT | 5 | *INCOMPLET: intrebarea nu da faptele de care depinde raspunsu…* |
| Q-PRF-01 | PARAMETRU | NU POT | NU POT | GREȘIT | 12 | *modelul s-a abţinut: Am regăsit în atomi doar prima parte a …* |
| Q-PRF-02 | REGULA | GREȘIT | CORECT | NU POT | 11 | - |
| Q-PRF-03 | CAPCANA | GREȘIT | CORECT | GREȘIT | 8 | x [calcul: anul_urmator = anul_fiscal + 1 = 2.027] |
| Q-PRF-04 | CAPCANA | GREȘIT | NU POT | NU POT | 8 | Impozitul minim pe cifra de afaceri este 2.700.000 lei, mai mare decât… |
| Q-PRF-05 | CALCUL | GREȘIT | NU POT | NU POT | 12 | Baza impozabilă a T1 2026 este 202.000 lei (200.000 lei venituri din v… |
| Q-PRF-06 | CALCUL | CORECT | NU POT | NU POT | 5 | Pierderea din 2024 se recuperează în limita a 70% din profitul impozab… |
| Q-PRF-07 | CALCUL | CORECT | NU POT | NU POT | 3 | Cheltuielile de protocol sunt deductibile în limita de 2% aplicată asu… |
| Q-PRF-08 | REGULA | CORECT | CORECT | NU POT | 8 | Condiția de a avea cel puțin un salariat trebuie îndeplinită în termen… |
| Q-PRF-09 | PROCEDURA | GREȘIT | GREȘIT | NU POT | 12 | Pentru trimestrul I 2026, plata anticipată NU se stabilește ca o pătri… |
| Q-PRF-10 | INCOMPLETA | GREȘIT | NU POT | NU POT | 11 | Da, din perspectiva plafonului și a salariatului: pentru 2026 limita v… |
| Q-SAL-01 | PARAMETRU | CORECT | CORECT | CORECT | 6 | Cota este de 2,25%, aplicată asupra bazei de calcul, și este suportată… |
| Q-SAL-02 | PROCEDURA | NU POT | NU POT | NU POT | 9 | *VERIFICAREA MECANICA a respins propunerea modelului: cifra '…* |
| Q-SAL-03 | CALCUL | NU POT | NU POT | NU POT | 12 | *modelul s-a abţinut: Răspunsul cerut presupune atât cote leg…* |
| Q-SAL-04 | CALCUL | NU POT | NU POT | NU POT | 12 | *modelul s-a abţinut: Atomii găsiți conțin facilitatea (scuti…* |
| Q-SAL-05 | CAPCANA | NU POT | CORECT | NU POT | 11 | *modelul s-a abţinut: Singura normă găsită în corpus care reg…* |
| Q-SAL-06 | CAPCANA | GREȘIT | NU POT | NU POT | 11 | CAS datorat (înainte de rotunjire) = 1.031,25 lei, întrucât CAS calcul… |
| Q-SAL-07 | REGULA | CORECT | NU POT | GREȘIT | 6 | Indemnizația se calculează prin aplicarea procentului de 65% asupra ba… |
| Q-SAL-08 | CAPCANA | CORECT | GREȘIT | GREȘIT | 7 | Se cumulează zilele din tot episodul de boală (10 zile), deci se aplic… |
| Q-SAL-09 | INCOMPLETA | NU POT | NU POT | NU POT | 10 | *INCOMPLET: intrebarea nu da faptele de care depinde raspunsu…* |
| Q-SAL-10 | REGULA | GREȘIT | GREȘIT | GREȘIT | 7 | Orele suplimentare prestate în septembrie 2026 se compensează prin ore… |
| Q-CPF-01 | PARAMETRU | CORECT | NU POT | GREȘIT | 5 | Dobânda este de 0,02% pentru fiecare zi de întârziere, iar penalitatea… |
| Q-CPF-02 | CALCUL | NU POT | NU POT | NU POT | 10 | *VERIFICAREA MECANICA a respins propunerea modelului: cifra '…* |
| Q-CPF-03 | CALCUL | GREȘIT | GREȘIT | NU POT | 12 | Datorează dobânzi de 0,02% pentru fiecare zi de întârziere și penalita… |
| Q-CPF-04 | REGULA | CORECT | NU POT | GREȘIT | 5 | Termenul de prescripție a dreptului organului fiscal de a stabili crea… |
| Q-CPF-05 | PARAMETRU | CORECT | NU POT | GREȘIT | 7 | Contestația se depune în termen de 45 de zile de la data comunicării d… |
| Q-CPF-06 | PROCEDURA | CORECT | NU POT | GREȘIT | 8 | Termenul general este de 45 de zile de la înregistrarea cererii. Dacă,… |
| Q-CPF-07 | REGULA | NU POT | CORECT | GREȘIT | 7 | *VERIFICAREA MECANICA a respins propunerea modelului: nicio c…* |
| Q-CPF-08 | CAPCANA | NU POT | NU POT | NU POT | 12 | *VERIFICAREA MECANICA a respins propunerea modelului: valoare…* |
| Q-CPF-09 | CAPCANA | CORECT | GREȘIT | NU POT | 5 | Nu datorează nimic: pentru sumele cu titlu de amenzi de orice fel nu s… |
| Q-CPF-10 | INCOMPLETA | CORECT | NU POT | NU POT | 11 | Amendă contravențională pentru nedepunerea la termen a declarației: de… |
| Q-CTB-01 | PARAMETRU | CORECT | CORECT | CORECT | 6 | O imobilizare corporală este mijloc fix amortizabil dacă, la data intr… |
| Q-CTB-02 | CAPCANA | GREȘIT | NU POT | NU POT | 12 | Nu. Condiția de valoare (limita stabilită prin hotărâre a Guvernului) … |
| Q-CTB-03 | CALCUL | NU POT | GREȘIT | NU POT | 4 | *VERIFICAREA CALCULULUI a respins propunerea: operandul valoa…* |
| Q-CTB-04 | REGULA | GREȘIT | NU POT | NU POT | 3 | Amortizarea contabilă se calculează începând cu luna următoare punerii… |
| Q-CTB-05 | PROCEDURA | GREȘIT | NU POT | NU POT | 6 | Fiind o eroare aferentă unui exercițiu financiar precedent (2024), cor… |
| Q-CTB-06 | CAPCANA | GREȘIT | GREȘIT | NU POT | 3 | Nu. Nu se recunosc provizioane pentru pierderile viitoare din exploata… |
| Q-CTB-07 | CALCUL | CORECT | NU POT | GREȘIT | 3 | Se reține impozit pe dividende de 8.000 lei (cotă 16%, impozit final),… |
| Q-CTB-08 | CAPCANA | GREȘIT | CORECT | NU POT | 3 |  |
| Q-CTB-09 | CALCUL | NU POT | NU POT | NU POT | 12 | *modelul s-a abţinut: Regula de bază este identificată: la un…* |
| Q-CTB-10 | REGULA | CORECT | NU POT | NU POT | 5 | Poate plăti în numerar cel mult 5.000 lei (plafonul zilnic pe persoană… |
