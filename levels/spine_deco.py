"""Strategy-of-the-day and common look-back on the HOLIDAY lesson decks (docs/pedagogy/spine_routine_spec.md sections 2-4).
IDEMPOTENT post-pass, called from levels/restyle.py just before mi_deco (so it survives a gen_* rebuild + restyle), or run directly:
    python3 levels/spine_deco.py split/l1 [...]          (second run changes 0 files)
What it does per deck:
  title slide   a 'TODAY'S TOOL' chip (icon + name) inside the 'Today we will' card; speaker note line starting 'SPINE:'
  Levels 1-3    one full slide '<key>-tool' ('Strategy of the day') right after the title, added to deck.json order if absent
  Levels 4-6    a small badge on the talk slide ('Tool today: <name>. Did it help?') instead of a full slide
  reflect slide rebuilt whole: title 'Look back', three prompts in the level's band wording, tool ticks, still stuck / pass, timer label
Idempotence: every inserted fragment is ONE top-level element with data-spine="..." followed by <!--/spine-->; each run removes
those first. The tool slide and reflect slide are written whole from templates; aside text added by this pass starts 'SPINE:'.
Only the levels in LEVELS_ON are touched (Level 1 pilot; add '2'..'6' to roll out)."""
import sys, os, re, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import spine_icons as si
LEVELS_ON = {'1', '2', '3', '4', '5', '6'} if os.environ.get('SPINE_ALL') else {'1'}   # Level 1 pilot (stage A); SPINE_ALL=1 or edit this set to roll out
ACC = {'1': '#1F7A6F', '2': '#2A7DC9', '3': '#3E8E41', '4': '#7B4FB5', '5': '#D9662B', '6': '#C2386B'}   # same as restyle.ACC
NAVY, CREAM, YEL = '#1B2A49', '#FFF9EC', '#FFC93C'
MARK = re.compile(r'<(div|span) data-spine=.*?<!--/spine-->\n?', re.S)
ASIDE_SP = re.compile(r' ?SPINE:.*?</aside>', re.S)
IMG = re.compile(r'<img data-mi="[^>]*>\n?')
def key_level(d):
    k = os.path.basename(d.rstrip('/')); m = re.match(r'p(\d)l(\d+)$', k)
    if m: return k, m.group(1), int(m.group(2))
    m = re.match(r'l(\d+)$', k); return (k, '1', int(m.group(1))) if m else (k, None, 0)
def esc(s): return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
def aside_text(s): return s.replace('"', '&quot;')

def info(lv, ln):
    row = si.lesson(lv, ln); band = si.band(lv)
    if row['main'] == 'choose': return row, band, None
    return row, band, si.tool(row['main'])

# ---------- title slide ----------
def chip(lv, ln):
    row, band, t = info(lv, ln)
    if t is None:
        icons = ''.join(si.icon(x['id'], CREAM, 62) for x in si.SPINE['tools'])
        inner = (f'<div style="display:flex;gap:18px;flex:none">{icons}</div><div><p style="font-size:24px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY&#39;S TOOL</p>'
                 f'<p style="font-family:\'Fredoka\', Arial, sans-serif;font-size:44px;font-weight:600">You choose</p></div>')
    else:
        inner = (f'<div style="flex:none;width:90px;height:90px">{si.icon(t["id"], CREAM, 90)}</div><div><p style="font-size:24px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY&#39;S TOOL</p>'
                 f'<p style="font-family:\'Fredoka\', Arial, sans-serif;font-size:50px;font-weight:600;line-height:1.05">{esc(t["name"])}</p></div>')
    return f'<div data-spine="chip" style="display:flex;align-items:center;gap:26px;min-height:90px;margin-top:14px">{inner}</div><!--/spine-->'
def note_title(lv, ln):
    row, band, t = info(lv, ln); S = si.SPINE['script']
    if t is None: return f'SPINE: {S["choose_say"]} {S["choose_do"]}'
    return 'SPINE: ' + S['opening_say'].replace('{name}', t['name']).replace('{def}', t['def'][band]) + ' ' + S['opening_do']
def do_title(html, lv, ln):
    html = MARK.sub('', html); html = ASIDE_SP.sub('</aside>', html)
    m = re.search(r'(<div style="background:#26385F;[^"]*">.*?</p>)(</div>)', html, re.S)
    if not m: return html
    html = html[:m.end(1)] + chip(lv, ln) + html[m.end(1):]
    html = re.sub(r'</aside>', lambda _: ' ' + aside_text(note_title(lv, ln)) + '</aside>', html, count=1)
    return html

# ---------- tool slide (Levels 1-3) ----------
def pill_text(title_html):
    m = re.search(r'([\d.]+–[\d.]+ MIN)</p>', title_html); return m.group(1) if m else '0–2 MIN'
def tool_slide(sid, lv, ln, pill):
    row, band, t = info(lv, ln); a = ACC[lv]; S = si.SPINE; kit = S['kit_line'] if ln == 1 else ''
    sec = (f'<section id="{sid}" data-transition="fade" data-theme="modern2" style="background:linear-gradient(135deg,#1B2A49 0%,#101B33 100%);color:{CREAM};'
           f'font-family:\'Nunito Sans\', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px;position:relative;overflow:hidden">\n')
    bar = (f'<div data-deco="bar" style="position:absolute;left:0;top:0;width:1920px;height:18px;display:flex"><div style="flex:5;background:{NAVY}"></div><div style="flex:3;background:{a}"></div><div style="flex:1;background:{YEL}"></div></div>\n'
           f'<p style="position:absolute;right:128px;top:52px;font-size:26px;font-weight:800;letter-spacing:2px;color:{a};background:#FFFFFF;border:2px solid {a};border-radius:999px;padding:6px 22px">{pill}</p>\n')
    lab = f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">STRATEGY OF THE DAY</p>'
    if t is None:
        cells = ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:10px;width:360px">{si.icon(x["id"], CREAM, 150)}<p style="font-size:32px;font-weight:700;text-align:center">{esc(x["name"])}</p></div>' for x in S['tools'])
        body = (f'{lab}<h2 style="font-family:\'Fredoka\', Arial, sans-serif;font-size:96px;font-weight:600;line-height:1.05">Today you choose the tool</h2>'
                f'<div style="display:flex;flex-wrap:wrap;gap:24px 20px;width:1500px">{cells}</div>'
                f'<p style="font-size:40px;color:#C9D4EC">Which tool will you pick? Tick it in your workbook, then say why.</p>')
    else:
        defn = t['def'][band]
        body = (f'{lab}<div style="display:flex;align-items:center;gap:72px"><div style="flex:none;width:360px;height:360px">{si.icon(t["id"], CREAM, 360)}</div>'
                f'<div style="display:flex;flex-direction:column;gap:22px"><h2 style="font-family:\'Fredoka\', Arial, sans-serif;font-size:110px;font-weight:600;line-height:1.05">{esc(t["name"])}</h2>'
                f'<p style="font-size:44px;line-height:1.3;color:#C9D4EC">{esc(defn)}</p></div></div>'
                f'<div style="background:#26385F;border-radius:24px;padding:28px 40px;align-self:flex-start;margin-right:150px"><p style="font-size:44px;font-weight:600">Say it with me: &ldquo;{esc(t["name"])}!&rdquo;</p></div>')
        if kit: body += f'<p style="font-size:34px;color:#C9D4EC">{esc(kit)}.</p>'
    foot = '<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">Math Inquirers Holiday Program  •  Notice it. Test it. Explain why.</p>\n'
    aside = '<aside>' + aside_text(note_title(lv, ln).replace('SPINE: ', 'SPINE: Show for about 20 seconds, inside the opening. ', 1) + (' ' + kit + '.' if kit else '')) + '</aside>\n'
    return sec + bar + body + '\n' + foot + aside + '</section>\n'

# ---------- talk badge (Levels 4-6) ----------
def badge(lv, ln):
    row, band, t = info(lv, ln)
    txt = 'Tool today: ' + esc(t['name']) + '. Did it help?' if t else 'Which tool did you choose? Why?'
    ic = si.icon(t['id'], NAVY, 50) if t else ''
    return (f'<div data-spine="badge" style="position:absolute;left:128px;bottom:100px;height:70px;display:flex;align-items:center;gap:16px;background:#FFFFFF;border:2px solid {ACC[lv]};border-radius:999px;padding:6px 28px 6px 16px;font-size:30px;font-weight:700;color:{NAVY}">{ic}<span>{txt}</span></div><!--/spine-->\n')
def do_talk(html, lv, ln):
    html = MARK.sub('', html)
    i = html.rfind('<aside')
    if i < 0: i = html.rfind('</section>')
    return html[:i] + badge(lv, ln) + html[i:]

# ---------- reflect slide ----------
def box(px=36):
    return f'<span style="display:inline-block;flex:none;width:{px}px;height:{px}px;border:4px solid {NAVY};border-radius:8px;background:#FFFFFF"></span>'
def reflect_slide(old, lv, ln, sid):
    a = ACC[lv]; band = si.band(lv); L = si.SPINE['lookback']; P = L['prompts'][band]
    head = old[:old.index('<h2')]
    head = MARK.sub('', head)
    pm = re.search(r'([\d.]+)–([\d.]+) MIN', old); s0, s1 = (pm.group(1), pm.group(2)) if pm else ('85', '88')
    h2style = re.search(r'<h2 style="([^"]*)"', old).group(1)
    foot = re.search(r'<p style="position:absolute;left:128px;bottom:64px[^>]*>[^<]*</p>', old).group(0)
    img = IMG.search(old); img = img.group(0) if img else ''
    yn = f'<span style="display:inline-flex;align-items:center;gap:12px;margin-left:28px;white-space:nowrap">{box()}yes</span><span style="display:inline-flex;align-items:center;gap:12px;margin-left:28px;white-space:nowrap">{box()}not yet</span>'
    a3 = L['answer3'][band]
    ans3 = f'<span style="display:inline-flex;align-items:flex-end;gap:14px;font-size:32px;font-weight:600;color:#3B4A6B;white-space:nowrap">{esc(a3)}<span style="display:inline-block;width:{260 if band=="A" else 420}px;border-bottom:4px dotted {NAVY};height:30px"></span></span>'
    def row(n, q, right, first=False):
        bt = '' if first else f'border-top:2px solid #DCE4F0;'
        return (f'<div style="display:flex;gap:28px;align-items:center;padding:24px 0;{bt}"><p style="flex:none;width:64px;height:64px;border-radius:50%;background:{a};color:{CREAM};font-size:38px;font-weight:800;display:flex;align-items:center;justify-content:center">{n}</p>'
                f'<p style="flex:1;font-size:46px;font-weight:700;line-height:1.2">{esc(q)}</p><div style="flex:none;font-size:38px;font-weight:700;display:flex;align-items:center">{right}</div></div>')
    rows = row(1, P[0], yn, True) + row(2, P[1], yn) + row(3, P[2], ans3)
    tools = ''.join(f'<span style="display:inline-flex;align-items:center;gap:8px">{si.icon(x["id"], NAVY, 76)}{box(32)}</span>' for x in si.SPINE['tools'])
    foot2 = (f'<div style="display:flex;align-items:center;gap:20px;border-top:2px solid #DCE4F0;padding-top:24px;font-size:32px;font-weight:700"><span style="white-space:nowrap">{esc(L["footer_tools"])}:</span>{tools}</div>'
             f'<div style="display:flex;gap:56px;font-size:32px;font-weight:600;color:#3B4A6B;margin-top:14px"><span style="display:inline-flex;align-items:center;gap:12px">{box(32)}{esc(L["stuck"])}</span><span style="display:inline-flex;align-items:center;gap:12px">{box(32)}{esc(L["pass"])}</span></div>')
    timer = f'Timer: {L["timer_seconds"][band]} seconds'
    card = (f'<div data-spine="reflect" style="background:#FFFFFF;border:2px solid #DCE4F0;box-shadow:0 6px 18px rgba(27,42,73,0.08);border-radius:24px;padding:14px 40px 22px;display:flex;flex-direction:column;gap:6px;width:1520px">{rows}{foot2}</div><!--/spine-->')
    sub = f'<div style="display:flex;gap:20px;align-items:center"><p style="background:{YEL};color:{NAVY};border-radius:999px;padding:8px 24px;font-size:28px;font-weight:700">{timer}</p><p style="font-size:28px;color:#3B4A6B">{esc(L["intro"])}</p></div>'
    S = si.SPINE['script']
    flex = f' After the look-back, minutes {s1} to 90 are flex time (the buffer): finish stamps, then goodbye. Do not start anything new.' if float(s1) < 90 else ''
    note = ('SPINE: ' + f'Minutes {s0} to {s1}. Start the timer ({L["timer_seconds"][band]} seconds). Say: "{S["lookback_say"]}" '
            'Children tick the Look back box on the Choose and look-back page of their workbook, or just tick on paper. A pass is always allowed. It is never marked, never collected in front of the group and never read out; the tutor may look at it afterwards. '
            'If a child ticks "I am still stuck", check in during the open session next lesson (a quick visit to the shared breakout room or a hand signal, with a parent nearby; never a direct message). Do not ask children to share. '
            'Praise a check you saw, not speed. Then stamp the journals.' + flex)
    return (head + f'<h2 style="{h2style}">Look back</h2>{sub}{card}\n' + foot + '\n' + img + '<aside>' + aside_text(note) + '</aside>\n</section>\n')

# ---------- deck ----------
def apply(d):
    k, lv, ln = key_level(d)
    if lv not in LEVELS_ON: return 0
    base = os.path.join(d, 'project'); dj = os.path.join(base, 'deck.json'); sl = os.path.join(base, 'slides')
    deck = json.load(open(dj)); order = deck['order']; n = 0
    def rw(path, new):
        nonlocal n
        old = open(path).read() if os.path.exists(path) else None
        if old != new: open(path, 'w').write(new); n += 1
    pre = k if lv == '1' else k   # slide ids are '<key>-title', e.g. l1-title, p2l3-title
    tid = f'{pre}-title'
    if tid in order:
        p = os.path.join(sl, tid + '.html'); h = open(p).read(); rw(p, do_title(h, lv, ln))
    if lv in '123' and tid in order:
        toolid = f'{pre}-tool'
        pill = pill_text(open(os.path.join(sl, tid + '.html')).read())
        rw(os.path.join(sl, toolid + '.html'), tool_slide(toolid, lv, ln, pill))
        if toolid not in order:
            order.insert(order.index(tid) + 1, toolid); deck['order'] = order
            json.dump(deck, open(dj, 'w'), indent=1, ensure_ascii=False); n += 1
    if lv in '456':
        tk = f'{pre}-talk'
        if tk in order:
            p = os.path.join(sl, tk + '.html'); rw(p, do_talk(open(p).read(), lv, ln))
    rid = f'{pre}-reflect'
    if rid in order:
        p = os.path.join(sl, rid + '.html'); rw(p, reflect_slide(open(p).read(), lv, ln, rid))
    # no duplicate ids
    if len(order) != len(set(order)): raise SystemExit(f'{d}: duplicate slide ids in deck.json order')
    return n
if __name__ == '__main__':
    for d in sys.argv[1:]: print(d, apply(d))
