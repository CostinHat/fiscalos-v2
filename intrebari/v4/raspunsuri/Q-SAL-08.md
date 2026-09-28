# Q-SAL-08 — CAPCANA

**Întrebarea:** Boală obișnuită (cod 01): certificat inițial 28–30.09.2026 (3 zile), prelungit fără întrerupere 01–07.10.2026 (7 zile). Septembrie a fost plătit cu 55%. Ce procent se aplică și cum se tratează luna septembrie?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 30.09.2026, pentru un asigurat salariat cu concediu medical pentru boală obișnuită (cod 01) în cadrul aceluiași episod de boală — certificat inițial 28–30.09.2026 (3 zile) urmat, fără întrerupere, de un certificat „în continuare" 01–07.10.2026 (7 zile) —, presupun aplicarea regimului OUG 158/2005 în forma în vigoare la data eliberării certificatului inițial și că baza de calcul este cea stabilită conform art. 10.*

> **Se cumulează zilele din tot episodul de boală (10 zile), deci se aplică procentul de 65% (interval 8–14 zile) pentru întreaga perioadă a episodului, inclusiv pentru certificatul inițial. În consecință, septembrie (plătit inițial cu 55%) se recalculează la 65%, iar diferența de indemnizație rezultată din recalculare se include în veniturile lunii octombrie 2026 (luna în care este determinată) și se declară în declarația privind obligațiile de plată a contribuțiilor sociale, impozitului pe venit și evidența nominală a persoanelor asigurate aferentă lunii octombrie 2026; nu se rectifică declarația lunii septembrie. [calcul: total_zile = zile_initial + zile_prelungire = 10]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul — evaluat de cod, nu de model

- `total_zile = zile_initial + zile_prelungire` → **10**
  - `zile_initial` = 3 — din întrebare: „certificat inițial 28–30.09.2026 (3 zile)”
  - `zile_prelungire` = 7 — din întrebare: „prelungit fără întrerupere 01–07.10.2026 (7 zile)”

- **OUG 158/2005 art. 17 alin. (1) lit. b)** — `oug_158_2005_consolidat#art17/alin1/litb` · valabil din nedovedit
  > prin aplicarea procentului de 65% asupra bazei de calcul stabilite conform art. 10 pentru certificatele de concediu medical eliberate pentru o perioadă cuprinsă între 8 și 14 zile de incapacitate temporară de muncă; ...
- **OMS 15/2018 art. I** — `oms_15_2018_modificare_2025#artI` · valabil din nedovedit
  > Pe parcursul unui episod de boală, numărul de zile rezultat din certificatul de concediu medical inițial se adună cu numărul de zile rezultat din certificatul/certificatele de concediu medical acordat/acordate în continuare, iar în funcție de numărul de zile total rezultat se aplică asupra bazei de calcul procentul corespunzător pentru zilele aferente întregului episod de boală.
- **OMS 15/2018 art. I** — `oms_15_2018_modificare_2025#artI` · valabil din nedovedit
  > certificatul de concediu medical inițial se acordă la sfârșitul lunii și acesta este urmat de un certificat de concediu medical în continuare în luna următoare care conduce la majorarea numărului de zile aferent aceluiași episodul de boală și, implicit, la majorarea procentului aplicat asupra bazei de calcul, indemnizația pentru concediu medical se recalculează.
- **OUG 158/2005 art. 17 alin. (1^2)** — `oug_158_2005_consolidat#art17/alin1^2` · valabil din 2026-07-01
  > diferențele de indemnizații pentru incapacitate temporară de muncă cauzată de boli obișnuite sau de accidente în afara muncii, rezultate ca urmare a recalculării și aferente lunii anterioare celei în care are loc această operațiune, se includ în veniturile lunii în care sunt determinate și se declară în Declarația privind obligațiile de plată a contribuțiilor sociale, impozitului pe venit și evidența nominală a persoanelor asigurate
- **OUG 158/2005 art. 17 alin. (1)** — `oug_158_2005_consolidat#art17/alin1` · valabil din nedovedit
  > prin aplicarea procentului de 55% asupra bazei de calcul stabilite conform art. 10 pentru certificatele de concediu medical eliberate pentru o perioadă de până la 7 zile de incapacitate temporară de muncă; ...
- derogare tratată: `legea_141_2025_consolidat#artXI/alin1` — Regula tranzitorie (pentru episoadele al căror certificat inițial a fost eliberat înainte de intrarea în vigoare a art. IX din Legea 141/2025) nu se aplică: certificatul inițial din speță este eliberat la 28.09.2026, ulterior acelei date, deci se aplică procentele din art. 17 alin. (1) în forma actu…
- derogare tratată: `oug_158_2005_consolidat#art17/alin1^1` — Nu se aplică: procentul special de 75% vizează bolile cardiovasculare stabilite conform art. 13 alin. (3) lit. a), iar cazul este boală obișnuită (cod 01).

### Navigarea (7 pași, 5 ture)

1. `cauta` {"interogare": "indemnizatie incapacitate temporara de munca 55% boala obisnuita procent"}
2. `cauta` {"interogare": "prelungirea certificatului de concediu medical recalculare procent"}
3. `deschide` {"id": "oug_158_2005_consolidat#art17/alin1^2"}
4. `deschide` {"id": "oug_158_2005_consolidat#art17/alin1"}
5. `deschide` {"id": "oug_158_2005_consolidat#art17"}
6. `deschide` {"id": "legea_141_2025_consolidat#artXI/alin1"}
7. `deschide` {"id": "oms_15_2018_modificare_2025#artI"}

Apel: `claude-opus-5`, {'intrare': 10, 'iesire': 4530, 'cache_scriere': 6962, 'cache_citire': 44364} tokeni, $0.1790, 65 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Stratul semantic v3 (context dat de căutare) — RĂSPUNS, pe fond GREȘIT

> Se aplică procentul de 65%, corespunzător perioadei cuprinse între 8 și 14 zile, deoarece zilele certificatului inițial se adună cu zilele certificatului eliberat în continuare în cadrul aceluiași episod de boală. Procentul rezultat se aplică zilelor aferente întregului episod, deci și zilelor din septembrie: luna septembrie, plătită cu 55%, se recalculează la 65%.

## Cheia

- Procentul se stabilește pe episodul de boală (10 zile) → 65% pentru tot episodul, inclusiv zilele din septembrie; diferența 55%→65% pentru septembrie se recalculează, se include în veniturile lunii octombrie 2026 și se declară în D112 pentru octombrie
- temei: OUG 158/2005 art. 17 alin. (1) partea introductivă („raportat la fiecare episod de boală”) și lit. b); art. 17 alin. (1^2) (introdus de OUG 89/2025 art. VII)
