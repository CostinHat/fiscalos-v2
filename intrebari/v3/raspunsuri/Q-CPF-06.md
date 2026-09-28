# Q-CPF-06 — PROCEDURA

**Întrebarea:** O firmă a depus decont de TVA cu opțiune de rambursare. În ce termen trebuie ANAF să soluționeze cererea, și dacă analiza de risc impune inspecție fiscală anticipată?

## Stratul semantic — NU POT RĂSPUNDE

*La data de referință 28.09.2026, presupun o persoană impozabilă înregistrată în scopuri de TVA în România, care a depus în termenul legal un decont cu sumă negativă de TVA cu opțiune de rambursare la organul fiscal central, fără să se precizeze categoria (mare/mijlociu/alt contribuabil) sau existența unor situații de risc.*

Motiv: modelul s-a abţinut: Atomii primiți reglementează regula rambursării cu inspecție fiscală ulterioară și cazurile în care decontul se soluționează după inspecție fiscală anticipată (inclusiv riscul de rambursare necuvenită constatat de organul fiscal central), dar niciunul dintre ei nu conține termenul legal de soluționare a cererii de rambursare (numărul de zile în care organul fiscal trebuie să soluționeze decontul, nici termenul prelungit în cazul inspecției anticipate). Nu pot indica un termen fără un atom care să îl prevadă literal, iar deducerea lui ar însemna folosirea unor cunoștințe din afara contextului.

- **Codul de procedură fiscală (Legea 207/2015) art. 169 alin. (1)** — `legea_207_2015_consolidat#art169/alin1` · valabil din nedovedit
  > Taxa pe valoarea adăugată, denumită în continuare TVA, solicitată la rambursare prin deconturile cu sumă negativă de TVA cu opțiune de rambursare, depuse în cadrul termenului legal de depunere, se rambursează de organul fiscal central, cu efectuarea, ulterior, a inspecției fiscale.
- **Codul de procedură fiscală (Legea 207/2015) art. 169 alin. (2)** — `legea_207_2015_consolidat#art169/alin2` · valabil din nedovedit
  > Prevederile alin. (1) nu se aplică deconturilor cu sume negative de TVA cu opțiune de rambursare, depuse de contribuabilii mari și mijlocii, stabiliți potrivit prevederilor art. 30 alin. (3) , care se soluționează după efectuarea inspecției fiscale anticipate, în cazul în care:
- **Codul de procedură fiscală (Legea 207/2015) art. 169 alin. (2) lit. b)** — `legea_207_2015_consolidat#art169/alin2/litb` · valabil din nedovedit
  > organul fiscal central, pe baza informațiilor deținute, constată că există riscul unei rambursări necuvenite; ...
- derogare tratată: `legea_207_2015_consolidat#art167/alin13` — Derogarea privește doar situația confirmării unui acord de restructurare/omologării unui plan de restructurare și modul de preluare a soldului negativ; nu se aplică cazului descris (decont obișnuit cu opțiune de rambursare) și, oricum, nu privește termenul de soluționare.
- derogare tratată: `legea_207_2015_consolidat#art121/alin1^1` — Derogarea vizează selectarea aleatorie pentru inspecție fiscală (maximum 10% din contribuabilii selectați într-un an), nu regimul de soluționare a decontului cu opțiune de rambursare; nu am invocat art. 121 alin. (1) ca temei.

Apel: `claude-opus-5`, {'intrare': 4645, 'iesire': 1875, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0711

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți reglementează regula rambursării cu inspecție fiscală ulterioară și cazurile în care decontul se soluționează după inspecție fiscală anticipată (inclusiv riscul de

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-09-28 (implicita (ziua intrebarii)). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **soldul sumei negative de TVA solicitată la rambursare provine dintr-un număr de perioade mai mare decât numărul perioadelor de raportare utilizate într-o perioadă de 12 luni.**

Motiv: D15: fraza care conţine un fapt de forma cerută (termen) si potriveste cel mai bine intrebarea (scor local 7.9)

- **Codul de procedură fiscală (Legea 207/2015) art. 169 alin. (3) lit. e)** — `legea_207_2015_consolidat#art169/alin3/lite` · valabil din nedovedit
  > soldul sumei negative de TVA solicitată la rambursare provine dintr-un număr de perioade mai mare decât numărul perioadelor de raportare utilizate într-o perioadă de 12 luni. ...

Pe fond: **GREȘIT** — faptul principal al cheii (['45 zile']) nu e in raspuns; articolul citat [('cpf', '169')] nu e printre cele ale cheii [('cpf', '77'), (None, '182')]

## Cheia

- 45 de zile de la înregistrarea cererii; dacă e necesară inspecția fiscală (pe baza analizei de risc), cel mult 90 de zile de la înregistrare (inspecție parțială), cu prelungirile pentru probe suplimentare (2/3/6 luni). Dacă termenul e depășit, firma are dreptul la dobândă 0,02%/zi, la cerere.
- temei: Legea 207/2015 art. 77 alin. (1), (2) și (5); art. 182 alin. (1) și (4)
