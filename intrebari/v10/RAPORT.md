# FiscalOS v2 — Pasul 11: C41 ca avertisment, C54, C55, iConta din starea comisă

Generat 29.09.2026 23:20 · ZIP: `/home/costin/ghid_incoming/fiscalos_v10_rezultat.zip`

> Fără rulare plătită (decizia 5). Efectele măsurate pe propunerile salvate ale seturilor 2 și 3; costul C54 — pe setul 4.

## 0. CERINȚE — decizii de arhitect, aplicate

| | Decizia | Cum e aplicată | Dovada |
|---|---|---|---|
| **C41/C49** | geamănul nejustificat nu mai respinge: devine AVERTISMENT în răspuns și în raport (decizie pe măsurătoare) | geamenii atomului decisiv, căutați în tot actul lui (nu doar printre atomii văzuți); nejustificați → `avertismente` + „[avertisment C41: …]” la finalul răspunsului | `test_navigare.test_C41_geamanul_nejustificat_al_atomului_decisiv_e_avertisment_nu_respingere` |
| **C54** | `deschide` arată geamenii numai ca id + temei, fără text; textul complet numai la cerere explicită | lista `atomi_cu_text_aproape_identic` = {id, temei}; geamenii nu mai devin „văzuți” (deci citabili) până nu sunt deschiși | `test_navigare.test_C41_deschide_arata_geamanul_din_acelasi_act` (extins) |
| **C55** | operanzii legali poartă valabil_din / valabil_pana; respins operandul a cărui valabilitate nu acoperă data faptului | `navigare.valabilitate_valoare`: nota de consolidare a atomului + textul din jurul valorii sau de la începutul atomului („începând cu (data de) D”, „în perioada D1–D2”); data faptului = `data_aplicarii` declarată pe operand (câmp nou, obligatoriu în schemă; „” = data de referință) | `test_navigare.test_C55_*` (4): HG 146/2026 art. 1 → valabil din 01.07.2026; 4.325 lei aplicat la 01.01.2026 respins |
| **iConta HEAD** | FiscalOS citește numai starea COMISĂ (git HEAD); `test_read_only` raportat la HEAD; instantaneu + inventar refăcute de pe HEAD | `iconta_head.py`: numai `rev-parse`, `ls-tree`, `cat-file`, cu `--no-optional-locks`; manifestul (`sursa_commit_git`, `blob_git` per fișier) și inventarul (`iconta_commit_git`) înregistrează commitul | `test_read_only` (2 probe noi): fiecare fișier citit = obiectul git de la commitul înregistrat; nicio citire din copia de lucru |

## Instantaneul de pe HEAD

HEAD-ul iConta: `85a811f6`. Față de instantaneul din 28.09 (luat din copia de lucru): 3 acte noi (Legea 114/1996, 180/2002, 196/2018), 6 acte aduse de iConta la forma consolidată (273/2006, 346/2002, 52/2011, 319/2006, OUG 41/2022, HG 1/2016), 4 PDF-uri înlocuite. **Modificarea necomisă din `core/common.py` (`CHIRIE_PF`) nu intră** — inventarul (147 de parametri) e identic cu cel vechi.

Detectorul C31 a semnalat 6 dintre actele noi/actualizate ca stricate; toate aduse din sursa oficială (C31/C35): Legea 196/2018, 273/2006, 319/2006, OUG 41/2022, Legea 114/1996 și Legea 52/2011. La ultimele două, căutarea dădea forma inițială și republicarea („LEGE (R)”, aceeași dată) — o regulă nouă, de clasă: republicarea e **același act**, nu ambiguitate. Detectorul iese din nou curat. Două corecturi ale rulării C31, raportate: fișierul de rezolvări era suprascris la fiecare rulare (acum se îmbină, cu istoricul rulărilor), iar o a doua rulare fără re-atomizare marca greșit actele abia aduse (regula corectată; înregistrările refăcute din manifest).

Efectul asupra propunerii: **`propuneri/v9/`** — aceleași clasificări (94/1/26/26) și aceiași atomi; referința la instantaneul de pe HEAD.

## Efectul pe propunerile salvate (re-notare; scorurile oficiale nu se schimbă)

| Set | Scor oficial | Comparatorul de acum | Verificarea de acum (C40, C41 avertisment, C49–C51, C55) |
|---|---|---|---|
| Setul 3 | 18/1/31 | 18/1/31 | **28/3/19** |
| Setul 2 | 28/7/15 | 30/5/15 | 28/4/18 |

Setul 3, schimbările:

- Q3-TVA-01: NU_POT → CORECT
- Q3-TVA-02: NU_POT → CORECT
- Q3-TVA-05: NU_POT → CORECT
- Q3-TVA-09: GRESIT → NU_POT
- Q3-PRF-02: NU_POT → CORECT
- Q3-PRF-04: NU_POT → CORECT
- Q3-SAL-02: NU_POT → CORECT
- Q3-SAL-07: NU_POT → GRESIT
- Q3-SAL-08: NU_POT → CORECT
- Q3-CPF-03: NU_POT → GRESIT
- Q3-CPF-08: NU_POT → CORECT
- Q3-CTB-01: NU_POT → CORECT
- Q3-CTB-03: NU_POT → CORECT
- Q3-CTB-09: NU_POT → GRESIT

Ce se vede, citit pe fond:

- Din cele 9 răspunsuri corecte pierdute de C41 pe setul 3, **8 trec acum**; Q3-PRF-09 rămâne respins de **C40** (termen scris direct).
- **Q3-SAL-07 trece acum — ca GREȘIT**, cu avertismentul C41 atașat. Greșeala lui (salariul minim de 4.325 lei, valabil de la 01.07.2026, aplicat CASS pe 2026, unde legea cere valoarea de la 01.01.2026) nu e prinsă: **C55 o prinde numai dacă modelul declară `data_aplicarii`**, iar propunerea salvată nu avea câmpul. Cu promptul nou, modelul trebuie să-l dea; efectul se vede pe setul 4.
- Q3-TVA-09 e prins de C50.
- Q3-CPF-03 ("un an de la 10.02.2026", fără data 10.02.2027) și Q3-CTB-09 (concluzia cheii, alt temei) trec ca GREȘIT — corecte pe fond, notare strictă.
- Q3-CPF-08 trece acum (CORECT): în v3 fusese respins de C17; după refacerea instantaneului, relația de derogare citată nu mai există în corpus — schimbare venită din corpus, nu din reguli.
- Avertismente C41 pe setul 3: Q3-TVA-05, Q3-PRF-04, Q3-SAL-07, Q3-SAL-08.

Setul 2: numai C40 mai respinge (Q2-PRF-05, Q2-SAL-05, Q2-CTB-05 — termene scrise direct; ultimul era o greșeală de fond).

## De decis

**C56 — Q3-SAL-07 trece ca răspuns greșit.** Prin trecerea C41 pe avertisment, singurul mecanism care îl oprea (întâmplător) nu mai respinge, iar C55 depinde de declarația modelului. *De decis:* se acceptă ca risc până la setul 4 (unde se vede dacă modelul declară `data_aplicarii`), sau C55 primește o regulă mecanică: dacă un atom citat spune „în vigoare la data de 1 ianuarie” / „de la începutul anului” pentru valoarea folosită, data aplicării e acea dată, nu data de referință?

## Operațiile, cu durata măsurată

| Operație | Durată | Cost |
|---|---|---|
| Instantaneul corpusului din iConta HEAD | 3.9 s | $0 |
| Stratul de text | 2.0 s | $0 |
| Atomizarea instantaneului | 3.1 s | $0 |
| Atomizarea actelor oficiale | 7.6 s | $0 |
| Inventarul iConta din HEAD | 8.8 s | $0 |
| Potrivirea | 13.4 s | $0 |
| Bancul de mutatii | 8.1 s | $0 |
| C31: aducerea celor 6 acte din portal (2 rulări: 42,7 s și 17,2 s) | 59,9 s | $0 |
| Re-verificarea propunerilor salvate ale seturilor 2 și 3 | 99.2 s | $0 |
| Propunerea v9 | 7,2 s | $0 |
