# Q4-PRF-06 — CALCUL

**Întrebarea:** Microîntreprindere (îndeplinește condițiile pentru 2026), trimestrul II 2026: venituri din vânzarea mărfurilor 250.000 lei, venituri din prestări servicii 30.000 lei, venituri din subvenții 20.000 lei, despăgubiri primite de la asigurător pentru mărfuri distruse 12.000 lei, venituri din producția de imobilizări corporale 18.000 lei, bonificație acordată de organul fiscal 1.000 lei; reduceri comerciale acordate clienților ulterior facturării, înregistrate în contul 709: 4.000 lei. Cât impozit pe veniturile microîntreprinderilor datorează pentru T2 2026 și până când îl plătește?

## RĂSPUNS

> **Baza impozabilă a trimestrului II 2026 este de 276.000 lei (250.000 lei mărfuri + 30.000 lei servicii, minus 4.000 lei reduceri comerciale acordate ulterior facturării din contul 709; nu intră în bază subvențiile de 20.000 lei, despăgubirile de la asigurător de 12.000 lei pentru mărfurile distruse, veniturile din producția de imobilizări corporale de 18.000 lei și bonificația de 1.000 lei acordată de organul fiscal). Impozitul datorat este de 2.760 lei, cu cota de 1%, și se plătește până la 27.07.2026 (termenul de 25 a lunii următoare trimestrului cade sâmbătă și se prelungește în prima zi lucrătoare). [calcul: baza_impozabila = venituri_marfuri + venituri_servicii - reduceri_709 = ((250.000 + 30.000) − 4.000) = 276.000; impozit = baza_impozabila * cota = (276.000 × 1%) = 2.760; termen_efectiv(25.07.2026) = 27.07.2026: 25.07.2026 sâmbătă, 26.07.2026 duminică → prima zi lucrătoare, 27.07.2026 (luni). Regula: `legea_134_2010_codul_de_procedura_civila#art181/alin2`; sărbătorile: `legea_53_2003_codul_muncii#art139/alin1`; date mobile calculate pentru 2026 (Paștele ortodox: algoritmul Meeus pentru calendarul iulian + 13 zile): Vinerea Mare = 10.04.2026; Paștele ortodox = 12.04.2026; Rusaliile = Paștele + 49 de zile = 31.05.2026; sărbători numite în art. 139 fără dată, cu data de calendar liturgic fix (dată de calendar, nescrisă în lege): Adormirea Maicii Domnului = 15.08.2026; Crăciunul = 25-26.12.2026; termen = termen_efectiv(data(zi, luna, an)) = termen_efectiv(data(25, 7, 2.026)) = 27.07.2026] [data de referință: 28.09.2026 — Singura dată purtată de întrebare este anul 2026, iar faptul întrebat (impozitul trimestrului II 2026 și termenul lui de plată) se raportează la legislația în vigoare în 2026.]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- `baza_impozabila = venituri_marfuri + venituri_servicii - reduceri_709` = ((250.000 + 30.000) − 4.000) = **276.000**
- `impozit = baza_impozabila * cota` = (276.000 × 1%) = **2.760**
- `termen_efectiv(25.07.2026) = 27.07.2026: 25.07.2026 sâmbătă, 26.07.2026 duminică → prima zi lucrătoare, 27.07.2026 (luni). Regula: `legea_134_2010_codul_de_procedura_civila#art181/alin2`; sărbătorile: `legea_53_2003_codul_muncii#art139/alin1`; date mobile calculate pentru 2026 (Paștele ortodox: algoritmul Meeus pentru calendarul iulian + 13 zile): Vinerea Mare = 10.04.2026; Paștele ortodox = 12.04.2026; Rusaliile = Paștele + 49 de zile = 31.05.2026; sărbători numite în art. 139 fără dată, cu data de calendar liturgic fix (dată de calendar, nescrisă în lege): Adormirea Maicii Domnului = 15.08.2026; Crăciunul = 25-26.12.2026`
- `termen = termen_efectiv(data(zi, luna, an))` = termen_efectiv(data(25, 7, 2.026)) = **27.07.2026**
- **Codul fiscal (Legea 227/2015) art. 53 alin. (1)** — `cod_fiscal_227_2015_consolidat#art53/alin1`
  > Baza impozabilă a impozitului pe veniturile microîntreprinderilor o constituie veniturile din orice sursă, din care se scad:
- **Codul fiscal (Legea 227/2015) art. 51 alin. (1)** — `cod_fiscal_227_2015_consolidat#art51/alin1`
  > Cota de impozit pe veniturile microîntreprinderilor este de 1%.
- **Codul fiscal (Legea 227/2015) art. 56 alin. (1)** — `cod_fiscal_227_2015_consolidat#art56/alin1`
  > Calculul și plata impozitului pe veniturile microîntreprinderilor se efectuează trimestrial, până la data de 25 inclusiv a lunii următoare trimestrului pentru care se calculează impozitul.
- **Codul fiscal (Legea 227/2015) art. 53 alin. (1) lit. j)** — `cod_fiscal_227_2015_consolidat#art53/alin1/litj`
  > valoarea reducerilor comerciale acordate ulterior facturării, înregistrate în contul "709", potrivit reglementărilor contabile aplicabile;
- **Codul fiscal (Legea 227/2015) art. 53 alin. (1) lit. g)** — `cod_fiscal_227_2015_consolidat#art53/alin1/litg`
  > veniturile realizate din despăgubiri, de la societățile de asigurare/reasigurare, pentru pagubele produse bunurilor de natura stocurilor sau a activelor corporale proprii;
- **Legea 134/2010 art. 181 alin. (2)** — `legea_134_2010_codul_de_procedura_civila#art181/alin2`
  > Când ultima zi a unui termen cade într-o zi nelucrătoare, termenul se prelungește până în prima zi lucrătoare care urmează.
- **Codul muncii (Legea 53/2003) art. 139 alin. (1)** — `legea_53_2003_codul_muncii#art139/alin1`
  > Zilele de sărbătoare legală în care nu se lucrează sunt: – 1 și 2 ianuarie; – 6 ianuarie - Botezul Domnului - Boboteaza; – 7 ianuarie - Soborul Sfântului Proroc Ioan Botezătorul; – 24 ianuarie – Ziua Unirii Principatelor Române; – Vinerea Mare, ultima zi de vineri înaintea Paștelui; – prima și a doua zi de Paști; – 1 mai; – 1 iunie;

Navigare: 17 pași, 9 ture; $0.5747; 114 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## Cheia

- 2.760 lei. Venituri din orice sursă: 250.000 + 30.000 + 20.000 + 12.000 + 18.000 + 1.000 = 331.000 lei. Se scad: subvenții 20.000, despăgubiri de la asigurător pentru stocuri 12.000, producția de imobilizări 18.000, bonificația organului fiscal 1.000, reducerile comerciale din 709 4.000 = 55.000 lei. Baza impozabilă = 276.000 lei × 1% = 2.760 lei. Termen de plată și de depunere a declarației: 25.07.2026 cade sâmbătă, deci se prelungește la 27.07.2026.
- temei: Cod fiscal art. 53 alin. (1) lit. c), d), g), j) și p); art. 51 alin. (1); art. 56 alin. (1) și (2); Legea 207/2015 art. 75; Legea 134/2010 (Codul de procedură civilă) art. 181 alin. (2)
