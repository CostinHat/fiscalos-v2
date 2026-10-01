# -*- coding: utf-8 -*-
"""PROBE pentru pagina de intrebari (punctul 7): accesul numai pentru Costin, povestea raspunsului,
si 7d - intrebarile lui Costin NU ajung la reglaj (niciun modul al motorului nu citeste `pagina_date`)."""
import http.client
import json
import os
import re
import subprocess
import contextlib
import tempfile
import threading

from fiscalos import pagina

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_7d_niciun_modul_al_motorului_nu_citeste_intrebarile_lui_Costin():
    for f in sorted(os.listdir(os.path.join(_RAD, "fiscalos"))):
        if f.endswith(".py") and f not in ("pagina.py", "test_pagina.py"):
            t = open(os.path.join(_RAD, "fiscalos", f), encoding="utf-8").read()
            # singura mentiune admisa: EXCLUDEREA din copia de test a urmaririi (opusul citirii)
            t = re.sub(r"ignore_patterns\([^)]*\)", "", t)
            assert "pagina_date" not in t and "intrebari_costin" not in t, f
            assert not re.search(r"^\s*(from fiscalos import .*\bpagina\b|import fiscalos\.pagina)", t, re.M), f


def test_7c_intrebarile_nu_intra_in_git():
    r = subprocess.run(["git", "check-ignore", "pagina_date/intrebari_costin/x.json"], cwd=_RAD,
                       capture_output=True, text=True)
    assert r.returncode == 0, "pagina_date/ trebuie ignorat de git"


@contextlib.contextmanager
def _inlocuit(**kw):
    vechi = {k: getattr(pagina, k) for k in kw}
    for k, v in kw.items():
        setattr(pagina, k, v)
    try:
        yield
    finally:
        for k, v in vechi.items():
            setattr(pagina, k, v)


@contextlib.contextmanager
def _server():
    """Pagina pe un port liber, cu acces si date intr-un director temporar (nu atinge ~/.fiscalos)."""
    with tempfile.TemporaryDirectory() as tmp, _inlocuit(
            FISIER_ACCES=os.path.join(tmp, "pagina.env"), FISIER_PAROLA_INITIALA=os.path.join(tmp, "i.txt"),
            INTREBARI=os.path.join(tmp, "intrebari"), _incercari={}, _sesiuni={}):
        pagina.seteaza_parola("parola-de-proba-123")
        assert oct(os.stat(pagina.FISIER_ACCES).st_mode & 0o777) == "0o600"
        assert "parola-de-proba" not in open(pagina.FISIER_ACCES).read()      # numai hash-ul
        srv = pagina.ThreadingHTTPServer(("127.0.0.1", 0), pagina.Handler)
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        try:
            yield srv.server_address[1]
        finally:
            srv.shutdown()
            srv.server_close()


def _cere(port, metoda, cale, corp=None, cookie=None):
    c = http.client.HTTPConnection("127.0.0.1", port, timeout=10)
    h = {"Content-Type": "application/x-www-form-urlencoded"}
    if cookie:
        h["Cookie"] = cookie
    c.request(metoda, cale, body=corp, headers=h)
    r = c.getresponse()
    return r.status, dict(r.getheaders()), r.read().decode("utf-8")


def test_fara_sesiune_nu_se_vede_nimic():
  with _server() as server:
    for cale in ("/", "/urmarire", "/i/20260101-000000-abcdef"):
        st, _h, corp = _cere(server, "GET", cale)
        assert "Parola" in corp and "Întrebările tale" not in corp, cale
    st, _h, _c = _cere(server, "POST", "/intreaba", "text=ceva&csrf=x")
    assert st == 403


def test_parola_gresita_si_limita_de_incercari():
  with _server() as server:
    for _ in range(8):
        assert _cere(server, "POST", "/intrare", "parola=gresit")[0] == 401
    assert _cere(server, "POST", "/intrare", "parola=parola-de-proba-123")[0] == 429   # chiar si cea buna


def test_intrare_cookie_si_csrf():
  with _server() as server:
    st, h, _c = _cere(server, "POST", "/intrare", "parola=parola-de-proba-123")
    assert st == 303
    ck = h["Set-Cookie"]
    assert "HttpOnly" in ck and "SameSite=Strict" in ck
    cookie = ck.split(";")[0]
    st, _h, corp = _cere(server, "GET", "/", cookie=cookie)
    assert st == 200 and "Trimite" in corp
    csrf = re.search(r"name='csrf' value='([^']+)'", corp).group(1)
    assert _cere(server, "POST", "/intreaba", "text=x&csrf=altul", cookie=cookie)[0] == 403
    assert csrf


def test_id_cu_cale_ocolita_e_refuzat():
    for rau in ("../../etc/passwd", "20260101-000000-abcdef/../x", "x.json"):
        try:
            pagina._cale(rau)
            raise AssertionError(rau)
        except ValueError:
            pass


def test_7b_povestea_pe_un_raspuns_real_din_setul_4():
  with _inlocuit(_forma_consolidata=lambda a: "oficial: legislatie.just.ro, forma consolidata din 22.09.2026"):
    rs = json.load(open(os.path.join(_RAD, "intrebari", "set4", "raspunsuri_set4.json"), encoding="utf-8"))["raspunsuri"]
    r = next(x for x in rs if x["stare"] == "RASPUNS" and x.get("calcule"))
    h = pagina.poveste(r)
    ordine = [h.index(s) for s in ("Data de referință", "Răspunsul", "citate verbatim", "pas cu pas")]
    assert ordine == sorted(ordine)
    for a in r["argument"]:
        assert pagina.E(a["verbatim"]) in h and pagina.E(a["temei"]) in h and a["atom"] in h
    assert "forma consolidata din 22.09.2026" in h
    for c in r["calcule"]:
        assert pagina.E(c["rezultat"]) in h
    ab = next(x for x in rs if x["stare"] != "RASPUNS")
    h = pagina.poveste(ab)
    assert "Abținere" in h and pagina.E(ab["motiv"]) in h


def test_regula_5_la_pregatire_cifrele_din_afara_intrebarii_sunt_prinse():
    q = "Cât impozit pe dividende reține o firmă la o distribuire de 10.000 lei?"
    assert pagina.cifre_nesursate("Cota s-a modificat (5% / 8% / 10%), plata până pe 25.", q) == ["10", "25", "5", "8"]
    assert pagina.cifre_nesursate("Suma de 10.000 lei e brută?", q) == []
