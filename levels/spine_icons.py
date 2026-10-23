"""Inline SVG strings for the eight strategy icons (levels/spine_icons/<id>.svg) and the spine.json data loader.
    import spine_icons as si;  si.icon('draw', '#1B2A49', 120)   ->  '<svg ... width="120" height="120" style="color:#1B2A49">...</svg>'
Icons are stroke-only (3 units, round caps), 64x64 viewBox, stroke colour = CSS colour (currentColor)."""
import os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
IDS = ['pattern', 'list', 'draw', 'table', 'backwards', 'guess', 'simpler', 'actout']
DARK, LIGHT = '#1B2A49', '#FFF9EC'     # workbook ink, ink on navy slides
SPINE = json.load(open(os.path.join(HERE, 'spine.json'), encoding='utf-8'))
_cache = {}
def raw(i):
    if i not in _cache: _cache[i] = open(os.path.join(HERE, 'spine_icons', i + '.svg'), encoding='utf-8').read().strip()
    return _cache[i]
def icon(i, color=DARK, px=64, extra=''):
    s = raw(i)
    s = re.sub(r'width="64" height="64"', f'width="{px}" height="{px}"', s, count=1)
    return s.replace('<svg ', f'<svg style="color:{color};flex:none;display:block;{extra}" ', 1)
def tool(i): return next(t for t in SPINE['tools'] if t['id'] == i)
def band(level): return SPINE['bands'][str(level)]
def lesson(level, n): return SPINE['lessons'][f'{level}.{n}']
