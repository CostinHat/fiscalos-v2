# Q-CTB-03 — CALCUL

**Întrebarea:** Un utilaj nou din subgrupa 2.1 (echipamente tehnologice), valoare fiscală 100.000 lei, achiziționat și pus în funcțiune în aprilie 2026. Contribuabilul aplică metoda superaccelerată. Care este amortizarea fiscală maximă în primul an de utilizare?

## Stratul semantic — RĂSPUNS

*La data de referință aprilie 2026, presupun un contribuabil plătitor de impozit pe profit, cu an fiscal calendaristic, care a achiziționat și pus în funcțiune un activ nou din subgrupa 2.1 în aprilie 2026 și care optează pentru metoda de amortizare superaccelerată, fără a aplica scutirea de impozit a profitului reinvestit pentru acest activ (întrebarea nu menționează o astfel de scutire).*

> **În primul an de utilizare, amortizarea fiscală nu poate depăși 65% din valoarea fiscală a activului de la data intrării în patrimoniu.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 28 alin. (8^1) lit. a)** — `cod_fiscal_227_2015_consolidat#art28/alin8^1/lita` · valabil din nedovedit
  > pentru primul an de utilizare, amortizarea nu poate depăși 65% din valoarea fiscală de la data intrării în patrimoniul contribuabilului a activului;
- **Codul fiscal (Legea 227/2015) art. 28 alin. (8^1)** — `cod_fiscal_227_2015_consolidat#art28/alin8^1` · valabil din nedovedit
  > pentru activele noi, achiziționate/produse și puse în funcțiune, în perioada cuprinsă între 1 ianuarie 2026-31 decembrie 2026 inclusiv, respectiv în anul fiscal modificat care începe în anul 2026, după caz, din subgrupa 2.1 - Echipamente tehnologice, respectiv mașini, unelte și instalații de lucru
- derogare tratată: `cod_fiscal_227_2015_consolidat#art28/alin8/lita` — Regula generală a amortizării accelerate (maximum 50% în primul an) nu se aplică, fiind înlăturată expres pentru cazul din întrebare de excepția din alin. (8^1), care privește activele noi din subgrupa 2.1 puse în funcțiune în 2026.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art28/alin5/litb` — Opțiunea generală între metodele liniară, degresivă sau accelerată este înlăturată prin excepția din alin. (8^1), contribuabilul aplicând metoda superaccelerată permisă pentru anul 2026.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art22/alin9` — Interdicția de a opta pentru amortizarea superaccelerată vizează contribuabilii care aplică scutirea profitului reinvestit (art. 22 alin. (1)) pentru activele respective; întrebarea nu indică aplicarea unei astfel de scutiri pentru acest utilaj, deci restricția nu se aplică cazului.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art28/alin8^3/lita` — Regulile privind anul fiscal modificat care începe în 2026 nu se aplică, întrucât se presupune an fiscal calendaristic, iar punerea în funcțiune are loc în aprilie 2026, în intervalul 1 ianuarie–31 decembrie 2026.

Apel: `claude-opus-5`, {'intrare': 6132, 'iesire': 2341, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0901

Pe fond: **GREȘIT** — faptul principal al cheii (['65.000 lei']) nu e in raspuns

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-04-30 (luna, din "aprilie 2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: R-CALC: niciun atom din primii 5 nu da O SINGURA cota


Pe fond: **NU POT** — R-CALC: niciun atom din primii 5 nu da O SINGURA cota

## Cheia

- 65.000 lei (maxim 65% din valoarea fiscală de intrare); restul de 35.000 lei se amortizează în anii următori raportat la durata normală de utilizare rămasă.
- temei: Legea 227/2015 art. 28 alin. (8^1) lit. a) și b), introdus de OUG 8/2026 art. 6 pct. 8, pentru active noi puse în funcțiune 01.01.2026-31.12.2026
