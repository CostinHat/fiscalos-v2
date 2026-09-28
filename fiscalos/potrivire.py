# -*- coding: utf-8 -*-
"""OP6+OP7 — POTRIVIREA fiecarui parametru cu atomul din corpus care il stabileste, si CLASIFICAREA.

CE INTREABA acest pas. Nu "seamana valoarea cu ceva din lege", ci trei intrebari separate, fiindca
raspunsurile lor pot diverge si fiecare divergenta e informatie:

  1. SE REZOLVA CITAREA?  Temeiul declarat de iConta numeste un act si (de regula) un articol si un
     citat verbatim. Acel citat trebuie sa se gaseasca in acel act din corpus. Cand nu se gaseste,
     asta NU inseamna ca valoarea e greșita - inseamna ca proba nu duce unde spune ca duce.
  2. SPUNE LEGEA ACEEASI VALOARE?  Valoarea din cod trebuie sa apara in textul verbatim al atomului,
     in FORMA in care legea scrie numere (21%, 50.000 lei, 2,25%).
  3. DESPRE ACELASI LUCRU E VORBA?  Un "25" gasit intr-un alineat nu inseamna nimic fara subiect.
     Deci un atom conteaza numai daca poarta SI valoarea SI un cuvant-cheie al subiectului.

CLASIFICAREA (regula 4 din brief, regula 5 din CLAUDE.md):
  CONCORDA  exista un atom care poarta subiectul SI valoarea din cod. Se citeaza id-ul si fragmentul.
  DIFERA    exista un atom care poarta subiectul, dar cu ALTA valoare de aceeasi forma. Se arata
            AMBELE parti: valoarea din codul iConta si numarul din textul legii.
  NEGASIT   niciun atom din corpus nu stabileste parametrul. Inclusiv cand actul declarat nu e in
            corpus sau nu e extractibil - caz in care motivul spune care din cele doua, fiindca o
            limita a uneltei nu e o absenta din lege (CLAUDE.md §2).

DE UNDE VIN CUVINTELE-CHEIE, si de ce nu sunt valori. Un cuvant-cheie e un INDICIU DE CAUTARE, nu o
valoare: el decide UNDE se uita programul, niciodata CE raporteaza. Orice rezultat citeaza atomul si
fragmentul verbatim, deci un indiciu prost produce NEGASIT sau un atom vizibil nepotrivit - nu o
valoare inventata. Trei surse, in ordine:
  (a) `text_citat` din `Temei`-ul iConta - cuvintele LOR, nu ale noastre;
  (b) `art`/`alin`/`lit` din `Temei` - duc direct la id-ul atomului;
  (c) un tabel de fraze scris aici, pentru parametrii pe care iConta NU-i sursează deloc. Fara el,
      clasa nesursata ar da NEGASIT prin construcţie, iar masuratoarea ar fi despre tabel, nu
      despre corpus.
"""
import json
import os
import re
import time
import unicodedata
from decimal import Decimal, InvalidOperation

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ── normalizare ──────────────────────────────────────────────────────────────────────────────────
def norm(t):
    """Fara diacritice, minuscule, spatii strânse. Textul VERBATIM nu se atinge - se normalizeaza
    numai copia pe care se CAUTA, ca `întreprinderi` sa gaseasca `intreprinderi`."""
    t = unicodedata.normalize("NFKD", t or "")
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.replace("ș", "s").replace("ş", "s").replace("ț", "t").replace("ţ", "t")
    return re.sub(r"\s+", " ", t.lower()).strip()


# ── formele in care LEGEA scrie un numar ─────────────────────────────────────────────────────────
def _grupat(intreg):
    s = str(intreg)
    parti = []
    while len(s) > 3:
        parti.insert(0, s[-3:])
        s = s[:-3]
    parti.insert(0, s)
    return parti


def forme_numar(valoare, fel):
    """Formele textuale in care `valoare` poate apărea intr-un act. `fel` = 'procent' | 'suma'.

    Legea scrie `50.000 lei`, nu `50000`; `2,25%`, nu `2.25%`. Fara formele romanesti, o valoare
    corecta ar ieși NEGASIT - adica raportul ar masura formatarea, nu concordanta.
    """
    try:
        d = Decimal(str(valoare))
    except (InvalidOperation, ValueError, TypeError):
        return set()
    forme = set()
    if fel == "procent":
        # FARA `.normalize()` si fara `rstrip("0")` pe intreg. `Decimal("10").normalize()` da
        # `1E+1`, iar `format(...,"f").rstrip("0")` transforma "10" in "1" - deci cota de 10% primea
        # printre formele ei si "1%", si un text care spune 1% o "confirma". Masurat pe inventarul
        # real: `bacsis.COTA_IMPOZIT=10` ieșea CONCORDA pe CF art.51 alin.(1) ("cota ... este de 1%"),
        # `d216.COTA_IMPOZIT=0.3` pe acelasi articol ca "3%", iar `d394.COTE=20` pe un "2%" din norme.
        # Trei valori greșite confirmate de trei texte care spun altceva - o CONCORDA falsa e la fel
        # de grava ca un DIFERA fals. Zerourile se taie NUMAI din partea zecimala.
        pr = d * 100 if d < 1 else d
        txt = format(pr, "f")
        if "." in txt:
            txt = txt.rstrip("0").rstrip(".")
        for baza in {txt, txt.replace(".", ",")}:
            forme.add(baza + "%")
            forme.add(baza + " %")
        return forme
    intreg = int(d)
    frac = format(d, "f")
    if d == intreg:
        forme.add(str(intreg))
        forme.add(".".join(_grupat(intreg)))
        forme.add(" ".join(_grupat(intreg)))
    else:
        forme.add(frac)
        forme.add(frac.replace(".", ","))
        forme.add(".".join(_grupat(intreg)) + "," + frac.split(".")[1])
    return forme


_MARGINE = r"(?<![0-9.,])%s(?![0-9])"


def gaseste_forma(text_norm, forme):
    """Prima forma din `forme` prezenta in text, cu margini de cifra (ca `5000` sa nu prinda `50000`)."""
    for f in sorted(forme, key=len, reverse=True):
        if re.search(_MARGINE % re.escape(f), text_norm):
            return f
    return None


_PROCENT_IN_TEXT = re.compile(r"(\d{1,3}(?:[.,]\d{1,3})?)\s*%")
_SUMA_IN_TEXT = re.compile(r"(\d{1,3}(?:\.\d{3})+|\d+(?:,\d{1,2})?)\s*(?:lei|euro|eur\b)")


def numere_din_text(text_norm, fel):
    rx = _PROCENT_IN_TEXT if fel == "procent" else _SUMA_IN_TEXT
    ies = []
    for m in rx.finditer(text_norm):
        if m.group(1) not in ies:
            ies.append(m.group(1))
    return ies


# ── indiciile de subiect (sursa (c): fraze, NU valori) ───────────────────────────────────────────
SUBIECT = {
    # registrul COTE
    "tva_standard": ["cota standard"],
    "tva_redusa": ["cota redusa"],
    "tva_redusa_9": ["cota redusa"],
    "tva_redusa_5": ["cota redusa"],
    "impozit_dividend": ["dividende"],
    "plafon_tva_incasare": ["tva la incasare", "cifra de afaceri", "plafon"],
    "plafon_mijloc_fix": ["mijloace fixe", "mijloc fix", "imobilizari corporale"],
    "plafon_intrastat": ["intrastat", "praguri valorice"],
    "plafon_sold_casa": ["numerar", "plafon zilnic"],
    "plafon_avans_decontare": ["avansuri spre decontare", "plafon zilnic"],
    "impozit_micro": ["microintreprinderi"],
    "impozit_profit": ["impozit pe profit", "profitul impozabil"],
    "cas": ["asigurari sociale"],
    "cass": ["asigurari sociale de sanatate"],
    "impozit_venit": ["cota de impozit"],
    "cam": ["contributiei asiguratorii pentru munca", "asiguratorie pentru munca"],
    "salariu_minim": ["salariul de baza minim brut", "salariul minim"],
    "facilitate_salariu_minim": ["nu se datoreaza impozit", "nu se cuprinde in baza lunara"],
    "plafon_facilitate_salariu_minim": ["venitul brut", "nu depaseste nivelul de"],
    "tichet_masa_plafon": ["tichet de masa", "valoarea nominala"],
    # Termenele NU au indicii aici: `_potriveste_termen` isi construieste fraza de scadenta din
    # valoarea din cod (`_FRAZA_TERMEN`) si numele declaraţiei din `_NUME_DECLARATIE`. Intrarile de
    # dinainte conţineau ziua ("pana la data de 25 inclusiv"), adica VALOAREA in indiciu - erau
    # neutilizate, dar incalcau regula ca un indiciu nu poarta cifre.
    # constante nesursate - fraze scrise DUPA ce s-a citit ce face fiecare modul
    "COTA_IMPOZIT": ["bacsis", "cota de impozit"],
    "PLAFON_CADOU": ["cadouri", "cadou"],
    "PLAFON_SOLD_ZI_CC": ["plafon", "casierie", "sold"],
    "PLAFON_INCASARE_PJ": ["incasari in numerar", "plafon zilnic"],
    "PLAFON_INCASARE_PJ_CC": ["incasari in numerar", "plafon zilnic"],
    "PLAFON_PLATA_PJ": ["plati in numerar", "plafon zilnic"],
    "PLAFON_PLATA_PJ_TOTAL": ["plati in numerar", "plafon"],
    "PLAFON_PF": ["persoane fizice", "numerar", "plafon"],
    "COTA_STANDARD": ["cota standard", "impozit pe profit"],
    "COTA_REDUSA": ["cota redusa"],
    "PRAG_IMCA_EUR": ["cifra de afaceri"],
    "IMPOZIT_ANUAL": ["impozit anual"],
    "COTE": ["cota"],
    "_PCT_DEDUCERE_BAZA": ["deducere personala"],
    "DEDUCERE_COPIL_SCOALA": ["deducere personala suplimentara"],
    "PRAG_VENIT_DEDUCERE": ["deducere personala", "salariul de baza minim brut"],
    "PLAFON_EUR": ["activitati economice"],
    "PRAG_ELECTRONICE": ["taxare inversa", "telefoane mobile", "dispozitive cu circuite integrate"],
    "PRAG_BRENT_USD": ["brent", "petrol"],
}
# parametri OPERATIONALI, nu fiscali: iConta insasi scrie, in `test_constante_nesursate.py`, ca sunt
# "o regula de produs (cate esecuri, in cate minute), fara act normativ de citat". NU li se cauta
# temei - dar nici nu se ascund: ies NEGASIT cu acest motiv, ca sa se vada ca absenta e asteptata.
OPERATIONALE = {"PRAG_ESECURI", "PRAG_RITM", "PRAG_VECHIME_ZILE", "PRAG_ATENTIE",
                "PRAG_URMARIT_ZILE", "PRAG_ZILE", "PRAGURI", "DOAR_VENITURI", "MOD_VENIT_NET"}


# Un indiciu nu are voie sa conţina cifre. Doua dintre cele scrise la prima versiune le conţineau
# ("15.000 euro", "50.000.000 euro"): un indiciu cu valoarea in el se confirma pe sine, fiindca
# localizarea unitaţii de text ar depinde de numarul caăutat. Gardul e verificat de o proba.
_CIFRA = re.compile(r"\d")


def _stemuri_indiciu(frază):
    """Stemurile unui indiciu de subiect. TOATE trebuie sa apară in atom.

    DE CE STEMURI si nu subsir. Indiciul "mijloace fixe" NU e subsir in "valoarea minima de intrare a
    mijloacelor fixe ... este de 2.500 lei" - romana flexioneaza, iar potrivirea pe subsir cere forma
    exacta a dicţionarului. Masurat: `plafon_mijloc_fix` ieșea NEGASIT desi HG 276/2013 din corpus
    scrie limpede pragul. Se cere prezenţa TUTUROR stemurilor in acelasi atom, ca indiciul sa rămână
    strâns: "mijloac" singur ar prinde si "mijloace de transport".
    """
    return [_stem(w) for w in norm(frază).split() if len(w) >= 3]


_FEREASTRA_INDICIU = 80
_ADIACENT = 25          # cate caractere pot sta intre doua stemuri ale aceleiasi fraze


def _valoare_langa_subiect(atom, forma, indicii_stem):
    """Valoarea sta la mai puţin de o fereastra de un stem de subiect, in acelasi atom.

    Folosit NUMAI pentru actele fara structura de articol (pliante ANAF, structuri de formular), unde
    atomul e un paragraf, nu un alineat. `anaf_limite_2025` e un tabel pe coloane redat in text: ANAF
    publica pliantul cu coloane paralele, iar extractia le intretese, asa ca fraza-subiect se rupe
    ("stabilirea valorii nominale inde-") si nu se mai potriveste cu indiciul. Acolo singurul test
    disponibil e vecinatatea, si se declara ca atare in raport - nu se da drept ancora tare.
    """
    i = atom["_n"].find(forma)
    if i < 0:
        return False
    for stems in indicii_stem:
        for st in stems:
            j = atom["_n"].find(st)
            if j >= 0 and abs(j - i) <= 3 * _FEREASTRA_INDICIU:
                return True
    return False


def _are_subiect(atom, indicii_stem):
    """Un indiciu e prezent numai ca FRAZĂ: stemurile lui, in ORDINE, fiecare aproape de precedentul.

    DE CE ORDINE SI ADIACENŢĂ, nu doar prezenţa. Cu stemuri cerute oriunde in atom, indiciul
    "deducere personala" s-a intalnit intamplator in alineate despre cu totul altceva, si asa au ieșit
    patru CONCORDA FALSE pentru procentele deducerii personale (20%, 25%, 30%, 35% "confirmate" pe
    venituri din cedarea folosinţei bunurilor, pe definiţia persoanei afiliate si pe un tabel de
    formular). Cu proximitate dar FARA ordine, doua au rămas: CF art.85 alin.(2) spune "...proprietate
    personală se determină prin deducerea din venitul brut...", adica exact cele doua stemuri la 25 de
    caractere unul de altul - dar in ordine INVERSĂ si in propoziţii diferite. O frază are ordine.

    O CONCORDA falsa e la fel de grava ca un DIFERA fals: amandoua citeaza corect un atom care nu
    stabileste parametrul.
    """
    for stems in indicii_stem:
        if not stems:
            continue
        de_la = 0
        ok = True
        for k, st in enumerate(stems):
            i = atom["_n"].find(st, de_la)
            if i < 0 or (k > 0 and i - de_la > _ADIACENT):
                ok = False
                break
            de_la = i + len(st)
        if ok:
            return True
    return False


def _fel(p):
    """'procent' pentru rate, 'suma' pentru plafoane/sume, 'alt' pentru termene/conturi/nomenclatoare."""
    if p["clasa"] == "cota":
        return "procent"
    if p["clasa"] == "plafon":
        return "suma"
    return "alt"


# ── indexul de atomi ─────────────────────────────────────────────────────────────────────────────
class Corpus(object):
    def __init__(self):
        rap = json.load(open(os.path.join(_RAD, "artefacte", "atomi_raport.json"), encoding="utf-8"))
        self.structura = {b: v.get("structura") for b, v in rap["acte"].items()}
        self.strat = json.load(open(os.path.join(_RAD, "artefacte", "strat_text.json"),
                                   encoding="utf-8"))
        self.pe_act = {}
        for baza, v in rap["acte"].items():
            atomi = [json.loads(l) for l in
                     open(os.path.join(_RAD, v["fisier"]), encoding="utf-8")]
            for a in atomi:
                a["_n"] = norm(a["text"])
            self.pe_act[baza] = atomi
        self.toti = [a for ats in self.pe_act.values() for a in ats]
        self.dupa_id = {a["id"]: a for a in self.toti}

    def act_din_url(self, url):
        """'anaf_surse/legea_141_2025_consolidat.html' -> baza de act din corpus, sau None."""
        if not url:
            return None
        baza = os.path.splitext(os.path.basename(url))[0]
        if baza in self.pe_act:
            return baza
        for cand in self.pe_act:                       # forma .pdf/.html/.txt a aceluiasi act
            if os.path.basename(cand) == baza:
                return cand
        return None

    def act_neextractibil(self, url):
        if not url:
            return None
        baza = os.path.splitext(os.path.basename(url))[0]
        return baza if baza in self.strat["neextractibile"] else None


# ── planul de conturi, CITIT DIN CORPUS ──────────────────────────────────────────────────────────
# OMFP 1802/2014 listeaza planul ca serie de `NNNN. Denumire (A/P)` in interiorul unui singur atom
# (lista e o enumerare in proza, nu articole). Deci intrebarea pusa corpusului pentru un cont nu e
# "ce valoare are" - un simbol de cont NU e o valoare - ci "exista in plan, si cu ce denumire".
# Un simbol de cont din plan e o CIFRA urmata de o denumire cu majuscula. Denumirea se intinde pana
# la simbolul urmator - nu se poate descrie cu o singura potrivire, fiindca ea contine paranteze
# ("Echipamente tehnologice (masini, utilaje...)") si cifre ("Conturi la banci in lei"). Prima
# versiune cerea ca urmatorul simbol sa urmeze imediat, si rata astfel ultima intrare din fiecare
# serie plus toate denumirile cu paranteze: 562 simboluri citite, dar 2131, 2805, 282, 436 - conturi
# reale, folosite de iConta - lipseau. Deci se taie INTRE pozitii, nu se potriveste o intrare.
_POZITIE_CONT = re.compile(r"(?<![\d^.,/-])(\d{2,4})\.?\s+(?=[A-ZĂÂÎȘȚ])")
# Denumirea se incheie la marcajul de fel - (A)/(P)/(A/P) - sau la nota de valabilitate care poate
# urma imediat dupa el in consolidat ("436. Contribuția asiguratorie pentru muncă (P) (la 07-02-2018
# Planul de conturi a fost completat de...)"). Prima versiune ancora marcajul la SFARSITUL denumirii,
# deci contul 436 - folosit de iConta - cadea peste plafonul de lungime si dispărea din plan.
_FEL_CONT = re.compile(r"\s*\((A/P|A|P)\)")
_NOTA_IN_PLAN = re.compile(r"\s*\(la \d{2}-\d{2}-\d{4}")
_ACTE_PLAN = ("omfp_1802_2014_reglementari_consolidat", "omfp_1802_2014")


# Proza care imita o intrare de plan se taie pe LUNGIMEA denumirii, si plafonul e MASURAT pe act:
# cele 1626 de candidaturi din atomul planului au mediana 42, p90 84, p97 121 - iar proza incepe la
# 234 ("6511 Cheltuieli ocazionate de constituirea fiduciei ---------- Contul 6511 ...") si urca la
# 749 pentru falsul `2015` (anul din "...ulterior datei de 1 ianuarie 2015. Ca urmare, acestea
# efectueaza...") si la 85.998 pentru falsul `2019`. Toate intrarile reale verificate stau sub 80.
_MAX_DENUMIRE = 130
# marcaje de PROZA despre un cont, nu de intrare in plan
_PROZA_CONT = re.compile(r"Contul\s|\(rd\.|\(ct\.|-{6,}|Not[ăa]\s|Cu ajutorul|În funcție de forma")


def plan_de_conturi(corp):
    """{simbol: {denumire, fel, atom, verbatim}} = planul de conturi, CITIT din atomii OMFP 1802/2014.

    SE RESTRANGE LA ATOMUL CARE *E* PLANUL (masurat: unul singur, cu 1626 de candidati, antetele
    "Planul de conturi" si "CLASA 1"). Fara restrangere, extractia culegea `100 Patrimoniul public
    (ct. 1016)` si `102 CAPITALURI - TOTAL (rd. 100 + 101 + 102)` din tabelul de RANDURI al unui
    formular, dintr-un alt atom - adica raportul ar fi confirmat conturi care nu exista.

    NU se taie insa la o REGIUNE din atom. Prima incercare a pornit de la antetul "CLASA 1", si a
    pierdut 45 de simboluri, intre care 436 (CAM), 4315/4316, 463 si 646 - exact conturile ADAUGATE
    prin modificari, care in consolidat stau in blocul de note de completare, INAINTEA planului de
    baza. Planul curent nu e o regiune contigua, deci se citeste tot atomul si se taie pe FORMA
    intrarii (vezi `_MAX_DENUMIRE`, `_PROZA_CONT`).
    """
    plan = {}
    for act in _ACTE_PLAN:
        for a in corp.pe_act.get(act, []):
            txt = a["text"]
            if "Planul de conturi" not in txt or "CLASA 1" not in txt:
                continue
            poz = list(_POZITIE_CONT.finditer(txt))
            if len(poz) < 500:
                continue
            for i, m in enumerate(poz):
                simbol = m.group(1)
                if len(simbol) < 3:
                    continue
                sfarsit = poz[i + 1].start() if i + 1 < len(poz) else len(txt)
                den = txt[m.end():sfarsit].strip(" .-;,")
                fel = None
                mf = _FEL_CONT.search(den)
                mn = _NOTA_IN_PLAN.search(den)
                taieturi = [x.start() for x in (mf, mn) if x is not None]
                if mf is not None and (mn is None or mf.start() <= mn.start()):
                    fel = mf.group(1)
                if taieturi:
                    den = den[:min(taieturi)].strip(" .-;,")
                if len(den) < 4 or len(den) > _MAX_DENUMIRE or simbol in plan:
                    continue
                if _PROZA_CONT.search(den):
                    continue
                i0 = max(0, m.start() - 50)
                j0 = min(len(txt), sfarsit + 20)
                plan[simbol] = {"denumire": den, "fel": fel, "atom": a["id"],
                                "verbatim": txt[i0:j0].strip(),
                                "valabil_din": a["valabil_din"]}
    return plan


# ── potrivirea unui parametru ────────────────────────────────────────────────────────────────────
def _fragmente_citat(text_citat):
    """Bucatile distinctive ale citatului declarat de iConta, pentru cautare partiala.

    Citatul lor e o REDARE (diacritice normalizate, ghilimele proprii, uneori parafraza intre
    paranteze), deci potrivirea exacta ar eșua pe forma, nu pe fond. Se taie pe punctuatie tare si se
    pastreaza bucatile de >= 25 de caractere: destul de lungi ca sa fie distinctive, destul de multe
    ca o parafraza partiala sa tot prinda.
    """
    t = norm(text_citat)
    t = re.sub(r"art\.?\s*[\divxlcm^]+|alin\.?\s*\(?[\d^]+\)?|lit\.?\s*[a-z]\)?|pct\.?\s*\d+", " ", t)
    bucati = [b.strip(" ;:,.\"'()") for b in re.split(r"[;:\"]|\.\s|\(|\)", t)]
    return [b for b in bucati if len(b) >= 25]


# ── potrivirea unui CITAT PARAFRAZAT ─────────────────────────────────────────────────────────────
# `text_citat` din `Temei` e REDAREA iConta, nu textul legii: "impozit pe dividende cota 16% asupra
# dividendului brut" fata de "Impozitul pe dividende se stabileste prin aplicarea unei cote de impozit
# de 16% asupra dividendului brut". Potrivirea pe subsir cade pe parafraza, si atunci decizia trece la
# indiciul de subiect - care pe un act mare e prea larg: `legea_141_2025_consolidat` vorbeste despre
# dividende in cinci locuri, cu 16% si cu 10%, deci "dividende" singur confirma orice.
#
# CIFRELE SE EXCLUD DIN POTRIVIRE, si asta e miezul: daca numerele ar intra in punga de cuvinte,
# gasirea unitatii de text ar depinde de valoarea caăutata, si un 10% greșit si-ar gasi singur gazda.
# Aici se localizeaza UNITATEA prin cuvintele de conţinut, si abia apoi se verifica valoarea in ea.
_SUFIXE = ("urilor", "urile", "ilor", "elor", "ului", "lui", "uri", "ile", "ele", "ii", "ei", "ea",
           "or", "ul", "a", "e", "i", "u")
_STOP = {"care", "prin", "pentru", "asupra", "unei", "unui", "este", "sunt", "dintre", "conform",
         "potrivit", "prevazut", "prevazute", "art", "alin", "lit", "pct", "din", "catre"}


def _stem(w):
    for suf in _SUFIXE:
        if len(w) > len(suf) + 2 and w.endswith(suf):
            return w[:-len(suf)]
    return w


def _cuvinte_citat(text_citat):
    """Punga de cuvinte de conţinut a citatului, FARA cifre. Pentru localizare, nu pentru valoare."""
    t = norm(text_citat)
    t = re.sub(r"[^a-z\s]", " ", t)          # scoate cifre si punctuaţie: raman numai cuvinte
    ies = []
    for w in t.split():
        if len(w) < 4 or w in _STOP:
            continue
        st = _stem(w)
        if len(st) >= 3 and st not in ies:
            ies.append(st)
    return ies


def _alege_atom(atomi, cuvinte):
    """Dintre atomii candidaţi, cel pe care CITAREA il descrie cel mai bine; la egalitate, cel mai scurt.

    DE CE NU "cel mai scurt". HG 276/2013 poarta "2.500 lei" in doua alineate: alin.(1) stabileste
    pragul ("valoarea minima de intrare a mijloacelor fixe ... este de 2.500 lei"), iar alin.(2) e o
    regula tranzitorie despre valoarea rămasa neamortizata "cuprinsa intre 1.800 lei si 2.500 lei".
    Cel mai SCURT e al doilea, deci raportul citea regula tranzitorie ca temei al pragului. Scorul pe
    cuvintele citarii il alege pe primul (5 stemuri fata de 4), si nu foloseste cifre - deci nu poate
    rescrie verdictul, doar alege unitatea de text pe care iConta o descrie.
    """
    def cheie(a):
        scor = sum(1 for c in cuvinte if c in a["_n"]) if cuvinte else 0
        return (-scor, len(a["text"]))
    return min(atomi, key=cheie)


def _potrivire_pe_cuvinte(atomi, cuvinte, prag=0.8):
    """Atomii care conţin cel puţin `prag` din cuvintele de conţinut ale citatului."""
    if len(cuvinte) < 3:
        return []
    nevoie = max(3, int(round(prag * len(cuvinte))))
    ies = []
    for a in atomi:
        n = sum(1 for c in cuvinte if c in a["_n"])
        if n >= nevoie:
            ies.append((n, a))
    if not ies:
        return []
    maxim = max(n for n, _a in ies)
    return [a for n, a in ies if n == maxim]      # numai cei mai buni, nu toti cei care trec pragul


def potriveste(p, corp, plan=None):
    if p["clasa"] == "cont":
        return _potriveste_cont(p, plan or {})
    if p["clasa"] == "nomenclator":
        return _potriveste_nomenclator(p, corp)
    fel = _fel(p)
    temei = p["temei_declarat"] or {}
    url = temei.get("url")
    subiecte = [norm(s) for s in SUBIECT.get(p["nume"], [])]
    if not subiecte and temei.get("text_citat"):
        subiecte = _fragmente_citat(temei["text_citat"])[:3]
    if p["clasa"] == "termen":
        return _potriveste_termen(p, corp)

    rez = {"parametru": p["id"], "clasa": p["clasa"], "nume": p["nume"],
           "valoare_cod": p["valoare_cod"], "valabil_din_cod": p["valabil_din_cod"],
           "unde_in_cod": p["unde"],
           "temei_declarat_de_iconta": (temei.get("text") or
                                        " ".join(str(temei.get(k)) for k in ("tip", "nr", "an")
                                                 if temei.get(k))) or None,
           "citare_rezolvata": None, "atom": None, "atom_verbatim": None,
           "valabil_din_corpus": None, "act_modificator": None,
           "valoare_lege": None, "clasificare": None, "motiv": None, "indicii": subiecte}

    # ── actul declarat: e in corpus? e extractibil? ──────────────────────────────────────────────
    act = corp.act_din_url(url)
    if url and act is None:
        nex = corp.act_neextractibil(url)
        rez["clasificare"] = "NEGASIT"
        rez["motiv"] = ("actul declarat (%s) e in corpus dar NU e extractibil: %s - limita a "
                        "uneltei, nu absenta din lege"
                        % (url, corp.strat["neextractibile"][nex]["motiv"])) if nex else (
            "actul declarat (%s) nu exista in corpus" % url)
        rez["citare_rezolvata"] = False
        return rez

    if p["nume"] in OPERATIONALE:
        rez["clasificare"] = "NEGASIT"
        rez["motiv"] = ("parametru OPERATIONAL, nu fiscal: iConta insasi il declara regula de produs "
                        "fara act normativ de citat (core/test_constante_nesursate.py). Absenta e "
                        "asteptata, nu o lipsa de acoperire a corpusului.")
        return rez

    forme = forme_numar(p["valoare_cod"], fel) if fel != "alt" else set()

    indicii_stem = [_stemuri_indiciu(sb) for sb in subiecte]
    cuvinte_citat = _cuvinte_citat(temei["text_citat"]) if temei.get("text_citat") else []

    def _cu_subiect(atomi):
        return [a for a in atomi if _are_subiect(a, indicii_stem)] if subiecte else []

    # ── DECIZIA VINE DIN ACTUL DECLARAT, si numai de acolo ───────────────────────────────────────
    # ASA A TREBUIT SA FIE REFACUT, si de ce. Versiunea dinainte acumula niveluri de proba si CAUTA
    # VALOAREA IN FIECARE, pana in tot corpusul. Scopul era bun - reparase trei NEGASIT false - dar
    # efectul a fost ca a facut CONCORDA nefalsificabil: bancul de mutatii (`banc_mutatii.py`) a
    # injectat cinci greșeli cunoscute din istoria fiscala si TOATE CINCI au ieșit CONCORDA.
    #   - dividende 10% in loc de 16% -> "confirmat" pe `legea_141_2025_consolidat#artVII/alin2`
    #   - TVA 19% in loc de 21%       -> "confirmat" pe OUG 200/2008 (!), gasit in tot corpusul
    #   - salariu minim 4050 pe iulie 2026 -> "confirmat" pe HG 1506/2024, actul ABROGAT
    #   - cota micro 5%, care nu exista in niciun act -> "confirmat" pe CF art.481 alin.(2) lit.b)
    # Cauza e structurala, nu o scapare de reglaj: legislaţia fiscala romaneasca conţine aproape
    # orice procent si aproape orice suma pe undeva, deci o cautare care se intinde pana la ultimul
    # atom gaseste mereu o gazda pentru o valoare greșita. Un detector care nu poate produce DIFERA
    # face din "0 DIFERA" o propozitie fara conţinut.
    #
    # REGULA de acum: cand iConta declara un temei, verdictul se ia din ACTUL ACELA. Nu exista
    # salvare din alt act. Ce s-a pastrat din reparatia veche e strict necesarul - anume ca ANCORA
    # dintr-un act poate fi imprecisa (id cu sufix `~2`, valoare intr-un articol CITAT de un punct) -,
    # deci in interiorul actului declarat se coboara pe niveluri. Ce a dispărut cu totul sunt cele
    # doua niveluri care rescriau verdictul: "valoarea, gasita oriunde in actul declarat" (fara
    # subiect) si cautarea in tot corpusul pentru un parametru care ARE temei.
    #
    # UN NIVEL SE SARE DACA E NEINFORMATIV - adica nu poarta niciun numar de forma cerută. Un
    # articol-antet ca `legea_201_2025#artI` nu spune nimic despre sume, deci nu are dreptul sa
    # produca nici CONCORDA nici DIFERA; se trece la nivelul urmator. Dar primul nivel care POARTA
    # un numar decide, si de acolo nu se mai coboara: altfel o valoare greșita ar fi iar salvata de
    # un nivel mai slab.
    niveluri = []
    if act:
        atomi_act = corp.pe_act[act]
        if temei.get("art"):
            tinta = "%s#art%s" % (act, str(temei["art"]).replace(" ", ""))
            if temei.get("alin"):
                tinta += "/alin%s" % temei["alin"]
            pe_ancora = [a for a in atomi_act
                         if a["id"] == tinta or a["id"].startswith(tinta + "/")
                         or a["id"].startswith(tinta + "~")]
            if pe_ancora:
                niveluri.append((pe_ancora, "ancora pe articolul din Temei (%s)" % tinta, True))
        if temei.get("text_citat"):
            frag = _fragmente_citat(temei["text_citat"])
            pe_citat = [a for a in atomi_act if any(f in a["_n"] for f in frag)]
            if pe_citat:
                niveluri.append((pe_citat, "citatul declarat de iConta, gasit verbatim in actul "
                                           "declarat", True))
            else:
                cuv = _cuvinte_citat(temei["text_citat"])
                pe_cuvinte = _potrivire_pe_cuvinte(atomi_act, cuv)
                if pe_cuvinte:
                    niveluri.append((pe_cuvinte,
                                     "citatul declarat de iConta, potrivit pe cuvintele lui de "
                                     "conţinut (%d cuvinte, fara cifre) in actul declarat"
                                     % len(cuv), True))
        pe_subiect = _cu_subiect(atomi_act)
        if pe_subiect:
            niveluri.append((pe_subiect, "indiciu de subiect, in actul declarat (%s)" % act, True))
        if corp.structura.get(act) == "fragmente" and forme:
            pe_vecinatate = [a for a in atomi_act
                             if any(_valoare_langa_subiect(a, f, indicii_stem) for f in forme)]
            if pe_vecinatate:
                niveluri.append((pe_vecinatate,
                                 "valoarea in vecinatatea subiectului, in actul declarat (%s) - act "
                                 "FARA structura de articol, deci ancora slaba" % act, True))
    elif subiecte:
        # Niciun temei declarat: singurul drum e indiciul de subiect in tot corpusul. El NU poate
        # produce DIFERA (vezi mai jos) si se marcheaza ca ancora slaba in raport.
        pe_tot = _cu_subiect(corp.toti)
        if pe_tot:
            niveluri.append((pe_tot, "indiciu de subiect, CAUTAT IN TOT CORPUSUL", False))

    if not niveluri:
        rez["citare_rezolvata"] = False if url else None
        rez["clasificare"] = "NEGASIT"
        rez["motiv"] = (("actul declarat (%s) e in corpus, dar niciun atom al lui nu se potriveste "
                         "nici cu articolul citat, nici cu citatul iConta, nici cu subiectul "
                         "parametrului - citarea nu duce unde spune" % act) if act else
                        ("niciun atom din corpus nu poarta subiectul acestui parametru" if subiecte
                         else "parametrul nu are nici temei declarat de iConta, nici indiciu de "
                              "subiect - nu se poate interoga corpusul fara a inventa unul"))
        return rez

    for atomi_n, cum_n, in_act_n in niveluri:
        potrivite = [a for a in atomi_n if gaseste_forma(a["_n"], forme)]
        if potrivite and not in_act_n:
            # ANCORA SLABA (cautare in tot corpusul, parametru pe care iConta nu-l sursează): nu e de
            # ajuns ca atomul sa conţina fraza-subiect SI numarul. Intr-un atom mare ele pot fi la mii
            # de caractere una de alta, deci nu aparţin aceleiasi reguli. Masurat:
            # `_PCT_DEDUCERE_BAZA=0.20` a ieșit CONCORDA pe `og_16_2022#art77/alin14` - un alineat
            # despre impozitarea JOCURILOR DE NOROC -, iar `=0.35` pe un tabel dintr-o anexa de
            # formular. Cel corect din aceeasi familie, `PRAG_VENIT_DEDUCERE=2000`, are valoarea la 85
            # de caractere de fraza ("Deducerea personală de bază se acordă ... venit lunar brut de
            # până la 2.000 de lei"). Deci se cere VECINATATEA valorii cu subiectul, nu coexistenţa
            # lor in acelasi atom - un test care nu depinde de marimea atomului.
            potrivite = [a for a in potrivite
                         if any(_valoare_langa_subiect(a, f, indicii_stem) for f in forme)]
        if potrivite:
            # atomul pe care CITAREA il descrie; la egalitate, cel mai scurt - adica alineatul care
            # stabileste valoarea, nu articolul-parinte care o conţine din intamplare.
            a = _alege_atom(potrivite, cuvinte_citat)
            forma = gaseste_forma(a["_n"], forme)
            rez.update(_din_atom(a, forma))
            rez["valoare_lege"] = forma
            rez["ancora"] = cum_n
            rez["cum_gasit"] = cum_n
            rez["citare_rezolvata"] = in_act_n if url else None
            rez["clasificare"] = "CONCORDA"
            rez["motiv"] = "atomul poarta valoarea din cod, in forma legii, la nivelul: %s" % cum_n
            if cum_n != niveluri[0][1]:
                rez["nota"] = ("valoarea NU s-a gasit la nivelul cel mai tare de proba (%s), ci la "
                               "%s - citarea iConta duce la actul corect, dar nu exact la unitatea "
                               "care stabileste valoarea" % (niveluri[0][1], cum_n))
            return rez

        # nivelul nu poarta valoarea din cod. Poarta el VREUN numar de forma cerută?
        cu_numar = [(a, numere_din_text(a["_n"], fel)) for a in atomi_n]
        cu_numar = [(a, ns) for a, ns in cu_numar if ns]
        if not cu_numar:
            continue                  # nivel NEINFORMATIV: nu decide, se trece la urmatorul

        # DIFERA NU se pronunta pe un atom de FRAGMENT. Un fragment vine dintr-un act fara structura
        # de articol, deci nu se poate spune CE unitate de text e - iar cand actul e un tabel pe
        # coloane, textul lui e intretesut. Masurat: `tichet_masa_plafon@2025-04-01` (40,18 lei) a
        # ieșit DIFERA pe `anaf_limite_2025#frag23`, un fragment de tabel cu sapte numere lipite
        # ('15,18','20','20,01','20,09','20,17','30','35'), desi 40,18 chiar exista in act, in
        # fragmentul urmator. Un fragment poate confirma o valoare care e literal in el; nu poate
        # contrazice una.
        cu_numar = [(a, ns) for a, ns in cu_numar if a["nivel"] != "fragment"]
        if not cu_numar:
            continue

        # DIFERA se pronunta numai cand atomul vine din ACTUL DECLARAT de iConta. O potrivire pe
        # cuvinte in tot corpusul nu susţine "legea spune altceva" - vezi masuratoarea din antet.
        if not in_act_n:
            a = _alege_atom([x[0] for x in cu_numar], cuvinte_citat)
            ns = dict((id(x[0]), x[1]) for x in cu_numar)[id(a)]
            rez.update(_din_atom(a, ns[0]))
            rez["ancora"] = cum_n
            rez["clasificare"] = "NEGASIT"
            rez["motiv"] = ("s-a gasit un atom pe subiect, dar numai prin indiciu de cuvinte in tot "
                            "corpusul, fara temei declarat de iConta, si el poarta alta valoare "
                            "(%s) decat cea din cod (%s). O astfel de potrivire e prea slaba ca sa "
                            "susţina un verdict: se raporteaza NEGASIT, nu DIFERA."
                            % (ns[0], p["valoare_cod"]))
            return rez

        a = _alege_atom([x[0] for x in cu_numar], cuvinte_citat)
        ns = dict((id(x[0]), x[1]) for x in cu_numar)[id(a)]
        rez.update(_din_atom(a, ns[0]))
        rez["valoare_lege"] = ns[0] if len(ns) == 1 else ns
        rez["ancora"] = cum_n
        rez["cum_gasit"] = cum_n
        rez["citare_rezolvata"] = True if url else None
        rez["clasificare"] = "DIFERA"
        rez["motiv"] = ("atomul din actul declarat de iConta poarta un numar de aceeasi forma, dar "
                        "NU pe cel din cod (%s vs %s) - la nivelul: %s"
                        % (p["valoare_cod"], ns[0] if len(ns) == 1 else ns, cum_n))
        return rez

    # toate nivelurile au fost neinformative
    a = niveluri[0][0][0]
    rez.update(_din_atom(a))
    rez["ancora"] = niveluri[0][1]
    # citarea a dus la NISTE atomi, dar niciunul nu stabileste parametrul: deci nu s-a rezolvat.
    # `citare_rezolvata` inseamna "proba duce unde spune", nu "s-a gasit ceva in actul numit".
    rez["citare_rezolvata"] = False if url else None
    rez["clasificare"] = "NEGASIT"
    rez["motiv"] = ("atomii gasiti prin temeiul declarat nu poarta nicio valoare de forma cerută "
                    "(%s) - deci niciunul nu stabileste parametrul. Nu se caută in alte acte: "
                    "cand iConta declara un temei, verdictul se ia din actul acela." % fel)
    return rez


# ── termene: un termen se dovedeste pe FRAZA de scadenta, nu pe prezenta cifrei ──────────────────
# Prima versiune declara CONCORDA cand atomul purta subiectul SAU numarul, oriunde in actul declarat.
# Masurat, asta a confirmat greșit trei din cinci termene: `d301` cadea pe CF art.41 alin.(7) (plati
# anticipate de impozit pe profit), `d394` pe art.96 alin.(3) lit.c) din forma initiala ("ultima zi a
# lunii februarie"), iar `d406` pe definitia lui "declaratie informativa" din Codul de procedura.
# Un "25" intr-un alineat nu e un termen; fraza de scadenta e.
_FRAZA_TERMEN = [
    "pana la data de %s inclusiv", "data de %s inclusiv", "%s inclusiv a lunii",
    "pana la data de %s a lunii", "cel mai tarziu la data de %s",
]
_FRAZA_ULTIMA_ZI = ["ultima zi a lunii", "ultima zi calendaristica a lunii",
                    "pana in ultima zi a lunii"]


# Fraza de scadenta nu e de ajuns singura: "pana la data de 25 inclusiv a lunii urmatoare" apare in
# Codul fiscal de zeci de ori, pentru impozite diferite. Masurat, cel mai SCURT atom cu fraza era
# `art.68^2 alin.(4)` - impozit reţinut la sursa - pentru AMANDOUA declaraţiile de TVA, iar `d406`
# cadea pe un fragment din structura XML a lui D112 ("dataAng <= dataSf <= ultima zi a lunii"). Deci
# atomul trebuie sa fie si despre DEPUNEREA declaraţiei, si despre declaraţia CERUTA.
# Lista a fost largita dupa o masuratoare, nu dupa intuiţie: cu numai formele verbale ("se depune"),
# termenul lui D406 ieșea NEGASIT desi OPANAF 1783/2021 din corpus il scrie de doua ori - o data ca
# "termen de depunere - ultima zi a lunii care urmeaza perioadei..." si o data in enumerarea
# termenelor. Forma NOMINALA a depunerii era invizibila regulii.
_MARCAJ_DEPUNERE = [norm(x) for x in ("se depune", "depun la organele fiscale", "trebuie sa depuna",
                                      "trebuie să depună", "se completeaza si se depune",
                                      "termen de depunere", "termenul de depunere",
                                      "depunerea declaraţiei", "depunerea declaratiei")]
# numele declaraţiei in limbajul actului - indiciu de cautare, nu valoare
_NUME_DECLARATIE = {
    "d300": ["decont de taxa"],
    "d301": ["decont special de taxa", "decontul special"],
    "d390": ["declaratie recapitulativa", "declaraţia recapitulativă"],
    "d394": ["declaratie informativa privind livrarile", "declaraţia informativă privind livrările"],
    "d406": ["fisierul standard de control fiscal", "saf-t"],
    "d100": ["declaratie privind obligatiile de plata"],
    "d101": ["declaratie privind impozitul pe profit"],
    "d112": ["declaratie privind obligatiile de plata a contributiilor sociale"],
    "d205": ["declaratie informativa privind impozitul retinut"],
}


def _potriveste_termen(p, corp):
    temei = p["temei_declarat"] or {}
    act = corp.act_din_url(temei.get("url"))
    val = p["valoare_cod"]
    tip = p["id"].split("/")[-1]
    if val == "ultima_zi_luna":
        fraze = [norm(f) for f in _FRAZA_ULTIMA_ZI]
    else:
        fraze = [norm(f % val) for f in _FRAZA_TERMEN]
    nume_decl = [norm(x) for x in _NUME_DECLARATIE.get(tip, [])]
    citat = _fragmente_citat(temei["text_citat"]) if temei.get("text_citat") else []

    rez = {"parametru": p["id"], "clasa": "termen", "nume": p["nume"], "valoare_cod": val,
           "valabil_din_cod": None, "unde_in_cod": p["unde"],
           "temei_declarat_de_iconta": temei.get("text"), "citare_rezolvata": None,
           "atom": None, "atom_verbatim": None, "valabil_din_corpus": None,
           "act_modificator": None, "valoare_lege": None,
           "indicii": {"fraze_scadenta": fraze, "nume_declaratie": nume_decl}}

    def _cu_fraza(atomi):
        return [(a, f) for a in atomi for f in fraze if f in a["_n"]]

    niveluri = []
    if act:
        ats = corp.pe_act[act]
        if citat:
            pe_citat = [(a, f) for a, f in _cu_fraza(ats) if any(c in a["_n"] for c in citat)]
            if pe_citat:
                niveluri.append((pe_citat, "citatul declarat de iConta + fraza de scadenta, in %s"
                                 % act, True))
        pe_nume = [(a, f) for a, f in _cu_fraza(ats) if any(n in a["_n"] for n in nume_decl)]
        if pe_nume:
            niveluri.append((pe_nume, "numele declaratiei + fraza de scadenta, in %s" % act, True))
        pe_dep = [(a, f) for a, f in _cu_fraza(ats) if any(d in a["_n"] for d in _MARCAJ_DEPUNERE)]
        if pe_dep:
            niveluri.append((pe_dep, "marcaj de depunere + fraza de scadenta, in %s" % act, True))
    # Actele corpusului isi poarta declaraţia in NUME (`opanaf_2194_2025_d394`). Pentru termenele pe
    # care iConta nu le sursează, asta e indiciul cel mai tare disponibil - si e un indiciu de
    # CAUTARE, nu o valoare: verdictul tot din atom iese. Fara el, `d394` ieșea NEGASIT desi actul
    # lui spune limpede "Declaraţia se depune ... pana in data de 30 inclusiv" - textul nu repeta
    # titlul lung al declaraţiei, fiindca tot ordinul e despre ea.
    acte_ale_declaratiei = [b for b in corp.pe_act if tip in b.lower()]
    for b in acte_ale_declaratiei:
        pe_act_decl = [(a, f) for a, f in _cu_fraza(corp.pe_act[b])
                       if any(d in a["_n"] for d in _MARCAJ_DEPUNERE)]
        if pe_act_decl:
            niveluri.append((pe_act_decl,
                             "act dedicat declaratiei (%s) + depunere + fraza de scadenta" % b,
                             False))
    if nume_decl:
        pe_tot = [(a, f) for a, f in _cu_fraza(corp.toti)
                  if any(n in a["_n"] for n in nume_decl)
                  and any(d in a["_n"] for d in _MARCAJ_DEPUNERE)]
        if pe_tot:
            niveluri.append((pe_tot, "numele declaratiei + depunere + fraza, CAUTAT IN TOT CORPUSUL",
                             False))

    if niveluri:
        gasiti, unde, in_act = niveluri[0]
        a, f = min(gasiti, key=lambda t: len(t[0]["text"]))
        rez.update(_din_atom(a, val if val != "ultima_zi_luna" else "ultima zi"))
        rez["valoare_lege"] = val
        rez["ancora"] = unde
        rez["citare_rezolvata"] = in_act if act else None
        rez["clasificare"] = "CONCORDA"
        rez["motiv"] = "atomul poarta fraza de scadenta cu ziua din cod (%r), la: %s" % (f, unde)
        return rez

    rez["clasificare"] = "NEGASIT"
    rez["citare_rezolvata"] = False if act else None
    rez["motiv"] = ("niciun atom nu poarta SI fraza de scadenta cu ziua %s, SI numele declaratiei, "
                    "SI un marcaj de depunere. Fraza singura nu e o proba: ea apare de zeci de ori "
                    "in Codul fiscal, pentru impozite diferite. %s"
                    % (val, "iConta insasi noteaza acest termen ca NESURSAT in scadente.py."
                       if not temei else ""))
    return rez


# ── nomenclatoare: enumerarea din cod trebuie sa fie ENUMERATA de act ────────────────────────────
def _potriveste_nomenclator(p, corp):
    temei = p["temei_declarat"] or {}
    act = corp.act_din_url(temei.get("url"))
    valori = [v for v in (p["valoare_cod"] or "").split(",") if v]
    rez = {"parametru": p["id"], "clasa": "nomenclator", "nume": p["nume"],
           "valoare_cod": p["valoare_cod"], "valabil_din_cod": p["valabil_din_cod"],
           "unde_in_cod": p["unde"],
           "temei_declarat_de_iconta": " ".join(str(temei.get(k)) for k in ("tip", "nr", "an")
                                                if temei.get(k)) or None,
           "citare_rezolvata": None, "atom": None, "atom_verbatim": None,
           "valabil_din_corpus": None, "act_modificator": None, "valoare_lege": None,
           "indicii": valori}
    if p.get("deschis") or not valori:
        # iConta declara ea insasi ca norma NU inchide lista (`deschis=True`). Atunci setul din cod e
        # o inchidere CONSTRUITA de ei, nu o enumerare a actului - deci nu exista ce sa confirmi.
        # Nici DIFERA nu e: actul nu spune altceva, nu spune nimic. NEGASIT, cu motivul exact.
        rez["clasificare"] = "NEGASIT"
        rez["motiv"] = ("norma nu inchide lista - iConta o declara `deschis=True` in "
                        "nomenclatoare.py. Setul din cod e o inchidere construita de ei, nu o "
                        "enumerare a actului, deci nu exista enumerare de confirmat in corpus.")
        return rez
    atomi = corp.pe_act.get(act) if act else None
    for lot, unde in ([(atomi, "actul declarat (%s)" % act)] if atomi else []) + \
                     [(corp.toti, "CAUTAT IN TOT CORPUSUL")]:
        best, best_n = None, 0
        for a in lot:
            n = sum(1 for v in valori if re.search(r"\b%s\b" % re.escape(norm(v)), a["_n"]))
            if n > best_n or (n == best_n and best is not None and len(a["text"]) < len(best["text"])):
                best, best_n = a, n
        if best is None or best_n < max(2, int(0.8 * len(valori))):
            continue
        rez.update(_din_atom(best))
        rez["valoare_lege"] = "%d din %d valori enumerate in atom" % (best_n, len(valori))
        rez["ancora"] = "enumerarea, gasita in %s" % unde
        rez["citare_rezolvata"] = unde.startswith("actul declarat") if act else None
        rez["clasificare"] = "CONCORDA"
        rez["motiv"] = ("atomul ENUMERA %d din cele %d valori din cod (%s) - enumerarea actului, nu "
                        "doar subiectul lui" % (best_n, len(valori), unde))
        return rez
    rez["clasificare"] = "NEGASIT"
    rez["citare_rezolvata"] = False if act else None
    rez["motiv"] = ("niciun atom nu enumera cel putin %d din cele %d valori din cod (%s) - "
                    "prezenta subiectului nu e o enumerare"
                    % (max(2, int(0.8 * len(valori))), len(valori), ", ".join(valori)))
    return rez


def _potriveste_cont(p, plan):
    """Un simbol de cont se confrunta cu PLANUL DE CONTURI din OMFP 1802/2014, aflat in corpus."""
    simbol = p["valoare_cod"]
    rez = {"parametru": p["id"], "clasa": "cont", "nume": p["nume"],
           "valoare_cod": simbol, "valabil_din_cod": None, "unde_in_cod": p["unde"],
           "temei_declarat_de_iconta": None, "citare_rezolvata": None,
           "atom": None, "atom_verbatim": None, "valabil_din_corpus": None,
           "act_modificator": None, "valoare_lege": None, "ancora": "plan de conturi OMFP 1802/2014",
           "indicii": ["planul de conturi OMFP 1802/2014"]}
    intrare = plan.get(simbol)
    if intrare is None:
        rez["clasificare"] = "NEGASIT"
        rez["motiv"] = ("simbolul %s nu apare in planul de conturi din OMFP 1802/2014 asa cum e "
                        "extras din corpus (%d simboluri citite). ATENTIE: inventarul culege "
                        "simbolurile de cont euristic (literal de 3-4 cifre, folosit in >=3 locuri "
                        "din core/), deci e posibil ca literalul sa nu fie un cont - se raporteaza "
                        "ca negasit, nu se taie tacut." % (simbol, len(plan)))
        return rez
    rez["atom"] = intrare["atom"]
    rez["atom_verbatim"] = intrare["verbatim"]
    rez["valabil_din_corpus"] = intrare["valabil_din"]
    rez["valoare_lege"] = "%s %s%s" % (simbol, intrare["denumire"],
                                       " (%s)" % intrare["fel"] if intrare["fel"] else "")
    rez["clasificare"] = "CONCORDA"
    rez["motiv"] = ("contul exista in planul de conturi al OMFP 1802/2014, cu denumirea %r. "
                    "Un simbol de cont nu e o valoare numerica - ce se confirma e EXISTENTA lui in "
                    "nomenclator, nu o cifra." % intrare["denumire"])
    return rez


_FEREASTRA = 1200


def _fereastra_verbatim(text, forma):
    """Fragmentul verbatim, CENTRAT pe valoarea citata - nu primele 1200 de caractere.

    Un atom de plan sau un alineat lung depaseste fereastra, si valoarea poate sta dupa taietura:
    masurat, 7 din 204 CONCORDA citau un fragment care NU contine valoarea raportata. Un citat care
    nu arata ce pretinde nu e o proba, e o afirmaţie - exact ce interzice CLAUDE.md §2.
    """
    if len(text) <= _FEREASTRA:
        return text
    i = text.find(forma) if forma else -1
    if i < 0:
        return text[:_FEREASTRA]
    j = max(0, i - _FEREASTRA // 3)
    return ("…" if j else "") + text[j:j + _FEREASTRA] + "…"


def _din_atom(a, forma=None):
    return {"atom": a["id"], "atom_verbatim": _fereastra_verbatim(a["text"], forma),
            "valabil_din_corpus": a["valabil_din"],
            "act_modificator": (a["modificat_de"][0]["nota"] if a["modificat_de"] else None),
            "atom_abrogat": a["abrogat"],
            "atom_nivel": a["nivel"], "atom_linie": a["linie"]}


def potriveste_tot():
    t0 = time.time()
    inv = json.load(open(os.path.join(_RAD, "artefacte", "inventar_iconta.json"), encoding="utf-8"))
    corp = Corpus()
    plan = plan_de_conturi(corp)
    rez = [potriveste(p, corp, plan) for p in inv["parametri"]]
    sumar = {}
    for r in rez:
        sumar[r["clasificare"]] = sumar.get(r["clasificare"], 0) + 1
    raport = {"_ce": "OP6+OP7 potrivire si clasificare. Fiecare CONCORDA/DIFERA citeaza id-ul "
                     "atomului si fragmentul verbatim (CLAUDE.md §2).",
              "facut_la": time.strftime("%Y-%m-%dT%H:%M:%S"),
              "n_parametri": len(rez), "sumar": sumar,
              "citari_declarate": sum(1 for r in rez if r["citare_rezolvata"] is not None),
              "citari_rezolvate": sum(1 for r in rez if r["citare_rezolvata"] is True),
              "n_atomi_corpus": len(corp.toti),
              "n_conturi_in_plan_din_corpus": len(plan),
              "potriviri": rez, "secunde": round(time.time() - t0, 2)}
    with open(os.path.join(_RAD, "artefacte", "potriviri.json"), "w", encoding="utf-8") as f:
        json.dump(raport, f, ensure_ascii=False, indent=1, sort_keys=True)
    return raport


if __name__ == "__main__":
    r = potriveste_tot()
    print("potrivire: %d parametri -> %s | citari declarate %d, rezolvate %d | %.1f s"
          % (r["n_parametri"], r["sumar"], r["citari_declarate"], r["citari_rezolvate"],
             r["secunde"]))
