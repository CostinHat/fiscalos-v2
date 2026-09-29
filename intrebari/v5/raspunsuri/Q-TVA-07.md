# Q-TVA-07 — PROCEDURA

**Întrebarea:** O firmă înregistrată în scopuri de TVA, cu perioadă fiscală lunară, nu a avut nicio operațiune în ianuarie 2026. Trebuie să depună D394 pentru ianuarie și până când?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 31.01.2026, pentru o persoană impozabilă înregistrată în scopuri de TVA în România conform art. 316 Cod fiscal, cu perioadă fiscală lunară, fără operațiuni în luna ianuarie 2026, presupunând că societatea este activă (nu în inactivitate temporară înscrisă în registrul comerțului) și că are obligația declarativă D394 conform OPANAF 2194/2025, aplicabil operațiunilor derulate de la 1.08.2025.*

Datele din întrebare: 2026-01-31 · data de referință aleasă: **2026-01-31** — Faptul întrebat privește obligația declarativă aferentă perioadei de raportare ianuarie 2026, singura dată din întrebare.

> **Da, declarația 394 se depune și pentru o lună fără operațiuni (se bifează situația lipsei operațiunilor de natura celor declarabile). Regula generală este până în data de 30 inclusiv a lunii următoare perioadei de raportare, iar pentru luna ianuarie termenul este până la data de 28, respectiv 29 februarie — deci pentru ianuarie 2026, până la 28 februarie 2026.**

Citatul decisiv (`opanaf_2194_2025_d394#anexa2/pct2`):
> inclusiv dacă în această perioadă nu au fost realizate operaţiuni de natura celor care fac obiectul declaraţiei. În cazul în care perioada de raportare este luna calendaristică, termenul de depunere a declaraţiei pentru luna ianuarie este până la data de 28, respectiv 29 februarie.

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **OPANAF 2194/2025 anexa nr. 2, pct. 2** — `opanaf_2194_2025_d394#anexa2/pct2` · valabil din nedovedit
  > inclusiv dacă în această perioadă nu au fost realizate operaţiuni de natura celor care fac obiectul declaraţiei. În cazul în care perioada de raportare este luna calendaristică, termenul de depunere a declaraţiei pentru luna ianuarie este până la data de 28, respectiv 29 februarie.
- **OPANAF 2194/2025 anexa nr. 2, pct. 2** — `opanaf_2194_2025_d394#anexa2/pct2` · valabil din nedovedit
  > Declaraţia se depune la organul fiscal competent până în data de 30 inclusiv a lunii următoare încheierii perioadei de raportare, declarate pentru depunerea decontului (luna, trimestrul etc.), inclusiv dacă în această perioadă nu au fost realizate operaţiuni
- **OPANAF 2194/2025 anexa nr. 2, pct. 1 lit. a)** — `opanaf_2194_2025_d394#anexa2/pct1/lita` · valabil din nedovedit
  > persoanele impozabile înregistrate în scopuri de TVA în România conform art. 316 din Legea nr. 227/2015 privind Codul fiscal, cu modificările şi completările ulterioare, denumită în continuare Codul fiscal
- **OPANAF 2194/2025 art. II** — `opanaf_2194_2025_d394#artII` · valabil din nedovedit
  > Anexele nr. 1 şi 2 fac parte integrantă din prezentul ordin. Art. III - Prevederile prezentului ordin se aplică începând cu operaţiunile derulate de la data de 1.08.2025.

### Navigarea (7 pași, 7 ture)

1. `cauta` {"interogare": "declarația 394 termen depunere 30 a lunii următoare perioadei de raportare"}
2. `cuprins` {"act": "opanaf_3769_2015_d394_baza", "filtru": "depune"}
3. `deschide` {"id": "opanaf_2194_2025_d394#anexa2/pct2"}
4. `cuprins` {"act": "opanaf_2194_2025_d394", "filtru": "aplic"}
5. `deschide` {"id": "opanaf_2194_2025_d394#artII"}
6. `deschide` {"id": "opanaf_2194_2025_d394#anexa2/pct1"}
7. `deschide` {"id": "opanaf_2194_2025_d394#anexa2/pct1/lita"}

Apel: `claude-opus-5`, {'intrare': 14, 'iesire': 3488, 'cache_scriere': 5988, 'cache_citire': 69590} tokeni, $0.1595, 56 s

Pe fond (comparator): **GREȘIT** — faptul principal al cheii (['28.02.2026']) nu e in raspuns; articolul citat [('opanaf_2194_2025', 'pct2')] nu e printre cele ale cheii [('opanaf_3769_2015', 'pct2'), ('cpf', '75')]

Lectura pe fond (de verificat de om): **fond** — Răspunsul dă termenul nominal (28 februarie 2026) și regula corectă (D394 se depune și fără operațiuni), dar nu aplică amânarea pentru zi nelucrătoare: 28.02.2026 cade sâmbătă, termenul efectiv e luni, 02.03.2026 (CPF art. 75 → Codul de procedură civilă). Un contabil care urmează răspunsul depune corect, dar i se spune un termen mai scurt decât cel legal; răspunsul e incomplet pe fond.

## v4 — RĂSPUNS, pe fond GREȘIT

> Da, declarația 394 trebuie depusă și pentru perioada în care nu au fost realizate operațiuni de natura celor care fac obiectul declarației, la organul fiscal competent până în data de 25 inclusiv a lunii următoare încheierii perioadei de raportare (deci, pentru raportarea lunii ianuarie, până pe 25 a lunii următoare).

## Cheia

- Da, se depune și fără operațiuni. Termen nominal 28.02.2026, care cade sâmbătă → termen efectiv luni, 02.03.2026.
- temei: OPANAF 3769/2015 anexa 2 pct. 2 (forma OPANAF 2194/2025); CPF art. 75 (calculul termenelor după Codul de procedură civilă)
