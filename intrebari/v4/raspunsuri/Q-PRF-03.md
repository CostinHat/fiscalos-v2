# Q-PRF-03 — CAPCANA

**Întrebarea:** Până când se depune D101 și se plătește impozitul pe profit anual pentru anul fiscal 2026 (an calendaristic), la o societate care nu se dizolvă?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 28.09.2026, pentru o persoană juridică română plătitoare de impozit pe profit, cu an fiscal = anul calendaristic 2026, care nu se dizolvă (cu sau fără lichidare) și care nu datorează impozitul special prevăzut la art. 40^3; presupun că nu face parte dintr-un grup fiscal consolidat și că nu intră sub incidența art. 16 alin. (5).</declaratie>
<parameter name="raspuns">Declarația anuală privind impozitul pe profit (D101) pentru anul fiscal 2026 se depune până la data de 25 iunie inclusiv a anului următor, respectiv 25 iunie {anul_urmator}; la același termen se fac definitivarea și plata impozitului pe profit anual.*

> **x [calcul: anul_urmator = anul_fiscal + 1 = 2.027]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul — evaluat de cod, nu de model

- `anul_urmator = anul_fiscal + 1` → **2.027**
  - `anul_fiscal` = 2026 — din întrebare: „anul fiscal 2026 (an calendaristic)”

- **Codul fiscal (Legea 227/2015) art. 42 alin. (1)** — `cod_fiscal_227_2015_consolidat#art42/alin1` · valabil din 2026-02-25
  > Contribuabilii au obligația să depună o declarație anuală privind impozitul pe profit până la data de 25 iunie inclusiv a anului următor, cu excepția contribuabililor prevăzuți la art. 41 alin. (16) și (17)
- **Codul fiscal (Legea 227/2015) art. 41 alin. (1)** — `cod_fiscal_227_2015_consolidat#art41/alin1` · valabil din nedovedit
  > Definitivarea și plata impozitului pe profit aferent anului fiscal respectiv se efectuează până la termenul de depunere a declarației privind impozitul pe profit prevăzut la art. 42 .
- derogare tratată: `cod_fiscal_227_2015_consolidat#art42/alin5` — Excepția vizează exclusiv impozitul pe profit stabilit potrivit art. 40^3, care nu se declară prin declarația anuală; societatea din întrebare nu datorează acest impozit, deci termenul general de la art. 42 alin. (1) rămâne aplicabil.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art41/alin16` — Termenele speciale privesc persoanele juridice care se dizolvă cu lichidare; întrebarea precizează că societatea nu se dizolvă, deci nu se aplică.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art41/alin17` — Termenul special privește persoanele juridice care se dizolvă fără lichidare în cursul anului fiscal; nu este cazul societății din întrebare.

### Navigarea (8 pași, 6 ture)

1. `cauta` {"interogare": "declarația anuală de impozit pe profit depunere plata termen"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Depunerea declaraţiei de impozit pe profit"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art42"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art42/alin1"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art42/alin5"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art41"}
7. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art41/alin1"}
8. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art41/alin14"}

Apel: `claude-opus-5`, {'intrare': 12, 'iesire': 3549, 'cache_scriere': 11055, 'cache_citire': 66574} tokeni, $0.1912, 54 s

Pe fond: **GREȘIT** — faptul principal al cheii (['25 iunie']) nu e in raspuns

## Stratul semantic v3 (context dat de căutare) — RĂSPUNS, pe fond CORECT

> Declarația anuală privind impozitul pe profit (D101) pentru anul fiscal 2026 se depune până la data de 25 iunie inclusiv a anului următor, iar definitivarea și plata impozitului pe profit aferent anului fiscal se efectuează până la același termen, respectiv termenul de depunere a declarației anuale.

## Cheia

- 25 iunie 2027 inclusiv (nu 25 martie). Notă: validatorul DUKIntegrator testat la 03.08.2026 încă cere martie pentru an 2026 — termenul legal e totuși iunie
- temei: Cod fiscal art. 42 alin. (1), modificat de OUG 8/2026 art. 6 pct. 12 (MO 147/25.02.2026), aplicabil începând cu anul fiscal 2026 cf. art. 10 alin. (2) OUG 8/2026; art. 41 alin. (1) și (2) (definitivarea și plata până la termenul art. 42)
