"""Verify the Level 1 story try-it answers (hp/stories_p1.json) and check the slides/notes."""
import json, os, re
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
S = json.load(open(os.path.join(R, 'hp', 'stories_p1.json')))
ok = []
def chk(n, cond, msg): ok.append(cond); print(('OK  ' if cond else 'FAIL'), 'L%d' % n, msg)
rows = [3 * r for r in range(1, 6)]
chk(1, rows[4] == 15 and rows[3] == 12 and all(b - a == 3 for a, b in zip(rows, rows[1:])), 'row 5 = 15, rule add 3')
chk(2, 4 + 4 == 5 + 3, '4+4 = 5+3, missing 3')
chk(3, 6 == 6 and 6 - 4 == 2, '6 apple pictures, 2 more')
seq = [1, 2, 4, 8]; chk(4, all(b == 2 * a for a, b in zip(seq, seq[1:])) and (16, 32) == (8 * 2, 8 * 4), 'double: 16, 32')
chk(5, [x for x in range(0, 50) if x + 8 == 14] == [6], 'x + 8 = 14 -> 6')
chk(6, [k for k in range(0, 10) if 10 + 5 * k == 20] == [2], '10 + 5k = 20 -> 2 coins')
chk(7, 6 + 6 == 12, 'hexagon: 6 sides, two = 12')
animals = {'cat', 'dog'}; cats = {'cat'}
chk(8, cats <= animals and not animals <= cats, 'every cat an animal; not every animal a cat')
chk(9, 6 * 10 == 60, '6 rods of 10 cm = 60 cm')
pairs = [(a, b) for a in range(13) for b in range(13) if a + b == 12 and a - b == 2]
chk(10, pairs == [(7, 5)], '7 and 5')
exp = {1: '15', 2: '3', 3: '6', 4: '16 and 32', 5: '6', 6: '2', 7: '12', 8: 'Yes', 9: '60', 10: '7 and 5'}
for n, e in exp.items(): chk(n, e in S[str(n)]['a'], 'stored answer contains ' + e)
for n in range(1, 11):
    w = len(S[str(n)]['story'].split()); chk(n, 60 <= w <= 80, 'story words %d' % w)
    sl = open(os.path.join(R, 'split', 'l%d' % n, 'project', 'slides', 'l%d-story.html' % n)).read()
    body = sl.split('<aside>')[0]
    chk(n, 'Story break: ' + S[str(n)]['name'].split()[0] in body and S[str(n)]['a'] not in body, 'slide titled, answer only in notes')
print('ALL OK' if all(ok) else 'FAILURES')
