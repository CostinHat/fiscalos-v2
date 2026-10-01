# -*- coding: utf-8 -*-
"""PROBE pentru urmarirea legilor (punctul 8): ce declanseaza propunerea urmatoare si ce nu.
Proba completa (copie de test, cota simulata, saptamana fara schimbari) e `fiscalos.urmarire_proba`."""
import json
import os

from fiscalos import urmarire

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _p(par, cls, val, atom, verb, cod="0.16"):
    return {"parametru": par, "clasificare": cls, "valoare_lege": val, "atom": atom, "atom_verbatim": verb,
            "valoare_cod": cod, "unde_in_cod": "core/x.py:1"}


def test_aceeasi_stare_nu_declanseaza_nimic():
    v = [_p("a", "CONCORDA", "16%", "cf#art17", "este de 16%"), _p("b", "DIFERA", "9", "cf#art1", "9 zile")]
    assert urmarire.compara_potriviri(v, [dict(x) for x in v]) == []


def test_DIFERA_vechi_neschimbat_nu_redeclanseaza():
    v = [_p("b", "DIFERA", "9", "cf#art1", "9 zile")]
    assert urmarire.compara_potriviri(v, [dict(v[0])]) == []


def test_cota_schimbata_e_DIFERA_nou_cu_ambele_parti():
    v = [_p("a", "CONCORDA", "16%", "cf#art17", "este de 16%")]
    n = [_p("a", "DIFERA", "18", "cf#art17", "este de 18%")]
    s = urmarire.compara_potriviri(v, n)
    assert s[0]["motive"] == ["DIFERA nou", "temei schimbat"]
    assert s[0]["valoare_cod"] == "0.16" and s[0]["verbatim"] == "este de 18%"
    assert s[0]["verbatim_anterior"] == "este de 16%"


def test_temei_mutat_pe_alt_atom_e_semnalat_chiar_daca_valoarea_concorda():
    v = [_p("a", "NEVERIFICAT", "16%", "cf#art17", "este de 16%")]
    n = [_p("a", "NEVERIFICAT", "16%", "hg#anexa/pct6", "(16% x rd. 1)")]
    assert urmarire.compara_potriviri(v, n)[0]["motive"] == ["temei schimbat"]


def test_parametru_nou_sau_disparut_e_raportat_fara_a_declansa():
    v = [_p("a", "CONCORDA", "16%", "cf#art17", "x")]
    n = [_p("c", "CONCORDA", "10%", "cf#art84", "y")]
    m = sorted(m for s in urmarire.compara_potriviri(v, n) for m in s["motive"])
    assert m == ["parametru disparut din iConta", "parametru nou in iConta"]


def test_proba_8d_in_copia_de_test():
    """Rezultatul comis al probei: saptamana fara schimbari -> "nimic schimbat"; cota simulata -> DIFERA."""
    r = json.load(open(os.path.join(_RAD, "urmarire", "proba", "rezultat_proba.json"), encoding="utf-8"))
    assert r["verdict"] == {"A_nimic_schimbat": True, "B_DIFERA_in_propunere": True, "depozitul_real_neatins": True}
    assert r["A"]["rezumat"].startswith("nimic schimbat")


class _PortalCuCaderi(object):
    def __init__(self, cad_pana_la):
        self.n, self.cad = 0, cad_pana_la

    def act(self, i):
        self.n += 1
        if i == "2" and self.n < self.cad:
            raise OSError("timed out")
        return b"", {"consolidare_curenta": "01.01.2026"}


_MAN = {"acte": {a: {"id_portal": i, "de_ce": "x", "data_formei_consolidate": "01.01.2026",
                     "fisiere": [{"consolidare": "01.01.2026"}]} for a, i in (("a", "1"), ("b", "2"))}}


def test_actul_cazut_se_reia_o_data_si_altfel_ramane_NEVERIFICAT():
    assert urmarire.forme_noi(_PortalCuCaderi(3), _MAN, 0) == ({}, {}, 2)          # reluarea reuseste
    s, e, v = urmarire.forme_noi(_PortalCuCaderi(4), _MAN, 0)                       # cade si la reluare
    assert s == {} and list(e) == ["b"] and v == 1


def test_rezumatul_nu_spune_nimic_schimbat_pentru_toate_cand_unele_n_au_fost_verificate():
    r = {"forme_noi": {}, "schimbari_pentru_iconta": [], "acte_verificate": 59, "acte_urmarite": 61,
         "neverificate": {"x": "timeout", "y": "timeout"}, "iconta_schimbat_de_la_ultima_comparatie": False}
    t = urmarire._rezumat(r, [])
    assert "în cele 59 acte verificate (din 61)" in t and "NEVERIFICATE" in t and "toate" not in t
