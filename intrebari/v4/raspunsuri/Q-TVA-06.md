# Q-TVA-06 — CAPCANA

**Întrebarea:** O firmă cu perioadă fiscală trimestrială face o livrare intracomunitară scutită în februarie 2026. Depune D390 trimestrial, odată cu D300 din aprilie?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 28.02.2026, presupun o persoană impozabilă stabilită în România, înregistrată în scopuri de TVA conform art. 316, cu perioadă fiscală trimestrială la TVA, care a efectuat în februarie 2026 o livrare intracomunitară de bunuri scutită ce trebuie raportată în declarația recapitulativă (D390).*

> **Nu. Declarația recapitulativă 390 se depune lunar, până la data de 25 inclusiv a lunii următoare lunii calendaristice în care a intervenit operațiunea, indiferent de faptul că perioada fiscală pentru TVA (decontul D300) este trimestrială. Deci pentru livrarea intracomunitară din februarie 2026 D390 se depune până la 25 ale lunii următoare, nu în aprilie odată cu decontul trimestrial.**

Citatul decisiv (`opanaf_705_2020_d390#art10/pct3/pct3/pct6/pct1/pct1`):
> Declaraţia recapitulativă se depune lunar, până la data de 25 inclusiv a lunii următoare unei luni calendaristice, de către persoanele impozabile înregistrate în scopuri de TVA conform art. 316 sau 317 din Codul fiscal.

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **OPANAF 705/2020 art. 10 pct. 3 pct. 3 pct. 6 pct. 1 pct. 1** — `opanaf_705_2020_d390#art10/pct3/pct3/pct6/pct1/pct1` · valabil din nedovedit
  > Declaraţia recapitulativă se depune lunar, până la data de 25 inclusiv a lunii următoare unei luni calendaristice, de către persoanele impozabile înregistrate în scopuri de TVA conform art. 316 sau 317 din Codul fiscal.
- **Codul fiscal (Legea 227/2015) art. 325 alin. (2)** — `cod_fiscal_227_2015_consolidat#art325/alin2` · valabil din 2024-07-01
  > Declarația se întocmește pentru fiecare lună calendaristică în care ia naștere exigibilitatea taxei pentru operațiunile prevăzute la alin. (1)
- **Codul fiscal (Legea 227/2015) art. 325 alin. (4)** — `cod_fiscal_227_2015_consolidat#art325/alin4` · valabil din nedovedit
  > Declarațiile recapitulative se depun numai pentru perioadele în care ia naștere exigibilitatea taxei pentru operațiunile menționate la alin. (1)
- derogare tratată: `cod_fiscal_227_2015_consolidat#art325/alin2` — Nota la acest alineat privește o excepție punctuală (declarația aferentă lunii iunie 2024, OUG 70/2024), care nu se aplică unei operațiuni din februarie 2026.

### Navigarea (4 pași, 3 ture)

1. `cauta` {"interogare": "declarația recapitulativă 390 lunar până la data de 25 inclusiv a lunii următoare"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "recapitulativ"}
3. `deschide` {"id": "opanaf_705_2020_d390#art10/pct3/pct3/pct6/pct1/pct1"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art325/alin2"}

Apel: `claude-opus-5`, {'intrare': 6, 'iesire': 1697, 'cache_scriere': 3278, 'cache_citire': 21060} tokeni, $0.0735, 22 s

Pe fond: **GREȘIT** — faptul principal al cheii (['25.03.2026']) nu e in raspuns

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Niciun atom primit nu conține regula privind periodicitatea și termenul de depunere a declarației recapitulative (D390) prevăzută la art. 325 din Codul fiscal. Atomul din OPANAF 3769/2015 se referă la altă declarație informativă (D394), iar norma citată (art. V alin. (2)) arată doar că exigibilitatea determină perioada în care livrarea intracomunitară scutită se înscrie în decont și în declarația recapitulativă, fără a stabili dacă declarația recapitulativă se depune lunar s…

## Cheia

- Nu. D390 se depune lunar, pentru luna în care a luat naștere exigibilitatea, nu trimestrial cu D300. Exigibilitatea la livrarea intracomunitară = data facturii sau, dacă factura nu s-a emis până atunci, 15 a lunii următoare faptului generator. Factură emisă în februarie → D390 pentru februarie, până la 25.03.2026. Fără factură până la 15.03.2026 → D390 pentru martie, termen 25.04.2026 (sâmbătă), efectiv 27.04.2026.
- temei: Cod fiscal art. 283 alin. (1); art. 325 alin. (1) lit. a) și alin. (2); OPANAF 705/2020 anexa 2 pct. 1.1-1.2; CPF art. 75
