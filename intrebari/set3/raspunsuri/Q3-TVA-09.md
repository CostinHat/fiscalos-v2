# Q3-TVA-09 — CAPCANA

**Întrebarea:** O SRL înregistrată în scopuri de TVA vinde în iulie 2026 unei persoane fizice (neînregistrate în scopuri de TVA) un teren intravilan liber de construcții, pe care, conform certificatului de urbanism, se pot executa construcții, la prețul de 500.000 lei. Contabilul aplică scutirea de la art. 292 alin. (2) lit. f) Cod fiscal („livrarea ... oricăror altor terenuri”) și facturează fără TVA. Este corect?

## RĂSPUNS

> **Nu, nu este corect. Scutirea pentru „livrarea ... oricăror altor terenuri” nu se aplică terenurilor construibile, iar terenul pe care, conform certificatului de urbanism, se pot executa construcții este teren construibil. Livrarea este taxabilă cu cota standard de 21%, deci factura trebuia emisă cu TVA de 1.050 lei, la o bază de impozitare de 500.000 lei. [calcul: tva = baza * cota / 100 = ((500.000 × 21%) ÷ 100) = 1.050] [data de referință: 31.07.2026 — Faptul întrebat este tratamentul TVA al livrării efectuate în iulie 2026, singura dată din întrebare.]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- `tva = baza * cota / 100` = ((500.000 × 21%) ÷ 100) = **1.050**
- **Codul fiscal (Legea 227/2015) art. 292 alin. (2) lit. f)** — `cod_fiscal_227_2015_consolidat#art292/alin2/litf`
  > livrarea de construcții/părți de construcții și a terenurilor pe care sunt construite, precum și a oricăror altor terenuri. Prin excepție, scutirea nu se aplică pentru livrarea de construcții noi, de părți de construcții noi sau de terenuri construibile.
- **Codul fiscal (Legea 227/2015) art. 292 alin. (2) lit. f) pct. 1** — `cod_fiscal_227_2015_consolidat#art292/alin2/litf/pct1`
  > teren construibil reprezintă orice teren amenajat sau neamenajat, pe care se pot executa construcții, conform legislației în vigoare;
- **Normele metodologice ale Codului fiscal (HG 1/2016) anexa, Titlul VII, pct. 55 alin. (6)** — `hg_1_2016_norme_cod_fiscal#anexa/pct55/alin6`
  > În aplicarea art. 292 alin. (2) lit. f) din Codul fiscal, calificarea unui teren drept teren construibil sau teren cu altă destinație, la momentul vânzării sale de către proprietar, rezultă din certificatul de urbanism.
- **Codul fiscal (Legea 227/2015) art. 291 alin. (1)** — `cod_fiscal_227_2015_consolidat#art291/alin1`
  > Cota standard se aplică asupra bazei de impozitare pentru operațiunile impozabile care nu sunt scutite de taxă sau care nu sunt supuse cotei reduse, iar nivelul acesteia este 21%.

Navigare: 6 pași, 6 ture; {'intrare': 12, 'iesire': 2168, 'cache_scriere': 15682, 'cache_citire': 63329} tokeni; $0.1839; 37 s

Cauza (dacă NU POT): RASPUNS

Pe fond (comparator): **GREȘIT** — faptul principal al cheii (['105000 lei']) nu e in raspuns

Lectura: **greșeală de fond** (procentul împărțit de două ori la 100) — Concluzia e corectă (terenul construibil nu e scutit, livrarea e taxabilă cu 21%, pe temeiul cheii — CF art. 292 alin. (2) lit. f) pct. 1, art. 291 alin. (1)), dar suma e greșită: formula modelului `baza * cota / 100`, cu operandul `cota` = „21%” (deja 0,21), împarte a doua oară la 100 — TVA 1.050 lei în loc de 105.000 lei. Codul a evaluat corect o formulă greșită; verificarea nu are o regulă pentru asta.

## Cheia

- Nu. Trebuie colectată TVA de 105.000 lei (500.000 × 21%). Scutirea pentru livrarea terenurilor nu se aplică terenurilor construibile — teren construibil fiind orice teren, amenajat sau neamenajat, pe care se pot executa construcții conform legislației. Livrarea este taxabilă prin efectul legii, cu cota standard de 21%. Taxarea inversă nu se aplică, deoarece cumpărătorul nu este înregistrat în scopuri de TVA, deci vânzătorul colectează taxa.
- temei: Cod fiscal art. 292 alin. (2) lit. f) pct. 1; art. 291 alin. (1); art. 331 alin. (1); art. 307 alin. (1)
