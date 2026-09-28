# FiscalOS v2 — Motorul de întrebări v3: consolidatele oficiale și relația de derogare

Generat 28.09.2026 19:15 · ZIP: `/home/costin/ghid_incoming/fiscalos_intrebari_v3_rezultat.zip`

> **Scor INDICATIV** — setul de 50 e expus. Măsurătoarea finală va fi pe setul nou.

## Scorul pe fond

| Motor | CORECT | GREȘIT | NU POT | Cost / rulare |
|---|---|---|---|---|
| **Stratul semantic v3** | **10** | **8** | **32** | **$3.2538** |
| Stratul semantic v2 (rularea precedentă) | 11 | 8 | 31 | $2.5148 |
| Motorul lexical v3 (L2) | 2 | 12 | 36 | $0 |
| Motorul lexical L0 — instantaneul iConta, fara relatia C17 | 4 | 17 | 29 | $0 |
| Motorul lexical L1 — + consolidatele oficiale (C12) | 4 | 17 | 29 | $0 |

Tokeni stratul semantic v3: {'intrare': 241303, 'iesire': 79523, 'cache_scriere': 1923, 'cache_citire': 94227}. Verificarea mecanică a respins 1 propuneri — din care 0 pentru o derogare netratată (C17 b: —) și 0 pentru o valoare legală nedovedită din atom (C13: —). Model de rezervă folosit (C15): niciodată.

## Abțineri dispărute — separat, pe cauze (decizia 7)

**Stratul semantic** (v2 → v3), atribuire cauzală pe citate — vezi antetul `raport_intrebari_v3.py`:

| Cauza | Câte | Întrebări |
|---|---|---|
| **prin consolidatele noi** (citează un atom nou/schimbat față de instantaneu) | **0** | — |
| **prin relația de derogare** (citează/tratează un atom adus de relație) | **0** | — |
| variație între rulări (nicio citare nouă, nicio derogare) | 1 | Q-SAL-08 |

Abțineri apărute (răspunsuri v2 retrase în v3): Q-TVA-05 — modelul s-a abţinut; Q-SAL-04 — modelul s-a abţinut.

**Motorul lexical**, ablație exactă (e determinist):

| Pas | Abțineri dispărute | Abțineri apărute | Răspunsuri retrase greșite / corecte |
|---|---|---|---|
| L0->L1 — prin consolidatele noi | 1 ['Q-CPF-04'] | 1 | 1 / 0 |
| L1->L2 — prin relația de derogare (b) | 0  | 7 | 5 / 2 |

La motorul lexical, relația nu poate *elimina* abțineri — el nu tratează derogări, doar se abține în fața lor. Calea (a) contează numai pentru stratul semantic.

### Efectul relației de derogare asupra GREȘELILOR (nu asupra abținerilor)

Atribuirea pe abțineri nu vede efectul principal al relației. Cele două greșeli reale de fond din v2 — regula generală citată în locul celei speciale — **nu mai sunt răspunsuri greșite pe regulă**, și amândouă au derogările aduse de relație tratate explicit în răspuns:

- **Q-PRF-09** — v2: GREȘIT (regula generală). v3: răspuns cu regula specială (CF art. 41 alin. (10^1)) — *Pentru trimestrul I 2026 plata anticipată nu se mai determină ca o pătrime din impozitul anului precedent, ci prin aplicarea cotei de impozit asupra profitului …*; notat **GREȘIT** pe fond, fiindcă nu conține cifra de 16% din cheie (cota stă în CF art. 17, necitat). Derogări tratate de model: `art41/alin8`, `art45/alin8`, `artVIII/alin1`, `art41/alin7`, `art41/alin10`, `art42^9/alin3`.
- **Q-SAL-04** — v2: GREȘIT (regula generală). v3: abținere — modelul a găsit derogările și a refuzat să răspundă cu valorile din 2025. Derogări tratate de model: `art146/alin5^6`, `artLXXIII/alin1`.

### Defecte de clasă găsite după comparație (decizia: raportate cu scorul înainte și după)

**V1 — verificatorul trata identificatorul unui act („OPANAF 587/2016") ca pe o valoare.** Reparat. Măsurat EXACT, fără niciun apel nou: propunerile salvate ale modelului au fost re-verificate (`semantic.reverifica`, contextul se reconstruiește determinist). Scor semantic pe fond: **10/7/33 → 10/8/32**. Q-PRF-09 trece verificarea; notat GREȘIT de comparatorul strict, din motivul de mai sus.

**V2 — notele cu dispoziții tranzitorii citate devin pseudo-articole ale Codului.** Forma consolidată oficială pune, după unele alineate, note care citează textul actului modificator („Articolul III din OG 22/2025 prevede: (6) …"). Conversia mea le atomizează ca articole romane ale Codului fiscal (`cod_fiscal…#artIII~2/alin6~2`). La Q-TVA-03, modelul a citat nota în locul art. 310 alin. (6), cu același text — răspuns corect pe fond, notat GREȘIT pentru articol (din CORECT în v2). Tot de aici vin sursele de derogare din C20 („Art. VIII"). **Nereparat** — vezi C22.

### Cele 8 GREȘIT ale stratului semantic v3 — de citit

- **Q-TVA-03** (REGULA): motorul — Firma trebuie să solicite înregistrarea în scopuri de TVA cel târziu la data depășirii plafonului, adică cel târziu în 14.05.2026. Regimul n… · cheia — Cel târziu la data depășirii plafonului (14.05.2026); regimul normal se aplică din data depășirii, începând cu tranzacția care a condus la d…
- **Q-PRF-09** (PROCEDURA): motorul — Pentru trimestrul I 2026 plata anticipată nu se mai determină ca o pătrime din impozitul anului precedent, ci prin aplicarea cotei de impozi… · cheia — 16% × profitul contabil al trimestrului I 2026 (NU 1/4 din impozitul anului precedent actualizat cu IPC); D100, cod obligație 103; termen no…
- **Q-SAL-08** (CAPCANA): motorul — Se aplică procentul de 65%, corespunzător perioadei cuprinse între 8 și 14 zile, deoarece zilele certificatului inițial se adună cu zilele c… · cheia — Procentul se stabilește pe episodul de boală (10 zile) → 65% pentru tot episodul, inclusiv zilele din septembrie; diferența 55%→65% pentru s…
- **Q-SAL-10** (REGULA): motorul — Munca suplimentară se compensează prin ore libere plătite în următoarele 90 de zile calendaristice după efectuarea acesteia. Dacă această co… · cheia — Ore libere plătite în următoarele 90 de zile calendaristice; altfel se plătesc cu spor negociat de minim 75% din salariul de bază (în luna u…
- **Q-CPF-03** (CALCUL): motorul — Firma datorează penalitate de nedeclarare de 0,08% pe fiecare zi, începând cu ziua imediat următoare scadenței inițiale (25.07.2025) și până… · cheia — 252 zile (26.07.2025–03.04.2026 inclusiv). Penalitate de nedeclarare 20.000 × 0,08% × 252 = 4.032 lei, redusă cu 75% (plată până la 05.04.20…
- **Q-CPF-09** (CAPCANA): motorul — Nu datorează nimic cu titlu de dobânzi și penalități de întârziere: pentru sumele datorate cu titlu de amenzi de orice fel nu se calculează … · cheia — 0 lei: nu se datorează dobânzi și penalități de întârziere pentru amenzi de orice fel (nici pentru accesorii, cheltuieli de executare etc.).
- **Q-CTB-03** (CALCUL): motorul — În primul an de utilizare, amortizarea fiscală nu poate depăși 65% din valoarea fiscală a activului de la data intrării în patrimoniu. · cheia — 65.000 lei (maxim 65% din valoarea fiscală de intrare); restul de 35.000 lei se amortizează în anii următori raportat la durata normală de u…
- **Q-CTB-06** (CAPCANA): motorul — Nu. Simpla estimare a unor pierderi viitoare din exploatare pentru 2027 nu permite recunoașterea unui provizion la 31.12.2026: un provizion … · cheia — Nu. Nu se recunosc provizioane pentru pierderi viitoare din exploatare (nu corespund definiției unei datorii); activele de exploatare se tes…

Fapt corect, articol diferit (C2): Q-TVA-03, Q-SAL-10, Q-CTB-06.
Abțineri pe INCOMPLETA (C1): Q-TVA-10 — alt motiv; Q-PRF-10 — alt motiv; Q-SAL-09 — incompletitudine detectată; Q-CPF-10 — alt motiv.

---

## 0. CERINȚE — decizii de arhitect

### Aplicate în acest pas

| | Decizia | Cum e aplicată |
|---|---|---|
| **C12** | consolidatele la zi, din legislatie.just.ro, într-un strat propriu, cu proveniență, dată și SHA | `surse_oficiale/` + `MANIFEST.json`; instantaneul iConta neatins; lista în `propuneri/v4/acte_aduse.json` |
| **C13** | cifrele din întrebare numai ca fapte ale cazului; o valoare legală se dovedește din atom | `semantic.e_valoare_legala()` + verificare |
| **C14** | lângă orice Da/Nu, citatul decisiv | `citat_decisiv`, în fiecare fișier per întrebare |
| **C15** | fallback-ul se păstrează; răspunsul de la modelul de rezervă e marcat | `apel.fallback`; lista din tabelul de scor |
| **C16** | luat la cunoștință | — |
| **C17** | relația „modifică / derogă / prin excepție", extrasă din text; (a) în context, (b) plasa de siguranță | `fiscalos/relatii.py`: 883 de muchii (543 excepții, 338 derogări, 2 modificări neîncorporate), 234 de trimiteri nerezolvabile, numărate |

### De decis

**C20 — Dispozițiile tranzitorii citate în consolidat.** Forma consolidată oficială a Codului fiscal
conține dispoziții tranzitorii citate din OUG-uri („Art. VIII … prin derogare de la art. 41 alin.
(8)"), fără dată de expirare în text. Relația le tratează ca derogări valabile, deci plasa de siguranță
(b) poate produce abțineri în plus — o eroare în direcția sigură. *De decis:* se caută data de
expirare a fiecărei dispoziții tranzitorii (în actul-sursă), sau abținerea în plus e acceptată?

**C22 — Notele tranzitorii din consolidatul oficial (V2).** Repararea — atomii unui articol roman
dintr-un cod cu articole arabe marcați „notă: dispoziție tranzitorie citată", penalizați la căutare
și numiți ca atare în temei — schimbă contextul modelului, deci efectul ei pe stratul semantic se
măsoară numai cu o rulare nouă (~$3,3, cu variația de la o rulare la alta). *De decis:* se repară și
se măsoară acum, sau odată cu setul nou?

**C21 — Plasa de siguranță costă răspunsuri corecte la motorul lexical.** L1 → L2 a retras 7
răspunsuri: 5 greșite, 2 corecte. Motorul lexical nu poate trata o derogare, doar se poate abține. *De
decis:* motorul lexical rămâne cu plasa (mai puține greșeli), sau ea se aplică numai stratului semantic?

---

## Operațiile, cu durata și costul măsurate

| Operație | Durată | Cost |
|---|---|---|
| Aducerea celor 6 acte din legislatie.just.ro | 52.0 s | $0 |
| Stratul semantic v3: 50 de apeluri la `claude-opus-5` | 1152.3 s | $3.2538 |
| Motorul lexical L0 (index + 50 de întrebări + comparație) | 15.5 s | $0 |
| Motorul lexical L1 (index + 50 de întrebări + comparație) | 15.2 s | $0 |
| Motorul lexical L2 (index + 50 de întrebări + comparație) | 21.5 s | $0 |
| Comparații, atribuire, raport | 25.0 s | $0 |

## Cele 50 de întrebări

| Id | Tip | Semantic | Lexical | Răspunsul semantic |
|---|---|---|---|---|
| Q-TVA-01 | PARAMETRU | CORECT | GREȘIT | Cota standard de TVA este 21%. |
| Q-TVA-02 | PARAMETRU | CORECT | NU POT | Plafonul cifrei de afaceri anuale, declarate sau realizate, este de 39… |
| Q-TVA-03 | REGULA | GREȘIT | GREȘIT | Firma trebuie să solicite înregistrarea în scopuri de TVA cel târziu l… |
| Q-TVA-04 | REGULA | NU POT | NU POT | *modelul s-a abţinut: Plafonul din atomul aplicabil este expr…* |
| Q-TVA-05 | CAPCANA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți conțin plafonul de scuti…* |
| Q-TVA-06 | CAPCANA | NU POT | NU POT | *modelul s-a abţinut: Niciun atom primit nu conține regula pr…* |
| Q-TVA-07 | PROCEDURA | NU POT | GREȘIT | *modelul s-a abţinut: Niciunul dintre atomii primiți nu regle…* |
| Q-TVA-08 | CALCUL | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți privesc înregistrarea în…* |
| Q-TVA-09 | CALCUL | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți conțin doar reguli privi…* |
| Q-TVA-10 | INCOMPLETA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți nu conțin nici cota de T…* |
| Q-PRF-01 | PARAMETRU | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți nu conțin nicio dispoziț…* |
| Q-PRF-02 | REGULA | CORECT | NU POT | Plafonul este de 100.000 euro venituri realizate într-un an fiscal. Ve… |
| Q-PRF-03 | CAPCANA | CORECT | GREȘIT | Declarația anuală privind impozitul pe profit (D101) pentru anul fisca… |
| Q-PRF-04 | CAPCANA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți nu conțin regula de dete…* |
| Q-PRF-05 | CALCUL | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți conțin doar reguli privi…* |
| Q-PRF-06 | CALCUL | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți nu conțin regula aplicab…* |
| Q-PRF-07 | CALCUL | NU POT | NU POT | *modelul s-a abţinut: Atomul primit stabilește doar regula (l…* |
| Q-PRF-08 | REGULA | CORECT | NU POT | Condiția privind salariatul trebuie îndeplinită în termen de 90 de zil… |
| Q-PRF-09 | PROCEDURA | GREȘIT | NU POT | Pentru trimestrul I 2026 plata anticipată nu se mai determină ca o păt… |
| Q-PRF-10 | INCOMPLETA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți nu conțin norma care sta…* |
| Q-SAL-01 | PARAMETRU | CORECT | CORECT | Cota contribuției asiguratorii pentru muncă este de 2,25%, aplicată as… |
| Q-SAL-02 | PROCEDURA | NU POT | NU POT | *INCOMPLET: intrebarea nu da faptele de care depinde raspunsu…* |
| Q-SAL-03 | CALCUL | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți conțin doar reguli privi…* |
| Q-SAL-04 | CALCUL | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți nu conțin nicio normă ca…* |
| Q-SAL-05 | CAPCANA | CORECT | NU POT | Nu, nu pierde facilitatea. Plafonul de 4.600 lei inclusiv (valabil 1 i… |
| Q-SAL-06 | CAPCANA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți stabilesc doar regula ba…* |
| Q-SAL-07 | REGULA | NU POT | GREȘIT | *modelul s-a abţinut: Atomii primiți nu conțin regula privind…* |
| Q-SAL-08 | CAPCANA | GREȘIT | GREȘIT | Se aplică procentul de 65%, corespunzător perioadei cuprinse între 8 ș… |
| Q-SAL-09 | INCOMPLETA | NU POT | NU POT | *INCOMPLET: intrebarea nu da faptele de care depinde raspunsu…* |
| Q-SAL-10 | REGULA | GREȘIT | GREȘIT | Munca suplimentară se compensează prin ore libere plătite în următoare… |
| Q-CPF-01 | PARAMETRU | NU POT | GREȘIT | *modelul s-a abţinut: Atomii primiți conțin doar regula gener…* |
| Q-CPF-02 | CALCUL | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți confirmă doar că se dato…* |
| Q-CPF-03 | CALCUL | GREȘIT | NU POT | Firma datorează penalitate de nedeclarare de 0,08% pe fiecare zi, înce… |
| Q-CPF-04 | REGULA | NU POT | GREȘIT | *VERIFICAREA MECANICA a respins propunerea modelului: cifra '…* |
| Q-CPF-05 | PARAMETRU | NU POT | GREȘIT | *modelul s-a abţinut: Atomii primiți confirmă doar că împotri…* |
| Q-CPF-06 | PROCEDURA | NU POT | GREȘIT | *modelul s-a abţinut: Atomii primiți reglementează regula ram…* |
| Q-CPF-07 | REGULA | CORECT | GREȘIT | Durata inspecției fiscale nu poate fi mai mare de 45 de zile (categori… |
| Q-CPF-08 | CAPCANA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți conțin exclusiv dispoziț…* |
| Q-CPF-09 | CAPCANA | GREȘIT | NU POT | Nu datorează nimic cu titlu de dobânzi și penalități de întârziere: pe… |
| Q-CPF-10 | INCOMPLETA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți nu conțin norma care san…* |
| Q-CTB-01 | PARAMETRU | CORECT | CORECT | Valoarea fiscală minimă la data intrării în patrimoniu este de 5.000 l… |
| Q-CTB-02 | CAPCANA | NU POT | NU POT | *modelul s-a abţinut: Niciunul dintre atomii primiți nu conți…* |
| Q-CTB-03 | CALCUL | GREȘIT | NU POT | În primul an de utilizare, amortizarea fiscală nu poate depăși 65% din… |
| Q-CTB-04 | REGULA | NU POT | NU POT | *modelul s-a abţinut: Întrebarea vizează amortizarea CONTABIL…* |
| Q-CTB-05 | PROCEDURA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți nu conțin regula contabi…* |
| Q-CTB-06 | CAPCANA | GREȘIT | NU POT | Nu. Simpla estimare a unor pierderi viitoare din exploatare pentru 202… |
| Q-CTB-07 | CALCUL | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți conțin cota de impozit (…* |
| Q-CTB-08 | CAPCANA | CORECT | NU POT | Nu. Pentru dividendele distribuite în baza situațiilor financiare inte… |
| Q-CTB-09 | CALCUL | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți stabilesc doar condiția …* |
| Q-CTB-10 | REGULA | NU POT | NU POT | *modelul s-a abţinut: Atomii primiți nu conțin regula privind…* |
