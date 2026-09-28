# Q-PRF-05 — CALCUL

**Întrebarea:** Microîntreprindere, trimestrul I 2026: venituri din vânzări 200.000 lei, dividende primite de la o SRL română 30.000 lei, venituri din diferențe de curs valutar 5.000 lei, reduceri comerciale primite ulterior facturării (cont 609) 2.000 lei. Cât impozit datorează pentru T1?

## Stratul semantic (motorul nou) — NU POT RĂSPUNDE

*La data de referință 28.09.2026, presupun o societate plătitoare de impozit pe veniturile microîntreprinderilor (persoană juridică română, fără activități care obligă la impozit pe profit) care calculează impozitul pentru trimestrul I 2026, fără a se fi depășit plafonul de venituri.*

Motiv: modelul s-a abţinut: Atomii primiți conțin doar reguli privind elementele care se adaugă la baza impozabilă (reducerile comerciale din contul 609, diferențele de curs valutar doar în trimestrul IV), dar nu conțin nici textul art. 53 alin. (1) cu veniturile care intră în baza impozabilă și excluderea dividendelor primite de la o persoană juridică română ca element în vigoare la data de referință, nici cota de impozitare aplicabilă microîntreprinderilor. În plus, determinarea sumei impozitului ar necesita un calcul (însumarea bazei și aplicarea unei cote), iar rezultatul nu apare literal în nici…

- **Codul fiscal (Legea 227/2015) art. 53 alin. (2)** — `cod_fiscal_227_2015_consolidat#art53/alin2` · valabil din nedovedit
  > Pentru determinarea impozitului pe veniturile microîntreprinderilor, la baza impozabilă determinată potrivit alin. (1) se adaugă următoarele: a) valoarea reducerilor comerciale primite ulterior facturării, înregistrate în contul "609", potrivit reglementărilor contabile aplicabile;
- **Codul fiscal (Legea 227/2015) art. 53 alin. (2) lit. b)** — `cod_fiscal_227_2015_consolidat#art53/alin2/litb` · valabil din 2023-01-01
  > în trimestrul IV sau în ultimul trimestru al perioadei impozabile, în cazul contribuabililor care își încetează existența, diferența favorabilă dintre veniturile din diferențe de curs valutar/veniturile financiare aferente creanțelor și datoriilor cu decontare în funcție de cursul unei valute

Apel: `claude-opus-5`, {'intrare': 3703, 'iesire': 1076, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0462, 19.0 s

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți conțin doar reguli privind elementele care se adaugă la baza impozabilă (reducerile comerciale din contul 609, diferențele de curs valutar doar în trimestrul IV), d

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: R-CALC: intrebarea are 4 baze monetare; calculul cere compunerea mai multor reguli, pe care motorul nu o face


Pe fond: **NU POT** — R-CALC: intrebarea are 4 baze monetare; calculul cere compunerea mai multor reguli, pe care motorul nu o face

## Cheia

- răspuns așteptat: 2.020 lei (bază 202.000 = 235.000 − 30.000 dividende − 5.000 dif. curs + 2.000 cont 609; × 1%)
- temei așteptat: Cod fiscal art. 53 alin. (1) partea introductivă, lit. h) și lit. n); art. 53 alin. (2) lit. a); art. 51 alin. (1) (mod. OUG 89/2025); art. 56 alin. (1)

