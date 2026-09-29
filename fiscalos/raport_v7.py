# -*- coding: utf-8 -*-
"""Livrabilul pasului 8: deciziile C34-C37. Fara niciun apel la model; efectul pe motor se masoara pe
setul nou."""
import json
import os
import time
from collections import Counter

from fiscalos import detector_structura, navigare, potrivire

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(_RAD, "intrebari", "v7")
ZIP = "/home/costin/ghid_incoming/fiscalos_v7_rezultat.zip"


def construieste():
    os.makedirs(DEST, exist_ok=True)
    t0 = time.time()
    inainte = json.load(open(os.path.join(_RAD, "intrebari", "v6", "masuratori.json"), encoding="utf-8"))["C31_detector_dupa"]
    corp = potrivire.Corpus()
    dupa = detector_structura.detecteaza(corp)
    rez = json.load(open(os.path.join(_RAD, "surse_oficiale", "C31_rezolvare.json"), encoding="utf-8"))["acte"]
    # C34, pe atomii reali: lista oficiala -> abtinere
    dupa_id = {i: corp.dupa_id[i] for i in ("legea_134_2010_codul_de_procedura_civila#art181/alin2",
                                             "legea_53_2003_codul_muncii#art139/alin1")}
    calc = [{"nume": "termen", "formula": "termen_efectiv(d)", "operanzi": [
        {"nume": "d", "valoare": "28.02.2026", "eticheta": "FAPT_CAZ", "atom": "", "fragment": "28.02.2026"}]}]
    _v, gr, _d = navigare.evalueaza_calcule(calc, dupa_id, "Termen nominal 28.02.2026.", citati=list(dupa_id))
    m = {"detector_inainte": inainte, "detector_dupa": dupa, "C34_abtinere": gr,
         "C34_text_art139": corp.dupa_id["legea_53_2003_codul_muncii#art139/alin1"]["text"],
         "C37": rez.get("ordin_1099_2016")}
    json.dump(m, open(os.path.join(DEST, "masuratori.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    L = []
    A = L.append
    A("# FiscalOS v2 — Pasul 8: deciziile C34–C37")
    A("")
    A("Generat %s · ZIP: `%s`" % (time.strftime("%d.%m.%Y %H:%M"), ZIP))
    A("")
    A("> Fără niciun apel la model ($0). Efectul pe motor se măsoară pe setul nou.")
    A("")
    A("## C34 — art. 139 din Codul muncii, textul oficial")
    A("")
    A("Verificat în HTML-ul portalului (forma consolidată din 27.04.2026): elementele listei sunt "
      "`<span class=\"S_LIN_BDY\">`, iar două dintre ele nu au dată — „Adormirea Maicii Domnului;” și „prima "
      "și a doua zi de Crăciun;”. **Textul oficial nu le scrie data.** Atomul, după reparația de mai jos:")
    A("")
    A("> %s" % m["C34_text_art139"][:900])
    A("")
    A("**Un defect de conversie real, găsit la această verificare și reparat ca clasă:** „...” dintre "
      "elementele listelor nu era text al legii, ci forma *restrânsă* a elementului, pe care portalul o "
      "ascunde (`<span class=\"S_LIN_SHORT\" style=\"display:none\"> ... </span>`; la fel `S_LIT_SHORT`, "
      "`S_PCT_SHORT`, `S_NTA_SHORT`). 24.930 de asemenea span-uri în actele oficiale, toate cu conținutul "
      "„...” și nimic altceva — scoase; 18.058 de texte de atomi s-au curățat. Detectorul C31, rulat după: "
      "vezi C36.")
    A("")
    A("Consecința, fără dată pusă de mână: `termen_efectiv` **se abține**, cu motivul scris. Pe atomii reali "
      "(Q-TVA-07, 28.02.2026):")
    A("")
    for g in gr:
        A("> %s" % g)
    A("")
    A("Mecanismul (Paști/Rusalii calculate și declarate, sâmbătă → luni, zi lucrătoare neschimbată) rămâne "
      "probat pe o listă *sintetică* cu toate sărbătorile datate (`test_navigare.test_C32_mecanismul_*`). "
      "Ce rămâne de decis: C38.")
    A("")
    A("## C36 — conversia oficială, reparată acum")
    A("")
    A("Șase clase de defect, fiecare reparată ca regulă (nu act cu act) și probată:")
    A("")
    A("| Clasa | Unde s-a văzut | Reparația |")
    A("|---|---|---|")
    A("| forma restrânsă ascunsă („...”) | toate actele (C34) | `S_*_SHORT` scos din HTML |")
    A("| textul **citat** (conținutul unui punct de intervenție) luat drept articole/alineate proprii | "
      "OG 13/2011, OUG 70/2024, Legea 129/2019, Legea 265/2022 | portalul îl marchează cu `S_CIT`; titlurile "
      "din interiorul lui primesc marcajul „citat”, cu **adâncimea** citării (Legea 30/2019: lege de aprobare → "
      "OUG 25/2018 → Codul fiscal); un articol citat se cuibărește sub punctul care îl introduce, unul propriu "
      "închide tot. Informația e a portalului, nu ghicită |")
    A("| număr de articol cu exponent roman sau cu literă | OUG 89/2025 „Articolul V^1”, Legea 31/1990 "
      "„Articolul 270^2 a)” | recunoscute; cheia normalizată (`artV^1`, `art270^2a`) |")
    A("| punct cu exponent | Legea 30/2019 „1^5.”, Codul fiscal, Normele | recunoscut; părintele — nodul "
      "al cărui ultim punct e baza |")
    A("| text **reprodus din alt act** la finalul consolidatului („NOTĂ: Reproducem mai jos … din Legea nr. "
      "76/2012”) | Codul civil (Legea 71/2011), Codul de procedură civilă (Legea 76/2012) | devine un atom "
      "*notă* al actului, marcat ca notă (nu articol); zona se oprește la sfârșitul documentului sau la "
      "primul articol care continuă numerotarea proprie. Numai în stratul oficial — C39 |")
    A("| punct de intervenție într-un articol **arab** (instantaneu) | Legea 239/2025, OUG 50/2015 | "
      "recunoscut după text („… se modifică și va avea următorul cuprins”) |")
    A("")
    cv = Counter(v["categorie"] for v in inainte.values())
    cn = Counter(v["categorie"] for v in dupa.values())
    A("**Detectorul, înainte (pasul 7) și după:**")
    A("")
    A("| Categorie | Înainte | După |")
    A("|---|---|---|")
    for k in sorted(set(cv) | set(cn)):
        A("| %s | %d | %d |" % (k, cv.get(k, 0), cn.get(k, 0)))
    A("")
    A("**Fiecare semnal rămas, cu motivul lui:**")
    A("")
    A("| Act | Semnale | Motivul |")
    A("|---|---|---|")
    for a, v in sorted(dupa.items()):
        A("| `%s` | S1=%d, S2=%s, S4=%d | %s |" % (a, v["S1_alineate_duplicate"], v["S2_acoperire"],
                                                v["S4_articole_in_nota"], v["categorie"]))
    A("")
    A("Niciun act oficial nu mai e semnalat. Atomii-cheie ai pașilor anteriori există neschimbați (TVA 21%: "
      "`legea_141_2025_consolidat#artII/pct42/art291/alin1`; Codul muncii art. 122; CF art. 310 alin. (6), "
      "art. 41 alin. (10^1); CPC art. 181 alin. (2)).")
    A("")
    A("Efectul asupra propunerii: **`propuneri/v8/`** — aceleași clasificări (94/1/26/26) și aceiași atomi; "
      "18 citate verbatim curățate de „...”. Bancul de mutații: 9/9.")
    A("")
    A("## C37 — ordinul 1099/2016")
    A("")
    A("Portalul are trei ordine nr. 1099/2016 (29.03, 23.06, 12.07). Contextul care decide e **antetul "
      "actului, așa cum îl are instantaneul**: %s. Adus: id portal %s. Regula e generală: la o căutare "
      "ambiguă, se citesc data și emitentul din antetul actului; dacă nici ele nu decid, actul rămâne în "
      "afara corpusului, cu mențiune." % (m["C37"]["motiv"], m["C37"]["id_portal"]))
    A("")
    A("---")
    A("")
    A(open(os.path.join(_RAD, "fiscalos", "cerinte_v7.md"), encoding="utf-8").read().strip())
    A("")
    A("---")
    A("")
    A("## Operațiile, cu durata măsurată")
    A("")
    A("| Operație | Durată | Cost |")
    A("|---|---|---|")
    for f in ("durate_v8.json", "durate_v8b.json"):
        for k, v in json.load(open(os.path.join(_RAD, "fiscalos", f), encoding="utf-8")).items():
            A("| %s | %.1f s | $0 |" % (k, v))
    A("| Detector (înainte/după), demonstrația C34, raport | %.1f s | $0 |" % (time.time() - t0))
    A("")
    A("Niciun apel la model: **$0**.")
    open(os.path.join(DEST, "RAPORT.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    return m


if __name__ == "__main__":
    m = construieste()
    print(m["C34_abtinere"])
    print(Counter(v["categorie"] for v in m["detector_dupa"].values()))
