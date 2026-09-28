# Q-CPF-09 — CAPCANA

**Întrebarea:** O firmă a plătit cu 60 de zile întârziere o amendă contravențională de 2.000 lei aplicată de ANAF. Cât datorează ca dobânzi și penalități de întârziere pentru această întârziere?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 28.09.2026, presupun o persoană juridică (firmă) care a achitat cu întârziere o amendă contravențională aplicată de ANAF, deci o creanță bugetară administrată de organul fiscal central (nu de organul fiscal local), fără suspendarea judecătorească a executării actului.*

> **Nu datorează nimic: pentru sumele cu titlu de amenzi de orice fel nu se datorează dobânzi și penalități de întârziere, indiferent de durata întârzierii (0 lei accesorii pentru amenda de 2.000 lei). Întârzierea poate atrage doar executarea silită a amenzii, nu accesorii.**

Citatul decisiv (`legea_207_2015_consolidat#art173/alin2`):
> Nu se datorează dobânzi și penalități de întârziere pentru sumele datorate cu titlu de amenzi de orice fel, obligații fiscale accesorii stabilite potrivit legii, cheltuieli de executare silită, cheltuieli judiciare, sumele confiscate

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul de procedură fiscală (Legea 207/2015) art. 173 alin. (2)** — `legea_207_2015_consolidat#art173/alin2` · valabil din nedovedit
  > Nu se datorează dobânzi și penalități de întârziere pentru sumele datorate cu titlu de amenzi de orice fel, obligații fiscale accesorii stabilite potrivit legii, cheltuieli de executare silită, cheltuieli judiciare, sumele confiscate
- **Codul de procedură fiscală (Legea 207/2015) art. 173 alin. (1)** — `legea_207_2015_consolidat#art173/alin1` · valabil din nedovedit
  > Pentru neachitarea la termenul de scadență de către debitor a obligațiilor fiscale principale, se datorează după acest termen dobânzi și penalități de întârziere.
- derogare tratată: `legea_207_2015_consolidat#art183/alin1` — Excepția privește obligațiile fiscale principale datorate bugetelor locale, pentru care se datorează majorări de întârziere; amenda din speță este aplicată de ANAF (organ fiscal central), deci nu se aplică.
- derogare tratată: `legea_207_2015_consolidat#art278/alin4` — Excepția vizează situația suspendării executării actului administrativ fiscal de către instanța de contencios administrativ; în speță nu există o astfel de suspendare, iar regula ar fi oricum tot de neaplicare a penalităților.

### Navigarea (5 pași, 4 ture)

1. `cauta` {"interogare": "nu se datorează dobânzi și penalități de întârziere pentru amenzi de orice fel"}
2. `cuprins` {"act": "legea_207_2015_consolidat", "filtru": "dobânzi"}
3. `deschide` {"id": "legea_207_2015_consolidat#art173/alin2"}
4. `deschide` {"id": "legea_207_2015_consolidat#art183/alin1"}
5. `deschide` {"id": "legea_207_2015_consolidat#art278/alin4"}

Apel: `claude-opus-5`, {'intrare': 8, 'iesire': 1593, 'cache_scriere': 3934, 'cache_citire': 30999} tokeni, $0.0799, 29 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Stratul semantic v3 (context dat de căutare) — RĂSPUNS, pe fond GREȘIT

> Nu datorează nimic cu titlu de dobânzi și penalități de întârziere: pentru sumele datorate cu titlu de amenzi de orice fel nu se calculează astfel de accesorii, indiferent de durata întârzierii. Se achită doar amenda în sine.

## Cheia

- 0 lei: nu se datorează dobânzi și penalități de întârziere pentru amenzi de orice fel (nici pentru accesorii, cheltuieli de executare etc.).
- temei: Legea 207/2015 art. 173 alin. (2)
