## 0. CERINȚE — decizii de arhitect

### Aplicate în acest pas

| | Decizia | Cum e aplicată |
|---|---|---|
| **C18** | candidatul, la nivelul cel mai fin neambiguu; mai multe litere cu valoarea → articolul, cu literele ca opțiuni | `potrivire.potriveste`: strămoșul comun + `optiuni`; `propuneri/v5/temeiuri_candidate.json` (`ambiguu`, `optiuni`) |
| **C19** | anexele din instantaneu, textul ordinului din sursa oficială, fiecare parte cu data ei | `potrivire.COMPUSE`: OPANAF 3769/2015 = atomii oficiali ai ordinului + 91 de atomi ANEXA din instantaneu, fiecare cu `parte` și `data_formei` |
| **C20** | abținerea în plus e acceptată; datele de expirare nu se caută acum | neschimbat: plasa (b) rămâne pe dispozițiile tranzitorii citate |
| **C21** | motorul lexical păstrează plasa și rămâne doar referință de $0 | rulat o dată pe corpusul de acum, fără nicio optimizare |
| **C22** | V2 reparat acum, efectul măsurat în rularea de la punctul 8 | `surse_oficiale._aplatizeaza_note` (nota ⟦NOTĂ⟧ lipită de alineatul-gazdă) + `nota_tranzitorie` pe articolele romane din codurile arabe (281, 0 în CF); efectul — în secțiunea „Efectul V2" |
| **6** | stratul semantic trece la navigare structurală, cu pași limitați; căutarea lexicală doar punct de intrare; verificarea mecanică neschimbată | `fiscalos/navigare.py`: unelte `cauta` / `cuprins` / `deschide` (structură + relații de derogare/modificare în ambele sensuri) / `raspunde`; limită 12 pași; modelul poate cita numai atomi arătați de unelte; `semantic.verifica` neschimbat |
| **7** | modelul nu calculează: formulă + operanzi cu sursă literală; codul evaluează; operand fără sursă → respins | `navigare.evalueaza_calcule`: numai `+ - * /`, `min`, `max`, `zile(a,b)`; fiecare operand — valoare literală în fragment, fragment verbatim în atom arătat sau în întrebare; C13: o valoare legală nu vine din întrebare; constantele permise fără sursă: 1 și 100; 14 probe adversariale în `test_navigare.py` |

### Defecte de clasă găsite după comparație — NEREPARATE (pasul se oprește după rulare, decizia 8)

Scorul de mai sus e cel măsurat, fără nicio reparație. Citirea celor 17 GREȘIT, întrebare cu
întrebare (lectura mea, de verificat): **6 sunt greșeli de fond ale răspunsului** (Q-PRF-04 cota 1%
în loc de 0,5%; Q-TVA-06 și Q-TVA-07 fără data concretă și amânarea de weekend; Q-PRF-09 fără cota de
16%; Q-PRF-10 răspunde „Da" la o întrebare INCOMPLETA; Q-CTB-02 concluzie corectă pe alt temei), iar
**11 vin din defectele de mai jos**, nu din răspunsul pe fond.

**C23 — Parametrii scurși în apelul final (N1).** La 7 din 50 de întrebări (Q-TVA-03, Q-PRF-02,
Q-PRF-03, Q-CPF-01, Q-CPF-07, Q-CTB-03, Q-CTB-08), modelul a scris în câmpul `declaratie` al uneltei
`raspunde` textul celorlalte câmpuri, cu marcaj de parametri (`</declaratie><parameter
name="raspuns">…`), iar `raspuns` a rămas `"x"`, `"-"`, `""` sau `"."`. În 5 dintre ele textul scurs
conține faptul din cheie; 3 au ieșit GREȘIT (răspuns gol), 2 NU POT („nicio citare"). *De decis:*
răspunsul final trece pe ieșire structurată (`output_config.format`, ca în v3 — acolo defectul nu a
apărut în 100 de apeluri), într-o tură finală fără unelte; sau se păstrează unealta și orice marcaj
`<parameter` într-un câmp respinge propunerea și cere reemiterea (o tură în plus, cost).

**C24 — Gaură în verificator: răspunsul gol trecea (N2).** Verificarea „răspuns gol" din
`semantic.verifica` stătea în ramura C17 (b), deci rula numai când contextul avea derogări. 3
răspunsuri cu `raspuns` = `"x"` / `"-"` / `""` au trecut ca RĂSPUNS (cu atomi citați verbatim, dar
fără conținut). Nu a afectat v2/v3 (ieșirea structurată nu a produs niciodată un răspuns gol).
*Recomandare:* reparat necondiționat, cu probă adversarială. Cere autorizare, fiindcă atinge
verificatorul „neschimbat" din decizia 6.

**C25 — C13 pe operanzii din întrebare, prea larg (N3).** „valoare fiscală 100.000 lei" din
întrebare a fost tratat ca valoare legală (cuvântul „valoare" din euristica C13), iar Q-CTB-03 —
corect în v3, 65.000 lei — a fost respins. *De decis:* pentru operanzii din întrebare, valoare
legală = procent sau termen (zile/luni/ani); o sumă în lei/euro din întrebare e fapt al cazului.

**C26 — Anexele actelor oficiale, atomizate sub ultimul articol (N4).** Reglementările contabile
din OMFP 1802/2014 (pct. 67, 238, 372…), anexele OPANAF 3769/2015 și 705/2020 ajung, în forma
oficială, copii ale ultimului articol: temeiul iese „OMFP 1802/2014 art. 12 alin. (2)" în loc de
„pct. 238 alin. (2)". Faptul e corect, articolul greșit: Q-CTB-04, Q-CTB-05, Q-CTB-06 (și același
defect de structură la Codul muncii din instantaneu, Q-SAL-10: `art281/alin7~6`). *De decis:* nivel
`anexa → punct` în atomizarea oficială (afectează și potrivirea din propunere, deci v6).

**C27 — Data de referință a unei întrebări cu doi ani (N7).** Q-PRF-04 („cifra de afaceri 2025 …
cât impozit datorează pentru 2026?") a primit data 31.12.2025, deci R-VALAB a ascuns CF art. 18^1
alin. (16) („Pentru anul fiscal 2026 … cota … este 0,5%", valabil din 01.01.2026) — de aici 1% în
loc de 0,5%. La fel Q-CTB-08. *De decis:* când întrebarea numește mai mulți ani, data de referință e
cea a perioadei *despre care se întreabă* („pentru 2026", „datorează"), nu cea mai veche.

**C28 — Comparatorul (numai scor, nu motor) (N6).** Q-TVA-08 (10.500 lei, corect) și Q-PRF-05
(2.020 lei, corect) sunt GREȘIT pentru articol: cheia „art. 51 alin. (1) (mod. OUG 89/2025)" e citită
ca articol al OUG-ului, iar „; art. 298 alin. (1)-(3)" pierde actul. Q-SAL-06 (1.031,25 lei, corect)
e GREȘIT fiindcă primul fapt al cheii ales e „25%". Q-CPF-03 (1.008 / 4.032 / 1.008 lei, corecte) e
GREȘIT fiindcă „252 zile" e calculat în formulă, dar valoarea intermediară `zile(...)` nu e afișată
(defect de prezentare al calculului, N5; tot N5: un an calculat, 2027, e afișat „2.027", Q-PRF-03). *De decis:* comparatorul se repară înainte de setul nou
(altfel scorul final e subestimat), iar calculul afișează fiecare sub-expresie.

**C29 — Costul navigării.** $7,86 pentru 50 de întrebări ($0,157 / întrebare), de 2,4× costul v3
($3,25); 9 întrebări s-au oprit la limita de 12 pași. *De decis:* limita rămâne 12, sau crește
(mai puține abțineri de regăsire, cost mai mare)?
