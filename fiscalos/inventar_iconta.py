# -*- coding: utf-8 -*-
"""OP5 — INVENTARUL parametrilor fiscali ai iConta, prin CITIRE.

DE CE AST SI NU IMPORT. Un `import core.common` ar executa codul iConta si ar scrie `__pycache__/`
in arborele lui - adica ar incalca CLAUDE.md §1 tocmai in pasul care pretinde ca doar citeste.
Deci fiecare valoare se ia din arborele sintactic, cu un evaluator care cunoaste EXACT formele din
codul lor (`date(...)`, `Decimal("...")`, `Temei(...)`) si refuza restul. Un apel necunoscut nu se
aproximeaza - se noteaza ca neevaluat si se vede in inventar.

CE SE INVENTARIAZA, si de ce ASA. Nu "toate numerele din iConta" - asta a fost drumul care a produs
460 de tichete. Se inventariaza clasele de parametri pe care iConta le TRATEAZA ca fiscale, adica
acolo unde codul lor are deja o structura pentru asta:

  cota, plafon   `core/common.py` -> `COTE`: (valabil_din, valoare, Temei) per cheie. Registrul lor
                 declara si TEMEIUL si CITATUL - deci se poate verifica nu doar valoarea, ci si daca
                 citarea se rezolva in corpus. Asta e partea cea mai utila a livrabilului.
  termen         `core/scadente.py` -> `TEMEI_TERMEN` (3 sursate) + `_ZIUA`/`_ULTIMA_ZI` (ziua reala
                 folosita la calcul, sursata sau nu).
  nomenclator    `core/nomenclatoare.py` -> `ANCORE_NORMA`: enumerarea + norma care o inchide.
  cont           simbolurile de cont scrise literal in modulele de productie. Ele au o sursa
                 (planul de conturi din OMFP 1802/2014, aflat in corpus), dar codul nu o citeaza.
  cota/plafon    constante fiscale de modul FARA `Temei` in stramosi - clasa pe care propriul lor
  nesursat       clichet o numara. Aici intra ca parametri cu `temei_declarat = None`.

CE NU SE INVENTARIAZA, scris fiindca tacerea unui scan se citeste ca absenta: planul de conturi al
FIECAREI firme (e date in baza, nu cod), valorile operationale (praguri de blocare la login, TTL de
cache) - care n-au act normativ de citat -, si nomenclatoarele derivate din XSD-uri.
"""
import ast
import json
import os
import re
import time
from collections import OrderedDict

ICONTA = "/home/costin/iconta_nou"
_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# nume care marcheaza o constanta ca FISCALA (calibrat pe vocabularul registrului lor)
_NUME_FISCAL = re.compile(
    r"prag|plafon|cota|cote|salariu|salar|venit|impozit|contrib|\bcas\b|\bcass\b|\bcam\b|deduc|"
    r"scutir|termen|scadent|micro|profit|dividend|tichet|norma|minim|maxim|accaccciz|acciz", re.I)
# nume care marcheaza un nomenclator/cod (are sursa, dar ALTA - XSD, validator, algoritm)
_NUME_NOMENCLATOR = re.compile(
    r"_W$|_WEIGHT|_KEY$|CHEIE|CNP|CUI|JUD|SIRUTA|TIPURI|TIP_|_TIP|FORMA|LIMITE_TEXT|TAXCODE|COD_|"
    r"CODURI|CAEN|VALUT|TARA|_MAP$|SCHEMA|XSD|NOMENCL|SARB|HEADER|_STR_|_OPT$|_CAT_|CATEG", re.I)
_CONT = re.compile(r"^[1-8][0-9]{2,3}$")


# ── evaluator AST restrans ───────────────────────────────────────────────────────────────────────
class Neevaluabil(Exception):
    pass


def _ev(nod):
    """Evalueaza un nod AST la o valoare Python, cunoscand DOAR formele din codul iConta."""
    if isinstance(nod, ast.Constant):
        return nod.value
    if isinstance(nod, (ast.Tuple, ast.List)):
        return [_ev(e) for e in nod.elts]
    if isinstance(nod, ast.Set):
        return [_ev(e) for e in nod.elts]
    if isinstance(nod, ast.Dict):
        return OrderedDict((_cheie(k), _ev(v)) for k, v in zip(nod.keys, nod.values))
    if isinstance(nod, ast.UnaryOp) and isinstance(nod.op, ast.USub):
        return -_ev(nod.operand)
    if isinstance(nod, ast.Call):
        nume = _nume_apel(nod.func)
        args = [_ev(a) for a in nod.args]
        kw = {k.arg: _ev(k.value) for k in nod.keywords if k.arg}
        if nume == "date":
            return "%04d-%02d-%02d" % (args[0], args[1], args[2])
        if nume == "Decimal":
            return str(args[0])
        if nume == "Temei":
            # semnatura pozitionala din core/common.py: (tip, nr, an, art, alin, lit, ...)
            poz = ["tip", "nr", "an", "art", "alin", "lit"]
            t = {}
            for i, v in enumerate(args):
                if i < len(poz):
                    t[poz[i]] = v
            t.update(kw)
            t["_obiect"] = "Temei"
            return t
        if nume in ("Ancora", "Constrangere", "Dezacord"):
            d = dict(kw)
            d["_obiect"] = nume
            for i, v in enumerate(args):
                d["_poz%d" % i] = v
            return d
        if nume == "frozenset":
            return args[0] if args else []
        raise Neevaluabil(nume)
    if isinstance(nod, ast.Name):
        raise Neevaluabil("nume:" + nod.id)
    if isinstance(nod, ast.Attribute):
        raise Neevaluabil("atribut")
    raise Neevaluabil(type(nod).__name__)


def _cheie(nod):
    v = _ev(nod)
    return "|".join(str(x) for x in v) if isinstance(v, list) else str(v)


def _nume_apel(f):
    if isinstance(f, ast.Name):
        return f.id
    if isinstance(f, ast.Attribute):
        return f.attr
    return "?"


def _arbore(rel):
    cale = os.path.join(ICONTA, rel)
    with open(cale, encoding="utf-8") as f:            # "r": citire, niciodata scriere
        src = f.read()
    return ast.parse(src), src.splitlines()


def _atribuiri_modul(rel):
    """{nume: (nod_valoare, linie)} pentru atribuirile de la nivelul modulului."""
    arb, _linii = _arbore(rel)
    out = {}
    for n in arb.body:
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    out[t.id] = (n.value, n.lineno)
    return out


# ── clasificare cota / plafon ────────────────────────────────────────────────────────────────────
_PLAFON = re.compile(r"plafon|salariu|tichet|facilitate|prag|limita", re.I)


def _clasa_cheie(cheie):
    return "plafon" if _PLAFON.search(cheie) else "cota"


def _procent(v):
    """0.21 -> '21', 0.0225 -> '2,25'. Intoarce None cand valoarea nu e o rata."""
    try:
        from decimal import Decimal
        d = Decimal(str(v))
    except Exception:
        return None
    if d <= 0 or d >= 1:
        return None
    p = d * 100
    s = format(p.normalize(), "f")
    return s.replace(".", ",")


# ── extractoarele ────────────────────────────────────────────────────────────────────────────────
def din_registrul_cote():
    """`COTE` din core/common.py: fiecare (valabil_din, valoare, Temei) devine un parametru."""
    atrib = _atribuiri_modul("core/common.py")
    nod, linie0 = atrib["COTE"]
    par, probleme = [], []
    for k, v in zip(nod.keys, nod.values):
        cheie = _ev(k)
        for intrare in v.elts:
            try:
                val = _ev(intrare)
            except Neevaluabil as e:
                probleme.append({"cheie": cheie, "motiv": "neevaluabil: %s" % e})
                continue
            din, valoare, temei = val[0], val[1], (val[2] if len(val) > 2 else None)
            par.append({
                "id": "cote/%s@%s" % (cheie, din),
                "clasa": _clasa_cheie(cheie),
                "nume": cheie,
                "valoare_cod": str(valoare),
                "procent_cod": _procent(valoare),
                "valabil_din_cod": din,
                "unde": "core/common.py:%d (registrul COTE)" % intrare.lineno,
                "temei_declarat": temei if isinstance(temei, dict) else None,
                "sursa_inventar": "registru COTE",
            })
    return par, probleme


def din_scadente():
    """Termenele: cele 3 sursate (`TEMEI_TERMEN`) + ziua REAL folosita la calcul (`_ZIUA`)."""
    atrib = _atribuiri_modul("core/scadente.py")
    par = []
    nod, _l = atrib["TEMEI_TERMEN"]
    sursate = {}
    for k, v in zip(nod.keys, nod.values):
        tip = _ev(k)
        act, fisier, citat = _ev(v)
        sursate[tip] = {"act": act, "fisier": fisier, "text_citat": citat}
    ziua, _l = atrib["_ZIUA"]
    ziua = _ev(ziua)
    ultima, _l = atrib["_ULTIMA_ZI"]
    ultima = set(_ev(ultima))
    # ziua implicita 25 e un DEFAULT la .get(), nu o intrare din dict: se citeste din apel.
    arb, linii = _arbore("core/scadente.py")
    implicita, linie_impl = None, None
    for n in ast.walk(arb):
        if (isinstance(n, ast.Call) and _nume_apel(n.func) == "get" and len(n.args) == 2
                and isinstance(n.func, ast.Attribute) and isinstance(n.func.value, ast.Name)
                and n.func.value.id == "_ZIUA"):
            implicita = _ev(n.args[1])
            linie_impl = n.lineno
    tipuri = sorted(set(list(sursate) + list(ziua) + list(ultima)))
    for tip in tipuri:
        if tip in ultima:
            val, nota = "ultima_zi_luna", "tratat separat (_ULTIMA_ZI)"
        elif tip in ziua:
            val, nota = str(ziua[tip]), "_ZIUA[%r]" % tip
        else:
            val, nota = str(implicita), "default la _ZIUA.get(tip, %s) - linia %d" % (implicita, linie_impl)
        s = sursate.get(tip)
        par.append({
            "id": "termen/%s" % tip,
            "clasa": "termen",
            "nume": "termen_depunere_%s" % tip,
            "valoare_cod": val,
            "procent_cod": None,
            "valabil_din_cod": None,
            "unde": "core/scadente.py (%s)" % nota,
            "temei_declarat": ({"tip": "citare in proza", "text": s["act"],
                                "url": s["fisier"], "text_citat": s["text_citat"],
                                "_obiect": "TEMEI_TERMEN"} if s else None),
            "sursa_inventar": "scadente.TEMEI_TERMEN + _ZIUA",
        })
    return par, []


def _dezacorduri_declarate():
    """{(declaratie, cheie): {ce, consecinta, unde}} din apelurile `_dez(...)` din nomenclatoare.py.

    Decizia C9: DIFERA-ul pe d394.TIPURI poarta mentiunea ca iConta declara Î1/Î2 neconstruite.
    Mentiunea se ia din OBIECTUL `Dezacord` pe care iConta il construieste ea insasi, verbatim, nu
    dintr-un comentariu si nu parafrazata de noi."""
    arb, _l = _arbore("core/nomenclatoare.py")
    ies = {}
    for n in arb.body:
        if not (isinstance(n, ast.Expr) and isinstance(n.value, ast.Call)
                and _nume_apel(n.value.func) == "_dez" and n.value.args):
            continue
        try:
            cheie = tuple(_ev(n.value.args[0]))
            kw = {k.arg: _ev(k.value) for k in n.value.keywords if k.arg}
        except Neevaluabil:
            continue
        ies[cheie] = {"ce": kw.get("ce"), "consecinta": kw.get("consecinta"),
                      "unde": "core/nomenclatoare.py:%d (_dez)" % n.lineno}
    return ies


def din_nomenclatoare():
    """`ANCORE_NORMA`: enumerarea din cod + norma care pretinde ca o inchide."""
    atrib = _atribuiri_modul("core/nomenclatoare.py")
    nod, _l = atrib["ANCORE_NORMA"]
    dezacorduri = _dezacorduri_declarate()
    par, probleme = [], []
    for k, v in zip(nod.keys, nod.values):
        cheie = _cheie(k).replace("|", ".")
        try:
            a = _ev(v)
        except Neevaluabil as e:
            probleme.append({"cheie": cheie, "motiv": "neevaluabil: %s" % e})
            continue
        enumerare = a.get("enumerare")
        par.append({
            "id": "nomenclator/%s" % cheie,
            "clasa": "nomenclator",
            "nume": cheie,
            "valoare_cod": ",".join(enumerare) if enumerare else None,
            "procent_cod": None,
            "valabil_din_cod": (a.get("norma") or {}).get("data_in"),
            "unde": "core/nomenclatoare.py:%d (ANCORE_NORMA)" % v.lineno,
            "temei_declarat": a.get("norma"),
            "deschis": bool(a.get("deschis")),
            "dezacord_declarat": dezacorduri.get(tuple(_ev(k))),
            "sursa_inventar": "nomenclatoare.ANCORE_NORMA",
        })
    return par, probleme


def _nume_de_cont(nume):
    """iConta numeste ea insasi un container de conturi: CONTURI_TVA, CONT_AVANS, cont_imo, cont.

    Se cere TOKENUL `cont`/`conturi` (numele taiat pe `_`), nu subsirul: altfel `DECONT_LUNG`,
    `control`, `contrib`, `contracte` si `continut` - toate masurate in core/ - ar trece drept conturi.
    """
    return any(t.lower() in ("cont", "conturi") for t in nume.split("_") if t)


def din_conturi():
    """Simbolurile de cont, culese NUMAI de unde iConta le foloseste ca CONTURI.

    DECIZIA C3 (Costin): "zgomotul nu se accepta intr-o propunere de aprobat uman. Conturile se culeg
    doar din locurile unde iConta le foloseste ca conturi, nu din orice literal de 3-4 cifre."
    Prima versiune lua orice literal de 3-4 cifre folosit in >=3 locuri si a adus in propunere `2015`
    (un an), `5000` (un plafon), `100`/`102` (randuri de formular).

    SEMNALUL de acum e numele pe care IConta il da containerului: un literal conteaza ca simbol de cont
    numai daca sta in partea dreapta a unei atribuiri al carei nume poarta tokenul `cont`/`conturi`.
    E numirea lor, nu ghicirea noastra. Masurat: 62 de simboluri marcate astfel, 364 nemarcate.

    CE SE PIERDE, si se scrie: cele 364 nemarcate nu sunt neaparat altceva decat conturi - multe sunt
    conturi reale folosite ca literale directe (`startswith("401")`, tuple pozitionale). Ele nu se pot
    distinge de un an sau de un rand de formular FARA o modificare in iConta. Deci nu intra in
    propunere; intra ca CERINTA pentru iConta (`conturi_nemarcate`), cu numarul lor.
    """
    folos, nemarcate = {}, {}
    rad = os.path.join(ICONTA, "core")
    for nume in sorted(os.listdir(rad)):
        if not nume.endswith(".py") or nume.startswith("test_") or nume.startswith("proba"):
            continue
        cale = os.path.join(rad, nume)
        try:
            with open(cale, encoding="utf-8") as f:
                arb = ast.parse(f.read())
        except (SyntaxError, OSError):
            continue
        marcate_aici = set()
        for n in ast.walk(arb):
            if not isinstance(n, ast.Assign):
                continue
            tinte = [t.id for t in n.targets if isinstance(t, ast.Name)]
            if not tinte or not _nume_de_cont(tinte[0]):
                continue
            for sub in ast.walk(n.value):
                if (isinstance(sub, ast.Constant) and isinstance(sub.value, str)
                        and _CONT.match(sub.value)):
                    folos.setdefault(sub.value, []).append("%s:%d %s" % (nume, sub.lineno, tinte[0]))
                    marcate_aici.add(id(sub))
        for n in ast.walk(arb):
            if (isinstance(n, ast.Constant) and isinstance(n.value, str) and _CONT.match(n.value)
                    and id(n) not in marcate_aici):
                nemarcate.setdefault(n.value, set()).add(nume)
    par = []
    for cont in sorted(folos):
        locuri = folos[cont]
        par.append({
            "id": "cont/%s" % cont,
            "clasa": "cont",
            "nume": "cont_%s" % cont,
            "valoare_cod": cont,
            "procent_cod": None,
            "valabil_din_cod": None,
            "unde": "core/ in %d locuri: %s" % (len(locuri), ", ".join(locuri[:3])),
            "temei_declarat": None,
            "sursa_inventar": "simbol de cont in container numit de iConta ca CONT",
        })
    doar_nemarcate = {k: v for k, v in nemarcate.items() if k not in folos}
    CONTURI_NEMARCATE.clear()
    CONTURI_NEMARCATE.update({"n_simboluri": len(doar_nemarcate),
                              "exemple": sorted(doar_nemarcate)[:25],
                              "n_module": len({m for v in doar_nemarcate.values() for m in v})})
    return par, []


CONTURI_NEMARCATE = {}


# `Temei` e importat sub alias in unele module (`from core.common import Temei as _Tm` in d101.py).
# Un scan care cauta litera "Temei(" il rateaza - si atunci NUMERELE CITARII (296, 2023, 89, 2025)
# intra in inventar ca valori fiscale. Masurat: 10 din primele 68 de intrari erau numere de act si
# ani de publicare, nu parametri. O citare nu e o valoare.
_APEL_TEMEI = re.compile(r"^(Temei|_Tm|_Temei|T)$")


def _valori_literale(nod):
    """Literalii din POZITII DE VALOARE dintr-o expresie: nu cheile de dict, nu argumentele unui apel.

    DE CE POZITIA si nu forma. `_PCT_DEDUCERE_BAZA = {0: Decimal("0.20"), ...}` are cheile 0..4 =
    numarul persoanelor in intretinere, nu procente; `PLAFOANE_VENIT_2025 = plafoane_an(2025)` are
    2025 = anul, nu un plafon; `_Tm("Legea", 296, 2023, ...)` are numarul si anul ACTULUI. Toate trei
    sunt numere intr-o atribuire fiscala, si niciunul nu e un parametru. Ce le distinge e locul, nu
    valoarea - deci se culege pe loc: RHS direct, elementele unei liste/tuple/set, VALORILE unui dict,
    si argumentul lui `Decimal(...)`. Argumentele oricarui alt apel se sar.
    """
    ies = []
    if isinstance(nod, ast.Constant):
        if isinstance(nod.value, (int, float)) and not isinstance(nod.value, bool):
            ies.append(nod.value)
        return ies
    if isinstance(nod, (ast.List, ast.Tuple, ast.Set)):
        for e in nod.elts:
            ies.extend(_valori_literale(e))
        return ies
    if isinstance(nod, ast.Dict):
        for v in nod.values:                       # cheile NU sunt valori
            ies.extend(_valori_literale(v))
        return ies
    if isinstance(nod, ast.UnaryOp) and isinstance(nod.op, ast.USub):
        return [-v for v in _valori_literale(nod.operand)]
    if isinstance(nod, ast.Call):
        nume = _nume_apel(nod.func)
        if nume == "Decimal" and nod.args:
            try:
                return [_ev(nod.args[0])]
            except Neevaluabil:
                return []
        return []                                  # argumentele altui apel: citare sau parametru tehnic
    return ies


def _folosit_ca_procent(arb, nume_c):
    """True daca modulul imparte constanta la 100 (`X * NUME / 100`) - adica NUME e un PROCENT
    LITERAL (0.3 = 0,3%), nu o fractie (0.21 = 21%).

    DE CE DIN FOLOSIRE. Registrul COTE tine ratele ca fracţii (0.21), dar constantele nesursate nu au
    o convenţie: `d216.COTA_IMPOZIT = 0.3` e folosita ca `baza * COTA_IMPOZIT / 100`, deci inseamna
    0,3% - impozitul special pe bunuri de valoare mare din Legea 296/2023. Citita ca fractie, devenea
    30%, iar potrivirea ii gasea un "temei candidat" in normele despre coeficienţii impozitului pe
    cladiri. Literalul singur nu spune unitatea; codul care il foloseste o spune.
    """
    for n in ast.walk(arb):
        if (isinstance(n, ast.BinOp) and isinstance(n.op, ast.Div)
                and isinstance(n.right, ast.Constant) and n.right.value in (100, 100.0)):
            if any(isinstance(x, ast.Name) and x.id == nume_c for x in ast.walk(n.left)):
                return True
    return False


def din_constante_nesursate():
    """Constante fiscale de MODUL fara `Temei` in stramosi - clasa pe care clichetul lor o numara.

    Se exclud: valorile din registrul COTE (deja inventariate), nomenclatoarele (au alta sursa),
    numerele de structura (0/1/-1/2/100), si tot ce nu sta pe o POZITIE DE VALOARE (vezi
    `_valori_literale`). Ce rămâne intra cu `temei_declarat = None`.
    """
    rad = os.path.join(ICONTA, "core")
    structura = {0, 1, -1, 2, 100}
    par = []
    for nume in sorted(os.listdir(rad)):
        if not nume.endswith(".py") or nume.startswith("test_") or nume in ("common.py",
                                                                            "scan_constante.py"):
            continue
        try:
            with open(os.path.join(rad, nume), encoding="utf-8") as f:
                src = f.read()
            arb = ast.parse(src)
        except (SyntaxError, OSError):
            continue
        if "Temei(" in src:
            pass                      # modulul poate avea si sursate si nesursate: se filtreaza per nod
        for n in arb.body:
            if not isinstance(n, ast.Assign):
                continue
            ținte = [t.id for t in n.targets if isinstance(t, ast.Name)]
            if not ținte:
                continue
            nume_c = ținte[0]
            if not _NUME_FISCAL.search(nume_c) or _NUME_NOMENCLATOR.search(nume_c):
                continue
            # SURSAT = un apel de temei apare oriunde in expresie, sub orice alias.
            if any(isinstance(x, ast.Call) and _APEL_TEMEI.match(_nume_apel(x.func))
                   for x in ast.walk(n.value)):
                continue
            ca_procent = _folosit_ca_procent(arb, nume_c)
            for v in _valori_literale(n.value):
                if v in structura:
                    continue
                par.append({
                    "unitate": "procent_literal" if ca_procent else None,
                    "id": "nesursat/%s.%s=%s" % (nume[:-3], nume_c, v),
                    "clasa": _clasa_cheie(nume_c),
                    "nume": nume_c,
                    "valoare_cod": str(v),
                    "procent_cod": _procent(v),
                    "valabil_din_cod": None,
                    "unde": "core/%s:%d" % (nume, n.lineno),
                    "temei_declarat": None,
                    "sursa_inventar": "constanta fiscala de modul, fara Temei",
                })
    return par, []


def inventariaza():
    t0 = time.time()
    par, probleme = [], []
    for f in (din_registrul_cote, din_scadente, din_nomenclatoare, din_conturi,
              din_constante_nesursate):
        p, pr = f()
        par.extend(p)
        probleme.extend({"extractor": f.__name__, **x} for x in pr)
    vazut = set()
    unic = []
    for p in par:
        if p["id"] in vazut:
            continue
        vazut.add(p["id"])
        unic.append(p)
    pe_clasa = {}
    for p in unic:
        pe_clasa[p["clasa"]] = pe_clasa.get(p["clasa"], 0) + 1
    raport = {
        "_ce": "OP5 inventarul parametrilor fiscali ai iConta, prin CITIRE (AST, fara import - un "
               "import ar scrie __pycache__ in arborele iConta, deci ar incalca CLAUDE.md §1).",
        "iconta": ICONTA,
        "facut_la": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "n_parametri": len(unic), "pe_clasa": pe_clasa,
        "cu_temei_declarat": sum(1 for p in unic if p["temei_declarat"]),
        "fara_temei_declarat": sum(1 for p in unic if not p["temei_declarat"]),
        "probleme": probleme,
        "conturi_nemarcate": dict(CONTURI_NEMARCATE),
        "parametri": unic,
        "secunde": round(time.time() - t0, 2),
    }
    with open(os.path.join(_RAD, "artefacte", "inventar_iconta.json"), "w", encoding="utf-8") as f:
        json.dump(raport, f, ensure_ascii=False, indent=1, sort_keys=True)
    return raport


if __name__ == "__main__":
    r = inventariaza()
    print("inventar: %d parametri, %s, cu temei declarat %d / fara %d, %.1f s"
          % (r["n_parametri"], r["pe_clasa"], r["cu_temei_declarat"], r["fara_temei_declarat"],
             r["secunde"]))
    if r["probleme"]:
        print("probleme:", r["probleme"][:5])
