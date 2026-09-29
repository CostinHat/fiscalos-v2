# Q-PRF-06 — CALCUL

**Întrebarea:** Plătitor de impozit pe profit (cifra de afaceri sub 50 mil. euro) are o pierdere fiscală din 2024 de 100.000 lei, nerecuperată. În 2026 profitul impozabil înainte de recuperarea pierderii este 120.000 lei. Cât impozit pe profit datorează și ce pierdere rămâne de recuperat?

## Stratul de navigare v5 — NU POT RĂSPUNDE

*La data de 28.09.2026, pentru o persoană juridică plătitoare de impozit pe profit (cifra de afaceri sub 50 mil. euro, deci fără incidența impozitului minim pe cifra de afaceri), care recuperează în anul 2026 o pierdere fiscală anuală înregistrată în anul 2024, presupunând an fiscal calendaristic și absența altor ajustări sau scutiri.*

Datele din întrebare: 2024-12-31, 2026-09-28 · data de referință aleasă: **2026-09-28** — Faptul întrebat este impozitul pe profit datorat pentru anul 2026 și pierderea rămasă de recuperat după acest an; anul 2024 apare doar ca an al înregistrării pierderii.

Motiv: VERIFICAREA MECANICA a respins propunerea modelului: citatul NU e verbatim in atomul cod_fiscal_227_2015_consolidat#art31/alin1; valoarea legala '70' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare); valoarea legala '16' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare); valoarea legala '5' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare)

### Calculul, pas cu pas — evaluat de cod, nu de model

- `pierdere_recuperata = min(pierdere_2024, profit_impozabil * limita_recuperare)` = min(100.000, (120.000 × 70%)) = **84.000**
  - `pierdere_2024` = 100.000 — FAPT_CAZ (din întrebare): „o pierdere fiscală din 2024 de 100.000 lei, nerecuperată”
  - `profit_impozabil` = 120.000 — FAPT_CAZ (din întrebare): „În 2026 profitul impozabil înainte de recuperarea pierderii este 120.000 lei”
  - `limita_recuperare` = 70% — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art31/alin1`: „se recuperează din profiturile impozabile realizate, în limita a 70% inclusiv, în următorii 5 ani consecutivi”
- `baza_impozabila = profit_impozabil - pierdere_recuperata` = (120.000 − 84.000) = **36.000**
  - `profit_impozabil` = 120.000 — FAPT_CAZ (din întrebare): „În 2026 profitul impozabil înainte de recuperarea pierderii este 120.000 lei”
- `impozit = baza_impozabila * cota_impozit` = (36.000 × 16%) = **5.760**
  - `cota_impozit` = 16% — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art17`: „Cota de impozit pe profit care se aplică asupra profitului impozabil este de 16%.”
- `pierdere_ramasa = pierdere_2024 - pierdere_recuperata` = (100.000 − 84.000) = **16.000**
  - `pierdere_2024` = 100.000 — FAPT_CAZ (din întrebare): „o pierdere fiscală din 2024 de 100.000 lei, nerecuperată”

- **Codul fiscal (Legea 227/2015) art. 31 alin. (1)** — `cod_fiscal_227_2015_consolidat#art31/alin1` · valabil din nedovedit
  > Pierderile fiscale anuale stabilite prin declara tia de impozit pe profit, "ncep"nd cu anul 2024
- derogare tratată: `cod_fiscal_227_2015_consolidat#art31/alin7` — Regula pentru pierderile aferente anilor anteriori anului 2024, rămase de recuperat la 31.12.2023, nu se aplică, întrucât pierderea din speță este înregistrată în anul 2024 și intră sub regula alin. (1).

### Navigarea (6 pași, 5 ture, 1 reîncercare C23)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "pierderi fiscale"}
2. `cauta` {"interogare": "cota de impozit pe profit 16%"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art31"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art17"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art31/alin1"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art31/alin7"}

Apel: `claude-opus-5`, {'intrare': 10, 'iesire': 5006, 'cache_scriere': 10357, 'cache_citire': 54541} tokeni, $0.2172, 53 s

Pe fond (comparator): **NU POT** — VERIFICAREA MECANICA a respins propunerea modelului: citatul NU e verbatim in atomul cod_fiscal_227_2015_consolidat#art31/alin1; valoarea legala '70' nu apare in niciun citat (C13: o valoare legala se

## v4 — RĂSPUNS, pe fond CORECT

> Pierderea din 2024 se recuperează în limita a 70% din profitul impozabil, adică 84.000 lei; profitul impozabil rămas este 36.000 lei, iar impozitul pe profit datorat, la cota de 16%, este 5.760 lei. Pierderea rămasă de recuperat (în cadrul celor 5 ani consecutivi) este 16.000 lei. [calcul: pierdere_recuperata = min(pierdere_2024, profit_inainte * limita_procent) = 84.000; profit_impozabil = profit_inainte - pierdere_recuperata = 36.000; impozit = profit_impozabil * cota = 5.760; pierdere_ramasa …

## Cheia

- Recuperare max. 70% × 120.000 = 84.000; profit impozabil 36.000; impozit 16% = 5.760 lei; rămân de recuperat 16.000 lei (în limita celor 5 ani consecutivi, până în 2029)
- temei: Cod fiscal art. 31 alin. (1) (limita 70%, 5 ani, pierderi din 2024 încoace; mod. OUG 115/2023); art. 17 (cota 16%)
