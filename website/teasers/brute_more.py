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
def b_match_assign(people, things, clues, ask_thing=None, ask_person=None):
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
def b_regroup(tens, ones, hundreds=0):
    total = 0
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
