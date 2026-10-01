# -*- coding: utf-8 -*-
"""PROBE pentru predarea catre iConta (INTEGRARE_ICONTA.md): modulul care intra in iConta NU apeleaza API-ul
platit si nu atinge motorul de intrebari sau pagina (inghetate)."""
import os
import subprocess
import sys

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODUL = ["corpus_snapshot", "strat_text", "atomizare", "surse", "portal", "surse_oficiale", "surse_oficiale_c31",
         "detector_structura", "iconta_head", "inventar_iconta", "potrivire", "relatii", "banc_mutatii",
         "propunere", "urmarire", "urmarire_proba"]
INGHETAT = ("anthropic", "fiscalos.semantic", "fiscalos.navigare", "fiscalos.intrebari", "fiscalos.pagina",
            "fiscalos.comparatie", "fiscalos.rulare_cu_reluare")


def test_modulul_nu_incarca_API_ul_platit_nici_motorul():
    cod = ("import sys, importlib\n"
           "for m in %r: importlib.import_module('fiscalos.' + m)\n"
           "print([x for x in %r if x in sys.modules])" % (MODUL, INGHETAT))
    o = subprocess.run([sys.executable, "-c", cod], cwd=_RAD, capture_output=True, text=True, timeout=300)
    assert o.returncode == 0, o.stderr[-2000:]
    assert o.stdout.strip().splitlines()[-1] == "[]", o.stdout


def test_modulul_nu_citeste_cheia_API():
    for m in MODUL:
        t = open(os.path.join(_RAD, "fiscalos", m + ".py"), encoding="utf-8").read()
        for interzis in ("anthropic", "api_keys", "sk-ant", "ANTHROPIC_API_KEY"):
            assert interzis not in t, (m, interzis)


def test_pagina_nu_mai_porneste_din_cron():
    """Decizia 5: pagina inghetata - nicio linie de cron nu o mai porneste; urmarirea ramane activa."""
    o = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
    if o.returncode != 0:                                   # alta masina, fara crontab: nimic de verificat
        return
    assert "pagina_porneste.sh" not in o.stdout
    assert "fiscalos.urmarire" in o.stdout
