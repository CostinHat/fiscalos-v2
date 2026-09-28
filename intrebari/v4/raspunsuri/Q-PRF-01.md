# Q-PRF-01 — PARAMETRU

**Întrebarea:** Ce cotă de impozit pe veniturile microîntreprinderilor se aplică în 2026 unei microîntreprinderi care realizează venituri din consultanță, și cu ce cod de obligație se declară în D100?

## Stratul de navigare (v4) — NU POT RĂSPUNDE

*La data de referință 28.09.2026, pentru o persoană juridică română plătitoare de impozit pe veniturile microîntreprinderilor (Titlul III Cod fiscal) care obține venituri din consultanță, presupunând că îndeplinește condițiile de microîntreprindere din art. 47 și că declară trimestrial prin formularul 100.*

Motiv: modelul s-a abţinut: Am regăsit în atomi doar prima parte a răspunsului: art. 51 alin. (1) din Codul fiscal prevede o cotă unică, fără diferențiere pentru veniturile din consultanță, iar textul nu conține o cotă distinctă pentru consultanță. În schimb, nu am obținut niciun atom care să conțină Nomenclatorul obligațiilor de plată la bugetul de stat (anexa nr. 3 la OPANAF 587/2016) cu poziția/codul de obligație aferent impozitului pe veniturile microîntreprinderilor; OPANAF 57/2026 doar modifică acel nomenclator după poziția 112, fără ca textul pozițiilor să-mi fie disponibil. Fără acest atom nu pot indica codul de obligație din D100, deci mă abțin de la un răspuns complet.

- **Codul fiscal (Legea 227/2015) art. 51 alin. (1)** — `cod_fiscal_227_2015_consolidat#art51/alin1` · valabil din 2026-01-01
  > Cota de impozit pe veniturile microîntreprinderilor este de 1%.
- **Codul fiscal (Legea 227/2015) art. 56 alin. (1)** — `cod_fiscal_227_2015_consolidat#art56/alin1` · valabil din nedovedit
  > Calculul și plata impozitului pe veniturile microîntreprinderilor se efectuează trimestrial, până la data de 25 inclusiv a lunii următoare trimestrului pentru care se calculează impozitul.

### Navigarea (12 pași, 7 ture)

1. `cauta` {"interogare": "cotele de impozitare pe veniturile microîntreprinderilor consultanță"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "cotele de impozitare"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art51"}
4. `cauta` {"interogare": "nomenclatorul obligațiilor de plată impozit pe veniturile microîntreprinderilor D100 cod"}
5. `cuprins` {"act": "opanaf_57_2026_d100_d710", "filtru": "microîntreprinderilor"}
6. `cauta` {"interogare": "Impozit pe veniturile microîntreprinderilor nomenclator obligații de plată buget de stat denumire creanță fiscală"}
7. `cuprins` {"act": "opanaf_57_2026_d100_d710", "filtru": ""}
8. `cauta` {"interogare": "poziția din Nomenclatorul obligațiilor de plată la bugetul de stat impozit pe veniturile microîntreprinderilor formular 100"}
9. `cuprins` {"act": "opanaf_57_2026_d100_d710", "filtru": "Nomenclator"}
10. `cauta` {"interogare": "Impozit pe veniturile microîntreprinderilor se completează rândul 1 suma reprezentând impozit datorat trimestrial declarația 100"}
11. `deschide` {"id": "opanaf_57_2026_d100_d710#artI"}
12. `cauta` {"interogare": "cod 17 impozit pe veniturile microîntreprinderilor anexa nomenclator obligații plată bugetul de stat"}

Apel: `claude-opus-5`, {'intrare': 14, 'iesire': 3667, 'cache_scriere': 11588, 'cache_citire': 74729} tokeni, $0.2015, 62 s

Pe fond: **NU POT** — modelul s-a abţinut: Am regăsit în atomi doar prima parte a răspunsului: art. 51 alin. (1) din Codul fiscal prevede o cotă unică, fără diferențiere pentru veniturile din consultanță, iar textul nu con

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți nu conțin nicio dispoziție privind cotele de impozit pe veniturile microîntreprinderilor (nici regula specială pentru veniturile din consultanță) aplicabile în 2026, nici nomenclatorul codurilor de obligații de plată din formularul D100. Fragmentele furnizate se referă la bonificația de 3% pentru anul fiscal 2025 și la reguli de valoare fiscală/amortizare din titlul impozitului pe profit, fără legătură cu întrebarea.

## Cheia

- 1% (cotă unică; cota de 3% a fost abrogată de la 01.01.2026); D100 cod obligație 121, câmp cota = 1
- temei: Legea 227/2015 (Cod fiscal) art. 51 alin. (1), modificat de OUG 89/2025 art. I pct. 4, în vigoare 01.01.2026; art. 51 alin. (1^1) abrogat de OUG 89/2025 art. I pct. 5; structura XML D100 v2 (OPANAF 57/2026), pct. 3 „cota micro”: dacă cod_oblig=121 atunci cota=1
