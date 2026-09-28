# -*- coding: utf-8 -*-
"""PROBE pentru stratul de navigare (decizia 6) si calculul evaluat de cod (decizia 7) - fara model.

Calculul e locul unde un model ar putea strecura o valoare inventata sub forma unui operand. Deci se
proba cu formule construite anume sa pacaleasca verificatorul: operand fara sursa, valoare care nu e
in fragment, fragment parafrazat, cota luata din intrebare, constanta ascunsa in formula, apel de
functie nepermis.
"""
import ast
import os

from fiscalos import navigare

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ATOM = {"id": "cf#art291/alin1", "act": "cod_fiscal_227_2015_consolidat", "valabil_din": "2025-08-01",
        "text": "Cota standard se aplică asupra bazei de impozitare pentru operațiunile impozabile, "
                "iar nivelul acesteia este 21%."}
Q = "O firmă livrează bunuri de 10.000 lei la 15.03.2026, cu plata la 14.04.2026. Care e TVA-ul?"
V = {ATOM["id"]: ATOM}


def _op(nume, valoare, sursa, fragment, atom=""):
    return {"nume": nume, "valoare": valoare, "sursa": sursa, "atom": atom, "fragment": fragment}


def _tva(formula="baza * cota / 100", cota=None, baza=None):
    return [{"nume": "tva", "formula": formula, "operanzi": [
        baza or _op("baza", "10.000", "intrebare", "bunuri de 10.000 lei"),
        cota or _op("cota", "21", "atom", "nivelul acesteia este 21%", ATOM["id"])]}]


def test_calculul_corect_se_evalueaza_de_cod():
    val, gr, det = navigare.evalueaza_calcule(_tva(), V, Q)
    assert gr == [] and val == {"tva": "2.100"}, (gr, val)
    assert det[0]["formula"] == "baza * cota / 100"


def test_procentul_ca_procent():
    c = _op("cota", "21%", "atom", "nivelul acesteia este 21%", ATOM["id"])
    val, gr, _d = navigare.evalueaza_calcule(_tva("baza * cota", cota=c), V, Q)
    assert gr == [] and val == {"tva": "2.100"}, (gr, val)


def test_operand_din_atom_nearatat_e_respins():
    c = _op("cota", "21", "atom", "nivelul acesteia este 21%", "cf#art999")
    assert any("nu i-a fost aratat" in g for g in navigare.evalueaza_calcule(_tva(cota=c), V, Q)[1])


def test_valoarea_care_nu_e_in_fragment_e_respinsa():
    c = _op("cota", "19", "atom", "nivelul acesteia este 21%", ATOM["id"])
    assert any("nu apare literal" in g for g in navigare.evalueaza_calcule(_tva(cota=c), V, Q)[1])


def test_fragmentul_parafrazat_e_respins():
    c = _op("cota", "21", "atom", "cota standard este de 21%", ATOM["id"])
    assert any("verbatim" in g for g in navigare.evalueaza_calcule(_tva(cota=c), V, Q)[1])


def test_C13_cota_luata_din_intrebare_e_respinsa():
    q = Q + " Cota este de 21%."
    c = _op("cota", "21%", "intrebare", "Cota este de 21%")
    assert any("C13" in g for g in navigare.evalueaza_calcule(_tva("baza * cota", cota=c), V, q)[1])


def test_constanta_ascunsa_in_formula_e_respinsa():
    """0,21 scris direct in formula e o cota fara sursa."""
    gr = navigare.evalueaza_calcule(_tva("baza * 0.21"), V, Q)[1]
    assert any("constanta fara sursa" in g for g in gr), gr


def test_nume_fara_operand_e_respins():
    assert any("fara sursa" in g for g in navigare.evalueaza_calcule(_tva("baza * cota_tva"), V, Q)[1])


def test_functie_nepermisa_e_respinsa():
    assert navigare.evalueaza_calcule(_tva("__import__('os')"), V, Q)[1]


def test_zile_intre_doua_date_din_intrebare():
    c = [{"nume": "n", "formula": "zile(d1, d2)", "operanzi": [
        _op("d1", "15.03.2026", "intrebare", "la 15.03.2026"),
        _op("d2", "14.04.2026", "intrebare", "la 14.04.2026")]}]
    val, gr, _d = navigare.evalueaza_calcule(c, V, Q)
    assert gr == [] and val == {"n": "30"}, (gr, val)


def test_formatul_romanesc():
    assert navigare._format(1234567.5) == "1.234.567,50"
    assert navigare._numar("100.000")[0] == 100000 and navigare._numar("2,25%")[0] * 100 == 2.25


def test_schema_raspunsului_contine_calculele():
    assert "calcule" in navigare.SCHEMA["required"]
    assert [u["name"] for u in navigare.UNELTE] == ["cauta", "cuprins", "deschide", "raspunde"]


def test_navigarea_e_oarba_la_cheie():
    """Stratul de navigare nu citeste coloanele cu raspunsurile asteptate si nu importa comparatorul."""
    src = open(os.path.join(_RAD, "fiscalos", "navigare.py"), encoding="utf-8").read()
    arb = ast.parse(src)
    nume = {n.id for n in ast.walk(arb) if isinstance(n, ast.Name)} | \
        {a.name for n in ast.walk(arb) if isinstance(n, (ast.Import, ast.ImportFrom)) for a in n.names}
    assert "comparatie" not in nume
    assert "raspuns_asteptat" not in src and "Raspuns verificat" not in src and "csv" not in nume


def test_uneltele_arata_numai_atomi_in_vigoare():
    from fiscalos import intrebari
    idx = intrebari.Index()
    nav = navigare.Navigator(idx, idx.rel, "2016-01-01")
    viitor = next(a for a in idx.corp.toti if (a.get("valabil_din") or "") > "2020-01-01"
                  and a["act"] == "cod_fiscal_227_2015_consolidat")
    assert "eroare" in nav.deschide(viitor["id"])
    nav.cauta("cota standard TVA")
    nav.cuprins("cod_fiscal_227_2015_consolidat", "taxa pe valoarea adaugata cota")
    nav.deschide("cod_fiscal_227_2015_consolidat#art291")
    assert nav.vazuti and all(not a.get("valabil_din") or a["valabil_din"] <= "2016-01-01"
                              for a in nav.vazuti.values())
