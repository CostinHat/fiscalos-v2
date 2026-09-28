# Q-CTB-06 — CAPCANA

**Întrebarea:** Societatea estimează pierderi din exploatare de 200.000 lei în 2027. Poate constitui la 31.12.2026 un provizion pentru ele?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 31.12.2026, pentru o societate care ține contabilitatea potrivit reglementărilor contabile privind situațiile financiare anuale individuale (OMFP 1802/2014), presupunând că este vorba de estimarea unor pierderi din exploatare aferente exercițiului următor (2027), fără a exista un contract oneros sau o obligație prezentă rezultată dintr-un eveniment trecut.*

> **Nu. Nu se recunosc provizioane pentru pierderile viitoare din exploatare, deoarece acestea nu corespund definiției unei datorii și nu îndeplinesc criteriile de recunoaștere a provizioanelor; previzionarea unor astfel de pierderi impune însă testarea pentru depreciere a activelor de exploatare.**

Citatul decisiv (`omfp_1802_2014#art12~2/alin2~203`):
> 372. - (1) Nu se recunosc provizioane pentru pierderile viitoare din exploatare deoarece aceste pierderi viitoare nu corespund definiției unei datorii și nu sunt îndeplinite criteriile de recunoaștere a provizioanelor.

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **OMFP 1802/2014 art. 12 alin. (2)** — `omfp_1802_2014#art12~2/alin2~203` · valabil din nedovedit
  > 372. - (1) Nu se recunosc provizioane pentru pierderile viitoare din exploatare deoarece aceste pierderi viitoare nu corespund definiției unei datorii și nu sunt îndeplinite criteriile de recunoaștere a provizioanelor.
- **OMFP 1802/2014 art. 12 alin. (2)** — `omfp_1802_2014#art12~2/alin2~204` · valabil din nedovedit
  > Previzionarea unor pierderi viitoare din exploatare indică faptul că anumite active de exploatare ar putea fi depreciate. Ca urmare, entitatea testează aceste active pentru depreciere.

### Navigarea (3 pași, 3 ture)

1. `cauta` {"interogare": "provizioane pierderi viitoare din exploatare"}
2. `cuprins` {"act": "omfp_1802_2014_reglementari_consolidat", "filtru": "provizioane"}
3. `deschide` {"id": "omfp_1802_2014#art12~2/alin2~203"}

Apel: `claude-opus-5`, {'intrare': 6, 'iesire': 1503, 'cache_scriere': 2145, 'cache_citire': 20935} tokeni, $0.0615, 23 s

Pe fond: **GREȘIT** — articolul citat [('omfp_1802_2014', '12')] nu e printre cele ale cheii [('omfp_1802_2014', 'pct372'), ('omfp_1802_2014', 'pct374')]

## Stratul semantic v3 (context dat de căutare) — RĂSPUNS, pe fond GREȘIT

> Nu. Simpla estimare a unor pierderi viitoare din exploatare pentru 2027 nu permite recunoașterea unui provizion la 31.12.2026: un provizion se recunoaște doar dacă există o obligație curentă generată de un eveniment anterior, este probabilă o ieșire de resurse și valoarea poate fi estimată credibil; previzionarea de pierderi viitoare din exploatare obligă, în schimb, la testarea pentru depreciere a activelor de exploatare (ajustări pentru depreciere, nu provizion).

## Cheia

- Nu. Nu se recunosc provizioane pentru pierderi viitoare din exploatare (nu corespund definiției unei datorii); activele de exploatare se testează pentru depreciere.
- temei: OMFP 1802/2014, Reglementări contabile, pct. 372 alin. (1)-(2) coroborat cu pct. 374 alin. (1)
