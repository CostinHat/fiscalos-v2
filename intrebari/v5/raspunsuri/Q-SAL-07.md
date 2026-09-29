# Q-SAL-07 — REGULA

**Întrebarea:** Salariat cu stagiu minim îndeplinit primește certificat de concediu medical pentru boală obișnuită (cod 01), eliberat pentru 10 zile, în 2026. Ce procent din baza de calcul și cine suportă indemnizația?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 28.09.2026, presupun un salariat asigurat la angajator (art. 1 alin. (1) lit. A din OUG 158/2005), cu stagiul minim de asigurare îndeplinit, care prezintă un certificat de concediu medical pentru boală obișnuită (cod 01) eliberat pentru 10 zile în 2026 (deci în perioada 1 februarie 2026-31 decembrie 2027), fără situație de izolare potrivit Legii nr. 136/2020 și fără boală din categoriile speciale (tuberculoză, SIDA, neoplazii, boli infectocontagioase grupa A, urgențe medico-chirurgicale, boli cardiovasculare).*

Datele din întrebare: 2026-09-28 · data de referință aleasă: **2026-09-28** — Singura dată din întrebare: certificatul de concediu medical este eliberat în 2026, iar faptul întrebat (procent și suportare) se apreciază la data eliberării certificatului.

> **Se aplică procentul de 65% asupra bazei de calcul, întrucât certificatul este eliberat pentru o perioadă cuprinsă între 8 și 14 zile de incapacitate temporară de muncă. Suportarea: pentru certificatele eliberate în perioada 1 februarie 2026-31 decembrie 2027 indemnizația se calculează și se plătește prin diminuarea cu o zi (prima zi nu se plătește), angajatorul suportă din a 2-a zi până inclusiv în a 6-a zi de incapacitate, iar din ziua următoare celor suportate de angajator și până la încetarea incapacității indemnizația se suportă din bugetul Fondului național unic de asigurări sociale de sănătate.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **OUG 158/2005 art. 17 alin. (1) lit. b)** — `oug_158_2005_consolidat#art17/alin1/litb` · valabil din nedovedit
  > prin aplicarea procentului de 65% asupra bazei de calcul stabilite conform art. 10 pentru certificatele de concediu medical eliberate pentru o perioadă cuprinsă între 8 și 14 zile de incapacitate temporară de muncă;
- **OUG 158/2005 art. 17 alin. (1)** — `oug_158_2005_consolidat#art17/alin1` · valabil din nedovedit
  > Cuantumul brut lunar al indemnizației pentru incapacitate temporară de muncă cauzată de boli obișnuite sau de accidente în afara muncii se determină raportat la fiecare episod de boală, după cum urmează:
- **OUG 91/2025 art. II alin. (1)** — `oug_91_2025#artII~2/alin1` · valabil din nedovedit
  > Pentru certificatele de concediu medical eliberate în perioada 1 februarie 2026-31 decembrie 2027, indemnizațiile de asigurări sociale de sănătate prevăzute prin Ordonanța de urgență a Guvernului nr. 158/2005
- **OUG 91/2025 art. II alin. (1)** — `oug_91_2025#artII~2/alin1` · valabil din nedovedit
  > se calculează și se plătesc prin diminuarea cu o zi și se suportă după cum urmează: a) de către angajator, din a 2-a zi până inclusiv în a 6-a zi de incapacitate temporară de muncă, în cazul indemnizațiilor pentru incapacitate temporară de muncă
- **OUG 91/2025 art. II alin. (1) lit. b)** — `oug_91_2025#artII~2/alin1/litb` · valabil din nedovedit
  > din bugetul Fondului național unic de asigurări sociale de sănătate, începând cu: (i) ziua următoare celor suportate de angajator, conform lit. a) , și până la data încetării incapacității temporare de muncă a asiguratului sau a pensionării acestuia;
- derogare tratată: `oug_158_2005_consolidat#art12` — Regula generală (angajatorul suportă din prima zi până în a 5-a zi) este înlăturată pentru cazul dat de norma tranzitorie din art. II al OUG 91/2025 (astfel cum a fost modificat prin Legea nr. 64/2026), aplicabilă certificatelor eliberate în perioada 1 februarie 2026-31 decembrie 2027: diminuare cu …
- derogare tratată: `oug_158_2005_consolidat#art17/alin1^1` — Nu se aplică: procentul de 75% de la art. 17 alin. (1^1) vizează bolile cardiovasculare stabilite în condițiile art. 13 alin. (3) lit. a), nu boala obișnuită cod 01.
- derogare tratată: `oug_158_2005_consolidat#art17/alin2` — Nu se aplică: vizează incapacitatea determinată de tuberculoză, SIDA, neoplazii, boli infectocontagioase din grupa A, urgențe medico-chirurgicale, situații care nu sunt cele din întrebare.
- derogare tratată: `oug_158_2005_consolidat#art17/alin1/litc` — Nu se aplică: procentul de 75% este pentru certificate eliberate pentru o perioadă de peste 15 zile, iar certificatul din caz este de 10 zile.

### Navigarea (12 pași, 9 ture)

1. `cauta` {"interogare": "cuantumul brut lunar al indemnizației pentru incapacitate temporară de muncă din baza de calcul"}
2. `cuprins` {"act": "oug_158_2005_consolidat", "filtru": "incapacitate temporară de muncă"}
3. `deschide` {"id": "oug_158_2005_consolidat#art17/alin1"}
4. `deschide` {"id": "oug_158_2005_consolidat#art17/alin1/litb"}
5. `deschide` {"id": "oug_158_2005_consolidat#art17/alin1/litc"}
6. `cauta` {"interogare": "indemnizația pentru incapacitate temporară de muncă se suportă de angajator primele zile din bugetul Fondului național unic de asigurări sociale de sănătate"}
7. `deschide` {"id": "oug_158_2005_consolidat#art12"}
8. `deschide` {"id": "oug_158_2005_consolidat#art51/alin6/litb"}
9. `deschide` {"id": "oug_91_2025#artII~2/alin1/litb"}
10. `deschide` {"id": "oug_158_2005_consolidat#art51/alin6"}
11. `cuprins` {"act": "oug_91_2025", "filtru": "procent"}
12. `deschide` {"id": "oug_91_2025#artII~2/alin1"}

Apel: `claude-opus-5`, {'intrare': 18, 'iesire': 5311, 'cache_scriere': 8656, 'cache_citire': 95154} tokeni, $0.2345, 77 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond CORECT

> Indemnizația se calculează prin aplicarea procentului de 65% asupra bazei de calcul (certificat eliberat pentru o perioadă cuprinsă între 8 și 14 zile). Suportarea: angajatorul plătește din prima zi până în a 5-a zi de incapacitate, iar restul zilelor (din ziua următoare celor suportate de angajator până la încetarea incapacității) se suportă din bugetul Fondului național unic de asigurări sociale de sănătate.

## Cheia

- 65% din baza de calcul (episod de 8-14 zile). Pentru certificatele eliberate 01.02.2026–31.12.2027 prima zi a episodului nu se plătește (diminuare cu o zi); angajatorul suportă zilele 2-6, FNUASS din ziua a 7-a.
- temei: OUG 158/2005 art. 17 alin. (1) lit. b); OUG 91/2025 art. II alin. (1) și (1^1), modificat de Legea 64/2026; Norme OMS 15/2018 art. 78^4 (Ordinul 506/1030/2026)
