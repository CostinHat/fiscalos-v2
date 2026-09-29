# -*- coding: utf-8 -*-
"""PROBE pentru deciziile de arhitect C2, C3, C4, C7 (Costin, dupa propunerea v1).

Fiecare decizie e o regula care poate fi incalcata tacut de o schimbare viitoare. Proba e ce o face
mecanica: daca regula cade, cade si testul.
"""
import json
import os

from fiscalos import banc_mutatii, surse

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _pot():
    r = json.load(open(os.path.join(_RAD, "artefacte", "potriviri.json"), encoding="utf-8"))
    return r["potriviri"]


# ── C2 ───────────────────────────────────────────────────────────────────────────────────────────
def test_C2_ancora_slaba_nu_e_niciodata_CONCORDA():
    """Ancora slaba (cautare in tot corpusul, parametru nesursat) e NEVERIFICAT, nu CONCORDA."""
    for p in _pot():
        if p["clasificare"] == "CONCORDA":
            assert "TOT CORPUSUL" not in str(p.get("ancora")), p["parametru"]


def test_C2_temeiul_candidat_vine_numai_din_act_normativ():
    """"Un formular, o structura de declaratie sau un pliant ANAF nu poate fi temei." """
    n = 0
    for p in _pot():
        c = p.get("temei_candidat")
        if c:
            n += 1
            ok, de_ce = surse.e_act_normativ(c["act"])
            assert ok, (p["parametru"], c["act"], de_ce)
            assert c["de_aprobat"] is True
    assert n > 0, "nu s-a propus niciun temei candidat - proba ar trece pe gol"


def test_C2_CONCORDA_si_DIFERA_stau_numai_pe_acte_normative():
    """Si temeiurile DECLARATE: o nota scrisa de iConta sau un pliant nu verifica nimic."""
    for p in _pot():
        if p["clasificare"] in ("CONCORDA", "DIFERA") and p["clasa"] != "cont" and p.get("atom"):
            act = p["atom"].split("#")[0]
            assert surse.e_act_normativ(act)[0], (p["parametru"], act)


def test_C2_notele_SCRIS_citate_ca_temei_ies_NEVERIFICAT():
    """Registrul COTE citeaza nota `cf_art291_2016_forma_initiala` (SCRIS) pentru cotele din 2016."""
    P = {p["parametru"]: p for p in _pot()}
    for k in ("cote/tva_redusa_9@2016-01-01", "cote/tva_redusa_5@2016-01-01"):
        assert P[k]["clasificare"] == "NEVERIFICAT", (k, P[k]["clasificare"])
        assert P[k]["clasificare_initiala"] == "CONCORDA"
        assert "SCRIS" in P[k]["motiv"]


def test_clasificatorul_de_surse_nu_se_lasa_pacalit_de_nume():
    """Trei note SCRIS au nume de act normativ. Prefixul singur le-ar fi acceptat."""
    for baza in ("cf_art291_2016_forma_initiala", "hg518_1995_diurna_externa",
                 "hg714_2018_diurna_interna", "impozit_dividende_istoric_cote"):
        assert not surse.e_act_normativ(baza)[0], baza
    for baza in ("anaf_limite_2025", "d394_struct_anaf",
                 "pdf_original/structura_D300_v12.0.0_10022026",
                 "GRESIT_oms_484_2025_modificarea_ordin_ms_444_2019"):
        assert not surse.e_act_normativ(baza)[0], baza
    for baza in ("cod_fiscal_227_2015_consolidat", "legea_141_2025", "hg_146_2026_salariu_minim",
                 "opanaf_705_2020_d390", "oug_89_2025", "omfp_3103_2017"):
        assert surse.e_act_normativ(baza)[0], baza


# ── C4 ───────────────────────────────────────────────────────────────────────────────────────────
def test_C4_fiecare_verdict_pe_valoare_are_pereche_de_valabilitate_sau_o_declara_lipsa():
    """Perechea (atom-valoare, atom-valabilitate); cand lipseste al doilea, se spune explicit."""
    for p in _pot():
        if p["clasa"] in ("cota", "plafon") and p["clasificare"] in ("CONCORDA", "DIFERA",
                                                                      "NEVERIFICAT") and p["atom"]:
            assert p.get("atom_valabilitate") or p.get("valabilitate_lipsa"), p["parametru"]


def test_C4_TVA_valoarea_si_data_vin_din_atomi_diferiti():
    P = {p["parametru"]: p for p in _pot()}
    t = P["cote/tva_standard@2025-08-01"]
    assert t["atom"].startswith("legea_141_2025_consolidat#artII/pct42/art291/alin1")   # C31, oficial
    v = t["atom_valabilitate"]
    assert v["atom"] == "cod_fiscal_227_2015_consolidat#art291/alin1", v
    assert v["valabil_din"] == "2025-08-01"
    assert v["acelasi_cu_atomul_valorii"] is False


def test_C4_actul_care_isi_scrie_data_e_propriul_atom_de_valabilitate():
    """HG 146/2026: "Incepand cu data de 1 iulie 2026, salariul ... la suma de 4.325 lei"."""
    P = {p["parametru"]: p for p in _pot()}
    v = P["cote/salariu_minim@2026-07-01"]["atom_valabilitate"]
    assert v["valabil_din"] == "2026-07-01", v
    assert "textul atomului" in v["sursa_datei"]


# ── C3 ───────────────────────────────────────────────────────────────────────────────────────────
def test_C3_cerinta_pentru_iConta_are_numarul_conturilor_nemarcate():
    inv = json.load(open(os.path.join(_RAD, "artefacte", "inventar_iconta.json"), encoding="utf-8"))
    cn = inv["conturi_nemarcate"]
    assert cn["n_simboluri"] >= 100 and cn["n_module"] >= 10, cn


# ── C7 ───────────────────────────────────────────────────────────────────────────────────────────
def test_C7_bancul_acopera_fiecare_clasa():
    clase = {m["clasa"] for m in banc_mutatii.MUTATII}
    for c in ("cota", "plafon", "termen", "nomenclator", "cont"):
        assert c in clase, c
    for m in banc_mutatii.MUTATII:
        assert m["aștept"] in ("DIFERA", "NEGASIT"), m["nume"]
        if m["aștept"] == "NEGASIT":
            assert m.get("motiv_conţine"), ("NEGASIT fara motiv cerut", m["nume"])


# ── v1 neatins, v2 complet ───────────────────────────────────────────────────────────────────────
# v1 asa cum l-a citit arhitectul pe GitHub. NU e commit-ul care l-a creat (6f64a12): v1 a fost
# regenerat pe loc o data, in e261e01, cand bancul de mutaţii a schimbat regulile de clasificare
# (202/0/29 -> 200/0/31). Istoria le pastreaza pe amandoua. De la e261e01 incolo, v1 e inghetat.
_V1_INGHETAT = "e261e01"


def test_v1_ramane_neatins_in_afara_de_C7():
    """Singura schimbare admisa in v1 e textul C7, cerut explicit de arhitect: numai ADAUGARI in RAPORT."""
    import subprocess
    for f in ("propunere.json", "APROBARE.md"):
        d = subprocess.run(["git", "diff", _V1_INGHETAT, "--", "propuneri/v1/" + f], cwd=_RAD,
                           capture_output=True, text=True).stdout
        assert d == "", (f, d[:300])
    d = subprocess.run(["git", "diff", _V1_INGHETAT, "--", "propuneri/v1/RAPORT.md"], cwd=_RAD,
                       capture_output=True, text=True).stdout
    sterse = [l for l in d.splitlines() if l.startswith("-") and not l.startswith("---")]
    adaugate = [l for l in d.splitlines() if l.startswith("+") and not l.startswith("+++")]
    assert not sterse, sterse
    assert any(l.startswith("+**C7") for l in adaugate), "C7 lipseste din v1"
    assert len(adaugate) <= 20, len(adaugate)


def test_v2_are_toate_livrabilele():
    for f in ("propunere.json", "RAPORT.md", "APROBARE.md", "temeiuri_candidate.json",
              "cerinte_iconta.json"):
        assert os.path.isfile(os.path.join(_RAD, "propuneri", "v3", f)), f
    r = open(os.path.join(_RAD, "propuneri", "v3", "RAPORT.md"), encoding="utf-8").read()
    for c in ("C1", "C2", "C3", "C4", "C5", "C7", "C8", "C9", "C10", "C11", "C12"):
        assert "**%s" % c in r, c
    # prima pagina: CONCORDA numai pe temei declarat verificat, NEVERIFICAT separat
    cap = r[:900]
    assert "CONCORDĂ** — pe temei declarat și verificat" in cap
    assert "NEVERIFICAT" in cap


def test_temeiurile_candidate_sunt_toate_din_act_normativ_si_neaprobate():
    t = json.load(open(os.path.join(_RAD, "propuneri", "v3", "temeiuri_candidate.json"),
                       encoding="utf-8"))
    assert t["aprobare"] == "NEAPROBAT"
    assert t["candidati"]
    for c in t["candidati"]:
        assert surse.e_act_normativ(c["act"])[0], c["act"]


# ── deciziile C8-C11 (propunerea v3) ─────────────────────────────────────────────────────────────
_V2_INGHETAT = "b0a02c6"


def test_v2_ramane_neatins():
    import subprocess
    d = subprocess.run(["git", "diff", _V2_INGHETAT, "--", "propuneri/v2/"], cwd=_RAD,
                       capture_output=True, text=True).stdout
    assert d == "", d[:300]


def test_C9_difera_poarta_dezacordul_declarat_de_iconta_verbatim():
    P = {p["parametru"]: p for p in _pot()}
    t = P["nomenclator/d394.TIPURI"]
    assert t["clasificare"] == "DIFERA"
    dz = t["dezacord_declarat_de_iconta"]
    assert "Î1/Î2" in dz["ce"] and dz["unde"].startswith("core/nomenclatoare.py:")
    r = open(os.path.join(_RAD, "propuneri", "v3", "RAPORT.md"), encoding="utf-8").read()
    assert dz["ce"] in r, "mentiunea C9 trebuie sa apara VERBATIM in raport"


def test_C10_temeiul_candidat_e_act_de_baza_iar_modificatorul_e_valabilitate():
    from fiscalos import potrivire
    corp = potrivire.Corpus()
    n = 0
    for p in _pot():
        c = p.get("temei_candidat")
        if c:
            n += 1
            assert surse.e_act_de_baza(c["act"], corp.modificatoare), (p["parametru"], c["act"])
        elif p["clasificare"] == "NEVERIFICAT" and not p.get("clasificare_initiala"):
            assert p.get("act_de_baza") is not None, p["parametru"]
            assert "MODIFICATOR" in p["motiv"]
    assert n > 0


def test_C10_normele_nu_sunt_act_modificator():
    """HG 1/2016 are articole proprii romane ("Art. I - Se aproba Normele"), dar nu modifica nimic."""
    from fiscalos import potrivire
    corp = potrivire.Corpus()
    assert "hg_1_2016_norme_cod_fiscal" not in corp.modificatoare
    for a in ("legea_141_2025", "opanaf_2194_2025_d394", "legea_296_2023_masuri_fiscal_bugetare_asigurarea_sustenabilitatii"):
        assert a in corp.modificatoare, a


def test_C11_unitatea_dedusa_e_marcata_si_R_UNIT_e_cerinta():
    P = {p["parametru"]: p for p in _pot()}
    assert "unitate_dedusa" in P["nesursat/d216.COTA_IMPOZIT=0.3"]
    cer = json.load(open(os.path.join(_RAD, "propuneri", "v3", "cerinte_iconta.json"),
                         encoding="utf-8"))["cerinte"]
    assert any(c["id"] == "R-UNIT" for c in cer)
