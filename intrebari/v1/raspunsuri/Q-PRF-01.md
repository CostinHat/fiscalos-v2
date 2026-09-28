# Q-PRF-01 — PARAMETRU

**Întrebarea:** Ce cotă de impozit pe veniturile microîntreprinderilor se aplică în 2026 unei microîntreprinderi care realizează venituri din consultanță, și cu ce cod de obligație se declară în D100?

**Data de referință:** 2026-09-28 (an)

## Răspunsul motorului — RĂSPUNS

> 1%

*Motiv:* valoarea de forma cerută (procent) din atomul care poarta o asemenea valoare si potriveste cel mai bine cuvintele rare ale intrebarii (scor local 12.6)

### Argument (atomul care răspunde)

- **Codul fiscal (Legea 227/2015) art. 51 alin. (1)** — `cod_fiscal_227_2015_consolidat#art51/alin1`
  - valabil din: 2026-01-01 · la data întrebării: True
  > Cota de impozit pe veniturile microîntreprinderilor este de 1%.

## Comparația cu cheia — **CORECT**

- *de ce:* faptul principal si articolul coincid
- *răspunsul așteptat:* 1% (cotă unică; cota de 3% a fost abrogată de la 01.01.2026); D100 cod obligație 121, câmp cota = 1
- *temeiul așteptat:* Legea 227/2015 (Cod fiscal) art. 51 alin. (1), modificat de OUG 89/2025 art. I pct. 4, în vigoare 01.01.2026; art. 51 alin. (1^1) abrogat de OUG 89/2025 art. I pct. 5; structura XML D100 v2 (OPANAF 57/2026), pct. 3 „cota micro”: dacă cod_oblig=121 atunci cota=1

