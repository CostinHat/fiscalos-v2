# FiscalOS v2 — Testul de acceptare, setul 4

Generat 01.10.2026 08:35 · ZIP: `/home/costin/ghid_incoming/fiscalos_acceptare_set4.zip`

## Verdict: **ACCEPTAT**

| Criteriu | Cerut | Măsurat | |
|---|---|---|---|
| Greșeli de fond | cel mult 2 | **2** (Q4-PRF-07, Q4-CPF-10) | îndeplinit |
| CORECT pe fond (comparator neschimbat) | cel puțin 25 | **36** | îndeplinit |

Scorul pe fond (cifra oficială): **36 CORECT / 6 GREȘIT / 8 NU POT**.

Versiunea motorului: **1858001** (C40–C56), neschimbată; bucla de reluare (3d2c48b) e un script separat. Răspunsurile comise (**757af8a**) înainte de orice citire a cheii. Comparatorul neschimbat. Nicio reparație după comparație. Rularea a fost întreruptă o dată de creditul API după 16 întrebări și reluată de la a 17-a (cele salvate nu s-au plătit din nou).

**Marja verdictului:** a doua greșeală de fond (Q4-CPF-10) e o lectură — o întrebare INCOMPLETA la care modelul dă o cifră unică, deși explică apoi distincțiile; am numărat-o, consecvent cu setul 1. Dacă un om o judecă altfel, greșelile de fond sunt 1. Verdictul nu se schimbă în niciun caz; o a treia greșeală de fond l-ar fi schimbat.

## Greșelile de fond (cifra principală)

- **Q4-PRF-07** (CALCUL) — *valoarea întrebată necalculată*. Întrebarea cere cât impozit pe reprezentanță se datorează pentru 2026. Răspunsul dă regula (proporțional, de la luna înființării, din 18.000 lei/an) și termenele, dar nu suma: 18.000 × 8/12 = 12.000 lei. Nici termenul pentru 2027 nu e calculat (ultima zi a lui februarie 2027 e duminică → 01.03.2027): „până în ultima zi a lunii februarie” nu conține o dată, deci C40 nu-l vede.
- **Q4-CPF-10** (INCOMPLETA) — *INCOMPLETA tratată ca determinată*. Cheia: „depinde” (a câta licitație, imobil cu un singur ofertant). Răspunsul afirmă „Prețul minim de adjudecare este 50.000 lei” și abia apoi explică etapele. Conținutul explicației e corect (pragul de 25% din evaluare, la licitația de după a treia), dar răspunsul dat întrebării e o cifră unică acolo unde legea cere distincția. Numărat ca greșeală de fond, consecvent cu Q-PRF-10 din setul 1 (lectură de verificat de om: dacă nu se numără, greșelile de fond sunt 1).

## Celelalte GREȘIT ale comparatorului, citite pe fond (scorul nu s-a schimbat)

- **Q4-TVA-02** — comparator, nu fond (*procent scris „3 la mie”*): „în limita a 3 la mie din cifra de afaceri” = 0,3%, pe temeiul cheii (CF art. 270 alin. (8) lit. c), Norme pct. 7 alin. (12) lit. b)). Comparatorul nu recunoaște „3 la mie”.
- **Q4-TVA-08** — comparator, nu fond (*zero în alte cuvinte*): „nu se ajustează deducerea inițială … TVA de 4.200 lei rămâne dedusă” = ajustare 0 lei, pe temeiul cheii (CF art. 304 alin. (2) lit. a)). Formularea „nu se ajustează” nu e în lista C42.
- **Q4-CPF-04** — incomplet față de cheie, nu greșit (*faptul secundar al cheii omis*): Concluzia e a cheii („Nu … audierea se consideră îndeplinită la neprezentarea la două termene consecutive”, CPF art. 9 alin. (3) lit. b), art. 26 alin. (3)); cheia pune primul termenul de 5 zile lucrătoare pentru punctul de vedere scris — o informație de context, neîntrebată.
- **Q4-CTB-02** — comparator, nu fond (*numeral în litere*): „după trecerea a două luni din ziua publicării” = 2 luni, pe temeiul cheii (Legea 31/1990 art. 208). Comparatorul nu citește „două luni” ca „2 luni”.

## Pe tipuri

| Tip | CORECT | GREȘIT | NU POT |
|---|---|---|---|
| PARAMETRU | 7 | 2 | 1 |
| REGULA | 8 | 1 | 1 |
| CALCUL | 8 | 1 | 1 |
| CAPCANA | 9 | 1 | 0 |
| PROCEDURA | 4 | 0 | 1 |
| INCOMPLETA | 0 | 1 | 4 |

## Abțineri (8)

- **INCOMPLET detectat corect** (4): Q4-TVA-10, Q4-PRF-10, Q4-SAL-10, Q4-CTB-10 — toate cele 4 întrebări INCOMPLETA la care s-a abținut (a cincea, Q4-CPF-10, e greșeala de fond de mai sus).
- **C40** (2): Q4-PRF-01 („30 septembrie 2027”), Q4-SAL-04 („30 septembrie 2026”, „14 iulie”) — termene scrise direct. Trecute prin comparator *ca și cum* ar fi fost acceptate (numai citire): **ambele ar fi fost CORECTE**; C40 n-a prevenit nicio greșeală pe setul 4.
- **Calculul** (2): Q4-CPF-05 (sintaxa formulei; ar fi fost CORECT), Q4-CPF-07 (constanta 480.0 scrisă în formulă; ar fi fost GREȘIT pe faptul cheii).

## Mecanismele noi, pe setul 4

- **C41 (avertisment):** 3 răspunsuri cu avertisment (Q4-PRF-05, Q4-SAL-05, Q4-SAL-06) — toate CORECTE.
- **C52 (tura de reparație):** declanșată la 12 întrebări; 11 au trecut după reparație, 1 a rămas respinsă (Q4-CPF-05). Q4-PRF-07 (greșeala de fond) a trecut prin reparație — reparația a pus cifrele prin calcul, nu a adus suma lipsă.
- **C55/C56:** niciun operand legal nu a avut data valorii fixată de un atom citat, iar niciunul n-a fost respins pe valabilitate.

## C57 — „orice valoare numerică din răspuns sprijinită de un atom citat care o conține” (propunere, neimplementată)

**Există regula?** Parțial. Verificatorul de azi (C13 + C46) cere: o valoare legală — într-un citat; orice altă cifră — în citate **sau în întrebare**; iar comparația e pe **subșir** („5” trece dacă un citat conține „4.325”). Nu cere ca *orice* număr să fie într-un atom citat.

Ce ar fi schimbat pe răspunsurile acceptate salvate (`fiscalos/analiza_C57.py`, fără apel):

| Varianta | Setul 3 (19 acceptate) | Setul 4 (42 acceptate) |
|---|---|---|
| (a) strictă: orice număr — ca număr întreg într-un fragment citat, sau rezultat de calcul | 11 respinse: 10 CORECT pierdute, 1 GREȘIT (Q3-TVA-09, dar pentru „500.000”, fapt al cazului, nu pentru greșeala lui) | 28 respinse: 24 CORECT pierdute, 4 GREȘIT de comparator (dintre care **nicio greșeală de fond**) |
| (b) ca (a), dar faptele cazului (literal în întrebare) permise | 0 schimbări | 1 respins: Q4-TVA-05, CORECT (anul „2026” scris în text) |

Numerele „nesprijinite” sunt, aproape toate, fapte ale cazului (sume, date din întrebare) sau ani. **Niciuna dintre cele 3 greșeli de fond ale seturilor 3–4 nu ar fi fost prinsă** (Q3-TVA-09 — formula; Q4-PRF-07 — suma lipsește cu totul; Q4-CPF-10 — 50.000 e rezultat de calcul). Recomandare: C57 nu se adoptă în forma strictă; varianta (b) nu adaugă protecție măsurabilă — singura ei diferență utilă față de azi ar fi comparația pe număr întreg în loc de subșir.

## Costul

**$14.2196** pentru 50 de întrebări = **$0.284 / întrebare** (setul 3: $0,310; setul 2: $0,175; ținta orientativă: $0,20 — neatinsă). Pași de navigare: 8.9; ture: 7.9. Nemodificat înainte de verdict, cum s-a decis.

## 0. CERINȚE

### Aplicate în testul de acceptare

| | Decizia | Cum |
|---|---|---|
| **C56** | data valorii fixată de lege câștigă asupra declarației modelului | aplicată (`1858001`); pe setul 4 nu s-a declanșat |
| **C56/C57 (decizia de azi)** | nu se extinde la atomii văzuți necitați; C57 — verificată, propusă, neimplementată | secțiunea C57 |
| **Costul** | nimic schimbat înainte de verdict | — |
| **Regulile măsurătorii** | orbire (proba `test_setul_4_se_incarca_orb`), versiune fixă, răspunsuri comise înainte de comparație, comparator neschimbat, nicio reparație după | 1858001 → 757af8a |

### De decis (după acceptare)

**C58 — C40 costă răspunsuri corecte.** Pe seturile 3–4 a respins 3 răspunsuri (Q3-PRF-09, Q4-PRF-01, Q4-SAL-04), toate corecte pe fond; a prevenit o greșeală de fond o singură dată (Q2-CTB-05, pe propunerile salvate ale setului 2). Iar greșeala de termen de pe setul 4 (Q4-PRF-07, „ultima zi a lunii februarie”, fără dată) i-a scăpat. *De decis:* C40 rămâne respingere sau devine o tură de reparație (ca C52) care cere `termen_efectiv` pentru data găsită?

**C59 — Comparatorul: „3 la mie”, „nu se ajustează”, „două luni”.** 3 dintre cele 6 GREȘIT ale comparatorului sunt corecte pe fond (formulări nerecunoscute). Scorul oficial nu se schimbă; pentru măsurătorile următoare, extinderea C42 (procent „la mie”, zero în „nu se ajustează”, numerale în litere ca la C45).

**C60 — Costul $0,284/întrebare.** Peste ținta de $0,20. Contribuitori măsurabili: tura finală separată (C44), turele de reparație C52 (12 din 50 pe setul 4), 8.9 pași de navigare.

## Operațiile, cu durata și costul măsurate

| Operație | Durată | Cost |
|---|---|---|
| Apel de control al creditului (înainte de reluare) | <1 s | ~$0,0002 |
| Rularea, primul segment: întrebările 1–16 (oprită de creditul API la a 17-a) | 992 s | $5.1175 |
| Întrebarea întreruptă de credit (nesalvată) | — | nemăsurabil |
| Rularea, reluarea: întrebările 17–50 (timp de ceas: 2.170 s) | 2144 s | $9.1021 |
| Comparația cu cheia | 8 s | $0 |
| Analiza C57 pe seturile 3 și 4; citirea ipotetică a abținerilor | 8 s | $0 |
| Raport, fișiere per întrebare, ZIP | <5 s | $0 |
| **Total testul de acceptare** | **3136 s** de apeluri | **$14.2196** |
