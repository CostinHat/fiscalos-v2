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

v5 (deciziile C23, C25, C27, C28, C29, dupa rularea v4):
  C23  campul `raspuns` e validat STRUCTURAL inainte de verificare: nu gol, nu "x"/"-", fara marcaj de
       parametri scurs ("</declaratie><parameter name=...>"), nu continutul altui camp. La esec: O
       singura reincercare, apoi abtinere cu motivul scris.
  C25  fiecare operand are o ETICHETA: FAPT_CAZ (din intrebare; acceptat numai daca valoarea apare
       literal in intrebare) sau VALOARE_LEGALA (din atom; cere atom aratat si fragment verbatim).
  C27  data de referinta se stabileste pentru FAPTUL intrebat si se declara in raspuns. Cand intrebarea
       poarta mai multe date, modelul alege una dintre ele si spune de ce; daca nu reiese la care se
       refera faptul, raspunsul e INCOMPLET - nu cea mai veche data.
  C28  calculul se afiseaza pas cu pas: fiecare formula cu valorile puse in ea, fiecare zile(a, b).
  C29  limita e 20 de pasi; o cerere peste limita = abtinere, cu traseul navigarii.
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
MAX_PASI = 20
MAX_TEXT = 3500

SISTEM = semantic.SISTEM.replace(
    "Primești o întrebare de fiscalitate românească, data de referință la care trebuie să fie valabil "
    "răspunsul și un set de ATOMI: fragmente de acte normative, fiecare cu un id. Atomii au fost aleși "
    "de o căutare mecanică și sunt, toți, în vigoare la data de referință.",
    "Primești o întrebare de fiscalitate românească și data de referință la care trebuie să fie valabil "
    "răspunsul. Atomii (fragmente de acte normative, fiecare cu un id) NU îi primești gata aleși: îi "
    "găsești singur, navigând.") + """

NAVIGARE. Ai trei unelte:
- `cauta(interogare)` — căutare lexicală; e doar un PUNCT DE INTRARE, nu răspunsul.
- `cuprins(act, filtru)` — structura unui act: titlurile/capitolele, articolele și ANEXELE lui; cu \\
`filtru`, numai articolele (cu denumirea marginală) și punctele de anexă care conțin cuvintele date. \\
Anexele (norme metodologice, reglementări contabile, instrucțiuni de formular) au id-uri proprii \\
(`act#anexa/pct238/alin2`) și se citează ca atare.
- `deschide(id)` — textul unui atom, părintele, copiii (alineate, litere, puncte) și RELAȚIILE lui: \\
atomii care derogă de la el, fac excepție de la el sau îl modifică, și cei de la care derogă el.
Ai cel mult %d pași de navigare; fiecare rezultat îți spune câți au rămas. O cerere peste limită \\
încheie întrebarea cu abținere. Navighează ca un contabil: găsește actul și articolul potrivit prin \\
structură, deschide-l, urmează relațiile lui de derogare, apoi răspunde. Poți cita numai atomi pe care \\
o unealtă ți i-a arătat.

DATA DE REFERINȚĂ (C27). Data se stabilește pentru FAPTUL ÎNTREBAT. Primești datele pe care le poartă \\
întrebarea (`date_din_intrebare`). Dacă e una singură, ea e data. Dacă sunt mai multe, alegi pe cea la \\
care se referă faptul întrebat (de ex. „cifra de afaceri 2025 … cât impozit datorează pentru 2026" → \\
faptul întrebat e impozitul pentru 2026) și o scrii în `data_referinta` (AAAA-LL-ZZ, exact una dintre \\
cele primite), cu motivul în `data_referinta_motiv`. Dacă nu reiese la care dată se referă faptul, \\
răspunzi INCOMPLET — nu alegi data cea mai veche. Unealtele îți arată atomii în vigoare la cea mai \\
recentă dintre date; citezi numai atomi în vigoare la data aleasă.

RĂSPUNSUL FINAL (C44). Când ai terminat navigarea, NU mai apela unelte: scrie un rând scurt („Gata.”). \\
Tura următoare îți cere răspunsul final, în format structurat; acolo fiecare câmp își conține numai \\
propriul text (răspunsul complet în `raspuns`, niciodată gol).

TERMENE (C40). Orice termen calendaristic din răspuns (o dată până la care se depune, se plătește, se \\
face ceva) se calculează cu termen_efectiv și intră în răspuns ca {nume} — un termen scris direct \\
(„31 mai”, „25 iunie a anului următor”, „15.06.2026”) e respins.

TEMEIUL ALĂTURAT (C41). Dacă printre atomii pe care i-ai văzut există unul cu text aproape identic cu \\
un atom pe care îl citezi (altă condiție, același final), scrie în `alegeri_temei` de ce l-ai ales pe \\
al tău: `atom` (cel citat), `alternativa` (celălalt), `conditie` = fragmentul literal din atomul tău care \\
îi descrie subiectul/condiția și care NU e în alternativă. `deschide` îți arată geamenii ca id + temei; \\
deschide-i dacă ai nevoie de text. Un geamăn nejustificat al atomului decisiv apare ca avertisment.

CONSECINȚA CUANTIFICATĂ (C43). Când legea cuantifică consecința faptului întrebat (cauțiune, amendă, \\
prag, penalitate), răspunsul o dă — calculată, cu temeiul ei citat — chiar dacă întrebarea e de tip \\
„are dreptate?” / „este legal?”.

CIFRELE (C46). Orice cifră din răspuns e fie citată literal (dintr-un atom sau din întrebare), fie \\
rezultatul unui calcul, pus ca {nume}.

CALCUL. Nu calculezi. Dacă răspunsul cere un calcul, îl descrii în `calcule`: fiecare calcul are un \\
`nume`, o `formula` (numai numele operanzilor și ale calculelor anterioare, + - * / paranteze, \\
min(), max(), zile(data1, data2) = numărul de zile de la data1 la data2, data(zi, lună, an), data + N \\
zile, termen_efectiv(data) = ziua în care expiră efectiv un termen care cade într-o zi nelucrătoare) și \\
lista de `operanzi`. termen_efectiv cere să CITEZI atomul regulii prelungirii termenului (Codul de \\
procedură civilă art. 181 alin. (2), la care trimite CPF art. 75) și atomul listei sărbătorilor legale \\
(Codul muncii art. 139 alin. (1)); codul calculează zilele nelucrătoare numai din ele. \\
Fiecare operand are `valoare` scrisă exact ca în sursă (ex. "21%%", "100.000", "25.03.2026") și o \\
`eticheta` (C25): FAPT_CAZ — o valoare a cazului, luată din întrebare (`atom` gol, `fragment` = bucata \\
din întrebare care o conține); sau VALOARE_LEGALA — o cotă, un plafon, un termen, o limită, luată dintr-un \\
atom (`atom` = id-ul, `fragment` = bucata literală din atom). O valoare legală nu e niciodată FAPT_CAZ, \\
chiar dacă întrebarea o repetă. Singurele constante permise fără sursă sunt 1 și 100. În `raspuns` pui \\
rezultatul unui calcul ca {nume}; codul îl evaluează, îl înlocuiește și afișează calculul pas cu pas. \\
Un număr scris în litere în atom („cinci ani”, „o cincime”, „jumătate”) e operand valid cu `valoare` \\
exact ca în atom („cinci”, „cincime”); la fel un ordinal („15-a”) sau o cifră cu unitate („60 de zile”) \\
(C51). Un operand scris cu „%%” valorează deja fracțiunea (21%% = 0,21): nu-l mai împărți la 100 (C50). \\
Fiecare VALOARE_LEGALA are `data_aplicarii` (AAAA-LL-ZZ): data la care legea cere valoarea pentru \\
faptul întrebat (de ex. „salariul minim în vigoare la 1 ianuarie”), sau "" dacă e data de referință. \\
Codul respinge o valoare care nu era în vigoare la acea dată (C55).""" % MAX_PASI

_CALC = {"type": "array", "items": {"type": "object", "properties": {
    "nume": {"type": "string"}, "formula": {"type": "string"},
    "operanzi": {"type": "array", "items": {"type": "object", "properties": {
        "nume": {"type": "string"}, "valoare": {"type": "string"},
        "eticheta": {"type": "string", "enum": ["FAPT_CAZ", "VALOARE_LEGALA"]},
        "atom": {"type": "string"}, "fragment": {"type": "string"}, "data_aplicarii": {"type": "string"}},
        "required": ["nume", "valoare", "eticheta", "atom", "fragment", "data_aplicarii"],
        "additionalProperties": False}}},
    "required": ["nume", "formula", "operanzi"], "additionalProperties": False}}
SCHEMA = json.loads(json.dumps(semantic.SCHEMA))
SCHEMA["properties"]["calcule"] = _CALC
SCHEMA["properties"]["alegeri_temei"] = {"type": "array", "items": {"type": "object", "properties": {
    "atom": {"type": "string"}, "alternativa": {"type": "string"}, "conditie": {"type": "string"}},
    "required": ["atom", "alternativa", "conditie"], "additionalProperties": False}}
SCHEMA["properties"]["data_referinta"] = {"type": "string"}
SCHEMA["properties"]["data_referinta_motiv"] = {"type": "string"}
SCHEMA["required"] = SCHEMA["required"] + ["calcule", "alegeri_temei", "data_referinta", "data_referinta_motiv"]

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
]


# ── uneltele, executate de cod ───────────────────────────────────────────────────────────────────
class Navigator(object):
    def __init__(self, idx, rel, data_ref):
        self.idx, self.rel, self.data_ref = idx, rel, data_ref
        self.corp = idx.corp
        self.vazuti = {}                      # id -> atom: tot ce i s-a aratat modelului
        self.relatie = {}                     # sursa -> [(fel, tinta)] aratate modelului (C17 b)
        self.pasi = []
        self._schinduri_act = {}

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
        # C26: anexele si punctele lor de prim nivel sunt unitati navigabile, ca articolele
        anexe = [a for a in self.corp.pe_act[act] if a["nivel"] == "anexa" and self._valid(a)]
        id_anexe = {a["id"] for a in anexe}
        pct_anexa = [a for a in self.corp.pe_act[act] if a.get("parinte") in id_anexe
                     and a["nivel"] == "punct" and self._valid(a)]
        if not filtru.strip():
            for a in anexe:
                self._vede(a)
            # in ordinea actului: fiecare portiune continua sub acelasi titlu/capitol
            grupe = []
            for a in ats:
                t = a.get("titlu_structural") or "(fara titlu)"
                if not grupe or grupe[-1][0] != t:
                    grupe.append((t, []))
                grupe[-1][1].append(a["cheie"])
            return {"act": act, "sursa": self.corp.sursa_act.get(act, {}).get("sursa"),
                    "nota": "pentru denumirile articolelor si punctele anexelor, cere `cuprins` cu un filtru",
                    "titluri": [{"titlu": t, "articole": "%s..%s (%d)" % (v[0], v[-1], len(v))}
                                for t, v in grupe[:120]],
                    "anexe": [{"id": a["id"], "titlu": " ".join(a["text"].split())[:120],
                               "puncte": sum(1 for x in pct_anexa if x["parinte"] == a["id"])}
                              for a in anexe[:60]]}
        st = set(intrebari._stemuri(intrebari._extinde(filtru)))
        ies = []
        for a in ats:
            den = " ".join(a["text"].split())[:160] if len(a["text"]) <= 250 else ""
            ctx = potrivire.norm(den + " " + (a.get("titlu_structural") or ""))
            n = sum(1 for x in st if x in ctx)
            if n:
                ies.append((n, a, den))
        for a in pct_anexa:
            inc = " ".join(a["text"].split())[:160]
            if not inc:                                  # "238." / "- (1) ...": inceputul e in copil
                copil = next((x for x in self.corp.pe_act[act] if x.get("parinte") == a["id"]), None)
                inc = " ".join((copil or {}).get("text", "").split())[:160]
            ctx = potrivire.norm(inc + " " + (a.get("titlu_structural") or "") + " " + (a.get("titlul") or ""))
            n = sum(1 for x in st if x in ctx)
            if n:
                ies.append((n, a, inc))
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
        # C41: GEMENII din acelasi act (text aproape identic, alt articol) se arata aici, ca modelul sa-i
        # vada si sa-si justifice alegerea; verificarea cere justificarea pentru orice geaman vazut
        # C54: geamenii se arata NUMAI ca id + temei, fara text, si nu devin "vazuti": textul lor il
        # primeste modelul doar daca il cere explicit (`deschide` pe id), ca sa-l poata cita
        gem = self.gemeni_in_act(a)
        return {"id": aid, "temei": intrebari.temei_uman(a),
                "valabil_din": a.get("valabil_din") or "nedovedit",
                "sursa": self.corp.sursa_act.get(a["act"], {}).get("sursa"),
                "text": txt[:MAX_TEXT] + (" [... trunchiat; citeaza numai din partea aratata]"
                                          if trunchiat else ""),
                "parinte": a.get("parinte"),
                "copii": [{"id": x["id"], "inceput": " ".join(x["text"].split())[:90]} for x in copii[:40]],
                "deroga_sau_modifica_acest_atom": [
                    {"id": e["sursa"], "fel": e["fel"], "fragment": e["fragment"][:200]} for e in intrari],
                "atomi_cu_text_aproape_identic": [{"id": y["id"], "temei": intrebari.temei_uman(y)} for y in gem],
                "acest_atom_deroga_de_la": [
                    {"tinta": "%s#art%s%s" % (e["tinta_act"], e["tinta_art"],
                                              "/alin%s" % e["tinta_alin"] if e["tinta_alin"] else ""),
                     "fel": e["fel"]} for e in iesiri]}

    def gemeni_in_act(self, a):
        """Atomii din acelasi act cu un fragment identic de >= PRAG_COMUN caractere, din alt articol."""
        if len(a["text"]) < PRAG_COMUN:
            return []
        if a["act"] not in self._schinduri_act:
            ix = {}
            for y in self.corp.pe_act[a["act"]]:
                if len(y["text"]) >= PRAG_COMUN and self._valid(y) and not y.get("nota_tranzitorie"):
                    for sh in _schinduri(potrivire.norm(y["text"].split("⟦NOTĂ⟧")[0])):
                        ix.setdefault(sh, set()).add(y["id"])
            self._schinduri_act[a["act"]] = ix
        ix = self._schinduri_act[a["act"]]
        x = potrivire.norm(a["text"].split("⟦NOTĂ⟧")[0])
        cand = set().union(*[ix.get(sh, set()) for sh in _schinduri(x)]) if x else set()
        art = a["id"].split("/")[0]
        ies = []
        for yid in sorted(cand):
            y = self.corp.dupa_id[yid]
            if yid == a["id"] or yid.split("/")[0] == art:
                continue
            if _fragment_comun(x, potrivire.norm(y["text"].split("⟦NOTĂ⟧")[0])) >= PRAG_COMUN:
                ies.append(y)
        return ies[:5]

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
_MII = re.compile(r"\d\.\d{3}(?!\d)")


# C45: numerele scrise in litere in lege. Operandul poarta forma LITERALA din atom ("cinci", "cincime");
# conversia o face codul si o declara in calcul.
_UNITATI = {"zero": 0, "unu": 1, "una": 1, "un": 1, "o": 1, "doi": 2, "doua": 2, "trei": 3, "patru": 4,
            "cinci": 5, "sase": 6, "sapte": 7, "opt": 8, "noua": 9, "zece": 10, "unsprezece": 11,
            "doisprezece": 12, "douasprezece": 12, "treisprezece": 13, "paisprezece": 14,
            "cincisprezece": 15, "saisprezece": 16, "saptesprezece": 17, "optsprezece": 18,
            "nouasprezece": 19}
_ZECI = {"douazeci": 20, "treizeci": 30, "patruzeci": 40, "cincizeci": 50, "saizeci": 60,
         "saptezeci": 70, "optzeci": 80, "nouazeci": 90}
_FRACTII = {"jumatate": Decimal(1) / 2, "treime": Decimal(1) / 3, "patrime": Decimal(1) / 4,
            "cincime": Decimal(1) / 5, "zecime": Decimal(1) / 10}


def numar_din_litere(v):
    """Decimal pentru un numeral romanesc scris in litere, sau None."""
    t = potrivire.norm(v).strip()
    t = re.sub(r"^(o|un|una)\s+(?=\w*(ime|jumatate))", "", t)
    if t in _FRACTII:
        return _FRACTII[t]
    t = re.sub(r"\s+(de\s+)?(ani|luni|zile|lei|euro|salarii)$", "", t)
    if t in _UNITATI:
        return Decimal(_UNITATI[t])
    m = re.match(r"^(\w+)(?:\s+si\s+(\w+))?$", t)
    if m and m.group(1) in _ZECI and (not m.group(2) or m.group(2) in _UNITATI):
        return Decimal(_ZECI[m.group(1)] + (_UNITATI[m.group(2)] if m.group(2) else 0))
    m = re.match(r"^(o|doua|trei|patru|cinci|sase|sapte|opt|noua)?\s*(suta|sute)$", t)
    if m:
        return Decimal(100 * (_UNITATI.get(m.group(1) or "o", 1)))
    return None


# C51: ordinalele ("15-a", "a 15-a", "al 3-lea") si "cifra + unitate" ("60 de zile", "5 ani", "12 luni")
# sunt operanzi valizi: valoarea e cifra, conversia se declara in calcul.
_ORDINAL_UNITATE = re.compile(r"^(?:a|al)?\s*(\d+(?:[.,]\d+)?)\s*(?:-a|-lea)?"
                              r"(?:\s+(?:de\s+)?(?:zile|zi|luni|luna|ani|an|salarii|salariu|ore|saptamani))?$")


def forma_ordinal_unitate(v):
    """Cifra dintr-un ordinal sau dintr-o "cifra + unitate", ori None daca forma e alta (sau e cifra goala)."""
    t = potrivire.norm(v.strip())
    if re.match(r"^\d+(?:[.,]\d+)*%?$", t):
        return None
    m = _ORDINAL_UNITATE.match(t)
    return m.group(1) if m else None


def _numar(v):
    """"100.000" -> 100000; "2,25%" -> 0.0225; "25.03.2026" -> date. Intoarce (valoare, e_procent)."""
    ou = forma_ordinal_unitate(v)
    if ou is not None:
        v = ou
    t = potrivire.norm(v.strip())
    lit = numar_din_litere(v) if re.search(r"[a-z]", t) and not re.search(r"\d", t) and \
        t not in intrebari._LUNI else None
    if lit is not None:
        return lit, False
    m = re.match(r"^(\d{1,2})\s+(%s)\s+(\d{4})$" % "|".join(intrebari._LUNI), t)
    if m:                                               # "28 februarie 2026" -> data
        return datetime.date(int(m.group(3)), intrebari._LUNI[m.group(2)], int(m.group(1))), False
    if t in intrebari._LUNI:                            # "februarie" -> 2 (luna, pentru data(z, l, a))
        return Decimal(intrebari._LUNI[t]), False
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


_OP = {ast.Add: "+", ast.Sub: "−", ast.Mult: "×", ast.Div: "÷"}


def _eval(nod, env, pasi=None, fmt=None):
    """Valoarea formulei. `pasi` aduna, pentru afisare, fiecare apel zile(a, b) cu rezultatul lui."""
    if isinstance(nod, ast.Expression):
        return _eval(nod.body, env, pasi, fmt)
    if isinstance(nod, ast.BinOp) and type(nod.op) in _OP:
        a, b = _eval(nod.left, env, pasi, fmt), _eval(nod.right, env, pasi, fmt)
        # o data +/- un numar intreg de zile e o data (C32: termenul nominal = data + N zile)
        if isinstance(a, datetime.date) and isinstance(b, Decimal) and type(nod.op) in (ast.Add, ast.Sub):
            if b != b.to_integral_value():
                raise ValueError("o data se aduna numai cu un numar intreg de zile")
            zi = datetime.timedelta(days=int(b))
            return a + zi if isinstance(nod.op, ast.Add) else a - zi
        if isinstance(nod.op, ast.Add):
            return a + b
        if isinstance(nod.op, ast.Sub):
            return a - b
        if isinstance(nod.op, ast.Mult):
            return a * b
        return a / b
    if isinstance(nod, ast.UnaryOp) and isinstance(nod.op, ast.USub):
        return -_eval(nod.operand, env, pasi, fmt)
    if isinstance(nod, ast.Name):
        if nod.id not in env:
            raise ValueError("nume fara sursa in formula: %s" % nod.id)
        return env[nod.id]
    if isinstance(nod, ast.Constant) and nod.value in (1, 100) and not isinstance(nod.value, bool):
        return Decimal(nod.value)
    if isinstance(nod, ast.Constant):
        raise ValueError("constanta fara sursa in formula: %r (permise numai 1 si 100)" % nod.value)
    if isinstance(nod, ast.Call) and isinstance(nod.func, ast.Name) and not nod.keywords:
        args = [_eval(x, env, pasi, fmt) for x in nod.args]
        if nod.func.id == "min" and args:
            return min(args)
        if nod.func.id == "max" and args:
            return max(args)
        if nod.func.id == "data" and len(args) == 3:
            return datetime.date(int(args[2]), int(args[1]), int(args[0]))
        if nod.func.id == "termen_efectiv" and len(args) == 1 and isinstance(args[0], datetime.date):
            if not (fmt or {}).get("calendar"):
                raise ValueError("termen_efectiv cere, CITATE in raspuns, atomul regulii prelungirii "
                                 "termenului si atomul listei sarbatorilor legale (C32)")
            v, explicatie = fmt["calendar"].termen_efectiv(args[0])
            if pasi is not None:
                pasi.append(explicatie)
            return v
        if nod.func.id == "zile" and len(args) == 2:
            v = Decimal((args[1] - args[0]).days)
            if pasi is not None:
                pasi.append("zile(%s, %s) = %s zile" % (_arata(args[0], fmt), _arata(args[1], fmt),
                                                         _arata(v, fmt)))
            return v
    raise ValueError("forma nepermisa in formula: %s" % ast.dump(nod)[:80])


def _format(d, mii=True):
    d = Decimal(d).quantize(Decimal("0.01"))
    intreg, _, zec = ("%.2f" % d).partition(".")
    semn = "-" if intreg.startswith("-") else ""
    intreg = intreg.lstrip("-")
    if mii:
        intreg = ".".join([intreg[max(0, i - 3):i] for i in range(len(intreg), 0, -3)][::-1])
    return semn + intreg + ("" if zec == "00" else "," + zec)


def _arata(v, fmt):
    if isinstance(v, datetime.date):
        return v.strftime("%d.%m.%Y")
    return _format(v, mii=(fmt or {}).get("mii", True))


def _cu_valori(nod, env, fmt, procente):
    """Formula cu valorile puse in locul numelor - ca un contabil s-o poata reface (C28)."""
    if isinstance(nod, ast.Expression):
        return _cu_valori(nod.body, env, fmt, procente)
    if isinstance(nod, ast.BinOp) and type(nod.op) in _OP:
        return "(%s %s %s)" % (_cu_valori(nod.left, env, fmt, procente), _OP[type(nod.op)],
                               _cu_valori(nod.right, env, fmt, procente))
    if isinstance(nod, ast.UnaryOp):
        return "−" + _cu_valori(nod.operand, env, fmt, procente)
    if isinstance(nod, ast.Name):
        if nod.id in procente:
            return procente[nod.id]
        return _arata(env[nod.id], fmt)
    if isinstance(nod, ast.Constant):
        return str(nod.value)
    if isinstance(nod, ast.Call):
        return "%s(%s)" % (nod.func.id, ", ".join(_cu_valori(x, env, fmt, procente) for x in nod.args))
    return "?"


# ── C32: termenul efectiv - regula prelungirii si sarbatorile legale, din atomi ─────────────────
_REGULA_PRELUNGIRE = re.compile(r"zi nelucr[aă]toare.{0,120}prelunge|prelunge.{0,120}zi nelucr[aă]toare"
                                r"|sfar[sș]esc.{0,60}zi de s[aă]rb[aă]toare.{0,120}prelunge", re.I | re.S)
_LISTA_SARBATORI = re.compile(r"s[aă]rb[aă]toare legal[aă] [iî]n care nu se lucreaz[aă]", re.I)
_ZILE_SAPT = ["luni", "marți", "miercuri", "joi", "vineri", "sâmbătă", "duminică"]


def pastele_ortodox(an):
    """Pastele ortodox: algoritmul Meeus pentru calendarul iulian, + 13 zile (valabil 1900-2099)."""
    a, b, c = an % 4, an % 7, an % 19
    d = (19 * c + 15) % 30
    e = (2 * a + 4 * b - d + 34) % 7
    luna, zi = (d + e + 114) // 31, (d + e + 114) % 31 + 1
    return datetime.date(an, luna, zi) + datetime.timedelta(days=13)


class Calendar(object):
    """Zilele nelucratoare, construite din DOI atomi citati: regula prelungirii (Codul de procedura
    civila art. 181 alin. (2), la care trimite CPF art. 75) si lista sarbatorilor legale (Codul muncii
    art. 139 alin. (1)). Nimic din memorie: o sarbatoare intra numai daca atomul o numeste.

    Datele: cele scrise in atom ("1 și 2 ianuarie", "24 ianuarie", "1 mai") se citesc din text; cele
    MOBILE (Vinerea Mare, Pastele, Rusaliile) se CALCULEAZA, iar calculul se declara; cele NUMITE fara
    data in atom (Adormirea Maicii Domnului, Craciunul) primesc data de calendar liturgic fix, DECLARATA ca
    "data de calendar, nescrisa in lege" (decizia C38, dupa C34).
    Sarbatorile cultelor necrestine "pentru persoanele apartinand acestora" nu sunt zile nelucratoare
    generale si nu intra."""

    def __init__(self, regula, lista):
        self.regula, self.lista = regula, lista
        self.weekend = bool(re.search(r"nelucr[aă]toare|s[aâ]mb[aă]t|duminic", regula["text"], re.I))
        self.text = potrivire.norm(lista["text"])

    @classmethod
    def din_atomi(cls, atomi):
        regula = next((a for a in atomi if _REGULA_PRELUNGIRE.search(a["text"].split("⟦NOTĂ⟧")[0])), None)
        lista = next((a for a in atomi if _LISTA_SARBATORI.search(a["text"])), None)
        return cls(regula, lista) if regula and lista else None

    def sarbatori(self, an):
        """{data: denumire} si lista declaratiilor (calcule si date declarate) pentru anul dat."""
        t, ies, decl = self.text, {}, []
        luni = "|".join(intrebari._LUNI)
        for m in re.finditer(r"(\d{1,2})(?:\s*si\s*(\d{1,2}))?\s+(%s)\b" % luni, t):
            for z in (m.group(1), m.group(2)):
                if z:
                    ies[datetime.date(an, intrebari._LUNI[m.group(3)], int(z))] = "%s %s" % (z, m.group(3))
        p = pastele_ortodox(an)
        mobile = []
        if "vinerea mare" in t:
            ies[p - datetime.timedelta(days=2)] = "Vinerea Mare"
            mobile.append("Vinerea Mare = %s" % (p - datetime.timedelta(days=2)).strftime("%d.%m.%Y"))
        if re.search(r"prima si a doua zi de pasti", t):
            ies[p], ies[p + datetime.timedelta(days=1)] = "Paștele", "a doua zi de Paști"
            mobile.append("Paștele ortodox = %s" % p.strftime("%d.%m.%Y"))
        if re.search(r"prima si a doua zi de rusalii", t):
            r = p + datetime.timedelta(days=49)
            ies[r], ies[r + datetime.timedelta(days=1)] = "Rusaliile", "a doua zi de Rusalii"
            mobile.append("Rusaliile = Paștele + 49 de zile = %s" % r.strftime("%d.%m.%Y"))
        if mobile:
            decl.append("date mobile calculate pentru %d (Paștele ortodox: algoritmul Meeus pentru "
                        "calendarul iulian + 13 zile): %s" % (an, "; ".join(mobile)))
        # C34: o sarbatoare NUMITA in atom fara data ("Adormirea Maicii Domnului", "prima si a doua zi de
        # Craciun" - textul oficial al art. 139 chiar nu le scrie data, verificat in HTML-ul portalului)
        # nu primeste data de mana. Ramane fara data, iar calculul se abtine (vezi `termen_efectiv`).
        # C38 (decizia arhitectului, dupa C34): o sarbatoare NUMITA in atom fara data (textul oficial al
        # art. 139 chiar nu o scrie) primeste data ei de CALENDAR LITURGIC FIX, tratata ca Pastele (C32):
        # declarata explicit in raspuns ca "data de calendar, nescrisa in lege"; atomul art. 139 ramane
        # citat pentru caracterul de sarbatoare legala. Numai aceste doua, numai cand atomul le numeste.
        self.fara_data = []
        data_in = re.compile(r"\d{1,2}(?:\s*si\s*\d{1,2})?\s+(%s)\b" % luni)
        calendar_fix = []
        for element in re.split(r";", t):                   # elementele listei, fiecare cu data lui
            if data_in.search(element):
                continue
            if "adormirea maicii domnului" in element:
                ies[datetime.date(an, 8, 15)] = "Adormirea Maicii Domnului"
                calendar_fix.append("Adormirea Maicii Domnului = 15.08.%d" % an)
            elif "zi de craciun" in element:
                ies[datetime.date(an, 12, 25)], ies[datetime.date(an, 12, 26)] = \
                    "Crăciunul", "a doua zi de Crăciun"
                calendar_fix.append("Crăciunul = 25-26.12.%d" % an)
        if calendar_fix:
            decl.append("sărbători numite în art. 139 fără dată, cu data de calendar liturgic fix (dată de "
                        "calendar, nescrisă în lege): %s" % "; ".join(calendar_fix))
        return ies, decl

    def termen_efectiv(self, d):
        s, decl = self.sarbatori(d.year)
        s2, decl2 = self.sarbatori(d.year + 1) if d.month == 12 else ({}, [])
        s.update(s2)
        motive, x = [], d
        while (self.weekend and x.weekday() >= 5) or x in s:
            motive.append("%s %s" % (x.strftime("%d.%m.%Y"), s.get(x) or _ZILE_SAPT[x.weekday()]))
            x += datetime.timedelta(days=1)
        if not motive:
            expl = "termen_efectiv(%s) = %s (zi lucrătoare: %s)" % (
                d.strftime("%d.%m.%Y"), d.strftime("%d.%m.%Y"), _ZILE_SAPT[d.weekday()])
        else:
            expl = ("termen_efectiv(%s) = %s: %s → prima zi lucrătoare, %s (%s). Regula: `%s`; sărbătorile: "
                    "`%s`" % (d.strftime("%d.%m.%Y"), x.strftime("%d.%m.%Y"), ", ".join(motive),
                              x.strftime("%d.%m.%Y"), _ZILE_SAPT[x.weekday()], self.regula["id"],
                              self.lista["id"]))
        return x, expl + ("; " + "; ".join(decl + decl2) if decl else "")


# ── C55: valabilitatea unei valori legale, din nota atomului si din textul lui ────────────────────
_LUNI_V = {"ianuarie": 1, "februarie": 2, "martie": 3, "aprilie": 4, "mai": 5, "iunie": 6, "iulie": 7,
           "august": 8, "septembrie": 9, "octombrie": 10, "noiembrie": 11, "decembrie": 12}
_DATA_TEXT = r"(?:(\d{1,2})\s+(%s)\s+(\d{4})|(\d{1,2})\.(\d{1,2})\.(\d{4}))" % "|".join(_LUNI_V)


def _data_din(m, k=0):
    g = m.groups()[k:k + 6]
    if g[0]:
        return datetime.date(int(g[2]), _LUNI_V[g[1]], int(g[0]))
    return datetime.date(int(g[5]), int(g[4]), int(g[3]))


def valabilitate_valoare(atom, valoare, fragment=""):
    """(valabil_din, valabil_pana) pentru o valoare legala: nota de consolidare a atomului ("(la
    DD-MM-YYYY, ...)") si textul din jurul valorii: "incepand cu (data de) D", "in perioada D1-D2" /
    "pentru perioada D1-D2". Ce nu se gaseste ramane None (nu se inventeaza)."""
    din = datetime.date.fromisoformat(atom["valabil_din"]) if atom.get("valabil_din") else None
    pana = datetime.date.fromisoformat(atom["valabil_pana"]) if atom.get("valabil_pana") else None
    t = potrivire.norm(atom["text"].split("⟦NOTĂ⟧")[0])
    p = t.find(potrivire.norm(valoare)) if valoare else -1
    # intai in jurul valorii; apoi la inceputul atomului, unde o fraza de valabilitate guverneaza tot atomul
    # ("Incepand cu data de 1 iulie 2026, salariul ... la suma de 4.325 lei")
    for zona in ([t[max(0, p - 220):p + 220]] if p >= 0 else []) + [t[:250]]:
        m = re.search(r"(?:perioada|intervalul)\s+" + _DATA_TEXT + r"\s*[-–]\s*" + _DATA_TEXT, zona)
        if m:
            return max(filter(None, [din, _data_din(m, 0)])), _data_din(m, 6)
        m = re.search(r"incepand cu(?: data de)?\s+" + _DATA_TEXT, zona)
        if m:
            return max(filter(None, [din, _data_din(m, 0)])), pana
    return din, pana


def evalueaza_calcule(calcule, dupa_id, intrebare, citati=None, data_faptului=None):
    """(valori, incalcari, detalii). Fara model: sursa fiecarui operand verificata literal.

    C25: eticheta operandului decide sursa ceruta. FAPT_CAZ - valoarea trebuie sa apara LITERAL in
    intrebare (altfel e o valoare fara sursa). VALOARE_LEGALA - atom aratat modelului, fragment verbatim
    in el, valoarea literal in fragment."""
    env, greseli, detalii, procente, conversii = {}, [], [], {}, []
    # C28: stilul numerelor urmeaza sursa - cu separator de mii daca operanzii il au ("10.000"),
    # fara daca nu ("2026" + 1 = 2027, nu "2.027")
    fmt = {"mii": any(_MII.search(o["valoare"]) for c in calcule for o in c["operanzi"])}
    # C32: calendarul termenelor se construieste NUMAI din atomii citati in raspuns
    if any("termen_efectiv" in c["formula"] for c in calcule):
        fmt["calendar"] = Calendar.din_atomi([dupa_id[i] for i in (citati or []) if i in dupa_id])
    q = semantic._n(intrebare)
    for c in calcule:
        for o in c["operanzi"]:
            val = o["valoare"].strip()
            if o["eticheta"] == "VALOARE_LEGALA":
                a = dupa_id.get(o["atom"])
                # C55: valabilitatea valorii trebuie sa acopere data la care se aplica (declarata pe
                # operand; altfel data de referinta a raspunsului)
                if a is not None:
                    din, pana = valabilitate_valoare(a, val, o.get("fragment", ""))
                    try:
                        cand = datetime.date.fromisoformat((o.get("data_aplicarii") or "").strip() or
                                                           (data_faptului or ""))
                    except ValueError:
                        cand = None
                    o["valabil_din"], o["valabil_pana"] = (din.isoformat() if din else None,
                                                           pana.isoformat() if pana else None)
                    if cand and ((din and cand < din) or (pana and cand > pana)):
                        greseli.append("C55: operandul %s=%s (din %s) e valabil %s-%s, iar se aplica la %s"
                                       % (o["nume"], val, o["atom"], din.strftime("%d.%m.%Y") if din else "…",
                                          pana.strftime("%d.%m.%Y") if pana else "…", cand.strftime("%d.%m.%Y")))
                if not o["atom"]:
                    greseli.append("operandul %s=%s e VALOARE_LEGALA fara atom" % (o["nume"], val))
                elif a is None:
                    greseli.append("operandul %s: atomul %s nu i-a fost aratat" % (o["nume"], o["atom"]))
                elif semantic._n(o["fragment"]) not in semantic._n(a["text"]):
                    greseli.append("operandul %s: fragmentul nu e verbatim in %s" % (o["nume"], o["atom"]))
                if val not in o["fragment"]:
                    greseli.append("operandul %s=%r nu apare literal in fragmentul lui" % (o["nume"], val))
            else:
                if val not in q:
                    greseli.append("operandul %s=%r e FAPT_CAZ, dar nu apare literal in intrebare"
                                   % (o["nume"], val))
            try:
                env[o["nume"]], proc = _numar(val)
                if proc:
                    procente[o["nume"]] = val
                lit = numar_din_litere(val) if re.search(r"[a-zA-ZăâîșțĂÂÎȘȚ]", val) and \
                    not re.search(r"\d", val) else None
                if lit is not None:
                    conversii.append("„%s” (în litere în atom) = %s" % (val, _format(lit)))
                elif forma_ordinal_unitate(val) is not None:
                    conversii.append("„%s” (ordinal / cifră cu unitate) = %s" % (val, forma_ordinal_unitate(val)))
            except ValueError as e:
                greseli.append(str(e))
        try:
            arb = ast.parse(c["formula"], mode="eval")
            # C50: un operand scris cu "%" valoreaza deja fractiunea (21% = 0,21); impartit la 100 inca o
            # data da o suma de 100 de ori mai mica (Q3-TVA-09: 1.050 lei in loc de 105.000)
            for n in ast.walk(arb):
                if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Div) and \
                        isinstance(n.right, ast.Constant) and n.right.value == 100 and \
                        {x.id for x in ast.walk(n.left) if isinstance(x, ast.Name)} & set(procente):
                    greseli.append("C50: calculul %s imparte la 100 un operand scris cu %% (%s), care "
                                   "valoreaza deja fractiunea" % (c["nume"], ", ".join(
                                       sorted({x.id for x in ast.walk(n.left) if isinstance(x, ast.Name)}
                                              & set(procente)))))
            zile = []
            v = _eval(arb, env, zile, fmt)
            env[c["nume"]] = v
            if conversii:
                zile = ["conversie C45/C51: " + x for x in conversii] + zile
                conversii = []
            detalii.append({"nume": c["nume"], "formula": c["formula"],
                            "cu_valori": _cu_valori(arb, env, fmt, procente),
                            "zile": zile, "rezultat": _arata(v, fmt), "operanzi": c["operanzi"]})
        except (ValueError, SyntaxError, ZeroDivisionError, TypeError, InvalidOperation,
                AttributeError, KeyError) as e:
            greseli.append("calculul %s: %s" % (c["nume"], e))
    valori = {d["nume"]: d["rezultat"] for d in detalii}
    return valori, greseli, detalii


def pas_cu_pas(detalii):
    """Textul calculului: fiecare pas cu formula, valorile puse in ea si rezultatul (C28)."""
    rand = []
    for d in detalii:
        for z in d["zile"]:
            rand.append(z)
        rand.append("%s = %s = %s = %s" % (d["nume"], d["formula"], d["cu_valori"], d["rezultat"]))
    return rand


# ── C27: datele pe care le poarta intrebarea ─────────────────────────────────────────────────────
def date_din_intrebare(text):
    """[(data_iso, precizie, fragment)], fara datele mai grosiere cuprinse intr-una mai fina.

    Reguli ca in `intrebari.data_referinta` (D12: luna -> ultima zi, an -> 31.12 dar nu dupa ziua
    intrebarii), aplicate TUTUROR datelor, nu numai primei."""
    t = potrivire.norm(text)
    ies, ocupat = [], []

    def liber(m):
        return not any(a < m.end() and m.start() < b for a, b in ocupat)

    for m in re.finditer(r"\b(\d{1,2})\.(\d{1,2})\.(20\d\d)\b", t):
        ies.append(("%s-%02d-%02d" % (m.group(3), int(m.group(2)), int(m.group(1))), "zi", m.group(0)))
        ocupat.append(m.span())
    luni = "|".join(intrebari._LUNI)
    for m in re.finditer(r"\b(\d{1,2})\s+(%s)\s+(20\d\d)\b" % luni, t):
        if liber(m):
            ies.append(("%s-%02d-%02d" % (m.group(3), intrebari._LUNI[m.group(2)], int(m.group(1))),
                        "zi", m.group(0)))
            ocupat.append(m.span())
    for m in re.finditer(r"\b(%s)\s+(20\d\d)\b" % luni, t):
        if liber(m):
            an, luna = int(m.group(2)), intrebari._LUNI[m.group(1)]
            ultima = datetime.date(an + (luna == 12), luna % 12 + 1, 1) - datetime.timedelta(days=1)
            ies.append((ultima.isoformat(), "luna", m.group(0)))
            ocupat.append(m.span())
    for m in re.finditer(r"\b(20\d\d)\b", t):
        if liber(m):
            ies.append((min("%s-12-31" % m.group(1), intrebari.DATA_INTREBARII), "an", m.group(0)))
    fine = [(d, p) for d, p, _f in ies if p != "an"]
    ies = [x for x in ies if not (
        (x[1] == "an" and any(d[:4] == x[2] for d, _p in fine)) or
        (x[1] == "luna" and any(p == "zi" and d[:7] == x[0][:7] for d, p in fine)))]
    unice, vazut = [], set()
    for x in ies:
        if x[0] not in vazut:
            vazut.add(x[0])
            unice.append(x)
    return unice


# ── C40: orice termen calendaristic din raspuns vine din termen_efectiv ──────────────────────────
_LUNI_RX = "|".join(["ianuarie", "februarie", "martie", "aprilie", "mai", "iunie", "iulie", "august",
                     "septembrie", "octombrie", "noiembrie", "decembrie"])
_DATA_RASPUNS = re.compile(r"\b(\d{1,2}\.\d{1,2}\.\d{4}|\d{1,2}\s+(?:%s)(?:\s+\d{4})?)\b" % _LUNI_RX, re.I)
_CONTEXT_TERMEN = re.compile(r"p[aâ]n[aă] (la|[iî]n)|cel t[aâ]rziu|termen|scaden|se depun|se pl[aă]t|expir[aă]"
                             r"|ultima zi|inclusiv", re.I)


_INCEPUT = re.compile(r"(\bde la|[iî]ncep[aâ]nd cu|curge de la|s[aă] curg[aă] (de )?la|\bdin)\s+(data de\s+)?$", re.I)


def verifica_termene(raspuns, intrebare, termene_ok):
    """C40: o data aflata intr-un context de termen ("pana la", "cel tarziu", "termenul", "inclusiv") e un
    termen calendaristic; trece numai daca e rezultatul unui termen_efectiv evaluat de cod sau un fapt
    al cazului, literal in intrebare. Regulile recurente fara luna ("pana la 25 a lunii urmatoare") nu
    sunt termene calendaristice si nu se ating."""
    gr = []
    q = potrivire.norm(intrebare)
    raspuns = raspuns.split("  [data de referință")[0]      # sufixul declarativ nu e raspuns
    for m in _DATA_RASPUNS.finditer(raspuns):
        d = m.group(1)
        inainte = raspuns[max(0, m.start() - 120):m.start()]
        # o data de INCEPUT ("curge de la 1 ianuarie", "incepand cu", "de la") nu e un termen
        if _INCEPUT.search(inainte[-30:]):
            continue
        if not _CONTEXT_TERMEN.search(inainte + raspuns[m.end():m.end() + 25]):
            continue
        if d in termene_ok or potrivire.norm(d) in q:
            continue
        gr.append("C40: termenul %r nu vine din termen_efectiv (un termen calendaristic se calculeaza, nu "
                  "se scrie)" % d)
    return gr


# ── C41: temeiul alaturat, cu text aproape identic ───────────────────────────────────────────────
PRAG_COMUN = 100          # caractere identice consecutive; masurat: perechea CF art. 319(3)/320(3) are
#                           162, iar din 11.165 de perechi aleatoare de alineate niciuna nu ajunge la 80


def _fragment_comun(x, y):
    import difflib
    return difflib.SequenceMatcher(None, x, y, autojunk=False).find_longest_match(0, len(x), 0, len(y)).size


def _schinduri(t, n=8):
    w = t.split()
    return {" ".join(w[i:i + n]) for i in range(0, max(0, len(w) - n + 1))}


def gemeni(atom, vazuti):
    """Atomii vazuti cu text aproape identic cu `atom` (fragment comun >= PRAG_COMUN), din alt articol."""
    x = potrivire.norm(atom["text"].split("⟦NOTĂ⟧")[0])
    sx = _schinduri(x)
    art = atom["id"].split("/")[0]
    ies = []
    for y in vazuti.values():
        if y["id"] == atom["id"] or y["id"].split("/")[0] == art or len(y["text"]) < PRAG_COMUN:
            continue
        ty = potrivire.norm(y["text"].split("⟦NOTĂ⟧")[0])
        if sx & _schinduri(ty) and _fragment_comun(x, ty) >= PRAG_COMUN:
            ies.append(y)
    return ies


_FAPT_UNITATE = re.compile(r"(\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d+(?:,\d+)?)\s*(%|lei|euro|zile|luni|ani)"
                           r"|(\d{1,2}\.\d{1,2}\.\d{4})")


def fapt_principal(raspuns, intrebare):
    """Prima valoare cu unitate din raspuns (procent, suma, durata, data) care NU e un fapt al cazului."""
    q = potrivire.norm(intrebare)
    for m in _FAPT_UNITATE.finditer(raspuns or ""):
        v = (m.group(1) + ("%" if m.group(2) == "%" else "")) if m.group(1) else m.group(3)
        if potrivire.norm(v) not in q:
            return v
    return None


def atomi_decisivi(final, raspuns, intrebare="", detalii=None):
    """C49: {atom: ancora} - atomii din care vine FAPTUL PRINCIPAL al raspunsului.

    Faptul e rezultatul unui calcul -> atomii operanzilor legali din lantul lui, fiecare cu valoarea
    operandului ca ancora. Faptul e citat -> citatul care il contine, cu faptul ca ancora. Raspuns fara
    valoare (Da/Nu, regula) -> primul citat (C14), fara ancora."""
    f = fapt_principal(raspuns, intrebare)
    if f is None:
        return {final["citate"][0]["atom"]: None} if final.get("citate") else {}
    nume = {d["nume"]: d for d in detalii or []}
    for d in detalii or []:
        if d["rezultat"] == f.rstrip("%"):
            ies, stiva, vazut = {}, [d["nume"]], set()
            while stiva:
                n = stiva.pop()
                if n in vazut:
                    continue
                vazut.add(n)
                for o in nume[n]["operanzi"]:
                    if o.get("eticheta") == "VALOARE_LEGALA" and o.get("atom"):
                        ies[o["atom"]] = o["valoare"]
                for x in ast.walk(ast.parse(nume[n]["formula"], mode="eval")):
                    if isinstance(x, ast.Name) and x.id in nume:
                        stiva.append(x.id)
            return ies
    ies = {c["atom"]: f for c in final.get("citate") or [] if f in (c.get("fragment") or "")}
    if not ies and final.get("citate"):
        ies = {final["citate"][0]["atom"]: None}
    return ies


def geaman_relevant(a, y, ancora):
    """Un geaman conteaza pentru faptul principal numai daca textul comun INCONJOARA ancora (acelasi sablon
    in jurul valorii); fara ancora, orice fragment comun >= PRAG_COMUN."""
    import difflib
    x = potrivire.norm(a["text"].split("⟦NOTĂ⟧")[0])
    ty = potrivire.norm(y["text"].split("⟦NOTĂ⟧")[0])
    if _fragment_comun(x, ty) < PRAG_COMUN:
        return False
    p = x.find(potrivire.norm(ancora)) if ancora else -1
    if p < 0:
        return True
    sm = difflib.SequenceMatcher(None, x, ty, autojunk=False)
    return any(b.size >= 40 and b.a - 60 <= p <= b.a + b.size + 60 for b in sm.get_matching_blocks())


def verifica_alegeri_temei(final, vazuti, decisivi=None, gemeni_fn=None):
    """C41: pentru fiecare atom citat care are un geaman printre atomii vazuti, `alegeri_temei` trebuie sa
    contina justificarea: un fragment literal din atomul citat care NU e in geaman (conditia care ii
    deosebeste). Fara ea - abtinere."""
    gr = []
    alegeri = final.get("alegeri_temei") or []
    citati = {c["atom"] for c in final.get("citate") or []}
    tinte = decisivi if decisivi is not None else {c: None for c in citati}
    for c, ancora in tinte.items():                         # C49: numai atomul decisiv
        a = vazuti.get(c)
        if a is None:
            continue
        for y in (gemeni_fn(a) if gemeni_fn else gemeni(a, vazuti)):
            # un geaman citat si el e folosit, nu inlocuit (CAS art. 138 si CASS art. 156 in acelasi calcul)
            if y["id"] in citati or (decisivi is not None and not geaman_relevant(a, y, ancora)):
                continue
            ok = False
            for al in alegeri:
                if al["atom"] == c and al["alternativa"] == y["id"]:
                    f = semantic._n(al["conditie"])
                    ok = len(f) >= 15 and f in semantic._n(a["text"]) and f not in semantic._n(y["text"])
            if not ok:
                gr.append("C41: atomul citat %s are un geaman (%s) si alegerea nu e "
                          "justificata printr-o conditie literala care ii deosebeste" % (c, y["id"]))
    return gr


# ── C23: validarea structurala a raspunsului final ──────────────────────────────────────────────
_MARCAJ = re.compile(r"</?\s*(parameter|declaratie|raspuns|citate|lipsa|motiv|calcule|derogari_tratate|"
                     r"data_referinta)\b|<parameter\b", re.I)


# ── C33: secventele \uXXXX scrise ca TEXT sunt un artefact de transport, nu de continut ─────────
# La reemiterea ceruta de C23, modelul a scris diacriticele ca "imobiliz\u0103rilor". Se decodeaza numai
# secventa completa \u + 4 cifre hexa care da un caracter tiparibil (nu un surogat, nu un caracter de
# control); orice alt backslash ramane neatins.
_ESC_U = re.compile(r"\\u([0-9a-fA-F]{4})")


def _caracter(m):
    c = chr(int(m.group(1), 16))
    if 0xD800 <= ord(c) <= 0xDFFF or not c.isprintable():
        return m.group(0)
    return c


def decodeaza_transport(x):
    """Aceeasi structura, cu secventele backslash-u-XXXX din texte decodate; restul, neatins."""
    if isinstance(x, str):
        return _ESC_U.sub(_caracter, x)
    if isinstance(x, dict):
        return {k: decodeaza_transport(v) for k, v in x.items()}
    if isinstance(x, list):
        return [decodeaza_transport(v) for v in x]
    return x


def valideaza_structura(inp):
    """Lista de probleme; goala = structura e buna. Fara model."""
    probleme = []

    def texte(x, cale):
        if isinstance(x, str):
            yield cale, x
        elif isinstance(x, dict):
            for k, v in x.items():
                for y in texte(v, cale + "." + k):
                    yield y
        elif isinstance(x, list):
            for i, v in enumerate(x):
                for y in texte(v, "%s[%d]" % (cale, i)):
                    yield y

    for cale, t in texte(inp, "raspunde"):
        if _MARCAJ.search(t):
            probleme.append("marcaj de parametri scurs in %s" % cale)
    r = (inp.get("raspuns") or "").strip()
    if inp.get("stare") == "RASPUNS":
        if len(re.sub(r"\W", "", r)) < 2:
            probleme.append("campul raspuns e gol sau un substituent (%r)" % r[:10])
        for k in ("declaratie", "motiv", "data_referinta_motiv"):
            alt = (inp.get(k) or "").strip()
            if r and alt and len(r) >= 20 and (r == alt or r in alt):
                probleme.append("campul raspuns repeta continutul campului %s" % k)
    return probleme


# ── bucla ────────────────────────────────────────────────────────────────────────────────────────
def sistem(idx):
    acte = sorted(b for b, v in idx.normativ.items() if v)
    return SISTEM + "\n\nACTELE NORMATIVE din corpus (id-urile folosite de `cuprins`):\n" + ", ".join(acte)


def _apel(client, sis, messages, final=False):
    # uneltele raman declarate si in tura finala (istoricul contine tool_use), dar nu se pot folosi
    extra = {"tool_choice": {"type": "none"},
             "output_config": {"format": {"type": "json_schema", "schema": SCHEMA}}} if final else {}
    return client.beta.messages.create(
        model=MODEL, max_tokens=16000, betas=["server-side-fallback-2026-07-01"],
        fallbacks="default", thinking={"type": "adaptive"},
        system=[{"type": "text", "text": sis, "cache_control": {"type": "ephemeral"}}],
        tools=UNELTE, messages=messages, cache_control={"type": "ephemeral"}, **extra)


def raspunde(q, idx, rel, client, sis=None):
    date = date_din_intrebare(q["intrebare"])
    admise = [d for d, _p, _f in date] or [intrebari.DATA_INTREBARII]
    # unealtele arata atomii in vigoare la cea mai recenta data a intrebarii (C27); citatele se
    # verifica apoi la data ALEASA pentru faptul intrebat
    vizibil = max(admise)
    nav = Navigator(idx, rel, vizibil)
    baza = {"id": q["id"], "tip": q["tip"], "intrebare": q["intrebare"], "date_din_intrebare": date,
            "strat": "navigare v5"}
    descriere = "; ".join("%s (%s, din „%s”)" % (d, p, f) for d, p, f in date) or \
        "%s (întrebarea nu poartă nicio dată: ziua întrebării)" % intrebari.DATA_INTREBARII
    messages = [{"role": "user", "content": "<intrebare>%s</intrebare>\n<date_din_intrebare>%s"
                                            "</date_din_intrebare>" % (q["intrebare"], descriere)}]
    apeluri, final, t0, reincercari, oprit = [], None, time.time(), 0, None
    probleme_c23 = []

    def inregistreaza(r):
        u = r.usage
        iteratii = getattr(u, "iterations", None) or []
        apeluri.append({"model": r.model, "stop_reason": r.stop_reason,
                        "tokeni": {"intrare": u.input_tokens, "iesire": u.output_tokens,
                                   "cache_scriere": getattr(u, "cache_creation_input_tokens", 0) or 0,
                                   "cache_citire": getattr(u, "cache_read_input_tokens", 0) or 0},
                        "cost_usd": semantic._cost(u, r.model),
                        "fallback": bool(r.model != MODEL or any(
                            getattr(x, "type", "") == "fallback_message" for x in iteratii))})

    # 1. NAVIGAREA: numai uneltele de citire, pana cand modelul nu mai cere niciuna
    while True:
        r = _apel(client, sis or sistem(idx), messages)
        inregistreaza(r)
        if r.stop_reason == "refusal" or len(apeluri) > MAX_PASI + 6:
            oprit = "stop_reason=%s" % r.stop_reason
            break
        messages.append({"role": "assistant", "content": r.content})
        uses = [b for b in r.content if b.type == "tool_use"]
        if not uses:
            break                                          # "Gata." - urmeaza tura finala
        if len(nav.pasi) + len(uses) > MAX_PASI:           # C29: peste limita = abtinere cu traseu
            oprit = "C29"
            break
        rezultate = []
        for b in uses:
            out = nav.executa(b.name, b.input)
            out["pasi_ramasi"] = MAX_PASI - len(nav.pasi)
            rezultate.append({"type": "tool_result", "tool_use_id": b.id,
                              "content": json.dumps(out, ensure_ascii=False)})
        messages.append({"role": "user", "content": rezultate})

    # 2. C44: RASPUNSUL FINAL pe iesire structurata, intr-o tura FARA unelte (tool_choice none). In v4-v5,
    # raspunsul dat ca argument al unei unelte isi scurgea campurile unele in altele (C23) si, la
    # reincercare, strica diacriticele (C33, C44). O singura reincercare daca structura e tot invalida.
    cerere = ("Navigarea s-a încheiat. Dă acum răspunsul final, în formatul cerut, numai din atomii pe care "
              "i-ai văzut.")
    while oprit is None:
        messages.append({"role": "user", "content": cerere})
        r = _apel(client, sis or sistem(idx), messages, final=True)
        inregistreaza(r)
        if r.stop_reason == "refusal":
            oprit = "stop_reason=refusal"
            break
        text = next((b.text for b in r.content if b.type == "text"), "")
        messages.append({"role": "assistant", "content": r.content})
        try:
            intrare = decodeaza_transport(json.loads(text))        # C33 ramane plasa
            probleme = valideaza_structura(intrare)
        except ValueError:
            intrare, probleme = None, ["iesirea finala nu e JSON valid (stop_reason=%s)" % r.stop_reason]
        if not probleme:
            final = intrare
            break
        probleme_c23.append(probleme)
        if reincercari >= 1:
            oprit = "C23"
            break
        reincercari += 1
        cerere = ("Structura răspunsului e invalidă: %s. Dă din nou răspunsul final, fiecare câmp cu "
                  "numai textul lui." % "; ".join(probleme))
    apel = {"model": apeluri[-1]["model"] if apeluri else MODEL, "tururi": len(apeluri),
            "pasi_navigare": len(nav.pasi), "pasi": nav.pasi, "reincercari_C23": reincercari,
            "probleme_C23": probleme_c23,
            "tokeni": {k: sum(a["tokeni"][k] for a in apeluri) for k in
                       ("intrare", "iesire", "cache_scriere", "cache_citire")},
            "cost_usd": round(sum(a["cost_usd"] for a in apeluri), 5),
            "fallback": any(a["fallback"] for a in apeluri), "secunde": round(time.time() - t0, 2)}
    traseu = " → ".join("%s(%s)" % (p["unealta"], ", ".join(str(v) for v in p["intrare"].values()))
                        for p in nav.pasi)
    if final is None:
        if oprit == "C29":
            motiv = ("C29: limita de %d pași de navigare a fost atinsă fără răspuns. Traseul: %s"
                     % (MAX_PASI, traseu))
        elif oprit == "C23":
            motiv = ("C23: structura răspunsului final a fost invalidă de două ori (%s)"
                     % " / ".join("; ".join(p) for p in probleme_c23))
        else:
            motiv = "fara raspuns final (%s)" % oprit
        return dict(baza, data_referinta=None, stare="NU_POT_RASPUNDE", tip_abtinere=oprit,
                    raspuns=None, argument=[], apel=apel, traseu=traseu, motiv=motiv)
    rez = verifica_propunerea(final, dict(baza), q, nav, admise, vizibil, apel, traseu)
    # C52: CEL MULT o tura automata de reparatie, numai pentru cifrele respinse (C13/C46): modelul vede
    # exact cifrele si le pune prin calcul sau citat. Ce iese trece prin ACEEASI verificare, fara exceptii.
    cifre = cifre_respinse(rez)
    if rez["stare"] != "RASPUNS" and cifre and oprit is None:
        messages.append({"role": "user", "content": (
            "Verificarea a respins răspunsul pentru aceste cifre, care nu sunt nici citate literal dintr-un "
            "atom, nici rezultatul unui calcul: %s. Dă din nou răspunsul final: fiecare dintre ele fie vine "
            "dintr-un citat literal, fie e rezultatul unui calcul pus ca {nume}, fie lipsește. Restul "
            "regulilor rămân aceleași." % ", ".join("„%s”" % c for c in cifre))})
        r = _apel(client, sis or sistem(idx), messages, final=True)
        inregistreaza(r)
        text = next((b.text for b in r.content if b.type == "text"), "")
        messages.append({"role": "assistant", "content": r.content})
        try:
            final2 = decodeaza_transport(json.loads(text))
            probleme = valideaza_structura(final2)
        except ValueError:
            final2, probleme = None, ["iesirea reparatiei nu e JSON valid"]
        apel = dict(apel, tururi=len(apeluri),
                    tokeni={k: sum(x["tokeni"][k] for x in apeluri) for k in
                            ("intrare", "iesire", "cache_scriere", "cache_citire")},
                    cost_usd=round(sum(x["cost_usd"] for x in apeluri), 5),
                    secunde=round(time.time() - t0, 2))
        prima = {"cifre": cifre, "motiv_initial": rez["motiv"]}
        if not probleme:
            rez = verifica_propunerea(final2, dict(baza), q, nav, admise, vizibil, apel, traseu)
        else:
            rez = dict(rez, apel=apel)
        rez["reparatie_C52"] = dict(prima, structura_invalida=probleme or None, rezultat=rez["stare"])
    return rez


_CIFRA_RESPINSA = re.compile(r"(?:cifra|valoarea legala) '([^']+)'")


def cifre_respinse(rez):
    """Cifrele respinse de C13/C46 - singurele pe care tura de reparatie C52 le poate trata."""
    inc = (rez.get("verificare") or {}).get("incalcari") or []
    ies = []
    for g in inc:
        m = _CIFRA_RESPINSA.search(g)
        if m and m.group(1) not in ies and ("nu apare" in g):
            ies.append(m.group(1))
    return ies


def verifica_propunerea(final, baza, q, nav, admise, vizibil, apel, traseu):
    """Toata verificarea unei propuneri finale: C27, verificarea mecanica, calculul (C25, C45, C50, C51),
    C40, C41 (C49). Fara model - aceeasi pentru prima propunere si pentru reparatia C52."""
    # C27: data aleasa trebuie sa fie una dintre datele intrebarii
    data_ref = (final.get("data_referinta") or "").strip()
    baza["data_referinta"] = data_ref
    baza["data_referinta_motiv"] = final.get("data_referinta_motiv")
    greseli_data = []
    if final["stare"] == "RASPUNS" and data_ref not in admise:
        greseli_data.append("C27: data de referinta %r nu e una dintre datele intrebarii %s"
                            % (data_ref, admise))
    atomi = list(nav.vazuti.values())
    rez = semantic.finalizeaza(baza, final, atomi, q, data_ref if data_ref in admise else vizibil,
                               nav.relatie, apel)
    rez["propunerea_modelului"] = final
    rez["traseu"] = traseu
    if greseli_data:
        return dict(rez, stare="NU_POT_RASPUNDE", raspuns=None,
                    verificare={"trece": False, "incalcari": rez["verificare"]["incalcari"] + greseli_data},
                    motiv="VERIFICAREA DATEI a respins propunerea: " + "; ".join(greseli_data))
    # calculul, evaluat de cod
    if final.get("calcule") and final["stare"] == "RASPUNS":
        valori, greseli, detalii = evalueaza_calcule(final["calcule"], nav.vazuti, q["intrebare"],
                                                     citati=[c["atom"] for c in final.get("citate") or []],
                                                     data_faptului=data_ref if data_ref in admise else None)
        rez["calcule"] = detalii
        if greseli:
            return dict(rez, stare="NU_POT_RASPUNDE", raspuns=None,
                        verificare={"trece": False, "incalcari": rez["verificare"]["incalcari"] + greseli},
                        motiv="VERIFICAREA CALCULULUI a respins propunerea: " + "; ".join(greseli))
        if rez["stare"] == "RASPUNS":
            txt = rez["raspuns"]
            for k, v in valori.items():
                txt = txt.replace("{%s}" % k, v)
            rez["raspuns"] = txt + "  [calcul: " + "; ".join(pas_cu_pas(detalii)) + "]"
    if rez["stare"] == "RASPUNS":
        # C40 (termenele) si C41 (temeiul alaturat, numai pentru atomul decisiv - C49)
        corp_raspuns = rez["raspuns"].split("  [calcul:")[0]
        termene_ok = {d["rezultat"] for d in rez.get("calcule") or [] if "termen_efectiv" in d["formula"]}
        decisivi = atomi_decisivi(final, corp_raspuns, q["intrebare"], rez.get("calcule"))
        rez["atomi_decisivi"] = decisivi
        gr = verifica_termene(corp_raspuns, q["intrebare"], termene_ok)
        if gr:
            return dict(rez, stare="NU_POT_RASPUNDE", raspuns=None,
                        verificare={"trece": False, "incalcari": rez["verificare"]["incalcari"] + gr},
                        motiv="VERIFICAREA (C40) a respins propunerea: " + "; ".join(gr))
        # C41 -> AVERTISMENT (decizia arhitectului, pe masurare: setul 3 - 0 greseli de fond prevenite,
        # 9 raspunsuri corecte pierdute). Geamenii atomului decisiv, din tot actul lui, nejustificati: se
        # scriu in raspuns si in raport; raspunsul nu se respinge.
        av = verifica_alegeri_temei(final, nav.vazuti, decisivi, gemeni_fn=nav.gemeni_in_act)
        if av:
            rez["avertismente"] = [g.replace("C41: ", "C41 (avertisment): ", 1) for g in av]
            rez["raspuns"] += "  [avertisment C41: temei cu geamăn nejustificat — %s]" % "; ".join(
                sorted({re.search(r"\(([^)]+)\)", g).group(1) for g in av if re.search(r"\(([^)]+)\)", g)}))
    if rez["stare"] == "RASPUNS":
        d = datetime.date.fromisoformat(data_ref).strftime("%d.%m.%Y")
        rez["raspuns"] += "  [data de referință: %s — %s]" % (d, final.get("data_referinta_motiv") or "")
    return rez


def ruleaza(dest, intrebari_id=None, csv_intrebari=None):
    import anthropic
    t0 = time.time()
    idx = intrebari.Index()
    rel = idx.rel
    sis = sistem(idx)
    client = anthropic.Anthropic(api_key=semantic.cheie())
    qs = [q for q in (intrebari.incarca_intrebari(csv_intrebari) if csv_intrebari else intrebari.incarca_intrebari())
          if not intrebari_id or q["id"] in intrebari_id]
    # fiecare raspuns se scrie IMEDIAT (o rulare intrerupta - retea, credit - nu pierde ce a platit);
    # la repornire, intrebarile deja raspunse se iau din fisierul partial, fara apel nou
    partial = dest + ".partial.jsonl"
    facute = {}
    if os.path.exists(partial):
        for l in open(partial, encoding="utf-8"):
            r = json.loads(l)
            facute[r["id"]] = r
    ies = []
    for q in qs:
        if q["id"] in facute:
            ies.append(facute[q["id"]])
            continue
        r = raspunde(q, idx, rel, client, sis)
        with open(partial, "a", encoding="utf-8") as f:
            f.write(json.dumps(r, ensure_ascii=False, default=str) + "\n")
        ies.append(r)
        print("%-9s %-16s pasi=%-2d $%.4f %s" % (q["id"], r["stare"], r["apel"]["pasi_navigare"],
                                                   r["apel"]["cost_usd"], (r.get("raspuns") or r["motiv"])[:70]),
              flush=True)
    for r in ies:
        if r["stare"] == "RASPUNS":
            assert r["argument"] and r["verificare"]["trece"], r["id"]
    tok = {k: sum(r["apel"]["tokeni"][k] for r in ies) for k in ("intrare", "iesire", "cache_scriere",
                                                                   "cache_citire")}
    rez = {"_ce": "Stratul semantic v5: navigare structurala + calcul evaluat de cod (C23, C25, C27-C29).",
           "model": MODEL, "la_limita_de_pasi_C29": [r["id"] for r in ies if r.get("tip_abtinere") == "C29"],
           "abtineri_C23": [r["id"] for r in ies if r.get("tip_abtinere") == "C23"],
           "reincercari_C23": [r["id"] for r in ies if r["apel"].get("reincercari_C23")],
           "max_pasi": MAX_PASI, "n": len(ies), "raspunse": sum(1 for r in ies if r["stare"] == "RASPUNS"),
           "respinse_de_verificare": sum(1 for r in ies if r.get("verificare") and not r["verificare"]["trece"]),
           "incomplete_detectate": sum(1 for r in ies if r.get("tip_abtinere") == "INCOMPLET"),
           "de_la_modelul_de_rezerva": [r["id"] for r in ies if r["apel"].get("fallback")],
           "pasi_medii": round(sum(r["apel"]["pasi_navigare"] for r in ies) / float(len(ies)), 2),
           "tokeni": tok, "cost_usd": round(sum(r["apel"]["cost_usd"] for r in ies), 4),
           "secunde_total": round(sum(r["apel"]["secunde"] for r in ies), 2),
           "reluat_din_partial": sorted(facute), "raspunsuri": ies}
    json.dump(rez, open(dest, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
    return rez


if __name__ == "__main__":
    import sys
    # --set2 / --set3: masuratorile pe seturi noi. Motorul citeste din CSV numai COLOANE_PERMISE.
    SETURI = {"--set2": ("set2", "/home/costin/ghid_incoming/FiscalOS_intrebari_set2_50.csv"),
              "--set3": ("set3", "/home/costin/ghid_incoming/FiscalOS_intrebari_set3_50.csv")}
    ales = next((SETURI[a] for a in sys.argv[1:] if a in SETURI), None)
    ids = [a for a in sys.argv[1:] if a.startswith("Q")]
    dest = os.path.join(_RAD, "artefacte", "intrebari", "raspunsuri_navigare_%s%s.json"
                        % (ales[0] if ales else "v5", "_proba" if ids else ""))
    r = ruleaza(dest, ids or None, ales[1] if ales else None)
    print("navigare: %d/%d raspunse | respinse %d | incomplete %d | pasi medii %.1f | %s | $%.4f | %.0f s"
          % (r["raspunse"], r["n"], r["respinse_de_verificare"], r["incomplete_detectate"],
             r["pasi_medii"], r["tokeni"], r["cost_usd"], r["secunde_total"]))
