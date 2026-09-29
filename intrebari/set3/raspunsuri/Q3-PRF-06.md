# Q3-PRF-06 — CALCUL

**Întrebarea:** SRL plătitoare de impozit pe profit (nu e microîntreprindere; cifra de afaceri 2025 sub 50 mil. euro; fără pierderi de recuperat). La inventarul din 2026 constată o lipsă neimputabilă de mărfuri cu costul de 10.000 lei; mărfurile nu erau asigurate, iar lipsa nu provine din calamitate/forță majoră, degradare cu dovada distrugerii sau expirare. Pentru lipsă a ajustat (anulat) TVA dedusă la achiziție, de 2.100 lei, înregistrată pe cheltuieli. Profitul contabil 2026 înainte de impozit (care include aceste cheltuieli) este 88.000 lei și nu există alte ajustări fiscale sau sume de scăzut din impozit. Cât impozit pe profit datorează pentru 2026?

## RĂSPUNS

> **Cheltuiala cu lipsa neimputabilă de mărfuri de 10.000 lei și TVA aferentă de 2.100 lei sunt nedeductibile (nu se încadrează în niciuna dintre situațiile de deductibilitate: calamitate/forță majoră, bunuri asigurate, degradare calitativă cu dovada distrugerii, produse alimentare/agroalimentare sau termen de valabilitate depășit). Profitul impozabil pentru 2026 este 100.100 lei, iar impozitul pe profit datorat este 16.016 lei. [calcul: profit_impozabil = profit_contabil + cheltuiala_lipsa + cheltuiala_tva_ajustata = ((88.000 + 10.000) + 2.100) = 100.100; impozit = profit_impozabil * cota = (100.100 × 16%) = 16.016] [data de referință: 28.09.2026 — Faptul întrebat este impozitul pe profit datorat pentru anul fiscal 2026 (lipsa constatată la inventarul din 2026), deci se aplică legislația în vigoare în 2026; cifra de afaceri 2025 este doar o premisă pentru excluderea impozitului minim.]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- `profit_impozabil = profit_contabil + cheltuiala_lipsa + cheltuiala_tva_ajustata` = ((88.000 + 10.000) + 2.100) = **100.100**
- `impozit = profit_impozabil * cota` = (100.100 × 16%) = **16.016**
- **Codul fiscal (Legea 227/2015) art. 25 alin. (3) lit. c)** — `cod_fiscal_227_2015_consolidat#art25/alin3/litc~2`
  > cheltuielile privind bunurile de natura stocurilor sau a mijloacelor fixe amortizabile constatate lipsă din gestiune ori degradate, neimputabile, precum și taxa pe valoarea adăugată aferentă, dacă aceasta este datorată potrivit prevederilor titlului VII . Aceste cheltuieli sunt deductibile în următoarele situații/condiții:
- **Codul fiscal (Legea 227/2015) art. 17** — `cod_fiscal_227_2015_consolidat#art17`
  > Cota de impozit pe profit care se aplică asupra profitului impozabil este de 16%.
- **Codul fiscal (Legea 227/2015) art. 19 alin. (1)** — `cod_fiscal_227_2015_consolidat#art19/alin1`
  > Rezultatul fiscal se calculează ca diferență între veniturile și cheltuielile înregistrate conform reglementărilor contabile aplicabile, din care se scad veniturile neimpozabile și deducerile fiscale și la care se adaugă cheltuielile nedeductibile.
- **Codul fiscal (Legea 227/2015) art. 25 alin. (3) lit. c) pct. 7** — `cod_fiscal_227_2015_consolidat#art25/alin3/litc~2/pct7`
  > alte bunuri decât cele aflate în situațiile/condițiile prevăzute la pct. 1-6 , dacă termenul de valabilitate/expirare este depășit, potrivit legii;

Navigare: 10 pași, 9 ture; {'intrare': 18, 'iesire': 5178, 'cache_scriere': 26630, 'cache_citire': 110543} tokeni; $0.3513; 87 s

Cauza (dacă NU POT): RASPUNS

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## Cheia

- 16.016 lei. Cheltuielile cu stocurile constatate lipsă, neimputabile, și TVA aferentă sunt nedeductibile (nu se încadrează în excepțiile pct. 1–7): 10.000 + 2.100 = 12.100 lei cheltuieli nedeductibile. Profit impozabil = 88.000 + 12.100 = 100.100 lei. Impozit = 100.100 × 16% = 16.016 lei.
- temei: Cod fiscal art. 25 alin. (4) lit. c); art. 17
