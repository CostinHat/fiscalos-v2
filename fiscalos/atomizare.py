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
# C31: numerele de articol peste 999 apar in forma portalului cu separator de mii ("Articolul 1.000",
# Codul civil); nerecunoscute, tot ce urma se lipea ca alineate de art. 999. Numarul se normalizeaza.
# C36: si "Articolul V^1" (roman cu exponent, OUG 89/2025) si "Articolul 270^2 a)" (numar cu litera,
# Legea 31/1990) - nerecunoscute, corpul lor se lipea ca alineate duplicate de articolul dinainte
_NR_ART = r"(\d{1,3}(?:\.\d{3})+(?:\^\d+)?|\d+(?:\^\d+)?(?:\s+[a-z]\))?|[IVXLCDM]+(?:\^\d+)?)"
_ART = re.compile(r"^\s*(?:Articolul|ARTICOLUL|Art\.|ART\.|Art|ART)\s*" + _NR_ART + r"\s*\.?\s*$")
# ── F2: "Art. I - (1) text" / "Art. 1577 - Baza lunară..." — liniuta separa numarul de corp ─────
_ART_INLINE = re.compile(r"^\s*(?:Articolul|ARTICOLUL|Art\.|ART\.)\s*" + _NR_ART +
                         r"\s*[-–—]\s*(\S.*)$")
# ── F3: "ART. 1 Definiții" — numar + titlu scurt, fara punct final ──────────────────────────────
_ART_TITLU = re.compile(r"^\s*(?:ART|Art)\.?\s*(\d+(?:\^\d+)?)\s+(\S[^.]{0,118})$")
# Vocabularul notelor de modificare: "Articolul 502 , Titlul XI a fost completat de..." NU e titlu
# de articol. Si nici o referinta interna ("Art. 291 alin. (1) din Codul fiscal").
_NU_E_TITLU = re.compile(r"a fost (modificat|completat|abrogat|introdus|republicat)|"
                         r"^(alin|pct|lit|paragraf)|prevede|se aplică|se aplica", re.I)

# "- (1) text": forma portalului pentru primul alineat al unui PUNCT ("238." / "- (1) Amortizarea ...")
_ALIN = re.compile(r"^\s*(?:[-–]\s*)?\((\d+(?:\^\d+)?)\)\s*(.*)$")
_LIT = re.compile(r"^\s*([a-z](?:\^\d+)?)\)\s*(.*)$")
# C26: in forma portalului, numarul punctului sta SINGUR pe rand ("238."), textul vine dupa
_PCT = re.compile(r"^\s*(\d+(?:\^\d+)?)\.\s*(\S.*)?$")
_NOTA_DIN = re.compile(r"^\s*\(la\s+(\d{2})-(\d{2})-(\d{4})\s*,?\s*(.*)$")
_ABROGAT = re.compile(r"^\s*Abrogat[ăa]?\.?\s*$", re.I)
_TITLU = re.compile(r"^\s*(Titlul|TITLUL|Capitolul|CAPITOLUL|Secțiunea|SECȚIUNEA|Sectiunea|"
                    r"SECTIUNEA|Subsecțiunea|Subsectiunea|Partea|PARTEA|Anexa|ANEXA)\s+"
                    r"([IVXLCDM0-9]+.*)$")
_ROMAN = re.compile(r"^[IVXLCDM]+(?:\^\d+)?$")
# C26: inceputul unei ANEXE - rand de sine statator: "ANEXA", "ANEXĂ", "Anexa nr. 2", "ANEXA 1 *1)",
# "Anexa Nr. 1*)", "ANEXĂ^1)", optional urmat de un titlu cu majuscule ("ANEXĂ REGLEMENTĂRI
# CONTABILE ...", "ANEXA 1 - PROCEDURI ..."). NU: "Anexa nr. 1 a fost modificată", "Anexa face parte
# integrantă", "Anexă Nr. crt. Țara" (cap de tabel).
_ANEXA = re.compile(r"^\s*(?:ANEXA|ANEXĂ|Anexa|Anexă)"
                    r"(?:\s*(?:nr\.|Nr\.|NR\.)?\s*(\d+(?:\^\d+)?(?:\.\d+)?|[IVX]+)(?![\w.]))?"
                    r"\s*(?:\*+\d*\)?|\^\d+\))?"
                    r"(?:\s*(?:[-–—]\s*)?(?=[A-ZĂÂÎȘȚŞŢ]{4,})(?![A-ZĂÂÎȘȚŞŢ]+\s+(?:a|se)\b).*)?\s*$")


def _e_anexa(linie):
    """Numarul anexei ('' daca e unica/nenumerotata), sau None daca randul nu deschide o anexa."""
    if len(linie) > 200:
        return None
    m = _ANEXA.match(linie)
    if not m:
        return None
    return (m.group(1) or "").replace(" ", "")


def _valoare_art(cheie):
    """Ordinea unui numar de articol: 18^1 -> (18, 1); roman -> valoarea lui."""
    c = str(cheie)
    if _ROMAN.match(c):
        c, _s, exp = c.partition("^")
        v, prev = 0, 0
        for ch in reversed(c):
            x = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}[ch]
            v = v - x if x < prev else v + x
            prev = max(prev, x)
        return (v, int(exp or 0))
    b, _s, e = c.partition("^")
    try:
        return (int(b), int(e or 0))
    except ValueError:
        return (0, 0)


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


_RANG = {"anexa": -1, "articol": 0, "alineat": 1, "litera": 2, "punct": 3}
_REPRODUCERE = re.compile(r"^(NOTĂ:\s*)?Reproducem mai jos", re.I)
DOC_MARCAJ = "⟦DOCUMENT⟧"
CITAT_MARCAJ = "⟦CITAT⟧"


# C36: un punct e de INTERVENTIE si intr-un articol ARAB, daca textul lui o spune ("1. La articolul 6
# alineatul (2), literele a) si c) se modifica si vor avea urmatorul cuprins:"). Legea 129/2019 art. 53,
# OG 13/2011, OUG 70/2024 modifica alte legi din articole arabe; alineatele citate se lipeau ca alineate
# duplicate ale articolului-gazda. Textul punctului vine pe randul URMATOR in forma portalului, deci
# decizia se ia cand sosesc alineatele, nu la deschiderea punctului.
_TEXT_INTERVENTIE = re.compile(r"(se modific[ăa]|se complet(?:ează|eaza)|se introduc[e]?|se înlocuiește|"
                               r"se inlocuieste|va avea|vor avea|se adaug[ăa])\b[^.]{0,200}"
                               r"\b(urm[ăa]torul cuprins|următoarea formă)", re.I)


def _e_interventie(nod):
    if nod.get("interventie"):
        return True
    if nod.get("citat"):
        return False                     # un punct din textul citat nu e interventia actului
    if nod["nivel"] == "punct" and _TEXT_INTERVENTIE.search(" ".join(nod["text"]) if isinstance(
            nod["text"], list) else nod["text"]):
        nod["interventie"] = True
        return True
    return False


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
        self.ultim_art_propriu = None
        self.anexa_principala = None
        self.titlul = None      # ultimul "Titlul X" (capitolele nu il sterg): numeste titlul in norme
        self.oficial = False
        self.citat = 0          # adancimea S_CIT a randului curent (0 = text propriu; stratul oficial)

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
            if top["nivel"] == "punct" and _e_interventie(top) and nivel in ("alineat", "litera"):
                return top                      # citat verbatim in actul modificator
            if top["nivel"] == "punct" and top.get("punct_de_anexa") and nivel in ("alineat", "litera"):
                return top                      # C26: punctul unei anexe e unitatea ei, ca un articol
            if _RANG[top["nivel"]] < _RANG[nivel]:
                return top
            self.stiva.pop()
        return None

    def _parinte_punct(self, v):
        """Nodul din stiva care ASTEAPTA punctul `v` (secventa), sau None daca niciunul.

        C26: o ANEXA isi numeroteaza punctele continuu (Reglementarile contabile: 1..600), cu goluri
        (puncte abrogate nereproduse, 12^1). Daca niciun nod nu asteapta exact `v`, anexa il accepta
        cand `v` urmeaza, cu un gol de cel mult 10, dupa ultimul ei punct."""
        for nod in reversed(self.stiva):
            if self.secv.get(nod["id"], 0) + 1 == v:
                return nod
        for nod in reversed(self.stiva):
            if nod["nivel"] == "anexa" and self.secv.get(nod["id"], 0) < v <= self.secv.get(nod["id"], 0) + 10:
                return nod
        return None

    _PREFIX = {"articol": "art", "alineat": "alin", "litera": "lit", "punct": "pct",
               "fragment": "frag", "anexa": "anexa", "nota": "nota"}

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
            if self.oficial:
                # stratul oficial: portalul spune ce e citat (S_CIT) - articolul citat se cuibareste sub
                # punctul care il introduce, cel propriu inchide tot
                if self.citat:
                    gazda = next((nod for nod in reversed(self.stiva) if nod["nivel"] == "punct"
                                  and nod.get("citat", 0) < self.citat), None)
            elif not _ROMAN.match(str(cheie)):
                for nod in reversed(self.stiva):
                    if nod["nivel"] == "punct" and _e_interventie(nod):
                        gazda = nod
                        break
            # C36: intr-un act de baza ARAB care modifica alte acte (OG 13/2011 art. 12), articolul care
            # urmeaza imediat ultimului articol propriu (13 dupa 12) e al actului, nu citat - altfel
            # art. 13-17 se cuibareau sub punctul de interventie al art. 12
            # ... afara de cazul in care punctul de interventie numeste chiar acel articol ("30. Articolul
            # 72 se modifica ..." in Legea 265/2022, al carei articol-gazda e chiar art. 71)
            if gazda is not None and not self.oficial and self.ultim_art_propriu is not None and \
                    not _ROMAN.match(str(self.ultim_art_propriu)) and \
                    _valoare_art(cheie)[0] == _valoare_art(self.ultim_art_propriu)[0] + 1 and \
                    not re.search(r"\barticolul\s+%s\b" % re.escape(str(cheie)),
                                  " ".join(gazda["text"]) if isinstance(gazda["text"], list) else gazda["text"], re.I):
                gazda = None
            anexa = self._nod("anexa")
            if gazda is None and anexa is not None:
                # C26: un articol dintr-o anexa (norme, regulament aprobat prin anexa) e al anexei,
                # daca numerotarea lui NU continua articolele proprii ale actului. Unul care le
                # continua (Codul fiscal: anexele unui titlu, apoi art. urmator) inchide anexa.
                if self.ultim_art_propriu is not None and \
                        _valoare_art(cheie) > _valoare_art(self.ultim_art_propriu):
                    self.stiva = []
                else:
                    gazda = anexa
            if gazda is not None:
                while self.stiva and self.stiva[-1] is not gazda:
                    self.stiva.pop()
                parinte = gazda
            else:
                self.stiva = []
        elif nivel == "anexa":
            # O anexa "la normele metodologice" e anexa NORMELOR, care sunt ele insele anexa actului
            # (HG 1/2016): se cuibareste sub anexa principala, iar un "Titlul ..." ulterior revine la
            # norme (vezi `atomizeaza_text`). Altfel, anexa e de nivel superior.
            principala = self.anexa_principala
            if principala is not None and re.search(r"\bla\s+(normele|prezentele norme|norme)\b",
                                                    text or "", re.I):
                self.stiva = [principala]
                parinte = principala
            else:
                self.stiva = []
                parinte = None
        elif nivel in ("fragment", "nota"):
            self.stiva = []
            parinte = None
        else:
            if parinte is None:
                parinte = self._parinte_pentru(nivel)
            else:
                while self.stiva and self.stiva[-1] is not parinte:
                    self.stiva.pop()
            if parinte is None and nivel not in ("fragment", "nota"):
                return None                     # unitate fara articol-gazda: nu se inventeaza una
        if nivel == "articol" and parinte is None:
            self.ultim_art_propriu = cheie
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
        if self.citat:
            a["citat"] = self.citat
        anexa = self._nod("anexa") if nivel != "anexa" else a
        if anexa is not None:
            a["anexa"] = anexa["cheie"]
            if self.titlul:
                a["titlul"] = self.titlul
        if nivel == "punct":
            a["interventie"] = bool(parinte is not None and parinte["nivel"] == "articol"
                                    and _ROMAN.match(str(parinte["cheie"])))
            if parinte is not None and parinte["nivel"] == "anexa":
                a["punct_de_anexa"] = True
            self.secv[parinte["id"]] = int(cheie) if str(cheie).isdigit() else 0
        if nivel == "nota":
            a["nota_tranzitorie"] = True     # C36: text reprodus din ALT act, nu articol al actului
        if nivel == "anexa" and parinte is None and self.anexa_principala is None:
            self.anexa_principala = a
        self.atomi.append(a)
        self.index[aid] = a
        if nivel not in ("fragment", "nota"):
            self.stiva.append(a)
        return a

    def curent(self):
        return self.atomi[-1] if self.atomi else None

    def adauga_text(self, linie):
        a = self.curent()
        if a is not None:
            a["text"].append(linie)


def atomizeaza_text(act, text, oficial=False):
    """(atomi, structura) pentru un act. `structura` = 'articole' sau 'fragmente'."""
    randuri = text.split("\n")
    cuprins = _randuri_de_cuprins(randuri)
    c = _Culegator(act)
    c.oficial = oficial
    n = len(randuri)
    i = 0
    while i < n:
        idx = i
        linie = randuri[i].strip()
        i += 1
        if not linie or idx in cuprins:
            continue
        c.citat = 0
        while linie.startswith(CITAT_MARCAJ):          # adancimea citarii (gradul 1, 2, ...)
            c.citat += 1
            linie = linie[len(CITAT_MARCAJ):]
        if c.citat:
            # un alineat/litera/punct CITAT: punctul care il cuprinde e, prin definitie, de interventie
            linie = linie.strip()
            # gazda = cel mai apropiat punct de adancime MAI MICA: o enumerare "1. 2. 3." din acelasi text
            # citat nu e punctul de interventie (Legea 141/2025 art. II pct. 42: lit. c) ajungea sub
            # lit. b) pct. 4)
            gazda = next((nod for nod in reversed(c.stiva) if nod["nivel"] == "punct"
                          and nod.get("citat", 0) < c.citat), None)
            if gazda is not None:
                gazda["interventie"] = True

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

        # C36: "NOTĂ: Reproducem mai jos: - prevederile art. 74-77 ... din Legea nr. 76/2012" - ce urmeaza
        # sunt articole ALTUI act, reproduse la finalul consolidatului (Codul civil: Legea 71/2011; Codul de
        # procedura civila: Legea 76/2012). Parsate ca structura, ele dadeau un al doilea "art. 74" si
        # alineate duplicate sub ultimul articol. Devin un atom NOTA al actului, pana la sfarsitul
        # documentului (separatorul DOC_MARCAJ, pus de stratul oficial intre documente).
        # numai in forma PORTALULUI (stratul oficial): in textul liber al instantaneului, aceeasi fraza
        # apare si in mijlocul actului, fara o granita sigura - masurat, regula muta acolo continut real
        if oficial and (_REPRODUCERE.match(linie) or (linie.startswith("NOTĂ:") and i < n and
                                                      _REPRODUCERE.match(randuri[i].strip()))):
            corp = [linie]
            while i < n and randuri[i].strip() != DOC_MARCAJ:
                r = randuri[i].strip()
                # zona se incheie la primul articol care CONTINUA numerotarea proprie a actului: in
                # instantaneu nota apare si in mijlocul actului (Codul fiscal), nu doar la final
                fel_r, nr_r, _rest = _marcaj(r) if r else (None, None, None)
                if fel_r == "articol" and c.ultim_art_propriu is not None and \
                        _valoare_art(nr_r.replace(".", "")) > _valoare_art(c.ultim_art_propriu):
                    break
                if r:
                    corp.append(r)
                i += 1
            c.deschide("nota", str(sum(1 for a in c.atomi if a["nivel"] == "nota") + 1), " ".join(corp), idx + 1)
            continue
        if linie == DOC_MARCAJ:
            continue

        nr_anexa = _e_anexa(linie)
        # o anexa CITATA intr-un punct de interventie ("Anexa nr. 2 se modifica ... cu urmatorul
        # cuprins:") e continutul punctului, nu o anexa a actului modificator
        if nr_anexa is not None and any(x["nivel"] == "punct" and x.get("interventie") for x in c.stiva):
            nr_anexa = None
        if nr_anexa is not None:
            # o SERIE de marcaje de anexa (lista anexelor, nu corpul lor) nu deschide nimic
            vecini = []
            for pas in (-1, 1):                 # cel mai apropiat rand NEGOL, in fiecare sens
                j = idx + pas
                while 0 <= j < n and not randuri[j].strip():
                    j += pas
                if 0 <= j < n:
                    vecini.append(randuri[j].strip())
            # ... si nici una lipita de CUPRINS (portalul incheie lista articolelor cu "Anexa nr. 2")
            anterioare, j = [], idx - 1
            while j >= 0 and len(anterioare) < 3:
                if randuri[j].strip():
                    anterioare.append(j)
                j -= 1
            if not any(_e_anexa(v) is not None for v in vecini) and \
                    not any(j in cuprins for j in anterioare):
                c.deschide("anexa", nr_anexa, linie, idx + 1)
                c.titlu = None
                if c.stiva and c.stiva[0] is c.curent():
                    c.titlul = None             # anexa de nivel superior: titlurile incep din nou
                continue
        fel, numar, rest = _marcaj(linie)
        if fel == "titlu":
            c.titlu = rest
            mt = re.match(r"^(?:Titlul|TITLUL)\s+([IVXLC]+(?:\^\d+)?)\b", rest)
            if mt:
                c.titlul = "Titlul " + mt.group(1)
            # un titlu nou al normelor inchide anexa-la-norme deschisa inainte
            if rest.lower().startswith("titlul") and c.anexa_principala is not None and \
                    any(x["nivel"] == "anexa" and x is not c.anexa_principala for x in c.stiva):
                c.stiva = [c.anexa_principala]
            continue
        if fel == "articol":
            c.deschide("articol", numar.replace(" ", "").replace(".", "").replace(")", ""), "", idx + 1)
            if rest:
                ma = _ALIN.match(rest)          # F2: `Art. I - (1) text`
                if ma:
                    c.deschide("alineat", ma.group(1), ma.group(2).strip(), idx + 1)
                else:
                    c.adauga_text(rest)         # F3: titlul articolului
            continue

        if c.art is None and c._nod("anexa") is None:
            continue

        m = _ALIN.match(linie)
        if m:
            c.deschide("alineat", m.group(1), m.group(2).strip(), idx + 1)
            continue

        m = _LIT.match(linie)
        if m and (c._nod("alineat") is not None or
                  any(x["nivel"] == "punct" and x.get("punct_de_anexa") for x in c.stiva)):
            c.deschide("litera", m.group(1), m.group(2).strip(), idx + 1)
            continue

        # C26: in forma portalului, punctul DE ANEXA sta singur pe rand ("238."), iar randul urmator
        # incepe cu liniuta ("- (1) Amortizarea ..." / "- Capitalurile proprii ..."). Enumerarile
        # interioare ("1. text") nu au liniuta. Acesta e punctul anexei, oricare ar fi secventa. In
        # Normele Codului fiscal punctele se renumeroteaza pe fiecare titlu: acelasi numar primeste
        # sufixul ~N, iar temeiul uman numeste titlul.
        m = re.match(r"^(\d+(?:\^\d+)?)\.$", linie)
        if m and c._nod("anexa") is not None:
            j = i
            while j < n and not randuri[j].strip():
                j += 1
            urm = randuri[j].strip() if j < n else ""
            # "- ..." (Reglementarile contabile) sau "(1)" (Normele Codului fiscal: "40^1." / "(1)")
            if urm[:1] in "-–" or re.match(r"^\(1\)", urm):
                c.deschide("punct", m.group(1), "", idx + 1, parinte=c._nod("anexa"))
                continue

        # C36: un PUNCT CITAT (stratul oficial, adancime d) are parintele in acelasi text citat (secventa,
        # noduri de adancime d) sau, altfel, punctul care il introduce (cel mai apropiat de adancime < d).
        # Legea 30/2019: punctele 1^1-1^6 ale OUG 25/2018, introduse de pct. 1 al legii de aprobare, se
        # legau prin secventa de art. I, ca frati ai pct. 1.
        m = re.match(r"^(\d{1,3})(?:\^(\d+))?\.\s*(\S.*)?$", linie) if c.citat else None
        if m and c._nod("articol") is not None:
            v, exp = int(m.group(1)), m.group(2)
            par = next((nod for nod in reversed(c.stiva) if nod.get("citat", 0) == c.citat and (
                c.secv.get(nod["id"], 0) == v if exp else c.secv.get(nod["id"], 0) + 1 == v)), None)
            if par is None:
                par = next((nod for nod in reversed(c.stiva) if nod["nivel"] == "punct"
                            and nod.get("citat", 0) < c.citat), None)
            if par is not None:
                c.deschide("punct", "%s^%s" % (v, exp) if exp else str(v), (m.group(3) or "").strip(),
                           idx + 1, parinte=par)
                if exp:
                    c.secv[par["id"]] = v
                continue

        # C36: punct cu exponent ("1^5.", Legea 30/2019) - il asteapta nodul al carui ultim punct e 1
        m = re.match(r"^(\d{1,3})\^(\d+)\.\s*(\S.*)?$", linie)
        if m:
            par = next((nod for nod in reversed(c.stiva) if c.secv.get(nod["id"]) == int(m.group(1))), None)
            if par is not None:
                c.deschide("punct", "%s^%s" % (m.group(1), m.group(2)), (m.group(3) or "").strip(), idx + 1,
                           parinte=par)
                c.secv[par["id"]] = int(m.group(1))
                continue

        m = _PCT.match(linie)
        if m and m.group(1).isdigit() and len(m.group(1)) <= 3:
            par = c._parinte_punct(int(m.group(1)))
            if par is not None:
                c.deschide("punct", m.group(1), (m.group(2) or "").strip(), idx + 1, parinte=par)
                continue
            # niciun nod nu asteapta acest numar -> nu e punct, e proza care incepe cu o cifra

        if _ABROGAT.match(linie):
            a = c.curent()
            if a is not None:
                a["abrogat"] = True
                a["text"].append(linie)
            continue

        c.adauga_text(linie)

    if not any(a["nivel"] in ("articol", "anexa") for a in c.atomi):
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
