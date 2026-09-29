# FiscalOS v2 — Pasul 8: deciziile C34–C37

Generat 29.09.2026 11:04 · ZIP: `/home/costin/ghid_incoming/fiscalos_v7_rezultat.zip`

> Fără niciun apel la model ($0). Efectul pe motor se măsoară pe setul nou.

## C34 — art. 139 din Codul muncii, textul oficial

Verificat în HTML-ul portalului (forma consolidată din 27.04.2026): elementele listei sunt `<span class="S_LIN_BDY">`, iar două dintre ele nu au dată — „Adormirea Maicii Domnului;” și „prima și a doua zi de Crăciun;”. **Textul oficial nu le scrie data.** Atomul, după reparația de mai jos:

> Zilele de sărbătoare legală în care nu se lucrează sunt: – 1 și 2 ianuarie; – 6 ianuarie - Botezul Domnului - Boboteaza; – 7 ianuarie - Soborul Sfântului Proroc Ioan Botezătorul; – 24 ianuarie – Ziua Unirii Principatelor Române; – Vinerea Mare, ultima zi de vineri înaintea Paștelui; – prima și a doua zi de Paști; – 1 mai; – 1 iunie; – prima și a doua zi de Rusalii; – Adormirea Maicii Domnului; – 30 noiembrie - Sfântul Apostol Andrei, cel Întâi chemat, Ocrotitorul României; – 1 decembrie; – prima și a doua zi de Crăciun; – două zile pentru fiecare dintre cele 3 sărbători religioase anuale, declarate astfel de cultele religioase legale, altele decât cele creștine, pentru persoanele aparținând acestora.

**Un defect de conversie real, găsit la această verificare și reparat ca clasă:** „...” dintre elementele listelor nu era text al legii, ci forma *restrânsă* a elementului, pe care portalul o ascunde (`<span class="S_LIN_SHORT" style="display:none"> ... </span>`; la fel `S_LIT_SHORT`, `S_PCT_SHORT`, `S_NTA_SHORT`). 24.930 de asemenea span-uri în actele oficiale, toate cu conținutul „...” și nimic altceva — scoase; 18.058 de texte de atomi s-au curățat. Detectorul C31, rulat după: vezi C36.

Consecința, fără dată pusă de mână: `termen_efectiv` **se abține**, cu motivul scris. Pe atomii reali (Q-TVA-07, 28.02.2026):

> calculul termen: C34: atomul listei sarbatorilor legale (legea_53_2003_codul_muncii#art139/alin1) numeste fara data: Adormirea Maicii Domnului, prima și a doua zi de Crăciun - ziua lucratoare nu se poate stabili din atomi; calculul se abtine

Mecanismul (Paști/Rusalii calculate și declarate, sâmbătă → luni, zi lucrătoare neschimbată) rămâne probat pe o listă *sintetică* cu toate sărbătorile datate (`test_navigare.test_C32_mecanismul_*`). Ce rămâne de decis: C38.

## C36 — conversia oficială, reparată acum

Șase clase de defect, fiecare reparată ca regulă (nu act cu act) și probată:

| Clasa | Unde s-a văzut | Reparația |
|---|---|---|
| forma restrânsă ascunsă („...”) | toate actele (C34) | `S_*_SHORT` scos din HTML |
| textul **citat** (conținutul unui punct de intervenție) luat drept articole/alineate proprii | OG 13/2011, OUG 70/2024, Legea 129/2019, Legea 265/2022 | portalul îl marchează cu `S_CIT`; titlurile din interiorul lui primesc marcajul „citat”, cu **adâncimea** citării (Legea 30/2019: lege de aprobare → OUG 25/2018 → Codul fiscal); un articol citat se cuibărește sub punctul care îl introduce, unul propriu închide tot. Informația e a portalului, nu ghicită |
| număr de articol cu exponent roman sau cu literă | OUG 89/2025 „Articolul V^1”, Legea 31/1990 „Articolul 270^2 a)” | recunoscute; cheia normalizată (`artV^1`, `art270^2a`) |
| punct cu exponent | Legea 30/2019 „1^5.”, Codul fiscal, Normele | recunoscut; părintele — nodul al cărui ultim punct e baza |
| text **reprodus din alt act** la finalul consolidatului („NOTĂ: Reproducem mai jos … din Legea nr. 76/2012”) | Codul civil (Legea 71/2011), Codul de procedură civilă (Legea 76/2012) | devine un atom *notă* al actului, marcat ca notă (nu articol); zona se oprește la sfârșitul documentului sau la primul articol care continuă numerotarea proprie. Numai în stratul oficial — C39 |
| punct de intervenție într-un articol **arab** (instantaneu) | Legea 239/2025, OUG 50/2015 | recunoscut după text („… se modifică și va avea următorul cuprins”) |

**Detectorul, înainte (pasul 7) și după:**

| Categorie | Înainte | După |
|---|---|---|
| de adus din sursa oficiala | 5 | 0 |
| deja din sursa oficiala - defect al conversiei portalului | 9 | 0 |
| nenormativ - numai raportat | 4 | 4 |
| redare istorica - nu se inlocuieste cu consolidatul curent | 1 | 1 |
| varianta stricata, inlocuita de legea_165_2018_anaf (oficial) - pastrata numai pentru potrivirea iConta, scoasa din indexul motorului de intrebari | 0 | 1 |
| varianta stricata, inlocuita de legea_31_1990_societatile (oficial) - pastrata numai pentru potrivirea iConta, scoasa din indexul motorului de intrebari | 0 | 1 |
| varianta stricata, inlocuita de omfp_1802_2014 (oficial) - pastrata numai pentru potrivirea iConta, scoasa din indexul motorului de intrebari | 0 | 2 |

**Fiecare semnal rămas, cu motivul lui:**

| Act | Semnale | Motivul |
|---|---|---|
| `anaf_concedii_2025` | S1=0, S2=0.059, S4=0 | nenormativ - numai raportat |
| `d100_struct_anaf` | S1=0, S2=0.038, S4=0 | nenormativ - numai raportat |
| `legea_165_2018_mf_2024` | S1=7, S2=0.917, S4=0 | varianta stricata, inlocuita de legea_165_2018_anaf (oficial) - pastrata numai pentru potrivirea iConta, scoasa din indexul motorului de intrebari |
| `legea_31_1990_modif_L222_2023` | S1=1, S2=0.013, S4=0 | varianta stricata, inlocuita de legea_31_1990_societatile (oficial) - pastrata numai pentru potrivirea iConta, scoasa din indexul motorului de intrebari |
| `omfp_1802_2014_ordin_consolidat` | S1=0, S2=0.083, S4=0 | varianta stricata, inlocuita de omfp_1802_2014 (oficial) - pastrata numai pentru potrivirea iConta, scoasa din indexul motorului de intrebari |
| `omfp_1802_2014_reglementari_consolidat` | S1=21, S2=None, S4=0 | varianta stricata, inlocuita de omfp_1802_2014 (oficial) - pastrata numai pentru potrivirea iConta, scoasa din indexul motorului de intrebari |
| `oug_158_2005_pre_L141` | S1=7, S2=1.0, S4=0 | redare istorica - nu se inlocuieste cu consolidatul curent |
| `pdf_original/structura_D100_2026` | S1=0, S2=0.038, S4=0 | nenormativ - numai raportat |
| `pdf_original/structura_D100_v200_2014` | S1=0, S2=0.007, S4=0 | nenormativ - numai raportat |

Niciun act oficial nu mai e semnalat. Atomii-cheie ai pașilor anteriori există neschimbați (TVA 21%: `legea_141_2025_consolidat#artII/pct42/art291/alin1`; Codul muncii art. 122; CF art. 310 alin. (6), art. 41 alin. (10^1); CPC art. 181 alin. (2)).

Efectul asupra propunerii: **`propuneri/v8/`** — aceleași clasificări (94/1/26/26) și aceiași atomi; 18 citate verbatim curățate de „...”. Bancul de mutații: 9/9.

## C37 — ordinul 1099/2016

Portalul are trei ordine nr. 1099/2016 (29.03, 23.06, 12.07). Contextul care decide e **antetul actului, așa cum îl are instantaneul**: identificat dupa antetul din textul instantaneului: "ORDIN nr. 1.099 din 12 iulie 2016 pentru reglementarea unor aspecte privind rezidența în România a persoanelor fizice EMITENT MINISTERUL FIN" (data 12/07/2016, emitent MINISTERUL FINANȚELOR PUBLICE) -> ORDIN 1099 12/07/2016; pagina adusa contine acelasi obiect ("reglementarea unor aspecte privind rezidenta in Romania a persoanelor fizice"). Adus: id portal 180514. Regula e generală: la o căutare ambiguă, se citesc data și emitentul din antetul actului; dacă nici ele nu decid, actul rămâne în afara corpusului, cu mențiune.

---

## 0. CERINȚE — decizii de arhitect

### Aplicate în acest pas

| | Decizia | Cum e aplicată | Dovada |
|---|---|---|---|
| **C34** | nicio dată pusă de mână; textul oficial al art. 139 verificat; defect de conversie → reparat ca clasă + detector; altfel sărbătoarea rămâne fără dată, cu abținere | Textul oficial chiar nu scrie data pentru „Adormirea Maicii Domnului” și „prima și a doua zi de Crăciun” (verificat în HTML-ul portalului, `S_LIN_BDY`). Am găsit însă un defect de conversie real: „...” dintre elementele listelor e forma restrânsă ascunsă a portalului (`S_*_SHORT`, `display:none`) — scoasă ca clasă (24.930 de span-uri, 18.058 de texte de atomi curățate). `termen_efectiv` se abține când lista citată numește o sărbătoare fără dată | `test_navigare.test_C34_*`, `test_c12_c17.test_C36_forma_restransa_*` |
| **C35** | Codul de procedură civilă rămâne; un act la care trimite explicit o normă citată se aduce din sursa oficială, cu proveniență | neschimbat; proveniența în `surse_oficiale/MANIFEST.json` (`de_ce`) | — |
| **C36** | conversia reparată acum, la $0; detectorul curat sau cu motiv scris | 6 clase reparate (secțiunea C36); detectorul: 0 acte oficiale semnalate (erau 8); fiecare semnal rămas are categoria și motivul scris | `test_c12_c17.test_C36_*` (5) |
| **C37** | ordinul se identifică după context; altfel rămâne în afara corpusului | antetul din textul instantaneului („ORDIN nr. 1.099 din 12 iulie 2016 pentru reglementarea unor aspecte privind rezidența în România a persoanelor fizice, EMITENT MINISTERUL FINANȚELOR PUBLICE”) decide între cele trei ordine 1099/2016 → id 180514; regula e generală în `surse_oficiale_c31.rezolva` | `test_c12_c17.test_C37_*` |

### De decis

**C38 — `termen_efectiv` se abține acum pentru orice dată.** Consecința directă a lui C34: lista
oficială a sărbătorilor numește două sărbători fără dată, iar orice zi examinată — inclusiv „prima zi
lucrătoare” — ar putea fi una dintre ele. Cu corpusul de acum, calculul termenului efectiv (Q-TVA-07,
sâmbătă → luni) se abține întotdeauna, cu motivul scris. Nicio altă normă din corpus nu dă datele
(verificat: niciun atom normativ nu leagă „15 august” de Adormirea Maicii Domnului sau „25 decembrie” de
Crăciun). *De decis:* există o sursă normativă pentru aceste date care să fie adusă (ca la C35), sau
`termen_efectiv` rămâne inert până atunci?

**C39 — Nota de reproducere, numai în stratul oficial.** Regula „Reproducem mai jos … → notă” se aplică
numai formei portalului. În textul liber al instantaneului, aceeași frază apare și în mijlocul actului
(Codul fiscal), fără o graniță sigură: aplicată acolo, muta conținut real (măsurat: 6.098 → 333 de
atomi). Actele afectate din instantaneu sunt toate aduse acum din sursa oficială. *De confirmat.*

---

## Operațiile, cu durata măsurată

| Operație | Durată | Cost |
|---|---|---|
| Re-atomizarea instantaneului (C36: exponent, litera, interventie) | 1.9 s | $0 |
| Atomizarea celor 55 de acte oficiale (C34 forma restransa, C36 S_CIT, note reproduse) | 4.7 s | $0 |
| Detectorul C31/C36 pe corpusul de acum | 4.2 s | $0 |
| Potrivirea parametrilor iConta | 8.1 s | $0 |
| Bancul de mutatii (9/9) | 4.8 s | $0 |
| C37: aducerea ordinului 1099/2016 din portal (retea) | 0.4 s | $0 |
| Propunerea v8 | 4.2 s | $0 |
| Detector (înainte/după), demonstrația C34, raport | 4.2 s | $0 |

Niciun apel la model: **$0**.
