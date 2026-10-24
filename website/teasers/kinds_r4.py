"""GENERATOR side, part 5 (fix round 6): solvers for the NEW sub-structures of round 6 (taxonomy.json, ids marked "round": 6).

Two groups.  (1) Five new Level 5 sub-structures (AUDIT_ROUND6 M1: Level 5 had a slack of 2): unknown angles in a parallelogram, rhombus and
trapezium; a whole number divided by a whole number as a fraction or decimal; comparing rates; where to put one pair of brackets; the
height of a right-angled triangle on its longest side.  (2) Six TEXT-ANSWER asks (AUDIT_ROUND6 G4, TEXT_ANSWER_PLAN.md section 3): who has
the most in a table, which shop is cheaper, who has more after gifts and spending, which place is first on the shortest route, what kind of
triangle it is, which of several amounts in mixed units is the heaviest.

Same contract as kinds.py: SOLVE[kind](**params) -> (answer, ctx).  The independent checkers are in brute_r4.py (which never imports this
file); samples_r4.py lists worked instances and `verify_bank.py --selftest` proves solver and checker agree on each, even for
sub-structures that no month uses yet."""
from fractions import Fraction as Fr

SOLVE = {}


def kind(fn):
    SOLVE[fn.__name__] = fn
    return fn


# ================================================================== (1) new Level 5 sub-structures
@kind
def quad_angles(shape, a, ask, b=None):
    """Unknown angles in a parallelogram ABCD, a rhombus ABCD or a trapezium ABCD (AB parallel to DC); `a` is the angle at A (and `b` the angle at B)."""
    if shape == 'parallelogram' and ask == 'adjacent':
        return 180 - a, {'rest': 180 - a}
    if shape == 'parallelogram' and ask == 'three':
        return 360 - a, {'whole': 360}
    if shape == 'rhombus' and ask == 'diag_side':
        assert a % 2 == 0
        return a // 2, {'half': a // 2}
    if shape == 'rhombus' and ask == 'tri_base':
        assert (180 - a) % 2 == 0
        return (180 - a) // 2, {'left': 180 - a}
    if shape == 'trapezium' and ask == 'D':
        return 180 - a, {'rest': 180 - a}
    if shape == 'trapezium' and ask == 'cd_sum':
        return 360 - a - b, {'dd': 180 - a, 'cc': 180 - b}
    raise ValueError((shape, ask))


@kind
def frac_quotient(total, parts, ask, k=1):
    """total wholes shared equally between `parts`: one share as a fraction (each), k shares together (k_shares), or one share as a decimal (decimal)."""
    one = Fr(total, parts)
    if ask == 'each':
        return one, {'frac': '%d/%d' % (total, parts)}
    if ask == 'k_shares':
        return one * k, {'frac': '%d/%d' % (total, parts)}
    if ask == 'decimal':
        d = parts
        for p in (2, 5):
            while d % p == 0:
                d //= p
        assert d == 1, 'not a terminating decimal'
        return one, {'frac': '%d/%d' % (total, parts)}
    raise ValueError(ask)


@kind
def rate_compare(items, ask):
    """items = [[name, amount, time], ...]: the rate of each is amount / time.  Ask fastest or slowest (a name) or gap (fastest minus slowest, a number)."""
    rates = [(Fr(a, t), n) for n, a, t in items]
    rs = sorted(rates)
    if ask == 'fastest':
        assert rs[-1][0] != rs[-2][0]
        return rs[-1][1], {'rates': ', '.join('%s %s' % (n, r) for r, n in rates)}
    if ask == 'slowest':
        assert rs[0][0] != rs[1][0]
        return rs[0][1], {'rates': ', '.join('%s %s' % (n, r) for r, n in rates)}
    if ask == 'gap':
        return rs[-1][0] - rs[0][0], {'hi': rs[-1][0], 'lo': rs[0][0]}
    raise ValueError(ask)


def _eval_expr(tokens):
    """tokens = [n, op, n, op, n ...] with '(' and ')' tokens; recursive descent, x binds tighter than + and -."""
    pos = [0]

    def atom():
        t = tokens[pos[0]]
        if t == '(':
            pos[0] += 1
            v = expr()
            pos[0] += 1                  # the ')'
            return v
        pos[0] += 1
        return t

    def term():
        v = atom()
        while pos[0] < len(tokens) and tokens[pos[0]] == 'x':
            pos[0] += 1
            v = v * atom()
        return v

    def expr():
        v = term()
        while pos[0] < len(tokens) and tokens[pos[0]] in ('+', '-'):
            op = tokens[pos[0]]
            pos[0] += 1
            w = term()
            v = v + w if op == '+' else v - w
        return v
    return expr()


@kind
def bracket_values(nums, ops, ask, target=None):
    """One pair of brackets round two or more neighbouring numbers (never the whole expression): the greatest value (max), the number of different
    values (values), or the number of placements that give `target` (ways)."""
    n = len(nums)
    vals = []
    for i in range(n):
        for j in range(i + 1, n):
            if i == 0 and j == n - 1:
                continue
            toks = []
            for k in range(n):
                if k == i:
                    toks.append('(')
                toks.append(nums[k])
                if k == j:
                    toks.append(')')
                if k < n - 1:
                    toks.append(ops[k])
            vals.append(_eval_expr(toks))
    plain = _eval_expr([x for k in range(n) for x in ([nums[k]] + ([ops[k]] if k < n - 1 else []))])
    ctx = {'plain': plain, 'count': len(vals)}
    if ask == 'max':
        return max(vals), ctx
    if ask == 'values':
        return len(set(vals)), ctx
    if ask == 'ways':
        return sum(1 for v in vals if v == target), ctx
    raise ValueError(ask)


@kind
def right_triangle_height(a, b, c, ask):
    """Right-angled triangle with legs a and b and longest side c (a, b, c a Pythagorean triple).  The height on the longest side, from the area:
    area = a x b / 2 = c x height / 2."""
    assert ask == 'height' and a * a + b * b == c * c
    return Fr(a * b, c), {'area': Fr(a * b, 2), 'twice': a * b}


@kind
def clock_span(start, end, less=0):
    """Minutes from start to end on a 12-hour clock ([hour, minute, 'am' or 'pm'], the end is the next time it is reached), less the minutes of a break."""
    def mins(t):
        return ((t[0] % 12) + (12 if t[2] == 'pm' else 0)) * 60 + t[1]
    span = (mins(end) - mins(start)) % 1440
    assert 0 < span - less
    return span - less, {'span': span, 'sh': span // 60, 'sm': span % 60}


@kind
def halfway_end(a, mid):
    """The point `mid` is exactly halfway between a and an unknown point b (b is on the far side of mid): find b."""
    assert mid > a
    return 2 * mid - a, {'gap': mid - a, 'twice': 2 * mid}


# ================================================================== (2) text-answer asks
@kind
def table_who(names, vals, ask):
    """A table of named children: who has the most (most), the least (least) or the second most (second)."""
    order = sorted(zip(vals, names))
    assert len(set(vals)) == len(vals)
    if ask == 'most':
        return order[-1][1], {'val': order[-1][0]}
    if ask == 'least':
        return order[0][1], {'val': order[0][0]}
    if ask == 'second':
        return order[-2][1], {'val': order[-2][0]}
    raise ValueError(ask)


@kind
def shop_choice(offers, want, ask):
    """Shops A, B, C ... each with an offer ['each', price] / ['pack', n, price] / ['free', buy, get, price]; which shop is cheapest (cheapest) or dearest."""
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
        else:
            raise ValueError(o)
    best = min(costs) if ask == 'cheapest' else max(costs)
    assert costs.count(best) == 1
    return 'Shop ' + 'ABCDEFG'[costs.index(best)], {'costs': ', '.join(str(c) for c in costs)}


@kind
def gift_who(names, start, steps, ask):
    """Two children with start amounts; steps ['give', i, j, k] (i gives k to j), ['spend', i, k], ['earn', i, k]; who has more (more) or less (less) at the end."""
    now = list(start)
    for s in steps:
        if s[0] == 'give':
            now[s[1]] -= s[3]
            now[s[2]] += s[3]
        elif s[0] == 'spend':
            now[s[1]] -= s[2]
        elif s[0] == 'earn':
            now[s[1]] += s[2]
        else:
            raise ValueError(s)
    assert now[0] != now[1] and min(now) >= 0
    hi = 0 if now[0] > now[1] else 1
    who = hi if ask == 'more' else 1 - hi
    return names[who], {'end': '%d and %d' % tuple(now), 'gap': abs(now[0] - now[1])}


@kind
def route_via(edges, start, end, ask):
    """Shortest route on a map of roads [[u, v, length], ...] (the shortest route is unique): the first place after the start (first) or the last place before the end (last)."""
    import heapq
    adj = {}
    for u, v, w in edges:
        adj.setdefault(u, []).append((v, w))
        adj.setdefault(v, []).append((u, w))
    dist, prev, ways = {start: 0}, {}, {start: 1}
    pq = [(0, start)]
    done = set()
    while pq:
        d, u = heapq.heappop(pq)
        if u in done:
            continue
        done.add(u)
        for v, w in adj[u]:
            nd = d + w
            if v not in dist or nd < dist[v]:
                dist[v], prev[v], ways[v] = nd, u, ways[u]
                heapq.heappush(pq, (nd, v))
            elif nd == dist[v]:
                ways[v] += ways[u]
    assert ways[end] == 1, 'the shortest route is not unique'
    path = [end]
    while path[-1] != start:
        path.append(prev[path[-1]])
    path.reverse()
    assert len(path) >= 3
    return (path[1] if ask == 'first' else path[-2]), {'dist': dist[end], 'path': ' to '.join(path)}


@kind
def classify_triangle(mode, vals, options):
    """What kind of triangle?  mode sides: vals = three sides -> equilateral / isosceles / scalene.  mode angles2: vals = two angles -> acute / right-angled / obtuse.
    mode isoangles: vals = two angles -> equilateral / isosceles / scalene (by the angles)."""
    if mode == 'sides':
        a, b, c = sorted(vals)
        assert a + b > c
        word = 'equilateral' if a == c else ('isosceles' if a == b or b == c else 'scalene')
    elif mode == 'angles2':
        t = 180 - sum(vals)
        assert t > 0
        angs = list(vals) + [t]
        word = 'right-angled' if 90 in angs else ('obtuse' if max(angs) > 90 else 'acute')
    elif mode == 'isoangles':
        t = 180 - sum(vals)
        assert t > 0
        angs = list(vals) + [t]
        word = 'equilateral' if len(set(angs)) == 1 else ('isosceles' if len(set(angs)) == 2 else 'scalene')
    else:
        raise ValueError(mode)
    assert word in options
    return word, {'word': word}


@kind
def unit_heavier(items, ratio, ask):
    """Amounts written in different ways: ['mix', big, small] (3 kg 250 g), ['dec', 3.25] (in the big unit), ['small', 3250]; `ratio` small units make 1 big unit.
    ask heaviest or lightest (any quantity: longest, most ...).  Returns the label."""
    tot = []
    for lab, *f in items:
        if f[0] == 'mix':
            v = Fr(f[1] * ratio + f[2])
        elif f[0] == 'dec':
            v = Fr(str(f[1])) * ratio
        else:
            v = Fr(f[1])
        tot.append((v, lab))
    s = sorted(tot)
    assert len({v for v, _ in tot}) == len(tot)
    return (s[-1][1] if ask == 'heaviest' else s[0][1]), {'order': ', '.join('%s %s' % (l, v) for v, l in s)}
