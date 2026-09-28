# Q-TVA-04 — REGULA

**Întrebarea:** O persoană înregistrată în scopuri de TVA a avut în 2025 o cifră de afaceri de 350.000 lei și nu a făcut achiziții intracomunitare de bunuri. Ce perioadă fiscală de TVA are în 2026 și la ce curs se verifică plafonul?

## Stratul de navigare (v4) — NU POT RĂSPUNDE

*La data de referință 31.12.2025, presupun o persoană impozabilă stabilită în România, înregistrată în scopuri de TVA conform art. 316, cu cifră de afaceri realizată în 2025 din operațiuni taxabile/scutite cu drept de deducere de 350.000 lei și fără achiziții intracomunitare de bunuri în 2025, care nu a optat și nu se află în vreo situație specială de înregistrare în cursul anului.*

Motiv: VERIFICAREA MECANICA a respins propunerea modelului: C17: atomul hg_1_2016_norme_cod_fiscal#art2~2/alin3~155 deroga de la / modifica un atom citat si raspunsul nu il trateaza; C17: atomul hg_1_2016_norme_cod_fiscal#art2~2/alin3~243 deroga de la / modifica un atom citat si raspunsul nu il trateaza

- **Codul fiscal (Legea 227/2015) art. 322 alin. (2)** — `cod_fiscal_227_2015_consolidat#art322/alin2` · valabil din nedovedit
  > perioada fiscală este trimestrul calendaristic pentru persoana impozabilă care în cursul anului calendaristic precedent a realizat o cifră de afaceri din operațiuni taxabile și/sau scutite cu drept de deducere și/sau neimpozabile în România conform art. 275 și 278 , dar care dau drept de deducere conform art. 297 alin. (4) lit. b) , care nu a depășit plafonul de 100.000 euro
- **Codul fiscal (Legea 227/2015) art. 322 alin. (2)** — `cod_fiscal_227_2015_consolidat#art322/alin2` · valabil din nedovedit
  > cu excepția situației în care persoana impozabilă a efectuat în cursul anului calendaristic precedent una sau mai multe achiziții intracomunitare de bunuri.
- **Normele metodologice ale Codului fiscal (HG 1/2016) art. 2 alin. (2)** — `hg_1_2016_norme_cod_fiscal#art2~2/alin2~185` · valabil din nedovedit
  > Echivalentul în lei al plafonului de 100.000 euro, prevăzut la art. 322 alin. (2) din Codul fiscal, în orice situație, se determină pe baza cursului de schimb comunicat de Banca Națională a României valabil pentru data de 31 decembrie a anului precedent
- derogare tratată: `cod_fiscal_227_2015_consolidat#art322/alin7` — Excepția care transformă trimestrul în lună calendaristică se aplică numai persoanei care efectuează o achiziție intracomunitară de bunuri taxabilă în România; în cazul din întrebare nu s-au făcut achiziții intracomunitare de bunuri, deci nu se aplică.
- derogare tratată: `hg_1_2016_norme_cod_fiscal#art2~2/alin3~141` — Excepția privește regularizările la schimbarea cotei de TVA pentru avansuri, nu determinarea plafonului perioadei fiscale; nu se aplică.
- derogare tratată: `hg_1_2016_norme_cod_fiscal#art2~2/alin3~260` — Excepția privește aplicarea banderolelor de către destinatari înregistrați în domeniul accizelor; nu are legătură cu plafonul perioadei fiscale de TVA.

### Navigarea (11 pași, 8 ture)

1. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Perioada fiscală"}
2. `cauta` {"interogare": "perioada fiscală trimestrul calendaristic plafon 100.000 euro achiziții intracomunitare"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art322/alin2"}
4. `cauta` {"interogare": "echivalentul în lei al plafonului de 100.000 euro perioada fiscală curs de schimb comunicat de Banca Națională a României ultima zi lucrătoare a anului"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art322/alin7"}
6. `cuprins` {"act": "hg_1_2016_norme_cod_fiscal", "filtru": "Perioada fiscală"}
7. `cauta` {"interogare": "plafonul cifrei de afaceri pentru trimestru se determină curs de schimb 31 decembrie decont trimestrial TVA norme"}
8. `cauta` {"interogare": "art. 322 din Codul fiscal echivalentul în lei al plafonului de 100.000 euro cursul de schimb valabil pentru data de 31 decembrie a anului precedent"}
9. `deschide` {"id": "hg_1_2016_norme_cod_fiscal#art2~2/alin2~185"}
10. `deschide` {"id": "hg_1_2016_norme_cod_fiscal#art2~2/alin3~141"}
11. `deschide` {"id": "hg_1_2016_norme_cod_fiscal#art2~2/alin3~260"}

Apel: `claude-opus-5`, {'intrare': 16, 'iesire': 3719, 'cache_scriere': 14181, 'cache_citire': 104678} tokeni, $0.2340, 70 s

Pe fond: **NU POT** — VERIFICAREA MECANICA a respins propunerea modelului: C17: atomul hg_1_2016_norme_cod_fiscal#art2~2/alin3~155 deroga de la / modifica un atom citat si raspunsul nu il trateaza; C17: atomul hg_1_2016_no

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Plafonul din atomul aplicabil este exprimat în euro (100.000 euro), iar echivalentul în lei „se calculează conform normelor metodologice”, normă care nu se află printre atomii primiți. Prin urmare nu pot stabili, fără un calcul de conversie și fără textul care indică cursul de schimb, nici cursul la care se verifică plafonul, nici dacă cifra de afaceri de 350.000 lei se situează sub plafon, deci nici perioada fiscală aplicabilă în 2026.

## Cheia

- Trimestrul calendaristic (CA sub plafonul de 100.000 euro și fără AIC în anul precedent); echivalentul în lei al plafonului se determină la cursul BNR valabil pentru 31 decembrie a anului precedent
- temei: Cod fiscal art. 322 alin. (2); HG 1/2016 (Norme metodologice), Titlul VII pct. 103 alin. (2)
