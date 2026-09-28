# Q-TVA-05 — CAPCANA

**Întrebarea:** O firmă în regim special de scutire are în 2026 venituri din servicii de 300.000 lei și vinde în același an un utilaj (mijloc fix) cu 120.000 lei. A depășit plafonul de scutire de 395.000 lei?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 28.09.2026, presupun o persoană impozabilă stabilită în România care aplică regimul special de scutire pentru întreprinderi mici (art. 310 Cod fiscal), cu operațiuni taxabile numai în România, iar utilajul vândut este un activ fix corporal al firmei; presupun că nu este agricultor care aplică regimul special pentru agricultori și că nu are alte operațiuni în afara celor menționate.*

> **Nu. Livrarea utilajului (activ fix corporal) nu se cuprinde în cifra de afaceri de referință, așa că la plafonul de 395.000 lei se compară numai cei 300.000 lei din servicii, deci plafonul nu a fost depășit și firma poate rămâne în regimul special de scutire.**

Citatul decisiv (`cod_fiscal_227_2015_consolidat#art310/alin2`):
> Prin excepție, nu se cuprind în cifra de afaceri prevăzută la alin. (1) livrările de active fixe corporale, astfel cum sunt definite la art. 266 alin. (1) pct. 3 , și cesiunea/transferul de active necorporale, efectuate de persoana impozabilă.

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 310 alin. (2)** — `cod_fiscal_227_2015_consolidat#art310/alin2` · valabil din 2025-09-01
  > Prin excepție, nu se cuprind în cifra de afaceri prevăzută la alin. (1) livrările de active fixe corporale, astfel cum sunt definite la art. 266 alin. (1) pct. 3 , și cesiunea/transferul de active necorporale, efectuate de persoana impozabilă.
- **Codul fiscal (Legea 227/2015) art. 310 alin. (1)** — `cod_fiscal_227_2015_consolidat#art310/alin1` · valabil din 2025-09-01
  > a cărei cifră de afaceri anuală, declarată sau realizată, nu depășește plafonul de 395.000 lei, poate aplica scutirea de taxă, denumită în continuare regim special de scutire, pentru operațiunile prevăzute la art. 268 alin. (1)
- **Codul fiscal (Legea 227/2015) art. 310 alin. (2)** — `cod_fiscal_227_2015_consolidat#art310/alin2` · valabil din 2025-09-01
  > Cifra de afaceri care servește drept referință pentru aplicarea alin. (1) este constituită din valoarea totală, exclusiv taxa în situația persoanelor impozabile care solicită scoaterea din evidența persoanelor înregistrate în scopuri de TVA, a livrărilor de bunuri și a prestărilor de servicii efectuate de persoana impozabilă în cursul unui an calendaristic
- derogare tratată: `cod_fiscal_227_2015_consolidat#art315^1/alin4/litc` — Excepția de la art. 310 vizează persoanele impozabile care aplică regimul special pentru agricultori (art. 315^1), pentru operațiunile prevăzute la alin. (1) lit. c) și d); firma din întrebare prestează servicii și vinde un utilaj, nefiind agricultor în regimul special, deci excepția nu se aplică.

### Navigarea (6 pași, 5 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "regim special scutire întreprinderi mici"}
2. `cauta` {"interogare": "plafon 395.000 lei cifra de afaceri regim special de scutire active fixe corporale"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art310/alin2"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art310/alin1"}
5. `cauta` {"interogare": "art. 266 alin. (1) pct. 3 active corporale fixe definiție mijloace fixe amortizabile"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art266/alin1/pct3"}

Apel: `claude-opus-5`, {'intrare': 10, 'iesire': 2825, 'cache_scriere': 9556, 'cache_citire': 53717} tokeni, $0.1573, 43 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți conțin plafonul de scutire, dar nu conțin regula care definește modul de calcul al cifrei de afaceri de referință pentru regimul special de scutire (dacă livrările de active corporale fixe, cum este utilajul, se includ sau se exclud din acest plafon). În plus, stabilirea depășirii ar presupune un calcul (însumarea veniturilor din servicii cu prețul utilajului), iar rezultatul acestui calcul nu apare literal în niciun atom. Prin urmare nu pot stabili pe baza at…

## Cheia

- Nu. Livrările de active fixe corporale nu se cuprind în cifra de afaceri de referință; CA relevantă = 300.000 lei < 395.000 lei
- temei: Cod fiscal art. 310 alin. (2) teza finală, forma modificată de OG 22/2025 art. I pct. 11
