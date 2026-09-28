# -*- coding: utf-8 -*-
"""C12 — STRATUL DE SURSE OFICIALE: consolidatele la zi, aduse de FiscalOS din legislatie.just.ro.

DECIZIA ARHITECTULUI: "se aduce in corpus consolidatul la zi al actelor de baza ... FiscalOS le ia
din sursa oficiala, intr-un strat propriu, separat de instantaneul iConta, cu provenienta, data formei
consolidate si SHA in manifest. Instantaneul iConta ramane neatins."

SEPARAT, si cum se folosesc impreuna. Fisierele stau in `surse_oficiale/`, cu manifestul lor
(`surse_oficiale/MANIFEST.json`), iar atomii in `artefacte/atomi_oficiale/`. `corpus/` si
`artefacte/atomi/` nu se ating. La citire (`potrivire.Corpus`), un act adus oficial INLOCUIESTE actul
cu acelasi nume din instantaneu - o singura versiune per act, cea mai noua -, iar inlocuirea se
inregistreaza (`corp.sursa_act`). Numele actului ramane acelasi, ca id-urile atomilor (`cod_fiscal_227_
2015_consolidat#art291/alin1`) sa se rezolve la fel: s-a schimbat textul din spatele lor, nu adresa.

CE ACTE. Stabilite FARA cheia intrebarilor: cele trei din cerinta C12 (Codul fiscal, Legea 70/2015,
OPANAF 3769/2015) si actele de baza MARI (>= 1000 de atomi) din corpus care nu sunt un consolidat la
zi (nicio nota de consolidare dupa 01.01.2025): Codul de procedura fiscala, normele Codului fiscal
(HG 1/2016), reglementarile contabile (OMFP 1802/2014).

CUM SE AJUNGE LA TEXT, masurat. Pentru actele mari, pagina actului de aprobare (Legea 207/2015) e un
CIOT: antetul si o trimitere `S_REF` spre documentul care conţine codul insusi
(`DetaliiDocumentAfis/<id>`). Si "forma printabila" e ciot. Se urmeaza trimiterile `S_REF`. Asta e si
raspunsul la limita notata de iConta in PORTAL_IDS.json ("forma consolidata la alt id, negasit").
"""
import hashlib
import json
import os
import re
import time

from fiscalos import atomizare, portal, strat_text

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(_RAD, "surse_oficiale")
DIR_ATOMI = os.path.join(_RAD, "artefacte", "atomi_oficiale")

# (numele actului din corpus pe care il inlocuieste, id-ul de pe portal, de ce)
ACTE = [
    ("cod_fiscal_227_2015_consolidat", "171280", "C12"),
    ("legea_70_2015_consolidat", "167088", "C12"),
    ("opanaf_3769_2015_d394_baza", "174685", "C12"),
    ("legea_207_2015_consolidat", "170005", "act de baza mare, fara consolidare la zi in corpus"),
    ("hg_1_2016_norme_cod_fiscal", "174822", "act de baza mare, fara consolidare la zi in corpus"),
    ("omfp_1802_2014", "164320", "act de baza mare, fara consolidare la zi in corpus"),
]
_SREF = re.compile(r'class="S_REF"><A href="[^"]*DetaliiDocumentAfis/(\d+)"', re.I)


def _sha(b):
    return hashlib.sha256(b).hexdigest()


def aduce(acte=ACTE):
    os.makedirs(DIR, exist_ok=True)
    p = portal.Portal()
    manifest = {"_ce": "Consolidatele la zi aduse de FiscalOS din sursa oficiala (C12). Separate de "
                       "instantaneul iConta, care rămâne neatins.",
                "sursa": portal.BAZA, "user_agent": portal.UA, "adus_la": time.strftime(
                    "%Y-%m-%dT%H:%M:%S"), "acte": {}}
    for act, id_portal, de_ce in acte:
        t0 = time.time()
        corp, info = p.act(id_portal)
        documente = [(id_portal, corp, info)]
        # un act de aprobare care e ciot trimite, prin S_REF, la documentul cu textul (codul, normele)
        for id_ref in _SREF.findall(corp.decode("utf-8", "replace")):
            c2, i2 = p.act(id_ref)
            documente.append((id_ref, c2, i2))
        fisiere = []
        for id_d, c, i in documente:
            nume = "%s__%s.html" % (act, id_d)
            with open(os.path.join(DIR, nume), "wb") as f:
                f.write(c)
            fisiere.append({"fisier": nume, "id_portal": id_d, "id_forma": i.get("id_forma"),
                            "url": "%s/Public/DetaliiDocument%s/%s" % (
                                portal.BAZA, "Afis" if id_d != id_portal else "", id_d),
                            "titlu": i.get("titlu"), "consolidare": i.get("consolidare_curenta"),
                            "e_forma_curenta": i.get("afisata_e_cea_curenta"),
                            "articole": i.get("articole_in_pagina"), "octeti": len(c),
                            "sha256": _sha(c)})
        cons = [x["consolidare"] for x in fisiere if x["consolidare"]]
        manifest["acte"][act] = {
            "id_portal": id_portal, "de_ce": de_ce, "fisiere": fisiere,
            "data_formei_consolidate": max(cons, key=lambda d: d[6:] + d[3:5] + d[:2]) if cons else None,
            "articole_total": sum(x["articole"] for x in fisiere),
            "secunde": round(time.time() - t0, 1)}
        print("%-36s %s | %d documente | %d articole | consolidare %s | %.1f s"
              % (act, id_portal, len(fisiere), manifest["acte"][act]["articole_total"],
                 manifest["acte"][act]["data_formei_consolidate"], time.time() - t0))
    with open(os.path.join(DIR, "MANIFEST.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    return manifest


# Portalul marcheaza structura cu clase pe <span>-uri INLINE: S_ART_TTL ("Articolul 291"), S_ART_DEN
# (denumirea), S_ALN_TTL ("(1)"), S_LIT_TTL ("a)"), S_PCT_TTL, S_NTA (notele de modificare) etc.
# Conversia generica html->text le lipea pe un rand ("Articolul 291 Cotele (1) Cota standard..."),
# iar parserul cere unitatea singura pe rand (forma F1). Masurat inainte de reparatie: Codul fiscal
# dadea 1.143 de atomi din 3.137 de articole, Legea 70/2015 11 din 71. Se pune un rand nou inaintea
# fiecarui span STRUCTURAL - informatia de structura e a portalului, nu ghicita.
_SPAN_STRUCT = re.compile(
    r'(<span[^>]*class="S_(?:ART|ART_TTL|ART_DEN|ART_BDY|ALN|ALN_TTL|ALN_BDY|LIT|LIT_TTL|LIT_BDY|'
    r'PCT|PCT_TTL|PCT_BDY|NTA|NTA_TTL|NTA_PAR|PAR|CAP|CAP_TTL|CAP_DEN|SEC|SEC_TTL|SEC_DEN|TTL|'
    r'TTL_TTL|TTL_DEN|PRT|PRT_TTL|PRT_DEN|ANX|ANX_TTL|ANX_DEN|CIT|DEN|HDR)"[^>]*>)', re.I)


# V2 (decizia C22): elementele <span class="S_NTA"> ("Nota") conţin, pe langa explicatii, articole
# CITATE din actele modificatoare ("Articolul III din OG 22/2025 prevede: (1) ... (6) ..."), cu propriile
# lor marcaje de alineat. Tratate ca structura, ele deschideau un pseudo-articol "III" in MIJLOCUL
# art. 310 al Codului fiscal, iar alineatele reale (3)-(6^2) ale art. 310 se lipeau de el - de aceea
# `art310/alin6` lipsea. O nota nu e structura: se aplatizeaza intr-un singur rand, marcat NOTA_MARCAJ,
# atasat atomului curent. Notele de VALABILITATE "(la 01-09-2025, ...)" stau in S_PAR si nu se ating.
NOTA_MARCAJ = "⟦NOTĂ⟧"
_SPAN_DESCHIS = re.compile(r"<span\b", re.I)
_SPAN_INCHIS = re.compile(r"</span\s*>", re.I)


def _aplatizeaza_note(h):
    ies, poz = [], 0
    for m in re.finditer(r'<span[^>]*class="S_NTA"[^>]*>', h):
        if m.start() < poz:
            continue                          # o nota imbricata intr-una deja aplatizata
        ies.append(h[poz:m.start()])
        adanc, i = 1, m.end()
        while adanc and i < len(h):
            d = _SPAN_DESCHIS.search(h, i)
            z = _SPAN_INCHIS.search(h, i)
            if z is None:
                i = len(h)
                break
            if d is not None and d.start() < z.start():
                adanc, i = adanc + 1, d.end()
            else:
                adanc, i = adanc - 1, z.end()
        text = strat_text.html_in_text(h[m.end():i])
        ies.append("<br/>%s %s<br/>" % (NOTA_MARCAJ, " ".join(text.split())))
        poz = i
    ies.append(h[poz:])
    return "".join(ies)


def html_portal_in_text(h):
    h = _aplatizeaza_note(h)
    return strat_text.html_in_text(_SPAN_STRUCT.sub(lambda m: "<br/>" + m.group(1), h))


def atomizeaza():
    """Atomii actelor oficiale, cu ACELASI parser ca instantaneul. Documentele unui act se concateneaza."""
    man = json.load(open(os.path.join(DIR, "MANIFEST.json"), encoding="utf-8"))
    os.makedirs(DIR_ATOMI, exist_ok=True)
    rez = {}
    for act, v in man["acte"].items():
        texte = []
        for x in v["fisiere"]:
            b = open(os.path.join(DIR, x["fisier"]), "rb").read()
            assert _sha(b) == x["sha256"], ("fisier modificat dupa aducere", x["fisier"])
            texte.append(html_portal_in_text(b.decode("utf-8", "replace")))
        atomi, structura = atomizare.atomizeaza_text(act, "\n\n".join(texte))
        for a in atomi:
            a["sursa"] = "oficial"
        with open(os.path.join(DIR_ATOMI, act + ".jsonl"), "w", encoding="utf-8") as f:
            for a in atomi:
                f.write(json.dumps(a, ensure_ascii=False) + "\n")
        rez[act] = {"n": len(atomi), "structura": structura,
                    "cu_valabilitate": sum(1 for a in atomi if a["valabil_din"]),
                    "ultima_nota": max((a["valabil_din"] for a in atomi if a["valabil_din"]),
                                       default=None),
                    "data_formei_consolidate": v["data_formei_consolidate"]}
    with open(os.path.join(DIR_ATOMI, "_raport.json"), "w", encoding="utf-8") as f:
        json.dump(rez, f, ensure_ascii=False, indent=1)
    return rez


if __name__ == "__main__":
    import sys
    if "--aduce" in sys.argv:
        aduce()
    r = atomizeaza()
    for act, v in r.items():
        print("%-36s %6d atomi | %s | note %d, ultima %s | forma consolidata %s"
              % (act, v["n"], v["structura"], v["cu_valabilitate"], v["ultima_nota"],
                 v["data_formei_consolidate"]))
