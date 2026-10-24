"""Online practice for Level 3 (Primary 3, ages 8-10) holiday lesson 5: Remainder Riddles (Division with remainders).

The questions are the ones printed in the Level 3 holiday workbook (p3/workbook_html.js builds it from p3/content/l5.js: Start here = the lesson's workbook()
pages; Think harder 1 to 4 and Go further 5 to 7 = qbank stretch[0..3] and challenge[-3:]; the Extra pair = deck.takeHome (printed as "Take-home");
the Investigation = p3/gifted.json lesson 5).  Every answer is recomputed by an INDEPENDENT checker below (counting up in the divisor, trying each number, trying each
day), never a copy of the printed answer; build_holiday.py stops if a checker and the printed answer differ.  The picture of the counters and plates is the
workbook's own figure (p3/content/l5.js, via p3/figs_p3_w3.js).
"""
import itertools, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *          # noqa: E402,F401
from p3lib import *         # noqa: E402,F401
from p3lib_w3 import *      # noqa: E402,F401

META = dict(level=3, lesson=5, key='p3', title='Remainder Riddles', workbook_title='REMAINDER RIDDLES', topic='Division', strand='Division',
            sources=['p3/content/l5.js', 'p3/gifted.json'],
            intro=['When we share or make groups, some may be left over. The leftover is called the remainder. It is always smaller than the number we divide by.',
                   'Use counters, draw dots, or count up in a times table on paper to help. Type the answers here.'])
FIG = figs3()
SK = 'Division'


def I(**kw):
    kw.setdefault('strand', SK)
    return kw


def one(solutions):
    """The only solution, or None if there are none or several (a riddle must have exactly one answer)."""
    return solutions[0] if len(solutions) == 1 else None


def rem(n, d):
    return groups_of(n, d)[1]


def find(pred, lo=0, hi=5000):
    for x in range(lo, hi + 1):
        if pred(x):
            return x
    return None


ITEMS = [
    # ================= Start here (workbook lesson 5, No.1 to No.6)
    I(id='1a', tier='core', no='1(a)', type='fields', skill='division with a remainder', answer=[7, 5], svg=FIG['l5_share'], frame=grp('Each friend gets {f1}.      Left over: {f2}'),
      q='Siti shares 47 stickers equally among 6 friends. The picture shows 47 counters and 6 plates. How many stickers does each friend get, and how many are left over? Fill in the boxes.',
      check=lambda: list(groups_of(47, 6)),
      hint='Count in 6s: 6, 12, 18 ... Stop before you pass 47. What is left?',
      steps=['Count in 6s: 6 × 7 = 42, and 6 × 8 = 48 is too many.', 'Each friend gets 7 stickers. 47 - 42 = 5 stickers are left over.', 'Check: 6 × 7 + 5 = 47, and the remainder 5 is smaller than 6.'],
      src=['Siti shares 47 stickers equally among 6 friends.', 'How many stickers does each friend get?', 'How many are left over?']),
    I(id='1b', tier='core', no='1(b)', type='number', skill='the remainder and the next group', answer=1, svg=FIG['l5_share'],
      q='Siti shares 47 stickers equally among 6 friends. What is the smallest number of extra stickers Siti needs so that none are left over? Type the number.',
      check=lambda: find(lambda e: e >= 1 and rem(47 + e, 6) == 0),
      hint='Look at the numbers in the 6 times table. Which is the next one after 47?',
      steps=['Count in 6s: 42, 48. The next number in the 6 times table after 47 is 48.', '48 - 47 = 1.', 'With 1 extra sticker, 48 stickers share equally: 8 each and none left over.'],
      src=['What is the smallest number of extra stickers Siti needs so that none are left over?']),
    I(id='1c', tier='core', no='1(c) wrong', label='1(c) wrong', type='choice', skill='the remainder is smaller than the divisor',
      options=['The remainder 11 is bigger than 7', 'The remainder 11 is too small', '7 × 7 + 11 does not make 60', 'You cannot divide 60 by 7'], answer='The remainder 11 is bigger than 7',
      q='Ben works out 60 ÷ 7. He writes: 60 ÷ 7 = 7 remainder 11. What is wrong?',
      check=lambda: 'The remainder 11 is bigger than 7' if 11 >= 7 else 'The remainder 11 is too small',
      hint='Compare the remainder with the number we are dividing by.',
      steps=['The remainder must be smaller than the number we divide by. 11 is bigger than 7.', 'So another group of 7 still fits: Ben has not finished dividing.', '(7 × 7 + 11 does make 60, so the adding is right. It is the remainder that is too big.)'],
      src=['Ben works out 60 ÷ 7. He writes:', 'What is wrong?']),
    I(id='1c-ans', tier='core', no='1(c) correct', label='1(c) fix', type='fields', skill='division with a remainder', answer=[8, 4], frame=grp('60 ÷ 7 = {f1} remainder {f2}'),
      q='Ben works out 60 ÷ 7. Work out the correct answer. Fill in the boxes.',
      check=lambda: list(groups_of(60, 7)),
      hint='Count in 7s: 7, 14, 21 ... How far can you go without passing 60?',
      steps=['Count in 7s: 7 × 8 = 56, and 7 × 9 = 63 is too many.', '60 - 56 = 4 is left over, and 4 is smaller than 7.', '60 ÷ 7 = 8 remainder 4. Check: 8 × 7 + 4 = 60.'],
      src=['Write the correct answer.']),

    I(id='2a', tier='core', no='2(a)', type='number', skill='what to do with the leftover', answer=9,
      q='Divide. Then decide what to do with the leftover. There are 75 pupils. 1 minibus holds 9 pupils. How many minibuses are needed? Type the number.',
      check=lambda: groups_needed(75, 9),
      hint='Work out 75 ÷ 9. Then think: do the pupils who are left over still need to travel?',
      steps=['75 ÷ 9 = 8 remainder 3, because 9 × 8 = 72.', 'The 3 pupils left over still need a ride, so they need another minibus.', '8 + 1 = 9 minibuses.'],
      src=['75 pupils. 1 minibus holds 9 pupils. How many minibuses?']),
    I(id='2b', tier='core', no='2(b)', type='number', skill='what to do with the leftover', answer=8,
      q='Mei has $60. 1 book costs $7. How many books can Mei buy? Type the number.',
      check=lambda: groups_of(60, 7)[0],
      hint='Work out 60 ÷ 7. Can Mei buy a book with the money that is left over?',
      steps=['60 ÷ 7 = 8 remainder 4, because 7 × 8 = 56.', 'The $4 left over is not enough for another book.', 'Mei can buy 8 books.'],
      src=['$60. 1 book costs $7. How many books can Mei buy?']),
    I(id='2c', tier='core', no='2(c)', type='number', skill='what to do with the leftover', answer=14,
      q='There are 87 eggs. 1 box holds 6 eggs. How many boxes are FULL? Type the number.',
      check=lambda: groups_of(87, 6)[0],
      hint='Count in 6s without going past 87. How many boxes did you fill?',
      steps=['87 ÷ 6 = 14 remainder 3, because 6 × 14 = 84.', 'The 3 eggs left over do not fill a box.', '14 boxes are full.'],
      src=['87 eggs. 1 box holds 6 eggs. How many boxes are FULL?']),
    I(id='2d', tier='core', no='2(d)', type='number', skill='what to do with the leftover', answer=15,
      q='There are 87 eggs. 1 box holds 6 eggs. How many boxes hold ALL the eggs? Type the number.',
      check=lambda: groups_needed(87, 6),
      hint='Think about the eggs that do not fill a whole box. Do they still need a box?',
      steps=['87 ÷ 6 = 14 remainder 3.', 'The 3 eggs left over still need a box.', '14 + 1 = 15 boxes hold all the eggs.'],
      src=['How many boxes hold ALL the eggs?']),

    I(id='3a', tier='core', no='3(a)', type='number', skill='working backwards from groups and leftover', answer=101,
      q='Ravi packs marbles into bags of 8. He fills 12 bags and has 5 marbles left over. How many marbles does Ravi have? Type the number. (Draw a picture on paper to help if you like.)',
      check=lambda: sum(8 for _ in range(12)) + 5,
      hint='Find how many marbles are in the 12 full bags first. Then add the leftover marbles.',
      steps=['12 bags of 8 marbles: 12 × 8 = 96 marbles.', 'Add the 5 marbles left over: 96 + 5 = 101.', 'Ravi has 101 marbles.'],
      src=['Ravi packs marbles into bags of 8 (draw them to help). He fills 12 bags and has 5 marbles left over.', 'How many marbles does Ravi have?']),
    I(id='3b', tier='core', no='3(b)', type='fields', skill='working backwards from groups and leftover', answer=[11, 2], frame=grp('Full bags: {f1}      Left over: {f2}'),
      q='(if time) Ravi packs marbles into bags of 8. He fills 12 bags and has 5 marbles left over. He tips them all out and packs them again into bags of 9. How many full bags does he get, and how many marbles are left over? Fill in the boxes.',
      check=lambda: list(groups_of(sum(8 for _ in range(12)) + 5, 9)),
      hint='First find how many marbles Ravi has in all. Then count in 9s without going past that number.',
      steps=['Ravi has 12 × 8 + 5 = 101 marbles.', 'Count in 9s: 9 × 11 = 99, and 9 × 12 = 108 is too many.', '11 full bags, and 101 - 99 = 2 marbles are left over.'],
      src=['(if time) He tips them all out and packs them again into bags of 9. How many full bags does he get? How many marbles are left over?']),

    I(id='4-list', tier='core', no='4(a) list', label='4(a) list', type='set', ordered=False, grouped=False, skill='making a list', answer=[43, 48, 53, 58],
      q='What number am I? Make a list, then test each number. I am between 40 and 60. When I am divided by 5, the remainder is 3. First list ALL the numbers between 40 and 60 that leave a remainder of 3 when divided by 5. Type them with commas.',
      check=lambda: [n for n in range(41, 60) if rem(n, 5) == 3],
      hint='Think of the 5 times table near 40 to 60. Which numbers are 3 more than a number in the table?',
      steps=['The 5 times table from 40 to 60: 40, 45, 50, 55, 60.', 'A number with remainder 3 is 3 more than one of these: 43, 48, 53, 58.', 'Check: 43 = 8 × 5 + 3, 48 = 9 × 5 + 3, 53 = 10 × 5 + 3, 58 = 11 × 5 + 3.'],
      src=['I am between 40 and 60. When I am divided by 5, the remainder is 3.', 'Remainder 3 when ÷ 5']),
    I(id='4-iam', tier='core', no='4(a) I am', label='4(a) I am', type='number', skill='making a list', answer=53,
      q='What number am I? I am between 40 and 60. When I am divided by 5, the remainder is 3. When I am divided by 4, the remainder is 1. Type the number.',
      check=lambda: one([n for n in range(41, 60) if rem(n, 5) == 3 and rem(n, 4) == 1]),
      hint='Make a list of the numbers that fit the first clue. Then test each one with the second clue.',
      steps=['Numbers between 40 and 60 with remainder 3 when divided by 5: 43, 48, 53, 58.', 'Divide each by 4: 43 gives remainder 3, 48 gives 0, 53 gives 1, 58 gives 2.', 'Only 53 leaves a remainder of 1. I am 53.'],
      src=['When I am divided by 4, the remainder is 1.', 'Remainder when ÷ 4', 'I am:']),
    I(id='4b', tier='core', no='4(b)', type='set', ordered=False, grouped=False, skill='making a list', answer=[11, 23, 35, 47],
      q='(if time) I am a 2-digit number less than 50. When I am divided by 6, the remainder is 5. When I am divided by 4, the remainder is 3. Find ALL the numbers I could be. Type them with commas.',
      check=lambda: [n for n in range(10, 50) if rem(n, 6) == 5 and rem(n, 4) == 3],
      hint='List the 2-digit numbers that leave 5 when divided by 6. Then test each one with the other clue.',
      steps=['2-digit numbers less than 50 with remainder 5 when divided by 6: 11, 17, 23, 29, 35, 41, 47.', 'Divide each by 4: 11, 23, 35 and 47 leave 3 (17, 29 and 41 leave 1).', 'The numbers are 11, 23, 35 and 47. They go up by 12 each time.'],
      src=['(if time) I am a 2-digit number less than 50. When I am divided by 6, the remainder is 5. When I am divided by 4, the remainder is 3. Find ALL the numbers I could be.']),

    I(id='5a', tier='core', no='5(a)', type='set', ordered=False, grouped=False, skill='the biggest remainder', answer=[0, 1, 2, 3, 4, 5, 6, 7],
      q='Dividing by 8. Write ALL the remainders you could get when you divide a number by 8. (A remainder of 0 means nothing is left over.) Type them with commas.',
      check=lambda: sorted({rem(n, 8) for n in range(8, 200)}),
      hint='Share 9, 10, 11, 12 ... counters into groups of 8. What is left over each time? When does the pattern start again?',
      steps=['Try the numbers one after the other: 8 leaves 0, 9 leaves 1, 10 leaves 2, and so on up to 15 leaves 7.', '16 leaves 0 again, so the pattern repeats.', 'The remainders are 0, 1, 2, 3, 4, 5, 6 and 7. A remainder can never be 8 or more, because then another group of 8 would fit.'],
      src=['Write ALL the remainders you could get when you divide a number by 8.', 'share 9, 10, 11, … counters into groups of 8. What is left over each time?']),
    I(id='5b', tier='core', no='5(b)', type='number', skill='the biggest remainder', answer=63,
      q='A number between 60 and 70 is divided by 8. The remainder is as big as it can be. What is the number? Type the number.',
      check=lambda: one([n for n in range(61, 70) if rem(n, 8) == max(rem(m, 8) for m in range(0, 400))]),
      hint='What is the biggest remainder you can get when you divide by 8? Which number between 60 and 70 leaves it?',
      steps=['The biggest remainder when dividing by 8 is one less than 8.', 'The 8 times table near 60 to 70: 56 and 64. The number just before 64 is the one with the biggest remainder.', '63 = 7 × 8 + 7. The number is 63. (Check: 61 leaves 5, 62 leaves 6, 65 leaves 1, and so on.)'],
      src=['A number between 60 and 70 is divided by 8. The remainder is as big as it can be. What is the number?']),

    I(id='6-row1', tier='core', no='6 table 1', label='6 table 1', type='fields', skill='making a table', answer=[17, 23, 29, 35, 41],
      frame=grp('2 tables: {f1}   3 tables: {f2}   4 tables: {f3}   5 tables: {f4}   6 tables: {f5}'),
      q='(if time) Children sit at tables. With 6 children at each table, 5 children have no seat. With 1 table there are 11 children. Each new table adds 6 children. How many children are there with 2, 3, 4, 5 and 6 tables? Fill in the boxes.',
      check=lambda: (lambda row: row[1:])([(lambda n: sum(6 for _ in range(n)) + 5)(n) for n in range(1, 7)]),
      hint='Start from 11 and add 6 for each new table.',
      steps=['1 table: 11 children. Add 6 for each new table.', '2 tables: 17. 3 tables: 23. 4 tables: 29. 5 tables: 35. 6 tables: 41.', 'Check: 4 tables is 4 × 6 + 5 = 29.'],
      src=['At a class party, children sit at tables. If 6 children sit at each table, 5 children have no seat.', 'Hint: fill in the table. Each new table adds 6 children in the first row and 7 in the second.']),
    I(id='6-row2', tier='core', no='6 table 2', label='6 table 2', type='fields', skill='making a table', answer=[14, 21, 28, 35, 42],
      frame=grp('2 tables: {f1}   3 tables: {f2}   4 tables: {f3}   5 tables: {f4}   6 tables: {f5}'),
      q='(if time) Children sit at tables. With 7 children at each table, every seat is filled. With 1 table there are 7 children. Each new table adds 7 children. How many children are there with 2, 3, 4, 5 and 6 tables? Fill in the boxes.',
      check=lambda: [sum(7 for _ in range(n)) for n in range(2, 7)],
      hint='Start from 7 and add 7 for each new table. These are numbers in the 7 times table.',
      steps=['1 table: 7 children. Add 7 for each new table.', '2 tables: 14. 3 tables: 21. 4 tables: 28. 5 tables: 35. 6 tables: 42.', 'These are the 7 times table.'],
      src=['If 7 children sit at each table, every seat is filled and nobody is left over.', 'Each new table adds 6 children in the first row and 7 in the second.', 'Children: 7 at each table']),
    I(id='6a', tier='core', no='6(a)', type='fields', skill='making a table', answer=[5, 35], frame=grp('Tables: {f1}      Children: {f2}'),
      q='(if time) At a class party, children sit at tables. If 6 children sit at each table, 5 children have no seat. If 7 children sit at each table, every seat is filled and nobody is left over. How many tables are there, and how many children? Fill in the boxes.',
      check=lambda: (lambda n: [n, 7 * n])(one([n for n in range(1, 200) if 6 * n + 5 == 7 * n])),
      hint='Work out the number of children for 2, 3, 4 ... tables both ways. Look for the number of tables where both ways give the same number of children.',
      steps=['6 at each table with 5 left: 11, 17, 23, 29, 35 children for 1, 2, 3, 4, 5 tables.', '7 at each table: 7, 14, 21, 28, 35 children for 1, 2, 3, 4, 5 tables.', 'Both rows show 35 when there are 5 tables. So there are 5 tables and 35 children. (6 × 5 + 5 = 35 and 7 × 5 = 35.)'],
      src=['How many tables are there?', 'How many children?']),
    I(id='6b', tier='core', no='6(b)', type='number', skill='making a table', answer=5,
      q='(if time) At a class party, if 6 children sit at each table, 5 children have no seat. If 7 children sit at each table, every seat is filled and nobody is left over. If 8 children sit at each table instead, how many seats are empty? Type the number.',
      check=lambda: (lambda n: 8 * n - (6 * n + 5))(one([n for n in range(1, 200) if 6 * n + 5 == 7 * n])),
      hint='Find the number of tables and the number of children first. Then find how many seats there are with 8 at each table.',
      steps=['There are 5 tables and 35 children.', 'With 8 seats at each table there are 5 × 8 = 40 seats.', '40 - 35 = 5 seats are empty.'],
      src=['If 8 children sit at each table instead, how many seats are empty?']),

    # ================= Investigation (Investigation and look back page, No.8: Is it always true? Three in a row)
    I(id='I8-easy', tier='invest', no='8 easy', label='Inv easy', type='number', skill='multiples in a row', answer=21,
      q='Is it always true? Write any three whole numbers in a row, like 14, 15, 16. Exactly one of them is in the 3 times table. Easy first step: which of the numbers 20, 21 and 22 is in the 3 times table? Type the number.',
      check=lambda: one([n for n in (20, 21, 22) if rem(n, 3) == 0]),
      hint='Say the 3 times table: 3, 6, 9, 12 ... Which of the three numbers do you meet?',
      steps=['Count in 3s: ..., 15, 18, 21, 24.', '21 is in the 3 times table. 20 and 22 are not (20 = 6 × 3 + 2, 22 = 7 × 3 + 1).'],
      src=['Easy first step: circle the number in the 3 times table in 14, 15, 16. Then try 20, 21, 22.']),
    I(id='I8a-tries', tier='invest', no='8(a) tries', label='Inv 8a tries', type='fields', skill='multiples in a row', answer=[9, 27, 63, 120, 153],
      frame=grp('7, 8, 9: {f1}   25, 26, 27: {f2}   61, 62, 63: {f3}   118, 119, 120: {f4}   152, 153, 154: {f5}'),
      q='Is it always true? Take three numbers in a row. For each group of three, write the one number that is in the 3 times table.',
      check=lambda: [one([n for n in (s, s + 1, s + 2) if rem(n, 3) == 0]) for s in (7, 25, 61, 118, 152)],
      hint='For each group, check the three numbers one at a time: divide by 3 and see if anything is left over.',
      steps=['A number is in the 3 times table when nothing is left over after dividing by 3.', '7, 8, 9: 9. 25, 26, 27: 27. 61, 62, 63: 63. 118, 119, 120: 120. 152, 153, 154: 153.', 'Each group of three had exactly one, even the groups with numbers bigger than 100.'],
      src=['Try 5 different starting numbers (make one of them bigger than 100). Circle the number in the 3 times table each time. Is it always exactly one?']),
    I(id='I8a-always', tier='invest', no='8(a) always?', label='Inv 8a yes?', type='choice', skill='multiples in a row',
      options=['Yes, exactly one every time', 'No, sometimes none or two'], answer='Yes, exactly one every time',
      q='Is it always true? Look at three whole numbers in a row, and the 3 times table. Is exactly one of the three numbers in the 3 times table every time?',
      check=lambda: 'Yes, exactly one every time' if all(len([n for n in (s, s + 1, s + 2) if rem(n, 3) == 0]) == 1 for s in range(0, 1000)) else 'No, sometimes none or two',
      hint='Try several different starting numbers. Did you ever find none, or two?',
      steps=['Try any three numbers in a row: you always find exactly one in the 3 times table.', 'It never happens that there are none or two. (Checked for every starting number up to 1000.)'],
      src=['Is it always exactly one?']),
    I(id='I8b-why', tier='invest', no='8(b) why', label='Inv 8b why', type='selfcheck', open=True, marking_mode='self', skill='explaining why',
      q='Explain why exactly one of three numbers in a row is in the 3 times table. Think about the remainders when you divide by 3. Write your idea, then compare with the answer shown.',
      check=lambda: all(sorted(rem(n, 3) for n in (s, s + 1, s + 2)) == [0, 1, 2] for s in range(0, 1000)),
      hint='What are the remainders when you divide 1, 2, 3, 4, 5, 6 by 3? Look at what repeats.',
      steps=['When you divide by 3 the remainders go 1, 2, 0, 1, 2, 0 and so on.', 'In any three numbers in a row, each of the remainders 0, 1 and 2 appears exactly once.', 'The number with remainder 0 is in the 3 times table. So there is always exactly one.'],
      src=['Explain why. Think about the remainders when you divide by 3.']),
    I(id='I8c-four', tier='invest', no='8(c) four', label='Inv 8c x4', type='fields', skill='multiples in a row', answer=[12, 24, 36],
      frame=grp('10, 11, 12, 13: {f1}   21, 22, 23, 24: {f2}   33, 34, 35, 36: {f3}'),
      q='What if we change it? Now take FOUR numbers in a row and the 4 times table. For each group of four, write the one number that is in the 4 times table.',
      check=lambda: [one([n for n in range(s, s + 4) if rem(n, 4) == 0]) for s in (10, 21, 33)],
      hint='For each group, divide the four numbers by 4 one at a time. Which one leaves nothing over?',
      steps=['10, 11, 12, 13: 12 is in the 4 times table (3 × 4).', '21, 22, 23, 24: 24 (6 × 4). 33, 34, 35, 36: 36 (9 × 4).'],
      src=['Try 4 numbers in a row and the 4 times table.']),
    I(id='I8c-four-always', tier='invest', no='8(c) four always?', label='Inv 8c4 yes?', type='choice', skill='multiples in a row',
      options=['Yes, exactly one every time', 'No, sometimes none or two'], answer='Yes, exactly one every time',
      q='What if we change it? Take FOUR numbers in a row and the 4 times table. Is exactly one of the four numbers in the 4 times table every time?',
      check=lambda: 'Yes, exactly one every time' if all(len([n for n in range(s, s + 4) if rem(n, 4) == 0]) == 1 for s in range(0, 1000)) else 'No, sometimes none or two',
      hint='Try some more groups of four. Look at the remainders when you divide by 4.',
      steps=['Dividing by 4 the remainders go 0, 1, 2, 3, 0, 1, 2, 3 ...', 'In any four numbers in a row each remainder appears exactly once, so there is always exactly one number in the 4 times table.'],
      src=['Try 4 numbers in a row and the 4 times table.']),
    I(id='I8c-two', tier='invest', no='8(c) two', label='Inv 8c x2', type='fields', skill='multiples in a row', answer=[1, 0, 1, 0],
      frame=grp('3, 4: {f1}   4, 5: {f2}   5, 6: {f3}   7, 8: {f4}'),
      q='What if we change it? Now take only TWO numbers in a row and the 3 times table. For each pair, how many of the two numbers are in the 3 times table? Write 0, 1 or 2.',
      check=lambda: [len([n for n in pair if rem(n, 3) == 0]) for pair in ((3, 4), (4, 5), (5, 6), (7, 8))],
      hint='For each pair, divide both numbers by 3. Count the ones that leave nothing over.',
      steps=['3 and 4: 3 is in the table, so 1.', '4 and 5: neither is in the table, so 0.', '5 and 6: 6 is in the table, so 1. 7 and 8: neither, so 0.'],
      src=['Then try only 2 numbers in a row and the 3 times table.']),
    I(id='I8c-two-always', tier='invest', no='8(c) two always?', label='Inv 8c2 yes?', type='choice', skill='multiples in a row',
      options=['Yes, exactly one every time', 'No, sometimes none'], answer='No, sometimes none',
      q='What if we change it? Take only TWO numbers in a row and the 3 times table. Is exactly one of the two numbers in the 3 times table every time?',
      check=lambda: 'Yes, exactly one every time' if all(len([n for n in (s, s + 1) if rem(n, 3) == 0]) == 1 for s in range(0, 1000)) else 'No, sometimes none',
      hint='Try several pairs. Look for a pair with none of the numbers in the 3 times table.',
      steps=['Some pairs have one number in the 3 times table, like 3 and 4.', '4 and 5 have none. So it is not always exactly one.', 'In general, n numbers in a row always have exactly one number in the n times table. Two numbers in a row and the 3 times table is not that rule.'],
      src=['Then try only 2 numbers in a row and the 3 times table.']),

    # ================= Think harder (workbook Think harder, No.1 to No.4)
    I(id='T1', tier='stretch', no='T1', type='fields', skill='remainders in a story', answer=[6, 3], frame=grp('Bracelets: {f1}      More beads needed: {f2}'),
      q='Mei has 53 beads. She makes bracelets with 8 beads each. How many bracelets can she make, and how many more beads does she need to make one more bracelet? Fill in the boxes.',
      check=lambda: (lambda g: [g[0], 8 - g[1]])(groups_of(53, 8)),
      hint='Count in 8s without going past 53. For the second part, how many beads short of the next bracelet is she?',
      steps=['53 ÷ 8 = 6 remainder 5, because 8 × 6 = 48.', 'She can make 6 bracelets, with 5 beads left over.', 'One more bracelet needs 8 beads. She has 5, so she needs 8 - 5 = 3 more.'],
      src=['Mei has 53 beads. She makes bracelets with 8 beads each. How many bracelets can she make? How many more beads does she need to make one more bracelet?']),
    I(id='T2', tier='stretch', no='T2', type='number', skill='riddles with two clues', answer=23,
      q='I am a number between 20 and 30. When I am divided by 4, the remainder is 3. When I am divided by 6, the remainder is 5. What number am I? Type the number.',
      check=lambda: one([n for n in range(21, 30) if rem(n, 4) == 3 and rem(n, 6) == 5]),
      hint='List the numbers between 20 and 30 that fit one clue. Then test each with the other clue.',
      steps=['Remainder 3 when divided by 4: 23 and 27.', '23 ÷ 6 = 3 remainder 5. 27 ÷ 6 = 4 remainder 3.', 'Only 23 fits both clues. I am 23.'],
      src=['I am a number between 20 and 30. When I am divided by 4, the remainder is 3. When I am divided by 6, the remainder is 5. What number am I?']),
    I(id='T3', tier='stretch', no='T3', type='number', skill='the biggest remainder', answer=98,
      q='What is the biggest 2-digit number that leaves a remainder of 8 when it is divided by 9? Type the number.',
      check=lambda: max(n for n in range(10, 100) if rem(n, 9) == 8),
      hint='Numbers with remainder 8 are 8 more than a number in the 9 times table. Find the biggest one that still has 2 digits.',
      steps=['The 9 times table near 100: 81, 90, 99.', '90 + 8 = 98 has remainder 8 and 2 digits. 99 + 8 = 107 has 3 digits.', '98 ÷ 9 = 10 remainder 8. The number is 98. (99 is in the 9 times table with no remainder.)'],
      src=['What is the biggest 2-digit number that leaves a remainder of 8 when it is divided by 9?']),
    I(id='T4', tier='stretch', no='T4', type='number', skill='what to do with the leftover', answer=12,
      q='A boat can carry 9 people at a time. 100 people want to cross the river. How many boatloads are needed? Type the number.',
      check=lambda: groups_needed(100, 9),
      hint='Work out 100 ÷ 9. What happens to the people who are left over?',
      steps=['100 ÷ 9 = 11 remainder 1, because 9 × 11 = 99.', 'The 1 person left over still needs a boat.', '11 + 1 = 12 boatloads.'],
      src=['A boat can carry 9 people at a time. 100 people want to cross the river. How many boatloads are needed?']),

    # ================= Go further (workbook Go further, No.5 to No.7) and the Extra pair (printed as "Take-home")
    I(id='G5', tier='challenge', no='G5', type='selfcheck', open=True, marking_mode='open', skill='making up a riddle',
      q='Make up your own remainder riddle: "I am a number between ___ and ___. When I am divided by ___ the remainder is ___. When I am divided by ___ the remainder is ___." Check that only ONE number fits, by listing the numbers for the first clue and testing them. Read it to a partner or a grown-up.',
      check=lambda: [[n for n in range(21, 50) if rem(n, 5) == 2 and rem(n, 6) == 4], [n for n in range(21, 60) if rem(n, 5) == 2 and rem(n, 6) == 4]],
      hint='Pick a number first, like 22. Write down its remainders for two different divisors. Then build the clues around it. Is it the only number in your range?',
      steps=['Answers vary. Check that the number fits both clues, and that it is the only one.', 'Example: "I am between 20 and 50. Divided by 5 the remainder is 2. Divided by 6 the remainder is 4." Only 22 fits (22 = 4 × 5 + 2 = 3 × 6 + 4).', 'Careful with the range: between 20 and 60, 52 would fit as well, and then the riddle has two answers.'],
      src=['Make up your own remainder riddle:', 'Check that only ONE number fits, by listing the numbers for the first clue and testing them.']),
    I(id='G6-after', tier='challenge', no='G6 after', label='G6 after', type='text', skill='remainders and the days of the week', accept=['Wednesday', 'Wed'], shown='Wednesday',
      q='Today is Monday. What day of the week will it be 100 days from today? Type the day.',
      check=lambda: day_after('Monday', 100),
      hint='How many days make a week? Count in 7s up to 100. How many days are left over?',
      steps=['A week has 7 days. 100 ÷ 7 = 14 remainder 2, because 7 × 14 = 98.', 'After 14 weeks (98 days) it is Monday again.', '2 more days: Tuesday, then Wednesday. It will be Wednesday.'],
      src=['Today is Monday. What day of the week will it be 100 days from today? What day of the week was it 100 days ago? Explain how you know.']),
    I(id='G6-before', tier='challenge', no='G6 ago', label='G6 ago', type='text', skill='remainders and the days of the week', accept=['Saturday', 'Sat'], shown='Saturday',
      q='Today is Monday. What day of the week was it 100 days ago? Type the day.',
      check=lambda: day_after('Monday', -100),
      hint='Go back in whole weeks first. How many days are left to go back after that?',
      steps=['100 ÷ 7 = 14 remainder 2.', 'Go back 14 weeks (98 days): it was a Monday.', 'Go back 2 more days: Sunday, then Saturday. It was Saturday.'],
      src=['What day of the week was it 100 days ago?']),
    I(id='G6-why', tier='challenge', no='G6 explain', label='G6 explain', type='selfcheck', open=True, marking_mode='self', skill='explaining why',
      q='Today is Monday. Explain how you know the day of the week 100 days from today and 100 days ago. Write your idea, then compare with the answer shown.',
      check=lambda: [groups_of(100, 7), day_after('Monday', 100), day_after('Monday', -100)],
      hint='A week has 7 days. How many whole weeks are in 100 days, and how many days are left over?',
      steps=['100 ÷ 7 = 14 remainder 2. Whole weeks bring you back to the same day, so only the 2 leftover days matter.', 'Forward: Monday + 2 days = Wednesday.', 'Back: Monday - 2 days = Saturday.'],
      src=['Explain how you know.']),
    I(id='G7', tier='challenge', no='G7', type='fields', skill='working backwards from groups and leftover', answer=[7, 38], frame=grp('Pupils: {f1}      Pens: {f2}'),
      q='Mr Lim gives pens to his pupils. If each pupil gets 4 pens, 10 pens are left over. If each pupil gets 6 pens, he is 4 pens short. How many pupils are there, and how many pens does Mr Lim have? Fill in the boxes.',
      check=lambda: (lambda p: [p, 4 * p + 10])(one([p for p in range(1, 500) if 4 * p + 10 == 6 * p - 4])),
      hint='Compare the two plans. How many more pens does each pupil get in the second plan? How many more pens in all does that need?',
      steps=['In the second plan each pupil gets 2 more pens. That needs the 10 leftover pens plus 4 more: 10 + 4 = 14 pens.', '14 pens ÷ 2 pens each = 7 pupils.', 'Mr Lim has 7 × 4 + 10 = 38 pens. Check: 7 × 6 = 42 = 38 + 4.'],
      src=['Mr Lim gives pens to his pupils. If each pupil gets 4 pens, 10 pens are left over. If each pupil gets 6 pens, he is 4 pens short. How many pupils are there? How many pens does he have?']),
    I(id='TH-a', tier='challenge', no='Extra (a)', type='fields', skill='division with a remainder', answer=[6, 2], frame=grp('50 ÷ 8 = {f1} remainder {f2}'),
      q='Extra practice (not for the lesson). Fill in the boxes.',
      check=lambda: list(groups_of(50, 8)),
      hint='Count in 8s: 8, 16, 24 ... Stop before you pass 50.',
      steps=['8 × 6 = 48, and 8 × 7 = 56 is too many.', '50 - 48 = 2.', '50 ÷ 8 = 6 remainder 2.'],
      src=['50 ÷ 8']),
    I(id='TH-b', tier='challenge', no='Extra (b)', type='fields', skill='division with a remainder', answer=[7, 0], frame=grp('63 ÷ 9 = {f1} remainder {f2}'),
      q='Extra practice (not for the lesson). Fill in the boxes. (Write 0 if nothing is left over.)',
      check=lambda: list(groups_of(63, 9)),
      hint='Count in 9s: 9, 18, 27 ... Does 63 come up?',
      steps=['9 × 7 = 63 exactly.', 'Nothing is left over, so the remainder is 0.', '63 ÷ 9 = 7 remainder 0.'],
      src=['63 ÷ 9']),
]


# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
def _n(e):
    return e['q'] * e['k'] + e['r']


VARIANTS = {
    '1a': dict(
        base=dict(q=7, k=6, r=5),
        tpl=dict(vars=dict(q=[6, 7, 9], k=[5, 6, 7, 8], r=[1, 2, 3, 4]), derive=dict(N='q*k+r'),
                 q='Siti shares {N} stickers equally among {k} friends. How many stickers does each friend get, and how many are left over? Fill in the boxes.',
                 frame=grp('Each friend gets {f1}.      Left over: {f2}'), answers=dict(f1='N//k', f2='N%k'),
                 hint='Count in {k}s. Stop before you pass {N}. What is left?',
                 steps=['Count in {k}s: how many times can you go without passing {N}?', 'That is how many each friend gets. What remains is the leftover.', 'The answers are {ans}.']),
        oracle=lambda e: dict(zip(('f1', 'f2'), groups_of(_n(e), e['k'])))),
    '1b': dict(
        base=dict(q=7, k=6, r=5),
        tpl=dict(vars=dict(q=[6, 7, 9], k=[5, 6, 7, 8], r=[1, 2, 3, 4]), derive=dict(N='q*k+r'),
                 q='Siti shares {N} stickers equally among {k} friends. What is the smallest number of extra stickers Siti needs so that none are left over? Type the number.',
                 answer='k-N%k', hint='Look at the numbers in the {k} times table. Which is the next one after {N}?',
                 steps=['Count in {k}s until you pass {N}. That next number in the {k} times table is the amount needed.', 'Take {N} away from it.', 'Siti needs {ans} extra.']),
        oracle=lambda e: find(lambda x: x >= 1 and rem(_n(e) + x, e['k']) == 0)),
    '2a': dict(
        base=dict(q=8, k=9, r=3),
        tpl=dict(vars=dict(q=[6, 8, 9], k=[7, 8, 9, 10], r=[1, 2, 3]), derive=dict(N='q*k+r'),
                 q='Divide. Then decide what to do with the leftover. There are {N} pupils. 1 minibus holds {k} pupils. How many minibuses are needed? Type the number.',
                 answer='(N+k-1)//k', hint='Work out {N} ÷ {k}. Then think: do the pupils who are left over still need to travel?',
                 steps=['Divide {N} by {k}: there is a remainder.', 'The pupils left over still need a ride, so they need one more minibus.', 'Minibuses needed: {ans}.']),
        oracle=lambda e: groups_needed(_n(e), e['k'])),
    '2b': dict(
        base=dict(q=8, k=7, r=4),
        tpl=dict(vars=dict(q=[6, 8, 9], k=[6, 7, 8, 9], r=[1, 2, 3, 4]), derive=dict(N='q*k+r'),
                 q='Mei has ${N}. 1 book costs ${k}. How many books can Mei buy? Type the number.',
                 answer='N//k', hint='Work out {N} ÷ {k}. Can Mei buy a book with the money that is left over?',
                 steps=['Divide {N} by {k}: there is a remainder.', 'The money left over is not enough for another book.', 'Mei can buy {ans} books.']),
        oracle=lambda e: groups_of(_n(e), e['k'])[0]),
    '2c': dict(
        base=dict(q=14, k=6, r=3),
        tpl=dict(vars=dict(q=[12, 14, 17], k=[5, 6, 8], r=[1, 2, 3, 4]), derive=dict(N='q*k+r'),
                 q='There are {N} eggs. 1 box holds {k} eggs. How many boxes are FULL? Type the number.',
                 answer='N//k', hint='Count in {k}s without going past {N}. How many boxes did you fill?',
                 steps=['Divide {N} by {k}: there is a remainder.', 'The eggs left over do not fill a box.', '{ans} boxes are full.']),
        oracle=lambda e: groups_of(_n(e), e['k'])[0]),
    '2d': dict(
        base=dict(q=14, k=6, r=3),
        tpl=dict(vars=dict(q=[12, 14, 17], k=[5, 6, 8], r=[1, 2, 3, 4]), derive=dict(N='q*k+r'),
                 q='There are {N} eggs. 1 box holds {k} eggs. How many boxes hold ALL the eggs? Type the number.',
                 answer='(N+k-1)//k', hint='Think about the eggs that do not fill a whole box. Do they still need a box?',
                 steps=['Divide {N} by {k}: there is a remainder.', 'The eggs left over still need a box.', '{ans} boxes hold all the eggs.']),
        oracle=lambda e: groups_needed(_n(e), e['k'])),
    '3a': dict(
        base=dict(q=12, k=8, r=5),
        tpl=dict(vars=dict(q=[9, 12, 15], k=[6, 8, 9], r=[2, 3, 4]),
                 q='Ravi packs marbles into bags of {k}. He fills {q} bags and has {r} marbles left over. How many marbles does Ravi have? Type the number.',
                 answer='q*k+r', hint='Find how many marbles are in the {q} full bags first. Then add the leftover marbles.',
                 steps=['{q} bags of {k} marbles: multiply {q} by {k}.', 'Add the {r} marbles left over.', 'Ravi has {ans} marbles.']),
        oracle=lambda e: sum(e['k'] for _ in range(e['q'])) + e['r']),
    '3b': dict(
        base=dict(q=12, k=8, r=5, j=9),
        tpl=dict(vars=dict(q=[10, 12, 14], k=[6, 8], r=[2, 5], j=[7, 9]), derive=dict(T='q*k+r'),
                 q='Ravi packs marbles into bags of {k}. He fills {q} bags and has {r} marbles left over. He tips them all out and packs them again into bags of {j}. How many full bags does he get, and how many marbles are left over? Fill in the boxes.',
                 frame=grp('Full bags: {f1}      Left over: {f2}'), answers=dict(f1='T//j', f2='T%j'),
                 hint='First find how many marbles Ravi has in all. Then count in {j}s without going past that number.',
                 steps=['Ravi has {q} × {k} + {r} = {T} marbles.', 'Share {T} into bags of {j}.', 'The answers are {ans}.']),
        oracle=lambda e: dict(zip(('f1', 'f2'), groups_of(sum(e['k'] for _ in range(e['q'])) + e['r'], e['j'])))),
    'T1': dict(
        base=dict(N=53, k=8),
        tpl=dict(vars=dict(N=[53, 47, 62, 75], k=[6, 7, 8, 9]),
                 q='Mei has {N} beads. She makes bracelets with {k} beads each. How many bracelets can she make, and how many more beads does she need to make one more bracelet? Fill in the boxes.',
                 frame=grp('Bracelets: {f1}      More beads needed: {f2}'), answers=dict(f1='N//k', f2='k-N%k'),
                 hint='Count in {k}s without going past {N}. For the second part, how many beads short of the next bracelet is she?',
                 steps=['Divide {N} by {k}: the full bracelets and the beads left over.', 'One more bracelet needs {k} beads. Take away the beads she has left.', 'The answers are {ans}.']),
        oracle=lambda e: (lambda g: dict(f1=g[0], f2=e['k'] - g[1]))(groups_of(e['N'], e['k']))),
    'T4': dict(
        base=dict(N=100, k=9),
        tpl=dict(vars=dict(N=[100, 52, 71, 205], k=[6, 7, 8, 9]),
                 q='A boat can carry {k} people at a time. {N} people want to cross the river. How many boatloads are needed? Type the number.',
                 answer='(N+k-1)//k', hint='Work out {N} ÷ {k}. What happens to the people who are left over?',
                 steps=['Divide {N} by {k}: there is a remainder.', 'The people left over still need a boat.', '{ans} boatloads are needed.']),
        oracle=lambda e: groups_needed(e['N'], e['k'])),
    'TH-a': dict(
        base=dict(N=50, k=8),
        tpl=dict(vars=dict(N=[50, 35, 67, 58, 79], k=[6, 7, 8, 9]),
                 q='Extra practice (not for the lesson). {N} ÷ {k}. Fill in the boxes.', frame=grp('{N} ÷ {k} = {f1} remainder {f2}'), answers=dict(f1='N//k', f2='N%k'),
                 hint='Count in {k}s. Stop before you pass {N}.', steps=['Count in {k}s without going past {N}.', 'What is left is the remainder.', 'The answers are {ans}.']),
        oracle=lambda e: dict(zip(('f1', 'f2'), groups_of(e['N'], e['k'])))),
    'TH-b': dict(
        base=dict(N=63, k=9),
        tpl=dict(vars=dict(N=[63, 48, 56, 72, 45], k=[6, 7, 8, 9]),
                 q='Extra practice (not for the lesson). {N} ÷ {k}. Fill in the boxes. (Write 0 if nothing is left over.)', frame=grp('{N} ÷ {k} = {f1} remainder {f2}'), answers=dict(f1='N//k', f2='N%k'),
                 hint='Count in {k}s. Does {N} come up?', steps=['Count in {k}s without going past {N}.', 'What is left is the remainder.', 'The answers are {ans}.']),
        oracle=lambda e: dict(zip(('f1', 'f2'), groups_of(e['N'], e['k'])))),
}

for _d in ITEMS:
    if _d['type'] == 'selfcheck' and 'marking_mode' not in _d:
        _d['marking_mode'] = 'self'
