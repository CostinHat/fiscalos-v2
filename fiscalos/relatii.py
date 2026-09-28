# -*- coding: utf-8 -*-
"""C17 — RELATIA STRUCTURALA intre atomi: "deroga de la / prin exceptie de la / modifica".

DECIZIA ARHITECTULUI: ambele cai, pe o baza comuna - relatia extrasa din text. (a) cautarea aduce in
context atomii care modifica sau deroga de la atomul gasit, valabili la data intrebarii; (b) plasa de
siguranta mecanica: daca in context exista un atom valabil care deroga de la cel citat si raspunsul nu-l
trateaza, raspunsul devine abţinere.

DE CE. Singura clasa de greseala reala a stratului semantic v1: o regula generala citata literal, dar
inlocuita pentru cazul din intrebare de o regula speciala - "Prin exceptie de la prevederile alin. (8),
plata anticipata pentru trimestrul I ..." (CF art. 41 alin. (10^1)). Verificarea literala nu o putea
prinde, fiindca citatul era adevarat. Relatia o face vizibila: e scrisa in textul legii.

CE SE EXTRAGE. Din textul fiecarui atom:
  derogare   "prin derogare de la (prevederile) art. X alin. (Y) din <act>"
  exceptie   "prin exceptie de la (prevederile) alin. (Y)" - fara act numit: actul sursei
  modificare punctele actelor modificatoare: "La articolul X, alineatul (Y) se modifica"
Tinta e (act, articol, alineat); alineat None = tot articolul. O trimitere pe care nu o pot rezolva
("aceste prevederi") se numara, nu se ghiceste.

CE NU CONTEAZA CA SURSA: textul istoric (`forma_initiala`, `_pre_`), textul CITAT intr-un act
modificator (articol arab intr-un act cu articole proprii romane - instantaneul Codului din ziua
modificarii), un atom abrogat, o sursa nenormativa. Altfel, Codul din 2015 ar "deroga" de la cel din
2026. O MODIFICARE conteaza numai daca e mai noua decat ultima nota de consolidare a actului-tinta:
altfel e deja in textul consolidat.
"""
import re

from fiscalos import surse

_DECLANSATOR = re.compile(
    r"(prin derogare de la|în derogare de la|in derogare de la|prin excepție de la|prin excepţie de la|"
    r"prin exceptie de la)\s+(?:(?:prevederile|dispozițiile|dispoziţiile|dispozitiile)\s+)?", re.I)
_ELEMENT = re.compile(
    r"\s*(?:(?:ale|și|şi|si|,|precum și)\s*)*(art\.|articolul|alin\.|alineatul|lit\.|litera|pct\.)\s*"
    r"(\(?\s*[\dIVXLCDM]+(?:\^\d+)?\s*\)?(?:\s*[-–]\s*\(?\s*\d+(?:\^\d+)?\s*\)?)?"
    r"(?:\s*(?:și|şi|si|,)\s*\(\s*\d+(?:\^\d+)?\s*\))*)", re.I)
_DIN = re.compile(
    r"\s*din\s+(Legea\s+nr\.\s*[\d.]+/\d{4}|Ordonan[tţț]a de urgen[tţț][aă][^,;.]{0,40}?nr\.\s*[\d.]+/\d{4}|"
    r"Ordonan[tţț]a Guvernului\s+nr\.\s*[\d.]+/\d{4}|Hot[aă]r[aâ]rea Guvernului\s+nr\.\s*[\d.]+/\d{4}|"
    r"Codul fiscal|Codul de procedur[aă] fiscal[aă]|Codul muncii|prezentul cod|prezenta lege|"
    r"prezenta ordonan[tţț][aă][^,;.]{0,20}|prezentul titlu|prezentul capitol)", re.I)
_MODIF = re.compile(
    r"^\s*(?:La\s+)?articolul\s+(\d+(?:\^\d+)?)\s*(?:,\s*|\s+)?(?:alineatul\s+\((\d+(?:\^\d+)?)\))?"
    r"[^.]{0,120}?se\s+(?:modific[aă]|abrog[aă]|completeaz[aă])", re.I)


def _nums(s):
    """"(1)-(3)" -> ['1','2','3']; "(1) si (2)" -> ['1','2']; "28" -> ['28']."""
    s = s.replace("–", "-")
    m = re.match(r"\(?\s*(\d+)\s*\)?\s*-\s*\(?\s*(\d+)\s*\)?$", s.strip())
    if m and int(m.group(2)) - int(m.group(1)) < 30:
        return [str(k) for k in range(int(m.group(1)), int(m.group(2)) + 1)]
    return re.findall(r"\d+(?:\^\d+)?|[IVXLCDM]+", s)


def _act_numit(corp, text, sursa):
    if not text:
        return sursa["act"]
    t = text.lower()
    if t.startswith(("prezent",)):
        return sursa["act"]
    if "codul fiscal" in t:
        return "cod_fiscal_227_2015_consolidat"
    if "procedur" in t:
        return "legea_207_2015_consolidat"
    if "codul muncii" in t:
        return "legea_53_2003_codul_muncii"
    m = re.search(r"nr\.\s*([\d.]+)/(\d{4})", text)
    if not m:
        return None
    nr, an = m.group(1).replace(".", ""), m.group(2)
    if (nr, an) == ("227", "2015"):
        return "cod_fiscal_227_2015_consolidat"
    if (nr, an) == ("207", "2015"):
        return "legea_207_2015_consolidat"
    cand = sorted((b for b in corp.pe_act if "_%s_%s" % (nr, an) in b and "forma_initiala" not in b),
                  key=lambda b: ("consolidat" not in b, len(b)))
    return cand[0] if cand else None


def _sursa_valida(corp, a):
    act = a["act"]
    if a.get("abrogat") or "forma_initiala" in act or "_pre_" in act:
        return False
    if not surse.e_act_normativ(act)[0]:
        return False
    if act in corp.modificatoare and a.get("articol") and str(a["articol"])[:1].isdigit():
        return False                                  # text citat intr-un act modificator
    return True


def _ultima_nota(corp, act):
    d = [x["valabil_din"] for x in corp.pe_act.get(act, []) if x.get("valabil_din")]
    return max(d) if d else None


class Relatii(object):
    """Indexul relatiilor: tinta (act, articol, alineat) -> [muchii]."""

    def __init__(self, corp):
        self.corp = corp
        self.muchii, self.nerezolvate = [], 0
        self.pe_tinta = {}
        for a in corp.toti:
            if not _sursa_valida(corp, a):
                continue
            for m in _DECLANSATOR.finditer(a["text"]):
                self._din_trimitere(a, m)
            if a["nivel"] == "punct" and a.get("interventie"):
                self._din_modificare(a)
        for e in self.muchii:
            self.pe_tinta.setdefault((e["tinta_act"], e["tinta_art"]), []).append(e)

    def _adauga(self, a, fel, act, art, alin, fragment):
        if not act or not art or act not in self.corp.pe_act:
            self.nerezolvate += 1
            return
        self.muchii.append({"sursa": a["id"], "fel": fel, "tinta_act": act, "tinta_art": str(art),
                            "tinta_alin": str(alin) if alin else None,
                            "fragment": " ".join(fragment.split())[:240],
                            "valabil_din": a.get("valabil_din")})

    def _din_trimitere(self, a, m):
        fel = "exceptie" if "excep" in m.group(1).lower() else "derogare"
        rest = a["text"][m.end():m.end() + 260]
        elemente, poz = [], 0
        while True:
            e = _ELEMENT.match(rest, poz)
            if not e:
                break
            elemente.append((e.group(1).lower(), e.group(2)))
            poz = e.end()
        if not elemente:
            self.nerezolvate += 1
            return
        dn = _DIN.match(rest, poz)
        act = _act_numit(self.corp, dn.group(1) if dn else None, a)
        if act == a["act"] and a["act"] in self.corp.modificatoare:
            act = surse.tinta_modificarii(self.corp, a)[1] or act
        art_cur = a.get("articol") if act == a["act"] else None
        tinte = []
        for tip, val in elemente:
            if tip.startswith("art"):
                for n in _nums(val):
                    art_cur = n
                    tinte.append([n, None])
            elif tip.startswith("alin"):
                ns = _nums(val)
                if tinte and tinte[-1][0] == art_cur and tinte[-1][1] is None:
                    tinte.pop()
                for n in ns:
                    tinte.append([art_cur, n])
        fragment = a["text"][m.start():m.end() + poz + (dn.end() - poz if dn else 0)]
        for art, alin in tinte:
            self._adauga(a, fel, act, art, alin, fragment)

    def _din_modificare(self, a):
        m = _MODIF.match(a["text"])
        if not m:
            return
        _nume, act = surse.tinta_modificarii(self.corp, a)
        d_sursa = a.get("valabil_din") or ("%s-01-01" % re.search(r"_(\d{4})", a["act"]).group(1)
                                           if re.search(r"_(\d{4})", a["act"]) else None)
        d_tinta = _ultima_nota(self.corp, act) if act else None
        # o modificare deja consolidata in actul-tinta nu mai e o relatie activa
        if d_sursa and d_tinta and d_sursa <= d_tinta:
            return
        self._adauga(a, "modificare", act, m.group(1), m.group(2), a["text"][:200])

    def asupra(self, atom, data_ref=None):
        """Muchiile care DEROGA DE LA / MODIFICA atomul dat, cu sursa valabila la data_ref."""
        art = atom.get("articol")
        if not art:
            return []
        alin = atom.get("alineat")
        ies = []
        for e in self.pe_tinta.get((atom["act"], str(art)), []):
            if e["tinta_alin"] and alin and e["tinta_alin"] != str(alin):
                continue
            if e["sursa"] == atom["id"]:
                continue
            if data_ref and e["valabil_din"] and e["valabil_din"] > data_ref:
                continue
            ies.append(e)
        return ies
