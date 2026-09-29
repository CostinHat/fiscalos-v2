# FiscalOS v2 — Pasul 10: deciziile C49–C53

Generat 29.09.2026 22:07 · ZIP: `/home/costin/ghid_incoming/fiscalos_v9_rezultat.zip`

> Fără rulare plătită (decizia 6). Efectele C49–C51 măsurate pe propunerile salvate ale seturilor 2 și 3, fără niciun apel; C52 cere modelul și se măsoară pe setul 4; C53 (costul) — pe setul 4.

## Corecție la raportul setului 3

Am scris acolo că la Q3-SAL-07 „geamănul nejustificat era exact perechea HG 146/2026 art. 1 / art. 2” și că C41 „a prevenit o greșeală de fond”. **Fals.** Art. 2 al HG 146/2026 e blocul de semnături, nu o altă valoare a salariului minim. Greșeala de fond a propunerii (salariul minim de 4.325 lei, în vigoare de la 01.07.2026, în locul celui de 4.050 lei, în vigoare la 01.01.2026) nu vine dintr-un geamăn, ci din data de valabilitate a valorii; respingerea C41 a fost **întâmplătoare** (alți geameni, fără legătură cu greșeala). Bilanțul corect al C47 pe setul 3: C41 nu a prevenit nicio greșeală de fond și a pierdut 9 răspunsuri corecte.

## 0. CERINȚE — decizii de arhitect, aplicate

| | Decizia | Cum e aplicată | Dovada |
|---|---|---|---|
| **C49** | justificarea geamănului numai pentru atomul decisiv (cel din care vine faptul principal) | *faptul principal* = prima valoare cu unitate din răspuns (procent, sumă, durată, dată) care nu e fapt al cazului; *atomul decisiv* = sursa ei (operanzii legali ai calculului care o produce, cu valoarea operandului ca ancoră, sau citatul care o conține); fără valoare → primul citat (C14). Un geamăn contează numai dacă textul comun **înconjoară ancora** (același șablon în jurul valorii); un geamăn citat și el e folosit, nu înlocuit | `test_navigare.test_C49_*` (3) |
| **C50** | respinsă împărțirea la 100 a unui operand deja scris cu „%” | regulă pe arborele formulei; promptul spune că „21%” valorează 0,21 | `test_navigare.test_C50_*`: Q3-TVA-09 (propunerea salvată) respins; formula corectă trece |
| **C51** | ordinalele și „cifră + unitate” sunt operanzi, conversia declarată | „15-a”, „a 15-a”, „60 de zile”, „5 ani” → cifra; calculul afișează conversia | `test_navigare.test_C51_*` |
| **C52** | cel mult o tură automată de reparație, care arată cifrele respinse; totul trece prin aceeași verificare | declanșată numai de respingerile C13/C46 (cifre); verificarea reluată integral (`verifica_propunerea`); rezultatul în `reparatie_C52` | `test_navigare.test_C52_*` (client simulat) |
| **C53** | costul se măsoară după 1–4; țintă < $0,20/întrebare | nemăsurabil fără rulare (decizia 6) — vezi mai jos | — |

## Efectul C49–C51 pe propunerile salvate (re-notare; scorurile oficiale nu se schimbă)

| Set | Scor oficial | Comparatorul de acum (C42) | Verificarea de acum (C49–C51) |
|---|---|---|---|
| Setul 3 | 18/1/31 | 18/1/31 | **24/1/25** |
| Setul 2 | 28/7/15 | 30/5/15 | 18/3/29 |

**Setul 3**, schimbările:

- Q3-TVA-01: NU_POT → CORECT — propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale
- Q3-TVA-02: NU_POT → CORECT — propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale
- Q3-TVA-09: GRESIT → NU_POT — VERIFICAREA CALCULULUI a respins propunerea: C50: calculul tva imparte la 100 un operand scris cu % (cota), care valoreaza deja fractiunea
- Q3-PRF-02: NU_POT → CORECT — propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale
- Q3-SAL-02: NU_POT → CORECT — propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale
- Q3-CTB-01: NU_POT → CORECT — propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale
- Q3-CTB-03: NU_POT → CORECT — propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale
- Q3-CTB-09: NU_POT → GRESIT — propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

Din cele 9 răspunsuri corecte pierdute de C41 pe setul 3, **5 trec acum** (Q3-TVA-01, PRF-02, SAL-02, CTB-01, CTB-03); Q3-TVA-02 trece prin C51; Q3-TVA-09 (singura greșeală de fond) e **prins** de C50; Q3-CTB-09 devine GREȘIT numai pe articol (concluzia e a cheii, temeiul CF art. 29 în loc de OMFP 1802/2014). **Criteriul arhitectului nu e îndeplinit întreg** — 4 dintre cele 9 rămân respinse, fiecare cu motiv:

- **Q3-PRF-09** — C40, nu C41: „25 decembrie 2026” scris direct, mutat de model fără `termen_efectiv`. C49 nu-l atinge.
- **Q3-TVA-05** — geamănul art. 315^1 alin. (16) e relevant (același șablon „până la data de 25 a lunii următoare…”), iar „condiția” dată de model e chiar textul comun, deci nu deosebește nimic — verificarea procedează corect.
- **Q3-SAL-08** — geamănul art. 147 alin. (18) față de art. 138/156 (aceeași formulare a cotei, alt subiect), nejustificat.
- **Q3-PRF-04** — răspuns fără valoare (30.000 lei e fapt al cazului), deci atomul decisiv e primul citat, cu 8 geameni cu definiții comune.

Ca să treacă și acestea ar trebui fie relaxat C40, fie C41 transformat în avertisment (varianta (c) din C49) — nu am făcut-o: ar fi reglaj pe setul 3. Q3-SAL-07 rămâne respins, dar — vezi corecția — din motive fără legătură cu greșeala lui. **Setul 2** scade (18/3/29) numai pentru că propunerile lui nu aveau câmpul `alegeri_temei` și nici regula C40 în prompt; nu e o măsură a versiunii de acum.

## C53 — costul

Nu se poate măsura fără rulare (decizia 6). Ce se știe: C49–C51 nu schimbă navigarea (geamenii se arată în continuare la fiecare `deschide`, cum a cerut C41), deci costul de bază rămâne cel al setului 3 (**$0,310/întrebare**); C52 adaugă cel mult o tură, numai la întrebările respinse pentru cifre (pe setul 3: 9 din 50). **Ținta de $0,20 nu va fi atinsă fără o schimbare de navigare** — de decis mai jos.

## De decis

**C54 — Costul: geamenii arătați la fiecare `deschide`.** După C49, justificarea se cere numai pentru atomul decisiv, dar textul geamenilor se trimite pentru fiecare atom deschis (în medie 6,7 deschideri pe întrebare pe setul 3). *De decis:* `deschide` arată numai id-ul și temeiul geamenilor (fără începutul textului), iar modelul îi deschide dacă îi trebuie — sau geamenii nu se mai arată la navigare, ci numai în tura de reparație (C52 extins la C41), pentru atomul decisiv.

**C55 — Valoarea luată cu data greșită (Q3-SAL-07).** Clasa reală a greșelii: o valoare legală validă de la o dată (HG 146/2026: 4.325 lei de la 01.07.2026) folosită pentru un fapt care cere valoarea de la altă dată (CASS pe 2026: salariul minim la 01.01.2026). Nici C27 (data întrebării), nici C41 nu o prind. *De decis:* operanzii VALOARE_LEGALA poartă data de la care e valabilă valoarea (din nota atomului sau din textul lui, „începând cu data de…”), iar calculul o declară, ca să se vadă nepotrivirea cu data faptului?

**Proba `test_read_only.test_fisierele_citite_din_iconta_sunt_neatinse` pică** — și trebuie să pice: `~/iconta_nou/core/common.py` are o modificare **necomisă** din 29.09.2026 21:55 (+14 rânduri: `CHIRIE_PF`, CF art. 84^1, `de_cine="Code/Costin"`), făcută în iConta, nu de FiscalOS (FiscalOS nu are cale de scriere spre iConta; proba de gard de scriere trece). Proba spune corect că iConta s-a schimbat după instantaneul inventarului (28.09.2026 17:47). *De decis:* se reface instantaneul (corpus + inventar) înaintea setului 4, sau setul 4 rulează pe instantaneul de acum?

## Operațiile, cu durata măsurată

| Operație | Durată | Cost |
|---|---|---|
| C49–C51 pe propunerile salvate ale seturilor 2 și 3 (navigarea reluată, 100 de propuneri, 2 comparații) | 105.8 s | $0 |
| Probe: 183 (182 trec; 1 pică — iConta modificat, vezi mai sus) | — | $0 |
