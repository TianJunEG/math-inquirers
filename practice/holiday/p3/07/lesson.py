"""Online practice for Level 3 (Primary 3, ages 8-10) holiday lesson 7: Area Architects (Area and perimeter).

The questions are the ones printed in the Level 3 holiday workbook (p3/workbook_html.js builds it from p3/content/l7.js: Start here = the lesson's workbook()
pages; Think harder 1 to 4 and Go further 5 to 7 = qbank stretch[0..3] and challenge[-3:]; the Extra question = deck.takeHome (printed as "Take-home");
the Investigation = p3/gifted.json lesson 7).  Every answer is recomputed by an INDEPENDENT checker below (counting squares and the edges of squares, the shoelace
rule for the L-shape, listing every pair of sides, building every shape of 5 squares), never a copy of the printed answer; build_holiday.py stops if a checker and the
printed answer differ.  The figures are the workbook's own data (p3/content/l7.js: the four figures A to D, the L-shape, the staircase, the L of 4 squares), drawn larger,
one per card; the checks just below stop the build if the data here differs from the printed figures.
"""
import itertools, os, re, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *          # noqa: E402,F401
from p3lib import *         # noqa: E402,F401
from p3lib_w4 import *      # noqa: E402,F401

META = dict(level=3, lesson=7, key='p3', title='Area Architects', workbook_title='AREA ARCHITECTS', topic='Area and Perimeter', strand='Area and perimeter',
            sources=['p3/content/l7.js', 'p3/gifted.json'],
            intro=['Area is the amount of flat space inside a shape. We count it in squares: cm² means squares that are 1 cm by 1 cm. Perimeter is the distance all the way round the edge, in cm.',
                   'Use squared paper or tiles if you like, and type the answers here. To find a perimeter, walk round the edge and count the sides of the squares you pass.'])
D4 = figs4()
PR = D4['printed']
SK = 'Area and perimeter'
EXTRA = 'Extra practice. '


def I(**kw):
    kw.setdefault('strand', SK)
    return kw


def one(solutions):
    return solutions[0] if len(solutions) == 1 else None


def find(pred, lo=0, hi=5000):
    for x in range(lo, hi + 1):
        if pred(x):
            return x
    return None


# ---------------------------------------------------------------- the data of the figures equals the printed workbook figures
FIGS = {'A': D4['data']['FA'], 'B': D4['data']['FB'], 'C': D4['data']['FC'], 'D': D4['data']['FD']}
assert PR['l7_q1'].count('<rect ') == sum(len(v) for v in FIGS.values()) + 0, 'figures A to D'      # one rect per square
assert 'points="80,34 212,34 212,100 300,100 300,188 80,188"' in PR['l7_q4']                               # the L-shape: bottom 10, left 7, top 6, right 4
_stair = sorted((int(round((int(x) - 10) / 30)), int(round((int(y) - 6) / 30))) for x, y in re.findall(r'<rect x="(\d+)" y="(\d+)" width="30" height="30" fill="#DDEBF7"', PR['l7_q5']))
assert _stair == sorted((1 + i, 4 - j) for i, j in stair_cells(4)), 'staircase'
_l = sorted((int(round((int(x) - 40) / 30)), int(round((int(y) - 32) / 30))) for x, y in re.findall(r'<rect x="(\d+)" y="(\d+)" width="30" height="30" fill="#DDEBF7"', PR['l7_q6'])[:4])
assert _l == sorted(L6), 'the L of 4 squares'

LW, LH, LTOP, LRIGHT = 10, 7, 6, 4          # the L-shape of Q4 (bottom, left, top, right)
LPOLY = lambda W, H, t, r: [(0, 0), (t, 0), (t, H - r), (W, H - r), (W, H), (0, H)]
FENCE = 18


def gardens(fence):
    """Every rectangle with whole-metre sides that uses the whole fence (length at least the width), longest length first: found by trying every length and width."""
    out = []
    for l in range(fence, 0, -1):
        for w in range(1, l + 1):
            if 2 * (l + w) == fence:
                out.append((l, w))
    return out


def sq_item(letter, area, per, steps):
    cells = FIGS[letter]
    return I(id=f'1{letter}', tier='core', no=f'1 (figure {letter})', label=f'1 {letter}', type='fields', skill='area and perimeter of a figure', answer=[area, per],
             svg=squares_fig(cells, f'Figure {letter}', f'Figure {letter} made of squares that are each 1 cm by 1 cm, on a grid'),
             frame=grp('Area = {f1} cm²      Perimeter = {f2} cm'),
             q=f'Each small square is 1 cm by 1 cm. Find the area (in cm²) and the perimeter (in cm) of figure {letter}. Fill in the boxes.',
             check=lambda: [cell_area(cells), cell_perimeter(cells)],
             hint='Count the squares for the area. For the perimeter, walk all the way round the edge and count the sides of the squares you pass.', steps=steps,
             src=['Each small square is 1 cm by 1 cm. Find the area (in cm²) and the perimeter (in cm) of each figure.'])


def pair_name(a, b):
    return f'{a} and {b}'


def same_area_diff_perim():
    out = []
    for a, b in itertools.combinations('ABCD', 2):
        if cell_area(FIGS[a]) == cell_area(FIGS[b]) and cell_perimeter(FIGS[a]) != cell_perimeter(FIGS[b]):
            out.append(pair_name(a, b))
    return one(out)


def same_perim_diff_area():
    out = []
    for p in {cell_perimeter(FIGS[k]) for k in 'ABCD'}:
        grp_ = [k for k in 'ABCD' if cell_perimeter(FIGS[k]) == p]
        areas = [cell_area(FIGS[k]) for k in grp_]
        if len(grp_) > 1 and len(set(areas)) == len(areas):
            out.append(', '.join(grp_))
    return one(out)


STAIR = stair_cells(4)
STAIR_FULL = [(i, j) for i in range(4) for j in range(4)]
FIVE = polyominoes(5)
CORNERS_7x5 = lambda a, b: [(x, y) for x in range(a) for y in range(b) if (x, y) not in {(0, 0), (a - 1, 0), (0, b - 1), (a - 1, b - 1)}]


def rect_cells(a, b):
    return [(x, y) for x in range(a) for y in range(b)]




def square_to_rect(s):
    """(perimeter of the s by s square, its area, perimeter of the (s+1) by (s-1) rectangle, its area), from the squares."""
    a, b = rect_cells(s, s), rect_cells(s + 1, s - 1)
    return [cell_perimeter(a), cell_area(a), cell_perimeter(b), cell_area(b)]


ITEMS = [
    # ================= Start here (workbook lesson 7, No.1 to No.6)
    sq_item('A', 8, 12, ['Figure A is 4 squares long and 2 squares wide: 4 × 2 = 8 squares, so the area is 8 cm².', 'Walk round the edge: 4 + 2 + 4 + 2 = 12 cm.', 'Area 8 cm², perimeter 12 cm.']),
    sq_item('B', 8, 14, ['Count the squares: 5 in the top row and 3 in the bottom row, 5 + 3 = 8, so the area is 8 cm².', 'Walk round the edge, side by side: 5 + 1 + 2 + 1 + 3 + 2 = 14 cm. (Check: the step can be pushed out to make a 5 by 2 rectangle, 5 + 2 + 5 + 2 = 14.)', 'Area 8 cm², perimeter 14 cm.']),
    sq_item('C', 9, 12, ['Figure C is 3 squares long and 3 squares wide: 3 × 3 = 9 squares, so the area is 9 cm².', 'Walk round the edge: 3 + 3 + 3 + 3 = 12 cm.', 'Area 9 cm², perimeter 12 cm.']),
    sq_item('D', 5, 12, ['Count the squares: 3 in the bottom row and 1 at each end above it, 3 + 2 = 5, so the area is 5 cm².', 'Walk all the way round the edge, including the 3 sides of the gap in the middle: 12 cm.', 'Area 5 cm², perimeter 12 cm.']),
    I(id='1a', tier='core', no='1(a)', label='1(a)', type='choice', skill='area and perimeter of a figure',
      options=[pair_name(a, b) for a, b in itertools.combinations('ABCD', 2)], answer='A and B',
      q='Look at the areas and perimeters of your figures A, B, C and D. Which two figures have the same area but different perimeters?',
      check=same_area_diff_perim,
      hint='Write the area of each figure in a row. Which two are the same? Then check that their perimeters are not the same.',
      steps=['The areas are A 8, B 8, C 9 and D 5. Only A and B have the same area.', 'Their perimeters are different: A has 12 cm and B has 14 cm.', 'So the figures are A and B.'],
      src=['Which two figures have the same area but different perimeters?']),
    I(id='1b', tier='core', no='1(b)', label='1(b)', type='text', skill='area and perimeter of a figure', accept=letter_forms(['A', 'C', 'D']), shown='A, C, D',
      q='Which figures have the same perimeter but different areas? Type the letters with commas.',
      check=same_perim_diff_area,
      hint='Write the perimeter of each figure in a row. Which ones are the same? Then check that their areas are all different.',
      steps=['The perimeters are A 12 cm, B 14 cm, C 12 cm and D 12 cm. A, C and D have the same perimeter.', 'Their areas are 8, 9 and 5 cm², all different.', 'So the figures are A, C and D.'],
      src=['Which figures have the same perimeter but different areas?']),

    I(id='2-len', tier='core', no='2 (lengths)', label='2 lengths', type='set', ordered=True, skill='making a list in order', answer=[8, 7, 6, 5],
      q='Siti uses all of her 18 m of fence to make a rectangular garden with whole-metre sides. List the length (the longer side) of EVERY garden she can make, longest first.',
      check=lambda: [l for l, w in gardens(FENCE)],
      hint='Half of the fence goes along one length and one width together. Start with the shortest width, 1 m, and list in order.',
      steps=['Half of 18 m is 9 m, so length + width = 9.', 'List in order: width 1 and length 8; width 2 and length 7; width 3 and length 6; width 4 and length 5.', 'After that the rectangles just turn round (5 by 4 is the same garden as 4 by 5). The lengths are 8, 7, 6 and 5.'],
      src=['Siti has 18 m of fence. She makes a rectangular garden with the whole fence. Each side is a whole number of metres. List ALL the gardens she can make, in order.']),
    I(id='2-wid', tier='core', no='2 (widths)', label='2 widths', type='set', ordered=True, skill='making a list in order', answer=[1, 2, 3, 4],
      q='Siti has 18 m of fence and makes a rectangular garden with the whole fence. List the width of every garden in the same order as the lengths (longest length first). Type the widths with commas.',
      check=lambda: [w for l, w in gardens(FENCE)],
      hint='For each length, how much of the half-fence is left for the width?',
      steps=['Length + width = 9, so each width is 9 take away its length.', '8 and 1, 7 and 2, 6 and 3, 5 and 4.', 'The widths are 1, 2, 3 and 4.'],
      src=['List ALL the gardens she can make, in order.']),
    I(id='2-area', tier='core', no='2 (areas)', label='2 areas', type='set', ordered=True, skill='area of a rectangle', answer=[8, 14, 18, 20],
      q='Siti has 18 m of fence and makes a rectangular garden with the whole fence. Find the area of every garden, in the same order (longest length first). Type the areas with commas.',
      check=lambda: [l * w for l, w in gardens(FENCE)],
      hint='Area = length × width for each garden. Keep the same order as your lengths.',
      steps=['8 × 1 = 8, 7 × 2 = 14, 6 × 3 = 18, 5 × 4 = 20.', 'The areas are 8, 14, 18 and 20 (in m²).'],
      src=['Length (m) Width (m) Check: perimeter Area (m²)', 'List ALL the gardens she can make, in order.']),
    I(id='2-count', tier='core', no='2 (how many)', label='2 how many', type='number', skill='making a list in order', answer=4,
      q='Siti has 18 m of fence and makes a rectangular garden with the whole fence. Each side is a whole number of metres. How many different gardens can she make? Type the number.',
      check=lambda: len(gardens(FENCE)),
      hint='Count the gardens in your list. A garden turned round is still the same garden, so count it only once.',
      steps=['Length + width = 9. The gardens are 8 by 1, 7 by 2, 6 by 3 and 5 by 4.', 'That is 4 different gardens.'],
      src=['List ALL the gardens she can make, in order.']),
    I(id='2a', tier='core', no='2(a)', label='2(a)', type='fields', skill='area of a rectangle', answer=[5, 4], frame=grp('Length {f1} m      Width {f2} m'),
      q='Siti has 18 m of fence and makes a rectangular garden with the whole fence, with whole-metre sides. Which garden has the biggest area? Write the length (the longer side) and the width.',
      check=lambda: (lambda g: [g[0], g[1]])(max(gardens(FENCE), key=lambda lw: lw[0] * lw[1])),
      hint='Find the area of every garden you can make. Which area is the biggest?',
      steps=['The areas are 8, 14, 18 and 20 m².', 'The biggest is 20 m², from the 5 m by 4 m garden.', 'The gardens that are closer to a square have the bigger area.'],
      src=['Which garden has the biggest area?']),

    I(id='3', tier='core', no='3', label='3', type='number', skill='perimeter and area of a square', answer=25,
      q='A square has the same perimeter as a rectangle 7 cm long and 3 cm wide. Hint: first walk round the rectangle. What is the area of the square? Type the number.',
      check=lambda: (lambda p: (lambda s: s * s)(find(lambda s: 4 * s == p)))(2 * 7 + 2 * 3),
      hint='First find the perimeter of the rectangle. A square has 4 equal sides.',
      steps=['The perimeter of the rectangle is 7 + 3 + 7 + 3 = 20 cm.', 'The square has 4 equal sides: 20 ÷ 4 = 5 cm each.', 'Its area is 5 × 5 = 25 cm².'],
      src=['A square has the same perimeter as a rectangle 7 cm long and 3 cm wide. Hint: first walk round the rectangle. What is the area of the square?']),

    I(id='4-miss', tier='core', no='4 (missing sides)', label='4 sides', type='fields', skill='finding missing sides', answer=[4, 3], frame=grp('Across {f1} cm      Down {f2} cm'),
      svg=lshape_fig(LW, LH, LTOP, LRIGHT, 'An L-shaped figure. Bottom 10 cm, left side 7 cm, top 6 cm, right side 4 cm. The step in the top right corner has no lengths marked.'),
      q='Find the two missing sides first. The step in the top right corner has no lengths marked. How long is the missing side going across, and the missing side going down?',
      check=lambda: (lambda P: [P[3][0] - P[2][0], P[2][1] - P[1][1]])(LPOLY(LW, LH, LTOP, LRIGHT)),      # the step: across from (6, 3) to (10, 3), down from (6, 0) to (6, 3)
      hint='The bottom of the figure is 10 cm. The top part is 6 cm. How much is the rest? Do the same for the sides going down.',
      steps=['Across: the bottom is 10 cm and the top is 6 cm, so the step goes across 10 - 6 = 4 cm.', 'Down: the left side is 7 cm and the right side is 4 cm, so the step goes down 7 - 4 = 3 cm.', 'The missing sides are 4 cm and 3 cm.'],
      src=['Find the two missing sides first. Then find the area and the perimeter of this figure.']),
    I(id='4a', tier='core', no='4(a)', label='4(a)', type='number', skill='area of an L-shape', answer=58,
      svg=lshape_fig(LW, LH, LTOP, LRIGHT, 'An L-shaped figure. Bottom 10 cm, left side 7 cm, top 6 cm, right side 4 cm. The step in the top right corner has no lengths marked.'),
      q='Find the area of this figure, in cm². Hint: you can cut the figure into two rectangles. Type the number.',
      check=lambda: int(poly_area(LPOLY(LW, LH, LTOP, LRIGHT))),
      hint='Cut the figure into two rectangles. Find the area of each, then add.',
      steps=['Cut off the top left piece: 6 cm by 7 cm, area 6 × 7 = 42 cm².', 'The bottom right piece is 4 cm by 4 cm, area 4 × 4 = 16 cm².', '42 + 16 = 58 cm². (Check the other way: 10 × 7 = 70, take away the corner 4 × 3 = 12, 70 - 12 = 58.)'],
      src=['Hint: you can cut the figure into two rectangles.', 'Area = __________ cm²']),
    I(id='4b', tier='core', no='4(b)', label='4(b)', type='number', skill='perimeter of an L-shape', answer=34,
      svg=lshape_fig(LW, LH, LTOP, LRIGHT, 'An L-shaped figure. Bottom 10 cm, left side 7 cm, top 6 cm, right side 4 cm. The step in the top right corner has no lengths marked.'),
      q='Find the perimeter of this figure, in cm. Type the number.',
      check=lambda: poly_perimeter(LPOLY(LW, LH, LTOP, LRIGHT)),
      hint='Find the two missing sides first. Then add all the sides, or push the step out.',
      steps=['The sides are 6, 3, 4, 4, 10 and 7 cm. 6 + 3 + 4 + 4 + 10 + 7 = 34 cm.', 'Or push the step out to make a 10 by 7 rectangle: 10 + 7 + 10 + 7 = 34 cm.'],
      src=['Perimeter = __________ cm']),

    I(id='5a', tier='core', no='5(a)', label='5(a)', type='number', skill='area of a staircase', answer=10,
      svg=stairs_fig(4, 'A staircase on a 1 cm grid: columns of 4, 3, 2 and 1 squares standing side by side'),
      q='Look at this staircase. Each small square is 1 cm by 1 cm. What is its area, in cm²? Type the number.',
      check=lambda: cell_area(STAIR),
      hint='Count the squares in each column. Then add the columns.',
      steps=['The columns have 4, 3, 2 and 1 squares.', '4 + 3 + 2 + 1 = 10 squares.', 'The area is 10 cm².'],
      src=['Look at this staircase.', 'What is its area?   ________ cm²']),
    I(id='5b', tier='core', no='5(b)', label='5(b)', type='number', skill='perimeter of a staircase', answer=16,
      svg=stairs_fig(4, 'A staircase on a 1 cm grid: columns of 4, 3, 2 and 1 squares standing side by side'),
      q='Look at this staircase. Each small square is 1 cm by 1 cm. What is its perimeter, in cm? Type the number.',
      check=lambda: cell_perimeter(STAIR),
      hint='Walk all the way round the edge and count the sides of the squares. Or push the steps out.',
      steps=['Push the steps up and out. The staircase has the same perimeter as a 4 by 4 square.', '4 + 4 + 4 + 4 = 16 cm.', 'Counting the sides of the squares round the edge also gives 16 cm.'],
      src=['What is its perimeter?   ________ cm']),
    I(id='5c-per', tier='core', no='5(c) perimeter', label='5(c) perim.', type='choice', skill='perimeter and area', options=['The perimeter goes up', 'The perimeter goes down', 'The perimeter stays the same'],
      answer='The perimeter stays the same', svg=stairs_fig(4, 'The staircase with the empty squares that fill it up to a 4 by 4 square shown as dashed boxes', gaps=True),
      q='Ben fills in the gaps with squares to make a 4 by 4 square. What happens to the perimeter?',
      check=lambda: (lambda a, b: 'The perimeter stays the same' if a == b else ('The perimeter goes up' if b > a else 'The perimeter goes down'))(cell_perimeter(STAIR), cell_perimeter(STAIR_FULL)),
      hint='Find the perimeter of the 4 by 4 square. Compare it with the perimeter of the staircase.',
      steps=['The 4 by 4 square has perimeter 4 + 4 + 4 + 4 = 16 cm.', 'The staircase also has a perimeter of 16 cm.', 'So the perimeter stays the same.'],
      src=['Ben fills in the gaps with squares to make a 4 by 4 square. What happens to the perimeter? What happens to the area?']),
    I(id='5c-area', tier='core', no='5(c) area', label='5(c) area', type='choice', skill='perimeter and area', options=['The area stays the same', 'The area goes up', 'The area goes down'],
      answer='The area goes up', svg=stairs_fig(4, 'The staircase with the empty squares that fill it up to a 4 by 4 square shown as dashed boxes', gaps=True),
      q='Ben fills in the gaps with squares to make a 4 by 4 square. What happens to the area?',
      check=lambda: (lambda a, b: 'The area stays the same' if a == b else ('The area goes up' if b > a else 'The area goes down'))(cell_area(STAIR), cell_area(STAIR_FULL)),
      hint='Ben adds squares. Does the figure cover more squares or fewer squares than before?',
      steps=['The staircase covers 10 squares.', 'The 4 by 4 square covers 16 squares.', 'So the area goes up.'],
      src=['What happens to the perimeter? What happens to the area?']),
    I(id='5c-more', tier='core', no='5(c) how much', label='5(c) more', type='number', skill='perimeter and area', answer=6,
      svg=stairs_fig(4, 'The staircase with the empty squares that fill it up to a 4 by 4 square shown as dashed boxes', gaps=True),
      q='Ben fills in the gaps with squares to make a 4 by 4 square. What is the difference between the two areas, in cm²? Type the number.',
      check=lambda: cell_area(STAIR_FULL) - cell_area(STAIR),
      hint='Count the empty squares Ben fills in, or take the area of the staircase away from the area of the 4 by 4 square.',
      steps=['The 4 by 4 square has area 16 cm². The staircase has area 10 cm².', '16 - 10 = 6.', 'The area goes up by 6 cm².'],
      src=['What happens to the area?']),

    I(id='6a', tier='core', no='6(a)', label='6(a)', type='text', skill='perimeter and area', accept=['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I'], shown='any of A, B, C, D, F, G, H, I', accept_prefix=False,
      svg=cand_fig(),
      q='This L shape is made of 4 squares and its perimeter is 10 cm. Add ONE square that shares a whole side with the L (places A to I). Which place makes the perimeter 12 cm? Type one letter.',
      check=lambda: [k for k in CANDS if perimeter_with(k) == 12][0],
      hint='Put a new square in one place. Count the edges round the new shape, or count how many sides of the new square touch the L.',
      steps=['The L has a perimeter of 10 cm. A new square adds 4 sides and hides the sides that touch the L (one on the new square and one on the L for each touch).', 'A new square that touches the L along ONE side gives 12 cm. This works for A, B, C, D, F, G, H and I.', 'Only E touches two sides, so E leaves the perimeter at 10 cm.'],
      src=['(if time) This L shape is made of 4 squares. Its perimeter is 10 cm. Add ONE square that shares a whole side with the L. Shade it.', 'In grid (a), add a square so that the perimeter becomes 12 cm.']),
    I(id='6b', tier='core', no='6(b)', label='6(b)', type='text', skill='perimeter and area', accept=['E'], shown='E', accept_prefix=False, svg=cand_fig(),
      q='The same L shape has a perimeter of 10 cm. Add ONE square that shares a whole side with the L. Which place, A to I, keeps the perimeter at 10 cm? Type the letter.',
      check=lambda: one([k for k in CANDS if perimeter_with(k) == 10]),
      hint='Look for a place where the new square touches the L along more than one side.',
      steps=['A new square hides two of its own sides (and two sides of the L) when it touches the L along two sides.', 'Place E touches the middle square and the bottom square of the L, so the perimeter stays 10 cm.', 'No other place touches two sides.'],
      src=['In grid (b), add a square so that the perimeter stays 10 cm.']),
    I(id='6c', tier='core', no='6(c)', label='6(c)', type='choice', skill='perimeter and area', options=['Yes', 'No'], answer='No', svg=cand_fig(),
      q='Can you add one square to the L so that the perimeter becomes 8 cm? The new square must share a whole side with the L.',
      check=lambda: 'Yes' if any(perimeter_with(k) == 8 for k in CANDS) else 'No',
      hint='Try each place A to I and find the perimeter. Is any of them 8 cm?',
      steps=['Try each place. The perimeter is 12 cm in eight places and 10 cm in place E.', 'No place gives 8 cm.', 'So the answer is No.'],
      src=['Can you add one square so that the perimeter becomes 8 cm? Explain.']),
    I(id='6c-why', tier='core', no='6(c) explain', label='6(c) explain', type='selfcheck', open=True, marking_mode='self', skill='explaining why', svg=cand_fig(),
      q='Explain how you know whether the perimeter of the L can become 8 cm by adding one square. Write your idea, then compare with the answer shown.',
      check=lambda: sorted({perimeter_with(k) for k in CANDS}, reverse=True),
      hint='A new square can touch the L along 1 side, 2 sides, or more. How many sides would it have to touch to make the perimeter 8 cm?',
      steps=['Each side of the new square that touches the L hides 2 sides (one of the new square, one of the L) and the new square brings 4 sides.', 'To go from 10 cm down to 8 cm the new square would have to touch the L along 3 sides.', 'No place next to this L touches 3 sides, so the perimeter can only be 12 cm or 10 cm.'],
      src=['Can you add one square so that the perimeter becomes 8 cm? Explain.']),

    # ================= Investigation (Investigation and look back page, No.8: What if we change it? What stays the same?)
    I(id='I8-easy', tier='invest', no='8 easy step', label='Inv easy', type='fields', skill='area and perimeter', answer=[16, 16, 15, 16],
      q='A square has sides of 4 cm. Make it 1 cm longer one way and 1 cm shorter the other way: a 5 cm by 3 cm rectangle. Work out the area and perimeter of each.',
      frame=grp('Square: area {f1} cm²      perimeter {f2} cm      Rectangle: area {f3} cm²      perimeter {f4} cm'),
      check=lambda: (lambda r: [r[1], r[0], r[3], r[2]])(square_to_rect(4)),
      hint='Area = length × width. Perimeter = all four sides added. Do the 4 by 4 square first.',
      steps=['The 4 by 4 square: area 4 × 4 = 16 cm², perimeter 4 × 4 = 16 cm.', 'The 5 by 3 rectangle: area 5 × 3 = 15 cm², perimeter 5 + 3 + 5 + 3 = 16 cm.', 'The numbers are 16, 16, 15 and 16.'],
      src=['Easy first step: work out the area and perimeter of the 4 by 4 square and of the 5 by 3 rectangle.']),
    I(id='I8a', tier='invest', no='8(a)', label='Inv 8(a)', type='choice', skill='noticing what changes', answer='The perimeter stays the same and the area is smaller',
      options=['The area stays the same and the perimeter is smaller', 'Both stay the same', 'The perimeter stays the same and the area is smaller', 'Both are smaller', 'The perimeter stays the same and the area is bigger'],
      q='A 4 cm square becomes a 5 cm by 3 cm rectangle (1 cm longer one way, 1 cm shorter the other way). Compare the rectangle with the square. What changed and what stayed the same?',
      check=lambda: (lambda r: 'The perimeter stays the same and the area is smaller' if r[0] == r[2] and r[3] < r[1] else 'other')(square_to_rect(4)),
      hint='Work out the area and perimeter of both, then compare each pair of numbers.',
      steps=['Square: perimeter 16 cm, area 16 cm². Rectangle: perimeter 16 cm, area 15 cm².', 'The perimeter did not change. The area went down by 1 cm².'],
      src=['Work out the area and perimeter of the 5 by 3 rectangle. What changed? What stayed the same?']),
    I(id='I8b6', tier='invest', no='8(b) 6 cm', label='Inv 6 cm', type='fields', skill='area and perimeter', answer=[24, 36, 24, 35],
      q='Do the same for a square with sides of 6 cm. Make it 1 cm longer one way and 1 cm shorter the other way: a 7 cm by 5 cm rectangle. Fill in the boxes.',
      frame=grp('Square: perimeter {f1} cm      area {f2} cm²      Rectangle: perimeter {f3} cm      area {f4} cm²'),
      check=lambda: square_to_rect(6),
      hint='Perimeter: add all four sides. Area: length × width. Do the square first, then the rectangle.',
      steps=['The 6 by 6 square: perimeter 6 × 4 = 24 cm, area 6 × 6 = 36 cm².', 'The 7 by 5 rectangle: perimeter 7 + 5 + 7 + 5 = 24 cm, area 7 × 5 = 35 cm².', 'The numbers are 24, 36, 24 and 35.'],
      src=['Do the same for a 6 cm square (7 by 5) and a 10 cm square (11 by 9). Fill in the table.']),
    I(id='I8b10', tier='invest', no='8(b) 10 cm', label='Inv 10 cm', type='fields', skill='area and perimeter', answer=[40, 100, 40, 99],
      q='Now a square with sides of 10 cm. Make it 1 cm longer one way and 1 cm shorter the other way: an 11 cm by 9 cm rectangle. Fill in the boxes.',
      frame=grp('Square: perimeter {f1} cm      area {f2} cm²      Rectangle: perimeter {f3} cm      area {f4} cm²'),
      check=lambda: square_to_rect(10),
      hint='Perimeter: add all four sides. Area: length × width. Do the square first, then the rectangle.',
      steps=['The 10 by 10 square: perimeter 10 × 4 = 40 cm, area 10 × 10 = 100 cm².', 'The 11 by 9 rectangle: perimeter 11 + 9 + 11 + 9 = 40 cm, area 11 × 9 = 99 cm².', 'The numbers are 40, 100, 40 and 99.'],
      src=['Do the same for a 6 cm square (7 by 5) and a 10 cm square (11 by 9). Fill in the table.']),
    I(id='I8own', tier='invest', no='8(b) my own', label='Inv my own', type='selfcheck', open=True, marking_mode='open', skill='testing an idea',
      q='Choose a square of your own. Make it 1 cm longer one way and 1 cm shorter the other way. Work out the perimeter and the area of both. Does your square do the same as the others? Then compare with the example shown.',
      check=lambda: all(square_to_rect(n)[0] == square_to_rect(n)[2] and square_to_rect(n)[1] - square_to_rect(n)[3] == 1 for n in range(2, 41)),
      hint='Pick a side that is easy to work with, like 5 or 8. Work out the square first, then the rectangle.',
      steps=['Answers vary. Example: an 8 cm square becomes a 9 by 7 rectangle.', 'Square: perimeter 32 cm, area 64 cm². Rectangle: perimeter 9 + 7 + 9 + 7 = 32 cm, area 9 × 7 = 63 cm².', 'Same as the others, just with different numbers.'],
      src=['Then choose a square of your own.']),
    I(id='I8c', tier='invest', no='8(c)', label='Inv 8(c)', type='choice', skill='noticing what stays the same', options=['No, it only works for some squares', 'Yes, it works for every square'],
      answer='Yes, it works for every square',
      q='You tried a 4 cm, a 6 cm and a 10 cm square, and one of your own. Do you think what you found works for EVERY square? Test one more square if you like.',
      check=lambda: 'Yes, it works for every square' if all(square_to_rect(n)[0] == square_to_rect(n)[2] and square_to_rect(n)[1] - square_to_rect(n)[3] == 1 for n in range(2, 41)) else 'No, it only works for some squares',
      hint='Pick a square you have not used yet, like 7 or 12. Does it do the same as the others?',
      steps=['A square with sides 7 cm: perimeter 28 cm, area 49 cm². The 8 by 6 rectangle: perimeter 28 cm, area 48 cm².', 'It does the same again. It works for every square.', 'The next question asks why.'],
      src=['Is it always true? Draw the 4 by 4 square and explain what happens to the area.']),
    I(id='I8c-why', tier='invest', no='8(c) explain', label='Inv explain', type='selfcheck', open=True, marking_mode='self', skill='explaining why',
      sol_fig=lambda g: move_row_fig('The bottom row of 4 squares moved to the right side makes a column of 3 squares tall with 1 square left over'),
      q='Draw the 4 by 4 square. Make it 1 cm longer one way and 1 cm shorter the other way. Explain what happens to the area and why. Write your idea, then compare with the answer shown.',
      check=lambda: [square_to_rect(4), square_to_rect(9)],
      hint='Take the bottom row of the square away. Where could you put those squares so that the shape is 1 cm longer?',
      steps=['Move the bottom row of 4 squares to the right side of the square.', 'The new column is only 3 squares tall (the rectangle is 3 cm tall now), so 3 squares fit and 1 square is left over.', 'The area is 1 cm² smaller. The perimeter does not change because the shape is still 5 cm by 3 cm, with the same distance round.'],
      src=['Is it always true? Draw the 4 by 4 square and explain what happens to the area.']),

    # ================= Think harder (workbook Think harder, No.1 to No.4)
    I(id='T1-len', tier='stretch', no='T1 (lengths)', label='T1 lengths', type='set', ordered=True, skill='making a list in order', answer=[24, 12, 8, 6],
      q='Find ALL the rectangles with whole-cm sides and an area of 24 cm². List the length (the longer side) of each one, longest first. Type the lengths with commas.',
      check=lambda: [l for l in range(24, 0, -1) for w in range(1, l + 1) if l * w == 24],
      hint='Find pairs of whole numbers that multiply to make 24. Start with a width of 1 and list in order.',
      steps=['The pairs are 24 × 1, 12 × 2, 8 × 3 and 6 × 4.', '(After 6 × 4 the next pair would be 4 × 6, the same rectangle turned round.)', 'The lengths are 24, 12, 8 and 6.'],
      src=['Find all the rectangles with whole-cm sides and an area of 24 cm². Which one has the shortest perimeter?']),
    I(id='T1-per', tier='stretch', no='T1 (perimeters)', label='T1 perims', type='set', ordered=True, skill='perimeter of a rectangle', answer=[50, 28, 22, 20],
      q='Find ALL the rectangles with whole-cm sides and an area of 24 cm². Work out the perimeter of each one, in the same order (longest length first). Type the perimeters with commas.',
      check=lambda: [2 * (l + w) for l in range(24, 0, -1) for w in range(1, l + 1) if l * w == 24],
      hint='Perimeter = length + width + length + width. Keep your list in the same order.',
      steps=['24 by 1: 24 + 1 + 24 + 1 = 50 cm. 12 by 2: 28 cm. 8 by 3: 22 cm. 6 by 4: 20 cm.', 'The perimeters are 50, 28, 22 and 20 cm.'],
      src=['Find all the rectangles with whole-cm sides and an area of 24 cm². Which one has the shortest perimeter?']),
    I(id='T1-best', tier='stretch', no='T1 (shortest)', label='T1 shortest', type='fields', skill='perimeter of a rectangle', answer=[6, 4], frame=grp('Length {f1} cm      Width {f2} cm'),
      q='Of all the rectangles with whole-cm sides and an area of 24 cm², which one has the shortest perimeter? Write its length (the longer side) and its width.',
      check=lambda: (lambda g: [g[0], g[1]])(min([(l, w) for l in range(24, 0, -1) for w in range(1, l + 1) if l * w == 24], key=lambda lw: 2 * (lw[0] + lw[1]))),
      hint='Find the perimeter of each rectangle with an area of 24 cm². Which perimeter is the smallest?',
      steps=['The perimeters are 50, 28, 22 and 20 cm.', 'The shortest is 20 cm.', 'It is the 6 cm by 4 cm rectangle.'],
      src=['Which one has the shortest perimeter?']),
    I(id='T2', tier='stretch', no='T2', label='T2', type='number', skill='area and perimeter', answer=36,
      q='A rectangle is 12 cm long. Its perimeter is 30 cm. Find its area, in cm². Type the number.',
      check=lambda: (lambda w: 12 * w)(find(lambda w: 2 * (12 + w) == 30)),
      hint='Half of the perimeter is one length plus one width. What is left for the width?',
      steps=['Half of 30 is 15, so length + width = 15.', 'The width is 15 - 12 = 3 cm.', 'The area is 12 × 3 = 36 cm².'],
      src=['A rectangle is 12 cm long. Its perimeter is 30 cm. Find its area.']),
    I(id='T3-which', tier='stretch', no='T3 (bigger)', label='T3 bigger', type='choice', skill='area and perimeter', options=['The rectangle', 'The square', 'They have the same area'], answer='The square',
      q='A rectangle 8 cm by 2 cm and a square have the same perimeter. Which has the bigger area?',
      check=lambda: (lambda p, s: 'The square' if s * s > 8 * 2 else ('The rectangle' if s * s < 8 * 2 else 'They have the same area'))(2 * (8 + 2), find(lambda s: 4 * s == 2 * (8 + 2))),
      hint='Find the perimeter of the rectangle first. Then find the side of the square.',
      steps=['The perimeter of the rectangle is 8 + 2 + 8 + 2 = 20 cm.', 'The square has 4 equal sides: 20 ÷ 4 = 5 cm. Its area is 5 × 5 = 25 cm².', 'The rectangle has area 8 × 2 = 16 cm². The square has the bigger area.'],
      src=['A rectangle 8 cm by 2 cm and a square have the same perimeter. Which has the bigger area, and by how much?']),
    I(id='T3-by', tier='stretch', no='T3 (by how much)', label='T3 by', type='number', skill='area and perimeter', answer=9,
      q='A rectangle 8 cm by 2 cm and a square have the same perimeter. How many cm² bigger is the bigger area than the smaller area? Type the number.',
      check=lambda: (lambda s: abs(s * s - 8 * 2))(find(lambda s: 4 * s == 2 * (8 + 2))),
      hint='Work out both areas, then find the difference.',
      steps=['The rectangle has area 16 cm². The square (sides 5 cm) has area 25 cm².', '25 - 16 = 9.', 'The difference is 9 cm².'],
      src=['Which has the bigger area, and by how much?']),
    I(id='T4', tier='stretch', no='T4', label='T4', type='number', skill='perimeter of a rectangle', answer=18,
      q='A square with sides of 6 cm is cut into two rectangles of the same size. What is the perimeter of each rectangle, in cm? Type the number.',
      check=lambda: (lambda w: 2 * (6 + w))(find(lambda w: 2 * w == 6)),
      hint='How wide is each rectangle? Draw the square and the cut on paper.',
      steps=['Cutting the square into two rectangles of the same size cuts one side in half: 6 ÷ 2 = 3 cm.', 'Each rectangle is 6 cm by 3 cm.', 'The perimeter is 6 + 3 + 6 + 3 = 18 cm.'],
      src=['A square with sides of 6 cm is cut into two rectangles of the same size. What is the perimeter of each rectangle?']),

    # ================= Go further (workbook Go further, No.5 to No.7) and the Extra question (printed as "Take-home")
    I(id='G5', tier='challenge', no='G5', label='G5', type='selfcheck', open=True, marking_mode='open', skill='making up a puzzle',
      q='Make up your own rectangle puzzle. Choose a rectangle with whole-cm sides, then give a partner only TWO clues about it (for example its area and its perimeter). Check that only ONE rectangle fits both clues. Which two clues did you choose, and why do they work?',
      check=lambda: [(l, w) for l in range(36, 0, -1) for w in range(1, l + 1) if l * w == 36 and 2 * (l + w) == 26],
      hint='Pick the secret rectangle first. Write its area and its perimeter. List all rectangles with that area. Does only one have that perimeter?',
      steps=['Answers vary. Check that the clues fit the secret rectangle and that listing the rectangles for the first clue leaves exactly one for the second.', 'Example: "Area 36 cm² and perimeter 26 cm". The rectangles with area 36 cm² are 36 by 1 (perimeter 74), 18 by 2 (40), 12 by 3 (30), 9 by 4 (26) and 6 by 6 (24), so only 9 by 4 fits.'],
      src=['Make up your own rectangle puzzle. Choose a rectangle with whole-cm sides, then give a partner only TWO clues about it (for example its area and its perimeter).']),
    I(id='G6', tier='challenge', no='G6', label='G6', type='fields', skill='area and perimeter', answer=[24, 20], frame=grp('Biggest {f1} cm      Smallest {f2} cm'),
      q='Ali joins 5 same-size squares with sides of 2 cm, whole sides touching. What is the biggest perimeter his shape can have? What is the smallest? Fill in the boxes.',
      check=lambda: [2 * max(cell_perimeter(p) for p in FIVE), 2 * min(cell_perimeter(p) for p in FIVE)],
      hint='Draw some different shapes with 5 squares. For each one, count the sides of the squares round the edge, then multiply by 2 cm.',
      steps=['Count the sides of the small squares round the edge, then multiply by 2 cm for each side.', 'The most is 12 sides (for example a row of 5 squares): 12 × 2 = 24 cm. The fewest is 10 sides (a 2 by 2 square with one more square on a side): 10 × 2 = 20 cm.', 'Biggest 24 cm, smallest 20 cm.'],
      src=['Ali joins 5 same-size squares with sides of 2 cm, whole sides touching. What is the biggest perimeter his shape can have? The smallest?']),
    I(id='G7', tier='challenge', no='G7', label='G7', type='fields', skill='area and perimeter', answer=[31, 24], frame=grp('Area {f1} cm²      Perimeter {f2} cm'),
      svg=squares_fig(CORNERS_7x5(7, 5), 'The new figure', 'A rectangle 7 cm by 5 cm with a 1 cm square cut out of each of its 4 corners, on a grid', cols=9, rows=7, c=32),
      q='A rectangle 7 cm by 5 cm has a 1 cm square cut out of each of its 4 corners. Find the new area and the new perimeter. Fill in the boxes.',
      check=lambda: [cell_area(CORNERS_7x5(7, 5)), cell_perimeter(CORNERS_7x5(7, 5))],
      hint='Area: take the squares that were cut out away from the whole rectangle. Perimeter: look at what happens to the edge at one corner.',
      steps=['Area: 7 × 5 = 35 cm², and 4 squares are cut out: 35 - 4 = 31 cm².', 'Perimeter: at each corner the cut takes away 2 cm of edge and adds 2 cm of new edge, so push the cut corners out and you get the 7 by 5 rectangle back: 7 + 5 + 7 + 5 = 24 cm.', 'Area 31 cm², perimeter 24 cm.'],
      src=['A rectangle 7 cm by 5 cm has a 1 cm square cut out of each of its 4 corners. Find the new area and the new perimeter.']),
    I(id='TH-a', tier='challenge', no='Extra (a)', label='Extra (a)', type='number', skill='area of a square', answer=7,
      q=EXTRA + 'A square has an area of 49 cm². How long is each side, in cm? Type the number.',
      check=lambda: find(lambda s: s * s == 49),
      hint='Which number multiplied by itself makes 49?',
      steps=['The area of a square is side × side.', '7 × 7 = 49.', 'Each side is 7 cm.'],
      src=['A square has an area of 49 cm². How long is each side?']),
]

for _d in ITEMS:
    if _d['type'] == 'selfcheck' and 'marking_mode' not in _d:
        _d['marking_mode'] = 'self'
assert [k for k in CANDS if perimeter_with(k) == 12] == ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I'] and perimeter_with('E') == 10 and cell_perimeter(L6) == 10


# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
def _fence_count(e):
    return len(gardens(e['F']))


def _lfig(env):
    return lshape_fig(env['W'], env['H'], env['t'], env['r'], f'An L-shaped figure. Bottom {env["W"]} cm, left side {env["H"]} cm, top {env["t"]} cm, right side {env["r"]} cm. The step in the top right corner has no lengths marked.')


def _sfig(env):
    return stairs_fig(env['n'], f'A staircase on a 1 cm grid: columns of {env["n"]} down to 1 squares standing side by side')


VARIANTS = {
    '2-count': dict(
        base=dict(F=18),
        tpl=dict(vars=dict(F=[14, 18, 22, 26, 30, 34]), derive=dict(S='F//2'),
                 q='Siti has {F} m of fence and makes a rectangular garden with the whole fence. Each side is a whole number of metres. How many different gardens can she make? Type the number.',
                 answer='S//2', hint='Half of the fence is one length plus one width, {S} m. List the gardens in order, starting with a width of 1 m.',
                 steps=['Length + width = {S}.', 'List the gardens in order until the rectangles start to turn round.', 'Siti can make {ans} different gardens.']),
        oracle=lambda e: _fence_count(e)),
    '3': dict(
        base=dict(l=7, w=3),
        tpl=dict(vars=dict(l=[7, 9, 11, 13], w=[1, 3, 5]), derive=dict(S='(l+w)//2'),
                 q='A square has the same perimeter as a rectangle {l} cm long and {w} cm wide. Hint: first walk round the rectangle. What is the area of the square? Type the number.',
                 answer='S*S', hint='First find the perimeter of the rectangle. A square has 4 equal sides.',
                 steps=['Find the perimeter of the rectangle: {l} + {w} + {l} + {w}.', 'Share the perimeter between the 4 sides of the square to find one side.', 'The area of the square is {ans} cm².']),
        oracle=lambda e: (lambda s: s * s)(find(lambda s: 4 * s == 2 * (e['l'] + e['w'])))),
    '4a': dict(
        base=dict(W=10, H=7, t=6, r=4),
        tpl=dict(vars=dict(W=[9, 10, 12], H=[7, 8], t=[5, 6, 7], r=[3, 4, 5]),
                 q='Find the area of this figure, in cm². The bottom is {W} cm, the left side is {H} cm, the top is {t} cm and the right side is {r} cm. Hint: you can cut the figure into two rectangles. Type the number.',
                 answer='W*H-(W-t)*(H-r)', hint='Cut the figure into two rectangles. Find the area of each, then add. Or fill in the corner and take it away.',
                 steps=['Find the missing sides of the step first.', 'Cut the figure into two rectangles and add their areas (or fill in the corner and take it away).', 'The area is {ans} cm².']),
        oracle=lambda e: int(poly_area(LPOLY(e['W'], e['H'], e['t'], e['r']))), fig=_lfig),
    '4b': dict(
        base=dict(W=10, H=7, t=6, r=4),
        tpl=dict(vars=dict(W=[9, 10, 12], H=[7, 8], t=[5, 6, 7], r=[3, 4, 5]),
                 q='Find the perimeter of this figure, in cm. The bottom is {W} cm, the left side is {H} cm, the top is {t} cm and the right side is {r} cm. Type the number.',
                 answer='2*(W+H)', hint='Find the two missing sides first. Then add all the sides, or push the step out.',
                 steps=['Push the step out to make a rectangle {W} cm by {H} cm.', 'The perimeter is {W} + {H} + {W} + {H} = {ans} cm.']),
        oracle=lambda e: poly_perimeter(LPOLY(e['W'], e['H'], e['t'], e['r'])), fig=_lfig),
    '5a': dict(
        base=dict(n=4),
        tpl=dict(vars=dict(n=[3, 5, 6, 7, 8]),
                 q='Look at this staircase with {n} steps. Each small square is 1 cm by 1 cm. What is its area, in cm²? Type the number.',
                 answer='n*(n+1)//2', hint='Count the squares in each column. Then add the columns.',
                 steps=['The columns have {n}, then one fewer each time, down to 1 square.', 'Add the columns to find the number of squares.', 'The area is {ans} cm².']),
        oracle=lambda e: cell_area(stair_cells(e['n'])), fig=_sfig),
    '5b': dict(
        base=dict(n=4),
        tpl=dict(vars=dict(n=[3, 5, 6, 7, 8]),
                 q='Look at this staircase with {n} steps. Each small square is 1 cm by 1 cm. What is its perimeter, in cm? Type the number.',
                 answer='4*n', hint='Walk all the way round the edge and count the sides of the squares. Or push the steps out.',
                 steps=['Push the steps up and out. The staircase has the same perimeter as a {n} by {n} square.', '{n} + {n} + {n} + {n} = {ans} cm.']),
        oracle=lambda e: cell_perimeter(stair_cells(e['n'])), fig=_sfig),
    'I8b6': dict(
        base=dict(s=6),
        tpl=dict(vars=dict(s=[5, 7, 8, 9, 12]), derive=dict(L='s+1', M='s-1'),
                 q='A square has sides of {s} cm. Make it 1 cm longer one way and 1 cm shorter the other way: a {L} cm by {M} cm rectangle. Fill in the boxes.',
                 frame=grp('Square: perimeter {f1} cm      area {f2} cm²      Rectangle: perimeter {f3} cm      area {f4} cm²'), answers=dict(f1='4*s', f2='s*s', f3='4*s', f4='s*s-1'),
                 hint='Perimeter: add all four sides. Area: length × width. Do the square first, then the rectangle.',
                 steps=['The {s} by {s} square: perimeter {s} + {s} + {s} + {s}, area {s} × {s}.', 'The {L} by {M} rectangle: perimeter {L} + {M} + {L} + {M}, area {L} × {M}.', 'The numbers are {ans}.']),
        oracle=lambda e: dict(zip(('f1', 'f2', 'f3', 'f4'), square_to_rect(e['s'])))),
    'T2': dict(
        base=dict(L=12, P=30),
        tpl=dict(vars=dict(L=[10, 12, 14], P=[30, 40, 44]), derive=dict(w='P//2-L'),
                 q='One side of a rectangle is {L} cm. Its perimeter is {P} cm. Find its area, in cm². Type the number.',
                 answer='L*w', hint='Half of the perimeter is two sides that meet, added together. What is left for the other side?',
                 steps=['Half of the perimeter ({P} cm) is two sides that meet added together.', 'Take {L} away to find the other side.', 'The area is {L} × the other side = {ans} cm².']),
        oracle=lambda e: e['L'] * find(lambda w: 2 * (e['L'] + w) == e['P'])),
    'G7': dict(
        base=dict(a=7, b=5),
        tpl=dict(vars=dict(a=[6, 7, 8, 9], b=[4, 5, 6]),
                 q='A rectangle {a} cm by {b} cm has a 1 cm square cut out of each of its 4 corners. Find the new area and the new perimeter. Fill in the boxes.',
                 frame=grp('Area {f1} cm²      Perimeter {f2} cm'), answers=dict(f1='a*b-4', f2='2*(a+b)'),
                 hint='Area: take the squares that were cut out away from the whole rectangle. Perimeter: look at what happens to the edge at one corner.',
                 steps=['Area: {a} × {b}, then take away the 4 cut squares.', 'Perimeter: push the cut corners out and you get the {a} by {b} rectangle back.', 'The answers are {ans}.']),
        oracle=lambda e: dict(f1=cell_area(CORNERS_7x5(e['a'], e['b'])), f2=cell_perimeter(CORNERS_7x5(e['a'], e['b']))),
        fig=lambda env: squares_fig(CORNERS_7x5(env['a'], env['b']), 'The new figure', f'A rectangle {env["a"]} cm by {env["b"]} cm with a 1 cm square cut out of each of its 4 corners, on a grid', cols=env['a'] + 2, rows=env['b'] + 2, c=32)),
    'TH-a': dict(
        base=dict(s=7),
        tpl=dict(vars=dict(s=[5, 6, 8, 9, 11, 12]), derive=dict(A='s*s'),
                 q=EXTRA + 'A square has an area of {A} cm². How long is each side, in cm? Type the number.',
                 answer='s', hint='Which number multiplied by itself makes {A}?', steps=['The area of a square is side × side.', 'Find the number that multiplied by itself makes {A}.', 'Each side is {ans} cm.']),
        oracle=lambda e: find(lambda s: s * s == e['s'] * e['s'])),
}

# ---- inquiry habit (docs/pedagogy/inquiry_skills_explicit.md; levels/habits.json)
ITEMS.insert(max(i for i, x in enumerate(ITEMS) if x['tier'] == 'core') + 1, habit_item('Wonder',
    'A rectangle is 4 cm by 3 cm. Its area is 12 square cm. Write a question of your own that starts with "What if ...?" about changing the rectangle.',
    ['Many questions are good. A good "What if" changes one thing.', 'For example: What if I make it 1 cm longer? What if the perimeter stays the same but the sides change? What is the biggest area I can make?'],
    'Change one side. What happens to the area and the perimeter?'))
