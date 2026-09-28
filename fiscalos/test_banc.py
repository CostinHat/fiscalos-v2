# -*- coding: utf-8 -*-
"""PROBE pentru dovada in CEALALTA direcţie, si pentru cele patru defecte pe care bancul le-a scos.

"0 DIFERA" e o propoziţie fara conţinut daca detectorul nu poate produce un DIFERA. Bancul injecteaza
greșeli cunoscute din istoria fiscala si cere ca fiecare sa iasa DIFERA, cu temeiul corect alaturi.
La prima rulare TOATE CINCI au ieșit CONCORDA - deci raportul de dinainte nu masura concordanţa, ci
tacerea unui detector care nu putea contrazice.
"""
import json
import os

from fiscalos import banc_mutatii, potrivire

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_CACHE = {}


def _banc():
    if "ies" not in _CACHE:
        corp = potrivire.Corpus()
        _CACHE["ies"] = banc_mutatii.ruleaza(corp, potrivire.plan_de_conturi(corp))
    return _CACHE["ies"]


def test_fiecare_greseala_injectata_iese_DIFERA_cu_temeiul_corect():
    ies = _banc()
    trecute, picate = banc_mutatii.verdict(ies)
    assert not picate, [(x["mutaţie"], x["mutant"]["clasificare"],
                         x["mutant"]["valoare_lege"]) for x in picate]
    assert len(trecute) == len(banc_mutatii.MUTATII)


def test_citarea_spre_actul_gresit_e_semnalata_nu_inghitita():
    """Valoarea din cod e CORECTA (CAS 25%), dar temeiul trimite la o HG de salariu minim.

    Verdictul nu e despre valoare, ci despre proba: `citare_rezolvata` trebuie sa fie False, iar
    clasificarea NEGASIT - fiindca actul declarat nu stabileste parametrul. Inainte ieșea CONCORDA,
    pe un atom gasit in cu totul alt act, cu `citare_rezolvata=True`.
    """
    x = [y for y in _banc() if "actul greșit" in y["mutaţie"]][0]
    assert x["mutant"]["citare_rezolvata"] is False, x["mutant"]
    assert x["mutant"]["clasificare"] == "NEGASIT", x["mutant"]["clasificare"]
    assert "Nu se caută in alte acte" in x["mutant"]["motiv"]


def test_originalele_rămân_CONCORDA_cand_mutantul_iese_DIFERA():
    """Bancul e util numai daca mutaţia e singura diferenţa: originalul aceluiasi parametru concorda."""
    for x in _banc():
        if x["aștept"] == "DIFERA":
            assert x["original"]["clasificare"] == "CONCORDA", (x["mutaţie"],
                                                               x["original"])


# ── defectele pe care bancul le-a scos ───────────────────────────────────────────────────────────
def test_forma_procentului_nu_pierde_zeroul_final():
    """`Decimal("10").normalize()` da `1E+1`, iar `rstrip("0")` face din "10" -> "1".

    Efectul: cota de 10% avea printre formele ei si "1%", deci un text care spune 1% o confirma.
    Masurat pe inventarul real: trei CONCORDA false (bacsis 10% pe "1%", d216 30% pe "3%",
    d394 20% pe "2%").
    """
    for v, aștept in (("10", "10%"), ("0.10", "10%"), ("0.3", "30%"), ("20", "20%"),
                      ("0.0225", "2,25%"), ("0.005", "0,5%")):
        forme = potrivire.forme_numar(v, "procent")
        assert aștept in forme, (v, sorted(forme))
        for f in forme:
            cifre = f.replace("%", "").replace(" ", "").replace(",", ".")
            assert cifre not in ("1", "3", "2") or aștept.startswith(cifre + "%"), (v, f)


def test_niciun_indiciu_de_subiect_nu_conţine_cifre():
    """Un indiciu cu valoarea in el se confirma pe sine. Doua le conţineau ("15.000 euro")."""
    for nume, indicii in potrivire.SUBIECT.items():
        for ind in indicii:
            assert not potrivire._CIFRA.search(ind), (nume, ind)


def test_indiciul_cere_frază_nu_cuvinte_imprastiate():
    """"proprietate personală se determină prin deducerea" NU e "deducere personala": ordine inversa."""
    stems = [potrivire._stemuri_indiciu("deducere personala")]
    bun = {"_n": potrivire.norm("Deducerea personală de bază se acordă pentru persoanele fizice")}
    rau = {"_n": potrivire.norm("locuințe proprietate personală se determină prin deducerea din "
                                "venitul brut")}
    assert potrivire._are_subiect(bun, stems)
    assert not potrivire._are_subiect(rau, stems)


def test_indiciul_tolereaza_flexiunea():
    """"mijloace fixe" trebuie sa gaseasca "mijloacelor fixe" - altfel NEGASIT fals pe HG 276/2013."""
    stems = [potrivire._stemuri_indiciu("mijloace fixe")]
    a = {"_n": potrivire.norm("valoarea minimă de intrare a mijloacelor fixe este de 2.500 lei")}
    assert potrivire._are_subiect(a, stems)


def test_difera_nu_se_pronunta_pe_un_fragment():
    """Un fragment vine dintr-un act fara structura de articol; nu se stie CE unitate de text e.

    `anaf_limite_2025` e un tabel pe coloane, intretesut de extractie: fragmentul purta sapte numere
    lipite si a produs un DIFERA fals pentru tichetul de masa, desi 40,18 chiar exista in act.
    """
    r = json.load(open(os.path.join(_RAD, "artefacte", "potriviri.json"), encoding="utf-8"))
    for p in r["potriviri"]:
        if p["clasificare"] == "DIFERA":
            assert p.get("atom_nivel") != "fragment", p["parametru"]


def test_ancora_slaba_cere_valoarea_langa_subiect():
    """Pe ancora slaba, subiectul si valoarea trebuie sa aparţina aceleiasi reguli, nu aceluiasi atom.

    `_PCT_DEDUCERE_BAZA=0.20` ieșea CONCORDA pe un alineat despre impozitarea jocurilor de noroc:
    fraza si numarul erau in acelasi atom, dar la mii de caractere unul de altul.
    """
    r = json.load(open(os.path.join(_RAD, "artefacte", "potriviri.json"), encoding="utf-8"))
    P = {p["parametru"]: p for p in r["potriviri"]}
    for cheie in ("nesursat/salarizare._PCT_DEDUCERE_BAZA=0.20",
                  "nesursat/salarizare._PCT_DEDUCERE_BAZA=0.35"):
        assert P[cheie]["clasificare"] == "NEGASIT", (cheie, P[cheie].get("atom"))
    # iar cel corect din aceeasi familie rămâne confirmat
    bun = P["nesursat/salarizare.PRAG_VENIT_DEDUCERE=2000"]
    assert bun["clasificare"] == "CONCORDA"
    assert "Deducerea personală de bază" in bun["atom_verbatim"]
