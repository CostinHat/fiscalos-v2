# Q-CPF-07 — REGULA

**Întrebarea:** Care este durata maximă a unei inspecții fiscale la o microîntreprindere fără sedii secundare (nici contribuabil mijlociu/mare) și ce se întâmplă dacă inspecția depășește acest termen?

## Stratul semantic (motorul nou) — RĂSPUNS

*La data de referință 2026-09-28, presupun un contribuabil persoană juridică microîntreprindere, fără sedii secundare, care nu este încadrat ca mare sau mijlociu contribuabil și nu este nerezident, supus inspecției fiscale de organul fiscal central; presupun, acolo unde întrebarea tace, că nu intervine nicio suspendare a inspecției.*

> **Durata maximă a inspecției fiscale este de 45 de zile (termenul pentru „ceilalți contribuabili”, adică alții decât cei mari, cei cu sedii secundare, nerezidenții și cei mijlocii). Consecința depășirii acestui termen nu rezultă din atomii primiți, deci nu o pot preciza.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul de procedură fiscală (Legea 207/2015) art. 126 alin. (1) lit. c)** — `legea_207_2015_consolidat#art126/alin1/litc` · valabil din nedovedit
  > 45 de zile pentru ceilalți contribuabili.
- **Codul de procedură fiscală (Legea 207/2015) art. 126 alin. (1)** — `legea_207_2015_consolidat#art126/alin1` · valabil din nedovedit
  > Durata efectuării inspecției fiscale este stabilită de organul de inspecție fiscală, în funcție de obiectivele inspecției, și nu poate fi mai mare de:
- **Codul de procedură fiscală (Legea 207/2015) art. 126 alin. (1) lit. a)** — `legea_207_2015_consolidat#art126/alin1/lita` · valabil din nedovedit
  > 180 de zile pentru contribuabilii mari, pentru contribuabilii/plătitorii care au sedii secundare, indiferent de mărime, precum și pentru contribuabilii nerezidenți;
- **Codul de procedură fiscală (Legea 207/2015) art. 126 alin. (1) lit. b)** — `legea_207_2015_consolidat#art126/alin1/litb` · valabil din nedovedit
  > 90 de zile pentru contribuabilii mijlocii;

Apel: `claude-opus-5`, {'intrare': 2749, 'iesire': 1907, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0622, 29.0 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-09-28 (implicita (ziua intrebarii)). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **Contribuabilul/Plătitorul are obligația de a declara organului fiscal central, înființarea de sedii secundare, în termen de 30 de zile de la:**

Motiv: D15: fraza care conţine un fapt de forma cerută (termen) si potriveste cel mai bine intrebarea (scor local 17.7)

- **Codul de procedură fiscală (Legea 207/2015) art. 85 alin. (1)** — `legea_207_2015_consolidat#art85~2/alin1` · valabil din nedovedit
  > Contribuabilul/Plătitorul are obligația de a declara organului fiscal central, înființarea de sedii secundare, în termen de 30 de zile de la:

Pe fond: **GREȘIT** — faptul principal al cheii (['45 zile']) nu e in raspuns; articolul citat [('cpf', '85')] nu e printre cele ale cheii [('cpf', '126')]

## Cheia

- răspuns așteptat: Maximum 45 de zile. Dacă nu se finalizează în dublul perioadei (90 de zile, fără perioadele de suspendare legală), inspecția încetează fără raport și fără decizie de impunere; poate fi reluată o singură dată, cu aprobarea organului ierarhic superior; suspendarea prescripției pe durata inspecției nu mai operează.
- temei așteptat: Legea 207/2015 art. 126 alin. (1) lit. c), (2) și (3)

