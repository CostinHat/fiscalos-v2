# Q-TVA-03 — REGULA

**Întrebarea:** O firmă neplătitoare de TVA (regim special de scutire) depășește plafonul de scutire pe 14.05.2026 printr-o factură emisă în acea zi. Până când trebuie să solicite înregistrarea în scopuri de TVA și de când aplică regimul normal de taxare?

## Stratul de navigare (v4) — NU POT RĂSPUNDE

*La data de referință 14.05.2026, presupun o persoană impozabilă cu sediul activității economice în România, care aplica regimul special de scutire pentru întreprinderi mici (art. 310 Cod fiscal), fără regim special pentru agricultori, și care depășește plafonul de scutire printr-o factură emisă în 14.05.2026.</declaratie>
<parameter name="raspuns">Trebuie să solicite înregistrarea în scopuri de TVA cel târziu la data depășirii plafonului, adică cel târziu la 14.05.2026. Regimul normal de taxare se aplică din data depășirii plafonului (14.05.2026), începând cu tranzacția care conduce la depășirea plafonului, adică cu factura emisă în acea zi; opțional, poate aplica regimul normal de taxare și pentru operațiunile anterioare acelei tranzacții, realizate în aceeași zi.</raspuns>
<parameter name="citate">[{"atom": "cod_fiscal_227_2015_consolidat#art310/alin6", "fragment": "trebuie să solicite înregistrarea în scopuri de TVA, conform art. 316 , cel târziu la data depășirii plafonului. Regimul normal de taxare se aplică din data depășirii plafonului prevăzut la alin. (1) , începând cu tranzacția care conduce la depășirea plafonului."}, {"atom": "cod_fiscal_227_2015_consolidat#art310/alin6", "fragment": "Persoana impozabilă poate aplica regimul normal de taxare și pentru operațiunile anterioare tranzacției care a condus la depășirea plafonului de scutire, realizate în data în care plafonul de scutire este depășit."}]</citate>
<parameter name="lipsa">[]*

Motiv: VERIFICAREA MECANICA a respins propunerea modelului: nicio citare; raspuns gol

- derogare tratată: `cod_fiscal_227_2015_consolidat#art315^1/alin4/litc` — Excepția privește persoanele care aplică regimul special pentru agricultori (art. 315^1), pentru operațiunile de la alin. (1) lit. c) și d); firma din întrebare nu aplică acest regim special, deci excepția nu schimbă regula de la art. 310 alin. (6).

### Navigarea (4 pași, 4 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "regim special de scutire"}
2. `cauta` {"interogare": "depășirea plafonului de scutire solicita înregistrarea în scopuri de TVA 10 zile"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art310/alin6"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art315^1/alin4/litc"}

Apel: `claude-opus-5`, {'intrare': 8, 'iesire': 1771, 'cache_scriere': 6385, 'cache_citire': 36591} tokeni, $0.1025, 30 s

Pe fond: **NU POT** — VERIFICAREA MECANICA a respins propunerea modelului: nicio citare; raspuns gol

## Stratul semantic v3 (context dat de căutare) — RĂSPUNS, pe fond GREȘIT

> Firma trebuie să solicite înregistrarea în scopuri de TVA cel târziu la data depășirii plafonului, adică cel târziu în 14.05.2026. Regimul normal de taxare se aplică din data depășirii plafonului, adică din 14.05.2026, începând chiar cu tranzacția (factura) care conduce la depășirea plafonului. Opțional, poate aplica regimul normal de taxare și pentru operațiunile anterioare acelei tranzacții, realizate în aceeași zi (14.05.2026).

## Cheia

- Cel târziu la data depășirii plafonului (14.05.2026); regimul normal se aplică din data depășirii, începând cu tranzacția care a condus la depășire (opțional și pentru operațiunile anterioare din aceeași zi)
- temei: Cod fiscal art. 310 alin. (6), forma modificată de OG 22/2025 art. I pct. 11, în vigoare de la 01.09.2025
