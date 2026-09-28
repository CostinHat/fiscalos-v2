# Q-TVA-02 — PARAMETRU

**Întrebarea:** Care este plafonul cifrei de afaceri anuale sub care o persoană impozabilă stabilită în România poate aplica regimul special de scutire pentru întreprinderi mici în 2026?

## Stratul semantic — RĂSPUNS

*La data de referință 28.09.2026, presupun o persoană impozabilă stabilită în România conform art. 266 alin. (2) lit. a), care nu aplică un regim special de tipul celui de la art. 315^1 și care verifică plafonul pentru regimul special de scutire pentru întreprinderi mici (TVA).*

> **Plafonul cifrei de afaceri anuale, declarate sau realizate, este de 395.000 lei: sub acest plafon persoana impozabilă stabilită în România poate aplica regimul special de scutire pentru întreprinderi mici.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 310 alin. (1)** — `cod_fiscal_227_2015_consolidat#art310/alin1` · valabil din 2025-09-01
  > a cărei cifră de afaceri anuală, declarată sau realizată, nu depășește plafonul de 395.000 lei, poate aplica scutirea de taxă, denumită în continuare regim special de scutire
- derogare tratată: `cod_fiscal_227_2015_consolidat#art315^1/alin4/litc` — Derogarea vizează doar persoanele care aplică regimul special de la art. 315^1, pentru operațiunile prevăzute la alin. (1) lit. c) și d), care nu se cuprind în cifra de afaceri de referință; întrebarea privește o persoană impozabilă obișnuită stabilită în România, fără astfel de operațiuni, deci nu …

Apel: `claude-opus-5`, {'intrare': 3696, 'iesire': 863, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0410

Pe fond: **CORECT** — faptul principal si articolul coincid

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: C17 (b): atomul pe care as raspunde are 1 derogari/exceptii/modificari valabile la data intrebarii (ex. cod_fiscal_227_2015_consolidat#art315^1/alin4/litc: "prin excepție de la art. 310"); motorul lexical nu le poate trata, deci se abţine.

- **Codul fiscal (Legea 227/2015) art. 310 alin. (1)** — `cod_fiscal_227_2015_consolidat#art310/alin1` · valabil din 2025-09-01
  > Persoana impozabilă stabilită în România conform art. 266 alin. (2) lit. a) , a cărei cifră de afaceri anuală, declarată sau realizată, nu depășește plafonul de 395.000 lei, poate aplica scutirea de taxă, denumită în continuare regim special de scutire, pentru operațiunile prevăzute la art. 268 alin. (1) , cu excepția livrărilor intracomunitare de mijloace de transport noi, scutite conform art. 294 alin. (2) lit. b) .

Pe fond: **NU POT** — C17 (b): atomul pe care as raspunde are 1 derogari/exceptii/modificari valabile la data intrebarii (ex. cod_fiscal_227_2015_consolidat#art315^1/alin4/litc: "prin excepție de la art. 310"); motorul lex

## Cheia

- 395.000 lei
- temei: Cod fiscal art. 310 alin. (1), forma modificată de OG 22/2025 art. I pct. 11, în vigoare de la 01.09.2025
