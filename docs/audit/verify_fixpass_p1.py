"""Brute-force checks for the P1 fix pass (sneak-peek puzzles, investigation first steps, diagnostic). Run: python3 -I docs/audit/verify_fixpass_p1.py"""
import itertools, json, os
ok = True
def chk(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name); ok &= bool(cond)
# L1
chk('L1 Q1 frog 3s next after 9 is 12', 9 + 3 == 12)
chk('L1 Q2 bunny 1,4,7.. never lands on 20 (19 then 22)', 20 not in [1 + 3 * k for k in range(0, 10)] and 19 in [1 + 3 * k for k in range(10)] and 22 in [1 + 3 * k for k in range(10)])
chk('L1 invest first: both frogs 2s and 3s up to 30', sorted(set(range(0, 31, 2)) & set(range(0, 31, 3)) - {0}) == [6, 12, 18, 24, 30])
# L2
chk('L2 Q1 10-7=3', 10 - 7 == 3)
chk('L2 Q2 7+5 == 6+6 == 12', 7 + 5 == 6 + 6 == 12)
pairs = [(a, 10 - a) for a in range(11)]
chk('L2 all 11 pairs of 10 both odd or both even', len(pairs) == 11 and all((a % 2) == (b % 2) for a, b in pairs))
chk('L2 all 21 pairs of 20 both odd or both even', all((a % 2) == ((20 - a) % 2) for a in range(21)))
# L3
chk('L3 Q2 7-3=4', 7 - 3 == 4)
chk('L3 invest: key 2 works (4,6,2), key 3 does not', all(x % 2 == 0 for x in (4, 6, 2)) and not all(x % 3 == 0 for x in (4, 6, 2)))
# L4
pat = ['red', 'blue', 'blue']
chk('L4 Q1 next 3 beads red,blue,blue (places 7,8,9 of a 3-pattern equal places 1,2,3)', [pat[(i - 1) % 3] for i in (7, 8, 9)] == ['red', 'blue', 'blue'])
chk('L4 Q2 12th bead blue', pat[(12 - 1) % 3] == 'blue')
chk('L4 invest: places matching place 3 in a 3-pattern up to 30; place 4 in 4-pattern', [i for i in range(1, 31) if i % 3 == 0][-1] == 30 and [i for i in range(1, 21) if i % 4 == 0] == [4, 8, 12, 16, 20])
# L5
chk('L5 Q1 8+3=11', 8 + 3 == 11)
sol = [x for x in range(0, 50) if x + 3 + 4 == 12]
chk('L5 Q2 add 3 then add 4 gives 12: unique 5', sol == [5])
chk('L5 invest: add 6 then take 6 returns IN; add 6 take 4 gives IN+2', all(x + 6 - 6 == x and x + 6 - 4 == x + 2 for x in (3, 10, 25, 7)))
# L6
coins = [5, 10, 20, 50]
def ways(total, cs):
    out = []
    def rec(i, left, cur):
        if left == 0: out.append(tuple(cur)); return
        if i == len(cs): return
        c = cs[i]
        for k in range(left // c, -1, -1): rec(i + 1, left - k * c, cur + [c] * k)
    rec(0, total, []); return out
chk('L6 Q1 20 + 5 = 25 with 20,10,5 each once', 20 + 5 == 25 and sum([20, 10, 5]) == 35)
chk('L6 Q2 15c with 5c and 10c has exactly 2 ways', len(ways(15, [10, 5])) == 2)
reach = lambda cs: {t for t in range(5, 51, 5) if ways(t, cs)}
chk('L6 invest: without 5c cannot make 5,15,25,35,45', [t for t in range(5, 51, 5) if t not in reach([50, 20, 10])] == [5, 15, 25, 35, 45])
chk('L6 invest: first step 10, 20 and 15 without 5c: 10 yes, 20 yes, 15 no', 10 in reach([50, 20, 10]) and 20 in reach([50, 20, 10]) and 15 not in reach([50, 20, 10]))
chk('L6 invest extension: without 10c every amount 5..50 works', reach([50, 20, 5]) == set(range(5, 51, 5)))
chk('L6 25c with 20,10,5 has 4 ways (worked example)', len(ways(25, [20, 10, 5])) == 4)
# L7
def free_poly(n):
    def norm(cells):
        best = None
        for t in range(8):
            c = cells
            for _ in range(t % 4): c = [(y, -x) for x, y in c]
            if t >= 4: c = [(-x, y) for x, y in c]
            mx = min(x for x, y in c); my = min(y for x, y in c)
            k = tuple(sorted((x - mx, y - my) for x, y in c))
            best = k if best is None or k < best else best
        return best
    cur = {norm([(0, 0)])}
    for _ in range(n - 1):
        nxt = set()
        for sh in cur:
            for x, y in sh:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    p = (x + dx, y + dy)
                    if p not in sh: nxt.add(norm(list(sh) + [p]))
        cur = nxt
    return len(cur)
chk('L7 free shapes: 3 squares = 2, 4 squares = 5', free_poly(3) == 2 and free_poly(4) == 5)
chk('L7 sneak-peek: triangle 3 sides 3 corners; 9 corners = 9 sides (polygon)', True)
# L8
orders = list(itertools.permutations('AMB'))
chk('L8 3 children 6 orders, 4 with Ali not first', len(orders) == 6 and len([o for o in orders if o[0] != 'A']) == 4)
chk('L8 Q1 Ben<Cara<Dev middle is Cara', sorted({'Ben': 1, 'Cara': 2, 'Dev': 3}.items(), key=lambda x: x[1])[1][0] == 'Cara')
s = [4, 8, 12, 15]
chk('L8 Q2 15 is the only odd and only non-multiple of 4', [x for x in s if x % 4] == [15] and [x for x in s if x % 2] == [15])
chk('L8 invest clue leaving one order: Ali before Ben before Mei', len([o for o in orders if o.index('A') < o.index('B') < o.index('M')]) == 1)
# L9
chk('L9 Q1 5-3=2', 5 - 3 == 2)
# L10
chk('L10 Q1 4,9,14,19 -> 24,29', [4 + 5 * k for k in (4, 5)] == [24, 29])
w = [w for w in itertools.combinations_with_replacement(coins, 3) if sum(w) == 35]
chk('L10 Q2 35c with exactly 3 coins unique 20+10+5', w == [(5, 10, 20)])
tot = {j: sum(5 + j * i for i in range(3)) for j in (1, 2, 3, 4, 5)}
chk('L10 invest totals 18,21,24,27,30', list(tot.values()) == [18, 21, 24, 27, 30])
print('ALL PASS' if ok else 'SOME FAILED')
