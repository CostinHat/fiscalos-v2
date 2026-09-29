# Q2-TVA-07 — CALCUL

**Întrebarea:** O firmă cu perioadă fiscală lunară a oferit în aprilie 2026, în cadrul acțiunilor de protocol, 30 de cadouri a câte 80 lei și 10 cadouri a câte 250 lei (valori fără TVA), bunuri pentru care a dedus integral TVA la achiziție. Cât TVA trebuie să colecteze pentru aprilie 2026?

## Răspunsul — NU POT RĂSPUNDE

*La data de 30.04.2026, pentru o persoană impozabilă înregistrată în scopuri de TVA cu perioadă fiscală lunară, care a acordat gratuit bunuri în cadrul acțiunilor de protocol (TVA dedusă integral la achiziție), presupun că valorile date sunt per cadou, exclusiv TVA, și că bunurile sunt supuse cotei standard de TVA.*

Motiv: VERIFICAREA MECANICA a respins propunerea modelului: valoarea legala '2026' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare)

- `depasire_totala = numar_cadouri_mari * (valoare_cadou_mare - plafon_cadou)` = (10 × (250 − 100)) = **1500**
- `tva_colectata = depasire_totala * cota_standard` = (1500 × 21%) = **315**
- **Normele metodologice ale Codului fiscal (HG 1/2016) anexa, Titlul VII, pct. 7 alin. (12) lit. a)** — `hg_1_2016_norme_cod_fiscal#anexa/pct7~5/alin12/lita`
  > bunurile de mică valoare acordate gratuit în cadrul acțiunilor de protocol nu sunt considerate livrări de bunuri dacă valoarea fiecărui cadou oferit este mai mică sau egală cu plafonul de 100 lei, exclusiv TVA.
- **Normele metodologice ale Codului fiscal (HG 1/2016) anexa, Titlul VII, pct. 7 alin. (12) lit. a)** — `hg_1_2016_norme_cod_fiscal#anexa/pct7~5/alin12/lita`
  > În situația în care persoana impozabilă a oferit și cadouri care depășesc individual plafonul de 100 lei, exclusiv TVA, însumează valoarea depășirilor de plafon aferente unei perioade fiscale, care constituie livrare de bunuri cu plată, și colectează taxa, dacă taxa aferentă bunurilor respective este deductibilă total sau parțial.
- **Codul fiscal (Legea 227/2015) art. 291 alin. (1)** — `cod_fiscal_227_2015_consolidat#art291/alin1`
  > Cota standard se aplică asupra bazei de impozitare pentru operațiunile impozabile care nu sunt scutite de taxă sau care nu sunt supuse cotei reduse, iar nivelul acesteia este 21%.
- **Codul fiscal (Legea 227/2015) art. 270 alin. (8) lit. c)** — `cod_fiscal_227_2015_consolidat#art270/alin8/litc`
  > acordarea de bunuri de mică valoare, în mod gratuit, în cadrul acțiunilor de sponsorizare, de mecenat, de protocol/reprezentare, în condițiile stabilite prin normele metodologice.

Navigare: 5 pași; `claude-opus-5`; {'intrare': 8, 'iesire': 3613, 'cache_scriere': 5105, 'cache_citire': 36349} tokeni; $0.1404; 52 s

Pe fond (comparator): **NU POT** — VERIFICAREA MECANICA a respins propunerea modelului: valoarea legala '2026' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare)

## Cheia

- 315 lei TVA colectată. Calcul: cadourile de până la 100 lei (fără TVA) nu sunt livrări; pentru cele peste plafon se însumează doar depășirile: 10 × (250 − 100) = 1.500 lei bază impozabilă; TVA = 1.500 × 21% = 315 lei. Livrarea se consideră efectuată în ultima zi lucrătoare a lunii aprilie 2026 (30.04.2026); baza și TVA se înscriu în autofactura prevăzută la art. 319 alin. (8), inclusă în decontul pentru aprilie 2026.
- temei: HG 1/2016 (Norme metodologice), Titlul VII pct. 7 alin. (12) lit. a); Cod fiscal art. 270 alin. (8) lit. c); art. 291 alin. (1)
