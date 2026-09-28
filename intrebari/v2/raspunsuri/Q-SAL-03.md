# Q-SAL-03 — CALCUL

**Întrebarea:** Salariat cu normă întreagă la funcția de bază, septembrie 2026, salariu brut 10.000 lei, fără persoane în întreținere, fără copii școlarizați, peste 26 de ani, fără alte deduceri. Calculați CAS, CASS, impozit, net și CAM.

## Stratul semantic (motorul nou) — NU POT RĂSPUNDE

*La data de referință septembrie 2026, presupun un salariat cu contract individual de muncă cu normă întreagă, la funcția de bază, cu salariu brut lunar de 10.000 lei, fără persoane în întreținere, fără copii școlarizați, peste 26 de ani și fără alte deduceri, iar angajatorul este un plătitor obișnuit (fără scutiri sectoriale), acestea din urmă fiind presupuneri acolo unde întrebarea tace.*

Motiv: modelul s-a abţinut: Atomii primiți stabilesc doar bazele lunare de calcul (art. 139 alin. (1) pentru CAS, art. 157 alin. (1) pentru CASS) și regula salariului minim pentru CAS, dar nu conțin cotele aplicabile (cota CAS, cota CASS, cota de impozit pe venit, cota contribuției asiguratorii pentru muncă) și nici regulile de determinare a impozitului și a netului. În plus, răspunsul cerut presupune efectuarea unor calcule (înmulțiri și diferențe) ale căror rezultate nu apar literal în niciun atom, ceea ce nu îmi este permis.

- **Codul fiscal (Legea 227/2015) art. 139 alin. (1)** — `cod_fiscal_227_2015_consolidat#art139/alin1` · valabil din 2018-01-01
  > Baza lunară de calcul al contribuției de asigurări sociale, în cazul persoanelor fizice care realizează venituri din salarii sau asimilate salariilor, o reprezintă câștigul brut realizat din salarii și venituri asimilate salariilor

Apel: `claude-opus-5`, {'intrare': 5520, 'iesire': 940, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0519, 16.4 s

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți stabilesc doar bazele lunare de calcul (art. 139 alin. (1) pentru CAS, art. 157 alin. (1) pentru CASS) și regula salariului minim pentru CAS, dar nu conțin cotele a

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-09-30 (luna, din "septembrie 2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: R-CALC: niciun atom din primii 5 nu da O SINGURA cota


Pe fond: **NU POT** — R-CALC: niciun atom din primii 5 nu da O SINGURA cota

## Cheia

- răspuns așteptat: CAS 2.500 lei; CASS 1.000 lei; deducere personală 0 (brut > 4.325 + 2.000 = 6.325 lei); impozit 10% × (10.000 − 3.500) = 650 lei; net 5.850 lei; CAM 2,25% × 10.000 = 225 lei
- temei așteptat: Cod fiscal art. 138 lit. a) (CAS 25%); art. 156 (CASS 10%); art. 77 alin. (3) și (4) (fără deducere peste salariul minim + 2.000 lei); art. 78 alin. (2) lit. a) (cota 10%); art. 220^3 alin. (1) (CAM 2,25%); HG 146/2026 art. 1 (salariul minim 4.325 lei de la 01.07.2026)

