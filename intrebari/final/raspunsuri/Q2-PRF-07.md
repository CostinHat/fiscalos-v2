# Q2-PRF-07 — CALCUL

**Întrebarea:** SRL plătitoare de impozit pe profit (cifra de afaceri 2025 sub 50 mil. euro), anul fiscal 2026: cifra de afaceri 2.000.000 lei, profit impozabil 312.500 lei (sponsorizarea fiind deja adăugată ca cheltuială nedeductibilă). A acordat o sponsorizare de 12.000 lei unei asociații înscrise, la data contractului, în Registrul entităților/unităților de cult pentru care se acordă deduceri fiscale. Cât impozit pe profit datorează pentru 2026?

## Răspunsul — RĂSPUNS

*La data de referință 28.09.2026, presupun o societate română plătitoare de impozit pe profit în regim trimestrial/anual standard, cu cifră de afaceri în anul precedent sub 50.000.000 euro (deci fără impozit minim pe cifra de afaceri), fără credit fiscal extern, fără profit reinvestit scutit și fără sume de sponsorizare reportate din anii anteriori, care a acordat în 2026 o sponsorizare de 12.000 lei unei asociații înscrise la data contractului în Registrul entităților/unităților de cult pentru care se acordă deduceri fiscale.*

> **Impozitul pe profit datorat pentru 2026 este 40.000 lei: impozit pe profit brut 50.000 lei (16% aplicat profitului impozabil), din care se scade sponsorizarea în limita minimului dintre 0,75% din cifra de afaceri (15.000 lei) și 20% din impozitul pe profit datorat (10.000 lei), adică 10.000 lei; diferența de sponsorizare nescăzută (12.000 lei acordați minus creditul folosit) nu reduce impozitul anului. [calcul: impozit_brut = profit_impozabil * cota_impozit_profit = (312.500 × 16%) = 50.000; plafon_cifra_afaceri = cifra_de_afaceri * cota_sponsorizare_ca = (2.000.000 × 0,75%) = 15.000; plafon_impozit = impozit_brut * cota_sponsorizare_impozit = (50.000 × 20%) = 10.000; credit_sponsorizare = min(sponsorizare_acordata, min(plafon_cifra_afaceri, plafon_impozit)) = min(12.000, min(15.000, 10.000)) = 10.000; impozit_datorat = impozit_brut - credit_sponsorizare = (50.000 − 10.000) = 40.000] [data de referință: 28.09.2026 — Faptul întrebat este impozitul pe profit datorat pentru anul fiscal 2026; cifra de afaceri 2025 este doar criteriu de încadrare, astfel că se aplică legea în vigoare în 2026.]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- `impozit_brut = profit_impozabil * cota_impozit_profit` = (312.500 × 16%) = **50.000**
- `plafon_cifra_afaceri = cifra_de_afaceri * cota_sponsorizare_ca` = (2.000.000 × 0,75%) = **15.000**
- `plafon_impozit = impozit_brut * cota_sponsorizare_impozit` = (50.000 × 20%) = **10.000**
- `credit_sponsorizare = min(sponsorizare_acordata, min(plafon_cifra_afaceri, plafon_impozit))` = min(12.000, min(15.000, 10.000)) = **10.000**
- `impozit_datorat = impozit_brut - credit_sponsorizare` = (50.000 − 10.000) = **40.000**
- **Codul fiscal (Legea 227/2015) art. 25 alin. (3) lit. i)** — `cod_fiscal_227_2015_consolidat#art25/alin3/liti~2`
  > contribuabilii care efectuează sponsorizări și/sau acte de mecenat, potrivit prevederilor Legii nr. 32/1994 privind sponsorizarea, cu modificările și completările ulterioare, și ale Legii bibliotecilor nr. 334/2002, republicată, cu modificările și completările ulterioare, scad sumele aferente din impozitul pe profit datorat la nivelul valorii minime dintre următoarele:
- **Codul fiscal (Legea 227/2015) art. 25 alin. (3) lit. i) pct. 1** — `cod_fiscal_227_2015_consolidat#art25/alin3/liti~2/pct1`
  > valoarea calculată prin aplicarea a 0,75% la cifra de afaceri; pentru situațiile în care reglementările contabile aplicabile nu definesc indicatorul cifra de afaceri, această limită se determină potrivit normelor;
- **Codul fiscal (Legea 227/2015) art. 25 alin. (3) lit. i) pct. 2** — `cod_fiscal_227_2015_consolidat#art25/alin3/liti~2/pct2`
  > valoarea reprezentând 20% din impozitul pe profit datorat. În cazul sponsorizărilor efectuate către entități persoane juridice fără scop lucrativ, inclusiv unități de cult, sumele aferente acestora se scad din impozitul pe profit datorat, în limitele prevăzute de prezenta literă, doar dacă beneficiarul sponsorizării este înscris, la data încheierii contractului, în Registrul entităților/unităților de cult pentru care se acordă deduceri fiscale
- **Codul fiscal (Legea 227/2015) art. 17** — `cod_fiscal_227_2015_consolidat#art17`
  > Cota de impozitare Cota de impozit pe profit care se aplică asupra profitului impozabil este de 16%.

Navigare: 8 pași; `claude-opus-5`; {'intrare': 14, 'iesire': 6258, 'cache_scriere': 9064, 'cache_citire': 81948} tokeni; $0.2541; 93 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## Cheia

- 40.000 lei. Pas 1: impozit pe profit = 312.500 × 16% = 50.000 lei. Pas 2: limitele pentru sponsorizare: 0,75% × 2.000.000 = 15.000 lei; 20% × 50.000 = 10.000 lei; se aplică minimul = 10.000 lei. Pas 3: sponsorizarea de 12.000 lei se scade doar în limita de 10.000 lei; impozit datorat = 50.000 − 10.000 = 40.000 lei. Diferența de 2.000 lei de sponsorizare nu se scade din impozitul anului 2026. Impozitul minim pe cifra de afaceri nu e aplicabil (cifra de afaceri sub 50 mil. euro).
- temei: Cod fiscal art. 25 alin. (4) lit. i); art. 17; art. 18^1 alin. (1)
