# Q-SAL-10 — REGULA

**Întrebarea:** Un salariat a prestat ore suplimentare în septembrie 2026. În ce termen trebuie compensate prin ore libere plătite și, dacă nu este posibil, care este sporul minim?

## Stratul semantic (motorul nou) — RĂSPUNS

*La data de referință septembrie 2026, presupun un salariat cu contract individual de muncă în sectorul privat, supus regimului general al Codului muncii (nu personal militar/polițist ori alt statut special, pentru care există reguli derogatorii).*

> **Munca suplimentară se compensează prin ore libere plătite în următoarele 90 de zile calendaristice după efectuarea ei. Dacă această compensare nu este posibilă, munca suplimentară se plătește cu un spor la salariu stabilit prin negociere (contract colectiv sau individual de muncă), care nu poate fi mai mic de 75% din salariul de bază.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul muncii (Legea 53/2003) art. 281 alin. (7)** — `legea_53_2003_codul_muncii#art281/alin7~6` · valabil din 2025-10-12
  > + Articolul 122(1) Munca suplimentară se compensează prin ore libere plătite în următoarele 90 de zile calendaristice după efectuarea acesteia.
- **Codul muncii (Legea 53/2003) art. 281 alin. (2)** — `legea_53_2003_codul_muncii#art281/alin2~3` · valabil din 2024-06-03
  > Sporul pentru munca suplimentară, acordat în condițiile prevăzute la alin. (1), se stabilește prin negociere, în cadrul contractului colectiv de muncă sau, după caz, al contractului individual de muncă, și nu poate fi mai mic de 75% din salariul de bază.

Apel: `claude-opus-5`, {'intrare': 5239, 'iesire': 947, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0506, 13.1 s

Pe fond: **GREȘIT** — articolul citat [('cm', '281')] nu e printre cele ale cheii [('cm', '122'), (None, '123')]

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-09-30 (luna, din "septembrie 2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **Plata drepturilor pentru munca suplimentară prestată în cadrul activităților deosebite cu caracter operativ sau neprevăzut se efectuează dacă munca astfel prestată nu a fost compensată cu timp liber corespunzător în termen de 90 de zile de la momentul prestării acesteia.**

Motiv: D15: fraza care conţine un fapt de forma cerută (termen) si potriveste cel mai bine intrebarea (scor local 27.3)

- **Legea 141/2025 art. XVIII alin. (2)** — `legea_141_2025_consolidat#artXVIII/alin2` · valabil din nedovedit
  > Prin excepție de la prevederile alin. (1) , în anul 2026, pentru activitatea desfășurată de personalul militar, polițiștii și polițiștii de penitenciare din instituțiile publice de apărare, ordine publică și securitate națională în zilele de repaus săptămânal, de sărbători legale și în celelalte zile în care, în conformitate cu reglementările în vigoare, nu se lucrează, precum și pentru munca suplimentară, care nu se poate compensa cu timp liber corespunzător, prestată peste programul normal de lucru de către aceste categorii de personal în cadrul activităților deosebite cu caracter operativ s…

Pe fond: **GREȘIT** — articolul citat [('lege_141_2025', 'XVIII')] nu e printre cele ale cheii [('cm', '122'), (None, '123')]

## Cheia

- răspuns așteptat: Ore libere plătite în următoarele 90 de zile calendaristice; altfel se plătesc cu spor negociat de minim 75% din salariul de bază (în luna următoare)
- temei așteptat: Legea 53/2003 (Codul muncii) art. 122 alin. (1) (forma OUG 117/2021); art. 123 alin. (1) și (2)

