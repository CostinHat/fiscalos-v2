# Q-TVA-07 — PROCEDURA

**Întrebarea:** O firmă înregistrată în scopuri de TVA, cu perioadă fiscală lunară, nu a avut nicio operațiune în ianuarie 2026. Trebuie să depună D394 pentru ianuarie și până când?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 31.01.2026, pentru o persoană impozabilă înregistrată în scopuri de TVA în România, cu perioadă fiscală luna calendaristică, care în luna de raportare (ianuarie 2026) nu a efectuat operațiuni de natura celor declarate în formularul 394; presupun că societatea își păstrează calitatea de persoană înregistrată în scopuri de TVA și are obligația depunerii decontului lunar de TVA.*

> **Da, declarația 394 trebuie depusă și pentru perioada în care nu au fost realizate operațiuni de natura celor care fac obiectul declarației, la organul fiscal competent până în data de 25 inclusiv a lunii următoare încheierii perioadei de raportare (deci, pentru raportarea lunii ianuarie, până pe 25 a lunii următoare).**

Citatul decisiv (`opanaf_3769_2015_d394_baza#art12/alin21`):
> Declaraţia se depune la organul fiscal competent până în data de 25 inclusiv a lunii următoare încheierii perioadei de raportare declarate pentru depunerea decontului (lunar, trimestrial etc.), inclusiv dacă în această perioadă nu au fost realizate operaţiuni de natura celor care fac obiectul declaraţiei.

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **OPANAF 3769/2015 art. 12 alin. (21)** — `opanaf_3769_2015_d394_baza#art12/alin21` · valabil din nedovedit
  > Declaraţia se depune la organul fiscal competent până în data de 25 inclusiv a lunii următoare încheierii perioadei de raportare declarate pentru depunerea decontului (lunar, trimestrial etc.), inclusiv dacă în această perioadă nu au fost realizate operaţiuni de natura celor care fac obiectul declaraţiei.
- **OPANAF 3769/2015 art. 12 alin. (394)** — `opanaf_3769_2015_d394_baza#art12/alin394` · valabil din nedovedit
  > "Declaraţie informativă privind livrările/prestările şi achiziţiile efectuate pe teritoriul naţional de persoanele înregistrate în scopuri de TVA", cod MFP 14.13.01.02/f, denumită în continuare declaraţia (394)
- derogare tratată: `opanaf_3769_2015_d394_baza#art12/alin21` — Excepția din același text (depunerea pe formularul vechi pentru lunile ianuarie și februarie 2016 și înlocuirea lor până la 25 aprilie 2016) este o măsură tranzitorie pentru anul 2016 și nu se aplică raportării lunii ianuarie 2026. OPANAF 2194/2025 modifică doar anexele (modelul formularului), nu te…

### Navigarea (7 pași, 6 ture)

1. `cauta` {"interogare": "declarația informativă 394 se depune până la data de 30 inclusiv a lunii următoare"}
2. `cauta` {"interogare": "394 nu au desfășurat operațiuni nu se depune declarația"}
3. `cuprins` {"act": "opanaf_3769_2015_d394_baza", "filtru": ""}
4. `cuprins` {"act": "opanaf_2194_2025_d394", "filtru": ""}
5. `cauta` {"interogare": "declarația 394 livrări prestări achiziții efectuate pe teritoriul național termen de depunere"}
6. `deschide` {"id": "opanaf_3769_2015_d394_baza#art12/alin21"}
7. `deschide` {"id": "opanaf_2194_2025_d394#artI"}

Apel: `claude-opus-5`, {'intrare': 12, 'iesire': 2962, 'cache_scriere': 7311, 'cache_citire': 55885} tokeni, $0.1477, 49 s

Pe fond: **GREȘIT** — faptul principal al cheii (['28.02.2026']) nu e in raspuns; articolul citat [('opanaf_3769_2015', '12')] nu e printre cele ale cheii [('opanaf_3769_2015', 'pct2'), ('cpf', '75')]

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Niciunul dintre atomii primiți nu reglementează declarația informativă privind livrările/prestările și achizițiile efectuate pe teritoriul național (D394): nu există în context nicio prevedere despre obligativitatea depunerii ei în lipsa operațiunilor și nici despre termenul de depunere. Atomii disponibili privesc înregistrarea în scopuri de TVA, dreptul de deducere, soldul sumei negative și rambursarea, iar singurul termen prezent (data de 25 a lunii următoare) se referă la…

## Cheia

- Da, se depune și fără operațiuni. Termen nominal 28.02.2026, care cade sâmbătă → termen efectiv luni, 02.03.2026.
- temei: OPANAF 3769/2015 anexa 2 pct. 2 (forma OPANAF 2194/2025); CPF art. 75 (calculul termenelor după Codul de procedură civilă)
