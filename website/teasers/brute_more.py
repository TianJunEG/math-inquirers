"""INDEPENDENT checker side, part 2 (fix round 1).  Never imports kinds.py or kinds_more.py.

BRUTE[kind](**params) walks the whole search space and returns the SET of all answers that satisfy the puzzle;
verify_bank.py requires exactly one value equal to the bank's answer.  Merged into brute.BRUTE at the bottom of brute.py."""
import itertools
import re
from fractions import Fraction as Fr

BRUTE = {}


def brute(fn):
    BRUTE[fn.__name__[2:]] = fn
    return fn


# ================================================================== Level 1 structures
@brute
def b_doubling(start, times):
    n = start
    for _ in range(times):
        n = n + n
    return {n}


@brute
def b_bond_pairs(total, lo=1):
    seen = set()
    for a in range(0, total + 1):
        for b in range(0, total + 1):
            if a + b == total and a >= lo and b >= lo:
                seen.add(frozenset((a, b)))
    return {len(seen)}


@brute
def b_scaled_diff(scale, a, b):
    row_a = ['*'] * a
    row_b = ['*'] * b
    return {len(row_a) * scale - len(row_b) * scale}


@brute
def b_fewest_coins(target, coins):
    best = None
    ranges = [range(target // c + 1) for c in coins]
    for combo in itertools.product(*ranges):
        if sum(n * c for n, c in zip(combo, coins)) == target:
            k = sum(combo)
            if best is None or k < best:
                best = k
    return {best}


@brute
def b_count_between(lo, hi, inclusive):
    days = [d for d in range(lo - 5, hi + 6) if (lo <= d <= hi if inclusive else lo < d < hi)]
    return {len(days)}


@brute
def b_growing_gaps(first, gap0, n):
    seq, x = [], first
    for i in range(n):
        seq.append(x)
        x += gap0 + i
    return {seq[-1]}


@brute
def b_span(a, b):
    return {sum(1 for _ in range(a, b))}


@brute
def b_match_assign(people, things, clues, ask_thing=None, ask_person=None, verb='has the'):
    out = set()
    count = 0
    for perm in itertools.permutations(range(len(things))):
        ok = True
        for p, t, truth in clues:
            mine = things[perm[people.index(p)]]
            if truth and mine != t:
                ok = False
            if (not truth) and mine == t:
                ok = False
        if ok:
            count += 1
            if ask_thing:
                out.add(people[[perm[i] for i in range(len(people))].index(things.index(ask_thing))])
            else:
                out.add(things[perm[people.index(ask_person)]])
    return out if count == 1 else (out | {'#%d solutions' % count})


@brute
def b_turns(start, moves):
    vec = {'north': (0, 1), 'east': (1, 0), 'south': (0, -1), 'west': (-1, 0)}
    name = {v: k for k, v in vec.items()}
    d = vec[start]
    for m in moves:
        x, y = d
        if m == 'R':
            d = (y, -x)
        elif m == 'L':
            d = (-y, x)
        else:
            d = (-x, -y)
    return {name[d]}


@brute
def b_filter_count(numbers, conds):
    tests = {'even': 'n % 2 == 0', 'odd': 'n % 2 == 1', 'gt': 'n > {0}', 'lt': 'n < {0}', 'multiple': 'n % {0} == 0'}
    cnt = 0
    for n in numbers:
        good = True
        for c in conds:
            expr = tests[c[0]].format(*c[1:])
            if not eval(expr, {'n': n}):
                good = False
        cnt += good
    return {cnt}


@brute
def b_venn_both(total, a, b, neither=0):
    out = set()
    for both in range(0, min(a, b) + 1):
        only_a, only_b = a - both, b - both
        if only_a + only_b + both + neither == total:
            out.add(both)
    return out


@brute
def b_parity(op, parts):
    results = set()
    pools = [[1, 3, 5, 7, 9, 11] if p == 'odd' else [2, 4, 6, 8, 10] for p in parts]
    for combo in itertools.product(*pools):
        v = sum(combo) if op == 'sum' else eval('*'.join(str(c) for c in combo))
        results.add('odd' if v % 2 else 'even')
    return results


@brute
def b_regroup(tens, ones, hundreds=0, thousands=0):
    total = 0
    for _ in range(thousands):
        total += 1000
    for _ in range(hundreds):
        total += 100
    for _ in range(tens):
        total += 10
    for _ in range(ones):
        total += 1
    return {total}


@brute
def b_digit_value_diff(n, i, j):
    digits = [int(c) for c in str(n)]
    places = [10 ** k for k in range(len(digits) - 1, -1, -1)]
    return {digits[i] * places[i] - digits[j] * places[j]}


@brute
def b_pairs_with_sum(nums, target):
    cnt = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j and nums[i] + nums[j] == target:
                cnt += 1
    return {cnt}


@brute
def b_perm_count(n, k=None):
    k = n if k is None else k
    return {len(list(itertools.permutations(range(n), k)))}


@brute
def b_cards_sum(digits, shape, ask):
    totals = []
    n1 = shape[0]
    for a in range(10 ** (n1 - 1) if n1 > 1 else 0, 10 ** n1):
        for rest in itertools.product(*[range(10 ** (w - 1) if w > 1 else 0, 10 ** w) for w in shape[1:]]):
            nums = [a] + list(rest)
            used = sorted(''.join(str(x).zfill(w) for x, w in zip(nums, shape)))
            if used == sorted(str(d) for d in digits):
                totals.append(sum(nums))
    return {max(totals) if ask == 'max' else min(totals)}


@brute
def b_position_from_back(total, k):
    line = list(range(1, total + 1))
    return {len(line) - line.index(k)}


@brute
def b_pyramid(bottom, ask, top=None, hide=None):
    def build(row):
        while len(row) > 1:
            row = [row[i] + row[i + 1] for i in range(len(row) - 1)]
        return row[0]
    if ask == 'top':
        return {build(list(bottom))}
    out = set()
    for v in range(0, 500):
        row = list(bottom)
        row[hide] = v
        if build(row) == top:
            out.add(v)
    return out


@brute
def b_age_gap(a, gap, when):
    mine, other = a, a + gap
    while mine < when:
        mine += 1
        other += 1
    return {other}


@brute
def b_equal_sides(left, right):
    return {x for x in range(0, 400) if sum(left) == sum(right) + x}


@brute
def b_climb_slip(height, up, down):
    pos, day = 0, 0
    while True:
        day += 1
        pos += up
        if pos >= height:
            return {day}
        pos -= down


@brute
def b_equalise(a, b):
    return {g for g in range(0, a + 1) if a - g == b + g}


@brute
def b_missing_digit(eq):
    out = set()
    for d in '0123456789':
        s = eq.replace('?', d)
        s = re.sub(r'\d+', lambda m: str(int(m.group(0))), s)
        left, right = s.split('=')
        if Fr(eval(left.replace('x', '*'))) == Fr(eval(right.replace('x', '*'))):
            out.add(int(d))
    return out


# ================================================================== Level 2 structures
@brute
def b_unit_price(buy, cost, want):
    prices = [Fr(x, 100) for x in range(0, 20000) if Fr(x, 100) * buy == Fr(cost, 100)]
    prices_c = [p for p in prices]
    return {p * want for p in prices_c} if prices_c else set()


@brute
def b_time_convert(h, m):
    t = 0
    for _ in range(h):
        for _ in range(60):
            t += 1
    return {t + m}


@brute
def b_solid_parts(shapes, part):
    def build(name):
        if name in ('cube', 'cuboid'):
            v = list(itertools.product((0, 1), repeat=3))
            e = [(a, b) for a, b in itertools.combinations(v, 2) if sum(x != y for x, y in zip(a, b)) == 1]
            f = len([1 for axis in range(3) for val in (0, 1)])
            return f, len(e), len(v)
        if name == 'square pyramid':
            base = [(0, 0), (1, 0), (1, 1), (0, 1)]
            v = base + ['apex']
            e = [(base[i], base[(i + 1) % 4]) for i in range(4)] + [(b, 'apex') for b in base]
            return 1 + 4, len(e), len(v)
        if name == 'triangular prism':
            tri = [0, 1, 2]
            v = [(t, z) for t in tri for z in (0, 1)]
            e = [e_ for e_ in itertools.combinations(v, 2) if (e_[0][0] != e_[1][0] and e_[0][1] == e_[1][1]) or (e_[0][0] == e_[1][0] and e_[0][1] != e_[1][1])]
            return 2 + 3, len(e), len(v)
        if name == 'triangular pyramid':
            v = range(4)
            e = list(itertools.combinations(v, 2))
            f = list(itertools.combinations(v, 3))
            return len(f), len(e), len(list(v))
        raise ValueError(name)
    idx = {'faces': 0, 'edges': 1, 'vertices': 2}[part]
    return {sum(build(s)[idx] for s in shapes)}


@brute
def b_unit_convert(factor, big, small):
    return {sum(1 for _ in range(big * factor)) + small}


@brute
def b_fraction_diff(n, f1, f2):
    def part(f):
        num, den = f
        items = list(range(n))
        groups = [items[i::den] for i in range(den)]
        assert all(len(g) == n // den for g in groups)
        return sum(len(g) for g in groups[:num])
    return {abs(part(f1) - part(f2))}


# ================================================================== Level 3 structures
@brute
def b_elapsed_overnight(h1, m1, h2, m2):
    t, n = h1 * 60 + m1, 0
    while True:
        t = (t + 1) % (24 * 60)
        n += 1
        if t == h2 * 60 + m2:
            return {n}


@brute
def b_times_as_many(k, ask, total=None, diff=None):
    out = set()
    for small in range(1, 3000):
        large = small + small + small * 0
        large = 0
        for _ in range(k):
            large += small
        ok = (small + large == total) if total is not None else (large - small == diff)
        if ok:
            out.add(small if ask == 'small' else large)
    return out


@brute
def b_equiv_fraction(n1, d1, d2):
    return {n2 for n2 in range(0, 1000) if n2 * d1 == n1 * d2}


@brute
def b_quarter_turns(a, b):
    pos, turned, hours = a, 0, 0
    while pos != b:
        pos = pos % 12 + 1
        hours += 1
        if hours % 3 == 0:
            turned += 1
    return {turned} if hours % 3 == 0 else set()


# ================================================================== Level 4 structures
@brute
def b_series_gap(values, ask):
    best = None
    for i in range(len(values) - 1):
        d = values[i + 1] - values[i]
        if ask == 'biggest_rise':
            best = d if best is None or d > best else best
        else:
            best = d if best is None or d < best else best
    return {abs(best)}
