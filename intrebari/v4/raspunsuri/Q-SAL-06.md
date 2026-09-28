# Q-SAL-06 — CAPCANA

**Întrebarea:** Septembrie 2026: salariat cu CIM cu timp parțial 4 h/zi, singurul contract, nu e elev/student, ucenic, persoană cu dizabilități sau pensionar, salariu brut 2.162,50 lei, contract activ toată luna. Cât este CAS datorat? (înainte de rotunjire)

## Stratul de navigare (v4) — RĂSPUNS

*La 30.09.2026, pentru un salariat cu contract individual de muncă cu timp parțial (4 h/zi), unic contract, activ toată luna septembrie 2026, care nu se află în niciuna dintre situațiile de excepție (elev/student, ucenic, persoană cu dizabilități, pensionar), presupun regimul general al veniturilor din salarii, cu aplicarea CAS reținute de angajator și a regulii CAS minim raportate la salariul minim brut pe țară în vigoare în luna respectivă, diminuat potrivit derogării aplicabile semestrului II 2026.*

> **CAS datorat (înainte de rotunjire) = 1.031,25 lei, întrucât CAS calculat asupra salariului brut este sub nivelul minim aferent salariului minim brut diminuat. [calcul: baza_minima = salariu_minim - diminuare = 4.125; cas_calculat = cota * salariu_brut = 540,62; cas_minim = cota * baza_minima = 1.031,25; cas_datorat = max(cas_calculat, cas_minim) = 1.031,25]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul — evaluat de cod, nu de model

- `baza_minima = salariu_minim - diminuare` → **4.125**
  - `salariu_minim` = 4.325 — din `hg_146_2026_salariu_minim#art1`: „la suma de 4.325 lei lunar”
  - `diminuare` = 200 — din `oug_89_2025#artIII~2/alin5/litb`: „pentru veniturile aferente perioadei 1 iulie-31 decembrie 2026, cu suma de 200 lei lunar.”
- `cas_calculat = cota * salariu_brut` → **540,62**
  - `cota` = 25% — din `cod_fiscal_227_2015_consolidat#art138`: „a) 25% datorată de către persoanele fizice care au calitatea de angajați”
  - `salariu_brut` = 2.162,50 — din întrebare: „salariu brut 2.162,50 lei”
- `cas_minim = cota * baza_minima` → **1.031,25**
  - `cota` = 25% — din `cod_fiscal_227_2015_consolidat#art138`: „a) 25% datorată de către persoanele fizice care au calitatea de angajați”
- `cas_datorat = max(cas_calculat, cas_minim)` → **1.031,25**

- **Codul fiscal (Legea 227/2015) art. 146 alin. (5^6)** — `cod_fiscal_227_2015_consolidat#art146/alin5^6` · valabil din 2025-01-01
  > în baza unui contract individual de muncă cu normă întreagă sau cu timp parțial, calculată potrivit alin. (5) , nu poate fi mai mică decât nivelul contribuției de asigurări sociale calculate prin aplicarea cotei prevăzute la art. 138 lit. a) asupra salariului de bază minim brut pe țară în vigoare în luna pentru care se datorează contribuția de asigurări sociale
- **Codul fiscal (Legea 227/2015) art. 138** — `cod_fiscal_227_2015_consolidat#art138` · valabil din 2018-01-01
  > Cotele de contribuții de asigurări sociale sunt următoarele: a) 25% datorată de către persoanele fizice care au calitatea de angajați sau pentru care există obligația plății contribuției de asigurări sociale, potrivit prezentei legi;
- **HG 146/2026 art. 1** — `hg_146_2026_salariu_minim#art1` · valabil din 2026-07-01
  > Începând cu data de 1 iulie 2026, salariul de bază minim brut pe țară garantat în plată, prevăzut la art. 164 alin. (1) din Legea nr. 53/2003 - Codul muncii, republicată , cu modificările și completările ulterioare, se stabilește în bani, fără a include sporuri și alte adaosuri, la suma de 4.325 lei lunar
- **OUG 89/2025 art. III alin. (5)** — `oug_89_2025#artIII~2/alin5` · valabil din nedovedit
  > nivelul salariului de bază minim brut pe țară garantat în plată în vigoare în luna pentru care se aplică prevederile art. 146 alin. (5^6 )-( 5^9) și ale art. 168 alin. (6^1) din Legea nr. 227/2015 , cu modificările și completările ulterioare, se diminuează astfel:
- **OUG 89/2025 art. III alin. (5) lit. b)** — `oug_89_2025#artIII~2/alin5/litb` · valabil din nedovedit
  > pentru veniturile aferente perioadei 1 iulie-31 decembrie 2026, cu suma de 200 lei lunar.
- derogare tratată: `oug_89_2025#artIII~2/alin5` — Se aplică: pentru veniturile aferente perioadei 1 iulie-31 decembrie 2026 (deci și septembrie 2026), salariul minim folosit la aplicarea art. 146 alin. (5^6) se diminuează cu 200 lei lunar; am folosit baza diminuată în calcul.
- derogare tratată: `oug_115_2023_consolidat#artLXXIII/alin5` — Nu se aplică: derogarea privește expres veniturile aferente anului 2024, nu luna septembrie 2026.
- derogare tratată: `oug_156_2024#artLXVI/alin5` — Nu se aplică cazului: pentru veniturile aferente semestrului II 2026 diminuarea salariului minim folosit la art. 146 alin. (5^6) este reglementată de OUG 89/2025 art. III alin. (5) lit. b), normă specială pentru perioada 1 iulie-31 decembrie 2026.

### Navigarea (11 pași, 8 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Stabilirea şi plata contribuţiei de asigurări sociale"}
2. `cauta` {"interogare": "contribuţia de asigurări sociale datorată nu poate fi mai mică decât nivelul contribuţiei calculate prin aplicarea cotei asupra salariului minim brut contract cu timp parţial"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art146/alin5^6"}
4. `deschide` {"id": "oug_89_2025#artIII~2/alin5"}
5. `cauta` {"interogare": "salariul de bază minim brut pe țară garantat în plată 2026 se stabilește în bani lei lunar"}
6. `deschide` {"id": "hg_146_2026_salariu_minim#art1"}
7. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Cotele de contribuții de asigurări sociale"}
8. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art138"}
9. `deschide` {"id": "oug_115_2023_consolidat#artLXXIII/alin5"}
10. `deschide` {"id": "oug_89_2025#artIII~2/alin5/litb"}
11. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art146"}

Apel: `claude-opus-5`, {'intrare': 16, 'iesire': 7123, 'cache_scriere': 18714, 'cache_citire': 123081} tokeni, $0.3567, 103 s

Pe fond: **GREȘIT** — faptul principal al cheii (['25%']) nu e in raspuns

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți stabilesc doar regula bazei minime de calcul prin trimitere la cota de la art. 138 lit. a), dar nu conțin textul cu nivelul cotei CAS, nici nivelul salariului de bază minim brut pe țară în vigoare în septembrie 2026 (fragmentul din OUG 89/2025 acoperă doar 1 ianuarie-30 iunie 2026 și este trunchiat). În plus, cuantumul CAS ar rezulta dintr-un calcul (cotă aplicată bazei) care nu apare literal în niciun atom.

## Cheia

- Nu 25% × 2.162,50 = 540,63 lei, ci minimul: 25% × (4.325 − 200) = 1.031,25 lei; diferența de 490,63 lei o suportă angajatorul în numele salariatului (analog CASS: minim 10% × 4.125 = 412,50 lei)
- temei: Cod fiscal art. 146 alin. (5^6), (5^7), (5^9); art. 168 alin. (6^1) (CASS, aplicare corespunzătoare); OUG 89/2025 art. III alin. (5) lit. b) (salariul minim diminuat cu 200 lei pentru 01.07–31.12.2026); HG 146/2026 art. 1
