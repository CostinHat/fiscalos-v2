# Q4-PRF-07 — CALCUL

**Întrebarea:** O persoană juridică străină își înființează în România o reprezentanță autorizată la 10.05.2026. Cât impozit pe reprezentanță datorează pentru anul 2026, în ce termen se declară și se plătește, și cât datorează pentru 2027 (dacă funcționează tot anul)?

## RĂSPUNS

> **Pentru anul înființării, impozitul pe reprezentanță se datorează proporțional cu numărul de luni de existență a reprezentanței în anul fiscal, pornind de la nivelul de 18.000 lei pentru un an fiscal, impozitul fiind calculat începând cu data de 1 a lunii în care reprezentanța a fost înființată (luna mai) până la sfârșitul anului respectiv. Reprezentanța are obligația să calculeze, să depună declarația fiscală la organul fiscal competent și să plătească acest impozit în termen de 30 de zile de la data înființării, adică până la 09.06.2026. Pentru anul următor, dacă funcționează tot anul, impozitul pe reprezentanță este de 18.000 lei și se declară și se plătește la bugetul de stat până în ultima zi a lunii februarie inclusiv a anului de impunere. [calcul: conversie C45/C51: „30 de zile” (ordinal / cifră cu unitate) = 30; termen_efectiv(09.06.2026) = 09.06.2026 (zi lucrătoare: marți); date mobile calculate pentru 2026 (Paștele ortodox: algoritmul Meeus pentru calendarul iulian + 13 zile): Vinerea Mare = 10.04.2026; Paștele ortodox = 12.04.2026; Rusaliile = Paștele + 49 de zile = 31.05.2026; sărbători numite în art. 139 fără dată, cu data de calendar liturgic fix (dată de calendar, nescrisă în lege): Adormirea Maicii Domnului = 15.08.2026; Crăciunul = 25-26.12.2026; termen_declarare = termen_efectiv(data_infiintare + zile_termen) = termen_efectiv((10.05.2026 + 30)) = 09.06.2026] [data de referință: 10.05.2026 — Faptul întrebat principal este impozitul datorat pentru anul înființării și termenul de declarare/plată care curge de la data înființării reprezentanței, 10.05.2026.]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- `conversie C45/C51: „30 de zile” (ordinal / cifră cu unitate) = 30`
- `termen_efectiv(09.06.2026) = 09.06.2026 (zi lucrătoare: marți); date mobile calculate pentru 2026 (Paștele ortodox: algoritmul Meeus pentru calendarul iulian + 13 zile): Vinerea Mare = 10.04.2026; Paștele ortodox = 12.04.2026; Rusaliile = Paștele + 49 de zile = 31.05.2026; sărbători numite în art. 139 fără dată, cu data de calendar liturgic fix (dată de calendar, nescrisă în lege): Adormirea Maicii Domnului = 15.08.2026; Crăciunul = 25-26.12.2026`
- `termen_declarare = termen_efectiv(data_infiintare + zile_termen)` = termen_efectiv((10.05.2026 + 30)) = **09.06.2026**
- **Codul fiscal (Legea 227/2015) art. 237 alin. (2)** — `cod_fiscal_227_2015_consolidat#art237/alin2`
  > Reprezentanța unei/unor persoane juridice străine înființată în România în cursul unei luni din anul de impunere are obligația să calculeze, să depună declarația fiscală la organul fiscal competent și să plătească impozitul pentru anul de impunere, în termen de 30 de zile de la data la care aceasta a fost înființată.
- **Codul fiscal (Legea 227/2015) art. 237 alin. (2)** — `cod_fiscal_227_2015_consolidat#art237/alin2`
  > Impozitul se calculează începând cu data de 1 a lunii în care aceasta a fost înființată până la sfârșitul anului respectiv.
- **Codul fiscal (Legea 227/2015) art. 236 alin. (1)** — `cod_fiscal_227_2015_consolidat#art236/alin1`
  > Impozitul pe reprezentanță pentru un an fiscal este de 18.000 lei.
- **Codul fiscal (Legea 227/2015) art. 236 alin. (2)** — `cod_fiscal_227_2015_consolidat#art236/alin2`
  > În cazul reprezentanței unei/unor persoane juridice străine, care se înființează sau desființează în cursul unui an fiscal, impozitul datorat pentru acest an se calculează proporțional cu numărul de luni de existență a reprezentanței în anul fiscal respectiv.
- **Codul fiscal (Legea 227/2015) art. 237 alin. (1)** — `cod_fiscal_227_2015_consolidat#art237/alin1`
  > Reprezentanța unei/unor persoane juridice străine are obligația să declare și să plătească impozitul pe reprezentanță la bugetul de stat până în ultima zi a lunii februarie inclusiv a anului de impunere.
- **Legea 134/2010 art. 181 alin. (2)** — `legea_134_2010_codul_de_procedura_civila#art181/alin2`
  > Când ultima zi a unui termen cade într-o zi nelucrătoare, termenul se prelungește până în prima zi lucrătoare care urmează.
- **Codul muncii (Legea 53/2003) art. 139 alin. (1)** — `legea_53_2003_codul_muncii#art139/alin1`
  > Zilele de sărbătoare legală în care nu se lucrează sunt: – 1 și 2 ianuarie; – 6 ianuarie - Botezul Domnului - Boboteaza; – 7 ianuarie - Soborul Sfântului Proroc Ioan Botezătorul; – 24 ianuarie – Ziua Unirii Principatelor Române; – Vinerea Mare, ultima zi de vineri înaintea Paștelui; – prima și a doua zi de Paști; – 1 mai; – 1 iunie; – prima și a doua zi de Rusalii;

Reparație C52: cifre ['2026', '2027'] → RASPUNS

Navigare: 18 pași, 13 ture; $0.8830; 213 s

Pe fond (comparator): **GREȘIT** — faptul principal al cheii (['12000 lei']) nu e in raspuns

Lectura pe fond: **fond** (valoarea întrebată necalculată) — Întrebarea cere cât impozit pe reprezentanță se datorează pentru 2026. Răspunsul dă regula (proporțional, de la luna înființării, din 18.000 lei/an) și termenele, dar nu suma: 18.000 × 8/12 = 12.000 lei. Nici termenul pentru 2027 nu e calculat (ultima zi a lui februarie 2027 e duminică → 01.03.2027): „până în ultima zi a lunii februarie” nu conține o dată, deci C40 nu-l vede.

## Cheia

- 12.000 lei pentru 2026. Impozitul anual este 18.000 lei; pentru reprezentanța înființată în cursul anului se calculează proporțional, de la data de 1 a lunii înființării (mai) până la sfârșitul anului: 8 luni → 18.000 × 8 / 12 = 12.000 lei, declarat și plătit în termen de 30 de zile de la înființare. Pentru 2027 datorează 18.000 lei, de declarat și plătit până în ultima zi a lunii februarie 2027 (28.02.2027 este duminică, deci până la 01.03.2027).
- temei: Cod fiscal art. 236 alin. (1) și (2); art. 237 alin. (1) și (2); Legea 134/2010 (Codul de procedură civilă) art. 181 alin. (2)
