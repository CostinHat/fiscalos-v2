# Q-TVA-05 — CAPCANA

**Întrebarea:** O firmă în regim special de scutire are în 2026 venituri din servicii de 300.000 lei și vinde în același an un utilaj (mijloc fix) cu 120.000 lei. A depășit plafonul de scutire de 395.000 lei?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 28.09.2026, presupun o persoană impozabilă stabilită în România care aplică regimul special de scutire pentru întreprinderi mici (TVA), cu operațiuni cu locul în România, iar utilajul vândut este o imobilizare corporală amortizabilă (activ corporal fix) folosită în activitatea firmei; presupun că nu aplică regimuri speciale de tip OSS pentru operațiunile în cauză.*

Datele din întrebare: 2026-09-28 · data de referință aleasă: **2026-09-28** — Faptul întrebat este depășirea plafonului de scutire în anul 2026, singura dată din întrebare fiind cea corespunzătoare anului 2026.

> **Nu. Livrarea utilajului (activ corporal fix) nu se cuprinde în cifra de afaceri de referință pentru regimul special de scutire, deci se iau în calcul doar veniturile din servicii de 300.000 lei, sub plafonul de 395.000 lei. Firma nu a depășit plafonul și poate rămâne în regimul special de scutire.**

Citatul decisiv (`cod_fiscal_227_2015_consolidat#art310/alin2`):
> Prin excepție, nu se cuprind în cifra de afaceri prevăzută la alin. (1) livrările de active fixe corporale, astfel cum sunt definite la art. 266 alin. (1) pct. 3 , și cesiunea/transferul de active necorporale, efectuate de persoana impozabilă.

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 310 alin. (2)** — `cod_fiscal_227_2015_consolidat#art310/alin2` · valabil din 2025-09-01
  > Prin excepție, nu se cuprind în cifra de afaceri prevăzută la alin. (1) livrările de active fixe corporale, astfel cum sunt definite la art. 266 alin. (1) pct. 3 , și cesiunea/transferul de active necorporale, efectuate de persoana impozabilă.
- **Codul fiscal (Legea 227/2015) art. 310 alin. (1)** — `cod_fiscal_227_2015_consolidat#art310/alin1` · valabil din 2025-09-01
  > Persoana impozabilă stabilită în România conform art. 266 alin. (2) lit. a) , a cărei cifră de afaceri anuală, declarată sau realizată, nu depășește plafonul de 395.000 lei, poate aplica scutirea de taxă, denumită în continuare regim special de scutire
- **Codul fiscal (Legea 227/2015) art. 266 alin. (1) pct. 3** — `cod_fiscal_227_2015_consolidat#art266/alin1/pct3` · valabil din nedovedit
  > active corporale fixe reprezintă orice imobilizare corporală amortizabilă, construcțiile și terenurile de orice fel, deținute pentru a fi utilizate în producția sau livrarea de bunuri ori în prestarea de servicii, pentru a fi închiriate terților sau pentru scopuri administrative
- **Codul fiscal (Legea 227/2015) art. 310 alin. (2)** — `cod_fiscal_227_2015_consolidat#art310/alin2` · valabil din 2025-09-01
  > Cifra de afaceri care servește drept referință pentru aplicarea alin. (1) este constituită din valoarea totală, exclusiv taxa în situația persoanelor impozabile care solicită scoaterea din evidența persoanelor înregistrate în scopuri de TVA, a livrărilor de bunuri și a prestărilor de servicii efectuate de persoana impozabilă în cursul unui an calendaristic
- derogare tratată: `cod_fiscal_227_2015_consolidat#art315^1/alin4/litc` — Excepția de la art. 310 privește operațiunile derulate în regimul special prevăzut la art. 315^1 alin. (1) lit. c) și d); firma din întrebare prestează servicii și livrează bunuri cu locul în România în regim special de scutire, fără indiciu că ar aplica acel regim special, deci excepția nu se aplic…

### Navigarea (6 pași, 5 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "întreprinderi mici"}
2. `cauta` {"interogare": "cifra de afaceri regim special scutire 395.000 lei livrări de active fixe"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art310/alin2"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art315^1/alin4/litc"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art310/alin1"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art266/alin1/pct3"}

Apel: `claude-opus-5`, {'intrare': 10, 'iesire': 2712, 'cache_scriere': 6845, 'cache_citire': 50357} tokeni, $0.1358, 50 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond CORECT

> Nu. Livrarea utilajului (activ fix corporal) nu se cuprinde în cifra de afaceri de referință, așa că la plafonul de 395.000 lei se compară numai cei 300.000 lei din servicii, deci plafonul nu a fost depășit și firma poate rămâne în regimul special de scutire.

## Cheia

- Nu. Livrările de active fixe corporale nu se cuprind în cifra de afaceri de referință; CA relevantă = 300.000 lei < 395.000 lei
- temei: Cod fiscal art. 310 alin. (2) teza finală, forma modificată de OG 22/2025 art. I pct. 11
