# Q-SAL-01 — PARAMETRU

**Întrebarea:** Care este cota contribuției asiguratorii pentru muncă (CAM) datorată de angajator în 2026 și cine o suportă?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 28.09.2026, pentru un angajator persoană juridică cu sediul în România care acordă venituri din salarii și asimilate salariilor unor salariați obișnuiți (fără regimuri speciale sau angajatori străini fără sediu în România).*

> **Cota este de 2,25%, aplicată asupra bazei de calcul, și este suportată integral de angajator (persoanele fizice și juridice care au calitatea de angajatori sau sunt asimilate acestora), care are obligația să o calculeze și să o plătească la bugetul de stat; nu se reține din salariul angajatului.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 220^3 alin. (1)** — `cod_fiscal_227_2015_consolidat#art220^3/alin1` · valabil din nedovedit
  > Cota contribuției asiguratorii pentru muncă este de 2,25%.
- **Codul fiscal (Legea 227/2015) art. 220^1** — `cod_fiscal_227_2015_consolidat#art220^1` · valabil din 2018-01-01
  > Contribuabilii obligați la plata contribuției asiguratorii pentru muncă sunt, după caz: a) persoanele fizice și juridice care au calitatea de angajatori sau sunt asimilate acestora, pentru cetățenii români, cetățeni ai altor state sau apatrizii, pe perioada în care au, conform legii, domiciliul sau reședința în România
- **Codul fiscal (Legea 227/2015) art. 220^6 alin. (1)** — `cod_fiscal_227_2015_consolidat#art220^6/alin1` · valabil din nedovedit
  > Persoanele fizice și juridice prevăzute la art. 220^1 lit. a) au obligația de a calcula contribuția asiguratorie pentru muncă și de a o plăti la bugetul de stat, într-un cont distinct, până la data de 25 inclusiv a lunii următoare celei pentru care se plătesc veniturile
- **Codul fiscal (Legea 227/2015) art. 220^6 alin. (3)** — `cod_fiscal_227_2015_consolidat#art220^6/alin3` · valabil din nedovedit
  > Calculul contribuției asiguratorie pentru muncă se realizează prin aplicarea cotei prevăzute la art. 220^3 asupra bazei de calcul prevăzute la art. 220^4 , cu respectarea prevederilor art. 220^5 .
- derogare tratată: `cod_fiscal_227_2015_consolidat#art220^6/alin2` — Excepția vizează persoanele fizice care obțin venituri din salarii de la angajatori care nu au sediu social, sediu permanent sau reprezentanță în România (caz în care plata revine persoanei fizice); nu se aplică situației din întrebare, care privește un angajator obișnuit din România.

### Navigarea (6 pași, 4 ture)

1. `cauta` {"interogare": "contribuția asiguratorie pentru muncă cota 2,25%"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "asiguratorie pentru muncă"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art220^3"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art220^1"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art220^3/alin1"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art220^6/alin1"}

Apel: `claude-opus-5`, {'intrare': 8, 'iesire': 1931, 'cache_scriere': 4234, 'cache_citire': 30576} tokeni, $0.0901, 30 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Stratul semantic v3 (context dat de căutare) — RĂSPUNS, pe fond CORECT

> Cota contribuției asiguratorii pentru muncă este de 2,25%, aplicată asupra bazei lunare de calcul. Din atomii disponibili rezultă că ea se datorează pentru veniturile din salarii și asimilate salariilor acordate de contribuabilii-plătitori (angajatori), nu de salariat; textul care desemnează expres persoana care o suportă (enumerarea contribuabililor) nu se regăsește însă integral în atomii primiți.

## Cheia

- 2,25%, datorată de angajator, asupra bazei de la art. 220^4 (câștigurile brute din salarii)
- temei: Legea 227/2015 (Cod fiscal) art. 220^3 alin. (1); baza: art. 220^4 alin. (1)
