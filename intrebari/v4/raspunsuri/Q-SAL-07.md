# Q-SAL-07 — REGULA

**Întrebarea:** Salariat cu stagiu minim îndeplinit primește certificat de concediu medical pentru boală obișnuită (cod 01), eliberat pentru 10 zile, în 2026. Ce procent din baza de calcul și cine suportă indemnizația?

## Stratul de navigare (v4) — RĂSPUNS

*La 28.09.2026, pentru un salariat (asigurat în sistemul de asigurări sociale de sănătate, angajat cu contract de muncă) cu stagiu minim de cotizare îndeplinit, cu certificat de concediu medical pentru boală obișnuită (cod 01) eliberat pentru 10 zile, presupunând un singur episod de boală și că nu e vorba de o boală cu regim special (tuberculoză, neoplazii, urgențe medico-chirurgicale, boli cardiovasculare) și nici de măsura izolării.*

> **Indemnizația se calculează prin aplicarea procentului de 65% asupra bazei de calcul (certificat eliberat pentru o perioadă cuprinsă între 8 și 14 zile). Suportarea: angajatorul plătește din prima zi până în a 5-a zi de incapacitate, iar restul zilelor (din ziua următoare celor suportate de angajator până la încetarea incapacității) se suportă din bugetul Fondului național unic de asigurări sociale de sănătate.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **OUG 158/2005 art. 17 alin. (1) lit. b)** — `oug_158_2005_consolidat#art17/alin1/litb` · valabil din nedovedit
  > prin aplicarea procentului de 65% asupra bazei de calcul stabilite conform art. 10 pentru certificatele de concediu medical eliberate pentru o perioadă cuprinsă între 8 și 14 zile de incapacitate temporară de muncă;
- **OUG 158/2005 art. 17 alin. (1)** — `oug_158_2005_consolidat#art17/alin1` · valabil din nedovedit
  > Cuantumul brut lunar al indemnizației pentru incapacitate temporară de muncă cauzată de boli obișnuite sau de accidente în afara muncii se determină raportat la fiecare episod de boală, după cum urmează:
- **OUG 158/2005 art. 12** — `oug_158_2005_consolidat#art12` · valabil din 2020-08-03
  > Indemnizațiile pentru incapacitate temporară de muncă se suportă după cum urmează: A. de către angajator, din prima zi până în a 5-a zi de incapacitate temporară de muncă
- **OUG 158/2005 art. 12** — `oug_158_2005_consolidat#art12` · valabil din 2020-08-03
  > B. din bugetul Fondului național unic de asigurări sociale de sănătate, începând cu: a) ziua următoare celor suportate de angajator, conform lit. A , și până la data încetării incapacității temporare de muncă a asiguratului sau a pensionării acestuia;
- derogare tratată: `oug_158_2005_consolidat#art17/alin1^1` — Regula specială de 75% pentru bolile cardiovasculare stabilite în condițiile art. 13 alin. (3) lit. a) nu se aplică, întrebarea vizând boală obișnuită (cod 01).
- derogare tratată: `oug_158_2005_consolidat#art17/alin2` — Cuantumul special pentru tuberculoză, SIDA, neoplazii, boli infectocontagioase din grupa A și urgențe medico-chirurgicale nu se aplică, fiind vorba de boală obișnuită (cod 01).
- derogare tratată: `oug_158_2005_consolidat#art12` — Excepția privind indemnizațiile aferente certificatelor acordate persoanelor pentru care a fost instituită măsura izolării (Legea nr. 136/2020), suportate din prima zi din FNUASS, nu se aplică cazului.

### Navigarea (6 pași, 5 ture)

1. `cauta` {"interogare": "cuantumul brut lunar al indemnizației pentru incapacitate temporară de muncă procent baza de calcul"}
2. `cuprins` {"act": "oug_158_2005_consolidat", "filtru": "incapacitate temporară de muncă"}
3. `deschide` {"id": "oug_158_2005_consolidat#art17/alin1"}
4. `deschide` {"id": "oug_158_2005_consolidat#art17/alin1/litb"}
5. `cauta` {"interogare": "indemnizația pentru incapacitate temporară de muncă se suportă de angajator primele zile"}
6. `deschide` {"id": "oug_158_2005_consolidat#art12"}

Apel: `claude-opus-5`, {'intrare': 10, 'iesire': 2687, 'cache_scriere': 4814, 'cache_citire': 40954} tokeni, $0.1178, 42 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți nu conțin regula privind cine suportă indemnizația (angajator pentru primele zile, respectiv Fondul național unic de asigurări sociale de sănătate) — nu există în context niciun fragment din care să rezulte suportarea. În plus, atomul OUG 89/2025 art. VIII alin. (2) semnalează că art. VII (al cărui conținut nu se află printre atomi) se aplică de la 1 iulie 2026 indemnizațiilor pentru boli obișnuite, ceea ce face nesigură, pe baza contextului dat, și confirmare…

## Cheia

- 65% din baza de calcul (episod de 8-14 zile). Pentru certificatele eliberate 01.02.2026–31.12.2027 prima zi a episodului nu se plătește (diminuare cu o zi); angajatorul suportă zilele 2-6, FNUASS din ziua a 7-a.
- temei: OUG 158/2005 art. 17 alin. (1) lit. b); OUG 91/2025 art. II alin. (1) și (1^1), modificat de Legea 64/2026; Norme OMS 15/2018 art. 78^4 (Ordinul 506/1030/2026)
