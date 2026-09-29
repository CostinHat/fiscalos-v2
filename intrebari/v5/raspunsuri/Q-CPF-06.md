# Q-CPF-06 — PROCEDURA

**Întrebarea:** O firmă a depus decont de TVA cu opțiune de rambursare. În ce termen trebuie ANAF să soluționeze cererea, și dacă analiza de risc impune inspecție fiscală anticipată?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 28.09.2026, presupun o persoană impozabilă înregistrată în scopuri de TVA (societate, contribuabil mic/mijlociu/mare nespecificat), care a depus în termen un decont cu sumă negativă de TVA cu opțiune de rambursare la organul fiscal central, cererea fiind supusă regulilor generale de soluționare din Codul de procedură fiscală; nu presupun existența unei suspendări a inspecției fiscale.*

Datele din întrebare: niciuna (ziua întrebării) · data de referință aleasă: **2026-09-28** — Întrebarea nu poartă nicio dată proprie; faptul întrebat (termenul de soluționare aplicabil unei cereri de rambursare depuse acum) se apreciază la data întrebării.

> **Regula generală: cererea (decontul cu opțiune de rambursare) se soluționează în termen de 45 de zile de la înregistrare, termen care se prelungește cu perioada necesară administrării de probe suplimentare. Dacă, pe baza analizei de risc, soluționarea necesită efectuarea inspecției fiscale (inspecție fiscală anticipată, parțială), termenul de soluționare este de cel mult 90 de zile de la înregistrarea cererii, iar contribuabilul trebuie notificat cu privire la termenul aplicabil în termen de 5 zile de la finalizarea analizei de risc. La inspecția fiscală anticipată pentru deconturi negative de TVA, perioada verificată cuprinde exclusiv perioadele fiscale în care s-au derulat operațiunile care au generat soldul sumei negative a taxei.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul de procedură fiscală (Legea 207/2015) art. 77 alin. (1)** — `legea_207_2015_consolidat#art77/alin1` · valabil din nedovedit
  > Cererile depuse de către contribuabil/plătitor la organul fiscal se soluționează de către acesta în termen de 45 de zile de la înregistrare.
- **Codul de procedură fiscală (Legea 207/2015) art. 77 alin. (5)** — `legea_207_2015_consolidat#art77/alin5` · valabil din nedovedit
  > În situația în care, pe baza analizei de risc, soluționarea cererii necesită efectuarea inspecției fiscale, termenul de soluționare a cererii este de cel mult 90 de zile de la înregistrarea cererii, prevederile alin. (2)-(4) aplicându-se în mod corespunzător. În acest caz contribuabilul/plătitorul este notificat cu privire la termenul de soluționare aplicabil în termen de 5 zile de la finalizarea analizei de risc.
- **Codul de procedură fiscală (Legea 207/2015) art. 169 alin. (1)** — `legea_207_2015_consolidat#art169/alin1` · valabil din nedovedit
  > Taxa pe valoarea adăugată, denumită în continuare TVA, solicitată la rambursare prin deconturile cu sumă negativă de TVA cu opțiune de rambursare, depuse în cadrul termenului legal de depunere, se rambursează de organul fiscal central, cu efectuarea, ulterior, a inspecției fiscale.
- **Codul de procedură fiscală (Legea 207/2015) art. 169 alin. (9)** — `legea_207_2015_consolidat#art169/alin9` · valabil din nedovedit
  > În cazul inspecției fiscale anticipate, efectuate pentru soluționarea deconturilor cu sumă negativă de TVA, prin excepție de la prevederile art. 117 , perioada supusă inspecției fiscale va cuprinde exclusiv perioadele fiscale în care s-au derulat operațiunile care au generat soldul sumei negative a taxei.
- derogare tratată: `legea_207_2015_consolidat#art169/alin9` — Excepția vizează art. 117 (perioada supusă inspecției fiscale), nu termenele din art. 77; am citat-o pentru a arăta limitarea perioadei verificate în cazul inspecției anticipate pentru deconturi negative de TVA.

### Navigarea (9 pași, 6 ture)

1. `cauta` {"interogare": "rambursarea TVA decont cu sumă negativă opțiune de rambursare inspecție fiscală anticipată"}
2. `cuprins` {"act": "legea_207_2015_consolidat", "filtru": "rambursare"}
3. `deschide` {"id": "legea_207_2015_consolidat#art169/alin1"}
4. `deschide` {"id": "legea_207_2015_consolidat#art169"}
5. `cauta` {"interogare": "termen de soluționare a cererilor 45 de zile de la înregistrare"}
6. `deschide` {"id": "legea_207_2015_consolidat#art77/alin1"}
7. `deschide` {"id": "legea_207_2015_consolidat#art77/alin5"}
8. `deschide` {"id": "legea_207_2015_consolidat#art169/alin9"}
9. `deschide` {"id": "legea_207_2015_consolidat#art77"}

Apel: `claude-opus-5`, {'intrare': 12, 'iesire': 3227, 'cache_scriere': 6744, 'cache_citire': 57024} tokeni, $0.1514, 48 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond CORECT

> Termenul general este de 45 de zile de la înregistrarea cererii. Dacă, pe baza analizei de risc, soluționarea necesită efectuarea inspecției fiscale (inspecție anticipată, parțială), termenul este de cel mult 90 de zile de la înregistrarea cererii, iar firma este notificată despre termenul aplicabil în termen de 5 zile de la finalizarea analizei de risc. Termenele se pot prelungi cu perioada necesară administrării de probe suplimentare.

## Cheia

- 45 de zile de la înregistrarea cererii; dacă e necesară inspecția fiscală (pe baza analizei de risc), cel mult 90 de zile de la înregistrare (inspecție parțială), cu prelungirile pentru probe suplimentare (2/3/6 luni). Dacă termenul e depășit, firma are dreptul la dobândă 0,02%/zi, la cerere.
- temei: Legea 207/2015 art. 77 alin. (1), (2) și (5); art. 182 alin. (1) și (4)
