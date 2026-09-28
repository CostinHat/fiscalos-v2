# Q-CTB-08 — CAPCANA

**Întrebarea:** În 2025 s-au distribuit dividende interimare cu impozit de 10%. În 2026 se aprobă situațiile financiare 2025 și se regularizează dividendele interimare. Se recalculează impozitul la 16%?

## Stratul semantic — RĂSPUNS

*La data de referință 31.12.2025, presupun un plătitor de dividende (persoană juridică română cu exercițiu financiar coincident cu anul calendaristic) care a distribuit dividende în cursul anului 2025 pe baza situațiilor financiare interimare, reținând impozit pe dividende, și care regularizează aceste dividende în 2026, după aprobarea situațiilor financiare anuale aferente exercițiului 2025.*

> **Nu. Pentru dividendele distribuite în baza situațiilor financiare interimare întocmite în cursul anului 2025, cota de impozit pe dividende rămâne de 10%, fără recalcularea impozitului după regularizarea lor pe baza situațiilor financiare anuale aferente exercițiului financiar 2025, aprobate potrivit legii.**

Citatul decisiv (`legea_141_2025#artVII/alin2`):
> În cazul dividendelor distribuite în baza situaţiilor financiare interimare întocmite în cursul anului 2025/anului fiscal modificat care începe în anul 2025, cota de impozit pe dividende este de 10%, fără recalcularea impozitului pe dividendele respective, după regularizarea acestora pe baza situaţiilor financiare anuale aferente exerciţiului financiar 2025/anului fiscal modificat care începe în anul 2025, aprobate potrivit legii.

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Legea 141/2025 art. VII alin. (2)** — `legea_141_2025#artVII/alin2` · valabil din nedovedit
  > În cazul dividendelor distribuite în baza situaţiilor financiare interimare întocmite în cursul anului 2025/anului fiscal modificat care începe în anul 2025, cota de impozit pe dividende este de 10%, fără recalcularea impozitului pe dividendele respective, după regularizarea acestora pe baza situaţiilor financiare anuale aferente exerciţiului financiar 2025/anului fiscal modificat care începe în anul 2025, aprobate potrivit legii.
- **Legea 141/2025 art. VII alin. (2)** — `legea_141_2025_consolidat#artVII/alin2` · valabil din nedovedit
  > În cazul dividendelor distribuite în baza situațiilor financiare interimare întocmite în cursul anului 2025/anului fiscal modificat care începe în anul 2025, cota de impozit pe dividende este de 10%, fără recalcularea impozitului pe dividendele respective, după regularizarea acestora pe baza situațiilor financiare anuale aferente exercițiului financiar 2025
- **OMFP 3067/2018 art. III alin. (1)** — `omfp_3067_2018#artIII/alin1` · valabil din nedovedit
  > Situațiile financiare interimare reprezintă situații financiare cu scop special, fiind destinate repartizării de dividende în cursul exercițiului financiar.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art43/alin3` — Derogarea vizează exclusiv termenul de plată a impozitului pentru dividendele distribuite și neplătite până la sfârșitul anului aprobării distribuirii, nu cota de impozit; nu afectează regula potrivit căreia dividendele interimare din 2025 rămân impozitate cu 10% fără recalculare la regularizare.

Apel: `claude-opus-5`, {'intrare': 3016, 'iesire': 1526, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0542

Pe fond: **CORECT** — faptul principal si articolul coincid

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2025-12-31 (an, din "2025"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: D15: intrebarea cere o JUDECATA (Da/Nu) - aplicarea unei reguli la faptele date. Motorul nu compune si nu aplica reguli; atasez regula cea mai bine potrivita, ca material, nu ca raspuns.


Pe fond: **NU POT** — D15: intrebarea cere o JUDECATA (Da/Nu) - aplicarea unei reguli la faptele date. Motorul nu compune si nu aplica reguli; atasez regula cea mai bine potrivita, ca material, nu ca raspuns.

## Cheia

- Nu. Pentru dividendele distribuite pe baza situațiilor interimare din 2025 cota rămâne 10%, fără recalculare după regularizare. (Cota se stabilește după data distribuirii, nu a plății sau a aprobării anuale.)
- temei: Legea 141/2025 art. VII alin. (2); Legea 227/2015 art. 43 alin. (2) și art. 97 alin. (7) cu aplicare de la 01.01.2026 (Legea 141/2025 art. VII alin. (1) lit. a) și c))
