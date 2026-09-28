# -*- coding: utf-8 -*-
"""C3 (a) — STRATUL SEMANTIC ANCORAT PE ATOMI: modelul propune, verificatorul mecanic decide.

DECIZIA ARHITECTULUI: "un model (API Anthropic) propune raspunsul; orice cifra si orice citat trebuie
sa existe verbatim intr-un atom, verificat mecanic; ce nu trece verificarea devine abţinere."

ÎMPARTIREA MUNCII, si de ce ASA. Motorul lexical gasea des ARTICOLUL corect si fraza greşita (11 din
17 greşeli). Modelul poate citi un articol si alege fraza - dar poate si inventa. Deci:
  - CAUTAREA ramane mecanica (`intrebari.Index`, cu toate regulile de clasa D3..D14): modelul vede
    NUMAI atomii pe care i-a gasit cautarea, valabili la data intrebarii, din acte normative;
  - RASPUNSUL il propune modelul, intr-o forma structurata (schema JSON);
  - VERDICTUL il da `verifica()`, fara model: fiecare citat e cautat caracter cu caracter in textul
    COMPLET al atomului, fiecare cifra din raspuns trebuie sa apara literal intr-un citat sau in
    intrebare. Un raspuns care pica verificarea devine abţinere, cu motivul pastrat pentru audit.
Modelul nu poate face un raspuns sa treaca: el propune, codul decide.

ORB LA CHEIE, ca motorul lexical: modelul primeste intrebarea, data si atomii - nimic din coloanele
cheii. `test_intrebari.py` verifica si acest modul prin AST.

COST, masurat pe fiecare apel din `response.usage`, la preturile de mai jos (USD / milion de tokeni).
"""
import json
import os
import re
import time

from fiscalos import intrebari, potrivire

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = "claude-opus-5"
# USD per milion de tokeni. Scriere in cache (TTL 5 min) = 1,25 x intrare; citire = 0,1 x intrare.
PRET = {"claude-opus-5": {"in": 5.00, "out": 25.00, "cache_scriere": 6.25, "cache_citire": 0.50},
        "claude-opus-4-8": {"in": 5.00, "out": 25.00, "cache_scriere": 6.25, "cache_citire": 0.50}}
MAX_ATOMI = 16
MAX_CARACTERE_ATOM = 2500

SISTEM = """Ești stratul semantic al motorului FiscalOS. Primești o întrebare de fiscalitate românească, \
data de referință la care trebuie să fie valabil răspunsul și un set de ATOMI: fragmente de acte \
normative, fiecare cu un id. Atomii au fost aleși de o căutare mecanică și sunt, toți, în vigoare la \
data de referință.

Răspunsul tău NU e crezut pe cuvânt: un verificator mecanic îl va respinge (și va transforma \
răspunsul în abținere) dacă încalcă oricare dintre regulile de mai jos. Respectă-le întocmai.

1. Răspunzi NUMAI din atomii primiți. Nu folosești cunoștințe proprii despre legislație și nicio \
valoare pe care o știi din memorie, chiar dacă ești sigur de ea.

2. Fiecare citat este un fragment copiat EXACT, caracter cu caracter, din textul unui atom primit - \
cu aceleași diacritice, spații și punctuație -, între 40 și 400 de caractere. Nu parafrazezi, nu \
scurtezi din interior, nu unești bucăți. Primul citat din listă este cel decisiv: fragmentul care \
stabilește răspunsul.

3. Orice VALOARE LEGALĂ din `raspuns` (cotă, procent, plafon, prag, limită, termen legal, număr de \
zile/luni/ani) trebuie să apară literal, cu aceeași scriere, într-unul dintre citatele tale - chiar \
dacă apare și în întrebare. Cifrele din întrebare sunt permise numai ca FAPTE ALE CAZULUI (date, sume \
ale cazului). NU calculezi: dacă \
răspunsul cere un rezultat obținut prin calcul (o înmulțire, o sumă, o diferență) care nu apare \
literal într-un atom, răspunzi cu stare NU_POT și explici în `motiv` că e nevoie de un calcul. Nu \
pune în `raspuns` trimiteri la articole (temeiul se dă prin citate).

4. `declaratie` începe cu data de referință și perimetrul presupus: ce fel de contribuabil și ce regim \
presupui, din ce spune întrebarea, și ce presupui acolo unde întrebarea tace. Explicit, într-o frază.

5. Întrebări Da/Nu (fără cuvânt interogativ): răspunzi „Da" sau „Nu" numai dacă citatul decisiv \
conține literal regula care decide cazul descris; altfel stare NU_POT.

6. Dacă întrebarea NU dă faptele de care depinde răspunsul - după textul unui atom primit (de exemplu \
atomul spune că regula depinde de o condiție pe care întrebarea nu o precizează) - stare INCOMPLET: \
enumeri în `lipsa` faptele care lipsesc și citezi atomul care arată dependența.

7. Dacă atomii primiți nu conțin răspunsul, stare NU_POT, cu motivul. O abținere corectă e mai \
valoroasă decât un răspuns ghicit.

8. `raspuns` e scurt, în română: faptul cerut, fără ocolișuri. Pentru NU_POT și INCOMPLET, `raspuns` \
e un șir gol.

9. Unii atomi poartă atributul `deroga_de_la` sau `modifica`: sunt reguli speciale care derogă de la \
alt atom din context, îl modifică sau fac excepție de la el. Dacă citezi un atom de la care un alt \
atom din context derogă, TREBUIE să tratezi derogarea: fie o citezi (dacă se aplică cazului), fie o \
treci în `derogari_tratate` cu explicația de ce nu se aplică cazului din întrebare. Un răspuns care \
ignoră o derogare prezentă în context e respins."""

SCHEMA = {
    "type": "object",
    "properties": {
        "stare": {"type": "string", "enum": ["RASPUNS", "NU_POT", "INCOMPLET"]},
        "declaratie": {"type": "string"},
        "raspuns": {"type": "string"},
        "citate": {"type": "array", "items": {
            "type": "object",
            "properties": {"atom": {"type": "string"}, "fragment": {"type": "string"}},
            "required": ["atom", "fragment"], "additionalProperties": False}},
        "lipsa": {"type": "array", "items": {"type": "string"}},
        "derogari_tratate": {"type": "array", "items": {
            "type": "object",
            "properties": {"atom": {"type": "string"}, "cum": {"type": "string"}},
            "required": ["atom", "cum"], "additionalProperties": False}},
        "motiv": {"type": "string"},
    },
    "required": ["stare", "declaratie", "raspuns", "citate", "lipsa", "derogari_tratate", "motiv"],
    "additionalProperties": False,
}


# ── contextul: numai ce a gasit cautarea mecanica ────────────────────────────────────────────────
MAX_DEROGARI = 8


def context(q, idx, rel=None):
    data_ref, precizie, frag = intrebari.data_referinta(q["intrebare"])
    if not data_ref:
        data_ref, precizie, frag = intrebari.DATA_INTREBARII, "implicita (ziua intrebarii)", None
    hit = idx.cauta(q["intrebare"], data_ref, k=10)
    atomi, vazut = [], set()
    for _s, a in hit:
        for x in [a] + idx.copii(a, data_ref)[:6]:
            if x["id"] not in vazut and len(atomi) < MAX_ATOMI:
                vazut.add(x["id"])
                atomi.append(x)
    # C17 (a): atomii care DEROGA DE LA / fac EXCEPTIE DE LA / MODIFICA un atom gasit, valabili la data
    # intrebarii, intra in context, marcati. `relatie[id]` = [(fel, id_tinta)].
    relatie = {}
    if rel is not None:
        adaugate = 0
        for a in list(atomi):
            for e in rel.asupra(a, data_ref):
                relatie.setdefault(e["sursa"], []).append((e["fel"], a["id"]))
                if e["sursa"] not in vazut and adaugate < MAX_DEROGARI:
                    x = idx.corp.dupa_id.get(e["sursa"])
                    if x is not None:
                        vazut.add(x["id"])
                        atomi.append(x)
                        adaugate += 1
    stem = set(intrebari._stemuri(intrebari._extinde(q["intrebare"])))
    blocuri = []
    for a in atomi:
        txt = a["text"]
        trunchiat = len(txt) > MAX_CARACTERE_ATOM
        if trunchiat:
            # fereastra in jurul locului cu cele mai multe cuvinte ale intrebarii; se DECLARA
            n = potrivire.norm(txt)
            poz = [n.find(s) for s in stem if n.find(s) >= 0]
            c = sorted(poz)[len(poz) // 2] if poz else 0
            i = max(0, min(c - MAX_CARACTERE_ATOM // 2, len(txt) - MAX_CARACTERE_ATOM))
            txt = txt[i:i + MAX_CARACTERE_ATOM]
        rel_atr = "".join(' %s="%s"' % ("modifica" if fel == "modificare" else "deroga_de_la", t)
                          for fel, t in relatie.get(a["id"], []) if t in vazut)
        blocuri.append('<atom id="%s" temei="%s" valabil_din="%s"%s%s>\n%s\n</atom>'
                       % (a["id"], intrebari.temei_uman(a), a.get("valabil_din") or "nedovedit",
                          ' fragment="trunchiat"' if trunchiat else "", rel_atr, txt))
    utilizator = ("<intrebare>%s</intrebare>\n<data_referinta>%s (%s)</data_referinta>\n\n%s"
                  % (q["intrebare"], data_ref, precizie, "\n\n".join(blocuri)))
    return utilizator, atomi, data_ref, precizie, relatie


# ── verificarea MECANICA ─────────────────────────────────────────────────────────────────────────
_SPATII = re.compile(r"\s+")
_CIFRA = re.compile(r"\d+(?:[.,]\d+)*")
_TRIMITERE = re.compile(r"\b(art|alin|lit|pct|nr|anexa)\.?\s*\(?[\w^]+\)?", re.I)
# V1 (defect de clasa, gasit dupa rularea v3): identificatorul unui ACT ("OPANAF 587/2016",
# "Legea nr. 227/2015") nu e o valoare - e o trimitere. Verificatorul il trata ca pe o cifra si a respins
# la Q-PRF-09 un raspuns corect pe fond ("587" si "2016" nu apareau in citate). Se scoate, ca si
# trimiterile la articole, inainte de verificarea cifrelor.
_ID_ACT = re.compile(r"\b\d{1,5}/(19|20)\d\d\b")


def _n(t):
    return _SPATII.sub(" ", t or "").strip()


# C13: o cifra e VALOARE LEGALA daca e procent, termen (zile/luni/ani, "inclusiv") sau sta langa un
# cuvant de valoare legala; atunci trebuie sa fie intr-un CITAT, chiar daca apare si in intrebare.
# Datele calendaristice (zz.ll.aaaa) sunt fapte ale cazului.
_LEGAL_DUPA = re.compile(r"^\s*(%|(de\s+)?(zile|zi|luni|ani)\b|inclusiv)", re.I)
_LEGAL_LANGA = re.compile(r"cot[aăe]|procent|plafon|prag|limit|termen|nivel|maxim|minim|valoare[a]? "
                          r"(nominal|minim|maxim|fiscal)", re.I)
_DATA = re.compile(r"^\d{1,2}\.\d{1,2}\.\d{4}$")


def e_valoare_legala(text, m):
    if _DATA.match(m.group(0)):
        return False
    if _LEGAL_DUPA.match(text[m.end():m.end() + 12]):
        return True
    return bool(_LEGAL_LANGA.search(text[max(0, m.start() - 40):m.start()]))


def verifica(out, atomi, intrebare, data_ref, relatie=None):
    """Lista de incalcari; goala = raspunsul trece. Nu cheama niciun model."""
    dupa_id = {a["id"]: a for a in atomi}
    greseli = []
    if out["stare"] in ("RASPUNS", "INCOMPLET") and not out["citate"]:
        greseli.append("nicio citare")
    for c in out["citate"]:
        a = dupa_id.get(c["atom"])
        if a is None:
            greseli.append("citeaza un atom care nu i-a fost dat: %s" % c["atom"])
            continue
        if len(_n(c["fragment"])) < 20:
            greseli.append("citat prea scurt ca sa fie proba (%s)" % c["atom"])
        elif _n(c["fragment"]) not in _n(a["text"]):
            greseli.append("citatul NU e verbatim in atomul %s" % c["atom"])
        if data_ref and a.get("valabil_din") and a["valabil_din"] > data_ref:
            greseli.append("atomul %s nu era in vigoare la %s" % (c["atom"], data_ref))
    if out["stare"] == "RASPUNS":
        citate = " ".join(_n(c["fragment"]) for c in out["citate"])
        rasp = _ID_ACT.sub(" ", _TRIMITERE.sub(" ", out["raspuns"] or ""))
        for m in _CIFRA.finditer(rasp):
            cifra = m.group(0)
            if e_valoare_legala(rasp, m):
                if cifra not in citate:
                    greseli.append("valoarea legala %r nu apare in niciun citat (C13: o valoare "
                                   "legala se dovedeste din atom, chiar daca e si in intrebare)" % cifra)
            elif cifra not in citate and cifra not in intrebare:
                greseli.append("cifra %r din raspuns nu apare literal in citate sau in intrebare"
                               % cifra)
    # C17 (b): o derogare prezenta in context, de la un atom citat, trebuie TRATATA
    if out["stare"] == "RASPUNS" and relatie:
        citati = {c["atom"] for c in out["citate"]}
        tratate = {d["atom"] for d in out.get("derogari_tratate") or []}
        for sursa, tinte in relatie.items():
            if sursa in dupa_id and any(t in citati for _f, t in tinte) and \
                    sursa not in citati and sursa not in tratate:
                greseli.append("C17: atomul %s deroga de la / modifica un atom citat si raspunsul nu "
                               "il trateaza" % sursa)
        if not (out["raspuns"] or "").strip():
            greseli.append("raspuns gol")
    if out["stare"] == "INCOMPLET" and not out["lipsa"]:
        greseli.append("INCOMPLET fara faptele care lipsesc")
    return greseli


def _cost(usage, model):
    p = PRET.get(model, PRET[MODEL])
    cw = getattr(usage, "cache_creation_input_tokens", 0) or 0
    cr = getattr(usage, "cache_read_input_tokens", 0) or 0
    return (usage.input_tokens * p["in"] + usage.output_tokens * p["out"]
            + cw * p["cache_scriere"] + cr * p["cache_citire"]) / 1e6


FISIER_CHEIE = os.path.expanduser("~/.fiscalos/api_keys.env")


def cheie():
    """Cheia API a FiscalOS, citita NUMAI din ~/.fiscalos/api_keys.env.

    Decizia lui Costin: cheie separata, nu cea din ~/.iconta/api_keys.env (secretele de productie ale
    iConta). Cheia se trece EXPLICIT clientului, ca SDK-ul sa nu cada pe o variabila de mediu sau pe
    un profil gasit altundeva - o cheie luata din alta parte ar muta tacut costul si ar lega FiscalOS
    de iConta. Valoarea nu se afiseaza si nu se scrie niciodata in artefacte."""
    if not os.path.isfile(FISIER_CHEIE):
        raise RuntimeError(
            "Lipseste %s. De configurat: o linie ANTHROPIC_API_KEY=<cheia>, apoi "
            "`chmod 600 %s`." % (FISIER_CHEIE, FISIER_CHEIE))
    mod = os.stat(FISIER_CHEIE).st_mode & 0o777
    if mod & 0o077:
        raise RuntimeError("%s e citibil si de altii (mod %o). De configurat: `chmod 600 %s`."
                           % (FISIER_CHEIE, mod, FISIER_CHEIE))
    for linie in open(FISIER_CHEIE, encoding="utf-8"):
        linie = linie.strip()
        if linie.startswith("ANTHROPIC_API_KEY="):
            v = linie.split("=", 1)[1].strip().strip('"').strip("'")
            if v:
                return v
    raise RuntimeError("%s nu conţine o linie ANTHROPIC_API_KEY=<cheia> nevida." % FISIER_CHEIE)


def cheama(client, utilizator):
    """Un apel. Fallback server-side pentru refuzuri activat (recomandarea pentru claude-opus-5)."""
    r = client.beta.messages.create(
        model=MODEL, max_tokens=16000,
        betas=["server-side-fallback-2026-07-01"], fallbacks="default",
        thinking={"type": "adaptive"},
        system=[{"type": "text", "text": SISTEM, "cache_control": {"type": "ephemeral"}}],
        output_config={"format": {"type": "json_schema", "schema": SCHEMA}},
        messages=[{"role": "user", "content": utilizator}])
    return r


def raspunde(q, idx, client, rel=None):
    utilizator, atomi, data_ref, precizie, relatie = context(q, idx, rel)
    baza = {"id": q["id"], "tip": q["tip"], "intrebare": q["intrebare"],
            "data_referinta": data_ref, "precizie_data": precizie, "strat": "semantic"}
    t0 = time.time()
    r = cheama(client, utilizator)
    u = r.usage
    apel = {"model": r.model, "stop_reason": r.stop_reason, "request_id": getattr(r, "_request_id", None),
            "tokeni": {"intrare": u.input_tokens, "iesire": u.output_tokens,
                       "cache_scriere": getattr(u, "cache_creation_input_tokens", 0) or 0,
                       "cache_citire": getattr(u, "cache_read_input_tokens", 0) or 0},
            "cost_usd": round(_cost(u, r.model), 5), "secunde": round(time.time() - t0, 2)}
    # C15: fallback-ul se pastreaza; orice raspuns venit de la modelul de rezerva se MARCHEAZA
    iteratii = getattr(u, "iterations", None) or []
    apel["fallback"] = bool(r.model != MODEL
                            or any(getattr(b, "type", "") == "fallback" for b in r.content)
                            or any(getattr(x, "type", "") == "fallback_message" for x in iteratii))
    if r.stop_reason == "refusal":
        return dict(baza, stare="NU_POT_RASPUNDE", raspuns=None, argument=[], apel=apel,
                    motiv="modelul a refuzat cererea (stop_reason=refusal) - abţinere")
    text = next((b.text for b in r.content if b.type == "text"), "")
    try:
        out = json.loads(text)
    except ValueError:
        return dict(baza, stare="NU_POT_RASPUNDE", raspuns=None, argument=[], apel=apel,
                    motiv="iesirea modelului nu e JSON valid (stop_reason=%s)" % r.stop_reason)
    return finalizeaza(baza, out, atomi, q, data_ref, relatie, apel)


def finalizeaza(baza, out, atomi, q, data_ref, relatie, apel):
    """Verificarea mecanica + forma raspunsului. Fara model: se poate re-rula pe o propunere salvata."""
    greseli = verifica(out, atomi, q["intrebare"], data_ref, relatie)
    dupa_id = {a["id"]: a for a in atomi}
    argument = [{"atom": c["atom"], "temei": intrebari.temei_uman(dupa_id[c["atom"]]),
                 "act": dupa_id[c["atom"]]["act"], "verbatim": c["fragment"],
                 "valabilitate": intrebari._valabilitate(dupa_id[c["atom"]], data_ref)}
                for c in out["citate"] if c["atom"] in dupa_id]
    rez = dict(baza, declaratie=out["declaratie"], propunerea_modelului=out, apel=apel,
               verificare={"trece": not greseli, "incalcari": greseli},
               relatii_in_context=relatie,
               derogari_tratate=out.get("derogari_tratate") or [])
    if greseli:
        return dict(rez, stare="NU_POT_RASPUNDE", raspuns=None, argument=argument,
                    motiv="VERIFICAREA MECANICA a respins propunerea modelului: " + "; ".join(greseli))
    if out["stare"] == "RASPUNS":
        # C14: langa orice Da/Nu, citatul decisiv - ca cititorul sa-l poata verifica
        if re.match(r"^\s*(Da|Nu)\b", out["raspuns"] or "") and argument:
            rez["citat_decisiv"] = {"atom": argument[0]["atom"], "fragment": argument[0]["verbatim"]}
        return dict(rez, stare="RASPUNS", raspuns=out["raspuns"], argument=argument,
                    motiv="propus de model, trecut prin verificarea mecanica: citate verbatim, cifre "
                          "literale")
    if out["stare"] == "INCOMPLET":
        return dict(rez, stare="NU_POT_RASPUNDE", tip_abtinere="INCOMPLET", lipsa=out["lipsa"],
                    raspuns=None, argument=argument,
                    motiv="INCOMPLET: intrebarea nu da faptele de care depinde raspunsul: "
                          + "; ".join(out["lipsa"]))
    return dict(rez, stare="NU_POT_RASPUNDE", raspuns=None, argument=argument,
                motiv="modelul s-a abţinut: " + out["motiv"])


def reverifica(fis, dest):
    """Re-verifica propunerile SALVATE ale modelului cu verificatorul de acum - fara niciun apel.

    Contextul se reconstruieste determinist (cautarea e mecanica), deci verificarea vede exact atomii
    pe care i-a vazut modelul. Asa se masoara o reparatie a verificatorului pe aceleasi iesiri."""
    from fiscalos import relatii
    vechi = json.load(open(fis, encoding="utf-8"))
    idx = intrebari.Index()
    rel = relatii.Relatii(idx.corp)
    Q = {q["id"]: q for q in intrebari.incarca_intrebari()}
    ies = []
    for r in vechi["raspunsuri"]:
        if not r.get("propunerea_modelului"):
            ies.append(r)
            continue
        q = Q[r["id"]]
        _u, atomi, data_ref, precizie, relatie = context(q, idx, rel)
        baza = {k: r[k] for k in ("id", "tip", "intrebare", "data_referinta", "precizie_data", "strat")}
        ies.append(finalizeaza(baza, r["propunerea_modelului"], atomi, q, data_ref, relatie, r["apel"]))
    rez = dict(vechi, raspunsuri=ies, reverificat_la=time.strftime("%Y-%m-%dT%H:%M:%S"),
               raspunse=sum(1 for r in ies if r["stare"] == "RASPUNS"),
               respinse_de_verificare=sum(1 for r in ies if r.get("verificare") and
                                          not r["verificare"]["trece"]))
    json.dump(rez, open(dest, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return rez


def ruleaza(dest=None, simulare=False):
    t0 = time.time()
    idx = intrebari.Index()
    t_idx = time.time() - t0
    qs = intrebari.incarca_intrebari()
    if simulare:
        # fara apel: marimea contextului, pentru o estimare de cost INAINTE de a cheltui ceva
        from fiscalos import relatii
        rel = relatii.Relatii(idx.corp)
        L = [len(context(q, idx, rel)[0]) for q in qs]
        return {"intrebari": len(qs), "caractere_context": sum(L), "max": max(L),
                "tokeni_intrare_estimati": int(sum(L) / 3.2) + len(qs) * int(len(SISTEM) / 3.2)}
    import anthropic
    from fiscalos import relatii
    client = anthropic.Anthropic(api_key=cheie())
    rel = relatii.Relatii(idx.corp)
    ies = [raspunde(q, idx, client, rel) for q in qs]
    for r in ies:
        if r["stare"] == "RASPUNS":
            assert r["argument"] and r["verificare"]["trece"], r["id"]
    tok = {k: sum(r["apel"]["tokeni"][k] for r in ies if r.get("apel"))
           for k in ("intrare", "iesire", "cache_scriere", "cache_citire")}
    rez = {"_ce": "Raspunsurile stratului semantic ancorat pe atomi (C3 a).", "model": MODEL,
           "data_intrebarii": intrebari.DATA_INTREBARII, "n": len(ies),
           "raspunse": sum(1 for r in ies if r["stare"] == "RASPUNS"),
           "respinse_de_verificare": sum(1 for r in ies if r.get("verificare") and
                                         not r["verificare"]["trece"]),
           "incomplete_detectate": sum(1 for r in ies if r.get("tip_abtinere") == "INCOMPLET"),
           "de_la_modelul_de_rezerva": [r["id"] for r in ies if r.get("apel", {}).get("fallback")],
           "respinse_C17": [r["id"] for r in ies if any("C17" in g for g in
                                                          (r.get("verificare") or {}).get("incalcari", []))],
           "respinse_C13": [r["id"] for r in ies if any("C13" in g for g in
                                                          (r.get("verificare") or {}).get("incalcari", []))],
           "tokeni": tok, "cost_usd": round(sum(r["apel"]["cost_usd"] for r in ies if r.get("apel")), 4),
           "secunde_index": round(t_idx, 2), "secunde_total": round(time.time() - t0, 2),
           "raspunsuri": ies}
    dest = dest or os.path.join(_RAD, "artefacte", "intrebari", "raspunsuri_semantic.json")
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(rez, f, ensure_ascii=False, indent=1)
    return rez


if __name__ == "__main__":
    import sys
    if "--simulare" in sys.argv:
        print(json.dumps(ruleaza(simulare=True), indent=1))
    else:
        r = ruleaza()
        print("semantic: %d raspunse / %d | respinse de verificare %d | incomplete %d | %s tokeni | "
              "$%.4f | %.0f s" % (r["raspunse"], r["n"], r["respinse_de_verificare"],
                                  r["incomplete_detectate"], r["tokeni"], r["cost_usd"],
                                  r["secunde_total"]))
