# Q2-TVA-06 — CALCUL

**Întrebarea:** O persoană impozabilă înregistrată în scopuri de TVA a cumpărat o clădire pe 15.06.2019 și a dedus integral TVA de 380.000 lei. În martie 2026 vinde clădirea în regim de scutire (art. 292 alin. 2 lit. f, fără opțiune de taxare). Ce ajustare a TVA dedusă trebuie să facă?

## Răspunsul — NU POT RĂSPUNDE

*La data de referință 31.03.2026, presupun o persoană impozabilă înregistrată în scopuri de TVA, cu regim normal de taxare, care a achiziționat în 15.06.2019 o clădire (bun de capital – bun imobil) cu TVA dedusă integral 380.000 lei și care în martie 2026 o livrează în regim de scutire fără drept de deducere conform art. 292 alin. (2) lit. f), fără opțiune de taxare; presupun că nu a existat pro rata, nici transformări/modernizări ulterioare și că bunul a fost folosit anterior exclusiv pentru operațiuni cu drept de deducere.*

Motiv: VERIFICAREA MECANICA a respins propunerea modelului: cifra '1.01.2019' din raspuns nu apare literal in citate sau in intrebare

- `ajustare = taxa_dedusa * (perioada_ajustare - (an_livrare - an_achizitie)) / perioada_ajustare` = ((380.000 × (20 − (2.026 − 2.019))) ÷ 20) = **247.000**
- **Codul fiscal (Legea 227/2015) art. 305 alin. (5) lit. a)** — `cod_fiscal_227_2015_consolidat#art305/alin5/lita`
  > precum și în cazul livrării bunului de capital în regim de scutire conform art. 292 , ajustarea deducerii se face o singură dată pentru întreaga perioadă de ajustare rămasă, incluzând anul în care apare modificarea destinației de utilizare;
- **Codul fiscal (Legea 227/2015) art. 305 alin. (5) lit. a)** — `cod_fiscal_227_2015_consolidat#art305/alin5/lita`
  > ajustarea se efectuează în cadrul perioadei de ajustare prevăzute la alin. (2) , pentru o cincime sau, după caz, o douăzecime din taxa dedusă inițial, pentru fiecare an în care apare o modificare a destinației de utilizare.
- **Codul fiscal (Legea 227/2015) art. 305 alin. (2) lit. b)** — `cod_fiscal_227_2015_consolidat#art305/alin2/litb`
  > pe o perioadă de 20 de ani, pentru construcția sau achiziția unui bun imobil, precum și pentru transformarea sau modernizarea unui bun imobil
- **Codul fiscal (Legea 227/2015) art. 305 alin. (3) lit. c)** — `cod_fiscal_227_2015_consolidat#art305/alin3/litc`
  > de la data de 1 ianuarie a anului în care bunurile au fost achiziționate, pentru bunurile de capital prevăzute la alin. (2) lit. b) , și se efectuează pentru suma integrală a taxei deductibile aferente bunului de capital
- **Codul fiscal (Legea 227/2015) art. 305 alin. (4) lit. a) pct. 2** — `cod_fiscal_227_2015_consolidat#art305/alin4/lita/pct2`
  > pentru realizarea de operațiuni care nu dau drept de deducere a taxei;
- **Codul fiscal (Legea 227/2015) art. 305 alin. (2)** — `cod_fiscal_227_2015_consolidat#art305/alin2`
  > Taxa deductibilă aferentă bunurilor de capital, în condițiile în care nu se aplică regulile privind livrarea către sine sau prestarea către sine, se ajustează, în situațiile prevăzute la alin. (4) lit. a)-d) :

Navigare: 12 pași; `claude-opus-5`; {'intrare': 16, 'iesire': 7064, 'cache_scriere': 17056, 'cache_citire': 122595} tokeni; $0.3446; 105 s

Pe fond (comparator): **NU POT** — VERIFICAREA MECANICA a respins propunerea modelului: cifra '1.01.2019' din raspuns nu apare literal in citate sau in intrebare

## Cheia

- 247.000 lei ajustare negativă (TVA de restituit), făcută o singură dată în decontul perioadei în care are loc livrarea. Calcul: perioada de ajustare pentru bunuri imobile = 20 de ani, începând cu 01.01.2019 → 2019–2038; ani rămași, incluzând anul livrării 2026: 2026–2038 = 13 ani; ajustare = 380.000 / 20 × 13 = 19.000 × 13 = 247.000 lei.
- temei: Cod fiscal art. 305 alin. (2) lit. b); art. 305 alin. (3) lit. c); art. 305 alin. (4) lit. a) pct. 2; art. 305 alin. (5) lit. a); HG 1/2016 (Norme metodologice), Titlul VII pct. 58 alin. (6)
