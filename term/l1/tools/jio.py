"""Round-trip lesson JSON files byte for byte (detects indent, ensure_ascii and trailing newline), so edits leave no formatting noise."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(n):
    f = os.path.join(ROOT, 'lessons', f'l{n:02d}.json')
    raw = open(f, encoding='utf-8').read(); d = json.loads(raw)
    for ind in (1, 2):
        for ea in (False, True):
            for nl in ('', '\n'):
                if json.dumps(d, indent=ind, ensure_ascii=ea) + nl == raw:
                    return d, (f, ind, ea, nl)
    raise ValueError('cannot round-trip ' + f)

def save(d, fmt):
    f, ind, ea, nl = fmt
    open(f, 'w', encoding='utf-8').write(json.dumps(d, indent=ind, ensure_ascii=ea) + nl)

def questions(d):
    """Yield (container-name, question dict) for every workbook question, exit ticket and home item."""
    t = d['tiers']
    for k in ('start', 'think', 'go'):
        for q in t[k]: yield k, q
    yield 'inv', t['investigation']
    for q in d['exit']: yield 'exit', q
    for q in d['home_practice']: yield 'home', q

def find(d, qid):
    for k, q in questions(d):
        if q.get('id') == qid: return q
    raise KeyError(qid)
