#!/usr/bin/env python3
"""P3 re-budget (docs/audit/timing_p3.md): the single source of the new 90-minute clock.

    python3 rebuild/p3_rebudget.py        # rewrites p3/budget.json and the "plan" of every lesson in p3/gifted.json

Each lesson is eight parts; each part lists its slides with their length in minutes (slides are shown in this order).
  p3/budget.json   parts (title, start, end) and optional_slides: read by the tutor console timer
  p3/gifted.json   "plan": slide id -> [start, end]; read by rebuild/p3_gifted.py (slide pills, notes) and p3/guide.js (scripts)
Optional slides (Think harder / Go further) keep a plan window (the 3-minute 'choose' time) but their pill says
'Optional, if you finish early' and carries no clock time.
Part budgets are the audit's proposal; every lesson sums to 90 and Talk time holds the named 3-minute float."""
import json, os
H = os.path.dirname(os.path.abspath(__file__)); P3 = os.path.join(H, '..', 'p3')
TITLES = ['Opening', 'Sneak-peek, game and quick questions', 'Explore', 'Mini-lesson', 'Brain break', 'Worksheet', 'Talk time', 'Exit ticket, look back and close']
OPT = ['stretch', 'challenge', 'chdiag', 'chwalk']
# lesson -> list of 8 parts; a part is (budget, [(slide id, minutes), ...])
L = {
 1: [(1.5, [('title', 1.5)]), (9.5, [('warmcheck', 3.5), ('warm1', 3), ('warm2', 3)]), (13, [('explore1', 9), ('explore2', 4)]),
     (11, [('teach1', 2.5), ('we1', 2), ('we2', 1.5), ('try1', 1.5), ('teach2', 2.5), ('key', 1)]), (5, [('break', 5)]),
     (31, [('teachpat', 2), ('ws1', 13), ('ws1ans', 1.5), ('teachrename', 1.5), ('teachclues', 2), ('ws2', 6.5), ('ws2ans', 1.5), ('stretch', 3)]),
     (8, [('talk', 8)]), (11, [('exit', 6), ('reflect', 3), ('close', 2)])],
 2: [(1.5, [('title', 1.5)]), (9.5, [('warmcheck', 3.5), ('warm1', 3), ('warm2', 3)]), (14, [('explore1', 10), ('explore2', 4)]),
     (9, [('teach1', 2), ('try1', 1.5), ('teach2', 2), ('teach3', 2.5), ('key', 1)]), (5, [('break', 5)]),
     (32, [('teachmagic', 2.5), ('ws1', 13), ('ws1ans', 1.5), ('teachpyr', 2), ('teach999', 2), ('ws2', 6.5), ('ws2ans', 1.5), ('stretch', 3)]),
     (8, [('talk', 8)]), (11, [('exit', 6), ('reflect', 3), ('close', 2)])],
 3: [(1.5, [('title', 1.5)]), (9.5, [('warmcheck', 3.5), ('warm1', 3), ('warm2', 3)]), (14.5, [('explore1', 10), ('explore2', 4.5)]),
     (11, [('teach1', 2.5), ('try1', 2.5), ('teach2', 2), ('we2', 1.5), ('try2', 1.5), ('key', 1)]), (5, [('break', 5)]),
     (29, [('ws1', 12.5), ('ws1ans', 1.5), ('teachlist', 2), ('teachgrid', 2), ('teachboth', 1.5), ('ws2', 5), ('ws2ans', 1.5), ('stretch', 3)]),
     (8, [('talk', 8)]), (11.5, [('exit', 6), ('reflect', 3), ('close', 2.5)])],
 4: [(1.5, [('title', 1.5)]), (9.5, [('warmcheck', 3.5), ('warm1', 3), ('warm2', 3)]), (14, [('explore1', 9), ('explore2', 5)]),
     (9.5, [('we1', 2), ('try1', 1), ('we2', 2.5), ('try2', 2), ('key', 2)]), (5, [('break', 5)]),
     (32, [('teachunits', 2), ('ws1', 13), ('ws1ans', 1.5), ('teachtd', 2), ('teachgive', 1.5), ('ws2', 7.5), ('ws2ans', 1.5), ('stretch', 3)]),
     (7.5, [('teachsame', 1.5), ('talk', 6)]), (11, [('exit', 6), ('reflect', 3), ('close', 2)])],
 5: [(1.5, [('title', 1.5)]), (9.5, [('warmcheck', 3.5), ('warm1', 3), ('warm2', 3)]), (14.5, [('explore1', 10), ('explore2', 4.5)]),
     (11, [('teach1', 2), ('we1', 2), ('try1', 1.5), ('we2', 2), ('try2', 1.5), ('key', 2)]), (5, [('break', 5)]),
     (31, [('teachback', 2), ('ws1', 12), ('ws1ans', 1.5), ('teachlist', 2), ('teachbig', 1.5), ('ws2', 7.5), ('ws2ans', 1.5), ('stretch', 3)]),
     (7, [('talk', 7)]), (10.5, [('exit', 5.5), ('reflect', 3), ('close', 2)])],
 6: [(1.5, [('title', 1.5)]), (9.5, [('warmcheck', 3.5), ('warm1', 3), ('warm2', 3)]), (14, [('explore1', 10), ('explore2', 4)]),
     (11, [('teach1', 1.5), ('we1', 2), ('try1', 1.5), ('we2', 2), ('try2', 2.5), ('key', 1.5)]), (5, [('break', 5)]),
     (30, [('ws1', 14.5), ('ws1ans', 1.5), ('teachadd', 2), ('ws2', 7), ('ws2ans', 2), ('stretch', 3)]),
     (8, [('talk', 8)]), (11, [('exit', 6), ('reflect', 3), ('close', 2)])],
 7: [(1.5, [('title', 1.5)]), (9.5, [('warmcheck', 3.5), ('warm1', 3), ('warm2', 3)]), (13.5, [('explore1', 9.5), ('explore2', 4)]),
     (11.5, [('teach1', 2.5), ('try1', 1.5), ('teach2', 2), ('try2', 2), ('teach3', 2), ('key', 1.5)]), (5, [('break', 5)]),
     (31, [('teachsq', 2), ('ws1', 14), ('ws1ans', 2), ('ws2', 8.5), ('ws2ans', 1.5), ('stretch', 3)]),
     (7, [('talk', 7)]), (11, [('exit', 6), ('reflect', 3), ('close', 2)])],
 8: [(1.5, [('title', 1.5)]), (9, [('warmcheck', 3), ('warm1', 3), ('warm2', 3)]), (13.5, [('explore1', 9.5), ('explore2', 4)]),
     (10.5, [('teach1', 2), ('teach2', 2), ('we2', 2), ('try2', 1.5), ('teach3', 2), ('key', 1)]), (5, [('break', 5)]),
     (31, [('we1', 1.5), ('ws1', 15), ('ws1ans', 1.5), ('teachgrid', 1.5), ('ws2', 7), ('ws2ans', 1.5), ('stretch', 3)]),
     (8, [('talk', 8)]), (11.5, [('exit', 6), ('reflect', 3), ('close', 2.5)])],
 9: [(1.5, [('title', 1.5)]), (9, [('warmcheck', 3), ('warm1', 3), ('warm2', 3)]), (15, [('explore1', 10.5), ('explore2', 4.5)]),
     (8.5, [('teach1', 2), ('we1', 2.5), ('try1', 2.5), ('key', 1.5)]), (5, [('break', 5)]),
     (31, [('teachbudget', 1.5), ('ws1', 15.5), ('ws1ans', 1.5), ('teach2', 1.5), ('we2', 1), ('ws2', 5.5), ('ws2ans', 1.5), ('stretch', 3)]),
     (8.5, [('talk', 8.5)]), (11.5, [('exit', 6), ('reflect', 3), ('close', 2.5)])],
 10: [(1.5, [('title', 1.5)]), (9, [('warmcheck', 3), ('warm1', 3), ('warm2', 3)]), (16.5, [('explore1', 12), ('explore2', 4.5)]),
      (9.5, [('teach1', 1.5), ('we1', 1.5), ('try1', 1), ('we2', 1.5), ('try2', 1), ('we3', 1.5), ('key', 1.5)]), (5, [('break', 5)]),
      (29.5, [('ws1', 15.5), ('ws1ans', 1.5), ('teachlist', 1), ('ws2', 7), ('ws2ans', 1.5), ('stretch', 3)]),
      (6, [('talk', 6)]), (13, [('exit', 5), ('reflect', 3), ('end', 5)])],
}
# slides with no slide of their own (the close part has none) are not written to the plan
NOSLIDE = {'close'}

def build():
    gf = json.load(open(os.path.join(P3, 'gifted.json'), encoding='utf8'))
    bud = {'lessons': {}}
    for n, parts in L.items():
        t = 0.0; plan = {}; pj = []
        assert len(parts) == 8, n
        for (b, slides), title in zip(parts, TITLES):
            start = t
            for sid, d in slides:
                if sid not in NOSLIDE:
                    plan[sid] = [t, t + d]
                t += d
            assert abs(t - start - b) < 1e-9, (n, title, t - start, b)
            pj.append({'title': title, 'start': start, 'end': t})
        assert abs(t - 90) < 1e-9, (n, t)
        # the optional pages share the 3-minute choose window
        w = plan['stretch']
        for o in OPT: plan[o] = list(w)
        plan = {k: [int(a) if a == int(a) else a for a in v] for k, v in plan.items()}
        for p in pj:
            for k in ('start', 'end'):
                if p[k] == int(p[k]): p[k] = int(p[k])
        gf[str(n)]['plan'] = plan
        bud['lessons'][str(n)] = {'parts': pj, 'optional_slides': ['p3l%d-%s' % (n, o) for o in OPT]}
    json.dump(gf, open(os.path.join(P3, 'gifted.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    out = ['{', ' "lessons": {']
    for i, (k, v) in enumerate(bud['lessons'].items()):
        out.append('  "%s": {' % k)
        out.append('   "parts": [')
        out.append(',\n'.join('    ' + json.dumps(p) for p in v['parts']))
        out.append('   ],')
        out.append('   "optional_slides": ' + json.dumps(v['optional_slides']))
        out.append('  }' + (',' if i < len(bud['lessons']) - 1 else ''))
    out += [' }', '}']
    open(os.path.join(P3, 'budget.json'), 'w', encoding='utf8').write('\n'.join(out) + '\n')
    print('wrote p3/budget.json and gifted.json plans')

if __name__ == '__main__':
    build()
