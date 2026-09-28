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
        p = d * 100 if d < 1 else d
        p = p.normalize()
        intreg = int(p)
        zecimal = format(p, "f").rstrip("0").rstrip(".")
        for baza in {str(intreg), zecimal, format(p, "f")}:
            b = baza.replace(".", ",")
            forme.add(b + "%")
            forme.add(b + " %")
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
    return [m.group(1) for m in rx.finditer(text_norm)]


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
    # termene
    "termen_depunere_d300": ["pana la data de 25 inclusiv a lunii urmatoare"],
    "termen_depunere_d301": ["pana la data de 25 inclusiv a lunii urmatoare"],
    "termen_depunere_d390": ["pana la data de 25 inclusiv", "declaratie recapitulativa"],
    "termen_depunere_d394": ["declaratie informativa", "pana la data de 30 inclusiv"],
    "termen_depunere_d406": ["fisierul standard de control fiscal", "saf-t"],
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
    "PRAG_IMCA_EUR": ["cifra de afaceri", "50.000.000 euro"],
    "IMPOZIT_ANUAL": ["impozit anual"],
    "COTE": ["cota"],
    "_PCT_DEDUCERE_BAZA": ["deducere personala"],
    "DEDUCERE_COPIL_SCOALA": ["deducere personala suplimentara"],
    "PRAG_VENIT_DEDUCERE": ["deducere personala", "salariul de baza minim brut"],
    "PLAFON_EUR": ["15.000 euro", "activitati economice"],
    "PRAG_ELECTRONICE": ["taxare inversa", "telefoane mobile", "dispozitive cu circuite integrate"],
    "PRAG_BRENT_USD": ["brent", "petrol"],
}
# parametri OPERATIONALI, nu fiscali: iConta insasi scrie, in `test_constante_nesursate.py`, ca sunt
# "o regula de produs (cate esecuri, in cate minute), fara act normativ de citat". NU li se cauta
# temei - dar nici nu se ascund: ies NEGASIT cu acest motiv, ca sa se vada ca absenta e asteptata.
OPERATIONALE = {"PRAG_ESECURI", "PRAG_RITM", "PRAG_VECHIME_ZILE", "PRAG_ATENTIE",
                "PRAG_URMARIT_ZILE", "PRAG_ZILE", "PRAGURI", "DOAR_VENITURI", "MOD_VENIT_NET"}


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


def potriveste(p, corp, plan=None):
    if p["clasa"] == "cont":
        return _potriveste_cont(p, plan or {})
    fel = _fel(p)
    temei = p["temei_declarat"] or {}
    url = temei.get("url")
    subiecte = [norm(s) for s in SUBIECT.get(p["nume"], [])]
    if not subiecte and temei.get("text_citat"):
        subiecte = _fragmente_citat(temei["text_citat"])[:3]

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

    def _cu_subiect(atomi):
        return [a for a in atomi if any(sb in a["_n"] for sb in subiecte)] if subiecte else []

    # ── NIVELURILE DE PROBA, in ordine descrescatoare de forta ───────────────────────────────────
    # DE CE SE ACUMULEAZA si nu se opreste la primul nivel nevid. Prima versiune se oprea, si a
    # produs trei NEGASIT false pe valori care ERAU in corpus:
    #   - `cass` 10% sta in `#art156~2` (sufixul `~2` apare cand acelasi id revine - cuprins vs corp);
    #     ancora `#art156` nu-l cuprindea, si cautarea se oprea acolo.
    #   - `facilitate_salariu_minim` 200 lei sta in `oug_89_2025#artIII~2/alin4`, nu in `#artIII`.
    #   - `tichet_masa_plafon` 45 lei sta in articolul CITAT de pct. 1 al art. I din Legea 201/2025,
    #     deci nu sub id-ul articolului citat de iConta.
    # Un NEGASIT fals e la fel de grav ca o valoare inventata: amandoua mint despre corpus. Deci se
    # incearca toate nivelurile din ACTUL DECLARAT, si se raporteaza nivelul la care valoarea a fost
    # chiar gasita - inclusiv cand el e mai slab decat cel declarat, fiindca ASTA e informatia.
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
                niveluri.append((pe_citat, "citatul declarat de iConta, gasit in actul declarat", True))
        pe_subiect = _cu_subiect(atomi_act)
        if pe_subiect:
            niveluri.append((pe_subiect, "indiciu de subiect, in actul declarat (%s)" % act, True))
        if forme:
            pe_valoare = [a for a in atomi_act if gaseste_forma(a["_n"], forme)]
            if pe_valoare:
                niveluri.append((pe_valoare, "valoarea, gasita in actul declarat (%s)" % act, True))
    if subiecte:
        pe_tot = _cu_subiect(corp.toti)
        if pe_tot:
            niveluri.append((pe_tot, "indiciu de subiect, CAUTAT IN TOT CORPUSUL", False))

    rez["citare_rezolvata"] = bool(niveluri and niveluri[0][2] and url) if url else None

    if not niveluri:
        rez["clasificare"] = "NEGASIT"
        rez["motiv"] = ("niciun atom din corpus nu poarta subiectul acestui parametru" if subiecte
                        else "parametrul nu are nici temei declarat de iConta, nici indiciu de "
                             "subiect - nu se poate interoga corpusul fara a inventa unul")
        return rez

    candidati, cum, in_actul_declarat = niveluri[0]

    if fel == "alt":
        # Un articol-antet (`opanaf_705_2020_d390#art5`) are textul in COPII, deci el insusi e gol.
        # Masurat: doua nomenclatoare citau un verbatim de zero caractere. Se alege primul candidat
        # care poarta text; daca niciunul nu poarta, se spune, nu se citeaza golul.
        cu_text = [a for a in candidati if len(a["text"]) >= 40]
        a = (cu_text or candidati)[0]
        rez.update(_din_atom(a))
        rez["clasificare"] = "CONCORDA"
        rez["motiv"] = ("atomul poarta subiectul; parametrul nu e o valoare numerica comparabila "
                        "(termen/nomenclator/cont) - se confirma temeiul, nu o cifra")
        return rez

    for atomi_n, cum_n, in_act_n in niveluri:
        potrivite = [a for a in atomi_n if gaseste_forma(a["_n"], forme)]
        if not potrivite:
            continue
        # cel mai SCURT atom care poarta valoarea: alineatul care o stabileste, nu articolul-parinte
        # care o contine din intamplare.
        a = min(potrivite, key=lambda x: len(x["text"]))
        forma = gaseste_forma(a["_n"], forme)
        rez.update(_din_atom(a, forma))
        rez["valoare_lege"] = forma
        rez["ancora"] = cum_n
        rez["cum_gasit"] = cum_n
        rez["clasificare"] = "CONCORDA"
        rez["motiv"] = "atomul poarta valoarea din cod, in forma legii, la nivelul: %s" % cum_n
        if cum_n is not cum:
            rez["nota"] = ("valoarea NU s-a gasit la nivelul cel mai tare de proba (%s), ci la %s - "
                           "citarea iConta duce la actul corect, dar nu exact la unitatea care "
                           "stabileste valoarea" % (cum, cum_n))
        return rez

    # ── DIFERA e o AFIRMATIE TARE: "legea spune altceva". Ea cere o ANCORA TARE - adica citarea
    # declarata de iConta sa se fi rezolvat la un articol sau la citatul lor. Masurat: fara aceasta
    # conditie, cele 7 "DIFERA" produse erau TOATE false pozitive - un indiciu de doua-trei cuvinte
    # ("deducere personala") cautat in 46.000 de atomi prinde un alineat intamplator din OPANAF
    # 605/2026, si raportul ar fi pus "legea zice 3,5" langa "codul zice 0,20". Un parametru pe care
    # iConta nu-l sursează deloc nu poate produce o divergenta dovedita; el produce NEGASIT, cu
    # motivul scris. Asta e chiar regula 5 din CLAUDE.md: nicio valoare inventata.
    # DIFERA e defensabil numai cand atomul vine din ACTUL DECLARAT de iConta. O potrivire pe
    # cuvinte in tot corpusul nu susţine "legea spune altceva" - vezi masuratoarea din antet.
    ancora_tare = in_actul_declarat
    cu_numar = [(a, numere_din_text(a["_n"], fel)) for a in candidati] if ancora_tare else []
    cu_numar = [(a, ns) for a, ns in cu_numar if ns]
    if cu_numar:
        a, ns = min(cu_numar, key=lambda t: len(t[0]["text"]))
        rez.update(_din_atom(a, ns[0]))
        rez["valoare_lege"] = ns[0] if len(ns) == 1 else ns
        rez["clasificare"] = "DIFERA"
        rez["motiv"] = ("atomul poarta subiectul, dar numarul din textul legii nu e cel din cod "
                        "(vezi ambele parti)")
        return rez

    a = candidati[0]
    rez.update(_din_atom(a))
    rez["clasificare"] = "NEGASIT"
    rez["motiv"] = (("citarea declarata de iConta s-a rezolvat, dar atomul nu poarta nicio valoare "
                     "de forma ceruta (%s) - deci nu el stabileste parametrul" % fel)
                    if ancora_tare else
                    ("s-a gasit un atom pe subiect, dar numai prin indiciu de cuvinte in tot "
                     "corpusul, fara temei declarat de iConta. O astfel de potrivire e prea slaba "
                     "ca sa susţina un verdict: se raporteaza NEGASIT, nu DIFERA."))
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
