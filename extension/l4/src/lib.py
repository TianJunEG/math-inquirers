"""Authoring helpers for the Level 4 units (the unit sources in this folder write extension/data/l4_uNN.json)."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'data')


def nf(x):
    """Format a whole number for printing: 5 digits or more get a non-breaking space between the thousands."""
    s = str(x)
    if s.lstrip('-').isdigit() and len(s) >= 5:
        return f'{int(s):,}'.replace(',', '\u00a0')
    return s


def A(*vals, text=None, **kw):
    """Answer: values (strings or numbers), printed text (default: values joined with ', ')."""
    v = [str(x) for x in vals]
    d = {'value': v, 'text': text if text is not None else ', '.join(nf(x) for x in v)}
    d.update(kw)
    return d


def P(label, text, ans):
    if '{ll}' in text:
        ans = dict(ans, list=True)
    return {'label': label, 'text': text, 'answer': ans}


def item(id_, tier, page, text, ans=None, parts=None, why='', fig=None, hint=None, space=None, **kw):
    if ans is not None and '{ll}' in text:
        ans = dict(ans, list=True)
    d = {'id': id_, 'tier': tier}
    if text.startswith('Beyond Level 4: '):          # printed by the renderer as a label above the question
        first, _, text = text.partition('\n')
        d['beyond'] = first[len('Beyond Level 4: '):]
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


import re
_NB = re.compile(r'(?<![\d])(\d{2,3}) (\d{3})(?!\d)')


def _fmt(o, key=None):
    if isinstance(o, str):
        if key in ('value', 'id'):
            return o
        return _NB.sub('\\1\u00a0\\2', o)
    if isinstance(o, list):
        return [_fmt(x, key) for x in o]
    if isinstance(o, dict):
        return {k: _fmt(v, k) for k, v in o.items()}
    return o


def write(n, unit):
    unit = _fmt(unit)

    def widen(holder, ans):
        """Blanks whose answer has 5 or more characters get the wide answer box {bw}."""
        if not ans or ans.get('list'):
            return
        vals = ans['value']
        n = holder['text'].count('{b}')
        if n != len(vals) or n == 0:
            return
        out, k = [], 0
        for piece in holder['text'].split('{b}')[:-1]:
            out.append(piece + ('{bw}' if len(str(vals[k])) >= 5 else '{b}'))
            k += 1
        holder['text'] = ''.join(out) + holder['text'].split('{b}')[-1]
        left = ''.join(out).count('{b}') + holder['text'].split('{b}')[-1].count('{b}')
        if 0 < left < n:      # the shared answer runner counts only {b}: mark the mixed answer as a list
            ans['list'] = True
    for it in [unit['learn']['try']] + unit['items']:
        if it.get('parts'):
            for p in it['parts']:
                widen(p, p['answer'])
        else:
            widen(it, it.get('answer'))
    for k in ('example', 'example2', 'facts'):       # Learn it figures sit in a column about 73 mm wide: keep their text at 10 pt or more
        f = unit['learn'].get(k, {}).get('figure')
        if f and f.get('width_mm', 0) > 70:
            f['width_mm'] = 70
    tr = unit['learn']['try']
    if '{ll}' in tr['text']:
        tr['answer'] = dict(tr['answer'], list=True)
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
