# Q-CTB-06 — CAPCANA

**Întrebarea:** Societatea estimează pierderi din exploatare de 200.000 lei în 2027. Poate constitui la 31.12.2026 un provizion pentru ele?

## Stratul de navigare v5 — RĂSPUNS

*La data de 31.12.2026, presupunând o societate care aplică reglementările contabile conforme cu directivele europene (OMFP 1802/2014) și care dorește să înregistreze la închiderea exercițiului 2026 un provizion pentru pierderi din exploatare estimate a se produce în 2027, fără ca întrebarea să indice existența unui contract oneros sau a altei obligații prezente.*

Datele din întrebare: 2026-12-31, 2026-09-28 · data de referință aleasă: **2026-12-31** — Faptul întrebat este posibilitatea constituirii provizionului la închiderea exercițiului, adică la 31.12.2026; anul 2027 este doar perioada pierderilor estimate.

> **Nu. Pentru pierderile viitoare din exploatare estimate pentru 2027 nu se poate recunoaște un provizion la 31.12.2026, deoarece astfel de pierderi viitoare nu corespund definiției unei datorii și nu îndeplinesc criteriile de recunoaștere a provizioanelor. Previzionarea unor astfel de pierderi indică însă că activele de exploatare ar putea fi depreciate, astfel încât societatea trebuie să testeze aceste active pentru depreciere.**

Citatul decisiv (`omfp_1802_2014#anexa/pct372/alin1`):
> Nu se recunosc provizioane pentru pierderile viitoare din exploatare deoarece aceste pierderi viitoare nu corespund definiției unei datorii și nu sunt îndeplinite criteriile de recunoaștere a provizioanelor.

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **OMFP 1802/2014 anexa, pct. 372 alin. (1)** — `omfp_1802_2014#anexa/pct372/alin1` · valabil din nedovedit
  > Nu se recunosc provizioane pentru pierderile viitoare din exploatare deoarece aceste pierderi viitoare nu corespund definiției unei datorii și nu sunt îndeplinite criteriile de recunoaștere a provizioanelor.
- **OMFP 1802/2014 anexa, pct. 372 alin. (2)** — `omfp_1802_2014#anexa/pct372/alin2` · valabil din nedovedit
  > Previzionarea unor pierderi viitoare din exploatare indică faptul că anumite active de exploatare ar putea fi depreciate. Ca urmare, entitatea testează aceste active pentru depreciere.

### Navigarea (3 pași, 3 ture)

1. `cauta` {"interogare": "provizioanele nu pot fi constituite pentru pierderi viitoare din exploatare"}
2. `cuprins` {"act": "omfp_1802_2014_reglementari_consolidat", "filtru": "provizioane"}
3. `deschide` {"id": "omfp_1802_2014#anexa/pct372/alin1"}

Apel: `claude-opus-5`, {'intrare': 6, 'iesire': 1386, 'cache_scriere': 2174, 'cache_citire': 23291} tokeni, $0.0599, 27 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond GREȘIT

> Nu. Nu se recunosc provizioane pentru pierderile viitoare din exploatare, deoarece acestea nu corespund definiției unei datorii și nu îndeplinesc criteriile de recunoaștere a provizioanelor; previzionarea unor astfel de pierderi impune însă testarea pentru depreciere a activelor de exploatare.

## Cheia

- Nu. Nu se recunosc provizioane pentru pierderi viitoare din exploatare (nu corespund definiției unei datorii); activele de exploatare se testează pentru depreciere.
- temei: OMFP 1802/2014, Reglementări contabile, pct. 372 alin. (1)-(2) coroborat cu pct. 374 alin. (1)
