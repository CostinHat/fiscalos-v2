# Q2-PRF-08 — CAPCANA

**Întrebarea:** SRL A (plătitoare de impozit pe profit) deține din 2020 5% din SRL B (plătitoare de impozit pe profit). Prin hotărârea AGA din aprilie 2026, B distribuie dividende din profitul anului 2025 și plătește pe 15.06.2026 lui A dividende brute de 100.000 lei. Contabilul lui B spune: „dividendele primite de la o persoană juridică română sunt neimpozabile la beneficiar, deci nu reținem impozit”. Are dreptate? Ce impozit se datorează?

## Răspunsul — NU POT RĂSPUNDE

*La data de referință 15.06.2026, presupun două societăți române plătitoare de impozit pe profit (SRL-uri), A deținând din 2020 doar 5% din capitalul lui B, dividende distribuite prin AGA din aprilie 2026 din profitul 2025 și plătite efectiv la 15.06.2026, fără an fiscal modificat și fără alte scutiri speciale.*

Motiv: VERIFICAREA MECANICA a respins propunerea modelului: citatul NU e verbatim in atomul cod_fiscal_227_2015_consolidat#art43/alin4/lita; valoarea legala '5' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare); valoarea legala '16' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare); valoarea legala '25' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare)

- `impozit_pe_dividende = dividend_brut * cota / 100` = ((100.000 × 16%) ÷ 100) = **160**
- **Codul fiscal (Legea 227/2015) art. 43 alin. (4) lit. a)** — `cod_fiscal_227_2015_consolidat#art43/alin4/lita`
  > (i) de tine minimum 10% din titlurile de participare ale persoanei juridice române care plătește dividendele

Navigare: 10 pași; `claude-opus-5`; {'intrare': 16, 'iesire': 6141, 'cache_scriere': 13137, 'cache_citire': 94169} tokeni; $0.2828; 90 s

Pe fond (comparator): **NU POT** — VERIFICAREA MECANICA a respins propunerea modelului: citatul NU e verbatim in atomul cod_fiscal_227_2015_consolidat#art43/alin4/lita; valoarea legala '5' nu apare in niciun citat (C13: o valoare legal

## Cheia

- Nu. B trebuie să rețină 16.000 lei impozit pe dividende (16% × 100.000 lei, cotă aplicabilă dividendelor distribuite începând cu 01.01.2026) și să îl declare și plătească până la 27.07.2026 (termenul de 25 a lunii următoare plății cade sâmbătă, 25.07.2026, și se prelungește la prima zi lucrătoare). Scutirea de la reținere se aplică doar dacă beneficiarul deține minimum 10% din titlurile plătitorului pe o perioadă de un an împlinit la data plății (plus condițiile de formă și plată a impozitului pe profit); A deține doar 5%. Separat, la A dividendul rămâne venit neimpozabil la calculul rezultatului fiscal — neimpozabilitatea la beneficiar nu elimină obligația de reținere la sursă a plătitorului.
- temei: Cod fiscal art. 43 alin. (1), (2) și (4); art. 23 lit. a); Legea 207/2015 art. 75; Legea 134/2010 (Codul de procedură civilă) art. 181 alin. (2)
