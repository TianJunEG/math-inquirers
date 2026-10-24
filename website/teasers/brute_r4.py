"""INDEPENDENT checker side, part 5 (fix round 6).  Never imports kinds.py, kinds_more.py, kinds_r2.py, kinds_r3.py or kinds_r4.py.

BRUTE[kind](**params) rebuilds the puzzle in its own way (coordinates and angles for the quadrilaterals, counting pieces for a shared whole,
every simple path of a map, Python's own expression evaluator for brackets, one item at a time for shops) and returns the SET of all answers
that satisfy it; verify_bank.py requires exactly one value equal to the bank's answer.  When the puzzle is not well posed (a tie, two
shortest routes) the checker returns two values or the impossible value BAD, so the verifier reports it as 'valid answers: 2'.
Merged into brute.BRUTE at the bottom of brute.py."""
import itertools
import math
from fractions import Fraction as Fr

BRUTE = {}
BAD = '#NOT-UNIQUE#'


def brute(fn):
    BRUTE[fn.__name__[2:]] = fn
    return fn


def _angle(p, q, r):
    """The angle at q between the rays q->p and q->r, in degrees."""
    ux, uy = p[0] - q[0], p[1] - q[1]
    vx, vy = r[0] - q[0], r[1] - q[1]
    return math.degrees(math.acos((ux * vx + uy * vy) / (math.hypot(ux, uy) * math.hypot(vx, vy))))


def _whole(x):
    r = round(x)
    return r if abs(x - r) < 1e-6 else None


@brute
def b_quad_angles(shape, a, ask, b=None):
    ra = math.radians(a)
    if shape == 'parallelogram':
        A, B = (0.0, 0.0), (2.0, 0.0)
        D = (1.3 * math.cos(ra), 1.3 * math.sin(ra))
        C = (B[0] + D[0], B[1] + D[1])
        angB, angC, angD = _angle(A, B, C), _angle(B, C, D), _angle(C, D, A)
        v = angB if ask == 'adjacent' else angB + angC + angD
    elif shape == 'rhombus':
        A, B = (0.0, 0.0), (1.0, 0.0)
        D = (math.cos(ra), math.sin(ra))
        C = (B[0] + D[0], B[1] + D[1])
        if ask == 'diag_side':
            v = _angle(C, A, B)                  # the long diagonal AC against the side AB
        else:
            v = _angle(A, B, D)                  # the short diagonal BD against the side BA
    elif shape == 'trapezium':
        A, B = (0.0, 0.0), (5.0, 0.0)
        D = (1.1 * math.cos(ra), 1.1 * math.sin(ra))
        if ask == 'D':
            C = (D[0] + 3.0, D[1])
            v = _angle(A, D, C)
        else:
            rb = math.radians(b)
            t = 1.1 * math.sin(ra) / math.sin(rb)
            C = (B[0] - t * math.cos(rb), t * math.sin(rb))
            assert abs(C[1] - D[1]) < 1e-9       # DC is parallel to AB
            v = _angle(A, D, C) + _angle(B, C, D)
    else:
        return {BAD}
    w = _whole(v)
    return {w} if w is not None else {BAD}


@brute
def b_frac_quotient(total, parts, ask, k=1):
    # share the wholes out piece by piece: cut every whole into `parts` equal pieces and deal them out one at a time
    got = [0] * parts
    for _ in range(total):
        for piece in range(parts):
            got[piece] += 1                      # one piece of size 1/parts for child `piece`
    one = Fr(got[0], parts)
    if ask in ('each', 'decimal'):
        if ask == 'decimal':
            rem, digits, guard = total % parts, 0, 0
            while rem and guard < 12:
                rem = rem * 10 % parts
                guard += 1
            if rem:
                return {BAD}
        return {one}
    return {one * k}


@brute
def b_rate_compare(items, ask):
    def faster(x, y):                            # x has the greater rate: compare amount / time without dividing
        return x[1] * y[2] > y[1] * x[2]
    best = [it for it in items if all(faster(it, o) for o in items if o is not it)]
    worst = [it for it in items if all(faster(o, it) for o in items if o is not it)]
    if ask == 'fastest':
        return {it[0] for it in best} if len(best) == 1 else {BAD}
    if ask == 'slowest':
        return {it[0] for it in worst} if len(worst) == 1 else {BAD}
    hi = max(items, key=lambda it: Fr(it[1], it[2]))
    lo = min(items, key=lambda it: Fr(it[1], it[2]))
    return {Fr(hi[1], hi[2]) - Fr(lo[1], lo[2])}


@brute
def b_bracket_values(nums, ops, ask, target=None):
    n = len(nums)
    sym = {'+': '+', '-': '-', 'x': '*'}
    results = []
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) == (0, n - 1):
                continue
            s = ''
            for k in range(n):
                s += ('(' if k == i else '') + str(nums[k]) + (')' if k == j else '')
                if k < n - 1:
                    s += sym[ops[k]]
            results.append(eval(s))              # Python's own precedence: * before + and -
    if ask == 'max':
        return {max(results)}
    if ask == 'values':
        return {len(set(results))}
    return {sum(1 for r in results if r == target)}


@brute
def b_right_triangle_height(a, b, c, ask):
    # corners (0,0), (a,0), (0,b); area by the shoelace formula; then area = 1/2 x longest side x height
    pts = [(0, 0), (a, 0), (0, b)]
    area = Fr(abs(sum(pts[i][0] * pts[(i + 1) % 3][1] - pts[(i + 1) % 3][0] * pts[i][1] for i in range(3))), 2)
    if math.dist(pts[1], pts[2]) != c:          # the longest side is the line from (a,0) to (0,b)
        return {BAD}
    return {2 * area / c}


@brute
def b_clock_span(start, end, less=0):
    # run the clock on one minute at a time from the start time until the end time is shown
    def clock(t):
        h = t[0]
        if t[2] == 'am':
            h = 0 if h == 12 else h
        else:
            h = 12 if h == 12 else h + 12
        return h * 60 + t[1]
    now, goal, count = clock(start), clock(end), 0
    while now != goal:
        now = (now + 1) % 1440
        count += 1
    return {count - less} if count - less > 0 else {BAD}


@brute
def b_halfway_end(a, mid):
    found = {x for x in range(0, 4 * mid + 1) if x != a and Fr(a + x, 2) == mid}
    return found or {BAD}


@brute
def b_table_who(names, vals, ask):
    rows = sorted(zip(vals, names), reverse=True)
    if len(set(vals)) != len(vals):
        return {BAD}
    rank = {'most': 0, 'second': 1, 'least': len(rows) - 1}[ask]
    return {rows[rank][1]}


@brute
def b_shop_choice(offers, want, ask):
    totals = []
    for o in offers:
        bought = paid = 0
        if o[0] == 'each':
            while bought < want:
                bought += 1
                paid += o[1]
        elif o[0] == 'pack':
            while bought < want:
                bought += o[1]
                paid += o[2]
        else:
            buy, get, price = o[1], o[2], o[3]
            while bought < want:
                for _ in range(buy):
                    bought += 1
                    paid += price
                bought += get                    # the free ones
        totals.append((paid, bought))
    if any(b != want for _, b in totals):
        return {BAD}
    pick = min(t for t, _ in totals) if ask == 'cheapest' else max(t for t, _ in totals)
    return {'Shop ' + 'ABCDEFG'[i] for i, (t, _) in enumerate(totals) if t == pick}


@brute
def b_gift_who(names, start, steps, ask):
    purse = {names[0]: start[0], names[1]: start[1]}
    for s in steps:
        if s[0] == 'give':
            purse[names[s[1]]] -= s[3]
            purse[names[s[2]]] += s[3]
        elif s[0] == 'spend':
            purse[names[s[1]]] -= s[2]
        else:
            purse[names[s[1]]] += s[2]
    if min(purse.values()) < 0 or purse[names[0]] == purse[names[1]]:
        return {BAD}
    top = max(purse.values())
    return {n for n, v in purse.items() if (v == top) == (ask == 'more')}


@brute
def b_route_via(edges, start, end, ask):
    adj = {}
    for u, v, w in edges:
        adj.setdefault(u, []).append((v, w))
        adj.setdefault(v, []).append((u, w))
    routes = []

    def walk(at, seen, length, path):
        if at == end:
            routes.append((length, list(path)))
            return
        for nxt, w in adj[at]:
            if nxt not in seen:
                seen.add(nxt)
                path.append(nxt)
                walk(nxt, seen, length + w, path)
                path.pop()
                seen.discard(nxt)
    walk(start, {start}, 0, [start])
    best = min(l for l, _ in routes)
    paths = [p for l, p in routes if l == best]
    if len(paths) != 1 or len(paths[0]) < 3:
        return {BAD}
    return {paths[0][1] if ask == 'first' else paths[0][-2]}


@brute
def b_classify_triangle(mode, vals, options):
    if mode == 'sides':
        a, b, c = vals
        if not (a + b > c and a + c > b and b + c > a):
            return {BAD}
        same = sum(1 for x, y in itertools.combinations(vals, 2) if x == y)
        word = {3: 'equilateral', 1: 'isosceles', 0: 'scalene'}[same]
    else:
        # build the triangle from its angles (law of sines) and look at the corners
        third = 180 - sum(vals)
        if third <= 0:
            return {BAD}
        angs = list(vals) + [third]
        sides = [math.sin(math.radians(x)) for x in angs]
        A = (0.0, 0.0)
        B = (sides[2], 0.0)
        C = (sides[1] * math.cos(math.radians(angs[0])), sides[1] * math.sin(math.radians(angs[0])))
        corners = [_angle(B, A, C), _angle(A, B, C), _angle(A, C, B)]
        if mode == 'angles2':
            if any(abs(c - 90) < 1e-7 for c in corners):
                word = 'right-angled'
            elif any(c > 90 + 1e-7 for c in corners):
                word = 'obtuse'
            else:
                word = 'acute'
        else:
            lens = [math.dist(A, B), math.dist(B, C), math.dist(C, A)]
            same = sum(1 for x, y in itertools.combinations(lens, 2) if abs(x - y) < 1e-9)
            word = {3: 'equilateral', 1: 'isosceles', 0: 'scalene'}[same]
    return {word} if word in options else {BAD}


@brute
def b_unit_heavier(items, ratio, ask):
    # write every amount in big units as a decimal fraction and compare
    def big(f):
        if f[0] == 'mix':
            return Fr(f[1]) + Fr(f[2], ratio)
        if f[0] == 'dec':
            return Fr(str(f[1]))
        return Fr(f[1], ratio)
    vals = [(big(it[1:]), it[0]) for it in items]
    if len({v for v, _ in vals}) != len(vals):
        return {BAD}
    pick = max(v for v, _ in vals) if ask == 'heaviest' else min(v for v, _ in vals)
    return {lab for v, lab in vals if v == pick}
