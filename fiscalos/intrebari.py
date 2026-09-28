# -*- coding: utf-8 -*-
"""C6 — MOTORUL DE ÎNTREBĂRI: raspuns argumentat din atomi, sau "nu pot raspunde" cu motiv.

CE PROMITE, si ce NU. Pentru fiecare intrebare: un raspuns care citeaza atomul (temei + fragment
verbatim + valabilitate la data intrebarii), SAU "nu pot raspunde" cu motivul. NICIODATA un raspuns
fara atom: orice raspuns fara `argument` e un defect si o proba il prinde. Motorul NU e un jurist: nu
compune reguli si nu rationeaza despre capcane. E un extractor care stie sa spuna cand nu stie.

ORB LA CHEIE, MECANIC (decizia arhitectului: "raspunsurile verificate din CSV nu le folosesti la
constructie; le compari abia la final"). `incarca_intrebari` citeste NUMAI coloanele din
`COLOANE_PERMISE`. Coloanele cu raspunsul si temeiul asteptat nu apar in acest modul - nici ca sir -,
si `test_intrebari.py` o verifica prin AST. Comparaţia traieste in alt modul (`comparatie.py`) si
ruleaza DUPA ce raspunsurile au fost scrise si comise.

REGULILE DE CLASA, fixate INAINTE de prima rulare (nu dupa ce s-a vazut ce iese):
  R-DATA   Fara referinta temporala in intrebare -> NU POT: valorile fiscale se schimba in timp, iar
           valabilitatea la data intrebarii e o cerinta, nu un detaliu.
  R-SURSA  Raspunde numai un atom dintr-un ACT NORMATIV (`surse.e_act_normativ`), NEABROGAT.
  R-VERS   Redarile istorice (`*forma_initiala*`, `*_pre_*`) nu raspund la o intrebare de dupa ele
           cand exista o redare curenta; consolidatele au prioritate fata de actele modificatoare.
  R-VALAB  Un atom cu `valabil_din` DUPA data intrebarii nu e in vigoare la acea data -> exclus.
           Un atom fara data se foloseste, dar raspunsul declara "valabilitate nedovedita".
  R-PRAG   Daca cel mai bun atom nu atinge un scor minim de potrivire -> NU POT: corpusul nu conţine
           un atom care sa raspunda.
  R-CALC   Un CALCUL se face numai cand intrebarea are O SINGURA baza monetara si atomul da O SINGURA
           cota; altfel NU POT - motorul nu compune reguli, si o compunere ghicita e mai rea decat o
           abţinere.
"""
import csv
import json
import math
import os
import re
import time
from collections import Counter, defaultdict

from fiscalos import potrivire, surse

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = "/home/costin/ghid_incoming/FiscalOS_intrebari_test_50.csv"
COLOANE_PERMISE = ("id", "tip", "intrebare")
PRAG_SCOR = 6.0            # R-PRAG: sub acest scor BM25, cel mai bun atom nu raspunde

_STOP = {"care", "este", "sunt", "pentru", "prin", "din", "dintre", "catre", "unui", "unei", "sau",
         "daca", "cand", "pana", "cat", "cate", "cati", "ce", "cum", "cine", "unde", "firma", "firme",
         "societate", "societatea", "srl", "anul", "luna", "lunii", "face", "facut", "are", "avea",
         "poate", "trebuie", "aplica", "aplicabil", "aplicabila", "lei", "euro", "fara", "doar",
         "acest", "aceasta", "acesta", "acea", "acel", "dupa", "inainte", "intre", "asupra"}
_LUNI = {"ianuarie": 1, "februarie": 2, "martie": 3, "aprilie": 4, "mai": 5, "iunie": 6,
         "iulie": 7, "august": 8, "septembrie": 9, "octombrie": 10, "noiembrie": 11,
         "decembrie": 12}


# ── incarcarea, ORBA ─────────────────────────────────────────────────────────────────────────────
def incarca_intrebari(cale=CSV):
    """Numai `COLOANE_PERMISE`. Restul coloanelor nu se citesc in dict - nu doar nu se folosesc."""
    ies = []
    with open(cale, encoding="utf-8") as f:
        for rand in csv.DictReader(f):
            ies.append({k: rand[k] for k in COLOANE_PERMISE})
    return ies


# ── data de referinta ────────────────────────────────────────────────────────────────────────────
def data_referinta(text):
    """(data_iso, precizie, fragment). Precizie: 'zi' | 'luna' | 'an' | None."""
    t = potrivire.norm(text)
    m = re.search(r"\b(\d{1,2})\.(\d{1,2})\.(20\d\d)\b", t)
    if m:
        return "%s-%02d-%02d" % (m.group(3), int(m.group(2)), int(m.group(1))), "zi", m.group(0)
    m = re.search(r"\b(\d{1,2})\s+(%s)\s+(20\d\d)\b" % "|".join(_LUNI), t)
    if m:
        return ("%s-%02d-%02d" % (m.group(3), _LUNI[m.group(2)], int(m.group(1))), "zi",
                m.group(0))
    m = re.search(r"\b(%s)\s+(20\d\d)\b" % "|".join(_LUNI), t)
    if m:
        return "%s-%02d-01" % (m.group(2), _LUNI[m.group(1)]), "luna", m.group(0)
    m = re.search(r"\b(20\d\d)\b", t)
    if m:
        return "%s-01-01" % m.group(1), "an", m.group(0)
    return None, None, None


# ── indexul BM25 peste atomii din acte normative ─────────────────────────────────────────────────
def _stemuri(text):
    t = re.sub(r"[^a-z\s]", " ", potrivire.norm(text))
    return [potrivire._stem(w) for w in t.split() if len(w) >= 3 and w not in _STOP]


def _e_istoric(act):
    return "forma_initiala" in act or "_pre_" in act


class Index(object):
    def __init__(self, corp=None):
        self.corp = corp or potrivire.Corpus()
        self.normativ = {}
        for act in self.corp.pe_act:
            self.normativ[act] = surse.e_act_normativ(act)[0]
        self.atomi = [a for a in self.corp.toti
                      if self.normativ.get(a["act"]) and not a["abrogat"] and len(a["text"]) >= 30]
        self.tf = []
        df = Counter()
        self.lung = []
        for a in self.atomi:
            st = Counter(_stemuri(a["text"]))
            self.tf.append(st)
            self.lung.append(sum(st.values()))
            df.update(st.keys())
        self.N = len(self.atomi)
        self.avg = sum(self.lung) / float(self.N)
        self.idf = {w: math.log(1 + (self.N - n + 0.5) / (n + 0.5)) for w, n in df.items()}
        self.inv = defaultdict(list)
        for i, st in enumerate(self.tf):
            for w in st:
                self.inv[w].append(i)
        acte = set(self.corp.pe_act)
        # R-VERS: o redare istorica are o redare curenta daca exista un act cu acelasi numar/an
        self.are_curent = {}
        for act in acte:
            if _e_istoric(act):
                m = re.search(r"(\d+)_(\d{4})", act)
                self.are_curent[act] = bool(m and any(
                    x != act and not _e_istoric(x) and "%s_%s" % m.groups() in x for x in acte))

    def cauta(self, intrebare, data_ref, k=10, k1=1.2, b=0.75):
        q = Counter(_stemuri(intrebare))
        scor = defaultdict(float)
        for w in q:
            idf = self.idf.get(w)
            if not idf:
                continue
            for i in self.inv[w]:
                f = self.tf[i][w]
                scor[i] += idf * f * (k1 + 1) / (f + k1 * (1 - b + b * self.lung[i] / self.avg))
        ies = []
        for i, s in scor.items():
            a = self.atomi[i]
            if data_ref and a.get("valabil_din") and a["valabil_din"] > data_ref:
                continue                                  # R-VALAB
            if _e_istoric(a["act"]) and self.are_curent.get(a["act"]):
                s *= 0.2                                  # R-VERS
            elif "consolidat" in a["act"]:
                s *= 1.15                                 # R-VERS: consolidatul inaintea modificatorului
            ies.append((s, a))
        ies.sort(key=lambda t: -t[0])
        return ies[:k]


# ── temeiul, citit de om ─────────────────────────────────────────────────────────────────────────
_ACTE_NUMITE = {
    "cod_fiscal_227_2015_consolidat": "Codul fiscal (Legea 227/2015)",
    "legea_207_2015_consolidat": "Codul de procedură fiscală (Legea 207/2015)",
    "legea_53_2003_codul_muncii": "Codul muncii (Legea 53/2003)",
    "hg_1_2016_norme_cod_fiscal": "Normele metodologice ale Codului fiscal (HG 1/2016)",
}
_TIP_ACT = {"legea": "Legea", "lege": "Legea", "oug": "OUG", "og": "OG", "hg": "HG", "omfp": "OMFP",
            "omf": "OMF", "opanaf": "OPANAF", "ordin": "Ordinul", "oms": "OMS"}


def temei_uman(a):
    act = a["act"]
    nume = _ACTE_NUMITE.get(act)
    if not nume:
        m = re.match(r"([a-z]+)_?(\d+)_(\d{4})", act)
        nume = ("%s %s/%s" % (_TIP_ACT.get(m.group(1), m.group(1).upper()), m.group(2), m.group(3))
                if m else act)
    parti = []
    for seg in a["id"].split("#", 1)[1].split("/"):
        seg = seg.split("~")[0]
        for pref, et in (("art", "art. "), ("alin", "alin. ("), ("lit", "lit. "), ("pct", "pct. ")):
            if seg.startswith(pref) and seg[len(pref):] not in ("-", "None"):
                v = seg[len(pref):]
                parti.append(et + v + (")" if pref == "alin" else ")" if pref == "lit" else ""))
                break
    return "%s %s" % (nume, " ".join(parti))


# ── extragerea valorilor ─────────────────────────────────────────────────────────────────────────
_FORMA_INTREBATA = [
    ("procent", re.compile(r"\bcot[aăe]|\bprocent|\bnivelurile dobanzii|\bdobanz|\bpenalit", re.I)),
    ("suma", re.compile(r"\bplafon|\bvaloare[a]? (fiscala )?minima|\bprag|\bsuma\b", re.I)),
    ("termen", re.compile(r"\bin ce termen\b|\bpana cand\b|\btermen", re.I)),
]
_NR_PROCENT = re.compile(r"(\d{1,3}(?:,\d{1,3})?)\s*%")
_NR_SUMA = re.compile(r"(\d{1,3}(?:\.\d{3})+|\d{3,})\s*(?:de\s+)?(lei|euro)")
_NR_TERMEN = re.compile(r"(\d{1,3})\s+(zile|de zile|luni|de luni|ani|de ani)|data de (\d{1,2}) inclusiv")
_BANI = re.compile(r"(\d{1,3}(?:\.\d{3})+|\d+)(?:,\d+)?\s*lei")


def _forma(intrebare):
    t = potrivire.norm(intrebare)
    for fel, rx in _FORMA_INTREBATA:
        if rx.search(t):
            return fel
    return None


def _valori(text_norm, fel):
    if fel == "procent":
        return [m.group(1) + "%" for m in _NR_PROCENT.finditer(text_norm)]
    if fel == "suma":
        return ["%s %s" % (m.group(1), m.group(2)) for m in _NR_SUMA.finditer(text_norm)]
    if fel == "termen":
        return [(m.group(3) + " inclusiv") if m.group(3) else "%s %s" % (m.group(1), m.group(2))
                for m in _NR_TERMEN.finditer(text_norm)]
    return []


def _valabilitate(a, data_ref):
    d = a.get("valabil_din") or potrivire._data_din_text(a["_n"])
    if not d:
        return {"valabil_din": None, "la_data_intrebarii": None,
                "nota": "valabilitate nedovedita: atomul nu poarta data de intrare in vigoare"}
    return {"valabil_din": d, "la_data_intrebarii": (d <= data_ref) if data_ref else None}


def _argument(a, scor, data_ref, forma=None):
    return {"atom": a["id"], "temei": temei_uman(a), "act": a["act"], "scor": round(scor, 2),
            "verbatim": potrivire._fereastra_verbatim(a["text"], forma),
            "valabilitate": _valabilitate(a, data_ref)}


def _nu_pot(q, motiv, **extra):
    r = {"id": q["id"], "tip": q["tip"], "intrebare": q["intrebare"], "stare": "NU_POT_RASPUNDE",
         "raspuns": None, "argument": [], "motiv": motiv}
    r.update(extra)
    return r


def _fraza_cheie(text, stemuri_q):
    """Propozitia din atom care poarta cele mai multe stemuri ale intrebarii - rezumatul raspunsului."""
    fraze = [f.strip() for f in re.split(r"(?<=[.;])\s+", text) if len(f.strip()) > 20]
    if not fraze:
        return text[:300]
    return max(fraze, key=lambda f: sum(1 for s in stemuri_q if s in potrivire.norm(f)))


# ── raspunsul ────────────────────────────────────────────────────────────────────────────────────
def raspunde(q, idx):
    data_ref, precizie, frag_data = data_referinta(q["intrebare"])
    baza = {"data_referinta": data_ref, "precizie_data": precizie, "data_din": frag_data}
    if not data_ref:
        return _nu_pot(q, "R-DATA: intrebarea nu spune cand. Valorile fiscale se schimba in timp, "
                          "iar raspunsul trebuie sa fie valabil la data intrebarii - fara ea, "
                          "valabilitatea nu se poate stabili.", **baza)

    hit = idx.cauta(q["intrebare"], data_ref)
    if not hit or hit[0][0] < PRAG_SCOR:
        return _nu_pot(q, "R-PRAG: niciun atom dintr-un act normativ nu atinge scorul minim de "
                          "potrivire (%.1f; cel mai bun: %.1f)"
                          % (PRAG_SCOR, hit[0][0] if hit else 0), **baza)

    stemuri_q = set(_stemuri(q["intrebare"]))
    fel = _forma(q["intrebare"])

    if q["tip"] == "CALCUL":
        return _calcul(q, hit, data_ref, baza, stemuri_q)

    # PARAMETRU (si orice intrebare care cere o valoare): primul atom care poarta o valoare de
    # forma cerută, printre primii 5
    if q["tip"] == "PARAMETRU" and fel:
        for s, a in hit[:5]:
            vals = _valori(a["_n"], fel)
            if vals:
                v = vals[0]
                r = {"id": q["id"], "tip": q["tip"], "intrebare": q["intrebare"],
                     "stare": "RASPUNS", "raspuns": v,
                     "argument": [_argument(a, s, data_ref, v.split()[0].replace("%", ""))],
                     "motiv": "valoarea de forma cerută (%s) din atomul cel mai bine potrivit care "
                              "o poarta" % fel, "valori_in_atom": vals[:6]}
                r.update(baza)
                return r
        return _nu_pot(q, "niciunul din primii 5 atomi nu poarta o valoare de forma cerută (%s)"
                          % fel, candidati=[_argument(a, s, data_ref) for s, a in hit[:3]], **baza)

    # REGULA / PROCEDURA / CAPCANA / INCOMPLETA cu data: raspuns EXTRACTIV - regula din atom
    s, a = hit[0]
    fraza = _fraza_cheie(a["text"], stemuri_q)
    r = {"id": q["id"], "tip": q["tip"], "intrebare": q["intrebare"], "stare": "RASPUNS",
         "raspuns": fraza,
         "argument": [_argument(a, s, data_ref)] + [_argument(b, t, data_ref) for t, b in hit[1:3]],
         "motiv": "raspuns extractiv: fraza din atomul cel mai bine potrivit care poarta cele mai "
                  "multe cuvinte ale intrebarii. Motorul nu compune reguli.",
         "valori_in_atom": (_valori(a["_n"], "termen") + _valori(a["_n"], "procent")
                            + _valori(a["_n"], "suma"))[:8]}
    r.update(baza)
    return r


def _calcul(q, hit, data_ref, baza, stemuri_q):
    """R-CALC: o singura baza monetara in intrebare, o singura cota in atom -> baza x cota."""
    baze = [m.group(1) for m in _BANI.finditer(potrivire.norm(q["intrebare"]))]
    if len(baze) != 1:
        return _nu_pot(q, "R-CALC: intrebarea are %d baze monetare; calculul cere compunerea mai "
                          "multor reguli, pe care motorul nu o face" % len(baze),
                       candidati=[_argument(a, s, data_ref) for s, a in hit[:3]], **baza)
    for s, a in hit[:5]:
        cote = sorted(set(_valori(a["_n"], "procent")))
        if len(cote) == 1:
            b = float(baze[0].replace(".", ""))
            c = float(cote[0].rstrip("%").replace(",", "."))
            rez = round(b * c / 100.0, 2)
            r = {"id": q["id"], "tip": q["tip"], "intrebare": q["intrebare"], "stare": "RASPUNS",
                 "raspuns": "%s lei x %s = %s lei" % (baze[0], cote[0], ("%.2f" % rez).replace(".", ",")),
                 "argument": [_argument(a, s, data_ref, cote[0].rstrip("%"))],
                 "motiv": "R-CALC: o baza, o cota; baza x cota", "calcul": {"baza": b, "cota": c,
                                                                          "rezultat": rez}}
            r.update(baza)
            return r
    return _nu_pot(q, "R-CALC: niciun atom din primii 5 nu da O SINGURA cota", 
                   candidati=[_argument(a, s, data_ref) for s, a in hit[:3]], **baza)


def ruleaza(dest=None):
    t0 = time.time()
    idx = Index()
    t_idx = time.time() - t0
    qs = incarca_intrebari()
    ies = [raspunde(q, idx) for q in qs]
    # NICIODATA raspuns fara atom: verificat aici, nu doar in teste
    for r in ies:
        if r["stare"] == "RASPUNS":
            assert r["argument"] and r["argument"][0]["atom"], r["id"]
    dest = dest or os.path.join(_RAD, "artefacte", "intrebari")
    os.makedirs(dest, exist_ok=True)
    rez = {"_ce": "C6 raspunsurile motorului, scrise INAINTE de comparatia cu cheia.",
           "generat_la": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "n": len(ies), "raspunse": sum(1 for r in ies if r["stare"] == "RASPUNS"),
           "nu_pot": sum(1 for r in ies if r["stare"] == "NU_POT_RASPUNDE"),
           "n_atomi_indexati": idx.N, "secunde_index": round(t_idx, 2),
           "secunde_total": round(time.time() - t0, 2), "raspunsuri": ies}
    with open(os.path.join(dest, "raspunsuri.json"), "w", encoding="utf-8") as f:
        json.dump(rez, f, ensure_ascii=False, indent=1)
    return rez


if __name__ == "__main__":
    r = ruleaza()
    print("intrebari: %d | raspunse %d | nu pot %d | index %d atomi (%.1f s) | total %.1f s"
          % (r["n"], r["raspunse"], r["nu_pot"], r["n_atomi_indexati"], r["secunde_index"],
             r["secunde_total"]))
