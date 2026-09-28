# -*- coding: utf-8 -*-
"""PROBA pe corpus a atomizarii (CLAUDE.md §4: fiecare pas produce o bucata DOVEDITA pe corpus).

Fiecare caz de aici a fost un DEFECT REAL, gasit privind atomii, nu presupus:
  - `legea_207` isi pierdea tot corpul primului articol din fiecare titlu (cuprinsul inghitea capul);
  - `legea_141_2025` se opria la punctul 25 din 50 (articolul citat golea stiva);
  - `D112_XML` trecea drept act cu text, desi pdftotext scosese placeholderul Acrobat.
Testul nu apara o teorie despre parser, ci cele patru masuratori care l-au corectat.
"""
import json
import os

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _atomi(act):
    cale = os.path.join(_RAD, "artefacte", "atomi", act.replace("/", "__") + ".jsonl")
    return {a["id"]: a for a in (json.loads(l) for l in open(cale, encoding="utf-8"))}


def test_cota_tva_standard_e_un_atom_cu_valabilitate():
    """Cota de 21% trebuie sa fie CITABILA: un id, textul verbatim, data de intrare, actul."""
    a = _atomi("cod_fiscal_227_2015_consolidat")["cod_fiscal_227_2015_consolidat#art291/alin1"]
    assert "21%" in a["text"], a["text"][:200]
    assert "Cota standard" in a["text"]
    assert a["valabil_din"] == "2025-08-01", a["valabil_din"]
    assert any("141" in m["nota"] for m in a["modificat_de"]), a["modificat_de"]
    assert a["abrogat"] is False


def test_alineatul_abrogat_rămâne_atom():
    """Un alineat abrogat NU se sterge: altfel o valoare cautata in el ar da tacere, nu abrogare."""
    a = _atomi("cod_fiscal_227_2015_consolidat")["cod_fiscal_227_2015_consolidat#art291/alin3"]
    assert a["abrogat"] is True
    assert a["valabil_din"] == "2025-08-01"


def test_articolul_din_corp_nu_e_inghitit_de_cuprins():
    """legea_207 (forma static.anaf.ro): `ART. 1 Definiții` e urmat de 51 de definitii, nu de gol."""
    ats = _atomi("legea_207_2015_consolidat")
    art1 = ats["legea_207_2015_consolidat#art1"]
    assert "termenii și expresiile" in art1["text"], art1["text"][:120]
    copii = [a for a in ats.values() if a["parinte"] == art1["id"]]
    assert len(copii) >= 40, len(copii)


def test_punctele_actului_modificator_sunt_complete_si_nu_se_rup_la_citat():
    """Art. II al Legii 141/2025 are 50 de puncte, numerotate 1..50, fara gauri."""
    ats = _atomi("legea_141_2025")
    pct = [a for a in ats.values()
           if a["nivel"] == "punct" and a["parinte"] == "legea_141_2025#artII"]
    chei = sorted(int(a["cheie"]) for a in pct)
    assert chei == list(range(1, 51)), chei


def test_temeiul_citat_de_iconta_pentru_tva_exista_ca_atom():
    """iConta citeaza `Art.II pct.42` din Legea 141/2025. Atomul trebuie sa existe si sa spuna 21%."""
    a = _atomi("legea_141_2025")["legea_141_2025#artII/pct42"]
    assert "articolul 291" in a["text"]
    assert "21%" in a["text"], a["text"][:300]


def test_articolul_citat_se_cuibareste_sub_punct_nu_langa_el():
    """`Art. 1577` introdus de pct. 25 e CONTINUTUL punctului, deci id-ul lui trece prin pct25."""
    ats = _atomi("legea_141_2025")
    citate = [i for i in ats if "/pct25/art" in i]
    assert citate, [i for i in ats if "art157" in i][:5]


def test_formularele_xfa_sunt_neextractibile_nu_negasite():
    """CLAUDE.md §2: o limita a UNELTEI se raporteaza ca atare, nu ca absenta din lege."""
    st = json.load(open(os.path.join(_RAD, "artefacte", "strat_text.json"), encoding="utf-8"))
    assert "D112_XML_2026_0726_050826" in st["neextractibile"]
    assert "XFA" in st["neextractibile"]["D112_XML_2026_0726_050826"]["motiv"]
    assert "D112_XML_2026_0726_050826" not in st["acte"]


def test_manifestul_acopera_fiecare_act_atomizat():
    """Un id de atom trebuie sa duca la OCTETI: actul lui e in manifestul SHA."""
    man = json.load(open(os.path.join(_RAD, "corpus_manifest.json"), encoding="utf-8"))
    st = json.load(open(os.path.join(_RAD, "artefacte", "strat_text.json"), encoding="utf-8"))
    for baza, v in st["acte"].items():
        assert v["din"] in man["fisiere"], (baza, v["din"])
