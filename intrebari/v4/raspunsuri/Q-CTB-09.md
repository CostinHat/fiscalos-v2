# Q-CTB-09 — CALCUL

**Întrebarea:** PFA în sistem real, venit net anual 2026 de 60.000 lei, nepensionar, fără salariu sau alte venituri. Cât este CAS minim datorat pentru 2026 și până când se depune D212?

## Stratul de navigare (v4) — NU POT RĂSPUNDE

*La data de referință 28.09.2026, pentru o persoană fizică autorizată care determină venitul net anual în sistem real pentru anul fiscal 2026 (60.000 lei venit net), nepensionară, fără venituri din salarii sau alte categorii de venituri care s-ar cumula în plafon, presupun că nu se încadrează în cursul anului în categoriile exceptate de la plata CAS.*

Motiv: modelul s-a abţinut: Regula de bază este identificată: la un venit net cuprins între 12 și 24 de salarii minime brute pe țară, baza anuală de calcul al CAS este nivelul de 12 salarii minime brute pe țară, iar Declarația unică se depune până la 25 mai inclusiv a anului următor celui de realizare a veniturilor (deci pentru 2026, în anul următor). Nu pot însă indica suma CAS minim datorat: aceasta ar presupune un calcul (cotă × 12 salarii minime), iar în atomii obținuți nu apar nici valoarea salariului minim brut pe țară pentru 2026, nici cota CAS; de asemenea, încadrarea celor 60.000 lei între cele două plafoane depinde de valoarea salariului minim, care nu este dovedită prin atomi.

- **Codul fiscal (Legea 227/2015) art. 148 alin. (2) lit. a)** — `cod_fiscal_227_2015_consolidat#art148/alin2/lita` · valabil din nedovedit
  > nivelul de 12 salarii minime brute pe țară, în cazul veniturilor realizate cuprinse între 12 salarii minime brute pe țară inclusiv și 24 de salarii minime brute pe țară; ...
- **Codul fiscal (Legea 227/2015) art. 122 alin. (3)** — `cod_fiscal_227_2015_consolidat#art122/alin3` · valabil din nedovedit
  > Declarația unică privind impozitul pe venit și contribuțiile sociale datorate de persoanele fizice se completează și se depune la organul fiscal competent, pentru fiecare an fiscal, până la data de 25 mai inclusiv a anului următor celui de realizare a veniturilor.
- **Codul fiscal (Legea 227/2015) art. 148 alin. (1)** — `cod_fiscal_227_2015_consolidat#art148/alin1` · valabil din nedovedit
  > a căror valoare anuală cumulată este cel puțin egală cu 12 salarii minime brute pe țară, datorează contribuția de asigurări sociale la o bază de calcul stabilită potrivit alin. (2) .
- derogare tratată: `cod_fiscal_227_2015_consolidat#art151/alin3` — Excepția privește contribuabilii care în cursul anului de realizare a venitului intră în categoria persoanelor exceptate de la plata CAS potrivit art. 150 (recalculare a plafonului pe lunile de activitate). În cazul descris (PFA nepensionar, fără alte venituri, care desfășoară activitatea pe tot anu…

### Navigarea (12 pași, 7 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "baza de calcul al contribuției de asigurări sociale datorate de persoanele fizice care realizează venituri din activități independente"}
2. `cauta` {"interogare": "declarația unică termen 25 mai venit estimat activități independente"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art148"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art122/alin3"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art148/alin1"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art148/alin2"}
7. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art148/alin2/lita"}
8. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art151/alin3"}
9. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art148/alin3"}
10. `cauta` {"interogare": "salariul de bază minim brut pe țară garantat în plată 2026 lei lunar"}
11. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art135^1/alin1"}
12. `cuprins` {"act": "hg_146_2026_salariu_minim", "filtru": "salariul"}

Apel: `claude-opus-5`, {'intrare': 14, 'iesire': 3718, 'cache_scriere': 12255, 'cache_citire': 86727} tokeni, $0.2130, 65 s

Pe fond: **NU POT** — modelul s-a abţinut: Regula de bază este identificată: la un venit net cuprins între 12 și 24 de salarii minime brute pe țară, baza anuală de calcul al CAS este nivelul de 12 salarii minime brute pe ț

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți stabilesc doar condiția de plafon (cel puțin 12 salarii minime brute pe țară) pentru datorarea CAS, dar nu conțin nici cota contribuției, nici valoarea salariului minim brut pe țară pentru 2026, iar suma CAS ar rezulta dintr-un calcul (bază × cotă) care nu apare literal în niciun atom. De asemenea, termenul de depunere a Declarației unice prevăzut la art. 122 alin. (3) nu este prezent în context; atomul art. 122 alin. (5) menționează data de 25 mai doar pentru…

## Cheia

- CAS minim 12.150 lei = 25% × 48.600 lei (12 salarii minime × 4.050 lei, salariul minim în vigoare la 01.01.2026; NU 4.325 lei, în vigoare de la 01.07.2026). Venitul se încadrează între 12 și 24 salarii minime (48.600-97.200 lei). D212 până la 25 mai 2027 inclusiv.
- temei: Legea 227/2015 art. 135^1 alin. (3), art. 138 lit. a), art. 148 alin. (1)-(3), art. 122 alin. (3); HG 1506/2024 art. 1 (4.050 lei de la 01.01.2025); HG 146/2026 art. 1-2 (4.325 lei de la 01.07.2026)
