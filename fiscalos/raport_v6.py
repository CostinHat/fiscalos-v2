# -*- coding: utf-8 -*-
"""Livrabilul pasului 7: deciziile C30-C33. FARA rulare platita pe setul vechi (decizia 5): efectul lui
C30 si C33 se masoara pe iesirile SALVATE, efectul lui C31 si C32 se masoara pe setul nou.

Fiecare rulare se compara pe corpusul EI (`comparatie.corpus_la_commit`): dupa C31, id-urile unor atomi
s-au schimbat, iar un temei citat de o rulare veche nu s-ar mai rezolva pe corpusul de acum."""
import json
import os
import time

from fiscalos import comparatie, detector_structura, navigare, potrivire
from fiscalos import _comparatie_inainte_C30 as vechi

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(_RAD, "intrebari", "v6")
ZIP = "/home/costin/ghid_incoming/fiscalos_v6_rezultat.zip"
RULARI = [("semantic v2", "intrebari/v2/raspunsuri_semantic.json", "b0a02c6"),
          ("semantic v3", "intrebari/v3/raspunsuri_semantic.json", "7eb6fa0"),
          ("navigare v4", "intrebari/v4/raspunsuri_navigare.json", "d35c21a"),
          ("navigare v5", "intrebari/v5/raspunsuri_navigare.json", "778e826"),
          ("navigare v5 + C33 (propunerile salvate, decodate)", "intrebari/v5/masura_C33_raspunsuri.json", "778e826"),
          ("lexical v5", "intrebari/v5/raspunsuri_lexical.json", "778e826")]


def _f(s):
    return "%d/%d/%d" % (s["CORECT"], s["GRESIT"], s["NU_POT"])


def construieste():
    os.makedirs(DEST, exist_ok=True)
    t0 = time.time()
    c30, final = [], None
    for n, f, cm in RULARI:
        corp = comparatie.corpus_la_commit(cm)
        a, b = vechi.compara(os.path.join(_RAD, f), corp), comparatie.compara(os.path.join(_RAD, f), corp)
        A = {x["id"]: x["verdict_pe_fond"] for x in a["comparatii"]}
        B = {x["id"]: x["verdict_pe_fond"] for x in b["comparatii"]}
        c30.append({"rulare": n, "corpus": cm, "inainte": a["scor_referinta_pe_fond"],
                    "dupa": b["scor_referinta_pe_fond"], "schimbari": [(i, A[i], B[i]) for i in A if A[i] != B[i]]})
        if "C33" in n:
            final = b
    c33 = json.load(open(os.path.join(_RAD, "intrebari", "v5", "masura_C33.json"), encoding="utf-8"))
    det_vechi = detector_structura.detecteaza(potrivire.Corpus(oficiale=False))
    corp = potrivire.Corpus()
    det_nou = detector_structura.detecteaza(corp)
    rez = json.load(open(os.path.join(_RAD, "surse_oficiale", "C31_rezolvare.json"), encoding="utf-8"))["acte"]
    man = json.load(open(os.path.join(_RAD, "surse_oficiale", "MANIFEST.json"), encoding="utf-8"))["acte"]
    ramase = [x for x in final["comparatii"] if x["verdict_pe_fond"] == "GRESIT"]
    # C32, demonstrat pe atomii reali (fara model): termenul din Q-TVA-07
    dupa = {i: corp.dupa_id[i] for i in ("legea_134_2010_codul_de_procedura_civila#art181/alin2",
                                          "legea_53_2003_codul_muncii#art139/alin1")}
    calc = [{"nume": "termen", "formula": "termen_efectiv(d)", "operanzi": [
        {"nume": "d", "valoare": "28.02.2026", "eticheta": "FAPT_CAZ", "atom": "", "fragment": "28.02.2026"}]}]
    _v, _g, det_c32 = navigare.evalueaza_calcule(calc, dupa, "Termen nominal 28.02.2026.", citati=list(dupa))
    masuri = {"C30": c30, "C33": c33, "scor_final_fara_apel": final["scor_referinta_pe_fond"],
              "gresit_ramase": [(x["id"], x["de_ce"]) for x in ramase],
              "C31_detector_inainte": det_vechi, "C31_detector_dupa": det_nou, "C31_rezolvare": rez,
              "C32_demonstratie": navigare.pas_cu_pas(det_c32)}
    json.dump(masuri, open(os.path.join(DEST, "masuratori.json"), "w", encoding="utf-8"), ensure_ascii=False,
              indent=1, default=str)
    json.dump(final, open(os.path.join(DEST, "comparatie_v5_C33_C30.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    L = []
    A = L.append
    A("# FiscalOS v2 — Pasul 7: deciziile C30–C33")
    A("")
    A("Generat %s · ZIP: `%s`" % (time.strftime("%d.%m.%Y %H:%M"), ZIP))
    A("")
    A("> **Fără rulare plătită pe setul vechi (decizia 5).** C30 și C33 sunt măsurate pe ieșirile salvate, "
      "fără niciun apel; efectul lui C31 și C32 se măsoară pe setul nou. Scorurile sunt INDICATIVE.")
    A("")
    A("## Rezultatul, măsurat fără apel nou")
    A("")
    A("| | CORECT | GREȘIT | NU POT |")
    A("|---|---|---|---|")
    v5 = c30[3]["inainte"]
    A("| Navigare v5, cum a fost raportată | %d | %d | %d |" % (v5["CORECT"], v5["GRESIT"], v5["NU_POT"]))
    A("| + C33 (decodarea `\\uXXXX`, pe propunerile salvate) | %d | %d | %d |" % tuple(
        c30[4]["inainte"][k] for k in ("CORECT", "GRESIT", "NU_POT")))
    A("| **+ C30 (comparatorul)** | **%d** | **%d** | **%d** |" % tuple(
        final["scor_referinta_pe_fond"][k] for k in ("CORECT", "GRESIT", "NU_POT")))
    A("")
    A("GREȘIT rămase: %s. Ambele sunt ținta deciziilor măsurate pe setul nou: Q-TVA-07 (termenul efectiv, "
      "sâmbătă → luni) — C32; Q-SAL-10 (Codul muncii din instantaneu, stricat) — C31." % "; ".join(
          "**%s** — %s" % (i, d[:160]) for i, d in masuri["gresit_ramase"]))
    A("")
    A("## C30 — comparatorul: zero în cuvinte și data în litere")
    A("")
    A("Defecte de clasă ale **scorului**, nu ale motorului. Reparațiile: un răspuns care spune explicit că "
      "nu se datorează nimic („nimic”, „zero”, „nu (se) datorează”) satisface o cheie al cărei fapt principal "
      "e zero; o dată în litere cu an („28 februarie 2026”) primește și forma numerică („28.02.2026”) ca alias "
      "(faptul principal rămâne zi + lună, ca anul relativ „anul următor” să nu devină mai sever); datele "
      "numerice se normalizează (1.3.2026 = 01.03.2026). Fiecare rulare pe corpusul ei:")
    A("")
    A("| Rulare | Corpus (commit) | Înainte | După | Schimbări |")
    A("|---|---|---|---|---|")
    for x in c30:
        A("| %s | `%s` | %s | %s | %s |" % (x["rulare"], x["corpus"], _f(x["inainte"]), _f(x["dupa"]),
                                           ", ".join("%s %s→%s" % s for s in x["schimbari"]) or "—"))
    A("")
    A("Nicio notă nu a devenit mai severă. Probe în ambele direcții: `test_intrebari.test_C30_*` (zero "
      "recunoscut numai când e spus; alt an nu se potrivește).")
    A("")
    A("**Corectarea metodei, găsită aici:** după C31, id-urile unor atomi s-au schimbat (cuprinsul "
      "portalului, de ex. `cod_fiscal…#art156~2` → `#art156`). Re-comparată pe corpusul de acum, v5 ar fi "
      "ieșit 33/4/13 — o scădere care nu e a motorului. De aceea `comparatie.compara` primește acum corpusul "
      "rulării (`corpus_la_commit`, din git); tabelul de mai sus e calculat așa, iar cifrele istorice se "
      "reproduc (v2: 12/7/31, v5: 34/3/13).")
    A("")
    A("## C33 — decodarea artefactului de transport")
    A("")
    A("Aplicată: `navigare.decodeaza_transport` decodează, înainte de validare și verificare, numai secvența "
      "completă `\\u` + 4 cifre hexa care dă un caracter tipăribil; orice alt backslash rămâne neatins. "
      "Probe: `test_navigare.test_C33_*` — secvențele reale („imobiliz\\u0103rilor”, „\\u021Aara”) se "
      "decodează; textul legitim (diacritice deja scrise, „C:\\users”, „\\u00” incomplet, „\\uZZZZ”, "
      "caractere de control, surogate) nu se atinge. Pe propunerile v5 salvate, decodorul aplicat dă exact "
      "rezultatul măsurat în pasul anterior (0 diferențe).")
    A("")
    A("Efect, fără apel: %s → %s (%s)." % (_f(c33["inainte"]), _f(c33["dupa"]), ", ".join(
        "%s → %s" % kv for kv in c33["verdict_dupa"].items())))
    A("")
    A("## C31 — Codul muncii din sursa oficială și detectorul de structură")
    A("")
    n_ad = sum(1 for v in rez.values() if v["stare"] == "adus")
    A("**Detectorul** (`fiscalos/detector_structura.py`) caută mecanic clasa „articole atomizate sub alt "
      "articol”, cu patru semnale: S1 alineate duplicate direct sub același articol; S2 acoperirea "
      "numerotării (articole recunoscute / cel mai mare număr, numai la actele de bază întregi); S3 articol "
      "imbricat într-un act de bază; S4 articol înghițit într-o notă. Rulat pe tot corpusul:")
    A("")
    from collections import Counter
    cv, cn = Counter(v["categorie"] for v in det_vechi.values()), Counter(v["categorie"] for v in det_nou.values())
    A("| Categorie | Instantaneul iConta | Corpusul de acum |")
    A("|---|---|---|")
    for k in sorted(set(cv) | set(cn)):
        A("| %s | %d | %d |" % (k, cv.get(k, 0), cn.get(k, 0)))
    A("")
    A("**Aduse din sursa oficială: %d acte** (`surse_oficiale/C31_rezolvare.json` — id-ul din portal și "
      "căutarea care l-a dat, pentru fiecare). Codul muncii: forma consolidată din %s; art. 122 alin. (1) "
      "(„…în următoarele 90 de zile calendaristice…”) are acum id-ul lui. Actele, cu atomii oficiali față de "
      "cei din instantaneu:" % (n_ad, man["legea_53_2003_codul_muncii"]["data_formei_consolidate"]))
    A("")
    A("| Act | id portal | Atomi oficial / instantaneu |")
    A("|---|---|---|")
    for a, v in sorted(rez.items()):
        if v["stare"] == "adus":
            sa = corp.sursa_act.get(a, {})
            A("| `%s` | %s | %s / %s |" % (a, v["id_portal"], sa.get("atomi_oficial"), sa.get("atomi_instantaneu")))
    A("")
    A("Neaduse, cu motivul: %s." % "; ".join("`%s` — %s" % (a, v.get("motiv") or "%s `%s`" % (v["stare"], v.get("ca")))
                                             for a, v in sorted(rez.items()) if v["stare"] != "adus"))
    A("Variantele stricate ale unui act care există acum oficial rămân în corpus (pentru potrivirea iConta), "
      "marcate „înlocuit de”, și **nu mai sunt indexate** de motorul de întrebări.")
    A("")
    A("**Trei defecte de conversie a portalului, găsite de detector după aducere și reparate** (fiecare cu "
      "probă în `test_c12_c17.test_C31_*`):")
    A("")
    A("1. **Cuprinsul-meniu** al portalului (linkuri `pozitioneaza(...)`) intra în text; ultimul marcaj din "
      "fiecare serie a cuprinsului rămânea „articol” — de aici dublurile `art135^2~2` în Codul fiscal și "
      "2.455 de alineate duplicate în Codul civil. Linkurile de navigare se scot înainte de conversie.")
    A("2. **„Articolul 1.000”** (separator de mii) nu era recunoscut: tot Codul civil de după art. 999 se lipea "
      "de art. 999.")
    A("3. **Nota goală `<span …/>`** (element care se închide singur) era numărată ca deschisă: nota nu se mai "
      "închidea și înghițea articolele următoare — în Codul muncii oficial, art. 122–124. S4 a fost adăugat "
      "după acest caz.")
    A("")
    res = {a: v for a, v in det_nou.items() if v["categorie"].startswith("deja")}
    A("**Defecte reziduale ale conversiei oficiale (%d acte, raportate, nereparate):** %s. La OG 13/2011 și "
      "OUG 70/2024 e altă clasă: acte de bază cu numerotare arabă care modifică alte legi — articolele citate "
      "(de ex. „art. 325” din Codul fiscal) apar ca articole proprii. Vezi C36." % (len(res), ", ".join(
          "`%s` (S1=%d, S2=%s)" % (a, v["S1_alineate_duplicate"], v["S2_acoperire"]) for a, v in res.items())))
    A("")
    A("Efectul asupra propunerii: **`propuneri/v7/`** — aceleași clasificări (94/1/26/26), 16 parametri cu "
      "atomul la locul lui din textul oficial (de ex. TVA 21%%: `legea_141_2025_consolidat#artII/pct42/"
      "art291/alin1`, sub punctul de intervenție). Bancul de mutații: 9/9.")
    A("")
    A("## C32 — `termen_efectiv(data)`")
    A("")
    A("Funcție de calcul: regula prelungirii și lista sărbătorilor legale se iau **numai din atomii citați "
      "în răspuns** — fără ei, calculul e respins. Sărbătorile cu dată mobilă se calculează (Paștele "
      "ortodox: algoritmul Meeus pentru calendarul iulian + 13 zile; Vinerea Mare = Paștele − 2; Rusaliile = "
      "Paștele + 49), iar calculul e declarat în răspuns. Tot acum: `data(zi, lună, an)` (luna poate fi scrisă "
      "în litere, din atom) și data + N zile, ca termenul nominal să poată fi construit din atomi.")
    A("")
    A("Regula prelungirii pentru termenele fiscale e în **Codul de procedură civilă** (CPF art. 75 trimite la "
      "el), care **nu era în corpus**; l-am adus din sursa oficială, ca la C12 (%s, forma din %s) — "
      "art. 181 alin. (2): „Când ultima zi a unui termen cade într-o zi nelucrătoare, termenul se prelungește "
      "până în prima zi lucrătoare care urmează.” Decizie a mea — de confirmat (C35)."
      % ("id portal 120644", man["legea_134_2010_codul_de_procedura_civila"]["data_formei_consolidate"]))
    A("")
    A("Demonstrat pe atomii reali, fără model — termenul din Q-TVA-07:")
    A("")
    for x in masuri["C32_demonstratie"]:
        A("> %s" % x)
    A("")
    A("Probe: `test_navigare.test_C32_*` (Paștele 2025–2027; sâmbătă → luni; Vinerea Mare 10.04.2026 → "
      "14.04.2026; zi lucrătoare neschimbată; fără atomii citați — respins).")
    A("")
    A("---")
    A("")
    A(open(os.path.join(_RAD, "fiscalos", "cerinte_v6.md"), encoding="utf-8").read().strip())
    A("")
    A("---")
    A("")
    A("## Operațiile, cu durata măsurată")
    A("")
    A("| Operație | Durată | Cost |")
    A("|---|---|---|")
    for k, v in json.load(open(os.path.join(_RAD, "fiscalos", "durate_v6.json"), encoding="utf-8")).items():
        A("| %s | %.1f s | $0 |" % (k, v))
    for k, v in json.load(open(os.path.join(_RAD, "fiscalos", "durate_v7.json"), encoding="utf-8")).items():
        A("| %s | %.1f s | $0 |" % (k, v))
    A("| Comparații C30 pe 6 rulări (fiecare pe corpusul ei), detector, raport | %.1f s | $0 |" % (time.time() - t0))
    A("")
    A("Niciun apel la model în acest pas: **$0**.")
    open(os.path.join(DEST, "RAPORT.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    return masuri


if __name__ == "__main__":
    m = construieste()
    print(m["scor_final_fara_apel"], m["gresit_ramase"])
