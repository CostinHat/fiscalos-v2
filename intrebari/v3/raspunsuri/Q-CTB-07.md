# Q-CTB-07 — CALCUL

**Întrebarea:** SRL distribuie (hotărâre AGA) și plătește în 10 aprilie 2026 unui asociat persoană fizică rezidentă dividende brute de 50.000 lei. Cât impozit se reține, cât primește net și până când se virează?

## Stratul semantic — NU POT RĂSPUNDE

*La data de referință 2026-04-10, presupun un SRL român plătitor de dividende către un asociat persoană fizică rezidentă, dividende brute de 50.000 lei distribuite prin hotărâre AGA și efectiv plătite la 10 aprilie 2026, impozitul pe dividende fiind reținut la sursă de plătitor.*

Motiv: modelul s-a abţinut: Atomii primiți conțin cota de impozit (16%) și termenul de virare (până la data de 25 inclusiv a lunii următoare celei în care se face plata), dar cuantumul impozitului reținut și suma netă încasată de asociat rezultă dintr-un calcul (aplicarea cotei asupra dividendului brut de 50.000 lei și scăderea impozitului), iar aceste valori nu apar literal în niciun atom. Nu am voie să efectuez calculul, deci nu pot da răspunsul cerut în întregime.

- **Codul fiscal (Legea 227/2015) art. 97 alin. (7)** — `cod_fiscal_227_2015_consolidat#art97/alin7` · valabil din 2025-08-01
  > Veniturile sub formă de dividende, inclusiv câștigul obținut ca urmare a deținerii de titluri de participare definite de legislația în materie la organisme de plasament colectiv, se impozitează cu o cotă de 16% din suma acestora, impozitul fiind final.
- **Codul fiscal (Legea 227/2015) art. 97 alin. (7)** — `cod_fiscal_227_2015_consolidat#art97/alin7` · valabil din 2025-08-01
  > Termenul de virare a impozitului este până la data de 25 inclusiv a lunii următoare celei în care se face plata.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art43/alin3` — Excepția de la art. 43 alin. (3) (plata impozitului până la 25 ianuarie a anului următor) vizează dividendele distribuite și neplătite până la sfârșitul anului și regimul dividendelor plătite persoanelor juridice; în cazul din întrebare beneficiarul este persoană fizică rezidentă, iar dividendele au…

Apel: `claude-opus-5`, {'intrare': 4451, 'iesire': 1518, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0612

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți conțin cota de impozit (16%) și termenul de virare (până la data de 25 inclusiv a lunii următoare celei în care se face plata), dar cuantumul impozitului reținut și

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-04-10 (zi, din "10 aprilie 2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: C17 (b): atomul pe care as raspunde are 1 derogari/exceptii/modificari valabile la data intrebarii (ex. cod_fiscal_227_2015_consolidat#art43/alin3: "Prin excepție de la prevederile alin. (1) și (2)"); motorul lexical nu le poate trata, deci se abţine.

- **Codul fiscal (Legea 227/2015) art. 43 alin. (2)** — `cod_fiscal_227_2015_consolidat#art43/alin2` · valabil din 2025-08-01
  > Impozitul pe dividende se stabilește prin aplicarea unei cote de impozit de 16% asupra dividendului brut plătit unei persoane juridice române. Impozitul pe dividende se declară și se plătește la bugetul de stat, până la data de 25 inclusiv a lunii următoare celei în care se plătește dividendul. Notă ... Litera a) a alineatului (1), articolul VII din LEGEA nr. 141 din 25 iulie 2025, publicată în MONITORUL OFICIAL nr. 699 din 25 iulie 2025 prevede:

Pe fond: **NU POT** — C17 (b): atomul pe care as raspunde are 1 derogari/exceptii/modificari valabile la data intrebarii (ex. cod_fiscal_227_2015_consolidat#art43/alin3: "Prin excepție de la prevederile alin. (1) și (2)");

## Cheia

- Impozit 8.000 lei (16%, final); net 42.000 lei; virare până la 25 mai 2026 inclusiv (25 a lunii următoare plății). Dacă nu s-ar plăti până la sfârșitul anului aprobării, impozitul s-ar plăti până la 25 ianuarie a anului următor.
- temei: Legea 227/2015 art. 97 alin. (7), modificat de Legea 141/2025 art. II pct. 5, aplicabil dividendelor distribuite de la 01.01.2026 (Legea 141/2025 art. VII alin. (1) lit. c))
