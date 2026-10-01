# Q4-CPF-03 — REGULA

**Întrebarea:** O SRL a cerut ANAF (organul fiscal central) un certificat de atestare fiscală pe 02.03.2026, iar certificatul i-a fost eliberat pe 04.03.2026. Firma vrea să îl prezinte pe 15.04.2026 într-o procedură de achiziție publică. Mai poate folosi acest certificat?

## RĂSPUNS

> **Nu. Certificatul de atestare fiscală emis de organul fiscal central poate fi utilizat pe o perioadă de până la 30 de zile de la data eliberării, deci certificatul eliberat la 04.03.2026 putea fi folosit cel târziu până la 03.04.2026. La 15.04.2026 perioada de utilizare este depășită, astfel încât certificatul nu mai poate fi prezentat în procedura de achiziție publică, iar societatea trebuie să solicite un certificat nou. [calcul: termen_efectiv(03.04.2026) = 03.04.2026 (zi lucrătoare: vineri); date mobile calculate pentru 2026 (Paștele ortodox: algoritmul Meeus pentru calendarul iulian + 13 zile): Vinerea Mare = 10.04.2026; Paștele ortodox = 12.04.2026; Rusaliile = Paștele + 49 de zile = 31.05.2026; sărbători numite în art. 139 fără dată, cu data de calendar liturgic fix (dată de calendar, nescrisă în lege): Adormirea Maicii Domnului = 15.08.2026; Crăciunul = 25-26.12.2026; data_limita = termen_efectiv(data_eliberarii + zile_utilizare) = termen_efectiv((04.03.2026 + 30)) = 03.04.2026] [data de referință: 15.04.2026 — Faptul întrebat este dacă certificatul mai poate fi folosit la momentul prezentării lui în procedura de achiziție publică, adică la 15.04.2026; celelalte date (02.03.2026, 04.03.2026) sunt doar elemente de fapt ale emiterii.]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- `termen_efectiv(03.04.2026) = 03.04.2026 (zi lucrătoare: vineri); date mobile calculate pentru 2026 (Paștele ortodox: algoritmul Meeus pentru calendarul iulian + 13 zile): Vinerea Mare = 10.04.2026; Paștele ortodox = 12.04.2026; Rusaliile = Paștele + 49 de zile = 31.05.2026; sărbători numite în art. 139 fără dată, cu data de calendar liturgic fix (dată de calendar, nescrisă în lege): Adormirea Maicii Domnului = 15.08.2026; Crăciunul = 25-26.12.2026`
- `data_limita = termen_efectiv(data_eliberarii + zile_utilizare)` = termen_efectiv((04.03.2026 + 30)) = **03.04.2026**
- **Codul de procedură fiscală (Legea 207/2015) art. 158 alin. (5)** — `legea_207_2015_consolidat#art158/alin5`
  > Certificatul de atestare fiscală se emite în maximum 3 zile lucrătoare de la data depunerii cererii și poate fi utilizat de persoana interesată, pe o perioadă de până la 30 de zile de la data eliberării.
- **Codul de procedură fiscală (Legea 207/2015) art. 158 alin. (5)** — `legea_207_2015_consolidat#art158/alin5`
  > Pe perioada de utilizare, certificatul poate fi prezentat de contribuabil/plătitor, în original sau în copie legalizată, oricărui solicitant.
- **Legea 134/2010 art. 181 alin. (2)** — `legea_134_2010_codul_de_procedura_civila#art181/alin2`
  > Când ultima zi a unui termen cade într-o zi nelucrătoare, termenul se prelungește până în prima zi lucrătoare care urmează.
- **Codul muncii (Legea 53/2003) art. 139 alin. (1)** — `legea_53_2003_codul_muncii#art139/alin1`
  > Zilele de sărbătoare legală în care nu se lucrează sunt: – 1 și 2 ianuarie; – 6 ianuarie - Botezul Domnului - Boboteaza; – 7 ianuarie - Soborul Sfântului Proroc Ioan Botezătorul; – 24 ianuarie – Ziua Unirii Principatelor Române; – Vinerea Mare, ultima zi de vineri înaintea Paștelui; – prima și a doua zi de Paști; – 1 mai; – 1 iunie;

Reparație C52: cifre ['90'] → RASPUNS

Navigare: 8 pași, 8 ture; $0.3593; 86 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## Cheia

- Nu. Certificatul de atestare fiscală emis de organul fiscal central poate fi utilizat pe o perioadă de până la 30 de zile de la data eliberării (04.03.2026); la 15.04.2026 au trecut 42 de zile, deci firma trebuie să ceară un certificat nou, pe care ANAF îl emite în maximum 3 zile lucrătoare de la depunerea cererii. (Perioada de 90 de zile se aplică doar persoanelor fizice care nu desfășoară activități economice independente sau profesii libere.) Noul certificat va cuprinde obligațiile restante în sold în ultima zi a lunii anterioare depunerii cererii și nestinse până la eliberare.
- temei: Legea 207/2015 art. 158 alin. (5); art. 158 alin. (2)
