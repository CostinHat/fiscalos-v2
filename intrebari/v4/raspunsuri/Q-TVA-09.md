# Q-TVA-09 — CALCUL

**Întrebarea:** Un restaurant emite în 2026 o notă cu mâncare 800 lei bază și vin 200 lei bază. Cât TVA colectează în total?

## Stratul de navigare (v4) — NU POT RĂSPUNDE

*La data de referință 28.09.2026, presupun un restaurant persoană impozabilă înregistrată în scopuri de TVA în România, care prestează servicii de restaurant în regim normal de taxare (nu import prin mecanismul special), consumul fiind la fața locului, iar vinul fiind băutură alcoolică.*

Motiv: VERIFICAREA MECANICA a respins propunerea modelului: valoarea legala '200' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare)

### Calculul — evaluat de cod, nu de model

- `tva_mancare = baza_mancare * cota_redusa` → **88**
  - `baza_mancare` = 800 — din întrebare: „mâncare 800 lei bază”
  - `cota_redusa` = 11% — din `cod_fiscal_227_2015_consolidat#art291/alin2`: „Cota redusă de 11% se aplică asupra bazei de impozitare pentru următoarele prestări de servicii și/sau livrări de bunuri:”
- `tva_vin = baza_vin * cota_standard` → **42**
  - `baza_vin` = 200 — din întrebare: „vin 200 lei bază”
  - `cota_standard` = 21% — din `cod_fiscal_227_2015_consolidat#art291/alin1`: „iar nivelul acesteia este 21%”
- `total_tva = tva_mancare + tva_vin` → **130**

- **Codul fiscal (Legea 227/2015) art. 291 alin. (2) lit. n)** — `cod_fiscal_227_2015_consolidat#art291/alin2/litn` · valabil din 2025-08-01
  > serviciile de restaurant și de catering, cu excepția băuturilor alcoolice, precum și a băuturilor nealcoolice care se încadrează la codul NC 2202.
- **Codul fiscal (Legea 227/2015) art. 291 alin. (2)** — `cod_fiscal_227_2015_consolidat#art291/alin2` · valabil din nedovedit
  > Cota redusă de 11% se aplică asupra bazei de impozitare pentru următoarele prestări de servicii și/sau livrări de bunuri:
- **Codul fiscal (Legea 227/2015) art. 291 alin. (1)** — `cod_fiscal_227_2015_consolidat#art291/alin1` · valabil din 2025-08-01
  > Cota standard se aplică asupra bazei de impozitare pentru operațiunile impozabile care nu sunt scutite de taxă sau care nu sunt supuse cotei reduse, iar nivelul acesteia este 21%.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art315^3/alin4` — Excepția privește exclusiv importurile de bunuri realizate în cadrul mecanismului special pentru declararea și plata TVA la import; nu se aplică prestării de servicii de restaurant în România.
- derogare tratată: `legea_296_2023_masuri_fiscal_bugetare_asigurarea_sustenabilitatii#artV/alin1` — Derogarea vizează art. 291 alin. (2) lit. m) pct. 3 (locuințe), nu lit. n) privind serviciile de restaurant și catering.

### Navigarea (6 pași, 5 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Cotele"}
2. `cauta` {"interogare": "servicii de restaurant și de catering cota redusă băuturi alcoolice"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art291/alin2/litn"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art291"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art291/alin1"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art315^3/alin4"}

Apel: `claude-opus-5`, {'intrare': 10, 'iesire': 2892, 'cache_scriere': 5494, 'cache_citire': 43414} tokeni, $0.1284, 42 s

Pe fond: **NU POT** — VERIFICAREA MECANICA a respins propunerea modelului: valoarea legala '200' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare)

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți conțin doar reguli privind baza de impozitare (art. 286), rambursarea soldului negativ, deducerea și regimuri speciale, dar niciun atom nu conține cotele de TVA aplicabile serviciilor de restaurant, respectiv băuturilor alcoolice. În plus, determinarea TVA total ar presupune aplicarea unor cote asupra bazelor din speță și însumarea rezultatelor, adică un calcul al cărui rezultat nu apare literal în niciun atom primit. Prin urmare mă abțin.

## Cheia

- 130 lei (800 × 11% = 88 lei; 200 × 21% = 42 lei — băuturile alcoolice sunt excluse de la cota redusă)
- temei: Cod fiscal art. 291 alin. (2) lit. n) și alin. (1), forma modificată de Legea 141/2025 art. II pct. 42
