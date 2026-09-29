## 0. CERINȚE — decizii de arhitect

### Aplicate în acest pas

| | Decizia | Cum e aplicată | Dovada |
|---|---|---|---|
| **C23** | `raspuns` obligatoriu și validat structural (nu gol, nu „x"/„-", nu conținutul altor câmpuri); la eșec o singură reîncercare, apoi abținere cu motivul scris | `navigare.valideaza_structura`: substituent/gol, marcaj de parametri scurs în orice câmp, `raspuns` care repetă alt câmp; reîncercarea primește problemele scrise; a doua = NU POT cu `tip_abtinere: C23` | `test_navigare.test_C23_*` (5), inclusiv forma exactă din v4 |
| **C24** | „răspuns gol" verificat întotdeauna; repararea unei găuri în verificator, cu dovadă în ambele direcții | `semantic.verifica`: verificarea iese din ramura C17 (b); gol = mai puțin de 2 caractere-cuvânt | `test_semantic.test_C24_*` (4): se resping „", „x", „-", „." cu și fără derogări; „Nu." și „21%" trec; abținerea nu e „gol" |
| **C25** | fiecare operand: FAPT_CAZ (din întrebare, literal) sau VALOARE_LEGALĂ (din atom) | câmpul `eticheta` în schema calculului; euristica C13 pe operanzi a fost înlocuită de etichetă | `test_navigare.test_C25_*` (3), inclusiv „valoare fiscală 100.000 lei" (Q-CTB-03 din v4) |
| **C26** | anexele, structură proprie (anexă → punct/secțiune), id-uri proprii; temeiul „anexa, pct. 238" | `atomizare.py`: nivelul `anexa`; punctul de anexă (forma portalului „238." / „- (1) …"); anexele „la norme" sub norme; titlul normelor în temei; lista anexelor și anexa citată într-un punct de intervenție nu deschid anexe; un articol care continuă numerotarea actului închide anexa | `test_c12_c17.test_C26_*` (4); `propuneri/v6/` |
| **C27** | data de referință pentru faptul întrebat, declarată în răspuns; mai multe date fără legătură clară → INCOMPLET | `navigare.date_din_intrebare` (toate datele, nu prima); modelul alege una și o motivează (`data_referinta`, `data_referinta_motiv`); verificatorul cere ca ea să fie una dintre datele întrebării și citatele să fie în vigoare la ea; data e scrisă la finalul răspunsului | `test_navigare.test_C27_*` (3) |
| **C28** | comparatorul reparat ca defect de clasă, scor înainte/după; calculul afișat pas cu pas | `comparatie.py`: sume ca numere, fapt negat, paranteza de proveniență, actul bucății anterioare; `navigare.pas_cu_pas` | `test_intrebari.test_C28_*` (4), `test_navigare.test_C28_*` (2); tabelul „înainte/după" |
| **C29** | 20 de pași; la limită abținere cu traseul | `MAX_PASI = 20`; fiecare rezultat de unealtă spune câți pași au rămas; o cerere peste limită = NU POT cu traseul în motiv | `test_navigare.test_C29_*`; secțiunea C29 |

### De decis (găsite la citirea celor 3 GREȘIT; nereparate — pasul se oprește după rulare)

**C30 — Comparatorul: zero spus în cuvinte și data în litere față de data numerică.** Q-CPF-09
(„Nu datorează nimic", temeiul exact al cheii) e notat GREȘIT pentru că faptul cheii e „0 lei". La
Q-TVA-07, „28 februarie 2026" nu se potrivește cu „28.02.2026" din cheie (comparatorul le reține în
forme diferite: zi + lună, respectiv data numerică). Ambele sunt defecte de clasă ale **scorului**, nu
ale motorului. *De decis:* se repară înainte de setul nou (ca C28, cu scorul înainte/după), sau
notarea rămâne strictă și cazurile se rejudecă de om?

**C31 — Codul muncii din instantaneu are structura stricată.** Textul art. 122 („compensare prin
ore libere plătite în următoarele 90 de zile") e atomizat sub `legea_53_2003_codul_muncii#art281/alin7~6`:
instantaneul iConta al Codului muncii include lanțuri de modificări care rup ierarhia. Faptul e corect,
temeiul e greșit (Q-SAL-10). *De decis:* Codul muncii se aduce consolidat din legislatie.just.ro, în
stratul oficial (ca C12), sau se repară atomizarea instantaneului?

**C32 — Termenul care cade în zi nelucrătoare.** Q-TVA-07 dă termenul nominal (28.02.2026, sâmbătă),
nu pe cel efectiv (02.03.2026). Regula e în lege (CPF art. 75 → Codul de procedură civilă), dar
aplicarea ei cere un calendar: ce zi a săptămânii e o dată și care sunt sărbătorile legale. Modelul
nu calculează (decizia 7), iar calculul nu are azi o funcție pentru asta. *De decis:* se adaugă în
calcul o funcție `termen_efectiv(data)` (sâmbătă/duminică + sărbătorile legale, cu lista sărbătorilor
luată dintr-un atom — Codul muncii art. 139), sau termenul efectiv rămâne în afara motorului?

**C33 — Reemiterea după C23 scrie diacriticele ca `ă`.** Toate cele 10 reîncercări C23 au fost
scurgeri reale de marcaj (niciuna falsă). Dar la reemitere, în 3 cazuri (Q-TVA-09, Q-CPF-08, Q-CTB-04),
modelul a scris diacriticele ca secvențe literale (`imobilizărilor`), iar verificatorul a respins,
corect, citatele: ca șir, nu sunt verbatim. Măsurat EXACT, fără niciun apel (`fiscalos/masoara_C33.py`:
navigarea reluată determinist din pașii salvați, aceleași propuneri cu secvențele decodate, aceeași
verificare): Q-TVA-09 și Q-CTB-04 ar trece și ar fi CORECT, Q-CPF-08 rămâne respins (C13). Scor:
**34/3/13 → 36/3/11**. *De decis:* decodarea secvențelor `\uXXXX` din intrarea uneltei (transformare
deterministă, fără schimbare de conținut) se aplică înainte de verificare, sau C23 tratează o
asemenea secvență ca defect de structură și cere reemiterea încă o dată?
