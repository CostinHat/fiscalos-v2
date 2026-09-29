# Q-PRF-09 — PROCEDURA

**Întrebarea:** Societate care aplică sistemul anual cu plăți anticipate trimestriale. Cum se calculează plata anticipată pentru trimestrul I 2026, până când și cu ce declarație/cod?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 28.09.2026, pentru o societate plătitoare de impozit pe profit care aplică sistemul anual cu plăți anticipate trimestriale (an fiscal egal cu anul calendaristic 2026), fără a fi instituție de credit, grup fiscal sau contribuabil în lichidare, presupun că nu beneficiază de facilitățile OUG nr. 153/2020.*

Datele din întrebare: 2026-09-28 · data de referință aleasă: **2026-09-28** — Singura dată purtată de întrebare; faptul întrebat este plata anticipată aferentă trimestrului I al anului fiscal 2026, iar regimul reținut este cel în vigoare la această dată.

> **Pentru trimestrul I 2026 nu se aplică regula generală a pătrimii din impozitul anului precedent actualizat cu indicele prețurilor de consum: prin excepție, plata anticipată a trimestrului I se calculează aplicând cota de impozit pe profit de 16% asupra profitului contabil al perioadei pentru care se efectuează plata anticipată (trimestrul I). Se declară și se plătește până la data de 25 inclusiv a lunii următoare trimestrului I. Declarația este formularul 100 „Declarație privind obligațiile de plată la bugetul de stat”, cod 14.13.01.99/bs, obligația fiind cea de la poziția 1 din Nomenclatorul obligațiilor de plată la bugetul de stat (plăți anticipate în contul impozitului pe profit anual).**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 41 alin. (10^1)** — `cod_fiscal_227_2015_consolidat#art41/alin10^1` · valabil din 2026-02-25
  > Prin excepție de la prevederile alin. (8) , plata anticipată pentru trimestrul I al fiecărui an fiscal/an fiscal modificat se calculează prin aplicarea cotei de impozit asupra profitului contabil al perioadei pentru care se efectuează plata anticipată. Aceasta se declară și se plătește până la data de 25 inclusiv a lunii următoare trimestrului I.
- **Codul fiscal (Legea 227/2015) art. 17** — `cod_fiscal_227_2015_consolidat#art17` · valabil din nedovedit
  > Cota de impozitare Cota de impozit pe profit care se aplică asupra profitului impozabil este de 16%.
- **Codul fiscal (Legea 227/2015) art. 41 alin. (8)** — `cod_fiscal_227_2015_consolidat#art41/alin8` · valabil din nedovedit
  > determină plățile anticipate trimestriale în sumă de o pătrime din impozitul pe profit datorat pentru anul precedent, actualizat cu indicele prețurilor de consum, estimat cu ocazia elaborării bugetului inițial al anului pentru care se efectuează plățile anticipate, până la data de 25 inclusiv a lunii următoare trimestrului pentru care se efectuează plata
- **OPANAF 587/2016 art. 1 alin. (1)** — `opanaf_587_2016_aprobarea_modelului_continutului_formularelor_utilizate#art1/alin1` · valabil din nedovedit
  > a) 100 "Declarație privind obligațiile de plată la bugetul de stat", cod 14.13.01.99/bs, prevăzut în anexa nr. 1
- **OPANAF 587/2016 anexa nr. 4, pct. 3** — `opanaf_587_2016_aprobarea_modelului_continutului_formularelor_utilizate#anexa4/pct3` · valabil din 2024-02-02
  > Pentru plățile anticipate în contul impozitului pe profit anual, prevăzute la poziția 1 din Nomenclatorul obligațiilor de plată la bugetul de stat, prevăzut în anexa nr. 3 la ordin
- derogare tratată: `cod_fiscal_227_2015_consolidat#art41/alin10^1` — Este excepția aplicabilă cazului: pentru trimestrul I al anului fiscal 2026 înlocuiește regula pătrimii din art. 41 alin. (8); a fost citată ca temei decisiv.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art41/alin7` — Nu se aplică: privește contribuabilii de la art. 41 alin. (4) (instituții de credit) nou-înființați, cu pierdere fiscală în anul precedent sau foști plătitori de impozit pe veniturile microîntreprinderilor; întrebarea descrie o societate care aplică sistemul anual cu plăți anticipate trimestriale.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art41/alin10` — Nu se aplică: vizează situația specială a contribuabilului care în primul an al perioadei obligatorii a înregistrat pierdere fiscală ori nu a datorat impozit anual, situație neindicată în întrebare.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art45/alin8` — Excepție tranzitorie de la art. 41 alin. (8) care nu este invocată de datele cazului; pentru trimestrul I al anului 2026 regula aplicabilă este cea din art. 41 alin. (10^1).
- derogare tratată: `opanaf_587_2016_aprobarea_modelului_continutului_formularelor_utilizate#anexa4/pct3` — Excepția din instrucțiunile formularului 100 privește contribuabilii sub incidența OUG nr. 153/2020 și instituțiile de credit; din acest atom am reținut doar încadrarea plăților anticipate la poziția 1 din Nomenclator, presupunând că societatea nu aplică OUG nr. 153/2020.

### Navigarea (16 pași, 11 ture, 1 reîncercare C23)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "plata impozitului"}
2. `cauta` {"interogare": "plăți anticipate trimestriale impozit pe profit indice prețuri de consum"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art41/alin8"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art41/alin2"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art41/alin7"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art41/alin10"}
7. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art41/alin10^1"}
8. `cauta` {"interogare": "formular 100 Declarație privind obligațiile de plată la bugetul de stat nomenclator impozit pe profit"}
9. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art17"}
10. `cuprins` {"act": "opanaf_57_2026_d100_d710", "filtru": "impozit pe profit"}
11. `cuprins` {"act": "opanaf_57_2026_d100_d710", "filtru": "100"}
12. `cauta` {"interogare": "nomenclatorul obligațiilor de plată la bugetul de stat 1 Impozit pe profit 14.13.01.99/bs"}
13. `cuprins` {"act": "opanaf_57_2026_d100_d710", "filtru": ""}
14. `deschide` {"id": "opanaf_1950_2012#anexa6/pct1/litb~3"}
15. `deschide` {"id": "opanaf_587_2016_aprobarea_modelului_continutului_formularelor_utilizate#anexa4/pct3"}
16. `cauta` {"interogare": "100 \"Declarație privind obligațiile de plată la bugetul de stat\", cod 14.13.01.99/bs prevăzut în anexa nr. 1"}

Apel: `claude-opus-5`, {'intrare': 22, 'iesire': 9857, 'cache_scriere': 23465, 'cache_citire': 182398} tokeni, $0.4844, 148 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond GREȘIT

> Pentru trimestrul I 2026, plata anticipată NU se stabilește ca o pătrime din impozitul anului precedent, ci prin aplicarea cotei de impozit asupra profitului contabil al perioadei pentru care se efectuează plata anticipată. Ea se declară și se plătește până la data de 25 inclusiv a lunii următoare trimestrului I (adică 25 aprilie 2026), prin formularul 100 „Declarație privind obligațiile de plată la bugetul de stat”, cod 14.13.01.99/bs.

## Cheia

- 16% × profitul contabil al trimestrului I 2026 (NU 1/4 din impozitul anului precedent actualizat cu IPC); D100, cod obligație 103; termen nominal 25.04.2026 (sâmbătă) → efectiv 27.04.2026.
- temei: Cod fiscal art. 41 alin. (10^1) (OUG 8/2026 art. 6 pct. 11, aplicabil din anul fiscal 2026 cf. art. 10 alin. (2)); art. 17; structura D100 cod 103; CPF art. 75
