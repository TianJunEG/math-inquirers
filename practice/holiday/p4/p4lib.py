"""Level 4 (Primary 4, ages 9-11) helpers for the online holiday practice: number formatting, brute-force helpers for the INDEPENDENT checkers,
and the figures that the printed workbook draws (redrawn here at a size that is readable on a 390 px phone).

Lesson files import this as  `from p4lib import *`  after putting this folder on sys.path.
"""
import itertools, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *      # noqa: E402,F401  (svg, T, Ln, Ci, Re, NAVY, YEL, TEAL, WARM, PALE ...)

SKY = '#DDEBF7'


def g(n):
    """The workbook way to print a whole number: a space between groups from 5 digits (4982, 5350, 47 285, 100 000)."""
    s = str(n)
    if len(s) < 5:
        return s
    out = []
    while s:
        out.insert(0, s[-3:]); s = s[:-3]
    return ' '.join(out)


# ---------------------------------------------------------------- independent checkers (loops over the numbers in the question)
def factors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def factor_pairs(n):
    """Pairs a x b = n with a <= b, found by trying 1, 2, 3 ... in order."""
    return [(a, n // a) for a in range(1, n + 1) if a * a <= n and n % a == 0]


def multiples_up_to(k, limit):
    out, v = [], k
    while v <= limit:
        out.append(v); v += k
    return out


def first_common_multiple(a, b):
    v = max(a, b)
    while v % a or v % b:
        v += 1
    return v


def common_factors(a, b):
    return [d for d in factors(a) if b % d == 0]


def greatest_common_factor(a, b):
    return max(common_factors(a, b))


def round_to(n, unit):
    """Round a whole number to the nearest `unit`; exactly halfway rounds UP (the rule children are taught)."""
    q, r = divmod(n, unit)
    return (q + 1) * unit if 2 * r >= unit else q * unit


def rounds_to(lo, hi, value, unit):
    """All whole numbers in [lo, hi] that round to `value` to the nearest `unit`."""
    return [n for n in range(lo, hi + 1) if round_to(n, unit) == value]


def digit_sum(n):
    return sum(int(c) for c in str(n))


def five_digit_numbers():
    return range(10000, 100000)


def card_numbers(cards):
    """Every 5-digit number made from the digit cards once each (no leading 0)."""
    out = []
    for p in itertools.permutations(cards):
        if p[0] != 0:
            out.append(int(''.join(map(str, p))))
    return sorted(out)


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


# ---------------------------------------------------------------- figures
def array_figure(rows, cols, highlight_rows=None, caption=''):
    """A rows x cols array of dots (trees), drawn small enough for a phone."""
    r, gap, x0, y0 = 7, 20, 14, 14
    W = x0 * 2 + (cols - 1) * gap + 2 * r
    b = ''
    for i in range(rows):
        for j in range(cols):
            b += Ci(x0 + r + j * gap, y0 + r + i * gap, r, '#CDE8C8', NAVY, 1.8)
    H = y0 * 2 + (rows - 1) * gap + 2 * r + 24
    b += T(W / 2, H - 6, caption or f'{rows} rows of {cols} trees', 15, 'middle', 800, TEAL)
    return svg(W, H, b, f'An array of {rows * cols} trees: {rows} rows with {cols} trees in each row.')


def time_line(start_h=6, minutes=60, label_every=15, tick_every=5, suffix='am'):
    """A time line from start_h:00 for `minutes`, a tick every tick_every minutes, a label every label_every minutes."""
    x0, k = 24, 5.0
    W = int(2 * x0 + minutes * k + 30)
    y = 40
    b = Ln(x0 - 8, y, x0 + minutes * k + 8, y, 3)
    for m in range(0, minutes + 1, tick_every):
        big = m % label_every == 0
        x = x0 + m * k
        b += Ln(x, y - (11 if big else 6), x, y + (11 if big else 6), 3 if big else 2)
        if big:
            h, mm = start_h + m // 60, m % 60
            b += T(x, y + 32, f'{h}:{mm:02d}', 15)
    b += T(x0 + minutes * k + 24, y + 5, suffix, 15, 'middle', 800, TEAL)
    return svg(W, 84, b, f'A time line from {start_h}:00 {suffix} for {minutes} minutes, marked every {tick_every} minutes.')


def number_line_k(lo, hi, major, minor, cross=None, dots=(), caption='', label_fmt=g, extra_labels=()):
    """A number line lo..hi, ticks every `minor`, labelled every `major`. cross: a value marked with an X above the line. dots: values marked with a filled dot."""
    x0, x1 = 28, 332
    W = x1 + x0
    px = lambda v: x0 + (v - lo) * (x1 - x0) / (hi - lo)
    y = 58
    b = (T(6, 16, caption, 15, 'start', 800) if caption else '') + Ln(x0 - 14, y, x1 + 14, y, 3)
    v = lo
    while v <= hi:
        big = (v - lo) % major == 0
        b += Ln(px(v), y - (12 if big else 7), px(v), y + (12 if big else 7), 3 if big else 1.6)
        if big or v in extra_labels:
            b += T(px(v), y + 34, label_fmt(v), 14, 'middle', 700, NAVY)
        v += minor
    if cross is not None:
        b += T(px(cross), y - 16, '×', 30, 'middle', 800, WARM) + T(px(cross), y - 40, label_fmt(cross), 14, 'middle', 800, WARM)
    for d in dots:
        b += Ci(px(d), y, 6, YEL, NAVY, 2)
    return svg(W, 96, b, caption or f'A number line from {g(lo)} to {g(hi)} with a tick every {g(minor)} and a label every {g(major)}.')


def digit_cards(digits):
    w, gp = 46, 12
    W = len(digits) * w + (len(digits) - 1) * gp + 12
    b = ''
    for i, d in enumerate(digits):
        x = 6 + i * (w + gp)
        b += Re(x, 6, w, 62, YEL, NAVY, 2.6, 9) + T(x + w / 2, 49, d, 34)
    return svg(W, 76, b, 'Digit cards ' + ', '.join(map(str, digits)))
