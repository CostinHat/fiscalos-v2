# Q-PRF-05 — CALCUL

**Întrebarea:** Microîntreprindere, trimestrul I 2026: venituri din vânzări 200.000 lei, dividende primite de la o SRL română 30.000 lei, venituri din diferențe de curs valutar 5.000 lei, reduceri comerciale primite ulterior facturării (cont 609) 2.000 lei. Cât impozit datorează pentru T1?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 28.09.2026, pentru o persoană juridică română plătitoare de impozit pe veniturile microîntreprinderilor în anul fiscal 2026, care determină impozitul trimestrial pe baza veniturilor trimestrului I 2026; presupun că societatea rămâne în sistemul microîntreprinderilor în T1 (nu depășește plafonul și nu iese din sistem) și că nu există alte venituri sau elemente de adăugat/scăzut în afara celor enumerate în întrebare.*

> **Baza impozabilă a T1 2026 este 202.000 lei (200.000 lei venituri din vânzări + 2.000 lei reduceri comerciale primite din contul 609; dividendele de la SRL română și veniturile din diferențe de curs valutar nu se includ în T1), iar impozitul datorat este 2.020 lei. [calcul: baza = venituri_vanzari + reduceri_609 = 202.000; impozit = baza * cota = 2.020]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul — evaluat de cod, nu de model

- `baza = venituri_vanzari + reduceri_609` → **202.000**
  - `venituri_vanzari` = 200.000 — din întrebare: „venituri din vânzări 200.000 lei”
  - `reduceri_609` = 2.000 — din întrebare: „reduceri comerciale primite ulterior facturării (cont 609) 2.000 lei”
- `impozit = baza * cota` → **2.020**
  - `cota` = 1% — din `cod_fiscal_227_2015_consolidat#art51/alin1`: „Cota de impozit pe veniturile microîntreprinderilor este de 1%.”

- **Codul fiscal (Legea 227/2015) art. 51 alin. (1)** — `cod_fiscal_227_2015_consolidat#art51/alin1` · valabil din 2026-01-01
  > Cota de impozit pe veniturile microîntreprinderilor este de 1%.
- **Codul fiscal (Legea 227/2015) art. 53 alin. (1)** — `cod_fiscal_227_2015_consolidat#art53/alin1` · valabil din nedovedit
  > Baza impozabilă a impozitului pe veniturile microîntreprinderilor o constituie veniturile din orice sursă, din care se scad:
- **Codul fiscal (Legea 227/2015) art. 53 alin. (1) lit. n)** — `cod_fiscal_227_2015_consolidat#art53/alin1/litn` · valabil din 2020-12-24
  > dividendele primite de la o persoană juridică română. ...
- **Codul fiscal (Legea 227/2015) art. 53 alin. (1) lit. h)** — `cod_fiscal_227_2015_consolidat#art53/alin1/lith` · valabil din nedovedit
  > veniturile din diferențe de curs valutar; ...
- **Codul fiscal (Legea 227/2015) art. 53 alin. (2)** — `cod_fiscal_227_2015_consolidat#art53/alin2` · valabil din nedovedit
  > Pentru determinarea impozitului pe veniturile microîntreprinderilor, la baza impozabilă determinată potrivit alin. (1) se adaugă următoarele:
- **Codul fiscal (Legea 227/2015) art. 53 alin. (2) lit. a)** — `cod_fiscal_227_2015_consolidat#art53/alin2/lita` · valabil din nedovedit
  > valoarea reducerilor comerciale primite ulterior facturării, înregistrate în contul "609", potrivit reglementărilor contabile aplicabile; ...
- **Codul fiscal (Legea 227/2015) art. 53 alin. (2) lit. b)** — `cod_fiscal_227_2015_consolidat#art53/alin2/litb` · valabil din 2023-01-01
  > în trimestrul IV sau în ultimul trimestru al perioadei impozabile, în cazul contribuabililor care își încetează existența, diferența favorabilă dintre veniturile din diferențe de curs valutar/veniturile financiare aferente creanțelor și datoriilor cu decontare în funcție de cursul unei valute, rezultate din evaluarea sau decontarea acestora,
- derogare tratată: `cod_fiscal_227_2015_consolidat#art53/alin2/litb` — Regula de adăugare a diferenței favorabile din diferențe de curs valutar se aplică numai în trimestrul IV (sau ultimul trimestru, la încetarea existenței), deci nu se aplică la calculul impozitului pentru trimestrul I 2026; în T1 veniturile din diferențe de curs valutar se scad potrivit art. 53 alin…

### Navigarea (12 pași, 7 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "impozabilă microîntreprinderilor"}
2. `cauta` {"interogare": "baza impozabilă microîntreprinderi diferențe de curs valutar reduceri comerciale"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art53"}
4. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Cotele de impozitare"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art53/alin1"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art53/alin2"}
7. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art51"}
8. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art53/alin2/lita"}
9. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art51/alin1"}
10. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art53/alin1/lith"}
11. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art53/alin1/litn"}
12. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art53/alin2/litb"}

Apel: `claude-opus-5`, {'intrare': 14, 'iesire': 5438, 'cache_scriere': 11952, 'cache_citire': 86293} tokeni, $0.2539, 78 s

Pe fond: **GREȘIT** — articolul citat [('cf', '51')] nu e printre cele ale cheii [('cf', '53'), (None, '53'), ('oug_89_2025', '51'), (None, '56')]

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți conțin doar reguli privind baza impozabilă (scăderea reducerilor comerciale din contul 609 și tratamentul diferențelor de curs valutar doar în trimestrul IV), nu și textul care stabilește baza impozabilă generală (art. 53 alin. (1), inclusiv excluderea dividendelor primite de la o persoană juridică română, care apare doar ca text de modificare din Legea 296/2020, fără atom din Codul fiscal în vigoare) și nici cota de impozitare aplicabilă microîntreprinderilor…

## Cheia

- 2.020 lei (bază 202.000 = 235.000 − 30.000 dividende − 5.000 dif. curs + 2.000 cont 609; × 1%)
- temei: Cod fiscal art. 53 alin. (1) partea introductivă, lit. h) și lit. n); art. 53 alin. (2) lit. a); art. 51 alin. (1) (mod. OUG 89/2025); art. 56 alin. (1)
