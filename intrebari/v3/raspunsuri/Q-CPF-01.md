# Q-CPF-01 — PARAMETRU

**Întrebarea:** Care sunt, în 2026, nivelurile dobânzii și penalității de întârziere pentru obligațiile fiscale principale datorate bugetului de stat (organ fiscal central) neachitate la scadență?

## Stratul semantic — NU POT RĂSPUNDE

*La data de referință 28.09.2026, pentru un contribuabil cu obligații fiscale principale administrate de organul fiscal central (buget de stat), neachitate la scadență, presupunând obligații declarate corect (deci fără penalitate de nedeclarare) și fără suspendare judecătorească a actului administrativ fiscal.*

Motiv: modelul s-a abţinut: Atomii primiți conțin doar regula generală că se datorează dobânzi și penalități de întârziere (art. 173 alin. (1)) și nivelul majorării de întârziere pentru bugetele locale (1% pe lună, art. 183 alin. (2)), respectiv nivelul penalității de nedeclarare (0,08% pe zi, art. 181 alin. (1)). Nivelul propriu-zis al dobânzii de întârziere și al penalității de întârziere pentru creanțele organului fiscal central (textele art. 174 și art. 176 alin. (2), la care atomii doar fac trimitere) nu se află în contextul primit, deci valorile nu pot fi citate literal.


Apel: `claude-opus-5`, {'intrare': 2731, 'iesire': 904, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0372

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți conțin doar regula generală că se datorează dobânzi și penalități de întârziere (art. 173 alin. (1)) și nivelul majorării de întârziere pentru bugetele locale (1% p

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **1%**

Motiv: valoarea de forma cerută (procent) din atomul care poarta o asemenea valoare si potriveste cel mai bine cuvintele rare ale intrebarii (scor local 30.0)

- **Codul de procedură fiscală (Legea 207/2015) art. 183 alin. (2)** — `legea_207_2015_consolidat#art183/alin2` · valabil din nedovedit
  > Nivelul majorării de întârziere este de 1% din cuantumul obligațiilor fiscale principale neachitate în termen, calculată pentru fiecare lună sau fracțiune de lună, începând cu ziua imediat următoare termenului de scadență și până la data stingerii sumei datorate, inclusiv.

Pe fond: **GREȘIT** — faptul principal al cheii (['0,02%']) nu e in raspuns; articolul citat [('cpf', '183')] nu e printre cele ale cheii [('cpf', '174'), (None, '176')]

## Cheia

- Dobândă 0,02% pe fiecare zi de întârziere + penalitate de întârziere 0,01% pe fiecare zi de întârziere (cumulative), calculate din ziua următoare scadenței până la stingere inclusiv.
- temei: Legea 207/2015 art. 174 alin. (1) și (5); art. 176 alin. (1), (2) și (3)
