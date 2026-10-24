"""Level 2 (P2) holiday lesson 1: DIGIT DETECTIVES (Numbers to 1000), week 1, first lesson.  Online mirror of the printed workbook pages.

The questions are the ones printed in the Level 2 holiday workbook (p2/content/l1.js `workbook()` = Start here, p2/gaps.json lesson 1 `invest` =
Investigation, p2/content/l1.js `qbank.stretch` first four = Think harder 1 to 4, `qbank.challenge` last three = Go further 5 to 7, as built by
p2/workbook_html.js).  Every answer is recomputed by an INDEPENDENT checker (loops over the numbers in the question, never a copy of the printed
answer); build_holiday.py stops if a checker and the printed answer differ.  Figures are the printed ones (p2/workbook_body.html) or redrawn.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *          # noqa: E402,F401
from p2lib import *         # noqa: E402,F401

META = dict(level=2, lesson=1, key='p2', title='Digit detectives', workbook_title='DIGIT DETECTIVES', topic='Numbers to 1000', strand='Numbers to 1000',
            sources=['p2/content/l1.js', 'p2/gaps.json', 'p2/workbook_html.js'],
            intro=['Use the pictures, counters or paper if they help you. Type numbers with a comma between them when a question asks for a list.',
                   'Some questions ask you to explain. Write your idea in the box, then read the worked solution after you submit and compare.'])
SK = 'Numbers to 1000'


# ---------------------------------------------------------------- independent checkers
def place_total(h, t, o):
    """Count the value up: h hundreds, t tens, o ones."""
    total = 0
    for _ in range(h):
        total += 100
    for _ in range(t):
        total += 10
    for _ in range(o):
        total += 1
    return total


def chart(first, row0, col0):
    """A piece of a 1000 chart (rows of 10): the number at (row, col) when `first` sits at (row0, col0)."""
    return lambda r, c: first + 10 * (r - row0) + (c - col0)


def mirror_numbers(lo, hi):
    return [n for n in range(lo, hi + 1) if str(n) == str(n)[::-1]]


def swap_tens_ones(n):
    s = str(n)
    return int(s[0] + s[2] + s[1])


def counting(start, step, how_many):
    out, v = [], start
    for _ in range(how_many):
        out.append(v); v += step
    return out


def says(start, step, limit):
    out, v = set(), start
    while v <= limit:
        out.add(v); v += step
    return out


A = chart(347, 0, 0)           # piece A: 347 at the top left
B = chart(586, 0, 1)           # piece B: 586 at the top middle

CARDS = [
    dict(figure=printed_fig('Digit cards 2, 7 and 4')),
    dict(figure=printed_fig('Digit cards 0, 5 and 9')),
]
CHART_FIG = printed_fig('Two pieces of a 1000 chart').replace('font-size="20"', 'font-size="26"')   # bigger Piece A / Piece B labels for a phone
P1 = numbers_from_cards([2, 7, 4])

ITEMS = [
    # ================= Start here (workbook lesson 1, No.1 to No.6)
    dict(id='1a', tier='core', no='1(a)', type='number', skill='place value',
         q='Place value. Fill in the blank. 4 hundreds, 0 tens and 7 ones = ?', answer=407, check=lambda: place_total(4, 0, 7),
         hint='Hundreds first, then tens, then ones. 4 hundreds is 400.',
         steps=['4 hundreds is 400.', '0 tens is 0.', '7 ones is 7.', '400 + 0 + 7 = 407.'],
         src=['4 hundreds, 0 tens and 7 ones']),
    dict(id='1b', tier='core', no='1(b)', type='number', skill='place value',
         q='Place value. Fill in the blank. 6 hundreds, 15 tens and 2 ones = ?', answer=752, check=lambda: place_total(6, 15, 2),
         hint='15 tens is more than 10 tens. Work out 15 tens first: 10 tens make a hundred.',
         steps=['6 hundreds is 600.', '15 tens is 150, because 15 x 10 = 150.', '2 ones is 2.', '600 + 150 = 750, and 750 + 2 = 752.'],
         src=['6 hundreds, 15 tens and 2 ones']),
    dict(id='1c', tier='core', no='1(c)', type='fields', skill='place value',
         q='Place value. Fill in the blanks.', frame='830 = 8 hundreds and {f1} tens, and 830 = 7 hundreds and {f2} tens', answer=[3, 13],
         check=lambda: [(830 - 800) // 10, (830 - 700) // 10],
         hint='Take away the hundreds first. What is left? Then count it in tens.',
         steps=['830 - 800 = 30, and 30 is 3 tens. So 830 = 8 hundreds and 3 tens.', '830 - 700 = 130, and 130 is 13 tens. So 830 = 7 hundreds and 13 tens.'],
         src=['830  =  8 hundreds and ____ tens', '830  =  7 hundreds and ____ tens']),
    dict(id='1d', tier='core', no='1(d)', type='number', skill='place value',
         q='In 572, the digit 7 is worth ?', answer=70, check=lambda: int('572'[1]) * 10,
         hint='Which place is the 7 in: hundreds, tens or ones?',
         steps=['In 572 the 5 is in the hundreds place, the 7 is in the tens place and the 2 is in the ones place.', 'So the 7 is worth 7 tens, which is 70.'],
         src=['In 572, the digit 7 is worth']),

    dict(id='2a', tier='core', no='2(a)', type='set', ordered=False, skill='digit cards', answer=P1,
         q='Use the digit cards 2, 7 and 4. Use each card once to make a 3-digit number. Make a list in order. Write every number you can make. Type them with a comma between.',
         svg=CARDS[0]['figure'], check=lambda: numbers_from_cards([2, 7, 4]),
         hint='Start with 2 in the hundreds place and make two numbers. Then start with 4, then 7.',
         steps=['Start with 2: 247 and 274.', 'Start with 4: 427 and 472.', 'Start with 7: 724 and 742.', 'In order: 247, 274, 427, 472, 724, 742. There are 6 numbers.'],
         src=['Use the digit cards 2, 7 and 4. Use each card once to make a 3-digit number.', 'Make a list in order. Write every number you can make.']),
    dict(id='2b', tier='core', no='2(b)', type='fields', skill='digit cards',
         q='Use the digit cards 2, 7 and 4 again. Look at your list.', frame='Biggest number: {f1}   Smallest number: {f2}', answer=[742, 247],
         svg=CARDS[0]['figure'], check=lambda: [max(numbers_from_cards([2, 7, 4])), min(numbers_from_cards([2, 7, 4]))],
         hint='The biggest number has the biggest card in the hundreds place. The smallest has the smallest card there.',
         steps=['Biggest: put 7 in the hundreds, then 4, then 2. That is 742.', 'Smallest: put 2 in the hundreds, then 4, then 7. That is 247.'],
         src=['Biggest number:  ________        Smallest number:  ________']),
    dict(id='2c', tier='core', no='2(c)', type='number', skill='digit cards',
         q='Which of your numbers (made with the cards 2, 7 and 4) is closest to 500?', answer=472, svg=CARDS[0]['figure'],
         check=lambda: min(numbers_from_cards([2, 7, 4]), key=lambda n: abs(n - 500)),
         hint='Look for the numbers just below and just above 500. Which one is nearer?',
         steps=['The numbers near 500 are 472 and 724. 472 is 28 below 500.', '427 is 73 below 500, and 724 is 224 above 500.', 'The closest is 472.'],
         src=['Which of your numbers is closest to 500?']),
    dict(id='2d', tier='core', no='2(d)', type='number', skill='digit cards',
         q='How many of your numbers (made with the cards 2, 7 and 4) are odd?', answer=2, svg=CARDS[0]['figure'],
         check=lambda: sum(1 for n in numbers_from_cards([2, 7, 4]) if n % 2 == 1),
         hint='A number is odd when its ones digit is odd. Look at the last digit of each of your 6 numbers.',
         steps=['The numbers are 247, 274, 427, 472, 724 and 742.', 'The odd ones end in 7: 247 and 427.', 'So 2 of the numbers are odd.'],
         src=['How many of your numbers are odd?']),

    dict(id='3a', tier='core', no='3(a)', type='set', ordered=False, skill='digit cards with zero', answer=[509, 590, 905, 950],
         q='Now use the digit cards 0, 5 and 9. List every 3-digit number you can make, in order. Type them with a comma between.',
         svg=CARDS[1]['figure'], check=lambda: numbers_from_cards([0, 5, 9]),
         hint='Can 0 go in the hundreds place? A number like 059 is really 59, a 2-digit number.',
         steps=['0 cannot go first, so the hundreds digit is 5 or 9.', 'Start with 5: 509 and 590.', 'Start with 9: 905 and 950.', 'In order: 509, 590, 905, 950. There are 4 numbers.'],
         src=['Now use the digit cards 0, 5 and 9.', 'List every 3-digit number you can make, in order.']),
    dict(id='3b', tier='core', no='3(b)', type='selfcheck', open=False, skill='digit cards with zero',
         q='The cards 2, 7, 4 made 6 numbers. Why do 0, 5, 9 make fewer?', svg=CARDS[1]['figure'],
         facts=dict(with_247=6, with_059=4, starting_with_zero=['059', '095']),
         check=lambda: dict(with_247=len(numbers_from_cards([2, 7, 4])), with_059=len(numbers_from_cards([0, 5, 9])),
                            starting_with_zero=sorted(''.join(map(str, p)) for p in itertools.permutations([0, 5, 9]) if p[0] == 0)),
         hint='Write down all 6 ways to order the cards 0, 5, 9. Are they all 3-digit numbers?',
         steps=['The 6 ways are 059, 095, 509, 590, 905 and 950.', '059 and 095 start with 0, so they are really 59 and 95, which are 2-digit numbers.', 'Only 4 of the 6 ways make a 3-digit number: 509, 590, 905 and 950.',
                'So the zero card makes fewer, because 0 cannot go in the hundreds place. Any answer that says this is good.'],
         src=['The cards 2, 7, 4 made 6 numbers. Why do 0, 5, 9 make fewer?']),

    dict(id='4A', tier='core', no='4 (Piece A)', type='fields', skill='1000 chart', answer=[348, 349, 357, 359, 367, 368],
         q='These are pieces cut from a 1000 chart. Each row has 10 numbers. Fill in the empty squares of Piece A.', svg=CHART_FIG,
         frame='Piece A. Top row: 347, {f1}, {f2}. Middle row: {f3}, 358, {f4}. Bottom row: {f5}, {f6}, 369.',
         check=lambda: [A(0, 1), A(0, 2), A(1, 0), A(1, 2), A(2, 0), A(2, 1)] if (A(1, 1), A(2, 2)) == (358, 369) else None,
         hint='On a chart with rows of 10, the next square to the right is 1 more. The square below is 10 more.',
         steps=['Going right adds 1, so the top row is 347, 348, 349.', 'Going down adds 10, so the middle row is 357, 358, 359 (358 is already there).', 'The bottom row is 367, 368, 369.', 'The empty squares are 348, 349, 357, 359, 367 and 368.'],
         src=['These are pieces cut from a 1000 chart. Each row has 10 numbers. Fill in the empty squares.']),
    dict(id='4B', tier='core', no='4 (Piece B)', type='fields', skill='1000 chart', answer=[595, 596, 597, 606],
         q='Now fill in the empty squares of Piece B.', svg=CHART_FIG,
         frame='Piece B. Top row: 586. Middle row: {f1}, {f2}, {f3}. Bottom row: {f4} (the square under the middle one).',
         check=lambda: [B(1, 0), B(1, 1), B(1, 2), B(2, 1)],
         hint='Start at 586. One square down is 10 more. Then go left and right by 1.',
         steps=['The square under 586 is 586 + 10 = 596.', 'To its left is 1 less, 595. To its right is 1 more, 597.', 'The square under 596 is 596 + 10 = 606.', 'The empty squares are 595, 596, 597 and 606.'],
         src=['These are pieces cut from a 1000 chart.']),
    dict(id='4a', tier='core', no='4(a)', type='fields', skill='1000 chart', answer=[10, 1],
         q='Look at the pieces of the 1000 chart.', svg=CHART_FIG, frame='On the chart, one square DOWN is {f1} more. One square RIGHT is {f2} more.',
         check=lambda: [A(1, 0) - A(0, 0), A(0, 1) - A(0, 0)],
         hint='Look at 347 and the square below it. How much bigger is the one below?',
         steps=['A row has 10 numbers, so the number below is 10 more: 347, then 357.', 'The number to the right is 1 more: 347, then 348.'],
         src=['On the chart, one square DOWN is ______ more.  One square RIGHT is ______ more.']),
    dict(id='4b', tier='core', no='4(b)', type='number', skill='1000 chart',
         q='Which number is 2 squares below 385 on the chart?', answer=405, check=lambda: 385 + 10 + 10,
         hint='One square down is 10 more. Go down 2 squares.',
         steps=['One square below 385 is 385 + 10 = 395.', 'One more square down is 395 + 10 = 405.', 'So 405 is 2 squares below 385.'],
         src=['Which number is 2 squares below 385 on the chart?']),

    dict(id='5a', tier='core', no='5(a)', type='fields', skill='number patterns', answer=[347, 447],
         q='Look for the pattern. Fill in the next numbers.', frame='47, 147, 247, {f1}, {f2}', check=lambda: counting(47, 100, 5)[3:],
         hint='From 47 to 147 is how much? Does it keep going up by that much?',
         steps=['47 to 147 is 100 more, and 147 to 247 is 100 more.', '247 + 100 = 347, and 347 + 100 = 447.'],
         src=['47,   147,   247,   ______,   ______']),
    dict(id='5b', tier='core', no='5(b)', type='fields', skill='number patterns', answer=[502, 492],
         q='Look for the pattern. Fill in the next numbers.', frame='532, 522, 512, {f1}, {f2}', check=lambda: counting(532, -10, 5)[3:],
         hint='The numbers get smaller. By how much each time?',
         steps=['532 to 522 is 10 less. 522 to 512 is 10 less too.', '512 - 10 = 502, and 502 - 10 = 492.'],
         src=['532,   522,   512,   ______,   ______']),
    dict(id='5c', tier='core', no='5(c)', type='fields', skill='number patterns', answer=[1000],
         q='Look for the pattern. Fill in the next number.', frame='980, 985, 990, 995, {f1}', check=lambda: counting(980, 5, 5)[4:],
         hint='The numbers go up in 5s. What comes after 995?',
         steps=['The pattern adds 5 each time: 980, 985, 990, 995.', '995 + 5 = 1000.'],
         src=['980,   985,   990,   995,   ______']),
    dict(id='5d', tier='core', no='5(d)', type='fields', skill='number patterns', answer=[700, 699],
         q='Look for the pattern. Fill in the next numbers.', frame='703, 702, 701, {f1}, {f2}', check=lambda: counting(703, -1, 5)[3:],
         hint='The numbers go down by 1 each time. Be careful when you reach 700.',
         steps=['The pattern takes away 1 each time: 703, 702, 701.', '701 - 1 = 700, and 700 - 1 = 699.', 'After 700 the hundreds digit changes from 7 to 6.'],
         src=['703,   702,   701,   ______,   ______']),

    dict(id='6a', tier='core', no='6(a)', type='number', skill='digit riddles', answer=435,
         q='Digit riddles. Who am I? I am a 3-digit number. My hundreds digit is 4. My ones digit is 2 more than my tens digit. My digits add up to 12.',
         check=lambda: [n for n in range(100, 1000) if n // 100 == 4 and n % 10 == (n // 10) % 10 + 2 and digit_sum(n) == 12][0],
         hint='The hundreds digit is 4, so the tens and ones digits add up to 12 - 4. Try a tens digit and find the ones digit that is 2 more.',
         steps=['The three digits add up to 12 and the hundreds digit is 4, so the tens digit and the ones digit add up to 8.', 'The ones digit is 2 more than the tens digit. Two digits that add up to 8 and differ by 2 are 3 and 5.', 'The tens digit is 3 and the ones digit is 5. The number is 435.', 'Check: 4 + 3 + 5 = 12, and 5 is 2 more than 3.'],
         src=['I am a 3-digit number. My hundreds digit is 4. My ones digit is 2 more than my tens digit. My digits add up to 12.']),
    dict(id='6b', tier='core', no='6(b)', type='set', ordered=False, skill='digit riddles', answer=[102, 111, 120, 201, 210, 300],
         q='Digit riddles. I am a 3-digit number. My digits add up to 3. Find ALL the numbers I could be. Type them with a comma between.',
         check=lambda: [n for n in range(100, 1000) if digit_sum(n) == 3],
         hint='Use 3 counters. Put 1 counter in the hundreds box, then share the other 2 between the tens and the ones. Then try 2 counters in the hundreds box, then 3.',
         steps=['1 counter in the hundreds: share 2 counters between tens and ones: 102, 111, 120.', '2 counters in the hundreds: share 1 counter: 201, 210.', '3 counters in the hundreds: 300.', 'The numbers are 102, 111, 120, 201, 210 and 300.'],
         src=['I am a 3-digit number. My digits add up to 3. Find ALL the numbers I could be.']),
    dict(id='6c', tier='core', no='6(b) how many', type='number', skill='digit riddles', answer=6,
         q='Digit riddles. I am a 3-digit number and my digits add up to 3. How many numbers could I be?', check=lambda: len([n for n in range(100, 1000) if digit_sum(n) == 3]),
         hint='Count the numbers you found in the question before.',
         steps=['The numbers are 102, 111, 120, 201, 210 and 300.', 'That is 6 numbers.'],
         src=['How many numbers?']),

    # ================= Investigation (end of the Start here pages): Mirror numbers
    dict(id='I1', tier='invest', no='Investigation (a)', type='selfcheck', open=False, skill='mirror numbers',
         q='Mirror numbers. A mirror number reads the same forwards and backwards, like 252 or 909. Write 5 mirror numbers of your own. Easy first step: write 252, 909 and 131, then write three more mirror numbers.',
         facts=[101, 111, 121, 131, 141], check=lambda: mirror_numbers(100, 999)[:5],
         hint='The first digit and the last digit must be the same. The middle digit can be anything.',
         steps=['A mirror number has the same first and last digit, for example 101, 111, 121, 131 and 141.', 'Any 5 numbers whose first and last digits match are right, for example 454 or 777.'],
         src=['A mirror number reads the same forwards and backwards, like 252 or 909.', 'Write 5 mirror numbers of your own.']),
    dict(id='I2', tier='invest', no='Investigation (b)', type='set', ordered=False, skill='mirror numbers', answer=[202, 212, 222, 232, 242, 252, 262, 272, 282, 292],
         q='Mirror numbers. Find ALL the mirror numbers from 200 to 299. Type them with a comma between.', check=lambda: mirror_numbers(200, 299),
         hint='The first digit is 2, so the last digit is 2 too. Then try every middle digit from 0 to 9.',
         steps=['The first and last digits must both be 2.', 'The middle digit can be 0, 1, 2, ... 9. That is 10 choices.', 'The numbers are 202, 212, 222, 232, 242, 252, 262, 272, 282 and 292.'],
         src=['Find ALL the mirror numbers from 200 to 299.']),
    dict(id='I3', tier='invest', no='Investigation (b) how', type='selfcheck', open=False, skill='mirror numbers',
         q='Mirror numbers. How do you know you have found ALL the mirror numbers from 200 to 299?', facts=dict(ends=2, middle_choices=10, count=10),
         check=lambda: dict(ends=2, middle_choices=len({(n // 10) % 10 for n in mirror_numbers(200, 299)}), count=len(mirror_numbers(200, 299))),
         hint='What must the first and last digits be? How many choices are there for the middle digit?',
         steps=['The first and last digits must both be 2. Only the middle digit can change.', 'The middle digit has 10 choices (0 to 9), so there are exactly 10 numbers.', 'A child who lists them by the middle digit in order, 202, 212, 222 ..., has not missed any. That is a good reason.'],
         src=['How do you know you have found them all?']),
    dict(id='I4', tier='invest', no='Investigation (c)', type='choice', skill='mirror numbers', options=['Yes', 'No'], answer='No',
         q='Mirror numbers. Ali says every mirror number is odd. Is he right?', check=lambda: 'Yes' if all(n % 2 == 1 for n in mirror_numbers(100, 999)) else 'No',
         hint='Can you find one mirror number that is even? Its last digit would be even.',
         steps=['Ali is not right. 202 is a mirror number and it is even.', 'A mirror number is even when its first (and last) digit is even.'],
         src=['Ali says every mirror number is odd. Is he right?']),

    # ================= Think harder (workbook Think harder 1 to 4)
    dict(id='T1a', tier='stretch', no='Think harder 1', type='set', ordered=False, skill='digit cards', answer=[629, 692, 926, 962],
         q='Use the digit cards 2, 6 and 9 once each. Make a list in order of every 3-digit number you can make that is bigger than 500. Type them with a comma between.',
         check=lambda: [n for n in numbers_from_cards([2, 6, 9]) if n > 500],
         hint='A number that starts with 2 is smaller than 300. So which cards can go in the hundreds place?',
         steps=['If 2 is in the hundreds place the number is less than 300, so 2 cannot be first.', 'Start with 6: 629 and 692.', 'Start with 9: 926 and 962.', 'In order: 629, 692, 926, 962.'],
         src=['Use the digit cards 2, 6 and 9 once each. Make a list in order of every 3-digit number you can make that is bigger than 500.']),
    dict(id='T1b', tier='stretch', no='Think harder 1 (how)', type='selfcheck', open=False, skill='digit cards',
         q='How do you know you have found all the numbers bigger than 500 that you can make with the cards 2, 6 and 9?',
         facts=dict(hundreds_digits=[6, 9], how_many=4),
         check=lambda: dict(hundreds_digits=sorted({n // 100 for n in numbers_from_cards([2, 6, 9]) if n > 500}), how_many=len([n for n in numbers_from_cards([2, 6, 9]) if n > 500])),
         hint='Which cards can go in the hundreds place so the number is bigger than 500?',
         steps=['The hundreds digit must be 6 or 9, because a number that starts with 2 is smaller than 500.', 'With 6 in the hundreds place the other two cards make 629 and 692.', 'With 9 in the hundreds place they make 926 and 962.', 'Each starting card gives 2 numbers, so there are 4 altogether and none is missed.'],
         src=['How do you know you have found them all?']),
    dict(id='T2a', tier='stretch', no='Think harder 2', type='number', skill='digit cards', answer=3,
         q='Use the digit cards 4, 4 and 7. How many different 3-digit numbers can you make?', check=lambda: len(numbers_from_cards([4, 4, 7])),
         hint='Write the numbers in order. Remember the two 4s look the same.',
         steps=['The numbers are 447, 474 and 744.', 'There are 3 different numbers.'],
         src=['Use the digit cards 4, 4 and 7. How many different 3-digit numbers can you make?']),
    dict(id='T2b', tier='stretch', no='Think harder 2 (why)', type='selfcheck', open=False, skill='digit cards',
         q='Why is it not 6? (You use the cards 4, 4 and 7.)', facts=dict(orders=6, different=3),
         check=lambda: dict(orders=len(list(itertools.permutations([4, 4, 7]))), different=len(numbers_from_cards([4, 4, 7]))),
         hint='If the two 4s swap places, do you get a new number?',
         steps=['There are 6 ways to order three cards, but the two 4s look the same.', 'Swapping the two 4s does not make a new number. 447 with the 4s swapped is still 447.', 'So the 6 ways make only 3 different numbers: 447, 474 and 744.'],
         src=['Why is it not 6?']),
    dict(id='T3a', tier='stretch', no='Think harder 3', type='choice', skill='place value', options=['Ali', 'Siti'], answer='Ali',
         q='Ali has 46 ten-blocks. Siti has 3 hundred-blocks and 15 ten-blocks. Who has the bigger number?', svg=tens_blocks(46, 3, 15),
         check=lambda: 'Ali' if place_total(0, 46, 0) > place_total(3, 15, 0) else 'Siti',
         hint='Change each one to a number. 46 ten-blocks is 46 tens. 3 hundred-blocks and 15 ten-blocks is 3 hundreds and 15 tens.',
         steps=['Ali: 46 tens is 460.', 'Siti: 3 hundreds is 300 and 15 tens is 150. 300 + 150 = 450.', '460 is bigger than 450, so Ali has the bigger number.'],
         src=['Ali has 46 ten-blocks. Siti has 3 hundred-blocks and 15 ten-blocks. Who has the bigger number?']),
    dict(id='T3b', tier='stretch', no='Think harder 3 (how much)', type='number', skill='place value', answer=10,
         q='Ali has 46 ten-blocks. Siti has 3 hundred-blocks and 15 ten-blocks. How much bigger is the bigger number?', svg=tens_blocks(46, 3, 15),
         check=lambda: abs(place_total(0, 46, 0) - place_total(3, 15, 0)),
         hint='Work out both numbers, then find the difference.',
         steps=['Ali has 460 and Siti has 450.', '460 - 450 = 10.', 'Ali has 10 more.'],
         src=['How much bigger?']),
    dict(id='T4a', tier='stretch', no='Think harder 4', type='choice', skill='swapping digits', options=['Yes', 'No'], answer='No',
         q='Mei says: "If I swap the tens digit and the ones digit of a 3-digit number, the new number is always smaller." Is she right?',
         check=lambda: 'Yes' if all(swap_tens_ones(n) < n for n in range(100, 1000)) else 'No',
         hint='Try 452 and 425. Then try going the other way: swap the digits of 425.',
         steps=['452 becomes 425, which is smaller.', 'But 425 becomes 452, which is bigger. So Mei is not always right.'],
         src=['Mei says:', 'Is she right?']),
    dict(id='T4b', tier='stretch', no='Think harder 4 (examples)', type='selfcheck', open=False, skill='swapping digits',
         q='Show what happens with some examples. When does the number stay the same?', facts=dict(smaller=405, bigger=405, same=90),
         check=lambda: dict(smaller=sum(1 for n in range(100, 1000) if swap_tens_ones(n) < n), bigger=sum(1 for n in range(100, 1000) if swap_tens_ones(n) > n),
                            same=sum(1 for n in range(100, 1000) if swap_tens_ones(n) == n)),
         hint='Try a number whose tens digit is bigger than its ones digit, one where it is smaller, and one where they are the same.',
         steps=['452 becomes 425 (smaller): the tens digit 5 is bigger than the ones digit 2.', '425 becomes 452 (bigger): the tens digit 2 is smaller than the ones digit 5.', '733 stays 733: the tens digit and the ones digit are the same.',
                'The number gets smaller when the tens digit is bigger than the ones digit, bigger when it is smaller, and stays the same when the two digits are equal.'],
         src=['Show what happens with some examples. When does the number stay the same?']),

    # ================= Go further (workbook Go further 5 to 7, then Make up your own)
    dict(id='C5', tier='challenge', no='Go further 5', type='number', skill='digit cards', answer=381,
         q='Mei uses each of the digit cards 1, 2, 3, 4, 5 and 6 once to make two 3-digit numbers. She adds them. What is the smallest total she can make?',
         check=lambda: min(x + y for x, y in split_two([1, 2, 3, 4, 5, 6])),
         hint='The hundreds digits matter most. Which cards should go in the hundreds places to keep the total small?',
         steps=['Put the smallest cards in the biggest places: 1 and 2 in the hundreds, 3 and 4 in the tens, 5 and 6 in the ones.', 'For example 135 + 246.', 'The total is 100 + 200 + 30 + 40 + 5 + 6 = 381.'],
         src=['Mei uses each of the digit cards 1, 2, 3, 4, 5 and 6 once to make two 3-digit numbers. She adds them. What is the smallest total she can make?']),
    dict(id='C6a', tier='challenge', no='Go further 6 (500)', type='choice', skill='number patterns', options=['Yes', 'No'], answer='No',
         q='Ali counts in 5s, starting at 3: 3, 8, 13, 18 ... Will he say 500?', check=lambda: 'Yes' if 500 in says(3, 5, 1000) else 'No',
         hint='Look at the ones digit of the numbers Ali says: 3, 8, 3, 8 ...',
         steps=['Ali says only numbers that end in 3 or 8.', '500 ends in 0, so he will not say 500.'],
         src=['Ali counts in 5s, starting at 3: 3, 8, 13, 18']),
    dict(id='C6b', tier='challenge', no='Go further 6 (998)', type='choice', skill='number patterns', options=['Yes', 'No'], answer='Yes',
         q='Ali counts in 5s, starting at 3: 3, 8, 13, 18 ... Will he say 998?', check=lambda: 'Yes' if 998 in says(3, 5, 1000) else 'No',
         hint='Look at the ones digit of the numbers Ali says: 3, 8, 3, 8 ...',
         steps=['Ali says only numbers that end in 3 or 8.', '998 ends in 8, and 998 - 3 = 995 is in the 5s table, so he will say 998.'],
         src=['Will he say 500? Will he say 998? Explain.']),
    dict(id='C6c', tier='challenge', no='Go further 6 (explain)', type='selfcheck', open=False, skill='number patterns',
         q='Explain how you know whether Ali will say a number when he counts in 5s starting at 3.', facts=dict(ones_digits=[3, 8]),
         check=lambda: dict(ones_digits=sorted({n % 10 for n in says(3, 5, 1000)})),
         hint='Write the first 8 numbers Ali says. What do you notice about the ones digits?',
         steps=['Ali says 3, 8, 13, 18, 23, 28 ... The ones digit is always 3 or 8, taking turns.', 'So he says a number only if it ends in 3 or 8: not 500, but yes 998.'],
         src=['Explain.']),
    dict(id='C7', tier='challenge', no='Go further 7', type='number', skill='digit counting', answer=120,
         q='Ben writes all the numbers from 300 to 399. How many times does he write the digit 3?',
         check=lambda: sum(str(n).count('3') for n in range(300, 400)),
         hint='Count the 3s in each place separately: hundreds, tens and ones.',
         steps=['Hundreds place: every number from 300 to 399 has a 3, so 100 times.', 'Tens place: 330 to 339 have a 3 in the tens place, so 10 times.', 'Ones place: 303, 313, 323 ... 393, so 10 times.', '100 + 10 + 10 = 120.'],
         src=['Ben writes all the numbers from 300 to 399. How many times does he write the digit 3?']),
    dict(id='M', tier='challenge', no='Make up your own', type='selfcheck', open=False, skill='making riddles',
         q='Make up your own: a 3-digit number riddle with 2 or 3 clues, so that only ONE number fits. Swap with a partner.', facts=[324],
         check=lambda: [n for n in range(100, 1000) if 300 <= n < 400 and digit_sum(n) == 9 and n % 10 == 2 * ((n // 10) % 10)],
         hint='Start with a number you like. Write clues about the hundreds digit, the digits adding up, odd or even. Check that no other number fits.',
         steps=['Many answers are right. Here is one example.', '"I am between 300 and 400. My digits add up to 9. My ones digit is double my tens digit."', 'Clue 1 leaves 100 numbers. Clue 2 leaves 306, 315, 324, 333, 342, 351 and 360. Clue 3 leaves only 324.',
                'Check yours: after each clue say how many numbers still fit, and make sure a partner cannot find a second number that fits all your clues.'],
         src=['a 3-digit number riddle with 2 or 3 clues, so that only ONE number fits. Swap with a partner.']),
]

# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
VARIANTS = {
    '1a': dict(
        base=dict(h=4, t=0, o=7),
        tpl=dict(vars=dict(h=[1, 2, 3, 4, 5, 6, 7, 8, 9], t=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], o=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), q='Place value. Fill in the blank. {h} hundreds, {t} tens and {o} ones = ?',
                 answer='100*h+10*t+o', hint='Hundreds first, then tens, then ones. {h} hundreds is {h}00.',
                 steps=['{h} hundreds is {h} x 100.', '{t} tens is {t} x 10.', '{o} ones is {o}.', 'Add them: the number is {ans}.']),
        oracle=lambda e: int(f'{e["h"]}{e["t"]}{e["o"]}')),
    '1b': dict(
        base=dict(h=6, t=15, o=2),
        tpl=dict(vars=dict(h=[1, 2, 3, 4, 5, 6, 7], t=[10, 11, 12, 13, 14, 15, 16, 17, 18, 19], o=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), q='Place value. Fill in the blank. {h} hundreds, {t} tens and {o} ones = ?',
                 answer='100*h+10*t+o', hint='{t} tens is more than 10 tens. 10 tens make a hundred.',
                 steps=['{h} hundreds is {h} x 100.', '{t} tens is {t} x 10.', '{o} ones is {o}.', 'Add them: the number is {ans}.']),
        oracle=lambda e: sum([100] * e['h'] + [10] * e['t'] + [1] * e['o'])),
    '4b': dict(
        base=dict(n=385, k=2),
        tpl=dict(vars=dict(n=[101, 142, 217, 263, 385, 429, 504, 618, 735, 851], k=[1, 2, 3, 4]), q='On a 1000 chart with rows of 10, which number is {k} squares below {n}?',
                 answer='n+10*k', hint='One square down is 10 more. Go down {k} squares.',
                 steps=['One square down is 10 more.', '{k} squares down is {k} x 10 more than {n}.', 'The number is {ans}.']),
        oracle=lambda e: (lambda v: [v := v + 10 for _ in range(e['k'])][-1])(e['n'])),
    '5a': dict(
        base=dict(a=47, d=100),
        tpl=dict(vars=dict(a=[7, 17, 27, 47, 58, 63, 91], d=[10, 100]), q='Look for the pattern. Fill in the next numbers.', frame='{a}, {b}, {c}, {f1}, {f2}',
                 answers=dict(f1='a+3*d', f2='a+4*d'), derive=dict(b='a+d', c='a+2*d'), hint='From {a} to {b} is how much? Does it keep going up by that much?',
                 steps=['{a} to {b} is {d} more, and {b} to {c} is {d} more.', 'Keep adding {d}. The next numbers are {ans}.']),
        oracle=lambda e: (lambda l: dict(f1=l[3], f2=l[4]))([e['a'] + k * e['d'] for k in range(5)])),
    '5b': dict(
        base=dict(a=532, d=10),
        tpl=dict(vars=dict(a=[532, 645, 758, 861, 974, 687], d=[10, 100]), q='Look for the pattern. Fill in the next numbers.', frame='{a}, {b}, {c}, {f1}, {f2}',
                 answers=dict(f1='a-3*d', f2='a-4*d'), derive=dict(b='a-d', c='a-2*d'), hint='The numbers get smaller. By how much each time?',
                 steps=['{a} to {b} is {d} less, and {b} to {c} is {d} less.', 'Keep taking away {d}. The next numbers are {ans}.']),
        oracle=lambda e: (lambda l: dict(f1=l[3], f2=l[4]))([e['a'] - k * e['d'] for k in range(5)])),
    '5d': dict(
        base=dict(a=703),
        tpl=dict(vars=dict(a=[102, 203, 303, 403, 503, 603, 703, 803, 903]), q='Look for the pattern. Fill in the next numbers.', frame='{a}, {b}, {c}, {f1}, {f2}',
                 answers=dict(f1='a-3', f2='a-4'), derive=dict(b='a-1', c='a-2'), hint='The numbers go down by 1 each time. Be careful when you reach a hundred.',
                 steps=['The pattern takes away 1 each time: {a}, {b}, {c}.', 'The next numbers are {ans}.']),
        oracle=lambda e: (lambda l: dict(f1=l[3], f2=l[4]))([e['a'] - k for k in range(5)])),
}
