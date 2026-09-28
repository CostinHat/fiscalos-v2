# Q-TVA-01 — PARAMETRU

**Întrebarea:** Care este cota standard de TVA aplicabilă în 2026?

## Stratul semantic (motorul nou) — RĂSPUNS

*La data de referință 28.09.2026, pentru operațiuni impozabile realizate în România care nu sunt scutite de taxă și nu intră sub incidența unei cote reduse, presupunând aplicarea regimului general de TVA din Codul fiscal.*

> **Cota standard de TVA este 21%.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 291 alin. (1)** — `cod_fiscal_227_2015_consolidat#art291/alin1` · valabil din 2025-08-01
  > Cota standard se aplică asupra bazei de impozitare pentru operațiunile impozabile care nu sunt scutite de taxă sau care nu sunt supuse cotei reduse, iar nivelul acesteia este 21%.

Apel: `claude-opus-5`, {'intrare': 6913, 'iesire': 294, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0427, 6.8 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **9%**

Motiv: valoarea de forma cerută (procent) din atomul care poarta o asemenea valoare si potriveste cel mai bine cuvintele rare ale intrebarii (scor local 15.8)

- **Codul fiscal (Legea 227/2015) art. 291 alin. (3^5) lit. d)** — `cod_fiscal_227_2015_consolidat#art291/alin3^5/litd` · valabil din 2023-01-01
  > să înscrie în actele juridice între vii care au ca obiect transferul dreptului de proprietate sau plata în avans pentru locuințele prevăzute la alin. (3) lit. c) pct. 3 cota de TVA aplicată, indiferent dacă TVA se aplică la preț sau este inclusă în preț. ... Notă ... Articolul III din LEGEA nr. 141 din 25 iulie 2025, publicată în MONITORUL OFICIAL nr. 699 din 25 iulie 2025 prevede: Articolul III (1) Persoana fizică, în mod individual sau în comun cu altă persoană fizică/alte persoane fizice, poate achiziționa în perioada 1 august 2025-31 iulie 2026 inclusiv o singură locuință cu cota redusă de…

Pe fond: **GREȘIT** — faptul principal al cheii (['21%']) nu e in raspuns

## Cheia

- răspuns așteptat: 21%
- temei așteptat: Legea 227/2015 (Cod fiscal) art. 291 alin. (1), forma modificată de Legea 141/2025 art. II pct. 42, în vigoare de la 01.08.2025

