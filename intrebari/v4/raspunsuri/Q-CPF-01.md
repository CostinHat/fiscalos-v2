# Q-CPF-01 — PARAMETRU

**Întrebarea:** Care sunt, în 2026, nivelurile dobânzii și penalității de întârziere pentru obligațiile fiscale principale datorate bugetului de stat (organ fiscal central) neachitate la scadență?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 28.09.2026, pentru obligații fiscale principale administrate de organul fiscal central (venit al bugetului de stat), neachitate la scadență, presupunând un debitor obișnuit fără înlesniri la plată (fără eșalonare) și fără să fie incident vreunul dintre cazurile speciale de la art. 174 alin. (4).</declaratie>
<parameter name="raspuns">Dobânda este de 0,02% pentru fiecare zi de întârziere, iar penalitatea de întârziere este de 0,01% pentru fiecare zi de întârziere (ambele calculate din ziua imediat următoare scadenței până la stingerea sumei, inclusiv).*

> **Dobânda este de 0,02% pentru fiecare zi de întârziere, iar penalitatea de întârziere este de 0,01% pentru fiecare zi de întârziere.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul de procedură fiscală (Legea 207/2015) art. 174 alin. (5)** — `legea_207_2015_consolidat#art174/alin5` · valabil din nedovedit
  > Nivelul dobânzii este de 0,02% pentru fiecare zi de întârziere.
- **Codul de procedură fiscală (Legea 207/2015) art. 176 alin. (2)** — `legea_207_2015_consolidat#art176/alin2` · valabil din nedovedit
  > Nivelul penalității de întârziere este de 0,01% pentru fiecare zi de întârziere.
- **Codul de procedură fiscală (Legea 207/2015) art. 173 alin. (1)** — `legea_207_2015_consolidat#art173/alin1` · valabil din nedovedit
  > Pentru neachitarea la termenul de scadență de către debitor a obligațiilor fiscale principale, se datorează după acest termen dobânzi și penalități de întârziere.
- **Codul de procedură fiscală (Legea 207/2015) art. 174 alin. (1)** — `legea_207_2015_consolidat#art174/alin1` · valabil din nedovedit
  > Dobânzile se calculează pentru fiecare zi de întârziere, începând cu ziua imediat următoare termenului de scadență și până la data stingerii sumei datorate, inclusiv.
- derogare tratată: `legea_207_2015_consolidat#art174/alin4` — Excepție de la art. 174 alin. (1) privind modul de calcul al dobânzilor în situații speciale; nu schimbă nivelul dobânzii (0,02%/zi) și nu privește cazul simplu al neplății la scadență descris în întrebare.
- derogare tratată: `legea_207_2015_consolidat#art197/alin1` — Derogă de la art. 174 alin. (5) numai pe perioada pentru care s-au acordat eșalonări la plată; întrebarea vizează obligații neachitate la scadență, fără eșalonare, deci nu se aplică.

### Navigarea (5 pași, 4 ture)

1. `cuprins` {"act": "legea_207_2015_consolidat", "filtru": "dobânzi penalitate întârziere"}
2. `cauta` {"interogare": "nivelul dobânzii 0,02% pentru fiecare zi de întârziere"}
3. `deschide` {"id": "legea_207_2015_consolidat#art174"}
4. `deschide` {"id": "legea_207_2015_consolidat#art176/alin2"}
5. `deschide` {"id": "legea_207_2015_consolidat#art174/alin5"}

Apel: `claude-opus-5`, {'intrare': 8, 'iesire': 1994, 'cache_scriere': 4819, 'cache_citire': 32102} tokeni, $0.0961, 33 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți conțin doar regula generală că se datorează dobânzi și penalități de întârziere (art. 173 alin. (1)) și nivelul majorării de întârziere pentru bugetele locale (1% pe lună, art. 183 alin. (2)), respectiv nivelul penalității de nedeclarare (0,08% pe zi, art. 181 alin. (1)). Nivelul propriu-zis al dobânzii de întârziere și al penalității de întârziere pentru creanțele organului fiscal central (textele art. 174 și art. 176 alin. (2), la care atomii doar fac trimit…

## Cheia

- Dobândă 0,02% pe fiecare zi de întârziere + penalitate de întârziere 0,01% pe fiecare zi de întârziere (cumulative), calculate din ziua următoare scadenței până la stingere inclusiv.
- temei: Legea 207/2015 art. 174 alin. (1) și (5); art. 176 alin. (1), (2) și (3)
