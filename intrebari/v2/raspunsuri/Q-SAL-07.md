# Q-SAL-07 — REGULA

**Întrebarea:** Salariat cu stagiu minim îndeplinit primește certificat de concediu medical pentru boală obișnuită (cod 01), eliberat pentru 10 zile, în 2026. Ce procent din baza de calcul și cine suportă indemnizația?

## Stratul semantic (motorul nou) — NU POT RĂSPUNDE

*La data de referință 28.09.2026, presupun un salariat asigurat în sistemul concediilor și indemnizațiilor de asigurări sociale de sănătate (OUG 158/2005), cu stagiu de asigurare îndeplinit, care primește un certificat de concediu medical inițial pentru boală obișnuită (cod 01) pe 10 zile, fără spitalizare și fără alte certificate în continuare în cadrul aceluiași episod de boală.*

Motiv: modelul s-a abţinut: Întrebarea are două componente, iar atomii primiți nu acoperă ambele. (1) Suportarea indemnizației: niciun atom nu conține regula privind cine plătește indemnizația (angajator pentru primele zile / Fondul național unic de asigurări sociale de sănătate), deci nu pot indica plătitorul. (2) Procentul: deși art. 17 alin. (1) lit. b) prevede 65% pentru certificatele eliberate pentru 8-14 zile, un atom primit arată că prevederile art. VII din OUG 89/2025 intră în vigoare la 1 iulie 2026 și se aplică indemnizațiilor pentru incapacitate temporară de muncă cauzată de boli obișnuite…

- **OUG 158/2005 art. 17 alin. (1) lit. b)** — `oug_158_2005_consolidat#art17/alin1/litb` · valabil din nedovedit
  > prin aplicarea procentului de 65% asupra bazei de calcul stabilite conform art. 10 pentru certificatele de concediu medical eliberate pentru o perioadă cuprinsă între 8 și 14 zile de incapacitate temporară de muncă;
- **OUG 89/2025 art. VIII alin. (2)** — `oug_89_2025#artVIII/alin2` · valabil din nedovedit
  > Prevederile art. VII intră în vigoare la data de 1 iulie 2026 și se aplică inclusiv în cazul indemnizațiilor pentru incapacitate temporară de muncă cauzată de boli obișnuite sau de accidente în afara muncii aferente certificatelor de concediu medical eliberate

Apel: `claude-opus-5`, {'intrare': 4901, 'iesire': 1871, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0721, 30.3 s

Pe fond: **NU POT** — modelul s-a abţinut: Întrebarea are două componente, iar atomii primiți nu acoperă ambele. (1) Suportarea indemnizației: niciun atom nu conține regula privind cine plătește indemnizația (angajator pen

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **Cuantumul brut lunar al indemnizației pentru incapacitate temporară de muncă cauzată de boli obișnuite sau de accidente în afara muncii se determină raportat la fiecare episod de boală, după cum urmează: a) prin aplicarea procentului de 55% asupra bazei de calcul stabilite conform art.**

Motiv: D15: fraza care conţine un fapt de forma cerută (procent) si potriveste cel mai bine intrebarea (scor local 26.3)

- **OUG 158/2005 art. 17 alin. (1)** — `oug_158_2005_consolidat#art17/alin1` · valabil din nedovedit
  > Cuantumul brut lunar al indemnizației pentru incapacitate temporară de muncă cauzată de boli obișnuite sau de accidente în afara muncii se determină raportat la fiecare episod de boală, după cum urmează: a) prin aplicarea procentului de 55% asupra bazei de calcul stabilite conform art. 10 pentru certificatele de concediu medical eliberate pentru o perioadă de până la 7 zile de incapacitate temporară de muncă; ...

Pe fond: **GREȘIT** — faptul principal al cheii (['65%']) nu e in raspuns

## Cheia

- răspuns așteptat: 65% din baza de calcul (episod de 8-14 zile). Pentru certificatele eliberate 01.02.2026–31.12.2027 prima zi a episodului nu se plătește (diminuare cu o zi); angajatorul suportă zilele 2-6, FNUASS din ziua a 7-a.
- temei așteptat: OUG 158/2005 art. 17 alin. (1) lit. b); OUG 91/2025 art. II alin. (1) și (1^1), modificat de Legea 64/2026; Norme OMS 15/2018 art. 78^4 (Ordinul 506/1030/2026)

