# Q-CPF-02 — CALCUL

**Întrebarea:** O SRL avea TVA de plată 10.000 lei cu scadența 25.03.2026 și a plătit integral pe 24.04.2026. Ce accesorii datorează (dobânzi și penalități de întârziere)?

## Stratul de navigare (v4) — NU POT RĂSPUNDE

*La data de referință 25.03.2026, presupun o societate (SRL) plătitoare de TVA, cu obligație fiscală principală declarată de 10.000 lei scadentă la 25.03.2026 și achitată integral, voluntar (fără executare silită, fără eșalonare la plată și fără diferențe stabilite de organul fiscal care să atragă penalitate de nedeclarare), la 24.04.2026, accesoriile fiind cele de drept comun din Codul de procedură fiscală.*

Motiv: VERIFICAREA MECANICA a respins propunerea modelului: cifra '26.03.2026' din raspuns nu apare literal in citate sau in intrebare

### Calculul — evaluat de cod, nu de model

- `zile_intarziere = zile(scadenta, data_platii)` → **30**
  - `scadenta` = 25.03.2026 — din întrebare: „cu scadența 25.03.2026”
  - `data_platii` = 24.04.2026 — din întrebare: „a plătit integral pe 24.04.2026”
- `dobanda = suma_datorata * cota_dobanda * zile_intarziere` → **60**
  - `suma_datorata` = 10.000 — din întrebare: „TVA de plată 10.000 lei”
  - `cota_dobanda` = 0,02% — din `legea_207_2015_consolidat#art174/alin5`: „Nivelul dobânzii este de 0,02% pentru fiecare zi de întârziere.”
- `penalitate = suma_datorata * cota_penalitate * zile_intarziere` → **30**
  - `suma_datorata` = 10.000 — din întrebare: „TVA de plată 10.000 lei”
  - `cota_penalitate` = 0,01% — din `legea_207_2015_consolidat#art176/alin2`: „Nivelul penalității de întârziere este de 0,01% pentru fiecare zi de întârziere.”
- `total = dobanda + penalitate` → **90**

- **Codul de procedură fiscală (Legea 207/2015) art. 174 alin. (5)** — `legea_207_2015_consolidat#art174/alin5` · valabil din nedovedit
  > Nivelul dobânzii este de 0,02% pentru fiecare zi de întârziere.
- **Codul de procedură fiscală (Legea 207/2015) art. 176 alin. (2)** — `legea_207_2015_consolidat#art176/alin2` · valabil din nedovedit
  > Nivelul penalității de întârziere este de 0,01% pentru fiecare zi de întârziere.
- **Codul de procedură fiscală (Legea 207/2015) art. 174 alin. (1)** — `legea_207_2015_consolidat#art174/alin1` · valabil din nedovedit
  > Dobânzile se calculează pentru fiecare zi de întârziere, începând cu ziua imediat următoare termenului de scadență și până la data stingerii sumei datorate, inclusiv.
- **Codul de procedură fiscală (Legea 207/2015) art. 176 alin. (1)** — `legea_207_2015_consolidat#art176/alin1` · valabil din nedovedit
  > Penalitățile de întârziere se calculează pentru fiecare zi de întârziere, începând cu ziua imediat următoare termenului de scadență și până la data stingerii sumei datorate, inclusiv.
- **Codul de procedură fiscală (Legea 207/2015) art. 176 alin. (3)** — `legea_207_2015_consolidat#art176/alin3` · valabil din nedovedit
  > Penalitatea de întârziere nu înlătură obligația de plată a dobânzilor.
- derogare tratată: `legea_207_2015_consolidat#art174/alin4` — Excepția de la art. 174 alin. (1) privește creanțele stinse prin executare silită și obligațiile debitorului declarat insolvabil; în speță plata a fost făcută voluntar de un contribuabil în activitate, deci nu se aplică.
- derogare tratată: `legea_207_2015_consolidat#art197/alin1` — Excepția de la nivelul dobânzii (0,015%/zi) se aplică numai pe perioada eșalonării la plată cu garanție constituită integral sub forma scrisorii de garanție/poliței de asigurare/consemnării de mijloace bănești; în speță nu există eșalonare, deci rămâne nivelul de 0,02%/zi.
- derogare tratată: `legea_207_2015_consolidat#art176/alin4` — Penalitatea de întârziere nu se aplică obligațiilor principale pentru care se datorează penalitate de nedeclarare; în speță TVA a fost declarată corect și doar plătită cu întârziere, deci penalitatea de întârziere se datorează.

### Navigarea (10 pași, 6 ture)

1. `cuprins` {"act": "legea_207_2015_consolidat", "filtru": "dobânzi"}
2. `cuprins` {"act": "legea_207_2015_consolidat", "filtru": "penalitate"}
3. `deschide` {"id": "legea_207_2015_consolidat#art174"}
4. `deschide` {"id": "legea_207_2015_consolidat#art176"}
5. `deschide` {"id": "legea_207_2015_consolidat#art174/alin1"}
6. `deschide` {"id": "legea_207_2015_consolidat#art174/alin5"}
7. `deschide` {"id": "legea_207_2015_consolidat#art174/alin4"}
8. `deschide` {"id": "legea_207_2015_consolidat#art176/alin1"}
9. `deschide` {"id": "legea_207_2015_consolidat#art176/alin2"}
10. `deschide` {"id": "legea_207_2015_consolidat#art197/alin1"}

Apel: `claude-opus-5`, {'intrare': 12, 'iesire': 4347, 'cache_scriere': 7938, 'cache_citire': 54057} tokeni, $0.1854, 50 s

Pe fond: **NU POT** — VERIFICAREA MECANICA a respins propunerea modelului: cifra '26.03.2026' din raspuns nu apare literal in citate sau in intrebare

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți confirmă doar că se datorează dobânzi și penalități de întârziere, dar nu conțin textele care stabilesc nivelul (cota zilnică) al dobânzii (art. 174) și al penalității de întârziere (art. 176 alin. (1)) și nici regula de calcul al perioadei. Cuantificarea accesoriilor pentru intervalul 26.03.2026-24.04.2026 ar presupune atât o cotă legală care nu apare în niciun atom, cât și un calcul (număr de zile × cotă × 10.000 lei), care nu este permis.

## Cheia

- 30 zile de întârziere (26.03–24.04 inclusiv): dobânzi 10.000 × 0,02% × 30 = 60 lei; penalități de întârziere 10.000 × 0,01% × 30 = 30 lei; total 90 lei.
- temei: Legea 207/2015 art. 174 alin. (1) și (5); art. 176 alin. (1) și (2)
