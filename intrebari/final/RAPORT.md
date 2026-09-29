# FiscalOS v2 — Măsurătoarea finală, setul 2

Generat 29.09.2026 12:50 · ZIP: `/home/costin/ghid_incoming/fiscalos_masuratoare_finala.zip`

Versiunea motorului: **485ffc3**, neschimbată (după, s-au schimbat numai probele). Răspunsurile au fost comise (**8b3269f**) înainte de orice citire a cheii. Comparatorul, neschimbat. Nicio reparație după comparație.

## Cifra principală: greșelile de fond

**2** din 50 (din 35 răspunsuri date). Fiecare, citită (lectura mea, de verificat de om):

- **Q2-TVA-05** (PROCEDURA) — *temei greșit (regula alăturată, cu același text)*. Concluzia practică e cea din cheie (autofactură, până în a 15-a zi a lunii următoare celei în care a intervenit reducerea), dar temeiul citat e CF art. 320 alin. (3) — regula pentru beneficiarul OBLIGAT LA PLATA TAXEI (taxare inversă, art. 307 alin. (2)-(4), art. 331), care ajustează și baza de impozitare. Pentru un client care și-a dedus TVA, regula e art. 319 alin. (3) (ajustarea taxei deductibile), exact cum spune cheia. Nici data concretă (15.06.2026) nu e calculată.
- **Q2-CTB-05** (PROCEDURA) — *termenul efectiv necalculat*. Întrebarea cere o dată; răspunsul dă regula (31 mai, cu prelungire dacă e zi nelucrătoare), nu data: 02.06.2026 (31.05.2026 duminică, 01.06.2026 sărbătoare legală — 1 iunie și a doua zi de Rusalii). `termen_efectiv` exista și ar fi dat exact această dată, dar modelul nu l-a folosit: navigarea s-a oprit la Legea 82/1991 art. 36, fără regula prelungirii (CPC art. 181) și fără lista sărbătorilor (Codul muncii art. 139).

## Scorul pe fond (cifra finală)

| | CORECT | GREȘIT | NU POT |
|---|---|---|---|
| **Setul 2 (nou), comparator neschimbat** | **28** | **7** | **15** |

Cele 7 GREȘIT ale comparatorului, citite pe fond: 2 greșeli de fond; 2 corecte pe fond, notate GREȘIT de comparator (C42: Q2-TVA-09, Q2-PRF-05); 3 corecte la întrebarea pusă, fără faptul pe care cheia îl pune primul (C43: Q2-CPF-08, Q2-CTB-03, Q2-CTB-09). Scorul **nu** a fost ajustat pe baza lecturii.

Pe tipuri:

| Tip | CORECT | GREȘIT | NU POT |
|---|---|---|---|
| PARAMETRU | 10 | 0 | 0 |
| REGULA | 9 | 1 | 0 |
| CALCUL | 3 | 0 | 7 |
| CAPCANA | 4 | 3 | 3 |
| PROCEDURA | 2 | 3 | 0 |
| INCOMPLETA | 0 | 0 | 5 |

**INCOMPLETA** (C1: orice abținere e NU POT în scorul pe fond; se raportează separat): Q2-TVA-10 — incompletitudine detectată; Q2-PRF-10 — respins de verificare; Q2-SAL-10 — incompletitudine detectată; Q2-CPF-10 — respins de verificare; Q2-CTB-10 — incompletitudine detectată.

**Abțineri (NU POT), pe cauze:**

- Q2-TVA-06 (CALCUL): VERIFICAREA MECANICA a respins propunerea modelului: cifra '1.01.2019' din raspuns nu apare literal in citate sau in intrebare
- Q2-TVA-07 (CALCUL): VERIFICAREA MECANICA a respins propunerea modelului: valoarea legala '2026' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare)
- Q2-TVA-08 (CAPCANA): C23: structura răspunsului final a fost invalidă de două ori (marcaj de parametri scurs in raspunde.declaratie; campul raspuns e gol sau un substituent ('-') / marcaj de parametri scurs in raspunde.declaratie; campul ras…
- Q2-PRF-06 (CALCUL): VERIFICAREA CALCULULUI a respins propunerea: operandul cincime='5' nu apare literal in fragmentul lui
- Q2-PRF-08 (CAPCANA): VERIFICAREA MECANICA a respins propunerea modelului: citatul NU e verbatim in atomul cod_fiscal_227_2015_consolidat#art43/alin4/lita; valoarea legala '5' nu apare in niciun citat (C13: o valoare legala se dovedeste din a…
- Q2-SAL-07 (CALCUL): VERIFICAREA CALCULULUI a respins propunerea: calculul total_impozabil: constanta fara sursa in formula: 0 (permise numai 1 si 100)
- Q2-CPF-06 (CALCUL): VERIFICAREA MECANICA a respins propunerea modelului: cifra '1.000.000' din raspuns nu apare literal in citate sau in intrebare
- Q2-CTB-06 (CALCUL): VERIFICAREA MECANICA a respins propunerea modelului: cifra '150' din raspuns nu apare literal in citate sau in intrebare
- Q2-CTB-07 (CALCUL): VERIFICAREA CALCULULUI a respins propunerea: operandul parte_capital='5' nu apare literal in fragmentul lui
- Q2-CTB-08 (CAPCANA): VERIFICAREA MECANICA a respins propunerea modelului: valoarea legala '10' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare)

## Chei care par greșite

Niciuna. Cheile celor 7 GREȘIT au fost confruntate cu atomii: Q2-TVA-05 (CF art. 319 alin. (3) — confirmat de atom), Q2-CTB-05 (31.05.2026 duminică, 01.06.2026 = 1 iunie și a doua zi de Rusalii — confirmat de calendarul C32/C38), celelalte pe temeiul pe care îl citează și răspunsul.

## Setul 1, pentru comparație

Scorul setului 1 cu **aceeași** versiune (485ffc3) nu se poate obține fără o rulare plătită: ieșirile salvate ale setului 1 sunt produse de versiunea v5 (778e826), iar între timp s-au schimbat corpusul (C31, C36 — 48 de acte oficiale, conversia) și calculul (C32, C38). Cel mai apropiat scor din ieșirile salvate, fără apel: **37/2/11** (v5 + decodarea C33 + comparatorul C30, fiecare pe corpusul rulării).

| | CORECT | GREȘIT | NU POT |
|---|---|---|---|
| Setul 1 (expus), v5 + C33 + C30, din ieșirile salvate | 37 | 2 | 11 |
| **Setul 2 (nou), 485ffc3** | **28** | **7** | **15** |

---

## 0. CERINȚE — decizii de arhitect

### Aplicate înainte de măsurătoare

| | Decizia | Cum e aplicată |
|---|---|---|
| **C38** | datele Adormirii (15.08) și ale Crăciunului (25–26.12): dată de calendar liturgic fix, declarată („dată de calendar, nescrisă în lege”), art. 139 citat; `termen_efectiv` reactivat | `navigare.Calendar.sarbatori`; probe: Q-TVA-07 → 02.03.2026, 15.08.2025 → 18.08.2025, 25.12.2026 → 28.12.2026 |
| **C39** | „Reproducem mai jos” numai în stratul oficial | neschimbat (confirmat) |
| **Regulile măsurătorii** | orbire (id, tip, intrebare), versiunea 485ffc3 neschimbată, răspunsuri comise înainte de comparație, comparator neschimbat, nicio reparație după comparație | proba `test_setul_2_se_incarca_orb`; commit-ul răspunsurilor `8b3269f` înaintea oricărei citiri a cheii; `git diff 485ffc3` pe `fiscalos/` = numai probe |

### Defecte găsite de măsurătoare — raportate ca cerințe, NEREPARATE (setul 2 nu se folosește pentru reglaje)

**C40 — Termenul efectiv nu e cerut modelului (clasa: calcul disponibil, nefolosit).** Q2-CTB-05: întrebarea
cere o dată, iar răspunsul dă regula, nu data. `termen_efectiv` exista și ar fi dat 02.06.2026, dar
promptul nu cere ca, la o întrebare „până la ce dată”, termenul nominal să treacă prin el. *Cerință:* orice
răspuns care dă un termen calendaristic îl calculează cu `termen_efectiv`; altfel răspunsul e INCOMPLET.

**C41 — Temeiul alăturat, cu text aproape identic (clasa: selecția temeiului).** Q2-TVA-05: CF art. 320
alin. (3) (beneficiarul obligat la plata taxei, taxare inversă) citat în locul art. 319 alin. (3)
(ajustarea taxei deductibile) — aceeași frază despre autofactură și „a 15-a zi a lunii următoare”, alt
subiect. Verificatorul nu poate prinde asta (citatul e verbatim, cifrele sunt literale). *Cerință:* la
două atomi cu text aproape identic, modelul vede subiectul fiecăruia (condiția din fraza introductivă) și
motivează alegerea.

**C42 — Comparatorul: zero și data cu an relativ (clasa: scor, nu motor).** Q2-TVA-09 („nu restituie”, „nu
implică ajustări” = 0 lei) și Q2-PRF-05 („25 iunie … a anului următor” = 25.06.2027) sunt corecte pe fond
și notate GREȘIT. *Cerință:* extinderea C30 — formulări de zero și data zi+lună cu an relativ față de o
cheie numerică. Scorul NU a fost schimbat pe baza lor.

**C43 — Faptul principal al cheii e un fapt secundar al întrebării (clasa: completitudine).** Q2-CPF-08
(cauțiunea de 4.500 lei), Q2-CTB-03 (pragul de 16.000.000 lei), Q2-CTB-09 (amenda de 2.000 lei): răspunsul
corect la întrebarea pusă („Are dreptate?”, „Este obligată?”, „Este legală?”), fără cifra pe care cheia o
pune pe primul loc. *De decis:* răspunsul trebuie să adauge consecința cuantificată (cauțiune, amendă,
prag), sau cheia se notează pe concluzie?

**C44 — Reîncercarea C23 degradează transportul (clasa: C23/C33).** 7 reîncercări C23 pe setul 2; după ele,
Q2-CPF-10 a scris diacriticele ca `"` („ceilal"i contribuabili/pl"titori”) — ireversibil, deci nedecodabil
ca la C33 — și a fost respinsă; Q2-TVA-08 s-a abținut după a doua structură invalidă. *Cerință:* răspunsul
final pe ieșire structurată (`output_config.format`) într-o tură finală fără unelte, în locul uneltei
`raspunde` (varianta din C23 neadoptată atunci).

**C45 — Respingeri ale calculului pe forma operandului (clasa: C25).** Q2-PRF-06 și Q2-CTB-07: operandul
„5” (o cincime, 5 ani) nu apare literal în fragmentul lui (textul spune „5 ani” sau „cincime”); Q2-SAL-07:
constanta 0 în formulă. Direcția e sigură (abținere), dar 3 întrebări CALCUL au pierdut răspunsul. *De
decis:* numerele scrise în litere în atom („cinci”, „o cincime”) ca operanzi, cu forma lor literală?

**C46 — Cifre derivate în textul răspunsului (clasa: C13/verificator).** Q2-TVA-06 („1.01.2019”),
Q2-CPF-06 („1.000.000”), Q2-CTB-06 („150”): o cifră calculată sau reformulată de model direct în text, nu
prin `calcule`, e respinsă corect. *Cerință:* promptul cere ca orice cifră care nu e citată literal să vină
dintr-un calcul.

---

## Operațiile, cu durata și costul măsurate

| Operație | Durată | Cost |
|---|---|---|
| Setul 2: 50 de întrebări, 289 ture la `claude-opus-5` ({'intrare': 578, 'iesire': 183393, 'cache_scriere': 407525, 'cache_citire': 3255123} tokeni) | 2780.1 s | $8.7623 |
| Apeluri de control al creditului (2 × 8+5 tokeni) | — | ~$0.0004 |
| Prima pornire, oprită: fișierul setului 2 lipsea (niciun apel) | — | $0 |
| Comparația, lectura, raportul | 0.0 s | $0 |

Pași de navigare: 6.9 în medie; la limita de 20: 0; reîncercări C23: 7 (Q2-TVA-08, Q2-PRF-06, Q2-PRF-08, Q2-PRF-10, Q2-CPF-10, Q2-CTB-03, Q2-CTB-05); model de rezervă: niciodată.

## Cele 50 de întrebări

| Id | Tip | Pe fond | Lectura | Răspunsul |
|---|---|---|---|---|
| Q2-TVA-01 | PARAMETRU | CORECT |  | Pragul este de 10.000 euro pe an calendaristic, echivalent în lei 46.337 lei. Câ… |
| Q2-TVA-02 | PARAMETRU | CORECT |  | Poate emite factură simplificată atunci când valoarea facturii nu este mai mare … |
| Q2-TVA-03 | REGULA | CORECT |  | Nu. Locul prestării serviciilor de consultanță către o persoană impozabilă care … |
| Q2-TVA-04 | REGULA | CORECT |  | TVA aferentă avansului devine exigibilă la data încasării avansului, adică la 18… |
| Q2-TVA-05 | PROCEDURA | GREȘIT | fond | Clientul trebuie să ajusteze (în sensul reducerii) TVA dedusă inițial pentru ach… |
| Q2-TVA-06 | CALCUL | NU POT |  | *VERIFICAREA MECANICA a respins propunerea modelului: cifra '1.01.2019'…* |
| Q2-TVA-07 | CALCUL | NU POT |  | *VERIFICAREA MECANICA a respins propunerea modelului: valoarea legala '…* |
| Q2-TVA-08 | CAPCANA | NU POT |  | *C23: structura răspunsului final a fost invalidă de două ori (marcaj d…* |
| Q2-TVA-09 | CAPCANA | GREȘIT | comparator, nu fond | Nu. Casarea utilajului — scoaterea din funcțiune urmată de dezmembrare — nu impl… |
| Q2-TVA-10 | INCOMPLETA | NU POT |  | *INCOMPLET: intrebarea nu da faptele de care depinde raspunsul: Calitat…* |
| Q2-PRF-01 | PARAMETRU | CORECT |  | Costurile excedentare ale îndatorării sunt deductibile, într-o perioadă fiscală,… |
| Q2-PRF-02 | PARAMETRU | CORECT |  | Sunt cheltuieli sociale cu deductibilitate limitată: se deduc în limita unei cot… |
| Q2-PRF-03 | REGULA | CORECT |  | Cheltuielile de exploatare (combustibil, reparații, asigurare) sunt deductibile … |
| Q2-PRF-04 | REGULA | CORECT |  | Nu. Rezerva fiscală constituită din profitul scutit aferent anului fiscal 2026 n… |
| Q2-PRF-05 | PROCEDURA | GREȘIT | comparator, nu fond | Poate dispune redirecționarea impozitului pe profit, în limita sumei neutilizate… |
| Q2-PRF-06 | CALCUL | NU POT |  | *VERIFICAREA CALCULULUI a respins propunerea: operandul cincime='5' nu …* |
| Q2-PRF-07 | CALCUL | CORECT |  | Impozitul pe profit datorat pentru 2026 este 40.000 lei: impozit pe profit brut … |
| Q2-PRF-08 | CAPCANA | NU POT |  | *VERIFICAREA MECANICA a respins propunerea modelului: citatul NU e verb…* |
| Q2-PRF-09 | CAPCANA | CORECT |  | Nu. Sponsorizarea nu se mai scade din impozitul pe veniturile microîntreprinderi… |
| Q2-PRF-10 | INCOMPLETA | NU POT |  | *VERIFICAREA MECANICA a respins propunerea modelului: citat prea scurt …* |
| Q2-SAL-01 | PARAMETRU | CORECT |  | Termenul de preaviz la demisie este cel convenit în contractul individual de mun… |
| Q2-SAL-02 | PARAMETRU | CORECT |  | Baza anuală de calcul a CASS pentru veniturile din activități independente reali… |
| Q2-SAL-03 | REGULA | CORECT |  | Perioada de probă poate fi de cel mult 120 de zile calendaristice, fiind vorba d… |
| Q2-SAL-04 | REGULA | CORECT |  | Munca prestată se compensează, în primul rând, cu timp liber corespunzător acord… |
| Q2-SAL-05 | PROCEDURA | CORECT |  | Datele contractului (identificare angajator/salariat, funcție, tip și durată con… |
| Q2-SAL-06 | CALCUL | CORECT |  | Neimpozabilă este suma de 1.485 lei (plafonul cel mai mic dintre limita de 1.500… |
| Q2-SAL-07 | CALCUL | NU POT |  | *VERIFICAREA CALCULULUI a respins propunerea: calculul total_impozabil:…* |
| Q2-SAL-08 | CAPCANA | CORECT |  | Nu. Cât timp contractul individual de muncă continuă, zilele de concediu de odih… |
| Q2-SAL-09 | CAPCANA | CORECT |  | Nu. Salariul de bază minim brut pe țară garantat în plată poate fi acordat unui … |
| Q2-SAL-10 | INCOMPLETA | NU POT |  | *INCOMPLET: intrebarea nu da faptele de care depinde raspunsul: Gradul …* |
| Q2-CPF-01 | PARAMETRU | CORECT |  | Creanțele fiscale restante administrate de ANAF, aflate în sold la 31 decembrie,… |
| Q2-CPF-02 | PARAMETRU | CORECT |  | Termenul de prescripție al dreptului organului de executare silită de a cere exe… |
| Q2-CPF-03 | REGULA | CORECT |  | Nu. Declarația rectificativă D101 pentru 2024, depusă în timpul inspecției fisca… |
| Q2-CPF-04 | REGULA | CORECT |  | Nu. Fiind o diferență de impozit pe venit de restituit mai mică de 10 lei, suma … |
| Q2-CPF-05 | PROCEDURA | CORECT |  | Suma plătită în plus se recuperează prin cerere de restituire depusă la organul … |
| Q2-CPF-06 | CALCUL | NU POT |  | *VERIFICAREA MECANICA a respins propunerea modelului: cifra '1.000.000'…* |
| Q2-CPF-07 | CALCUL | CORECT |  | Firma primește efectiv în cont 8.800 lei: restituirea se face numai după compens… |
| Q2-CPF-08 | CAPCANA | GREȘIT | incomplet față de cheie, nu greșit | Nu, administratorul nu are dreptate. Simpla depunere a contestației pe calea adm… |
| Q2-CPF-09 | CAPCANA | CORECT |  | Nu, contabilul nu are dreptate. Termenul de prescripție de 5 ani nu curge de la … |
| Q2-CPF-10 | INCOMPLETA | NU POT |  | *VERIFICAREA MECANICA a respins propunerea modelului: citatul NU e verb…* |
| Q2-CTB-01 | PARAMETRU | CORECT |  | Plafonul este de 50.000 lei numerar în casierie la sfârșitul fiecărei zile, iar … |
| Q2-CTB-02 | PARAMETRU | CORECT |  | Sunt microentități entitățile care, la data bilanțului, nu depășesc limitele a c… |
| Q2-CTB-03 | REGULA | GREȘIT | incomplet față de cheie, nu greșit | Da. Societatea a depășit, la data bilanțului, limitele a două dintre cele trei c… |
| Q2-CTB-04 | REGULA | CORECT |  | Nu. Societatea care a distribuit trimestrial dividende nu poate acorda împrumutu… |
| Q2-CTB-05 | PROCEDURA | GREȘIT | fond | Situațiile financiare anuale se depun la organul fiscal competent din subordinea… |
| Q2-CTB-06 | CALCUL | NU POT |  | *VERIFICAREA MECANICA a respins propunerea modelului: cifra '150' din r…* |
| Q2-CTB-07 | CALCUL | NU POT |  | *VERIFICAREA CALCULULUI a respins propunerea: operandul parte_capital='…* |
| Q2-CTB-08 | CAPCANA | NU POT |  | *VERIFICAREA MECANICA a respins propunerea modelului: valoarea legala '…* |
| Q2-CTB-09 | CAPCANA | GREȘIT | incomplet față de cheie, nu greșit | Nu. Primirea unui împrumut de la o persoană fizică nu poate fi făcută în numerar… |
| Q2-CTB-10 | INCOMPLETA | NU POT |  | *INCOMPLET: intrebarea nu da faptele de care depinde raspunsul: Natura …* |
