# -*- coding: utf-8 -*-
"""Rulatorul probelor, fara pytest (nu e instalat pe masina): `python3 probe.py`.

Un test care nu se poate rula nu e o proba. Runner-ul e 20 de linii tocmai ca proba sa nu depinda
de o instalare care poate lipsi.
"""
import importlib
import sys
import traceback

MODULE = ["fiscalos.test_read_only", "fiscalos.test_atomizare", "fiscalos.test_potrivire",
          "fiscalos.test_banc"]


def ruleaza():
    ok = fail = 0
    for nume in MODULE:
        try:
            m = importlib.import_module(nume)
        except ImportError:
            continue
        for n in sorted(dir(m)):
            if not n.startswith("test_"):
                continue
            try:
                getattr(m, n)()
                print("  PASS %s.%s" % (nume.split(".")[-1], n))
                ok += 1
            except Exception:
                print("  FAIL %s.%s" % (nume.split(".")[-1], n))
                traceback.print_exc(limit=3)
                fail += 1
    print("\n%d PASS / %d FAIL" % (ok, fail))
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(ruleaza())
