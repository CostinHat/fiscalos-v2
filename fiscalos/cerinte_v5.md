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
