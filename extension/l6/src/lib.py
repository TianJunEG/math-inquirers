"""Authoring helpers for the Level 6 extension workbook (units are written as Python and dumped to extension/data/l6_uNN.json)."""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'data')
MINUS = '−'


def m(s):
    """Typeset a minus sign between spaces / before digits with the real minus sign: ' - ' -> ' − ', '(-3' -> '(−3'."""
    s = re.sub(r'(?<=\s)-(?=\s|\d)', MINUS, s)
    s = re.sub(r'(?<=\()-(?=\d)', MINUS, s)
    return s


def A(vals, text=None, **kw):
    vals = [str(v) for v in (vals if isinstance(vals, (list, tuple)) else [vals])]
    d = {'value': vals, 'text': m(text) if text is not None else ', '.join(vals)}
    d.update(kw)
    return d


def P(label, text, vals, ans_text=None, **kw):
    return {'label': label, 'text': m(text), 'answer': A(vals, ans_text, **kw)}


def IT(uid, kind, n, page, text, why, answer=None, parts=None, fig=None, hint=None, space=None, **kw):
    tier = {'S': 'start', 'T': 'think', 'G': 'go', 'C': 'quiz', 'L': 'start'}[kind]
    if kw.get('beyond'):
        text = 'Beyond Level 6: ' + kw.pop('beyond') + '.\n' + text   # the shared renderer prints 'Beyond Level 1' for the beyond key, so the label is part of the text (see extension/l6/TOOL_REQUESTS.md)
    it = {'id': f'{uid}-{kind}{n:02d}', 'tier': tier, 'text': m(text)}
    if kind != 'L':
        it['page'] = page
    if parts:
        it['parts'] = parts
    if answer:
        it['answer'] = answer
    if fig:
        it['figure'] = fig
    if hint:
        assert len(hint) <= 68, (it['id'], len(hint), hint)
        it['hint'] = hint
    if space:
        it['space'] = space
    it['explanation'] = m(why)
    it.update(kw)
    return it


def grid(rows, cw, head=None, rowhead=False, ch=9, **kw):
    d = {'type': 'l6_grid', 'rows': rows, 'cw': cw, 'rowhead': rowhead, 'ch': ch}
    if head:
        d['head'] = head
    d.update(kw)
    return d


def code(prog, **kw):
    d = {'type': 'l6_code', 'prog': prog}
    d.update(kw)
    return d


HAT = ['hat', 'when green flag clicked']


def finalize(u, lo=0.87, hi=0.985):
    """Measure the items, put the Start here items on pages 1-3 (best fit, keeping the written order where possible), renumber the ids by page order,
    and print the fill of every page.  Returns the unit."""
    import sys
    tools = os.path.join(os.path.dirname(HERE), 'tools')
    sys.path.insert(0, tools)
    import measure
    cap, hs, bn = measure.measure(u)
    start = [i for i in u['items'] if i['tier'] == 'start']
    segs, fills, how = measure.suggest(start, hs, bn['start'], cap, lo, hi)
    if not segs:
        tot = sum(hs[i['id']] + measure.GAP for i in start) + 3 * bn['start']
        print(f'  !! Start here does not fit 3 pages: total {tot:.0f} mm, wanted {lo * 3 * cap:.0f}..{hi * 3 * cap:.0f} mm')
        segs, fills, how = measure.suggest(start, hs, bn['start'], cap, 0.5, 1.0)
        if not segs:
            return u
    order = {iid: k for k, s_ in enumerate(segs) for iid in s_}
    pos = {i['id']: n for n, i in enumerate(u['items'])}
    for it in start:
        it['page'] = order[it['id']] + 1
    print('  Start here pages (' + how + '): ' + '   '.join(f'p{k + 1} {f:.3f}' for k, f in enumerate(fills)))
    for tier, label in (('think', 'Think harder'), ('go', 'Go further')):
        ids = [i['id'] for i in u['items'] if i['tier'] == tier]
        f = measure.page_fill(ids, hs, bn[tier], cap)
        print(f'  {label} fill {f:.3f}' + ('   <-- out of range' if not (lo <= f <= hi) else ''))
    q = [i['id'] for i in u['items'] if i['tier'] == 'quiz']
    tot = (sum(hs[i] + measure.GAP for i in q) + bn['quiz'] + measure.QUIZ_FURN) / cap
    print(f'  Check yourself fill {tot:.3f}' + ('   <-- out of range' if not (lo <= tot <= hi) else ''))
    # the ids stay as authored (they are internal: the printed numbers are the positions on the page); the list is ordered as it is printed
    u['items'].sort(key=lambda i: ({'start': 0, 'think': 1, 'go': 2, 'quiz': 3}[i['tier']], i.get('page', 0), pos[i['id']]))
    return u


def write_unit(n, title, topic, goal, learn, items, **extra):
    u = {'schema_version': 1, 'level': 6, 'unit': n, 'id': f'L6U{n:02d}', 'title': title, 'topic': topic, 'holiday_lesson': n, 'goal': m(goal),
         'learn': learn, 'items': items}
    u.update(extra)
    uid = u['id']
    for it in items:
        assert it['id'].startswith(uid + '-')
    print(uid, 'start', sum(i['tier'] == 'start' for i in items), 'think', sum(i['tier'] == 'think' for i in items), 'go', sum(i['tier'] == 'go' for i in items), 'quiz', sum(i['tier'] == 'quiz' for i in items))
    finalize(u)
    json.dump(u, open(os.path.join(DATA, f'l6_u{n:02d}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return u
