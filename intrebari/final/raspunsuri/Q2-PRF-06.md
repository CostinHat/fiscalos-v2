# Q2-PRF-06 — CALCUL

**Întrebarea:** SRL plătitoare de impozit pe profit, anul fiscal 2026: capital social subscris și vărsat 40.000 lei, rezervă legală existentă la 01.01.2026 = 5.000 lei (dedusă anterior), profit contabil 2026 = 84.000 lei, cheltuiala cu impozitul pe profit = 16.000 lei. Ce sumă din rezerva legală constituită pentru 2026 este deductibilă fiscal?

## Răspunsul — NU POT RĂSPUNDE

*La data de referință 01.01.2026, pentru o societate cu răspundere limitată plătitoare de impozit pe profit care constituie rezervă legală în anul fiscal 2026, presupunând că nu au avut loc reorganizări, diminuări de capital social sau utilizări ale rezervei legale, iar rezerva legală dedusă anterior este de 5.000 lei la un capital social subscris și vărsat de 40.000 lei.*

Motiv: VERIFICAREA CALCULULUI a respins propunerea: operandul cincime='5' nu apare literal in fragmentul lui

- `baza = profit_contabil + cheltuiala_impozit_profit` = (84.000 + 16.000) = **100.000**
- `limita_cota = baza * cota_rezerva` = (100.000 × 5%) = **5.000**
- `plafon = capital_social / cincime` = (40.000 ÷ 5) = **8.000**
- `rezerva_deductibila = min(limita_cota, plafon - rezerva_existenta)` = min(5.000, (8.000 − 5.000)) = **3.000**
- **Codul fiscal (Legea 227/2015) art. 26 alin. (1) lit. a)** — `cod_fiscal_227_2015_consolidat#art26/alin1/lita`
  > rezerva legal" + "ă este deductibilă în limita unei cote de 5% aplicate asupra profitului contabil, la care se adaugă cheltuielile cu impozitul pe profit, până ce aceasta va atinge a cincea parte din capitalul social subscris și vărsat sau din patrimoniu, după caz;

Navigare: 4 pași; `claude-opus-5`; {'intrare': 10, 'iesire': 5254, 'cache_scriere': 6760, 'cache_citire': 45365} tokeni; $0.1963; 73 s

Pe fond (comparator): **NU POT** — VERIFICAREA CALCULULUI a respins propunerea: operandul cincime='5' nu apare literal in fragmentul lui

## Cheia

- 3.000 lei. Pas 1: baza = profit contabil + cheltuiala cu impozitul pe profit = 84.000 + 16.000 = 100.000 lei. Pas 2: 5% × 100.000 = 5.000 lei. Pas 3: plafonul total al rezervei = a cincea parte din capitalul social subscris și vărsat = 40.000 / 5 = 8.000 lei; spațiu disponibil = 8.000 − 5.000 = 3.000 lei. Pas 4: deductibil = min(5.000; 3.000) = 3.000 lei. Rezerva se calculează cumulat de la începutul anului.
- temei: Cod fiscal art. 26 alin. (1) lit. a); HG 1/2016 (Norme metodologice), Titlul II pct. 19 alin. (1)
