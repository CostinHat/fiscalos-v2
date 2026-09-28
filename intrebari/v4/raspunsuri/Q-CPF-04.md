# Q-CPF-04 — REGULA

**Întrebarea:** Pentru impozitele aferente anului 2021, de când curge și cât durează termenul de prescripție a dreptului ANAF de a stabili creanțe fiscale?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 31.12.2021, pentru obligații fiscale aferente anului fiscal 2021 ale unui contribuabil supus regulilor generale din Codul de procedură fiscală, presupunând că nu este vorba de creanțe rezultate din săvârșirea unei fapte prevăzute de legea penală și că nu au intervenit cauze de întrerupere sau suspendare.*

> **Termenul de prescripție a dreptului organului fiscal de a stabili creanțe fiscale este de 5 ani și curge de la data de 1 iulie a anului următor celui pentru care se datorează obligația fiscală, deci de la 1 iulie 2.022 pentru impozitele aferente anului 2021. [calcul: an_incepere = an_fiscal + 1 = 2.022]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul — evaluat de cod, nu de model

- `an_incepere = an_fiscal + 1` → **2.022**
  - `an_fiscal` = 2021 — din întrebare: „Pentru impozitele aferente anului 2021”

- **Codul de procedură fiscală (Legea 207/2015) art. 110 alin. (2)** — `legea_207_2015_consolidat#art110/alin2` · valabil din nedovedit
  > Termenul de prescripție a dreptului prevăzut la alin. (1) începe să curgă de la data de 1 iulie a anului următor celui pentru care se datorează obligația fiscală, dacă legea nu dispune altfel.
- **Codul de procedură fiscală (Legea 207/2015) art. 110 alin. (1)** — `legea_207_2015_consolidat#art110/alin1` · valabil din nedovedit
  > Dreptul organului fiscal de a stabili creanțe fiscale se prescrie în termen de 5 ani, cu excepția cazului în care legea dispune altfel.
- derogare tratată: `legea_207_2015_consolidat#art110/alin3` — Termenul special de 10 ani, care curge de la data săvârșirii faptei, se aplică numai creanțelor fiscale rezultate din săvârșirea unei fapte prevăzute de legea penală; întrebarea nu descrie o astfel de situație, deci se aplică regula generală de 5 ani.

### Navigarea (5 pași, 5 ture)

1. `cauta` {"interogare": "termenul de prescripție a dreptului de a stabili creanțe fiscale 5 ani"}
2. `cuprins` {"act": "legea_207_2015_consolidat", "filtru": "prescripţie"}
3. `deschide` {"id": "legea_207_2015_consolidat#art110"}
4. `deschide` {"id": "legea_207_2015_consolidat#art110/alin2"}
5. `deschide` {"id": "legea_207_2015_consolidat#art110/alin1"}

Apel: `claude-opus-5`, {'intrare': 10, 'iesire': 1942, 'cache_scriere': 3182, 'cache_citire': 39300} tokeni, $0.0881, 32 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> VERIFICAREA MECANICA a respins propunerea modelului: cifra '2022' din raspuns nu apare literal in citate sau in intrebare

## Cheia

- Curge de la 1 iulie 2022, durează 5 ani (se împlinește în iulie 2027), dacă nu intervin întreruperi/suspendări (ex. depunere declarație după termen sau rectificativă întrerup; inspecția fiscală suspendă). Dacă creanța rezultă dintr-o faptă penală: 10 ani de la săvârșirea faptei.
- temei: Legea 207/2015 art. 110 alin. (1)–(4); art. 111 alin. (1) lit. b)–c) și alin. (2) lit. b)
