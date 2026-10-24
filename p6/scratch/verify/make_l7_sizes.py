#!/usr/bin/env python3
"""Builds a test-only project (not given to children) with every Lesson 7 drawing the slides and workbook ask for,
each on its own key, starting from the standard set-up (erase all, go to x: -50 y: 100, point in direction 90, pen down).
Usage: python3 make_l7_sizes.py <out.sb3>   (then run l7_sizes_check.js on it).  Prints the program table as JSON."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import build_sb3 as B

# key, label, repeats, move, turn, start (None = standard set-up)
PROGS = [
    ('a', 'triangle', 3, 100, 120, None), ('b', 'square', 4, 100, 90, None), ('c', 'pentagon', 5, 100, 72, None),
    ('d', 'hexagon', 6, 100, 60, None), ('e', 'octagon', 8, 80, 45, None), ('f', '9-gon', 9, 80, 40, None),
    ('g', '10-gon', 10, 80, 36, None), ('h', '12-gon', 12, 50, 30, None), ('i', '15-gon', 15, 50, 24, None),
    ('j', '24-gon', 24, 30, 15, None), ('k', '36-gon', 36, 10, 10, None),
    ('l', 'Ben nonagon (turn 120)', 9, 80, 120, None), ('m', '5-point star', 5, 150, 144, None),
    ('n', 'Q3 program: 9 x (move 150, turn 80)', 9, 150, 80, None), ('o', '9-point star, 4 times round', 9, 120, 160, None),
    ('p', '20-point star, 3 times round', 20, 100, 54, None), ('q', '10-point star (turn 108)', 10, 150, 108, None),
    ('r', '8-point star (turn 135)', 8, 100, 135, None), ('s', "Ali's pentagon (turn 108, does not close)", 5, 100, 108, None),
    ('t', 'hexagon trial: turn 120 x 6', 6, 100, 120, None),
]


def build(path):
    p = B.Proj('L7 sizes'); S = p.sprite; p.sprite_art = 'arrow'; p.extensions = ['pen']
    p.x, p.y = -50, 100
    p.var('fx', 0, True); p.var('fy', 0, True, (5, 30)); p.var('fd', 0, True, (5, 55))
    for key, label, n, move, turn, start in PROGS:
        body = [S.erase(), S.goto(-50, 100), S.point(90), S.pendown(), S.repeat(n, [S.move(move), S.turnr(turn)]),
                S.setv('fx', S.xpos()), S.setv('fy', S.b('motion_yposition')), S.setv('fd', S.b('motion_direction'))]
        S.script(S.key(key), body)
    # rosette extension (starts from go to x: 0 y: 0, as the lesson says)
    S.script(S.key('u'), [S.erase(), S.goto(0, 0), S.point(90), S.pendown(),
                          S.repeat(12, [S.repeat(4, [S.move(100), S.turnr(90)]), S.turnr(30)]),
                          S.setv('fx', S.xpos()), S.setv('fy', S.b('motion_yposition')), S.setv('fd', S.b('motion_direction'))])
    p.save(path)
    rows = [dict(key=k, label=l, n=n, move=m, turn=t, start=[-50, 100]) for k, l, n, m, t, s in PROGS]
    rows.append(dict(key='u', label='rosette: 12 x (square, turn 30), from 0,0', n=12, move=100, turn=30, start=[0, 0], rosette=True))
    return rows


if __name__ == '__main__':
    print(json.dumps(build(sys.argv[1])))
