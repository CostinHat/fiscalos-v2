# Q-PRF-10 — INCOMPLETA

**Întrebarea:** SRL-ul meu a avut în 2025 cifră de afaceri de 90.000 euro și are un salariat cu normă întreagă. Pot plăti impozit micro în 2026?

## Stratul de navigare v5 — NU POT RĂSPUNDE

*La data de referință 28.09.2026, presupun un SRL persoană juridică română, cu venituri (cifră de afaceri) de 90.000 euro realizate în anul fiscal 2025 și cel puțin un salariat cu normă întreagă la 31.12.2025, fără întreprinderi legate ale căror venituri să se cumuleze, cu obiect de activitate care nu este exclus (bancar, asigurări, jocuri de noroc, petrol și gaze) și care îndeplinește și celelalte condiții (capital social nedeținut de stat, fără dizolvare urmată de lichidare, situații financiare anuale depuse în termen, asociați care dețin peste 25% la o singură microîntreprindere).*

Datele din întrebare: 2025-12-31, 2026-09-28 · data de referință aleasă: **2026-09-28** — Faptul întrebat este dreptul de a aplica impozitul pe veniturile microîntreprinderilor în anul fiscal 2026; cifra de afaceri 2025 este doar elementul de fapt verificat la 31.12.2025.

Motiv: VERIFICAREA MECANICA a respins propunerea modelului: valoarea legala '25' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare)

- **Codul fiscal (Legea 227/2015) art. 47 alin. (1) lit. c)** — `cod_fiscal_227_2015_consolidat#art47/alin1/litc` · valabil din 2026-02-25
  > a realizat venituri care nu au depășit echivalentul în lei a 100.000 euro. Cursul de schimb pentru determinarea echivalentului în euro este cel valabil la închiderea exercițiului financiar în care s-au înregistrat veniturile;
- **Codul fiscal (Legea 227/2015) art. 47 alin. (1)** — `cod_fiscal_227_2015_consolidat#art47/alin1` · valabil din nedovedit
  > În sensul prezentului titlu, o microîntreprindere este o persoană juridică română care îndeplinește cumulativ următoarele condiții, la data de 31 decembrie a anului fiscal precedent:
- **Codul fiscal (Legea 227/2015) art. 47 alin. (1) lit. g)** — `cod_fiscal_227_2015_consolidat#art47/alin1/litg` · valabil din 2023-01-01
  > are cel puțin un salariat, cu excepția situației prevăzute la art. 48 alin. (3)
- **Codul fiscal (Legea 227/2015) art. 47 alin. (1^1)** — `cod_fiscal_227_2015_consolidat#art47/alin1^1` · valabil din 2026-02-25
  > În aplicarea prevederilor alin. (1) lit. c) limita privind veniturile realizate se verifică luând în calcul veniturile realizate de persoana juridică română, cumulate cu veniturile întreprinderilor legate cu aceasta, iar veniturile care se iau în calcul sunt cele care constituie cifra de afaceri definită potrivit reglementărilor contabile aplicabile
- **Codul fiscal (Legea 227/2015) art. 47 alin. (3)** — `cod_fiscal_227_2015_consolidat#art47/alin3` · valabil din nedovedit
  > Nu intră sub incidența prezentului titlu următoarele persoane juridice române:
- derogare tratată: `og_16_2022_consolidat#artVI/alin2` — Excepție aplicabilă doar contribuabililor care au fost sub incidența Legii nr. 170/2016 (impozit specific HORECA) până la 31.12.2022; întrebarea nu descrie o astfel de situație, deci nu se aplică.
- derogare tratată: `oug_25_2018#artI/pct3` — Excepție privind opțiunea microîntreprinderilor cu capital social subscris de cel puțin 45.000 lei și cel puțin 2 salariați de a trece la impozit pe profit; societatea are un singur salariat și nu se invocă o astfel de opțiune, deci nu se aplică.

### Navigarea (9 pași, 6 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "microîntreprinderi"}
2. `cauta` {"interogare": "condiții microîntreprindere 250.000 euro salariat"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art47/alin1"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art47/alin1/litc"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art47"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art47/alin1^1"}
7. `deschide` {"id": "og_16_2022_consolidat#artVI/alin2"}
8. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art47/alin3"}
9. `deschide` {"id": "oug_25_2018#artI/pct3"}

Apel: `claude-opus-5`, {'intrare': 12, 'iesire': 4612, 'cache_scriere': 9192, 'cache_citire': 59948} tokeni, $0.2028, 60 s

Pe fond (comparator): **NU POT** — INCOMPLETA: motorul s-a abţinut, iar cheia spune si ea ca lipsesc date

## v4 — RĂSPUNS, pe fond GREȘIT

> Da, din perspectiva plafonului și a salariatului: pentru 2026 limita veniturilor este echivalentul în lei a 100.000 euro, verificată pe baza veniturilor de la 31 decembrie 2025, iar 90.000 euro se încadrează sub această limită, iar condiția de a avea cel puțin un salariat este îndeplinită. Aplicarea regimului rămâne condiționată de îndeplinirea cumulativă și a celorlalte condiții de la 31 decembrie 2025 (structura capitalului social, lipsa dizolvării urmate de lichidare, deținerile asociaților d…

## Cheia

- Depinde — trebuie clarificat: (1) dacă există întreprinderi legate (deținere/control >25% direct sau indirect, inclusiv asociat >25% cu PFA/II/IF), ale căror cifre de afaceri se cumulează la plafonul de 100.000 euro; (2) dacă situațiile financiare 2025 au fost depuse până la 31.03.2026; (3) dacă asociații >25% au desemnat-o ca singura micro; (4) dacă activitatea nu e exclusă (bancar, asigurări, jocuri de noroc, petrol/gaze). Doar cu 90.000 euro individual nu se poate răspunde
- temei: Cod fiscal art. 47 alin. (1) lit. c), g), h), i) și alin. (1^1) (mod. OUG 8/2026 art. 6 pct. 15-16, aplicabile încadrării în 2026 cf. art. 10 alin. (3) OUG 8/2026); art. 47 alin. (3) lit. f)-i); art. 48 alin. (2) (termen SF 31.03.2026 pentru 2026, mod. OUG 8/2026 art. 6 pct. 17)
