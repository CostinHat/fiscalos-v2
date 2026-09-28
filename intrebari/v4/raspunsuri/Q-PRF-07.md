# Q-PRF-07 — CALCUL

**Întrebarea:** Profit contabil 2026 = 100.000 lei, cheltuiala cu impozitul pe profit = 20.000 lei, cheltuieli de protocol = 10.000 lei. Ce sumă din protocol e deductibilă și cât se adaugă ca nedeductibil?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 28.09.2026, presupun un contribuabil plătitor de impozit pe profit (persoană juridică română), care determină rezultatul fiscal anual pe 2026 conform Titlului II din Codul fiscal, fără regim derogatoriu special, pornind de la datele contabile indicate în întrebare.*

> **Cheltuielile de protocol sunt deductibile în limita de 2% aplicată asupra bazei formate din profitul contabil + cheltuiala cu impozitul pe profit + cheltuielile de protocol, adică 2.600 lei deductibili, iar restul de 7.400 lei se adaugă ca cheltuială nedeductibilă la calculul rezultatului fiscal. [calcul: baza = profit_contabil + impozit_profit + protocol = 130.000; deductibil = baza * cota = 2.600; nedeductibil = protocol - deductibil = 7.400]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul — evaluat de cod, nu de model

- `baza = profit_contabil + impozit_profit + protocol` → **130.000**
  - `profit_contabil` = 100.000 — din întrebare: „Profit contabil 2026 = 100.000 lei”
  - `impozit_profit` = 20.000 — din întrebare: „cheltuiala cu impozitul pe profit = 20.000 lei”
  - `protocol` = 10.000 — din întrebare: „cheltuieli de protocol = 10.000 lei”
- `deductibil = baza * cota` → **2.600**
  - `cota` = 2% — din `cod_fiscal_227_2015_consolidat#art25/alin3/lita`: „cheltuielile de protocol în limita unei cote de 2% aplicată asupra profitului contabil la care se adaugă cheltuielile cu impozitul pe profit și cheltuielile de protocol.”
- `nedeductibil = protocol - deductibil` → **7.400**
  - `protocol` = 10.000 — din întrebare: „cheltuieli de protocol = 10.000 lei”

- **Codul fiscal (Legea 227/2015) art. 25 alin. (3) lit. a)** — `cod_fiscal_227_2015_consolidat#art25/alin3/lita` · valabil din nedovedit
  > cheltuielile de protocol în limita unei cote de 2% aplicată asupra profitului contabil la care se adaugă cheltuielile cu impozitul pe profit și cheltuielile de protocol.

### Navigarea (3 pași, 3 ture)

1. `cauta` {"interogare": "cheltuieli de protocol deductibile limita 2% profit contabil"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Cheltuieli"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art25/alin3/lita"}

Apel: `claude-opus-5`, {'intrare': 6, 'iesire': 2156, 'cache_scriere': 2485, 'cache_citire': 21345} tokeni, $0.0801, 31 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomul primit stabilește doar regula (limita de 2% aplicată asupra profitului contabil la care se adaugă cheltuielile cu impozitul pe profit și cheltuielile de protocol), dar sumele cerute (partea deductibilă și partea nedeductibilă din cei 10.000 lei) rezultă exclusiv din calcul aritmetic asupra datelor cazului și nu apar literal în niciun atom; conform regulilor, nu efectuez calcule.

## Cheia

- Deductibil 2.600 lei (2% × (100.000 + 20.000 + 10.000) = 2% × 130.000); nedeductibil 7.400 lei
- temei: Cod fiscal art. 25 alin. (3) lit. a)
