# Q-CTB-05 — PROCEDURA

**Întrebarea:** În 2026 se descoperă o factură de cheltuieli din 2024 neînregistrată. Pe ce cont se corectează eroarea?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 28.09.2026, presupun o entitate care aplică reglementările contabile OMFP 1802/2014 (situații financiare anuale individuale), care descoperă în exercițiul 2026 o factură de cheltuieli aferentă exercițiului financiar precedent 2024, neînregistrată; întrebarea nu precizează dacă eroarea este semnificativă sau nesemnificativă, nici ce prevăd politicile contabile proprii, așa că indic regula de bază și opțiunea aplicabilă erorilor nesemnificative.*

> **Fiind o eroare aferentă unui exercițiu financiar precedent (2024), corectarea se face pe seama rezultatului reportat, în contul 1174 „Rezultatul reportat provenit din corectarea erorilor contabile" (obligatoriu pentru erorile semnificative). Dacă eroarea este nesemnificativă, ea se corectează de asemenea pe seama rezultatului reportat, dar, potrivit politicilor contabile aprobate, poate fi corectată pe seama contului de profit și pierdere (cheltuiala anului 2026).**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **OMFP 1802/2014 art. 12 alin. (2)** — `omfp_1802_2014#art12~2/alin2~37` · valabil din nedovedit
  > Corectarea erorilor semnificative aferente exercițiilor financiare precedente se efectuează pe seama rezultatului reportat (contul 1174 "Rezultatul reportat provenit din corectarea erorilor contabile").
- **OMFP 1802/2014 art. 12 alin. (3)** — `omfp_1802_2014#art12~2/alin3~26` · valabil din nedovedit
  > Erorile nesemnificative aferente exercițiilor financiare precedente se corectează, de asemenea, pe seama rezultatului reportat. Totuși, potrivit politicilor contabile aprobate, erorile nesemnificative pot fi corectate pe seama contului de profit și pierdere.

### Navigarea (6 pași, 6 ture)

1. `cauta` {"interogare": "corectarea erorilor contabile rezultat reportat 1174"}
2. `cuprins` {"act": "omfp_1802_2014_reglementari_consolidat", "filtru": "erori"}
3. `deschide` {"id": "omfp_1802_2014#art12~2/alin2~37"}
4. `deschide` {"id": "omfp_1802_2014#art12~2"}
5. `cauta` {"interogare": "erorile nesemnificative aferente exercițiilor financiare precedente se corectează pe seama contului de profit și pierdere"}
6. `deschide` {"id": "omfp_1802_2014#art12~2/alin3~26"}

Apel: `claude-opus-5`, {'intrare': 12, 'iesire': 2244, 'cache_scriere': 8484, 'cache_citire': 56985} tokeni, $0.1377, 38 s

Pe fond: **GREȘIT** — articolul citat [('omfp_1802_2014', '12')] nu e printre cele ale cheii [('omfp_1802_2014', 'pct67'), (None, 'pct68')]

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți nu conțin regula contabilă privind corectarea erorilor aferente exercițiilor financiare precedente și nici simbolul/denumirea contului pe care se face corecția. Atomii fiscali (art. 19 alin. (3) lit. b) și art. 46^1 alin. (4^3) din Codul fiscal) doar menționează, pentru scopuri fiscale, ipotezele de corectare „pe seama contului de profit și pierdere”, respectiv „pe seama rezultatului reportat”, fără a stabili ce cont se folosește și în ce condiții (eroare semn…

## Cheia

- DEPINDE dacă eroarea e semnificativă și de politica contabilă aprobată — trebuie clarificat. Semnificativă: pe rezultatul reportat, cont 1174. Nesemnificativă: tot pe 1174, sau pe contul de profit și pierdere dacă politicile contabile permit. În niciun caz nu se retratează situațiile financiare 2024; se prezintă în notele explicative.
- temei: OMFP 1802/2014, Reglementări contabile, pct. 67 alin. (2)-(4) și pct. 68 alin. (1)-(3)
