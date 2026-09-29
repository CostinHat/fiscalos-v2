# Q-CPF-03 — CALCUL

**Întrebarea:** La inspecție s-a stabilit prin decizie de impunere o diferență de TVA nedeclarată de 20.000 lei, cu scadența inițială 25.07.2025. Decizia e comunicată pe 10.03.2026, iar firma plătește diferența pe 03.04.2026. Ce accesorii datorează?

## Stratul de navigare v5 — NU POT RĂSPUNDE

*La data de referință 03.04.2026, presupun un contribuabil persoană juridică cu creanță fiscală principală de TVA administrată de organul fiscal central, diferență nedeclarată stabilită prin decizie de impunere în urma inspecției fiscale (fără fapte de evaziune constatate de organele judiciare și fără eșalonare la plată sau contestație suspendată), stinsă integral prin plată la 03.04.2026.*

Datele din întrebare: 2025-07-25, 2026-03-10, 2026-04-03 · data de referință aleasă: **2026-04-03** — Faptul întrebat este cuantumul accesoriilor datorate la stingerea obligației principale, iar accesoriile se calculează până la data stingerii inclusiv, adică 03.04.2026.

Motiv: VERIFICAREA MECANICA a respins propunerea modelului: cifra '26.07.2025' din raspuns nu apare literal in citate sau in intrebare; cifra '05.04.2026' din raspuns nu apare literal in citate sau in intrebare

### Calculul, pas cu pas — evaluat de cod, nu de model

- `zile(25.07.2025, 03.04.2026) = 252 zile`
- `dobanzi = suma * rata_dobanda * zile(scadenta_initiala, data_platii)` = ((20.000 × 0,02%) × zile(25.07.2025, 03.04.2026)) = **1.008**
  - `suma` = 20.000 — FAPT_CAZ (din întrebare): „o diferență de TVA nedeclarată de 20.000 lei”
  - `rata_dobanda` = 0,02% — VALOARE_LEGALA din `legea_207_2015_consolidat#art174/alin5`: „Nivelul dobânzii este de 0,02% pentru fiecare zi de întârziere.”
  - `scadenta_initiala` = 25.07.2025 — FAPT_CAZ (din întrebare): „cu scadența inițială 25.07.2025”
  - `data_platii` = 03.04.2026 — FAPT_CAZ (din întrebare): „firma plătește diferența pe 03.04.2026”
- `zile(25.07.2025, 03.04.2026) = 252 zile`
- `penalitate_nedeclarare_bruta = suma * rata_nedeclarare * zile(scadenta_initiala, data_platii)` = ((20.000 × 0,08%) × zile(25.07.2025, 03.04.2026)) = **4.032**
  - `suma` = 20.000 — FAPT_CAZ (din întrebare): „o diferență de TVA nedeclarată de 20.000 lei”
  - `rata_nedeclarare` = 0,08% — VALOARE_LEGALA din `legea_207_2015_consolidat#art181/alin1`: „datorează o penalitate de nedeclarare de 0,08% pe fiecare zi, începând cu ziua imediat următoare scadenței și până la data stingerii sumei datorate, inclusiv”
  - `scadenta_initiala` = 25.07.2025 — FAPT_CAZ (din întrebare): „cu scadența inițială 25.07.2025”
  - `data_platii` = 03.04.2026 — FAPT_CAZ (din întrebare): „firma plătește diferența pe 03.04.2026”
- `penalitate_nedeclarare_redusa = penalitate_nedeclarare_bruta * (1 - reducere)` = (4.032 × (1 − 75%)) = **1.008**
  - `reducere` = 75% — VALOARE_LEGALA din `legea_207_2015_consolidat#art181/alin2`: „Penalitatea de nedeclarare stabilită potrivit alin. (1) se reduce cu 75%, dacă obligațiile fiscale principale stabilite prin decizie:”
- `total_accesorii = dobanzi + penalitate_nedeclarare_redusa` = (1.008 + 1.008) = **2.016**

- **Codul de procedură fiscală (Legea 207/2015) art. 181 alin. (1)** — `legea_207_2015_consolidat#art181/alin1` · valabil din 2020-12-24
  > contribuabilul/plătitorul datorează o penalitate de nedeclarare de 0,08% pe fiecare zi, începând cu ziua imediat următoare scadenței și până la data stingerii sumei datorate, inclusiv, din obligațiile fiscale principale nedeclarate sau declarate incorect de contribuabil/plătitor și stabilite de organul fiscal prin decizii de impunere.
- **Codul de procedură fiscală (Legea 207/2015) art. 174 alin. (5)** — `legea_207_2015_consolidat#art174/alin5` · valabil din nedovedit
  > Nivelul dobânzii este de 0,02% pentru fiecare zi de întârziere.
- **Codul de procedură fiscală (Legea 207/2015) art. 174 alin. (1)** — `legea_207_2015_consolidat#art174/alin1` · valabil din nedovedit
  > Dobânzile se calculează pentru fiecare zi de întârziere, începând cu ziua imediat următoare termenului de scadență și până la data stingerii sumei datorate, inclusiv.
- **Codul de procedură fiscală (Legea 207/2015) art. 181 alin. (2)** — `legea_207_2015_consolidat#art181/alin2` · valabil din 2020-12-24
  > Penalitatea de nedeclarare stabilită potrivit alin. (1) se reduce cu 75%, dacă obligațiile fiscale principale stabilite prin decizie:
- **Codul de procedură fiscală (Legea 207/2015) art. 181 alin. (2) lit. a)** — `legea_207_2015_consolidat#art181/alin2/lita` · valabil din nedovedit
  > se sting prin plată sau compensare până la termenul prevăzut la art. 156 alin. (1) ;
- **Codul de procedură fiscală (Legea 207/2015) art. 156 alin. (1) lit. a)** — `legea_207_2015_consolidat#art156/alin1/lita` · valabil din nedovedit
  > dacă data comunicării este cuprinsă în intervalul 1-15 din lună, termenul de plată este până la data de 5 a lunii următoare, inclusiv;
- **Codul de procedură fiscală (Legea 207/2015) art. 176 alin. (4)** — `legea_207_2015_consolidat#art176/alin4` · valabil din 2017-09-03
  > Penalitatea de întârziere nu se aplică pentru obligațiile fiscale principale pentru care se datorează penalitate de nedeclarare potrivit art. 181 .
- **Codul de procedură fiscală (Legea 207/2015) art. 181 alin. (4)** — `legea_207_2015_consolidat#art181/alin4` · valabil din nedovedit
  > Aplicarea penalității de nedeclarare prevăzute de prezentul articol nu înlătură obligația de plată a dobânzilor prevăzute de prezentul cod.
- derogare tratată: `legea_207_2015_consolidat#art174/alin4` — Excepția de la art. 174 alin. (1) privește situații speciale de calcul al dobânzilor (altele decât diferențele de TVA stabilite prin decizie de impunere la inspecție), deci nu se aplică; se aplică regula generală din alin. (1).
- derogare tratată: `legea_207_2015_consolidat#art197/alin1` — Excepția privește nivelul dobânzii pe perioada eșalonării la plată; în cazul dat nu există eșalonare, obligația fiind stinsă integral prin plată la 03.04.2026.
- derogare tratată: `legea_207_2015_consolidat#art278/alin4` — Excepția de la art. 173 și art. 181 vizează situația contestării actului administrativ fiscal cu suspendarea executării; întrebarea nu indică nicio contestație sau suspendare, deci nu se aplică.
- derogare tratată: `legea_207_2015_consolidat#art183/alin1` — Excepția privește majorările de întârziere pentru obligațiile datorate bugetelor locale; TVA este creanță administrată de organul fiscal central, deci nu se aplică.
- derogare tratată: `legea_207_2015_consolidat#art181/alin3` — Majorarea cu 100% a penalității de nedeclarare se aplică doar dacă obligațiile au rezultat din fapte de evaziune fiscală constatate de organele judiciare; nu este cazul descris.

### Navigarea (15 pași, 8 ture)

1. `cauta` {"interogare": "dobânzi 0,02% pentru fiecare zi de întârziere"}
2. `cauta` {"interogare": "penalitate de nedeclarare 0,08% obligații fiscale principale nedeclarate"}
3. `deschide` {"id": "legea_207_2015_consolidat#art181/alin1"}
4. `deschide` {"id": "legea_207_2015_consolidat#art174/alin1"}
5. `deschide` {"id": "legea_207_2015_consolidat#art174"}
6. `deschide` {"id": "legea_207_2015_consolidat#art181"}
7. `deschide` {"id": "legea_207_2015_consolidat#art174/alin5"}
8. `deschide` {"id": "legea_207_2015_consolidat#art181/alin2"}
9. `deschide` {"id": "legea_207_2015_consolidat#art181/alin4"}
10. `deschide` {"id": "legea_207_2015_consolidat#art173"}
11. `cuprins` {"act": "legea_207_2015_consolidat", "filtru": "penalitate de întârziere"}
12. `deschide` {"id": "legea_207_2015_consolidat#art156/alin1"}
13. `deschide` {"id": "legea_207_2015_consolidat#art156/alin1/lita"}
14. `deschide` {"id": "legea_207_2015_consolidat#art176"}
15. `deschide` {"id": "legea_207_2015_consolidat#art176/alin4"}

Apel: `claude-opus-5`, {'intrare': 16, 'iesire': 7078, 'cache_scriere': 12790, 'cache_citire': 105171} tokeni, $0.3095, 93 s

Pe fond (comparator): **NU POT** — VERIFICAREA MECANICA a respins propunerea modelului: cifra '26.07.2025' din raspuns nu apare literal in citate sau in intrebare; cifra '05.04.2026' din raspuns nu apare literal in citate sau in intreb

## v4 — RĂSPUNS, pe fond GREȘIT

> Datorează dobânzi de 0,02% pentru fiecare zi de întârziere și penalitate de nedeclarare de 0,08% pentru fiecare zi, ambele calculate de la ziua imediat următoare scadenței inițiale până la data stingerii sumei, inclusiv; penalitatea de întârziere de 0,01% NU se aplică, fiind datorată penalitate de nedeclarare. Dobândă: 1.008 lei. Penalitate de nedeclarare brută: 4.032 lei; dacă plata s-a făcut până la termenul de plată stabilit în funcție de data comunicării deciziei, penalitatea se reduce cu 75…

## Cheia

- 252 zile (26.07.2025–03.04.2026 inclusiv). Penalitate de nedeclarare 20.000 × 0,08% × 252 = 4.032 lei, redusă cu 75% (plată până la 05.04.2026, termenul art. 156) → 1.008 lei. Dobânzi 20.000 × 0,02% × 252 = 1.008 lei. Penalitate de întârziere: 0 (nu se aplică când se datorează penalitate de nedeclarare). Total 2.016 lei.
- temei: Legea 207/2015 art. 181 alin. (1), (2) lit. a), (4); art. 156 alin. (1) lit. a); art. 176 alin. (4); art. 174 alin. (2) și (5)
