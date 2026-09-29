# Q-PRF-07 — CALCUL

**Întrebarea:** Profit contabil 2026 = 100.000 lei, cheltuiala cu impozitul pe profit = 20.000 lei, cheltuieli de protocol = 10.000 lei. Ce sumă din protocol e deductibilă și cât se adaugă ca nedeductibil?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 28.09.2026, presupun un contribuabil plătitor de impozit pe profit care determină rezultatul fiscal pentru anul 2026, cu profit contabil de 100.000 lei, cheltuială cu impozitul pe profit de 20.000 lei și cheltuieli de protocol de 10.000 lei, fără TVA colectată aferentă cadourilor peste 100 lei inclusă suplimentar.*

Datele din întrebare: 2026-09-28 · data de referință aleasă: **2026-09-28** — Faptul întrebat este deductibilitatea cheltuielilor de protocol la calculul rezultatului fiscal al anului 2026, singura dată purtată de întrebare.

> **Cheltuielile de protocol sunt deductibile în limita a 2% aplicată asupra profitului contabil la care se adaugă cheltuielile cu impozitul pe profit și cheltuielile de protocol: baza este 130.000 lei, deci deductibil 2.600 lei, iar restul de 7.400 lei se adaugă ca cheltuială nedeductibilă.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul, pas cu pas — evaluat de cod, nu de model

- `baza_protocol = profit_contabil + cheltuiala_impozit_profit + cheltuieli_protocol` = ((100.000 + 20.000) + 10.000) = **130.000**
  - `profit_contabil` = 100.000 — FAPT_CAZ (din întrebare): „Profit contabil 2026 = 100.000 lei”
  - `cheltuiala_impozit_profit` = 20.000 — FAPT_CAZ (din întrebare): „cheltuiala cu impozitul pe profit = 20.000 lei”
  - `cheltuieli_protocol` = 10.000 — FAPT_CAZ (din întrebare): „cheltuieli de protocol = 10.000 lei”
- `limita_deductibila = baza_protocol * cota_protocol` = (130.000 × 2%) = **2.600**
  - `cota_protocol` = 2% — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art25/alin3/lita`: „cheltuielile de protocol în limita unei cote de 2% aplicată asupra profitului contabil”
- `nedeductibil = cheltuieli_protocol - limita_deductibila` = (10.000 − 2.600) = **7.400**
  - `cheltuieli_protocol` = 10.000 — FAPT_CAZ (din întrebare): „cheltuieli de protocol = 10.000 lei”

- **Codul fiscal (Legea 227/2015) art. 25 alin. (3) lit. a)** — `cod_fiscal_227_2015_consolidat#art25/alin3/lita` · valabil din nedovedit
  > cheltuielile de protocol în limita unei cote de 2% aplicată asupra profitului contabil la care se adaugă cheltuielile cu impozitul pe profit și cheltuielile de protocol.
- **Codul fiscal (Legea 227/2015) art. 25 alin. (3) lit. a)** — `cod_fiscal_227_2015_consolidat#art25/alin3/lita` · valabil din nedovedit
  > În cadrul cheltuielilor de protocol se includ și cheltuielile înregistrate cu taxa pe valoarea adăugată colectată potrivit prevederilor titlului VII , pentru cadourile oferite de contribuabil, cu valoare mai mare de 100 lei

### Navigarea (3 pași, 3 ture)

1. `cauta` {"interogare": "cheltuielile de protocol în limita unei cote de 2% profitul contabil"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "protocol"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art25/alin3/lita"}

Apel: `claude-opus-5`, {'intrare': 6, 'iesire': 2351, 'cache_scriere': 2305, 'cache_citire': 23336} tokeni, $0.0849, 28 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond CORECT

> Cheltuielile de protocol sunt deductibile în limita de 2% aplicată asupra bazei formate din profitul contabil + cheltuiala cu impozitul pe profit + cheltuielile de protocol, adică 2.600 lei deductibili, iar restul de 7.400 lei se adaugă ca cheltuială nedeductibilă la calculul rezultatului fiscal. [calcul: baza = profit_contabil + impozit_profit + protocol = 130.000; deductibil = baza * cota = 2.600; nedeductibil = protocol - deductibil = 7.400]

## Cheia

- Deductibil 2.600 lei (2% × (100.000 + 20.000 + 10.000) = 2% × 130.000); nedeductibil 7.400 lei
- temei: Cod fiscal art. 25 alin. (3) lit. a)
