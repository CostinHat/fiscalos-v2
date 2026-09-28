# Q-CPF-09 — CAPCANA

**Întrebarea:** O firmă a plătit cu 60 de zile întârziere o amendă contravențională de 2.000 lei aplicată de ANAF. Cât datorează ca dobânzi și penalități de întârziere pentru această întârziere?

## Stratul semantic (motorul nou) — RĂSPUNS

*La data de referință 28.09.2026, pentru o persoană juridică ce a achitat cu întârziere o amendă contravențională aplicată de ANAF, presupun că este vorba de o sumă datorată cu titlu de amendă (obligație nefiscală principală de tip amendă), fără alte obligații fiscale principale restante.*

> **Nu datorează nimic: pentru sumele datorate cu titlu de amenzi de orice fel nu se datorează dobânzi și penalități de întârziere, indiferent de durata întârzierii.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul de procedură fiscală (Legea 207/2015) art. 173 alin. (2)** — `legea_207_2015_consolidat#art173/alin2` · valabil din nedovedit
  > Nu se datorează dobânzi și penalități de întârziere pentru sumele datorate cu titlu de amenzi de orice fel, obligații fiscale accesorii stabilite potrivit legii, cheltuieli de executare silită, cheltuieli judiciare, sumele confiscate
- **Codul de procedură fiscală (Legea 207/2015) art. 173 alin. (1)** — `legea_207_2015_consolidat#art173/alin1` · valabil din nedovedit
  > Pentru neachitarea la termenul de scadență de către debitor a obligațiilor fiscale principale, se datorează după acest termen dobânzi și penalități de întârziere.

Apel: `claude-opus-5`, {'intrare': 2054, 'iesire': 452, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0223, 8.9 s

Pe fond: **GREȘIT** — faptul principal al cheii (['0 lei']) nu e in raspuns

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-09-28 (implicita (ziua intrebarii)). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: D15: intrebarea cere un fapt de forma 'procent', si niciun atom gasit (nici copiii lor) nu conţine unul


Pe fond: **NU POT** — D15: intrebarea cere un fapt de forma 'procent', si niciun atom gasit (nici copiii lor) nu conţine unul

## Cheia

- răspuns așteptat: 0 lei: nu se datorează dobânzi și penalități de întârziere pentru amenzi de orice fel (nici pentru accesorii, cheltuieli de executare etc.).
- temei așteptat: Legea 207/2015 art. 173 alin. (2)

