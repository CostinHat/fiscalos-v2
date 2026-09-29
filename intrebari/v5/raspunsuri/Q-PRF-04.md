# Q-PRF-04 — CAPCANA

**Întrebarea:** O societate cu cifra de afaceri 2025 peste 50 mil. euro are în 2026: VT = 300.000.000 lei, Vs = 20.000.000 lei, I = 0, A = 10.000.000 lei; impozitul pe profit anual calculat (fără sponsorizări sau alte sume de scăzut) = 1.000.000 lei. Cât impozit pe profit datorează pentru 2026?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 28.09.2026, presupun o societate plătitoare de impozit pe profit (nu dintre cele de la art. 15 și neexclusă prin art. 18^1 alin. (14)), cu an fiscal = anul calendaristic 2026, care în 2025 a avut cifră de afaceri peste 50.000.000 euro și la care, pentru anul 2026, impozitul pe profit anual ajustat nu se diminuează cu sponsorizări sau alte sume scăzute potrivit legilor speciale.*

Datele din întrebare: 2025-12-31, 2026-09-28 · data de referință aleasă: **2026-09-28** — Faptul întrebat este impozitul pe profit datorat pentru anul fiscal 2026; cifra de afaceri 2025 este doar condiția de intrare în sfera art. 18^1.

> **Societatea datorează impozit pe profit la nivelul impozitului minim pe cifra de afaceri, întrucât IMCA (calculat pentru 2026 cu cota de 0,5% asupra VT – Vs – I – A) este 1.350.000 lei, mai mare decât impozitul pe profit calculat. Impozit datorat pentru 2026: 1.350.000 lei.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul, pas cu pas — evaluat de cod, nu de model

- `IMCA_2026 = cota_IMCA_2026 * (VT - Vs - I - A)` = (0,5% × (((300.000.000 − 20.000.000) − 0) − 10.000.000)) = **1.350.000**
  - `cota_IMCA_2026` = 0,5% — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art18^1/alin16`: „cota de impozit din cadrul formulei prevăzute la alin. (3) este 0,5%.”
  - `VT` = 300.000.000 — FAPT_CAZ (din întrebare): „VT = 300.000.000 lei”
  - `Vs` = 20.000.000 — FAPT_CAZ (din întrebare): „Vs = 20.000.000 lei”
  - `I` = 0 — FAPT_CAZ (din întrebare): „I = 0”
  - `A` = 10.000.000 — FAPT_CAZ (din întrebare): „A = 10.000.000 lei”
- `Impozit_datorat = max(impozit_pe_profit_calculat, IMCA_2026)` = max(1.000.000, 1.350.000) = **1.350.000**
  - `impozit_pe_profit_calculat` = 1.000.000 — FAPT_CAZ (din întrebare): „impozitul pe profit anual calculat (fără sponsorizări sau alte sume de scăzut) = 1.000.000 lei”

- **Codul fiscal (Legea 227/2015) art. 18^1 alin. (1)** — `cod_fiscal_227_2015_consolidat#art18^1/alin1` · valabil din nedovedit
  > care în anul de calcul determină un impozit pe profit, cumulat de la începutul anului fiscal/anului fiscal modificat până la sfârșitul trimestrului/anului de calcul, mai mic decât impozitul minim pe cifra de afaceri stabilit potrivit prevederilor alin. (3) , sunt obligați la plata impozitului pe profit la nivelul impozitului minim pe cifra de afaceri.
- **Codul fiscal (Legea 227/2015) art. 18^1 alin. (16)** — `cod_fiscal_227_2015_consolidat#art18^1/alin16` · valabil din 2026-01-01
  > Pentru anul fiscal 2026/anul fiscal modificat care începe în anul 2026, cota de impozit din cadrul formulei prevăzute la alin. (3) este 0,5%.
- **Codul fiscal (Legea 227/2015) art. 18^1 alin. (3)** — `cod_fiscal_227_2015_consolidat#art18^1/alin3` · valabil din 2024-01-01
  > Impozitul minim pe cifra de afaceri se determină astfel: IMCA = 1% x (VT – Vs – I – A), unde indicatorii au următoarea semnificație: IMCA - impozit minim pe cifra de afaceri, determinat cumulat de la începutul anului fiscal/anului fiscal modificat până la sfârșitul trimestrului/anului de calcul;
- **Codul fiscal (Legea 227/2015) art. 18^1 alin. (1)** — `cod_fiscal_227_2015_consolidat#art18^1/alin1` · valabil din nedovedit
  > Contribuabilii, alții decât cei prevăzuți la art. 15 , care înregistrează în anul precedent o cifră de afaceri de peste 50.000.000 euro și care în anul de calcul determină un impozit pe profit
- **Codul fiscal (Legea 227/2015) art. 18^1 alin. (5)** — `cod_fiscal_227_2015_consolidat#art18^1/alin5` · valabil din 2026-02-25
  > pentru efectuarea comparației între impozitul pe profit și impozitul minim pe cifra de afaceri potrivit dispozițiilor alin. (1) , impozitul pe profit trimestrial/anual reprezintă impozitul pe profit înainte de scăderea sumelor potrivit legii, ajustat astfel: din acest impozit pe profit se scad sumele reprezentând sponsorizare/mecenat, alte sume care se scad din impozitul pe profit
- **Codul fiscal (Legea 227/2015) art. 18^1 alin. (17)** — `cod_fiscal_227_2015_consolidat#art18^1/alin17` · valabil din 2026-01-01
  > Prevederile prezentului articol se aplică până la data de 31 decembrie 2026 inclusiv/ultima zi a anului fiscal modificat care se încheie în anul 2027 inclusiv.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art18^1/alin16` — Regulă specială pentru anul fiscal 2026, care înlocuiește cota de 1% din formula de la alin. (3) cu 0,5%; fiind vorba de impozitul aferent anului 2026, am aplicat-o și am folosit cota de 0,5%.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art18^1/alin14` — Exclude de la aplicarea art. 18^1 operatorii economici reglementați/licențiați în domeniul energiei; întrebarea nu indică o astfel de activitate, deci nu se aplică cazului.

### Navigarea (10 pași, 6 ture)

1. `cauta` {"interogare": "impozit minim pe cifra de afaceri IMCA = 1% x (VT - Vs - I - A)"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "impozit minim pe cifra de afaceri"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art18^1/alin1"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art18^1/alin3"}
5. `cauta` {"interogare": "abrogă art. 18^1 impozit minim pe cifra de afaceri începând cu 1 ianuarie 2026"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art18^1"}
7. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art18^1/alin16"}
8. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art18^1/alin17"}
9. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art18^1/alin5"}
10. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art18^1/alin7"}

Apel: `claude-opus-5`, {'intrare': 12, 'iesire': 6540, 'cache_scriere': 14634, 'cache_citire': 78868} tokeni, $0.2945, 83 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond GREȘIT

> Impozitul minim pe cifra de afaceri este 2.700.000 lei, mai mare decât impozitul pe profit calculat, deci societatea datorează pentru 2026 impozit pe profit la nivelul impozitului minim: 2.700.000 lei. [calcul: IMCA = cota * (VT - Vs - I - A) = 2.700.000; impozit_datorat = max(IMCA, impozit_profit) = 2.700.000]

## Cheia

- 1.350.000 lei — IMCA = 0,5% × (300.000.000 − 20.000.000 − 0 − 10.000.000) = 1.350.000 > 1.000.000, deci plătește la nivelul IMCA (nu 1%, care ar da 2.700.000)
- temei: Cod fiscal art. 18^1 alin. (1) și (3); alin. (16) (cota 0,5% pentru anul fiscal 2026, introdus de OUG 89/2025 art. I pct. 1); alin. (17) (articolul se aplică până la 31.12.2026)
