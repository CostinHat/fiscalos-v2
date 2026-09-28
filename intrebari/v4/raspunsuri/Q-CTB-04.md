# Q-CTB-04 — REGULA

**Întrebarea:** Un mijloc fix corporal este pus în funcțiune pe 15 martie 2026. Din ce lună începe amortizarea contabilă?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 15.03.2026, pentru o entitate care aplică reglementările contabile OMFP 1802/2014 (contabilitate în partidă dublă), presupunând că imobilizarea corporală este recunoscută ca mijloc fix amortizabil pus în funcțiune la 15 martie 2026.*

> **Amortizarea contabilă se calculează începând cu luna următoare punerii în funcțiune, deci din aprilie 2026.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **OMFP 1802/2014 art. 12 alin. (2)** — `omfp_1802_2014#art12~2/alin2~122` · valabil din nedovedit
  > Amortizarea imobilizărilor corporale se calculează începând cu luna următoare punerii în funcțiune și până la recuperarea integrală a valorii lor.

### Navigarea (3 pași, 3 ture)

1. `cauta` {"interogare": "amortizarea începe luna următoare punerii în funcțiune"}
2. `cauta` {"interogare": "amortizarea contabilă începe luna următoare punerii în funcțiune mijloc fix"}
3. `deschide` {"id": "omfp_1802_2014#art12~2/alin2~122"}

Apel: `claude-opus-5`, {'intrare': 6, 'iesire': 1185, 'cache_scriere': 3224, 'cache_citire': 22087} tokeni, $0.0609, 21 s

Pe fond: **GREȘIT** — articolul citat [('omfp_1802_2014', '12')] nu e printre cele ale cheii [('omfp_1802_2014', 'pct238')]

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Întrebarea vizează amortizarea CONTABILĂ, care este reglementată de normele contabile, nu de Codul fiscal. Atomii primiți conțin exclusiv reguli privind amortizarea fiscală (art. 28 din Codul fiscal), iar unul dintre ei precizează expres că deducerile de amortizare se determină fără a lua în calcul amortizarea contabilă. Prin urmare, momentul începerii amortizării contabile nu rezultă din atomii furnizați; regula privind luna următoare punerii în funcțiune, prezentă în conte…

## Cheia

- Din aprilie 2026 (luna următoare punerii în funcțiune), până la recuperarea integrală a valorii.
- temei: OMFP 1802/2014, Reglementări contabile, pct. 238 alin. (2)
