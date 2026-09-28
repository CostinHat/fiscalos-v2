# Q-PRF-09 — PROCEDURA

**Întrebarea:** Societate care aplică sistemul anual cu plăți anticipate trimestriale. Cum se calculează plata anticipată pentru trimestrul I 2026, până când și cu ce declarație/cod?

## Stratul semantic (motorul nou) — RĂSPUNS

*La data de referință 28.09.2026, presupun o societate plătitoare de impozit pe profit, fără an fiscal modificat, care aplică sistemul anual de declarare și plată cu plăți anticipate trimestriale și care a datorat impozit pe profit în anul precedent (nu este în dizolvare cu lichidare și nu face parte dintr-un grup fiscal sau operațiuni de reorganizare).*

> **Plata anticipată pentru trimestrul I 2026 se stabilește în sumă de o pătrime din impozitul pe profit datorat pentru anul precedent (impozitul pe profit anual, conform declarației privind impozitul pe profit), actualizat cu indicele prețurilor de consum estimat cu ocazia elaborării bugetului inițial al anului pentru care se efectuează plățile anticipate. Termenul: până la data de 25 inclusiv a lunii următoare trimestrului pentru care se efectuează plata. Atomii primiți nu indică denumirea/codul formularului de declarare, deci acest element nu poate fi confirmat din textele furnizate.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 41 alin. (8)** — `cod_fiscal_227_2015_consolidat#art41/alin8` · valabil din nedovedit
  > determină plățile anticipate trimestriale în sumă de o pătrime din impozitul pe profit datorat pentru anul precedent, actualizat cu indicele prețurilor de consum, estimat cu ocazia elaborării bugetului inițial al anului pentru care se efectuează plățile anticipate, până la data de 25 inclusiv a lunii următoare trimestrului pentru care se efectuează plata
- **Codul fiscal (Legea 227/2015) art. 41 alin. (8)** — `cod_fiscal_227_2015_consolidat#art41/alin8` · valabil din nedovedit
  > Impozitul pe profit pentru anul precedent, pe baza căruia se determină plățile anticipate trimestriale, este impozitul pe profit anual, conform declarației privind impozitul pe profit.

Apel: `claude-opus-5`, {'intrare': 4565, 'iesire': 2405, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0837, 28.6 s

Pe fond: **GREȘIT** — faptul principal al cheii (['16%']) nu e in raspuns

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **Contribuabilii care aplică sistemul de declarare și plată a impozitului pe profit anual, cu plăți anticipate efectuate trimestrial, determină plățile anticipate trimestriale în sumă de o pătrime din impozitul pe profit datorat pentru anul precedent, actualizat cu indicele prețurilor de consum, estimat cu ocazia elaborării bugetului inițial al anului pentru care se efectuează plățile anticipate, până la data de 25 inclusiv a lunii următoare trimestrului pentru care se efectuează plata, cu excepția plății anticipate aferente trimestrului IV care se declară și se plătește până la data de 25 decembrie, respectiv până la data de 25 a ultimei luni din anul fiscal modificat.**

Motiv: D15: fraza care conţine un fapt de forma cerută (termen) si potriveste cel mai bine intrebarea (scor local 22.4)

- **Codul fiscal (Legea 227/2015) art. 41 alin. (8)** — `cod_fiscal_227_2015_consolidat#art41/alin8` · valabil din nedovedit
  > … care aplică sistemul de declarare și plată a impozitului pe profit anual, cu plăți anticipate efectuate trimestrial, determină plățile anticipate trimestriale în sumă de o pătrime din impozitul pe profit datorat pentru anul precedent, actualizat cu indicele prețurilor de consum, estimat cu ocazia elaborării bugetului inițial al anului pentru care se efectuează plățile anticipate, până la data de 25 inclusiv a lunii următoare trimestrului pentru care se efectuează plata, cu excepția plății anticipate aferente trimestrului IV care se declară și se plătește până la data de 25 decembrie, respect…

Pe fond: **GREȘIT** — faptul principal al cheii (['16%']) nu e in raspuns

## Cheia

- răspuns așteptat: 16% × profitul contabil al trimestrului I 2026 (NU 1/4 din impozitul anului precedent actualizat cu IPC); D100, cod obligație 103; termen nominal 25.04.2026 (sâmbătă) → efectiv 27.04.2026.
- temei așteptat: Cod fiscal art. 41 alin. (10^1) (OUG 8/2026 art. 6 pct. 11, aplicabil din anul fiscal 2026 cf. art. 10 alin. (2)); art. 17; structura D100 cod 103; CPF art. 75

