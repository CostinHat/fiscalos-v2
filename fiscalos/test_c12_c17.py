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


def test_C19_opanaf_3769_compus_ordin_oficial_si_anexe_din_instantaneu():
    """C19: textul ordinului din sursa oficiala, anexele din instantaneu; fiecare parte cu data ei."""
    from fiscalos import potrivire
    c = potrivire.Corpus()
    assert c.sursa_act["opanaf_3769_2015_d394_baza"]["sursa"].startswith("compus")
    ats = c.pe_act["opanaf_3769_2015_d394_baza"]
    assert {a["parte"] for a in ats} == {"textul ordinului (oficial)",
                                          "anexe (instantaneu iConta, forma de baza)"}
    assert all(a.get("data_formei") for a in ats)
    assert sum(1 for a in ats if a["parte"].startswith("anexe")) == 91
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


def test_V2_notele_nu_mai_rup_structura_codului():
    """V2 reparat la radacina: nota "Articolul III din OG 22/2025 prevede: (1)...(6)" din mijlocul
    art. 310 rupea articolul - alineatele (3)-(6^2) se lipeau de un pseudo-articol "III". Acum nota e
    un rand marcat, atasat atomului curent, iar art. 310 isi are toate alineatele."""
    from fiscalos import potrivire
    c = potrivire.Corpus()
    cf = c.pe_act["cod_fiscal_227_2015_consolidat"]
    assert not any(a.get("nota_tranzitorie") for a in cf)
    alin = [a["cheie"] for a in cf if a["id"].startswith("cod_fiscal_227_2015_consolidat#art310/")
            and a["nivel"] == "alineat"]
    for k in ("1", "2", "3", "4", "5", "6", "6^1", "6^2"):
        assert k in alin, (k, alin)
    assert any("⟦NOTĂ⟧" in a["text"] for a in cf)
    r = json.load(open(os.path.join(_RAD, "artefacte", "potriviri.json"), encoding="utf-8"))
    for p in r["potriviri"]:
        t = p.get("temei_candidat")
        if t:
            assert not c.dupa_id.get(t["atom"], {}).get("nota_tranzitorie"), p["parametru"]


def test_V2_derogarea_citata_in_nota_nu_e_a_atomului_gazda():
    from fiscalos import potrivire, relatii
    c = potrivire.Corpus()
    r = relatii.Relatii(c)
    for e in r.muchii:
        s0 = c.dupa_id[e["sursa"]]["text"].split("⟦NOTĂ⟧")[0]
        assert e["fragment"][:30] in " ".join(s0.split()), e["sursa"]


def test_C18_candidatul_ambiguu_are_optiuni_si_nivel_comun():
    r = json.load(open(os.path.join(_RAD, "artefacte", "potriviri.json"), encoding="utf-8"))
    n = 0
    for p in r["potriviri"]:
        t = p.get("temei_candidat")
        if t and t.get("ambiguu"):
            n += 1
            assert len(t["optiuni"]) > 1
            assert all(o["atom"].startswith(t["atom"] + "/") for o in t["optiuni"]), p["parametru"]
    assert n > 0
