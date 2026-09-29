# -*- coding: utf-8 -*-
"""PROBA interdicţiei din CLAUDE.md §1: FiscalOS nu scrie NIMIC in ~/iconta_nou.

DE CE NU SE VERIFICA "nimic nu s-a schimbat in iconta_nou". Serviciul iConta RULEAZA (systemd
`iconta-nou`, activ) si isi scrie singur jurnalele - `alerta_acces.log`, `sonda_web.log`,
`.poarta_jurnal.log` cresc in permanenta. Un test care cere arborele neschimbat ar cadea din cauza
lui, nu din cauza noastra, si ar fi dezactivat in trei zile.

Ce se verifica sunt cele doua lucruri care ne privesc:
  1. GARDUL refuza mecanic orice cale sub prefixul interzis - inclusiv prin legatura simbolica;
  2. FISIERELE PE CARE LE CITIM sunt neatinse.

Observaţie din sesiunea de generare, pastrata fiindca era gata sa fie citita greșit: un `.pyc` NOU a
apărut in `iconta_nou/__pycache__` in timpul lucrului. Nu e al nostru - e un cache de PYTEST, iar
pytest nu exista in interpretorul de sistem folosit aici (exista numai in `iconta_nou/venv`), si e
pentru un modul pe care nu l-am deschis niciodata (`test_decontari_asociati`). Inventarul nu importa
NICIODATA cod iConta, tocmai ca sa nu poata scrie bytecode in arborele lor: citeste sursa si o trece
prin `ast.parse`.
"""
import os

from fiscalos import corpus_snapshot as cs

# fisierele din iConta pe care inventarul le CITESTE
CITITE = ("core/common.py", "core/scadente.py", "core/nomenclatoare.py")


def test_gardul_refuza_scrierea_sub_iconta():
    for cale in ("/home/costin/iconta_nou", "/home/costin/iconta_nou/core/common.py",
                 "/home/costin/iconta_nou/anaf_surse/x.txt", "/home/costin/iconta_nou/../iconta_nou/z"):
        try:
            cs._refuza_scrierea(cale)
        except PermissionError:
            continue
        raise AssertionError("gardul a lasat sa treaca %r" % cale)


def test_gardul_lasa_sa_treaca_propriul_arbore():
    rad = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cs._refuza_scrierea(os.path.join(rad, "corpus"))
    cs._refuza_scrierea(os.path.join(rad, "artefacte", "x.json"))


def test_inventarul_nu_importa_cod_iconta():
    """Un `import core.common` ar scrie __pycache__ in arborele lor. Deci nu exista in sursa noastra.

    Se verifica prin AST, nu prin caut de text: prima versiune caăuta sirul "import core" si se
    prindea pe PROPRIUL docstring, care explica de ce importul e interzis. O proba care nu distinge
    codul de comentariul despre cod nu masoara nimic.
    """
    import ast
    rad = os.path.dirname(os.path.abspath(__file__))
    for nume in sorted(os.listdir(rad)):
        if not nume.endswith(".py"):
            continue
        arb = ast.parse(open(os.path.join(rad, nume), encoding="utf-8").read())
        for n in ast.walk(arb):
            if isinstance(n, ast.Import):
                for al in n.names:
                    assert al.name.split(".")[0] != "core", (nume, al.name)
            elif isinstance(n, ast.ImportFrom):
                assert (n.module or "").split(".")[0] != "core", (nume, n.module)


def test_fisierele_citite_din_iconta_sunt_neatinse():
    """Decizia dupa pasul 10: FiscalOS citeste NUMAI starea COMISA a iConta (git HEAD). Copia de lucru
    poate avea modificari necomise (e lucrul lor in curs), deci mtime-ul ei nu mai e proba. Proba e:
    inventarul si corpusul inregistreaza commitul din care au citit, iar fiecare fisier citit e exact
    obiectul git de la acel commit - FiscalOS n-a citit (si n-a scris) nimic in afara lui."""
    import json
    from fiscalos import iconta_head
    rad = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    inv = json.load(open(os.path.join(rad, "artefacte", "inventar_iconta.json"), encoding="utf-8"))
    la = inv["iconta_commit_git"]
    for rel in CITITE:
        assert iconta_head.citeste(rel, la)                   # obiectul exista la commitul inregistrat
    man = json.load(open(os.path.join(rad, "corpus_manifest.json"), encoding="utf-8"))
    obiecte = {r: sha for r, sha, _o in iconta_head.fisiere("anaf_surse", man["sursa_commit_git"])}
    assert {r: v["blob_git"] for r, v in man["fisiere"].items()} == obiecte


def test_inventarul_citeste_numai_prin_git_head():
    """Nicio citire directa din copia de lucru iConta: fara open()/listdir pe calea ICONTA."""
    import ast
    rad = os.path.dirname(os.path.abspath(__file__))
    for nume in ("inventar_iconta.py", "corpus_snapshot.py"):
        arb = ast.parse(open(os.path.join(rad, nume), encoding="utf-8").read())
        for n in ast.walk(arb):
            if isinstance(n, ast.Call) and getattr(n.func, "attr", getattr(n.func, "id", "")) in ("open", "listdir", "walk", "copy2"):
                txt = ast.dump(n)
                assert "ICONTA" not in txt and "SURSA" not in txt and "sursa" not in txt, (nume, txt[:120])


def test_corpusul_sursa_are_aceleasi_amprente_ca_instantaneul():
    """Dupa toata lucrarea, sursa trebuie sa dea inca hash-urile din manifest."""
    import json
    import random
    rad = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    man = json.load(open(os.path.join(rad, "corpus_manifest.json"), encoding="utf-8"))
    nume = sorted(man["fisiere"])
    random.seed(7)
    # sursa = obiectul git de la commitul inregistrat (starea comisa), nu copia de lucru
    import hashlib
    from fiscalos import iconta_head
    for rel in random.sample(nume, 25):
        octeti = iconta_head.blob(man["fisiere"][rel]["blob_git"])
        assert hashlib.sha256(octeti).hexdigest() == man["fisiere"][rel]["sha256"], rel
