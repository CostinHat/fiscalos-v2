# Q-TVA-03 — REGULA

**Întrebarea:** O firmă neplătitoare de TVA (regim special de scutire) depășește plafonul de scutire pe 14.05.2026 printr-o factură emisă în acea zi. Până când trebuie să solicite înregistrarea în scopuri de TVA și de când aplică regimul normal de taxare?

## Stratul semantic — RĂSPUNS

*La data de referință 14.05.2026, presupun o persoană impozabilă stabilită în România, care aplică regimul special de scutire pentru întreprinderi mici și a cărei cifră de afaceri depășește plafonul de scutire printr-o tranzacție (factură) emisă în 14.05.2026, fără a fi vorba de situația tranzitorie a depășirii plafonului în luna august 2025.*

> **Firma trebuie să solicite înregistrarea în scopuri de TVA cel târziu la data depășirii plafonului, adică cel târziu în 14.05.2026. Regimul normal de taxare se aplică din data depășirii plafonului, adică din 14.05.2026, începând chiar cu tranzacția (factura) care conduce la depășirea plafonului. Opțional, poate aplica regimul normal de taxare și pentru operațiunile anterioare acelei tranzacții, realizate în aceeași zi (14.05.2026).**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. III alin. (6)** — `cod_fiscal_227_2015_consolidat#artIII~2/alin6~2` · valabil din 2025-09-01
  > trebuie să solicite înregistrarea în scopuri de TVA, conform art. 316 , cel târziu la data depășirii plafonului. Regimul normal de taxare se aplică din data depășirii plafonului prevăzut la alin. (1) , începând cu tranzacția care conduce la depășirea plafonului.
- **Codul fiscal (Legea 227/2015) art. III alin. (6)** — `cod_fiscal_227_2015_consolidat#artIII~2/alin6~2` · valabil din 2025-09-01
  > Persoana impozabilă poate aplica regimul normal de taxare și pentru operațiunile anterioare tranzacției care a condus la depășirea plafonului de scutire, realizate în data în care plafonul de scutire este depășit.
- derogare tratată: `cod_fiscal_227_2015_consolidat#artIII~2/alin1` — Regula tranzitorie privind depășirea plafonului de 300.000 lei/395.000 lei în luna august 2025 (cu termen 10 septembrie 2025) nu se aplică în cazul din întrebare, unde depășirea plafonului are loc la 14.05.2026.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art310^2/alin5` — Excepția de la obligația de înregistrare vizează persoana impozabilă care aplică regimul transfrontalier de scutire prevăzut la art. 310^2 și care rămâne sub plafon; în speță plafonul este depășit, deci obligația de solicitare a înregistrării subzistă.

Apel: `claude-opus-5`, {'intrare': 3490, 'iesire': 1630, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0592

Pe fond: **GREȘIT** — articolul citat [('cf', 'III')] nu e printre cele ale cheii [('cf', '310'), ('cf', 'I')]

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-05-14 (zi, din "14.05.2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **Dacă în luna august 2025 a fost depășit și plafonul de 395.000 lei, persoana impozabilă trebuie să solicite înregistrarea în scopuri de TVA cel târziu în data de 10 septembrie 2025 și să aplice regimul normal de taxare începând cu această dată.**

Motiv: D15: fraza care conţine un fapt de forma cerută (suma) si potriveste cel mai bine intrebarea (scor local 32.5)

- **Codul fiscal (Legea 227/2015) art. III alin. (1)** — `cod_fiscal_227_2015_consolidat#artIII~2/alin1` · valabil din 2025-09-10
  > Persoanele impozabile care au depășit în luna august 2025 plafonul de scutire pentru întreprinderile mici de 300.000 de lei, calculat potrivit prevederilor art. 310 alin. (2) din Legea nr. 227/2015 , cu modificările și completările ulterioare, în vigoare la data depășirii plafonului, nu trebuie să solicite înregistrarea în scopuri de TVA decât la depășirea plafonului anual de scutire de 395.000 lei, calculat conform art. 310 alin. (2) din Legea nr. 227/2015 , cu modificările și completările ulte…

Pe fond: **GREȘIT** — faptul principal al cheii (['14.05.2026']) nu e in raspuns; articolul citat [('cf', 'III')] nu e printre cele ale cheii [('cf', '310'), ('cf', 'I')]

## Cheia

- Cel târziu la data depășirii plafonului (14.05.2026); regimul normal se aplică din data depășirii, începând cu tranzacția care a condus la depășire (opțional și pentru operațiunile anterioare din aceeași zi)
- temei: Cod fiscal art. 310 alin. (6), forma modificată de OG 22/2025 art. I pct. 11, în vigoare de la 01.09.2025
