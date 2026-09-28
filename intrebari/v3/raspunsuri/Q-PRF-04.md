# Q-PRF-04 — CAPCANA

**Întrebarea:** O societate cu cifra de afaceri 2025 peste 50 mil. euro are în 2026: VT = 300.000.000 lei, Vs = 20.000.000 lei, I = 0, A = 10.000.000 lei; impozitul pe profit anual calculat (fără sponsorizări sau alte sume de scăzut) = 1.000.000 lei. Cât impozit pe profit datorează pentru 2026?

## Stratul semantic — NU POT RĂSPUNDE

*La data de referință 31.12.2025, pentru anul fiscal 2026, presupun o persoană juridică română plătitoare de impozit pe profit, nefinanciară (nu instituție de credit), cu cifra de afaceri în anul precedent peste 50.000.000 euro, fără credit fiscal extern, scutiri sau sponsorizări de scăzut.*

Motiv: modelul s-a abţinut: Atomii primiți nu conțin regula de determinare a impozitului minim pe cifra de afaceri (formula cu VT, Vs, I, A și cota aplicabilă, prevăzute la art. 18^1 alin. (3)); art. 18^1 alin. (1) doar face trimitere la alin. (3), care lipsește din context. În plus, stabilirea sumei ar presupune un calcul (scăderi și aplicarea unei cote) al cărui rezultat nu apare literal în niciun atom, ceea ce nu îmi este permis.

- **Codul fiscal (Legea 227/2015) art. 18^1 alin. (1)** — `cod_fiscal_227_2015_consolidat#art18^1/alin1` · valabil din nedovedit
  > mai mic decât impozitul minim pe cifra de afaceri stabilit potrivit prevederilor alin. (3) , sunt obligați la plata impozitului pe profit la nivelul impozitului minim pe cifra de afaceri.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art46^1/alin1/litb` — Regula specială privind impozitul pe cifra de afaceri de 4% pentru perioada 1 ianuarie 2026-31 decembrie 2026 se aplică doar instituțiilor de credit; societatea din întrebare nu este instituție de credit, deci nu se aplică.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art46^1/alin1/litc` — Excepția pentru instituțiile de credit cu cotă de piață mai mică de 0,2% nu se aplică, contribuabilul din speță nefiind instituție de credit sau sucursală a unei instituții de credit.

Apel: `claude-opus-5`, {'intrare': 5614, 'iesire': 1369, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0633

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți nu conțin regula de determinare a impozitului minim pe cifra de afaceri (formula cu VT, Vs, I, A și cota aplicabilă, prevăzute la art. 18^1 alin. (3)); art. 18^1 al

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2025-12-31 (an, din "2025"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: D15: intrebarea cere un fapt a carui forma motorul nu o recunoaste; nu pot verifica ca un fragment extras raspunde la ce s-a intrebat. Atasez regula cea mai bine potrivita, ca material, nu ca raspuns.


Pe fond: **NU POT** — D15: intrebarea cere un fapt a carui forma motorul nu o recunoaste; nu pot verifica ca un fragment extras raspunde la ce s-a intrebat. Atasez regula cea mai bine potrivita, ca material, nu ca raspuns.

## Cheia

- 1.350.000 lei — IMCA = 0,5% × (300.000.000 − 20.000.000 − 0 − 10.000.000) = 1.350.000 > 1.000.000, deci plătește la nivelul IMCA (nu 1%, care ar da 2.700.000)
- temei: Cod fiscal art. 18^1 alin. (1) și (3); alin. (16) (cota 0,5% pentru anul fiscal 2026, introdus de OUG 89/2025 art. I pct. 1); alin. (17) (articolul se aplică până la 31.12.2026)
