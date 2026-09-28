# Q-CPF-06 — PROCEDURA

**Întrebarea:** O firmă a depus decont de TVA cu opțiune de rambursare. În ce termen trebuie ANAF să soluționeze cererea, și dacă analiza de risc impune inspecție fiscală anticipată?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 28.09.2026, presupun o societate înregistrată în scopuri de TVA care a depus un decont cu sumă negativă de TVA cu opțiune de rambursare (cerere de rambursare adresată organului fiscal central), fără să se precizeze categoria de contribuabil (mare/mijlociu/mic), și analizez termenul general de soluționare a cererilor din Codul de procedură fiscală.*

> **Termenul general este de 45 de zile de la înregistrarea cererii. Dacă, pe baza analizei de risc, soluționarea necesită efectuarea inspecției fiscale (inspecție anticipată, parțială), termenul este de cel mult 90 de zile de la înregistrarea cererii, iar firma este notificată despre termenul aplicabil în termen de 5 zile de la finalizarea analizei de risc. Termenele se pot prelungi cu perioada necesară administrării de probe suplimentare.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul de procedură fiscală (Legea 207/2015) art. 77 alin. (1)** — `legea_207_2015_consolidat#art77/alin1` · valabil din nedovedit
  > Cererile depuse de către contribuabil/plătitor la organul fiscal se soluționează de către acesta în termen de 45 de zile de la înregistrare.
- **Codul de procedură fiscală (Legea 207/2015) art. 77 alin. (5)** — `legea_207_2015_consolidat#art77/alin5` · valabil din nedovedit
  > În situația în care, pe baza analizei de risc, soluționarea cererii necesită efectuarea inspecției fiscale, termenul de soluționare a cererii este de cel mult 90 de zile de la înregistrarea cererii, prevederile alin. (2)-(4) aplicându-se în mod corespunzător. În acest caz contribuabilul/plătitorul este notificat cu privire la termenul de soluționare aplicabil în termen de 5 zile de la finalizarea analizei de risc.
- **Codul de procedură fiscală (Legea 207/2015) art. 77 alin. (2)** — `legea_207_2015_consolidat#art77/alin2` · valabil din nedovedit
  > În situațiile în care, pentru soluționarea cererii, este necesară administrarea de probe suplimentare relevante pentru luarea deciziei, acest termen se prelungește cu perioada cuprinsă între data solicitării probei și da
- **Codul de procedură fiscală (Legea 207/2015) art. 169 alin. (9)** — `legea_207_2015_consolidat#art169/alin9` · valabil din nedovedit
  > În cazul inspecției fiscale anticipate, efectuate pentru soluționarea deconturilor cu sumă negativă de TVA, prin excepție de la prevederile art. 117 , perioada supusă inspecției fiscale va cuprinde exclusiv perioadele fiscale în care s-au derulat operațiunile care au generat soldul sumei negative a taxei.
- derogare tratată: `legea_207_2015_consolidat#art169/alin9` — Atom-excepție față de art. 117 (perioada supusă inspecției): îl citez, întrucât în ipoteza inspecției fiscale anticipate pentru soluționarea decontului cu sumă negativă de TVA perioada verificată se limitează la perioadele fiscale care au generat soldul negativ.

### Navigarea (8 pași, 5 ture)

1. `cauta` {"interogare": "rambursarea TVA soluționarea deconturilor cu sume negative inspecție fiscală anticipată"}
2. `cuprins` {"act": "legea_207_2015_consolidat", "filtru": "rambursare"}
3. `deschide` {"id": "legea_207_2015_consolidat#art169/alin1"}
4. `deschide` {"id": "legea_207_2015_consolidat#art169/alin9"}
5. `deschide` {"id": "legea_207_2015_consolidat#art169"}
6. `cauta` {"interogare": "termenul de soluționare a cererilor 45 de zile de la înregistrare"}
7. `deschide` {"id": "legea_207_2015_consolidat#art77/alin5"}
8. `deschide` {"id": "legea_207_2015_consolidat#art77/alin1"}

Apel: `claude-opus-5`, {'intrare': 10, 'iesire': 2788, 'cache_scriere': 5816, 'cache_citire': 41515} tokeni, $0.1269, 45 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți reglementează regula rambursării cu inspecție fiscală ulterioară și cazurile în care decontul se soluționează după inspecție fiscală anticipată (inclusiv riscul de rambursare necuvenită constatat de organul fiscal central), dar niciunul dintre ei nu conține termenul legal de soluționare a cererii de rambursare (numărul de zile în care organul fiscal trebuie să soluționeze decontul, nici termenul prelungit în cazul inspecției anticipate). Nu pot indica un terme…

## Cheia

- 45 de zile de la înregistrarea cererii; dacă e necesară inspecția fiscală (pe baza analizei de risc), cel mult 90 de zile de la înregistrare (inspecție parțială), cu prelungirile pentru probe suplimentare (2/3/6 luni). Dacă termenul e depășit, firma are dreptul la dobândă 0,02%/zi, la cerere.
- temei: Legea 207/2015 art. 77 alin. (1), (2) și (5); art. 182 alin. (1) și (4)
