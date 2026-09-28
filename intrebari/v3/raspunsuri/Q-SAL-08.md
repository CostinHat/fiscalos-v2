# Q-SAL-08 — CAPCANA

**Întrebarea:** Boală obișnuită (cod 01): certificat inițial 28–30.09.2026 (3 zile), prelungit fără întrerupere 01–07.10.2026 (7 zile). Septembrie a fost plătit cu 55%. Ce procent se aplică și cum se tratează luna septembrie?

## Stratul semantic — RĂSPUNS

*La data de referință 30.09.2026, presupun un asigurat în sistemul de asigurări sociale de sănătate, cu indemnizație pentru incapacitate temporară de muncă cauzată de boală obișnuită (cod 01), un singur episod de boală format dintr-un certificat inițial (28–30.09.2026) urmat fără întrerupere de un certificat în continuare (01–07.10.2026), fără spitalizare, iar certificatul inițial fiind eliberat sub regimul în vigoare la data de referință.*

> **Se aplică procentul de 65%, corespunzător perioadei cuprinse între 8 și 14 zile, deoarece zilele certificatului inițial se adună cu zilele certificatului eliberat în continuare în cadrul aceluiași episod de boală. Procentul rezultat se aplică zilelor aferente întregului episod, deci și zilelor din septembrie: luna septembrie, plătită cu 55%, se recalculează la 65%.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **OMS 15/2018 art. I** — `oms_15_2018_modificare_2025#artI` · valabil din nedovedit
  > Pe parcursul unui episod de boală, numărul de zile rezultat din certificatul de concediu medical inițial se adună cu numărul de zile rezultat din certificatul/certificatele de concediu medical acordat/acordate în continuare, iar în funcție de numărul de zile total rezultat se aplică asupra bazei de calcul procentul corespunzător pentru zilele aferente întregului episod de boală.
- **OUG 158/2005 art. 17 alin. (1) lit. b)** — `oug_158_2005_consolidat#art17/alin1/litb` · valabil din nedovedit
  > prin aplicarea procentului de 65% asupra bazei de calcul stabilite conform art. 10 pentru certificatele de concediu medical eliberate pentru o perioadă cuprinsă între 8 și 14 zile de incapacitate temporară de muncă;
- **OUG 158/2005 art. 17 alin. (1)** — `oug_158_2005_consolidat#art17/alin1` · valabil din nedovedit
  > prin aplicarea procentului de 55% asupra bazei de calcul stabilite conform art. 10 pentru certificatele de concediu medical eliberate pentru o perioadă de până la 7 zile de incapacitate temporară de muncă;
- **OMS 15/2018 art. I** — `oms_15_2018_modificare_2025#artI` · valabil din nedovedit
  > cuantumul brut lunar al indemnizației pentru incapacitate temporară de muncă cauzată de boli obișnuite sau de accidente în afara muncii se determină raportat la fiecare episod de boală și în funcție de totalul zilelor de concediu medical acordate pentru fiecare episod de boală.
- derogare tratată: `oug_158_2005_consolidat#art17/alin1/litc` — Procentul de 75% se aplică certificatelor eliberate pentru o perioadă de peste 15 zile; nu este cazul aici, întrucât episodul descris cumulează zilele celor două certificate sub acest prag, rămânând în intervalul între 8 și 14 zile.
- derogare tratată: `legea_141_2025_consolidat#artXI/alin1` — Regula tranzitorie privește episoadele al căror certificat inițial a fost eliberat până la intrarea în vigoare a art. IX; aici certificatul inițial este eliberat la 28.09.2026, ulterior, deci se aplică dispozițiile în vigoare la data de referință (inclusiv lit. c) valabilă din 2025-08-01).
- derogare tratată: `legea_141_2025#artXI/alin1` — Identic cu atomul precedent (variantă a aceluiași text): nu se aplică, certificatul inițial fiind eliberat după intrarea în vigoare a art. IX.
- derogare tratată: `oug_158_2005_consolidat#art51/alin1^1` — Regula diminuării cu o singură zi pentru întregul episod acordat fără întrerupere privește calculul și plata indemnizației, nu procentul aplicabil; nu modifică încadrarea procentuală solicitată.
- derogare tratată: `ordin_506_1030_2026_norme_oug158#artI/alin2^2` — Excepția privește bolnavii cu servicii medicale în regim de spitalizare; cazul descris este de boală obișnuită fără spitalizare, iar formula de calcul trimite oricum la procentele de 55%/65%/75% din art. 17 alin. (1).

Apel: `claude-opus-5`, {'intrare': 3788, 'iesire': 4378, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.1293

Pe fond: **GREȘIT** — faptul principal al cheii (['10 zile']) nu e in raspuns; articolul citat [('oms_15_2018', 'I')] nu e printre cele ale cheii [('oug_158_2005', '17'), ('oug_89_2025', '17'), ('oug_89_2025', 'VII')]

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-09-30 (zi, din "30.09.2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **Cuantumul brut lunar al indemnizației pentru incapacitate temporară de muncă cauzată de boli obișnuite sau de accidente în afara muncii se determină raportat la fiecare episod de boală, după cum urmează: a) prin aplicarea procentului de 55% asupra bazei de calcul stabilite conform art.**

Motiv: D15: fraza care conţine un fapt de forma cerută (procent) si potriveste cel mai bine intrebarea (scor local 16.9)

- **OUG 158/2005 art. 17 alin. (1)** — `oug_158_2005_consolidat#art17/alin1` · valabil din nedovedit
  > Cuantumul brut lunar al indemnizației pentru incapacitate temporară de muncă cauzată de boli obișnuite sau de accidente în afara muncii se determină raportat la fiecare episod de boală, după cum urmează: a) prin aplicarea procentului de 55% asupra bazei de calcul stabilite conform art. 10 pentru certificatele de concediu medical eliberate pentru o perioadă de până la 7 zile de incapacitate temporară de muncă; ...

Pe fond: **GREȘIT** — faptul principal al cheii (['10 zile']) nu e in raspuns

## Cheia

- Procentul se stabilește pe episodul de boală (10 zile) → 65% pentru tot episodul, inclusiv zilele din septembrie; diferența 55%→65% pentru septembrie se recalculează, se include în veniturile lunii octombrie 2026 și se declară în D112 pentru octombrie
- temei: OUG 158/2005 art. 17 alin. (1) partea introductivă („raportat la fiecare episod de boală”) și lit. b); art. 17 alin. (1^2) (introdus de OUG 89/2025 art. VII)
