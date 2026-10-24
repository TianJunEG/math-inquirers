"""Inline SVG for the six inquiry-habit icons (levels/habit_icons/<id>.svg) and the levels/habits.json loader.
    import habit_icons as hi;  hi.icon('notice', '#1B2A49', 50);  hi.habit(2, 4) -> ('Notice', {...})
Same icon and same wording every time a habit appears (slide badge, guide line, online item)."""
import os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = json.load(open(os.path.join(HERE, 'habits.json'), encoding='utf-8'))
def icon(i, color='#1B2A49', px=64, extra=''):
    s = open(os.path.join(HERE, 'habit_icons', i + '.svg'), encoding='utf-8').read().strip().replace('\n', '')
    s = re.sub(r'width="64" height="64"', f'width="{px}" height="{px}"', s, count=1)
    return s.replace('<svg ', f'<svg style="color:{color};flex:none;display:block;{extra}" ', 1)
def habit(level, n):
    name = DATA['lessons'][f'{level}.{n}']; return name, DATA['habits'][name]
