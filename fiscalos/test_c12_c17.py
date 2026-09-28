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
    """Stratul oficial nu scrie in corpus/ si nu atinge atomii instantaneului.

    Manifestul corpusului e neschimbat de la d7efc18. Atomii instantaneului (`artefacte/atomi/`) sunt
    DERIVATI: se schimba cand se schimba atomizatorul (C26, anexele), dar numai prin el - fiecare
    fisier e exact re-atomizarea textului instantaneului, fara nicio mana si fara stratul oficial."""
    d = subprocess.run(["git", "diff", "--stat", "d7efc18", "--", "corpus_manifest.json"],
                       cwd=_RAD, capture_output=True, text=True).stdout
    assert d == "", d
    from fiscalos import atomizare
    strat = json.load(open(os.path.join(_RAD, "artefacte", "strat_text.json"), encoding="utf-8"))
    for baza in ("cod_fiscal_227_2015_consolidat", "omfp_1802_2014", "opanaf_3769_2015_d394_baza",
                 "legea_141_2025"):
        txt = open(os.path.join(_RAD, strat["acte"][baza]["text"]), encoding="utf-8").read()
        atomi, _s = atomizare.atomizeaza_text(baza, txt)
        disc = [json.loads(l) for l in open(os.path.join(
            _RAD, "artefacte", "atomi", baza.replace("/", "__") + ".jsonl"), encoding="utf-8")]
        assert atomi == disc, baza
        assert not any(a.get("sursa") == "oficial" for a in disc), baza


def test_C19_opanaf_3769_compus_ordin_oficial_si_anexe_din_instantaneu():
    """C19: textul ordinului din sursa oficiala, anexele din instantaneu; fiecare parte cu data ei."""
    from fiscalos import potrivire
    c = potrivire.Corpus()
    assert c.sursa_act["opanaf_3769_2015_d394_baza"]["sursa"].startswith("compus")
    ats = c.pe_act["opanaf_3769_2015_d394_baza"]
    assert {a["parte"] for a in ats} == {"textul ordinului (oficial)",
                                          "anexe (instantaneu iConta, forma de baza)"}
    assert all(a.get("data_formei") for a in ats)
    # C26: anexele instantaneului au structura proprie; toate vin din instantaneu, niciuna oficiala
    anexe = [a for a in ats if a["parte"].startswith("anexe")]
    assert len(anexe) > 50 and all("#anexa" in a["id"] for a in anexe)
    assert not any("#anexa" in a["id"] for a in ats if a["parte"].startswith("textul"))
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


# ── C26: anexele, structura proprie ─────────────────────────────────────────────────────────────
def test_C26_anexa_are_structura_proprie_si_temeiul_o_numeste():
    from fiscalos import atomizare, intrebari
    txt = "\n".join(["Articolul 1", "Se aprobă reglementările din anexă.", "Articolul 2",
                     "Prezentul ordin se publică.", "", "ANEXĂ", "REGLEMENTĂRI CONTABILE", "",
                     "237.", "- (1) Text 237.", "", "238.", "- (1) Amortizarea se stabilește.",
                     "(2)", "Amortizarea începe cu luna următoare punerii în funcțiune.",
                     "239.", "- Alt punct."])
    atomi, _s = atomizare.atomizeaza_text("omfp_1802_2014", txt)
    ids = {a["id"]: a for a in atomi}
    assert "omfp_1802_2014#anexa/pct238/alin2" in ids, sorted(ids)
    assert "omfp_1802_2014#anexa/pct239" in ids
    assert not any(i.startswith("omfp_1802_2014#art2/") for i in ids)       # nu sub ultimul articol
    t = intrebari.temei_uman(ids["omfp_1802_2014#anexa/pct238/alin2"])
    assert t.endswith("anexa, pct. 238 alin. (2)"), t


def test_C26_articolul_care_continua_actul_inchide_anexa_si_lista_nu_deschide():
    from fiscalos import atomizare
    txt = "\n".join(["Articolul 45", "(1) Text.", "", "+", "Anexa nr. 1", "LISTA SOCIETĂȚILOR",
                     "1. Societatea A", "Articolul 46", "(1) Text 46.",
                     "Articolul 47", "Anexa nr. 2", "Anexa nr. 3", "Articolul 48", "(1) Text 48."])
    atomi, _s = atomizare.atomizeaza_text("cf", txt)
    ids = [a["id"] for a in atomi]
    assert "cf#anexa1" in ids and "cf#art46/alin1" in ids and "cf#art48/alin1" in ids, ids
    assert "cf#anexa2" not in ids and "cf#anexa3" not in ids          # serie = lista, nu anexe


def test_C26_anexa_citata_intr_un_punct_de_interventie_nu_e_anexa():
    from fiscalos import atomizare
    txt = "\n".join(["Articolul I", "Legea nr. 227/2015 se modifică:", "1. Anexa nr. 2 se înlocuiește:",
                     "Anexa nr. 2", "Nr. crt. Produs", "Articolul II", "(1) Text."])
    atomi, _s = atomizare.atomizeaza_text("og_x_2022", txt)
    assert not any(a["nivel"] == "anexa" for a in atomi)


def test_C26_normele_numesc_titlul():
    from fiscalos import potrivire, intrebari
    c = potrivire.Corpus()
    a = c.dupa_id["hg_1_2016_norme_cod_fiscal#anexa/pct1/alin1"]
    assert "anexa, Titlul II, pct. 1 alin. (1)" in intrebari.temei_uman(a)
    assert c.dupa_id["omfp_1802_2014#anexa/pct238/alin2"]["text"].startswith("Amortizarea")


def test_propunerea_v5_ramane_neatinsa():
    d = subprocess.run(["git", "diff", "0012001", "--", "propuneri/v5/"], cwd=_RAD,
                       capture_output=True, text=True).stdout
    assert d == "", d[:300]


def test_intrebari_v4_ramane_neatins():
    d = subprocess.run(["git", "diff", "d35c21a", "--", "intrebari/v4/"], cwd=_RAD,
                       capture_output=True, text=True).stdout
    assert d == "", d[:300]
