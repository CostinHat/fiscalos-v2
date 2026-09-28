# Q-CTB-02 — CAPCANA

**Întrebarea:** O societate are un echipament cu valoare fiscală de intrare de 3.200 lei, intrat în 2024 și amortizat parțial la 31.12.2025. Din 2026 pragul e 5.000 lei: se trece valoarea rămasă integral pe cheltuieli deductibile în 2026?

## Stratul de navigare (v4) — RĂSPUNS

*La data de referință 31.12.2025, pentru un plătitor de impozit pe profit care deține un echipament (imobilizare corporală) intrat în patrimoniu în 2024 cu valoare fiscală de intrare de 3.200 lei, peste limita în vigoare la acea dată, amortizat parțial la 31.12.2025; presupun că activul rămâne în funcțiune și își păstrează calitatea de mijloc fix amortizabil, iar majorarea ulterioară a limitei stabilite prin hotărâre a Guvernului nu are efect retroactiv asupra activelor deja intrate în patrimoniu.*

> **Nu. Condiția de valoare (limita stabilită prin hotărâre a Guvernului) se apreciază la data intrării în patrimoniu, așa că echipamentul rămâne mijloc fix amortizabil, iar valoarea rămasă neamortizată se recuperează în continuare prin deduceri de amortizare, pe durata normală de funcționare rămasă, nu integral pe cheltuieli deductibile într-un singur an.**

Citatul decisiv (`cod_fiscal_227_2015_consolidat#art28/alin21`):
> În cazul unei imobilizări corporale care la data intrării în patrimoniu are o valoare fiscală mai mică decât limita stabilită prin hotărâre a Guvernului, contribuabilul poate recupera aceste cheltuieli prin deduceri de amortizare, potrivit prevederilor prezentului articol.

Motiv: propus de model, trecut prin verificarea mecanica: citate verbatim, cifre literale

- **Codul fiscal (Legea 227/2015) art. 28 alin. (21)** — `cod_fiscal_227_2015_consolidat#art28/alin21` · valabil din nedovedit
  > În cazul unei imobilizări corporale care la data intrării în patrimoniu are o valoare fiscală mai mică decât limita stabilită prin hotărâre a Guvernului, contribuabilul poate recupera aceste cheltuieli prin deduceri de amortizare, potrivit prevederilor prezentului articol.
- **HG 276/2013 art. 1 alin. (2)** — `hg_276_2013#art1~2/alin2` · valabil din nedovedit
  > Valoarea rămasă neamortizată a mijloacelor fixe cu valoarea de intrare cuprinsă între 1.800 lei şi 2.500 lei, existente în patrimoniul operatorilor economici la data intrării în vigoare a prezentei hotărâri, se va recupera pe durata normală de funcţionare rămasă.
- **HG 276/2013 art. 1 alin. (1)** — `hg_276_2013#art1~2/alin1` · valabil din nedovedit
  > Începând cu data intrării în vigoare a prezentei hotărâri, valoarea minimă de intrare a mijloacelor fixe stabilită în condiţiile art. 3 alin. 2 lit. a) din Legea nr. 15/1994 privind amortizarea capitalului imobilizat în active corporale şi necorporale, republicată, cu modificările şi completările ulterioare, este de 2.500 lei.
- derogare tratată: `cod_fiscal_227_2015_consolidat#art28/alin8^1` — Excepția de la art. 28 alin. (5) și (8) privește regimul de amortizare accelerată pentru active noi achiziționate/produse; nu se aplică aici, întrucât întrebarea vizează efectul majorării limitei valorice asupra unui activ deja intrat în patrimoniu, nu alegerea regimului de amortizare.

### Navigarea (12 pași, 7 ture)

1. `cauta` {"interogare": "valoarea fiscală de intrare a mijloacelor fixe amortizabile 5.000 lei prag"}
2. `cauta` {"interogare": "mijloace fixe aflate în patrimoniu continuă amortizarea potrivit regulilor în vigoare la data intrării"}
3. `cauta` {"interogare": "valoarea minimă de intrare a mijloacelor fixe 5.000 lei hotărâre"}
4. `deschide` {"id": "hg_276_2013#art1~2/alin2"}
5. `cuprins` {"act": "hg_145_2026", "filtru": ""}
6. `cauta` {"interogare": "valoarea rămasă neamortizată se recuperează pe durata normală de funcționare rămasă 5.000 lei"}
7. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art28/alin21"}
8. `cuprins` {"act": "cod_fiscal_227_2015_consolidat", "filtru": "Amortizarea fiscală"}
9. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art28"}
10. `deschide` {"id": "hg_276_2013#art1~2/alin1"}
11. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art28/alin2"}
12. `deschide` {"id": "cod_fiscal_227_2015_consolidat#art28/alin12"}

Apel: `claude-opus-5`, {'intrare': 14, 'iesire': 4729, 'cache_scriere': 16689, 'cache_citire': 85487} tokeni, $0.2653, 65 s

Pe fond: **GREȘIT** — faptul principal al cheii (['5.000 lei']) nu e in raspuns; articolul citat [('cf', '28')] nu e printre cele ale cheii [('cf', '45'), ('cf', '6')]

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Niciunul dintre atomii primiți nu conține regula privind pragul valoric de încadrare a unui bun ca mijloc fix amortizabil (nici valoarea de 5.000 lei, nici o dispoziție tranzitorie privind mijloacele fixe intrate anterior majorării pragului și amortizate parțial). Atomii disponibili se referă la înlocuirea de părți componente ale mijloacelor fixe, la regimurile de amortizare (liniar, degresiv, accelerat), la reglementări contabile, la ajustări de TVA pentru bunuri de capital…

## Cheia

- Nu. Valoarea fiscală rămasă neamortizată a mijloacelor fixe cu valoare de intrare între 2.500 și 5.000 lei existente la 31.12.2025 se recuperează în continuare pe durata normală de utilizare rămasă.
- temei: Legea 227/2015 art. 45 alin. (21^3), introdus de OUG 8/2026 art. 6 pct. 14
