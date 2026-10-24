"""GENERATOR side, part 3 (fix round 2): solvers for the NEW sub-structures added in round 2 (see taxonomy.json, ids marked "round 2").

Same contract as kinds.py: SOLVE[kind](**params) -> (answer, ctx).  Merged into kinds.SOLVE at the bottom of kinds.py.
The independent brute-force checkers are in brute_r2.py (which never imports this file); samples_r2.py lists one worked
instance per kind and `verify_bank.py --selftest` proves solver and checker agree on each."""
import itertools
import math
from fractions import Fraction as Fr

SOLVE = {}


def kind(fn):
    SOLVE[fn.__name__] = fn
    return fn


def _j(xs, sep=', '):
    return sep.join(str(x) for x in xs)


# ================================================================== cards, coins, number sense
@kind
def triple_sum(cards, target, ask):
    trip = [t for t in itertools.combinations(sorted(cards), 3) if sum(t) == target]
    assert len(trip) == 1, trip
    t = trip[0]
    ans = {'smallest': t[0], 'middle': t[1], 'largest': t[2]}[ask]
    return ans, {'trip': ' + '.join(str(x) for x in t), 'a': t[0], 'b': t[1], 'c': t[2]}


@kind
def coin_amounts(coins):
    sums = set()
    for c in coins:
        sums |= {s + c for s in sums} | {c}
    return len(sums), {'sums': _j(sorted(sums)), 'n': len(coins)}


@kind
def cannot_pay(coins, amounts):
    ok = []
    for a in amounts:
        reach = {0}
        for t in range(1, a + 1):
            if any((t - c) in reach for c in coins if t - c >= 0):
                reach.add(t)
        if a in reach:
            ok.append(a)
    return len(ok), {'can': _j(ok), 'cannot': _j([a for a in amounts if a not in ok])}


@kind
def halfway(a, b):
    assert (a + b) % 2 == 0
    return (a + b) // 2, {'gap': b - a, 'half': (b - a) // 2}


@kind
def odd_one_out(numbers):
    found = []
    for k in range(2, 11):
        non = [x for x in numbers if x % k]
        if len(non) == 1:
            found.append((k, non[0]))
    assert found and len({x for _, x in found}) == 1, found
    return found[0][1], {'k': found[0][0], 'ks': _j(sorted(k for k, _ in found))}


@kind
def page_digits(lo, hi):
    one = len([n for n in range(lo, hi + 1) if n < 10])
    two = len([n for n in range(lo, hi + 1) if 10 <= n < 100])
    three = len([n for n in range(lo, hi + 1) if n >= 100])
    return one + 2 * two + 3 * three, {'one': one, 'two': two, 'three': three, 'ones': one, 'twos': 2 * two, 'threes': 3 * three}


_WORDS = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
          12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
          20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}


def _word_len(n):
    if n in _WORDS:
        return len(_WORDS[n])
    if n == 100:
        return len('onehundred')
    return len(_WORDS[n // 10 * 10]) + len(_WORDS[n % 10])


@kind
def number_words(lo, hi):
    return sum(_word_len(n) for n in range(lo, hi + 1)), {'first': _WORDS.get(lo), 'last': _WORDS.get(hi)}


@kind
def hundred_chart(start, moves):
    cur = start
    path = [cur]
    for d, k in moves:
        step = {'down': 10, 'up': -10, 'right': 1, 'left': -1}[d]
        for _ in range(k):
            nxt = cur + step
            assert 1 <= nxt <= 100
            if d in ('left', 'right'):
                assert (nxt - 1) // 10 == (cur - 1) // 10
            cur = nxt
        path.append(cur)
    return cur, {'path': ' to '.join(str(x) for x in path)}


@kind
def days_in_common(r1, r2):
    lo, hi = max(r1[0], r2[0]), min(r1[1], r2[1])
    n = max(0, hi - lo + 1)
    return n, {'lo': lo, 'hi': hi}


@kind
def fan_triangles(n):
    return n * (n + 1) // 2, {'single': n, 'pairs': n - 1}


@kind
def function_machine(pairs, x, forms):
    (i1, o1), (i2, o2) = pairs[0], pairs[1]
    assert i1 != i2
    a = Fr(o2 - o1, i2 - i1)
    b = o1 - a * i1
    assert a.denominator == 1 and a >= 1
    a = int(a)
    kinds_ = set()
    if a == 1 and b != 0:
        kinds_.add('add')
    if b == 0 and a > 1:
        kinds_.add('mul')
    if a > 1 and b != 0:
        kinds_.add('both')
    assert kinds_ & set(forms), (a, b, forms)
    for i, o in pairs:
        assert a * i + b == o
    return a * x + b, {'a': a, 'b': int(b), 'rule': ('add %d' % b if a == 1 else 'times %d' % a if b == 0 else 'times %d then %s %d' % (a, 'add' if b > 0 else 'take away', abs(b)))}


# ================================================================== time
@kind
def clock_hand(h, m, add, ask):
    t = m + add
    mm = t % 60
    assert mm % 5 == 0
    hour = (h - 1 + t // 60) % 12 + 1
    if ask == 'number':
        return (mm // 5 or 12), {'mm': mm, 'hour': hour}
    if ask == 'minutes':
        return mm, {'mm': mm, 'hour': hour}
    if ask == 'hour':
        return hour, {'mm': mm, 'hour': hour}
    raise ValueError(ask)


def _h24(h, ap):
    return h % 12 + (12 if ap == 'pm' else 0)


@kind
def am_pm(times, ask):
    vals = [(_h24(h, ap), '%d %s' % (h, ap)) for h, ap in times]
    if ask == 'latest':
        return max(vals)[1], {}
    if ask == 'earliest':
        return min(vals)[1], {}
    if ask == 'hours':
        a, b = vals[0][0], vals[1][0]
        return (b - a) % 24, {'a': vals[0][1], 'b': vals[1][1]}
    raise ValueError(ask)


_MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
_MLEN = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


@kind
def date_after(month, day, add):
    i = _MONTHS.index(month)
    d = day + add
    new_month = month
    if d > _MLEN[i]:
        d -= _MLEN[i]
        new_month = _MONTHS[(i + 1) % 12]
    return d, {'new_month': new_month, 'len': _MLEN[i]}


@kind
def timetable_wait(first, every, now):
    t = first
    while t < now:
        t += every
    return t - now, {'next': t, 'next_h': t // 60, 'next_m': t % 60}


# ================================================================== shapes and arrangements
_SHAPES2 = {'circle': dict(straight=0, curved=1, equal=None), 'triangle': dict(straight=3, curved=0, equal=None),
            'square': dict(straight=4, curved=0, equal=True), 'rectangle': dict(straight=4, curved=0, equal=False),
            'half circle': dict(straight=1, curved=1, equal=None), 'quarter circle': dict(straight=2, curved=1, equal=None)}
_SHAPES3 = {'cube': dict(flat=6, curved=0, vertices=8, same=True), 'cuboid': dict(flat=6, curved=0, vertices=8, same=False),
            'cone': dict(flat=1, curved=1, vertices=1, same=None), 'cylinder': dict(flat=2, curved=1, vertices=0, same=None),
            'sphere': dict(flat=0, curved=1, vertices=0, same=None)}


@kind
def shape_riddle(pool, clue):
    table = _SHAPES2 if pool == '2d' else _SHAPES3
    hits = [name for name, d in table.items() if all(d.get(k) == v for k, v in clue.items())]
    assert len(hits) == 1, hits
    return hits[0], {}


@kind
def seat_number(per_row, ask, row=None, col=None, seat=None):
    if ask == 'seat':
        return (row - 1) * per_row + col, {'before': (row - 1) * per_row}
    if ask == 'row':
        return (seat - 1) // per_row + 1, {'full': (seat - 1) // per_row}
    if ask == 'col':
        return (seat - 1) % per_row + 1, {'full': (seat - 1) // per_row}
    raise ValueError(ask)


@kind
def circle_opposite(n, a, ask):
    assert n % 2 == 0
    if ask == 'opposite':
        return (a - 1 + n // 2) % n + 1, {'half': n // 2}
    if ask == 'between':
        return n // 2 - 1, {'half': n // 2}
    raise ValueError(ask)


@kind
def border_tiles(n, m):
    assert n >= 2 and m >= 2
    return 2 * (n + m) - 4, {'inner': (n - 2) * (m - 2), 'all': n * m}


@kind
def square_stack(n):
    layers = [k * k for k in range(1, n + 1)]
    return sum(layers), {'layers': ' + '.join(str(x) for x in layers)}


@kind
def dice_opposite(vals, ask):
    if ask == 'bottoms':
        return sum(7 - v for v in vals), {'each': ', '.join(str(7 - v) for v in vals)}
    if ask == 'hidden':
        assert len(set(vals)) == len(vals) and all(a + b != 7 for a, b in itertools.combinations(vals, 2))
        return 21 - sum(vals), {'seen': sum(vals)}
    raise ValueError(ask)


@kind
def polyomino(n):
    return {1: 1, 2: 1, 3: 2, 4: 5, 5: 12, 6: 35}[n], {}


@kind
def fold_cut(folds):
    return 2 ** folds + 1, {'layers': 2 ** folds, 'cuts': 2 ** folds}


# ================================================================== logic
@kind
def grid_totals(rows, cols, known, ask):
    R, C = len(rows), len(cols)
    cell = {(r, c): v for r, c, v in known}
    changed = True
    while changed:
        changed = False
        for r in range(R):
            miss = [c for c in range(C) if (r, c) not in cell]
            if len(miss) == 1:
                cell[(r, miss[0])] = rows[r] - sum(cell[(r, c)] for c in range(C) if c != miss[0])
                changed = True
        for c in range(C):
            miss = [r for r in range(R) if (r, c) not in cell]
            if len(miss) == 1:
                cell[(miss[0], c)] = cols[c] - sum(cell[(r, c)] for r in range(R) if r != miss[0])
                changed = True
    assert len(cell) == R * C, cell
    assert all(sum(cell[(r, c)] for c in range(C)) == rows[r] for r in range(R)) and all(sum(cell[(r, c)] for r in range(R)) == cols[c] for c in range(C))
    return cell[tuple(ask)], {'row_total': rows[ask[0]], 'col_total': cols[ask[1]]}


@kind
def symbols(eqs, ask, maxv):
    names = sorted({s for terms, _ in eqs for s in terms})
    sols = []
    for vals in itertools.product(range(1, maxv + 1), repeat=len(names)):
        env = dict(zip(names, vals))
        if all(sum(c * env[s] for s, c in terms.items()) == tot for terms, tot in eqs):
            sols.append(env)
    assert len(sols) == 1, sols
    return sols[0][ask], {'all': ', '.join('%s = %d' % (k, v) for k, v in sols[0].items())}


@kind
def insert_signs(nums, target):
    ways = {nums[0]: 1}
    for x in nums[1:]:
        new = {}
        for s, c in ways.items():
            new[s + x] = new.get(s + x, 0) + c
            new[s - x] = new.get(s - x, 0) + c
        ways = new
    return ways.get(target, 0), {}


@kind
def knockout(n):
    return n - 1, {'players': n}


@kind
def snaps(rows, cols):
    return rows * cols - 1, {'squares': rows * cols}


@kind
def latin_square(n, given, ask):
    cells = {(r, c): v for r, c, v in given}
    sols = []

    def fill(r, c, grid):
        if r == n:
            sols.append(dict(grid))
            return
        nr, nc = (r, c + 1) if c + 1 < n else (r + 1, 0)
        opts = [cells[(r, c)]] if (r, c) in cells else range(1, n + 1)
        for v in opts:
            if all(grid.get((r, k)) != v for k in range(c)) and all(grid.get((k, c)) != v for k in range(r)):
                grid[(r, c)] = v
                fill(nr, nc, grid)
                del grid[(r, c)]
    fill(0, 0, {})
    assert len(sols) == 1, len(sols)
    return sols[0][tuple(ask)], {}


@kind
def worst_case(counts, need, ask):
    if ask == 'k_alike':
        return sum(min(c, need - 1) for c in counts) + 1, {'safe': sum(min(c, need - 1) for c in counts)}
    if ask == 'all_colours':
        return sum(counts) - min(counts) + 1, {'others': sum(counts) - min(counts)}
    raise ValueError(ask)


@kind
def take_away_game(total, m):
    wins = [k for k in range(1, m + 1) if (total - k) % (m + 1) == 0]
    assert len(wins) == 1 and total - wins[0] >= 0
    return wins[0], {'leave': total - wins[0], 'cycle': m + 1}


@kind
def network_shortest(edges, a, b):
    dist = {a: 0}
    todo = {a}
    done = set()
    while todo:
        u = min(todo, key=lambda x: dist[x])
        todo.discard(u)
        done.add(u)
        for x, y, w in edges:
            for p, q in ((x, y), (y, x)):
                if p == u and q not in done and dist[u] + w < dist.get(q, 10 ** 9):
                    dist[q] = dist[u] + w
                    todo.add(q)
    return dist[b], {}


@kind
def sum_product(s, p, ask):
    pairs = [(x, s - x) for x in range(1, s // 2 + 1) if x * (s - x) == p]
    assert len(pairs) == 1, pairs
    return (pairs[0][1] if ask == 'larger' else pairs[0][0]), {'pair': '%d and %d' % pairs[0]}


@kind
def heads_legs(heads, legs, a, b):
    sols = [(x, heads - x) for x in range(heads + 1) if a * x + b * (heads - x) == legs]
    assert len(sols) == 1, sols
    return sols[0][1], {'fewer': sols[0][0]}


@kind
def bar_three(extras, total, ask):
    base = Fr(total - sum(extras), 1 + len(extras))
    assert base == int(base) and base > 0
    base = int(base)
    vals = [base] + [base + e for e in extras]
    return {'smallest': vals[0], 'largest': max(vals), 'last': vals[-1]}[ask], {'base': base, 'extra': sum(extras), 'vals': _j(vals)}


@kind
def compound_units(unit, a, b, op, times=1):
    big, small = {'m': ('m', 'cm'), 'km': ('km', 'm'), 'kg': ('kg', 'g'), 'L': ('L', 'ml'), 'h': ('h', 'min')}[unit]
    per = {'m': 100, 'km': 1000, 'kg': 1000, 'L': 1000, 'h': 60}[unit]
    x, y = a[0] * per + a[1], b[0] * per + b[1]
    val = {'sum': x + y, 'diff': x - y, 'times': x * times}[op]
    return val, {'x': x, 'y': y, 'small': small, 'big': big}


@kind
def best_deal(offers, want, ask):
    costs = []
    for o in offers:
        if o[0] == 'each':
            costs.append(o[1] * want)
        elif o[0] == 'pack':
            assert want % o[1] == 0
            costs.append(want // o[1] * o[2])
        elif o[0] == 'free':
            buy, get, price = o[1], o[2], o[3]
            assert want % (buy + get) == 0
            costs.append(want // (buy + get) * buy * price)
    if ask == 'saving':
        return abs(costs[0] - costs[1]), {'costs': _j(costs)}
    return min(costs), {'costs': _j(costs)}


@kind
def fraction_parts(total, eaten, ask):
    left = total - sum(eaten)
    assert left > 0
    if ask == 'fraction_left':
        return Fr(left, total), {'left': left}
    return left, {'left': left}


# ================================================================== higher-level additions (Levels 3 to 6)
@kind
def digit_sum_total(lo, hi):
    return sum(sum(int(c) for c in str(n)) for n in range(lo, hi + 1)), {}


@kind
def round_table(n):
    return math.factorial(n - 1), {}


@kind
def divisible_digit(template, by, ask):
    ok = [d for d in range(10) if int(template.replace('_', str(d))) % by == 0]
    assert ok
    return ({'count': len(ok), 'sum': sum(ok), 'largest': max(ok), 'smallest': min(ok)}[ask]), {'digits': _j(ok)}


@kind
def work_time(people, days, new_people):
    total = people * days
    assert total % new_people == 0
    return total // new_people, {'total': total}


@kind
def simple_interest(principal, rate_pct, years):
    return Fr(principal * rate_pct * years, 100), {'per_year': Fr(principal * rate_pct, 100)}


@kind
def pie_sector(total, angle):
    assert total * angle % 360 == 0
    return total * angle // 360, {}


@kind
def twenty_four(h, ap, m, add_h, add_m):
    t = (_h24(h, ap) * 60 + m + add_h * 60 + add_m) % 1440
    return t // 60 * 100 + t % 60, {'start': _h24(h, ap) * 100 + m}


@kind
def minutes_seconds(songs):
    return sum(m * 60 + s for m, s in songs), {}


@kind
def fraction_order(fracs, ask):
    vals = sorted(fracs, key=lambda f: Fr(f[0], f[1]))
    f = vals[1] if ask == 'middle' else vals[-1] if ask == 'greatest' else vals[0]
    return Fr(f[0], f[1]), {}


@kind
def improper(whole, num, den):
    return whole * den + num, {}


@kind
def profit_pct(cost, sell):
    return Fr((sell - cost) * 100, cost), {'profit': sell - cost}
