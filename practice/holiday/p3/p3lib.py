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


# ---------------------------------------------------------------- week 2 (lessons 3 and 4)
_figs2 = None


def figs2():
    """{name: svg} of the Level 3 week 2 figures drawn by the workbook's own functions (node, figs_p3_w2.js: l3.js array, l4.js and figs_l3.js bar models)."""
    global _figs2
    if _figs2 is None:
        _figs2 = json.loads(subprocess.check_output(['node', os.path.join(HERE, 'figs_p3_w2.js')], text=True))
    return _figs2


def digit_sum(n):
    return sum(int(c) for c in str(n))


def _fig_helpers():
    import sys
    sys.path.insert(0, os.path.join(HERE, '..'))
    import hlib
    return hlib


def times_fig(rows, caption):
    """A times-table strip like the printed one, as two blocks of five columns (readable on a phone).
    rows: [(row name, [10 cell values; None = an empty box to fill in]), ...]; the first row is the grey header row."""
    h = _fig_helpers()
    cw, lw, rh, gap, x0 = 50, 92, 36, 14, 2
    W = x0 * 2 + lw + 5 * cw
    y, body = 2, ''
    for blk in (range(0, 5), range(5, 10)):
        for ri, (name, vals) in enumerate(rows):
            head = ri == 0
            body += h.Re(x0, y, lw, rh, '#D9D9D9' if head else '#EDEDED', h.NAVY, 2) + h.T(x0 + 8, y + rh / 2 + 6, name, 15, 'start', 800)
            for j, k in enumerate(blk):
                x, v = x0 + lw + j * cw, vals[k]
                if v is None:
                    body += h.Re(x, y, cw, rh, '#fff', h.NAVY, 2, 0, '5 4') + h.T(x + cw / 2, y + rh / 2 + 7, '?', 18, 'middle', 700, '#5B6785')
                else:
                    body += h.Re(x, y, cw, rh, '#EDEDED' if head else '#fff', h.NAVY, 2) + h.T(x + cw / 2, y + rh / 2 + 6, v, 17, 'middle', 800 if head else 700)
            y += rh
        y += gap
    return h.svg(W, y - gap + 4, body, caption)


def grid_fig(cols, rows, cells, caption):
    """The printed grid puzzle: a 4 x 4 table. cols: the 3 column numbers (None = to find); rows: the 3 row numbers (None = to find);
    cells: 3 x 3 products (None = to find).  Header cells are grey; every unknown shows a dashed box with a question mark."""
    h = _fig_helpers()
    cw, x0 = 66, 2
    W = 4 * cw + 2 * x0
    body = ''

    def cell(c, r, v, head):
        x, y = x0 + c * cw, x0 + r * cw
        if v is None:
            return h.Re(x, y, cw, cw, '#fff', h.NAVY, 2, 0, '6 4') + h.T(x + cw / 2, y + cw / 2 + 8, '?', 26, 'middle', 700, '#5B6785')
        return h.Re(x, y, cw, cw, '#D9D9D9' if head else '#fff', h.NAVY, 2.4) + h.T(x + cw / 2, y + cw / 2 + 9, v, 28, 'middle', 800)
    body += cell(0, 0, '×', True)
    for j, v in enumerate(cols):
        body += cell(j + 1, 0, v, True)
    for i, v in enumerate(rows):
        body += cell(0, i + 1, v, True)
        for j in range(3):
            body += cell(j + 1, i + 1, cells[i][j], False)
    return h.svg(W, W, body, caption)


def grp(s, limit=30):
    """Frame helper: groups separated by 3 or more spaces keep their words together (no-break spaces) so a box never wraps away from its label;
    a group longer than `limit` characters (a sentence) is left to wrap normally."""
    import re
    out = []
    for g in re.split(r' {3,}', s):
        out.append(g.replace(' ', ' ') if len(re.sub(r'\{f\d+\}', '000', g)) <= limit else g)
    return ' '.join(out)
