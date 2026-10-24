"""Online practice for Level 5 (Primary 5, ages 10 to 12) holiday lesson 5: Volume ("Volume Vault").

The questions are the ones printed in the Level 5 holiday workbook, lesson 5: Start here Q1 to Q6 (p5/content/l5.js, workbook()), the Investigation
(p5/content/inv.js), Think harder A1 to A4 (the first four 'stretch' questions of p5/content/l5.js qbank) and Go further B1 to B3 (the last three
'challenge' questions) and the "Make up your own" prompt (gaps.js), in the printed order, exactly as p5/workbook_html.js prints them.  Every answer is recomputed
by an INDEPENDENT checker below (every unit cube is listed and counted, every whole-number box is searched, every cuboid cube is classified by its position,
water volumes are matched by a search over the depth), never by copying the printed answer; build_holiday.py stops if a checker and the printed answer differ.
Every figure is drawn from the same numbers (practice/holiday/p5/p5fig3.py).
"""
import itertools, os, sys
HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE_, '..', '..'))
sys.path.insert(0, os.path.join(HERE_, '..'))
from hlib import *          # noqa: E402,F401
from p5lib import *         # noqa: E402,F401
import p5fig3 as G          # noqa: E402

META = dict(level=5, lesson=5, key='p5', title='Volume Vault', workbook_title='VOLUME VAULT', topic='Volume', strand='Measurement',
            sources=['p5/content/l5.js', 'p5/content/inv.js', 'p5/content/gaps.js'],
            intro=['Volume is the space inside a solid. A cuboid is built from layers of 1-cm cubes, and 1 cm³ is the volume of one small cube. 1 litre = 1000 cm³. '
                   'Water in a tank is a cuboid too: the area of the base times the depth of the water.',
                   'Type the answer into the box (a unit after the number is fine). The drawings help you; read the sizes from the words and the labels. '
                   'Some questions ask you to list or to explain: write your idea, then compare it with the model answer after you submit.'])
ST = 'Measurement'
F = Fraction


def D(**k):
    k.setdefault('strand', ST)
    return k


# ---------------------------------------------------------------- checkers: independent searches and counts (no formula copied from a printed answer)
def cubes(L, B, H):
    """Every unit cube of an L x B x H cuboid, by its position."""
    return [(x, y, z) for x in range(L) for y in range(B) for z in range(H)]


def painted_faces(c, dims):
    """How many faces of the small cube at position c are on the outside of the big cuboid."""
    return sum((c[k] == 0) + (c[k] == dims[k] - 1) for k in range(3))


def paint_counts(L, B, H):
    out = {0: 0, 1: 0, 2: 0, 3: 0}
    for c in cubes(L, B, H):
        out[painted_faces(c, (L, B, H))] += 1
    return out


def triples(n):
    """Every cuboid with whole-number edges and exactly n unit cubes, as (a, b, c) with a <= b <= c (a cuboid turned round is the same cuboid)."""
    out = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            for c in range(b, n + 1):
                if a * b * c == n:
                    out.append((a, b, c))
    return out


def fmt3(t):
    return ' × '.join(str(x) for x in t)


def flat3(ts):
    return [x for t in ts for x in t]


def smallest_cube_edge(L, B, H):
    e = 1
    while e < max(L, B, H):
        e += 1
    return e


def fit_count(edge, L, B, H):
    """How many cubes with the given edge fit in neat layers in an L x B x H box: place cubes at 0, edge, 2 x edge ... while they stay inside."""
    def along(n):
        k = 0
        while (k + 1) * edge <= n:
            k += 1
        return k
    return along(L) * along(B) * along(H)


def water_litres(L, B, w):
    return F(sum(1 for _ in range(L * B * w)), 1000)          # every cm³ of water counted


def depth_for(volume, base):
    found = [d for d in range(0, 400) if base * d == volume]
    assert len(found) == 1, (volume, base)
    return found[0]


def whole(v):
    v = F(v)
    assert v.denominator == 1, v
    return int(v)


T36 = triples(36)
T48 = triples(48)
T64 = triples(64)
assert len(T36) == 8 and len(T48) == 9 and len(T64) == 7


def fits_5(t):
    return all(e <= 5 for e in t)


def most_cubelike(ts):
    best = min(ts, key=lambda t: t[2] - t[0])
    assert [t for t in ts if t[2] - t[0] == best[2] - best[0]] == [best]
    return best


def one_box_choice(options):
    one = [n for n in options if len(triples(n)) == 1]
    assert len(one) == 1
    return one[0]


def a2_capacity():
    found = [c for c in range(1, 2000) if F(3, 5) * c - F(1, 3) * c == 12]
    assert len(found) == 1
    return found[0]


def a3_side():
    found = [s for s in range(1, 200) if s * s * 5 == 245]
    assert len(found) == 1
    return found[0]


def b1_volume():
    sols = [(a, b, c) for a in range(1, 31) for b in range(1, 31) for c in range(1, 31) if a * b == 12 and a * c == 15 and b * c == 20]
    assert len(sols) == 1
    return sols[0][0] * sols[0][1] * sols[0][2]


def b3_depth():
    """Tank 30 x 20, water 10 cm deep, a block 10 x 10 x 15 standing on the bottom: find the new depth d by matching the water volume (the block only takes room up to the water)."""
    water = 30 * 20 * 10
    found = []
    for half in range(1, 50):
        d = F(half, 2)
        room = 30 * 20 * d - 10 * 10 * min(d, 15)
        if room == water:
            found.append(d)
    assert len(found) == 1 and found[0] < 15
    return whole(found[0])


SQ3 = 'cm³'

ITEMS = [
    # ================= Start here (workbook lesson 5: Q1 to Q6)
    D(id='1a', tier='core', no='1(a)', type='number', skill='volume of a cuboid', answer=24,
      q='This solid cuboid is built from 1-cm cubes. What is its volume? (Type the number of cm³.)', svg=G.cuboid_grid(4, 3, 2),
      check=lambda: len(cubes(4, 3, 2)),
      hint='Count the cubes in one layer first. How many layers are there?',
      steps=['One layer has 4 × 3 = 12 cubes.', 'There are 2 layers: 12 × 2 = 24 cubes.', 'Each cube is 1 cm³, so the volume is 24 cm³.'],
      src=['This solid cuboid is built from 1-cm cubes.', 'What is its volume?']),
    D(id='1b', tier='core', no='1(b)', type='number', skill='cube from a cuboid', answer=40,
      q='Mei adds 1-cm cubes (none taken away) to this solid until it is a cube. What is the fewest cubes she must add? (Type the number of cubes.)', svg=G.cuboid_grid(4, 3, 2),
      check=lambda: smallest_cube_edge(4, 3, 2) ** 3 - len(cubes(4, 3, 2)),
      hint='A cube has all its edges equal. Which is the longest edge of this solid?',
      steps=['The longest edge of the solid is 4 cubes. A cube that holds the solid needs that edge on every side.', 'The smallest such cube is 4 × 4 × 4 = 64 cubes.',
             'Mei must add 64 − 24 = 40 cubes. A smaller cube would be too short for the longest edge.'],
      src=['Mei adds 1-cm cubes (none taken away) until the solid is a cube. What is the fewest she must add? Explain.']),
    D(id='1c', tier='core', no='1(b) explain', label='1(b) why', type='selfcheck', open=False, skill='explaining a cube from a cuboid',
      q='Mei adds 1-cm cubes (none taken away) to this solid until it is a cube. Explain how you know your number of cubes is the fewest she must add. Write your idea, then compare it with the model answer.',
      svg=G.cuboid_grid(4, 3, 2), check=lambda: (smallest_cube_edge(4, 3, 2), smallest_cube_edge(4, 3, 2) ** 3),
      hint='Think about the edges. How long must every edge of a cube be, if the solid has to fit inside it?',
      steps=['A cube has three equal edges. The solid has an edge of 4 cubes, so the cube must be at least 4 cubes long, wide and high.', 'The smallest possible cube is 4 × 4 × 4 = 64 cubes, so Mei needs 64 − 24 = 40 more.',
             'A good explanation says that the longest edge decides the size of the cube, and that a bigger cube would need even more cubes.'],
      src=['Explain.']),

    D(id='2a', tier='core', no='2(a) list', label='2(a) list', type='selfcheck', open=False, skill='listing all the cuboids', facts=T36,
      q='Ravi has 36 one-centimetre cubes. He uses all of them to build one cuboid. Turning a cuboid round does not make a new one.\nList every cuboid he can build (length × breadth × height), in order. Write your list, then compare it with the model answer.',
      check=lambda: triples(36),
      hint='Go in order: first the cuboids with a 1 cm edge, then the ones whose shortest edge is 2 cm, and so on. What do the other two edges multiply to?',
      steps=['Go in order of the shortest edge. Shortest edge 1 cm: ' + ', '.join(fmt3(t) for t in T36 if t[0] == 1) + '.',
             'Shortest edge 2 cm: ' + ', '.join(fmt3(t) for t in T36 if t[0] == 2) + '. Shortest edge 3 cm: ' + ', '.join(fmt3(t) for t in T36 if t[0] == 3) + '.',
             'A shortest edge of 4 cm or more would need at least 4 × 4 × 4 = 64 cubes, which is more than 36, so the list ends here.',
             'A good list is in order and has no cuboid twice (a 3 × 4 × 3 box is the same as 3 × 3 × 4).'],
      src=['Ravi has 36 one-centimetre cubes. He uses all of them to build one cuboid. Turning a cuboid round does not make a new one.', 'List every cuboid he can build (length × breadth × height), in order. How many are there?']),
    D(id='2a2', tier='core', no='2(a) how many', label='2(a) count', type='number', skill='counting all the cuboids', answer=8,
      q='Ravi has 36 one-centimetre cubes. He uses all of them to build one cuboid. Turning a cuboid round does not make a new one.\nHow many different cuboids can he build?',
      check=lambda: len(triples(36)),
      hint='List the cuboids in order, starting with the shortest edge 1 cm. Then count your list.',
      steps=['Listed in order of the shortest edge: ' + ', '.join(fmt3(t) for t in T36) + '.', 'That is 8 cuboids.'],
      src=['How many are there?']),
    D(id='2b', tier='core', no='2(b)', type='set', ordered=True, grouped=False, skill='fitting in a box', answer=flat3([t for t in T36 if fits_5(t)]),
      q='Which of Ravi’s cuboids can fit inside a box 5 cm long, 5 cm wide and 5 cm high? Type its three edges, smallest first, with commas.',
      check=lambda: flat3([t for t in T36 if fits_5(t)]),
      hint='A cuboid fits in the box only if none of its edges is longer than 5 cm. Look at the longest edge of each cuboid on your list.',
      steps=['The box is 5 cm long, 5 cm wide and 5 cm high, so every edge of the cuboid must be 5 cm or less.', 'The longest edges of the eight cuboids are ' + ', '.join(str(t[2]) for t in T36) + ' cm.',
             'Only 3 × 3 × 4 has no edge longer than 5 cm, so the answer is 3, 3, 4.'],
      src=['Which of them can fit inside a box 5 cm long, 5 cm wide and 5 cm high?']),

    D(id='3s', tier='core', no='3 Start here', label='3 start', type='fields', skill='water in a tank as layers', answer=[1500, 27000],
      q='A glass tank is 50 cm long, 30 cm wide and 40 cm high. The water in it is 18 cm deep.\nStart here: think of the water as 18 layers of cubes. One layer is 50 × 30.', svg=G.tank_q3(),
      frame='One layer (cubes): {f1}     18 layers (cm³): {f2}', check=lambda: [50 * 30, len(cubes(50, 30, 18))],
      hint='One layer covers the whole base of the tank. How many 1-cm cubes cover a base 50 cm by 30 cm? Then count the layers.',
      steps=['One layer covers the base: 50 × 30 = 1500 cubes.', '18 layers: 18 × 1500 = 27000 cubes, so the water is 27000 cm³.'],
      src=['18 layers of cubes. One layer is 50 × 30 = ______ cubes. 18 layers hold ______ cm³.']),
    D(id='3a', tier='core', no='3(a)', type='number', skill='litres in a tank', answer=27,
      q='A glass tank is 50 cm long, 30 cm wide and 40 cm high. The water in it is 18 cm deep.\nHow many litres of water are in the tank? (Type the number of litres.)', svg=G.tank_q3(),
      check=lambda: whole(water_litres(50, 30, 18)),
      hint='Find the volume of the water in cm³ first. Then change cm³ into litres.',
      steps=['The water is 50 × 30 × 18 cm³, and 1 litre = 1000 cm³.', '50 × 30 × 18 = 27 000 cm³, and 27 000 ÷ 1000 = 27.', 'There are 27 litres of water in the tank.'],
      src=['How many litres of water are in the tank?']),
    D(id='3b', tier='core', no='3(b)', type='number', skill='filling a tank', answer=33,
      q='A glass tank is 50 cm long, 30 cm wide and 40 cm high. The water in it is 18 cm deep.\nHow many more litres are needed to fill it to the top? (Type the number of litres.)', svg=G.tank_q3(),
      check=lambda: whole(water_litres(50, 30, 40 - 18)),
      hint='How much empty space is there in the tank? Think of the empty part as a cuboid too.',
      steps=['The empty part of the tank is 40 − 18 = 22 cm high.', '50 × 30 × 22 = 33 000 cm³, and 33 000 ÷ 1000 = 33.', 'You need 33 more litres.'],
      src=['How many more litres are needed to fill it to the top?']),
    D(id='3c', tier='core', no='3(c)', type='number', skill='water level after pouring out', answer=12,
      q='A glass tank is 50 cm long, 30 cm wide and 40 cm high. The water in it is 18 cm deep. Then 9 ℓ of water is let out.\nHow deep is the water now? (Type the number of cm.)', svg=G.tank_q3(),
      check=lambda: depth_for(len(cubes(50, 30, 18)) - 9 * 1000, 50 * 30),
      hint='Work in cm³. How much water is left in the tank? Then ask how deep that water is over the base.',
      steps=['At first there is 50 × 30 × 18 = 27 000 cm³. The 9 ℓ let out is 9000 cm³, so 18 000 cm³ is left.', 'One cm of depth over the base holds 50 × 30 = 1500 cm³.',
             '18 000 ÷ 1500 = 12, so the water is 12 cm deep.'],
      src=['Instead, 9 ℓ of water is let out. How deep is the water now?']),

    D(id='4s', tier='core', no='4 Start here', label='4 start', type='fields', skill='base area and one layer of water', answer=[1000, 1000],
      q='A tank has a base 40 cm by 25 cm. The water is 15 cm deep. Ali drops in 5 metal cubes with edges of 10 cm. They sink and are completely under water.\nStart here: the cubes take up space, so the water rises.',
      svg=G.tank_q4(), frame='Base area, 40 × 25 (cm²): {f1}     1 cm layer of water (cm³): {f2}', check=lambda: [40 * 25, len(cubes(40, 25, 1))],
      hint='The base is a rectangle 40 cm by 25 cm. A layer of water 1 cm deep has the same area as the base and is 1 cm thick.',
      steps=['The base is 40 × 25 = 1000 cm².', 'A layer of water 1 cm deep has 1000 cubes of 1 cm³, so it is 1000 cm³.'],
      src=['the base is 40 × 25 = ______ cm². A 1 cm layer of water over the base is ______ cm³. The cubes take up space, so the water rises.']),
    D(id='4a', tier='core', no='4(a)', type='number', skill='volume of cubes', answer=5000,
      q='A tank has a base 40 cm by 25 cm. The water is 15 cm deep. Ali drops in 5 metal cubes with edges of 10 cm. They sink and are completely under water.\nWhat is the volume of the 5 cubes? (Type the number of cm³.)',
      svg=G.tank_q4(), check=lambda: 5 * len(cubes(10, 10, 10)),
      hint='Find the volume of one cube with edges of 10 cm. Then count 5 of them.',
      steps=['One cube is 10 × 10 × 10 = 1000 cm³.', '5 cubes: 5 × 1000 = 5000 cm³.'],
      src=['Volume of 5 cubes:']),
    D(id='4b', tier='core', no='4(b)', type='number', skill='rise in water level', answer=5,
      q='A tank has a base 40 cm by 25 cm. The water is 15 cm deep. Ali drops in 5 metal cubes with edges of 10 cm. They sink and are completely under water.\nHow much does the water rise? (Type the number of cm.)',
      svg=G.tank_q4(), check=lambda: depth_for(5 * len(cubes(10, 10, 10)), 40 * 25),
      hint='The cubes push up a new slice of water that has the same volume as the cubes. How thick is a slice of that volume over the base?',
      steps=['The water rises by a slice with the same volume as the cubes: 5000 cm³.', 'The base is 40 × 25 = 1000 cm², so the slice is 5000 ÷ 1000 = 5 cm thick.', 'The water rises 5 cm.'],
      src=['Rise:']),
    D(id='4c', tier='core', no='4(c)', type='number', skill='new water depth', answer=20,
      q='A tank has a base 40 cm by 25 cm. The water is 15 cm deep. Ali drops in 5 metal cubes with edges of 10 cm. They sink and are completely under water.\nHow deep is the water now? (Type the number of cm.)',
      svg=G.tank_q4(), check=lambda: depth_for(40 * 25 * 15 + 5 * len(cubes(10, 10, 10)), 40 * 25),
      hint='The water was 15 cm deep before. How much did the cubes make it rise?',
      steps=['The water was 15 cm deep and it rises 5 cm.', '15 + 5 = 20, so the water is now 20 cm deep.'],
      src=['Depth now:']),

    D(id='5s', tier='core', no='5 Start here', label='5 start', type='fields', skill='painted cube: edges and faces', answer=[2, 2, 2],
      q='A 4 by 4 by 4 cube is built from 64 small cubes. The outside of the big cube is painted yellow. Then it is taken apart.\nStart here: corner cubes have 3 painted faces.', svg=G.painted_cube_4(),
      frame='Cubes between 2 corners: {f1}     Middle of a face: {f2} by {f3}',
      check=lambda: [len([x for x in range(4) if (x not in (0, 3))]), len([x for x in range(4) if (x not in (0, 3))]), len([y for y in range(4) if (y not in (0, 3))])],
      hint='Look along one edge of the big cube: 4 small cubes in a row. Two of them are corners. How many are left? On a face, the cubes that are not on its edges make a square.',
      steps=['Along one edge there are 4 small cubes. The 2 corners are at the ends, so 4 − 2 = 2 cubes are between them.', 'On one face, leave out the cubes on its four edges. What is left in the middle is a 2 by 2 square.'],
      src=['An edge has 2 corners and ____ cubes between. The middle of a face is a ____ by ____ square. Fill in the table.']),
    D(id='5t2', tier='core', no='5 table: 2 faces', label='5 2-face', type='fields', skill='painted cube: 2 painted faces', answer=[2, 24],
      q='A 4 by 4 by 4 cube is built from 64 small cubes and painted on the outside, then taken apart.\nCubes with 2 painted faces are on the edges (not the corners). The big cube has 12 edges.', svg=G.painted_cube_4(),
      frame='12 edges × {f1} = {f2}', check=lambda: [paint_counts(4, 4, 4)[2] // 12, paint_counts(4, 4, 4)[2]],
      hint='How many cubes with 2 painted faces are on one edge? Then count that for all 12 edges.',
      steps=['Each edge has 2 cubes between the corners, and each of them has 2 painted faces.', '12 edges × 2 = 24 cubes with 2 painted faces.'],
      src=['12 edges × ____ = ____']),
    D(id='5t1', tier='core', no='5 table: 1 face', label='5 1-face', type='fields', skill='painted cube: 1 painted face', answer=[4, 24],
      q='A 4 by 4 by 4 cube is built from 64 small cubes and painted on the outside, then taken apart.\nCubes with 1 painted face are in the middle of a face. The big cube has 6 faces.', svg=G.painted_cube_4(),
      frame='6 faces × {f1} = {f2}', check=lambda: [paint_counts(4, 4, 4)[1] // 6, paint_counts(4, 4, 4)[1]],
      hint='How many cubes are in the middle of one face, away from its edges? Then count that for all 6 faces.',
      steps=['The middle of each face is a 2 by 2 square, so each face has 2 × 2 = 4 cubes with 1 painted face.', '6 faces × 4 = 24 cubes with 1 painted face.'],
      src=['6 faces × ____ = ____']),
    D(id='5n', tier='core', no='5 no paint', label='5 no paint', type='number', skill='painted cube: no paint', answer=8,
      q='A 4 by 4 by 4 cube is built from 64 small cubes. The outside of the big cube is painted yellow. Then it is taken apart.\nHow many small cubes have no paint at all? (Type the number of cubes.)', svg=G.painted_cube_4(),
      check=lambda: paint_counts(4, 4, 4)[0],
      hint='The cubes with no paint are hidden inside, away from every face. What block do they make?',
      steps=['Take away the outer layer from every side. The cubes with no paint make a block 2 × 2 × 2.', '2 × 2 × 2 = 8 cubes have no paint.'],
      src=['How many small cubes have no paint at all?']),
    D(id='5c', tier='core', no='5 check', label='5 check', type='selfcheck', open=False, skill='checking a total', facts=64,
      q='Check your four numbers: the cubes with 3 painted faces, 2 painted faces, 1 painted face and no paint. Do they add up to 64, the number of small cubes? Write the sum, then compare it with the model answer.',
      check=lambda: sum(paint_counts(4, 4, 4).values()), svg=None,
      sol_fig=lambda t: G.kinds_bar([('3 faces', paint_counts(4, 4, 4)[3]), ('2 faces', paint_counts(4, 4, 4)[2]), ('1 face', paint_counts(4, 4, 4)[1]), ('no paint', paint_counts(4, 4, 4)[0])]),
      hint='Add the four numbers. Is the total the number of small cubes in the whole cube?',
      steps=['8 + 24 + 24 + 8 = 64, and the big cube has 4 × 4 × 4 = 64 small cubes.', 'The picture shows all 64 cubes sorted by the number of painted faces. If your total is not 64, look for the number that is wrong.'],
      src=['Check: do your four numbers add up to 64?']),

    D(id='6a', tier='core', no='6(a)', type='text', skill='litres in a container', accept=G.dec_accepts(F(30 * 20 * 24, 1000), units=['l', 'ℓ', 'litres', 'liters', 'litre', 'L'], places=(2,)), shown='14.4',
      q='Container A is full of water. Tank B is empty.\nHow many litres of water are in container A? (Type the number of litres, like 2.5.)', svg=G.two_containers(),
      check=lambda: G.dec_text(water_litres(30, 20, 24)),
      hint='Find the volume of container A in cm³. Then change cm³ into litres.',
      steps=['Container A is full: 30 × 20 × 24 = 14 400 cm³.', '1 litre = 1000 cm³, so 14 400 ÷ 1000 = 14.4.', 'Container A holds 14.4 litres.'],
      src=['How many litres of water are in container A?']),
    D(id='6b', tier='core', no='6(b)', type='number', skill='pouring into another tank', answer=12,
      q='Container A is full of water. Tank B is empty. All of the water in A is poured into B.\nHow deep is the water in B? (Type the number of cm.)', svg=G.two_containers(),
      check=lambda: depth_for(len(cubes(30, 20, 24)), 40 * 30),
      hint='The amount of water does not change when it is poured. Find the base area of tank B. Then ask how deep that volume is over it.',
      steps=['The water is 14 400 cm³ and it does not change.', 'The base of tank B is 40 × 30 = 1200 cm².', '14 400 ÷ 1200 = 12, so the water is 12 cm deep. (Tank B is 25 cm high, so it does not overflow.)'],
      src=['All of A is poured into B. How deep is the water in B?']),

    # ================= Investigation: Find all the ways
    D(id='C0', tier='invest', no='C (easy first step)', label='C easy', type='number', skill='listing all the boxes', answer=4,
      q='Find all the ways.\nEasy first step: list every box that holds exactly 12 cubes (for example 1 × 1 × 12). How many different boxes are there? (A box turned round is the same box.)', check=lambda: len(triples(12)),
      hint='Go in order of the shortest edge. If the shortest edge is 1, what do the other two edges multiply to?',
      steps=['The boxes with exactly 12 cubes: ' + ', '.join(fmt3(t) for t in triples(12)) + '.', 'That is 4 boxes.'],
      src=['Easy first step: list every box that holds exactly 12 cubes (for example 1 × 1 × 12). Then do part (a).']),
    D(id='Ca', tier='invest', no='C(a) list', label='C(a) list', type='selfcheck', open=False, skill='listing all the boxes', facts=T48,
      q='A shop wants a box that holds exactly 48 small cubes of sugar, packed with no gaps. The box is a cuboid with whole-number edges in cubes. A 2 by 4 by 6 box is the same as a 6 by 4 by 2 box.\n'
        'Find ALL the different boxes. Make a list in order, then compare it with the model answer.',
      check=lambda: triples(48),
      hint='Go in order of the shortest edge: 1, then 2, then 3. For each one, what do the other two edges multiply to?',
      steps=['Go in order of the shortest edge. Shortest edge 1: ' + ', '.join(fmt3(t) for t in T48 if t[0] == 1) + '.', 'Shortest edge 2: ' + ', '.join(fmt3(t) for t in T48 if t[0] == 2) + '. Shortest edge 3: ' + ', '.join(fmt3(t) for t in T48 if t[0] == 3) + '.',
             'A shortest edge of 4 or more would need at least 4 × 4 × 4 = 64 cubes, which is more than 48, so the list ends here.', 'A good list is in order and has no box twice.'],
      src=['A shop wants a box that holds exactly 48 small cubes of sugar, packed with no gaps. The box is a cuboid with whole-number edges in cubes. Find ALL the different boxes (a 2 by 4 by 6 box is the same as a 6 by 4 by 2 box). Make a list in order.']),
    D(id='Ca2', tier='invest', no='C(a) how many', label='C(a) count', type='number', skill='counting all the boxes', answer=9,
      q='A shop packs exactly 48 small cubes of sugar, with no gaps, in a cuboid box with whole-number edges. A 2 by 4 by 6 box is the same as a 6 by 4 by 2 box.\nHow many different boxes can the shop use?',
      check=lambda: len(triples(48)),
      hint='Make a list in order of the shortest edge, then count the list.',
      steps=['Listed in order: ' + ', '.join(fmt3(t) for t in T48) + '.', 'That is 9 boxes.'],
      src=['Find ALL the different boxes']),
    D(id='Cb', tier='invest', no='C(b) choose', label='C(b) choose', type='selfcheck', open=True, marking_mode='open', skill='choosing and explaining',
      q='Which box would you choose to sell, and why? Write your idea. There is no single right answer.',
      hint='Think about which box would be easy to pack, to carry or to stack.',
      steps=['This question is open: many choices are good if the reason makes sense.', 'Some ideas: a box that is nearly a cube is easy to stack; a long thin box is hard to carry; a flat box is easy to fit on a shelf.'],
      src=['Which box would you choose to sell, and why?']),
    D(id='Cb2', tier='invest', no='C(b) cube', label='C(b) cube', type='set', ordered=True, grouped=False, skill='comparing boxes', answer=list(most_cubelike(T48)),
      q='Which of the boxes for 48 cubes is most like a cube? Type its three edges, smallest first, with commas.', check=lambda: list(most_cubelike(T48)),
      hint='A cube has three equal edges. Look for the box whose edges are closest to each other.',
      steps=['A cube has all three edges equal, so look for the box whose longest and shortest edges are nearest.', '3 × 4 × 4 has edges 3, 4 and 4, only 1 cm apart. Every other box has edges further apart: for example 2 × 4 × 6 has its edges 4 cm apart.'],
      src=['Which is most like a cube?']),
    D(id='Cc', tier='invest', no='C(c) 64 cubes', label='C(c) 64', type='number', skill='counting all the boxes', answer=7,
      q='What if the shop packs 64 cubes (all of them, no gaps, whole-number edges)? How many different boxes are there now?', check=lambda: len(triples(64)),
      hint='Use the same method: go in order of the shortest edge and see what the other two edges multiply to.',
      steps=['The boxes for 64 cubes: ' + ', '.join(fmt3(t) for t in T64) + '.', 'That is 7 boxes.'],
      src=['What if the shop packs 64 cubes? How many different boxes now?']),
    D(id='Cc2', tier='invest', no='C(c) one box', label='C(c) one', type='choice', skill='numbers with one box shape', options=['15 cubes', '16 cubes', '17 cubes', '18 cubes'], answer='17 cubes',
      q='Is there a number of cubes that gives only ONE box shape? Which of these numbers of cubes gives only one?',
      check=lambda: f'{one_box_choice([15, 16, 17, 18])} cubes',
      hint='Every number of cubes gives the box 1 × 1 × that number. For each choice, look for a second box.',
      steps=['15 cubes: 1 × 1 × 15 and 1 × 3 × 5. 16 cubes: 1 × 1 × 16, 1 × 2 × 8, 1 × 4 × 4 and 2 × 2 × 4. 17 cubes: only 1 × 1 × 17. 18 cubes: 1 × 1 × 18, 1 × 2 × 9, 1 × 3 × 6 and 2 × 3 × 3.',
             '17 is a prime number: its only whole-number factors are 1 and 17. So 17 cubes give only one box shape. The same is true for every prime number of cubes.'],
      src=['Is there a number of cubes that gives only ONE box shape?']),

    # ================= Think harder (A1 to A4)
    D(id='A1', tier='stretch', no='A1', type='number', skill='packing cubes in layers', answer=24,
      q='How many cubes with 2-cm edges can be packed in neat layers into a box 9 cm long, 6 cm wide and 5 cm high? (Type the number of cubes.)',
      svg=G.plain_box(9, 6, 5, 16, ('9 cm', '5 cm', '6 cm'), 'A box 9 cm long, 6 cm wide and 5 cm high.'), check=lambda: fit_count(2, 9, 6, 5),
      hint='How many 2-cm cubes fit along each edge of the box? Cubes cannot be cut, so part of a cube does not count.',
      steps=['Along the 9 cm length: 4 cubes (4 × 2 = 8 cm, with 1 cm left over). Across the 6 cm width: 3 cubes. Up the 5 cm height: 2 cubes (4 cm, with 1 cm left over).', '4 × 3 × 2 = 24 cubes.',
             'Dividing the volumes, 270 ÷ 8, does not work: the cubes cannot be cut, so the left-over space cannot be used.'],
      src=['How many cubes with 2-cm edges can be packed in neat layers into a box 9 cm long, 6 cm wide and 5 cm high?']),
    D(id='A2', tier='stretch', no='A2', type='number', skill='fractions of a tank', answer=45,
      q='A tank is 1/3 full of water. After 12 ℓ more is poured in, it is 3/5 full. How many litres does the tank hold when full? (Type the number of litres.)', check=a2_capacity,
      hint='The 12 ℓ fill the gap between 1/3 and 3/5 of the tank. What fraction of the tank is that gap?',
      steps=['The water goes from 1/3 to 3/5 of the tank. 3/5 − 1/3 = 9/15 − 5/15 = 4/15.', '4/15 of the tank is 12 ℓ, so 1/15 is 12 ÷ 4 = 3 ℓ.', 'The whole tank is 15 × 3 = 45 ℓ.'],
      src=['A tank is 1/3 full of water. After 12 ℓ more is poured in, it is 3/5 full. How many litres does the tank hold when full?']),
    D(id='A3', tier='stretch', no='A3', type='number', skill='working backwards from the volume', answer=7,
      q='A cuboid has a square base and a height of 5 cm. Its volume is 245 cm³. How long is each side of the base? (Type the number of cm.)', check=a3_side,
      hint='Volume = base area × height. First find the area of the base. Then ask which number times itself gives that area.',
      steps=['The base area is 245 ÷ 5 = 49 cm².', 'The base is a square, so each side times itself is 49: 7 × 7 = 49.', 'Each side of the base is 7 cm.'],
      src=['A cuboid has a square base and a height of 5 cm. Its volume is 245 cm³. How long is each side of the base?']),
    D(id='A4', tier='stretch', no='A4', type='number', skill='painted cuboid: no paint', answer=6,
      q='A cuboid 3 cm by 4 cm by 5 cm is built from 1-cm cubes and painted on the outside. How many cubes have no paint at all? (Type the number of cubes.)',
      svg=G.cuboid_grid(5, 4, 3, 28, 'A cuboid 5 cubes long, 4 cubes wide and 3 cubes high, built from 1-centimetre cubes and painted on the outside.'),
      check=lambda: paint_counts(5, 4, 3)[0],
      hint='The cubes with no paint are hidden inside. Take off the outer layer from every side: what block is left?',
      steps=['Take off the outer layer of cubes on every side: each length goes down by 2 cm, one layer off each end.', 'The inside block is 1 × 2 × 3 cubes.', '1 × 2 × 3 = 6 cubes have no paint.'],
      src=['A cuboid 3 cm by 4 cm by 5 cm is built from 1-cm cubes and painted on the outside. How many cubes have no paint at all?']),

    # ================= Go further (B1 to B3)
    D(id='B1', tier='challenge', no='B1', type='number', skill='edges from face areas', answer=60,
      q='Three faces of a cuboid have areas 12 cm², 15 cm² and 20 cm². What is the volume of the cuboid? (Type the number of cm³.)', check=b1_volume,
      hint='Each face is made from two of the edges. Find three whole numbers so that two of them multiply to 12, two multiply to 15 and two multiply to 20.',
      steps=['Call the edges a, b and c. Then a × b = 12, a × c = 15 and b × c = 20 (the three faces that meet at a corner).', 'Try whole numbers: 3 × 4 = 12, 3 × 5 = 15 and 4 × 5 = 20 all work, so the edges are 3 cm, 4 cm and 5 cm.', 'Volume = 3 × 4 × 5 = 60 cm³.'],
      src=['Three faces of a cuboid have areas 12 cm², 15 cm² and 20 cm². What is the volume of the cuboid?']),
    D(id='B2', tier='challenge', no='B2', type='fields', skill='painted cuboid: 2 faces and 1 face', answer=[24, 22],
      q='A cuboid 3 cm by 4 cm by 5 cm is built from 1-cm cubes and painted on the outside.\nHow many cubes have exactly 2 painted faces? How many have exactly 1?',
      svg=G.cuboid_grid(5, 4, 3, 28, 'A cuboid 5 cubes long, 4 cubes wide and 3 cubes high, built from 1-centimetre cubes and painted on the outside.'),
      frame='Exactly 2 painted faces: {f1}     Exactly 1 painted face: {f2}', check=lambda: [paint_counts(5, 4, 3)[2], paint_counts(5, 4, 3)[1]],
      hint='Cubes with 2 painted faces are on the edges but not at the corners. Cubes with 1 painted face are in the middle of a face. Count them edge by edge or face by face.',
      steps=['Cubes with exactly 2 painted faces are along the edges, between the corners. The 4 edges that are 5 cm long have 3 cubes each, the 4 that are 4 cm long have 2 each and the 4 that are 3 cm long have 1 each: 12 + 8 + 4 = 24.',
             'Cubes with exactly 1 painted face are in the middle of a face. Two faces are 5 by 4 (3 × 2 = 6 in the middle), two are 5 by 3 (3 × 1 = 3) and two are 4 by 3 (2 × 1 = 2): 12 + 6 + 4 = 22.',
             'Check: 8 corners + 24 + 22 + 6 with no paint = 60 cubes.'],
      src=['A cuboid 3 cm by 4 cm by 5 cm is built from 1-cm cubes and painted on the outside. How many cubes have exactly 2 painted faces? How many have exactly 1?']),
    D(id='B3', tier='challenge', no='B3', type='number', skill='water level around a block', answer=12,
      q='A tank has a base 30 cm by 20 cm and water 10 cm deep. A block 10 cm by 10 cm by 15 cm is stood upright on the bottom. How deep is the water now? (Type the number of cm.)',
      svg=G.tank_block(), check=b3_depth,
      hint='The block takes up part of the floor of the tank, and it is taller than the water. How much floor is left for the water to spread over?',
      steps=['The water is 30 × 20 × 10 = 6000 cm³ and it does not change.', 'The block stands on the floor and is taller than the water, so it covers 10 × 10 = 100 cm² of the floor. The water spreads over 600 − 100 = 500 cm².',
             '6000 ÷ 500 = 12, so the water is 12 cm deep. That is less than the 15 cm of the block, so the block still sticks out.',
             'Adding the whole block, 10 × 10 × 15 = 1500 cm³, to the water would be wrong: the block sticks out of the water.'],
      src=['A tank has a base 30 cm by 20 cm and water 10 cm deep. A block 10 cm by 10 cm by 15 cm is stood upright on the bottom. How deep is the water now?']),
    D(id='pose', tier='challenge', no='Make up your own', label='Make up', type='selfcheck', open=True, marking_mode='open', skill='making up a problem',
      q='Make up a tank puzzle with a stone: choose the base, the depth of the water and the stone. Swap and solve. (Think for 30 seconds before anyone speaks.)',
      hint='Choose the base and the depth first. Then pick a stone whose volume makes a nice rise, such as a volume that fits a whole number of layers.',
      steps=['This question is open: many puzzles are right.', 'Check your puzzle by solving it two ways, for example by finding the volume of water before and after.',
             'Sample: a tank has a base 25 cm by 20 cm and water 10 cm deep. A stone of 1000 cm³ sinks. The base is 500 cm², so the water rises 1000 ÷ 500 = 2 cm and is 12 cm deep.'],
      src=['Make up a tank puzzle with a stone: choose the base, the depth of the water and the stone. Swap and solve.']),
]


# ---------------------------------------------------------------- variants: a template with an oracle that counts, lists or searches
def _o_1a(e):
    return len(cubes(e['L'], e['B'], e['H']))


def _o_3a(e):
    return whole(water_litres(e['L'], e['B'], e['W']))


def _o_4b(e):
    base = (20 * e['a']) * 25
    found = [d for d in range(1, 100) if base * d == e['k'] * len(cubes(10, 10, 10))]
    assert len(found) == 1
    return found[0]


def _o_a1(e):
    return fit_count(2, e['L'], e['B'], e['H'])


def _o_a2(e):
    found = [c for c in range(1, 3000) if F(3, 5) * c - F(1, 3) * c == e['m']]
    assert len(found) == 1
    return found[0]


def _o_a3(e):
    v = e['s'] * e['s'] * e['h']
    found = [s for s in range(1, 200) if s * s * e['h'] == v]
    assert len(found) == 1
    return found[0]


def _o_a4(e):
    return paint_counts(e['L'], e['B'], e['H'])[0]


def _o_b1(e):
    A, Bc, C = e['a'] * e['b'], e['a'] * e['c'], e['b'] * e['c']
    sols = [(a, b, c) for a in range(1, 31) for b in range(1, 31) for c in range(1, 31) if a * b == A and a * c == Bc and b * c == C]
    assert len(sols) == 1
    return sols[0][0] * sols[0][1] * sols[0][2]


def _o_b2(e):
    pc = paint_counts(e['L'], e['B'], e['H'])
    return dict(f1=pc[2], f2=pc[1])


def _o_b3(e):
    water = 30 * 20 * e['W']
    found = [F(half, 2) for half in range(1, 100) if 30 * 20 * F(half, 2) - 10 * 10 * min(F(half, 2), e['Hb']) == water]
    assert len(found) == 1 and found[0] < e['Hb']
    return whole(found[0])


finish(ITEMS)

VARIANTS = {
    '1a': dict(
        base=dict(L=4, B=3, H=2),
        tpl=dict(vars=dict(L=[3, 4, 5, 6], B=[2, 3, 4, 5], H=[2, 3, 4]),
                 q='A solid cuboid is built from 1-cm cubes. It is {L} cubes long, {B} cubes deep and {H} cubes high. What is its volume? (Type the number of cm³.)', answer='L * B * H',
                 hint='Count the cubes in one layer first. How many layers are there?',
                 steps=['One layer has {L} × {B} cubes.', 'There are {H} layers. Multiply the cubes in a layer by the number of layers.', 'The volume is {ans} cm³.']),
        oracle=_o_1a),
    '3a': dict(
        base=dict(L=50, B=30, W=18),
        tpl=dict(vars=dict(L=[40, 50, 60], B=[20, 30, 40], W=[10, 20, 30]),
                 q='A glass tank is {L} cm long and {B} cm wide. The water in it is {W} cm deep. How many litres of water are in the tank? (Type the number of litres.)', answer='L * B * W / 1000',
                 hint='Find the volume of the water in cm³ first. Then change cm³ into litres.',
                 steps=['The water is {L} × {B} × {W} cm³, and 1 litre = 1000 cm³.', 'Divide the cm³ by 1000.', 'There are {ans} litres of water.']),
        oracle=_o_3a),
    '4b': dict(
        base=dict(a=2, k=5),
        tpl=dict(vars=dict(a=[1, 2, 3, 6], k=[3, 6, 12]), derive=dict(w='20 * a'),
                 q='A tank has a base {w} cm by 25 cm. Ali drops in {k} metal cubes with edges of 10 cm. They sink and are completely under water. How much does the water rise? (Type the number of cm.)',
                 answer='2 * k / a', hint='The cubes push up a new slice of water with the same volume as the cubes. How thick is a slice of that volume over the base?',
                 steps=['One cube is 10 × 10 × 10 = 1000 cm³, so the cubes are {k} × 1000 cm³.', 'The base is {w} × 25 cm². Divide the volume of the cubes by the base area.', 'The water rises {ans} cm.']),
        oracle=_o_4b),
    'A1': dict(
        base=dict(L=9, B=6, H=5),
        tpl=dict(vars=dict(L=[7, 8, 9, 11], B=[5, 6, 7], H=[4, 5, 6, 7]),
                 q='How many cubes with 2-cm edges can be packed in neat layers into a box {L} cm long, {B} cm wide and {H} cm high? (Type the number of cubes.)', answer='(L // 2) * (B // 2) * (H // 2)',
                 hint='How many 2-cm cubes fit along each edge of the box? Cubes cannot be cut, so part of a cube does not count.',
                 steps=['Along each edge, count how many 2-cm cubes fit. Any part left over is wasted.', 'Multiply the three numbers.', 'The box holds {ans} cubes.']),
        oracle=_o_a1),
    'A2': dict(
        base=dict(m=12),
        tpl=dict(vars=dict(m=[8, 12, 16, 20, 24]),
                 q='A tank is 1/3 full of water. After {m} ℓ more is poured in, it is 3/5 full. How many litres does the tank hold when full? (Type the number of litres.)', answer='m * 15 / 4',
                 hint='The litres poured in fill the gap between 1/3 and 3/5 of the tank. What fraction of the tank is that gap?',
                 steps=['The gap is 3/5 − 1/3 = 9/15 − 5/15 = 4/15 of the tank.', '4/15 of the tank is {m} ℓ. Find 1/15, then 15/15.', 'The tank holds {ans} ℓ when full.']),
        oracle=_o_a2),
    'A3': dict(
        base=dict(s=7, h=5),
        tpl=dict(vars=dict(s=[3, 4, 6, 7, 8], h=[4, 5, 6, 10]), derive=dict(V='s * s * h'),
                 q='A cuboid has a square base and a height of {h} cm. Its volume is {V} cm³. How long is each side of the base? (Type the number of cm.)', answer='s',
                 hint='Volume = base area × height. First find the area of the base. Then ask which number times itself gives that area.',
                 steps=['The base area is {V} ÷ {h} cm².', 'The base is a square: find the number that multiplied by itself gives the base area.', 'Each side of the base is {ans} cm.']),
        oracle=_o_a3),
    'A4': dict(
        base=dict(L=5, B=4, H=3),
        tpl=dict(vars=dict(L=[3, 4, 5, 6], B=[4, 5, 6], H=[3, 5, 7]),
                 q='A cuboid {L} cm by {B} cm by {H} cm is built from 1-cm cubes and painted on the outside. How many cubes have no paint at all? (Type the number of cubes.)', answer='(L - 2) * (B - 2) * (H - 2)',
                 hint='The cubes with no paint are hidden inside. Take off the outer layer from every side: what block is left?',
                 steps=['Take off one layer of cubes from each end of every edge: each length goes down by 2.', 'The inside block is {L} − 2 by {B} − 2 by {H} − 2 cubes. Multiply them.', '{ans} cubes have no paint.']),
        oracle=_o_a4),
    'B1': dict(
        base=dict(a=3, b=4, c=5),
        tpl=dict(vars=dict(a=[2, 3, 4, 5], b=[3, 4, 6], c=[5, 6, 7]), derive=dict(x='a * b', y='a * c', z='b * c'),
                 q='Three faces of a cuboid have areas {x} cm², {y} cm² and {z} cm². What is the volume of the cuboid? (Type the number of cm³.)', answer='a * b * c',
                 hint='Each face is made from two of the edges. Find three whole numbers so that two of them multiply to each of the three areas.',
                 steps=['Call the edges a, b and c, so a × b, a × c and b × c are the three face areas.', 'Find three whole numbers that fit. Then multiply them for the volume.', 'The volume is {ans} cm³.']),
        oracle=_o_b1),
    'B2': dict(
        base=dict(L=5, B=4, H=3),
        tpl=dict(vars=dict(L=[3, 4, 5, 6], B=[4, 5, 6], H=[3, 5, 7]),
                 q='A cuboid {L} cm by {B} cm by {H} cm is built from 1-cm cubes and painted on the outside.\nHow many cubes have exactly 2 painted faces? How many have exactly 1?',
                 frame='Exactly 2 painted faces: {f1}     Exactly 1 painted face: {f2}', answers=dict(f1='4 * ((L - 2) + (B - 2) + (H - 2))', f2='2 * ((L - 2) * (B - 2) + (L - 2) * (H - 2) + (B - 2) * (H - 2))'),
                 hint='Cubes with 2 painted faces are on the edges but not at the corners. Cubes with 1 painted face are in the middle of a face.',
                 steps=['Each edge has 2 fewer cubes than its length (the 2 corners are left out). Four edges of each kind.', 'On each face, the middle is a rectangle with 2 fewer along each side. Two faces of each kind.', 'The two numbers are {ans}.']),
        oracle=_o_b2),
    'B3': dict(
        base=dict(W=10, Hb=15),
        tpl=dict(vars=dict(W=[5, 10, 15], Hb=[20, 25]),
                 q='A tank has a base 30 cm by 20 cm and water {W} cm deep. A block 10 cm by 10 cm by {Hb} cm is stood upright on the bottom. How deep is the water now? (Type the number of cm.)', answer='6 * W / 5',
                 hint='The block takes up part of the floor of the tank, and it is taller than the water. How much floor is left for the water to spread over?',
                 steps=['The water is 30 × 20 × {W} cm³ and it does not change.', 'The block covers 10 × 10 = 100 cm² of the floor, so the water spreads over 600 − 100 = 500 cm².', 'The depth is {ans} cm, which is less than the height of the block.']),
        oracle=_o_b3),
}


polish(ITEMS, VARIANTS)
