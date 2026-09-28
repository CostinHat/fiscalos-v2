# Q-CTB-01 — PARAMETRU

**Întrebarea:** Care este valoarea fiscală minimă de intrare de la care o imobilizare corporală este mijloc fix amortizabil în anul fiscal 2026?

## Stratul semantic — RĂSPUNS

*La data de referință 28.09.2026, pentru anul fiscal 2026, presupun un contribuabil plătitor de impozit pe profit care aplică regulile de amortizare fiscală din Codul fiscal pentru o imobilizare corporală intrată în patrimoniu, fără a analiza reguli contabile speciale sau eventuale actualizări prin hotărâre a Guvernului nedovedite în context.*

> **Valoarea fiscală minimă la data intrării în patrimoniu este de 5.000 lei: imobilizarea corporală este mijloc fix amortizabil dacă are o valoare fiscală egală sau mai mare decât 5.000 lei (limită care se actualizează anual, în funcție de indicele de inflație, prin hotărâre a Guvernului), cu îndeplinirea cumulativă și a celorlalte condiții (deținere/utilizare în scopurile prevăzute și durată normală de utilizare mai mare de un an).**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 28 alin. (2) lit. b)** — `cod_fiscal_227_2015_consolidat#art28/alin2/litb` · valabil din 2026-02-25
  > la data intrării în patrimoniul contribuabilului, are o valoare fiscală egală sau mai mare decât suma de 5.000 lei; această limită se actualizată anual, în funcție de indicele de inflație, prin hotărâre a Guvernului;
- **Codul fiscal (Legea 227/2015) art. 28 alin. (2)** — `cod_fiscal_227_2015_consolidat#art28/alin2` · valabil din nedovedit
  > Mijlocul fix amortizabil este orice imobilizare corporală care îndeplinește cumulativ următoarele condiții:
- **Codul fiscal (Legea 227/2015) art. 28 alin. (2) lit. c)** — `cod_fiscal_227_2015_consolidat#art28/alin2/litc` · valabil din nedovedit
  > are o durată normală de utilizare mai mare de un an. ...
- derogare tratată: `cod_fiscal_227_2015_consolidat#art28/alin8^1` — Această excepție (amortizare superaccelerată pentru active noi din subgrupele 2.1 și 2.4 puse în funcțiune în 2026) derogă doar de la alin. (5) și alin. (8) lit. a), privind metoda/regimul de amortizare, nu de la condiția de valoare minimă de intrare din alin. (2) lit. b), deci nu afectează pragul c…

Apel: `claude-opus-5`, {'intrare': 2855, 'iesire': 1210, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0455

Pe fond: **CORECT** — faptul principal si articolul coincid

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **5.000 lei**

Motiv: valoarea de forma cerută (suma) din atomul care poarta o asemenea valoare si potriveste cel mai bine cuvintele rare ale intrebarii (scor local 7.3)

- **Codul fiscal (Legea 227/2015) art. 28 alin. (2) lit. b)** — `cod_fiscal_227_2015_consolidat#art28/alin2/litb` · valabil din 2026-02-25
  > la data intrării în patrimoniul contribuabilului, are o valoare fiscală egală sau mai mare decât suma de 5.000 lei; această limită se actualizată anual, în funcție de indicele de inflație, prin hotărâre a Guvernului; Notă ... Potrivit alin. (2) al art. 10 din ORDONANȚA DE URGENȚĂ nr. 8 din 24 februarie 2026, publicată în MONITORUL OFICIAL nr. 147 din 25 februarie 2026, prevederile art. 6 pct. 7 se aplică începând cu anul fiscal 2026. ...

Pe fond: **CORECT** — faptul principal si articolul coincid

## Cheia

- 5.000 lei (egală sau mai mare), limită actualizabilă anual cu inflația prin HG; până în 2025 limita era 2.500 lei (HG 276/2013).
- temei: Legea 227/2015 (Cod fiscal) art. 28 alin. (2) lit. b), modificat de OUG 8/2026 art. 6 pct. 7, aplicabil de la anul fiscal 2026 (OUG 8/2026 art. 10 alin. (2)); HG 276/2013 art. 1 alin. (1) pentru limita anterioară
