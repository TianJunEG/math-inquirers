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
S.append(item(U+'-S02', 'start', 1, 'Mei buys some $3 pens and some $5 notebooks. She buys at least 1 of each. She pays exactly $41.',
  parts=[P('a', 'How many different ways can she do it? {b}', A(3)), P('b', 'The way with the fewest pens: {b} pens and {b} notebooks', A(2, 7, text='2 pens and 7 notebooks'))],
  why='Try the number of notebooks: 1 notebook leaves $36, which is 12 pens. 2 leaves $31 (no). 3 leaves $26 (no). 4 leaves $21, which is 7 pens. 5 leaves $16 (no). 6 leaves $11 (no). 7 leaves $6, which is 2 pens. 8 notebooks cost $40 and leave $1 (no). So the ways are 12 pens and 1 notebook, 7 pens and 4 notebooks, and 2 pens and 7 notebooks.',
  space={'rows': ['Notebooks, money left, pens: {ll}', 'My answer: {l}']}))
S.append(item(U+'-S03', 'start', 1, 'A farm has hens (2 legs) and cows (4 legs). There are 17 animals with 50 legs.',
  parts=[P('a', 'Suppose all 17 are hens. They have {b} legs.', A(34)), P('b', 'That is {b} legs short.', A(16)),
         P('c', 'Each swap to a cow adds 2 legs. There are {b} cows.', A(8))],
  space={'rows': ['Check:']},
  why='(a) 17 × 2 = 34. (b) 50 − 34 = 16. (c) 16 ÷ 2 = 8 swaps, so 8 cows and 9 hens. Check: 8 × 4 + 9 × 2 = 32 + 18 = 50.'))
S.append(item(U+'-S04', 'start', 2, 'A shed has bicycles (2 wheels) and tricycles (3 wheels). There are 13 of them with 33 wheels.',
  parts=[P('a', 'The number of tricycles is {b}', A(7)), P('b', 'The number of bicycles is {b}', A(6))], partsrow=True,
  why='Suppose all 13 are bicycles: 26 wheels. That is 7 short. Each swap to a tricycle adds 1 wheel, so 7 tricycles and 13 − 7 = 6 bicycles. Check: 7 × 3 + 6 × 2 = 33.',
  space={'rows': ['Working:']}))
S.append(item(U+'-S05', 'start', 2, 'Mei had some stickers. She gave half of them to Ali. Then she bought 12 more. Then she lost 7. Now she has 25 stickers. Find how many she had at the start. {b}',
  fig={'type': 'l4_flow', 'items': [None, None, None, 25], 'ops': ['÷ 2', '+ 12', '− 7'], 'width_mm': 130},
  ans=A(40), why='Work backwards. Undo the loss of 7: 25 + 7 = 32. Undo the 12 she bought: 32 − 12 = 20. Undo giving away half: 20 × 2 = 40. Check: half of 40 is 20, 20 + 12 = 32, 32 − 7 = 25.'))
S.append(item(U+'-S06', 'start', 2, 'Kumar thinks of a number. He doubles it, adds 14 and then divides by 4. His answer is 10. What is his number? {b}',
  ans=A(13), why='Work backwards. 10 × 4 = 40. 40 − 14 = 26. 26 ÷ 2 = 13. Check: 13 × 2 = 26, 26 + 14 = 40, 40 ÷ 4 = 10.',
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
S.append(item(U+'-S12', 'start', 3, 'Who am I? My 2 digits add up to 12. Swapping them gives a number 18 greater than me. {b}',
  ans=A(57), why='Try pairs of digits that add up to 12: 39, 48, 57, 66, 75, 84, 93. The swapped numbers are 93, 84, 75, 66, 57, 48, 39. The swapped number is 18 more only for 57 and 75: 75 − 57 = 18. The number must be the smaller one, 57.',
  space={'rows': ['Try:']}))

T.append(item(U+'-T01', 'think', 4, 'A shop sells pens in boxes of 2 and boxes of 5. Ali buys 12 boxes with 45 pens in all.',
  parts=[P('a', 'The number of boxes of 5 is {b}', A(7)), P('b', 'The number of boxes of 2 is {b}', A(5))], partsrow=True,
  hint='Suppose all 12 boxes hold 2 pens. How many pens are missing?',
  why='If all 12 boxes held 2 pens, there would be 24 pens. 45 − 24 = 21 pens are missing. Each box of 5 instead of 2 adds 3 pens, so 21 ÷ 3 = 7 boxes of 5. The other 12 − 7 = 5 boxes hold 2. Check: 35 + 10 = 45.',
  space={'rows': ['Working:', '']}))
T.append(item(U+'-T02', 'think', 4, 'Ali, Ben, Kumar, Mei and Siti run a race. Nobody ties. Ali finishes before Mei. Mei finishes before Ben. Kumar finishes just after Siti. Ben does not finish last.',
  parts=[P('a', 'Places 1 to 5, in order: {b} {b} {b} {b} {b}', A('Ali', 'Mei', 'Ben', 'Siti', 'Kumar', text='Ali, Mei, Ben, Siti, Kumar'))],
  hint='Write what you know in 3 groups. Which group can go last?',
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
