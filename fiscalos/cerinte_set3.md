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
