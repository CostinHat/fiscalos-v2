# Q-TVA-08 — CALCUL

**Întrebarea:** O firmă cumpără în 2026 un autoturism (sub 3.500 kg, max. 9 locuri, nu intră în excepțiile legale) la 100.000 lei + TVA, folosit și în scop personal. Cât TVA poate deduce?

## Stratul de navigare v5 — RĂSPUNS

*La data de 2026-09-28, presupun o persoană impozabilă înregistrată în scopuri de TVA, cu drept de deducere integral în rest, care achiziționează în România un vehicul rutier motorizat cu masa sub 3.500 kg și maximum 9 scaune, neîncadrat în excepțiile legale, utilizat și în scop personal (deci nu exclusiv în scopul activității economice), achiziția fiind taxată cu cota standard de TVA.*

Datele din întrebare: 2026-09-28 · data de referință aleasă: **2026-09-28** — Achiziția are loc în 2026, singura dată din întrebare fiind 2026-09-28; dreptul de deducere se apreciază la data achiziției.

> **Dreptul de deducere este limitat la 50% din TVA aferentă achiziției. TVA facturată este 21.000 lei, iar TVA deductibilă este 10.500 lei.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul, pas cu pas — evaluat de cod, nu de model

- `tva_factura = baza_impozabila * cota_standard / 100` = ((100.000 × 21) ÷ 100) = **21.000**
  - `baza_impozabila` = 100.000 — FAPT_CAZ (din întrebare): „la 100.000 lei + TVA”
  - `cota_standard` = 21 — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art291/alin1`: „nivelul acesteia este 21%”
- `tva_deductibila = tva_factura * limita_deducere / 100` = ((21.000 × 50) ÷ 100) = **10.500**
  - `limita_deducere` = 50 — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art298/alin1`: „se limitează la 50% dreptul de deducere a taxei aferente cumpărării”

- **Codul fiscal (Legea 227/2015) art. 298 alin. (1)** — `cod_fiscal_227_2015_consolidat#art298/alin1` · valabil din nedovedit
  > se limitează la 50% dreptul de deducere a taxei aferente cumpărării, achiziției intracomunitare, importului, închirierii sau leasingului de vehicule rutiere motorizate și a taxei aferente cheltuielilor legate de vehiculele aflate în proprietatea sau în folosința persoanei impozabile, în cazul în care vehiculele nu sunt utilizate exclusiv în scopul activității economice.
- **Codul fiscal (Legea 227/2015) art. 291 alin. (1)** — `cod_fiscal_227_2015_consolidat#art291/alin1` · valabil din 2025-08-01
  > Cota standard se aplică asupra bazei de impozitare pentru operațiunile impozabile care nu sunt scutite de taxă sau care nu sunt supuse cotei reduse, iar nivelul acesteia este 21%.
- **Codul fiscal (Legea 227/2015) art. 298 alin. (2)** — `cod_fiscal_227_2015_consolidat#art298/alin2` · valabil din nedovedit
  > Restricția prevăzută la alin. (1) nu se aplică vehiculelor rutiere motorizate având o masă totală maximă autorizată care depășește 3.500 kg sau mai mult de 9 scaune, inclusiv scaunul șoferului.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art298/alin2` — Nu se aplică: vehiculul din speță are masa sub 3.500 kg și maximum 9 locuri, deci rămâne sub limitarea de 50%.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art298/alin3` — Nu se aplică: întrebarea precizează expres că vehiculul nu intră în categoriile exceptate de la alin. (1).
- derogare tratată: `cod_fiscal_227_2015_consolidat#art297` — Art. 298 alin. (1) este excepție de la regula generală de deducere din art. 297 și se aplică prioritar cazului (vehicul neutilizat exclusiv în scopul activității economice).

### Navigarea (4 pași, 4 ture)

1. `cauta` {"interogare": "limitarea special a dreptului de deducere 50% vehicule rutiere motorizate"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "limitări speciale ale dreptului de deducere"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art298/alin1"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art291/alin1"}

Apel: `claude-opus-5`, {'intrare': 8, 'iesire': 3318, 'cache_scriere': 5933, 'cache_citire': 39152} tokeni, $0.1396, 42 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond CORECT

> Poate deduce doar 50% din TVA aferentă achiziției, adică 10.500 lei (TVA facturată de 21.000 lei la cota standard de 21%). [calcul: tva_facturata = baza * cota / 100 = 21.000; tva_deductibila = tva_facturata * procent_limitare / 100 = 10.500]

## Cheia

- 10.500 lei (TVA 21.000 lei × 50%)
- temei: Cod fiscal art. 291 alin. (1) (cota 21%); art. 298 alin. (1)-(3)
