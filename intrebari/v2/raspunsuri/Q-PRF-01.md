# Q-PRF-01 — PARAMETRU

**Întrebarea:** Ce cotă de impozit pe veniturile microîntreprinderilor se aplică în 2026 unei microîntreprinderi care realizează venituri din consultanță, și cu ce cod de obligație se declară în D100?

## Stratul semantic (motorul nou) — NU POT RĂSPUNDE

*La data de referință 28.09.2026 presupun o persoană juridică română plătitoare de impozit pe veniturile microîntreprinderilor, care obține venituri din activități de consultanță și care ar trebui să declare impozitul trimestrial prin formularul D100, fără alte precizări din întrebare.*

Motiv: modelul s-a abţinut: Atomii primiți conțin doar regula generală de cotă (art. 51 alin. (1) din Codul fiscal - 1%), dar nu conțin nicio prevedere privind tratamentul specific al veniturilor din consultanță (eventuală cotă diferențiată sau condiție de pondere a acestor venituri), astfel încât nu pot confirma cota aplicabilă cazului descris. În plus, nu există niciun atom din care să rezulte codul de obligație bugetară sub care se declară impozitul pe veniturile microîntreprinderilor în formularul D100 (nomenclatorul obligațiilor de plată nu a fost furnizat). Un răspuns ar necesita informații din…


Apel: `claude-opus-5`, {'intrare': 2391, 'iesire': 895, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0351, 17.7 s

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți conțin doar regula generală de cotă (art. 51 alin. (1) din Codul fiscal - 1%), dar nu conțin nicio prevedere privind tratamentul specific al veniturilor din consult

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **1%**

Motiv: valoarea de forma cerută (procent) din atomul care poarta o asemenea valoare si potriveste cel mai bine cuvintele rare ale intrebarii (scor local 12.6)

- **Codul fiscal (Legea 227/2015) art. 51 alin. (1)** — `cod_fiscal_227_2015_consolidat#art51/alin1` · valabil din 2026-01-01
  > Cota de impozit pe veniturile microîntreprinderilor este de 1%.

Pe fond: **CORECT** — faptul principal si articolul coincid

## Cheia

- răspuns așteptat: 1% (cotă unică; cota de 3% a fost abrogată de la 01.01.2026); D100 cod obligație 121, câmp cota = 1
- temei așteptat: Legea 227/2015 (Cod fiscal) art. 51 alin. (1), modificat de OUG 89/2025 art. I pct. 4, în vigoare 01.01.2026; art. 51 alin. (1^1) abrogat de OUG 89/2025 art. I pct. 5; structura XML D100 v2 (OPANAF 57/2026), pct. 3 „cota micro”: dacă cod_oblig=121 atunci cota=1

