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
import datetime
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
# Data la care se pun intrebarile - ziua rularii motorului. O intrebare "in 2026" pusa azi intreaba de
# regula in vigoare azi, nu de cea din 1 ianuarie.
DATA_INTREBARII = "2026-09-28"

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
    # D12: o LUNA nu e prima ei zi, un AN nu e 1 ianuarie. Masurat: "anul fiscal 2026" devenea
    # 2026-01-01, iar R-VALAB excludea tot ce a intrat in vigoare mai tarziu in 2026 - inclusiv pragul
    # de 5.000 lei pentru mijloacele fixe (CF art.28 alin.(2) lit.b), in vigoare din 25.02.2026).
    # Luna -> ultima ei zi (obligatiile se calculeaza pe luna intreaga). An -> sfarsitul anului, dar nu
    # mai tarziu de ziua in care se pune intrebarea.
    m = re.search(r"\b(%s)\s+(20\d\d)\b" % "|".join(_LUNI), t)
    if m:
        an, luna = int(m.group(2)), _LUNI[m.group(1)]
        ultima = (datetime.date(an + (luna == 12), luna % 12 + 1, 1) - datetime.timedelta(days=1))
        return ultima.isoformat(), "luna", m.group(0)
    m = re.search(r"\b(20\d\d)\b", t)
    if m:
        return min("%s-12-31" % m.group(1), DATA_INTREBARII), "an", m.group(0)
    return None, None, None


# ── indexul BM25 peste atomii din acte normative ─────────────────────────────────────────────────
def _stemuri(text):
    t = re.sub(r"[^a-z\s]", " ", potrivire.norm(text))
    return [potrivire._stem(w) for w in t.split() if len(w) >= 3 and w not in _STOP]


_INTERVENTIE = re.compile(r"#art[IVXLCDM]+(?:~\d+)?/(?:alin[^/]*/)*pct\d+")


def _e_interventie(atom_id):
    """Atomul face parte dintr-o INSTRUCTIUNE DE MODIFICARE: articol roman -> punct ("42. La articolul
    291, alineatele (1) si (2) se modifica si vor avea urmatorul cuprins: ...").

    D3: asemenea puncte raspundeau la intrebari din 2026 cu text de modificare vechi - OUG 50/2015
    pentru cota micro, OUG 115/2023 pentru orele suplimentare. Textul lor e fie deja in consolidat,
    fie inlocuit de o modificare ulterioara; in ambele cazuri nu e legea in vigoare. O prevedere DE
    SINE STATATOARE a unui act modificator (OUG 89/2025 art. III alin. (4), facilitatea pentru salariul
    minim) nu trece printr-un punct si nu e atinsa.
    """
    return bool(_INTERVENTIE.search(atom_id))


# D9: intrebarile vorbesc in abrevieri, actele in forma lunga. Codul fiscal spune "taxa", nu "TVA";
# "contributia asiguratorie pentru munca", nu "CAM". Tabelul e VOCABULARUL DOMENIULUI - abrevierile
# standard ale fiscalitaţii romanesti si denumirile oficiale ale declaraţiilor -, nu raspunsuri: nu
# conţine nicio cifra, niciun articol, nicio valoare. Fara el, intrebarea "cota standard de TVA" nu se
# potrivea cu CF art. 291, care nu conţine cuvantul "TVA".
_ABREVIERI = {
    "tva": "taxa pe valoarea adaugata taxa",
    "cas": "contributia de asigurari sociale",
    "cass": "contributia de asigurari sociale de sanatate",
    "cam": "contributia asiguratorie pentru munca",
    "pfa": "persoana fizica autorizata",
    "anaf": "organul fiscal central",
    "cim": "contract individual de munca",
    "aga": "adunarea generala a asociatilor",
    "imca": "impozit minim pe cifra de afaceri",
    "micro": "microintreprinderi",
    # Codurile de FORMULAR (D100, D300...) NU se extind. Masurat: cu ele, D9 a regresat 5 -> 4 -
    # "D100" devenea "declaratie privind obligatiile de plata la bugetul de stat" si tragea intrebarea
    # despre cota micro spre atomii FORMULARULUI, departe de CF art. 51. O intrebare care numeste un
    # formular intreaba de regula de fond raportata in el, nu de formular.
}


def _extinde(text):
    t = potrivire.norm(text)
    ext = [_ABREVIERI[w] for w in re.findall(r"[a-z0-9]+", t) if w in _ABREVIERI]
    return t + " " + " ".join(ext)


_ACT_DE_FORMULAR = re.compile(r"(?:^|_)d\d{3}(?:_|$)|formular|anexa_\d+_instructiuni", re.I)
_INTREABA_DE_FORMULAR = re.compile(r"\bd\d{3}\b|declarati|formular|decont", re.I)


def _e_act_de_formular(act):
    """Ordin care aproba un FORMULAR si instructiunile lui de completare (`opanaf_605_2026_d112`,
    `opanaf_3769_2015_d394_baza`). E act normativ - dar conţinutul lui descrie ce se trece in fiecare
    rubrica, deci pomeneste aproape orice concept fiscal, si castiga cautarea lexicala la intrebari de
    fond. D7: la "cota standard de TVA" primele doua raspunsuri erau "Coloana Taxă pe valoarea
    adăugată ... se înscriu"; la concediul medical, instrucţiunile D112 inaintea OUG 158/2005."""
    return bool(_ACT_DE_FORMULAR.search(act))


# D14: IERARHIA ACTELOR NORMATIVE. Legea (si codul, OUG-ul, OG-ul) prevaleaza asupra hotararii de
# aplicare si a ordinului: o norma de aplicare nu poate contrazice legea, iar cand cele doua spun
# valori diferite, norma e de regula depasita. Masurat: la "cota standard de TVA", normele Codului
# fiscal (HG 1/2016) scriu inca "cota standard de 20%" - textul din 2016 - si castigau alegerea intre
# candidaţi in fata CF art. 291 alin. (1). Factorul se aplica NUMAI la alegerea intre atomi care poarta
# deja o valoare de forma cerută, nu la cautare.
_RANG_ACT = [(re.compile(r"^(cod_|cf_|legea_|lege_|oug_|og_)"), 1.0),
             (re.compile(r"^hg"), 0.6),
             (re.compile(r"^(omfp|omf|oms|opanaf|ordin)"), 0.6)]


def _rang_act(act):
    nume = os.path.basename(act).lower()
    for rx, f in _RANG_ACT:
        if rx.match(nume):
            return f
    return 0.6


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
        # D10: DENUMIREA MARGINALA a articolului, ca context pentru alineatele lui. Titlul e scurt si
        # foarte discriminant, iar alineatul nu il repeta: CF art. 310 ("Regimul special de scutire
        # pentru intreprinderile mici") si art. 310^1 (regimul transfrontalier) au alineate aproape
        # identice lexical; CPF art. 183 e despre majorarile datorate BUGETELOR LOCALE, dar alineatul
        # lui spune doar "Nivelul majorarii de intarziere este de 1%". Titlul se ia din atomul-articol
        # stramos, cand textul lui e scurt (<= 250 de caractere): unul lung e corp, nu titlu.
        titlu = {}
        for act, ats in self.corp.pe_act.items():
            for a in ats:
                if a["nivel"] == "articol" and len(a["text"]) <= 250:
                    titlu[a["id"]] = set(_stemuri(a["text"]))
        self.titlu = []
        for a in self.atomi:
            art_id = a["id"].split("/")[0]
            self.titlu.append(titlu.get(art_id, set()) if art_id != a["id"] else set())
        self.inv_titlu = defaultdict(list)
        for i, t in enumerate(self.titlu):
            for w in t:
                self.inv_titlu[w].append(i)
        acte = set(self.corp.pe_act)
        # D3b: un act ale carui articole PROPRII sunt romane e un act modificator; in redarea lui
        # consolidata, un articol ARAB e textul CITAT al actului modificat, ca instantaneu din ziua
        # modificarii. Masurat: `og_16_2022_consolidat#art52/alin1` (Codul fiscal asa cum era in 2022)
        # raspundea la cota micro din 2026.
        self.modificator = {}
        for act, ats in self.corp.pe_act.items():
            arts = [a for a in ats if a["nivel"] == "articol" and a.get("parinte") is None]
            rom = sum(1 for a in arts if re.match(r"^[IVXLCDM]+$", str(a["cheie"])))
            self.modificator[act] = bool(arts) and rom >= 0.5 * len(arts)
        # R-VERS: o redare istorica are o redare curenta daca exista un act cu acelasi numar/an
        self.are_curent = {}
        for act in acte:
            if _e_istoric(act):
                m = re.search(r"(\d+)_(\d{4})", act)
                self.are_curent[act] = bool(m and any(
                    x != act and not _e_istoric(x) and "%s_%s" % m.groups() in x for x in acte))

    def copii(self, a, data_ref=None):
        """Descendentii unui atom (litere, puncte), in ordinea din act - cu ACELEASI filtre ca `cauta`.

        Prima versiune (D13) ii lua direct din act si ocolea R-VALAB: un copil intrat in vigoare DUPA
        data intrebarii ar fi putut raspunde. Coborarea in ierarhie nu are voie sa scape de regulile
        de vigoare pe care le respecta cautarea."""
        pref = a["id"] + "/"
        return [x for x in self.corp.pe_act[a["act"]]
                if x["id"].startswith(pref) and not x["abrogat"]
                and not (data_ref and x.get("valabil_din") and x["valabil_din"] > data_ref)]

    def cauta(self, intrebare, data_ref, k=10, k1=1.2, b=0.75):
        q = Counter(_stemuri(_extinde(intrebare)))              # D9
        despre_formular = bool(_INTREABA_DE_FORMULAR.search(potrivire.norm(intrebare)))
        scor = defaultdict(float)
        for w in q:
            idf = self.idf.get(w)
            if not idf:
                continue
            for i in self.inv[w]:
                f = self.tf[i][w]
                scor[i] += idf * f * (k1 + 1) / (f + k1 * (1 - b + b * self.lung[i] / self.avg))
        # D10: fiecare stem al intrebarii prezent in TITLUL articolului adauga idf-ul lui
        for w in q:
            idf = self.idf.get(w)
            if not idf:
                continue
            for i in self.inv_titlu.get(w, ()):
                scor[i] += idf
        ies = []
        for i, s in scor.items():
            a = self.atomi[i]
            if data_ref and a.get("valabil_din") and a["valabil_din"] > data_ref:
                continue                                  # R-VALAB
            if _e_istoric(a["act"]):
                # D4: penalizarea NU mai depinde de gasirea perechii curente. Legatura se facea pe
                # "numar_an" din nume, iar `cf_2015_forma_initiala` n-are numar de act - deci Codul
                # fiscal din 2015 nu era recunoscut ca istoric si raspundea la intrebari din 2026
                # (CAM "26,3%", adica cotele CAS din 2015). O redare istorica e istorica prin nume.
                s *= 0.2                                  # R-VERS
            elif "consolidat" in a["act"]:
                s *= 1.15                                 # R-VERS: consolidatul inaintea modificatorului
            if _e_interventie(a["id"]):
                s *= 0.3                                  # D3: instructiune de modificare
            elif self.modificator.get(a["act"]) and a.get("articol") and \
                    str(a["articol"])[:1].isdigit():
                s *= 0.3                                  # D3b: text citat intr-un act modificator
            if _e_act_de_formular(a["act"]) and not despre_formular:
                s *= 0.3                                  # D7: instructiuni de formular, intrebare de fond
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


# D15 (certitudine): o intrebare fara cuvant interogativ cere o JUDECATA (Da/Nu): "A depasit
# plafonul?", "Se recalculeaza impozitul la 16%?". Motorul nu compune reguli si nu aplica o regula la
# fapte, deci nu poate judeca - poate doar arata regula. Un fragment extras pus in locul unui "Da" sau
# "Nu" e un pseudo-raspuns; in v0 asemenea extrase au produs cele mai multe GRESIT.
_INTEROGATIV = re.compile(r"\b(care|ce|cat|cata|cati|cate|catre|cand|cum|cine|unde|in ce|pana cand|"
                          r"de cand|din ce|pe ce|la ce|cu ce)\b")


def _cere_judecata(intrebare):
    return not _INTEROGATIV.search(potrivire.norm(intrebare))


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
    v = {"valabil_din": d, "la_data_intrebarii": (d <= data_ref) if data_ref else None}
    if data_ref and d[:4] == data_ref[:4] and d[5:] != "01-01" and d <= data_ref:
        v["nota"] = ("forma aceasta e in vigoare din %s, adica s-a schimbat IN CURSUL anului %s: "
                     "inainte de acea data se aplica o alta forma" % (d, d[:4]))
    return v


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
    if not data_ref:
        # D5: o intrebare fara data intreaba de regula in vigoare in ziua in care e pusa. R-DATA o
        # refuza, ceea ce era gresit de doua ori: a refuzat intrebari la care se poate raspunde (termenul
        # de contestatie), si a "castigat" doua intrebari INCOMPLETA din motivul GRESIT - le lipseau
        # fapte (folosinta masinii, marimea firmei), nu data. Acum data implicita e declarata ca atare.
        data_ref, precizie, frag_data = DATA_INTREBARII, "implicita (ziua intrebarii)", None
    baza = {"data_referinta": data_ref, "precizie_data": precizie, "data_din": frag_data,
            # DECIZIA C5: fiecare raspuns incepe prin a declara data si perimetrul presupus. Motorul
            # lexical NU citeste perimetrul din intrebare - il declara pe cel implicit, ca atare.
            "declaratie": ("Data de referinta: %s (%s%s). Perimetru presupus: persoana juridica "
                           "romana in regim general, fara situatii speciale nementionate in "
                           "intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare."
                           % (data_ref, precizie, (", din \"%s\"" % frag_data) if frag_data else ""))}

    hit = idx.cauta(q["intrebare"], data_ref)
    if not hit or hit[0][0] < PRAG_SCOR:
        return _nu_pot(q, "R-PRAG: niciun atom dintr-un act normativ nu atinge scorul minim de "
                          "potrivire (%.1f; cel mai bun: %.1f)"
                          % (PRAG_SCOR, hit[0][0] if hit else 0), **baza)

    stemuri_q = set(_stemuri(q["intrebare"]))
    # scorul local (D1) foloseste ACEEASI extindere de vocabular ca si cautarea (D9); altfel "TVA" din
    # intrebare nu se potriveste cu "taxa" din Cod exact in pasul care alege intre candidati
    stemuri_ext = set(_stemuri(_extinde(q["intrebare"])))
    fel = _forma(q["intrebare"])

    if q["tip"] == "CALCUL":
        return _calcul(q, hit, data_ref, baza, stemuri_q)

    # PARAMETRU (si orice intrebare care cere o valoare): primul atom care poarta o valoare de
    # forma cerută, printre primii 5
    if q["tip"] == "PARAMETRU" and fel:
        # D1: dintre atomii care POARTA o valoare de forma cerută - primii 5 si copiii lor (D13) -
        # castiga cel al carui TEXT PROPRIU potriveste cel mai bine cuvintele RARE ale intrebarii, nu
        # primul in ordinea cautarii. Masurat: titlul "Cotele" (D10) a adus CF art. 291 in fata, dar
        # a ridicat toate alineatele lui la fel, iar extractorul lua primul cu o valoare - alin. (3^5)
        # lit. d), 9% -, in loc de alin. (1), singurul care spune "cota STANDARD". Scorul local e
        # suma idf-urilor stemurilor intrebarii prezente in textul atomului, fara titlu.
        cand = []
        for s0, a0 in hit[:5]:
            for a in [a0] + idx.copii(a0, data_ref):
                if _valori(a["_n"], fel):
                    local = sum(idx.idf.get(st, 0) for st in stemuri_ext if st in a["_n"])
                    cand.append((local * _rang_act(a["act"]), s0, a))       # D14
        if cand:
            cand.sort(key=lambda t: (-t[0], -t[1]))
            local, s, a = cand[0]
            vals = _valori(a["_n"], fel)
            v = vals[0]
            r = {"id": q["id"], "tip": q["tip"], "intrebare": q["intrebare"],
                 "stare": "RASPUNS", "raspuns": v,
                 "argument": [_argument(a, s, data_ref, v.split()[0].replace("%", ""))],
                 "motiv": "valoarea de forma cerută (%s) din atomul care poarta o asemenea valoare "
                          "si potriveste cel mai bine cuvintele rare ale intrebarii (scor local %.1f)"
                          % (fel, local), "valori_in_atom": vals[:6]}
            r.update(baza)
            return r
        return _nu_pot(q, "niciunul din primii 5 atomi nu poarta o valoare de forma cerută (%s)"
                          % fel, candidati=[_argument(a, s, data_ref) for s, a in hit[:3]], **baza)

    # D15a: o judecata (Da/Nu) nu se poate da - se arata regula, ca material, si se spune
    if _cere_judecata(q["intrebare"]):
        return _nu_pot(q, "D15: intrebarea cere o JUDECATA (Da/Nu) - aplicarea unei reguli la faptele "
                          "date. Motorul nu compune si nu aplica reguli; atasez regula cea mai bine "
                          "potrivita, ca material, nu ca raspuns.",
                       candidati=[_argument(a, s, data_ref) for s, a in hit[:3]], **baza)

    # D15b: intrebarea cere un fapt de o forma anume -> raspunsul trebuie sa-l conţina
    if fel:
        cand = []
        for s0, a0 in hit[:5]:
            for a in [a0] + idx.copii(a0, data_ref):
                for fraza in re.split(r"(?<=[.;])\s+", a["text"]):
                    fn = potrivire.norm(fraza)
                    if len(fraza) > 20 and _valori(fn, fel):
                        local = sum(idx.idf.get(st, 0) for st in stemuri_ext if st in fn)
                        cand.append((local * _rang_act(a["act"]), s0, a, fraza.strip()))
        if not cand:
            return _nu_pot(q, "D15: intrebarea cere un fapt de forma '%s', si niciun atom gasit (nici "
                              "copiii lor) nu conţine unul" % fel,
                           candidati=[_argument(a, s, data_ref) for s, a in hit[:3]], **baza)
        cand.sort(key=lambda t: (-t[0], -t[1]))
        local, s, a, fraza = cand[0]
        r = {"id": q["id"], "tip": q["tip"], "intrebare": q["intrebare"], "stare": "RASPUNS",
             "raspuns": fraza,
             "argument": [_argument(a, s, data_ref, _valori(potrivire.norm(fraza), fel)[0].split()[0]
                                    .replace("%", ""))],
             "motiv": "D15: fraza care conţine un fapt de forma cerută (%s) si potriveste cel mai "
                      "bine intrebarea (scor local %.1f)" % (fel, local),
             "valori_in_atom": _valori(potrivire.norm(fraza), fel)[:6]}
        r.update(baza)
        return r

    # D15c: fara forma recunoscuta si fara judecata. Intrebarea tot cere un fapt anume ("Cat poate
    # plati in numerar?", "Pe ce cont se corecteaza?", "Din ce luna incepe amortizarea?"), dar motorul
    # nu recunoaste FORMA acelui fapt - deci nu poate verifica ca fraza extrasa raspunde la ce s-a
    # intrebat. E acelasi principiu ca la D15b, dus la capat. Masurat inainte de regula: toate cele 9
    # raspunsuri de pe acest drum ieseau GRESIT. Regula aplicabila se ataseaza ca material.
    return _nu_pot(q, "D15: intrebarea cere un fapt a carui forma motorul nu o recunoaste; nu pot "
                      "verifica ca un fragment extras raspunde la ce s-a intrebat. Atasez regula cea "
                      "mai bine potrivita, ca material, nu ca raspuns.",
                   candidati=[_argument(a, s, data_ref) for s, a in hit[:3]], **baza)


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
