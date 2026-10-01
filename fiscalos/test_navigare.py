# -*- coding: utf-8 -*-
"""PROBE pentru stratul de navigare (decizia 6) si calculul evaluat de cod (decizia 7) - fara model.

Calculul e locul unde un model ar putea strecura o valoare inventata sub forma unui operand. Deci se
proba cu formule construite anume sa pacaleasca verificatorul: operand fara sursa, valoare care nu e
in fragment, fragment parafrazat, cota luata din intrebare, constanta ascunsa in formula, apel de
functie nepermis.
"""
import ast
import json
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
    # C44: raspunsul final nu mai e o unealta, ci iesirea structurata a turei finale
    assert [u["name"] for u in navigare.UNELTE] == ["cauta", "cuprins", "deschide"]
    assert "alegeri_temei" in navigare.SCHEMA["required"]


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


# ── C33: decodarea artefactului de transport, in ambele directii ────────────────────────────────
def test_C33_secventele_reale_se_decodeaza():
    x = {"citate": [{"fragment": "Amortizarea imobiliz\\u0103rilor corporale \\u00eencep\\u00e2nd"}],
         "raspuns": "Da, \\u0219i \\u021Aara"}
    y = navigare.decodeaza_transport(x)
    assert y["citate"][0]["fragment"] == "Amortizarea imobilizărilor corporale începând"
    assert y["raspuns"] == "Da, și Țara"


def test_C33_textul_legitim_nu_se_atinge():
    for t in ("Cota standard este 21%.", "imobilizărilor corporale (deja cu diacritice)",
              "cale C:\\users\\nume", "\\u00 incomplet", "\\uZZZZ nu e hexa", "\\u0007 control",
              "\\ud800 surogat", "art. 18^1 alin. (1)"):
        assert navigare.decodeaza_transport(t) == t, t
    assert navigare.decodeaza_transport({"n": 3, "l": [True, None]}) == {"n": 3, "l": [True, None]}


# ── C32: termen_efectiv, din atomii citati ──────────────────────────────────────────────────────
def _atomi_calendar():
    from fiscalos import potrivire
    c = potrivire.Corpus()
    r = c.dupa_id["legea_134_2010_codul_de_procedura_civila#art181/alin2"]
    s = c.dupa_id["legea_53_2003_codul_muncii#art139/alin1"]
    return {r["id"]: r, s["id"]: s, ATOM["id"]: ATOM}, [r["id"], s["id"]]


def _termen(d, citati, dupa):
    q = "Termenul nominal este %s." % d
    c = [{"nume": "t", "formula": "termen_efectiv(d)", "operanzi": [_op("d", d, "intrebare", "este %s" % d)]}]
    return navigare.evalueaza_calcule(c, dupa, q, citati=citati)


def test_C32_pastele_ortodox_calculat():
    import datetime
    assert navigare.pastele_ortodox(2026) == datetime.date(2026, 4, 12)
    assert navigare.pastele_ortodox(2025) == datetime.date(2025, 4, 20)
    assert navigare.pastele_ortodox(2027) == datetime.date(2027, 5, 2)


def _lista_datata(dupa):
    """Un atom-lista SINTETIC, cu toate sarbatorile datate - ca sa se probeze mecanismul (C32) separat de
    lipsa datelor din textul oficial (C34)."""
    s = dict(dupa["legea_53_2003_codul_muncii#art139/alin1"])
    s["id"] = "sintetic#lista_datata"
    s["text"] = s["text"].replace("Adormirea Maicii Domnului", "15 august - Adormirea Maicii Domnului") \
        .replace("prima și a doua zi de Crăciun", "25 și 26 decembrie - Crăciunul")
    return s


def test_C38_pe_textul_oficial_Q_TVA_07_da_din_nou_02_03_2026():
    dupa, cit = _atomi_calendar()
    assert "Adormirea Maicii Domnului;" in dupa["legea_53_2003_codul_muncii#art139/alin1"]["text"]  # fara data
    val, gr, det = _termen("28.02.2026", cit, dupa)
    assert gr == [] and val == {"t": "02.03.2026"}, (gr, val)
    txt = " ".join(navigare.pas_cu_pas(det))
    assert "dată de calendar, nescrisă în lege" in txt and "15.08.2026" in txt and "art139/alin1" in txt, txt


def test_C38_termenul_care_cade_pe_15_august_se_muta():
    """15.08.2025 e vineri (Adormirea), 16-17 weekend -> luni 18.08.2025; 15.08.2026 e sambata -> luni 17."""
    dupa, cit = _atomi_calendar()
    val, gr, det = _termen("15.08.2025", cit, dupa)
    assert gr == [] and val == {"t": "18.08.2025"}, (gr, val)
    assert "15.08.2025 Adormirea Maicii Domnului" in " ".join(navigare.pas_cu_pas(det))
    assert _termen("25.12.2026", cit, dupa)[0] == {"t": "28.12.2026"}      # vineri, sambata-26, duminica


def test_C32_mecanismul_sambata_se_prelungeste_la_luni_Q_TVA_07():
    dupa, cit = _atomi_calendar()
    s = _lista_datata(dupa)
    dupa[s["id"]] = s
    val, gr, det = _termen("28.02.2026", [cit[0], s["id"]], dupa)
    assert gr == [] and val == {"t": "02.03.2026"}, (gr, val)
    txt = " ".join(navigare.pas_cu_pas(det))
    assert "28.02.2026 sâmbătă" in txt and "01.03.2026 duminică" in txt and "art181/alin2" in txt, txt


def test_C32_mecanismul_vinerea_mare_si_pastele_din_calcul_declarat():
    dupa, cit = _atomi_calendar()
    s = _lista_datata(dupa)
    dupa[s["id"]] = s
    val, gr, det = _termen("10.04.2026", [cit[0], s["id"]], dupa)
    assert val == {"t": "14.04.2026"}, (gr, val)
    txt = " ".join(navigare.pas_cu_pas(det))
    assert "Paștele ortodox = 12.04.2026" in txt and "Meeus" in txt, txt


def test_C32_mecanismul_zi_lucratoare_ramane_neschimbata():
    dupa, cit = _atomi_calendar()
    s = _lista_datata(dupa)
    dupa[s["id"]] = s
    assert _termen("25.03.2026", [cit[0], s["id"]], dupa)[0] == {"t": "25.03.2026"}


def test_C32_fara_atomii_citati_termen_efectiv_e_respins():
    dupa, cit = _atomi_calendar()
    gr = _termen("28.02.2026", cit[:1], dupa)[1]           # numai regula, fara lista sarbatorilor
    assert any("termen_efectiv cere" in g for g in gr), gr
    gr = _termen("28.02.2026", [], dupa)[1]
    assert any("termen_efectiv cere" in g for g in gr), gr


def test_C32_data_din_luna_in_litere_si_zile_adunate():
    a = {"id": "opanaf#anexa2/pct2", "text": "se depune până la data de 25 inclusiv a lunii următoare"}
    q = "Pentru luna ianuarie 2026, cu operațiuni în ianuarie."
    c = [{"nume": "nominal", "formula": "data(z, l, a) + 0", "operanzi": [
        _op("z", "25", "atom", "până la data de 25 inclusiv", a["id"]),
        _op("l", "ianuarie", "intrebare", "luna ianuarie 2026"),
        _op("a", "2026", "intrebare", "ianuarie 2026")]}]
    # "+ 0" nu e permis (constanta fara sursa) - cealalta directie
    assert any("constanta" in g for g in navigare.evalueaza_calcule(c, {a["id"]: a}, q)[1])
    c[0]["formula"] = "data(z, l, a) + z"
    val, gr, _d = navigare.evalueaza_calcule(c, {a["id"]: a}, q)
    assert gr == [] and val == {"nominal": "19.02.2026"}, (gr, val)


# ── C40: termenul calendaristic vine din termen_efectiv ─────────────────────────────────────────
def test_C40_termenul_scris_direct_e_respins():
    for r in ("Situațiile se depun până la data de 31 mai inclusiv a anului următor.",
              "Termenul este 15.06.2026.", "Cel târziu la 25 iunie 2027 se depune declarația."):
        assert navigare.verifica_termene(r, "Până când se depun?", set()), r


def test_C40_termenul_calculat_si_faptele_cazului_trec():
    assert navigare.verifica_termene("Se depun până la 02.06.2026.", "Până când?", {"02.06.2026"}) == []
    assert navigare.verifica_termene("Factura emisă la 12.05.2026 se corectează.", "La 12.05.2026 ...", set()) == []
    # regula recurenta fara luna numita nu e un termen calendaristic
    assert navigare.verifica_termene("până la data de 25 inclusiv a lunii următoare", "Când?", set()) == []
    # o data care nu e termen (fara context de termen) nu se atinge
    assert navigare.verifica_termene("Cota se aplică începând cu 01.08.2025.", "Ce cotă?", set()) == []


# ── C41: temeiul alaturat, pe perechea reala CF art. 319 alin. (3) / art. 320 alin. (3) ─────────
def _gemeni():
    from fiscalos import potrivire
    c = potrivire.Corpus()
    a = c.dupa_id["cod_fiscal_227_2015_consolidat#art320/alin3"]
    b = c.dupa_id["cod_fiscal_227_2015_consolidat#art319/alin3"]
    return a, b, {a["id"]: a, b["id"]: b}


def test_C41_perechea_319_320_e_recunoscuta_ca_gemeni():
    a, b, v = _gemeni()
    assert [y["id"] for y in navigare.gemeni(a, v)] == [b["id"]]


def test_C41_fara_justificare_abtinere():
    a, b, v = _gemeni()
    final = {"citate": [{"atom": a["id"], "fragment": "x"}], "alegeri_temei": []}
    assert any("C41" in g for g in navigare.verifica_alegeri_temei(final, v))


def test_C41_justificarea_cu_conditia_care_ii_deosebeste_trece():
    a, b, v = _gemeni()
    ok = {"citate": [{"atom": b["id"], "fragment": "x"}], "alegeri_temei": [
        {"atom": b["id"], "alternativa": a["id"],
         "conditie": "beneficiarul trebuie să emită o autofactură în vederea ajustării taxei deductibile"}]}
    assert navigare.verifica_alegeri_temei(ok, v) == []
    # o "conditie" care e si in geaman nu deosebeste nimic
    rau = {"citate": [{"atom": b["id"], "fragment": "x"}], "alegeri_temei": [
        {"atom": b["id"], "alternativa": a["id"],
         "conditie": "dacă furnizorul de bunuri/prestatorul de servicii nu emite factura de corecție"}]}
    assert any("C41" in g for g in navigare.verifica_alegeri_temei(rau, v))


def test_C41_atomii_fara_geaman_nu_cer_justificare():
    v = {ATOM["id"]: ATOM}
    fin = {"citate": [{"atom": ATOM["id"], "fragment": "x"}], "alegeri_temei": []}
    assert navigare.verifica_alegeri_temei(fin, v) == []


# ── C45: numerele scrise in litere ──────────────────────────────────────────────────────────────
def test_C45_numeralul_in_litere_din_atom_e_operand_si_conversia_se_declara():
    a = {"id": "cf#art28/alin4", "text": "valoarea se recuperează într-o perioadă de cinci ani, câte o cincime pe an"}
    q = "Valoarea fiscală de 10.000 lei."
    c = [{"nume": "anual", "formula": "v * f", "operanzi": [
        _op("v", "10.000", "intrebare", "Valoarea fiscală de 10.000 lei"),
        _op("f", "cincime", "atom", "câte o cincime pe an", a["id"])]}]
    val, gr, det = navigare.evalueaza_calcule(c, {a["id"]: a}, q)
    assert gr == [] and val == {"anual": "2.000"}, (gr, val)
    assert "conversie C45/C51: „cincime” (în litere în atom) = 0,20" in " ".join(navigare.pas_cu_pas(det))


def test_C45_cifra_care_nu_e_in_atom_ramane_respinsa():
    a = {"id": "cf#art28/alin4", "text": "într-o perioadă de cinci ani"}
    c = [{"nume": "n", "formula": "x + 1", "operanzi": [_op("x", "5", "atom", "cinci ani", a["id"])]}]
    assert any("nu apare literal" in g for g in navigare.evalueaza_calcule(c, {a["id"]: a}, "Q")[1])


# ── C46: cifra din raspuns e citata sau calculata ───────────────────────────────────────────────
def test_C46_cifra_calculata_scrisa_direct_e_respinsa():
    from fiscalos import semantic
    atom = {"id": "cf#a", "text": "Cota standard este de 21% din baza de impozitare, pentru livrări.",
            "valabil_din": None}
    out = {"stare": "RASPUNS", "declaratie": "d", "raspuns": "TVA este 2.100 lei (21%).", "lipsa": [],
           "motiv": "", "citate": [{"atom": "cf#a", "fragment": "Cota standard este de 21% din baza de impozitare"}]}
    gr = semantic.verifica(out, [atom], "Baza e 10.000 lei.", "2026-09-28")
    assert any("2.100" in g for g in gr), gr


# ── C44: bucla, cu un client simulat - navigare, apoi tura finala structurata fara unelte ────────
class _Bloc(object):
    def __init__(self, **k):
        self.__dict__.update(k)


class _Uz(object):
    input_tokens, output_tokens, cache_creation_input_tokens, cache_read_input_tokens = 10, 10, 0, 0


class _ClientSimulat(object):
    """Primul apel cere o unealta; al doilea spune Gata; al treilea (tura finala) intoarce JSON."""

    def __init__(self, final):
        self.cereri, self.final = [], final
        self.beta = self
        self.messages = self

    def create(self, **k):
        self.cereri.append(k)
        n = len(self.cereri)
        if n == 1:
            c = [_Bloc(type="tool_use", id="t1", name="cauta", input={"interogare": "cota standard TVA"})]
            return _Bloc(content=c, stop_reason="tool_use", usage=_Uz(), model=navigare.MODEL)
        if n == 2:
            return _Bloc(content=[_Bloc(type="text", text="Gata.")], stop_reason="end_turn", usage=_Uz(),
                         model=navigare.MODEL)
        return _Bloc(content=[_Bloc(type="text", text=json.dumps(self.final, ensure_ascii=False))],
                     stop_reason="end_turn", usage=_Uz(), model=navigare.MODEL)


def test_C44_raspunsul_final_vine_pe_iesire_structurata_intr_o_tura_fara_unelte():
    from fiscalos import intrebari
    idx = intrebari.Index()
    hit = idx.cauta("cota standard TVA", "2026-09-28", k=8)
    a = next(x for _s, x in hit if "21%" in x["text"])
    i = a["text"].index("21%")
    final = {"stare": "RASPUNS", "declaratie": "La data de referință 28.09.2026.",
             "raspuns": "Cota standard este 21%.", "citate": [{"atom": a["id"], "fragment": a["text"][i - 40:i + 3]}],
             "lipsa": [], "motiv": "", "derogari_tratate": [], "calcule": [], "alegeri_temei": [],
             "data_referinta": "2026-09-28", "data_referinta_motiv": "ziua întrebării"}
    cl = _ClientSimulat(final)
    r = navigare.raspunde({"id": "Q", "tip": "PARAMETRU", "intrebare": "Care este cota standard de TVA?"},
                          idx, idx.rel, cl, sis="S")
    assert r["stare"] == "RASPUNS", r.get("motiv")
    assert "tool_choice" not in cl.cereri[0] and cl.cereri[2]["tool_choice"] == {"type": "none"}
    assert cl.cereri[2]["output_config"]["format"]["type"] == "json_schema"


def test_C41_deschide_arata_geamanul_din_acelasi_act():
    """Q2-TVA-05: modelul a deschis CF art. 320 alin. (3) si n-a vazut art. 319 alin. (3). Acum il vede."""
    from fiscalos import intrebari
    idx = intrebari.Index()
    nav = navigare.Navigator(idx, idx.rel, "2026-09-28")
    out = nav.deschide("cod_fiscal_227_2015_consolidat#art320/alin3")
    ids = [x["id"] for x in out["atomi_cu_text_aproape_identic"]]
    assert "cod_fiscal_227_2015_consolidat#art319/alin3" in ids, ids
    # C54: numai id + temei, fara text; geamanul nu devine "vazut" (deci citabil) pana nu e deschis
    assert all(set(x) == {"id", "temei"} for x in out["atomi_cu_text_aproape_identic"])
    assert "cod_fiscal_227_2015_consolidat#art319/alin3" not in nav.vazuti
    nav.deschide("cod_fiscal_227_2015_consolidat#art319/alin3")
    assert "cod_fiscal_227_2015_consolidat#art319/alin3" in nav.vazuti


def test_C40_data_de_inceput_si_sufixul_nu_sunt_termene():
    r = ("Termenul de prescripție curge de la 1 ianuarie a anului următor.  "
         "[data de referință: 30.09.2026 — motiv]")
    assert navigare.verifica_termene(r, "Q", set()) == []


# ── C49: justificarea geamanului numai pentru atomul decisiv ────────────────────────────────────
def test_C49_faptul_principal_si_atomul_decisiv():
    assert navigare.fapt_principal("Cota este de 4%, declarată până la data de 25.", "Ce cotă?") == "4%"
    assert navigare.fapt_principal("Venitul de 30.000 lei este neimpozabil.", "Venit de 30.000 lei?") is None
    fin = {"citate": [{"atom": "a#1", "fragment": "procedura, până la data de 25"},
                      {"atom": "a#2", "fragment": "4%, pentru perioada 2026"}], "calcule": []}
    assert navigare.atomi_decisivi(fin, "Cota este de 4%.", "Ce cotă?", []) == {"a#2": "4%"}
    assert navigare.atomi_decisivi(fin, "Da, se aplică.", "Se aplică?", []) == {"a#1": None}


def test_C49_geamanul_neciteaza_la_atomul_nedecisiv_nu_mai_respinge():
    a, b, v = _gemeni()
    fin = {"citate": [{"atom": a["id"], "fragment": "x"}], "alegeri_temei": []}
    assert navigare.verifica_alegeri_temei(fin, v, {}) == []                   # a nu e decisiv
    assert navigare.verifica_alegeri_temei(fin, v, {a["id"]: None})            # a e decisiv: Q2-TVA-05 prins


def test_C49_geamanul_citat_si_el_nu_e_alternativa():
    a, b, v = _gemeni()
    fin = {"citate": [{"atom": a["id"], "fragment": "x"}, {"atom": b["id"], "fragment": "y"}], "alegeri_temei": []}
    assert navigare.verifica_alegeri_temei(fin, v, {a["id"]: None}) == []


# ── C50: procentul impartit la 100, pe propunerea salvata Q3-TVA-09 ─────────────────────────────
def test_C50_Q3_TVA_09_e_respins():
    r = {x["id"]: x for x in json.load(open(os.path.join(_RAD, "intrebari", "set3", "raspunsuri_set3.json"),
                                            encoding="utf-8"))["raspunsuri"]}["Q3-TVA-09"]
    p = r["propunerea_modelului"]
    from fiscalos import intrebari
    idx = intrebari.Index()
    nav = navigare.Navigator(idx, idx.rel, "2026-07-31")
    for s in r["apel"]["pasi"]:
        nav.executa(s["unealta"], s["intrare"])
    gr = navigare.evalueaza_calcule(p["calcule"], nav.vazuti, r["intrebare"], [c["atom"] for c in p["citate"]])[1]
    assert any(g.startswith("C50") for g in gr), gr


def test_C50_procentul_folosit_corect_trece():
    c = _tva("baza * cota", cota=_op("cota", "21%", "atom", "nivelul acesteia este 21%", ATOM["id"]))
    assert navigare.evalueaza_calcule(c, V, Q)[1] == []


# ── C51: ordinale si cifra + unitate ────────────────────────────────────────────────────────────
def test_C51_ordinalul_si_cifra_cu_unitate_sunt_operanzi():
    a = {"id": "cf#art1", "text": "până în cea de-a 15-a zi a lunii, iar termenul este de 60 de zile"}
    c = [{"nume": "n", "formula": "z + t", "operanzi": [
        _op("z", "15-a", "atom", "cea de-a 15-a zi", a["id"]), _op("t", "60 de zile", "atom", "este de 60 de zile", a["id"])]}]
    val, gr, det = navigare.evalueaza_calcule(c, {a["id"]: a}, "Q")
    assert gr == [] and val == {"n": "75"}, (gr, val)
    txt = " ".join(navigare.pas_cu_pas(det))
    assert "„15-a” (ordinal / cifră cu unitate) = 15" in txt and "„60 de zile”" in txt, txt


# ── C52: tura de reparatie, cu client simulat ───────────────────────────────────────────────────
class _ClientReparatie(_ClientSimulat):
    """Tura finala 1: raspuns cu o cifra necitata; tura 2 (reparatia): aceeasi cifra pusa printr-un calcul."""

    def __init__(self, gresit, bun):
        _ClientSimulat.__init__(self, gresit)
        self.bun = bun

    def create(self, **k):
        if len(self.cereri) >= 3:
            self.cereri.append(k)
            return _Bloc(content=[_Bloc(type="text", text=json.dumps(self.bun, ensure_ascii=False))],
                         stop_reason="end_turn", usage=_Uz(), model=navigare.MODEL)
        return _ClientSimulat.create(self, **k)


def test_C52_o_tura_de_reparatie_arata_cifrele_si_reverifica_totul():
    from fiscalos import intrebari
    idx = intrebari.Index()
    hit = idx.cauta("cota standard TVA", "2026-09-28", k=8)
    a = next(x for _s, x in hit if "21%" in x["text"])
    i = a["text"].index("21%")
    baza = {"stare": "RASPUNS", "declaratie": "La data de referință 28.09.2026.", "citate": [
        {"atom": a["id"], "fragment": a["text"][i - 40:i + 3]}], "lipsa": [], "motiv": "", "derogari_tratate": [],
        "alegeri_temei": [], "data_referinta": "2026-09-28", "data_referinta_motiv": "ziua întrebării"}
    gresit = dict(baza, raspuns="TVA este 2.100 lei.", calcule=[])
    bun = dict(baza, raspuns="TVA este {tva} lei.", calcule=[{"nume": "tva", "formula": "b * c", "operanzi": [
        {"nume": "b", "valoare": "10.000", "eticheta": "FAPT_CAZ", "atom": "", "fragment": "baza de 10.000 lei"},
        {"nume": "c", "valoare": "21%", "eticheta": "VALOARE_LEGALA", "atom": a["id"], "fragment": a["text"][i - 40:i + 3]}]}])
    cl = _ClientReparatie(gresit, bun)
    r = navigare.raspunde({"id": "Q", "tip": "CALCUL", "intrebare": "Cât TVA pe o bază de 10.000 lei?"},
                          idx, idx.rel, cl, sis="S")
    assert r["stare"] == "RASPUNS" and "2.100" in r["raspuns"], r.get("motiv")
    assert r["reparatie_C52"]["cifre"] == ["2.100"] and len(cl.cereri) == 4
    assert any(m["role"] == "user" and isinstance(m["content"], str) and "„2.100”" in m["content"]
               for m in cl.cereri[3]["messages"])


# ── C41 ca avertisment (decizia dupa setul 3) ───────────────────────────────────────────────────
def test_C41_geamanul_nejustificat_al_atomului_decisiv_e_avertisment_nu_respingere():
    from fiscalos import intrebari
    idx = intrebari.Index()
    nav = navigare.Navigator(idx, idx.rel, "2026-09-28")
    nav.deschide("cod_fiscal_227_2015_consolidat#art320/alin3")
    a = idx.corp.dupa_id["cod_fiscal_227_2015_consolidat#art320/alin3"]
    frag = "trebuie să emită o autofactură în vederea ajustării bazei de impozitare și a taxei deductibile"
    assert frag in a["text"]
    final = {"stare": "RASPUNS", "declaratie": "La data de referință 28.09.2026.",
             "raspuns": "Beneficiarul emite o autofactură.", "citate": [{"atom": a["id"], "fragment": frag}],
             "lipsa": [], "motiv": "", "derogari_tratate": [], "calcule": [], "alegeri_temei": [],
             "data_referinta": "2026-09-28", "data_referinta_motiv": "ziua întrebării"}
    baza = {"id": "Q", "tip": "REGULA", "intrebare": "Ce face beneficiarul?", "date_din_intrebare": [], "strat": "t"}
    rez = navigare.verifica_propunerea(final, baza, {"intrebare": baza["intrebare"]}, nav, ["2026-09-28"],
                                       "2026-09-28", {}, "")
    assert rez["stare"] == "RASPUNS", rez.get("motiv")
    assert any("art319/alin3" in g for g in rez["avertismente"]) and "avertisment C41" in rez["raspuns"]


# ── C55: valabilitatea operandului legal ────────────────────────────────────────────────────────
def _hg146():
    from fiscalos import potrivire
    a = potrivire.Corpus().dupa_id["hg_146_2026_salariu_minim#art1"]
    return a, [{"nume": "sal", "formula": "s * 1", "operanzi": [
        {"nume": "s", "valoare": "4.325", "eticheta": "VALOARE_LEGALA", "atom": a["id"],
         "fragment": "la suma de 4.325 lei lunar", "data_aplicarii": ""}]}]


def test_C55_valabilitatea_se_citeste_din_textul_atomului():
    import datetime
    a, _c = _hg146()
    din, pana = navigare.valabilitate_valoare(a, "4.325")
    assert din == datetime.date(2026, 7, 1) and pana is None


def test_C55_Q3_SAL_07_salariul_de_4325_aplicat_inainte_de_1_iulie_e_respins():
    a, c = _hg146()
    c[0]["operanzi"][0]["data_aplicarii"] = "2026-01-01"
    gr = navigare.evalueaza_calcule(c, {a["id"]: a}, "CASS pe 2026?")[1]
    assert any(g.startswith("C55") and "01.07.2026" in g for g in gr), gr


def test_C55_valoarea_in_vigoare_la_data_aplicarii_trece():
    a, c = _hg146()
    assert navigare.evalueaza_calcule(c, {a["id"]: a}, "Q", data_faptului="2026-09-28")[1] == []
    assert any(g.startswith("C55") for g in navigare.evalueaza_calcule(c, {a["id"]: a}, "Q",
                                                                       data_faptului="2026-03-31")[1])


def test_C55_perioada_din_text():
    import datetime
    a = {"id": "x", "text": "plafonul de 5.000.000 lei, în perioada 1 martie 2026-31 decembrie 2026, iar de la 1 ianuarie 2027 ..."}
    assert navigare.valabilitate_valoare(a, "5.000.000") == (datetime.date(2026, 3, 1), datetime.date(2026, 12, 31))


# ── C56: data valorii fixata de lege castiga asupra declaratiei modelului ────────────────────────
def _c56(data_aplicarii, regula_id, data_faptului):
    from fiscalos import potrivire
    c = potrivire.Corpus()
    a, reg = c.dupa_id["hg_146_2026_salariu_minim#art1"], c.dupa_id[regula_id]
    calc = [{"nume": "sal", "formula": "s * 1", "operanzi": [
        {"nume": "s", "valoare": "4.325", "eticheta": "VALOARE_LEGALA", "atom": a["id"],
         "fragment": "la suma de 4.325 lei lunar", "data_aplicarii": data_aplicarii}]}]
    return navigare.evalueaza_calcule(calc, {a["id"]: a, reg["id"]: reg}, "CASS pe 2026?",
                                      citati=[reg["id"], a["id"]], data_faptului=data_faptului)


def test_C56_regula_la_1_ianuarie_respinge_4325_chiar_daca_modelul_declara_septembrie():
    """Q3-SAL-07: CF art. 135^1 alin. (3) - salariul minim "in vigoare la data de 1 ianuarie a anului de
    realizare a venitului"; 4.325 lei e valabil de la 01.07.2026 -> respins; textul castiga asupra
    declaratiei modelului (2026-09-28)."""
    _v, gr, det = _c56("2026-09-28", "cod_fiscal_227_2015_consolidat#art135^1/alin3", "2026-09-28")
    assert any(g.startswith("C55") and "01.01.2026" in g for g in gr), gr
    op = det[0]["operanzi"][0] if det else None
    assert op is None or op["data_aplicarii_din_lege"]["data"] == "2026-01-01"


def test_C56_aceeasi_valoare_pe_o_regula_fara_data_fixa_in_iulie_decembrie_e_acceptata():
    for d in ("2026-07-15", "2026-12-31"):
        _v, gr, _det = _c56("", "cod_fiscal_227_2015_consolidat#art170/alin3/litb", d)
        assert gr == [], (d, gr)


def test_C56_intrarea_in_vigoare_a_unei_prevederi_nu_e_data_valorii():
    a = {"id": "hg#1", "text": "salariul de bază minim brut pe țară garantat în plată la suma de 4.325 lei lunar",
         "valabil_din": None}
    r = {"id": "cf#x", "text": "Prevederile privind salariul minim brut pe țară intră în vigoare la data de 1 ianuarie 2025."}
    assert navigare.data_fixata_de_lege([r], a, 2026) is None


# ── C58: termenul scris direct trece prin tura de reparatie ─────────────────────────────────────
class _ClientC58(_ClientSimulat):
    def __init__(self, gresit, bun):
        _ClientSimulat.__init__(self, gresit)
        self.bun = bun

    def create(self, **k):
        if len(self.cereri) >= 3:
            self.cereri.append(k)
            return _Bloc(content=[_Bloc(type="text", text=json.dumps(self.bun, ensure_ascii=False))],
                         stop_reason="end_turn", usage=_Uz(), model=navigare.MODEL)
        return _ClientSimulat.create(self, **k)


def test_C58_termenul_scris_direct_declanseaza_reparatia_nu_respingerea_directa():
    from fiscalos import intrebari
    idx = intrebari.Index()
    hit = idx.cauta("cota standard TVA", "2026-09-28", k=8)
    a = next(x for _s, x in hit if "21%" in x["text"])
    i = a["text"].index("21%")
    baza = {"stare": "RASPUNS", "declaratie": "La data de referință 28.09.2026.", "citate": [
        {"atom": a["id"], "fragment": a["text"][i - 40:i + 3]}], "lipsa": [], "motiv": "", "derogari_tratate": [],
        "alegeri_temei": [], "calcule": [], "data_referinta": "2026-09-28", "data_referinta_motiv": "ziua întrebării"}
    # cifrele "25" si "2026" sunt in intrebare (trec de C46); data compusa nu e - C40 o vede ca termen
    gresit = dict(baza, raspuns="Decontul se depune până la 25 octombrie 2026.")
    bun = dict(baza, raspuns="Decontul se depune lunar.")
    cl = _ClientC58(gresit, bun)
    r = navigare.raspunde({"id": "Q", "tip": "REGULA", "intrebare": "Până când se depune decontul, în 2026, la 25 a lunii?"},
                          idx, idx.rel, cl, sis="S")
    assert r["reparatie_C52"]["termene"] == ["25 octombrie 2026"], r.get("reparatie_C52")
    assert r["stare"] == "RASPUNS" and len(cl.cereri) == 4
    assert any(m["role"] == "user" and isinstance(m["content"], str) and "termen_efectiv" in m["content"]
               for m in cl.cereri[3]["messages"])


# ── raspunsul care depinde de fapte lipsa (Q4-CPF-10) ───────────────────────────────────────────
def test_raspunsul_conditionat_incepe_cu_ce_trebuie_clarificat():
    ok, _m = navigare.verifica_raspuns_conditionat(
        "De clarificat: a câta licitație este și dacă bunul e imobil. La prima licitație prețul de pornire e "
        "prețul de evaluare; la următoarele, diminuat. Exemplu: la o evaluare de 200.000 lei, pragul final e 50.000 lei.")
    assert ok
    assert not navigare.verifica_raspuns_conditionat("Prețul minim este 50.000 lei. De clarificat: a câta licitație.")[0]
    assert not navigare.verifica_raspuns_conditionat("De clarificat: licitația. Prețul minim este 50.000 lei.")[0]
