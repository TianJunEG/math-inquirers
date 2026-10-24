"""Online practice for Level 3 (Primary 3, ages 8-10) holiday lesson 4: Model Makers (word problems with bar models).

The questions are the ones printed in the Level 3 holiday workbook (p3/workbook_html.js builds it from p3/content/l4.js: Start here = the lesson's workbook()
pages; Think harder 1 to 4 and Go further 5 to 7 = qbank stretch[0..3] and challenge[-3:]; the Extra pair = deck.takeHome (printed as "Take-home");
the Investigation = p3/gifted.json lesson 4).  Every answer is recomputed by an INDEPENDENT checker below (loops that try the numbers of the story, never a
copy of the printed answer); build_holiday.py stops if a checker and the printed answer differ.  The bar models are the workbook's own figures
(p3/content/l4.js and p3/figs_l3.js, via p3/figs_p3_w2.js); they are the printed skeletons (given numbers and question marks, no answers).
"""
import itertools, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *      # noqa: E402,F401
from p3lib import *     # noqa: E402,F401

META = dict(level=3, lesson=4, key='p3', title='Model Makers', workbook_title='MODEL MAKERS', topic='Word Problems: Bar Models', strand='Word problems',
            sources=['p3/content/l4.js', 'p3/gifted.json'],
            intro=['Draw a model. Label what you know. Put a ? on what you want to find. The pictures on the screen are the starting bars: use paper to draw your own and try your ideas.',
                   'Type the answers here. A model is like a map of the story: it shows what stays the same.'])
FIG = figs2()
SK = 'Word problems'


def I(**kw):
    kw.setdefault('strand', SK)
    return kw


def one(solutions):
    """The only solution, or None if there are none or several (a puzzle must have exactly one answer)."""
    return solutions[0] if len(solutions) == 1 else None


def find(pred, hi=5000):
    """The first whole number from 0 to hi that makes pred true; None if there is none (a story must have such a number)."""
    for x in range(hi + 1):
        if pred(x):
            return x
    return None


def give_fig(caption):
    """The model of the example in Go further 5: Ali 50 stickers, Ben 20 stickers, Ali gives 15 so that each has 35 (the correct drawing shown after Submit)."""
    sc, x0 = 7, 62
    b = T(8, 38, 'Ali', 16, 'start', 800) + T(8, 92, 'Ben', 16, 'start', 800)
    b += Re(x0, 14, 35 * sc, 36, YEL, NAVY, 2.4) + T(x0 + 17 * sc, 38, '35', 18) + Re(x0 + 35 * sc, 14, 15 * sc, 36, '#fff', NAVY, 2.4, 0, '6 4') + T(x0 + 42.5 * sc, 38, '15', 16, 'middle', 800, TEAL)
    b += Re(x0, 68, 20 * sc, 36, YEL, NAVY, 2.4) + T(x0 + 10 * sc, 92, '20', 18) + Re(x0 + 20 * sc, 68, 15 * sc, 36, '#D3F1E4', NAVY, 2.4, 0, '6 4') + T(x0 + 27.5 * sc, 92, '+15', 16, 'middle', 800, TEAL)
    b += Ln(x0 + 35 * sc, 6, x0 + 35 * sc, 112, 2, TEAL, '5 4') + T(x0 + 35 * sc, 130, 'same number: 35 each', 15, 'middle', 800, TEAL)
    b += T(x0 + 50 * sc + 8, 38, '50', 16, 'start', 800)
    return svg(x0 + 50 * sc + 50, 140, b, caption)


YN = ['Yes', 'No']
SAME = ['The difference got bigger', 'The difference got smaller', 'The difference stayed the same']


def ages(years, mei=13, bro=5):
    return mei + years, bro + years


ITEMS = [
    # ================= Start here (workbook lesson 4, No.1 to No.6)
    I(id='1a', tier='core', no='1(a)', type='number', skill='part-whole model', answer=386, svg=FIG['l4_q1'],
      q='Draw a model. A bakery made 1250 buns. It sold 486 buns in the morning and 378 buns in the afternoon. How many buns were left? Type the number.',
      check=lambda: find(lambda left: left + 486 + 378 == 1250),
      hint='Add the two amounts sold first (486 + 378). Then take that away from 1250.',
      steps=['Add the buns sold: 486 + 378 = 864.', 'Take that away from the whole bar: 1250 - 864 = 386.', '386 buns were left. Check: 486 + 378 + 386 = 1250.'],
      src=['A bakery made 1250 buns. It sold 486 buns in the morning and 378 buns in the afternoon.', 'How many buns were left?']),
    I(id='1b', tier='core', no='1(b)', type='number', skill='comparison model', answer=108, svg=FIG['l4_q1'],
      q='A bakery sold 486 buns in the morning and 378 buns in the afternoon. How many more buns were sold in the morning than in the afternoon? Type the number.',
      check=lambda: find(lambda d: 378 + d == 486),
      hint='Put the two amounts side by side as two bars. How much longer is the morning bar?',
      steps=['Morning is the longer bar: 486. Afternoon is 378.', 'The difference is 486 - 378 = 108.', '108 more buns were sold in the morning.'],
      src=['How many more buns were sold in the morning than in the afternoon?']),

    I(id='2a', tier='core', no='2(a)', type='fields', skill='comparison model', answer=[473, 394], svg=FIG['l4_q2'], frame=grp('Ali has {f1} stickers.      Ben has {f2} stickers.'),
      q='Mei has 345 stickers. Ali has 128 more stickers than Mei. Ben has 79 fewer stickers than Ali. Fill in the boxes.',
      check=lambda: [345 + 128, 345 + 128 - 79],
      hint='Find Ali first (compare with Mei). Then find Ben (compare with Ali, not Mei).',
      steps=['Ali has 128 more than Mei: 345 + 128 = 473.', 'Ben has 79 fewer than Ali, so compare with Ali, not Mei: 473 - 79 = 394.', 'Ali has 473 stickers and Ben has 394 stickers.'],
      src=['Mei has 345 stickers. Ali has 128 more stickers than Mei. Ben has 79 fewer stickers than Ali.', 'Ali has ______ stickers.      Ben has ______ stickers.']),
    I(id='2b', tier='core', no='2(b)', type='number', skill='comparison model', answer=1212, svg=FIG['l4_q2'],
      q='Mei has 345 stickers. Ali has 128 more stickers than Mei. Ben has 79 fewer stickers than Ali. How many stickers do the three children have altogether? Type the number.',
      check=lambda: 345 + (345 + 128) + (345 + 128 - 79),
      hint='Find how many each child has first. Then add the three numbers.',
      steps=['Mei has 345. Ali has 345 + 128 = 473. Ben has 473 - 79 = 394.', '345 + 473 = 818 and 818 + 394 = 1212.', 'The three children have 1212 stickers altogether.'],
      src=['How many stickers do the three children have altogether?']),

    I(id='3a', tier='core', no='3(a)', type='fields', skill='times-as-many model', answer=[4, 62], svg=FIG['l4_q3'], frame=grp('There are {f1} units altogether.      1 unit = {f2} beads'),
      q='Siti has 3 times as many beads as Ravi. They have 248 beads altogether. Each box in the picture is 1 unit (one equal part). Fill in the boxes.',
      check=lambda: [1 + 3, find(lambda u: u * (1 + 3) == 248)],
      hint='Count the boxes in both bars. Then share the 248 beads equally between the boxes.',
      steps=['Ravi has 1 unit and Siti has 3 units, so there are 1 + 3 = 4 units altogether.', 'Share the 248 beads equally into 4 units: 248 ÷ 4 = 62.', '1 unit = 62 beads.'],
      src=['Siti has 3 times as many beads as Ravi. They have 248 beads altogether. Each box in the picture is 1 unit (one equal part).', 'How many units are there altogether?   ______      1 unit = ______ beads']),
    I(id='3b', tier='core', no='3(b)', type='fields', skill='times-as-many model', answer=[186, 124], svg=FIG['l4_q3'], frame='Siti has {f1} beads. She has {f2} more beads than Ravi.',
      q='Siti has 3 times as many beads as Ravi. They have 248 beads altogether. Each box in the picture is 1 unit (one equal part). Fill in the boxes.',
      check=lambda: (lambda u: [3 * u, 3 * u - u])(find(lambda u: u * 4 == 248)),
      hint='First find how many beads are in 1 unit. Then count the units in Siti\'s bar, and the units that Siti has extra.',
      steps=['1 unit = 248 ÷ 4 = 62 beads.', 'Siti has 3 units: 3 × 62 = 186 beads.', 'Siti has 2 more units than Ravi: 2 × 62 = 124 more beads. (Check: 186 - 62 = 124.)'],
      src=['Siti has 3 times as many beads as Ravi.', 'Siti has ______ beads. She has ______ more beads than Ravi.']),

    I(id='4', tier='core', no='4', type='fields', skill='total and difference', answer=[63, 87], svg=FIG['l4_q4'], frame=grp('Ben: {f1}      Ali: {f2}'),
      q='Ali and Ben have 150 marbles altogether. Ali has 24 more marbles than Ben. How many marbles does each boy have? Fill in the boxes.',
      check=lambda: (lambda b: [b, b + 24])(find(lambda b: b + (b + 24) == 150)),
      hint='You can guess and check. Try Ben = 50, so Ali = 74. Is the total 150? Is it too big or too small? Try again.',
      steps=['Take away the extra 24 that Ali has: 150 - 24 = 126.', 'Share 126 equally between the two boys: 126 ÷ 2 = 63. Ben has 63.', 'Ali has 24 more: 63 + 24 = 87. Check: 63 + 87 = 150.'],
      src=['Ali and Ben have 150 marbles altogether. Ali has 24 more marbles than Ben. How many marbles does each boy have?', 'Hint: you can guess and check. Try Ben = 50, so Ali = 74.']),

    I(id='5a', tier='core', no='5(a)', type='number', skill='make them equal', answer=19, svg=FIG['l4_q5'],
      q='Mei has 85 stickers. Siti has 47 stickers. Mei gives some stickers to Siti so that they both have the same number. How many stickers does Mei give Siti? Type the number.',
      check=lambda: find(lambda g: 85 - g == 47 + g),
      hint='Try giving 10 stickers. Do they have the same number now? Keep trying.',
      steps=['The difference is 85 - 47 = 38.', 'To make them equal, Mei gives half of the difference: 38 ÷ 2 = 19.', 'Check: Mei has 85 - 19 = 66 and Siti has 47 + 19 = 66.'],
      src=['Mei has 85 stickers. Siti has 47 stickers. Mei gives some stickers to Siti so that they both have the same number.', 'How many stickers does Mei give Siti?']),
    I(id='5b-test', tier='core', no='5(b) test', type='fields', skill='make them equal', answer=[47, 85], svg=FIG['l4_q5'], frame='Mei has {f1} stickers and Siti has {f2} stickers.',
      q='(if time) Mei has 85 stickers and Siti has 47 stickers. Ravi says, "Mei must give Siti 38 stickers, because 85 - 47 = 38." Test his idea. Mei gives Siti 38 stickers. Fill in how many stickers each girl has now.',
      check=lambda: [85 - 38, 47 + 38],
      hint='Mei starts with 85 and gives away 38. Siti starts with 47 and gets 38 more.',
      steps=['Mei: 85 - 38 = 47.', 'Siti: 47 + 38 = 85.', 'They do not have the same number. They have only swapped.'],
      src=['(if time) Ravi says, "Mei must give Siti 38 stickers, because 85 − 47 = 38." What mistake did Ravi make?']),
    I(id='5b', tier='core', no='5(b) mistake', type='selfcheck', open=True, skill='make them equal',
      q='(if time) Ravi says, "Mei must give Siti 38 stickers, because 85 - 47 = 38." What mistake did Ravi make? Write your idea, then compare with the answer shown.',
      check=lambda: [85 - 47, 85 - 38, 47 + 38, 85 - 47 == 2 * find(lambda g: 85 - g == 47 + g)],
      hint='38 is the whole difference between the two girls. What happens to the two amounts if Mei gives Siti 38?',
      steps=['38 is the whole difference between 85 and 47.', 'If Mei gave 38, Mei would have 85 - 38 = 47 and Siti would have 47 + 38 = 85. They would just swap places.', 'Mei must give half of the difference, 38 ÷ 2 = 19, so that both end up with 66.'],
      src=['(if time) Ravi says, "Mei must give Siti 38 stickers, because 85 − 47 = 38." What mistake did Ravi make?']),

    I(id='6a', tier='core', no='6(a)', type='number', skill='before and after', answer=27, svg=FIG['l4_q6'],
      q='(if time) Ali has $45. Ben has $18. Grandma gives each boy $10. How much more money does Ali have than Ben now? Type the number of dollars.',
      check=lambda: (45 + 10) - (18 + 10),
      hint='Find how much money each boy has now. Then find how much more Ali has.',
      steps=['Ali now has $45 + $10 = $55. Ben now has $18 + $10 = $28.', '$55 - $28 = $27.', 'Ali has $27 more than Ben now.'],
      src=['(if time) Ali has $45. Ben has $18. Grandma gives each boy $10.', 'How much more money does Ali have than Ben now?']),
    I(id='6b', tier='core', no='6(b)', type='number', skill='before and after', answer=27, svg=FIG['l4_q6'],
      q='(if time) Ali has $45. Ben has $18. Grandma gives each boy $10. How much more did Ali have than Ben before Grandma gave the money? Type the number of dollars.',
      check=lambda: 45 - 18,
      hint='Look at the first two bars: Ali before and Ben before. How much longer is Ali\'s bar?',
      steps=['Before Grandma gave the money, Ali had $45 and Ben had $18.', '$45 - $18 = $27.', 'Ali had $27 more than Ben.'],
      src=['How much more did Ali have than Ben before Grandma gave the money?']),
    I(id='6c', tier='core', no='6(c)', type='choice', skill='before and after', options=SAME, answer=SAME[2],
      q='(if time) Look at your answers to 6(a) and 6(b). What happened to the difference between Ali\'s money and Ben\'s money when Grandma gave each boy $10?',
      check=lambda: SAME[2] if (45 + 10) - (18 + 10) == 45 - 18 else (SAME[0] if (45 + 10) - (18 + 10) > 45 - 18 else SAME[1]),
      hint='Put your two answers side by side. Are they the same, or did one get bigger or smaller?',
      steps=['Before: the difference was $27. Now: the difference is still $27.', 'The difference stayed the same.'],
      src=['What do you notice? Why?']),
    I(id='6c-why', tier='core', no='6(c) why', type='selfcheck', open=True, skill='before and after',
      q='(if time) Why does the difference between the two boys stay the same when Grandma gives each of them $10? Write your idea, then compare with the answer shown.',
      check=lambda: [(45 + k) - (18 + k) for k in range(0, 50)],
      hint='Look at the bars. Both bars get the same extra piece at the end. What happens to the gap between the ends of the bars?',
      steps=['Both boys get the same amount, $10, so both bars grow by the same piece.', 'The gap between the ends of the two bars does not change, so the difference stays $27.', 'This works for any amount given to both: the difference between them stays the same.'],
      src=['What do you notice? Why?']),

    # ================= Investigation (Investigation and look back page, No.8: What stays the same?)
    I(id='I8-easy', tier='invest', no='8 easy', type='fields', skill='what stays the same', answer=[8, 20], frame=grp('The difference is {f1}.      The total of both ages is {f2}.'),
      q='Investigation: What stays the same? Mei is 13 years old and her brother is 5. Easy first step: fill in the first row. In 1 year Mei is 14 and her brother is 6. What is the difference between their ages, and what is the total of both ages?',
      check=lambda: [14 - 6, 14 + 6],
      hint='The difference is how much older Mei is: take the smaller age away from the bigger. The total is both ages added together.',
      steps=['The difference is 14 - 6 = 8.', 'The total of both ages is 14 + 6 = 20.'],
      src=['Mei is 13 years old and her brother is 5.', 'Easy first step: fill in the first row. In 1 year Mei is 14 and her brother is 6. What is the difference?']),
    I(id='I8a-ages', tier='invest', no='8(a) ages', type='fields', skill='what stays the same', answer=[15, 7, 16, 8, 17, 9, 18, 10],
      frame=grp('In 2 years: Mei {f1}, brother {f2}.   In 3 years: Mei {f3}, brother {f4}.   In 4 years: Mei {f5}, brother {f6}.   In 5 years: Mei {f7}, brother {f8}.'),
      q='Mei is 13 years old and her brother is 5. Fill in the table for the next 5 years: the ages of Mei and her brother. (The first row, 1 year from now, is in the easy step.)',
      check=lambda: [a for y in (2, 3, 4, 5) for a in ages(y)],
      hint='Each year, both of them get 1 year older. Add the number of years to each age.',
      steps=['In 2 years: 13 + 2 = 15 and 5 + 2 = 7.', 'In 3 years: 16 and 8. In 4 years: 17 and 9. In 5 years: 18 and 10.'],
      src=['Fill in the table for the next 5 years.']),
    I(id='I8a-sums', tier='invest', no='8(a) table', type='fields', skill='what stays the same', answer=[8, 18, 8, 22, 8, 24, 8, 26, 8, 28],
      frame=grp('Now: difference {f1}, total {f2}.   In 2 years: difference {f3}, total {f4}.   In 3 years: difference {f5}, total {f6}.   In 4 years: difference {f7}, total {f8}.   In 5 years: difference {f9}, total {f10}.'),
      q='Mei is 13 years old and her brother is 5. For now and for the next years, fill in the difference between their ages and the total of both ages.',
      check=lambda: [v for y in (0, 2, 3, 4, 5) for v in (ages(y)[0] - ages(y)[1], ages(y)[0] + ages(y)[1])],
      hint='Work out both ages for each row first. The difference is the bigger age take away the smaller. The total is both ages added.',
      steps=['Now: 13 and 5. Difference 13 - 5 = 8, total 13 + 5 = 18.', 'In 2 years: 15 and 7: difference 8, total 22. In 3 years: 16 and 8: difference 8, total 24.', 'In 4 years: 17 and 9: difference 8, total 26. In 5 years: 18 and 10: difference 8, total 28.'],
      src=['Fill in the table for the next 5 years.']),
    I(id='I8b-same', tier='invest', no='8(b) same', type='choice', skill='what stays the same',
      options=["Mei's age", "Her brother's age", 'The difference between their ages', 'The total of both ages'], answer='The difference between their ages',
      q='Mei is 13 years old and her brother is 5. Look at your table for the next 5 years. What stays the same every year?',
      check=lambda: (lambda cols: [n for n, v in cols if len(set(v)) == 1][0])([("Mei's age", [ages(y)[0] for y in range(6)]), ("Her brother's age", [ages(y)[1] for y in range(6)]),
                                                                              ('The difference between their ages', [ages(y)[0] - ages(y)[1] for y in range(6)]), ('The total of both ages', [sum(ages(y)) for y in range(6)])]),
      hint='Look down each column of your table. Which column has the same number in every row?',
      steps=['Mei\'s age goes up by 1 each year. Her brother\'s age goes up by 1 each year.', 'The total goes up each year too.', 'The difference is 8 in every row: the difference stays the same.'],
      src=['What stays the same every year? What changes? How does it change?']),
    I(id='I8b-change', tier='invest', no='8(b) change', type='number', skill='what stays the same', answer=2,
      q='Mei is 13 years old and her brother is 5. Each year the total of both ages changes. By how much does the total of both ages go up each year? Type the number.',
      check=lambda: (lambda t: t[1] - t[0] if len({b - a for a, b in zip(t, t[1:])}) == 1 else None)([sum(ages(y)) for y in range(6)]),
      hint='Look down the column of totals in your table. How much more is each total than the one before?',
      steps=['The totals are 18, 20, 22, 24, 26, 28.', 'Each total is 2 more than the one before: both ages go up by 1, and 1 + 1 = 2.', 'The total goes up by 2 each year.'],
      src=['What stays the same every year? What changes? How does it change?']),
    I(id='I8c-double', tier='invest', no='8(c) double', type='number', skill='what stays the same', answer=3,
      q='Mei is 13 years old and her brother is 5. Will Mei ever be exactly DOUBLE her brother\'s age? In how many years from now? Type the number of years.',
      check=lambda: one([y for y in range(0, 100) if 13 + y == 2 * (5 + y)]),
      hint='Try each year in your table. In which year is Mei\'s age exactly twice her brother\'s age?',
      steps=['Try each year: in 1 year 14 and 6, in 2 years 15 and 7 (not double).', 'In 3 years Mei is 16 and her brother is 8. 16 = 2 × 8.', 'Mei is double her brother\'s age in 3 years.'],
      src=["Will Mei ever be exactly DOUBLE her brother's age? When? What about TRIPLE? Explain."]),
    I(id='I8c-triple', tier='invest', no='8(c) triple', type='choice', skill='what stays the same', options=['Yes, one day', 'No, not from now on'], answer='No, not from now on',
      q='Mei is 13 years old and her brother is 5. What about TRIPLE? Will Mei ever be exactly 3 times her brother\'s age, from now on? Choose your answer.',
      check=lambda: 'Yes, one day' if any(13 + y == 3 * (5 + y) for y in range(0, 1000)) else 'No, not from now on',
      hint='Try some years. Is Mei\'s age getting closer to 3 times her brother\'s age, or further away?',
      steps=['Now Mei is 13 and her brother is 5, so 3 times his age is 15, more than Mei.', 'Each year his age goes up by 1, so 3 times his age goes up by 3, but Mei\'s age goes up by only 1. 3 times his age gets further away.', 'So she will not be triple his age from now on. (Last year she was: 12 and 4.)'],
      src=["Will Mei ever be exactly DOUBLE her brother's age? When? What about TRIPLE? Explain."]),
    I(id='I8c-why', tier='invest', no='8(c) explain', type='selfcheck', open=True, skill='explaining why',
      q='Explain how you know when Mei is double her brother\'s age, and why she is never triple his age from now on. Write your idea, then compare with the answer shown.',
      check=lambda: [(y, 13 + y, 5 + y) for y in range(0, 10) if 13 + y == 2 * (5 + y)] + [(y, 13 + y, 5 + y) for y in range(-5, 100) if 13 + y == 3 * (5 + y)],
      hint='The difference between their ages is 8 every year. When Mei is double, how big is her brother\'s age compared with the difference?',
      steps=['The difference between their ages is always 8. Mei is double her brother\'s age when her brother\'s age equals the difference: 8. That is in 3 years (16 and 8).', 'Triple would mean her brother\'s age is half the difference, 4. He was 4 last year (Mei 12), and he only gets older, so it will never be triple again.', 'A bar model helps: the difference is the part of Mei\'s bar that is longer than her brother\'s bar.'],
      src=["Will Mei ever be exactly DOUBLE her brother's age? When? What about TRIPLE? Explain."]),

    # ================= Think harder (workbook Think harder, No.1 to No.4)
    I(id='T1', tier='stretch', no='T1', type='number', skill='times-as-many model', answer=48, svg=FIG['l4_t1'],
      q='Ali and Ben have 96 cards altogether. Ali has 3 times as many cards as Ben. How many more cards does Ali have than Ben? Type the number.',
      check=lambda: (lambda b: 3 * b - b)(find(lambda b: b + 3 * b == 96)),
      hint='Count the units in both bars. Share 96 equally to find 1 unit. Then look at how many extra units Ali has.',
      steps=['Ben has 1 unit and Ali has 3 units: 4 units = 96, so 1 unit = 24.', 'Ali has 2 more units than Ben.', '2 × 24 = 48. Ali has 48 more cards than Ben.'],
      src=['Ali and Ben have 96 cards altogether. Ali has 3 times as many cards as Ben. How many more cards does Ali have than Ben?']),
    I(id='T2', tier='stretch', no='T2', type='number', skill='make them equal', answer=27, svg=FIG['l4_t2'],
      q='Siti has 54 more beads than Mei. Siti gives Mei some beads, and now they have the same number. How many beads did Siti give Mei? Type the number.',
      check=lambda: one(list({find(lambda g: (m + 54) - g == m + g, 60) for m in (0, 10, 33, 100)})),
      hint='Look at the difference between the two bars. To make them equal, how much of the difference must Siti give away?',
      steps=['The difference is 54.', 'To make them equal, Siti gives half of the difference: 54 ÷ 2 = 27.', 'Check: Siti has 27 more than Mei, then gives 27 away, so now Siti has 27 less than before, and Mei has 27 more than before. They are equal.'],
      src=['Siti has 54 more beads than Mei. Siti gives Mei some beads, and now they have the same number. How many beads did Siti give Mei?']),
    I(id='T3', tier='stretch', no='T3', type='number', skill='comparison model', answer=250, svg=FIG['l4_t3'],
      q='Three boxes hold 600 pens altogether. Box A has 50 more pens than Box B. Box C has 50 more pens than Box A. How many pens are in Box C? Type the number.',
      check=lambda: (lambda b: b + 100)(find(lambda b: b + (b + 50) + (b + 100) == 600)),
      hint='Take away the extra pens first, so that the three boxes are equal. Then share what is left.',
      steps=['Box A has 50 extra and Box C has 100 extra: 50 + 100 = 150 extra altogether.', 'Take them away: 600 - 150 = 450. Share into 3 equal boxes: 450 ÷ 3 = 150 in Box B.', 'Box A has 200 and Box C has 250. Check: 150 + 200 + 250 = 600.'],
      src=['Three boxes hold 600 pens altogether. Box A has 50 more pens than Box B. Box C has 50 more pens than Box A. How many pens are in Box C?']),
    I(id='T4', tier='stretch', no='T4', type='fields', skill='total and difference', answer=[3, 6], svg=FIG['l4_t4'], frame=grp('Flour: {f1} kg      Rice: {f2} kg'),
      q='A bag of rice and a bag of flour weigh 9 kg altogether. The rice is 3 kg heavier than the flour. How heavy is each bag? Fill in the boxes.',
      check=lambda: (lambda f: [f, f + 3])(find(lambda f: f + (f + 3) == 9)),
      hint='Take away the extra from the rice. Then the two bags are equal. How much is left to share?',
      steps=['Take away the extra 3 kg: 9 - 3 = 6 kg.', 'Share 6 kg equally between the two bags: 6 ÷ 2 = 3 kg. The flour is 3 kg.', 'The rice is 3 kg heavier: 3 + 3 = 6 kg. Check: 3 + 6 = 9.'],
      src=['A bag of rice and a bag of flour weigh 9 kg altogether. The rice is 3 kg heavier than the flour. How heavy is each bag?']),

    # ================= Go further (workbook Go further, No.5 to No.7) and the Extra pair (printed as "Take-home")
    I(id='G5', tier='challenge', no='G5', type='selfcheck', paper=True, open=True, skill='making up a story', sol_fig=lambda got: give_fig('A model of the example: Ali has 50 stickers and Ben has 20. Ali gives 15 stickers and then they have 35 each.'),
      q='Make up your own before-and-after story about stickers or money, where one child gives some to another child. Draw its model, solve it and check it. Then change ONE number in your story. What changes in the answer, and what stays the same? Swap with a partner.',
      check=lambda: [(find(lambda g: a - g == b + g), a, b) for a, b in ((50, 20), (60, 20))],
      hint='Start with two amounts, for example Ali has more than Ben. Draw two bars. Decide how much one child gives so that they end up with the same number. Then check with your model.',
      steps=['Answers vary. Check that the model matches the story, the total is the same before and after, and you can explain what changed.', 'Example: Ali has 50 stickers and Ben has 20. Ali gives Ben some so that they have the same number. The difference is 30, so Ali gives half of it: 15. They have 35 each.', 'If Ali had 60 stickers, the difference would be 40 and Ali would give 20: the difference grows by 10 and the gift by 5. The total of the two children stays the same before and after giving.'],
      src=['Make up your own before-and-after story about stickers or money, where one child gives some to another child. Draw its model, solve it and check it. Then change ONE number in your story. What changes in the answer, and what stays the same? Swap with a partner.']),
    I(id='G6', tier='challenge', no='G6', type='number', skill='what stays the same', answer=10,
      q='Ravi is 7 years old and his sister is 3. In how many years will their ages add up to 30? Type the number of years.',
      check=lambda: find(lambda y: (7 + y) + (3 + y) == 30, 100),
      hint='Find the total of their ages now. How much does the total go up each year? How much more do you need to reach 30?',
      steps=['Now their ages add up to 7 + 3 = 10.', 'Each year both get 1 year older, so the total goes up by 2.', 'To go from 10 to 30 the total must go up by 20: 20 ÷ 2 = 10 years. Check: 17 + 13 = 30.'],
      src=['Ravi is 7 years old and his sister is 3. In how many years will their ages add up to 30? Explain how you know.']),
    I(id='G6-why', tier='challenge', no='G6 why', type='selfcheck', open=True, skill='explaining why',
      q='Explain how you know how many years it takes for Ravi\'s age and his sister\'s age to add up to 30. Write your idea, then compare with the answer shown.',
      check=lambda: [(y, (7 + y) + (3 + y)) for y in (0, 1, 2, 10)],
      hint='What is the total of their ages now? By how much does that total change in one year?',
      steps=['Now they add up to 10, and each year the total grows by 2 (one year for each child).', '30 - 10 = 20, and 20 ÷ 2 = 10 years.', 'Check: in 10 years Ravi is 17 and his sister is 13, and 17 + 13 = 30.'],
      src=['Ravi is 7 years old and his sister is 3. In how many years will their ages add up to 30? Explain how you know.']),
    I(id='G7', tier='challenge', no='G7', type='fields', skill='comparison model', answer=[2, 5], svg=FIG['l4_c7'], frame='{f1} m {f2} cm',
      q='A ribbon 4 m 75 cm long is cut into 3 pieces. The second piece is twice as long as the first. The third piece is 25 cm longer than the second. How long is the third piece? Fill in the boxes.',
      check=lambda: (lambda x: [(2 * x + 25) // 100, (2 * x + 25) % 100])(find(lambda x: x + 2 * x + (2 * x + 25) == 475)),
      hint='Change the ribbon to centimetres. Take away the extra 25 cm so that the pieces are made of equal units. How many units are there?',
      steps=['4 m 75 cm = 475 cm. Take away the extra 25 cm: 475 - 25 = 450 cm.', 'The first piece is 1 unit, the second is 2 units and the third is 2 units: 5 equal units, so 1 unit = 450 ÷ 5 = 90 cm.', 'The third piece is 2 × 90 + 25 = 205 cm = 2 m 5 cm.'],
      src=['A ribbon 4 m 75 cm long is cut into 3 pieces. The second piece is twice as long as the first. The third piece is 25 cm longer than the second. How long is the third piece?']),
    I(id='TH-a', tier='challenge', no='Extra (a)', type='number', skill='comparison model', answer=55,
      q='Extra practice (not for the lesson). Ben has 40. Ali has 15 more than Ben. How many does Ali have? Type the number.',
      check=lambda: find(lambda a: a - 40 == 15),
      hint='More than means the bar is longer. Add the extra.',
      steps=['Ali has 15 more than Ben.', '40 + 15 = 55.'],
      src=['Ben has 40. Ali has 15 more than Ben. How many does Ali have?']),
    I(id='TH-b', tier='challenge', no='Extra (b)', type='number', skill='comparison model', answer=48,
      q='Extra practice (not for the lesson). Mei has 60. Siti has 12 fewer than Mei. How many does Siti have? Type the number.',
      check=lambda: find(lambda s: 60 - s == 12),
      hint='Fewer than means the bar is shorter. Take away the difference.',
      steps=['Siti has 12 fewer than Mei.', '60 - 12 = 48.'],
      src=['Mei has 60. Siti has 12 fewer than Mei. How many does Siti have?']),
]


# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
VARIANTS = {
    '1a': dict(
        base=dict(T=1250, a=486, b=378),
        tpl=dict(vars=dict(T=[1250, 1400, 1600], a=[486, 312, 245], b=[378, 215, 190]),
                 q='A bakery made {T} buns. It sold {a} buns in the morning and {b} buns in the afternoon. How many buns were left? Type the number.', answer='T-a-b',
                 hint='Add the two amounts sold first. Then take that away from {T}.',
                 steps=['Add the buns sold: {a} + {b}.', 'Take that away from the whole bar: {T} take away the buns sold.', '{ans} buns were left.']),
        oracle=lambda e: find(lambda left: left + e['a'] + e['b'] == e['T'], 2000)),
    '1b': dict(
        base=dict(a=486, b=378),
        tpl=dict(vars=dict(a=[486, 520, 650], b=[378, 299, 410]),
                 q='A bakery sold {a} buns in the morning and {b} buns in the afternoon. How many more buns were sold in the morning than in the afternoon? Type the number.', answer='a-b',
                 hint='Put the two amounts side by side as two bars. How much longer is the morning bar?',
                 steps=['The morning bar is longer: {a}. The afternoon bar is {b}.', 'The difference is {a} - {b}.', '{ans} more buns were sold in the morning.']),
        oracle=lambda e: find(lambda d: e['b'] + d == e['a'], 2000)),
    '2a': dict(
        base=dict(m=345, d=128, e=79),
        tpl=dict(vars=dict(m=[345, 280, 410], d=[128, 95, 240], e=[79, 40, 60]),
                 q='Mei has {m} stickers. Ali has {d} more stickers than Mei. Ben has {e} fewer stickers than Ali. Fill in the boxes.', frame=grp('Ali has {f1} stickers.      Ben has {f2} stickers.'),
                 answers=dict(f1='m+d', f2='m+d-e'),
                 hint='Find Ali first (compare with Mei). Then find Ben (compare with Ali, not Mei).',
                 steps=['Ali has {d} more than Mei: add {d} to {m}.', 'Ben has {e} fewer than Ali, so compare with Ali, not Mei: take {e} away from Ali\'s number.', 'The answers are {ans}.']),
        oracle=lambda e: dict(f1=find(lambda a: a - e['d'] == e['m'], 2000), f2=find(lambda b: b + e['e'] == e['m'] + e['d'], 2000))),
    '3a': dict(
        base=dict(k=3, u=62),
        tpl=dict(vars=dict(k=[2, 3, 4, 5], u=[62, 45, 30, 25]), derive=dict(T='(k+1)*u'),
                 q='Siti has {k} times as many beads as Ravi. They have {T} beads altogether. Each box in a picture of the two bars is 1 unit (one equal part). Fill in the boxes.',
                 frame=grp('There are {f1} units altogether.      1 unit = {f2} beads'), answers=dict(f1='k+1', f2='T//(k+1)'),
                 hint='Count the boxes in both bars. Then share the {T} beads equally between the boxes.',
                 steps=['Ravi has 1 unit and Siti has {k} units, so count them together.', 'Share the {T} beads equally between all the units.', 'The answers are {ans}.']),
        oracle=lambda e: dict(f1=1 + e['k'], f2=find(lambda x: x * (e['k'] + 1) == (e['k'] + 1) * e['u'], 500))),
    '3b': dict(
        base=dict(k=3, u=62),
        tpl=dict(vars=dict(k=[2, 3, 4, 5], u=[62, 45, 30, 25]), derive=dict(T='(k+1)*u'),
                 q='Siti has {k} times as many beads as Ravi. They have {T} beads altogether. Fill in the boxes.', frame='Siti has {f1} beads. She has {f2} more beads than Ravi.',
                 answers=dict(f1='k*u', f2='(k-1)*u'),
                 hint='First find how many beads are in 1 unit. Then count the units in Siti\'s bar, and the units that Siti has extra.',
                 steps=['Find 1 unit by sharing {T} into {k} + 1 equal parts.', 'Siti has {k} units. She has {k} - 1 units more than Ravi.', 'The answers are {ans}.']),
        oracle=lambda e: (lambda u: dict(f1=e['k'] * u, f2=e['k'] * u - u))(find(lambda x: x * (e['k'] + 1) == (e['k'] + 1) * e['u'], 500))),
    '4': dict(
        base=dict(T=150, d=24),
        tpl=dict(vars=dict(T=[150, 120, 98, 200], d=[24, 10, 36, 40]),
                 q='Ali and Ben have {T} marbles altogether. Ali has {d} more marbles than Ben. How many marbles does each boy have? Fill in the boxes.', frame=grp('Ben: {f1}      Ali: {f2}'),
                 answers=dict(f1='(T-d)//2', f2='(T-d)//2+d'),
                 hint='Take away the extra {d} that Ali has. Then the two boys have equal amounts. Share what is left.',
                 steps=['Take away the extra {d}: {T} - {d}.', 'Share what is left equally between the two boys. That is Ben\'s number.', 'Ali has {d} more than Ben. The answers are {ans}.']),
        oracle=lambda e: (lambda b: dict(f1=b, f2=b + e['d']))(find(lambda b: b + (b + e['d']) == e['T'], 300))),
    '5a': dict(
        base=dict(a=85, b=47),
        tpl=dict(vars=dict(a=[85, 91, 77, 99], b=[47, 33, 51, 25]),
                 q='Mei has {a} stickers. Siti has {b} stickers. Mei gives some stickers to Siti so that they both have the same number. How many stickers does Mei give Siti? Type the number.', answer='(a-b)//2',
                 hint='Find the difference between the two numbers. How much of the difference must Mei give away?',
                 steps=['The difference is {a} - {b}.', 'To make them equal, Mei gives half of the difference.', 'Mei gives {ans} stickers.']),
        oracle=lambda e: find(lambda g: e['a'] - g == e['b'] + g, 100)),
    '6a': dict(
        base=dict(a=45, b=18, g=10),
        tpl=dict(vars=dict(a=[45, 60, 38, 72], b=[18, 25, 12, 30], g=[10, 5, 20, 15]),
                 q='Ali has ${a}. Ben has ${b}. Grandma gives each boy ${g}. How much more money does Ali have than Ben now? Type the number of dollars.', answer='a-b',
                 hint='Find how much money each boy has now. Then find how much more Ali has.',
                 steps=['Ali now has ${a} + ${g}. Ben now has ${b} + ${g}.', 'Subtract to find how much more Ali has.', 'Ali has ${ans} more than Ben now. It is the same as before: both boys got the same amount.']),
        oracle=lambda e: (e['a'] + e['g']) - (e['b'] + e['g'])),
    'T1': dict(
        base=dict(k=3, u=24),
        tpl=dict(vars=dict(k=[2, 3, 4, 5], u=[24, 12, 15, 30]), derive=dict(T='(k+1)*u'),
                 q='Ali and Ben have {T} cards altogether. Ali has {k} times as many cards as Ben. How many more cards does Ali have than Ben? Type the number.', answer='(k-1)*u',
                 hint='Count the units in both bars. Share {T} equally to find 1 unit. Then look at how many extra units Ali has.',
                 steps=['Ben has 1 unit and Ali has {k} units. Share {T} between all the units to find 1 unit.', 'Ali has {k} - 1 more units than Ben.', 'Ali has {ans} more cards than Ben.']),
        oracle=lambda e: (lambda b: e['k'] * b - b)(find(lambda b: b + e['k'] * b == (e['k'] + 1) * e['u'], 500))),
    'T2': dict(
        base=dict(d=54),
        tpl=dict(vars=dict(d=[54, 30, 72, 48, 26]),
                 q='Siti has {d} more beads than Mei. Siti gives Mei some beads, and now they have the same number. How many beads did Siti give Mei? Type the number.', answer='d//2',
                 hint='Look at the difference between the two bars. To make them equal, how much of the difference must Siti give away?',
                 steps=['The difference is {d}.', 'To make them equal, Siti gives half of the difference.', 'Siti gave Mei {ans} beads.']),
        oracle=lambda e: find(lambda g: (20 + e['d']) - g == 20 + g, 100)),
    'T3': dict(
        base=dict(T=600, x=50),
        tpl=dict(vars=dict(T=[600, 450, 900, 300], x=[50, 20, 30, 10]),
                 q='Three boxes hold {T} pens altogether. Box A has {x} more pens than Box B. Box C has {x} more pens than Box A. How many pens are in Box C? Type the number.', answer='(T-3*x)//3+2*x',
                 hint='Take away the extra pens first, so that the three boxes are equal. Then share what is left.',
                 steps=['Box A has {x} extra and Box C has 2 × {x} extra. Take all the extras away from {T}.', 'Share what is left into 3 equal boxes. That is Box B.', 'Box C has the extra pens too: {ans} pens.']),
        oracle=lambda e: find(lambda b: b + (b + e['x']) + (b + 2 * e['x']) == e['T'], 1000) + 2 * e['x']),
    'T4': dict(
        base=dict(T=9, d=3),
        tpl=dict(vars=dict(T=[9, 11, 15, 13], d=[3, 5, 1, 7]),
                 q='A bag of rice and a bag of flour weigh {T} kg altogether. The rice is {d} kg heavier than the flour. How heavy is each bag? Fill in the boxes.', frame=grp('Flour: {f1} kg      Rice: {f2} kg'),
                 answers=dict(f1='(T-d)//2', f2='(T-d)//2+d'),
                 hint='Take away the extra from the rice. Then the two bags are equal. How much is left to share?',
                 steps=['Take away the extra {d} kg: {T} - {d}.', 'Share what is left equally between the two bags. That is the flour.', 'The rice is {d} kg heavier. The answers are {ans}.']),
        oracle=lambda e: (lambda f: dict(f1=f, f2=f + e['d']))(find(lambda f: f + (f + e['d']) == e['T'], 100))),
    'G6': dict(
        base=dict(a=7, b=3, N=30),
        tpl=dict(vars=dict(a=[7, 9, 5], b=[3, 5, 1], N=[30, 24, 40, 50]),
                 q='Ravi is {a} years old and his sister is {b}. In how many years will their ages add up to {N}? Type the number of years.', answer='(N-a-b)//2',
                 hint='Find the total of their ages now. How much does the total go up each year? How much more do you need to reach {N}?',
                 steps=['Now their ages add up to {a} + {b}.', 'Each year both get 1 year older, so the total goes up by 2.', 'Divide the amount still needed by 2: the answer is {ans} years.']),
        oracle=lambda e: find(lambda y: (e['a'] + y) + (e['b'] + y) == e['N'], 100)),
    'TH-a': dict(
        base=dict(b=40, d=15),
        tpl=dict(vars=dict(b=[40, 25, 60, 75], d=[15, 12, 30, 8]),
                 q='Ben has {b}. Ali has {d} more than Ben. How many does Ali have? Type the number.', answer='b+d',
                 hint='More than means the bar is longer. Add the extra.', steps=['Ali has {d} more than Ben.', 'Add {d} to {b}.', 'Ali has {ans}.']),
        oracle=lambda e: find(lambda a: a - e['b'] == e['d'], 500)),
    'TH-b': dict(
        base=dict(m=60, d=12),
        tpl=dict(vars=dict(m=[60, 45, 80, 92], d=[12, 9, 25, 30]),
                 q='Mei has {m}. Siti has {d} fewer than Mei. How many does Siti have? Type the number.', answer='m-d',
                 hint='Fewer than means the bar is shorter. Take away the difference.', steps=['Siti has {d} fewer than Mei.', 'Take {d} away from {m}.', 'Siti has {ans}.']),
        oracle=lambda e: find(lambda s: e['m'] - s == e['d'], 500)),
}
