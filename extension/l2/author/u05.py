import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

def mach(*steps, **kw):
    d = {'type': 'l2_machine', 'steps': list(steps)}
    d.update(kw)
    return d

def mrows(rows, **kw):
    d = {'type': 'l2_machine', 'rows': [{'label': l, 'steps': st} for l, st in rows]}
    d.update(kw)
    return d

learn = {
 'intro': 'A number machine changes a number, one step at a time. To find what went IN, work backwards. Undo the LAST step first. Use the opposite: + and - undo each other, and so do × and ÷.',
 'example': {
  'problem': 'Ali picks a secret number. He multiplies it by 3, then adds 5. He gets 29. What is his number?',
  'figure': mach('?', '× 3', '+ 5', '29', width_mm=150),
  'steps': ['Undo the last step. It was + 5, so take away 5: 29 - 5 = 24.', 'Undo the first step. It was × 3, so divide by 3: 24 ÷ 3 = 8.', 'Check going forwards: 8 × 3 = 24, then 24 + 5 = 29.'],
  'answer': 'The secret number is 8.'},
 'howto': {'title': 'How to work backwards', 'steps': ['Draw the machine.', 'Start at the OUT. Undo the last step first.', 'Use the opposite step.', 'Check going forwards.']},
 'facts': {'title': 'Opposites', 'lines': ['+ 6 is undone by - 6.', '× 4 is undone by ÷ 4.', 'Undo in the opposite order.']},
 'try': {'text': 'Mei picks a secret number. She multiplies it by 5, then takes away 8. She gets 32. What is her number? {b}', 'answer': A('8'),
         'explanation': 'Undo - 8 with + 8: 32 + 8 = 40. Undo × 5 with ÷ 5: 40 ÷ 5 = 8. Check: 8 × 5 = 40 and 40 - 8 = 32.'}}

items = [
 I('start', 1, 'What is my number? Write it in the box.', partsrow=True, parts=[
   P('a', 'I add 27. I get 61.   {b}', '34'), P('b', 'I multiply by 5. I get 35.   {b}', '7'), P('c', 'I divide by 4. I get 9.   {b}', '36'), P('d', 'I take away 18. I get 25.   {b}', '43')],
   why='Use the opposite step. (a) 61 - 27 = 34. (b) 35 ÷ 5 = 7. (c) 9 × 4 = 36. (d) 25 + 18 = 43.'),
 I('start', 1, 'Circle the step that undoes the first one.', partsrow=True, parts=[
   P('a', '+ 7 is undone by   {circ:+ 7|- 7|× 7}', '- 7'), P('b', '× 5 is undone by   {circ:× 5|÷ 5|- 5}', '÷ 5'), P('c', '- 12 is undone by   {circ:- 12|+ 12|÷ 12}', '+ 12'), P('d', '÷ 3 is undone by   {circ:÷ 3|+ 3|× 3}', '× 3')],
   why='The opposite of adding is taking away, and the opposite of multiplying is dividing. (a) - 7. (b) ÷ 5. (c) + 12. (d) × 3.'),
 I('start', 1, 'Find the number that went IN. Undo the last step first.', figure=mrows([('(a)', ['?', '× 2', '+ 9', '25']), ('(b)', ['?', '- 6', '× 4', '28']), ('(c)', ['?', '÷ 5', '+ 7', '11'])], width_mm=150),
   partsrow=True, parts=[P('a', 'IN {b}', '8'), P('b', 'IN {b}', '13'), P('c', 'IN {b}', '20')],
   why='(a) 25 - 9 = 16, then 16 ÷ 2 = 8. Check: 8 × 2 = 16, 16 + 9 = 25. (b) 28 ÷ 4 = 7, then 7 + 6 = 13. Check: 13 - 6 = 7, 7 × 4 = 28. (c) 11 - 7 = 4, then 4 × 5 = 20. Check: 20 ÷ 5 = 4, 4 + 7 = 11.'),
 I('start', 2, 'This machine does × 4, then - 1. Fill in the table.', figure={'type': 'l2_table', 'cols': ['IN', '3', '6', None, None], 'rows': [['OUT', None, None, '31', '39']], 'first_bold': True, 'widths': [1.4, 1, 1, 1, 1], 'width_mm': 120},
   parts=[P('a', 'Write the 4 missing numbers. Do the OUT of IN 3 and 6 first, then work backwards for 31 and 39.', ['11', '23', '8', '10'], '11 and 23 in the OUT row, 8 and 10 in the IN row', lst=True)],
   why='IN 3: 3 × 4 = 12, 12 - 1 = 11. IN 6: 6 × 4 = 24, 24 - 1 = 23. OUT 31: 31 + 1 = 32, 32 ÷ 4 = 8. OUT 39: 39 + 1 = 40, 40 ÷ 4 = 10.'),
 I('start', 2, 'A fair machine gives stickers for tokens. Each token gives the same number of stickers, plus a bonus. 3 tokens give 11 stickers. 6 tokens give 17.', figure={'type': 'l2_table', 'cols': ['Tokens', '3', '6', '10'], 'rows': [['Stickers', '11', '17', None]], 'first_bold': True, 'widths': [1.4, 1, 1, 1], 'width_mm': 100},
   parts=[P('a', 'Each token gives   {circ:2|3|4}   stickers.', '2'), P('b', 'The bonus is {b} stickers.', '5'), P('c', '10 tokens give {b} stickers.', '25')],
   why='Try 2 stickers a token: 3 tokens give 6, and 11 - 6 = 5 is the bonus. Test 6 tokens: 12 + 5 = 17. It fits. 3 and 4 a token do not fit both. 10 tokens: 20 + 5 = 25.'),
 I('start', 2, 'Ali had some marbles. He lost 18 in a game. Then he won 25 marbles. Now he has 60.', figure=mach('?', '- 18', '+ 25', '60', width_mm=150),
   parts=[P('a', 'Before he won 25, Ali had {b} marbles.', '35'), P('b', 'At first Ali had {b} marbles.', '53'), P('c', 'Check: 53 - 18 = {b}, then + 25 = {b}', ['35', '60'], '35, then 60')],
   why='Undo the last step: 60 - 25 = 35. Undo the first step: 35 + 18 = 53. Check: 53 - 18 = 35, then 35 + 25 = 60.'),
 I('start', 3, 'Kumar puts his stickers into 4 boxes. Every box has the same number. He takes 3 stickers out of box 4. Now box 4 has 7 stickers.',
   figure={'type': 'l2_bar', 'rows': [{'label': 'Box 1', 'segs': [{'w': 7, 'unknown': True, 't': '?'}]}, {'label': 'Box 2', 'segs': [{'w': 7, 'unknown': True, 't': '?'}]}, {'label': 'Box 3', 'segs': [{'w': 7, 'unknown': True, 't': '?'}]},
                                                                          {'label': 'Box 4', 'segs': [{'w': 5, 't': '7'}, {'w': 2, 'hatch': True, 't': '3'}]}], 'width_units': 380, 'width_mm': 100},
   parts=[P('a', 'Each box had {b} stickers at first.', '10'), P('b', 'Kumar has {b} stickers altogether.', '40')],
   why='Box 4 had 7 + 3 = 10 stickers before he took 3 out. Every box had the same, so each box had 10. 4 boxes: 4 × 10 = 40 stickers.'),
 I('start', 3, 'Mei had some stickers. She bought 12 more. Then she put them equally into 4 albums, 5 in each album.', figure=mach('?', '+ 12', '÷ 4', '5', width_mm=150),
   parts=[P('a', 'After buying 12 more, Mei had {b} stickers.', '20'), P('b', 'At first Mei had {b} stickers.', '8')],
   why='4 albums with 5 stickers each: 4 × 5 = 20 stickers. That is after buying 12 more, so at first she had 20 - 12 = 8. Check: 8 + 12 = 20 and 20 ÷ 4 = 5.'),
 I('start', 1, 'Fill in the missing number.', partsrow=True, parts=[
   P('a', '{b} ÷ 2 + 7 = 15', '16'), P('b', '4 × {b} - 5 = 19', '6'), P('c', '{b} × 10 + 8 = 78', '7')],
   why='Undo the last step first. (a) 15 - 7 = 8, then 8 × 2 = 16. (b) 19 + 5 = 24, then 24 ÷ 4 = 6. (c) 78 - 8 = 70, then 70 ÷ 10 = 7.'),
 I('start', 3, 'Lily had some money. She bought a pen for $3 and a book for $8. She has $12 left.', parts=[
   P('a', 'Lily spent $ {b} altogether.', '11'), P('b', 'At first Lily had $ {b}', '23')],
   why='(a) $3 + $8 = $11 spent. (b) Undo the spending: $12 + $11 = $23. Check: 23 - 3 = 20, 20 - 8 = 12.'),
 # Think harder
 I('think', 4, 'Mei, Lily and Aisha have 51 beads altogether. Lily has 6 more than Mei. Aisha has 9 more than Mei.',
   figure={'type': 'l2_bar', 'rows': [{'label': 'Mei', 'segs': [{'w': 5, 'unknown': True, 't': '?'}]}, {'label': 'Lily', 'segs': [{'w': 5, 'unknown': True, 't': '?'}, {'w': 2, 't': '6'}]}, {'label': 'Aisha', 'segs': [{'w': 5, 'unknown': True, 't': '?'}, {'w': 3, 't': '9'}]}],
           'brace': {'text': '51', 'rows': [0, 2]}, 'width_units': 400, 'width_mm': 94},
   partsrow=True, parts=[P('a', 'Mei has {b} beads.', '12'), P('b', 'Lily has {b} beads.', '18'), P('c', 'Aisha has {b} beads.', '21')],
   hint='Take off the extra bits. Then share the rest equally.',
   why='Take away the extra 6 and 9: 51 - 6 - 9 = 36. Now 3 equal bars share 36, so each is 36 ÷ 3 = 12. Mei has 12, Lily 12 + 6 = 18 and Aisha 12 + 9 = 21. Check: 12 + 18 + 21 = 51.'),
 I('think', 4, 'Aisha had some stickers. She used 8 on a card. Then she got as many stickers as she had left. Now she has 30.',
   figure={'type': 'l2_bar', 'rows': [{'label': 'Start', 'segs': [{'w': 6, 'unknown': True, 't': '?'}]}, {'label': 'Then', 'segs': [{'w': 4, 'unknown': True, 't': '?'}, {'w': 2, 't': '8'}]}, {'label': 'Now', 'segs': [{'w': 4, 'unknown': True, 't': '?'}, {'w': 4, 'unknown': True, 't': '?'}]}],
           'brace': {'text': '30', 'rows': [2, 2]}, 'width_units': 400, 'width_mm': 92},
   partsrow=True, parts=[P('a', 'After the card, Aisha had {b} stickers.', '15'), P('b', 'At first she had {b} stickers.', '23')],
   hint='Now she has 2 equal parts. Find one part first.',
   why='Now she has twice the number she had after the card, so 30 is 2 equal parts: 30 ÷ 2 = 15. After the card she had 15. At first she had 15 + 8 = 23. Check: 23 - 8 = 15, then 15 + 15 = 30.'),
 I('think', 4, 'A machine does × 4, then + 1. Could it give this OUT? Try IN 1, 2, 3 ... first.', partsrow=True, parts=[
   P('a', '29   {circ:Yes|No}', 'Yes'), P('b', '30   {circ:Yes|No}', 'No'), P('c', '33   {circ:Yes|No}', 'Yes'), P('d', '42   {circ:Yes|No}', 'No')],
   hint='Write the first OUT numbers. What do you see?',
   why='IN 1, 2, 3, 4 give 5, 9, 13, 17: always 1 more than the 4 times table. 29 = 28 + 1: yes. 30 is skipped (29, 33): no. 33 = 32 + 1: yes. 42 is skipped (41, 45): no.'),
 # Go further
 I('go', 5, 'A letter can stand for a mystery number. Let n be the mystery number. 3 × n + 4 = 25 means: 3 times the number, plus 4, makes 25.', beyond='Letters for numbers', parts=[
   P('a', '3 × n + 4 = 25. n = {b}', '7'), P('b', '5 × n - 3 = 27. n = {b}', '6'), P('c', 'n ÷ 2 + 8 = 13. n = {b}', '10')],
   hint='Work backwards, just like a machine.',
   why='(a) 25 - 4 = 21, 21 ÷ 3 = 7. (b) 27 + 3 = 30, 30 ÷ 5 = 6. (c) 13 - 8 = 5, 5 × 2 = 10.'),
 I('go', 5, 'Three jars have 36 beans altogether. 4 beans move from jar A to jar B. Then 6 beans move from jar B to jar C. Now every jar has the same number.', parts=[
   P('a', 'Now each jar has {b} beans.', '12'), P('b', 'At first: jar A {b}, jar B {b}, jar C {b}', ['16', '14', '6'], '16, 14 and 6')],
   hint='Undo the last move first. Jar C gave nothing, it got 6.',
   why='(a) 36 ÷ 3 = 12. (b) Undo B to C: jar C had 12 - 6 = 6 and jar B had 12 + 6 = 18. Undo A to B: jar B had 18 - 4 = 14 and jar A had 12 + 4 = 16. Check: 16 + 14 + 6 = 36.'),
 I('go', 5, 'Make your own riddle. "I think of a number. I ... then I ... I get ..." The mystery number must be 12. Many answers work.', value='open',
   atext='Open. Example: I think of a number. I add 7, then multiply by 2. I get 38. (38 ÷ 2 = 19, 19 - 7 = 12.)',
   space={'rows': ['My riddle:']},
   why='Start at 12 and go forwards: 12 + 7 = 19, 19 × 2 = 38. The riddle ends at 38. To solve it, work backwards from 38.'),
 I('go', 5, 'Machine A does × 2, then + 3. Machine B does - 5, then × 3. The OUT of A goes into B. The final OUT is 36.',
   figure=mach('?', '× 2', '+ 3', '- 5', '× 3', '36', width_mm=120), figside=False,
   partsrow=True, parts=[P('a', 'The OUT of machine A was {b}', '17'), P('b', 'The number that went into A was {b}', '7')],
   hint='Undo machine B first. Then undo machine A.',
   why='Undo B: 36 ÷ 3 = 12, then 12 + 5 = 17. That is the OUT of A. Undo A: 17 - 3 = 14, then 14 ÷ 2 = 7. Check: 7 → 14 → 17 → 12 → 36.'),
 # Check yourself
 I('quiz', 0, 'I multiply a number by 4, then add 6. I get 38. My number: {b}', value='8', why='38 - 6 = 32, then 32 ÷ 4 = 8. Check: 8 × 4 = 32, 32 + 6 = 38.'),
 I('quiz', 0, 'Kumar gave away 14 stickers, then bought 9. Now 31. At first: {b}', value='36', why='Undo buying 9: 31 - 9 = 22. Undo giving away 14: 22 + 14 = 36. Check: 36 - 14 = 22, 22 + 9 = 31.'),
 I('quiz', 0, 'Kumar doubles his number, then adds 9. He gets 25. His number: {b}', value='8', why='25 - 9 = 16, then 16 ÷ 2 = 8. Check: 8 × 2 = 16, 16 + 9 = 25.'),
 I('quiz', 0, '5 equal bags. Bag 5 has 4 left after losing 6. Pens in all: {b}', value='50', why='Bag 5 had 4 + 6 = 10 pens before. Every bag had 10, so 5 × 10 = 50 pens.'),
]
build(5, 'Mystery number machines', 'Working backwards', 'I can find a mystery number by working backwards. I undo the last step first. I can use bars for before-and-after stories.', learn, items, snug=['start1', 'start2', 'start3'])
