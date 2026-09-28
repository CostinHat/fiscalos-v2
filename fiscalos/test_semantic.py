# -*- coding: utf-8 -*-
"""PROBE pentru verificatorul mecanic al stratului semantic - fara niciun apel la model.

Verificatorul e garantia intregului strat: modelul propune, codul decide. Daca verificatorul lasa sa
treaca un citat parafrazat sau o cifra inventata, stratul semantic nu mai e ancorat pe atomi. Deci
se proba cu propuneri construite anume sa-l pacaleasca.
"""
import ast
import os

from fiscalos import semantic

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ATOM = {"id": "cf#art291/alin1", "act": "cod_fiscal_227_2015_consolidat", "valabil_din": "2025-08-01",
        "text": "Cota standard se aplică asupra bazei de impozitare pentru operațiunile impozabile care "
                "nu sunt scutite de taxă sau care nu sunt supuse cotei reduse, iar nivelul acesteia "
                "este 21%."}
FRAG = "iar nivelul acesteia este 21%."
Q = "Care este cota standard de TVA aplicabilă în 2026?"


def _out(**kw):
    o = {"stare": "RASPUNS", "declaratie": "Data: 2026-09-28.", "raspuns": "21%",
         "citate": [{"atom": ATOM["id"], "fragment": FRAG}], "lipsa": [], "motiv": ""}
    o.update(kw)
    return o


def test_raspunsul_corect_si_verbatim_trece():
    assert semantic.verifica(_out(), [ATOM], Q, "2026-09-28") == []


def test_citatul_parafrazat_e_respins():
    o = _out(citate=[{"atom": ATOM["id"], "fragment": "nivelul cotei standard este de 21%."}])
    assert any("verbatim" in g for g in semantic.verifica(o, [ATOM], Q, "2026-09-28"))


def test_cifra_inventata_e_respinsa():
    """19% nu apare nici in citat, nici in intrebare: exact greşeala pe care o prinde bancul."""
    o = _out(raspuns="19%")
    assert any("19" in g for g in semantic.verifica(o, [ATOM], Q, "2026-09-28"))


def test_rezultatul_unui_calcul_e_respins():
    """Decizia C3: fara calcul. 100.000 x 21% = 21.000 nu e literal in niciun atom."""
    o = _out(raspuns="21.000 lei")
    assert semantic.verifica(o, [ATOM], "Cât TVA la 100.000 lei?", "2026-09-28")


def test_cifra_din_intrebare_e_permisa():
    o = _out(raspuns="Da, de la 14.05.2026 se aplică 21%")
    assert semantic.verifica(o, [ATOM], Q + " Pe 14.05.2026?", "2026-09-28") == []


def test_atom_care_nu_i_a_fost_dat_e_respins():
    o = _out(citate=[{"atom": "cf#art999", "fragment": FRAG}])
    assert any("nu i-a fost dat" in g for g in semantic.verifica(o, [ATOM], Q, "2026-09-28"))


def test_atom_care_nu_era_in_vigoare_e_respins():
    assert any("in vigoare" in g for g in semantic.verifica(_out(), [ATOM], Q, "2025-01-01"))


def test_incomplet_fara_faptele_lipsa_e_respins():
    o = _out(stare="INCOMPLET", raspuns="", lipsa=[])
    assert any("INCOMPLET" in g for g in semantic.verifica(o, [ATOM], Q, "2026-09-28"))


def test_raspuns_fara_citat_e_respins():
    assert semantic.verifica(_out(citate=[]), [ATOM], Q, "2026-09-28")


def test_stratul_semantic_e_orb_la_cheie():
    src = open(os.path.join(_RAD, "fiscalos", "semantic.py"), encoding="utf-8").read()
    for n in ast.walk(ast.parse(src)):
        if isinstance(n, ast.Constant) and isinstance(n.value, str):
            for c in ("raspuns_asteptat", "verificare\"", "temei_asteptat"):
                assert c not in n.value, c


# ── C13: valorile legale se dovedesc din atom, nu din enunt ─────────────────────────────────────
def test_C13_procent_din_intrebare_nu_trece_ca_valoare_legala():
    """Intrebarea-capcana spune "10%"; atomul spune 21%. Raspunsul "10%" nu trece, desi e in enunt."""
    o = _out(raspuns="10%")
    q = "O firmă aplică 10% TVA. Care e cota standard în 2026?"
    g = semantic.verifica(o, [ATOM], q, "2026-09-28")
    assert any("C13" in x for x in g), g


def test_C13_termenul_legal_din_intrebare_nu_trece():
    o = _out(raspuns="în termen de 45 de zile")
    g = semantic.verifica(o, [ATOM], "Se contestă în 45 de zile?", "2026-09-28")
    assert any("C13" in x for x in g), g


def test_C13_data_cazului_din_intrebare_trece():
    o = _out(raspuns="Da, de la 14.05.2026 se aplică 21%")
    assert semantic.verifica(o, [ATOM], Q + " Pe 14.05.2026?", "2026-09-28") == []


# ── C17 (b): o derogare din context, de la atomul citat, trebuie tratata ────────────────────────
DEROG = {"id": "cf#art291/alin9", "act": "cod_fiscal_227_2015_consolidat", "valabil_din": "2026-01-01",
         "text": "Prin excepție de la prevederile alin. (1), pentru livrările de ... se aplică o altă cotă."}


def test_C17_derogarea_netratata_respinge_raspunsul():
    rel = {DEROG["id"]: [("exceptie", ATOM["id"])]}
    g = semantic.verifica(_out(), [ATOM, DEROG], Q, "2026-09-28", rel)
    assert any("C17" in x for x in g), g


def test_C17_derogarea_tratata_trece():
    rel = {DEROG["id"]: [("exceptie", ATOM["id"])]}
    o = _out(derogari_tratate=[{"atom": DEROG["id"], "cum": "nu se aplica: intrebarea nu e despre acele livrari"}])
    assert semantic.verifica(o, [ATOM, DEROG], Q, "2026-09-28", rel) == []


def test_C17_derogarea_citata_trece():
    rel = {DEROG["id"]: [("exceptie", ATOM["id"])]}
    o = _out(citate=[{"atom": ATOM["id"], "fragment": FRAG},
                     {"atom": DEROG["id"], "fragment": "Prin excepție de la prevederile alin. (1)"}])
    assert semantic.verifica(o, [ATOM, DEROG], Q, "2026-09-28", rel) == []


# ── C24: raspunsul gol se respinge INTOTDEAUNA, nu numai cand contextul are derogari ────────────
def test_C24_raspunsul_gol_e_respins_fara_derogari():
    for gol in ("", "x", "-", ".", "  "):
        o = _out(raspuns=gol)
        assert "raspuns gol" in semantic.verifica(o, [ATOM], Q, "2026-09-28"), repr(gol)


def test_C24_raspunsul_gol_e_respins_si_cu_derogari():
    o = _out(raspuns="x")
    assert "raspuns gol" in semantic.verifica(o, [ATOM], Q, "2026-09-28", relatie={})


def test_C24_raspunsul_scurt_dar_real_trece():
    """Cealalta directie: "Nu." si "21%" sunt raspunsuri, nu goluri."""
    assert semantic.verifica(_out(raspuns="21%"), [ATOM], Q, "2026-09-28") == []
    o = _out(raspuns="Nu.")
    assert "raspuns gol" not in semantic.verifica(o, [ATOM], Q, "2026-09-28")


def test_C24_abtinerea_fara_raspuns_nu_e_raspuns_gol():
    o = _out(stare="NU_POT_RASPUNDE", raspuns="", citate=[], motiv="nu am temei")
    assert "raspuns gol" not in semantic.verifica(o, [ATOM], Q, "2026-09-28")
