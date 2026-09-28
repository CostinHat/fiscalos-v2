# Q-TVA-05 — CAPCANA

**Întrebarea:** O firmă în regim special de scutire are în 2026 venituri din servicii de 300.000 lei și vinde în același an un utilaj (mijloc fix) cu 120.000 lei. A depășit plafonul de scutire de 395.000 lei?

## Stratul semantic (motorul nou) — RĂSPUNS

*La data de referință 28.09.2026, presupun o persoană impozabilă stabilită în România care aplică regimul special de scutire pentru întreprinderi mici prevăzut de art. 310 Cod fiscal, cu plafonul de scutire de 395.000 lei indicat în întrebare, iar utilajul vândut este un activ fix corporal al firmei; presupun că nu există alte operațiuni care să intre în cifra de afaceri în afara celor menționate.*

> **Nu. Vânzarea utilajului (activ fix corporal) nu se cuprinde în cifra de afaceri de referință pentru plafonul de scutire, astfel că se ia în calcul doar suma de 300.000 lei din servicii, care rămâne sub plafonul de 395.000 lei. Firma poate continua regimul special de scutire.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 310 alin. (2)** — `cod_fiscal_227_2015_consolidat#art310/alin2` · valabil din 2025-09-01
  > Prin excepție, nu se cuprind în cifra de afaceri prevăzută la alin. (1) livrările de active fixe corporale, astfel cum sunt definite la art. 266 alin. (1) pct. 3 , și cesiunea/transferul de active necorporale, efectuate de persoana impozabilă.
- **Codul fiscal (Legea 227/2015) art. 310 alin. (2)** — `cod_fiscal_227_2015_consolidat#art310/alin2` · valabil din 2025-09-01
  > Cifra de afaceri care servește drept referință pentru aplicarea alin. (1) este constituită din valoarea totală, exclusiv taxa în situația persoanelor impozabile care solicită scoaterea din evidența persoanelor înregistrate în scopuri de TVA, a livrărilor de bunuri și a prestărilor de servicii efectuate de persoana impozabilă în cursul unui an calendaristic
- **Codul fiscal (Legea 227/2015) art. 310 alin. (3)** — `cod_fiscal_227_2015_consolidat#art310/alin3` · valabil din 2025-09-01
  > nu au depășit plafonul de 395.000 lei, calculat conform art. 310 alin. (2) din Legea nr. 227/2015 , cu modificările și completările ulterioare.
- **Codul fiscal (Legea 227/2015) art. 310 alin. (6)** — `cod_fiscal_227_2015_consolidat#art310/alin6~2` · valabil din 2025-09-01
  > Persoana impozabilă care aplică regimul special de scutire și a cărei cifră de afaceri, prevăzută la alin. (2) , depășește plafonul de scutire prevăzut la alin. (1) trebuie să solicite înregistrarea în scopuri de TVA, conform art. 316 , cel târziu la data depășirii plafonului.

Apel: `claude-opus-5`, {'intrare': 4450, 'iesire': 1566, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0622, 22.6 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: D15: intrebarea cere o JUDECATA (Da/Nu) - aplicarea unei reguli la faptele date. Motorul nu compune si nu aplica reguli; atasez regula cea mai bine potrivita, ca material, nu ca raspuns.


Pe fond: **NU POT** — D15: intrebarea cere o JUDECATA (Da/Nu) - aplicarea unei reguli la faptele date. Motorul nu compune si nu aplica reguli; atasez regula cea mai bine potrivita, ca material, nu ca raspuns.

## Cheia

- răspuns așteptat: Nu. Livrările de active fixe corporale nu se cuprind în cifra de afaceri de referință; CA relevantă = 300.000 lei < 395.000 lei
- temei așteptat: Cod fiscal art. 310 alin. (2) teza finală, forma modificată de OG 22/2025 art. I pct. 11

