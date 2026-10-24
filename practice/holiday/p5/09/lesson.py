"""Online practice for Level 5 (Primary 5, ages 10 to 12) holiday lesson 9: Patterns and Number Sense ("Pattern Generalisers").

The questions are the ones printed in the Level 5 holiday workbook, lesson 9: Start here Q1 to Q5 (p5/content/l9.js, workbook()), the Investigation
(p5/content/inv.js), Think harder A1 to A4 (the first four 'stretch' questions of p5/content/l9.js qbank) and Go further B1 to B3 (the last three
'challenge' questions) and the "Make up your own" prompt (gaps.js), in the printed order, exactly as p5/workbook_html.js prints them.  Every answer is recomputed
by an INDEPENDENT checker below: the chairs and sticks and dots of every pattern are COUNTED from the drawn shapes (free sides of square tables, the lines of the matchstick
houses, the dots of a diamond), a rule is found by trying every pair of whole numbers, a total of tickets, coins or quiz marks is found by trying every split, the digits of the
counting numbers are written out one after another; never by copying the printed answer.  build_holiday.py stops if a checker and the printed answer differ.
The figures are drawn by practice/holiday/p5/p5fig5.py.
"""
import os, sys
HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE_, '..', '..'))
sys.path.insert(0, os.path.join(HERE_, '..'))
from hlib import *          # noqa: E402,F401
from p5lib import *         # noqa: E402,F401
import p5fig3 as G3         # noqa: E402  (decimal answers)
import p5fig5 as G          # noqa: E402

META = dict(level=5, lesson=9, key='p5', title='Pattern Generalisers', workbook_title='PATTERN GENERALISERS', topic='Patterns and Number Sense', strand='Patterns and number sense',
            sources=['p5/content/l9.js', 'p5/content/inv.js', 'p5/content/gaps.js'],
            intro=['A growing pattern: find what stays the same and what grows each time. Then say the rule in words, like this: number of sticks = 3 × figure number + 1. '
                   'To go backwards from a total, undo the steps in reverse order: take away first, then divide. With two kinds of things and one total, guess and check with a table, '
                   'or suppose they are all one kind and see how far you are from the real total.',
                   'Type the number in the box (a unit after the number is fine). Money can have a decimal point, like 3.5. '
                   'Some questions ask you to explain: write your idea, then compare it with the model answer after you submit.'])
ST = 'Patterns and number sense'
F = Fraction


def D(**k):
    k.setdefault('strand', ST)
    return k


# ---------------------------------------------------------------- checkers: count the drawn shapes, try every split (no formula copied from a printed answer)
def chairs_row(n):
    """Chairs for n square tables in a row, one on every free side: count the sides of each table that touch no other table."""
    return G.chairs_by_free_sides(G.tables_cells(n))


def sticks_row(n):
    """Matchsticks for n houses joined in a row: the lines of the drawing (a shared wall is one stick)."""
    return len(G.house_sticks(n))


for _n in (1, 2, 3, 7):
    assert G.drawn_chairs(G.tables_fig((_n,))) == chairs_row(_n), _n          # the drawn circles are the counted chairs
    assert G.drawn_sticks(G.houses_fig((_n,))) == sticks_row(_n), _n          # the drawn lines are the counted sticks
assert (chairs_row(1), chairs_row(2), chairs_row(3)) == (4, 6, 8) and (sticks_row(1), sticks_row(2), sticks_row(3)) == (6, 11, 16)


def fit_rule(f, ns=range(1, 9)):
    """The one pair (a, b) of whole numbers with a * n + b = f(n) for every n tested."""
    found = [(a, b) for a in range(0, 13) for b in range(0, 13) if all(a * n + b == f(n) for n in ns)]
    assert len(found) == 1, found
    return found[0]


def added_each_time(f, upto=12):
    d = {f(n + 1) - f(n) for n in range(1, upto)}
    assert len(d) == 1, d
    return d.pop()


def houses_for(sticks):
    """The greatest number of houses that can be made from `sticks` sticks, and the sticks left over."""
    h = 0
    while sticks_row(h + 1) <= sticks:
        h += 1
    return h, sticks - sticks_row(h)


def tables_for(people):
    found = [n for n in range(1, 400) if chairs_row(n) == people]
    assert len(found) == 1, people
    return found[0]


def tickets(a, c, n, total):
    """Adult tickets a dollars, child tickets c dollars, n tickets, total dollars: the number of adult tickets (every split is tried)."""
    found = [k for k in range(n + 1) if a * k + c * (n - k) == total]
    assert len(found) == 1, (a, c, n, total)
    return found[0]


def coins_b(a, b, n, total):
    """n coins of a cents and b cents worth `total` cents: the number of b-cent coins (every split is tried)."""
    found = [k for k in range(n + 1) if a * (n - k) + b * k == total]
    assert len(found) == 1, (a, b, n, total)
    return found[0]


def quiz_scores(n, right, lost):
    """The score for 0, 1, 2 ... wrong answers when every question is answered."""
    return [right * (n - w) - lost * w for w in range(n + 1)]


def quiz_correct(n, right, lost, scored):
    found = [n - w for w, s in enumerate(quiz_scores(n, right, lost)) if s == scored]
    assert len(found) == 1, (n, right, lost, scored)
    return found[0]


def quiz_blank(n, blank, right, lost, scored):
    """n questions, `blank` left blank (0 marks), the rest answered: the number correct (every split of the answered questions is tried)."""
    found = [c for c in range(n - blank + 1) if right * c - lost * (n - blank - c) == scored]
    assert len(found) == 1, (n, blank, right, lost, scored)
    return found[0]


def odd_total(k):
    return sum(2 * i + 1 for i in range(k))


def even_total(k):
    return sum(2 * i + 2 for i in range(k))


def diamond_dots(f):
    """Dots in figure f: the rows are 1, 3, ... 2f - 1, ... 3, 1; the drawing is counted too."""
    rows = list(range(1, 2 * f, 2)) + list(range(2 * f - 3, 0, -2))
    n = sum(rows)
    assert G.drawn_dots(G.diamond_fig((f,))) == n, f
    return n


def digit_at(p):
    return int(''.join(str(i) for i in range(1, 400))[p - 1])


def yellow_in(n):
    return sum(1 for k in range(1, n + 1) if G.BEADS[(k - 1) % 6][0] == 'Y')


assert (diamond_dots(1), diamond_dots(2), diamond_dots(3)) == (1, 5, 13)

MONEY = dict(money=True, places=(2,))


def money(v):
    return G3.dec_accepts(F(v), **MONEY)


TABLES_Q = 'At a hawker centre, square tables are pushed together in a row. One chair goes on each free side.'
HOUSES_Q = 'Matchstick houses are joined in a row.'
TICKET_Q = 'Guess and check with a table. Adult tickets to the Science Centre cost $12 each and child tickets cost $7 each. A group buys 15 tickets for $145 altogether.'
COIN_Q = 'Siti has 30 coins. They are all 20¢ and 50¢ coins, worth $10.20 altogether.'
QUIZ_Q = 'A quiz has 20 questions. Each correct answer scores 5 marks. For each wrong answer, 2 marks are taken away.'
BEAD_Q = 'Beads repeat in the order red, red, blue, yellow, yellow, yellow.'
ODD_Q = 'Add the first odd numbers: 1, then 1 + 3, then 1 + 3 + 5, then 1 + 3 + 5 + 7, and so on.'
EVEN_Q = 'Now add the first EVEN numbers instead: 2, then 2 + 4, then 2 + 4 + 6, and so on.'
TAB_SVG, HOU_SVG = G.tables_fig(), G.houses_fig()

ITEMS = [
    # ================= Start here (workbook lesson 9: Q1 to Q5)
    D(id='1a', tier='core', no='1(a)', label='1(a)', type='fields', skill='counting a growing pattern', answer=[10, 12, 22],
      q=TABLES_Q + '\nHow many chairs are there for 4 tables, 5 tables and 10 tables? (The picture shows 1, 2 and 3 tables.)', svg=TAB_SVG,
      frame='4 tables: {f1} chairs     5 tables: {f2} chairs     10 tables: {f3} chairs', check=lambda: [chairs_row(4), chairs_row(5), chairs_row(10)],
      hint='Count the chairs for 1, 2 and 3 tables in the picture. What happens to the number of chairs each time one more table joins the row?',
      steps=['1 table has 4 chairs, 2 tables have 6 chairs and 3 tables have 8 chairs.', 'Each new table adds 2 chairs, one above and one below.',
             '4 tables: 8 + 2 = 10 chairs. 5 tables: 10 + 2 = 12 chairs. 10 tables: 8 + 7 × 2 = 22 chairs.'],
      src=[TABLES_Q, '4 tables: ______ chairs. 5 tables: ______ chairs. 10 tables: ______ chairs.']),
    D(id='1b', tier='core', no='1(b)', label='1(b)', type='fields', skill='rule in words', answer=[2, 2],
      q=TABLES_Q + '\nSay the rule in words. Fill in the boxes. (The rule must work for 1, 2 and 3 tables.)', svg=TAB_SVG,
      frame='chairs = {f1} × tables + {f2}', check=lambda: list(fit_rule(chairs_row)),
      hint='Try your rule on the pictures. It must give the right number of chairs for 1 table, for 2 tables and for 3 tables.',
      steps=['Each table adds 2 chairs, so the number of tables is multiplied by 2.', 'The 2 chairs at the two ends are always there, so add 2.',
             'Check with 3 tables: 2 × 3 + 2 = 8 chairs, as in the picture. The rule is: chairs = 2 × tables + 2.'],
      src=[TABLES_Q, 'Rule in words: chairs = ______ × tables + ______']),
    D(id='1c', tier='core', no='1(c)', label='1(c)', type='number', skill='working backwards from a total', answer=24,
      q=TABLES_Q + '\nHow many tables are needed to seat exactly 50 people? (One person sits on each chair.)', svg=TAB_SVG,
      check=lambda: tables_for(50), hint='Use the rule for the chairs backwards. Undo the last step of the rule first.',
      steps=['50 people need 50 chairs.', 'Chairs = 2 × tables + 2, so take away the 2 end chairs first: 50 − 2 = 48.', '48 = 2 × tables, so tables = 48 ÷ 2 = 24. Check: 2 × 24 + 2 = 50.'],
      src=['How many tables are needed to seat exactly 50 people?']),
    D(id='1d', tier='core', no='1(d)', label='1(d)', type='choice', skill='doubling does not double', options=['Yes, Ben is right', 'No, Ben is not right'], answer='No, Ben is not right',
      q=TABLES_Q + '\nBen says, “If I put twice as many tables in the row, twice as many people can sit.” Is he right?', svg=TAB_SVG,
      check=lambda: 'Yes, Ben is right' if chairs_row(20) == 2 * chairs_row(10) else 'No, Ben is not right',
      hint='Test it on a small case. Does 2 tables seat twice as many people as 1 table?',
      steps=['10 tables seat 2 × 10 + 2 = 22 people, so “twice as many” would be 44.', '20 tables seat 2 × 20 + 2 = 42 people, not 44.',
             'Doubling the people counts the 2 end chairs twice, but there are only 2 end chairs in the whole row.'],
      src=['Ben says, “10 tables seat 22 people, so 20 tables seat 44.” Is he right? Explain.']),
    D(id='1d2', tier='core', no='1(d) 20 tables', label='1(d) 20', type='number', skill='using the rule', answer=42,
      q=TABLES_Q + '\nHow many people can sit at 20 tables in one long row?', svg=TAB_SVG,
      check=lambda: chairs_row(20), hint='Use the rule for the chairs, or count the chairs for a few tables and carry on the pattern.',
      steps=['The rule is chairs = 2 × tables + 2.', '2 × 20 + 2 = 42 people.'],
      src=['Ben says, “10 tables seat 22 people, so 20 tables seat 44.” Is he right? Explain.']),
    D(id='1dw', tier='core', no='1(d) why', label='1(d) why', type='selfcheck', open=False, skill='explaining a pattern', facts=(22, 42),
      q=TABLES_Q + '\nExplain what you notice about the number of people when the number of tables is doubled, for example from 10 tables to 20 tables. Write your idea, then compare it with the model answer.',
      svg=TAB_SVG, check=lambda: (chairs_row(10), chairs_row(20)), hint='Work out the number of people for 10 tables and for 20 tables. Is the second number double the first?',
      steps=['10 tables seat 22 people and 20 tables seat 42 people. Double 22 is 44, so 42 is not double.',
             'Every table adds 2 chairs, but the 2 end chairs are only there once. Doubling the number of people counts the 2 end chairs twice.',
             'A good answer says that doubling the tables does not double the chairs, and why (the end chairs).'],
      src=['Ben says, “10 tables seat 22 people, so 20 tables seat 44.” Is he right? Explain.']),

    D(id='2a', tier='core', no='2(a)', label='2(a)', type='number', skill='counting a growing pattern', answer=5,
      q=HOUSES_Q + '\nEach new house adds how many sticks? (Type the number.)', svg=HOU_SVG, sol_fig=lambda f: G.houses_fig((1, 2, 3), hl=2),
      check=lambda: added_each_time(sticks_row), hint='Count the sticks for 1 house and for 2 houses. How many more did the second house need?',
      steps=['1 house uses 6 sticks and 2 houses use 11 sticks.', 'The new house is built next to the house before it, so it shares a wall with it. It needs 11 − 6 = 5 more sticks.',
             '3 houses use 16 sticks, which is 5 more again.'],
      src=[HOUSES_Q, 'Each new house adds']),
    D(id='2a2', tier='core', no='2(a) why', label='2(a) why', type='selfcheck', open=False, skill='explaining a pattern', facts=(5, 6),
      q=HOUSES_Q + '\nThe first house uses 6 sticks. Explain why each new house does not add 6 sticks. Write your idea, then compare it with the model answer.', svg=HOU_SVG,
      sol_fig=lambda f: G.houses_fig((1, 2, 3), hl=2), check=lambda: (added_each_time(sticks_row), sticks_row(1)),
      hint='Look at where the second house stands. Is there a stick that the first house already has?',
      steps=['The new house stands next to the house before it, so it uses that house’s right wall. That wall is already there.', 'So the new house needs only 6 − 1 = 5 new sticks.'],
      src=[HOUSES_Q, 'Why not 6?']),
    D(id='2b', tier='core', no='2(b)', label='2(b)', type='fields', skill='rule in words', answer=[5, 1],
      q=HOUSES_Q + '\nSay the rule in words for the number of sticks. Fill in the boxes. (The rule must work for 1, 2 and 3 houses.)', svg=HOU_SVG,
      frame='sticks = {f1} × houses + {f2}', check=lambda: list(fit_rule(sticks_row)),
      hint='Try your rule on the pictures. It must give the right number of sticks for 1 house, for 2 houses and for 3 houses.',
      steps=['Each new house adds 5 sticks, so the number of houses is multiplied by 5.', 'The 1 extra stick is the left wall of the first house, which no other house shares: 5 × 1 + 1 = 6 sticks.',
             'Check with 3 houses: 5 × 3 + 1 = 16 sticks, as in the picture. The rule is: sticks = 5 × houses + 1.'],
      src=[HOUSES_Q, 'Rule: sticks = ______ × houses + ______.']),
    D(id='2b2', tier='core', no='2(b) 20 houses', label='2(b) 20', type='number', skill='using the rule', answer=101,
      q=HOUSES_Q + '\nFor 20 houses, how many sticks are needed? (Type the number.)', svg=HOU_SVG,
      check=lambda: sticks_row(20), hint='Use the rule for the number of sticks, or carry on the pattern from the pictures.',
      steps=['The rule is sticks = 5 × houses + 1.', '5 × 20 + 1 = 100 + 1 = 101 sticks.'],
      src=['For 20 houses: ______ sticks.']),
    D(id='2c', tier='core', no='2(c)', label='2(c)', type='fields', skill='working backwards from a total', answer=[39, 4],
      q=HOUSES_Q + '\nMei has 200 sticks. What is the greatest number of houses she can make, and how many sticks are left over?', svg=HOU_SVG,
      frame='Houses: {f1}     Sticks left over: {f2}', check=lambda: list(houses_for(200)), hint='Use the rule for the sticks backwards: undo the last step of the rule first.',
      steps=['Take away the 1 extra stick first: 200 − 1 = 199.', '199 ÷ 5 = 39 with 4 left over, so 39 houses can be made.', '39 houses use 5 × 39 + 1 = 196 sticks, so 200 − 196 = 4 sticks are left over.'],
      src=['Mei has 200 sticks. Greatest number of houses she can make? Sticks left over?']),

    D(id='3t', tier='core', no='3 (try)', label='3 try', type='number', skill='guess and check', answer=155,
      q=TICKET_Q + '\nA first try: 5 adult tickets and 10 child tickets cost $60 + $70 = $130, which is too little. Now try 10 adult tickets and 5 child tickets. What do they cost altogether? (Type the number of dollars.)',
      check=lambda: 12 * 10 + 7 * 5, hint='Multiply the number of adult tickets by $12 and the number of child tickets by $7. Then add.',
      steps=['10 adult tickets cost 10 × $12 = $120.', '5 child tickets cost 5 × $7 = $35.', '$120 + $35 = $155.'],
      src=[TICKET_Q, '$60 + $70 = $130', 'too little']),
    D(id='3c', tier='core', no='3 (compare)', label='3 compare', type='choice', skill='guess and check', options=['too much', 'too little'], answer='too much',
      q=TICKET_Q + '\nWork out the cost of 10 adult tickets and 5 child tickets. Is it too much or too little compared with $145?',
      check=lambda: 'too much' if 12 * 10 + 7 * 5 > 145 else 'too little', hint='Work out the cost of the ten adult tickets and the five child tickets, then compare it with $145.',
      steps=['10 adult tickets cost $120 and 5 child tickets cost $35, which is $155 altogether.', '$155 is more than $145, so it is too much.',
             'An adult ticket costs more than a child ticket, so the group must have fewer adult tickets.'],
      src=[TICKET_Q, 'Too much or too little?']),
    D(id='3', tier='core', no='3 (answer)', label='3 answer', type='fields', skill='guess and check', answer=[8, 7],
      q=TICKET_Q + '\nHow many adult tickets and how many child tickets do they buy? Keep guessing and checking (a table helps) until the cost is exactly $145.',
      frame='Adult tickets: {f1}     Child tickets: {f2}', check=lambda: [tickets(12, 7, 15, 145), 15 - tickets(12, 7, 15, 145)],
      hint='The adult tickets and the child tickets must add up to 15. Change your guess by 1 and see what happens to the total cost.',
      steps=['5 adult and 10 child: $60 + $70 = $130, too little.', '10 adult and 5 child: $120 + $35 = $155, too much.', '8 adult and 7 child: $96 + $49 = $145. This is exactly right.',
             'Each adult ticket in place of a child ticket adds $5. From 5 adult tickets ($130) we need 3 more swaps to reach $145.'],
      src=[TICKET_Q, 'Answer: ______ adult tickets and ______ child tickets.']),

    D(id='4a1', tier='core', no='4(a) worth', label='4(a) worth', type='text', skill='supposition', accept=money(F(600, 100)) + ['600 cents', '600¢', '600c'], shown='6.00',
      q=COIN_Q + '\nIf all 30 coins were 20¢ coins, how much would they be worth? (Type the number of dollars, like 3.50.)',
      check=lambda: G3.dec_text(F(30 * 20, 100)), hint='Multiply the number of coins by the value of one coin. Then change cents to dollars.',
      steps=['30 coins × 20¢ = 600¢.', '600¢ = $6.00.'],
      src=[COIN_Q, 'If all 30 coins were 20¢: worth']),
    D(id='4a2', tier='core', no='4(a) adds', label='4(a) adds', type='number', skill='supposition', answer=30,
      q='Siti has 30 coins. They are all 20¢ and 50¢ coins.\nEach time you change a 20¢ coin for a 50¢ coin, the total goes up. By how many cents? (Type the number.)',
      check=lambda: (50 * 1 + 20 * 29) - (50 * 0 + 20 * 30), hint='Take away a 20¢ coin and put in a 50¢ coin. How much more money is that?',
      steps=['Changing a 20¢ coin for a 50¢ coin: 50¢ − 20¢ = 30¢ more.'],
      src=['Each change of a 20¢ for a 50¢ adds']),
    D(id='4b', tier='core', no='4(b)', label='4(b)', type='number', skill='supposition', answer=14,
      q=COIN_Q + '\nHow many 50¢ coins does Siti have? (Type the number.)', check=lambda: coins_b(20, 50, 30, 1020),
      hint='How far is $10.20 from what 30 coins of 20¢ would be worth? Each change of a coin moves the total by the same amount.',
      steps=['If all 30 coins were 20¢, they would be worth $6.00.', '$10.20 − $6.00 = $4.20 more.', 'Each change of a 20¢ coin for a 50¢ coin adds 30¢, and 420¢ ÷ 30¢ = 14 changes.',
             'So 14 of the coins are 50¢ coins (and 16 are 20¢ coins).'],
      src=['How many 50¢ coins does Siti have? Show your working and check.']),
    D(id='4bc', tier='core', no='4(b) check', label='4(b) check', type='selfcheck', open=False, skill='checking against every fact', facts=(14, 16),
      q=COIN_Q + '\nCheck your answer for the 50¢ coins against BOTH facts: the number of coins and the money. Write what you check, then compare it with the model answer.',
      check=lambda: (coins_b(20, 50, 30, 1020), 30 - coins_b(20, 50, 30, 1020)), hint='If you know how many 50¢ coins there are, how many 20¢ coins are there? What are all the coins worth?',
      steps=['14 fifty-cent coins are worth 14 × 50¢ = 700¢ = $7.00.', '16 twenty-cent coins are worth 16 × 20¢ = 320¢ = $3.20.', '14 + 16 = 30 coins, and $7.00 + $3.20 = $10.20. Both facts are true.'],
      src=['Show your working and check.']),

    D(id='5a', tier='core', no='5(a)', label='5(a)', type='number', skill='supposition with marks taken away', answer=15,
      q=QUIZ_Q + ' Ali answered every question and scored 65 marks.\nHow many questions did Ali get correct? (Type the number.)', check=lambda: quiz_correct(20, 5, 2, 65),
      hint='Suppose he got them all correct first. What would he score? How far is that from 65?',
      steps=['If Ali got every question correct he would score 20 × 5 = 100 marks.', 'He scored 65, which is 100 − 65 = 35 marks less.',
             'Each wrong answer loses the 5 marks and has 2 marks taken away as well, so it costs 7 marks. 35 ÷ 7 = 5 wrong answers.', '20 − 5 = 15 correct. Check: 15 × 5 = 75, and 75 − 5 × 2 = 65.'],
      src=['A quiz has 20 questions. Each correct answer scores 5 marks. For each wrong answer, 2 marks are taken away. Ali answered every question and scored 65 marks.',
           'How many questions did Ali get correct?']),
    D(id='5b1', tier='core', no='5(b) list', label='5(b) list', type='fields', skill='listing the possible scores', answer=[93, 86, 79],
      q='Mei also answered every question in the quiz (20 questions, 5 marks for each correct answer, 2 marks taken away for each wrong one).\nStart here: all correct scores 100. Each wrong answer takes off 7. Write the scores for 1, 2 and 3 wrong answers.',
      frame='1 wrong: {f1}     2 wrong: {f2}     3 wrong: {f3}', check=lambda: quiz_scores(20, 5, 2)[1:4],
      hint='Start at 100 and take off 7 each time.', steps=['0 wrong answers: 100 marks.', '1 wrong answer: 100 − 7 = 93.', '2 wrong answers: 93 − 7 = 86.', '3 wrong answers: 86 − 7 = 79.'],
      src=['Start here: all correct scores 100. Each wrong answer takes off 7. Write the scores for 0, 1, 2, 3 wrong: 100,']),
    D(id='5b2', tier='core', no='5(b) 80', label='5(b) 80', type='choice', skill='testing a claim', options=['Yes, 80 could be her score', 'No, 80 cannot be her score'], answer='No, 80 cannot be her score',
      q='Mei also answered every question in the quiz. All correct scores 100 and each wrong answer takes off 7. Mei says she scored 80 marks.\nCould 80 be her score?',
      check=lambda: 'Yes, 80 could be her score' if 80 in quiz_scores(20, 5, 2) else 'No, 80 cannot be her score',
      hint='Keep going down the list of possible scores. Do you land on 80, or do you jump over it?',
      steps=['The possible scores are 100, 93, 86, 79, 72 and so on: each one is 7 less than the one before.', '80 is not in the list: the scores jump from 86 to 79.'],
      src=['Mei also answered every question and says she scored 80 marks. Why must she be wrong?', 'Is 80 in your list?']),
    D(id='5b3', tier='core', no='5(b) why', label='5(b) why', type='selfcheck', open=False, skill='explaining', facts=(False,),
      q='Mei also answered every question in the quiz. All correct scores 100 and each wrong answer takes off 7. Mei says she scored 80 marks.\nExplain what you find out about Mei’s score of 80. Write your idea, then compare it with the model answer.',
      check=lambda: (80 in quiz_scores(20, 5, 2),), hint='Think about the numbers you can get by taking 7 away from 100 again and again.',
      steps=['Every possible score is 100 take away a number of 7s: 100, 93, 86, 79, 72 and so on.', '100 − 80 = 20, and 20 is not a multiple of 7, so no number of wrong answers gives a score of 80.',
             'So Mei must be wrong.'],
      src=['Mei also answered every question and says she scored 80 marks. Why must she be wrong?']),

    # ================= Investigation: Is it always true? Test and explain
    D(id='C0', tier='invest', no='C (easy first step)', label='C easy', type='number', skill='adding odd numbers', answer=9,
      q='Is it always true? Test and explain.\nEasy first step: 1 = 1 and 1 + 3 = 4. What is 1 + 3 + 5? (Type the number.)', check=lambda: odd_total(3),
      hint='Add the next odd number to the total before it.', steps=['1 + 3 = 4.', '4 + 5 = 9.'],
      src=['Easy first step: fill in the first three totals: 1 = 1, 1 + 3 = 4, 1 + 3 + 5 =']),
    D(id='Ca', tier='invest', no='C(a)', label='C(a)', type='fields', skill='adding odd numbers', answer=[16, 25, 36],
      q=ODD_Q + ' Make a table of the totals.\nWhat is the total of the first 4 odd numbers, the first 5 and the first 6? (Type the numbers.)',
      frame='first 4 odd numbers: {f1}     first 5: {f2}     first 6: {f3}', check=lambda: [odd_total(4), odd_total(5), odd_total(6)],
      hint='Keep adding the next odd number to the total before.',
      steps=['The odd numbers are 1, 3, 5, 7, 9, 11.', 'The totals go 1, 4, 9, 16, 25, 36: 9 + 7 = 16, 16 + 9 = 25, 25 + 11 = 36.'],
      src=['Add the first odd numbers: 1, then 1 + 3, then 1 + 3 + 5, then 1 + 3 + 5 + 7. Make a table of the first 6 totals. What do you notice?']),
    D(id='Ca2', tier='invest', no='C(a) kind', label='C(a) kind', type='choice', skill='noticing a pattern', options=['square numbers', 'even numbers', 'multiples of 4', 'cube numbers'], answer='square numbers',
      q='Look at the totals of the first 1, 2, 3, 4, 5 and 6 odd numbers (1, then 1 + 3, then 1 + 3 + 5 and so on). What kind of numbers are they?',
      check=lambda: [k for k, ok in {'square numbers': lambda t: any(i * i == t for i in range(1, 50)), 'even numbers': lambda t: t % 2 == 0,
                                     'multiples of 4': lambda t: t % 4 == 0, 'cube numbers': lambda t: any(i ** 3 == t for i in range(1, 20))}.items()
                     if all(ok(odd_total(j)) for j in range(1, 7))][0],
      hint='Check each choice against all six totals, not just one or two.',
      steps=['The totals are 1, 4, 9, 16, 25 and 36.', '1 × 1 = 1, 2 × 2 = 4, 3 × 3 = 9, 4 × 4 = 16, 5 × 5 = 25 and 6 × 6 = 36: they are square numbers.',
             'They are not all even (1 and 9 are odd), not all multiples of 4 (9 is not) and not cube numbers (4 is not).'],
      src=['What do you notice?']),
    D(id='Ca3', tier='invest', no='C(a) 10', label='C(a) 10', type='number', skill='using a pattern', answer=100,
      q='Use the pattern in the totals to find the total of the first 10 odd numbers, 1 + 3 + 5 + … + 19. (Type the number.)', check=lambda: odd_total(10),
      hint='Look at how each total is related to the number of odd numbers that were added.',
      steps=['The total of the first 6 odd numbers is 6 × 6 = 36. In the same way the total of the first 10 odd numbers is 10 × 10 = 100.',
             'Check by adding in pairs: (1 + 19) + (3 + 17) + (5 + 15) + (7 + 13) + (9 + 11) = 5 × 20 = 100.'],
      src=['What do you notice?']),
    D(id='Cb', tier='invest', no='C(b)', label='C(b)', type='choice', skill='is it always true', options=['Yes, it is always true', 'No, it stops working for some number'], answer='Yes, it is always true',
      q='You found a pattern in the totals of the first odd numbers. Does it keep working for 100 odd numbers, for 1000 odd numbers, for any number? Is it always true?',
      sol_fig=lambda f: G.dot_squares_fig(4),
      check=lambda: 'Yes, it is always true' if all(odd_total(k) == k * k for k in range(1, 3001)) else 'No, it stops working for some number',
      hint='Test the pattern on one more total that you have not done yet, such as the first 7 odd numbers.',
      steps=['Yes. Each new odd number is an L-shaped border of dots round a square of dots: 3 dots round a 1 by 1 square, 5 dots round a 2 by 2 square, 7 dots round a 3 by 3 square.',
             'The L-shaped border turns an n by n square into an (n + 1) by (n + 1) square, every time.', 'So the total of the first n odd numbers is always n × n.'],
      src=['Is it always true? Use a picture of square dots (add an L-shaped border each time) to explain why.']),
    D(id='Cb2', tier='invest', no='C(b) why', label='C(b) why', type='selfcheck', open=False, skill='explaining with a picture', facts=(1, 4, 9, 16),
      q='Use a picture of square dots to explain why the pattern of the totals works. Each time, add an L-shaped border of dots. Draw it on paper if it helps. Write your idea, then compare it with the model answer.',
      sol_fig=lambda f: G.dot_squares_fig(4), check=lambda: tuple(odd_total(k) for k in range(1, 5)),
      hint='Start with 1 dot. How many dots does the L-shaped border need to make a 2 by 2 square? Then a 3 by 3 square?',
      steps=['1 dot is a 1 by 1 square. An L-shaped border of 3 dots makes a 2 by 2 square (4 dots). A border of 5 dots makes a 3 by 3 square (9 dots). A border of 7 dots makes a 4 by 4 square (16 dots).',
             'Each L-shaped border is the next odd number of dots, so adding odd numbers builds bigger and bigger squares.', 'That is why the totals are 1 × 1, 2 × 2, 3 × 3, 4 × 4 and so on, every time.'],
      src=['Is it always true? Use a picture of square dots (add an L-shaped border each time) to explain why.']),
    D(id='Cc1', tier='invest', no='C(c)', label='C(c)', type='fields', skill='adding even numbers', answer=[12, 20, 30, 42],
      q=EVEN_Q + '\nWhat is the total of the first 3 even numbers, the first 4, the first 5 and the first 6? (Type the numbers.)',
      frame='first 3 even numbers: {f1}     first 4: {f2}     first 5: {f3}     first 6: {f4}', check=lambda: [even_total(3), even_total(4), even_total(5), even_total(6)],
      hint='Keep adding the next even number to the total before.',
      steps=['The even numbers are 2, 4, 6, 8, 10, 12.', 'The totals go 2, 6, 12, 20, 30, 42: 6 + 6 = 12, 12 + 8 = 20, 20 + 10 = 30, 30 + 12 = 42.'],
      src=['What if you add the first EVEN numbers instead (2, then 2 + 4, then 2 + 4 + 6 …)?']),
    D(id='Cc2', tier='invest', no='C(c) 20', label='C(c) 20', type='number', skill='predicting with a pattern', answer=420,
      q=EVEN_Q + '\nUse a pattern to predict the total of the first 20 even numbers, 2 + 4 + … + 40. (Type the number.)', check=lambda: even_total(20),
      hint='Compare each total with the number of even numbers that were added. Is there a pattern like the one for the odd numbers?',
      steps=['The totals of the first 1, 2, 3, 4, 5, 6 even numbers are 2, 6, 12, 20, 30, 42. Each one is the number of even numbers times the next number: 1 × 2, 2 × 3, 3 × 4, 4 × 5, 5 × 6, 6 × 7.',
             'For the first 20 even numbers: 20 × 21 = 420.'],
      src=['Use it to predict the total of the first 20 even numbers, then check it another way.']),
    D(id='Cc3', tier='invest', no='C(c) rule', label='C(c) rule', type='selfcheck', open=False, skill='a rule in words', facts=(420,),
      q='Find a rule in words for the total of the first even numbers. Then check your prediction for the first 20 even numbers a different way. Write your idea, then compare it with the model answer.',
      check=lambda: (even_total(20),), hint='Think about a rule for the odd numbers that you found. What is different for the even numbers? Each even number is double an ordinary counting number.',
      steps=['The total of the first n even numbers is n × (n + 1): 1 × 2 = 2, 2 × 3 = 6, 3 × 4 = 12 and so on.', 'For 20 even numbers: 20 × 21 = 420.',
             'Another way to check: the even numbers are 2 × (1 + 2 + 3 + … + 20) = 2 × 210 = 420. Or: the first 20 odd numbers add to 400, and each even number is 1 more than the odd number before it, so 400 + 20 = 420.'],
      src=['Find a rule in words. Use it to predict the total of the first 20 even numbers, then check it another way.']),

    # ================= Think harder (A1 to A4)
    D(id='A1c', tier='stretch', no='A1 colour', label='A1 colour', type='choice', skill='repeating pattern', options=['red', 'blue', 'yellow'], answer='red',
      q=BEAD_Q + '\nWhat colour is the 50th bead?', svg=G.beads_fig(2),
      check=lambda: G.bead_at(50), hint='The pattern repeats every 6 beads. Where does the 50th bead fall in a group of 6?',
      steps=['The beads come in groups of 6: red, red, blue, yellow, yellow, yellow.', '8 full groups use 8 × 6 = 48 beads. Bead 49 is the first bead of the next group (red) and bead 50 is the second (red).', 'The 50th bead is red.'],
      src=['Beads repeat in the order red, red, blue, yellow, yellow, yellow. What colour is the 50th bead?']),
    D(id='A1y', tier='stretch', no='A1 yellow', label='A1 yellow', type='number', skill='repeating pattern', answer=49,
      q=BEAD_Q + '\nHow many yellow beads are in the first 100 beads? (Type the number.)', svg=G.beads_fig(2),
      check=lambda: yellow_in(100), hint='How many yellow beads are in one group of 6? How many full groups fit into 100 beads, and how many beads are left over?',
      steps=['16 full groups of 6 beads use 96 beads. Each group has 3 yellow beads: 16 × 3 = 48 yellow beads.', 'The last 4 beads (97 to 100) are red, red, blue, yellow: 1 more yellow bead.', '48 + 1 = 49 yellow beads.'],
      src=['How many yellow beads are in the first 100?']),
    D(id='A2', tier='stretch', no='A2', label='A2', type='number', skill='counting a growing pattern', answer=96,
      q='40 square tables in one long row seat 82 people (one chair on each free side).\nHow many people can sit if the 40 tables are put in 8 separate rows, each with 5 tables? (Type the number.)',
      sol_fig=lambda f: G.rows_fig(8, 5), check=lambda: 8 * chairs_row(5),
      hint='How many people does a single row of 5 tables seat? Count the chairs on its free sides.',
      steps=['One row of 5 tables has 5 chairs along the top, 5 along the bottom and 2 at the ends: 12 chairs.', '8 rows seat 8 × 12 = 96 people.',
             'One long row seats only 82. Every row has two ends, so more rows means more end chairs.'],
      src=['40 square tables in one long row seat 2 × 40 + 2 = 82 people. How many can sit if the tables are put in 8 rows of 5 tables instead?']),
    D(id='A3', tier='stretch', no='A3', label='A3', type='number', skill='supposition', answer=12,
      q='A farm has chickens and goats. There are 35 heads and 94 legs.\nHow many goats are there? (Type the number.)', check=lambda: [g for g in range(36) if 4 * g + 2 * (35 - g) == 94][0],
      hint='Suppose they are all chickens. How many legs would there be? How far is that from 94?',
      steps=['If all 35 animals were chickens there would be 35 × 2 = 70 legs.', '94 − 70 = 24 legs short. Each goat in place of a chicken adds 2 legs.', '24 ÷ 2 = 12 goats (and 23 chickens). Check: 48 + 46 = 94 legs.'],
      src=['A farm has chickens and goats. There are 35 heads and 94 legs. How many goats are there?']),
    D(id='A4a', tier='stretch', no='A4 totals', label='A4 totals', type='fields', skill='adding odd numbers', answer=[4, 9, 16],
      q='Work out these sums.', frame='1 + 3 = {f1}     1 + 3 + 5 = {f2}     1 + 3 + 5 + 7 = {f3}', check=lambda: [odd_total(2), odd_total(3), odd_total(4)],
      hint='Add the numbers one at a time.', steps=['1 + 3 = 4.', '4 + 5 = 9.', '9 + 7 = 16.'],
      src=['Work out 1 + 3, 1 + 3 + 5 and 1 + 3 + 5 + 7.']),
    D(id='A4w', tier='stretch', no='A4 notice', label='A4 notice', type='selfcheck', open=False, skill='noticing a pattern', facts=(4, 9, 16),
      q='Work out 1 + 3, then 1 + 3 + 5, then 1 + 3 + 5 + 7. What do you notice about the totals? Write your idea, then compare it with the model answer.',
      check=lambda: (odd_total(2), odd_total(3), odd_total(4)), hint='Compare each total with the number of odd numbers that were added.',
      steps=['The totals are 4, 9 and 16. Each one is the number of odd numbers added times itself: 2 × 2, 3 × 3 and 4 × 4. They are square numbers.'],
      src=['What do you notice?']),
    D(id='A4b', tier='stretch', no='A4 first 20', label='A4 first 20', type='number', skill='using a pattern', answer=400,
      q='Use the pattern you noticed in 1 + 3, 1 + 3 + 5 and 1 + 3 + 5 + 7 to add the first 20 odd numbers, 1 + 3 + … + 39. (Type the number.)', check=lambda: odd_total(20),
      hint='How many odd numbers are being added? How are the totals you found related to that number?',
      steps=['The total of the first 2, 3 and 4 odd numbers is 2 × 2, 3 × 3 and 4 × 4.', 'So the total of the first 20 odd numbers is 20 × 20 = 400. (Each new odd number adds an L-shaped layer to a square of dots.)'],
      src=['Use it to add the first 20 odd numbers, 1 + 3 + … + 39.']),

    # ================= Go further (B1 to B3)
    D(id='B1', tier='challenge', no='B1', label='B1', type='number', skill='a dot pattern', answer=61,
      q='A dot pattern makes diamonds. Figure 1 has 1 dot. Figure 2 has rows of 1, 3 and 1 dots (5 dots). Figure 3 has rows of 1, 3, 5, 3 and 1 dots (13 dots).\nHow many dots are in figure 6? (Type the number.)',
      svg=G.diamond_fig((1, 2, 3)), sol_fig=lambda f: G.diamond_fig((6,)), check=lambda: diamond_dots(6),
      hint='Find how many dots each figure adds to the one before. Or think about the rows: the middle row has the most dots.',
      steps=['The numbers of dots go 1, 5, 13, 25, 41, 61. Each figure adds 4, 8, 12, 16, 20 dots.', 'Another way: each figure is two squares of dots. Figure 6 is 6 × 6 and 5 × 5, so 36 + 25 = 61.'],
      src=['A dot pattern makes diamonds. Figure 1 has 1 dot. Figure 2 has rows of 1, 3 and 1 dots (5 dots). Figure 3 has rows of 1, 3, 5, 3 and 1 dots (13 dots). How many dots are in figure 6?']),
    D(id='B2', tier='challenge', no='B2', label='B2', type='number', skill='supposition with blanks', answer=18,
      q='A quiz has 25 questions. A correct answer scores 4 marks, 1 mark is taken away for each wrong answer, and a blank scores 0. Mei left 3 questions blank and scored 68.\nHow many did she get correct? (Type the number.)',
      check=lambda: quiz_blank(25, 3, 4, 1, 68), hint='How many questions did Mei answer? Suppose she got all of those correct. What would she score?',
      steps=['She answered 25 − 3 = 22 questions.', 'If all 22 were correct she would score 22 × 4 = 88 marks.', '68 is 20 marks less. Each wrong answer loses 4 marks and has 1 taken away, so it costs 5 marks. 20 ÷ 5 = 4 wrong answers.',
             '22 − 4 = 18 correct. Check: 18 × 4 = 72 and 72 − 4 = 68.'],
      src=['A quiz has 25 questions. A correct answer scores 4 marks, 1 mark is taken away for each wrong answer, and a blank scores 0. Mei left 3 questions blank and scored 68. How many did she get correct?']),
    D(id='B3', tier='challenge', no='B3', label='B3', type='number', skill='digits of the counting numbers', answer=5,
      q='Ali writes the counting numbers one after another without spaces: 123456789101112131415…\nWhat is the 100th digit he writes? (Type the digit.)', check=lambda: digit_at(100),
      hint='How many digits do the one-digit numbers use? Then how many digits does each two-digit number use?',
      steps=['The numbers 1 to 9 use 9 digits. That leaves 100 − 9 = 91 digits.', 'Each two-digit number uses 2 digits. 45 two-digit numbers (10 to 54) use 90 digits.', 'The 100th digit is the first digit of the next number, 55. It is 5.'],
      src=['Ali writes the counting numbers one after another without spaces: 123456789101112131415… What is the 100th digit he writes?']),
    D(id='pose', tier='challenge', no='Make up your own', label='Make up', type='selfcheck', open=True, marking_mode='open', skill='making up a problem',
      q='Make up a growing pattern with dots or matchsticks. Draw figures 1, 2 and 3 on paper. Then work out figure 10 yourself.',
      hint='Start with a small shape and decide what you add each time. Count the dots or sticks in figures 1, 2 and 3 first.',
      steps=['This question is open: many patterns are right.', 'Check your rule on figures 1, 2 and 3 before you use it for figure 10.',
             'Sample: matchstick triangles in a row use 3, 5, 7 sticks, so sticks = 2 × figure number + 1, and figure 10 uses 21 sticks.'],
      src=['Make up a growing pattern with dots or matchsticks. Draw figures 1, 2 and 3, and ask a partner for figure 10.']),
]


# ---------------------------------------------------------------- variants: a template with an oracle that counts, searches or writes out the digits
def _o_1a(e):
    return dict(f1=chairs_row(e['a']), f2=chairs_row(e['b']), f3=chairs_row(e['c']))


def _o_1c(e):
    return tables_for(e['P'])


def _o_2b2(e):
    return sticks_row(e['h'])


def _o_2c(e):
    h, left = houses_for(e['S'])
    return dict(f1=h, f2=left)


def _o_3(e):
    k = tickets(e['a'], e['c'], e['n'], e['a'] * e['k'] + e['c'] * (e['n'] - e['k']))
    return dict(f1=k, f2=e['n'] - k)


def _o_4b(e):
    return coins_b(e['a'], e['b'], e['n'], e['a'] * (e['n'] - e['k']) + e['b'] * e['k'])


def _o_5a(e):
    return quiz_correct(e['n'], e['r'], e['w'], e['r'] * e['k'] - e['w'] * (e['n'] - e['k']))


def _o_ca3(e):
    return odd_total(e['k'])


def _o_cc2(e):
    return even_total(e['k'])


def _o_a1y(e):
    return yellow_in(e['N'])


def _o_a2(e):
    assert chairs_row(e['r'] * e['m']) == 2 * e['r'] * e['m'] + 2
    return e['r'] * chairs_row(e['m'])


def _o_a3(e):
    legs = 2 * e['h'] + 2 * e['g']
    return [g for g in range(e['h'] + 1) if 4 * g + 2 * (e['h'] - g) == legs][0]


def _o_a4b(e):
    return odd_total(e['k'])


def _o_b1(e):
    return diamond_dots(e['f'])


def _o_b2(e):
    return quiz_blank(e['n'], e['b'], e['r'], e['w'], e['r'] * e['c'] - e['w'] * (e['n'] - e['b'] - e['c']))


def _o_b3(e):
    return digit_at(e['p'])


finish(ITEMS)

VARIANTS = {
    '1a': dict(
        base=dict(a=4, b=5, c=10),
        tpl=dict(vars=dict(a=[3, 4], b=[5, 7, 8], c=[9, 10, 12, 15]),
                 q=TABLES_Q + '\nHow many chairs are there for {a} tables, {b} tables and {c} tables? (The picture shows 1, 2 and 3 tables.)',
                 frame='{a} tables: {f1} chairs     {b} tables: {f2} chairs     {c} tables: {f3} chairs', answers=dict(f1='2 * a + 2', f2='2 * b + 2', f3='2 * c + 2'),
                 hint='Count the chairs for 1, 2 and 3 tables in the picture. What happens to the number of chairs each time one more table joins the row?',
                 steps=['1 table has 4 chairs, 2 tables have 6 chairs and 3 tables have 8 chairs.', 'Each new table adds 2 chairs, one above and one below.', 'The numbers of chairs are {ans}.'],
                 fig=TAB_SVG),
        oracle=_o_1a),
    '1c': dict(
        base=dict(P=50),
        tpl=dict(vars=dict(P=[30, 40, 50, 60, 72]),
                 q=TABLES_Q + '\nHow many tables are needed to seat exactly {P} people? (One person sits on each chair.)', answer='(P - 2) / 2',
                 hint='Use the rule for the chairs backwards. Undo the last step of the rule first.',
                 steps=['{P} people need {P} chairs.', 'Chairs = 2 × tables + 2, so take away the 2 end chairs first, then divide by 2.', 'The number of tables is {ans}.'],
                 fig=TAB_SVG),
        oracle=_o_1c),
    '2b2': dict(
        base=dict(h=20),
        tpl=dict(vars=dict(h=[10, 15, 20, 30, 50]),
                 q=HOUSES_Q + '\nFor {h} houses, how many sticks are needed? (Type the number.)', answer='5 * h + 1',
                 hint='Use the rule for the number of sticks, or carry on the pattern from the pictures.',
                 steps=['The rule is sticks = 5 × houses + 1.', '5 × {h} + 1 = {ans} sticks.'], fig=HOU_SVG),
        oracle=_o_2b2),
    '2c': dict(
        base=dict(S=200),
        tpl=dict(vars=dict(S=[133, 148, 187, 200, 241, 266]),
                 q=HOUSES_Q + '\nMei has {S} sticks. What is the greatest number of houses she can make, and how many sticks are left over?',
                 frame='Houses: {f1}     Sticks left over: {f2}', answers=dict(f1='(S - 1) // 5', f2='(S - 1) % 5'),
                 hint='Use the rule for the sticks backwards: undo the last step of the rule first.',
                 steps=['Take away the 1 extra stick first, then see how many groups of 5 sticks you can make.', 'The greatest number of houses and the sticks left over are {ans}.'], fig=HOU_SVG),
        oracle=_o_2c),
    '3': dict(
        base=dict(a=12, c=7, n=15, k=8),
        tpl=dict(vars=dict(a=[9, 10, 12, 15], c=[4, 6, 7], n=[12, 15, 20], k=[5, 6, 7, 8, 9]), derive=dict(T='a * k + c * (n - k)', d='a - c'),
                 q='Guess and check with a table. Adult tickets to the Science Centre cost ${a} each and child tickets cost ${c} each. A group buys {n} tickets for ${T} altogether.\nHow many adult tickets and how many child tickets do they buy? Keep guessing and checking (a table helps) until the cost is exactly ${T}.',
                 frame='Adult tickets: {f1}     Child tickets: {f2}', answers=dict(f1='k', f2='n - k'),
                 hint='The adult tickets and the child tickets must add up to {n}. Change your guess by 1 and see what happens to the total cost.',
                 steps=['Try some numbers of adult tickets. The adult and child tickets always add up to {n}.', 'Each adult ticket in place of a child ticket adds ${d} to the total.', 'The tickets are {ans} (adult, then child).'], paper=True),
        oracle=_o_3),
    '4b': dict(
        base=dict(a=20, b=50, n=30, k=14),
        tpl=dict(vars=dict(a=[10, 20], b=[40, 50], n=[20, 24, 30], k=[8, 10, 12, 14]), derive=dict(T='a * (n - k) + b * k', allA='n * a', gap='a * (n - k) + b * k - n * a', chg='b - a'),
                 q='Siti has {n} coins. They are all {a}¢ and {b}¢ coins, worth {T} cents altogether.\nHow many {b}¢ coins does Siti have? (Type the number.)', answer='k',
                 hint='How far is {T} cents from what {n} coins of {a}¢ would be worth? Each change of a coin moves the total by the same amount.',
                 steps=['If all {n} coins were {a}¢ they would be worth {allA} cents.', 'The real total is {gap} cents more. Each change of a {a}¢ coin for a {b}¢ coin adds {chg} cents.',
                        '{gap} ÷ {chg} = {ans}, so {ans} of the coins are {b}¢ coins.']),
        oracle=_o_4b),
    '5a': dict(
        base=dict(n=20, r=5, w=2, k=15),
        tpl=dict(vars=dict(n=[20, 25, 30], r=[4, 5, 6], w=[2, 3], k=[16, 17, 18, 19]), derive=dict(s='r * k - w * (n - k)', full='n * r', cost='r + w', gap='n * r - (r * k - w * (n - k))', wrong='n - k'),
                 q='A quiz has {n} questions. Each correct answer scores {r} marks. For each wrong answer, {w} marks are taken away. Ali answered every question and scored {s} marks.\nHow many questions did Ali get correct? (Type the number.)',
                 answer='k', hint='Suppose he got them all correct first. What would he score? How far is that from {s}?',
                 steps=['If Ali got every question correct he would score {n} × {r} = {full} marks.', 'He scored {s}, which is {gap} marks less. Each wrong answer costs {r} + {w} = {cost} marks.',
                        '{gap} ÷ {cost} = {wrong} wrong answers, so he got {ans} correct.']),
        oracle=_o_5a),
    'Ca3': dict(
        base=dict(k=10),
        tpl=dict(vars=dict(k=[8, 10, 12, 15, 20]), derive=dict(last='2 * k - 1'),
                 q='Use the pattern in the totals to find the total of the first {k} odd numbers, 1 + 3 + 5 + … + {last}. (Type the number.)', answer='k * k',
                 hint='Look at how each total is related to the number of odd numbers that were added.',
                 steps=['The total of the first n odd numbers is n × n, so the total of the first {k} odd numbers is {k} × {k} = {ans}.']),
        oracle=_o_ca3),
    'Cc2': dict(
        base=dict(k=20),
        tpl=dict(vars=dict(k=[8, 10, 12, 15, 20]), derive=dict(last='2 * k'),
                 q=EVEN_Q + '\nUse a pattern to predict the total of the first {k} even numbers, 2 + 4 + … + {last}. (Type the number.)', answer='k * (k + 1)',
                 hint='Compare each total with the number of even numbers that were added. Is there a pattern like the one for the odd numbers?',
                 steps=['The total of the first n even numbers is n × (n + 1).', 'For the first {k} even numbers the total is {ans}.']),
        oracle=_o_cc2),
    'A1y': dict(
        base=dict(N=100),
        tpl=dict(vars=dict(N=[46, 58, 77, 87, 100, 107]),
                 q=BEAD_Q + '\nHow many yellow beads are in the first {N} beads? (Type the number.)', answer='N // 6 * 3 + N % 6 - 3',
                 hint='How many yellow beads are in one group of 6? How many full groups fit into {N} beads, and how many beads are left over?',
                 steps=['Each full group of 6 beads has 3 yellow beads. Count the full groups, then look at the beads left over: red, red, blue, yellow, yellow.', 'The number of yellow beads is {ans}.'],
                 fig=G.beads_fig(2)),
        oracle=_o_a1y),
    'A2': dict(
        base=dict(r=8, m=5),
        tpl=dict(vars=dict(r=[4, 6, 8, 10], m=[3, 4, 5, 6]), derive=dict(T='r * m', S='2 * r * m + 2'),
                 q='{T} square tables in one long row seat {S} people (one chair on each free side).\nHow many people can sit if the {T} tables are put in {r} separate rows, each with {m} tables? (Type the number.)',
                 answer='r * (2 * m + 2)', hint='How many people does a single row of {m} tables seat? Count the chairs on its free sides.',
                 steps=['One row of {m} tables has {m} chairs along the top, {m} along the bottom and 2 at the ends.', '{r} rows seat {r} times that: {ans} people.'], paper=True),
        oracle=_o_a2),
    'A3': dict(
        base=dict(h=35, g=12),
        tpl=dict(vars=dict(h=[30, 35, 40, 45], g=[8, 12, 15, 18]), derive=dict(L='2 * h + 2 * g', allc='2 * h', short='2 * g'),
                 q='A farm has chickens and goats. There are {h} heads and {L} legs.\nHow many goats are there? (Type the number.)', answer='g',
                 hint='Suppose they are all chickens. How many legs would there be? How far is that from {L}?',
                 steps=['If all {h} animals were chickens there would be {allc} legs.', '{L} − {allc} = {short} legs short. Each goat in place of a chicken adds 2 legs.', '{short} ÷ 2 = {ans} goats.']),
        oracle=_o_a3),
    'A4b': dict(
        base=dict(k=20),
        tpl=dict(vars=dict(k=[10, 15, 20, 25, 30]), derive=dict(last='2 * k - 1'),
                 q='Use the pattern you noticed in 1 + 3, 1 + 3 + 5 and 1 + 3 + 5 + 7 to add the first {k} odd numbers, 1 + 3 + … + {last}. (Type the number.)', answer='k * k',
                 hint='How many odd numbers are being added? How are the totals you found related to that number?',
                 steps=['The total of the first n odd numbers is n × n.', 'So the total of the first {k} odd numbers is {k} × {k} = {ans}.']),
        oracle=_o_a4b),
    'B1': dict(
        base=dict(f=6),
        tpl=dict(vars=dict(f=[4, 5, 6, 7, 8]),
                 q='A dot pattern makes diamonds. Figure 1 has 1 dot. Figure 2 has rows of 1, 3 and 1 dots (5 dots). Figure 3 has rows of 1, 3, 5, 3 and 1 dots (13 dots).\nHow many dots are in figure {f}? (Type the number.)',
                 answer='f * f + (f - 1) * (f - 1)', hint='Find how many dots each figure adds to the one before. Or think about the rows: the middle row has the most dots.',
                 steps=['Each figure is two squares of dots. Figure {f} is {f} × {f} and one smaller square.', 'The number of dots in figure {f} is {ans}.'], fig=G.diamond_fig((1, 2, 3))),
        oracle=_o_b1),
    'B2': dict(
        base=dict(n=25, b=3, r=4, w=1, c=18),
        tpl=dict(vars=dict(n=[20, 25, 30], b=[2, 3, 4], r=[4, 5], w=[2, 3], c=[13, 14, 15]), derive=dict(s='r * c - w * (n - b - c)', ans_q='n - b', full='(n - b) * r', cost='r + w', gap='(n - b) * r - (r * c - w * (n - b - c))', wrong='n - b - c'),
                 q='A quiz has {n} questions. A correct answer scores {r} marks, {w} marks are taken away for each wrong answer, and a blank scores 0. Mei left {b} questions blank and scored {s}.\nHow many did she get correct? (Type the number.)',
                 answer='c', hint='How many questions did Mei answer? Suppose she got all of those correct. What would she score?',
                 steps=['She answered {ans_q} questions. If all of them were correct she would score {full} marks.', '{s} is {gap} marks less. Each wrong answer costs {r} + {w} = {cost} marks.', '{gap} ÷ {cost} = {wrong} wrong answers, so {ans_q} − {wrong} = {ans} correct.']),
        oracle=_o_b2),
    'B3': dict(
        base=dict(p=100),
        tpl=dict(vars=dict(p=[50, 60, 80, 100, 110, 120, 150]),
                 q='Ali writes the counting numbers one after another without spaces: 123456789101112131415…\nWhat is the {p}th digit he writes? (Type the digit.)', answer='((p + 10) // 2) // 10',
                 hint='How many digits do the one-digit numbers use? Then how many digits does each two-digit number use?',
                 steps=['The numbers 1 to 9 use 9 digits. After that each two-digit number uses 2 digits.', 'The {p}th digit is the first digit of a two-digit number. It is {ans}.']),
        oracle=_o_b3),
}


polish(ITEMS, VARIANTS)
