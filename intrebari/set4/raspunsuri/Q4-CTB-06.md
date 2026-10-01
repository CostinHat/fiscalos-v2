# Q4-CTB-06 — CALCUL

**Întrebarea:** O SRL producătoare (aplică OMFP 1802/2014) are în iunie 2026 următoarele date pentru produsul X: capacitatea normală de producție 10.000 buc./lună; producție efectivă 8.000 buc. (producție scăzută din cauza unei avarii, nivelul real nu aproximează capacitatea normală); materii prime directe 160.000 lei; manoperă directă 96.000 lei; regie variabilă de producție 24.000 lei; regie fixă de producție 60.000 lei; cheltuieli generale de administrație 30.000 lei; cheltuieli de depozitare a produselor finite (nenecesare procesului de producție) 4.000 lei; pierderi de materiale peste limitele normal admise 2.000 lei (necuprinse în cei 160.000 lei). Care este costul de producție al celor 8.000 buc. și ce sumă rămâne cheltuială a perioadei?

## RĂSPUNS

> **Regia fixă se alocă pe baza capacității normale: din cei 60.000 lei se alocă 48.000 lei, iar 12.000 lei rămân regie fixă nealocată. Costul de producție al celor 8.000 buc. = materii prime directe 160.000 + manoperă directă 96.000 + regie variabilă 24.000 + regie fixă alocată 48.000 = 328.000 lei. Cheltuieli ale perioadei (necuprinse în cost): regia fixă nealocată 12.000 lei + cheltuieli generale de administrație 30.000 lei + cheltuieli de depozitare nenecesare procesului de producție 4.000 lei + pierderile de materiale peste limitele normal admise = 48.000 lei. [calcul: regie_fixa_alocata = regie_fixa * (productie_efectiva / capacitate_normala) = (60.000 × (8.000 ÷ 10.000)) = 48.000; regie_fixa_nealocata = regie_fixa - regie_fixa_alocata = (60.000 − 48.000) = 12.000; cost_productie = materii_prime + manopera + regie_variabila + regie_fixa_alocata = (((160.000 + 96.000) + 24.000) + 48.000) = 328.000; cheltuieli_perioada = regie_fixa_nealocata + cheltuieli_administratie + depozitare + pierderi = (((12.000 + 30.000) + 4.000) + 2.000) = 48.000] [data de referință: 30.06.2026 — Faptul întrebat este determinarea costului de producție pentru luna iunie 2026; data 2014-12-31 se referă doar la anul actului normativ aplicat (OMFP 1802/2014).]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- `regie_fixa_alocata = regie_fixa * (productie_efectiva / capacitate_normala)` = (60.000 × (8.000 ÷ 10.000)) = **48.000**
- `regie_fixa_nealocata = regie_fixa - regie_fixa_alocata` = (60.000 − 48.000) = **12.000**
- `cost_productie = materii_prime + manopera + regie_variabila + regie_fixa_alocata` = (((160.000 + 96.000) + 24.000) + 48.000) = **328.000**
- `cheltuieli_perioada = regie_fixa_nealocata + cheltuieli_administratie + depozitare + pierderi` = (((12.000 + 30.000) + 4.000) + 2.000) = **48.000**
- **OMFP 1802/2014 anexa, pct. 8 pct. 7** — `omfp_1802_2014#anexa/pct8/pct7`
  > Alocarea regiei fixe de producție asupra costurilor de conversie se face pe baza capacității normale a instalațiilor de producție. Nivelul real de producție poate fi folosit dacă se consideră că acesta aproximează capacitatea normală.
- **OMFP 1802/2014 anexa, pct. 8 pct. 7** — `omfp_1802_2014#anexa/pct8/pct7`
  > Valoarea cheltuielilor cu regia fixă alocate fiecărei unități de producție nu se majorează ca urmare a obținerii unei producții scăzute sau a neutilizării unor echipamente. Cheltuielile de regie nealocate sunt recunoscute drept cheltuială în perioada în care sunt suportate.
- **OMFP 1802/2014 anexa, pct. 8 pct. 7** — `omfp_1802_2014#anexa/pct8/pct7`
  > Costul de producție sau de prelucrare al stocurilor, precum și costul de producție al imobilizărilor cuprind cheltuielile directe aferente producției, și anume: materiale directe, energie consumată în scopuri tehnologice, manoperă directă și alte cheltuieli directe de producție, costul proiectării produselor, precum și cota cheltuielilor indirecte de producție alocată în mod rațional ca fiind legată de fabricația acestora.
- **OMFP 1802/2014 anexa, pct. 79 alin. (1)** — `omfp_1802_2014#anexa/pct79/alin1`
  > Exemple de costuri care nu trebuie incluse în costul stocurilor, ci sunt recunoscute drept cheltuieli ale perioadei în care au survenit, sunt următoarele: – pierderile de materiale, manopera sau alte costuri de producție înregistrate peste limitele normal admise, inclusiv pierderile datorate risipei; – cheltuielile de depozitare, cu excepția cazurilor în care aceste costuri sunt necesare în procesul de producție
- **OMFP 1802/2014 anexa, pct. 79 alin. (1)** — `omfp_1802_2014#anexa/pct79/alin1`
  > – regiile (cheltuielile) generale de administrație care nu participă la aducerea stocurilor în forma și locul final; – regia fixă nealocată costului, care se recunoaște drept cheltuială în perioada în care a apărut. Alocarea regiei fixe asupra costurilor se face pe baza capacității normale de producție (activitate).

Reparație C52: cifre ['2.000'] → RASPUNS

Navigare: 5 pași, 6 ture; $0.3462; 87 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## Cheia

- 328.000 lei (41 lei/buc.). Calcul: regia fixă se alocă pe baza capacității normale: 60.000 / 10.000 = 6 lei/buc.; regie fixă alocată = 8.000 × 6 = 48.000 lei; regie fixă nealocată = 60.000 − 48.000 = 12.000 lei (cheltuială a perioadei, nu majorează costul unitar din cauza producției scăzute). Cost de producție = 160.000 + 96.000 + 24.000 (regie variabilă, pe baza utilizării reale) + 48.000 = 328.000 lei; 328.000 / 8.000 = 41 lei/buc. Cheltuieli ale perioadei, excluse din cost: 12.000 (regie fixă nealocată) + 30.000 (cheltuieli generale de administrație) + 4.000 (depozitare) + 2.000 (pierderi peste limite normale) = 48.000 lei.
- temei: OMFP 1802/2014, Reglementări contabile, pct. 8 pct. 7; pct. 79 alin. (1)
