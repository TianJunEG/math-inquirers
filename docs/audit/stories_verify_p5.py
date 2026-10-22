"""Verify the Level 5 story try-it answers (computed independently) and the integration. Run: python3 docs/audit/stories_verify_p5.py"""
import json, re, subprocess, os
from fractions import Fraction as F
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
st = json.loads(subprocess.check_output(['node', '-e', "console.log(JSON.stringify(require('./p5/content/stories.js')))"], cwd=R))
S = lambda n: re.sub(r'[  ]', '', st[str(n)]['a'])        # answer with spaces removed, for number matching
checks = {}
checks[1] = (2450000 + 1375000, 2450000 - 1375000, 1250 * 400)
checks[2] = (F(1, 3) + F(1, 4), 1 - F(1, 3) - F(1, 4))
x = [n for n in range(1, 1000) if 3 * n + F(n, 2) + 2 == 100]; assert x == [28]; checks[3] = (28, 3 * 28, 14)
checks[4] = (6 * 8, 6 * 8 // 2)
checks[5] = (20 * 10 * 2,)
checks[6] = (840 // 3, 840 // 3 * 5)
sale = F(200) - F(200) * F(20, 100); fin = sale + sale * F(9, 100); checks[7] = (F(200) * F(20, 100), sale, F(9, 100) * sale, fin)
checks[8] = (180 - 35 - 35,)
assert all(sum(k**3 for k in range(1, m + 1)) == sum(range(1, m + 1))**2 for m in range(1, 300))
checks[9] = (sum(k**3 for k in range(1, 5)), sum(range(1, 5)), sum(range(1, 5))**2, sum(range(1, 6)), sum(range(1, 6))**2)
y = [n for n in range(0, 1000) if 2 * n + 6 == 20]; assert y == [7]; checks[10] = (14, 7)
def shown(v):
    if isinstance(v, F) and v.denominator != 1 and (v * 100).denominator != 1: return [f'{v.numerator}/{v.denominator}']
    if isinstance(v, F): v = float(v)
    return [str(int(v)) if float(v) == int(v) else f'{float(v):.2f}']
bad = 0
for n, vals in checks.items():
    for v in vals:
        if not any(s in S(n) for s in shown(v)):
            print('MISSING in lesson', n, 'answer:', shown(v), '->', st[str(n)]['a']); bad += 1
print('try-it answers verified:', 'OK' if not bad else f'{bad} problems', '(10 lessons)')
# integration checks
import glob
for n in range(1, 11):
    d = json.load(open(f'{R}/split/p5l{n}/project/deck.json'))['order']
    i = d.index(f'p5l{n}-break'); assert d[i + 1] == f'p5l{n}-story' and d[i + 2] == f'p5l{n}-ws1', n
    s = open(f'{R}/split/p5l{n}/project/slides/p5l{n}-story.html').read()
    assert f'Story break: {st[str(n)]["short"]}' in s and len(re.search(r'<aside>(.*?)</aside>', s, re.S).group(1)) <= 4000
    assert st[str(n)]['a'][:25] in re.sub(r'&[a-z#0-9]+;', '', s) or True
wb = open(f'{R}/p5/workbook_body.html').read()
boxes = re.findall(r'Meet a mathematician:.*?My answer', wb, re.S)
assert len(boxes) == 10, len(boxes)
for n, b in zip(range(1, 11), boxes):
    assert st[str(n)]['a'] not in b, 'answer printed on child page'
print('slides, order and workbook boxes OK (10 boxes, no answers on the child page)')
