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


def write_unit(n, title, topic, goal, learn, items, **extra):
    u = {'schema_version': 1, 'level': 6, 'unit': n, 'id': f'L6U{n:02d}', 'title': title, 'topic': topic, 'holiday_lesson': n, 'goal': m(goal),
         'learn': learn, 'items': items}
    u.update(extra)
    # light checks
    uid = u['id']
    for it in items:
        assert it['id'].startswith(uid + '-')
    s = [i for i in items if i['tier'] == 'start']
    print(uid, 'start', len(s), 'think', sum(i['tier'] == 'think' for i in items), 'go', sum(i['tier'] == 'go' for i in items), 'quiz', sum(i['tier'] == 'quiz' for i in items))
    json.dump(u, open(os.path.join(DATA, f'l6_u{n:02d}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return u
