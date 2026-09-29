# Q-SAL-05 — CAPCANA

**Întrebarea:** Octombrie 2026: salariat cu normă întreagă, funcția de bază, salariu de bază = salariul minim 4.325 lei, fără sporuri, primește și tichete de masă de 800 lei. Total 5.125 lei depășește 4.600 lei — pierde facilitatea de 200 lei?

## Stratul de navigare v5 — RĂSPUNS

*La data de 31.10.2026, pentru un salariat cu contract individual de muncă cu normă întreagă, la locul unde se află funcția de bază, cu salariu de bază brut egal cu salariul minim brut pe țară garantat în plată, fără sporuri și adaosuri, care primește și tichete de masă; presupun că salariul de bază nu a fost majorat în sensul condiției care anulează facilitatea și că tichetele sunt acordate potrivit legii.*

Datele din întrebare: 2026-10-31 · data de referință aleasă: **2026-10-31** — Faptul întrebat privește veniturile salariale aferente lunii octombrie 2026, singura dată din întrebare.

> **Nu. Tichetele de masă nu se iau în calcul la verificarea plafonului de 4.600 lei: venitul brut relevant este doar salariul de 4.325 lei, care se încadrează în plafon, astfel că facilitatea de 200 lei/lună (sumă scutită de impozit pe venit și de contribuții sociale obligatorii) se menține pentru octombrie 2026.**

Citatul decisiv (`oug_89_2025#artIII~2/alin1/litb`):
> fără a include contravaloarea tichetelor de masă, voucherelor de vacanță, respectiv indemnizația de hrană, după caz, acordate potrivit legii, în baza aceluiași contract individual de muncă, pentru aceeași lună, nu depășește nivelul de 4.300 lei inclusiv în perioada cuprinsă între 1 ianuarie 2026-30 iunie 2026, respectiv nivelul de 4.600 lei inclusiv în perioada cuprinsă între 1 iulie 2026-31 decembrie 2026.

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **OUG 89/2025 art. III alin. (1) lit. b)** — `oug_89_2025#artIII~2/alin1/litb` · valabil din nedovedit
  > fără a include contravaloarea tichetelor de masă, voucherelor de vacanță, respectiv indemnizația de hrană, după caz, acordate potrivit legii, în baza aceluiași contract individual de muncă, pentru aceeași lună, nu depășește nivelul de 4.300 lei inclusiv în perioada cuprinsă între 1 ianuarie 2026-30 iunie 2026, respectiv nivelul de 4.600 lei inclusiv în perioada cuprinsă între 1 iulie 2026-31 decembrie 2026.
- **OUG 89/2025 art. III alin. (1)** — `oug_89_2025#artIII~2/alin1` · valabil din nedovedit
  > în cazul salariaților care desfășoară activitate în baza contractului individual de muncă, încadrați cu normă întreagă, la locul unde se află funcția de bază, pentru suma de 300 lei/lună din veniturile din salarii și asimilate salariilor aferente perioadei 1 ianuarie-30 iunie 2026, respectiv pentru suma de 200 lei/lună, din veniturile din salarii și asimilate salariilor aferente perioadei 1 iulie-31 decembrie 2026, nu se datorează impozit pe venit și contribuții sociale obligatorii
- **OUG 89/2025 art. III alin. (1)** — `oug_89_2025#artIII~2/alin1` · valabil din nedovedit
  > nivelul salariului de bază brut lunar stabilit potrivit contractului individual de muncă, fără a include sporuri și alte adaosuri, este egal cu nivelul salariului minim brut pe țară garantat în plată stabilit prin act normativ, în vigoare în luna căreia îi sunt aferente veniturile
- derogare tratată: `oug_89_2025#artIII~2/alin1` — Atomul citat este el însuși o derogare de la art. 78, art. 139 alin. (1), art. 140, art. 157 alin. (1) și art. 220^4 alin. (1) din Codul fiscal; ca normă specială pentru anul 2026 se aplică prioritar cazului descris, iar regulile generale de impozitare/contribuții rămân aplicabile restului venitului…

### Navigarea (13 pași, 10 ture)

1. `cauta` {"interogare": "300 lei salariul de bază minim brut nu se cuprind în baza de calcul venit brut 4.300 lei"}
2. `cauta` {"interogare": "facilitate 200 lei salariu minim 2026 impozit contribuții"}
3. `cauta` {"interogare": "nu se datorează impozit pe venit și nu se cuprinde în baza lunară de calcul al contribuțiilor sociale obligatorii suma de 200 lei/lună"}
4. `cuprins` {"act": "oug_8_2026", "filtru": "salari"}
5. `cauta` {"interogare": "4.600 lei venit brut lunar realizat din salarii nu depășește nivelul de 4.600 lei inclusiv"}
6. `cauta` {"interogare": "salariul de bază minim brut pe țară garantat în plată 4.325 lei 2026"}
7. `cuprins` {"act": "oug_89_2025", "filtru": "salari"}
8. `deschide` {"id": "oug_89_2025#artXXXVI/alin10"}
9. `deschide` {"id": "oug_89_2025#artXXXVI"}
10. `cauta` {"interogare": "În perioada 1 ianuarie-31 decembrie 2026 salariați normă întreagă funcția de bază nu se datorează impozit pe venit suma de lei/lună"}
11. `deschide` {"id": "oug_89_2025#artIII~2/alin1"}
12. `deschide` {"id": "oug_89_2025#artIII~2/alin1/litb"}
13. `deschide` {"id": "oug_89_2025#artIII~2"}

Apel: `claude-opus-5`, {'intrare': 20, 'iesire': 3884, 'cache_scriere': 13226, 'cache_citire': 140048} tokeni, $0.2499, 74 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — NU POT, pe fond NU POT

> modelul s-a abţinut: Singura normă găsită în corpus care reglementează această facilitate este OUG 156/2024 art. LXVI, cu o sumă neimpozabilă de 300 lei/lună și un plafon de 4.300 lei, aplicabile începând cu 1 ianuarie 2025. Nu am identificat în atomii deschiși norma care ar institui, pentru luna octombrie 2026, facilitatea de 200 lei/lună și plafonul de 4.600 lei invocate în întrebare, astfel încât nu pot confirma nici valorile, nici modul de verificare a plafonului (inclusiv excluderea tichete…

## Cheia

- Nu, facilitatea se aplică: la verificarea pragului de 4.600 lei nu se include contravaloarea tichetelor de masă (nici vouchere de vacanță / indemnizație de hrană); venitul relevant este 4.325 lei ≤ 4.600 lei
- temei: OUG 89/2025 art. III alin. (1) lit. b) („fără a include contravaloarea tichetelor de masă, voucherelor de vacanță, respectiv indemnizația de hrană”)
