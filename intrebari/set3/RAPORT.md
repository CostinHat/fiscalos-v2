# FiscalOS v2 — Măsurătoarea pe setul 3

Generat 29.09.2026 21:27 · ZIP: `/home/costin/ghid_incoming/fiscalos_masuratoare_set3.zip`

Versiunea motorului: **b6a2d04** (C40–C48), neschimbată; bucla de reluare (3d2c48b) e un script separat. Răspunsurile comise (**024fab8**) înainte de orice citire a cheii. Comparatorul neschimbat. Nicio reparație după comparație.

## Cifra principală: greșelile de fond

**1** din 50 (din 19 răspunsuri date):

- **Q3-TVA-09** (CAPCANA) — *procentul împărțit de două ori la 100*. Concluzia e corectă (terenul construibil nu e scutit, livrarea e taxabilă cu 21%, pe temeiul cheii — CF art. 292 alin. (2) lit. f) pct. 1, art. 291 alin. (1)), dar suma e greșită: formula modelului `baza * cota / 100`, cu operandul `cota` = „21%” (deja 0,21), împarte a doua oară la 100 — TVA 1.050 lei în loc de 105.000 lei. Codul a evaluat corect o formulă greșită; verificarea nu are o regulă pentru asta.

## Scorul pe fond (cifra oficială)

| | CORECT | GREȘIT | NU POT | Greșeli de fond |
|---|---|---|---|---|
| **Setul 3, b6a2d04 (C40–C48)** | **18** | **1** | **31** | **1** |
| Setul 2, 485ffc3 (oficial) | 28 | 7 | 15 | 2 |

Pe tipuri (setul 3):

| Tip | CORECT | GREȘIT | NU POT |
|---|---|---|---|
| PARAMETRU | 4 | 0 | 6 |
| REGULA | 3 | 0 | 7 |
| CALCUL | 5 | 0 | 5 |
| CAPCANA | 3 | 1 | 6 |
| PROCEDURA | 2 | 0 | 3 |
| INCOMPLETA | 1 | 0 | 4 |

## C47 — abținerile din C40 și C41, citite pe fond

Abțineri venite din **C41: 12** (din care una și C40); din **C40: 1** (Q3-PRF-09, împreună cu C41). Fiecare propunere respinsă, trecută prin comparator *ca și cum* ar fi fost acceptată (numai citire, scorul nu se schimbă — `intrebari/set3/ipotetic_fara_C40_C41.json`) și citită:

| Id | Regula | Citirea | De ce |
|---|---|---|---|
| Q3-TVA-01 | C41 | **ar fi fost CORECT** | plafonul 5.000.000 lei; modelul a justificat lit. a) față de lit. b) (perioada), dar nu și geamenii din alte articole arătați de `deschide` (art. 319, 324, 297, OUG 8/2026) |
| Q3-TVA-05 | C41 | **ar fi fost CORECT** | termenul (ultimul decont) prin termen_efectiv; justificare dată pentru art. 310/315^1, dar nu în forma cerută pentru geamănul art. 315^1 alin. (16) |
| Q3-PRF-02 | C41 | **ar fi fost CORECT** | cota de 4%; geamenii nejustificați sunt art. 26 și art. 41 (text de procedură comun) |
| Q3-PRF-04 | C41 | **ar fi fost CORECT** | venit neimpozabil; art. 23 are 11 geameni arătați (definiții cu text comun), justificat unul |
| Q3-PRF-09 | C40 + C41 | **ar fi fost CORECT** | termenul T4: modelul a scris „25 decembrie 2026 … zi nelucrătoare” și a mutat singur termenul, fără termen_efectiv (C40); plus trei geameni nejustificați |
| Q3-SAL-02 | C41 | **ar fi fost CORECT** | 85% / 126 de zile; geamănul din Normele OMS 15/2018 justificat pentru alt atom citat decât cel verificat |
| Q3-SAL-07 | C41 | **C41 a prevenit o greșeală de fond** | modelul a luat salariul minim de 4.325 lei (HG 146/2026 art. 2, de la 01.07.2026) în loc de 4.050 lei, în vigoare la 01.01.2026 (art. 1): CASS 5.190 lei în loc de 4.860. Geamănul nejustificat era exact perechea art. 1 / art. 2 |
| Q3-SAL-08 | C41 | **ar fi fost CORECT** | impozitul de 780 lei; geamenii art. 138/156/147 (cotele CAS/CASS) și art. 68/76/142 |
| Q3-CPF-03 | C41 | **corect pe fond, notat GREȘIT de comparator** | „un an de la 10.02.2026” fără data 10.02.2027 — faptul cheii; C40 nu-l prinde (nu e dată în context de termen) |
| Q3-CTB-01 | C41 | **ar fi fost CORECT** | 500 lei; geamănul e textul Legii 31/1990 reprodus de modificare (legea_31_1990_modif_L239_2025) |
| Q3-CTB-03 | C41 | **ar fi fost CORECT** | evenimentul ulterior care conduce la ajustare; geamănul OMFP 3103/2017 (reglementările pentru alte entități) justificat pentru alt atom citat |
| Q3-CTB-09 | C41 | **corect pe fond, alt temei decât cheia** | leasing financiar, amortizarea la utilizator — concluzia cheii, pe CF art. 29 în loc de OMFP 1802/2014 pct. 213-214 |

**Bilanț C40/C41 pe setul 3:** 12 abțineri; **9 ar fi fost răspunsuri CORECTE**, 1 a prevenit o greșeală de fond (Q3-SAL-07), 2 ar fi fost corecte pe fond dar nu pe notarea strictă (Q3-CPF-03, Q3-CTB-09).

**De ce pierde C41 răspunsuri corecte:** modelul completează `alegeri_temei`, dar pentru perechile pe care le consideră relevante (lit. a) față de lit. b), perioada); verificatorul cere justificare pentru **fiecare** geamăn văzut — iar `deschide` arată acum, în medie, geamenii fiecărui atom deschis, inclusiv texte de procedură sau definiții comune din alte articole (art. 23 CF: 11 geameni). Singurul geamăn care conta cu adevărat (Q3-SAL-07: HG 146/2026 art. 1 / art. 2) a fost prins — celelalte 9 nu schimbau răspunsul.

## Celelalte abțineri, pe cauze

| Cauza | Câte |
|---|---|
| C40/C41 | 12 |
| C46 (cifră nici citată, nici calculată) | 5 |
| verificarea calculului (forma operandului / formula) | 4 |
| C13 (valoare legală nedovedită din atom) | 4 |
| INCOMPLET (detectat de model, pe întrebări INCOMPLETA) | 3 |
| C17 (derogare netratată) | 2 |
| citat ne-verbatim | 1 |

## Cheile

Niciuna nu pare greșită. Q3-TVA-09 (105.000 lei = 500.000 × 21%) și Q3-SAL-07 (salariul minim în vigoare la 01.01.2026 = 4.050 lei, HG 146/2026 art. 1) sunt confirmate de atomi.

## Costul pe întrebare, față de setul 2

| | Cost / întrebare | Pași de navigare | Ture | Cost total |
|---|---|---|---|---|
| **Setul 3 (b6a2d04)** | **$0.310** | 10.0 | 7.9 | $15.52 |
| Setul 2 (485ffc3) | $0.175 | 6.9 | 5.8 | $8.76 |

Creșterea (+77%) vine din: tura finală separată (C44, +1 tură), geamenii arătați de `deschide` (C41 — mai mult text de citit în fiecare pas) și mai mulți pași de navigare (10,0 față de 6,9).

---

## 0. CERINȚE

### Aplicate în măsurătoare

| | Decizia | Cum |
|---|---|---|
| **C47** | respingerea C40/C41 neschimbată pe setul 3; decizia pe cifre | neschimbată; cifrele în secțiunea C47 |
| **C48** | C43 rămâne regulă de prompt | neschimbat |
| **Regulile măsurătorii** | orbire, versiune fixă, răspunsuri comise înainte de comparație, comparator neschimbat, nicio reparație după | proba `test_setul_3_se_incarca_orb`; `024fab8` înaintea citirii cheii; motorul = b6a2d04 |
| **Bucla de reluare** | numai la 429/529, cu așteptare crescătoare; oprire la orice eroare definitivă | `fiscalos/rulare_cu_reluare.py` (script separat) |

### De decis (defecte găsite, NEREPARATE — setul 3 nu se folosește pentru reglaje)

**C49 — C41 cere prea mult (clasa: domeniul justificării).** 12 abțineri; 9 ar fi fost răspunsuri corecte,
1 a prevenit o greșeală de fond (Q3-SAL-07). Cauza: verificatorul cere justificare pentru fiecare geamăn
văzut, iar `deschide` arată geamenii tuturor atomilor deschiși — inclusiv texte de procedură și definiții
comune. *Variante de decis:* (a) justificarea se cere numai pentru geamenii atomului care poartă **valoarea
sau concluzia** din răspuns (atomul citat decisiv), nu pentru orice atom citat; (b) numai pentru geamenii
din **același act**, cu **valori diferite** (cazul Q3-SAL-07: HG 146/2026 art. 1 = 4.050, art. 2 = 4.325;
cazul Q2-TVA-05: CF 319/320 — aceeași valoare, alt subiect, deci (b) nu l-ar prinde); (c) C41 devine
avertisment în raport, nu abținere. Cifrele setului 3: sub (a) sau (c), 9 răspunsuri corecte în plus.

**C50 — Procentul împărțit de două ori (clasa: semantica operandului procent).** Q3-TVA-09: operandul
„21%” e deja 0,21; formula `baza * cota / 100` dă 1.050 în loc de 105.000. *Cerință:* verificatorul
respinge o formulă care împarte la 100 un operand scris cu „%” (sau îl înmulțește cu 100), cu motivul
scris; promptul spune explicit că un operand „21%” valorează 0,21.

**C51 — Forma operandului și constantele (clasa: C25/C45).** 4 respingeri la calcul: operanzi „15-a”
(numeral ordinal), „60 de zile” (cifră + unitate), constante 24 și 6 în formulă (numărul de salarii minime
din lege, scris în formulă în loc de operand). Direcția e sigură (abținere), dar CALCUL a rămas la 5/10 răspunse.
*De decis:* ordinalele și „cifră + unitate” ca forme literale acceptate (valoarea = cifra), cu conversia
declarată, ca la C45.

**C52 — C46 și C13 (clasa: cifre scrise direct).** 5 + 4 respingeri: cifre calculate sau reformulate de
model direct în text („4.000”, „31”, „100”, „2025”) sau valori legale necitate. Corecte ca direcție;
promptul C46 nu a fost suficient. *De decis:* o a doua tură automată care îi arată modelului exact cifrele
respinse și îi cere să le pună prin calcul sau citat (o singură dată, ca C23)?

**C53 — Costul (+77% pe întrebare).** $0,310 față de $0,175 pe setul 2: tura finală separată (C44), textul
geamenilor în fiecare `deschide` (C41) și mai mulți pași (10,0 față de 6,9). *De decis împreună cu C49:*
dacă geamenii se arată numai pentru atomul decisiv, scad și costul, și abținerile.

---

## Operațiile, cu durata și costul măsurate

| Operație | Durată | Cost |
|---|---|---|
| Setul 3: 50 de întrebări (din care 47 în rularea finală, 3 salvate anterior) | 3679 s | $15.5245 |
| Întrebările întrerupte de erori (529 × 2, credit × 1) — nesalvate | — | nemăsurabil |
| Apeluri de control (3 × 8+5 tokeni) | — | ~$0,0006 |
| Reîncercări refuzate (credit insuficient, 14 + 1) | — | $0 |
| Comparația, citirea, raportul | — | $0 |
