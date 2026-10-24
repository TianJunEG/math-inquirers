"""Online practice for Level 4 (Primary 4, ages 9-11) holiday lesson 9: Data Detectives (tables and line graphs).

The questions are the ones printed in the Level 4 holiday workbook, built by p4/workbook_html.js from p4/content/l9.js:
  Start here = l9.js workbook() Q1 to Q5;   Investigation = l9.js gaps.invest (Sales have doubled!);
  Think harder = l9.js qbank.stretch[0:4];   Go further = l9.js qbank.challenge[-3:]  (printed as Q5 to Q7).
Every answer is recomputed by an INDEPENDENT checker: changes between neighbouring days, row and column totals, the point where two lines meet, missing values from totals and equal steps,
the share of the graph's height that a rise takes up.  Nothing is copied from the printed key.  The build stops if a checker and the printed answer differ.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from p4lib import *      # noqa: E402,F401

META = dict(level=4, lesson=9, key='p4', title='Data Detectives', workbook_title='DATA DETECTIVES', topic='Tables and line graphs',
            strand='Tables and line graphs',
            sources=['p4/content/l9.js'],
            intro=['Type numbers. Graph questions: read the scale first, then read the points. Some questions are choices: tap one.',
                   'Drawing questions are done on paper, on squared paper: do them, then compare with the graph shown after you submit. '
                   'Some questions ask you to explain: think or write on paper, then compare.'])
S9 = 'Tables and line graphs'


def D(**k):
    return dict(strand=S9, **k)


# ---------------------------------------------------------------- the data behind the printed figures
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
FULL = {'Mon': 'Monday', 'Tue': 'Tuesday', 'Wed': 'Wednesday', 'Thu': 'Thursday', 'Fri': 'Friday', 'Sat': 'Saturday', 'Sun': 'Sunday'}
JUICE = [40, 55, 50, 75, 65, 25, 30]
PAIRS = [f'{DAYS[i]} to {DAYS[i + 1]}' for i in range(6)]
WEEKS = ['Wk 1', 'Wk 2', 'Wk 3', 'Wk 4', 'Wk 5', 'Wk 6']
ALI = [10, 20, 30, 40, 50, 60]
MEI = [30, 35, 40, 45, 50, 55]


def changes(vals):
    return [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]


def juice_fig():
    return line_graph(DAYS, [dict(v=JUICE)], 0, 80, 5, 20, 'Cups of sugarcane juice sold each day', 'Number of cups', h=262,
                      label='A line graph of cups of sugarcane juice sold each day, Monday to Sunday. The side goes from 0 to 80, with a number every 20 and a line every 5.')


def money_fig():
    return line_graph(WEEKS, [dict(v=ALI, c=TEAL, name='Ali'), dict(v=MEI, c=WARM, mark='sq', dash=True, name='Mei')], 0, 60, 5, 20, 'Money in each money box at the end of the week',
                      'Money ($)', legend=True, h=282,
                      label='A line graph of the money in Ali\'s and Mei\'s money boxes at the end of weeks 1 to 6. Ali is the solid line with round dots, Mei the dashed line with square dots. The side goes from 0 to 60 dollars, a number every 20 and a line every 5.')


LIB = [['Class', 'Week 1', 'Week 2', 'Total'], ['4A', '38', '', '85'], ['4B', '', '29', '70'], ['4C', '45', '52', ''], ['Total', '', '', '']]


def lib_fig():
    return table_fig(LIB, [78, 80, 80, 80], label='A table of library books borrowed. 4A: Week 1 38, Week 2 missing, total 85. 4B: Week 1 missing, Week 2 29, total 70. 4C: Week 1 45, Week 2 52, total missing. '
                     'The Total row is missing.')


def lib_solved():
    """The library table solved by the row and column totals (independent of the printed key)."""
    w1 = {'4A': 38, '4C': 45}
    w2 = {'4B': 29, '4C': 52}
    tot = {'4A': 85, '4B': 70}
    w2['4A'] = tot['4A'] - w1['4A']
    w1['4B'] = tot['4B'] - w2['4B']
    tot['4C'] = w1['4C'] + w2['4C']
    return w1, w2, tot


W1, W2, TOT = lib_solved()
assert sum(W1.values()) + sum(W2.values()) == sum(TOT.values())


def pages_fig(a=None):
    return table_fig([['Day', '1', '2', '3', '4', '5'], ['Pages', '', '14', '', '', '26']] if a is None else
                     [['Day', '1', '2', '3', '4', '5'], ['Pages', '', str(a[0]), '', '', str(a[1])]], [68, 52, 52, 52, 52, 52], rh=40,
                     label='A table of pages read on days 1 to 5. Day 2 is ' + str(14 if a is None else a[0]) + ' pages and day 5 is ' + str(26 if a is None else a[1]) + ' pages. The others are missing.')


def pages_seq(d2, d5):
    """Siti reads the same number more each day: find the step and the five days (searching the step, no formula)."""
    for step in range(0, 100):
        first = d2 - step
        seq = [first + k * step for k in range(5)]
        if seq[1] == d2 and seq[4] == d5:
            return step, seq
    raise ValueError


def shop_graph(vals, y0, y1, step, title):
    return line_graph(['Jan', 'Feb', 'Mar', 'Apr'], [dict(v=vals)], y0, y1, step, step, title, 'Number sold', h=214,
                      label=f'{title}. The side goes from {y0} to {y1} with a line every {step}.')


def shops_fig():
    return combine([shop_graph([20, 40, 60, 80], 0, 100, 20, 'Shop A: phone cases sold'), shop_graph([44, 48, 52, 56], 40, 60, 4, 'Shop B: phone cases sold')],
                   'Two line graphs of phone cases sold from January to April. Shop A: side from 0 to 100, a line every 20. Shop B: side from 40 to 60, a line every 4. Both lines go steadily up.')


SHOP_A = ([20, 40, 60, 80], 0, 20)
SHOP_B = ([44, 48, 52, 56], 40, 4)


# ---------------------------------------------------------------- honest and misleading scales
MAY_JUNE = [('A', 'starts at 40, each line is worth 10', 40, 110, 10, 20), ('B', 'starts at 0, each line is worth 10', 0, 100, 10, 20), ('C', 'starts at 0, each line is worth 100', 0, 1000, 100, 200)]
MJ_OPTS = {x[0]: f'{x[0]}: it {x[1]}' for x in MAY_JUNE}
FOUR = [52, 54, 56, 58]
FOUR_SC = [('A', 'starts at 50, each line is worth 1', 50, 60, 1, 5), ('B', 'starts at 0, each line is worth 10', 0, 60, 10, 20), ('C', 'starts at 0, each line is worth 100', 0, 600, 100, 200)]
F_OPTS = {x[0]: f'{x[0]}: it {x[1]}' for x in FOUR_SC}


def pick(scales, vals, biggest):
    """The scale on which the rise takes up the biggest (or smallest) share of the height of the graph."""
    sh = {x[0]: rise_share(vals[0], vals[-1], x[2], x[3]) for x in scales}
    best = (max if biggest else min)(sh.values())
    ks = [k for k, v in sh.items() if v == best]
    assert len(ks) == 1
    return ks[0]


def scales_fig(vals, scales, xl):
    figs = [line_graph(xl, [dict(v=vals)], y0, y1, st, lab, f'Graph {k}', '', w=260, h=172, label=f'Graph {k}: the scale {d}.') for k, d, y0, y1, st, lab in scales]
    return combine(figs, 'The same numbers drawn on three different scales: ' + '; '.join(f'graph {k} {d}' for k, d, *_ in scales) + '.')


def one_graph(vals, xl, y0, y1, st, lab, title='', w=270, h=210):
    return line_graph(xl, [dict(v=vals)], y0, y1, st, lab, title, w=w, h=h, label=title or 'A line graph.')


ITEMS = [
    # ================= Start here (workbook lesson 9, Q1 to Q5)
    D(id='1a-thu', tier='core', no='1(a)', label='1(a) Thu', type='number', answer=75, skill='reading a line graph', svg=juice_fig(), check=lambda: JUICE[DAYS.index('Thu')],
      q='A sugarcane juice stall is next to an office building. The line graph shows how many cups it sold each day for one week. Read the scale first! How many cups did it sell on Thursday?',
      hint='What is each small line on the side worth? Count the small lines from a number that is printed.',
      steps=['The side has a number every 20 and a line every 5, so each small line is worth 5.', 'The point for Thursday is on the line 3 small lines above 60: 60 + 15 = 75.', 'The stall sold 75 cups on Thursday.'],
      src=['A sugarcane juice stall is next to an office building. The line graph shows how many cups it sold each day for one week. Read the scale first!', 'Cups sold on Thursday?']),
    D(id='1a-wknd', tier='core', no='1(a)', label='1(a) wknd', type='number', answer=55, skill='reading a line graph', svg=juice_fig(), check=lambda: JUICE[DAYS.index('Sat')] + JUICE[DAYS.index('Sun')],
      q='How many cups did the stall sell on Saturday and Sunday together?',
      hint='Read the point for each of the two days. Then add them.',
      steps=['On Saturday the point is on the line 1 small line above 20: 25 cups.', 'On Sunday the point is 2 small lines above 20: 30 cups.', '25 + 30 = 55 cups.'],
      src=['On Saturday and Sunday together?']),
    D(id='1b-days', tier='core', no='1(b)', label='1(b) days', type='choice', options=PAIRS, answer='Wed to Thu', skill='the biggest increase', svg=juice_fig(),
      check=lambda: PAIRS[max(range(6), key=lambda i: changes(JUICE)[i])],
      q='Look at the change from each day to the next. Between which two days did sales go up the most?',
      hint='Work out the change between each pair of neighbouring days. Which pairs went up?',
      steps=['The changes are: Mon to Tue up 15, Tue to Wed down 5, Wed to Thu up 25, Thu to Fri down 10, Fri to Sat down 40, Sat to Sun up 5.', 'The biggest increase is from Wednesday to Thursday.'],
      src=['Biggest increase: from ________ to ________, up by ______ cups']),
    D(id='1b-cups', tier='core', no='1(b)', label='1(b) cups', type='number', answer=25, skill='the biggest increase', svg=juice_fig(), check=lambda: max(changes(JUICE)),
      q='What is the biggest increase in cups sold from one day to the next? Type the number of cups.',
      hint='Take away to find each change. Write up or down next to each.',
      steps=['Going up: Monday to Tuesday 15, Wednesday to Thursday 25, Saturday to Sunday 5.', 'The biggest increase is 25 cups.'],
      src=['Biggest increase: from ________ to ________, up by ______ cups']),
    D(id='1c-days', tier='core', no='1(c)', label='1(c) days', type='choice', options=PAIRS, answer='Fri to Sat', skill='the biggest decrease', svg=juice_fig(),
      check=lambda: PAIRS[min(range(6), key=lambda i: changes(JUICE)[i])],
      q='Between which two days did sales go down the most?',
      hint='Which pairs of days went down? Compare how far each one fell.',
      steps=['The days that went down are Tue to Wed (5), Thu to Fri (10) and Fri to Sat (40).', 'The biggest decrease is from Friday to Saturday.'],
      src=['Biggest decrease: from ________ to ________, down by ______ cups']),
    D(id='1c-cups', tier='core', no='1(c)', label='1(c) cups', type='number', answer=40, skill='the biggest decrease', svg=juice_fig(), check=lambda: -min(changes(JUICE)),
      q='What is the biggest decrease in cups sold from one day to the next? Type the number of cups.',
      hint='Look for a pair of days where the point falls. How far does it fall?',
      steps=['Going down: 5, 10 and 40 cups.', 'The biggest decrease is 40 cups.'],
      src=['Biggest decrease: from ________ to ________, down by ______ cups']),
    D(id='1d', tier='core', no='1(d)', label='1(d)', type='selfcheck', skill='reading steepness', svg=juice_fig(), check=lambda: PAIRS[min(range(6), key=lambda i: changes(JUICE)[i])],
      q='How can you spot the biggest decrease on the graph without working out every change? Why might sales drop like that?',
      hint='Look at the lines between the points. Which one slopes most?',
      steps=['The biggest decrease is the steepest line going down: you can see it without working anything out.', 'A reason such as: the stall is next to an office building, and the office workers do not come to work on Saturday and Sunday.', 'Any sensible reason is good.'],
      src=['How can you see (c) on the graph without working out every change? Why might sales drop on those days?']),

    D(id='2-missing', tier='core', no='2', label='2 missing', type='fields', frame='4A Week 2: {f1}    4B Week 1: {f2}    4C Total: {f3}', answer=[47, 41, 97], skill='missing values in a table', svg=lib_fig(),
      check=lambda: [W2['4A'], W1['4B'], TOT['4C']],
      q='The table shows how many books three classes borrowed from the library. Fill in the three missing numbers in the table.',
      hint='Each row adds up across: Week 1 and Week 2 make the Total.',
      steps=['4A: the Total is 85 and Week 1 is 38, so Week 2 is 85 − 38 = 47.', '4B: the Total is 70 and Week 2 is 29, so Week 1 is 70 − 29 = 41.', '4C: Week 1 and Week 2 make 45 + 52 = 97.'],
      src=['The table shows how many books three classes borrowed from the library. Fill in the missing numbers.']),
    D(id='2-totals', tier='core', no='2', label='2 totals', type='fields', frame='Week 1: {f1}    Week 2: {f2}    altogether: {f3}', answer=[124, 128, 252], skill='column totals and a check', svg=lib_fig(),
      check=lambda: [sum(W1.values()), sum(W2.values()), sum(W1.values()) + sum(W2.values())],
      q='Now fill in the Total row of the table: the total for Week 1, the total for Week 2, and the grand total.',
      hint='Add down each column first. Is the grand total the same when you add along the Total column?',
      steps=['Week 1 column: 38 + 41 + 45 = 124.', 'Week 2 column: 47 + 29 + 52 = 128.', 'Altogether: 124 + 128 = 252. Check by adding the Total column: 85 + 70 + 97 = 252.'],
      src=['Fill in the missing numbers.']),
    D(id='2a', tier='core', no='2(a)', label='2(a)', type='choice', options=['4A', '4B', '4C'], answer='4B', skill='comparing table entries', svg=lib_fig(),
      check=lambda: next(c for c in ('4A', '4B', '4C') if W1[c] > W2[c]),
      q='Which class borrowed more books in Week 1 than in Week 2?',
      hint='Fill in the missing numbers first. Then compare the Week 1 and Week 2 numbers of each class.',
      steps=['4A: Week 1 is 38 and Week 2 is 47, so fewer.', '4B: Week 1 is 41 and Week 2 is 29, so more.', '4C: Week 1 is 45 and Week 2 is 52, so fewer.', 'Only 4B borrowed more in Week 1.'],
      src=['Which class borrowed more in Week 1 than in Week 2?']),
    D(id='2b', tier='core', no='2(b)', label='2(b)', type='number', answer=146, skill='totals from a table', svg=lib_fig(), check=lambda: sum(W2.values()) + 3 * 6,
      q='In Week 3, each class borrowed 6 more books than in Week 2. How many books did the three classes borrow in Week 3?',
      hint='Find the Week 2 total. How many more books is that for three classes?',
      steps=['The Week 2 total is 128.', 'Each of the 3 classes borrowed 6 more, which is 3 × 6 = 18 more.', '128 + 18 = 146 books.'],
      src=['In Week 3, each class borrowed 6 more books than in Week 2. Week 3 total?']),

    D(id='3-ali', tier='core', no='3', label='3 Ali dots', type='set', ordered=True, answer=ALI, skill='reading a line graph', svg=money_fig(), check=lambda: list(ALI),
      q='The graph shows how much money Ali and Mei had in their money boxes at the end of each week. Read each dot for Ali, weeks 1 to 6. Type the six amounts in order, with commas.',
      hint='Read the scale first. What is each small line worth?',
      steps=['Each small line is worth $5, with a number every $20.', 'Ali has $10, $20, $30, $40, $50 and $60 in weeks 1 to 6.'],
      src=['The graph shows how much money Ali and Mei had in their money boxes at the end of each week.', 'read each dot. Ali, weeks 1 to 6']),
    D(id='3-mei', tier='core', no='3', label='3 Mei dots', type='set', ordered=True, answer=MEI, skill='reading a line graph', svg=money_fig(), check=lambda: list(MEI),
      q='Now read each dot for Mei, weeks 1 to 6. Type the six amounts in order, with commas.',
      hint='Mei is the dashed line with square dots. Count the small lines from a number that is printed.',
      steps=['Mei has $30, $35, $40, $45, $50 and $55 in weeks 1 to 6.'],
      src=['Mei: $___ $___ $___ $___ $___ $___']),
    D(id='3a-mei', tier='core', no='3(a)', label='3(a) Mei', type='number', answer=40, skill='reading a line graph', svg=money_fig(), check=lambda: MEI[2],
      q='How much money did Mei have in Week 3?',
      hint='Find Week 3 along the bottom. Go straight up to the dashed line.',
      steps=['In Week 3 the square dot is on the line 4 small lines above 20: $40.'],
      src=['Mei’s money in Week 3?']),
    D(id='3a-ali', tier='core', no='3(a)', label='3(a) Ali', type='number', answer=10, skill='equal steps on a graph', svg=money_fig(), check=lambda: ALI[1] - ALI[0],
      q='How much money does Ali save each week?',
      hint='How much does the solid line go up from one week to the next?',
      steps=['Ali has $10 more every week: $10, $20, $30 and so on.', 'He saves $10 each week.'],
      src=['Ali saves each week?']),
    D(id='3b-same', tier='core', no='3(b)', label='3(b) same', type='number', answer=5, skill='where two lines meet', svg=money_fig(), check=lambda: next(i + 1 for i in range(6) if ALI[i] == MEI[i]),
      q='In which week do Ali and Mei have the same amount of money? Type the week number.',
      hint='Where do the two lines meet?',
      steps=['The two lines meet at Week 5, where both have $50.'],
      src=['Same amount in Week ____']),
    D(id='3b-more', tier='core', no='3(b)', label='3(b) more', type='number', answer=6, skill='where two lines cross', svg=money_fig(), check=lambda: next(i + 1 for i in range(6) if ALI[i] > MEI[i]),
      q='In which week does Ali first have more money than Mei? Type the week number.',
      hint='Compare the two dots in each week. Look for the first week the solid line is higher.',
      steps=['In Week 6 Ali has $60 and Mei has $55.', 'Before that, Ali had less than Mei or the same, so Week 6 is the first week Ali has more.'],
      src=['Ali first has more in Week ____']),
    D(id='3c', tier='core', no='3(c)', label='3(c)', type='number', answer=15, skill='continuing a pattern', svg=money_fig(),
      check=lambda: (lambda a, m: a - m)(ALI[-1] + 2 * 10, MEI[-1] + 2 * 5),
      q='They keep saving the same way. In Week 8, how much more money does Ali have than Mei?',
      hint='How much does each of them add every week? Carry on both lines past Week 6.',
      steps=['Ali adds $10 a week, so Week 7 is $70 and Week 8 is $80.', 'Mei adds $5 a week, so Week 7 is $60 and Week 8 is $65.', '$80 − $65 = $15 more.'],
      src=['They keep saving the same way. In Week 8, Ali has $______ more than Mei.']),

    D(id='4-table', tier='core', no='4', label='4 table', type='fields', frame='Day 1: {f1}    Day 3: {f2}    Day 4: {f3}', answer=[10, 18, 22], skill='equal steps in a table', svg=pages_fig(),
      check=lambda: (lambda s: [s[1][0], s[1][2], s[1][3]])(pages_seq(14, 26)),
      q='Siti reads more pages each day, always the same number more. Fill in the missing days in the table.',
      hint='From Day 2 to Day 5 there are 3 steps. How many pages does she gain in all?',
      steps=['From Day 2 to Day 5 she reads 26 − 14 = 12 more pages, in 3 equal steps.', 'Each step is 4 pages. So Day 3 is 18, Day 4 is 22, and Day 1 is 14 − 4 = 10.'],
      src=['Siti reads more pages each day, always the same number more. Fill in the table.']),
    D(id='4a-step', tier='core', no='4(a)', label='4(a) more', type='number', answer=4, skill='equal steps in a table', svg=pages_fig(), check=lambda: pages_seq(14, 26)[0],
      q='How many more pages does Siti read each day than the day before?',
      hint='How many equal steps are there between Day 2 and Day 5?',
      steps=['She reads 26 − 14 = 12 more pages over 3 days.', '12 ÷ 3 = 4 more pages each day.'],
      src=['How many more each day?']),
    D(id='4a-total', tier='core', no='4(a)', label='4(a) total', type='number', answer=90, skill='totals from a table', svg=pages_fig(), check=lambda: sum(pages_seq(14, 26)[1]),
      q='How many pages does Siti read in the 5 days altogether?',
      hint='Find the pages for every day first. Then add.',
      steps=['The days are 10, 14, 18, 22 and 26 pages.', '10 + 14 + 18 + 22 + 26 = 90 pages.'],
      src=['Pages in the 5 days?']),

    D(id='5-scales', tier='core', no='5', label='5 scales', type='fields', frame='Shop A starts at {f1}, each line is worth {f2}.    Shop B starts at {f3}, each line is worth {f4}.', answer=[0, 20, 40, 4],
      skill='reading the scale of a graph', svg=shops_fig(), check=lambda: [0, SHOP_A[2], SHOP_B[1], SHOP_B[2]],
      q='Two shops drew line graphs of the phone cases they sold. Ravi says, "Both shops\' sales went up by the same amount, because the lines look the same." Read the scale of each graph.',
      hint='Look at the lowest number on the side, then at the step from one number to the next.',
      steps=['Shop A: the side starts at 0 and goes up in 20s.', 'Shop B: the side starts at 40 and goes up in 4s.'],
      src=['Two shops drew line graphs of the phone cases they sold. Ravi says, “Both shops’ sales went up by the same amount, because the lines look the same.”', 'read the scale of each graph']),
    D(id='5a', tier='core', no='5(a)', label='5(a)', type='fields', frame='Shop A went up by {f1}.    Shop B went up by {f2}.', answer=[60, 12], skill='reading two graphs', svg=shops_fig(),
      check=lambda: [SHOP_A[0][-1] - SHOP_A[0][0], SHOP_B[0][-1] - SHOP_B[0][0]],
      q='From January to April, by how many phone cases did the sales of each shop go up?',
      hint='Read the January point and the April point on each graph, using that graph\'s own scale.',
      steps=['Shop A: January 20 and April 80, so up by 60.', 'Shop B: January 44 and April 56, so up by 12.'],
      src=['January to April: Shop A went up by ______.  Shop B went up by ______.']),
    D(id='5b', tier='core', no='5(b)', label='5(b)', type='choice', options=['Yes', 'No'], answer='No', skill='misleading graphs', svg=shops_fig(),
      check=lambda: 'Yes' if SHOP_A[0][-1] - SHOP_A[0][0] == SHOP_B[0][-1] - SHOP_B[0][0] else 'No',
      q='Ravi says, "Both shops\' sales went up by the same amount, because the lines look the same." Is Ravi right?',
      hint='Read both graphs carefully: how much did each shop\'s sales go up?',
      steps=['Shop A went up by 60 and Shop B went up by 12, so the sales did not go up by the same amount.', 'Ravi is not right.'],
      src=['Is Ravi right? Explain why the two graphs look the same.']),
    D(id='5b-why', tier='core', no='5(b)', label='5(b) why', type='selfcheck', skill='misleading graphs', svg=shops_fig(), check=lambda: (SHOP_A[2], SHOP_B[2]),
      q='Explain why the two graphs look the same.',
      hint='Look at the numbers up the side of each graph. How are they different?',
      steps=['The scales are different. Shop A\'s starts at 0 and each line is worth 20. Shop B\'s starts at 40 and each line is worth 4.',
             'On Shop B\'s graph each line is worth much less, so a small rise takes up as much of the graph as Shop A\'s big rise.', 'Shop A\'s sales went up by 48 more than Shop B\'s.'],
      src=['Is Ravi right? Explain why the two graphs look the same.']),

    # ================= Investigation: Sales have doubled!
    D(id='Ieasy', tier='invest', no='Investigation (easy step)', label='Inv easy', type='selfcheck', paper=True, skill='drawing a line graph', svg=None,
      check=lambda: (50, 100), sol_fig=lambda f: one_graph([50, 100], ['May', 'June'], 0, 100, 10, 10, 'Phone cases sold: scale 0 to 100 in 10s'),
      q='A shop sold 50 phone cases in May and 100 in June. A newspaper says: "Sales have doubled!" On squared paper, write 0, 10, 20 and so on up the side. Plot May and June and join the points.',
      hint='Each line on the side is worth 10.',
      steps=['Go up in 10s from 0 to 100. May is at 50, the 5th line, and June is at 100, the 10th line.', 'Join the two points with a straight line.'],
      src=['A shop sold 50 phone cases in May and 100 in June. A newspaper says: "Sales have doubled!"', 'On the Graph grid, write 0, 10, 20 ... up the side. Plot the points (May, 50) and (June, 100) and join them.']),
    D(id='Ilines', tier='invest', no='Investigation (a)', label='Inv (a)', type='fields', frame='May is {f1} lines up.    June is {f2} lines up.', answer=[5, 10], skill='reading a scale', svg=None,
      check=lambda: [50 // 10, 100 // 10],
      q='Draw the line graph with the side going up in 10s from 0 to 100. How many lines up from 0 is the point for May (50), and how many for June (100)?',
      hint='Count up in 10s: 10 is 1 line up.',
      steps=['50 is 5 lines up, and 100 is 10 lines up.', 'The line goes up through 5 lines, a fair picture of doubling.'],
      src=['On the first Graph grid, draw a line graph of May and June. Go up in 10s from 0 to 100. Is the line steep or gentle?']),
    D(id='Ib-huge', tier='invest', no='Investigation (b)', label='Inv (b) huge', type='choice', options=list(MJ_OPTS.values()), answer=MJ_OPTS['A'], skill='scales can mislead',
      check=lambda: MJ_OPTS[pick(MAY_JUNE, [50, 100], True)], sol_fig=lambda f: scales_fig([50, 100], MAY_JUNE, ['May', 'June']),
      q='The same two numbers, 50 in May and 100 in June, can be drawn on different scales. Which scale makes the rise look HUGE?',
      hint='Think about how much of the graph\'s height the rise fills.',
      steps=['A scale from 40 to 110 has a short side, so the rise from 50 to 100 fills most of the graph: it looks huge.', 'On the scale from 0 to 100 it fills half the graph, and on the scale from 0 to 1000 only a small part.', 'The numbers are the same on all three. Only the picture changes.'],
      src=['Now draw the same two numbers on the second grid so the rise looks HUGE. Choose a different scale and write it.']),
    D(id='Ib-flat', tier='invest', no='Investigation (b)', label='Inv (b) flat', type='choice', options=list(MJ_OPTS.values()), answer=MJ_OPTS['C'], skill='scales can mislead',
      check=lambda: MJ_OPTS[pick(MAY_JUNE, [50, 100], False)], sol_fig=lambda f: scales_fig([50, 100], MAY_JUNE, ['May', 'June']),
      q='Which of these scales makes the rise from 50 to 100 look almost flat?',
      hint='Think about how much of the graph\'s height the rise fills.',
      steps=['A scale from 0 to 1000 has a tall side, so the rise from 50 to 100 fills only a small part of the graph: it looks almost flat.'],
      src=['Then say how you would make the rise look almost flat.']),
    D(id='Ib-own', tier='invest', no='Investigation (b)', label='Inv (b) draw', type='selfcheck', paper=True, skill='drawing a graph with a chosen scale', svg=None,
      check=lambda: MAY_JUNE[0], sol_fig=lambda f: one_graph([50, 100], ['May', 'June'], 40, 110, 10, 20, 'Model: starts at 40, each line is worth 10'),
      q='On a second grid, draw May and June again. Choose a scale that makes the rise look HUGE, and write your scale next to your graph.',
      hint='Start the side near 50 and make each line worth only a little.',
      steps=['Model: start at 40 and make each line worth 10. May (50) is 1 line up and June (100) is 6 lines up.', 'Other scales that start near 50 and use small steps also work.'],
      src=['Choose a different scale and write it.']),
    D(id='Ic', tier='invest', no='Investigation (c)', label='Inv (c)', type='selfcheck', skill='honest graphs', check=lambda: MAY_JUNE[1],
      q='Which of your graphs is the most honest? What would you ask the newspaper to add to its graph?',
      hint='What would a reader need to know to be sure the picture is fair?',
      steps=['A graph that starts at 0, has equal steps, and says what each line is worth is the fairest.', 'Ask the newspaper to show where the side starts and what each line is worth. The headline is true because the numbers say so, but the picture can be made to look bigger or smaller.',
             'The numbers did not change, only the drawing did.'],
      src=['Which graph is the most honest? What would you ask the newspaper to add to its graph?']),

    # ================= Think harder (qbank.stretch[0:4])
    D(id='T1-girls', tier='stretch', no='Think harder 1', label='T1 girls', type='number', answer=34, skill='finding two parts from a total and a difference',
      check=lambda: next(g for g in range(1, 63) if g + (g - 5) == 63),
      q='Class 4B has 63 pupils, with 5 more girls than boys. How many girls are in Class 4B?',
      hint='Draw a bar for the boys and a longer bar for the girls. The longer bar has 5 extra.',
      steps=['Take away the 5 extra girls: 63 − 5 = 58 pupils share equally. 58 ÷ 2 = 29 boys.', 'Girls: 29 + 5 = 34. Check: 29 + 34 = 63.'],
      src=['Class 4B has 63 pupils, with 5 more girls than boys.']),
    D(id='T1-which', tier='stretch', no='Think harder 1', label='T1 which', type='choice', options=['Class 4A', 'Class 4B', 'Neither: the same'], answer='Neither: the same', skill='comparing two classes',
      check=lambda: (lambda a, b: 'Class 4A' if a > b else 'Class 4B' if b > a else 'Neither: the same')(28 + 6, next(g for g in range(1, 63) if g + (g - 5) == 63)),
      q='Class 4A has 28 boys and 6 more girls than boys. Class 4B has 63 pupils, with 5 more girls than boys. Which class has more girls?',
      hint='Find the number of girls in each class. Then compare.',
      steps=['Class 4A: 28 + 6 = 34 girls.', 'Class 4B: 63 − 5 = 58, 58 ÷ 2 = 29 boys, and 29 + 5 = 34 girls.', 'Both classes have 34 girls.'],
      src=['Class 4A has 28 boys and 6 more girls than boys. Class 4B has 63 pupils, with 5 more girls than boys. Which class has more girls?']),
    D(id='T2-more', tier='stretch', no='Think harder 2', label='T2 more', type='number', answer=100, skill='reading a scale that does not start at 0',
      check=lambda: (100 + 7 * 25) - (100 + 3 * 25),
      q='A graph\'s scale starts at 100 and each line is worth 25. Ali\'s point is 3 lines above the start and Mei\'s point is 7 lines above the start. How much more is Mei\'s number than Ali\'s?',
      hint='Work out each number. The start is 100, not 0.',
      steps=['Ali: 100 + 3 × 25 = 175.', 'Mei: 100 + 7 × 25 = 275.', '275 − 175 = 100 more.'],
      src=['A graph\'s scale starts at 100 and each line is worth 25. Ali\'s point is 3 lines above the start and Mei\'s point is 7 lines above the start. How much more is Mei\'s number than Ali\'s?']),
    D(id='T2-double', tier='stretch', no='Think harder 2', label='T2 double', type='choice', options=['Yes', 'No'], answer='No', skill='reading a scale that does not start at 0',
      check=lambda: 'Yes' if (100 + 7 * 25) > 2 * (100 + 3 * 25) else 'No',
      q='A graph\'s scale starts at 100 and each line is worth 25. Ali\'s point is 3 lines above the start and Mei\'s point is 7 lines above the start. Mei says hers is more than double Ali\'s. Is she right?',
      hint='Work out Ali\'s number and Mei\'s number first. Then double Ali\'s.',
      steps=['Ali has 175 and Mei has 275. Double Ali\'s is 350, and 275 is less than 350.', 'Mei is not right.'],
      src=['Mei says hers is more than double Ali\'s. Is she right?']),
    D(id='T2-why', tier='stretch', no='Think harder 2', label='T2 why', type='selfcheck', skill='reading a scale that does not start at 0', check=lambda: (175, 275),
      q='Explain how you know whether Mei is right.',
      hint='Where does the scale start? Do the lines count from 0?',
      steps=['Her point is more than twice as many lines up (7 against 3), but the scale starts at 100, not 0.', 'The real numbers are 175 and 275. Double 175 is 350, so 275 is not more than double.'],
      src=['Mei says hers is more than double Ali\'s.']),
    D(id='T3-fri', tier='stretch', no='Think harder 3', label='T3 Fri', type='number', answer=40, skill='reading a pattern on a line graph',
      check=lambda: (lambda d: d[4])((lambda s, st: [s, s + st, s + 2 * st, s + st, s])(40, 15)),
      q='A stall\'s line graph starts on Monday with 40 cups sold. The line goes up by 15 cups each day until Wednesday, then down by 15 cups each day. How many cups were sold on Friday?',
      hint='Write the number for each day, one under the other. Go up first, then down.',
      steps=['Monday 40, Tuesday 55, Wednesday 70.', 'Then down: Thursday 55, Friday 40.', 'On Friday the stall sold 40 cups.'],
      src=['A stall\'s line graph starts on Monday with 40 cups sold. The line goes up by 15 cups each day until Wednesday, then down by 15 cups each day.']),
    D(id='T3-same', tier='stretch', no='Think harder 3', label='T3 same', type='choice', options=['Monday', 'Tuesday', 'Wednesday', 'Friday'], answer='Tuesday', skill='reading a pattern on a line graph',
      check=lambda: (lambda d: next(n for n, v in zip(['Monday', 'Tuesday', 'Wednesday', 'Friday'], [d[0], d[1], d[2], d[4]]) if v == d[3]))((lambda s, st: [s, s + st, s + 2 * st, s + st, s])(40, 15)),
      q='A stall sold 40 cups on Monday. The line goes up by 15 cups each day until Wednesday, then down by 15 cups each day. Which day sold the same number of cups as Thursday?',
      hint='Write the number for each day. Which other day has the same number as Thursday?',
      steps=['Monday 40, Tuesday 55, Wednesday 70, Thursday 55, Friday 40.', 'Thursday (55) matches Tuesday (55).'],
      src=['Which day sold the same as Thursday?']),
    D(id='T4-year', tier='stretch', no='Think harder 4', label='T4 year', type='choice', options=['Age 7 to 8', 'Age 8 to 9', 'Age 9 to 10'], answer='Age 7 to 8', skill='the biggest change',
      check=lambda: (lambda h: ['Age 7 to 8', 'Age 8 to 9', 'Age 9 to 10'][max(range(3), key=lambda i: h[i + 1] - h[i])])([120, 127, 131, 137]),
      q='Ali\'s height: age 7, 120 cm; age 8, 127 cm; age 9, 131 cm; age 10, 137 cm. In which year did he grow the most?',
      hint='Work out how much he grew in each year.',
      steps=['Age 7 to 8: 7 cm. Age 8 to 9: 4 cm. Age 9 to 10: 6 cm.', 'He grew the most from age 7 to age 8.'],
      src=['Ali’s height: age 7, 120 cm; age 8, 127 cm; age 9, 131 cm; age 10, 137 cm. In which year did he grow the most?']),
    D(id='T4-total', tier='stretch', no='Think harder 4', label='T4 total', type='number', answer=17, skill='total change', check=lambda: (lambda h: h[-1] - h[0])([120, 127, 131, 137]),
      q='Ali\'s height: age 7, 120 cm; age 8, 127 cm; age 9, 131 cm; age 10, 137 cm. How much did he grow altogether from age 7 to age 10?',
      hint='You can add the growth of each year, or compare the first height with the last.',
      steps=['137 − 120 = 17 cm.', 'Check by adding each year: 7 + 4 + 6 = 17 cm.'],
      src=['How much did he grow altogether from age 7 to age 10?']),

    # ================= Go further (qbank.challenge[-3:], printed Q5 to Q7)
    D(id='G5', tier='challenge', no='Go further 5', label='G5', type='fields', frame='Team A: {f1}    Team B: {f2}    Team C: {f3}', answer=[34, 17, 27], skill='finding parts from a total',
      check=lambda: next([2 * b, b, b + 10] for b in range(1, 100) if 2 * b + b + (b + 10) + 22 == 100),
      q='Four teams scored 100 points altogether. Team A scored twice as many as Team B. Team C scored 10 more than Team B. Team D scored 22. How many points did Teams A, B and C score?',
      hint='Take away Team D\'s points first. Draw a bar for Team B and show the others using it.',
      steps=['A, B and C scored 100 − 22 = 78 together.', 'Team B has 1 part, Team A has 2 parts, and Team C has 1 part and 10 more. That is 4 equal parts and 10 more: 78 − 10 = 68, and 68 ÷ 4 = 17.',
             'B = 17, A = 34, C = 27. Check: 34 + 17 + 27 + 22 = 100.'],
      src=['Four teams scored 100 points altogether. Team A scored twice as many as Team B. Team C scored 10 more than Team B. Team D scored 22. How many points did each team score?']),
    D(id='G6-hours', tier='challenge', no='Go further 6', label='G6 hours', type='number', answer=4, skill='where two lines cross',
      check=lambda: next(t for t in range(0, 40) if 80 - 6 * t == 20 + 9 * t),
      q='Tank A has 80 litres of water and loses 6 litres every hour. Tank B has 20 litres and gains 9 litres every hour. On a line graph the two lines cross. After how many hours do the tanks hold the same amount?',
      hint='Make a table of the two amounts, hour by hour. What happens to the gap between them?',
      steps=['At the start Tank A has 60 litres more than Tank B.', 'Each hour the gap closes by 6 + 9 = 15 litres.', '60 ÷ 15 = 4 hours.'],
      src=['Tank A has 80 litres of water and loses 6 litres every hour. Tank B has 20 litres and gains 9 litres every hour.']),
    D(id='G6-litres', tier='challenge', no='Go further 6', label='G6 litres', type='number', answer=56, skill='where two lines cross',
      check=lambda: next(80 - 6 * t for t in range(0, 40) if 80 - 6 * t == 20 + 9 * t),
      q='Tank A has 80 litres of water and loses 6 litres every hour. Tank B has 20 litres and gains 9 litres every hour. The lines cross when the tanks hold the same amount. How much is in each tank then?',
      hint='Make a table of the two amounts, hour by hour, until they are equal.',
      steps=['The tanks hold the same amount after 4 hours.', 'Tank A: 80 − 4 × 6 = 56 litres. Tank B: 20 + 4 × 9 = 56 litres.'],
      src=['How much is in each?']),
    D(id='G7-huge', tier='challenge', no='Go further 7', label='G7 huge', type='choice', options=list(F_OPTS.values()), answer=F_OPTS['A'], skill='scales can mislead',
      check=lambda: F_OPTS[pick(FOUR_SC, FOUR, True)], sol_fig=lambda f: scales_fig(FOUR, FOUR_SC, ['Wk 1', 'Wk 2', 'Wk 3', 'Wk 4']),
      q='Four numbers: 52, 54, 56, 58. They go up by 2 each time. Which scale makes a line graph of these numbers look like a huge increase?',
      hint='Think about how much of the graph\'s height the rise fills.',
      steps=['A scale from 50 to 60 has a short side, so the rise from 52 to 58 fills most of it: a huge increase.', 'On the other two scales the same rise is small.'],
      src=['Four numbers: 52, 54, 56, 58. Choose where the scale starts and how much each line is worth, so that a line graph of these numbers looks (a) like a huge increase']),
    D(id='G7-flat', tier='challenge', no='Go further 7', label='G7 flat', type='choice', options=list(F_OPTS.values()), answer=F_OPTS['C'], skill='scales can mislead',
      check=lambda: F_OPTS[pick(FOUR_SC, FOUR, False)], sol_fig=lambda f: scales_fig(FOUR, FOUR_SC, ['Wk 1', 'Wk 2', 'Wk 3', 'Wk 4']),
      q='Which of these scales makes a line graph of 52, 54, 56, 58 look like hardly any increase?',
      hint='Think about how much of the graph\'s height the rise fills.',
      steps=['A scale from 0 to 600 has a very tall side, so the rise from 52 to 58 fills almost none of it: the line looks nearly flat.'],
      src=['(b) like hardly any increase']),
    D(id='G7-own', tier='challenge', no='Go further 7', label='G7 draw', type='selfcheck', paper=True, skill='drawing graphs on different scales', check=lambda: (FOUR_SC[0], FOUR_SC[2]),
      sol_fig=lambda f: combine([one_graph(FOUR, ['Wk 1', 'Wk 2', 'Wk 3', 'Wk 4'], 50, 60, 1, 5, 'Huge', w=260, h=172),
                                 one_graph(FOUR, ['Wk 1', 'Wk 2', 'Wk 3', 'Wk 4'], 0, 600, 100, 200, 'Flat', w=260, h=172)], 'Two graphs of 52, 54, 56 and 58, one that looks like a huge increase and one that looks almost flat.'),
      q='On paper, draw a line graph of 52, 54, 56 and 58 twice: once so it looks like a huge increase and once so it looks like hardly any increase. Write both scales and a sentence a shop owner might say with each graph.',
      hint='A short side makes the rise look big, and a tall side makes it look small.',
      steps=['Huge: start at 50, with each line worth 1. A sentence: "Look how fast our sales are growing!"', 'Flat: start at 0, with each line worth 100. A sentence: "Our sales are steady."', 'Both graphs show the same numbers.'],
      src=['Write both scales and a sentence a shop owner might say with each graph.']),
    D(id='G7-fair', tier='challenge', no='Go further 7', label='G7 fair', type='selfcheck', skill='honest graphs', check=lambda: FOUR_SC[1],
      q='Which graph is fair? Why?',
      hint='What would help a reader see the real change?',
      steps=['A fair graph starts at 0, or says clearly that it does not, so the viewer can see the real change of 6.', 'Both graphs show the same numbers: only the scale makes them look different.'],
      src=['Which graph is fair? Why?']),
]

finish(ITEMS)


# ---------------------------------------------------------------- variants (every combination is run against an oracle that does not use the template's formula)
def _lib_sum_week2():
    return sum(W2.values())


def _grow(h, a, b, c):
    return [h, h + a, h + a + b, h + a + b + c]


def _tanks(A0, ra, B0, rb):
    t = 0
    while A0 - ra * t > B0 + rb * t:
        t += 1
    assert A0 - ra * t == B0 + rb * t
    return t, A0 - ra * t


def _teams(total, d):
    for b in range(1, 200):
        if 2 * b + b + (b + 10) + d == total:
            return dict(f1=2 * b, f2=b, f3=b + 10)
    raise ValueError


def _wk(w):
    a = ALI[-1]; m = MEI[-1]
    for _ in range(w - 6):
        a += 10; m += 5
    return a, m


def _days(s, st):
    return [s, s + st, s + 2 * st, s + st, s]


VARIANTS = {
    '2b': dict(
        base=dict(k=6),
        tpl=dict(vars=dict(k=[4, 5, 6, 7, 8, 10]),
                 q='In Week 3, each class borrowed {k} more books than in Week 2. How many books did the three classes borrow in Week 3?', answer='128+3*k',
                 hint='Find the Week 2 total. How many more books is that for three classes?',
                 steps=['The Week 2 total is 128.', 'Each of the 3 classes borrowed {k} more, which is 3 × {k} more.', 'The three classes borrowed {ans} books in Week 3.']),
        fig=lambda e: lib_fig(),
        oracle=lambda e: _lib_sum_week2() + 3 * e['k']),
    '3c': dict(
        base=dict(w=8),
        tpl=dict(vars=dict(w=[7, 8, 9, 10, 11]),
                 q='They keep saving the same way. In Week {w}, how much more money does Ali have than Mei?', answer='5*w-25',
                 hint='How much does each of them add every week? Carry on both lines past Week 6.',
                 steps=['Ali adds $10 a week and Mei adds $5 a week.', 'In Week {w} Ali has $10 × {w} and Mei has $25 + $5 × {w}.', 'Ali has ${ans} more than Mei.']),
        fig=lambda e: money_fig(),
        oracle=lambda e: (lambda a, m: a - m)(*_wk(e['w']))),
    '4a-step': dict(
        base=dict(s=10, d=4),
        tpl=dict(vars=dict(s=[6, 8, 10, 12], d=[3, 4, 5, 6]), derive=dict(a='s+d', b='s+4*d'),
                 q='Siti reads more pages each day, always the same number more. On Day 2 she reads {a} pages and on Day 5 she reads {b} pages. How many more pages does she read each day than the day before?',
                 answer='d', hint='How many equal steps are there between Day 2 and Day 5?',
                 steps=['From Day 2 to Day 5 she reads {b} − {a} more pages, in 3 equal steps.', 'Each step is {ans} pages.']),
        fig=lambda e: pages_fig((e['s'] + e['d'], e['s'] + 4 * e['d'])),
        oracle=lambda e: pages_seq(e['s'] + e['d'], e['s'] + 4 * e['d'])[0]),
    '4a-total': dict(
        base=dict(s=10, d=4),
        tpl=dict(vars=dict(s=[6, 8, 10, 12], d=[3, 4, 5, 6]), derive=dict(a='s+d', b='s+4*d'),
                 q='Siti reads more pages each day, always the same number more. On Day 2 she reads {a} pages and on Day 5 she reads {b} pages. How many pages does she read in the 5 days altogether?',
                 answer='5*s+10*d', hint='Find the pages for every day first. Then add.',
                 steps=['The same number more each day: first find the step, then every day.', 'Adding the five days gives {ans} pages.']),
        fig=lambda e: pages_fig((e['s'] + e['d'], e['s'] + 4 * e['d'])),
        oracle=lambda e: sum(pages_seq(e['s'] + e['d'], e['s'] + 4 * e['d'])[1])),
    'T1-girls': dict(
        base=dict(P=63, d=5),
        tpl=dict(vars=dict(P=[45, 51, 57, 63, 69, 75], d=[3, 5, 7]),
                 q='Class 4B has {P} pupils, with {d} more girls than boys. How many girls are in Class 4B?', answer='(P+d)//2',
                 hint='Draw a bar for the boys and a longer bar for the girls. The longer bar has {d} extra.',
                 steps=['Take away the {d} extra girls, then share the rest equally between boys and girls.', 'The girls are the boys and {d} more. There are {ans} girls.']),
        oracle=lambda e: next(g for g in range(1, e['P']) if g + (g - e['d']) == e['P'])),
    'T2-more': dict(
        base=dict(s=100, st=25, la=3, lm=7),
        tpl=dict(vars=dict(s=[100, 200, 300], st=[20, 25, 50], la=[2, 3, 4], lm=[6, 7, 8]),
                 q='A graph\'s scale starts at {s} and each line is worth {st}. Ali\'s point is {la} lines above the start and Mei\'s point is {lm} lines above the start. How much more is Mei\'s number than Ali\'s?',
                 answer='(lm-la)*st', hint='Work out each number. The start is {s}, not 0.',
                 steps=['Ali: {s} + {la} × {st}. Mei: {s} + {lm} × {st}.', 'Mei has {ans} more than Ali.']),
        oracle=lambda e: (e['s'] + e['lm'] * e['st']) - (e['s'] + e['la'] * e['st'])),
    'T3-fri': dict(
        base=dict(s=40, st=15),
        tpl=dict(vars=dict(s=[30, 40, 50, 60], st=[10, 15, 20, 25]), derive=dict(t='s+st', w='s+2*st'),
                 q='A stall\'s line graph starts on Monday with {s} cups sold. The line goes up by {st} cups each day until Wednesday, then down by {st} cups each day. How many cups were sold on Friday?',
                 answer='s', hint='Write the number for each day, one under the other. Go up first, then down.',
                 steps=['Monday {s}, Tuesday {t}, Wednesday {w}.', 'Then down: Thursday {t}, Friday {ans}.', 'On Friday the stall sold {ans} cups.']),
        oracle=lambda e: _days(e['s'], e['st'])[4]),
    'T4-total': dict(
        base=dict(h=120, a=7, b=4, c=6),
        tpl=dict(vars=dict(h=[110, 120, 125], a=[6, 7, 8], b=[3, 4, 5], c=[5, 6, 7]), derive=dict(h2='h+a', h3='h+a+b', h4='h+a+b+c'),
                 q='Ali\'s height: age 7, {h} cm; age 8, {h2} cm; age 9, {h3} cm; age 10, {h4} cm. How much did he grow altogether from age 7 to age 10?', answer='a+b+c',
                 hint='You can add the growth of each year, or compare the first height with the last.',
                 steps=['{h4} − {h} = {ans} cm.', 'Check by adding each year: {a} + {b} + {c} = {ans} cm.']),
        oracle=lambda e: (lambda hs: hs[-1] - hs[0])(_grow(e['h'], e['a'], e['b'], e['c']))),
    'G5': dict(
        base=dict(x=17, D=22),
        tpl=dict(vars=dict(x=[12, 15, 17, 20, 25], D=[14, 18, 22, 26]), derive=dict(T='4*x+10+D'),
                 q='Four teams scored {T} points altogether. Team A scored twice as many as Team B. Team C scored 10 more than Team B. Team D scored {D}. How many points did Teams A, B and C score?',
                 frame='Team A: {f1}    Team B: {f2}    Team C: {f3}', answers=dict(f1='2*x', f2='x', f3='x+10'),
                 hint='Take away Team D\'s points first. Draw a bar for Team B and show the others using it.',
                 steps=['A, B and C scored {T} − {D} together.', 'That is 4 equal parts of Team B\'s score and 10 more. So the scores are {ans}.']),
        oracle=lambda e: _teams(4 * e['x'] + 10 + e['D'], e['D'])),
    'G6-hours': dict(
        base=dict(B0=20, t=4, ra=6, rb=9),
        tpl=dict(vars=dict(B0=[10, 20, 30], t=[3, 4, 5, 6], ra=[4, 6, 8], rb=[5, 7, 9]), derive=dict(A0='B0+t*(ra+rb)'),
                 q='Tank A has {A0} litres of water and loses {ra} litres every hour. Tank B has {B0} litres and gains {rb} litres every hour. On a line graph the two lines cross. After how many hours do the tanks hold the same amount?',
                 answer='t', hint='Make a table of the two amounts, hour by hour. What happens to the gap between them?',
                 steps=['At the start Tank A has {A0} − {B0} litres more than Tank B.', 'Each hour the gap closes by {ra} + {rb} litres.', 'The tanks hold the same amount after {ans} hours.']),
        oracle=lambda e: _tanks(e['B0'] + e['t'] * (e['ra'] + e['rb']), e['ra'], e['B0'], e['rb'])[0]),
    'G6-litres': dict(
        base=dict(B0=20, t=4, ra=6, rb=9),
        tpl=dict(vars=dict(B0=[10, 20, 30], t=[3, 4, 5, 6], ra=[4, 6, 8], rb=[5, 7, 9]), derive=dict(A0='B0+t*(ra+rb)'),
                 q='Tank A has {A0} litres of water and loses {ra} litres every hour. Tank B has {B0} litres and gains {rb} litres every hour. The lines cross when the tanks hold the same amount. How much is in each tank then?',
                 answer='B0+rb*t', hint='Make a table of the two amounts, hour by hour, until they are equal.',
                 steps=['Find the hour when the tanks are equal: the gap {A0} − {B0} closes by {ra} + {rb} litres each hour.', 'Then Tank B has {B0} + {rb} × {t} litres, and so does Tank A: {ans} litres.']),
        oracle=lambda e: _tanks(e['B0'] + e['t'] * (e['ra'] + e['rb']), e['ra'], e['B0'], e['rb'])[1]),
}
