# Q-CPF-01 — PARAMETRU

**Întrebarea:** Care sunt, în 2026, nivelurile dobânzii și penalității de întârziere pentru obligațiile fiscale principale datorate bugetului de stat (organ fiscal central) neachitate la scadență?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 28.09.2026, pentru un contribuabil cu obligații fiscale principale administrate de organul fiscal central (buget de stat), neachitate la termenul de scadență, în afara unei eșalonări la plată sau a altui regim special, presupun aplicarea regimului general al accesoriilor din Codul de procedură fiscală.*

Datele din întrebare: 2026-09-28 · data de referință aleasă: **2026-09-28** — Singura dată purtată de întrebare, corespunzând anului 2026 pentru care se cer nivelurile accesoriilor.

> **Dobânda este de 0,02% pentru fiecare zi de întârziere, iar penalitatea de întârziere este de 0,01% pentru fiecare zi de întârziere; ambele se calculează începând cu ziua imediat următoare termenului de scadență și până la data stingerii sumei, inclusiv, iar penalitatea nu înlătură obligația de plată a dobânzilor.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul de procedură fiscală (Legea 207/2015) art. 174 alin. (5)** — `legea_207_2015_consolidat#art174/alin5` · valabil din nedovedit
  > Nivelul dobânzii este de 0,02% pentru fiecare zi de întârziere.
- **Codul de procedură fiscală (Legea 207/2015) art. 176 alin. (2)** — `legea_207_2015_consolidat#art176/alin2` · valabil din nedovedit
  > Nivelul penalității de întârziere este de 0,01% pentru fiecare zi de întârziere.
- **Codul de procedură fiscală (Legea 207/2015) art. 173 alin. (1)** — `legea_207_2015_consolidat#art173/alin1` · valabil din nedovedit
  > Pentru neachitarea la termenul de scadență de către debitor a obligațiilor fiscale principale, se datorează după acest termen dobânzi și penalități de întârziere.
- **Codul de procedură fiscală (Legea 207/2015) art. 174 alin. (1)** — `legea_207_2015_consolidat#art174/alin1` · valabil din nedovedit
  > Dobânzile se calculează pentru fiecare zi de întârziere, începând cu ziua imediat următoare termenului de scadență și până la data stingerii sumei datorate, inclusiv.
- **Codul de procedură fiscală (Legea 207/2015) art. 176 alin. (3)** — `legea_207_2015_consolidat#art176/alin3` · valabil din nedovedit
  > Penalitatea de întârziere nu înlătură obligația de plată a dobânzilor.
- derogare tratată: `legea_207_2015_consolidat#art197/alin1` — Excepția de la art. 174 alin. (5) privește dobânzile datorate pe perioada eșalonării la plată a obligațiilor fiscale; întrebarea vizează obligații principale simplu neachitate la scadență, fără eșalonare acordată, deci excepția nu se aplică.

### Navigarea (4 pași, 3 ture)

1. `cauta` {"interogare": "nivelul dobânzii 0,02% pentru fiecare zi de întârziere"}
2. `cauta` {"interogare": "nivelul penalității de întârziere pentru fiecare zi de întârziere"}
3. `deschide` {"id": "legea_207_2015_consolidat#art174/alin5"}
4. `deschide` {"id": "legea_207_2015_consolidat#art176/alin2"}

Apel: `claude-opus-5`, {'intrare': 6, 'iesire': 1899, 'cache_scriere': 4128, 'cache_citire': 24181} tokeni, $0.0854, 22 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond CORECT

> Dobânda este de 0,02% pentru fiecare zi de întârziere, iar penalitatea de întârziere este de 0,01% pentru fiecare zi de întârziere.

## Cheia

- Dobândă 0,02% pe fiecare zi de întârziere + penalitate de întârziere 0,01% pe fiecare zi de întârziere (cumulative), calculate din ziua următoare scadenței până la stingere inclusiv.
- temei: Legea 207/2015 art. 174 alin. (1) și (5); art. 176 alin. (1), (2) și (3)
