from lib import *
U = 'L4U06'
ANG = lambda angs, **kw: dict({'type': 'l4_angle', 'angles': angs, 'cols': 2, 'width_mm': 150}, **kw)

learn = {
 'intro': 'You need a 180° protractor and a ruler for this unit. A full turn is 360°, a half turn is 180° and a quarter turn is 90°. To measure, count up from the 0 on one arm.',
 'example': {
  'problem': 'How big is the angle? Use the scale that starts at 0 on the arm.',
  'figure': {'type': 'l4_proto', 'angle': 55, 'flip': False, 'label_step': 30, 'width_mm': 78},
  'steps': ['Put the centre of the protractor on the corner. Put the 0 line on one arm.', 'Read the scale that starts at 0 on that arm.'],
  'answer': 'The angle is 55°.'},
 'example2': {
  'problem': 'What is the angle between the clock hands at 4 o\'clock?',
  'figure': {'type': 'l4_clock', 'clocks': [{'h': 4, 'm': 0}], 'r': 120, 'width_mm': 48},
  'steps': ['A clock has 12 equal spaces in 360°. 360 ÷ 12 = 30, so 1 space is 30°.', 'At 4 o\'clock the hands are 4 spaces apart: 4 × 30°.'],
  'answer': 'The angle is 120°.'},
 'pair': True, 'tight': True,
 'howto': {'title': 'How to measure',
           'steps': ['Estimate first. Is it less than 90° or more?',
                     'Centre on the corner. 0 line on one arm.',
                     'Read from the 0 on that arm. Check with your estimate.']},
 'facts': {'title': 'Good to know', 'lines': ['Compass: 1 step = 45°.', 'Clock: 1 space = 30°.', 'Minute hand: 1 minute = 6°.', '∠AOC is the angle at O between OA and OC.']},
 'try': {'id': U + '-L01', 'text': 'Ali faces NE. He turns 135° clockwise. Which way does he face now? {circ:E|SE|S|SW}',
         'answer': A('S'),
         'explanation': '135° is 3 steps of 45°. Clockwise from NE: E, SE, S. He faces S.'}}

S, T, G, C = [], [], [], []
S.append(item(U+'-S01', 'start', 1, 'Estimate each angle. Then measure it with your protractor. Use a ruler to make the arms longer first.',
  fig=ANG([{'d1': 0, 'd2': 25, 'label': 'a'}, {'d1': 0, 'd2': 65, 'label': 'b'}, {'d1': 0, 'd2': 130, 'label': 'c'}], cols=3, len=150, width_mm=160),
  parts=[P('a', 'a = {b}°', A(25)), P('b', 'b = {b}°', A(65)), P('c', 'c = {b}°', A(130))], partsrow=True,
  why='Each angle starts at 0 on the horizontal arm. a = 25°, b = 65° and c = 130°. Answers within 2° are fine. Angle c is greater than a right angle, so a good estimate is more than 90°.'))
S.append(item(U+'-S02', 'start', 1, 'Read the angle from the protractor.',
  fig={'type': 'l4_proto', 'angle': 52, 'flip': True, 'width_mm': 92},
  parts=[P('a', 'The angle is {b}°', A(52)), P('b', 'Is it smaller or greater than a right angle? {circ:smaller|greater}', A('smaller'))],
  figside=True,
  why='One arm lies along the baseline at 0 on the left. Read the scale that starts at 0 on the left arm: 52°. A right angle is 90°, and 52° is smaller. The other scale says 128°, which is the angle measured from the other arm.'))
S.append(item(U+'-S03', 'start', 1, 'Rays OA, OB, OC and OD leave O. The 3 small angles lie side by side. Find the angles.',
  fig={'type': 'l4_fan', 'rays': [{'d': 20, 'label': 'A'}, {'d': 45, 'label': 'B'}, {'d': 80, 'label': 'C'}, {'d': 120, 'label': 'D'}],
       'arcs': [{'i': 0, 'j': 1, 'text': '25°'}, {'i': 1, 'j': 2, 'text': '35°'}, {'i': 2, 'j': 3, 'text': '40°'}], 'width_mm': 78, 'len': 320},
  parts=[P('a', '∠AOC = {b}°', A(60)), P('b', '∠BOD = {b}°', A(75)), P('c', '∠AOD = {b}°', A(100)),
         P('d', 'How many angles are there in all? {b}', A(6))], partsrow=True,
  figside=True,
  why='The angles add. ∠AOC = 25° + 35° = 60°. ∠BOD = 35° + 40° = 75°. ∠AOD = 25° + 35° + 40° = 100°. The angles are AOB, BOC, COD, AOC, BOD and AOD: 6 angles.'))
S.append(item(U+'-S04', 'start', 2, 'Each step round the compass is 45°. Find the direction.',
  fig={'type': 'l4_compass', 'width_mm': 50},
  parts=[P('a', 'Ali faces W. He turns 90° clockwise. He now faces {b}', A('N')),
         P('b', 'Mei faces SE. She turns 180°. She now faces {b}', A('NW')),
         P('c', 'Siti faces NE. She turns 270° clockwise. She now faces {b}', A('NW')),
         P('d', 'Ravi turns 135° anticlockwise and now faces S. At first he faced {b}', A('NW'))],
  figside=True,
  why='(a) 90° is 2 steps. From W clockwise: NW, N. (b) 180° is 4 steps. From SE: S, SW, W, NW. (c) 270° is 6 steps. From NE clockwise: E, SE, S, SW, W, NW. (d) Go back the other way: 135° is 3 steps clockwise from S: SW, W, NW.'))
S.append(item(U+'-S05', 'start', 2, 'Find the smaller angle between the clock hands.',
  fig={'type': 'l4_clock', 'clocks': [{'h': 5, 'm': 0, 'cap': '5 o\'clock'}, {'h': 8, 'm': 0, 'cap': '8 o\'clock'}, {'h': 11, 'm': 0, 'cap': '11 o\'clock'}], 'r': 120, 'width_mm': 150},
  parts=[P('a', '5 o\'clock: {b}°', A(150)), P('b', '8 o\'clock: {b}°', A(120)), P('c', '11 o\'clock: {b}°', A(30))], partsrow=True,
  why='Each space between numbers is 30°. At 5 o\'clock the hands are 5 spaces apart: 150°. At 8 o\'clock they are 4 spaces apart the short way: 120°. At 11 o\'clock they are 1 space apart: 30°.'))
S.append(item(U+'-S06', 'start', 2, 'Ben faces W. He wants to face NE. What is his smallest turn?',
  parts=[P('a', 'The turn is {b}°', A(135)), P('b', 'The direction is {circ:clockwise|anticlockwise}', A('clockwise'))],
  why='Clockwise from W: NW, N, NE is 3 steps, 135°. Anticlockwise from W: SW, S, SE, E, NE is 5 steps, 225°. The smallest turn is 135° clockwise.'))
S.append(item(U+'-S07', 'start', 3, 'Each rectangle corner is 90°. Lines split the corners. Find the angles a and b. The drawings are not to scale.',
  fig={'type': 'l4_corner', 'figs': [{'parts': [{'deg': 53, 'text': 'a'}, {'deg': 37, 'text': '37°'}]}, {'parts': [{'deg': 43, 'text': 'b'}, {'deg': 19, 'text': '19°'}, {'deg': 28, 'text': '28°'}]}], 'width_mm': 120, 'len': 200},
  parts=[P('a', 'a = {b}°', A(53)), P('b', 'b = {b}°', A(43))], partsrow=True,
  why='(a) a + 37° = 90°, so a = 90° − 37° = 53°. (b) The three angles add to 90°: b = 90° − 19° − 28° = 43°.'))
S.append(item(U+'-S08', 'start', 3, 'A robot faces E. It turns 135° anticlockwise. Then it turns 90° clockwise. Then it turns 45° clockwise.',
  parts=[P('a', 'It now faces {b}', A('E')), P('b', 'The turns add up to {b}°', A(270))],
  why='135° anticlockwise from E: NE, N, NW. 90° clockwise from NW: N, NE. 45° clockwise from NE: E. It faces E. The turns add to 135° + 90° + 45° = 270°.'))
S.append(item(U+'-S09', 'start', 3, 'A corner of a rectangle is split into 2 angles. One angle is 5 times the other.',
  parts=[P('a', 'The smaller angle is {b}°', A(15)), P('b', 'The greater angle is {b}°', A(75))],
  why='The corner is 90° and is made of 1 + 5 = 6 equal parts. 90° ÷ 6 = 15° for 1 part. The greater angle is 5 × 15° = 75°.',
  space={'rows': ['Draw a bar model here.', '']}))
S.append(item(U+'-S10', 'start', 3, 'How long does the minute hand take to turn through each angle?',
  parts=[P('a', '90°: {b} minutes', A(15)), P('b', '180°: {b} minutes', A(30)), P('c', '270°: {b} minutes', A(45)), P('d', '60°: {b} minutes', A(10))], partsrow=True,
  why='The minute hand turns 6° each minute. 90° ÷ 6 = 15. 180° ÷ 6 = 30. 270° ÷ 6 = 45. 60° ÷ 6 = 10.'))

T.append(item(U+'-T01', 'think', 4, 'Beyond Level 4: Angles on a line and at a point\nAngles on a straight line add up to 180°. Angles around a point add up to 360°.',
  parts=[P('a', 'On a straight line the angles are 47°, 85° and a. a = {b}°', A(48)),
         P('b', 'Around a point the angles are 95°, 120°, 78° and b. b = {b}°', A(67))],
  hint='Add the angles you know. Then take the sum away from the total.',
  why='(a) 47° + 85° = 132°, and 180° − 132° = 48°. (b) 95° + 120° + 78° = 293°, and 360° − 293° = 67°.',
  space={'rows': ['Working:', '']}))
T.append(item(U+'-T02', 'think', 4, 'Find the smaller angle between the clock hands.',
  parts=[P('a', 'At 7:30 it is {b}°', A(45)), P('b', 'At 1:30 it is {b}°', A(135))],
  hint='At half past, the hour hand is halfway between 2 numbers.',
  why='At 7:30 the minute hand is on the 6. The hour hand is halfway between 7 and 8, which is 1 and a half spaces from the 6: 45°. At 1:30 the hour hand is halfway between 1 and 2, which is 4 and a half spaces from the 6: 4 × 30° + 15° = 135°.',
  space={'rows': ['Working:', '', '']}))
T.append(item(U+'-T03', 'think', 4, 'A robot faces N. It turns 90° clockwise, then 135° anticlockwise, then 225° clockwise, then 45° anticlockwise.',
  parts=[P('a', 'It now faces {b}', A('SE')), P('b', 'The turns add up to {b}°', A(495))],
  hint='Count the steps of 45°. Clockwise is plus, anticlockwise is minus.',
  why='In steps of 45°: +2, −3, +5, −1. From N: 2 steps is E, then 3 steps back is NW, then 5 steps forward is S, then 1 step back is SE. The turns add to 90° + 135° + 225° + 45° = 495°.',
  space={'rows': ['Working:', '']}))

G.append(item(U+'-G01', 'go', 5, 'Six rays leave one point. They make 5 equal angles in a row. The 2 outside rays are 150° apart.',
  parts=[P('a', 'How many angles can you find in all? {b}', A(15)), P('b', 'Count the right angles among them. {b}', A(3))],
  hint='One small angle is 30°. Count 1-part, 2-part, 3-part angles.',
  why='Each small angle is 150° ÷ 5 = 30°. Angles made of 1 part: 5. Of 2 parts: 4. Of 3 parts: 3. Of 4 parts: 2. Of 5 parts: 1. In all 5 + 4 + 3 + 2 + 1 = 15. A right angle is 3 parts of 30°, and there are 3 of them.',
  space={'rows': ['Working:']}))
G.append(item(U+'-G02', 'go', 5, 'A robot faces N. It turns 135° clockwise again and again.',
  parts=[P('a', 'How many turns until it faces N again? {b}', A(8)), P('b', 'After 50 turns it faces {b}', A('W'))],
  hint='135° is 3 steps of 45°. Write the directions after each turn.',
  why='Each turn is 3 steps. The directions are SE, W, NE, S, NW, E, SW, N. It faces N again after 8 turns. 50 turns is 6 lots of 8, which is 48 turns, and 2 more turns. After 48 turns it faces N. 2 more turns take it to SE and then W.',
  space={'rows': ['List:']}))
G.append(item(U+'-G03', 'go', 5, 'A rectangle corner of 90° is cut by 2 lines. The middle angle is 2 times the smallest. The greatest is 6 times the smallest.',
  parts=[P('a', 'The smallest angle is {b}°', A(10)), P('b', 'The greatest angle is {b}°', A(60))],
  hint='Count the equal parts. 1 + 2 + 6 = 9.',
  why='The 3 angles are 1, 2 and 6 equal parts. That is 9 parts in all, and 9 parts = 90°, so 1 part = 10°. The smallest is 10°, the middle is 20° and the greatest is 60°.',
  space={'rows': ['Working:']}))
G.append(item(U+'-G04', 'go', 5, 'Think about the smaller angle between the clock hands at each o\'clock time. Which times give an angle between 100° and 160°?',
  parts=[P('a', 'How many times are there? {b}', A(4)), P('b', 'Write the times: {b} {b} {b} {b}', A(4, 5, 7, 8, text='4, 5, 7 and 8 o\'clock'))],
  hint='Write the angle for every o\'clock time first.',
  why='The angle at 1 to 12 o\'clock is 30°, 60°, 90°, 120°, 150°, 180°, 150°, 120°, 90°, 60°, 30°, 0°. Those between 100° and 160° are 120°, 150°, 150° and 120°, at 4, 5, 7 and 8 o\'clock.',
  ))

C.append(item(U+'-C01', 'quiz', None, 'Find the smaller angle between the clock hands at 7 o\'clock. {b}°', ans=A(150),
  why='At 7 o\'clock the hands are 5 spaces apart the short way. 5 × 30° = 150°.'))
C.append(item(U+'-C02', 'quiz', None, 'Aisha faces S and turns 135° clockwise. Which way does she face now? {b}', ans=A('NW'),
  why='135° is 3 steps of 45°. Clockwise from S: SW, W, NW.'))
C.append(item(U+'-C03', 'quiz', None, 'A corner of a square is split into 2 angles. One angle is 41°. How big is the other? {b}°', ans=A(49),
  why='The corner is 90°. 90° − 41° = 49°.'))
C.append(item(U+'-C04', 'quiz', None, 'The minute hand moves from 5:10 to 5:35. How many degrees does it turn? {b}°', ans=A(150),
  why='From 5:10 to 5:35 is 25 minutes. 25 × 6° = 150°.'))

unit = {'schema_version': 1, 'level': 4, 'unit': 6, 'id': U, 'title': 'Angle Turns', 'topic': 'Angles', 'holiday_lesson': 6,
        'goal': 'I can measure angles and find missing angles. I can find the angle between clock hands and turn on the 8-point compass.',
        'learn': learn, 'items': S + T + G + C}
write(6, unit)
