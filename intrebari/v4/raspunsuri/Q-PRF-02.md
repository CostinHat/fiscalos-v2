# Q-PRF-02 — REGULA

**Întrebarea:** O microîntreprindere depășește în luna mai 2026 plafonul de venituri cumulate de la începutul anului. Care e plafonul, la ce curs se verifică și de când datorează impozit pe profit?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 31.05.2026, presupun o persoană juridică română plătitoare de impozit pe veniturile microîntreprinderilor, în activitate (nu în inactivitate temporară înscrisă la registrul comerțului), care în luna mai 2026 depășește prin veniturile cumulate de la începutul anului fiscal plafonul de ieșire din regim.</declaratie>
<parameter name="raspuns">Plafonul este de 100.000 euro (echivalent în lei), verificat pe baza veniturilor înregistrate cumulat de la începutul anului fiscal, luându-se în calcul veniturile care constituie cifra de afaceri (plus veniturile din transferul mijloacelor fixe/terenurilor în situația prevăzută de lege). Echivalentul în euro se determină la cursul de schimb valabil la închiderea exercițiului financiar precedent (cel de la 31.12.2025). Microîntreprinderea datorează impozit pe profit începând cu trimestrul în care s-a depășit această limită, adică începând cu trimestrul în care se situează luna mai 2026, iar calculul se face luând în considerare veniturile și cheltuielile realizate începând cu trimestrul respectiv.*

> **-**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 52 alin. (1)** — `cod_fiscal_227_2015_consolidat#art52/alin1` · valabil din 2026-02-25
  > Dacă în cursul unui an fiscal o microîntreprindere realizează venituri mai mari de 100.000 euro, aceasta datorează impozit pe profit începând cu trimestrul în care s-a depășit această limită.
- **Codul fiscal (Legea 227/2015) art. 52 alin. (5)** — `cod_fiscal_227_2015_consolidat#art52/alin5` · valabil din 2026-01-01
  > Limitele fiscale prevăzute la alin. (1) se verifică pe baza veniturilor înregistrate cumulat de la începutul anului fiscal. Cursul de schimb pentru determinarea echivalentului în euro este cel valabil la închiderea exercițiului financiar precedent.
- **Codul fiscal (Legea 227/2015) art. 54 alin. (1)** — `cod_fiscal_227_2015_consolidat#art54/alin1` · valabil din 2026-02-25
  > Pentru încadrarea în condițiile privind nivelul veniturilor prevăzute la art. 47 alin. (1) lit. c) și la art. 52 alin. (1) se iau în calcul veniturile care constituie cifra de afaceri definită potrivit reglementărilor contabile aplicabile.
- **Codul fiscal (Legea 227/2015) art. 52 alin. (6)** — `cod_fiscal_227_2015_consolidat#art52/alin6` · valabil din nedovedit
  > Calculul și plata impozitului pe profit de către microîntreprinderile care se încadrează în prevederile alin. (1) , (2) , (4) și (7) se efectuează luând în considerare veniturile și cheltuielile realizate începând cu tri
- derogare tratată: `cod_fiscal_227_2015_consolidat#art48/alin2^3` — Excepția privind microîntreprinderea aflată în inactivitate temporară înscrisă în registrul comerțului (care rămâne plătitoare de impozit pe veniturile microîntreprinderilor pe toată perioada inactivității) nu se aplică, întrebarea descriind o microîntreprindere care realizează venituri, deci în act…

### Navigarea (11 pași, 7 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "microîntreprinderi"}
2. `cauta` {"interogare": "depășire plafon 100.000 euro microîntreprindere impozit pe profit trimestru"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art52/alin1"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art54"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art54/alin1"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art54/alin3"}
7. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art54/alin2"}
8. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "curs de schimb"}
9. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art52"}
10. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art52/alin5"}
11. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art48/alin2^3"}

Apel: `claude-opus-5`, {'intrare': 14, 'iesire': 3193, 'cache_scriere': 8153, 'cache_citire': 68667} tokeni, $0.1652, 51 s

Pe fond: **GREȘIT** — faptul principal al cheii (['100.000 euro']) nu e in raspuns

## Stratul semantic v3 (context dat de căutare) — RĂSPUNS, pe fond CORECT

> Plafonul este de 100.000 euro venituri realizate într-un an fiscal. Verificarea se face pe baza veniturilor înregistrate cumulat de la începutul anului fiscal, iar echivalentul în euro se determină la cursul de schimb valabil la închiderea exercițiului financiar precedent. Microîntreprinderea datorează impozit pe profit începând cu trimestrul în care s-a depășit această limită, adică trimestrul în care se situează luna mai 2026.

## Cheia

- Plafon 100.000 euro; curs valabil la închiderea exercițiului financiar precedent (31.12.2025); impozit pe profit începând cu trimestrul în care s-a depășit limita, adică trimestrul II 2026 (calculat pe veniturile și cheltuielile de la începutul trimestrului II)
- temei: Cod fiscal art. 52 alin. (1) (mod. OUG 8/2026 art. 6 pct. 20, aplicabil de la trim. I 2026 cf. art. 10 alin. (5) OUG 8/2026); art. 52 alin. (5) (mod. OUG 89/2025 art. I pct. 6); art. 52 alin. (6); art. 54 alin. (1)
