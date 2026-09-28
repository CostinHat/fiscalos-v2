# Q-PRF-04 — CAPCANA

**Întrebarea:** O societate cu cifra de afaceri 2025 peste 50 mil. euro are în 2026: VT = 300.000.000 lei, Vs = 20.000.000 lei, I = 0, A = 10.000.000 lei; impozitul pe profit anual calculat (fără sponsorizări sau alte sume de scăzut) = 1.000.000 lei. Cât impozit pe profit datorează pentru 2026?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 31.12.2025, pentru anul fiscal 2026, presupun o societate plătitoare de impozit pe profit (nu dintre cele de la art. 15), cu an fiscal = an calendaristic, cu cifră de afaceri în anul precedent peste 50.000.000 euro, care intră în sfera impozitului minim pe cifra de afaceri (nu este operator reglementat/licențiat exceptat) și care nu are sponsorizări, deduceri suplimentare de cercetare-dezvoltare sau alte sume de scăzut.*

> **Impozitul minim pe cifra de afaceri este 2.700.000 lei, mai mare decât impozitul pe profit calculat, deci societatea datorează pentru 2026 impozit pe profit la nivelul impozitului minim: 2.700.000 lei. [calcul: IMCA = cota * (VT - Vs - I - A) = 2.700.000; impozit_datorat = max(IMCA, impozit_profit) = 2.700.000]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul — evaluat de cod, nu de model

- `IMCA = cota * (VT - Vs - I - A)` → **2.700.000**
  - `cota` = 1% — din `cod_fiscal_227_2015_consolidat#art18^1/alin3`: „Impozitul minim pe cifra de afaceri se determină astfel: IMCA = 1% x (VT – Vs – I – A)”
  - `VT` = 300.000.000 — din întrebare: „VT = 300.000.000 lei”
  - `Vs` = 20.000.000 — din întrebare: „Vs = 20.000.000 lei”
  - `I` = 0 — din întrebare: „I = 0”
  - `A` = 10.000.000 — din întrebare: „A = 10.000.000 lei”
- `impozit_datorat = max(IMCA, impozit_profit)` → **2.700.000**
  - `impozit_profit` = 1.000.000 — din întrebare: „impozitul pe profit anual calculat (fără sponsorizări sau alte sume de scăzut) = 1.000.000 lei”

- **Codul fiscal (Legea 227/2015) art. 18^1 alin. (1)** — `cod_fiscal_227_2015_consolidat#art18^1/alin1` · valabil din nedovedit
  > care în anul de calcul determină un impozit pe profit, cumulat de la începutul anului fiscal/anului fiscal modificat până la sfârșitul trimestrului/anului de calcul, mai mic decât impozitul minim pe cifra de afaceri stabilit potrivit prevederilor alin. (3) , sunt obligați la plata impozitului pe profit la nivelul impozitului minim pe cifra de afaceri.
- **Codul fiscal (Legea 227/2015) art. 18^1 alin. (1)** — `cod_fiscal_227_2015_consolidat#art18^1/alin1` · valabil din nedovedit
  > Contribuabilii, alții decât cei prevăzuți la art. 15 , care înregistrează în anul precedent o cifră de afaceri de peste 50.000.000 euro și care în anul de calcul determină un impozit pe profit
- **Codul fiscal (Legea 227/2015) art. 18^1 alin. (3)** — `cod_fiscal_227_2015_consolidat#art18^1/alin3` · valabil din 2024-01-01
  > Impozitul minim pe cifra de afaceri se determină astfel: IMCA = 1% x (VT – Vs – I – A), unde indicatorii au următoarea semnificație: IMCA - impozit minim pe cifra de afaceri, determinat cumulat de la începutul anului fiscal/anului fiscal modificat până la sfârșitul trimestrului/anului de calcul;
- **Codul fiscal (Legea 227/2015) art. 18^1 alin. (4)** — `cod_fiscal_227_2015_consolidat#art18^1/alin4` · valabil din nedovedit
  > În aplicarea prevederilor alin. (3) , în cazul în care din aplicarea formulei de calcul pentru determinarea impozitului minim pe cifra de afaceri rezultă o valoare negativă, impozitul minim este zero.

### Navigarea (8 pași, 5 ture)

1. `cauta` {"interogare": "impozit minim pe cifra de afaceri IMCA 1% VT Vs I A"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "impozit minim pe cifra de afaceri"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art18^1/alin3"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art18^1/alin1"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art18^1"}
6. `cauta` {"interogare": "abrogare art. 18^1 impozit minim pe cifra de afaceri începând cu 1 ianuarie 2026"}
7. `cuprins` {"act": "legea_141_2025_consolidat", "filtru": "impozit minim"}
8. `cauta` {"interogare": "Legea 141/2025 abrogă impozitul minim pe cifra de afaceri articolul 18^1 din Legea 227/2015"}

Apel: `claude-opus-5`, {'intrare': 10, 'iesire': 5518, 'cache_scriere': 12073, 'cache_citire': 54454} tokeni, $0.2407, 72 s

Pe fond: **GREȘIT** — faptul principal al cheii (['1.350.000 lei']) nu e in raspuns

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți nu conțin regula de determinare a impozitului minim pe cifra de afaceri (formula cu VT, Vs, I, A și cota aplicabilă, prevăzute la art. 18^1 alin. (3)); art. 18^1 alin. (1) doar face trimitere la alin. (3), care lipsește din context. În plus, stabilirea sumei ar presupune un calcul (scăderi și aplicarea unei cote) al cărui rezultat nu apare literal în niciun atom, ceea ce nu îmi este permis.

## Cheia

- 1.350.000 lei — IMCA = 0,5% × (300.000.000 − 20.000.000 − 0 − 10.000.000) = 1.350.000 > 1.000.000, deci plătește la nivelul IMCA (nu 1%, care ar da 2.700.000)
- temei: Cod fiscal art. 18^1 alin. (1) și (3); alin. (16) (cota 0,5% pentru anul fiscal 2026, introdus de OUG 89/2025 art. I pct. 1); alin. (17) (articolul se aplică până la 31.12.2026)
