#!/usr/bin/env python3
"""Build website/teasers/bank.json from defs_l1.py ... defs_l6.py.

    python3 website/teasers/build_bank.py

Every puzzle is solved by kinds.py (the author's solver).  verify_bank.py then re-solves each one
with the separate brute-force code in brute.py.  Nothing here touches website/dist.
"""
import importlib
import json
import os
import random
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kinds                                   # noqa: E402
from defs_common import FMT, UNIT_SYN, LEVEL_AGES, dec_str, show_frac   # noqa: E402

BANK = os.path.join(HERE, 'bank.json')


def solve(d):
    ans, ctx = kinds.SOLVE[d['kind']](**d['p'])
    ctx = dict(ctx)
    t = d['t']
    if d['kind'] == 'moves':
        ctx['route'] = kinds.route_text(d['p']['mv'], t['up'], t['down'])
    if d['kind'] == 'expr_form':
        ctx['expr'] = kinds.EXPR_TEXT[d['p']['form']].format(**d['p'])
    if d['kind'] == 'cryptarithm':
        ctx['sum'] = d['p']['pattern'].replace('+', ' + ').replace('=', ' = ').replace('*', ' × ')
    return ans, ctx


def finish(d, ans):
    """canonical answer string, display string, accepted unit words / prefixes, type."""
    fmt, unit = d['fmt'], d['unit']
    out = dict(type='n', units=[], prefix=[], accept=[], exact=False)
    if isinstance(ans, str):
        out.update(type='s', canon=ans.lower(), shown=ans, accept=[a.lower() for a in (d['accept'] or [])])
        return out
    ans = Fr(ans)
    if fmt in ('int', 'plain'):
        assert ans == int(ans), (d['frame'], ans)
        canon, shown = str(int(ans)), ('{:,}'.format(int(ans)) if abs(ans) >= 10000 and fmt == 'int' else str(int(ans)))
    elif fmt == 'dec':
        canon = shown = dec_str(ans)
        if abs(ans) >= 10000:
            shown = '{:,}'.format(ans.numerator // ans.denominator) + (dec_str(ans - ans.numerator // ans.denominator)[1:] if ans.denominator != 1 else '')
    elif fmt == 'money':
        canon = dec_str(ans)
        shown = '$%d' % ans if ans == int(ans) else '$%.2f' % float(ans)
        assert Fr('%.2f' % float(ans)) == ans
        out['prefix'] = ['$', 's$']
        out['units'] = ['dollars', 'dollar']
        unit = None
    elif fmt in ('frac', 'mixed'):
        canon = str(ans.numerator) if ans.denominator == 1 else '%d/%d' % (ans.numerator, ans.denominator)
        shown = show_frac(ans, mixed=(fmt == 'mixed'))
        out['exact'] = True
    else:
        raise ValueError(fmt)
    out['canon'] = canon
    out['num'] = shown
    if unit:
        glue = '' if unit in ('%', '°') else ' '
        shown = shown + glue + unit
        out['units'] = list(d['units'] or UNIT_SYN.get(unit, [unit, unit.rstrip('s')]))
    elif d['units']:
        out['units'] = list(d['units'])
    if d['prefix']:
        out['prefix'] = list(d['prefix'])
    out['shown'] = shown
    return out


def wrongs(d, ans, fin):
    if fin['type'] == 's':
        return list(d['w'])
    a = Fr(ans)
    cand = [a + 1, a - 1, a + 2, a - 2, a * 2, a / 2, a + 10, a - 10, a + Fr(1, 2), a * 10]
    cand += [Fr(str(x)) for x in d['w']]
    out = []
    for c in cand:
        if c != a and c >= 0 and c not in out and (c == int(c) or d['fmt'] != 'int'):
            out.append(c)
    return [dec_str(c) if d['fmt'] != 'frac' and d['fmt'] != 'mixed' else show_frac(c, False) for c in out
            if d['fmt'] in ('int', 'dec', 'money') or c.denominator <= 64]


def render(d, ans, ctx, fin):
    ns = {}
    ns.update(d['t'])
    ns['t'] = d['t']
    ns.update(d['p'])
    ns.update(ctx)
    ns['ans'] = fin['shown']
    ns['ansn'] = fin.get('num', fin['shown'])
    ns['ansv'] = int(fin['canon']) if fin['type'] == 'n' and fin['canon'].lstrip('-').isdigit() else fin['canon']
    r = {}
    for k in ('q', 'hint', 'why', 'big'):
        if d[k] is not None:
            r[k] = FMT.vformat(d[k], (), ns)
    code = d['code'] or ctx.get('code')
    if code:
        r['code'] = code if not d['code'] else FMT.vformat(d['code'], (), ns)
    return r


def order(level, items):
    """Deterministic interleave: no two neighbours (cyclically) share a topic or a kind."""
    rnd = random.Random(1000 + level)
    best = None
    for _ in range(20000):
        rnd.shuffle(items)
        n = len(items)
        bad = sum(1 for i in range(n) if items[i]['topic'] == items[(i + 1) % n]['topic'] or items[i]['kind'] == items[(i + 1) % n]['kind'])
        if best is None or bad < best[0]:
            best = (bad, list(items))
        if bad == 0:
            break
    return best[1]


DAYS_IN = {'01': 31, '02': 29, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}


def manifest():
    return json.load(open(os.path.join(HERE, 'manifest.json')))


def build_month(mm):
    """Build batches/m<MM>/bank.json: for every level, one puzzle per calendar day of the month."""
    out = {}
    for lv in range(1, 7):
        mod = importlib.import_module('defs.m%s.l%d' % (mm, lv))
        items = []
        for d in mod.DEFS:
            ans, ctx = solve(d)
            fin = finish(d, ans)
            r = render(d, ans, ctx, fin)
            e = dict(id='L%d-%s' % (lv, d['frame']), level=lv, frame=d['frame'], kind=d['kind'], topic=d['topic'],
                     p=d['p'], t=d['t'], fmt=d['fmt'], type=fin['type'], ans=fin['canon'], shown=fin['shown'],
                     units=fin['units'], prefix=fin['prefix'], accept=fin['accept'], exact=fin['exact'],
                     wrong=wrongs(d, ans, fin), **r)
            items.append(e)
        want = DAYS_IN[mm]
        if len(items) != want:
            print('WARNING month %s level %d has %d puzzles (want %d)' % (mm, lv, len(items), want))
        items = order(lv * 100 + int(mm), items)
        for i, e in enumerate(items):
            e['date'] = '%s-%02d' % (mm, i + 1)
        out[str(lv)] = items
    d = os.path.join(HERE, 'batches', 'm%s' % mm)
    os.makedirs(d, exist_ok=True)
    json.dump({'version': 2, 'month': mm, 'levels': out}, open(os.path.join(d, 'bank.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('month %s: %s' % (mm, {k: len(v) for k, v in out.items()}))


def main():
    months = sys.argv[1:] or manifest()['released']
    for mm in months:
        build_month(mm)


if __name__ == '__main__':
    main()
