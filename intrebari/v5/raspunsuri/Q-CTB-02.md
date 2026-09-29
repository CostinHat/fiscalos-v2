# Q-CTB-02 — CAPCANA

**Întrebarea:** O societate are un echipament cu valoare fiscală de intrare de 3.200 lei, intrat în 2024 și amortizat parțial la 31.12.2025. Din 2026 pragul e 5.000 lei: se trece valoarea rămasă integral pe cheltuieli deductibile în 2026?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 28.09.2026, pentru un plătitor de impozit pe profit care deține un mijloc fix cu valoare fiscală de intrare de 3.200 lei, intrat în patrimoniu în 2024 și parțial amortizat la 31.12.2025, presupunând an fiscal calendaristic și că bunul îndeplinea condițiile de mijloc fix amortizabil la data intrării.*

Datele din întrebare: 2025-12-31, 2024-12-31, 2026-09-28 · data de referință aleasă: **2026-09-28** — Faptul întrebat este tratamentul fiscal al valorii rămase în anul 2026, deci data din anul 2026; datele 31.12.2025 și 2024 sunt doar fapte ale cazului (momentul intrării și al amortizării parțiale).

> **Nu. Pentru mijloacele fixe cu valoare fiscală de intrare cuprinsă între 2.500 lei și 5.000 lei existente în patrimoniu la 31 decembrie 2025, valoarea fiscală rămasă neamortizată nu se deduce integral în 2026, ci se recuperează pe durata normală de utilizare rămasă, prin amortizare fiscală. Noul prag de 5.000 lei se aplică doar activelor la data intrării lor în patrimoniu.**

Citatul decisiv (`cod_fiscal_227_2015_consolidat#art45/alin21^3`):
> valoarea fiscală rămasă neamortizată a mijloacelor fixe cu valoarea fiscală de intrare cuprinsă între 2.500 lei și 5.000 lei, existente în patrimoniul contribuabililor la data de 31 decembrie 2025/ultima zi a anului fiscal modificat care se încheie în anul 2026, se recuperează pe durata normală de utilizare rămasă.

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 45 alin. (21^3)** — `cod_fiscal_227_2015_consolidat#art45/alin21^3` · valabil din 2026-02-25
  > valoarea fiscală rămasă neamortizată a mijloacelor fixe cu valoarea fiscală de intrare cuprinsă între 2.500 lei și 5.000 lei, existente în patrimoniul contribuabililor la data de 31 decembrie 2025/ultima zi a anului fiscal modificat care se încheie în anul 2026, se recuperează pe durata normală de utilizare rămasă.
- **Codul fiscal (Legea 227/2015) art. 28 alin. (2) lit. b)** — `cod_fiscal_227_2015_consolidat#art28/alin2/litb` · valabil din 2026-02-25
  > la data intrării în patrimoniul contribuabilului, are o valoare fiscală egală sau mai mare decât suma de 5.000 lei; această limită se actualizată anual, în funcție de indicele de inflație, prin hotărâre a Guvernului;

### Navigarea (6 pași, 4 ture)

1. `cauta` {"interogare": "mijloc fix amortizabil valoare de intrare 5.000 lei"}
2. `cauta` {"interogare": "mijloacele fixe intrate în patrimoniu anterior regimul de amortizare în vigoare la data intrării"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art28/alin2"}
4. `cauta` {"interogare": "valoarea de intrare a mijloacelor fixe 5.000 lei începând cu 2026"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art45/alin21^3"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art28/alin2/litb"}

Apel: `claude-opus-5`, {'intrare': 8, 'iesire': 2513, 'cache_scriere': 6396, 'cache_citire': 36871} tokeni, $0.1213, 34 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond GREȘIT

> Nu. Condiția de valoare (limita stabilită prin hotărâre a Guvernului) se apreciază la data intrării în patrimoniu, așa că echipamentul rămâne mijloc fix amortizabil, iar valoarea rămasă neamortizată se recuperează în continuare prin deduceri de amortizare, pe durata normală de funcționare rămasă, nu integral pe cheltuieli deductibile într-un singur an.

## Cheia

- Nu. Valoarea fiscală rămasă neamortizată a mijloacelor fixe cu valoare de intrare între 2.500 și 5.000 lei existente la 31.12.2025 se recuperează în continuare pe durata normală de utilizare rămasă.
- temei: Legea 227/2015 art. 45 alin. (21^3), introdus de OUG 8/2026 art. 6 pct. 14
