# Q-SAL-04 — CALCUL

**Întrebarea:** Septembrie 2026: salariat cu normă întreagă, funcția de bază, salariu de bază din CIM = 4.325 lei, plus spor de 200 lei, fără alte venituri. Se aplică facilitatea pentru salariul minim? Dacă da, care sunt baza și valoarea CAS și CASS (înainte de rotunjire)?

## Stratul de navigare (v4) — NU POT RĂSPUNDE

*La data de referință 30.09.2026, pentru un salariat cu contract individual de muncă cu normă întreagă, la funcția de bază, cu salariu de bază din CIM de 4.325 lei plus un spor de 200 lei, fără alte venituri, presupun regim salarial standard (fără sectoare privilegiate - construcții, agricol, IT) și verificarea facilității de scutire a unei sume lunare pentru salariul minim.*

Motiv: modelul s-a abţinut: Atomii găsiți conțin facilitatea (scutirea unei sume lunare din baza de impozit și contribuții pentru salariații cu salariul de bază egal cu salariul minim) doar pentru anul 2024 (OUG 115/2023, 200 lei) și pentru anul 2025 (OUG 156/2024), nu și pentru veniturile aferente lunii septembrie 2026; nu am identificat niciun atom în vigoare care să o prelungească pentru 2026. În plus, stabilirea bazei și a valorii CAS/CASS ar presupune un calcul (aplicarea unor cote asupra câștigului brut) ale cărui rezultate nu apar literal în niciun atom pe care l-am deschis, iar cotele de CAS/CASS nu au fost confirmate dintr-un atom.

- **OUG 115/2023 art. LXXIII alin. (1)** — `oug_115_2023_consolidat#artLXXIII/alin1` · valabil din 2024-01-01
  > începând cu data de 1 ianuarie 2024, în cazul salariaților care desfășoară activitate în baza contractului individual de muncă, încadrați cu normă întreagă, la locul unde se află funcția de bază, nu se datorează impozit pe venit și nu se cuprinde în baza lunară de calcul al contribuțiilor sociale obligatorii suma de 200 lei/lună
- **OUG 156/2024 art. LXVI alin. (1)** — `oug_156_2024#artLXVI/alin1` · valabil din 2025-01-01
  > din Legea nr. 227/2015, cu modificările şi completările ulterioare, începând cu data de 1 ianuarie 2025
- **HG 146/2026 art. 1** — `hg_146_2026_salariu_minim#art1` · valabil din 2026-07-01
  > Începând cu data de 1 iulie 2026, salariul de bază minim brut pe țară garantat în plată, prevăzut la art. 164 alin. (1) din Legea nr. 53/2003 - Codul muncii, republicată , cu modificările și completările ulterioare, se stabilește în bani, fără a include sporuri și alte adaosuri, la suma de 4.325 lei lunar
- derogare tratată: `oug_115_2023_consolidat#artLXXIII/alin1` — Derogare de la art. 78, art. 139 alin. (1), art. 140, art. 157 alin. (1) și art. 220^4 din Codul fiscal, dar textul o instituie pentru suma de 200 lei/lună începând cu 1 ianuarie 2024; nu am identificat un atom care să o extindă asupra veniturilor aferente lunii septembrie 2026, deci nu o pot aplica…
- derogare tratată: `oug_156_2024#artLXVI/alin1` — Derogare similară, dar instituită expres începând cu data de 1 ianuarie 2025; textul nu acoperă anul 2026, deci nu se poate aplica lunii septembrie 2026.

### Navigarea (12 pași, 7 ture)

1. `cauta` {"interogare": "suma de 300 lei/lună nu se cuprinde în baza de calcul salariul de bază brut egal cu salariul minim"}
2. `cauta` {"interogare": "salariul de bază minim brut pe țară garantat în plată 2026"}
3. `deschide` {"id": "oug_89_2025#artXXXVI/alin10"}
4. `cuprins` {"act": "hg_146_2026_salariu_minim", "filtru": ""}
5. `deschide` {"id": "oug_89_2025#artXXXVI"}
6. `cuprins` {"act": "hg_146_2026_salariu_minim", "filtru": "salariu"}
7. `cauta` {"interogare": "nu se cuprinde în baza lunară de calcul al contribuțiilor sociale obligatorii suma de 300 lei/lună salariu de bază brut lunar fără a include sporuri"}
8. `cauta` {"interogare": "4.325 lei salariul de bază minim brut pe țară garantat în plată"}
9. `deschide` {"id": "oug_115_2023_consolidat#artLXXIII/alin1"}
10. `cauta` {"interogare": "se stabilește salariul de bază minim brut pe țară garantat în plată la suma de lei lunar 2026 fără a include sporuri"}
11. `deschide` {"id": "hg_146_2026_salariu_minim#art1"}
12. `cauta` {"interogare": "începând cu data de 1 ianuarie 2026 nu se datorează impozit pe venit și nu se cuprinde în baza lunară de calcul al contribuțiilor sociale obligatorii suma de 300 lei/lună"}

Apel: `claude-opus-5`, {'intrare': 14, 'iesire': 3953, 'cache_scriere': 12336, 'cache_citire': 74761} tokeni, $0.2134, 67 s

Pe fond: **NU POT** — modelul s-a abţinut: Atomii găsiți conțin facilitatea (scutirea unei sume lunare din baza de impozit și contribuții pentru salariații cu salariul de bază egal cu salariul minim) doar pentru anul 2024

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți nu conțin nicio normă care să stabilească facilitatea pentru salariul minim aplicabilă veniturilor lunii septembrie 2026 (textele existente vizează expres 2024, 2025 și, pentru diminuare, perioada 1 ianuarie-30 iunie 2026), nici nivelul salariului minim brut pe țară în vigoare în septembrie 2026, nici cotele de CAS și CASS. În plus, determinarea bazelor și a valorilor CAS/CASS ar presupune un calcul (însumări și aplicări de cote) care nu apare literal în niciu…

## Cheia

- Da (salariul de bază fără sporuri = salariul minim, iar brutul 4.525 lei ≤ 4.600 lei). Suma exceptată: 200 lei/lună. Baza CAS/CASS = 4.525 − 200 = 4.325 lei; CAS 25% = 1.081,25 lei; CASS 10% = 432,50 lei
- temei: OUG 89/2025 art. III alin. (1) lit. a) și b) (200 lei/lună pentru 01.07–31.12.2026, prag 4.600 lei inclusiv) și alin. (6); HG 146/2026 art. 1 (4.325 lei); Cod fiscal art. 138 lit. a), art. 156
