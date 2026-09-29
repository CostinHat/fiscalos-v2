# Q-CPF-04 — REGULA

**Întrebarea:** Pentru impozitele aferente anului 2021, de când curge și cât durează termenul de prescripție a dreptului ANAF de a stabili creanțe fiscale?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 31.12.2021, pentru obligații fiscale aferente anului 2021 ale unui contribuabil supus Codului de procedură fiscală, presupun regimul general de stabilire a creanțelor fiscale de către organul fiscal central (ANAF), fără fapte prevăzute de legea penală și fără cauze de întrerupere sau suspendare a prescripției.*

Datele din întrebare: 2021-12-31 · data de referință aleasă: **2021-12-31** — Singura dată din întrebare; faptul întrebat privește obligațiile fiscale aferente anului 2021.

> **Termenul de prescripție a dreptului organului fiscal de a stabili creanțe fiscale este de 5 ani și, pentru obligațiile aferente anului 2021, începe să curgă de la data de 1 iulie a anului următor celui pentru care se datorează obligația fiscală, adică de la 1 iulie 2022. Dacă creanțele rezultă din săvârșirea unei fapte prevăzute de legea penală, termenul este de 10 ani. Termenul poate fi întrerupt sau suspendat în cazurile prevăzute de lege.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul, pas cu pas — evaluat de cod, nu de model

- `anul_inceperii_prescriptiei = an_obligatie + 1` = (2021 + 1) = **2022**
  - `an_obligatie` = 2021 — FAPT_CAZ (din întrebare): „Pentru impozitele aferente anului 2021”

- **Codul de procedură fiscală (Legea 207/2015) art. 110 alin. (2)** — `legea_207_2015_consolidat#art110/alin2` · valabil din nedovedit
  > Termenul de prescripție a dreptului prevăzut la alin. (1) începe să curgă de la data de 1 iulie a anului următor celui pentru care se datorează obligația fiscală, dacă legea nu dispune altfel.
- **Codul de procedură fiscală (Legea 207/2015) art. 110 alin. (1)** — `legea_207_2015_consolidat#art110/alin1` · valabil din nedovedit
  > Dreptul organului fiscal de a stabili creanțe fiscale se prescrie în termen de 5 ani, cu excepția cazului în care legea dispune altfel.
- **Codul de procedură fiscală (Legea 207/2015) art. 110 alin. (3)** — `legea_207_2015_consolidat#art110/alin3` · valabil din nedovedit
  > Dreptul de a stabili creanțe fiscale se prescrie în termen de 10 ani în cazul în care acestea rezultă din săvârșirea unei fapte prevăzute de legea penală.
- **Codul de procedură fiscală (Legea 207/2015) art. 111 alin. (1)** — `legea_207_2015_consolidat#art111/alin1` · valabil din nedovedit
  > Termenele de prescripție prevăzute la art. 110 se întrerup:
- derogare tratată: `legea_207_2015_consolidat#art110/alin3` — Termenul special de 10 ani se aplică numai creanțelor care rezultă din săvârșirea unei fapte prevăzute de legea penală; întrebarea nu indică o astfel de situație, deci se aplică termenul general de 5 ani, iar excepția a fost citată explicit.
- derogare tratată: `legea_207_2015_consolidat#art111/alin1` — Cauzele de întrerupere (și de suspendare, alin. 2) ale termenului nu sunt invocate în speță; au fost menționate ca rezervă.

### Navigarea (4 pași, 3 ture)

1. `cauta` {"interogare": "termenul de prescripție a dreptului de a stabili creanțe fiscale 5 ani 1 iulie"}
2. `cuprins` {"act": "legea_207_2015_consolidat", "filtru": "prescripţie"}
3. `deschide` {"id": "legea_207_2015_consolidat#art110/alin2"}
4. `deschide` {"id": "legea_207_2015_consolidat#art110/alin1"}

Apel: `claude-opus-5`, {'intrare': 6, 'iesire': 2421, 'cache_scriere': 2773, 'cache_citire': 23498} tokeni, $0.0896, 32 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond CORECT

> Termenul de prescripție a dreptului organului fiscal de a stabili creanțe fiscale este de 5 ani și curge de la data de 1 iulie a anului următor celui pentru care se datorează obligația fiscală, deci de la 1 iulie 2.022 pentru impozitele aferente anului 2021. [calcul: an_incepere = an_fiscal + 1 = 2.022]

## Cheia

- Curge de la 1 iulie 2022, durează 5 ani (se împlinește în iulie 2027), dacă nu intervin întreruperi/suspendări (ex. depunere declarație după termen sau rectificativă întrerup; inspecția fiscală suspendă). Dacă creanța rezultă dintr-o faptă penală: 10 ani de la săvârșirea faptei.
- temei: Legea 207/2015 art. 110 alin. (1)–(4); art. 111 alin. (1) lit. b)–c) și alin. (2) lit. b)
