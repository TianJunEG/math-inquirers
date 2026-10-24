"""Loads taxonomy.json (the list of maths kinds = families, and sub-structures) for build_bank.py and verify_bank.py."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(HERE, 'taxonomy.json'), encoding='utf-8'))
RULES = T['rules']
FAMILIES = T['families']
SUBS = {}
for sid, s in T['subs'].items():
    fam = sid.split('.')[0]
    assert fam in FAMILIES, 'sub %s has no family' % sid
    SUBS[sid] = dict(s, family=fam, id=sid)
FIXED = T['fixed_fallback']


def quarter(mm):
    """Calendar quarter (1-4) of a month given as 'MM' or int."""
    return (int(mm) - 1) // 3 + 1


def matches(sub, entry):
    """True if a bank entry (kind, parameters) is a legitimate instance of the sub-structure."""
    s = SUBS[sub]
    if entry['kind'] not in s['kinds']:
        return False, 'kind %s is not one of %s' % (entry['kind'], s['kinds'])
    p = entry['p']
    for k, allowed in (s.get('where') or {}).items():
        if k == 'pred':
            names = [x[0] for x in p.get('preds', [])]
            if not any(n in allowed for n in names):
                return False, 'no predicate in %s (has %s)' % (allowed, names)
        elif k == 'has':
            miss = [n for n in allowed if p.get(n) is None]
            if miss:
                return False, 'parameters %s are missing' % miss
        else:
            if p.get(k) not in allowed:
                return False, 'parameter %s=%r not in %s' % (k, p.get(k), allowed)
    return True, ''
