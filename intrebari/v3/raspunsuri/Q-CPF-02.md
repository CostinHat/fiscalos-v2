# Q-CPF-02 — CALCUL

**Întrebarea:** O SRL avea TVA de plată 10.000 lei cu scadența 25.03.2026 și a plătit integral pe 24.04.2026. Ce accesorii datorează (dobânzi și penalități de întârziere)?

## Stratul semantic — NU POT RĂSPUNDE

*La data de referință 25.03.2026, pentru o societate comercială (SRL) cu obligație fiscală principală de TVA datorată bugetului de stat, achitată după termenul de scadență, presupunând că nu există dizolvare, eșalonare sau suspendare a executării actului administrativ fiscal.*

Motiv: modelul s-a abţinut: Atomii primiți confirmă doar că se datorează dobânzi și penalități de întârziere, dar nu conțin textele care stabilesc nivelul (cota zilnică) al dobânzii (art. 174) și al penalității de întârziere (art. 176 alin. (1)) și nici regula de calcul al perioadei. Cuantificarea accesoriilor pentru intervalul 26.03.2026-24.04.2026 ar presupune atât o cotă legală care nu apare în niciun atom, cât și un calcul (număr de zile × cotă × 10.000 lei), care nu este permis.

- **Codul de procedură fiscală (Legea 207/2015) art. 173 alin. (1)** — `legea_207_2015_consolidat#art173/alin1` · valabil din nedovedit
  > Pentru neachitarea la termenul de scadență de către debitor a obligațiilor fiscale principale, se datorează după acest termen dobânzi și penalități de întârziere.
- **Codul de procedură fiscală (Legea 207/2015) art. 176 alin. (3)** — `legea_207_2015_consolidat#art176/alin3` · valabil din nedovedit
  > Penalitatea de întârziere nu înlătură obligația de plată a dobânzilor.
- derogare tratată: `legea_207_2015_consolidat#art183/alin1` — Se referă la obligațiile fiscale principale datorate bugetelor locale, pentru care se datorează majorări de întârziere; TVA nu este creanță a bugetului local, deci derogarea nu se aplică.
- derogare tratată: `legea_207_2015_consolidat#art278/alin4` — Se aplică doar când instanța de contencios administrativ a admis cererea de suspendare a executării actului administrativ fiscal; în speță nu există o astfel de suspendare.

Apel: `claude-opus-5`, {'intrare': 2556, 'iesire': 808, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0339

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți confirmă doar că se datorează dobânzi și penalități de întârziere, dar nu conțin textele care stabilesc nivelul (cota zilnică) al dobânzii (art. 174) și al penalită

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-03-25 (zi, din "25.03.2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: R-CALC: niciun atom din primii 5 nu da O SINGURA cota


Pe fond: **NU POT** — R-CALC: niciun atom din primii 5 nu da O SINGURA cota

## Cheia

- 30 zile de întârziere (26.03–24.04 inclusiv): dobânzi 10.000 × 0,02% × 30 = 60 lei; penalități de întârziere 10.000 × 0,01% × 30 = 30 lei; total 90 lei.
- temei: Legea 207/2015 art. 174 alin. (1) și (5); art. 176 alin. (1) și (2)
