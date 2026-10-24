"""Shared helpers for the Level 3 (P3) holiday online practice, WEEK 5 (lessons 9 and 10): figures drawn larger than the printed ones (so the text is readable on a 390 px phone)
from the SAME data as the workbook's own figures (the lesson files check that the data equals the printed figures, which figs_p3_w5.js prints from the workbook's own generator
functions), the accepted writings of money, times and lists of names, and small exact helpers for the INDEPENDENT checkers (changing units, time arithmetic in minutes, money in cents,
every way of paying, queue positions, handshakes, counting the numbers made from digit cards).  Imported by p3/09/lesson.py and p3/10/lesson.py (after `from hlib import *`)."""
import itertools, json, os, re, subprocess, textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
_f5 = None


def figs5():
    """{'figs': {name: svg}, 'pics': {item name: svg}}: the PRINTED figures, from the workbook's own generator functions (node, figs_p3_w5.js)."""
    global _f5
    if _f5 is None:
        _f5 = json.loads(subprocess.check_output(['node', os.path.join(HERE, 'figs_p3_w5.js')], text=True))
    return _f5


def _h():
    import sys
    sys.path.insert(0, os.path.join(HERE, '..'))
    import hlib
    return hlib


BLU, GRN = '#CDE8F7', '#CDEBD7'


# ================================================================= arithmetic helpers for the independent checkers
def cm_of(m, cm=0):
    return m * 100 + cm


def g_of(kg, g=0):
    return kg * 1000 + g


def ml_of(litres, ml=0):
    return litres * 1000 + ml


def mins(h, m=0):
    """Minutes since midnight of a 24-hour time."""
    return h * 60 + m


def pm(h, m=0):
    """Minutes since midnight of a pm time (1 to 11 pm; 12 pm is noon)."""
    return (h % 12 + 12) * 60 + m


def hm(t):
    """(hours, minutes) of a count of minutes since midnight (hours may pass 24)."""
    return (t // 60, t % 60)


def count_in(total, size):
    """How many whole `size`s can be taken from `total` and what is left, by taking them away one at a time (no division)."""
    n = 0
    while total >= size:
        total -= size
        n += 1
    return n, total


def hourly_from(first, gap, how_many):
    """The times (minutes since midnight) of buses that leave every `gap` minutes, first one at `first`."""
    out, t = [], first
    for _ in range(how_many):
        out.append(t)
        t += gap
    return out


def tm(t):
    """'07:05' from minutes since midnight."""
    return f'{t // 60:02d}:{t % 60:02d}'


def cents(dollars_text):
    """'$7.85' or '7.85' -> 785, by reading the digits."""
    d, _, c = dollars_text.replace('$', '').partition('.')
    return int(d) * 100 + int((c + '00')[:2])


# ---------------------------------------------------------------- money and name lists the child may type
def money_forms(c):
    """Every way a child may write an amount of money of c cents: $x.yy, x.yy, $x.y (when the last digit is 0), $x when whole, c¢, c cents, c c.
    (Amounts below $1 also as $0.yy, 0.yy and .yy.)"""
    d, r = divmod(c, 100)
    out = [f'${d}.{r:02d}', f'{d}.{r:02d}', f'$ {d}.{r:02d}', f'{d}.{r:02d} dollars', f'${d}.{r:02d} dollars', f'{c}¢', f'{c} cents', f'{c}c', f'{c} c', f'{c} ¢']
    if r % 10 == 0:
        out += [f'${d}.{r // 10}', f'{d}.{r // 10}']
        if r == 0:
            out += [f'${d}', f'{d} dollars', f'{d} dollar', f'$ {d}']
    if c < 100:
        out += [f'$.{r:02d}', f'.{r:02d}']
    out += [f'{d} dollars {r} cents', f'{d} dollar {r} cents', f'${d} and {r}¢'] if (r and d) else []
    seen, res = set(), []
    for x in out:
        if x not in seen:
            seen.add(x)
            res.append(x)
    return res


def order_forms(items):
    """Typed letters in this ORDER: 'C, D, B, A', 'C,D,B,A', 'C D B A', 'CDBA', 'C; D; B; A', 'C then D then B then A', 'C > D...' is not accepted."""
    seq = list(items)
    return list(dict.fromkeys([', '.join(seq), ','.join(seq), ' '.join(seq), ''.join(seq), '; '.join(seq), ' then '.join(seq), ', '.join(seq[:-1]) + ' and ' + seq[-1], ', '.join(seq[:-1]) + ', and ' + seq[-1]]))


def name_list_forms(alts, ordered=False):
    """alts: for every thing, the writings the child may use for its name, e.g. [['Book'], ['Pen set', 'pens', 'pen'], ['Puzzle']].  Any order unless ordered=True; separators comma, 'and', '+', space."""
    out = []
    orders = [list(range(len(alts)))] if ordered else [list(p) for p in itertools.permutations(range(len(alts)))]
    for o in orders:
        for combo in itertools.product(*[alts[i] for i in o]):
            c = list(combo)
            out += [', '.join(c), ','.join(c), ' '.join(c), ' and '.join(c), ' + '.join(c), '; '.join(c), ', '.join(c[:-1]) + ' and ' + c[-1], ', '.join(c[:-1]) + ', and ' + c[-1]]
    return list(dict.fromkeys(out))


def time_list_forms(times):
    """A typed list of clock times as '07:05, 07:30, ...': each time with or without the zero in front of the hour, separators comma, comma and space, space, semicolon, 'and'."""
    per = []
    for t in times:
        h, m = t // 60, t % 60
        per.append(list(dict.fromkeys([f'{h:02d}:{m:02d}', f'{h}:{m:02d}'])))
    out = []
    for combo in itertools.product(*per):
        c = list(combo)
        out += [', '.join(c), ','.join(c), ' '.join(c), '; '.join(c), ', '.join(c[:-1]) + ' and ' + c[-1]]
    return list(dict.fromkeys(out))


def twelve_forms(h, m):
    """'8:05 pm' written the usual ways (8:05 pm, 8:05pm, 8.05 pm, 08:05 pm, 8:05 p.m)."""
    return list(dict.fromkeys([f'{h}:{m:02d} pm', f'{h}.{m:02d} pm', f'{h:02d}:{m:02d} pm', f'{h}:{m:02d} p.m', f'{h}.{m:02d} p.m', f'{h}:{m:02d} in the evening']))


def twentyfour_forms(h, m):
    """'14:00' written the usual ways (14:00, 14.00, 1400, 14 00, 14:00 hours, 1400 hours)."""
    return list(dict.fromkeys([f'{h:02d}:{m:02d}', f'{h}:{m:02d}', f'{h:02d}.{m:02d}', f'{h:02d}{m:02d}', f'{h:02d} {m:02d}', f'{h:02d}:{m:02d} hours', f'{h:02d}{m:02d} hours']))


# ================================================================= independent helpers for the puzzles
def pay_ways(total, coins):
    """Every way of paying `total` with the coins (as many of each as you like): a list of tuples (count of each coin, in the order of `coins`), found by trying every count."""
    out = []

    def go(i, left, so_far):
        if i == len(coins):
            if left == 0:
                out.append(tuple(so_far))
            return
        n = 0
        while n * coins[i] <= left:
            go(i + 1, left - n * coins[i], so_far + [n])
            n += 1
    go(0, total, [])
    return out


def amounts(coins):
    """Every different amount of money that one coin, two coins, ... or all the coins can make (each coin used at most once)."""
    seen = set()
    for r in range(1, len(coins) + 1):
        for combo in itertools.combinations(coins, r):
            seen.add(sum(combo))
    return sorted(seen)


def handshakes(n):
    """The number of handshakes of n friends, counted pair by pair."""
    return len(list(itertools.combinations(range(n), 2)))


def queue_total(front, back):
    """The children in a queue when one child is `front`th from the front and `back`th from the back: build the queue and count."""
    queue = list(range(1, front + back))           # a queue long enough: positions 1..; the child is at `front`
    n = front + back - 1
    assert queue[front - 1] == front and n - front + 1 == back
    return n


def numbers_from_digits(cards, pred=None):
    """Every number made by using each digit card once (no leading zero), in order."""
    out = set()
    for p in itertools.permutations(cards):
        if p[0] == 0:
            continue
        n = int(''.join(map(str, p)))
        if pred is None or pred(n):
            out.add(n)
    return sorted(out)


# ================================================================= figures (phone first: every text is at least 12.5 px on a 360 px phone)
def bracket(x0, x1, y, toward=1, c=None):
    """A horizontal bracket with short ends; the ends point `toward` (+1 down, -1 up)."""
    h = _h()
    return f'<path d="M{x0} {y + 7 * toward} L{x0} {y} L{x1} {y} L{x1} {y + 7 * toward}" fill="none" stroke="{c or h.NAVY}" stroke-width="2.4" stroke-linejoin="round"/>'


def vbracket(x, y0, y1, toward=1):
    """A vertical bracket on the right of two rows (the ends point `toward`: +1 to the left, i.e. towards the bars)."""
    h = _h()
    return f'<path d="M{x - 7 * toward} {y0} L{x} {y0} L{x} {y1} L{x - 7 * toward} {y1}" fill="none" stroke="{h.NAVY}" stroke-width="2.4" stroke-linejoin="round"/>'


def seg(x, y, w, hgt, text, kind='a', size=15):
    """One part of a bar model: kind a = yellow (to find / counted), h = hatched grey (already known / the box), b = blue (water), d = dashed white (to find)."""
    h = _h()
    fill = {'a': h.YEL, 'h': '#E8EBF2', 'b': BLU, 'd': '#fff'}[kind]
    dash = '5 4' if kind == 'd' else None
    out = h.Re(x, y, w, hgt, fill, h.NAVY, 2.4, 0, dash)
    if text != '':
        out += h.T(x + w / 2, y + hgt / 2 + 5.5, text, size, 'middle', 700)
    return out


def ribbon_fig(solved=False):
    """A ribbon 3 m = 300 cm: four pieces of 65 cm and the part left over (to find; solved: shows 40)."""
    h = _h()
    s, x0, y = 0.92, 12, 50
    body = bracket(x0, x0 + 300 * s, 38, 1) + h.T(x0 + 150 * s, 22, '3 m = 300 cm', 15, 'middle', 800, h.TEAL)
    for i in range(4):
        body += seg(x0 + i * 65 * s, y, 65 * s, 36, '65')
    body += seg(x0 + 260 * s, y, 40 * s, 36, '40' if solved else '?', 'd')
    return h.svg(300, 96, body, 'A ribbon 3 m long (300 cm) with four pieces of 65 cm and a piece left over' + (': 40 cm' if solved else ''))


def strip_fig():
    """The 24 hours of a day as two rows: am (00:00 to 12:00) and pm (12:00 to 24:00), a label every 3 hours."""
    h = _h()
    x0, x1 = 24, 276
    px = lambda hr: x0 + hr * (x1 - x0) / 12
    body = ''
    for row, (y, lo, name, fill) in enumerate([(8, 0, 'am (before noon)', '#fff'), (78, 12, 'pm (after noon)', '#F1ECD9')]):
        body += h.Re(x0, y, x1 - x0, 28, fill, h.NAVY, 2.4) + h.T((x0 + x1) / 2, y + 20, name, 15, 'middle', 800)
        for k in range(0, 13, 3):
            body += h.Ln(px(k), y + 28, px(k), y + 38, 2.4) + h.T(px(k), y + 54, f'{lo + k:02d}:00', 13.5, 'middle', 700)
    return h.svg(300, 148, body, 'The 24 hours of a day in two rows. The am row runs from 00:00 to 12:00 and the pm row from 12:00 to 24:00, with a label every 3 hours.')


def time_line(t0, t1, ticks, hops=(), minor=(), marks=(), label='', W=300):
    """A time line (minutes since midnight). ticks: [(t, text, level)] (level 1 = the label sits one line lower, with a thin line up to its tick);
    hops: [(from, to, text)] drawn as arcs over the line, with an arrow; minor: [t] small unlabelled ticks; marks: [(t, text)] a teal arrow from above (such as 'Ravi arrives')."""
    h = _h()
    x0, x1 = 16, W - 16
    px = lambda t: x0 + (t - t0) * (x1 - x0) / (t1 - t0)
    ay = 74 if hops or marks else 30
    body = h.Ln(x0 - 8, ay, x1 + 4, ay, 3) + f'<polygon points="{x1 + 10},{ay} {x1 + 1},{ay - 6} {x1 + 1},{ay + 6}" fill="{h.NAVY}"/>'
    for t in minor:
        body += h.Ln(px(t), ay - 7, px(t), ay + 7, 2.2)
    lv = 0
    for t, text, level in ticks:
        lv = max(lv, level)
        body += h.Ln(px(t), ay - 9, px(t), ay + 9, 2.6)
        if level:
            body += h.Ln(px(t), ay + 10, px(t), ay + 30, 1.4, '#7C86A2', '3 3')
        body += h.T(px(t), ay + 28 + 20 * level + 4, text, 14, 'middle', 800)
    for a, b, text in hops:
        xa, xb = px(a), px(b)
        mid = (xa + xb) / 2
        body += f'<path d="M{xa} {ay - 10} Q{mid} {ay - 56} {xb} {ay - 10}" fill="none" stroke="{h.TEAL}" stroke-width="2.4"/>'
        body += f'<polygon points="{xb},{ay - 9} {xb - 5.5},{ay - 19} {xb + 4.5},{ay - 17}" fill="{h.TEAL}"/>'
        body += h.T(mid, ay - 50, text, 14, 'middle', 800, h.TEAL)
    for t, text in marks:
        body += h.Ln(px(t), ay - 36, px(t), ay - 9, 2.6, h.TEAL) + h.T(px(t), ay - 44, text, 14, 'middle', 800, h.TEAL)
    H = ay + 28 + 20 * lv + 14
    return h.svg(W, H, body, label or 'A time line')


def price_list_fig(items, label='Prices'):
    """items: [(name, price text)]; a small picture (from the workbook's own item pictures), the name and the price on each row."""
    h = _h()
    pics = figs5()['pics']
    rh, body = 40, ''
    for i, (name, price) in enumerate(items):
        y = i * rh + 4
        pic = pics.get(name, '')
        pic = re.sub(r'<svg[^>]*>', f'<svg x="8" y="{y + 3}" viewBox="0 0 48 48" width="32" height="32">', pic, count=1)
        body += pic + h.T(54, y + 26, name, 16, 'start', 800) + h.T(292, y + 26, price, 17, 'end', 800)
        body += h.Ln(4, y + rh - 3, 296, y + rh - 3, 1.2, '#C9D0E2')
    return h.svg(300, len(items) * rh + 6, body, label + ': ' + '; '.join(f'{n} {p}' for n, p in items))


def clue_fig(title_lines, clues, label):
    """A card of clues (one shared picture for every question of a logic puzzle): a heading sentence and 'Clue 1: ...' lines, wrapped to fit a phone."""
    h = _h()
    y, body, wrapped = 26, '', []
    for t in title_lines:
        wrapped += [(w, True) for w in textwrap.wrap(t, 36)]
    for i, c in enumerate(clues):
        lines = textwrap.wrap(f'Clue {i + 1}: {c}', 36)
        wrapped += [(w, False) for w in lines]
    H = len(wrapped) * 21 + 24
    body += h.Re(4, 4, 292, H, h.PALE, h.NAVY, 2.4, 10)
    for w, head in wrapped:
        body += h.T(16, y, w, 14.5, 'start', 800 if head else 700)
        y += 21
    return h.svg(300, H + 8, body, label)


# ---------------------------------------------------------------- the drinks bar graph of Lesson 10 (drawn from the printed data; the printed one has 4 px per cup, this one 3.2)
DRINKS = [('Milo', 45), ('Teh', 30), ('Kopi', 55), ('Bandung', 20)]
PATS = ['hz', 'dt', 'hx', 'hh', 'hv']


def drinks_fig(lime=None):
    """The bar graph of cups of drinks sold. lime=None: the Lime juice bar is missing (a dashed '?' slot); lime=50: its bar is drawn."""
    h = _h()
    x0, y0, k, slot, bw = 40, 218, 3.2, 50, 34
    defs = ('<defs>'
            f'<pattern id="hz" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="8" height="8" fill="#fff"/><line x1="0" y1="0" x2="0" y2="8" stroke="{h.NAVY}" stroke-width="2.2"/></pattern>'
            f'<pattern id="dt" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#fff"/><circle cx="4" cy="4" r="1.7" fill="{h.NAVY}"/></pattern>'
            f'<pattern id="hx" width="9" height="9" patternUnits="userSpaceOnUse"><rect width="9" height="9" fill="#fff"/><path d="M0 0L9 9M9 0L0 9" stroke="{h.NAVY}" stroke-width="1.6"/></pattern>'
            f'<pattern id="hh" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#fff"/><line x1="0" y1="4" x2="8" y2="4" stroke="{h.NAVY}" stroke-width="2.2"/></pattern>'
            f'<pattern id="hv" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#fff"/><line x1="4" y1="0" x2="4" y2="8" stroke="{h.NAVY}" stroke-width="2.2"/></pattern>'
            '</defs>')
    body = defs
    for v in range(0, 61, 10):
        y = y0 - v * k
        body += h.Ln(x0, y, x0 + 5 * slot + 8, y, 3 if v == 0 else 1.2, h.NAVY if v == 0 else '#9AA6C4') + h.T(x0 - 7, y + 5, v, 14, 'end', 700)
    body += h.Ln(x0, y0, x0, y0 - 62 * k, 3)
    bars = DRINKS + [('Lime juice', lime)]
    for i, (name, v) in enumerate(bars):
        x = x0 + 8 + i * slot
        if v is not None:
            body += h.Re(x, y0 - v * k, bw, v * k, f'url(#{PATS[i]})', h.NAVY, 2.4) + h.Re(x + bw / 2 - 15, y0 - v * k - 21, 30, 18, '#fff', 'none', 0) + h.T(x + bw / 2, y0 - v * k - 6, v, 15, 'middle', 800)
        else:
            body += h.Re(x, y0 - 5, bw, 5, 'none', h.NAVY, 2.2, 0, '6 4') + h.T(x + bw / 2, y0 - 14, '?', 22, 'middle', 800)
        cx = x + bw / 2
        body += h.T(cx + 4, y0 + 20, name, 14, 'end', 700).replace('<text ', f'<text transform="rotate(-40 {cx + 4} {y0 + 20})" ')
    body += h.T(10, y0 - 100, 'Number of cups', 14, 'middle', 700).replace('<text ', f'<text transform="rotate(-90 10 {y0 - 100})" ')
    label = 'Bar graph of cups of drinks sold: Milo 45, Teh 30, Kopi 55, Bandung 20, and ' + ('Lime juice 50' if lime is not None else 'the bar for Lime juice is missing')
    return h.svg(300, y0 + 62, body, label)


def queue_fig(front, back, who='Ben'):
    """The queue with one child (`who`) counted from the front (top row) and from the back (bottom row); the two rows share the child, like the printed figure."""
    h = _h()
    r, step = 16, 41
    nfront, nback = front - 1, back - 1
    xs = 14 + r + nfront * step           # x of the shared child
    W = max(300, xs + nback * step + r + 14)
    body = h.T(8, 16, 'front', 14, 'start', 700, h.TEAL, True) + h.T(W - 8, 16, 'back', 14, 'end', 700, h.TEAL, True)
    ord_ = lambda n: f'{n}{"th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")}'
    y1, y2 = 52, 128
    for i in range(1, front):
        x = xs - (front - i) * step
        body += h.Ci(x, y1, r, '#fff') + h.T(x, y1 + 34, ord_(i), 13.5, 'middle', 700)
    body += h.Ci(xs, y1, r, h.YEL) + h.T(xs, y1 + 5, who[:3], 13, 'middle', 800) + h.T(xs, y1 + 34, ord_(front), 13.5, 'middle', 700)
    body += h.Ci(xs, y2, r, h.YEL) + h.T(xs, y2 + 5, who[:3], 13, 'middle', 800) + h.T(xs, y2 + 34, ord_(back), 13.5, 'middle', 700)
    for j in range(1, back):
        x = xs + j * step
        n = back - j
        body += h.Ci(x, y2, r, '#fff') + h.T(x, y2 + 34, 'last' if n == 1 else ord_(n), 13.5, 'middle', 700)
    body += h.T(xs + r + 10, y1 + 5, 'from the front', 13.5, 'start', 700, '#44506F') + h.T(xs - r - 10, y2 + 5, 'from the back', 13.5, 'end', 700, '#44506F')
    return h.svg(W, y2 + 46, body, f'{who} is {ord_(front)} from the front and {ord_(back)} from the back. The two counts share {who}.')


def queue_between_fig():
    """Ali 2nd from the front, 3 people between Ali and Siti, Siti last (the printed figure)."""
    h = _h()
    r = 16
    body = h.T(8, 16, 'front', 14, 'start', 700, h.TEAL, True) + h.T(292, 16, 'back', 14, 'end', 700, h.TEAL, True)
    y = 62
    body += h.Ci(30, y, r, '#fff') + h.Ci(76, y, r, h.YEL) + h.T(76, y + 5, 'Ali', 13, 'middle', 800) + h.T(76, y + 36, '2nd', 13.5, 'middle', 700)
    body += h.Re(108, y - 22, 114, 44, '#fff', h.NAVY, 2.2, 8, '6 4') + h.T(165, y - 3, '3 people', 14, 'middle', 800, h.TEAL) + h.T(165, y + 14, 'between', 14, 'middle', 800, h.TEAL)
    body += h.Ci(262, y, r, h.YEL) + h.T(262, y + 5, 'Siti', 13, 'middle', 800) + h.T(262, y + 36, 'last', 13.5, 'middle', 700)
    return h.svg(300, 112, body, 'Ali is 2nd from the front, 3 people are between Ali and Siti, and Siti is last')


def cards_fig(digits):
    h = _h()
    body = ''
    for i, d in enumerate(digits):
        x = 10 + i * 66
        body += h.Re(x, 6, 54, 62, h.YEL, h.NAVY, 3, 8) + h.T(x + 27, 48, d, 30, 'middle', 800)
    return h.svg(max(150, 20 + len(digits) * 66), 76, body, 'Digit cards ' + ', '.join(str(d) for d in digits))


def sticks_fig(table=(4, 7, 10, None, None, None), solved=None):
    """Matchstick squares in a row (1, 2 and 3 squares) and the table of squares and sticks; None = a dashed box to fill (solved: the values shown)."""
    h = _h()
    u, y = 36, 12
    body, x = '', 16
    for n in (1, 2, 3):
        for i in range(n):
            xx = x + i * u
            body += h.Ln(xx, y, xx + u, y, 6, h.NAVY) + h.Ln(xx, y + u, xx + u, y + u, 6, h.NAVY)
        for i in range(n + 1):
            xx = x + i * u
            body += h.Ln(xx, y, xx, y + u, 6, h.NAVY)
        body += h.T(x + n * u / 2, y + u + 28, f'{n} square' + ('s' if n > 1 else ''), 14, 'middle', 700)
        x += n * u + 26
    ty = 108
    cw0, cw = 74, 36
    body += h.Re(4, ty, cw0, 32, '#E8EBF2', h.NAVY, 2) + h.T(4 + cw0 / 2, ty + 21, 'Squares', 13, 'middle', 800)
    body += h.Re(4, ty + 32, cw0, 36, '#fff', h.NAVY, 2) + h.T(4 + cw0 / 2, ty + 56, 'Sticks', 13, 'middle', 800)
    vals = list(solved) if solved else list(table)
    for i in range(6):
        xx = 4 + cw0 + i * cw
        body += h.Re(xx, ty, cw, 32, '#E8EBF2', h.NAVY, 2) + h.T(xx + cw / 2, ty + 22, i + 1, 15, 'middle', 800)
        v = vals[i]
        if v is None:
            body += h.Re(xx, ty + 32, cw, 36, '#fff', h.NAVY, 2, 0, '4 3') + h.T(xx + cw / 2, ty + 57, '?', 16, 'middle', 700, '#5B6785')
        else:
            body += h.Re(xx, ty + 32, cw, 36, h.YEL if solved and table[i] is None else '#fff', h.NAVY, 2) + h.T(xx + cw / 2, ty + 57, v, 16, 'middle', 700)
    return h.svg(300, ty + 76, body, 'Squares made in a row with sticks: 1 square, 2 squares and 3 squares, and a table of the number of sticks for 1 to 6 squares')


def triangles_fig():
    """Triangles in a row made with sticks: 1, 2 and 3 triangles (3, 5 and 7 sticks)."""
    h = _h()
    w, ht, y = 38, 34, 10
    body, x = '', 14
    for n in (1, 2, 3):
        pts = [(x + i * w / 2, y + ht if i % 2 == 0 else y) for i in range(n + 2)]   # zigzag: bottom, top, bottom, ...
        for a, b in zip(pts, pts[1:]):
            body += h.Ln(a[0], a[1], b[0], b[1], 5)
        for i in range(n):                                                           # the chords: every other point of the zigzag
            a, b = pts[i], pts[i + 2]
            body += h.Ln(a[0], a[1], b[0], b[1], 5)
        body += h.T(x + (n + 1) * w / 4, y + ht + 28, f'{n} triangle' + ('s' if n > 1 else ''), 14, 'middle', 700)
        x += (n + 1) * w / 2 + 28
    return h.svg(300, y + ht + 40, body, 'Triangles made in a row with sticks: 1 triangle, 2 triangles and 3 triangles')


def ways_table_fig(ways, label):
    """The table of every way of paying: 20-cent, 10-cent and 5-cent coins, one row for each way."""
    h = _h()
    rh = 24
    cw = [100, 100, 100]
    body = ''
    heads = ['20-cent coins', '10-cent coins', '5-cent coins']
    for j, t in enumerate(heads):
        body += h.Re(2 + sum(cw[:j]), 2, cw[j], 32, '#E8EBF2', h.NAVY, 2) + h.T(2 + sum(cw[:j]) + cw[j] / 2, 23, t.replace('-cent coins', '-cent'), 14, 'middle', 800)
    for i, w in enumerate(ways):
        for j, v in enumerate(w):
            body += h.Re(2 + sum(cw[:j]), 34 + i * rh, cw[j], rh, '#fff', h.NAVY, 1.6) + h.T(2 + sum(cw[:j]) + cw[j] / 2, 34 + i * rh + 17, v, 15, 'middle', 700)
    return h.svg(304, 36 + len(ways) * rh + 4, body, label)


def box_books_fig():
    """Think harder 3: a box and 4 books in a row, 1 kg 50 g altogether."""
    h = _h()
    u, x0, y = 52, 12, 30
    body = h.T(x0, 18, 'Box + 4 books', 15, 'start', 800)
    x = x0
    body += seg(x, y, 1.25 * u, 34, 'box', 'h', 14)
    x += 1.25 * u
    for _ in range(4):
        body += seg(x, y, u, 34, '?')
        x += u
    body += bracket(x0, x, y + 42, -1) + h.T((x0 + x) / 2, y + 66, '1 kg 50 g', 15, 'middle', 800, h.TEAL)
    return h.svg(300, y + 78, body, 'A box and four books in a row; together they weigh 1 kg 50 g')


def bottle_fig():
    """Go further 5: a full bottle (bottle + 2 parts of water) and the same bottle with half the water poured out."""
    h = _h()
    u, x0 = 56, 12
    body = bracket(x0, x0 + 4 * u, 30, 1) + h.T(x0 + 2 * u, 20, '1 kg 200 g', 15, 'middle', 800, h.TEAL)
    body += h.T(x0, 56, 'Full', 15, 'start', 800)
    body += seg(x0, 62, u, 34, 'bottle', 'h', 14) + seg(x0 + u, 62, 1.5 * u, 34, 'water', 'b') + seg(x0 + 2.5 * u, 62, 1.5 * u, 34, 'water', 'b')
    body += h.T(x0, 126, 'Half poured out', 15, 'start', 800)
    body += seg(x0, 132, u, 34, 'bottle', 'h', 14) + seg(x0 + u, 132, 1.5 * u, 34, 'water', 'b')
    body += bracket(x0, x0 + 2.5 * u, 174, -1) + h.T(x0 + 1.25 * u, 198, '750 g', 15, 'middle', 800, h.TEAL)
    return h.svg(300, 208, body, 'A bottle full of water weighs 1 kg 200 g. With half of the water poured out it weighs 750 g.')


def pens_files_fig():
    """Go further 6: 3 pens and 2 files (each file is a pen and 60 cents more); $9.20 altogether."""
    h = _h()
    u, x0 = 58, 12
    body = h.T(x0, 18, '3 pens', 15, 'start', 800)
    for i in range(3):
        body += seg(x0 + i * u, 24, u, 34, '?')
    body += h.T(x0, 84, '2 files', 15, 'start', 800)
    x = x0
    for _ in range(2):
        body += seg(x, 90, u, 34, '?') + seg(x + u, 90, 0.66 * u, 34, '60¢', 'h', 13)
        x += 1.66 * u
    bx = x + 10
    body += vbracket(bx, 24, 124) + h.T(bx + 10, 80, '$9.20', 17, 'start', 800, h.TEAL)
    return h.svg(bx + 78, 134, body, 'Three pens in one row and two files in another row; each file is a pen and 60 cents more. All five cost $9.20.')
