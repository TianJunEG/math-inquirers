from lib import *

u = Unit(9, 'Measure it, pay it', 'Length, mass, volume, money and time',
         'I can change units, solve money problems and find how long things last.')


def seg(w, t='', style='plain'):
    return {'w': w, 't': t, 'style': style}


u.learn(
    'Use one unit before you add or take away. 1 m = 100 cm, 1 kg = 1000 g, 1 ℓ = 1000 ml and $1 = 100¢.',
    {'problem': 'A ribbon is 2 m 35 cm long. Mei cuts off 80 cm. How long is the ribbon now?',
     'figure': {'type': 'l3_bars', 'rows': [{'segs': [seg(3.5, '?', 'q'), seg(1.5, '80 cm', 'ghost')], 'braces': [{'a': 0, 'b': 1, 't': '2 m 35 cm'}]}], 'width_mm': 68, 'u': 60, 'lab': 20},
     'steps': ['Change to cm: 2 m 35 cm = 235 cm.', 'Take away: 235 - 80 = 155 cm = 1 m 55 cm.'],
     'answer': 'The ribbon is 1 m 55 cm long.'},
    {'title': 'Tips',
     'steps': ['Write both amounts in the small unit first.', 'On a time line, jump to the next o’clock.']},
    {'text': 'A jug holds 2 ℓ 350 ml. Ali pours out 800 ml. The jug now holds {b} ℓ {b} ml.', 'answer': A(['1', '550'], '1 ℓ 550 ml', list=True),
     'explanation': '2 ℓ 350 ml = 2350 ml. Then 2350 - 800 = 1550 ml = 1 ℓ 550 ml. Check: 1550 + 800 = 2350.'},
    example2={'problem': 'A film starts at 2:50 pm and ends at 4:20 pm. How long is the film?',
              'figure': {'type': 'l3_timeline', 'points': [{'t': '2:50'}, {'t': '3:00'}, {'t': '4:00'}, {'t': '4:20'}], 'arcs': [{'a': 0, 'b': 1, 'text': '10 min'}, {'a': 1, 'b': 2, 'text': '1 h'}, {'a': 2, 'b': 3, 'text': '20 min'}], 'width_mm': 100},
              'steps': ['Jump to the next o’clock, then to 4:00, then to 4:20.', 'Add the jumps: 10 min + 1 h + 20 min = 1 h 30 min.'],
              'answer': 'The film is 1 h 30 min long.'})
u.u['learn']['tight'] = True

# ---------------- Start here (pages 1 to 3)
u.S(1, 'Change the units.', parts=[
    P('a', '3 m = {b} cm', A('300')), P('b', '4 kg 50 g = {b} g', A('4050')), P('c', '5 ℓ 300 ml = {b} ml', A('5300')),
    P('d', '2750 g = {b} kg {b} g', A(['2', '750'], '2 kg 750 g', list=True)), P('e', '365 cm = {b} m {b} cm', A(['3', '65'], '3 m 65 cm', list=True))],
    partsrow=True,
    why='(a) 3 × 100 = 300. (b) 4 kg = 4000 g, and 4000 + 50 = 4050. (c) 5 ℓ = 5000 ml, and 5000 + 300 = 5300. (d) 2000 g is 2 kg, and 750 g is left. (e) 300 cm is 3 m, and 65 cm is left.')
u.S(1, 'The ruler is shown at real size. Read the length of each object.', parts=[
    P('a', 'The pencil is {b} cm long.', A('8')), P('b', 'The crayon is {b} cm long.', A('7')),
    P('c', 'The pencil is {b} cm longer than the crayon.', A('1'))],
    figure={'type': 'l3_ruler', 'max': 14, 'objects': [{'label': 'pencil', 'start': 3, 'end': 11}, {'label': 'crayon', 'start': 6, 'end': 13}]},
    why='The pencil starts at 3 and ends at 11: 11 - 3 = 8 cm. The crayon starts at 6 and ends at 13: 13 - 6 = 7 cm. The pencil is 8 - 7 = 1 cm longer.')
u.S(1, 'The parcels weigh: A 1 kg 80 g, B 1900 g, C 1 kg 8 g, D 1 kg 90 g. Write the letters in order. Begin with the lightest.\n{b}  {b}  {b}  {b}',
    A(['C', 'A', 'D', 'B'], 'C, A, D, B', list=True),
    why='Write each in grams: A is 1080 g, B is 1900 g, C is 1008 g and D is 1090 g. In order: 1008, 1080, 1090, 1900. That is C, A, D, B.')
u.S(1, 'A jug has 2 ℓ 500 ml of juice. Ali pours it into cups of 400 ml.', parts=[
    P('a', 'He fills {b} cups.', A('6')), P('b', '{b} ml of juice are left over.', A('100'))],
    why='2 ℓ 500 ml = 2500 ml. 2500 ÷ 400 = 6 remainder 100. He fills 6 cups, and 100 ml are left over.')
u.S(2, 'Read the water level in each jug.', parts=[
    P('a', 'A holds {b} ml', A('350')), P('b', 'B holds {b} ml', A('600')), P('c', 'C holds {b} ml', A('850')),
    P('d', 'C has {b} ml more than A', A('500'))],
    figure={'type': 'l3_jug', 'jugs': [{'level': 350, 'label': 'A'}, {'level': 600, 'label': 'B'}, {'level': 850, 'label': 'C'}], 'major': 200, 'minor': 50, 'width_mm': 96}, figside=True,
    why='Each small mark is 50 ml. A is 1 mark above 300: 350 ml. B is at 600 ml. C is 1 mark above 800: 850 ml. 850 - 350 = 500 ml.')
u.S(2, 'A notebook costs $2.65 and a ruler costs $1.40. Mei pays with a $5 note.', parts=[
    P('a', 'They cost ${bw} in all.', A('4.05')), P('b', 'Her change is ${bw}.', A('0.95'))],
    why='(a) 2.65 + 1.40 = 4.05. (b) 5.00 - 4.05 = 0.95. Check: 4.05 + 0.95 = 5.00.')
u.S(2, 'Siti has $20 and buys the first 3 things on the list.', parts=[
    P('a', 'They cost ${bw} in all.', A('14.45')), P('b', 'Her change is ${bw}.', A('5.55')),
    P('c', 'Can she buy all 4 things on the list?   {circ:Yes|No}', A('Yes'))],
    figure={'type': 'l3_grid', 'head_row': True, 'cw': 118, 'ch': 42, 'fs': 26, 'width_mm': 76, 'rows': [['Book', 'Puzzle', 'Bottle', 'Stickers'], ['$6.20', '$4.85', '$3.40', '$1.75']]},
    why='(a) 6.20 + 4.85 = 11.05, and 11.05 + 3.40 = 14.45. (b) 20.00 - 14.45 = 5.55. (c) All 4 things cost 14.45 + 1.75 = 16.20, which is less than $20. So she can.')
u.S(2, '3 melons with the same mass weigh 2 kg 400 g. An apple weighs 150 g. 1 melon and 2 apples weigh {b} g.', A('1100'),
    space={'rows': ['Working:']},
    why='2 kg 400 g = 2400 g. 1 melon: 2400 ÷ 3 = 800 g. 2 apples: 2 × 150 = 300 g. Together: 800 + 300 = 1100 g.')
u.S(3, 'Write the time in the other kind of time.', parts=[
    P('a', '6:15 am = {bw}', A('06:15')), P('b', '1:40 pm = {bw}', A('13:40')), P('c', '9:05 pm = {bw}', A('21:05')),
    P('d', '16:50 = {bw} pm', A('4:50')), P('e', '20:25 = {bw} pm', A('8:25'))],
    partsrow=True,
    why='After 12 noon, add 12 to the hour for 24-hour time. (b) 1 + 12 = 13. (c) 9 + 12 = 21. For (d) and (e), take away 12: 16 - 12 = 4 and 20 - 12 = 8.')
u.S(3, 'How long does each take? Use a time line to help.', parts=[
    P('a', 'Aisha’s class: 5:25 pm to 6:40 pm. It lasts {b} h {b} min.', A(['1', '15'], '1 h 15 min', list=True)),
    P('b', 'Ben’s class starts at 3:40 pm and lasts 55 minutes. It ends at {bw}.', A('4:35 pm')),
    P('c', 'A show ends at 8:15 pm. It is 1 h 45 min long. It starts at {bw}.', A('6:30 pm'))],
    space={'rows': ['Time line:']},
    why='(a) 5:25 to 6:00 is 35 min, then 6:00 to 6:40 is 40 min. 35 + 40 = 75 min = 1 h 15 min. (b) 3:40 + 20 min = 4:00, then 35 more min = 4:35 pm. (c) 8:15 pm - 1 h = 7:15 pm, then 45 min back = 6:30 pm.')
u.S(3, 'Write the time shown on each clock.', parts=[
    P('a', 'A: {bw}', A('4:10')), P('b', 'B: {bw}', A('7:45')), P('c', 'C: {bw}', A('11:25'))],
    partsrow=True,
    figure={'type': 'l3_clock', 'clocks': [{'h': 4, 'm': 10, 'label': 'A'}, {'h': 7, 'm': 45, 'label': 'B'}, {'h': 11, 'm': 25, 'label': 'C'}], 'cols': 3, 'width_mm': 134},
    why='The short hand shows the hour and the long hand shows the minutes. A: the long hand points at 2, which is 10 minutes, and the short hand is just past 4. B: the long hand points at 9, which is 45 minutes. C: the long hand points at 5, which is 25 minutes.')

u.S(3, 'A stamp costs 65¢. Kumar buys 8 stamps.', parts=[
    P('a', 'The stamps cost ${bw}.', A('5.20')), P('b', 'He pays with a $10 note. His change is ${bw}.', A('4.80'))],
    why='(a) 8 × 65¢ = 520¢ = $5.20. (b) 10.00 - 5.20 = 4.80.')

# ---------------- Think harder
u.T('A pool has 4 swimming lessons in a row. Each lesson is 45 minutes. There is a 10 minute break between lessons. The first lesson starts at 07:30. When does the 4th lesson end? {bw}', A('11:00'),
    hint='Write the start and the end of each lesson.',
    space={'rows': ['Lesson 1:', 'Lesson 2:', '']},
    why='Lesson 1: 07:30 to 08:15. Break. Lesson 2: 08:25 to 09:10. Break. Lesson 3: 09:20 to 10:05. Break. Lesson 4: 10:15 to 11:00. The 4th lesson ends at 11:00.')
u.T('Ali starts his homework at 18:35 and stops at 20:10. He has a 15 minute break. How long does he work? {b} h {b} min', A(['1', '20'], '1 h 20 min', list=True),
    hint='Find the whole time first. Then take away the break.',
    space={'rows': ['Time line:', '']},
    why='From 18:35 to 19:00 is 25 min. From 19:00 to 20:00 is 1 h. From 20:00 to 20:10 is 10 min. The whole time is 1 h 35 min. Take away the 15 min break: 1 h 20 min.')
u.T('2 notebooks and 3 pens cost $9. A notebook costs $1.50 more than a pen.', parts=[
    P('a', 'A pen costs ${bw}.', A('1.20')), P('b', 'A notebook costs ${bw}.', A('2.70'))],
    hint='How much more do 2 notebooks cost than 2 pens?',
    space={'rows': ['Working:', '', '']},
    why='The 2 notebooks cost $3 more than 2 pens in all (2 × $1.50). Take that away: $9 - $3 = $6 for 5 pens. One pen costs $6 ÷ 5 = $1.20. A notebook costs $1.20 + $1.50 = $2.70. Check: 2 × 2.70 + 3 × 1.20 = 5.40 + 3.60 = 9.00.')

# ---------------- Go further
u.G('Beyond Level 3: A water puzzle.\nYou have a 3 ℓ jug, a 5 ℓ jug and a tap. The jugs have no marks. You want exactly 4 ℓ.', parts=[
    P('a', 'Fill the 5 ℓ jug. Pour from it into the 3 ℓ jug until full. The 5 ℓ jug has {b} ℓ left.', A('2')),
    P('b', 'Empty the 3 ℓ jug. Pour the 2 ℓ into it. Fill the 5 ℓ jug. Pour from it into the 3 ℓ jug until full. The 5 ℓ jug has {b} ℓ left.', A('4'))],
    hint='Follow each step. The jug is full when it holds 3 ℓ.',
    why='(a) The 3 ℓ jug takes 3 ℓ, so 5 - 3 = 2 ℓ are left in the 5 ℓ jug. (b) The 3 ℓ jug holds 2 ℓ and has room for 1 ℓ more. The full 5 ℓ jug gives 1 ℓ, so 5 - 1 = 4 ℓ are left. That is exactly 4 ℓ.')
u.G('Mei’s watch is 8 minutes slow.', parts=[
    P('a', 'Her watch shows 4:20 pm. The real time is {bw}.', A('4:28 pm')),
    P('b', 'A film starts at 4:45 pm. When it starts, her watch shows {bw}.', A('4:37 pm'))],
    hint='A slow watch shows an earlier time than the real time.',
    why='(a) A slow watch is behind: the real time is 8 minutes later: 4:20 pm + 8 min = 4:28 pm. (b) At the real time 4:45 pm her watch shows 8 minutes earlier: 4:37 pm.')
u.G('Write a shopping story that uses $6.40 and $2.15. The answer to your story must be $4.25.', A('4.25', 'Answers vary. Example: A book costs $6.40 and a pen costs $2.15. How much more does the book cost than the pen? The answer is $4.25.'),
    hint='Which sum or take-away of $6.40 and $2.15 gives $4.25?',
    space={'rows': ['My story:', '', 'My answer:']},
    why='Check that your story uses both amounts and gives $4.25. The only way is the difference: 6.40 - 2.15 = 4.25. A sum of the two would be $8.55.')
u.G('A night shift starts at 22:30 and lasts 8 h 45 min. At what time does it end? Write it in 24-hour time. {bw}', A('07:15'),
    hint='How long is it from 22:30 to midnight?',
    space={'rows': ['Time line:']},
    why='From 22:30 to 24:00 (midnight) is 1 h 30 min. The rest of the shift is 8 h 45 min - 1 h 30 min = 7 h 15 min after midnight. So it ends at 07:15. Check: 22:30 + 8 h = 06:30, and 45 min more is 07:15.')

# ---------------- Check yourself
u.C('2 m 40 cm = {b} cm', A('240'), why='2 m = 200 cm, and 200 + 40 = 240 cm.')
u.C('A bottle holds 1 ℓ 200 ml. A child drinks 700 ml. The bottle then holds {b} ml.', A('500'), why='1 ℓ 200 ml = 1200 ml. Then 1200 - 700 = 500 ml.')
u.C('A bus trip starts at 9:40 am and ends at 11:10 am. It lasts {b} h {b} min.', A(['1', '30'], '1 h 30 min', list=True),
    why='9:40 to 10:00 is 20 min. 10:00 to 11:00 is 1 h. 11:00 to 11:10 is 10 min. In all: 1 h 30 min.')
u.C('Kumar buys a snack for $2.35. He pays with a $5 note. His change is ${bw}.', A('2.65'), why='5.00 - 2.35 = 2.65. Check: 2.35 + 2.65 = 5.00.')
u.save()
