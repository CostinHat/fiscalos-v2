# Q-PRF-04 — CAPCANA

**Întrebarea:** O societate cu cifra de afaceri 2025 peste 50 mil. euro are în 2026: VT = 300.000.000 lei, Vs = 20.000.000 lei, I = 0, A = 10.000.000 lei; impozitul pe profit anual calculat (fără sponsorizări sau alte sume de scăzut) = 1.000.000 lei. Cât impozit pe profit datorează pentru 2026?

## Stratul semantic (motorul nou) — NU POT RĂSPUNDE

*La data de referință 31.12.2025, presupun un contribuabil plătitor de impozit pe profit, altul decât cei de la art. 15, cu cifră de afaceri în anul precedent peste 50.000.000 euro, care în 2026 ar intra în sfera impozitului minim pe cifra de afaceri, fără regimuri speciale (nu instituție de credit) și fără credit fiscal extern sau sponsorizări.*

Motiv: modelul s-a abţinut: Răspunsul ar presupune determinarea impozitului minim pe cifra de afaceri pornind de la indicatorii VT, Vs, I și A și compararea lui cu impozitul pe profit de 1.000.000 lei, adică un calcul (scădere și aplicare de cotă) al cărui rezultat nu apare literal în niciun atom. În plus, atomii primiți nu conțin textul art. 18^1 alin. (3) cu formula și cota aplicabilă impozitului minim pe cifra de afaceri, la care face trimitere alin. (1), deci baza legală a calculului lipsește din materialul furnizat.

- **Codul fiscal (Legea 227/2015) art. 18^1 alin. (1)** — `cod_fiscal_227_2015_consolidat#art18^1/alin1` · valabil din nedovedit
  > care în anul de calcul determină un impozit pe profit, cumulat de la începutul anului fiscal/anului fiscal modificat până la sfârșitul trimestrului/anului de calcul, mai mic decât impozitul minim pe cifra de afaceri stabilit potrivit prevederilor alin. (3) , sunt obligați la plata impozitului pe profit la nivelul impozitului minim pe cifra de afaceri.

Apel: `claude-opus-5`, {'intrare': 4342, 'iesire': 1248, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0537, 16.6 s

Pe fond: **NU POT** — modelul s-a abţinut: Răspunsul ar presupune determinarea impozitului minim pe cifra de afaceri pornind de la indicatorii VT, Vs, I și A și compararea lui cu impozitul pe profit de 1.000.000 lei, adică

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2025-12-31 (an, din "2025"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: D15: intrebarea cere un fapt a carui forma motorul nu o recunoaste; nu pot verifica ca un fragment extras raspunde la ce s-a intrebat. Atasez regula cea mai bine potrivita, ca material, nu ca raspuns.


Pe fond: **NU POT** — D15: intrebarea cere un fapt a carui forma motorul nu o recunoaste; nu pot verifica ca un fragment extras raspunde la ce s-a intrebat. Atasez regula cea mai bine potrivita, ca material, nu ca raspuns.

## Cheia

- răspuns așteptat: 1.350.000 lei — IMCA = 0,5% × (300.000.000 − 20.000.000 − 0 − 10.000.000) = 1.350.000 > 1.000.000, deci plătește la nivelul IMCA (nu 1%, care ar da 2.700.000)
- temei așteptat: Cod fiscal art. 18^1 alin. (1) și (3); alin. (16) (cota 0,5% pentru anul fiscal 2026, introdus de OUG 89/2025 art. I pct. 1); alin. (17) (articolul se aplică până la 31.12.2026)

