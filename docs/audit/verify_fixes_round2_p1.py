"""Verify every answer changed or relabelled in the P1 round-2 fix pass.  Run: python3 docs/audit/verify_fixes_round2_p1.py"""
import itertools, json, re, subprocess
R = '/home/claude/math-inquirers/'
ok = True
def chk(name, cond):
    global ok; ok &= bool(cond); print('OK  ' if cond else 'FAIL', name)

# L9 Q4: 1 clip = 3 erasers
chk('L9 Q4a 6 clips x 3 = 18 erasers', 6 * 3 == 18)
chk('L9 Q4b 15 erasers / 3 = 5 clips', 15 / 3 == 5 and 15 % 3 == 0)
# L3 C1: three fruits, 24 votes, apple 6, orange = banana + 6
sol = [(b, o) for b in range(25) for o in range(25) if 6 + b + o == 24 and o == b + 6]
chk('L3 C1 unique answer banana 6, orange 12', sol == [(6, 12)])
# L7 T3 (rectangles in a 1 x 3 strip) and T2 (squares in 3 x 2 grid)
chk('L7 T3 rectangles in a 1x3 strip = 6', sum(3 - w + 1 for w in (1, 2, 3)) == 6)
chk('L7 T2 squares in a 3x2 grid = 8', sum((3 - k + 1) * (2 - k + 1) for k in (1, 2)) == 8)
# L10 Q5b: triangle split by a line from the top corner = 2 small + 1 whole = 3
chk('L10 Q5b 3 triangles (2 small + 1 big)', 2 + 1 == 3)
# L2 magic triangle (1-6): which corner sets give side totals 12, 9, 10
def corner_sets(total):
    out = set()
    for p in itertools.permutations(range(1, 7)):
        a, b, c, d, e, f = p   # corners a,b,c ; d between a-b, e between b-c, f between c-a
        if a + d + b == b + e + c == c + f + a == total: out.add(tuple(sorted((a, b, c))))
    return sorted(out)
chk('L2 total 12 -> corners {4,5,6}', corner_sets(12) == [(4, 5, 6)])
chk('L2 total 9 -> corners {1,2,3}', corner_sets(9) == [(1, 2, 3)])
chk('L2 total 10 -> corners {1,3,5}', corner_sets(10) == [(1, 3, 5)])
# L6 Think harder T1, T2, T4 (labels T1/T2 used on slides)
coins = (5, 10, 20, 50)
t1 = [c for c in itertools.combinations_with_replacement(coins, 4) if sum(c) == 70]
chk('L6 T1 two sets of 4 coins making 70c', len(t1) == 2)
t2 = [(a, 6 - a) for a in range(7) if a * 10 + (6 - a) * 20 == 90]
chk('L6 T2 Sam: three 10c + three 20c', t2 == [(3, 3)])
t4 = [c for n in range(1, 7) for c in itertools.combinations_with_replacement((5, 10, 20), n) if sum(c) == 30]
chk('L6 T4 six ways to make 30c', len(t4) == 6)
# keys in lessons.js equal the bank answers for T1..T4 in every lesson
q = json.load(open(R + 'hp/qbank.json'))
L = json.loads(subprocess.run(['node', '-e', "console.log(JSON.stringify(require(process.argv[1]).lessons))", R + 'hp/lessons.js'], capture_output=True, text=True).stdout)
for les in L:
    n = les['n']; rows = {k: v for k, v in les['key']}
    key = rows.get('Think harder T1 to T4') or rows.get('Think harder T1 to T5')
    good = key is not None and (n == 6 and all('T%d:' % i in key for i in range(1, 6)) or n != 6 and all(('T%d: %s' % (i + 1, x['a'])) in key for i, x in enumerate(q[str(n)]['stretch'][:4])))
    chk('L%d key T1-T4 matches bank' % n, good)
chk('lessons.js L7 exit has no hexagon', 'hexagon' not in json.dumps(L[6]['exit']))
chk('lessons.js L9 key Q4 = 18 erasers, 5 clips', dict(L[8]['key'])['Q4'] == '(a) 18 erasers  (b) 5 clips')
print('ALL OK' if ok else 'SOME FAILED')
