# -*- coding: utf-8 -*-
"""OP2 — INSTANTANEU al corpusului, cu manifest SHA256.

DE CE UN INSTANTANEU si nu o citire directa din iConta. Un atom citat trebuie sa fie reproductibil:
daca FiscalOS ar citi live din `~/iconta_nou/anaf_surse`, un atom extras azi si un act reimprospatat
maine ar da acelasi id pentru doua texte diferite, iar citarea ar minti fara sa se vada. Manifestul
SHA256 leaga id-ul atomului de octetii din care a ieist.

DE CE MANIFESTUL INTRA IN GIT SI SNAPSHOTUL NU. Snapshotul e 126 MB de acte publice, reproductibil
din sursa. Manifestul e 726 de linii care nu se pot reface daca sursa se schimba - deci el e proba.

INTERDICTIE (CLAUDE.md §1): nimic nu se scrie in ~/iconta_nou. Sursa se deschide numai la citire;
`_CITIRE_DOAR` e verificata inainte de orice operatie de copiere, ca regula sa fie mecanica, nu o
promisiune din comentariu.
"""
import hashlib
import json
import os
import shutil
import time

SURSA = "/home/costin/iconta_nou/anaf_surse"
_CITIRE_DOAR = ("/home/costin/iconta_nou",)   # prefixe INTERZISE la scriere


def _refuza_scrierea(cale):
    """Gard mecanic pentru CLAUDE.md §1. Ridica daca `cale` ar cadea sub un prefix read-only."""
    real = os.path.realpath(cale)
    for p in _CITIRE_DOAR:
        if real == os.path.realpath(p) or real.startswith(os.path.realpath(p) + os.sep):
            raise PermissionError(
                "REFUZ: %s cade sub prefixul read-only %s (CLAUDE.md §1). "
                "FiscalOS nu scrie niciodata in iConta." % (real, p))


def sha256(cale, buf=1 << 20):
    h = hashlib.sha256()
    with open(cale, "rb") as f:                      # "rb": citire, niciodata scriere
        for bloc in iter(lambda: f.read(buf), b""):
            h.update(bloc)
    return h.hexdigest()


def instantaneu(sursa=SURSA, dest=None, manifest=None):
    """Scrie instantaneul corpusului din starea COMISA a iConta (git HEAD) in dest si manifestul.

    Decizia arhitectului dupa pasul 10: FiscalOS citeste numai starea comisa - o modificare necomisa din
    copia de lucru nu e starea iConta. Fisierele se iau ca obiecte git (`ls-tree` + `cat-file`), nu din
    arborele de lucru; manifestul inregistreaza commitul si, pentru fiecare fisier, blob-ul git."""
    from fiscalos import iconta_head
    rad = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dest = dest or os.path.join(rad, "corpus")
    manifest = manifest or os.path.join(rad, "corpus_manifest.json")
    _refuza_scrierea(dest)
    _refuza_scrierea(manifest)
    prefix = os.path.relpath(sursa, iconta_head.ICONTA)
    la = iconta_head.commit()
    if os.path.isdir(dest):
        shutil.rmtree(dest)                          # propriul nostru director, nu iConta
    fisiere = {}
    for rel, sha_git, octeti in iconta_head.fisiere(prefix, la):
        dst = os.path.join(dest, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, "wb") as f:
            f.write(iconta_head.blob(sha_git))
        fisiere[rel] = {"sha256": sha256(dst), "octeti": octeti, "blob_git": sha_git}
    man = {
        "_ce": "Manifestul instantaneului de corpus FiscalOS v2. Leaga fiecare id de atom de octetii "
               "din care a fost extras.",
        "sursa": sursa,
        "sursa_mod": "DOAR CITIRE (CLAUDE.md §1), numai starea COMISA (git HEAD)",
        "sursa_commit_git": la,
        "luat_la": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "n_fisiere": len(fisiere),
        "octeti_total": sum(v["octeti"] for v in fisiere.values()),
        "fisiere": fisiere,
    }
    with open(manifest, "w", encoding="utf-8") as f:
        json.dump(man, f, ensure_ascii=False, indent=1, sort_keys=True)
    return man


if __name__ == "__main__":
    t0 = time.time()
    m = instantaneu()
    print("instantaneu: %d fisiere, %.1f MB, %.1f s" %
          (m["n_fisiere"], m["octeti_total"] / 1e6, time.time() - t0))
