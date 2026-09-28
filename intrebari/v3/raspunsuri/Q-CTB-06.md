# Q-CTB-06 — CAPCANA

**Întrebarea:** Societatea estimează pierderi din exploatare de 200.000 lei în 2027. Poate constitui la 31.12.2026 un provizion pentru ele?

## Stratul semantic — RĂSPUNS

*La data de referință 31.12.2026, presupun o societate comercială care aplică reglementările contabile conforme cu directivele europene (OMFP 1802/2014) și care dorește să recunoască în situațiile financiare ale exercițiului 2026 un provizion pentru pierderi din exploatare estimate a se produce în exercițiul următor, fără să invoce o obligație asumată față de un terț.*

> **Nu. Simpla estimare a unor pierderi viitoare din exploatare pentru 2027 nu permite recunoașterea unui provizion la 31.12.2026: un provizion se recunoaște doar dacă există o obligație curentă generată de un eveniment anterior, este probabilă o ieșire de resurse și valoarea poate fi estimată credibil; previzionarea de pierderi viitoare din exploatare obligă, în schimb, la testarea pentru depreciere a activelor de exploatare (ajustări pentru depreciere, nu provizion).**

Citatul decisiv (`omfp_1802_2014#artII/alin2~197`):
> Previzionarea unor pierderi viitoare din exploatare indică faptul că anumite active de exploatare ar putea fi depreciate. Ca urmare, entitatea testează aceste active pentru depreciere.

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **OMFP 1802/2014 art. II alin. (2)** — `omfp_1802_2014#artII/alin2~197` · valabil din nedovedit
  > Previzionarea unor pierderi viitoare din exploatare indică faptul că anumite active de exploatare ar putea fi depreciate. Ca urmare, entitatea testează aceste active pentru depreciere.
- **OMFP 1802/2014 art. II alin. (2)** — `omfp_1802_2014#artII/alin2~197` · valabil din nedovedit
  > Un provizion va fi recunoscut numai în momentul în care: – o entitate are o obligație curentă generată de un eveniment anterior; ... – este probabil ca o ieșire de resurse să fie necesară pentru a onora obligația respectivă; și ... – poate fi realizată o estimare credibilă a valorii obligației. ... Dacă aceste condiții nu sunt îndeplinite, nu va fi recunoscut un provizion.

Apel: `claude-opus-5`, {'intrare': 3475, 'iesire': 2328, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0765

Pe fond: **GREȘIT** — articolul citat [('omfp_1802_2014', 'II')] nu e printre cele ale cheii [('omfp_1802_2014', 'pct372'), ('omfp_1802_2014', 'pct374')]

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-12-31 (zi, din "31.12.2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: D15: intrebarea cere o JUDECATA (Da/Nu) - aplicarea unei reguli la faptele date. Motorul nu compune si nu aplica reguli; atasez regula cea mai bine potrivita, ca material, nu ca raspuns.


Pe fond: **NU POT** — D15: intrebarea cere o JUDECATA (Da/Nu) - aplicarea unei reguli la faptele date. Motorul nu compune si nu aplica reguli; atasez regula cea mai bine potrivita, ca material, nu ca raspuns.

## Cheia

- Nu. Nu se recunosc provizioane pentru pierderi viitoare din exploatare (nu corespund definiției unei datorii); activele de exploatare se testează pentru depreciere.
- temei: OMFP 1802/2014, Reglementări contabile, pct. 372 alin. (1)-(2) coroborat cu pct. 374 alin. (1)
