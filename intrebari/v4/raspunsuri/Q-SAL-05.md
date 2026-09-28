# Q-SAL-05 — CAPCANA

**Întrebarea:** Octombrie 2026: salariat cu normă întreagă, funcția de bază, salariu de bază = salariul minim 4.325 lei, fără sporuri, primește și tichete de masă de 800 lei. Total 5.125 lei depășește 4.600 lei — pierde facilitatea de 200 lei?

## Stratul de navigare (v4) — NU POT RĂSPUNDE

*La data de referință 31.10.2026, pentru un salariat cu contract individual de muncă cu normă întreagă, la locul unde se află funcția de bază, cu salariu de bază la nivelul salariului minim și tichete de masă de 800 lei; presupun că se are în vedere facilitatea fiscală lunară de tip „sumă scutită de impozit și contribuții" pentru salariul minim.*

Motiv: modelul s-a abţinut: Singura normă găsită în corpus care reglementează această facilitate este OUG 156/2024 art. LXVI, cu o sumă neimpozabilă de 300 lei/lună și un plafon de 4.300 lei, aplicabile începând cu 1 ianuarie 2025. Nu am identificat în atomii deschiși norma care ar institui, pentru luna octombrie 2026, facilitatea de 200 lei/lună și plafonul de 4.600 lei invocate în întrebare, astfel încât nu pot confirma nici valorile, nici modul de verificare a plafonului (inclusiv excluderea tichetelor de masă) pentru 2026. Un răspuns pe fond ar presupune aplicarea prin analogie a unei norme cu alte valori, ceea ce nu este permis.

- **OUG 156/2024 art. LXVI alin. (1) lit. b)** — `oug_156_2024#artLXVI/alin1/litb` · valabil din nedovedit
  > venitul brut realizat din salarii şi asimilate salariilor, astfel cum este definit la art. 76 alin. (1) - (3) din Legea nr. 227/2015, cu modificările şi completările ulterioare, fără a include contravaloarea tichetelor de masă, voucherelor de vacanţă, respectiv indemnizaţia de hrană, după caz, acordate potrivit legii, în baza aceluiaşi contract individual de muncă, pentru aceeaşi lună, nu depăşeşte nivelul de 4.300 lei inclusiv.
- **OUG 156/2024 art. LXVI alin. (1)** — `oug_156_2024#artLXVI/alin1` · valabil din 2025-01-01
  > începând cu data de 1 ianuarie 2025, în cazul salariaţilor care desfăşoară activitate în baza contractului individual de muncă, încadraţi cu normă întreagă, la locul unde se află funcţia de bază, nu se datorează impozit pe venit şi nu se cuprinde în baza lunară de calcul al contribuţiilor sociale obligatorii suma de 300 lei/lună
- derogare tratată: `oug_156_2024#artLXVI/alin1` — Atomul este el însuși o derogare de la art. 78, art. 139 alin. (1), art. 140, art. 157 alin. (1) și art. 220^4 alin. (1) din Codul fiscal; nu a fost însă folosit ca temei al unui răspuns pe fond, întrucât valorile lui (300 lei/lună, plafon 4.300 lei, aplicabile de la 1 ianuarie 2025) nu corespund ce…

### Navigarea (11 pași, 8 ture)

1. `cauta` {"interogare": "200 lei nu se cuprind in baza de calcul salariu minim brut 4.600 lei"}
2. `cauta` {"interogare": "suma de 300 lei/luna nu se cuprinde in baza lunara de calcul salariu de baza minim brut"}
3. `cauta` {"interogare": "4.600 lei inclusiv venituri brute din salarii facilitate 200 lei"}
4. `cauta` {"interogare": "prin derogare incepand cu 1 ianuarie 2026 suma de 200 lei/luna reprezentand venituri din salarii nu se cuprinde in baza de calcul"}
5. `deschide` {"id": "oug_156_2024#artLXVI/alin1"}
6. `cauta` {"interogare": "1 ianuarie 2026 salariul de bază minim brut pe țară garantat în plată 4.325 lei facilitate impozit"}
7. `deschide` {"id": "oug_89_2025#artXXXVI"}
8. `cauta` {"interogare": "nu se datorează impozit pe venit și nu se cuprinde în baza lunară de calcul al contribuțiilor sociale obligatorii suma de 200 lei/lună"}
9. `cuprins` {"act": "oug_89_2025", "filtru": "salari"}
10. `cauta` {"interogare": "venitul brut realizat din salarii nu depășește nivelul de 4.600 lei inclusiv"}
11. `deschide` {"id": "oug_156_2024#artLXVI/alin1/litb"}

Apel: `claude-opus-5`, {'intrare': 16, 'iesire': 4093, 'cache_scriere': 13647, 'cache_citire': 101946} tokeni, $0.2387, 71 s

Pe fond: **NU POT** — modelul s-a abţinut: Singura normă găsită în corpus care reglementează această facilitate este OUG 156/2024 art. LXVI, cu o sumă neimpozabilă de 300 lei/lună și un plafon de 4.300 lei, aplicabile înce

## Stratul semantic v3 (context dat de căutare) — RĂSPUNS, pe fond CORECT

> Nu, nu pierde facilitatea. Plafonul de 4.600 lei inclusiv (valabil 1 iulie 2026-31 decembrie 2026) se verifică la venitul brut din salarii și asimilate salariilor fără a include contravaloarea tichetelor de masă, deci tichetele de 800 lei nu se adună la plafon. Cum salariul de bază este egal cu salariul minim și venitul brut salarial (fără tichete) se încadrează în plafon, se aplică suma netaxabilă de 200 lei/lună pentru octombrie 2026.

## Cheia

- Nu, facilitatea se aplică: la verificarea pragului de 4.600 lei nu se include contravaloarea tichetelor de masă (nici vouchere de vacanță / indemnizație de hrană); venitul relevant este 4.325 lei ≤ 4.600 lei
- temei: OUG 89/2025 art. III alin. (1) lit. b) („fără a include contravaloarea tichetelor de masă, voucherelor de vacanță, respectiv indemnizația de hrană”)
