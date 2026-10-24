"""Online practice for Level 4 (Primary 4, ages 9-11) holiday lesson 7: Area Architects II (Area and perimeter).

The questions are the ones printed in the Level 4 holiday workbook, built by p4/workbook_html.js from p4/content/l7.js:
  Start here = l7.js workbook() Q1 to Q6;   Investigation = l7.js gaps.invest (Bigger area, bigger perimeter?);
  Think harder = l7.js qbank.stretch[0:4];   Go further = l7.js qbank.challenge[-3:]  (printed as Q5 to Q7).
Every answer is recomputed by an INDEPENDENT checker (the shoelace formula and a ray-casting cell count for areas, edge counting for perimeters, a search over every way to cut an
L-shape into two rectangles, every whole-number rectangle for an area or a perimeter, every 6-square shape, a cell count for the paths), never a copy of the printed answer; the build stops
if a checker and the printed answer (the l7.js `key`, `gaps.invest.key` and `qbank` answers) differ.  The figures on screen are drawn to scale from the same numbers as the checkers.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from p4lib import *      # noqa: E402,F401

META = dict(level=4, lesson=7, key='p4', title='Area Architects II', workbook_title='AREA ARCHITECTS II', topic='Area and Perimeter',
            strand='Area and perimeter',
            sources=['p4/content/l7.js'],
            intro=['Type numbers, like 32. You may add the unit, like 32 cm or 48 cm². Some questions ask for a number sentence, like 3 x 5 + 2 x 6: use x for times.',
                   'Drawing questions are done on paper (your workbook page or squared paper): do them, then compare with the picture shown after you submit. '
                   'Some questions ask you to explain or to make up your own puzzle: think or write on paper, then compare.'])
S7 = 'Area and perimeter'


def D(**k):
    return dict(strand=S7, **k)


# ---------------------------------------------------------------- independent checkers
LP = l_poly(9, 7, 5, 3)                 # the L-shape of Q1: 9 cm by 7 cm with a 5 cm by 3 cm piece missing from the top right
LCELLS = poly_cells(LP)
BOX = [(0, 0), (9, 0), (9, 7), (0, 7)]
STAIR = stair_poly(11, 2)
RECT82 = [(0, 0), (8, 0), (8, 2), (0, 2)]
OUTER, INNER = [(0, 0), (10, 0), (10, 8), (0, 8)], [(1, 1), (9, 1), (9, 7), (1, 7)]
SQ44 = [(0, 0), (4, 0), (4, 4), (0, 4)]
R24 = rectangles_with_area(24)
R30 = rectangles_with_area(30)
P24 = rectangles_with_perimeter(24)
P20 = rectangles_with_perimeter(20)
SIX = polyominoes(6)
SPLIT = rect_splits(LCELLS)             # [((4, 7), (5, 4)), ((4, 3), (9, 4))]
assert len(SPLIT) == 2


def edge(pts, i):
    (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % len(pts)]
    return abs(x2 - x1) + abs(y2 - y1)


def split_sentence():
    a, b = SPLIT[0]
    s = f'{a[0]}x{a[1]}+{b[0]}x{b[1]}'
    assert eval(s.replace('x', '*')) == poly_area(LP)
    return s


def take_sentence():
    piece = {(x, y) for x in range(9) for y in range(7)} - LCELLS
    assert is_rect(piece)
    pw, ph = dims_of(piece)
    s = f'9x7-{pw}x{ph}'
    assert eval(s.replace('x', '*')) == poly_area(LP)
    return s


def split_accepts():
    out = []
    for a, b in SPLIT:
        out += sum_sentences([a, b], '+', 48)
    full = []
    for s in out:
        full += [s, s + '=48', s + ' = 48 cm²']
    return list(dict.fromkeys(full))


def take_accepts():
    pw, ph = dims_of({(x, y) for x in range(9) for y in range(7)} - LCELLS)
    out = []
    for s in sum_sentences([(9, 7), (pw, ph)], '-', 48):
        out += [s, s + '=48', s + ' = 48 cm²']
    return list(dict.fromkeys(out))


def tile_perimeters():
    return sorted({cells_perimeter(p) for p in SIX})


def fence_best(total, wall):
    """The largest area of a whole-metre pen by trying every length of the side next to the fence."""
    best = 0
    for w in range(1, total):
        l = (total - 2 * w) if wall else (total // 2 - w)
        if l > 0:
            best = max(best, w * l)
    return best


def garden_grass(L, W):
    pr, pc = W // 2 - 1, L // 2 - 1
    return sum(1 for i in range(L) for j in range(W) if i != pc and j != pr)


def cut_cells(a, b, s):
    return {(x, y) for x in range(a) for y in range(b)} - {(x, y) for x0 in (0, a - s) for y0 in (0, b - s) for x in range(x0, x0 + s) for y in range(y0, y0 + s)}


FRAME_W = [(0, 0), (10, 0), (10, 8), (0, 8)]
SQFIG = square_from_pieces_fig(4)


def by(pair):
    return f'{pair[0]} by {pair[1]}'


ITEMS = [
    # ================= Start here (workbook lesson 7, Q1 to Q6)
    D(id='1a1', tier='core', no='1(a)', label='1(a) a', type='number', answer=5, skill='finding missing lengths from opposite sides', svg=l_shape_fig(), check=lambda: edge(LP, 2),
      q='This figure has only square corners. Each small square on the grid is 1 cm by 1 cm. Use the opposite sides to find the missing length marked a.',
      hint='Side a is across, and the bottom side is across too. How much of the bottom is already counted by the top?',
      steps=['The top (4 cm) and side a together reach as far across as the bottom (9 cm).', 'a = 9 cm − 4 cm = 5 cm.'],
      src=['This figure has only square corners. Each small square on the grid is 1 cm by 1 cm.', 'Use the opposite sides to find the two missing lengths.']),
    D(id='1a2', tier='core', no='1(a)', label='1(a) b', type='number', answer=3, skill='finding missing lengths from opposite sides', svg=l_shape_fig(), check=lambda: edge(LP, 1),
      q='Now find the missing length marked b in the same figure.',
      hint='Side b goes down, and the left side goes down too. How much of the left side is already counted by the right side?',
      steps=['The right side (4 cm) and side b together go as far down as the left side (7 cm).', 'b = 7 cm − 4 cm = 3 cm.'],
      src=['Use the opposite sides to find the two missing lengths.']),
    D(id='1b-split', tier='core', no='1(b)', label='1(b) split', type='text', accept=split_accepts(), shown='4 x 7 + 5 x 4 = 48', skill='area by splitting into rectangles', svg=l_shape_fig(),
      check=split_sentence, accept_prefix=False,
      q='Find the area of the figure in TWO ways. First split it into 2 rectangles. Type your number sentence, like 3 x 5 + 2 x 6.',
      hint='Imagine one straight cut that makes two rectangles. Find the length and breadth of each piece.',
      steps=['Cut down along the vertical side b. The left piece is 4 cm by 7 cm and the right piece is 5 cm by 4 cm.', '4 × 7 + 5 × 4 = 28 + 20 = 48 cm².',
             'A cut across works too: the top piece is 4 cm by 3 cm and the bottom piece is 9 cm by 4 cm, and 4 × 3 + 9 × 4 = 12 + 36 = 48 cm².'],
      src=['Find the area in TWO ways.', 'Split it into 2 rectangles:']),
    D(id='1b-take', tier='core', no='1(b)', label='1(b) take', type='text', accept=take_accepts(), shown='9 x 7 - 5 x 3 = 48', skill='area by taking away the missing piece', svg=l_shape_fig(),
      check=take_sentence, accept_prefix=False,
      q='Now find the area the other way: the big rectangle take away the missing piece. Type your number sentence, like 8 x 5 - 2 x 3.',
      hint='Put the shape inside one big rectangle. Which piece of the big rectangle is not part of the figure?',
      steps=['The big rectangle is 9 cm by 7 cm. The missing piece is 5 cm by 3 cm.', '9 × 7 − 5 × 3 = 63 − 15 = 48 cm².', 'Both ways give 48 cm², so we can trust it.'],
      src=['Find the area in TWO ways.', 'Big rectangle take away the missing piece:']),
    D(id='1c', tier='core', no='1(c)', label='1(c)', type='number', answer=32, skill='perimeter of a composite figure', svg=l_shape_fig(), check=lambda: poly_perimeter(LP),
      q='Find the perimeter of the figure.',
      hint='Add all six sides, including a and b. Or slide the two step sides out: what shape is the outline then?',
      steps=['The sides are 4, b, a, 4, 9 and 7 cm: 4 + 3 + 5 + 4 + 9 + 7 = 32 cm.', 'Check: slide the step sides to the edges and the outline is a 9 cm by 7 cm rectangle, and 9 + 7 + 9 + 7 = 32 cm.'],
      src=['Find the perimeter.']),

    D(id='2len', tier='core', no='2', label='2 lengths', type='set', answer=[x[0] for x in R24], ordered=False, skill='listing the rectangles for an area',
      check=lambda: [a for a in range(1, 25) if 24 % a == 0 and a <= 24 // a],
      q='Rectangles with whole-cm sides have an area of 24 cm². Find them all. Start with a length of 1 cm and go up. Turning a rectangle round does not make a new one. Type the length of each rectangle you find.',
      hint='Which whole numbers multiply with the length to make 24? Try length 1, then 2, then 3, and so on. When do you start to meet rectangles you already have?',
      steps=['Try each length and see if it makes 24: 1 × 24, 2 × 12, 3 × 8, 4 × 6.', 'The next one is 6 × 4, the 4 by 6 rectangle turned round, so we stop. The lengths are 1, 2, 3 and 4.'],
      src=['Rectangles with whole-cm sides have an area of 24 cm². Find them all. Start with a length of 1 cm.']),
    D(id='2bre', tier='core', no='2', label='2 breadths', type='set', answer=[x[1] for x in R24], ordered=True, skill='listing the rectangles for an area',
      check=lambda: [24 // a for a in range(1, 25) if 24 % a == 0 and a <= 24 // a],
      q='Write the breadth of each rectangle you found, in the same order as the lengths (smallest length first). Type the numbers with commas.',
      hint='For each length, how many cm of breadth do you need to make an area of 24 cm²?',
      steps=['Length 1 needs breadth 24 (1 × 24 = 24). Length 2 needs 12. Length 3 needs 8. Length 4 needs 6.', 'The breadths are 24, 12, 8 and 6.'],
      src=['Rectangles with whole-cm sides have an area of 24 cm². Find them all.']),
    D(id='2per', tier='core', no='2', label='2 perimeters', type='set', answer=[2 * (a + b) for a, b in R24], ordered=True, skill='perimeter of a rectangle',
      check=lambda: [(a + b) * 2 for a, b in rectangles_with_area(24)],
      q='Write the perimeter of each rectangle, in the same order (smallest length first). Type the numbers with commas.',
      hint='The perimeter is the way round: length + breadth + length + breadth.',
      steps=['1 by 24: 1 + 24 + 1 + 24 = 50 cm. 2 by 12: 28 cm. 3 by 8: 22 cm. 4 by 6: 20 cm.', 'The perimeters are 50, 28, 22 and 20.'],
      src=['Rectangles with whole-cm sides have an area of 24 cm². Find them all.']),
    D(id='2a-large', tier='core', no='2(a)', label='2(a) most', type='text', accept_by=True, accept=x_forms(*max(R24, key=lambda r: 2 * (r[0] + r[1]))), shown='1 by 24', skill='comparing perimeters',
      check=lambda: by(max(rectangles_with_area(24), key=lambda r: 2 * (r[0] + r[1]))),
      q='Which of your rectangles has the LARGEST perimeter? Type it as length by breadth, like 5 by 7.',
      hint='Compare the perimeters you found. Is the largest one long and thin, or close to a square?',
      steps=['The perimeters are 50, 28, 22 and 20 cm.', 'The largest is 50 cm, for the 1 cm by 24 cm rectangle.'],
      src=['Largest perimeter:']),
    D(id='2a-small', tier='core', no='2(a)', label='2(a) least', type='text', accept_by=True, accept=x_forms(*min(R24, key=lambda r: 2 * (r[0] + r[1]))), shown='4 by 6', skill='comparing perimeters',
      check=lambda: by(min(rectangles_with_area(24), key=lambda r: 2 * (r[0] + r[1]))),
      q='Which of your rectangles has the SMALLEST perimeter? Type it as length by breadth, like 5 by 7.',
      hint='Compare the perimeters you found. Which rectangle is the closest to a square?',
      steps=['The perimeters are 50, 28, 22 and 20 cm.', 'The smallest is 20 cm, for the 4 cm by 6 cm rectangle.'],
      src=['Smallest perimeter:']),

    D(id='3a', tier='core', no='3(a)', label='3(a)', type='number', answer=6, skill='area of a shape made of tiles', svg=tiles_fig(6), check=lambda: len(next(iter(SIX))) * 1,
      q='Mei joins 6 square tiles, each 1 cm by 1 cm, edge to edge (whole sides touching). What is the area of any shape she makes?',
      hint='Each tile covers 1 cm². How many tiles does she use?',
      steps=['Each tile has an area of 1 cm².', 'All 6 tiles are used, so the area is 6 cm² for every shape she makes.'],
      src=['Mei joins 6 square tiles, each 1 cm by 1 cm, edge to edge (whole sides touching).', 'What is the area of any shape she makes?']),
    D(id='3b-draw', tier='core', no='3(b)', label='3(b) draw', type='selfcheck', paper=True, skill='shapes with the smallest and largest perimeter', svg=tiles_fig(6),
      check=lambda: (min(tile_perimeters()), max(tile_perimeters())), sol_fig=lambda f: tile_shapes_fig(),
      q='Mei joins her 6 tiles edge to edge. Draw the shape with the SMALLEST perimeter and one with the LARGEST perimeter on 1 cm squared paper.',
      hint='For the smallest, keep the tiles close together. For the largest, try long thin shapes. Count the edges round the outside.',
      steps=['The smallest perimeter is 10 cm: a block of 2 rows of 3 tiles.', 'The largest perimeter is 14 cm: for example a row of 6 tiles, or any shape with no 2 by 2 block of tiles in it.',
             'Other shapes give 12 cm. Your drawing is good if its perimeter is 10 cm or 14 cm.'],
      src=['Mei joins 6 square tiles, each 1 cm by 1 cm, edge to edge (whole sides touching).', 'Draw the shape with the SMALLEST perimeter and one with the LARGEST']),
    D(id='3b-small', tier='core', no='3(b)', label='3(b) least', type='number', answer=10, skill='shapes with the smallest and largest perimeter', svg=tiles_fig(6), check=lambda: min(tile_perimeters()),
      q='Mei joins her 6 tiles edge to edge in every way she can. What is the SMALLEST perimeter a shape of 6 tiles can have?',
      hint='Count the unit edges round the outside. A shape with its tiles close together has fewer edges showing.',
      steps=['A block of 2 rows of 3 tiles has a perimeter of 2 + 3 + 2 + 3 = 10 cm.', 'No shape made of 6 tiles can have a perimeter below 10 cm (we checked every shape).'],
      src=['Mei joins 6 square tiles, each 1 cm by 1 cm, edge to edge (whole sides touching).', 'Draw the shape with the SMALLEST perimeter and one with the LARGEST']),
    D(id='3b-large', tier='core', no='3(b)', label='3(b) most', type='number', answer=14, skill='shapes with the smallest and largest perimeter', svg=tiles_fig(6), check=lambda: max(tile_perimeters()),
      q='What is the LARGEST perimeter a shape of 6 tiles joined edge to edge can have?',
      hint='Count the unit edges round the outside. Which shapes have the most edges showing?',
      steps=['A row of 6 tiles has a perimeter of 6 + 1 + 6 + 1 = 14 cm.', 'No shape made of 6 tiles can have a perimeter above 14 cm (we checked every shape).'],
      src=['Mei joins 6 square tiles, each 1 cm by 1 cm, edge to edge (whole sides touching).', 'Draw the shape with the SMALLEST perimeter and one with the LARGEST']),

    D(id='4a-box', tier='core', no='4(a)', label='4(a) box', type='fields', frame='It fits in a rectangle {f1} cm wide and {f2} cm high.', answer=[11, 6], skill='perimeter by pushing the steps out', svg=stair_fig(),
      check=lambda: (max(p[0] for p in STAIR), max(p[1] for p in STAIR)),
      q='Ravi says, "I cannot find the perimeter of this staircase, because the steps are not labelled." Show Ravi how to find it WITHOUT measuring each step. Push the steps out: the shape then fits in a rectangle. How wide and how high is that rectangle?',
      hint='Push every step out to the edge. How wide is the widest row, and how high is the whole staircase?',
      steps=['Push the steps out to the longest row and the full height.', 'The staircase fits in a rectangle 11 cm wide and 6 cm high.'],
      src=['Ravi says, "I cannot find the perimeter of this staircase, because the steps are not labelled."', 'Push the steps out: the shape then fits in a ___ cm by ___ cm rectangle.']),
    D(id='4a-per', tier='core', no='4(a)', label='4(a) perim', type='number', answer=34, skill='perimeter by pushing the steps out', svg=stair_fig(), check=lambda: poly_perimeter(STAIR),
      q='Now find the perimeter of the staircase.',
      hint='All the steps go the same way, so the outline is just as long as the rectangle round it.',
      steps=['Pushing the steps out does not change the length of the outline.', 'The perimeter is the same as the 11 cm by 6 cm rectangle: 11 + 6 + 11 + 6 = 34 cm.'],
      src=['Push the steps out: the shape then fits in a ___ cm by ___ cm rectangle.', 'Perimeter:']),
    D(id='4b', tier='core', no='4(b)', label='4(b)', type='number', answer=42, skill='area of a staircase', svg=stair_fig(), check=lambda: poly_area(STAIR),
      q='Think of the staircase as 3 rows. The rows are 3 cm, 7 cm and 11 cm long, and each row is 2 cm high. What is the area?',
      hint='Find the area of each row, then add the three areas.',
      steps=['The rows have areas 3 × 2 = 6 cm², 7 × 2 = 14 cm² and 11 × 2 = 22 cm².', '6 + 14 + 22 = 42 cm².'],
      src=['Think of the staircase as 3 rows. The rows are 3 cm, 7 cm and 11 cm long, and each row is 2 cm high.']),

    D(id='5a', tier='core', no='5(a)', label='5(a) draw', type='selfcheck', paper=True, skill='cutting and rearranging', svg=cut_rect_fig(), check=lambda: next(s for s in range(1, 20) if s * s == 8 * 2),
      sol_fig=lambda f: square_from_pieces_fig(f),
      q='An 8 cm by 2 cm rectangle is cut along the dashed line. The two pieces are put together to make a square. Draw the square on paper.',
      hint='Each piece is the same size. Try putting one piece on top of the other.',
      steps=['Each piece is 4 cm by 2 cm. Stack one on top of the other to make a square.', 'The square is 4 cm by 4 cm. Your drawing is good if every side is 4 cm.'],
      src=['An 8 cm by 2 cm rectangle is cut along the dashed line. The two pieces are put together to make a square.', 'Draw the square on the grid.']),
    D(id='5b-area', tier='core', no='5(b)', label='5(b) area', type='fields', frame='rectangle {f1} cm²   square {f2} cm²', answer=[16, 16], skill='area stays the same', svg=cut_rect_fig(),
      check=lambda: (poly_area(RECT82), next(s for s in range(1, 20) if s * s == poly_area(RECT82)) ** 2),
      q='The rectangle is cut and the two pieces make a square. Find the area of the rectangle and the area of the square.',
      hint='The pieces are only moved. Is any of the paper added or taken away?',
      steps=['The rectangle is 8 cm by 2 cm: 8 × 2 = 16 cm².', 'The square is made from the same two pieces, so its area is also 16 cm² (4 × 4 = 16).'],
      src=['Area: rectangle ____ cm², square ____ cm².']),
    D(id='5b-per', tier='core', no='5(b)', label='5(b) perim', type='fields', frame='rectangle {f1} cm   square {f2} cm', answer=[20, 16], skill='perimeter changes', svg=cut_rect_fig(),
      check=lambda: (poly_perimeter(RECT82), poly_perimeter(SQ44)),
      q='Find the perimeter of the rectangle and the perimeter of the square it makes.',
      hint='Find the side of the square first. Then add the four sides of each shape.',
      steps=['The rectangle: 8 + 2 + 8 + 2 = 20 cm.', 'The square has sides of 4 cm: 4 + 4 + 4 + 4 = 16 cm.'],
      src=['Perimeter: rectangle ____ cm, square ____ cm.']),
    D(id='5c', tier='core', no='5(c)', label='5(c)', type='choice', options=['Yes', 'No'], answer='No', skill='area and perimeter are different',
      check=lambda: 'Yes' if poly_perimeter(RECT82) == poly_perimeter(SQ44) else 'No',
      q='Ali says, "The area stayed the same, so the perimeter stayed the same too." Is he right?',
      hint='Compare the perimeter of the rectangle with the perimeter of the square.',
      steps=['The area stayed the same, 16 cm².', 'The perimeter changed from 20 cm to 16 cm, so Ali is not right.'],
      src=['Ali says, "The area stayed the same, so the perimeter stayed the same too." Is he right? Explain.']),
    D(id='5c-why', tier='core', no='5(c)', label='5(c) explain', type='selfcheck', open=True, marking_mode='self', skill='area and perimeter are different',
      q='Explain what you notice about the area and the perimeter before and after the cut.',
      hint='What did you add or take away when you cut and moved the pieces? Which measure counts the edge?',
      steps=['The area stayed the same because nothing was added or taken away: the same paper covers the same space.', 'The perimeter changed because moving the pieces hid some edges and uncovered others.',
             'Any answer that says the area stays the same but the perimeter can change is good.'],
      src=['Is he right? Explain.']),

    D(id='6a-long', tier='core', no='6(a)', label='6(a) long', type='number', answer=10, skill='border problems', svg=frame_fig(), check=lambda: max(p[0] for p in FRAME_W),
      q='A photo 8 cm long and 6 cm wide is put in a frame. The frame is 1 cm wide all round. How long is the whole thing (photo and frame)?',
      hint='The frame is on both ends of the photo. How much does it add to the length?',
      steps=['The frame adds 1 cm at each end of the photo.', '8 + 1 + 1 = 10 cm long.'],
      src=['A photo 8 cm long and 6 cm wide is put in a frame. The frame is 1 cm wide all round.', 'How long and how wide is the whole thing (photo and frame)?']),
    D(id='6a-wide', tier='core', no='6(a)', label='6(a) wide', type='number', answer=8, skill='border problems', svg=frame_fig(), check=lambda: max(p[1] for p in FRAME_W),
      q='How wide is the whole thing (photo and frame)?',
      hint='The frame is on both sides of the photo. How much does it add to the width?',
      steps=['The frame adds 1 cm on each side of the photo.', '6 + 1 + 1 = 8 cm wide.'],
      src=['How long and how wide is the whole thing (photo and frame)?']),
    D(id='6b', tier='core', no='6(b)', label='6(b)', type='number', answer=32, skill='border problems', svg=frame_fig(), check=lambda: len(poly_cells(OUTER)) - len(poly_cells(INNER)),
      q='Find the area of the frame only (the yellow strip, not the photo).',
      hint='Find the area of the whole thing first. Which part of it is the photo?',
      steps=['The whole thing is 10 cm by 8 cm: 10 × 8 = 80 cm².', 'The photo is 8 cm by 6 cm: 8 × 6 = 48 cm².', 'The frame is 80 − 48 = 32 cm².'],
      src=['Find the area of the frame only.']),
    D(id='6c', tier='core', no='6(c)', label='6(c)', type='selfcheck', skill='border problems', svg=frame_fig(), check=lambda: (len(poly_cells(OUTER)) - len(poly_cells(INNER))) - (8 + 8 + 6 + 6),
      q='Mei found the area of the frame like this: 8 + 8 + 6 + 6 = 28 cm². What did she forget?',
      hint='Mei added up four strips, one along each side of the photo. Look at the corners of the frame.',
      steps=['Her four strips (8 + 8 + 6 + 6 = 28 cm²) leave out the 4 corner squares of the frame.', '28 + 4 = 32 cm², the area you found in 6(b).'],
      src=['Mei found the frame like this: 8 + 8 + 6 + 6 = 28 cm². What did she forget?']),

    # ================= Investigation: Bigger area, bigger perimeter?
    D(id='Ieasy', tier='invest', no='Investigation (easy step)', label='Inv easy', type='fields', frame='area {f1} cm²   perimeter {f2} cm', answer=[16, 16], skill='area and perimeter of a square',
      svg=plain_rect_fig(4, 4), check=lambda: (poly_area(SQ44), poly_perimeter(SQ44)),
      q='Look at this 4 cm by 4 cm square. Write its area and its perimeter.',
      hint='Area is the number of 1 cm squares inside. Perimeter is the way round.',
      steps=['The area is 4 × 4 = 16 cm².', 'The perimeter is 4 + 4 + 4 + 4 = 16 cm.'],
      src=['Draw a 4 cm by 4 cm square on the Square grid. Write its area and its perimeter.']),
    D(id='Ia', tier='invest', no='Investigation (a)', label='Inv (a)', type='fields', frame='area {f1} cm²   perimeter {f2} cm', answer=[11, 24], skill='area and perimeter of a rectangle',
      svg=plain_rect_fig(11, 1), check=lambda: (1 * 11, 2 * (1 + 11)),
      q='Ali says: "A rectangle with a bigger area always has a bigger perimeter." Test his idea. First find the area and the perimeter of a 1 cm by 11 cm rectangle.',
      hint='Area is length times breadth. Perimeter is length + breadth + length + breadth.',
      steps=['The area is 1 × 11 = 11 cm².', 'The perimeter is 1 + 11 + 1 + 11 = 24 cm.'],
      src=['Test Ali\'s idea. Find the area and perimeter of a 1 cm by 11 cm rectangle, and of a 4 cm by 4 cm square.', 'Ali says: "A rectangle with a bigger area always has a bigger perimeter."']),
    D(id='Ia-area', tier='invest', no='Investigation (a)', label='Inv (a) A', type='choice', options=['the 1 cm by 11 cm rectangle', 'the 4 cm by 4 cm square'], answer='the 4 cm by 4 cm square', skill='comparing area',
      check=lambda: 'the 4 cm by 4 cm square' if poly_area(SQ44) > 11 else 'the 1 cm by 11 cm rectangle',
      q='Which has the bigger area, the 1 cm by 11 cm rectangle or the 4 cm by 4 cm square?',
      hint='Compare the two areas you found.',
      steps=['The rectangle has an area of 11 cm². The square has an area of 16 cm².', 'The square has the bigger area.'],
      src=['Which has the bigger area? Which has the bigger perimeter?']),
    D(id='Ia-per', tier='invest', no='Investigation (a)', label='Inv (a) P', type='choice', options=['the 1 cm by 11 cm rectangle', 'the 4 cm by 4 cm square'], answer='the 1 cm by 11 cm rectangle', skill='comparing perimeter',
      check=lambda: 'the 1 cm by 11 cm rectangle' if 2 * (1 + 11) > poly_perimeter(SQ44) else 'the 4 cm by 4 cm square',
      q='Which has the bigger perimeter, the 1 cm by 11 cm rectangle or the 4 cm by 4 cm square?',
      hint='Compare the two perimeters you found.',
      steps=['The rectangle has a perimeter of 24 cm. The square has a perimeter of 16 cm.', 'The rectangle has the bigger perimeter.'],
      src=['Which has the bigger area? Which has the bigger perimeter?']),
    D(id='Ib', tier='invest', no='Investigation (b)', label='Inv (b)', type='set', answer=sorted(a * b for a, b in P24), ordered=False, skill='systematic listing of rectangles', svg=None,
      check=lambda: sorted(a * b for a, b in rectangles_with_perimeter(24)),
      q='List ALL the rectangles with whole-cm sides and a perimeter of 24 cm. Type the area of each one, with commas.',
      hint='The length and breadth add up to half of 24. List the pairs in order, starting with 1 cm, and find each area.',
      steps=['Half of 24 is 12, so the length and breadth add up to 12.', 'The pairs are 1 and 11, 2 and 10, 3 and 9, 4 and 8, 5 and 7, 6 and 6.',
             'Their areas are 11, 20, 27, 32, 35 and 36 cm². That is 6 rectangles.'],
      src=['List ALL the rectangles with whole-cm sides and a perimeter of 24 cm. Write the area of each.']),
    D(id='Ic', tier='invest', no='Investigation (c)', label='Inv (c)', type='choice', options=['Yes', 'No'], answer='No', skill='testing a claim',
      check=lambda: 'No' if (poly_area(SQ44) > 11 and poly_perimeter(SQ44) < 24) else 'Yes',
      q='Is Ali right that a rectangle with a bigger area always has a bigger perimeter?',
      hint='Look at the 1 cm by 11 cm rectangle and the 4 cm by 4 cm square. Does the bigger area have the bigger perimeter?',
      steps=['The square has the bigger area (16 cm² and 11 cm²) but the smaller perimeter (16 cm and 24 cm).', 'One example that does not fit is enough, so Ali is not right.'],
      src=['Is Ali right?']),
    D(id='Ic-big', tier='invest', no='Investigation (c)', label='Inv (c) big', type='text', accept_by=True, accept=x_forms(*max(P24, key=lambda r: r[0] * r[1])), shown='6 by 6', skill='systematic listing of rectangles',
      check=lambda: by(max(rectangles_with_perimeter(24), key=lambda r: r[0] * r[1])),
      q='Of all the rectangles with a perimeter of 24 cm, which one has the biggest area? Type it as length by breadth, like 5 by 7.',
      hint='Look at the areas in your list. Which is the biggest?',
      steps=['The areas are 11, 20, 27, 32, 35 and 36 cm².', 'The biggest is 36 cm², for the 6 cm by 6 cm rectangle.'],
      src=['Which of your rectangles has the biggest area?']),
    D(id='Ic-shape', tier='invest', no='Investigation (c)', label='Inv (c) form', type='selfcheck', skill='systematic listing of rectangles', check=lambda: 'square' if max(P24, key=lambda r: r[0] * r[1])[0] == max(P24, key=lambda r: r[0] * r[1])[1] else 'not a square',
      q='What is special about the shape of the rectangle with the biggest area?',
      hint='Look at its length and its breadth.',
      steps=['Its length and its breadth are the same, 6 cm, so it is a square.', 'For the same perimeter, the closer a rectangle is to a square, the bigger its area.'],
      src=['What is special about its shape?']),

    # ================= Think harder (qbank.stretch[0:4])
    D(id='T1-list', tier='stretch', no='Think harder 1', label='T1', type='set', answer=[x[0] for x in R30], ordered=False, skill='listing the rectangles for an area',
      check=lambda: [a for a in range(1, 31) if 30 % a == 0 and a <= 30 // a],
      q='List every rectangle with whole-cm sides and an area of 30 cm². Type the shorter side of each one, with commas.',
      hint='Which whole numbers multiply with the shorter side to make 30? Try 1, then 2, and so on, and stop when you meet a rectangle turned round.',
      steps=['Try each whole number that divides 30: 1 × 30, 2 × 15, 3 × 10, 5 × 6.', 'The next is 6 × 5, the 5 by 6 rectangle turned round. The shorter sides are 1, 2, 3 and 5.'],
      src=['List every rectangle with whole-cm sides and an area of 30 cm².']),
    D(id='T1-small', tier='stretch', no='Think harder 1', label='T1 least', type='text', accept_by=True, accept=x_forms(*min(R30, key=lambda r: 2 * (r[0] + r[1]))), shown='5 by 6', skill='comparing perimeters',
      check=lambda: by(min(rectangles_with_area(30), key=lambda r: 2 * (r[0] + r[1]))),
      q='Which rectangle with whole-cm sides and an area of 30 cm² has the smallest perimeter? Type it as shorter side by longer side, like 2 by 9.',
      hint='Find the perimeter of each rectangle with an area of 30 cm². Which is the closest to a square?',
      steps=['The perimeters are 62 cm (1 by 30), 34 cm (2 by 15), 26 cm (3 by 10) and 22 cm (5 by 6).', 'The smallest is 22 cm, for the 5 cm by 6 cm rectangle.'],
      src=['Which one has the smallest perimeter?']),
    D(id='T2-area', tier='stretch', no='Think harder 2', label='T2', type='set', answer=sorted(a * b for a, b in P20), ordered=False, skill='systematic listing of rectangles',
      check=lambda: sorted(a * b for a, b in rectangles_with_perimeter(20)),
      q='A rectangle has whole-cm sides and a perimeter of 20 cm. List all the possible rectangles. Type the area of each one, with commas.',
      hint='The length and breadth add up to half of 20. List the pairs in order, starting with 1 cm, and find each area.',
      steps=['Half of 20 is 10, so the length and breadth add up to 10.', 'The pairs are 1 and 9, 2 and 8, 3 and 7, 4 and 6, 5 and 5.', 'Their areas are 9, 16, 21, 24 and 25 cm².'],
      src=['A rectangle has whole-cm sides and a perimeter of 20 cm. List all the possible rectangles and their areas.']),
    D(id='T2-big', tier='stretch', no='Think harder 2', label='T2 big', type='text', accept_by=True, accept=x_forms(*max(P20, key=lambda r: r[0] * r[1])), shown='5 by 5', skill='systematic listing of rectangles',
      check=lambda: by(max(rectangles_with_perimeter(20), key=lambda r: r[0] * r[1])),
      q='Which of these rectangles has the largest area? Type it as length by breadth, like 2 by 7.',
      hint='Compare all the areas in your list.',
      steps=['The areas are 9, 16, 21, 24 and 25 cm².', 'The largest is 25 cm², for the 5 cm by 5 cm rectangle.'],
      src=['Which has the largest area?']),
    D(id='T3a', tier='stretch', no='Think harder 3', label='T3 area', type='number', answer=60, skill='cutting corners', svg=cut_corners_fig(),
      check=lambda: len(cut_cells(12, 8, 3)),
      q='A 3 cm by 3 cm square is cut from each of the four corners of a 12 cm by 8 cm rectangle. Find the area of the shape that is left.',
      hint='Find the area of the whole rectangle. Then take away the four corner squares.',
      steps=['The rectangle has an area of 12 × 8 = 96 cm².', 'The four corner squares have an area of 4 × 3 × 3 = 36 cm².', '96 − 36 = 60 cm².'],
      src=['A 3 cm by 3 cm square is cut from each of the four corners of a 12 cm by 8 cm rectangle.', 'Find the area and the perimeter of the shape that is left.']),
    D(id='T3p', tier='stretch', no='Think harder 3', label='T3 perim', type='number', answer=40, skill='cutting corners', svg=cut_corners_fig(),
      check=lambda: cells_perimeter(cut_cells(12, 8, 3)),
      q='Now find the perimeter of the shape that is left after the four corner squares are cut off.',
      hint='Walk round the new outline. What happens to the length of the edge at each corner when you cut it off?',
      steps=['Each cut takes away 3 cm along one side and 3 cm along the other, and adds 3 cm and 3 cm round the notch.', 'So the perimeter does not change: 12 + 8 + 12 + 8 = 40 cm.'],
      src=['Find the area and the perimeter of the shape that is left.']),
    D(id='T4a', tier='stretch', no='Think harder 4', label='T4 area', type='number', answer=29, skill='composite figures', svg=squares_row_fig(), check=lambda: poly_area(squares_row_poly((2, 3, 4))),
      q='Three squares with sides 2 cm, 3 cm and 4 cm stand side by side in a row on the same line, smallest on the left. Find the area of the figure.',
      hint='The figure is made of the three squares. Find the area of each.',
      steps=['The squares have areas 2 × 2 = 4 cm², 3 × 3 = 9 cm² and 4 × 4 = 16 cm².', '4 + 9 + 16 = 29 cm².'],
      src=['Three squares with sides 2 cm, 3 cm and 4 cm stand side by side in a row on the same line, smallest on the left.', 'Find the area and the perimeter of the figure.']),
    D(id='T4p', tier='stretch', no='Think harder 4', label='T4 perim', type='number', answer=26, skill='composite figures', svg=squares_row_fig(), check=lambda: poly_perimeter(squares_row_poly((2, 3, 4))),
      q='Now find the perimeter of the figure made by the three squares.',
      hint='The steps all go the same way. What shape is the outline when you push them out?',
      steps=['Push the steps out. The figure fits in a rectangle 9 cm long (2 + 3 + 4) and 4 cm high.', 'The perimeter is 9 + 4 + 9 + 4 = 26 cm.'],
      src=['Find the area and the perimeter of the figure.']),

    # ================= Go further (qbank.challenge[-3:], printed Q5 to Q7)
    D(id='G5', tier='challenge', no='Go further 5', label='G5', type='selfcheck', open=True, marking_mode='open', skill='making up a fencing puzzle',
      check=lambda: (fence_best(30, False), fence_best(30, True)),
      q='Make up your own fencing puzzle like Ravi\'s: choose a length of fence (a whole number of metres, more than 20) and say whether one side is a wall. Find the largest area the pen can have, and prove it by listing every whole-metre pen.',
      hint='List the pens in order: the side next to the fence is 1 m, then 2 m, then 3 m, and so on. Find the area of each.',
      steps=['Puzzles will vary: check that every whole-metre pen is listed.',
             'Model: 30 m of fence, no wall. The sides add up to 15 m, and 7 m by 8 m gives the largest area, 56 m².',
             'With a wall on one side and 30 m of fence: 7 m, 16 m, 7 m gives 112 m², and so does 8 m, 14 m, 8 m. Show your puzzle to your tutor or a grown-up and check each other\'s lists.'],
      src=['Make up your own fencing puzzle like Ravi', 'choose a length of fence (a whole number of metres, more than 20) and say whether one side is a wall']),
    D(id='G6', tier='challenge', no='Go further 6', label='G6', type='number', answer=63, skill='area of grass between paths', svg=garden_fig(), check=lambda: garden_grass(10, 8),
      q='A garden is 10 m long and 8 m wide. Two paths 1 m wide cross it: one goes along its length and one goes across its width. What area of the garden is NOT path?',
      hint='Imagine sliding the paths to the edges of the garden. What shape is the grass then?',
      steps=['Slide the paths to the edges. The grass makes a rectangle 9 m by 7 m.', '9 × 7 = 63 m².', 'Check: 80 − 10 − 8 + 1 = 63, because the square where the paths cross was counted twice.'],
      src=['A garden is 10 m long and 8 m wide. Two paths 1 m wide cross it: one goes along its length and one goes across its width.']),
    D(id='G7-side', tier='challenge', no='Go further 7', label='G7', type='number', answer=6, skill='cutting and rearranging', svg=plain_rect_fig(9, 4), check=lambda: next(s for s in range(1, 50) if s * s == 9 * 4),
      q='A rectangle 9 cm long and 4 cm wide is cut into 2 pieces. The pieces fit together exactly to make a square. How long is a side of the square?',
      hint='The pieces are only moved, so the area stays the same. Which number times itself gives that area?',
      steps=['The area of the rectangle is 9 × 4 = 36 cm².', 'The square has the same area, and 6 × 6 = 36, so a side is 6 cm.'],
      src=['A rectangle 9 cm long and 4 cm wide is cut into 2 pieces. The pieces fit together exactly to make a square. How long is a side of the square?']),
    D(id='G7-per', tier='challenge', no='Go further 7', label='G7 perim', type='choice', options=['up', 'down', 'the same'], answer='down', skill='perimeter changes',
      check=lambda: (lambda a, b: 'up' if b > a else 'down' if b < a else 'the same')(2 * (9 + 4), 4 * next(s for s in range(1, 50) if s * s == 36)),
      q='The 9 cm by 4 cm rectangle is cut and made into a square. Did the perimeter go up, go down, or stay the same?',
      hint='Find the perimeter of the rectangle and the perimeter of the square.',
      steps=['The rectangle has a perimeter of 9 + 4 + 9 + 4 = 26 cm.', 'The square has a perimeter of 4 × 6 = 24 cm.', 'The perimeter went down from 26 cm to 24 cm.'],
      src=['Did the perimeter go up or down?']),
]

finish(ITEMS)

# ---------------------------------------------------------------- variants (every combination is run against an oracle that does not use the template's formula)
VARIANTS = {
    '1c': dict(
        base=dict(W=9, H=7),
        tpl=dict(vars=dict(W=[8, 9, 10, 11], H=[6, 7, 8]),
                 q='This figure has only square corners. Each small square on the grid is 1 cm by 1 cm. Find its perimeter.', answer='2*(W+H)',
                 hint='Add all six sides, including a and b. Or slide the two step sides out: what shape is the outline then?',
                 steps=['Slide the two step sides to the edges: the outline is a {W} cm by {H} cm rectangle.', 'The perimeter is {W} + {H} + {W} + {H} = {ans} cm.']),
        fig=lambda e: l_shape_fig(e['W'], e['H'], e['W'] - 4, e['H'] - 4),
        oracle=lambda e: poly_perimeter(l_poly(e['W'], e['H'], e['W'] - 4, e['H'] - 4))),
    '4a-per': dict(
        base=dict(w=11, r=2),
        tpl=dict(vars=dict(w=[9, 11, 13], r=[2, 3]),
                 q='This staircase has three steps. Find its perimeter.', answer='2*(w+3*r)',
                 hint='All the steps go the same way, so the outline is just as long as the rectangle round it.',
                 steps=['Push the steps out: the staircase fits in a rectangle {w} cm wide and {h} cm high.', 'The perimeter is {w} + {h} + {w} + {h} = {ans} cm.'],
                 derive=dict(h='3*r')),
        fig=lambda e: stair_fig(e['w'], e['r']),
        oracle=lambda e: poly_perimeter(stair_poly(e['w'], e['r']))),
    '6b': dict(
        base=dict(L=8, W=6, w=1),
        tpl=dict(vars=dict(L=[8, 10, 12], W=[5, 6, 7], w=[1, 2]),
                 q='A photo {L} cm long and {W} cm wide is put in a frame. The frame is {w} cm wide all round. Find the area of the frame only (not the photo).', answer='(L+2*w)*(W+2*w)-L*W',
                 hint='Find the area of the whole thing first. Which part of it is the photo?',
                 steps=['The whole thing is ({L} + {w} + {w}) cm long and ({W} + {w} + {w}) cm wide.', 'Take away the area of the photo, {L} × {W} cm². The frame is {ans} cm².'],
                 ),
        fig=lambda e: frame_fig(e['L'], e['W'], e['w']),
        oracle=lambda e: len(poly_cells([(0, 0), (e['L'] + 2 * e['w'], 0), (e['L'] + 2 * e['w'], e['W'] + 2 * e['w']), (0, e['W'] + 2 * e['w'])])) - len(poly_cells([(e['w'], e['w']), (e['L'] + e['w'], e['w']), (e['L'] + e['w'], e['W'] + e['w']), (e['w'], e['W'] + e['w'])]))),
    'T3a': dict(
        base=dict(a=12, b=8, s=3),
        tpl=dict(vars=dict(a=[10, 12, 14], b=[8, 9, 10], s=[1, 2, 3]),
                 q='A {s} cm by {s} cm square is cut from each of the four corners of a {a} cm by {b} cm rectangle. Find the area of the shape that is left.', answer='a*b-4*s*s',
                 hint='Find the area of the whole rectangle. Then take away the four corner squares.',
                 steps=['The rectangle has an area of {a} × {b} cm².', 'The four corner squares take away 4 × {s} × {s} cm². The area left is {ans} cm².']),
        fig=lambda e: cut_corners_fig(e['a'], e['b'], e['s']),
        oracle=lambda e: len(cut_cells(e['a'], e['b'], e['s']))),
    'T3p': dict(
        base=dict(a=12, b=8, s=3),
        tpl=dict(vars=dict(a=[10, 12, 14], b=[8, 9, 10], s=[1, 2, 3]),
                 q='A {s} cm by {s} cm square is cut from each of the four corners of a {a} cm by {b} cm rectangle. Find the perimeter of the shape that is left.', answer='2*(a+b)',
                 hint='Walk round the new outline. What happens to the length of the edge at each corner when you cut it off?',
                 steps=['Each cut takes away {s} cm along one side and {s} cm along the other, and adds {s} cm and {s} cm round the notch.', 'So the perimeter does not change: {a} + {b} + {a} + {b} = {ans} cm.']),
        fig=lambda e: cut_corners_fig(e['a'], e['b'], e['s']),
        oracle=lambda e: cells_perimeter(cut_cells(e['a'], e['b'], e['s']))),
    'T4a': dict(
        base=dict(a=2, b=3, c=4),
        tpl=dict(vars=dict(a=[1, 2], b=[3, 4], c=[5, 6]),
                 q='Three squares with sides {a} cm, {b} cm and {c} cm stand side by side in a row on the same line, smallest on the left. Find the area of the figure.', answer='a*a+b*b+c*c',
                 hint='The figure is made of the three squares. Find the area of each.',
                 steps=['The squares have areas {a} × {a}, {b} × {b} and {c} × {c} cm².', 'Add them: the area is {ans} cm².']),
        fig=lambda e: squares_row_fig((e['a'], e['b'], e['c'])),
        oracle=lambda e: poly_area(squares_row_poly((e['a'], e['b'], e['c'])))),
    'T4p': dict(
        base=dict(a=2, b=3, c=4),
        tpl=dict(vars=dict(a=[1, 2], b=[3, 4], c=[5, 6]),
                 q='Three squares with sides {a} cm, {b} cm and {c} cm stand side by side in a row on the same line, smallest on the left. Find the perimeter of the figure.', answer='2*(a+b+2*c)',
                 hint='The steps all go the same way. What shape is the outline when you push them out?',
                 steps=['Push the steps out. The figure fits in a rectangle ({a} + {b} + {c}) cm long and {c} cm high.', 'The perimeter is 2 × ({a} + {b} + {c} + {c}) = {ans} cm.']),
        fig=lambda e: squares_row_fig((e['a'], e['b'], e['c'])),
        oracle=lambda e: poly_perimeter(squares_row_poly((e['a'], e['b'], e['c'])))),
    'G6': dict(
        base=dict(L=10, W=8),
        tpl=dict(vars=dict(L=[8, 9, 10, 12], W=[6, 7, 8]),
                 q='A garden is {L} m long and {W} m wide. Two paths 1 m wide cross it: one goes along its length and one goes across its width. What area of the garden is NOT path?', answer='(L-1)*(W-1)',
                 hint='Imagine sliding the paths to the edges of the garden. What shape is the grass then?',
                 steps=['Slide the paths to the edges. The grass makes a rectangle ({L} − 1) m by ({W} − 1) m.', '({L} − 1) × ({W} − 1) = {ans} m².']),
        fig=lambda e: garden_fig(e['L'], e['W']),
        oracle=lambda e: garden_grass(e['L'], e['W'])),
}

# ---- inquiry habit (docs/pedagogy/inquiry_skills_explicit.md; levels/habits.json)
habit_tag(ITEMS, 'Notice', ['5c-why'])
