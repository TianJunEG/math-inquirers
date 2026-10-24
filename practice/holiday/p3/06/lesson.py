"""Online practice for Level 3 (Primary 3, ages 8-10) holiday lesson 6: Fraction Walls (Fractions).

The questions are the ones printed in the Level 3 holiday workbook (p3/workbook_html.js builds it from p3/content/l6.js: Start here = the lesson's workbook()
pages; Think harder 1 to 4 and Go further 5 to 7 = qbank stretch[0..3] and challenge[-3:]; the Extra pair = deck.takeHome (printed as "Take-home");
the Investigation = p3/gifted.json lesson 6).  Every answer is recomputed by an INDEPENDENT checker below (exact fraction arithmetic with fractions.Fraction, cross-multiplying,
counting the shaded and the equal parts of the printed figure, trying every way to fill a bar), never a copy of the printed answer; build_holiday.py stops if a checker
and the printed answer differ.  The bars of Q5, Think harder 2 to 4 and Go further 6 are the workbook's own figures (p3/figs_l3.js, via p3/figs_p3_w3.js); the fraction wall,
the five shapes and the partner cards are the printed ones redrawn larger so that the parts and the fractions can be read on a phone (the shaded parts and the cards are the
printed ones; the shape counts are checked against the printed figure).
"""
import itertools, os, re, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *          # noqa: E402,F401
from p3lib import *         # noqa: E402,F401
from p3lib_w3 import *      # noqa: E402,F401

META = dict(level=3, lesson=6, key='p3', title='Fraction Walls', workbook_title='FRACTION WALLS', topic='Fractions', strand='Fractions',
            sources=['p3/content/l6.js', 'p3/gifted.json'],
            intro=['Each row of a fraction wall is one whole, cut into EQUAL parts. To compare or add fractions, make the parts the same size.',
                   'Type a fraction with a slash, like 1/5. A fraction that is equal to the answer is also right. Example for adding: 1/5 + 1/10 = 2/10 + 1/10 = 3/10. Use paper to draw bars if you like.'])
FIG = figs3()
SK = 'Fractions'
WALL = wall_fig()
SHAPES = shapes_fig()
PIECES = pieces_fig()
EXTRA = 'Extra practice (not for the lesson). '


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


def top_for(a, b, d):
    """The top number t that makes a/b = t/d, found by trying t and cross-multiplying (t * b = a * d)."""
    return find(lambda t: t * b == a * d, 0, 400)


def ftext(iid, tier, no, skill, printed, calc, q, hint, steps, src, svg=None, shown=None, label=None, equiv=True):
    """A typed fraction. `printed` is the printed answer (any equal fraction up to twelve times bigger is accepted); `calc` recomputes it with exact fractions."""
    acc = eq_forms(Fr(printed))
    d = I(id=iid, tier=tier, no=no, type='text', skill=skill, accept=acc, shown=shown or acc[0], equiv_frac=equiv,
          check=lambda: ftxt(calc()), q=q, hint=hint, steps=steps, src=src)
    if svg:
        d['svg'] = svg
    if label:
        d['label'] = label
    return d


def cmp_item(iid, no, a, b, hint, steps, svg=None):
    (an, ad), (bn, bd) = a, b
    sym = lambda: '>' if Fr(an, ad) > Fr(bn, bd) else ('<' if Fr(an, ad) < Fr(bn, bd) else '=')
    opts = [f'{an}/{ad} > {bn}/{bd}', f'{an}/{ad} < {bn}/{bd}', f'{an}/{ad} = {bn}/{bd}']
    ans = {'>': opts[0], '<': opts[1], '=': opts[2]}[sym()]
    d = I(id=iid, tier='core', no=no, type='choice', options=opts, answer=ans, skill='comparing fractions', check=lambda: f'{an}/{ad} {sym()} {bn}/{bd}',
          q=f'Which is true? Compare {an}/{ad} and {bn}/{bd}.', hint=hint, steps=steps, src=[' or = in each circle.'])
    if svg:
        d['svg'] = svg
    return d


def order_item(iid, tier, no, fracs, q, hint, steps, src, svg=None):
    """Put fractions in order, smallest first: typed 'a, b, c' (any equal fractions, same order; also with < between them)."""
    srt = sorted(fracs, key=lambda f: f)
    plain = [f'{f.numerator}/{f.denominator}' for f in srt]
    from math import lcm
    L = 1
    for f in srt:
        L = lcm(L, f.denominator)
    common = [f'{f.numerator * (L // f.denominator)}/{L}' for f in srt]
    acc = list_forms(plain) + [x for x in list_forms(common) if x not in list_forms(plain)]
    d = I(id=iid, tier=tier, no=no, type='text', skill='ordering fractions', accept=acc, shown=', '.join(plain), equiv_frac=True,
          check=lambda: ', '.join(ftxt(f) for f in sorted(fracs)), q=q, hint=hint, steps=steps, src=src)
    if svg:
        d['svg'] = svg
    return d


def letter_forms(letters):
    out = set()
    for p in itertools.permutations(letters):
        out.update([', '.join(p), ','.join(p), ' '.join(p), '; '.join(p), ', '.join(p[:-1]) + ' and ' + p[-1]])
    first = ', '.join(letters)
    return [first] + sorted(out - {first})


def printed_shapes():
    """{shape: (equal parts, shaded parts)} counted from the PRINTED figure (the workbook's own svg): A square with n diagonals, B strips, C sectors, D and E grids of squares."""
    s = FIG['l6_shapes']
    Y = '#FFC93C'
    lines_a = len(re.findall(r'<line\b', s))
    a = (2 * lines_a, len(re.findall(r'<polygon\b[^>]*fill="' + Y + '"', s)))
    strips = re.findall(r'<rect x="([\d.]+)" y="\d+" width="14" height="70" fill="(#\w+)"', s)
    b = (len(strips), sum(1 for _, f in strips if f == Y))
    paths = re.findall(r'<path\b[^>]*fill="(#\w+)"', s)
    c = (len(paths), sum(1 for f in paths if f == Y))
    sq = re.findall(r'<rect x="(\d+)" y="\d+" width="25" height="25" fill="(#\w+)"', s)
    d = [(int(x), f) for x, f in sq if int(x) < 480]
    e = [(int(x), f) for x, f in sq if int(x) >= 480]
    return dict(A=a, B=b, C=c, D=(len(d), sum(1 for _, f in d if f == Y)), E=(len(e), sum(1 for _, f in e if f == Y)))


PS = printed_shapes()
assert PS == {k: tuple(v) for k, v in {'A': (4, 1), 'B': (8, 2), 'C': (6, 2), 'D': (12, 3), 'E': (8, 3)}.items()}, PS      # the printed figure has the parts the key says


def shape_item(letter, printed):
    return ftext(f'3b-{letter}', 'core', f'3(b) {letter}', 'fraction of a shape', printed, lambda: Fr(PS[letter][1], PS[letter][0]),
                 f'Each shape is cut into EQUAL parts. What fraction of shape {letter} is shaded? Type a fraction.',
                 'Count all the equal parts: that is the bottom number. Count the shaded parts: that is the top number.',
                 {'A': ['Shape A is a square cut by two lines from corner to corner into 4 equal triangles. 1 triangle is shaded: 1/4.'],
                  'B': ['Shape B is cut into 8 equal strips. 2 strips are shaded: 2/8. (This is the same as 1/4.)'],
                  'C': ['Shape C is a circle cut into 6 equal parts. 2 parts are shaded: 2/6. (This is the same as 1/3.)'],
                  'D': ['Shape D is a grid of 4 × 3 = 12 equal squares. 3 squares are shaded, even though they do not touch: 3/12. (This is the same as 1/4.)'],
                  'E': ['Shape E is a grid of 4 × 2 = 8 equal squares. 3 squares are shaded: 3/8.']}[letter] +
                 [{'A': 'The shaded part is 1/4 of the whole shape.', 'B': '2/8 is equal to 1/4, so shape B has 1/4 shaded.', 'C': '2/6 is equal to 1/3, not 1/4.',
                   'D': '3/12 is equal to 1/4, so shape D has 1/4 shaded.', 'E': '3/8 is not equal to 1/4 (1/4 = 2/8), so shape E does not have 1/4 shaded.'}[letter]],
                 ['Write the fraction shaded in each of the other shapes.'], svg=SHAPES, label=f'3(b) {letter}')


# the ten partner cards of Q6 (as printed): five yellow, five blue
YELLOW = [(1, 4), (2, 3), (3, 8), (5, 12), (1, 6)]
BLUE = [(7, 12), (6, 8), (5, 6), (5, 8), (4, 12)]
CARDS = cards_fig(YELLOW, BLUE)


def partner(n, d):
    """The blue card that makes ONE WHOLE with the yellow card n/d (found by adding every blue card to it); exactly one must."""
    return one([b for b in BLUE if Fr(n, d) + Fr(*b) == 1])


def pair_item(k, printed_blue):
    n, d = YELLOW[k]
    return ftext(f'6-{n}-{d}', 'core', f'6 ({n}/{d})', 'fractions that make one whole', printed_blue, lambda: Fr(*partner(n, d)),
                 f'{EXTRA}Pair each yellow card with the blue card that makes ONE WHOLE with it. Which blue card goes with the yellow card {n}/{d}? Type the fraction on that blue card.',
                 f'Add each blue card to {n}/{d}, or take {n}/{d} away from 1 whole. Which blue card is the match?',
                 [f'Take {n}/{d} away from 1 whole: 1 - {n}/{d} = {ftxt(1 - Fr(n, d))}.', f'The blue card with this value is {printed_blue}.', f'Check: {n}/{d} + {printed_blue} makes 1 whole.'],
                 ['Pair each yellow card with the blue card that makes one whole with it.', 'Partners that make ONE WHOLE.'], svg=CARDS, shown=printed_blue, label=f'6: {n}/{d}')


def wall_equal(iid, no, a, b, mults, extra, hint, steps):
    frame = grp(f'{a}/{b} = ' + '      = '.join(f'{{f{i + 1}}}/{b * m}' for i, m in enumerate(mults)))
    return I(id=iid, tier='core', no=no, type='fields', skill='equal fractions', answer=[a * m for m in mults], svg=WALL, frame=frame,
             q=extra + 'Use the fraction wall. Fill in the boxes to make equal fractions.', check=lambda: [top_for(a, b, b * m) for m in mults],
             hint=hint, steps=steps, src=['Use the fraction wall.'])


ITEMS = [
    # ================= Start here (workbook lesson 6, No.1 to No.6)
    wall_equal('1a', '1(a)', 1, 2, (2, 3, 4, 6), '', 'Find 1/2 on the wall. Which pieces in the other rows end at the same place?',
               ['1/2 lines up with 2 quarters, 3 sixths, 4 eighths and 6 twelfths.', 'So 1/2 = 2/4 = 3/6 = 4/8 = 6/12.']),
    wall_equal('1b', '1(b)', 2, 3, (2, 4), '', 'Find 2 thirds on the wall. Which pieces in the sixths row and the twelfths row end at the same place?',
               ['2/3 lines up with 4 sixths and with 8 twelfths.', 'So 2/3 = 4/6 = 8/12. (Top and bottom were both multiplied by 2, then by 4.)']),
    wall_equal('1c', '1(c)', 3, 4, (2, 3), EXTRA, 'Find 3 quarters on the wall. Which pieces in the eighths row and the twelfths row end at the same place?',
               ['3/4 lines up with 6 eighths and with 9 twelfths.', 'So 3/4 = 6/8 = 9/12. (Top and bottom were both multiplied by 2, then by 3.)']),
    I(id='1d', tier='core', no='1(d)', type='choice', skill='equal fractions', svg=WALL,
      options=['Each bottom number is double its top number', 'Each top number is double its bottom number', 'The top numbers are all the same', 'The bottom numbers are all the same'],
      answer='Each bottom number is double its top number',
      q='Look at your answers to 1(a): 1/2 = ?/4 = ?/6 = ?/8 = ?/12. What do you notice about the top and bottom numbers?',
      check=lambda: 'Each bottom number is double its top number' if all(b == 2 * top_for(1, 2, b) for b in (4, 6, 8, 12)) else 'other',
      hint='Pick two of the equal fractions. Compare the top number with the bottom number of the same fraction.',
      steps=['The equal fractions are 1/2, 2/4, 3/6, 4/8 and 6/12.', 'In each one the bottom number is double the top number: 2 = 2 × 1, 4 = 2 × 2, 6 = 2 × 3, 8 = 2 × 4, 12 = 2 × 6.', 'The top and bottom numbers were multiplied by the same number each time, so they keep the same pattern.'],
      src=['Look at your answers to (a). What do you notice about the top and bottom numbers?']),

    cmp_item('2a', '2(a)', (1, 5), (1, 7), 'Both fractions have 1 piece. Compare the size of one fifth and one seventh.',
             ['Both fractions have 1 piece, so compare the size of the pieces.', 'A whole cut into 5 equal parts has bigger pieces than a whole cut into 7 equal parts.', 'So 1/5 > 1/7.']),
    cmp_item('2b', '2(b)', (3, 8), (5, 8), 'Both fractions are in eighths: the pieces are the same size. Which has more pieces?',
             ['Both are eighths, so the pieces are the same size.', '3 pieces are fewer than 5 pieces.', 'So 3/8 < 5/8.']),
    cmp_item('2c', '2(c)', (2, 3), (4, 6), 'Change 2/3 into sixths. Then compare.',
             ['2/3 = 4/6 (multiply the top and the bottom by 2).', 'The two fractions are the same amount.', 'So 2/3 = 4/6.']),
    cmp_item('2d', '2(d)', (3, 4), (5, 8), 'Change 3/4 into eighths. Then compare the top numbers.',
             ['3/4 = 6/8 (multiply the top and the bottom by 2).', '6/8 is more than 5/8.', 'So 3/4 > 5/8.']),
    cmp_item('2e', '2(e)', (4, 9), (4, 7), 'Both fractions have 4 pieces. Compare the size of one ninth and one seventh.',
             ['Both fractions have 4 pieces, so compare the size of the pieces.', 'A whole cut into 9 equal parts has smaller pieces than a whole cut into 7 equal parts.', 'So 4/9 < 4/7.']),
    cmp_item('2f', '2(f)', (2, 3), (3, 4), 'Change both fractions to twelfths. Then compare the top numbers.',
             ['2/3 = 8/12 and 3/4 = 9/12.', '8/12 is less than 9/12.', 'So 2/3 < 3/4.']),
    order_item('2g', 'core', '2(g)', [Fr(5, 12), Fr(1, 2), Fr(1, 3), Fr(3, 4)],
               'Put in order, smallest first: 5/12, 1/2, 1/3, 3/4. Type them with commas.',
               'Change them all to the same bottom number. Which bottom number do 12, 2, 3 and 4 all go into?',
               ['Change them all to twelfths: 5/12, 1/2 = 6/12, 1/3 = 4/12, 3/4 = 9/12.', 'Put the top numbers in order: 4, 5, 6, 9.', 'Smallest first: 1/3, 5/12, 1/2, 3/4.'],
               ['Put in order, smallest first:']),

    I(id='3a', tier='core', no='3(a)', type='text', skill='one quarter of a shape', svg=SHAPES, accept=letter_forms(['A', 'B', 'D']), shown='A, B, D',
      q='Each shape is cut into equal parts. Which shapes have exactly 1/4 shaded? Type the letters with commas.',
      check=lambda: ', '.join(k for k in 'ABCDE' if Fr(PS[k][1], PS[k][0]) == Fr(1, 4)),
      hint='For each shape, count all the equal parts and the shaded parts. Which shapes shade 1 out of 4 equal parts, or the same amount?',
      steps=['A shades 1 of 4 equal parts: 1/4.', 'B shades 2 of 8: 2/8 = 1/4. D shades 3 of 12: 3/12 = 1/4.', 'C shades 2/6 and E shades 3/8, which are not 1/4. So the shapes are A, B and D.'],
      src=['Each shape is cut into equal parts.', 'Which shapes have exactly ']),
    shape_item('A', '1/4'), shape_item('B', '2/8'), shape_item('C', '2/6'), shape_item('D', '3/12'), shape_item('E', '3/8'),

    ftext('4a', 'core', '4(a)', 'adding fractions', '5/7', lambda: Fr(2, 7) + Fr(3, 7), 'Add: 2/7 + 3/7. Type the answer as a fraction.',
          'The parts are the same size (sevenths). Add the number of parts.',
          ['Both are sevenths, so the parts are the same size.', 'Add the top numbers: 2 + 3 = 5. The bottom number stays 7.', '2/7 + 3/7 = 5/7.'],
          ['Add or subtract. Make the parts the same size first. Use your fraction wall.'], shown='5/7'),
    ftext('4b', 'core', '4(b)', 'adding fractions', '5/8', lambda: Fr(1, 4) + Fr(3, 8), 'Add: 1/4 + 3/8. Type the answer as a fraction.',
          'Change one fraction first so both have parts of the same size. Example: 1/5 + 1/10 = 2/10 + 1/10 = 3/10.',
          ['1/4 = 2/8, so change 1/4 into eighths.', '2/8 + 3/8 = 5/8.', '1/4 + 3/8 = 5/8.'], ['Add or subtract. Make the parts the same size first. Use your fraction wall.'], svg=WALL, shown='5/8'),
    ftext('4c', 'core', '4(c)', 'adding fractions', '9/12', lambda: Fr(1, 3) + Fr(5, 12), 'Add: 1/3 + 5/12. Type the answer as a fraction.',
          'Change one fraction first so both have parts of the same size.',
          ['1/3 = 4/12, so change 1/3 into twelfths.', '4/12 + 5/12 = 9/12.', '1/3 + 5/12 = 9/12 (which is the same as 3/4).'], ['Add or subtract. Make the parts the same size first. Use your fraction wall.'], svg=WALL, shown='9/12 (or 3/4)'),
    ftext('4d', 'core', '4(d)', 'subtracting fractions', '3/6', lambda: Fr(5, 6) - Fr(1, 3), 'Subtract: 5/6 − 1/3. Type the answer as a fraction.',
          'Change one fraction first so both have parts of the same size.',
          ['1/3 = 2/6, so change 1/3 into sixths.', '5/6 - 2/6 = 3/6.', '5/6 - 1/3 = 3/6 (which is the same as 1/2).'], ['Add or subtract. Make the parts the same size first. Use your fraction wall.'], svg=WALL, shown='3/6 (or 1/2)'),
    ftext('4e', 'core', '4(e)', 'subtracting fractions', '7/10', lambda: Fr(1) - Fr(3, 10), 'Subtract: 1 − 3/10. Type the answer as a fraction.',
          'One whole is a number of tenths. How many tenths? Then take 3 tenths away.',
          ['1 whole = 10/10.', '10/10 - 3/10 = 7/10.', '1 - 3/10 = 7/10.'], ['Add or subtract. Make the parts the same size first. Use your fraction wall.'], shown='7/10'),
    ftext('4f', 'core', '4(f)', 'adding fractions', '8/10', lambda: Fr(1, 2) + Fr(3, 10), 'Add: 1/2 + 3/10. Type the answer as a fraction.',
          'Change one fraction first so both have parts of the same size.',
          ['1/2 = 5/10, so change 1/2 into tenths.', '5/10 + 3/10 = 8/10.', '1/2 + 3/10 = 8/10 (which is the same as 4/5).'], ['Add or subtract. Make the parts the same size first. Use your fraction wall.'], shown='8/10 (or 4/5)'),

    ftext('5a', 'core', '5(a)', 'fractions of a whole', '5/6', lambda: Fr(1, 6) + Fr(2, 3),
          'Ravi paints 1/6 of a fence in the morning and 2/3 of it in the afternoon. The bar shows the fence cut into 6 equal parts. What fraction of the fence has he painted? Type a fraction.',
          'Change 2/3 into sixths first. Use the bar.',
          ['2/3 = 4/6 (the bar has 6 equal parts, and 2/3 of it is 4 parts).', '1/6 + 4/6 = 5/6.', 'Ravi has painted 5/6 of the fence.'],
          ['Ravi paints ', ' of a fence in the morning and ', ' of it in the afternoon. Draw a bar.', 'What fraction has he painted?'], svg=FIG['l6_q5'], shown='5/6'),
    ftext('5b', 'core', '5(b)', 'fractions of a whole', '1/6', lambda: Fr(1) - (Fr(1, 6) + Fr(2, 3)),
          'Ravi paints 1/6 of a fence in the morning and 2/3 in the afternoon. What fraction of the fence is NOT painted? Type a fraction.',
          'The whole fence is 1, or 6/6. Take away the painted part.',
          ['The painted part is 5/6 (1/6 + 4/6).', 'The whole fence is 6/6, so 6/6 - 5/6 = 1/6.', '1/6 of the fence is not painted.'],
          ['What fraction is not painted?'], svg=FIG['l6_q5'], shown='1/6'),
    ftext('5c', 'core', '5(c)', 'fractions of a whole', '3/6', lambda: Fr(2, 3) - Fr(1, 6),
          'Ravi paints 1/6 of a fence in the morning and 2/3 in the afternoon. How much more of the fence did he paint in the afternoon than in the morning? Type a fraction.',
          'Change 2/3 into sixths first. Then find the difference.',
          ['2/3 = 4/6.', '4/6 - 1/6 = 3/6.', 'He painted 3/6 of the fence more in the afternoon (3/6 is the same as 1/2).'],
          ['How much more did he paint in the afternoon than in the morning?'], svg=FIG['l6_q5'], shown='3/6 (or 1/2)'),

    pair_item(0, '6/8'), pair_item(1, '4/12'), pair_item(2, '5/8'), pair_item(3, '7/12'), pair_item(4, '5/6'),

    # ================= Investigation (Investigation and look back page, No.8: Find all the ways)
    ftext('I8-easy', 'invest', '8 easy', 'making a fraction from pieces', '1/4', lambda: Fr(3, 4) - Fr(1, 2),
          'Make exactly 3/4 using pieces of 1/2, 1/4 and 1/8. Easy first step: make 3/4 with one half. How much is left to fill? Type a fraction.',
          'Take the half away from 3/4. You can use eighths: 3/4 = 6/8.',
          ['3/4 = 6/8 and 1/2 = 4/8.', '6/8 - 4/8 = 2/8, which is the same as 1/4.', 'After one half, 1/4 is left to fill.'],
          ['Easy first step: make 3/4 with one half. How much is left to fill?'], svg=PIECES, shown='1/4 (or 2/8)', label='Inv easy'),
    I(id='I8a-half', tier='invest', no='8(a) one half', label='Inv 1 half', type='number', skill='making a fraction from pieces', answer=2, svg=PIECES,
      q='Make exactly 3/4 using pieces of 1/2, 1/4 and 1/8. Use as many of each as you like; the order does not matter. In how many different ways can you do it with one 1/2 piece? Type the number.',
      check=lambda: len([w for w in ways(6) if w[0] == 1]),
      hint='Put a 1/2 piece down. How much is left? Fill that with quarters and eighths in every possible way.',
      steps=['After one 1/2, 1/4 is left (3/4 - 1/2).', '1/4 can be filled with one 1/4, or with two 1/8s.', 'So 2 ways: 1/2 + 1/4, and 1/2 + 1/8 + 1/8.'],
      src=['Make exactly 3/4 using pieces of 1/2, 1/4 and 1/8.', 'List every way. Start with the most halves.']),
    I(id='I8a-nohalf', tier='invest', no='8(a) no half', label='Inv no half', type='number', skill='making a fraction from pieces', answer=4, svg=PIECES,
      q='Make exactly 3/4 using pieces of 1/2, 1/4 and 1/8. Use as many of each as you like; the order does not matter. In how many different ways can you do it with NO 1/2 piece? Type the number.',
      check=lambda: len([w for w in ways(6) if w[0] == 0]),
      hint='Use quarters and eighths only. Work in order: decide the quarters first, then fill the rest with eighths.',
      steps=['3/4 is 6 eighths. A quarter is 2 eighths.', '3 quarters; 2 quarters + 2 eighths; 1 quarter + 4 eighths; 6 eighths.', 'So 4 ways with no halves.'],
      src=['Make exactly 3/4 using pieces of 1/2, 1/4 and 1/8.', 'List every way. Start with the most halves.']),
    I(id='I8a-total', tier='invest', no='8(a) all', label='Inv all ways', type='number', skill='making a fraction from pieces', answer=6, svg=PIECES,
      q='Make exactly 3/4 using pieces of 1/2, 1/4 and 1/8. Use as many of each as you like; the order does not matter. In how many different ways in all can you do it? Type the number.',
      check=lambda: len(ways(6)),
      hint='Work in order: first decide how many halves, then how many quarters, then fill the rest with eighths.',
      steps=['With one 1/2: 1/2 + 1/4 and 1/2 + 1/8 + 1/8 (2 ways).', 'With no 1/2: 3 quarters; 2 quarters + 2 eighths; 1 quarter + 4 eighths; 6 eighths (4 ways).', '2 + 4 = 6 ways in all.'],
      src=['Make exactly 3/4 using pieces of 1/2, 1/4 and 1/8.', 'List every way. Start with the most halves.']),
    I(id='I8a-list', tier='invest', no='8(a) list', label='Inv list', type='selfcheck', paper=True, skill='making a fraction from pieces', svg=PIECES,
      q='Make exactly 3/4 using pieces of 1/2, 1/4 and 1/8. List every way. Start with the most halves.',
      check=lambda: ways(6), sol_fig=lambda ws: ways_fig(ws, 6, 'The 6 ways to make three quarters: 1/2 + 1/4; 1/2 + 1/8 + 1/8; 1/4 + 1/4 + 1/4; 1/4 + 1/4 + 1/8 + 1/8; 1/4 + four 1/8; six 1/8.'),
      hint='Start with one half. Then use no halves, and use quarters first, then fill the rest with eighths.',
      steps=['With one half: 1/2 + 1/4, and 1/2 + 1/8 + 1/8.', 'With no half: 1/4 + 1/4 + 1/4; 1/4 + 1/4 + 1/8 + 1/8; 1/4 + 1/8 + 1/8 + 1/8 + 1/8; and six 1/8.', 'That is 6 ways.'],
      src=['List every way. Start with the most halves.']),
    I(id='I8b-how', tier='invest', no='8(b) how do you know', label='Inv how', type='selfcheck', open=True, marking_mode='self', skill='explaining why',
      q='How do you know you have found ALL the ways to make 3/4 with pieces of 1/2, 1/4 and 1/8? Write your idea, then compare with the answer shown.',
      check=lambda: [len(ways(6)), sorted(ways(6), reverse=True) == ways(6)],
      hint='Think about a way of listing that cannot miss one: decide the biggest pieces first.',
      steps=['Fix the number of halves first (1 or 0). Then fix the number of quarters. Then fill what is left with eighths.', 'Because you go through every choice in order, nothing is missed and nothing is repeated.', 'This gives 2 ways with a half and 4 ways with no half: 6 in all.'],
      src=['How do you know you have found them all?']),
    I(id='I8c-more', tier='invest', no='8(c) more or fewer', label='Inv more?', type='choice', skill='making a fraction from pieces', svg=PIECES,
      options=['More ways than for 3/4', 'Fewer ways than for 3/4', 'The same number of ways'], answer='More ways than for 3/4',
      q='What if we want exactly 1 whole instead of 3/4, with pieces of 1/2, 1/4 and 1/8? Do you think there will be more ways or fewer? Test your idea, then choose.',
      check=lambda: 'More ways than for 3/4' if len(ways(8)) > len(ways(6)) else ('Fewer ways than for 3/4' if len(ways(8)) < len(ways(6)) else 'The same number of ways'),
      hint='Count the ways to make 1 whole in the same organised way: halves first, then quarters, then eighths.',
      steps=['3/4 is 6 eighths and 1 whole is 8 eighths, so there are 2 more eighths to fill.', 'With 1/8 pieces to use, every way to make 3/4 can be finished off with one more 1/4, so we expect more ways for 1 whole.', 'Count them to be sure: that is the next question.'],
      src=['What if we want exactly 1 whole instead? Do you think there will be more ways or fewer? Test your idea.']),
    I(id='I8c-count', tier='invest', no='8(c) count', label='Inv 1 whole', type='number', skill='making a fraction from pieces', answer=9, svg=PIECES,
      q='How many different ways can you make exactly 1 whole with pieces of 1/2, 1/4 and 1/8? Use as many of each as you like; the order does not matter. Type the number.',
      check=lambda: len(ways(8)),
      hint='Work in order: two halves, then one half, then no halves. For each, fill the rest with quarters and eighths.',
      steps=['Two halves: 1 way.', 'One half (and 1/2 left to fill with quarters and eighths): 3 ways.', 'No halves (1 whole of quarters and eighths): 5 ways. 1 + 3 + 5 = 9 ways.'],
      src=['What if we want exactly 1 whole instead?']),

    # ================= Think harder (workbook Think harder, No.1 to No.4)
    I(id='T1a', tier='stretch', no='T1', label='T1', type='text', skill='fractions between two fractions', svg=WALL, accept=list_forms(['7/12', '8/12'], ordered=False) , shown='7/12, 8/12', equiv_frac=False,
      q='Find ALL the fractions with bottom number 12 that are bigger than 1/2 but smaller than 3/4. Write each one with bottom number 12, with commas between them.',
      check=lambda: ', '.join(f'{n}/12' for n in range(1, 12) if Fr(1, 2) < Fr(n, 12) < Fr(3, 4)),
      hint='Look at the twelfths row of the wall. Find 1/2 and 3/4 in it. Which twelfths are between them?',
      steps=['1/2 = 6/12 and 3/4 = 9/12.', 'The twelfths between 6/12 and 9/12 are 7/12 and 8/12. (The end fractions 6/12 and 9/12 are not between.)', 'The fractions are 7/12 and 8/12.'],
      src=['Find ALL the fractions with bottom number 12 that are bigger than 1/2 but smaller than 3/4.']),
    I(id='T1b', tier='stretch', no='T1 (b)', label='T1 (b)', type='fields', skill='equal fractions', answer=[8], frame='2/3 = {f1}/12',
      q='Which fraction with bottom number 12 is equal to 2/3? Fill in the box.',
      check=lambda: [top_for(2, 3, 12)],
      hint='Find 2/3 on the wall. Which twelfths end at the same place?',
      steps=['3 × 4 = 12, so multiply the top and bottom of 2/3 by 4.', '2 × 4 = 8, so 2/3 = 8/12.'],
      src=['Which one is equal to 2/3?']),
    I(id='T2', tier='stretch', no='T2', type='choice', skill='comparing fractions', svg=FIG['l6_t2'], options=['3/5 is bigger', '7/10 is bigger', 'They are equal'], answer='7/10 is bigger',
      q='Which is bigger, 3/5 or 7/10? The two bars have the same length. One is cut into fifths and one into tenths.',
      check=lambda: '3/5 is bigger' if Fr(3, 5) > Fr(7, 10) else ('7/10 is bigger' if Fr(7, 10) > Fr(3, 5) else 'They are equal'),
      hint='Change one of the fractions so that both have parts of the same size.',
      steps=['3/5 = 6/10 (each fifth is 2 tenths).', '6/10 is less than 7/10.', '7/10 is bigger.'],
      src=['Which is bigger, 3/5 or 7/10? Show how you know.']),
    I(id='T2-how', tier='stretch', no='T2 (how)', label='T2 (how)', type='selfcheck', open=True, marking_mode='self', skill='explaining why',
      q='Show how you know which is bigger, 3/5 or 7/10. Write your idea, then compare with the answer shown.',
      check=lambda: [Fr(3, 5) == Fr(6, 10), Fr(6, 10) < Fr(7, 10)],
      hint='Make the parts the same size first, then compare the top numbers.',
      steps=['Change 3/5 into tenths: 3/5 = 6/10, because each fifth is 2 tenths.', 'Compare 6/10 and 7/10: 6 is less than 7.', 'So 7/10 is bigger. A drawing of two bars of the same length shows the same.'],
      src=['Show how you know.']),
    ftext('T3a', 'stretch', 'T3', 'adding fractions', '3/4', lambda: Fr(1, 4) + Fr(1, 2),
          'Siti reads 1/4 of a book on Monday and 1/2 of the book on Tuesday. What fraction of the book has she read? Type a fraction.',
          'The bar shows the book cut into 4 equal parts. How many parts is 1/2 of the book?',
          ['1/2 = 2/4 (the bar has 4 equal parts).', '1/4 + 2/4 = 3/4.', 'Siti has read 3/4 of the book.'],
          ['Siti reads 1/4 of a book on Monday and 1/2 of the book on Tuesday. What fraction of the book has she read?'], svg=FIG['l6_t3'], shown='3/4', label='T3'),
    ftext('T3b', 'stretch', 'T3 (left)', 'fractions of a whole', '1/4', lambda: Fr(1) - (Fr(1, 4) + Fr(1, 2)),
          'Siti reads 1/4 of a book on Monday and 1/2 of the book on Tuesday. What fraction of the book is left? Type a fraction.',
          'The whole book is 1, or 4/4. Take away what she has read.',
          ['She has read 1/4 + 2/4 = 3/4.', '4/4 - 3/4 = 1/4.', '1/4 of the book is left.'],
          ['What fraction is left?'], svg=FIG['l6_t3'], shown='1/4', label='T3 (left)'),
    order_item('T4', 'stretch', 'T4', [Fr(2, 3), Fr(5, 6), Fr(7, 12)],
               'Put these in order, smallest first: 2/3, 5/6, 7/12. The three bars have the same length. Type them with commas.',
               'Change them all to the same bottom number. Use the bars: which bottom number do thirds, sixths and twelfths all go into?',
               ['Change them all to twelfths: 2/3 = 8/12, 5/6 = 10/12, 7/12 stays 7/12.', 'Put the top numbers in order: 7, 8, 10.', 'Smallest first: 7/12, 2/3, 5/6.'],
               ['Put these in order, smallest first: 2/3, 5/6, 7/12.'], svg=FIG['l6_t4']),

    # ================= Go further (workbook Go further, No.5 to No.7) and the Extra pair (printed as "Take-home")
    I(id='G5', tier='challenge', no='G5', type='selfcheck', open=True, marking_mode='open', skill='making up a riddle',
      q='Make up your own "What fraction am I?" riddle, like: "I am equal to 3/4. My top and bottom numbers add up to ___." Choose a number for the blank and check your riddle. Then read it to a partner or a grown-up.',
      check=lambda: [s for s in range(2, 61) if len([n for n in range(1, s) if n * 4 == 3 * (s - n)]) == 1][:3],
      hint='Write some fractions equal to 3/4. Add the top and bottom of each one. Which number will you put in the blank?',
      steps=['Answers vary. Check that the fraction is equal to the one in your riddle, and that only one fraction fits your clue.', 'Example: "I am equal to 3/4. My top and bottom numbers add up to 21." Fractions equal to 3/4 are 3/4, 6/8, 9/12, 12/16 ... Their top and bottom numbers add up to 7, 14, 21, 28 ... so only 9/12 fits.', 'Not every number works: see the next questions.'],
      src=['Make up your own "What fraction am I?" riddle, like:']),
    I(id='G5-any', tier='challenge', no='G5 (any number?)', label='G5 any?', type='choice', skill='making up a riddle',
      options=['Yes, any number works', 'No, only some numbers work'], answer='No, only some numbers work',
      q='Here is the riddle: "I am equal to 3/4. My top and bottom numbers add up to ___." Does the riddle work for ANY number you put in the blank (so that exactly one fraction fits)?',
      check=lambda: 'Yes, any number works' if all(len([n for n in range(1, s) if n * 4 == 3 * (s - n)]) == 1 for s in range(2, 61)) else 'No, only some numbers work',
      hint='Try a few numbers in the blank, like 12 or 14. Does exactly one fraction equal to 3/4 fit each time?',
      steps=['Try 10: no fraction equal to 3/4 has top and bottom adding to 10. Try 14: 6/8 fits.', 'So some numbers work and some do not.'],
      src=['Is your riddle always going to work for any number you choose? Explain.']),
    I(id='G5-why', tier='challenge', no='G5 (explain)', label='G5 explain', type='selfcheck', open=True, marking_mode='self', skill='explaining why',
      q='Think about the riddle "I am equal to 3/4. My top and bottom numbers add up to ___." What can you say about the numbers you can put in the blank, and why? Write your idea, then compare with the answer shown.',
      check=lambda: [s for s in range(2, 61) if len([n for n in range(1, s) if n * 4 == 3 * (s - n)]) == 1],
      hint='List fractions equal to 3/4: 3/4, 6/8, 9/12 ... What happens to the top and bottom numbers each time? What do they add up to?',
      steps=['Fractions equal to 3/4: 3/4, 6/8, 9/12, 12/16 ... The top and bottom are 3 and 4 multiplied by the same number.', 'Their sums are 7, 14, 21, 28 ...: the numbers in the 7 times table (3 + 4 = 7).', 'The riddle only works if the number in the blank is in the 7 times table.'],
      src=['Is your riddle always going to work for any number you choose? Explain.']),
    I(id='G6-count', tier='challenge', no='G6', label='G6', type='number', skill='making a fraction from pieces', answer=2, svg=FIG['l6_c6'],
      q='Fill one whole bar using exactly 5 pieces. You may use 1/2, 1/4 and 1/8 pieces, as many of each as you like. How many different ways are there? Type the number.',
      check=lambda: len(ways(8, pieces=5)),
      hint='Use a table: how many halves, how many quarters, how many eighths? The pieces must add up to 1 whole, and there must be 5 pieces.',
      steps=['1 whole is 8 eighths. A half is 4 eighths, a quarter is 2 eighths.', 'One half, no quarters and four eighths: 1 + 0 + 4 = 5 pieces. And three quarters and two eighths: 0 + 3 + 2 = 5 pieces.', 'There are 2 ways.'],
      src=['Fill one whole bar using exactly 5 pieces. You may use 1/2, 1/4 and 1/8 pieces, as many of each as you like. Find all the ways.']),
    I(id='G6-list', tier='challenge', no='G6 (list)', label='G6 (list)', type='selfcheck', paper=True, skill='making a fraction from pieces', svg=FIG['l6_c6'],
      q='Find all the ways to fill one whole bar using exactly 5 pieces of 1/2, 1/4 and 1/8. Write down each way.',
      check=lambda: ways(8, pieces=5), sol_fig=lambda ws: ways_fig(ws, 8, 'The 2 ways to fill one whole bar with exactly 5 pieces: 1/2 and four 1/8; three 1/4 and two 1/8.'),
      hint='Make a table of halves, quarters and eighths. The pieces must add up to 1 whole, and there must be 5 pieces.',
      steps=['1/2 + 1/8 + 1/8 + 1/8 + 1/8 (5 pieces).', '1/4 + 1/4 + 1/4 + 1/8 + 1/8 (5 pieces).', 'No other way uses exactly 5 pieces.'],
      src=['Find all the ways.']),
    I(id='G7', tier='challenge', no='G7', type='text', skill='fractions between two fractions', accept=fracs_between(Fr(2, 3), Fr(3, 4), 60), shown='17/24 (many answers are right)',
      q='Find a fraction that is bigger than 2/3 but smaller than 3/4. Type a fraction.',
      check=lambda: '17/24' if Fr(2, 3) < Fr(17, 24) < Fr(3, 4) else None,
      hint='The fraction wall has no row that helps. Cut every part of 2/3 and 3/4 into smaller equal parts, so that there is room between them.',
      steps=['The wall has 2/3 = 8/12 and 3/4 = 9/12 side by side, with no twelfth between them.', 'Cut every part into 2 equal pieces: 2/3 = 16/24 and 3/4 = 18/24. Now 17/24 is between.', 'Many answers are possible: 25/36 works too (2/3 = 24/36, 3/4 = 27/36).'],
      src=['Find a fraction that is bigger than 2/3 but smaller than 3/4.']),
    I(id='G7-another', tier='challenge', no='G7 (another)', label='G7 another', type='selfcheck', open=True, marking_mode='self', skill='fractions between two fractions',
      q='Can you find another fraction that is bigger than 2/3 but smaller than 3/4? Write one that is different from your first. Then compare with the answers shown.',
      check=lambda: all(Fr(2, 3) < Fr(n, d) < Fr(3, 4) for n, d in ((17, 24), (25, 36), (5, 7), (34, 48))),
      hint='Cut the parts into even smaller equal parts, like 36ths or 48ths. Convert 2/3 and 3/4 and look for a top number between.',
      steps=['In 36ths: 2/3 = 24/36 and 3/4 = 27/36. So 25/36 and 26/36 are between.', 'In 48ths: 2/3 = 32/48 and 3/4 = 36/48. So 33/48, 34/48 and 35/48 are between.', '5/7 is between too (2/3 = 0.667, 5/7 = 0.714, 3/4 = 0.75). The smaller the pieces, the more fractions fit between.'],
      src=['Can you find another one?']),
    ftext('TH-a', 'challenge', 'Extra (a)', 'adding fractions', '6/9', lambda: Fr(2, 9) + Fr(4, 9), EXTRA + 'Add: 2/9 + 4/9. Type the answer as a fraction.',
          'The parts are the same size (ninths). Add the number of parts.',
          ['Both are ninths, so add the top numbers: 2 + 4 = 6.', '2/9 + 4/9 = 6/9 (which is the same as 2/3).'], ['2/9 + 4/9'], shown='6/9 (or 2/3)'),
    ftext('TH-b', 'challenge', 'Extra (b)', 'subtracting fractions', '3/5', lambda: Fr(1) - Fr(2, 5), EXTRA + 'Subtract: 1 − 2/5. Type the answer as a fraction.',
          'One whole is a number of fifths. How many fifths? Then take 2 fifths away.',
          ['1 whole = 5/5.', '5/5 - 2/5 = 3/5.'], ['1 − 2/5'], shown='3/5'),
]


# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
def _eq(e, names, mults):
    return {n: top_for(e['a'], e['b'], e['b'] * m) for n, m in zip(names, mults)}


VARIANTS = {
    '1a': dict(
        base=dict(a=1, b=2),
        tpl=dict(vars=dict(a=[1, 2, 3], b=[5, 7, 8, 9]), derive=dict(m1='b*2', m2='b*3', m3='b*4', m4='b*6'),
                 q='Fill in the boxes to make equal fractions: {a}/{b} = ?/{m1} = ?/{m2} = ?/{m3} = ?/{m4}.',
                 frame=grp('{a}/{b} = {f1}/{m1}      = {f2}/{m2}      = {f3}/{m3}      = {f4}/{m4}'), answers=dict(f1='a*2', f2='a*3', f3='a*4', f4='a*6'),
                 hint='Each bigger bottom number is the old one times something. Do the same to the top number.',
                 steps=['{m1} is {b} × 2, so the top number is multiplied by 2 as well. The same idea gives the other boxes (× 3, × 4, × 6).', 'The answers are {ans}.']),
        oracle=lambda e: _eq(e, ('f1', 'f2', 'f3', 'f4'), (2, 3, 4, 6))),
    '1b': dict(
        base=dict(a=2, b=3, k1=2, k2=4),
        tpl=dict(vars=dict(a=[1, 2, 3], b=[4, 5, 7, 8], k1=[2, 3], k2=[4, 5]), derive=dict(m1='b*k1', m2='b*k2'),
                 q='Fill in the boxes to make equal fractions: {a}/{b} = ?/{m1} = ?/{m2}.',
                 frame=grp('{a}/{b} = {f1}/{m1}      = {f2}/{m2}'), answers=dict(f1='a*k1', f2='a*k2'),
                 hint='What was {b} multiplied by to make the new bottom number? Multiply the top number by the same number.',
                 steps=['{m1} is {b} × {k1}, so multiply the top number by {k1} too. {m2} is {b} × {k2}, so multiply the top number by {k2}.', 'The answers are {ans}.']),
        oracle=lambda e: dict(f1=top_for(e['a'], e['b'], e['b'] * e['k1']), f2=top_for(e['a'], e['b'], e['b'] * e['k2']))),
    '1c': dict(
        base=dict(a=3, b=4, k1=2, k2=3),
        tpl=dict(vars=dict(a=[1, 2, 3, 4], b=[5, 7, 8, 9], k1=[2, 3], k2=[4, 5]), derive=dict(m1='b*k1', m2='b*k2'),
                 q=EXTRA + 'Fill in the boxes to make equal fractions: {a}/{b} = ?/{m1} = ?/{m2}.',
                 frame=grp('{a}/{b} = {f1}/{m1}      = {f2}/{m2}'), answers=dict(f1='a*k1', f2='a*k2'),
                 hint='What was {b} multiplied by to make the new bottom number? Multiply the top number by the same number.',
                 steps=['{m1} is {b} × {k1}, so multiply the top number by {k1} too. {m2} is {b} × {k2}, so multiply the top number by {k2}.', 'The answers are {ans}.']),
        oracle=lambda e: dict(f1=top_for(e['a'], e['b'], e['b'] * e['k1']), f2=top_for(e['a'], e['b'], e['b'] * e['k2']))),
}

for _d in ITEMS:
    if _d['type'] == 'selfcheck' and 'marking_mode' not in _d:
        _d['marking_mode'] = 'self'

# ---- inquiry habit (docs/pedagogy/inquiry_skills_explicit.md; levels/habits.json)
ITEMS.insert(max(i for i, x in enumerate(ITEMS) if x['tier'] == 'core') + 1, habit_item('Check',
    'Is 1/2 equal to 2/4? Use a fraction wall or draw it. Then test a second case: is 1/2 equal to 3/6? Does it always work to multiply the top and bottom by the same number? Write what you found.',
    ['1/2 = 2/4 and 1/2 = 3/6.', 'Multiplying the top and the bottom by the same number (2, then 3) gave a fraction of the same size.', 'I could test a third case: 4/8 is also 1/2. So far it always works.'],
    'Draw one bar for 1/2. Cut it into 4 parts, then 6 parts. How many parts are shaded?'))
