# Q-TVA-07 — PROCEDURA

**Întrebarea:** O firmă înregistrată în scopuri de TVA, cu perioadă fiscală lunară, nu a avut nicio operațiune în ianuarie 2026. Trebuie să depună D394 pentru ianuarie și până când?

## Stratul semantic (motorul nou) — NU POT RĂSPUNDE

*La data de referință 31 ianuarie 2026, presupun o persoană impozabilă stabilită în România, înregistrată în scopuri de TVA conform art. 316, cu perioadă fiscală lunară, fără operațiuni în luna ianuarie 2026, și analizez obligația de depunere a declarației informative privind livrările/prestările și achizițiile pe teritoriul național (D394) și termenul acesteia.*

Motiv: modelul s-a abţinut: Atomii primiți se referă la dreptul de deducere, sumele negative de TVA, rambursări și decontul de taxă, dar niciunul nu conține regula privind declarația informativă D394 (obligația de depunere, situația lipsei operațiunilor și termenul de depunere). Fără un atom care reglementează această declarație nu pot stabili nici dacă există obligația de depunere pentru ianuarie 2026, nici termenul.


Apel: `claude-opus-5`, {'intrare': 5160, 'iesire': 340, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0351, 8.0 s

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți se referă la dreptul de deducere, sumele negative de TVA, rambursări și decontul de taxă, dar niciunul nu conține regula privind declarația informativă D394 (obliga

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-01-31 (luna, din "ianuarie 2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **316 , și nu se va înregistra în scopuri de TVA ca urmare a transferului, trebuie să depună, până la data de 25 inclusiv a lunii următoare celei în care a avut loc transferul, o declarație privind sumele rezultate ca urmare a livrărilor/ajustărilor taxei pe valoarea adăugată efectuate conform art.**

Motiv: D15: fraza care conţine un fapt de forma cerută (termen) si potriveste cel mai bine intrebarea (scor local 22.8)

- **Codul fiscal (Legea 227/2015) art. 324 alin. (8)** — `cod_fiscal_227_2015_consolidat#art324/alin8` · valabil din nedovedit
  > Persoana impozabilă care este beneficiar al transferului de active prevăzut la art. 270 alin. (7) , care nu este înregistrată în scopuri de TVA, conform art. 316 , și nu se va înregistra în scopuri de TVA ca urmare a transferului, trebuie să depună, până la data de 25 inclusiv a lunii următoare celei în care a avut loc transferul, o declarație privind sumele rezultate ca urmare a livrărilor/ajustărilor taxei pe valoarea adăugată efectuate conform art. 270 alin. (4) , art. 304 , 305 sau 332 .

Pe fond: **GREȘIT** — faptul principal al cheii (['28.02.2026']) nu e in raspuns; articolul citat [('cf', '324')] nu e printre cele ale cheii [('opanaf_3769_2015', 'pct2'), ('cpf', '75')]

## Cheia

- răspuns așteptat: Da, se depune și fără operațiuni. Termen nominal 28.02.2026, care cade sâmbătă → termen efectiv luni, 02.03.2026.
- temei așteptat: OPANAF 3769/2015 anexa 2 pct. 2 (forma OPANAF 2194/2025); CPF art. 75 (calculul termenelor după Codul de procedură civilă)

