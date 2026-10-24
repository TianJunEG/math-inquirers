"""Online practice for Level 6 (Primary 6, ages 11-13) holiday lesson 9: Data Detectives (averages and data: mean, total = mean x how many, median, mode; list-and-loop mean program).

The questions are the ones printed in the Level 6 holiday workbook (p6/content/l9.js workbook(): Start here Q1 to Q6; the Finish page: the Investigation (p6/content/gaps.json lesson 9)
and the exit slip (l9.js lesson.exit); Think harder = the first four l9.js qbank.stretch questions; Go further = the last three l9.js qbank.challenge questions).
Every answer is recomputed by an INDEPENDENT checker below: exact means (Fraction of total over count), the median by sorting, the mode by counting, a missing value by searching for the number
that gives the stated mean, the code questions by running the SAME block program that is drawn (w5lib.run), and the unique 'mean mystery' by trying every list of five whole numbers.
build_holiday.py stops if a checker and the printed answer differ.  Scratch is not run in the page.
"""
import itertools, os, re, sys
from fractions import Fraction
HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE_, '..'))
sys.path.insert(0, os.path.join(HERE_, '..', '..'))
from hlib import *      # noqa: E402,F401
import p6lib as P       # noqa: E402
import w5lib as W       # noqa: E402

M = W.MINUS
META = dict(level=6, lesson=9, key='p6', title='Data Detectives', workbook_title='DATA DETECTIVES', topic='Averages and Data', strand='Data and averages',
            sources=['p6/content/l9.js', 'p6/content/gaps.json'],
            intro=['You do not need Scratch on this page. The mean (the average) is the total divided by how many values there are. Turn it round: total = mean x how many values.',
                   'The median is the middle value when the numbers are in order. The mode is the value that appears most often.',
                   'Code is drawn as blocks so you can follow it; you never need to run it here.'])
ME, CO = 'Mean and total', 'Data and code'

_src = open(os.path.join(HERE_, '..', '..', '..', '..', 'p6', 'content', 'l9.js'), encoding='utf-8').read()
# ---- the two programs drawn in the workbook (the block texts are asserted to be in l9.js)
MEAN_PROG = ['when green flag clicked', 'set total to 0', 'set i to 1',
             {'c': 'repeat 4', 'body': ['change total by (item i of scores)', 'change i by 1']}, 'say (total / 4)']
PLAN_PROG = ['set count to 0', 'set i to 1',
             {'c': 'repeat (length of temps)', 'body': [{'c': 'if (item i of temps) > ( _____ ) then', 'body': ['change ( _____ ) by 1']}, 'change i by 1']}, 'say count']
for _p in (MEAN_PROG, PLAN_PROG):
    def _texts(prog):
        for it in prog:
            if isinstance(it, dict):
                yield it['c']
                yield from _texts(it['body'])
            else:
                yield it
    for _t in _texts(_p):
        assert _t in _src, _t
for _t in ('A dot plot of books read', 'A dot plot of pocket money from $8 to $22'):
    assert _t in _src, _t

BOOKS = [4, 7, 2, 8, 9]
SIT_MEAN, SIT_FIRST = 17, [15, 20, 14]
D3 = [6, 8, 10, 12, 14]
POCKET = [10, 12, 12, 15, 16, 20, 69]
SCORES = [5, 9, 6, 12]
TEMPS = [29, 31, 33, 30, 32, 34, 28]
DATA = [4, 6, 7, 9, 14]


def scoreslist(v):
    return ', '.join(str(x) for x in v)


def trend(old, new):
    return 'Up' if new > old else 'Down' if new < old else 'The same'


def mean_prog_fill(prog, blank1, blank2):
    """Fills the two blanks of the planning program (first blank: what the temperature is compared with; second: the variable that counts)."""
    out = []
    for it in prog:
        if isinstance(it, dict):
            head = it['c']
            if '( _____ )' in head:
                head = head.replace('( _____ )', f'({blank1})', 1)
            out.append({'c': head, 'body': mean_prog_fill(it['body'], blank1, blank2)})
        else:
            out.append(it.replace('( _____ )', f'({blank2})', 1) if '( _____ )' in it else it)
    return out


FIG_BOOKS = W.dot1()
FIG_POCKET = W.dot4()
FIG_MEAN = W.blocks('l9', MEAN_PROG, 'Code blocks: when green flag clicked, set total to 0, set i to 1, repeat 4 (change total by item i of scores, change i by 1), say total divided by 4.')
FIG_PLAN = W.blocks('l9', PLAN_PROG, 'Code blocks with two blanks: set count to 0, set i to 1, repeat length of temps (if item i of temps is greater than blank then change blank by 1; change i by 1), say count.', fs=15)


def trace_rows():
    tr = []
    W.run(MEAN_PROG, lists={'scores': SCORES}, trace=tr)
    rows = []
    for k, st in enumerate(tr):
        i_start = int(st['i']) - 1
        rows.append([i_start, SCORES[i_start - 1], int(st['total'])])
    return rows


TRACE = trace_rows()
ORD = ['1st', '2nd', '3rd', '4th']

ITEMS = []
A = ITEMS.append

# ================= Start here (workbook Lesson 9, Q1 to Q6)
A(dict(id='1a', tier='core', no='1(a)', type='number', strand=ME, skill='total of a list', answer=30, svg=FIG_BOOKS, label='1(a)',
       q='Five friends counted the books they read in the holidays: 4, 7, 2, 8, 9. What is the total?',
       check=lambda: sum(BOOKS),
       hint='Add the numbers two at a time and keep a running total.',
       steps=['4 + 7 = 11, 11 + 2 = 13, 13 + 8 = 21, 21 + 9 = 30.', 'The total is 30.'],
       src=['Five friends counted the books they read in the holidays']))
A(dict(id='1b', tier='core', no='1(b)', type='number', strand=ME, skill='mean as total divided by how many', answer=6, svg=FIG_BOOKS, label='1(b)',
       q='Five friends counted the books they read in the holidays: 4, 7, 2, 8, 9. What is the average (the mean) number of books?',
       check=lambda: W.whole(W.mean(BOOKS)),
       hint='The mean is what each friend would have if all the books were shared out equally between the 5 friends.',
       steps=['The total is 4 + 7 + 2 + 8 + 9 = 30 and there are 5 friends.', '30 ÷ 5 = 6.', 'The mean is 6.'],
       src=['The average (mean)?']))
A(dict(id='1c', tier='core', no='1(c)', type='fields', strand=ME, skill='balance check around the mean', answer=[-2, 1, -4, 2, 3], svg=FIG_BOOKS, label='1(c)',
       q='Balance check. Use the mean of the five friends\' books (4, 7, 2, 8, 9). How far is each value above or below the mean? Type a minus sign for below the mean (for above, just type the number).',
       frame='4 → {f1}   7 → {f2}   2 → {f3}   8 → {f4}   9 → {f5}',
       check=lambda: [v - W.whole(W.mean(BOOKS)) for v in BOOKS],
       hint='Count the steps from the mean up or down to each value. Below the mean is a minus number.',
       steps=['The mean is 6.', f'4 is 2 below 6, so {M}2. 7 is 1 above, so 1. 2 is 4 below, so {M}4.', '8 is 2 above, so 2. 9 is 3 above, so 3.'],
       src=['Balance check: how far is each value above (+) or below (−) the mean?']))
A(dict(id='1d', tier='core', no='1(d)', type='number', strand=ME, skill='values above and below the mean balance', answer=0, svg=FIG_BOOKS, label='1(d)',
       q='Balance check. Add up your five answers from the balance check (the distances above and below the mean). What do you get?',
       check=lambda: sum(v - W.mean(BOOKS) for v in BOOKS),
       hint='Add the numbers above the mean, then take away the numbers below it.',
       steps=[f'Above the mean: 1 + 2 + 3 = 6. Below the mean: {M}2 and {M}4, which make {M}6.', f'6 + ({M}6) = 0.',
              'The answer is 0: the amounts above the mean and the amounts below it balance. This is true for the mean of any list of numbers.'],
       src=['Add them up']))

A(dict(id='2a', tier='core', no='2(a)', type='number', strand=ME, skill='total from a mean', answer=68, label='2(a)',
       q='Siti played 4 games. Her mean score was 17. Her first three scores were 15, 20 and 14. What was her total for the 4 games?',
       check=lambda: SIT_MEAN * 4,
       hint='Mean x how many values gives the total.',
       steps=['The total is the mean x the number of games.', '17 x 4 = 68.', 'Her total for the 4 games was 68.'],
       src=['Siti played 4 games. Her mean score was 17. Her first three scores were 15, 20 and 14.']))
A(dict(id='2b', tier='core', no='2(b)', type='number', strand=ME, skill='missing value from a mean', answer=19, label='2(b)',
       q='Siti played 4 games. Her mean score was 17. Her first three scores were 15, 20 and 14. What was her 4th score?',
       check=lambda: next(s for s in range(1, 200) if W.mean(SIT_FIRST + [s]) == SIT_MEAN),
       hint='Find the total for all 4 games first. How much of it do the three scores you know use up?',
       steps=['The total for 4 games is 4 x 17 = 68.', 'The first three scores add up to 15 + 20 + 14 = 49.', '68 − 49 = 19.', 'Her 4th score was 19. (Check: 49 + 19 = 68, and 68 ÷ 4 = 17.)'],
       src=['Her 4th score?']))
A(dict(id='2c', tier='core', no='2(c)', type='number', strand=ME, skill='new value for a target mean', answer=22, label='2(c)',
       q='Siti played 4 games with a mean score of 17. She plays a 5th game. What score makes her mean exactly 18?',
       check=lambda: next(s for s in range(1, 200) if Fraction(SIT_MEAN * 4 + s, 5) == 18),
       hint='How big must the total for 5 games be to give a mean of 18? How much of it does she already have?',
       steps=['A mean of 18 over 5 games needs a total of 5 x 18 = 90.', 'After 4 games her total is 4 x 17 = 68.', '90 − 68 = 22.', 'She needs 22 in the 5th game. (Check: 68 + 22 = 90, and 90 ÷ 5 = 18.)'],
       src=['A 5th game: what score makes her mean exactly 18?']))

CH3 = [('a', 'Add a new value, 10.', 'adding a value equal to the mean'), ('b', 'Add 3 to every value.', 'adding the same amount to every value'),
       ('c', 'Remove the 14.', 'removing a value above the mean'), ('d', 'Change the 14 to 44.', 'raising one value')]


def d3_after(k):
    if k == 'a':
        return D3 + [10]
    if k == 'b':
        return [v + 3 for v in D3]
    if k == 'c':
        return [v for v in D3 if v != 14]
    return [v if v != 14 else 44 for v in D3]


P3 = dict(
    a=('Is the new value above, below or equal to the mean of 10?', 'Work out the new total and how many values there are now.',
       ['The new value, 10, is equal to the mean.', 'A value equal to the mean does not move the balance point, so the mean stays the same.'],
       ['The old total is 5 x 10 = 50. Adding 10 makes 60, and there are 6 values now.', '60 ÷ 6 = 10.', 'The new mean is 10.']),
    b=('Every value gets 3 bigger. Think of the towers: where does the level go?', 'Work out the new total, then share it equally.',
       ['Every value is 3 bigger, so the total goes up (by 5 x 3 = 15).', 'The same total is shared by the same number of values, so the mean goes up.'],
       ['The old total is 50. Adding 3 to each of 5 values adds 15, so the new total is 65.', '65 ÷ 5 = 13.', 'The new mean is 13.']),
    c=('Is the value you take away above or below the mean?', 'Take 14 away from the total, and one away from how many values there are.',
       ['14 is above the mean of 10.', 'Taking away a value that is above the mean lowers the mean, so it goes down.'],
       ['The old total is 50. Take away 14: 36. There are 4 values left.', '36 ÷ 4 = 9.', 'The new mean is 9.']),
    d=('The 14 changes to a much bigger number. What happens to the total?', 'Work out the new total, then divide by how many values there are.',
       ['44 is 30 more than 14, so the total goes up by 30 and the number of values stays 5.', 'A bigger total shared by 5 values means a bigger mean, so it goes up.'],
       ['The old total is 50. 50 − 14 + 44 = 80.', '80 ÷ 5 = 16.', 'The new mean is 16.']))
for k, what, _sk in CH3:
    after = d3_after(k)
    hp, hm, sp, sm = P3[k]
    A(dict(id=f'3{k}p', tier='core', no=f'3({k}) predict', type='choice', strand=ME, skill='predicting how the mean changes', options=['Up', 'Down', 'The same'], label=f'3({k}) predict',
           q=f'The data 6, 8, 10, 12, 14 has a mean of 10. Predict first. Change: {what[0].lower() + what[1:]} Does the mean go up, go down or stay the same?',
           answer=trend(W.mean(D3), W.mean(after)), check=(lambda after=after: trend(W.mean(D3), W.mean(after))),
           hint=hp, steps=sp, src=[f'({k}) {what}', 'Predict first: up, down or the same?']))
    A(dict(id=f'3{k}m', tier='core', no=f'3({k}) new mean', type='number', strand=ME, skill='new mean after a change', label=f'3({k}) mean',
           q=f'The data 6, 8, 10, 12, 14 has a mean of 10. Work out the new mean after this change: {what[0].lower() + what[1:]}',
           answer=W.whole(W.mean(after)), check=(lambda after=after: W.whole(W.mean(after))),
           hint=hm, steps=sm, src=[f'({k}) {what}', 'Then work out the new mean.']))

A(dict(id='4a', tier='core', no='4(a)', type='number', strand=ME, skill='mean with an extreme value', answer=22, svg=FIG_POCKET, label='4(a)',
       q='Seven P6 pupils get this pocket money each week: $10, $12, $12, $15, $16, $20, $69. The total is $154. What is the mean? (in dollars)',
       check=lambda: W.whole(W.mean(POCKET)),
       hint='Share the total equally between the 7 pupils.',
       steps=['154 ÷ 7 = 22.', 'The mean is $22.'], src=['Mean (total $154)']))
A(dict(id='4b', tier='core', no='4(b)', type='number', strand=ME, skill='median', answer=15, svg=FIG_POCKET, label='4(b)',
       q='Seven P6 pupils get this pocket money each week: $10, $12, $12, $15, $16, $20, $69. What is the median (the middle value when the amounts are in order)? (in dollars)',
       check=lambda: W.whole(W.median(POCKET)),
       hint='The amounts are already in order. Which one has the same number of amounts on each side of it?',
       steps=['The 7 amounts are in order, so the middle one is the 4th.', 'Three amounts are below it ($10, $12, $12) and three are above it ($16, $20, $69).', 'The median is $15.'],
       src=['Median']))
A(dict(id='4c', tier='core', no='4(c)', type='number', strand=ME, skill='mode', answer=12, svg=FIG_POCKET, label='4(c)',
       q='Seven P6 pupils get this pocket money each week: $10, $12, $12, $15, $16, $20, $69. What is the mode (the amount that appears most often)? (in dollars)',
       check=lambda: W.modes(POCKET)[0] if len(W.modes(POCKET)) == 1 else None,
       hint='Which amount is written more than once?',
       steps=['$12 appears twice. Every other amount appears once.', 'The mode is $12.'], src=['Mode']))
A(dict(id='4d', tier='core', no='4(d)', type='number', strand=ME, skill='comparing values with the mean', answer=6, svg=FIG_POCKET, label='4(d)',
       q='Seven P6 pupils get this pocket money each week: $10, $12, $12, $15, $16, $20, $69. Use the mean of these amounts. How many of the 7 pupils get less than the mean?',
       check=lambda: sum(1 for v in POCKET if v < W.mean(POCKET)),
       hint='Compare each amount with the mean. Which pupils get less than it?',
       steps=['The mean is $22.', 'Every amount except $69 is less than $22: $10, $12, $12, $15, $16 and $20.', '6 of the 7 pupils get less than the mean.'],
       src=['How many of the pupils get less than the mean?']))
OPT_FAIR = ['Yes, it is fair', 'No, it is not fair']
A(dict(id='4ef', tier='core', no='4(e) fair', type='choice', strand=ME, skill='a misleading mean', options=OPT_FAIR, answer=OPT_FAIR[1], svg=FIG_POCKET, label='4(e) fair',
       q='Seven P6 pupils get this pocket money each week: $10, $12, $12, $15, $16, $20, $69. Jun says, "A typical pupil gets the mean amount a week." Is that fair?',
       check=lambda: OPT_FAIR[1] if sum(1 for v in POCKET if v < W.mean(POCKET)) > len(POCKET) / 2 else OPT_FAIR[0],
       hint='Count how many of the 7 pupils get less than the mean.',
       steps=['The mean is $22, but 6 of the 7 pupils get less than $22.', 'The mean is bigger than what most pupils get, so it does not describe a typical pupil.'],
       src=['Is that fair?']))
OPT_AVG = ['The mean', 'The median']


def closer_average():
    """The average that is nearer to the amounts overall: the smaller total distance from all seven amounts."""
    dm = sum(abs(v - W.mean(POCKET)) for v in POCKET)
    dd = sum(abs(v - W.median(POCKET)) for v in POCKET)
    return OPT_AVG[1] if dd < dm else OPT_AVG[0]


A(dict(id='4eb', tier='core', no='4(e) better', type='choice', strand=ME, skill='choosing an average', options=OPT_AVG, answer=OPT_AVG[1], svg=FIG_POCKET, label='4(e) better',
       q='Seven P6 pupils get this pocket money each week: $10, $12, $12, $15, $16, $20, $69. Which average describes a typical pupil better, the mean or the median?',
       check=closer_average,
       hint='Think about what the one very large amount, $69, does to each average.',
       steps=['The mean is $22, pulled up by the $69. The median is $15, the amount of the middle pupil.',
              'The median does not move when the largest amount is made bigger, so it is the better description of a typical pupil here.'],
       src=['Which average describes a typical pupil better?']))
A(dict(id='4ew', tier='core', no='4(e) explain', type='selfcheck', strand=ME, skill='explaining a misleading average', svg=FIG_POCKET, label='4(e) explain',
       q='Look at the mean, the median and the seven amounts of pocket money. Explain which average describes a typical pupil better, and why. Write your reason, then check it against the worked solution.',
       facts=dict(below=6, median=15, mean=22), check=lambda: dict(below=sum(1 for v in POCKET if v < W.mean(POCKET)), median=W.whole(W.median(POCKET)), mean=W.whole(W.mean(POCKET))),
       hint='Compare the mean and the median with the amounts most pupils really get.',
       steps=['The mean is $22, but 6 of the 7 pupils get less than $22.', 'The one very large amount, $69, pulls the mean up.',
              'The median, $15, is the middle amount. It is not pulled up by the $69, so it describes a typical pupil better.'],
       src=['Which average describes a typical pupil better? Explain.']))

for k in range(4):
    row = TRACE[k]
    prev = TRACE[k - 1][2] if k else 0
    A(dict(id=f'5r{k + 1}', tier='core', no=f'5 loop {k + 1}', type='fields', strand=CO, skill='tracing a loop', label=f'5 loop {k + 1}', svg=FIG_MEAN,
           q=f'Trace the code. The list called scores holds 5, 9, 6 and 12 (item 1 is 5, item 2 is 9, and so on). Fill in the row for the {ORD[k]} time round the loop: i at the start, item i, and total at the end.',
           frame='i {f1}   item i {f2}   total {f3}', answer=row, check=(lambda k=k: TRACE[k]),
           hint=('Before the loop, total is 0 and i is 1. Which item of scores is item 1?' if k == 0 else
                 'Each time round starts where the last time round ended: total and i keep their values, and i went up by 1.'),
           steps=[f'i is {row[0]} when this time round starts.', f'Item {row[0]} of scores is {row[1]}.', f'total was {prev}, and {prev} + {row[1]} = {row[2]}.'],
           src=['Fill in the trace table, one row for each time round the loop.']))
A(dict(id='5a', tier='core', no='5(a)', type='number', strand=CO, skill='tracing a loop', answer=8, svg=FIG_MEAN, label='5(a)',
       q='Trace the code. The list called scores holds 5, 9, 6 and 12. What does the sprite say at the end?',
       check=lambda: W.whole(W.run(MEAN_PROG, lists={'scores': SCORES})[0][-1]),
       hint='Follow the loop round 4 times, then do the last block.',
       steps=['After the loop, total is 5 + 9 + 6 + 12 = 32.', 'The last block says total / 4 = 32 ÷ 4 = 8.', 'The sprite says 8.'],
       src=['What does the sprite say?']))


def which_blocks_hold_the_length():
    """The blocks of the drawn program with the list length (4) written into them as a number."""
    heads = [it['c'] if isinstance(it, dict) else it for it in MEAN_PROG]
    return [h for h in heads if re.search(r'\b%d\b' % len(SCORES), h)]


OPT_BLK = ['repeat 4 and say (total / 4)', 'set total to 0 and set i to 1', 'change total by (item i of scores) and change i by 1', 'when green flag clicked and say (total / 4)']
A(dict(id='5bk', tier='core', no='5(b) blocks', type='choice', strand=CO, skill='making a program work for any length', options=OPT_BLK, answer=OPT_BLK[0], label='5(b) blocks',
       svg=W.blocks('l9', MEAN_PROG, 'Code blocks: when green flag clicked, set total to 0, set i to 1, repeat 4 (change total by item i of scores, change i by 1), say total divided by 4.'),
       q='Jo adds a 5th score, 13, to the list scores. Which two blocks must change so the program works for a list of ANY length?',
       check=lambda: ' and '.join(which_blocks_hold_the_length()),
       hint='Look for the blocks that only work when the list has exactly 4 items.',
       steps=['"repeat 4" goes round the loop exactly 4 times, and "say (total / 4)" divides by exactly 4.',
              'For a list of any length both must use the length of the list: repeat (length of scores) and say (total / (length of scores)).',
              'The other blocks work for a list of any length.'],
       src=['Which two blocks must change so the program works for a list of ANY length?']))
FIXED = [it if not isinstance(it, dict) else {'c': 'repeat (length of scores)', 'body': it['body']} for it in MEAN_PROG]
FIXED[-1] = 'say (total / (length of scores))'
A(dict(id='5bs', tier='core', no='5(b) says', type='number', strand=CO, skill='the mean program with a longer list', answer=9, label='5(b) says',
       q='Jo adds a 5th score, 13, to the list scores (now 5, 9, 6, 12, 13) and changes the program so it works for a list of any length. What does the sprite say now?',
       check=lambda: W.whole(W.run(FIXED, lists={'scores': SCORES + [13]})[0][-1]),
       hint='Add up all 5 scores, then divide by how many scores there are.',
       steps=['The total is 5 + 9 + 6 + 12 + 13 = 45.', 'There are 5 scores, so the program says 45 ÷ 5 = 9.', 'The sprite says 9.'],
       src=['What should it say now?']))

A(dict(id='6a', tier='core', no='6(a)', type='number', strand=ME, skill='mean temperature', answer=31, label='Bonus 6(a)',
       q='Bonus question. The highest temperature each day for a week in Singapore, in °C: 29, 31, 33, 30, 32, 34, 28. What is the mean temperature?',
       check=lambda: W.whole(W.mean(TEMPS)),
       hint='Add the seven temperatures, then share the total equally between the 7 days.',
       steps=['The total is 29 + 31 + 33 + 30 + 32 + 34 + 28 = 217.', '217 ÷ 7 = 31.', 'The mean temperature is 31 °C.'],
       src=['The highest temperature each day for a week in Singapore, in °C']))
A(dict(id='6b', tier='core', no='6(b)', type='number', strand=ME, skill='counting values above the mean', answer=3, label='Bonus 6(b)',
       q='Bonus question. The highest temperature each day for a week in Singapore, in °C: 29, 31, 33, 30, 32, 34, 28. How many days were hotter than the mean temperature?',
       check=lambda: sum(1 for t in TEMPS if t > W.mean(TEMPS)),
       hint='Find the mean first. Then look at each day and ask: is it hotter than the mean?',
       steps=['The mean temperature is 31 °C.', 'The days hotter than 31 °C are 33, 32 and 34.', '3 days were hotter than the mean.'],
       src=['Days hotter than the mean?']))
OPT_VAR = ['mean', 'count', 'total', 'i']
STEM6 = 'Bonus question. Plan your code. The variable mean already holds the mean temperature. The program counts the days hotter than the mean. '
A(dict(id='6c1', tier='core', no='6(c) blank 1', type='choice', strand=CO, skill='planning a counting loop', options=OPT_VAR, answer='mean', svg=FIG_PLAN, label='6(c) blank 1',
       q=STEM6 + 'Which variable goes in blank 1 (the one each temperature is compared with)?',
       check=lambda: 'mean',
       hint='Each temperature is tested to see if it is hotter than what?',
       steps=['The program asks, for each temperature: is it greater than the mean?', 'So blank 1 is mean.'],
       src=['The variable mean already holds your answer to (a).', 'Blank 1:']))
A(dict(id='6c2', tier='core', no='6(c) blank 2', type='choice', strand=CO, skill='planning a counting loop', options=OPT_VAR, answer='count', svg=FIG_PLAN, label='6(c) blank 2',
       q=STEM6 + 'Which variable goes in blank 2 (the one that goes up by 1 each time a day is hotter)?',
       check=lambda: 'count',
       hint='Look at the first and the last block of the program. Which variable starts at 0 and is said at the end?',
       steps=['The program starts with "set count to 0" and ends with "say count".', 'So the variable that goes up by 1 for each hot day is count.'],
       src=['Blank 2:']))
A(dict(id='6c3', tier='core', no='6(c) says', type='number', strand=CO, skill='tracing a counting loop', answer=3, svg=FIG_PLAN, label='6(c) says',
       q='Bonus question. Plan your code. The blanks are filled in correctly, mean holds the mean temperature, and the program runs on these temperatures: 29, 31, 33, 30, 32, 34, 28. What does the sprite say?',
       check=lambda: W.whole(W.run(mean_prog_fill(PLAN_PROG, 'mean', 'count'), v={'mean': 31}, lists={'temps': TEMPS})[0][-1]),
       hint='Go through the seven temperatures one at a time. Add 1 to the count each time one is hotter than the mean.',
       steps=['The mean is 31. The temperatures hotter than 31 are 33, 32 and 34.', 'The count goes up by 1 three times.', 'The sprite says 3.'],
       src=['It says:']))

A(dict(id='Xa', tier='core', no='Exit slip (a)', type='number', strand=ME, skill='missing value from a mean', answer=10, label='Exit (a)',
       q='The mean of 3 numbers is 9. Two of them are 5 and 12. What is the third number?',
       check=lambda: next(s for s in range(1, 200) if W.mean([5, 12, s]) == 9),
       hint='Find the total of the 3 numbers first. Then take away the two you know.',
       steps=['The total of the 3 numbers is 3 x 9 = 27.', '5 + 12 = 17.', '27 − 17 = 10.', 'The third number is 10.'],
       src=['The mean of 3 numbers is 9. Two of them are 5 and 12. What is the third number?']))
A(dict(id='Xb', tier='core', no='Exit slip (b)', type='number', strand=ME, skill='new mean after adding a value', answer=10, label='Exit (b)',
       q='The mean of 3 numbers is 9. Two of them are 5 and 12. A fourth number, 13, is added. What is the new mean?',
       check=lambda: W.whole(W.mean([5, 12, next(s for s in range(1, 200) if W.mean([5, 12, s]) == 9), 13])),
       hint='Work out the new total of the 4 numbers, then divide by 4.',
       steps=['The total of the first 3 numbers is 3 x 9 = 27.', 'Adding 13 makes 27 + 13 = 40, and there are 4 numbers.', '40 ÷ 4 = 10.', 'The new mean is 10.'],
       src=['A fourth number, 13, is added. What is the new mean?']))

# ================= Investigation (printed on the Finish page)
INV_NO = 'Investigation'


def mode_options(data):
    return ['There is no mode'] + [f'The mode is {v}' for v in sorted(set(data))]


def mode_answer(data):
    m = W.modes(data)
    return 'There is no mode' if not m else f'The mode is {m[0]}'


A(dict(id='I1', tier='invest', no='Investigation first step', type='number', strand=ME, skill='mean of a list', answer=8, label='Inv 1',
       q='What if one number changes? The data is 4, 6, 7, 9, 14. First step: find the mean of 4, 6, 7, 9 and 14.',
       check=lambda: W.whole(W.mean(DATA)),
       hint='Add them up, then share the total equally.',
       steps=['4 + 6 + 7 + 9 + 14 = 40.', '40 ÷ 5 = 8.', 'The mean is 8.'],
       src=['First step: find the mean of 4, 6, 7, 9 and 14']))
A(dict(id='I2', tier='invest', no='Investigation 2', type='number', strand=ME, skill='median', answer=7, label='Inv 2',
       q='The data is 4, 6, 7, 9, 14. What is the median?',
       check=lambda: W.whole(W.median(DATA)),
       hint='The numbers are in order. Find the middle one.',
       steps=['There are 5 numbers in order: 4, 6, 7, 9, 14.', 'The middle one is the 3rd, which is 7.', 'The median is 7.'],
       src=['Find the mean, the median and the mode']))
A(dict(id='I3', tier='invest', no='Investigation 3', type='choice', strand=ME, skill='mode', options=mode_options(DATA), answer=mode_answer(DATA), label='Inv 3',
       q='The data is 4, 6, 7, 9, 14. Is there a mode?',
       check=lambda: mode_answer(DATA),
       hint='Does any number appear more than once?',
       steps=['Every number appears exactly once, so no number appears most often.', 'There is no mode.'],
       src=['(is there one?)']))
INV_ID = 4
for c, label in ((24, 'change 24'), (4, 'change 4'), (7, 'change 7')):
    d = DATA[:-1] + [c]
    ds = ', '.join(str(x) for x in d)
    is_dec = W.mean(d).denominator != 1
    mean_item = dict(id=f'I{INV_ID}', tier='invest', no=f'Investigation {INV_ID}', strand=ME, skill='mean after one value changes', label=f'Inv {INV_ID}',
                     q=f'Change the 14 to {c}. The data is now {ds}. What is the mean?',
                     hint='Work out the new total, then divide by 5.',
                     steps=[f'The new total is {" + ".join(str(x) for x in d)} = {sum(d)}.', (f'{sum(d)} ÷ 5 = {W.dec(W.mean(d))}.'), f'The mean is {W.dec(W.mean(d))}.'],
                     src=['Now change the 14 to 24, then change it to 4, then to 7.'])
    if is_dec:
        mean_item.update(type='text', accept=[W.dec(W.mean(d)), W.dec(W.mean(d)) + '0'], shown=W.dec(W.mean(d)), check=(lambda d=d: W.dec(W.mean(d))))
        mean_item['q'] += ' Type a decimal.'
    else:
        mean_item.update(type='number', answer=W.whole(W.mean(d)), check=(lambda d=d: W.whole(W.mean(d))))
    A(mean_item)
    A(dict(id=f'I{INV_ID + 1}', tier='invest', no=f'Investigation {INV_ID + 1}', type='number', strand=ME, skill='median after one value changes', label=f'Inv {INV_ID + 1}',
           q=f'Change the 14 to {c}. The data is now {ds}. What is the median?',
           answer=W.whole(W.median(d)), check=(lambda d=d: W.whole(W.median(d))),
           hint='Put the numbers in order first. Then find the middle one.',
           steps=[f'In order the numbers are {", ".join(str(x) for x in sorted(d))}.', f'The middle (3rd) number is {sorted(d)[2]}.', f'The median is {sorted(d)[2]}.'],
           src=['Make a table of the mean, median and mode each time.']))
    A(dict(id=f'I{INV_ID + 2}', tier='invest', no=f'Investigation {INV_ID + 2}', type='choice', strand=ME, skill='mode after one value changes', label=f'Inv {INV_ID + 2}',
           options=mode_options(d), answer=mode_answer(d), check=(lambda d=d: mode_answer(d)),
           q=f'Change the 14 to {c}. The data is now {ds}. Is there a mode?',
           hint='Does any number appear more than once now?',
           steps=([f'{W.modes(d)[0]} appears twice and every other number appears once.', f'The mode is {W.modes(d)[0]}.'] if W.modes(d) else
                  ['Every number appears exactly once.', 'There is no mode.']),
           src=['Make a table of the mean, median and mode each time.']))
    INV_ID += 3

SETS = [DATA, DATA[:-1] + [24], DATA[:-1] + [4], DATA[:-1] + [7]]
A(dict(id='Iw', tier='invest', no='Investigation (a)', type='selfcheck', strand=ME, skill='what changes and what stays the same', label='Inv (a)',
       q='Look at your table of the mean, the median and the mode for the four lists of data (the original, and the 14 changed to 24, to 4 and to 7). What changes? What stays the same? Explain why. '
         'Write your reasons, then check them against the worked solution.',
       facts=dict(means=['8', '10', '6', '6.6'], medians=[7, 7, 6, 7], modes=['none', 'none', '4', '7']),
       check=lambda: dict(means=[W.dec(W.mean(s)) for s in SETS], medians=[W.whole(W.median(s)) for s in SETS], modes=[(str(W.modes(s)[0]) if W.modes(s) else 'none') for s in SETS]),
       hint='Compare each row of your table with the first row. Which numbers moved and which stayed put?',
       steps=['Mean: 8, then 10, 6 and 6.6. It changed every time, because the mean uses every value, so changing one value changes the total.',
              'Median: 7, 7, 6 and 7. It stayed 7 when the 14 became 24 or 7, but fell to 6 when the 14 became 4, because then the numbers in order were 4, 4, 6, 7, 9 and the middle one was 6.',
              'Mode: there was no mode at first. A mode only appears when two values are the same: 4 and 4, or 7 and 7.'],
       src=['What changes? What stays the same?']))
EX_TWO = [6, 6, 7, 9, 12]
A(dict(id='I2n', tier='invest', no='Investigation (b)', type='selfcheck', strand=ME, skill='changing two numbers and keeping the mean', label='Inv (b)',
       q='Can you change TWO of the numbers in 4, 6, 7, 9, 14 and keep the mean the same? Try to find a way, then check against the worked solution.',
       facts=dict(total=40, example_total=40), check=lambda: dict(total=sum(DATA), example_total=sum(EX_TWO)),
       hint='The mean stays the same only if the total stays the same. If one number goes up, what must the other do?',
       steps=['The mean stays the same if the total stays the same, and the total of 4, 6, 7, 9, 14 is 40.',
              'Change one number up by some amount and another down by the same amount. For example, 4 to 6 (up 2) and 14 to 12 (down 2) gives 6, 6, 7, 9, 12.',
              'The new total is 6 + 6 + 7 + 9 + 12 = 40, so the mean is still 8. Many other pairs of changes also work, as long as the total stays 40.'],
       src=['Can you change TWO numbers and keep the mean the same?']))

# ================= Think harder (first four qbank.stretch questions)
A(dict(id='T1', tier='stretch', no='T1', type='number', strand=ME, skill='new value from a change in the mean', answer=160, label='T1',
       q='The mean height of 4 children is 150 cm. A fifth child joins the group and the mean height becomes 152 cm. How tall is the fifth child? (in cm)',
       check=lambda: next(h for h in range(100, 300) if Fraction(4 * 150 + h, 5) == 152),
       hint='Work out the total height of the 4 children, and then the total height of all 5.',
       steps=['The 4 children have a total height of 4 x 150 = 600 cm.', 'All 5 have a total of 5 x 152 = 760 cm.', '760 − 600 = 160.', 'The fifth child is 160 cm tall.'],
       src=['The mean height of 4 children is 150 cm.']))
A(dict(id='T2', tier='stretch', no='T2', type='number', strand=ME, skill='score needed for a target mean', answer=92, label='T2',
       q='Mei\'s mean score for 3 tests is 84. What must she score in the 4th test to raise her mean to 86?',
       check=lambda: next(s for s in range(1, 300) if Fraction(3 * 84 + s, 4) == 86),
       hint='Find the total she needs after 4 tests, and the total she has after 3.',
       steps=['After 3 tests her total is 3 x 84 = 252.', 'For a mean of 86 over 4 tests she needs 4 x 86 = 344.', '344 − 252 = 92.', 'She must score 92 in the 4th test.'],
       src=['Mei’s mean score for 3 tests is 84.']))
EX_T3 = [4, 4, 5, 8, 9]
A(dict(id='T3', tier='stretch', no='T3', type='selfcheck', strand=ME, skill='building a list with a given mean and mode', label='T3',
       q='Write 5 whole numbers with a mean of 6 and a mode of 4. Check your total and your mode, then compare with the worked example.',
       facts=dict(total=30, mean=6, mode=4), check=lambda: dict(total=sum(EX_T3), mean=W.whole(W.mean(EX_T3)), mode=W.modes(EX_T3)[0]),
       hint='The mean tells you what all five numbers must add up to. The mode is the number that appears most often.',
       steps=['A mean of 6 for 5 numbers means the total must be 5 x 6 = 30.', 'The mode is 4, so 4 must appear more often than any other number (at least twice).',
              'Example: 4, 4, 5, 8, 9. The total is 30, so the mean is 6, and 4 appears twice. Many other lists work too.'],
       src=['Write 5 whole numbers with a mean of 6 and a mode of 4.']))
A(dict(id='T4', tier='stretch', no='T4', type='number', strand=CO, skill='the mean program with a new value', answer=13, label='T4',
       q='A Scratch list holds 8 numbers with a mean of 12. Then the number 21 is added to the list. What will the mean program say now?',
       check=lambda: W.whole(W.run([{'c': 'repeat 8', 'body': ['change total by 12']}, 'change total by 21', 'say (total / 9)'], v={'total': 0})[0][-1]),
       hint='Find the total of the 8 numbers first. Add the new number, then divide by how many numbers there are now.',
       steps=['The 8 numbers have a total of 8 x 12 = 96.', 'Adding 21 gives 96 + 21 = 117, and there are 9 numbers.', '117 ÷ 9 = 13.', 'The mean program says 13.'],
       src=['A Scratch list holds 8 numbers with a mean of 12.']))

# ================= Go further (last three qbank.challenge questions)


def mean_mysteries():
    """Every list of five whole numbers (1 to 12) with mean 5, median 4, mode 4 (the only mode), smallest 2 and largest 9, in order."""
    out = []
    for c in itertools.combinations_with_replacement(range(1, 13), 5):
        if sum(c) == 25 and c[2] == 4 and c[0] == 2 and c[4] == 9 and W.modes(list(c)) == [4]:
            out.append(list(c))
    return out


A(dict(id='C1', tier='challenge', no='C1', type='selfcheck', open=True, marking_mode='open', strand=ME, skill='writing mean, median and mode clues', label='C1',
       q='Make up your own "mean mystery" like the Think harder mean puzzles: choose five whole numbers, then write clues (any of mean, median, mode, smallest, largest) that give ONLY your numbers. '
         'Then compare with the worked example.',
       hint='Pick your five numbers first, then work out their mean, median and mode. Check that your clues cannot fit a different list.',
       steps=['Open: many mysteries work. The clues must fit your numbers and no other list.',
              'Example clues: mean 5, median 4, mode 4, smallest 2, largest 9. The total is 5 x 5 = 25, so the middle three numbers (with the smallest and largest) leave 25 − 2 − 4 − 9 = 10 for the 2nd and 4th numbers.',
              'The 2nd number is from 2 to 4 and the 4th from 4 to 9. Of the pairs that make 10, only 4 and 6 make 4 the mode, so the numbers are 2, 4, 4, 6, 9 and no other list fits.'],
       src=['Make up your own “mean mystery” like the Think harder mean puzzles']))
assert mean_mysteries() == [[2, 4, 4, 6, 9]]
GAUSS = [(a, 100 - a) for a in range(1, 50)]
A(dict(id='C2a', tier='challenge', no='C2(a)', type='selfcheck', strand=ME, skill='explaining a mean by pairing', label='C2(a)',
       q='The mean of 1, 2, 3, … , 99 is 50. Explain why this is true without adding them all up. Write your reason, then check it against the worked solution.',
       facts=dict(pairs=49, pair_total=100, total=4950), check=lambda: dict(pairs=len(GAUSS), pair_total=100 if all(a + b == 100 for a, b in GAUSS) else None, total=sum(range(1, 100))),
       hint='Add the smallest number and the biggest number. Then the second smallest and the second biggest. What do you notice?',
       steps=['Pair the numbers from the two ends: 1 + 99, 2 + 98, … , 49 + 51. Every pair makes 100.', 'That is 49 pairs, and 50 is left in the middle on its own.',
              'In every pair one number is as far below 50 as the other is above it, so the numbers balance round 50 and the mean is 50.', 'Check: the total is 4950, and 4950 ÷ 99 = 50.'],
       src=['The mean of 1, 2, 3, … , 99 is 50. Explain why without adding them all up.']))
PROG_C2 = ['when green flag clicked', 'set total to 0', 'set n to 1', {'c': 'repeat 99', 'body': ['change total by n', 'change n by 1']}, 'say (total / 99)']
A(dict(id='C2b', tier='challenge', no='C2(b)', type='selfcheck', paper=True, strand=CO, skill='planning a program that checks a mean', label='C2(b)',
       q='The mean of 1, 2, 3, … , 99 is 50. Plan a short program that checks it. Sketch the blocks on paper.',
       facts=dict(says=50), check=lambda: dict(says=W.whole(W.run(PROG_C2)[0][-1])),
       sol_fig=lambda f: W.blocks('l9', PROG_C2, 'A program that checks the mean: when green flag clicked, set total to 0, set n to 1, repeat 99 (change total by n, change n by 1), say total divided by 99.'),
       hint='You need a total that starts at 0 and a number n that goes 1, 2, 3, … up to 99.',
       steps=['One program: set total to 0 and n to 1; repeat 99 times: change total by n, then change n by 1; at the end say total / 99.', 'Running it, the sprite says 50. Other plans can be right too.'],
       src=['Then plan a short program that checks it.']))
A(dict(id='C3a', tier='challenge', no='C3(a)', type='number', strand=ME, skill='finding a value from two means', answer=68, label='C3(a)',
       q='A group of 8 children has a mean mass of 41 kg. When their tutor joins, the mean mass of all 9 becomes 44 kg. What is the tutor\'s mass? (in kg)',
       check=lambda: next(t for t in range(1, 300) if Fraction(8 * 41 + t, 9) == 44),
       hint='Find the total mass of the 8 children and the total mass of all 9 people.',
       steps=['The 8 children have a total mass of 8 x 41 = 328 kg.', 'All 9 people have a total mass of 9 x 44 = 396 kg.', '396 − 328 = 68.', 'The tutor\'s mass is 68 kg.'],
       src=['A group of 8 children has a mean mass of 41 kg.']))
A(dict(id='C3b', tier='challenge', no='C3(b)', type='number', strand=ME, skill='finding a value from two means', answer=34, label='C3(b)',
       q='A group of 8 children has a mean mass of 41 kg. When their tutor joins, the mean mass of all 9 becomes 44 kg. Then one more person joins, and the mean mass of all 10 becomes 43 kg. '
         'What is the mass of the last person to join? (in kg)',
       check=lambda: next(p for p in range(1, 300) if Fraction(9 * 44 + p, 10) == 43),
       hint='Compare the total mass of all 9 people with the total mass of all 10.',
       steps=['All 9 people have a total mass of 9 x 44 = 396 kg.', 'All 10 people have a total mass of 10 x 43 = 430 kg.', '430 − 396 = 34.', 'The last person to join has a mass of 34 kg.'],
       src=['Then one more person joins and the mean of all 10 becomes 43 kg.']))

for _it in ITEMS:
    _it['q'] = re.sub(r'\s{2,}', ' ', _it['q'])
    if _it.get('frame'):
        _it['frame'] = W.nb(_it['frame'])

P.finish(ITEMS)

# ---------------------------------------------------------------- variant families (every combination is run against an independent oracle at build time)
VARIANTS = {
    '2b': dict(base=dict(m=17, x=15, y=20, z=14),
               tpl=dict(vars=dict(m=[17, 18, 19, 20, 21], x=[13, 14, 15, 16, 18], y=[14, 16, 18, 20, 22], z=[12, 14, 16, 19]), derive=dict(tot='4*m', known='x+y+z'),
                        q='Sam played 4 games. His mean score was {m}. His first three scores were {x}, {y} and {z}. What was his 4th score?', answer='4*m-x-y-z',
                        hint='Find the total for all 4 games first. How much of it do the three scores you know use up?',
                        steps=['The total for 4 games is 4 x {m} = {tot}.', 'The first three scores add up to {x} + {y} + {z} = {known}.', '{tot} − {known} = {ans}.']),
               oracle=lambda e: next(s for s in range(1, 300) if W.mean([e['x'], e['y'], e['z'], s]) == e['m'])),
    '3bm': dict(base=dict(c=3),
                tpl=dict(vars=dict(c=[1, 2, 3, 4, 5, 6, 7, 8, 9]), derive=dict(inc='5*c'),
                         q='The data 6, 8, 10, 12, 14 has a mean of 10. Work out the new mean after this change: add {c} to every value.', answer='10+c',
                         hint='Work out the new total, then share it equally.',
                         steps=['The old total is 50. Adding {c} to each of 5 values adds {inc}.', 'The new total is 50 + {inc}, shared between 5 values.', 'The new mean is {ans}.']),
                oracle=lambda e: W.whole(W.mean([v + e['c'] for v in D3]))),
    'T1': dict(base=dict(m=150, d=2),
               tpl=dict(vars=dict(m=[140, 145, 150, 155, 160], d=[1, 2, 3, 4]), derive=dict(m2='m+d', t4='4*m', t5='5*(m+d)'),
                        q='The mean height of 4 children is {m} cm. A fifth child joins the group and the mean height becomes {m2} cm. How tall is the fifth child? (in cm)', answer='m+5*d',
                        hint='Work out the total height of the 4 children, and then the total height of all 5.',
                        steps=['The 4 children have a total height of 4 x {m} = {t4} cm.', 'All 5 have a total of 5 x {m2} = {t5} cm.', '{t5} − {t4} = {ans}.']),
               oracle=lambda e: next(h for h in range(100, 400) if Fraction(4 * e['m'] + h, 5) == e['m'] + e['d'])),
    'T2': dict(base=dict(m=84, d=2),
               tpl=dict(vars=dict(m=[72, 75, 78, 80, 84], d=[2, 3, 4]), derive=dict(m2='m+d', t3='3*m', t4='4*(m+d)'),
                        q='Mei\'s mean score for 3 tests is {m}. What must she score in the 4th test to raise her mean to {m2}?', answer='m+4*d',
                        hint='Find the total she needs after 4 tests, and the total she has after 3.',
                        steps=['After 3 tests her total is 3 x {m} = {t3}.', 'For a mean of {m2} over 4 tests she needs 4 x {m2} = {t4}.', '{t4} − {t3} = {ans}.']),
               oracle=lambda e: next(s for s in range(1, 400) if Fraction(3 * e['m'] + s, 4) == e['m'] + e['d'])),
    'T4': dict(base=dict(n=8, m=12, d=1),
               tpl=dict(vars=dict(n=[5, 6, 8, 9], m=[10, 12, 15], d=[1, 2, 3]), derive=dict(v='m+(n+1)*d', n1='n+1', t='n*m', t2='n*m+m+(n+1)*d'),
                        q='A Scratch list holds {n} numbers with a mean of {m}. Then the number {v} is added to the list. What will the mean program say now?', answer='m+d',
                        hint='Find the total of the {n} numbers first. Add the new number, then divide by how many numbers there are now.',
                        steps=['The {n} numbers have a total of {n} x {m} = {t}.', 'Adding {v} gives {t2}, and there are {n1} numbers.', '{t2} ÷ {n1} = {ans}.']),
               oracle=lambda e: W.whole(W.mean([e['m']] * e['n'] + [e['m'] + (e['n'] + 1) * e['d']]))),
    'C3a': dict(base=dict(m=41, d=3),
                tpl=dict(vars=dict(m=[38, 40, 41, 42], d=[2, 3, 4]), derive=dict(m2='m+d', t8='8*m', t9='9*(m+d)'),
                         q='A group of 8 children has a mean mass of {m} kg. When their tutor joins, the mean mass of all 9 becomes {m2} kg. What is the tutor\'s mass? (in kg)', answer='m+9*d',
                         hint='Find the total mass of the 8 children and the total mass of all 9 people.',
                         steps=['The 8 children have a total mass of 8 x {m} = {t8} kg.', 'All 9 people have a total mass of 9 x {m2} = {t9} kg.', '{t9} − {t8} = {ans}.']),
                oracle=lambda e: next(t for t in range(1, 400) if Fraction(8 * e['m'] + t, 9) == e['m'] + e['d'])),
    'Xa': dict(base=dict(m=9, x=5, y=12),
               tpl=dict(vars=dict(m=[8, 9, 10, 11, 12], x=[4, 5, 6, 7], y=[10, 12, 13, 14]), derive=dict(tot='3*m', known='x+y'),
                        q='The mean of 3 numbers is {m}. Two of them are {x} and {y}. What is the third number?', answer='3*m-x-y',
                        hint='Find the total of the 3 numbers first. Then take away the two you know.',
                        steps=['The total of the 3 numbers is 3 x {m} = {tot}.', '{x} + {y} = {known}.', '{tot} − {known} = {ans}.']),
               oracle=lambda e: next(s for s in range(1, 300) if W.mean([e['x'], e['y'], s]) == e['m'])),
}
