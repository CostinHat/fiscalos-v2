# Q3-CPF-07 — CALCUL

**Întrebarea:** O SRL a achitat integral pe 10.02.2026 suma de 50.000 lei stabilită printr-o decizie de impunere emisă de ANAF. Decizia a fost anulată definitiv de instanță, iar ANAF i-a restituit suma pe 30.06.2026. Firma nu a cerut despăgubiri în temeiul art. 18 din Legea 554/2004 și solicită acum dobânda. Ce dobândă i se cuvine? (La numărarea zilelor, ambele capete ale intervalului se includ.)

## RĂSPUNS

> **I se cuvine dobândă de 0,02% pentru fiecare zi, calculată la suma de 50.000 lei, de la ziua stingerii (10.02.2026) până în ziua restituirii (30.06.2026), adică 141 zile, rezultând o dobândă de 1.410 lei. [calcul: zile(10.02.2026, 30.06.2026) = 140 zile; zile_total = zile(data_plata, data_restituire) + 1 = (zile(10.02.2026, 30.06.2026) + 1) = 141; dobanda = suma * nivel_dobanda * zile_total = ((50.000 × 0,02%) × 141) = 1.410] [data de referință: 30.06.2026 — Faptul întrebat este dobânda cuvenită pentru perioada care se încheie în ziua restituirii sumei, 30.06.2026, dată la care se determină integral dreptul la dobândă.]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- `zile(10.02.2026, 30.06.2026) = 140 zile`
- `zile_total = zile(data_plata, data_restituire) + 1` = (zile(10.02.2026, 30.06.2026) + 1) = **141**
- `dobanda = suma * nivel_dobanda * zile_total` = ((50.000 × 0,02%) × 141) = **1.410**
- **Codul de procedură fiscală (Legea 207/2015) art. 182 alin. (2)** — `legea_207_2015_consolidat#art182/alin2`
  > contribuabilul/plătitorul este îndreptățit la dobândă începând cu ziua în care a operat stingerea creanței fiscale individualizate în actul administrativ anulat și până în ziua restituirii sau compensării creanței contribuabilului/plătitorului rezultate în urma anulării actului administrativ fiscal
- **Codul de procedură fiscală (Legea 207/2015) art. 182 alin. (2)** — `legea_207_2015_consolidat#art182/alin2`
  > Această prevedere nu se aplică în situația în care contribuabilul/plătitorul a solicitat acordarea de despăgubiri, în condițiile art. 18 din Legea nr. 554/2004 , cu modificările și completările ulterioare, precum și în situația prevăzută la art. 107 alin. (5) .
- **Codul de procedură fiscală (Legea 207/2015) art. 182 alin. (4)** — `legea_207_2015_consolidat#art182/alin4`
  > Nivelul dobânzii este cel prevăzut la art. 174 alin. (5) și se suportă din același buget din care se restituie ori se rambursează, după caz, sumele solicitate de contribuabil/plătitor.
- **Codul de procedură fiscală (Legea 207/2015) art. 174 alin. (5)** — `legea_207_2015_consolidat#art174/alin5`
  > Nivelul dobânzii este de 0,02% pentru fiecare zi de întârziere.

Navigare: 8 pași, 7 ture; {'intrare': 14, 'iesire': 4204, 'cache_scriere': 16804, 'cache_citire': 72670} tokeni; $0.2465; 67 s

Cauza (dacă NU POT): RASPUNS

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## Cheia

- 1.410 lei. În cazul sumelor rezultate din anularea unui act administrativ fiscal stinse anterior anulării, dobânda curge din ziua în care a operat stingerea (10.02.2026), nu după expirarea termenului de 45 de zile de soluționare a cererii, până în ziua restituirii (30.06.2026): 19 zile (10–28.02) + 31 + 30 + 31 + 30 = 141 zile. Nivel: 0,02% pe zi (art. 174 alin. 5). Dobânda = 50.000 × 0,02% × 141 = 10 lei/zi × 141 = 1.410 lei. Dreptul de a cere dobânda se prescrie în 5 ani de la 1 ianuarie a anului următor rămânerii definitive a anulării.
- temei: Legea 207/2015 art. 182 alin. (2); art. 182 alin. (4); art. 174 alin. (5)
