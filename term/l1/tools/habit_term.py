"""Inquiry-habit additions for the Term-time Level 1 builders (term/l1): guide line + six-habit table, slide badge, online self-check item.
Wording, icons and the 40-lesson assignment come ONLY from levels/habits.json (key term_l1_lessons) and levels/habit_icons/*.svg, the same
shared data as the holiday lessons. The online items are in term/l1/habit_items.json. Nothing here touches the lesson JSON or the printed
workbooks/books (b_print.py is not changed): the owner has not approved habit tags in print."""
import html, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
L1 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(L1))
E = html.escape
DATA = json.load(open(os.path.join(ROOT, 'levels', 'habits.json'), encoding='utf-8'))
ITEMS = json.load(open(os.path.join(L1, 'habit_items.json'), encoding='utf-8'))['items']
ORDER = ['Notice', 'Wonder', 'Try', 'Check', 'Explain', 'Look back']
NAVY = '#1B2A49'
TEAL = '#1F7A6F'
_svg = {}


def icon(i, color=NAVY, px=44, extra=''):
    if i not in _svg:
        _svg[i] = open(os.path.join(ROOT, 'levels', 'habit_icons', i + '.svg'), encoding='utf-8').read().strip().replace('\n', '')
    s = re.sub(r'width="64" height="64"', f'width="{px}" height="{px}"', _svg[i], count=1)
    return s.replace('<svg ', f'<svg style="color:{color};flex:none;display:block;{extra}" ', 1)


def name(d):
    return DATA['term_l1_lessons'][str(int(d['_num']))]


def habit(d):
    n = name(d)
    return n, DATA['habits'][n]


def note(d):
    n, h = habit(d)
    return f'HABIT: {DATA["badge_label"]}: {n}. {h["move"]} Say: "{h["prompt"]}" {DATA["rule"]}'


# ------------------------------------------------------------------ deck
def badge(d, where):
    """Focus-habit pill (same icon and words as the holiday decks). title: top left, above the 'LESSON n' line (Mi and the tool chip are lower down); reflect: top right, left of the minute pill (clear of the heading, the chip row and Mi)."""
    n, h = habit(d)
    pos = 'position:absolute;left:128px;top:64px' if where == 'title' else 'position:absolute;right:380px;top:52px'
    return (f'<div data-habit="badge" style="{pos};height:64px;display:flex;align-items:center;gap:14px;background:#FFFFFF;border:2px solid {TEAL};border-radius:999px;padding:6px 26px 6px 14px;font-size:28px;font-weight:700;color:{NAVY}">'
            f'{icon(h["icon"], NAVY, 44)}<span style="white-space:nowrap">{E(DATA["badge_label"])}: {E(n)}</span></div>')


# ------------------------------------------------------------------ tutor guide
def guide_line(d):
    n, h = habit(d)
    return f'{E(DATA["badge_label"])}: {E(n)} - {E(h["move"])} Say: &ldquo;{E(h["prompt"])}&rdquo; {E(DATA["rule"])}'


def guide_box(d):
    """Front-page box under the cover: this lesson's focus habit with its teaching move and scripted prompt."""
    n, h = habit(d)
    return (f'<div class="box t" data-habit="focus" style="display:flex;gap:12px;align-items:center">{icon(h["icon"], NAVY, 38)}'
            f'<div><b>{guide_line(d)}</b><div class="small">Supporting habit: none required. Also see the six-habit table below.</div></div></div>')


def guide_table(d):
    """Six-habit table for the guide front matter (same in every lesson; today's habit marked)."""
    n0, _ = habit(d)
    rows = ''.join(f'<tr><td style="width:26px">{icon(DATA["habits"][k]["icon"], NAVY, 20)}</td><td><b>{E(k)}</b>{" (today)" if k == n0 else ""}<div class="small">{E(DATA["habits"][k]["phrase"])}</div></td>'
                   f'<td>{E(DATA["habits"][k]["move"])}</td><td><i>&ldquo;{E(DATA["habits"][k]["prompt"])}&rdquo;</i></td></tr>' for k in ORDER)
    return (f'<h3>Focus habit (every lesson): the six inquiry habits</h3><table data-habit="table"><tr><th></th><th>Habit</th><th>Teaching move</th><th>Say</th></tr>{rows}</table>'
            f'<p class="small">{E(DATA["rule"])} Children practise one focus habit in each lesson; each term uses all six. Record, in your own words, one thing you saw a child do.</p>')


# ------------------------------------------------------------------ online practice
def add_item(d, items):
    """Insert the self-check item after the last core item. Returns a new list; existing items are untouched."""
    it = ITEMS[d['_num']]
    assert not any(x['id'] == it['id'] for x in items), 'habit item id clash'
    last = max(i for i, x in enumerate(items) if x['tier'] == 'core')
    return items[:last + 1] + [dict(it)] + items[last + 1:]
