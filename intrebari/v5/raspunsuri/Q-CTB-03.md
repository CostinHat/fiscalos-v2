# Q-CTB-03 — CALCUL

**Întrebarea:** Un utilaj nou din subgrupa 2.1 (echipamente tehnologice), valoare fiscală 100.000 lei, achiziționat și pus în funcțiune în aprilie 2026. Contribuabilul aplică metoda superaccelerată. Care este amortizarea fiscală maximă în primul an de utilizare?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 30.04.2026, presupun un contribuabil plătitor de impozit pe profit care deduce amortizarea fiscală pentru un activ nou din subgrupa 2.1 - Echipamente tehnologice, achiziționat și pus în funcțiune în anul 2026 (an fiscal calendaristic), pentru care optează pentru metoda de amortizare superaccelerată prevăzută ca excepție pentru activele puse în funcțiune în perioada 1 ianuarie 2026-31 decembrie 2026.*

Datele din întrebare: 2026-04-30 · data de referință aleasă: **2026-04-30** — Singura dată din întrebare; punerea în funcțiune în aprilie 2026 determină regimul de amortizare aplicabil primului an.

> **Pentru primul an de utilizare, amortizarea fiscală nu poate depăși 65% din valoarea fiscală a activului, deci maximul deductibil este 65.000 lei; valoarea rămasă se amortizează în următorii ani prin raportare la durata normală de utilizare rămasă.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul, pas cu pas — evaluat de cod, nu de model

- `amortizare_maxima_an1 = valoare_fiscala * cota_primul_an` = (100.000 × 65%) = **65.000**
  - `valoare_fiscala` = 100.000 — FAPT_CAZ (din întrebare): „valoare fiscală 100.000 lei”
  - `cota_primul_an` = 65% — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art28/alin8^1/lita`: „amortizarea nu poate depăși 65% din valoarea fiscală”

- **Codul fiscal (Legea 227/2015) art. 28 alin. (8^1) lit. a)** — `cod_fiscal_227_2015_consolidat#art28/alin8^1/lita` · valabil din nedovedit
  > pentru primul an de utilizare, amortizarea nu poate depăși 65% din valoarea fiscală de la data intrării în patrimoniul contribuabilului a activului;
- **Codul fiscal (Legea 227/2015) art. 28 alin. (8^1)** — `cod_fiscal_227_2015_consolidat#art28/alin8^1` · valabil din nedovedit
  > pentru activele noi, achiziționate/produse și puse în funcțiune, în perioada cuprinsă între 1 ianuarie 2026-31 decembrie 2026 inclusiv, respectiv în anul fiscal modificat care începe în anul 2026, după caz, din subgrupa 2.1 - Echipamente tehnologice, respectiv mașini, unelte și instalații de lucru și/sau subgrupa 2.4 - «Animale și plantații» se poate aplica o metodă de amortizare superaccelerată
- **Codul fiscal (Legea 227/2015) art. 28 alin. (8^1) lit. b)** — `cod_fiscal_227_2015_consolidat#art28/alin8^1/litb` · valabil din 2026-02-25
  > pentru următorii ani de utilizare, amortizarea se calculează prin raportarea valorii rămas
- derogare tratată: `cod_fiscal_227_2015_consolidat#art28/alin8^1` — Este chiar regula aplicată: excepție de la art. 28 alin. (5) și (8) (amortizare liniară/degresivă/accelerată cu maxim 50% în primul an), aplicabilă activelor noi din subgrupa 2.1 puse în funcțiune în 2026 - exact situația din întrebare.

### Navigarea (4 pași, 3 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Amortizare"}
2. `cauta` {"interogare": "amortizare accelerată primul an de utilizare 50% din valoarea fiscală"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art28/alin8^1"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art28/alin5/litb"}

Apel: `claude-opus-5`, {'intrare': 6, 'iesire': 2796, 'cache_scriere': 3474, 'cache_citire': 23639} tokeni, $0.1035, 37 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — NU POT, pe fond NU POT

> VERIFICAREA CALCULULUI a respins propunerea: operandul valoare_fiscala=100.000 e o valoare legala luata din intrebare (C13: numai din atom)

## Cheia

- 65.000 lei (maxim 65% din valoarea fiscală de intrare); restul de 35.000 lei se amortizează în anii următori raportat la durata normală de utilizare rămasă.
- temei: Legea 227/2015 art. 28 alin. (8^1) lit. a) și b), introdus de OUG 8/2026 art. 6 pct. 8, pentru active noi puse în funcțiune 01.01.2026-31.12.2026
