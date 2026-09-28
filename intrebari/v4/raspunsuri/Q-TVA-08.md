# Q-TVA-08 — CALCUL

**Întrebarea:** O firmă cumpără în 2026 un autoturism (sub 3.500 kg, max. 9 locuri, nu intră în excepțiile legale) la 100.000 lei + TVA, folosit și în scop personal. Cât TVA poate deduce?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 28.09.2026, presupun o persoană impozabilă înregistrată în scopuri de TVA în România, cu drept de deducere integral pentru achiziții obișnuite, care cumpără în 2026 un autoturism cu masa totală maximă autorizată sub 3.500 kg și maximum 9 scaune, neîncadrat în categoriile exceptate, utilizat atât în scopul activității economice, cât și în scop personal, achiziția fiind taxată cu cota standard.*

> **Poate deduce doar 50% din TVA aferentă achiziției, adică 10.500 lei (TVA facturată de 21.000 lei la cota standard de 21%). [calcul: tva_facturata = baza * cota / 100 = 21.000; tva_deductibila = tva_facturata * procent_limitare / 100 = 10.500]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul — evaluat de cod, nu de model

- `tva_facturata = baza * cota / 100` → **21.000**
  - `baza` = 100.000 — din întrebare: „la 100.000 lei + TVA”
  - `cota` = 21 — din `cod_fiscal_227_2015_consolidat#art291/alin1`: „nivelul acesteia este 21%”
- `tva_deductibila = tva_facturata * procent_limitare / 100` → **10.500**
  - `procent_limitare` = 50 — din `cod_fiscal_227_2015_consolidat#art298/alin1`: „se limitează la 50% dreptul de deducere a taxei aferente cumpărării”

- **Codul fiscal (Legea 227/2015) art. 298 alin. (1)** — `cod_fiscal_227_2015_consolidat#art298/alin1` · valabil din nedovedit
  > Prin excepție de la prevederile art. 297 se limitează la 50% dreptul de deducere a taxei aferente cumpărării, achiziției intracomunitare, importului, închirierii sau leasingului de vehicule rutiere motorizate și a taxei aferente cheltuielilor legate de vehiculele aflate în proprietatea sau în folosința persoanei impozabile, în cazul în care vehiculele nu sunt utilizate exclusiv în scopul activității economice.
- **Codul fiscal (Legea 227/2015) art. 291 alin. (1)** — `cod_fiscal_227_2015_consolidat#art291/alin1` · valabil din 2025-08-01
  > Cota standard se aplică asupra bazei de impozitare pentru operațiunile impozabile care nu sunt scutite de taxă sau care nu sunt supuse cotei reduse, iar nivelul acesteia este 21%.
- **Codul fiscal (Legea 227/2015) art. 298 alin. (2)** — `cod_fiscal_227_2015_consolidat#art298/alin2` · valabil din nedovedit
  > Restricția prevăzută la alin. (1) nu se aplică vehiculelor rutiere motorizate având o masă totală maximă autorizată care depășește 3.500 kg sau mai mult de 9 scaune, inclusiv scaunul șoferului.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art298/alin2` — Excepția pentru vehiculele de peste 3.500 kg sau cu mai mult de 9 scaune nu se aplică: vehiculul din speță are sub 3.500 kg și maximum 9 locuri, deci limitarea la 50% rămâne aplicabilă.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art298/alin3` — Categoriile exceptate de la limitare (vehicule de intervenție, agenți de vânzări, taximetrie, mărfuri în scop comercial etc.) nu se aplică, întrucât întrebarea precizează expres că vehiculul nu intră în excepțiile legale.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art297` — Regula generală a dreptului de deducere este înlăturată în speță prin excepția expresă de la art. 298 alin. (1), care limitează deducerea la 50%.

### Navigarea (5 pași, 4 ture)

1. `cauta` {"interogare": "limitări speciale ale dreptului de deducere 50% vehicule rutiere motor"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Limitări speciale ale dreptului de deducere"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art298/alin1"}
4. `cauta` {"interogare": "cota standard TVA 21%"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art291/alin1"}

Apel: `claude-opus-5`, {'intrare': 8, 'iesire': 2533, 'cache_scriere': 7157, 'cache_citire': 37055} tokeni, $0.1266, 37 s

Pe fond: **GREȘIT** — articolul citat [('cf', '298')] nu e printre cele ale cheii [('cf', '291'), (None, '298')]

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți privesc înregistrarea în scopuri de TVA, rambursarea soldului sumei negative, plata TVA la import și anularea codului de TVA; niciunul nu conține regula privind limitarea dreptului de deducere a TVA pentru vehiculele rutieri motorizate utilizate și în scop personal. În plus, determinarea sumei deductibile ar necesita un calcul (aplicarea unei cote asupra bazei de 100.000 lei), rezultat care nu apare literal în niciun atom.

## Cheia

- 10.500 lei (TVA 21.000 lei × 50%)
- temei: Cod fiscal art. 291 alin. (1) (cota 21%); art. 298 alin. (1)-(3)
