# -*- coding: utf-8 -*-
"""URMARIREA LEGILOR PENTRU ICONTA (punctul 8), saptamanal, automat (cron).

1. Pentru fiecare act din stratul oficial (`surse_oficiale/MANIFEST.json`) intreaba portalul care e
   consolidarea curenta; daca difera de cea din manifest, actul are o forma noua.
2. Actele schimbate se aduc din nou, se atomizeaza, si trec prin detectorul de structura.
3. Parametrii iConta se reinventariaza (NUMAI din git HEAD, `iconta_head`) si se recompara cu corpusul.
   Fata de potrivirea anterioara: orice DIFERA nou sau schimbat si orice TEMEI schimbat (alt atom, sau
   alt text al aceluiasi atom) declanseaza PROPUNEREA URMATOARE - NEAPROBATA, niciodata aplicata.
4. Rezultatul, cu data verificarii, se scrie in `urmarire/rezultate/` si apare pe pagina (punctul 7c).

Actele din instantaneul iConta care nu au un id de portal nu se pot urmari aici: se numara si se spun.
Un act pe care portalul nu-l da (eroare) e NEVERIFICAT, nu "neschimbat" - tacerea nu se citeste ca
absenta (CLAUDE.md §2).
"""
import json
import os
import re
import sys
import time

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_REZ = os.path.join(_RAD, "urmarire", "rezultate")
F_MAN = os.path.join(_RAD, "surse_oficiale", "MANIFEST.json")


def _data(d):
    """'08.08.2026' -> '2026-08-08' (pentru ordine); altceva -> None."""
    m = re.match(r"^(\d{2})\.(\d{2})\.(\d{4})$", d or "")
    return "%s-%s-%s" % (m.group(3), m.group(2), m.group(1)) if m else None


def forme_noi(p, man, pauza_reluare=30):
    """{act: {...}} actele cu alta consolidare decat cea din manifest; plus erorile si numarul verificat.
    Un act cazut (timeout) se reia O DATA, la sfarsit; ce cade si atunci ramane NEVERIFICAT."""
    schimbate, erori, verificate = {}, {}, 0
    acte = sorted(man["acte"].items())
    verificate = _verifica_acte(p, acte, schimbate, erori)
    if erori:
        time.sleep(pauza_reluare)
        reluate = [(a, man["acte"][a]) for a in sorted(erori)]
        erori.clear()
        verificate += _verifica_acte(p, reluate, schimbate, erori)
    return schimbate, erori, verificate


def _verifica_acte(p, acte, schimbate, erori):
    verificate = 0
    for act, v in acte:
        prim = v["fisiere"][0]
        try:
            _corp, info = p.act(v["id_portal"])
        except Exception as e:                                # NEVERIFICAT, nu "neschimbat"
            erori[act] = "%s: %s" % (type(e).__name__, str(e)[:200])
            continue
        verificate += 1
        vechi, nou = prim.get("consolidare"), info.get("consolidare_curenta")
        if nou != vechi:
            schimbate[act] = {"id_portal": v["id_portal"], "de_ce": v["de_ce"], "consolidare_veche": vechi,
                              "consolidare_noua": nou, "data_formei_vechi": v["data_formei_consolidate"],
                              "mai_veche_decat_cea_din_manifest": bool(_data(nou) and _data(vechi)
                                                                       and _data(nou) < _data(vechi)),
                              "fisiere_vechi": [{k: x[k] for k in ("fisier", "sha256", "consolidare")}
                                                for x in v["fisiere"]]}
    return verificate


def _cheie(p):
    return p["parametru"]


def compara_potriviri(vechi, noi):
    """Ce s-a schimbat pentru iConta: DIFERA noi/schimbate si temeiuri schimbate. Fiecare rand poarta
    AMBELE parti (valoarea din codul iConta si textul legii), ca in propunere."""
    V = {_cheie(p): p for p in vechi}
    ies = []
    for p in noi:
        a = V.get(_cheie(p))
        parti = {"parametru": p["parametru"], "valoare_cod": p.get("valoare_cod"),
                 "unde_in_cod": p.get("unde_in_cod"), "valoare_lege": p.get("valoare_lege"),
                 "atom": p.get("atom"), "verbatim": p.get("atom_verbatim"),
                 "clasificare": p["clasificare"], "clasificare_anterioara": a and a["clasificare"]}
        motive = []
        if p["clasificare"] == "DIFERA" and (not a or a["clasificare"] != "DIFERA"
                                             or a.get("valoare_lege") != p.get("valoare_lege")
                                             or a.get("atom") != p.get("atom")):
            motive.append("DIFERA nou" if not a or a["clasificare"] != "DIFERA" else "DIFERA schimbat")
        if a and a.get("atom") and (a.get("atom") != p.get("atom")
                                    or a.get("atom_verbatim") != p.get("atom_verbatim")):
            motive.append("temei schimbat")
            parti.update(atom_anterior=a.get("atom"), verbatim_anterior=a.get("atom_verbatim"),
                         valoare_lege_anterioara=a.get("valoare_lege"))
        if not a:
            motive.append("parametru nou in iConta")
        if motive:
            ies.append(dict(parti, motive=motive))
    for k in set(V) - {_cheie(p) for p in noi}:
        ies.append({"parametru": k, "motive": ["parametru disparut din iConta"],
                    "clasificare_anterioara": V[k]["clasificare"]})
    return ies


def _versiune_urmatoare():
    vs = [int(m.group(1)) for d in os.listdir(os.path.join(_RAD, "propuneri"))
          for m in [re.match(r"^v(\d+)$", d)] if m]
    return "v%d" % (max(vs) + 1)


def verifica(p=None, scrie=True):
    from fiscalos import (detector_structura, iconta_head, inventar_iconta, portal, potrivire,
                          propunere, surse_oficiale)
    t0, durate = time.time(), {}
    rez = {"data_verificarii": time.strftime("%Y-%m-%d %H:%M:%S"), "radacina": _RAD,
           "portal": "simulat" if p is not None else portal.BAZA}
    p = p or portal.Portal()
    man = json.load(open(F_MAN, encoding="utf-8"))
    schimbate, erori, verificate = forme_noi(p, man)
    durate["verificare_portal"] = round(time.time() - t0, 1)
    rez.update(acte_urmarite=len(man["acte"]), acte_verificate=verificate, neverificate=erori,
               forme_noi=schimbate)
    iconta_commit = iconta_head.commit()
    rez["iconta_commit_git"] = iconta_commit

    t = time.time()
    if schimbate:
        # 2. forma noua: se aduce (manifestul pastreaza restul actelor neatinse), se atomizeaza, detectorul
        for act in schimbate:
            del man["acte"][act]
        with open(F_MAN, "w", encoding="utf-8") as f:
            json.dump(man, f, ensure_ascii=False, indent=1)
        surse_oficiale.aduce([(a, v["id_portal"], v["de_ce"]) for a, v in schimbate.items()],
                             incremental=True, p=p)
        man2 = json.load(open(F_MAN, encoding="utf-8"))
        for a in schimbate:
            schimbate[a]["data_formei_noi"] = man2["acte"][a]["data_formei_consolidate"]
        surse_oficiale.atomizeaza()
        durate["aducere_si_atomizare"] = round(time.time() - t, 1)
        t = time.time()
        det = detector_structura.detecteaza()
        rez["detector_structura"] = {a: {k: det[a][k] for k in ("S1_alineate_duplicate", "S2_acoperire",
                                                               "S3_articole_imbricate", "S4_articole_in_nota",
                                                               "categorie")}
                                     for a in schimbate if a in det}
        rez["detector_structura_curat"] = [a for a in schimbate if a not in det]
        durate["detector"] = round(time.time() - t, 1)

    # 3. iConta din HEAD, recomparat - si cand legea nu s-a schimbat, daca iConta s-a schimbat
    f_pot = os.path.join(_RAD, "artefacte", "potriviri.json")
    f_inv = os.path.join(_RAD, "artefacte", "inventar_iconta.json")
    inv_vechi = json.load(open(f_inv, encoding="utf-8"))
    pot_vechi = json.load(open(f_pot, encoding="utf-8"))["potriviri"]
    iconta_schimbat = inv_vechi.get("iconta_commit_git") != iconta_commit
    rez["iconta_schimbat_de_la_ultima_comparatie"] = iconta_schimbat
    schimbari = []
    if schimbate or iconta_schimbat:
        t = time.time()
        inventar_iconta.inventariaza()
        noi = potrivire.potriveste_tot()["potriviri"]
        schimbari = compara_potriviri(pot_vechi, noi)
        durate["iconta_si_potrivire"] = round(time.time() - t, 1)
    rez["schimbari_pentru_iconta"] = schimbari

    # 4. propunerea urmatoare, la orice DIFERA nou/schimbat sau temei schimbat
    declansatoare = [s for s in schimbari if {"DIFERA nou", "DIFERA schimbat", "temei schimbat"} & set(s["motive"])]
    if declansatoare:
        t = time.time()
        propunere.VERSIUNE = _versiune_urmatoare()
        propunere.construieste()
        dest = os.path.join(_RAD, "propuneri", propunere.VERSIUNE)
        with open(os.path.join(dest, "SCHIMBARI_URMARIRE.json"), "w", encoding="utf-8") as f:
            json.dump({"_ce": "De ce exista aceasta propunere: verificarea saptamanala a legilor. "
                              "NEAPROBATA; nu se aplica niciodata automat in iConta.",
                       "data_verificarii": rez["data_verificarii"], "forme_noi": schimbate,
                       "iconta_commit_git": iconta_commit, "schimbari": declansatoare},
                      f, ensure_ascii=False, indent=1)
        _raport_schimbari(dest, rez, declansatoare)
        rez["propunere"] = "propuneri/%s (NEAPROBATĂ)" % propunere.VERSIUNE
        durate["propunere"] = round(time.time() - t, 1)

    rez["rezumat"] = _rezumat(rez, declansatoare)
    rez["detalii"] = _detalii(rez, declansatoare)
    durate["total"] = round(time.time() - t0, 1)
    rez["durate_secunde"] = durate
    if scrie:
        os.makedirs(DIR_REZ, exist_ok=True)
        with open(os.path.join(DIR_REZ, time.strftime("%Y-%m-%d_%H%M%S") + ".json"), "w", encoding="utf-8") as f:
            json.dump(rez, f, ensure_ascii=False, indent=1)
    return rez


def _rezumat(rez, declansatoare):
    nev = (" %d acte NEVERIFICATE (eroare de portal, și la reluare): %s — se reiau la verificarea următoare."
           % (len(rez["neverificate"]), ", ".join(sorted(rez["neverificate"])))) if rez["neverificate"] else ""
    if not rez["forme_noi"] and not rez["schimbari_pentru_iconta"]:
        return "nimic schimbat %s, nicio formă consolidată nouă%s.%s" % (
            "— toate cele %d acte verificate pe portal" % rez["acte_urmarite"] if not rez["neverificate"] else
            "în cele %d acte verificate (din %d)" % (rez["acte_verificate"], rez["acte_urmarite"]),
            "" if not rez["iconta_schimbat_de_la_ultima_comparatie"] else "; iConta s-a schimbat, fără efect", nev)
    s = "%d acte cu formă consolidată nouă (%s); %d schimbări pentru iConta" % (
        len(rez["forme_noi"]), ", ".join(rez["forme_noi"]) or "—", len(rez["schimbari_pentru_iconta"]))
    if declansatoare:
        s += "; %d DIFERĂ/temei schimbat → %s" % (len(declansatoare), rez["propunere"])
    else:
        s += "; niciun DIFERĂ sau temei schimbat, nicio propunere nouă"
    return s + "." + nev


def _detalii(rez, declansatoare):
    D = []
    for a, v in rez["forme_noi"].items():
        D.append("%s: consolidarea %s → %s" % (a, v["consolidare_veche"], v["consolidare_noua"]))
    for a, v in (rez.get("detector_structura") or {}).items():
        D.append("detector: %s semnalat (%s)" % (a, v["categorie"]))
    for s in rez["schimbari_pentru_iconta"]:
        if s in declansatoare:
            continue
        D.append("%s — %s (%s; nu declanșează propunere)" % (s["parametru"], "/".join(s["motive"]),
                                                             s.get("clasificare") or s.get("clasificare_anterioara")))
    for s in declansatoare:
        D.append("%s — %s: iConta are %s (%s), legea spune %s în %s: „%s”" % (
            s["parametru"], "/".join(s["motive"]), s.get("valoare_cod"), s.get("unde_in_cod"),
            s.get("valoare_lege"), s.get("atom"), (s.get("verbatim") or "")[:300]))
    for a, e in rez["neverificate"].items():
        D.append("NEVERIFICAT %s: %s" % (a, e))
    return D


def _raport_schimbari(dest, rez, declansatoare):
    L = ["", "## Urmărirea legilor — de ce există această propunere", "",
         "Verificarea din %s (automată, săptămânală). Propunerea e **NEAPROBATĂ**; nu se aplică niciodată "
         "automat în iConta." % rez["data_verificarii"], ""]
    for a, v in rez["forme_noi"].items():
        L.append("- **%s**: consolidarea %s → %s" % (a, v["consolidare_veche"], v["consolidare_noua"]))
    L += ["", "| Parametru | Ce | iConta (cod) | Legea | Atom | Text verbatim |", "|---|---|---|---|---|---|"]
    for s in declansatoare:
        L.append("| `%s` | %s | %s (`%s`) | %s | `%s` | %s |" % (
            s["parametru"], "/".join(s["motive"]), s.get("valoare_cod"), s.get("unde_in_cod"),
            s.get("valoare_lege"), s.get("atom"), (s.get("verbatim") or "").replace("|", "\\|")[:400]))
        if s.get("verbatim_anterior") is not None:
            L.append("| | înainte | | %s | `%s` | %s |" % (s.get("valoare_lege_anterioara"), s.get("atom_anterior"),
                                                           (s.get("verbatim_anterior") or "").replace("|", "\\|")[:400]))
    f = os.path.join(dest, "RAPORT.md")
    with open(f, "a", encoding="utf-8") as g:
        g.write("\n".join(L) + "\n")


if __name__ == "__main__":
    r = verifica()
    print(r["data_verificarii"], "|", r["rezumat"], "|", r["durate_secunde"])
    sys.exit(0)
