"""Level 4 (P4) re-budget: the single plan of record for the clock of every lesson (docs/audit/timing_p4.md section 6,
applied in docs/audit/rebudget_p4.md).

    python3 rebuild/p4_budget.py        # checks the plan and writes p4/budget.json

Used by
  * rebuild/p4_fix.py  (title-slide 'Time plan', clock checks for every slide pill),
  * p4/guide.js        (segment times, routine table; reads p4/budget.json),
  * tutor/build_data.py (reads p4/budget.json).

All times are minutes from the start of the lesson, in half minutes. Every lesson adds up to 90.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'p4', 'budget.json')

# durations in minutes, in lesson order (audit section 6, per-lesson tables)
#        sneak warm explore mini break | WS-a  WS-b WS-c WS-d  WS-e | talk exit looking [certificates]
DUR = {
 1: dict(sneak=5.5, warm=5.5, explore=12.0, mini=8.0, brk=3.5, a=18.0, b=2.5, c=3.5, d=17.0, e=2.5, talk=3.5, exit=3.5, look=3.5),
 2: dict(sneak=5.0, warm=5.0, explore=13.0, mini=5.0, brk=3.5, a=17.5, b=2.0, c=4.0, d=20.0, e=3.5, talk=3.5, exit=3.0, look=3.5),
 3: dict(sneak=5.0, warm=5.0, explore=12.0, mini=5.0, brk=4.0, a=16.5, b=2.0, c=2.5, d=23.0, e=4.0, talk=3.5, exit=2.5, look=3.5),
 4: dict(sneak=5.0, warm=5.0, explore=12.5, mini=8.0, brk=3.5, a=17.5, b=2.5, c=3.5, d=18.0, e=2.5, talk=4.0, exit=3.0, look=3.5),
 5: dict(sneak=5.0, warm=5.0, explore=13.5, mini=8.0, brk=3.5, a=18.5, b=2.0, c=5.0, d=15.5, e=2.0, talk=3.5, exit=3.5, look=3.5),
 6: dict(sneak=5.0, warm=5.0, explore=11.5, mini=7.5, brk=3.5, a=17.5, b=1.5, c=2.5, d=22.0, e=2.5, talk=3.5, exit=3.0, look=3.5),
 7: dict(sneak=5.0, warm=5.0, explore=12.0, mini=5.5, brk=3.5, a=16.0, b=2.0, c=3.5, d=21.0, e=3.5, talk=4.0, exit=4.0, look=3.5),
 8: dict(sneak=5.0, warm=5.0, explore=14.0, mini=8.5, brk=3.5, a=19.0, b=2.5, c=3.5, d=15.0, e=2.5, talk=4.0, exit=2.5, look=3.5),
 9: dict(sneak=5.0, warm=5.0, explore=14.5, mini=6.5, brk=3.5, a=18.0, b=2.0, c=4.0, d=17.5, e=2.5, talk=3.5, exit=3.0, look=3.5),
 10: dict(sneak=5.0, warm=5.0, explore=13.0, mini=6.5, brk=3.5, a=16.5, b=1.5, c=3.5, d=17.0, e=3.0, talk=3.5, exit=4.5, look=3.5, cert=2.5),
}
OPEN = 1.5
# standing buffer inside the page-2 solo block (audit F11: 2 to 3 minutes); it is the last stretch of that block, so a late start eats it first
BUFFER = {1: 3.0, 2: 3.0, 3: 3.0, 4: 2.0, 5: 2.5, 6: 3.0, 7: 3.0, 8: 2.5, 9: 2.0, 10: 2.0}

# Slide windows (the time pills). (slide suffix, start, end). Optional slides keep a window only when they are on the clock.
SLIDES = {
 1: [('title', 0, 1.5), ('check', 1.5, 7), ('warm1', 7, 9), ('warm2', 9, 12.5), ('explore1', 12.5, 21.5), ('explore2', 21.5, 24.5),
     ('teach1', 24.5, 26), ('we1', 26, 27.5), ('we2', 27.5, 29), ('we3', 29, 30), ('try2', 30, 31.5), ('key', 31.5, 32.5), ('break', 32.5, 36),
     ('ws1', 36, 54), ('ws1ans', 54, 56.5), ('teachodd', 56.5, 58), ('teachriddle', 58, 59), ('teachtest', 59, 60), ('ws2', 60, 77), ('ws2ans', 77, 79.5),
     ('talk', 79.5, 83), ('exit', 83, 86.5), ('reflect', 86.5, 90)],
 2: [('title', 0, 1.5), ('check', 1.5, 6.5), ('warm1', 6.5, 8.5), ('warm2', 8.5, 11.5), ('explore1', 11.5, 21), ('explore2', 21, 24.5),
     ('we1', 24.5, 25.5), ('we2', 25.5, 26.5), ('we4', 26.5, 27.5), ('we3', 27.5, 28.5), ('key', 28.5, 29.5), ('break', 29.5, 33),
     ('ws1', 33, 50.5), ('ws1ans', 50.5, 52.5), ('teachriddle', 52.5, 54), ('teachpattern', 54, 55), ('teachcards', 55, 56.5), ('ws2', 56.5, 76.5), ('ws2ans', 76.5, 80),
     ('talk', 80, 83.5), ('exit', 83.5, 86.5), ('reflect', 86.5, 90)],
 3: [('title', 0, 1.5), ('check', 1.5, 6.5), ('warm1', 6.5, 8.5), ('warm2', 8.5, 11.5), ('explore1', 11.5, 20.5), ('explore2', 20.5, 23.5),
     ('teach1', 23.5, 25), ('we1', 25, 26), ('we2', 26, 27.5), ('key', 27.5, 28.5), ('break', 28.5, 32.5),
     ('ws1', 32.5, 49), ('ws1ans', 49, 51), ('teachback', 51, 52), ('teachbar', 52, 53.5), ('ws2', 53.5, 76.5), ('ws2ans', 76.5, 80.5),
     ('talk', 80.5, 84), ('exit', 84, 86.5), ('reflect', 86.5, 90)],
 4: [('title', 0, 1.5), ('check', 1.5, 6.5), ('warm1', 6.5, 8.5), ('warm2', 8.5, 11.5), ('explore1', 11.5, 21), ('explore2', 21, 24),
     ('teach1', 24, 25.5), ('we1', 25.5, 27), ('teachline', 27, 28.5), ('we2', 28.5, 30), ('try2', 30, 31), ('key', 31, 32), ('break', 32, 35.5),
     ('ws1', 35.5, 53), ('ws1ans', 53, 55.5), ('teachcompare', 55.5, 56.5), ('teachcompare2', 56.5, 57.5), ('teachwhole', 57.5, 58.5), ('teachfind', 58.5, 59),
     ('ws2', 59, 77), ('ws2ans', 77, 79.5), ('talk', 79.5, 83.5), ('exit', 83.5, 86.5), ('reflect', 86.5, 90)],
 5: [('title', 0, 1.5), ('check', 1.5, 6.5), ('warm1', 6.5, 8.5), ('warm2', 8.5, 11.5), ('explore1', 11.5, 21.5), ('explore2', 21.5, 25),
     ('teach1', 25, 26.5), ('we1', 26.5, 28), ('we2', 28, 29.5), ('we3', 29.5, 31), ('try2', 31, 32), ('key', 32, 33), ('break', 33, 36.5),
     ('ws1', 36.5, 55), ('ws1ans', 55, 57), ('teachcards', 57, 58), ('teachbar', 58, 60), ('teachmass', 60, 61), ('teachclue', 61, 62),
     ('ws2', 62, 77.5), ('ws2ans', 77.5, 79.5), ('talk', 79.5, 83), ('exit', 83, 86.5), ('reflect', 86.5, 90)],
 6: [('title', 0, 1.5), ('check', 1.5, 6.5), ('warm1', 6.5, 8.5), ('warm2', 8.5, 11.5), ('explore1', 11.5, 20.5), ('explore2', 20.5, 23),
     ('teach1', 23, 25.5), ('teach2', 25.5, 28), ('try2', 28, 29.5), ('key', 29.5, 30.5), ('break', 30.5, 34),
     ('teachfan', 34, 36), ('ws1', 36, 51.5), ('ws1ans', 51.5, 53), ('teachclock', 53, 54), ('teachrect', 54, 54.5), ('teachrobot', 54.5, 55.5),
     ('ws2', 55.5, 77.5), ('ws2ans', 77.5, 80), ('talk', 80, 83.5), ('exit', 83.5, 86.5), ('reflect', 86.5, 90)],
 7: [('title', 0, 1.5), ('check', 1.5, 6.5), ('warm1', 6.5, 8.5), ('warm2', 8.5, 11.5), ('explore1', 11.5, 20.5), ('explore2', 20.5, 23.5),
     ('teach1', 23.5, 25), ('we1', 25, 26.5), ('we2', 26.5, 28), ('key', 28, 29), ('break', 29, 32.5),
     ('ws1', 32.5, 48.5), ('ws1ans', 48.5, 50.5), ('teachstair', 50.5, 51.5), ('teachcut', 51.5, 53), ('teachframe', 53, 54), ('ws2', 54, 75), ('ws2ans', 75, 78.5),
     ('talk', 78.5, 82.5), ('exit', 82.5, 86.5), ('reflect', 86.5, 90)],
 8: [('title', 0, 1.5), ('check', 1.5, 6.5), ('warm1', 6.5, 8.5), ('warm2', 8.5, 11.5), ('explore1', 11.5, 22), ('explore2', 22, 25.5),
     ('teach1', 25.5, 27.5), ('we1', 27.5, 29.5), ('we2', 29.5, 31.5), ('try2', 31.5, 33), ('key', 33, 34), ('break', 34, 37.5),
     ('ws1', 37.5, 56.5), ('ws1ans', 56.5, 59), ('teachsym', 59, 60), ('teachlines', 60, 61.5), ('teachshade', 61.5, 62.5), ('ws2', 62.5, 77.5), ('ws2ans', 77.5, 80),
     ('talk', 80, 84), ('exit', 84, 86.5), ('reflect', 86.5, 90)],
 9: [('title', 0, 1.5), ('check', 1.5, 6.5), ('warm1', 6.5, 8.5), ('warm2', 8.5, 11.5), ('explore1', 11.5, 22.5), ('explore2', 22.5, 26),
     ('teach1', 26, 27.5), ('we1', 27.5, 29), ('we2', 29, 30.5), ('try2', 30.5, 31.5), ('key', 31.5, 32.5), ('break', 32.5, 36),
     ('ws1', 36, 54), ('ws1ans', 54, 56), ('teachtwo', 56, 57.5), ('teachsteps', 57.5, 58.5), ('teachscale', 58.5, 60), ('ws2', 60, 77.5), ('ws2ans', 77.5, 80),
     ('talk', 80, 83.5), ('exit', 83.5, 86.5), ('reflect', 86.5, 90)],
 10: [('title', 0, 1.5), ('check', 1.5, 6.5), ('warm1', 6.5, 8.5), ('warm2', 8.5, 11.5), ('explore1', 11.5, 21.5), ('explore2', 21.5, 24.5),
      ('teach1', 24.5, 25.5), ('we1', 25.5, 27), ('we2', 27, 28.5), ('try2', 28.5, 29.5), ('we3', 29.5, 30.5), ('key', 30.5, 31), ('break', 31, 34.5),
      ('ws1', 34.5, 51), ('ws1ans', 51, 52.5), ('teachlogic', 52.5, 54), ('teachqueue', 54, 55), ('teachages', 55, 56), ('ws2', 56, 73), ('ws2ans', 73, 76),
      ('talk', 76, 79.5), ('exit', 79.5, 84), ('reflect', 84, 87.5), ('end', 87.5, 90)],
}
# kept "your turn" slides: on the clock, but optional (skip if behind)
KEPT_TRY = {1: ['try2'], 2: [], 3: [], 4: ['try2'], 5: ['try2'], 6: ['try2'], 7: [], 8: ['try2'], 9: ['try2'], 10: ['try2']}
# early-finisher / take-home slides: no clock time ("Optional, if you finish early")
EARLY = {n: ['stretch', 'challenge', 'chdiag', 'chwalk'] for n in range(1, 11)}
EARLY[3] = EARLY[3] + ['teachchain']
OPT_PILL = 'Optional, if you finish early'


def fmt(x):
    return ('%g' % x)


def pill(n, suffix):
    """text of the time pill of slide p4l<n>-<suffix>"""
    if suffix in EARLY[n]:
        return OPT_PILL
    for s, a, b in SLIDES[n]:
        if s == suffix:
            return '%s–%s MIN%s' % (fmt(a), fmt(b), ' • OPTIONAL' if suffix in KEPT_TRY[n] else '')
    raise KeyError((n, suffix))


def window(n, suffix):
    for s, a, b in SLIDES[n]:
        if s == suffix:
            return a, b
    return None


def parts(n):
    """[(title, start, end)] in lesson order (guide segments; the Worksheet is one part)"""
    d = DUR[n]; t = 0.0; out = []
    def add(title, dur):
        nonlocal t
        out.append((title, t, t + dur)); t += dur
    add('Opening', OPEN); add('Sneak-peek puzzles', d['sneak']); add('Warm-up', d['warm']); add('Explore (in pairs)', d['explore'])
    add('Mini-lesson', d['mini']); add('Brain break', d['brk'])
    add('Worksheet', d['a'] + d['b'] + d['c'] + d['d'] + d['e'])
    add('Talk time', d['talk']); add('Exit ticket', d['exit']); add('Looking back', d['look'])
    if 'cert' in d: add('Certificates and goodbye', d['cert'])
    return out


def ws_blocks(n):
    d = DUR[n]; start = [p for p in parts(n) if p[0] == 'Worksheet'][0][1]; t = start; out = []
    for key, title in (('a', 'Start here, page 1 in pairs'), ('b', 'Check page 1'), ('c', 'Short teaching before page 2'), ('d', 'Page 2 on your own (includes buffer)'), ('e', 'Check page 2')):
        out.append((title, t, t + d[key])); t += d[key]
    return out


def buffer_window(n):
    ws = ws_blocks(n)[3]
    return ws[2] - BUFFER[n], ws[2]


def part_at(n, minute):
    for title, a, b in parts(n):
        if a <= minute < b:
            return title
    return None


def check():
    for n in DUR:
        ps = parts(n)
        assert abs(ps[-1][2] - 90) < 1e-9, (n, ps[-1])
        # slide windows are contiguous, ordered, start at 0 and end at 90
        t = 0
        for s, a, b in SLIDES[n]:
            assert abs(a - t) < 1e-9 and b > a, (n, s, a, t)
            t = b
        assert t == 90, (n, t)
        # worksheet blocks tile the Worksheet part
        wb = ws_blocks(n); w = [p for p in ps if p[0] == 'Worksheet'][0]
        assert wb[0][1] == w[1] and abs(wb[-1][2] - w[2]) < 1e-9, n
        # each part boundary falls on a slide boundary
        edges = {a for _, a, _ in SLIDES[n]} | {90}
        for title, a, b in ps:
            assert a in edges, (n, title, a)
        # worksheet block edges too
        for title, a, b in wb:
            assert a in edges or title.startswith('Page 2'), (n, title, a)
        for s in KEPT_TRY[n]:
            assert window(n, s), (n, s)


def num(x):
    return int(x) if float(x).is_integer() else float(x)


def budget_json():
    out = {'lessons': {}}
    for n in sorted(DUR):
        bw = buffer_window(n)
        opt = [f'p4l{n}-{s}' for s in KEPT_TRY[n]] + [f'p4l{n}-{s}' for s in EARLY[n]]
        out['lessons'][str(n)] = {
            'parts': [{'title': t, 'start': num(a), 'end': num(b)} for t, a, b in parts(n)],
            'optional_slides': opt,
            'worksheet_blocks': [{'title': t, 'start': num(a), 'end': num(b)} for t, a, b in ws_blocks(n)],
            'buffer': {'title': 'Buffer', 'start': num(bw[0]), 'end': num(bw[1]), 'within': 'Worksheet'},
        }
    return out


if __name__ == '__main__':
    check()
    json.dump(budget_json(), open(OUT, 'w'), ensure_ascii=False, indent=1)
    print('ok, wrote', os.path.normpath(OUT))
