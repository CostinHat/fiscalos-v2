# Q-SAL-08 — CAPCANA

**Întrebarea:** Boală obișnuită (cod 01): certificat inițial 28–30.09.2026 (3 zile), prelungit fără întrerupere 01–07.10.2026 (7 zile). Septembrie a fost plătit cu 55%. Ce procent se aplică și cum se tratează luna septembrie?

## Stratul semantic (motorul nou) — NU POT RĂSPUNDE

*La data de referință 30.09.2026, presupun un salariat asigurat în sistemul OUG 158/2005, cu indemnizație pentru incapacitate temporară de muncă pentru boală obișnuită (cod 01), într-un singur episod de boală format din certificatul inițial 28–30.09.2026 și certificatul în continuare, fără întrerupere, 01–07.10.2026, plătit de angajator/FNUASS.*

Motiv: modelul s-a abţinut: Atomii arată că procentul se stabilește în funcție de totalul zilelor din episodul de boală, dar stabilirea încadrării în tranșa de zile ar presupune adunarea celor 3 zile cu cele 7 zile, iar rezultatul acestui calcul nu apare literal în niciun atom. În plus, regula privind tratamentul lunii septembrie (modul de regularizare/recalculare a indemnizației deja plătite cu 55% atunci când certificatul inițial se acordă la sfârșitul lunii și este urmat de un certificat în continuare în luna următoare) este cuprinsă într-un fragment trunchiat exact în acel punct („indemnizația pe…

- **OMS 15/2018 art. I** — `oms_15_2018_modificare_2025#artI` · valabil din nedovedit
  > Pe parcursul unui episod de boală, numărul de zile rezultat din certificatul de concediu medical inițial se adună cu numărul de zile rezultat din certificatul/certificatele de concediu medical acordat/acordate în continuare
- **OUG 158/2005 art. 17 alin. (1) lit. b)** — `oug_158_2005_consolidat#art17/alin1/litb` · valabil din nedovedit
  > prin aplicarea procentului de 65% asupra bazei de calcul stabilite conform art. 10 pentru certificatele de concediu medical eliberate pentru o perioadă cuprinsă între 8 și 14 zile de incapacitate temporară de muncă;

Apel: `claude-opus-5`, {'intrare': 4098, 'iesire': 2036, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0722, 30.7 s

Pe fond: **NU POT** — modelul s-a abţinut: Atomii arată că procentul se stabilește în funcție de totalul zilelor din episodul de boală, dar stabilirea încadrării în tranșa de zile ar presupune adunarea celor 3 zile cu cele

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-09-30 (zi, din "30.09.2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **Cuantumul brut lunar al indemnizației pentru incapacitate temporară de muncă cauzată de boli obișnuite sau de accidente în afara muncii se determină raportat la fiecare episod de boală, după cum urmează: a) prin aplicarea procentului de 55% asupra bazei de calcul stabilite conform art.**

Motiv: D15: fraza care conţine un fapt de forma cerută (procent) si potriveste cel mai bine intrebarea (scor local 16.7)

- **OUG 158/2005 art. 17 alin. (1)** — `oug_158_2005_consolidat#art17/alin1` · valabil din nedovedit
  > Cuantumul brut lunar al indemnizației pentru incapacitate temporară de muncă cauzată de boli obișnuite sau de accidente în afara muncii se determină raportat la fiecare episod de boală, după cum urmează: a) prin aplicarea procentului de 55% asupra bazei de calcul stabilite conform art. 10 pentru certificatele de concediu medical eliberate pentru o perioadă de până la 7 zile de incapacitate temporară de muncă; ...

Pe fond: **GREȘIT** — faptul principal al cheii (['10 zile']) nu e in raspuns

## Cheia

- răspuns așteptat: Procentul se stabilește pe episodul de boală (10 zile) → 65% pentru tot episodul, inclusiv zilele din septembrie; diferența 55%→65% pentru septembrie se recalculează, se include în veniturile lunii octombrie 2026 și se declară în D112 pentru octombrie
- temei așteptat: OUG 158/2005 art. 17 alin. (1) partea introductivă („raportat la fiecare episod de boală”) și lit. b); art. 17 alin. (1^2) (introdus de OUG 89/2025 art. VII)

