import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

def scales(*sc, **kw):
    d = {'type': 'l2_scale', 'scales': [{'left': l, 'right': r, 'label': lab} for lab, l, r in sc]}
    d.update(kw)
    return d

learn = {
 'intro': 'A balance that is level has the same mass on both sides. So you can swap a thing for whatever balances it. For time, count on in 5s on the clock. Count to the next hour first.',
 'example': {
  'problem': 'The scale is level. 1 melon balances 3 plums. 1 plum has a mass of 50 g. Find the mass of the melon.',
  'figure': scales(('Level', ['pear'], ['plum', 'plum', 'plum']), width_mm=70) if False else {'type': 'l2_scale', 'scales': [{'left': ['melon'], 'right': ['plum', 'plum', 'plum']}], 'width_mm': 66}, 'side': True,
  'steps': ['Level scale: the melon is as heavy as 3 plums.', '1 plum is 50 g. 3 plums are 3 × 50 g = 150 g.', 'So the melon is 150 g.', 'Check: 50 g + 50 g + 50 g = 150 g.'],
  'answer': 'The melon has a mass of 150 g.'},
 'howto': {'title': 'How to use a balance', 'steps': ['A level balance means both sides are equal.', 'Swap a thing for what balances it.', 'Write the mass of each thing.', 'Check both sides.']},
 'facts': {'title': 'Units', 'lines': ['1 kg = 1000 g.   1 m = 100 cm.', '60 minutes = 1 hour.', 'Count on in 5s to the next hour first.']},
 'try': {'text': 'One tin balances 4 pens. One pen has a mass of 25 g. Find the mass of the tin. {b} g', 'answer': A('100'),
         'explanation': 'The tin is as heavy as 4 pens. 4 × 25 g = 100 g. Check: 25 + 25 + 25 + 25 = 100.'}}

items = [
 I('start', 1, 'Read the clocks. Write each time.', figure={'type': 'l2_clock', 'clocks': [{'h': 4, 'm': 35, 'label': 'A'}, {'h': 8, 'm': 50, 'label': 'B'}, {'h': 11, 'm': 15, 'label': 'C'}], 'width_mm': 135},
   partsrow=True, parts=[P('a', 'A: {b} : {b}', ['4', '35']), P('b', 'B: {b} : {b}', ['8', '50']), P('c', 'C: {b} : {b}', ['11', '15'])],
   why='The long hand shows the minutes: count in 5s. A: long hand on 7 is 35 minutes, short hand past 4: 4:35. B: long hand on 10 is 50 minutes: 8:50. C: long hand on 3 is 15 minutes: 11:15.'),
 I('start', 1, 'Write am or pm.', partsrow=True, parts=[
   P('a', 'Mei eats breakfast at 7:30   {circ:am|pm}', 'am'), P('b', 'School ends at 1:30   {circ:am|pm}', 'pm'), P('c', 'Ali goes to bed at 9:15   {circ:am|pm}', 'pm'), P('d', 'The sun rises at 6:40   {circ:am|pm}', 'am')],
   why='am is from midnight to noon. pm is from noon to midnight. (a) Breakfast is in the morning: am. (b) 1:30 after lunch: pm. (c) Bedtime at night: pm. (d) Sunrise is in the morning: am.'),
 I('start', 1, 'Find the end or start time.', parts=[
   P('a', 'A film begins at 3:40 pm and runs for 35 minutes. It finishes at {b} : {b} pm.', ['4', '15']),
   P('b', 'A class starts at 9:50 am and ends at 10:30 am. It lasts {b} minutes.', '40'),
   P('c', 'A game ends at 5:05 pm. It lasted 25 minutes. It started at {b} : {b} pm.', ['4', '40'])],
   why='(a) 3:40 to 4:00 is 20 minutes. 15 more minutes: 4:15. (b) 9:50 to 10:00 is 10 minutes, and 10:00 to 10:30 is 30 minutes: 40 minutes. (c) Count back 5 minutes to 5:00, then 20 more minutes: 4:40.'),
 I('start', 2, 'A trip starts at 9:35 am and ends at 11:05 am. How long is the trip? Hint: draw a timeline.', parts=[P('a', 'The trip is {b} hour and {b} minutes long.', ['1', '30'], '1 hour 30 minutes')],
   space={'rows': ['Draw a timeline:']},
   why='9:35 to 10:00 is 25 minutes. 10:00 to 11:00 is 1 hour. 11:00 to 11:05 is 5 minutes. 25 + 5 = 30 minutes. The trip is 1 hour 30 minutes.'),
 I('start', 2, 'All the scales are level.', figure={'type': 'l2_scale', 'scales': [{'left': ['apple'], 'right': ['lemon', 'lemon', 'lemon'], 'label': 'Scale 1'}, {'left': ['lemon'], 'right': ['50 g'], 'label': 'Scale 2'}], 'width_mm': 120},
   partsrow=True, parts=[P('a', '1 lemon is {b} g', '50'), P('b', '1 apple is {b} g', '150')],
   why='Scale 2: 1 lemon is 50 g. Scale 1: 1 apple is as heavy as 3 lemons: 3 × 50 = 150 g.'),
 I('start', 2, 'You have a 5 ℓ jug and an 8 ℓ jug with no marks. Both jugs are empty.', figure={'type': 'l2_jugs', 'jugs': [{'cap': 5}, {'cap': 8}], 'width_mm': 40}, figside=True,
   parts=[P('a', 'Fill the 8 ℓ jug. Pour into the 5 ℓ jug until it is full. The 8 ℓ jug now holds {b} ℓ.', '3'),
          P('b', 'Empty the 5 ℓ jug. Pour the 3 ℓ in. Fill the 8 ℓ jug again. Pour into the 5 ℓ jug until it is full. The 8 ℓ jug now holds {b} ℓ.', '6')],
   why='(a) 8 - 5 = 3 ℓ is left in the 8 ℓ jug. (b) The 5 ℓ jug holds 3 ℓ, so it needs 2 ℓ more. The 8 ℓ jug gives 2 ℓ: 8 - 2 = 6 ℓ is left.'),
 I('start', 2, 'Circle the better unit.', partsrow=True, parts=[
   P('a', 'The mass of an egg   {circ:g|kg}', 'g'), P('b', 'The length of a pencil   {circ:cm|m}', 'cm'), P('c', 'The mass of a school bag   {circ:g|kg}', 'kg'), P('d', 'Water in a jug   {circ:ℓ|cm}', 'ℓ')],
   why='An egg is light: grams. A pencil is short: centimetres. A school bag is heavy: kilograms. Water in a jug is measured in litres.'),
 I('start', 3, 'Lily has a green ribbon 85 cm long. Her yellow ribbon is 27 cm shorter.',
   figure={'type': 'l2_bar', 'rows': [{'label': 'Green', 'segs': [{'w': 8.5, 't': '85 cm'}]}, {'label': 'Yellow', 'segs': [{'w': 5.8, 'unknown': True, 't': '?'}, {'w': 2.7, 'hatch': True, 't': '27'}]}], 'width_units': 400, 'width_mm': 100},
   parts=[P('a', 'The yellow ribbon is {b} cm long.', '58'), P('b', 'Lily joins them end to end with an overlap of 4 cm. The long ribbon is {b} cm.', '139'), P('c', 'She cuts 3 pieces of 20 cm from the green ribbon. Green ribbon left: {b} cm', '25')],
   why='(a) 85 - 27 = 58 cm. (b) Together 85 + 58 = 143 cm. The overlap is counted twice, so take away 4 cm: 139 cm. (c) 3 × 20 = 60 cm cut off. 85 - 60 = 25 cm left.'),
 I('start', 3, 'Change the units.', partsrow=True, parts=[
   P('a', '3 kg = {b} g', '3000'), P('b', '2500 g = {b} kg {b} g', ['2', '500']), P('c', 'A bag has 2 kg of rice. Mei uses 750 g. Rice left: {b} g', '1250')],
   why='1 kg is 1000 g. (a) 3 × 1000 = 3000 g. (b) 2500 g is 2000 g and 500 g: 2 kg 500 g. (c) 2 kg is 2000 g. 2000 - 750 = 1250 g.'),
 I('start', 3, 'Change the units.', partsrow=True, parts=[
   P('a', '2 m 35 cm = {b} cm', '235'), P('b', '180 cm = {b} m {b} cm', ['1', '80']), P('c', 'A rope is 5 m. Ali cuts off 130 cm. Rope left: {b} cm', '370')],
   why='1 m is 100 cm. (a) 200 + 35 = 235 cm. (b) 180 cm is 100 cm and 80 cm: 1 m 80 cm. (c) 5 m is 500 cm. 500 - 130 = 370 cm.'),
 I('start', 3, 'A bucket holds 12 ℓ. It has 4 ℓ in it. Mei pours in 2 ℓ each time.', parts=[
   P('a', 'How many pours fill the bucket? {b}', '4'), P('b', 'After 3 pours the bucket holds {b} ℓ.', '10')],
   why='(a) The bucket needs 12 - 4 = 8 ℓ more. 8 ÷ 2 = 4 pours. (b) 3 pours add 6 ℓ. 4 + 6 = 10 ℓ.'),
 # Think harder
 I('think', 4, '4 plums balance 1 pear. A pear and 2 plums balance 600 g.', parts=[
   P('a', 'One plum is {b} g.', '100'), P('b', 'The pear is {b} g.', '400')],
   hint='Swap the pear for 4 plums. How many plums are on that side?',
   why='Swap the pear for 4 plums. Then 4 plums and 2 plums, which is 6 plums, balance 600 g. 600 ÷ 6 = 100, so 1 plum is 100 g. The pear is 4 plums: 400 g. Check: 400 + 100 + 100 = 600.'),
 I('think', 4, 'A 5 ℓ jug and a 7 ℓ jug have no marks. Get exactly 4 ℓ. Three steps are done.',
   figure={'type': 'l2_table', 'cols': ['Step', 'What I do', '5 ℓ jug', '7 ℓ jug'], 'rows': [['Start', 'Both jugs empty', '0', '0'], ['1', 'Fill the 7 ℓ jug', '0', '7'], ['2', 'Pour into the 5 ℓ jug', '5', '2'], ['3', 'Empty the 5 ℓ jug', '0', '2'],
                                                                                           ['4', None, None, None], ['5', None, None, None], ['6', None, None, None]], 'widths': [1.1, 4, 1.4, 1.4], 'row_h': 46, 'head_h': 50, 'size': 28, 'first_bold': True, 'width_mm': 130},
   partsrow=True, parts=[P('a', 'After step 5 the jugs hold {b} ℓ and {b} ℓ.', ['2', '7']), P('b', 'At the end the 7 ℓ jug holds {b} ℓ.', '4')],
   hint='Pour the 2 ℓ into the 5 ℓ jug. Then fill the 7 ℓ jug.',
   why='Step 4: pour the 2 ℓ into the 5 ℓ jug (2, 0). Step 5: fill the 7 ℓ jug (2, 7). Step 6: pour from the 7 ℓ jug into the 5 ℓ jug until it is full. It needs 3 ℓ more, so 7 - 3 = 4 ℓ is left (5, 4). The 7 ℓ jug holds 4 ℓ.'),
 I('think', 4, 'A museum tour has 4 stops. Each stop takes 20 minutes. There is a 5-minute walk between stops. The tour starts at 9:15 am.', parts=[
   P('a', 'The tour takes {b} minutes.', '95'), P('b', 'It ends at {b} : {b} am.', ['10', '50'])],
   hint='4 stops, but how many walks?',
   why='4 stops of 20 minutes is 80 minutes. There are only 3 walks between 4 stops: 3 × 5 = 15 minutes. 80 + 15 = 95 minutes. 9:15 plus 95 minutes: 9:15 to 10:15 is 60 minutes, then 35 more: 10:50 am.'),
 # Go further
 I('go', 5, 'Beyond: the 24-hour clock. After noon add 12 to the hour: 1:30 pm is 13:30.', beyond='24-hour clock', partsrow=True, parts=[
   P('a', '3:45 pm = {b} : 45', '15'), P('b', '18:10 = {b} : 10 pm', '6'), P('c', '20:05 = {b} : 05 pm', '8')],
   hint='After noon: add 12 to the hour. Going back: take 12 away.',
   why='(a) 3 + 12 = 15, so 15:45. (b) 18 - 12 = 6, so 6:10 pm. (c) 20 - 12 = 8, so 8:05 pm.'),
 I('go', 5, 'Scale 1: 1 box and 2 cups balance 4 cups. Scale 2: 1 box and 1 cup balance 600 g.',
   figure={'type': 'l2_scale', 'scales': [{'left': ['box', 'cup', 'cup'], 'right': ['cup', 'cup', 'cup', 'cup'], 'label': 'Scale 1'}, {'left': ['box', 'cup'], 'right': ['600 g'], 'label': 'Scale 2'}], 'width_mm': 112}, figside=True,
   parts=[P('a', 'One cup is {b} g.', '200'), P('b', 'One box is {b} g.', '400')],
   hint='Take 2 cups off both sides of scale 1.',
   why='Scale 1: take 2 cups off both sides. 1 box balances 2 cups. Scale 2: swap the box for 2 cups: 3 cups balance 600 g, so a cup is 200 g. The box is 2 cups: 400 g. Check scale 1: 400 + 200 + 200 = 800 = 4 × 200.'),
 I('go', 5, 'Make your own balance puzzle with apples and lemons. One apple must be 200 g. Many answers are right.', value='open',
   atext='Open. Example: Scale 1: 1 apple balances 4 lemons. Scale 2: 1 lemon balances a 50 g weight. Then 1 apple is 4 × 50 = 200 g.', space={'rows': ['My scales:']},
   hint='Start from 200 g. What balances it?',
   why='Example: a lemon is 50 g and an apple is 4 lemons, so the apple is 200 g. Another way: 1 apple balances a 200 g weight, with a second scale for a lemon.'),
 I('go', 5, 'A clock gains 3 minutes every hour. It is set right at 7:00 am.', parts=[
   P('a', 'At 11:00 am the clock shows {b} : {b} am.', ['11', '12']), P('b', 'It shows 12:15 pm. The right time is {b} : {b}.', ['12', '00'])],
   hint='How many hours have passed? 3 minutes each hour.',
   why='(a) From 7 am to 11 am is 4 hours. 4 × 3 = 12 minutes fast: 11:12 am. (b) At the right time 12:00 pm, 5 hours have passed, and the clock is 5 × 3 = 15 minutes fast. So when the clock shows 12:15 pm the right time is 12:00 pm.'),
 # Check yourself
 I('quiz', 0, 'A show begins at 6:50 pm and runs for 35 minutes. It finishes at {b} : {b} pm.', value=['7', '25'], atext='7:25 pm', why='6:50 to 7:00 is 10 minutes. 25 more minutes: 7:25 pm.'),
 I('quiz', 0, '2 kg 300 g = {b} g', value='2300', why='2 kg is 2000 g. 2000 + 300 = 2300 g.'),
 I('quiz', 0, '1 melon balances 3 pears. 1 pear is 200 g. The melon is {b} g.', value='600', why='3 pears: 3 × 200 = 600 g. The melon is 600 g.'),
 I('quiz', 0, 'A rope is 3 m long. Ali cuts off 140 cm. Rope left: {b} cm', value='160', why='3 m is 300 cm. 300 - 140 = 160 cm.'),
]
build(9, 'Measure masters', 'Length, mass, volume and time', 'I can solve balance puzzles and pouring puzzles. I can change units. I can tell the time to 5 minutes and find how long.', learn, items, snug=['start1', 'start2', 'start3'])
