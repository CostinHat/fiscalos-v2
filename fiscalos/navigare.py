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
MAX_PASI = 12
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
- `cuprins(act, filtru)` — structura unui act: titlurile/capitolele și articolele lor, cu denumirea \\
marginală; cu `filtru`, numai articolele ale căror denumiri sau titluri conțin cuvintele date.
- `deschide(id)` — textul unui atom, părintele, copiii (alineate, litere, puncte) și RELAȚIILE lui: \\
atomii care derogă de la el, fac excepție de la el sau îl modifică, și cei de la care derogă el.
- `raspunde(...)` — răspunsul final, o singură dată.
Ai cel mult %d pași de navigare. Navighează ca un contabil: găsește actul și articolul potrivit prin \\
structură, deschide-l, urmează relațiile lui de derogare, apoi răspunde. Toate unealtele întorc numai \\
atomi în vigoare la data de referință. Poți cita numai atomi pe care o unealtă ți i-a arătat.

CALCUL. Nu calculezi. Dacă răspunsul cere un calcul, îl descrii în `calcule`: fiecare calcul are un \\
`nume`, o `formula` (numai numele operanzilor și ale calculelor anterioare, + - * / paranteze, \\
min(), max(), zile(data1, data2) = numărul de zile de la data1 la data2) și lista de `operanzi`. \\
Fiecare operand are `valoare` scrisă exact ca în sursă (ex. "21%%", "100.000", "25.03.2026") și sursa: \\
`atom` + `fragment` literal din acel atom, SAU `intrebare` + `fragment` literal din întrebare. O valoare \\
legală (cotă, plafon, termen) vine numai dintr-un atom. Singurele constante permise fără sursă sunt 1 și \\
100. În `raspuns` pui rezultatul unui calcul ca {nume}; codul îl evaluează și îl înlocuiește.""" % MAX_PASI

_CALC = {"type": "array", "items": {"type": "object", "properties": {
    "nume": {"type": "string"}, "formula": {"type": "string"},
    "operanzi": {"type": "array", "items": {"type": "object", "properties": {
        "nume": {"type": "string"}, "valoare": {"type": "string"},
        "sursa": {"type": "string", "enum": ["atom", "intrebare"]},
        "atom": {"type": "string"}, "fragment": {"type": "string"}},
        "required": ["nume", "valoare", "sursa", "atom", "fragment"], "additionalProperties": False}}},
    "required": ["nume", "formula", "operanzi"], "additionalProperties": False}}
SCHEMA = json.loads(json.dumps(semantic.SCHEMA))
SCHEMA["properties"]["calcule"] = _CALC
SCHEMA["required"] = SCHEMA["required"] + ["calcule"]

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
        if not filtru.strip():
            # in ordinea actului: fiecare portiune continua sub acelasi titlu/capitol
            grupe = []
            for a in ats:
                t = a.get("titlu_structural") or "(fara titlu)"
                if not grupe or grupe[-1][0] != t:
                    grupe.append((t, []))
                grupe[-1][1].append(a["cheie"])
            return {"act": act, "sursa": self.corp.sursa_act.get(act, {}).get("sursa"),
                    "nota": "pentru denumirile articolelor, cere `cuprins` cu un filtru",
                    "titluri": [{"titlu": t, "articole": "%s..%s (%d)" % (v[0], v[-1], len(v))}
                                for t, v in grupe[:120]]}
        st = set(intrebari._stemuri(intrebari._extinde(filtru)))
        ies = []
        for a in ats:
            den = " ".join(a["text"].split())[:160] if len(a["text"]) <= 250 else ""
            ctx = potrivire.norm(den + " " + (a.get("titlu_structural") or ""))
            n = sum(1 for x in st if x in ctx)
            if n:
                ies.append((n, a, den))
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


def _eval(nod, env):
    if isinstance(nod, ast.Expression):
        return _eval(nod.body, env)
    if isinstance(nod, ast.BinOp) and isinstance(nod.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
        a, b = _eval(nod.left, env), _eval(nod.right, env)
        if isinstance(nod.op, ast.Add):
            return a + b
        if isinstance(nod.op, ast.Sub):
            return a - b
        if isinstance(nod.op, ast.Mult):
            return a * b
        return a / b
    if isinstance(nod, ast.UnaryOp) and isinstance(nod.op, ast.USub):
        return -_eval(nod.operand, env)
    if isinstance(nod, ast.Name):
        if nod.id not in env:
            raise ValueError("nume fara sursa in formula: %s" % nod.id)
        return env[nod.id]
    if isinstance(nod, ast.Constant) and nod.value in (1, 100):
        return Decimal(nod.value)
    if isinstance(nod, ast.Constant):
        raise ValueError("constanta fara sursa in formula: %r (permise numai 1 si 100)" % nod.value)
    if isinstance(nod, ast.Call) and isinstance(nod.func, ast.Name):
        args = [_eval(x, env) for x in nod.args]
        if nod.func.id == "min":
            return min(args)
        if nod.func.id == "max":
            return max(args)
        if nod.func.id == "zile" and len(args) == 2:
            return Decimal((args[1] - args[0]).days)
    raise ValueError("forma nepermisa in formula: %s" % ast.dump(nod)[:80])


def _format(d):
    d = Decimal(d).quantize(Decimal("0.01"))
    intreg, _, zec = ("%.2f" % d).partition(".")
    semn = "-" if intreg.startswith("-") else ""
    intreg = intreg.lstrip("-")
    grup = ".".join([intreg[max(0, i - 3):i] for i in range(len(intreg), 0, -3)][::-1])
    return semn + grup + ("" if zec == "00" else "," + zec)


def evalueaza_calcule(calcule, dupa_id, intrebare):
    """(valori, incalcari, detalii). Fara model: sursa fiecarui operand verificata literal."""
    env, greseli, detalii = {}, [], []
    for c in calcule:
        for o in c["operanzi"]:
            frag = semantic._n(o["fragment"])
            if o["valoare"].strip() not in o["fragment"]:
                greseli.append("operandul %s=%r nu apare literal in fragmentul lui sursa"
                               % (o["nume"], o["valoare"]))
            if o["sursa"] == "atom":
                a = dupa_id.get(o["atom"])
                if a is None:
                    greseli.append("operandul %s: atomul %s nu i-a fost aratat" % (o["nume"], o["atom"]))
                elif frag not in semantic._n(a["text"]):
                    greseli.append("operandul %s: fragmentul nu e verbatim in %s" % (o["nume"], o["atom"]))
            else:
                if frag not in semantic._n(intrebare):
                    greseli.append("operandul %s: fragmentul nu e in intrebare" % o["nume"])
                # C13: o valoare legala (procent, termen, plafon) nu se ia din intrebare
                m = re.search(re.escape(o["valoare"].strip().rstrip("%")), frag)
                if o["valoare"].strip().endswith("%") or (m and semantic.e_valoare_legala(frag, m)):
                    greseli.append("operandul %s=%s e o valoare legala luata din intrebare "
                                   "(C13: numai din atom)" % (o["nume"], o["valoare"]))
            try:
                env[o["nume"]], _p = _numar(o["valoare"])
            except ValueError as e:
                greseli.append(str(e))
        try:
            v = _eval(ast.parse(c["formula"], mode="eval"), env)
            env[c["nume"]] = v
            detalii.append({"nume": c["nume"], "formula": c["formula"], "rezultat": _format(v),
                            "operanzi": c["operanzi"]})
        except (ValueError, SyntaxError, ZeroDivisionError, TypeError, InvalidOperation) as e:
            greseli.append("calculul %s: %s" % (c["nume"], e))
    return {k: _format(v) for k, v in env.items() if any(k == c["nume"] for c in calcule)}, \
        greseli, detalii


# ── bucla ────────────────────────────────────────────────────────────────────────────────────────
def sistem(idx):
    acte = sorted(b for b, v in idx.normativ.items() if v)
    return SISTEM + "\n\nACTELE NORMATIVE din corpus (id-urile folosite de `cuprins`):\n" + ", ".join(acte)


def raspunde(q, idx, rel, client, sis=None):
    data_ref, precizie, _f = intrebari.data_referinta(q["intrebare"])
    if not data_ref:
        data_ref, precizie = intrebari.DATA_INTREBARII, "implicita (ziua intrebarii)"
    nav = Navigator(idx, rel, data_ref)
    baza = {"id": q["id"], "tip": q["tip"], "intrebare": q["intrebare"], "data_referinta": data_ref,
            "precizie_data": precizie, "strat": "navigare"}
    messages = [{"role": "user", "content": "<intrebare>%s</intrebare>\n<data_referinta>%s (%s)"
                                            "</data_referinta>" % (q["intrebare"], data_ref, precizie)}]
    apeluri, final, t0 = [], None, time.time()
    for tura in range(MAX_PASI + 3):
        r = client.beta.messages.create(
            model=MODEL, max_tokens=16000, betas=["server-side-fallback-2026-07-01"],
            fallbacks="default", thinking={"type": "adaptive"},
            system=[{"type": "text", "text": sis or sistem(idx), "cache_control": {"type": "ephemeral"}}],
            tools=UNELTE, messages=messages, cache_control={"type": "ephemeral"})
        u = r.usage
        iteratii = getattr(u, "iterations", None) or []
        apeluri.append({"model": r.model, "stop_reason": r.stop_reason,
                        "tokeni": {"intrare": u.input_tokens, "iesire": u.output_tokens,
                                   "cache_scriere": getattr(u, "cache_creation_input_tokens", 0) or 0,
                                   "cache_citire": getattr(u, "cache_read_input_tokens", 0) or 0},
                        "cost_usd": semantic._cost(u, r.model),
                        "fallback": bool(r.model != MODEL or any(
                            getattr(x, "type", "") == "fallback_message" for x in iteratii))})
        if r.stop_reason == "refusal":
            break
        messages.append({"role": "assistant", "content": r.content})
        uses = [b for b in r.content if b.type == "tool_use"]
        fin = [b for b in uses if b.name == "raspunde"]
        if fin:
            final = fin[0].input
            break
        if not uses:
            messages.append({"role": "user", "content": "Încheie apelând unealta `raspunde`."})
            continue
        rezultate = []
        depasit = len(nav.pasi) + len(uses) > MAX_PASI
        for b in uses:
            if depasit:
                out = {"eroare": "limita de %d pasi atinsa; apeleaza acum `raspunde`" % MAX_PASI}
            else:
                out = nav.executa(b.name, b.input)
            rezultate.append({"type": "tool_result", "tool_use_id": b.id,
                              "content": json.dumps(out, ensure_ascii=False)})
        if depasit or len(nav.pasi) >= MAX_PASI:
            rezultate.append({"type": "text", "text": "Ai atins limita de pași. Apelează acum `raspunde`."})
        messages.append({"role": "user", "content": rezultate})
    apel = {"model": apeluri[-1]["model"] if apeluri else MODEL, "tururi": len(apeluri),
            "pasi_navigare": len(nav.pasi), "pasi": nav.pasi,
            "tokeni": {k: sum(a["tokeni"][k] for a in apeluri) for k in
                       ("intrare", "iesire", "cache_scriere", "cache_citire")},
            "cost_usd": round(sum(a["cost_usd"] for a in apeluri), 5),
            "fallback": any(a["fallback"] for a in apeluri), "secunde": round(time.time() - t0, 2)}
    if final is None:
        return dict(baza, stare="NU_POT_RASPUNDE", raspuns=None, argument=[], apel=apel,
                    motiv="modelul nu a apelat `raspunde` (stop_reason=%s)" %
                          (apeluri[-1]["stop_reason"] if apeluri else "-"))
    atomi = list(nav.vazuti.values())
    rez = semantic.finalizeaza(baza, final, atomi, q, data_ref, nav.relatie, apel)
    rez["propunerea_modelului"] = final
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
            rez["raspuns"] = txt + "  [calcul: " + "; ".join(
                "%s = %s = %s" % (d["nume"], d["formula"], d["rezultat"]) for d in detalii) + "]"
    return rez


def ruleaza(dest, intrebari_id=None):
    import anthropic
    t0 = time.time()
    idx = intrebari.Index()
    rel = idx.rel
    sis = sistem(idx)
    client = anthropic.Anthropic(api_key=semantic.cheie())
    qs = [q for q in intrebari.incarca_intrebari() if not intrebari_id or q["id"] in intrebari_id]
    ies = []
    for q in qs:
        r = raspunde(q, idx, rel, client, sis)
        ies.append(r)
        print("%-9s %-16s pasi=%-2d $%.4f %s" % (q["id"], r["stare"], r["apel"]["pasi_navigare"],
                                                   r["apel"]["cost_usd"], (r.get("raspuns") or r["motiv"])[:70]),
              flush=True)
    for r in ies:
        if r["stare"] == "RASPUNS":
            assert r["argument"] and r["verificare"]["trece"], r["id"]
    tok = {k: sum(r["apel"]["tokeni"][k] for r in ies) for k in ("intrare", "iesire", "cache_scriere",
                                                                   "cache_citire")}
    rez = {"_ce": "Stratul semantic v4: navigare structurala + calcul evaluat de cod.", "model": MODEL,
           "max_pasi": MAX_PASI, "n": len(ies), "raspunse": sum(1 for r in ies if r["stare"] == "RASPUNS"),
           "respinse_de_verificare": sum(1 for r in ies if r.get("verificare") and not r["verificare"]["trece"]),
           "incomplete_detectate": sum(1 for r in ies if r.get("tip_abtinere") == "INCOMPLET"),
           "de_la_modelul_de_rezerva": [r["id"] for r in ies if r["apel"].get("fallback")],
           "pasi_medii": round(sum(r["apel"]["pasi_navigare"] for r in ies) / float(len(ies)), 2),
           "tokeni": tok, "cost_usd": round(sum(r["apel"]["cost_usd"] for r in ies), 4),
           "secunde_total": round(time.time() - t0, 2), "raspunsuri": ies}
    json.dump(rez, open(dest, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
    return rez


if __name__ == "__main__":
    import sys
    ids = [a for a in sys.argv[1:] if a.startswith("Q-")]
    dest = os.path.join(_RAD, "artefacte", "intrebari",
                        "raspunsuri_navigare%s.json" % ("_proba" if ids else ""))
    r = ruleaza(dest, ids or None)
    print("navigare: %d/%d raspunse | respinse %d | incomplete %d | pasi medii %.1f | %s | $%.4f | %.0f s"
          % (r["raspunse"], r["n"], r["respinse_de_verificare"], r["incomplete_detectate"],
             r["pasi_medii"], r["tokeni"], r["cost_usd"], r["secunde_total"]))
