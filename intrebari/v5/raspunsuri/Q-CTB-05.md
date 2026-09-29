# Q-CTB-05 — PROCEDURA

**Întrebarea:** În 2026 se descoperă o factură de cheltuieli din 2024 neînregistrată. Pe ce cont se corectează eroarea?

## Stratul de navigare v5 — RĂSPUNS

*La data de 28.09.2026, pentru o entitate care aplică reglementările contabile conforme cu directivele europene (OMFP 1802/2014), presupun că factura de cheltuieli din 2024 neînregistrată reprezintă o eroare contabilă aferentă unui exercițiu financiar precedent, corectată în exercițiul 2026, și că entitatea nu aplică alte reglementări contabile speciale.*

Datele din întrebare: 2026-09-28, 2024-12-31 · data de referință aleasă: **2026-09-28** — Faptul întrebat este modul de corectare a erorii, operațiune efectuată în 2026, anul descoperirii; 2024 este doar exercițiul de proveniență a facturii.

> **Eroarea fiind aferentă unui exercițiu financiar precedent (2024), corectarea se face pe seama rezultatului reportat — contul 1174 „Rezultatul reportat provenit din corectarea erorilor contabile”. Aceasta este regula atât pentru erorile semnificative, cât și pentru cele nesemnificative; numai dacă eroarea este nesemnificativă și politicile contabile aprobate prevăd astfel, ea poate fi corectată pe seama contului de profit și pierdere (cheltuiala anului curent).**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **OMFP 1802/2014 anexa, pct. 67 alin. (2)** — `omfp_1802_2014#anexa/pct67/alin2` · valabil din nedovedit
  > Corectarea erorilor semnificative aferente exercițiilor financiare precedente se efectuează pe seama rezultatului reportat (contul 1174 "Rezultatul reportat provenit din corectarea erorilor contabile").
- **OMFP 1802/2014 anexa, pct. 67 alin. (3)** — `omfp_1802_2014#anexa/pct67/alin3` · valabil din nedovedit
  > Erorile nesemnificative aferente exercițiilor financiare precedente se corectează, de asemenea, pe seama rezultatului reportat. Totuși, potrivit politicilor contabile aprobate, erorile nesemnificative pot fi corectate pe seama contului de profit și pierdere.
- **OMFP 1802/2014 anexa, pct. 54 alin. (3)** — `omfp_1802_2014#anexa/pct54/alin3` · valabil din nedovedit
  > Înregistrarea pe seama rezultatului reportat a corectării erorilor semnificative aferente exercițiilor financiare precedente, precum și a modificării politicilor contabile nu se consideră încălcare a principiului intangi

### Navigarea (5 pași, 5 ture)

1. `cauta` {"interogare": "corectarea erorilor contabile rezultat reportat"}
2. `cuprins` {"act": "omfp_1802_2014_reglementari_consolidat", "filtru": "corectarea erorilor"}
3. `deschide` {"id": "omfp_1802_2014#anexa/pct67/alin2"}
4. `deschide` {"id": "omfp_1802_2014#anexa/pct67"}
5. `deschide` {"id": "omfp_1802_2014#anexa/pct67/alin3"}

Apel: `claude-opus-5`, {'intrare': 10, 'iesire': 2029, 'cache_scriere': 3111, 'cache_citire': 42383} tokeni, $0.0914, 36 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond GREȘIT

> Fiind o eroare aferentă unui exercițiu financiar precedent (2024), corectarea se face pe seama rezultatului reportat, în contul 1174 „Rezultatul reportat provenit din corectarea erorilor contabile" (obligatoriu pentru erorile semnificative). Dacă eroarea este nesemnificativă, ea se corectează de asemenea pe seama rezultatului reportat, dar, potrivit politicilor contabile aprobate, poate fi corectată pe seama contului de profit și pierdere (cheltuiala anului 2026).

## Cheia

- DEPINDE dacă eroarea e semnificativă și de politica contabilă aprobată — trebuie clarificat. Semnificativă: pe rezultatul reportat, cont 1174. Nesemnificativă: tot pe 1174, sau pe contul de profit și pierdere dacă politicile contabile permit. În niciun caz nu se retratează situațiile financiare 2024; se prezintă în notele explicative.
- temei: OMFP 1802/2014, Reglementări contabile, pct. 67 alin. (2)-(4) și pct. 68 alin. (1)-(3)
