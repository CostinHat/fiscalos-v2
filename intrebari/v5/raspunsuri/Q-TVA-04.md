# Q-TVA-04 — REGULA

**Întrebarea:** O persoană înregistrată în scopuri de TVA a avut în 2025 o cifră de afaceri de 350.000 lei și nu a făcut achiziții intracomunitare de bunuri. Ce perioadă fiscală de TVA are în 2026 și la ce curs se verifică plafonul?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 28.09.2026, presupun o persoană impozabilă stabilită în România, înregistrată în scopuri de TVA conform art. 316, care în anul calendaristic precedent (2025) a realizat o cifră de afaceri de 350.000 lei din operațiuni ce intră în calculul plafonului și care nu a efectuat achiziții intracomunitare de bunuri, fără a beneficia de o perioadă fiscală specială aprobată.*

Datele din întrebare: 2025-12-31, 2026-09-28 · data de referință aleasă: **2026-09-28** — Faptul întrebat este perioada fiscală de TVA aplicabilă în anul 2026; cifra de afaceri din 2025 este doar elementul de verificare a plafonului.

> **Perioada fiscală în 2026 este trimestrul calendaristic, atât timp cât cifra de afaceri a anului precedent (350.000 lei) nu depășește echivalentul în lei al plafonului de 100.000 euro și nu s-au efectuat achiziții intracomunitare de bunuri. Plafonul se verifică prin transformarea celor 100.000 euro în lei pe baza cursului de schimb comunicat de Banca Națională a României valabil pentru data de 31 decembrie a anului precedent (31 decembrie 2025). Dacă în cursul anului se efectuează o achiziție intracomunitară de bunuri taxabilă în România, perioada fiscală devine luna calendaristică.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 322 alin. (2)** — `cod_fiscal_227_2015_consolidat#art322/alin2` · valabil din nedovedit
  > perioada fiscală este trimestrul calendaristic pentru persoana impozabilă care în cursul anului calendaristic precedent a realizat o cifră de afaceri din operațiuni taxabile și/sau scutite cu drept de deducere și/sau neimpozabile în România conform art. 275 și 278 , dar care dau drept de deducere conform art. 297 alin. (4) lit. b) , care nu a depășit plafonul de 100.000 euro
- **Codul fiscal (Legea 227/2015) art. 322 alin. (2)** — `cod_fiscal_227_2015_consolidat#art322/alin2` · valabil din nedovedit
  > care nu a depășit plafonul de 100.000 euro al cărui echivalent în lei se calculează conform normelor metodologice, cu excepția situației în care persoana impozabilă a efectuat în cursul anului calendaristic precedent una sau mai multe achiziții intracomunitare de bunuri.
- **Normele metodologice ale Codului fiscal (HG 1/2016) anexa, Titlul VII, pct. 103 alin. (2)** — `hg_1_2016_norme_cod_fiscal#anexa/pct103/alin2` · valabil din nedovedit
  > Echivalentul în lei al plafonului de 100.000 euro, prevăzut la art. 322 alin. (2) din Codul fiscal, în orice situație, se determină pe baza cursului de schimb comunicat de Banca Națională a României valabil pentru data de 31 decembrie a anului precedent
- **Codul fiscal (Legea 227/2015) art. 322 alin. (7)** — `cod_fiscal_227_2015_consolidat#art322/alin7` · valabil din nedovedit
  > Prin excepție de la prevederile alin. (2)-(6) , pentru persoana impozabilă care utilizează trimestrul calendaristic ca perioadă fiscală și care efectuează o achiziție intracomunitară de bunuri taxabilă în România, perioada fiscală devine luna calendaristică începând cu:
- derogare tratată: `cod_fiscal_227_2015_consolidat#art322/alin7` — Excepția de la alin. (2)-(6) se aplică doar dacă persoana impozabilă efectuează o achiziție intracomunitară de bunuri taxabilă în România; în cazul din întrebare nu s-au efectuat achiziții intracomunitare, deci perioada fiscală rămâne trimestrul calendaristic, dar am semnalat efectul ei în răspuns.

### Navigarea (12 pași, 11 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Perioada fiscală"}
2. `cauta` {"interogare": "perioada fiscală este trimestrul calendaristic plafon 100.000 euro cifra de afaceri"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art322/alin2"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art322/alin7"}
5. `cauta` {"interogare": "echivalentul în lei al plafonului de 100.000 euro se determină pe baza cursului de schimb comunicat de Banca Națională a României ultima zi lucrătoare a anului precedent perioada fiscală"}
6. `cuprins` {"act": "hg_1_2016_norme_cod_fiscal", "filtru": "322"}
7. `cauta` {"interogare": "art. 322 alin. (2) din Codul fiscal echivalentul în lei al plafonului de 100.000 euro cursul de schimb valutar din ultima zi lucrătoare a anului precedent"}
8. `cuprins` {"act": "hg_1_2016_norme_cod_fiscal", "filtru": "perioada fiscală"}
9. `cauta` {"interogare": "plafonul de 100.000 euro pentru perioada fiscală trimestrul calendaristic se determină pe baza cursului de schimb valutar comunicat de BNR la data de 31 decembrie"}
10. `cuprins` {"act": "hg_1_2016_norme_cod_fiscal", "filtru": "trimestrul calendaristic"}
11. `cauta` {"interogare": "În aplicarea art. 322 alin. (2) din Codul fiscal echivalentul în lei se determină pe baza cursului de schimb comunicat de Banca Națională a României valabil pentru data de 31 decembrie a anului precedent"}
12. `deschide` {"id": "hg_1_2016_norme_cod_fiscal#anexa/pct103/alin2"}

Apel: `claude-opus-5`, {'intrare': 22, 'iesire': 5969, 'cache_scriere': 20098, 'cache_citire': 185276} tokeni, $0.3676, 93 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — NU POT, pe fond NU POT

> VERIFICAREA MECANICA a respins propunerea modelului: C17: atomul hg_1_2016_norme_cod_fiscal#art2~2/alin3~155 deroga de la / modifica un atom citat si raspunsul nu il trateaza; C17: atomul hg_1_2016_norme_cod_fiscal#art2~2/alin3~243 deroga de la / modifica un atom citat si raspunsul nu il trateaza

## Cheia

- Trimestrul calendaristic (CA sub plafonul de 100.000 euro și fără AIC în anul precedent); echivalentul în lei al plafonului se determină la cursul BNR valabil pentru 31 decembrie a anului precedent
- temei: Cod fiscal art. 322 alin. (2); HG 1/2016 (Norme metodologice), Titlul VII pct. 103 alin. (2)
