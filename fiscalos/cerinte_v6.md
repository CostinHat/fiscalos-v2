## 0. CERINȚE — decizii de arhitect

### Aplicate în acest pas

| | Decizia | Cum e aplicată | Dovada |
|---|---|---|---|
| **C30** | comparatorul reparat ca defect de clasă (zero în cuvinte, date în litere), scor înainte/după, fără apel | `comparatie._fapte_raspuns` (zero), alias numeric pentru data în litere cu an, normalizarea datelor numerice; `compara(…, corp)` pe corpusul rulării | `test_intrebari.test_C30_*`; tabelul C30 |
| **C31** | Codul muncii din sursa oficială; detector mecanic pe tot corpusul; actele stricate găsite, aduse tot din sursa oficială | `detector_structura.py` (S1–S4); `surse_oficiale_c31.py` (rezolvare în portal, aducere incrementală — actele deja aduse nu se ating); 47 de acte aduse; variantele stricate, scoase din index; 3 defecte de conversie a portalului reparate | `test_c12_c17.test_C31_*` (6); `propuneri/v7/` |
| **C32** | `termen_efectiv(data)`; regula și sărbătorile din atomi citați; Paști/Rusalii calculate, cu calculul declarat | `navigare.Calendar` + `termen_efectiv`, `data(z, l, a)`, data + N zile | `test_navigare.test_C32_*` (6) |
| **C33** | decodarea `\uXXXX` se aplică; probă în ambele direcții; scor înainte/după fără apel | `navigare.decodeaza_transport`, înainte de validarea C23 | `test_navigare.test_C33_*` (2); 34/3/13 → 36/3/11 |

### De decis

**C34 — Sărbătorile numite în lege fără dată.** Codul muncii art. 139 alin. (1) numește „Adormirea
Maicii Domnului” și „prima și a doua zi de Crăciun”, dar nu le scrie data. `termen_efectiv` le dă data
fixă a sărbătorii (15.08; 25–26.12) și o **declară** în răspuns ca atare („sărbători numite în atom
fără dată, cu data lor fixă”), la fel cum declară calculul Paștelui. *De decis:* se acceptă așa, sau
aceste două sărbători rămân în afara calculului (iar un termen care atinge 15.08 sau 25–26.12 iese
INCOMPLET)?

**C35 — Codul de procedură civilă adus în corpus.** CPF art. 75 trimite calculul termenelor fiscale la
Codul de procedură civilă, care nu era în instantaneu. L-am adus din legislatie.just.ro (ca la C12), ca
regula prelungirii (art. 181 alin. (2)) să vină dintr-un atom. *De confirmat:* rămâne în corpus?

**C36 — Defecte reziduale ale conversiei oficiale.** După reparații, detectorul mai semnalează 8 acte
oficiale: Codul civil (13 alineate duplicate, din 2.455), Legea 31/1990, Legea 129/2019, Legea 265/2022,
Legea 30/2019, OUG 89/2025 (alineate duplicate), și OG 13/2011, OUG 70/2024 — acte de bază arabe care
modifică alte legi, unde articolele citate apar ca articole proprii. *De decis:* se repară acum (a doua
clasă cere recunoașterea articolului citat într-un act de bază, nu doar într-un modificator), sau după
măsurătoarea pe setul nou?

**C37 — Ordinul 1099/2016, nerezolvat.** Portalul are trei ordine nr. 1099/2016 (29.03, 23.06, 12.07);
numele din instantaneu nu spune emitentul. Nu l-am ghicit. *De decis:* care e?
