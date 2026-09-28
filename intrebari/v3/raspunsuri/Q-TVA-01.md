# Q-TVA-01 — PARAMETRU

**Întrebarea:** Care este cota standard de TVA aplicabilă în 2026?

## Stratul semantic — RĂSPUNS

*La data de referință 28.09.2026, presupunând o operațiune impozabilă în România care nu este scutită de TVA și nici supusă unei cote reduse, efectuată de o persoană impozabilă înregistrată în scopuri de TVA în regim normal (întrebarea nu precizează tipul operațiunii sau al contribuabilului), cota standard de TVA este cea prevăzută de Codul fiscal în vigoare în 2026.*

> **Cota standard de TVA este 21%.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 291 alin. (1)** — `cod_fiscal_227_2015_consolidat#art291/alin1` · valabil din 2025-08-01
  > Cota standard se aplică asupra bazei de impozitare pentru operațiunile impozabile care nu sunt scutite de taxă sau care nu sunt supuse cotei reduse, iar nivelul acesteia este 21%.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art315^3/alin4` — Regula specială privind mecanismul special pentru declararea și plata TVA la import derogă de la cotele reduse (art. 291 alin. (2) și (3)) și trimite tot la cota standard din art. 291 alin. (1), deci nu modifică nivelul cotei standard aplicabile în 2026.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art291/alin3^5/lita` — Se referă la cota redusă de 5% pentru achiziția de locuințe și la verificările notariale, nu la nivelul cotei standard; nu se aplică întrebării privind cota standard.
- derogare tratată: `legea_141_2025_consolidat#artIII/alin1` — Vizează cota redusă de 9% pentru achiziția unei locuințe în perioada 1 august 2025-31 iulie 2026, deci o excepție de la cota standard doar pentru acele livrări, nu o modificare a nivelului cotei standard.

Apel: `claude-opus-5`, {'intrare': 5763, 'iesire': 966, 'cache_scriere': 1923, 'cache_citire': 0} tokeni, $0.0650

Pe fond: **CORECT** — faptul principal si articolul coincid

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **5%**

Motiv: valoarea de forma cerută (procent) din atomul care poarta o asemenea valoare si potriveste cel mai bine cuvintele rare ale intrebarii (scor local 13.3)

- **Codul fiscal (Legea 227/2015) art. 291 alin. (3^5) lit. a)** — `cod_fiscal_227_2015_consolidat#art291/alin3^5/lita` · valabil din 2023-01-01
  > să verifice îndeplinirea condiției referitoare la achiziția unei singure locuințe a cărei valoare nu depășește suma de 600.000 lei, exclusiv TVA, cu cota redusă de TVA de 5%, prin consultarea «Registrului achizițiilor de locuințe cu cota redusă de TVA de 5%, începând cu 1 ianuarie 2023», înainte de autentificarea actelor juridice între vii care au ca obiect transferul dreptului de proprietate sau plata în avans pentru achiziția unei astfel de locuințe și, în situația în care constată că nu este …

Pe fond: **GREȘIT** — faptul principal al cheii (['21%']) nu e in raspuns

## Cheia

- 21%
- temei: Legea 227/2015 (Cod fiscal) art. 291 alin. (1), forma modificată de Legea 141/2025 art. II pct. 42, în vigoare de la 01.08.2025
