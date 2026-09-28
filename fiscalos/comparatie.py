# -*- coding: utf-8 -*-
"""COMPARATIA raspunsurilor motorului cu cheia din CSV - singurul modul care citeste cheia.

RULEAZA DUPA ce raspunsurile au fost scrise si comise (commit f1997a8 pentru v0). Regulile de mai jos
au fost scrise INAINTE ca modulul sa citeasca vreo coloana a cheii - ca notarea sa nu se potriveasca
dupa ce se vede ce iese.

TREI STARI, cum cere decizia: CORECT / GRESIT / NU POT RASPUNDE.

  CORECT   raspunsul poarta FAPTUL PRINCIPAL al cheii (primul numar cu unitate: procent, suma, numar
           de zile/luni/ani, data) SI citeaza acelasi articol din acelasi act ca temeiul cheii.
           Cand cheia nu are niciun fapt numeric, ajunge articolul.
           Excepţie, pentru tipul INCOMPLETA: o abţinere al carei motiv e lipsa datelor e CORECTA daca
           si cheia spune ca lipsesc date - comportamentul cerut acolo e tocmai sa nu raspunzi.
  GRESIT   motorul a raspuns, dar nu indeplineste CORECT.
  NU POT   motorul s-a abţinut (in afara excepţiei de mai sus).

DE CE AMBELE CONDITII PENTRU CORECT. Numai valoarea: un atom greşit poate purta din intamplare
numarul corect (lectia bancului de mutaţii). Numai articolul: un extras din articolul corect poate
spune alt lucru decat intrebarea cere. Cerinta dubla e severa, si se spune: un raspuns corect in fond,
citat de pe alt articol decat cheia, iese GRESIT. Detaliile per intrebare sunt publicate, ca un om sa
poata rejudeca oricare rand.
"""
import csv
import json
import os
import re
import time

from fiscalos import potrivire

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = "/home/costin/ghid_incoming/FiscalOS_intrebari_test_50.csv"

_FAPT = re.compile(
    r"(\d{1,3}(?:[.,]\d{1,3})*\s*%)"                                   # procent
    r"|(\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d+(?:,\d+)?)\s*(?:de\s+)?lei"   # suma lei
    r"|(\d{1,3}(?:\.\d{3})+|\d+)\s*(?:de\s+)?euro"                    # suma euro
    r"|(\d{1,3})\s+(?:de\s+)?(zile|luni|ani)"                         # durata
    r"|(\d{1,2}\.\d{1,2}\.\d{4})"                                     # data
    r"|(\d{1,2}\s+(?:ianuarie|februarie|martie|aprilie|mai|iunie|iulie|august|septembrie|"
    r"octombrie|noiembrie|decembrie)(?:\s+\d{4})?)"                        # data in litere
)
# DEFECT DE COMPARATOR (al treilea, gasit dupa rularea stratului semantic): datele scrise in litere
# ("25 iunie 2027") nu se recunosteau ca fapte. La Q-PRF-03 cheia spune "25 iunie 2027 inclusiv (nu
# 25 martie). Nota: validatorul ... testat la 03.08.2026", deci "faptul principal" devenea data
# NOTEI, 03.08.2026 - iar un raspuns corect ("25 iunie ... a anului urmator") iesea GRESIT. Faptul
# de tip data in litere se compara pe zi + luna (anul poate fi dat relativ: "anul urmator").
_LIPSA = re.compile(r"depinde|lipse|nu se poate (stabili|raspunde|determina)|insuficient|"
                    r"trebuie (precizat|stiut|cunoscut)|necesar(a|e)? (informati|date)|"
                    r"nu rezulta|incomplet|neprecizat", re.I)


# C28 (defect de clasa, gasit dupa rularea v4): o suma se compara ca NUMAR, nu ca sir. "2.020 lei" si
# "2020 lei", "1.031,25" si "1031,25", "0,5%" si "0.5%" sunt aceeasi valoare; comparatia pe sir le
# despartea. Separatorul de mii se scoate, zecimala se scrie cu virgula, zecimalele nule cad.
def _suma(x):
    x = x.replace(" ", "")
    if re.match(r"^\d{1,3}(\.\d{3})+(,\d+)?$", x):
        x = x.replace(".", "")
    elif re.match(r"^\d+\.\d{1,2}$", x):
        x = x.replace(".", ",")
    return re.sub(r",0+$", "", x)


# C28: un fapt dintr-o propozitie NEGATA a cheii nu e faptul ei principal. "Nu 25% x 2.162,50 =
# 540,63 lei, ci minimul: ... 1.031,25 lei" si "25 iunie 2027 (nu 25 martie)" numesc intai valoarea
# RESPINSA. Se taie "nu ..." pana la ", ci" sau pana la paranteza care il inchide.
_NEGAT = re.compile(r"\bnu\b[^;()]*?(?=,\s*ci\b|\))")


def _fapte(text, fara_negate=False):
    t = potrivire.norm(text or "")
    if fara_negate:
        t = _NEGAT.sub(" ", t)
    ies = []
    for m in _FAPT.finditer(t):
        if m.group(1):
            ies.append(_suma(re.sub(r"\s+", "", m.group(1)).rstrip("%")) + "%")
        elif m.group(2):
            ies.append(_suma(m.group(2)) + " lei")
        elif m.group(3):
            ies.append(_suma(m.group(3)) + " euro")
        elif m.group(4):
            ies.append("%s %s" % (m.group(4), m.group(5)))
        elif m.group(6):
            ies.append(m.group(6))
        elif m.group(7):
            ies.append(" ".join(m.group(7).split()[:2]))          # zi + luna
    return ies


# ── familia actului: aceeasi pentru un cod si redarile/modificarile lui ─────────────────────────
_FAMILII = [
    (re.compile(r"cod(ul)? fiscal|legea 227/2015|l\.? ?227/2015", re.I), "cf"),
    (re.compile(r"cod(ul)? de procedura fiscala|legea 207/2015|\bcpf\b", re.I), "cpf"),
    (re.compile(r"codul muncii|legea 53/2003", re.I), "cm"),
    (re.compile(r"hg 1/2016|norme(le)? metodologice", re.I), "norme"),
]


def _familie_act_din_nume(act):
    a = act.lower()
    if a.startswith(("cod_fiscal", "cf_")):
        return "cf"
    if a.startswith("legea_207_2015"):
        return "cpf"
    if a.startswith("legea_53_2003"):
        return "cm"
    if a.startswith("hg_1_2016"):
        return "norme"
    m = re.match(r"([a-z]+)_?(\d+)_(\d{4})", a)
    return "%s_%s_%s" % (m.group(1).replace("legea", "lege"), m.group(2), m.group(3)) if m else a


def _temeiuri_cheie(text):
    """[(familie, articol)] numite in temeiul cheii."""
    t = potrivire.norm(text or "")
    # C28: o paranteza cu cuvinte e PROVENIENTA ("(mod. OUG 89/2025)", "(forma OPANAF 2194/2025)",
    # "(cota 21%)"), nu temeiul: actul numit in ea nu e actul articolului. "(1)" si "(5^6)" raman.
    t = re.sub(r"\((?=[^)]*[a-z]{3})[^()]*\)", " ", t)
    ies = []
    fam_anterioara = None
    for bucata in re.split(r";|\bsi\b(?=\s+[a-z])", t):
        fam = None
        for rx, f in _FAMILII:
            if rx.search(bucata):
                fam = f
                break
        if fam is None:
            m = re.search(r"\b(legea|lege|oug|og|hg|omfp|opanaf|ordin)\s+(?:nr\.?\s*)?(\d+)/(\d{4})",
                          bucata)
            if m:
                fam = "%s_%s_%s" % (m.group(1).replace("legea", "lege"), m.group(2), m.group(3))
        if fam is None and re.search(r"omfp\s*1802/2014|reglementari contabile", bucata):
            fam = "omfp_1802_2014"
        # C28: "Cod fiscal art. 291 alin. (1); art. 298 alin. (1)-(3)" - bucata fara act continua
        # actul bucatii dinainte (inainte ramanea fara act si nu se potrivea cu nimic)
        if fam is None:
            fam = fam_anterioara
        fam_anterioara = fam
        # articole arabe SI romane: actele de sine statatoare (OUG 89/2025 art. III) numara roman
        for m in re.finditer(r"\bart\.?\s*(\d+(?:\^\d+)?|[ivxlcdm]+)\b", bucata):
            ies.append((fam, m.group(1).upper() if not m.group(1)[0].isdigit() else m.group(1)))
        # `pct.` pentru ORICE act, nu numai pentru norme: Reglementarile contabile (OMFP 1802/2014)
        # isi numeroteaza prevederile pe puncte. Prima versiune le citea numai la norme, deci cheile
        # OMFP ieseau fara niciun temei, si comparatorul le trata ca "temei indeplinit" (vezi mai jos).
        if not re.search(r"\bart\.", bucata):
            for m in re.finditer(r"\bpct\.?\s*(\d+)", bucata):
                ies.append((fam, "pct" + m.group(1)))
    return ies


def _temei_nostru(r, corp):
    ies = []
    for a in r.get("argument", [])[:1]:                 # numai atomul care RASPUNDE, nu contextul
        at = corp.dupa_id.get(a["atom"])
        if at is None:
            continue
        fam = _familie_act_din_nume(at["act"])
        if fam.startswith("omfp_1802_2014"):
            fam = "omfp_1802_2014"
        if at.get("articol"):
            art = str(at["articol"]).replace(" ", "")
            ies.append((fam, art.upper() if not art[:1].isdigit() else art))
        for seg in at["id"].split("#", 1)[1].split("/"):
            if seg.startswith("pct"):
                ies.append((fam, seg.split("~")[0]))
    return ies


def compara(fis_raspunsuri=None):
    fis_raspunsuri = fis_raspunsuri or os.path.join(_RAD, "artefacte", "intrebari",
                                                    "raspunsuri.json")
    R = {r["id"]: r for r in json.load(open(fis_raspunsuri, encoding="utf-8"))["raspunsuri"]}
    corp = potrivire.Corpus()
    rez = []
    with open(CSV, encoding="utf-8") as f:
        cheie = list(csv.DictReader(f))
    for k in cheie:
        r = R[k["id"]]
        fapte_cheie = _fapte(k["raspuns_asteptat"], fara_negate=True)
        tem_cheie = _temeiuri_cheie(k["temei"])
        linie = {"id": k["id"], "tip": k["tip"], "stare_motor": r["stare"],
                 "raspuns_motor": r.get("raspuns"), "raspuns_asteptat": k["raspuns_asteptat"],
                 "temei_asteptat": k["temei"], "fapt_principal_cheie": fapte_cheie[:1],
                 "temeiuri_cheie": tem_cheie}
        if r["stare"] == "NU_POT_RASPUNDE":
            if k["tip"] == "INCOMPLETA" and _LIPSA.search(potrivire.norm(k["raspuns_asteptat"])):
                linie.update(verdict="CORECT", de_ce="INCOMPLETA: motorul s-a abţinut, iar cheia "
                                                      "spune si ea ca lipsesc date")
            else:
                linie.update(verdict="NU_POT", de_ce=r["motiv"][:200])
            rez.append(linie)
            continue
        noi = _temei_nostru(r, corp)
        text_nostru = (r.get("raspuns") or "") + " " + json.dumps(r.get("calcul") or {})
        fapte_noi = _fapte(text_nostru)
        valoare_ok = (not fapte_cheie) or (potrivire.norm(fapte_cheie[0]).replace(" ", "")
                                           in [potrivire.norm(x).replace(" ", "") for x in fapte_noi])
        # DEFECT DE COMPARATOR, reparat dupa prima rulare si raportat ca atare: cand temeiul cheii
        # nu se putea citi mecanic, `temei_ok` era None, iar None trecea drept "indeplinit". Asa au
        # ieşit CORECT trei raspunsuri care citau ALT ACT decat cheia (Codul fiscal in loc de
        # Reglementarile contabile OMFP 1802/2014). Un comparator care nu poate verifica articolul nu
        # poate certifica CORECT. Reparaţia face notarea mai STRICTA, nu mai blanda.
        if tem_cheie:
            temei_ok = bool(set(noi) & set(tem_cheie))
        elif (k["temei"] or "").strip():
            temei_ok = False
        else:
            temei_ok = None
        linie.update(temei_motor=noi, fapte_motor=fapte_noi[:6], valoare_ok=valoare_ok,
                     temei_ok=temei_ok)
        if valoare_ok and (temei_ok or temei_ok is None):
            linie.update(verdict="CORECT", de_ce="faptul principal si articolul coincid")
        else:
            lipsa = []
            if not valoare_ok:
                lipsa.append("faptul principal al cheii (%s) nu e in raspuns" % fapte_cheie[:1])
            if temei_ok is False:
                lipsa.append(("articolul citat %s nu e printre cele ale cheii %s" % (noi, tem_cheie))
                             if tem_cheie else "temeiul cheii nu s-a putut citi mecanic - fara el, "
                                               "CORECT nu se poate certifica (de rejudecat de om)")
            linie.update(verdict="GRESIT", de_ce="; ".join(lipsa))
        rez.append(linie)
    scor = {v: sum(1 for x in rez if x["verdict"] == v) for v in ("CORECT", "GRESIT", "NU_POT")}
    # ── DECIZIA C1: scorul de REFERINTA e cel PE FOND ──────────────────────────────────────────
    # Regula de notare de mai sus rămâne neschimbata (istoricul ramane comparabil), dar scorul de
    # referinta numara CORECT numai ce motorul a RASPUNS corect. Orice abţinere e NU POT, inclusiv
    # pe INCOMPLETA; acelea se raporteaza separat, cu distinctia pe care arhitectul a cerut-o:
    # a DETECTAT motorul incompletitudinea (`tip_abtinere == "INCOMPLET"`), sau s-a abţinut din alt
    # motiv?
    for x in rez:
        x["verdict_pe_fond"] = ("CORECT" if x["stare_motor"] == "RASPUNS" and x["verdict"] == "CORECT"
                                else "GRESIT" if x["stare_motor"] == "RASPUNS" else "NU_POT")
    scor_ref = {v: sum(1 for x in rez if x["verdict_pe_fond"] == v)
                for v in ("CORECT", "GRESIT", "NU_POT")}
    abt_inc = []
    for x in rez:
        if x["tip"] == "INCOMPLETA" and x["stare_motor"] != "RASPUNS":
            r = R[x["id"]]
            abt_inc.append({"id": x["id"],
                            "incompletitudine_detectata": r.get("tip_abtinere") == "INCOMPLET",
                            "ce_lipseste_dupa_motor": r.get("lipsa") or [],
                            "cheia_spune_ca_lipsesc_date": bool(_LIPSA.search(
                                potrivire.norm(x["raspuns_asteptat"]))),
                            "motivul_motorului": (r.get("motiv") or "")[:200]})
    # ── DECIZIA C2: notarea rămâne stricta; "fapt corect, articol diferit" se listeaza separat ──
    fapt_ok_art_dif = [{"id": x["id"], "raspuns_motor": x.get("raspuns_motor"),
                        "articol_motor": x.get("temei_motor"), "articole_cheie": x["temeiuri_cheie"],
                        "temei_asteptat": x["temei_asteptat"]}
                       for x in rez if x["stare_motor"] == "RASPUNS" and x.get("valoare_ok")
                       and x.get("temei_ok") is False]
    return {"scor": scor, "scor_referinta_pe_fond": scor_ref,
            "abtineri_pe_INCOMPLETA": abt_inc, "fapt_corect_articol_diferit": fapt_ok_art_dif,
            "comparatii": rez, "comparat_la": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "fisier_raspunsuri": os.path.relpath(fis_raspunsuri, _RAD)}


if __name__ == "__main__":
    import sys
    fis = sys.argv[1] if len(sys.argv) > 1 else None
    r = compara(fis)
    print("scor:", r["scor"])
    out = os.path.join(_RAD, "artefacte", "intrebari",
                       "comparatie_%s.json" % (os.path.basename(fis or "raspunsuri.json")
                                                .replace("raspunsuri", "").strip("_.json") or "curent"))
    with open(out, "w", encoding="utf-8") as f:
        json.dump(r, f, ensure_ascii=False, indent=1)
    print("scris:", os.path.relpath(out, _RAD))
