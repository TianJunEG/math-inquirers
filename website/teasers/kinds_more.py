"""GENERATOR side, part 2: solvers added in fix round 1 (new maths structures so that no structure repeats inside a quarter).

Same contract as kinds.py: SOLVE[kind](**params) -> (answer, ctx).  Merged into kinds.SOLVE at the bottom of kinds.py.
The independent brute-force checkers are in brute_more.py (which never imports this file)."""
import itertools
import math
from fractions import Fraction as Fr

SOLVE = {}


def kind(fn):
    SOLVE[fn.__name__] = fn
    return fn


def _j(xs):
    return ', '.join(str(x) for x in xs)


# ================================================================== Level 1 structures
@kind
def doubling(start, times):
    vals = [start * 2 ** i for i in range(times + 1)]
    return vals[-1], {'chain': _j(vals)}


@kind
def bond_pairs(total, lo=1):
    prs = [(a, total - a) for a in range(lo, total // 2 + 1) if total - a >= lo]
    return len(prs), {'list': ', '.join('%d + %d' % x for x in prs)}


@kind
def scaled_diff(scale, a, b):
    return (a - b) * scale, {'da': a * scale, 'db': b * scale, 'gap': a - b}


@kind
def fewest_coins(target, coins):
    best = {0: []}
    for t in range(1, target + 1):
        opts = [best[t - c] + [c] for c in coins if t - c >= 0 and (t - c) in best]
        if opts:
            best[t] = min(opts, key=len)
    sol = sorted(best[target], reverse=True)
    return len(sol), {'combo': ' + '.join(str(c) for c in sol)}


@kind
def count_between(lo, hi, inclusive):
    if inclusive:
        return hi - lo + 1, {'first': lo, 'last': hi}
    return hi - lo - 1, {'first': lo + 1, 'last': hi - 1}


@kind
def growing_gaps(first, gap0, n):
    terms, gaps, cur, g = [first], [], first, gap0
    for _ in range(n - 1):
        cur += g
        gaps.append(g)
        g += 1
        terms.append(cur)
    return terms[-1], {'terms': _j(terms[:5]), 'all': _j(terms), 'gaps': _j(gaps)}


@kind
def span(a, b):
    return b - a, {}


@kind
def match_assign(people, things, clues, ask_thing=None, ask_person=None):
    sols = []
    for perm in itertools.permutations(things):
        has = dict(zip(people, perm))
        if all((has[p] == t) == truth for p, t, truth in clues):
            sols.append(has)
    assert len(sols) == 1, sols
    has = sols[0]
    if ask_thing:
        ans = [p for p in people if has[p] == ask_thing][0]
    else:
        ans = has[ask_person]
    return ans, {'sol': ', '.join('%s has the %s' % (p, has[p]) for p in people)}


DIRS = ['north', 'east', 'south', 'west']


@kind
def turns(start, moves):
    i = DIRS.index(start)
    path = [start]
    for m in moves:
        i = (i + {'R': 1, 'L': -1, 'B': 2}[m]) % 4
        path.append(DIRS[i])
    return DIRS[i], {'path': ', then '.join(path)}


def _cond(c, n):
    t = c[0]
    if t == 'even':
        return n % 2 == 0
    if t == 'odd':
        return n % 2 == 1
    if t == 'gt':
        return n > c[1]
    if t == 'lt':
        return n < c[1]
    if t == 'multiple':
        return n % c[1] == 0
    raise ValueError(t)


@kind
def filter_count(numbers, conds):
    kept = [n for n in numbers if all(_cond(c, n) for c in conds)]
    return len(kept), {'kept': _j(kept)}


@kind
def venn_both(total, a, b, neither=0):
    inside = total - neither
    return a + b - inside, {'sum': a + b, 'inside': inside}


@kind
def parity(op, parts):
    odds = sum(1 for p in parts if p == 'odd')
    if op == 'sum':
        return ('odd' if odds % 2 else 'even'), {}
    return ('odd' if odds == len(parts) else 'even'), {}


@kind
def regroup(tens, ones, hundreds=0):
    return hundreds * 100 + tens * 10 + ones, {'t': tens * 10, 'o': ones}


@kind
def digit_value_diff(n, i, j):
    s = str(n)
    vi = int(s[i]) * 10 ** (len(s) - 1 - i)
    vj = int(s[j]) * 10 ** (len(s) - 1 - j)
    return vi - vj, {'vi': vi, 'vj': vj}


@kind
def pairs_with_sum(nums, target):
    prs = [(a, b) for a, b in itertools.combinations(nums, 2) if a + b == target]
    return len(prs), {'list': ' and '.join('%d + %d' % x for x in prs)}


@kind
def perm_count(n, k=None):
    k = n if k is None else k
    return math.perm(n, k), {}


@kind
def cards_sum(digits, shape, ask):
    best = None
    for perm in itertools.permutations(digits):
        if perm[0] == 0 and shape[0] > 1:
            continue
        nums, at = [], 0
        for w in shape:
            nums.append(int(''.join(map(str, perm[at:at + w]))))
            at += w
        if any(len(str(x)) != w for x, w in zip(nums, shape)):
            continue
        tot = sum(nums)
        if best is None or (ask == 'max' and tot > best[0]) or (ask == 'min' and tot < best[0]):
            best = (tot, nums)
    return best[0], {'nums': ' + '.join(str(x) for x in best[1])}


@kind
def position_from_back(total, k):
    return total - k + 1, {}


@kind
def pyramid(bottom, ask, top=None, hide=None):
    n = len(bottom)
    coef = [math.comb(n - 1, i) for i in range(n)]
    if ask == 'top':
        return sum(c * b for c, b in zip(coef, bottom)), {'row2': _j(bottom[i] + bottom[i + 1] for i in range(n - 1))}
    known = sum(c * b for i, (c, b) in enumerate(zip(coef, bottom)) if i != hide)
    v = Fr(top - known, coef[hide])
    assert v == int(v)
    return int(v), {'coef': coef[hide]}


@kind
def age_gap(a, gap, when):
    return when + gap, {'now': a + gap, 'years': when - a}


@kind
def equal_sides(left, right):
    return sum(left) - sum(right), {'total': sum(left)}


@kind
def climb_slip(height, up, down):
    day = math.ceil((height - up) / (up - down)) + 1 if height > up else 1
    return day, {}


@kind
def equalise(a, b):
    assert (a - b) % 2 == 0
    return (a - b) // 2, {'gap': a - b, 'each': (a + b) // 2}


@kind
def missing_digit(eq):
    hits = [d for d in range(10) if _eval_eq(eq.replace('?', str(d)))]
    assert len(hits) == 1, hits
    return hits[0], {}


def _eval_eq(s):
    import re
    s = re.sub(r'\d+', lambda m: str(int(m.group(0))), s)      # '05' is not a valid literal
    lhs, rhs = s.split('=')
    return eval(lhs.replace('x', '*')) == eval(rhs.replace('x', '*'))


SOLVE_NAMES = list(SOLVE)
