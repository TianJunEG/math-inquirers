"""Online practice for Level 4 (Primary 4, ages 9-11) holiday lesson 2: Big Number Puzzles (Numbers to 100 000).

Questions are the ones printed in the Level 4 holiday workbook (p4/workbook_html.js from p4/content/l2.js):
  Start here = l2.js workbook() Q1 to Q6; Investigation = gaps.invest (Double rounding); Think harder = qbank.stretch[0:4]; Go further = qbank.challenge[-3:] (printed Q5 to Q7).
Every answer is recomputed by an INDEPENDENT checker (brute force over the numbers in the question); build_holiday.py stops if a checker and the printed answer differ.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from p4lib import *      # noqa: E402,F401

META = dict(level=4, lesson=2, key='p4', title='Big Number Puzzles', workbook_title='BIG NUMBER PUZZLES', topic='Numbers to 100 000',
            strand='Whole numbers: numbers to 100 000',
            sources=['p4/content/l2.js'],
            intro=['Type numbers without spaces, or with spaces like the printed book (47 290 and 47290 are both fine). Where a question asks for a list, put commas between the numbers.',
                   'Some questions ask you to explain or mark a number line. Do those on paper or in your head, then compare with the answer after you submit.'])
S2 = 'Numbers to 100 000'


def D(**k):
    return dict(strand=S2, **k)


def r3(n):
    return [round_to(n, 10), round_to(n, 100), round_to(n, 1000)]


def next_terms(a, d, k=2, have=3):
    seq = [a]
    for _ in range(have + k - 1):
        seq.append(seq[-1] + d)
    return seq[have:]


def double_round(n):
    h = round_to(n, 100)
    return [h, round_to(h, 1000), round_to(n, 1000)]


BREAK = [n for n in range(1, 100000) if round_to(round_to(n, 100), 1000) != round_to(n, 1000)]
Q1_TIP = 'Round each number. Draw a number line if it helps.'

ITEMS = [
    # ================= Start here
    D(id='1a', tier='core', no='1(a)', type='fields', skill='rounding to 10, 100 and 1000', frame='47 285:  nearest 10 {f1}   nearest 100 {f2}   nearest 1000 {f3}', answer=[47290, 47300, 47000],
      check=lambda: r3(47285), q='Round each number. Draw a number line if it helps. Round 47 285 to the nearest 10, the nearest 100 and the nearest 1000.',
      hint='Look at the digit just to the right of the place you are rounding to. 5 or more rounds up.',
      steps=['Nearest 10: the ones digit is 5, so round up: 47 290.', 'Nearest 100: the tens digit is 8, so round up: 47 300.', 'Nearest 1000: the hundreds digit is 2, so round down: 47 000.'],
      src=['Round each number. Draw a number line if it helps.', '47 285']),
    D(id='1b', tier='core', no='1(b)', type='fields', skill='rounding to 10, 100 and 1000', frame='63 950:  nearest 10 {f1}   nearest 100 {f2}   nearest 1000 {f3}', answer=[63950, 64000, 64000],
      check=lambda: r3(63950), q='Round each number. Round 63 950 to the nearest 10, the nearest 100 and the nearest 1000.',
      hint='63 950 is already a whole number of tens. For the nearest 100 look at the tens digit; for the nearest 1000 look at the hundreds digit.',
      steps=['Nearest 10: 63 950 already ends in 0, so it stays 63 950.', 'Nearest 100: the tens digit is 5, so round up: 64 000.', 'Nearest 1000: the hundreds digit is 9, so round up: 64 000.'],
      src=['63 950']),
    D(id='1c-mark', tier='core', no='1 (number line)', type='selfcheck', paper=True, skill='rounding on a number line',
      q='Mark 47 285 on the line with an X.', svg=number_line_k(47000, 48000, 500, 100, caption='47 000 to 48 000'),
      facts=47285, check=lambda: 47000 + 285,
      sol_fig=lambda f: number_line_k(47000, 48000, 500, 100, cross=f),
      hint='Each small tick is 100. 47 285 is between 47 200 and 47 300, nearer to 47 300 but still before the middle mark 47 500.',
      steps=['47 285 is 285 after 47 000. Count 2 small ticks (200) from 47 000, then a little more than three quarters of the way to the next tick.', 'Put your X just before the tick for 47 300.', 'It is before the middle mark (47 500), so it is closer to 47 000.'],
      src=['Mark 47 285 on the line with an X.']),
    D(id='1c-near', tier='core', no='1 (closer to)', type='choice', options=['47 000', '48 000'], answer='47 000', skill='rounding on a number line',
      check=lambda: '47 000' if round_to(47285, 1000) == 47000 else '48 000',
      q='Which thousand is 47 285 closer to?', hint='Is 47 285 before or after the middle mark, 47 500?',
      steps=['The middle mark between 47 000 and 48 000 is 47 500.', '47 285 is before 47 500, so it is closer to 47 000.'], src=['Which thousand is it closer to?']),
    D(id='1d', tier='core', no='1 (try next) 9049', type='fields', skill='rounding to 10, 100 and 1000', frame='9049:  nearest 10 {f1}   nearest 100 {f2}   nearest 1000 {f3}', answer=[9050, 9000, 9000],
      check=lambda: r3(9049), q='Try next, if you have time: round 9049 to the nearest 10, the nearest 100 and the nearest 1000.',
      hint='Look at one digit at a time: ones for tens, tens for hundreds, hundreds for thousands.',
      steps=['Nearest 10: ones digit 9, round up: 9050.', 'Nearest 100: tens digit 4, round down: 9000.', 'Nearest 1000: hundreds digit 0, round down: 9000.'],
      src=['Try next, if you have time:   9049']),
    D(id='1e', tier='core', no='1 (try next) 80 503', type='fields', skill='rounding to 10, 100 and 1000', frame='80 503:  nearest 10 {f1}   nearest 100 {f2}   nearest 1000 {f3}', answer=[80500, 80500, 81000],
      check=lambda: r3(80503), q='Try next, if you have time: round 80 503 to the nearest 10, the nearest 100 and the nearest 1000.',
      hint='For the nearest 1000, look at the hundreds digit: 5 or more rounds up.',
      steps=['Nearest 10: ones digit 3, round down: 80 500.', 'Nearest 100: tens digit 0, round down: 80 500.', 'Nearest 1000: hundreds digit 5, round up: 81 000.'],
      src=['80 503']),

    D(id='2a', tier='core', no='2(a)', type='fields', skill='working backwards from a rounded number', frame='Smallest: {f1}   Largest: {f2}', answer=[62500, 63499],
      check=lambda: (lambda l: [min(l), max(l)])(rounds_to(60000, 66000, 63000, 1000)),
      q='Work backwards. The number of people at a concert is 63 000 when rounded to the nearest thousand. What is the smallest and the largest number of people there could be? '
        'Start here: 63 500 is halfway between 63 000 and 64 000. Does it round up or down?',
      svg=number_line_k(62000, 64000, 500, 100, caption='62 000 to 64 000'),
      hint='Halfway rounds up. So 63 500 rounds up to 64 000. What is the number just before 63 500?',
      steps=['63 500 is halfway between 63 000 and 64 000 and it rounds up to 64 000, so 63 500 is too big.', 'The largest number that still rounds to 63 000 is 63 499.', 'Halfway between 62 000 and 63 000 is 62 500, and 62 500 rounds up to 63 000. So the smallest is 62 500.'],
      src=['Work backwards.', 'The number of people at a concert is 63 000 when rounded to the nearest thousand. What is the smallest and the largest number of people there could be?',
           '63 500 is halfway between 63 000 and 64 000. Does it round up or down?', 'Smallest:  ____________          Largest:  ____________']),
    D(id='2b', tier='core', no='2(b)', type='set', ordered=False, skill='working backwards from a rounded number', answer=list(range(5345, 5355)),
      check=lambda: rounds_to(5300, 5400, 5350, 10),
      q='A whole number rounds to 5350 to the nearest 10. Find ALL the numbers it could be. Start at 5340 and check each one. '
        'Start here: 5345 is halfway between 5340 and 5350. Does 5345 round up or down? What about 5344? Type the numbers with commas between them.',
      hint='5345 rounds up to 5350 and 5344 rounds down to 5340. Check 5346, 5347 ... up to 5355.',
      steps=['5345 is halfway, so it rounds up to 5350. 5344 rounds down to 5340.', 'Going up: 5346, 5347, 5348, 5349 round to 5350, and so do 5350, 5351, 5352, 5353 and 5354.', '5355 rounds up to 5360, so stop at 5354.', 'The numbers are 5345, 5346, 5347, 5348, 5349, 5350, 5351, 5352, 5353 and 5354: 10 numbers.'],
      src=['A whole number rounds to 5350 to the nearest 10. Find ALL the numbers it could be. Start at 5340 and check each one.', '5345 is halfway between 5340 and 5350. Does 5345 round up or down? What about 5344?']),

    D(id='3a', tier='core', no='3(a)', type='number', skill='estimating by rounding', answer=30000, check=lambda: round_to(4982, 1000) * 6,
      q='A bakery bakes 4982 buns every day for 6 days. Round 4982 to the nearest thousand and estimate the total.',
      hint='4982 is close to which thousand? Then multiply that by 6.',
      steps=['4982 rounds to 5000 (the hundreds digit is 9).', 'Estimate: 6 × 5000 = 30 000.'], src=['A bakery bakes 4982 buns every day for 6 days.', 'Round 4982 to the nearest thousand and estimate the total.']),
    D(id='3b', tier='core', no='3(b)', type='choice', options=['More', 'Less'], answer='Less', skill='estimating by rounding',
      check=lambda: 'Less' if 4982 * 6 < round_to(4982, 1000) * 6 else 'More',
      q='A bakery bakes 4982 buns every day for 6 days. Is the exact total more or less than your estimate of 30 000?',
      hint='Did you round 4982 up or down?',
      steps=['4982 was rounded up to 5000, so each day was counted as a little more than it really is.', 'So the exact total is less than the estimate.'], src=['Is the exact total more or less than your estimate? How do you know without working it out?']),
    D(id='3b-why', tier='core', no='3(b) how do you know', type='selfcheck', open=True, skill='estimating by rounding',
      q='How do you know, without working it out?', hint='Think about whether 4982 was rounded up or down.',
      steps=['4982 was rounded up to 5000. Each day was counted as 18 buns too many.', 'So the estimate is more than the exact total. Any answer that says "I rounded up, so the exact total is less" is good.'],
      src=['How do you know without working it out?']),
    D(id='3c', tier='core', no='3(c)', type='number', skill='multiplying', answer=29892, check=lambda: sum([4982] * 6),
      q='A bakery bakes 4982 buns every day for 6 days. Work out the exact total.', hint='4982 × 6. You could do 5000 × 6 and take away 18 × 6.',
      steps=['6 × 5000 = 30 000.', '6 × 18 = 108.', '30 000 - 108 = 29 892.'], src=['Work out the exact total.']),

    D(id='4a', tier='core', no='4(a)', type='number', skill='number riddles', answer=47621,
      check=lambda: [n for n in five_digit_numbers() if round_to(n, 1000) == 48000 and n // 100 % 10 == 6 and n % 10 == 1 and n // 10 % 10 == 2 * (n % 10)][0],
      q='Number riddles. Who am I? I am a 5-digit number. Rounded to the nearest thousand, I am 48 000. My hundreds digit is 6. My ones digit is 1 and my tens digit is double my ones digit. '
        'Hint: the numbers that round to 48 000 are from 47 500 to 48 499. Which of them have 6 in the hundreds place?',
      hint='Numbers from 47 500 to 48 499 with 6 in the hundreds place are 47 6__ . Now use the tens and ones digits.',
      steps=['Numbers that round to 48 000 are from 47 500 to 48 499.', 'With 6 in the hundreds place: 47 600 to 47 699.', 'The ones digit is 1 and the tens digit is double that, 2. So the number is 47 621.'],
      src=['Number riddles. Who am I?', 'I am a 5-digit number. Rounded to the nearest thousand, I am 48 000. My hundreds digit is 6. My ones digit is 1 and my tens digit is double my ones digit.',
           'Hint: the numbers that round to 48 000 are from 47 500 to 48 499. Which of them have 6 in the hundreds place?']),
    D(id='4b', tier='core', no='4(b)', type='set', ordered=True, skill='number riddles', answer=[10001, 10010, 10100, 11000, 20000],
      check=lambda: [n for n in five_digit_numbers() if digit_sum(n) == 2],
      q='I am a 5-digit number. My digits add up to 2. Find ALL the numbers I could be. List them in order, smallest first, with commas between them. '
        'Start here: the digits are two 1s (and zeros) or one 2 (and zeros). The first digit cannot be 0. Write 20 000 and 10 001, then move the digits around.',
      hint='Keep the first digit 1 and move the other 1 along: 10 001, 10 010, 10 100, 11 000. Then 20 000.',
      steps=['Two 1s: the first digit must be 1, and the other 1 can be in the thousands, hundreds, tens or ones place: 11 000, 10 100, 10 010, 10 001.', 'One 2: 20 000.', 'In order: 10 001, 10 010, 10 100, 11 000, 20 000.'],
      src=['I am a 5-digit number. My digits add up to 2. Find ALL the numbers I could be. List them in order.', 'the digits are two 1s (and zeros) or one 2 (and zeros). The first digit cannot be 0. Write 20 000 and 10 001, then move the digits around.']),
    D(id='4b-count', tier='core', no='4(b) how many', type='number', skill='number riddles', answer=5, check=lambda: len([n for n in five_digit_numbers() if digit_sum(n) == 2]),
      q='How many 5-digit numbers have digits that add up to 2?', hint='Count the numbers in your list.',
      steps=['The list is 10 001, 10 010, 10 100, 11 000 and 20 000.', 'That is 5 numbers.'], src=['How many numbers?']),

    D(id='5a', tier='core', no='5(a)', type='fields', skill='number patterns', frame='23 450,  24 450,  25 450,  {f1},  {f2}', answer=[26450, 27450], check=lambda: next_terms(23450, 1000),
      q='Find the rule. Write the next numbers.', hint='How much does the number grow from 23 450 to 24 450? Which digit changes?',
      steps=['From 23 450 to 24 450 the number grows by 1000 (the thousands digit goes up by 1).', '25 450 + 1000 = 26 450, and 26 450 + 1000 = 27 450.'],
      src=['Find the rule. Write the next numbers.', '23 450,   24 450,   25 450,   ________,   ________']),
    D(id='5b', tier='core', no='5(b)', type='fields', skill='number patterns', frame='81 300,  79 800,  78 300,  {f1},  {f2}', answer=[76800, 75300], check=lambda: next_terms(81300, -1500),
      q='Find the rule. Write the next numbers.', hint='The numbers go down. How much from 81 300 to 79 800?',
      steps=['81 300 - 79 800 = 1500, and 79 800 - 78 300 = 1500. The rule is take away 1500.', '78 300 - 1500 = 76 800, and 76 800 - 1500 = 75 300.'], src=['81 300,   79 800,   78 300,   ________,   ________']),
    D(id='5c', tier='core', no='5(c)', type='fields', skill='number patterns', frame='99 950,  99 960,  99 970,  99 980,  {f1},  {f2}', answer=[99990, 100000], check=lambda: next_terms(99950, 10, have=4),
      q='Find the rule. Write the next numbers.', hint='The rule is add 10. What comes after 99 990?',
      steps=['The numbers grow by 10 each time.', '99 980 + 10 = 99 990, and 99 990 + 10 = 100 000.'], src=['99 950,   99 960,   99 970,   99 980,   ________,   ________']),
    D(id='5d', tier='core', no='5(d)', type='number', skill='number patterns', answer=32500,
      check=lambda: (lambda f: f(f, 12500))(lambda f, v: v if v > 30000 else f(f, v + 2500)),
      q='12 500, 15 000, 17 500, 20 000 ... What is the first number in this pattern that is more than 30 000?', hint='The rule is add 2500. Keep adding until you pass 30 000.',
      steps=['The rule is add 2500: 12 500, 15 000, 17 500, 20 000, 22 500, 25 000, 27 500, 30 000, 32 500.', '30 000 is not more than 30 000, so the first number more than 30 000 is 32 500.'],
      src=['12 500,   15 000,   17 500,   20 000 …   What is the first number in this pattern that is more than 30 000?']),

    D(id='6a', tier='core', no='6(a)', type='number', skill='digit cards', answer=86530, svg=digit_cards([0, 3, 5, 6, 8]),
      check=lambda: max(n for n in card_numbers([0, 3, 5, 6, 8]) if n % 2 == 0),
      q='Use the digit cards 0, 3, 5, 6 and 8 once each to make a 5-digit number. The largest even number:',
      hint='Put the biggest digits at the front, but the last digit must be even.',
      steps=['For the largest number, the biggest digits go first: 8, 6, 5, 3, 0.', '86 530 ends in 0, which is even, so it works.', 'The largest even number is 86 530.'],
      src=['Use the digit cards 0, 3, 5, 6 and 8 once each to make a 5-digit number.', 'The largest even number:']),
    D(id='6b', tier='core', no='6(b)', type='number', skill='digit cards', answer=30685, svg=digit_cards([0, 3, 5, 6, 8]),
      check=lambda: min(n for n in card_numbers([0, 3, 5, 6, 8]) if n % 2 == 1),
      q='Use the digit cards 0, 3, 5, 6 and 8 once each to make a 5-digit number. The smallest odd number:',
      hint='The first digit cannot be 0. The last digit must be odd: 3 or 5.',
      steps=['The ones digit must be odd: 3 or 5. Use 5 so that the 3 can go at the front.', 'The first digit cannot be 0, so use the smallest other digit, 3. Then 0, 6, 8 in order, and 5 at the end.', 'The smallest odd number is 30 685.'],
      src=['The smallest odd number:']),
    D(id='6c', tier='core', no='6(c)', type='number', skill='digit cards', answer=60358, svg=digit_cards([0, 3, 5, 6, 8]),
      check=lambda: min(card_numbers([0, 3, 5, 6, 8]), key=lambda n: abs(n - 60000)),
      q='Use the digit cards 0, 3, 5, 6 and 8 once each to make a 5-digit number. The number closest to 60 000:',
      hint='Start with 6 and 0. Then put the smallest digits next, to stay close to 60 000.',
      steps=['Start with 6 and 0: 60 ___.', 'Use the smallest digits left in order: 3, 5, 8.', '60 358 is 358 above 60 000. A number below 60 000 starts with 58 and is further away (for example 58 630 is 1370 away).'],
      src=['The number closest to 60 000:']),

    # ================= Investigation: Double rounding
    D(id='I1a', tier='invest', no='Investigation (a) 3 280', type='fields', skill='testing a claim about rounding', frame='3 280:  nearest hundred {f1},  then nearest thousand {f2};  straight to the nearest thousand {f3}', answer=[3300, 3000, 3000],
      check=lambda: double_round(3280),
      q='Double rounding. Mei says: "If I round a number to the nearest hundred, and then round that answer to the nearest thousand, I always get the same answer as rounding to the nearest thousand straight away." '
        'Test Mei\'s idea. Easy first step: round 3 280 to the nearest hundred. Then round your answer to the nearest thousand. Now round 3 280 straight to the nearest thousand.',
      hint='Do the two steps one at a time.', steps=['3 280 to the nearest hundred: 3 300.', '3 300 to the nearest thousand: 3 000.', '3 280 straight to the nearest thousand: 3 000. The same both ways.'],
      src=['Double rounding', 'Mei says: "If I round a number to the nearest hundred, and then round that answer to the nearest thousand, I always get the same answer as rounding to the nearest thousand straight away."',
           'Round 3 280 to the nearest hundred. Then round your answer to the nearest thousand. Now round 3 280 straight to the nearest thousand. Did you get the same answer both ways?']),
    D(id='I1b', tier='invest', no='Investigation (a) 1 449', type='fields', skill='testing a claim about rounding', frame='1 449:  nearest hundred {f1},  then nearest thousand {f2};  straight to the nearest thousand {f3}', answer=[1400, 1000, 1000],
      check=lambda: double_round(1449), q='Test Mei\'s idea on 1 449. Round to the nearest hundred, then that answer to the nearest thousand, and then 1 449 straight to the nearest thousand.',
      hint='1 449 is just below the halfway mark 1 450.', steps=['1 449 to the nearest hundred: 1 400.', '1 400 to the nearest thousand: 1 000.', '1 449 straight to the nearest thousand: 1 000. The same both ways.'],
      src=['Include 3 280, 1 449 and 1 450.']),
    D(id='I1c', tier='invest', no='Investigation (a) 1 450', type='fields', skill='testing a claim about rounding', frame='1 450:  nearest hundred {f1},  then nearest thousand {f2};  straight to the nearest thousand {f3}', answer=[1500, 2000, 1000],
      check=lambda: double_round(1450), q='Test Mei\'s idea on 1 450. Round to the nearest hundred, then that answer to the nearest thousand, and then 1 450 straight to the nearest thousand.',
      hint='1 450 to the nearest hundred is 1 500. What does 1 500 round to?', steps=['1 450 to the nearest hundred: 1 500.', '1 500 to the nearest thousand: 2 000.', '1 450 straight to the nearest thousand: 1 000 (the hundreds digit is 4). Different!'],
      src=['Include 3 280, 1 449 and 1 450.']),
    D(id='I2', tier='invest', no='Investigation (b)', type='choice', options=['Yes', 'No'], answer='No', skill='testing a claim about rounding',
      check=lambda: 'No' if BREAK else 'Yes', q='Is Mei always right?', hint='Look at 1 450.',
      steps=['For 1 450 the two ways gave 2 000 and 1 000. So Mei is not always right.', 'Checking every whole number below 100 000 by computer finds many numbers that break her idea.'], src=['Is Mei always right? If not, write one number that breaks her idea.']),
    D(id='I2b', tier='invest', no='Investigation (b) a number', type='selfcheck', open=False, skill='testing a claim about rounding',
      q='Write one number that breaks Mei\'s idea.', facts=1450, check=lambda: 1450 if 1450 in BREAK else None,
      hint='Try a number just below a halfway mark for the thousands, such as one that ends in 450.', steps=['1 450 breaks it: 1 500 then 2 000, but straight to the nearest thousand it is 1 000.', 'Any number whose last three digits are 450 to 499 works.'],
      src=['Is Mei always right? If not, write one number that breaks her idea.']),
    D(id='I3', tier='invest', no='Investigation (c)', type='selfcheck', open=False, skill='testing a claim about rounding',
      q='Look at the numbers that break it. What do their last three digits have in common?', facts=(450, 499), check=lambda: (min(n % 1000 for n in BREAK), max(n % 1000 for n in BREAK)),
      hint='List the numbers that broke the idea and look only at the last three digits.', steps=['Every number whose last three digits are 450 to 499 breaks the idea (checked for every whole number below 100 000).',
             'Why: rounding to the nearest hundred first turns a number just BELOW the halfway mark into exactly the halfway mark, which then rounds up.', 'A strong answer says "I tested ..." before "I think ...".'],
      src=['Look at the numbers that break it. What do their last three digits have in common?']),

    # ================= Think harder
    D(id='T1', tier='stretch', no='Think harder 1', type='number', skill='number riddles', answer=55555,
      check=lambda: [n for n in five_digit_numbers() if len(set(str(n))) == 1 and round_to(n, 10000) == 60000][0],
      q='I am a 5-digit number. All my digits are the same. Rounded to the nearest ten thousand, I am 60 000. Who am I?', hint='Try 66 666 and 55 555. Which rounds to 60 000?',
      steps=['The numbers with all digits the same are 11 111, 22 222, ... 99 999.', '66 666 rounds to 70 000 and 44 444 rounds to 40 000.', '55 555 rounds up to 60 000.'],
      src=['I am a 5-digit number. All my digits are the same. Rounded to the nearest ten thousand, I am 60 000. Who am I?']),
    D(id='T2', tier='stretch', no='Think harder 2', type='number', skill='digit cards', answer=69741,
      check=lambda: min(card_numbers([1, 4, 6, 7, 9]), key=lambda n: abs(n - 70000)),
      q='Use the digit cards 1, 4, 6, 7 and 9 once each. Make the 5-digit number that is closest to 70 000.', svg=digit_cards([1, 4, 6, 7, 9]),
      hint='Try 6 9 7 4 1 (just below 70 000) and 7 1 4 6 9 (just above). Which is closer?',
      steps=['Just below 70 000: 69 741 (259 away).', 'Just above 70 000: 71 469 (1469 away).', '69 741 is closer.'],
      src=['Use the digit cards 1, 4, 6, 7 and 9 once each. Make the 5-digit number that is closest to 70 000.']),
    D(id='T3', tier='stretch', no='Think harder 3', type='fields', skill='number patterns', frame='17 250,  19 500,  21 750,  {f1},  {f2}', answer=[24000, 26250], check=lambda: next_terms(17250, 2250),
      q='Find the rule and write the next two numbers: 17 250, 19 500, 21 750, ____, ____', hint='19 500 - 17 250 = ?', steps=['19 500 - 17 250 = 2250 and 21 750 - 19 500 = 2250. The rule is add 2250.', '21 750 + 2250 = 24 000 and 24 000 + 2250 = 26 250.'],
      src=['Find the rule and write the next two numbers: 17 250, 19 500, 21 750, ____, ____']),
    D(id='T4', tier='stretch', no='Think harder 4', type='number', skill='working backwards from a rounded number', answer=100, check=lambda: len(rounds_to(3000, 4000, 3500, 100)),
      q='How many whole numbers round to 3500 when rounded to the nearest hundred?', hint='Find the smallest and the largest. 3450 is halfway between 3400 and 3500.',
      steps=['The smallest is 3450 (halfway rounds up) and the largest is 3549.', 'From 3450 to 3549 there are 100 numbers.'], src=['How many whole numbers round to 3500 when rounded to the nearest hundred?']),

    # ================= Go further (printed Q5 to Q7)
    D(id='G5', tier='challenge', no='Go further 5', type='number', skill='counting numbers with a digit sum', answer=15, check=lambda: len([n for n in five_digit_numbers() if digit_sum(n) == 3]),
      q='How many 5-digit numbers have digits that add up to 3?', hint='Split by the first digit: 1, 2 or 3. For a first digit of 1, the other digits add up to 2.',
      steps=['First digit 1: the other digits add up to 2: one 2 in one of 4 places (4 ways) or two 1s in 2 of 4 places (6 ways): 10.', 'First digit 2: one 1 in one of 4 places: 4 ways.', 'First digit 3: 30 000, 1 way.', '10 + 4 + 1 = 15.'],
      src=['How many 5-digit numbers have digits that add up to 3?']),
    D(id='G6', tier='challenge', no='Go further 6', type='selfcheck', open=True, skill='making up a riddle',
      q='Make up your own number riddle about a 5-digit number. Use a rounding clue, a clue about the digits and an odd-or-even clue, so that exactly ONE number fits. Check your riddle: list every number that fits the rounding clue, then cross out the ones that break the other clues. Swap riddles with a partner.',
      hint='Start with the number, then write clues that only it fits.', steps=['Riddles will vary. Check that the rounding clue gives the right range and that only one number is left.', 'Model riddle: "Rounded to the nearest thousand I am 30 000. All my digits are different. My digits add up to 12. I am odd." The only number is 30 261.'],
      src=['Make up your own number riddle about a 5-digit number.']),
    D(id='G7', tier='challenge', no='Go further 7', type='fields', skill='palindromes', frame='The next palindrome: {f1}.  That is {f2} km more.', answer=[40004, 11],
      check=lambda: (lambda n: [n, n - 39993])(next(m for m in range(39994, 100000) if is_palindrome(m))),
      q='The distance counter on Mr Tan\'s car shows 39 993 km. This number is a palindrome: it reads the same forwards and backwards. What is the next palindrome the counter will show? How many more kilometres is that?',
      hint='The next palindrome starts with 4 and ends with 4. What is the smallest one?', steps=['Numbers from 39 994 to 39 999 are not palindromes (they would need to end in 93).', 'The next palindrome is 40 004.', '40 004 - 39 993 = 11 km more.'],
      src=['This number is a palindrome: it reads the same forwards and backwards. What is the next palindrome the counter will show? How many more kilometres is that?']),
]

VARIANTS = {
    '3a': dict(
        base=dict(k=5, j=18, n=6),
        tpl=dict(vars=dict(k=[3, 4, 5, 6, 7, 8, 9], j=[8, 12, 18, 25, 30, 42], n=[3, 4, 5, 6, 7, 8]), derive=dict(x='k*1000-j'),
                 q='A bakery bakes {x} buns every day for {n} days. Round {x} to the nearest thousand and estimate the total.', answer='k*1000*n',
                 hint='{x} is close to which thousand? Then multiply that by {n}.', steps=['{x} rounds to {k}000 (the hundreds digit is 9).', 'Estimate: {n} × {k}000 = {ans}.']),
        oracle=lambda e: round_to(e['k'] * 1000 - e['j'], 1000) * e['n']),
    '5a': dict(
        base=dict(a=23450, d=1000),
        tpl=dict(vars=dict(a=[23450, 41200, 56700, 12300, 68900], d=[1000, 2000, 500, 100, 250]), derive=dict(b='a+d', c='a+2*d'),
                 q='Find the rule. Write the next numbers.', frame='{a}, {b}, {c}, {f1}, {f2}', answers=dict(f1='a+3*d', f2='a+4*d'),
                 hint='How much does the number grow from {a} to {b}?', steps=['From {a} to {b} the number grows by {d}. The rule is add {d}.', 'Add {d} to {c} for the next number, then add {d} again.', 'The next numbers are {ans}.']),
        oracle=lambda e: dict(zip(('f1', 'f2'), next_terms(e['a'], e['d'])))),
}
