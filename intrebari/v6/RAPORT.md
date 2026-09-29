# FiscalOS v2 — Pasul 7: deciziile C30–C33

Generat 29.09.2026 09:29 · ZIP: `/home/costin/ghid_incoming/fiscalos_v6_rezultat.zip`

> **Fără rulare plătită pe setul vechi (decizia 5).** C30 și C33 sunt măsurate pe ieșirile salvate, fără niciun apel; efectul lui C31 și C32 se măsoară pe setul nou. Scorurile sunt INDICATIVE.

## Rezultatul, măsurat fără apel nou

| | CORECT | GREȘIT | NU POT |
|---|---|---|---|
| Navigare v5, cum a fost raportată | 34 | 3 | 13 |
| + C33 (decodarea `\uXXXX`, pe propunerile salvate) | 36 | 3 | 11 |
| **+ C30 (comparatorul)** | **37** | **2** | **11** |

GREȘIT rămase: **Q-TVA-07** — articolul citat [('opanaf_2194_2025', 'pct2')] nu e printre cele ale cheii [('opanaf_3769_2015', 'pct2'), ('cpf', '75')]; **Q-SAL-10** — articolul citat [('cm', '281')] nu e printre cele ale cheii [('cm', '122'), ('cm', '123')]. Ambele sunt ținta deciziilor măsurate pe setul nou: Q-TVA-07 (termenul efectiv, sâmbătă → luni) — C32; Q-SAL-10 (Codul muncii din instantaneu, stricat) — C31.

## C30 — comparatorul: zero în cuvinte și data în litere

Defecte de clasă ale **scorului**, nu ale motorului. Reparațiile: un răspuns care spune explicit că nu se datorează nimic („nimic”, „zero”, „nu (se) datorează”) satisface o cheie al cărei fapt principal e zero; o dată în litere cu an („28 februarie 2026”) primește și forma numerică („28.02.2026”) ca alias (faptul principal rămâne zi + lună, ca anul relativ „anul următor” să nu devină mai sever); datele numerice se normalizează (1.3.2026 = 01.03.2026). Fiecare rulare pe corpusul ei:

| Rulare | Corpus (commit) | Înainte | După | Schimbări |
|---|---|---|---|---|
| semantic v2 | `b0a02c6` | 12/7/31 | 13/6/31 | Q-CPF-09 GRESIT→CORECT |
| semantic v3 | `7eb6fa0` | 10/8/32 | 11/7/32 | Q-CPF-09 GRESIT→CORECT |
| navigare v4 | `d35c21a` | 20/15/15 | 20/15/15 | — |
| navigare v5 | `778e826` | 34/3/13 | 35/2/13 | Q-CPF-09 GRESIT→CORECT |
| navigare v5 + C33 (propunerile salvate, decodate) | `778e826` | 36/3/11 | 37/2/11 | Q-CPF-09 GRESIT→CORECT |
| lexical v5 | `778e826` | 3/13/34 | 3/13/34 | — |

Nicio notă nu a devenit mai severă. Probe în ambele direcții: `test_intrebari.test_C30_*` (zero recunoscut numai când e spus; alt an nu se potrivește).

**Corectarea metodei, găsită aici:** după C31, id-urile unor atomi s-au schimbat (cuprinsul portalului, de ex. `cod_fiscal…#art156~2` → `#art156`). Re-comparată pe corpusul de acum, v5 ar fi ieșit 33/4/13 — o scădere care nu e a motorului. De aceea `comparatie.compara` primește acum corpusul rulării (`corpus_la_commit`, din git); tabelul de mai sus e calculat așa, iar cifrele istorice se reproduc (v2: 12/7/31, v5: 34/3/13).

## C33 — decodarea artefactului de transport

Aplicată: `navigare.decodeaza_transport` decodează, înainte de validare și verificare, numai secvența completă `\u` + 4 cifre hexa care dă un caracter tipăribil; orice alt backslash rămâne neatins. Probe: `test_navigare.test_C33_*` — secvențele reale („imobiliz\u0103rilor”, „\u021Aara”) se decodează; textul legitim (diacritice deja scrise, „C:\users”, „\u00” incomplet, „\uZZZZ”, caractere de control, surogate) nu se atinge. Pe propunerile v5 salvate, decodorul aplicat dă exact rezultatul măsurat în pasul anterior (0 diferențe).

Efect, fără apel: 34/3/13 → 36/3/11 (Q-TVA-09 → CORECT, Q-CPF-08 → NU_POT, Q-CTB-04 → CORECT).

## C31 — Codul muncii din sursa oficială și detectorul de structură

**Detectorul** (`fiscalos/detector_structura.py`) caută mecanic clasa „articole atomizate sub alt articol”, cu patru semnale: S1 alineate duplicate direct sub același articol; S2 acoperirea numerotării (articole recunoscute / cel mai mare număr, numai la actele de bază întregi); S3 articol imbricat într-un act de bază; S4 articol înghițit într-o notă. Rulat pe tot corpusul:

| Categorie | Instantaneul iConta | Corpusul de acum |
|---|---|---|
| de adus din sursa oficiala | 56 | 5 |
| deja din sursa oficiala - defect al conversiei portalului | 0 | 9 |
| nenormativ - numai raportat | 4 | 4 |
| redare istorica - nu se inlocuieste cu consolidatul curent | 1 | 1 |

**Aduse din sursa oficială: 47 acte** (`surse_oficiale/C31_rezolvare.json` — id-ul din portal și căutarea care l-a dat, pentru fiecare). Codul muncii: forma consolidată din 27.04.2026; art. 122 alin. (1) („…în următoarele 90 de zile calendaristice…”) are acum id-ul lui. Actele, cu atomii oficiali față de cei din instantaneu:

| Act | id portal | Atomi oficial / instantaneu |
|---|---|---|
| `hg_1045_2018_norme_consolidat` | 209698 | 193 / 182 |
| `hg_1074_2021` | 247209 | 289 / 24 |
| `hg_1094_2025` | 305236 | 190 / 25 |
| `hg_295_2025_reges_online_registru_salariati` | 295995 | 104 / 1 |
| `hg_518_1995` | 7037 | 115 / 13 |
| `hg_867_2015` | 172757 | 624 / 13 |
| `hg_905_2017` | 195770 | 104 / 1 |
| `legea_129_2019` | 216157 | 911 / 152 |
| `legea_136_2020_consolidat` | 227953 | 136 / 126 |
| `legea_141_2025_consolidat` | 300022 | 591 / 413 |
| `legea_165_2018_anaf` | 202623 | 145 / 191 |
| `legea_1_2020` | 221917 | 1165 / 20 |
| `legea_226_2023` | 272230 | 229 / 6 |
| `legea_230_2007` | 83753 | 198 / 1 |
| `legea_239_2025_stabilirea_masuri_redresare_eficientizare_resurselor` | 305208 | 834 / 568 |
| `legea_241_2005` | 63590 | 167 / 34 |
| `legea_265_2022` | 257835 | 866 / 33 |
| `legea_26_1990` | 783 | 248 / 46 |
| `legea_287_2009` | 109883 | 7404 / 438 |
| `legea_296_2020_consolidat` | 235513 | 590 / 223 |
| `legea_296_2023_masuri_fiscal_bugetare_asigurarea_sustenabilitatii` | 275745 | 951 / 775 |
| `legea_30_2019_aprobarea_ordonantei_urgenta_guvernului_25` | 210007 | 128 / 74 |
| `legea_31_1990_societatile` | 798 | 1997 / 1959 |
| `legea_346_2002_consolidat` | 36905 | 327 / 368 |
| `legea_448_2006_protectia_persoanelor_cu_handicap` | 77815 | 823 / 154 |
| `legea_53_2003_codul_muncii` | 41625 | 1236 / 109 |
| `legea_72_2013` | 146555 | 63 / 1 |
| `legea_82_1991_consolidat` | 1576 | 256 / 60 |
| `legea_85_2014` | 159286 | 2035 / 177 |
| `legea_98_2016` | 178667 | 1350 / 177 |
| `og_13_2011` | 131085 | 197 / 4 |
| `og_2_2001` | 29779 | 193 / 33 |
| `og_39_2015` | 170982 | 92 / 4 |
| `omfp_3254_2017_registru_evidenta_fiscala_persoane_fizice` | 196396 | 43 / 3 |
| `oms_15_2018_norme` | 196682 | 459 / 292 |
| `ordin_2594_2015` | 171984 | 283 / 7 |
| `ordin_3845_2015` | 174717 | 193 / 9 |
| `ordin_3846_2015` | 174706 | 337 / 8 |
| `ordin_878_2022` | 254993 | 121 / 11 |
| `oug_115_2023_consolidat` | 277404 | 682 / 374 |
| `oug_116_2023` | 277398 | 83 / 3 |
| `oug_120_2021` | 247243 | 166 / 21 |
| `oug_158_2005_consolidat` | 66305 | 333 / 341 |
| `oug_28_1999` | 17431 | 153 / 19 |
| `oug_44_2008` | 91808 | 203 / 32 |
| `oug_70_2024_ro_etva_decont_precompletat` | 284214 | 83 / 2 |
| `oug_89_2025` | 305817 | 475 / 309 |

Neaduse, cu motivul: `legea_165_2018_mf_2024` — varianta a aceluiasi act `legea_165_2018_anaf`; `legea_31_1990_modif_L222_2023` — varianta a aceluiasi act `legea_31_1990_societatile`; `omfp_1802_2014_ordin_consolidat` — acelasi act exista deja in stratul oficial `omfp_1802_2014`; `omfp_1802_2014_reglementari_consolidat` — acelasi act exista deja in stratul oficial `omfp_1802_2014`; `ordin_1099_2016` — ambiguu: [('177075', '1. ORDIN 1099 29/03/2016'), ('179451', '2. ORDIN 1099 23/06/2016'), ('180514', '3. ORDIN 1099 12/07/2016')].
Variantele stricate ale unui act care există acum oficial rămân în corpus (pentru potrivirea iConta), marcate „înlocuit de”, și **nu mai sunt indexate** de motorul de întrebări.

**Trei defecte de conversie a portalului, găsite de detector după aducere și reparate** (fiecare cu probă în `test_c12_c17.test_C31_*`):

1. **Cuprinsul-meniu** al portalului (linkuri `pozitioneaza(...)`) intra în text; ultimul marcaj din fiecare serie a cuprinsului rămânea „articol” — de aici dublurile `art135^2~2` în Codul fiscal și 2.455 de alineate duplicate în Codul civil. Linkurile de navigare se scot înainte de conversie.
2. **„Articolul 1.000”** (separator de mii) nu era recunoscut: tot Codul civil de după art. 999 se lipea de art. 999.
3. **Nota goală `<span …/>`** (element care se închide singur) era numărată ca deschisă: nota nu se mai închidea și înghițea articolele următoare — în Codul muncii oficial, art. 122–124. S4 a fost adăugat după acest caz.

**Defecte reziduale ale conversiei oficiale (9 acte, raportate, nereparate):** `legea_129_2019` (S1=4, S2=0.274), `legea_134_2010_codul_de_procedura_civila` (S1=8, S2=1.0), `legea_265_2022` (S1=5, S2=0.522), `legea_287_2009` (S1=13, S2=1.0), `legea_30_2019_aprobarea_ordonantei_urgenta_guvernului_25` (S1=8, S2=None), `legea_31_1990_societatile` (S1=8, S2=1.0), `og_13_2011` (S1=10, S2=0.079), `oug_70_2024_ro_etva_decont_precompletat` (S1=0, S2=0.062), `oug_89_2025` (S1=3, S2=None). La OG 13/2011 și OUG 70/2024 e altă clasă: acte de bază cu numerotare arabă care modifică alte legi — articolele citate (de ex. „art. 325” din Codul fiscal) apar ca articole proprii. Vezi C36.

Efectul asupra propunerii: **`propuneri/v7/`** — aceleași clasificări (94/1/26/26), 16 parametri cu atomul la locul lui din textul oficial (de ex. TVA 21%%: `legea_141_2025_consolidat#artII/pct42/art291/alin1`, sub punctul de intervenție). Bancul de mutații: 9/9.

## C32 — `termen_efectiv(data)`

Funcție de calcul: regula prelungirii și lista sărbătorilor legale se iau **numai din atomii citați în răspuns** — fără ei, calculul e respins. Sărbătorile cu dată mobilă se calculează (Paștele ortodox: algoritmul Meeus pentru calendarul iulian + 13 zile; Vinerea Mare = Paștele − 2; Rusaliile = Paștele + 49), iar calculul e declarat în răspuns. Tot acum: `data(zi, lună, an)` (luna poate fi scrisă în litere, din atom) și data + N zile, ca termenul nominal să poată fi construit din atomi.

Regula prelungirii pentru termenele fiscale e în **Codul de procedură civilă** (CPF art. 75 trimite la el), care **nu era în corpus**; l-am adus din sursa oficială, ca la C12 (id portal 120644, forma din 14.12.2025) — art. 181 alin. (2): „Când ultima zi a unui termen cade într-o zi nelucrătoare, termenul se prelungește până în prima zi lucrătoare care urmează.” Decizie a mea — de confirmat (C35).

Demonstrat pe atomii reali, fără model — termenul din Q-TVA-07:

> termen_efectiv(28.02.2026) = 02.03.2026: 28.02.2026 sâmbătă, 01.03.2026 duminică → prima zi lucrătoare, 02.03.2026 (luni). Regula: `legea_134_2010_codul_de_procedura_civila#art181/alin2`; sărbătorile: `legea_53_2003_codul_muncii#art139/alin1`; date mobile calculate pentru 2026 (Paștele ortodox: algoritmul Meeus pentru calendarul iulian + 13 zile): Vinerea Mare = 10.04.2026; Paștele ortodox = 12.04.2026; Rusaliile = Paștele + 49 de zile = 31.05.2026; sărbători numite în atom fără dată, cu data lor fixă (declarată, C34): Adormirea Maicii Domnului = 15.08; Crăciunul = 25-26.12
> termen = termen_efectiv(d) = termen_efectiv(28.02.2026) = 02.03.2026

Probe: `test_navigare.test_C32_*` (Paștele 2025–2027; sâmbătă → luni; Vinerea Mare 10.04.2026 → 14.04.2026; zi lucrătoare neschimbată; fără atomii citați — respins).

---

## 0. CERINȚE — decizii de arhitect

### Aplicate în acest pas

| | Decizia | Cum e aplicată | Dovada |
|---|---|---|---|
| **C30** | comparatorul reparat ca defect de clasă (zero în cuvinte, date în litere), scor înainte/după, fără apel | `comparatie._fapte_raspuns` (zero), alias numeric pentru data în litere cu an, normalizarea datelor numerice; `compara(…, corp)` pe corpusul rulării | `test_intrebari.test_C30_*`; tabelul C30 |
| **C31** | Codul muncii din sursa oficială; detector mecanic pe tot corpusul; actele stricate găsite, aduse tot din sursa oficială | `detector_structura.py` (S1–S4); `surse_oficiale_c31.py` (rezolvare în portal, aducere incrementală — actele deja aduse nu se ating); 47 de acte aduse; variantele stricate, scoase din index; 3 defecte de conversie a portalului reparate | `test_c12_c17.test_C31_*` (6); `propuneri/v7/` |
| **C32** | `termen_efectiv(data)`; regula și sărbătorile din atomi citați; Paști/Rusalii calculate, cu calculul declarat | `navigare.Calendar` + `termen_efectiv`, `data(z, l, a)`, data + N zile | `test_navigare.test_C32_*` (6) |
| **C33** | decodarea `\uXXXX` se aplică; probă în ambele direcții; scor înainte/după fără apel | `navigare.decodeaza_transport`, înainte de validarea C23 | `test_navigare.test_C33_*` (2); 34/3/13 → 36/3/11 |

### De decis

**C34 — Sărbătorile numite în lege fără dată.** Codul muncii art. 139 alin. (1) numește „Adormirea
Maicii Domnului” și „prima și a doua zi de Crăciun”, dar nu le scrie data. `termen_efectiv` le dă data
fixă a sărbătorii (15.08; 25–26.12) și o **declară** în răspuns ca atare („sărbători numite în atom
fără dată, cu data lor fixă”), la fel cum declară calculul Paștelui. *De decis:* se acceptă așa, sau
aceste două sărbători rămân în afara calculului (iar un termen care atinge 15.08 sau 25–26.12 iese
INCOMPLET)?

**C35 — Codul de procedură civilă adus în corpus.** CPF art. 75 trimite calculul termenelor fiscale la
Codul de procedură civilă, care nu era în instantaneu. L-am adus din legislatie.just.ro (ca la C12), ca
regula prelungirii (art. 181 alin. (2)) să vină dintr-un atom. *De confirmat:* rămâne în corpus?

**C36 — Defecte reziduale ale conversiei oficiale.** După reparații, detectorul mai semnalează 8 acte
oficiale: Codul civil (13 alineate duplicate, din 2.455), Legea 31/1990, Legea 129/2019, Legea 265/2022,
Legea 30/2019, OUG 89/2025 (alineate duplicate), și OG 13/2011, OUG 70/2024 — acte de bază arabe care
modifică alte legi, unde articolele citate apar ca articole proprii. *De decis:* se repară acum (a doua
clasă cere recunoașterea articolului citat într-un act de bază, nu doar într-un modificator), sau după
măsurătoarea pe setul nou?

**C37 — Ordinul 1099/2016, nerezolvat.** Portalul are trei ordine nr. 1099/2016 (29.03, 23.06, 12.07);
numele din instantaneu nu spune emitentul. Nu l-am ghicit. *De decis:* care e?

---

## Operațiile, cu durata măsurată

| Operație | Durată | Cost |
|---|---|---|
| Re-atomizarea instantaneului | 1.6 s | $0 |
| Atomizarea celor 54 de acte oficiale (cu C31, C32) | 3.1 s | $0 |
| Detectorul C31 pe instantaneu | 2.4 s | $0 |
| Detectorul C31 pe corpusul de acum | 4.1 s | $0 |
| C31: rezolvarea în portal și aducerea celor 47 de acte (rețea, pauză 2 s între cereri) | 496.8 s | $0 |
| C32: aducerea Codului de procedură civilă (rețea) | 7.2 s | $0 |
| Potrivirea parametrilor iConta pe corpusul nou | 8.1 s | $0 |
| Bancul de mutatii (9/9) | 4.8 s | $0 |
| Propunerea v7 | 4.2 s | $0 |
| Comparații C30 pe 6 rulări (fiecare pe corpusul ei), detector, raport | 14.6 s | $0 |

Niciun apel la model în acest pas: **$0**.
