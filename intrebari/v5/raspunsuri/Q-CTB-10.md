# Q-CTB-10 — REGULA

**Întrebarea:** Un SRL are de plătit unui furnizor SRL o factură de 8.000 lei. Cât poate plăti în numerar?

## Stratul de navigare v5 — NU POT RĂSPUNDE

*La data de 28.09.2026, presupun un SRL (persoană juridică dintre cele prevăzute la art. 1 alin. (1) din Legea 70/2015) care plătește în aceeași zi o factură de 8.000 lei unui furnizor tot persoană juridică (nu magazin de tip cash and carry), fără alte plăți în numerar către acel furnizor în ziua respectivă.*

Datele din întrebare: niciuna (ziua întrebării) · data de referință aleasă: **2026-09-28** — Întrebarea nu poartă nicio dată; se aplică legislația în vigoare la ziua întrebării.

Motiv: VERIFICAREA MECANICA a respins propunerea modelului: C17: atomul legea_70_2015_consolidat#art3/alin1 deroga de la / modifica un atom citat si raspunsul nu il trateaza

### Calculul, pas cu pas — evaluat de cod, nu de model

- `rest_fara_numerar = valoare_factura - plafon_numerar` = (8.000 − 5.000) = **3.000**
  - `valoare_factura` = 8.000 — FAPT_CAZ (din întrebare): „o factură de 8.000 lei”
  - `plafon_numerar` = 5.000 — VALOARE_LEGALA din `legea_70_2015_consolidat#art3/alin3`: „pot achita facturile cu valori care depășesc plafonul de 5.000 lei, către furnizorii de bunuri și servicii”

- **Legea 70/2015 art. 3 alin. (3)** — `legea_70_2015_consolidat#art3/alin3` · valabil din 2023-11-11
  > Persoanele prevăzute la art. 1 alin. (1) pot achita facturile cu valori care depășesc plafonul de 5.000 lei, către furnizorii de bunuri și servicii, respectiv de 10.000 lei, către magazinele de tipul cash and carry, astfel: 5.000 lei/10.000 lei în numerar, suma care depășește acest plafon putând fi achitată numai prin instrumente de plată fără numerar.
- **Legea 70/2015 art. 3 alin. (1) lit. c)** — `legea_70_2015_consolidat#art3/alin1/litc` · valabil din nedovedit
  > plăți către persoanele prevăzute la art. 1 alin. (1) , în limita unui plafon zilnic de 5.000 lei/persoană, dar nu mai mult de un plafon total de 10.000 lei/zi;
- **Legea 70/2015 art. 1 alin. (1)** — `legea_70_2015_consolidat#art1/alin1` · valabil din 2026-01-01
  > Operațiunile de încasări și plăți efectuate de persoane juridice, persoane fizice autorizate, întreprinderi individuale, întreprinderi familiale, liber-profesioniști, persoane fizice care desfășoară activități în mod independent
- derogare tratată: `legea_70_2015_consolidat#art1/alin1` — Art. 3 alin. (1) instituie excepția de la regula generală de la art. 1 alin. (1); excepția se aplică în cazul de față și este citată (lit. c), plafonul zilnic de 5.000 lei/persoană pentru plăți către alte persoane juridice.

### Navigarea (7 pași, 5 ture)

1. `cauta` {"interogare": "plăți în numerar plafon zilnic persoane juridice 1.000 lei"}
2. `cuprins` {"act": "legea_70_2015_consolidat", "filtru": "numerar"}
3. `deschide` {"id": "legea_70_2015_consolidat#art3/alin1/litc"}
4. `deschide` {"id": "legea_296_2023_masuri_fiscal_bugetare_asigurarea_sustenabilitatii#artLXIV"}
5. `deschide` {"id": "legea_70_2015_consolidat#art3/alin3"}
6. `deschide` {"id": "legea_70_2015_consolidat#art3"}
7. `deschide` {"id": "legea_70_2015_consolidat#art1/alin1"}

Apel: `claude-opus-5`, {'intrare': 10, 'iesire': 2891, 'cache_scriere': 4799, 'cache_citire': 44515} tokeni, $0.1246, 50 s

Pe fond (comparator): **NU POT** — VERIFICAREA MECANICA a respins propunerea modelului: C17: atomul legea_70_2015_consolidat#art3/alin1 deroga de la / modifica un atom citat si raspunsul nu il trateaza

## v4 — RĂSPUNS, pe fond CORECT

> Poate plăti în numerar cel mult 5.000 lei (plafonul zilnic pe persoană), iar restul de 3.000 lei numai prin instrumente de plată fără numerar; plățile fragmentate în numerar pentru facturi mai mari de 5.000 lei sunt interzise. [calcul: rest = factura - plafon = 3.000]

## Cheia

- Maxim 5.000 lei în numerar; restul de 3.000 lei numai prin instrumente de plată fără numerar. Plățile în numerar către persoane de la art. 1 alin. (1) sunt limitate la 5.000 lei/zi/persoană și 10.000 lei/zi în total; fragmentarea e interzisă.
- temei: Legea 70/2015 art. 3 alin. (1) lit. c) și alin. (3)
