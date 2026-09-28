# -*- coding: utf-8 -*-
"""Stratul semantic v4 — NAVIGARE STRUCTURALA si CALCUL evaluat de cod (deciziile 6 si 7).

DE CE NAVIGARE. In v3, majoritatea abtinerilor stratului semantic au fost "atomii primiti nu conţin
regula": un esec de REGASIRE, nu de model. Contextul era fix, ales de o cautare lexicala. Aici
modelul cere singur atomi, prin STRUCTURA actului (act -> titlu/capitol -> articol -> alineat) si prin
relatiile de modificare/derogare, cu un numar LIMITAT de pasi. Cautarea lexicala rămâne doar un punct
de intrare.

CE NU SE SCHIMBA: verificarea mecanica. Citatele se cauta literal in textul COMPLET al atomului, cifrele
dupa regula C13, derogarile dupa C17 (b) - `semantic.verifica`, neschimbata. Modelul poate cita numai
atomi pe care i i-au aratat tool-urile.

CALCULUL (decizia 7): modelul NU calculeaza. Propune o formula cu operanzi numiti; fiecare operand are
o SURSA - un fragment literal dintr-un atom sau din intrebare (C13: o valoare legala numai din atom).
Codul evalueaza formula (numai + - * /, min, max, zile(a, b)) si pune rezultatul in raspuns, cu formula
si sursa fiecarui operand. Un operand fara sursa, sau a carui valoare nu apare literal in sursa ei,
respinge raspunsul. Singurele constante permise fara sursa sunt 1 si 100 (unitati, nu valori).

v5 (deciziile C23, C25, C27, C28, C29, dupa rularea v4):
  C23  campul `raspuns` e validat STRUCTURAL inainte de verificare: nu gol, nu "x"/"-", fara marcaj de
       parametri scurs ("</declaratie><parameter name=...>"), nu continutul altui camp. La esec: O
       singura reincercare, apoi abtinere cu motivul scris.
  C25  fiecare operand are o ETICHETA: FAPT_CAZ (din intrebare; acceptat numai daca valoarea apare
       literal in intrebare) sau VALOARE_LEGALA (din atom; cere atom aratat si fragment verbatim).
  C27  data de referinta se stabileste pentru FAPTUL intrebat si se declara in raspuns. Cand intrebarea
       poarta mai multe date, modelul alege una dintre ele si spune de ce; daca nu reiese la care se
       refera faptul, raspunsul e INCOMPLET - nu cea mai veche data.
  C28  calculul se afiseaza pas cu pas: fiecare formula cu valorile puse in ea, fiecare zile(a, b).
  C29  limita e 20 de pasi; o cerere peste limita = abtinere, cu traseul navigarii.
"""
import ast
import datetime
import json
import os
import re
import time
from decimal import Decimal, InvalidOperation

from fiscalos import intrebari, potrivire, semantic

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = semantic.MODEL
MAX_PASI = 20
MAX_TEXT = 3500

SISTEM = semantic.SISTEM.replace(
    "Primești o întrebare de fiscalitate românească, data de referință la care trebuie să fie valabil "
    "răspunsul și un set de ATOMI: fragmente de acte normative, fiecare cu un id. Atomii au fost aleși "
    "de o căutare mecanică și sunt, toți, în vigoare la data de referință.",
    "Primești o întrebare de fiscalitate românească și data de referință la care trebuie să fie valabil "
    "răspunsul. Atomii (fragmente de acte normative, fiecare cu un id) NU îi primești gata aleși: îi "
    "găsești singur, navigând.") + """

NAVIGARE. Ai patru unelte:
- `cauta(interogare)` — căutare lexicală; e doar un PUNCT DE INTRARE, nu răspunsul.
- `cuprins(act, filtru)` — structura unui act: titlurile/capitolele, articolele și ANEXELE lui; cu \\
`filtru`, numai articolele (cu denumirea marginală) și punctele de anexă care conțin cuvintele date. \\
Anexele (norme metodologice, reglementări contabile, instrucțiuni de formular) au id-uri proprii \\
(`act#anexa/pct238/alin2`) și se citează ca atare.
- `deschide(id)` — textul unui atom, părintele, copiii (alineate, litere, puncte) și RELAȚIILE lui: \\
atomii care derogă de la el, fac excepție de la el sau îl modifică, și cei de la care derogă el.
- `raspunde(...)` — răspunsul final, o singură dată.
Ai cel mult %d pași de navigare; fiecare rezultat îți spune câți au rămas. O cerere peste limită \\
încheie întrebarea cu abținere. Navighează ca un contabil: găsește actul și articolul potrivit prin \\
structură, deschide-l, urmează relațiile lui de derogare, apoi răspunde. Poți cita numai atomi pe care \\
o unealtă ți i-a arătat.

DATA DE REFERINȚĂ (C27). Data se stabilește pentru FAPTUL ÎNTREBAT. Primești datele pe care le poartă \\
întrebarea (`date_din_intrebare`). Dacă e una singură, ea e data. Dacă sunt mai multe, alegi pe cea la \\
care se referă faptul întrebat (de ex. „cifra de afaceri 2025 … cât impozit datorează pentru 2026" → \\
faptul întrebat e impozitul pentru 2026) și o scrii în `data_referinta` (AAAA-LL-ZZ, exact una dintre \\
cele primite), cu motivul în `data_referinta_motiv`. Dacă nu reiese la care dată se referă faptul, \\
răspunzi INCOMPLET — nu alegi data cea mai veche. Unealtele îți arată atomii în vigoare la cea mai \\
recentă dintre date; citezi numai atomi în vigoare la data aleasă.

RĂSPUNSUL FINAL (C23). Fiecare câmp al lui `raspunde` își conține numai propriul text: răspunsul \\
complet în `raspuns` (niciodată gol, niciodată „x" sau „-"), declarația în `declaratie`. Nu scrie \\
marcaj de parametri în valori.

CALCUL. Nu calculezi. Dacă răspunsul cere un calcul, îl descrii în `calcule`: fiecare calcul are un \\
`nume`, o `formula` (numai numele operanzilor și ale calculelor anterioare, + - * / paranteze, \\
min(), max(), zile(data1, data2) = numărul de zile de la data1 la data2) și lista de `operanzi`. \\
Fiecare operand are `valoare` scrisă exact ca în sursă (ex. "21%%", "100.000", "25.03.2026") și o \\
`eticheta` (C25): FAPT_CAZ — o valoare a cazului, luată din întrebare (`atom` gol, `fragment` = bucata \\
din întrebare care o conține); sau VALOARE_LEGALA — o cotă, un plafon, un termen, o limită, luată dintr-un \\
atom (`atom` = id-ul, `fragment` = bucata literală din atom). O valoare legală nu e niciodată FAPT_CAZ, \\
chiar dacă întrebarea o repetă. Singurele constante permise fără sursă sunt 1 și 100. În `raspuns` pui \\
rezultatul unui calcul ca {nume}; codul îl evaluează, îl înlocuiește și afișează calculul pas cu pas.""" % MAX_PASI

_CALC = {"type": "array", "items": {"type": "object", "properties": {
    "nume": {"type": "string"}, "formula": {"type": "string"},
    "operanzi": {"type": "array", "items": {"type": "object", "properties": {
        "nume": {"type": "string"}, "valoare": {"type": "string"},
        "eticheta": {"type": "string", "enum": ["FAPT_CAZ", "VALOARE_LEGALA"]},
        "atom": {"type": "string"}, "fragment": {"type": "string"}},
        "required": ["nume", "valoare", "eticheta", "atom", "fragment"], "additionalProperties": False}}},
    "required": ["nume", "formula", "operanzi"], "additionalProperties": False}}
SCHEMA = json.loads(json.dumps(semantic.SCHEMA))
SCHEMA["properties"]["calcule"] = _CALC
SCHEMA["properties"]["data_referinta"] = {"type": "string"}
SCHEMA["properties"]["data_referinta_motiv"] = {"type": "string"}
SCHEMA["required"] = SCHEMA["required"] + ["calcule", "data_referinta", "data_referinta_motiv"]

UNELTE = [
    {"name": "cauta", "strict": True,
     "description": "Cautare lexicala in corpusul de acte normative. Punct de intrare: intoarce atomi "
                    "(id, temei, inceputul textului). Nu inlocuieste deschiderea atomului.",
     "input_schema": {"type": "object", "properties": {"interogare": {"type": "string"}},
                      "required": ["interogare"], "additionalProperties": False}},
    {"name": "cuprins", "strict": True,
     "description": "Structura unui act: fara filtru, titlurile/capitolele lui; cu filtru, articolele "
                    "ale caror denumiri marginale sau titluri conţin cuvintele date (id + denumire).",
     "input_schema": {"type": "object", "properties": {"act": {"type": "string"},
                                                        "filtru": {"type": "string"}},
                      "required": ["act", "filtru"], "additionalProperties": False}},
    {"name": "deschide", "strict": True,
     "description": "Deschide un atom dupa id: textul lui, parintele, copiii si relatiile de derogare/"
                    "exceptie/modificare (in ambele sensuri), valabile la data de referinta.",
     "input_schema": {"type": "object", "properties": {"id": {"type": "string"}},
                      "required": ["id"], "additionalProperties": False}},
    {"name": "raspunde", "strict": True,
     "description": "Raspunsul final. Se apeleaza o singura data, la sfarsit.",
     "input_schema": SCHEMA},
]


# ── uneltele, executate de cod ───────────────────────────────────────────────────────────────────
class Navigator(object):
    def __init__(self, idx, rel, data_ref):
        self.idx, self.rel, self.data_ref = idx, rel, data_ref
        self.corp = idx.corp
        self.vazuti = {}                      # id -> atom: tot ce i s-a aratat modelului
        self.relatie = {}                     # sursa -> [(fel, tinta)] aratate modelului (C17 b)
        self.pasi = []

    def _valid(self, a):
        return not (self.data_ref and a.get("valabil_din") and a["valabil_din"] > self.data_ref) \
            and not a.get("abrogat")

    def _vede(self, a):
        self.vazuti[a["id"]] = a

    def cauta(self, interogare):
        hit = self.idx.cauta(interogare, self.data_ref, k=8)
        ies = []
        for s, a in hit:
            self._vede(a)
            ies.append({"id": a["id"], "temei": intrebari.temei_uman(a),
                        "text": " ".join(a["text"].split("⟦NOTĂ⟧")[0].split())[:220]})
        return {"rezultate": ies}

    def cuprins(self, act, filtru):
        if act not in self.corp.pe_act:
            cand = [b for b in self.corp.pe_act if act.lower() in b.lower()][:15]
            return {"eroare": "act necunoscut", "acte_asemanatoare": cand}
        ats = [a for a in self.corp.pe_act[act] if a["nivel"] == "articol" and self._valid(a)]
        # C26: anexele si punctele lor de prim nivel sunt unitati navigabile, ca articolele
        anexe = [a for a in self.corp.pe_act[act] if a["nivel"] == "anexa" and self._valid(a)]
        id_anexe = {a["id"] for a in anexe}
        pct_anexa = [a for a in self.corp.pe_act[act] if a.get("parinte") in id_anexe
                     and a["nivel"] == "punct" and self._valid(a)]
        if not filtru.strip():
            for a in anexe:
                self._vede(a)
            # in ordinea actului: fiecare portiune continua sub acelasi titlu/capitol
            grupe = []
            for a in ats:
                t = a.get("titlu_structural") or "(fara titlu)"
                if not grupe or grupe[-1][0] != t:
                    grupe.append((t, []))
                grupe[-1][1].append(a["cheie"])
            return {"act": act, "sursa": self.corp.sursa_act.get(act, {}).get("sursa"),
                    "nota": "pentru denumirile articolelor si punctele anexelor, cere `cuprins` cu un filtru",
                    "titluri": [{"titlu": t, "articole": "%s..%s (%d)" % (v[0], v[-1], len(v))}
                                for t, v in grupe[:120]],
                    "anexe": [{"id": a["id"], "titlu": " ".join(a["text"].split())[:120],
                               "puncte": sum(1 for x in pct_anexa if x["parinte"] == a["id"])}
                              for a in anexe[:60]]}
        st = set(intrebari._stemuri(intrebari._extinde(filtru)))
        ies = []
        for a in ats:
            den = " ".join(a["text"].split())[:160] if len(a["text"]) <= 250 else ""
            ctx = potrivire.norm(den + " " + (a.get("titlu_structural") or ""))
            n = sum(1 for x in st if x in ctx)
            if n:
                ies.append((n, a, den))
        for a in pct_anexa:
            inc = " ".join(a["text"].split())[:160]
            if not inc:                                  # "238." / "- (1) ...": inceputul e in copil
                copil = next((x for x in self.corp.pe_act[act] if x.get("parinte") == a["id"]), None)
                inc = " ".join((copil or {}).get("text", "").split())[:160]
            ctx = potrivire.norm(inc + " " + (a.get("titlu_structural") or "") + " " + (a.get("titlul") or ""))
            n = sum(1 for x in st if x in ctx)
            if n:
                ies.append((n, a, inc))
        ies.sort(key=lambda t: -t[0])
        for _n, a, _d in ies[:40]:
            self._vede(a)
        return {"act": act, "articole": [{"id": a["id"], "denumire": d,
                                          "titlu": a.get("titlu_structural")} for _n, a, d in ies[:40]]}

    def deschide(self, aid):
        a = self.corp.dupa_id.get(aid)
        if a is None:
            return {"eroare": "id necunoscut: %s" % aid}
        if not self._valid(a):
            return {"eroare": "atomul %s nu e in vigoare la %s" % (aid, self.data_ref)}
        self._vede(a)
        txt = a["text"]
        trunchiat = len(txt) > MAX_TEXT
        copii = [x for x in self.corp.pe_act[a["act"]] if x.get("parinte") == aid and self._valid(x)]
        for x in copii:
            self._vede(x)
        intrari = self.rel.asupra(a, self.data_ref)
        for e in intrari:
            x = self.corp.dupa_id.get(e["sursa"])
            if x is not None:
                self._vede(x)
                self.relatie.setdefault(e["sursa"], []).append((e["fel"], aid))
        iesiri = [e for e in self.rel.muchii if e["sursa"] == aid]
        return {"id": aid, "temei": intrebari.temei_uman(a),
                "valabil_din": a.get("valabil_din") or "nedovedit",
                "sursa": self.corp.sursa_act.get(a["act"], {}).get("sursa"),
                "text": txt[:MAX_TEXT] + (" [... trunchiat; citeaza numai din partea aratata]"
                                          if trunchiat else ""),
                "parinte": a.get("parinte"),
                "copii": [{"id": x["id"], "inceput": " ".join(x["text"].split())[:90]} for x in copii[:40]],
                "deroga_sau_modifica_acest_atom": [
                    {"id": e["sursa"], "fel": e["fel"], "fragment": e["fragment"][:200]} for e in intrari],
                "acest_atom_deroga_de_la": [
                    {"tinta": "%s#art%s%s" % (e["tinta_act"], e["tinta_art"],
                                              "/alin%s" % e["tinta_alin"] if e["tinta_alin"] else ""),
                     "fel": e["fel"]} for e in iesiri]}

    def executa(self, nume, inp):
        self.pasi.append({"unealta": nume, "intrare": inp})
        if nume == "cauta":
            return self.cauta(inp["interogare"])
        if nume == "cuprins":
            return self.cuprins(inp["act"], inp.get("filtru", ""))
        if nume == "deschide":
            return self.deschide(inp["id"])
        return {"eroare": "unealta necunoscuta"}


# ── calculul, evaluat de cod ─────────────────────────────────────────────────────────────────────
_MII = re.compile(r"\d\.\d{3}(?!\d)")


def _numar(v):
    """"100.000" -> 100000; "2,25%" -> 0.0225; "25.03.2026" -> date. Intoarce (valoare, e_procent)."""
    s = v.strip().replace(" ", "").replace("lei", "").replace("euro", "")
    if re.match(r"^\d{1,2}\.\d{1,2}\.\d{4}$", s):
        z, l, a = s.split(".")
        return datetime.date(int(a), int(l), int(z)), False
    proc = s.endswith("%")
    s = s.rstrip("%")
    s = s.replace(".", "").replace(",", ".") if "," in s or re.match(r"^\d{1,3}(\.\d{3})+$", s) else s
    try:
        d = Decimal(s)
    except InvalidOperation:
        raise ValueError("operand nenumeric: %r" % v)
    return (d / 100 if proc else d), proc


_OP = {ast.Add: "+", ast.Sub: "−", ast.Mult: "×", ast.Div: "÷"}


def _eval(nod, env, pasi=None, fmt=None):
    """Valoarea formulei. `pasi` aduna, pentru afisare, fiecare apel zile(a, b) cu rezultatul lui."""
    if isinstance(nod, ast.Expression):
        return _eval(nod.body, env, pasi, fmt)
    if isinstance(nod, ast.BinOp) and type(nod.op) in _OP:
        a, b = _eval(nod.left, env, pasi, fmt), _eval(nod.right, env, pasi, fmt)
        if isinstance(nod.op, ast.Add):
            return a + b
        if isinstance(nod.op, ast.Sub):
            return a - b
        if isinstance(nod.op, ast.Mult):
            return a * b
        return a / b
    if isinstance(nod, ast.UnaryOp) and isinstance(nod.op, ast.USub):
        return -_eval(nod.operand, env, pasi, fmt)
    if isinstance(nod, ast.Name):
        if nod.id not in env:
            raise ValueError("nume fara sursa in formula: %s" % nod.id)
        return env[nod.id]
    if isinstance(nod, ast.Constant) and nod.value in (1, 100) and not isinstance(nod.value, bool):
        return Decimal(nod.value)
    if isinstance(nod, ast.Constant):
        raise ValueError("constanta fara sursa in formula: %r (permise numai 1 si 100)" % nod.value)
    if isinstance(nod, ast.Call) and isinstance(nod.func, ast.Name) and not nod.keywords:
        args = [_eval(x, env, pasi, fmt) for x in nod.args]
        if nod.func.id == "min" and args:
            return min(args)
        if nod.func.id == "max" and args:
            return max(args)
        if nod.func.id == "zile" and len(args) == 2:
            v = Decimal((args[1] - args[0]).days)
            if pasi is not None:
                pasi.append("zile(%s, %s) = %s zile" % (_arata(args[0], fmt), _arata(args[1], fmt),
                                                         _arata(v, fmt)))
            return v
    raise ValueError("forma nepermisa in formula: %s" % ast.dump(nod)[:80])


def _format(d, mii=True):
    d = Decimal(d).quantize(Decimal("0.01"))
    intreg, _, zec = ("%.2f" % d).partition(".")
    semn = "-" if intreg.startswith("-") else ""
    intreg = intreg.lstrip("-")
    if mii:
        intreg = ".".join([intreg[max(0, i - 3):i] for i in range(len(intreg), 0, -3)][::-1])
    return semn + intreg + ("" if zec == "00" else "," + zec)


def _arata(v, fmt):
    if isinstance(v, datetime.date):
        return v.strftime("%d.%m.%Y")
    return _format(v, mii=(fmt or {}).get("mii", True))


def _cu_valori(nod, env, fmt, procente):
    """Formula cu valorile puse in locul numelor - ca un contabil s-o poata reface (C28)."""
    if isinstance(nod, ast.Expression):
        return _cu_valori(nod.body, env, fmt, procente)
    if isinstance(nod, ast.BinOp) and type(nod.op) in _OP:
        return "(%s %s %s)" % (_cu_valori(nod.left, env, fmt, procente), _OP[type(nod.op)],
                               _cu_valori(nod.right, env, fmt, procente))
    if isinstance(nod, ast.UnaryOp):
        return "−" + _cu_valori(nod.operand, env, fmt, procente)
    if isinstance(nod, ast.Name):
        if nod.id in procente:
            return procente[nod.id]
        return _arata(env[nod.id], fmt)
    if isinstance(nod, ast.Constant):
        return str(nod.value)
    if isinstance(nod, ast.Call):
        return "%s(%s)" % (nod.func.id, ", ".join(_cu_valori(x, env, fmt, procente) for x in nod.args))
    return "?"


def evalueaza_calcule(calcule, dupa_id, intrebare):
    """(valori, incalcari, detalii). Fara model: sursa fiecarui operand verificata literal.

    C25: eticheta operandului decide sursa ceruta. FAPT_CAZ - valoarea trebuie sa apara LITERAL in
    intrebare (altfel e o valoare fara sursa). VALOARE_LEGALA - atom aratat modelului, fragment verbatim
    in el, valoarea literal in fragment."""
    env, greseli, detalii, procente = {}, [], [], {}
    # C28: stilul numerelor urmeaza sursa - cu separator de mii daca operanzii il au ("10.000"),
    # fara daca nu ("2026" + 1 = 2027, nu "2.027")
    fmt = {"mii": any(_MII.search(o["valoare"]) for c in calcule for o in c["operanzi"])}
    q = semantic._n(intrebare)
    for c in calcule:
        for o in c["operanzi"]:
            val = o["valoare"].strip()
            if o["eticheta"] == "VALOARE_LEGALA":
                a = dupa_id.get(o["atom"])
                if not o["atom"]:
                    greseli.append("operandul %s=%s e VALOARE_LEGALA fara atom" % (o["nume"], val))
                elif a is None:
                    greseli.append("operandul %s: atomul %s nu i-a fost aratat" % (o["nume"], o["atom"]))
                elif semantic._n(o["fragment"]) not in semantic._n(a["text"]):
                    greseli.append("operandul %s: fragmentul nu e verbatim in %s" % (o["nume"], o["atom"]))
                if val not in o["fragment"]:
                    greseli.append("operandul %s=%r nu apare literal in fragmentul lui" % (o["nume"], val))
            else:
                if val not in q:
                    greseli.append("operandul %s=%r e FAPT_CAZ, dar nu apare literal in intrebare"
                                   % (o["nume"], val))
            try:
                env[o["nume"]], proc = _numar(val)
                if proc:
                    procente[o["nume"]] = val
            except ValueError as e:
                greseli.append(str(e))
        try:
            arb = ast.parse(c["formula"], mode="eval")
            zile = []
            v = _eval(arb, env, zile, fmt)
            env[c["nume"]] = v
            detalii.append({"nume": c["nume"], "formula": c["formula"],
                            "cu_valori": _cu_valori(arb, env, fmt, procente),
                            "zile": zile, "rezultat": _arata(v, fmt), "operanzi": c["operanzi"]})
        except (ValueError, SyntaxError, ZeroDivisionError, TypeError, InvalidOperation,
                AttributeError, KeyError) as e:
            greseli.append("calculul %s: %s" % (c["nume"], e))
    valori = {d["nume"]: d["rezultat"] for d in detalii}
    return valori, greseli, detalii


def pas_cu_pas(detalii):
    """Textul calculului: fiecare pas cu formula, valorile puse in ea si rezultatul (C28)."""
    rand = []
    for d in detalii:
        for z in d["zile"]:
            rand.append(z)
        rand.append("%s = %s = %s = %s" % (d["nume"], d["formula"], d["cu_valori"], d["rezultat"]))
    return rand


# ── C27: datele pe care le poarta intrebarea ─────────────────────────────────────────────────────
def date_din_intrebare(text):
    """[(data_iso, precizie, fragment)], fara datele mai grosiere cuprinse intr-una mai fina.

    Reguli ca in `intrebari.data_referinta` (D12: luna -> ultima zi, an -> 31.12 dar nu dupa ziua
    intrebarii), aplicate TUTUROR datelor, nu numai primei."""
    t = potrivire.norm(text)
    ies, ocupat = [], []

    def liber(m):
        return not any(a < m.end() and m.start() < b for a, b in ocupat)

    for m in re.finditer(r"\b(\d{1,2})\.(\d{1,2})\.(20\d\d)\b", t):
        ies.append(("%s-%02d-%02d" % (m.group(3), int(m.group(2)), int(m.group(1))), "zi", m.group(0)))
        ocupat.append(m.span())
    luni = "|".join(intrebari._LUNI)
    for m in re.finditer(r"\b(\d{1,2})\s+(%s)\s+(20\d\d)\b" % luni, t):
        if liber(m):
            ies.append(("%s-%02d-%02d" % (m.group(3), intrebari._LUNI[m.group(2)], int(m.group(1))),
                        "zi", m.group(0)))
            ocupat.append(m.span())
    for m in re.finditer(r"\b(%s)\s+(20\d\d)\b" % luni, t):
        if liber(m):
            an, luna = int(m.group(2)), intrebari._LUNI[m.group(1)]
            ultima = datetime.date(an + (luna == 12), luna % 12 + 1, 1) - datetime.timedelta(days=1)
            ies.append((ultima.isoformat(), "luna", m.group(0)))
            ocupat.append(m.span())
    for m in re.finditer(r"\b(20\d\d)\b", t):
        if liber(m):
            ies.append((min("%s-12-31" % m.group(1), intrebari.DATA_INTREBARII), "an", m.group(0)))
    fine = [(d, p) for d, p, _f in ies if p != "an"]
    ies = [x for x in ies if not (
        (x[1] == "an" and any(d[:4] == x[2] for d, _p in fine)) or
        (x[1] == "luna" and any(p == "zi" and d[:7] == x[0][:7] for d, p in fine)))]
    unice, vazut = [], set()
    for x in ies:
        if x[0] not in vazut:
            vazut.add(x[0])
            unice.append(x)
    return unice


# ── C23: validarea structurala a raspunsului final ──────────────────────────────────────────────
_MARCAJ = re.compile(r"</?\s*(parameter|declaratie|raspuns|citate|lipsa|motiv|calcule|derogari_tratate|"
                     r"data_referinta)\b|<parameter\b", re.I)


def valideaza_structura(inp):
    """Lista de probleme; goala = structura e buna. Fara model."""
    probleme = []

    def texte(x, cale):
        if isinstance(x, str):
            yield cale, x
        elif isinstance(x, dict):
            for k, v in x.items():
                for y in texte(v, cale + "." + k):
                    yield y
        elif isinstance(x, list):
            for i, v in enumerate(x):
                for y in texte(v, "%s[%d]" % (cale, i)):
                    yield y

    for cale, t in texte(inp, "raspunde"):
        if _MARCAJ.search(t):
            probleme.append("marcaj de parametri scurs in %s" % cale)
    r = (inp.get("raspuns") or "").strip()
    if inp.get("stare") == "RASPUNS":
        if len(re.sub(r"\W", "", r)) < 2:
            probleme.append("campul raspuns e gol sau un substituent (%r)" % r[:10])
        for k in ("declaratie", "motiv", "data_referinta_motiv"):
            alt = (inp.get(k) or "").strip()
            if r and alt and len(r) >= 20 and (r == alt or r in alt):
                probleme.append("campul raspuns repeta continutul campului %s" % k)
    return probleme


# ── bucla ────────────────────────────────────────────────────────────────────────────────────────
def sistem(idx):
    acte = sorted(b for b, v in idx.normativ.items() if v)
    return SISTEM + "\n\nACTELE NORMATIVE din corpus (id-urile folosite de `cuprins`):\n" + ", ".join(acte)


def _apel(client, sis, messages):
    return client.beta.messages.create(
        model=MODEL, max_tokens=16000, betas=["server-side-fallback-2026-07-01"],
        fallbacks="default", thinking={"type": "adaptive"},
        system=[{"type": "text", "text": sis, "cache_control": {"type": "ephemeral"}}],
        tools=UNELTE, messages=messages, cache_control={"type": "ephemeral"})


def raspunde(q, idx, rel, client, sis=None):
    date = date_din_intrebare(q["intrebare"])
    admise = [d for d, _p, _f in date] or [intrebari.DATA_INTREBARII]
    # unealtele arata atomii in vigoare la cea mai recenta data a intrebarii (C27); citatele se
    # verifica apoi la data ALEASA pentru faptul intrebat
    vizibil = max(admise)
    nav = Navigator(idx, rel, vizibil)
    baza = {"id": q["id"], "tip": q["tip"], "intrebare": q["intrebare"], "date_din_intrebare": date,
            "strat": "navigare v5"}
    descriere = "; ".join("%s (%s, din „%s”)" % (d, p, f) for d, p, f in date) or \
        "%s (întrebarea nu poartă nicio dată: ziua întrebării)" % intrebari.DATA_INTREBARII
    messages = [{"role": "user", "content": "<intrebare>%s</intrebare>\n<date_din_intrebare>%s"
                                            "</date_din_intrebare>" % (q["intrebare"], descriere)}]
    apeluri, final, t0, reincercari, oprit = [], None, time.time(), 0, None
    probleme_c23 = []
    while True:
        r = _apel(client, sis or sistem(idx), messages)
        u = r.usage
        iteratii = getattr(u, "iterations", None) or []
        apeluri.append({"model": r.model, "stop_reason": r.stop_reason,
                        "tokeni": {"intrare": u.input_tokens, "iesire": u.output_tokens,
                                   "cache_scriere": getattr(u, "cache_creation_input_tokens", 0) or 0,
                                   "cache_citire": getattr(u, "cache_read_input_tokens", 0) or 0},
                        "cost_usd": semantic._cost(u, r.model),
                        "fallback": bool(r.model != MODEL or any(
                            getattr(x, "type", "") == "fallback_message" for x in iteratii))})
        if r.stop_reason == "refusal" or len(apeluri) > MAX_PASI + 6:
            oprit = "stop_reason=%s" % r.stop_reason
            break
        messages.append({"role": "assistant", "content": r.content})
        uses = [b for b in r.content if b.type == "tool_use"]
        fin = [b for b in uses if b.name == "raspunde"]
        if fin:
            probleme = valideaza_structura(fin[0].input)
            if not probleme:
                final = fin[0].input
                break
            probleme_c23.append(probleme)
            if reincercari >= 1:                       # C23: o singura reincercare
                oprit = "C23"
                break
            reincercari += 1
            rezultate = [{"type": "tool_result", "tool_use_id": b.id, "is_error": True,
                          "content": ("Structura răspunsului e invalidă: %s. Apelează din nou `raspunde`, "
                                      "cu fiecare câmp conținând numai textul lui." % "; ".join(probleme))
                          if b is fin[0] else "ignorat"} for b in uses]
            messages.append({"role": "user", "content": rezultate})
            continue
        if not uses:
            messages.append({"role": "user", "content": "Încheie apelând unealta `raspunde`."})
            continue
        if len(nav.pasi) + len(uses) > MAX_PASI:        # C29: peste limita = abtinere cu traseu
            oprit = "C29"
            break
        rezultate = []
        for b in uses:
            out = nav.executa(b.name, b.input)
            out["pasi_ramasi"] = MAX_PASI - len(nav.pasi)
            rezultate.append({"type": "tool_result", "tool_use_id": b.id,
                              "content": json.dumps(out, ensure_ascii=False)})
        messages.append({"role": "user", "content": rezultate})
    apel = {"model": apeluri[-1]["model"] if apeluri else MODEL, "tururi": len(apeluri),
            "pasi_navigare": len(nav.pasi), "pasi": nav.pasi, "reincercari_C23": reincercari,
            "probleme_C23": probleme_c23,
            "tokeni": {k: sum(a["tokeni"][k] for a in apeluri) for k in
                       ("intrare", "iesire", "cache_scriere", "cache_citire")},
            "cost_usd": round(sum(a["cost_usd"] for a in apeluri), 5),
            "fallback": any(a["fallback"] for a in apeluri), "secunde": round(time.time() - t0, 2)}
    traseu = " → ".join("%s(%s)" % (p["unealta"], ", ".join(str(v) for v in p["intrare"].values()))
                        for p in nav.pasi)
    if final is None:
        if oprit == "C29":
            motiv = ("C29: limita de %d pași de navigare a fost atinsă fără răspuns. Traseul: %s"
                     % (MAX_PASI, traseu))
        elif oprit == "C23":
            motiv = ("C23: structura răspunsului final a fost invalidă de două ori (%s)"
                     % " / ".join("; ".join(p) for p in probleme_c23))
        else:
            motiv = "modelul nu a apelat `raspunde` (%s)" % oprit
        return dict(baza, data_referinta=None, stare="NU_POT_RASPUNDE", tip_abtinere=oprit,
                    raspuns=None, argument=[], apel=apel, traseu=traseu, motiv=motiv)
    # C27: data aleasa trebuie sa fie una dintre datele intrebarii
    data_ref = (final.get("data_referinta") or "").strip()
    baza["data_referinta"] = data_ref
    baza["data_referinta_motiv"] = final.get("data_referinta_motiv")
    greseli_data = []
    if final["stare"] == "RASPUNS" and data_ref not in admise:
        greseli_data.append("C27: data de referinta %r nu e una dintre datele intrebarii %s"
                            % (data_ref, admise))
    atomi = list(nav.vazuti.values())
    rez = semantic.finalizeaza(baza, final, atomi, q, data_ref if data_ref in admise else vizibil,
                               nav.relatie, apel)
    rez["propunerea_modelului"] = final
    rez["traseu"] = traseu
    if greseli_data:
        return dict(rez, stare="NU_POT_RASPUNDE", raspuns=None,
                    verificare={"trece": False, "incalcari": rez["verificare"]["incalcari"] + greseli_data},
                    motiv="VERIFICAREA DATEI a respins propunerea: " + "; ".join(greseli_data))
    # calculul, evaluat de cod
    if final.get("calcule") and final["stare"] == "RASPUNS":
        valori, greseli, detalii = evalueaza_calcule(final["calcule"], nav.vazuti, q["intrebare"])
        rez["calcule"] = detalii
        if greseli:
            return dict(rez, stare="NU_POT_RASPUNDE", raspuns=None,
                        verificare={"trece": False, "incalcari": rez["verificare"]["incalcari"] + greseli},
                        motiv="VERIFICAREA CALCULULUI a respins propunerea: " + "; ".join(greseli))
        if rez["stare"] == "RASPUNS":
            txt = rez["raspuns"]
            for k, v in valori.items():
                txt = txt.replace("{%s}" % k, v)
            rez["raspuns"] = txt + "  [calcul: " + "; ".join(pas_cu_pas(detalii)) + "]"
    if rez["stare"] == "RASPUNS":
        d = datetime.date.fromisoformat(data_ref).strftime("%d.%m.%Y")
        rez["raspuns"] += "  [data de referință: %s — %s]" % (d, final.get("data_referinta_motiv") or "")
    return rez


def ruleaza(dest, intrebari_id=None):
    import anthropic
    t0 = time.time()
    idx = intrebari.Index()
    rel = idx.rel
    sis = sistem(idx)
    client = anthropic.Anthropic(api_key=semantic.cheie())
    qs = [q for q in intrebari.incarca_intrebari() if not intrebari_id or q["id"] in intrebari_id]
    # fiecare raspuns se scrie IMEDIAT (o rulare intrerupta - retea, credit - nu pierde ce a platit);
    # la repornire, intrebarile deja raspunse se iau din fisierul partial, fara apel nou
    partial = dest + ".partial.jsonl"
    facute = {}
    if os.path.exists(partial):
        for l in open(partial, encoding="utf-8"):
            r = json.loads(l)
            facute[r["id"]] = r
    ies = []
    for q in qs:
        if q["id"] in facute:
            ies.append(facute[q["id"]])
            continue
        r = raspunde(q, idx, rel, client, sis)
        with open(partial, "a", encoding="utf-8") as f:
            f.write(json.dumps(r, ensure_ascii=False, default=str) + "\n")
        ies.append(r)
        print("%-9s %-16s pasi=%-2d $%.4f %s" % (q["id"], r["stare"], r["apel"]["pasi_navigare"],
                                                   r["apel"]["cost_usd"], (r.get("raspuns") or r["motiv"])[:70]),
              flush=True)
    for r in ies:
        if r["stare"] == "RASPUNS":
            assert r["argument"] and r["verificare"]["trece"], r["id"]
    tok = {k: sum(r["apel"]["tokeni"][k] for r in ies) for k in ("intrare", "iesire", "cache_scriere",
                                                                   "cache_citire")}
    rez = {"_ce": "Stratul semantic v5: navigare structurala + calcul evaluat de cod (C23, C25, C27-C29).",
           "model": MODEL, "la_limita_de_pasi_C29": [r["id"] for r in ies if r.get("tip_abtinere") == "C29"],
           "abtineri_C23": [r["id"] for r in ies if r.get("tip_abtinere") == "C23"],
           "reincercari_C23": [r["id"] for r in ies if r["apel"].get("reincercari_C23")],
           "max_pasi": MAX_PASI, "n": len(ies), "raspunse": sum(1 for r in ies if r["stare"] == "RASPUNS"),
           "respinse_de_verificare": sum(1 for r in ies if r.get("verificare") and not r["verificare"]["trece"]),
           "incomplete_detectate": sum(1 for r in ies if r.get("tip_abtinere") == "INCOMPLET"),
           "de_la_modelul_de_rezerva": [r["id"] for r in ies if r["apel"].get("fallback")],
           "pasi_medii": round(sum(r["apel"]["pasi_navigare"] for r in ies) / float(len(ies)), 2),
           "tokeni": tok, "cost_usd": round(sum(r["apel"]["cost_usd"] for r in ies), 4),
           "secunde_total": round(sum(r["apel"]["secunde"] for r in ies), 2),
           "reluat_din_partial": sorted(facute), "raspunsuri": ies}
    json.dump(rez, open(dest, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
    return rez


if __name__ == "__main__":
    import sys
    ids = [a for a in sys.argv[1:] if a.startswith("Q-")]
    dest = os.path.join(_RAD, "artefacte", "intrebari",
                        "raspunsuri_navigare_v5%s.json" % ("_proba" if ids else ""))
    r = ruleaza(dest, ids or None)
    print("navigare: %d/%d raspunse | respinse %d | incomplete %d | pasi medii %.1f | %s | $%.4f | %.0f s"
          % (r["raspunse"], r["n"], r["respinse_de_verificare"], r["incomplete_detectate"],
             r["pasi_medii"], r["tokeni"], r["cost_usd"], r["secunde_total"]))
