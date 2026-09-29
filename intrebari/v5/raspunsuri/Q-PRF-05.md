# Q-PRF-05 — CALCUL

**Întrebarea:** Microîntreprindere, trimestrul I 2026: venituri din vânzări 200.000 lei, dividende primite de la o SRL română 30.000 lei, venituri din diferențe de curs valutar 5.000 lei, reduceri comerciale primite ulterior facturării (cont 609) 2.000 lei. Cât impozit datorează pentru T1?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 28.09.2026, presupun o persoană juridică română care aplică în anul 2026 sistemul de impunere pe veniturile microîntreprinderilor (cotă unică, fără alte ajustări de bază impozabilă decât cele din datele întrebării) și calculez impozitul pentru trimestrul I 2026.*

Datele din întrebare: 2026-09-28 · data de referință aleasă: **2026-09-28** — Singura dată purtată de întrebare; faptul întrebat este impozitul pentru trimestrul I al anului fiscal 2026, iar cota și regulile de bază impozabilă sunt cele în vigoare în 2026.

> **Din veniturile trimestrului I se scad dividendele primite de la o persoană juridică română (30.000 lei) și veniturile din diferențe de curs valutar (5.000 lei), iar se adaugă reducerile comerciale primite ulterior facturării înregistrate în contul „609" (2.000 lei). Baza impozabilă a trimestrului I este 202.000 lei, iar impozitul pe veniturile microîntreprinderilor datorat pentru T1 este 2.020 lei.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul, pas cu pas — evaluat de cod, nu de model

- `baza = venituri_vanzari + reduceri_primite_609` = (200.000 + 2.000) = **202.000**
  - `venituri_vanzari` = 200.000 — FAPT_CAZ (din întrebare): „venituri din vânzări 200.000 lei”
  - `reduceri_primite_609` = 2.000 — FAPT_CAZ (din întrebare): „reduceri comerciale primite ulterior facturării (cont 609) 2.000 lei”
- `impozit = baza * cota` = (202.000 × 1%) = **2.020**
  - `cota` = 1% — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art51/alin1`: „Cota de impozit pe veniturile microîntreprinderilor este de 1%.”

- **Codul fiscal (Legea 227/2015) art. 53 alin. (1)** — `cod_fiscal_227_2015_consolidat#art53/alin1` · valabil din nedovedit
  > Baza impozabilă a impozitului pe veniturile microîntreprinderilor o constituie veniturile din orice sursă, din care se scad:
- **Codul fiscal (Legea 227/2015) art. 51 alin. (1)** — `cod_fiscal_227_2015_consolidat#art51/alin1` · valabil din 2026-01-01
  > Cota de impozit pe veniturile microîntreprinderilor este de 1%.
- **Codul fiscal (Legea 227/2015) art. 53 alin. (1) lit. n)** — `cod_fiscal_227_2015_consolidat#art53/alin1/litn` · valabil din 2020-12-24
  > dividendele primite de la o persoană juridică română. ...
- **Codul fiscal (Legea 227/2015) art. 53 alin. (1) lit. h)** — `cod_fiscal_227_2015_consolidat#art53/alin1/lith` · valabil din nedovedit
  > veniturile din diferențe de curs valutar; ...
- **Codul fiscal (Legea 227/2015) art. 53 alin. (2)** — `cod_fiscal_227_2015_consolidat#art53/alin2` · valabil din nedovedit
  > Pentru determinarea impozitului pe veniturile microîntreprinderilor, la baza impozabilă determinată potrivit alin. (1) se adaugă următoarele:
- **Codul fiscal (Legea 227/2015) art. 53 alin. (2) lit. a)** — `cod_fiscal_227_2015_consolidat#art53/alin2/lita` · valabil din nedovedit
  > valoarea reducerilor comerciale primite ulterior facturării, înregistrate în contul "609", potrivit reglementărilor contabile aplicabile; ...

### Navigarea (10 pași, 6 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "baza impozabilă microîntreprinderi"}
2. `cauta` {"interogare": "cotele de impozitare pe veniturile microîntreprinderilor"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art53"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art51"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art53/alin1"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art51/alin1"}
7. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art53/alin2"}
8. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art53/alin2/lita"}
9. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art53/alin1/lith"}
10. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art53/alin1/litn"}

Apel: `claude-opus-5`, {'intrare': 12, 'iesire': 4562, 'cache_scriere': 11011, 'cache_citire': 71886} tokeni, $0.2189, 63 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond CORECT

> Baza impozabilă a T1 2026 este 202.000 lei (200.000 lei venituri din vânzări + 2.000 lei reduceri comerciale primite din contul 609; dividendele de la SRL română și veniturile din diferențe de curs valutar nu se includ în T1), iar impozitul datorat este 2.020 lei. [calcul: baza = venituri_vanzari + reduceri_609 = 202.000; impozit = baza * cota = 2.020]

## Cheia

- 2.020 lei (bază 202.000 = 235.000 − 30.000 dividende − 5.000 dif. curs + 2.000 cont 609; × 1%)
- temei: Cod fiscal art. 53 alin. (1) partea introductivă, lit. h) și lit. n); art. 53 alin. (2) lit. a); art. 51 alin. (1) (mod. OUG 89/2025); art. 56 alin. (1)
