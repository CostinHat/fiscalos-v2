# Q-CTB-09 — CALCUL

**Întrebarea:** PFA în sistem real, venit net anual 2026 de 60.000 lei, nepensionar, fără salariu sau alte venituri. Cât este CAS minim datorat pentru 2026 și până când se depune D212?

## Stratul semantic (motorul nou) — NU POT RĂSPUNDE

*La data de referință 28.09.2026, pentru o persoană fizică autorizată care determină venitul net anual în sistem real, nepensionară, fără venituri din salarii sau din alte categorii, presupun că se pune problema CAS datorate pentru veniturile anului 2026 și a termenului de depunere a Declarației unice (D212) aferente.*

Motiv: modelul s-a abţinut: Atomii primiți conțin doar regula de încadrare în plafonul de 12 salarii minime brute pe țară (art. 148 alin. (1)), fără baza anuală de calcul efectivă (art. 148 alin. (2)), fără cota CAS și fără nivelul salariului minim brut pe țară pentru 2026; determinarea sumei CAS ar presupune un calcul (bază × cotă) care nu apare literal în niciun atom. De asemenea, niciun atom nu redă termenul de depunere a Declarației unice prevăzut la art. 122 alin. (3), la care se face doar trimitere.

- **Codul fiscal (Legea 227/2015) art. 148 alin. (1)** — `cod_fiscal_227_2015_consolidat#art148/alin1` · valabil din nedovedit
  > a căror valoare anuală cumulată este cel puțin egală cu 12 salarii minime brute pe țară, datorează contribuția de asigurări sociale la o bază de calcul stabilită potrivit alin. (2) .

Apel: `claude-opus-5`, {'intrare': 5208, 'iesire': 1052, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0531, 17.8 s

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți conțin doar regula de încadrare în plafonul de 12 salarii minime brute pe țară (art. 148 alin. (1)), fără baza anuală de calcul efectivă (art. 148 alin. (2)), fără

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: R-CALC: niciun atom din primii 5 nu da O SINGURA cota


Pe fond: **NU POT** — R-CALC: niciun atom din primii 5 nu da O SINGURA cota

## Cheia

- răspuns așteptat: CAS minim 12.150 lei = 25% × 48.600 lei (12 salarii minime × 4.050 lei, salariul minim în vigoare la 01.01.2026; NU 4.325 lei, în vigoare de la 01.07.2026). Venitul se încadrează între 12 și 24 salarii minime (48.600-97.200 lei). D212 până la 25 mai 2027 inclusiv.
- temei așteptat: Legea 227/2015 art. 135^1 alin. (3), art. 138 lit. a), art. 148 alin. (1)-(3), art. 122 alin. (3); HG 1506/2024 art. 1 (4.050 lei de la 01.01.2025); HG 146/2026 art. 1-2 (4.325 lei de la 01.07.2026)

