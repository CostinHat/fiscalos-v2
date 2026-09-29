# Q-SAL-01 — PARAMETRU

**Întrebarea:** Care este cota contribuției asiguratorii pentru muncă (CAM) datorată de angajator în 2026 și cine o suportă?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 28.09.2026, presupun un angajator (persoană fizică sau juridică) din România care acordă venituri din salarii și asimilate salariilor, în regimul general al Codului fiscal, fără facilități sectoriale speciale.*

Datele din întrebare: 2026-09-28 · data de referință aleasă: **2026-09-28** — Singura dată din întrebare, corespunzând anului 2026 pentru care se cere cota CAM.

> **Cota contribuției asiguratorii pentru muncă (CAM) este de 2,25%, aplicată asupra bazei de calcul a veniturilor din salarii și asimilate salariilor. Ea este datorată și suportată integral de angajator (persoanele fizice și juridice care au calitatea de angajatori sau sunt asimilate acestora), nu de salariat; angajatorul are obligația de a o calcula și de a o plăti la bugetul de stat.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 220^3 alin. (1)** — `cod_fiscal_227_2015_consolidat#art220^3/alin1` · valabil din nedovedit
  > Cota contribuției asiguratorii pentru muncă este de 2,25%.
- **Codul fiscal (Legea 227/2015) art. 220^1** — `cod_fiscal_227_2015_consolidat#art220^1` · valabil din 2018-01-01
  > Contribuabilii obligați la plata contribuției asiguratorii pentru muncă sunt, după caz: a) persoanele fizice și juridice care au calitatea de angajatori sau sunt asimilate acestora
- **Codul fiscal (Legea 227/2015) art. 220^6 alin. (1)** — `cod_fiscal_227_2015_consolidat#art220^6/alin1` · valabil din nedovedit
  > Persoanele fizice și juridice prevăzute la art. 220^1 lit. a) au obligația de a calcula contribuția asiguratorie pentru muncă și de a o plăti la bugetul de stat, într-un cont distinct
- **Codul fiscal (Legea 227/2015) art. 220^6 alin. (3)** — `cod_fiscal_227_2015_consolidat#art220^6/alin3` · valabil din nedovedit
  > Calculul contribuției asiguratorie pentru muncă se realizează prin aplicarea cotei prevăzute la art. 220^3 asupra bazei de calcul prevăzute la art. 220^4 , cu respectarea prevederilor art. 220^5 .

### Navigarea (5 pași, 4 ture)

1. `cauta` {"interogare": "contribuția asiguratorie pentru muncă cota"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "asiguratorie pentru muncă"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art220^3/alin1"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art220^1"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art220^3"}

Apel: `claude-opus-5`, {'intrare': 8, 'iesire': 1898, 'cache_scriere': 3813, 'cache_citire': 33730} tokeni, $0.0882, 29 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond CORECT

> Cota este de 2,25%, aplicată asupra bazei de calcul, și este suportată integral de angajator (persoanele fizice și juridice care au calitatea de angajatori sau sunt asimilate acestora), care are obligația să o calculeze și să o plătească la bugetul de stat; nu se reține din salariul angajatului.

## Cheia

- 2,25%, datorată de angajator, asupra bazei de la art. 220^4 (câștigurile brute din salarii)
- temei: Legea 227/2015 (Cod fiscal) art. 220^3 alin. (1); baza: art. 220^4 alin. (1)
