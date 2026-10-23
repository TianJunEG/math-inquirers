from lib import *
U = 'L4U04'
FB = lambda rows, **kw: dict({'type': 'l4_bars', 'rows': rows, 'width_mm': 100, 'unit': 44, 'gap': 14, 'row_h': 40}, **kw)
def frow(label, n, shaded, **kw):
    return dict({'label': label, 'segs': [{'u': 1, 'k': 'h' if i < shaded else 'p'} for i in range(n)]}, **kw)

learn = {
 'intro': 'A fraction bar shows equal parts of one whole. A fraction of a set uses a bar model: divide the total by the denominator to find 1 unit.',
 'example': {
  'problem': 'Write 17/5 as a mixed number.',
  'figure': FB([frow('', 5, 5), frow('', 5, 5), frow('', 5, 5), frow('', 5, 2)], width_mm=70, unit=40),
  'steps': ['5 fifths make 1 whole. Divide: 17 ÷ 5 = 3 with 2 left.', 'There are 3 wholes and 2 fifths.'],
  'answer': '17/5 = 3 2/5.'},
 'example2': {
  'problem': 'There are 48 stickers. 5/6 of them are gold. How many are gold?',
  'figure': FB([{'label': '', 'segs': [{'u': 1, 'k': 'h'}] * 5 + [{'u': 1}], 'brace': {'a': 0, 'b': 6, 'text': '48'}}], width_mm=82, unit=44),
  'steps': ['6 units = 48, so 1 unit = 48 ÷ 6 = 8.', 'Gold is 5 units: 5 × 8 = 40.'],
  'answer': '40 stickers are gold.'},
 'pair': True, 'tight': True,
 'howto': {'title': 'How to do it',
           'steps': ['Improper to mixed: divide the top by the bottom.',
                     'Mixed to improper: whole × bottom + top, over the bottom.',
                     'Fraction of a set: 1 unit is the total ÷ the bottom number.']},
 'facts': {'title': 'Comparing', 'lines': ['Same bottom: the greater top is more.', 'Same top: the smaller bottom is more.', 'Or compare with 1/2.', 'Equivalent: multiply or divide top and bottom by the same number.', 'Whole from a part: 3 units = 36, so 1 unit = 12.']},
 'try': {'id': U + '-L01', 'text': 'Write 3 4/5 as an improper fraction. {b} / {b}',
         'answer': A(19, 5, text='19/5'),
         'explanation': '3 wholes are 3 × 5 = 15 fifths. 15 fifths and 4 more fifths make 19 fifths: 19/5.'}}

S, T, G, C = [], [], [], []
S.append(item(U+'-S01', 'start', 1, 'Each bar is 1 whole cut into sixths. Look at the shaded parts.',
  fig=FB([frow('', 6, 6), frow('', 6, 6), frow('', 6, 5)], width_mm=70, unit=44, row_h=34, gap=10),
  parts=[P('a', 'How many sixths are shaded? {b} sixths', A(17)), P('b', 'Write it as a mixed number. {b} {b}/{b}', A(2, 5, 6, text='2 5/6'))],
  why='There are 6 + 6 + 5 = 17 sixths shaded. 2 whole bars are shaded and 5 of the 6 parts of the third bar: 2 5/6.'))
S.append(item(U+'-S02', 'start', 1, 'Write each as a mixed number.',
  parts=[P('a', '19/4 = {b} {b}/{b}', A(4, 3, 4, text='4 3/4')), P('b', '23/6 = {b} {b}/{b}', A(3, 5, 6, text='3 5/6')),
         P('c', '31/8 = {b} {b}/{b}', A(3, 7, 8, text='3 7/8')), P('d', '40/5 = {b}', A(8))],
  partsrow=True,
  why='(a) 19 ÷ 4 = 4 remainder 3. (b) 23 ÷ 6 = 3 remainder 5. (c) 31 ÷ 8 = 3 remainder 7. (d) 40 ÷ 5 = 8 with nothing left, so it is exactly 8.'))
S.append(item(U+'-S03', 'start', 1, 'Write each as an improper fraction.',
  parts=[P('a', '3 2/5 = {b}/{b}', A(17, 5, text='17/5')), P('b', '5 1/3 = {b}/{b}', A(16, 3, text='16/3')), P('c', '2 7/8 = {b}/{b}', A(23, 8, text='23/8'))],
  partsrow=True,
  why='(a) 3 × 5 + 2 = 17 fifths. (b) 5 × 3 + 1 = 16 thirds. (c) 2 × 8 + 7 = 23 eighths.'))
S.append(item(U+'-S04', 'start', 1, 'A box has 36 pencils. 5/9 of them are red.',
  fig=FB([{'label': '', 'segs': [{'u': 1, 'k': 'h'}] * 5 + [{'u': 1}] * 4, 'brace': {'a': 0, 'b': 9, 'text': '36 pencils'}}], width_mm=120, unit=40),
  parts=[P('a', 'How many pencils are red? {b} pencils', A(20)), P('b', 'How many are not red? {b} pencils', A(16))],
  why='9 units = 36, so 1 unit = 36 ÷ 9 = 4. Red is 5 units: 5 × 4 = 20 pencils. Not red is 4 units: 4 × 4 = 16 pencils.'))
S.append(item(U+'-S05', 'start', 2, 'The number line is marked in thirds. Write the number each arrow shows.',
  fig={'type': 'l4_numline', 'min': 0, 'max': 3, 'minor': 1 / 3, 'major': 1, 'labels': {0: '0', 1: '1', 2: '2', 3: '3'}, 'labels_only': True,
       'marks': [{'v': 2 / 3, 'kind': 'arrow', 'text': 'A'}, {'v': 4 / 3, 'kind': 'arrow', 'text': 'B'}, {'v': 8 / 3, 'kind': 'arrow', 'text': 'C'}], 'width_mm': 150, 'W': 700},
  parts=[P('a', 'A = {b}/{b}', A(2, 3, text='2/3')), P('b', 'B = {b} {b}/{b}', A(1, 1, 3, text='1 1/3')), P('c', 'C as an improper fraction = {b}/{b}', A(8, 3, text='8/3'))],
  partsrow=True,
  why='Each step is 1/3. A is 2 steps from 0: 2/3. B is 1 whole and 1 more step: 1 1/3. C is 8 steps from 0, so 8/3, which is 2 2/3.'))
S.append(item(U+'-S06', 'start', 2, 'Mei has read 3/7 of her book. She has read 36 pages.',
  parts=[P('a', 'Pages in the whole book: {b}', A(84)), P('b', 'How many pages are left to read? {b} pages', A(48))],
  why='3 units = 36 pages, so 1 unit = 12 pages. The whole book is 7 units: 7 × 12 = 84 pages. Left is 4 units: 4 × 12 = 48 pages.',
  space={'rows': ['Draw a bar model here.', '']}))
S.append(item(U+'-S07', 'start', 2, 'Circle the correct sign.',
  parts=[P('a', '3/4  {circ:>|<}  5/8', A('>')), P('b', '4/6  {circ:>|<}  7/12', A('>')),
         P('c', '3/8  {circ:>|<}  5/9', A('<')), P('d', '5/6  {circ:>|<}  5/8', A('>'))],
  partsrow=True,
  why='(a) 3/4 = 6/8, and 6/8 is more than 5/8. (b) 4/6 = 8/12, and 8/12 is more than 7/12. (c) 3/8 is less than 1/2 and 5/9 is more than 1/2. (d) Both have 5 parts, and sixths are larger than eighths.'))
S.append(item(U+'-S08', 'start', 2, 'Write the fractions in order. Begin with the smallest.\n3/4   2/3   5/12   1/2\n{ll}',
  ans=A('5/12', '1/2', '2/3', '3/4'),
  why='Write each as twelfths: 3/4 = 9/12, 2/3 = 8/12, 5/12, 1/2 = 6/12. In order: 5/12, 6/12, 8/12, 9/12.'))
S.append(item(U+'-S09', 'start', 3, 'Fill in the missing numbers.',
  parts=[P('a', '2/3 = {b}/12', A(8)), P('b', '15/20 = 3/{b}', A(4)), P('c', '9/12 = {b}/4', A(3)), P('d', '4/5 = 12/{b}', A(15))],
  partsrow=True,
  why='(a) 3 × 4 = 12, so 2 × 4 = 8. (b) 15 ÷ 5 = 3, so 20 ÷ 5 = 4. (c) 12 ÷ 3 = 4, so 9 ÷ 3 = 3. (d) 4 × 3 = 12, so 5 × 3 = 15.'))
S.append(item(U+'-S10', 'start', 3, 'Each pizza is cut into 8 slices. The children eat 27 slices.',
  parts=[P('a', 'How many pizzas is that? {b} {b}/{b} pizzas', A(3, 3, 8, text='3 3/8 pizzas')),
         P('b', 'How many slices are in 5 whole pizzas? {b} slices', A(40)),
         P('c', 'How many more slices make 4 whole pizzas? {b} slices', A(5))],
  why='(a) 27 ÷ 8 = 3 remainder 3, so 3 3/8 pizzas. (b) 5 × 8 = 40. (c) 4 pizzas are 32 slices, and 32 − 27 = 5.'))
S.append(item(U+'-S11', 'start', 3, 'A jug holds 2 1/2 litres of juice. Each cup holds 1/4 litre.',
  parts=[P('a', 'How many cups can a full jug fill? {b} cups', A(10)), P('b', 'Ravi fills 6 cups. How much juice is left? {b} litre', A(1))],
  why='Each litre has 4 quarters. 2 1/2 litres is 10 quarters, so 10 cups. After 6 cups, 4 quarters are left, and 4 quarters make 1 litre.',
  space={'rows': ['Working:']}))
S.append(item(U+'-S12', 'start', 3, 'Aisha has 48 stickers. Mei gets 1/4 of the stickers. Ben gets 1/3 of the stickers that are left. How many stickers does Aisha keep? {b}',
  ans=A(24), why='1/4 of 48 is 12, so she has 48 − 12 = 36 left. 1/3 of 36 is 12. Then 36 − 12 = 24 stickers.',
  space={'rows': ['Working:', '']}))

S.append(item(U+'-S13', 'start', 3, 'How many?',
  parts=[P('a', 'quarters in 5 wholes: {b}', A(20)), P('b', 'sixths in 3 wholes: {b}', A(18)), P('c', 'halves in 2 1/2: {b}', A(5))],
  why='(a) 5 × 4 = 20. (b) 3 × 6 = 18. (c) 2 wholes make 4 halves, and 1/2 makes 1 more half: 5 halves.'))

T.append(item(U+'-T01', 'think', 4, 'A fraction is equal to 2/3. Its top and bottom numbers add up to 35. Find the fraction.\n{b}/{b}',
  ans=A(14, 21, text='14/21'), hint='Write 2/3, 4/6, 6/9 and so on. Add the top and bottom each time.',
  why='The fractions equal to 2/3 are 4/6, 6/9, 8/12 and so on. Their top and bottom add up to 10, 15, 20 and so on, in fives. 35 = 7 × 5, so the fraction is 2 × 7 over 3 × 7 = 14/21.',
  space={'rows': ['List:', '', '']}))
T.append(item(U+'-T02', 'think', 4, 'A team scored some goals. Ali scored 2/5 of them and Ben scored 1/4 of them. Kumar scored the other 21 goals. How many goals did the team score? {b}',
  ans=A(60), hint='Which number do 5 and 4 both go into?',
  why='2/5 = 8/20 and 1/4 = 5/20, so Ali and Ben scored 13/20. Kumar scored 7/20. 7 units = 21, so 1 unit = 3 and 20 units = 60 goals.',
  space={'rows': ['Draw a bar model here.', '', '', '']}))
T.append(item(U+'-T03', 'think', 4, 'In a class, 1/3 of the children are boys. 3/4 of the girls wear glasses. 18 girls wear glasses. How many children are in the class? {b}',
  ans=A(36), hint='The girls are 2/3 of the class. Find 3/4 of 2/3.',
  why='The girls are 2/3 of the class. 3/4 of 2/3 is 6/12 = 1/2 of the class. 1/2 of the class is 18, so the class has 2 × 18 = 36 children.',
  space={'rows': ['Draw a bar model here.', '', '']}))

G.append(item(U+'-G01', 'go', 5, 'Think about fractions with denominator 20 that are greater than 1/4 and less than 3/5.',
  parts=[P('a', 'How many are there? {b}', A(6)), P('b', 'Which one is equal to 1/2? {b}/20', A(10))],
  hint='Write 1/4 and 3/5 as twentieths. List the ones in between.',
  why='1/4 = 5/20 and 3/5 = 12/20. The fractions in between are 6/20, 7/20, 8/20, 9/20, 10/20 and 11/20: 6 fractions. 10/20 = 1/2.'))
G.append(item(U+'-G02', 'go', 5, 'Beyond Level 4: Unit fractions\nWrite each fraction as a sum of 2 different unit fractions. A unit fraction has 1 on top.',
  parts=[P('a', '5/6 = 1/{b} + 1/{b}', A(2, 3, text='1/2 + 1/3')), P('b', '3/4 = 1/{b} + 1/{b}', A(2, 4, text='1/2 + 1/4')),
         P('c', '7/10 = 1/{b} + 1/{b}', A(2, 5, text='1/2 + 1/5'))],
  hint='Try 1/2 first. What is left?',
  why='(a) 5/6 − 1/2 = 5/6 − 3/6 = 2/6 = 1/3. (b) 3/4 − 1/2 = 1/4. (c) 7/10 − 1/2 = 7/10 − 5/10 = 2/10 = 1/5.'))
G.append(item(U+'-G03', 'go', 5, 'In a class, 2/5 of the children are girls. 1/3 of the girls wear glasses. 6 girls wear glasses. How many children are in the class? {b}',
  ans=A(45), hint='Find the number of girls first.',
  why='6 girls are 1/3 of the girls, so there are 18 girls. 18 girls are 2/5 of the class, so 1/5 is 9 children and the class has 5 × 9 = 45 children.',
  space={'rows': ['Draw a bar model here.', '']}))
G.append(item(U+'-G04', 'go', 5, 'Compare each pair. Circle the correct sign.',
  parts=[P('a', '7/9  {circ:>|<}  8/10', A('<')), P('b', '11/12  {circ:>|<}  9/10', A('>')), P('c', '14/15  {circ:>|<}  19/20', A('<'))],
  hint='How far is each fraction from 1?',
  why='(a) 7/9 is 2/9 short of 1 and 8/10 is 2/10 short of 1. Ninths are larger pieces than tenths, so 2/9 is more than 2/10 and 7/9 is less. (b) 1/12 is less than 1/10, so 11/12 is closer to 1: greater. (c) 1/15 is more than 1/20, so 14/15 is less than 19/20.'))

C.append(item(U+'-C01', 'quiz', None, 'Write 29/6 as a mixed number. {b} {b}/{b}', ans=A(4, 5, 6, text='4 5/6'),
  why='29 ÷ 6 = 4 remainder 5. That is 4 wholes and 5 sixths: 4 5/6.'))
C.append(item(U+'-C02', 'quiz', None, 'Write 5 3/8 as an improper fraction. {b}/{b}', ans=A(43, 8, text='43/8'),
  why='5 × 8 + 3 = 43, so 5 3/8 = 43/8.'))
C.append(item(U+'-C03', 'quiz', None, 'Which is greater, 5/8 or 7/12? Circle it. {circ:5/8|7/12}', ans=A('5/8'),
  why='In twenty-fourths, 5/8 = 15/24 and 7/12 = 14/24. 15/24 is greater, so 5/8 is greater.'))
C.append(item(U+'-C04', 'quiz', None, '4/9 of the beads in a bag are blue. There are 28 blue beads. How many beads are in the bag? {b}', ans=A(63),
  why='4 units = 28, so 1 unit = 7. The bag is 9 units: 9 × 7 = 63 beads.'))

unit = {'schema_version': 1, 'level': 4, 'unit': 4, 'id': U, 'title': 'Fraction Frontier', 'topic': 'Fractions', 'holiday_lesson': 4,
        'goal': 'I can change between improper fractions and mixed numbers. I can find a fraction of a set and compare fractions with different denominators.',
        'learn': learn, 'items': S + T + G + C}
write(4, unit)
