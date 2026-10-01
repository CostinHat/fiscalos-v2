# FiscalOS v2 — Pasul 12 (partea A): închiderea reglajului

Generat 01.10.2026 17:08 · ZIP: `/home/costin/ghid_incoming/fiscalos_v11_rezultat.zip`

> Fără rulare plătită. **Reglajul motorului se închide aici** (decizia 6). Efectele care cer modelul (C58, răspunsul condiționat) se văd numai la o rulare viitoare.

## 0. CERINȚE — decizii de arhitect, aplicate

| | Decizia | Cum e aplicată | Dovada |
|---|---|---|---|
| **C58** | C40 nu mai respinge direct: un termen dat fără `termen_efectiv` declanșează tura de reparație; respingerea rămâne numai dacă nici reparația nu-l calculează | aceeași tură unică de reparație ca C52 (cifre + termene, un singur mesaj); mesajul numește termenele și cere `termen_efectiv` | `test_navigare.test_C58_*` (client simulat: termenul respins → reparație → răspuns acceptat) |
| **C59** | comparatorul: „la mie”, zero spus ca „nu se ajustează”/„nu se datorează”, numerale în litere; re-notare separată | „N la mie” → N/10 %; „nu se ajustează” în lista de zero („nu (se) datorează” exista); numeral + unitate („două luni”) → cifră, la fel în cheie și în răspuns | `test_intrebari.test_C59_*` (ambele direcții) |
| **C60** | costul de $0,284/întrebare se acceptă | neschimbat | — |
| **C57** | nu se adoptă | neimplementată | — |
| **Q4-CPF-10** | răspunsul care depinde de fapte lipsă începe cu ce trebuie clarificat; o cifră numai ca exemplu marcat, după condiții | un răspuns cu `lipsa` nevidă devine INCOMPLET oricum l-ar marca modelul; textul condiționat se păstrează (`raspuns_conditionat`) numai dacă începe cu „De clarificat:” și nu are cifre înaintea marcajului „Exemplu”; regula e și în prompt | `test_navigare.test_raspunsul_conditionat_*` (ambele direcții) |

## C59 — re-notarea (scorurile oficiale nu se schimbă)

| Set | Corpus | Oficial | Re-notat (C59) | Schimbări |
|---|---|---|---|---|
| setul 2 | `8b3269f` | 30/5/15 | **30/5/15** | — |
| setul 3 | `024fab8` | 18/1/31 | **18/1/31** | — |
| setul 4 | `757af8a` | 36/6/8 | **38/4/8** | Q4-TVA-02 GRESIT→CORECT, Q4-TVA-08 GRESIT→CORECT, Q4-CTB-02 GRESIT→CORECT, Q4-CTB-09 CORECT→GRESIT |

Pe setul 4: Q4-TVA-02 („3 la mie”), Q4-TVA-08 („nu se ajustează”), Q4-CTB-02 („două luni”) devin CORECT. **Q4-CTB-09 devine GREȘIT** — notarea s-a făcut mai strictă: cheia spune „opt luni”, pe care comparatorul vechi nu-l citea ca fapt (verifica numai articolul); acum faptul principal e „8 luni”, iar răspunsul dă perioada prin date (01.02–30.09.2026), nu prin durată. Normalizarea se aplică la fel cheii și răspunsului.

## Operațiile, cu durata măsurată

| Operație | Durată | Cost |
|---|---|---|
| Re-notarea C59 pe seturile 2–4 (fiecare pe corpusul ei) | 5.9 s | $0 |
| Probe: 197 | ~7 min | $0 |
