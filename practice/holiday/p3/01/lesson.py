"""Online practice for Level 3 (Primary 3, ages 8-10) holiday lesson 1: Number Sleuths (Numbers to 10 000).

The questions are the ones printed in the Level 3 holiday workbook (p3/workbook_html.js builds it from p3/content/l1.js: Start here = the lesson's
workbook pages; Think harder 1 to 4 and Go further 5 to 7 = qbank stretch[0..3] and challenge[-3:]; the Take-home pair = deck.takeHome; the
Investigation = p3/gifted.json lesson 1).  Every answer is recomputed by an INDEPENDENT checker below (loops over the numbers and digit cards in the
question, never a copy of the printed answer); build_holiday.py stops if a checker and the printed answer differ.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *      # noqa: E402,F401
from p3lib import *     # noqa: E402,F401

META = dict(level=3, lesson=1, key='p3', title='Number Sleuths', workbook_title='NUMBER SLEUTHS', topic='Numbers to 10 000', strand='Numbers to 10 000',
            sources=['p3/content/l1.js', 'p3/gifted.json'],
            intro=['Digit cards: use each card once in each number. A 4-digit number cannot start with 0.',
                   'You do not need the cut-out digit cards: the cards are drawn on the screen. Use paper for lists and workings, then type the answers here.',
                   'For a list, type the numbers with a comma between them (any order is fine).'])
FIG = figs()
SK = 'Numbers to 10 000'
YN = ['Yes', 'No']


def I(**kw):
    kw.setdefault('strand', SK)
    return kw


def tally_by_first(nums):
    c = {}
    for n in nums:
        c[int(str(n)[0])] = c.get(int(str(n)[0]), 0) + 1
    return c


def next_after(seq_fn, x):
    for v in seq_fn():
        if v > x:
            return v


def gaps_up(first, n):
    """1000, 1001, 1003, 1006, 1010 ...: each gap is 1 bigger than the one before."""
    seq, g = [first], 1
    while len(seq) < n:
        seq.append(seq[-1] + g); g += 1
    return seq


CARDS = [3, 0, 7, 5]
ODD = fournums(CARDS, odd=True)

ITEMS = [
    # ================= Start here (workbook lesson 1, No.1 to No.6)
    I(id='1a', tier='core', no='1(a)', type='number', skill='greatest and smallest from digit cards', answer=7530, svg=FIG['l1_cards_3075'],
      q='Use these digit cards once each to make 4-digit numbers. The greatest number:', check=lambda: max(fournums(CARDS)),
      hint='Put the biggest card in the thousands place, then the next biggest, and so on.',
      steps=['For the greatest number, put the biggest digit in the biggest place.', 'The digits in order from biggest are 7, 5, 3, 0.', 'The greatest number is 7530.'],
      src=['Use these digit cards once each to make 4-digit numbers.', 'The greatest number:']),
    I(id='1b', tier='core', no='1(b)', type='number', skill='greatest and smallest from digit cards', answer=3057, svg=FIG['l1_cards_3075'],
      q='Use these digit cards once each to make 4-digit numbers. The smallest number:', check=lambda: min(fournums(CARDS)),
      hint='A 4-digit number cannot start with 0. Which card is the smallest one you can put first?',
      steps=['0 cannot go first, because 0357 is only a 3-digit number.', 'The smallest card that can go first is 3. Then use the smallest cards that are left: 0, 5, 7.', 'The smallest number is 3057.'],
      src=['The smallest number:']),
    I(id='1c', tier='core', no='1(c)', type='number', skill='odd and even numbers from digit cards', answer=7503, svg=FIG['l1_cards_3075'],
      q='Use these digit cards once each to make 4-digit numbers. The greatest ODD number:', check=lambda: max(ODD),
      hint='An odd number ends in 1, 3, 5, 7 or 9. Choose the ones digit first, then make the rest as big as you can.',
      steps=['The ones digit must be odd: 3, 5 or 7.', 'Try 7 in the ones place. The biggest number from 5, 3, 0 in front is 530, so 5307. Try 3 in the ones place: 7503. Try 5 in the ones place: 7305.', 'The biggest of these is 7503, so the greatest odd number is 7503.'],
      src=['The greatest ODD number:']),
    I(id='1d', tier='core', no='1(d)', type='number', skill='closest number', answer=5037, svg=FIG['l1_cards_3075'],
      q='Use these digit cards once each to make 4-digit numbers. The number closest to 5000:', check=lambda: min(fournums(CARDS), key=lambda n: abs(n - 5000)),
      hint='Look for a number just above 5000 and one just below. Which is nearer?',
      steps=['Start the number with 5. The smallest number that starts with 5 is 5037, which is only 37 more than 5000.', 'The numbers below 5000 start with 3 or 0 and are much further away: the biggest is 3750.', 'The closest number is 5037.'],
      src=['The number closest to 5000:']),
    I(id='1e', tier='core', no='1(e)', type='number', skill='closest number', answer=37, svg=FIG['l1_cards_3075'],
      q='Why is your answer to 1(d) the closest? It is only ____ away from 5000. Type the missing number.', check=lambda: abs(min(fournums(CARDS), key=lambda n: abs(n - 5000)) - 5000),
      hint='Subtract: take 5000 away from your answer to 1(d).',
      steps=['5037 - 5000 = 37.', 'It is only 37 away from 5000.', 'The closest number below 5000 is 3750, which is 1250 away. So 5037 is much closer.'],
      src=['Why is (d) the closest?', 'It is only']),

    I(id='2', tier='core', no='2', type='set', ordered=False, skill='making a list in order', answer=fournums([2, 0, 5, 5]),
      q='Make a list in order. Write ALL the 4-digit numbers you can make with the cards 2, 0, 5, 5. Start with the smallest. Type all the numbers with a comma between them.',
      check=lambda: fournums([2, 0, 5, 5]),
      hint='Fix the first digit. Write all the numbers that start with 2 first, then all the numbers that start with 5. 0 cannot go first.',
      steps=['Starting with 2: the cards left are 0, 5, 5. The numbers are 2055, 2505, 2550.', 'Starting with 5: the cards left are 0, 2, 5. The numbers are 5025, 5052, 5205, 5250, 5502, 5520.', 'There are 9 numbers. Fixing the first digit helps you know you have them all.'],
      src=['Make a list in order. Write ALL the 4-digit numbers you can make with the cards  2,  0,  5,  5.  Start with the smallest.']),
    I(id='2a', tier='core', no='2(a)', type='number', skill='making a list in order', answer=9,
      q='Make a list in order. Write ALL the 4-digit numbers you can make with the cards 2, 0, 5, 5. How many numbers did you find?',
      check=lambda: len(fournums([2, 0, 5, 5])),
      hint='Count the numbers in your list: the ones that start with 2, and the ones that start with 5.',
      steps=['3 numbers start with 2: 2055, 2505, 2550.', '6 numbers start with 5: 5025, 5052, 5205, 5250, 5502, 5520.', '3 + 6 = 9 numbers.'],
      src=['How many numbers did you find?']),
    I(id='2b', tier='core', no='2(b)', type='number', skill='comparing numbers', answer=4,
      q='From your list of numbers made with the cards 2, 0, 5, 5: how many of them are greater than 5200?',
      check=lambda: sum(1 for n in fournums([2, 0, 5, 5]) if n > 5200),
      hint='Look at the numbers that start with 5. Compare the hundreds digit with 2.',
      steps=['The numbers that start with 2 are all less than 5200.', 'Of the numbers that start with 5, these are greater than 5200: 5205, 5250, 5502, 5520.', '5025 and 5052 are less than 5200.', 'So 4 numbers are greater than 5200.'],
      src=['How many of them are greater than 5200?']),

    I(id='3a', tier='core', no='3(a)', type='fields', skill='number patterns', answer=[9550, 9450], frame='9850, 9750, 9650, {f1}, {f2}',
      q='Look for a pattern. Write the next two numbers.', check=lambda: ap(9850, -100, 5)[3:],
      hint='Look at how much the number changes each time. 9850 to 9750 is a change of how much?',
      steps=['Each number is 100 less than the one before.', '9650 - 100 = 9550, and 9550 - 100 = 9450.', 'The next two numbers are 9550 and 9450.'],
      src=['Look for a pattern. Write the next two numbers.', '9850,   9750,   9650,']),
    I(id='3b', tier='core', no='3(b)', type='fields', skill='number patterns', answer=[4567, 5678], frame='1234, 2345, 3456, {f1}, {f2}',
      q='Look for a pattern. Write the next two numbers.', check=lambda: ap(1234, 1111, 5)[3:],
      hint='Work out 2345 - 1234. Is it the same as 3456 - 2345?',
      steps=['2345 - 1234 = 1111 and 3456 - 2345 = 1111. Each number is 1111 more than the one before.', '3456 + 1111 = 4567, and 4567 + 1111 = 5678.', 'The next two numbers are 4567 and 5678.'],
      src=['1234,   2345,   3456,']),
    I(id='3c', tier='core', no='3(c)', type='fields', skill='number patterns', answer=[1015, 1021], frame='1000, 1001, 1003, 1006, 1010, {f1}, {f2}',
      q='Look for a pattern. Write the next two numbers.', check=lambda: gaps_up(1000, 7)[5:],
      hint='This pattern does not add the same number each time. Write the gaps between the numbers.',
      steps=['The gaps are 1, 2, 3, 4. Each gap is 1 bigger than the one before.', 'The next gaps are 5 and 6.', '1010 + 5 = 1015, and 1015 + 6 = 1021.'],
      src=['1000,   1001,   1003,   1006,   1010,']),
    I(id='3d-yes', tier='core', no='3(d)', type='choice', skill='number patterns', options=YN, answer='Yes',
      q='3000, 3250, 3500, 3750, ... Keep going. Will 5000 be in the pattern?',
      check=lambda: 'Yes' if 5000 in ap(3000, 250, 20) else 'No',
      hint='Keep adding 250 until you reach 5000 or go past it. Or count how many 250s are in 5000 - 3000.',
      steps=['Keep adding 250: 3000, 3250, 3500, 3750, 4000, 4250, 4500, 4750, 5000.', '5000 is in the pattern. It is 8 jumps of 250 after 3000.'],
      src=['3000,  3250,  3500,  3750,  …   Keep going. Will 5000 be in the pattern?']),
    I(id='3d-next', tier='core', no='3(d)', type='number', skill='number patterns', answer=5250,
      q='3000, 3250, 3500, 3750, ... Keep going. If 5000 is in the pattern, which number comes right after it?',
      check=lambda: next_after(lambda: ap(3000, 250, 20), 5000),
      hint='Add 250 to 5000.',
      steps=['The pattern adds 250 each time.', '5000 + 250 = 5250.', 'The number right after 5000 is 5250.'],
      src=['Which number comes right after 5000?']),

    I(id='4a', tier='core', no='4(a)', type='number', skill='place value and renaming', answer=5527,
      q='Place value puzzles. 4 thousands, 15 hundreds, 2 tens and 7 ones make ____',
      check=lambda: 4 * 1000 + 15 * 100 + 2 * 10 + 7,
      hint='10 hundreds make 1 thousand. Rename 15 hundreds as 1 thousand and 5 hundreds.',
      steps=['15 hundreds = 1 thousand + 5 hundreds.', 'So there are 4 + 1 = 5 thousands, 5 hundreds, 2 tens and 7 ones.', 'The number is 5527.'],
      src=['Place value puzzles.', '4 thousands, 15 hundreds, 2 tens and 7 ones make']),
    I(id='4b', tier='core', no='4(b)', type='number', skill='place value and renaming', answer=13,
      q='Place value puzzles. 7305 = 6 thousands + ____ hundreds + 5 ones. Type the missing number.',
      check=lambda: [h for h in range(0, 100) if 6 * 1000 + h * 100 + 5 == 7305][0],
      hint='7305 has 7 thousands. But here there are only 6 thousands, so one thousand has been renamed as hundreds.',
      steps=['7305 - 6000 - 5 = 1300.', '1300 is 13 hundreds.', 'So 7305 = 6 thousands + 13 hundreds + 5 ones.'],
      src=['7305  =  6 thousands  +  ______ hundreds  +  5 ones']),
    I(id='4c', tier='core', no='4(c)', type='choice', skill='place value and renaming', options=YN, answer='No',
      q='Mei says that 6 thousands, 0 hundreds and 23 tens is 6023. Is she right?',
      check=lambda: 'Yes' if 6 * 1000 + 0 * 100 + 23 * 10 == 6023 else 'No',
      hint='23 tens is not 23. How much is 23 tens?',
      steps=['23 tens = 230, because 10 tens make 100, so 20 tens make 200, and 3 tens make 30.', '6000 + 0 + 230 = 6230.', 'Mei is not right. The number is 6230, not 6023.'],
      src=['Mei says that 6 thousands, 0 hundreds and 23 tens is 6023. Is she right? Explain.']),
    I(id='4c-why', tier='core', no='4(c) explain', type='selfcheck', open=True, skill='place value and renaming',
      q='Mei says that 6 thousands, 0 hundreds and 23 tens is 6023. Explain in your own words (write it on paper or here), then compare with the answer shown.',
      check=lambda: 6 * 1000 + 0 * 100 + 23 * 10,
      hint='Say what 23 tens is worth.',
      steps=['23 tens = 230, not 23.', '6 thousands + 0 hundreds + 23 tens = 6000 + 230 = 6230.', 'Mei wrote the 23 as if it were ones and tens in the wrong places. A good explanation says that 23 tens is 230.'],
      src=['Is she right? Explain.']),

    I(id='5a', tier='core', no='5(a)', type='number', skill='clue puzzles', answer=6903,
      q='What number am I? Use one clue at a time. Clue 1: I am between 6000 and 7000. Clue 2: My ones digit is half of my thousands digit. Clue 3: My hundreds digit is the sum of my other three digits.',
      check=lambda: (lambda c: c[0] if len(c) == 1 else None)(all_four_digit(
          lambda n: 6000 < n < 7000 and digits(n)[3] * 2 == digits(n)[0] and digits(n)[1] == digits(n)[0] + digits(n)[2] + digits(n)[3])),
      hint='Clue 1 gives the thousands digit. Clue 2 gives the ones digit. Then use clue 3.',
      steps=['Clue 1: the thousands digit is 6.', 'Clue 2: the ones digit is half of 6, which is 3.', 'Clue 3: the hundreds digit is 6 + 3 + the tens digit. The hundreds digit is at most 9, so the tens digit must be 0, and the hundreds digit is 9.', 'The number is 6903. Check: 6 + 0 + 3 = 9.'],
      src=['What number am I? Use one clue at a time.', 'Clue 3:  My hundreds digit is the sum of my other three digits.']),
    I(id='5b', tier='core', no='5(b)', type='fields', skill='clue puzzles', answer=[3201, 1023], frame='Greatest: {f1}   Smallest: {f2}',
      q='(if time) I am a 4-digit ODD number. All my digits are different. My digits add up to 6. What is the greatest number I can be? What is the smallest?',
      check=lambda: (lambda c: [max(c), min(c)])(all_four_digit(lambda n: n % 2 == 1 and len(set(digits(n))) == 4 and sum(digits(n)) == 6)),
      hint='Which four different digits add up to 6? Then the number must end in an odd digit.',
      steps=['The only four different digits that add up to 6 are 0, 1, 2, 3.', 'The number is odd, so it ends in 1 or 3.', 'Greatest: 3201 (ends in 1, the rest as big as possible). Smallest: 1023 (ends in 3, the rest as small as possible, and 0 cannot be first).'],
      src=['(if time) I am a 4-digit ODD number. All my digits are different. My digits add up to 6. What is the greatest number I can be? What is the smallest?']),

    I(id='6', tier='core', no='6', type='set', ordered=False, skill='making a list in order', answer=all_four_digit(lambda n: sum(digits(n)) == 3),
      q='(if time) How many 4-digit numbers have digits that add up to 3? Make a list in order. Start with the biggest thousands digit. Type all the numbers with a comma between them.',
      check=lambda: all_four_digit(lambda n: sum(digits(n)) == 3),
      hint='Take 3 counters and put them in the 4 places. The thousands place needs at least 1. With 3 in the thousands place, the first number is 3000.',
      steps=['Thousands digit 3: 3000.', 'Thousands digit 2: one more counter goes in one of three places: 2100, 2010, 2001.', 'Thousands digit 1: two more counters go in the other places: 1200, 1110, 1101, 1020, 1011, 1002.', 'There are 1 + 3 + 6 = 10 numbers.'],
      src=['(if time) How many 4-digit numbers have digits that add up to 3? Make a list in order. Start with the biggest thousands digit.']),
    I(id='6a', tier='core', no='6(a)', type='number', skill='making a list in order', answer=10,
      q='(if time) How many 4-digit numbers have digits that add up to 3? How many numbers altogether?',
      check=lambda: len(all_four_digit(lambda n: sum(digits(n)) == 3)),
      hint='Count the numbers in your list.',
      steps=['1 number starts with 3, 3 numbers start with 2, and 6 numbers start with 1.', '1 + 3 + 6 = 10.', 'There are 10 numbers altogether.'],
      src=['How many numbers altogether?']),
    I(id='6b', tier='core', no='6(b)', type='fields', skill='making a list in order', answer=[1, 3, 6], frame='Start with 3: {f1}   Start with 2: {f2}   Start with 1: {f3}',
      q='How many start with 3? With 2? With 1?',
      check=lambda: (lambda c: [c[3], c[2], c[1]])(tally_by_first(all_four_digit(lambda n: sum(digits(n)) == 3))),
      hint='Look at your list. Count the numbers in each group.',
      steps=['Start with 3: 3000 (1 number).', 'Start with 2: 2100, 2010, 2001 (3 numbers).', 'Start with 1: 1200, 1110, 1101, 1020, 1011, 1002 (6 numbers).'],
      src=['How many start with 3? With 2? With 1? What do you notice?']),
    I(id='6b-notice', tier='core', no='6(b) notice', type='selfcheck', open=True, skill='noticing patterns',
      q='Look at your three counts in 6(b): starting with 3, then 2, then 1. What do you notice? Write it, then compare with the answer shown.',
      check=lambda: (lambda c: [c[2] - c[3], c[1] - c[2]])(tally_by_first(all_four_digit(lambda n: sum(digits(n)) == 3))),
      hint='Look at how much each count is bigger than the one before.',
      steps=['The counts are 1, 3, 6.', '3 is 2 more than 1, and 6 is 3 more than 3. The counts go up by 2, then by 3.', 'Any true pattern you notice is good.'],
      src=['What do you notice?']),

    # ================= Investigation (Investigation and look back page, No.8)
    I(id='I8a-list', tier='invest', no='Investigation 8(a)', type='set', ordered=False, skill='making a list in order', answer=[n for n in fournums([0, 1, 2, 3]) if str(n)[0] == '1'],
      q='Investigation: What if one card changes? The cards 1, 2, 3, 4 make 24 four-digit numbers: 6 start with each card. Now change the 4 card to a 0, so the cards are 0, 1, 2, 3. Make a list in order of the numbers that start with 1. Type them with a comma between.',
      check=lambda: [n for n in fournums([0, 1, 2, 3]) if str(n)[0] == '1'],
      hint='With the cards 0, 1, 2, 3, write only the numbers that start with 1. Use the cards to help you.',
      steps=['Put 1 first. The cards left are 0, 2, 3.', 'In order: 1023, 1032, 1203, 1230, 1302, 1320.', 'There are 6 numbers.'],
      src=['Make a list in order of the numbers that start with 1. How many are there?', 'Now change the 4 card to a 0, so the cards are 0, 1, 2, 3.']),
    I(id='I8a-count', tier='invest', no='Investigation 8(a)', type='number', skill='making a list in order', answer=6,
      q='With the cards 0, 1, 2, 3, how many 4-digit numbers start with 1?',
      check=lambda: sum(1 for n in fournums([0, 1, 2, 3]) if str(n)[0] == '1'),
      hint='Count the numbers in your list.',
      steps=['The numbers that start with 1 are 1023, 1032, 1203, 1230, 1302, 1320.', 'There are 6 of them.'],
      src=['Make a list in order of the numbers that start with 1. How many are there?']),
    I(id='I8b', tier='invest', no='Investigation 8(b)', type='fields', skill='counting systematically', answer=[6, 6, 0], frame='Start with 2: {f1}   Start with 3: {f2}   Start with 0: {f3}',
      q='With the cards 0, 1, 2, 3: how many 4-digit numbers start with 2? With 3? With 0?',
      check=lambda: (lambda c: [c.get(2, 0), c.get(3, 0), c.get(0, 0)])(tally_by_first(fournums([0, 1, 2, 3]))),
      hint='Fix the first card and arrange the other three cards. How many ways are there for each first card?',
      steps=['Start with 2: the cards left are 0, 1, 3. There are 6 ways to arrange them, so 6 numbers.', 'Start with 3: also 6 numbers.', 'Start with 0: none. 0123 is only a 3-digit number, so 0 cannot go first.'],
      src=['How many start with 2? With 3? With 0?']),
    I(id='I8c', tier='invest', no='Investigation 8(c)', type='number', skill='counting systematically', answer=18,
      q='With the cards 0, 1, 2, 3: how many 4-digit numbers can you make altogether now?',
      check=lambda: len(fournums([0, 1, 2, 3])),
      hint='Add up the numbers for each first card. Can every card go first?',
      steps=['6 start with 1, 6 start with 2 and 6 start with 3.', '6 + 6 + 6 = 18.', 'With the cards 1, 2, 3, 4 there were 24. With 0, 1, 2, 3 there are 18.'],
      src=['How many 4-digit numbers can you make altogether now? What stayed the same? What changed? Why?']),
    I(id='I8c-why', tier='invest', no='Investigation 8(c) explain', type='selfcheck', open=True, skill='explaining why',
      q='The cards 0, 1, 2, 3 make fewer numbers than the cards 1, 2, 3, 4 (which made 24). What stayed the same? What changed? Why? Write your idea, then compare with the answer shown.',
      check=lambda: (len(fournums([1, 2, 3, 4])), len(fournums([0, 1, 2, 3]))),
      hint='Compare the cards 1, 2, 3, 4 with the cards 0, 1, 2, 3. Which numbers can no longer be made?',
      steps=['Same: each of the cards 1, 2, 3 still makes 6 numbers.', 'Changed: 0 cannot go first, so the 6 numbers that would start with that card are lost. 24 - 6 = 18.', 'Why: a 4-digit number cannot start with 0 (0123 is only a 3-digit number).', 'Extension: how many of the 18 numbers are even? There are 10 with the cards 0, 1, 2, 3, and 12 with the cards 1, 2, 3, 4.'],
      src=['What stayed the same? What changed? Why?']),

    # ================= Think harder (workbook Think harder, No.1 to No.4)
    I(id='T1', tier='stretch', no='Think harder 1', type='fields', skill='greatest and smallest from digit cards', answer=[8520, 2085], frame='Greatest even: {f1}   Smallest odd: {f2}',
      q='Use the cards 5, 0, 8, 2 once each. Make the greatest even number and the smallest odd number.',
      check=lambda: [max(fournums([5, 0, 8, 2], even=True)), min(fournums([5, 0, 8, 2], odd=True))],
      hint='An even number ends in 0, 2, 4, 6 or 8. 5 is the only odd card.',
      steps=['Greatest even: the number must end in 0, 2 or 8. Biggest first digits: 8 5 2 0 would be 8520, which ends in 0 (even). So the greatest even number is 8520.', 'Smallest odd: 5 is the only odd card, so it goes last.', 'The smallest first digit is 2 (0 cannot be first), then 0 and 8: 2085.'],
      src=['Use the cards 5, 0, 8, 2 once each. Make the greatest even number and the smallest odd number.']),
    I(id='T2-list', tier='stretch', no='Think harder 2', type='set', ordered=False, skill='making a list in order', answer=fournums([1, 1, 0, 0]),
      q='How many 4-digit numbers can you make with the cards 1, 1, 0, 0? List them. Type the numbers with a comma between.',
      check=lambda: fournums([1, 1, 0, 0]),
      hint='The first digit must be 1. Where can the other 1 go?',
      steps=['The first digit is 1 (0 cannot go first).', 'The other 1 goes in the hundreds, tens or ones place: 1100, 1010, 1001.', 'The numbers are 1001, 1010 and 1100.'],
      src=['How many 4-digit numbers can you make with the cards 1, 1, 0, 0? List them.']),
    I(id='T2-count', tier='stretch', no='Think harder 2', type='number', skill='making a list in order', answer=3,
      q='How many 4-digit numbers can you make with the cards 1, 1, 0, 0?', check=lambda: len(fournums([1, 1, 0, 0])),
      hint='Count the numbers in your list.',
      steps=['The numbers are 1001, 1010 and 1100.', 'There are 3 numbers.'],
      src=['How many 4-digit numbers can you make with the cards 1, 1, 0, 0?']),
    I(id='T3', tier='stretch', no='Think harder 3', type='number', skill='place value and renaming', answer=8306,
      q='A number has 7 thousands, 13 hundreds and 6 ones. What is the number?', check=lambda: 7 * 1000 + 13 * 100 + 6,
      hint='13 hundreds is 1 thousand and 3 hundreds. There are no tens.',
      steps=['13 hundreds = 1 thousand + 3 hundreds.', 'So the number has 8 thousands, 3 hundreds, 0 tens and 6 ones.', '7000 + 1300 + 6 = 8306.'],
      src=['A number has 7 thousands, 13 hundreds and 6 ones. What is the number?']),
    I(id='T4', tier='stretch', no='Think harder 4', type='number', skill='clue puzzles', answer=5222,
      q='I am between 5000 and 6000. My hundreds, tens and ones digits are all the same. My digits add up to 11. What number am I?',
      check=lambda: (lambda c: c[0] if len(c) == 1 else None)(all_four_digit(
          lambda n: 5000 < n < 6000 and len(set(digits(n)[1:])) == 1 and sum(digits(n)) == 11)),
      hint='The thousands digit is 5. The other three digits are the same and add up to 11 - 5.',
      steps=['The thousands digit is 5.', '11 - 5 = 6 is shared by three equal digits: 2 + 2 + 2 = 6.', 'The number is 5222.'],
      src=['I am between 5000 and 6000. My hundreds, tens and ones digits are all the same. My digits add up to 11. What number am I?']),

    # ================= Go further (workbook Go further, No.5 to No.7) and the Take-home pair
    I(id='G5', tier='challenge', no='Go further 5', type='selfcheck', open=True, skill='making up a puzzle',
      q='Make up your own "What number am I?" puzzle. Choose a secret 4-digit number and write 3 or 4 clues about its digits. Check that ONLY ONE number fits all your clues. Then swap with a partner. Do this on paper, then compare with the example shown.',
      check=lambda: all_four_digit(lambda n: 4000 < n < 5000 and digits(n)[1] == digits(n)[0] - 1 and digits(n)[3] == 3 * digits(n)[2] and sum(digits(n)) == 15),
      hint='Pick a secret number first. Write clues that are true for it. Then list every number that fits clue 1, and cross out the ones that break clue 2, and so on.',
      steps=['Answers vary. Check that every clue is true for the secret number, and that the clues together leave only one number.',
             'Example: I am between 4000 and 5000. My hundreds digit is 1 less than my thousands digit. My ones digit is 3 times my tens digit. My digits add up to 15.',
             'The thousands digit is 4 and the hundreds digit is 3. The tens and ones digits add up to 15 - 7 = 8, and the ones digit is 3 times the tens digit, so the digits are 2 and 6.',
             'The only number is 4326.'],
      src=['Make up your own "What number am I?" puzzle. Choose a secret 4-digit number and write 3 or 4 clues about its digits. Check that ONLY ONE number fits all your clues. Then swap with a partner.']),
    I(id='G6', tier='challenge', no='Go further 6', type='fields', skill='clue puzzles', answer=[9810, 3012], frame='Greatest: {f1}   Smallest: {f2}',
      q='A 4-digit number has all different digits. Its thousands digit is the sum of its other three digits. What is the greatest such number? What is the smallest?',
      check=lambda: (lambda c: [max(c), min(c)])(all_four_digit(lambda n: len(set(digits(n))) == 4 and digits(n)[0] == sum(digits(n)[1:]))),
      hint='The thousands digit is at most 9. Which three different digits give the biggest sum that is 9 or less? Which give the smallest sum?',
      steps=['Greatest: the thousands digit is 9, so the other three different digits add up to 9. To make the number as big as possible, use 8, 1, 0 in that order: 9810.', 'Smallest: the smallest sum of three different digits is 0 + 1 + 2 = 3, so the thousands digit is 3. Then the smallest arrangement is 3012.'],
      src=['A 4-digit number has all different digits. Its thousands digit is the sum of its other three digits. What is the greatest such number? What is the smallest?']),
    I(id='G7', tier='challenge', no='Go further 7', type='number', skill='making a list in order', answer=2341,
      q='Mei uses the cards 1, 2, 3, 4 once each to make 4-digit numbers. She lists them all from smallest to greatest. What is the 10th number in her list?',
      check=lambda: fournums([1, 2, 3, 4])[9],
      hint='6 numbers start with 1. Then list the numbers that start with 2 in order.',
      steps=['The numbers that start with 1 are the first 6 in the list.', 'Then the numbers that start with 2: 2134 (7th), 2143 (8th), 2314 (9th), 2341 (10th).', 'The 10th number is 2341.'],
      src=['Mei uses the cards 1, 2, 3, 4 once each to make 4-digit numbers. She lists them all from smallest to greatest. What is the 10th number in her list?']),
    I(id='TH-a', tier='challenge', no='Take-home (a)', type='number', skill='place value and renaming', answer=5950,
      q='Take-home (not for the lesson). What is 100 less than 6050?', check=lambda: 6050 - 100,
      hint='100 less means the hundreds digit goes down by 1. 6050 has 0 hundreds, so rename 1 thousand as 10 hundreds.',
      steps=['6050 = 5 thousands + 10 hundreds + 5 tens.', 'Take away 1 hundred: 5 thousands + 9 hundreds + 5 tens = 5950.'],
      src=['What is 100 less than 6050?']),
    I(id='TH-b', tier='challenge', no='Take-home (b)', type='choice', skill='comparing numbers', options=['7089', '7098'], answer='7098',
      q='Take-home (not for the lesson). Which is greater: 7089 or 7098?', check=lambda: str(max(7089, 7098)),
      hint='Both have 7 thousands and 0 hundreds. Compare the tens.',
      steps=['Thousands: 7 and 7. Hundreds: 0 and 0.', 'Tens: 8 and 9. 9 tens is more than 8 tens.', '7098 is greater than 7089.'],
      src=['Which is greater: 7089 or 7098?']),
]


# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
def _down(start, step, n):
    out, v = [], start
    for _ in range(n):
        out.append(v); v -= step
    return out


def _place(th, h, t, o):
    n = 0
    for _ in range(th): n += 1000
    for _ in range(h): n += 100
    for _ in range(t): n += 10
    for _ in range(o): n += 1
    return n


def _minus100(n):
    for _ in range(100): n -= 1
    return n


VARIANTS = {
    '3a': dict(
        base=dict(a=9850, d=100),
        tpl=dict(vars=dict(a=[9850, 8700, 7250, 6400, 9990], d=[100, 50, 250, 10, 200]), q='Look for a pattern. Write the next two numbers.',
                 frame='{a}, {b}, {c}, {f1}, {f2}', answers=dict(f1='a-3*d', f2='a-4*d'), derive=dict(b='a-d', c='a-2*d'),
                 hint='Look at how much the number changes each time. {a} to {b} is a change of how much?',
                 steps=['Each number is {d} less than the one before.', '{c} - {d} is the first missing number, and then take away {d} again.', 'The next two numbers are {ans}.']),
        oracle=lambda e: (lambda l: dict(f1=l[3], f2=l[4]))(_down(e['a'], e['d'], 5))),
    '4a': dict(
        base=dict(th=4, h=15, t=2, o=7),
        tpl=dict(vars=dict(th=[2, 3, 4, 6], h=[11, 12, 15, 18], t=[0, 1, 2, 5], o=[3, 6, 7, 9]), q='Place value puzzles. {th} thousands, {h} hundreds, {t} tens and {o} ones make ____',
                 answer='1000*th+100*h+10*t+o', hint='10 hundreds make 1 thousand. Rename {h} hundreds as thousands and hundreds.',
                 steps=['10 hundreds make 1 thousand, so {h} hundreds is 1 thousand and the rest in hundreds.', 'Add up the thousands, the hundreds, the tens and the ones.', 'The number is {ans}.']),
        oracle=lambda e: _place(e['th'], e['h'], e['t'], e['o'])),
    '4b': dict(
        base=dict(th=6, h=13, o=5),
        tpl=dict(vars=dict(th=[4, 5, 6, 8], h=[11, 13, 15, 17], o=[2, 5, 7, 9]), q='Place value puzzles. {n} = {th} thousands + ____ hundreds + {o} ones. Type the missing number.',
                 derive=dict(n='1000*th+100*h+o'), answer='h', hint='Take away the thousands and the ones from {n}. What is left is hundreds.',
                 steps=['{n} - {th}000 - {o} is the number left for the hundreds.', 'Divide by 100 to count the hundreds.', 'The missing number is {ans}.']),
        oracle=lambda e: (lambda n: [h for h in range(0, 100) if e['th'] * 1000 + h * 100 + e['o'] == n][0])(_place(e['th'], e['h'], 0, e['o']))),
    'TH-a': dict(
        base=dict(n=6050),
        tpl=dict(vars=dict(n=[6050, 4000, 3205, 9100, 7099, 2010]), q='What is 100 less than {n}?', answer='n-100',
                 hint='100 less means the hundreds digit goes down by 1. If there are 0 hundreds, rename 1 thousand as 10 hundreds.',
                 steps=['Take away 1 hundred from {n}.', 'If there are no hundreds, rename 1 thousand as 10 hundreds first.', 'The answer is {ans}.']),
        oracle=lambda e: _minus100(e['n'])),
}

# ---- inquiry habit (docs/pedagogy/inquiry_skills_explicit.md; levels/habits.json)
ITEMS.insert(max(i for i, x in enumerate(ITEMS) if x['tier'] == 'core') + 1, habit_item('Explain',
    'Which is bigger, 4 302 or 4 032? Write one sentence. Start: I know because ...',
    ['4 302 is bigger.', 'For example: I know because both numbers have 4 thousands, so I look at the hundreds. 4 302 has 3 hundreds and 4 032 has 0 hundreds, so 4 302 is bigger.'],
    'Start at the left. Compare the thousands first, then the hundreds.'))
