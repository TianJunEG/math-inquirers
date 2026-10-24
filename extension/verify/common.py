"""Shared helpers for the per-item answer checks."""
import json, os, re, itertools
EXT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(EXT)


def load_unit(level, unit):
    return json.load(open(os.path.join(EXT, 'data', f'l{level}_u{unit:02d}.json'), encoding='utf-8'))


def arith(start, step, n):
    """First n terms of the pattern start, start+step, ... (written out term by term, no formula for the nth term)."""
    out, v = [], start
    for _ in range(n):
        out.append(v)
        v += step
    return out


def s(xs):
    return [str(x) for x in xs]


def norm(v):
    """Normalise an answer value (list of strings or scalars) for comparison."""
    if not isinstance(v, (list, tuple)):
        v = [v]
    return [re.sub(r'\s+', ' ', str(x).strip().lower().replace('¢', '')) for x in v]
