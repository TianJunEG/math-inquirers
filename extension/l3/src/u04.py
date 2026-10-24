from lib import *

u = Unit(4, 'Draw the problem', 'Word problems with bar models',
         'I can draw a bar model for a word problem. I can use it to decide what to add, subtract or divide.')


def bar(rows, w=110, u_=60, lab=20, **kw):
    d = {'type': 'l3_bars', 'rows': rows, 'width_mm': w, 'u': u_, 'lab': lab}
    d.update(kw)
    return d


def seg(w, t='', style='plain'):
    return {'w': w, 't': t, 'style': style}


u.learn(
    'A bar model is a picture of a word problem. Each bar is a length that shows an amount. Longer bar, greater amount.',
    {'problem': 'Siti has 260 beads. Ravi has 135 more beads than Siti. How many beads do they have in all?',
     'figure': bar([{'label': 'Siti', 'segs': [seg(4, '260', 'sky')]}, {'label': 'Ravi', 'segs': [seg(4, '260', 'sky'), seg(2, '135', 'ghost')]}], w=126, lab=120),
     'steps': ['Draw a bar for Siti. Draw a longer bar for Ravi. The extra part is 135.',
               'Ravi has 260 + 135 = 395 beads.',
               'Both children: 260 + 395 = 655 beads.'],
     'answer': 'They have 655 beads in all.'},
    {'title': 'How to draw a bar model',
     'steps': ['Draw one bar for each amount.', 'Write what you know on the bars. Put a ? on what you want to find.',
               'Look at the bars. Then add, subtract or divide.']},
    {'text': 'Ravi’s plant is 480 mm tall. Mei’s plant is 215 mm shorter. How tall is Mei’s plant? {b} mm', 'answer': A('265'),
     'explanation': 'Mei’s plant is shorter, so subtract: 480 - 215 = 265 mm. Check: 265 + 215 = 480.'})

u.u['learn']['facts'] = {'title': 'More models', 'lines': ['3 times as many, 48 in all: 4 boxes, 48 ÷ 4 = 12.', '50 in all, 10 more: 50 - 10 = 40, so 20 and 30.', '70 and 50: the gap is 20. Give half the gap, 10: 60 each.']}

# ---------------- Start here (pages 1 to 3)
u.S(1, 'A farm has 2400 eggs. 875 of them are brown. The rest are white. How many eggs are white? {b}', A('1525'),
    figure=bar([{'segs': [seg(3.5, '875', 'sky'), seg(6, '', 'q')], 'braces': [{'a': 0, 'b': 1, 't': '2400'}]}], w=112), figright=False,
    why='The whole bar is 2400 eggs. One part is 875, so the white part is 2400 - 875 = 1525. Check: 875 + 1525 = 2400.')
u.S(1, 'Ben has 1450 cards. Aisha has 380 fewer cards than Ben.', parts=[
    P('a', 'Aisha has {b} cards.', A('1070')), P('b', 'They have {b} cards in all.', A('2520'))],
    figure=bar([{'label': 'Ben', 'segs': [seg(7, '1450', 'sky')]}, {'label': 'Aisha', 'segs': [seg(5, '?', 'q'), seg(2, '380', 'ghost')]}], w=112, lab=120),
    why='(a) Aisha has fewer, so subtract: 1450 - 380 = 1070. (b) Together: 1450 + 1070 = 2520.')
u.S(1, 'A school sells 468 tickets on Friday, 539 on Saturday and 392 on Sunday.', parts=[
    P('a', 'It sells {b} tickets in all.', A('1399')), P('b', 'It sells {b} more tickets on Saturday than on Sunday.', A('147'))],
    why='(a) 468 + 539 = 1007, and 1007 + 392 = 1399. (b) 539 - 392 = 147.')
u.S(1, 'Siti has 64 beads. Wei has 29 beads. Each child gets 12 more beads.', parts=[
    P('a', 'Before, Siti has {b} more beads than Wei.', A('35')), P('b', 'After, Siti has {b} more beads than Wei.', A('35'))],
    why='Before: 64 - 29 = 35. After: Siti has 76 and Wei has 41, and 76 - 41 = 35. The gap stays the same because both children get the same number of beads.')
u.S(2, 'Ravi and Aisha have 140 coins in all. Ravi has 3 times as many coins as Aisha.', parts=[
    P('a', 'Aisha has {b} coins.', A('35')), P('b', 'Ravi has {b} coins.', A('105'))],
    space={'rows': ['Draw your model:', 'Working:', '']},
    why='There are 4 equal boxes in all. 140 ÷ 4 = 35, so 1 box is 35. Aisha has 1 box: 35 coins. Ravi has 3 boxes: 3 × 35 = 105 coins.')
u.S(2, 'Kumar and Wei have 90 stickers in all. Kumar has 18 more stickers than Wei.', parts=[
    P('a', 'Wei has {b} stickers.', A('36')), P('b', 'Kumar has {b} stickers.', A('54'))],
    space={'rows': ['Draw your model:', 'Working:', '']},
    why='Take away the extra 18 from the total: 90 - 18 = 72. Share the 72 into 2 equal parts: 36 each. Wei has 36. Kumar has 36 + 18 = 54. Check: 36 + 54 = 90.')
u.S(2, "Ravi's ribbon is 78 cm long. Mei's ribbon is 52 cm long. Ravi cuts a piece off his ribbon and gives it to Mei. Now both ribbons are the same length. How long is the piece? {b} cm", A('13'),
    space={'rows': ['Draw your model:', 'Working:']},
    why='The gap is 78 - 52 = 26 cm. The piece closes the gap from both sides, so it is half of the gap: 26 ÷ 2 = 13 cm. Check: 78 - 13 = 65 and 52 + 13 = 65.')
u.S(3, 'Ravi reads 85 pages on Monday. On Tuesday he reads 28 pages more than he does on Monday. On Wednesday he reads 17 pages fewer than on Tuesday.', parts=[
    P('a', 'He reads {b} pages on Tuesday.', A('113')), P('b', 'He reads {b} pages on Wednesday.', A('96')),
    P('c', 'He reads {b} pages in the 3 days.', A('294'))],
    why='(a) 85 + 28 = 113. (b) 113 - 17 = 96. (c) 85 + 113 + 96 = 294. Wednesday is compared with Tuesday, not with Monday.')
u.S(3, 'Mei has $50. She buys a book for $18.40 and a pen for $6.75. How much money does she have left? ${bw}', A('24.85'),
    why='First add what she spends: 18.40 + 6.75 = 25.15. Then 50.00 - 25.15 = 24.85. Check: 25.15 + 24.85 = 50.00.')
u.S(3, 'A zoo has 3 times as many monkeys as parrots. There are 48 monkeys.', parts=[
    P('a', 'There are {b} parrots.', A('16')), P('b', 'There are {b} monkeys and parrots in all.', A('64'))],
    space={'rows': ['Draw your model:']},
    why='Monkeys are 3 boxes and parrots are 1 box. 3 boxes are 48, so 1 box is 48 ÷ 3 = 16. Together they are 4 boxes: 4 × 16 = 64.')
u.S(3, 'A shop has 54 red pens. It has 18 fewer blue pens than red pens. Kumar says the shop has 54 + 18 = 72 blue pens.', parts=[
    P('a', 'Is Kumar right?   {circ:Yes|No}', A('No')), P('b', 'The shop has {b} blue pens.', A('36'))],
    why='There are fewer blue pens than red pens, so fewer than 54. Kumar added instead of subtracting. The right answer is 54 - 18 = 36.')
u.S(3, 'Siti saves $12 each week for 7 weeks. Then she spends $35. How much money does she have left? ${bw}', A('49'),
    space={'rows': ['Working:']},
    why='In 7 weeks she saves 7 × $12 = $84. Then 84 - 35 = 49. She has $49 left.')

# ---------------- Think harder
u.T('A library has 84 books on 2 shelves. The top shelf has 3 times as many books as the bottom shelf. The librarian moves some books from the top shelf to the bottom shelf. Now each shelf holds an equal number. How many does she move? {b}', A('21'), beyond='Giving to make them equal',
    hint='Find how many each shelf has at first. Then how many later.',
    space={'rows': ['Draw your model:', 'Working:']},
    why='At first there are 4 equal boxes: 84 ÷ 4 = 21, so the bottom shelf has 21 and the top shelf has 63. At the end each has 84 ÷ 2 = 42. She moves 63 - 42 = 21 books.')
u.T('Ali buys a pencil box and 2 pens for $14. Mei buys the same box and 5 pens for $23.', parts=[
    P('a', '1 pen costs ${bw}.', A('3')), P('b', 'The pencil box costs ${bw}.', A('8'))],
    hint='What is different between the 2 bills?',
    space={'rows': ['Draw your model:', 'Working:', '']},
    why='The second bill has 3 more pens and costs $23 - $14 = $9 more. So 3 pens cost $9 and 1 pen costs $3. The box costs $14 - 2 × $3 = $8. Check: 8 + 15 = 23.')
u.T('Ravi is 7 years old. His father is 35 years old. In how many years will his father be twice as old as Ravi? {b} years', A('21'), beyond='Ages and gaps',
    hint='The age gap never changes. Draw a bar for each age.',
    space={'rows': ['Draw your model:', 'Working:']},
    why='The gap is 35 - 7 = 28 years and it never changes. When the father is twice as old, Ravi is 1 box and his father is 2 boxes, so 1 box = the gap = 28. Ravi is 28, which is 21 years from now. Check: 28 and 56.')

# ---------------- Go further
u.G('Aisha, Kumar and Lily have 140 stickers in all. Kumar has 12 more stickers than Lily. Aisha has twice as many stickers as Kumar.', parts=[
    P('a', 'Lily has {b} stickers.', A('26')), P('b', 'Kumar has {b} stickers.', A('38')), P('c', 'Aisha has {b} stickers.', A('76'))],
    hint='Draw Lily as 1 bar. Build Kumar and Aisha from that bar.',
    partsrow=True, space={'rows': ['Draw your model:']},
    why='Lily is 1 box. Kumar is 1 box and 12. Aisha is 2 boxes and 24. In all: 4 boxes and 36 = 140. So 4 boxes = 104 and 1 box = 26. Lily 26, Kumar 38, Aisha 76. Check: 26 + 38 + 76 = 140.')
u.G('Beyond Level 3: One amount changes.\nA shop has 4 times as many red balloons as blue balloons. It sells 18 red balloons. Now the shop has the same number of red and blue balloons. How many balloons did the shop have at first? {b}', A('30'),
    hint='Draw blue as 1 box and red as 4 boxes. Selling 18 leaves 1 box.',
    space={'rows': ['Draw your model:']},
    why='Red is 4 boxes and blue is 1 box. After selling 18 red balloons, red is 1 box. So 3 boxes are 18, and 1 box is 6. At first there were 6 blue and 24 red: 30 balloons in all.')
u.G('Look at the bar model. Make up a story that fits it. Then solve your story.', A('24', 'Answers vary. Example: Ali and Ben have 60 stickers in all. Ben has 12 more stickers than Ali. Ali has 24 stickers and Ben has 36 stickers.'),
    figure=bar([{'label': 'Ali', 'segs': [seg(3, '', 'blank')]}, {'label': 'Ben', 'segs': [seg(3, '', 'blank'), seg(1, '12', 'ghost')], 'note': '60 in all'}], w=120, lab=100),
    hint='Pick things that fit: stickers, coins, cards or beads.',
    space={'rows': ['My story:', '', 'My answer:']},
    why='Check that the story says 60 in all and 12 more for Ben, and that the answer works. In the example, take away the 12: 60 - 12 = 48, and 48 ÷ 2 = 24. Ali has 24 and Ben has 24 + 12 = 36.')

# ---------------- Check yourself
u.C('A library has 2000 books. 735 books are lent out. 640 books are being mended. How many books are on the shelves? {b}', A('625'),
    why='2000 - 735 = 1265. Then 1265 - 640 = 625. Check: 735 + 640 + 625 = 2000.')
u.C('Ravi has 560 beads. Siti has 135 more beads than Ravi. How many beads do they have in all? {b}', A('1255'),
    why='Siti has 560 + 135 = 695 beads. Together: 560 + 695 = 1255.')
u.C('Siti and Kumar have 72 stamps in all. Siti has 5 times the number of stamps that Kumar has. How many stamps does Siti have? {b}', A('60'),
    why='There are 6 equal boxes in all. 72 ÷ 6 = 12, so 1 box is 12. Siti has 5 boxes: 5 × 12 = 60.')
u.C('Two boxes hold 50 pens in all. Box A has 8 more pens than Box B. How many pens are in Box A? {b}', A('29'),
    why='Take away the extra 8: 50 - 8 = 42. Share 42 into 2 equal parts: 21 each. Box B has 21 and Box A has 21 + 8 = 29.')
u.save()
