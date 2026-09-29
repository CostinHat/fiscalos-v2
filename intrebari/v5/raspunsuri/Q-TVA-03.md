# Q-TVA-03 — REGULA

**Întrebarea:** O firmă neplătitoare de TVA (regim special de scutire) depășește plafonul de scutire pe 14.05.2026 printr-o factură emisă în acea zi. Până când trebuie să solicite înregistrarea în scopuri de TVA și de când aplică regimul normal de taxare?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 14.05.2026, pentru o persoană impozabilă cu sediul activității economice în România care aplica regimul special de scutire pentru întreprinderi mici și a cărei cifră de afaceri depășește plafonul de scutire printr-o factură emisă în 14.05.2026; presupun că nu este agricultor care aplică regimul special pentru agricultori și că operațiunile intră în cifra de afaceri de referință.*

Datele din întrebare: 2026-05-14 · data de referință aleasă: **2026-05-14** — Singura dată din întrebare; este ziua depășirii plafonului, la care se raportează atât termenul de înregistrare, cât și aplicarea regimului normal de taxare.

> **Trebuie să solicite înregistrarea în scopuri de TVA cel târziu la data depășirii plafonului, adică cel târziu pe 14.05.2026. Regimul normal de taxare se aplică din data depășirii plafonului, adică din 14.05.2026, începând chiar cu tranzacția (factura) care a condus la depășire; opțional, poate aplica regimul normal de taxare și pentru operațiunile realizate în aceeași zi, anterioare tranzacției care a condus la depășire.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 310 alin. (6)** — `cod_fiscal_227_2015_consolidat#art310/alin6` · valabil din 2025-09-01
  > trebuie să solicite înregistrarea în scopuri de TVA, conform art. 316 , cel târziu la data depășirii plafonului. Regimul normal de taxare se aplică din data depășirii plafonului prevăzut la alin. (1) , începând cu tranzacția care conduce la depășirea plafonului.
- **Codul fiscal (Legea 227/2015) art. 310 alin. (6)** — `cod_fiscal_227_2015_consolidat#art310/alin6` · valabil din 2025-09-01
  > Persoana impozabilă poate aplica regimul normal de taxare și pentru operațiunile anterioare tranzacției care a condus la depășirea plafonului de scutire, realizate în data în care plafonul de scutire este depășit.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art315^1/alin4/litc` — Excepția privește exclusiv agricultorii care aplică regimul special pentru agricultori, pentru operațiunile prevăzute la art. 315^1 alin. (1) lit. c) și d); firma din întrebare nu este în această situație, deci regula generală se aplică integral.

### Navigarea (4 pași, 5 ture, 1 reîncercare C23)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "regimul special de scutire pentru întreprinderile mici"}
2. `cauta` {"interogare": "depășirea plafonului de scutire solicita înregistrarea în scopuri de TVA 10 zile"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art310/alin6"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art315^1/alin4/litc"}

Apel: `claude-opus-5`, {'intrare': 10, 'iesire': 3215, 'cache_scriere': 8105, 'cache_citire': 53613} tokeni, $0.1579, 54 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — NU POT, pe fond NU POT

> VERIFICAREA MECANICA a respins propunerea modelului: nicio citare; raspuns gol

## Cheia

- Cel târziu la data depășirii plafonului (14.05.2026); regimul normal se aplică din data depășirii, începând cu tranzacția care a condus la depășire (opțional și pentru operațiunile anterioare din aceeași zi)
- temei: Cod fiscal art. 310 alin. (6), forma modificată de OG 22/2025 art. I pct. 11, în vigoare de la 01.09.2025
