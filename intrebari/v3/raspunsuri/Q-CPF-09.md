# Q-CPF-09 — CAPCANA

**Întrebarea:** O firmă a plătit cu 60 de zile întârziere o amendă contravențională de 2.000 lei aplicată de ANAF. Cât datorează ca dobânzi și penalități de întârziere pentru această întârziere?

## Stratul semantic — RĂSPUNS

*La data de referință 28.09.2026, presupun o persoană juridică (firmă) care are de achitat o amendă contravențională aplicată de ANAF, deci o creanță bugetară administrată de organul fiscal central (nu de organul fiscal local), achitată cu întârziere, fără suspendarea executării actului de către instanța de contencios administrativ.*

> **Nu datorează nimic cu titlu de dobânzi și penalități de întârziere: pentru sumele datorate cu titlu de amenzi de orice fel nu se calculează astfel de accesorii, indiferent de durata întârzierii. Se achită doar amenda în sine.**

Citatul decisiv (`legea_207_2015_consolidat#art173/alin2`):
> Nu se datorează dobânzi și penalități de întârziere pentru sumele datorate cu titlu de amenzi de orice fel, obligații fiscale accesorii stabilite potrivit legii, cheltuieli de executare silită, cheltuieli judiciare, sumele confiscate

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul de procedură fiscală (Legea 207/2015) art. 173 alin. (2)** — `legea_207_2015_consolidat#art173/alin2` · valabil din nedovedit
  > Nu se datorează dobânzi și penalități de întârziere pentru sumele datorate cu titlu de amenzi de orice fel, obligații fiscale accesorii stabilite potrivit legii, cheltuieli de executare silită, cheltuieli judiciare, sumele confiscate
- **Codul de procedură fiscală (Legea 207/2015) art. 173 alin. (1)** — `legea_207_2015_consolidat#art173/alin1` · valabil din nedovedit
  > Pentru neachitarea la termenul de scadență de către debitor a obligațiilor fiscale principale, se datorează după acest termen dobânzi și penalități de întârziere.
- derogare tratată: `legea_207_2015_consolidat#art183/alin1` — Derogarea privește obligațiile fiscale principale datorate bugetelor locale, pentru care se datorează majorări de întârziere. Amenda a fost aplicată de ANAF (organ fiscal central), deci nu este o creanță a bugetului local și excepția nu se aplică.
- derogare tratată: `legea_207_2015_consolidat#art278/alin4` — Derogarea se aplică doar dacă instanța de contencios administrativ a admis cererea de suspendare a executării actului administrativ fiscal; întrebarea nu descrie nicio suspendare, iar efectul ei ar fi tot neplata de penalități, deci nu schimbă concluzia.

Apel: `claude-opus-5`, {'intrare': 2830, 'iesire': 930, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0384

Pe fond: **GREȘIT** — faptul principal al cheii (['0 lei']) nu e in raspuns

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-09-28 (implicita (ziua intrebarii)). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: D15: intrebarea cere un fapt de forma 'procent', si niciun atom gasit (nici copiii lor) nu conţine unul


Pe fond: **NU POT** — D15: intrebarea cere un fapt de forma 'procent', si niciun atom gasit (nici copiii lor) nu conţine unul

## Cheia

- 0 lei: nu se datorează dobânzi și penalități de întârziere pentru amenzi de orice fel (nici pentru accesorii, cheltuieli de executare etc.).
- temei: Legea 207/2015 art. 173 alin. (2)
