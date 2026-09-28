# -*- coding: utf-8 -*-
"""Clientul portalului legislatie.just.ro - sursa oficiala a consolidatelor (decizia C12).

Se prezinta onest (user-agent care numeste FiscalOS). Portalul refuza user-agent-ul implicit al lui
curl (HTTP 403 de la nginx-ul lor); cu un user-agent descriptiv raspunde 200. Nu e nevoie de proxy.

CE STIE PORTALUL, masurat:
  - pagina unui act (`/Public/DetaliiDocument/<id>`) intoarce FORMA CONSOLIDATA CURENTA; campul ascuns
    `id_act` e id-ul acelei forme, iar "istoric consolidari" listeaza formele, cea curenta prima si
    fara link ("Consolidarea din 01.01.2026");
  - cautarea e un formular POST cu jeton anti-falsificare, deci cere sesiune (cookie + jeton).
Pauza intre cereri: portalul e un serviciu public, nu un depozit de date.
"""
import html as _html
import http.cookiejar
import re
import time
import urllib.parse
import urllib.request

BAZA = "https://legislatie.just.ro"
UA = "Mozilla/5.0 (compatible; FiscalOS/2.0; audit fiscal; +https://github.com/CostinHat/fiscalos-v2)"
PAUZA = 2.0


class Portal(object):
    def __init__(self):
        self.jar = http.cookiejar.CookieJar()
        self.op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.jar))
        self.op.addheaders = [("User-Agent", UA), ("Accept-Language", "ro-RO,ro;q=0.9")]
        self._ultima = 0.0

    def _get(self, url, date=None, timeout=120):
        asteapta = PAUZA - (time.time() - self._ultima)
        if asteapta > 0:
            time.sleep(asteapta)
        cer = urllib.request.Request(url, data=urllib.parse.urlencode(date).encode() if date else None)
        with self.op.open(cer, timeout=timeout) as r:
            corp = r.read()
            self._ultima = time.time()
            return r.status, corp

    def cauta(self, tip=None, numar=None, an=None, titlu=None):
        """[(id, titlu)] - rezultatele cautarii dupa tip/numar/an semnarii/titlu."""
        _s, acasa = self._get(BAZA + "/Public/Acasa")
        t = acasa.decode("utf-8", "replace")
        jeton = re.search(r'name="__RequestVerificationToken"[^>]*value="([^"]+)"', t).group(1)
        date = {"__RequestVerificationToken": jeton, "TitleText": titlu or "",
                "DocumentType": tip or "", "DocumentNumber": numar or "",
                "DataSemnariiTextFrom": "01.01.%s" % an if an else "",
                "DataSemnariiTextTo": "31.12.%s" % an if an else "", "actiontype": "Căutare"}
        for k in ("ContentText_First", "opContentText_Second", "ContentText_Second",
                  "opContentText_Third", "ContentText_Third", "opContentText_Fourth",
                  "ContentText_Fourth", "PublishedInName", "PublishedInNumber",
                  "DataPublicariiTextFrom", "DataPublicariiTextTo", "ActInForceOnDateTextFrom",
                  "EmitentAct"):
            date.setdefault(k, "")
        _s, rez = self._get(BAZA + "/", date)
        t = rez.decode("utf-8", "replace")
        ies, vazut = [], set()
        for m in re.finditer(r'DetaliiDocument/(\d+)[^>]*>\s*([^<]{3,200})', t):
            if m.group(1) not in vazut:
                vazut.add(m.group(1))
                ies.append((m.group(1), _html.unescape(" ".join(m.group(2).split()))))
        return ies

    def act(self, id_act):
        """(html, info) - forma consolidata CURENTA a actului, cu data consolidarii."""
        _s, corp = self._get(BAZA + "/Public/DetaliiDocument/%s" % id_act)
        t = corp.decode("utf-8", "replace")
        info = {"id_cerut": str(id_act)}
        m = re.search(r'id="id_act"[^>]*value="(\d+)"', t)
        info["id_forma"] = m.group(1) if m else None
        m = re.search(r"<title>(.*?)</title>", t, re.S)
        info["titlu"] = " ".join(m.group(1).split()) if m else None
        # istoricul consolidarilor: prima intrare e cea mai noua; fara href = cea afisata
        ist = re.findall(r"<a title='Consolidarea din ([\d.]+)'([^>]*)>", t)
        info["consolidari"] = [d for d, _ in ist]
        if ist:
            d0, atr0 = ist[0]
            href = re.search(r"DetaliiDocument/(\d+)", atr0)
            info["consolidare_curenta"] = d0
            info["afisata_e_cea_curenta"] = href is None
            info["id_forma_curenta"] = href.group(1) if href else info["id_forma"]
        info["forma_de_baza"] = not ist
        info["articole_in_pagina"] = len(re.findall(r"Articolul\s+\d", t))
        info["octeti"] = len(corp)
        return corp, info
