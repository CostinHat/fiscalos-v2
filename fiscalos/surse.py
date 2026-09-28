# -*- coding: utf-8 -*-
"""Ce fel de SURSA e un act din corpus - si deci ce are voie sa dovedeasca.

DECIZIA C2 (Costin): un temei se ia NUMAI dintr-un act normativ. "Un formular, o structura de
declaraţie sau un pliant ANAF nu poate fi temei." Aici se decide, mecanic si cu motiv scris, in care
clasa cade fiecare act.

DOUA SEMNALE, fiindca unul singur minte:
  1. PREFIXUL numelui (legea_, oug_, hg_, opanaf_ ...) - spune ce PRETINDE fisierul ca e.
  2. PROVENIENTA.json din corpus - unde iConta declara ea insasi ce e fiecare fisier care nu se
     clasifica mecanic: ADUS (act oficial), ADUS_ADNOTAT (act oficial cu antet propriu), SCRIS (nota
     redactata de ei), DERIVAT_MANUAL.
Masurat, prefixul singur ar fi acceptat ca "act normativ" trei note scrise de iConta:
`hg518_1995_diurna_externa`, `hg714_2018_diurna_interna` si `cf_art291_2016_forma_initiala` - nume de
act, conţinut de nota. Ultima e citata chiar din registrul COTE al iConta, ca temei de nivel MO, pentru
cotele reduse de TVA din 2016. O valoare verificata pe o nota scrisa de cel verificat nu e o
verificare: e o tautologie.
"""
import json
import os
import re

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# prefixe de act normativ: lege, ordonanţa, hotarare, ordin, cod
_NORMATIV = re.compile(r"^(cod|cf|legea|lege|oug|og|hg|omfp|omf|oms|opanaf|ordin)(_|\d)", re.I)
# ce nu e act normativ chiar daca poarta un asemenea prefix
_FORMULAR = re.compile(r"struct|structura|_xml|xml_|istoriaversiunilor", re.I)
_MOTIVE_PREFIX = {
    "anaf": "pliant sau ghid ANAF - material de informare, nu act normativ",
    "d": "formular sau structura de declaratie ANAF",
    "structura": "structura de declaratie (specificatie de formular)",
    "structuraxml": "structura XML de declaratie",
    "raport": "raport redactat, nu act",
    "impozit": "nota redactata",
    "gresit": "fisier marcat GRESIT de iConta insasi (act adus greșit)",
}


def _provenienta():
    cale = os.path.join(_RAD, "corpus", "PROVENIENTA.json")
    try:
        return json.load(open(cale, encoding="utf-8")).get("fisiere", {})
    except (OSError, ValueError):
        return {}


_PROV = None


def clasa_provenienta(baza):
    """Clasa din PROVENIENTA.json pentru orice forma a actului (.txt/.html/.pdf), sau 'ADUS' implicit.

    PROVENIENTA listeaza doar fisierele care NU se clasifica mecanic; restul sunt, prin constructie,
    acte ADUSE (vezi antetul ei)."""
    global _PROV
    if _PROV is None:
        _PROV = _provenienta()
    nume = os.path.basename(baza)
    for fis, v in _PROV.items():
        if os.path.splitext(fis)[0] == nume:
            return v.get("clasa", "ADUS"), v.get("motiv", "")
    return "ADUS", ""


def e_act_normativ(baza):
    """(True/False, motiv). `baza` e radacina de nume din corpus (ex. `cod_fiscal_227_2015_consolidat`)."""
    nume = os.path.basename(baza)
    clasa, motiv_prov = clasa_provenienta(baza)
    if clasa in ("SCRIS", "DERIVAT_MANUAL"):
        return False, ("nota redactata de iConta (PROVENIENTA: %s - %s), nu act normativ"
                       % (clasa, motiv_prov[:90]))
    if nume.upper().startswith("GRESIT"):
        return False, _MOTIVE_PREFIX["gresit"]
    if _FORMULAR.search(nume):
        return False, "structura sau formular de declaratie, nu act normativ"
    if _NORMATIV.match(nume):
        return True, "act normativ (%s)" % nume.split("_")[0]
    pref = re.match(r"([a-zA-Z]+)", nume)
    pref = pref.group(1).lower() if pref else ""
    return False, _MOTIVE_PREFIX.get(pref, "nu are forma unui act normativ (%s)" % pref)


def acte_modificatoare(corp):
    """Actele ale caror articole PROPRII (de nivel superior) sunt in majoritate romane: acte care
    modifica alte acte (Legea 141/2025, OUG 115/2023, OG 16/2022). Semnalul e structural, acelasi pe
    care il foloseste motorul de intrebari (D3b)."""
    # Articole romane NU inseamna automat act modificator: HG 1/2016 are "Art. I - Se aproba Normele
    # metodologice", deci articole proprii romane, dar nu modifica nimic. Masurat: fara conditia de
    # mai jos, normele Codului fiscal devenau "actul modificator care introduce valoarea" pentru cota
    # de impozit pe venit. Se cere si o INTERVENTIE reala, in textul actului.
    ies = set()
    for act, ats in corp.pe_act.items():
        # NORMELE DE APLICARE nu sunt act modificator, ci text de baza - cel pe care il citeaza un
        # contabil ("pct. 103 din Norme"). Redarea lor consolidata conţine insa articole romane CITATE
        # din hotararile care le-au modificat ("Art. V din HOTĂRÂREA nr. ... se abroga"), deci trec de
        # ambele teste structurale de mai jos. Masurat: HG 1/2016 are 0 puncte de interventie proprii
        # din 3725 de atomi, la fel ca Legea 296/2023 (aplatizata) - structura nu le separa; functia da.
        if "norme" in act:
            continue
        arts = [a for a in ats if a["nivel"] == "articol" and a.get("parinte") is None]
        rom = sum(1 for a in arts if re.match(r"^[IVXLCDM]+$", str(a["cheie"])))
        if not arts or rom < 0.5 * len(arts):
            continue
        if any(_INTERVENTIE_TXT.search(a["text"]) for a in ats[:400]):
            ies.add(act)
    return ies


# Formulele de interventie, in variantele gasite in corpus: legile scriu "se modifica si va avea
# urmatorul cuprins", ordinele OPANAF "se modifica si se inlocuieste cu anexa...". Prima varianta a
# regulii le cerea pe cele din lege si a pierdut ordinele (OPANAF 2194/2025 modifica OPANAF 3769/2015).
_INTERVENTIE_TXT = re.compile(r"se modific[aă] (si|și) (se |va |vor )|se completeaz[aă]|"
                              r"se introduc(e)? (un|o|dou[aă]|trei|patru|noi)|se abrog[aă]\b|"
                              r"se [iî]nlocuie[sș]te cu", re.I)
_TINTA = re.compile(r"\b(Legea|Ordonan[tţț]a de urgen[tţț][aă] a Guvernului|Ordonan[tţț]a Guvernului|"
                    r"Hot[aă]r[aâ]rea Guvernului|Ordinul[^,]{0,120}?)\s+nr\.\s*([\d.]+)/(\d{4})", re.I)
_TIP_TINTA = [("urgen", "oug"), ("ordonan", "og"), ("hot", "hg"), ("ordin", "o"), ("lege", "legea")]


def tinta_modificarii(corp, atom):
    """(nume_citit, act_din_corpus_sau_None) - actul pe care il modifica atomul unui act modificator.

    Se citeste din textul articolului roman gazda ("Legea nr. 227/2015 privind Codul fiscal ... se
    modifica si se completeaza dupa cum urmeaza:"). Decizia C10 cere sa se scrie EXPLICIT cand actul
    de baza consolidat lipseste din corpus - deci lipsa trebuie constatata, nu dedusa din faptul ca
    potrivirea n-a gasit nimic."""
    # Tinta se numeste in ARTICOLUL ROMAN gazda. Un atom citat adanc (articol arab citat sub un punct
    # de interventie) nu o poarta; se urca pe lanţul de parinţi pana la primul articol roman.
    lant, x = [], atom
    while x is not None:
        lant.append(x)
        x = corp.dupa_id.get(x.get("parinte")) if x.get("parinte") else None
    romane = [y for y in lant if y["nivel"] == "articol" and re.match(r"^[IVXLCDM]+$", str(y["cheie"]))]
    if not romane:
        # Unele redari APLATIZEAZA textul citat: Legea 296/2023 pune CF art. 500^2 la nivelul
        # superior, fara parinte roman. Atunci contextul interventiei e ultimul articol roman care il
        # PRECEDE in act - ordinea din text.
        ats = corp.pe_act[atom["act"]]
        i = next((k for k, y in enumerate(ats) if y["id"] == atom["id"]), None)
        if i is not None:
            for y in reversed(ats[:i]):
                if y["nivel"] == "articol" and re.match(r"^[IVXLCDM]+$", str(y["cheie"])):
                    romane = [y]
                    break
    texte = [y["text"] for y in romane] + [atom["text"]]
    for txt in texte:
        m = _TINTA.search(txt[:600])
        if not m:
            continue
        tip = next((t for k, t in _TIP_TINTA if k in m.group(1).lower()), "act")
        nr, an = m.group(2).replace(".", ""), m.group(3)
        nume = "%s %s/%s" % (m.group(1).split()[0], nr, an)
        if (nr, an) == ("227", "2015"):
            cand = ["cod_fiscal_227_2015_consolidat"]
        elif (nr, an) == ("207", "2015"):
            cand = ["legea_207_2015_consolidat"]
        else:
            cand = sorted((b for b in corp.pe_act if "_%s_%s" % (nr, an) in b
                           and b != atom["act"]),
                          key=lambda b: ("consolidat" not in b, len(b)))
        return nume, (cand[0] if cand and cand[0] in corp.pe_act else None)
    return None, None



def e_act_de_baza(act, modificatoare):
    """Actul pe care il citeaza un contabil: normativ, nemodificator, neistoric.

    Decizia C10: temeiul candidat e actul de baza consolidat; actul modificator apare doar ca
    atom-valabilitate in perechea C4."""
    if act in modificatoare or not e_act_normativ(act)[0]:
        return False
    return "forma_initiala" not in act and "_pre_" not in act
