# Q-CTB-09 — CALCUL

**Întrebarea:** PFA în sistem real, venit net anual 2026 de 60.000 lei, nepensionar, fără salariu sau alte venituri. Cât este CAS minim datorat pentru 2026 și până când se depune D212?

## Stratul de navigare v5 — NU POT RĂSPUNDE

*La data de referință 28.09.2026, presupun o persoană fizică autorizată care realizează venituri din activități independente impuse în sistem real (art. 137 alin. (1) lit. b) din Codul fiscal), cu venit net anual 2026 de 60.000 lei, care nu este pensionar, nu are venituri din salarii și nu se încadrează în cursul anului în categoria persoanelor exceptate de la plata CAS, alegând baza minimă de calcul.*

Datele din întrebare: 2026-09-28 · data de referință aleasă: **2026-09-28** — Faptul întrebat este CAS datorat pentru veniturile anului 2026; singura dată purtată de întrebare este cea din anul 2026.

Motiv: VERIFICAREA MECANICA a respins propunerea modelului: valoarea legala '2026' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare); valoarea legala '2026' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare)

### Calculul, pas cu pas — evaluat de cod, nu de model

- `baza_CAS = nr_salarii_minime * salariu_minim` = (12 × 4.050) = **48.600**
  - `nr_salarii_minime` = 12 — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art148/alin2/lita`: „nivelul de 12 salarii minime brute pe țară, în cazul veniturilor realizate cuprinse între 12 salarii minime brute pe țară inclusiv și 24 de salarii minime brute pe țară;”
  - `salariu_minim` = 4.050 — VALOARE_LEGALA din `hg_1506_2024_salariu_minim#art1`: „salariul de bază minim brut pe țară garantat în plată se stabilește în bani, fără a include sporuri și alte adaosuri, la suma de 4.050 lei lunar”
- `CAS = baza_CAS * cota_CAS` = (48.600 × 25%) = **12.150**
  - `cota_CAS` = 25% — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art138`: „a) 25% datorată de către persoanele fizice care au calitatea de angajați sau pentru care există obligația plății contribuției de asigurări sociale, potrivit prezentei legi;”

- **Codul fiscal (Legea 227/2015) art. 148 alin. (2) lit. a)** — `cod_fiscal_227_2015_consolidat#art148/alin2/lita` · valabil din nedovedit
  > nivelul de 12 salarii minime brute pe țară, în cazul veniturilor realizate cuprinse între 12 salarii minime brute pe țară inclusiv și 24 de salarii minime brute pe țară;
- **Codul fiscal (Legea 227/2015) art. 148 alin. (2)** — `cod_fiscal_227_2015_consolidat#art148/alin2` · valabil din nedovedit
  > Baza anuală de calcul al contribuției de asigurări sociale, în cazul persoanelor care realizează veniturile prevăzute la art. 137 alin. (1) lit. b) și b^1) , o reprezintă venitul ales de contribuabil, care nu poate fi mai mic decât:
- **Codul fiscal (Legea 227/2015) art. 148 alin. (1)** — `cod_fiscal_227_2015_consolidat#art148/alin1` · valabil din nedovedit
  > au realizat venituri din activitățile prevăzute la art. 137 alin. (1) lit. b) și b^1) , din una sau mai multe surse și/sau categorii de venituri, a căror valoare anuală cumulată este cel puțin egală cu 12 salarii minime brute pe țară, datorează contribuția de asigurări sociale la o bază de calcul stabilită potrivit alin. (2) .
- **Codul fiscal (Legea 227/2015) art. 138** — `cod_fiscal_227_2015_consolidat#art138` · valabil din 2018-01-01
  > a) 25% datorată de către persoanele fizice care au calitatea de angajați sau pentru care există obligația plății contribuției de asigurări sociale, potrivit prezentei legi;
- **Codul fiscal (Legea 227/2015) art. 135^1 alin. (3)** — `cod_fiscal_227_2015_consolidat#art135^1/alin3` · valabil din 2025-01-01
  > la stabilirea bazei anuale de calcul al contribuției de asigurări sociale, respectiv al contribuției de asigurări sociale de sănătate datorate se ia în calcul valoarea salariului minim brut pe țară stabilit prin hotărâre a Guvernului, în vigoare la data de 1 ianuarie a anului de realizare a venitului pentru care se stabilesc contribuțiile sociale
- **HG 1506/2024 art. 1** — `hg_1506_2024_salariu_minim#art1` · valabil din 2025-01-01
  > Începând cu data de 1 ianuarie 2025, salariul de bază minim brut pe țară garantat în plată se stabilește în bani, fără a include sporuri și alte adaosuri, la suma de 4.050 lei lunar
- **Codul fiscal (Legea 227/2015) art. 122 alin. (3)** — `cod_fiscal_227_2015_consolidat#art122/alin3` · valabil din nedovedit
  > Declarația unică privind impozitul pe venit și contribuțiile sociale datorate de persoanele fizice se completează și se depune la organul fiscal competent, pentru fiecare an fiscal, până la data de 25 mai inclusiv a anului următor celui de realizare a veniturilor.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art151/alin3` — Excepția de la art. 148 alin. (1) și (2) privește contribuabilii care în cursul anului de realizare a venitului se încadrează în categoria persoanelor exceptate de la plata CAS potrivit art. 150 (caz în care plafonul se recalculează pe luni). Cazul din întrebare este al unei PFA nepensionare, fără s…

### Navigarea (19 pași, 11 ture)

1. `cauta` {"interogare": "baza anuala de calcul al contributiei de asigurari sociale venituri din activitati independente 12 salarii minime brute"}
2. `cauta` {"interogare": "declaratia unica termen 25 mai inclusiv a anului urmator venit estimat"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art148/alin1"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art122/alin3"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art148/alin2"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art151/alin3"}
7. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art148/alin2/lita"}
8. `cauta` {"interogare": "cota contributiei de asigurari sociale 25% art 138"}
9. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art138"}
10. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art148"}
11. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art148/alin3"}
12. `cauta` {"interogare": "salariul de bază minim brut pe țară garantat în plată 2026 lei lunar"}
13. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art135^1"}
14. `cuprins` {"act": "hg_146_2026_salariu_minim", "filtru": "salariul"}
15. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art135^1/alin3"}
16. `cuprins` {"act": "hg_146_2026_salariu_minim", "filtru": ""}
17. `cauta` {"interogare": "începând cu data de 1 ianuarie 2026 salariul de bază minim brut pe țară garantat în plată se stabilește în bani"}
18. `deschide` {"id": "hg_1506_2024_salariu_minim#art1"}
19. `cuprins` {"act": "hg_1094_2025", "filtru": "salariul"}

Apel: `claude-opus-5`, {'intrare': 22, 'iesire': 6921, 'cache_scriere': 15249, 'cache_citire': 159487} tokeni, $0.3482, 96 s

Pe fond (comparator): **NU POT** — VERIFICAREA MECANICA a respins propunerea modelului: valoarea legala '2026' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare); valoarea legala '2026'

## v4 — NU POT, pe fond NU POT

> modelul s-a abţinut: Regula de bază este identificată: la un venit net cuprins între 12 și 24 de salarii minime brute pe țară, baza anuală de calcul al CAS este nivelul de 12 salarii minime brute pe țară, iar Declarația unică se depune până la 25 mai inclusiv a anului următor celui de realizare a veniturilor (deci pentru 2026, în anul următor). Nu pot însă indica suma CAS minim datorat: aceasta ar presupune un calcul (cotă × 12 salarii minime), iar în atomii obținuți nu apar nici valoarea salari…

## Cheia

- CAS minim 12.150 lei = 25% × 48.600 lei (12 salarii minime × 4.050 lei, salariul minim în vigoare la 01.01.2026; NU 4.325 lei, în vigoare de la 01.07.2026). Venitul se încadrează între 12 și 24 salarii minime (48.600-97.200 lei). D212 până la 25 mai 2027 inclusiv.
- temei: Legea 227/2015 art. 135^1 alin. (3), art. 138 lit. a), art. 148 alin. (1)-(3), art. 122 alin. (3); HG 1506/2024 art. 1 (4.050 lei de la 01.01.2025); HG 146/2026 art. 1-2 (4.325 lei de la 01.07.2026)
