# -*- coding: utf-8 -*-
"""PROBE pentru C12 (surse oficiale), C17 (relatia de derogare) si defectul V1 al verificatorului."""
import hashlib
import json
import os
import subprocess

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_C12_fiecare_act_adus_are_SHA_data_si_provenienta_si_fisierele_sunt_intacte():
    man = json.load(open(os.path.join(_RAD, "surse_oficiale", "MANIFEST.json"), encoding="utf-8"))
    assert man["sursa"] == "https://legislatie.just.ro"
    for act, v in man["acte"].items():
        assert v["data_formei_consolidate"], act
        for x in v["fisiere"]:
            b = open(os.path.join(_RAD, "surse_oficiale", x["fisier"]), "rb").read()
            assert hashlib.sha256(b).hexdigest() == x["sha256"], x["fisier"]
            assert x["url"].startswith("https://legislatie.just.ro/Public/"), x["url"]


def test_C12_instantaneul_iconta_ramane_neatins():
    """Stratul oficial nu scrie in corpus/ si nu atinge artefacte/atomi/ (atomii instantaneului)."""
    d = subprocess.run(["git", "diff", "--stat", "d7efc18", "--", "artefacte/atomi/",
                        "corpus_manifest.json"], cwd=_RAD, capture_output=True, text=True).stdout
    assert d == "", d


def test_C12_actul_oficial_mai_sarac_nu_inlocuieste_instantaneul():
    from fiscalos import potrivire
    c = potrivire.Corpus()
    assert c.sursa_act["opanaf_3769_2015_d394_baza"]["sursa"] == "instantaneu iConta"
    assert c.sursa_act["legea_70_2015_consolidat"]["sursa"].startswith("oficial")
    assert len(c.pe_act["legea_70_2015_consolidat"]) >= 50      # instantaneul avea 1 atom


def test_C17_relatia_gaseste_exceptia_care_a_motivat_decizia():
    """CF art. 41 alin. (10^1): "Prin exceptie de la prevederile alin. (8), plata anticipata..."."""
    from fiscalos import potrivire, relatii
    c = potrivire.Corpus()
    r = relatii.Relatii(c)
    tinta = c.dupa_id["cod_fiscal_227_2015_consolidat#art41/alin8"]
    surse_ = [e["sursa"] for e in r.asupra(tinta, "2026-09-28")]
    assert "cod_fiscal_227_2015_consolidat#art41/alin10^1" in surse_, surse_


def test_C17_textul_istoric_nu_deroga():
    from fiscalos import potrivire, relatii
    r = relatii.Relatii(potrivire.Corpus())
    assert not any("forma_initiala" in e["sursa"] or "_pre_" in e["sursa"] for e in r.muchii)


def test_V1_identificatorul_de_act_nu_e_valoare():
    from fiscalos import semantic
    atom = {"id": "cf#art41/alin10^1", "act": "cod_fiscal_227_2015_consolidat", "valabil_din": None,
            "text": "Prin excepție de la prevederile alin. (8), plata anticipată pentru trimestrul I "
                    "se determină prin aplicarea cotei de impozit asupra profitului contabil."}
    out = {"stare": "RASPUNS", "declaratie": "x", "lipsa": [], "motiv": "", "derogari_tratate": [],
           "raspuns": "Prin aplicarea cotei asupra profitului; se declară pe formularul din OPANAF 587/2016.",
           "citate": [{"atom": atom["id"], "fragment": "plata anticipată pentru trimestrul I se "
                                                       "determină prin aplicarea cotei de impozit"}]}
    assert semantic.verifica(out, [atom], "Cum se calculează plata anticipată?", "2026-09-28") == []


def test_intrebari_v2_ramane_neatins():
    d = subprocess.run(["git", "diff", "d7efc18", "--", "intrebari/v2/"], cwd=_RAD,
                       capture_output=True, text=True).stdout
    assert d == "", d[:300]


def test_propunerea_v3_ramane_neatinsa_si_v4_listeaza_actele_aduse():
    d = subprocess.run(["git", "diff", "d7efc18", "--", "propuneri/v3/"], cwd=_RAD,
                       capture_output=True, text=True).stdout
    assert d == "", d[:300]
    aa = json.load(open(os.path.join(_RAD, "propuneri", "v4", "acte_aduse.json"), encoding="utf-8"))
    assert len(aa["acte"]) == 6 and all(x["fisiere"][0]["sha256"] for x in aa["acte"])
