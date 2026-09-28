# Q-SAL-05 — CAPCANA

**Întrebarea:** Octombrie 2026: salariat cu normă întreagă, funcția de bază, salariu de bază = salariul minim 4.325 lei, fără sporuri, primește și tichete de masă de 800 lei. Total 5.125 lei depășește 4.600 lei — pierde facilitatea de 200 lei?

## Stratul semantic (motorul nou) — RĂSPUNS

*La 31 octombrie 2026, presupun un salariat cu contract individual de muncă cu normă întreagă, la funcția de bază, al cărui salariu de bază brut lunar (4.325 lei, fără sporuri și adaosuri) este egal cu salariul minim brut pe țară în vigoare în luna octombrie 2026, care primește suplimentar tichete de masă de 800 lei acordate potrivit legii, și presupun că celelalte condiții legale sunt îndeplinite.*

> **Nu. Contravaloarea tichetelor de masă nu se include în venitul brut care se compară cu plafonul de 4.600 lei aplicabil în perioada 1 iulie-31 decembrie 2026. Se ia în calcul doar venitul brut din salarii fără tichete, adică 4.325 lei, care nu depășește 4.600 lei, așa că facilitatea de 200 lei/lună neimpozabilă și neinclusă în baza contribuțiilor se păstrează pentru octombrie 2026.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **OUG 89/2025 art. III alin. (1) lit. b)** — `oug_89_2025#artIII~2/alin1/litb` · valabil din nedovedit
  > contravaloarea tichetelor de masă, voucherelor de vacanță, respectiv indemnizația de hrană, după caz, acordate potrivit legii, în baza aceluiași contract individual de muncă, pentru aceeași lună, nu depășește nivelul de 4.300 lei inclusiv în perioada cuprinsă între 1 ianuarie 2026-30 iunie 2026, respectiv nivelul de 4.600 lei inclusiv în perioada cuprinsă între 1 iulie 2026-31 decembrie 2026.
- **OUG 89/2025 art. III alin. (1)** — `oug_89_2025#artIII~2/alin1` · valabil din nedovedit
  > la locul unde se află funcția de bază, pentru suma de 300 lei/lună din veniturile din salarii și asimilate salariilor aferente perioadei 1 ianuarie-30 iunie 2026, respectiv pentru suma de 200 lei/lună, din veniturile din salarii și asimilate salariilor aferente perioadei 1 iulie-31 decembrie 2026, nu se datorează impozit pe venit și contribuții sociale obligatorii

Apel: `claude-opus-5`, {'intrare': 8021, 'iesire': 4029, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.1416, 47.2 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-10-31 (luna, din "octombrie 2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: D15: intrebarea cere o JUDECATA (Da/Nu) - aplicarea unei reguli la faptele date. Motorul nu compune si nu aplica reguli; atasez regula cea mai bine potrivita, ca material, nu ca raspuns.


Pe fond: **NU POT** — D15: intrebarea cere o JUDECATA (Da/Nu) - aplicarea unei reguli la faptele date. Motorul nu compune si nu aplica reguli; atasez regula cea mai bine potrivita, ca material, nu ca raspuns.

## Cheia

- răspuns așteptat: Nu, facilitatea se aplică: la verificarea pragului de 4.600 lei nu se include contravaloarea tichetelor de masă (nici vouchere de vacanță / indemnizație de hrană); venitul relevant este 4.325 lei ≤ 4.600 lei
- temei așteptat: OUG 89/2025 art. III alin. (1) lit. b) („fără a include contravaloarea tichetelor de masă, voucherelor de vacanță, respectiv indemnizația de hrană”)

