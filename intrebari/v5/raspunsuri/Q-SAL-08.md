# Q-SAL-08 — CAPCANA

**Întrebarea:** Boală obișnuită (cod 01): certificat inițial 28–30.09.2026 (3 zile), prelungit fără întrerupere 01–07.10.2026 (7 zile). Septembrie a fost plătit cu 55%. Ce procent se aplică și cum se tratează luna septembrie?

## Stratul de navigare v5 — RĂSPUNS

*La data de 07.10.2026, pentru un asigurat aflat în incapacitate temporară de muncă pentru boală obișnuită (cod 01), cu un certificat inițial de 3 zile (28–30.09.2026) urmat fără întrerupere de un certificat „în continuare” de 7 zile (01–07.10.2026) în cadrul aceluiași episod de boală, indemnizația fiind suportată conform OUG 158/2005; presupun că nu există alte certificate în acest episod și că nu e vorba de afecțiunile cu procente speciale.*

Datele din întrebare: 2026-09-30, 2026-10-07 · data de referință aleasă: **2026-10-07** — Faptul întrebat este procentul aplicabil episodului de boală după prelungirea care se încheie la 07.10.2026, moment la care se cumulează zilele și se recalculează luna septembrie.

> **Procentul se stabilește pe total episod de boală: zilele din certificatul inițial se adună cu cele din certificatul în continuare, rezultând 10 zile, adică o perioadă cuprinsă între 8 și 14 zile, deci se aplică procentul de 65% asupra bazei de calcul. Luna septembrie, plătită inițial cu 55% (certificat de până la 7 zile), se recalculează: procentul majorat de 65% se aplică pentru toată perioada episodului de boală, inclusiv pentru indemnizația aferentă certificatului inițial din septembrie.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul, pas cu pas — evaluat de cod, nu de model

- `total_zile = zile_initial + zile_continuare` = (3 + 7) = **10**
  - `zile_initial` = 3 — FAPT_CAZ (din întrebare): „certificat inițial 28–30.09.2026 (3 zile)”
  - `zile_continuare` = 7 — FAPT_CAZ (din întrebare): „prelungit fără întrerupere 01–07.10.2026 (7 zile)”

- **OUG 158/2005 art. 17 alin. (1) lit. b)** — `oug_158_2005_consolidat#art17/alin1/litb` · valabil din nedovedit
  > prin aplicarea procentului de 65% asupra bazei de calcul stabilite conform art. 10 pentru certificatele de concediu medical eliberate pentru o perioadă cuprinsă între 8 și 14 zile de incapacitate temporară de muncă;
- **OMS 15/2018 art. I** — `oms_15_2018_modificare_2025#artI` · valabil din nedovedit
  > Pe parcursul unui episod de boală, numărul de zile rezultat din certificatul de concediu medical inițial se adună cu numărul de zile rezultat din certificatul/certificatele de concediu medical acordat/acordate în continuare, iar în funcție de numărul de zile total rezultat se aplică asupra bazei de calcul procentul corespunzător pentru zilele aferente întregului episod de boală.
- **OMS 15/2018 art. I** — `oms_15_2018_modificare_2025#artI` · valabil din nedovedit
  > urmat de un certificat de concediu medical în continuare în luna următoare care conduce la majorarea numărului de zile aferent aceluiași episodul de boală și, implicit, la majorarea procentului aplicat asupra bazei de calcul, indemnizația pentru concediu medical se recalculează.
- **OUG 158/2005 art. 17 alin. (1)** — `oug_158_2005_consolidat#art17/alin1` · valabil din nedovedit
  > Cuantumul brut lunar al indemnizației pentru incapacitate temporară de muncă cauzată de boli obișnuite sau de accidente în afara muncii se determină raportat la fiecare episod de boală, după cum urmează: a) prin aplicarea procentului de 55% asupra bazei de calcul stabilite conform art. 10 pentru certificatele de concediu medical eliberate pentru o perioadă de până la 7 zile de incapacitate temporară de muncă;

### Navigarea (4 pași, 3 ture)

1. `cauta` {"interogare": "cuantumul indemnizației pentru incapacitate temporară de muncă 55% din baza de calcul"}
2. `cauta` {"interogare": "certificat de concediu medical în continuare prelungire recalculare procent"}
3. `deschide` {"id": "oug_158_2005_consolidat#art17/alin1"}
4. `deschide` {"id": "oms_15_2018_modificare_2025#artI"}

Apel: `claude-opus-5`, {'intrare': 6, 'iesire': 3135, 'cache_scriere': 5124, 'cache_citire': 24513} tokeni, $0.1227, 40 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond CORECT

> Se cumulează zilele din tot episodul de boală (10 zile), deci se aplică procentul de 65% (interval 8–14 zile) pentru întreaga perioadă a episodului, inclusiv pentru certificatul inițial. În consecință, septembrie (plătit inițial cu 55%) se recalculează la 65%, iar diferența de indemnizație rezultată din recalculare se include în veniturile lunii octombrie 2026 (luna în care este determinată) și se declară în declarația privind obligațiile de plată a contribuțiilor sociale, impozitului pe venit ș…

## Cheia

- Procentul se stabilește pe episodul de boală (10 zile) → 65% pentru tot episodul, inclusiv zilele din septembrie; diferența 55%→65% pentru septembrie se recalculează, se include în veniturile lunii octombrie 2026 și se declară în D112 pentru octombrie
- temei: OUG 158/2005 art. 17 alin. (1) partea introductivă („raportat la fiecare episod de boală”) și lit. b); art. 17 alin. (1^2) (introdus de OUG 89/2025 art. VII)
