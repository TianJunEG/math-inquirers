"""Shared loading, timing model and text helpers for the Term-time Level 1 builders."""
import html, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
L1 = os.path.dirname(HERE)                      # term/l1
ROOT = os.path.dirname(os.path.dirname(L1))     # repo root
OUT = os.path.join(L1, 'out')
E = html.escape

NAVY = '#1B2A49'; TEAL = '#1F7A6F'; YEL = '#FFC93C'; CREAM = '#FFF9EC'; MUTED = '#3B4A6B'
FOOT_PARENT = 'Math Inquirers  •  Notice it. Test it. Explain why.'   # legacy; use foot_text(d)


STUCK_TEXT = 'I am still stuck (I will ask in the class chat or show my tutor on camera)'


def foot_text(d):
    return f"Math Inquirers Term {d['term']}  \u2022  Notice it. Test it. Explain why."

# ---------------------------------------------------------------- loading

def load(num):
    num = str(num).zfill(2)
    path = os.path.join(L1, 'lessons', f'l{num}.json')
    with open(path, encoding='utf-8') as f:
        d = json.load(f)
    d['_path'] = path
    d['_num'] = num
    return d


def outdir(d, *sub):
    p = os.path.join(OUT, f"l{d['_num']}", *sub)
    os.makedirs(p, exist_ok=True)
    return p


def all_questions(d):
    t = d['tiers']
    return t['start'] + t['think'] + t['go'] + [t['investigation']]


def qmap(d):
    m = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    m[d['tiers']['investigation']['id']] = d['tiers']['investigation']
    for q in d['exit']:
        m[q['id']] = q
    return m


def slide_map(d):
    return {s['id']: s for s in d['slides']}


def part_map(d):
    return {p['id']: p for p in d['timing']['parts']}


TIER_NAME = {'start': 'Start here', 'think': 'Think harder', 'go': 'Go further', 'investigation': 'Investigation'}

# ---------------------------------------------------------------- timing model (same assumptions as docs/audit/timing_p1.md)

SAY_WPM = 120.0
READ_WPM = 110.0
SLIDE_S = 25
HOLD_S = 30
MOVE_S = 90
ASK_RESP_S = 30


def words(s):
    return len(re.findall(r"[A-Za-z0-9’'-]+", s))


def resolve_text(d, part, line):
    t = line.get('text', '')
    if t == '@rec':
        return d['rec'][part]['say']
    return t


def line_seconds(d, part, line):
    """Seconds one script line takes. NOTE/STUCK take none; par lines run alongside the previous line."""
    if line.get('optional') or line.get('par'):
        return 0.0
    k = line['k']
    txt = resolve_text(d, part, line)
    if k in ('SAY', 'REC'):
        return words(txt) * 60.0 / SAY_WPM
    if k == 'READ':
        return words(txt) * 60.0 / READ_WPM
    if k == 'ASK':
        return words(txt) * 60.0 / SAY_WPM + line.get('resp', ASK_RESP_S)
    if k == 'SLIDE':
        return line.get('s', SLIDE_S)
    if k in ('DO', 'WORK'):
        return float(line['s'])
    if k == 'HOLD':
        return float(line.get('s', HOLD_S))
    if k == 'MOVE':
        return float(line.get('s', MOVE_S))
    return 0.0


def segment_timeline(d):
    """Return [{part, title, start, end, alloc, used, lines:[(t0, secs, line)]}]."""
    pm = part_map(d)
    out = []
    for seg in d['script']['segments']:
        p = pm[seg['part']]
        t = p['start'] * 60.0
        rows = []
        for ln in seg['lines']:
            s = line_seconds(d, seg['part'], ln)
            rows.append((t, s, ln))
            t += s
        used = t - p['start'] * 60.0
        out.append({'part': seg['part'], 'title': p['title'], 'start': p['start'], 'end': p['end'],
                    'alloc': (p['end'] - p['start']) * 60.0, 'used': used, 'lines': rows})
    return out


def optional_seconds(d):
    tot = 0.0
    for seg in d['script']['segments']:
        for ln in seg['lines']:
            if ln.get('optional'):
                k = ln['k']
                txt = ln.get('text', '')
                if k == 'SLIDE':
                    tot += SLIDE_S
                elif k in ('SAY',):
                    tot += words(txt) * 60.0 / SAY_WPM
                elif k == 'WORK':
                    tot += ln['s']
    return tot


def mmss(sec):
    sec = int(round(sec))
    return f'{sec // 60}:{sec % 60:02d}'


def slow_factor(line):
    """Slow-class scenario multipliers: speech 1.10, children's work/waits 1.20, slide changes/moves 1.20."""
    k = line['k']
    return 1.10 if k in ('SAY', 'REC', 'READ') else 1.20


def slow_used(seg):
    return sum(s * slow_factor(ln) for (_, s, ln) in seg['lines'])


def child_item_table(d):
    """Estimated finishers per child profile from each Start here question's `mins` (LOW x1.7, HIGH x0.65 of MIDDLE)."""
    pm = part_map(d)
    start = d['tiers']['start']
    p1 = [q for q in start if q['page'] == 1]
    p2 = [q for q in start if q['page'] == 2]
    work = pm['work']
    return {'p1': sum(q['mins'] for q in p1), 'p2': sum(q['mins'] for q in p2), 'n': len(start)}


# ---------------------------------------------------------------- text helpers

def p_html(s):
    return E(s)


BLANK_MM = {2: 9, 3: 17, 4: 22, 5: 30, 6: 40, 7: 55}   # 7 or more underscores = the longest line      # printed width of an answer line by the number of underscores (3 = the standard blank)


def blanks(text):
    """Answer blanks in a question: __ (2 underscores) a short line for one digit, ___ the standard line, ____ to _______ longer lines
    for words or numbers with units, and [] an empty answer box (a clear square for ages 6-8)."""
    t = E(text)
    t = re.sub(r'_{2,}', lambda m: f'<span class="al" style="min-width:{BLANK_MM[min(len(m.group(0)), 7)]}mm"></span>', t)
    return t.replace('[]', '<span class="boxb"></span>')


def kits(d):
    """Kit pages a lesson declares: workbook.kits = [] (none) or [{type, title, intro, ...}]. Absent = the legacy tens-bars page."""
    wb = d.get('workbook', {})
    if 'kits' in wb: return wb['kits']
    return [{'type': 'base_ten', 'title': 'Kit page: tens bars and ones squares', 'intro': 'A grown-up cuts these out before the lesson. A bar is a ten. A square is a one. Keep them in an envelope.'}]


def wb(d, key, default=''):
    return d.get('workbook', {}).get(key, default)


def header_topic(d):
    return wb(d, 'header') or d['moe']['strand'] + ': ' + d['big_idea'].lower()


def slide_time(d, s):
    p = part_map(d)[s['part']]
    return f"{p['start']}–{p['end']} MIN"


def font_css():
    path = os.path.join(ROOT, 'fonts', 'fonts.css')
    return open(path, encoding='utf-8').read()


def mi_uri():
    """Mi the dolphin (owner-chosen mascot) as a data URI. The image file is never edited."""
    import base64
    nocalc = os.path.join(L1, 'assets', 'mi_dolphin_nocalc.png')    # used automatically if the owner supplies a version without the calculator
    with open(nocalc if os.path.exists(nocalc) else os.path.join(L1, 'assets', 'mi_dolphin_transparent.png'), 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode()
