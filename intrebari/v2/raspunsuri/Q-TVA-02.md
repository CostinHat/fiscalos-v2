# Q-TVA-02 — PARAMETRU

**Întrebarea:** Care este plafonul cifrei de afaceri anuale sub care o persoană impozabilă stabilită în România poate aplica regimul special de scutire pentru întreprinderi mici în 2026?

## Stratul semantic (motorul nou) — RĂSPUNS

*La data de referință 28.09.2026, pentru o persoană impozabilă stabilită în România conform art. 266 alin. (2) lit. a), care aplică regimul special de scutire de TVA pentru întreprinderi mici (presupun operațiuni interne, fără opțiune pentru regimul normal de taxare și fără aplicarea scutirii în alte state membre).*

> **Plafonul este de 395.000 lei cifră de afaceri anuală, declarată sau realizată.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 310 alin. (1)** — `cod_fiscal_227_2015_consolidat#art310/alin1` · valabil din 2025-09-01
  > Persoana impozabilă stabilită în România conform art. 266 alin. (2) lit. a) , a cărei cifră de afaceri anuală, declarată sau realizată, nu depășește plafonul de 395.000 lei, poate aplica scutirea de taxă, denumită în continuare regim special de scutire
- **Codul fiscal (Legea 227/2015) art. 310 alin. (6)** — `cod_fiscal_227_2015_consolidat#art310/alin6~2` · valabil din 2025-09-01
  > Persoana impozabilă care aplică regimul special de scutire și a cărei cifră de afaceri, prevăzută la alin. (2) , depășește plafonul de scutire prevăzut la alin. (1) trebuie să solicite înregistrarea în scopuri de TVA, conform art. 316 , cel târziu la data depășirii plafonului.

Apel: `claude-opus-5`, {'intrare': 4029, 'iesire': 667, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0376, 10.2 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **100.000 euro**

Motiv: valoarea de forma cerută (suma) din atomul care poarta o asemenea valoare si potriveste cel mai bine cuvintele rare ale intrebarii (scor local 39.5)

- **Codul fiscal (Legea 227/2015) art. 310^1 alin. (1)** — `cod_fiscal_227_2015_consolidat#art310^1/alin1` · valabil din nedovedit
  > O persoană impozabilă stabilită în România conform art. 266 alin. (2) lit. a) poate aplica regimul special de scutire pentru întreprinderile mici în alte state membre dacă îndeplinește următoarele condiții: a) cifra de afaceri anuală la nivelul Uniunii Europene a respectivei persoane impozabile nu depășește 100.000 euro în anul în care solicită acordarea scutirii și în anul calendaristic precedent; ...

Pe fond: **GREȘIT** — faptul principal al cheii (['395.000 lei']) nu e in raspuns; articolul citat [('cf', '310^1')] nu e printre cele ale cheii [('cf', '310'), ('cf', 'I')]

## Cheia

- răspuns așteptat: 395.000 lei
- temei așteptat: Cod fiscal art. 310 alin. (1), forma modificată de OG 22/2025 art. I pct. 11, în vigoare de la 01.09.2025

