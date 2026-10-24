"""Shared helpers for the Level 3 (P3) holiday online practice: the workbook's own figures (drawn by the workbook generator, via figs_p3.js)
and small brute-force helpers used by the INDEPENDENT checkers of lessons 1 and 2.  Imported by p3/NN/lesson.py (after `from hlib import *`)."""
import itertools, json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
_figs = None


def figs():
    """{name: svg} drawn by the workbook's own figure functions (node, p3/content/l1.js and l2.js)."""
    global _figs
    if _figs is None:
        _figs = json.loads(subprocess.check_output(['node', os.path.join(HERE, 'figs_p3.js')], text=True))
    return _figs


def digits(n):
    return [int(c) for c in str(n)]


def fournums(cards, odd=None, even=None):
    """All 4-digit numbers (no leading 0) made by using each card once; optionally only odd / only even ones.  Sorted, no repeats."""
    out = set()
    for p in itertools.permutations(cards):
        if p[0] == 0:
            continue
        n = int(''.join(map(str, p)))
        if odd and n % 2 == 0:
            continue
        if even and n % 2 == 1:
            continue
        out.add(n)
    return sorted(out)


def all_four_digit(pred):
    return [n for n in range(1000, 10000) if pred(n)]


def lst(seq):
    return ', '.join(str(x) for x in seq)
