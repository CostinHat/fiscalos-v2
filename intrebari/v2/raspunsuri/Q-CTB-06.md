# Q-CTB-06 — CAPCANA

**Întrebarea:** Societatea estimează pierderi din exploatare de 200.000 lei în 2027. Poate constitui la 31.12.2026 un provizion pentru ele?

## Stratul semantic (motorul nou) — RĂSPUNS

*La data de referință 31.12.2026, presupun o entitate care aplică reglementările contabile conforme cu directivele europene (OMFP 1802/2014), care întocmește situații financiare anuale la 31.12.2026 și care ar dori să recunoască un provizion pentru pierderi din exploatare estimate a se produce în exercițiul următor (2027), fără să existe un contract cu titlu oneros sau altă obligație asumată.*

> **Nu. Pierderile din exploatare estimate pentru anul următor nu îndeplinesc condițiile de recunoaștere a unui provizion (nu există o obligație curentă generată de un eveniment anterior), deci nu se poate constitui provizionul la 31.12.2026. Previzionarea unor astfel de pierderi indică însă că activele de exploatare ar putea fi depreciate, iar entitatea trebuie să le testeze pentru depreciere.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **OMFP 1802/2014 art. 12 alin. (2)** — `omfp_1802_2014#art12/alin2~196` · valabil din nedovedit
  > ‐ o entitate are o obligație curentă generată de un eveniment anterior; ‐ este probabil ca o ieşire de resurse să fie necesară pentru a onora obligația respectivă; şi ‐ poate fi realizată o estimare credibilă a valorii obligației. Dacă aceste condiții nu sunt îndeplinite, nu va fi recunoscut un provizion.
- **OMFP 1802/2014 art. 12 alin. (2)** — `omfp_1802_2014#art12/alin2~196` · valabil din nedovedit
  > Previzionarea unor pierderi viitoare din exploatare indică faptul că anumite active de exploatare ar putea fi depreciate. Ca urmare, entitatea testează aceste active pentru depreciere.

Apel: `claude-opus-5`, {'intrare': 3438, 'iesire': 1769, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0622, 24.8 s

Pe fond: **GREȘIT** — articolul citat [('omfp_1802_2014', '12')] nu e printre cele ale cheii [('omfp_1802_2014', 'pct372'), ('omfp_1802_2014', 'pct374')]

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-12-31 (zi, din "31.12.2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: D15: intrebarea cere o JUDECATA (Da/Nu) - aplicarea unei reguli la faptele date. Motorul nu compune si nu aplica reguli; atasez regula cea mai bine potrivita, ca material, nu ca raspuns.


Pe fond: **NU POT** — D15: intrebarea cere o JUDECATA (Da/Nu) - aplicarea unei reguli la faptele date. Motorul nu compune si nu aplica reguli; atasez regula cea mai bine potrivita, ca material, nu ca raspuns.

## Cheia

- răspuns așteptat: Nu. Nu se recunosc provizioane pentru pierderi viitoare din exploatare (nu corespund definiției unei datorii); activele de exploatare se testează pentru depreciere.
- temei așteptat: OMFP 1802/2014, Reglementări contabile, pct. 372 alin. (1)-(2) coroborat cu pct. 374 alin. (1)

