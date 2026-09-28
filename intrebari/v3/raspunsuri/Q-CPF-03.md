# Q-CPF-03 — CALCUL

**Întrebarea:** La inspecție s-a stabilit prin decizie de impunere o diferență de TVA nedeclarată de 20.000 lei, cu scadența inițială 25.07.2025. Decizia e comunicată pe 10.03.2026, iar firma plătește diferența pe 03.04.2026. Ce accesorii datorează?

## Stratul semantic — RĂSPUNS

*La data de referință 25.07.2025, presupun o persoană juridică română plătitoare de TVA, cu obligație fiscală principală administrată de organul fiscal central (buget de stat), diferența de TVA fiind nedeclarată și stabilită prin decizie de impunere în urma inspecției fiscale; presupun, acolo unde întrebarea tace, că executarea deciziei nu a fost suspendată de instanță și că nu suntem în situația obligațiilor datorate bugetelor locale.*

> **Firma datorează penalitate de nedeclarare de 0,08% pe fiecare zi, începând cu ziua imediat următoare scadenței inițiale (25.07.2025) și până la data stingerii sumei, 03.04.2026, inclusiv, precum și obligații fiscale accesorii (dobânzi) calculate pentru aceeași perioadă, de la data scadenței obligației principale până la data plății, inclusiv. Cota dobânzii nu rezultă din atomii primiți, deci nu o pot preciza.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul de procedură fiscală (Legea 207/2015) art. 181 alin. (1)** — `legea_207_2015_consolidat#art181/alin1` · valabil din 2020-12-24
  > contribuabilul/plătitorul datorează o penalitate de nedeclarare de 0,08% pe fiecare zi, începând cu ziua imediat următoare scadenței și până la data stingerii sumei datorate, inclusiv
- **Codul de procedură fiscală (Legea 207/2015) art. 173 alin. (3) lit. b)** — `legea_207_2015_consolidat#art173/alin3/litb` · valabil din 2020-12-24
  > declarații de impunere rectificative sau decizii de impunere, inclusiv cele emise ca urmare a refacerii inspecției fiscale în condițiile art. 129 . În aceste cazuri, se datorează obligații fiscale accesorii de la data scadenței obligației fiscale principale până la data plății, inclusiv.
- derogare tratată: `legea_207_2015_consolidat#art278/alin4` — Derogarea de la art. 173 și art. 181 se aplică doar dacă instanța de contencios administrativ a admis suspendarea executării actului administrativ fiscal; întrebarea nu indică nicio suspendare judecătorească, decizia fiind comunicată și plătită, deci penalitatea de nedeclarare rămâne datorată.
- derogare tratată: `legea_207_2015_consolidat#art183/alin1` — Derogarea privește exclusiv obligațiile fiscale principale datorate bugetelor locale (majorări de întârziere); TVA este administrată de organul fiscal central, deci nu se aplică.
- derogare tratată: `legea_207_2015_consolidat#art133/alin5` — Atomul exclude dobânzi și penalități de nedeclarare doar pentru perioada în care decizia de impunere provizorie nu a fost emisă/comunicată în termen; întrebarea nu menționează o astfel de situație, deci nu am aplicat această excludere.

Apel: `claude-opus-5`, {'intrare': 3580, 'iesire': 3349, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.1026

Pe fond: **GREȘIT** — faptul principal al cheii (['252 zile']) nu e in raspuns

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2025-07-25 (zi, din "25.07.2025"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: C17 (b): atomul pe care as raspunde are 1 derogari/exceptii/modificari valabile la data intrebarii (ex. legea_207_2015_consolidat#art278/alin4: "Prin excepție de la prevederile art. 173 și ale art. 181"); motorul lexical nu le poate trata, deci se abţine.

- **Codul de procedură fiscală (Legea 207/2015) art. 181 alin. (1)** — `legea_207_2015_consolidat#art181/alin1` · valabil din 2020-12-24
  > Pentru obligațiile fiscale principale nedeclarate sau declarate incorect de contribuabil/plătitor și stabilite de organul fiscal prin decizii de impunere, contribuabilul/plătitorul datorează o penalitate de nedeclarare de 0,08% pe fiecare zi, începând cu ziua imediat următoare scadenței și până la data stingerii sumei datorate, inclusiv, din obligațiile fiscale principale nedeclarate sau declarate incorect de contribuabil/plătitor și stabilite de organul fiscal prin decizii de impunere.

Pe fond: **NU POT** — C17 (b): atomul pe care as raspunde are 1 derogari/exceptii/modificari valabile la data intrebarii (ex. legea_207_2015_consolidat#art278/alin4: "Prin excepție de la prevederile art. 173 și ale art. 18

## Cheia

- 252 zile (26.07.2025–03.04.2026 inclusiv). Penalitate de nedeclarare 20.000 × 0,08% × 252 = 4.032 lei, redusă cu 75% (plată până la 05.04.2026, termenul art. 156) → 1.008 lei. Dobânzi 20.000 × 0,02% × 252 = 1.008 lei. Penalitate de întârziere: 0 (nu se aplică când se datorează penalitate de nedeclarare). Total 2.016 lei.
- temei: Legea 207/2015 art. 181 alin. (1), (2) lit. a), (4); art. 156 alin. (1) lit. a); art. 176 alin. (4); art. 174 alin. (2) și (5)
