## 0. CERINȚE — decizii de arhitect

### Aplicate înainte de măsurătoare

| | Decizia | Cum e aplicată |
|---|---|---|
| **C38** | datele Adormirii (15.08) și ale Crăciunului (25–26.12): dată de calendar liturgic fix, declarată („dată de calendar, nescrisă în lege”), art. 139 citat; `termen_efectiv` reactivat | `navigare.Calendar.sarbatori`; probe: Q-TVA-07 → 02.03.2026, 15.08.2025 → 18.08.2025, 25.12.2026 → 28.12.2026 |
| **C39** | „Reproducem mai jos” numai în stratul oficial | neschimbat (confirmat) |
| **Regulile măsurătorii** | orbire (id, tip, intrebare), versiunea 485ffc3 neschimbată, răspunsuri comise înainte de comparație, comparator neschimbat, nicio reparație după comparație | proba `test_setul_2_se_incarca_orb`; commit-ul răspunsurilor `8b3269f` înaintea oricărei citiri a cheii; `git diff 485ffc3` pe `fiscalos/` = numai probe |

### Defecte găsite de măsurătoare — raportate ca cerințe, NEREPARATE (setul 2 nu se folosește pentru reglaje)

**C40 — Termenul efectiv nu e cerut modelului (clasa: calcul disponibil, nefolosit).** Q2-CTB-05: întrebarea
cere o dată, iar răspunsul dă regula, nu data. `termen_efectiv` exista și ar fi dat 02.06.2026, dar
promptul nu cere ca, la o întrebare „până la ce dată”, termenul nominal să treacă prin el. *Cerință:* orice
răspuns care dă un termen calendaristic îl calculează cu `termen_efectiv`; altfel răspunsul e INCOMPLET.

**C41 — Temeiul alăturat, cu text aproape identic (clasa: selecția temeiului).** Q2-TVA-05: CF art. 320
alin. (3) (beneficiarul obligat la plata taxei, taxare inversă) citat în locul art. 319 alin. (3)
(ajustarea taxei deductibile) — aceeași frază despre autofactură și „a 15-a zi a lunii următoare”, alt
subiect. Verificatorul nu poate prinde asta (citatul e verbatim, cifrele sunt literale). *Cerință:* la
două atomi cu text aproape identic, modelul vede subiectul fiecăruia (condiția din fraza introductivă) și
motivează alegerea.

**C42 — Comparatorul: zero și data cu an relativ (clasa: scor, nu motor).** Q2-TVA-09 („nu restituie”, „nu
implică ajustări” = 0 lei) și Q2-PRF-05 („25 iunie … a anului următor” = 25.06.2027) sunt corecte pe fond
și notate GREȘIT. *Cerință:* extinderea C30 — formulări de zero și data zi+lună cu an relativ față de o
cheie numerică. Scorul NU a fost schimbat pe baza lor.

**C43 — Faptul principal al cheii e un fapt secundar al întrebării (clasa: completitudine).** Q2-CPF-08
(cauțiunea de 4.500 lei), Q2-CTB-03 (pragul de 16.000.000 lei), Q2-CTB-09 (amenda de 2.000 lei): răspunsul
corect la întrebarea pusă („Are dreptate?”, „Este obligată?”, „Este legală?”), fără cifra pe care cheia o
pune pe primul loc. *De decis:* răspunsul trebuie să adauge consecința cuantificată (cauțiune, amendă,
prag), sau cheia se notează pe concluzie?

**C44 — Reîncercarea C23 degradează transportul (clasa: C23/C33).** 7 reîncercări C23 pe setul 2; după ele,
Q2-CPF-10 a scris diacriticele ca `"` („ceilal"i contribuabili/pl"titori”) — ireversibil, deci nedecodabil
ca la C33 — și a fost respinsă; Q2-TVA-08 s-a abținut după a doua structură invalidă. *Cerință:* răspunsul
final pe ieșire structurată (`output_config.format`) într-o tură finală fără unelte, în locul uneltei
`raspunde` (varianta din C23 neadoptată atunci).

**C45 — Respingeri ale calculului pe forma operandului (clasa: C25).** Q2-PRF-06 și Q2-CTB-07: operandul
„5” (o cincime, 5 ani) nu apare literal în fragmentul lui (textul spune „5 ani” sau „cincime”); Q2-SAL-07:
constanta 0 în formulă. Direcția e sigură (abținere), dar 3 întrebări CALCUL au pierdut răspunsul. *De
decis:* numerele scrise în litere în atom („cinci”, „o cincime”) ca operanzi, cu forma lor literală?

**C46 — Cifre derivate în textul răspunsului (clasa: C13/verificator).** Q2-TVA-06 („1.01.2019”),
Q2-CPF-06 („1.000.000”), Q2-CTB-06 („150”): o cifră calculată sau reformulată de model direct în text, nu
prin `calcule`, e respinsă corect. *Cerință:* promptul cere ca orice cifră care nu e citată literal să vină
dintr-un calcul.
