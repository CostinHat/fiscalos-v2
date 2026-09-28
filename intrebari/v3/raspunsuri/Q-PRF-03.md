# Q-PRF-03 — CAPCANA

**Întrebarea:** Până când se depune D101 și se plătește impozitul pe profit anual pentru anul fiscal 2026 (an calendaristic), la o societate care nu se dizolvă?

## Stratul semantic — RĂSPUNS

*La data de referință 28.09.2026, presupun o societate plătitoare de impozit pe profit, cu an fiscal calendaristic (nu an fiscal modificat), care nu se dizolvă cu sau fără lichidare, nu face parte dintr-un grup fiscal consolidat și nu datorează impozit stabilit prin regula specială exceptată de la declarația anuală.*

> **Declarația anuală privind impozitul pe profit (D101) pentru anul fiscal 2026 se depune până la data de 25 iunie inclusiv a anului următor, iar definitivarea și plata impozitului pe profit aferent anului fiscal se efectuează până la același termen, respectiv termenul de depunere a declarației anuale.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 42 alin. (1)** — `cod_fiscal_227_2015_consolidat#art42/alin1` · valabil din 2026-02-25
  > Contribuabilii au obligația să depună o declarație anuală privind impozitul pe profit până la data de 25 iunie inclusiv a anului următor, cu excepția contribuabililor prevăzuți la art. 41 alin. (16) și (17) care depun declarația anuală privind impozitul pe profit până la termenele prevăzute în cadrul acestor alineate.
- **Codul fiscal (Legea 227/2015) art. 41 alin. (10)** — `cod_fiscal_227_2015_consolidat#art41/alin10` · valabil din nedovedit
  > Definitivarea și plata impozitului pe profit aferent anului fiscal respectiv se efectuează până la termenul de depunere a declarației privind impozitul pe profit prevăzut la art. 42 .
- derogare tratată: `cod_fiscal_227_2015_consolidat#art42/alin5` — Derogă de la art. 42 alin. (1) și (2) doar pentru impozitul pe profit stabilit potrivit art. 40^3, care nu se declară prin declarația anuală; întrebarea vizează impozitul pe profit anual obișnuit, deci excepția nu se aplică.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art41/alin17` — Vizează persoanele juridice care se dizolvă fără lichidare; societatea din întrebare nu se dizolvă, deci termenul special (închiderea perioadei impozabile) nu se aplică.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art41/alin16` — Vizează persoanele juridice care se dizolvă cu lichidare; nu este cazul societății din întrebare.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art42/alin2` — Se aplică contribuabililor cu an fiscal modificat (art. 16 alin. (5)); întrebarea privește un an fiscal calendaristic, deci termenul de 25 a celei de-a șasea luni de la închiderea anului fiscal modificat nu se aplică.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art42^9/alin4` — Privește persoana juridică responsabilă dintr-un grup fiscal consolidat; societatea din întrebare nu este prezentată ca membru/responsabil de grup fiscal.

Apel: `claude-opus-5`, {'intrare': 8923, 'iesire': 3138, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.1240

Pe fond: **CORECT** — faptul principal si articolul coincid

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **în cazul în care anul fiscal modificat începe în a doua, respectiv în a treia lună a trimestrului calendaristic, prima lună, respectiv primele două luni ale trimestrului calendaristic respectiv, vor constitui un trimestru pentru care contribuabilul are obligația declarării și efectuării plăților anticipate, în sumă de 1/12 din impozitul pe profit datorat pentru anul precedent, pentru fiecare lună a trimestrului, până la data de 25 inclusiv a primei luni următoare încheierii trimestrului calendaristic respectiv.**

Motiv: D15: fraza care conţine un fapt de forma cerută (termen) si potriveste cel mai bine intrebarea (scor local 11.2)

- **Codul fiscal (Legea 227/2015) art. 41 alin. (15) lit. b)** — `cod_fiscal_227_2015_consolidat#art41/alin15/litb` · valabil din nedovedit
  > contribuabilii care declară și plătesc impozitul pe profit anual, cu plăți anticipate efectuate trimestrial, pentru anul fiscal modificat continuă efectuarea plăților anticipate la nivelul celor stabilite înainte de modificare; în cazul în care anul fiscal modificat începe în a doua, respectiv în a treia lună a trimestrului calendaristic, prima lună, respectiv primele două luni ale trimestrului calendaristic respectiv, vor constitui un trimestru pentru care contribuabilul are obligația declarări…

Pe fond: **GREȘIT** — faptul principal al cheii (['25 iunie']) nu e in raspuns; articolul citat [('cf', '41')] nu e printre cele ale cheii [('cf', '42'), ('cf', '6'), ('cf', '10'), (None, '41'), (None, '42')]

## Cheia

- 25 iunie 2027 inclusiv (nu 25 martie). Notă: validatorul DUKIntegrator testat la 03.08.2026 încă cere martie pentru an 2026 — termenul legal e totuși iunie
- temei: Cod fiscal art. 42 alin. (1), modificat de OUG 8/2026 art. 6 pct. 12 (MO 147/25.02.2026), aplicabil începând cu anul fiscal 2026 cf. art. 10 alin. (2) OUG 8/2026; art. 41 alin. (1) și (2) (definitivarea și plata până la termenul art. 42)
