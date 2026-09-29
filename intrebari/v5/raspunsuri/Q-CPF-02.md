# Q-CPF-02 — CALCUL

**Întrebarea:** O SRL avea TVA de plată 10.000 lei cu scadența 25.03.2026 și a plătit integral pe 24.04.2026. Ce accesorii datorează (dobânzi și penalități de întârziere)?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 24.04.2026, presupun o societate (SRL) contribuabil obișnuit, cu o obligație fiscală principală de TVA declarată, scadentă la 25.03.2026 și stinsă integral prin plată la 24.04.2026, fără eșalonare la plată, fără executare silită și fără penalitate de nedeclarare.*

Datele din întrebare: 2026-03-25, 2026-04-24 · data de referință aleasă: **2026-04-24** — Faptul întrebat este cuantumul accesoriilor datorate la stingerea obligației, care se calculează până la data plății inclusiv, respectiv 24.04.2026.

> **Se datorează dobânzi de întârziere de 0,02% pentru fiecare zi de întârziere și penalități de întârziere de 0,01% pentru fiecare zi de întârziere, calculate din ziua imediat următoare scadenței până la data plății inclusiv, adică 30 zile: dobânzi 60 lei, penalități de întârziere 30 lei, total accesorii 90 lei. Penalitatea de întârziere nu înlătură obligația de plată a dobânzilor.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul, pas cu pas — evaluat de cod, nu de model

- `zile(25.03.2026, 24.04.2026) = 30 zile`
- `zile_intarziere = zile(scadenta, data_platii)` = zile(25.03.2026, 24.04.2026) = **30**
  - `scadenta` = 25.03.2026 — FAPT_CAZ (din întrebare): „TVA de plată 10.000 lei cu scadența 25.03.2026”
  - `data_platii` = 24.04.2026 — FAPT_CAZ (din întrebare): „a plătit integral pe 24.04.2026”
- `dobanzi = suma_datorata * cota_dobanda * zile_intarziere` = ((10.000 × 0,02%) × 30) = **60**
  - `suma_datorata` = 10.000 — FAPT_CAZ (din întrebare): „O SRL avea TVA de plată 10.000 lei”
  - `cota_dobanda` = 0,02% — VALOARE_LEGALA din `legea_207_2015_consolidat#art174/alin5`: „Nivelul dobânzii este de 0,02% pentru fiecare zi de întârziere.”
- `penalitati = suma_datorata * cota_penalitate * zile_intarziere` = ((10.000 × 0,01%) × 30) = **30**
  - `suma_datorata` = 10.000 — FAPT_CAZ (din întrebare): „O SRL avea TVA de plată 10.000 lei”
  - `cota_penalitate` = 0,01% — VALOARE_LEGALA din `legea_207_2015_consolidat#art176/alin2`: „Nivelul penalității de întârziere este de 0,01% pentru fiecare zi de întârziere.”
- `total_accesorii = dobanzi + penalitati` = (60 + 30) = **90**

- **Codul de procedură fiscală (Legea 207/2015) art. 174 alin. (5)** — `legea_207_2015_consolidat#art174/alin5` · valabil din nedovedit
  > Nivelul dobânzii este de 0,02% pentru fiecare zi de întârziere.
- **Codul de procedură fiscală (Legea 207/2015) art. 176 alin. (2)** — `legea_207_2015_consolidat#art176/alin2` · valabil din nedovedit
  > Nivelul penalității de întârziere este de 0,01% pentru fiecare zi de întârziere.
- **Codul de procedură fiscală (Legea 207/2015) art. 174 alin. (1)** — `legea_207_2015_consolidat#art174/alin1` · valabil din nedovedit
  > Dobânzile se calculează pentru fiecare zi de întârziere, începând cu ziua imediat următoare termenului de scadență și până la data stingerii sumei datorate, inclusiv.
- **Codul de procedură fiscală (Legea 207/2015) art. 176 alin. (1)** — `legea_207_2015_consolidat#art176/alin1` · valabil din nedovedit
  > Penalitățile de întârziere se calculează pentru fiecare zi de întârziere, începând cu ziua imediat următoare termenului de scadență și până la data stingerii sumei datorate, inclusiv.
- derogare tratată: `legea_207_2015_consolidat#art174/alin4` — Excepția privește creanțele stinse prin executare silită și obligațiile debitorului declarat insolvabil; în speță obligația a fost stinsă prin plată voluntară, deci nu se aplică.
- derogare tratată: `legea_207_2015_consolidat#art197/alin1` — Dobânda redusă de 0,015%/zi se aplică numai pe perioada eșalonării la plată cu garanție integrală sub formă de scrisoare de garanție/poliță/consemnare; în speță nu există eșalonare, deci rămâne nivelul de 0,02%/zi.
- derogare tratată: `legea_207_2015_consolidat#art176/alin4` — Excluderea penalității de întârziere vizează obligațiile principale pentru care se datorează penalitate de nedeclarare; aici este vorba de TVA declarată și plătită cu întârziere, deci penalitatea de întârziere se datorează.

### Navigarea (10 pași, 6 ture)

1. `cuprins` {"act": "legea_207_2015_consolidat", "filtru": "dobânzi"}
2. `cuprins` {"act": "legea_207_2015_consolidat", "filtru": "penalit"}
3. `deschide` {"id": "legea_207_2015_consolidat#art174"}
4. `deschide` {"id": "legea_207_2015_consolidat#art176"}
5. `deschide` {"id": "legea_207_2015_consolidat#art174/alin5"}
6. `deschide` {"id": "legea_207_2015_consolidat#art174/alin1"}
7. `deschide` {"id": "legea_207_2015_consolidat#art174/alin4"}
8. `deschide` {"id": "legea_207_2015_consolidat#art197/alin1"}
9. `deschide` {"id": "legea_207_2015_consolidat#art176/alin1"}
10. `deschide` {"id": "legea_207_2015_consolidat#art176/alin2"}

Apel: `claude-opus-5`, {'intrare': 12, 'iesire': 4362, 'cache_scriere': 6831, 'cache_citire': 59379} tokeni, $0.1815, 59 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — NU POT, pe fond NU POT

> VERIFICAREA MECANICA a respins propunerea modelului: cifra '26.03.2026' din raspuns nu apare literal in citate sau in intrebare

## Cheia

- 30 zile de întârziere (26.03–24.04 inclusiv): dobânzi 10.000 × 0,02% × 30 = 60 lei; penalități de întârziere 10.000 × 0,01% × 30 = 30 lei; total 90 lei.
- temei: Legea 207/2015 art. 174 alin. (1) și (5); art. 176 alin. (1) și (2)
