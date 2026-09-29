# Q-CTB-01 — PARAMETRU

**Întrebarea:** Care este valoarea fiscală minimă de intrare de la care o imobilizare corporală este mijloc fix amortizabil în anul fiscal 2026?

## Stratul de navigare v5 — RĂSPUNS

*La data de referință 28.09.2026, pentru anul fiscal 2026, presupun un contribuabil plătitor de impozit pe profit care aplică regulile de amortizare fiscală din Codul fiscal, iar imobilizarea corporală îndeplinește celelalte condiții (deținere/utilizare în activitate și durată normală de utilizare mai mare de un an).*

Datele din întrebare: 2026-09-28 · data de referință aleasă: **2026-09-28** — Întrebarea vizează anul fiscal 2026, iar singura dată furnizată este 28.09.2026.

> **Valoarea fiscală la data intrării în patrimoniu trebuie să fie egală sau mai mare decât 5.000 lei (limită actualizabilă anual prin hotărâre a Guvernului, în funcție de indicele de inflație); pragul de 5.000 lei se aplică începând cu anul fiscal 2026.**

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 28 alin. (2) lit. b)** — `cod_fiscal_227_2015_consolidat#art28/alin2/litb` · valabil din 2026-02-25
  > la data intrării în patrimoniul contribuabilului, are o valoare fiscală egală sau mai mare decât suma de 5.000 lei; această limită se actualizată anual, în funcție de indicele de inflație, prin hotărâre a Guvernului;
- **Codul fiscal (Legea 227/2015) art. 28 alin. (2)** — `cod_fiscal_227_2015_consolidat#art28/alin2` · valabil din nedovedit
  > Mijlocul fix amortizabil este orice imobilizare corporală care îndeplinește cumulativ următoarele condiții:

### Navigarea (5 pași, 5 ture)

1. `cauta` {"interogare": "mijloc fix amortizabil valoare de intrare limita stabilita prin hotarare a Guvernului"}
2. `cauta` {"interogare": "valoarea minima de intrare a mijloacelor fixe 2500 lei"}
3. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art28/alin2"}
4. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art28/alin2/litb"}
5. `cauta` {"interogare": "actualizare limita 5.000 lei valoare fiscală mijloace fixe indice inflatie hotarare Guvern 2026"}

Apel: `claude-opus-5`, {'intrare': 10, 'iesire': 1397, 'cache_scriere': 5392, 'cache_citire': 45681} tokeni, $0.0915, 34 s

Pe fond (comparator): **CORECT** — faptul principal si articolul coincid

## v4 — RĂSPUNS, pe fond CORECT

> O imobilizare corporală este mijloc fix amortizabil dacă, la data intrării în patrimoniu, are o valoare fiscală egală sau mai mare decât 5.000 lei (limită actualizabilă anual, în funcție de indicele de inflație, prin hotărâre a Guvernului), pe lângă celelalte condiții cumulative (utilizare în activitate și durată normală de utilizare mai mare de un an).

## Cheia

- 5.000 lei (egală sau mai mare), limită actualizabilă anual cu inflația prin HG; până în 2025 limita era 2.500 lei (HG 276/2013).
- temei: Legea 227/2015 (Cod fiscal) art. 28 alin. (2) lit. b), modificat de OUG 8/2026 art. 6 pct. 7, aplicabil de la anul fiscal 2026 (OUG 8/2026 art. 10 alin. (2)); HG 276/2013 art. 1 alin. (1) pentru limita anterioară
