"""Level 2 (P2) holiday lesson 7: FAIR SHARES (Fractions), week 4, first lesson.  Online mirror of the printed workbook pages.

The questions are the ones printed in the Level 2 holiday workbook (p2/content/l7.js `workbook()` = Start here, p2/gaps.json lesson 7 `invest` = Investigation,
p2/content/l7.js `qbank.stretch` first four = Think harder 1 to 4, `qbank.challenge` last three = Go further 5 to 7, as built by p2/workbook_html.js, and the
"Make up your own" line).  Every answer is recomputed by an INDEPENDENT checker (the areas of the parts of each shape are found by sampling points, the shaded and the
equal parts are counted from the drawing, fractions are added with exact fractions, every way to share a cake is tried), never a copy of the printed answer;
build_holiday.py stops if a checker and the printed answer differ.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *          # noqa: E402,F401
from p2lib import *         # noqa: E402,F401
from p2lib_w4 import *      # noqa: E402,F401

STRAND = 'Fractions'
META = dict(level=2, lesson=7, key='p2', title='Fair shares', workbook_title='FAIR SHARES', topic='Fractions', strand=STRAND,
            sources=['p2/content/l7.js', 'p2/gaps.json', 'p2/workbook_html.js'],
            intro=['A fraction names EQUAL parts of a whole. The bottom number is how many equal parts the whole is cut into. The top number is how many of those parts we take.',
                   'Type a fraction in two boxes, the top number first. Bars and shapes are for looking at: draw bars on paper if it helps. Some questions ask you to explain: write your idea in the box, then read the worked solution after you submit and compare.'])


def ftxt(f):
    f = Fr(f)
    return f'{f.numerator}/{f.denominator}'


def over(f, d):
    """[top, bottom] of the fraction f written with the bottom number d (found by trying tops), so 9/12 stays 9/12 and is not reduced."""
    return [next(t for t in range(0, 4 * d) if Fr(t, d) == f), d]


# ---------------------------------------------------------------- figures
SHAPES = six_shapes_fig()
Q2A = frac_bar(8, [0, 3, 5], caption='A bar cut into 8 equal parts with 3 parts shaded')
Q2B = frac_pie(6, [0, 1, 3, 4, 5], caption='A circle cut into 6 equal parts with 5 parts shaded')
Q2C = frac_grid(5, 2, {(0, 0), (0, 1), (0, 3), (0, 4), (1, 1), (1, 2), (1, 4)}, caption='A grid of 10 equal squares with 7 squares shaded')
Q3 = printed_fig('Bars of the same length cut into equal parts, not shaded')
Q4 = {k: frac_bar(n, [], caption=f'A bar cut into {n} equal parts, none coloured') for k, n in dict(a=5, b=8, c=12, d=6, e=10).items()}
CAKE = frac_bar(8, [], 'Cake', 'A bar of 8 equal parts for the cake')
PIZZA = frac_bars([('Ravi', 4, []), ('Siti', 8, [])], 'Two bars the same length: Ravi’s pizza in 4 equal parts and Siti’s pizza in 8 equal parts')
PIZZA_SOL = frac_bars([('Ravi', 4, [0]), ('Siti', 8, [0, 1, 2])], 'Ravi’s bar with 1 of 4 parts shaded and Siti’s bar of 8 parts with 3 shaded: Siti’s shaded part is longer')
STRIPS = strips_fig()
T2 = frac_bars([('Eighths', 8, []), ('Fifths', 5, [])], 'Two bars of the same length, one cut into 8 equal parts and one cut into 5 equal parts, nothing shaded')
T2_SOL = frac_bars([('Eighths', 8, [0, 1, 2]), ('Fifths', 5, [0, 1, 2])], 'The same two bars with 3 parts shaded on each: the 3 fifths reach further than the 3 eighths')
T3 = frac_bar(8, [], caption='A bar cut into 8 equal parts')
STRIP12 = frac_bar(12, [], 'Cake', 'A cake drawn as a strip cut into 12 equal pieces')
STRIP10 = frac_bar(10, [], 'Cake', 'A cake drawn as a strip cut into 10 equal pieces')


def shaded_of(fig):
    s, n = count_parts(fig)
    return s, n


def fields_frac(iid, no, q, svg, frame, calc, answer, hint, steps, src, label=None, skill='naming and adding fractions', tier='core', **kw):
    d = dict(id=iid, tier=tier, no=no, type='fields', skill=skill, answer=answer, q=q, frame=frame, check=calc, hint=hint, steps=steps, src=src)
    if svg:
        d['svg'] = svg
    if label:
        d['label'] = label
    d.update(kw)
    return d


def total_quarters_check(k):
    return ', '.join(c for c in 'ABCDEF' if is_quarters(c))


ITEMS = [
    # ================= Start here (workbook lesson 7, No.1 to No.6)
    dict(id='1', tier='core', no='1', label='1', type='text', skill='equal parts', svg=SHAPES, accept=list_forms(['A', 'C', 'E', 'F'], ordered=False), shown='A, C, E, F', equiv_frac=False,
         q='Fair shares? Each shape has 4 parts and 1 part is shaded. Which shapes are cut into quarters (4 EQUAL parts)? Type the letters with commas.',
         check=lambda: ', '.join(c for c in 'ABCDEF' if is_quarters(c)),
         hint='A quarter needs all 4 parts to be the same size. For each shape, picture cutting out the parts and laying one on top of another. Do they match?',
         steps=['A: the 4 strips are the same width. C: the two lines go through the middle, so the 4 parts are the same. E: the two lines from corner to corner make 4 triangles that are the same size.',
                'F: the 4 small triangles are all the same size, even though the middle one is upside down.',
                'B and D have parts of different sizes. So the shapes cut into quarters are A, C, E and F.'],
         src=['Fair shares? Each shape has 4 parts and 1 part is shaded.', 'Circle the shapes that are cut into quarters (4 EQUAL parts).']),
    dict(id='1x', tier='core', no='1(a)', label='1(a)', type='selfcheck', open=False, skill='explaining equal parts', svg=SHAPES,
         q='Choose one shape that is NOT cut into quarters. Explain how you know. Write your idea in the box.',
         facts=dict(not_quarters=['B', 'D']), check=lambda: dict(not_quarters=[c for c in 'ABCDEF' if not is_quarters(c)]),
         hint='A shape is cut into quarters only if all 4 parts are the same size. Look for a shape where one part is bigger or smaller than another.',
         steps=['Shape B: the two lines do not cross in the middle of the circle, so the 4 parts are different sizes. Shape D: the 4 strips have different widths.',
                'Any answer that says the parts are not all the same size is a good one.'],
         src=['Choose one shape that is NOT cut into quarters. Explain how you know.']),

    fields_frac('2a', '2(a)', 'What fraction of the bar is shaded? What fraction is NOT shaded? Type each fraction, top number first.', Q2A, 'Shaded: {f1}/{f2}      Not shaded: {f3}/{f4}',
                lambda: (lambda s, n: [s, n, n - s, n])(*shaded_of(Q2A)), [3, 8, 5, 8],
                'Count all the equal parts first: that is the bottom number. Then count the shaded parts. The parts that are not shaded are the rest.',
                ['The bar has 8 equal parts, so the bottom number is 8. 3 parts are shaded: 3/8 is shaded.', '8 − 3 = 5 parts are not shaded: 5/8 is not shaded.', 'The two fractions together make 8/8, which is 1 whole.'],
                ['What fraction is shaded? What fraction is NOT shaded?'], label='2(a)'),
    fields_frac('2b', '2(b)', 'What fraction of the circle is shaded? What fraction is NOT shaded? Type each fraction, top number first.', Q2B, 'Shaded: {f1}/{f2}      Not shaded: {f3}/{f4}',
                lambda: (lambda s, n: [s, n, n - s, n])(*shaded_of(Q2B)), [5, 6, 1, 6],
                'Count all the equal parts of the circle first. Then count the shaded ones.',
                ['The circle has 6 equal parts, so the bottom number is 6. 5 parts are shaded: 5/6 is shaded.', '6 − 5 = 1 part is not shaded: 1/6 is not shaded.'],
                ['What fraction is shaded? What fraction is NOT shaded?'], label='2(b)'),
    fields_frac('2c', '2(c)', 'What fraction of the grid is shaded? What fraction is NOT shaded? Type each fraction, top number first.', Q2C, 'Shaded: {f1}/{f2}      Not shaded: {f3}/{f4}',
                lambda: (lambda s, n: [s, n, n - s, n])(*shaded_of(Q2C)), [7, 10, 3, 10],
                'All the squares are the same size. Count them all for the bottom number, then count the shaded ones.',
                ['The grid has 10 equal squares, so the bottom number is 10. 7 squares are shaded: 7/10 is shaded.', '10 − 7 = 3 squares are not shaded: 3/10 is not shaded.'],
                ['What fraction is shaded? What fraction is NOT shaded?'], label='2(c)'),

    dict(id='3a1', tier='core', no='3(a) first pair', label='3(a) i', type='choice', options=['1/3', '1/8'], answer='1/3', skill='comparing fractions', svg=Q3,
         q='Compare the fractions. Which is bigger, 1/3 or 1/8?',
         check=lambda: '1/3' if Fr(1, 3) > Fr(1, 8) else '1/8',
         hint='Picture two bars of the same length. One is cut into 3 equal parts and one into 8 equal parts. Which bar has the longer part?',
         steps=['Cut the same bar into 3 equal parts and into 8 equal parts. The parts of the bar cut into 3 are longer than the parts of the bar cut into 8.', 'So 1/3 is bigger than 1/8.'],
         src=['Compare the fractions. Draw bars the same length if it helps.', 'Circle the bigger fraction in each pair:']),
    dict(id='3a2', tier='core', no='3(a) second pair', label='3(a) ii', type='choice', options=['5/9', '7/9'], answer='7/9', skill='comparing fractions', svg=Q3,
         q='Compare the fractions. Which is bigger, 5/9 or 7/9?',
         check=lambda: '5/9' if Fr(5, 9) > Fr(7, 9) else '7/9',
         hint='Both bars are cut into 9 equal parts. Think about how many parts each one takes.',
         steps=['The two bars are cut into 9 equal parts, so the parts are the same size.', '7 of those parts is more than 5 of them, so 7/9 is bigger than 5/9.'],
         src=['Circle the bigger fraction in each pair:']),
    dict(id='3b', tier='core', no='3(b)', label='3(b)', type='text', skill='ordering unit fractions', svg=Q3, accept=list_forms(['1/10', '1/5', '1/4', '1/2']), shown='1/10, 1/5, 1/4, 1/2', equiv_frac=False,
         q='Put these in order, smallest first: 1/5, 1/2, 1/10, 1/4. Type them with commas.',
         check=lambda: ', '.join(ftxt(f) for f in sorted([Fr(1, 5), Fr(1, 2), Fr(1, 10), Fr(1, 4)])),
         hint='Picture the same whole cut into 2, 4, 5 and 10 equal parts. Which parts are the shortest? Which are the longest?',
         steps=['The same whole cut into more equal parts gives shorter parts.', 'The shortest part is 1/10 (10 parts), then 1/5, then 1/4, and the longest is 1/2.', 'Smallest first: 1/10, 1/5, 1/4, 1/2.'],
         src=['Smallest first:']),
    dict(id='3c1', tier='core', no='3(c)', label='3(c)', type='choice', options=['Yes', 'No'], answer='No', skill='comparing unit fractions',
         q='Mei says: “1/6 is bigger than 1/4, because 6 is bigger than 4.” Is she right?',
         check=lambda: 'Yes' if Fr(1, 6) > Fr(1, 4) else 'No',
         hint='Picture one pizza cut into 6 equal slices and the same pizza cut into 4 equal slices. Which slice is bigger?',
         steps=['The same whole cut into 6 equal parts has smaller parts than the same whole cut into 4 equal parts.', 'So 1/6 is smaller than 1/4. Mei is not right.'],
         src=['Mei says: “1/6 is bigger than 1/4, because 6 is bigger than 4.” Is she right?']),
    dict(id='3c2', tier='core', no='3(c) explain', label='3(c) why', type='selfcheck', open=False, skill='explaining comparing fractions',
         q='Mei says: “1/6 is bigger than 1/4, because 6 is bigger than 4.” Explain what you think about her idea. Write your idea in the box.',
         facts=dict(unit_fraction_smaller_when_more_parts=all(Fr(1, a) < Fr(1, b) for a in range(2, 13) for b in range(2, a))),
         check=lambda: dict(unit_fraction_smaller_when_more_parts=all(Fr(1, a) < Fr(1, b) for a in range(2, 13) for b in range(2, a))),
         hint='Draw two bars of the same length on paper, one cut into 6 equal parts and one into 4. Compare one part of each.',
         steps=['Example: If the same pizza is cut into 6 slices, each slice is smaller than a slice from the same pizza cut into 4. So 1/6 is smaller than 1/4.', 'Any idea that talks about the size of the parts is good.'],
         src=['Is she right? Explain.']),

    fields_frac('4a', '4(a)', 'Add. The bar is cut into 5 equal parts. 2/5 + 1/5 = ? Type the answer in the two boxes, top number first.', Q4['a'], '2/5 + 1/5 = {f1}/{f2}',
                lambda: over(Fr(2, 5) + Fr(1, 5), 5), [3, 5],
                'Colour 2 parts, then 1 more part, on a bar of 5 equal parts. How many parts are coloured? What are the parts called?',
                ['Colour 2 fifths, then 1 more fifth. 2 fifths and 1 fifth make 3 fifths.', 'The parts are still fifths, so the bottom number stays 5: 2/5 + 1/5 = 3/5.'],
                ['Add or take away. Colour the bars to help you. Write each answer in the box.'], label='4(a)'),
    fields_frac('4b', '4(b)', 'Add. The bar is cut into 8 equal parts. 3/8 + 4/8 = ? Type the answer in the two boxes, top number first.', Q4['b'], '3/8 + 4/8 = {f1}/{f2}',
                lambda: over(Fr(3, 8) + Fr(4, 8), 8), [7, 8],
                'Colour 3 parts, then 4 more parts, on the bar. How many are coloured? What are the parts called?',
                ['3 eighths and 4 eighths make 7 eighths.', 'The parts are still eighths: 3/8 + 4/8 = 7/8.'],
                ['Add or take away. Colour the bars to help you. Write each answer in the box.'], label='4(b)'),
    fields_frac('4c', '4(c)', 'Add. The bar is cut into 12 equal parts. 4/12 + 5/12 = ? Type the answer in the two boxes, top number first.', Q4['c'], '4/12 + 5/12 = {f1}/{f2}',
                lambda: over(Fr(4, 12) + Fr(5, 12), 12), [9, 12],
                'Colour 4 parts, then 5 more parts, on the bar. How many parts are coloured? How many equal parts does the bar have?',
                ['4 twelfths and 5 twelfths make 9 twelfths.', 'The parts are still twelfths: 4/12 + 5/12 = 9/12.'],
                ['Add or take away. Colour the bars to help you. Write each answer in the box.'], label='4(c)'),
    fields_frac('4d', '4(d)', 'The bar is cut into 6 equal parts. 1/6 + ? = 1 whole. What fraction goes in the box? Type it, top number first.', Q4['d'], '1/6 + {f1}/{f2} = 1 whole',
                lambda: over(1 - Fr(1, 6), 6), [5, 6],
                'How many sixths make 1 whole? You already have some of them. How many more do you need?',
                ['The bar has 6 equal parts, so 6 sixths make 1 whole.', 'You have 1 sixth. 6 − 1 = 5 more sixths are needed.', '1/6 + 5/6 = 6/6 = 1 whole.'],
                ['Add or take away. Colour the bars to help you. Write each answer in the box.'], label='4(d)'),
    fields_frac('4e', '4(e)', 'Take away. The bar is cut into 10 equal parts. 7/10 − 3/10 = ? Type the answer in the two boxes, top number first.', Q4['e'], '7/10 − 3/10 = {f1}/{f2}',
                lambda: over(Fr(7, 10) - Fr(3, 10), 10), [4, 10],
                'Colour 7 parts, then take away 3 of them. How many parts are still coloured? What are the parts called?',
                ['7 tenths take away 3 tenths leaves 4 tenths.', 'The parts are still tenths: 7/10 − 3/10 = 4/10.'],
                ['Add or take away. Colour the bars to help you. Write each answer in the box.'], label='4(e)'),

    fields_frac('5a', '5(a)', 'Mum cuts a cake into 8 equal slices. Ali eats 2 slices. Mei eats 3 slices. What fraction of the cake do they eat altogether?', CAKE, '{f1}/{f2} of the cake',
                lambda: over(Fr(2, 8) + Fr(3, 8), 8), [5, 8],
                'The slices are all the same size. How many slices do they eat in all? What is each slice called?',
                ['Ali eats 2 eighths and Mei eats 3 eighths. 2 + 3 = 5 slices.', 'They eat 5/8 of the cake.'],
                ['Mum cuts a cake into 8 equal slices. Ali eats 2 slices. Mei eats 3 slices.', 'What fraction of the cake do they eat altogether?'], label='5(a)'),
    fields_frac('5b', '5(b)', 'Mum cuts a cake into 8 equal slices. Ali eats 2 slices. Mei eats 3 slices. What fraction of the cake is left?', CAKE, '{f1}/{f2} of the cake',
                lambda: over(1 - Fr(2, 8) - Fr(3, 8), 8), [3, 8],
                'How many slices are left on the plate? Count the slices that nobody ate.',
                ['The cake has 8 slices. 2 + 3 = 5 slices are eaten, so 8 − 5 = 3 slices are left.', '3/8 of the cake is left.'],
                ['What fraction of the cake is left?'], label='5(b)'),
    dict(id='5c1', tier='core', no='5(c) who', label='5(c) who', type='choice', options=['Ali', 'Mei'], answer='Mei', skill='comparing fractions with the same bottom number', svg=CAKE,
         q='Mum cuts a cake into 8 equal slices. Ali eats 2 slices. Mei eats 3 slices. Who eats more?',
         check=lambda: 'Ali' if 2 > 3 else 'Mei',
         hint='The slices are the same size. Who eats more slices?',
         steps=['The slices are all the same size. Ali eats 2 slices and Mei eats 3 slices.', '3 slices is more than 2 slices, so Mei eats more.'],
         src=['Who eats more? How much more?']),
    fields_frac('5c2', '5(c) how much', 'Mum cuts a cake into 8 equal slices. Ali eats 2 slices. Mei eats 3 slices. How much more cake does the one who eats more have? Type the fraction.', CAKE,
                '{f1}/{f2} of the cake more',
                lambda: over(abs(Fr(3, 8) - Fr(2, 8)), 8), [1, 8],
                'Find how many more slices one child eats than the other. What are the slices called?',
                ['Mei eats 3 slices and Ali eats 2 slices. 3 − 2 = 1 more slice.', 'One slice is one eighth, so Mei eats 1/8 more.'],
                ['Who eats more? How much more?'], label='5(c) more'),

    dict(id='6a', tier='core', no='6', label='6', type='choice', options=['Ravi', 'Siti'], answer='Siti', skill='comparing fractions of the same whole', svg=PIZZA,
         q='Ravi and Siti each have a pizza. The pizzas are the same size. Ravi cuts his into 4 equal slices and eats 1 slice. Siti cuts hers into 8 equal slices and eats 3 slices. Who eats more pizza?',
         check=lambda: 'Ravi' if Fr(1, 4) > Fr(3, 8) else 'Siti',
         hint='Fold or line up the bars: one quarter covers two eighths. How many eighths does each child eat?',
         steps=['The bars are the same length. One quarter covers 2 eighths, so Ravi eats 2 eighths of a pizza.', 'Siti eats 3 eighths. 3 eighths is more than 2 eighths, so Siti eats more pizza.'],
         src=['Ravi and Siti each have a pizza. The pizzas are the same size.', 'Who eats more pizza?']),
    dict(id='6b', tier='core', no='6 how', label='6 how', type='selfcheck', open=False, skill='explaining with bars', svg=PIZZA,
         q='Ravi eats 1 of the 4 slices. Siti eats 3 of the 8 slices. Show how you can tell who eats more pizza, with the bars or in words. Write your idea in the box.',
         facts=dict(ravi=ftxt(Fr(1, 4)), siti=ftxt(Fr(3, 8)), quarter_in_eighths=2),
         check=lambda: dict(ravi=ftxt(Fr(1, 4)), siti=ftxt(Fr(3, 8)), quarter_in_eighths=next(k for k in range(1, 20) if Fr(k, 8) == Fr(1, 4))),
         hint='Look at the two bars. How many eighths cover one quarter?',
         steps=['Example: One quarter of Ravi’s bar covers 2 eighths of Siti’s bar. Siti’s 3 eighths reach further than that, so Siti eats more.', 'The picture shows Ravi’s 1 quarter and Siti’s 3 eighths.'],
         sol_fig=lambda facts: PIZZA_SOL,
         src=['Colour the bars to show how you know.']),

    # ================= Investigation: Fraction strips
    dict(id='I1', tier='invest', no='Investigation (a)', label='Inv 1', type='fields', skill='covering a half with equal pieces', svg=STRIPS, answer=[0, 2, 3, 4],
         q='Cover a HALF strip exactly with pieces of ONE kind only. How many pieces of each kind does it take? Type 0 if that kind cannot do it.',
         frame='thirds {f1}   quarters {f2}   sixths {f3}   eighths {f4}',
         check=lambda: [covers(k, 2) for k in (3, 4, 6, 8)],
         hint='Lay the strips on top of each other in your head, or use the picture. Start with the quarters: how many quarter strips lie on top of the half strip?',
         steps=['2 quarters, 3 sixths and 4 eighths each cover the half exactly.', 'Thirds do not: 1 third is too short, but 2 thirds is longer than a half.', 'So the boxes are 0, 2, 3 and 4.'],
         src=['Cover a HALF strip exactly with pieces of ONE kind only. Which kinds work? How many pieces of each?']),
    dict(id='I2', tier='invest', no='Investigation (b) third', label='Inv 2', type='fields', skill='covering a third with equal pieces', svg=STRIPS, answer=[0, 0, 2, 0],
         q='Now cover a THIRD strip exactly with pieces of ONE kind only. How many pieces of each kind does it take? Type 0 if that kind cannot do it.',
         frame='halves {f1}   quarters {f2}   sixths {f3}   eighths {f4}',
         check=lambda: [covers(k, 3) for k in (2, 4, 6, 8)],
         hint='Look at the third strip in the picture. Which kind of piece fits on it with no gap and nothing sticking out?',
         steps=['2 sixths cover a third exactly.', 'One half is longer than a third. Quarters and eighths do not fit exactly: 1 quarter is too short and 2 quarters stick out.', 'So the boxes are 0, 0, 2 and 0.'],
         src=['Do the same for a THIRD strip and a QUARTER strip.']),
    dict(id='I3', tier='invest', no='Investigation (b) quarter', label='Inv 3', type='fields', skill='covering a quarter with equal pieces', svg=STRIPS, answer=[0, 0, 0, 2],
         q='Now cover a QUARTER strip exactly with pieces of ONE kind only. How many pieces of each kind does it take? Type 0 if that kind cannot do it.',
         frame='halves {f1}   thirds {f2}   sixths {f3}   eighths {f4}',
         check=lambda: [covers(k, 4) for k in (2, 3, 6, 8)],
         hint='Look at the quarter strip in the picture. Which kind of piece fits on it with no gap and nothing sticking out?',
         steps=['2 eighths cover a quarter exactly.', 'Halves and thirds are longer than a quarter. 1 sixth is too short and 2 sixths stick out.', 'So the boxes are 0, 0, 0 and 2.'],
         src=['Do the same for a THIRD strip and a QUARTER strip.']),
    dict(id='I4', tier='invest', no='Investigation (c)', label='Inv 4', type='choice', options=['Yes', 'No'], answer='No', skill='why thirds do not cover a half', svg=STRIPS,
         q='Can thirds ever cover a half exactly?',
         check=lambda: 'Yes' if any(Fr(n, 3) == Fr(1, 2) for n in range(1, 200)) else 'No',
         hint='Try 1 third, then 2 thirds, then 3 thirds. Compare each with the half strip.',
         steps=['1 third is shorter than a half. 2 thirds is longer than a half. Nothing fits exactly in between.', 'So thirds can never cover a half exactly.'],
         src=['Can thirds ever cover a half exactly? Why not?']),
    dict(id='I5', tier='invest', no='Investigation (c) explain', label='Inv 5', type='selfcheck', open=False, skill='explaining with strips', svg=STRIPS,
         q='Explain your answer to: can thirds ever cover a half exactly? Write your idea in the box.',
         facts=dict(thirds_below_half=1, thirds_above_half=2), check=lambda: dict(thirds_below_half=max(n for n in range(1, 20) if Fr(n, 3) < Fr(1, 2)), thirds_above_half=min(n for n in range(1, 20) if Fr(n, 3) > Fr(1, 2))),
         hint='Count thirds one at a time and compare each with the half. When do they get past the half?',
         steps=['Example: 1 third is less than a half, and 2 thirds is more than a half, so no number of thirds is exactly a half.', 'Any idea that compares the thirds with the half is good.'],
         src=['Can thirds ever cover a half exactly? Why not?']),

    # ================= Think harder
    dict(id='T1', tier='stretch', no='Think harder 1', label='T1', type='text', skill='ordering unit fractions', accept=list_forms(['1/12', '1/5', '1/3', '1/2']), shown='1/12, 1/5, 1/3, 1/2', equiv_frac=False,
         q='Write these in order, smallest first: 1/3, 1/12, 1/2, 1/5. Type them with commas.',
         check=lambda: ', '.join(ftxt(f) for f in sorted([Fr(1, 3), Fr(1, 12), Fr(1, 2), Fr(1, 5)])),
         hint='Think about the same whole cut into 2, 3, 5 and 12 equal parts. Which parts are the smallest?',
         steps=['The more equal parts the whole is cut into, the smaller each part is.', 'Smallest first: 1/12, 1/5, 1/3, 1/2.'],
         src=['Write these in order, smallest first: 1/3, 1/12, 1/2, 1/5.']),
    dict(id='T2a', tier='stretch', no='Think harder 2', label='T2', type='choice', options=['Yes', 'No'], answer='No', skill='comparing fractions with bars', svg=T2,
         q='Mei says: “3/8 of a pizza is more than 3/5 of the same pizza, because 8 is bigger than 5.” Is she right?',
         check=lambda: 'Yes' if Fr(3, 8) > Fr(3, 5) else 'No',
         hint='Draw two bars of the same length: one cut into 8 equal parts, one into 5. Shade 3 parts of each and compare.',
         steps=['Eighths are smaller than fifths (the more equal parts, the smaller each part).', '3 eighths is less than 3 fifths, so 3/5 is bigger. Mei is not right.'],
         src=['Mei says: “3/8 of a pizza is more than 3/5 of the same pizza, because 8 is bigger than 5.” Is she right?']),
    dict(id='T2b', tier='stretch', no='Think harder 2 explain', label='T2 why', type='selfcheck', open=False, skill='explaining with bars', svg=T2,
         q='Mei says: “3/8 of a pizza is more than 3/5 of the same pizza, because 8 is bigger than 5.” Explain what you think about her idea, with bars of the same length. Write your idea in the box.',
         facts=dict(three_fifths_bigger=Fr(3, 5) > Fr(3, 8)), check=lambda: dict(three_fifths_bigger=Fr(3, 5) > Fr(3, 8)),
         hint='Look at the two bars. Picture 3 parts shaded on each one. Which shaded part would reach further along the bar?',
         steps=['Example: The two bars are the same length. The 3 shaded fifths reach further than the 3 shaded eighths, because fifths are bigger parts than eighths.', 'Any idea about the size of the parts is good.'],
         sol_fig=lambda facts: T2_SOL,
         src=['Is she right? Draw two bars of the same length to show.']),
    dict(id='T3a', tier='stretch', no='Think harder 3', label='T3', type='choice', options=['Yes', 'No'], answer='No', skill='adding fractions with the same bottom number',
         q='Siti says: “3/8 + 2/8 = 5/16, because 8 + 8 = 16.” Is she right?',
         check=lambda: 'Yes' if Fr(3, 8) + Fr(2, 8) == Fr(5, 16) else 'No',
         hint='Draw a bar cut into 8 equal parts. Colour 3 parts and then 2 more parts. What fraction of the bar is coloured?',
         steps=['Colour 3 eighths and then 2 more eighths: 5 parts of a bar of 8 equal parts are coloured.', 'That is 5/8, not 5/16. Siti is not right.'],
         src=['Siti says: “3/8 + 2/8 = 5/16, because 8 + 8 = 16.” Is she right?']),
    fields_frac('T3b', 'Think harder 3 answer', 'What is 3/8 + 2/8? Type the answer in the two boxes, top number first.', T3, '3/8 + 2/8 = {f1}/{f2}',
                lambda: over(Fr(3, 8) + Fr(2, 8), 8), [5, 8],
                'On a bar cut into 8 equal parts, colour 3 parts and then 2 more parts. How many parts are coloured?',
                ['3 eighths and 2 eighths make 5 eighths.', '3/8 + 2/8 = 5/8.'], ['What is the right answer, and why does the bottom number not change?'],
                label='T3 sum', tier='stretch', skill='adding fractions with the same bottom number'),
    dict(id='T3c', tier='stretch', no='Think harder 3 explain', label='T3 why', type='selfcheck', open=False, skill='explaining adding fractions',
         q='Siti says: “3/8 + 2/8 = 5/16, because 8 + 8 = 16.” Explain what you think about her idea. Write your idea in the box.',
         facts=dict(sum=ftxt(Fr(3, 8) + Fr(2, 8))), check=lambda: dict(sum=ftxt(Fr(3, 8) + Fr(2, 8))),
         hint='What are the parts called? Does the name of the parts change when you add more of them?',
         steps=['Example: 3 eighths and 2 eighths make 5 eighths, like 3 apples and 2 apples make 5 apples. The parts are still eighths, so the bottom number does not change.', 'Adding the bottom numbers would change the size of the parts.'],
         src=['What is the right answer, and why does the bottom number not change?']),
    dict(id='T4a', tier='stretch', no='Think harder 4', label='T4', type='choice', options=['Yes', 'No'], answer='Yes', skill='the whole must be the same size',
         q='Ali says: “Half of my pizza is bigger than half of your pizza.” Can he be right?',
         check=lambda: 'Yes' if any(Fr(1, 2) * a > Fr(1, 2) * b for a in range(1, 6) for b in range(1, 6)) else 'No',
         hint='Think about the two pizzas. Do they have to be the same size?',
         steps=['If Ali’s pizza is bigger than your pizza, half of his is bigger than half of yours.', 'So he can be right.'],
         src=['Ali says: “Half of my pizza is bigger than half of your pizza.” Can he be right? Explain.']),
    dict(id='T4b', tier='stretch', no='Think harder 4 explain', label='T4 why', type='selfcheck', open=False, skill='explaining halves of different wholes',
         q='Ali says: “Half of my pizza is bigger than half of your pizza.” Explain what you think about his idea. Write your idea in the box.',
         facts=dict(half_of_bigger_is_bigger=True), check=lambda: dict(half_of_bigger_is_bigger=Fr(1, 2) * 12 > Fr(1, 2) * 8),
         hint='Picture a big pizza and a small pizza. Cut each one in half.',
         steps=['Example: If Ali’s pizza is bigger, then half of it is bigger than half of a smaller pizza. Halves of different-size wholes are different sizes.', 'Any idea that talks about the size of the whole is good.'],
         src=['Can he be right? Explain.']),

    # ================= Go further
    fields_frac('C5', 'Go further 5', 'A cake is cut into 12 equal pieces. Mei gets 4/12. Ali and Ben share the rest, but Ali gets 2/12 more than Ben. What fraction does Ben get? Type it, top number first.', STRIP12,
                'Ben gets {f1}/{f2} of the cake',
                lambda: (lambda b: [b, 12])(next(b for b in range(0, 13) if 4 + b + (b + 2) == 12)), [3, 12],
                'First find how many pieces Ali and Ben share. Then take away the extra 2 pieces that Ali has. What is left to share equally?',
                ['Mei has 4 pieces, so Ali and Ben share 12 − 4 = 8 pieces.', 'Take away Ali’s 2 extra pieces: 6 pieces are left, shared equally, so Ben gets 3 pieces and Ali gets 3 + 2 = 5 pieces.', 'Ben gets 3/12. Check: 4 + 3 + 5 = 12 pieces.'],
                ['A cake is cut into 12 equal pieces. Mei gets 4/12.', 'What fraction does Ben get?'], label='G5', tier='challenge', skill='fair-sharing with bars'),
    dict(id='C6a', tier='challenge', no='Go further 6 smallest', label='G6 least', type='set', ordered=True, skill='finding all the ways to share', svg=STRIP10,
         q='Three children share a cake of 10 equal pieces. Each gets a DIFFERENT number of pieces (at least 1), and all 10 are shared. Write each way as three numbers, smallest first. List the ways in order (by the smallest number, then the middle one). Type the SMALLEST number of each way.',
         answer=[1, 1, 1, 2],
         check=lambda: [w[0] for w in sorted(w for w in itertools.product(range(1, 10), repeat=3) if w[0] < w[1] < w[2] and sum(w) == 10)],
         hint='Start with the child who gets 1 piece. How many pieces are left for the other two, and in how many ways can you split those left over between two children with different numbers?',
         steps=['The ways, smallest first and in order: 1, 2, 7; 1, 3, 6; 1, 4, 5; 2, 3, 5.', 'The smallest number of each way is 1, 1, 1, 2.'],
         src=['Three children share a cake cut into 10 equal pieces. Each child gets a DIFFERENT number of pieces (at least 1), and the whole cake is shared out.']),
    dict(id='C6b', tier='challenge', no='Go further 6 middle', label='G6 middle', type='set', ordered=True, skill='finding all the ways to share', svg=STRIP10,
         q='Same cake and same ways as before: three different numbers of pieces that make 10, smallest first, ways listed in order. Type the MIDDLE number of each way.',
         answer=[2, 3, 4, 3],
         check=lambda: [w[1] for w in sorted(w for w in itertools.product(range(1, 10), repeat=3) if w[0] < w[1] < w[2] and sum(w) == 10)],
         hint='Write each way out in full first, with the three numbers of pieces, then pick out the middle one of each way.',
         steps=['The ways are 1, 2, 7; 1, 3, 6; 1, 4, 5; 2, 3, 5.', 'The middle numbers are 2, 3, 4, 3.'],
         src=['Find ALL the ways to share it. Write each child’s share as a fraction.']),
    dict(id='C6c', tier='challenge', no='Go further 6 biggest', label='G6 most', type='set', ordered=True, skill='finding all the ways to share', svg=STRIP10,
         q='Same cake and same ways as before: three different numbers of pieces that make 10, smallest first, ways listed in order. Type the BIGGEST number of each way.',
         answer=[7, 6, 5, 5],
         check=lambda: [w[2] for w in sorted(w for w in itertools.product(range(1, 10), repeat=3) if w[0] < w[1] < w[2] and sum(w) == 10)],
         hint='Write each way out in full first, then pick out the biggest number of each way. Check that the three numbers of each way add up to 10.',
         steps=['The ways are 1, 2, 7; 1, 3, 6; 1, 4, 5; 2, 3, 5.', 'The biggest numbers are 7, 6, 5, 5. As fractions, the first way is 1/10, 2/10 and 7/10.'],
         src=['Find ALL the ways to share it. Write each child’s share as a fraction.']),
    dict(id='C7', tier='challenge', no='Go further 7', label='G7', type='set', ordered=False, skill='unit fractions between two fractions',
         q='I am a fraction with 1 on top. I am smaller than 1/4 but bigger than 1/7. Type the bottom number of each fraction I could be.',
         answer=[5, 6],
         check=lambda: [d for d in range(2, 60) if Fr(1, 7) < Fr(1, d) < Fr(1, 4)],
         hint='Try 1/5, 1/6 and so on. Compare each one with 1/4 and with 1/7: more equal parts means smaller parts.',
         steps=['Fractions with 1 on top get smaller as the bottom number gets bigger. 1/4 is too big, and 1/7 is too small.', '1/5 and 1/6 are in between, so the bottom numbers are 5 and 6.'],
         src=['I am a fraction with 1 on top. I am smaller than 1/4 but bigger than 1/7. What could I be? Find all the answers.']),
    dict(id='M', tier='challenge', no='Make up your own', label='Make', type='selfcheck', open=True, skill='making puzzles', marking_mode='open',
         q='Make up a fair-sharing story about a cake cut into 8 equal pieces and shared by 3 children. Write each share as a fraction.',
         hint='Decide how many pieces each child gets. Do the pieces add up to 8? Write each share as a fraction of 8 pieces.',
         steps=['Many answers are right. Example: Ali eats 3 pieces, Mei eats 3 pieces and Ben eats 2 pieces: 3/8, 3/8 and 2/8.', 'Check: 3 + 3 + 2 = 8 pieces, so the cake is all shared out: 8/8 = 1 whole.'],
         src=['a fair-sharing story about a cake cut into 8 equal pieces and shared by 3 children. Write each share as a fraction.']),
]
for _d in ITEMS:
    _d.setdefault('strand', STRAND)
    if _d['type'] == 'selfcheck':
        _d.setdefault('marking_mode', 'self')


# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
def _frac_parts(f):
    f = Fr(f)
    return dict(f1=f.numerator, f2=f.denominator)


VARIANTS = {
    '2a': dict(
        base=dict(n=8, k=3),
        tpl=dict(vars=dict(n=[6, 8, 10, 12], k=[2, 3, 4, 5]), answers=dict(f1='k', f2='n', f3='n-k', f4='n'), frame='Shaded: {f1}/{f2}      Not shaded: {f3}/{f4}',
                 q='A bar is cut into {n} equal parts and {k} parts are shaded. What fraction is shaded? What fraction is NOT shaded? Type each fraction, top number first.',
                 hint='The bottom number is how many equal parts there are in all. The top number is how many parts you take.',
                 steps=['The bar has {n} equal parts, so the bottom number is {n}. {k} parts are shaded: {k}/{n}.', '{n} − {k} parts are not shaded: the rest of the parts.']),
        fig=lambda e: frac_bar(e['n'], list(range(e['k']))),
        oracle=lambda e: (lambda s, n: dict(f1=s, f2=n, f3=n - s, f4=n))(*count_parts(frac_bar(e['n'], list(range(e['k'])))))),
    '4a': dict(
        base=dict(d=5, a=2, b=1),
        tpl=dict(vars=dict(d=[8, 9, 10, 12], a=[2, 3], b=[2, 3, 4]), derive=dict(s='a+b'), answers=dict(f1='a+b', f2='d'), frame='{a}/{d} + {b}/{d} = {f1}/{f2}',
                 q='Add: {a}/{d} + {b}/{d}. Type the answer in the two boxes, top number first.',
                 hint='Think of a bar cut into {d} equal parts. Colour {a} parts and then {b} more. How many are coloured?',
                 steps=['{a} parts and {b} more parts of the same size: {a} + {b} = {s} parts.', 'The parts are still the same size, so the bottom number stays {d}: the answer is {s}/{d}.']),
        fig=lambda e: frac_bar(e['d'], []),
        oracle=lambda e: dict(zip(('f1', 'f2'), over(Fr(e['a'], e['d']) + Fr(e['b'], e['d']), e['d'])))),
    '4e': dict(
        base=dict(d=10, a=7, b=3),
        tpl=dict(vars=dict(d=[10, 12], a=[7, 8, 9], b=[2, 3, 4]), derive=dict(s='a-b'), answers=dict(f1='a-b', f2='d'), frame='{a}/{d} − {b}/{d} = {f1}/{f2}',
                 q='Take away: {a}/{d} − {b}/{d}. Type the answer in the two boxes, top number first.',
                 hint='Think of a bar cut into {d} equal parts. Colour {a} parts, then take away {b} of them. How many are still coloured?',
                 steps=['{a} parts take away {b} parts of the same size: {a} − {b} = {s} parts.', 'The parts are still the same size, so the bottom number stays {d}: the answer is {s}/{d}.']),
        fig=lambda e: frac_bar(e['d'], []),
        oracle=lambda e: dict(zip(('f1', 'f2'), over(Fr(e['a'], e['d']) - Fr(e['b'], e['d']), e['d'])))),
    '5a': dict(
        base=dict(n=8, a=2, b=3),
        tpl=dict(vars=dict(n=[8, 10, 12], a=[2, 3], b=[2, 3, 4]), derive=dict(s='a+b'), answers=dict(f1='a+b', f2='n'), frame='{f1}/{f2} of the cake',
                 q='Mum cuts a cake into {n} equal slices. Ali eats {a} slices. Mei eats {b} slices. What fraction of the cake do they eat altogether?',
                 hint='The slices are all the same size. How many slices do they eat in all? What is each slice called?',
                 steps=['Ali eats {a} slices and Mei eats {b} slices: {a} + {b} = {s} slices in all.', 'They eat {s}/{n} of the cake.']),
        fig=lambda e: frac_bar(e['n'], [], 'Cake'),
        oracle=lambda e: dict(zip(('f1', 'f2'), over(Fr(e['a'], e['n']) + Fr(e['b'], e['n']), e['n'])))),
    'C5': dict(
        base=dict(t=12, m=4, e=2),
        tpl=dict(vars=dict(t=[12, 14, 16], m=[2, 4, 6], e=[2, 4]), derive=dict(r='t-m', u='t-m-e', b='(t-m-e)/2'), answers=dict(f1='(t-m-e)/2', f2='t'), frame='Ben gets {f1}/{f2} of the cake',
                 q='A cake is cut into {t} equal pieces. Mei gets {m}/{t}. Ali and Ben share the rest, but Ali gets {e}/{t} more than Ben. What fraction does Ben get? Type it, top number first.',
                 hint='First find how many pieces Ali and Ben share. Then take away the extra {e} pieces that Ali has. What is left to share equally?',
                 steps=['Ali and Ben share {t} − {m} = {r} pieces. Take away Ali’s {e} extra pieces: {u} pieces are left, shared equally, so Ben gets {b} pieces.', 'Ben gets {b}/{t}.']),
        fig=lambda e: frac_bar(e['t'], []),
        oracle=lambda e: dict(f1=next(b for b in range(0, e['t'] + 1) if e['m'] + b + (b + e['e']) == e['t']), f2=e['t'])),
}
