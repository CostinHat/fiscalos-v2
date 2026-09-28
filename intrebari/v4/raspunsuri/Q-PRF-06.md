# Q-PRF-06 — CALCUL

**Întrebarea:** Plătitor de impozit pe profit (cifra de afaceri sub 50 mil. euro) are o pierdere fiscală din 2024 de 100.000 lei, nerecuperată. În 2026 profitul impozabil înainte de recuperarea pierderii este 120.000 lei. Cât impozit pe profit datorează și ce pierdere rămâne de recuperat?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 31.12.2024, presupun un contribuabil plătitor de impozit pe profit în regim general (an fiscal = an calendaristic), cu cifră de afaceri sub 50 mil. euro (deci fără impozit minim pe cifra de afaceri), care are de recuperat o pierdere fiscală anuală aferentă anului 2024 de 100.000 lei și un profit impozabil al anului 2026 de 120.000 lei înainte de recuperarea pierderii, fără alte deduceri, credite fiscale sau scutiri.*

> **Pierderea din 2024 se recuperează în limita a 70% din profitul impozabil, adică 84.000 lei; profitul impozabil rămas este 36.000 lei, iar impozitul pe profit datorat, la cota de 16%, este 5.760 lei. Pierderea rămasă de recuperat (în cadrul celor 5 ani consecutivi) este 16.000 lei. [calcul: pierdere_recuperata = min(pierdere_2024, profit_inainte * limita_procent) = 84.000; profit_impozabil = profit_inainte - pierdere_recuperata = 36.000; impozit = profit_impozabil * cota = 5.760; pierdere_ramasa = pierdere_2024 - pierdere_recuperata = 16.000]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul — evaluat de cod, nu de model

- `pierdere_recuperata = min(pierdere_2024, profit_inainte * limita_procent)` → **84.000**
  - `pierdere_2024` = 100.000 — din întrebare: „o pierdere fiscală din 2024 de 100.000 lei, nerecuperată”
  - `profit_inainte` = 120.000 — din întrebare: „În 2026 profitul impozabil înainte de recuperarea pierderii este 120.000 lei”
  - `limita_procent` = 70% — din `cod_fiscal_227_2015_consolidat#art31/alin1`: „se recuperează din profiturile impozabile realizate, în limita a 70% inclusiv, în următorii 5 ani consecutivi”
- `profit_impozabil = profit_inainte - pierdere_recuperata` → **36.000**
  - `profit_inainte` = 120.000 — din întrebare: „În 2026 profitul impozabil înainte de recuperarea pierderii este 120.000 lei”
- `impozit = profit_impozabil * cota` → **5.760**
  - `cota` = 16% — din `cod_fiscal_227_2015_consolidat#art17`: „Cota de impozit pe profit care se aplică asupra profitului impozabil este de 16%.”
- `pierdere_ramasa = pierdere_2024 - pierdere_recuperata` → **16.000**
  - `pierdere_2024` = 100.000 — din întrebare: „o pierdere fiscală din 2024 de 100.000 lei, nerecuperată”

- **Codul fiscal (Legea 227/2015) art. 31 alin. (1)** — `cod_fiscal_227_2015_consolidat#art31/alin1` · valabil din nedovedit
  > Pierderile fiscale anuale stabilite prin declarația de impozit pe profit, începând cu anul 2024/anul fiscal modificat care începe în anul 2024, după caz, se recuperează din profiturile impozabile realizate, în limita a 70% inclusiv, în următorii 5 ani consecutivi.
- **Codul fiscal (Legea 227/2015) art. 17** — `cod_fiscal_227_2015_consolidat#art17` · valabil din nedovedit
  > Cota de impozitare Cota de impozit pe profit care se aplică asupra profitului impozabil este de 16%.

### Navigarea (5 pași, 4 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "pierderi fiscale"}
2. `cauta` {"interogare": "recuperarea pierderii fiscale 70% din profitul impozabil 5 ani consecutivi"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art31/alin1"}
4. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Cotele de impozitare"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art17"}

Apel: `claude-opus-5`, {'intrare': 8, 'iesire': 3343, 'cache_scriere': 7018, 'cache_citire': 37663} tokeni, $0.1463, 47 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți nu conțin regula aplicabilă pierderilor fiscale înregistrate începând cu anul 2024 (art. 31 alin. (1) din Codul fiscal nu se află în context); singurul text despre recuperarea pierderilor, art. 31 alin. (7), se referă expres la pierderile aferente anilor precedenți anului 2024, rămase de recuperat la 31 decembrie 2023, deci nu acoperă o pierdere din 2024. De asemenea, lipsește din atomi cota de impozit pe profit, iar determinarea sumei de impozit datorat și a …

## Cheia

- Recuperare max. 70% × 120.000 = 84.000; profit impozabil 36.000; impozit 16% = 5.760 lei; rămân de recuperat 16.000 lei (în limita celor 5 ani consecutivi, până în 2029)
- temei: Cod fiscal art. 31 alin. (1) (limita 70%, 5 ani, pierderi din 2024 încoace; mod. OUG 115/2023); art. 17 (cota 16%)
