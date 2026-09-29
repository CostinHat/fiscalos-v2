# -*- coding: utf-8 -*-
"""PROBE pentru C12 (surse oficiale), C17 (relatia de derogare) si defectul V1 al verificatorului."""
import hashlib
import json
import os
import re
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
    # Decizia dupa pasul 10: instantaneul se reface din starea COMISA a iConta (git HEAD); manifestul
    # inregistreaza commitul, iar fiecare fisier e obiectul git de la acel commit (test_read_only).
    man = json.load(open(os.path.join(_RAD, "corpus_manifest.json"), encoding="utf-8"))
    assert re.match(r"^[0-9a-f]{40}$", man["sursa_commit_git"]) and "COMISA" in man["sursa_mod"]
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
    # punctele normelor se renumeroteaza pe titluri: pct. 1 din Titlul I si pct. 1 din Titlul II sunt
    # atomi diferiti, iar temeiul uman numeste titlul
    a = c.dupa_id["hg_1_2016_norme_cod_fiscal#anexa/pct1/alin1"]
    assert "anexa, Titlul I, pct. 1 alin. (1)" in intrebari.temei_uman(a), intrebari.temei_uman(a)
    t2 = [x for x in c.pe_act["hg_1_2016_norme_cod_fiscal"] if x["id"].startswith("hg_1_2016_norme_cod_fiscal#anexa/pct1~")
          and x.get("titlul") == "Titlul II"]
    assert t2 and "Titlul II, pct. 1" in intrebari.temei_uman(t2[0])
    assert c.dupa_id["omfp_1802_2014#anexa/pct238/alin2"]["text"].startswith("Amortizarea")


def test_propunerea_v5_ramane_neatinsa():
    d = subprocess.run(["git", "diff", "0012001", "--", "propuneri/v5/"], cwd=_RAD,
                       capture_output=True, text=True).stdout
    assert d == "", d[:300]


def test_intrebari_v4_ramane_neatins():
    d = subprocess.run(["git", "diff", "d35c21a", "--", "intrebari/v4/"], cwd=_RAD,
                       capture_output=True, text=True).stdout
    assert d == "", d[:300]


# ── C31: detectorul de structura si actele aduse din sursa oficiala ──────────────────────────────
def test_C31_detectorul_prinde_codul_muncii_din_instantaneu_si_nu_pe_cel_oficial():
    from fiscalos import detector_structura, potrivire
    vechi = detector_structura.detecteaza(potrivire.Corpus(oficiale=False))
    assert "legea_53_2003_codul_muncii" in vechi
    assert vechi["legea_53_2003_codul_muncii"]["S1_alineate_duplicate"] >= 3
    nou = detector_structura.detecteaza(potrivire.Corpus())
    assert "legea_53_2003_codul_muncii" not in nou
    c = potrivire.Corpus()
    assert c.sursa_act["legea_53_2003_codul_muncii"]["sursa"].startswith("oficial")
    assert "90 de zile calendaristice" in c.dupa_id["legea_53_2003_codul_muncii#art122/alin1"]["text"]


def test_C31_detectorul_nu_semnaleaza_un_act_sanatos():
    from fiscalos import detector_structura
    ats = [{"id": "x#art%d" % i, "nivel": "articol", "cheie": str(i), "parinte": None, "text": ""} for i in range(1, 30)]
    ats += [{"id": "x#art%d/alin%d" % (i, j), "nivel": "alineat", "cheie": str(j), "parinte": "x#art%d" % i, "text": ""}
            for i in range(1, 30) for j in (1, 2)]
    assert not detector_structura.e_stricat(detector_structura.semnale(ats, False))
    ats.append({"id": "x#art29/alin1~2", "nivel": "alineat", "cheie": "1", "parinte": "x#art29", "text": ""})
    ats.append({"id": "x#art29/alin2~2", "nivel": "alineat", "cheie": "2", "parinte": "x#art29", "text": ""})
    ats.append({"id": "x#art29/alin1~3", "nivel": "alineat", "cheie": "1", "parinte": "x#art29", "text": ""})
    assert detector_structura.e_stricat(detector_structura.semnale(ats, False))


def test_C31_cuprinsul_portalului_nu_intra_in_text_si_articolul_1000_se_recunoaste():
    from fiscalos import atomizare, surse_oficiale
    h = ('<ul><li><a href="#id_artA136_ttl" onclick="pozitioneaza(\'id_artA136_ttl\')">Articolul 24</a></li></ul>'
         '<span class="S_ART_TTL">Articolul 24</span><span class="S_ALN_TTL">(1)</span>Text 24.'
         '<span class="S_ART_TTL">Articolul 1.000</span><span class="S_ALN_TTL">(1)</span>Text 1000.')
    t = surse_oficiale.html_portal_in_text(h)
    assert t.count("Articolul 24") == 1, t
    atomi, _s = atomizare.atomizeaza_text("cc", t)
    ids = {a["id"] for a in atomi}
    assert "cc#art1000/alin1" in ids and not any("~" in i for i in ids), ids


def test_C31_varianta_stricata_a_unui_act_oficial_nu_e_indexata():
    from fiscalos import intrebari
    idx = intrebari.Index()
    assert idx.corp.inlocuit.get("legea_165_2018_mf_2024") == "legea_165_2018_anaf"
    assert not idx.normativ["legea_165_2018_mf_2024"] and idx.normativ["legea_165_2018_anaf"]


def test_C31_nota_goala_care_se_inchide_singura_nu_inghite_articolele_urmatoare():
    from fiscalos import surse_oficiale
    h = ('<span class="S_NTA" id="n1"><span class="S_NTA_TTL">Notă </span>'
         '<span id="n1_lung"/></span>'
         '<span class="S_ART_TTL">Articolul 122</span><span class="S_ALN_TTL">(1)</span>Munca suplimentară.')
    t = surse_oficiale.html_portal_in_text(h)
    linie_nota = [l for l in t.split("\n") if "⟦NOTĂ⟧" in l]
    assert linie_nota and "Articolul 122" not in linie_nota[0], t
    assert "Articolul 122" in t


def test_C31_S4_prinde_articolul_inghitit_intr_o_nota():
    from fiscalos import detector_structura
    ats = [{"id": "cm#art%d" % i, "nivel": "articol", "cheie": str(i), "parinte": None, "text": ""}
           for i in range(1, 30)]
    ats[20]["text"] = "Text. ⟦NOTĂ⟧ Notă ... + Articolul 122 (1) Munca suplimentară se compensează"
    s = detector_structura.semnale(ats, False)
    assert s["S4_articole_in_nota"] == 1 and detector_structura.e_stricat(s)


def test_propunerea_v6_ramane_neatinsa():
    d = subprocess.run(["git", "diff", "778e826", "--", "propuneri/v6/", "intrebari/v5/"], cwd=_RAD,
                       capture_output=True, text=True).stdout
    assert d == "", d[:300]


# ── C36: conversia oficiala, reparata ca clasa; detectorul iese curat pe stratul oficial ─────────
def test_C36_articolul_citat_S_CIT_se_cuibareste_sub_punct_cel_propriu_nu():
    from fiscalos import atomizare, surse_oficiale
    h = ('<span class="S_ART"><span class="S_ART_TTL">Articolul 12</span><span class="S_ART_BDY">Legea X se modifică:'
         '<span class="S_PCT"><span class="S_PCT_TTL">1.</span><span class="S_PCT_BDY">Articolul 14 va avea următorul cuprins:'
         '<span class="S_CIT"><span class="S_ART"><span class="S_ART_TTL">Articolul 14</span><span class="S_ART_BDY">'
         '<span class="S_ALN"><span class="S_ALN_TTL">(1)</span><span class="S_ALN_BDY">Text citat.</span></span>'
         '</span></span></span></span></span></span></span>'
         '<span class="S_ART"><span class="S_ART_TTL">Articolul 13</span><span class="S_ART_BDY">'
         '<span class="S_ALN"><span class="S_ALN_TTL">(1)</span><span class="S_ALN_BDY">Text propriu.</span></span></span></span>')
    atomi, _s = atomizare.atomizeaza_text("og_x_2011", surse_oficiale.html_portal_in_text(h), oficial=True)
    ids = {a["id"] for a in atomi}
    assert "og_x_2011#art12/pct1/art14/alin1" in ids and "og_x_2011#art13/alin1" in ids, sorted(ids)


def test_C36_numere_de_articol_si_de_punct_cu_exponent_sau_litera():
    from fiscalos import atomizare
    t = "\n".join(["Articolul V", "(1) Text.", "Articolul V^1", "(1) Alt text.", "Articolul 270^2", "(1) A.",
                   "Articolul 270^2 a)", "(1) B."])
    ids = {a["id"] for a in atomizare.atomizeaza_text("x", t)[0]}
    assert {"x#artV^1/alin1", "x#art270^2a/alin1"} <= ids and not any("~" in i for i in ids), sorted(ids)


def test_C36_textul_reprodus_din_alt_act_e_nota_nu_articole():
    from fiscalos import atomizare
    t = "\n".join(["Articolul 1134", "(1) Intră în vigoare.", "(2) Guvernul.", "NOTĂ:",
                   "Reproducem mai jos: - prevederile art. 74-77 din Legea nr. 76/2012", "Articolul 74",
                   "(2) Textul altei legi."])
    atomi = atomizare.atomizeaza_text("cpc", t, oficial=True)[0]
    ids = {a["id"] for a in atomi}
    assert "cpc#nota1" in ids and "cpc#art74" not in ids and "cpc#art1134/alin2~2" not in ids, sorted(ids)
    assert next(a for a in atomi if a["id"] == "cpc#nota1")["nota_tranzitorie"]


def test_C36_forma_restransa_ascunsa_nu_intra_in_text():
    from fiscalos import surse_oficiale
    h = ('<span class="S_LIN_BDY">1 și 2 ianuarie;</span><span style="display:none" class="S_LIN_SHORT"> ... </span>'
         '<span class="S_LIN_BDY">6 ianuarie;</span>')
    assert "..." not in surse_oficiale.html_portal_in_text(h)


def test_C36_detectorul_iese_curat_pe_stratul_oficial_si_cu_motiv_pe_rest():
    from fiscalos import detector_structura, potrivire
    d = detector_structura.detecteaza(potrivire.Corpus())
    assert not any(v["categorie"].startswith("deja din sursa oficiala") for v in d.values()), \
        [a for a, v in d.items() if v["categorie"].startswith("deja")]
    assert not any(v["categorie"] == "de adus din sursa oficiala" for v in d.values()), \
        [a for a, v in d.items() if v["categorie"] == "de adus din sursa oficiala"]


def test_C37_ordinul_1099_identificat_dupa_antet():
    import json as _j
    r = _j.load(open(os.path.join(_RAD, "surse_oficiale", "C31_rezolvare.json"), encoding="utf-8"))["acte"]
    assert r["ordin_1099_2016"]["stare"] == "adus" and r["ordin_1099_2016"]["id_portal"] == "180514"
    assert "12 iulie 2016" in r["ordin_1099_2016"]["motiv"] and "FINANȚELOR" in r["ordin_1099_2016"]["motiv"]


def test_propunerea_v7_si_intrebari_v6_raman_neatinse():
    d = subprocess.run(["git", "diff", "529765c", "--", "propuneri/v7/", "intrebari/v6/"], cwd=_RAD,
                       capture_output=True, text=True).stdout
    assert d == "", d[:300]


def test_propunerea_v8_ramane_neatinsa():
    d = subprocess.run(["git", "diff", "1c9cbf9", "--", "propuneri/v8/", "intrebari/v9/"], cwd=_RAD,
                       capture_output=True, text=True).stdout
    assert d == "", d[:300]
