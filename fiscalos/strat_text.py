# -*- coding: utf-8 -*-
"""OP3 — STRATUL DE TEXT: fiecare act din corpus primeste o redare in text simplu, sau un MOTIV.

DE CE UN STRAT SEPARAT si nu extragere la cerere in atomizator. Trei formate (txt/html/pdf) dau trei
clase de eroare diferite, iar amestecarea lor cu parsarea structurii ar face imposibil de spus daca
un articol lipsa e o limita a extractiei sau o limita a parserului. Aici se raspunde la o singura
intrebare: EXISTA text? Structura se discuta dupa.

PREFERINTA .txt CAND EXISTA. Pentru 163 din acte, iConta a pus deja langa .html un .txt extras cu
pdftotext/pandoc. Cand exista, il folosim: e mai putina transformare intre octetii amprentati si
textul citat, deci mai putin loc unde un fragment "verbatim" sa nu fie verbatim.

NEEXTRACTIBIL NU E NEGASIT (CLAUDE.md §2). Formularele XFA ale ANAF (D112, D311) nu dau text prin
pdftotext. Ele se scriu in `neextractibile` cu motivul, si acolo RAMAN vizibile: un parametru care
s-ar stabili numai intr-un act neextractibil trebuie sa iasa in raport ca limita a uneltei, nu ca
absenta din lege.
"""
import html as _html
import json
import os
import re
import subprocess
import time

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(_RAD, "corpus")
DEST = os.path.join(_RAD, "artefacte", "strat_text")

# extensii care NU sunt acte: amprente, schema, date structurate
_NEACTE = (".sha256", ".xsd", ".json", ".xml", ".xlsx", ".py", ".properties", ".SHA256")

_SCRIPT_STIL = re.compile(r"(?is)<(script|style)\b.*?</\1\s*>")
_BR = re.compile(r"(?i)<br\s*/?>")
_BLOC = re.compile(r"(?i)</(p|div|tr|li|h[1-6]|table|section)\s*>")
_TAG = re.compile(r"(?s)<[^>]+>")
_SPATII = re.compile(r"[ \t ]+")
_RANDURI = re.compile(r"\n{3,}")


def html_in_text(sursa_html):
    """HTML -> text, pastrand granitele de bloc ca randuri noi (structura articolelor trece prin ele)."""
    t = _SCRIPT_STIL.sub(" ", sursa_html)
    t = _BR.sub("\n", t)
    t = _BLOC.sub("\n", t)
    t = _TAG.sub(" ", t)
    t = _html.unescape(t)
    t = _SPATII.sub(" ", t)
    t = "\n".join(linie.strip() for linie in t.split("\n"))
    return _RANDURI.sub("\n\n", t).strip()


# Placeholderul pe care Acrobat il tipareste IN LOC de formular, cand corpul e XFA. Masurat pe
# D112/D311 din corpus: pdftotext scoate 676 de caractere de text REAL, deci pragul de lungime il
# lasa sa treaca drept act. Se recunoaste dupa fraza, nu dupa dimensiune - un act scurt (HG cu un
# singur articol) are tot dreptul la 700 de caractere.
_XFA = re.compile(r"(?i)if this message is not eventually replaced|"
                  r"your PDF viewer may not be able to display this type of document")


def _pdf_in_text(cale):
    """pdftotext. Intoarce (text, motiv). Formularele XFA dau placeholder Acrobat -> motiv, nu tacere."""
    try:
        r = subprocess.run(["pdftotext", "-enc", "UTF-8", cale, "-"],
                           capture_output=True, timeout=180)
    except (OSError, subprocess.TimeoutExpired) as e:
        return None, "pdftotext a esuat: %s" % e
    t = r.stdout.decode("utf-8", "replace").strip()
    if _XFA.search(t):
        return None, ("formular XFA: pdftotext a scos numai placeholderul Acrobat, nu corpul "
                      "formularului (%d caractere)" % len(t))
    if len(t) < 200:
        return None, ("pdftotext a intors %d caractere - probabil formular XFA sau scan fara OCR"
                      % len(t))
    return t, None


def construieste(corpus=CORPUS, dest=DEST):
    os.makedirs(dest, exist_ok=True)
    acte, neextractibile = {}, {}
    # gruparea pe RADACINA de nume: acelasi act poate avea .pdf + .txt + .html
    fisiere = []
    for dirpath, _d, filenames in os.walk(corpus):
        for n in sorted(filenames):
            fisiere.append(os.path.relpath(os.path.join(dirpath, n), corpus))
    radacini = {}
    for rel in fisiere:
        if rel.endswith(_NEACTE) or os.path.basename(rel) == "SHA256":
            continue
        baza, ext = os.path.splitext(rel)
        radacini.setdefault(baza, {})[ext.lower()] = rel

    for baza in sorted(radacini):
        forme = radacini[baza]
        text = motiv = None
        provenit_din = None
        # ordinea de preferinta: .txt (cea mai putina transformare) -> .html -> .pdf -> .md
        for ext in (".txt", ".md", ".html", ".htm", ".pdf"):
            if ext not in forme:
                continue
            cale = os.path.join(corpus, forme[ext])
            if ext in (".txt", ".md"):
                text = open(cale, encoding="utf-8", errors="replace").read().strip()
                if len(text) < 200:
                    text, motiv = None, "fisier .txt aproape gol (%d caractere)" % len(text)
                    continue
            elif ext in (".html", ".htm"):
                text = html_in_text(open(cale, encoding="utf-8", errors="replace").read())
                if len(text) < 200:
                    text, motiv = None, "html fara text util (%d caractere)" % len(text)
                    continue
            else:
                text, motiv = _pdf_in_text(cale)
                if text is None:
                    continue
            provenit_din = forme[ext]
            motiv = None
            break

        if text is None:
            neextractibile[baza] = {"forme": sorted(forme.values()),
                                    "motiv": motiv or "nicio forma cu text"}
            continue
        out = os.path.join(dest, baza + ".text")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
        acte[baza] = {"text": os.path.relpath(out, _RAD), "din": provenit_din,
                      "caractere": len(text), "randuri": text.count("\n") + 1,
                      "forme_disponibile": sorted(forme.values())}

    raport = {"_ce": "OP3 strat de text. `neextractibile` e o limita a UNELTEI, nu a legii "
                     "(CLAUDE.md §2).",
              "facut_la": time.strftime("%Y-%m-%dT%H:%M:%S"),
              "n_acte_cu_text": len(acte), "n_neextractibile": len(neextractibile),
              "acte": acte, "neextractibile": neextractibile}
    with open(os.path.join(_RAD, "artefacte", "strat_text.json"), "w", encoding="utf-8") as f:
        json.dump(raport, f, ensure_ascii=False, indent=1, sort_keys=True)
    return raport


if __name__ == "__main__":
    t0 = time.time()
    r = construieste()
    print("strat text: %d acte cu text, %d neextractibile, %.1f s"
          % (r["n_acte_cu_text"], r["n_neextractibile"], time.time() - t0))
    for b, v in sorted(r["neextractibile"].items()):
        print("  NEEXTRACTIBIL %-55s %s" % (b, v["motiv"]))
