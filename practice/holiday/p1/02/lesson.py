"""Online practice for Level 1 (Primary 1, ages 6-8) holiday lesson 2: Whole Numbers: Number Bonds ("Number bond inquiry").

Questions as printed in the Level 1 holiday workbook (hp/workbook_html.js lesson 2; hp/qbank.json lesson 2 stretch/challenge for Think harder and Go further;
hp/gaps.json lesson 2 for the Investigation).  Every answer is recomputed by an independent checker (brute-force search over the numbers in the question).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from hlib import *      # noqa: E402,F401

META = dict(level=1, lesson=2, key='p1', title='Number bond inquiry', workbook_title='NUMBER BOND INQUIRY', topic='Whole Numbers: Number Bonds',
            strand='Whole numbers',
            sources=['hp/workbook_html.js', 'hp/qbank.json', 'hp/gaps.json'],
            intro=['Use counters, drawings of dots or your fingers if you like. The magic triangle is drawn for you on the screen: write the numbers on paper or keep them in your head.'])


def missing(total, known, pos):
    """The number that completes  total = known + ?  (pos 'r') or  total = ? + known  (pos 'l'), found by trying every number."""
    for x in range(0, total + 1):
        if (known + x if pos == 'r' else x + known) == total:
            return x


def balance(left, right_known, right_pos):
    """x such that left = right_known + x (the = sign means both sides are the same)."""
    total = sum(left)
    return next(x for x in range(0, 60) if right_known + x == total)


def sides_ok(arr, total):
    t, bl, br, lm, bm, rm = arr
    return t + lm + bl == total and bl + bm + br == total and t + rm + br == total


def pockets():
    return [(l, r) for l in range(1, 10) for r in range(1, 10) if l + r == 10 and l > r]


ONE_TO_SIX = range(1, 7)
TWO_TO_SEVEN = range(2, 8)
EX12 = (2, 3, 4, 7, 5, 6)      # top, bottom-left, bottom-right, left side, bottom side, right side: every side adds to 12

ITEMS = [
    # ================= Start here
    dict(id='1', tier='core', no='1', type='fields', skill='number bonds of 10', answer=[7, 4, 2, 5, 10],
         q='Number bonds of 10. Fill in the blanks.', frame='10 = 3 + {f1},   10 = {f2} + 6,   10 = 8 + {f3},   10 = {f4} + 5,   10 = 0 + {f5}',
         check=lambda: [missing(10, 3, 'r'), missing(10, 6, 'l'), missing(10, 8, 'r'), missing(10, 5, 'l'), missing(10, 0, 'r')],
         hint='Think: 3 and how many more make 10? Use ten counters, or count on from 3 to 10 on your fingers.',
         steps=['3 + 7 = 10, so the first box is 7.', '4 + 6 = 10, so the second box is 4.', '8 + 2 = 10, so the third box is 2.', '5 + 5 = 10, so the fourth box is 5.', '0 + 10 = 10, so the last box is 10.'],
         src=['Number bonds of 10. Fill in the blanks.', "['10 = 3 + ____', '10 = ____ + 6', '10 = 8 + ____', '10 = ____ + 5', '10 = 0 + ____']"]),
    dict(id='2a', tier='core', no='2(a)', type='fields', skill='all the pairs that make 10', answer=[8, 7, 6, 5],
         q='List the pairs that make 10, from the smallest first number.', frame='0 + 10,  1 + 9,  2 + {f1},  3 + {f2},  4 + {f3},  5 + {f4}',
         check=lambda: [b for a, b in pairs_sum(10) if 2 <= a <= 5],
         hint='Each time the first number goes up by 1, think about the second number. 1 + 9 comes before 2 + ?',
         steps=['2 + 8 = 10, 3 + 7 = 10, 4 + 6 = 10 and 5 + 5 = 10.', 'The boxes are 8, 7, 6 and 5.'],
         src=['List the pairs that make 10, from the smallest first number.', '0 + 10,   1 + 9,   2 + ____,   3 + ____,   4 + ____,   5 + ____']),
    dict(id='2b', tier='core', no='2(b)', type='selfcheck', open=False, skill='all the pairs that make 10',
         q='When the first number goes up by 1, what happens to the second number?', facts=-1,
         check=lambda: (lambda p: p[1][1] - p[0][1] if len({y[1] - x[1] for x, y in zip(p, p[1:])}) == 1 else None)(pairs_sum(10, ordered=True)),
         hint='Look at 0 + 10, 1 + 9, 2 + 8. What happens to the second number each time?',
         steps=['The second number goes down by 1: 10, 9, 8, 7 ...', 'The total stays 10. One number goes up by 1 and the other goes down by 1, so they cancel.'],
         src=['When the first number goes up by 1, what happens to the second number?']),
    dict(id='2c', tier='core', no='2(c)', type='number', skill='all the pairs that make 10', answer=6,
         q='How many different pairs make 10 if 3 + 7 and 7 + 3 count as the SAME pair?',
         check=lambda: len({frozenset((a, b)) for a in range(11) for b in range(11) if a + b == 10}),
         hint='Write the pairs from 0 + 10. Stop when the first number is as big as the second.',
         steps=['The pairs are 0 + 10, 1 + 9, 2 + 8, 3 + 7, 4 + 6 and 5 + 5.', 'After 5 + 5 the pairs just turn round (6 + 4 is the same pair as 4 + 6).', 'There are 6 different pairs.'],
         src=['How many different pairs make 10 if 3 + 7 and 7 + 3 count as the SAME pair?']),

    dict(id='3a', tier='core', no='3(a)', type='fields', skill='bonds of 20 from bonds of 10', answer=[20, 20],
         q='Use bonds of 10 to help you with bonds of 20.', frame='6 + 4 = 10, so  16 + 4 = {f1}   and   6 + 14 = {f2}',
         check=lambda: [sum([16, 4]), sum([6, 14])],
         hint='6 + 4 = 10. Then 16 is 10 more than 6, so 16 + 4 is 10 more than 10.',
         steps=['6 + 4 = 10. 16 is 6 and 10 more, so 16 + 4 = 10 + 10 = 20.', '14 is 4 and 10 more, so 6 + 14 = 10 + 10 = 20.'],
         src=['Use bonds of 10 to help you with bonds of 20.', '6 + 4 = 10, so  16 + 4 = ____   and   6 + 14 = ____']),
    dict(id='3b', tier='core', no='3(b)', type='fields', skill='bonds of 20 from bonds of 10', answer=[20, 20],
         q='Use bonds of 10 to help you with bonds of 20.', frame='7 + 3 = 10, so  17 + 3 = {f1}   and   7 + 13 = {f2}',
         check=lambda: [sum([17, 3]), sum([7, 13])],
         hint='7 + 3 = 10. 17 is 10 more than 7, so the answer is 10 more than 10.',
         steps=['7 + 3 = 10. 17 + 3 is 10 more, so it is 20.', '7 + 13 is also 10 more than 7 + 3, so it is 20.'],
         src=['7 + 3 = 10, so  17 + 3 = ____   and   7 + 13 = ____']),
    dict(id='3c', tier='core', no='3(c)', type='fields', skill='number bonds of 20', answer=[8, 11, 5],
         q='Use bonds of 10 to help you with bonds of 20.', frame='20 = 12 + {f1},   20 = {f2} + 9,   20 = 15 + {f3}',
         check=lambda: [missing(20, 12, 'r'), missing(20, 9, 'l'), missing(20, 15, 'r')],
         hint='From 12, count on to 20. Or: 12 + 8 = 20 because 2 + 8 = 10.',
         steps=['12 + 8 = 20, so the first box is 8.', '11 + 9 = 20, so the second box is 11.', '15 + 5 = 20, so the third box is 5.'],
         src=['20 = 12 + ____        20 = ____ + 9        20 = 15 + ____']),

    dict(id='4a', tier='core', no='4(a)', type='fields', skill='the equals sign', answer=[4],
         q='The = sign means "is the same as". Use counters or draw dots to make both sides the same. Fill in the blanks.', frame='5 + 3 = 4 + {f1}',
         check=lambda: [balance([5, 3], 4, 'r')],
         hint='5 + 3 is 8. What goes with 4 to make 8 as well?',
         steps=['5 + 3 = 8, so the right side must be 8 too.', '4 + 4 = 8, so the box is 4.'],
         src=['The = sign means “is the same as”. Use counters or draw dots to make both sides the same. Fill in the blanks.', '5 + 3 = 4 + ____']),
    dict(id='4b', tier='core', no='4(b)', type='fields', skill='the equals sign', answer=[4],
         q='The = sign means "is the same as". Use counters or draw dots to make both sides the same. Fill in the blanks.', frame='7 + {f1} = 9 + 2',
         check=lambda: [next(x for x in range(30) if 7 + x == 9 + 2)],
         hint='9 + 2 is 11. What goes with 7 to make 11?',
         steps=['9 + 2 = 11, so the left side must be 11 too.', '7 + 4 = 11, so the box is 4.'],
         src=['(b)  7 + ____ = 9 + 2']),
    dict(id='4c', tier='core', no='4(c)', type='fields', skill='the equals sign', answer=[6],
         q='The = sign means "is the same as". Use counters or draw dots to make both sides the same. Fill in the blanks.', frame='3 + 8 = {f1} + 5',
         check=lambda: [next(x for x in range(30) if x + 5 == 3 + 8)],
         hint='3 + 8 is 11. What goes with 5 to make 11?',
         steps=['3 + 8 = 11, so the right side must be 11 too.', '6 + 5 = 11, so the box is 6.'],
         src=['3 + 8 = ____ + 5']),
    dict(id='4d', tier='core', no='4(d)', type='fields', skill='the equals sign', answer=[2],
         q='The = sign means "is the same as". Use counters or draw dots to make both sides the same. Fill in the blanks.', frame='6 + 6 = 10 + {f1}',
         check=lambda: [next(x for x in range(30) if 10 + x == 6 + 6)],
         hint='6 + 6 is 12. What goes with 10 to make 12?',
         steps=['6 + 6 = 12, so the right side must be 12 too.', '10 + 2 = 12, so the box is 2.'],
         src=['(d)  6 + 6 = 10 + ____']),
    dict(id='4e', tier='core', no='4(e)', type='choice', skill='the equals sign', options=['Yes', 'No'], answer='No',
         q='Mei says "4 + 4 = 8 + 1 is true." Is she right?', check=lambda: 'Yes' if 4 + 4 == 8 + 1 else 'No',
         hint='Work out both sides. Are they the same?',
         steps=['The left side: 4 + 4 = 8.', 'The right side: 8 + 1 = 9.', '8 is not the same as 9, so Mei is not right.'],
         src=['Mei says “4 + 4 = 8 + 1 is true.” Is she right? Explain.']),
    dict(id='4e-why', tier='core', no='4(e) why', type='selfcheck', open=False, skill='the equals sign',
         q='Mei says "4 + 4 = 8 + 1 is true." Is she right? Explain.', facts=(8, 9), check=lambda: (4 + 4, 8 + 1),
         hint='Say what each side makes. Use the word "same".',
         steps=['4 + 4 makes 8, but 8 + 1 makes 9.', 'The two sides are not the same, so the = sign is wrong. It would be true if the right side were 8 + 0, or if the left side were 4 + 5.', 'Any answer that compares 8 and 9 is good.'],
         src=['Mei says “4 + 4 = 8 + 1 is true.” Is she right? Explain.']),

    dict(id='5a', tier='core', no='5(a)', type='fields', skill='magic triangle', answer=[6, 4, 5],
         q='Magic triangle. Use 1, 2, 3, 4, 5 and 6 so that each side adds up to 9. The corners are 1, 2 and 3. Which number goes between each pair of corners?',
         frame='Between 1 and 2: {f1}     Between 2 and 3: {f2}     Between 3 and 1: {f3}',
         svg=magic_triangle(corners=(1, 2, 3), caption='Magic triangle with 1, 2 and 3 in the corners and three empty circles'),
         check=lambda: (lambda m: list(m[0][3:]) if len(m) == 1 else None)([a for a in magic_solutions(ONE_TO_SIX, 9) if a[:3] == (1, 2, 3)]),
         sol_fig=lambda g: (lambda a: magic_triangle(corners=a[:3], sides=a[3:], caption='Every side adds up to 9'))(next(a for a in magic_solutions(ONE_TO_SIX, 9) if a[:3] == (1, 2, 3))),
         hint='Hint: use counters. Between 1 and 2 you need a number that makes 9 with them: 1 + 2 + ? = 9.',
         steps=['Between 1 and 2: 1 + 2 = 3, and 3 + 6 = 9, so put 6 there.', 'Between 2 and 3: 2 + 3 = 5, and 5 + 4 = 9, so put 4 there.', 'Between 3 and 1: 3 + 1 = 4, and 4 + 5 = 9, so put 5 there.', 'The numbers between the corners are 6, 4 and 5.'],
         src=['Magic triangle. Put 1, 2, 3, 4, 5 and 6 in the circles so that each side adds up to 9. Start with 1, 2 and 3 in the corners.', 'Hint: use counters. Find the number between each pair of corners.', 'Which numbers go between the corners?']),
    dict(id='5b', tier='core', no='5(b)', type='set', ordered=False, skill='magic triangle', answer=[1, 3, 5],
         q='If you have time: now make each side add up to 10. Which numbers are in the corners this time? Type them with a comma between.',
         svg=magic_triangle(caption='An empty magic triangle'),
         check=lambda: (lambda c: list(c.pop()) if len(c) == 1 else None)({tuple(sorted(a[:3])) for a in magic_solutions(ONE_TO_SIX, 10)}),
         sol_fig=lambda g: (lambda a: magic_triangle(corners=a[:3], sides=a[3:], caption='Every side adds up to 10'))(magic_solutions(ONE_TO_SIX, 10)[0]),
         hint='Use counters. Try three numbers for the corners, then find the number between each pair that makes the side 10. If a side does not work, change a corner and try again.',
         steps=['The corners are 1, 3 and 5.', 'Between 1 and 3 put 6 (1 + 6 + 3 = 10). Between 3 and 5 put 2 (3 + 2 + 5 = 10). Between 5 and 1 put 4 (5 + 4 + 1 = 10).', 'Every side adds up to 10. The corners are 1, 3 and 5.'],
         src=['If you have time: now make each side add up to 10. Which numbers are in the corners this time?']),

    dict(id='6a', tier='core', no='6(a)', type='set', ordered=False, skill='two numbers with a total and a difference', answer=[4, 6],
         q='Two numbers add up to 10. One is 2 more than the other. What are the numbers? Type them with a comma between.',
         svg=two_bars(10, 2), check=lambda: [v for a in range(11) for b in range(11) if a + b == 10 and b - a == 2 for v in (a, b)],
         sol_fig=lambda g: two_bars(10, 2, 4, 6),
         hint='If both numbers were the same, 5 + 5. Make one of them 1 smaller and the other 1 bigger.',
         steps=['Try pairs that make 10: 5 + 5, 4 + 6, 3 + 7.', '6 is 2 more than 4, and 4 + 6 = 10.', 'The numbers are 4 and 6.'],
         src=['Two numbers add up to 10. One is 2 more than the other. What are the numbers?']),
    dict(id='6b', tier='core', no='6(b)', type='set', ordered=False, skill='two numbers with a total and a difference', answer=[4, 8],
         q='If you have time: two numbers add up to 12. One is 4 more than the other. What are they? Type them with a comma between.',
         check=lambda: [v for a in range(13) for b in range(13) if a + b == 12 and b - a == 4 for v in (a, b)],
         hint='Try pairs that make 12. Which pair is 4 apart?',
         steps=['Pairs that make 12: 6 + 6, 5 + 7, 4 + 8.', '8 is 4 more than 4, and 4 + 8 = 12.', 'The numbers are 4 and 8.'],
         src=['If you have time: two numbers add up to 12. One is 4 more than the other. What are they?']),

    # ================= Investigation
    dict(id='I1', tier='invest', no='Investigation 1', type='selfcheck', open=False, skill='odd and even bonds',
         q='Investigation: Is it always true? On paper, write all the pairs that make 10, from 0 + 10 down to 10 + 0. Is each pair both odd, both even, or one of each?',
         facts=dict(pairs=11, same_kind=11),
         check=lambda: (lambda p: dict(pairs=len(p), same_kind=sum(1 for a, b in p if a % 2 == b % 2)))(pairs_sum(10, ordered=True)),
         hint='Write the pairs in a column. Write O for odd and E for even under each number.',
         steps=['The pairs are 0 + 10, 1 + 9, 2 + 8, 3 + 7, 4 + 6, 5 + 5, 6 + 4, 7 + 3, 8 + 2, 9 + 1 and 10 + 0.', '0 + 10, 2 + 8, 4 + 6, 6 + 4, 8 + 2 and 10 + 0 are both even. 1 + 9, 3 + 7, 5 + 5, 7 + 3 and 9 + 1 are both odd.',
                'No pair has one odd and one even number. All 11 pairs are both odd or both even.'],
         src=['Write all the pairs that make 10, from 0 + 10 and 1 + 9 down to 10 + 0. Look at each pair. Are both numbers odd, both even, or one of each?']),
    dict(id='I2a', tier='invest', no='Investigation 2', type='choice', skill='odd and even bonds', options=['Yes', 'No'], answer='Yes',
         q='Then: Mei says "When two numbers make 10, they are both odd or both even." Is Mei always right? Now test the pairs that make 20.',
         check=lambda: 'Yes' if all(a % 2 == b % 2 for t in (10, 20) for a, b in pairs_sum(t, ordered=True)) else 'No',
         hint='Test every pair, not just two or three. Write the pairs that make 20 too.',
         steps=['All 11 pairs that make 10 are both odd or both even.', 'All 21 pairs that make 20 (0 + 20 down to 20 + 0) are also both odd or both even.', 'So yes, Mei is right for 10 and for 20.'],
         src=['Mei says: "When two numbers make 10, they are both odd or both even." Is Mei always right? Now test the pairs that make 20. Why do you think it works?']),
    dict(id='I2b', tier='invest', no='Investigation 2 why', type='selfcheck', open=True, skill='odd and even bonds',
         q='Why do you think it works?',
         hint='When one number goes up by 1, the other goes down by 1. What happens to odd and even?',
         steps=['When the first number goes up by 1, the second goes down by 1. Both change from odd to even (or even to odd) together, so they always match.', 'Another way to say it: an odd number and an even number always make an odd total, and 10 and 20 are even, so that can never happen.', 'Any reason that is more than "it just works" is good.'],
         src=['Why do you think it works?']),

    # ================= Think harder
    dict(id='T1a', tier='stretch', no='T1(a)', type='choice', skill='sums that stay the same', options=['Mei', 'Ben'], answer='Mei',
         q='Mei says 7 + 5 = 8 + 4. Ben says 7 + 5 = 8 + 5. Who is right?', check=lambda: 'Mei' if 7 + 5 == 8 + 4 else ('Ben' if 7 + 5 == 8 + 5 else 'neither'),
         hint='Look at how 7 + 5 changed into 8 + 4. Did one number go up and the other go down by the same amount?',
         steps=['Mei is right. 7 + 5 = 12 and 8 + 4 = 12.', 'Ben is not right. 8 + 5 = 13, which is 1 more than 12.'],
         src=['Mei says 7 + 5 = 8 + 4. Ben says 7 + 5 = 8 + 5. Who is right? Show how you know without adding both sides.']),
    dict(id='T1b', tier='stretch', no='T1(b)', type='selfcheck', open=False, skill='sums that stay the same',
         q='Show how you know who is right without adding both sides.', facts=dict(mei=(1, -1), ben=(1, 0)),
         check=lambda: dict(mei=(8 - 7, 4 - 5), ben=(8 - 7, 5 - 5)),
         hint='Compare the first numbers (7 and 8) and the second numbers (5 and 4, or 5 and 5).',
         steps=['Mei: 8 is 1 more than 7 and 4 is 1 less than 5, so the total stays the same (both sides make 12).', 'Ben: 8 is 1 more than 7 but 5 is the same as 5, so his right side is 1 too big (13).', 'Any answer that says one number went up by 1 and the other went down by 1 is good.'],
         src=['Show how you know without adding both sides.']),
    dict(id='T2a', tier='stretch', no='T2(a)', type='number', skill='all the pairs', answer=4,
         q='Siti puts 10 stickers into two pockets. The left pocket must have MORE stickers than the right pocket, and each pocket has at least 1 sticker. How many ways can she do it?',
         check=lambda: len(pockets()),
         hint='List them in order, starting with the biggest right pocket that works. 5 and 5 is a tie, so it does not count.',
         steps=['Left and right must make 10, with left bigger and right at least 1.', '6 and 4, 7 and 3, 8 and 2, 9 and 1.', 'There are 4 ways.'],
         src=['Siti puts 10 stickers into two pockets. The left pocket must have MORE stickers than the right pocket, and each pocket has at least 1 sticker. How many ways can she do it? List them in order.']),
    dict(id='T2b', tier='stretch', no='T2(b)', type='selfcheck', open=False, skill='all the pairs',
         q='List the ways in order (left pocket, right pocket).', facts=[(6, 4), (7, 3), (8, 2), (9, 1)], check=lambda: sorted(pockets()),
         hint='Start with 6 and 4, then make the left pocket 1 bigger each time.',
         steps=['6 and 4', '7 and 3', '8 and 2', '9 and 1', 'Going one at a time shows none are missed. 5 and 5 is a tie, and 10 and 0 leaves a pocket empty.'],
         src=['How many ways can she do it? List them in order.']),
    dict(id='T3a', tier='stretch', no='T3(a)', type='fields', skill='sums that change', answer=[12, 10],
         q='7 + 3 = 10. What is 8 + 4? What is 8 + 2?', frame='8 + 4 = {f1}      8 + 2 = {f2}', check=lambda: [sum([8, 4]), sum([8, 2])],
         hint='Add the two numbers. You can use 7 + 3 = 10 to help you.',
         steps=['8 + 4 = 12.', '8 + 2 = 10.'],
         src=['7 + 3 = 10. What is 8 + 4? What is 8 + 2? What happened to the total each time, and why?']),
    dict(id='T3b', tier='stretch', no='T3(b)', type='selfcheck', open=False, skill='sums that change',
         q='What happened to the total each time, and why?', facts=dict(first=2, second=0),
         check=lambda: dict(first=(8 + 4) - (7 + 3), second=(8 + 2) - (7 + 3)),
         hint='Compare 7 + 3 with 8 + 4, then 7 + 3 with 8 + 2. What changed in each number?',
         steps=['8 + 4: both numbers went up by 1 (7 to 8 and 3 to 4), so the total went up by 2 (10 to 12).', '8 + 2: one number went up by 1 and the other went down by 1, so the total stayed the same (10).'],
         src=['What happened to the total each time, and why?']),
    dict(id='T4a', tier='stretch', no='T4(a)', type='number', skill='all the pairs', answer=6,
         q='Find all the pairs of numbers from 1 to 11 that make 12. (3 + 9 and 9 + 3 count as the same pair.) How many pairs are there?',
         check=lambda: len(pairs_sum(12, 1, 11)),
         hint='Write them in order from 1 + 11. Stop when the first number is as big as the second.',
         steps=['1 + 11, 2 + 10, 3 + 9, 4 + 8, 5 + 7 and 6 + 6.', 'After 6 + 6 the pairs only turn round.', 'There are 6 pairs.'],
         src=['Find all the pairs of numbers from 1 to 11 that make 12. (3 + 9 and 9 + 3 count as the same pair.) How many pairs are there?']),
    dict(id='T4b', tier='stretch', no='T4(b)', type='selfcheck', open=False, skill='all the pairs',
         q='Write all the pairs of numbers from 1 to 11 that make 12.', facts=[(1, 11), (2, 10), (3, 9), (4, 8), (5, 7), (6, 6)], check=lambda: pairs_sum(12, 1, 11),
         hint='Start with 1 + 11 and go down one number at a time.',
         steps=['1 + 11, 2 + 10, 3 + 9, 4 + 8, 5 + 7, 6 + 6.', 'Going down one number at a time shows none are missed.'],
         src=['Find all the pairs of numbers from 1 to 11 that make 12.']),

    # ================= Go further
    dict(id='C1a', tier='challenge', no='C1(a)', type='fields', skill='two shapes, two sums', answer=[5, 2],
         q='Two circles and one square add up to 12. One circle and two squares add up to 9. What number is each shape?', frame='circle = {f1},     square = {f2}',
         svg=shape_sums([(2, 1, 12), (1, 2, 9)]),
         check=lambda: next([c, s] for c in range(13) for s in range(13) if 2 * c + s == 12 and c + 2 * s == 9),
         hint='Try a number for the circle. Then find the square from the first sum and test it in the second sum.',
         steps=['Try circle = 5: 5 + 5 + square = 12, so the square is 2.', 'Check the second sum: 5 + 2 + 2 = 9. It works.', 'Each circle is 5 and each square is 2.'],
         src=['Two circles and one square add up to 12. One circle and two squares add up to 9. What number is each shape? Explain how you found it.']),
    dict(id='C1b', tier='challenge', no='C1(b)', type='selfcheck', open=False, skill='two shapes, two sums',
         q='Explain how you found it.', facts=3, check=lambda: next(c - s for c in range(13) for s in range(13) if 2 * c + s == 12 and c + 2 * s == 9),
         hint='Guess and check works. Or compare the two sums: what changes when you swap one circle for one square?',
         steps=['One way: guess a circle, find the square from the first sum, and check in the second sum.', 'Another way: the two totals differ by 3 (12 and 9), and the only change is one circle swapped for one square, so a circle is 3 more than a square.',
                'Then 3 squares and 6 more make 12, so each square is 2 and each circle is 5.'],
         src=['Explain how you found it.']),
    dict(id='C2', tier='challenge', no='C2', type='fields', skill='sharing with a difference', answer=[7, 4],
         q='Ali has 20 stickers. He keeps 9 and shares the rest between Ben and Mei. Ben gets 3 more than Mei. How many does each get?', frame='Ben gets {f1},     Mei gets {f2}',
         check=lambda: next([b, m] for m in range(21) for b in range(21) if b + m == 20 - 9 and b - m == 3),
         hint='First find how many stickers are shared. Then find two numbers with that total where one is 3 more.',
         steps=['20 - 9 = 11 stickers are shared.', 'Take away Ben\'s extra 3: 11 - 3 = 8. Share 8 equally: 4 and 4.', 'Mei gets 4. Ben gets 4 + 3 = 7.', 'Check: 7 + 4 = 11 and 7 is 3 more than 4.'],
         src=['Ali has 20 stickers. He keeps 9 and shares the rest between Ben and Mei. Ben gets 3 more than Mei. How many does each get?']),
    dict(id='C3a', tier='challenge', no='C3(a)', type='choice', skill='magic triangle', options=['Yes', 'No'], answer='Yes',
         q='Change the magic triangle: use the numbers 2, 3, 4, 5, 6 and 7 instead of 1 to 6. Can you make every side add to the same total?',
         svg=magic_triangle(caption='An empty magic triangle'),
         check=lambda: 'Yes' if any(magic_solutions(TWO_TO_SEVEN, S) for S in range(0, 40)) else 'No',
         hint='Try putting the three biggest numbers in the corners, or the three smallest. Test the sides.',
         steps=['Yes. It still works with 2, 3, 4, 5, 6 and 7.', 'The next question shows which totals you can make.'],
         src=['Change the magic triangle: use the numbers 2, 3, 4, 5, 6 and 7 instead of 1 to 6. Can you make every side add to the same total? Try it. Which totals can you make?']),
    dict(id='C3b', tier='challenge', no='C3(b)', type='set', ordered=False, skill='magic triangle', answer=[12, 13, 14, 15],
         q='Which totals can you make? Type them with a comma between.',
         check=lambda: [S for S in range(0, 40) if magic_solutions(TWO_TO_SEVEN, S)],
         hint='The smallest total comes with the smallest numbers in the corners. Try each total from 12 up.',
         steps=['Corners 2, 3 and 4 make every side add to 12.', 'The totals 13, 14 and 15 can be made too (the corners get bigger as the total gets bigger).', 'The totals are 12, 13, 14 and 15. No other total works.'],
         src=['Which totals can you make?']),
    dict(id='C3c', tier='challenge', no='C3(c)', type='selfcheck', paper=True, skill='magic triangle',
         q='Make a magic triangle with 2, 3, 4, 5, 6 and 7 so that every side adds to 12.', svg=magic_triangle(caption='An empty magic triangle'),
         facts=EX12, check=lambda: EX12 if EX12 in magic_solutions(TWO_TO_SEVEN, 12) else None,
         sol_fig=lambda f: magic_triangle(corners=f[:3], sides=f[3:], caption='An example: every side adds up to 12'),
         hint='Put 2, 3 and 4 in the corners. Then find the number between each pair of corners.',
         steps=['Here is one way (other answers are right too): corners 2, 3 and 4.', 'Put 7 between 2 and 3 (2 + 7 + 3 = 12), 5 between 3 and 4 (3 + 5 + 4 = 12) and 6 between 4 and 2 (4 + 6 + 2 = 12).', 'Check every side adds to 12.'],
         src=['Change the magic triangle: use the numbers 2, 3, 4, 5, 6 and 7 instead of 1 to 6.']),
]


def _count_on(start, k):
    v = start
    for _ in range(k):
        v += 1
    return v


def _search(total, known):
    return next(x for x in range(0, 40) if known + x == total)


VARIANTS = {
    '4a': dict(
        base=dict(a=5, b=3, c=4),
        tpl=dict(vars=dict(a=[2, 3, 4, 5, 6, 7], b=[1, 2, 3, 4, 5, 6], c=[1, 2, 3]),
                 q='The = sign means "is the same as". Fill in the blank.', frame='{a} + {b} = {c} + {f1}', answers=dict(f1='a+b-c'),
                 hint='Work out {a} + {b} first. What goes with {c} to make the same?',
                 steps=['{a} + {b} = {t}, so the right side must be {t} too.', '{c} + {ans} = {t}, so the box is {ans}.'], derive=dict(t='a+b')),
        oracle=lambda e: dict(f1=next(x for x in range(40) if e['a'] + e['b'] == e['c'] + x))),
    '3c': dict(
        base=dict(a=12, b=9, c=15),
        tpl=dict(vars=dict(a=[11, 12, 13, 14, 15], b=[6, 7, 8, 9], c=[15, 16, 17, 18]),
                 q='Use bonds of 10 to help you with bonds of 20.', frame='20 = {a} + {f1},   20 = {f2} + {b},   20 = {c} + {f3}',
                 answers=dict(f1='20-a', f2='20-b', f3='20-c'),
                 hint='Count on from the number you are given to 20. Use a bond of 10 to help.',
                 steps=['{a} + {f1} = 20: count on from {a} to 20.', 'The boxes are {ans}.']),
        oracle=lambda e: dict(f1=_search(20, e['a']), f2=_search(20, e['b']), f3=_search(20, e['c']))),
    '3a': dict(
        base=dict(a=6),
        tpl=dict(vars=dict(a=[1, 2, 3, 4, 5, 6, 7, 8, 9]),
                 q='Use bonds of 10 to help you with bonds of 20.', frame='{a} + {b} = 10, so  {s} + {b} = {f1}   and   {a} + {t} = {f2}',
                 answers=dict(f1='s+b', f2='a+t'), derive=dict(b='10-a', s='a+10', t='b+10'),
                 hint='{a} + {b} = 10. {s} is 10 more than {a}, so the answer is 10 more than 10.',
                 steps=['{a} + {b} = 10. {s} is {a} and 10 more, so {s} + {b} = 20.', '{t} is {b} and 10 more, so {a} + {t} = 20.']),
        oracle=lambda e: dict(f1=_count_on(e['a'] + 10, 10 - e['a']), f2=_count_on(e['a'], 10 - e['a'] + 10))),
}
