# -*- coding: utf-8 -*-
"""Citirea iConta NUMAI din starea COMISA (git HEAD) - decizia arhitectului dupa pasul 10.

De ce: iConta e un sistem viu; copia de lucru poate avea modificari NECOMISE (masurat: `core/common.py`,
29.09.2026 21:55, +14 randuri). O modificare necomisa nu e starea iConta - e lucru in curs. FiscalOS
citeste deci numai obiectele din `git HEAD`, la un commit inregistrat in manifest.

Numai comenzi git care NU scriu: `rev-parse`, `ls-tree`, `cat-file`, cu `--no-optional-locks` (fara el,
chiar si o comanda de citire poate reimprospata indexul). Niciun `status`, niciun `checkout`.
"""
import os
import subprocess

ICONTA = "/home/costin/iconta_nou"
_ENV = dict(os.environ, GIT_OPTIONAL_LOCKS="0")


def _git(*arg, text=True):
    return subprocess.run(["git", "-C", ICONTA, "--no-optional-locks"] + list(arg), env=_ENV,
                          capture_output=True, text=text, check=True).stdout


def commit():
    """Commit-ul HEAD al iConta, la momentul citirii."""
    return _git("rev-parse", "HEAD").strip()


def fisiere(prefix, la=None):
    """[(cale_relativa_la_prefix, blob_sha, octeti)] - fisierele urmarite sub `prefix`, la commitul `la`."""
    ies = []
    for rand in _git("ls-tree", "-r", "-l", la or "HEAD", "--", prefix).splitlines():
        meta, cale = rand.split("\t", 1)
        _mod, tip, sha, octeti = meta.split()
        if tip == "blob":
            rel = cale[len(prefix):].lstrip("/") if cale.startswith(prefix) else cale
            ies.append((rel, sha, int(octeti)))
    return ies


def blob(sha):
    """Octetii unui obiect blob."""
    return _git("cat-file", "blob", sha, text=False)


def citeste(cale, la=None):
    """Textul unui fisier, asa cum e COMIS la `la` (implicit HEAD)."""
    return _git("show", "%s:%s" % (la or "HEAD", cale))
