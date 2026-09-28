# Q-SAL-04 — CALCUL

**Întrebarea:** Septembrie 2026: salariat cu normă întreagă, funcția de bază, salariu de bază din CIM = 4.325 lei, plus spor de 200 lei, fără alte venituri. Se aplică facilitatea pentru salariul minim? Dacă da, care sunt baza și valoarea CAS și CASS (înainte de rotunjire)?

## Stratul semantic — NU POT RĂSPUNDE

*Presupun, la data de referință 30 septembrie 2026, un salariat persoană fizică rezidentă cu contract individual de muncă cu normă întreagă la locul unde se află funcția de bază, venit brut lunar format din salariu de bază 4.325 lei plus spor 200 lei, fără alte venituri și fără alte contracte de muncă.*

Motiv: modelul s-a abţinut: Atomii primiți nu conțin nicio normă care să stabilească facilitatea pentru salariul minim aplicabilă veniturilor lunii septembrie 2026 (textele existente vizează expres 2024, 2025 și, pentru diminuare, perioada 1 ianuarie-30 iunie 2026), nici nivelul salariului minim brut pe țară în vigoare în septembrie 2026, nici cotele de CAS și CASS. În plus, determinarea bazelor și a valorilor CAS/CASS ar presupune un calcul (însumări și aplicări de cote) care nu apare literal în niciun atom.

- **OUG 115/2023 art. LXXIII alin. (1) lit. b)** — `oug_115_2023_consolidat#artLXXIII/alin1/litb` · valabil din nedovedit
  > venitul brut realizat din salarii și asimilate salariilor, astfel cum este definit la art. 76 alin. (1)-(3) din Legea nr. 227/2015 , cu modificările și completările ulterioare, în baza aceluiași contract individual de muncă, pentru aceeași lună, nu depășește nivelul de 4.000 lei inclusiv.
- **Codul fiscal (Legea 227/2015) art. 146 alin. (5^6)** — `cod_fiscal_227_2015_consolidat#art146/alin5^6` · valabil din 2025-01-01
  > nu poate fi mai mică decât nivelul contribuției de asigurări sociale calculate prin aplicarea cotei prevăzute la art. 138 lit. a) asupra salariului de bază minim brut pe țară în vigoare în luna pentru care se datorează contribuția de asigurări sociale
- derogare tratată: `cod_fiscal_227_2015_consolidat#art146/alin5^6` — Derogările prezente în context (art. LXVI alin. (5) din Codul fiscal și art. LXXIII alin. (5) din OUG 115/2023) privesc doar veniturile aferente anilor 2025, respectiv 2024, deci nu luna septembrie 2026; derogarea din OUG 89/2025 art. III alin. (5) acoperă expres, în fragmentul primit, doar perioada…
- derogare tratată: `oug_115_2023_consolidat#artLXXIII/alin1` — Facilitatea din OUG 115/2023 se aplică începând cu 1 ianuarie 2024, iar cea din art. LXVI alin. (1) din Codul fiscal începând cu 1 ianuarie 2025; niciun atom primit nu stabilește regimul aplicabil veniturilor lunii septembrie 2026.

Apel: `claude-opus-5`, {'intrare': 9123, 'iesire': 2345, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.1052

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți nu conțin nicio normă care să stabilească facilitatea pentru salariul minim aplicabilă veniturilor lunii septembrie 2026 (textele existente vizează expres 2024, 202

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-09-30 (luna, din "septembrie 2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: R-CALC: intrebarea are 2 baze monetare; calculul cere compunerea mai multor reguli, pe care motorul nu o face


Pe fond: **NU POT** — R-CALC: intrebarea are 2 baze monetare; calculul cere compunerea mai multor reguli, pe care motorul nu o face

## Cheia

- Da (salariul de bază fără sporuri = salariul minim, iar brutul 4.525 lei ≤ 4.600 lei). Suma exceptată: 200 lei/lună. Baza CAS/CASS = 4.525 − 200 = 4.325 lei; CAS 25% = 1.081,25 lei; CASS 10% = 432,50 lei
- temei: OUG 89/2025 art. III alin. (1) lit. a) și b) (200 lei/lună pentru 01.07–31.12.2026, prag 4.600 lei inclusiv) și alin. (6); HG 146/2026 art. 1 (4.325 lei); Cod fiscal art. 138 lit. a), art. 156
