# Q-PRF-08 — REGULA

**Întrebarea:** O SRL înregistrată la registrul comerțului pe 10 martie 2026 optează pentru impozit micro din primul an. În cât timp trebuie să angajeze salariatul și ce se întâmplă dacă nu o face?

## Stratul semantic — RĂSPUNS

*La data de referință 10.03.2026, presupun o persoană juridică română nou-înființată (SRL înregistrată la registrul comerțului la 10 martie 2026) care optează pentru plata impozitului pe veniturile microîntreprinderilor începând cu primul an fiscal și care îndeplinea la data înregistrării celelalte condiții de încadrare, întrebarea vizând exclusiv condiția privind deținerea unui salariat.*

> **Condiția privind salariatul trebuie îndeplinită în termen de 90 de zile inclusiv de la data înregistrării persoanei juridice. Dacă în acest termen condiția nu este îndeplinită, societatea datorează impozit pe profit începând cu trimestrul următor celui în care expiră perioada de 90 de zile.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 48 alin. (3)** — `cod_fiscal_227_2015_consolidat#art48/alin3` · valabil din 2026-02-25
  > iar cea prevăzută la lit. g) în termen de 90 de zile inclusiv de la data înregistrării persoanei juridice respective. În cazul în care, în acest termen, nu se îndeplinește condiția de la art. 47 alin. (1) lit. g) , microîntreprinderea datorează impozit pe profit începând cu trimestrul următor celui în care expiră perioada de 90 de zile.
- **Codul fiscal (Legea 227/2015) art. 48 alin. (3)** — `cod_fiscal_227_2015_consolidat#art48/alin3` · valabil din 2026-02-25
  > O persoană juridică română care este nou-înființată poate opta să plătească impozit pe veniturile microîntreprinderilor începând cu primul an fiscal, dacă condițiile prevăzute la art. 47 alin. (1) lit. d) și h) sunt îndeplinite la data înregistrării în registrul comerțului
- derogare tratată: `cod_fiscal_227_2015_consolidat#art48/alin2^3` — Derogarea vizează microîntreprinderea aflată în inactivitate temporară înscrisă în registrul comerțului și derogă de la art. 52; societatea din întrebare este nou-înființată și activă, deci nu se aplică.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art52/alin3` — Se referă la încetarea raportului de muncă în cursul anului la o microîntreprindere care avea salariat (termen de 30 de zile pentru angajarea unui nou salariat), nu la termenul de îndeplinire inițială a condiției de către o societate nou-înființată; nu se aplică cazului.
- derogare tratată: `og_16_2022_consolidat#artI/pct2 (og_16_2022_consolidat#artI/alin2)` — Redă forma de modificare a art. 48 alin. (3) cu termen de 30 de zile; textul consolidat al art. 48 alin. (3) în vigoare la data de referință (valabil din 25.02.2026) prevede 90 de zile, deci versiunea anterioară nu se aplică.

Apel: `claude-opus-5`, {'intrare': 6076, 'iesire': 1720, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0743

Pe fond: **CORECT** — faptul principal si articolul coincid

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-03-10 (zi, din "10 martie 2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: D15: intrebarea cere un fapt a carui forma motorul nu o recunoaste; nu pot verifica ca un fragment extras raspunde la ce s-a intrebat. Atasez regula cea mai bine potrivita, ca material, nu ca raspuns.


Pe fond: **NU POT** — D15: intrebarea cere un fapt a carui forma motorul nu o recunoaste; nu pot verifica ca un fragment extras raspunde la ce s-a intrebat. Atasez regula cea mai bine potrivita, ca material, nu ca raspuns.

## Cheia

- În 90 de zile inclusiv de la înregistrare (nu 30, cum era înainte de OUG 8/2026); dacă nu, datorează impozit pe profit începând cu trimestrul următor celui în care expiră cele 90 de zile (termenul expiră 08.06.2026, trim. II → impozit pe profit din trim. III 2026)
- temei: Cod fiscal art. 48 alin. (3), modificat de OUG 8/2026 art. 6 pct. 18, în vigoare 25.02.2026; art. 47 alin. (1) lit. g); art. 51 alin. (4) (definiția salariatului)
