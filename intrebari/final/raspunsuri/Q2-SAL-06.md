# Q2-SAL-06 — CALCUL

**Întrebarea:** Iunie 2026: o SRL plătește pentru copilul unui salariat taxa de grădiniță/creșă (unitate de educație timpurie) de 1.800 lei pe lună, conform regulamentului intern. Salariul de bază al angajatului este 4.500 lei. Este singurul părinte care primește suma, la un singur angajator, și nu primește alte avantaje din categoria art. 76 alin. (4^1). Ce sumă din cei 1.800 lei este neimpozabilă și ce sumă se include în venitul din salarii în iunie 2026?

## Răspunsul — RĂSPUNS

*La data de referință 30.06.2026, pentru o SRL angajator care suportă, conform regulamentului intern, taxa la o unitate de educație timpurie (grădiniță/creșă) pentru copilul unui salariat cu salariu de bază 4.500 lei/lună, presupun salariat cu contract individual de muncă cu timp normal, suma acordată unui singur părinte la un singur angajator (cu declarație pe propria răspundere) și fără alte venituri din categoria art. 76 alin. (4^1) în aceeași lună.*

> **Neimpozabilă este suma de 1.485 lei (plafonul cel mai mic dintre limita de 1.500 lei/lună pe copil și plafonul lunar de 33% din salariul de bază), iar diferența de 315 lei se include în venitul din salarii al lunii iunie 2026 (impozabilă și cu contribuții sociale). [calcul: plafon_33_la_suta = salariu_de_baza * procent_plafon = (4.500 × 33%) = 1.485; suma_neimpozabila = min(min(plafon_33_la_suta, limita_pe_copil), suma_platita) = min(min(1.485, 1.500), 1.800) = 1.485; suma_impozabila = suma_platita - suma_neimpozabila = (1.800 − 1.485) = 315] [data de referință: 30.06.2026 — Faptul întrebat este tratamentul fiscal al sumei acordate în luna iunie 2026, singura dată din întrebare.]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- `plafon_33_la_suta = salariu_de_baza * procent_plafon` = (4.500 × 33%) = **1.485**
- `suma_neimpozabila = min(min(plafon_33_la_suta, limita_pe_copil), suma_platita)` = min(min(1.485, 1.500), 1.800) = **1.485**
- `suma_impozabila = suma_platita - suma_neimpozabila` = (1.800 − 1.485) = **315**
- **Codul fiscal (Legea 227/2015) art. 76 alin. (4^1) lit. i)** — `cod_fiscal_227_2015_consolidat#art76/alin4^1/liti`
  > sumele suportate de către angajator pentru plasarea copiilor angajaților proprii în unități de educație timpurie, potrivit legii, în limita stabilită de acesta, dar nu mai mult de 1.500 lei/lună pentru fiecare copil.
- **Codul fiscal (Legea 227/2015) art. 76 alin. (4^1)** — `cod_fiscal_227_2015_consolidat#art76/alin4^1`
  > Următoarele venituri cumulate lunar nu reprezintă venit impozabil în înțelesul impozitului pe venit, în limita plafonului lunar de cel mult 33% din salariul de bază corespunzător locului de muncă ocupat
- **Codul fiscal (Legea 227/2015) art. 76 alin. (4^2)** — `cod_fiscal_227_2015_consolidat#art76/alin4^2`
  > Ordinea în care veniturile prevăzute la alin. (4^1) se includ în plafonul lunar de cel mult 33% din salariul de bază corespunzător locului de muncă ocupat sau din solda lunară/salariul lunar acordată/acordat potrivit legii se stabilește de angajator.
- **Codul fiscal (Legea 227/2015) art. 76 alin. (12)** — `cod_fiscal_227_2015_consolidat#art76/alin12`
  > Sumele suportate/acordate de către angajator pentru plasarea copiilor angajaților proprii în unități de educație timpurie, potrivit legii, în condițiile alin. (4^1) lit. i)

Navigare: 7 pași; `claude-opus-5`; {'intrare': 12, 'iesire': 4348, 'cache_scriere': 12991, 'cache_citire': 76937} tokeni; $0.2284; 62 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## Cheia

- 315 lei se include în venitul din salarii (impozabil și în baza CAS/CASS); neimpozabil 1.485 lei. Calcul: limita specifică pentru educație timpurie = 1.500 lei/lună/copil, deci din 1.800 lei, maximum 1.500 lei pot fi neimpozabili; aceste sume intră însă în plafonul lunar cumulat de cel mult 33% din salariul de bază: 33% × 4.500 = 1.485 lei < 1.500 lei, deci neimpozabil = 1.485 lei; impozabil = 1.800 − 1.485 = 315 lei. Aceeași limită se aplică pentru excluderea din baza CAS, iar sumele excluse din baza CAS la art. 142 nu intră nici în baza CASS.
- temei: Cod fiscal art. 76 alin. (4^1) lit. i); art. 76 alin. (4^1); art. 142 lit. aa^1) pct. 9; art. 157 alin. (2)
