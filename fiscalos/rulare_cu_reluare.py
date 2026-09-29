# -*- coding: utf-8 -*-
"""Rularea reluabila a navigarii, cu reincercare NUMAI la erorile temporare ale API-ului.

Temporare: 429 (rate limit) si 529 (overloaded) - se reia, cu asteptare crescatoare; fiecare reluare
continua de unde a ramas (raspunsurile salvate nu se platesc din nou). Orice alta eroare - 400 credit
insuficient, cereri invalide, erori de cod - e DEFINITIVA: bucla se opreste imediat si o raporteaza.
Scriptul nu atinge motorul: ruleaza `python -m fiscalos.navigare <argumente>` ca proces separat."""
import os
import re
import subprocess
import sys
import time

_RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPORARE = re.compile(r"Error code: (429|529)\b|OverloadedError|RateLimitError")
ASTEPTARI = [60, 120, 240, 480, 900, 900, 900]


def ruleaza(argumente, jurnal, istoric):
    for incercare in range(len(ASTEPTARI) + 1):
        t0 = time.strftime("%H:%M:%S")
        with open(jurnal, "w", encoding="utf-8") as f:
            cod = subprocess.call([sys.executable, "-m", "fiscalos.navigare"] + argumente, cwd=_RAD,
                                  stdout=f, stderr=subprocess.STDOUT)
        text = open(jurnal, encoding="utf-8").read()
        ultima = (text.strip().splitlines() or [""])[-1]
        with open(istoric, "a", encoding="utf-8") as h:
            h.write("=== incercarea %d %s -> cod %d | %s\n" % (incercare + 1, t0, cod, ultima[:200]))
            h.write(text + "\n")
        if cod == 0:
            return 0, "gata"
        if not TEMPORARE.search(ultima):
            return cod, "EROARE DEFINITIVA, oprit: " + ultima[:300]
        if incercare < len(ASTEPTARI):
            time.sleep(ASTEPTARI[incercare])
    return 1, "eroare temporara persistenta dupa %d incercari" % (len(ASTEPTARI) + 1)


if __name__ == "__main__":
    cod, mesaj = ruleaza(sys.argv[1:], os.path.join(_RAD, "artefacte", "intrebari", "navigare_rulare_log.txt"),
                         os.path.join(_RAD, "artefacte", "intrebari", "navigare_rulare_istoric.txt"))
    print(mesaj)
    sys.exit(cod)
