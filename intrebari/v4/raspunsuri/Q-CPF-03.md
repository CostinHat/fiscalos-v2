# Q-CPF-03 — CALCUL

**Întrebarea:** La inspecție s-a stabilit prin decizie de impunere o diferență de TVA nedeclarată de 20.000 lei, cu scadența inițială 25.07.2025. Decizia e comunicată pe 10.03.2026, iar firma plătește diferența pe 03.04.2026. Ce accesorii datorează?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 25.07.2025, presupun o persoană juridică plătitoare de TVA, contribuabil administrat de organul fiscal central, căreia organul de inspecție fiscală i-a stabilit prin decizie de impunere o diferență de TVA nedeclarată (obligație fiscală principală nedeclarată), fără fapte de evaziune constatate de organele judiciare și fără eșalonare la plată sau suspendare a executării actului.*

> **Datorează dobânzi de 0,02% pentru fiecare zi de întârziere și penalitate de nedeclarare de 0,08% pentru fiecare zi, ambele calculate de la ziua imediat următoare scadenței inițiale până la data stingerii sumei, inclusiv; penalitatea de întârziere de 0,01% NU se aplică, fiind datorată penalitate de nedeclarare. Dobândă: 1.008 lei. Penalitate de nedeclarare brută: 4.032 lei; dacă plata s-a făcut până la termenul de plată stabilit în funcție de data comunicării deciziei, penalitatea se reduce cu 75%, rezultând 1.008 lei. [calcul: dobanda = baza * cota_dobanda * zile(scadenta, data_platii) = 1.008; penalitate_bruta = baza * cota_nedeclarare * zile(scadenta, data_platii) = 4.032; penalitate_redusa = penalitate_bruta - penalitate_bruta * reducere = 1.008]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul — evaluat de cod, nu de model

- `dobanda = baza * cota_dobanda * zile(scadenta, data_platii)` → **1.008**
  - `baza` = 20.000 — din întrebare: „o diferență de TVA nedeclarată de 20.000 lei”
  - `cota_dobanda` = 0,02% — din `legea_207_2015_consolidat#art174/alin5`: „Nivelul dobânzii este de 0,02% pentru fiecare zi de întârziere.”
  - `scadenta` = 25.07.2025 — din întrebare: „cu scadența inițială 25.07.2025”
  - `data_platii` = 03.04.2026 — din întrebare: „firma plătește diferența pe 03.04.2026”
- `penalitate_bruta = baza * cota_nedeclarare * zile(scadenta, data_platii)` → **4.032**
  - `baza` = 20.000 — din întrebare: „o diferență de TVA nedeclarată de 20.000 lei”
  - `cota_nedeclarare` = 0,08% — din `legea_207_2015_consolidat#art181/alin1`: „contribuabilul/plătitorul datorează o penalitate de nedeclarare de 0,08% pe fiecare zi, începând cu ziua imediat următoare scadenței și până la data stingerii sumei datorate, inclusiv”
  - `scadenta` = 25.07.2025 — din întrebare: „cu scadența inițială 25.07.2025”
  - `data_platii` = 03.04.2026 — din întrebare: „firma plătește diferența pe 03.04.2026”
- `penalitate_redusa = penalitate_bruta - penalitate_bruta * reducere` → **1.008**
  - `reducere` = 75% — din `legea_207_2015_consolidat#art181/alin2`: „Penalitatea de nedeclarare stabilită potrivit alin. (1) se reduce cu 75%, dacă obligațiile fiscale principale stabilite prin decizie:”

- **Codul de procedură fiscală (Legea 207/2015) art. 181 alin. (1)** — `legea_207_2015_consolidat#art181/alin1` · valabil din 2020-12-24
  > Pentru obligațiile fiscale principale nedeclarate sau declarate incorect de contribuabil/plătitor și stabilite de organul fiscal prin decizii de impunere, contribuabilul/plătitorul datorează o penalitate de nedeclarare de 0,08% pe fiecare zi, începând cu ziua imediat următoare scadenței și până la data stingerii sumei datorate, inclusiv
- **Codul de procedură fiscală (Legea 207/2015) art. 174 alin. (1)** — `legea_207_2015_consolidat#art174/alin1` · valabil din nedovedit
  > Dobânzile se calculează pentru fiecare zi de întârziere, începând cu ziua imediat următoare termenului de scadență și până la data stingerii sumei datorate, inclusiv.
- **Codul de procedură fiscală (Legea 207/2015) art. 174 alin. (5)** — `legea_207_2015_consolidat#art174/alin5` · valabil din nedovedit
  > Nivelul dobânzii este de 0,02% pentru fiecare zi de întârziere.
- **Codul de procedură fiscală (Legea 207/2015) art. 176 alin. (2)** — `legea_207_2015_consolidat#art176/alin2` · valabil din nedovedit
  > Nivelul penalității de întârziere este de 0,01% pentru fiecare zi de întârziere.
- **Codul de procedură fiscală (Legea 207/2015) art. 176 alin. (4)** — `legea_207_2015_consolidat#art176/alin4` · valabil din 2017-09-03
  > Penalitatea de întârziere nu se aplică pentru obligațiile fiscale principale pentru care se datorează penalitate de nedeclarare potrivit art. 181 .
- **Codul de procedură fiscală (Legea 207/2015) art. 181 alin. (2)** — `legea_207_2015_consolidat#art181/alin2` · valabil din 2020-12-24
  > Penalitatea de nedeclarare stabilită potrivit alin. (1) se reduce cu 75%, dacă obligațiile fiscale principale stabilite prin decizie:
- **Codul de procedură fiscală (Legea 207/2015) art. 181 alin. (2) lit. a)** — `legea_207_2015_consolidat#art181/alin2/lita` · valabil din nedovedit
  > se sting prin plată sau compensare până la termenul prevăzut la art. 156 alin. (1)
- **Codul de procedură fiscală (Legea 207/2015) art. 156 alin. (1)** — `legea_207_2015_consolidat#art156/alin1` · valabil din nedovedit
  > Pentru diferențele de obligații fiscale principale și pentru obligațiile fiscale accesorii, stabilite prin decizie potrivit legii, termenul de plată se stabilește în funcție de data comunicării deciziei, astfel:
- **Codul de procedură fiscală (Legea 207/2015) art. 181 alin. (4)** — `legea_207_2015_consolidat#art181/alin4` · valabil din nedovedit
  > Aplicarea penalității de nedeclarare prevăzute de prezentul articol nu înlătură obligația
- derogare tratată: `legea_207_2015_consolidat#art278/alin4` — Excepția privește situația contestării actului administrativ fiscal cu suspendarea executării; întrebarea nu menționează contestație sau suspendare, deci nu se aplică.
- derogare tratată: `legea_207_2015_consolidat#art174/alin4` — Excepția de la regula de calcul a dobânzilor vizează situații speciale (altele decât diferențele stabilite prin decizie de impunere la inspecție), care nu sunt descrise în întrebare.
- derogare tratată: `legea_207_2015_consolidat#art197/alin1` — Excepția privește nivelul dobânzii în cazul înlesnirilor la plată (eșalonare); firma a plătit integral, nu are eșalonare, deci nu se aplică.
- derogare tratată: `legea_207_2015_consolidat#art181/alin3` — Majorarea cu 100% se aplică doar dacă obligațiile rezultă din fapte de evaziune fiscală constatate de organele judiciare; nu este cazul.

### Navigarea (12 pași, 7 ture)

1. `cauta` {"interogare": "penalitate de nedeclarare 0,08% obligații fiscale principale nedeclarate"}
2. `cuprins` {"act": "legea_207_2015_consolidat", "filtru": "dobânzi penalități"}
3. `deschide` {"id": "legea_207_2015_consolidat#art181/alin1"}
4. `deschide` {"id": "legea_207_2015_consolidat#art174"}
5. `deschide` {"id": "legea_207_2015_consolidat#art181"}
6. `deschide` {"id": "legea_207_2015_consolidat#art176"}
7. `deschide` {"id": "legea_207_2015_consolidat#art176/alin4"}
8. `deschide` {"id": "legea_207_2015_consolidat#art181/alin2"}
9. `deschide` {"id": "legea_207_2015_consolidat#art156"}
10. `deschide` {"id": "legea_207_2015_consolidat#art174/alin1"}
11. `deschide` {"id": "legea_207_2015_consolidat#art156/alin1"}
12. `deschide` {"id": "legea_207_2015_consolidat#art174/alin5"}

Apel: `claude-opus-5`, {'intrare': 14, 'iesire': 7181, 'cache_scriere': 10130, 'cache_citire': 74559} tokeni, $0.2802, 97 s

Pe fond: **GREȘIT** — faptul principal al cheii (['252 zile']) nu e in raspuns

## Stratul semantic v3 (context dat de căutare) — RĂSPUNS, pe fond GREȘIT

> Firma datorează penalitate de nedeclarare de 0,08% pe fiecare zi, începând cu ziua imediat următoare scadenței inițiale (25.07.2025) și până la data stingerii sumei, 03.04.2026, inclusiv, precum și obligații fiscale accesorii (dobânzi) calculate pentru aceeași perioadă, de la data scadenței obligației principale până la data plății, inclusiv. Cota dobânzii nu rezultă din atomii primiți, deci nu o pot preciza.

## Cheia

- 252 zile (26.07.2025–03.04.2026 inclusiv). Penalitate de nedeclarare 20.000 × 0,08% × 252 = 4.032 lei, redusă cu 75% (plată până la 05.04.2026, termenul art. 156) → 1.008 lei. Dobânzi 20.000 × 0,02% × 252 = 1.008 lei. Penalitate de întârziere: 0 (nu se aplică când se datorează penalitate de nedeclarare). Total 2.016 lei.
- temei: Legea 207/2015 art. 181 alin. (1), (2) lit. a), (4); art. 156 alin. (1) lit. a); art. 176 alin. (4); art. 174 alin. (2) și (5)
