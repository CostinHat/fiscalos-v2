# Q-TVA-07 — PROCEDURA

**Întrebarea:** O firmă înregistrată în scopuri de TVA, cu perioadă fiscală lunară, nu a avut nicio operațiune în ianuarie 2026. Trebuie să depună D394 pentru ianuarie și până când?

## Stratul semantic — NU POT RĂSPUNDE

*La data de referință 31.01.2026, presupun o persoană impozabilă stabilită în România, înregistrată în scopuri de TVA conform art. 316, cu perioadă fiscală lunară și fără operațiuni în luna ianuarie 2026; întrebarea vizează obligația de depunere și termenul declarației informative D394.*

Motiv: modelul s-a abţinut: Niciunul dintre atomii primiți nu reglementează declarația informativă privind livrările/prestările și achizițiile efectuate pe teritoriul național (D394): nu există în context nicio prevedere despre obligativitatea depunerii ei în lipsa operațiunilor și nici despre termenul de depunere. Atomii disponibili privesc înregistrarea în scopuri de TVA, dreptul de deducere, soldul sumei negative și rambursarea, iar singurul termen prezent (data de 25 a lunii următoare) se referă la declarația beneficiarului unui transfer de active neînregistrat în scopuri de TVA, situație diferită de cea din întrebare. Prin urmare nu pot răspunde fără a folosi surse din afara contextului.


Apel: `claude-opus-5`, {'intrare': 4601, 'iesire': 486, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0361

Pe fond: **NU POT** — modelul s-a abţinut: Niciunul dintre atomii primiți nu reglementează declarația informativă privind livrările/prestările și achizițiile efectuate pe teritoriul național (D394): nu există în context ni

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-01-31 (luna, din "ianuarie 2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **316 , și nu se va înregistra în scopuri de TVA ca urmare a transferului, trebuie să depună, până la data de 25 inclusiv a lunii următoare celei în care a avut loc transferul, o declarație privind sumele rezultate ca urmare a livrărilor/ajustărilor taxei pe valoarea adăugată efectuate conform art.**

Motiv: D15: fraza care conţine un fapt de forma cerută (termen) si potriveste cel mai bine intrebarea (scor local 23.1)

- **Codul fiscal (Legea 227/2015) art. 324 alin. (8)** — `cod_fiscal_227_2015_consolidat#art324/alin8` · valabil din nedovedit
  > Persoana impozabilă care este beneficiar al transferului de active prevăzut la art. 270 alin. (7) , care nu este înregistrată în scopuri de TVA, conform art. 316 , și nu se va înregistra în scopuri de TVA ca urmare a transferului, trebuie să depună, până la data de 25 inclusiv a lunii următoare celei în care a avut loc transferul, o declarație privind sumele rezultate ca urmare a livrărilor/ajustărilor taxei pe valoarea adăugată efectuate conform art. 270 alin. (4) , art. 304 , 305 sau 332 .

Pe fond: **GREȘIT** — faptul principal al cheii (['28.02.2026']) nu e in raspuns; articolul citat [('cf', '324')] nu e printre cele ale cheii [('opanaf_3769_2015', 'pct2'), ('cpf', '75')]

## Cheia

- Da, se depune și fără operațiuni. Termen nominal 28.02.2026, care cade sâmbătă → termen efectiv luni, 02.03.2026.
- temei: OPANAF 3769/2015 anexa 2 pct. 2 (forma OPANAF 2194/2025); CPF art. 75 (calculul termenelor după Codul de procedură civilă)
