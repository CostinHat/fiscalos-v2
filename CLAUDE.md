# FiscalOS v2 — reguli

Proiect separat de iConta. Arhitect: Claude (alt chat). Direcția: Costin. Executor: Claude Code.

Vechiul FiscalOS (C#) s-a blocat în ~460 de tichete de arhitectură. Păstrăm **ideile**
(atomizare structurală, bi-temporalitate, slice micro), nu **metoda**.

**Principiu de extracție:** extragem ce e cerut, nu tot actul. *Structura* întregului act se
atomizează automat; *conținutul* treptat, la cerere.

---

## 1. Corpusul (regula 2)

Corpusul = **instantaneu copiat** din `anaf_surse` al iConta (`~/iconta_nou/anaf_surse`), cu
**manifest SHA256** per fișier (`corpus_manifest.json`).

> **Nu se scrie NIMIC, niciodată, în `~/iconta_nou`. Doar citire.**

Asta e o interdicție, nu o preferință: iConta e sistem în producție, iar orice atingere a lui
dintr-un proiect care îl *auditează* ar strica exact independența care face auditul util. Codul care
citește iConta deschide fișierele în `"r"` și nu are nicio cale de scriere spre acel prefix.

Instantaneul trăiește în `corpus/` și **nu intră în git** (126 MB de acte publice, reproductibile).
Ce intră în git e manifestul — el e proba că un atom citat a fost extras din *acel* octet.

## 2. Nicio valoare inventată (regula 5)

- Dacă valoarea nu e în corpus → **NEGĂSIT**. Nu se completează din memorie, din alt sistem sau
  prin raționament plauzibil.
- Fiecare **CONCORDĂ** / **DIFERĂ** citează **id-ul atomului** și **fragmentul verbatim**.
- Fiecare **DIFERĂ** arată **ambele părți**: valoarea din codul iConta *și* textul legii.
- Tăcerea nu se citește ca absență: un act neextractibil (PDF XFA, scan fără OCR) se raportează
  ca *neextractibil*, nu ca *negăsit* — altfel o limită a uneltei ar trece drept o limită a legii.

## 3. Rezultatul e o PROPUNERE (regula 6)

Fiecare livrabil e un **pachet versionat de propunere**: JSON (mecanic) + raport lizibil (om),
sub `propuneri/vN/`, cu **aprobare umană**.

> **Nu se aplică niciodată automat în iConta.** FiscalOS nu are cale de scriere spre iConta.

## 4. Fără tichete în avans (regula 8)

Fără tichete de arhitectură și fără contracte scrise înainte de folosire. Fiecare pas produce
**o bucată care rulează și e dovedită pe corpus**. Dacă un pas nu poate fi dovedit pe corpus,
nu e un pas — e o intenție, și stă în raport la secțiunea „0. CERINȚE", nu în cod.
