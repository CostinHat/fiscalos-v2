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
    et = "VALOARE_LEGALA" if sursa == "atom" else "FAPT_CAZ"
    return {"nume": nume, "valoare": valoare, "eticheta": et, "atom": atom, "fragment": fragment}


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


def test_C25_valoarea_legala_fara_atom_e_respinsa():
    """Cota luata din intrebare, dar etichetata corect VALOARE_LEGALA: fara atom nu trece."""
    q = Q + " Cota este de 21%."
    c = {"nume": "cota", "valoare": "21%", "eticheta": "VALOARE_LEGALA", "atom": "",
         "fragment": "Cota este de 21%"}
    assert any("fara atom" in g for g in navigare.evalueaza_calcule(_tva("baza * cota", cota=c), V, q)[1])


def test_C25_fapt_caz_care_nu_e_in_intrebare_e_respins():
    b = _op("baza", "12.000", "intrebare", "bunuri de 12.000 lei")
    gr = navigare.evalueaza_calcule(_tva(baza=b), V, Q)[1]
    assert any("FAPT_CAZ" in g for g in gr), gr


def test_C25_fapt_caz_literal_in_intrebare_trece_si_C25_repara_Q_CTB_03():
    """Cealalta directie: "valoare fiscală 100.000 lei" e fapt al cazului (in v4, euristica C13 o
    respingea pentru cuvantul "valoare")."""
    q = "Un utilaj nou, valoare fiscală 100.000 lei, pus în funcțiune în aprilie 2026."
    a = {"id": "cf#art28/alin8^1", "text": "a) amortizarea în primul an nu poate depăși 65% din valoarea fiscală"}
    c = [{"nume": "am", "formula": "vf * p", "operanzi": [
        {"nume": "vf", "valoare": "100.000", "eticheta": "FAPT_CAZ", "atom": "", "fragment": "valoare fiscală 100.000 lei"},
        {"nume": "p", "valoare": "65%", "eticheta": "VALOARE_LEGALA", "atom": a["id"],
         "fragment": "nu poate depăși 65% din valoarea fiscală"}]}]
    val, gr, _d = navigare.evalueaza_calcule(c, {a["id"]: a}, q)
    assert gr == [] and val == {"am": "65.000"}, (gr, val)


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


def test_C28_calculul_se_afiseaza_pas_cu_pas():
    """Fiecare valoare intermediara, inclusiv numarul de zile dintr-o formula (Q-CPF-03 in v4)."""
    q = "Suma de 20.000 lei, scadentă la 25.07.2025, plătită la 03.04.2026."
    a = {"id": "cpf#art174/alin5", "text": "Nivelul dobânzii este de 0,02% pentru fiecare zi de întârziere."}
    c = [{"nume": "dobanda", "formula": "s * c * zile(d1, d2)", "operanzi": [
        _op("s", "20.000", "intrebare", "Suma de 20.000 lei"),
        _op("c", "0,02%", "atom", "este de 0,02% pentru fiecare zi", a["id"]),
        _op("d1", "25.07.2025", "intrebare", "la 25.07.2025"),
        _op("d2", "03.04.2026", "intrebare", "la 03.04.2026")]}]
    val, gr, det = navigare.evalueaza_calcule(c, {a["id"]: a}, q)
    assert gr == [], gr
    txt = " ; ".join(navigare.pas_cu_pas(det))
    assert "zile(25.07.2025, 03.04.2026) = 252 zile" in txt, txt
    assert "20.000" in txt and "0,02%" in txt and val["dobanda"] == "1.008", txt


def test_C28_anul_nu_primeste_separator_de_mii():
    q = "Pentru anul fiscal 2026, până când se depune?"
    c = [{"nume": "an", "formula": "a + 1", "operanzi": [_op("a", "2026", "intrebare", "anul fiscal 2026")]}]
    assert navigare.evalueaza_calcule(c, V, q)[0] == {"an": "2027"}


def test_formatul_romanesc():
    assert navigare._format(1234567.5) == "1.234.567,50"
    assert navigare._numar("100.000")[0] == 100000 and navigare._numar("2,25%")[0] * 100 == 2.25


def test_schema_raspunsului_contine_calculele():
    assert "calcule" in navigare.SCHEMA["required"] and "data_referinta" in navigare.SCHEMA["required"]
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


# ── C23: structura raspunsului final ────────────────────────────────────────────────────────────
def _final(**kw):
    o = {"stare": "RASPUNS", "declaratie": "La data de referință 2026-09-28.", "raspuns": "Cota este 21%.",
         "citate": [], "lipsa": [], "motiv": "", "derogari_tratate": [], "calcule": [],
         "data_referinta": "2026-09-28", "data_referinta_motiv": "ziua intrebarii"}
    o.update(kw)
    return o


def test_C23_raspunsul_bun_trece():
    assert navigare.valideaza_structura(_final()) == []


def test_C23_substituentii_si_golul_sunt_respinsi():
    for r in ("x", "-", "", ".", "  "):
        assert navigare.valideaza_structura(_final(raspuns=r)), repr(r)


def test_C23_marcajul_scurs_e_respins():
    """Exact forma din v4 (Q-PRF-03): raspunsul scris in declaratie, cu marcaj de parametri."""
    d = 'La data 28.09.2026.</declaratie>\n<parameter name="raspuns">Declarația se depune până la 25 iunie.'
    pr = navigare.valideaza_structura(_final(declaratie=d, raspuns="Declarația se depune până la 25 iunie."))
    assert any("marcaj" in p for p in pr), pr


def test_C23_raspunsul_care_repeta_alt_camp_e_respins():
    t = "Declarația se depune până la 25 iunie inclusiv a anului următor."
    assert any("repeta" in p for p in navigare.valideaza_structura(_final(raspuns=t, declaratie="Premisa. " + t)))


def test_C23_abtinerea_fara_raspuns_nu_e_problema_structurala():
    assert navigare.valideaza_structura(_final(stare="NU_POT_RASPUNDE", raspuns="", motiv="nu am temei")) == []


# ── C27: datele intrebarii ──────────────────────────────────────────────────────────────────────
def test_C27_doi_ani_dau_doua_date_nu_cea_mai_veche():
    d = navigare.date_din_intrebare("Cifra de afaceri 2025 peste 50 mil. euro. Cât impozit datorează pentru 2026?")
    assert [x[0] for x in d] == ["2025-12-31", "2026-09-28"], d


def test_C27_anul_cuprins_intr_o_data_completa_nu_e_a_doua_data():
    d = navigare.date_din_intrebare("Factură emisă la 14.05.2026; în 2026 depășește plafonul.")
    assert [x[0] for x in d] == ["2026-05-14"], d


def test_C27_fara_data_nu_e_nicio_data():
    assert navigare.date_din_intrebare("Care este cota standard de TVA?") == []


def test_C29_limita_e_20_de_pasi():
    assert navigare.MAX_PASI == 20
