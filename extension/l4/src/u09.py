from lib import *
U = 'L4U09'
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
LINE = lambda panels, xl, **kw: dict({'type': 'l4_line', 'panels': panels, 'xlabels': xl, 'width_mm': 130}, **kw)

learn = {
 'intro': 'On a line graph, read the title and the scale first. The change between 2 neighbouring points is the difference of their values. A table can have a missing number: use the totals to find it.',
 'example': {
  'problem': 'The graph shows the cups of barley water a stall sold. Each line is worth 10. How many cups were sold on Wednesday? When was the greatest drop?',
  'figure': LINE([{'ymin': 0, 'ymax': 80, 'step': 10, 'label_every': 2, 'series': [{'values': [40, 65, 55, 75, 30]}]}], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], width_mm=74, plot_w=340, plot_h=160),
  'steps': ['The Wednesday point is halfway between 50 and 60: 55 cups.', 'Find each change. Thu to Fri is 75 − 30 = 45 down. That is the greatest drop.'],
  'answer': '55 cups. The greatest drop was Thursday to Friday.'},
 'example2': {
  'problem': 'Find the missing number. Each row and each column adds to its total.',
  'figure': {'type': 'l4_table', 'head': ['', 'Week 1', 'Week 2', 'Total'], 'rows': [['Ali', '14', '?', '31'], ['Mei', '20', '18', '38'], ['Total', '34', '35', '69']], 'widths': [1.2, 1.2, 1.2, 1.2], 'cell_h': 46, 'font': 26, 'first_col_head': True, 'width_mm': 82},
  'steps': ['Use Ali\'s row: 14 + ? = 31, so ? = 31 − 14 = 17.', 'Check the Week 2 column: 17 + 18 = 35.'],
  'answer': 'The missing number is 17.'},
 'pair': True, 'tight': True,
 'howto': {'title': 'How to read data',
           'steps': ['Read the title and the scale. What is one line worth?',
                     'Change = the difference between 2 neighbours.',
                     'Missing numbers: use the row or column total.']},
 'facts': {'title': 'Good to know', 'lines': ['The steepest line is the greatest change.', 'Check where each scale starts.']},
 'try': {'id': U + '-L01', 'text': 'Each line on a graph is worth 5. Monday\'s point is at 70 books. Tuesday\'s point is 2 lines higher. How many books does Tuesday show? {b}',
         'answer': A(80),
         'explanation': '2 lines are worth 2 × 5 = 10. 70 + 10 = 80 books.'}}

S, T, G, C = [], [], [], []
S.append(item(U+'-S01', 'start', 1, 'The graph shows how many people visited a library each day. Each line is worth 10.',
  fig=LINE([{'ymin': 0, 'ymax': 100, 'step': 10, 'label_every': 2, 'series': [{'values': [30, 45, 25, 60, 55, 95]}]}], DAYS, width_mm=112, plot_w=400, plot_h=200, ylabel='Visitors'),
  parts=[P('a', 'Visitors on Thursday: {b}', A(60)), P('b', 'Visitors on Tuesday: {b}', A(45)), P('c', 'Visitors on Monday and Tuesday together: {b}', A(75))],
  partsrow=True,
  why='(a) The Thursday point is on the 60 line. (b) The Tuesday point is halfway between 40 and 50: 45. (c) 30 + 45 = 75.'))
S.append(item(U+'-S02', 'start', 1, 'Use the graph in Question 1. Find the greatest increase and the greatest decrease between 2 days.',
  parts=[P('a', 'Greatest increase: from {b} to {b}, up by {b}', A('Fri', 'Sat', 40, text='Friday to Saturday, up by 40')),
         P('b', 'Greatest decrease: from {b} to {b}, down by {b}', A('Tue', 'Wed', 20, text='Tuesday to Wednesday, down by 20'))],
  why='The changes are +15, −20, +35, −5 and +40. The greatest increase is Friday to Saturday: 95 − 55 = 40. The greatest decrease is Tuesday to Wednesday: 45 − 25 = 20. The steepest line going up and the steepest line going down show these.',
  space={'rows': ['Changes: {ll}']}))
S.append(item(U+'-S03', 'start', 1, 'The table shows the library books 3 classes borrowed. Each row and each column adds up to its total. Write the missing numbers.',
  fig={'type': 'l4_table', 'head': ['', 'Week 1', 'Week 2', 'Total'], 'rows': [['4A', '38', '', '85'], ['4B', '', '29', '70'], ['4C', '33', '41', ''], ['Total', '', '', '']], 'widths': [1.1, 1.2, 1.2, 1.2], 'cell_h': 52, 'font': 28, 'first_col_head': True, 'width_mm': 100},
  parts=[P('a', 'Fill in the 6 empty boxes. Go row by row.', A(47, 41, 74, 112, 117, 229, text='47, 41, 74, 112, 117, 229')),
         P('b', 'Which class borrowed fewer books in Week 2 than in Week 1? {circ:4A|4B|4C}', A('4B'))],
  figside=True,
  why='4A: 85 − 38 = 47. 4B: 70 − 29 = 41. 4C: 33 + 41 = 74. Week 1: 38 + 41 + 33 = 112. Week 2: 47 + 29 + 41 = 117. Total: 112 + 117 = 229, and 85 + 70 + 74 = 229 too. 4B borrowed 41 in Week 1 and only 29 in Week 2.'))
S.append(item(U+'-S04', 'start', 2, 'The graph shows money in Ali\'s box and in Mei\'s box. The amounts are at the end of each week.',
  fig=LINE([{'ymin': 0, 'ymax': 100, 'step': 10, 'label_every': 2, 'series': [{'name': 'Ali', 'values': [20, 30, 40, 50, 60, 70, 80, 90]}, {'name': 'Mei', 'values': [50, 55, 60, 65, 70, 75, 80, 85]}]}], ['1', '2', '3', '4', '5', '6', '7', '8'], xlabel='Week', width_mm=120, plot_w=440, plot_h=190),
  parts=[P('a', 'Mei\'s money in Week 3: ${b}', A(60)), P('b', 'Each week Ali adds ${b}.', A(10)),
         P('c', 'Both have equal money in Week {b}.', A(7)), P('d', 'Ali first has more than Mei in Week {b}.', A(8))], partsrow=True,
  why='(a) The Mei line (dashed, square points) is on 60 in Week 3. (b) Ali\'s line goes up by 10 each week. (c) The lines meet in Week 7, where both have $80. (d) Ali has $90 in Week 8 and Mei has $85, so Week 8 is the first week Ali has more.'))
S.append(item(U+'-S05', 'start', 2, 'Siti reads more pages each day. She reads the same number more each day. Fill in the table.',
  fig={'type': 'l4_table', 'head': ['Day', '1', '2', '3', '4', '5'], 'rows': [['Pages', '12', '', '', '27', '']], 'widths': [1.4, 1, 1, 1, 1, 1], 'cell_h': 58, 'font': 28, 'first_col_head': True, 'width_mm': 120},
  parts=[P('a', 'She reads {b} more pages each day.', A(5)), P('b', 'In the 5 days she reads {b} pages.', A(110))],
  why='Day 1 to Day 4 is 3 days, and 27 − 12 = 15, so she reads 15 ÷ 3 = 5 more each day. The days are 12, 17, 22, 27 and 32. The total is 12 + 17 + 22 + 27 + 32 = 110 pages.',
  space={'rows': ['Working:']}))
S.append(item(U+'-S06', 'start', 3, 'Two bakeries show the cakes they sold. Look at each scale. Bakery Q\'s scale starts at 40.',
  fig=LINE([{'title': 'Bakery P', 'ymin': 0, 'ymax': 100, 'step': 20, 'series': [{'values': [40, 52, 64, 88]}]}, {'title': 'Bakery Q', 'ymin': 40, 'ymax': 52, 'step': 2, 'label_every': 1, 'series': [{'values': [42, 45, 48, 52]}]}], ['Jan', 'Feb', 'Mar', 'Apr'], width_mm=150, plot_w=300, plot_h=160),
  parts=[P('a', 'From January to April, Bakery P went up by {b} cakes.', A(48)), P('b', 'Bakery Q went up by {b} cakes.', A(10)),
         P('c', 'Which bakery sold more extra cakes? {circ:P|Q}', A('P'))],
  why='(a) P: 88 − 40 = 48. (b) Q: 52 − 42 = 10. (c) P went up by 48 and Q by 10. Bakery Q\'s line looks steeper only because its scale starts at 40 and each line is worth 2.'))
S.append(item(U+'-S07', 'start', 3, 'The graph shows the pencils a shop sold. Look at the scale.',
  fig=LINE([{'ymin': 40, 'ymax': 100, 'step': 10, 'label_every': 1, 'series': [{'values': [60, 90]}]}], ['Mon', 'Tue'], width_mm=60, plot_w=200, plot_h=150),
  parts=[P('a', 'Monday: {b} pencils', A(60)), P('b', 'Tuesday: {b} pencils', A(90)),
         P('c', 'Tuesday\'s point is more than twice as high as Monday\'s. Is Tuesday\'s number more than double Monday\'s? {circ:Yes|No}', A('No'))],
  figside=True,
  why='(a) Monday is on the 60 line. (b) Tuesday is on the 90 line. (c) Double 60 is 120, and 90 is less. The point looks more than twice as high because the scale starts at 40, not at 0.'))
S.append(item(U+'-S08', 'start', 3, 'At 7 am the temperature was 25 °C. It rose by 2 °C every hour until noon. Then it fell by 3 °C every hour.',
  parts=[P('a', 'The temperature at noon was {b} °C', A(35)), P('b', 'The temperature at 3 pm was {b} °C', A(26)),
         P('c', 'At what time before noon was it 29 °C? {b} am', A(9))],
  why='(a) From 7 am to noon is 5 hours: 25 + 5 × 2 = 35 °C. (b) From noon to 3 pm is 3 hours: 35 − 3 × 3 = 26 °C. (c) 29 − 25 = 4 °C more, and 4 ÷ 2 = 2 hours after 7 am, which is 9 am.',
  space={'rows': ['Working:']}))

T.append(item(U+'-T01', 'think', 4, 'Sales grow by the same number of toys each week. Week 3: 52 toys. Week 8: 87 toys.',
  parts=[P('a', 'It sold {b} toys in Week 1.', A(38)), P('b', 'It first sold more than 100 toys in Week {b}.', A(10))],
  hint='From Week 3 to Week 8 is 5 weeks. How much is that each week?',
  why='87 − 52 = 35 over 5 weeks, so sales go up by 7 each week. Week 1 is 2 weeks before Week 3: 52 − 14 = 38. Week 9 is 94 and Week 10 is 101, so Week 10 is the first week above 100.',
  space={'rows': ['Working:', '']}))
T.append(item(U+'-T02', 'think', 4, 'A stall sold 200 plates in 4 days. On Day 2 it sold twice as many as on Day 1. On Day 3 it sold 15 more than on Day 2. On Day 4 it sold 25. Find the number of plates sold on Day 1. {b}',
  ans=A(32), hint='Start with a bar for Day 1. Compare the other days with it.',
  why='Take away Day 4 and the extra 15: 200 − 25 − 15 = 160. Day 1 is 1 unit, Day 2 is 2 units and Day 3 is 2 units: 5 units = 160. 1 unit = 32. Check: 32 + 64 + 79 + 25 = 200.',
  space={'rows': ['Draw a bar model here.', '', '']}))
T.append(item(U+'-T03', 'think', 4, 'Taxi A charges $4 to start and then $2 for every km. Taxi B charges $10 to start and then $1 for every km.',
  parts=[P('a', 'For {b} km the 2 taxis cost the same.', A(6)), P('b', 'Then each fare is ${b}', A(16))],
  hint='Make a table of both fares for 1 km, 2 km, 3 km.',
  why='Taxi A: $6, $8, $10, $12, $14, $16 for 1 to 6 km. Taxi B: $11, $12, $13, $14, $15, $16 for 1 to 6 km. The fares are equal at 6 km: $4 + 6 × $2 = $16 and $10 + 6 × $1 = $16. Taxi B costs $6 more to start, and Taxi A gains $1 on B for each km, so 6 km.',
  space={'rows': ['Working:', '', '']}))

G.append(item(U+'-G01', 'go', 5, 'Two graphs show the same shop\'s sales in January and February. Graph X starts at 0 with 20 for each line. Graph Y starts at 60 with 5 for each line. Graph X shows January 4 lines up and February 5 lines up.',
  parts=[P('a', 'The sales rose by {b}', A(20)), P('b', 'On graph Y, January is {b} lines up and February is {b} lines up.', A(4, 8, text='4 lines and 8 lines')),
         P('c', 'Which graph makes the rise look greater? {circ:X|Y}', A('Y'))],
  hint='Find the sales in January and February first.',
  why='On X, January is 4 × 20 = 80 and February is 5 × 20 = 100, so sales rose by 20. On Y: (80 − 60) ÷ 5 = 4 lines and (100 − 60) ÷ 5 = 8 lines. Graph Y\'s line goes up 4 lines and X\'s goes up 1 line, so Y makes the rise look greater.',
  space={'rows': ['Working:']}))
G.append(item(U+'-G02', 'go', 5, 'A stall sold 340 plates in 5 days, Monday to Friday. Each day\'s sales beat the day before by 8 plates.',
  parts=[P('a', 'On Monday it sold {b} plates.', A(52)), P('b', 'On Friday it sold {b} plates.', A(84))],
  hint='Take away the extras: 0, 8, 16, 24 and 32.',
  why='The extras over Monday are 0 + 8 + 16 + 24 + 32 = 80. Without them, 5 equal days make 340 − 80 = 260, so Monday is 260 ÷ 5 = 52. Friday is 52 + 32 = 84. The days are 52, 60, 68, 76 and 84.',
  space={'rows': ['Working:', '']}))
G.append(item(U+'-G03', 'go', 5, 'Beyond Level 4: Average\nThe average is the total divided by the count of numbers.',
  parts=[P('a', 'The average of 3, 6 and 9 is {b}', A(6)),
         P('b', 'A stall\'s average over 4 days is 45 plates. Three days were 40, 50 and 38 plates. The fourth day was {b} plates.', A(52))],
  hint='Total = average × the number of days.',
  why='(a) 3 + 6 + 9 = 18, and 18 ÷ 3 = 6. (b) The total for 4 days is 4 × 45 = 180. The 3 known days make 40 + 50 + 38 = 128. The fourth day is 180 − 128 = 52 plates.',
  space={'rows': ['Working:', '']}))

C.append(item(U+'-C01', 'quiz', None, 'The graph shows the cakes a shop sold. Each line is worth 10. How many cakes were sold on Wednesday? {b}',
  fig=LINE([{'ymin': 0, 'ymax': 80, 'step': 10, 'label_every': 2, 'series': [{'values': [30, 50, 65, 40]}]}], ['Mon', 'Tue', 'Wed', 'Thu'], width_mm=64, plot_w=320, plot_h=190),
  ans=A(65), figright=True, why='The Wednesday point is halfway between the 60 line and the 70 line: 65 cakes.'))
C.append(item(U+'-C02', 'quiz', None, 'A shop sold 28 pens on Monday and 35 on Tuesday. The 3-day total was 99. Wednesday: {b} pens', ans=A(36),
  why='28 + 35 = 63 pens on Monday and Tuesday. 99 − 63 = 36 pens on Wednesday.'))
C.append(item(U+'-C03', 'quiz', None, 'Sales rise by the same amount each day. Day 1: 14. Day 4: 32. Day 6: {b}', ans=A(44),
  why='From Day 1 to Day 4 is 3 days, and 32 − 14 = 18, so sales go up by 6 each day. Day 6 is 32 + 2 × 6 = 44.'))
C.append(item(U+'-C04', 'quiz', None, 'Both graphs show sales of 60 in May and 70 in June. A starts at 0 and B starts at 50. Which looks steeper? {circ:A|B}', ans=A('B'),
  why='Graph B\'s scale starts at 50, so the same 10 more looks like a greater rise. Sales rose by 10 on both graphs.'))

unit = {'schema_version': 1, 'level': 4, 'unit': 9, 'id': U, 'title': 'Data Detectives', 'topic': 'Tables and line graphs', 'holiday_lesson': 9,
        'goal': 'I can read values and changes on line graphs. I can find missing numbers in tables and spot graphs with scales that mislead.',
        'learn': learn, 'items': S + T + G + C}
write(9, unit)
