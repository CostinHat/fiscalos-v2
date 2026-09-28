# Q-PRF-09 — PROCEDURA

**Întrebarea:** Societate care aplică sistemul anual cu plăți anticipate trimestriale. Cum se calculează plata anticipată pentru trimestrul I 2026, până când și cu ce declarație/cod?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 28.09.2026, presupun o persoană juridică română plătitoare de impozit pe profit, alta decât instituțiile de credit, care aplică sistemul anual de declarare și plată a impozitului pe profit cu plăți anticipate trimestriale, cu an fiscal calendaristic (2026) și fără situații speciale (reorganizare, dizolvare, an fiscal modificat, grup fiscal), acestea nefiind menționate în întrebare.*

> **Pentru trimestrul I 2026, plata anticipată NU se stabilește ca o pătrime din impozitul anului precedent, ci prin aplicarea cotei de impozit asupra profitului contabil al perioadei pentru care se efectuează plata anticipată. Ea se declară și se plătește până la data de 25 inclusiv a lunii următoare trimestrului I (adică 25 aprilie 2026), prin formularul 100 „Declarație privind obligațiile de plată la bugetul de stat”, cod 14.13.01.99/bs.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 41 alin. (10^1)** — `cod_fiscal_227_2015_consolidat#art41/alin10^1` · valabil din 2026-02-25
  > Prin excepție de la prevederile alin. (8) , plata anticipată pentru trimestrul I al fiecărui an fiscal/an fiscal modificat se calculează prin aplicarea cotei de impozit asupra profitului contabil al perioadei pentru care se efectuează plata anticipată. Aceasta se declară și se plătește până la data de 25 inclusiv a lunii următoare trimestrului I.
- **OPANAF 587/2016 art. 1 alin. (1)** — `opanaf_587_2016_aprobarea_modelului_continutului_formularelor_utilizate#art1/alin1` · valabil din nedovedit
  > Se aprobă modelul și conținutul următoarelor formulare: a) 100 "Declarație privind obligațiile de plată la bugetul de stat", cod 14.13.01.99/bs, prevăzut în anexa nr. 1
- **Codul fiscal (Legea 227/2015) art. 41 alin. (8)** — `cod_fiscal_227_2015_consolidat#art41/alin8` · valabil din nedovedit
  > Contribuabilii care aplică sistemul de declarare și plată a impozitului pe profit anual, cu plăți anticipate efectuate trimestrial, determină plățile anticipate trimestriale în sumă de o pătrime din impozitul pe profit datorat pentru anul precedent, actualizat cu indicele prețurilor de consum
- derogare tratată: `cod_fiscal_227_2015_consolidat#art41/alin10^1` — Se aplică și este regula decisivă: pentru trimestrul I al fiecărui an fiscal, prin excepție de la art. 41 alin. (8), plata anticipată se calculează prin aplicarea cotei de impozit asupra profitului contabil al perioadei; textul se aplică începând cu anul fiscal 2026 (OUG nr. 8/2026), deci și pentru …
- derogare tratată: `cod_fiscal_227_2015_consolidat#art41/alin7` — Nu se aplică: vizează contribuabilii prevăzuți la art. 41 alin. (4) (instituții de credit) nou-înființați, situație neindicată în întrebare.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art41/alin10` — Nu se aplică: vizează contribuabilii care, în primul an al perioadei obligatorii de aplicare a sistemului anual prin opțiune (art. 41 alin. (2)-(3)), se află în situațiile speciale descrise acolo; întrebarea nu indică primul an al opțiunii.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art45/alin8` — Nu se aplică: este o normă tranzitorie pentru situații specifice de trecere, neindicată în cazul din întrebare.
- derogare tratată: `opanaf_587_2016_aprobarea_modelului_continutului_formularelor_utilizate#art7~2/pct1/pct3` — Instrucțiunea de completare a formularului 100 confirmă regula pentru trimestrul I (aplicarea cotei asupra profitului contabil) în cazul contribuabililor sub incidența OUG nr. 153/2020; nu schimbă concluzia, întrucât regula legală generală pentru trimestrul I este dată de art. 41 alin. (10^1).

### Navigarea (12 pași, 7 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "plăți anticipate"}
2. `cauta` {"interogare": "plăți anticipate trimestriale impozit pe profit trimestrul I 25 aprilie"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art41/alin8"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art41"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art41/alin10^1"}
6. `deschide` {"id": "opanaf_587_2016_aprobarea_modelului_continutului_formularelor_utilizate#art7~2/pct1/pct3"}
7. `cauta` {"interogare": "Nomenclatorul obligațiilor de plată la bugetul de stat poziția 1 Plăți anticipate în contul impozitului pe profit anual formular 100"}
8. `cuprins` {"act": "opanaf_57_2026_d100_d710", "filtru": ""}
9. `cauta` {"interogare": "formularul 100 \"Declarație privind obligațiile de plată la bugetul de stat\" cod 14.13.01.99/bs"}
10. `cauta` {"interogare": "Plăți anticipate în contul impozitului pe profit anual - trimestrial termen de declarare 25 inclusiv a lunii următoare trimestrului"}
11. `cuprins` {"act": "opanaf_57_2026_d100_d710", "filtru": "100"}
12. `deschide` {"id": "opanaf_587_2016_aprobarea_modelului_continutului_formularelor_utilizate#art1/alin1"}

Apel: `claude-opus-5`, {'intrare': 14, 'iesire': 4810, 'cache_scriere': 17549, 'cache_citire': 100782} tokeni, $0.2804, 71 s

Pe fond: **GREȘIT** — faptul principal al cheii (['16%']) nu e in raspuns

## Stratul semantic v3 (context dat de căutare) — RĂSPUNS, pe fond GREȘIT

> Pentru trimestrul I 2026 plata anticipată nu se mai determină ca o pătrime din impozitul anului precedent, ci prin aplicarea cotei de impozit asupra profitului contabil al perioadei pentru care se efectuează plata anticipată (trimestrul I). Aceasta se declară și se plătește până la data de 25 inclusiv a lunii următoare trimestrului I. Declararea se face trimestrial, pentru trimestrele I-III, prin formularul de declarare a obligațiilor de plată la bugetul de stat reglementat de OPANAF 587/2016, p…

## Cheia

- 16% × profitul contabil al trimestrului I 2026 (NU 1/4 din impozitul anului precedent actualizat cu IPC); D100, cod obligație 103; termen nominal 25.04.2026 (sâmbătă) → efectiv 27.04.2026.
- temei: Cod fiscal art. 41 alin. (10^1) (OUG 8/2026 art. 6 pct. 11, aplicabil din anul fiscal 2026 cf. art. 10 alin. (2)); art. 17; structura D100 cod 103; CPF art. 75
