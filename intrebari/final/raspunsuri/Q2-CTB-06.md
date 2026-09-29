# Q2-CTB-06 — CALCUL

**Întrebarea:** O firmă evaluează ieșirile de materii prime prin metoda FIFO. În martie 2026: stoc inițial 100 kg × 10 lei/kg; intrare pe 05.03 de 200 kg × 12 lei/kg; intrare pe 10.03 de 100 kg × 13 lei/kg; pe 15.03 se dau în consum 250 kg. Care este valoarea consumului și valoarea stocului rămas?

## Răspunsul — NU POT RĂSPUNDE

*La data de referință 31.03.2026, presupun o entitate care ține contabilitatea potrivit reglementărilor contabile privind situațiile financiare anuale individuale (OMFP 1802/2014), cu inventar permanent al stocurilor de materii prime și cu politica contabilă de evaluare a ieșirilor prin metoda FIFO, așa cum precizează întrebarea; loturile și cantitățile sunt cele din enunț.*

Motiv: VERIFICAREA MECANICA a respins propunerea modelului: cifra '150' din raspuns nu apare literal in citate sau in intrebare

- `consum = cant_stoc_initial * pret_stoc_initial + (cant_consum - cant_stoc_initial) * pret_intrare_05` = ((100 × 10) + ((250 − 100) × 12)) = **2800**
- `stoc_ramas = (cant_intrare_05 - (cant_consum - cant_stoc_initial)) * pret_intrare_05 + cant_intrare_10 * pret_intrare_10` = (((200 − (250 − 100)) × 12) + (100 × 13)) = **1900**
- **OMFP 1802/2014 anexa, pct. 96 alin. (3)** — `omfp_1802_2014#anexa/pct96/alin3`
  > Potrivit metodei "primul intrat-primul ieșit" (FIFO), bunurile ieșite din gestiune se evaluează la costul de achiziție sau de producție al primei intrări (lot). Pe măsura epuizării lotului, bunurile ieșite din gestiune se evaluează la costul de achiziție sau de producție al lotului următor, în ordine cronologică.
- **OMFP 1802/2014 anexa, pct. 95 alin. (1)** — `omfp_1802_2014#anexa/pct95/alin1`
  > La data ieșirii din entitate sau la darea în consum, bunurile se evaluează și se scad din gestiune la valoarea lor de intrare sau valoarea la care sunt înregistrate în contabilitate

Navigare: 5 pași; `claude-opus-5`; {'intrare': 10, 'iesire': 3540, 'cache_scriere': 8327, 'cache_citire': 57431} tokeni; $0.1693; 48 s

Pe fond (comparator): **NU POT** — VERIFICAREA MECANICA a respins propunerea modelului: cifra '150' din raspuns nu apare literal in citate sau in intrebare

## Cheia

- 2.800 lei valoarea consumului; stoc rămas 1.900 lei. Calcul FIFO: se epuizează întâi primul lot: 100 kg × 10 = 1.000 lei; restul de 150 kg din lotul următor: 150 × 12 = 1.800 lei; total ieșire 2.800 lei. Stoc rămas: 50 kg × 12 = 600 lei + 100 kg × 13 = 1.300 lei = 1.900 lei (verificare: 1.000 + 2.400 + 1.300 = 4.700 − 2.800 = 1.900).
- temei: OMFP 1802/2014, Reglementări contabile, pct. 96 alin. (1) lit. b); pct. 96 alin. (3)
