# Q-CPF-07 — REGULA

**Întrebarea:** Care este durata maximă a unei inspecții fiscale la o microîntreprindere fără sedii secundare (nici contribuabil mijlociu/mare) și ce se întâmplă dacă inspecția depășește acest termen?

## Stratul semantic — RĂSPUNS

*La data de referință 28.09.2026, presupun o microîntreprindere persoană juridică română, contribuabil administrat de organul fiscal central, care nu este contribuabil mare și nici mijlociu și nu are sedii secundare, supusă unei inspecții fiscale obișnuite (nu inspecție la nerezidenți), fără a lua în calcul eventualele perioade de suspendare a inspecției.*

> **Durata inspecției fiscale nu poate fi mai mare de 45 de zile (categoria „ceilalți contribuabili”, alta decât contribuabilii mari, cei cu sedii secundare, nerezidenții sau contribuabilii mijlocii). Termenul poate fi însă afectat de perioadele în care inspecția este suspendată de conducătorul inspecției fiscale, în situațiile prevăzute de lege. Efectul juridic al depășirii acestei durate nu rezultă din fragmentele de act normativ puse la dispoziție, deci nu îl pot preciza.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul de procedură fiscală (Legea 207/2015) art. 126 alin. (1) lit. c)** — `legea_207_2015_consolidat#art126/alin1/litc` · valabil din nedovedit
  > 45 de zile pentru ceilalți contribuabili. ...
- **Codul de procedură fiscală (Legea 207/2015) art. 126 alin. (1)** — `legea_207_2015_consolidat#art126/alin1` · valabil din nedovedit
  > Durata efectuării inspecției fiscale este stabilită de organul de inspecție fiscală, în funcție de obiectivele inspecției, și nu poate fi mai mare de:
- **Codul de procedură fiscală (Legea 207/2015) art. 126 alin. (1) lit. a)** — `legea_207_2015_consolidat#art126/alin1/lita` · valabil din 2022-09-03
  > 180 de zile pentru contribuabilii mari, pentru contribuabilii/ plătitorii care au sedii secundare, indiferent de mărime, precum și pentru contribuabilii nerezidenți; ...
- **Codul de procedură fiscală (Legea 207/2015) art. 126 alin. (1) lit. b)** — `legea_207_2015_consolidat#art126/alin1/litb` · valabil din nedovedit
  > 90 de zile pentru contribuabilii mijlocii; ...
- **Codul de procedură fiscală (Legea 207/2015) art. 127 alin. (1)** — `legea_207_2015_consolidat#art127/alin1` · valabil din nedovedit
  > Conducătorul inspecției fiscale competent poate decide suspendarea unei inspecții fiscale în oricare din următoarele situații și numai dacă apariția acestei situații împiedică finalizarea inspecției fiscale:
- derogare tratată: `legea_207_2015_consolidat#art119/alin2` — Derogă de la art. 30 privind competența teritorială de administrare, nu de la art. 126 privind durata inspecției; nu influențează durata maximă din cazul de față.
- derogare tratată: `legea_207_2015_consolidat#art34/alin1` — Derogă de la art. 30 și 38 privind plata impozitului pe venituri din activități agricole de către persoane fizice; nu se aplică unei microîntreprinderi și nu afectează durata inspecției fiscale.

Apel: `claude-opus-5`, {'intrare': 3392, 'iesire': 2330, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0762

Pe fond: **CORECT** — faptul principal si articolul coincid

## Motorul lexical — RĂSPUNS

*Data de referinta: 2026-09-28 (implicita (ziua intrebarii)). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

> **Contribuabilul/Plătitorul are obligația de a declara organului fiscal central, înființarea de sedii secundare, în termen de 30 de zile de la:**

Motiv: D15: fraza care conţine un fapt de forma cerută (termen) si potriveste cel mai bine intrebarea (scor local 17.8)

- **Codul de procedură fiscală (Legea 207/2015) art. 85 alin. (1)** — `legea_207_2015_consolidat#art85/alin1` · valabil din nedovedit
  > Contribuabilul/Plătitorul are obligația de a declara organului fiscal central, înființarea de sedii secundare, în termen de 30 de zile de la:

Pe fond: **GREȘIT** — faptul principal al cheii (['45 zile']) nu e in raspuns; articolul citat [('cpf', '85')] nu e printre cele ale cheii [('cpf', '126')]

## Cheia

- Maximum 45 de zile. Dacă nu se finalizează în dublul perioadei (90 de zile, fără perioadele de suspendare legală), inspecția încetează fără raport și fără decizie de impunere; poate fi reluată o singură dată, cu aprobarea organului ierarhic superior; suspendarea prescripției pe durata inspecției nu mai operează.
- temei: Legea 207/2015 art. 126 alin. (1) lit. c), (2) și (3)
