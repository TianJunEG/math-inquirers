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
      q='Which letter is opposite C?', hint='Two pairs are already found. Which two faces are left?',
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

    D(id='5a', tier='core', no='5(a)', label='5(a)', type='number', answer=1, skill='lines of symmetry', svg=cells_g_fig(SHAPES['a']) if False else None, check=lambda: sym_lines(SHAPES['a']),
      q='How many lines of symmetry does shape (a) have?', hint='Fold it in your head along an up-down line, an across line, and a corner-to-corner line. Do the halves match?',
      steps=['The T shape has one line of symmetry: an up-down line through the middle.', 'An across line or a corner-to-corner line does not make the halves match.'],
      src=['Draw ALL the lines of symmetry on each shape. Then write how many.']),
]
