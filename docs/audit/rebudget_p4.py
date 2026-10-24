#!/usr/bin/env python3
"""Re-run of the P4 timing model on the re-budgeted decks (docs/audit/rebudget_p4.md).

    python3 docs/audit/rebudget_p4.py

Uses docs/audit/timing_p4.py unchanged (the audit's constants and the per-lesson fix switches FIX_OVER), reads the
rebuilt decks in split/p4l*/project, and compares the model's need for each part with the budget now in p4/budget.json.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import timing_p4 as T

ROOT = T.ROOT
BUD = json.load(open(ROOT + '/p4/budget.json'))['lessons']
NAMES = ['Opening', 'Sneak-peek', 'Warm-up', 'Explore', 'Mini-lesson', 'Brain break', 'WS-a', 'WS-b', 'WS-c', 'WS-d', 'WS-e', 'Talk', 'Exit', 'Looking back', 'Certificates']

def budgets(n):
    b = BUD[str(n)]; p = {x['title']: x['end'] - x['start'] for x in b['parts']}; w = [x['end'] - x['start'] for x in b['worksheet_blocks']]
    out = [p['Opening'], p['Sneak-peek puzzles'], p['Warm-up'], p['Explore (in pairs)'], p['Mini-lesson'], p['Brain break']] + w + [p['Talk time'], p['Exit ticket'], p['Looking back']]
    if 'Certificates and goodbye' in p: out.append(p['Certificates and goodbye'])
    return out

def main():
    data = T.load(); res = {}
    for x in data:
        n = x['lesson']['n']; sl = T.parse_slides(n)
        r = {}
        for sc in ('BEST', 'TYPICAL', 'SLOW'):
            rows, info = T.lesson_model(x, sl, sc, fix=True, over=T.FIX_OVER.get(n))
            r[sc] = rows
        bud = budgets(n); assert abs(sum(bud) - 90) < 1e-9, (n, sum(bud))
        res[n] = (r, bud)
    if '--json' in sys.argv:
        print(json.dumps({n: dict(best=sum(z['need'] for z in r['BEST']), typ=sum(z['need'] for z in r['TYPICAL']), slow=sum(z['need'] for z in r['SLOW'])) for n, (r, b) in res.items()}, indent=1)); return
    print('| L | Slides | Budget | Need best | Need typical | Need slow | Cushion (typical) |\n|--:|--:|--:|--:|--:|--:|--:|')
    for n, (r, bud) in sorted(res.items()):
        tot = {k: sum(z['need'] for z in r[k]) for k in r}
        print('| %d | %d | 90.0 | %.1f | %.1f | %.1f | %.1f |' % (n, len(T.parse_slides(n)), tot['BEST'], tot['TYPICAL'], tot['SLOW'], 90 - tot['TYPICAL']))
    for n, (r, bud) in sorted(res.items()):
        print('\n#### Lesson %d\n\n| Part | Budget | Need best / typical / slow |\n|---|--:|--:|' % n)
        for i, z in enumerate(r['TYPICAL']):
            print('| %s | %.1f | %.1f / %.1f / %.1f |' % (z['part'], bud[i], r['BEST'][i]['need'], z['need'], r['SLOW'][i]['need']))

if __name__ == '__main__':
    main()
