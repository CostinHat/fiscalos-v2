# Q-SAL-04 — CALCUL

**Întrebarea:** Septembrie 2026: salariat cu normă întreagă, funcția de bază, salariu de bază din CIM = 4.325 lei, plus spor de 200 lei, fără alte venituri. Se aplică facilitatea pentru salariul minim? Dacă da, care sunt baza și valoarea CAS și CASS (înainte de rotunjire)?

## Stratul de navigare v5 — NU POT RĂSPUNDE

*La data de 30.09.2026, pentru un salariat cu contract individual de muncă cu normă întreagă, la locul unde se află funcția de bază, cu salariu de bază din CIM de 4.325 lei și un spor de 200 lei, fără tichete de masă/vouchere de vacanță/indemnizație de hrană și fără alte venituri; presupun că salariul de bază este menținut la nivelul minim pe toată luna septembrie 2026 și că angajatorul nu se află în situația de neîndeplinire a condiției prevăzute la alin. (2).*

Datele din întrebare: 2026-09-30 · data de referință aleasă: **2026-09-30** — Faptul întrebat este tratamentul veniturilor salariale aferente lunii septembrie 2026, singura dată din întrebare.

Motiv: VERIFICAREA CALCULULUI a respins propunerea: operand nenumeric: '200 lei/lună'; calculul baza: nume fara sursa in formula: suma_netaxabila; calculul cas: nume fara sursa in formula: baza; calculul cass: nume fara sursa in formula: baza

### Calculul, pas cu pas — evaluat de cod, nu de model

- `venit_brut = salariu_baza + spor` = (4.325 + 200) = **4.525**
  - `salariu_baza` = 4.325 — FAPT_CAZ (din întrebare): „salariu de bază din CIM = 4.325 lei”
  - `spor` = 200 — FAPT_CAZ (din întrebare): „plus spor de 200 lei”

- **OUG 89/2025 art. III alin. (1)** — `oug_89_2025#artIII~2/alin1` · valabil din nedovedit
  > pentru suma de 300 lei/lună din veniturile din salarii și asimilate salariilor aferente perioadei 1 ianuarie-30 iunie 2026, respectiv pentru suma de 200 lei/lună, din veniturile din salarii și asimilate salariilor aferente perioadei 1 iulie-31 decembrie 2026, nu se datorează impozit pe venit și contribuții sociale obligatorii
- **OUG 89/2025 art. III alin. (1)** — `oug_89_2025#artIII~2/alin1` · valabil din nedovedit
  > nivelul salariului de bază brut lunar stabilit potrivit contractului individual de muncă, fără a include sporuri și alte adaosuri, este egal cu nivelul salariului minim brut pe țară garantat în plată stabilit prin act normativ, în vigoare în luna căreia îi sunt aferente veniturile
- **OUG 89/2025 art. III alin. (1) lit. b)** — `oug_89_2025#artIII~2/alin1/litb` · valabil din nedovedit
  > nu depășește nivelul de 4.300 lei inclusiv în perioada cuprinsă între 1 ianuarie 2026-30 iunie 2026, respectiv nivelul de 4.600 lei inclusiv în perioada cuprinsă între 1 iulie 2026-31 decembrie 2026.
- **HG 146/2026 art. 1** — `hg_146_2026_salariu_minim#art1` · valabil din 2026-07-01
  > Începând cu data de 1 iulie 2026, salariul de bază minim brut pe țară garantat în plată, prevăzut la art. 164 alin. (1) din Legea nr. 53/2003 - Codul muncii, republicată , cu modificările și completările ulterioare, se stabilește în bani, fără a include sporuri și alte adaosuri, la suma de 4.325 lei lunar
- **Codul fiscal (Legea 227/2015) art. 138** — `cod_fiscal_227_2015_consolidat#art138` · valabil din 2018-01-01
  > Cotele de contribuții de asigurări sociale sunt următoarele: a) 25% datorată de către persoanele fizice care au calitatea de angajați sau pentru care există obligația plății contribuției de asigurări sociale, potrivit prezentei legi;
- **Codul fiscal (Legea 227/2015) art. 156** — `cod_fiscal_227_2015_consolidat#art156~2` · valabil din 2021-12-18
  > Cota de contribuție de asigurări sociale de sănătate este de 10% și se datorează de către persoanele fizice care au calitatea de angajați sau pentru care există obligația plății contribuției de asigurări sociale de sănătate, potrivit prezentei legi.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art139/alin1` — OUG 89/2025 art. III alin. (1) derogă expres de la art. 139 alin. (1) și art. 157 alin. (1) din Codul fiscal; derogarea se aplică în cazul dat, astfel că suma de 200 lei/lună aferentă lunii septembrie 2026 se exclude din baza lunară de calcul al CAS și CASS.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art157/alin1` — Idem: baza lunară de calcul al CASS se diminuează cu suma netaxabilă de 200 lei/lună, prin derogarea din OUG 89/2025 art. III alin. (1).

### Navigarea (19 pași, 12 ture)

1. `cauta` {"interogare": "suma de 300 lei/lună nu se cuprinde în baza lunară de calcul al contribuțiilor sociale salariul minim brut"}
2. `cauta` {"interogare": "salariul de bază minim brut pe țară garantat în plată 2026 4.325 lei"}
3. `deschide` {"id": "oug_89_2025#artXXXVI/alin10"}
4. `cuprins` {"act": "hg_146_2026_salariu_minim", "filtru": "salariu"}
5. `deschide` {"id": "oug_89_2025#artXXXVI"}
6. `cuprins` {"act": "hg_146_2026_salariu_minim", "filtru": ""}
7. `cauta` {"interogare": "nu se datorează impozit pe venit pentru suma de 300 lei/lună salariați încadrați cu normă întreagă funcția de bază anul 2026"}
8. `cauta` {"interogare": "salariul de bază minim brut pe țară garantat în plată se stabilește la 4.325 lei lunar"}
9. `deschide` {"id": "oug_89_2025#artIII~2/alin1"}
10. `deschide` {"id": "hg_146_2026_salariu_minim#art1"}
11. `deschide` {"id": "oug_89_2025#artIII~2/alin1/litb"}
12. `deschide` {"id": "oug_89_2025#artIII~2"}
13. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Cotele de contribuții"}
14. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art138"}
15. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art156"}
16. `cauta` {"interogare": "Cota de contribuție de asigurări sociale de sănătate este de 10% asupra bazei de calcul"}
17. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Cota de contribuție de asigurări sociale de sănătate"}
18. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art156~2"}
19. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art155"}

Apel: `claude-opus-5`, {'intrare': 24, 'iesire': 8743, 'cache_scriere': 22870, 'cache_citire': 194395} tokeni, $0.4588, 126 s

Pe fond (comparator): **NU POT** — VERIFICAREA CALCULULUI a respins propunerea: operand nenumeric: '200 lei/lună'; calculul baza: nume fara sursa in formula: suma_netaxabila; calculul cas: nume fara sursa in formula: baza; calculul cas

## v4 — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii găsiți conțin facilitatea (scutirea unei sume lunare din baza de impozit și contribuții pentru salariații cu salariul de bază egal cu salariul minim) doar pentru anul 2024 (OUG 115/2023, 200 lei) și pentru anul 2025 (OUG 156/2024), nu și pentru veniturile aferente lunii septembrie 2026; nu am identificat niciun atom în vigoare care să o prelungească pentru 2026. În plus, stabilirea bazei și a valorii CAS/CASS ar presupune un calcul (aplicarea unor cote asupra câștigul…

## Cheia

- Da (salariul de bază fără sporuri = salariul minim, iar brutul 4.525 lei ≤ 4.600 lei). Suma exceptată: 200 lei/lună. Baza CAS/CASS = 4.525 − 200 = 4.325 lei; CAS 25% = 1.081,25 lei; CASS 10% = 432,50 lei
- temei: OUG 89/2025 art. III alin. (1) lit. a) și b) (200 lei/lună pentru 01.07–31.12.2026, prag 4.600 lei inclusiv) și alin. (6); HG 146/2026 art. 1 (4.325 lei); Cod fiscal art. 138 lit. a), art. 156
