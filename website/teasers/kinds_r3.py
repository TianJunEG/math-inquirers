"""GENERATOR side, part 4 (fix round 3): solvers for the NEW sub-structures added in round 3 (see taxonomy.json, ids marked "round 3").

Same contract as kinds.py: SOLVE[kind](**params) -> (answer, ctx).  Merged into kinds.SOLVE at the bottom of kinds.py.
The independent checkers are in brute_r3.py (which never imports this file); samples_r3.py lists worked instances and
`verify_bank.py --selftest` proves solver and checker agree on each, even for sub-structures that no released month uses yet."""
import itertools
import math
from fractions import Fraction as Fr

SOLVE = {}


def kind(fn):
    SOLVE[fn.__name__] = fn
    return fn


def _j(xs, sep=', '):
    return sep.join(str(x) for x in xs)


# ================================================================== counting, time, young structures
@kind
def intervals(n1, t1, n2):
    """n1 strikes (or cuts, or knocks) take t1 in all: the gaps between them are equal; the time for n2 of them."""
    gaps1, gaps2 = n1 - 1, n2 - 1
    assert t1 % gaps1 == 0
    per = t1 // gaps1
    return per * gaps2, {'gaps1': gaps1, 'gaps2': gaps2, 'per': per}


@kind
def unit_compare(dens, names, ask):
    """Several people each take 1/d of the same whole (ask most / least) or how many 1/b pieces fit in 1/a (ask fit)."""
    if ask == 'fit':
        a, b = dens
        assert b % a == 0
        return b // a, {'a': a, 'b': b}
    pairs = sorted(zip(dens, names))
    assert len({d for d in dens}) == len(dens)
    if ask == 'most':
        return pairs[0][1], {'den': pairs[0][0]}
    return pairs[-1][1], {'den': pairs[-1][0]}


@kind
def weeks_days(mode, w=0, d=0, n=0):
    if mode == 'total':          # w weeks and d days -> days
        return 7 * w + d, {'wk': 7 * w}
    if mode == 'rest':           # n days -> days left over after whole weeks
        return n % 7, {'weeks': n // 7, 'full': 7 * (n // 7)}
    if mode == 'weeks':          # n days -> whole weeks
        return n // 7, {'rest': n % 7}
    if mode == 'longer':         # w weeks d days against n days: how many days longer is the first
        tot = 7 * w + d
        return tot - n, {'tot': tot}
    raise ValueError(mode)


@kind
def swaps(order):
    """Fewest swaps of two NEIGHBOURS to put a row in order from smallest to biggest = the number of pairs that are the wrong way round."""
    n = len(order)
    inv = sum(1 for i in range(n) for j in range(i + 1, n) if order[i] > order[j])
    return inv, {'n': n}


@kind
def overlap_chain(ask, n=None, length=None, overlap=None, total=None):
    if ask == 'total':
        return n * length - (n - 1) * overlap, {'step': length - overlap}
    step = length - overlap
    assert (total - length) % step == 0
    return (total - length) // step + 1, {'step': step}


@kind
def ferry_trips(people, cap):
    """All start on one bank; the boat holds `cap` (somebody must always row it); crossings in either direction."""
    assert cap >= 2 and people > cap
    back_and_forth = -(-(people - cap) // (cap - 1))
    return 2 * back_and_forth + 1, {'rounds': back_and_forth, 'first': cap - 1}


@kind
def dice_ways(sides, total, ordered):
    n = sides - abs(total - (sides + 1))
    assert n >= 1
    if ordered:
        return n, {'pairs': n}
    return (n + 1) // 2, {'pairs': n}


@kind
def checkerboard(rows, cols, ask):
    """Dark and light squares alternate and the top-left square is dark."""
    cells = rows * cols
    if ask == 'dark':
        return (cells + 1) // 2, {'cells': cells}
    if ask == 'light':
        return cells // 2, {'cells': cells}
    if ask == 'edge_dark':
        return rows + cols - 2, {'edge': 2 * (rows + cols) - 4}
    raise ValueError(ask)


@kind
def equal_marks(start, end, marks, k, ask):
    gaps = marks - 1
    assert (end - start) % gaps == 0
    step = (end - start) // gaps
    if ask == 'step':
        return step, {'gaps': gaps}
    return start + (k - 1) * step, {'step': step, 'gaps': gaps}


@kind
def sum_later(a, b, target):
    assert (target - a - b) % 2 == 0 and target > a + b
    yrs = (target - a - b) // 2
    return yrs, {'now': a + b}


@kind
def order_by_key(numbers, rule, place):
    def key(n):
        ds = [int(c) for c in str(n)]
        return sum(ds) if rule == 'digit_sum' else math.prod(ds)
    ks = [key(n) for n in numbers]
    assert len(set(ks)) == len(ks), ks
    order = sorted(numbers, key=key)
    return order[place - 1], {'sorted': _j(order, ', '), 'keys': _j(sorted(ks), ', ')}


_NW = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
       11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
       18: 'eighteen', 19: 'nineteen', 20: 'twenty'}


@kind
def alpha_numbers(lo, hi, place):
    ws = sorted((_NW[n], n) for n in range(lo, hi + 1))
    return ws[place - 1][1], {'list': _j([w for w, _ in ws]), 'word': ws[place - 1][0]}


@kind
def alt_steps(start, deltas, ask, n=None, target=None):
    cyc = sum(deltas)
    if ask == 'after':
        full, rest = divmod(n, len(deltas))
        return start + full * cyc + sum(deltas[:rest]), {'cyc': cyc, 'full': full, 'rest': rest}
    # first step at which the value reaches the target (never before): checked step by step
    v, k = start, 0
    while v < target:
        v += deltas[k % len(deltas)]
        k += 1
        assert k < 10000
    return k, {'cyc': cyc}


@kind
def pass_places(start, moves, total, ask):
    place = start
    for kind_, k in moves:
        place += -k if kind_ == 'pass' else k
    assert 1 <= place <= total
    return (place if ask == 'place' else total - place), {'place': place}


@kind
def displacement(moves):
    x = y = 0
    for d, k in moves:
        dx, dy = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}[d]
        x, y = x + dx * k, y + dy * k
    assert (x, y) != (0, 0)
    return abs(x) + abs(y), {'x': x, 'y': y}


# ================================================================== time, number, measure
@kind
def schedule_breaks(start_h, start_m, parts, part_min, break_min, ask):
    total = parts * part_min + (parts - 1) * break_min
    if ask == 'total':
        return total, {'breaks': parts - 1, 'work': parts * part_min, 'rest': (parts - 1) * break_min}
    if ask == 'end24':
        t = start_h * 60 + start_m + total
        return (t // 60 % 24) * 100 + t % 60, {'total': total, 'hm': '%d h %d min' % (total // 60, total % 60)}
    raise ValueError(ask)


@kind
def reverse_division(divisor, quotient, remainder, ask, add=0):
    num = divisor * quotient + remainder
    if ask == 'number':
        return num, {'prod': divisor * quotient}
    return (num + add) // divisor, {'num': num, 'new': num + add}


@kind
def fake_coin(ask, n=None, w=None):
    if ask == 'max_coins':
        return 3 ** w, {}
    k, cap = 0, 1
    while cap < n:
        cap *= 3
        k += 1
    return k, {'cap': cap}


@kind
def mirror_time(h, m, ask):
    t = (720 - (h * 60 + m)) % 720
    th, tm = t // 60 or 12, t % 60
    return (th if ask == 'hour' else tm), {'hh': th, 'mm': '%02d' % tm}


@kind
def swap_digits(ask, number=None, pos=None, diff=None, t=None, h=None):
    if ask == 'difference':
        s = str(number)
        i, j = pos
        l = list(s)
        l[i], l[j] = l[j], l[i]
        return abs(int(''.join(l)) - number), {'new': ''.join(l)}
    # hundreds and ones swapped, the number gets `diff` bigger; tens digit t and hundreds digit h known
    assert diff % 99 == 0
    o = h + diff // 99
    assert 0 <= o <= 9
    return h * 100 + t * 10 + o, {'o': o, 'gap': diff // 99}


@kind
def notch_perimeter(w, h, notches, unit):
    # notches cut from corners never change the outline length
    return 2 * (w + h) * unit, {'full': 2 * (w + h)}


@kind
def container_mass(full, part, num, den, ask):
    f = Fr(num, den)
    contents = Fr(full - part) / (1 - f)
    jar = full - contents
    assert contents.denominator == 1 and jar >= 0
    return (int(jar) if ask == 'jar' else int(contents)), {'contents': int(contents), 'jar': int(jar), 'less': full - part}


@kind
def missing_term(n, got):
    total = n * (n + 1) // 2
    return total - got, {'total': total}


@kind
def jug_steps(a, b, target):
    from collections import deque
    start = (0, 0)
    seen = {start: 0}
    dq = deque([start])
    while dq:
        x, y = dq.popleft()
        if x == target or y == target:
            return seen[(x, y)], {}
        nxt = [(a, y), (x, b), (0, y), (x, 0)]
        p = min(x, b - y)
        nxt.append((x - p, y + p))
        p = min(y, a - x)
        nxt.append((x + p, y - p))
        for s in nxt:
            if s not in seen:
                seen[s] = seen[(x, y)] + 1
                dq.append(s)
    raise ValueError('target cannot be measured')


@kind
def euler_lifts(edges):
    deg = {}
    for u, v in edges:
        deg[u] = deg.get(u, 0) + 1
        deg[v] = deg.get(v, 0) + 1
    odd = sorted(k for k, d in deg.items() if d % 2)
    strokes = max(1, len(odd) // 2)
    return strokes - 1, {'odd': _j(odd), 'nodd': len(odd), 'strokes': strokes}


@kind
def diagonal_squares(w, h):
    return w + h - math.gcd(w, h), {'g': math.gcd(w, h)}


@kind
def net_opposite(cells, ask):
    """cells = {'A': (col, row), ...}: a cube net.  Roll a cube over the net starting on the first cell; the face that lands on each cell is that cell's face."""
    names = list(cells)
    pos = {c: n for n, c in cells.items()}
    # orientation: (top, bottom, north, south, east, west) as face labels of a numbered cube 0..5
    start = cells[names[0]]
    ori = dict(top=0, bottom=1, north=2, south=3, east=4, west=5)
    face = {start: ori['bottom']}      # the cube sits on the first cell: its bottom touches the net there
    todo = [(start, ori)]
    while todo:
        (cx, cy), o = todo.pop()
        for dx, dy, d in ((1, 0, 'east'), (-1, 0, 'west'), (0, -1, 'north'), (0, 1, 'south')):
            nc = (cx + dx, cy + dy)
            if nc in pos and nc not in face:
                t, b, n, s, e, w = o['top'], o['bottom'], o['north'], o['south'], o['east'], o['west']
                if d == 'east':
                    no = dict(top=w, bottom=e, north=n, south=s, east=t, west=b)
                elif d == 'west':
                    no = dict(top=e, bottom=w, north=n, south=s, east=b, west=t)
                elif d == 'north':
                    no = dict(top=s, bottom=n, north=t, south=b, east=e, west=w)
                else:
                    no = dict(top=n, bottom=s, north=b, south=t, east=e, west=w)
                face[nc] = no['bottom']
                todo.append((nc, no))
    assert len(set(face.values())) == 6, 'not a cube net'
    opp = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}
    me = face[cells[ask]]
    for n, c in cells.items():
        if face[c] == opp[me]:
            return n, {'pair': '%s and %s' % (ask, n)}
    raise ValueError


@kind
def symmetry_add(grid, axis):
    rows = grid
    h, w = len(rows), len(rows[0])
    need = set()
    for y in range(h):
        for x in range(w):
            if rows[y][x] == '#':
                m = (y, w - 1 - x) if axis == 'vertical' else (h - 1 - y, x)
                if rows[m[0]][m[1]] != '#':
                    need.add(m)
    return len(need), {'cells': len(need)}


@kind
def venn3(total, a, b, c, ab, ac, bc, abc, ask):
    union = a + b + c - ab - ac - bc + abc
    if ask == 'none':
        return total - union, {'union': union}
    if ask == 'union':
        return union, {'union': union}
    if ask == 'only_one':
        return a + b + c - 2 * (ab + ac + bc) + 3 * abc, {'union': union}
    raise ValueError(ask)


@kind
def cut_corners_area(w, h, cuts, unit=1):
    area = Fr(w * h) - sum(Fr(a * b, 2) for a, b in cuts)
    assert area.denominator == 1
    return int(area) * unit * unit, {'full': w * h, 'cut': _j([Fr(a * b, 2) for a, b in cuts], ' and ')}


@kind
def combined_mean(groups, ask, overall=None):
    n = sum(g[0] for g in groups)
    tot = sum(g[0] * g[1] for g in groups)
    if ask == 'mean':
        assert tot % n == 0
        return tot // n, {'n': n, 'tot': tot}
    # find the mean of the last group from the overall mean
    known = sum(g[0] * g[1] for g in groups[:-1])
    last = Fr(overall * n - known, groups[-1][0])
    assert last.denominator == 1
    return int(last), {'n': n, 'tot': overall * n, 'known': known}


@kind
def ratio_change(mode, a, b, c, d, k, ask):
    """Quantities in the ratio a:b. mode 'add': the first gets k more and the ratio becomes c:d; mode 'give': the first gives k to the second."""
    if mode == 'add':
        den = c * b - a * d
        num = k * d
    else:
        den = c * b - a * d + 0
        # (a u - k)/(b u + k) = c/d  ->  d(a u - k) = c(b u + k)  ->  u (d a - c b) = k (d + c)
        den = d * a - c * b
        num = k * (d + c)
    assert den != 0 and num % den == 0 and num // den > 0
    u = num // den
    first, second = a * u, b * u
    out = {'first': first, 'second': second, 'total': first + second, 'unit': u}
    return out[ask], dict(out, u=u)


@kind
def share_fraction(num, den, people):
    v = Fr(num, den) / people
    return v, {'each': '%d/%d' % (v.numerator, v.denominator)}


@kind
def branch_prog(start, n, even_op, odd_op):
    x = start
    for _ in range(n):
        x = _apply(x, even_op if x % 2 == 0 else odd_op)
    return x, {'code': _branch_code(start, n, even_op, odd_op)}


def _apply(x, op):
    k, v = op
    return {'half': x // 2, 'add': x + v, 'sub': x - v, 'times3plus1': 3 * x + 1}[k]


def _opcode(op):
    k, v = op
    return {'half': 'x = x / 2', 'add': 'x = x + %d' % v, 'sub': 'x = x - %d' % v, 'times3plus1': 'x = 3 * x + 1'}[k]


def _branch_code(start, n, even_op, odd_op):
    return 'x = %d\nrepeat %d times:\n    if x is even:\n        %s\n    else:\n        %s\nsay x' % (start, n, _opcode(even_op), _opcode(odd_op))


@kind
def faulty_clock(g, clock_min):
    """A clock gains g minutes in every real hour; it shows clock_min minutes since it was set right: real minutes passed."""
    num = clock_min * 60
    assert num % (60 + g) == 0
    return num // (60 + g), {'per': 60 + g}


@kind
def triangle_sides(first, ask, side):
    """Six consecutive numbers first..first+5 in the three corners and the three side-middles of a triangle; every side adds to `side`.
    The corners must be the three smallest numbers (or the three biggest): ask for the biggest corner or the smallest middle."""
    nums = list(range(first, first + 6))
    total = sum(nums)
    corners = 3 * side - total
    low = sum(nums[:3])
    high = sum(nums[3:])
    assert corners in (low, high), (corners, low, high)
    cs = nums[:3] if corners == low else nums[3:]
    mids = [x for x in nums if x not in cs]
    return (max(cs) if ask == 'largest_corner' else min(mids)), {'corners': _j(cs), 'mids': _j(mids), 'csum': corners}


@kind
def digit_segments(lo, hi, table):
    tot = 0
    for n in range(lo, hi + 1):
        tot += sum(table[str(c)] for c in str(n))
    return tot, {}


@kind
def circle_out(n, k):
    """n children stand in a circle numbered 1..n; counting from child 1, every k-th child sits down; who is the last standing?"""
    kids = list(range(1, n + 1))
    i = 0
    while len(kids) > 1:
        i = (i + k - 1) % len(kids)
        kids.pop(i)
    return kids[0], {'n': n}
