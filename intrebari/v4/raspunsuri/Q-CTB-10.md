# Q-CTB-10 — REGULA

**Întrebarea:** Un SRL are de plătit unui furnizor SRL o factură de 8.000 lei. Cât poate plăti în numerar?

## Stratul de navigare (v4) — RĂSPUNS

*La data de 28.09.2026, presupun o plată efectuată de un SRL (persoană juridică dintre cele prevăzute la art. 1 alin. (1) din Legea 70/2015) către un alt SRL furnizor de bunuri/servicii, care nu este magazin de tip cash and carry, pentru o factură unică de 8.000 lei achitată în aceeași zi.*

> **Poate plăti în numerar cel mult 5.000 lei (plafonul zilnic pe persoană), iar restul de 3.000 lei numai prin instrumente de plată fără numerar; plățile fragmentate în numerar pentru facturi mai mari de 5.000 lei sunt interzise. [calcul: rest = factura - plafon = 3.000]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul — evaluat de cod, nu de model

- `rest = factura - plafon` → **3.000**
  - `factura` = 8.000 — din întrebare: „o factură de 8.000 lei”
  - `plafon` = 5.000 — din `legea_70_2015_consolidat#art3/alin1/litc`: „în limita unui plafon zilnic de 5.000 lei/persoană”

- **Legea 70/2015 art. 3 alin. (3)** — `legea_70_2015_consolidat#art3/alin3` · valabil din 2023-11-11
  > Persoanele prevăzute la art. 1 alin. (1) pot achita facturile cu valori care depășesc plafonul de 5.000 lei, către furnizorii de bunuri și servicii, respectiv de 10.000 lei, către magazinele de tipul cash and carry, astfel: 5.000 lei/10.000 lei în numerar, suma care depășește acest plafon putând fi achitată numai prin instrumente de plată fără numerar.
- **Legea 70/2015 art. 3 alin. (1) lit. c)** — `legea_70_2015_consolidat#art3/alin1/litc` · valabil din nedovedit
  > plăți către persoanele prevăzute la art. 1 alin. (1) , în limita unui plafon zilnic de 5.000 lei/persoană, dar nu mai mult de un plafon total de 10.000 lei/zi;
- **Legea 70/2015 art. 3 alin. (1)** — `legea_70_2015_consolidat#art3/alin1` · valabil din nedovedit
  > Prin excepție de la prevederile art. 1 alin. (1) se pot efectua operațiuni de încasări și plăți în numerar, în următoarele condiții:
- derogare tratată: `legea_70_2015_consolidat#art1/alin1` — Art. 3 alin. (1) este excepție de la regula generală de efectuare a operațiunilor prin instrumente fără numerar de la art. 1 alin. (1); excepția se aplică cazului și a fost citată.

### Navigarea (5 pași, 4 ture)

1. `cauta` {"interogare": "plafon plăți în numerar persoane juridice 5.000 lei zi"}
2. `cuprins` {"act": "legea_70_2015_consolidat", "filtru": "numerar"}
3. `deschide` {"id": "legea_70_2015_consolidat#art3/alin1"}
4. `deschide` {"id": "legea_70_2015_consolidat#art3/alin1/litc"}
5. `deschide` {"id": "legea_70_2015_consolidat#art3/alin3"}

Apel: `claude-opus-5`, {'intrare': 8, 'iesire': 1787, 'cache_scriere': 3363, 'cache_citire': 29927} tokeni, $0.0807, 28 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți nu conțin regula privind plafonul plăților în numerar între persoane juridice (dispozițiile din Legea 70/2015 care stabilesc limitele zilnice pe persoană și pe zi). Singurul atom din Legea 70/2015 furnizat se referă la dreptul beneficiarilor de plăți salariale, pensii și indemnizații de a primi sumele în numerar, ceea ce nu privește cazul din întrebare. Fără textul care stabilește plafonul, nu pot indica suma care poate fi plătită în numerar și nici nu pot efe…

## Cheia

- Maxim 5.000 lei în numerar; restul de 3.000 lei numai prin instrumente de plată fără numerar. Plățile în numerar către persoane de la art. 1 alin. (1) sunt limitate la 5.000 lei/zi/persoană și 10.000 lei/zi în total; fragmentarea e interzisă.
- temei: Legea 70/2015 art. 3 alin. (1) lit. c) și alin. (3)
