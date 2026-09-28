# Q-CTB-01 — PARAMETRU

**Întrebarea:** Care este valoarea fiscală minimă de intrare de la care o imobilizare corporală este mijloc fix amortizabil în anul fiscal 2026?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 28.09.2026, pentru anul fiscal 2026, presupun un contribuabil plătitor de impozit pe profit care aplică regulile de amortizare fiscală din Codul fiscal pentru imobilizări corporale deținute și utilizate în activitate, cu durată normală de utilizare mai mare de un an.*

> **O imobilizare corporală este mijloc fix amortizabil dacă, la data intrării în patrimoniu, are o valoare fiscală egală sau mai mare decât 5.000 lei (limită actualizabilă anual, în funcție de indicele de inflație, prin hotărâre a Guvernului), pe lângă celelalte condiții cumulative (utilizare în activitate și durată normală de utilizare mai mare de un an).**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 28 alin. (2) lit. b)** — `cod_fiscal_227_2015_consolidat#art28/alin2/litb` · valabil din 2026-02-25
  > la data intrării în patrimoniul contribuabilului, are o valoare fiscală egală sau mai mare decât suma de 5.000 lei; această limită se actualizată anual, în funcție de indicele de inflație, prin hotărâre a Guvernului;
- **Codul fiscal (Legea 227/2015) art. 28 alin. (2)** — `cod_fiscal_227_2015_consolidat#art28/alin2` · valabil din nedovedit
  > Mijlocul fix amortizabil este orice imobilizare corporală care îndeplinește cumulativ următoarele condiții:
- **Codul fiscal (Legea 227/2015) art. 28 alin. (21)** — `cod_fiscal_227_2015_consolidat#art28/alin21` · valabil din nedovedit
  > În cazul unei imobilizări corporale care la data intrării în patrimoniu are o valoare fiscală mai mică decât limita stabilită prin hotărâre a Guvernului, contribuabilul poate recupera aceste cheltuieli prin deduceri de a

### Navigarea (6 pași, 4 ture)

1. `cauta` {"interogare": "mijloc fix amortizabil valoare de intrare mai mare decât limita stabilită prin hotărâre a Guvernului"}
2. `cuprins` {"act": "hg_276_2013", "filtru": ""}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art28/alin2/litb"}
4. `deschide` {"id": "hg_276_2013#art1"}
5. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art28/alin2"}
6. `cauta` {"interogare": "actualizarea limitei minime a valorii mijloacelor fixe hotărâre a Guvernului lei"}

Apel: `claude-opus-5`, {'intrare': 8, 'iesire': 2183, 'cache_scriere': 4803, 'cache_citire': 30030} tokeni, $0.0997, 34 s

Pe fond: **CORECT** — faptul principal si articolul coincid

## Stratul semantic v3 (context dat de căutare) — RĂSPUNS, pe fond CORECT

> Valoarea fiscală minimă la data intrării în patrimoniu este de 5.000 lei: imobilizarea corporală este mijloc fix amortizabil dacă are o valoare fiscală egală sau mai mare decât 5.000 lei (limită care se actualizează anual, în funcție de indicele de inflație, prin hotărâre a Guvernului), cu îndeplinirea cumulativă și a celorlalte condiții (deținere/utilizare în scopurile prevăzute și durată normală de utilizare mai mare de un an).

## Cheia

- 5.000 lei (egală sau mai mare), limită actualizabilă anual cu inflația prin HG; până în 2025 limita era 2.500 lei (HG 276/2013).
- temei: Legea 227/2015 (Cod fiscal) art. 28 alin. (2) lit. b), modificat de OUG 8/2026 art. 6 pct. 7, aplicabil de la anul fiscal 2026 (OUG 8/2026 art. 10 alin. (2)); HG 276/2013 art. 1 alin. (1) pentru limita anterioară
