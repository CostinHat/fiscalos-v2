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
