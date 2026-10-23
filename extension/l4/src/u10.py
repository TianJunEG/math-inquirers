from lib import *
U = 'L4U10'

learn = {
 'intro': 'A puzzle needs a way in. Guess and check with a table: use each try to decide whether to go up or down. Suppose all are the same: then see how many swaps you need to fix the total.',
 'example': {
  'problem': 'A shop has stools (3 legs) and chairs (4 legs). There are 11 of them with 38 legs in all. How many chairs are there?',
  'figure': {'type': 'l4_table', 'rows': [['11 stools', '11 × 3 = 33'], ['Legs short', '38 − 33 = 5'], ['1 swap adds', '1 leg']], 'widths': [1.1, 1.5], 'cell_h': 46, 'font': 26, 'first_col_head': True, 'width_mm': 82},
  'steps': ['Each swap from a stool to a chair adds 1 leg.', '5 legs short needs 5 swaps.'],
  'answer': '5 chairs and 6 stools. Check: 5 × 4 + 6 × 3 = 38.'},
 'example2': {
  'problem': 'Two next-door numbers multiply to 380. What are they?',
  'figure': {'type': 'l4_table', 'head': ['Try', 'Product', 'Check'], 'rows': [['18 × 19', '342', 'too small'], ['20 × 21', '420', 'too big'], ['19 × 20', '380', 'right']], 'widths': [1.2, 1, 1.2], 'cell_h': 44, 'font': 24, 'width_mm': 82},
  'steps': ['Try a pair. Is the product too big or too small?', 'Use each try to choose the next one.'],
  'answer': 'The numbers are 19 and 20.'},
 'pair': True, 'tight': True,
 'howto': {'title': 'Ways in',
           'steps': ['Guess and check: keep a table of tries.',
                     'Suppose all are the same. Count swaps.',
                     'Work backwards: undo the last step first.',
                     'Check your answer against every fact.']},
 'facts': {'title': 'Good to know', 'lines': ['Draw a queue or a bar model.', 'Check the answer against every clue.', 'A swap changes the total by a fixed amount.', 'Logic grid: ✓ for yes, ✗ for no. One ✓ in each row and column.']},
 'try': {'id': U + '-L01', 'text': 'A box has bees (6 legs) and spiders (8 legs). There are 10 animals with 66 legs. How many spiders are there? {b}',
         'answer': A(3),
         'explanation': 'Suppose all 10 are bees: 60 legs. That is 6 short. Each swap to a spider adds 2 legs, so 3 swaps. There are 3 spiders and 7 bees. Check: 3 × 8 + 7 × 6 = 66.'}}

S, T, G, C = [], [], [], []
S.append(item(U+'-S01', 'start', 1, 'Two next-door numbers multiply to make 506. What are they? Use the table for your tries.',
  fig={'type': 'l4_table', 'head': ['First number', 'Next number', 'Product', 'Too big or small?'], 'rows': [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], 'widths': [1.3, 1.3, 1.2, 1.6], 'cell_h': 44, 'font': 22, 'width_mm': 150},
  ans=A(22, 23, text='22 and 23'), partsrow=False,
  why='20 × 21 = 420 is too small. 25 × 26 = 650 is too big. 22 × 23 = 506. Use each try to decide the next one: 21 × 22 = 462 is too small, so go up.',
  space={'rows': ['The numbers are {b} and {b}']}))
S.append(item(U+'-S02', 'start', 1, 'Mei has one 5¢ coin, one 10¢ coin and one 50¢ coin. She picks some of the coins. She picks at least 1.',
  parts=[P('a', 'How many different totals can she make? {b}', A(7)), P('b', 'How many of the totals are more than 50¢? {b}', A(3))],
  why='The totals are 5, 10, 50, 15, 55, 60 and 65: 7 totals. The totals above 50 are 55, 60 and 65: 3 totals.',
  space={'rows': ['Totals: {ll}', '']}))
S.append(item(U+'-S03', 'start', 1, 'A concert sold 17 tickets. Some cost $6 and some cost $10. The takings were $134.',
  parts=[P('a', 'Suppose all 17 cost $6. They cost ${b}.', A(102)), P('b', 'That is ${b} too little.', A(32)),
         P('c', 'Each swap to a $10 ticket adds $4. There are {b} tickets at $10.', A(8))],
  space={'rows': ['Check:']},
  why='(a) 17 × 6 = 102. (b) 134 − 102 = 32. (c) 32 ÷ 4 = 8 swaps, so 8 tickets at $10 and 9 at $6.'))
S.append(item(U+'-S04', 'start', 2, 'A shop has 13 bags of rice. Some bags are 3 kg and some are 5 kg. They have a mass of 49 kg in all.',
  parts=[P('a', 'The number of 5 kg bags is {b}', A(5)), P('b', 'The number of 3 kg bags is {b}', A(8))], partsrow=True,
  why='Suppose all 13 are 3 kg: 39 kg. That is 10 kg short. Each swap to a 5 kg bag adds 2 kg, so 5 bags of 5 kg and 13 − 5 = 8 bags of 3 kg.',
  space={'rows': ['Working:']}))
S.append(item(U+'-S05', 'start', 2, 'A magic pot triples the coins put into it. Then 8 coins are taken out. Then the pot halves the coins that are left. Now there are 20 coins. How many coins were put in at the start? {b}',
  fig={'type': 'l4_flow', 'items': [None, None, None, 20], 'ops': ['× 3', '− 8', '÷ 2'], 'width_mm': 130},
  ans=A(16), why='Work backwards. Undo halving: 20 × 2 = 40. Undo taking out 8: 40 + 8 = 48. Undo tripling: 48 ÷ 3 = 16.'))
S.append(item(U+'-S06', 'start', 2, 'A film session ends at 3:20 pm. The film lasts 1 hour 45 minutes. The adverts before it last 15 minutes. The session starts at {b} pm.',
  ans=A('1:20'), why='Work backwards. 3:20 − 1 h 45 min = 1:35. Then 1:35 − 15 min = 1:20. The session starts at 1:20 pm.',
  space={'rows': ['Working:', '']}))
S.append(item(U+'-S07', 'start', 2, 'Ali, Ben, Mei and Siti each have a different pet: a cat, a dog, a fish or a rabbit. Ali\'s pet barks. Ben\'s pet has no fur. Mei\'s pet does not hop. Use the grid. Write ✓ for yes and ✗ for no.',
  fig={'type': 'l4_table', 'head': ['', 'cat', 'dog', 'fish', 'rabbit'], 'rows': [['Ali', '', '', '', ''], ['Ben', '', '', '', ''], ['Mei', '', '', '', ''], ['Siti', '', '', '', '']], 'widths': [1.1, 1, 1, 1, 1.2], 'cell_h': 40, 'font': 26, 'first_col_head': True, 'width_mm': 100},
  parts=[P('a', 'Ali: {b}', A('dog')), P('b', 'Ben: {b}', A('fish')), P('c', 'Mei: {b}', A('cat')), P('d', 'Siti: {b}', A('rabbit'))], partsrow=True,
  why='Ali\'s pet barks, so it is the dog. The fish is the only pet with no fur, so Ben has the fish. A rabbit hops, so Mei does not have the rabbit. The cat and the rabbit are left. Mei has the cat and Siti has the rabbit.'))
S.append(item(U+'-S08', 'start', 3, 'Aisha stands in a queue. There are 8 people in front of her and 4 behind her.',
  parts=[P('a', 'The queue has {b} people.', A(13)), P('b', 'Ben is in another queue. He has 4 people behind him and he is 6th in line. That queue has {b} people.', A(10))],
  why='(a) 8 people in front, Aisha herself and 4 behind: 8 + 1 + 4 = 13. (b) Ben is 6th, so 5 people are in front of him. 5 + 1 + 4 = 10.',
  space={'rows': ['Draw the queue here.', '']}))
S.append(item(U+'-S09', 'start', 3, 'Kumar is 4 times as old as his sister. Their ages add up to 45. How old is his sister? {b}',
  ans=A(9), why='The sister is 1 unit and Kumar is 4 units: 5 units = 45, so 1 unit = 9. The sister is 9 and Kumar is 36. Check: 9 + 36 = 45 and 36 = 4 × 9.',
  space={'rows': ['Draw a bar model here.', '']}))
S.append(item(U+'-S10', 'start', 3, 'Ravi has 9 coins. They are 20¢ coins and 50¢ coins. They are worth $3.00 altogether. Find the number of 50¢ coins. {b}',
  ans=A(4), why='Suppose all 9 are 20¢: 180¢. That is 120¢ short. Each swap to a 50¢ coin adds 30¢. 120 ÷ 30 = 4 swaps. So 4 coins of 50¢ and 5 coins of 20¢. Check: 200¢ + 100¢ = 300¢.',
  space={'rows': ['Working:']}))

S.append(item(U+'-S11', 'start', 3, 'Three next-door numbers add up to 87. What are they? {b}, {b}, {b}',
  ans=A(28, 29, 30, text='28, 29, 30'), why='The middle number is the one in the middle of the 3, so 87 ÷ 3 = 29. The numbers are 28, 29 and 30. Check: 28 + 29 + 30 = 87.',
  space={'rows': ['Working:']}))
S.append(item(U+'-S12', 'start', 3, 'A lock code has 3 digits. The middle digit is 0. The first digit is twice the last digit. The digits add up to 9. What is the code? {b}',
  ans=A(603), hint='Try a last digit of 1, then 2, then 3. Add the digits.',
  why='The first digit is twice the last, so the 3 digits add up to 3 times the last digit. 3 × last = 9, so the last digit is 3 and the first is 6. The code is 603.',
  space={'rows': ['Try:']}))

T.append(item(U+'-T01', 'think', 4, 'A shop sells pens in boxes of 2 and boxes of 5. Ali buys 12 boxes with 45 pens in all.',
  parts=[P('a', 'The number of boxes of 5 is {b}', A(7)), P('b', 'The number of boxes of 2 is {b}', A(5))], partsrow=True,
  hint='Suppose all 12 boxes hold 2 pens. How many pens are missing?',
  why='If all 12 boxes held 2 pens, there would be 24 pens. 45 − 24 = 21 pens are missing. Each box of 5 instead of 2 adds 3 pens, so 21 ÷ 3 = 7 boxes of 5. The other 12 − 7 = 5 boxes hold 2. Check: 35 + 10 = 45.',
  space={'rows': ['Working:', '']}))
T.append(item(U+'-T02', 'think', 4, 'Ali, Ben, Kumar, Mei and Siti run a race. Nobody ties. Ali finishes before Mei. Mei finishes before Ben. Kumar finishes just after Siti. Ben does not finish last.',
  parts=[P('a', 'Finishing order: {b} {b} {b} {b} {b}', A('Ali', 'Mei', 'Ben', 'Siti', 'Kumar', text='Ali, Mei, Ben, Siti, Kumar'))],
  hint='Join the clues into 2 groups. Which group can go last?',
  why='Ali, Mei and Ben finish in that order. Siti and Kumar finish side by side, Siti first. Ben is not last, so the pair Siti, Kumar cannot come before Ben and leave Ben last. The pair must be last: Ali, Mei, Ben, Siti, Kumar. Check each clue.',
  space={'rows': ['Try:', '']}))
T.append(item(U+'-T03', 'think', 4, 'Ravi saves $2 on Day 1, $4 on Day 2, $6 on Day 3 and so on. He saves $2 more each day.',
  parts=[P('a', 'His total first goes above $100 on Day {b}', A(10)), P('b', 'The total on that day is ${b}', A(110))],
  hint='Make a table: day, saved that day, total so far.',
  why='The totals are $2, $6, $12, $20, $30, $42, $56, $72, $90 and $110 for Days 1 to 10. On Day 9 the total is $90, which is not above $100. On Day 10 it is $110.',
  space={'rows': ['Day, saved, total: {ll}', '', '']}))

G.append(item(U+'-G01', 'go', 5, 'How many whole numbers from 1 to 200 have digits that add up to 5? {b}',
  ans=A(11), hint='Be systematic. How many 1-digit numbers fit?',
  why='1-digit: 5. 2-digit: 14, 23, 32, 41, 50. 3-digit, starting with 1: the other 2 digits add to 4: 104, 113, 122, 131, 140. 200 has a digit sum of 2. In all 1 + 5 + 5 = 11.',
  space={'rows': ['List: {ll}']}))
G.append(item(U+'-G02', 'go', 5, 'Ali has 3 times as many 20¢ coins as 50¢ coins. His coins are worth $4.40 altogether. How many coins does he have in all? {b}',
  ans=A(16), hint='Try a small number of 50¢ coins first.',
  why='A group of 3 coins of 20¢ and 1 coin of 50¢ is worth 60¢ + 50¢ = 110¢. $4.40 = 440¢ and 440 ÷ 110 = 4 groups. Each group has 4 coins, so he has 16 coins: 12 coins of 20¢ and 4 coins of 50¢.',
  space={'rows': ['Working:', '']}))
G.append(item(U+'-G03', 'go', 5, 'In a line of children, Ben is 11th from the left. Mei is 8th from the right. There are 5 children between Ben and Mei. How many children could be in the line? Find both answers.\n{b} or {b}',
  ans=A(12, 24, text='12 or 24', unordered=True), hint='Mei may be left or right of Ben.',
  why='If Mei is to the right of Ben, she is 6 places after him: 11 + 6 = 17th from the left. She is 8th from the right, so there are 17 + 7 = 24 children. If Mei is to the left of Ben, she is 11 − 6 = 5th from the left, so there are 5 + 7 = 12 children. Both fit: the 5 children in between are places 6 to 10 in the line of 12, or places 12 to 16 in the line of 24.',
  space={'rows': ['Draw the line here.', '']}))
G.append(item(U+'-G04', 'go', 5, 'Beyond Level 4: Number cycles\nThe ones digits of 3, 3 × 3, 3 × 3 × 3 and so on go round in a cycle.',
  parts=[P('a', 'The ones digit of 3 × 3 × 3 × 3 × 3 (five 3s) is {b}', A(3)), P('b', 'The ones digit of 20 threes multiplied together is {b}', A(1))],
  hint='Write the ones digits of the first 6 products. Look for the cycle.',
  why='The products are 3, 9, 27, 81, 243, 729, 2187. The ones digits are 3, 9, 7, 1, 3, 9, 7 and go round in a cycle of 4. (a) The 5th product ends in 3. (b) 20 is 5 whole cycles of 4, so the 20th product ends in the last digit of the cycle, which is 1.',
  space={'rows': ['Ones digits: {ll}']}))

C.append(item(U+'-C01', 'quiz', None, 'A garage has cars (4 wheels) and bikes (2 wheels). There are 10 of them with 28 wheels. How many cars are there? {b}', ans=A(4),
  why='Suppose all 10 are bikes: 20 wheels, 8 short. Each swap to a car adds 2 wheels, so 4 cars and 6 bikes. Check: 16 + 12 = 28.'))
C.append(item(U+'-C02', 'quiz', None, 'Ali thinks of a number. He adds 8, doubles it and takes away 6. His answer is 30. What is his number? {b}', ans=A(10),
  why='Work backwards. 30 + 6 = 36. 36 ÷ 2 = 18. 18 − 8 = 10. Check: 10 + 8 = 18, 18 × 2 = 36, 36 − 6 = 30.'))
C.append(item(U+'-C03', 'quiz', None, 'There are 9 people in front of Siti in a line and 6 behind her. The line has {b} people.', ans=A(16),
  why='9 in front, Siti herself and 6 behind: 9 + 1 + 6 = 16.'))
C.append(item(U+'-C04', 'quiz', None, 'Two next-door numbers multiply to make 272. What are they? {b} and {b}', ans=A(16, 17, text='16 and 17'),
  why='15 × 16 = 240 is too small and 17 × 18 = 306 is too big. 16 × 17 = 272.'))

unit = {'schema_version': 1, 'level': 4, 'unit': 10, 'id': U, 'title': 'Puzzle Day', 'topic': 'Mixed puzzle heuristics', 'holiday_lesson': 10,
        'goal': 'I can choose a way in to a puzzle: guess and check, suppose all are the same, work backwards, draw it or use a logic grid.',
        'learn': learn, 'items': S + T + G + C}
write(10, unit)
