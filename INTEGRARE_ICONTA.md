# FiscalOS → iConta: predarea modulului de legislație

Pentru sesiunea Claude Code a iConta. FiscalOS v2 se închide odată cu această predare. Depozitul e `CostinHat/fiscalos-v2`, iar ZIP-ul de predare e la `/home/costin/ghid_incoming/fiscalos_predare_iconta.zip`.

## 0. CERINȚE

Deciziile arhitectului (Costin) la predare:

1. **C61, C62 nu se repară.** Motorul de întrebări e înghețat. Cele două apar mai jos (§4) ca defecte cunoscute.
2. **C63 — cine comite.** Rezultatele urmăririi se comit la **aprobarea umană** a fiecărei propuneri. Cron-ul nu comite și nu face push.
3. **Ce declanșează o propunere.** Numai un DIFERĂ **nou sau schimbat** ori un temei schimbat. Un DIFERĂ deja aprobat (azi: `nomenclator/d394.TIPURI`, C9) nu declanșează din nou.
4. **Probele înghețate pe starea iConta se refac la fiecare aprobare**, cu motivul scris în probă (exemplu: `test_registrul_cote_e_inventariat_intreg`, 20/35 → 22/37 pentru iConta HEAD 663fb90).
5. **Pagina de întrebări rămâne înghețată.** Nu se publică (fără DNS sau nginx), iar cron-ul care o pornea s-a dezactivat. Urmărirea săptămânală rămâne activă.
6. Acest document descrie:
   - ce intră în modul și ce rămâne în afară;
   - dependențele;
   - cum se rulează probele;
   - regula: **modulul nu apelează API-ul plătit**.
7. Commit, push și ZIP la calea de mai sus.

Regulile care se moștenesc de la FiscalOS (`CLAUDE.md`) și rămân valabile în iConta:

- **Nicio valoare inventată.** Ce nu e în corpus e NEGĂSIT. Fiecare CONCORDĂ sau DIFERĂ citează id-ul atomului și fragmentul verbatim. Fiecare DIFERĂ arată ambele părți (codul iConta și textul legii).
- **Un act neextractibil se raportează ca *neextractibil*, nu ca *negăsit*.** Un act pe care portalul nu-l dă e *NEVERIFICAT*, nu *neschimbat*.
- **Rezultatul e o PROPUNERE.**
  - Fiecare propunere e un pachet `propuneri/vN/` (JSON plus raport), NEAPROBAT.
  - **Nu se aplică niciodată automat în codul iConta.** Modulul nu are cale de scriere spre parametrii iConta; aplicarea e un pas uman, separat.
- **iConta se citește numai în starea comisă (git HEAD)**, prin `iconta_head.py` (`git cat-file`, `--no-optional-locks`). Modificările necomise nu există pentru modul.

## 1. Ce intră în modul

| Fișier | Rol |
|---|---|
| `fiscalos/corpus_snapshot.py` | Instantaneul `anaf_surse` din git HEAD al iConta, cu manifest SHA256 (`corpus_manifest.json`); păzește interdicția de scriere. |
| `fiscalos/strat_text.py` | Redare în text: `.txt` ca atare, `.html` → text, `.pdf` → `pdftotext`. Un act neextractibil primește un motiv. |
| `fiscalos/atomizare.py` | Atomizarea structurală: act → articol → alineat → literă/punct, anexe, note; id stabil, text verbatim, valabilitate din note. |
| `fiscalos/portal.py` | Clientul legislatie.just.ro (user-agent declarat, pauză de 2 s între cereri); `info_din_html` citește consolidarea curentă. |
| `fiscalos/surse_oficiale.py` | **Formele oficiale** (C12): consolidatele la zi, aduse de pe portal în stratul `surse_oficiale/`, cu manifest (data formei, SHA, URL), plus conversia portal → text. |
| `fiscalos/surse_oficiale_c31.py` | C31: actele stricate în instantaneu, căutate și aduse de pe portal. |
| `fiscalos/detector_structura.py` | **Detectorul de structură**: S1 alineate dublate, S2 acoperire, S3 articole imbricate, S4 articol înghițit de o notă. |
| `fiscalos/surse.py` | Ce e act normativ și ce nu (un formular sau un pliant nu e temei); actele modificatoare. |
| `fiscalos/relatii.py` | Relațiile între atomi (excepții, derogări, C17). |
| `fiscalos/iconta_head.py` | Citirea iConta din git HEAD (numai citire). |
| `fiscalos/inventar_iconta.py` | Inventarul parametrilor iConta, prin AST (fără import, fără bytecode scris în arborele iConta). |
| `fiscalos/potrivire.py` | **Potrivirea parametrilor**: CONCORDĂ, DIFERĂ, NEVERIFICAT sau NEGĂSIT, cu atom, verbatim, pereche de valabilitate și temeiuri candidate. |
| `fiscalos/banc_mutatii.py` | Dovada inversă: greșeli injectate în parametri, care **trebuie** să iasă DIFERĂ. |
| `fiscalos/propunere.py` | **Propunerile cu aprobare umană**: `propuneri/vN/` cu `propunere.json`, `RAPORT.md`, `APROBARE.md`, `temeiuri_candidate.json`, `cerinte_iconta.json`, `acte_aduse.json`. |
| `fiscalos/urmarire.py` | **Urmărirea săptămânală**: consolidare nouă pe portal → aducere, atomizare, detector → inventar din HEAD și potrivire → propunerea `vN+1` la un DIFERĂ nou sau schimbat ori la un temei schimbat. Rezultatul se scrie în `urmarire/rezultate/`. |
| `fiscalos/urmarire_proba.py` | Proba urmăririi într-o copie de test, cu portal simulat: o săptămână fără schimbări dă „nimic schimbat", o cotă schimbată dă DIFERĂ. |
| `ruleaza_tot.py` | Lanțul întreg, cu durate măsurate. |
| `probe.py` | Rulatorul probelor (fără pytest). `--integrare` rulează numai probele modulului. |

Date:

| Director | În git | Ce e |
|---|---|---|
| `surse_oficiale/` (62 MB) | da | HTML-urile oficiale, `MANIFEST.json` (61 de acte), `C31_rezolvare.json` |
| `artefacte/` (119 MB) | da | atomii (instantaneu și oficiali), inventarul iConta, potrivirile, rapoartele detectorului și ale bancului |
| `corpus/` (129 MB) | **nu** | instantaneul `anaf_surse`; se reface cu `corpus_snapshot.instantaneu()`. Proba durabilă e `corpus_manifest.json`. |
| `propuneri/v1..v9/` | da | propunerile; v1–v8 sunt înghețate prin probe |
| `urmarire/` | da (fără `jurnal.log`) | rezultatele verificărilor, proba 8d, raportul |

## 2. Fluxul de aprobare

1. Cron-ul (luni la 06:00, utilizatorul `costin`) rulează `cd /home/costin/fiscalos && venv/bin/python -m fiscalos.urmarire >> urmarire/jurnal.log 2>&1`.
2. Rezultatul e unul din trei:
   - **„nimic schimbat"**: nu se scrie nimic în afară de `urmarire/rezultate/<data>.json`;
   - **formă nouă sau iConta schimbat, fără DIFERĂ nou ori temei schimbat**: stratul oficial, atomii, inventarul și potrivirea se actualizează în arborele de lucru, fără propunere;
   - **DIFERĂ nou/schimbat sau temei schimbat**: se generează `propuneri/vN+1/` NEAPROBAT, cu `SCHIMBARI_URMARIRE.json` și o secțiune în `RAPORT.md`. Fiecare rând are ambele părți și, unde e cazul, „înainte".
3. **Omul** citește propunerea și completează `APROBARE.md`. **La aprobare** (C63):
   1. refaci probele înghețate pe starea iConta care au căzut, cu motivul scris în probă (decizia 4);
   2. rulezi `python3 probe.py --integrare` până la 0 FAIL;
   3. faci `git add` pe `surse_oficiale/ artefacte/ propuneri/vN+1 urmarire/rezultate/`, apoi commit și push.
4. Aplicarea unei schimbări în parametrii iConta e un commit separat, făcut de om în iConta. Modulul o va vedea la verificarea următoare, din HEAD.

Până la aprobare, arborele de lucru FiscalOS rămâne „murdar" cu rezultatele urmăririi. E voit: nimic nu ajunge în git sau pe GitHub fără om.

## 3. Regula: modulul NU apelează API-ul plătit

Modulul e determinist și local: portalul public, git și fișiere. Nu importă `anthropic`, nu citește `~/.fiscalos/api_keys.env` și nu încarcă motorul de întrebări. Regula e verificată mecanic în `fiscalos/test_integrare.py`:

- `test_modulul_nu_incarca_API_ul_platit_nici_motorul`: importă toate cele 16 module ale modulului într-un proces curat. Verifică că `anthropic`, `semantic`, `navigare`, `intrebari`, `pagina`, `comparatie` și `rulare_cu_reluare` **nu** apar în `sys.modules`.
- `test_modulul_nu_citeste_cheia_API`: niciun fișier al modulului nu conține `anthropic`, `api_keys`, `sk-ant` sau `ANTHROPIC_API_KEY`.
- `test_pagina_nu_mai_porneste_din_cron`: decizia 5.

Costul măsurat al urmăririi: **$0**.

## 4. Ce rămâne în afară (înghețat)

**Motorul de întrebări:**

- fișierele: `navigare.py`, `semantic.py`, `intrebari.py`, `comparatie.py` și versiunile `_comparatie_inainte_*`, `rulare_cu_reluare.py`, `masoara*.py`, `analiza_C57.py`, `ablatie_lexical.py`, `raport_*.py`;
- seturile și rapoartele lor, în `intrebari/`.

Motorul folosește API-ul plătit (`claude-opus-5`, cheia din `~/.fiscalos/api_keys.env`). A fost acceptat pe setul 4 (36/6/8, 2 greșeli de fond; `intrebari/set4/RAPORT.md`), iar reglajul lui s-a închis la v11.

**Pagina de întrebări:** `pagina.py`, `pagina_porneste.sh`, `pagina_nginx.conf`, `pagina_date/`.

- E oprită, nu pornește din cron și nu e publicată.
- Întrebările de probă și raportul sunt în `intrebari/pagina_proba/`.
- `pagina_date/` e gol; acolo ar fi stat întrebările lui Costin, care nu se folosesc la reglaj.

**Defecte cunoscute ale motorului, nereparate (decizia 1):**

- **C61 — C40 respinge limitele unei perioade citate din lege.**
  - O dată care apare verbatim într-un citat, ca margine de perioadă, este tratată ca termen de calculat. Exemplul: „poate achiziționa în perioada 1 august 2025-31 iulie 2026 inclusiv", din Legea 141/2025 art. III alin. (1).
  - Tura de reparație (C58) nu are ce calcula, iar răspunsul devine NU_POT_RASPUNDE.
  - Observat pe întrebarea despre TVA la locuința nouă (`intrebari/pagina_proba/20261001-171624-0ca7c1.json`).
  - Efect: o abținere evitabilă, nu un răspuns greșit.
- **C62 — anul afișat cu separator de mii în textul calculului.**
  - Exemplu: `termen_efectiv(data(25, 4, 2.026))`. Rezultatul e corect (27.04.2026); doar afișarea operandului e greșită.
  - Observat în `intrebari/pagina_proba/20261001-172054-1ddfa6.json`.
- Celelalte limite măsurate ale motorului sunt în `intrebari/set4/RAPORT.md` și `intrebari/v11/RAPORT.md`.

Modulul nu depinde de nimic din această listă (vezi §3). Dacă iConta nu preia motorul, aceste fișiere pot rămâne doar în depozitul FiscalOS.

## 5. Dependențe

- **Python 3.12** (testat cu 3.12.3), numai biblioteca standard pentru modul. `venv/` are și `anthropic` 1.8.0, dar acesta e folosit numai de motorul înghețat.
- **git**: citirea iConta din HEAD și probele de înghețare (`git diff` pe propunerile vechi).
- **`pdftotext`** (poppler-utils): actele PDF din `anaf_surse`.
- **Rețea spre `https://legislatie.just.ro`**:
  - user-agent `FiscalOS/2.0` (portalul refuză user-agent-ul implicit al lui curl);
  - o verificare înseamnă 61 de cereri cu pauză de 2 s și durează 4–9 minute;
  - timeout-urile se reiau o singură dată, iar ce rămâne căzut e NEVERIFICAT.
- **Căi scrise în cod** (de schimbat dacă modulul se mută):
  - `fiscalos/iconta_head.py:14` și `fiscalos/inventar_iconta.py:38` → `ICONTA = "/home/costin/iconta_nou"`;
  - `fiscalos/corpus_snapshot.py:22-23` → `SURSA` și prefixul interzis la scriere.
- **Cron**, utilizatorul `costin`: o singură linie FiscalOS, cea a urmăririi. Liniile iConta din crontab nu au fost atinse (SHA256 al primelor 12 linii neschimbat, `50ac7ac8…`).

## 6. Cum se rulează

```sh
cd /home/costin/fiscalos
python3 probe.py --integrare             # numai probele modulului: 101 PASS / 0 FAIL, ~1,5 min, $0
python3 probe.py                         # toate probele, inclusiv motorul și pagina: ~7 min, $0
python3 ruleaza_tot.py                   # lanțul întreg (instantaneu → atomi → inventar → potrivire → banc) + probe
venv/bin/python -m fiscalos.urmarire     # o verificare a legilor acum (4–9 min, $0)
venv/bin/python -m fiscalos.urmarire_proba /tmp/proba_urmarire   # proba 8d în copie de test (~30 s, $0)
python3 -m fiscalos.propunere            # regenerează propunerea curentă (VERSIUNE din propunere.py)
```

Probele modulului sunt `test_read_only`, `test_atomizare`, `test_potrivire`, `test_banc`, `test_decizii`, `test_c12_c17`, `test_urmarire` și `test_integrare`.

`test_c12_c17` conține și 3 probe de înghețare care ating livrabilele motorului (`intrebari/v2`, `v4`, `v6`; ultima înghețează și `propuneri/v7`) și una pentru verificarea mecanică `semantic.verifica`. Toate rulează local, fără API. Dacă motorul nu e preluat, ele se pot scoate, mai puțin partea despre `propuneri/v7`.

## 7. De știut înainte de mutare

- **Independența auditului.** FiscalOS a fost construit ca auditor *din afara* iConta: citește iConta numai din HEAD, nu scrie nimic acolo și nu are cale de scriere spre parametri. Dacă modulul intră în depozitul iConta, aceste garanții trebuie păstrate explicit. Altfel o propunere ar putea ajunge să se „verifice" pe codul pe care tocmai l-a schimbat.
  - Inventarul și potrivirea se fac tot pe un commit fixat (HEAD).
  - Propunerile rămân pachete separate, aprobate de om.
  - Nicio rutină a modulului nu modifică registrul COTE sau alți parametri.
- **Versiunea propunerii.**
  - `propunere.py` are `VERSIUNE = "v9"`, iar urmărirea o înlocuiește la rulare cu `max(propuneri/vN) + 1`.
  - Textul raportului propunerii spune încă „Versiunile anterioare v1–v8 rămân neatinse". La o propunere v10 sau mai nouă, fraza e depășită (cosmetic).
- **Stratul oficial schimbă și ce vede motorul.** O formă nouă adusă de urmărire intră în corpusul comun. Ultima adusă: HG 1045/2018, consolidarea 30.09.2026, comisă în b9ee80d.
- **Starea la predare:**
  - ultima verificare reală (01.10.2026 17:53:53): **nimic schimbat, toate cele 61 de acte verificate**;
  - iConta HEAD inventariat: `663fb906`;
  - potrivirea: 96 CONCORDĂ, 1 DIFERĂ (cel aprobat), 26 NEVERIFICAT, 26 NEGĂSIT.
