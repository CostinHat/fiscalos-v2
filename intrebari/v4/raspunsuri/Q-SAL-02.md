# Q-SAL-02 — PROCEDURA

**Întrebarea:** Pentru salariile aferente lunii august 2026, ce declarație depune angajatorul și până când; până când se plătesc CAS și impozitul reținut?

## Stratul de navigare (v4) — NU POT RĂSPUNDE

*La data de referință august 2026, presupun un angajator obișnuit (persoană juridică ce nu se încadrează în categoriile cu obligații declarative și de plată trimestriale), plătitor de venituri din salarii, cu declarare și plată lunară; întrebarea nu indică apartenența la categoriile de la art. 80 alin. (2), deci aplic regula generală lunară.*

Motiv: VERIFICAREA MECANICA a respins propunerea modelului: cifra '112' din raspuns nu apare literal in citate sau in intrebare

- **Codul fiscal (Legea 227/2015) art. 147 alin. (1)** — `cod_fiscal_227_2015_consolidat#art147~2/alin1` · valabil din nedovedit
  > sunt obligate să depună lunar, până la data de 25 inclusiv a lunii următoare celei pentru care se plătesc veniturile, Declarația privind obligațiile de plată a contribuțiilor sociale, impozitului pe venit și evidența nominală a persoanelor asigurate.
- **Codul fiscal (Legea 227/2015) art. 146 alin. (3)** — `cod_fiscal_227_2015_consolidat#art146/alin3` · valabil din 2018-01-01
  > Contribuția de asigurări sociale calculată și reținută potrivit alin. (1) se plătește la bugetul asigurărilor sociale de stat până la data de 25 inclusiv a lunii următoare celei pentru care se plătesc veniturile
- **Codul fiscal (Legea 227/2015) art. 80 alin. (1)** — `cod_fiscal_227_2015_consolidat#art80/alin1` · valabil din nedovedit
  > Plătitorii de salarii și de venituri asimilate salariilor au obligația de a calcula și de a reține impozitul aferent veniturilor fiecărei luni la data efectuării plății acestor venituri, precum și de a-l plăti la bugetul de stat până la data de 25 inclusiv a lunii următoare celei pentru care se plătesc aceste venituri.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art147~2/alin4` — Excepția privește depunerea trimestrială a declarației de către plătitorii prevăzuți la art. 80 alin. (2) (ONG-uri, plătitori de impozit pe profit/microîntreprinderi sub pragurile acolo prevăzute, PFA etc.); întrebarea nu indică încadrarea angajatorului în aceste categorii, deci se aplică regula lun…
- derogare tratată: `cod_fiscal_227_2015_consolidat#art80/alin2` — Excepția stabilește plata impozitului până la 25 inclusiv a lunii următoare trimestrului doar pentru categoriile enumerate (asociații/fundații, anumite persoane juridice, PFA/întreprinderi individuale); cazul presupus nu se încadrează, deci rămâne termenul lunar din alin. (1).
- derogare tratată: `cod_fiscal_227_2015_consolidat#art147~2/alin8` — Se referă la opțiunea persoanelor și entităților de la alin. (4) de a depune lunar; nu schimbă termenul de 25 al lunii următoare pentru angajatorul lunar presupus.

### Navigarea (9 pași, 6 ture)

1. `cauta` {"interogare": "declarația privind obligațiile de plată a contribuțiilor sociale, impozitului pe venit termen 25 inclusiv a lunii următoare"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Declararea, reținerea și plata contribuției"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art147~2/alin1"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art80"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art80/alin1"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art146"}
7. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art146/alin3"}
8. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art147~2/alin4"}
9. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art80/alin2"}

Apel: `claude-opus-5`, {'intrare': 12, 'iesire': 2904, 'cache_scriere': 11482, 'cache_citire': 69235} tokeni, $0.1790, 44 s

Pe fond: **NU POT** — VERIFICAREA MECANICA a respins propunerea modelului: cifra '112' din raspuns nu apare literal in citate sau in intrebare

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> INCOMPLET: intrebarea nu da faptele de care depinde raspunsul: Dacă angajatorul este un plătitor de venituri din salarii dintre cei prevăzuți la art. 80 alin. (2) (care depun declarația trimestrial) sau un plătitor obligat la depunere lunară; Dacă în cursul trimestrului au intervenit concedii/indemnizații de asigurări sociale de sănătate sau încetarea calității de asigurat (situație care schimbă termenul de depunere pentru plătitorii trimestriali); Temeiul privind termenul de plată a impozitului…

## Cheia

- D112, până la 25.09.2026 inclusiv; CAS și impozitul pe salarii se plătesc tot până la 25.09.2026. Excepție: angajatorii din CF art. 80 alin. (2) (ex. micro cu sub 3 salariați, ONG-uri, PFA/II) depun D112 trimestrial și plătesc până la 25 a lunii următoare trimestrului — pentru august (T3): 25.10.2026, duminică → efectiv 26.10.2026.
- temei: Cod fiscal art. 147 alin. (1) și (4); art. 146 alin. (3); art. 80 alin. (1)-(2); CPF art. 75
