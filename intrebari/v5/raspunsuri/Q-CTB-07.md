# Q-CTB-07 — CALCUL

**Întrebarea:** SRL distribuie (hotărâre AGA) și plătește în 10 aprilie 2026 unui asociat persoană fizică rezidentă dividende brute de 50.000 lei. Cât impozit se reține, cât primește net și până când se virează?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 10.04.2026, presupun o societate cu răspundere limitată persoană juridică română care distribuie prin hotărâre AGA și plătește în 2026 dividende brute de 50.000 lei unui asociat persoană fizică rezidentă în România, impozitul pe dividende fiind reținut la sursă de plătitor (nu analizez contribuția de asigurări sociale de sănătate, neîntrebată).*

Datele din întrebare: 2026-04-10 · data de referință aleasă: **2026-04-10** — Singura dată din întrebare; este data plății dividendelor, care declanșează reținerea impozitului și curgerea termenului de virare.

> **Cota de impozit pe dividende este 16%, deci se reține un impozit de 8.000 lei, iar asociatul primește net 42.000 lei. Impozitul se virează integral la bugetul de stat până la data de 25 inclusiv a lunii următoare celei în care se face plata, adică până la 25 mai 2026 (plata dividendelor fiind făcută în aprilie 2026).**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul, pas cu pas — evaluat de cod, nu de model

- `impozit = dividend_brut * cota_dividende` = (50.000 × 16%) = **8.000**
  - `dividend_brut` = 50.000 — FAPT_CAZ (din întrebare): „plătește în 10 aprilie 2026 unui asociat persoană fizică rezidentă dividende brute de 50.000 lei”
  - `cota_dividende` = 16% — VALOARE_LEGALA din `cod_fiscal_227_2015_consolidat#art97/alin7`: „se impozitează cu o cotă de 16% din suma acestora, impozitul fiind final”
- `net = dividend_brut - impozit` = (50.000 − 8.000) = **42.000**
  - `dividend_brut` = 50.000 — FAPT_CAZ (din întrebare): „dividende brute de 50.000 lei”

- **Codul fiscal (Legea 227/2015) art. 97 alin. (7)** — `cod_fiscal_227_2015_consolidat#art97/alin7` · valabil din 2025-08-01
  > Veniturile sub formă de dividende, inclusiv câștigul obținut ca urmare a deținerii de titluri de participare definite de legislația în materie la organisme de plasament colectiv, se impozitează cu o cotă de 16% din suma acestora, impozitul fiind final.
- **Codul fiscal (Legea 227/2015) art. 97 alin. (7)** — `cod_fiscal_227_2015_consolidat#art97/alin7` · valabil din 2025-08-01
  > Obligația calculării și reținerii impozitului pe veniturile sub formă de dividende revine persoanelor juridice, odată cu plata dividendelor/sumelor reprezentând câștigul obținut ca urmare a deținerii de titluri de participare de către acționari/ asociați/investitori. Termenul de virare a impozitului este până la data de 25 inclusiv a lunii următoare celei în care se face plata.
- **Codul fiscal (Legea 227/2015) art. 97 alin. (7)** — `cod_fiscal_227_2015_consolidat#art97/alin7` · valabil din 2025-08-01
  > prevederile art. II pct. 5 referitor la modificarea dispozițiilor art. 97 alin. (7) din Legea nr. 227/2015 , cu modificările și completările ulterioare, se aplică veniturilor din dividende distribuite începând cu data de 1 ianuarie 2026;

### Navigarea (5 pași, 4 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "dividende"}
2. `cauta` {"interogare": "impozit pe dividende 16% reținere la sursă persoane fizice"}
3. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "investiții"}
4. `cauta` {"interogare": "venituri din dividende cota de impozit dividend brut distribuit persoană fizică termen 25 inclusiv a lunii următoare"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art97/alin7"}

Apel: `claude-opus-5`, {'intrare': 8, 'iesire': 2850, 'cache_scriere': 4802, 'cache_citire': 34628} tokeni, $0.1186, 39 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond CORECT

> Se reține impozit pe dividende de 8.000 lei (cotă 16%, impozit final), asociatul primește net 42.000 lei, iar impozitul se virează integral la bugetul de stat până la data de 25 inclusiv a lunii următoare celei în care se face plata. [calcul: impozit = baza * cota = 8.000; net = baza - impozit = 42.000]

## Cheia

- Impozit 8.000 lei (16%, final); net 42.000 lei; virare până la 25 mai 2026 inclusiv (25 a lunii următoare plății). Dacă nu s-ar plăti până la sfârșitul anului aprobării, impozitul s-ar plăti până la 25 ianuarie a anului următor.
- temei: Legea 227/2015 art. 97 alin. (7), modificat de Legea 141/2025 art. II pct. 5, aplicabil dividendelor distribuite de la 01.01.2026 (Legea 141/2025 art. VII alin. (1) lit. c))
