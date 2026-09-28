# -*- coding: utf-8 -*-
"""PROBE pentru motorul de intrebari: orb la cheie, niciodata raspuns fara atom."""
import ast
import json
import os

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_INTERZISE = ("raspuns_asteptat", "verificare")


def test_motorul_nu_poate_citi_coloanele_cheii():
    """Nici ca sir literal, nici ca cheie: `raspuns_asteptat`, `verificare` si coloana `temei` a CSV-ului
    nu apar in motor. Coloana `temei` se verifica pe contextul CSV (cheia de dict pe randul citit),
    fiindca cuvantul "temei" e si vocabularul propriu al motorului."""
    src = open(os.path.join(_RAD, "fiscalos", "intrebari.py"), encoding="utf-8").read()
    arb = ast.parse(src)
    for n in ast.walk(arb):
        if isinstance(n, ast.Constant) and isinstance(n.value, str):
            for c in _INTERZISE:
                assert c not in n.value, (c, n.value[:80])
    from fiscalos import intrebari
    assert intrebari.COLOANE_PERMISE == ("id", "tip", "intrebare")
    for q in intrebari.incarca_intrebari():
        assert set(q) == {"id", "tip", "intrebare"}, set(q)


def test_niciun_raspuns_fara_atom():
    r = json.load(open(os.path.join(_RAD, "artefacte", "intrebari", "raspunsuri.json"),
                       encoding="utf-8"))
    for x in r["raspunsuri"]:
        if x["stare"] == "RASPUNS":
            assert x["argument"], x["id"]
            for a in x["argument"]:
                assert a["atom"] and a["verbatim"] and a["temei"], (x["id"], a)
        else:
            assert x["motiv"], x["id"]


def test_fiecare_raspuns_declara_valabilitatea_la_data_intrebarii():
    r = json.load(open(os.path.join(_RAD, "artefacte", "intrebari", "raspunsuri.json"),
                       encoding="utf-8"))
    for x in r["raspunsuri"]:
        if x["stare"] == "RASPUNS":
            assert x["data_referinta"], x["id"]
            v = x["argument"][0]["valabilitate"]
            assert "valabil_din" in v and "la_data_intrebarii" in v, (x["id"], v)
            if v["la_data_intrebarii"] is False:
                raise AssertionError("raspuns pe un atom care nu era in vigoare: %s" % x["id"])


def test_citatul_verbatim_e_chiar_in_atom():
    """Fragmentul citat trebuie sa fie literal in textul atomului - altfel e o afirmaţie, nu o proba."""
    from fiscalos import potrivire
    c = potrivire.Corpus()
    r = json.load(open(os.path.join(_RAD, "artefacte", "intrebari", "raspunsuri.json"),
                       encoding="utf-8"))
    for x in r["raspunsuri"]:
        for a in x["argument"]:
            txt = c.dupa_id[a["atom"]]["text"]
            v = a["verbatim"].strip("…")
            assert v in txt, (x["id"], a["atom"])
