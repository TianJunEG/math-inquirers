"""INDEPENDENT checker side of the daily-teaser puzzles.  Never imports kinds.py.

BRUTE[kind](**params) walks the WHOLE search space (every candidate answer, every arrangement, every
step of a simulation) and returns the SET of all answers that satisfy the puzzle.  verify_bank.py
requires that set to hold exactly one value and that value to equal the bank's answer.
"""
import itertools
from collections import Counter
from decimal import Decimal
from fractions import Fraction as Fr

DAYNAMES = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def b_seq_term(a, d, n):
    x = a
    for _ in range(n - 1):
        x += d
    return {x}


def b_dot(pairs):
    t = 0
    for c, e in pairs:
        for _ in range(c):
            t += e
    return {t}


def b_seq_pos(a, d, v):
    out, x, n = set(), a, 1
    while n < 10000:
        if x == v:
            out.add(n)
        x += d
        n += 1
    return out


def b_groups_plus(g, s, r=0):
    t = r
    for _ in range(g):
        t += s
    return {t}


def b_part_whole(total, parts):
    return {x for x in range(0, total + 1) if sum(parts) + x == total}


def b_chain(base, steps, ask):
    seq = [base]
    for sgn, m in steps:
        if sgn == '+':
            seq.append(seq[-1] + m)
        elif sgn == '-':
            seq.append(seq[-1] - m)
        else:
            seq.append(seq[-1] * m)
    if ask == 'sum':
        t = 0
        for v in seq:
            t += v
        return {t}
    if ask == 'last':
        return {seq[len(seq) - 1]}
    return {max(seq) - min(seq)}


def b_sum_diff(S, D, ask):
    out = set()
    for a in range(0, S + 1):
        b = S - a
        if a - b == D:
            out.add(a if ask == 'larger' else b)
    return out


def b_sum_range(lo, hi, step=1):
    return {sum(range(lo, hi + 1, step))}


def b_queue(front, back):
    return {N for N in range(1, 400) if front <= N and back <= N and N - back + 1 == front}


def b_fence(length, gap, closed=False):
    pos = list(range(0, length, gap)) if closed else list(range(0, length + 1, gap))
    return {len(pos)}


def b_combos(counts):
    return {len(list(itertools.product(*[range(c) for c in counts])))}


def b_pairs(n):
    return {len(list(itertools.combinations(range(n), 2)))}


def _factors(n):
    return [k for k in range(1, n + 1) if n % k == 0]


def _is_prime(n):
    return n >= 2 and len([k for k in range(1, n + 1) if n % k == 0]) == 2


def _spred(name, arg, n):
    s = str(n)
    ds = [int(c) for c in s]
    if name == 'same_digits':
        return s == s[0] * len(s)
    if name == 'digit_sum':
        return sum(ds) == arg
    if name == 'contains':
        return str(arg) in s
    if name == 'even':
        return s[-1] in '02468'
    if name == 'multiple':
        return n // arg * arg == n
    if name == 'ends_in':
        return int(s[-1]) in arg
    if name == 'distinct':
        return len(set(s)) == len(s)
    if name == 'first_odd':
        return s[0] in '13579'
    if name == 'digit_product':
        p = 1
        for d in ds:
            p *= d
        return p == arg
    if name == 'increasing':
        return all(s[i] < s[i + 1] for i in range(len(s) - 1))
    if name == 'factor_count':
        return len(_factors(n)) == arg
    if name == 'prime':
        return _is_prime(n)
    if name == 'square':
        return any(k * k == n for k in range(0, n + 1))
    if name == 'palindrome':
        return s == s[::-1]
    if name == 'digit_eq':
        return int(s[arg[0]]) == arg[1]
    if name == 'digit_plus':
        return int(s[arg[0]]) == int(s[arg[1]]) + arg[2]
    if name == 'digit_times':
        return int(s[arg[0]]) == arg[2] * int(s[arg[1]])
    if name == 'digit_less':
        return s[arg[0]] < s[arg[1]]
    raise ValueError(name)


def b_scan(lo, hi, preds, ask):
    hits = [n for n in range(lo, hi + 1) if all(_spred(p, a, n) for p, a in preds)]
    if ask == 'count':
        return {len(hits)}
    if ask == 'only':
        return set(hits)
    return {min(hits) if ask == 'min' else max(hits)}


def _uses(n, digits, ndig):
    s = str(n)
    if len(s) != ndig:
        return False
    need, have = Counter(s), Counter(str(d) for d in digits)
    return all(need[c] <= have[c] for c in need)


def b_digits_extreme(digits, ndig, ask):
    lo = 1 if ndig == 1 else 10 ** (ndig - 1)
    pool = [n for n in range(lo, 10 ** ndig) if _uses(n, digits, ndig)]
    if ask in ('largest', 'smallest'):
        return {max(pool) if ask == 'largest' else min(pool)}
    ev = [n for n in pool if str(n)[-1] in '02468']
    od = [n for n in pool if str(n)[-1] in '13579']
    pick = {'smallest_even': (min, ev), 'largest_even': (max, ev), 'largest_odd': (max, od), 'smallest_odd': (min, od)}[ask]
    return {pick[0](pick[1])} if pick[1] else set()


def b_count_arrangements(digits, ndig, cond):
    lo = 10 ** (ndig - 1)
    pool = [n for n in range(lo, 10 ** ndig) if _uses(n, digits, ndig)]
    if cond == 'even':
        pool = [n for n in pool if str(n)[-1] in '02468']
    elif cond == 'odd':
        pool = [n for n in pool if str(n)[-1] in '13579']
    return {len(pool)}


def b_clock_end_hour(h, add):
    cur = h
    for _ in range(add):
        cur = 1 if cur == 12 else cur + 1
    return {cur}


def b_elapsed(h1, m1, h2, m2):
    t, n = h1 * 60 + m1, 0
    while t != h2 * 60 + m2:
        t += 1
        n += 1
    return {n}


def b_weekday(start, days):
    i = DAYNAMES.index(start)
    for _ in range(days):
        i = (i + 1) % 7
    return {DAYNAMES[i]}


def b_share(total, k, ask):
    if ask in ('each', 'left'):
        piles = [0] * k
        for i in range(total):
            piles[i % k] += 1
        if ask == 'each':
            return {piles[0]} if len(set(piles)) == 1 else set()
        return {sum(1 for p in piles if p > min(piles))}
    boxes, left = 0, total
    while left > 0:
        left -= k
        boxes += 1
    if ask == 'groups' and left != 0:
        return set()
    return {boxes}


def b_perimeter_regular(n, side):
    d = 0
    for _ in range(n):
        d += side
    return {d}


def b_rect(ask, l=None, w=None, P=None, A=None):
    if ask == 'perimeter':
        return {l + w + l + w}
    if ask == 'area':
        return {len([(x, y) for x in range(l) for y in range(w)])}
    if ask == 'width_from_perimeter':
        return {x for x in range(1, P) if 2 * l + 2 * x == P}
    if ask == 'width_from_area':
        return {x for x in range(1, A + 1) if l * x == A}
    if ask == 'square_perimeter_from_area':
        return {4 * s for s in range(1, A + 1) if s * s == A}
    if ask == 'square_area_from_perimeter':
        return {s * s for s in range(1, P) if 4 * s == P}
    raise ValueError(ask)


def b_cells(outer, cuts, ask):
    W, H = outer
    grid = {(x, y) for x in range(W) for y in range(H)}
    for (cx, cy, cw, ch) in cuts:
        grid -= {(x, y) for x in range(cx, cx + cw) for y in range(cy, cy + ch)}
    if ask == 'area':
        return {len(grid)}
    edges = 0
    for (x, y) in grid:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if (x + dx, y + dy) not in grid:
                edges += 1
    return {edges}


def b_equiv_chain(rates, n):
    units = n
    for r in rates:
        units = sum(units for _ in range(r))
    return {units}


def b_shopping(items, pay, ask):
    total = 0
    for c, q in items:
        for _ in range(q):
            total += c
    return {Fr(total, 100)} if ask == 'total' else {Fr(pay - total, 100)}


def b_mystery(ops, result):
    out = set()
    for x in range(0, 6000):
        v = Fr(x)
        for op, m in ops:
            v = v + m if op == '+' else v - m if op == '-' else v * m if op == '*' else v / m
        if v == result:
            out.add(x)
    return out


def b_order_logic(order, facts, idx, rel):
    out = set()
    for perm in itertools.permutations(order):
        pos = {n: i for i, n in enumerate(perm)}   # index 0 = first / tallest
        if all(pos[a] < pos[b] for a, b in facts):
            out.add(perm[idx])
    return out


def b_moves(start, mv, ask):
    pos, seen = start, [start]
    for m in mv:
        step = 1 if m > 0 else -1
        for _ in range(abs(m)):
            pos += step
            seen.append(pos)
    return {pos if ask == 'final' else max(seen) if ask == 'max' else min(seen)}


def b_coin_ways(target, coins):
    ranges = [range(target // c + 1) for c in coins]
    return {sum(1 for combo in itertools.product(*ranges) if sum(n * c for n, c in zip(combo, coins)) == target)}


def b_repeat_pattern(unit, n, ask, item=None):
    seq = []
    while len(seq) < n:
        seq.extend(unit)
    seq = seq[:n]
    return {seq[-1]} if ask == 'at' else {seq.count(item)}


def b_stairs(n, steps):
    def walk(left):
        if left == 0:
            return [()]
        out = []
        for s in steps:
            if s <= left:
                out += [(s,) + rest for rest in walk(left - s)]
        return out
    return {len(walk(n))}


def b_grid_count(m, n, what):
    cnt = 0
    if what == 'squares':
        for s in range(1, min(m, n) + 1):
            for x in range(0, n - s + 1):
                for y in range(0, m - s + 1):
                    cnt += 1
        return {cnt}
    for x1 in range(n + 1):
        for x2 in range(x1 + 1, n + 1):
            for y1 in range(m + 1):
                for y2 in range(y1 + 1, m + 1):
                    cnt += 1
    return {cnt}


def b_lattice(right, down, blocked):
    blocked = {tuple(b) for b in blocked}
    total = 0
    n = right + down
    for rpos in itertools.combinations(range(n), right):
        x = y = 0
        ok = True
        for i in range(n):
            if i in rpos:
                x += 1
            else:
                y += 1
            if (x, y) in blocked:
                ok = False
                break
        total += ok
    return {total}


def b_matchsticks(shape, n, r=None, c=None):
    edges = set()
    if shape == 'sq':
        for i in range(n):
            a, b, cc, d = (i, 0), (i + 1, 0), (i, 1), (i + 1, 1)
            edges |= {frozenset(p) for p in ((a, b), (cc, d), (a, cc), (b, d))}
    elif shape == 'tri':
        zig = [(k // 2, k % 2) for k in range(n + 2)]   # vertices bottom, top, bottom, top ...
        for i in range(n):
            u, v, w = zig[i], zig[i + 1], zig[i + 2]
            edges |= {frozenset((u, v)), frozenset((v, w)), frozenset((u, w))}
    else:
        for i in range(c):
            for j in range(r):
                a, b, cc, d = (i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)
                edges |= {frozenset(p) for p in ((a, b), (cc, d), (a, cc), (b, d))}
    return {len(edges)}


def b_age_times(child, parent, k):
    return {t for t in range(1, 200) if parent + t == k * (child + t)}


def b_fraction_of(n, num, den):
    groups = [list(range(i, n, den)) for i in range(den)]
    assert all(len(g) == len(groups[0]) for g in groups)
    return {sum(len(groups[i]) for i in range(num))}


def b_fraction_seq(start, steps, ask):
    left, given = start, 0
    for num, den, base in steps:
        pool = start if base == 'whole' else left
        assert (pool * num) % den == 0
        cut = pool * num // den
        given += cut
        left -= cut
    return {left if ask == 'left' else given}


def b_fraction_whole(left, num, den):
    return {w for w in range(1, 5000) if w - w * num // den == left and (w * num) % den == 0}


def _fr_mixed(t):
    whole, n, d = t
    return (whole * d + n, d)


def b_frac_arith(op, a, b):
    (n1, d1), (n2, d2) = _fr_mixed(a), _fr_mixed(b)
    D = d1 * d2
    x, y = n1 * d2, n2 * d1
    if op == '+':
        return {Fr(x + y, D)}
    if op == '-':
        return {Fr(x - y, D)}
    if op == '/':
        return {Fr(n1 * d2, d1 * n2)}
    return {Fr(n1 * n2, d1 * d2)}


def b_decimals(op, a, b):
    A, B = Decimal(a), Decimal(b)
    v = A + B if op == '+' else A - B if op == '-' else A * B if op == '*' else A / B
    return {Fr(str(v))}


def b_pct(kind, **k):
    if kind == 'of':
        return {Fr(str(Decimal(k['n']) * Decimal(k['p']) / Decimal(100)))}
    if kind == 'whole':
        return {Fr(w) for w in range(1, 10000) if w * k['p'] == k['part'] * 100}
    if kind == 'discount':
        price = Fr(k['price'])
        for _ in range(1):
            pay = sum(price / 100 for _ in range(100 - k['p']))
        return {pay if k['ask'] == 'pay' else price - pay}
    if kind == 'then':
        v = Fr(100)
        for s in k['steps']:
            v = v + v * s / 100
        return {v}
    raise ValueError(kind)


def b_pct_rest(n, ps):
    out = set()
    for x in range(0, n + 1):
        if all(True for _ in ps) and x * 100 == n * (100 - sum(ps)):
            out.add(x)
    return out


def b_ratio(kind, **k):
    if kind == 'share':
        a, b, N = k['a'], k['b'], k['N']
        out = set()
        for u in range(1, N + 1):
            if a * u + b * u == N:
                out.add({'larger': max(a, b) * u, 'smaller': min(a, b) * u, 'diff': abs(a - b) * u}[k['ask']])
        return out
    if kind == 'whole':
        a, b, known = k['a'], k['b'], k['known']
        return {(a + b) * u for u in range(1, 5000) if a * u == known}
    if kind == 'transfer_equal':
        a, b, give = k['a'], k['b'], k['give']
        return {(a + b) * u for u in range(1, 5000) if a * u - give == b * u + give}
    if kind == 'add_equal':
        a, b, add = k['a'], k['b'], k['add']
        out = set()
        for u in range(1, 5000):
            if a * u + add == b * u:
                out.add({'b': b * u, 'a': a * u, 'total': (a + b) * u}[k['ask']])
        return out
    raise ValueError(kind)


def b_stats(data, ask):
    import statistics
    if ask == 'mean':
        return {Fr(sum(data), len(data))}
    if ask == 'median':
        return {Fr(statistics.median(data)).limit_denominator(1000)}
    if ask == 'mode':
        return set(statistics.multimode(data))
    if ask == 'range':
        return {max(data) - min(data)}
    return {sum(data)}


def b_mean_missing(data, target):
    return {x for x in range(0, 1001) if Fr(sum(data) + x, len(data) + 1) == target}


def b_mean_remove(n, mean_all, mean_rest):
    return {x for x in range(0, 2001) if (n * mean_all - x) == (n - 1) * mean_rest}


def b_meet(d, v1, v2):
    t = 0
    a, b = 0, d
    while a < b:
        a += v1
        b -= v2
        t += 1
    return {t} if a == b else set()


def b_fill(cap, rin, rout):
    level, t = 0, 0
    while level < cap:
        level += rin - rout
        t += 1
    return {t} if level == cap else set()


def b_avg_speed(v1, v2):
    d = v1 * v2 * 7          # any common distance works
    time = Fr(d, v1) + Fr(d, v2)
    return {Fr(2 * d) / time}


def b_speed(d, h, m):
    return {Fr(v) for v in range(1, 2000) if v * (h * 60 + m) == d * 60}


def b_volume(l, w, h):
    return {sum(1 for _ in itertools.product(range(l), range(w), range(h)))}


def b_water_rise(l, w, litres):
    out = set()
    for h2 in range(1, 4000):       # candidate heights in half centimetres
        if l * w * Fr(h2, 2) == litres * 1000:
            out.add(Fr(h2, 2))
    return out


def b_tri_area(ask, b=None, h=None, A=None):
    if ask == 'area':
        return {Fr(sum(1 for _ in range(b * h)), 2)}
    return {Fr(x, 2) for x in range(1, 4000) if b * Fr(x, 2) / 2 == A}


def b_rect_tri_area(w, h, th):
    pts = [(0, 0), (w, 0), (w, h), (Fr(w, 2), h + th), (0, h)]
    s = 0
    for i in range(len(pts)):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % len(pts)]
        s += x1 * y2 - x2 * y1
    return {abs(Fr(s)) / 2}


def b_angle(kind, **k):
    if kind == 'sum':
        return {Fr(x) for x in range(0, 361) if x + sum(k['given']) == k['total']}
    if kind == 'isos_base':
        return {Fr(x) for x in range(1, 90) if 2 * x + k['apex'] == 180}
    if kind == 'regular':
        n = k['n']
        # exterior angles of a regular polygon add to 360; each interior angle = 180 - exterior
        return {Fr(180) - Fr(360, n)}
    if kind == 'clock':
        t = k['h'] * 60 + k['m']
        hour = Fr(t) * Fr(1, 2)
        while hour >= 360:
            hour -= 360
        minute = Fr(k['m']) * 6
        diff = abs(hour - minute)
        return {diff if diff <= 180 else 360 - diff}
    raise ValueError(kind)


def b_diag(n):
    segs = set(itertools.combinations(range(n), 2))
    sides = {tuple(sorted((i, (i + 1) % n))) for i in range(n)}
    return {len(segs - sides)}


def b_neg_diff(a, b):
    x, steps = min(a, b), 0
    while x < max(a, b):
        x += 1
        steps += 1
    return {steps}


def b_equation(form, a, b, c, d=0):
    out = set()
    for x in range(-300, 3000):
        if form == 'ax+b=c':
            ok = a * x + b == c
        else:
            ok = a * x + b == c * x + d
        if ok:
            out.add(x)
    return out


def b_nth_term(a, b, n):
    seq = [b + a * i for i in range(1, n + 1)]
    return {seq[-1]}


def b_term_index(a, b, v):
    return {i for i in range(1, 5000) if b + a * i == v}


def b_prob(kind, **k):
    if kind == 'marbles':
        bag = [c for c, n in k['counts'] for _ in range(n)]
        if k['draws'] == 1:
            good = [i for i, c in enumerate(bag) if (c == k['color']) != bool(k.get('negate'))]
            return {Fr(len(good), len(bag))}
        pairs = [(i, j) for i in range(len(bag)) for j in range(len(bag)) if i != j]
        good = [p for p in pairs if bag[p[0]] == k['color'] and bag[p[1]] == k['color']]
        return {Fr(len(good), len(pairs))}
    if kind == 'dice':
        outs = list(itertools.product(range(1, 7), repeat=2))
        arg = k.get('arg')
        f = {'sum_eq': lambda x, y: x + y == arg, 'product_even': lambda x, y: x * y % 2 == 0,
             'sum_at_least': lambda x, y: x + y >= arg, 'doubles': lambda x, y: x == y,
             'diff_eq': lambda x, y: abs(x - y) == arg, 'product_eq': lambda x, y: x * y == arg}[k['pred']]
        return {Fr(sum(1 for x, y in outs if f(x, y)), len(outs))}
    if kind == 'coins':
        outs = list(itertools.product('HT', repeat=k['n']))
        return {Fr(sum(1 for o in outs if o.count('H') >= k['atleast']), len(outs))}
    raise ValueError(kind)


def _prog_source(init, ops, repeat):
    src = 'x = Fraction(%d)\nfor _ in range(%d):\n' % (init, repeat)
    for op, m in ops:
        src += '    x = x %s Fraction(%d)\n' % (op, m)
    return src


def b_prog(init, ops, repeat):
    env = {'Fraction': Fr}
    exec(_prog_source(init, ops, repeat), env)
    return {env['x']}


def b_nested(o_lo, o_hi, i_from, i_hi):
    env = {}
    src = 'count = 0\nfor i in range(%d, %d + 1):\n    for j in range(%s, %d + 1):\n        count += 1\n' % (
        o_lo, o_hi, 'i' if i_from == 'i' else str(i_from), i_hi)
    exec(src, env)
    return {env['count']}


def b_turtle(angle_deg, length, ask):
    import cmath
    import math
    pos, heading, reps = 0j, 0.0, 0
    while True:
        pos += length * cmath.exp(1j * math.radians(heading))
        heading += angle_deg
        reps += 1
        if abs(pos) < 1e-6 and abs(heading % 360) < 1e-9 or reps > 2000:
            break
    return {reps if ask == 'repeats' else reps * length}


def b_cipher(enc, shift, words):
    out = set()
    for s in range(26):
        cand = ''.join(chr((ord(ch) - 65 - s) % 26 + 65) for ch in enc.upper()).lower()
        if cand in words:
            out.add(cand)
    return out


def b_binary(ask, s=None, n=None):
    if ask == 'to_dec':
        return {sum(int(ch) * 2 ** (len(s) - 1 - i) for i, ch in enumerate(s))}
    return {int(format(n, 'b'))}


def b_liar(people, claims, truths):
    out = set()
    for k in itertools.combinations(range(len(people)), truths):    # who is telling the truth
        for culprit in people:
            good = True
            for i, (target, mode) in enumerate(claims):
                holds = (culprit == target) if mode == 'is' else (culprit != target)
                if holds != (i in k):
                    good = False
            if good:
                out.add(culprit)
    return out


def b_magic(cells9, nums, ask_idx):
    out = set()
    lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for perm in itertools.permutations(nums):
        if any(c is not None and c != p for c, p in zip(cells9, perm)):
            continue
        if len({sum(perm[i] for i in ln) for ln in lines}) == 1:
            out.add(perm[ask_idx])
    return out


def b_cryptarithm(pattern, sol, ask):
    lhs, rhs = pattern.split('=')
    letters = sorted(set(c for c in pattern if c.isalpha()))
    out = set()
    for digs in itertools.permutations(range(10), len(letters)):
        m = dict(zip(letters, digs))
        ok = True
        for term in [t for t in lhs.replace('*', '+').replace('-', '+').split('+')] + [rhs]:
            if len(term) > 1 and term[0].isalpha() and m[term[0]] == 0:
                ok = False
        if not ok:
            continue
        conv = lambda e: ''.join(str(m[c]) if c.isalpha() else c for c in e)
        # numbers must not have a leading zero after substitution
        if eval(conv(lhs)) == eval(conv(rhs)):
            out.add(m[ask])
    return out


def b_rounding(n, place):
    cands = [m for m in range(0, n + 2 * place, place)]
    best = min(abs(n - m) for m in cands)
    near = [m for m in cands if abs(n - m) == best]
    return {max(near)}      # halfway rounds up


def b_rounding_count(place, center):
    return {len([n for n in range(0, center + 5 * place) if b_rounding(n, place) == {center}])}


def b_calendar_nth(day, on, want, nth):
    wd = DAYNAMES.index(on)
    hits = []
    for date in range(1, 32):
        w = (wd + date - day) % 7
        if DAYNAMES[w] == want:
            hits.append(date)
    return {hits[nth - 1]}


def b_lcm_meet(a, b):
    t = 1
    while not (t % a == 0 and t % b == 0):
        t += 1
    return {t}


def b_gcd_bags(x, y):
    return {max(g for g in range(1, min(x, y) + 1) if x % g == 0 and y % g == 0)}


def b_factor_count(n):
    return {len(_factors(n))}


def b_prime_factor_sum(n):
    return {sum(p for p in range(2, n + 1) if _is_prime(p) and n % p == 0)}


def b_remainder_pair(lo, hi, conds):
    return {n for n in range(lo, hi + 1) if all(n % m == r for m, r in conds)}


def b_consec(count, step, total, ask):
    out = set()
    for s in range(0, total + 1):
        seq = [s + step * i for i in range(count)]
        if sum(seq) == total:
            out.add(seq[0] if ask == 'smallest' else seq[-1])
    return out


def b_anagram(word):
    return {len(set(itertools.permutations(word)))}


def b_painted_cube(n, faces):
    cnt = 0
    for x, y, z in itertools.product(range(n), repeat=3):
        painted = sum(1 for v in (x, y, z) if v in (0, n - 1))
        cnt += painted == faces
    return {cnt}


def _poly(name):
    import math
    reg = {'square': 4, 'regular hexagon': 6, 'equilateral triangle': 3, 'regular pentagon': 5, 'regular octagon': 8}
    if name in reg:
        n = reg[name]
        return [(math.cos(2 * math.pi * i / n + 0.3), math.sin(2 * math.pi * i / n + 0.3)) for i in range(n)]
    if name == 'rectangle':
        return [(-2, -1), (2, -1), (2, 1), (-2, 1)]
    if name == 'rhombus':
        return [(-2, 0), (0, -1), (2, 0), (0, 1)]
    if name == 'isosceles triangle':
        return [(-1, 0), (1, 0), (0, 3)]
    if name == 'kite':
        return [(0, 4), (1.5, 1), (0, -1), (-1.5, 1)]
    raise ValueError(name)


def _sym_lines(name):
    import math
    pts = _poly(name)
    cx = sum(p[0] for p in pts) / len(pts)
    cy = sum(p[1] for p in pts) / len(pts)
    pts = [(x - cx, y - cy) for x, y in pts]
    angles = set()
    for (x, y) in pts:
        angles.add(round(math.atan2(y, x) % math.pi, 6))
    for i in range(len(pts)):
        mx = (pts[i][0] + pts[(i + 1) % len(pts)][0]) / 2
        my = (pts[i][1] + pts[(i + 1) % len(pts)][1]) / 2
        angles.add(round(math.atan2(my, mx) % math.pi, 6))
    # also axes perpendicular to an edge midpoint direction handled above; rectangle axes are along edge midpoints
    good = set()
    for a in angles:
        c, s = math.cos(2 * a), math.sin(2 * a)
        refl = [(c * x + s * y, s * x - c * y) for x, y in pts]
        if all(any(abs(rx - x) < 1e-5 and abs(ry - y) < 1e-5 for x, y in pts) for rx, ry in refl):
            good.add(round(a % math.pi, 4))
    return len(good)


def b_symmetry(shapes):
    return {sum(_sym_lines(s) for s in shapes)}


def b_expr_form(form, a, b, c, d):
    tmpl = {'A': '({a} + {b}) * {c} - {d}', 'B': '{a} + {b} * {c} - {d}', 'C': '{a} * {b} + {c} * {d}',
            'D': '({a} - {b}) * ({c} + {d})', 'F': '{a} * ({b} + {c}) - {d}', 'G': '({a} + {b}) / {c} * {d}'}[form]
    return {Fr(eval(tmpl.format(a='Fr(%d)' % a, b='Fr(%d)' % b, c='Fr(%d)' % c, d='Fr(%d)' % d), {'Fr': Fr}))}


BRUTE = {k[2:]: v for k, v in dict(globals()).items() if k.startswith('b_')}


import brute_more as _more   # noqa: E402  (fix round 1: further independent checkers)
BRUTE.update(_more.BRUTE)

import brute_r2 as _r2   # noqa: E402  (fix round 2: independent checkers for the new sub-structures)
BRUTE.update(_r2.BRUTE)
