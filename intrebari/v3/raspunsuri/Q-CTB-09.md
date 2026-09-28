# Q-CTB-09 — CALCUL

**Întrebarea:** PFA în sistem real, venit net anual 2026 de 60.000 lei, nepensionar, fără salariu sau alte venituri. Cât este CAS minim datorat pentru 2026 și până când se depune D212?

## Stratul semantic — NU POT RĂSPUNDE

*La data de referință 28.09.2026, pentru o persoană fizică autorizată impusă în sistem real, nepensionară, fără venituri din salarii sau alte categorii, cu venit net anual 2026 de 60.000 lei, presupun că se pune problema CAS datorate la plafonul minim și a termenului de depunere a Declarației unice (D212) pentru veniturile anului 2026.*

Motiv: modelul s-a abţinut: Atomii primiți stabilesc doar condiția de plafon (cel puțin 12 salarii minime brute pe țară) pentru datorarea CAS, dar nu conțin nici cota contribuției, nici valoarea salariului minim brut pe țară pentru 2026, iar suma CAS ar rezulta dintr-un calcul (bază × cotă) care nu apare literal în niciun atom. De asemenea, termenul de depunere a Declarației unice prevăzut la art. 122 alin. (3) nu este prezent în context; atomul art. 122 alin. (5) menționează data de 25 mai doar pentru situația specială a persoanelor cu handicap grav sau accentuat, care nu corespunde cazului.

- **Codul fiscal (Legea 227/2015) art. 148 alin. (1)** — `cod_fiscal_227_2015_consolidat#art148/alin1` · valabil din nedovedit
  > au realizat venituri din activitățile prevăzute la art. 137 alin. (1) lit. b) și b^1) , din una sau mai multe surse și/sau categorii de venituri, a căror valoare anuală cumulată este cel puțin egală cu 12 salarii minime brute pe țară, datorează contribuția de asigurări sociale la o bază de calcul stabilită potrivit alin. (2) .
- derogare tratată: `cod_fiscal_227_2015_consolidat#art151/alin3` — Derogarea de la art. 148 alin. (1) privește contribuabilii care în cursul anului se încadrează în categoria persoanelor exceptate de la plata CAS potrivit art. 150; din enunț nu rezultă o astfel de situație (PFA nepensionar, fără salariu), deci nu se aplică cazului. Oricum, nu schimbă lipsa datelor …

Apel: `claude-opus-5`, {'intrare': 10688, 'iesire': 1606, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0945

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți stabilesc doar condiția de plafon (cel puțin 12 salarii minime brute pe țară) pentru datorarea CAS, dar nu conțin nici cota contribuției, nici valoarea salariului m

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: R-CALC: niciun atom din primii 5 nu da O SINGURA cota


Pe fond: **NU POT** — R-CALC: niciun atom din primii 5 nu da O SINGURA cota

## Cheia

- CAS minim 12.150 lei = 25% × 48.600 lei (12 salarii minime × 4.050 lei, salariul minim în vigoare la 01.01.2026; NU 4.325 lei, în vigoare de la 01.07.2026). Venitul se încadrează între 12 și 24 salarii minime (48.600-97.200 lei). D212 până la 25 mai 2027 inclusiv.
- temei: Legea 227/2015 art. 135^1 alin. (3), art. 138 lit. a), art. 148 alin. (1)-(3), art. 122 alin. (3); HG 1506/2024 art. 1 (4.050 lei de la 01.01.2025); HG 146/2026 art. 1-2 (4.325 lei de la 01.07.2026)
