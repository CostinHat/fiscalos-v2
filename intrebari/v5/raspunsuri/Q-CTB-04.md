# Q-CTB-04 — REGULA

**Întrebarea:** Un mijloc fix corporal este pus în funcțiune pe 15 martie 2026. Din ce lună începe amortizarea contabilă?

## Stratul de navigare v5 — NU POT RĂSPUNDE

*La data de referință 15.03.2026, pentru o entitate care aplică reglementările contabile aprobate prin OMFP 1802/2014, presupun că este vorba de amortizarea contabilă a unei imobilizări corporale puse în funcțiune la 15 martie 2026, fără regim special.*

Datele din întrebare: 2026-03-15 · data de referință aleasă: **2026-03-15** — Singura dată din întrebare, data punerii în funcțiune, care determină momentul începerii amortizării.

Motiv: VERIFICAREA MECANICA a respins propunerea modelului: citatul NU e verbatim in atomul omfp_1802_2014#anexa/pct238/alin2

- **OMFP 1802/2014 anexa, pct. 238 alin. (2)** — `omfp_1802_2014#anexa/pct238/alin2` · valabil din nedovedit
  > Amortizarea imobiliz\u0103rilor corporale se calculeaz\u0103 \u00eencep\u00e2nd cu luna urm\u0103toare punerii \u00een func\u021biune \u0219i p\u00e2n\u0103 la recuperarea integral\u0103 a valorii lor.

### Navigarea (3 pași, 4 ture, 1 reîncercare C23)

1. `cauta` {"interogare": "amortizarea se calculează începând cu luna următoare punerii în funcțiune"}
2. `cuprins` {"act": "omfp_1802_2014_reglementari_consolidat", "filtru": "amortizare"}
3. `deschide` {"id": "omfp_1802_2014#anexa/pct238/alin2"}

Apel: `claude-opus-5`, {'intrare': 8, 'iesire': 1862, 'cache_scriere': 3134, 'cache_citire': 32364} tokeni, $0.0824, 30 s

Pe fond (comparator): **NU POT** — VERIFICAREA MECANICA a respins propunerea modelului: citatul NU e verbatim in atomul omfp_1802_2014#anexa/pct238/alin2

## v4 — RĂSPUNS, pe fond GREȘIT

> Amortizarea contabilă se calculează începând cu luna următoare punerii în funcțiune, deci din aprilie 2026.

## Cheia

- Din aprilie 2026 (luna următoare punerii în funcțiune), până la recuperarea integrală a valorii.
- temei: OMFP 1802/2014, Reglementări contabile, pct. 238 alin. (2)
