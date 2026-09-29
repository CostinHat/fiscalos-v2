# Q-PRF-02 — REGULA

**Întrebarea:** O microîntreprindere depășește în luna mai 2026 plafonul de venituri cumulate de la începutul anului. Care e plafonul, la ce curs se verifică și de când datorează impozit pe profit?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 31.05.2026, presupun o persoană juridică română plătitoare de impozit pe veniturile microîntreprinderilor, cu an fiscal = anul calendaristic, aflată în activitate (nu în inactivitate temporară înscrisă în registrul comerțului), care depășește în luna mai 2026 limita de venituri calculate cumulat de la începutul anului.*

Datele din întrebare: 2026-05-31 · data de referință aleasă: **2026-05-31** — Faptul întrebat este depășirea plafonului în luna mai 2026 și consecințele ei; singura dată din întrebare este luna mai 2026.

> **Plafonul este echivalentul în lei a 100.000 euro. Se verifică pe baza veniturilor (cifra de afaceri potrivit reglementărilor contabile aplicabile) înregistrate cumulat de la începutul anului fiscal, echivalentul în euro determinându-se la cursul de schimb valabil la închiderea exercițiului financiar precedent (închiderea exercițiului 2025). Odată depășit plafonul, societatea datorează impozit pe profit începând cu trimestrul în care s-a depășit limita, adică trimestrul în care se situează luna mai 2026, calculul și plata impozitului pe profit făcându-se luând în considerare veniturile și cheltuielile realizate începând cu acel trimestru.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 52 alin. (1)** — `cod_fiscal_227_2015_consolidat#art52/alin1` · valabil din 2026-02-25
  > Dacă în cursul unui an fiscal o microîntreprindere realizează venituri mai mari de 100.000 euro, aceasta datorează impozit pe profit începând cu trimestrul în care s-a depășit această limită.
- **Codul fiscal (Legea 227/2015) art. 52 alin. (5)** — `cod_fiscal_227_2015_consolidat#art52/alin5` · valabil din 2026-01-01
  > Limitele fiscale prevăzute la alin. (1) se verifică pe baza veniturilor înregistrate cumulat de la începutul anului fiscal. Cursul de schimb pentru determinarea echivalentului în euro este cel valabil la închiderea exercițiului financiar precedent.
- **Codul fiscal (Legea 227/2015) art. 54 alin. (1)** — `cod_fiscal_227_2015_consolidat#art54/alin1` · valabil din 2026-02-25
  > Pentru încadrarea în condițiile privind nivelul veniturilor prevăzute la art. 47 alin. (1) lit. c) și la art. 52 alin. (1) se iau în calcul veniturile care constituie cifra de afaceri definită potrivit reglementărilor contabile aplicabile.
- **Codul fiscal (Legea 227/2015) art. 54 alin. (3)** — `cod_fiscal_227_2015_consolidat#art54/alin3` · valabil din 2025-01-01
  > Pentru anul fiscal 2025/2026, limita veniturilor realizate, reprezentând echivalentul în lei a 250.000 euro, respectiv echivalentul în lei a 100.000 euro începând cu 1 ianuarie 2026, se verifică pe baza veniturilor realizate de către persoana juridică română la data de 31 decembrie 2024, respectiv la data de 31 decembrie 2025.
- **Codul fiscal (Legea 227/2015) art. 52 alin. (6)** — `cod_fiscal_227_2015_consolidat#art52/alin6` · valabil din nedovedit
  > Calculul și plata impozitului pe profit de către microîntreprinderile care se încadrează în prevederile alin. (1) , (2) , (4) și (7) se efectuează luând în considerare veniturile și cheltuielile realizate începând cu trimestrul respectiv.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art48/alin2^3` — Excepția de la art. 52 privește microîntreprinderea aflată în inactivitate temporară înscrisă în registrul comerțului, care rămâne plătitoare de impozit pe veniturile microîntreprinderilor pe toată perioada inactivității; cazul din întrebare este al unei societăți active care realizează venituri pes…

### Navigarea (14 pași, 8 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "microintreprinderi"}
2. `cauta` {"interogare": "microîntreprindere depășește plafonul 250.000 euro impozit pe profit trimestru"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art52/alin1"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art47"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art47/alin1"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art47/alin1^1"}
7. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art47/alin1/litc"}
8. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art54"}
9. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art54/alin3"}
10. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art54/alin1"}
11. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art52"}
12. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art48/alin2^3"}
13. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art52/alin5"}
14. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art52/alin6"}

Apel: `claude-opus-5`, {'intrare': 16, 'iesire': 4772, 'cache_scriere': 11487, 'cache_citire': 95513} tokeni, $0.2389, 64 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond GREȘIT

> -

## Cheia

- Plafon 100.000 euro; curs valabil la închiderea exercițiului financiar precedent (31.12.2025); impozit pe profit începând cu trimestrul în care s-a depășit limita, adică trimestrul II 2026 (calculat pe veniturile și cheltuielile de la începutul trimestrului II)
- temei: Cod fiscal art. 52 alin. (1) (mod. OUG 8/2026 art. 6 pct. 20, aplicabil de la trim. I 2026 cf. art. 10 alin. (5) OUG 8/2026); art. 52 alin. (5) (mod. OUG 89/2025 art. I pct. 6); art. 52 alin. (6); art. 54 alin. (1)
