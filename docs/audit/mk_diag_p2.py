"""Fix pass P2: writes diag/content/p2.json (placement check, Ages 7-9) and verifies every answer by brute force.
Run:  python3 -I docs/audit/mk_diag_p2.py   (repo root).  diag/build_diag.py is NOT changed; the keys it does not read yet
(childNote, scoring, parent, tutorKey) carry the recommended text for the build changes listed in docs/audit/fixpass_p2.md."""
import json, os, itertools
from math import comb
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')

# ---- verify answers ----
assert 64 + 10 == 74
assert sorted([58, 85, 49]) == [49, 58, 85]
assert 16 - 9 == 7 and 45 + 30 == 75
shapes = ['triangle', 'circle', 'circle', 'square']
assert [shapes[(i - 1) % 4] for i in (8, 10)] == ['square', 'circle']          # 10th is a circle; 8th is a square (the likely slip)
assert [d for d in range(10) if 50 + d + 27 == 81] == [4] and 81 - 27 == 54
assert 2 * 3 * 4 == 24 and 2 + 3 + 4 == 9
assert (3 * 60 + 50 + 25) == 4 * 60 + 15 and 50 + 25 == 75                      # 3:75 is the likely slip
assert 120 + 85 == 205 and (120 + 85) / 100 == 2.05
assert 3 / 4 == 0.75
assert [n for n in range(1, 40) if 2 * n + 3 == 17] == [7]
pets = ['cat', 'dog', 'fish', 'rabbit']; kids = ['Ali', 'Mei', 'Siti', 'Ben']
sols = [p for p in itertools.permutations(pets) if dict(zip(kids, p))['Siti'] == 'rabbit' and dict(zip(kids, p))['Ben'] not in ('cat', 'fish') and dict(zip(kids, p))['Mei'] != 'cat']
assert len(sols) == 1 and dict(zip(kids, sols[0]))['Ali'] == 'cat', sols            # exactly one solution: Ali has the cat

d = {
 'level': 'P2', 'ageName': 'Ages 7-9', 'minutes': 30,
 'foundation': [
  {'q': 'What is 10 more than 64?', 'a': '74', 'skill': 'Place value to 100',
   'work': 'Listen for: the tens digit going up by one. If the answer is 65, the child may have added 1 to the whole number: ask them to point to the tens digit.'},
  {'q': 'Put these numbers in order, smallest first: 58, 85, 49.', 'a': '49, 58, 85', 'skill': 'Comparing and ordering to 100',
   'work': 'Listen for: looking at the tens digit first. Any way of working is fine. If the order starts with 85, the child may have read "smallest" as "biggest": ask them to read the question aloud.'},
  {'q': 'What is 16 - 9?', 'a': '7', 'skill': 'Subtract within 20',
   'work': 'Listen for a strategy: take away 6 then 3, count on from 9, or use fingers. Every method is welcome.'},
  {'q': 'What is 45 + 30?', 'a': '75', 'skill': 'Add within 100',
   'work': 'Listen for: adding the tens to the tens. If the answer is 48 or 345, ask the child to say what 30 is made of.'}],
 'core': [
  {'q': 'A pattern goes triangle, circle, circle, square, triangle, circle, circle, square, and keeps going. What is the 10th shape?', 'a': 'circle', 'skill': 'Repeating patterns',
   'work': 'Listen for: finding the group of 4. Drawing out all 10 shapes or counting on in 4s both work. If the answer is square, the child may have found the 8th shape: ask them to count on two more.'},
  {'q': '5? + 27 = 81. The ? hides one digit. Which digit is it?', 'a': '4', 'skill': 'Missing digits',
   'work': 'Listen for: taking 27 away from 81 (54), or trying a digit and checking it. Both are fine. If the answer is 5 or 6, ask the child to check by adding.'},
  {'q': 'A stack of cubes has 2 layers. Each layer has 3 rows with 4 cubes in each row. How many cubes are in the stack?', 'a': '24', 'skill': 'Arrays and cube stacks',
   'work': 'Listen for: finding one layer first (12), then doubling. Drawing, skip counting and repeated adding are all fine. If the answer is 9, the child may have added 2 + 3 + 4: ask them to draw one layer.'},
  {'q': 'A film starts at 3:50 p.m. and lasts 25 minutes. What time does it end?', 'a': '4:15 p.m.', 'skill': 'Time to 5 minutes',
   'work': 'Listen for: counting on to 4:00 first (10 minutes), then 15 more. Accept 4:15 with or without p.m. If the answer is 3:75, the child may have added 25 to the minutes: ask how many minutes are in an hour.'},
  {'q': 'A pen costs $1.20. A ruler costs $0.85. How much do they cost together?', 'a': '$2.05', 'skill': 'Money',
   'work': 'Listen for: dollars and cents added with care (120 cents + 85 cents = 205 cents) or counting on with coins. Accept $2.05 or 2.05. If the answer is $1.105 or $2.5, ask the child to show it with coins.'},
  {'q': 'A pizza is cut into 4 equal parts. I eat 3 parts. What fraction of the pizza did I eat?', 'a': '3/4', 'skill': 'Fractions',
   'work': 'Listen for: the bottom number tells how many equal parts. If the answer is 1/4, the child may have named the part that is left: ask how many parts were eaten.'}],
 'stretch': [
  {'q': 'These last two are tricky on purpose, so it is fine to skip them. I think of a number. I double it, then add 3, and I get 17. What was my number?', 'a': '7', 'skill': 'Reverse two-step reasoning',
   'work': 'Listen for: working backwards (17 - 3 = 14, half of 14) or guess and check. Both are fine.'},
  {'q': 'Ali, Mei, Siti and Ben each have a different pet: cat, dog, fish or rabbit. Siti has the rabbit. Ben does not have the cat or the fish. Mei does not have the cat. Who has the cat?', 'a': 'Ali', 'skill': 'Logic puzzles',
   'work': 'Listen for: crossing out as they go (Siti rabbit, then Ben dog, then Mei fish, so Ali has the cat). Any way of working is fine.'}],
 'topics': ['place value and ordering to 100', 'add and subtract within 100', 'missing digits', 'arrays and cube stacks', 'repeating patterns', 'time to 5 minutes', 'money (dollars and cents)', 'fractions', 'reasoning and logic puzzles'],
 'childNote': 'These two are tricky on purpose. Have a go, and it is fine to skip them.',
 'scoring': {'placementOn': 'the 6 main questions (numbers 5 to 10)', 'join': '5 to 6', 'support': '3 to 4', 'down': '0 to 2', 'warmupRule': 'If the warm-up score is 2 or less, one level down may be the more comfortable start.',
             'stretchIsAFlag': 'Brain stretchers are not part of the placement score. If a child solves one or both, tell your tutor: they may enjoy the Go further pages. Level-up check only when main 6 of 6, warm-up 4 of 4 and both brain stretchers.',
             'scoreLine': 'Warm-up: ____ / 4     Main questions: ____ / 6     Brain stretchers (a bonus, not scored for placement): ____ / 2'},
 'parent': {
  'join': 'Join <b>Ages 7-9 (P2)</b>. Your child has the foundations and will be well challenged. If they scored 6 of 6 on the main questions and 4 of 4 on the warm-up, and solved both brain stretchers, you can also try the Ages 8-10 (P3) check.',
  'support': 'Join <b>Ages 7-9 (P2)</b>. Most children here find some of the puzzles tricky; that is what the class is for. Your tutor will check in with you after Lesson 1. If the warm-up score is 2 or less, <b>Ages 6-8 (P1)</b> may be a more comfortable start - talk to us first.',
  'down': 'We suggest a chat with your tutor and a free taster before choosing. <b>Ages 6-8 (P1)</b> builds the same thinking habits with smaller numbers. If your child is 9 or older, ask us: you do not have to choose a level by age.',
  'strongBox': '<b>Strong?</b><br>Choose the level that fits the score, not the school year. A child who finds this easy will enjoy the Go further pages in class.',
  'gentleBox': '<b>Want a gentler start?</b><br>Starting one level down means more wins early on and more joy in class.'},
 'tutorKey': {
  'header': 'Print pages 1 and 2 for your child. Keep pages 3 and 4 for yourself.',
  'columnName': 'Listen for',
  'tieBreak': 'Borderline (4 of the 6 main marks): ask your child to explain main questions 6, 8 and 9 aloud. If they can say why, use the higher band. If a child finishes in under 12 minutes, ask them to check two answers before you mark.',
  'prereq': 'Main questions 7, 8, 9 and 10 (cube stacks and arrays, time, money, fractions) are topics taught in school. Missing two or more means Lessons 3, 6, 7, 8 and 9 will need extra care, even if the main score is 5 or 6.'}}
json.dump(d, open(os.path.join(R, 'diag', 'content', 'p2.json'), 'w'), indent=2, ensure_ascii=False)
print('p2.json written:', len(d['foundation']), len(d['core']), len(d['stretch']), 'items; answers verified')

# ---- placement simulation (rule B: main six decide, warm-up <= 2 steers down, stretch only flags) ----
def dist(ps):
    t = {0: 1.0}
    for p in ps:
        n = {}
        for k, v in t.items(): n[k] = n.get(k, 0) + v * (1 - p); n[k + 1] = n.get(k + 1, 0) + v * p
        t = n
    return t
def place(w, c, s):
    if c >= 5: return 'level-up check' if (c == 6 and s == 2 and w == 4) else 'join'
    if c >= 3: return 'one level down (warm-up <= 2)' if w <= 2 else 'join, tutor checks in'
    return 'chat + taster'
PROF = {'strong for age (8y)': ([.98, .98, .97, .97], [.9, .95, .85, .9, .85, .95], [.6, .55]),
        'typical for age (8y)': ([.97, .95, .92, .92], [.6, .85, .7, .6, .85, .85], [.2, .15]),
        'weak for age (8y)': ([.85, .8, .55, .55], [.15, .4, .2, .15, .45, .45], [.02, .02]),
        'younger, strong (6y9m)': ([.98, .98, .95, .95], [.55, .5, .75, .3, .6, .6], [.5, .4]),
        'older, weak (9y)': ([.92, .9, .75, .75], [.3, .65, .4, .35, .6, .6], [.04, .04]),
        'guesser / rusher': ([.9, .5, .5, .85], [.1, .4, .3, .2, .35, .35], [.03, .03])}
print('\nPlacement, main six decide (assumed per-question success rates):')
for name, (w, m, s) in PROF.items():
    out = {}
    for tw, pw in dist(w).items():
        for tc, pc in dist(m).items():
            for ts, ps in dist(s).items():
                k = place(tw, tc, ts); out[k] = out.get(k, 0) + pw * pc * ps
    print(f'  {name:26s}', ', '.join(f'{k} {v:.0%}' for k, v in sorted(out.items(), key=lambda x: -x[1])))
