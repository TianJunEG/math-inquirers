"""INDEPENDENT checker side, part 3 (fix round 2).  Never imports kinds.py, kinds_more.py or kinds_r2.py.

BRUTE[kind](**params) walks the whole search space and returns the SET of all answers that satisfy the puzzle;
verify_bank.py requires exactly one value equal to the bank's answer.  When the puzzle itself is not well posed
(two different solutions) the checker returns an extra impossible value so the verifier reports it as 'valid answers: 2'.
Merged into brute.BRUTE at the bottom of brute.py."""
import itertools
import math
import re
from fractions import Fraction as Fr

BRUTE = {}
BAD = '#NOT-UNIQUE#'


def brute(fn):
    BRUTE[fn.__name__[2:]] = fn
    return fn


# ================================================================== cards, coins, number sense
@brute
def b_triple_sum(cards, target, ask):
    out, found = set(), 0
    n = len(cards)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if cards[i] + cards[j] + cards[k] == target:
                    found += 1
                    t = sorted((cards[i], cards[j], cards[k]))
                    out.add(t[{'smallest': 0, 'middle': 1, 'largest': 2}[ask]])
    if found != 1:
        out.add(BAD)
    return out


@brute
def b_coin_amounts(coins):
    seen = set()
    for size in range(1, len(coins) + 1):
        for combo in itertools.combinations(range(len(coins)), size):
            seen.add(sum(coins[i] for i in combo))
    return {len(seen)}


@brute
def b_cannot_pay(coins, amounts):
    count = 0
    for a in amounts:
        # try every number of the first coin, then check the rest by recursion
        def can(rest, cs):
            if rest == 0:
                return True
            if not cs:
                return False
            c = cs[0]
            return any(can(rest - c * k, cs[1:]) for k in range(rest // c + 1))
        if can(a, list(coins)):
            count += 1
    return {count}


@brute
def b_halfway(a, b):
    hits = [x for x in range(min(a, b) - 1, max(a, b) + 2) if x - a == b - x]
    return set(hits) if hits else {BAD}


@brute
def b_odd_one_out(numbers):
    cands = set()
    for x in numbers:
        rest = [y for y in numbers if y is not x]
        for k in range(2, 11):
            if all(y % k == 0 for y in rest) and x % k != 0:
                cands.add(x)
    return cands if cands else {BAD}


@brute
def b_page_digits(lo, hi):
    return {len(''.join(str(n) for n in range(lo, hi + 1)))}


@brute
def b_number_words(lo, hi):
    ones = 'one two three four five six seven eight nine'.split()
    teens = 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
    tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
    total = 0
    for n in range(lo, hi + 1):
        if n == 100:
            w = 'one hundred'
        elif n < 10:
            w = ones[n - 1]
        elif n < 20:
            w = teens[n - 10]
        else:
            w = tens[n // 10] + ('-' + ones[n % 10 - 1] if n % 10 else '')
        total += len(re.findall('[a-z]', w))
    return {total}


@brute
def b_hundred_chart(start, moves):
    pos = ((start - 1) // 10, (start - 1) % 10)
    for d, k in moves:
        dr, dc = {'down': (1, 0), 'up': (-1, 0), 'right': (0, 1), 'left': (0, -1)}[d]
        for _ in range(k):
            pos = (pos[0] + dr, pos[1] + dc)
            if not (0 <= pos[0] < 10 and 0 <= pos[1] < 10):
                return {BAD}
    return {pos[0] * 10 + pos[1] + 1}


@brute
def b_days_in_common(r1, r2):
    return {len(set(range(r1[0], r1[1] + 1)) & set(range(r2[0], r2[1] + 1)))}


@brute
def b_fan_triangles(n):
    # the fan is cut into n thin triangles; a triangle in the picture is any run of neighbouring thin triangles
    runs = 0
    for start in range(n):
        for end in range(start, n):
            runs += 1
    return {runs}


@brute
def b_function_machine(pairs, x, forms):
    outs = set()
    for a in range(1, 13):
        for b in range(-30, 31):
            kinds_ = set()
            if a == 1 and b != 0:
                kinds_.add('add')
            if b == 0 and a > 1:
                kinds_.add('mul')
            if a > 1 and b != 0:
                kinds_.add('both')
            if not (kinds_ & set(forms)):
                continue
            if all(a * i + b == o for i, o in pairs):
                outs.add(a * x + b)
    return outs if outs else {BAD}


# ================================================================== time
@brute
def b_clock_hand(h, m, add, ask):
    hour, minute = h, m
    for _ in range(add):
        minute += 1
        if minute == 60:
            minute = 0
            hour = hour % 12 + 1
    if minute % 5:
        return {BAD}
    if ask == 'number':
        # the minute hand points at number minute / 5, and at 12 when it is straight up
        return {minute // 5 if minute else 12}
    return {{'minutes': minute, 'hour': hour}[ask]}


@brute
def b_am_pm(times, ask):
    def minutes(h, ap):
        return ((h % 12) + (12 if ap == 'pm' else 0)) * 60
    ts = [(minutes(h, ap), '%d %s' % (h, ap)) for h, ap in times]
    if ask == 'latest':
        top = max(t for t, _ in ts)
        return {name for t, name in ts if t == top}
    if ask == 'earliest':
        low = min(t for t, _ in ts)
        return {name for t, name in ts if t == low}
    start, end = ts[0][0], ts[1][0]
    if end <= start:
        end += 24 * 60
    return {(end - start) // 60}


@brute
def b_date_after(month, day, add):
    names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    days_in = dict(zip(names, [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]))
    m, d = month, day
    for _ in range(add):
        d += 1
        if d > days_in[m]:
            d = 1
            m = names[(names.index(m) + 1) % 12]
    return {d}


@brute
def b_timetable_wait(first, every, now):
    departures = set(range(first, 24 * 60, every))
    t = now
    while t not in departures:
        t += 1
    return {t - now}


# ================================================================== shapes and arrangements
@brute
def b_shape_riddle(pool, clue):
    # a shape fits the clue if its full description agrees with every clue given (unlisted facts are not constrained)
    full2 = {'circle': dict(straight=0, curved=1), 'triangle': dict(straight=3, curved=0), 'square': dict(straight=4, curved=0, equal=True),
             'rectangle': dict(straight=4, curved=0, equal=False), 'half circle': dict(straight=1, curved=1), 'quarter circle': dict(straight=2, curved=1)}
    full3 = {'cube': dict(flat=6, curved=0, vertices=8, same=True), 'cuboid': dict(flat=6, curved=0, vertices=8, same=False),
             'cone': dict(flat=1, curved=1, vertices=1), 'cylinder': dict(flat=2, curved=1, vertices=0), 'sphere': dict(flat=0, curved=1, vertices=0)}
    full = full2 if pool == '2d' else full3
    hits = set()
    for name, desc in full.items():
        if all(desc.get(k, None) == v for k, v in clue.items()):
            hits.add(name)
    return hits if hits else {BAD}


@brute
def b_seat_number(per_row, ask, row=None, col=None, seat=None):
    seats = []
    for r in range(1, 40):
        for c in range(1, per_row + 1):
            seats.append((r, c))
    if ask == 'seat':
        return {seats.index((row, col)) + 1}
    r, c = seats[seat - 1]
    return {r if ask == 'row' else c}


@brute
def b_circle_opposite(n, a, ask):
    ring = list(range(1, n + 1))
    i = ring.index(a)
    opp = ring[(i + n // 2) % n]
    if ask == 'opposite':
        return {opp}
    # children standing strictly between a and its opposite, going one way round
    j = ring.index(opp)
    between = [ring[k % n] for k in range(i + 1, i + 1 + ((j - i) % n) - 1)]
    return {len(between)}


@brute
def b_border_tiles(n, m):
    return {sum(1 for r in range(n) for c in range(m) if r in (0, n - 1) or c in (0, m - 1))}


@brute
def b_square_stack(n):
    cubes = 0
    for layer in range(1, n + 1):
        for _r in range(layer):
            for _c in range(layer):
                cubes += 1
    return {cubes}


@brute
def b_dice_opposite(vals, ask):
    pairs = {1: 6, 6: 1, 2: 5, 5: 2, 3: 4, 4: 3}
    if ask == 'bottoms':
        return {sum(pairs[v] for v in vals)}
    faces = {1, 2, 3, 4, 5, 6}
    # the faces seen at one corner are three that touch each other: no two of them are opposite
    if any(pairs[a] == b for a in vals for b in vals):
        return {BAD}
    return {sum(faces - set(vals))}


@brute
def b_polyomino(n):
    def norm(cells):
        mx = min(x for x, y in cells)
        my = min(y for x, y in cells)
        return tuple(sorted((x - mx, y - my) for x, y in cells))

    def variants(cells):
        out = []
        cur = list(cells)
        for _ in range(4):
            cur = [(y, -x) for x, y in cur]
            out.append(norm(cur))
            out.append(norm([(-x, y) for x, y in cur]))
        return min(out)
    shapes = {variants([(0, 0)])}
    for _ in range(n - 1):
        nxt = set()
        for s in shapes:
            for (x, y) in s:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    c = (x + dx, y + dy)
                    if c not in s:
                        nxt.add(variants(list(s) + [c]))
        shapes = nxt
    return {len(shapes)}


@brute
def b_fold_cut(folds):
    # a strip of length 2**folds is folded in half `folds` times (x -> min(x, L - x)); one cut is made across the middle
    # of the folded bundle; count the cut points on the opened strip (work in half units)
    length = 2 ** folds
    cuts = 0
    for u in range(1, 2 * length):         # u/2 = position along the strip, strictly inside
        x, L = Fr(u, 2), Fr(length)
        for _ in range(folds):
            x = min(x, L - x)
            L = L / 2
        if x == L / 2:
            cuts += 1
    return {cuts + 1}


# ================================================================== logic
@brute
def b_grid_totals(rows, cols, known, ask):
    R, C = len(rows), len(cols)
    fixed = {(r, c): v for r, c, v in known}
    free = [(r, c) for r in range(R) for c in range(C) if (r, c) not in fixed]
    out = set()
    count = [0]

    def fill(i, grid, rrem, crem):
        if i == len(free):
            if all(x == 0 for x in rrem) and all(x == 0 for x in crem):
                count[0] += 1
                out.add(grid[tuple(ask)])
            return
        r, c = free[i]
        # every whole number that does not push a row or column total over its limit
        for v in range(0, min(rrem[r], crem[c]) + 1):
            grid[(r, c)] = v
            rrem[r] -= v
            crem[c] -= v
            fill(i + 1, grid, rrem, crem)
            rrem[r] += v
            crem[c] += v
        del grid[(r, c)]
    rrem, crem = list(rows), list(cols)
    grid = dict(fixed)
    for (r, c), v in fixed.items():
        rrem[r] -= v
        crem[c] -= v
    if min(rrem + crem) < 0:
        return {BAD}
    fill(0, grid, rrem, crem)
    if count[0] != 1:
        out.add(BAD)
    return out


@brute
def b_symbols(eqs, ask, maxv):
    names = sorted({s for terms, _ in eqs for s in terms})
    out = set()
    count = 0
    for vals in itertools.product(range(1, maxv + 1), repeat=len(names)):
        env = dict(zip(names, vals))
        if all(sum(c * env[s] for s, c in terms.items()) == tot for terms, tot in eqs):
            count += 1
            out.add(env[ask])
    if count != 1:
        out.add(BAD)
    return out


@brute
def b_insert_signs(nums, target):
    n = 0
    for signs in itertools.product((1, -1), repeat=len(nums) - 1):
        total = nums[0]
        for s, x in zip(signs, nums[1:]):
            total += s * x
        if total == target:
            n += 1
    return {n}


@brute
def b_knockout(n):
    players = list(range(n))
    matches = 0
    while len(players) > 1:
        nxt = []
        for i in range(0, len(players) - 1, 2):
            matches += 1
            nxt.append(players[i])       # the winner goes on
        if len(players) % 2:
            nxt.append(players[-1])      # a bye
        players = nxt
    return {matches}


@brute
def b_snaps(rows, cols):
    pieces = [(rows, cols)]
    snaps = 0
    while any(r * c > 1 for r, c in pieces):
        r, c = next(p for p in pieces if p[0] * p[1] > 1)
        pieces.remove((r, c))
        if r > 1:
            pieces += [(r // 2, c), (r - r // 2, c)]
        else:
            pieces += [(1, c // 2), (1, c - c // 2)]
        snaps += 1
    return {snaps}


@brute
def b_latin_square(n, given, ask):
    rows = list(itertools.permutations(range(1, n + 1)))
    fixed = {(r, c): v for r, c, v in given}
    out, count = set(), 0
    for grid in itertools.product(rows, repeat=n):
        if any(len({grid[r][c] for r in range(n)}) != n for c in range(n)):
            continue
        if all(grid[r][c] == v for (r, c), v in fixed.items()):
            count += 1
            out.add(grid[ask[0]][ask[1]])
    if count != 1:
        out.add(BAD)
    return out


@brute
def b_worst_case(counts, need, ask):
    if ask == 'k_alike':
        best = 0
        for draw in itertools.product(*[range(c + 1) for c in counts]):
            if all(d < need for d in draw):
                best = max(best, sum(draw))
        return {best + 1}
    # guarantee at least one of every colour: find the largest draw that misses some colour
    best = 0
    for draw in itertools.product(*[range(c + 1) for c in counts]):
        if any(d == 0 for d in draw):
            best = max(best, sum(draw))
    return {best + 1}


@brute
def b_take_away_game(total, m):
    win = {0: False}
    for n in range(1, total + 1):
        win[n] = any(not win[n - k] for k in range(1, m + 1) if n - k >= 0)
    moves = [k for k in range(1, m + 1) if total - k >= 0 and not win[total - k]]
    return set(moves) if len(moves) == 1 else {BAD}


@brute
def b_network_shortest(edges, a, b):
    adj = {}
    for x, y, w in edges:
        adj.setdefault(x, []).append((y, w))
        adj.setdefault(y, []).append((x, w))
    best = []

    def walk(u, seen, dist):
        if u == b:
            best.append(dist)
            return
        for v, w in adj.get(u, []):
            if v not in seen:
                walk(v, seen | {v}, dist + w)
    walk(a, {a}, 0)
    return {min(best)} if best else {BAD}


@brute
def b_sum_product(s, p, ask):
    pairs = [(x, y) for x in range(1, s) for y in range(x, s) if x + y == s and x * y == p]
    if len(pairs) != 1:
        return {BAD}
    return {pairs[0][1] if ask == 'larger' else pairs[0][0]}


@brute
def b_heads_legs(heads, legs, a, b):
    sols = [(x, y) for x in range(heads + 1) for y in range(heads + 1) if x + y == heads and a * x + b * y == legs]
    return {sols[0][1]} if len(sols) == 1 else {BAD}


@brute
def b_bar_three(extras, total, ask):
    outs = set()
    for base in range(1, total + 1):
        vals = [base] + [base + e for e in extras]
        if sum(vals) == total:
            outs.add({'smallest': vals[0], 'largest': max(vals), 'last': vals[-1]}[ask])
    return outs if outs else {BAD}


@brute
def b_compound_units(unit, a, b, op, times=1):
    per = {'m': 100, 'km': 1000, 'kg': 1000, 'L': 1000, 'h': 60}[unit]
    # count in single small units, one by one
    x = a[0] * per + a[1]
    y = b[0] * per + b[1]
    if op == 'sum':
        r = x
        for _ in range(y):
            r += 1
    elif op == 'diff':
        r = x
        for _ in range(y):
            r -= 1
    else:
        r = 0
        for _ in range(times):
            r += x
    return {r}


@brute
def b_best_deal(offers, want, ask):
    costs = []
    for o in offers:
        paid = got = 0
        if o[0] == 'each':
            while got < want:
                got += 1
                paid += o[1]
        elif o[0] == 'pack':
            while got < want:
                got += o[1]
                paid += o[2]
            if got != want:
                return {BAD}
        else:
            buy, get, price = o[1], o[2], o[3]
            while got < want:
                got += buy + get
                paid += buy * price
            if got != want:
                return {BAD}
        costs.append(paid)
    return {abs(costs[0] - costs[1])} if ask == 'saving' else {min(costs)}


@brute
def b_fraction_parts(total, eaten, ask):
    slices = list(range(total))
    for e in eaten:
        for _ in range(e):
            slices.pop()
    left = len(slices)
    if left <= 0:
        return {BAD}
    return {Fr(left, total)} if ask == 'fraction_left' else {left}


# ================================================================== higher-level additions (Levels 3 to 6)
@brute
def b_digit_sum_total(lo, hi):
    total = 0
    for n in range(lo, hi + 1):
        while n:
            total += n % 10
            n //= 10
    return {total}


@brute
def b_round_table(n):
    seen = set()
    for perm in itertools.permutations(range(n)):
        i = perm.index(0)
        seen.add(perm[i:] + perm[:i])     # a round table has no start: turn it so person 0 is first
    return {len(seen)}


@brute
def b_divisible_digit(template, by, ask):
    ok = []
    for d in '0123456789':
        n = int(template.replace('_', d))
        if n % by == 0:
            ok.append(int(d))
    if not ok:
        return {BAD}
    return {{'count': len(ok), 'sum': sum(ok), 'largest': max(ok), 'smallest': min(ok)}[ask]}


@brute
def b_work_time(people, days, new_people):
    for d in range(1, people * days + 1):
        if new_people * d == people * days:
            return {d}
    return {BAD}


@brute
def b_simple_interest(principal, rate_pct, years):
    total = Fr(0)
    for _ in range(years):
        total += Fr(principal) * Fr(rate_pct, 100)
    return {total}


@brute
def b_pie_sector(total, angle):
    hits = [n for n in range(total + 1) if Fr(n, total) == Fr(angle, 360)]
    return set(hits) if hits else {BAD}


@brute
def b_twenty_four(h, ap, m, add_h, add_m):
    minute = ((h % 12) + (12 if ap == 'pm' else 0)) * 60 + m
    for _ in range(add_h * 60 + add_m):
        minute = (minute + 1) % 1440
    return {(minute // 60) * 100 + minute % 60}


@brute
def b_minutes_seconds(songs):
    secs = 0
    for m, s in songs:
        for _ in range(m):
            secs += 60
        secs += s
    return {secs}


@brute
def b_fraction_order(fracs, ask):
    pts = sorted(fracs, key=lambda f: f[0] * 1.0 / f[1])
    pick = {'middle': pts[1], 'greatest': pts[-1], 'least': pts[0]}[ask]
    return {Fr(pick[0], pick[1])}


@brute
def b_improper(whole, num, den):
    pieces = 0
    for _ in range(whole):
        pieces += den
    return {pieces + num}


@brute
def b_profit_pct(cost, sell):
    for p in range(0, 1001):
        if cost + Fr(cost * p, 100) == sell:
            return {Fr(p)}
    return {BAD}
