# Q4-PRF-05 — PROCEDURA

**Întrebarea:** AGA unei SRL aprobă la 29.04.2026 situațiile financiare 2025 și distribuirea de dividende către asociatul persoană juridică rezident într-un stat din afara UE/SEE cu care România are convenție de evitare a dublei impuneri. Dividendele nu se plătesc până la 31.12.2026. Mai trebuie declarat și plătit impozitul pe dividende și, dacă da, până când și la ce cotă?

## RĂSPUNS

> **Da. Deși dividendele nu s-au plătit până la sfârșitul anului în care s-a aprobat distribuirea, impozitul pe dividende se declară și se plătește până la 25.01.2027. Cota internă este de 16% asupra dividendului brut; dacă nerezidentul prezintă plătitorului certificatul de rezidență fiscală, se aplică cota mai favorabilă prevăzută în convenția de evitare a dublei impuneri, iar altfel se aplică cota din Codul fiscal. Scutirea pentru dividende neplătite la sfârșitul anului nu operează, întrucât beneficiarul nu este rezident într-un stat membru UE/SEE. [calcul: termen_efectiv(25.01.2027) = 25.01.2027 (zi lucrătoare: luni); date mobile calculate pentru 2027 (Paștele ortodox: algoritmul Meeus pentru calendarul iulian + 13 zile): Vinerea Mare = 30.04.2027; Paștele ortodox = 02.05.2027; Rusaliile = Paștele + 49 de zile = 20.06.2027; sărbători numite în art. 139 fără dată, cu data de calendar liturgic fix (dată de calendar, nescrisă în lege): Adormirea Maicii Domnului = 15.08.2027; Crăciunul = 25-26.12.2027; termen_declarare_plata = termen_efectiv(data(zi_termen, 1, an_aprobare + 1)) = termen_efectiv(data(25, 1, (2026 + 1))) = 25.01.2027] [avertisment C41: temei cu geamăn nejustificat — cod_fiscal_227_2015_consolidat#art111/alin6^6; cod_fiscal_227_2015_consolidat#art227/alin1; cod_fiscal_227_2015_consolidat#art233/alin3] [data de referință: 31.12.2026 — Faptul întrebat este regimul dividendelor distribuite în 2026 și rămase neplătite la sfârșitul anului în care s-a aprobat distribuirea, adică situația constatată la 31.12.2026, dată care declanșează obligația de declarare și plată.]**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- `termen_efectiv(25.01.2027) = 25.01.2027 (zi lucrătoare: luni); date mobile calculate pentru 2027 (Paștele ortodox: algoritmul Meeus pentru calendarul iulian + 13 zile): Vinerea Mare = 30.04.2027; Paștele ortodox = 02.05.2027; Rusaliile = Paștele + 49 de zile = 20.06.2027; sărbători numite în art. 139 fără dată, cu data de calendar liturgic fix (dată de calendar, nescrisă în lege): Adormirea Maicii Domnului = 15.08.2027; Crăciunul = 25-26.12.2027`
- `termen_declarare_plata = termen_efectiv(data(zi_termen, 1, an_aprobare + 1))` = termen_efectiv(data(25, 1, (2026 + 1))) = **25.01.2027**
- **Codul fiscal (Legea 227/2015) art. 224 alin. (5)** — `cod_fiscal_227_2015_consolidat#art224/alin5`
  > În cazul dividendelor distribuite, potrivit legii, dar care nu au fost plătite acționarilor sau asociaților până la sfârșitul anului în care s-a aprobat distribuirea acestora, impozitul pe dividende se declară și se plătește până la data de 25 ianuarie a anului următor
- **Codul fiscal (Legea 227/2015) art. 224 alin. (4) lit. b)** — `cod_fiscal_227_2015_consolidat#art224/alin4/litb`
  > 16% pentru veniturile din dividende prevăzute la art. 223 alin. (1) lit. a) ;
- **Codul fiscal (Legea 227/2015) art. 230 alin. (1)** — `cod_fiscal_227_2015_consolidat#art230/alin1`
  > dacă un contribuabil este rezident al unei țări cu care România a încheiat o convenție pentru evitarea dublei impuneri, cota de impozit care se aplică venitului impozabil obținut de către acel contribuabil din România nu poate depăși cota de impozit prevăzută în convenția care se aplică asupra acelui venit.
- **Codul fiscal (Legea 227/2015) art. 230 alin. (2)** — `cod_fiscal_227_2015_consolidat#art230/alin2`
  > nerezidentul are obligația de a prezenta plătitorului de venit, în momentul plății venitului, certificatul de rezidență fiscală eliberat de către autoritatea competentă din statul său de rezidență
- **Codul fiscal (Legea 227/2015) art. 229 alin. (1) lit. c)** — `cod_fiscal_227_2015_consolidat#art229/alin1/litc`
  > dividendele plătite de un rezident unei persoane juridice rezidente într-un alt stat membru al Uniunii Europene ori unui sediu permanent al unei persoane juridice străine dintr-un stat membru al Uniunii Europene, situat într-un alt stat membru al Uniunii Europene, dacă:
- **Legea 134/2010 art. 181 alin. (2)** — `legea_134_2010_codul_de_procedura_civila#art181/alin2`
  > Când ultima zi a unui termen cade într-o zi nelucrătoare, termenul se prelungește până în prima zi lucrătoare care urmează.
- **Codul muncii (Legea 53/2003) art. 139 alin. (1)** — `legea_53_2003_codul_muncii#art139/alin1`
  > Zilele de sărbătoare legală în care nu se lucrează sunt: – 1 și 2 ianuarie; – 6 ianuarie - Botezul Domnului - Boboteaza; – 7 ianuarie - Soborul Sfântului Proroc Ioan Botezătorul; – 24 ianuarie – Ziua Unirii Principatelor Române;

Avertismente: C41 (avertisment): atomul citat cod_fiscal_227_2015_consolidat#art224/alin5 are un geaman (cod_fiscal_227_2015_consolidat#art111/alin6^6) si alegerea nu e justificata printr-o conditie literala care ii deosebeste; C41 (avertisment): atomul citat cod_fiscal_227_2015_consolidat#art224/alin5 are un geaman (cod_fiscal_227_2015_consolidat#art227/alin1) si alegerea nu e justificata printr-o conditie literala care ii deosebeste; C41 (avertisment): atomul citat cod_fiscal_227_2015_consolidat#art224/alin5 are un geaman (cod_fiscal_227_2015_consolidat#art233/alin3) si alegerea nu e justificata printr-o conditie literala care ii deosebeste

Navigare: 17 pași, 11 ture; $0.5089; 95 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## Cheia

- 25.01.2027 — impozitul pe dividendele distribuite și neplătite până la sfârșitul anului în care s-a aprobat distribuirea se declară și se plătește până la 25 ianuarie a anului următor (25.01.2027, zi lucrătoare), chiar dacă dividendele nu au fost plătite. Cota este 16% (dividende distribuite după 01.01.2026), sau cota mai favorabilă din convenție dacă nerezidentul prezintă certificatul de rezidență fiscală valabil pentru anul în care s-au aprobat situațiile financiare. Excepția de la calcul/reținere pentru dividendele neplătite se aplică doar beneficiarilor care îndeplinesc la finalul anului condițiile de scutire UE/SEE (art. 229 alin. (1) lit. c) sau c^1)), deci nu în acest caz. Impozitul se calculează și se plătește în lei.
- temei: Cod fiscal art. 224 alin. (5); art. 224 alin. (4) lit. b); art. 230 alin. (1) și (2); HG 1/2016 (Norme metodologice), Titlul VI pct. 11 alin. (3)
