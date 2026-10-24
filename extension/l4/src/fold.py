"""Cube-net folding by rolling a cube over the net (used by the Unit 8 sources and checks)."""

OPP = {'T': 'B', 'B': 'T', 'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}


def roll(state, d):
    t, b, n, s, e, w = (state[k] for k in 'TBNSEW')
    if d == 'E':
        return dict(T=w, B=e, N=n, S=s, E=t, W=b)
    if d == 'W':
        return dict(T=e, B=w, N=n, S=s, E=b, W=t)
    if d == 'N':
        return dict(T=s, B=n, N=t, S=b, E=e, W=w)
    if d == 'S':
        return dict(T=n, B=s, N=b, S=t, E=e, W=w)


def fold(cells):
    """cells: list of (col,row), row grows downward (south). Returns {cell: face} or None when the net does not fold into a cube."""
    cells = [tuple(c) for c in cells]
    if len(cells) != 6:
        return None
    start = cells[0]
    state = dict(T='T', B='B', N='N', S='S', E='E', W='W')
    seen = {start: state['B']}
    stack = [(start, state)]
    while stack:
        (x, y), st = stack.pop()
        for d, (dx, dy) in (('E', (1, 0)), ('W', (-1, 0)), ('N', (0, -1)), ('S', (0, 1))):
            nb = (x + dx, y + dy)
            if nb in cells and nb not in seen:
                ns = roll(st, d)
                seen[nb] = ns['B']
                stack.append((nb, ns))
    if len(seen) != 6 or len(set(seen.values())) != 6:
        return None
    return seen
