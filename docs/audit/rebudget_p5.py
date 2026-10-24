#!/usr/bin/env python3
"""Re-run of the P5 timing model (docs/audit/timing_p5.py) on the RE-BUDGETED decks and sources.   ANALYSIS ONLY: reads, writes nothing.

    python3 docs/audit/rebudget_p5.py

For every lesson: the model's need for each part (fix scenario of timing_p5.FIX: four quick questions, one game round, explore pair work capped,
two regroup questions, two items per Your-turn slide, only the in-class worksheet items, only the kept teaching slides, typed stamp) next to the new
budget from p5/budget.json.  Estimated clock total = sum of the parts' needs, the two worksheet blocks counted at their budget (they are time-boxes);
slack = 90 - total (what the Buffer has to cover)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import timing_p5 as T
ROOT = T.ROOT
BUD = json.load(open(os.path.join(ROOT, 'p5', 'budget.json')))['lessons']
D = T.load_data()
KEYS = [('open', 'Opening'), ('sneak', 'Sneak'), ('warm', 'Warm-up'), ('explore', 'Explore'), ('mini', 'Mini-lesson'), ('brk', 'Brain break'),
        ('p1', 'Worksheet page 1'), ('chk1', 'Check page 1'), ('teach', 'Short teaching'), ('p2', 'Worksheet page 2'), ('chk2', 'Check page 2'), ('talk', 'Talk time'), ('exit', 'Exit'), ('buffer', 'Buffer')]
def run():
    res = {}
    for n in range(1, 11):
        pl = T.plan(n, D); S = T.load_slides(n)
        R = T.model(n, D, S, pl['fx']); wb = R['wb']
        need = dict(open=T.tot(R['open']), sneak=T.tot(R['sneak']), warm=T.tot(R['warm']), explore=T.tot(R['explore']), mini=T.tot(R['mini']), brk=T.tot(R['brk']),
                    p1=T.tot(wb['p1']), chk1=T.tot(wb['chk1']), teach=T.tot(wb['teach']), p2=T.tot(wb['p2']), chk2=T.tot(wb['chk2']), talk=T.tot(R['talk']), exit=T.tot(R['exit']))
        need = {k: v / 60 for k, v in need.items()}
        parts = {p['title']: p['end'] - p['start'] for p in BUD[str(n)]['parts']}
        bud = {}
        for k, t in KEYS:
            bud[k] = next((v for title, v in parts.items() if title.startswith(t)), 0.0)
        res[n] = dict(need=need, bud=bud, plan_budget=pl['budgets'], p1_work=pl['p1_work'], p2_work=pl['p2_work'], slides=len(S))
    return res
if __name__ == '__main__':
    res = run()
    print('| Lesson | Slides | Sum of needs, worksheet blocks at their budget | Budget sum | Slack for the buffer | Buffer held | Parts over budget by 0.75 min or more |'); print('|---|---|---|---|---|---|---|')
    for n, r in res.items():
        need, bud = r['need'], r['bud']
        tot = sum(bud[k] if k in ('p1', 'p2') else need[k] for k, _ in KEYS if k != 'buffer')
        over = ['%s +%.1f' % (t, need[k] - bud[k]) for k, t in KEYS if k not in ('buffer', 'p1', 'p2') and need[k] - bud[k] >= 0.75]
        print('| %d | %d | %.1f | %.1f | %+.1f | %.1f | %s |' % (n, r['slides'], tot, sum(bud.values()), 90 - tot, bud['buffer'], '; '.join(over) or '-'))
    print(); 
    for n, r in res.items():
        print('Lesson %d  need/budget:' % n, ' | '.join('%s %.1f/%.1f' % (t, r['need'].get(k, 0), r['bud'][k]) for k, t in KEYS if k != 'buffer'))
