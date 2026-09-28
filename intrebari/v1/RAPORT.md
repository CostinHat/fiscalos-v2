# FiscalOS v2 — Motorul de întrebări: 50 de întrebări, răspunsuri din atomi

Generat 28.09.2026 17:22. Data la care se pun întrebările: **2026-09-28**. ZIP: `/home/costin/ghid_incoming/fiscalos_intrebari_rezultat.zip`.

## Scorul

| | |
|---|---|
| **CORECT** | **8** |
| **GREȘIT** | **17** |
| **NU POT RĂSPUNDE** | **25** |

**Citit corect, cele 8 CORECT sunt două lucruri diferite:**

- **4 răspunsuri corecte pe fond** — faptul cerut și articolul corect: Q-PRF-01, Q-PRF-02, Q-SAL-01, Q-CTB-01.
- **4 abțineri pe întrebări INCOMPLETA** — Q-TVA-10, Q-PRF-10, Q-SAL-09, Q-CPF-10. Regula de notare (fixată înainte de comparație) creditează o abținere pe INCOMPLETA dacă și cheia spune că lipsesc date. Dar **motorul nu detectează incompletitudinea**: s-a abținut din alt motiv (forma faptului nerecunoscută, sau judecată Da/Nu). Corecte după regulă, nu după merit. Vezi C1.

Pe fond, deci: **4 din 50**. Motorul e un extractor lexical care știe să se abțină: din 50, a dat 21 răspunsuri, iar 17 dintre ele sunt greșite.

---

## 0. CERINȚE — decizii de arhitect

**C1 — Cum se numără abținerile pe INCOMPLETA.** Toate cele 4 întrebări INCOMPLETA ies
CORECT, fiindcă motorul s-a abținut și cheia spune că lipsesc date. Dar motorul **nu detectează
incompletitudinea** — s-a abținut fiindcă nu recunoaște forma faptului cerut, sau fiindcă întrebarea
cere o judecată. Regula de notare a fost fixată înainte de comparație, deci n-am schimbat-o după.
*De decis:* scorul de referință e cel după regulă (CORECT include abținerile), sau cel pe fond
(4)? Și: detectarea incompletitudinii intră în motor ca o capacitate de sine stătătoare?
Nu am folosit coloana `tip` ca s-o simulez — o întrebare etichetată INCOMPLETA spune singură ce se
așteaptă, iar folosirea etichetei ar fi fost citirea răspunsului.

**C2 — Notarea cere și faptul, și articolul.** Un răspuns corect în fond, citat de pe alt articol
decât cheia, iese GREȘIT. E sever intenționat: numai valoarea poate fi o coincidență (lecția bancului
de mutații), numai articolul poate fi un extras care nu răspunde. *De decis:* rămâne așa?

**C3 — Plafonul motorului.** Motorul e un extractor lexical (BM25 peste atomi, plus reguli de
structură, vigoare și ierarhie). Nu compune reguli, nu aplică o regulă la fapte, nu calculează decât
„o bază × o cotă". Clasa cea mai mare de greșeli rămase — articolul corect, fraza greșită — e
limita acestui fel de motor. Următorul pas e o decizie de arhitectură: (a) extragere semantică
**ancorată pe atomi** — un model care propune răspunsul, dar orice cifră și orice citat trebuie să
existe verbatim într-un atom, verificat mecanic, ca acum; (b) calculatoare pe clase de calcul
(contribuții salariale, accesorii, TVA dedus), cu parametrii luați din atomi; (c) motorul rămâne un
extractor care se abține des. Nu am început niciuna.

**C4 — Compromisuri ale regulilor de certitudine (D15).** Regula „o judecată Da/Nu nu se dă" a
costat un răspuns corect: Q-CTB-08, unde extrasul era exact regula (dividendele interimare din 2025
rămân la 10%). A convertit în schimb 10 răspunsuri greșite în abțineri. *De decis:* motorul are voie
să răspundă la o judecată atunci când extrasul conține literal răspunsul?

**C5 — Data întrebării.** O întrebare fără dată e datată la ziua rulării (**2026-09-28**); „în 2026"
înseamnă sfârșitul anului, dar nu după ziua întrebării; o lună înseamnă ultima ei zi. *De decis:*
convenția se păstrează? Alternativa e ca întrebările să-și poarte data explicit.

**C6 — Expunere declarată.** La inspectarea structurii CSV-ului, înainte de instrucțiunea de
orbire, am văzut răspunsurile așteptate pentru Q-TVA-01…04. Motorul nu conține nicio regulă pentru
ele; dintre cele patru, niciuna nu iese CORECT pe fond.

**C7 — Două defecte ale comparatorului, reparate după prima comparație.** Ambele l-au făcut mai
strict: un temei de cheie necitibil trecea drept „îndeplinit" (3 CORECT false), iar articolele
romane nu se citeau. Scorul v0 pe aceleași răspunsuri comise: 5/31/14 cu notarea inițială, 3/33/14
cu cea reparată. *De ratificat.*

---

## 1. Operațiile rulate, cu durata măsurată

| Operație | Durată |
|---|---|
| Index BM25 peste atomii din acte normative (31485 atomi) | 11.31 s |
| Raspuns la cele 50 intrebari | 3.12 s |
| Comparatia cu cheia | 3.50 s |
| Scrierea celor 50 fisiere per intrebare | 0.01 s |
| **Total rularea finală** | **17.94 s** |

Fiecare reparație de clasă a rulat din nou toate cele 50 de întrebări și comparația; timpul motorului pe fiecare e în tabelul din §3.

## 2. Protocolul — de ce scorul e o măsurătoare, nu o ajustare

1. Regulile de clasă ale motorului (R-DATA, R-SURSA, R-VERS, R-VALAB, R-PRAG, R-CALC) au fost scrise
   înainte de prima rulare pe întrebări.
2. Motorul e **orb la cheie, mecanic**: citește numai coloanele `id`, `tip`, `intrebare`; numele
   coloanelor cu răspunsul așteptat nu apar în modul (verificat prin AST în `test_intrebari.py`).
3. Răspunsurile v0 au fost **comise înainte ca modulul de comparație să existe**: commit `f1997a8`,
   `artefacte/intrebari/raspunsuri_v0.json`, sha256 `c9af0408…6f9`.
4. Regulile de notare au fost comise **înainte ca comparatorul să citească cheia**.
5. După prima comparație, fiecare reparație a fost o **clasă de defect**, re-rulată pe toate cele
   50 de întrebări; istoricul e în `artefacte/intrebari/istoric_scor.json` și în §3, inclusiv
   reparațiile care n-au schimbat scorul și una care l-a scăzut.
6. Niciun răspuns fără atom: verificat la rulare (`assert`) și în probe; fragmentul citat e verificat
   literal în textul atomului.

## 3. Istoricul scorului — fiecare reparație e o clasă, măsurată pe toate 50

| Pas | CORECT | GREȘIT | NU POT | Δ CORECT | Motor | Clasa de defect |
|---|---|---|---|---|---|---|
| v0 | 3 | 33 | 14 |  | 12.7 s | motorul v0, raspunsuri comise in f1997a8 inainte de comparator; notare dupa repararea comparatorului (da71623) |
| D4 | 4 | 32 | 14 | +1 | 12.8 s | R-VERS: redarile istorice penalizate prin nume, nu prin gasirea perechii curente |
| D3 | 4 | 32 | 14 | +0 | 13.2 s | instructiunile de modificare (articol roman -> punct) nu sunt legea in vigoare |
| D3b | 5 | 31 | 14 | +1 | 13.5 s | text citat (articol arab) in redarea unui act modificator = instantaneu, nu lege in vigoare |
| D9 | 4 | 32 | 14 | -1 | 13.5 s | abrevierile fiscale (TVA, CAS, CAM, D300...) extinse la forma lunga a actelor |
| D9a | 5 | 31 | 14 | +1 | 13.6 s | abrevieri de CONCEPTE (TVA, CAS, CAM...) extinse; codurile de formular nu |
| D7 | 5 | 30 | 15 | +0 | 14.0 s | ordinele de formular (instructiuni de completare) cedeaza la intrebarile de fond care nu numesc un formular |
| D12 | 5 | 30 | 15 | +0 | 14.2 s | precizia datei: luna -> ultima zi, an -> sfarsitul anului dar nu dupa data intrebarii |
| D13 | 6 | 30 | 14 | +1 | 14.3 s | valoarea cautata si in copiii (litere/puncte) atomului gasit, cu aceleasi filtre de vigoare |
| D10 | 7 | 29 | 14 | +1 | 14.6 s | denumirea marginala a articolului (titlul) ca context pentru alineatele lui |
| D1 | 7 | 29 | 14 | +0 | 14.7 s | valoarea aleasa din atomul al carui text propriu potriveste cel mai bine cuvintele rare (extinse) ale intrebarii |
| D14 | 7 | 29 | 14 | +0 | 13.8 s | ierarhia actelor normative la alegerea intre candidati: legea prevaleaza asupra normei de aplicare |
| D5 | 5 | 36 | 9 | -2 | 10.9 s | intrebarea fara data e datata la ziua in care e pusa (inlocuieste R-DATA) |
| D15 | 5 | 26 | 19 | +0 | 10.9 s | certitudine: judecata Da/Nu -> abtinere cu material; faptul de forma cerută trebuie sa fie in raspuns |
| D15c | 8 | 17 | 25 | +3 | 11.6 s | drumul pur extractiv (forma faptului nerecunoscuta) -> abtinere cu material |

**Ce nu apare în cifre, dar contează:**

- **D9 a regresat (5 → 4)** și e păstrat în istoric. Extinderea codurilor de formular („D100" →
  „declarație privind obligațiile de plată…") trăgea întrebările de fond spre atomii formularului.
  D9a păstrează numai abrevierile de concepte (TVA, CAS, CAM).
- **D3, D7, D12, D1, D14 n-au schimbat scorul** și sunt păstrate: fiecare a mutat răspunsuri pe atomi
  mai buni, sau a fost condiția pentru altă reparație (D12 a făcut eligibil atomul pe care D13 l-a
  găsit apoi).
- **D11 a fost o ipoteză infirmată de măsurătoare**: presupunerea că Codul fiscal consolidat e depășit
  era falsă — are note până la 01.07.2026. Defectul real era D12.
- **D5 a scăzut scorul (7 → 5) și e corect să-l scadă**: cele două „victorii" pe care le pierde erau
  refuzuri pentru lipsa datei pe întrebări care nu aveau nevoie de dată.
- **Două defecte în propriile mele reparații**, prinse înainte de măsurătoarea următoare: D13 ocolea
  regula de vigoare la coborârea în copii; D1 folosea cuvintele neextinse ale întrebării.

## 4. Cele 50 de întrebări

Fiecare are fișierul ei în `intrebari/v1/raspunsuri/<id>.md`: răspunsul, atomul, fragmentul verbatim, valabilitatea la data întrebării, și comparația cu cheia.

| Id | Tip | Verdict | Răspunsul motorului | Atomul |
|---|---|---|---|---|
| Q-TVA-01 | PARAMETRU | GREȘIT | 9% | `cod_fiscal_227_2015_consolidat#art291/alin3^5/litd` |
| Q-TVA-02 | PARAMETRU | GREȘIT | 100.000 euro | `cod_fiscal_227_2015_consolidat#art310^1/alin1` |
| Q-TVA-03 | REGULA | GREȘIT | Dacă în luna august 2025 a fost depășit și plafonul de 395.0… | `cod_fiscal_227_2015_consolidat#art310/alin2` |
| Q-TVA-04 | REGULA | NU POT RĂSPUNDE | *nu pot — D15: intrebarea cere un fapt de forma 'suma',…* | — |
| Q-TVA-05 | CAPCANA | NU POT RĂSPUNDE | *nu pot — D15: intrebarea cere o JUDECATA (Da/Nu) - apl…* | — |
| Q-TVA-06 | CAPCANA | NU POT RĂSPUNDE | *nu pot — D15: intrebarea cere o JUDECATA (Da/Nu) - apl…* | — |
| Q-TVA-07 | PROCEDURA | GREȘIT | 316 , și nu se va înregistra în scopuri de TVA ca urmare a t… | `cod_fiscal_227_2015_consolidat#art324/alin8` |
| Q-TVA-08 | CALCUL | NU POT RĂSPUNDE | *nu pot — R-CALC: niciun atom din primii 5 nu da O SING…* | — |
| Q-TVA-09 | CALCUL | NU POT RĂSPUNDE | *nu pot — R-CALC: intrebarea are 2 baze monetare; calcu…* | — |
| Q-TVA-10 | INCOMPLETA | CORECT | *nu pot — D15: intrebarea cere un fapt a carui forma mo…* | — |
| Q-PRF-01 | PARAMETRU | CORECT | 1% | `cod_fiscal_227_2015_consolidat#art51/alin1` |
| Q-PRF-02 | REGULA | CORECT | Dacă în cursul unui an fiscal o microîntreprindere realizeaz… | `cod_fiscal_227_2015_consolidat#art52/alin1` |
| Q-PRF-03 | CAPCANA | GREȘIT | în cazul în care anul fiscal modificat începe în a doua, res… | `cod_fiscal_227_2015_consolidat#art41/alin15/litb` |
| Q-PRF-04 | CAPCANA | NU POT RĂSPUNDE | *nu pot — D15: intrebarea cere un fapt a carui forma mo…* | — |
| Q-PRF-05 | CALCUL | NU POT RĂSPUNDE | *nu pot — R-CALC: intrebarea are 4 baze monetare; calcu…* | — |
| Q-PRF-06 | CALCUL | NU POT RĂSPUNDE | *nu pot — R-CALC: intrebarea are 2 baze monetare; calcu…* | — |
| Q-PRF-07 | CALCUL | NU POT RĂSPUNDE | *nu pot — R-CALC: intrebarea are 3 baze monetare; calcu…* | — |
| Q-PRF-08 | REGULA | NU POT RĂSPUNDE | *nu pot — D15: intrebarea cere un fapt a carui forma mo…* | — |
| Q-PRF-09 | PROCEDURA | GREȘIT | Contribuabilii care aplică sistemul de declarare și plată a … | `cod_fiscal_227_2015_consolidat#art41/alin8` |
| Q-PRF-10 | INCOMPLETA | CORECT | *nu pot — D15: intrebarea cere o JUDECATA (Da/Nu) - apl…* | — |
| Q-SAL-01 | PARAMETRU | CORECT | 2,25% | `cod_fiscal_227_2015_consolidat#art220^3/alin1` |
| Q-SAL-02 | PROCEDURA | GREȘIT | d)-f) , precum și persoanele fizice care realizează în Român… | `cod_fiscal_227_2015_consolidat#art147~2/alin1` |
| Q-SAL-03 | CALCUL | NU POT RĂSPUNDE | *nu pot — R-CALC: niciun atom din primii 5 nu da O SING…* | — |
| Q-SAL-04 | CALCUL | NU POT RĂSPUNDE | *nu pot — R-CALC: intrebarea are 2 baze monetare; calcu…* | — |
| Q-SAL-05 | CAPCANA | NU POT RĂSPUNDE | *nu pot — D15: intrebarea cere o JUDECATA (Da/Nu) - apl…* | — |
| Q-SAL-06 | CAPCANA | NU POT RĂSPUNDE | *nu pot — D15: intrebarea cere un fapt a carui forma mo…* | — |
| Q-SAL-07 | REGULA | GREȘIT | Cuantumul brut lunar al indemnizației pentru incapacitate te… | `oug_158_2005_consolidat#art17/alin1` |
| Q-SAL-08 | CAPCANA | GREȘIT | Cuantumul brut lunar al indemnizației pentru incapacitate te… | `oug_158_2005_consolidat#art17/alin1` |
| Q-SAL-09 | INCOMPLETA | CORECT | *nu pot — D15: intrebarea cere un fapt a carui forma mo…* | — |
| Q-SAL-10 | REGULA | GREȘIT | Plata drepturilor pentru munca suplimentară prestată în cadr… | `legea_141_2025_consolidat#artXVIII/alin2` |
| Q-CPF-01 | PARAMETRU | GREȘIT | 1% | `legea_207_2015_consolidat#art183/alin2` |
| Q-CPF-02 | CALCUL | NU POT RĂSPUNDE | *nu pot — R-CALC: niciun atom din primii 5 nu da O SING…* | — |
| Q-CPF-03 | CALCUL | GREȘIT | 20.000 lei x 0,08% = 16,00 lei | `legea_207_2015_consolidat#art181/alin1` |
| Q-CPF-04 | REGULA | NU POT RĂSPUNDE | *nu pot — D15: intrebarea cere un fapt de forma 'termen…* | — |
| Q-CPF-05 | PARAMETRU | GREȘIT | 60 de zile | `legea_207_2015_consolidat#art281~2/alin3` |
| Q-CPF-06 | PROCEDURA | GREȘIT | soldul sumei negative de TVA solicitatâ la rambursare provin… | `legea_207_2015_consolidat#art168~2/alin3~2/lite` |
| Q-CPF-07 | REGULA | GREȘIT | Contribuabilul/Plătitorul are obligația de a declara organul… | `legea_207_2015_consolidat#art85~2/alin1` |
| Q-CPF-08 | CAPCANA | NU POT RĂSPUNDE | *nu pot — D15: intrebarea cere o JUDECATA (Da/Nu) - apl…* | — |
| Q-CPF-09 | CAPCANA | NU POT RĂSPUNDE | *nu pot — D15: intrebarea cere un fapt de forma 'procen…* | — |
| Q-CPF-10 | INCOMPLETA | CORECT | *nu pot — D15: intrebarea cere un fapt a carui forma mo…* | — |
| Q-CTB-01 | PARAMETRU | CORECT | 5.000 lei | `cod_fiscal_227_2015_consolidat#art28/alin2/litb` |
| Q-CTB-02 | CAPCANA | NU POT RĂSPUNDE | *nu pot — D15: intrebarea cere o JUDECATA (Da/Nu) - apl…* | — |
| Q-CTB-03 | CALCUL | GREȘIT | 100.000 lei x 65% = 65000,00 lei | `cod_fiscal_227_2015_consolidat#art28/alin8^1` |
| Q-CTB-04 | REGULA | NU POT RĂSPUNDE | *nu pot — D15: intrebarea cere un fapt a carui forma mo…* | — |
| Q-CTB-05 | PROCEDURA | NU POT RĂSPUNDE | *nu pot — D15: intrebarea cere un fapt a carui forma mo…* | — |
| Q-CTB-06 | CAPCANA | NU POT RĂSPUNDE | *nu pot — D15: intrebarea cere o JUDECATA (Da/Nu) - apl…* | — |
| Q-CTB-07 | CALCUL | GREȘIT | 50.000 lei x 16% = 8000,00 lei | `cod_fiscal_227_2015_consolidat#art43/alin2` |
| Q-CTB-08 | CAPCANA | NU POT RĂSPUNDE | *nu pot — D15: intrebarea cere o JUDECATA (Da/Nu) - apl…* | — |
| Q-CTB-09 | CALCUL | NU POT RĂSPUNDE | *nu pot — R-CALC: niciun atom din primii 5 nu da O SING…* | — |
| Q-CTB-10 | REGULA | NU POT RĂSPUNDE | *nu pot — D15: intrebarea cere un fapt a carui forma mo…* | — |

## 5. Unde greșește motorul — clasele rămase

- **Articolul corect, fraza sau numărul greșit (8):** Q-TVA-01, Q-TVA-03, Q-PRF-09, Q-SAL-02, Q-SAL-07, Q-SAL-08, Q-CPF-03, Q-CTB-03. Motorul găsește locul, nu propoziția: un extractor lexical nu știe care dintre alineatele unui articol răspunde la întrebare. Aceasta e clasa cea mai mare și e un plafon de capacitate, nu un defect de reglaj — vezi C3.
- **Faptul corect, articolul altul decât al cheii (1):** Q-SAL-10. Notarea cere ambele; un om poate rejudeca.
- **Restul (8):** articol și fapt greșite — căutarea lexicală a găsit un loc învecinat (ex. art. 310^1 în loc de art. 310; bugetele locale în loc de bugetul de stat).

