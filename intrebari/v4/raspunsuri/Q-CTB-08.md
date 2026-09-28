# Q-CTB-08 — CAPCANA

**Întrebarea:** În 2025 s-au distribuit dividende interimare cu impozit de 10%. În 2026 se aprobă situațiile financiare 2025 și se regularizează dividendele interimare. Se recalculează impozitul la 16%?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 31.12.2025, pentru o societate română care a distribuit dividende în cursul anului 2025 pe baza situațiilor financiare interimare (impozitate cu 10%) și care regularizează aceste dividende în 2026, după aprobarea situațiilor financiare anuale ale exercițiului 2025; presupun exercițiu financiar coincident cu anul calendaristic și dividende supuse impozitului pe dividende.</declaratie>
<parameter name="raspuns">Nu. Pentru dividendele distribuite în baza situațiilor financiare interimare întocmite în cursul anului 2025, cota rămâne 10%, fără recalcularea impozitului după regularizarea făcută pe baza situațiilor financiare anuale aferente exercițiului 2025 aprobate potrivit legii.*

> ****

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Legea 141/2025 art. VII alin. (2)** — `legea_141_2025_consolidat#artVII/alin2` · valabil din nedovedit
  > În cazul dividendelor distribuite în baza situațiilor financiare interimare întocmite în cursul anului 2025/anului fiscal modificat care începe în anul 2025, cota de impozit pe dividende este de 10%, fără recalcularea impozitului pe dividendele respective, după regularizarea acestora pe baza situațiilor financiare anuale aferente exercițiului financiar 2025/anului fiscal modificat care începe în anul 2025, aprobate potrivit legii.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art43/alin2` — Cota generală de 16% prevăzută de Codul fiscal nu se aplică retroactiv dividendelor interimare din 2025: norma tranzitorie din Legea 141/2025 art. VII alin. (2) menține expres cota de 10% și interzice recalcularea la regularizarea pe baza situațiilor financiare anuale 2025.

### Navigarea (3 pași, 3 ture)

1. `cauta` {"interogare": "cota de 16% dividende distribuite interimar regularizare situații financiare anuale"}
2. `cauta` {"interogare": "impozit pe dividende 10% dividende interimare 2025 se aplică"}
3. `deschide` {"id": "legea_141_2025_consolidat#artVII/alin2"}

Apel: `claude-opus-5`, {'intrare': 6, 'iesire': 1466, 'cache_scriere': 3316, 'cache_citire': 22216} tokeni, $0.0685, 22 s

Pe fond: **GREȘIT** — faptul principal al cheii (['10%']) nu e in raspuns

## Stratul semantic v3 (context dat de căutare) — RĂSPUNS, pe fond CORECT

> Nu. Pentru dividendele distribuite în baza situațiilor financiare interimare întocmite în cursul anului 2025, cota de impozit pe dividende rămâne de 10%, fără recalcularea impozitului după regularizarea lor pe baza situațiilor financiare anuale aferente exercițiului financiar 2025, aprobate potrivit legii.

## Cheia

- Nu. Pentru dividendele distribuite pe baza situațiilor interimare din 2025 cota rămâne 10%, fără recalculare după regularizare. (Cota se stabilește după data distribuirii, nu a plății sau a aprobării anuale.)
- temei: Legea 141/2025 art. VII alin. (2); Legea 227/2015 art. 43 alin. (2) și art. 97 alin. (7) cu aplicare de la 01.01.2026 (Legea 141/2025 art. VII alin. (1) lit. a) și c))
