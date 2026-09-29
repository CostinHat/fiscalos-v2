# Q-SAL-09 — INCOMPLETA

**Întrebarea:** Cât este deducerea personală pentru un salariat cu venit brut de 5.000 lei în septembrie 2026?

## Stratul de navigare v5 — NU POT RĂSPUNDE

*La 30.09.2026, presupun o persoană fizică rezidentă salariată care realizează venit brut lunar din salarii de 5.000 lei la locul unde se află funcția de bază (întrebarea nu precizează acest element, nici situația familială), impozitată potrivit regulilor Titlului IV din Codul fiscal, cu salariul minim brut pe țară în vigoare în septembrie 2026 stabilit prin hotărâre a Guvernului.*

Datele din întrebare: 2026-09-30 · data de referință aleasă: **2026-09-30** — Faptul întrebat este deducerea personală aferentă lunii septembrie 2026, deci se aplică legislația și salariul minim în vigoare în acea lună.

Motiv: INCOMPLET: intrebarea nu da faptele de care depinde raspunsul: Numărul persoanelor aflate în întreținerea salariatului (fără, 1, 2, 3, 4 și peste) - coloana aplicabilă din tabelul de la art. 77 alin. (4); Dacă venitul de 5.000 lei este realizat la locul unde se află funcția de bază (deducerea se acordă numai acolo); Vârsta salariatului (dacă are până la 26 de ani), pentru deducerea personală suplimentară; Dacă salariatul are copii cu vârsta de până la 18 ani înscriși în unități de învățământ, pentru deducerea personală suplimentară

- **Codul fiscal (Legea 227/2015) art. 77 alin. (4)** — `cod_fiscal_227_2015_consolidat#art77/alin4` · valabil din nedovedit
  > Pentru contribuabilii care realizează venituri brute lunare din salarii de până la nivelul prevăzut la alin. (3) inclusiv, deducerile personale de bază se stabilesc potrivit următorului tabel: Persoane aflate în întreținere fără 1 pers. 2 pers. 3 pers. 4 și peste
- **Codul fiscal (Legea 227/2015) art. 77 alin. (3)** — `cod_fiscal_227_2015_consolidat#art77/alin3` · valabil din nedovedit
  > Deducerea personală de bază se acordă pentru persoanele fizice care au un venit lunar brut de până la 2.000 de lei peste nivelul salariului de bază minim brut pe țară garantat în plată aprobat prin hotărâre a Guvernului, în vigoare în luna de realizare a venitului.
- **HG 146/2026 art. 1** — `hg_146_2026_salariu_minim#art1` · valabil din 2026-07-01
  > Începând cu data de 1 iulie 2026, salariul de bază minim brut pe țară garantat în plată, prevăzut la art. 164 alin. (1) din Legea nr. 53/2003 - Codul muncii, republicată , cu modificările și completările ulterioare, se stabilește în bani, fără a include sporuri și alte adaosuri, la suma de 4.325 lei lunar
- **Codul fiscal (Legea 227/2015) art. 77 alin. (2)** — `cod_fiscal_227_2015_consolidat#art77/alin2` · valabil din nedovedit
  > Deducerea personală cuprinde deducerea personală de bază și deducerea personală suplimentară și se acordă în limita venitului impozabil lunar realizat.
- **Codul fiscal (Legea 227/2015) art. 77 alin. (10)** — `cod_fiscal_227_2015_consolidat#art77/alin10` · valabil din nedovedit
  > Deducerea personală suplimentară se acordă astfel:

### Navigarea (10 pași, 8 ture)

1. `cauta` {"interogare": "deducere personală de bază venituri din salarii"}
2. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "deducere personală"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art77/alin3"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art77"}
5. `cauta` {"interogare": "salariul de bază minim brut pe țară garantat în plată 2026"}
6. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art77/alin4"}
7. `cuprins` {"act": "hg_146_2026_salariu_minim", "filtru": "salariu"}
8. `cuprins` {"act": "hg_146_2026_salariu_minim", "filtru": ""}
9. `deschide` {"id": "hg_146_2026_salariu_minim#art1"}
10. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art77/alin10"}

Apel: `claude-opus-5`, {'intrare': 16, 'iesire': 4530, 'cache_scriere': 10742, 'cache_citire': 96203} tokeni, $0.2286, 68 s

Pe fond (comparator): **NU POT** — INCOMPLETA: motorul s-a abţinut, iar cheia spune si ea ca lipsesc date

## v4 — NU POT, pe fond NU POT

> INCOMPLET: intrebarea nu da faptele de care depinde raspunsul: numărul persoanelor aflate în întreținerea salariatului (fără / 1 / 2 / 3 / 4 și peste), de care depinde procentul din salariul minim aplicabil potrivit tabelului de la art. 77 alin. (4); dacă veniturile sunt realizate la funcția de bază (locul unde este depus dosarul), condiție de acordare a deducerii personale; dacă salariatul are sub 26 de ani sau are copii până la 18 ani înscriși într-o unitate de învățământ, elemente de care dep…

## Cheia

- Depinde — trebuie clarificat: dacă venitul e la funcția de bază, numărul persoanelor în întreținere, vârsta (sub 26 ani → deducere suplimentară 15% din salariul minim) și copiii sub 18 ani înscriși la școală (100 lei/copil). Exemplu: funcție de bază, fără persoane în întreținere, peste 26 ani, fără copii → 13,00% × 4.325 = 562,25 lei (tranșa salariul minim + 651…700 lei)
- temei: Cod fiscal art. 77 alin. (1), (3), (4) (tabel), (10) lit. a) și b); HG 146/2026 art. 1
