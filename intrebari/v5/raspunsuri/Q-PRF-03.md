# Q-PRF-03 — CAPCANA

**Întrebarea:** Până când se depune D101 și se plătește impozitul pe profit anual pentru anul fiscal 2026 (an calendaristic), la o societate care nu se dizolvă?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 28.09.2026, pentru o persoană juridică plătitoare de impozit pe profit cu an fiscal calendaristic (anul fiscal 2026), care nu se dizolvă cu sau fără lichidare, nu are an fiscal modificat potrivit art. 16 alin. (5) și nu datorează impozit pe profit la ieșire potrivit art. 40^3.*

Datele din întrebare: 2026-09-28 · data de referință aleasă: **2026-09-28** — Singura dată purtată de întrebare, corespunzătoare anului fiscal 2026 pentru care se determină termenul de declarare și plată.

> **Declarația anuală privind impozitul pe profit (D101) pentru anul fiscal 2026 se depune până la data de 25 iunie inclusiv a anului următor anului fiscal 2026; la același termen se face și definitivarea și plata impozitului pe profit anual aferent anului 2026.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 42 alin. (1)** — `cod_fiscal_227_2015_consolidat#art42/alin1` · valabil din 2026-02-25
  > Contribuabilii au obligația să depună o declarație anuală privind impozitul pe profit până la data de 25 iunie inclusiv a anului următor, cu excepția contribuabililor prevăzuți la art. 41 alin. (16) și (17) care depun declarația anuală privind impozitul pe profit până la termenele prevăzute în cadrul acestor alineate.
- **Codul fiscal (Legea 227/2015) art. 41 alin. (1)** — `cod_fiscal_227_2015_consolidat#art41/alin1` · valabil din nedovedit
  > Definitivarea și plata impozitului pe profit aferent anului fiscal respectiv se efectuează până la termenul de depunere a declarației privind impozitul pe profit prevăzut la art. 42 .
- **Codul fiscal (Legea 227/2015) art. 42 alin. (1)** — `cod_fiscal_227_2015_consolidat#art42/alin1` · valabil din 2026-02-25
  > Potrivit alin. (2) al art. 10 din ORDONANȚA DE URGENȚĂ nr. 8 din 24 februarie 2026, publicată în MONITORUL OFICIAL nr. 147 din 25 februarie 2026, prevederile art. 6 pct. 12 se aplică începând cu anul fiscal 2026.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art42/alin5` — Excepția privește exclusiv impozitul pe profit stabilit potrivit art. 40^3 (impozit la ieșire), care nu se declară prin declarația anuală; cazul din întrebare nu vizează un astfel de impozit, deci termenul general rămâne aplicabil.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art41/alin16` — Se referă la persoanele juridice care se dizolvă cu lichidare; întrebarea precizează expres că societatea nu se dizolvă.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art41/alin17` — Se referă la persoanele juridice care se dizolvă fără lichidare în cursul anului fiscal; nu este cazul societății din întrebare.

### Navigarea (8 pași, 6 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "declaraț anuală impozit pe profit"}
2. `cauta` {"interogare": "depunerea declarației anuale de impozit pe profit 25 martie"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art42"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art42/alin1"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art42/alin5"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art41"}
7. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art41/alin14"}
8. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art41/alin1"}

Apel: `claude-opus-5`, {'intrare': 12, 'iesire': 3678, 'cache_scriere': 10942, 'cache_citire': 70873} tokeni, $0.1958, 51 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond GREȘIT

> x [calcul: anul_urmator = anul_fiscal + 1 = 2.027]

## Cheia

- 25 iunie 2027 inclusiv (nu 25 martie). Notă: validatorul DUKIntegrator testat la 03.08.2026 încă cere martie pentru an 2026 — termenul legal e totuși iunie
- temei: Cod fiscal art. 42 alin. (1), modificat de OUG 8/2026 art. 6 pct. 12 (MO 147/25.02.2026), aplicabil începând cu anul fiscal 2026 cf. art. 10 alin. (2) OUG 8/2026; art. 41 alin. (1) și (2) (definitivarea și plata până la termenul art. 42)
