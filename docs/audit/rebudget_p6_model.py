"""Re-run of the P6 timing model (docs/audit/timing_p6.py) on the RE-BUDGETED decks.
Slides that the re-budget removed are no longer in the decks, so the fixes that only counted their removal
(go_drop, exp_slide_merge, mini_drop, mini_merge, ws_merge) are not applied a second time; everything else in FX
(lean sneak, 3 quick questions, shorter explore tasks, take-home questions, 35 s check-together, held-up exit slips) is.
Usage: python3 docs/audit/rebudget_p6_model.py [--md]"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'rebuild'))
import timing_p6 as T
import p6_budget as B
C = T.load_content()
DROP = ('exp_slide_merge', 'mini_drop', 'mini_merge', 'ws_merge')
res = {}
for n in range(1, 11):
    fx = {k: v for k, v in T.FX[n].items() if k not in DROP}
    out = {}
    for name in ('fast', 'central', 'slow'):
        P, info = T.model_lesson(n, C, T.SCEN[name], fx)
        out[name] = sum(p.need for p in P)
        if name == 'central': parts = [(p.name, p.need) for p in P]
    bud = [(t, e - s) for t, s, e in B.BUD[n]['parts']]
    flex = [d for t, d in bud if t.startswith('Flex')][0]
    res[n] = (out, parts, bud, flex)
    print('L%d  fast %.1f  central %.1f  slow %.1f   flex in plan %.1f   spare at central %.1f' % (n, out['fast'], out['central'], out['slow'], flex, 90 - out['central']))
if '--md' in sys.argv:
    for n, (out, parts, bud, flex) in res.items():
        print('\nL%d' % n)
        for (nm, need) in parts: print('  %-40s need %.1f' % (nm, need))
