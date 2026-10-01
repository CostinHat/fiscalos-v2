# Pagina de întrebări pentru Costin (punctul 7) — raport

**ZIP:** `/home/costin/ghid_incoming/fiscalos_pagina_rezultat.zip`

## 0. CERINȚE

Deciziile arhitectului pentru acest pas (punctul 7, așa cum au fost date):

- **7a.** Fluxul: Costin scrie întrebarea, motorul spune ce date lipsesc și cere completarea, apoi afișează întrebarea reformulată completă, pe care Costin o confirmă. Abia apoi vine răspunsul.
- **7b.** Răspunsul are forma unei povești:
  - întâi data de referință și perimetrul presupus;
  - apoi argumentul, cu fiecare text de lege citat verbatim (act, articol, alineat, forma consolidată și data ei);
  - calculul pas cu pas, unde există;
  - avertismentele;
  - abținerea cu motiv, dacă e cazul.
- **7c.** Fiecare întrebare se păstrează (text, dialog, răspuns, cost măsurat). Costul apare pe pagină.
- **7d.** Întrebările lui Costin nu se folosesc pentru reglaj. Se păstrează separat, ca material pentru un set viitor, după verificare independentă.
- **7e.** Raportul dă adresa, pașii de intrare pentru un utilizator netehnic de pe Windows și o probă pe 3 întrebări proprii, cu costul.
- **9.** Pentru fiecare ZIP: calea exactă, duratele și costul măsurate, cerințele în această secțiune.

Cerințe noi, care așteaptă decizia arhitectului (**nu sunt implementate**; reglajul motorului s-a închis la v11):

- **C61 (propusă) — C40 respinge limitele unei perioade citate din lege.**
  - Întrebarea 1 a probei a fost respinsă pentru că „1 august 2025" și „31 iulie 2026" nu vin din `termen_efectiv`.
  - Aceste date nu sunt termene calculate. Sunt capetele perioadei din Legea 141/2025 art. III alin. (1): „poate achiziționa în perioada 1 august 2025-31 iulie 2026 inclusiv", citat verbatim.
  - Tura de reparație (C58) nu le poate „calcula", pentru că nu e nimic de calculat.
  - Propunere: o dată care apare literal într-un fragment citat și e folosită ca limită de perioadă, nu ca termen de îndeplinit, trece de C40.
- **C62 (propusă, cosmetică) — anul afișat cu separator de mii în calcul.**
  - În textul calculului, anul apare ca „2.026": `termen_efectiv(data(25, 4, 2.026))`.
  - Rezultatul e corect (27.04.2026); doar afișarea operandului e greșită.
- **Publicarea paginii cere un administrator.** Contul `costin` nu are sudo, deci nu se pot face din FiscalOS:
  - înregistrarea DNS (`fiscalos.iconta.eu` nu există azi; verificat);
  - blocul nginx;
  - certificatul TLS.

  Configurația e pregătită în `pagina_nginx.conf`, cu cei 3 pași de urmat. Până atunci, pagina se deschide printr-un tunel SSH (vezi mai jos).
- **Pornirea fără sesiune deschisă.** Pe server, `linger` e oprit (fără sudo nu se poate porni un serviciu systemd de utilizator). Am folosit cron-ul utilizatorului:
  - `@reboot` plus o verificare la 5 minute, care repornește pagina dacă a căzut;
  - am doar adăugat 3 linii; cele 12 linii existente ale iConta au rămas identice la octet (SHA256 `50ac7ac8…` înainte și după).

## 1. Adresa

| Ce | Unde |
|---|---|
| Acum, prin tunel SSH | **http://localhost:8030** (pe calculatorul lui Costin, cât timp tunelul e deschis) |
| După pașii administratorului | **https://fiscalos.iconta.eu** |
| Pe server | `127.0.0.1:8030` — nu se vede din internet (porturile publice rămân 22, 80, 443, ale iConta) |

## 2. Cum intră Costin (Windows, pași simpli)

1. Apasă **Start**, scrie `PowerShell` și deschide aplicația. Windows 10 și 11 au comanda `ssh` inclusă.
2. Scrie exact rândul de mai jos și apasă Enter:

   ```
   ssh -L 8030:127.0.0.1:8030 costin@178.105.201.56
   ```

   La prima conectare răspunde `yes`, apoi dă parola (sau cheia) obișnuită a serverului. **Lasă fereastra deschisă** cât lucrezi pe pagină.
3. Deschide browserul (Chrome, Edge) la adresa **http://localhost:8030**.
4. **Parola paginii.**
   - Prima parola e generată de server și nu e scrisă nicăieri altundeva. O afli scriind, în fereastra PowerShell de la pasul 2:

     ```
     cat ~/.fiscalos/pagina_parola_initiala.txt
     ```

   - Ca s-o schimbi cu una aleasă de tine (cel puțin 10 caractere), scrie în aceeași fereastră:

     ```
     cd ~/fiscalos && venv/bin/python -m fiscalos.pagina --parola
     ```

     Parola nu apare pe ecran cât o scrii. După schimbare, fișierul cu parola inițială se șterge singur.
5. Scrie întrebarea și apasă **Trimite**. Pagina îți arată ce fapte lipsesc.
   - Completează ce știi. Ce lași gol, motorul tratează ca nespecificat.
   - Apasă **Mai departe**, citește întrebarea completă și corecteaz-o dacă e cazul.
   - Apasă **Confirm și cer răspunsul**. Răspunsul vine în 2–3 minute, iar pagina se reîmprospătează singură.
6. Dacă motorul spune că îi lipsesc fapte (INCOMPLET), apasă **Completez faptele cerute și reîntreb**.
7. La final, apasă **Ieșire**, apoi închide fereastra PowerShell.

După ce administratorul publică pagina, pașii 1–2 nu mai sunt necesari: Costin deschide direct https://fiscalos.iconta.eu.

## 3. Ce face pagina (cum e construită)

- **Program și pornire.**
  - `fiscalos/pagina.py` folosește numai biblioteca standard și ascultă pe `127.0.0.1:8030`.
  - Indexul corpusului se încarcă o singură dată, la pornire.
  - `pagina_porneste.sh` o pornește, iar cron-ul o repornește dacă a căzut.
- **Accesul.**
  - Un singur utilizator.
  - Parola se păstrează doar ca hash PBKDF2 (300.000 de iterații) în `~/.fiscalos/pagina.env`, cu mod 600.
  - Sesiunea folosește un cookie `HttpOnly; SameSite=Strict`, plus `Secure` sub https, și expiră după 12 ore.
  - Fiecare formular poartă un jeton anti-CSRF.
  - După 8 parole greșite în 15 minute, accesul de pe acel IP se blochează; în acest interval nici parola bună nu mai e primită.
  - Id-urile sunt validate (o cale ocolită, ca `../../etc/passwd`, e refuzată).
- **Pregătirea (7a).** Pregătirea face două apeluri `claude-opus-5` cu ieșire structurată:
  - „ce fapte lipsesc" (cel mult 4);
  - „întrebarea completă".

  Pasul acesta nu citește legea, deci are o interdicție mecanică: orice cifră care nu e în întrebarea lui Costin duce la o reîncercare, iar dacă rămâne, e marcată pe pagină (regula 5, vezi §5).
- **Răspunsul.**
  - Răspunsul îl dă motorul închis la v11 (`navigare.raspunde`), neschimbat, cu toate verificările lui.
  - O abținere INCOMPLET oferă continuarea: faptele cerute de motor *după* citirea legii devin noua completare.
- **Povestea (7b).** Pagina afișează, în ordine:
  1. data de referință și motivul ei, apoi perimetrul;
  2. răspunsul sau abținerea, cu motivul și faptele lipsă;
  3. textele de lege verbatim, fiecare cu temeiul (act, articol, alineat), forma consolidată și data ei, data intrării în vigoare și id-ul atomului;
  4. calculul pas cu pas, evaluat de cod, cu sursa fiecărui operand;
  5. avertismentele.

  La o propunere respinsă de verificare, textele sunt marcate „consultate, nu temei dovedit".
- **Păstrarea (7c) și separarea (7d).**
  - Fiecare întrebare e un fișier JSON în `pagina_date/intrebari_costin/`. Fișierul conține textul, dialogul cu ora fiecărui pas, răspunsul complet al motorului, costul pe etape și câmpul `folosire: NU se foloseste la reglaj`.
  - `pagina_date/` e în `.gitignore`.
  - Proba `test_7d_…` verifică mecanic că niciun alt modul nu numește acest director și nu importă pagina, deci motorul nu are cale spre întrebările lui Costin.
  - Atenție: fiind în afara git-ului, aceste fișiere există numai pe discul serverului.

## 4. Proba pe 3 întrebări proprii

Toate au trecut prin pagina reală (HTTP, intrare cu parolă, CSRF), cu un apel de control înainte ($0,0003; a trecut). Întrebările sunt ale mele și stau în `intrebari/pagina_proba/`, nu în dosarul lui Costin. Fiecare are JSON-ul și pagina HTML exact cum o vede el.

| # | Întrebarea (inițial) | Rezultat | Cost | Durata răspunsului |
|---|---|---|---|---|
| 1 | Ce cotă de TVA se aplică la vânzarea unei locuințe noi? | **NU_POT_RASPUNDE** — respinsă de C40 (falsă; vezi C61) | $0,5545 | 115 s |
| 2 | Până când trebuie depusă declarația unică pentru chiria încasată în 2025? | **RASPUNS:** 25.05.2026 | $0,5487 | 110 s |
| 3 | Cât impozit pe dividende reține o firmă la o distribuire de 10.000 lei? | **INCOMPLET** — cere data distribuirii (normă tranzitorie la art. 97 alin. (7)) | $0,5948 | 134 s |
| 3′ | aceeași întrebare, continuată cu faptele cerute | **RASPUNS:** 16% → 1.600 lei impozit, 8.400 lei net, virare până la 27.04.2026 | $0,6399 | 147 s |

Citirea pe fond a fiecăruia:

- **Întrebarea 1.**
  - Completarea a dat: livrare la 15.09.2026, 450.000 lei, 95 mp, persoană fizică, prima locuință.
  - Motorul a găsit textele decisive: art. 291 alin. (2) lit. l) CF și Legea 141/2025 art. III, cu perioada „1 august 2025-31 iulie 2026" și condiția „care nu poate depăși data de 31 iulie 2026".
  - Prima propunere a fost respinsă pentru cifra „2023", necitată. Tura de reparație a scris limitele perioadei, iar C40 le-a respins.
  - Abținerea e afișată cu motivul exact.
  - **Nu este o greșeală de fond, dar e o abținere evitabilă (C61).**
- **Întrebarea 2.**
  - Răspunsul: 25.05.2026, din art. 122 alin. (3) CF, prin `termen_efectiv(data(25, 5, 2026))`.
  - Verificat independent: 25.05.2026 e luni, deci nu se prelungește.
  - Motorul a explicat și de ce faptele lăsate goale (sistemul real, plafonul CASS) nu schimbă termenul.
- **Întrebarea 3 și continuarea ei.**
  - Abținerea e corectă: art. 97 alin. (7) are o notă tranzitorie, deci data distribuirii contează, nu doar data plății.
  - Prin continuare, motorul a primit faptul cerut: distribuire aprobată pe 20.02.2026, din profitul anului 2025.
  - Răspunsul: 16% citat din art. 97 alin. (7); calculul evaluat de cod (`10.000 × 16% = 1.600`, `10.000 − 1.600 = 8.400`); termenul `termen_efectiv(25.04.2026)` = 27.04.2026.
  - Verificat independent: 25.04.2026 cade sâmbătă, deci termenul trece pe luni 27.04.

Forma consolidată afișată la citatele din Codul fiscal: „oficial: legislatie.just.ro, forma consolidata din 08.08.2026".

### Prima iterație, respinsă de mine ($0,1189)

Prima versiune a pasului de pregătire a scris în motive și presupuneri **valori legale din memorie**: „5% / 8% / 10%", „1 august 2025", „ziua de 25", „5 camere".

Pasul acela nu citește corpusul, deci era o încălcare a regulii 5. A cerut și 7–9 fapte, prea multe pentru un utilizator.

Am corectat trei lucruri:

- promptul: cel mult 4 fapte, nicio valoare legală;
- verificarea mecanică `cifre_nesursate`, cu probă;
- avertismentul de pe pagină.

A doua iterație a ieșit curată: 0 cifre nesursate la toate 3, fără reîncercare. Cele 3 fișiere ale primei iterații sunt păstrate în `iteratia1_respinsa/`.

## 5. Durate și cost măsurate

| Etapă | Durată măsurată | Cost |
|---|---|---|
| Apelul de control | 1,5 s | $0,0003 |
| Pregătire, „ce lipsește" (iterația 1, respinsă) | 26–30 s / întrebare | $0,1189 (3 întrebări) |
| Pregătire, „ce lipsește" (iterația 2) | 11,4 s / întrebare | $0,0189–0,0237 |
| Reformulare | 5,7–7,9 s | $0,0098–0,0133 |
| Răspunsul motorului | 110–147 s | $0,514–0,627 |
| **Cost total al probei B7** | | **$2,4571** |
| Probe (`probe.py`) | ~7 min (măsurat la v11; nu recronometrat) | 205 PASS / 0 FAIL (197 + 8 noi, în `test_pagina.py`) |

Costul tipic al unei întrebări puse de Costin: **~$0,55–0,65**. Pregătirea înseamnă ~$0,035, restul e răspunsul.

## 6. Fișiere

- `fiscalos/pagina.py` — pagina.
- `fiscalos/test_pagina.py` — 8 probe:
  - 7d: nicio cale de la motor spre `pagina_date/`;
  - 7c: `pagina_date/` ignorat de git;
  - accesul fără sesiune;
  - parola greșită și limita de încercări;
  - cookie și CSRF;
  - id-urile cu cale ocolită;
  - povestea pe un răspuns real din setul 4;
  - regula 5 la pregătire.
- `pagina_porneste.sh` — pornire și repornire (din cron).
- `pagina_nginx.conf` — pentru administrator.
- `intrebari/pagina_proba/` — proba: 4 JSON + 4 HTML, plus prima iterație respinsă.
- Corecție minoră: în `intrebari/v11/RAPORT.md` scria „Probe: 196"; numărul real era 197.
