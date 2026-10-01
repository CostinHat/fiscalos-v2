# Urmărirea legilor pentru iConta (punctul 8) — raport

**ZIP:** `/home/costin/ghid_incoming/fiscalos_urmarire_rezultat.zip`

## 0. CERINȚE

Deciziile arhitectului pentru acest pas (punctul 8, așa cum au fost date):

- **8a.** Verificarea rulează săptămânal și automat. Pe portalul oficial se verifică dacă actele din corpus au o formă consolidată nouă; cele schimbate se aduc, se atomizează și trec prin detectorul de structură.
- **8b.** Parametrii iConta se recompară, numai din HEAD, cu forma nouă. La orice DIFERĂ sau temei schimbat se generează propunerea următoare, cu aprobare umană, niciodată aplicată.
- **8c.** Rezultatul fiecărei verificări apare pe pagina de la punctul 7, cu data verificării.
- **8d.** Probă:
  - o modificare de lege simulată într-o copie de test (o cotă schimbată) apare ca DIFERĂ în propunere;
  - o săptămână fără schimbări dă „nimic schimbat".
- **9.** Pentru ZIP: calea exactă, duratele și costul măsurate, cerințele în această secțiune.

Cum am citit cerințele (de confirmat de arhitect):

- **„Orice DIFERĂ" = DIFERĂ nou sau schimbat față de comparația anterioară.**
  - Potrivirea curentă are deja 1 DIFERĂ (`nomenclator/d394.TIPURI`, C9), aprobat ca atare.
  - Dacă orice DIFERĂ ar declanșa o propunere, ar ieși o propunere nouă în fiecare săptămână, fără nimic nou. Un DIFERĂ existent se redeclanșează numai dacă se schimbă valoarea legii sau atomul.
- **„Temei schimbat" = alt atom sau alt text al aceluiași atom**, pentru orice parametru, inclusiv NEVERIFICAT.
  - În proba B, temeiul candidat al constantelor nesursate D101 s-a mutat de pe art. 17 pe un exemplu din normele Codului fiscal („Impozit pe profit (16% x rd. 1)"), care încă spune 16%.
  - Exact asta trebuie să vadă un om: o constantă care „concordă" pe un exemplu vechi, deși legea s-a schimbat.
- **„Actele din corpus" = cele 61 de acte ale stratului oficial**, singurele care au id de portal.
  - Actele care există numai în instantaneul iConta, fără id de portal, nu se pot urmări aici.
  - Ele se schimbă când iConta își actualizează `anaf_surse`; atunci le preia instantaneul, nu urmărirea.
- **iConta se recompară și când legea nu s-a schimbat**, dacă HEAD-ul iConta s-a mutat de la ultima comparație. Altfel, un DIFERĂ introdus de iConta ar aștepta până la următoarea lege nouă.

Cerințe noi, care așteaptă decizia arhitectului:

- **C63 (propusă) — cine comite rezultatele săptămânale.**
  - Cron-ul scrie în depozit: stratul oficial, atomii, inventarul, potrivirea, propunerea și `urmarire/rezultate/`. Nu comite și nu publică.
  - Pagina le arată imediat.
  - Propunere: commit la aprobarea umană a propunerii, nu automat. Un `git push` automat ar publica fără om.
- **Probele înghețate pe starea iConta se strică atunci când iConta se schimbă legitim.**
  - `test_registrul_cote_e_inventariat_intreg` aștepta 20 de chei și 35 de intrări. iConta HEAD 663fb90 a adăugat `chirie_pf_forfait` și `chirie_pf_impozit`, iar urmărirea le-a găsit.
  - Am actualizat proba la 22 de chei și 37 de intrări, cu motivul scris în ea.
  - Altă lege nouă poate strica alte probe înghețate pe text. Asta e un semnal, nu o eroare. Trebuie hotărât dacă probele se refac la aprobarea fiecărei propuneri.
- **Portalul cade uneori pe timeout.** La a doua verificare reală au căzut 2 acte din 61. Am adăugat o reluare, o singură dată, după 30 s. Un act care cade și la reluare rămâne **NEVERIFICAT**, nu „neschimbat", conform regulii 5: tăcerea nu se citește ca absență.

## 1. Cum funcționează

`fiscalos/urmarire.py` rulează din cron în fiecare luni la 06:00 și scrie în `urmarire/jurnal.log`:

1. **Portalul.** Pentru fiecare din cele 61 de acte din `surse_oficiale/MANIFEST.json`, cere pagina actului (cu pauză de 2 s între cereri) și citește „Consolidarea din …" curentă.
   - O dată diferită de cea din manifest înseamnă o formă nouă.
   - Un act care nu răspunde se reia o singură dată; dacă tot nu răspunde, e NEVERIFICAT.
2. **Forma nouă.**
   - Actul se aduce din nou cu același cod ca la C12 și C31 (inclusiv trimiterile `S_REF`); celelalte acte din manifest rămân neatinse.
   - Se atomizează stratul oficial și trece detectorul de structură (S1–S4). Rezultatul detectorului apare în verificare.
3. **iConta.**
   - Inventarul se reface numai din git HEAD (`iconta_head`, numai citire), iar potrivirea se reface pe corpusul nou.
   - Comparația cu potrivirea anterioară dă DIFERĂ noi sau schimbați, temeiuri schimbate și parametri apăruți sau dispăruți.
4. **Propunerea.**
   - La un DIFERĂ nou sau schimbat, ori la un temei schimbat, se generează `propuneri/vN+1`, NEAPROBATĂ.
   - Pe lângă fișierele obișnuite, conține `SCHIMBARI_URMARIRE.json` și o secțiune în `RAPORT.md`. Fiecare rând are ambele părți: valoarea din codul iConta (fișier:linie) și textul legii verbatim, cu atomul, plus „înainte", dacă temeiul s-a schimbat.
5. **Rezultatul.**
   - Fiecare verificare scrie `urmarire/rezultate/<data>.json`.
   - Pagina de întrebări (secțiunea **Urmărirea legilor**) arată, pentru fiecare: data verificării, rezumatul și detaliile.
   - Pagina își reîncarcă singură corpusul după o formă nouă, dacă nicio întrebare nu e în lucru.

## 2. Proba (8d), în copia de test

`python -m fiscalos.urmarire_proba <dir>` face o copie a proiectului și rulează acolo. Rulează cu un **portal simulat**, care servește exact octeții paginilor deja aduse; în varianta B, servește pagina Codului fiscal cu o modificare. Depozitul real nu se atinge: proba verifică `git status` pe `surse_oficiale/`, `artefacte/` și `propuneri/`.

| Rulare | Ce simulează | Rezultat |
|---|---|---|
| A0 | prima verificare (preia starea curentă a iConta) | nimic schimbat — toate cele 61 de acte verificate, nicio formă nouă |
| **A** | **o săptămână fără schimbări** | **„nimic schimbat — toate cele 61 acte verificate pe portal, nicio formă consolidată nouă."** Nicio propunere. |
| **B** | **Codul fiscal art. 17: „este de 16%" → „este de 18%", consolidare nouă 01.10.2026** | **DIFERĂ în `propuneri/v10` (NEAPROBATĂ)** |

Rândul B din propunerea simulată (`urmarire/proba/propunere_simulata_v10/`):

| Parametru | Ce | iConta (cod) | Legea | Atom | Text verbatim |
|---|---|---|---|---|---|
| `cote/impozit_profit@2018-01-01` | DIFERĂ nou / temei schimbat | 0.16 (`core/common.py:663`, registrul COTE) | 18 | `cod_fiscal_227_2015_consolidat#art17` | „Cota de impozit pe profit care se aplică asupra profitului impozabil este de 18%." |
| | înainte | | 16% | același atom | „… este de 16%." |

Detectorul de structură a trecut actul modificat curat. Verdictul probei: `A_nimic_schimbat: true`, `B_DIFERA_in_propunere: true`, `depozitul_real_neatins: true`.

**Prima rulare a probei** (înainte de A0) a dat la A „2 schimbări pentru iConta", nu „nimic schimbat". Motivul era real: HEAD-ul iConta se mutase de la 85a811f la 663fb90 față de ultimul inventar, cu 2 parametri noi, amândoi CONCORDĂ. Nu era DIFERĂ, deci nu s-a generat propunere. De aceea proba are acum A0: o săptămână „fără schimbări" are sens numai după ce starea curentă a fost preluată.

## 3. Primele verificări reale (legislatie.just.ro, 01.10.2026)

| Verificarea | Rezultat | Durată |
|---|---|---|
| 17:40:26 | **HG 1045/2018 (normele): consolidarea 15.09.2026 → 30.09.2026.** Adusă (noul text e la id 314229) și atomizată; detectorul a găsit-o curată. iConta HEAD 663fb90: 2 parametri noi (`cote/chirie_pf_forfait`, `cote/chirie_pf_impozit`), ambii CONCORDĂ pe art. 84^1 alin. (3) și (5) din Codul fiscal. **Niciun DIFERĂ, nicio propunere.** | 247 s (portal 216 s, aducere și atomizare 13 s, detector 4 s, iConta și potrivire 15 s) |
| 17:44:45 | nimic schimbat în 59 de acte; **2 NEVERIFICATE** (timeout la portal: Legea 30/2019, Legea 319/2006) | 514 s |
| 17:53:53 | **nimic schimbat — toate cele 61 de acte verificate**, nicio formă consolidată nouă | 521 s |

Rezumatul verificării de la 17:44:45 a fost scris cu formularea veche („nimic schimbat — 59 din 61"). Formularea a fost corectată după aceea („nimic schimbat **în cele 59 verificate (din 61)**"). Înregistrarea veche a rămas cum a fost scrisă.

Rezultatele reale sunt comise (b9ee80d): noua formă a HG 1045/2018, atomii ei, inventarul și potrivirea pe HEAD 663fb90.

## 4. Durate și cost măsurate

| Ce | Durată | Cost |
|---|---|---|
| Proba 8d (copie + A0 + A + B) | 29,1 s (B: 28,3 s; A0 și A: sub 0,2 s fiecare) | $0 |
| Verificare reală, fără schimbări | 514–521 s (aproape tot timpul e portalul: 61 de cereri cu pauză de 2 s, iar unele pagini sunt mari) | $0 |
| Verificare reală, cu o formă nouă | 247 s | $0 |
| Probe (`probe.py`) | — | 213 PASS / 0 FAIL (205 + 8 noi în `test_urmarire.py`) |

Urmărirea nu folosește API-ul Anthropic: **cost $0**.

## 5. Fișiere

- `fiscalos/urmarire.py` — verificarea săptămânală.
- `fiscalos/urmarire_proba.py` — proba în copia de test, cu portalul simulat.
- `fiscalos/test_urmarire.py` — 8 probe:
  - ce declanșează și ce nu;
  - DIFERĂ cu ambele părți;
  - temei mutat;
  - reluarea la timeout;
  - rezumatul onest la acte neverificate;
  - rezultatul comis al probei 8d.
- `fiscalos/portal.py` — `info_din_html` scos din `Portal.act`, aplicabil și paginilor deja aduse.
- `fiscalos/surse_oficiale.py` — `aduce(..., p=)`: clientul de portal se poate injecta.
- `fiscalos/pagina.py` — reîncarcă singură corpusul după o formă nouă.
- `fiscalos/test_potrivire.py` — registrul COTE la 22/37 (iConta HEAD 663fb90).
- `urmarire/rezultate/` — verificările reale.
- `urmarire/proba/` — `rezultat_proba.json` și `propunere_simulata_v10/` (marcată SIMULARE).
- crontab: o linie adăugată (`0 6 * * 1 … fiscalos.urmarire`). Cele 12 linii ale iConta au rămas identice la octet.
