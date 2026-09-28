# Q-PRF-02 — REGULA

**Întrebarea:** O microîntreprindere depășește în luna mai 2026 plafonul de venituri cumulate de la începutul anului. Care e plafonul, la ce curs se verifică și de când datorează impozit pe profit?

## Stratul semantic (motorul nou) — RĂSPUNS

*La data de referință 31.05.2026, presupun o societate plătitoare de impozit pe veniturile microîntreprinderilor, fără persoane legate relevante (art. 47 alin. (1^1)) și cu situații financiare depuse la termen, care depășește în luna mai 2026 plafonul de venituri cumulate de la începutul anului fiscal.*

> **Plafonul este de 100.000 euro venituri realizate în cursul anului fiscal. Verificarea se face pe baza veniturilor înregistrate cumulat de la începutul anului fiscal, iar echivalentul în euro se determină la cursul de schimb valabil la închiderea exercițiului financiar precedent. Microîntreprinderea datorează impozit pe profit începând cu trimestrul în care s-a depășit această limită (trimestrul în care se încadrează luna mai 2026).**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 52 alin. (1)** — `cod_fiscal_227_2015_consolidat#art52/alin1` · valabil din 2026-02-25
  > Dacă în cursul unui an fiscal o microîntreprindere realizează venituri mai mari de 100.000 euro, aceasta datorează impozit pe profit începând cu trimestrul în care s-a depășit această limită.
- **Codul fiscal (Legea 227/2015) art. 52 alin. (5)** — `cod_fiscal_227_2015_consolidat#art52/alin5` · valabil din 2026-01-01
  > Limitele fiscale prevăzute la alin. (1) se verifică pe baza veniturilor înregistrate cumulat de la începutul anului fiscal. Cursul de schimb pentru determinarea echivalentului în euro este cel valabil la închiderea exercițiului financiar precedent.
- **Codul fiscal (Legea 227/2015) art. 54 alin. (1)** — `cod_fiscal_227_2015_consolidat#art54/alin1` · valabil din 2026-02-25
  > Pentru încadrarea în condițiile privind nivelul veniturilor prevăzute la art. 47 alin. (1) lit. c) și la art. 52 alin. (1) se iau în calcul veniturile care constituie cifra de afaceri definită potrivit reglementărilor contabile aplicabile.

Apel: `claude-opus-5`, {'intrare': 3550, 'iesire': 1157, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0474, 16.3 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-05-31 (luna, din "mai 2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **Dacă în cursul unui an fiscal o microîntreprindere realizează venituri mai mari de 100.000 euro, aceasta datorează impozit pe profit începând cu trimestrul în care s-a depășit această limită.**

Motiv: D15: fraza care conţine un fapt de forma cerută (suma) si potriveste cel mai bine intrebarea (scor local 22.1)

- **Codul fiscal (Legea 227/2015) art. 52 alin. (1)** — `cod_fiscal_227_2015_consolidat#art52/alin1` · valabil din 2026-02-25
  > Dacă în cursul unui an fiscal o microîntreprindere realizează venituri mai mari de 100.000 euro, aceasta datorează impozit pe profit începând cu trimestrul în care s-a depășit această limită. Notă ... Potrivit alin. (5) al art. 10 din ORDONANȚA DE URGENȚĂ nr. 8 din 24 februarie 2026, publicată în MONITORUL OFICIAL nr. 147 din 25 februarie 2026, prevederile art. 6 pct. 20 se aplică pentru calculul plafonului microîntreprinderilor începând cu trimestrul I 2026.

Pe fond: **CORECT** — faptul principal si articolul coincid

## Cheia

- răspuns așteptat: Plafon 100.000 euro; curs valabil la închiderea exercițiului financiar precedent (31.12.2025); impozit pe profit începând cu trimestrul în care s-a depășit limita, adică trimestrul II 2026 (calculat pe veniturile și cheltuielile de la începutul trimestrului II)
- temei așteptat: Cod fiscal art. 52 alin. (1) (mod. OUG 8/2026 art. 6 pct. 20, aplicabil de la trim. I 2026 cf. art. 10 alin. (5) OUG 8/2026); art. 52 alin. (5) (mod. OUG 89/2025 art. I pct. 6); art. 52 alin. (6); art. 54 alin. (1)

