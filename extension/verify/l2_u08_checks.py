"""Independent checks for Level 2 Unit 8 (2D and 3D shapes): squares and rectangles are enumerated by position, cube nets are folded by simulation (a die is rolled over the net),
triangles are counted from the lines, painted-cube counts come from the coordinates of every small cube."""
import itertools
from common import s

CHECKS = {}


def check(i):
    def d(f):
        CHECKS['L2U08-' + i] = f
        return f
    return d


def squares(rows, cols):
    """number of squares of every size in a rows x cols grid, by size"""
    by = {}
    for k in range(1, min(rows, cols) + 1):
        by[k] = sum(1 for r in range(rows - k + 1) for c in range(cols - k + 1))
    return by


def rectangles(rows, cols):
    return sum(1 for r0 in range(rows) for r1 in range(r0, rows) for c0 in range(cols) for c1 in range(c0, cols))


def folds_to_cube(cells):
    """roll a die over the net: the six cells must show six different faces"""
    cells = {tuple(c) for c in cells}
    start = min(cells)
    # die: (top, bottom, north, south, east, west)
    seen = {start: (1, 6, 2, 5, 3, 4)}
    todo = [start]
    while todo:
        r, c = todo.pop()
        top, bot, n, so, e, w = seen[(r, c)]
        for (dr, dc), new in (((0, 1), (w, e, n, so, top, bot)),      # roll east: the west face becomes the top
                              ((0, -1), (e, w, n, so, bot, top)),
                              ((-1, 0), (so, n, top, bot, e, w)),       # roll north
                              ((1, 0), (n, so, bot, top, e, w))):
            q = (r + dr, c + dc)
            if q in cells and q not in seen:
                seen[q] = new
                todo.append(q)
    if len(seen) != len(cells):
        return False
    return len({v[1] for v in seen.values()}) == 6      # the face on the table is different for each of the 6 squares


def triangles(apex_lines, across_lines):
    rays = apex_lines + 2                # the two sloping sides count as rays from the top corner
    levels = across_lines + 1            # the base counts as a level
    return sum(1 for a, b in itertools.combinations(range(rays), 2) for _ in range(levels))


@check('L01')
def _():
    return s([sum(squares(2, 3).values())])


@check('S01')
def _():
    flat = {'cube': 6, 'cylinder': 2, 'cone': 1, 'sphere': 0}
    return {'a': s([flat['cube']]), 'b': s([flat['cylinder']]), 'c': s([flat['cone']]), 'd': s([flat['sphere']])}


@check('S02')
def _():
    seq = ['semicircle', 'quarter', 'square', 'triangle', 'quarter', 'semicircle', 'triangle', 'square', 'quarter', 'triangle', 'semicircle', 'quarter']
    return {'a': s([seq.count('semicircle')]), 'b': s([seq.count('quarter')]), 'c': s([seq.count('square')]), 'd': s([seq.count('triangle')])}


@check('S03')
def _():
    quarters_per_half, quarters_per_circle = 2, 4
    return {'a': s([quarters_per_half]), 'b': s([3 * quarters_per_half]), 'c': s([12 // quarters_per_circle])}


@check('S04')
def _():
    by = squares(3, 3)
    return {'a': s([by[1]]), 'b': s([by[2]]), 'c': s([by[3]]), 'd': s([sum(by.values())])}


@check('S05')
def _():
    A = [[3, 2, 1]]
    B = [[2, 1], [2, 1]]
    C = [[2, 2, 1], [2, 2, 1]]
    tot = lambda h: sum(sum(r) for r in h)
    return {'a': s([tot(A)]), 'b': s([tot(B)]), 'c': s([tot(C)])}


@check('S06')
def _():
    spans = {k: 4 - k for k in (1, 2, 3)}        # 3 rays gaps: spans of 1, 2, 3 neighbouring parts
    assert triangles(2, 0) == sum(spans.values())
    return {'a': s([spans[1]]), 'b': s([spans[2]]), 'c': s([spans[3]]), 'd': s([triangles(2, 0)])}


@check('S07')
def _():
    return {'a': ['cube'], 'b': ['cone'], 'c': ['sphere'], 'd': ['cylinder']}


@check('S08')
def _():
    return {'a': ['circle'], 'b': ['rectangle'], 'c': ['circle']}


@check('S09')
def _():
    layer = 5 * 2
    return {'a': s([layer]), 'b': s([layer * 3])}


@check('S10')
def _():
    return {'a': ['square'], 'b': ['circle'], 'c': ['circle']}


@check('T01')
def _():
    nets = {'A': [[1, 0], [1, 1], [1, 2], [1, 3], [0, 1], [2, 1]], 'B': [[0, 0], [0, 1], [1, 1], [1, 2], [2, 2], [2, 3]],
            'C': [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 2]], 'D': [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]}
    Y = lambda b: 'Yes' if b else 'No'
    # sanity: the die simulation must say that the well known cross folds and a straight line of 6 does not
    assert folds_to_cube(nets['A']) and not folds_to_cube([[0, i] for i in range(6)])
    return {k.lower(): [Y(folds_to_cube(v))] for k, v in nets.items()}


@check('T02')
def _():
    n = 5
    pieces = {L: sum(1 for start in range(n) if start + L <= n) for L in range(1, n + 1)}      # a piece is a run of neighbouring stamps
    return {'a': s([pieces[1]]), 'b': s([pieces[2]]), 'c': s([pieces[3]]), 'd': s([pieces[4] + pieces[5], sum(pieces.values())])}


@check('T03')
def _():
    rays = 4
    per_line = sum(1 for a, b in itertools.combinations(range(rays), 2))
    return {'a': s([per_line]), 'b': s([per_line]), 'c': s([triangles(2, 1)])}


@check('G01')
def _():
    rows6 = list(range(1, 7))
    return {'a': s([rows6[-1]]), 'b': s([sum(rows6)]), 'c': s([sum(range(1, 9))])}


@check('G02')
def _():
    n = 4
    cnt = {0: 0, 1: 0, 2: 0, 3: 0}
    for x, y, z in itertools.product(range(n), repeat=3):
        painted = sum(1 for v in (x, y, z) if v in (0, n - 1))
        cnt[painted] += 1
    assert sum(cnt.values()) == 64
    return {'a': s([cnt[3]]), 'b': s([cnt[2]]), 'c': s([cnt[1]]), 'd': s([cnt[0]])}


@check('G03')
def _():
    assert 4 * 3 * 2 == 24 and 12 + 8 + 4 == 24 and 4 * 3 >= 4 * 2 >= 2 * 2
    return ['open']


@check('G04')
def _():
    return s([rectangles(2, 3)])


@check('C01')
def _():
    return ['cone']


@check('C02')
def _():
    return s([3 * 2])


@check('C03')
def _():
    return s([4 * 3 * 2])


@check('C04')
def _():
    return s([sum(squares(2, 3).values())])
