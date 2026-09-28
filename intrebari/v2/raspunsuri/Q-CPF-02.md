# Q-CPF-02 — CALCUL

**Întrebarea:** O SRL avea TVA de plată 10.000 lei cu scadența 25.03.2026 și a plătit integral pe 24.04.2026. Ce accesorii datorează (dobânzi și penalități de întârziere)?

## Stratul semantic (motorul nou) — NU POT RĂSPUNDE

*La data de referință 25.03.2026, pentru o societate plătitoare de TVA care a achitat cu întârziere o obligație fiscală principală (TVA de plată scadentă la 25.03.2026, achitată la 24.04.2026), presupun regimul general al accesoriilor din Codul de procedură fiscală, fără înlesniri la plată sau proceduri de insolvență/dizolvare.*

Motiv: modelul s-a abţinut: Atomii primiți confirmă doar principiul că se datorează dobânzi și penalități de întârziere pentru neachitarea la scadență, dar nu conțin nivelul (procentul pe zi de întârziere) al dobânzii și al penalității de întârziere prevăzute la art. 174 și 176 și nici modul de determinare a numărului de zile de întârziere. Cuantumul cerut ar presupune un calcul (procent × 10.000 lei × număr de zile) care nu apare literal în niciun atom, deci nu îl pot furniza.

- **Codul de procedură fiscală (Legea 207/2015) art. 173 alin. (1)** — `legea_207_2015_consolidat#art173/alin1` · valabil din nedovedit
  > Pentru neachitarea la termenul de scadență de către debitor a obligațiilor fiscale principale, se datorează după acest termen dobânzi și penalități de întârziere.
- **Codul de procedură fiscală (Legea 207/2015) art. 176 alin. (3)** — `legea_207_2015_consolidat#art176/alin3` · valabil din nedovedit
  > Penalitatea de întârziere nu înlătură obligația de plată a dobânzilor.

Apel: `claude-opus-5`, {'intrare': 1838, 'iesire': 616, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0254, 7.9 s

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți confirmă doar principiul că se datorează dobânzi și penalități de întârziere pentru neachitarea la scadență, dar nu conțin nivelul (procentul pe zi de întârziere) a

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-03-25 (zi, din "25.03.2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: R-CALC: niciun atom din primii 5 nu da O SINGURA cota


Pe fond: **NU POT** — R-CALC: niciun atom din primii 5 nu da O SINGURA cota

## Cheia

- răspuns așteptat: 30 zile de întârziere (26.03–24.04 inclusiv): dobânzi 10.000 × 0,02% × 30 = 60 lei; penalități de întârziere 10.000 × 0,01% × 30 = 30 lei; total 90 lei.
- temei așteptat: Legea 207/2015 art. 174 alin. (1) și (5); art. 176 alin. (1) și (2)

