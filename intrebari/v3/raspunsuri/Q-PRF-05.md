# Q-PRF-05 — CALCUL

**Întrebarea:** Microîntreprindere, trimestrul I 2026: venituri din vânzări 200.000 lei, dividende primite de la o SRL română 30.000 lei, venituri din diferențe de curs valutar 5.000 lei, reduceri comerciale primite ulterior facturării (cont 609) 2.000 lei. Cât impozit datorează pentru T1?

## Stratul semantic — NU POT RĂSPUNDE

*La data de referință 28.09.2026, presupun o societate plătitoare de impozit pe veniturile microîntreprinderilor, aflată în activitate (nu în inactivitate temporară), care calculează impozitul trimestrial pentru trimestrul I 2026, fără opțiune de trecere la impozit pe profit.*

Motiv: modelul s-a abţinut: Atomii primiți conțin doar reguli privind baza impozabilă (scăderea reducerilor comerciale din contul 609 și tratamentul diferențelor de curs valutar doar în trimestrul IV), nu și textul care stabilește baza impozabilă generală (art. 53 alin. (1), inclusiv excluderea dividendelor primite de la o persoană juridică română, care apare doar ca text de modificare din Legea 296/2020, fără atom din Codul fiscal în vigoare) și nici cota de impozitare aplicabilă microîntreprinderilor. În plus, determinarea sumei datorate ar impune un calcul (scăderi din venituri și aplicarea unei cote), iar rezultatul nu apare literal în niciun atom.

- **Codul fiscal (Legea 227/2015) art. 53 alin. (2) lit. a)** — `cod_fiscal_227_2015_consolidat#art53/alin2/lita` · valabil din nedovedit
  > valoarea reducerilor comerciale primite ulterior facturării, înregistrate în contul "609", potrivit reglementărilor contabile aplicabile;
- **Codul fiscal (Legea 227/2015) art. 53 alin. (2) lit. b)** — `cod_fiscal_227_2015_consolidat#art53/alin2/litb` · valabil din 2023-01-01
  > în trimestrul IV sau în ultimul trimestru al perioadei impozabile, în cazul contribuabililor care își încetează existența, diferența favorabilă dintre veniturile din diferențe de curs valutar/veniturile financiare aferente creanțelor și datoriilor cu decontare în funcție de cursul unei valute, rezultate din evaluarea sau decontarea acestora,
- derogare tratată: `cod_fiscal_227_2015_consolidat#art48/alin2^3` — Derogarea privind microîntreprinderea aflată în inactivitate temporară înscrisă în registrul comerțului nu se aplică: întrebarea descrie o societate activă, cu venituri din vânzări în trimestrul I 2026; de altfel nu am întemeiat răspunsul pe art. 52.

Apel: `claude-opus-5`, {'intrare': 3360, 'iesire': 1641, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0588

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți conțin doar reguli privind baza impozabilă (scăderea reducerilor comerciale din contul 609 și tratamentul diferențelor de curs valutar doar în trimestrul IV), nu și

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: R-CALC: intrebarea are 4 baze monetare; calculul cere compunerea mai multor reguli, pe care motorul nu o face


Pe fond: **NU POT** — R-CALC: intrebarea are 4 baze monetare; calculul cere compunerea mai multor reguli, pe care motorul nu o face

## Cheia

- 2.020 lei (bază 202.000 = 235.000 − 30.000 dividende − 5.000 dif. curs + 2.000 cont 609; × 1%)
- temei: Cod fiscal art. 53 alin. (1) partea introductivă, lit. h) și lit. n); art. 53 alin. (2) lit. a); art. 51 alin. (1) (mod. OUG 89/2025); art. 56 alin. (1)
