# Q3-SAL-06 — CALCUL

**Întrebarea:** Septembrie 2026: un salariat are funcția de bază la alt angajator. La SRL-ul nostru are un al doilea CIM, cu timp parțial, cu salariu brut de 5.000 lei, fără alte beneficii, contract activ toată luna. Are 2 copii minori în întreținere, înscriși la școală. Nu plătește cotizație sindicală, pensie facultativă etc. Cât impozit pe venit reținem la SRL-ul nostru?

## NU POT RĂSPUNDE



Motiv: VERIFICAREA MECANICA a respins propunerea modelului: citatul NU e verbatim in atomul cod_fiscal_227_2015_consolidat#art157/alin1

- `cas = brut * cota_cas / 100` = ((5.000 × 25) ÷ 100) = **1.250**
- `cass = brut * cota_cass / 100` = ((5.000 × 10) ÷ 100) = **500**
- `baza_impozabila = brut - cas - cass` = ((5.000 − 1.250) − 500) = **3.250**
- `impozit = baza_impozabila * cota_impozit / 100` = ((3.250 × 10) ÷ 100) = **325**
- **Codul fiscal (Legea 227/2015) art. 78 alin. (2) lit. b)** — `cod_fiscal_227_2015_consolidat#art78/alin2/litb`
  > pentru veniturile obținute în celelalte cazuri, prin aplicarea cotei de 10% asupra bazei de calcul determinate ca diferență între venitul brut și contribuțiile sociale obligatorii aferente unei luni, datorate potrivit legii în România
- **Codul fiscal (Legea 227/2015) art. 77 alin. (1)** — `cod_fiscal_227_2015_consolidat#art77/alin1`
  > au dreptul la deducerea din venitul net lunar din salarii a unei sume sub formă de deducere personală, acordată pentru fiecare lună a perioadei impozabile numai pentru veniturile din salarii la locul unde se află funcția de bază.
- **Codul fiscal (Legea 227/2015) art. 138** — `cod_fiscal_227_2015_consolidat#art138`
  > Cotele de contribuții de asigurări sociale sunt următoarele: a) 25% datorată de către persoanele fizice care au calitatea de angajați sau pentru care există obligația plății contribuției de asigurări sociale, potrivit prezentei legi;
- **Codul fiscal (Legea 227/2015) art. 156** — `cod_fiscal_227_2015_consolidat#art156`
  > Cota de contribuție de asigurări sociale de sănătate este de 10% și se datorează de către persoanele fizice care au calitatea de angajați sau pentru care există obligația plății contribuției de asigurări sociale de sănătate, potrivit prezentei legi.
- **Codul fiscal (Legea 227/2015) art. 139 alin. (1)** — `cod_fiscal_227_2015_consolidat#art139/alin1`
  > Baza lunară de calcul al contribuției de asigurări sociale, în cazul persoanelor fizice care realizează venituri din salarii sau asimilate salariilor, o reprezintă câștigul brut realizat din salarii și venituri asimilate salariilor
- **Codul fiscal (Legea 227/2015) art. 157 alin. (1)** — `cod_fiscal_227_2015_consolidat#art157/alin1`
  > Baza lunară de calcul al contribuției de asigurări sociale de sănătate, în cazul persoanelor fizice care realizează venituri din salarii sau asimilate salariilor, în țară și în străinătate, (...) o reprezintă câștigul brut care include:
- **Codul fiscal (Legea 227/2015) art. 78 alin. (1)** — `cod_fiscal_227_2015_consolidat#art78/alin1`
  > Beneficiarii de venituri din salarii și asimilate salariilor datorează un impozit lunar, final, care se calculează și se reține la sursă de către plătitorii de venituri

Navigare: 12 pași, 9 ture; {'intrare': 18, 'iesire': 4895, 'cache_scriere': 45214, 'cache_citire': 135730} tokeni; $0.4729; 84 s

Cauza (dacă NU POT): verbatim

Pe fond (comparator): **NU POT** — VERIFICAREA MECANICA a respins propunerea modelului: citatul NU e verbatim in atomul cod_fiscal_227_2015_consolidat#art157/alin1

## Cheia

- 325 lei. În afara funcției de bază nu se acordă deducere personală (nici de bază, nici suplimentară pentru copii) — aceasta se acordă numai la locul funcției de bază. Calcul: CAS = 25% × 5.000 = 1.250 lei; CASS = 10% × 5.000 = 500 lei; baza de calcul a impozitului = 5.000 − 1.250 − 500 = 3.250 lei; impozit = 10% × 3.250 = 325 lei. (CAS de 1.250 lei depășește CAS minim aferent salariului minim, deci nu apare diferență suportată de angajator.)
- temei: Cod fiscal art. 78 alin. (2) lit. b); art. 77 alin. (1); art. 77 alin. (2); art. 138 lit. a); art. 156
