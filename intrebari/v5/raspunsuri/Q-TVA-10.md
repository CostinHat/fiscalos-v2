# Q-TVA-10 — INCOMPLETA

**Întrebarea:** Firma a cumpărat o mașină cu 150.000 lei + TVA. Cât TVA deduce?

## Stratul de navigare v5 — NU POT RĂSPUNDE

*La data de referință 2026-09-28, presupun o persoană impozabilă română înregistrată în scopuri de TVA, cu drept de deducere integral pentru achiziții destinate operațiunilor taxabile, care achiziționează un autovehicul cu preț de 150.000 lei plus TVA; întrebarea nu precizează caracteristicile vehiculului și modul de utilizare, de care depinde regula aplicabilă.*

Datele din întrebare: niciuna (ziua întrebării) · data de referință aleasă: **2026-09-28** — Întrebarea nu poartă nicio dată; se folosește ziua întrebării, la care se apreciază regimul de deducere aplicabil achiziției.

Motiv: INCOMPLET: intrebarea nu da faptele de care depinde raspunsul: dacă vehiculul este utilizat exclusiv în scopul activității economice (justificat cu foi de parcurs) sau și în scop personal; masa totală maximă autorizată a vehiculului (peste sau sub 3.500 kg) și numărul de scaune (peste sau sub 9, inclusiv al șoferului); dacă vehiculul se încadrează în una dintre categoriile exceptate (urgență, pază, agenți de vânzări/achiziții, transport de persoane cu plată, servicii cu plată, închiriere/leasing, mărfuri în scop comercial); cota de TVA înscrisă în factură și suma TVA facturată; dacă firma este înregistrată în scopuri de TVA și destinează achiziția operațiunilor cu drept de deducere

- **Codul fiscal (Legea 227/2015) art. 298 alin. (1)** — `cod_fiscal_227_2015_consolidat#art298/alin1` · valabil din nedovedit
  > Prin excepție de la prevederile art. 297 se limitează la 50% dreptul de deducere a taxei aferente cumpărării, achiziției intracomunitare, importului, închirierii sau leasingului de vehicule rutiere motorizate și a taxei aferente cheltuielilor legate de vehiculele aflate în proprietatea sau în folosința persoanei impozabile, în cazul în care vehiculele nu sunt utilizate exclusiv în scopul activității economice.
- **Codul fiscal (Legea 227/2015) art. 298 alin. (2)** — `cod_fiscal_227_2015_consolidat#art298/alin2` · valabil din nedovedit
  > Restricția prevăzută la alin. (1) nu se aplică vehiculelor rutiere motorizate având o masă totală maximă autorizată care depășește 3.500 kg sau mai mult de 9 scaune, inclusiv scaunul șoferului.
- **Codul fiscal (Legea 227/2015) art. 298 alin. (3)** — `cod_fiscal_227_2015_consolidat#art298/alin3` · valabil din nedovedit
  > Prevederile alin. (1) nu se aplică următoarelor categorii de vehicule rutiere motorizate:
- derogare tratată: `cod_fiscal_227_2015_consolidat#art297` — Art. 298 alin. (1) este o excepție de la regula generală a sferei dreptului de deducere din art. 297; excepția a fost semnalată, dar aplicarea ei nu poate fi stabilită fără datele lipsă.

### Navigarea (4 pași, 3 ture)

1. `cauta` {"interogare": "limitarea dreptului de deducere TVA vehicule rutiere motorizate 50%"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "limitări speciale ale dreptului de deducere"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art298/alin1"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art298/alin3"}

Apel: `claude-opus-5`, {'intrare': 6, 'iesire': 2124, 'cache_scriere': 6337, 'cache_citire': 26497} tokeni, $0.1060, 26 s

Pe fond (comparator): **NU POT** — INCOMPLETA: motorul s-a abţinut, iar cheia spune si ea ca lipsesc date

## v4 — NU POT, pe fond NU POT

> INCOMPLET: intrebarea nu da faptele de care depinde raspunsul: Dacă vehiculul este utilizat exclusiv în scopul activității economice (existența foilor de parcurs / justificarea utilizării exclusive); Masa totală maximă autorizată a vehiculului (peste sau sub 3.500 kg); Numărul de scaune, inclusiv scaunul șoferului (mai mult sau mai puțin de 9); Dacă vehiculul se încadrează într-una dintre categoriile de la art. 298 alin. (3) (urgență, agenți de vânzări/achiziții, transport de persoane cu plată, …

## Cheia

- Depinde — trebuie clarificat: (a) masa totală maximă autorizată > 3.500 kg sau > 9 locuri; (b) dacă e folosită exclusiv în scopul activității economice; (c) dacă intră într-o categorie exceptată (curierat, agenți de vânzări, taxi, închiriere/leasing, marfă etc.). Dacă nu e exceptată și are utilizare mixtă: 50% × 31.500 = 15.750 lei; altfel deducere integrală 31.500 lei
- temei: Cod fiscal art. 298 alin. (1)-(4); art. 291 alin. (1)
