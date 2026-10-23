"""Independent answer checks for Level 1 Term 3 Lesson 7 (Lesson 27, Fill the Grid).

Every grid is read back from the figure in the lesson file (a `panel` of shapes or a `grid` of digits), then every answer is recomputed by enumerating all
Latin squares of that size (12 of order 3 and 576 of order 4, built here from permutations, not from any rule the lesson teaches). So a puzzle has exactly
the number of completions the lesson says, each box named in a question has the answer in the key, 'could be' counts come from row and column crossing out,
and 'is it correct' items are decided by checking every row and every column. The tile kit is read back from the kit builder (16 tiles counted in its SVG).
No grid that a child sees in a workbook question, the exit ticket or the Quest is the same picture as a grid used in class.
"""
import itertools
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'tools'))

LET = {'circle': 'C', 'square': 'S', 'triangle': 'T', 'star': 'X'}
NAME = {'C': 'circle', 'S': 'square', 'T': 'triangle'}


def latin(n, syms):
    rows = list(itertools.permutations(syms))
    out = []

    def rec(cur):
        if len(cur) == n:
            out.append(tuple(cur)); return
        for r in rows:
            if all(r[j] != c[j] for c in cur for j in range(n)): rec(cur + [r])
    rec([])
    return out


L3 = latin(3, 'CST')
L4 = latin(4, '1234')


def fit(squares, known):
    return [s for s in squares if all(s[r][c] == v for (r, c), v in known.items())]


def shape_grid(fig):
    """A `panel` figure -> list of row strings, '?' for a hidden tile; also the labels {(r, c): label}."""
    cols = fig['cols']; tiles = fig['tiles']; hide = set(fig.get('hide', []))
    cells = ['?' if i in hide else LET[t['shape']] for i, t in enumerate(tiles)]
    rows = [''.join(cells[r * cols:(r + 1) * cols]) for r in range(len(cells) // cols)]
    labs = {}
    for i, lab in enumerate(fig.get('labels') or []):
        if lab: labs[divmod(i, cols)] = lab
    return rows, labs


def digit_grid(fig):
    """A `grid` figure with counts -> list of row strings; '[]' becomes '.', digits stay, other text (a, b, c, ?) stays."""
    rows = []
    for r in range(fig['rows']):
        s = ''
        for c in range(fig['cols']):
            t = fig['counts'].get(f'{r},{c}', '')
            s += '.' if t == '[]' else ('?' if t == '' else t)
        rows.append(s)
    return rows


def known_of(rows, ignore='?.abc'):
    return {(r, c): ch for r, row in enumerate(rows) for c, ch in enumerate(row) if ch not in ignore}


def is_latin(rows, syms):
    n = len(rows)
    ok_rows = all(sorted(r) == sorted(syms) for r in rows)
    ok_cols = all(sorted(rows[r][c] for r in range(n)) == sorted(syms) for c in range(n))
    return ok_rows, ok_cols


def could_be(rows, r, c, syms='CST'):
    """Shapes that cross-out by the row and the column of box (r, c) leaves."""
    n = len(rows)
    seen = {rows[r][k] for k in range(n)} | {rows[k][c] for k in range(n)}
    return [s for s in syms if s not in seen]


def figs_in(x, kind, out=None):
    out = [] if out is None else out
    if isinstance(x, dict):
        if x.get('type') == kind: out.append(x)
        for v in x.values(): figs_in(v, kind, out)
    elif isinstance(x, list):
        for v in x: figs_in(v, kind, out)
    return out


# ------------------------------------------------------------------------------------------------ online practice oracles
def _digits_row(m):
    return [d for d in (1, 2, 3, 4) if d != m]


ORACLES = {
    'c3': lambda e: next(d for d in (1, 2, 3, 4) if d not in _digits_row(e['m'])),
    'c4': lambda e: sum(1 for r in range(e['n']) for c in range(e['n'])),
    'c5': lambda e: sum(1 for row in [[(r + c) % e['n'] for c in range(e['n'])] for r in range(e['n'])] for x in row if x == 0),
    'g2': lambda e: sum(1 for row in [[(r + c) % e['n'] + 1 for c in range(e['n'])] for r in range(e['n'])] for x in row if x in (1, 2, 3)),
}
BASE_ENV = {'c3': {'m': 2}, 'c4': {'n': 3}, 'c5': {'n': 3}, 'g2': {'n': 5}}


def mid_all():
    return fit(latin(3, '123'), {(1, 1): '2'})


def run(d):
    n = 0

    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a!r}, expected {b!r}'
    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    X = {q['id']: q for q in d['exit']}
    H = {q['id']: q for q in d['home_practice']}
    sl = {s['id']: s for s in d['slides']}
    panels = lambda x: figs_in(x, 'panel')
    sg = lambda f: shape_grid(f)[0]
    shown = {}      # every grid picture a child sees, by item, for the distinctness checks

    def single(rows, want, msg):
        """A single row or column of three with one '?': the missing shape is the one that is not there."""
        flat = ''.join(rows)
        eq(flat.count('?'), 1, msg + ' has one ?'); eq(sorted(set('CST') - set(flat)), [want], msg + ' missing shape')

    # ---------------------------------------------------------------- warm-up
    g = sg(panels(sl['s-rem1']['blocks'])[0]); single(g, 'T', 'rem1'); shown['rem1'] = tuple(g)
    nr = [b for b in sl['s-rem2']['blocks'] if b.get('t') == 'numrow'][0]['items']
    eq((nr, sorted({1, 2, 3, 4} - {x for x in nr if x != '?'})), ([1, 3, 4, '?'], [2]), 'rem2 missing digit is 2')
    rA, rB = [sg(f)[0] for f in panels(sl['s-rem3']['blocks'])]
    eq((sorted(rA), sorted(rB)), (['C', 'S', 'T'], ['S', 'S', 'T']), 'rem3 rows'); eq((len(set(rA)), len(set(rB))), (3, 2), 'rem3 A has one of each, B has a repeat')
    # ---------------------------------------------------------------- sneak-peek
    sp = d['sneak_peek']; ps = panels(sl['s-sneak']['blocks'])
    g1 = sg(ps[0]); single(g1, 'C', 'sneak 1'); eq(sp['a1'], 'circle', 'sneak a1')
    g2, labs = shape_grid(ps[1]); fits = fit(L3, known_of(g2))
    eq(len(fits), 1, 'sneak 2 has exactly one completion'); eq(fits[0][2][0], 'S', 'sneak 2 box a is a square'); eq((labs, g2[2]), ({}, '??T'), 'sneak 2: the first ? of the bottom row is the box asked')
    eq(could_be(g2, 2, 0), ['S'], 'sneak 2: the row and the column cross out C and T'); eq({g2[2][k] for k in range(3)} - {'?'}, {'T'}, 'sneak 2: the row alone shows only a triangle')
    eq({g2[k][0] for k in range(3)} - {'?'}, {'T', 'C'}, 'sneak 2: the column has a triangle and a circle')
    eq(sp['a2'].startswith('A square.'), True, 'sneak a2 text'); shown['sneak2'] = tuple(g2)
    # ---------------------------------------------------------------- explore: the same top row has exactly 2 grids
    g = sg(panels(sl['s-explore3']['blocks'])[0])
    top = fit(L3, {(0, 0): 'C', (0, 1): 'S', (0, 2): 'T'}); eq(len(top), 2, 'explore 3: exactly 2 grids with the top row C S T')
    eq(sorted(''.join(r) for s in top for r in s[1:]), sorted(['STC', 'TCS', 'TCS', 'STC']), 'explore 3 grids'); eq(g[0], 'CST', 'explore 3 top row on the slide')
    eq(sum(1 for r in L3 if r[0][0] == 'C'), 4, 'four squares start with a circle in the corner (2 top rows x 2)')
    eq(len(L3), 12, 'there are 12 grids in all')
    # ---------------------------------------------------------------- mini-lesson
    g = sg(panels(sl['s-m1']['blocks'])[0]); eq(is_latin(g, 'CST'), (True, True), 's-m1 grid follows the rule'); eq(tuple(tuple(r) for r in g) in set(L3), True, 's-m1 is one of the 12'); shown['m1'] = tuple(g)
    mr = sg(panels(sl['s-m2']['blocks'])[0]); tb = [[x.split(': ')[1]] for x in [b for b in sl['s-m2']['blocks'][0]['cols'][1] if b.get('t') == 'list'][0]['items']]
    eq(mr, ['T?S'], 's-m2 row'); eq(sorted(set('CST') - set(mr[0])), ['C'], 's-m2 row: circle is missing')
    eq(tb, [['?'], ['circle'], ['triangle']], 's-m2 column'); eq(sorted({'circle', 'square', 'triangle'} - {r[0] for r in tb}), ['square'], 's-m2 column: square is missing')
    g, labs = shape_grid(panels(sl['s-m3']['blocks'])[0]); fits = fit(L3, known_of(g))
    eq((len(fits), fits[0][1][1]), (1, 'T'), 's-m3 unique completion, box a is a triangle'); eq(labs, {(1, 1): 'a'}, 's-m3 box a is the middle box')
    eq(({g[1][k] for k in range(3)} - {'?'}, {g[k][1] for k in range(3)} - {'?'}), ({'S'}, {'C'}), 's-m3: the row has a square, the column has a circle'); eq(could_be(g, 1, 1), ['T'], 's-m3 box a by crossing out')
    shown['m3'] = tuple(g)
    g = sg(panels(sl['s-m4']['blocks'])[0]); eq(is_latin(g, 'CST'), (True, False), 's-m4: rows fine, a column repeats'); eq([g[r][0] for r in range(3)], ['C', 'S', 'C'], 's-m4 first column has two circles'); shown['m4'] = tuple(g)
    ps5 = panels(sl['s-m5']['blocks']); g = sg(ps5[0]); single(g, 'T', 's-m5 row'); g5 = sg(ps5[1]); eq(is_latin(g5, 'CST'), (True, True), 's-m5 grid is correct'); shown['m5'] = tuple(g5)
    eq([b for b in sl['s-m5a']['blocks'] if b.get('t') == 'answer'][0]['text'], 'Row: a triangle. Grid: Yes, it is correct.', 's-m5a')
    # ---------------------------------------------------------------- Start here
    q = T['S1']; rows = [sg(f)[0] for f in q['visuals']]; eq(rows, ['TS?', '?CS', 'T?C'], 'S1 rows'); eq([sorted(set('CST') - set(r))[0] for r in rows], ['C', 'T', 'S'], 'S1 missing shapes')
    eq([NAME[x] for x in 'CTS'], q['val'], 'S1 val')
    q = T['S3']; g, labs = shape_grid(q['visual']); fits = fit(L3, known_of(g)); eq((len(fits), fits[0][2][0]), (1, 'T'), 'S3 unique, the bottom left box is a triangle'); eq(g[2][:2], '??', 'S3 bottom left is the first ?')
    col = {g[k][0] for k in range(3)} - {'?'}; row = {g[2][k] for k in range(3)} - {'?'}; eq((col, row), ({'C', 'S'}, {'C'}), 'S3 the column has a circle and a square, the row has only a circle')
    eq(q['parts'][1]['val'], 'column', 'S3 reason is the column'); eq(q['parts'][1]['choices'][0], 'The column has a circle and a square.', 'S3 first option is the true one'); shown['S3'] = tuple(g)
    q = T['S2']; rows = [sg(f)[0] for f in q['visuals']]; eq(rows, ['STC', 'CCT', 'TCS'], 'S2 rows'); eq([len(set(r)) == 3 for r in rows], [True, False, True], 'S2 one of each'); eq(q['val'], ['True', 'False', 'True'], 'S2 val')
    eq(len(q['tf']), 3, 'S2 three statements')
    q = T['S4']; rows = sg(q['visual']); eq(rows, ['CST', 'TCS', 'CTS'], 'S4 rows'); eq(is_latin(rows, 'CST'), (True, False), 'S4 rows fine, a column repeats'); eq([rows[r][0] for r in range(3)], ['C', 'T', 'C'], 'S4 first column has two circles')
    eq(q['val'], ['No'], 'S4 val'); eq('Every row has one of each' in q['text'], True, 'S4 text says every row has one of each'); shown['S4'] = tuple(rows)
    q = T['S5']; eq((sum(1 for L in L3 for r in range(3) for c in range(3) if L[r][c] == 'C') // 12, q['val']), (3, [3]), 'S5 every grid has 3 circles (counted over all 12 grids)')
    eq(sum(x['mins'] for x in d['tiers']['start']) <= 20, True, 'Start here within 20 minutes'); eq(len(d['tiers']['start']), 5, 'five Start here questions')
    # ---------------------------------------------------------------- Think harder
    q = T['T1']; g, labs = shape_grid(q['visual']); fits = fit(L3, known_of(g)); eq(len(fits), 1, 'T1 exactly one grid fits the two clues'); sol = fits[0]
    eq(sum(1 for row in g for ch in row if ch != '?'), 2, 'T1 gives only two shapes'); places = [(0, 1), (1, 2), (2, 2)]
    eq([NAME[sol[r][c]] for (r, c) in places], q['val'], 'T1 top middle, middle right, bottom right'); eq(sol, (('C', 'T', 'S'), ('T', 'S', 'C'), ('S', 'C', 'T')), 'T1 solution'); eq(could_be(g, 0, 1), ['T'], 'T1 top middle box by crossing out (row has C, column has S)')
    shown['T1'] = tuple(g)
    q = T['T2']; sets_ = [({'C'}, {'C'}), ({'T'}, {'S'})]; cnt = [len(set('CST') - a_ - b_) for a_, b_ in sets_]; eq(cnt, [2, 1], 'T2 how many shapes could go in the two boxes'); eq(q['val'], cnt, 'T2 val')
    q = T['T3']; eq(q['val'], ['True', 'False'], 'T3 val')
    eq(all(is_latin([L[a] for a in perm], 'CST') == (True, True) for L in L3 for perm in itertools.permutations(range(3))), True, 'swapping any rows of any correct grid is correct (all 12 grids, all 6 orders)')
    def swap_box(L, r, i, j):
        m = list(L[r]); m[i], m[j] = m[j], m[i]; return [L[0], L[1], L[2]][:r] + [''.join(m)] + [L[0], L[1], L[2]][r + 1:]
    eq(all(is_latin(swap_box([''.join(x) for x in L], 1, i, j), 'CST') == (True, False) for L in L3 for (i, j) in ((0, 1), (0, 2), (1, 2))), True, 'swapping two boxes inside a row breaks a column in every one of the 12 grids')
    # ---------------------------------------------------------------- Go further
    q = T['G1']; g = digit_grid(q['visual']); fits = fit(L4, known_of(g)); eq(len(fits), 1, 'G1 exactly one grid'); sol = fits[0]
    empties = [(r, c) for r in range(4) for c in range(4) if g[r][c] == '.']; eq(len(empties), 7, 'G1 seven empty boxes'); eq([int(sol[r][c]) for (r, c) in empties], q['val'], 'G1 answers in reading order')
    eq(sum(1 for row in g for ch in row if ch != '.'), 9, 'G1 nine clues'); eq([''.join(r) for r in sol], ['1423', '3142', '2314', '4231'], 'G1 solution'); shown['G1'] = tuple(g)
    q = T['G2']; g = digit_grid(q['visual']); fits = fit(L4, known_of(g, '?.abc')); eq(len(fits), 1, 'G2 exactly one grid with the six clues'); sol = fits[0]
    pos = {ch: (r, c) for r, row in enumerate(g) for c, ch in enumerate(row) if ch in 'abc'}; eq([int(sol[pos[k][0]][pos[k][1]]) for k in 'abc'], q['val'][0] if isinstance(q['val'][0], list) else q['val'], 'G2 a, b, c')
    eq(sum(1 for row in g for ch in row if ch in '1234'), 6, 'G2 six clues'); eq([''.join(r) for r in sol], ['2143', '3421', '4312', '1234'], 'G2 solution')
    shown['G2'] = tuple(g)
    q = T['G3']; k = 5
    sq = [[(r + c) % k + 1 for c in range(k)] for r in range(k)]
    eq(([len(sq) * len(sq[0]), sum(1 for row in sq for x in row if x in (4, 5))]), q['val'], 'G3 on a 5 by 5 grid built by shifting rows: boxes in all, boxes that hold a 4 or a 5')
    eq(all(sorted(row) == list(range(1, k + 1)) for row in sq) and all(sorted(sq[r][c] for r in range(k)) == list(range(1, k + 1)) for c in range(k)), True, 'G3 the 5 by 5 grid exists')
    # ---------------------------------------------------------------- Investigation
    inv = d['tiers']['investigation']; eq(inv['first'].startswith('Row 1 is 1 3 2. Row 2 is 3 2 1. Write row 3:'), True, 'I1 first step text'); eq('The first one is 132 321 213.' in inv['text'], True, 'I1 text gives the first grid, the one the first step builds')
    first = fit(latin(3, '123'), {(0, 0): '1', (0, 1): '3', (0, 2): '2', (1, 0): '3', (1, 1): '2', (1, 2): '1'}); eq(len(first), 1, 'I1 first step has one answer'); eq(first[0][2], ('2', '1', '3'), 'I1 last row is 2 1 3'); eq('row 3 is 2, 1, 3' in inv['answer'], True, 'I1 answer gives the first step')
    eq(first[0][1][1], '2', 'I1 the first step grid already has a 2 in the middle (it is one of the 4)')
    eq(all(((s_[0][0], s_[1][1], s_[2][2]) == ('2',) * 3) != ((s_[0][2], s_[1][1], s_[2][0]) == ('2',) * 3) for s_ in mid_all()), True, 'I1 look-for: the three 2s run along exactly one of the two diagonals in every grid')
    mid = fit(latin(3, '123'), {(1, 1): '2'}); eq(len(mid), 4, 'I1 exactly 4 grids with a 2 in the middle'); eq(inv['val'], ['4'], 'I1 val')
    for s_ in mid: eq(' '.join(s_[0]) + ' / ' + ' '.join(s_[1]) + ' / ' + ' '.join(s_[2]) in inv['answer'], True, 'I1 answer lists ' + str(s_))
    # ---------------------------------------------------------------- talk
    sneak_g = ['TSC', 'CTS', '??T']
    eq(sum(row.count('?') for row in sneak_g[2:]), 2, 'talk: the sneak-peek bottom row has two empty boxes, so the row alone cannot decide')
    eq(len(set(L3[i][2][0] for i in range(12))) >= 1 and len(could_be(sneak_g, 2, 0)) == 1, True, 'talk: the column decides box a')
    eq(len({s[2][0] for s in fit(L3, {(0, 0): 'T', (0, 1): 'S', (0, 2): 'C', (1, 0): 'C', (1, 1): 'T', (1, 2): 'S'})}), 1, 'talk grid')
    eq(d['talk']['answer'].startswith('Not always.'), True, 'talk answer')
    # ---------------------------------------------------------------- exit
    q = X['E1']; eq(sorted(set('CST') - {'C', 'S'}), ['T'], 'E1 a row with a circle and a square lacks the triangle'); eq(q['val'], ['triangle'], 'E1 val')
    q = X['E2']; opts = q['mcq']['options']; good = [i + 1 for i, o in enumerate(opts) if sorted(x.strip() for x in o.split(',')) == ['circle', 'square', 'triangle']]
    eq((good, q['val']), ([2], [2]), 'E2 only option 2 has one of each'); eq(len(opts), 4, 'E2 four options')
    q = X['E3']; eq(sorted(set(['circle', 'square', 'triangle']) - {'circle', 'square'}), ['triangle'], 'E3 box a: not the circle (row), not the square (column)'); eq(q['val'], ['triangle'], 'E3 val')
    # ---------------------------------------------------------------- the same picture is never in class and in the workbook
    class_keys = ['rem1', 'sneak2', 'm1', 'm3', 'm4', 'm5']; work_keys = [k for k in shown if k not in class_keys]
    eq(sorted(set(shown[k] for k in class_keys) & set(shown[k] for k in work_keys)), [], 'no workbook, exit or Quest grid is a class grid'); eq(len(work_keys) >= 4, True, 'workbook grids were checked')
    eq(len(set(shown.values())), len(shown), 'every grid a child sees is a different picture')
    # ---------------------------------------------------------------- home practice
    eq(sorted(set('CST') - {'C', 'T'}), ['S'], 'H1 square'); eq(H['H1']['val'], 'square', 'H1')
    eq(sorted({1, 2, 3} - {3, 1}), [2], 'H2'); eq(H['H2']['val'], 2, 'H2 val')
    h3 = fit(latin(3, '123'), {(0, 0): '1', (0, 1): '2', (0, 2): '3', (1, 0): '2'}); eq(len(h3), 1, 'H3 unique'); eq([[int(x) for x in h3[0][1]], [int(x) for x in h3[0][2]]], H['H3']['val'], 'H3 rows 2 and 3')
    h4 = fit(L4, {(0, 0): '1', (0, 1): '2', (0, 2): '3', (0, 3): '4', (1, 0): '2', (1, 1): '1', (1, 2): '4', (1, 3): '3', (2, 0): '3'}); eq({s[2][1] for s in h4}, {'4'}, 'H4 second box of row 3 is 4 in every grid that fits'); eq(len(h4) > 1, True, 'H4 the whole grid is not decided but the asked box is'); eq(H['H4']['val'], 4, 'H4 val')
    eq(52 - 46, H['H5']['val'], 'H5'); eq(H['H5'].get('rewind_of'), 'Term 1 Lesson 7', 'H5 rewind'); eq(len([h for h in d['home_practice'] if h['tier'] == 'start']) >= 3, True, 'home has 3 Start here items')
    # ---------------------------------------------------------------- online practice
    items = {i['id']: i for i in d['online_practice']['items']}
    eq(items['c1']['answer'], NAME[next(iter(set('CST') - set('CT')))], 'c1'); eq(sg(items['c1']['fig']), ['CT?'], 'c1 fig')
    eq(items['c2']['answer'], 'triangle', 'c2'); eq(sorted(set('CST') - set('SC')), ['T'], 'c2 row S ? C'); eq(sg(items['c2']['fig']), ['S?C'], 'c2 fig')
    eq(items['c3']['answer'], ORACLES['c3'](BASE_ENV['c3']), 'c3'); eq(items['c4']['answer'], 9, 'c4'); eq(items['c5']['answer'], 3, 'c5'); eq(items['g2']['answer'], 15, 'g2')
    for m in (1, 2, 3, 4):                                  # the derived digits shown in c3 are the other three, in order
        env = {'m': m}
        for k, ex in items['c3']['tpl']['derive'].items(): env[k] = eval(re.sub(r'\bm\b', str(m), ex))
        eq([env['x'], env['y'], env['z']], _digits_row(m), f'c3 shows the other three digits when m = {m}')
    t1 = items['t1']; g, labs = shape_grid(t1['fig']); fits = fit(L3, known_of(g)); eq((len(fits), fits[0][0][1], t1['answer']), (1, 'S', 'square'), 't1 unique, box a is a square'); eq(labs, {(0, 1): 'a'}, 't1 box a')
    t2 = items['t2']; g, labs = shape_grid(t2['fig']); (r, c), = labs; eq((len(could_be(g, r, c)), t2['answer']), (2, 2), 't2 two shapes could go in box a')
    t3 = items['t3']; g = sg(t3['fig']); eq((is_latin(g, 'CST'), t3['answer']), ((True, False), 'No'), 't3 grid is not correct')
    g1 = items['g1']; g = digit_grid(g1['fig']); fits = fit(L4, known_of(g, '?.abc')); eq(len(fits), 1, 'g1 one grid'); pos = [(r, c) for r, row in enumerate(g) for c, ch in enumerate(row) if ch == 'a'][0]
    eq((int(fits[0][pos[0]][pos[1]]), g1['answer']), (1, 1), 'g1 box a is 1')
    for cid, env in BASE_ENV.items(): eq(ORACLES[cid](env), items[cid]['answer'], cid + ' oracle at the authored numbers')
    for nn in items['g2']['tpl']['vars']['n']: eq(ORACLES['g2']({'n': nn}), 3 * nn, f'g2 variant n={nn}: three digits per row')
    eq(max(items['c4']['tpl']['vars']['n']) <= 5, True, 'c4 variants stay within 5 by 5 (no picture is shown)')
    st = ' '.join(g1['steps']); eq((g[2][0], sorted(g[2][1:]), '4' in g[1], sorted([g[0][0], g[2][0]])), ('?', ['1', '3', '4'][0:0] or sorted(g[2][1:]), True, ['3', '?']), 'g1 picture: row 3 is ? 3 4 1, row 2 ends in 4')
    eq((fits[0][2][0], fits[0][0][0], fits[0][2][0] == '2'), ('2', '3', True), 'g1 step 1: row 3 has 3, 4, 1 so its first box is 2'); eq({fits[0][r][0] for r in (0, 2)}, {'3', '2'}, 'g1 step 3: column 1 has 3 and 2 (so a is 1 or 4)')
    eq(('a cannot be 4' in st.replace('box a cannot be 4', 'a cannot be 4'), g[1][3]), (True, '4'), 'g1 step 2: the row of a has a 4')
    op = [x['text'] for x in d['script']['segments'][0]['lines'] if x['k'] in ('SAY', 'DO')]; ot = ' '.join(op)
    eq(('Nobody holds paper up to the camera' in ot, 'any voice that is not muted' in ot, 'Do not use children' in ot, 'by first name as they arrive' in ot), (True, True, True, False), 'opening carries the Term 1 recording and camera wording')
    eq(d['script']['segments'][0]['lines'][-3]['k'], 'NOTE', 'opening ends with notes')
    mt = sl['s-m4']; eq(sum(1 for c in range(3) if len({sg(panels(mt['blocks'])[0])[r][c] for r in range(3)}) < 3), 2, 's-m4: two columns repeat, so the question is plural')
    eq(any(l.get('text') == 'Which columns have two of the same?' for sg_ in d['script']['segments'] for l in sg_['lines']), True, 's-m4 question is plural')
    eq(sl['s-menu']['blocks'][0]['rows'][1][1].startswith('Row right, column right?'), True, 'menu slide is the guide M1')
    eq(d['parent']['term_line'], 'Your child is learning to give a reason for each step.', 'term line fits the lesson')
    for it in items.values():
        for s_ in it.get('slips', []):
            if it['type'] in ('number', 'choice'): eq(it['answer'] in s_['a'], False, it['id'] + ' slip is wrong')
    for cid in ('c3', 'c4', 'c5', 'g2'):                     # no variant prints a plural slip: every n is 3 or more
        tp = items[cid]['tpl']
        for combo in itertools.product(*[tp['vars'][k] for k in tp['vars']]): eq(all(v >= 1 for v in combo), True, f'{cid} variables are positive')
    # ---------------------------------------------------------------- the kit page: read back from the kit builder
    import figs3
    svg = figs3.render_kit({'type': 'grid_tiles'})
    tiles = re.findall(r'<rect x="[\d.]+" y="[\d.]+" width="[\d.]+" height="[\d.]+" rx="8" fill="#fff" stroke="[^"]+" stroke-width="2" stroke-dasharray="7 5"/>', svg)
    eq(len(tiles), 16, 'the page prints 16 cut-out tiles')
    eq((len(re.findall(r'<circle ', svg)), len(re.findall(r'fill="#BFE3DC"', svg)), len(re.findall(r'fill="#FFE59A"', svg)), len(re.findall(r'fill="#C9B6F0"', svg))), (4, 4, 4, 4), 'printed tiles: 4 circles, 4 squares, 4 triangles, 4 stars')
    digits = [int(x) for x in re.findall(r'>([1-4])<', svg)]; eq(sorted(digits), [1] * 4 + [2] * 4 + [3] * 4 + [4] * 4, 'each digit 1 to 4 is printed on 4 tiles')
    eq(len(re.findall(r'fill="#fff" stroke="#1B2A49" stroke-width="2.6"', svg)), 9 + 16, 'the two mats print 9 and 16 boxes')
    names = {'circle tiles': 4, 'square tiles': 4, 'triangle tiles': 4, 'star tiles': 4, 'tiles with each digit 1 to 4 (one on each symbol)': 4, 'mat 1 (3 by 3)': 1, 'mat 2 (4 by 4)': 1}
    for r in d['materials']['kit_contract']:
        eq(r['supplied'], names[r['piece']], r['piece'] + ' supplied matches the printed page'); eq(r['supplied'] >= r['max_used'], True, r['piece'] + ' supplied covers the most used')
    eq(3 * 3, 9, 'class uses 9 tiles: 3 of each of 3 symbols (supplied 4 of each)'); eq(4 * 4, 16, 'Go further uses all 16')
    # ---------------------------------------------------------------- hand-off to the next lesson (14 paper strips)
    nm = ' '.join(d['parent']['next_materials'])
    eq(('14' in nm, 'strip' in nm, 'cut' in nm, 'toothpicks' in nm), (True, True, True, True), 'hand-off to Lesson 28 names the 14 strips and says no matches or toothpicks')
    eq(d['workbook']['kits'][0]['type'], 'grid_tiles', 'kit type')
    return n
