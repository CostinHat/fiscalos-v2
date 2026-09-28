# Q-SAL-04 — CALCUL

**Întrebarea:** Septembrie 2026: salariat cu normă întreagă, funcția de bază, salariu de bază din CIM = 4.325 lei, plus spor de 200 lei, fără alte venituri. Se aplică facilitatea pentru salariul minim? Dacă da, care sunt baza și valoarea CAS și CASS (înainte de rotunjire)?

## Stratul semantic (motorul nou) — RĂSPUNS

*La data de referință septembrie 2026, presupun un salariat cu contract individual de muncă cu normă întreagă, la funcția de bază, cu salariu de bază brut lunar din CIM de 4.325 lei și un spor de 200 lei, fără tichete de masă/vouchere de vacanță/indemnizație de hrană și fără alte venituri, și analizez exclusiv facilitatea privind suma neimpozabilă de 300 lei/lună condiționată de plafonul de venit brut.*

> **Nu. Facilitatea de 300 lei/lună nu se aplică, deoarece una dintre condițiile cumulative este ca venitul brut din salarii pentru luna respectivă să nu depășească 4.300 lei inclusiv, iar numai salariul de bază din CIM este de 4.325 lei (la care se adaugă sporul de 200 lei). În plus, salariul de bază nu este la nivelul salariului minim brut pe țară garantat în plată.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 146 alin. (5^6) lit. b)** — `cod_fiscal_227_2015_consolidat#art146/alin5^6/litb` · valabil din nedovedit
  > fără a include contravaloarea tichetelor de masă, voucherelor de vacanță, respectiv indemnizația de hrană, după caz, acordate potrivit legii, în baza aceluiași contract individual de muncă, pentru aceeași lună, nu depășește nivelul de 4.300 lei inclusiv.
- **Codul fiscal (Legea 227/2015) art. 146 alin. (5^6)** — `cod_fiscal_227_2015_consolidat#art146/alin5^6` · valabil din 2025-01-01
  > nu se datorează impozit pe venit și nu se cuprinde în baza lunară de calcul al contribuțiilor sociale obligatorii suma de 300 lei/lună, reprezentând venituri din salarii și asimilate salariilor, dacă sunt îndeplinite cumulativ următoarele condiții:

Apel: `claude-opus-5`, {'intrare': 6504, 'iesire': 3068, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.1100, 43.6 s

Pe fond: **GREȘIT** — faptul principal al cheii (['4.525 lei']) nu e in raspuns; articolul citat [('cf', '146')] nu e printre cele ale cheii [('oug_89_2025', 'III'), ('hg_146_2026', '1'), ('cf', '138'), ('cf', '156')]

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-09-30 (luna, din "septembrie 2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: R-CALC: intrebarea are 2 baze monetare; calculul cere compunerea mai multor reguli, pe care motorul nu o face


Pe fond: **NU POT** — R-CALC: intrebarea are 2 baze monetare; calculul cere compunerea mai multor reguli, pe care motorul nu o face

## Cheia

- răspuns așteptat: Da (salariul de bază fără sporuri = salariul minim, iar brutul 4.525 lei ≤ 4.600 lei). Suma exceptată: 200 lei/lună. Baza CAS/CASS = 4.525 − 200 = 4.325 lei; CAS 25% = 1.081,25 lei; CASS 10% = 432,50 lei
- temei așteptat: OUG 89/2025 art. III alin. (1) lit. a) și b) (200 lei/lună pentru 01.07–31.12.2026, prag 4.600 lei inclusiv) și alin. (6); HG 146/2026 art. 1 (4.325 lei); Cod fiscal art. 138 lit. a), art. 156

