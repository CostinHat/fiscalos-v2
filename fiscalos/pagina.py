# -*- coding: utf-8 -*-
"""PAGINA DE ÎNTREBĂRI pentru Costin (punctul 7). Separată de iConta: alt proces, alt port, alte date.

Fluxul (7a): întrebarea → motorul spune ce date lipsesc și cere completarea → întrebarea reformulată
completă, confirmată de Costin → abia apoi răspunsul. Răspunsul ca poveste (7b): data de referință și
perimetrul, argumentul cu fiecare text de lege citat verbatim (act, articol, alineat, forma consolidată și
data ei), calculul pas cu pas, avertismentele, abținerea cu motivul. Fiecare întrebare se păstrează (text,
dialog, răspuns, cost) - 7c - în `pagina_date/`, în afara git-ului; ele NU se folosesc la reglaj (7d):
niciun modul al motorului nu citește acest director (probă în test_pagina.py).

Numai biblioteca standard. Ascultă pe 127.0.0.1 (invizibil din afară); expunerea se face prin nginx cu
HTTPS (configurația pentru administrator: `pagina_nginx.conf`) sau, până atunci, printr-un tunel SSH.
Autentificare proprie: un singur utilizator, parolă păstrată ca hash PBKDF2 în ~/.fiscalos/pagina.env
(mod 600), sesiune cu cookie HttpOnly + SameSite=Strict, jeton anti-CSRF pe fiecare formular.
"""
import hashlib
import hmac
import html
import json
import os
import re
import secrets
import sys
import threading
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = os.path.join(_RAD, "pagina_date")
INTREBARI = os.path.join(DATE, "intrebari_costin")      # 7c/7d: pastrate, NU folosite la reglaj
URMARIRE = os.path.join(_RAD, "urmarire", "rezultate")   # punctul 8c
FISIER_ACCES = os.path.expanduser("~/.fiscalos/pagina.env")
PORT = int(os.environ.get("FISCALOS_PAGINA_PORT", "8030"))
UTILIZATOR = "costin"
SESIUNE_ORE = 12

_sesiuni = {}                 # jeton -> {"expira": t, "csrf": ...}
_incercari = {}               # ip -> [timpi esuati] (limitare a ghicirii parolei)
_motor = {}                   # idx, sistem, client - incarcate o singura data
_lucru = {}                   # id intrebare -> "in lucru"
_blocaj = threading.Lock()


# ── accesul ──────────────────────────────────────────────────────────────────────────────────────
def _hash(parola, sare):
    return hashlib.pbkdf2_hmac("sha256", parola.encode("utf-8"), bytes.fromhex(sare), 300000).hex()


FISIER_PAROLA_INITIALA = os.path.expanduser("~/.fiscalos/pagina_parola_initiala.txt")


def _scrie_600(cale, text):
    os.makedirs(os.path.dirname(cale), exist_ok=True)
    tmp = cale + ".tmp"
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f:
        f.write(text)
    os.replace(tmp, cale)


def seteaza_parola(parola):
    sare = secrets.token_hex(16)
    _scrie_600(FISIER_ACCES, "FISCALOS_PAGINA_SARE=%s\nFISCALOS_PAGINA_HASH=%s\n" % (sare, _hash(parola, sare)))
    if os.path.exists(FISIER_PAROLA_INITIALA):
        os.remove(FISIER_PAROLA_INITIALA)                    # parola aleasa de Costin o inlocuieste


def initializeaza_acces():
    """La prima pornire: o parola aleatoare, scrisa NUMAI in ~/.fiscalos/pagina_parola_initiala.txt (mod
    600; nu se tipareste); pe server se pastreaza doar hash-ul. Costin o schimba cu `--parola`."""
    if os.path.exists(FISIER_ACCES):
        return False
    parola = "-".join(secrets.token_urlsafe(4) for _ in range(4))
    seteaza_parola(parola)
    _scrie_600(FISIER_PAROLA_INITIALA, parola + "\n")
    return True


def _acces():
    v = dict(l.strip().split("=", 1) for l in open(FISIER_ACCES) if "=" in l)
    return v["FISCALOS_PAGINA_SARE"], v["FISCALOS_PAGINA_HASH"]


def verifica_parola(parola):
    sare, h = _acces()
    return hmac.compare_digest(_hash(parola, sare), h)


# ── motorul ──────────────────────────────────────────────────────────────────────────────────────
F_STRAT_OFICIAL = os.path.join(_RAD, "artefacte", "atomi_oficiale", "_raport.json")


def _versiune_corpus():
    return os.path.getmtime(F_STRAT_OFICIAL) if os.path.exists(F_STRAT_OFICIAL) else None


def motor():
    """Indexul se incarca o data; se REINCARCA daca urmarirea (punctul 8) a adus o forma noua a unei legi
    si nicio intrebare nu e in lucru - altfel pagina ar raspunde din textul vechi."""
    with _blocaj:
        if _motor and _motor.get("corpus") != _versiune_corpus() and not _lucru:
            _motor.clear()
        if not _motor:
            import anthropic
            from fiscalos import intrebari, navigare, semantic
            idx = intrebari.Index()
            _motor.update(idx=idx, sistem=navigare.sistem(idx), corpus=_versiune_corpus(),
                          client=anthropic.Anthropic(api_key=semantic.cheie()))
        return _motor


_SCHEMA_LIPSA = {"type": "object", "properties": {
    "date_lipsa": {"type": "array", "items": {"type": "object", "properties": {
        "intrebare": {"type": "string"}, "de_ce_conteaza": {"type": "string"}},
        "required": ["intrebare", "de_ce_conteaza"], "additionalProperties": False}},
    "presupuneri": {"type": "array", "items": {"type": "string"}}},
    "required": ["date_lipsa", "presupuneri"], "additionalProperties": False}
_SCHEMA_REFORMULARE = {"type": "object", "properties": {"intrebare_completa": {"type": "string"}},
                       "required": ["intrebare_completa"], "additionalProperties": False}
_SISTEM_PREGATIRE = (
    "Ești asistentul care PREGĂTEȘTE o întrebare de fiscalitate și contabilitate românească înainte să "
    "ajungă la motorul care răspunde din lege. Nu răspunzi la întrebare și nu dai valori legale.")


def _apel_structurat(sistem, mesaj, schema):
    from fiscalos import navigare, semantic
    m = motor()
    r = m["client"].messages.create(model=navigare.MODEL, max_tokens=4000, thinking={"type": "adaptive"},
                                    system=sistem, messages=[{"role": "user", "content": mesaj}],
                                    output_config={"format": {"type": "json_schema", "schema": schema}})
    text = next(b.text for b in r.content if b.type == "text")
    return json.loads(text), round(semantic._cost(r.usage, r.model), 5)


_CIFRA = re.compile(r"\d+(?:[.,]\d+)*")


def cifre_nesursate(text, intrebare):
    """Regula 5 la pregatire: pasul acesta NU citeste legea, deci nu are voie sa aduca valori (cote,
    plafoane, date, termene). Orice numar care nu e deja in textul lui Costin e suspect."""
    din_q = set(_CIFRA.findall(intrebare))
    return sorted({c for c in _CIFRA.findall(text) if c not in din_q})


def cere_date_lipsa(intrebare):
    cer = (
        "Întrebarea utilizatorului:\n<intrebare>%s</intrebare>\n\nSpune ce FAPTE ale cazului lipsesc și de care "
        "depinde răspunsul (perioada/data, tipul persoanei, regimul fiscal, sume, durate etc.) — fiecare ca o "
        "întrebare scurtă către utilizator, cu motivul. CEL MULT 4, cele mai decisive; nu cere ce se deduce clar "
        "din text. Dacă nu lipsește nimic, `date_lipsa` e goală. În `presupuneri`, ce ai presupune dacă "
        "utilizatorul nu precizează.\n\nINTERDICȚIE: nu consulți legea în acest pas, deci NU scrii nicio valoare "
        "legală — nicio cotă, plafon, prag, sumă, dată de intrare în vigoare, termen sau număr de articol. "
        "Motivul spune doar CE fel de fapt contează („cota depinde de perioadă”), nu valoarea. Singurele cifre "
        "admise sunt cele din întrebarea utilizatorului." % intrebare)
    rez, cost = _apel_structurat(_SISTEM_PREGATIRE, cer, _SCHEMA_LIPSA)
    tot = lambda r: " ".join([x["intrebare"] + " " + x["de_ce_conteaza"] for x in r["date_lipsa"]] + r["presupuneri"])
    if cifre_nesursate(tot(rez), intrebare):
        rez2, cost2 = _apel_structurat(_SISTEM_PREGATIRE, cer + "\n\nO încercare anterioară a scris valori "
                                       "(%s) care nu sunt în întrebare. Rescrie fără ele." % ", ".join(
                                           cifre_nesursate(tot(rez), intrebare)), _SCHEMA_LIPSA)
        rez, cost = rez2, round(cost + cost2, 5)
        rez["reincercare_cifre"] = True
    rez["date_lipsa"] = rez["date_lipsa"][:4]
    rez["cifre_nesursate"] = cifre_nesursate(tot(rez), intrebare)
    return rez, cost


def reformuleaza(intrebare, completari):
    lista = "\n".join("- %s → %s" % (q, (r or "(fără răspuns)")) for q, r in completari)
    return _apel_structurat(_SISTEM_PREGATIRE, (
        "Întrebarea inițială:\n<intrebare>%s</intrebare>\n\nCompletările utilizatorului:\n%s\n\nScrie întrebarea "
        "COMPLETĂ, într-un singur text, care include toate faptele de mai sus, fără să adaugi fapte noi, fără "
        "valori legale și fără să răspunzi. Un fapt la care utilizatorul n-a răspuns NU se inventează: rămâne "
        "nespecificat." % (intrebare, lista or "(niciuna)")), _SCHEMA_REFORMULARE)


def raspunde_complet(qid):
    """Ruleaza motorul pe intrebarea confirmata si salveaza raspunsul (in fundal)."""
    from fiscalos import navigare
    d = incarca(qid)
    try:
        m = motor()
        r = navigare.raspunde({"id": qid, "tip": "PAGINA", "intrebare": d["intrebare_confirmata"]},
                              m["idx"], m["idx"].rel, m["client"], m["sistem"])
        d["raspuns"] = r
        d["cost"]["raspuns"] = r["apel"]["cost_usd"]
        d["stare"] = "raspuns"
    except Exception as e:                                   # se scrie, nu se ascunde
        d["stare"], d["eroare"] = "eroare", "%s: %s" % (type(e).__name__, str(e)[:500])
    d["dialog"].append({"cand": time.strftime("%Y-%m-%d %H:%M:%S"), "cine": "motor", "ce": d["stare"]})
    salveaza(d)
    _lucru.pop(qid, None)


# ── pastrarea (7c) ───────────────────────────────────────────────────────────────────────────────
def _cale(qid):
    if not re.match(r"^[0-9]{8}-[0-9]{6}-[a-f0-9]{6}$", qid):
        raise ValueError("id invalid")
    return os.path.join(INTREBARI, qid + ".json")


def salveaza(d):
    os.makedirs(INTREBARI, exist_ok=True)
    tmp = _cale(d["id"]) + ".tmp"
    json.dump(d, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
    os.replace(tmp, _cale(d["id"]))


def incarca(qid):
    return json.load(open(_cale(qid), encoding="utf-8"))


def toate():
    if not os.path.isdir(INTREBARI):
        return []
    return sorted((json.load(open(os.path.join(INTREBARI, f), encoding="utf-8"))
                   for f in os.listdir(INTREBARI) if f.endswith(".json")), key=lambda d: d["id"], reverse=True)


def intrebare_noua(text):
    qid = time.strftime("%Y%m%d-%H%M%S-") + secrets.token_hex(3)
    d = {"id": qid, "creat": time.strftime("%Y-%m-%d %H:%M:%S"), "intrebare": text, "stare": "noua",
         "dialog": [{"cand": time.strftime("%Y-%m-%d %H:%M:%S"), "cine": "Costin", "ce": text}],
         "cost": {}, "folosire": "NU se foloseste la reglaj; material pentru un set viitor, dupa verificare "
                                 "independenta"}
    lipsa, cost = cere_date_lipsa(text)
    d.update(date_lipsa=lipsa["date_lipsa"], presupuneri=lipsa["presupuneri"], stare="completare",
             cifre_nesursate_la_pregatire=lipsa["cifre_nesursate"])
    d["cost"]["date_lipsa"] = cost
    d["dialog"].append({"cand": time.strftime("%Y-%m-%d %H:%M:%S"), "cine": "motor", "ce": lipsa})
    salveaza(d)
    return d


def completeaza(qid, raspunsuri):
    d = incarca(qid)
    perechi = [(x["intrebare"], raspunsuri.get(str(i), "").strip()) for i, x in enumerate(d["date_lipsa"])]
    d["completari"] = perechi
    d["dialog"].append({"cand": time.strftime("%Y-%m-%d %H:%M:%S"), "cine": "Costin", "ce": perechi})
    ref, cost = reformuleaza(d["intrebare"], perechi)
    d["intrebare_reformulata"], d["stare"] = ref["intrebare_completa"], "confirmare"
    d["cost"]["reformulare"] = cost
    d["dialog"].append({"cand": time.strftime("%Y-%m-%d %H:%M:%S"), "cine": "motor", "ce": ref["intrebare_completa"]})
    salveaza(d)
    return d


def continua(qid):
    """INCOMPLET (7a): motorul a spus ce fapte lipsesc DUPA ce a citit legea. Costin le completeaza si
    intrebarea reia fluxul (reformulare -> confirmare -> raspuns) ca intrebare noua, legata de prima."""
    vechi = incarca(qid)
    nou = time.strftime("%Y%m%d-%H%M%S-") + secrets.token_hex(3)
    d = {"id": nou, "creat": time.strftime("%Y-%m-%d %H:%M:%S"), "intrebare": vechi["intrebare_confirmata"],
         "continua": qid, "stare": "completare", "cost": {}, "folosire": vechi["folosire"],
         "date_lipsa": [{"intrebare": x, "de_ce_conteaza": "cerut de motor după citirea legii (întrebarea %s)" % qid}
                        for x in vechi["raspuns"].get("lipsa") or []], "presupuneri": [],
         "cifre_nesursate_la_pregatire": [],
         "dialog": [{"cand": time.strftime("%Y-%m-%d %H:%M:%S"), "cine": "Costin", "ce": "continuare a %s" % qid}]}
    salveaza(d)
    return d


def confirma(qid, text):
    d = incarca(qid)
    d["intrebare_confirmata"], d["stare"] = text.strip(), "in_lucru"
    d["dialog"].append({"cand": time.strftime("%Y-%m-%d %H:%M:%S"), "cine": "Costin", "ce": "confirmat: " + text.strip()})
    salveaza(d)
    _lucru[qid] = True
    threading.Thread(target=raspunde_complet, args=(qid,), daemon=True).start()
    return d


# ── afișarea ─────────────────────────────────────────────────────────────────────────────────────
E = html.escape
CSS = """body{font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:900px;margin:24px auto;padding:0 16px;
color:#1d2433;background:#fafbfc;line-height:1.5}h1{font-size:1.4em}h2{font-size:1.15em;margin-top:1.6em}
textarea,input[type=text],input[type=password]{width:100%;box-sizing:border-box;font:inherit;padding:8px;
border:1px solid #b9c2cf;border-radius:6px}button{font:inherit;padding:8px 18px;border:0;border-radius:6px;
background:#1f5fbf;color:#fff;cursor:pointer}.cutie{background:#fff;border:1px solid #dfe3e8;border-radius:8px;
padding:14px 16px;margin:12px 0}.lege{border-left:4px solid #1f5fbf;padding:6px 12px;margin:8px 0;
background:#f3f6fb}.mic{color:#5b6576;font-size:.9em}.av{border-left:4px solid #c27c0e;background:#fff8ec;
padding:6px 12px}.abt{border-left:4px solid #b3261e;background:#fdf0ef;padding:6px 12px}
code{background:#eef1f5;padding:1px 4px;border-radius:4px}a{color:#1f5fbf}table{border-collapse:collapse}
td,th{border-bottom:1px solid #e5e8ec;padding:4px 8px;text-align:left}"""


def pagina(titlu, corp, reimprospatare=None):
    meta = '<meta http-equiv="refresh" content="%d">' % reimprospatare if reimprospatare else ""
    return ("<!doctype html><html lang='ro'><head><meta charset='utf-8'><meta name='viewport' "
            "content='width=device-width,initial-scale=1'>%s<title>%s</title><style>%s</style></head><body>"
            "<p class='mic'><a href='/'>Întrebări</a> · <a href='/urmarire'>Urmărirea legilor</a> · "
            "<a href='/iesire'>Ieșire</a></p>%s</body></html>" % (meta, E(titlu), CSS, corp))


def _forma_consolidata(atom_id):
    """Forma textului citat si data ei - din `sursa_act` al corpusului; pentru actele compuse (C19),
    data partii din care vine atomul. Ce nu se stie se spune ("data formei nedovedita")."""
    corp = motor()["idx"].corp
    a = corp.dupa_id.get(atom_id) or {}
    if a.get("data_formei"):
        return "%s, forma din %s" % (a.get("parte", ""), a["data_formei"])
    s = corp.sursa_act.get(atom_id.split("#")[0], {}).get("sursa", "")
    return s if "oficial" in s else (s or "sursă necunoscută") + ", data formei nedovedită"


def poveste(r):
    """Raspunsul ca poveste (7b)."""
    P = []
    P.append("<h2>1. Data de referință și perimetrul presupus</h2><div class='cutie'>")
    P.append("<p><b>Data de referință:</b> %s</p>" % E(str(r.get("data_referinta") or "—")))
    if r.get("data_referinta_motiv"):
        P.append("<p class='mic'>%s</p>" % E(r["data_referinta_motiv"]))
    P.append("<p><b>Perimetrul:</b> %s</p></div>" % E(r.get("declaratie") or "—"))
    respins = r["stare"] != "RASPUNS" and not r.get("lipsa")
    if r["stare"] == "RASPUNS":
        corp = re.split(r"  \[(?:calcul|avertisment|data de referință)", r["raspuns"])[0]
        P.append("<h2>2. Răspunsul</h2><div class='cutie'><p><b>%s</b></p></div>" % E(corp))
    else:
        P.append("<h2>2. Abținere</h2><div class='abt'><p><b>Motorul nu răspunde.</b> %s</p>" % E(r.get("motiv") or ""))
        if r.get("lipsa"):
            P.append("<p>Ce lipsește:</p><ul>%s</ul>" % "".join("<li>%s</li>" % E(x) for x in r["lipsa"]))
        if r.get("raspuns_conditionat"):
            P.append("<p>%s</p>" % E(r["raspuns_conditionat"]))
        P.append("</div>")
    if r.get("argument"):
        P.append("<h2>3. Argumentul — textele de lege, citate verbatim</h2>")
        if respins:
            P.append("<p class='av'>Propunerea modelului a fost respinsă de verificare; textele de mai jos sunt "
                     "cele pe care le-a consultat, nu un temei dovedit pentru un răspuns.</p>")
        for a in r["argument"]:
            val = a.get("valabilitate") or {}
            P.append("<div class='lege'><p><b>%s</b> <span class='mic'>(%s; în vigoare din %s)</span></p>"
                     "<p>„%s”</p><p class='mic'><code>%s</code></p></div>" % (
                         E(a["temei"]), E(_forma_consolidata(a["atom"])), E(str(val.get("valabil_din") or "nedovedit")),
                         E(a["verbatim"]), E(a["atom"])))
    for d in r.get("derogari_tratate") or []:
        P.append("<p class='mic'>Derogare tratată: <code>%s</code> — %s</p>" % (E(d["atom"]), E(d["cum"])))
    if r.get("calcule"):
        P.append("<h2>4. Calculul, pas cu pas (evaluat de cod, nu de model)</h2><div class='cutie'><ol>")
        for c in r["calcule"]:
            for z in c.get("zile") or []:
                P.append("<li class='mic'>%s</li>" % E(z))
            P.append("<li><code>%s = %s</code> = %s = <b>%s</b><ul>" % (E(c["nume"]), E(c["formula"]),
                                                                       E(c.get("cu_valori", "")), E(c["rezultat"])))
            for o in c["operanzi"]:
                P.append("<li class='mic'>%s = %s — %s%s</li>" % (
                    E(o["nume"]), E(o["valoare"]), "din " + E(o["atom"]) if o.get("atom") else "din întrebare",
                    ": „%s”" % E(o["fragment"]) if o.get("fragment") else ""))
            P.append("</ul></li>")
        P.append("</ol></div>")
    if r.get("avertismente"):
        P.append("<h2>5. Avertismente</h2>" + "".join("<div class='av'>%s</div>" % E(a) for a in r["avertismente"]))
    return "".join(P)


def _cost_total(d):
    return round(sum(v for v in (d.get("cost") or {}).values() if isinstance(v, (int, float))), 4)


def vede_intrebare(d, csrf):
    P = ["<h1>Întrebarea %s</h1><div class='cutie'><p>%s</p><p class='mic'>pusă la %s · cost până acum: "
         "<b>$%.4f</b> %s</p></div>" % (E(d["id"]), E(d["intrebare"]), E(d["creat"]), _cost_total(d),
                                          E(json.dumps(d.get("cost") or {})))]
    if d["stare"] == "completare":
        P.append("<h2>Ce date lipsesc</h2><p class='mic'>Pasul acesta doar pregătește întrebarea; nu citește "
                 "legea și nu dă valori. Lasă gol ce nu știi — motorul va spune atunci de ce depinde răspunsul.</p>")
        if d.get("cifre_nesursate_la_pregatire"):
            P.append("<div class='av'>Atenție: textul de mai jos conține cifre care nu vin din întrebarea ta "
                     "și nici din lege (%s). Ignoră-le.</div>" % E(", ".join(d["cifre_nesursate_la_pregatire"])))
        P.append("<form method='post' action='/completeaza'>"
                 "<input type='hidden' name='id' value='%s'><input type='hidden' name='csrf' value='%s'>" % (E(d["id"]), csrf))
        if not d["date_lipsa"]:
            P.append("<p>Motorul nu are nevoie de alte date.</p>")
        for i, x in enumerate(d["date_lipsa"]):
            P.append("<p><b>%s</b><br><span class='mic'>%s</span><br><input type='text' name='r%d'></p>" % (
                E(x["intrebare"]), E(x["de_ce_conteaza"]), i))
        if d.get("presupuneri"):
            P.append("<p class='mic'>Dacă nu precizezi, motorul ar presupune: %s</p>" % E("; ".join(d["presupuneri"])))
        P.append("<button>Mai departe</button></form>")
    elif d["stare"] == "confirmare":
        P.append("<h2>Întrebarea completă — confirm-o (o poți corecta)</h2><form method='post' action='/confirma'>"
                 "<input type='hidden' name='id' value='%s'><input type='hidden' name='csrf' value='%s'>"
                 "<textarea name='text' rows='6'>%s</textarea><p><button>Confirm și cer răspunsul</button></p></form>"
                 % (E(d["id"]), csrf, E(d["intrebare_reformulata"])))
    elif d["stare"] == "in_lucru":
        P.append("<div class='cutie'><p>Motorul caută în lege și verifică răspunsul (de obicei 1–3 minute). "
                 "Pagina se reîmprospătează singură.</p><p class='mic'>Întrebarea confirmată: %s</p></div>"
                 % E(d["intrebare_confirmata"]))
        return pagina("În lucru", "".join(P), reimprospatare=8)
    elif d["stare"] == "raspuns":
        if d.get("continua"):
            P.append("<p class='mic'>Continuare a întrebării <a href='/i/%s'>%s</a>.</p>" % (E(d["continua"]), E(d["continua"])))
        P.append("<p class='mic'>Întrebarea confirmată: %s</p>" % E(d["intrebare_confirmata"]))
        P.append(poveste(d["raspuns"]))
        if d["raspuns"].get("lipsa"):
            P.append("<form method='post' action='/continua'><input type='hidden' name='id' value='%s'>"
                     "<input type='hidden' name='csrf' value='%s'><p><button>Completez faptele cerute și "
                     "reîntreb</button></p></form>" % (E(d["id"]), csrf))
    elif d["stare"] == "eroare":
        P.append("<div class='abt'>Eroare: %s</div>" % E(d.get("eroare", "")))
    return pagina("Întrebarea %s" % d["id"], "".join(P))


def acasa(csrf):
    P = ["<h1>FiscalOS — întrebări</h1><form method='post' action='/intreaba'>"
         "<input type='hidden' name='csrf' value='%s'><textarea name='text' rows='5' placeholder='Scrie întrebarea "
         "de fiscalitate sau contabilitate…' required></textarea><p><button>Trimite</button></p></form>" % csrf]
    tot = toate()
    if tot:
        P.append("<h2>Întrebările tale</h2><table><tr><th>Când</th><th>Întrebarea</th><th>Stare</th><th>Cost</th></tr>")
        for d in tot:
            P.append("<tr><td class='mic'>%s</td><td><a href='/i/%s'>%s</a></td><td>%s</td><td>$%.4f</td></tr>" % (
                E(d["creat"]), E(d["id"]), E(d["intrebare"][:90]), E(d["stare"]), _cost_total(d)))
        P.append("</table><p class='mic'>Cost total: <b>$%.4f</b>. Întrebările de aici nu se folosesc pentru "
                 "reglajul motorului.</p>" % sum(_cost_total(d) for d in tot))
    return pagina("FiscalOS — întrebări", "".join(P))


def urmarire_html():
    P = ["<h1>Urmărirea legilor pentru iConta</h1><p class='mic'>Verificare săptămânală automată a formelor "
         "consolidate pe legislatie.just.ro; o propunere nouă nu se aplică niciodată automat.</p>"]
    if not os.path.isdir(URMARIRE) or not os.listdir(URMARIRE):
        P.append("<p>Nicio verificare încă.</p>")
    else:
        for f in sorted(os.listdir(URMARIRE), reverse=True):
            if not f.endswith(".json"):
                continue
            v = json.load(open(os.path.join(URMARIRE, f), encoding="utf-8"))
            P.append("<div class='cutie'><p><b>%s</b> — %s</p>%s</div>" % (
                E(v.get("data_verificarii", f)), E(v.get("rezumat", "")),
                "".join("<p class='mic'>%s</p>" % E(x) for x in v.get("detalii", [])[:30])))
    return pagina("Urmărirea legilor", "".join(P))


def login_html(mesaj=""):
    return pagina("Intrare", "<h1>FiscalOS — intrare</h1>%s<form method='post' action='/intrare'>"
                  "<p>Parola<br><input type='password' name='parola' autofocus></p><button>Intră</button></form>"
                  % ("<p class='abt'>%s</p>" % E(mesaj) if mesaj else ""))


class Handler(BaseHTTPRequestHandler):
    server_version = "FiscalOS"

    def log_message(self, fmt, *a):
        sys.stderr.write("%s %s\n" % (time.strftime("%Y-%m-%d %H:%M:%S"), fmt % a))

    def _sesiune(self):
        c = self.headers.get("Cookie", "")
        m = re.search(r"fiscalos=([A-Za-z0-9_\-]+)", c)
        s = _sesiuni.get(m.group(1)) if m else None
        if s and s["expira"] > time.time():
            return s
        return None

    def _trimite(self, cod, corp, antet=None):
        b = corp.encode("utf-8")
        self.send_response(cod)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(b)))
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Cache-Control", "no-store")
        for k, v in (antet or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(b)

    def _redirect(self, unde, antet=None):
        self.send_response(303)
        self.send_header("Location", unde)
        for k, v in (antet or {}).items():
            self.send_header(k, v)
        self.end_headers()

    def _form(self):
        n = int(self.headers.get("Content-Length", "0") or 0)
        if n > 200000:
            raise ValueError("cerere prea mare")
        return {k: v[0] for k, v in urllib.parse.parse_qs(self.rfile.read(n).decode("utf-8")).items()}

    def do_GET(self):
        s = self._sesiune()
        if self.path.startswith("/intrare") or not s:
            return self._trimite(200, login_html())
        if self.path == "/iesire":
            return self._redirect("/intrare", {"Set-Cookie": "fiscalos=; Max-Age=0; Path=/; HttpOnly; SameSite=Strict"})
        if self.path == "/":
            return self._trimite(200, acasa(s["csrf"]))
        if self.path == "/urmarire":
            return self._trimite(200, urmarire_html())
        m = re.match(r"^/i/([0-9a-f\-]+)$", self.path)
        if m:
            try:
                return self._trimite(200, vede_intrebare(incarca(m.group(1)), s["csrf"]))
            except (ValueError, OSError):
                return self._trimite(404, pagina("Negăsit", "<p>Întrebare inexistentă.</p>"))
        return self._trimite(404, pagina("Negăsit", "<p>Pagină inexistentă.</p>"))

    def do_POST(self):
        ip = self.headers.get("X-Real-IP") or self.client_address[0]
        try:
            f = self._form()
        except ValueError:
            return self._trimite(413, pagina("Eroare", "<p>Cerere prea mare.</p>"))
        if self.path == "/intrare":
            recente = [t for t in _incercari.get(ip, []) if t > time.time() - 900]
            if len(recente) >= 8:
                return self._trimite(429, login_html("Prea multe încercări; reîncearcă peste 15 minute."))
            if verifica_parola(f.get("parola", "")):
                jet = secrets.token_urlsafe(32)
                _sesiuni[jet] = {"expira": time.time() + SESIUNE_ORE * 3600, "csrf": secrets.token_urlsafe(24)}
                secure = "; Secure" if self.headers.get("X-Forwarded-Proto") == "https" else ""
                return self._redirect("/", {"Set-Cookie": "fiscalos=%s; Path=/; HttpOnly; SameSite=Strict; Max-Age=%d%s"
                                                          % (jet, SESIUNE_ORE * 3600, secure)})
            _incercari[ip] = recente + [time.time()]
            return self._trimite(401, login_html("Parolă greșită."))
        s = self._sesiune()
        if not s or not hmac.compare_digest(f.get("csrf", ""), s["csrf"]):
            return self._trimite(403, login_html("Sesiune expirată; intră din nou."))
        try:
            if self.path == "/intreaba" and f.get("text", "").strip():
                d = intrebare_noua(f["text"].strip()[:5000])
                return self._redirect("/i/%s" % d["id"])
            if self.path == "/completeaza":
                d = completeaza(f["id"], {k[1:]: v for k, v in f.items() if re.match(r"^r\d+$", k)})
                return self._redirect("/i/%s" % d["id"])
            if self.path == "/continua":
                d = continua(f["id"])
                return self._redirect("/i/%s" % d["id"])
            if self.path == "/confirma" and f.get("text", "").strip():
                d = confirma(f["id"], f["text"][:6000])
                return self._redirect("/i/%s" % d["id"])
        except Exception as e:
            return self._trimite(500, pagina("Eroare", "<div class='abt'>%s: %s</div>" % (E(type(e).__name__), E(str(e)[:400]))))
        return self._redirect("/")


def porneste(port=PORT):
    if initializeaza_acces():
        print("parola initiala scrisa in %s (mod 600)" % FISIER_PAROLA_INITIALA, flush=True)
    motor()                                                   # indexul se incarca inainte de prima cerere
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print("FiscalOS pagina pe http://127.0.0.1:%d" % port, flush=True)
    srv.serve_forever()


if __name__ == "__main__":
    if "--parola" in sys.argv:                               # Costin isi alege parola (nu apare pe ecran)
        import getpass
        p1, p2 = getpass.getpass("Parola noua: "), getpass.getpass("Inca o data: ")
        if p1 != p2 or len(p1) < 10:
            sys.exit("Parolele difera sau au sub 10 caractere; nimic schimbat.")
        seteaza_parola(p1)
        print("Parola schimbata. Sesiunile vechi expira la repornirea paginii.")
    else:
        porneste()
