# Q-PRF-01 — PARAMETRU

**Întrebarea:** Ce cotă de impozit pe veniturile microîntreprinderilor se aplică în 2026 unei microîntreprinderi care realizează venituri din consultanță, și cu ce cod de obligație se declară în D100?

## Stratul semantic — NU POT RĂSPUNDE

*La data de referință 28.09.2026, presupun o microîntreprindere persoană juridică română plătitoare de impozit pe veniturile microîntreprinderilor care obține venituri din consultanță și care declară trimestrial prin D100.*

Motiv: modelul s-a abţinut: Atomii primiți nu conțin nicio dispoziție privind cotele de impozit pe veniturile microîntreprinderilor (nici regula specială pentru veniturile din consultanță) aplicabile în 2026, nici nomenclatorul codurilor de obligații de plată din formularul D100. Fragmentele furnizate se referă la bonificația de 3% pentru anul fiscal 2025 și la reguli de valoare fiscală/amortizare din titlul impozitului pe profit, fără legătură cu întrebarea.


Apel: `claude-opus-5`, {'intrare': 5008, 'iesire': 319, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0340

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți nu conțin nicio dispoziție privind cotele de impozit pe veniturile microîntreprinderilor (nici regula specială pentru veniturile din consultanță) aplicabile în 2026

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: C17 (b): atomul pe care as raspunde are 4 derogari/exceptii/modificari valabile la data intrebarii (ex. cod_fiscal_227_2015_consolidat#art28/alin13: "Prin excepție de la prevederile art. 7 pct. 44"); motorul lexical nu le poate trata, deci se abţine.

- **Codul fiscal (Legea 227/2015) art. 7 alin. (1)** — `cod_fiscal_227_2015_consolidat#art7~2/alin1` · valabil din nedovedit
  > Contribuabilii plătitori de impozit pe profit, indiferent de sistemul de declarare și plată prevăzut la art. 41 din Legea nr. 227/2015 privind Codul fiscal, cu modificările și completările ulterioare, precum și contribuabilii plătitori de impozit pe veniturile microîntreprinderilor, potrivit titlului III „Impozitul pe veniturile microîntreprinderilor“ din aceeași lege, beneficiază de o bonificație de 3% din impozitul pe profit anual/impozitul pe veniturile microîntreprinderilor, aferente anului …

Pe fond: **NU POT** — C17 (b): atomul pe care as raspunde are 4 derogari/exceptii/modificari valabile la data intrebarii (ex. cod_fiscal_227_2015_consolidat#art28/alin13: "Prin excepție de la prevederile art. 7 pct. 44");

## Cheia

- 1% (cotă unică; cota de 3% a fost abrogată de la 01.01.2026); D100 cod obligație 121, câmp cota = 1
- temei: Legea 227/2015 (Cod fiscal) art. 51 alin. (1), modificat de OUG 89/2025 art. I pct. 4, în vigoare 01.01.2026; art. 51 alin. (1^1) abrogat de OUG 89/2025 art. I pct. 5; structura XML D100 v2 (OPANAF 57/2026), pct. 3 „cota micro”: dacă cod_oblig=121 atunci cota=1
