# Q-TVA-09 — CALCUL

**Întrebarea:** Un restaurant emite în 2026 o notă cu mâncare 800 lei bază și vin 200 lei bază. Cât TVA colectează în total?

## Stratul de navigare v5 — NU POT RĂSPUNDE

*La data de referință 28.09.2026, presupun un restaurant persoană impozabilă înregistrată în scopuri de TVA în România, care prestează servicii de restaurant taxabile în regim normal, nota cuprinzând mâncare cu bază de impozitare 800 lei și vin (băutură alcoolică) cu bază de impozitare 200 lei.*

Datele din întrebare: 2026-09-28 · data de referință aleasă: **2026-09-28** — Singura dată din întrebare: operațiunea (nota emisă de restaurant) are loc în 2026.

Motiv: VERIFICAREA MECANICA a respins propunerea modelului: citatul NU e verbatim in atomul cod_fiscal_227_2015_consolidat#art291/alin2/litn; citatul NU e verbatim in atomul cod_fiscal_227_2015_consolidat#art291/alin2; citatul NU e verbatim in atomul cod_fiscal_227_2015_consolidat#art291/alin1

### Calculul, pas cu pas — evaluat de cod, nu de model

- `TVA_total = baza_mancare * cota_redusa + baza_vin * cota_standard` = ((800 × 11%) + (200 × 21%)) = **130**
  - `baza_mancare` = 800 — FAPT_CAZ (din întrebare): „mâncare 800 lei bază”
  - `cota_redusa` = 11% — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art291/alin2`: „Cota redusă de 11% se aplică asupra bazei de impozitare”
  - `baza_vin` = 200 — FAPT_CAZ (din întrebare): „vin 200 lei bază”
  - `cota_standard` = 21% — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art291/alin1`: „iar nivelul acesteia este 21%”

- **Codul fiscal (Legea 227/2015) art. 291 alin. (2) lit. n)** — `cod_fiscal_227_2015_consolidat#art291/alin2/litn` · valabil din 2025-08-01
  > serviciile de restaurant \u0219i de catering, cu excep\u021bia b\u0103uturilor alcoolice, precum \u0219i a b\u0103uturilor nealcoolice care se \u00eencadreaz\u0103 la codul NC 2202.
- **Codul fiscal (Legea 227/2015) art. 291 alin. (2)** — `cod_fiscal_227_2015_consolidat#art291/alin2` · valabil din nedovedit
  > Cota redus\u0103 de 11% se aplic\u0103 asupra bazei de impozitare pentru urm\u0103toarele prest\u0103ri de servicii \u0219i/sau livr\u0103ri de bunuri:
- **Codul fiscal (Legea 227/2015) art. 291 alin. (1)** — `cod_fiscal_227_2015_consolidat#art291/alin1` · valabil din 2025-08-01
  > Cota standard se aplic\u0103 asupra bazei de impozitare pentru opera\u021biunile impozabile care nu sunt scutite de tax\u0103 sau care nu sunt supuse cotei reduse, iar nivelul acesteia este 21%.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art315^3/alin4` — Excepția privește importurile de bunuri realizate în cadrul mecanismului special pentru declararea și plata TVA la import; cazul din întrebare este o prestare internă de servicii de restaurant, deci nu se aplică.
- derogare tratată: `legea_296_2023_masuri_fiscal_bugetare_asigurarea_sustenabilitatii#artV/alin1` — Derogarea vizează art. 291 alin. (2) lit. m) pct. 3, nu lit. n) privind serviciile de restaurant, deci nu se aplică cazului.

### Navigarea (6 pași, 5 ture, 1 reîncercare C23)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Cotele"}
2. `cauta` {"interogare": "servicii de restaurant și de catering cota redusă băuturi alcoolice"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art291/alin1"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art291/alin2/litn"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art291/alin2"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art315^3/alin4"}

Apel: `claude-opus-5`, {'intrare': 10, 'iesire': 4826, 'cache_scriere': 8129, 'cache_citire': 46597} tokeni, $0.1948, 64 s

Pe fond (comparator): **NU POT** — VERIFICAREA MECANICA a respins propunerea modelului: citatul NU e verbatim in atomul cod_fiscal_227_2015_consolidat#art291/alin2/litn; citatul NU e verbatim in atomul cod_fiscal_227_2015_consolidat#ar

## v4 — NU POT, pe fond NU POT

> VERIFICAREA MECANICA a respins propunerea modelului: valoarea legala '200' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare)

## Cheia

- 130 lei (800 × 11% = 88 lei; 200 × 21% = 42 lei — băuturile alcoolice sunt excluse de la cota redusă)
- temei: Cod fiscal art. 291 alin. (2) lit. n) și alin. (1), forma modificată de Legea 141/2025 art. II pct. 42
