# Q-CPF-09 — CAPCANA

**Întrebarea:** O firmă a plătit cu 60 de zile întârziere o amendă contravențională de 2.000 lei aplicată de ANAF. Cât datorează ca dobânzi și penalități de întârziere pentru această întârziere?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 28.09.2026, presupun o persoană juridică debitoare a unei amenzi contravenționale aplicate de organul fiscal central (ANAF), achitată cu întârziere, fără contestație cu suspendare judecătorească a executării actului și fără ca amenda să fie o creanță administrată de organul fiscal local.*

Datele din întrebare: niciuna (ziua întrebării) · data de referință aleasă: **2026-09-28** — Întrebarea nu poartă nicio dată proprie; se folosește ziua întrebării, la care se verifică forma în vigoare a regulii privind accesoriile.

> **Nu datorează nimic: pentru sumele datorate cu titlu de amenzi de orice fel nu se datorează dobânzi și penalități de întârziere, indiferent de durata întârzierii de plată.**

Citatul decisiv (`legea_207_2015_consolidat#art173/alin2`):
> Nu se datorează dobânzi și penalități de întârziere pentru sumele datorate cu titlu de amenzi de orice fel, obligații fiscale accesorii stabilite potrivit legii, cheltuieli de executare silită, cheltuieli judiciare, sumele confiscate

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul de procedură fiscală (Legea 207/2015) art. 173 alin. (2)** — `legea_207_2015_consolidat#art173/alin2` · valabil din nedovedit
  > Nu se datorează dobânzi și penalități de întârziere pentru sumele datorate cu titlu de amenzi de orice fel, obligații fiscale accesorii stabilite potrivit legii, cheltuieli de executare silită, cheltuieli judiciare, sumele confiscate
- **Codul de procedură fiscală (Legea 207/2015) art. 173 alin. (1)** — `legea_207_2015_consolidat#art173/alin1` · valabil din nedovedit
  > Pentru neachitarea la termenul de scadență de către debitor a obligațiilor fiscale principale, se datorează după acest termen dobânzi și penalități de întârziere.
- derogare tratată: `legea_207_2015_consolidat#art183/alin1` — Excepția privește obligațiile fiscale principale datorate bugetelor locale, pentru care se datorează majorări de întârziere; în cazul din întrebare amenda este aplicată de ANAF (organ fiscal central), deci excepția nu se aplică.
- derogare tratată: `legea_207_2015_consolidat#art278/alin4` — Excepția vizează situația în care instanța de contencios administrativ admite cererea de suspendare a executării actului administrativ fiscal; întrebarea nu descrie o contestație cu suspendare judecătorească, iar efectul ei ar fi tot neplata de penalități, deci nu schimbă soluția.

### Navigarea (5 pași, 4 ture)

1. `cauta` {"interogare": "nu se datorează dobânzi și penalități de întârziere pentru amenzi de orice fel"}
2. `cuprins` {"act": "legea_207_2015_consolidat", "filtru": "dobânzi și penalități de întârziere"}
3. `deschide` {"id": "legea_207_2015_consolidat#art173/alin2"}
4. `deschide` {"id": "legea_207_2015_consolidat#art278/alin4"}
5. `deschide` {"id": "legea_207_2015_consolidat#art183/alin1"}

Apel: `claude-opus-5`, {'intrare': 8, 'iesire': 1802, 'cache_scriere': 4540, 'cache_citire': 34873} tokeni, $0.0909, 27 s

Pe fond (comparator): **GREȘIT** — faptul principal al cheii (['0 lei']) nu e in raspuns

Lectura pe fond (de verificat de om): **comparator, nu fond** — Răspunsul spune „Nu datorează nimic”, cu temeiul exact al cheii (CPF art. 173 alin. (2)). Comparatorul caută faptul „0 lei” și nu recunoaște „nimic” ca zero (vezi C30).

## v4 — RĂSPUNS, pe fond CORECT

> Nu datorează nimic: pentru sumele cu titlu de amenzi de orice fel nu se datorează dobânzi și penalități de întârziere, indiferent de durata întârzierii (0 lei accesorii pentru amenda de 2.000 lei). Întârzierea poate atrage doar executarea silită a amenzii, nu accesorii.

## Cheia

- 0 lei: nu se datorează dobânzi și penalități de întârziere pentru amenzi de orice fel (nici pentru accesorii, cheltuieli de executare etc.).
- temei: Legea 207/2015 art. 173 alin. (2)
