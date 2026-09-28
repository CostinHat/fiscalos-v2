# Q-CTB-07 — CALCUL

**Întrebarea:** SRL distribuie (hotărâre AGA) și plătește în 10 aprilie 2026 unui asociat persoană fizică rezidentă dividende brute de 50.000 lei. Cât impozit se reține, cât primește net și până când se virează?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 10.04.2026, presupun un SRL român plătitor de dividende către un asociat persoană fizică rezidentă, dividende distribuite prin hotărâre AGA în 2026 și plătite efectiv la 10.04.2026, impozitul pe dividende fiind final și reținut la sursă (nu analizez contribuția de asigurări sociale de sănătate, care nu face obiectul întrebării).*

> **Se reține impozit pe dividende de 8.000 lei (cotă 16%, impozit final), asociatul primește net 42.000 lei, iar impozitul se virează integral la bugetul de stat până la data de 25 inclusiv a lunii următoare celei în care se face plata. [calcul: impozit = baza * cota = 8.000; net = baza - impozit = 42.000]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

### Calculul — evaluat de cod, nu de model

- `impozit = baza * cota` → **8.000**
  - `baza` = 50.000 — din întrebare: „dividende brute de 50.000 lei”
  - `cota` = 16% — din `cod_fiscal_227_2015_consolidat#art97/alin7`: „se impozitează cu o cotă de 16% din suma acestora, impozitul fiind final”
- `net = baza - impozit` → **42.000**
  - `baza` = 50.000 — din întrebare: „dividende brute de 50.000 lei”

- **Codul fiscal (Legea 227/2015) art. 97 alin. (7)** — `cod_fiscal_227_2015_consolidat#art97/alin7` · valabil din 2025-08-01
  > Veniturile sub formă de dividende, inclusiv câștigul obținut ca urmare a deținerii de titluri de participare definite de legislația în materie la organisme de plasament colectiv, se impozitează cu o cotă de 16% din suma acestora, impozitul fiind final.
- **Codul fiscal (Legea 227/2015) art. 97 alin. (7)** — `cod_fiscal_227_2015_consolidat#art97/alin7` · valabil din 2025-08-01
  > Obligația calculării și reținerii impozitului pe veniturile sub formă de dividende revine persoanelor juridice, odată cu plata dividendelor/sumelor reprezentând câștigul obținut ca urmare a deținerii de titluri de participare de către acționari/ asociați/investitori. Termenul de virare a impozitului este până la data de 25 inclusiv a lunii următoare celei în care se face plata.
- **Codul fiscal (Legea 227/2015) art. 97 alin. (7)** — `cod_fiscal_227_2015_consolidat#art97/alin7` · valabil din 2025-08-01
  > se aplică veniturilor din dividende distribuite începând cu data de 1 ianuarie 2026
- **Codul fiscal (Legea 227/2015) art. 132 alin. (1)** — `cod_fiscal_227_2015_consolidat#art132/alin1` · valabil din nedovedit
  > Plătitorii de venituri, cu regim de reținere la sursă a impozitelor, sunt obligați să calculeze, să rețină, să plătească și să declare impozitul reținut la sursă, până la termenul de plată a acestuia inclusiv.

### Navigarea (3 pași, 3 ture)

1. `cauta` {"interogare": "impozit pe dividende cota 16% reținere la sursă termen 25 inclusiv a lunii următoare"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "dividende"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art97/alin7"}

Apel: `claude-opus-5`, {'intrare': 6, 'iesire': 2460, 'cache_scriere': 2975, 'cache_citire': 21358} tokeni, $0.0908, 34 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți conțin cota de impozit (16%) și termenul de virare (până la data de 25 inclusiv a lunii următoare celei în care se face plata), dar cuantumul impozitului reținut și suma netă încasată de asociat rezultă dintr-un calcul (aplicarea cotei asupra dividendului brut de 50.000 lei și scăderea impozitului), iar aceste valori nu apar literal în niciun atom. Nu am voie să efectuez calculul, deci nu pot da răspunsul cerut în întregime.

## Cheia

- Impozit 8.000 lei (16%, final); net 42.000 lei; virare până la 25 mai 2026 inclusiv (25 a lunii următoare plății). Dacă nu s-ar plăti până la sfârșitul anului aprobării, impozitul s-ar plăti până la 25 ianuarie a anului următor.
- temei: Legea 227/2015 art. 97 alin. (7), modificat de Legea 141/2025 art. II pct. 5, aplicabil dividendelor distribuite de la 01.01.2026 (Legea 141/2025 art. VII alin. (1) lit. c))
