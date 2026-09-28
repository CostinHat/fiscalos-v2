# Q-CTB-07 — CALCUL

**Întrebarea:** SRL distribuie (hotărâre AGA) și plătește în 10 aprilie 2026 unui asociat persoană fizică rezidentă dividende brute de 50.000 lei. Cât impozit se reține, cât primește net și până când se virează?

## Stratul semantic (motorul nou) — NU POT RĂSPUNDE

*La data de referință 10 aprilie 2026, presupun o societate cu răspundere limitată persoană juridică română care plătește dividende unui asociat persoană fizică rezidentă în România, impozitul pe dividende fiind reținut la sursă de plătitor, iar întrebarea cere sume concrete (impozit reținut și sumă netă) pentru un dividend brut de 50.000 lei.*

Motiv: modelul s-a abţinut: Atomii primiți stabilesc cota de 16% aplicată sumei dividendelor, reținerea odată cu plata și termenul de virare până la data de 25 inclusiv a lunii următoare celei în care se face plata, însă cuantumul impozitului reținut și suma netă pentru un dividend brut de 50.000 lei, precum și data-limită concretă din luna următoare lunii aprilie 2026, rezultă doar dintr-un calcul (înmulțire, scădere, respectiv determinarea lunii următoare) care nu apare literal în niciun atom; conform regulilor, nu pot efectua acest calcul.

- **Codul fiscal (Legea 227/2015) art. 97 alin. (7)** — `cod_fiscal_227_2015_consolidat#art97/alin7` · valabil din 2025-08-01
  > Veniturile sub formă de dividende, inclusiv câștigul obținut ca urmare a deținerii de titluri de participare definite de legislația în materie la organisme de plasament colectiv, se impozitează cu o cotă de 16% din suma acestora, impozitul fiind final.
- **Codul fiscal (Legea 227/2015) art. 97 alin. (7)** — `cod_fiscal_227_2015_consolidat#art97/alin7` · valabil din 2025-08-01
  > Obligația calculării și reținerii impozitului pe veniturile sub formă de dividende revine persoanelor juridice, odată cu plata dividendelor/sumelor reprezentând câștigul obținut ca urmare a deținerii de titluri de participare de către acționari/ asociați/investitori. Termenul de virare a impozitului este până la data de 25 inclusiv a lunii următoare celei în care se face plata.

Apel: `claude-opus-5`, {'intrare': 4095, 'iesire': 1129, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0495, 14.7 s

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți stabilesc cota de 16% aplicată sumei dividendelor, reținerea odată cu plata și termenul de virare până la data de 25 inclusiv a lunii următoare celei în care se fac

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-04-10 (zi, din "10 aprilie 2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **50.000 lei x 16% = 8000,00 lei**

Motiv: R-CALC: o baza, o cota; baza x cota

- **Codul fiscal (Legea 227/2015) art. 43 alin. (2)** — `cod_fiscal_227_2015_consolidat#art43/alin2` · valabil din 2025-08-01
  > Impozitul pe dividende se stabilește prin aplicarea unei cote de impozit de 16% asupra dividendului brut plătit unei persoane juridice române. Impozitul pe dividende se declară și se plătește la bugetul de stat, până la data de 25 inclusiv a lunii următoare celei în care se plătește dividendul. Notă ... Litera a) a alineatului (1), articolul VII din LEGEA nr. 141 din 25 iulie 2025, publicată în MONITORUL OFICIAL nr. 699 din 25 iulie 2025 prevede:

Pe fond: **GREȘIT** — faptul principal al cheii (['8.000 lei']) nu e in raspuns; articolul citat [('cf', '43')] nu e printre cele ale cheii [('cf', '97'), ('cf', 'II'), ('cf', 'VII')]

## Cheia

- răspuns așteptat: Impozit 8.000 lei (16%, final); net 42.000 lei; virare până la 25 mai 2026 inclusiv (25 a lunii următoare plății). Dacă nu s-ar plăti până la sfârșitul anului aprobării, impozitul s-ar plăti până la 25 ianuarie a anului următor.
- temei așteptat: Legea 227/2015 art. 97 alin. (7), modificat de Legea 141/2025 art. II pct. 5, aplicabil dividendelor distribuite de la 01.01.2026 (Legea 141/2025 art. VII alin. (1) lit. c))

