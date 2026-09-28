# Q-PRF-08 — REGULA

**Întrebarea:** O SRL înregistrată la registrul comerțului pe 10 martie 2026 optează pentru impozit micro din primul an. În cât timp trebuie să angajeze salariatul și ce se întâmplă dacă nu o face?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 10.03.2026, pentru o persoană juridică română nou-înființată (SRL înregistrat la registrul comerțului pe 10.03.2026) care optează pentru impozitul pe veniturile microîntreprinderilor din primul an fiscal, presupunând că celelalte condiții de la art. 47 alin. (1) lit. d) și h) sunt îndeplinite la data înregistrării și că nu se încadrează în regimurile de excepție (fost impozit specific sau opțiunea cu capital social de 45.000 lei).*

> **Condiția de a avea cel puțin un salariat trebuie îndeplinită în termen de 90 de zile inclusiv de la data înregistrării persoanei juridice. Dacă în acest termen nu se angajează salariatul, societatea datorează impozit pe profit începând cu trimestrul următor celui în care expiră perioada de 90 de zile.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 48 alin. (3)** — `cod_fiscal_227_2015_consolidat#art48/alin3` · valabil din 2026-02-25
  > iar cea prevăzută la lit. g) în termen de 90 de zile inclusiv de la data înregistrării persoanei juridice respective. În cazul în care, în acest termen, nu se îndeplinește condiția de la art. 47 alin. (1) lit. g) , microîntreprinderea datorează impozit pe profit începând cu trimestrul următor celui în care expiră perioada de 90 de zile.
- **Codul fiscal (Legea 227/2015) art. 47 alin. (1) lit. g)** — `cod_fiscal_227_2015_consolidat#art47/alin1/litg` · valabil din 2023-01-01
  > are cel puțin un salariat, cu excepția situației prevăzute la art. 48 alin. (3) ; ...
- derogare tratată: `og_16_2022_consolidat#artVI/alin2` — Excepție de la art. 47 alin. (1) rezervată contribuabililor care au aplicat impozitul specific (Legea nr. 170/2016) până la 31.12.2022; nu se aplică unei societăți nou-înființate în 2026.
- derogare tratată: `oug_25_2018#artI/pct3` — Excepție privind opțiunea microîntreprinderilor cu capital social subscris de cel puțin 45.000 lei și cel puțin 2 salariați de a trece la impozit pe profit; întrebarea nu descrie această situație, ci opțiunea pentru impozit micro din primul an.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art48/alin2^3` — Excepție de la art. 52 (ieșirea din sistem în cursul anului); cazul descris este al persoanei nou-înființate, guvernat de art. 48 alin. (3), nu de pierderea condiției în cursul anului prin încetarea raportului de muncă.

### Navigarea (8 pași, 5 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "microîntreprinderi"}
2. `cauta` {"interogare": "salariat în termen de 30 de zile microîntreprindere nou-înființată"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art48/alin3"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art52/alin3"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art47/alin1/litg"}
6. `deschide` {"id": "oug_8_2026#art20^1"}
7. `deschide` {"id": "og_16_2022_consolidat#artVI/alin2"}
8. `deschide` {"id": "oug_25_2018#artI/pct3"}

Apel: `claude-opus-5`, {'intrare': 10, 'iesire': 2849, 'cache_scriere': 7791, 'cache_citire': 43692} tokeni, $0.1418, 47 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Stratul semantic v3 (context dat de căutare) — RĂSPUNS, pe fond CORECT

> Condiția privind salariatul trebuie îndeplinită în termen de 90 de zile inclusiv de la data înregistrării persoanei juridice. Dacă în acest termen condiția nu este îndeplinită, societatea datorează impozit pe profit începând cu trimestrul următor celui în care expiră perioada de 90 de zile.

## Cheia

- În 90 de zile inclusiv de la înregistrare (nu 30, cum era înainte de OUG 8/2026); dacă nu, datorează impozit pe profit începând cu trimestrul următor celui în care expiră cele 90 de zile (termenul expiră 08.06.2026, trim. II → impozit pe profit din trim. III 2026)
- temei: Cod fiscal art. 48 alin. (3), modificat de OUG 8/2026 art. 6 pct. 18, în vigoare 25.02.2026; art. 47 alin. (1) lit. g); art. 51 alin. (4) (definiția salariatului)
