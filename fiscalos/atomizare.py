# -*- coding: utf-8 -*-
"""OP4 — ATOMIZARE STRUCTURALA: act -> articol -> alineat -> litera/punct.

CE SE ATOMIZEAZA AUTOMAT si ce nu. Principiul proiectului: *structura* intregului act se atomizeaza
automat, *continutul* treptat, la cerere. Aici se face structura - fiecare atom primeste id stabil,
text verbatim si valabilitate. Nimeni nu citeste cei ~100.000 de atomi; ei exista ca sa poata fi
citat EXACT atomul care stabileste o valoare, cand se cere.

ID STABIL, si de ce ASA:
    <act>#art<N>                  articol            ex. cod_fiscal_227_2015_consolidat#art291
    <act>#art<N>/alin<M>          alineat            ex. ...#art291/alin1
    <act>#art<N>/alin<M>/lit<x>   litera
    <act>#art<N>/alin<M>/pct<k>   punct
    <act>#frag<N>                 fragment (act fara structura de articol - vezi mai jos)
`act` e radacina de nume din corpus (`cod_fiscal_227_2015_consolidat`), nu un slug inventat: el se
rezolva direct in `corpus_manifest.json`, deci un id citat duce la OCTETI, nu la o eticheta.
Numarul de articol e cel din text (inclusiv formele `18^1` si cele romane `II`), nu o pozitie
ordinala - pozitia se schimba la fiecare completare a legii, numarul nu.

PATRU FORMATE, fiindca asa e corpusul - MASURAT, nu presupus. Un singur marcaj de articol a dat 108
acte cu ZERO atomi, intre care Codul de procedura fiscala si Legea 141/2025 (cea care stabileste
cota de TVA de azi). Formele gasite:

  F1  portal legislativ  `Articolul 291` pe rand propriu, apoi `(1)` pe rand propriu
  F2  monitor/inline     `Art. I - (1) text...` - articolul si primul alineat pe ACELASI rand;
                         articolele modificatoare sunt romane (`Art. II`), iar punctele lor
                         (`42. La articolul 291...`) sunt unitatea citata de iConta ca "Art.II pct.42"
  F3  static.anaf.ro     `ART. 1 Definiții` - numar + TITLUL articolului pe acelasi rand
  F4  fara articole      pliante ANAF, structuri de formular, note. Atomul e FRAGMENTUL de paragraf.

F4 NU e un eșec deghizat in succes: actul isi declara `structura: "fragmente"`, si un parametru gasit
numai in fragmente se citeaza ca fragment. Ce nu se face e sa para ca actul are articole cand nu are.

CUPRINSUL nu e corp. Consolidatele pun intai un CUPRINS cu aceleasi marcaje de articol; fara
distingere, `#art291` ar fi randul din cuprins (gol), iar textul real ar cadea pe `#art291~2`.
Se recunoaste STRUCTURAL, nu pe poziție: cuprinsul e o serie lunga de marcaje consecutive FARA text
intre ele (>= _RUN_CUPRINS). In corp, fiecare marcaj e urmat de alineate. Regula nu depinde de unde
incepe actul, deci tine si pe actele care isi pun cuprinsul la mijloc (anexe).

VALABILITATE, si de ce e DERIVATA din text, nu presupusa. Consolidatele poarta, dupa fiecare unitate
modificata, o nota:

    (la 01-08-2025,
    Alineatul (1) , Articolul 291 , ... a fost modificat de Punctul 42. , Articolul II din LEGEA
    nr. 141 din 25 iulie 2025, publicată în MONITORUL OFICIAL nr. 699 din 25 iulie 2025
    )

De acolo iese `valabil_din` = 2025-08-01 si actul modificator. `valabil_pana` NU se scrie de mana: o
lege spune de CAND intra, nu pana cand. Cand acelasi atom are mai multe note, se ia data cea mai
recenta - ea e forma pe care textul o AFISEAZA. Un atom fara nota are `valabil_din = None`, si asta
se SCRIE, nu se ghiceste (CLAUDE.md §2).

ATOMI ABROGATI: textul "Abrogat." rămâne in consolidat, cu nota lui. Se marcheaza `abrogat=True` si
NU se sterge - un parametru cautat intr-un alineat abrogat trebuie sa gaseasca abrogarea, nu tacerea.
"""
import json
import os
import re
import time

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_RUN_CUPRINS = 6            # atatea marcaje consecutive fara text = cuprins, nu corp

# ── F1: "Articolul 291" / "Articolul 18^1" / "ART. 291." — numarul SINGUR pe rand ───────────────
_ART = re.compile(r"^\s*(?:Articolul|ARTICOLUL|Art\.|ART\.|Art|ART)\s*"
                  r"(\d+(?:\^\d+)?|[IVXLCDM]+)\s*\.?\s*$")
# ── F2: "Art. I - (1) text" / "Art. 1577 - Baza lunară..." — liniuta separa numarul de corp ─────
_ART_INLINE = re.compile(r"^\s*(?:Articolul|ARTICOLUL|Art\.|ART\.)\s*"
                         r"(\d+(?:\^\d+)?|[IVXLCDM]+)\s*[-–—]\s*(\S.*)$")
# ── F3: "ART. 1 Definiții" — numar + titlu scurt, fara punct final ──────────────────────────────
_ART_TITLU = re.compile(r"^\s*(?:ART|Art)\.?\s*(\d+(?:\^\d+)?)\s+(\S[^.]{0,118})$")
# Vocabularul notelor de modificare: "Articolul 502 , Titlul XI a fost completat de..." NU e titlu
# de articol. Si nici o referinta interna ("Art. 291 alin. (1) din Codul fiscal").
_NU_E_TITLU = re.compile(r"a fost (modificat|completat|abrogat|introdus|republicat)|"
                         r"^(alin|pct|lit|paragraf)|prevede|se aplică|se aplica", re.I)

_ALIN = re.compile(r"^\s*\((\d+(?:\^\d+)?)\)\s*(.*)$")
_LIT = re.compile(r"^\s*([a-z](?:\^\d+)?)\)\s*(.*)$")
_PCT = re.compile(r"^\s*(\d+(?:\^\d+)?)\.\s*(\S.*)$")
_NOTA_DIN = re.compile(r"^\s*\(la\s+(\d{2})-(\d{2})-(\d{4})\s*,?\s*(.*)$")
_ABROGAT = re.compile(r"^\s*Abrogat[ăa]?\.?\s*$", re.I)
_TITLU = re.compile(r"^\s*(Titlul|TITLUL|Capitolul|CAPITOLUL|Secțiunea|SECȚIUNEA|Sectiunea|"
                    r"SECTIUNEA|Subsecțiunea|Subsectiunea|Partea|PARTEA|Anexa|ANEXA)\s+"
                    r"([IVXLCDM0-9]+.*)$")
_ROMAN = re.compile(r"^[IVXLCDM]+$")


def _marcaj(linie):
    """(fel, numar, rest) pentru un rand care deschide o unitate; altfel (None, None, None).

    Ordinea conteaza: F1 (numar singur) inainte de F3 (numar + titlu), fiindca F3 ar accepta si un
    rand F1 urmat de spatii. Notele de modificare se exclud INAINTE de F3, nu dupa."""
    m = _ART.match(linie)
    if m:
        return "articol", m.group(1), ""
    m = _ART_INLINE.match(linie)
    if m:
        rest = m.group(2).strip()
        if not _NU_E_TITLU.match(rest):
            return "articol", m.group(1), rest
    m = _ART_TITLU.match(linie)
    if m:
        rest = m.group(2).strip()
        if not _NU_E_TITLU.search(rest) and len(rest) <= 120:
            return "articol", m.group(1), rest
    if _TITLU.match(linie) and len(linie) < 200:
        return "titlu", None, linie.strip()
    return None, None, None


def _randuri_de_cuprins(randuri):
    """Indicii randurilor care fac parte din CUPRINS (serie lunga de marcaje fara text intre ele).

    Se intoarce un set, nu se taie textul: atomizarea are nevoie de numerotarea originala de randuri
    pentru `linie`, care e urma spre fisierul de text."""
    fel_pe_rand = []
    fel_articol = {}
    for i, r in enumerate(randuri):
        s = r.strip()
        if not s:
            fel_pe_rand.append(("gol", i))
            continue
        fel, _n, rest = _marcaj(s)
        # un marcaj cu corp (F2 `Art. I - (1)...`) e deja CORP, nu cuprins
        if fel == "articol" and rest and not rest.startswith("("):
            fel_pe_rand.append(("marcaj", i))
            fel_articol[i] = True
        elif fel == "articol" and not rest:
            fel_pe_rand.append(("marcaj", i))
            fel_articol[i] = True
        elif fel == "titlu":
            fel_pe_rand.append(("marcaj", i))
        else:
            fel_pe_rand.append(("text", i))

    cuprins = set()
    run = []
    for fel, i in fel_pe_rand + [("text", -1)]:
        if fel == "marcaj":
            run.append((i, fel_articol.get(i, False)))
        elif fel == "gol":
            continue
        else:
            if len(run) >= _RUN_CUPRINS:
                # ULTIMUL marcaj de ARTICOL din serie nu e cuprins - e capul corpului. Seria se
                # rupe abia la primul rand de TEXT, iar acel text e corpul primului articol; deci
                # marcajul dinaintea lui apartine corpului. Masurat pe legea_207_2015_consolidat:
                # fara taietura, `ART. 1 Definiții` de la randul 506 cadea in cuprins si articolul
                # isi pierdea toate cele 51 de definitii.
                taie = None
                for k in range(len(run) - 1, -1, -1):
                    if run[k][1]:
                        taie = k
                        break
                pastrate = run if taie is None else run[:taie]
                cuprins.update(i for i, _e_art in pastrate)
            run = []
    return cuprins


_RANG = {"articol": 0, "alineat": 1, "litera": 2, "punct": 3}


class _Culegator:
    """Aduna atomii unui act pe o STIVA de ierarhie, nu pe trei variabile plate.

    DE CE O STIVA. Un act MODIFICATOR isi numeroteaza intervenţiile ca puncte sub un articol roman
    ("Art. II ... 42. La articolul 291, alineatele (1) si (2) se modifica si vor avea urmatorul
    cuprins:") si apoi CITEAZA VERBATIM alineatele actului modificat. Cu trei variabile plate,
    primul alineat citat inchidea contextul de punct si punctele urmatoare se pierdeau: masurat pe
    Legea 141/2025, din 63 de puncte ale art. II se culegeau 3, iar `pct42` - exact temeiul cotei de
    TVA de 21% pe care iConta il citeaza - nu exista deloc.

    PARINTELE unui punct se alege prin SECVENTA, nu prin rang. Un punct continua enumerarea care il
    asteapta: se urca in stiva pana la primul nod al carui urmator numar de punct e chiar acesta.
    Daca nimeni nu-l asteapta, randul NU e un punct - e proza care incepe cu o cifra, si se adauga
    ca text. Asa `43.` de dupa un alineat citat se leaga la articolul roman (care asteapta 43), nu
    la alineatul citat (care ar fi asteptat 1).

    ALINEATUL CITAT se cuibareste SUB punct (`#artII/pct42/alin1`), nu langa el: el e continutul
    intervenţiei, nu un alineat al actului modificator. Excepţia e restransa la punctele de
    INTERVENTIE (copii directi ai unui articol roman) - altfel un `(3)` normal, venit dupa o
    enumerare `1./2./3.` dintr-o litera, s-ar lega la punct in loc de articol.
    """

    def __init__(self, act):
        self.act = act
        self.atomi = []
        self.index = {}
        self.stiva = []
        self.secv = {}          # id parinte -> ultimul numar de punct acceptat
        self.titlu = None

    # ── ierarhie ────────────────────────────────────────────────────────────────────────────────
    @property
    def art(self):
        nod = self._nod("articol")
        return nod["cheie"] if nod is not None else None

    def _nod(self, nivel):
        for nod in reversed(self.stiva):
            if nod["nivel"] == nivel:
                return nod
        return None

    def _parinte_pentru(self, nivel):
        """Urca in stiva pana la un parinte valid pentru `nivel` (si o taie acolo)."""
        while self.stiva:
            top = self.stiva[-1]
            if top["nivel"] == "punct" and top.get("interventie") and nivel in ("alineat", "litera"):
                return top                      # citat verbatim in actul modificator
            if _RANG[top["nivel"]] < _RANG[nivel]:
                return top
            self.stiva.pop()
        return None

    def _parinte_punct(self, v):
        """Nodul din stiva care ASTEAPTA punctul `v` (secventa), sau None daca niciunul."""
        for nod in reversed(self.stiva):
            if self.secv.get(nod["id"], 0) + 1 == v:
                return nod
        return None

    _PREFIX = {"articol": "art", "alineat": "alin", "litera": "lit", "punct": "pct",
               "fragment": "frag"}

    def deschide(self, nivel, cheie, text, linie, parinte=None):
        if nivel == "articol" and parinte is None:
            # Un act modificator CITEAZA verbatim articole noi ale actului modificat ("25. Dupa
            # articolul 1575 se introduc patru noi articole, art. 1576 - 1579, cu urmatorul
            # cuprins:" urmat de `Art. 1577 - ...`). Citatul e CONTINUTUL punctului, nu un articol
            # al legii modificatoare: daca golea stiva, articolul roman gazda dispărea si cu el
            # secvenţa punctelor. Masurat pe Legea 141/2025: art. II se opria la pct. 25 din 63, iar
            # pct. 42 - temeiul cotei de TVA de 21% - nu exista.
            # DISCRIMINANTUL e cifra: articolele PROPRII ale unui act modificator sunt romane
            # (Art. I, Art. II), cele citate din Codul fiscal sunt arabe. Deci `Art. III` inchide
            # art. II, iar `Art. 1577` se cuibareste.
            gazda = None
            if not _ROMAN.match(str(cheie)):
                for nod in reversed(self.stiva):
                    if nod["nivel"] == "punct" and nod.get("interventie"):
                        gazda = nod
                        break
            if gazda is not None:
                while self.stiva and self.stiva[-1] is not gazda:
                    self.stiva.pop()
                parinte = gazda
            else:
                self.stiva = []
        elif nivel == "fragment":
            self.stiva = []
            parinte = None
        else:
            if parinte is None:
                parinte = self._parinte_pentru(nivel)
            else:
                while self.stiva and self.stiva[-1] is not parinte:
                    self.stiva.pop()
            if parinte is None and nivel != "fragment":
                return None                     # unitate fara articol-gazda: nu se inventeaza una
        baza = parinte["id"] if parinte is not None else self.act + "#"
        sep = "/" if parinte is not None else ""
        aid = "%s%s%s%s" % (baza, sep, self._PREFIX[nivel], cheie)
        if aid in self.index:
            n = 2
            while "%s~%d" % (aid, n) in self.index:
                n += 1
            aid = "%s~%d" % (aid, n)
        a = {"id": aid, "act": self.act, "nivel": nivel, "cheie": str(cheie),
             "parinte": parinte["id"] if parinte is not None else None,
             "articol": (str(cheie) if nivel == "articol"
                         else (self._nod("articol") or {}).get("cheie")),
             "alineat": (str(cheie) if nivel == "alineat"
                         else (self._nod("alineat") or {}).get("cheie")),
             "litera": (str(cheie) if nivel == "litera"
                        else (self._nod("litera") or {}).get("cheie")),
             "titlu_structural": self.titlu, "linie": linie,
             "text": [text] if text else [],
             "valabil_din": None, "valabil_pana": None, "modificat_de": [], "abrogat": False}
        if nivel == "punct":
            a["interventie"] = bool(parinte is not None and parinte["nivel"] == "articol"
                                    and _ROMAN.match(str(parinte["cheie"])))
            self.secv[parinte["id"]] = int(cheie) if str(cheie).isdigit() else 0
        self.atomi.append(a)
        self.index[aid] = a
        if nivel != "fragment":
            self.stiva.append(a)
        return a

    def curent(self):
        return self.atomi[-1] if self.atomi else None

    def adauga_text(self, linie):
        a = self.curent()
        if a is not None:
            a["text"].append(linie)


def atomizeaza_text(act, text):
    """(atomi, structura) pentru un act. `structura` = 'articole' sau 'fragmente'."""
    randuri = text.split("\n")
    cuprins = _randuri_de_cuprins(randuri)
    c = _Culegator(act)
    n = len(randuri)
    i = 0
    while i < n:
        idx = i
        linie = randuri[i].strip()
        i += 1
        if not linie or idx in cuprins:
            continue

        # ── nota de valabilitate: se ataseaza la atomul CURENT si se consuma pana la ")" ────────
        m = _NOTA_DIN.match(linie)
        if m:
            z, l, a, rest = m.groups()
            corp = [rest] if rest else []
            while i < n:
                r = randuri[i].strip()
                i += 1
                if r == ")" or (r.endswith(")") and len(r) <= 2):
                    break
                corp.append(r)
                if len(corp) > 12:       # nota nu se intinde; nu inghitim articolul urmator
                    break
            nota = " ".join(x for x in corp if x).strip()
            tinta = c.curent()
            if tinta is not None:
                d = "%s-%s-%s" % (a, l, z)
                if tinta["valabil_din"] is None or d > tinta["valabil_din"]:
                    tinta["valabil_din"] = d
                if nota:
                    tinta["modificat_de"].append({"din": d, "nota": nota})
            continue

        fel, numar, rest = _marcaj(linie)
        if fel == "titlu":
            c.titlu = rest
            continue
        if fel == "articol":
            c.deschide("articol", numar.replace(" ", ""), "", idx + 1)
            if rest:
                ma = _ALIN.match(rest)          # F2: `Art. I - (1) text`
                if ma:
                    c.deschide("alineat", ma.group(1), ma.group(2).strip(), idx + 1)
                else:
                    c.adauga_text(rest)         # F3: titlul articolului
            continue

        if c.art is None:
            continue

        m = _ALIN.match(linie)
        if m:
            c.deschide("alineat", m.group(1), m.group(2).strip(), idx + 1)
            continue

        m = _LIT.match(linie)
        if m and c._nod("alineat") is not None:
            c.deschide("litera", m.group(1), m.group(2).strip(), idx + 1)
            continue

        m = _PCT.match(linie)
        if m and m.group(1).isdigit() and len(m.group(1)) <= 3:
            par = c._parinte_punct(int(m.group(1)))
            if par is not None:
                c.deschide("punct", m.group(1), m.group(2).strip(), idx + 1, parinte=par)
                continue
            # niciun nod nu asteapta acest numar -> nu e punct, e proza care incepe cu o cifra

        if _ABROGAT.match(linie):
            a = c.curent()
            if a is not None:
                a["abrogat"] = True
                a["text"].append(linie)
            continue

        c.adauga_text(linie)

    if not any(a["nivel"] == "articol" for a in c.atomi):
        # F4: actul nu are structura de articol. Atomul e FRAGMENTUL de paragraf, si se declara ca atare.
        c = _Culegator(act)
        k = 0
        buf, linie_start = [], 1
        for idx, r in enumerate(randuri):
            s = r.strip()
            if s:
                if not buf:
                    linie_start = idx + 1
                buf.append(s)
            elif buf:
                k += 1
                c.deschide("fragment", k, " ".join(buf), linie_start)
                buf = []
        if buf:
            k += 1
            c.deschide("fragment", k, " ".join(buf), linie_start)
        for a in c.atomi:
            a["text"] = " ".join(x for x in a["text"] if x).strip()
        return c.atomi, "fragmente"

    for a in c.atomi:
        a["text"] = " ".join(x for x in a["text"] if x).strip()
    return c.atomi, "articole"


def atomizeaza_tot(dest=None):
    strat = json.load(open(os.path.join(_RAD, "artefacte", "strat_text.json"), encoding="utf-8"))
    dest = dest or os.path.join(_RAD, "artefacte", "atomi")
    os.makedirs(dest, exist_ok=True)
    per_act, total = {}, 0
    for baza in sorted(strat["acte"]):
        cale_text = os.path.join(_RAD, strat["acte"][baza]["text"])
        atomi, structura = atomizeaza_text(baza, open(cale_text, encoding="utf-8").read())
        out = os.path.join(dest, baza.replace("/", "__") + ".jsonl")
        with open(out, "w", encoding="utf-8") as f:
            for a in atomi:
                f.write(json.dumps(a, ensure_ascii=False) + "\n")
        niv = {}
        for a in atomi:
            niv[a["nivel"]] = niv.get(a["nivel"], 0) + 1
        per_act[baza] = {"fisier": os.path.relpath(out, _RAD), "n": len(atomi),
                         "structura": structura, "niveluri": niv,
                         "cu_valabilitate": sum(1 for a in atomi if a["valabil_din"]),
                         "abrogati": sum(1 for a in atomi if a["abrogat"])}
        total += len(atomi)
    raport = {
        "_ce": "OP4 atomizare structurala. `structura=fragmente` = actul NU are articole (pliant "
               "ANAF, structura de formular); atomul e paragraful, si se citeaza ca fragment.",
        "facut_la": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "n_acte": len(per_act), "n_atomi": total,
        "n_acte_pe_articole": sum(1 for v in per_act.values() if v["structura"] == "articole"),
        "n_acte_pe_fragmente": sum(1 for v in per_act.values() if v["structura"] == "fragmente"),
        "acte": per_act}
    with open(os.path.join(_RAD, "artefacte", "atomi_raport.json"), "w", encoding="utf-8") as f:
        json.dump(raport, f, ensure_ascii=False, indent=1, sort_keys=True)
    return raport


if __name__ == "__main__":
    t0 = time.time()
    r = atomizeaza_tot()
    print("atomizare: %d acte (%d pe articole, %d pe fragmente), %d atomi, %.1f s"
          % (r["n_acte"], r["n_acte_pe_articole"], r["n_acte_pe_fragmente"],
             r["n_atomi"], time.time() - t0))
