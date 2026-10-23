import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

def fr(*items, **kw):
    d = {'type': 'l2_frac', 'items': list(items)}
    d.update(kw)
    return d

learn = {
 'intro': 'A fraction names equal parts of one whole. The bottom number says how many equal parts the whole is cut into. The top number says how many parts we take.',
 'example': {
  'problem': 'Kumar cuts a pizza into 8 equal slices. He eats 3 slices. What fraction did he eat? What fraction is left?',
  'figure': fr({'kind': 'bar', 'n': 8, 'shaded': 3, 'w': 400}, width_mm=60), 'side': False,
  'steps': ['The slices are equal. There are 8 of them: the bottom number is 8.', 'He eats 3 slices: the top number is 3. He ate 3/8.', 'Slices left: 8 - 3 = 5. So 5/8 is left.', 'Check: 3/8 + 5/8 = 8/8 = 1 whole pizza.'],
  'answer': 'He ate 3/8. 5/8 is left.'},
 'example2': {
  'problem': 'The number line goes from 0 to 1 in 4 equal steps. What fraction does the arrow show?',
  'figure': fr({'kind': 'line', 'n': 4, 'arrows': [{'k': 3, 'label': '?'}], 'w': 320}, width_mm=62),
  'steps': ['Each step is 1/4.', 'The arrow is 3 steps from 0: 3/4.'],
  'answer': 'The arrow shows 3/4.'},
 'pair': True,
 'tight': True,
 'howto': {'title': 'How to name a fraction', 'steps': ['Check that the parts are equal.', 'Count all the parts: the bottom number.', 'Count the parts you take: the top number.', 'Same bottom number? Just add or subtract the tops.']},
 'facts': {'title': 'Remember', 'lines': ['More parts means smaller parts: 1/6 is less than 1/4.', 'Like fractions: 2/7 + 3/7 = 5/7. The bottom number stays.', 'All the parts make 1 whole: 7/7 = 1.']},
 'try': {'text': 'Mei cuts a cake into 10 equal slices and eats 3. The part of the cake left is {b}', 'answer': A('7/10'),
         'explanation': '10 - 3 = 7 slices are left. Each slice is 1/10, so 7/10 is left. Check: 3/10 + 7/10 = 10/10 = 1 whole.'}}

items = [
 I('start', 1, 'Each shape is cut into 4 parts. Is each shape cut into quarters (4 EQUAL parts)?',
   figure=fr({'kind': 'bar', 'n': 4, 'shaded': 1, 'w': 230, 'label': 'A'}, {'kind': 'bar', 'widths': [1, 1, 1, 3], 'shaded': 1, 'w': 230, 'label': 'B'},
             {'kind': 'circle', 'n': 4, 'shaded': 1, 'label': 'C', 'r': 62}, {'kind': 'circle', 'angles': [120, 90, 90, 60], 'shaded': 1, 'label': 'D', 'r': 62},
             {'kind': 'sq', 'style': 'diag', 'shaded': [0], 'label': 'E', 's': 112}, {'kind': 'sq', 'style': 'unequal', 'widths': [1, 1, 1, 3], 'shaded': [0], 'label': 'F', 's': 112}, max_w=1300, width_mm=150),
   partsrow=True, parts=[P('a', 'A   {circ:Yes|No}', 'Yes'), P('b', 'B   {circ:Yes|No}', 'No'), P('c', 'C   {circ:Yes|No}', 'Yes'), P('d', 'D   {circ:Yes|No}', 'No'), P('e', 'E   {circ:Yes|No}', 'Yes'), P('f', 'F   {circ:Yes|No}', 'No')],
   why='Quarters must be 4 parts of the SAME size. A, C and E are quarters. In B and F one part is much greater than the other three. In D the parts are not the same size. In E the four triangles are all the same size.'),
 I('start', 1, 'Write the shaded fraction. Write the fraction not shaded.',
   figure=fr({'kind': 'circle', 'n': 5, 'shaded': 2, 'label': 'A', 'r': 62}, {'kind': 'bar', 'n': 8, 'shaded': 6, 'w': 250, 'label': 'B'}, {'kind': 'bar', 'n': 12, 'shaded': 5, 'w': 300, 'label': 'C'}, max_w=860, width_mm=150),
   parts=[P('a', 'A: shaded {b}   not shaded {b}', ['2/5', '3/5'], '2/5 and 3/5'), P('b', 'B: shaded {b}   not shaded {b}', ['6/8', '2/8'], '6/8 and 2/8'), P('c', 'C: shaded {b}   not shaded {b}', ['5/12', '7/12'], '5/12 and 7/12'), P('d', 'To make 8/12 shaded in C, shade {b} more parts.', '3')],
   why='The bottom number is the number of equal parts. (a) 2/5 and 3/5. (b) 6/8 and 2/8. (c) 5/12 and 7/12. (d) 8/12 needs 8 shaded parts. 5 are shaded, so 3 more.'),
 I('start', 1, 'The whole is 1. Fill in the missing number.', partsrow=True, parts=[
   P('a', '6/6 = {b} whole', '1'), P('b', '1 whole = 9/{b}', '9'), P('c', '4/8 + {b}/8 = 1', '4')],
   why='(a) 6 sixths make 1 whole. (b) 1 whole cut into 9 equal parts is 9/9. (c) 1 whole is 8/8, and 8 - 4 = 4, so 4/8 + 4/8 = 1.'),
 I('start', 2, 'The fraction wall shows bars of the same length. One part of each bar is shaded.', figure=fr({'kind': 'wall', 'rows': [1, 2, 3, 4, 6, 8], 'shaded': {2: 0, 3: 0, 4: 0, 6: 0, 8: 0}, 'w': 480}, width_mm=120),
   parts=[P('a', 'Which is greater?   {circ:1/3|1/4}', '1/3'), P('b', 'Which is smaller?   {circ:1/6|1/8}', '1/8'),
          P('c', 'Smallest first:  1/2,  1/6,  1/4,  1/8      {ll}', ['1/8', '1/6', '1/4', '1/2'], '1/8, 1/6, 1/4, 1/2', lst=True),
          ],
   why='The more parts a bar is cut into, the smaller each part. (a) Thirds are greater than quarters. (b) Eighths are smaller than sixths. (c) Order: 1/8, 1/6, 1/4, 1/2.'),
 I('start', 2, 'The same bottom number means the same size parts. Circle the greater fraction.', partsrow=True, parts=[
   P('a', 'Circle:  {circ:3/10|6/10}', '6/10'), P('b', 'Circle:  {circ:7/12|5/12}', '7/12'),
   P('c', 'Smallest first:  6/7,  2/7,  4/7     {ll}', ['2/7', '4/7', '6/7'], '2/7, 4/7, 6/7', lst=True)],
   why='When the bottom numbers are the same, the parts are the same size, so more parts is greater. (a) 6/10 is greater than 3/10. (b) 7/12 is greater than 5/12. (c) 2/7, 4/7, 6/7.'),
 I('start', 2, 'Add or take away. The bottom number stays the same.', partsrow=True, parts=[
   P('a', '3/12 + 6/12 = {b}', '9/12'), P('b', '7/8 - 2/8 = {b}', '5/8'), P('c', '1 - 3/5 = {b}', '2/5'), P('d', '4/9 + {b} = 1', '5/9')],
   why='(a) 3 twelfths + 6 twelfths = 9 twelfths. (b) 7 eighths - 2 eighths = 5 eighths. (c) 1 whole is 5/5, and 5/5 - 3/5 = 2/5. (d) 1 whole is 9/9, and 9/9 - 4/9 = 5/9.'),
 I('start', 3, 'A pizza is cut into 10 equal slices. Siti eats the slices marked S. Ravi eats the slices marked R.', figure=fr({'kind': 'bar', 'n': 10, 'shaded': [], 'w': 480, 'marks': {0: 'S', 1: 'S', 2: 'S', 3: 'R', 4: 'R', 5: 'R', 6: 'R'}}, width_mm=130),
   parts=[P('a', 'They eat {b} of the pizza altogether.', '7/10'), P('b', '{b} of the pizza is left.', '3/10'), P('c', 'Who eats more?   {circ:Siti|Ravi}', 'Ravi'), P('d', 'Ravi eats {b} more than Siti.', '1/10')],
   why='Siti ate 3 slices and Ravi ate 4 slices. (a) 3/10 + 4/10 = 7/10. (b) 10/10 - 7/10 = 3/10. (c) 4 is more than 3, so Ravi. (d) 4/10 - 3/10 = 1/10.'),
 I('start', 3, 'A cake is shared equally among 5 children.', parts=[
   P('a', 'Each child gets {b} of the cake.', '1/5'), P('b', 'Kumar and Mei are 2 of the children. Together they get {b}.', '2/5'), P('c', 'The other children get {b} together.', '3/5')],
   why='(a) 5 equal shares: each is 1/5. (b) 1/5 + 1/5 = 2/5. (c) The whole is 5/5. 5/5 - 2/5 = 3/5.'),
 I('start', 3, 'The number line goes from 0 to 1. It is cut into 8 equal steps.', figure=fr({'kind': 'line', 'n': 8, 'arrows': [{'k': 3, 'label': 'A'}, {'k': 7, 'label': 'B'}], 'w': 560}, width_mm=150),
   parts=[P('a', 'Arrow A shows {b}', '3/8'), P('b', 'Arrow B shows {b}', '7/8')],
   why='Each step is 1/8. (a) A is 3 steps from 0: 3/8. (b) B is 7 steps from 0: 7/8.'),
 # Think harder
 I('think', 4, 'Ravi and Siti each have a pizza of the same size. Ravi eats 3/4 of his pizza. Siti eats 5/8 of hers.',
   figure=fr({'kind': 'bar', 'n': 4, 'shaded': 3, 'w': 420, 'label': 'Ravi: 3/4'}, {'kind': 'bar', 'n': 8, 'shaded': 5, 'w': 420, 'label': 'Siti: 5/8'}, max_w=460, width_mm=80),
   partsrow=True, parts=[P('a', 'Who eats more?   {circ:Ravi|Siti}', 'Ravi'), P('b', 'How much more? {b}', '1/8')],
   hint='Line up the bars. Cut each quarter in 2 equal parts.',
   why='The bars are the same length. 3/4 of the first bar covers 6 of the small eighths, because each quarter is 2 eighths. Siti eats 5 eighths. Ravi eats 6 eighths, so Ravi eats 1/8 more.'),
 I('think', 4, 'Mei eats 1/4 of a pizza. Then Ali eats half of what is left.',
   figure=fr({'kind': 'bar', 'n': 8, 'shaded': [], 'w': 420, 'label': 'Pizza bar'}, width_mm=70),
   partsrow=True, parts=[P('a', 'After Mei, {b} is left.', '3/4'), P('b', 'Ali eats {b} of the pizza.', '3/8'), P('c', 'Now {b} is left.', '3/8')],
   hint='Cut each part in 2 equal parts to make eighths.',
   why='(a) 1/4 eaten, so 3/4 is left. On the bar of 8 parts, 1/4 is 2 parts, and 6 parts are left. (b) Half of 6 parts is 3 parts: Ali eats 3/8. (c) 6 - 3 = 3 parts are left: 3/8.'),
 I('think', 4, 'Two fractions have the bottom number 12. Together they make 1 whole. The greater one is 6/12 more.', partsrow=True, parts=[
   P('a', 'The smaller fraction is {b}', '3/12'), P('b', 'The greater fraction is {b}', '9/12')],
   hint='Take away the extra 6/12. Share what is left.',
   why='The whole is 12/12. Take away the extra 6/12: 6/12 is left. Share it between the two equal parts: 3/12 and 3/12. Give the extra back to one of them: 3/12 and 9/12. Check: 3/12 + 9/12 = 12/12.'),
 # Go further
 I('go', 5, 'Equal fractions. Different fractions can cover the same length. 1/2 and 2/4 and 4/8 are equal.', beyond='Equal fractions', partsrow=True, parts=[
   P('a', '1/2 = {b}/6', '3'), P('b', '2/3 = {b}/6', '4'), P('c', '3/4 = {b}/8', '6')],
   hint='Line up 2 bars of the same length. Cut one into more parts.',
   why='(a) A half of 6 sixths is 3 sixths. (b) A third is 2 sixths, so 2 thirds are 4 sixths. (c) A quarter is 2 eighths, so 3 quarters are 6 eighths.'),
 I('go', 5, 'Nine equal pieces of cake are shared by 3 children. The shares must all be different. Each share is 1 piece or more.', parts=[
   P('a', 'How many different ways are there? {b}', '3'), P('b', 'In the way where the greatest share is 6/9, the other shares are {b}/9 and {b}/9.', ['1', '2'], '1/9 and 2/9')],
   space={'rows': ['Working:']}, hint='Start with the smallest share, 1 piece. Then try 2.',
   why='The 3 different numbers of pieces add to 9. With 1 piece for the smallest: 1 + 2 + 6 and 1 + 3 + 5. With 2 pieces: 2 + 3 + 4. 1 + 4 + 4 repeats a number. So 3 ways. The way with 6/9 is 1/9, 2/9 and 6/9.'),
 I('go', 5, 'Make your own fair-share story. Picture a cake with 8 equal pieces. Three people eat different shares and some is left. Write each share as a fraction. Many answers are right.', value='open',
   atext='Open. Example: Ali eats 3/8, Mei eats 2/8, Ben eats 1/8 and 2/8 is left. 3 + 2 + 1 + 2 = 8 eighths = 1 whole.', space={'rows': ['My story:', 'Check: shares and what is left make 1 whole:']},
   hint='Add all the shares and what is left. Do you get 8/8?',
   why='A good story has shares and leftovers that add to 8/8. Example: 3/8 + 2/8 + 1/8 + 2/8 = 8/8 = 1 whole.'),
 I('go', 5, 'My top number is 1. I am less than 1/3 and more than 1/9. Which fractions fit? Find ALL of them.', parts=[
   P('a', 'I could be:  {ll}', ['1/4', '1/5', '1/6', '1/7', '1/8'], '1/4, 1/5, 1/6, 1/7, 1/8', lst=True), P('b', 'How many answers are there? {b}', '5')],
   hint='Greater bottom number, smaller part. Try 1/4, 1/5 ...',
   why='With 1 on top, the greater the bottom number, the smaller the fraction. 1/3 is too big and 1/9 is too small. 1/4, 1/5, 1/6, 1/7 and 1/8 are in between: 5 answers.'),
 # Check yourself
 I('quiz', 0, 'What fraction is shaded? {b}', figure=fr({'kind': 'bar', 'n': 8, 'shaded': 5, 'w': 360}, width_mm=60), figright=True, value='5/8', why='The bar has 8 equal parts. 5 are shaded. The fraction is 5/8.'),
 I('quiz', 0, 'Which is greater?   {circ:1/5|1/9}', value='1/5', why='The more parts a whole is cut into, the smaller each part. 5 parts are greater than 9 parts, so 1/5 is greater.'),
 I('quiz', 0, '2/7 + 4/7 = {b}', value='6/7', why='2 sevenths + 4 sevenths = 6 sevenths. The bottom number stays 7.'),
 I('quiz', 0, 'A pizza has 12 slices. Ali eats 5/12 and Mei eats 3/12. What is left, in twelfths? {b}', value='4/12', why='5/12 + 3/12 = 8/12 eaten. 12/12 - 8/12 = 4/12 is left.'),
]
build(7, 'Fair shares', 'Fractions', 'I can name fractions of a whole. I can compare fractions and add like fractions. I can solve fair-sharing stories with a bar.', learn, items, snug=['start1', 'start2', 'start3'])
