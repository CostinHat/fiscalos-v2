# Q3-TVA-06 — CALCUL

**Întrebarea:** O firmă aplică sistemul TVA la încasare în 2026. Pe 15.06.2026 livrează mărfuri unui client neafiliat din România (operațiune taxabilă cu cota standard, fără taxare inversă) și emite factura de 20.000 lei + TVA 21% = 24.200 lei. Pe 20.07.2026 încasează parțial 12.100 lei; restul rămâne neîncasat la 31.08.2026. Cât TVA colectat devine exigibil în iunie 2026 și cât în iulie 2026?

## RĂSPUNS

> **În iunie 2026 nu devine exigibilă nicio sumă de TVA colectat din această factură: în sistemul TVA la încasare exigibilitatea intervine la data încasării, nu la data livrării/facturării. În iulie 2026 devine exigibil TVA colectat de 2.100 lei, aferent încasării parțiale de 12.100 lei (încasarea se consideră că include și taxa, determinată prin procedeul sutei mărite, la cota standard). TVA aferentă părții neîncasate rămâne neexigibilă la 31.08.2026, urmând să devină exigibilă la data încasării. [calcul: tva_iulie = incasare_partiala * cota_standard / (1 + cota_standard) = ((12.100 × 21%) ÷ (1 + 21%)) = 2.100] [data de referință: 20.07.2026 — Faptul întrebat este momentul și cuantumul exigibilității TVA colectat, care, în sistemul TVA la încasare, intervine la data încasării parțiale, respectiv 20.07.2026; datele de 15.06.2026 (livrare/facturare) și 31.08.2026 (sold neîncasat) sunt doar context.]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- `tva_iulie = incasare_partiala * cota_standard / (1 + cota_standard)` = ((12.100 × 21%) ÷ (1 + 21%)) = **2.100**
- **Codul fiscal (Legea 227/2015) art. 282 alin. (3)** — `cod_fiscal_227_2015_consolidat#art282/alin3`
  > Prin excepție de la prevederile alin. (1) și alin. (2) lit. a) , exigibilitatea taxei intervine la data încasării contravalorii integrale sau parțiale a livrării de bunuri ori a prestării de servicii, în cazul persoanelor impozabile care optează în acest sens, denumite în continuare persoane care aplică sistemul TVA la încasare.
- **Codul fiscal (Legea 227/2015) art. 282 alin. (8)** — `cod_fiscal_227_2015_consolidat#art282/alin8`
  > Pentru determinarea taxei aferente încasării contravalorii integrale sau parțiale a livrării de bunuri ori a prestării de servicii, care devine exigibilă potrivit prevederilor alin. (3) , fiecare încasare totală sau parțială se consideră că include și taxa aferentă.
- **Codul fiscal (Legea 227/2015) art. 291 alin. (1)** — `cod_fiscal_227_2015_consolidat#art291/alin1`
  > Cota standard se aplică asupra bazei de impozitare pentru operațiunile impozabile care nu sunt scutite de taxă sau care nu sunt supuse cotei reduse, iar nivelul acesteia este 21%.
- **Normele metodologice ale Codului fiscal (HG 1/2016) anexa, Titlul VII, pct. 36 lit. b)** — `hg_1_2016_norme_cod_fiscal#anexa/pct36~4/litb`
  > contrapartida unei livrări de bunuri/prestări de servicii trebuie considerată ca incluzând deja taxa pe valoarea adăugată, taxa determinându-se prin aplicarea procedeului sutei mărite, respectiv 21 x 100/121 în cazul cotei standard
- **Codul fiscal (Legea 227/2015) art. 282 alin. (6)** — `cod_fiscal_227_2015_consolidat#art282/alin6`
  > Persoanele impozabile care optează pentru aplicarea sistemului TVA la încasare aplică sistemul respectiv numai pentru operațiuni pentru care locul livrării, conform prevederilor art. 275 , sau locul prestării, conform prevederilor art. 278 , se consideră a fi în România, dar nu aplică sistemul respectiv pentru următoarele operațiuni care intră sub incidența regulilor generale privind exigibilitatea TVA:

Navigare: 17 pași, 14 ture; {'intrare': 28, 'iesire': 8407, 'cache_scriere': 58490, 'cache_citire': 273100} tokeni; $0.7124; 146 s

Cauza (dacă NU POT): RASPUNS

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## Cheia

- 2.100 lei devin exigibili în iulie 2026 (0 lei în iunie 2026). Calcul: în sistemul TVA la încasare exigibilitatea intervine la data încasării, iar fiecare încasare se consideră că include și taxa: 12.100 × 21/121 = 2.100 lei, exigibili la 20.07.2026 (decontul lunii iulie). La emiterea facturii din iunie nu intervine exigibilitatea (taxa de 4.200 lei este neexigibilă); restul de 4.200 − 2.100 = 2.100 lei rămâne neexigibil până la încasarea diferenței de 12.100 lei.
- temei: Cod fiscal art. 282 alin. (3); art. 282 alin. (8); art. 282 alin. (6); art. 291 alin. (1)
