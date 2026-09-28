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
