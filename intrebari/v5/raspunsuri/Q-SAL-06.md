# Q-SAL-06 — CAPCANA

**Întrebarea:** Septembrie 2026: salariat cu CIM cu timp parțial 4 h/zi, singurul contract, nu e elev/student, ucenic, persoană cu dizabilități sau pensionar, salariu brut 2.162,50 lei, contract activ toată luna. Cât este CAS datorat? (înainte de rotunjire)

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 30.09.2026, pentru un salariat cu contract individual de muncă cu timp parțial (4 h/zi), unic contract la funcția de bază, activ toată luna, care nu se află în niciuna dintre situațiile de excepție (elev/student, ucenic, persoană cu dizabilități, pensionar, mai multe contracte), presupun venit brut lunar de 2.162,50 lei impozabil în România și condiții normale de muncă.*

Datele din întrebare: 2026-09-30 · data de referință aleasă: **2026-09-30** — Faptul întrebat este CAS aferent veniturilor lunii septembrie 2026, singura dată din întrebare; salariul minim și derogarea aplicabilă se raportează la luna pentru care se datorează contribuția.

> **CAS datorat pentru septembrie 2026 este 1.031,25 lei (înainte de rotunjire), pentru că nivelul minim al CAS, calculat asupra salariului minim brut în vigoare diminuat conform derogării aplicabile semestrului II 2026, depășește CAS calculat asupra salariului brut de 2.162,50 lei.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul, pas cu pas — evaluat de cod, nu de model

- `CAS_pe_brut = cota_CAS * salariu_brut` = (25% × 2.162,50) = **540,62**
  - `cota_CAS` = 25% — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art138`: „a) 25% datorată de către persoanele fizice care au calitatea de angajați”
  - `salariu_brut` = 2.162,50 — FAPT_CAZ (din întrebare): „salariu brut 2.162,50 lei, contract activ toată luna”
- `baza_minima = salariu_minim - diminuare` = (4.325 − 200) = **4.125**
  - `salariu_minim` = 4.325 — VALOARE_LEGALA din `hg_146_2026_salariu_minim#art1`: „se stabilește în bani, fără a include sporuri și alte adaosuri, la suma de 4.325 lei lunar”
  - `diminuare` = 200 — VALOARE_LEGALA din `oug_89_2025#artIII~2/alin5/litb`: „pentru veniturile aferente perioadei 1 iulie-31 decembrie 2026, cu suma de 200 lei lunar.”
- `CAS_minim = cota_CAS * baza_minima` = (25% × 4.125) = **1.031,25**
  - `cota_CAS` = 25% — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art138`: „a) 25% datorată de către persoanele fizice care au calitatea de angajați”
- `CAS = max(CAS_pe_brut, CAS_minim)` = max(540,62, 1.031,25) = **1.031,25**

- **Codul fiscal (Legea 227/2015) art. 146 alin. (5^6)** — `cod_fiscal_227_2015_consolidat#art146/alin5^6` · valabil din 2025-01-01
  > Contribuția de asigurări sociale datorată de către persoanele fizice care obțin venituri din salarii sau asimilate salariilor, în baza unui contract individual de muncă cu normă întreagă sau cu timp parțial, calculată potrivit alin. (5) , nu poate fi mai mică decât nivelul contribuției de asigurări sociale calculate prin aplicarea cotei prevăzute la art. 138 lit. a) asupra salariului de bază minim brut pe țară
- **OUG 89/2025 art. III alin. (5)** — `oug_89_2025#artIII~2/alin5` · valabil din nedovedit
  > Prin derogare de la prevederile art. 146 alin. (5^6) și ale art. 168 alin. (6^1) din Legea nr. 227/2015 , cu modificările și completările ulterioare, nivelul salariului de bază minim brut pe țară garantat în plată în vigoare în luna pentru care se aplică prevederile art. 146 alin. (5^6 )-( 5^9)
- **OUG 89/2025 art. III alin. (5) lit. b)** — `oug_89_2025#artIII~2/alin5/litb` · valabil din nedovedit
  > pentru veniturile aferente perioadei 1 iulie-31 decembrie 2026, cu suma de 200 lei lunar.
- **HG 146/2026 art. 1** — `hg_146_2026_salariu_minim#art1` · valabil din 2026-07-01
  > Începând cu data de 1 iulie 2026, salariul de bază minim brut pe țară garantat în plată, prevăzut la art. 164 alin. (1) din Legea nr. 53/2003 - Codul muncii, republicată , cu modificările și completările ulterioare, se stabilește în bani, fără a include sporuri și alte adaosuri, la suma de 4.325 lei lunar
- **Codul fiscal (Legea 227/2015) art. 138** — `cod_fiscal_227_2015_consolidat#art138` · valabil din 2018-01-01
  > Cotele de contribuții de asigurări sociale sunt următoarele: a) 25% datorată de către persoanele fizice care au calitatea de angajați sau pentru care există obligația plății contribuției de asigurări sociale, potrivit prezentei legi;
- **Codul fiscal (Legea 227/2015) art. 146 alin. (5^7)** — `cod_fiscal_227_2015_consolidat#art146/alin5^7` · valabil din nedovedit
  > Prevederile alin. (5^6) nu se aplică în cazul persoanelor fizice aflate în una dintre următoarele situații:
- derogare tratată: `oug_89_2025#artIII~2/alin5` — Se aplică: pentru veniturile aferente perioadei 1 iulie-31 decembrie 2026 (deci și septembrie 2026), salariul de bază minim brut folosit la aplicarea art. 146 alin. (5^6) se diminuează cu 200 lei lunar; am folosit nivelul diminuat în calculul CAS minim.
- derogare tratată: `oug_115_2023_consolidat#artLXXIII/alin5` — Nu se aplică: diminuarea cu 200 lei prevăzută de acest text vizează exclusiv veniturile aferente anului 2024, iar faptul întrebat este luna septembrie 2026.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art146/alin5^7` — Excepțiile de la regula CAS minim (elev/student până la 26 ani, ucenic sub 18 ani, persoană cu dizabilități, pensionar pentru limită de vârstă, mai multe contracte în aceeași lună) nu se aplică, întrebarea precizând expres că salariatul nu se află în niciuna dintre aceste situații.

### Navigarea (12 pași, 9 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "contribuției de asigurări sociale"}
2. `cauta` {"interogare": "contribuția de asigurări sociale nu poate fi mai mică decât nivelul salariului minim brut contract cu timp parțial"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art146/alin5^6"}
4. `deschide` {"id": "oug_89_2025#artIII~2/alin5"}
5. `cuprins` {"act": "hg_146_2026_salariu_minim", "filtru": "salariul de bază minim brut"}
6. `cuprins` {"act": "hg_146_2026_salariu_minim", "filtru": ""}
7. `deschide` {"id": "oug_89_2025#artIII~2/alin5/litb"}
8. `cauta` {"interogare": "salariul de bază minim brut pe țară garantat în plată se stabilește în bani 2026 lei lunar"}
9. `deschide` {"id": "hg_146_2026_salariu_minim#art1"}
10. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art138"}
11. `deschide` {"id": "oug_115_2023_consolidat#artLXXIII/alin5"}
12. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art146/alin5^7"}

Apel: `claude-opus-5`, {'intrare': 18, 'iesire': 6359, 'cache_scriere': 13281, 'cache_citire': 127236} tokeni, $0.3057, 98 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond GREȘIT

> CAS datorat (înainte de rotunjire) = 1.031,25 lei, întrucât CAS calculat asupra salariului brut este sub nivelul minim aferent salariului minim brut diminuat. [calcul: baza_minima = salariu_minim - diminuare = 4.125; cas_calculat = cota * salariu_brut = 540,62; cas_minim = cota * baza_minima = 1.031,25; cas_datorat = max(cas_calculat, cas_minim) = 1.031,25]

## Cheia

- Nu 25% × 2.162,50 = 540,63 lei, ci minimul: 25% × (4.325 − 200) = 1.031,25 lei; diferența de 490,63 lei o suportă angajatorul în numele salariatului (analog CASS: minim 10% × 4.125 = 412,50 lei)
- temei: Cod fiscal art. 146 alin. (5^6), (5^7), (5^9); art. 168 alin. (6^1) (CASS, aplicare corespunzătoare); OUG 89/2025 art. III alin. (5) lit. b) (salariul minim diminuat cu 200 lei pentru 01.07–31.12.2026); HG 146/2026 art. 1
