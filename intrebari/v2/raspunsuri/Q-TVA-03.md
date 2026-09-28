# Q-TVA-03 — REGULA

**Întrebarea:** O firmă neplătitoare de TVA (regim special de scutire) depășește plafonul de scutire pe 14.05.2026 printr-o factură emisă în acea zi. Până când trebuie să solicite înregistrarea în scopuri de TVA și de când aplică regimul normal de taxare?

## Stratul semantic (motorul nou) — RĂSPUNS

*La data de referință 14.05.2026, presupun o persoană impozabilă cu sediul activității economice în România, care aplica regimul special de scutire pentru întreprinderi mici și a depășit plafonul de scutire prin factura emisă la 14.05.2026, iar întrebarea nu precizează alte operațiuni, deci mă limitez la regula generală de depășire a plafonului.*

> **Trebuie să solicite înregistrarea în scopuri de TVA cel târziu la data depășirii plafonului, adică cel târziu pe 14.05.2026. Regimul normal de taxare se aplică din data depășirii plafonului, începând cu tranzacția care a condus la depășire (factura din 14.05.2026); opțional, poate aplica regimul normal și pentru operațiunile anterioare acelei tranzacții, realizate în aceeași zi.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 310 alin. (6)** — `cod_fiscal_227_2015_consolidat#art310/alin6~2` · valabil din 2025-09-01
  > trebuie să solicite înregistrarea în scopuri de TVA, conform art. 316 , cel târziu la data depășirii plafonului. Regimul normal de taxare se aplică din data depășirii plafonului prevăzut la alin. (1) , începând cu tranzacția care conduce la depășirea plafonului.
- **Codul fiscal (Legea 227/2015) art. 310 alin. (6)** — `cod_fiscal_227_2015_consolidat#art310/alin6~2` · valabil din 2025-09-01
  > Persoana impozabilă poate aplica regimul normal de taxare și pentru operațiunile anterioare tranzacției care a condus la depășirea plafonului de scutire, realizate în data în care plafonul de scutire este depășit.
- **Codul fiscal (Legea 227/2015) art. 316 alin. (1) lit. b)** — `cod_fiscal_227_2015_consolidat#art316/alin1/litb` · valabil din nedovedit
  > dacă în cursul unui an calendaristic depășește plafonul de scutire prevăzut la art. 310 alin. (1) , cel târziu la data depășirii plafonului; ...

Apel: `claude-opus-5`, {'intrare': 5634, 'iesire': 1055, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0553, 15.0 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-05-14 (zi, din "14.05.2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **Dacă în luna august 2025 a fost depășit și plafonul de 395.000 lei, persoana impozabilă trebuie să solicite înregistrarea în scopuri de TVA cel târziu în data de 10 septembrie 2025 și să aplice regimul normal de taxare începând cu această dată.**

Motiv: D15: fraza care conţine un fapt de forma cerută (suma) si potriveste cel mai bine intrebarea (scor local 32.2)

- **Codul fiscal (Legea 227/2015) art. 310 alin. (2)** — `cod_fiscal_227_2015_consolidat#art310/alin2` · valabil din 2025-09-01
  > …l III (1) Persoanele impozabile care au depășit în luna august 2025 plafonul de scutire pentru întreprinderile mici de 300.000 de lei, calculat potrivit prevederilor art. 310 alin. (2) din Legea nr. 227/2015 , cu modificările și completările ulterioare, în vigoare la data depășirii plafonului, nu trebuie să solicite înregistrarea în scopuri de TVA decât la depășirea plafonului anual de scutire de 395.000 lei, calculat conform art. 310 alin. (2) din Legea nr. 227/2015 , cu modificările și completările ulterioare. Dacă în luna august 2025 a fost depășit și plafonul de 395.000 lei, persoana impo…

Pe fond: **GREȘIT** — faptul principal al cheii (['14.05.2026']) nu e in raspuns

## Cheia

- răspuns așteptat: Cel târziu la data depășirii plafonului (14.05.2026); regimul normal se aplică din data depășirii, începând cu tranzacția care a condus la depășire (opțional și pentru operațiunile anterioare din aceeași zi)
- temei așteptat: Cod fiscal art. 310 alin. (6), forma modificată de OG 22/2025 art. I pct. 11, în vigoare de la 01.09.2025

