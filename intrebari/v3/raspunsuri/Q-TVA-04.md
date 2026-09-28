# Q-TVA-04 — REGULA

**Întrebarea:** O persoană înregistrată în scopuri de TVA a avut în 2025 o cifră de afaceri de 350.000 lei și nu a făcut achiziții intracomunitare de bunuri. Ce perioadă fiscală de TVA are în 2026 și la ce curs se verifică plafonul?

## Stratul semantic — NU POT RĂSPUNDE

*La data de referință 31.12.2025, presupun o persoană impozabilă stabilită în România, înregistrată în scopuri de TVA conform art. 316, care în anul calendaristic precedent (2025) a realizat o cifră de afaceri de 350.000 lei din operațiuni care intră în calculul plafonului și care nu a efectuat achiziții intracomunitare de bunuri în 2025, întrebarea vizând perioada fiscală aplicabilă în 2026 și cursul de schimb de verificare a plafonului.*

Motiv: modelul s-a abţinut: Plafonul din atomul aplicabil este exprimat în euro (100.000 euro), iar echivalentul în lei „se calculează conform normelor metodologice”, normă care nu se află printre atomii primiți. Prin urmare nu pot stabili, fără un calcul de conversie și fără textul care indică cursul de schimb, nici cursul la care se verifică plafonul, nici dacă cifra de afaceri de 350.000 lei se situează sub plafon, deci nici perioada fiscală aplicabilă în 2026.

- **Codul fiscal (Legea 227/2015) art. 322 alin. (2)** — `cod_fiscal_227_2015_consolidat#art322/alin2` · valabil din nedovedit
  > care nu a depășit plafonul de 100.000 euro al cărui echivalent în lei se calculează conform normelor metodologice, cu excepția situației în care persoana impozabilă a efectuat în cursul anului calendaristic precedent una sau mai multe achiziții intracomunitare de bunuri.
- **Codul fiscal (Legea 227/2015) art. 322 alin. (6)** — `cod_fiscal_227_2015_consolidat#art322/alin6` · valabil din nedovedit
  > Persoana impozabilă care, potrivit alin. (2) și (5) , are obligația depunerii deconturilor trimestriale trebuie să depună la organele fiscale competente, până la data de 25 ianuarie inclusiv, o declarație de mențiuni în care să înscrie cifra de afaceri din anul precedent
- derogare tratată: `cod_fiscal_227_2015_consolidat#art322/alin7` — Derogarea privește persoana care utilizează trimestrul calendaristic și efectuează o achiziție intracomunitară de bunuri taxabilă în România; potrivit faptelor din întrebare nu s-au efectuat achiziții intracomunitare de bunuri, deci excepția nu se aplică cazului.

Apel: `claude-opus-5`, {'intrare': 4656, 'iesire': 1686, 'cache_scriere': 0, 'cache_citire': 1923} tokeni, $0.0664

Pe fond: **NU POT** — modelul s-a abţinut: Plafonul din atomul aplicabil este exprimat în euro (100.000 euro), iar echivalentul în lei „se calculează conform normelor metodologice”, normă care nu se află printre atomii pri

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2025-12-31 (an, din "2025"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: D15: intrebarea cere un fapt de forma 'suma', si niciun atom gasit (nici copiii lor) nu conţine unul


Pe fond: **NU POT** — D15: intrebarea cere un fapt de forma 'suma', si niciun atom gasit (nici copiii lor) nu conţine unul

## Cheia

- Trimestrul calendaristic (CA sub plafonul de 100.000 euro și fără AIC în anul precedent); echivalentul în lei al plafonului se determină la cursul BNR valabil pentru 31 decembrie a anului precedent
- temei: Cod fiscal art. 322 alin. (2); HG 1/2016 (Norme metodologice), Titlul VII pct. 103 alin. (2)
