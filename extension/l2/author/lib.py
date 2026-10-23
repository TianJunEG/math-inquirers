"""Authoring helpers for the Level 2 unit JSON files (extension/data/l2_uNN.json).
The unit scripts u01.py ... u10.py in this folder build the JSON with these helpers; run `python3 extension/l2/author/u01.py` to rewrite one file.
Answers printed in the book are written here; the independent recomputation lives in extension/verify/l2_uNN_checks.py (never copied from here)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'data')


def A(value, text=None, unordered=False, lst=False):
    value = [str(v) for v in (value if isinstance(value, (list, tuple)) else [value])]
    a = {'value': value, 'text': text if text is not None else ', '.join(value)}
    if unordered:
        a['unordered'] = True
    if lst:
        a['list'] = True
    return a


def P(label, text, value, atext=None, **kw):
    return {'label': label, 'text': text, 'answer': A(value, atext, **kw)}


def I(tier, page, text, value=None, atext=None, why='', figure=None, parts=None, hint=None, space=None, beyond=None, **kw):
    it = {'tier': tier, 'page': page, 'text': text}
    if figure:
        it['figure'] = figure
    if parts:
        it['parts'] = parts
    else:
        it['answer'] = A(value, atext, **{k: kw.pop(k) for k in ('unordered', 'lst') if k in kw})
    it['explanation'] = why
    if hint:
        it['hint'] = hint
    if space:
        it['space'] = space
    if beyond:
        it['beyond'] = beyond
    it.update(kw)
    return it


def build(n, title, topic, goal, learn, items, **extra):
    pre = f'L2U{n:02d}'
    count = {'start': 0, 'think': 0, 'go': 0, 'quiz': 0}
    code = {'start': 'S', 'think': 'T', 'go': 'G', 'quiz': 'C'}
    out = []
    order = {'start': 0, 'think': 1, 'go': 2, 'quiz': 3}
    items = sorted(items, key=lambda it: (order[it['tier']], it.get('page', 0)))   # numbering and answer order follow the printed page order
    for it in items:
        count[it['tier']] += 1
        d = {'id': f'{pre}-{code[it["tier"]]}{count[it["tier"]]:02d}'}
        d.update(it)
        if it['tier'] == 'quiz':
            d.pop('page', None)
        elif it['tier'] == 'think':
            d['page'] = 4
        elif it['tier'] == 'go':
            d['page'] = 5
        out.append(d)
    learn = dict(learn)
    learn['try'] = dict({'id': f'{pre}-L01'}, **learn['try'])
    unit = {'schema_version': 1, 'level': 2, 'unit': n, 'id': pre, 'title': title, 'topic': topic, 'holiday_lesson': n, 'goal': goal, 'learn': learn, 'items': out}
    unit.update(extra)
    path = os.path.join(DATA, f'l2_u{n:02d}.json')
    json.dump(unit, open(path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print('wrote', path, {k: v for k, v in count.items()})
