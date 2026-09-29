# Q2-CTB-07 — CALCUL

**Întrebarea:** O societate pe acțiuni are capital social 400.000 lei și un fond de rezervă legală constituit până la 31.12.2024 de 70.000 lei. Profitul exercițiului 2025 (baza de calcul pentru rezerva legală) este 300.000 lei. Ce sumă trebuie repartizată obligatoriu la rezerva legală din profitul 2025?

## Răspunsul — NU POT RĂSPUNDE

*La data de referință 31.12.2025, pentru o societate pe acțiuni română supusă Legii 31/1990, care repartizează profitul exercițiului 2025 (300.000 lei) la rezerva legală, având capital social 400.000 lei și rezervă legală deja constituită 70.000 lei; presupun că fondul de rezervă nu s-a micșorat și că nu există sume care se includ suplimentar în rezervă (excedent din vânzarea acțiunilor peste valoarea nominală).*

Motiv: VERIFICAREA CALCULULUI a respins propunerea: operandul parte_capital='5' nu apare literal in fragmentul lui

- `plafon_rezerva = capital_social / parte_capital` = (400.000 ÷ 5) = **80.000**
- `spatiu_ramas = plafon_rezerva - rezerva_existenta` = (80.000 − 70.000) = **10.000**
- `cota_5_din_profit = profit * cota / 100` = ((300.000 × 5) ÷ 100) = **15.000**
- `repartizare = min(cota_5_din_profit, spatiu_ramas)` = min(15.000, 10.000) = **10.000**
- **Legea 31/1990 art. 183 alin. (1)** — `legea_31_1990_societatile#art183/alin1`
  > Din profitul societății se va prelua, în fiecare an, cel puțin 5% pentru formarea fondului de rezervă, până ce acesta va atinge minimum a cincea parte din capitalul social.
- **Codul fiscal (Legea 227/2015) art. 26 alin. (1) lit. a)** — `cod_fiscal_227_2015_consolidat#art26/alin1/lita`
  > rezerva legală este deductibilă în limita unei cote de 5% aplicate asupra profitului contabil, la care se adaugă cheltuielile cu impozitul pe profit, până ce aceasta va atinge a cincea parte din capitalul social subscris

Navigare: 4 pași; `claude-opus-5`; {'intrare': 8, 'iesire': 3502, 'cache_scriere': 3264, 'cache_citire': 33550} tokeni; $0.1248; 50 s

Pe fond (comparator): **NU POT** — VERIFICAREA CALCULULUI a respins propunerea: operandul parte_capital='5' nu apare literal in fragmentul lui

## Cheia

- 10.000 lei. Se preia cel puțin 5% din profit până când fondul de rezervă atinge a cincea parte din capitalul social. 5% × 300.000 = 15.000 lei, dar plafonul este 400.000 / 5 = 80.000 lei, iar rezerva existentă e 70.000 lei, deci obligatoriu se completează doar 80.000 − 70.000 = 10.000 lei.
- temei: Legea 31/1990 art. 183 alin. (1)
