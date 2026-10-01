# -*- coding: utf-8 -*-
"""PROBA urmaririi (punctul 8d), intr-o COPIE DE TEST a proiectului - depozitul real nu se atinge.

Trei verificari la rand, cu un portal simulat care serveste paginile deja aduse (aceleasi octeti):
  A0. prima verificare: preia starea curenta a iConta (HEAD se poate fi mutat de la ultima comparatie);
  A. saptamana fara schimbari  -> trebuie "nimic schimbat", nicio propunere;
  B. o cota schimbata in lege  -> Codul fiscal art. 17, "este de 16%" -> "este de 18%", cu o consolidare
     noua; trebuie DIFERA pentru impozitul pe profit (iConta: 0.16), in propunerea urmatoare, cu
     ambele parti.
iConta se citeste ca de obicei: numai din git HEAD, numai citire.

`python -m fiscalos.urmarire_proba` -> urmarire/proba/rezultat_proba.json
"""
import json
import os
import shutil
import subprocess
import sys
import time

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable
ACT, CONSOLIDARE_NOUA = "cod_fiscal_227_2015_consolidat", "01.10.2026"
VECHI, NOU = "profitului impozabil este de 16%.", "profitului impozabil este de 18%."


class PortalSimulat(object):
    """Acelasi contract ca `portal.Portal.act`; serveste fisierele copiei. `modificari`: {act: (data, f)}."""

    def __init__(self, radacina, modificari=None):
        from fiscalos import portal
        self._info = portal.info_din_html
        self.rad, self.mod = radacina, modificari or {}
        man = json.load(open(os.path.join(radacina, "surse_oficiale", "MANIFEST.json"), encoding="utf-8"))
        self.fis = {x["id_portal"]: (act, x["fisier"]) for act, v in man["acte"].items() for x in v["fisiere"]}
        self.cereri = 0

    def act(self, id_act):
        self.cereri += 1
        act, fis = self.fis[str(id_act)]
        b = open(os.path.join(self.rad, "surse_oficiale", fis), "rb").read()
        info = self._info(id_act, b)
        if act in self.mod:
            data, f = self.mod[act]
            b = f(b.decode("utf-8")).encode("utf-8")
            info = dict(self._info(id_act, b), consolidare_curenta=data)
        return b, info


def copie_de_test(dest):
    """Arborele proiectului fara venv/, corpus/ (nefolosit de urmarire), .git, pagina_date/."""
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(_RAD, dest, ignore=shutil.ignore_patterns(
        "venv", "corpus", ".git", "pagina_date", "__pycache__", "urmarire"))
    return dest


_SCENARIU = r'''
import json, sys
from fiscalos import urmarire, urmarire_proba as up
mod = {}
if sys.argv[1] == "B":
    mod = {up.ACT: (up.CONSOLIDARE_NOUA, lambda h: h.replace(up.VECHI, up.NOU))}
p = up.PortalSimulat(urmarire._RAD, mod)
r = urmarire.verifica(p)
r["cereri_portal_simulat"] = p.cereri
print("@@" + json.dumps(r, ensure_ascii=False))
'''


def scenariu(copie, nume):
    t0 = time.time()
    o = subprocess.run([PY, "-c", _SCENARIU, nume], cwd=copie, capture_output=True, text=True, timeout=1800)
    if o.returncode:
        raise RuntimeError(o.stderr[-3000:])
    r = json.loads(next(l for l in o.stdout.splitlines() if l.startswith("@@"))[2:])
    r["secunde_scenariu"] = round(time.time() - t0, 1)
    return r


def ruleaza(baza):
    t0 = time.time()
    copie = copie_de_test(os.path.join(baza, "copie_test"))
    t_copie = round(time.time() - t0, 1)
    A0 = scenariu(copie, "A0")
    A = scenariu(copie, "A")
    B = scenariu(copie, "B")
    prop = B.get("propunere", "").split(" ")[0]
    sch = json.load(open(os.path.join(copie, prop, "SCHIMBARI_URMARIRE.json"), encoding="utf-8")) if prop else None
    profit = [s for s in (sch or {}).get("schimbari", []) if s["parametru"].startswith("cote/impozit_profit")]
    verdict = {
        "A_nimic_schimbat": A["rezumat"].startswith("nimic schimbat") and "propunere" not in A,
        "B_DIFERA_in_propunere": bool(profit) and profit[0]["clasificare"] == "DIFERA"
        and "18%" in (profit[0].get("verbatim") or "") and profit[0].get("valoare_cod") is not None,
        "depozitul_real_neatins": _real_neatins(),
    }
    return {"copie_de_test": copie, "secunde_copie": t_copie, "A0": A0, "A": A, "B": B,
            "B_parametrul_impozit_profit": profit, "verdict": verdict,
            "secunde_total": round(time.time() - t0, 1)}


def _real_neatins():
    o = subprocess.run(["git", "status", "--porcelain", "--", "surse_oficiale", "artefacte", "propuneri"],
                       cwd=_RAD, capture_output=True, text=True).stdout
    return o.strip() == ""


if __name__ == "__main__":
    baza = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_RAD, "..", "fiscalos_copie_test")
    r = ruleaza(os.path.abspath(baza))
    os.makedirs(os.path.join(_RAD, "urmarire", "proba"), exist_ok=True)
    with open(os.path.join(_RAD, "urmarire", "proba", "rezultat_proba.json"), "w", encoding="utf-8") as f:
        json.dump(r, f, ensure_ascii=False, indent=1)
    print("A0:", r["A0"]["rezumat"])
    print("A:", r["A"]["rezumat"])
    print("B:", r["B"]["rezumat"])
    print("verdict:", r["verdict"], "| %.1f s" % r["secunde_total"])
