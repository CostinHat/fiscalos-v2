# Q-PRF-09 — PROCEDURA

**Întrebarea:** Societate care aplică sistemul anual cu plăți anticipate trimestriale. Cum se calculează plata anticipată pentru trimestrul I 2026, până când și cu ce declarație/cod?

## Stratul semantic — RĂSPUNS

*La data de referință 28.09.2026, presupun o societate plătitoare de impozit pe profit, persoană juridică română, care a optat pentru sistemul anual de declarare și plată a impozitului pe profit cu plăți anticipate trimestriale, care nu face parte dintr-un grup fiscal, nu este instituție de credit și nu se află în situații de reorganizare, iar anul fiscal coincide cu anul calendaristic.*

> **Pentru trimestrul I 2026 plata anticipată nu se mai determină ca o pătrime din impozitul anului precedent, ci prin aplicarea cotei de impozit asupra profitului contabil al perioadei pentru care se efectuează plata anticipată (trimestrul I). Aceasta se declară și se plătește până la data de 25 inclusiv a lunii următoare trimestrului I. Declararea se face trimestrial, pentru trimestrele I-III, prin formularul de declarare a obligațiilor de plată la bugetul de stat reglementat de OPANAF 587/2016, plățile anticipate în contul impozitului pe profit anual figurând la poziția 1 din Nomenclatorul obligațiilor de plată la bugetul de stat (anexa nr. 3 la ordin).**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 41 alin. (10^1)** — `cod_fiscal_227_2015_consolidat#art41/alin10^1` · valabil din 2026-02-25
  > Prin excepție de la prevederile alin. (8) , plata anticipată pentru trimestrul I al fiecărui an fiscal/an fiscal modificat se calculează prin aplicarea cotei de impozit asupra profitului contabil al perioadei pentru care se efectuează plata anticipată. Aceasta se declară și se plătește până la data de 25 inclusiv a lunii următoare trimestrului I.
- **OPANAF 587/2016 art. 7 pct. 1 pct. 2 pct. 4 pct. 4 pct. 1 pct. 1** — `opanaf_587_2016_aprobarea_modelului_continutului_formularelor_utilizate#art7~2/pct1/pct2/pct4/pct4/pct1/pct1` · valabil din 2025-02-07
  > b) plăți anticipate, în contul impozitului pe profit anual, pentru trimestrele I-III, datorate de către contribuabilii care au optat, potrivit legii, pentru declararea și plata impozitului pe profit anual, cu plăți anticipate, efectuate trimestrial;
- **OPANAF 587/2016 art. 7 pct. 1 pct. 3** — `opanaf_587_2016_aprobarea_modelului_continutului_formularelor_utilizate#art7~2/pct1/pct3` · valabil din 2024-02-02
  > Pentru plățile anticipate în contul impozitului pe profit anual, prevăzute la poziția 1 din Nomenclatorul obligațiilor de plată la bugetul de stat, prevăzut în anexa nr. 3 la ordin
- derogare tratată: `cod_fiscal_227_2015_consolidat#art41/alin8` — Regula generală a plăților anticipate de o pătrime din impozitul anului precedent este înlăturată pentru trimestrul I de excepția expresă din art. 41 alin. (10^1), aplicabilă începând cu anul fiscal 2026, pe care am citat-o ca temei decisiv.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art45/alin8` — Prevede aceeași regulă de calcul a plății anticipate pentru trimestrul I (cota aplicată profitului contabil, cu termen 25 inclusiv a lunii următoare trimestrului I), însă numai pentru contribuabilii care intră sub incidența OUG 153/2020; întrebarea nu indică această situație, iar rezultatul ar fi or…
- derogare tratată: `cod_fiscal_227_2015_consolidat#artVIII/alin1` — Derogarea privește exclusiv plățile anticipate pentru anul fiscal 2020, deci nu se aplică trimestrului I 2026.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art41/alin7` — Excepția vizează contribuabilii de la alin. (4) (instituții de credit) nou-înființați, cu pierdere fiscală în anul precedent sau foști plătitori de impozit pe veniturile microîntreprinderilor; nu s-a indicat o astfel de situație.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art41/alin10` — Excepția se aplică doar în al doilea an al perioadei obligatorii, când în primul an s-a înregistrat pierdere fiscală; nu rezultă din întrebare, iar regula de calcul pentru trimestrul I ar fi aceeași.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art42^9/alin3` — Vizează grupul fiscal (plățile anticipate stabilite de persoana juridică responsabilă); societatea din întrebare nu este prezentată ca membru al unui grup fiscal.

Apel: `claude-opus-5`, {'intrare': 10547, 'iesire': 5912, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.2015

Pe fond: **GREȘIT** — faptul principal al cheii (['16%']) nu e in raspuns

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: C17 (b): atomul pe care as raspunde are 6 derogari/exceptii/modificari valabile la data intrebarii (ex. cod_fiscal_227_2015_consolidat#artVIII/alin1: "Prin derogare de la prevederile art. 41 alin. (8) din Legea nr. 227/2015"); motorul lexical nu le poate trata, deci se abţine.

- **Codul fiscal (Legea 227/2015) art. 41 alin. (8)** — `cod_fiscal_227_2015_consolidat#art41/alin8` · valabil din nedovedit
  > … care aplică sistemul de declarare și plată a impozitului pe profit anual, cu plăți anticipate efectuate trimestrial, determină plățile anticipate trimestriale în sumă de o pătrime din impozitul pe profit datorat pentru anul precedent, actualizat cu indicele prețurilor de consum, estimat cu ocazia elaborării bugetului inițial al anului pentru care se efectuează plățile anticipate, până la data de 25 inclusiv a lunii următoare trimestrului pentru care se efectuează plata, cu excepția plății anti…

Pe fond: **NU POT** — C17 (b): atomul pe care as raspunde are 6 derogari/exceptii/modificari valabile la data intrebarii (ex. cod_fiscal_227_2015_consolidat#artVIII/alin1: "Prin derogare de la prevederile art. 41 alin. (8)

## Cheia

- 16% × profitul contabil al trimestrului I 2026 (NU 1/4 din impozitul anului precedent actualizat cu IPC); D100, cod obligație 103; termen nominal 25.04.2026 (sâmbătă) → efectiv 27.04.2026.
- temei: Cod fiscal art. 41 alin. (10^1) (OUG 8/2026 art. 6 pct. 11, aplicabil din anul fiscal 2026 cf. art. 10 alin. (2)); art. 17; structura D100 cod 103; CPF art. 75
