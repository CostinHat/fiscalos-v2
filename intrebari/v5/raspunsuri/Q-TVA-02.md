# Q-TVA-02 — PARAMETRU

**Întrebarea:** Care este plafonul cifrei de afaceri anuale sub care o persoană impozabilă stabilită în România poate aplica regimul special de scutire pentru întreprinderi mici în 2026?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 2026-09-28, presupun o persoană impozabilă stabilită în România conform art. 266 alin. (2) lit. a), care nu utilizează regimuri speciale de tip one-stop-shop pentru operațiunile de la art. 315^1 alin. (1) lit. c) și d), și care verifică plafonul regimului special de scutire pentru întreprinderi mici (TVA) în anul 2026.*

Datele din întrebare: 2026-09-28 · data de referință aleasă: **2026-09-28** — Singura dată purtată de întrebare, corespunzând anului 2026 pentru care se cere plafonul.

> **Plafonul este de 395.000 lei cifră de afaceri anuală, declarată sau realizată; sub acest plafon persoana impozabilă stabilită în România poate aplica regimul special de scutire pentru întreprinderi mici.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 310 alin. (1)** — `cod_fiscal_227_2015_consolidat#art310/alin1` · valabil din 2025-09-01
  > Persoana impozabilă stabilită în România conform art. 266 alin. (2) lit. a) , a cărei cifră de afaceri anuală, declarată sau realizată, nu depășește plafonul de 395.000 lei, poate aplica scutirea de taxă, denumită în continuare regim special de scutire
- **Codul fiscal (Legea 227/2015) art. 310 alin. (6)** — `cod_fiscal_227_2015_consolidat#art310/alin6` · valabil din 2025-09-01
  > Persoana impozabilă care aplică regimul special de scutire și a cărei cifră de afaceri, prevăzută la alin. (2) , depășește plafonul de scutire prevăzut la alin. (1) trebuie să solicite înregistrarea în scopuri de TVA
- derogare tratată: `cod_fiscal_227_2015_consolidat#art315^1/alin4/litc` — Excepția vizează doar persoanele care utilizează regimurile speciale de la art. 315^1 pentru operațiunile prevăzute la alin. (1) lit. c) și d); întrebarea nu descrie astfel de operațiuni, deci excepția nu schimbă plafonul general de 395.000 lei.

### Navigarea (4 pași, 4 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "întreprinderi mici"}
2. `cauta` {"interogare": "regimul special de scutire pentru întreprinderile mici plafon cifra de afaceri"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art310/alin1"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art315^1/alin4/litc"}

Apel: `claude-opus-5`, {'intrare': 8, 'iesire': 1562, 'cache_scriere': 4345, 'cache_citire': 35559} tokeni, $0.0840, 23 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond CORECT

> Plafonul este de 395.000 lei cifră de afaceri anuală, declarată sau realizată.

## Cheia

- 395.000 lei
- temei: Cod fiscal art. 310 alin. (1), forma modificată de OG 22/2025 art. I pct. 11, în vigoare de la 01.09.2025
