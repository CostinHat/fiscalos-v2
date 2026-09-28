# Q-SAL-10 — REGULA

**Întrebarea:** Un salariat a prestat ore suplimentare în septembrie 2026. În ce termen trebuie compensate prin ore libere plătite și, dacă nu este posibil, care este sporul minim?

## Stratul semantic — RĂSPUNS

*La data de referință 30.09.2026, presupun un salariat încadrat cu contract individual de muncă în regimul general al Codului muncii (nu personal militar, polițist sau polițist de penitenciare din instituțiile de apărare, ordine publică și securitate națională, pentru care există reguli speciale), care a prestat muncă suplimentară în septembrie 2026.*

> **Munca suplimentară se compensează prin ore libere plătite în următoarele 90 de zile calendaristice după efectuarea acesteia. Dacă această compensare nu este posibilă, munca suplimentară se plătește printr-un spor la salariu stabilit prin negociere (contract colectiv sau individual de muncă), care nu poate fi mai mic de 75% din salariul de bază.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul muncii (Legea 53/2003) art. 281 alin. (7)** — `legea_53_2003_codul_muncii#art281/alin7~6` · valabil din 2025-10-12
  > Munca suplimentară se compensează prin ore libere plătite în următoarele 90 de zile calendaristice după efectuarea acesteia.
- **Codul muncii (Legea 53/2003) art. 281 alin. (2)** — `legea_53_2003_codul_muncii#art281/alin2~3` · valabil din 2024-06-03
  > Sporul pentru munca suplimentară, acordat în condițiile prevăzute la alin. (1), se stabilește prin negociere, în cadrul contractului colectiv de muncă sau, după caz, al contractului individual de muncă, și nu poate fi mai mic de 75% din salariul de bază.
- **Codul muncii (Legea 53/2003) art. 281 alin. (2)** — `legea_53_2003_codul_muncii#art281/alin2~3` · valabil din 2024-06-03
  > În cazul în care compensarea prin ore libere plătite nu este posibilă în termenul prevăzut de art. 122 alin. (1) în luna următoare, munca suplimentară va fi plătită salariatului prin adăugarea unui spor la salariu corespunzător duratei acesteia.
- derogare tratată: `legea_141_2025_consolidat#artXVIII/alin2` — Derogare aplicabilă în anul 2026 doar personalului militar, polițiștilor și polițiștilor de penitenciare din instituțiile publice de apărare, ordine publică și securitate națională, pentru activități deosebite cu caracter operativ sau neprevăzut; nu se aplică unui salariat obișnuit din regimul gener…
- derogare tratată: `legea_141_2025#artXVIII/alin2` — Aceeași derogare (text în varianta publicată), limitată la personalul militar/polițiști/polițiști de penitenciare în anul 2026; cazul din întrebare privește un salariat de drept comun.
- derogare tratată: `legea_141_2025_consolidat#artXVIII/alin7` — Privește procedura de aprobare a plății drepturilor prevăzute la alin. (2) pentru ordonatorii de credite din sectorul de apărare/ordine publică; nu vizează salariatul din sectorul reglementat de Codul muncii.
- derogare tratată: `legea_141_2025#artXVIII/alin7` — Idem, regulă bugetară pentru ordonatorii de credite, inaplicabilă cazului.
- derogare tratată: `oug_115_2023_consolidat#artIII/alin3` — Vizează munca suplimentară prestată în anul 2024 de personal cu statut special; nu privește septembrie 2026 și nici un salariat de drept comun.
- derogare tratată: `oug_115_2023_consolidat#artIII/alin7` — Condiție de plată (dispunere în scris, maximum 180 de ore anual) aferentă situațiilor de la art. III alin. (3) și (4) din OUG 115/2023, aplicabile personalului cu statut special în 2024; nu se aplică.
- derogare tratată: `oug_156_2024#artIII/alin2` — Se referă la anul 2025 și la personal militar, polițiști, polițiști de penitenciare și salvatori montani; nu se aplică muncii suplimentare prestate în septembrie 2026 de un salariat de drept comun.
- derogare tratată: `oug_156_2024#artIII/alin3` — Procedura de aprobare a majorării de la alin. (2) al aceluiași articol, inaplicabilă cazului.

Apel: `claude-opus-5`, {'intrare': 5239, 'iesire': 2227, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0828

Pe fond: **GREȘIT** — articolul citat [('cm', '281')] nu e printre cele ale cheii [('cm', '122'), (None, '123')]

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-09-30 (luna, din "septembrie 2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **Plata drepturilor pentru munca suplimentară prestată în cadrul activităților deosebite cu caracter operativ sau neprevăzut se efectuează dacă munca astfel prestată nu a fost compensată cu timp liber corespunzător în termen de 90 de zile de la momentul prestării acesteia.**

Motiv: D15: fraza care conţine un fapt de forma cerută (termen) si potriveste cel mai bine intrebarea (scor local 27.7)

- **Legea 141/2025 art. XVIII alin. (2)** — `legea_141_2025_consolidat#artXVIII/alin2` · valabil din nedovedit
  > Prin excepție de la prevederile alin. (1) , în anul 2026, pentru activitatea desfășurată de personalul militar, polițiștii și polițiștii de penitenciare din instituțiile publice de apărare, ordine publică și securitate națională în zilele de repaus săptămânal, de sărbători legale și în celelalte zile în care, în conformitate cu reglementările în vigoare, nu se lucrează, precum și pentru munca suplimentară, care nu se poate compensa cu timp liber corespunzător, prestată peste programul normal de …

Pe fond: **GREȘIT** — articolul citat [('lege_141_2025', 'XVIII')] nu e printre cele ale cheii [('cm', '122'), (None, '123')]

## Cheia

- Ore libere plătite în următoarele 90 de zile calendaristice; altfel se plătesc cu spor negociat de minim 75% din salariul de bază (în luna următoare)
- temei: Legea 53/2003 (Codul muncii) art. 122 alin. (1) (forma OUG 117/2021); art. 123 alin. (1) și (2)
