# Q-SAL-03 — CALCUL

**Întrebarea:** Salariat cu normă întreagă la funcția de bază, septembrie 2026, salariu brut 10.000 lei, fără persoane în întreținere, fără copii școlarizați, peste 26 de ani, fără alte deduceri. Calculați CAS, CASS, impozit, net și CAM.

## Stratul semantic — NU POT RĂSPUNDE

*La data de referință 30.09.2026, presupun un salariat român cu contract individual de muncă cu normă întreagă la funcția de bază, venit brut lunar 10.000 lei, fără persoane în întreținere, fără copii școlarizați, peste 26 de ani și fără alte deduceri, impozitat în regimul general al veniturilor din salarii.*

Motiv: modelul s-a abţinut: Atomii primiți conțin doar reguli privind baza de calcul al CAS (art. 139 alin. (1)) și al CASS (art. 157 alin. (1)), contribuția minimă de CAS raportată la salariul minim și derogările privind suma neimpozabilă de 200/300 lei pentru salariații plătiți la nivelul salariului minim. Nu există în context niciun atom care să prevadă literal cotele de contribuție (CAS, CASS), cota de impozit pe venit, deducerea personală sau cota contribuției asiguratorii pentru muncă (CAM). În plus, determinarea sumelor cerute (CAS, CASS, impozit, net, CAM) presupune calcule aritmetice asupra bazei de 10.000 lei, iar rezultatele nu apar literal în niciun atom. Prin urmare nu pot furniza cifr…


Apel: `claude-opus-5`, {'intrare': 10548, 'iesire': 707, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0714

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți conțin doar reguli privind baza de calcul al CAS (art. 139 alin. (1)) și al CASS (art. 157 alin. (1)), contribuția minimă de CAS raportată la salariul minim și dero

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-09-30 (luna, din "septembrie 2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: R-CALC: niciun atom din primii 5 nu da O SINGURA cota


Pe fond: **NU POT** — R-CALC: niciun atom din primii 5 nu da O SINGURA cota

## Cheia

- CAS 2.500 lei; CASS 1.000 lei; deducere personală 0 (brut > 4.325 + 2.000 = 6.325 lei); impozit 10% × (10.000 − 3.500) = 650 lei; net 5.850 lei; CAM 2,25% × 10.000 = 225 lei
- temei: Cod fiscal art. 138 lit. a) (CAS 25%); art. 156 (CASS 10%); art. 77 alin. (3) și (4) (fără deducere peste salariul minim + 2.000 lei); art. 78 alin. (2) lit. a) (cota 10%); art. 220^3 alin. (1) (CAM 2,25%); HG 146/2026 art. 1 (salariul minim 4.325 lei de la 01.07.2026)
