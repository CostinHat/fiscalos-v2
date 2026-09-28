# Q-PRF-10 — INCOMPLETA

**Întrebarea:** SRL-ul meu a avut în 2025 cifră de afaceri de 90.000 euro și are un salariat cu normă întreagă. Pot plăti impozit micro în 2026?

## Stratul semantic (motorul nou) — NU POT RĂSPUNDE

*La data de referință 31.12.2025, presupun o societate cu răspundere limitată din România, fără regim special (nu instituție de credit, nu activități exceptate), care verifică dacă poate aplica impozitul pe veniturile microîntreprinderilor în anul fiscal 2026 pe baza cifrei de afaceri realizate în 2025 și a unui salariat cu normă întreagă.*

Motiv: modelul s-a abţinut: Între atomii primiți nu se află textul care stabilește condițiile de încadrare ca microîntreprindere (art. 47 din Codul fiscal): lipsește plafonul de venituri exprimat în euro aplicabil pentru anul 2026 și celelalte condiții cumulative. Atomii disponibili se referă la impozitul minim/specific pe cifra de afaceri, la definiția salariatului și la situații particulare (inactivitate temporară), dar niciunul nu conține regula care ar decide dacă o cifră de afaceri de 90.000 euro în 2025 permite aplicarea regimului micro în 2026. Fără acest text nu pot da un răspuns Da/Nu.


Apel: `claude-opus-5`, {'intrare': 2799, 'iesire': 697, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0322, 13.4 s

Pe fond: **NU POT** — INCOMPLETA: motorul s-a abţinut, iar cheia spune si ea ca lipsesc date

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2025-12-31 (an, din "2025"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: D15: intrebarea cere o JUDECATA (Da/Nu) - aplicarea unei reguli la faptele date. Motorul nu compune si nu aplica reguli; atasez regula cea mai bine potrivita, ca material, nu ca raspuns.


Pe fond: **NU POT** — INCOMPLETA: motorul s-a abţinut, iar cheia spune si ea ca lipsesc date

## Cheia

- răspuns așteptat: Depinde — trebuie clarificat: (1) dacă există întreprinderi legate (deținere/control >25% direct sau indirect, inclusiv asociat >25% cu PFA/II/IF), ale căror cifre de afaceri se cumulează la plafonul de 100.000 euro; (2) dacă situațiile financiare 2025 au fost depuse până la 31.03.2026; (3) dacă asociații >25% au desemnat-o ca singura micro; (4) dacă activitatea nu e exclusă (bancar, asigurări, jocuri de noroc, petrol/gaze). Doar cu 90.000 euro individual nu se poate răspunde
- temei așteptat: Cod fiscal art. 47 alin. (1) lit. c), g), h), i) și alin. (1^1) (mod. OUG 8/2026 art. 6 pct. 15-16, aplicabile încadrării în 2026 cf. art. 10 alin. (3) OUG 8/2026); art. 47 alin. (3) lit. f)-i); art. 48 alin. (2) (termen SF 31.03.2026 pentru 2026, mod. OUG 8/2026 art. 6 pct. 17)

