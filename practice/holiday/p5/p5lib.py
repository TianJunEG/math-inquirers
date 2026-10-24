"""Helpers for the Level 5 (Primary 5) online holiday lessons: independent checkers, accepted wordings of typed answers, and the figures.

Used only by practice/holiday/p5/<NN>/lesson.py.  Everything here is plain Python (no formula copied from a printed answer):
the checkers search or simulate, and the accepted wordings are generated from the checked value.
"""
import itertools, os, re, sys
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import svg, T, Ln, Ci, Re, NAVY, YEL, TEAL, WARM, PALE      # noqa: E402,F401

SKY = '#CDE8F7'


# ---------------------------------------------------------------- numbers
def spaced(n):
    """1234567 -> '1 234 567' (the Singapore way of writing a big number)."""
    s = str(abs(int(n)))
    out = []
    while s:
        out.insert(0, s[-3:]); s = s[:-3]
    return ('-' if n < 0 else '') + ' '.join(out)


_U = dict(zero=0, one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9, ten=10, eleven=11, twelve=12, thirteen=13, fourteen=14,
          fifteen=15, sixteen=16, seventeen=17, eighteen=18, nineteen=19)
_TENS = dict(twenty=20, thirty=30, forty=40, fifty=50, sixty=60, seventy=70, eighty=80, ninety=90)


def words_to_number(s):
    """'five million, three hundred and eight thousand and forty' -> 5308040."""
    total = cur = 0
    for w in re.findall(r'[a-z]+', s.lower().replace('-', ' ')):
        if w == 'and':
            continue
        if w in _U:
            cur += _U[w]
        elif w in _TENS:
            cur += _TENS[w]
        elif w == 'hundred':
            cur *= 100
        elif w in ('thousand', 'million'):
            total += cur * (1000 if w == 'thousand' else 10 ** 6); cur = 0
        else:
            raise ValueError(w)
    return total + cur


def round_nearest(x, unit):
    """Round a whole number to the nearest `unit`, halves go up (by counting, not by a library rounding rule)."""
    lo = (x // unit) * unit
    return lo + unit if x - lo >= unit - (x - lo) else lo


def digit_sum(n):
    return sum(int(c) for c in str(n))


def sig2(x):
    """Round a positive whole number to its first two digits (4987 -> 5000, 3 004 512 -> 3 000 000)."""
    s = str(x)
    if len(s) <= 2:
        return x
    k = len(s) - 2
    return round_nearest(x, 10 ** k)


def numbers_with_digit_sum(ndigits, total):
    """All ndigits-digit numbers (no leading zero) whose digits add to `total`, by building digit by digit."""
    out = []

    def go(prefix, left, remaining):
        if left == 0:
            if remaining == 0:
                out.append(int(prefix))
            return
        for d in range(1 if not prefix else 0, 10):
            if d <= remaining:
                go(prefix + str(d), left - 1, remaining - d)
    go('', ndigits, total)
    return sorted(out)


def perm_numbers(digits, leading_zero=False):
    """Every number made by using each of `digits` exactly once (no leading 0 unless allowed)."""
    seen = set()
    for p in itertools.permutations(digits):
        if p[0] == 0 and not leading_zero:
            continue
        seen.add(int(''.join(map(str, p))))
    return sorted(seen)


def closest(target, digits):
    """The number made with each digit once that is nearest to `target`, plus the best one below and the best one above."""
    nums = perm_numbers(digits)
    best = min(nums, key=lambda n: (abs(n - target), n))
    ties = [n for n in nums if abs(n - target) == abs(best - target)]
    assert len(ties) == 1, ('tie', target, ties)
    below = max((n for n in nums if n <= target), default=None)
    above = min((n for n in nums if n >= target), default=None)
    return best, below, above


# ---------------------------------------------------------------- brackets
OPV = {'+': ['+'], '−': ['-', '−'], '×': ['×', 'x', '*'], '÷': ['÷', '/', ':']}


def evaluate(tokens):
    expr = ''.join(f'F({t})' if isinstance(t, int) else {'×': '*', '÷': '/', '−': '-'}.get(t, t) for t in tokens)
    return eval(expr, {'F': Fraction})        # tokens are only our own numbers, + − × ÷ and brackets


def with_brackets(nums, ops, i, j):
    toks = []
    for k, n in enumerate(nums):
        if k == i:
            toks.append('(')
        toks.append(n)
        if k == j:
            toks.append(')')
        if k < len(ops):
            toks.append(ops[k])
    return toks


def one_pair_solutions(nums, ops, target):
    """Every way to put ONE pair of brackets round two or more neighbouring numbers (not the whole sum) so that the sum equals the target."""
    sols = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if i == 0 and j == len(nums) - 1:
                continue
            t = with_brackets(nums, ops, i, j)
            if evaluate(t) == target:
                sols.append(t)
    return sols


def show_tokens(toks):
    out = ''
    for t in toks:
        if isinstance(t, int):
            out += spaced(t) if t >= 10000 else str(t)
        elif t in '()':
            out += t
        else:
            out += f' {t} '
    return out.replace('( ', '(').replace(' )', ')').replace('  ', ' ').strip()


def bracket_accepts(sols):
    """All typed ways of writing each solution: x or × or * for times, - or − for minus, / : ÷ for divide; spaces never matter; big numbers with or without commas."""
    out = set()
    for toks in sols:
        pools = []
        for t in toks:
            if isinstance(t, int):
                pools.append([str(t)] + ([f'{t:,}'] if t >= 1000 else []))
            elif t in '()':
                pools.append([t])
            else:
                pools.append(OPV[t])
        for combo in itertools.product(*pools):
            out.add(''.join(combo))
    return sorted(out)


# ---------------------------------------------------------------- typed answers: sets of numbers and fractions
def numlist_accepts(vals):
    """The numbers in any order, separated by a comma, a space, 'and' or a semicolon; each with or without commas inside it."""
    out = set()
    forms = [[str(v), f'{v:,}'] for v in vals]
    for perm in itertools.permutations(range(len(vals))):
        for fm in itertools.product(*[forms[k] for k in perm]):
            for sep in (',', '', 'and', ';'):
                out.add(sep.join(fm))
    return sorted(out)


def _terminating(d):
    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5
    return d == 1


def frac_text(f):
    """'3/4', '11/2' or '5' (improper fractions stay improper)."""
    f = Fraction(f)
    return str(f.numerator) if f.denominator == 1 else f'{f.numerator}/{f.denominator}'


def mixed_text(f):
    f = Fraction(f)
    if f.denominator == 1 or f < 1:
        return frac_text(f)
    w, r = divmod(f.numerator, f.denominator)
    return f'{w} {r}/{f.denominator}' if r else str(w)


def frac_accepts(f, simplest=False, units=(), also=(), maxk=12):
    """Accepted ways to type the fraction f.  simplest=True: only the lowest terms (and the mixed number / decimal of it).
    Otherwise any equal fraction n*k / d*k for k up to maxk is also right.  `units` are words that may follow ('of a pizza'), `also` extra exact wordings."""
    f = Fraction(f)
    n, d = f.numerator, f.denominator
    forms = set()
    ks = [1] if simplest else range(1, maxk + 1)
    if d == 1:
        forms.add(str(n))
    else:
        for k in ks:
            forms.add(f'{n * k}/{d * k}')
        if n > d:
            w, r = divmod(n, d)
            if r:
                for k in ks:
                    forms.add(f'{w} {r * k}/{d * k}')
            else:
                forms.add(str(w))
        if _terminating(d):
            s = ('%.10f' % float(f)).rstrip('0').rstrip('.')
            forms.add(s)
            if s.startswith('0.'):
                forms.add(s[1:])
    out = set(forms)
    for u in units:
        for x in forms:
            out.add(f'{x} {u}')
    out.update(also)
    return sorted(out)


# ---------------------------------------------------------------- figures (viewBox about 380 wide: text is about 13 px on a 390 px phone)
def cards(digits, caption):
    w, h, g, m = 44, 56, 8, 6
    W = m * 2 + len(digits) * w + (len(digits) - 1) * g
    b = ''
    for i, d in enumerate(digits):
        x = m + i * (w + g)
        b += Re(x, 6, w, h, YEL, NAVY, 2.6, 8) + T(x + w / 2, 6 + h / 2 + 11, d, 30)
    return svg(W, h + 12, b, caption)


def round_line():
    xs = [40 + 80 * i for i in range(5)]
    labs = ['2 499 000', '2 499 500', '2 500 000', '2 500 500', '2 501 000']
    b = Ln(10, 40, 390, 40, 3)
    for i, (x, s) in enumerate(zip(xs, labs)):
        b += Ln(x, 24, x, 56, 3, TEAL if i == 2 else NAVY) + T(x, 84, s, 15, 'middle', 800 if i == 2 else 700, TEAL if i == 2 else NAVY)
    return svg(400, 96, b, 'A number line marked 2 499 000, 2 499 500, 2 500 000, 2 500 500 and 2 501 000')


def bar_cells(x, y, w, h, n, shaded=(), fill=SKY, labels=None, size=15):
    """A bar of width w cut in n equal parts; parts whose index is in `shaded` are filled."""
    b = ''
    for k in range(n):
        b += Re(x + k * w / n, y, w / n, h, fill if k in shaded else '#fff', NAVY, 2.4)
        if labels:
            b += T(x + (k + 0.5) * w / n, y + h / 2 + 5, labels[k], size)
    return b


def share_bars(shade=False):
    """Q1(b): Group A (2 pizzas for 3 children) and Group B (3 pizzas for 5 children): two bars of the same length cut in 3 and in 5 parts."""
    x0, w = 96, 270
    b = T(x0 - 10, 34, 'Group A', 15, 'end') + T(x0 - 10, 96, 'Group B', 15, 'end')
    b += bar_cells(x0, 14, w, 30, 3, (0, 1) if shade else ()) + bar_cells(x0, 76, w, 30, 5, (0, 1, 2) if shade else ())
    if shade:
        b += T(x0 + w * 5 / 6, 62, 'short by 1/3', 14, 'middle', 800, WARM) + T(x0 + w * 4 / 5, 126, 'short by 2/5', 14, 'middle', 800, WARM)
        return svg(390, 134, b, 'One whole pizza as a bar for a child in each group. A child in group A gets 2 of 3 parts and is short by 1/3. A child in group B gets 3 of 5 parts and is short by 2/5.')
    return svg(390, 118, b, 'Two bars of the same length. Group A is cut in 3 equal parts and Group B in 5 equal parts. Nothing is shaded.')


def sticker_bar():
    x0, w, y, h = 30, 320, 44, 40
    b = f'<path d="M{x0} {y - 8} V{y - 18} H{x0 + w} V{y - 8}" fill="none" stroke="{NAVY}" stroke-width="2.5"/>' + T(x0 + w / 2, y - 26, '240 stickers', 16, 'middle', 800)
    b += bar_cells(x0, y, w, h, 4, (0,))
    b += T(x0 + w / 8, y + h + 24, 'Ben', 15, 'middle', 800, TEAL) + T(x0 + w * 5 / 8, y + h + 24, 'the remainder', 15, 'middle', 800, TEAL)
    return svg(380, 124, b, 'A bar for 240 stickers cut into 4 equal parts. The first part is for Ben. The other three parts are the remainder.')


def ravi_bar():
    x0, w, y, h = 30, 320, 40, 40
    u = w / 5
    b = bar_cells(x0, y, 2 * u, h, 2, (0, 1)) + T(x0 + u, y + h / 2 + 5, 'game', 15, 'middle', 800)
    b += Re(x0 + 2 * u, y, 1.5 * u, h, '#fff', NAVY, 2.4) + T(x0 + 2.75 * u, y + h / 2 + 5, 'book', 15, 'middle', 800)
    b += Re(x0 + 3.5 * u, y, 1.5 * u, h, '#fff', NAVY, 2.4) + T(x0 + 4.25 * u, y + h / 2 + 5, '$36 left', 14, 'middle', 800, TEAL)
    b += f'<path d="M{x0} {y - 6} V{y - 16} H{x0 + w} V{y - 6}" fill="none" stroke="{NAVY}" stroke-width="2.5"/>' + T(x0 + w / 2, y - 24, '? at first', 16, 'middle', 800)
    b += f'<path d="M{x0 + 2 * u} {y + h + 6} V{y + h + 16} H{x0 + w} V{y + h + 6}" fill="none" stroke="{NAVY}" stroke-width="2.5"/>' + T(x0 + 3.5 * u, y + h + 36, 'the rest: the book is half of it', 14, 'middle', 700, TEAL)
    return svg(380, 130, b, 'A bar for all of Ravi\'s money cut into 5 equal parts. The first 2 parts are shaded for the game. The other 3 parts are cut in half: the book and $36 left. A brace over the whole bar is marked with a question mark.')


def box_fractions(digits):
    """The four digit cards, and the empty boxes  [ ]/[ ] + [ ]/[ ]."""
    b = ''
    w, g, m = 44, 12, 0
    W = 380
    x0 = (W - (len(digits) * w + (len(digits) - 1) * g)) / 2
    for i, d in enumerate(digits):
        x = x0 + i * (w + g)
        b += Re(x, 6, w, 52, YEL, NAVY, 2.6, 8) + T(x + w / 2, 6 + 26 + 11, d, 30)
    def bf(cx, y):
        return Re(cx - 22, y, 44, 36, '#fff', NAVY, 2.6, 5) + Ln(cx - 28, y + 46, cx + 28, y + 46, 3) + Re(cx - 22, y + 56, 44, 36, '#fff', NAVY, 2.6, 5)
    b += bf(110, 76) + T(190, 138, '+', 34, 'middle', 800) + bf(270, 76)
    return svg(W, 178, b, 'The digit cards ' + ', '.join(map(str, digits)) + ' and two fractions to fill in, each with an empty box on top and an empty box below, added together.')


def twelve_bar():
    """Investigation (b): a bar cut into 12 equal parts: 1/3 is 4 parts, 1/4 is 3 parts, the difference is 1 part = 1/12."""
    x0, w = 44, 324
    b = T(x0 + w / 2, 18, 'one bar cut into 3 × 4 = 12 equal parts', 15, 'middle', 800)
    b += bar_cells(x0, 30, w, 34, 12, (0, 1, 2, 3)) + T(x0 - 4, 53, '1/3', 14, 'end', 800)
    b += bar_cells(x0, 78, w, 34, 12, (0, 1, 2)) + T(x0 - 4, 101, '1/4', 14, 'end', 800)
    xx = x0 + 3 * w / 12
    b += Re(xx, 30, w / 12, 34, YEL, WARM, 3.2) + T(xx + w / 24, 150, '1 part = 1/12', 15, 'middle', 800, WARM) + Ln(xx + w / 24, 118, xx + w / 24, 134, 2.4, WARM)
    return svg(390, 162, b, 'A bar cut into 12 equal parts. 1/3 is 4 parts. 1/4 is 3 parts. The difference is 1 part, which is 1/12.')
