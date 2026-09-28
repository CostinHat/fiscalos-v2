# Q-SAL-03 — CALCUL

**Întrebarea:** Salariat cu normă întreagă la funcția de bază, septembrie 2026, salariu brut 10.000 lei, fără persoane în întreținere, fără copii școlarizați, peste 26 de ani, fără alte deduceri. Calculați CAS, CASS, impozit, net și CAM.

## Stratul de navigare (v4) — NU POT RĂSPUNDE

*La data de referință 30.09.2026, pentru un salariat cu contract individual de muncă cu normă întreagă, la funcția de bază, cu salariu brut lunar de 10.000 lei, fără persoane în întreținere și fără alte deduceri, presupun regimul general de impozitare a veniturilor din salarii și de contribuții sociale obligatorii din Codul fiscal (fără scutiri sectoriale de tip construcții/IT/agricultură).*

Motiv: modelul s-a abţinut: Răspunsul cerut presupune atât cote legale (CAS, CASS, impozit, CAM), cât și rezultate obținute prin calcul. Dintre acestea, cota CASS și bazele de calcul (art. 139 alin. (1), art. 157 alin. (1)) nu au putut fi obținute dintr-un atom - atomul art. 156 deschis nu conține cota, iar căutările nu au returnat textul cotei. De asemenea, nu am putut verifica din atomi regimul deducerii personale la acest nivel de venit și nici dacă derogările temporare (OUG 156/2024, OUG 89/2025) sunt sau nu active în septembrie 2026. Fără aceste elemente, nu pot stabili corect CASS, baza impozabilă, impozitul și netul.

- **Codul fiscal (Legea 227/2015) art. 138** — `cod_fiscal_227_2015_consolidat#art138` · valabil din 2018-01-01
  > Cotele de contribuții de asigurări sociale sunt următoarele: a) 25% datorată de către persoanele fizice care au calitatea de angajați sau pentru care există obligația plății contribuției de asigurări sociale, potrivit prezentei legi;
- **Codul fiscal (Legea 227/2015) art. 220^3 alin. (1)** — `cod_fiscal_227_2015_consolidat#art220^3/alin1` · valabil din nedovedit
  > Cota contribuției asiguratorii pentru muncă este de 2,25%.
- derogare tratată: `oug_156_2024#artLXVI/alin1` — Derogare temporară de la art. 78, art. 139 alin. (1), art. 140, art. 157 alin. (1) și art. 220^4 alin. (1) aplicabilă veniturilor la nivelul salariului minim brut; nu a putut fi verificată în detaliu, dar cazul are un brut de 10.000 lei, peste nivelul salariului minim.
- derogare tratată: `oug_89_2025#artIII~2/alin1` — Aceeași derogare, cu aceleași articole vizate, pentru veniturile la nivelul salariului minim; nu a fost deschisă, deci aplicabilitatea ei la septembrie 2026 rămâne neverificată.
- derogare tratată: `oug_115_2023_consolidat#artLXXIII/alin1` — Derogare privind veniturile la nivelul salariului minim brut, pentru perioade anterioare; nu a fost deschisă și nu a putut fi verificată pentru septembrie 2026.

### Navigarea (12 pași, 7 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "cotele de contribuții"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "deducere personală"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art138"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art156"}
5. `cauta` {"interogare": "Cota de contribuție de asigurări sociale de sănătate este de 10%"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art220^3"}
7. `cauta` {"interogare": "Cota contribuției de asigurări sociale de sănătate 10% art. 156"}
8. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art220^3/alin1"}
9. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Cota de contribuție de asigurări sociale de sănătate"}
10. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art78"}
11. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art78/alin2"}
12. `cauta` {"interogare": "cota de 10% și se datorează de către persoanele fizice care au calitatea de angajați sănătate"}

Apel: `claude-opus-5`, {'intrare': 14, 'iesire': 4453, 'cache_scriere': 16998, 'cache_citire': 86589} tokeni, $0.2609, 72 s

Pe fond: **NU POT** — modelul s-a abţinut: Răspunsul cerut presupune atât cote legale (CAS, CASS, impozit, CAM), cât și rezultate obținute prin calcul. Dintre acestea, cota CASS și bazele de calcul (art. 139 alin. (1), art

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți conțin doar reguli privind baza de calcul al CAS (art. 139 alin. (1)) și al CASS (art. 157 alin. (1)), contribuția minimă de CAS raportată la salariul minim și derogările privind suma neimpozabilă de 200/300 lei pentru salariații plătiți la nivelul salariului minim. Nu există în context niciun atom care să prevadă literal cotele de contribuție (CAS, CASS), cota de impozit pe venit, deducerea personală sau cota contribuției asiguratorii pentru muncă (CAM). În p…

## Cheia

- CAS 2.500 lei; CASS 1.000 lei; deducere personală 0 (brut > 4.325 + 2.000 = 6.325 lei); impozit 10% × (10.000 − 3.500) = 650 lei; net 5.850 lei; CAM 2,25% × 10.000 = 225 lei
- temei: Cod fiscal art. 138 lit. a) (CAS 25%); art. 156 (CASS 10%); art. 77 alin. (3) și (4) (fără deducere peste salariul minim + 2.000 lei); art. 78 alin. (2) lit. a) (cota 10%); art. 220^3 alin. (1) (CAM 2,25%); HG 146/2026 art. 1 (salariul minim 4.325 lei de la 01.07.2026)
