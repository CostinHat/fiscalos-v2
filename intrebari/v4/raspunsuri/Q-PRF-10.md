# Q-PRF-10 — INCOMPLETA

**Întrebarea:** SRL-ul meu a avut în 2025 cifră de afaceri de 90.000 euro și are un salariat cu normă întreagă. Pot plăti impozit micro în 2026?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 31.12.2025, presupun o persoană juridică română (SRL) care nu desfășoară activități excluse de la regimul micro și care verifică, pentru anul fiscal 2026, condițiile de microîntreprindere la 31 decembrie 2025, având venituri realizate în 2025 de 90.000 euro și cel puțin un salariat cu normă întreagă.*

> **Da, din perspectiva plafonului și a salariatului: pentru 2026 limita veniturilor este echivalentul în lei a 100.000 euro, verificată pe baza veniturilor de la 31 decembrie 2025, iar 90.000 euro se încadrează sub această limită, iar condiția de a avea cel puțin un salariat este îndeplinită. Aplicarea regimului rămâne condiționată de îndeplinirea cumulativă și a celorlalte condiții de la 31 decembrie 2025 (structura capitalului social, lipsa dizolvării urmate de lichidare, deținerile asociaților de peste 25% într-o singură microîntreprindere, depunerea în termen a situațiilor financiare anuale).**

Citatul decisiv (`cod_fiscal_227_2015_consolidat#art54/alin3`):
> Pentru anul fiscal 2025/2026, limita veniturilor realizate, reprezentând echivalentul în lei a 250.000 euro, respectiv echivalentul în lei a 100.000 euro începând cu 1 ianuarie 2026, se verifică pe baza veniturilor realizate de către persoana juridică română la data de 31 decembrie 2024, respectiv la data de 31 decembrie 2025.

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 54 alin. (3)** — `cod_fiscal_227_2015_consolidat#art54/alin3` · valabil din 2025-01-01
  > Pentru anul fiscal 2025/2026, limita veniturilor realizate, reprezentând echivalentul în lei a 250.000 euro, respectiv echivalentul în lei a 100.000 euro începând cu 1 ianuarie 2026, se verifică pe baza veniturilor realizate de către persoana juridică română la data de 31 decembrie 2024, respectiv la data de 31 decembrie 2025.
- **Codul fiscal (Legea 227/2015) art. 47 alin. (1)** — `cod_fiscal_227_2015_consolidat#art47/alin1` · valabil din nedovedit
  > În sensul prezentului titlu, o microîntreprindere este o persoană juridică română care îndeplinește cumulativ următoarele condiții, la data de 31 decembrie a anului fiscal precedent:
- **Codul fiscal (Legea 227/2015) art. 47 alin. (1) lit. g)** — `cod_fiscal_227_2015_consolidat#art47/alin1/litg` · valabil din 2023-01-01
  > are cel puțin un salariat, cu excepția situației prevăzute la art. 48 alin. (3) ;
- derogare tratată: `og_16_2022_consolidat#artVI/alin2` — Excepție tranzitorie de la art. 47 alin. (1), adoptată prin OG 16/2022 pentru trecerea la noul regim de la acel moment (ani fiscali anteriori lui 2026); nu guvernează verificarea condițiilor la 31 decembrie 2025 pentru anul 2026, pentru care se aplică regula specială din art. 54 alin. (3).
- derogare tratată: `oug_25_2018#artI/pct3` — Excepție tranzitorie de la art. 47 alin. (1) introdusă prin OUG 25/2018, vizând situații de opțiune din anul 2018; nu privește cazul unui SRL cu un salariat care verifică plafonul pentru anul fiscal 2026.

### Navigarea (11 pași, 9 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "microîntreprinderi"}
2. `cauta` {"interogare": "plafon 100.000 euro microîntreprindere condiții"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art47/alin1"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art47"}
5. `cauta` {"interogare": "veniturile care nu au depășit echivalentul în lei a 250.000 euro"}
6. `cauta` {"interogare": "plafon venituri microîntreprindere 2026 100.000 euro condiția de la art. 47 alin. (1) lit. c)"}
7. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art54/alin3"}
8. `cauta` {"interogare": "art. 47 alin. (1) lit. c) au realizat venituri care nu au depășit echivalentul în lei a 100.000 euro microîntreprindere condiție"}
9. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art47/alin1/litg"}
10. `deschide` {"id": "oug_8_2026#art10/alin5"}
11. `cauta` {"interogare": "OUG 8/2026 articolul 47 alineatul (1) litera c) se modifică plafon microîntreprinderi"}

Apel: `claude-opus-5`, {'intrare': 18, 'iesire': 6283, 'cache_scriere': 13554, 'cache_citire': 102898} tokeni, $0.2933, 93 s

Pe fond: **GREȘIT** — articolul citat [('cf', '54')] nu e printre cele ale cheii [('cf', '47'), ('oug_8_2026', '6'), ('oug_8_2026', '10'), (None, '47'), ('oug_8_2026', '48'), ('oug_8_2026', '6')]

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți nu conțin norma care stabilește condițiile de încadrare ca microîntreprindere pentru anul fiscal următor - în special plafonul de venituri exprimat în echivalent euro (art. 47 din Codul fiscal) și regula de conversie a acestuia. Atomii disponibili se referă la definiția salariatului (art. 51 alin. (4)), la impozitul minim/specific pe cifra de afaceri (art. 18^1, 46^1, 46^2), la bonificația pentru 2025, la reținerea la sursă (art. 80) și la reglementări contabi…

## Cheia

- Depinde — trebuie clarificat: (1) dacă există întreprinderi legate (deținere/control >25% direct sau indirect, inclusiv asociat >25% cu PFA/II/IF), ale căror cifre de afaceri se cumulează la plafonul de 100.000 euro; (2) dacă situațiile financiare 2025 au fost depuse până la 31.03.2026; (3) dacă asociații >25% au desemnat-o ca singura micro; (4) dacă activitatea nu e exclusă (bancar, asigurări, jocuri de noroc, petrol/gaze). Doar cu 90.000 euro individual nu se poate răspunde
- temei: Cod fiscal art. 47 alin. (1) lit. c), g), h), i) și alin. (1^1) (mod. OUG 8/2026 art. 6 pct. 15-16, aplicabile încadrării în 2026 cf. art. 10 alin. (3) OUG 8/2026); art. 47 alin. (3) lit. f)-i); art. 48 alin. (2) (termen SF 31.03.2026 pentru 2026, mod. OUG 8/2026 art. 6 pct. 17)
