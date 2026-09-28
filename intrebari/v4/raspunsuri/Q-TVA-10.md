# Q-TVA-10 — INCOMPLETA

**Întrebarea:** Firma a cumpărat o mașină cu 150.000 lei + TVA. Cât TVA deduce?

## Stratul de navigare (v4) — NU POT RĂSPUNDE

*La data de referință 28.09.2026, presupun o persoană impozabilă înregistrată în scopuri de TVA în România, cu drept de deducere integral (operațiuni taxabile), care achiziționează un vehicul rutier motorizat cu preț de 150.000 lei fără TVA; întrebarea nu spune dacă vehiculul este utilizat exclusiv în scopul activității economice, care sunt masa totală maximă autorizată și numărul de scaune, nici dacă se încadrează în categoriile exceptate.*

Motiv: INCOMPLET: intrebarea nu da faptele de care depinde raspunsul: Dacă vehiculul este utilizat exclusiv în scopul activității economice (existența foilor de parcurs / justificarea utilizării exclusive); Masa totală maximă autorizată a vehiculului (peste sau sub 3.500 kg); Numărul de scaune, inclusiv scaunul șoferului (mai mult sau mai puțin de 9); Dacă vehiculul se încadrează într-una dintre categoriile de la art. 298 alin. (3) (urgență, agenți de vânzări/achiziții, transport de persoane cu plată, servicii cu plată, închiriere/leasing, mărfuri în scop comercial); Cota de TVA înscrisă în factura de achiziție și dacă persoana impozabilă are drept de deducere integral (operațiuni taxabile)

- **Codul fiscal (Legea 227/2015) art. 298 alin. (1)** — `cod_fiscal_227_2015_consolidat#art298/alin1` · valabil din nedovedit
  > Prin excepție de la prevederile art. 297 se limitează la 50% dreptul de deducere a taxei aferente cumpărării, achiziției intracomunitare, importului, închirierii sau leasingului de vehicule rutiere motorizate și a taxei aferente cheltuielilor legate de vehiculele aflate în proprietatea sau în folosința persoanei impozabile, în cazul în care vehiculele nu sunt utilizate exclusiv în scopul activității economice.
- **Codul fiscal (Legea 227/2015) art. 298 alin. (2)** — `cod_fiscal_227_2015_consolidat#art298/alin2` · valabil din nedovedit
  > Restricția prevăzută la alin. (1) nu se aplică vehiculelor rutiere motorizate având o masă totală maximă autorizată care depășește 3.500 kg sau mai mult de 9 scaune, inclusiv scaunul șoferului.
- **Codul fiscal (Legea 227/2015) art. 298 alin. (3)** — `cod_fiscal_227_2015_consolidat#art298/alin3` · valabil din nedovedit
  > Prevederile alin. (1) nu se aplică următoarelor categorii de vehicule rutiere motorizate:
- derogare tratată: `cod_fiscal_227_2015_consolidat#art298/alin1` — Alin. (1) este el însuși o excepție de la art. 297 (sfera generală a dreptului de deducere); l-am citat ca regulă aplicabilă vehiculelor rutiere motorizate.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art298/alin3` — Categoriile exceptate de la limitarea de 50% sunt semnalate ca fapt lipsă, întrucât întrebarea nu precizează destinația vehiculului.

### Navigarea (5 pași, 4 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Limitări speciale ale dreptului de deducere"}
2. `cauta` {"interogare": "deducere 50% taxa vehicule rutiere motor masa maxima 3.500 kg 9 scaune"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art298"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art298/alin1"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art298/alin3"}

Apel: `claude-opus-5`, {'intrare': 8, 'iesire': 2342, 'cache_scriere': 6975, 'cache_citire': 36424} tokeni, $0.1204, 37 s

Pe fond: **NU POT** — INCOMPLETA: motorul s-a abţinut, iar cheia spune si ea ca lipsesc date

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți nu conțin nici cota de TVA aplicabilă, nici regulile privind dreptul de deducere a taxei pentru achiziția de vehicule (inclusiv eventuala limitare a deducerii în funcție de utilizare); ei privesc înregistrarea în scopuri de TVA, rambursarea soldului negativ, TVA la import și intermedieri. În plus, determinarea sumei deductibile ar presupune un calcul (aplicarea unei cote la baza de 150.000 lei), rezultat care nu apare literal în niciun atom. Pentru un răspuns …

## Cheia

- Depinde — trebuie clarificat: (a) masa totală maximă autorizată > 3.500 kg sau > 9 locuri; (b) dacă e folosită exclusiv în scopul activității economice; (c) dacă intră într-o categorie exceptată (curierat, agenți de vânzări, taxi, închiriere/leasing, marfă etc.). Dacă nu e exceptată și are utilizare mixtă: 50% × 31.500 = 15.750 lei; altfel deducere integrală 31.500 lei
- temei: Cod fiscal art. 298 alin. (1)-(4); art. 291 alin. (1)
