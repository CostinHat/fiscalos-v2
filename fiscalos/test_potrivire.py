# -*- coding: utf-8 -*-
"""PROBE pe corpus pentru OP5-OP7. Fiecare caz a fost un defect MASURAT, nu presupus."""
import json
import os

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _pot():
    r = json.load(open(os.path.join(_RAD, "artefacte", "potriviri.json"), encoding="utf-8"))
    return {p["parametru"]: p for p in r["potriviri"]}, r


def _inv():
    return json.load(open(os.path.join(_RAD, "artefacte", "inventar_iconta.json"), encoding="utf-8"))


# ── OP5 inventar ─────────────────────────────────────────────────────────────────────────────────
def test_citarea_nu_intra_ca_valoare():
    """`_Tm("Legea", 296, 2023, ...)` e o CITARE. 296 si 2023 nu sunt parametri fiscali.

    `Temei` e importat sub alias in d101.py; un scan care caută litera "Temei(" il rateaza si
    numerele actului intra ca valori. Masurat: 10 din 68 de intrari erau numere de act si ani.
    """
    ids = {p["id"] for p in _inv()["parametri"]}
    for fals in ("nesursat/d101._VARIANTE_COTA_IMCA=296", "nesursat/d101._VARIANTE_COTA_IMCA=2023",
                 "nesursat/lichidare._VARIANTE_COTA_LICHIDARE=227",
                 "nesursat/d212_engine.PLAFOANE_VENIT_2025=2025"):
        assert fals not in ids, fals


def test_cheile_de_dict_nu_intra_ca_valori():
    """`_PCT_DEDUCERE_BAZA = {0: 0.20, 1: 0.25, ...}` - cheile sunt numarul de persoane, nu procente."""
    ids = {p["id"] for p in _inv()["parametri"]}
    assert "nesursat/salarizare._PCT_DEDUCERE_BAZA=0.20" in ids
    assert "nesursat/salarizare._PCT_DEDUCERE_BAZA=3" not in ids


def test_registrul_cote_e_inventariat_intreg():
    """Cele 20 de chei ale registrului COTE, cu toate versiunile lor in timp."""
    par = [p for p in _inv()["parametri"] if p["sursa_inventar"] == "registru COTE"]
    nume = {p["nume"] for p in par}
    assert len(nume) == 20, sorted(nume)
    assert len(par) == 35, len(par)
    assert all(p["temei_declarat"] for p in par), "orice intrare din registru are Temei"


# ── OP6/OP7 potrivire ────────────────────────────────────────────────────────────────────────────
def test_tva_standard_concorda_pe_atomul_legii():
    """Cota de 21% se confirma pe ACTUL DECLARAT de iConta (Legea 141/2025), nu pe alt act.

    `valabil_din_corpus` e None aici, si e corect: redarea Legii 141/2025 din corpus poarta
    VALOAREA, dar notele de intrare in vigoare "(la 01-08-2025, ...)" sunt ale CONSOLIDATULUI de Cod
    fiscal. Deci data se dovedeste pe alt atom decat valoarea - o observatie despre corpus, nu un
    defect, si de-aia raportul are coloana ei separata.
    """
    p, _r = _pot()
    t = p["cote/tva_standard@2025-08-01"]
    assert t["clasificare"] == "CONCORDA", t
    assert t["valoare_lege"] == "21%", t["valoare_lege"]
    assert "21%" in t["atom_verbatim"]
    assert t["atom"].startswith("legea_141_2025_consolidat#art291/alin1"), t["atom"]
    assert t["valabil_din_cod"] == "2025-08-01"


def test_data_de_intrare_in_vigoare_se_dovedeste_pe_consolidat():
    """Perechea probei de mai sus: acelasi alineat, in consolidatul de Cod fiscal, poarta data."""
    import json as _j
    cale = os.path.join(_RAD, "artefacte", "atomi", "cod_fiscal_227_2015_consolidat.jsonl")
    for l in open(cale, encoding="utf-8"):
        a = _j.loads(l)
        if a["id"] == "cod_fiscal_227_2015_consolidat#art291/alin1":
            assert a["valabil_din"] == "2025-08-01", a["valabil_din"]
            assert "21%" in a["text"]
            return
    raise AssertionError("atomul de consolidat lipseste")


def test_toate_citarile_declarate_de_iconta_se_rezolva_in_corpus():
    """Un temei care nu se rezolva e o proba care nu duce unde spune. Masurat: 42 din 42 se rezolva."""
    _p, r = _pot()
    assert r["citari_rezolvate"] == r["citari_declarate"], (r["citari_rezolvate"],
                                                           r["citari_declarate"])


def test_valorile_din_id_uri_cu_sufix_nu_se_pierd():
    """`cass` 10% sta in `#art156~2`, nu in `#art156`. O ancora prea strâmta = NEGASIT fals."""
    p, _r = _pot()
    t = p["cote/cass@2018-01-01"]
    assert t["clasificare"] == "CONCORDA", t
    assert t["valoare_lege"] == "10%", t["valoare_lege"]
    assert "asigurări sociale de sănătate" in t["atom_verbatim"]


def test_valoarea_din_articolul_citat_de_un_punct_se_gaseste():
    """45 lei/tichet sta in articolul CITAT de art. I pct. 1 al Legii 201/2025, nu sub id-ul lui."""
    p, _r = _pot()
    t = p["cote/tichet_masa_plafon@2025-11-01"]
    assert t["clasificare"] == "CONCORDA", t
    assert "45 lei" in t["atom_verbatim"], t["atom_verbatim"][:200]


def test_difera_nu_se_pronunta_fara_ancora_in_actul_declarat():
    """O potrivire pe 2-3 cuvinte in 46.000 de atomi nu susţine "legea spune altceva".

    Masurat: fara aceasta conditie ieseau 7 DIFERA, TOATE false - `_PCT_DEDUCERE_BAZA=0,20` era pus
    langa "legea zice 3,5" dintr-un alineat intamplator din OPANAF 605/2026.
    """
    p, _r = _pot()
    for cheie in ("nesursat/salarizare._PCT_DEDUCERE_BAZA=0.20",
                  "nesursat/salarizare.DEDUCERE_COPIL_SCOALA=100"):
        t = p[cheie]
        assert t["clasificare"] == "NEGASIT", (cheie, t["clasificare"], t.get("valoare_lege"))
        assert "prea slaba" in t["motiv"]


def test_planul_de_conturi_nu_culege_ani_si_randuri_de_formular():
    """`2015` (an), `100`/`102` (randuri de formular) nu sunt conturi. Toate trei ieseau CONCORDA."""
    p, _r = _pot()
    for fals in ("cont/2015", "cont/100", "cont/102", "cont/5000"):
        assert p[fals]["clasificare"] == "NEGASIT", (fals, p[fals]["valoare_lege"])


def test_conturile_adaugate_prin_modificari_sunt_in_plan():
    """436 (CAM), 4315, 463, 646 au intrat in plan prin completari; ele stau INAINTEA planului de baza."""
    p, _r = _pot()
    for cont, bucata in (("436", "asiguratorie pentru muncă"), ("4315", "asigurări sociale"),
                         ("463", "dividende"), ("646", "asiguratorie")):
        t = p["cont/%s" % cont]
        assert t["clasificare"] == "CONCORDA", (cont, t["motiv"][:120])
        assert bucata in t["valoare_lege"], (cont, t["valoare_lege"])


def test_fiecare_concorda_citeaza_atom_si_verbatim():
    """CLAUDE.md §2: fiecare CONCORDA/DIFERA citeaza id-ul atomului si fragmentul verbatim."""
    _p, r = _pot()
    for t in r["potriviri"]:
        if t["clasificare"] in ("CONCORDA", "DIFERA"):
            assert t["atom"], t["parametru"]
            assert t["atom_verbatim"], t["parametru"]


def test_nicio_valoare_inventata_valoarea_lege_apare_in_verbatim():
    """Valoarea raportata ca "a legii" trebuie sa fie in textul verbatim citat - altfel e inventata."""
    import unicodedata

    def n(t):
        t = unicodedata.normalize("NFKD", t or "")
        t = "".join(c for c in t if not unicodedata.combining(c))
        return t.replace("ș", "s").replace("ş", "s").replace("ț", "t").replace("ţ", "t").lower()

    _p, r = _pot()
    for t in r["potriviri"]:
        if t["clasificare"] != "CONCORDA" or not t.get("valoare_lege"):
            continue
        if t["clasa"] in ("cont", "termen", "nomenclator"):
            continue
        assert n(str(t["valoare_lege"])) in n(t["atom_verbatim"]), (t["parametru"],
                                                                   t["valoare_lege"])


# ── termene si nomenclatoare ─────────────────────────────────────────────────────────────────────
def test_termenele_citeaza_articolul_declaratiei_nu_orice_fraza_cu_25():
    """"pana la data de 25 inclusiv" apare de zeci de ori in CF, pentru impozite diferite.

    Fara marcaj de depunere si nume de declaratie, cel mai scurt atom cu fraza era `art.68^2
    alin.(4)` (impozit reţinut la sursa) - pentru AMANDOUA declaraţiile de TVA -, iar `d406` cadea pe
    un fragment din structura XML a lui D112 ("dataAng <= dataSf <= ultima zi a lunii").
    """
    p, _r = _pot()
    asteptat = {
        "termen/d300": ("cod_fiscal_227_2015_consolidat#art323/alin1", "decont de taxă"),
        "termen/d301": ("cod_fiscal_227_2015_consolidat#art324/alin2", "Decontul special de taxă"),
        "termen/d390": ("opanaf_705_2020_d390#art10", "recapitulativă se depune lunar"),
        "termen/d394": ("opanaf_2194_2025_d394#artIV", "până în data de 30 inclusiv"),
        "termen/d406": ("opanaf_1783_2021_saft_d406#art8", "ultima zi calendaristică"),
    }
    for cheie, (prefix_atom, bucata) in asteptat.items():
        t = p[cheie]
        assert t["clasificare"] == "CONCORDA", (cheie, t["motiv"][:150])
        assert t["atom"].startswith(prefix_atom), (cheie, t["atom"])
        assert bucata in t["atom_verbatim"], (cheie, t["atom_verbatim"][:200])


def test_nomenclatorul_cere_enumerare_nu_doar_subiect():
    """d390.TIPURI se confirma numai pe atomul care ENUMERA L/T/A/P/S/R, nu pe oricare din ordin."""
    p, _r = _pot()
    t = p["nomenclator/d390.TIPURI"]
    assert t["clasificare"] == "CONCORDA", t["motiv"]
    for v in ("L", "T", "A", "P", "S", "R"):
        assert v in t["atom_verbatim"], (v, t["atom_verbatim"][:250])


def test_nomenclatorul_deschis_nu_se_confirma():
    """Cand norma NU inchide lista (iConta scrie `deschis=True`), nu exista enumerare de confirmat.

    Nici DIFERA nu e: actul nu spune altceva, nu spune nimic. Inainte, amandoua ieseau CONCORDA pe
    un alineat oarecare din ordin - o confirmare a subiectului luata drept confirmare a listei.
    """
    p, _r = _pot()
    for cheie in ("nomenclator/d390.TARI_UE", "nomenclator/d301.VALUTE"):
        t = p[cheie]
        assert t["clasificare"] == "NEGASIT", (cheie, t["clasificare"])
        assert "nu inchide lista" in t["motiv"]
