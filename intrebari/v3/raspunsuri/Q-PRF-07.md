# Q-PRF-07 — CALCUL

**Întrebarea:** Profit contabil 2026 = 100.000 lei, cheltuiala cu impozitul pe profit = 20.000 lei, cheltuieli de protocol = 10.000 lei. Ce sumă din protocol e deductibilă și cât se adaugă ca nedeductibil?

## Stratul semantic — NU POT RĂSPUNDE

*La data de referință 28.09.2026, presupun un contribuabil plătitor de impozit pe profit care aplică regulile titlului II privind deductibilitatea limitată a cheltuielilor de protocol, fără alte facilități sau regimuri speciale precizate în întrebare.*

Motiv: modelul s-a abţinut: Atomul primit stabilește doar regula (limita de 2% aplicată asupra profitului contabil la care se adaugă cheltuielile cu impozitul pe profit și cheltuielile de protocol), dar sumele cerute (partea deductibilă și partea nedeductibilă din cei 10.000 lei) rezultă exclusiv din calcul aritmetic asupra datelor cazului și nu apar literal în niciun atom; conform regulilor, nu efectuez calcule.

- **Codul fiscal (Legea 227/2015) art. 25 alin. (3) lit. a)** — `cod_fiscal_227_2015_consolidat#art25/alin3/lita` · valabil din nedovedit
  > cheltuielile de protocol în limita unei cote de 2% aplicată asupra profitului contabil la care se adaugă cheltuielile cu impozitul pe profit și cheltuielile de protocol.

Apel: `claude-opus-5`, {'intrare': 3376, 'iesire': 515, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0307

Pe fond: **NU POT** — modelul s-a abţinut: Atomul primit stabilește doar regula (limita de 2% aplicată asupra profitului contabil la care se adaugă cheltuielile cu impozitul pe profit și cheltuielile de protocol), dar sume

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: R-CALC: intrebarea are 3 baze monetare; calculul cere compunerea mai multor reguli, pe care motorul nu o face


Pe fond: **NU POT** — R-CALC: intrebarea are 3 baze monetare; calculul cere compunerea mai multor reguli, pe care motorul nu o face

## Cheia

- Deductibil 2.600 lei (2% × (100.000 + 20.000 + 10.000) = 2% × 130.000); nedeductibil 7.400 lei
- temei: Cod fiscal art. 25 alin. (3) lit. a)
