"""Level 2 (P2) holiday lesson 2: MISSING DIGIT MYSTERIES (Addition and subtraction within 1000), week 1, second lesson.  Online mirror of the printed workbook.

The questions are the ones printed in the Level 2 holiday workbook (p2/content/l2.js `workbook()` = Start here, p2/gaps.json lesson 2 `invest` =
Investigation, p2/content/l2.js `qbank.stretch` first four = Think harder 1 to 4, `qbank.challenge` last three = Go further 5 to 7, as built by
p2/workbook_html.js).  Every answer is recomputed by an INDEPENDENT checker (brute force over digits or numbers, never a copy of the printed answer);
build_holiday.py stops if a checker and the printed answer differ.  Figures are the printed ones (p2/workbook_body.html) or redrawn.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *          # noqa: E402,F401
from p2lib import *         # noqa: E402,F401

META = dict(level=2, lesson=2, key='p2', title='Missing digit mysteries', workbook_title='MISSING DIGIT MYSTERIES', topic='Addition and Subtraction within 1000',
            strand='Addition and subtraction within 1000', sources=['p2/content/l2.js', 'p2/gaps.json', 'p2/workbook_html.js'],
            intro=['Start at the ones column. Ask: was there a carry? Type each missing digit in its own box.',
                   'Some questions ask you to draw or explain. Draw on paper, then compare with the picture shown after you submit.'])


# ---------------------------------------------------------------- independent checkers (brute force)
def one(lst, what):
    if len(lst) != 1:
        raise ValueError(f'{what}: {len(lst)} answers, expected exactly 1')
    return lst[0]


def digit_pair(test):
    """The one pair of digits (x, y) in 0..9 for which test(x, y) is true."""
    return list(one([(x, y) for x in range(10) for y in range(10) if test(x, y)], 'digit pair'))


LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def is_magic(cells):
    return len({cells[a] + cells[b] + cells[c] for a, b, c in LINES}) == 1


def magic_total(cells):
    return one(sorted({cells[a] + cells[b] + cells[c] for a, b, c in LINES}), 'magic total')


def fill_square(given):
    """given: 9 cells, None = empty.  The one way to fill the empty cells with multiples of 10 (0 to 200) that makes a magic square."""
    empty = [i for i, v in enumerate(given) if v is None]
    sols = []
    for vals in itertools.product(range(0, 201, 10), repeat=len(empty)):
        cells = list(given)
        for i, v in zip(empty, vals):
            cells[i] = v
        if is_magic(cells):
            sols.append(cells)
    return one(sols, 'magic square')


SQ = [80, None, 60, None, 50, None, 40, None, 20]
SQ_FULL = fill_square(SQ)


def triangle_solutions(total, fixed=None):
    """All placements (top, bottom-left, bottom-right, left side, bottom side, right side) of 110..160 with every side adding to total."""
    out = magic_solutions([110, 120, 130, 140, 150, 160], total)
    if fixed:
        out = [s for s in out if all(s[i] == v for i, v in fixed.items())]
    return out


def tri_svg(sol, caption):
    return magic_triangle(corners=sol[:3], sides=sol[3:], caption=caption)


def parity(n):
    return 'odd' if n % 2 else 'even'


ODDS = [n for n in range(101, 1000, 2)]
EVENS = [n for n in range(100, 1000, 2)]


def all_sums_have(a_list, b_list, want):
    return all(parity(a + b) == want for a in a_list for b in b_list)


def take_from(total, part):
    """The number that makes `total` when added to `part` (found by search, no subtraction)."""
    return one([x for x in range(0, total + 1) if x + part == total], 'difference')


SUMS = printed_fig('Three additions with missing digits')
SUBS = printed_fig('Two subtractions with missing digits')
SQUARE = printed_fig('Magic square with 80')
TRI_A = magic_triangle((110, 120, None), (None, None, None), 'Magic triangle (a). 110 is in the top corner and 120 in the bottom left corner. The bottom right corner and the three middle circles are empty. Each side adds up to 390.')
TRI_B = magic_triangle((None, None, None), (None, None, None), 'Magic triangle (b). All six circles are empty. Each side adds up to 420.')
BARS = two_bars_model(700, 200)
sol390 = one(triangle_solutions(390, {0: 110, 1: 120}), 'triangle 390')
sol420 = min(triangle_solutions(420))

ITEMS = [
    # ================= Start here (workbook lesson 2, No.1 to No.6)
    dict(id='1a', tier='core', no='1(a)', type='fields', skill='missing digits', answer=[2, 5],
         q='Find the missing digits. Write them in the boxes.', svg=SUMS, frame='(a)  2{f1}4 + 35{f2} = 579',
         check=lambda: digit_pair(lambda x, y: (200 + 10 * x + 4) + (350 + y) == 579),
         hint='Start at the ones column: 4 + the ones box ends in 9. Then the tens column.',
         steps=['Ones: 4 + the box makes 9, so the box is 5. No carry.', 'Tens: the box + 5 makes 7, so the box is 2.', 'Hundreds: 2 + 3 = 5. This matches.', 'Check: 224 + 355 = 579.'],
         src=['Find the missing digits. Write them in the boxes.']),
    dict(id='1b', tier='core', no='1(b)', type='fields', skill='missing digits', answer=[2, 3],
         q='Find the missing digits. Write them in the boxes.', svg=SUMS, frame='(b)  46{f1} + {f2}75 = 837',
         check=lambda: digit_pair(lambda x, y: (460 + x) + (100 * y + 75) == 837),
         hint='Ones first: the ones box + 5 ends in 7. Was there a carry to the tens?',
         steps=['Ones: the box + 5 makes 7, so the box is 2. No carry.', 'Tens: 6 + 7 = 13. Write 3 and carry 1 hundred.', 'Hundreds: 4 + the box + 1 carried makes 8, so the box is 3.', 'Check: 462 + 375 = 837.'],
         src=['Find the missing digits. Write them in the boxes.']),
    dict(id='1c', tier='core', no='1(c)', type='fields', skill='missing digits', answer=[3, 5],
         q='Find the missing digits. Write them in the boxes.', svg=SUMS, frame='(c)  {f1}86 + 2{f2}9 = 645',
         check=lambda: digit_pair(lambda x, y: (100 * x + 86) + (200 + 10 * y + 9) == 645),
         hint='Ones first: 6 + 9 = 15. Write 5 and carry 1 ten.',
         steps=['Ones: 6 + 9 = 15. Write 5 and carry 1 ten.', 'Tens: 8 + the box + 1 carried ends in 4, so 8 + box + 1 = 14 and the box is 5. Carry 1 hundred.', 'Hundreds: the box + 2 + 1 carried makes 6, so the box is 3.', 'Check: 386 + 259 = 645.'],
         src=['Find the missing digits. Write them in the boxes.']),
    dict(id='1d', tier='core', no='1 (check)', type='selfcheck', open=False, skill='checking by adding',
         q='Check one of your answers by adding the full numbers: ____ + ____ = ____. Write the full sum for one of (a), (b) or (c).',
         facts=['224 + 355 = 579', '462 + 375 = 837', '386 + 259 = 645'],
         check=lambda: [f'{a} + {b} = {a + b}' for a, b in [(224, 355), (462, 375), (386, 259)] if a + b in (579, 837, 645)],
         hint='Put your digits in the boxes to make the two full numbers, then add them. Is the total the one in the question?',
         steps=['(a) 224 + 355 = 579.', '(b) 462 + 375 = 837.', '(c) 386 + 259 = 645.', 'Each total matches the number in the question, so the digits are right.'],
         src=['Check one of your answers by adding the full numbers:']),

    dict(id='2a', tier='core', no='2(a)', type='fields', skill='missing digits in subtraction', answer=[7, 5],
         q='Find the missing digits. Try a digit and check it. Check: answer + the number you took away = the number you started with.', svg=SUBS, frame='(a)  7{f1}8 - 32{f2} = 453',
         check=lambda: digit_pair(lambda x, y: (700 + 10 * x + 8) - (320 + y) == 453),
         hint='Ones: 8 take away the box leaves 3. What goes in the box?',
         steps=['Ones: 8 - the box = 3, so the box is 5.', 'Tens: the box - 2 = 5, so the box is 7.', 'Hundreds: 7 - 3 = 4. This matches.', 'Check: 453 + 325 = 778.'],
         src=['Find the missing digits. Try a digit and check it.']),
    dict(id='2b', tier='core', no='2(b)', type='fields', skill='missing digits in subtraction', answer=[4, 2],
         q='Find the missing digits. Tip: 3 - 7 cannot be done, so think 13 - 7.', svg=SUBS, frame='(b)  5{f1}3 - {f2}67 = 276',
         check=lambda: digit_pair(lambda x, y: (500 + 10 * x + 3) - (100 * y + 67) == 276),
         hint='Ones: 3 - 7 cannot be done, so borrow: 13 - 7 = 6. Then the tens box has lent 1 ten.',
         steps=['Ones: 3 - 7 cannot be done. Borrow 1 ten: 13 - 7 = 6. This matches 276.', 'Tens: the box has lent 1 ten, so it is the box - 1. Then (the box - 1) - 6 must end in 7, so we borrow again: 14 - 1 - 6 = 7, and the box is 4.', 'Hundreds: 5 - 1 (lent) - the box = 2, so the box is 2.', 'Check: 276 + 267 = 543.'],
         src=['Tip for (b): 3 − 7 cannot be done, so think 13 − 7.']),

    dict(id='3a', tier='core', no='3(a)', type='number', skill='balance equations', answer=190,
         q='The = sign means "is the same as". Fill in the box. 350 + 140 = 300 + ?', check=lambda: one([x for x in range(0, 1000) if 350 + 140 == 300 + x], 'box'),
         hint='Work out the left side first. Then ask: 300 and what make that number?',
         steps=['350 + 140 = 490.', 'Both sides must be 490, so 300 + ? = 490.', '490 - 300 = 190. The box is 190.'],
         src=['350 + 140  =  300 + ______']),
    dict(id='3b', tier='core', no='3(b)', type='number', skill='balance equations', answer=525,
         q='Fill in the box. 625 - 200 = ? - 100', check=lambda: one([x for x in range(0, 1000) if 625 - 200 == x - 100], 'box'),
         hint='Work out the left side first. The box is a number that leaves that answer when you take away 100.',
         steps=['625 - 200 = 425.', 'Both sides must be 425, so ? - 100 = 425.', '425 + 100 = 525. The box is 525.'],
         src=['625 − 200  =  ______ − 100']),
    dict(id='3c', tier='core', no='3(c)', type='number', skill='balance equations', answer=280,
         q='Fill in the box. 480 + ? = 500 + 260', check=lambda: one([x for x in range(0, 1000) if 480 + x == 500 + 260], 'box'),
         hint='Work out the right side first. 480 and what make that number?',
         steps=['500 + 260 = 760.', 'Both sides must be 760, so 480 + ? = 760.', '760 - 480 = 280. The box is 280.'],
         src=['480 + ______  =  500 + 260']),
    dict(id='3d', tier='core', no='3(d)', type='choice', skill='balance equations', options=['Yes', 'No'], answer='Yes',
         q='Ravi says 398 + 205 = 400 + 203 is true. Is he right?', check=lambda: 'Yes' if 398 + 205 == 400 + 203 else 'No',
         hint='398 is a bit less than 400. 205 is a bit more than 203. How much less and how much more?',
         steps=['398 is 2 less than 400, and 205 is 2 more than 203.', 'One number lost 2 and the other gained 2, so both sides are the same.', 'Check: 398 + 205 = 603 and 400 + 203 = 603. Yes, Ravi is right.'],
         src=['Ravi says 398 + 205 = 400 + 203 is true. Is he right?']),
    dict(id='3e', tier='core', no='3(d) explain', type='selfcheck', open=False, skill='balance equations',
         q='How do you know that 398 + 205 = 400 + 203 is true without adding?', facts=dict(less_than_400=2, more_than_203=2),
         check=lambda: dict(less_than_400=400 - 398, more_than_203=205 - 203),
         hint='Compare 398 with 400, and 205 with 203. What changed on each side?',
         steps=['398 is 2 less than 400. 205 is 2 more than 203.', 'Moving 2 from one number to the other does not change the total. So both sides are the same.'],
         src=['Explain how you know without adding.']),

    dict(id='4a', tier='core', no='4(a)', type='number', skill='magic squares', answer=150,
         q='Magic square. Every row, column and diagonal adds up to the same total. What is the magic total? (Find a line with all three numbers.)', svg=SQUARE,
         check=lambda: magic_total(SQ_FULL),
         hint='Look for a line where all three numbers are given. The diagonal 80, 50, 20 is one.',
         steps=['The diagonal 80, 50 and 20 has all three numbers.', '80 + 50 + 20 = 150.', 'The magic total is 150. (The other diagonal agrees: 60 + 50 + 40 = 150.)'],
         src=['Magic square. Every row, column and diagonal adds up to the same total.', 'What is the magic total?']),
    dict(id='4b', tier='core', no='4(b)', type='fields', skill='magic squares', answer=[10, 30, 70, 90],
         q='Magic square. Fill in the empty squares.', svg=SQUARE, frame='Top row: 80, {f1}, 60. Middle row: {f2}, 50, {f3}. Bottom row: 40, {f4}, 20.',
         check=lambda: [SQ_FULL[1], SQ_FULL[3], SQ_FULL[5], SQ_FULL[7]],
         hint='Every line adds up to 150. The top row has 80 and 60, so the middle number is 150 - 80 - 60.',
         steps=['Top row: 150 - 80 - 60 = 10.', 'Left column: 150 - 80 - 40 = 30.', 'Right column: 150 - 60 - 20 = 70.', 'Bottom row: 150 - 40 - 20 = 90.', 'Check the middle row: 30 + 50 + 70 = 150, and the middle column: 10 + 50 + 90 = 150.'],
         src=['Fill in the empty squares.']),
    dict(id='4c', tier='core', no='4(c)', type='choice', skill='magic squares', options=['Yes', 'No'], answer='Yes',
         q='Add 100 to every number of the magic square. Is it still a magic square?', check=lambda: 'Yes' if is_magic([v + 100 for v in SQ_FULL]) else 'No',
         hint='Each line has 3 numbers. How much does each line total grow by?',
         steps=['Every line has 3 numbers, and each number is 100 bigger.', 'So every line total is 300 bigger, and all the lines still match. It is still a magic square.'],
         src=['Add 100 to every number. Is it still a magic square? What is the new total? Explain.']),
    dict(id='4d', tier='core', no='4(c) total', type='number', skill='magic squares', answer=450,
         q='Add 100 to every number of the magic square. What is the new total?', check=lambda: magic_total([v + 100 for v in SQ_FULL]),
         hint='The old total was 150. Each line has 3 numbers that each grew by 100.',
         steps=['Each line has 3 numbers, each 100 bigger, so the total grows by 3 x 100 = 300.', '150 + 300 = 450. The new total is 450.'],
         src=['What is the new total?']),
    dict(id='4e', tier='core', no='4(c) explain', type='selfcheck', open=False, skill='magic squares',
         q='Explain why the magic square is still magic when you add 100 to every number.', facts=dict(old=150, new=450, grew_by=300),
         check=lambda: dict(old=magic_total(SQ_FULL), new=magic_total([v + 100 for v in SQ_FULL]), grew_by=magic_total([v + 100 for v in SQ_FULL]) - magic_total(SQ_FULL)),
         hint='Look at one line. How many numbers are in it? How much did each grow?',
         steps=['Every line has 3 numbers, and every number grew by the same amount, 100.', 'So every line total grew by 300, from 150 to 450. All lines grew by the same amount, so they still match.'],
         src=['Explain.']),

    dict(id='5a1', tier='core', no='5(a) between', type='number', skill='magic triangles', answer=160,
         q='Magic triangle. Put the numbers 110, 120, 130, 140, 150 and 160 in the circles, once each, so every side has the same total. (a) Each side adds up to 390. The numbers 110 and 120 are already in two corners. First: what goes between them?', svg=TRI_A,
         check=lambda: sol390[3], hint='A side has 3 numbers: two corners and the circle between them. 390 - 110 - 120 = ?',
         steps=['The side from 110 to 120 adds up to 390.', '390 - 110 - 120 = 160.', '160 goes between 110 and 120.'],
         src=['Each side adds up to 390. The numbers 110 and 120 are already in two corners. First: what goes between them?']),
    dict(id='5a2', tier='core', no='5(a) circles', type='fields', skill='magic triangles', answer=[130, 150, 140],
         q='Triangle (a): 110 is at the top, 120 at the bottom left, and 160 is between them. Fill in all the circles. Each side adds up to 390.', svg=TRI_A,
         frame='Empty corner (bottom right): {f1}. Between 110 and the empty corner: {f2}. Between 120 and the empty corner: {f3}.',
         check=lambda: [sol390[2], sol390[5], sol390[4]],
         hint='The numbers left are 130, 140 and 150. The corner is on two sides, so it is the smallest of the three.',
         steps=['The numbers left are 130, 140 and 150.', 'The right side is 110 + circle + corner = 390, so circle + corner = 280. The bottom is 120 + circle + corner = 390, so circle + corner = 270.', 'Try the corner 130: 150 + 130 = 280 and 140 + 130 = 270. It fits.', 'The corner is 130, the right side circle is 150 and the bottom circle is 140.'],
         src=['Then fill in all the circles.']),
    dict(id='5a3', tier='core', no='5(a) corners', type='set', ordered=False, skill='magic triangles', answer=[110, 120, 130],
         q='Magic triangle (a), each side adds up to 390. Which numbers are in the corners? Type them with a comma between.', svg=TRI_A,
         check=lambda: sorted(sol390[:3]),
         hint='You found 110, 120 and the empty corner. What is the empty corner?',
         steps=['The corners are 110, 120 and 130.'],
         src=['Which numbers are in the corners?']),
    dict(id='5b1', tier='core', no='5(b) draw', type='selfcheck', paper=True, skill='magic triangles',
         q='Magic triangle (b). Each side adds up to 420. Fill in the second triangle with the numbers 110, 120, 130, 140, 150 and 160.', svg=TRI_B,
         check=lambda: sol420,
         sol_fig=lambda f: tri_svg(f, 'One magic triangle with every side 420: corners ' + ', '.join(map(str, f[:3]))),
         hint='The three biggest numbers go in the corners, because each corner is counted on two sides.',
         steps=['The corners are counted on two sides, so the three biggest numbers, 140, 150 and 160, go in the corners.', 'Between 140 and 150 goes 420 - 140 - 150 = 130. Between 150 and 160 goes 420 - 150 - 160 = 110. Between 140 and 160 goes 420 - 140 - 160 = 120.',
                'Every side adds up to 420. Turning the triangle round or flipping it gives other correct answers.'],
         src=['Each side adds up to 420. Fill in the second triangle.']),
    dict(id='5b2', tier='core', no='5(b) corners', type='set', ordered=False, skill='magic triangles', answer=[140, 150, 160],
         q='Magic triangle (b), each side adds up to 420. Which numbers are in the corners? Type them with a comma between.', svg=TRI_B,
         check=lambda: sorted({n for s in triangle_solutions(420) for n in s[:3]}),
         hint='Which numbers are counted twice? The corners. Which numbers should they be?',
         steps=['The corners are 140, 150 and 160.'],
         src=['Which numbers are in the corners?']),

    dict(id='6', tier='core', no='6', type='set', ordered=False, skill='two numbers with a difference', answer=[250, 450],
         q='Mei thinks of two numbers. They add up to 700. One number is 200 more than the other. What are the two numbers? Type the two numbers with a comma between.', svg=BARS,
         check=lambda: one([[s, s + 200] for s in range(0, 701) if s + (s + 200) == 700], 'two numbers'),
         hint='Take the 200 off the long bar. Then the two bars are the same length. What do they add up to?',
         steps=['Take the extra 200 off the long bar. The two bars are now the same length and add up to 700 - 200 = 500.', 'Each equal bar is 500 / 2 = 250. So the short bar is 250.', 'The long bar is 250 + 200 = 450.', 'Check: 250 + 450 = 700 and 450 - 250 = 200.'],
         src=['Mei thinks of two numbers. They add up to 700. One number is 200 more than the other. What are the two numbers?']),

    # ================= Investigation: Odd or even?
    dict(id='I1', tier='invest', no='Investigation (a)', type='choice', skill='odd and even', options=['Yes', 'No'], answer='Yes',
         q='Odd or even? Ali says: "When I add two odd numbers, I always get an even number." Test Ali\'s idea with pairs of odd 3-digit numbers (for example 345 + 271). Is Ali right? Easy first step: use counters to try 3 + 5, 7 + 9 and 11 + 13.',
         check=lambda: 'Yes' if all_sums_have(ODDS, ODDS, 'even') else 'No',
         hint='Try 345 + 271, then 123 + 457. Is each answer odd or even?',
         steps=['345 + 271 = 616, which is even.', 'Other pairs also give even answers. Ali is right: odd + odd is always even.'],
         src=['Ali says: "When I add two odd numbers, I always get an even number."', 'Test Ali']),
    dict(id='I2', tier='invest', no='Investigation (a) tests', type='selfcheck', open=False, skill='odd and even',
         q='Odd or even? Test Ali\'s idea with 5 pairs of odd 3-digit numbers. Write each sum.', facts=['345 + 271 = 616', '123 + 457 = 580', '789 + 901 = 1690', '111 + 999 = 1110', '555 + 333 = 888'],
         check=lambda: [f'{a} + {b} = {a + b}' for a, b in [(345, 271), (123, 457), (789, 901), (111, 999), (555, 333)] if a % 2 and b % 2 and (a + b) % 2 == 0],
         hint='Pick any odd 3-digit numbers, such as 345, 123, 789, 111 and 555. Add each to another odd number.',
         steps=['Here are 5 pairs: 345 + 271 = 616, 123 + 457 = 580, 789 + 901 = 1690, 111 + 999 = 1110 and 555 + 333 = 888.', 'Every answer is even.', 'Any 5 pairs of odd numbers give even answers.'],
         src=['Test Ali']),
    dict(id='I3', tier='invest', no='Investigation (b) odd + even', type='choice', skill='odd and even', options=['odd', 'even'], answer='odd',
         q='Odd or even? Now test odd + even. Is the answer odd or even?', check=lambda: one(sorted({parity(a + b) for a in ODDS for b in EVENS}), 'odd + even'),
         hint='Try 345 + 270. Try 123 + 456.',
         steps=['345 + 270 = 615, which is odd.', '123 + 456 = 579, which is odd.', 'Odd + even is always odd.'],
         src=['Now test odd + even, and even + even. What do you notice?']),
    dict(id='I4', tier='invest', no='Investigation (b) even + even', type='choice', skill='odd and even', options=['odd', 'even'], answer='even',
         q='Odd or even? Now test even + even. Is the answer odd or even?', check=lambda: one(sorted({parity(a + b) for a in EVENS for b in EVENS}), 'even + even'),
         hint='Try 340 + 270. Try 124 + 456.',
         steps=['340 + 270 = 610, which is even.', '124 + 456 = 580, which is even.', 'Even + even is always even.'],
         src=['Now test odd + even, and even + even. What do you notice?']),
    dict(id='I5', tier='invest', no='Investigation (c)', type='selfcheck', open=False, skill='odd and even',
         q='Odd or even? Explain WHY odd + odd is always even, using pairs of counters or a drawing.',
         facts=dict(odd_plus_odd='even', odd_plus_even='odd', even_plus_even='even'),
         check=lambda: dict(odd_plus_odd=one(sorted({parity(a + b) for a in ODDS for b in ODDS}), 'oo'), odd_plus_even=one(sorted({parity(a + b) for a in ODDS for b in EVENS}), 'oe'),
                            even_plus_even=one(sorted({parity(a + b) for a in EVENS for b in EVENS}), 'ee')),
         hint='Put counters in pairs. An odd number has one counter left over. What happens to the two left-over counters?',
         steps=['An even number is only pairs of counters. An odd number is some pairs and 1 counter left over.', 'Two odd numbers have 2 left-over counters. Those 2 make one more pair, so nobody is left over. The answer is even.',
                'Another good reason: an odd number ends in 1, 3, 5, 7 or 9, and two of these always add to an even ones digit.'],
         src=['Explain WHY, using pairs of counters or a drawing.']),

    # ================= Think harder (workbook Think harder 1 to 4)
    dict(id='T1a', tier='stretch', no='Think harder 1', type='set', ordered=False, skill='magic triangles', answer=[140, 150, 160],
         q='A magic triangle has 3 corner circles and 3 circles in the middle of the sides. Put the numbers 110, 120, 130, 140, 150 and 160 in the circles, once each, so that every side adds up to 420. Which numbers are in the corners? Type them with a comma between.',
         check=lambda: sorted({n for s in triangle_solutions(420) for n in s[:3]}),
         hint='Each corner is counted on two sides. Which numbers should go in the corners to make the side total big?',
         steps=['The corners are 140, 150 and 160.', 'Between 140 and 150: 420 - 140 - 150 = 130. Between 150 and 160: 110. Between 160 and 140: 120.'],
         src=['A magic triangle has 3 corner circles and 3 circles in the middle of the sides.']),
    dict(id='T1b', tier='stretch', no='Think harder 1 (draw)', type='selfcheck', paper=True, skill='magic triangles',
         q='Draw the magic triangle with every side adding up to 420, using 110, 120, 130, 140, 150 and 160.', check=lambda: sol420,
         sol_fig=lambda f: tri_svg(f, 'One magic triangle with every side 420: corners ' + ', '.join(map(str, f[:3]))),
         hint='Draw a triangle with a circle at each corner and one in the middle of each side. Put the 3 biggest numbers in the corners.',
         steps=['Corners 140, 150 and 160. Between 140 and 150: 130. Between 150 and 160: 110. Between 160 and 140: 120.',
                'Each side: 140 + 130 + 150 = 420, 150 + 110 + 160 = 420, 160 + 120 + 140 = 420. Turning or flipping the triangle gives other right answers.'],
         src=['Draw the triangle.']),
    dict(id='T2', tier='stretch', no='Think harder 2', type='fields', skill='missing digits', answer=[7, 3],
         q='Find the missing digits. There are three numbers, so the carry from the ones may be more than 1.', frame='5{f1} + {f2}7 + 38 = 132',
         check=lambda: digit_pair(lambda x, y: (50 + x) + (10 * y + 7) + 38 == 132),
         hint='Ones: the box + 7 + 8 ends in 2. What can the box be? Then see how many tens you carry.',
         steps=['Ones: the first box + 7 + 8 ends in 2. 7 + 7 + 8 = 22, so the first box is 7 and we carry 2 tens.', 'Tens: 5 + the second box + 3 + 2 carried makes 13, so the second box is 3.', 'Check: 57 + 37 + 38 = 132.'],
         src=['Find the missing digits:  5[ ] + [ ]7 + 38 = 132.']),
    dict(id='T3a', tier='stretch', no='Think harder 3', type='choice', skill='checking subtraction', options=['Yes', 'No'], answer='No',
         q='Mei did 523 - 267 and wrote 266. She checked by adding 266 + 267 = 533. Was her answer right?', check=lambda: 'Yes' if 266 + 267 == 523 else 'No',
         hint='A check by adding should give the number you started with. Is 533 the same as 523?',
         steps=['The check should give back 523, but 266 + 267 = 533.', '533 is not 523, so her answer is not right.'],
         src=['Mei did 523 − 267 and wrote 266. She checked by adding 266 + 267 = 533. Was her answer right?']),
    dict(id='T3b', tier='stretch', no='Think harder 3 (right answer)', type='number', skill='checking subtraction', answer=256,
         q='Mei did 523 - 267. What is the right answer?', check=lambda: take_from(523, 267),
         hint='What do you add to 267 to make 523?',
         steps=['Ones: 3 - 7 cannot be done, so borrow: 13 - 7 = 6.', 'Tens: 2 tens lent 1 ten, so 1 ten is left. 1 - 6 cannot be done, so borrow again: 11 - 6 = 5.', 'Hundreds: 5 hundreds lent 1, so 4 - 2 = 2.', 'The answer is 256. Check: 256 + 267 = 523.'],
         src=['What is the right answer?']),
    dict(id='T3c', tier='stretch', no='Think harder 3 (mistake)', type='selfcheck', open=False, skill='checking subtraction',
         q='What mistake did Mei make in 523 - 267 = 266?', facts=dict(her_answer=266, right_answer=256, her_check=533, too_big_by=10),
         check=lambda: dict(her_answer=266, right_answer=take_from(523, 267), her_check=266 + 267, too_big_by=266 - take_from(523, 267)),
         hint='Compare her answer 266 with the right answer. Which digit is different?',
         steps=['Her answer 266 is 10 too big. The right answer is 256.', 'Only the tens digit is different: she wrote 6 but it should be 5.', 'She forgot that the tens had already lent 1 ten to the ones, so only 1 ten was left. Then she should have borrowed again from the hundreds.'],
         src=['What mistake did she make?']),
    dict(id='T4a', tier='stretch', no='Think harder 4(a)', type='choice', skill='balance equations', options=['True', 'False'], answer='True',
         q='True or false? 346 + 199 = 345 + 200', check=lambda: 'True' if 346 + 199 == 345 + 200 else 'False',
         hint='Compare the numbers: 346 and 345, 199 and 200. Which is bigger, and by how much?',
         steps=['346 is 1 more than 345, and 199 is 1 less than 200.', 'One number is 1 more and the other is 1 less, so the sides match. True.'],
         src=['(a) 346 + 199 = 345 + 200']),
    dict(id='T4b', tier='stretch', no='Think harder 4(b)', type='choice', skill='balance equations', options=['True', 'False'], answer='False',
         q='True or false? 270 + 130 = 260 + 150', check=lambda: 'True' if 270 + 130 == 260 + 150 else 'False',
         hint='Compare 270 with 260, and 130 with 150.',
         steps=['270 is 10 more than 260, but 130 is 20 less than 150.', 'The sides are 400 and 410, so they are not the same. False.'],
         src=['(b) 270 + 130 = 260 + 150']),
    dict(id='T4c', tier='stretch', no='Think harder 4(c)', type='choice', skill='balance equations', options=['True', 'False'], answer='True',
         q='True or false? 618 + 99 = 600 + 117', check=lambda: 'True' if 618 + 99 == 600 + 117 else 'False',
         hint='Compare 618 with 600, and 99 with 117.',
         steps=['618 is 18 more than 600, and 99 is 18 less than 117.', 'The sides match (both are 717). True.'],
         src=['(c) 618 + 99 = 600 + 117']),
    dict(id='T4d', tier='stretch', no='Think harder 4 (how)', type='selfcheck', open=False, skill='balance equations',
         q='Say how you know whether each is true or false, without working out both sides.', facts=dict(a=(545, 545), b=(400, 410), c=(717, 717)),
         check=lambda: dict(a=(346 + 199, 345 + 200), b=(270 + 130, 260 + 150), c=(618 + 99, 600 + 117)),
         hint='Look at how much each number changes: one number goes up, the other goes down. Do the changes cancel?',
         steps=['(a) 346 is 1 more than 345 and 199 is 1 less than 200: true.', '(b) 270 is 10 more than 260, but 130 is 20 less than 150: false (400 and 410).', '(c) 618 is 18 more than 600 and 99 is 18 less than 117: true (717 and 717).'],
         src=['Say how you know without working out both sides.']),

    # ================= Go further (workbook Go further 5 to 7, then Make up your own)
    dict(id='C5', tier='challenge', no='Go further 5', type='set', ordered=False, skill='missing digits', answer=[507, 517, 527, 537, 547, 557, 567, 577, 587, 597],
         q='Find ALL the ways to fill in the four boxes: [ ][ ]7 + 4[ ][ ] = 1000. Type the first number of each way (the one that ends in 7), with commas between.',
         check=lambda: sorted(100 * a + 10 * b + 7 for a in range(1, 10) for b in range(10) for c in range(10) for d in range(10) if (100 * a + 10 * b + 7) + (400 + 10 * c + d) == 1000),
         hint='Start at the ones: 7 + the box makes 10. Carry 1 ten. What must the tens boxes add to?',
         steps=['Ones: 7 + 3 = 10. Write 0 and carry 1 ten, so the last box is 3.', 'Tens: the two tens boxes and the 1 carried must make 10, so the two tens digits add up to 9. That can be done in 10 ways: 0 and 9, 1 and 8, ... 9 and 0.',
                'Hundreds: the box + 4 + 1 carried = 10, so the first box is 5.', 'The ways are 507 + 493, 517 + 483, 527 + 473, 537 + 463, 547 + 453, 557 + 443, 567 + 433, 577 + 423, 587 + 413 and 597 + 403. The first numbers are 507, 517, ... 597.'],
         src=['Find ALL the ways to fill in the four boxes:']),
    dict(id='C6', tier='challenge', no='Go further 6', type='fields', skill='working backwards', answer=[150, 100, 250],
         q='Box A and Box B hold 250 marbles together. Box B and Box C hold 350. Box A and Box C hold 400. How many marbles are in each box?',
         frame='Box A: {f1}   Box B: {f2}   Box C: {f3}',
         check=lambda: one([[a, b, c] for a in range(0, 401) for b in range(0, 401) for c in range(0, 401) if a + b == 250 and b + c == 350 and a + c == 400], 'boxes'),
         hint='Box B + Box C is 100 more than Box A + Box B. So Box C has how many more than Box A?',
         steps=['Box B + Box C is 100 more than Box A + Box B, so Box C has 100 more than Box A.', 'Box A and Box C together are 400. Take away the extra 100: 300 is two equal boxes, so Box A is 150.', 'Box C is 150 + 100 = 250. Box B is 250 - 150 = 100.', 'Check: 150 + 100 = 250, 100 + 250 = 350, 150 + 250 = 400.'],
         src=['Box A and Box B hold 250 marbles together. Box B and Box C hold 350. Box A and Box C hold 400.']),
    dict(id='C7', tier='challenge', no='Go further 7', type='number', skill='digit cards', answer=47,
         q='Use the digit cards 1, 2, 3, 4, 5 and 6 once each to make two 3-digit numbers. Make the difference as SMALL as possible. What is the smallest difference?',
         check=lambda: min(abs(x - y) for x, y in split_two([1, 2, 3, 4, 5, 6])),
         hint='The hundreds digits should be next to each other, like 4 and 3. Then make the bigger number as small as possible and the smaller number as big as possible.',
         steps=['Put 4 and 3 in the hundreds places (next to each other).', 'The number that starts with 4 should be as small as possible: 412. The number that starts with 3 should be as big as possible: 365.', '412 - 365 = 47. The smallest difference is 47.'],
         src=['Use the digit cards 1, 2, 3, 4, 5 and 6 once each to make two 3-digit numbers. Make the difference as SMALL as possible.']),
    dict(id='M', tier='challenge', no='Make up your own', type='selfcheck', open=False, skill='making puzzles',
         q='Make up your own: a missing-digit sum with two boxes that has only ONE answer. Swap with a partner.', facts=[(2, 5)],
         check=lambda: [(x, y) for x in range(10) for y in range(10) if (400 + 10 * x + 6) + (370 + y) == 801],
         hint='Write a sum, hide two digits in different columns, and check that only one pair of digits works.',
         steps=['Many answers are right. Here is one example: 4[ ]6 + 37[ ] = 801.', 'Ones: 6 + the second box ends in 1, so the second box is 5. Tens: the first box + 7 + 1 carried ends in 0, so the first box is 2. Only one pair works: 426 + 375 = 801.',
                'Check yours: try every digit for one box and see whether only one pair of digits fits.'],
         src=['a missing-digit sum with two boxes that has only ONE answer. Swap with a partner.']),
]

# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
VARIANTS = {
    '1a': dict(
        base=dict(h1=2, t1=2, o1=4, h2=3, t2=5, o2=5),
        tpl=dict(vars=dict(h1=[1, 2, 3], t1=[2, 5, 8], o1=[4, 6, 9], h2=[1, 2, 3], t2=[3, 5, 7], o2=[3, 5, 8]), q='Find the missing digits. Write them in the boxes.',
                 frame='{h1}{f1}{o1} + {h2}{t2}{f2} = {tot}', answers=dict(f1='t1', f2='o2'), derive=dict(tot='100*(h1+h2)+10*(t1+t2)+o1+o2'),
                 hint='Start at the ones column: {o1} + the ones box makes a number that ends in the last digit of {tot}.',
                 steps=['Ones: {o1} + the box ends in the ones digit of {tot}. Find the digit for the second box.', 'Tens: add the carry if there was one, then find the first box.', 'The missing digits are {ans}. Check by adding the full numbers.']),
        oracle=lambda e: (lambda s: dict(f1=s[0], f2=s[1]))(digit_pair(lambda x, y: (100 * e['h1'] + 10 * x + e['o1']) + (100 * e['h2'] + 10 * e['t2'] + y) ==
                                                                  (100 * e['h1'] + 10 * e['t1'] + e['o1']) + (100 * e['h2'] + 10 * e['t2'] + e['o2'])))),
    '2a': dict(
        base=dict(h1=7, t1=7, o1=8, h2=3, t2=2, o2=5),
        tpl=dict(vars=dict(h1=[6, 7, 8], t1=[4, 7, 9], o1=[2, 5, 8], h2=[2, 3], t2=[1, 2, 3], o2=[1, 5, 9]), q='Find the missing digits. Try a digit and check it.',
                 frame='{h1}{f1}{o1} - {h2}{t2}{f2} = {res}', answers=dict(f1='t1', f2='o2'), derive=dict(res='(100*h1+10*t1+o1)-(100*h2+10*t2+o2)'),
                 hint='Ones: {o1} take away the ones box leaves the ones digit of {res}. If it cannot be done, borrow.',
                 steps=['Ones: find the digit that makes the ones column work. Borrow 1 ten if the top digit is too small.', 'Tens: remember if you borrowed, then find the first box.', 'The missing digits are {ans}. Check: {res} + the number you took away = the number you started with.']),
        oracle=lambda e: (lambda s: dict(f1=s[0], f2=s[1]))(digit_pair(lambda x, y: (100 * e['h1'] + 10 * x + e['o1']) - (100 * e['h2'] + 10 * e['t2'] + y) ==
                                                                  (100 * e['h1'] + 10 * e['t1'] + e['o1']) - (100 * e['h2'] + 10 * e['t2'] + e['o2'])))),
    '3a': dict(
        base=dict(a=350, b=140, c=300),
        tpl=dict(vars=dict(a=[250, 350, 450], b=[130, 140, 160, 170], c=[100, 200, 300]), q='The = sign means "is the same as". Fill in the box. {a} + {b} = {c} + ?',
                 answer='a+b-c', hint='Work out the left side first. Then ask: {c} and what make that number?',
                 steps=['Work out {a} + {b}. Both sides must be that number.', 'The box is that number take away {c}.', 'The box is {ans}.']),
        oracle=lambda e: one([x for x in range(0, 3000) if e['a'] + e['b'] == e['c'] + x], 'box')),
    '3b': dict(
        base=dict(a=625, b=200, c=100),
        tpl=dict(vars=dict(a=[625, 740, 830, 915], b=[200, 300, 150], c=[100, 50, 20]), q='The = sign means "is the same as". Fill in the box. {a} - {b} = ? - {c}',
                 answer='a-b+c', hint='Work out the left side first. The box is a number that leaves that answer when you take away {c}.',
                 steps=['Work out {a} - {b}. Both sides must be that number.', 'The box is that number plus {c}.', 'The box is {ans}.']),
        oracle=lambda e: one([x for x in range(0, 3000) if e['a'] - e['b'] == x - e['c']], 'box')),
    '3c': dict(
        base=dict(a=480, b=500, c=260),
        tpl=dict(vars=dict(a=[480, 350, 260], b=[500, 600, 700], c=[260, 170, 330]), q='The = sign means "is the same as". Fill in the box. {a} + ? = {b} + {c}',
                 answer='b+c-a', hint='Work out the right side first. {a} and what make that number?',
                 steps=['Work out {b} + {c}. Both sides must be that number.', 'The box is that number take away {a}.', 'The box is {ans}.']),
        oracle=lambda e: one([x for x in range(0, 3000) if e['a'] + x == e['b'] + e['c']], 'box')),
    '6': dict(
        base=dict(s=700, d=200),
        tpl=dict(vars=dict(s=[500, 600, 700, 800, 900, 1000], d=[100, 200, 300]), q='Mei thinks of two numbers. They add up to {s}. One number is {d} more than the other. What are the two numbers?',
                 frame='The smaller number is {f1}. The bigger number is {f2}.', answers=dict(f1='(s-d)//2', f2='(s+d)//2'),
                 hint='Take the {d} off the long bar. Then the two bars are the same length.',
                 steps=['Take the extra {d} off the long bar. The two bars are the same length and add up to {s} - {d}.', 'Half of that is the smaller number. The bigger number is {d} more.', 'The numbers are {ans}.']),
        oracle=lambda e: (lambda p: dict(f1=p[0], f2=p[1]))(one([(x, x + e['d']) for x in range(0, e['s'] + 1) if x + (x + e['d']) == e['s']], 'pair'))),
}
