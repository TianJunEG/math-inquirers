"""Shared helpers for the Level 6 independent checks: a tiny interpreter for our code-block specs (so a check can run the very program that is printed in
the book), plus small brute-force tools.  The interpreter never reads an answer from the book."""
import re, itertools, math, random

MINUS = '−'


def _py(expr):
    e = expr.replace('×', '*').replace('÷', '/').replace(MINUS, '-').replace('{gt}', '>').replace('{lt}', '<')
    e = re.sub(r'\bmod\b', '%', e)
    e = re.sub(r'(?<![<>=!])=(?!=)', '==', e)
    e = e.replace('{ge}', '>=').replace('{le}', '<=').replace(' and ', ' and ').replace(' or ', ' or ')
    return e


def ev(expr, env):
    v = eval(_py(expr), {'__builtins__': {}}, dict(env, abs=abs, max=max, min=min, round=round, len=len, sum=sum, int=int))
    if isinstance(v, float) and v == int(v):
        v = int(v)
    return v


def cond(text, env):
    t = text.strip()
    assert t[0] == '<' and t[-1] == '>', t
    return bool(ev(t[1:-1], env))


class Stop(Exception):
    pass


def run(prog, env=None, said=None, trace=None, maxsteps=200000, hooks=None):
    """Execute a block list.  env: dict of variables.  said: list that receives everything said (values).  trace: list of env snapshots, one at the end
    of every pass of every `repeat` body (the outermost loop only if trace_all is not used).  hooks: dict kind-> fn(text, env) for extra blocks."""
    env = dict(env or {})
    said = [] if said is None else said
    steps = [0]

    def blk(items, depth):
        for it in items:
            steps[0] += 1
            if steps[0] > maxsteps:
                raise Stop('too many steps')
            k, t = it[0], it[1]
            kids = it[2] if len(it) > 2 else None
            if k == 'hat':
                continue
            mm = re.match(r'set (\w+) to \((.*)\)$', t)
            if mm:
                env[mm.group(1)] = ev(mm.group(2), env); continue
            mm = re.match(r'change (\w+) by \((.*)\)$', t)
            if mm:
                env[mm.group(1)] = env[mm.group(1)] + ev(mm.group(2), env); continue
            mm = re.match(r'say \((.*?)\)( for \(.*\) seconds)?$', t)
            if mm and kids is None:
                said.append(ev(mm.group(1), env)); continue
            mm = re.match(r'repeat until (<.*>)$', t)
            if mm:
                while not cond(mm.group(1), env):
                    blk(kids, depth + 1)
                    if trace is not None and depth == 0:
                        trace.append(dict(env))
                continue
            mm = re.match(r'repeat \((.*)\)$', t)
            if mm:
                for _ in range(ev(mm.group(1), env)):
                    blk(kids, depth + 1)
                    if trace is not None and depth == 0:
                        trace.append(dict(env))
                continue
            mm = re.match(r'if (<.*>) then$', t)
            if mm:
                if cond(mm.group(1), env):
                    blk(kids, depth + 1)
                elif len(it) > 3:
                    blk(it[3], depth + 1)
                continue
            if hooks:
                for kk, fn in hooks.items():
                    if re.match(kk, t):
                        fn(t, env, kids); break
                else:
                    raise ValueError('cannot run block: ' + t)
                continue
            raise ValueError('cannot run block: ' + t)
    blk(prog, 0)
    return env, said


def s(xs):
    return [str(x) for x in xs]


def rule_str(a, b, var='n'):
    """canonical text of a n + b: '6n + 2', '5n - 2', '4n'."""
    if b > 0:
        return f'{a}{var} + {b}'
    if b < 0:
        return f'{a}{var} - {-b}'
    return f'{a}{var}'


def fit_rule(pairs):
    """pairs: [(n, term), ...] of a sequence with a constant difference -> (a, b) with term = a n + b, found by trying every a, b in a range (no formula)."""
    for a in range(-60, 61):
        for b in range(-300, 301):
            if all(a * n + b == t for n, t in pairs):
                return a, b
    raise ValueError('no linear rule')
