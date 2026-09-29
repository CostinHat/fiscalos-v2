# Q-SAL-10 — REGULA

**Întrebarea:** Un salariat a prestat ore suplimentare în septembrie 2026. În ce termen trebuie compensate prin ore libere plătite și, dacă nu este posibil, care este sporul minim?

## Stratul de navigare v5 — RĂSPUNS

*La data de 30.09.2026, pentru un salariat încadrat cu contract individual de muncă la un angajator din sectorul privat (întrebarea nu indică personal bugetar/cu statut special), aflat sub regimul general al Codului muncii privind munca suplimentară.*

Datele din întrebare: 2026-09-30 · data de referință aleasă: **2026-09-30** — Singura dată din întrebare; orele suplimentare au fost prestate în septembrie 2026, deci regula aplicabilă este cea în vigoare la acea dată.

> **Munca suplimentară trebuie compensată prin ore libere plătite în următoarele 90 de zile calendaristice după efectuarea acesteia; dacă această compensare nu este posibilă, munca suplimentară se plătește prin adăugarea unui spor negociat prin contractul colectiv sau individual de muncă, care nu poate fi mai mic de 75% din salariul de bază.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul muncii (Legea 53/2003) art. 281 alin. (7)** — `legea_53_2003_codul_muncii#art281/alin7~6` · valabil din 2025-10-12
  > + Articolul 122(1) Munca suplimentară se compensează prin ore libere plătite în următoarele 90 de zile calendaristice după efectuarea acesteia.
- **Codul muncii (Legea 53/2003) art. 281 alin. (2)** — `legea_53_2003_codul_muncii#art281/alin2~3` · valabil din 2024-06-03
  > Sporul pentru munca suplimentară, acordat în condițiile prevăzute la alin. (1), se stabilește prin negociere, în cadrul contractului colectiv de muncă sau, după caz, al contractului individual de muncă, și nu poate fi mai mic de 75% din salariul de bază.
- **Codul muncii (Legea 53/2003) art. 281 alin. (2)** — `legea_53_2003_codul_muncii#art281/alin2~3` · valabil din 2024-06-03
  > + Articolul 123(1) În cazul în care compensarea prin ore libere plătite nu este posibilă în termenul prevăzut de art. 122 alin. (1) în luna următoare, munca suplimentară va fi plătită salariatului prin adăugarea unui spor la salariu corespunzător duratei acesteia.
- derogare tratată: `legea_141_2025_consolidat#artXVIII/alin1` — Regimul special al muncii suplimentare în anul 2026 prevăzut de Legea 141/2025 art. XVIII derogă de la Legea-cadru nr. 153/2017 și privește personalul plătit din fonduri publice (inclusiv personal militar, polițiști); nu se aplică salariatului din sectorul privat presupus în întrebare.
- derogare tratată: `legea_141_2025_consolidat#artXVIII/alin2` — Excepția vizează personalul militar, polițiștii și polițiștii de penitenciare din instituțiile publice de apărare, ordine publică și securitate națională; nu se aplică salariatului obișnuit din sectorul privat.

### Navigarea (15 pași, 13 ture)

1. `cuprins` {"act": "legea_53_2003_codul_muncii", "filtru": "ore suplimentare"}
2. `cauta` {"interogare": "munca suplimentara compensata ore libere platite spor"}
3. `cuprins` {"act": "legea_53_2003_codul_muncii", "filtru": "suplimentară"}
4. `cuprins` {"act": "legea_53_2003_codul_muncii", "filtru": "munca"}
5. `cuprins` {"act": "legea_53_2003_codul_muncii", "filtru": ""}
6. `deschide` {"id": "legea_53_2003_codul_muncii#art122"}
7. `cauta` {"interogare": "compensare prin ore libere plătite în următoarele 60 de zile calendaristice după efectuarea acesteia"}
8. `deschide` {"id": "legea_53_2003_codul_muncii#art122/alin1"}
9. `deschide` {"id": "legea_53_2003_codul_muncii#art123"}
10. `cauta` {"interogare": "munca suplimentară se compensează prin ore libere plătite în următoarele 90 de zile calendaristice"}
11. `cauta` {"interogare": "spor pentru munca suplimentară 75% din salariul de bază"}
12. `deschide` {"id": "legea_53_2003_codul_muncii#art281/alin7~6"}
13. `deschide` {"id": "legea_53_2003_codul_muncii#art281"}
14. `cauta` {"interogare": "spor nu poate fi mai mic de 75% din salariul de bază muncă suplimentară compensare cu timp liber"}
15. `deschide` {"id": "legea_53_2003_codul_muncii#art281/alin2~3"}

Apel: `claude-opus-5`, {'intrare': 26, 'iesire': 3641, 'cache_scriere': 16526, 'cache_citire': 154164} tokeni, $0.2715, 70 s

Pe fond (comparator): **GREȘIT** — articolul citat [('cm', '281')] nu e printre cele ale cheii [('cm', '122'), ('cm', '123')]

Lectura pe fond (de verificat de om): **articol, nu fond** — Faptele coincid cu cheia (90 de zile calendaristice, spor de minimum 75%). Citatul e verbatim din Codul muncii din instantaneul iConta, unde textul art. 122 apare atomizat sub `art281/alin7~6`: structura instantaneului Codului muncii e greșită, nu răspunsul (vezi C31).

## v4 — RĂSPUNS, pe fond GREȘIT

> Orele suplimentare prestate în septembrie 2026 se compensează prin ore libere plătite în următoarele 90 de zile calendaristice după efectuarea lor; dacă această compensare nu este posibilă în acest termen, munca suplimentară se plătește în luna următoare cu un spor la salariu stabilit prin negociere (contract colectiv sau individual de muncă), care nu poate fi mai mic de 75% din salariul de bază.

## Cheia

- Ore libere plătite în următoarele 90 de zile calendaristice; altfel se plătesc cu spor negociat de minim 75% din salariul de bază (în luna următoare)
- temei: Legea 53/2003 (Codul muncii) art. 122 alin. (1) (forma OUG 117/2021); art. 123 alin. (1) și (2)
