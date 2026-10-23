"""Authoring helpers for the Level 4 units (the unit sources in this folder write extension/data/l4_uNN.json)."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'data')


def A(*vals, text=None, **kw):
    """Answer: values (strings or numbers), printed text (default: values joined with ', ')."""
    v = [str(x) for x in vals]
    d = {'value': v, 'text': text if text is not None else ', '.join(v)}
    d.update(kw)
    return d


def P(label, text, ans):
    return {'label': label, 'text': text, 'answer': ans}


def item(id_, tier, page, text, ans=None, parts=None, why='', fig=None, hint=None, space=None, **kw):
    d = {'id': id_, 'tier': tier}
    if tier != 'quiz':
        d['page'] = page
    d['text'] = text
    if fig:
        d['figure'] = fig
    if parts:
        d['parts'] = parts
    else:
        d['answer'] = ans
    if space:
        d['space'] = space
    if hint:
        d['hint'] = hint
    d['explanation'] = why
    d.update(kw)
    return d


def write(n, unit):
    import re
    last = {}
    for it in unit['items']:
        t = it['id'].split('-')[-1]
        k = t[0]
        nn = int(t[1:])
        assert nn == last.get(k, 0) + 1, f'id order: {it["id"]}'
        last[k] = nn
    pg = {}
    for it in unit['items']:
        if it.get('page'):
            assert it['page'] >= pg.get(it['tier'], 0), f'page order: {it["id"]}'
            pg[it['tier']] = it['page']
    path = os.path.join(DATA, f'l4_u{n:02d}.json')
    # ids for items are written as L4U<nn>-<tier letter><nn> by the caller
    json.dump(unit, open(path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print('wrote', path, len([i for i in unit['items']]), 'items')
