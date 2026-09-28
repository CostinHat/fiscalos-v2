# Q-PRF-06 — CALCUL

**Întrebarea:** Plătitor de impozit pe profit (cifra de afaceri sub 50 mil. euro) are o pierdere fiscală din 2024 de 100.000 lei, nerecuperată. În 2026 profitul impozabil înainte de recuperarea pierderii este 120.000 lei. Cât impozit pe profit datorează și ce pierdere rămâne de recuperat?

## Stratul semantic (motorul nou) — NU POT RĂSPUNDE

*La data de referință 31.12.2024, presupun un plătitor de impozit pe profit, fără regim de grup fiscal, cu cifra de afaceri sub 50 mil. euro (deci fără impozit minim pe cifra de afaceri), care are o pierdere fiscală înregistrată în 2024, nerecuperată, și un profit impozabil în 2026 de 120.000 lei înainte de recuperarea pierderii.*

Motiv: modelul s-a abţinut: Atomii primiți stabilesc doar regula de recuperare a pierderii (limita de 70% din profitul impozabil, în 5 ani consecutivi), dar determinarea sumei impozitului datorat și a pierderii rămase de recuperat presupune calcule (aplicarea procentului de 70% la 120.000 lei, scăderea din profitul impozabil și aplicarea cotei de impozit), iar rezultatele nu apar literal în niciun atom. În plus, cota de impozit pe profit aplicabilă nu este prezentă în atomii furnizați.

- **Codul fiscal (Legea 227/2015) art. 31 alin. (1)** — `cod_fiscal_227_2015_consolidat#art31/alin1` · valabil din nedovedit
  > Pierderile fiscale anuale stabilite prin declarația de impozit pe profit, începând cu anul 2024/anul fiscal modificat care începe în anul 2024, după caz, se recuperează din profiturile impozabile realizate, în limita a 70% inclusiv, în următorii 5 ani consecutivi.

Apel: `claude-opus-5`, {'intrare': 2777, 'iesire': 693, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0320, 11.7 s

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți stabilesc doar regula de recuperare a pierderii (limita de 70% din profitul impozabil, în 5 ani consecutivi), dar determinarea sumei impozitului datorat și a pierde

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2024-12-31 (an, din "2024"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: R-CALC: intrebarea are 2 baze monetare; calculul cere compunerea mai multor reguli, pe care motorul nu o face


Pe fond: **NU POT** — R-CALC: intrebarea are 2 baze monetare; calculul cere compunerea mai multor reguli, pe care motorul nu o face

## Cheia

- răspuns așteptat: Recuperare max. 70% × 120.000 = 84.000; profit impozabil 36.000; impozit 16% = 5.760 lei; rămân de recuperat 16.000 lei (în limita celor 5 ani consecutivi, până în 2029)
- temei așteptat: Cod fiscal art. 31 alin. (1) (limita 70%, 5 ani, pierderi din 2024 încoace; mod. OUG 115/2023); art. 17 (cota 16%)

