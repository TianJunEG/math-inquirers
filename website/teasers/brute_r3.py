"""INDEPENDENT checker side, part 4 (fix round 3).  Never imports kinds.py, kinds_more.py, kinds_r2.py or kinds_r3.py.

BRUTE[kind](**params) walks the whole search space (simulation, enumeration, search) and returns the SET of all answers that
satisfy the puzzle; verify_bank.py requires exactly one value equal to the bank's answer.  When the puzzle itself is not well
posed (two different solutions) the checker returns an extra impossible value so the verifier reports it as 'valid answers: 2'.
Merged into brute.BRUTE at the bottom of brute.py."""
import itertools
from collections import deque
from fractions import Fraction as Fr

BRUTE = {}
BAD = '#NOT-UNIQUE#'


def brute(fn):
    BRUTE[fn.__name__[2:]] = fn
    return fn


@brute
def b_intervals(n1, t1, n2):
    out = set()
    for gap in range(1, t1 + 1):
        times = [i * gap for i in range(n1)]          # n1 strikes, one every `gap`
        if times[-1] - times[0] == t1:
            out.add((n2 - 1) * gap)
    return out or {BAD}


@brute
def b_unit_compare(dens, names, ask):
    if ask == 'fit':
        a, b = dens
        pieces, got = 0, Fr(0)
        while got < Fr(1, a):
            got += Fr(1, b)
            pieces += 1
        return {pieces} if got == Fr(1, a) else {BAD}
    sizes = [(Fr(1, d), n) for d, n in zip(dens, names)]
    best = max(s for s, _ in sizes) if ask == 'most' else min(s for s, _ in sizes)
    return {n for s, n in sizes if s == best}


@brute
def b_weeks_days(mode, w=0, d=0, n=0):
    def split(days):
        weeks = left = 0
        for _ in range(days):
            left += 1
            if left == 7:
                weeks, left = weeks + 1, 0
        return weeks, left
    if mode == 'total':
        return {sum(1 for _ in range(w) for _ in range(7)) + d}
    if mode == 'rest':
        return {split(n)[1]}
    if mode == 'weeks':
        return {split(n)[0]}
    wk = sum(7 for _ in range(w)) + d
    return {wk - n}


@brute
def b_swaps(order):
    start = tuple(order)
    goal = tuple(sorted(order))
    if len(set(order)) != len(order):
        return {BAD}
    seen = {start: 0}
    dq = deque([start])
    while dq:
        cur = dq.popleft()
        if cur == goal:
            return {seen[cur]}
        for i in range(len(cur) - 1):
            nxt = list(cur)
            nxt[i], nxt[i + 1] = nxt[i + 1], nxt[i]
            nxt = tuple(nxt)
            if nxt not in seen:
                seen[nxt] = seen[cur] + 1
                dq.append(nxt)
    return {BAD}


@brute
def b_overlap_chain(ask, n=None, length=None, overlap=None, total=None):
    def span(k):
        end = 0
        for i in range(k):
            start = 0 if i == 0 else end - overlap
            end = start + length
        return end
    if ask == 'total':
        return {span(n)}
    return {k for k in range(1, 400) if span(k) == total} or {BAD}


@brute
def b_ferry_trips(people, cap):
    # state: (people still on the start bank, boat on the start bank?)
    start = (people, True)
    seen = {start: 0}
    dq = deque([start])
    while dq:
        left, here = dq.popleft()
        if left == 0:
            return {seen[(left, here)]}
        avail = left if here else people - left
        for k in range(1, min(cap, avail) + 1):
            nxt = (left - k, False) if here else (left + k, True)
            if nxt not in seen:
                seen[nxt] = seen[(left, here)] + 1
                dq.append(nxt)
    return {BAD}


@brute
def b_dice_ways(sides, total, ordered):
    pairs = [(a, b) for a in range(1, sides + 1) for b in range(1, sides + 1) if a + b == total]
    if ordered:
        return {len(pairs)}
    return {len({tuple(sorted(p)) for p in pairs})}


@brute
def b_checkerboard(rows, cols, ask):
    dark = light = edge = 0
    for r in range(rows):
        for c in range(cols):
            is_dark = (r + c) % 2 == 0
            dark += is_dark
            light += not is_dark
            if is_dark and (r in (0, rows - 1) or c in (0, cols - 1)):
                edge += 1
    return {{'dark': dark, 'light': light, 'edge_dark': edge}[ask]}


@brute
def b_equal_marks(start, end, marks, k, ask):
    pos = [start + Fr(i * (end - start), marks - 1) for i in range(marks)]
    if any(p.denominator != 1 for p in pos):
        return {BAD}
    if ask == 'step':
        return {pos[1] - pos[0]}
    return {pos[k - 1]}


@brute
def b_sum_later(a, b, target):
    out = set()
    for y in range(1, 200):
        if (a + y) + (b + y) == target:
            out.add(y)
    return out or {BAD}


@brute
def b_order_by_key(numbers, rule, place):
    def key(n):
        total, prod = 0, 1
        while n:
            n, d = divmod(n, 10)
            total += d
            prod *= d
        return total if rule == 'digit_sum' else prod
    keyed = [(key(n), n) for n in numbers]
    if len({k for k, _ in keyed}) != len(keyed):
        return {BAD}
    rank = {n: sum(1 for k2, _ in keyed if k2 < k) + 1 for k, n in keyed}
    return {n for n, r in rank.items() if r == place}


_W = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
      'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']


@brute
def b_alpha_numbers(lo, hi, place):
    items = [(_W[n - 1], n) for n in range(lo, hi + 1)]

    def before(a, b):          # dictionary order, letter by letter
        for x, y in zip(a, b):
            if x != y:
                return x < y
        return len(a) < len(b)
    rank = {n: sum(1 for w2, _ in items if before(w2, w)) + 1 for w, n in items}
    return {n for n, r in rank.items() if r == place}


@brute
def b_alt_steps(start, deltas, ask, n=None, target=None):
    v = start
    if ask == 'after':
        for i in range(n):
            v += deltas[i % len(deltas)]
        return {v}
    for i in range(1, 5000):
        v += deltas[(i - 1) % len(deltas)]
        if v >= target:
            return {i}
    return {BAD}


@brute
def b_pass_places(start, moves, total, ask):
    line = ['r%d' % i for i in range(1, total + 1)]
    me = line.pop(start - 1)
    line.insert(start - 1, me)
    for kind_, k in moves:
        i = line.index(me)
        for _ in range(k):
            i = line.index(me)
            j = i - 1 if kind_ == 'pass' else i + 1
            line[i], line[j] = line[j], line[i]
    place = line.index(me) + 1
    return {place if ask == 'place' else total - place}


@brute
def b_displacement(moves):
    x = y = 0
    for d, k in moves:
        for _ in range(k):
            if d == 'N':
                y += 1
            elif d == 'S':
                y -= 1
            elif d == 'E':
                x += 1
            else:
                x -= 1
    # shortest walk back along the streets (grid lines), by search
    seen = {(x, y): 0}
    dq = deque([(x, y)])
    while dq:
        c = dq.popleft()
        if c == (0, 0):
            return {seen[c]} if (x, y) != (0, 0) else {BAD}
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nc = (c[0] + dx, c[1] + dy)
            if nc not in seen and abs(nc[0]) <= 60 and abs(nc[1]) <= 60:
                seen[nc] = seen[c] + 1
                dq.append(nc)
    return {BAD}


@brute
def b_schedule_breaks(start_h, start_m, parts, part_min, break_min, ask):
    clock = start_h * 60 + start_m
    t0 = clock
    for i in range(parts):
        clock += part_min
        if i != parts - 1:
            clock += break_min
    if ask == 'total':
        return {clock - t0}
    clock %= 1440
    return {(clock // 60) * 100 + clock % 60}


@brute
def b_reverse_division(divisor, quotient, remainder, ask, add=0):
    cands = [n for n in range(0, divisor * (quotient + 2) + 5) if n // divisor == quotient and n % divisor == remainder]
    if len(cands) != 1:
        return {BAD}
    n = cands[0]
    return {n} if ask == 'number' else {(n + add) // divisor}


@brute
def b_fake_coin(ask, n=None, w=None):
    # with k weighings, can a group of m coins (one heavier) be searched?  Put a coins on each pan.
    memo = {}

    def ok(m, k):
        if m <= 1:
            return True
        if k == 0:
            return False
        if (m, k) in memo:
            return memo[(m, k)]
        res = False
        for a in range(1, m // 2 + 1):
            # lighter pan up => fake is among the heavier pan's a coins; balance => among the m - 2a left aside
            if ok(a, k - 1) and ok(m - 2 * a, k - 1):
                res = True
                break
        memo[(m, k)] = res
        return res
    if ask == 'max_coins':
        m = 1
        while ok(m + 1, w):
            m += 1
        return {m}
    k = 0
    while not ok(n, k):
        k += 1
    return {k}


@brute
def b_mirror_time(h, m, ask):
    hour_angle = Fr(30 * (h % 12)) + Fr(m, 2)
    min_angle = Fr(6 * m)
    rh, rm = (360 - hour_angle) % 360, (360 - min_angle) % 360
    real_min = rm / 6
    real_hour = int(rh // 30) or 12
    if real_min.denominator != 1:
        return {BAD}
    return {real_hour if ask == 'hour' else int(real_min)}


@brute
def b_swap_digits(ask, number=None, pos=None, diff=None, t=None, h=None):
    if ask == 'difference':
        n = len(str(number))
        i, j = pos
        di = (number // 10 ** (n - 1 - i)) % 10
        dj = (number // 10 ** (n - 1 - j)) % 10
        return {abs((di - dj) * (10 ** (n - 1 - j) - 10 ** (n - 1 - i)))}
    out = set()
    for num in range(100, 1000):
        hh, tt, oo = num // 100, num // 10 % 10, num % 10
        if hh == h and tt == t and (oo * 100 + tt * 10 + hh) - num == diff:
            out.add(num)
    return out or {BAD}


@brute
def b_notch_perimeter(w, h, notches, unit):
    cells = {(x, y) for x in range(w) for y in range(h)}
    for corner, a, b in notches:
        xs = range(0, a) if corner[1] == 'l' else range(w - a, w)
        ys = range(0, b) if corner[0] == 'b' else range(h - b, h)
        for x in xs:
            for y in ys:
                cells.discard((x, y))
    edges = 0
    for (x, y) in cells:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if (x + dx, y + dy) not in cells:
                edges += 1
    return {edges * unit}


@brute
def b_container_mass(full, part, num, den, ask):
    out = set()
    for jar in range(0, full + 1):
        contents = full - jar
        if Fr(contents) * Fr(num, den) + jar == part:
            out.add(jar if ask == 'jar' else contents)
    return out or {BAD}


@brute
def b_missing_term(n, got):
    out = set()
    for k in range(1, n + 1):
        if sum(i for i in range(1, n + 1) if i != k) == got:
            out.add(k)
    return out or {BAD}


@brute
def b_jug_steps(a, b, target):
    best = {}

    def go(x, y, depth, limit):
        if x == target or y == target:
            return True
        if depth == limit:
            return False
        if best.get((x, y), 99) <= depth:
            return False
        best[(x, y)] = depth
        moves = {(a, y), (x, b), (0, y), (x, 0),
                 (max(0, x - (b - y)), min(b, y + x)), (min(a, x + y), max(0, y - (a - x)))}
        return any(go(nx, ny, depth + 1, limit) for nx, ny in moves)
    for limit in range(1, 25):
        best.clear()
        if go(0, 0, 0, limit):
            return {limit}
    return {BAD}


@brute
def b_euler_lifts(edges):
    n = len(edges)
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def trail(v, mask):
        if mask == 0:
            return True
        for i in range(n):
            if mask >> i & 1:
                a, b = edges[i]
                if a == v and trail(b, mask ^ (1 << i)):
                    return True
                if b == v and trail(a, mask ^ (1 << i)):
                    return True
        return False
    verts = {x for e in edges for x in e}

    def coverable(mask):
        return any(trail(v, mask) for v in verts)
    full = (1 << n) - 1
    best = {0: 0}

    def strokes(mask):
        if mask in best:
            return best[mask]
        low = mask & -mask            # the stroke that covers the lowest edge
        res = 99
        sub = mask
        while sub:
            if sub & low and coverable(sub):
                res = min(res, 1 + strokes(mask ^ sub))
            sub = (sub - 1) & mask
        best[mask] = res
        return res
    return {strokes(full) - 1}


@brute
def b_diagonal_squares(w, h):
    count = 0
    for i in range(w):
        for j in range(h):
            # on the diagonal y = h x / w the square (i, j) is crossed inside when the line is strictly inside it somewhere
            ylo, yhi = Fr(h * i, w), Fr(h * (i + 1), w)
            if ylo < j + 1 and yhi > j:
                count += 1
    return {count}


def _sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def _add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def _dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def _cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def _turn90(v, axis_dir, sign):
    """Rotate vector v by sign*90 degrees about the (unit, axis-aligned) direction axis_dir."""
    c = _cross(axis_dir, v)
    k = _dot(axis_dir, v)
    return tuple(axis_dir[i] * k + sign * c[i] for i in range(3))


@brute
def b_net_opposite(cells, ask):
    cells = {n: tuple(c) for n, c in cells.items()}
    names = list(cells)
    pos = {c: n for n, c in cells.items()}
    # every cell is a unit square; keep its four corners in 3D and its centre
    def corners(c):
        x, y = c
        return [(2 * x, 2 * y, 0), (2 * x + 2, 2 * y, 0), (2 * x + 2, 2 * y + 2, 0), (2 * x, 2 * y + 2, 0)]
    root = names[0]
    rx, ry = cells[root]
    centre = (2 * rx + 1, 2 * ry + 1, 1)                         # centre of the folded cube (side 2)
    tree = {root: None}
    order = [root]
    for n in order:
        cx, cy = cells[n]
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nb = pos.get((cx + dx, cy + dy))
            if nb and nb not in tree:
                tree[nb] = n
                order.append(nb)
    kids = {n: [m for m in order if tree[m] == n] for n in order}

    flat = {n: corners(cells[n]) for n in names}
    moved = {n: list(flat[n]) for n in names}                   # current 3D corners of each cell (changes while folding)
    # Apply folds from the root outwards: a child (with all its descendants) turns 90 degrees about the hinge it shares with its parent.
    def descendants(n):
        out = [n]
        for m in kids[n]:
            out += descendants(m)
        return out

    def fold_child(parent, child):
        hinge = [p for p in flat[child] if p in flat[parent]]       # two flat corners shared by the two cells
        idx = [(flat[child].index(p)) for p in hinge]
        pidx = [(flat[parent].index(p)) for p in hinge]
        a, b = moved[parent][pidx[0]], moved[parent][pidx[1]]       # where that edge is now (the parent may already be folded)
        d = _sub(b, a)
        axis = tuple((x // 2 if x else 0) for x in d)               # unit direction (edge length is 2 in doubled coordinates)
        best = None
        for sign in (1, -1):
            trial = {}
            for m in descendants(child):
                trial[m] = [_add(a, _turn90(_sub(p, a), axis, sign)) for p in moved[m]]
            c = tuple(Fr(sum(trial[child][k][i] for k in range(4)), 4) for i in range(3))
            dist2 = sum((c[i] - centre[i]) ** 2 for i in range(3))
            if dist2 == 1:                                          # a cube face centre is exactly one (half side) from the centre
                best = trial
        assert best is not None
        for m, v in best.items():
            moved[m] = v

    for n in order:
        for m in kids[n]:
            fold_child(n, m)
    normals = {}
    for n in names:
        c = tuple(Fr(sum(moved[n][k][i] for k in range(4)), 4) for i in range(3))
        normals[n] = tuple(int(c[i] - centre[i]) for i in range(3))
    if len(set(normals.values())) != 6:
        return {BAD}
    me = normals[ask]
    return {n for n in names if normals[n] == tuple(-x for x in me)}


@brute
def b_symmetry_add(grid, axis):
    h, w = len(grid), len(grid[0])
    shaded = {(y, x) for y in range(h) for x in range(w) if grid[y][x] == '#'}
    free = [(y, x) for y in range(h) for x in range(w) if (y, x) not in shaded]

    def mirror(c):
        y, x = c
        return (y, w - 1 - x) if axis == 'vertical' else (h - 1 - y, x)
    best = None
    for r in range(len(free) + 1):
        for extra in itertools.combinations(free, r):
            s = shaded | set(extra)
            if all(mirror(c) in s for c in s):
                best = r
                break
        if best is not None:
            break
    return {best}


@brute
def b_venn3(total, a, b, c, ab, ac, bc, abc, ask):
    only_ab, only_ac, only_bc = ab - abc, ac - abc, bc - abc
    only_a = a - only_ab - only_ac - abc
    only_b = b - only_ab - only_bc - abc
    only_c = c - only_ac - only_bc - abc
    regions = [only_a, only_b, only_c, only_ab, only_ac, only_bc, abc]
    if min(regions) < 0:
        return {BAD}
    union = sum(regions)
    none = total - union
    if none < 0:
        return {BAD}
    return {{'none': none, 'union': union, 'only_one': only_a + only_b + only_c}[ask]}


@brute
def b_cut_corners_area(w, h, cuts, unit=1):
    pts = []
    spec = list(cuts) + [None] * (4 - len(cuts))
    bl, br, tr, tl = spec
    pts += [(0, bl[1]), (bl[0], 0)] if bl else [(0, 0)]
    pts += [(w - br[0], 0), (w, br[1])] if br else [(w, 0)]
    pts += [(w, h - tr[1]), (w - tr[0], h)] if tr else [(w, h)]
    pts += [(tl[0], h), (0, h - tl[1])] if tl else [(0, h)]
    s = 0
    for i in range(len(pts)):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % len(pts)]
        s += x1 * y2 - x2 * y1
    area = Fr(abs(s), 2)
    if area.denominator != 1:
        return {BAD}
    return {int(area) * unit * unit}


@brute
def b_combined_mean(groups, ask, overall=None):
    if ask == 'mean':
        values = [g[1] for g in groups for _ in range(g[0])]
        m = Fr(sum(values), len(values))
        return {int(m)} if m.denominator == 1 else {BAD}
    out = set()
    n = sum(g[0] for g in groups)
    for last in range(0, 1000):
        values = [g[1] for g in groups[:-1] for _ in range(g[0])] + [last] * groups[-1][0]
        if Fr(sum(values), n) == overall:
            out.add(last)
    return out or {BAD}


@brute
def b_ratio_change(mode, a, b, c, d, k, ask):
    out = set()
    for u in range(1, 3000):
        first, second = a * u, b * u
        if mode == 'add':
            ok = (first + k) * d == c * second
        else:
            ok = d * (first - k) == c * (second + k) and first - k >= 0
        if ok:
            out.add({'first': first, 'second': second, 'total': first + second, 'unit': u}[ask])
    return out or {BAD}


@brute
def b_share_fraction(num, den, people):
    out = set()
    for d in range(1, 400):
        for n in range(0, d + 1):
            if Fr(n, d) * people == Fr(num, den):
                out.add(Fr(n, d))
    return {min(out)} if out else {BAD}


@brute
def b_branch_prog(start, n, even_op, odd_op):
    def line(op):
        k, v = op
        return {'half': 'x = x // 2', 'add': 'x = x + %d' % v, 'sub': 'x = x - %d' % v, 'times3plus1': 'x = 3 * x + 1'}[k]
    src = 'x = %d\nfor _ in range(%d):\n    if x %% 2 == 0:\n        %s\n    else:\n        %s\n' % (start, n, line(even_op), line(odd_op))
    ns = {}
    exec(src, {}, ns)
    return {ns['x']}


@brute
def b_faulty_clock(g, clock_min):
    out = set()
    for real in range(0, 5000):
        shown = Fr(real * (60 + g), 60)
        if shown == clock_min:
            out.add(real)
    return out or {BAD}


@brute
def b_triangle_sides(first, ask, side):
    nums = range(first, first + 6)
    seen = set()
    for p in itertools.permutations(nums):
        c1, c2, c3, m12, m23, m13 = p
        if c1 + m12 + c2 == side and c2 + m23 + c3 == side and c3 + m13 + c1 == side:
            seen.add(c1 + c2 + c3 if ask == 'corner_sum' else (max(c1, c2, c3) if ask == 'largest_corner' else min(m12, m23, m13)))
    return seen or {BAD}


@brute
def b_digit_segments(lo, hi, table):
    return {sum(table[ch] for n in range(lo, hi + 1) for ch in '%d' % n)}


@brute
def b_circle_out(n, k):
    # the children are seated one after another: simulate with a queue that rotates
    q = deque(range(1, n + 1))
    while len(q) > 1:
        q.rotate(-(k - 1))
        q.popleft()
    return {q[0]}
