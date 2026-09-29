# FiscalOS v2 — Pasul 9: deciziile C40–C46

Generat 29.09.2026 13:28 · ZIP: `/home/costin/ghid_incoming/fiscalos_v8_rezultat.zip`

> **Fără rulare plătită (decizia 8): setul 2 e consumat.** Efectele se măsoară fără apel pe ieșirile salvate, acolo unde se poate; restul se măsoară pe setul 3. Singurul apel: o verificare a formei cererii C44 pe un exemplu sintetic ($0,0039).

## 0. CERINȚE — decizii de arhitect, aplicate

| | Decizia | Cum e aplicată | Dovada |
|---|---|---|---|
| **C40** | orice termen calendaristic din răspuns trece prin `termen_efectiv`; altfel, respins | `navigare.verifica_termene`: o dată în context de termen („până la”, „cel târziu”, „termen”, „se depune/plătește”, „inclusiv”) trebuie să fie rezultatul unui `termen_efectiv` evaluat de cod sau un fapt al cazului, literal în întrebare. Nu se ating: datele de început („curge de la 1 ianuarie”), regulile recurente fără lună („25 a lunii următoare”), sufixul cu data de referință | `test_navigare.test_C40_*` (3) |
| **C41** | la două alineate cu text aproape identic, alegerea se justifică prin condiția care le deosebește, citată; fără justificare, abținere | „aproape identic” = fragment identic de ≥ 100 de caractere, alt articol (măsurat: perechea CF 319(3)/320(3) are 162; din 11.165 de perechi aleatoare, niciuna ≥ 80). `deschide` arată acum geamenii din același act; câmpul `alegeri_temei` (atom, alternativă, condiție literală din atom care NU e în alternativă); `navigare.verifica_alegeri_temei` | `test_navigare.test_C41_*` (5), inclusiv perechea reală |
| **C42** | comparatorul: formulări pentru zero și date cu an relativ, defect de clasă, înainte/după pe ieșirile salvate | zero: „nu restituie”, „nu implică (efectuarea de) ajustări”, „nicio ajustare”; data „zi lună … a anului următor/curent” față de anul datei de referință declarate | `test_intrebari.test_C42_*` (2), în ambele direcții |
| **C43** | când legea cuantifică consecința (cauțiune, amendă, prag), răspunsul o dă, cu calculul și temeiul | regulă în prompt. **Nu are verificare mecanică**: atomul consecinței (de ex. Legea 70/2015 art. 12) nu e, de obicei, cel citat pentru regulă, deci codul nu poate ști că lipsește. Se măsoară pe setul 3 | — |
| **C44** | răspunsul final pe ieșire structurată, într-o tură fără unelte | unealta `raspunde` a dispărut; navigarea se încheie când modelul nu mai cere unelte, apoi o tură cu `tool_choice: none` + `output_config.format` (schema răspunsului); validarea C23 și decodarea C33 rămân ca plasă, cu o reîncercare | `test_navigare.test_C44_*` (client simulat); forma cererii verificată pe API: acceptată |
| **C45** | numerele scrise în litere sunt operanzi valizi, forma literală în atom, conversia declarată | `navigare.numar_din_litere` (unități, zeci, sute, fracții: jumătate … zecime); calculul afișează „conversie C45: „cincime” (în litere în atom) = 0,20” | `test_navigare.test_C45_*` (2) |
| **C46** | orice cifră din răspuns e citată literal sau rezultat de calcul | confirmat: verificatorul o impunea deja (C13 + cifrele din răspuns în citate/întrebare); regula e acum și în prompt | `test_navigare.test_C46_*` |

## C42 — re-notarea (scorul oficial al setului 2 rămâne 28/7/15)

| Rulare | Corpus | Înainte | După | Schimbări |
|---|---|---|---|---|
| setul 2 (485ffc3) | `8b3269f` | 28/7/15 | 30/5/15 | Q2-TVA-09 GRESIT→CORECT, Q2-PRF-05 GRESIT→CORECT |
| setul 1: navigare v5 + C33 | `778e826` | 37/2/11 | 37/2/11 | — |
| setul 1: navigare v5 | `778e826` | 35/2/13 | 35/2/13 | — |
| setul 1: navigare v4 | `d35c21a` | 20/15/15 | 20/15/15 | — |
| setul 1: semantic v3 | `7eb6fa0` | 11/7/32 | 11/7/32 | — |

**Setul 2, re-notat (C42): 30/5/15** — raportat separat, ca re-notare; scorul oficial al măsurătorii finale rămâne **28/7/15**.

## C40 și C41 pe propunerile salvate ale setului 2 (fără apel)

Navigarea reluată determinist din pașii salvați; propunerile vechi trecute prin verificarea nouă. **Ambele greșeli de fond ale setului 2 sunt acum prinse:** Q2-TVA-05 prin C41 (geamănul art. 319 alin. (3) e arătat acum de `deschide` lângă art. 320 alin. (3), iar alegerea nejustificată e respinsă) și Q2-CTB-05 prin C40 („31 mai” scris direct, fără `termen_efectiv`).

Costul, ca **limită superioară**: 12 răspunsuri CORECTE vechi ar fi respinse — propunerile vechi nu aveau câmpul `alegeri_temei` și nu fuseseră cerute să treacă termenele prin `termen_efectiv`. Cu promptul nou, modelul trebuie să dea justificarea și calculul; câte abțineri rămân se vede numai pe setul 3.

| Id | Verdict oficial | C40 | C41 (gemeni fără justificare) |
|---|---|---|---|
| Q2-TVA-05 | GRESIT | — | 1 |
| Q2-PRF-03 | CORECT | — | 4 |
| Q2-PRF-04 | CORECT | — | 1 |
| Q2-PRF-05 | GRESIT | 25 iunie | 2 |
| Q2-PRF-07 | CORECT | — | 4 |
| Q2-PRF-09 | CORECT | — | 1 |
| Q2-SAL-02 | CORECT | — | 2 |
| Q2-SAL-05 | CORECT | 14.07.2026 | 0 |
| Q2-SAL-06 | CORECT | — | 4 |
| Q2-SAL-09 | CORECT | — | 2 |
| Q2-CPF-02 | CORECT | — | 1 |
| Q2-CPF-05 | CORECT | — | 1 |
| Q2-CPF-09 | CORECT | — | 1 |
| Q2-CTB-04 | CORECT | — | 4 |
| Q2-CTB-05 | GRESIT | 31 mai, 31 mai | 2 |

### De decis

**C47 — Riscul C40/C41 pe setul 3.** Pe propunerile vechi, verificarea nouă ar fi respins 12 răspunsuri corecte (limită superioară: câmpurile noi lipseau). Dacă modelul nu dă justificarea/termenul, crește abținerea. *De decis după setul 3:* se păstrează respingerea, sau C41 devine avertisment când alternativa e din alt act (de ex. OUG 8/2026 care reproduce CF art. 26)?

**C48 — C43 nu are verificare mecanică.** Consecința cuantificată stă, de obicei, în alt articol decât regula (Legea 70/2015: regula la art. 4, amenda la art. 12). Codul nu poate ști că lipsește. *De decis:* se acceptă ca regulă de prompt, măsurată pe setul 3, sau se construiește o relație „sancțiune pentru art. X” (ca C17), din care verificarea să ceară tratarea ei?

## Operațiile, cu durata măsurată

| Operație | Durată | Cost |
|---|---|---|
| C42 inainte/dupa pe 5 rulari (fiecare pe corpusul ei) | 10.9 s | $0 |
| C40/C41 pe propunerile salvate ale setului 2 (reluarea navigării, 35 de răspunsuri) | 37,3 s | $0 |
| Verificarea formei cererii C44 pe API (exemplu sintetic, 666+21 tokeni) | — | $0,0039 |
| Probe: 175 | — | $0 |
