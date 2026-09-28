# Q-PRF-02 — REGULA

**Întrebarea:** O microîntreprindere depășește în luna mai 2026 plafonul de venituri cumulate de la începutul anului. Care e plafonul, la ce curs se verifică și de când datorează impozit pe profit?

## Stratul semantic — RĂSPUNS

*La data de referință 31.05.2026, presupun o persoană juridică română plătitoare de impozit pe veniturile microîntreprinderilor, în activitate (nu în inactivitate temporară înscrisă în registrul comerțului) și care nu se află în situația prevăzută la art. 47 alin. (1^1) privind persoanele legate, care depășește plafonul de venituri în luna mai 2026.*

> **Plafonul este de 100.000 euro venituri realizate într-un an fiscal. Verificarea se face pe baza veniturilor înregistrate cumulat de la începutul anului fiscal, iar echivalentul în euro se determină la cursul de schimb valabil la închiderea exercițiului financiar precedent. Microîntreprinderea datorează impozit pe profit începând cu trimestrul în care s-a depășit această limită, adică trimestrul în care se situează luna mai 2026.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 52 alin. (1)** — `cod_fiscal_227_2015_consolidat#art52/alin1` · valabil din 2026-02-25
  > Dacă în cursul unui an fiscal o microîntreprindere realizează venituri mai mari de 100.000 euro, aceasta datorează impozit pe profit începând cu trimestrul în care s-a depășit această limită.
- **Codul fiscal (Legea 227/2015) art. 52 alin. (5)** — `cod_fiscal_227_2015_consolidat#art52/alin5` · valabil din 2026-01-01
  > Limitele fiscale prevăzute la alin. (1) se verifică pe baza veniturilor înregistrate cumulat de la începutul anului fiscal. Cursul de schimb pentru determinarea echivalentului în euro este cel valabil la închiderea exercițiului financiar precedent.
- **Codul fiscal (Legea 227/2015) art. 48 alin. (2^3)** — `cod_fiscal_227_2015_consolidat#art48/alin2^3` · valabil din 2024-01-01
  > Prin excepție de la prevederile art. 52 , respectiv de la art. 47 alin. (1) și alin. (4) , microîntreprinderea care se află în inactivitate temporară înscrisă în registrul comerțului, potrivit prevederilor legale, continuă să fie plătitoare de impozit pe veniturile microîntreprinderilor pentru întreaga perioadă în care înregistrează această situație de inactivitate.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art48/alin2^3` — Excepția privind microîntreprinderea aflată în inactivitate temporară înscrisă în registrul comerțului nu se aplică: întrebarea descrie o microîntreprindere activă, care realizează venituri cumulate în cursul anului 2026; am citat totuși textul derogării.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art52/alin5^1` — Regula suplimentară de cumulare a veniturilor cu cele ale persoanelor legate se aplică doar microîntreprinderii aflate în situația prevăzută la art. 47 alin. (1^1); întrebarea nu indică existența unor persoane legate, deci se aplică doar regulile de la alin. (5).

Apel: `claude-opus-5`, {'intrare': 6923, 'iesire': 1851, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0819

Pe fond: **CORECT** — faptul principal si articolul coincid

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-05-31 (luna, din "mai 2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: C17 (b): atomul pe care as raspunde are 1 derogari/exceptii/modificari valabile la data intrebarii (ex. cod_fiscal_227_2015_consolidat#art48/alin2^3: "Prin excepție de la prevederile art. 52"); motorul lexical nu le poate trata, deci se abţine.

- **Codul fiscal (Legea 227/2015) art. 52 alin. (1)** — `cod_fiscal_227_2015_consolidat#art52/alin1` · valabil din 2026-02-25
  > Dacă în cursul unui an fiscal o microîntreprindere realizează venituri mai mari de 100.000 euro, aceasta datorează impozit pe profit începând cu trimestrul în care s-a depășit această limită. Notă ... Potrivit alin. (5) al art. 10 din ORDONANȚA DE URGENȚĂ nr. 8 din 24 februarie 2026, publicată în MONITORUL OFICIAL nr. 147 din 25 februarie 2026, prevederile art. 6 pct. 20 se aplică pentru calculul plafonului microîntreprinderilor începând cu trimestrul I 2026.

Pe fond: **NU POT** — C17 (b): atomul pe care as raspunde are 1 derogari/exceptii/modificari valabile la data intrebarii (ex. cod_fiscal_227_2015_consolidat#art48/alin2^3: "Prin excepție de la prevederile art. 52"); motoru

## Cheia

- Plafon 100.000 euro; curs valabil la închiderea exercițiului financiar precedent (31.12.2025); impozit pe profit începând cu trimestrul în care s-a depășit limita, adică trimestrul II 2026 (calculat pe veniturile și cheltuielile de la începutul trimestrului II)
- temei: Cod fiscal art. 52 alin. (1) (mod. OUG 8/2026 art. 6 pct. 20, aplicabil de la trim. I 2026 cf. art. 10 alin. (5) OUG 8/2026); art. 52 alin. (5) (mod. OUG 89/2025 art. I pct. 6); art. 52 alin. (6); art. 54 alin. (1)
