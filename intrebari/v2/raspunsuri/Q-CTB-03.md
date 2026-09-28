# Q-CTB-03 — CALCUL

**Întrebarea:** Un utilaj nou din subgrupa 2.1 (echipamente tehnologice), valoare fiscală 100.000 lei, achiziționat și pus în funcțiune în aprilie 2026. Contribuabilul aplică metoda superaccelerată. Care este amortizarea fiscală maximă în primul an de utilizare?

## Stratul semantic (motorul nou) — RĂSPUNS

*La data de referință aprilie 2026, presupun un plătitor de impozit pe profit cu an fiscal calendaristic, care a achiziționat și pus în funcțiune în 2026 un activ nou din subgrupa 2.1 și optează pentru metoda de amortizare superaccelerată, presupunând totodată că nu aplică scutirea de impozit a profitului reinvestit pentru acel activ (caz în care opțiunea pentru amortizarea superaccelerată nu ar fi permisă).*

> **În primul an de utilizare, amortizarea fiscală nu poate depăși 65% din valoarea fiscală de la data intrării în patrimoniu, deci maximum 65% din cei 100.000 lei.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 28 alin. (8^1)** — `cod_fiscal_227_2015_consolidat#art28/alin8^1` · valabil din nedovedit
  > se poate aplica o metodă de amortizare superaccelerată potrivit căreia amortizarea se calculează după cum urmează: a) pentru primul an de utilizare, amortizarea nu poate depăși 65% din valoarea fiscală de la data intrării în patrimoniul contribuabilului a activului;
- **Codul fiscal (Legea 227/2015) art. 28 alin. (8^1)** — `cod_fiscal_227_2015_consolidat#art28/alin8^1` · valabil din nedovedit
  > Prin excepție de la prevederile alin. (5) și (8) , pentru activele noi, achiziționate/produse și puse în funcțiune, în perioada cuprinsă între 1 ianuarie 2026-31 decembrie 2026 inclusiv, respectiv în anul fiscal modificat care începe în anul 2026, după caz,
- **Codul fiscal (Legea 227/2015) art. 22 alin. (9)** — `cod_fiscal_227_2015_consolidat#art22/alin9` · valabil din nedovedit
  > Contribuabilii care aplică prevederile alin. (1) nu pot opta pentru metoda de amortizare accelerată/superaccelerată, potrivit art. 28 alin. (5) lit. b) și alin. (8^1) , pentru activele respective.

Apel: `claude-opus-5`, {'intrare': 6570, 'iesire': 2258, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0901, 28.4 s

Pe fond: **GREȘIT** — faptul principal al cheii (['65.000 lei']) nu e in raspuns

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-04-30 (luna, din "aprilie 2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **100.000 lei x 65% = 65000,00 lei**

Motiv: R-CALC: o baza, o cota; baza x cota

- **Codul fiscal (Legea 227/2015) art. 28 alin. (8^1)** — `cod_fiscal_227_2015_consolidat#art28/alin8^1` · valabil din nedovedit
  > Prin excepție de la prevederile alin. (5) și (8) , pentru activele noi, achiziționate/produse și puse în funcțiune, în perioada cuprinsă între 1 ianuarie 2026-31 decembrie 2026 inclusiv, respectiv în anul fiscal modificat care începe în anul 2026, după caz, din subgrupa 2.1 - Echipamente tehnologice, respectiv mașini, unelte și instalații de lucru și/sau subgrupa 2.4 - «Animale și plantații» se poate aplica o metodă de amortizare superaccelerată potrivit căreia amortizarea se calculează după cum urmează: a) pentru primul an de utilizare, amortizarea nu poate depăși 65% din valoarea fiscală de …

Pe fond: **GREȘIT** — faptul principal al cheii (['65.000 lei']) nu e in raspuns

## Cheia

- răspuns așteptat: 65.000 lei (maxim 65% din valoarea fiscală de intrare); restul de 35.000 lei se amortizează în anii următori raportat la durata normală de utilizare rămasă.
- temei așteptat: Legea 227/2015 art. 28 alin. (8^1) lit. a) și b), introdus de OUG 8/2026 art. 6 pct. 8, pentru active noi puse în funcțiune 01.01.2026-31.12.2026

