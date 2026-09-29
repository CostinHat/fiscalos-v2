# Q-SAL-03 — CALCUL

**Întrebarea:** Salariat cu normă întreagă la funcția de bază, septembrie 2026, salariu brut 10.000 lei, fără persoane în întreținere, fără copii școlarizați, peste 26 de ani, fără alte deduceri. Calculați CAS, CASS, impozit, net și CAM.

## Stratul de navigare v5 — RĂSPUNS

*La data de 30.09.2026, pentru un salariat cu contract individual de muncă cu normă întreagă, la locul unde se află funcția de bază, cu venit brut lunar de 10.000 lei în septembrie 2026, fără persoane în întreținere, fără copii școlarizați, peste 26 de ani, fără cotizație sindicală, contribuții la pensii facultative/ocupaționale sau alte deduceri; presupun regimul general de impozitare a salariilor (fără facilități sectoriale) și că venitul brut depășește plafonul de acordare a deducerii personale de bază.*

Datele din întrebare: 2026-09-30 · data de referință aleasă: **2026-09-30** — Faptul întrebat este calculul salarial aferent lunii septembrie 2026, singura dată din întrebare.

> **CAS reținut salariatului = 2.500 lei; CASS reținută = 1.000 lei; baza de calcul a impozitului = 6.500 lei (deducerea personală nu se acordă, întrucât venitul brut depășește nivelul salariului minim brut pe țară majorat cu 2.000 de lei); impozit pe salariu = 650 lei; salariu net de plată = 5.850 lei; contribuția asiguratorie pentru muncă datorată de angajator = 225 lei.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul, pas cu pas — evaluat de cod, nu de model

- `CAS = brut * cota_cas` = (10.000 × 25%) = **2.500**
  - `brut` = 10.000 — FAPT_CAZ (din întrebare): „salariu brut 10.000 lei”
  - `cota_cas` = 25% — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art138`: „a) 25% datorată de către persoanele fizice care au calitatea de angajați”
- `CASS = brut * cota_cass` = (10.000 × 10%) = **1.000**
  - `brut` = 10.000 — FAPT_CAZ (din întrebare): „salariu brut 10.000 lei”
  - `cota_cass` = 10% — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art156~2`: „Cota de contribuție de asigurări sociale de sănătate este de 10%”
- `baza_impozit = brut - CAS - CASS` = ((10.000 − 2.500) − 1.000) = **6.500**
  - `brut` = 10.000 — FAPT_CAZ (din întrebare): „salariu brut 10.000 lei”
- `impozit = baza_impozit * cota_impozit` = (6.500 × 10%) = **650**
  - `cota_impozit` = 10% — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art78/alin2/lita`: „prin aplicarea cotei de 10% asupra bazei de calcul”
- `net = brut - CAS - CASS - impozit` = (((10.000 − 2.500) − 1.000) − 650) = **5.850**
  - `brut` = 10.000 — FAPT_CAZ (din întrebare): „salariu brut 10.000 lei”
- `CAM = brut * cota_cam` = (10.000 × 2,25%) = **225**
  - `brut` = 10.000 — FAPT_CAZ (din întrebare): „salariu brut 10.000 lei”
  - `cota_cam` = 2,25% — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art220^3/alin1`: „Cota contribuției asiguratorii pentru muncă este de 2,25%.”

- **Codul fiscal (Legea 227/2015) art. 78 alin. (2) lit. a)** — `cod_fiscal_227_2015_consolidat#art78/alin2/lita` · valabil din 2026-03-01
  > la locul unde se află funcția de bază, prin aplicarea cotei de 10% asupra bazei de calcul determinată ca diferență între venitul net din salarii calculat prin deducerea din venitul brut a contribuțiilor sociale obligatorii aferente unei luni
- **Codul fiscal (Legea 227/2015) art. 138** — `cod_fiscal_227_2015_consolidat#art138` · valabil din 2018-01-01
  > Cotele de contribuții de asigurări sociale sunt următoarele: a) 25% datorată de către persoanele fizice care au calitatea de angajați sau pentru care există obligația plății contribuției de asigurări sociale, potrivit prezentei legi;
- **Codul fiscal (Legea 227/2015) art. 156** — `cod_fiscal_227_2015_consolidat#art156~2` · valabil din 2021-12-18
  > Cota de contribuție de asigurări sociale de sănătate este de 10% și se datorează de către persoanele fizice care au calitatea de angajați sau pentru care există obligația plății contribuției de asigurări sociale de sănătate, potrivit prezentei legi.
- **Codul fiscal (Legea 227/2015) art. 220^3 alin. (1)** — `cod_fiscal_227_2015_consolidat#art220^3/alin1` · valabil din nedovedit
  > Cota contribuției asiguratorii pentru muncă este de 2,25%.
- **Codul fiscal (Legea 227/2015) art. 77 alin. (3)** — `cod_fiscal_227_2015_consolidat#art77/alin3` · valabil din nedovedit
  > Deducerea personală de bază se acordă pentru persoanele fizice care au un venit lunar brut de până la 2.000 de lei peste nivelul salariului de bază minim brut pe țară garantat în plată aprobat prin hotărâre a Guvernului, în vigoare în luna de realizare a venitului.
- **Codul fiscal (Legea 227/2015) art. 139 alin. (1)** — `cod_fiscal_227_2015_consolidat#art139/alin1` · valabil din 2018-01-01
  > Baza lunară de calcul al contribuției de asigurări sociale, în cazul persoanelor fizice care realizează venituri din salarii sau asimilate salariilor, o reprezintă câștigul brut realizat din salarii
- derogare tratată: `oug_89_2025#artIII~2/alin1` — Derogarea de la art. 78, art. 139 alin. (1), art. 140, art. 157 alin. (1) și art. 220^4 alin. (1) (sumă neimpozabilă lunară în 2026) nu se aplică: se acordă numai dacă salariul de bază brut lunar este egal cu salariul minim brut pe țară garantat în plată, or în speță salariul brut este de 10.000 lei…
- derogare tratată: `oug_156_2024#artLXVI/alin1` — Derogare cu același obiect pentru anul 2025, condiționată de încadrarea salariului de bază la nivelul salariului minim brut pe țară; nu privește luna septembrie 2026 și nici un salariu brut de 10.000 lei.
- derogare tratată: `oug_115_2023_consolidat#artLXXIII/alin1` — Derogare cu același obiect pentru anul 2024, condiționată de salariul de bază la nivelul salariului minim brut pe țară; nu se aplică lunii septembrie 2026 și nici unui salariu brut de 10.000 lei.

### Navigarea (19 pași, 12 ture, 1 reîncercare C23)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "cotele de contribuții de asigurări sociale"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "cota de contribuție de asigurări sociale de sănătate"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art138"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art156"}
5. `cauta` {"interogare": "Cota de contribuție de asigurări sociale de sănătate este de 10%"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art64"}
7. `cauta` {"interogare": "Cota de contribuție de asigurări sociale de sănătate Secţiunea a 2-a cota 10% datorată de către persoanele fizice care au calitatea de angajați"}
8. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art220^3"}
9. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Cota de contribuție de asigurări sociale de sănătate"}
10. `cauta` {"interogare": "cota de 10% contribuție asigurări sociale de sănătate salarii baza lunară de calcul câștigul brut"}
11. `cauta` {"interogare": "Articolul 156 Cota contribuției de asigurări sociale de sănătate este de 10%"}
12. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art156~2"}
13. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "deducere personală"}
14. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art77"}
15. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art78"}
16. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art78/alin2"}
17. `deschide` {"id": "oug_89_2025#artIII~2/alin1"}
18. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art78/alin2/lita"}
19. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art77/alin3"}

Apel: `claude-opus-5`, {'intrare': 24, 'iesire': 12369, 'cache_scriere': 34995, 'cache_citire': 256533} tokeni, $0.6563, 161 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — NU POT, pe fond NU POT

> modelul s-a abţinut: Răspunsul cerut presupune atât cote legale (CAS, CASS, impozit, CAM), cât și rezultate obținute prin calcul. Dintre acestea, cota CASS și bazele de calcul (art. 139 alin. (1), art. 157 alin. (1)) nu au putut fi obținute dintr-un atom - atomul art. 156 deschis nu conține cota, iar căutările nu au returnat textul cotei. De asemenea, nu am putut verifica din atomi regimul deducerii personale la acest nivel de venit și nici dacă derogările temporare (OUG 156/2024, OUG 89/2025) s…

## Cheia

- CAS 2.500 lei; CASS 1.000 lei; deducere personală 0 (brut > 4.325 + 2.000 = 6.325 lei); impozit 10% × (10.000 − 3.500) = 650 lei; net 5.850 lei; CAM 2,25% × 10.000 = 225 lei
- temei: Cod fiscal art. 138 lit. a) (CAS 25%); art. 156 (CASS 10%); art. 77 alin. (3) și (4) (fără deducere peste salariul minim + 2.000 lei); art. 78 alin. (2) lit. a) (cota 10%); art. 220^3 alin. (1) (CAM 2,25%); HG 146/2026 art. 1 (salariul minim 4.325 lei de la 01.07.2026)
