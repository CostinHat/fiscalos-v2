# Q-CTB-03 — CALCUL

**Întrebarea:** Un utilaj nou din subgrupa 2.1 (echipamente tehnologice), valoare fiscală 100.000 lei, achiziționat și pus în funcțiune în aprilie 2026. Contribuabilul aplică metoda superaccelerată. Care este amortizarea fiscală maximă în primul an de utilizare?

## Stratul de navigare (v4) — NU POT RĂSPUNDE

*La data de referință aprilie 2026, presupun un contribuabil plătitor de impozit pe profit care deține un activ nou din subgrupa 2.1 - Echipamente tehnologice, achiziționat și pus în funcțiune în 2026, pentru care optează pentru metoda de amortizare superaccelerată și care nu aplică scutirea de impozit pentru profitul reinvestit.</declaratie>
<parameter name="raspuns">Pentru primul an de utilizare, amortizarea fiscală nu poate depăși 65% din valoarea fiscală de la data intrării activului în patrimoniu (aplicată la valoarea fiscală de 100.000 lei din speță).*

Motiv: VERIFICAREA CALCULULUI a respins propunerea: operandul valoare_fiscala=100.000 e o valoare legala luata din intrebare (C13: numai din atom)

### Calculul — evaluat de cod, nu de model

- `amortizare_maxima_an1 = valoare_fiscala * cota` → **65.000**
  - `valoare_fiscala` = 100.000 — din întrebare: „valoare fiscală 100.000 lei”
  - `cota` = 65% — din `cod_fiscal_227_2015_consolidat#art28/alin8^1/lita`: „amortizarea nu poate depăși 65% din valoarea fiscală de la data intrării în patrimoniul contribuabilului a activului”

- **Codul fiscal (Legea 227/2015) art. 28 alin. (8^1) lit. a)** — `cod_fiscal_227_2015_consolidat#art28/alin8^1/lita` · valabil din nedovedit
  > pentru primul an de utilizare, amortizarea nu poate depăși 65% din valoarea fiscală de la data intrării în patrimoniul contribuabilului a activului;
- **Codul fiscal (Legea 227/2015) art. 28 alin. (8^1)** — `cod_fiscal_227_2015_consolidat#art28/alin8^1` · valabil din nedovedit
  > pentru activele noi, achiziționate/produse și puse în funcțiune, în perioada cuprinsă între 1 ianuarie 2026-31 decembrie 2026 inclusiv, respectiv în anul fiscal modificat care începe în anul 2026, după caz, din subgrupa 2.1 - Echipamente tehnologice, respectiv mașini, unelte și instalații de lucru și/sau subgrupa 2.4 - «Animale și plantații» se poate aplica o metodă de amortizare superaccelerată
- derogare tratată: `cod_fiscal_227_2015_consolidat#art28/alin5` — Art. 28 alin. (8^1) este excepție expresă de la alin. (5) și (8); pentru activele noi din subgrupa 2.1 puse în funcțiune în 2026 se aplică regula specială superaccelerată, deci alin. (5)/(8) nu guvernează cazul.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art22/alin9` — Interdicția de a opta pentru amortizarea accelerată/superaccelerată vizează activele pentru care se aplică scutirea de impozit a profitului reinvestit; întrebarea nu indică aplicarea acestei scutiri, deci nu se aplică.

### Navigarea (4 pași, 3 ture)

1. `cauta` {"interogare": "amortizare accelerată 50% primul an de utilizare echipamente tehnologice"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "amortizare"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art28/alin8^1"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art28/alin8^1/lita"}

Apel: `claude-opus-5`, {'intrare': 6, 'iesire': 3199, 'cache_scriere': 3051, 'cache_citire': 21221} tokeni, $0.1097, 45 s

Pe fond: **NU POT** — VERIFICAREA CALCULULUI a respins propunerea: operandul valoare_fiscala=100.000 e o valoare legala luata din intrebare (C13: numai din atom)

## Stratul semantic v3 (context dat de căutare) — RĂSPUNS, pe fond GREȘIT

> În primul an de utilizare, amortizarea fiscală nu poate depăși 65% din valoarea fiscală a activului de la data intrării în patrimoniu.

## Cheia

- 65.000 lei (maxim 65% din valoarea fiscală de intrare); restul de 35.000 lei se amortizează în anii următori raportat la durata normală de utilizare rămasă.
- temei: Legea 227/2015 art. 28 alin. (8^1) lit. a) și b), introdus de OUG 8/2026 art. 6 pct. 8, pentru active noi puse în funcțiune 01.01.2026-31.12.2026
