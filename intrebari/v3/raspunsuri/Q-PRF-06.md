# Q-PRF-06 — CALCUL

**Întrebarea:** Plătitor de impozit pe profit (cifra de afaceri sub 50 mil. euro) are o pierdere fiscală din 2024 de 100.000 lei, nerecuperată. În 2026 profitul impozabil înainte de recuperarea pierderii este 120.000 lei. Cât impozit pe profit datorează și ce pierdere rămâne de recuperat?

## Stratul semantic — NU POT RĂSPUNDE

*La data de referință 31.12.2024, presupun un contribuabil plătitor de impozit pe profit, cu cifră de afaceri sub 50 mil. euro (deci fără impozit minim pe cifra de afaceri), care are o pierdere fiscală înregistrată în anul 2024 și un profit impozabil în 2026 înainte de recuperarea pierderii.*

Motiv: modelul s-a abţinut: Atomii primiți nu conțin regula aplicabilă pierderilor fiscale înregistrate începând cu anul 2024 (art. 31 alin. (1) din Codul fiscal nu se află în context); singurul text despre recuperarea pierderilor, art. 31 alin. (7), se referă expres la pierderile aferente anilor precedenți anului 2024, rămase de recuperat la 31 decembrie 2023, deci nu acoperă o pierdere din 2024. De asemenea, lipsește din atomi cota de impozit pe profit, iar determinarea sumei de impozit datorat și a pierderii rămase de recuperat ar presupune efectuarea unor calcule (aplicarea unei limite procentuale asupra profitului de 120.000 lei, scăderea pierderii recuperate și aplicarea cotei), rezultate car…


Apel: `claude-opus-5`, {'intrare': 4421, 'iesire': 857, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0445

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți nu conțin regula aplicabilă pierderilor fiscale înregistrate începând cu anul 2024 (art. 31 alin. (1) din Codul fiscal nu se află în context); singurul text despre

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2024-12-31 (an, din "2024"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: R-CALC: intrebarea are 2 baze monetare; calculul cere compunerea mai multor reguli, pe care motorul nu o face


Pe fond: **NU POT** — R-CALC: intrebarea are 2 baze monetare; calculul cere compunerea mai multor reguli, pe care motorul nu o face

## Cheia

- Recuperare max. 70% × 120.000 = 84.000; profit impozabil 36.000; impozit 16% = 5.760 lei; rămân de recuperat 16.000 lei (în limita celor 5 ani consecutivi, până în 2029)
- temei: Cod fiscal art. 31 alin. (1) (limita 70%, 5 ani, pierderi din 2024 încoace; mod. OUG 115/2023); art. 17 (cota 16%)
