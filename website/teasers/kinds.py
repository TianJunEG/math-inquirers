"""GENERATOR side of the daily-teaser puzzles.

Each kind is a function SOLVE[kind](**params) -> (answer, ctx).
  answer : int | Fraction | str   (Fraction = a value in the unit asked, e.g. dollars)
  ctx    : extra strings/numbers the worked explanation and question can quote.
These are the solvers the puzzle author used.  verify_bank.py re-solves every puzzle with
the separate brute-force code in brute.py (which never imports this file) and also proves
the answer is the ONLY one in the search space.
"""
import itertools
import math
from fractions import Fraction as Fr

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def _join(xs):
    xs = [str(x) for x in xs]
    return xs[0] if len(xs) == 1 else ', '.join(xs[:-1]) + ' and ' + xs[-1]


# ---------------------------------------------------------------- sequences and arithmetic
def seq_term(a, d, n):
    ans = a + (n - 1) * d
    return ans, {'terms': ', '.join(str(a + i * d) for i in range(4)), 'step': abs(d),
                 'all': ', '.join(str(a + i * d) for i in range(n))}


def dot(pairs):
    prods = [c * e for c, e in pairs]
    return sum(prods), {'parts': ' and '.join('%d \u00d7 %d = %d' % (c, e, c * e) for c, e in pairs),
                        'add': '%s = %d' % (' + '.join(str(x) for x in prods), sum(prods))}


def seq_pos(a, d, v):
    assert (v - a) % d == 0
    n = (v - a) // d + 1
    assert n >= 1
    return n, {'steps': n - 1, 'step': abs(d), 'second': a + d, 'gap': v - a,
               'terms': ', '.join(str(a + i * d) for i in range(4))}


def groups_plus(g, s, r=0):
    return g * s + r, {'prod': g * s}


def part_whole(total, parts):
    return total - sum(parts), {'used': sum(parts)}


def chain(base, steps, ask):
    vals = [base]
    for sgn, m in steps:
        vals.append(vals[-1] + m if sgn == '+' else vals[-1] - m if sgn == '-' else vals[-1] * m)
    ctx = {'v%d' % i: v for i, v in enumerate(vals)}
    ans = {'sum': sum(vals), 'last': vals[-1], 'spread': max(vals) - min(vals)}[ask]
    return ans, ctx


def sum_diff(S, D, ask):
    assert (S + D) % 2 == 0
    big, small = (S + D) // 2, (S - D) // 2
    return (big if ask == 'larger' else small), {'big': big, 'small': small, 'twice_small': S - D}


def sum_range(lo, hi, step=1):
    n = (hi - lo) // step + 1
    assert lo + (n - 1) * step == hi
    return n * (lo + hi) // 2, {'n': n, 'pair': lo + hi, 'half': n // 2}


def queue(front, back):
    return front + back - 1, {'both': front + back}


def fence(length, gap, closed=False):
    assert length % gap == 0
    s = length // gap
    return (s if closed else s + 1), {'sections': s}


def combos(counts):
    return math.prod(counts), {}


def pairs(n):
    return n * (n - 1) // 2, {'each': n - 1}


def _digits(n):
    out = []
    while n:
        n, r = divmod(n, 10)
        out.append(r)
    return out[::-1] or [0]


def _pred(name, arg, n):
    d = _digits(n)
    if name == 'same_digits':
        return len(set(d)) == 1
    if name == 'digit_sum':
        return sum(d) == arg
    if name == 'contains':
        return arg in d
    if name == 'even':
        return n % 2 == 0
    if name == 'multiple':
        return n % arg == 0
    if name == 'ends_in':
        return n % 10 in arg
    if name == 'distinct':
        return len(set(d)) == len(d)
    if name == 'first_odd':
        return d[0] % 2 == 1
    if name == 'digit_product':
        return math.prod(d) == arg
    if name == 'increasing':
        return all(d[i] < d[i + 1] for i in range(len(d) - 1))
    if name == 'factor_count':
        c, k = 0, 1
        while k * k <= n:
            if n % k == 0:
                c += 1 if k * k == n else 2
            k += 1
        return c == arg
    if name == 'prime':
        return n > 1 and all(n % k for k in range(2, int(n ** 0.5) + 1))
    if name == 'square':
        r = math.isqrt(n)
        return r * r == n
    if name == 'palindrome':
        return d == d[::-1]
    if name == 'digit_eq':
        return d[arg[0]] == arg[1]
    if name == 'digit_plus':
        return d[arg[0]] == d[arg[1]] + arg[2]
    if name == 'digit_times':
        return d[arg[0]] == arg[2] * d[arg[1]]
    if name == 'digit_less':
        return d[arg[0]] < d[arg[1]]
    raise ValueError(name)


def scan(lo, hi, preds, ask):
    hits = [n for n in range(lo, hi + 1) if all(_pred(p, a, n) for p, a in preds)]
    if ask == 'only':
        assert len(hits) == 1, hits
        return hits[0], {}
    ans = {'count': len(hits), 'min': hits[0] if hits else None, 'max': hits[-1] if hits else None}[ask]
    return ans, {'first': ', '.join(str(h) for h in hits[:6])}


def digits_extreme(digits, ndig, ask):
    perms = {int(''.join(map(str, p))) for p in itertools.permutations(digits, ndig)
             if p[0] != 0 or ndig == 1}
    if ask == 'largest':
        r = max(perms)
    elif ask == 'smallest':
        r = min(perms)
    elif ask == 'smallest_even':
        r = min(x for x in perms if x % 2 == 0)
    elif ask == 'largest_odd':
        r = max(x for x in perms if x % 2 == 1)
    elif ask == 'largest_even':
        r = max(x for x in perms if x % 2 == 0)
    elif ask == 'smallest_odd':
        r = min(x for x in perms if x % 2 == 1)
    else:
        raise ValueError(ask)
    return r, {}


def count_arrangements(digits, ndig, cond):
    perms = {int(''.join(map(str, p))) for p in itertools.permutations(digits, ndig) if p[0] != 0}
    if cond == 'even':
        perms = {x for x in perms if x % 2 == 0}
    elif cond == 'odd':
        perms = {x for x in perms if x % 2 == 1}
    elif cond == 'over':
        pass
    return len(perms), {'list': ', '.join(str(x) for x in sorted(perms)[:8])}


def clock_end_hour(h, add):
    return (h - 1 + add) % 12 + 1, {}


def elapsed(h1, m1, h2, m2):
    return (h2 * 60 + m2) - (h1 * 60 + m1), {}


def weekday(start, days):
    return DAYS[(DAYS.index(start) + days) % 7], {'weeks': days // 7, 'extra': days % 7}


def share(total, k, ask):
    if ask == 'each':
        assert total % k == 0
        return total // k, {}
    if ask == 'left':
        return total % k, {'q': total // k}
    if ask == 'boxes':
        return -(-total // k), {'q': total // k, 'r': total % k}
    if ask == 'groups':
        assert total % k == 0
        return total // k, {}
    raise ValueError(ask)


def perimeter_regular(n, side):
    return n * side, {}


def rect(ask, l=None, w=None, P=None, A=None):
    if ask == 'perimeter':
        return 2 * (l + w), {'half': l + w}
    if ask == 'area':
        return l * w, {}
    if ask == 'width_from_perimeter':
        assert P % 2 == 0
        return P // 2 - l, {'half': P // 2}
    if ask == 'width_from_area':
        assert A % l == 0
        return A // l, {}
    if ask == 'square_perimeter_from_area':
        s = math.isqrt(A)
        assert s * s == A
        return 4 * s, {'side': s}
    if ask == 'square_area_from_perimeter':
        assert P % 4 == 0
        return (P // 4) ** 2, {'side': P // 4}
    raise ValueError(ask)


def cells(outer, cuts, ask):
    W, H = outer
    area = W * H - sum(cw * ch for (_, _, cw, ch) in cuts)
    for (x, y, cw, ch) in cuts:   # corner cut-outs only: the perimeter stays that of the outer rectangle
        assert (x == 0 or x + cw == W) and (y == 0 or y + ch == H)
    return (area if ask == 'area' else 2 * (W + H)), {'whole': W * H, 'removed': W * H - area}


def equiv_chain(rates, n):
    return n * math.prod(rates), {}


def shopping(items, pay, ask):
    total = sum(c * q for c, q in items)
    return (Fr(total, 100) if ask == 'total' else Fr(pay - total, 100)), {'total_c': total}


def mystery(ops, result):
    x = result
    for op, m in reversed(ops):
        x = {'+': x - m, '-': x + m, '*': Fr(x, m), '/': x * m}[op]
    assert x == int(x)
    return int(x), {}


def order_logic(order, facts, idx, rel):
    ctx = {'clues': ' '.join('%s is %s %s.' % (a, rel, b) for a, b in facts)}
    return order[idx], ctx


def moves(start, mv, ask):
    pos, path = start, [start]
    for m in mv:
        pos += m
        path.append(pos)
    ans = {'final': pos, 'max': max(path), 'min': min(path)}[ask]
    return ans, {'path': ', '.join(str(p).replace('-', '\u2212') for p in path)}


def route_text(mv, up, down):
    return ', then '.join('%s %d' % (up if m > 0 else down, abs(m)) for m in mv)


def coin_ways(target, coins):
    ways = [1] + [0] * target
    for c in coins:
        for t in range(c, target + 1):
            ways[t] += ways[t - c]
    return ways[target], {}


def repeat_pattern(unit, n, ask, item=None):
    if ask == 'at':
        return unit[(n - 1) % len(unit)], {'cycle': len(unit)}
    full, rest = divmod(n, len(unit))
    return full * unit.count(item) + unit[:rest].count(item), {'cycle': len(unit), 'full': full, 'rest': rest}


def stairs(n, steps):
    f = [1] + [0] * n
    for i in range(1, n + 1):
        f[i] = sum(f[i - s] for s in steps if i - s >= 0)
    return f[n], {'seq': ', '.join(str(x) for x in f[1:])}


def grid_count(m, n, what):
    if what == 'squares':
        assert m == n
        return sum(k * k for k in range(1, n + 1)), {}
    return (m * (m + 1) // 2) * (n * (n + 1) // 2), {'rows': m * (m + 1) // 2, 'cols': n * (n + 1) // 2}


def lattice(right, down, blocked):
    ways = {}
    for i in range(right + 1):
        for j in range(down + 1):
            if (i, j) in map(tuple, blocked):
                ways[(i, j)] = 0
            elif i == 0 and j == 0:
                ways[(i, j)] = 1
            else:
                ways[(i, j)] = ways.get((i - 1, j), 0) + ways.get((i, j - 1), 0)
    return ways[(right, down)], {}


def matchsticks(shape, n, r=None, c=None):
    if shape == 'sq':
        return 3 * n + 1, {}
    if shape == 'tri':
        return 2 * n + 1, {}
    if shape == 'grid':
        return r * (c + 1) + c * (r + 1), {}
    raise ValueError(shape)


def age_times(child, parent, k):
    t = Fr(parent - k * child, k - 1)
    assert t == int(t) and t > 0
    return int(t), {'c': child + int(t), 'p': parent + int(t)}


def fraction_of(n, num, den):
    assert n % den == 0
    return n // den * num, {'part': n // den}


def fraction_seq(start, steps, ask):
    cur, taken = Fr(start), []
    for num, den, base in steps:
        t = (Fr(start) if base == 'whole' else cur) * Fr(num, den)
        taken.append(t)
        cur -= t
    ctx = {'t%d' % i: (int(t) if t == int(t) else t) for i, t in enumerate(taken)}
    ctx['left'] = int(cur) if cur == int(cur) else cur
    ans = cur if ask == 'left' else sum(taken)
    assert ans == int(ans)
    return int(ans), ctx


def fraction_whole(left, num, den):
    w = Fr(left * den, den - num)
    assert w == int(w)
    return int(w), {'unit': w / den}


def _mixed(t):
    whole, n, d = t
    return Fr(whole) + Fr(n, d)


def frac_arith(op, a, b):
    A, B = _mixed(a), _mixed(b)
    return {'+': A + B, '-': A - B, '*': A * B}[op], {}


def decimals(op, a, b):
    A, B = Fr(a), Fr(b)
    return {'+': A + B, '-': A - B, '*': A * B, '/': A / B}[op], {}


def pct(kind, **k):
    if kind == 'of':
        return Fr(k['n']) * k['p'] / 100, {}
    if kind == 'whole':
        return Fr(k['part'] * 100, k['p']), {'one': Fr(k['part'], k['p'])}
    if kind == 'discount':
        price = Fr(k['price'])
        pay = price * (100 - k['p']) / 100
        return (pay if k['ask'] == 'pay' else price - pay), {'off': price * k['p'] / 100}
    if kind == 'then':
        v = Fr(100)
        for s in k['steps']:
            v = v * (100 + s) / 100
        return v, {}
    raise ValueError(kind)


def pct_rest(n, ps):
    rest = 100 - sum(ps)
    assert (n * rest) % 100 == 0
    return n * rest // 100, {'rest': rest}


def ratio(kind, **k):
    if kind == 'share':
        a, b, N = k['a'], k['b'], k['N']
        assert N % (a + b) == 0
        u = N // (a + b)
        return {'larger': max(a, b) * u, 'smaller': min(a, b) * u, 'diff': abs(a - b) * u}[k['ask']], {'unit': u, 'parts': a + b}
    if kind == 'whole':
        a, b, known = k['a'], k['b'], k['known']
        assert known % a == 0
        u = known // a
        return (a + b) * u, {'unit': u, 'parts': a + b}
    if kind == 'transfer_equal':
        a, b, give = k['a'], k['b'], k['give']
        assert (2 * give) % (a - b) == 0
        u = 2 * give // (a - b)
        return (a + b) * u, {'unit': u}
    if kind == 'add_equal':
        a, b, add = k['a'], k['b'], k['add']
        assert add % (b - a) == 0
        u = add // (b - a)
        return {'b': b * u, 'a': a * u, 'total': (a + b) * u}[k['ask']], {'unit': u}
    raise ValueError(kind)


def stats(data, ask):
    n = len(data)
    s = sorted(data)
    if ask == 'mean':
        return Fr(sum(data), n), {'sum': sum(data), 'n': n}
    if ask == 'median':
        m = n // 2
        return (Fr(s[m]) if n % 2 else Fr(s[m - 1] + s[m], 2)), {'sorted': ', '.join(map(str, s))}
    if ask == 'mode':
        best = max(set(data), key=lambda v: (data.count(v), -v))
        return best, {}
    if ask == 'range':
        return s[-1] - s[0], {}
    if ask == 'total':
        return sum(data), {}
    raise ValueError(ask)


def mean_missing(data, target):
    return target * (len(data) + 1) - sum(data), {'need': target * (len(data) + 1), 'have': sum(data)}


def mean_remove(n, mean_all, mean_rest):
    return n * mean_all - (n - 1) * mean_rest, {'all': n * mean_all, 'rest': (n - 1) * mean_rest}


def meet(d, v1, v2):
    assert d % (v1 + v2) == 0
    return d // (v1 + v2), {'closing': v1 + v2}


def fill(cap, rin, rout):
    assert cap % (rin - rout) == 0
    return cap // (rin - rout), {'net': rin - rout}


def avg_speed(v1, v2):
    return Fr(2 * v1 * v2, v1 + v2), {}


def speed(d, h, m):
    return Fr(d) / (Fr(h) + Fr(m, 60)), {'mins': h * 60 + m}


def volume(l, w, h):
    return l * w * h, {'base': l * w}


def water_rise(l, w, litres):
    return Fr(litres * 1000, l * w), {'cm3': litres * 1000, 'base': l * w}


def tri_area(ask, b=None, h=None, A=None):
    if ask == 'area':
        return Fr(b * h, 2), {}
    if ask == 'height':
        return Fr(2 * A, b), {}
    raise ValueError(ask)


def rect_tri_area(w, h, th):
    return w * h + Fr(w * th, 2), {'rect': w * h, 'tri': Fr(w * th, 2)}


def angle(kind, **k):
    if kind == 'sum':
        return k['total'] - sum(k['given']), {'used': sum(k['given'])}
    if kind == 'isos_base':
        return Fr(180 - k['apex'], 2), {}
    if kind == 'regular':
        return Fr(180 * (k['n'] - 2), k['n']), {'total': 180 * (k['n'] - 2)}
    if kind == 'clock':
        mins = k['h'] * 60 + k['m']
        hour_a, min_a = Fr(mins, 2) % 360, Fr(k['m'] * 6) % 360
        d = abs(hour_a - min_a)
        return min(d, 360 - d), {'hour': hour_a, 'minute': min_a}
    raise ValueError(kind)


def diag(n):
    return n * (n - 3) // 2, {}


def neg_diff(a, b):
    return abs(a - b), {}


def equation(form, a, b, c, d=0):
    if form == 'ax+b=c':
        assert (c - b) % a == 0
        return (c - b) // a, {'rhs': c - b}
    assert (d - b) % (a - c) == 0
    return (d - b) // (a - c), {'diff_x': a - c, 'diff_c': d - b}


def nth_term(a, b, n):
    return a * n + b, {}


def term_index(a, b, v):
    assert (v - b) % a == 0
    return (v - b) // a, {}


def prob(kind, **k):
    if kind == 'marbles':
        counts = k['counts']
        tot = sum(c for _, c in counts)
        want = dict(counts)[k['color']]
        if k['draws'] == 1:
            p = Fr(want if not k.get('negate') else tot - want, tot)
        else:
            p = Fr(want, tot) * Fr(want - 1, tot - 1)
        return p, {'total': tot}
    if kind == 'dice':
        pred = k['pred']
        arg = k.get('arg') or 0
        good = 0
        for x in range(1, 7):
            for y in range(1, 7):
                ok = {'sum_eq': x + y == arg, 'product_even': (x * y) % 2 == 0, 'sum_at_least': x + y >= arg,
                      'doubles': x == y, 'diff_eq': abs(x - y) == arg, 'product_eq': x * y == arg}[pred]
                good += ok
        return Fr(good, 36), {'good': good}
    if kind == 'coins':
        n, atleast = k['n'], k['atleast']
        good = sum(math.comb(n, j) for j in range(atleast, n + 1))
        return Fr(good, 2 ** n), {'good': good, 'all': 2 ** n}
    raise ValueError(kind)


def prog_text(init, ops, repeat, var='x'):
    lines = ['%s = %d' % (var, init), 'repeat %d times:' % repeat]
    for op, m in ops:
        sym = {'+': '+', '-': '-', '*': '*', '/': '/'}[op]
        lines.append('    %s = %s %s %d' % (var, var, sym if op != '/' else '/', m))
    return lines


def prog(init, ops, repeat):
    x = init
    for _ in range(repeat):
        for op, m in ops:
            x = {'+': x + m, '-': x - m, '*': x * m, '/': Fr(x, m)}[op]
    assert x == int(x)
    return int(x), {'code': '\n'.join(prog_text(init, ops, repeat))}


def nested_text(o_lo, o_hi, i_from, i_hi):
    return ['count = 0', 'for i from %d to %d:' % (o_lo, o_hi),
            '    for j from %s to %d:' % ('i' if i_from == 'i' else i_from, i_hi), '        count = count + 1']


def nested(o_lo, o_hi, i_from, i_hi):
    total = 0
    for i in range(o_lo, o_hi + 1):
        start = i if i_from == 'i' else i_from
        total += max(0, i_hi - start + 1)
    return total, {'code': '\n'.join(nested_text(o_lo, o_hi, i_from, i_hi))}


def turtle(angle_deg, length, ask):
    reps = 360 // angle_deg
    assert reps * angle_deg == 360
    return (reps if ask == 'repeats' else reps * length), {'reps': reps}


def cipher(enc, shift, words):
    dec = ''.join(chr((ord(c) - 65 - shift) % 26 + 65) for c in enc.upper())
    return dec.lower(), {'dec': dec.lower()}


def binary(ask, s=None, n=None):
    if ask == 'to_dec':
        v = 0
        for ch in s:
            v = v * 2 + int(ch)
        return v, {}
    # to_bin: answer is the digit string, compared as a number
    out, m = '', n
    while m:
        out = str(m % 2) + out
        m //= 2
    return int(out), {'bin': out}


def _claim_text(speaker, target, mode):
    if mode == 'is':
        return 'It was me.' if speaker == target else 'It was %s.' % target
    return 'It was not me.' if speaker == target else 'It was not %s.' % target


def liar(people, claims, truths):
    ok = []
    for culprit in people:
        t = 0
        for who, (target, mode) in zip(people, claims):
            holds = (culprit == target) if mode == 'is' else (culprit != target)
            t += holds
        if t == truths:
            ok.append(culprit)
    assert len(ok) == 1
    lines = ['%s says: "%s"' % (p, _claim_text(p, t, m)) for p, (t, m) in zip(people, claims)]
    return ok[0], {'statements': ' '.join(lines)}


def magic(cells9, nums, ask_idx):
    S = Fr(sum(nums), 3)
    grid = [None if c is None else c for c in cells9]
    lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    known = list(grid)
    for _ in range(9):
        for ln in lines:
            unk = [i for i in ln if known[i] is None]
            if len(unk) == 1:
                known[unk[0]] = int(S - sum(known[i] for i in ln if known[i] is not None))
    rows = '\n'.join('   '.join(str(c) if c is not None else '?' for c in cells9[i:i + 3]) for i in (0, 3, 6))
    return known[ask_idx], {'S': int(S), 'grid': rows}


def cryptarithm(pattern, sol, ask):
    return sol[ask], {}


def rounding(n, place):
    q, r = divmod(n, place)
    return (q + 1 if 2 * r >= place else q) * place, {}


def rounding_count(place, center):
    lo, hi = center - place // 2, center + place // 2 - 1
    return hi - lo + 1, {'lo': lo, 'hi': hi}


def calendar_nth(day, on, want, nth):
    gap = (DAYS.index(want) - DAYS.index(on)) % 7
    first = day + gap
    while first - 7 >= 1:
        first -= 7
    return first + 7 * (nth - 1), {'first': first}


def lcm_meet(a, b):
    return a * b // math.gcd(a, b), {'g': math.gcd(a, b)}


def gcd_bags(x, y):
    return math.gcd(x, y), {}


def factor_count(n):
    return sum(2 if d * d != n else 1 for d in range(1, math.isqrt(n) + 1) if n % d == 0), {}


def prime_factor_sum(n):
    ps, m, p = [], n, 2
    while m > 1:
        if m % p == 0:
            ps.append(p)
            while m % p == 0:
                m //= p
        p += 1
    return sum(ps), {'primes': _join(ps)}


def remainder_pair(lo, hi, conds):
    m0, r0 = conds[0]
    hits = [n for n in range(lo + (r0 - lo) % m0, hi + 1, m0) if all(n % m == r for m, r in conds)]
    assert len(hits) == 1
    return hits[0], {}


def consec(count, step, total, ask):
    first = Fr(total - step * count * (count - 1) // 2, count)
    assert first == int(first)
    first = int(first)
    return (first if ask == 'smallest' else first + step * (count - 1)), {'first': first}


def anagram(word):
    c = math.factorial(len(word))
    for ch in set(word):
        c //= math.factorial(word.count(ch))
    return c, {}


def painted_cube(n, faces):
    k = n - 2
    return {0: k ** 3, 1: 6 * k * k, 2: 12 * k, 3: 8}[faces], {}


SHAPE_LINES = {'square': 4, 'rectangle': 2, 'equilateral triangle': 3, 'regular hexagon': 6, 'rhombus': 2,
               'regular pentagon': 5, 'isosceles triangle': 1, 'kite': 1, 'regular octagon': 8}


def symmetry(shapes):
    return sum(SHAPE_LINES[s] for s in shapes), {'each': ', '.join('%s %d' % (s, SHAPE_LINES[s]) for s in shapes)}


def expr_form(form, a, b, c, d):
    v = {'A': (a + b) * c - d, 'B': a + b * c - d, 'C': a * b + c * d, 'D': (a - b) * (c + d),
         'E': a + b * c * 1 - d // 1, 'F': a * (b + c) - d, 'G': Fr(a + b, c) * d}[form]
    return v, {}


EXPR_TEXT = {'A': '({a} + {b}) × {c} − {d}', 'B': '{a} + {b} × {c} − {d}', 'C': '{a} × {b} + {c} × {d}',
             'D': '({a} − {b}) × ({c} + {d})', 'E': '{a} + {b} × {c} − {d}',
             'F': '{a} × ({b} + {c}) − {d}', 'G': '({a} + {b}) ÷ {c} × {d}'}


SOLVE = {k: v for k, v in dict(globals()).items()
         if callable(v) and not k.startswith('_') and k in (
             'seq_term', 'seq_pos', 'dot', 'groups_plus', 'part_whole', 'chain', 'sum_diff', 'sum_range', 'queue', 'fence',
             'combos', 'pairs', 'scan', 'digits_extreme', 'count_arrangements', 'clock_end_hour', 'elapsed',
             'weekday', 'share', 'perimeter_regular', 'rect', 'cells', 'equiv_chain', 'shopping', 'mystery',
             'order_logic', 'moves', 'coin_ways', 'repeat_pattern', 'stairs', 'grid_count', 'lattice',
             'matchsticks', 'age_times', 'fraction_of', 'fraction_seq', 'fraction_whole', 'frac_arith',
             'decimals', 'pct', 'pct_rest', 'ratio', 'stats', 'mean_missing', 'mean_remove', 'meet', 'fill', 'avg_speed',
             'speed', 'volume', 'water_rise', 'tri_area', 'rect_tri_area', 'angle', 'diag', 'neg_diff',
             'equation', 'nth_term', 'term_index', 'prob', 'prog', 'nested', 'turtle', 'cipher', 'binary',
             'liar', 'magic', 'cryptarithm', 'rounding', 'rounding_count', 'calendar_nth', 'lcm_meet',
             'gcd_bags', 'factor_count', 'prime_factor_sum', 'remainder_pair', 'consec', 'anagram',
             'painted_cube', 'symmetry', 'expr_form')}


import kinds_more as _more   # noqa: E402  (fix round 1: further solvers)
SOLVE.update(_more.SOLVE)
