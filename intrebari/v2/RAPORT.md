# FiscalOS v2 — Motorul de întrebări v2: stratul semantic ancorat pe atomi

Generat 28.09.2026 18:26 · data întrebărilor: **2026-09-28** · ZIP: `/home/costin/ghid_incoming/fiscalos_intrebari_v2_rezultat.zip`

> **Scor INDICATIV, nu măsurătoare finală** (decizia 12): setul de 50 e expus — l-am văzut și am reparat clase de defecte pe el. Măsurătoarea finală va fi pe un set nou.

## Scorul de referință — pe fond (decizia C1)

| Motor | CORECT | GREȘIT | NU POT | Cost / rulare |
|---|---|---|---|---|
| **Stratul semantic (nou)** | **12** | **7** | **31** | **$2.5148** ({'intrare': 207610, 'iesire': 57535, 'cache_scriere': 0, 'cache_citire': 76550} tokeni) |
| Motorul lexical (v1, cu C5) | 4 | 17 | 29 | $0 |

Stratul semantic: modelul a propus un răspuns la 19 întrebări; **verificarea mecanică a respins 0** propuneri (citat neliteral sau cifră neliterală), iar acestea au devenit abțineri. A detectat incompletitudinea la 2 întrebări.

### Abținerile pe întrebările INCOMPLETA — separat (C1)

| Id | Motor | Incompletitudine detectată? | Ce lipsește, după motor | Cheia spune că lipsesc date? |
|---|---|---|---|---|
| Q-TVA-10 | semantic | nu — alt motiv | — | da |
| Q-PRF-10 | semantic | nu — alt motiv | — | da |
| Q-SAL-09 | semantic | **da** | Numărul persoanelor aflate în întreținere (fără / 1 / 2 / 3 / 4 și peste), de care depinde… | da |
| Q-CPF-10 | semantic | nu — alt motiv | — | da |
| Q-TVA-10 | lexical | nu — alt motiv | — | da |
| Q-PRF-10 | lexical | nu — alt motiv | — | da |
| Q-SAL-09 | lexical | nu — alt motiv | — | da |
| Q-CPF-10 | lexical | nu — alt motiv | — | da |

### Fapt corect, articol diferit de al cheii — de judecat de om (C2)

- **Q-SAL-10** (semantic): răspuns `Munca suplimentară se compensează prin ore libere plătite în…` · articolul motorului [('cm', '281')] · al cheii [('cm', '122'), (None, '123')] — *Legea 53/2003 (Codul muncii) art. 122 alin. (1) (forma OUG 117/2021); art. 123 alin. (1) și (2)*
- **Q-CTB-06** (semantic): răspuns `Nu. Pierderile din exploatare estimate pentru anul următor n…` · articolul motorului [('omfp_1802_2014', '12')] · al cheii [('omfp_1802_2014', 'pct372'), ('omfp_1802_2014', 'pct374')] — *OMFP 1802/2014, Reglementări contabile, pct. 372 alin. (1)-(2) coroborat cu pct. 374 alin. (1)*
- **Q-SAL-10** (lexical): răspuns `Plata drepturilor pentru munca suplimentară prestată în cadr…` · articolul motorului [('lege_141_2025', 'XVIII')] · al cheii [('cm', '122'), (None, '123')] — *Legea 53/2003 (Codul muncii) art. 122 alin. (1) (forma OUG 117/2021); art. 123 alin. (1) și (2)*

### Cele 7 GREȘIT ale stratului semantic — citite una câte una

Toate au **trecut** verificarea mecanică: citatele sunt literale, cifrele sunt literale. Niciuna nu e o
invenție. Categoriile de mai jos sunt citirea mea, nu un verdict mecanic — de aceea sunt separate de
scor.

| Categorie | Întrebări | Ce s-a întâmplat |
|---|---|---|
| **Regulă generală în loc de regula specială / mai nouă** | Q-PRF-09, Q-SAL-04 | Modelul a citat o regulă încă prezentă în text, dar înlocuită pentru 2026 de una specială: plata anticipată după CF art. 41 alin. (8) în loc de alin. (10^1); facilitatea pentru salariul minim din CF art. 146 (300 lei / 4.300 lei, valorile din 2025) în loc de OUG 89/2025 art. III (200 lei / 4.600 lei, septembrie 2026). **Singura clasă de greșeală reală de fond** — și exact cea pe care verificarea literală nu o poate prinde: citatul e adevărat, doar nu e cel aplicabil. Vezi C17. |
| **Calcul descris în loc de abținere** | Q-CPF-03 | Regula 3 cerea abținere la un calcul; modelul a descris calculul fără rezultat. |
| **Corect pe fond, fără cifra cheii** | Q-CTB-03, Q-CPF-09 | „maximum 65% din cei 100.000 lei" — modelul a refuzat să înmulțească, cum cere decizia C3 (calculatoarele sunt varianta b). „Nu datorează nimic" în loc de „0 lei". |
| **Fapt corect, articol diferit** | Q-SAL-10, Q-CTB-06 | Listate separat, cum cere C2. |

**Un al treilea defect de comparator**, reparat și raportat ca atare: datele scrise în litere („25 iunie
2027") nu erau recunoscute ca fapte, iar la Q-PRF-03 „faptul principal" al cheii devenea data unei
note (03.08.2026). Scorul semantic pe fond: **11 → 12** după reparație; motorul lexical neschimbat
(4 → 4) — deci reparația nu a avut efecte asupra altor chei.

**Incompletitudine detectată**: Q-SAL-09 (INCOMPLETA) — corect, cu faptele care lipsesc: numărul
persoanelor în întreținere, funcția de bază, vârsta. Și Q-SAL-02 (PROCEDURA) — din prudență,
fiindcă termenul depinde de periodicitatea angajatorului, pe care întrebarea nu o spune. La Q-TVA-10 și
Q-PRF-10 modelul s-a abținut spunând că **atomii primiți nu conțin regula** — o limită a căutării, nu
detectarea incompletitudinii.

---

## 0. CERINȚE — decizii de arhitect

### Aplicate în acest pas

| | Decizia | Cum e aplicată |
|---|---|---|
| **C1** | scorul de referință e cel pe fond; abținerile pe INCOMPLETA separat; detectarea incompletitudinii devine capacitate proprie | tabelele de mai sus; capacitatea e în stratul semantic (`stare INCOMPLET`, cu faptele lipsă și atomul care arată dependența) |
| **C2** | notarea rămâne strictă; „fapt corect, articol diferit" listat separat | lista de mai sus |
| **C3 (a)** | model Anthropic ancorat pe atomi; citatele și cifrele verificate mecanic; eșecul devine abținere | `fiscalos/semantic.py`, `verifica()` — probat pe 10 propuneri construite să-l păcălească |
| **C4** | Da/Nu permis când atomul citat conține literal răspunsul | regula 5 din promptul modelului + verificarea literală a citatului decisiv |
| **C5** | fiecare răspuns începe cu data și perimetrul presupus | câmpul `declaratie`, primul în fiecare fișier per întrebare |
| **C6, C7** | luat la cunoștință / ratificat | — |

### De decis

**C13 — Cifrele din întrebare sunt permise în răspuns.** Verificatorul acceptă o cifră care apare
literal în întrebare, chiar dacă nu apare în niciun atom (ex. „cel târziu la 14.05.2026" — data e a
cazului, nu a legii). Consecința: la o întrebare-capcană, modelul poate repeta o cifră greșită din
enunț și verificarea o lasă să treacă. Alternativa strictă — nicio cifră în afara atomilor — ar
transforma în abținere orice răspuns care numește data cazului. *De decis.*

**C14 — „Conține literal răspunsul" (C4), interpretat mecanic.** Codul poate verifica numai că citatul
decisiv e literal în atom; nu poate verifica că acel citat *decide* Da-ul sau Nu-ul — asta rămâne
judecata modelului. *De ratificat sau de strâns.*

**C15 — Fallback server-side la refuz.** Apelurile au `fallbacks: "default"` (recomandarea pentru
`claude-opus-5`): dacă modelul refuză o cerere, API-ul o rulează pe modelul de rezervă ales de
Anthropic. Modelul care a răspuns efectiv e înregistrat la fiecare apel (`apel.model`). *Îl păstrăm?*

**C17 — Regula specială / mai nouă, necontrolată mecanic.** Singura clasă de greșeală reală a
stratului semantic (Q-PRF-09, Q-SAL-04): un atom valabil și citat literal, dar înlocuit, pentru cazul
din întrebare, de o regulă specială (o derogare dintr-o OUG, un alineat nou introdus pentru anul
fiscal). Verificarea literală nu o poate prinde. Două căi, de decis: (a) căutarea aduce în context,
lângă atomul găsit, derogările și alineatele „prin excepție" care îl vizează, iar modelul primește
regula să le verifice; (b) o probă mecanică: dacă în context există un atom mai nou care derogă de la
cel citat, răspunsul devine abținere.

**C16 — Cheia API.** FiscalOS citește numai `~/.fiscalos/api_keys.env` (mod 600) și trece cheia
explicit clientului; nu folosește cheia iConta și nu cade pe variabile de mediu. Valoarea nu apare în
niciun artefact.

---

## 1. Operațiile, cu durata măsurată

| Operație | Durată |
|---|---|
| Index BM25 (31485 atomi din acte normative) | 7.06 s |
| Motorul lexical: 50 de intrebari | 1.99 s |
| Comparatia - motorul lexical | 2.45 s |
| Stratul semantic: 50 de apeluri la claude-opus-5 | 875.87 s |
| Comparatia - stratul semantic | 2.35 s |
| **Total** | **889.72 s** |

## 2. Cele 50 de întrebări

Fiecare are fișierul ei în `intrebari/v2/raspunsuri/<id>.md` — declarația de dată și perimetru (C5), răspunsul, citatele verbatim, costul apelului și comparația.

| Id | Tip | Semantic | Lexical | Răspunsul semantic |
|---|---|---|---|---|
| Q-TVA-01 | PARAMETRU | CORECT | GREȘIT | Cota standard de TVA este 21%. |
| Q-TVA-02 | PARAMETRU | CORECT | GREȘIT | Plafonul este de 395.000 lei cifră de afaceri anuală, declarată sau re… |
| Q-TVA-03 | REGULA | CORECT | GREȘIT | Trebuie să solicite înregistrarea în scopuri de TVA cel târziu la data… |
| Q-TVA-04 | REGULA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți stabilesc plafonul în eu…* |
| Q-TVA-05 | CAPCANA | CORECT | NU POT | Nu. Vânzarea utilajului (activ fix corporal) nu se cuprinde în cifra d… |
| Q-TVA-06 | CAPCANA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți nu conțin norma care reg…* |
| Q-TVA-07 | PROCEDURA | NU POT | GREȘIT | *modelul s-a abţinut: Atomii primiți se referă la dreptul de …* |
| Q-TVA-08 | CALCUL | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți privesc exclusiv ramburs…* |
| Q-TVA-09 | CALCUL | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți arată doar că băuturilor…* |
| Q-TVA-10 | INCOMPLETA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți nu conțin nici cota de T…* |
| Q-PRF-01 | PARAMETRU | NU POT | CORECT | *modelul s-a abţinut: Atomii primiți conțin doar regula gener…* |
| Q-PRF-02 | REGULA | CORECT | CORECT | Plafonul este de 100.000 euro venituri realizate în cursul anului fisc… |
| Q-PRF-03 | CAPCANA | CORECT | GREȘIT | Declarația anuală privind impozitul pe profit (D101) pentru anul fisca… |
| Q-PRF-04 | CAPCANA | NU POT | NU POT | *modelul s-a abţinut: Răspunsul ar presupune determinarea imp…* |
| Q-PRF-05 | CALCUL | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți conțin doar reguli privi…* |
| Q-PRF-06 | CALCUL | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți stabilesc doar regula de…* |
| Q-PRF-07 | CALCUL | NU POT | NU POT | *modelul s-a abţinut: Atomii dau doar regula (limita de 2% ap…* |
| Q-PRF-08 | REGULA | CORECT | NU POT | Condiția privind salariatul trebuie îndeplinită în termen de 90 de zil… |
| Q-PRF-09 | PROCEDURA | GREȘIT | GREȘIT | Plata anticipată pentru trimestrul I 2026 se stabilește în sumă de o p… |
| Q-PRF-10 | INCOMPLETA | NU POT | NU POT | *modelul s-a abţinut: Între atomii primiți nu se află textul …* |
| Q-SAL-01 | PARAMETRU | CORECT | CORECT | Cota contribuției asiguratorii pentru muncă este de 2,25%. Ea este dat… |
| Q-SAL-02 | PROCEDURA | NU POT | GREȘIT | *INCOMPLET: intrebarea nu da faptele de care depinde raspunsu…* |
| Q-SAL-03 | CALCUL | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți stabilesc doar bazele lu…* |
| Q-SAL-04 | CALCUL | GREȘIT | NU POT | Nu. Facilitatea de 300 lei/lună nu se aplică, deoarece una dintre cond… |
| Q-SAL-05 | CAPCANA | CORECT | NU POT | Nu. Contravaloarea tichetelor de masă nu se include în venitul brut ca… |
| Q-SAL-06 | CAPCANA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți stabilesc doar principiu…* |
| Q-SAL-07 | REGULA | NU POT | GREȘIT | *modelul s-a abţinut: Întrebarea are două componente, iar ato…* |
| Q-SAL-08 | CAPCANA | NU POT | GREȘIT | *modelul s-a abţinut: Atomii arată că procentul se stabilește…* |
| Q-SAL-09 | INCOMPLETA | NU POT | NU POT | *INCOMPLET: intrebarea nu da faptele de care depinde raspunsu…* |
| Q-SAL-10 | REGULA | GREȘIT | GREȘIT | Munca suplimentară se compensează prin ore libere plătite în următoare… |
| Q-CPF-01 | PARAMETRU | NU POT | GREȘIT | *modelul s-a abţinut: Atomii primiți confirmă doar că pentru …* |
| Q-CPF-02 | CALCUL | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți confirmă doar principiul…* |
| Q-CPF-03 | CALCUL | GREȘIT | GREȘIT | Firma datorează accesorii calculate de la scadența obligației principa… |
| Q-CPF-04 | REGULA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți nu conțin textul art. 11…* |
| Q-CPF-05 | PARAMETRU | NU POT | GREȘIT | *modelul s-a abţinut: Atomii primiți nu conțin norma privind …* |
| Q-CPF-06 | PROCEDURA | NU POT | GREȘIT | *modelul s-a abţinut: Atomii primiți reglementează doar modul…* |
| Q-CPF-07 | REGULA | CORECT | GREȘIT | Durata maximă a inspecției fiscale este de 45 de zile (termenul pentru… |
| Q-CPF-08 | CAPCANA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți conțin exclusiv dispoziț…* |
| Q-CPF-09 | CAPCANA | GREȘIT | NU POT | Nu datorează nimic: pentru sumele datorate cu titlu de amenzi de orice… |
| Q-CPF-10 | INCOMPLETA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți nu conțin regula care sa…* |
| Q-CTB-01 | PARAMETRU | CORECT | CORECT | 5.000 lei (valoarea fiscală la data intrării în patrimoniu trebuie să … |
| Q-CTB-02 | CAPCANA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți nu conțin nicio regulă d…* |
| Q-CTB-03 | CALCUL | GREȘIT | GREȘIT | În primul an de utilizare, amortizarea fiscală nu poate depăși 65% din… |
| Q-CTB-04 | REGULA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți provin exclusiv din Codu…* |
| Q-CTB-05 | PROCEDURA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți nu conțin regula contabi…* |
| Q-CTB-06 | CAPCANA | GREȘIT | NU POT | Nu. Pierderile din exploatare estimate pentru anul următor nu îndeplin… |
| Q-CTB-07 | CALCUL | NU POT | GREȘIT | *modelul s-a abţinut: Atomii primiți stabilesc cota de 16% ap…* |
| Q-CTB-08 | CAPCANA | CORECT | NU POT | Nu. Pentru dividendele distribuite în baza situațiilor financiare inte… |
| Q-CTB-09 | CALCUL | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți conțin doar regula de în…* |
| Q-CTB-10 | REGULA | NU POT | NU POT | *modelul s-a abţinut: Niciunul dintre atomii primiți nu conți…* |

