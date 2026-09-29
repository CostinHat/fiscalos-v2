# Q-TVA-06 — CAPCANA

**Întrebarea:** O firmă cu perioadă fiscală trimestrială face o livrare intracomunitară scutită în februarie 2026. Depune D390 trimestrial, odată cu D300 din aprilie?

## Stratul de navigare v5 — NU POT RĂSPUNDE

*—*

Datele din întrebare: 2026-02-28 · data de referință aleasă: **—** — 

Motiv: C23: structura răspunsului final a fost invalidă de două ori (marcaj de parametri scurs in raspunde.declaratie; marcaj de parametri scurs in raspunde.motiv; campul raspuns e gol sau un substituent ('') / marcaj de parametri scurs in raspunde.declaratie)


### Navigarea (6 pași, 6 ture, 1 reîncercare C23)

1. `cauta` {"interogare": "declaratie recapitulativa livrari intracomunitare lunar pana la data de 25"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "recapitulativă"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art325/alin2"}
4. `cuprins` {"act": "opanaf_705_2020_d390", "filtru": "depune"}
5. `cauta` {"interogare": "declarația recapitulativă se depune lunar până la data de 25 inclusiv a lunii următoare celei în care ia naștere exigibilitatea taxei"}
6. `deschide` {"id": "opanaf_705_2020_d390#anexa2/pct1"}

Apel: `claude-opus-5`, {'intrare': 12, 'iesire': 3874, 'cache_scriere': 9016, 'cache_citire': 59157} tokeni, $0.1828, 52 s

Pe fond (comparator): **NU POT** — C23: structura răspunsului final a fost invalidă de două ori (marcaj de parametri scurs in raspunde.declaratie; marcaj de parametri scurs in raspunde.motiv; campul raspuns e gol sau un substituent (''

## v4 — RĂSPUNS, pe fond GREȘIT

> Nu. Declarația recapitulativă 390 se depune lunar, până la data de 25 inclusiv a lunii următoare lunii calendaristice în care a intervenit operațiunea, indiferent de faptul că perioada fiscală pentru TVA (decontul D300) este trimestrială. Deci pentru livrarea intracomunitară din februarie 2026 D390 se depune până la 25 ale lunii următoare, nu în aprilie odată cu decontul trimestrial.

## Cheia

- Nu. D390 se depune lunar, pentru luna în care a luat naștere exigibilitatea, nu trimestrial cu D300. Exigibilitatea la livrarea intracomunitară = data facturii sau, dacă factura nu s-a emis până atunci, 15 a lunii următoare faptului generator. Factură emisă în februarie → D390 pentru februarie, până la 25.03.2026. Fără factură până la 15.03.2026 → D390 pentru martie, termen 25.04.2026 (sâmbătă), efectiv 27.04.2026.
- temei: Cod fiscal art. 283 alin. (1); art. 325 alin. (1) lit. a) și alin. (2); OPANAF 705/2020 anexa 2 pct. 1.1-1.2; CPF art. 75
