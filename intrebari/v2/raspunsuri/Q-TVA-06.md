# Q-TVA-06 — CAPCANA

**Întrebarea:** O firmă cu perioadă fiscală trimestrială face o livrare intracomunitară scutită în februarie 2026. Depune D390 trimestrial, odată cu D300 din aprilie?

## Stratul semantic (motorul nou) — NU POT RĂSPUNDE

*La data de referință 2026-02-28, pentru o persoană impozabilă înregistrată în scopuri de TVA în România cu perioadă fiscală trimestrială, care efectuează în februarie 2026 o livrare intracomunitară scutită conform art. 294 alin. (2), presupun că întrebarea vizează termenul și periodicitatea de depunere a declarației recapitulative (D390).*

Motiv: modelul s-a abţinut: Atomii primiți nu conțin norma care reglementează periodicitatea și termenul de depunere a declarației recapitulative (D390). Singurul atom privind un termen de depunere corelat cu perioada decontului (lunar/trimestrial) se referă la declarația informativă privind livrările/prestările și achizițiile pe teritoriul național (D394), nu la declarația recapitulativă. Atomul din normele metodologice menționează doar, într-un exemplu cu perioadă lunară, includerea livrării în declarația recapitulativă aferentă unei luni, fără a stabili regula de periodicitate aplicabilă unui cont…


Apel: `claude-opus-5`, {'intrare': 5419, 'iesire': 777, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0473, 14.1 s

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți nu conțin norma care reglementează periodicitatea și termenul de depunere a declarației recapitulative (D390). Singurul atom privind un termen de depunere corelat c

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-02-28 (luna, din "februarie 2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: D15: intrebarea cere o JUDECATA (Da/Nu) - aplicarea unei reguli la faptele date. Motorul nu compune si nu aplica reguli; atasez regula cea mai bine potrivita, ca material, nu ca raspuns.


Pe fond: **NU POT** — D15: intrebarea cere o JUDECATA (Da/Nu) - aplicarea unei reguli la faptele date. Motorul nu compune si nu aplica reguli; atasez regula cea mai bine potrivita, ca material, nu ca raspuns.

## Cheia

- răspuns așteptat: Nu. D390 se depune lunar, pentru luna în care a luat naștere exigibilitatea, nu trimestrial cu D300. Exigibilitatea la livrarea intracomunitară = data facturii sau, dacă factura nu s-a emis până atunci, 15 a lunii următoare faptului generator. Factură emisă în februarie → D390 pentru februarie, până la 25.03.2026. Fără factură până la 15.03.2026 → D390 pentru martie, termen 25.04.2026 (sâmbătă), efectiv 27.04.2026.
- temei așteptat: Cod fiscal art. 283 alin. (1); art. 325 alin. (1) lit. a) și alin. (2); OPANAF 705/2020 anexa 2 pct. 1.1-1.2; CPF art. 75

