"""Online practice for Level 4 (Primary 4, ages 9-11) holiday lesson 8: Symmetry and Nets.

The questions are the ones printed in the Level 4 holiday workbook, built by p4/workbook_html.js from p4/content/l8.js:
  Start here = l8.js workbook() Q1 to Q6;   Investigation = l8.js gaps.invest (A row of four);
  Think harder = l8.js qbank.stretch[0:4];   Go further = l8.js qbank.challenge[-3:]  (printed as Q5 to Q7).
Every answer is recomputed by an INDEPENDENT checker: a cube is rolled over each net (faces, opposite faces, every dice labelling), every mirror line of a shape is tried, every
shading of a grid is tested for symmetry, every face count is added up; never a copy of the printed answer.  The build stops if a checker and the printed answer differ.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from p4lib import *      # noqa: E402,F401

META = dict(level=4, lesson=8, key='p4', title='Symmetry and Nets', workbook_title='SYMMETRY AND NETS', topic='Symmetry and Nets',
            strand='Symmetry and nets',
            sources=['p4/content/l8.js'],
            intro=['Type numbers, or squares such as A2 (column letter, then row number). Shape and direction questions are choices: tap one.',
                   'Drawing questions (completing a figure, shading squares) are done on paper, on your workbook page or squared paper: do them, then compare with the picture shown after you submit. '
                   'Some questions ask you to explain or to design your own: think or write on paper, then compare.'])
S8 = 'Symmetry and nets'


def D(**k):
    return dict(strand=S8, **k)


def row4(y=1):
    return [(0, y), (1, y), (2, y), (3, y)]


NETS = {'A': row4() + [(1, 0), (1, 2)], 'B': row4() + [(0, 0), (2, 0)], 'C': [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1)],
        'D': [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (1, 0)], 'E': [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2)], 'F': [(0, 0), (1, 0), (0, 1), (1, 1), (2, 1), (3, 1)]}
FOLDS = [k for k, v in NETS.items() if fold(v)]
NOFOLD = [k for k in NETS if k not in FOLDS]
NETQ2 = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2)]
Q2L = {(0, 0): 'A', (0, 1): 'B', (1, 1): 'C', (2, 1): 'D', (2, 2): 'E', (3, 2): 'F'}
NETA = row4() + [(0, 0), (3, 2)]
GIVENA = {(0, 0): 1, (2, 1): 4, (3, 1): 2}
NETB = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2)]
GIVENB = {(0, 0): 5, (1, 1): 1, (2, 2): 3}
SHAPES = {'a': [(0, 0), (1, 0), (2, 0), (1, 1), (1, 2)], 'b': [(0, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (2, 2)], 'c': [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)], 'd': [(1, 0), (2, 0), (0, 1), (1, 1)]}
Q6 = {(1, 1), (1, 2), (2, 1), (2, 2), (3, 1)}


def sq(c):
    return 'ABCD'[c[0]] + str(c[1] + 1)


def q6_ways():
    out = []
    for x in range(4):
        for y in range(4):
            if (x, y) in Q6:
                continue
            s = Q6 | {(x, y)}
            if s == {(3 - a, b) for a, b in s} or s == {(a, 3 - b) for a, b in s}:
                out.append((x, y))
    return out


def net_with(top, bottom):
    return row4() + [(top, 0), (bottom, 2)]


def net_above(i, j):
    return row4() + [(i, 0), (j, 0)]


ALL16 = [(t, b) for t in range(4) for b in range(4)]
BOTH6 = [(i, j) for i in range(4) for j in range(i + 1, 4)]
FOUR_NETS = [('A', net_with(0, 3)), ('B', net_with(3, 0)), ('C', net_with(1, 1)), ('D', net_with(2, 3))]
TWO_ABOVE = [('A', net_above(0, 2)), ('B', net_above(1, 3))]
GRID3 = [(x, y) for x in range(3) for y in range(3)]
import itertools as _it
FIVE = [s for s in _it.combinations(GRID3, 5) if sym_lines(s) == 4]
assert len(FIVE) == 2
MODEL_DICE = {(0, 1): 2, (1, 1): 1, (2, 1): 5, (3, 1): 6, (1, 0): 3, (1, 2): 4}


def squares_name(s):
    return ['ABC'[x] + str(y + 1) for x, y in sorted(s, key=lambda c: (c[1], c[0]))]


def fiveacc():
    out = []
    for s in FIVE:
        out += perm_accepts(squares_name(s))
    return list(dict.fromkeys(out))


def fold_facts():
    """For each shape that does not fold: which squares land on the same face."""
    res = {}
    for k in NOFOLD:
        cells = NETS[k]
        # roll the cube over the spanning tree and record which squares get the same face
        ori = {cells[0]: (0, 1, 2, 3, 4, 5)}
        todo = [cells[0]]
        while todo:
            cur = todo.pop()
            for d, q in (('E', (cur[0] + 1, cur[1])), ('W', (cur[0] - 1, cur[1])), ('N', (cur[0], cur[1] - 1)), ('S', (cur[0], cur[1] + 1))):
                if q in cells and q not in ori:
                    ori[q] = roll(ori[cur], d)
                    todo.append(q)
        faces = {}
        for c, o in ori.items():
            faces.setdefault(o[1], []).append(c)
        res[k] = [v for v in faces.values() if len(v) > 1]
    return res


FF = fold_facts()
assert FF['B'] == [[(0, 0), (2, 0)]] or sorted(map(sorted, FF['B'])) == [[(0, 0), (2, 0)]], FF['B']
assert any((0, 1) in g and (4, 1) in g for g in FF['D']), FF['D']
assert any(len([c for c in g if c in {(0, 0), (1, 0), (0, 1), (1, 1)}]) >= 2 for g in FF['F']), FF['F']


def cuboid_faces(a, b, c):
    return sum(2 * x * y for x, y in _it.combinations([a, b, c], 2))


def sym_pairs_n(n):
    """Ways to shade exactly 2 squares of an n by n grid so that the up-down middle line is a line of symmetry."""
    cells = [(x, y) for x in range(n) for y in range(n)]
    return sum(1 for s in _it.combinations(cells, 2) if set(s) == {(n - 1 - x, y) for x, y in s})


def shape_svg(cells, c=40, fill=YEL, label=''):
    w, h = dims_c(cells)
    return svg(w * c + 8, h * c + 8, cells_g(cells, c, 4, 4, fill, sw=2.6), label or 'A shape made of squares.')


def lines_item(k, no, name, cells, hint, steps):
    return D(id='5' + k, tier='core', no=no, label=no, type='number', answer=sym_lines(cells), skill='lines of symmetry', svg=shape_svg(cells, 40, YEL, 'Shape ' + k + ': ' + name),
             check=lambda: sym_lines(cells), q='How many lines of symmetry does shape (' + k + ') have?', hint=hint, steps=steps,
             src=['Draw ALL the lines of symmetry on each shape. Then write how many.'])


def grid3(shaded=(), lines=(), c=48):
    return grid_cells_fig(set(shaded), 3, 3, c, YEL, True, True, lines, 'A 3 by 3 grid with columns A to C and rows 1 to 3.')


ITEMS = [
    # ================= Start here (workbook lesson 8, Q1 to Q6)
    D(id='1fold', tier='core', no='1', label='1 fold', type='text', accept=perm_accepts(FOLDS), shown=', '.join(FOLDS), skill='which nets fold into a cube', svg=nets_fig(list(NETS.items())),
      accept_prefix=False, check=lambda: ', '.join(k for k in NETS if fold(NETS[k])),
      q='Each shape is made of 6 squares. Which ones fold into a cube? Type the letters, with commas.',
      hint='Fold it in your head. Choose one square as the base. The squares that touch it fold up as walls. Does any square land where another one already is?',
      steps=['A shape folds into a cube when it has one base, one lid and four walls with nothing overlapping.', 'A, C and E fold into a cube.', 'B, D and F do not: see the next questions.'],
      src=['Each shape is made of 6 squares. Which ones fold into a cube?']),
    D(id='1not', tier='core', no='1', label='1 not', type='text', accept=NOFOLD + ['shape ' + k for k in NOFOLD], shown='B, D or F', skill='which nets fold into a cube', svg=nets_fig(list(NETS.items())),
      check=lambda: NOFOLD[0],
      q='Pick one of the shapes that does NOT fold into a cube. Type its letter.',
      hint='Fold each shape in your head. Look for a shape where two squares land on the same face.',
      steps=[f'Three of the shapes do not fold into a cube: {", ".join(NOFOLD)}.', 'Any one of them is a right answer.'],
      src=['Shape that does NOT fold:']),
    D(id='1why', tier='core', no='1', label='1 why', type='selfcheck', skill='why a net fails', svg=nets_fig(list(NETS.items())), check=lambda: FF,
      q='Explain why the shape you picked does not fold into a cube.',
      hint='Fold it in your head. Which squares land in the same place, or is a face left empty?',
      steps=['B: both extra squares are on the same side of the row of 4, so both fold over to the same end and land on top of each other. The other end has no square.',
             'D: it has 5 squares in a row. The 5th lands on the 1st.',
             'F: it has a 2 by 2 block. Four squares meet at one corner, but only 3 faces of a cube meet at a corner, so two of them overlap.'],
      src=['Explain why:']),

    D(id='2a', tier='core', no='2(a)', label='2(a)', type='choice', options=['B', 'C', 'D', 'E', 'F'], answer='E', skill='opposite faces of a net', svg=labelled_net_fig(NETQ2, Q2L, 40),
      check=lambda: next(Q2L[b] if Q2L[a] == 'A' else Q2L[a] for a, b in opposite_cells(NETQ2) if 'A' in (Q2L[a], Q2L[b])),
      q='This net folds into a cube. Which letter is opposite A?', hint='Fold it in your head. Which face is on the other side of the cube from A, with nothing between them?',
      steps=['Fold the net: A and E end up on opposite faces of the cube.', 'The answer is E.'], src=['This net folds into a cube. Which letter is opposite']),
    D(id='2b', tier='core', no='2(b)', label='2(b)', type='choice', options=['A', 'C', 'D', 'E', 'F'], answer='D', skill='opposite faces of a net', svg=labelled_net_fig(NETQ2, Q2L, 40),
      check=lambda: next(Q2L[b] if Q2L[a] == 'B' else Q2L[a] for a, b in opposite_cells(NETQ2) if 'B' in (Q2L[a], Q2L[b])),
      q='Which letter is opposite B?', hint='Look for a straight line of 3 squares. Which two squares are its ends?',
      steps=['B, C, D are three squares in a row. The middle one folds between the ends, so B and D are opposite.', 'The answer is D.'], src=['Which letter is opposite']),
    D(id='2c', tier='core', no='2(c)', label='2(c)', type='choice', options=['A', 'B', 'D', 'E', 'F'], answer='F', skill='opposite faces of a net', svg=labelled_net_fig(NETQ2, Q2L, 40),
      check=lambda: next(Q2L[b] if Q2L[a] == 'C' else Q2L[a] for a, b in opposite_cells(NETQ2) if 'C' in (Q2L[a], Q2L[b])),
      q='Which letter is opposite C?', hint='Look for pairs of faces with exactly one square between them in a row of the net. Which pair does C belong to?',
      steps=['A and E are opposite, and B and D are opposite.', 'The last two faces, C and F, are the last pair.'], src=['Which letter is opposite']),

    D(id='3a', tier='core', no='3(a)', label='3(a)', type='fields', frame='row: {f1}, {f2}, 4, 2   below the right end: {f3}', answer=[3, 5, 6], skill='dice nets',
      svg=labelled_net_fig(NETA, {(0, 0): '1', (2, 1): '4', (3, 1): '2'}, 40, caption='net (a)'),
      check=lambda: (lambda f: (f[0][(0, 1)], f[0][(1, 1)], f[0][(3, 2)]) if len(f) == 1 else None)(dice_fills(NETA, GIVENA)),
      q='On a dice, the numbers on opposite faces add up to 7. Write the missing numbers on net (a). Give the row from left to right, then the square below the right end.',
      hint='Find the face opposite each number you can see. Opposite faces add up to 7.',
      steps=['In the row of 4, the 1st and 3rd squares are opposite, and the 2nd and 4th are opposite. The 3rd shows 4, so the 1st is 7 − 4 = 3. The 4th shows 2, so the 2nd is 5.',
             'The square above the row and the square below it are opposite. 1 + 6 = 7, so the square below is 6.', 'The row reads 3, 5, 4, 2 and the square below is 6.'],
      src=['On a dice, the numbers on opposite faces add up to 7. Write the missing numbers on each dice net.']),
    D(id='3b', tier='core', no='3(b)', label='3(b)', type='fields', frame='top row: 5, {f1}   middle row: 1, {f2}   bottom row: 3, {f3}', answer=[4, 2, 6], skill='dice nets',
      svg=labelled_net_fig(NETB, {(0, 0): '5', (1, 1): '1', (2, 2): '3'}, 40, caption='net (b)'),
      check=lambda: (lambda f: (f[0][(1, 0)], f[0][(2, 1)], f[0][(3, 2)]) if len(f) == 1 else None)(dice_fills(NETB, GIVENB)),
      q='Now write the missing numbers on net (b). Give each row from left to right.',
      hint='Find the face opposite each number you can see. Opposite faces add up to 7.',
      steps=['Opposite faces add up to 7: 5 is opposite 2, 3 is opposite 4 and 1 is opposite 6.', 'The top row is 5, 4. The middle row is 1, 2. The bottom row is 3, 6.'],
      src=['Write the missing numbers on each dice net.']),
    D(id='3c', tier='core', no='3(c)', label='3(c)', type='selfcheck', skill='dice nets', svg=labelled_net_fig(NETB, {(0, 0): '5', (1, 1): '1', (2, 2): '3'}, 40, caption='net (b)'),
      check=lambda: [p for p in opposite_cells(NETB) if (1, 1) in p][0],
      q='In net (b), how did you find the number opposite 1?', hint='Look at the zigzag of squares that 1 is part of. Which squares are at its two ends?',
      steps=['The squares 1, 2, 3 and 6 make a zigzag (a step). The two ends of a step are opposite faces.', 'So 1 and 6 are opposite, and 1 + 6 = 7.'],
      src=['In net (b), how did you find the number opposite 1?']),

    D(id='4a', tier='core', no='4(a)', label='4(a)', type='selfcheck', paper=True, skill='completing a symmetric figure', svg=half_fig('rocket'), check=lambda: True, sol_fig=lambda f: half_fig('rocket', True),
      q='Complete the rocket on paper so that the dashed line is a line of symmetry. Count the squares from the line to each corner, and put a dot the same number of squares on the other side.',
      hint='Each corner on the left has a partner the same distance from the line on the right.',
      steps=['Each corner is flipped across the dashed line: the shoulders are 2 squares to the right of the line, the fin tips 4 squares to the right at the bottom, and the bottom edge ends 1 square to the right.', 'The notch is on the line. Join the dots.'],
      src=['Complete each figure so that the dashed line is a line of symmetry.']),
    D(id='4b', tier='core', no='4(b)', label='4(b)', type='selfcheck', paper=True, skill='completing a symmetric figure', svg=half_fig('fish'), check=lambda: True, sol_fig=lambda f: half_fig('fish', True),
      q='Complete the fish on paper so that the dashed line is a line of symmetry. Count the squares from the line to each corner, and put a dot the same number of squares on the other side.',
      hint='Each corner above the line has a partner the same distance below it.',
      steps=['Each corner is flipped across the dashed line: the tail tip 2 squares below, then 1 below, the back 3 below, then 2 below, and the nose is on the line.', 'Join the dots.'],
      src=['Complete each figure so that the dashed line is a line of symmetry.', 'Count the squares from the line to each corner.']),

    lines_item('a', '5(a)', 'T shape', SHAPES['a'], 'Fold it in your head along an up-down line, an across line and a corner-to-corner line. Do the two halves match?',
               ['The T shape has one line of symmetry: an up-down line through the middle.', 'An across line or a corner-to-corner line does not make the halves match.']),
    lines_item('b', '5(b)', 'H shape', SHAPES['b'], 'Try an up-down line, an across line and the two corner-to-corner lines. Which make the halves match?',
               ['The H shape has two lines of symmetry: an up-down line and an across line through the middle.', 'The corner-to-corner lines do not work.']),
    lines_item('c', '5(c)', 'plus shape', SHAPES['c'], 'Try an up-down line, an across line and the two corner-to-corner lines. Which make the halves match?',
               ['The plus shape has four lines of symmetry: up-down, across and both corner-to-corner lines.']),
    lines_item('d', '5(d)', 'zigzag of 4 squares', SHAPES['d'], 'Try every line: up-down, across and corner-to-corner. Do the halves ever match?',
               ['The zigzag has no line of symmetry. It looks the same when you turn it half a turn, but a half turn is not a fold.']),

    D(id='6a', tier='core', no='6(a)', label='6(a)', type='text', accept=perm_accepts([sq(c) for c in q6_ways()]), shown=', '.join(sq(c) for c in q6_ways()), skill='shading for symmetry',
      svg=grid_cells_fig(Q6, 4, 4, 44, TEAL, True, True, ('v', 'h'), 'A 4 by 4 grid, columns A to D and rows 1 to 4. Squares B2, B3, C2, C3 and D2 are shaded. An up-down dashed line and an across dashed line go through the middle.'),
      accept_prefix=False, check=lambda: ', '.join(sq(c) for c in q6_ways()),
      q='Shade ONE more square so that a dashed line becomes a line of symmetry of the shaded squares. Find ALL the squares that work. Type them like A1, with commas.',
      hint='Fold on each dashed line in your head. Where does each shaded square land? Is that square shaded?',
      steps=['Fold on the up-down line: B2 meets C2, B3 meets C3, but D2 meets A2. Shade A2.', 'Fold on the across line: B2 meets B3, C2 meets C3, but D2 meets D3. Shade D3.', 'No other square works. The squares are A2 and D3.'],
      src=['Shade ONE more square so that a dashed line becomes a line of symmetry of the shaded squares. Find ALL the ways.']),
    D(id='6count', tier='core', no='6(a)', label='6(a) ways', type='number', answer=2, skill='shading for symmetry',
      svg=grid_cells_fig(Q6, 4, 4, 44, TEAL, True, True, ('v', 'h'), 'A 4 by 4 grid with five shaded squares and two dashed lines.'), check=lambda: len(q6_ways()),
      q='Do the "find ALL" question first. Now count the squares in your list: how many are there?', hint='Count the squares in your list, one for each square that works.',
      steps=['One square works for the up-down line (A2) and one for the across line (D3).', 'That is 2 ways.'], src=['How many ways?']),
    D(id='6b', tier='core', no='6(b)', label='6(b)', type='selfcheck', open=True, marking_mode='self', skill='shading for symmetry',
      svg=grid_cells_fig(Q6, 4, 4, 44, TEAL, True, True, ('v', 'h'), 'A 4 by 4 grid with five shaded squares and two dashed lines.'),
      q='Choose a square that does NOT work. Where would its partner have to be?', hint='Pick a square, then fold on a dashed line in your head. Where would it land?',
      steps=['Answers vary. Example: A1. For the up-down line its partner would have to be D1. For the across line its partner would have to be A4.', 'Neither D1 nor A4 is shaded, so A1 does not work.'],
      src=['Choose a square that does NOT work. Where would its partner have to be?']),

    # ================= Investigation: A row of four
    D(id='Ieasy', tier='invest', no='Investigation (easy step)', label='Inv easy', type='choice', options=['Yes', 'No'], answer='Yes', skill='folding a net in your head', svg=labelled_net_fig(net_with(2, 1), {c: '\u00a0' for c in net_with(2, 1)}, 34, label='A net: a row of 4 squares with one square above and one square below.'),
      check=lambda: 'Yes' if fold(net_with(2, 1)) else 'No',
      q='Here is a net: a row of 4 squares with one square above it and one square below it. Fold it in your head. Does it make a cube?', hint='The row of 4 wraps round. What do the square above and the square below become?',
      steps=['The row of 4 folds round as four walls.', 'The square above becomes the lid and the square below becomes the base. It makes a cube.'],
      src=['Make the net in the picture (a row of 4 squares with one square above it and one below). Fold it. Does it make a cube?']),
    D(id='Ia', tier='invest', no='Investigation (a)', label='Inv (a)', type='choice', options=['Yes, all four fold', 'No, some do not fold'], answer='Yes, all four fold', skill='testing a claim', svg=nets_fig(FOUR_NETS),
      check=lambda: 'Yes, all four fold' if all(fold(c) for _, c in FOUR_NETS) else 'No, some do not fold',
      q='Mei says: "A row of 4 squares with ONE square above it and ONE square below it always folds into a cube, wherever the two squares are." Here are four such nets. Fold each in your head. Do they all fold into a cube?',
      hint='Pick the row as the walls. Where does the square above go, and where does the square below go?',
      steps=['In all four nets the row of 4 folds round as four walls.', 'The square above folds over as the lid and the square below as the base, wherever they are along the row.',
             f'We checked all {len(ALL16)} ways to place the two squares, and every one folds into a cube.'],
      src=['Test Mei\'s idea.', 'Do they all fold into a cube?']),
    D(id='Ib', tier='invest', no='Investigation (b)', label='Inv (b)', type='selfcheck', check=lambda: sum(1 for t, b in ALL16 if fold(net_with(t, b))), skill='explaining why a net folds',
      q='Explain why a row of 4 squares with one square above and one below makes a cube. Use the words wall, lid and base.', hint='What do the 4 squares in the row become? What does the square above become? And the square below?',
      steps=['The row of 4 squares wraps round to make four walls.', 'The square above becomes the lid, and the square below becomes the base. Nothing overlaps.', 'This works wherever the two squares are along the row: all 16 ways fold into a cube.'],
      src=['Explain why it works. Use the words wall, lid and base.']),
    D(id='Ic', tier='invest', no='Investigation (c)', label='Inv (c)', type='choice', options=['Yes, sometimes', 'No, never'], answer='No, never', skill='testing a claim', svg=nets_fig(TWO_ABOVE),
      check=lambda: 'Yes, sometimes' if any(fold(net_above(i, j)) for i, j in BOTH6) else 'No, never',
      q='What if BOTH extra squares are above the row? Here are two such nets, and there are others. Do shapes like these ever fold into a cube?',
      hint='Fold the row into walls. Where do the two extra squares go?',
      steps=['The row folds round as four walls. Both squares above fold over to become a lid, so they land on top of each other.', 'The base is left empty. We checked all 6 ways to put two squares above the row, and none folds into a cube.'],
      src=['What if BOTH extra squares are above the row? Try two. Do they ever fold into a cube? Why or why not?']),
    D(id='Ic-why', tier='invest', no='Investigation (c)', label='Inv (c) why', type='selfcheck', open=True, marking_mode='self', skill='explaining why a net fails',
      q='Explain what happens when the two extra squares are folded.', hint='Which face of the cube does each extra square become?',
      steps=['Both squares become the lid, so two squares land in the same place.', 'The base has no square. Any answer like this is good.'],
      src=['Do they ever fold into a cube? Why or why not?']),

    # ================= Think harder (qbank.stretch[0:4])
    D(id='T1', tier='stretch', no='Think harder 1', label='T1', type='number', answer=22, skill='nets of a cuboid', svg=cuboid_fig(3, 2, 1), check=lambda: cuboid_faces(3, 2, 1),
      q='A cuboid is 3 cm long, 2 cm wide and 1 cm high. Its net is drawn on 1 cm squared paper. How many squares does the net cover?', hint='A cuboid has 6 faces, in 3 pairs. Find the number of squares on each pair of faces.',
      steps=['2 faces of 3 by 2 have 6 squares each: 12.', '2 faces of 3 by 1 have 3 squares each: 6.', '2 faces of 2 by 1 have 2 squares each: 4.', '12 + 6 + 4 = 22 squares.'],
      src=['A cuboid is 3 cm long, 2 cm wide and 1 cm high.']),
    D(id='T2a', tier='stretch', no='Think harder 2', label='T2 bottom', type='number', answer=4, skill='opposite faces of a dice', check=lambda: next(v for v in range(1, 7) if v + 3 == 7),
      q='Ben puts a dice on the table. The top face shows 3 and the front face shows 5. What number is on the bottom face?', hint='Which face is opposite the top? Opposite faces add up to 7.',
      steps=['The bottom face is opposite the top face.', '3 + 4 = 7, so the bottom is 4.'], src=['Ben puts a dice on the table. The top face shows 3 and the front face shows 5.']),
    D(id='T2b', tier='stretch', no='Think harder 2', label='T2 back', type='number', answer=2, skill='opposite faces of a dice', check=lambda: next(v for v in range(1, 7) if v + 5 == 7),
      q='A dice shows 5 on its front face. What number is on its back face?', hint='Which face is opposite the front? Opposite faces add up to 7.',
      steps=['The back face is opposite the front face.', '5 + 2 = 7, so the back is 2.'], src=['What numbers are on the bottom face and on the back face?']),
    D(id='T3', tier='stretch', no='Think harder 3', label='T3', type='number', answer=2, skill='opposite faces of a dice', check=lambda: sum(range(1, 7)) - 19,
      q='A dice is on a table. Mei walks round it and can see the top and the four side faces. The numbers she can see add up to 19. What number is on the bottom face?', hint='How much do all six faces add up to? Which face is Mei not counting?',
      steps=['All six faces add up to 1 + 2 + 3 + 4 + 5 + 6 = 21.', 'Mei cannot see the bottom, so the bottom is 21 − 19 = 2.'], src=['A dice is on a table. Mei walks round it and can see the top and the four side faces.']),
    D(id='T4', tier='stretch', no='Think harder 4', label='T4', type='choice', options=[n for n, _ in TETRAS], answer='T', skill='lines of symmetry', svg=tetra_fig(),
      check=lambda: [n for n, c in TETRAS if sym_lines(c) == 1][0],
      q='There are 5 different shapes made of 4 squares joined edge to edge. Which one has exactly 1 line of symmetry?', hint='Count the lines of symmetry of each shape. Which one has just one?',
      steps=['The line has 2 lines of symmetry, the square has 4, the L has 0, the T has 1 and the zigzag has 0.', 'Only the T has exactly 1.'],
      src=['There are 5 different shapes made of 4 squares joined edge to edge']),

    # ================= Go further (qbank.challenge[-3:], printed Q5 to Q7)
    D(id='G5', tier='challenge', no='Go further 5', label='G5', type='selfcheck', open=True, marking_mode='open', skill='designing a dice net',
      check=lambda: (lambda f: f)(dice_fills(net_with(1, 1), {(0, 1): 2, (1, 1): 1, (1, 0): 3}) and MODEL_DICE),
      sol_fig=lambda f: labelled_net_fig(sorted(MODEL_DICE), {k: str(v) for k, v in MODEL_DICE.items()}, 36, label='A model dice net: a row 2, 1, 5, 6 with 3 above the 1 and 4 below it.'),
      q='Design your own dice. Draw a net of a cube and write the numbers 1 to 6 on it so that opposite faces add up to 7. Name each pair of opposite faces to prove it works.',
      hint='Pick a net that folds into a cube. Find the pairs of opposite faces first, then write numbers that add up to 7 on each pair.',
      steps=['Designs will vary: check that each pair of opposite faces on your net adds up to 7.', 'Model: a row of four squares 2, 1, 5, 6 with a 3 above the 1 and a 4 below the 1.', 'Opposite pairs: 2 and 5, 1 and 6 (first and third, second and fourth in the row), and 3 and 4 (above and below).'],
      src=['Design your own dice.']),
    D(id='G6', tier='challenge', no='Go further 6', label='G6', type='number', answer=6, skill='shading for symmetry', svg=grid_cells_fig(set(), 3, 3, 48, YEL, False, False, ('v',), 'A 3 by 3 grid with an up-down dashed line through the middle.'),
      check=lambda: sym_pairs_n(3),
      q='In how many ways can you shade exactly 2 squares of a 3 by 3 grid so that the up-down line through the middle is a line of symmetry?', hint='Each shaded square needs a partner the same distance from the line on the other side. List the possibilities in order.',
      steps=['Both squares in the middle column: 3 ways (top and middle, top and bottom, middle and bottom).', 'One square in each side column, in the same row: 3 ways.', '3 + 3 = 6 ways.'],
      src=['In how many ways can you shade exactly 2 squares of a 3 by 3 grid so that the up-down line through the middle is a line of symmetry?']),
    D(id='G7a', tier='challenge', no='Go further 7', label='G7', type='text', accept=fiveacc(), shown=', '.join(squares_name(FIVE[0])), skill='shading for symmetry', svg=grid3(),
      accept_prefix=False, check=lambda: ', '.join(squares_name(FIVE[0])),
      q='Shade exactly 5 squares of a 3 by 3 grid so that the pattern has 4 lines of symmetry. There are 2 ways. Type the 5 squares of one way, like A1, with commas.',
      hint='A pattern with 4 lines of symmetry looks the same after every fold: up-down, across and both corners. Which squares share a fold-partner?',
      steps=['One way: the middle square and the 4 corners (A1, C1, B2, A3, C3), like an X.', 'The other way: the middle square and the 4 squares in the middle of each side (B1, A2, B2, C2, B3), like a plus.'],
      src=['Shade exactly 5 squares of a 3 by 3 grid so that the pattern has 4 lines of symmetry. There are 2 ways.']),
    D(id='G7b', tier='challenge', no='Go further 7', label='G7 both', type='selfcheck', paper=True, skill='shading for symmetry', svg=grid3(), check=lambda: [squares_name(s) for s in FIVE],
      sol_fig=lambda f: side_by_side([grid_cells_fig(set(FIVE[i]), 3, 3, 40, YEL, False, False, (), 'A 3 by 3 pattern.') for i in (0, 1)], 'The two patterns of 5 shaded squares with 4 lines of symmetry.'),
      q='Now find BOTH ways. Shade each pattern on paper, then compare with the two patterns shown after you submit.', hint='Once you have one pattern, look for a different one that still has all 4 folds.',
      steps=['The two patterns are the X (the middle and the 4 corners) and the plus (the middle and the 4 side squares).', 'Both have the up-down, across and two corner-to-corner lines of symmetry.'],
      src=['There are 2 ways. Find both.']),
]

finish(ITEMS)

VARIANTS = {
    'T1': dict(
        base=dict(a=3, b=2, c=1),
        tpl=dict(vars=dict(a=[3, 4, 5], b=[2, 3], c=[1, 2]),
                 q='A cuboid is {a} cm long, {b} cm wide and {c} cm high. Its net is drawn on 1 cm squared paper. How many squares does the net cover?', answer='2*(a*b+a*c+b*c)',
                 hint='A cuboid has 6 faces, in 3 pairs. Find the number of squares on each pair of faces.',
                 steps=['The three pairs of faces have {a} × {b}, {a} × {c} and {b} × {c} squares each.', 'Double each and add: the net covers {ans} squares.']),
        fig=lambda e: cuboid_fig(e['a'], e['b'], e['c']),
        oracle=lambda e: cuboid_faces(e['a'], e['b'], e['c'])),
    'T2a': dict(
        base=dict(t=3),
        tpl=dict(vars=dict(t=[1, 2, 3, 4, 5, 6]),
                 q='Ben puts a dice on the table. The top face shows {t}. What number is on the bottom face?', answer='7-t', hint='Which face is opposite the top? Opposite faces add up to 7.',
                 steps=['The bottom face is opposite the top face.', '{t} + {ans} = 7, so the bottom is {ans}.']),
        oracle=lambda e: next(v for v in range(1, 7) if v + e['t'] == 7)),
    'T3': dict(
        base=dict(S=19),
        tpl=dict(vars=dict(S=[15, 16, 17, 18, 19, 20]),
                 q='A dice is on a table. Mei walks round it and can see the top and the four side faces. The numbers she can see add up to {S}. What number is on the bottom face?',
                 answer='21-S', hint='How much do all six faces add up to? Which face is Mei not counting?',
                 steps=['All six faces add up to 1 + 2 + 3 + 4 + 5 + 6 = 21.', 'Mei cannot see the bottom, so the bottom is 21 − {S} = {ans}.']),
        oracle=lambda e: sum(range(1, 7)) - e['S']),
    'G6': dict(
        base=dict(n=3),
        tpl=dict(vars=dict(n=[3, 5]),
                 q='In how many ways can you shade exactly 2 squares of a {n} by {n} grid so that the up-down line through the middle is a line of symmetry?', answer='n*(n-1)',
                 hint='Each shaded square needs a partner the same distance from the line on the other side. Count the possibilities in order.',
                 steps=['Both squares in the middle column: {n} × ({n} − 1) ÷ 2 ways. One square in each of a pair of side columns, in the same row: the same number of ways.', 'Together that is {ans} ways.']),
        fig=lambda e: grid_cells_fig(set(), e['n'], e['n'], 40 if e['n'] == 3 else 34, YEL, False, False, ('v',), f'A {e["n"]} by {e["n"]} grid with an up-down dashed line through the middle.'),
        oracle=lambda e: sym_pairs_n(e['n'])),
}
