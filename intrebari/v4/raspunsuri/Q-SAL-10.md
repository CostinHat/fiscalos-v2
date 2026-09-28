# Q-SAL-10 — REGULA

**Întrebarea:** Un salariat a prestat ore suplimentare în septembrie 2026. În ce termen trebuie compensate prin ore libere plătite și, dacă nu este posibil, care este sporul minim?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 30.09.2026, presupun un salariat cu contract individual de muncă la un angajator din sectorul privat, supus regulilor generale din Codul muncii privind munca suplimentară (nu personal plătit din fonduri publice, pentru care există reguli speciale de salarizare), iar întrebarea nu indică un nivel al sporului negociat prin contract colectiv/individual.*

> **Orele suplimentare prestate în septembrie 2026 se compensează prin ore libere plătite în următoarele 90 de zile calendaristice după efectuarea lor; dacă această compensare nu este posibilă în acest termen, munca suplimentară se plătește în luna următoare cu un spor la salariu stabilit prin negociere (contract colectiv sau individual de muncă), care nu poate fi mai mic de 75% din salariul de bază.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul muncii (Legea 53/2003) art. 281 alin. (7)** — `legea_53_2003_codul_muncii#art281/alin7~6` · valabil din 2025-10-12
  > Munca suplimentară se compensează prin ore libere plătite în următoarele 90 de zile calendaristice după efectuarea acesteia.
- **Codul muncii (Legea 53/2003) art. 281 alin. (2)** — `legea_53_2003_codul_muncii#art281/alin2~3` · valabil din 2024-06-03
  > Sporul pentru munca suplimentară, acordat în condițiile prevăzute la alin. (1), se stabilește prin negociere, în cadrul contractului colectiv de muncă sau, după caz, al contractului individual de muncă, și nu poate fi mai mic de 75% din salariul de bază.
- **Codul muncii (Legea 53/2003) art. 281 alin. (2)** — `legea_53_2003_codul_muncii#art281/alin2~3` · valabil din 2024-06-03
  > În cazul în care compensarea prin ore libere plătite nu este posibilă în termenul prevăzut de art. 122 alin. (1) în luna următoare, munca suplimentară va fi plătită salariatului prin adăugarea unui spor la salariu corespunzător duratei acesteia.
- derogare tratată: `legea_141_2025_consolidat#artXVIII/alin1` — Regimul special al muncii suplimentare pentru anul 2026 din Legea 141/2025 derogă de la art. 21 din Legea-cadru nr. 153/2017 și vizează personalul plătit din fonduri publice; nu se aplică salariatului din sectorul privat presupus în întrebare, astfel că rămân aplicabile regulile generale din Codul m…

### Navigarea (7 pași, 6 ture)

1. `cuprins` {"act": "legea_53_2003_codul_muncii", "filtru": "muncă suplimentară"}
2. `cauta` {"interogare": "munca suplimentară se compensează prin ore libere plătite 90 de zile spor"}
3. `cauta` {"interogare": "Codul muncii sporul pentru munca suplimentară 75% din salariul de bază ore libere plătite"}
4. `deschide` {"id": "legea_53_2003_codul_muncii#art281/alin7~6"}
5. `deschide` {"id": "legea_53_2003_codul_muncii#art281"}
6. `cauta` {"interogare": "În cazul în care compensarea prin ore libere plătite nu este posibilă spor la salariu stabilit prin negociere"}
7. `deschide` {"id": "legea_53_2003_codul_muncii#art281/alin2~3"}

Apel: `claude-opus-5`, {'intrare': 12, 'iesire': 3414, 'cache_scriere': 13013, 'cache_citire': 64390} tokeni, $0.1989, 52 s

Pe fond: **GREȘIT** — articolul citat [('cm', '281')] nu e printre cele ale cheii [('cm', '122'), (None, '123')]

## Stratul semantic v3 (context dat de căutare) — RĂSPUNS, pe fond GREȘIT

> Munca suplimentară se compensează prin ore libere plătite în următoarele 90 de zile calendaristice după efectuarea acesteia. Dacă această compensare nu este posibilă, munca suplimentară se plătește printr-un spor la salariu stabilit prin negociere (contract colectiv sau individual de muncă), care nu poate fi mai mic de 75% din salariul de bază.

## Cheia

- Ore libere plătite în următoarele 90 de zile calendaristice; altfel se plătesc cu spor negociat de minim 75% din salariul de bază (în luna următoare)
- temei: Legea 53/2003 (Codul muncii) art. 122 alin. (1) (forma OUG 117/2021); art. 123 alin. (1) și (2)
