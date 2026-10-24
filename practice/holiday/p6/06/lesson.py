"""Online practice for Level 6 (Primary 6, ages 11-13) holiday lesson 6: Fair or Unfair? (probability as a fraction; random numbers; running a game 1000 times).

The questions are the ones printed in the Level 6 holiday workbook (p6/content/l6.js workbook(): Start here Q1 to Q5; the Finish page: the Investigation
(p6/content/gaps.json lesson 6) and the exit slip (l6.js lesson.exit); Think harder = the first three l6.js qbank.stretch questions plus the one moved there from Start here
(l6.js moved); Go further = the last three l6.js qbank.challenge questions).  Every answer is recomputed by an INDEPENDENT checker below: exact fractions over a list of every
equally likely outcome (never a simulation, never a copy of the printed answer); the random programs are read from the drawn program and their expected count is found by
listing the outcomes (w3lib.expected_changes).  build_holiday.py stops if a checker and the printed answer differ.  Scratch is not run in the page.
"""
import itertools, math, os, sys
from fractions import Fraction
HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE_, '..'))
sys.path.insert(0, os.path.join(HERE_, '..', '..'))
from hlib import *      # noqa: E402,F401
import p6lib as P       # noqa: E402
import w3lib as W       # noqa: E402

M = W.MINUS
META = dict(level=6, lesson=6, key='p6', title='Fair or Unfair?', workbook_title='FAIR OR UNFAIR?', topic='Probability',
            strand='Probability and coding',
            sources=['p6/content/l6.js', 'p6/content/gaps.json'],
            intro=['You do not need Scratch on this page. The code is drawn as blocks: read it and work out what it does. "pick random 1 to 6" gives a whole number from 1 to 6, each with the same chance.',
                   'Write a probability as a fraction: the ways it can happen out of all the equally likely outcomes. Where a question says "simplest form", type it in simplest form. Type a fraction with a slash, like 3/5, or in the two boxes.',
                   'A random result is close to what you expect, but not exactly the same every time. Questions with "explain" are for you to check against the worked solution.'])
PR, CP = 'Probability', 'Coding and probability'

SPIN = ['R', 'B', 'Y', 'R', 'G', 'B', 'R', 'Y']        # the eight equal parts of Ben's spinner, as drawn
COIN = W.program('l6', 'coinCode')
PLAN = W.program('l6', 'planCode')
COIN_LABEL = 'Code: set heads to 0. Repeat 1000 times: if pick random 1 to 2 equals 1 then change heads by 1. Then say heads.'
PLAN_LABEL = 'Plan with three gaps: set doubles to 0. Repeat 1000 times: set a to pick random 1 to a gap, set b to pick random 1 to a gap, if a gap then change doubles by 1. Then say doubles.'
DICE = list(itertools.product(range(1, 7), repeat=2))      # the 36 equally likely outcomes of two dice


def fr(p, q=None):
    """A Fraction in lowest terms as [numerator, denominator] (for the two-box answers), or as 'a/b'."""
    f = Fraction(p, q) if q else p
    return [f.numerator, f.denominator]


def fs(f):
    return f'{f.numerator}/{f.denominator}'


def prob(hits, total):
    return Fraction(hits, total)


def diff_counts():
    return {d: len([1 for a, b in DICE if abs(a - b) == d]) for d in range(6)}


def pmf(n, p, k):
    return math.comb(n, k) * p ** k * (1 - p) ** (n - k)


def sd(n, p):
    return math.sqrt(n * p * (1 - p))


def coin_prog(k):
    """The coin program with 'pick random 1 to 2' changed to 'pick random 1 to k'."""
    def walk(items):
        out = []
        for it in items:
            it = list(it)
            it[1] = it[1].replace('pick random 1 to 2', f'pick random 1 to {k}')
            if len(it) > 2:
                it[2] = walk(it[2])
            out.append(it)
        return out
    return walk(COIN)


def double_ok(c):
    return W.expected_changes(W.fill(PLAN, [6, 6, c])) == Fraction(1000, 6)


def loop_needed(faces):
    return next(r for r in range(1, 100) if set(range(1, r + 1)) >= set(range(1, faces + 1)))


def spinner_fig():
    return W.spinner()


def diff_table(full=False, shade=False):
    head = ['Difference'] + [str(c) for c in range(1, 7)]
    rows = []
    for r in range(1, 7):
        rows.append([str(r)] + [str(abs(r - c)) if (full or r <= 2 or r == c) else '' for c in range(1, 7)])
    sh = (lambda r, c: ('#CDE8F7' if c >= 1 and abs(r + 1 - c) <= 2 else '#FFE9B0') if c >= 1 else None) if shade else None
    return W.table_svg(head, rows, 'Difference table for two dice: first die down the side, second die across the top. ' + ('Complete table; the differences 0, 1 and 2 (Ali) are shaded blue and 3, 4 and 5 (Ben) are shaded yellow.' if shade else
                       'The cells in rows 1 and 2 and on the diagonal are filled in; the others are empty.'), [96] + [38] * 6, 16, 30, sh)


def winners_grid(rows, cols, cell, win, label):
    """A small table of results for the correct answer: cell(r, c) text, win(r, c) -> True for the cells shaded as the first player's."""
    return W.table_svg([''] + [str(c) for c in cols], [[str(r)] + [str(cell(r, c)) for c in cols] for r in rows], label, [54] + [40] * len(cols), 16, 30,
                       lambda i, c: ('#CDE8F7' if win(rows[i], cols[c - 1]) else '#FFE9B0') if c >= 1 else None)


def grid_fig(rows, cols, rt, ct, cell, label):
    return W.fg_grid(rows, cols, rt, ct, cell, label)


FAIR_SPLITS = [s for k in range(1, 6) for s in itertools.combinations(range(6), k) if sum(diff_counts()[d] for d in s) == 18]

ITEMS = [
    # ================= Start here (workbook Lesson 6, Q1 to Q5)
    dict(id='1a', tier='core', no='1(a)', type='fields', strand=PR, skill='probability as a fraction', svg=spinner_fig(),
         q="Ben's spinner has 8 equal parts: 3 red (R), 2 blue (B), 2 yellow (Y) and 1 green (G). Write the probability as a fraction in its simplest form.",
         frame='P(red) = {f1} / {f2}', answer=fr(prob(SPIN.count('R'), 8)), check=lambda: fr(prob(SPIN.count('R'), len(SPIN))),
         hint='How many parts are red? How many parts are there altogether? Is every part equally likely?',
         steps=['3 of the 8 equal parts are red.', 'P(red) = 3/8. It cannot be made simpler.'],
         src=['Write each probability as a fraction in its simplest form.']),
    dict(id='1b', tier='core', no='1(b)', type='fields', strand=PR, skill='probability of not', svg=spinner_fig(),
         q="Ben's spinner has 8 equal parts: 3 red (R), 2 blue (B), 2 yellow (Y) and 1 green (G). Write P(not yellow) as a fraction in its simplest form.",
         frame='P(not yellow) = {f1} / {f2}', answer=fr(prob(len([c for c in SPIN if c != 'Y']), 8)), check=lambda: fr(prob(len([c for c in SPIN if c != 'Y']), len(SPIN))),
         hint='Count the parts that are not yellow. Then make the fraction simpler if you can.',
         steps=['The parts that are not yellow are the red, blue and green ones: 3 + 2 + 1 = 6 parts.', 'P(not yellow) = 6/8 = 3/4 in simplest form.'],
         src=['(b) P(not yellow) =']),
    dict(id='1c', tier='core', no='1(c)', type='number', strand=CP, skill='expected number', answer=375, svg=spinner_fig(),
         q="Ben makes the spinner in code and spins it 1000 times. About how many reds do you expect?", check=lambda: int(prob(SPIN.count('R'), 8) * 1000),
         hint='What fraction of the spins should be red? Find that fraction of 1000.',
         steps=['P(red) = 3/8.', '3/8 of 1000 = 1000 ÷ 8 × 3 = 125 × 3 = 375.', 'About 375 reds.'],
         src=['Ben makes the spinner in code and spins it 1000 times. About how many reds do you expect?']),
    dict(id='1d', tier='core', no='1(d)', type='choice', strand=CP, skill='random results are close, not exact', options=['Yes, it is wrong', 'No, it is not wrong'], answer='No, it is not wrong', svg=spinner_fig(),
         q="Ben's program spins the spinner 1000 times. It says 362 reds. Compare 362 with the number you expected in (c). Ben says, “My program is wrong!” Do you agree?",
         check=lambda: 'No, it is not wrong' if abs(362 - 1000 * Fraction(3, 8)) < 2 * sd(1000, 3 / 8) else 'Yes, it is wrong',
         hint='Each spin is random. Would you expect a random count to land exactly on the expected number every time?',
         steps=['The expected number is 375 and the program says 362: only 13 away.', 'A random result is close to the expected number, not exactly on it, so the program is not wrong.'],
         src=['His program says 362 reds.']),
    dict(id='1d-why', tier='core', no='1(d) explain', type='selfcheck', strand=CP, skill='explaining random results', svg=spinner_fig(), label='1(d) why',
         q="Ben's program says 362 reds, and Ben says, “My program is wrong!” Explain what you think. Write your reason, then check it against the worked solution.",
         facts=dict(expected=375, seen=362, exact_one_in=40), check=lambda: dict(expected=int(Fraction(3, 8) * 1000), seen=362, exact_one_in=(lambda r: 40 if 35 <= r <= 45 else None)(1 / pmf(1000, 3 / 8, 375))),
         hint='Think about what "random" means. Would two runs of the program give exactly the same number?',
         steps=['Every spin is random, so the count of reds changes a little from run to run. It is close to 375, but not exactly 375.', '362 is only 13 away from 375, so the program is working.',
                'Even a perfect program lands exactly on 375 only about 1 run in 40.'],
         src=['His program says 362 reds.']),

    dict(id='2a', tier='core', no='2(a)', type='number', strand=CP, skill='predicting what code says', answer=500, svg=W.blocks('l6', COIN, COIN_LABEL),
         q='Predict what this code does. "pick random 1 to 2" gives 1 or 2, each with probability 1/2. About what number will it say?', check=lambda: int(W.expected_changes(COIN)),
         hint='How often is the random number 1? Then think about 1000 turns of the loop.',
         steps=['The random number is 1 half of the time, so "change heads by 1" happens about half of the 1000 turns.', '1/2 of 1000 = 500.', 'It will say about 500.'],
         src=['About what number will it say?']),
    dict(id='2b', tier='core', no='2(b)', type='choice', strand=CP, skill='random results are close, not exact', options=['Yes, it is broken', 'No, it is not broken'], answer='No, it is not broken', svg=W.blocks('l6', COIN, COIN_LABEL),
         q='Predict what this code does. Mei runs it 3 times and gets 513, 489 and 502. Is her code broken?',
         check=lambda: 'No, it is not broken' if all(abs(x - 500) < 2 * sd(1000, 0.5) for x in (513, 489, 502)) else 'Yes, it is broken',
         hint='Compare each of her numbers with what you expected in (a). Are they close?',
         steps=['The expected number is 500. Her numbers are 13, 11 and 2 away from it.', 'That is what we expect from random results, so her code is not broken.'],
         src=['Mei runs it 3 times and gets 513, 489 and 502.']),
    dict(id='2b-why', tier='core', no='2(b) explain', type='selfcheck', strand=CP, skill='explaining random results', svg=W.blocks('l6', COIN, COIN_LABEL), label='2(b) why',
         q='Mei runs the code 3 times and gets 513, 489 and 502. Explain what you think about her code. Write your reason, then check it against the worked solution.',
         facts=dict(exact_one_in=40), check=lambda: dict(exact_one_in=(lambda r: 40 if 35 <= r <= 45 else None)(1 / pmf(1000, 0.5, 500))),
         hint='What would you expect if the coin were fair? Should each run give exactly the same number?',
         steps=['The flips are random, so each run gives a slightly different count near 500.', 'Exactly 500 happens only about 1 run in 40.', 'Three results this close to 500 are what a working program gives.'],
         src=['Is her code broken? Explain.']),
    dict(id='2c', tier='core', no='2(c)', type='number', strand=CP, skill='expected number', answer=200, svg=W.blocks('l6', COIN, COIN_LABEL),
         q='If "pick random 1 to 2" is changed to "pick random 1 to 5", about what will it say?', check=lambda: int(W.expected_changes(coin_prog(5))),
         hint='Now the random number can be 1, 2, 3, 4 or 5. How often is it 1?',
         steps=['The random number is 1 for 1 turn in 5, so P = 1/5.', '1/5 of 1000 = 200.', 'It will say about 200.'],
         src=['If “pick random 1 to 2” is changed to “pick random 1 to 5”, about what will it say?']),

    dict(id='3a', tier='core', no='3(a)', type='text', strand=PR, skill='probability as a fraction', accept=['2/5', '4/10'], shown='2/5', equiv_frac=True,
         q='A bag has 4 red and 6 blue counters. You pick one without looking. What is the probability of picking red? Type it like 3/5, or in simplest form.',
         check=lambda: fs(prob(4, 4 + 6)),
         hint='How many counters are red? How many counters are there altogether?',
         steps=['There are 4 + 6 = 10 counters, and 4 of them are red.', 'P(red) = 4/10 = 2/5.'],
         src=['What is the probability of picking red?']),
    dict(id='3b', tier='core', no='3(b)', type='number', strand=PR, skill='changing a probability', answer=2,
         q='A bag has 4 red and 6 blue counters. How many red counters must be added so that P(red) = 1/2?',
         check=lambda: next(x for x in range(0, 100) if prob(4 + x, 4 + x + 6) == Fraction(1, 2)),
         hint='P(red) = 1/2 means half of the counters are red. How many red counters would match the 6 blue ones?',
         steps=['For P(red) = 1/2, the red and blue counters must be equal in number.', 'There are 6 blue counters, so there must be 6 red: 6 − 4 = 2 more.', '(Check: 6 red out of 12 counters is 1/2.)'],
         src=['How many red counters must be added so that P(red) = 1/2?']),

    dict(id='4r3', tier='core', no='4(a) row 3', type='fields', strand=PR, skill='listing the 36 outcomes', svg=diff_table(), label='4(a) row 3',
         q='The Difference Game. Roll two dice. The difference is the bigger number minus the smaller (0 if they are the same). Row 3 of the table is for a first die of 3. Fill in the empty cells of row 3, one for each second die.',
         frame='Second die 1: {f1}   2: {f2}   4: {f3}   5: {f4}   6: {f5}', answer=[abs(3 - c) for c in (1, 2, 4, 5, 6)], check=lambda: [abs(3 - c) for c in (1, 2, 4, 5, 6)],
         hint='Take the smaller number away from the bigger number. For a first die of 3 and a second die of 1, what is 3 take away 1?',
         steps=['3 and 1: 3 − 1 = 2. 3 and 2: 1. 3 and 4: 4 − 3 = 1. 3 and 5: 2. 3 and 6: 3.', 'Row 3 is 2, 1, 0, 1, 2, 3.'],
         src=['Complete the table.']),
    dict(id='4r4', tier='core', no='4(a) row 4', type='fields', strand=PR, skill='listing the 36 outcomes', svg=diff_table(), label='4(a) row 4',
         q='The Difference Game. The difference is the bigger number minus the smaller (0 if they are the same). Row 4 of the table is for a first die of 4. Fill in the empty cells of row 4.',
         frame='Second die 1: {f1}   2: {f2}   3: {f3}   5: {f4}   6: {f5}', answer=[abs(4 - c) for c in (1, 2, 3, 5, 6)], check=lambda: [abs(4 - c) for c in (1, 2, 3, 5, 6)],
         hint='Take the smaller number away from the bigger number each time.',
         steps=['4 and 1: 3. 4 and 2: 2. 4 and 3: 1. 4 and 5: 1. 4 and 6: 2.', 'Row 4 is 3, 2, 1, 0, 1, 2.'],
         src=['Complete the table.']),
    dict(id='4r5', tier='core', no='4(a) row 5', type='fields', strand=PR, skill='listing the 36 outcomes', svg=diff_table(), label='4(a) row 5',
         q='The Difference Game. The difference is the bigger number minus the smaller (0 if they are the same). Row 5 of the table is for a first die of 5. Fill in the empty cells of row 5.',
         frame='Second die 1: {f1}   2: {f2}   3: {f3}   4: {f4}   6: {f5}', answer=[abs(5 - c) for c in (1, 2, 3, 4, 6)], check=lambda: [abs(5 - c) for c in (1, 2, 3, 4, 6)],
         hint='Take the smaller number away from the bigger number each time.',
         steps=['5 and 1: 4. 5 and 2: 3. 5 and 3: 2. 5 and 4: 1. 5 and 6: 1.', 'Row 5 is 4, 3, 2, 1, 0, 1.'],
         src=['Complete the table.']),
    dict(id='4r6', tier='core', no='4(a) row 6', type='fields', strand=PR, skill='listing the 36 outcomes', svg=diff_table(), label='4(a) row 6',
         q='The Difference Game. The difference is the bigger number minus the smaller (0 if they are the same). Row 6 of the table is for a first die of 6. Fill in the empty cells of row 6.',
         frame='Second die 1: {f1}   2: {f2}   3: {f3}   4: {f4}   5: {f5}', answer=[abs(6 - c) for c in (1, 2, 3, 4, 5)], check=lambda: [abs(6 - c) for c in (1, 2, 3, 4, 5)],
         hint='Take the smaller number away from 6 each time.',
         steps=['6 and 1: 5. 6 and 2: 4. 6 and 3: 3. 6 and 4: 2. 6 and 5: 1.', 'Row 6 is 5, 4, 3, 2, 1, 0.'],
         src=['Complete the table.']),
    dict(id='4b-ali', tier='core', no='4(b) Ali', type='text', strand=PR, skill='probability from a table', svg=diff_table(), accept=['2/3', '24/36'], shown='2/3', equiv_frac=True, label='4(b) Ali',
         q='The Difference Game. Ali wins on a difference of 0, 1 or 2. Ben wins on 3, 4 or 5. Use the completed table of all 36 outcomes (complete it on paper if you need to). What is P(Ali wins)? Type it like 3/5.',
         check=lambda: fs(prob(len([1 for a, b in DICE if abs(a - b) <= 2]), 36)),
         hint='Count the cells of the table that show 0, 1 or 2. Out of how many cells?',
         steps=['Cells showing 0: 6. Showing 1: 10. Showing 2: 8.', 'Ali wins in 6 + 10 + 8 = 24 of the 36 cells.', 'P(Ali wins) = 24/36 = 2/3.'],
         sol_fig=lambda f: diff_table(True, True),
         src=['(b) P(Ali wins) =']),
    dict(id='4b-ben', tier='core', no='4(b) Ben', type='text', strand=PR, skill='probability from a table', svg=diff_table(), accept=['1/3', '12/36'], shown='1/3', equiv_frac=True, label='4(b) Ben',
         q='The Difference Game. Ali wins on a difference of 0, 1 or 2. Ben wins on 3, 4 or 5. Use the completed table of all 36 outcomes. What is P(Ben wins)? Type it like 3/5.',
         check=lambda: fs(prob(len([1 for a, b in DICE if abs(a - b) >= 3]), 36)),
         hint='Count the cells of the table that show 3, 4 or 5. Out of how many cells?',
         steps=['Cells showing 3: 6. Showing 4: 4. Showing 5: 2.', 'Ben wins in 6 + 4 + 2 = 12 of the 36 cells.', 'P(Ben wins) = 12/36 = 1/3.'],
         src=['P(Ben wins) =']),
    dict(id='4c', tier='core', no='4(c)', type='choice', strand=PR, skill='judging a game', options=['Fair', 'Not fair'], answer='Not fair',
         q='The Difference Game. Ali wins on a difference of 0, 1 or 2. Ben wins on 3, 4 or 5. Is the game fair?',
         check=lambda: 'Fair' if len([1 for a, b in DICE if abs(a - b) <= 2]) == len([1 for a, b in DICE if abs(a - b) >= 3]) else 'Not fair',
         hint='A game is fair when both players have the same probability of winning. Compare your two fractions from (b).',
         steps=['P(Ali wins) = 2/3 and P(Ben wins) = 1/3.', 'They are not equal, so the game is not fair.'],
         src=['Is the game fair? Explain.']),
    dict(id='4c-why', tier='core', no='4(c) explain', type='selfcheck', strand=PR, skill='explaining fairness', label='4(c) why',
         q='The Difference Game. Ali wins on a difference of 0, 1 or 2. Ben wins on 3, 4 or 5. Explain why the game is fair or not fair. Write your reason, then check it against the worked solution.',
         facts=dict(ali=24, ben=12, three_each=True), check=lambda: dict(ali=len([1 for a, b in DICE if abs(a - b) <= 2]), ben=len([1 for a, b in DICE if abs(a - b) >= 3]), three_each=True),
         hint='Each player has 3 differences, but are the 6 differences equally likely? Count how many outcomes each one has.',
         steps=['Each player wins on 3 differences, but the differences are not equally likely: 0 has 6 outcomes, 1 has 10, 2 has 8, 3 has 6, 4 has 4 and 5 has 2.', 'Ali wins on 24 of the 36 outcomes and Ben on 12.',
                'Ali is twice as likely to win, so the game is not fair, even though each has 3 differences.'],
         src=['Is the game fair? Explain.']),

    dict(id='5-gaps', tier='core', no='5 repeats', type='fields', strand=CP, skill='planning random code', svg=W.blocks('l6', PLAN, PLAN_LABEL), label='5 repeats',
         q='Plan your code. Fill the 3 gaps to count doubles in 1000 rolls of two dice. (A die shows 1 to 6. A double is when both dice show the same number.) First, the two "pick random 1 to ..." gaps, from the top.',
         frame='First gap: {f1}   second gap: {f2}', answer=[6, 6], check=lambda: [loop_needed(6), loop_needed(6)] if double_ok('a = b') else None,
         hint='Each die shows a whole number from 1 up to what number?',
         steps=['A die shows 1 to 6, so both gaps are 6: "pick random 1 to 6".'],
         src=['Fill the 3 gaps to count doubles in 1000 rolls of two dice.']),
    dict(id='5-test', tier='core', no='5 test', type='text', strand=CP, skill='planning random code', svg=W.blocks('l6', PLAN, PLAN_LABEL), accept=['a=b', 'a = b', 'b=a', 'b = a', 'a==b'], shown='a = b', label='5 test',
         q='Plan your code. The program must count doubles. Type the test for the last gap, the one after "if". (Type it like this: a + b = 7, which is a different test.)',
         check=lambda: 'a=b' if all(double_ok(c) for c in ('a=b', 'a = b', 'b=a', 'b = a', 'a==b')) and not double_ok('a < b') else None,
         hint='When is a roll a double? What must be true about the two numbers a and b?',
         steps=['A double means both dice show the same number, so a is equal to b.', 'The test is a = b.'],
         src=['A double is when both dice show the same number.']),
    dict(id='5-frac', tier='core', no='5(a) fraction', type='fields', strand=PR, skill='probability as a fraction', svg=W.blocks('l6', PLAN, PLAN_LABEL), label='5(a) frac',
         q='Plan your code. What is the probability that two dice show a double? Write the fraction in its simplest form.', frame='P(double) = {f1} / {f2}', answer=fr(prob(6, 36)),
         check=lambda: fr(prob(len([1 for a, b in DICE if a == b]), len(DICE))),
         hint='List the doubles (1 and 1, ...). How many are there out of the 36 equally likely outcomes?',
         steps=['There are 6 doubles: 1-1, 2-2, 3-3, 4-4, 5-5 and 6-6.', 'P(double) = 6/36 = 1/6.'],
         src=['About what number will it say? Show your fraction.']),
    dict(id='5a', tier='core', no='5(a)', type='number', strand=CP, skill='expected number', answer=167, svg=W.blocks('l6', PLAN, PLAN_LABEL),
         q='Plan your code. With the 3 gaps filled in correctly, about what number will the program say? Round to the nearest whole number.',
         check=lambda: round(W.expected_changes(W.fill(PLAN, [6, 6, 'a = b']))),
         hint='Find that fraction of 1000. The number must be a whole number.',
         steps=['The expected number is 1/6 of 1000 = 166 and 2/3.', 'A count must be a whole number, so we say about 167.'],
         src=['About what number will it say? Show your fraction.']),
    dict(id='5b', tier='core', no='5(b)', type='selfcheck', strand=CP, skill='explaining random results', svg=W.blocks('l6', PLAN, PLAN_LABEL),
         q='Plan your code. Why will the program not say exactly 1000 × 1/6? Write your reason, then check it against the worked solution.',
         facts=dict(whole_number=False), check=lambda: dict(whole_number=(Fraction(1000, 6).denominator == 1)),
         hint='Could a count of doubles ever be a number with a fraction? And is each run random?',
         steps=['1000 × 1/6 = 166 2/3, and a count must be a whole number.', 'Also, each run is random, so it lands near 167, but not exactly.'],
         src=['Why will it not say exactly 1000 × 1/6?']),

    dict(id='Xa', tier='core', no='Exit slip (a)', type='fields', strand=PR, skill='probability with two dice', label='Exit (a)',
         q='Roll two dice and add. What is the probability that the total is 8? Write the fraction in its simplest form.', frame='P(total 8) = {f1} / {f2}', answer=[5, 36],
         check=lambda: fr(prob(len([1 for a, b in DICE if a + b == 8]), 36)),
         hint='List the pairs of dice that make 8. A red die and a blue die give 36 equally likely pairs.',
         steps=['The totals of 8: 2 + 6, 3 + 5, 4 + 4, 5 + 3, 6 + 2. That is 5 pairs.', 'P(total 8) = 5/36.'],
         src=['What is the probability that the total is 8?']),
    dict(id='Xb', tier='core', no='Exit slip (b)', type='number', strand=CP, skill='expected number', answer=50, label='Exit (b)',
         q='Roll two dice and add. If you roll them 360 times, about how many totals of 8 do you expect?', check=lambda: int(prob(len([1 for a, b in DICE if a + b == 8]), 36) * 360),
         hint='Find the probability of a total of 8, then that fraction of 360.',
         steps=['P(total 8) = 5/36.', '5/36 of 360 = 360 ÷ 36 × 5 = 10 × 5 = 50.', 'About 50 eights.'],
         src=['If you roll them 360 times, about how many 8s do you expect?']),

    # ================= Investigation (printed on the Finish page)
    dict(id='I1', tier='invest', no='Investigation 1', type='choice', strand=PR, skill='is a two-outcome game fair', options=['Fair', 'Not fair'], answer='Fair', label='Inv 1',
         q='Is it always true? Ali says: “A game with only two outcomes is always fair.” Test him. First step: if you have a coin, flip it 10 times and tally heads and tails. Game (1): flip a coin, heads or tails. Is it fair?',
         check=lambda: 'Fair' if Fraction(1, 2) == Fraction(1, 2) else 'Not fair',
         hint='Are heads and tails equally likely? Compare the two probabilities.',
         steps=['P(heads) = 1/2 and P(tails) = 1/2.', 'They are equal, so the coin game is fair.'],
         src=['First step: flip a coin 10 times and tally heads and tails.']),
    dict(id='I2', tier='invest', no='Investigation 2', type='choice', strand=PR, skill='is a two-outcome game fair', options=['Fair', 'Not fair'], answer='Not fair', label='Inv 2',
         q='Ali says: “A game with only two outcomes is always fair.” Game (2): roll a dice. One player wins on six, the other wins on not six. Is it fair?',
         check=lambda: 'Fair' if prob(1, 6) == prob(5, 6) else 'Not fair',
         hint='List the six faces. On how many does each player win?',
         steps=['P(six) = 1/6 and P(not six) = 5/6.', 'They are not equal, so the game is not fair.'],
         src=['(2) Roll a dice: six or not six.']),
    dict(id='I3', tier='invest', no='Investigation 3', type='choice', strand=PR, skill='is a two-outcome game fair', options=['Fair', 'Not fair'], answer='Not fair', label='Inv 3',
         q='Ali says: “A game with only two outcomes is always fair.” Game (3): roll two dice. One player wins on a total of 7, the other wins on not 7. Is it fair? (List the 36 outcomes.)',
         check=lambda: 'Fair' if len([1 for a, b in DICE if a + b == 7]) * 2 == 36 else 'Not fair',
         hint='In how many of the 36 outcomes is the total 7?',
         steps=['A total of 7 happens in 6 of the 36 outcomes: 1 + 6, 2 + 5, 3 + 4, 4 + 3, 5 + 2, 6 + 1.', 'P(7) = 6/36 = 1/6 and P(not 7) = 30/36 = 5/6. Not equal, so the game is not fair.'],
         src=['(3) Roll two dice: total 7 or not 7.']),
    dict(id='I4', tier='invest', no='Investigation 4', type='choice', strand=PR, skill='testing a claim', options=['Yes', 'No'], answer='No', label='Inv 4',
         q='Ali says: “A game with only two outcomes is always fair.” You tested three games. Is Ali right?',
         check=lambda: 'No' if any(a != b for a, b in ((Fraction(1, 2), Fraction(1, 2)), (prob(1, 6), prob(5, 6)), (prob(6, 36), prob(30, 36)))) else 'Yes',
         hint='What does one game that is not fair tell you about “always”?',
         steps=['One game with two outcomes that is not fair is enough to show Ali is wrong.', 'Two outcomes does not mean two EQUAL chances.'],
         src=['Is Ali right?']),
    dict(id='I5', tier='invest', no='Investigation 5', type='selfcheck', strand=PR, skill='making a game fair', label='Inv 5',
         q='Change one unfair game to make it fair. Write your new rule and show that each player has the same probability. Then check it against the worked solution.',
         facts=dict(dice=(3, 3), two_dice=(18, 18)),
         check=lambda: dict(dice=(len([f for f in range(1, 7) if f <= 3]), len([f for f in range(1, 7) if f > 3])), two_dice=(len([1 for a, b in DICE if (a + b) % 2 == 0]), len([1 for a, b in DICE if (a + b) % 2 == 1]))),
         hint='A fair game needs the same number of equally likely outcomes for each player. How could you share the six faces of a dice?',
         steps=['One dice: one player wins on 1, 2 or 3 and the other on 4, 5 or 6: 3 faces each, 3/6 = 1/2 each.', 'Two dice: one player wins on an even total and the other on an odd total: 18 of the 36 outcomes each.', 'Any rule that gives each player the same number of outcomes works.'],
         src=['Change one unfair game to make it fair.']),

    # ================= Think harder (first three Think harder questions, then the one moved from Start here)
    dict(id='T1', tier='stretch', no='T1', type='text', strand=PR, skill='probability as a fraction', accept=['2/5', '4/10'], shown='2/5', equiv_frac=True,
         q='A spinner has 10 equal parts numbered 1 to 10. What is the probability of spinning a prime number? Type it like 3/5.',
         check=lambda: fs(prob(len([n for n in range(1, 11) if P.is_prime(n)]), 10)),
         hint='List the prime numbers from 1 to 10. Is 1 a prime number?',
         steps=['The primes from 1 to 10 are 2, 3, 5 and 7: 4 of the 10 parts.', 'P(prime) = 4/10 = 2/5.'],
         src=['A spinner has 10 equal parts numbered 1 to 10.']),
    dict(id='T2', tier='stretch', no='T2', type='text', strand=PR, skill='probability with two dice', accept=['1/9', '4/36'], shown='1/9', equiv_frac=True,
         svg=grid_fig([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 'first dice', 'second dice', 26, 'An empty 6 by 6 table for the two dice: first dice down the side, second dice across the top. Use a table like this on paper to find the totals.'),
         q='Roll two dice and add. What is the probability that the total is 9? Type it like 3/5. (The empty table is the one in your workbook: fill in the totals on paper if it helps.)',
         check=lambda: fs(prob(len([1 for a, b in DICE if a + b == 9]), 36)),
         hint='Fill in the 36 totals, or list the pairs of dice that make 9.',
         steps=['The pairs that make 9: 3 + 6, 4 + 5, 5 + 4, 6 + 3. That is 4 pairs.', 'P(total 9) = 4/36 = 1/9.'],
         src=['Roll two dice and add. What is the probability that the total is 9?']),
    dict(id='T3', tier='stretch', no='T3', type='number', strand=PR, skill='probability backwards', answer=15,
         q='A bag has 5 red counters and some blue counters. The probability of picking red is 1/4. How many blue counters are there?',
         check=lambda: next(b for b in range(0, 200) if prob(5, 5 + b) == Fraction(1, 4)),
         hint='If 5 counters are 1/4 of the bag, how many counters are in the whole bag?',
         steps=['5 red counters are 1/4 of the bag, so the whole bag has 5 × 4 = 20 counters.', 'The blue counters are 20 − 5 = 15.', '(Check: 5 out of 20 is 1/4.)'],
         src=['A bag has 5 red counters and some blue counters.']),
    dict(id='T4a', tier='stretch', no='T4(a)', type='number', strand=PR, skill='changing a probability', answer=10,
         q='A bag has 4 red and 6 blue counters. How many blue counters must be added so that P(red) = 1/5?',
         check=lambda: next(x for x in range(0, 200) if prob(4, 4 + 6 + x) == Fraction(1, 5)),
         hint='The 4 red counters must be 1/5 of the bag. How many counters should the bag hold?',
         steps=['4 red counters are 1/5 of the bag, so the bag must have 4 × 5 = 20 counters.', 'There are 10 counters now, so add 20 − 10 = 10 blue counters.', '(Check: 4/20 = 1/5.)'],
         src=['How many blue counters must be added so that P(red) = 1/5?']),
    dict(id='T4b', tier='stretch', no='T4(b)', type='selfcheck', strand=PR, skill='making a game fair', label='T4(b)',
         svg=diff_table(),
         q='In the Difference Game (Ali wins on 0, 1, 2; Ben on 3, 4, 5), change who wins on which differences so that the game is fair. Write the differences for Ali and for Ben, then check against the worked solution.',
         facts=FAIR_SPLITS, check=lambda: [s for k in range(1, 6) for s in itertools.combinations(range(6), k) if sum(diff_counts()[d] for d in s) == 18],
         hint='Count how many of the 36 outcomes each difference has. Each player needs the same number of outcomes.',
         steps=['The differences 0, 1, 2, 3, 4, 5 have 6, 10, 8, 6, 4 and 2 outcomes. A fair game gives each player 18 of the 36.', 'For example: Ali on 1, 3, 5 (10 + 6 + 2 = 18) and Ben on 0, 2, 4 (6 + 8 + 4 = 18).',
                'Or Ali on 1 and 2 (10 + 8 = 18) and Ben on 0, 3, 4, 5. Or Ali on 0, 1 and 5 (6 + 10 + 2 = 18) and Ben on 2, 3, 4.', 'Any split with 18 outcomes for each player works.'],
         src=['change who wins on which differences so that the game is fair']),

    # ================= Go further (last three Go further questions)
    dict(id='C1', tier='challenge', no='C1', type='selfcheck', open=True, marking_mode='open', strand=PR, skill='designing a fair game',
         q='Design a FAIR game for two players using one dice, two coins or a spinner. Write the rules and show with a list or table that each player has the same chance of winning. Then change ONE rule to make the game unfair, and say who is favoured. Then compare with the example in the worked solution.',
         hint='List every equally likely outcome. Share them so that each player gets the same number.',
         steps=['Open: many games work. Example: roll one dice. Player A wins on 1, 2 or 3 and player B wins on 4, 5 or 6: 3/6 each.', 'Change one rule: A also wins on 4. Now A has 4/6 and B has 2/6, so A is favoured.', 'Check that every outcome is listed and the winning outcomes add up to the whole.'],
         src=['Design a FAIR game for two players using one dice, two coins or a spinner.']),
    dict(id='C2a', tier='challenge', no='C2(a)', type='choice', strand=PR, skill='judging a game', options=['Fair', 'Not fair'], answer='Not fair', label='C2(a)',
         svg=grid_fig([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 'Mei', 'Ali', 26, 'An empty 6 by 6 table: Mei down the side, Ali across the top, for the two dice. Use a table like this on paper.'),
         q='Mei and Ali each roll one dice. Mei wins if her number is bigger. Ali wins if his number is bigger or the same. Is the game fair? (The empty table is the one in your workbook.)',
         check=lambda: 'Fair' if len([1 for m, a in DICE if m > a]) == len([1 for m, a in DICE if m <= a]) else 'Not fair',
         hint='Fill in the table of 36 outcomes, or count the outcomes in which Mei wins and the ones in which Ali wins.',
         steps=['Mei wins when her number is bigger: 15 of the 36 outcomes. Ali wins when his is bigger or the same: 15 + 6 = 21.', 'They are not equal, so the game is not fair.'],
         src=['Mei and Ali each roll one dice.']),
    dict(id='C2b', tier='challenge', no='C2(b)', type='text', strand=PR, skill='probability with two dice', accept=['5/12', '15/36'], shown='5/12', equiv_frac=True, label='C2(b)',
         svg=grid_fig([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 'Mei', 'Ali', 26, 'An empty 6 by 6 table: Mei down the side, Ali across the top, for the two dice. Use a table like this on paper.'),
         q='Mei and Ali each roll one dice. Mei wins if her number is bigger. Ali wins if his number is bigger or the same. What is the probability that Mei wins? Type it like 3/5.',
         check=lambda: fs(prob(len([1 for m, a in DICE if m > a]), 36)),
         hint='In how many of the 36 outcomes is Mei\'s number bigger? Look for a pattern row by row.',
         steps=['If Mei rolls 1, she wins in 0 outcomes; 2: 1 outcome; 3: 2; 4: 3; 5: 4; 6: 5.', '0 + 1 + 2 + 3 + 4 + 5 = 15 outcomes out of 36.', 'P(Mei wins) = 15/36 = 5/12.'],
         sol_fig=lambda f: winners_grid(range(1, 7), range(1, 7), lambda m, a: 'M' if m > a else 'A', lambda m, a: m > a, 'Results of Mei and Ali: M where Mei wins, A where Ali wins (blue is Mei); Mei wins 15 of 36'),
         src=['Is the game fair? What is the probability that Mei wins?']),
    dict(id='C3a', tier='challenge', no='C3(a)', type='choice', strand=PR, skill='judging a game', options=['Fair', 'Not fair'], answer='Not fair', label='C3(a)',
         svg=grid_fig([1, 2, 3], [1, 2, 3, 4], 'spinner A', 'spinner B', 30, 'An empty 3 by 4 table: spinner A down the side, spinner B across the top, to fill in each product.'),
         q='Spinner A has 3 equal parts: 1, 2, 3. Spinner B has 4 equal parts: 1, 2, 3, 4. Spin both and multiply. Even wins if the answer is even, Odd wins if it is odd. Is the game fair?',
         check=lambda: 'Fair' if len([1 for a in range(1, 4) for b in range(1, 5) if a * b % 2 == 0]) * 2 == 12 else 'Not fair',
         hint='Fill in the table of 12 products. How many are even and how many are odd?',
         steps=['There are 3 × 4 = 12 equally likely outcomes.', 'The product is odd only when both numbers are odd: 2 × 2 = 4 outcomes. The other 8 are even.', 'The two players do not have the same number of outcomes, so the game is not fair.'],
         src=['Spinner A has 3 equal parts: 1, 2, 3.']),
    dict(id='C3b', tier='challenge', no='C3(b)', type='text', strand=PR, skill='probability with two spinners', accept=['1/3', '4/12'], shown='1/3', equiv_frac=True, label='C3(b)',
         svg=grid_fig([1, 2, 3], [1, 2, 3, 4], 'spinner A', 'spinner B', 30, 'An empty 3 by 4 table: spinner A down the side, spinner B across the top, to fill in each product.'),
         q='Spinner A has 3 equal parts: 1, 2, 3. Spinner B has 4 equal parts: 1, 2, 3, 4. Spin both and multiply. What is the probability that Odd wins? Type it like 3/5.',
         check=lambda: fs(prob(len([1 for a in range(1, 4) for b in range(1, 5) if a * b % 2 == 1]), 12)),
         hint='When is a product odd? Count those outcomes out of all 12.',
         steps=['The product is odd only when both numbers are odd: A is 1 or 3 and B is 1 or 3: 4 outcomes.', 'P(Odd wins) = 4/12 = 1/3, and P(Even wins) = 8/12 = 2/3.'],
         sol_fig=lambda f: winners_grid(range(1, 4), range(1, 5), lambda a, b: a * b, lambda a, b: (a * b) % 2 == 1, 'The 12 products: odd ones (blue) are 1, 3, 3 and 9; the other 8 are even (yellow)'),
         src=['Spinner A has 3 equal parts: 1, 2, 3.']),
]

assert FAIR_SPLITS and (1, 3, 5) in FAIR_SPLITS and (1, 2) in FAIR_SPLITS and (0, 1, 5) in FAIR_SPLITS
assert diff_counts() == {0: 6, 1: 10, 2: 8, 3: 6, 4: 4, 5: 2}

for _it in ITEMS:
    if _it.get('frame'):
        _it['frame'] = W.nb(_it['frame'])

P.finish(ITEMS)

# ---------------------------------------------------------------- variant families (every combination is run against an independent oracle at build time)
VARIANTS = {
    '1c': dict(base=dict(n=8, a=3, t=1000),
               tpl=dict(vars=dict(n=[4, 5, 8, 10], a=[1, 2, 3], t=[40, 80, 120, 200, 400, 1000]),
                        q="Ben's spinner has {n} equal parts and {a} of them are red. He spins it {t} times in code. About how many reds do you expect?", answer='a*t//n',
                        hint='What fraction of the spins should be red? Find that fraction of {t}.',
                        steps=['P(red) = {a}/{n}.', '{t} ÷ {n} × {a} = {ans}.', 'About {ans} reds.']),
               oracle=lambda e: int(Fraction(e['a'], e['n']) * e['t'])),
    '2c': dict(base=dict(k=5, t=1000),
               tpl=dict(vars=dict(k=[2, 4, 5, 10], t=[100, 200, 400, 1000]),
                        q='A counter goes up by 1 each time "pick random 1 to {k}" gives 1. The code repeats {t} times. About what number will the counter end on?', answer='t//k',
                        hint='The random number is 1 for 1 turn in {k}. Find that fraction of {t}.',
                        steps=['P(1) = 1/{k}.', '{t} ÷ {k} = {ans}.', 'About {ans}.']),
               oracle=lambda e: int(Fraction(1, e['k']) * e['t'])),
    '3b': dict(base=dict(r=4, d=2),
               tpl=dict(vars=dict(r=[2, 3, 4, 5], d=[2, 4, 6]), derive=dict(b='r+d'),
                        q='A bag has {r} red and {b} blue counters. How many red counters must be added so that P(red) = 1/2?', answer='d',
                        hint='P(red) = 1/2 means the red and blue counters must be equal in number.',
                        steps=['There are {b} blue counters, so there must be {b} red.', '{b} − {r} = {ans} more red counters.']),
               oracle=lambda e: next(x for x in range(0, 100) if Fraction(e['r'] + x, e['r'] + x + e['r'] + e['d']) == Fraction(1, 2))),
    'T3': dict(base=dict(r=5, k=4),
               tpl=dict(vars=dict(r=[2, 3, 4, 5, 6, 7, 8], k=[3, 4, 5, 6]),
                        q='A bag has {r} red counters and some blue counters. The probability of picking red is 1/{k}. How many blue counters are there?', answer='r*(k-1)',
                        hint='If {r} counters are 1/{k} of the bag, how many counters are in the whole bag?',
                        steps=['{r} red counters are 1/{k} of the bag, so the whole bag has {r} × {k} counters.', 'The blue counters are the rest: {ans}.']),
               oracle=lambda e: next(b for b in range(0, 300) if Fraction(e['r'], e['r'] + b) == Fraction(1, e['k']))),
    'Xb': dict(base=dict(s=6, t=360),
               tpl=dict(vars=dict(s=[2, 3, 4, 5, 6, 7], t=[36, 72, 108, 180, 360, 720]), derive=dict(w='s-1'),
                        q='Roll two dice and add. If you roll them {t} times, about how many totals of {s} do you expect?', answer='w*t//36',
                        hint='List the pairs of dice that make {s}. Out of 36 pairs, what fraction is that? Then find that fraction of {t}.',
                        steps=['A total of {s} can be made in {w} ways out of 36.', '{t} ÷ 36 × {w} = {ans}.', 'About {ans}.']),
               oracle=lambda e: int(Fraction(len([1 for a, b in DICE if a + b == e['s']]), 36) * e['t'])),
}
