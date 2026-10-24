"""Online practice for Level 3 (Primary 3, ages 8-10) holiday lesson 2: Cryptarithm Crackers (Addition and Subtraction).

The questions are the ones printed in the Level 3 holiday workbook (p3/workbook_html.js builds it from p3/content/l2.js: Start here = the lesson's
workbook pages; Think harder 1 to 4 and Go further 5 to 7 = qbank stretch[0..3] and challenge[-3:]; the Take-home pair = deck.takeHome; the
Investigation = p3/gifted.json lesson 2).  Every answer is recomputed by an INDEPENDENT checker below (loops over digits and numbers, never a
copy of the printed answer); build_holiday.py stops if a checker and the printed answer differ.  The figures are the workbook's own.
"""
import itertools, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *      # noqa: E402,F401
from p3lib import *     # noqa: E402,F401

META = dict(level=3, lesson=2, key='p3', title='Cryptarithm Crackers', workbook_title='CRYPTARITHM CRACKERS', topic='Addition and Subtraction', strand='Addition and subtraction',
            sources=['p3/content/l2.js', 'p3/gifted.json'],
            intro=['Work one column at a time, starting with the ones. Remember the carried 1!',
                   'You do not need the cut-out digit cards: the cards are drawn on the screen. Use paper for workings, then type the answers here.',
                   'Each letter in a letter puzzle is one digit. Different letters are different digits.'])
FIG = figs()
SK = 'Addition and subtraction'


def I(**kw):
    kw.setdefault('strand', SK)
    return kw


def one(solutions):
    """The only solution, or None if there are none or several (a puzzle must have exactly one answer)."""
    return solutions[0] if len(solutions) == 1 else None


def six_split():
    """All ways to use the cards 1 to 6 once each to make two 3-digit numbers: (first, second)."""
    out = []
    for p in itertools.permutations([1, 2, 3, 4, 5, 6]):
        out.append((p[0] * 100 + p[1] * 10 + p[2], p[3] * 100 + p[4] * 10 + p[5]))
    return out


def eight_split():
    out = []
    for p in itertools.permutations(range(1, 9)):
        out.append((int(''.join(map(str, p[:4]))), int(''.join(map(str, p[4:])))))
    return out


def magic_solve(top, mid_c):
    """3 x 3 magic square with top row `top`, centre mid_c: find (ml, mr, bl, bm, br) by testing every line (all rows, columns and diagonals equal)."""
    t = sum(top)
    sols = []
    for bl in range(0, 4001, 100):
        for br in range(0, 4001, 100):
            bm = t - bl - br
            ml = t - top[0] - bl        # column 1
            mr = t - top[2] - br        # column 3
            g = [top, [ml, mid_c, mr], [bl, bm, br]]
            lines = [sum(r) for r in g] + [sum(g[r][c] for r in range(3)) for c in range(3)] + [g[0][0] + g[1][1] + g[2][2], g[0][2] + g[1][1] + g[2][0]]
            if all(x == t for x in lines):
                sols.append([ml, mr, bl, bm, br])
    return sols


def pyr_a():
    """(a) top 5975, middle right 3600, bottom left 1250: find middle left, bottom middle, bottom right so that every brick is the sum of the two under it."""
    out = []
    for ml in range(0, 6001):
        if ml + 3600 != 5975:
            continue
        for bm in range(0, 6001):
            if 1250 + bm != ml:
                continue
            for br in range(0, 6001):
                if bm + br == 3600:
                    out.append([ml, bm, br])
    return out


def pyr_b():
    """(b) top 7000, bottom middle 2000, equal corner bricks: bottom row x, 2000, x; middle row x + 2000 twice."""
    out = []
    for x in range(0, 7001):
        ml, mr = x + 2000, 2000 + x
        if ml + mr == 7000:
            out.append([x, x, ml, mr])
    return out


def pyr_t3():
    out = []
    for bm in range(0, 6001):
        if 1200 + bm != 2650:
            continue
        for br in range(0, 6001):
            mr = bm + br
            if 2650 + mr == 6000:
                out.append([bm, br, mr])
    return out


def reverse_diff(n):
    r = int(str(n)[::-1])
    return abs(n - r)


R3 = [n for n in range(100, 1000) if int(str(n)[0]) > int(str(n)[2])]
SOL_MAGIC = magic_solve([1200, 1700, 1600], 1500)

ITEMS = [
    # ================= Start here (workbook lesson 2, No.1 to No.6)
    I(id='1a', tier='core', no='1(a)', type='fields', skill='missing digits in an addition', answer=[4, 7, 6], svg=FIG['l2_q1'], frame='3 {f1} 4 7  +  2 5 {f2} 8  =  {f3} 0 2 5',
      q='Find the missing digits. Write them in the boxes. Example: 3_2 + 115 = 467. Ones: 2 + 5 = 7. Tens: _ + 1 = 6, so the missing digit is 5. Now (a): find the three missing digits.',
      check=lambda: one([[a, b, c] for a in range(10) for b in range(10) for c in range(10) if 3000 + a * 100 + 47 + 2500 + b * 10 + 8 == c * 1000 + 25]),
      sol_fig=lambda got: FIG['l2_q1_sol'],
      hint='Start with the ones: 7 + 8 = 15, write 5 and carry 1. Then the tens, the hundreds and the thousands. Remember the carried 1!',
      steps=['Ones: 7 + 8 = 15. Write 5 and carry 1.', 'Tens: 4 + the missing digit + the carried 1 must end in 2. 4 + 7 + 1 = 12, so the second box is 7. Write 2 and carry 1.', 'Hundreds: the missing digit + 5 + the carried 1 must end in 0. 4 + 5 + 1 = 10, so the first box is 4. Write 0 and carry 1.', 'Thousands: 3 + 2 + 1 = 6, so the third box is 6.', '3447 + 2578 = 6025. The missing digits, in the order of the boxes, are 4, 7 and 6.'],
      src=['Find the missing digits. Write them in the boxes. Example:  3 __ 2 + 115 = 467.  Ones: 2 + 5 = 7.  Tens: __ + 1 = 6, so the missing digit is 5.']),
    I(id='1b', tier='core', no='1(b)', type='number', skill='missing digits in a subtraction', answer=3, svg=FIG['l2_q1'],
      q='Find the missing digit in (b): 5_2 - 216 = 316. Type the missing digit.',
      check=lambda: one([d for d in range(10) if 500 + d * 10 + 2 - 216 == 316]),
      hint='Turn it round and add. The answer plus the number taken away makes the first number: 316 + 216.',
      steps=['Turn it round: 316 + 216 = 5_2.', 'Ones: 6 + 6 = 12. Write 2 and carry 1. Tens: 1 + 1 + 1 = 3. Hundreds: 3 + 2 = 5.', 'So the number is 532, and the missing digit is 3. Check: 532 - 216 = 316.'],
      src=['Hint for (b): turn it round and add. The answer plus the number taken away makes the first number.']),
    I(id='1c', tier='core', no='1(c)', type='number', skill='checking subtraction by adding', answer=532,
      q='Hint for (b): turn it round and add. The answer plus the number taken away makes the first number. Check (b) by adding: 316 + 216 = ____',
      check=lambda: 316 + 216,
      hint='Add the ones first: 6 + 6. Carry the 1.',
      steps=['Ones: 6 + 6 = 12. Write 2 and carry 1.', 'Tens: 1 + 1 + 1 = 3. Hundreds: 3 + 2 = 5.', '316 + 216 = 532. It is the first number in (b), so the subtraction is right.'],
      src=['Check (b) by adding: 316  +  216  =  ________']),

    I(id='2a', tier='core', no='2(a)', type='number', skill='guess, check and improve', answer=1173, svg=FIG['l2_cards'],
      q='Use the digit cards 1 to 6, each once, to make two 3-digit numbers. Make the sum as GREAT as possible. Work it out on paper, then type the sum.',
      check=lambda: max(a + b for a, b in six_split()),
      hint='Put the biggest cards in the hundreds places. Then the next biggest in the tens places.',
      steps=['For a great sum, the biggest digits go in the biggest places: 6 and 5 in the hundreds, 4 and 3 in the tens, 2 and 1 in the ones.', 'For example 642 + 531 = 1173 (or 641 + 532, 632 + 541 ...). The sum is always 1173.', 'The greatest sum is 1173.'],
      src=['Use the digit cards 1 to 6, each once, to make two 3-digit numbers.', 'Make the sum as GREAT as possible.']),
    I(id='2b', tier='core', no='2(b)', type='number', skill='guess, check and improve', answer=381, svg=FIG['l2_cards'],
      q='Use the digit cards 1 to 6, each once, to make two 3-digit numbers. Make the sum as SMALL as possible. Work it out on paper, then type the sum.',
      check=lambda: min(a + b for a, b in six_split()),
      hint='Put the smallest cards in the hundreds places. Then the next smallest in the tens places.',
      steps=['For a small sum, the smallest digits go in the biggest places: 1 and 2 in the hundreds, 3 and 4 in the tens, 5 and 6 in the ones.', 'For example 135 + 246 = 381 (or 136 + 245 ...). The sum is always 381.', 'The smallest sum is 381.'],
      src=['Make the sum as SMALL as possible.']),
    I(id='2c', tier='core', no='2(c)', type='number', skill='guess, check and improve', answer=47, svg=FIG['l2_cards'],
      q='Take-home (not for the lesson). Use the digit cards 1 to 6, each once, to make two 3-digit numbers. Make the DIFFERENCE as small as possible. Guess, check, then improve. Type the smallest difference you find.',
      check=lambda: min(abs(a - b) for a, b in six_split() if a != b),
      hint='The hundreds digits should be next to each other, like 4 and 3. Then make the bigger number as small as you can and the smaller number as big as you can.',
      steps=['Hundreds digits next to each other: 4 and 3. Make the number that starts with 4 as small as possible (412) and the number that starts with 3 as big as possible (365).', '412 - 365 = 47.', 'The smallest difference is 47. Other tries, such as 413 - 265 = 148, are bigger.'],
      src=['Make the DIFFERENCE as small as possible. Guess, check, then improve. Write your tries.']),

    I(id='3a-total', tier='core', no='3(a)', type='number', skill='magic squares', answer=4500, svg=FIG['l2_magic'],
      q='Magic square: every row, column and diagonal adds up to the same total. What is the magic total?',
      check=lambda: sum([1200, 1700, 1600]),
      hint='Find a full line (a row with all three numbers). Add it up.',
      steps=['The top row is full: 1200 + 1700 + 1600.', '1200 + 1700 = 2900 and 2900 + 1600 = 4500.', 'The magic total is 4500.'],
      src=['Magic square: every row, column and diagonal adds up to the same total.', 'What is the magic total?']),
    I(id='3a-fill', tier='core', no='3(a)', type='fields', skill='magic squares', answer=[1900, 1100, 1400, 1300, 1800], svg=FIG['l2_magic'],
      frame='Middle row: {f1}, 1500, {f2}.   Bottom row: {f3}, {f4}, {f5}.',
      q='Fill in the missing numbers in the magic square. The magic total is 4500.',
      check=lambda: one(SOL_MAGIC), sol_fig=lambda got: FIG['l2_magic_sol'],
      hint='Use a line with only one missing number. Total 4500 minus the two numbers you know.',
      steps=['The diagonal 1200, 1500, ? gives the bottom right: 4500 - 1200 - 1500 = 1800.', 'The other diagonal 1600, 1500, ? gives the bottom left: 4500 - 1600 - 1500 = 1400. The middle column 1700, 1500, ? gives the bottom middle: 4500 - 1700 - 1500 = 1300.', 'Left column: 1200 + ? + 1400 = 4500, so the middle left is 1900. Right column: 1600 + ? + 1800 = 4500, so the middle right is 1100.', 'Middle row: 1900, 1500, 1100. Bottom row: 1400, 1300, 1800.'],
      src=['Fill in the missing numbers.', 'Magic square: every row, column and diagonal adds up to the same total.']),
    I(id='3b', tier='core', no='3(b)', type='selfcheck', open=True, skill='magic squares', svg=FIG['l2_magic_sol'],
      q='Look at two numbers opposite each other across the centre. What do you notice? Write your idea, then compare with the answer shown.',
      check=lambda: sorted({a + b for a, b in [(1200, 1800), (1700, 1300), (1600, 1400), (1900, 1100)]}),
      hint='Add 1200 and 1800. Add 1700 and 1300. Add 1600 and 1400. What do you see?',
      steps=['1200 + 1800 = 3000, 1700 + 1300 = 3000, 1600 + 1400 = 3000, and 1900 + 1100 = 3000.', 'Two numbers opposite each other across the centre always add up to 3000.', 'That is double the centre number: 1500 + 1500 = 3000.'],
      src=['Look at two numbers opposite each other across the centre. What do you notice?']),

    I(id='4a', tier='core', no='4(a)', type='fields', skill='number pyramids', answer=[2375, 1125, 2475], svg=FIG['l2_pyr'], frame='(a) Middle row: {f1}, 3600.   Bottom row: 1250, {f2}, {f3}.',
      q='Number pyramids: each brick is the sum of the two bricks under it. Work backwards. Fill in the missing bricks of pyramid (a).',
      check=lambda: one(pyr_a()), sol_fig=lambda got: FIG['l2_pyr_sol'],
      hint='The top brick is the sum of the two middle bricks. So the left middle brick is 5975 - 3600.',
      steps=['Top = left middle + right middle, so left middle = 5975 - 3600 = 2375.', 'Left middle = 1250 + bottom middle, so the bottom middle = 2375 - 1250 = 1125.', 'Right middle = bottom middle + bottom right, so the bottom right = 3600 - 1125 = 2475.'],
      src=['Number pyramids: each brick is the sum of the two bricks under it. Work backwards.']),
    I(id='4b', tier='core', no='4(b)', type='fields', skill='number pyramids', answer=[1500, 1500, 3500, 3500], svg=FIG['l2_pyr'], frame='(b) Bottom row: {f1}, 2000, {f2}.   Middle row: {f3}, {f4}.',
      q='Number pyramids: each brick is the sum of the two bricks under it. Pyramid (b): the corner bricks are equal. Fill in the missing bricks.',
      check=lambda: one(pyr_b()), sol_fig=lambda got: FIG['l2_pyr_sol'],
      hint='Both corner bricks are the same number. The two middle bricks are then equal too, and together they make 7000.',
      steps=['The corner bricks are equal, so the two middle bricks are equal.', 'Together the middle bricks make 7000, so each is 7000 / 2 = 3500.', 'Middle brick 3500 = corner + 2000, so each corner brick is 3500 - 2000 = 1500.'],
      src=['(b)  corner bricks are equal']),

    I(id='5a', tier='core', no='5(a)', type='fields', skill='patterns in sums', answer=[5872, 7406], frame='4127 + {f1} = 9999    and    2593 + {f2} = 9999',
      q='Look for a pattern. Find the missing numbers.', check=lambda: [[v for v in range(10000) if 4127 + v == 9999][0], [v for v in range(10000) if 2593 + v == 9999][0]],
      hint='What do you add to 4127 to make 9999? Think of each digit: what do you add to 4 to make 9?',
      steps=['Make 9 in each place. 4 + 5 = 9, 1 + 8 = 9, 2 + 7 = 9, 7 + 2 = 9, so 4127 + 5872 = 9999.', 'For 2593: 2 + 7 = 9, 5 + 4 = 9, 9 + 0 = 9, 3 + 6 = 9, so 2593 + 7406 = 9999.'],
      src=['Look for a pattern.', '4127 + ________ = 9999    and    2593 + ________ = 9999']),
    I(id='5b', tier='core', no='5(b)', type='selfcheck', open=True, skill='patterns in sums',
      q='4127 + 5872 = 9999 and 2593 + 7406 = 9999. What do you notice about the digits? Why is there no carrying? Write your idea, then compare with the answer shown.',
      check=lambda: [[int(a) + int(b) for a, b in zip(str(x), str(y))] for x, y in [(4127, 5872), (2593, 7406)]],
      hint='Add the two digits in each place. What is the total in every place?',
      steps=['The two digits in each place add up to 9: 4 + 5, 1 + 8, 2 + 7, 7 + 2.', 'The biggest single digit is 9. Two digits that add up to 9 never make 10, so nothing is carried.'],
      src=['What do you notice about the digits? Why is there no carrying?']),
    I(id='5c', tier='core', no='5(c)', type='number', skill='patterns in sums', answer=5873,
      q='Use your pattern: 10 000 - 4127 = ____', check=lambda: 10000 - 4127,
      hint='You know 4127 + 5872 = 9999. 10 000 is one more than 9999.',
      steps=['4127 + 5872 = 9999.', '10 000 is 1 more than 9999, so the answer is 1 more than 5872.', '5872 + 1 = 5873. Check: 4127 + 5873 = 10 000.'],
      src=['Use your pattern:   10 000 − 4127  =  ________']),

    I(id='6a', tier='core', no='6(a)', type='fields', skill='letter puzzles', answer=[5, 0, 1], frame='A = {f1}   B = {f2}   C = {f3}',
      q='(if time) Letter puzzle: AB + AB + AB = CAB. Each letter stands for a digit. Different letters are different digits. Same letter, same digit: a code puzzle. Try AB = 40: 40 + 40 + 40 = 120, which does not end in 40. Try 10, 20, 30 ... until the answer ends in the number you started with.',
      check=lambda: one([[a, b, c] for a in range(1, 10) for b in range(10) for c in range(1, 10) if len({a, b, c}) == 3 and 3 * (10 * a + b) == 100 * c + 10 * a + b]),
      hint='Try AB = 10, 20, 30, 40, 50 ... Write 3 times the number. Does the answer end in the number you started with?',
      steps=['Try AB = 40: 40 + 40 + 40 = 120. It does not end in 40.', 'Try AB = 50: 50 + 50 + 50 = 150. It ends in 50, and it has the form CAB with C = 1.', 'So A = 5, B = 0 and C = 1. Check: 50 + 50 + 50 = 150.'],
      src=['(if time) Letter puzzle:  AB + AB + AB = CAB.  Each letter stands for a digit. Different letters are different digits.', 'Try AB = 40: 40 + 40 + 40 = 120, which does not end in 40.']),

    # ================= Investigation (Investigation and look back page, No.8)
    I(id='I8-easy', tier='invest', no='Investigation 8', type='fields', skill='patterns in subtraction', answer=[594, 198], frame='953 - 359 = {f1}      351 - 153 = {f2}',
      q='Investigation: Is it always true? The reverse trick. Take a 3-digit number whose first digit is bigger than its last digit, like 842. Reverse it to make 248. Subtract the smaller from the bigger: 842 - 248 = 594. Easy first step: now try 953 and 351 (reverse it, then subtract).',
      check=lambda: [reverse_diff(953), reverse_diff(351)],
      hint='Reverse 953 to make 359. Then subtract 359 from 953. Do the same for 351 and 153.',
      steps=['953 reversed is 359. 953 - 359 = 594.', '351 reversed is 153. 351 - 153 = 198.', 'Both answers are in the 99 times table: 594 = 99 x 6 and 198 = 99 x 2.'],
      src=['Easy first step: try 842 − 248 = 594 for yourself. Then try 953 and 351 (reverse it, then subtract).', 'Take a 3-digit number whose first digit is bigger than its last digit, like 842.']),
    I(id='I8a', tier='invest', no='Investigation 8(a)', type='selfcheck', open=True, skill='patterns in subtraction',
      q='Try 4 more numbers of your own. Write each subtraction and its answer (on paper). Then compare with the examples shown.',
      check=lambda: all(n - int(str(n)[::-1]) == 99 * (int(str(n)[0]) - int(str(n)[2])) for n in R3),
      hint='Choose a 3-digit number whose first digit is bigger than its last digit. Reverse it. Subtract the smaller from the bigger.',
      steps=['Examples: 731 - 137 = 594. 962 - 269 = 693. 513 - 315 = 198. 640 - 046 = 594 (046 is just 46).', 'Your four subtractions can be different. Every correct one works the same way.'],
      src=['Try 4 more numbers of your own. Write each subtraction and its answer.']),
    I(id='I8b', tier='invest', no='Investigation 8(b)', type='selfcheck', open=True, skill='patterns in subtraction',
      q='What do you notice about all your answers? Compare with a partner. Write your idea, then compare with the answer shown.',
      check=lambda: all((n - int(str(n)[::-1])) % 99 == 0 for n in R3),
      hint='Look at your answers: 594, 693, 198 ... Count in 99s: 99, 198, 297 ...',
      steps=['Every answer is in the 99 times table: 594 = 99 x 6, 693 = 99 x 7, 198 = 99 x 2.', 'The answer is 99 times (first digit - last digit). For 842 - 248: 8 - 2 = 6 and 99 x 6 = 594.'],
      src=['What do you notice about all your answers? Compare with a partner.']),
    I(id='I8c-720', tier='invest', no='Investigation 8(c)', type='number', skill='patterns in subtraction', answer=693,
      q='Is it always true? Test it on a number that ends in 0, like 720. Reverse 720 (it becomes 027, which is just 27) and subtract the smaller from the bigger. What is the answer?',
      check=lambda: reverse_diff(720),
      hint='Subtract: 720 - 27. Start by taking away 20, then 7.',
      steps=['720 - 27 = 693.', '693 is in the 99 times table: 99 x 7 = 693, and 7 - 0 = 7.', 'So the trick still works when the number ends in 0.'],
      src=['Is it always true? Test it on a number that ends in 0, like 720, then explain why you think it works.']),
    I(id='I8c-why', tier='invest', no='Investigation 8(c) explain', type='selfcheck', open=True, skill='explaining why',
      q='Why do you think it works? Write your idea, then compare with the answer shown.',
      check=lambda: all(n - int(str(n)[::-1]) == 99 * (int(str(n)[0]) - int(str(n)[2])) for n in R3),
      hint='Look at the middle digit. Is it in the same place in both numbers?',
      steps=['The middle digit is in the same place in both numbers, so it cancels out.', 'The hundreds digit and the ones digit swap places. Each step of difference between the first and last digits adds 99 (100 - 1).', 'This is true for every 3-digit number whose first digit is bigger than its last digit (checked for all of them). Extension: when is the answer exactly 495? When the first digit is 5 more than the last digit.'],
      src=['Is it always true? Test it on a number that ends in 0, like 720, then explain why you think it works.']),

    # ================= Think harder (workbook Think harder, No.1 to No.4)
    I(id='T1', tier='stretch', no='Think harder 1', type='fields', skill='missing digits in a subtraction', answer=[0, 4, 5], frame='A = {f1}   B = {f2}   C = {f3}',
      q='Find the missing digits (each letter is one digit; turn it round and add): 7A03 - B46C = 2538',
      check=lambda: one([[a, b, c] for a in range(10) for b in range(10) for c in range(10) if 7000 + a * 100 + 3 - (b * 1000 + 460 + c) == 2538]),
      hint='Turn it round: 2538 + B46C = 7A03. Start with the ones: 8 + C ends in 3.',
      steps=['Turn it round: 2538 + B46C = 7A03.', 'Ones: 8 + C ends in 3, so C = 5 (8 + 5 = 13). Write 3, carry 1.', 'Tens: 3 + 6 + 1 = 10. Write 0, carry 1. Hundreds: 5 + 4 + 1 = 10, so A = 0, carry 1. Thousands: 2 + B + 1 = 7, so B = 4.', 'A = 0, B = 4, C = 5: 7003 - 4465 = 2538. Check: 2538 + 4465 = 7003.'],
      src=['Find the missing digits (each letter is one digit; turn it round and add):  7A03 − B46C = 2538']),
    I(id='T2', tier='stretch', no='Think harder 2', type='fields', skill='missing digits in an addition', answer=[3, 1, 3, 2], frame='A = {f1}   B = {f2}   C = {f3}   D = {f4}',
      q='Find the missing digits (each letter is one digit): 2A7B + C6D9 = 6000',
      check=lambda: one([[a, b, c, d] for a in range(10) for b in range(10) for c in range(10) for d in range(10) if 2000 + a * 100 + 70 + b + c * 1000 + 600 + d * 10 + 9 == 6000]),
      hint='Ones: B + 9 must end in 0. Start there and carry.',
      steps=['Ones: B + 9 ends in 0, so B = 1 (1 + 9 = 10). Write 0, carry 1.', 'Tens: 7 + D + 1 must end in 0, so D = 2 (7 + 2 + 1 = 10). Write 0, carry 1.', 'Hundreds: A + 6 + 1 must end in 0, so A = 3 (3 + 6 + 1 = 10). Write 0, carry 1.', 'Thousands: 2 + C + 1 = 6, so C = 3.', 'A = 3, B = 1, C = 3, D = 2: 2371 + 3629 = 6000.'],
      src=['Find the missing digits (each letter is one digit):  2A7B + C6D9 = 6000']),
    I(id='T3', tier='stretch', no='Think harder 3', type='fields', skill='number pyramids', answer=[1450, 1900, 3350], svg=FIG['l2_t3'], frame='Bottom row: 1200, {f1}, {f2}.   Middle row: 2650, {f3}.',
      q='In a number pyramid, each brick is the sum of the two bricks under it. The bottom row is 1200 and two empty bricks. The middle row is 2650 and one empty brick. The top brick is 6000. Find the three empty bricks.',
      check=lambda: one(pyr_t3()), sol_fig=lambda got: FIG['l2_t3_sol'],
      hint='The top brick is the sum of the two middle bricks. Start there: 6000 - 2650.',
      steps=['Right middle brick: 6000 - 2650 = 3350.', 'Left middle brick 2650 = 1200 + bottom middle, so the bottom middle brick = 2650 - 1200 = 1450.', 'Right middle brick 3350 = 1450 + bottom right, so the bottom right brick = 3350 - 1450 = 1900.'],
      src=['In a number pyramid, each brick is the sum of the two bricks under it. The bottom row is 1200 and two empty bricks. The middle row is 2650 and one empty brick. The top brick is 6000. Find the three empty bricks.']),
    I(id='T4', tier='stretch', no='Think harder 4', type='number', skill='working backwards', answer=5643,
      q='Ali meant to add 1099 to a number, but he added 1999 by mistake and got 6543. What is the correct answer?',
      check=lambda: [n for n in range(0, 6544) if n + 1999 == 6543][0] + 1099,
      hint='Work backwards: first find the number Ali started with. Then add the right amount.',
      steps=['Ali added 1999 and got 6543, so the number he started with is 6543 - 1999 = 4544.', 'The correct answer is 4544 + 1099 = 5643.', 'Quick way: 1999 - 1099 = 900 too much was added, so 6543 - 900 = 5643.'],
      src=['Ali meant to add 1099 to a number, but he added 1999 by mistake and got 6543. What is the correct answer?']),

    # ================= Go further (workbook Go further, No.5 to No.7) and the Take-home pair
    I(id='G5', tier='challenge', no='Go further 5', type='selfcheck', open=True, skill='making up a puzzle',
      q='Make up your own missing-digits sum. Write a 4-digit + 4-digit addition that works, then rub out exactly 3 digits in 3 DIFFERENT columns and write the letters A, B and C instead. Swap with a partner. Does your partner find only one answer? Explain why your sum has only one answer. Do this on paper, then compare with the example shown.',
      check=lambda: [(a, b, c) for a in range(10) for b in range(10) for c in range(10) if (a * 1000 + 517) + (2000 + b * 100 + 86) == 6000 + c * 10 + 3],
      hint='Write a true sum first, for example 3517 + 2486 = 6003. Then rub out three digits, one from each of three different columns, and swap letters in.',
      steps=['Answers vary. Check that the sum is true and that the letters are in different columns, so that each column fixes one digit.', 'Example: 3517 + 2486 = 6003, rubbed out to A517 + 2B86 = 60C3. The only answer is A = 3, B = 4, C = 0.', 'Why only one answer: each column holds one letter, so working from the ones column, each letter is fixed by its column. Three letters in the same column, or a letter that can be anything, would give many answers.'],
      src=['Make up your own missing-digits sum. Write a 4-digit + 4-digit addition that works, then rub out exactly 3 digits in 3 DIFFERENT columns and write the letters A, B and C instead. Swap with a partner. Does your partner find only one answer? Explain why your sum has only one answer.']),
    I(id='G6', tier='challenge', no='Go further 6', type='number', skill='guess, check and improve', answer=247,
      q='Use the digit cards 1 to 8 once each to make two 4-digit numbers. Make their difference as small as possible. Work it out on paper, then type the smallest difference.',
      check=lambda: min(abs(a - b) for a, b in eight_split()),
      hint='The thousands digits should be next to each other, like 5 and 4. Make the bigger number as small as you can and the smaller number as big as you can.',
      steps=['Thousands digits next to each other: 5 and 4.', 'The number that starts with 5 should be as small as possible: 5123. The number that starts with 4 should be as big as possible: 4876.', '5123 - 4876 = 247. This is the smallest difference.'],
      src=['Use the digit cards 1 to 8 once each to make two 4-digit numbers. Make their difference as small as possible.']),
    I(id='G7', tier='challenge', no='Go further 7', type='fields', skill='letter puzzles', answer=[4, 5, 9], frame='A = {f1}   B = {f2}   C = {f3}',
      q='ABC + ACB = CBA. Different letters are different digits. Find them.',
      check=lambda: one([[a, b, c] for a in range(1, 10) for b in range(10) for c in range(1, 10) if len({a, b, c}) == 3 and (100 * a + 10 * b + c) + (100 * a + 10 * c + b) == 100 * c + 10 * b + a]),
      hint='Ones: C + B ends in A. Hundreds: A + A makes C, perhaps with a carry. Try a few values for A.',
      steps=['Hundreds: A + A (and a carry) gives C, so C is about double A.', 'Try A = 4: then 4BC + 4CB = CB4. Ones: C + B ends in 4. Tens: B + C + the carry ends in B, so C + carry makes 10 or more.', 'It works for A = 4, B = 5, C = 9: 459 + 495 = 954. It is the only answer.'],
      src=['ABC + ACB = CBA. Different letters are different digits. Find them.']),
    I(id='TH-a', tier='challenge', no='Take-home (a)', type='number', skill='mental subtraction', answer=5500,
      q='Take-home (not for the lesson). 8000 - 2500 = ?', check=lambda: 8000 - 2500,
      hint='Take away 2000 first, then 500.',
      steps=['8000 - 2000 = 6000.', '6000 - 500 = 5500.'],
      src=['8000 − 2500 = ?']),
    I(id='TH-b', tier='challenge', no='Take-home (b)', type='number', skill='mental addition', answer=5001,
      q='Take-home (not for the lesson). 4999 + 2 = ?', check=lambda: 4999 + 2,
      hint='4999 is 1 less than 5000.',
      steps=['4999 + 1 = 5000.', '5000 + 1 = 5001.'],
      src=['4999 + 2 = ?']),
]


# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
def _missing(a, total=9999):
    return [v for v in range(total + 1) if a + v == total][0]


def _since(a, b):
    n, c = b, 0
    while n < a:
        n += 1; c += 1
    return c


VARIANTS = {
    '5a': dict(
        base=dict(a=4127, b=2593),
        tpl=dict(vars=dict(a=[4127, 2593, 3086, 1904, 7650], b=[2593, 5001, 8888, 1234, 6070]), q='Look for a pattern. Find the missing numbers.',
                 frame='{a} + {f1} = 9999    and    {b} + {f2} = 9999', answers=dict(f1='9999-a', f2='9999-b'),
                 hint='What do you add to {a} to make 9999? Think of each digit: what do you add to each digit to make 9?',
                 steps=['Make 9 in each place: the missing number has digits that add to 9 with the digits of {a}.', 'Then do the same for {b}.', 'The missing numbers are {ans}.']),
        oracle=lambda e: dict(f1=_missing(e['a']), f2=_missing(e['b']))),
    '5c': dict(
        base=dict(a=4127),
        tpl=dict(vars=dict(a=[4127, 3500, 2899, 6004, 1999, 7310]), q='Use your pattern: 10 000 - {a} = ____', answer='10000-a',
                 hint='9999 - {a} is easy: make 9 in each place. 10 000 is one more than 9999.',
                 steps=['Find 9999 - {a} by making 9 in each place.', '10 000 is 1 more than 9999, so add 1 to that answer.', 'The answer is {ans}.']),
        oracle=lambda e: _missing(e['a'], 10000)),
    'T4': dict(
        base=dict(x=1099, d=900, z=6543),
        tpl=dict(vars=dict(x=[499, 899, 1099, 1199], d=[500, 800, 900, 1000], z=[6543, 7210, 8000]),
                 q='Ali meant to add {x} to a number, but he added {y} by mistake and got {z}. What is the correct answer?',
                 derive=dict(y='x+d'), answer='z-d',
                 hint='Work backwards: first find the number Ali started with. Then add the right amount.',
                 steps=['Ali added {y} and got {z}, so the number he started with is {z} - {y}.', 'Then add {x} to that number.', 'The correct answer is {ans}. (He added {d} too much.)']),
        oracle=lambda e: [n for n in range(0, e['z'] + 1) if n + e['x'] + e['d'] == e['z']][0] + e['x']),
    'TH-a': dict(
        base=dict(a=8000, b=2500),
        tpl=dict(vars=dict(a=[8000, 6000, 9000, 5000], b=[2500, 1200, 3700, 4500]), q='{a} - {b} = ?', answer='a-b',
                 hint='Take away the thousands first, then the hundreds.', steps=['Take away {b} from {a} in two steps.', 'The answer is {ans}.']),
        oracle=lambda e: _since(e['a'], e['b'])),
}
