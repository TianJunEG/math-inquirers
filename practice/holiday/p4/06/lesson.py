"""Online practice for Level 4 (Primary 4, ages 9-11) holiday lesson 6: Angle Turns (Angles).

The questions are the ones printed in the Level 4 holiday workbook, built by p4/workbook_html.js from p4/content/l6.js:
  Start here = l6.js workbook() Q1 to Q6;   Investigation = l6.js gaps.invest (Splitting a corner);
  Think harder = l6.js qbank.stretch[0:4];   Go further = l6.js qbank.challenge[-3:]  (printed as Q5 to Q7).
Every answer is recomputed by an INDEPENDENT checker (the directions of the rays, the clock hands placed by the minute, stepping round the compass one 45 degree step at a time,
a search over every set of angles), never a copy of the printed answer; the build stops if a checker and the printed answer (the l6.js `key`, `gaps.invest.key` and `qbank`
answers) differ.  The angles on screen are drawn to size from the same numbers as the checkers.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from p4lib import *      # noqa: E402,F401

META = dict(level=4, lesson=6, key='p4', title='Angle Turns', workbook_title='ANGLE TURNS', topic='Angles',
            strand='Angles and turns',
            sources=['p4/content/l6.js'],
            intro=['Type angles as numbers, like 120. You may add the degree sign, like 120°. Compass questions are choices: tap the direction.',
                   'Measuring with a protractor needs your printed workbook page and your own protractor, so that question is done on paper: do it, then compare with the answer after you submit. '
                   'Some questions ask you to explain or to make up your own puzzle: think or write on paper, then compare.'])
S6 = 'Angles and turns'


def D(**k):
    return dict(strand=S6, **k)


# ---------------------------------------------------------------- independent checkers
def clock_angle(h, m=0):
    """The smaller angle between the hands: the hour hand has turned 30 degrees for each hour and half a degree for each minute, the minute hand 6 degrees for each minute."""
    hour, minute = 30 * (h % 12) + m / 2, 6 * m
    d = abs(hour - minute) % 360
    a = min(d, 360 - d)
    return int(a) if a == int(a) else a


def turn(face, degrees, clockwise=True):
    """Face a compass direction and turn, one 45 degree step at a time."""
    i = DIRS.index(face)
    for _ in range(degrees // 45):
        i = (i + (1 if clockwise else -1)) % 8
    return DIRS[i]


def smallest_turn(a, b):
    """(degrees, direction) of the smaller turn from facing a to facing b, counting 45 degree steps both ways."""
    cw = 0
    i = DIRS.index(a)
    while DIRS[i] != b:
        i = (i + 1) % 8
        cw += 1
    acw = 8 - cw
    return (45 * cw, 'clockwise') if cw <= acw else (45 * acw, 'anticlockwise')


def fan_angles():
    """Every angle between two of the rays OA, OB, OC, OD: (name, size)."""
    return [(a + 'O' + b, db - da) for (da, a), (db, b) in itertools.combinations(FAN, 2)]


def angle_sets(total, unit):
    """Every set of three angles (each a whole multiple of `unit`, smallest first) that add up to `total`."""
    out = []
    for a in range(unit, total, unit):
        for b in range(a, total, unit):
            c = total - a - b
            if c >= b:
                out.append((a, b, c))
    return out


def angle_set_accepts(sets):
    """The three angles typed in any order: '10, 30, 50', '10 30 50', '10 + 30 + 50', '10° and 30° and 50°' ..."""
    out = []
    for s in sets:
        for p in set(itertools.permutations(s)):
            for deg in ('', '°'):
                v = [f'{x}{deg}' for x in p]
                out += [', '.join(v), ' '.join(v), ' + '.join(v), '; '.join(v), ', '.join(v[:-1]) + ' and ' + v[-1]]
    return list(dict.fromkeys(out))


def letters_accepts(letters):
    out = []
    for p in itertools.permutations(letters):
        out += [', '.join(p), ','.join(p), ' '.join(p), ''.join(p), ' and '.join(p)]
    return list(dict.fromkeys(out))


CARDS_T4 = {1: 45, 2: 90, 3: -135, 4: 180}      # card 4 (180 degrees) is the same turn either way


def pairs_to_west():
    """Pairs of different cards that turn a robot from N to W (270 degrees clockwise): try every pair, and the 180 either way."""
    out = []
    for a, b in itertools.combinations(CARDS_T4, 2):
        for sa in ((1, -1) if a == 4 else (1,)):
            for sb in ((1, -1) if b == 4 else (1,)):
                if (CARDS_T4[a] * sa + CARDS_T4[b] * sb) % 360 == 270:
                    if (a, b) not in out:
                        out.append((a, b))
    return out


def pairs_accepts(pairs):
    out = []
    forms = lambda p: [f'{p[0]}+{p[1]}', f'{p[0]} + {p[1]}', f'{p[0]} and {p[1]}', f'{p[0]} {p[1]}'] + ([f'{p[1]}+{p[0]}', f'{p[1]} + {p[0]}', f'{p[1]} and {p[0]}', f'{p[1]} {p[0]}'] if True else [])
    # each pair in either order inside, the pairs in either order, joined by a comma, a semicolon, 'and' or a space
    for order in itertools.permutations(pairs):
        for fa in forms(order[0]):
            for fb in forms(order[1]):
                for sp in (', ', ',', '; ', ' and ', ' / '):
                    out.append(fa + sp + fb)
    return list(dict.fromkeys(out))


def _faces(a, b):
    # the direction a robot facing N ends up in after cards a and b (card 4, 180 degrees, ends in the same direction either way)
    return DIRS[((CARDS_T4[a] + CARDS_T4[b]) % 360) // 45]


OTHER = {(a, b): _faces(a, b) for a, b in itertools.combinations(CARDS_T4, 2) if (a, b) not in pairs_to_west()}
assert OTHER == {(1, 2): 'SE', (1, 4): 'SW', (2, 3): 'NW', (3, 4): 'NE'}, OTHER
FIG_COMPASS = compass()
CLOCK4 = clocks([dict(h=4, m=0, shade=True, cap="4 o'clock")], r=76)
CLOCK7 = clocks([dict(h=7, m=0, shade=True, cap="7 o'clock")], r=76)
CLOCK_BLANK = clocks([dict(hands=False, cap='a blank clock')], r=76, label='A blank clock face with no hands.')
RIGHT_SIZE = [n for n, s in fan_angles() if s == 90]
SETS90 = angle_sets(90, 10)
SETS180 = angle_sets(180, 30)


def dir_choice(iid, no, label, answer, q, hint, steps, src, compute, skill='compass turns', svg=None, tier='core'):
    return D(id=iid, tier=tier, no=no, label=label, type='choice', options=list(DIRS), answer=answer, skill=skill, svg=svg or FIG_COMPASS, check=compute, q=q, hint=hint, steps=steps, src=src)


ITEMS = [
    # ================= Start here (workbook lesson 6, Q1 to Q6)
    D(id='1est', tier='core', no='1', label='1 est', type='text', skill='estimating angles', accept=letters_accepts(['b', 'd']), shown='b, d', svg=four_angles(),
      check=lambda: ', '.join(n for n in 'abcd' if FOUR[n][1] - FOUR[n][0] > 90),
      q='Estimate each angle first. Here are four angles drawn to size. Which of them are bigger than a right angle, the corner of a sheet of paper (90°)? Type the letters with a comma between them.',
      hint='Compare each angle with the corner of a sheet of paper. Is the angle smaller or bigger than the corner?',
      steps=['Compare each angle with a right angle, 90°.', 'Angles b and d are wider open than a right angle. Angles a and c are narrower.', 'So the answer is b and d.'],
      src=['Estimate each angle first. Then measure it with your protractor.']),
    D(id='1measure', tier='core', no='1', label='1 measure', type='selfcheck', paper=True, skill='measuring angles with a protractor', svg=four_angles(),
      check=lambda: {n: FOUR[n][1] - FOUR[n][0] for n in 'abcd'}, sol_fig=lambda f: four_angles(sizes=True),
      q='Measure angles a, b, c and d with your protractor on a copy of the angles. The arms are short: draw them longer with a ruler first. Write your estimate and your measurement for each angle.',
      hint='Put the centre of the protractor on the corner. Count up from the 0 that lines up with one arm. Check your measurement with your estimate.',
      steps=['The angles measure a = 40°, b = 115°, c = 75° and d = 150°.', 'Your measurement is good if it is within 2° of these. An estimate within about 20° is a good estimate.',
             'If you read 140° for angle a, you read the wrong scale. Start counting from the 0 that lines up with one arm.'],
      src=['Estimate each angle first. Then measure it with your protractor.', 'The arms are short: draw them longer with a ruler first.']),

    D(id='2a', tier='core', no='2(a)', label='2(a)', type='number', answer=6, skill='finding every angle in a fan', svg=fan_figure(), check=lambda: len(list(itertools.combinations(FAN, 2))),
      q='Four rays OA, OB, OC and OD come out of point O. ∠AOB means the angle at O between OA and OB. How many angles can you find altogether?',
      hint='Make a list. First OA with each ray after it, then OB with the rays after it, and so on.',
      steps=['OA makes an angle with OB, OC and OD: 3 angles.', 'OB makes a new angle with OC and OD: 2 more. OC makes a new one with OD: 1 more.', '3 + 2 + 1 = 6 angles.'],
      src=['Four rays OA, OB, OC and OD come out of point O.', 'How many angles can you find altogether?']),
    D(id='2b', tier='core', no='2(b)', label='2(b)', type='selfcheck', skill='finding every angle in a fan', svg=fan_figure(), check=lambda: fan_angles(),
      q='Name every angle and find its size. Work in order so you do not miss one. Write your list, then compare it with the answer.',
      hint='Start with the angles next to each other. Then add two angles side by side, and then three.',
      steps=['The angles next to each other: ∠AOB = 30°, ∠BOC = 60° and ∠COD = 45°.', 'Two angles side by side: ∠AOC = 30° + 60° = 90° and ∠BOD = 60° + 45° = 105°.', 'All three side by side: ∠AOD = 30° + 60° + 45° = 135°.', 'That is 6 angles in all.'],
      src=['Name every angle and find its size. Work in order so you do not miss one.']),
    D(id='2bBOD', tier='core', no='2(b)', label='2(b) BOD', type='number', answer=105, skill='adding angles', svg=fan_figure(), check=lambda: dict(fan_angles())['BOD'],
      q='Look at the fan. What is the size of ∠BOD?', hint='∠BOD is made of two smaller angles side by side. Which two, and what are their sizes?',
      steps=['∠BOD is made of ∠BOC and ∠COD side by side.', '∠BOC = 60° and ∠COD = 45°, so ∠BOD = 60° + 45° = 105°.'],
      src=['Name every angle and find its size.']),
    D(id='2bAOD', tier='core', no='2(b)', label='2(b) AOD', type='number', answer=135, skill='adding angles', svg=fan_figure(), check=lambda: dict(fan_angles())['AOD'],
      q='Look at the fan. What is the size of ∠AOD, from OA all the way to OD?', hint='∠AOD is made of three smaller angles side by side. What are they?',
      steps=['∠AOD is made of ∠AOB, ∠BOC and ∠COD side by side.', '30° + 60° + 45° = 135°.'],
      src=['Name every angle and find its size.']),
    D(id='2c', tier='core', no='2(c)', label='2(c)', type='text', skill='right angles', accept=['AOC', '∠AOC', 'angle AOC', 'COA', '∠COA', 'angle COA'], shown='∠AOC', svg=fan_figure(),
      check=lambda: RIGHT_SIZE[0],
      q='Which angle in the fan is a right angle? Type its name, like ∠XYZ.', hint='A right angle is 90°. Look at the sizes of the angles you found.',
      steps=['A right angle is 90°.', '∠AOC = 30° + 60° = 90°, so ∠AOC is the right angle.', 'Check the others: 30°, 60°, 45°, 105° and 135° are not 90°.'],
      src=['Which angle is a right angle?']),

    D(id='3a', tier='core', no='3(a)', label='3(a)', type='number', answer=120, skill='angles on a clock face', svg=CLOCK4, check=lambda: clock_angle(4, 0),
      q="Clock angles. A clock face has 12 equal spaces in 360°. What is the smaller angle between the hands at 4 o'clock?",
      hint='How many degrees is one space? How many spaces are there between the hands, the short way round?',
      steps=['One space is 360° ÷ 12 = 30°.', "At 4 o'clock the hands are 4 spaces apart: 4 × 30° = 120°."],
      src=['Clock angles. A clock face has 12 equal spaces in 360°. Find the smaller angle.']),
    D(id='3b', tier='core', no='3(b)', label='3(b)', type='number', answer=150, skill='angles on a clock face', svg=CLOCK7, check=lambda: clock_angle(7, 0),
      q="Clock angles. A clock face has 12 equal spaces in 360°. What is the smaller angle between the hands at 7 o'clock?",
      hint='Go the short way round between the hands. How many spaces is that?',
      steps=["At 7 o'clock the hands are 5 spaces apart the short way round (the other way is 7 spaces).", 'The smaller angle is 5 × 30° = 150°.'],
      src=['Clock angles. A clock face has 12 equal spaces in 360°. Find the smaller angle.']),
    D(id='3c', tier='core', no='3(c)', label='3(c)', type='set', answer=[1, 11], ordered=False, skill='angles on a clock face', svg=CLOCK_BLANK, check=lambda: [h for h in range(1, 13) if clock_angle(h, 0) == 30],
      q="Find both o'clock times when the angle between the hands is 30°. Type the two hours with a comma between them.",
      hint='One space on the clock is 30°. At which hours are the two hands one space apart?',
      steps=["The hands are one space (30°) apart at 1 o'clock: the minute hand is on 12 and the hour hand is on 1.", "They are also one space apart at 11 o'clock: the hour hand is on 11, one space before 12.", "The two times are 1 o'clock and 11 o'clock."],
      src=['Find both o’clock times when the angle is 30°.']),

    dir_choice('4a', '4(a)', '4(a)', 'N', 'Compass turns. One step from a direction to the next one is 45°. Ali faces W and turns 90° clockwise. Which way does he face now?',
               'How many 45° steps is 90°? Count them clockwise, the way clock hands go.',
               ['90° is 2 steps of 45°.', 'Clockwise from W: NW (1 step), N (2 steps). Ali now faces N.'], ['Ali faces W and turns 90° clockwise. Now he faces:'], lambda: turn('W', 90, True)),
    dir_choice('4b', '4(b)', '4(b)', 'E', 'Compass turns. One step from a direction to the next one is 45°. Mei faces SW and turns 135° anticlockwise. Which way does she face now?',
               'How many 45° steps is 135°? Count them anticlockwise, the opposite way to clock hands.',
               ['135° is 3 steps of 45°.', 'Anticlockwise from SW: S (1 step), SE (2 steps), E (3 steps). Mei now faces E.'], ['Mei faces SW and turns 135° anticlockwise. Now she faces:'], lambda: turn('SW', 135, False)),
    D(id='4c-deg', tier='core', no='4(c)', label='4(c) turn', type='number', answer=135, skill='compass turns', svg=FIG_COMPASS, check=lambda: smallest_turn('NE', 'S')[0],
      q='Compass turns. Siti faces NE and wants to face S. What is her smallest turn, in degrees?',
      hint='Count the 45° steps from NE to S going clockwise, and then going anticlockwise. Which way is shorter?',
      steps=['Clockwise from NE: E, SE, S. That is 3 steps, 3 × 45° = 135°.', 'Anticlockwise from NE: N, NW, W, SW, S. That is 5 steps, 225°.', 'The smallest turn is 135°.'],
      src=['Siti faces NE and wants to face S. Her smallest turn is:']),
    D(id='4c-dir', tier='core', no='4(c)', label='4(c) way', type='choice', options=['clockwise', 'anticlockwise'], answer='clockwise', skill='compass turns', svg=FIG_COMPASS, check=lambda: smallest_turn('NE', 'S')[1],
      q='Compass turns. Siti faces NE and wants to face S. She makes her smallest turn. Which way does she turn?',
      hint='Count the 45° steps both ways round from NE to S. Which way takes fewer steps?',
      steps=['Clockwise from NE to S is 3 steps. Anticlockwise is 5 steps.', 'The smallest turn is clockwise.'],
      src=['Siti faces NE and wants to face S. Her smallest turn is:']),
    dir_choice('4d', '4(d)', '4(d)', 'NE', 'Compass turns. One step from a direction to the next one is 45°. Ravi turns 90° anticlockwise and ends up facing NW. Which way did he face at first?',
               'Work backwards. Undo the turn by turning 90° the other way, starting from NW.',
               ['90° is 2 steps of 45°. Ravi turned 2 steps anticlockwise and ended at NW.', 'To go back, turn 2 steps clockwise from NW: N (1 step), NE (2 steps).', 'At first Ravi faced NE. Check: from NE, 2 steps anticlockwise are N, NW.'],
               ['Ravi turns 90° anticlockwise and ends up facing NW. At first he faced:'], lambda: turn('NW', 90, True)),

    D(id='5a', tier='core', no='5(a)', label='5(a)', type='number', answer=32, skill='angles in squares and rectangles', svg=rect_corner(58), check=lambda: 90 - 58,
      q='The corners of squares and rectangles are 90°. In this rectangle, a line from the corner makes an angle of 58° with the left side. Find the angle marked a.',
      hint='The two angles at the corner sit side by side and make the corner of the rectangle. How big is the whole corner?',
      steps=['The corner of a rectangle is 90°, and the 58° angle and ∠a make it together.', '∠a = 90° − 58° = 32°.'],
      src=['The corners of squares and rectangles are 90°. Find the angles marked a and b.']),
    D(id='5b', tier='core', no='5(b)', label='5(b)', type='number', answer=27, skill='angles in squares and rectangles', svg=square_corner(15, 48), check=lambda: 90 - 15 - 48,
      q='The corners of squares and rectangles are 90°. In this square, two lines from a corner make three angles: 15°, b and 48°. Find the angle marked b.',
      hint='The three angles sit side by side and make the corner of the square. Take away the two you know.',
      steps=['The three angles make the corner of the square, 90°.', '∠b = 90° − 15° − 48° = 27°.', 'Check: 15° + 27° + 48° = 90°.'],
      src=['The corners of squares and rectangles are 90°. Find the angles marked a and b.']),

    dir_choice('6', '6', '6', 'SW', 'A robot starts facing N. It turns 90° clockwise, then 45° anticlockwise, then 180°. Which way does it face now?',
               'Follow the robot one turn at a time. After each turn, write down which way it faces.',
               ['Start facing N. Turn 90° clockwise (2 steps): E.', 'Turn 45° anticlockwise (1 step back): NE.', 'Turn 180° (4 steps): SW. The robot faces SW.'],
               ['A robot starts facing N.', 'It turns 90° clockwise, then 45° anticlockwise, then 180°. Now it faces:'],
               lambda: turn(turn(turn('N', 90, True), 45, False), 180, True)),

    # ================= Investigation: Splitting a corner
    D(id='I1', tier='invest', no='Investigation (easy step)', label='Inv easy', type='number', answer=30, skill='splitting a right angle', svg=right_corner(), check=lambda: [a for a in range(1, 91) if a * 3 == 90][0],
      q='Splitting a corner. A square corner is 90°. Mei cuts it into three EQUAL angles. How big is each one?',
      hint='Share 90° equally into 3 angles.',
      steps=['90° ÷ 3 = 30°.', 'Each angle is 30°. Check: 30° + 30° + 30° = 90°.'],
      src=['A square corner is 90°. Draw it and split it into three EQUAL angles. How big is each one?']),
    D(id='Ia-one', tier='invest', no='Investigation (a)', label='Inv (a)', type='text', skill='systematic listing of angle sets',
      accept=angle_set_accepts([s for s in SETS90 if s != (10, 20, 60)]), shown='another set that adds up to 90°, for example 10, 30, 50',
      check=lambda: ', '.join(str(x) for x in [s for s in SETS90 if s != (10, 20, 60)][0]),
      q='A square corner is 90°. Mei cuts it into three angles. Every angle is a multiple of 10°. One way is 10°, 20° and 60°. Find a different set and type its three angles with commas between them. (The same angles in a different order are one set.)',
      hint='Keep 10° as the smallest angle and change the other two. All three must still add up to 90°.',
      steps=['The three angles must be multiples of 10° and add up to 90°.', 'For example 10° + 30° + 50° = 90°, or 20° + 30° + 40° = 90°, or 30° + 30° + 30° = 90°.', 'There are 7 sets in all (see the next question).'],
      src=['A square corner is 90°. Mei cuts it into three angles.', 'Find as many different sets of three angles as you can.']),
    D(id='Ia-count', tier='invest', no='Investigation (a)', label='Inv (a) n', type='number', answer=7, skill='systematic listing of angle sets', check=lambda: len(SETS90),
      q='A square corner is 90°. It is cut into three angles, and every angle is a whole multiple of 10°. How many different sets of three angles are there altogether? (The same angles in a different order count as one set.)',
      hint='Be systematic: choose the smallest angle first, then list the other two. In units of 10°, you need three whole numbers that add up to 9.',
      steps=['In units of 10° we need three whole numbers (smallest first) that add up to 9.', 'Smallest 1: 1, 1, 7 and 1, 2, 6 and 1, 3, 5 and 1, 4, 4. Smallest 2: 2, 2, 5 and 2, 3, 4. Smallest 3: 3, 3, 3.', 'That is 4 + 2 + 1 = 7 sets: 10, 10, 70; 10, 20, 60; 10, 30, 50; 10, 40, 40; 20, 20, 50; 20, 30, 40; 30, 30, 30.'],
      src=['Find as many different sets of three angles as you can.']),
    D(id='Ib-how', tier='invest', no='Investigation (b)', label='Inv (b)', type='selfcheck', open=True, marking_mode='self', skill='systematic listing of angle sets',
      q='How do you know you have found all the sets of three angles that add up to 90°? Write how you checked.',
      hint='Did you use a system, such as fixing the smallest angle and then listing the other two in order?',
      steps=['A good method: fix the smallest angle, then list the other two in order. Counting in units of 10° helps: three whole numbers that add up to 9.',
             'The smallest angle can be 10°, 20° or 30°. It cannot be more than 30°, because three angles of 40° or more would add up to more than 90°.', 'Smallest 10°: four sets. Smallest 20°: two sets. Smallest 30°: one set. That is 7 sets, and no set is missed. Any clear system is good.'],
      src=['How do you know you have found them all? Write how you checked.']),
    D(id='Ic-count', tier='invest', no='Investigation (c)', label='Inv (c)', type='number', answer=3, skill='systematic listing of angle sets', check=lambda: len(SETS180),
      q='What if the corner is a straight line (180°) cut into three angles that are multiples of 30°? How many different sets of three angles are there?',
      hint='Count in units of 30°. You need three whole numbers that add up to 6. List them with the smallest first.',
      steps=['In units of 30° we need three whole numbers (smallest first) that add up to 6: 1, 1, 4 and 1, 2, 3 and 2, 2, 2.', 'In degrees: 30, 30, 120; 30, 60, 90; 60, 60, 60. That is 3 sets.'],
      src=['What if the corner is a straight line (180°) cut into three angles that are multiples of 30°? Find all the sets. What stays the same?']),
    D(id='Ic-same', tier='invest', no='Investigation (c)', label='Inv (c) same', type='selfcheck', open=True, marking_mode='self', skill='angles that make a whole turn',
      q='Look at the sets of angles for the square corner (90°) and for the straight line (180°). What stays the same in every set?',
      hint='Look at the sets you found for 90° and for 180°. What is the same about all of them?',
      steps=['In every set the three angles add up to the whole angle they were cut from: 90° for the square corner and 180° for the straight line.', 'Angles side by side add up to the whole. Any answer that says this is good.'],
      src=['What stays the same?']),

    # ================= Think harder (qbank.stretch[0:4])
    dir_choice('T1', 'Think harder 1', 'T1', 'N', 'Siti faces SE. She turns 225° clockwise. Which direction does she face now?',
               'How many 45° steps is 225°? Count them clockwise from SE.',
               ['225° is 5 steps of 45°.', 'Clockwise from SE: S, SW, W, NW, N. Siti faces N.'], ['Siti faces SE. She turns 225° clockwise. Which direction does she face now?'],
               lambda: turn('SE', 225, True), svg=compass(hi=('SE',)), tier='stretch'),
    D(id='T2a', tier='stretch', no='Think harder 2', label='T2 (10)', type='number', answer=60, skill='angles on a clock face', svg=clocks([dict(h=10, m=0, cap="10 o'clock")], r=76), check=lambda: clock_angle(10, 0),
      q="What is the smaller angle between the clock hands at 10 o'clock?", hint='Go the short way round. How many spaces apart are the hands? One space is 30°.',
      steps=["At 10 o'clock the hands are 2 spaces apart the short way round.", '2 × 30° = 60°.'],
      src=['What is the angle between the clock hands at 10 o’clock? At 2 o’clock? What do you notice?']),
    D(id='T2b', tier='stretch', no='Think harder 2', label='T2 (2)', type='number', answer=60, skill='angles on a clock face', svg=clocks([dict(h=2, m=0, cap="2 o'clock")], r=76), check=lambda: clock_angle(2, 0),
      q="What is the smaller angle between the clock hands at 2 o'clock?", hint='How many spaces apart are the hands? One space is 30°.',
      steps=["At 2 o'clock the hands are 2 spaces apart.", '2 × 30° = 60°.'],
      src=['What is the angle between the clock hands at 10 o’clock? At 2 o’clock? What do you notice?']),
    D(id='T2c', tier='stretch', no='Think harder 2', label='T2 notice', type='selfcheck', open=True, marking_mode='self', skill='angles on a clock face',
      svg=clocks([dict(h=10, m=0, cap="10 o'clock"), dict(h=2, m=0, cap="2 o'clock")], r=60),
      q="Look at the clock at 10 o'clock and the clock at 2 o'clock. What do you notice about the angles between the hands?",
      hint='Compare the two clock pictures. Where is the hour hand in each, and how far is it from the minute hand?',
      steps=["The angle is 60° at both times. At each time the hands are 2 spaces apart the short way round.", '10 and 2 are the same distance from 12, one on each side. The two pictures are mirror images of each other. Any answer like this is good.'],
      src=['What is the angle between the clock hands at 10 o’clock? At 2 o’clock? What do you notice?']),
    D(id='T3', tier='stretch', no='Think harder 3', label='T3', type='number', answer=210, skill='turns of the minute hand', svg=clocks([dict(h=7, m=15, cap='7:15'), dict(h=7, m=50, cap='7:50')], r=60),
      check=lambda: (6 * 50 - 6 * 15) % 360,
      q='How many degrees does the minute hand turn from 7:15 to 7:50?', hint='How many minutes is that? The minute hand turns the same number of degrees every minute.',
      steps=['From 7:15 to 7:50 is 35 minutes.', 'The minute hand turns 360° ÷ 60 = 6° every minute.', '35 × 6° = 210°.'],
      src=['How many degrees does the minute hand turn from 7:15 to 7:50?']),
    D(id='T4', tier='stretch', no='Think harder 4', label='T4', type='text', skill='combining turns', accept=pairs_accepts(pairs_to_west()), shown='1+3, 2+4',
      check=lambda: ', '.join(f'{a}+{b}' for a, b in pairs_to_west()),
      q='A robot starts facing N. Ben wants it to turn from N to W using two DIFFERENT cards from: card 1 is 45° clockwise, card 2 is 90° clockwise, card 3 is 135° anticlockwise, card 4 is 180°. Find ALL the pairs that work. Type each pair with a + between, and a comma between the pairs.',
      hint='How far must the robot turn from N to W? List every pair of cards, and add the two turns. Remember anticlockwise turns go the other way.',
      steps=['From N to W is a 270° turn clockwise (or 90° anticlockwise).', 'Try each pair: 45° clockwise + 135° anticlockwise ends 90° anticlockwise of N, which is W. 90° clockwise + 180° ends 270° clockwise, which is W.',
             'The other pairs end somewhere else: ' + ', '.join(f'{a} + {b} faces {OTHER[(a, b)]}' for a, b in OTHER) + '.', 'The two ways are cards 1 + 3 and cards 2 + 4.'],
      src=['A robot starts facing N. Ben wants it to turn from N to W using two DIFFERENT cards from:']),

    # ================= Go further (qbank.challenge[-3:], printed Q5 to Q7)
    D(id='G5', tier='challenge', no='Go further 5', label='G5', type='selfcheck', open=True, marking_mode='open', skill='making up a clock-angle puzzle',
      svg=clocks([dict(hands=False, cap='my time'), dict(hands=False, cap='a second time')], r=60, label='Two blank clock faces for your puzzle.'),
      check=lambda: (clock_angle(9, 30), clock_angle(2, 30)),
      q='Make up your own clock-angle puzzle. Choose a time that is NOT an o\'clock time (half past is easiest) and work out the angle between the hands. Then find a second time with the same angle.',
      hint='Think about where the hour hand is at half past: it is halfway between two numbers.',
      steps=['Puzzles will vary. Check yours by working out where the hour hand is: it moves half a degree every minute.',
             'Model: at 9:30 the minute hand points to 6 (180°) and the hour hand is halfway between 9 and 10 (285°). The angle is 105°: 3 spaces and a half, 3 × 30° + 15°. Another time with the same angle is 2:30.', 'Show your puzzle to a partner or your tutor and check each other\'s answers.'],
      src=['Make up your own clock-angle puzzle.']),
    D(id='G6', tier='challenge', no='Go further 6', label='G6', type='fields', frame='smallest {f1}°   middle {f2}°   biggest {f3}°', answer=[15, 30, 45], skill='angles in a square corner',
      check=lambda: (lambda s: [s, 2 * s, 3 * s])([s for s in range(1, 91) if s + 2 * s + 3 * s == 90][0]),
      q='The corner of a square is cut into 3 angles. The middle angle is twice the smallest. The biggest is 3 times the smallest. Find all three angles.',
      hint='Call the smallest angle 1 part. How many parts is the middle angle, and how many parts is the biggest?',
      steps=['The smallest is 1 part, the middle is 2 parts and the biggest is 3 parts: 6 equal parts in all.', 'The corner is 90°, so 6 parts = 90° and 1 part = 90° ÷ 6 = 15°.', 'The angles are 15°, 30° and 45°. Check: 15° + 30° + 45° = 90°.'],
      src=['The corner of a square is cut into 3 angles. The middle angle is twice the smallest. The biggest is 3 times the smallest. Find all three angles.']),
    D(id='G7', tier='challenge', no='Go further 7', label='G7', type='number', answer=20, skill='angles in squares and rectangles', svg=overlap_figure(160), check=lambda: 90 - (160 - 90),
      q='Two squares share one corner O and overlap, like the picture. The angle between their outside sides is 160°. What is the angle where the squares overlap?',
      hint='Each square has a 90° corner at O. What do the two corners add up to? How much of that is counted twice?',
      steps=['The two square corners add up to 90° + 90° = 180°.', 'The overlap is counted twice in that 180°, but the angle across both squares is only 160°.', 'So the overlap is 180° − 160° = 20°.'],
      src=['Two squares share one corner O and overlap, like the picture.']),
]

finish(ITEMS)

VARIANTS = {
    '2a': dict(
        base=dict(k=4),
        tpl=dict(vars=dict(k=[3, 4, 5, 6]),
                 q='{k} rays come out of one point O, one after the other like a fan (not all the way round). How many angles can you find altogether?',
                 answer='k*(k-1)/2', hint='Make a list. Count the angles each ray makes with the rays after it, and add them up.',
                 steps=['Each of the {k} rays makes an angle with each of the other {k} − 1 rays.', 'Every angle is counted from both of its rays, so divide by 2: {k} × ({k} − 1) ÷ 2 = {ans} angles.']),
        oracle=lambda e: len(list(itertools.combinations(range(e['k']), 2)))),
    '3a': dict(
        base=dict(h=4),
        tpl=dict(vars=dict(h=[1, 2, 3, 4, 5]),
                 q="What is the smaller angle between the clock hands at {h} o'clock?", answer='30*h', hint='One space on the clock is 30°. How many spaces apart are the hands?',
                 steps=["At {h} o'clock the hands are {h} spaces apart the short way round.", 'Each space is 30°, so {h} × 30° = {ans}°.']),
        oracle=lambda e: clock_angle(e['h'], 0)),
    '5a': dict(
        base=dict(x=58),
        tpl=dict(vars=dict(x=[28, 32, 35, 42, 52, 58, 64, 71]),
                 q='A line from the corner of a rectangle makes an angle of {x}° with one side. What is the angle between the line and the other side?', answer='90-x',
                 hint='The two angles at the corner sit side by side and make the corner. How big is the whole corner?',
                 steps=['The corner of a rectangle is 90°.', '90° − {x}° = {ans}°.']),
        oracle=lambda e: 180 // 2 - e['x']),
    'T3': dict(
        base=dict(a=15, n=35),
        tpl=dict(vars=dict(a=[10, 15, 20], n=[10, 15, 20, 25, 30, 35]), derive=dict(b='a+n'),
                 q='How many degrees does the minute hand turn from 7:{a} to 7:{b}?', answer='6*n', hint='How many minutes is that? The minute hand turns the same number of degrees every minute.',
                 steps=['From 7:{a} to 7:{b} is {n} minutes.', 'The minute hand turns 6° every minute: {n} × 6° = {ans}°.']),
        oracle=lambda e: (6 * (e['a'] + e['n']) - 6 * e['a']) % 360),
    'G7': dict(
        base=dict(S=160),
        tpl=dict(vars=dict(S=[130, 140, 150, 160, 170]),
                 q='Two squares share one corner O and overlap. The angle between their outside sides is {S}°. What is the angle where the squares overlap?', answer='180-S',
                 hint='Each square has a 90° corner at O. What do the two corners add up to? How much of that is counted twice?',
                 steps=['The two square corners add up to 90° + 90° = 180°.', 'The overlap is counted twice, but the angle across both squares is {S}°, so the overlap is 180° − {S}° = {ans}°.']),
        oracle=lambda e: min(90, e['S']) - max(0, e['S'] - 90)),
}
