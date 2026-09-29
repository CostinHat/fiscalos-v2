# Q-PRF-01 — PARAMETRU

**Întrebarea:** Ce cotă de impozit pe veniturile microîntreprinderilor se aplică în 2026 unei microîntreprinderi care realizează venituri din consultanță, și cu ce cod de obligație se declară în D100?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 28.09.2026 presupun o persoană juridică română plătitoare de impozit pe veniturile microîntreprinderilor (Titlul III din Codul fiscal), care obține venituri din consultanță, fără a fi în vreo situație specială de ieșire din sistem, și că întrebarea vizează cota aplicabilă în anul fiscal 2026 și poziția din Nomenclatorul obligațiilor de plată la bugetul de stat utilizat la formularul 100.*

Datele din întrebare: 2026-09-28 · data de referință aleasă: **2026-09-28** — Singura dată purtată de întrebare; faptul întrebat este cota aplicabilă în anul 2026.

> **Cota este de 1% — Codul fiscal prevede o cotă unică pentru veniturile microîntreprinderilor, fără o cotă distinctă pentru veniturile din consultanță. În formularul 100 impozitul se declară la poziția „Impozit pe veniturile microîntreprinderilor" (temei art. 47 și 56 din Legea nr. 227/2015) din Nomenclatorul obligațiilor de plată la bugetul de stat, respectiv pct. 5 din anexa nr. 3 la OPANAF 587/2016; un cod numeric de trezorerie distinct nu apare în textul normativ.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 51 alin. (1)** — `cod_fiscal_227_2015_consolidat#art51/alin1` · valabil din 2026-01-01
  > Cota de impozit pe veniturile microîntreprinderilor este de 1%.
- **OPANAF 587/2016 anexa nr. 3, pct. 5** — `opanaf_587_2016_aprobarea_modelului_continutului_formularelor_utilizate#anexa3/pct5` · valabil din nedovedit
  > Impozit pe veniturile microîntreprinderilor art. 47 și 56 din Legea nr. 227/2015 , cu modificările și completările ulterioare
- **OPANAF 587/2016 anexa nr. 3,** — `opanaf_587_2016_aprobarea_modelului_continutului_formularelor_utilizate#anexa3` · valabil din nedovedit
  > Anexa nr. 3 Nomenclatorul obligațiilor de plată la bugetul de stat Nr. crt. Denumirea creanței fiscale Temeiul legal

### Navigarea (15 pași, 12 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "cotele de impozitare"}
2. `cauta` {"interogare": "impozit pe veniturile microîntreprinderilor cota 3% consultanță"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art51"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art51/alin1"}
5. `cauta` {"interogare": "nomenclator obligații de plată impozit pe veniturile microîntreprinderilor cod 1130 declarația 100"}
6. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Definiții microîntreprindere"}
7. `cuprins` {"act": "opanaf_57_2026_d100_d710", "filtru": "microîntreprinderilor"}
8. `cuprins` {"act": "opanaf_57_2026_d100_d710", "filtru": "nomenclator"}
9. `cauta` {"interogare": "Nomenclatorul obligațiilor de plată la bugetul de stat impozit pe veniturile microîntreprinderilor"}
10. `cuprins` {"act": "opanaf_587_2016_aprobarea_modelului_continutului_formularelor_utilizate", "filtru": "microîntreprinderilor"}
11. `cuprins` {"act": "opanaf_602_2026_modificare_opanaf_587_2016_formulare", "filtru": "microîntreprinderilor"}
12. `deschide` {"id": "opanaf_587_2016_aprobarea_modelului_continutului_formularelor_utilizate#anexa3/pct5"}
13. `deschide` {"id": "opanaf_587_2016_aprobarea_modelului_continutului_formularelor_utilizate#anexa3"}
14. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art47"}
15. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art47/alin1"}

Apel: `claude-opus-5`, {'intrare': 24, 'iesire': 5720, 'cache_scriere': 16324, 'cache_citire': 166507} tokeni, $0.3284, 98 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — NU POT, pe fond NU POT

> modelul s-a abţinut: Am regăsit în atomi doar prima parte a răspunsului: art. 51 alin. (1) din Codul fiscal prevede o cotă unică, fără diferențiere pentru veniturile din consultanță, iar textul nu conține o cotă distinctă pentru consultanță. În schimb, nu am obținut niciun atom care să conțină Nomenclatorul obligațiilor de plată la bugetul de stat (anexa nr. 3 la OPANAF 587/2016) cu poziția/codul de obligație aferent impozitului pe veniturile microîntreprinderilor; OPANAF 57/2026 doar modifică a…

## Cheia

- 1% (cotă unică; cota de 3% a fost abrogată de la 01.01.2026); D100 cod obligație 121, câmp cota = 1
- temei: Legea 227/2015 (Cod fiscal) art. 51 alin. (1), modificat de OUG 89/2025 art. I pct. 4, în vigoare 01.01.2026; art. 51 alin. (1^1) abrogat de OUG 89/2025 art. I pct. 5; structura XML D100 v2 (OPANAF 57/2026), pct. 3 „cota micro”: dacă cod_oblig=121 atunci cota=1
