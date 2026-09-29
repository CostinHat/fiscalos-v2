# Q-PRF-08 — REGULA

**Întrebarea:** O SRL înregistrată la registrul comerțului pe 10 martie 2026 optează pentru impozit micro din primul an. În cât timp trebuie să angajeze salariatul și ce se întâmplă dacă nu o face?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 10.03.2026, presupun o persoană juridică română nou-înființată (SRL) înregistrată la registrul comerțului la 10.03.2026, care optează să plătească impozit pe veniturile microîntreprinderilor începând cu primul an fiscal și care îndeplinește la data înregistrării celelalte condiții (art. 47 alin. (1) lit. d) și h)), întrebarea privind exclusiv condiția de a avea cel puțin un salariat.*

Datele din întrebare: 2026-03-10 · data de referință aleasă: **2026-03-10** — Singura dată din întrebare; faptul întrebat (termenul de angajare) curge de la data înregistrării în registrul comerțului, 10 martie 2026.

> **Condiția de a avea cel puțin un salariat trebuie îndeplinită în termen de 90 de zile inclusiv de la data înregistrării persoanei juridice (data înregistrării în registrul comerțului). Dacă în acest termen nu angajează salariatul, societatea pierde regimul micro și datorează impozit pe profit începând cu trimestrul următor celui în care expiră perioada de 90 de zile.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 48 alin. (3)** — `cod_fiscal_227_2015_consolidat#art48/alin3` · valabil din 2026-02-25
  > iar cea prevăzută la lit. g) în termen de 90 de zile inclusiv de la data înregistrării persoanei juridice respective. În cazul în care, în acest termen, nu se îndeplinește condiția de la art. 47 alin. (1) lit. g) , microîntreprinderea datorează impozit pe profit începând cu trimestrul următor celui în care expiră perioada de 90 de zile.
- **Codul fiscal (Legea 227/2015) art. 47 alin. (1) lit. g)** — `cod_fiscal_227_2015_consolidat#art47/alin1/litg` · valabil din 2023-01-01
  > are cel puțin un salariat, cu excepția situației prevăzute la art. 48 alin. (3) ; ...
- derogare tratată: `og_16_2022_consolidat#artVI/alin2` — Excepție de la art. 47 alin. (1) aplicabilă doar contribuabililor care au fost sub incidența Legii nr. 170/2016 (impozit specific HoReCa) până la 31.12.2022; nu se aplică unei societăți înființate la 10.03.2026.
- derogare tratată: `oug_25_2018#artI/pct3` — Excepție privind microîntreprinderile cu capital social subscris de cel puțin 45.000 lei și cel puțin 2 salariați, care pot opta pentru impozit pe profit; cazul din întrebare vizează opțiunea pentru impozit micro cu un salariat, deci nu se aplică.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art48/alin2^3` — Este excepție de la art. 52 (ieșirea în cursul anului), nu de la art. 48 alin. (3) care guvernează termenul pentru societatea nou-înființată; nu afectează termenul de 90 de zile.

### Navigarea (8 pași, 5 ture)

1. `cauta` {"interogare": "microîntreprindere nou-înființată termen de 30 de zile angajare salariat"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "microîntreprinderi"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art48/alin3"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art52/alin3"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art47/alin1/litg"}
6. `deschide` {"id": "oug_8_2026#art20^1/alin3~2"}
7. `deschide` {"id": "og_16_2022_consolidat#artVI/alin2"}
8. `deschide` {"id": "oug_25_2018#artI/pct3"}

Apel: `claude-opus-5`, {'intrare': 10, 'iesire': 3335, 'cache_scriere': 6836, 'cache_citire': 46968} tokeni, $0.1496, 55 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond CORECT

> Condiția de a avea cel puțin un salariat trebuie îndeplinită în termen de 90 de zile inclusiv de la data înregistrării persoanei juridice. Dacă în acest termen nu se angajează salariatul, societatea datorează impozit pe profit începând cu trimestrul următor celui în care expiră perioada de 90 de zile.

## Cheia

- În 90 de zile inclusiv de la înregistrare (nu 30, cum era înainte de OUG 8/2026); dacă nu, datorează impozit pe profit începând cu trimestrul următor celui în care expiră cele 90 de zile (termenul expiră 08.06.2026, trim. II → impozit pe profit din trim. III 2026)
- temei: Cod fiscal art. 48 alin. (3), modificat de OUG 8/2026 art. 6 pct. 18, în vigoare 25.02.2026; art. 47 alin. (1) lit. g); art. 51 alin. (4) (definiția salariatului)
