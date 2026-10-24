"""Online practice for Level 6 (Primary 6, ages 11-13) holiday lesson 3: Below Zero (negative numbers; a sprite on a number line; variables below 0).

The questions are the ones printed in the Level 6 holiday workbook (p6/content/l3.js workbook(): Start here Q1 to Q7; the Finish page: the Investigation
(p6/content/gaps.json lesson 3) and the exit slip (l3.js lesson.exit); Think harder = the first four l3.js qbank.stretch questions; Go further = the last three
l3.js qbank.challenge questions).  Every answer is recomputed by an INDEPENDENT checker below (loops and comparisons on the numbers in the question, or the block-program
interpreter w2lib.run for the code questions; never a copy of the printed answer).  build_holiday.py stops if a checker and the printed answer differ.
Scratch is not run in the page: the code is drawn as blocks (the workbook's own drawing) and traced on paper or in the head.
"""
import os, sys
HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE_, '..'))
sys.path.insert(0, os.path.join(HERE_, '..', '..'))
from hlib import *      # noqa: E402,F401
import p6lib as P       # noqa: E402
import w2lib as W       # noqa: E402

M = W.MINUS
META = dict(level=6, lesson=3, key='p6', title='Below Zero', workbook_title='BELOW ZERO', topic='Negative Numbers', strand='Number',
            sources=['p6/content/l3.js', 'p6/content/gaps.json'],
            intro=['You do not need Scratch on this page. The code is drawn as blocks: read it, trace it on paper or in your head, and type what the sprite says.',
                   'For a number below zero, type a minus sign in front (for example -4). The minus key on your keyboard is fine.',
                   'Draw a number line on paper if it helps: right is bigger, left is smaller.'])
NU, CO = 'Number', 'Coding and number'

# ---------------------------------------------------------------- data and programs (as drawn in the workbook)
MARKS = {'A': -8, 'B': -3, 'C': 4}
LIST1B = [3, -5, 0, -1, -12, 7]
HARBIN = [('6 a.m.', -24), ('9 a.m.', -19), ('12 noon', -13), ('3 p.m.', -11), ('9 p.m.', -20)]
GULL, DIVER, CRAB = 9, -6, -15
SG_NOON = 31

HAT = [0, 'event', 'when green flag clicked']
TRACE = [HAT, [0, 'motion', 'set x to [40]'], [0, 'control', 'repeat [4]'], [1, 'motion', 'change x by [-30]'], [0, 'looks', 'say [x position]']]
LIFT = [HAT, [0, 'var', 'set floor to [5]'], [0, 'control', 'repeat [8]'], [1, 'var', 'change floor by [1]'], [1, 'looks', 'say [floor] for [1] seconds']]
LIFT_FIX = lambda k: [HAT, [0, 'var', 'set floor to [5]'], [0, 'control', 'repeat [8]'], [1, 'var', f'change floor by [{k}]'], [1, 'looks', 'say [floor] for [1] seconds']]
DIVER_PLAN = [HAT, [0, 'var', 'set depth to [      ]'], [0, 'control', 'repeat [      ]'], [1, 'var', 'change depth by [      ]'], [1, 'looks', 'say [depth] for [1] seconds']]
SUB_PROG = lambda n0, r, k: [HAT, [0, 'var', f'set n to [{n0}]'], [0, 'control', f'repeat [{r}]'], [1, 'var', f'change n by [{k}]'], [0, 'looks', 'say [n]']]


def code(prog, label):
    return W.blocks(W.show(prog), label, 17)


def harbin_fig():
    return W.table_svg(['Time', 'Temperature'], [[t, f'{W.neg(v)} °C'] for t, v in HARBIN], 'Mei\'s temperatures in Harbin: 6 a.m. minus 24, 9 a.m. minus 19, 12 noon minus 13, 3 p.m. minus 11, 9 p.m. minus 20 degrees Celsius', [118, 140], 17, 34)


def sea_fig():
    return W.vertical_line(-17, 12, 5, [(GULL, f'seagull: {GULL} m', 'gull'), (DIVER, f'diver: {M}{-DIVER} m', 'diver'), (CRAB, f'crab: {M}{-CRAB} m', 'crab')],
                           'Sea-level picture: a seagull at 9 metres, a diver at minus 6 metres and a crab at minus 15 metres, with sea level at 0', sc=9, width=310)


def blank_line():
    return W.number_line(-12, 12, label_every=4, sp=13, label='Blank number line from minus 12 to 12 to picture the jumps on', height=22)


def seagull_line():
    return W.vertical_line(-15, 10, 5, [(9, 'seagull: 9 m', 'gull'), (-14, f'diver: {M}14 m', 'diver')],
                           'A vertical number line in metres from minus 15 to 10: a seagull at 9, sea level at 0 and a diver at minus 14', sc=9, width=310)


def in_seq_levels():
    return [4, 3, 2, 1, 'B1', 'B2', 'B3']


def evalx(s):
    return eval(s.replace(M, '-'))


ITEMS = [
    # ================= Start here (workbook Lesson 3, Q1 to Q7)
    dict(id='1a', tier='core', no='1(a)', type='fields', strand=NU, skill='reading a number line',
         q='The number line. Numbers get bigger to the right. Read the number at each letter.',
         frame='A = {f1};   B = {f2};   C = {f3}', answer=[-8, -3, 4], check=lambda: [MARKS['A'], MARKS['B'], MARKS['C']],
         svg=W.number_line(-10, 10, [(v, k) for k, v in MARKS.items()], 2, 16, 'Number line from minus 10 to 10 with every second number labelled, and points A, B and C'),
         hint='Only every second number has a label. Find the nearest label, then count the small marks. Left of 0 the numbers have a minus sign.',
         steps=[f'A is on the label {M}8.', f'B is one mark to the right of the label {M}4, or one mark to the left of {M}2: it is {M}3.', 'C is four marks to the right of 0: it is 4.'],
         src=['Write the number at each letter.']),
    dict(id='1b', tier='core', no='1(b)', type='set', ordered=True, strand=NU, skill='ordering negative numbers',
         q=f'Put these numbers in order, smallest first: 3, {M}5, 0, {M}1, {M}12, 7. Type them with a comma between.',
         answer=[-12, -5, -1, 0, 3, 7], check=lambda: sorted(LIST1B),
         hint='The smallest number is the one furthest to the left on the number line. Which of these is furthest left?',
         steps=[f'On the number line, left is smaller. Numbers below zero come first. Of the negatives, {M}12 is furthest left, then {M}5, then {M}1.', f'Then 0, then the positive numbers 3 and 7.', f'The order is {M}12, {M}5, {M}1, 0, 3, 7.'],
         src=['Smallest first:']),
    dict(id='1c1', tier='core', no='1(c1)', type='choice', strand=NU, skill='comparing negative numbers', options=['<', '>'], answer='>',
         q=f'Which sign goes in the gap? {M}4 ____ {M}9 ("<" means is less than, ">" means is greater than)', check=lambda: '>' if -4 > -9 else '<',
         hint='Picture both numbers on a number line. The one further to the right is greater.',
         steps=[f'{M}4 is to the right of {M}9 on the number line.', f'The number on the right is greater, so {M}4 > {M}9.', f'(It is warmer at {M}4 degrees than at {M}9 degrees.)'],
         src=['Write < or > in each gap.']),
    dict(id='1c2', tier='core', no='1(c2)', type='choice', strand=NU, skill='comparing negative numbers', options=['<', '>'], answer='<',
         q=f'Which sign goes in the gap? {M}1 ____ 0 ("<" means is less than, ">" means is greater than)', check=lambda: '>' if -1 > 0 else '<',
         hint='Which is further to the right on the number line: the number just below zero, or zero itself?',
         steps=[f'{M}1 is one step to the left of 0.', f'The number on the left is smaller, so {M}1 < 0.'],
         src=['Write < or > in each gap.']),
    dict(id='1c3', tier='core', no='1(c3)', type='choice', strand=NU, skill='comparing negative numbers', options=['<', '>'], answer='<',
         q=f'Which sign goes in the gap? {M}15 ____ 2 ("<" means is less than, ">" means is greater than)', check=lambda: '>' if -15 > 2 else '<',
         hint='A number below zero and a number above zero: which one is on the left of the other?',
         steps=[f'{M}15 is below zero and 2 is above zero.', f'Every number below zero is to the left of every number above zero, so {M}15 < 2.'],
         src=['Write < or > in each gap.']),

    dict(id='2a', tier='core', no='2(a)', type='choice', strand=NU, skill='reading a table of temperatures', options=[t for t, _ in HARBIN], answer='3 p.m.',
         q='On a December trip to Harbin, China, Mei wrote down the temperature (see the table). At which time was it warmest?', svg=harbin_fig(),
         check=lambda: max(HARBIN, key=lambda r: r[1])[0],
         hint='Warmest is the temperature furthest to the right on a number line. Which of the five is furthest right?',
         steps=[f'On a number line, the warmest temperature is the one furthest right.', f'The temperatures are {M}24, {M}19, {M}13, {M}11 and {M}20. The furthest right is {M}11.', f'{M}11 °C was at 3 p.m.'],
         src=['At which time was it warmest?']),
    dict(id='2b', tier='core', no='2(b)', type='number', strand=NU, skill='difference of two temperatures', answer=11, svg=harbin_fig(),
         q='Mei\'s temperatures in Harbin (see the table). How many degrees did it rise from 6 a.m. to 12 noon?',
         check=lambda: dict(HARBIN)['12 noon'] - dict(HARBIN)['6 a.m.'],
         hint='Picture a number line. How many steps is it from the 6 a.m. temperature up to the 12 noon temperature?',
         steps=[f'From {M}24 up to {M}13 on the number line.', f'{M}24 up to {M}14 is 10 steps, then one more step to {M}13: 11 steps.', 'It rose 11 degrees. (Check: -24 + 11 = -13.)'],
         src=['How many degrees did it rise from 6 a.m. to 12 noon?']),
    dict(id='2c', tier='core', no='2(c)', type='number', strand=NU, skill='difference of two temperatures', answer=9, svg=harbin_fig(),
         q='Mei\'s temperatures in Harbin (see the table). How many degrees did it fall from 3 p.m. to 9 p.m.?',
         check=lambda: dict(HARBIN)['3 p.m.'] - dict(HARBIN)['9 p.m.'],
         hint='Picture a number line. How many steps down is it from the 3 p.m. temperature to the 9 p.m. temperature?',
         steps=[f'From {M}11 down to {M}20 on the number line.', f'{M}11 down to {M}20 is 9 steps.', 'It fell 9 degrees. (Check: -11 - 9 = -20.)'],
         src=['How many degrees did it fall from 3 p.m. to 9 p.m.?']),
    dict(id='2d', tier='core', no='2(d)', type='number', strand=NU, skill='temperature change', answer=-25, svg=harbin_fig(),
         q='Mei\'s temperatures in Harbin (see the table). Midnight was 5 degrees colder than 9 p.m. What was the temperature at midnight? (in degrees Celsius)',
         check=lambda: dict(HARBIN)['9 p.m.'] - 5,
         hint='Colder means moving to the left on the number line. Start at the 9 p.m. temperature.',
         steps=[f'9 p.m. was {M}20 °C.', f'5 degrees colder is 5 steps to the left: {M}20 - 5 = {M}25.', f'Midnight was {M}25 °C.'],
         src=['Midnight was 5 degrees colder than 9 p.m.']),
    dict(id='2e', tier='core', no='2(e)', type='number', strand=NU, skill='difference across zero', answer=44, svg=harbin_fig(),
         q='Mei\'s temperatures in Harbin (see the table). At 12 noon Singapore was 31 °C. How many degrees warmer was Singapore than Harbin?',
         check=lambda: SG_NOON - dict(HARBIN)['12 noon'],
         hint='The two temperatures are on different sides of 0. How far is Harbin below 0? How far is Singapore above 0?',
         steps=[f'Harbin at noon: {M}13 °C. Singapore: 31 °C.', f'From {M}13 up to 0 is 13 degrees, then 31 more to reach 31.', '13 + 31 = 44. Singapore was 44 degrees warmer.'],
         src=['At noon Singapore was 31']),

    dict(id='3a', tier='core', no='3(a)', type='number', strand=NU, skill='height above and below sea level', answer=15, svg=sea_fig(),
         q='Heights above sea level are positive. Heights below sea level are negative. How many metres above the diver is the seagull?',
         check=lambda: GULL - DIVER,
         hint='The diver is below sea level and the seagull is above. How far is the diver from sea level, and how far is sea level from the seagull?',
         steps=[f'The diver is at {M}6 m, so she is 6 m below sea level.', 'The seagull is 9 m above sea level.', '6 + 9 = 15. The seagull is 15 m above the diver.'],
         src=['Heights above sea level are positive.']),
    dict(id='3b', tier='core', no='3(b)', type='number', strand=NU, skill='height above and below sea level', answer=9, svg=sea_fig(),
         q='Heights above sea level are positive. Heights below sea level are negative. How many metres below the diver is the crab?',
         check=lambda: DIVER - CRAB,
         hint='Both are below sea level. How many metres further down is the crab than the diver?',
         steps=[f'The diver is at {M}6 m and the crab is at {M}15 m.', f'From {M}6 down to {M}15 is 9 m.', 'The crab is 9 m below the diver.'],
         src=['Heights above sea level are positive.']),
    dict(id='3c', tier='core', no='3(c)', type='number', strand=NU, skill='moving up and down', answer=-13, svg=sea_fig(),
         q='Heights above sea level are positive. Heights below sea level are negative. The diver swims up 4 m, then down 11 m. What is her height now? (in metres)',
         check=lambda: DIVER + 4 - 11,
         hint='Start at the diver\'s height and move one swim at a time. Up means the number gets bigger, down means it gets smaller.',
         steps=[f'She starts at {M}6 m.', f'Up 4 m: {M}6 + 4 = {M}2 m.', f'Down 11 m: {M}2 - 11 = {M}13 m.', f'Her height now is {M}13 m (13 m below sea level).'],
         src=['Heights above sea level are positive.']),

    dict(id='4a', tier='core', no='4(a)', type='number', strand=NU, skill='adding across zero', answer=3, svg=blank_line(),
         q=f'Work this out. Picture the jumps on a number line (or draw it on paper). {M}6 + 9 = ?', check=lambda: evalx('-6 + 9'),
         hint=f'Start at {M}6 and move 9 steps to the right. How many steps take you to 0? How many are left after that?',
         steps=[f'Start at {M}6. Move right 6 steps to reach 0.', 'There are 9 - 6 = 3 more steps to the right.', f'{M}6 + 9 = 3.'],
         src=['Work these out.']),
    dict(id='4b', tier='core', no='4(b)', type='number', strand=NU, skill='subtracting across zero', answer=-7, svg=blank_line(),
         q=f'Work this out. Picture the jumps on a number line (or draw it on paper). 4 {M} 11 = ?', check=lambda: evalx('4 - 11'),
         hint='Start at 4 and move 11 steps to the left. How many steps take you to 0? How many are left after that?',
         steps=['Start at 4. Move left 4 steps to reach 0.', f'There are 11 - 4 = 7 more steps to the left, so you land below zero.', f'4 {M} 11 = {M}7.'],
         src=['Work these out.']),
    dict(id='4c', tier='core', no='4(c)', type='number', strand=NU, skill='subtracting from a negative', answer=-8, svg=blank_line(),
         q=f'Work this out. Picture the jumps on a number line (or draw it on paper). {M}3 {M} 5 = ?', check=lambda: evalx('-3 - 5'),
         hint=f'Start at {M}3. Take away 5 means move 5 steps to the left.',
         steps=[f'Start at {M}3 and move 5 steps to the left.', f'{M}3 {M} 5 = {M}8.'],
         src=['Work these out.']),
    dict(id='4d', tier='core', no='4(d)', type='number', strand=NU, skill='adding a negative number', answer=-8, svg=blank_line(),
         q=f'Work this out. Picture the jumps on a number line (or draw it on paper). {M}2 + ({M}6) = ?', check=lambda: evalx('-2 + (-6)'),
         hint='Adding a negative number moves you to the left. How many steps left, starting from the first number?',
         steps=[f'Adding {M}6 means moving 6 steps to the left.', f'Start at {M}2 and move 6 steps left: {M}8.', f'{M}2 + ({M}6) = {M}8.'],
         src=['Work these out.']),
    dict(id='4e', tier='core', no='4(e)', type='number', strand=NU, skill='subtracting a negative number', answer=8, svg=blank_line(),
         q=f'Work this out. Picture the jumps on a number line (or draw it on paper). 5 {M} ({M}3) = ?', check=lambda: evalx('5 - (-3)'),
         hint=f'5 {M} ({M}3) asks: how far is it from {M}3 up to 5? Split the journey at 0.',
         steps=[f'5 {M} ({M}3) is the jump from {M}3 to 5.', f'From {M}3 up to 0 is 3 steps, then 5 more steps to reach 5: 8 steps.', f'5 {M} ({M}3) = 8. (Check: {M}3 + 8 = 5.)'],
         src=['Work these out.']),
    dict(id='4f', tier='core', no='4(f)', type='number', strand=NU, skill='subtracting a negative number', answer=6, svg=blank_line(),
         q=f'Work this out. Picture the jumps on a number line (or draw it on paper). {M}1 {M} ({M}7) = ?', check=lambda: evalx('-1 - (-7)'),
         hint=f'{M}1 {M} ({M}7) asks: how far is it from {M}7 up to {M}1?',
         steps=[f'{M}1 {M} ({M}7) is the jump from {M}7 to {M}1.', f'From {M}7 up to {M}1 is 6 steps to the right.', f'{M}1 {M} ({M}7) = 6. (Check: {M}7 + 6 = {M}1.)'],
         src=['Work these out.']),

    dict(id='5-trace', tier='core', no='5 table', type='fields', strand=CO, skill='tracing code with negative numbers',
         q='Trace the code. Fill in the table: the value of x after each repeat (x starts at 40).', frame='x after repeat 1: {f1};   repeat 2: {f2};   repeat 3: {f3};   repeat 4: {f4}',
         answer=[10, -20, -50, -80], svg=code(TRACE, 'Code: set x to 40, repeat 4: change x by minus 30, then say x position'),
         check=lambda: [W.run([HAT, [0, 'motion', 'set x to [40]'], [0, 'control', f'repeat [{k}]'], [1, 'motion', 'change x by [-30]']])[1]['x'] for k in (1, 2, 3, 4)],
         hint='x starts at 40. Each repeat adds a negative number, so x moves to the left.',
         steps=['Start: x = 40.', f'Repeat 1: 40 + ({M}30) = 10. Repeat 2: 10 {M} 30 = {M}20. Repeat 3: {M}20 {M} 30 = {M}50. Repeat 4: {M}50 {M} 30 = {M}80.', f'The table reads 10, {M}20, {M}50, {M}80.'],
         src=['Trace the code. Fill in the table to show x after each repeat.']),
    dict(id='5a', tier='core', no='5(a)', type='number', strand=CO, skill='tracing code with negative numbers', answer=-80,
         svg=code(TRACE, 'Code: set x to 40, repeat 4: change x by minus 30, then say x position'),
         q='Trace the code. What does the sprite say at the end?', check=lambda: W.run(TRACE)[0][-1],
         hint='Look where the "say" block is: inside the loop or after it? Then use the value of x after the last repeat.',
         steps=['The "say" block is after the loop, so the sprite says x once, after all 4 repeats.', f'After 4 repeats x = {M}80.', f'The sprite says {M}80.'],
         src=['What does it say at the end?']),
    dict(id='5b', tier='core', no='5(b)', type='number', strand=CO, skill='tracing code with negative numbers', answer=4,
         svg=code(TRACE, 'Code: set x to 40, repeat 4: change x by minus 30, then say x position'),
         q=f'How many MORE repeats would take it to x = {M}200?',
         check=lambda: (lambda x0: next(k for k in range(1, 200) if x0 - 30 * k == -200))(W.run(TRACE)[1]['x']),
         hint='Start from where x is after the 4 repeats. How far is that from the target? How far does one repeat move x?',
         steps=[f'After 4 repeats x = {M}80. The target is {M}200.', f'From {M}80 down to {M}200 is 120.', 'Each repeat moves 30, so 120 ÷ 30 = 4 more repeats.'],
         src=['How many MORE repeats would']),

    dict(id='6a', tier='core', no='6(a)', type='number', strand=CO, skill='finding a bug', answer=13, svg=code(LIFT, 'Siti\'s code: set floor to 5, repeat 8: change floor by 1, say floor'),
         q='Find the bug. Siti wants the lift to go DOWN 8 floors from floor 5 (0 = ground floor). Her code is shown. What is the last floor her code says?',
         check=lambda: W.run(LIFT)[0][-1],
         hint='Trace the code: floor starts at 5 and the loop runs 8 times.',
         steps=['Floor starts at 5. Each repeat adds 1.', '8 repeats add 8: 5 + 8 = 13.', 'Her code says 13 last: the lift goes UP, not down.'],
         src=['Her code says this floor last:']),
    dict(id='6b', tier='core', no='6(b)', type='number', strand=CO, skill='finding a bug', answer=-1, svg=code(LIFT, 'Siti\'s code: set floor to 5, repeat 8: change floor by 1, say floor'),
         q='Siti\'s lift must go DOWN 8 floors from floor 5. Change ONE block so that it does. Which number should go in the block "change floor by ( )"?',
         check=lambda: next(k for k in range(-5, 6) if k and W.run(LIFT_FIX(k))[0][-1] == 5 - 8),
         hint='Going down means the floor number gets smaller each repeat. What do you add to make a number smaller?',
         steps=['The lift must go down 1 floor each repeat, so the block must make the floor number smaller by 1.', f'Change floor by {M}1.', f'Check: 5 + 8 × ({M}1) = {M}3, and the lift has gone down 8 floors.'],
         src=['Change ONE block so the lift']),
    dict(id='6c', tier='core', no='6(c)', type='fields', strand=CO, skill='negative floors', answer=[-3, 3],
         q=f'Siti fixes her code so that the lift goes DOWN 8 floors from floor 5 (0 = ground floor). Now what is the last floor it says, and which basement is that? (Floor {M}1 is basement 1, floor {M}2 is basement 2, and so on. Type the basement number only.)',
         frame='The last floor it says is {f1}.   That is basement number {f2}.',
         check=lambda: (lambda f: [f, -f])(W.run(LIFT_FIX(-1))[0][-1]),
         hint='Go down 8 floors from floor 5, one floor at a time, and see where you end up. Then match the floor number to its basement.',
         steps=[f'The lift starts at 5 and goes down 1 floor 8 times: 5 {M} 8 = {M}3.', f'The last floor it says is {M}3.', f'Floor {M}3 is the third basement (B3).'],
         src=['Now the last floor it says is']),

    dict(id='7a', tier='core', no='7(a)', type='fields', strand=CO, skill='planning a loop', answer=[0, 7, -4],
         q='Plan your code. A diver starts at sea level (0 m) and goes down 4 m at a time to reach the depth of -28 m (28 m below sea level). Fill in the three blanks of the plan.'.replace('-28', M + '28'),
         frame='set depth to {f1};   repeat {f2};   change depth by {f3}', svg=code(DIVER_PLAN, 'Plan with three blanks: set depth to blank, repeat blank, change depth by blank, say depth'),
         check=lambda: (lambda hits: [0, hits[0], -4] if len(hits) == 1 else None)([r for r in range(1, 40) if W.run(W.fill(DIVER_PLAN, [0, r, -4]))[1]['depth'] == -28]),
         hint='She starts at sea level. How many jumps of 4 m does it take to go from 0 m down to 28 m below?',
         steps=['She starts at sea level, so set depth to 0.', f'Each step down is 4 m, so change depth by {M}4.', f'{M}28 is 28 m below 0, and 28 ÷ 4 = 7, so repeat 7.', f'Check: 7 repeats of {M}4 give {M}28.'],
         src=['Plan your code.']),
    dict(id='7b', tier='core', no='7(b)', type='number', strand=CO, skill='undoing a change', answer=28,
         q=f'After the loop the diver is at {M}28 m. Add one more block: "change depth by ( )". What number brings her back to 0 m?',
         check=lambda: next(k for k in range(-60, 61) if -28 + k == 0),
         hint='She is below 0. Which number do you add to get from her depth up to 0?',
         steps=[f'She is at {M}28 m.', f'To get back to 0 you need to go up 28 m: {M}28 + 28 = 0.', 'The block is "change depth by 28".'],
         src=['After the loop she is at']),

    # ---- exit slip (printed on the Finish page)
    dict(id='X', tier='core', no='Exit slip', type='number', strand=NU, skill='rises and falls across zero', answer=-5,
         q='It is -3 °C. The temperature falls 6 degrees, then rises 4 degrees. What is the temperature now? (in degrees Celsius)'.replace('-3', M + '3'),
         check=lambda: -3 - 6 + 4,
         hint='Move one change at a time on a number line: a fall moves left, a rise moves right.',
         steps=[f'Start at {M}3 °C. A fall of 6 degrees: {M}3 {M} 6 = {M}9.', f'A rise of 4 degrees: {M}9 + 4 = {M}5.', f'The temperature now is {M}5 °C.'],
         src=['It is', 'The temperature falls 6 degrees, then rises 4 degrees.']),

    # ================= Investigation (printed on the Finish page)
    dict(id='I1', tier='invest', no='Investigation', type='selfcheck', paper=True, strand=NU, skill='differences as distances',
         q=f'Find all the pairs. Here are some numbers: {M}5, {M}3, {M}1, 0, 2, 4, 6. Find ALL the pairs (a, b) from the list with a {M} b = 7. Mark each pair on a number line. What do you notice? Then try again with a {M} b = 3. First step: draw a number line from {M}5 to 6. Pick a = 2 and ask: what number b makes 2 {M} b = 7?',
         facts={7: [(2, -5), (4, -3), (6, -1)], 3: [(0, -3), (2, -1)]},
         check=lambda: {d: [(a, b) for a in (-5, -3, -1, 0, 2, 4, 6) for b in (-5, -3, -1, 0, 2, 4, 6) if a - b == d] for d in (7, 3)},
         sol_fig=lambda f: W.hop_lines(-5, 6, [(f'a {M} b = 7', [(b, a) for a, b in f[7]]), (f'a {M} b = 3', [(b, a) for a, b in f[3]])],
                                       'Number lines from minus 5 to 6. For a minus b equals 7 the pairs are 2 and minus 5, 4 and minus 3, 6 and minus 1. For a minus b equals 3 the pairs are 0 and minus 3, 2 and minus 1.'),
         hint='Take each b in turn and ask what a would be (a = 7 + b). Then check that a is on the list.',
         steps=[f'a {M} b = 7: the pairs are (2, {M}5), (4, {M}3) and (6, {M}1). That is exactly three pairs.', f'a {M} b = 3: the pairs are (0, {M}3) and (2, {M}1). That is two pairs.',
                'What stays the same: in each pair the gap between a and b is the same distance (7, or 3): the same jump slid along the line.',
                'A good answer searches in order (each b, then the a it needs), checks that a is on the list, and draws the jump on a number line. (7, 0) is not allowed: 7 is not on the list.'],
         src=['Open investigation', 'Find ALL the pairs']),

    # ================= Think harder (first four Think harder questions of the workbook)
    dict(id='T1', tier='stretch', no='T1', type='fields', strand=NU, skill='adding and subtracting across zero', answer=[5, -8],
         q='Work out both.', frame=f'{M}7 + 12 = {{f1}};   5 {M} 13 = {{f2}}', check=lambda: [evalx('-7 + 12'), evalx('5 - 13')],
         hint=f'For each one, start at the first number and move along the number line. Split the move at 0.',
         steps=[f'{M}7 + 12: from {M}7 up to 0 is 7, then 5 more: 5.', f'5 {M} 13: from 5 down to 0 is 5, then 8 more below zero: {M}8.', f'The answers are 5 and {M}8.'],
         src=['Work out −7 + 12 and 5 − 13.']),
    dict(id='T2', tier='stretch', no='T2', type='number', strand=NU, skill='distance across sea level', answer=23, svg=seagull_line(),
         q=f'A diver is at {M}14 m. A seagull is flying at 9 m. How far apart are they? (in metres)', check=lambda: 9 - (-14),
         hint='They are on opposite sides of sea level. How far is each one from sea level?',
         steps=[f'The diver is 14 m below sea level and the seagull is 9 m above it.', '14 + 9 = 23.', 'They are 23 m apart.'],
         src=['A diver is at']),
    dict(id='T3', tier='stretch', no='T3', type='number', strand=NU, skill='subtracting a negative number', answer=10,
         q=f'Work out 4 {M} ({M}6). Hint: how far is it from {M}6 to 4?', check=lambda: evalx('4 - (-6)'),
         hint='Count the steps from the smaller number up to the bigger one. Go to 0 first.',
         steps=[f'4 {M} ({M}6) is the jump from {M}6 to 4.', f'From {M}6 up to 0 is 6, then 4 more: 10.', f'4 {M} ({M}6) = 10. (Check: {M}6 + 10 = 4.)'],
         src=['Work out 4']),
    dict(id='T4', tier='stretch', no='T4', type='number', strand=NU, skill='finding a missing number', answer=-7,
         q=f'Find the missing number: {M}3 + ____ = {M}10.', check=lambda: next(k for k in range(-30, 30) if -3 + k == -10),
         hint=f'Do you need to move left or right to get from {M}3 to {M}10? How many steps?',
         steps=[f'To get from {M}3 to {M}10 you move left. The distance is 7.', f'Moving 7 to the left means adding {M}7.', f'{M}3 + ({M}7) = {M}10.'],
         src=['Find the missing number']),

    # ================= Go further (last three Go further questions of the workbook)
    dict(id='C1', tier='challenge', no='C1', type='selfcheck', marking_mode='open', strand=NU, skill='making up a temperature story',
         q=f'Make up your own temperature story with at least three changes (rises and falls) that starts below zero and ends at exactly {M}7 °C. Write the story and the working, and sketch a number line. Swap with a partner and check each other\'s.',
         facts=dict(start=-2, changes=[-6, 3, -2], end=-7), check=lambda: dict(start=-2, changes=[-6, 3, -2], end=-2 + sum([-6, 3, -2])),
         hint='Choose a start below zero. Pick your last change so the answer comes out exactly. Or work backwards from the end.',
         steps=[f'Open question. One example: it starts at {M}2 °C, falls 6 degrees ({M}8), rises 3 degrees ({M}5) and falls 2 degrees ({M}7).', f'Check the story really ends at {M}7 and show each change on a number line.',
                f'Another way to build one: start at {M}7 and undo each change, going backwards.'],
         src=['Make up your own temperature story']),
    dict(id='C2', tier='challenge', no='C2', type='set', strand=NU, skill='sum and difference of two numbers', answer=[-6, 4],
         q=f'Two numbers add up to {M}2. Their difference is 10. What are the two numbers? Type both, with a comma between.',
         check=lambda: sorted(next((a, b) for a in range(-30, 31) for b in range(-30, 31) if a + b == -2 and a - b == 10)),
         hint='Pick two numbers that are 10 apart and find their sum. How must you move both of them to make the sum smaller?',
         steps=[f'Two numbers 10 apart that balance around 0 are 5 and {M}5, and their sum is 0. Moving both numbers 1 to the left lowers the sum by 2.', f'So the numbers are 4 and {M}6: they are 10 apart, and 4 + ({M}6) = {M}2.', f'The numbers are 4 and {M}6. (Check: 4 {M} ({M}6) = 10.)'],
         src=['Two numbers add up to']),
    dict(id='C3', tier='challenge', no='C3', type='number', strand=NU, skill='counting levels without a zero', answer=6,
         q=f'In some Singapore buildings there is no level 0: level 1 is the ground floor and B1 is the level below it. A lift goes from level 4 down to B3. How many floors does it go down? (Count the levels one by one; do not use a number line with 0.)',
         check=lambda: len(in_seq_levels()) - 1,
         hint='List the levels in order from 4 down to B3 and count the moves between them.',
         steps=['The levels in order are 4, 3, 2, 1, B1, B2, B3.', 'Count the moves between them: 6 moves down.', 'A number line with 0 would give 7, because it counts a level 0 that these buildings do not have.'],
         src=['In some Singapore buildings there is no level 0.']),
]

for _it in ITEMS:
    if _it.get('frame'):
        _it['frame'] = W.nb(_it['frame'])

# ---------------------------------------------------------------- variant families (every combination is run against an independent oracle at build time)
_UNIT = {'2b': ' (Type the number of degrees.)', '2c': ' (Type the number of degrees.)', '2e': ' (Type the number of degrees.)'}
for _it in ITEMS:
    if _it['id'] in _UNIT:
        _it['q'] += _UNIT[_it['id']]
    elif _it['id'] in ('2d', 'X'):
        _it['q'] = _it['q'].replace(' (in degrees Celsius)', '') + ' (Type the temperature in degrees Celsius, as a number only. Use a minus sign if it is below zero.)'
P.finish(ITEMS)

VARIANTS = {
    '4a': dict(base=dict(a=6, b=9),
               tpl=dict(vars=dict(a=[2, 3, 4, 5, 6, 7, 8, 9], b=[10, 11, 12, 13, 14, 15, 16]),
                        q=f'Work this out. Picture the jumps on a number line. {M}{{a}} + {{b}} = ?', answer='b-a',
                        hint=f'Start at {M}{{a}} and move {{b}} steps to the right. How many steps take you to 0?',
                        steps=[f'Start at {M}{{a}}. Move right {{a}} steps to reach 0.', 'The rest of the {b} steps are after 0: {b} - {a}.', 'The answer is {ans}.']),
               oracle=lambda e: eval(f"-{e['a']} + {e['b']}")),
    '4e': dict(base=dict(a=5, b=3),
               tpl=dict(vars=dict(a=[2, 3, 4, 5, 6, 7, 8, 9], b=[2, 3, 4, 5, 6, 7, 8, 9]),
                        q=f'Work this out. Picture the jump on a number line. {{a}} {M} ({M}{{b}}) = ?', answer='a+b',
                        hint=f'{{a}} {M} ({M}{{b}}) asks: how far is it from {M}{{b}} up to {{a}}? Split the journey at 0.',
                        steps=[f'{{a}} {M} ({M}{{b}}) is the jump from {M}{{b}} up to {{a}}.', 'From {b} below zero up to 0 is {b}, then {a} more: {a} + {b}.', 'The answer is {ans}.']),
               oracle=lambda e: eval(f"{e['a']} - (-{e['b']})")),
    'T2': dict(base=dict(a=14, b=9),
               tpl=dict(vars=dict(a=[6, 8, 10, 12, 14, 16, 18, 20], b=[5, 7, 9, 11, 13, 15]),
                        q=f'A diver is at {M}{{a}} m. A seagull is flying at {{b}} m. How far apart are they? (in metres)', answer='a+b',
                        hint='They are on opposite sides of sea level. How far is each one from sea level?',
                        steps=['The diver is {a} m below sea level and the seagull is {b} m above it.', '{a} + {b} = {ans}.']),
               oracle=lambda e: abs(e['b'] - (-e['a']))),
}

# ---- inquiry habit (docs/pedagogy/inquiry_skills_explicit.md; levels/habits.json)
ITEMS.insert(max(i for i, x in enumerate(ITEMS) if x['tier'] == 'core') + 1, habit_item('Try',
    'Predict first: is 3 - 5 above zero or below zero? Then test it on a number line. What happens?',
    ['Start at 3 and move 5 steps down the number line: 3, 2, 1, 0, -1, -2.', '3 - 5 = -2, which is below zero. If my prediction was different, that is useful: testing shows what really happens.'],
    'Draw a number line. Start at 3 and move down 5 steps.'))
