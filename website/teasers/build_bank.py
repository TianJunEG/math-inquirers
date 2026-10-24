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
import taxonomy as TAX                          # noqa: E402
from defs_common import FMT, UNIT_SYN, LEVEL_AGES, dec_str, show_frac   # noqa: E402



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
    if canon.startswith('-'):
        shown = shown.replace('-', '\u2212')
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


def order(level, items, left=None, right=None):
    """Deterministic interleave: no two neighbours share a family (topic) or a kind; `left` / `right` are the families and kinds of the last puzzle of the
    month before and the first of the month after (when those months already exist), so the rule also holds across a month boundary."""
    rnd = random.Random(1000 + level)
    best = None

    def clash(a, b):
        return a['family'] == b['family'] or a['kind'] == b['kind']
    for _ in range(40000):
        rnd.shuffle(items)
        n = len(items)
        bad = sum(1 for i in range(n - 1) if clash(items[i], items[i + 1]))
        if left and clash(left, items[0]):
            bad += 1
        if right and clash(items[-1], right):
            bad += 1
        if best is None or bad < best[0]:
            best = (bad, list(items))
        if bad == 0:
            break
    if best[0]:
        print('WARNING level %d: %d neighbouring puzzles share a family or kind' % (level, best[0]))
    return best[1]


LEVELS = [int(x) for x in os.environ.get('MI_LEVELS', '1 2 3 4 5 6').split()]   # development: build chosen levels only
DAYS_IN = {'01': 31, '02': 29, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}


def manifest():
    return json.load(open(os.path.join(HERE, 'manifest.json')))


def edge(mm, lv, which):
    """The family/kind of the last puzzle of the previous month (which = -1) or the first of the next month (which = 0), if that month's bank exists."""
    other = '%02d' % ((int(mm) - 2) % 12 + 1 if which == -1 else int(mm) % 12 + 1)
    if which == 0 and mm == '12' and str(lv) in TAX.RULES['min_gap_days'] and os.path.exists(os.path.join(HERE, 'batches', 'm11', 'bank.json')):
        other = '11'      # Levels 1 and 2 repeat the released order every 61 days (see plan_year), so 31 Dec is followed by what was 1 Nov
    p = os.path.join(HERE, 'batches', 'm%s' % other, 'bank.json')
    if not os.path.exists(p):
        return None
    try:
        items = json.load(open(p, encoding='utf-8'))['levels'][str(lv)]
    except Exception:
        return None
    e = items[-1] if which == -1 else items[0]
    return {'family': e['family'], 'kind': e['kind']}


def build_month(mm):
    """Build batches/m<MM>/bank.json: for every level, one puzzle per calendar day of the month."""
    out = {}
    for lv in LEVELS:
        mod = importlib.import_module('defs.m%s.l%d' % (mm, lv))
        items = []
        for d in mod.DEFS:
            ans, ctx = solve(d)
            fin = finish(d, ans)
            r = render(d, ans, ctx, fin)
            assert d['sub'] in TAX.SUBS, 'unknown sub-structure %r in L%d %s' % (d['sub'], lv, d['frame'])
            e = dict(id='L%d-%s' % (lv, d['frame']), level=lv, frame=d['frame'], kind=d['kind'], topic=d['topic'],
                     sub=d['sub'], family=TAX.SUBS[d['sub']]['family'],
                     p=d['p'], t=d['t'], fmt=d['fmt'], type=fin['type'], ans=fin['canon'], shown=fin['shown'],
                     units=fin['units'], prefix=fin['prefix'], accept=fin['accept'], exact=fin['exact'],
                     wrong=wrongs(d, ans, fin), **r)
            items.append(e)
        want = DAYS_IN[mm]
        if len(items) != want:
            print('WARNING month %s level %d has %d puzzles (want %d)' % (mm, lv, len(items), want))
        items = order(lv * 100 + int(mm), items, edge(mm, lv, -1), edge(mm, lv, 0))
        for i, e in enumerate(items):
            e['date'] = '%s-%02d' % (mm, i + 1)
        out[str(lv)] = items
    d = os.path.join(HERE, 'batches', 'm%s' % mm)
    os.makedirs(d, exist_ok=True)
    json.dump({'version': 2, 'month': mm, 'levels': out}, open(os.path.join(d, 'bank.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('month %s: %s' % (mm, {k: len(v) for k, v in out.items()}))


def plan_year():
    """Levels 1 and 2 (gap rule, 60 days): write batches/YEAR_PLAN.md.  With 61 days released (1 Nov to 31 Dec) and 61 distinct sub-structures, the
    only calendar that keeps every sub-structure at least 60 days apart is a rotation: day k of the year (counted from 1 Nov, 366 dates including 29 Feb)
    uses the sub-structure of released day (k mod 61).  366 = 6 x 61, so every sub-structure returns exactly every 61 days in a leap year and every 60 or 61 days
    in an ordinary year.  The plan is checked with verify_bank's own gap and family rules for a 365-day and a 366-day year."""
    import verify_bank as V
    man = manifest()
    if man['released'] != ['11', '12']:
        print('plan_year: written for the released months 11 and 12 only (a rotation needs the 61 released days)')
        return
    months = [('11', 30), ('12', 31)] + [(m, DAYS_IN[m]) for m in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10')]
    dates = ['%s-%02d' % (m, d) for m, n in months for d in range(1, n + 1)]
    assert len(dates) == 366
    lines = ['# Year plan for Levels 1 and 2 (owner L1L2-GAP60)', '',
             'Day k of the year, counted from 1 Nov (366 dates, 29 Feb included), uses the sub-structure of released day k mod 61.  366 = 6 x 61, so a sub-structure '
             'returns exactly 61 days later (60 days in an ordinary year, because 29 Feb is missing).  A new story and new numbers are written for every return; '
             'the answer of a puzzle must not equal any answer within 60 days (checked by verify_bank.py as the months are written).', '']
    bad = []
    for lv in (1, 2):
        released = []
        for mm in man['released']:
            released += json.load(open(os.path.join(HERE, 'batches', 'm%s' % mm, 'bank.json'), encoding='utf-8'))['levels'][str(lv)]
        released.sort(key=lambda e: e['date'][:2] != '11' and 1 or 0)
        released = sorted(released, key=lambda e: (0 if e['date'][:2] == '11' else 1, e['date']))
        assert len(released) == 61
        entries = []
        for k, d in enumerate(dates):
            r = released[k % 61]
            entries.append(('', dict(id='L%d-%s' % (lv, d), date=d, sub=r['sub'], family=r['family'], ans='P%d' % k)))
        fails = []
        V.gap_rules(lv, entries, fails)
        wrap = released[60]['family'] == released[0]['family']
        if wrap:
            fails.append('L%d: 31 Dec and 1 Nov of the next cycle are the same family' % lv)
        lines += ['## Level %d' % lv, '', 'Checked with the gap rules for a 365-day and a 366-day year: %s.' % ('no violation' if not fails else '%d violation(s): %s' % (len(fails), '; '.join(fails[:3]))), '',
                  '| Released day | Date | Sub-structure | Later dates it returns on |', '|---|---|---|---|']
        for i, r in enumerate(released):
            ret = [dates[k] for k in range(i + 61, 366, 61)]
            lines.append('| %d | %s | %s | %s |' % (i + 1, r['date'], r['sub'], ', '.join(ret)))
        lines.append('')
        bad += fails
    open(os.path.join(HERE, 'batches', 'YEAR_PLAN.md'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    print('year plan written: %d violation(s)' % len(bad))
    for b in bad:
        print('  ', b)


def main():
    if '--plan' in sys.argv:
        plan_year()
        return
    months = sys.argv[1:] or manifest()['released']
    for mm in months:
        build_month(mm)


if __name__ == '__main__':
    main()
