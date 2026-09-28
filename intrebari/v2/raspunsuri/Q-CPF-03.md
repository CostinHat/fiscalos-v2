# Q-CPF-03 — CALCUL

**Întrebarea:** La inspecție s-a stabilit prin decizie de impunere o diferență de TVA nedeclarată de 20.000 lei, cu scadența inițială 25.07.2025. Decizia e comunicată pe 10.03.2026, iar firma plătește diferența pe 03.04.2026. Ce accesorii datorează?

## Stratul semantic (motorul nou) — RĂSPUNS

*La data de referință 25.07.2025, presupun o persoană juridică înregistrată în scopuri de TVA în România, cu obligație principală de TVA nedeclarată (20.000 lei, scadentă 25.07.2025) stabilită prin decizie de impunere în urma unei inspecții fiscale, decizie comunicată la 10.03.2026 și achitată la 03.04.2026, fără suspendarea executării deciziei și fără vreo reducere/anulare specială a accesoriilor.*

> **Firma datorează accesorii calculate de la scadența obligației principale (25.07.2025) până la data plății, inclusiv (03.04.2026), și anume: penalitate de nedeclarare de 0,08% pe fiecare zi, începând cu ziua imediat următoare scadenței și până la data stingerii sumei datorate, inclusiv, aplicată la cei 20.000 lei stabiliți prin decizia de impunere, la care se adaugă dobânzi pentru aceeași perioadă. Cuantumul exact în lei și cota dobânzii nu rezultă din textele avute la dispoziție.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul de procedură fiscală (Legea 207/2015) art. 181 alin. (1)** — `legea_207_2015_consolidat#art181/alin1` · valabil din nedovedit
  > contribuabilul/plătitorul datorează o penalitate de nedeclarare de 0,08% pe fiecare zi, începând cu ziua imediat următoare scadenței și până la data stingerii sumei datorate, inclusiv
- **Codul de procedură fiscală (Legea 207/2015) art. 173 alin. (3) lit. b)** — `legea_207_2015_consolidat#art173/alin3/litb` · valabil din nedovedit
  > declarații de impunere rectificative sau decizii de impunere, inclusiv cele emise ca urmare a refacerii inspecției fiscale în condițiile art. 129. În aceste cazuri, se datorează obligații fiscale accesorii de la data scadenței obligației fiscale principale până la data plății, inclusiv.

Apel: `claude-opus-5`, {'intrare': 4435, 'iesire': 1798, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0679, 26.3 s

Pe fond: **GREȘIT** — faptul principal al cheii (['252 zile']) nu e in raspuns

## Motorul lexical — RĂSPUNS

*Data de referinta: 2025-07-25 (zi, din "25.07.2025"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **20.000 lei x 0,08% = 16,00 lei**

Motiv: R-CALC: o baza, o cota; baza x cota

- **Codul de procedură fiscală (Legea 207/2015) art. 181 alin. (1)** — `legea_207_2015_consolidat#art181/alin1` · valabil din nedovedit
  > Pentru obligațiile fiscale principale nedeclarate sau declarate incorect de contribuabil/plătitor și stabilite de organul fiscal prin decizii de impunere, contribuabilul/plătitorul datorează o penalitate de nedeclarare de 0,08% pe fiecare zi, începând cu ziua imediat următoare scadenței și până la data stingerii sumei datorate, inclusiv, din obligațiile fiscale principale nedeclarate sau declarate incorect de contribuabil/plătitor și stabilite de organul fiscal prin decizii de impunere.

Pe fond: **GREȘIT** — faptul principal al cheii (['252 zile']) nu e in raspuns

## Cheia

- răspuns așteptat: 252 zile (26.07.2025–03.04.2026 inclusiv). Penalitate de nedeclarare 20.000 × 0,08% × 252 = 4.032 lei, redusă cu 75% (plată până la 05.04.2026, termenul art. 156) → 1.008 lei. Dobânzi 20.000 × 0,02% × 252 = 1.008 lei. Penalitate de întârziere: 0 (nu se aplică când se datorează penalitate de nedeclarare). Total 2.016 lei.
- temei așteptat: Legea 207/2015 art. 181 alin. (1), (2) lit. a), (4); art. 156 alin. (1) lit. a); art. 176 alin. (4); art. 174 alin. (2) și (5)

