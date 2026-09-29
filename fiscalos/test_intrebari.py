# -*- coding: utf-8 -*-
"""PROBE pentru motorul de intrebari: orb la cheie, niciodata raspuns fara atom."""
import ast
import json
import os

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_INTERZISE = ("raspuns_asteptat", "verificare")


def test_motorul_nu_poate_citi_coloanele_cheii():
    """Nici ca sir literal, nici ca cheie: `raspuns_asteptat`, `verificare` si coloana `temei` a CSV-ului
    nu apar in motor. Coloana `temei` se verifica pe contextul CSV (cheia de dict pe randul citit),
    fiindca cuvantul "temei" e si vocabularul propriu al motorului."""
    src = open(os.path.join(_RAD, "fiscalos", "intrebari.py"), encoding="utf-8").read()
    arb = ast.parse(src)
    for n in ast.walk(arb):
        if isinstance(n, ast.Constant) and isinstance(n.value, str):
            for c in _INTERZISE:
                assert c not in n.value, (c, n.value[:80])
    from fiscalos import intrebari
    assert intrebari.COLOANE_PERMISE == ("id", "tip", "intrebare")
    for q in intrebari.incarca_intrebari():
        assert set(q) == {"id", "tip", "intrebare"}, set(q)


def test_niciun_raspuns_fara_atom():
    r = json.load(open(os.path.join(_RAD, "artefacte", "intrebari", "raspunsuri.json"),
                       encoding="utf-8"))
    for x in r["raspunsuri"]:
        if x["stare"] == "RASPUNS":
            assert x["argument"], x["id"]
            for a in x["argument"]:
                assert a["atom"] and a["verbatim"] and a["temei"], (x["id"], a)
        else:
            assert x["motiv"], x["id"]


def test_fiecare_raspuns_declara_valabilitatea_la_data_intrebarii():
    r = json.load(open(os.path.join(_RAD, "artefacte", "intrebari", "raspunsuri.json"),
                       encoding="utf-8"))
    for x in r["raspunsuri"]:
        if x["stare"] == "RASPUNS":
            assert x["data_referinta"], x["id"]
            v = x["argument"][0]["valabilitate"]
            assert "valabil_din" in v and "la_data_intrebarii" in v, (x["id"], v)
            if v["la_data_intrebarii"] is False:
                raise AssertionError("raspuns pe un atom care nu era in vigoare: %s" % x["id"])


def test_citatul_verbatim_e_chiar_in_atom():
    """Fragmentul citat trebuie sa fie literal in textul atomului - altfel e o afirmaţie, nu o proba.

    Raspunsurile din artefacte/intrebari/ au fost produse pe INSTANTANEUL iConta, inainte de stratul
    oficial (C12); se verifica pe corpusul cu care au fost produse, nu pe cel de azi - altfel un text
    consolidat mai nou ar face sa para inventat un citat care era literal la momentul lui."""
    from fiscalos import potrivire
    c = potrivire.Corpus(oficiale=False)
    r = json.load(open(os.path.join(_RAD, "artefacte", "intrebari", "raspunsuri.json"),
                       encoding="utf-8"))
    for x in r["raspunsuri"]:
        for a in x["argument"]:
            txt = c.dupa_id[a["atom"]]["text"]
            v = a["verbatim"].strip("…")
            assert v in txt, (x["id"], a["atom"])


# ── motorul v2 ───────────────────────────────────────────────────────────────────────────────────
def test_intrebari_v1_ramane_neatins():
    import subprocess
    d = subprocess.run(["git", "diff", "b0a02c6", "--", "intrebari/v1/"], cwd=_RAD,
                       capture_output=True, text=True).stdout
    assert d == "", d[:300]


def test_fiecare_raspuns_semantic_a_trecut_verificarea_mecanica():
    """Niciun RASPUNS al stratului semantic fara verificare trecuta si fara citat literal in atom.

    Fiecare versiune se verifica pe corpusul cu care a fost produsa: v2 pe instantaneu, v3 cu stratul
    oficial."""
    # v2 a fost produs pe instantaneul atomizat de DINAINTEA anexelor (C26): atomii lui, din git
    f = os.path.join(_RAD, "intrebari", "v2", "raspunsuri_semantic.json")
    _verifica_semantic(json.load(open(f, encoding="utf-8")), _corpus_la_commit("b0a02c6"))
    # v3 a fost produs pe atomizarea oficiala de DINAINTEA reparatiei V2; ea e in git la 7eb6fa0
    f = os.path.join(_RAD, "intrebari", "v3", "raspunsuri_semantic.json")
    _verifica_semantic(json.load(open(f, encoding="utf-8")), _corpus_la_commit("7eb6fa0"))


class _CorpusIstoric(object):
    def __init__(self, dupa_id):
        self.dupa_id = dupa_id


def _corpus_la_commit(commit):
    """Instantaneul + atomii oficiali asa cum erau la `commit` (din git, nu de pe disc)."""
    import subprocess
    d = {}
    lista = subprocess.run(["git", "ls-tree", "--name-only", commit, "artefacte/atomi/",
                            "artefacte/atomi_oficiale/"],
                           cwd=_RAD, capture_output=True, text=True).stdout.split()
    for cale in lista:
        if cale.endswith(".jsonl"):
            txt = subprocess.run(["git", "show", "%s:%s" % (commit, cale)], cwd=_RAD,
                                 capture_output=True, text=True).stdout
            for l in txt.splitlines():
                a = json.loads(l)
                d[a["id"]] = a
    return _CorpusIstoric(d)


def _verifica_semantic(r, c):
    n = 0
    for x in r["raspunsuri"]:
        if x["stare"] == "RASPUNS":
            n += 1
            assert x["verificare"]["trece"], x["id"]
            for a in x["argument"]:
                assert " ".join(a["verbatim"].split()) in " ".join(c.dupa_id[a["atom"]]["text"].split())
        # C5; o abtinere C23/C29 nu are declaratie: iesirea modelului a fost respinsa sau n-a existat
        assert x.get("declaratie") or x.get("tip_abtinere") in ("C23", "C29"), x["id"]
    assert n > 0


def test_costul_e_masurat_pe_fiecare_apel():
    r = json.load(open(os.path.join(_RAD, "intrebari", "v2", "raspunsuri_semantic.json"),
                       encoding="utf-8"))
    for x in r["raspunsuri"]:
        assert x["apel"]["cost_usd"] > 0 and x["apel"]["tokeni"]["iesire"] > 0, x["id"]
    assert abs(sum(x["apel"]["cost_usd"] for x in r["raspunsuri"]) - r["cost_usd"]) < 0.01


def test_comparatorul_recunoaste_data_in_litere():
    from fiscalos import comparatie
    assert comparatie._fapte("25 iunie 2027 inclusiv (nu 25 martie). Nota: 03.08.2026")[0] == "25 iunie"


# ── C28: defectele de clasa ale comparatorului (numai scorul, nu motorul) ──────────────────────
def test_C28_sumele_se_compara_ca_numere():
    from fiscalos import comparatie
    assert comparatie._fapte("2.020 lei") == comparatie._fapte("2020 lei") == ["2020 lei"]
    assert comparatie._fapte("1.031,25 lei") == comparatie._fapte("1031,25 lei")
    assert comparatie._fapte("0,5%") == comparatie._fapte("0.5%")
    assert comparatie._fapte("21%") != comparatie._fapte("19%")          # cealalta directie


def test_C28_faptul_negat_nu_e_faptul_principal():
    from fiscalos import comparatie
    k = "Nu 25% x 2.162,50 = 540,63 lei, ci minimul: 1.031,25 lei"
    assert "540,63 lei" not in comparatie._fapte(k, fara_negate=True)
    assert comparatie._fapte("25 iunie 2027 (nu 25 martie)", fara_negate=True)[0] == "25 iunie"
    # fara negatie, nimic nu se taie
    assert comparatie._fapte("Cota este 10%, fara recalculare.", fara_negate=True) == ["10%"]


def test_C28_paranteza_de_provenienta_nu_e_temei():
    from fiscalos import comparatie
    t = comparatie._temeiuri_cheie("Cod fiscal art. 51 alin. (1) (mod. OUG 89/2025); art. 56 alin. (1)")
    assert ("cf", "51") in t and ("cf", "56") in t
    assert not any(f == "oug_89_2025" for f, _a in t)


def test_C28_bucata_fara_act_continua_actul_anterior():
    from fiscalos import comparatie
    t = comparatie._temeiuri_cheie("Cod fiscal art. 291 alin. (1); art. 298 alin. (1)-(3)")
    assert ("cf", "298") in t and (None, "298") not in t


def test_raspunsurile_navigarii_au_trecut_verificarea_pe_corpusul_lor():
    """v4 pe atomizarea de la d35c21a (inainte de C26), v5 pe cea de la 778e826 (inainte de C31)."""
    f = os.path.join(_RAD, "intrebari", "v4", "raspunsuri_navigare.json")
    _verifica_semantic(json.load(open(f, encoding="utf-8")), _corpus_la_commit("d35c21a"))
    # v5 pe corpusul commit-ului lui (778e826): C31 a schimbat apoi id-urile (cuprinsul portalului)
    f = os.path.join(_RAD, "intrebari", "v5", "raspunsuri_navigare.json")
    r = json.load(open(f, encoding="utf-8"))
    _verifica_semantic(r, _corpus_la_commit("778e826"))
    for x in r["raspunsuri"]:
        if x["stare"] == "RASPUNS":                      # C24 + C23: niciun raspuns gol
            assert len(x["raspuns"].split("  [")[0].strip()) >= 2, x["id"]
            assert x["data_referinta"] in [d[0] for d in x["date_din_intrebare"]] or \
                (not x["date_din_intrebare"] and x["data_referinta"] == "2026-09-28"), x["id"]   # C27


# ── C30: formulari echivalente pentru zero si date in litere ────────────────────────────────────
def test_C30_zero_spus_in_cuvinte():
    from fiscalos import comparatie
    assert "0 lei" in comparatie._fapte_raspuns("Nu datorează nimic: pentru amenzi nu se datorează accesorii.")
    assert "0 lei" not in comparatie._fapte_raspuns("Datorează dobânzi de 1.008 lei.")     # cealalta directie


def test_C30_data_in_litere_cu_an_e_aceeasi_cu_data_numerica():
    from fiscalos import comparatie
    assert "28.02.2026" in comparatie._fapte("până la 28 februarie 2026")
    assert comparatie._fapte("până la 28 februarie 2026")[0] == "28 februarie"   # faptul principal, neschimbat
    assert comparatie._fapte("1.3.2026") == ["01.03.2026"]
    assert "28.02.2027" not in comparatie._fapte("până la 28 februarie 2026")     # alt an nu se potriveste


def test_setul_2_se_incarca_orb():
    """Masuratoarea finala: aceeasi orbire pe setul 2 - motorul primeste numai id, tip, intrebare."""
    from fiscalos import intrebari
    f = "/home/costin/ghid_incoming/FiscalOS_intrebari_set2_50.csv"
    # fara fisier, proba PICA (nu trece pe tacute): prima versiune facea `return` si a raportat PASS
    # fara sa verifice nimic
    assert os.path.exists(f), "setul 2 lipseste: %s" % f
    qs = intrebari.incarca_intrebari(f)
    assert len(qs) == 50 and all(set(q) == {"id", "tip", "intrebare"} for q in qs)
    assert all(q["id"].startswith("Q2-") for q in qs)
    src = open(os.path.join(_RAD, "fiscalos", "navigare.py"), encoding="utf-8").read()
    for c in _INTERZISE:
        assert c not in src, c
