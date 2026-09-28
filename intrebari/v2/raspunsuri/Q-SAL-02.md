# Q-SAL-02 — PROCEDURA

**Întrebarea:** Pentru salariile aferente lunii august 2026, ce declarație depune angajatorul și până când; până când se plătesc CAS și impozitul reținut?

## Stratul semantic (motorul nou) — NU POT RĂSPUNDE

*La data de referință 31.08.2026, presupun un angajator persoană juridică din România care plătește venituri din salarii aferente lunii august 2026 și reține la sursă impozitul și contribuțiile sociale; întrebarea nu precizează dacă angajatorul se încadrează în categoria plătitorilor care depun declarația trimestrial, iar acest element schimbă atât termenul de depunere, cât și termenul de plată a CAS.*

Motiv: INCOMPLET: intrebarea nu da faptele de care depinde raspunsul: Dacă angajatorul face parte dintre plătitorii prevăzuți la art. 80 alin. (2), care depun declarația trimestrial, sau este obligat la depunere lunară; Dacă în cursul trimestrului au intervenit concedii și indemnizații de asigurări sociale de sănătate ori încetarea calității de asigurat (situație care modifică termenul de depunere pentru plătitorii cu regim trimestrial); Data la care se plătesc efectiv veniturile din salarii aferente lunii august 2026

- **Codul fiscal (Legea 227/2015) art. 147 alin. (4)** — `cod_fiscal_227_2015_consolidat#art147~2/alin4` · valabil din nedovedit
  > plătitorii de venituri din salarii și asimilate salariilor prevăzuți la art. 80 alin. (2) , în calitate de angajatori sau de persoane asimilate angajatorului, depun trimestrial Declarația privind obligațiile de plată a contribuțiilor sociale, impozitului pe venit și evidența nominală a persoanelor asigurate aferentă fiecărei luni a trimestrului,
- **Codul fiscal (Legea 227/2015) art. 147 alin. (1)** — `cod_fiscal_227_2015_consolidat#art147~2/alin1` · valabil din nedovedit
  > sunt obligate să depună lunar, până la data de 25 inclusiv a lunii următoare celei pentru care se plătesc veniturile, Declarația privind obligațiile de plată a contribuțiilor sociale, impozitului pe venit și evidența nominală a persoanelor asigurate.
- **Codul fiscal (Legea 227/2015) art. 146 alin. (3)** — `cod_fiscal_227_2015_consolidat#art146/alin3` · valabil din 2018-01-01
  > Contribuția de asigurări sociale calculată și reținută potrivit alin. (1) se plătește la bugetul asigurărilor sociale de stat până la data de 25 inclusiv a lunii următoare celei pentru care se plătesc veniturile sau până la data de 25 inclusiv a lunii următoare trimestrului pentru care se datorează, după caz

Apel: `claude-opus-5`, {'intrare': 3196, 'iesire': 3223, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0973, 42.1 s

Pe fond: **NU POT** — INCOMPLET: intrebarea nu da faptele de care depinde raspunsul: Dacă angajatorul face parte dintre plătitorii prevăzuți la art. 80 alin. (2), care depun declarația trimestrial, sau este obligat la depu

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-08-31 (luna, din "august 2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **d)-f) , precum și persoanele fizice care realizează în România venituri din salarii sau asimilate salariilor de la angajatori din state care nu intră sub incidența legislației europene aplicabile în domeniul securității sociale, precum și a acordurilor privind sistemele de securitate socială la care România este parte sunt obligate să depună lunar, până la data de 25 inclusiv a lunii următoare celei pentru care se plătesc veniturile, Declarația privind obligațiile de plată a contribuțiilor sociale, impozitului pe venit și evidența nominală a persoanelor asigurate.**

Motiv: D15: fraza care conţine un fapt de forma cerută (termen) si potriveste cel mai bine intrebarea (scor local 26.9)

- **Codul fiscal (Legea 227/2015) art. 147 alin. (1)** — `cod_fiscal_227_2015_consolidat#art147~2/alin1` · valabil din nedovedit
  > Persoanele fizice și juridice care au calitatea de angajatori sau sunt asimilate acestora, instituțiile prevăzute la art. 136 lit. d)-f) , precum și persoanele fizice care realizează în România venituri din salarii sau asimilate salariilor de la angajatori din state care nu intră sub incidența legislației europene aplicabile în domeniul securității sociale, precum și a acordurilor privind sistemele de securitate socială la care România este parte sunt obligate să depună lunar, până la data de 25 inclusiv a lunii următoare celei pentru care se plătesc veniturile, Declarația privind obligațiile …

Pe fond: **GREȘIT** — faptul principal al cheii (['25.09.2026']) nu e in raspuns

## Cheia

- răspuns așteptat: D112, până la 25.09.2026 inclusiv; CAS și impozitul pe salarii se plătesc tot până la 25.09.2026. Excepție: angajatorii din CF art. 80 alin. (2) (ex. micro cu sub 3 salariați, ONG-uri, PFA/II) depun D112 trimestrial și plătesc până la 25 a lunii următoare trimestrului — pentru august (T3): 25.10.2026, duminică → efectiv 26.10.2026.
- temei așteptat: Cod fiscal art. 147 alin. (1) și (4); art. 146 alin. (3); art. 80 alin. (1)-(2); CPF art. 75

