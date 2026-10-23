#!/usr/bin/env python3
"""Generate the six per-level pages (website/level_pages/ages-A-B.html) from one template.

    node level_dump.js        # only to refresh data/level_lessons.json from the lesson files
    python3 level_pages.py    # writes level_pages/*.html; build_site.py then wraps them

Inputs: data/level_lessons.json (real lesson titles and topics), data/beta_schedule.json (the same
schedule the home page uses), the hand-written per-level facts below (taken from each level's SPEC.md,
kit.js and lesson materials), and lp_parts.txt (the home page CSS). Nothing here is invented: the
placement thresholds are the ones on the home page and in docs/levels_and_placement.md.
"""
import datetime as dt
import html
import json
import os

import interest_ui

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'level_pages')

# TODO(singapore-map): when the Singapore row / tier-level syllabus map page exists, set this to its
# URL path (for example '/singapore-syllabus/') and the link appears in the "Not affiliated" note.
SYLLABUS_MAP_URL = '/syllabus/'

LEVELS = [
    dict(n=1, a=6, b=8, builds='Primary 1 maths', full='Ages 6-8 (builds on Primary 1 maths)',
         blurb='Number patterns, number bonds, money, shapes and logic, with objects.',
         kit=['Play coins and play notes, with $1 coins',
              'Paper cube strips',
              'Ten-frames and 20 paper counters (10 red, 10 yellow)',
              'Number strips 0 to 50 and 0 to 20',
              '24 shape and sorting tiles (4 shapes, 3 colours, 2 sizes)'],
         home=['A laptop or tablet with a camera, on a table with space for the kit',
               'Pencil, crayons, scissors and a cm ruler',
               'A mini whiteboard and marker',
               'Everyday things the lessons use, such as paper cups, straws or lolly sticks (never real matches), paper clips, erasers and buttons (small objects only with a grown-up nearby)'],
         puzzle=dict(tag='Go further · Lesson 1', big='3, 7, 11 …',
                     q='Frog A starts at 3 and jumps 4 each time. Frog B starts at 5 and jumps 3 each time. Which numbers up to 40 do both frogs land on?',
                     a='11, 23 and 35.'),
         note=None),
    dict(n=2, a=7, b=9, builds='Primary 2 maths', full='Ages 7-9 (builds on Primary 2 maths)',
         blurb='Three-digit numbers, missing digits, arrays, money, fractions and measures.',
         kit=['Place-value cards', 'Two sets of digit cards 0 to 9', 'Fraction strips', 'A paper clock',
              'Paper strips of numbered squares', 'Cube nets', 'Play coins and play notes, with $1 coins'],
         home=['A laptop or tablet with a camera, on a table with space for the kit',
               'Pencil, coloured pencils, scissors and squared paper',
               'A mini whiteboard and marker',
               'Counters, and linking cubes in 3 colours if you have them',
               'Everyday things the lessons use, such as paper cups, string, a coat hanger, two cups or bottles of different sizes, and a little dry rice or sand'],
         puzzle=dict(tag='Think harder · Lesson 1', big='4 4 7',
                     q='Use the digit cards 4, 4 and 7. How many different 3-digit numbers can you make? Why is it not 6?',
                     a='3 numbers: 447, 474 and 744. The two 4s look the same, so swapping them does not make a new number.'),
         note=None),
    dict(n=3, a=8, b=10, builds='Primary 3 maths', full='Ages 8-10 (builds on Primary 3 maths)',
         blurb='Four-digit numbers, times tables 6 to 9, bar models, remainders, fractions and area.',
         kit=['Digit cards', 'A fraction wall', 'A square grid', 'Right-angle testers', 'Play coins and play notes, with $1 coins'],
         home=['A laptop or tablet with a camera, on a table with space for the kit',
               'Pencil, coloured pencils, a ruler and scissors',
               'A mini whiteboard and marker',
               'Scrap paper, squared or 1 cm grid paper, and about 25 to 30 counters or cubes',
               'If you have them: a measuring tape or metre ruler, a kitchen scale, a measuring jug and a clock with movable hands'],
         puzzle=dict(tag='Think harder · Lesson 5', big='r 3 and r 5',
                     q='I am a number between 20 and 30. When I am divided by 4, the remainder is 3. When I am divided by 6, the remainder is 5. What number am I?',
                     a='23. Divided by 4 the choices are 23 and 27, and 23 ÷ 6 = 3 remainder 5.'),
         note=None),
    dict(n=4, a=9, b=11, builds='Primary 4 maths', full='Ages 9-11 (builds on Primary 4 maths)',
         blurb='Factors and multiples, five-digit numbers, order of operations, decimals, angles and data.',
         kit=['A fraction wall', 'A square grid and a dot grid', 'A cube net', 'Right-angle testers',
              'Digit, point, sign and bracket cards', 'Graph grids', 'A paper clock and pizza circles'],
         home=['A laptop or tablet with a camera, on a table with space for the kit',
               'A clear 180° protractor and a 30 cm ruler for each child (not printed in the kit; the kit page lists them)',
               'Pencil, two coloured pencils, scissors and sticky tape',
               'A mini whiteboard and marker',
               'Squared paper, about 30 counters or tiles, and a dice'],
         puzzle=dict(tag='Think harder · Lesson 1', big='6 s and 9 s',
                     q='One lighthouse flashes every 6 seconds. Another flashes every 9 seconds. They flash together now. After how many seconds will they next flash together?',
                     a='18 seconds. The first flashes at 6, 12, 18 and the second at 9, 18.'),
         note=None),
    dict(n=5, a=10, b=12, builds='Primary 5 maths', full='Ages 10-12 (builds on Primary 5 maths)',
         blurb='Numbers to 10 million, fractions, area of a triangle, volume, rate, percentage and angles.',
         kit=['A fraction wall', 'A square grid', 'A dot grid', 'A cube net'],
         home=['A laptop or tablet with a camera, on a table with space for the kit',
               'Pencil, coloured pencils, a ruler, scissors and a protractor',
               'A mini whiteboard and marker',
               'A calculator (a phone calculator is fine); the lessons use it to check, not to do the thinking',
               'About 30 one-centimetre cubes, dice or similar, matchsticks or toothpicks, counters and squared paper'],
         puzzle=dict(tag='Think harder · Lesson 2', big='1/3 then 1/4',
                     q='Ben ate 1/3 of a pizza. Ali ate 1/4 of what was left. What fraction of the pizza is left?',
                     a='1/2. 2/3 was left after Ben. Ali ate 1/4 of that, so 3/4 of 2/3 = 1/2 is left.'),
         note=None),
    dict(n=6, a=11, b=13, builds='Primary 6 maths, after the PSLE', full='Ages 11-13 (maths + coding bridge, after PSLE)',
         blurb='Sequences, primes, negative numbers, algebra, counting, probability, codes and data, each also explored in Scratch.',
         kit=['Unplugged code cards', 'A square grid'],
         home=['A laptop or desktop with Scratch 3 open in the browser (scratch.mit.edu, free, no account needed); a tablet can run Scratch but is slower',
               'Pencil, coloured pencils, a ruler, a protractor and scissors',
               'A mini whiteboard and marker',
               'About 25 matchsticks or toothpicks, linking cubes or counters, two dice and a coin, and squared paper',
               'Optional: a Python editor, for children who already know Python'],
         puzzle=dict(tag='Think harder · Lesson 1', big='2, 9, 16, 23 …',
                     q='Is 200 a term of 2, 9, 16, 23, …? Explain.',
                     a='No. The rule is 7n − 5. The 29th term is 198 and the 30th term is 205, so 200 is skipped.'),
         note='The maths is enrichment toward secondary maths, with every puzzle also explored in code. Some topics (negative numbers, primes, simple equations, angles in polygons) are met in lower-secondary maths; others (sequences and the nth term, counting, probability, clock arithmetic) are enrichment, so this is not a Secondary 1 course.'),
]
for L in LEVELS:
    L['slug'] = 'ages-%d-%d' % (L['a'], L['b'])
    L['ages'] = '%d-%d' % (L['a'], L['b'])
    L['path'] = '/%s/' % L['slug']


def esc(s):
    return html.escape(str(s), quote=True)


def t12(t):
    h, m = map(int, t.split(':'))
    return '%d:%02d%s' % ((h % 12) or 12, m, 'pm' if h >= 12 else 'am')


def dlabel(iso):
    return dt.date.fromisoformat(iso).strftime('%a %-d %b')


# Card CSS shared by the level pages and the level index on the home page (added to the home page CSS).
LEVEL_CSS = '''
.lvgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.lvcard{display:grid;gap:8px;align-content:start;border:2.5px solid var(--ink);border-radius:22px;padding:18px;background:var(--card);box-shadow:5px 5px 0 var(--ink);text-decoration:none;color:var(--fg)}
.lvcard:hover{background:var(--soft)}
.lvcard .k{font:800 12px var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.lvcard h3{font-size:24px}
.lvcard .go{font-weight:800;font-size:14px}
.lvcard[aria-current="page"]{background:var(--soft)}
@media (max-width:900px){.lvgrid{grid-template-columns:1fr 1fr}}
@media (max-width:520px){.lvgrid{grid-template-columns:1fr}}
'''
PAGE_CSS = '''
.hero{grid-template-columns:1.2fr 1fr}
.glance{display:grid;gap:10px;color:#1B2A49;background:var(--cream);border:2.5px solid #1B2A49;border-radius:22px;padding:20px;box-shadow:5px 5px 0 #1B2A49;list-style:none;margin:0}
.glance li{display:grid;gap:0}
.glance b{font:800 12px var(--body);letter-spacing:.08em;text-transform:uppercase;opacity:.7}
.glance span{font:600 19px var(--head)}
.tiers{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.klist{padding-left:20px;display:grid;gap:6px}
.sched{display:grid;gap:14px}
.sched table td,.sched table th{white-space:nowrap}
.fine{font-size:13.5px;color:var(--muted)}
.crumbs{font-size:14px;color:var(--muted)}
details.dates{background:var(--card);border:2px solid var(--ink);border-radius:16px;padding:12px 16px}
details.dates summary{font:600 17px var(--head);cursor:pointer}
details.ans{margin-top:4px}
details.ans summary{font-weight:800;cursor:pointer;color:var(--fg)}
details.ans p{margin-top:8px}
@media (max-width:820px){.tiers{grid-template-columns:1fr}.hero{grid-template-columns:1fr}}
'''


def css():
    return open(os.path.join(HERE, 'lp_parts.txt'), encoding='utf-8').read() + LEVEL_CSS + PAGE_CSS + interest_ui.CSS


def level_index_cards(current=None):
    out = []
    for L in LEVELS:
        cur = ' aria-current="page"' if L['n'] == current else ''
        out.append('<a class="lvcard" href="%s"%s><span class="k">Level %d</span><h3>Ages %s</h3>'
                   '<p class="small muted">Builds on %s</p><p class="small">%s</p><span class="go">%s</span></a>'
                   % (L['path'], cur, L['n'], L['ages'], esc(L['builds']), esc(L['blurb']),
                      'You are here' if L['n'] == current else 'See Ages %s →' % L['ages']))
    return ''.join(out)


def schedule_block(L, sch):
    g = next(x for x in sch['groups'] if x['level'] == L['n'])
    per, tot = sch['price']['per_lesson'], sch['price']['total']
    times = '<br>'.join('<b>%s</b> %s–%s' % (esc(s['day']), t12(s['start']), t12(s['end'])) for s in g['sessions'])
    moved = next((l for l in g['lessons'] if l.get('moved')), None)
    exc = ''
    if moved:
        exc = '<br>Week 5: %s %s–%s (not Fri 25 Dec)' % (dlabel(moved['date']), t12(moved['start']), t12(moved['end']))
    rows = ''.join('<tr><td class="num">%d</td><td>%s</td><td>%s–%s</td></tr>'
                   % (l['n'], dlabel(l['date']), t12(l['start']), t12(l['end'])) for l in g['lessons'])
    reg = '/?level=%d&amp;group=%s#register' % (L['n'], g['id'])
    return ('<div class="sched"><div class="session"><div class="row" style="justify-content:space-between">'
            '<span class="pill p-ok">Open</span><span class="small muted">Up to %d children</span></div>'
            '<h3>Level %d <span class="muted small">ages %s</span></h3>'
            '<p>%s<br><span class="muted small">First lesson %s · last %s%s<br>Live video class · %d minutes a lesson · 10 lessons over %d weeks</span></p>'
            '<a class="btn yel" href="%s" style="justify-self:start">Register for Level %d</a></div>'
            '<details class="dates"><summary>All 10 lesson dates</summary><div class="tbl" style="margin-top:10px"><table>'
            '<thead><tr><th class="num">Lesson</th><th>Date</th><th>Time (Singapore)</th></tr></thead><tbody>%s</tbody></table></div>'
            '<p class="fine" style="margin-top:8px">No lessons on Fri 25 Dec (Christmas Day).</p></details>'
            '<p class="small muted">Beta fee: S$%s a lesson, S$%s for all 10 lessons. Nothing to pay when you register: we confirm your place first and then send payment details. If a group fills, we open another.</p>%s</div>'
            % (g['seats'], L['n'], esc(g['ages']), times, esc(g['first']), esc(g['last']), exc,
               sch['lesson_minutes'], sch['weeks'], reg, L['n'], rows, per, tot,
               interest_ui.other_times_block(L['n'], interest_ui.load_slots())))


def placement_block(L):
    prev = next((x for x in LEVELS if x['n'] == L['n'] - 1), None)
    nxt = next((x for x in LEVELS if x['n'] == L['n'] + 1), None)
    down = ('one level down (<a href="%s">Ages %s</a>)' % (prev['path'], prev['ages'])) if prev else 'one level down'
    s = ('<p class="muted">Levels are named by age, and each spans three ages and overlaps the next, so children can join the level that suits how they are learning now. '
         'This level is for ages %s and builds on %s.</p>'
         "<p>Take the free 30-minute diagnostic for the level that matches your child's school year (the Math Inquirers Placement Check for that level). Then:</p>"
         '<ul><li>The check is scored out of 10. 7 to 10: enrol at this level.</li>'
         '<li>4 to 6: enrol at this level (the tutor will note that support may help), or choose %s.</li>'
         '<li>0 to 3: we recommend %s.</li>' % (L['ages'], esc(L['builds']), down, down))
    if nxt:
        s += '<li>If it was too easy (9 or 10 out of 10), your child may also try the diagnostic one level up (<a href="%s">Ages %s</a>).</li>' % (nxt['path'], nxt['ages'])
    s += '</ul><p>You have the final say. You can change the level before lesson 1 at no cost, and the price is the same at every level.'
    if not prev:
        s += ' Ages 6-8 is the lowest level: if your child is a weaker learner there, they start with the free taster and a tutor chat.'
    s += '</p>'
    return s


def page(L, lessons, sch):
    n = L['n']
    title = 'Ages %s maths holiday program | Math Inquirers' % L['ages']
    cards = ''.join('<div class="lesson"><div class="n">%d</div><div class="t">%s</div><div class="s">%s</div></div>'
                    % (x['n'], esc(x['title']), esc(x['topic'])) for x in lessons)
    g = next(x for x in sch['groups'] if x['level'] == n)
    p = L['puzzle']
    syl = ''
    if SYLLABUS_MAP_URL:
        syl = ' See how the levels line up with the Singapore syllabus on the <a href="%s">syllabus map</a>.' % SYLLABUS_MAP_URL
    note = ('<p class="small muted">%s</p>' % esc(L['note'])) if L['note'] else ''
    return '''<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<style>%(css)s</style>
<div class="wrap">
<header class="bar"><a class="brand" href="/" style="text-decoration:none"><i>?</i><span>Math Inquirers</span></a><nav class="nav" aria-label="Site"><a class="tab" href="/#program" style="text-decoration:none">Program</a><a class="tab" href="/#classes" style="text-decoration:none">Classes</a><a class="tab" href="/#levels" style="text-decoration:none" aria-current="true">Levels</a><a class="tab" href="/#price" style="text-decoration:none">Price</a><a class="tab" href="/#faq" style="text-decoration:none">FAQ</a><a class="btn yel sm" href="/?level=%(n)d#register" style="margin-left:6px;padding:8px 16px">Register</a></nav></header>
<main id="top">
<p class="crumbs"><a href="/">Home</a> · <a href="/#levels">Levels</a> · Ages %(ages)s</p>
<section class="hero"><div class="sec"><span class="eyebrow">Level %(n)d · Ages %(ages)s · Builds on %(builds)s</span><h1>Ages %(ages)s <mark>maths</mark> holiday program</h1><p class="slogan">Notice it. Test it. Explain why.</p><p class="lead">Ten hands-on lessons where children solve puzzles, test ideas and explain their answers. Live online in small groups of up to 8, from your own home.</p>
<div class="row" style="margin-top:6px"><a class="btn yel" href="/?level=%(n)d#register">Register for Level %(n)d</a><a class="btn ghost" href="#times">See class times</a></div></div>
<ul class="glance" aria-label="Level at a glance"><li><b>Ages</b><span>%(ages)s</span></li><li><b>Builds on</b><span>%(builds)s</span></li><li><b>Lessons</b><span>10 × %(mins)d minutes, over %(weeks)d weeks</span></li><li><b>Group size</b><span>Up to %(seats)d children, live online</span></li><li><b>Beta fee</b><span>S$%(per)s a lesson, S$%(tot)s for all 10</span></li></ul></section>

<section class="sec" id="learn"><div class="shead"><span class="eyebrow">The 10 lessons</span><h2>What your child learns</h2><p class="muted">%(blurb)s Each lesson follows the same four steps: notice the pattern, test it, check the answer, explain why.</p>%(note)s</div><div class="lessons">%(cards)s</div></section>

<section class="sec" id="tiers"><div class="shead"><span class="eyebrow">Three tiers</span><h2>Start here, Think harder, Go further</h2><p class="muted">Every child's workbook has all three, plus an Investigation on the Finish page. After the first few questions, any child may choose to carry on or try the next tier. Nobody is told which page they are on, and a child who finds Think harder too hard simply goes back to Start here.</p></div>
<div class="tiers"><div class="tile yel"><span class="tag">Start here</span><h3>Start here</h3><p class="small">The core questions for the lesson, worked with objects, drawings and a partner. Everyone begins here.</p></div>
<div class="tile sky"><span class="tag">Think harder</span><h3>Think harder</h3><p class="small">Questions that ask for more than one step, a full list of possibilities, or a reason.</p></div>
<div class="tile mint"><span class="tag">Go further</span><h3>Go further</h3><p class="small">Open challenges with room to explore, where the aim is to find a way in and explain it.</p></div></div></section>

<section class="two"><div class="tile yel"><span class="tag">In the kit</span><h3>Cut-outs in the workbook</h3><ul class="klist">%(kit)s</ul><p class="small muted">Nothing needs to be bought for the kit. We post the printed workbook and kit to your home before the first lesson, and you cut out the pieces and keep them in one envelope.</p></div>
<div class="tile mint"><span class="tag">At home</span><h3>What your child needs</h3><ul class="klist">%(home)s</ul><p class="small muted">These come from the lesson plans for this level.</p></div></section>

<section class="sec" id="puzzle"><div class="shead"><span class="eyebrow">Try one now</span><h2>A sample puzzle</h2></div><div class="pzcard"><div class="pzl"><span class="tag">%(ptag)s</span><div class="big">%(pbig)s</div><p style="font-size:18px">%(pq)s</p><details class="ans"><summary>Show the answer</summary><p>%(pa)s</p></details></div><div class="pzr"><h3>In class, the answer is only half the job</h3><p class="muted">Children then explain how they know, and hear other ways of seeing the same puzzle. That is where the thinking grows.</p><a class="btn sm alt" href="/?level=%(n)d#register" style="justify-self:start">Register for Level %(n)d</a></div></div></section>

<section class="sec" id="placement"><div class="shead"><span class="eyebrow">Placement</span><h2>Is Ages %(ages)s right for my child?</h2></div>%(placement)s</section>

<section class="sec" id="times"><div class="shead"><span class="eyebrow">November beta · Singapore time</span><h2>Class times for Level %(n)d</h2></div>%(sched)s</section>

<section class="band yel" id="register"><div class="sec"><span class="eyebrow">Register</span><h2>Hold a seat</h2><p class="muted">Registration is a short form on our home page. Your level and group are already filled in. We reply within 2 working days with your group and payment details.</p></div><div class="row"><a class="btn yel" href="/?level=%(n)d&amp;group=%(gid)s#register">Register for Level %(n)d</a><a class="btn alt" href="/terms/">Terms and refund policy</a><a class="btn alt" href="/privacy/">Privacy and recording notice</a></div></section>

<section class="sec" id="levels"><div class="shead"><span class="eyebrow">All levels</span><h2>The six levels</h2></div><div class="lvgrid">%(index)s</div></section>
</main>
<footer><div><b>Math Inquirers</b><p style="margin-top:6px">An independent maths enrichment program by Preciouslyours Pte Ltd, Singapore. Not affiliated with MOE or the Gifted Education Programme. We do not identify or test for giftedness and we do not promise exam or competition results.%(syl)s</p></div><div><b>Register</b><p style="margin-top:6px"><a href="/?level=%(n)d#register">Register for Level %(n)d</a><br><a href="/">Back to the home page</a></p></div><div><b>Your details</b><p style="margin-top:6px">We use your details only to arrange the class and reply to you, in line with the PDPA. <a href="/terms/">Terms</a> · <a href="/privacy/">Privacy</a></p></div></footer>
</div>
''' % dict(
        title=esc(title), desc=esc('Math Inquirers Level %d for ages %s, building on %s: 10 live online lessons, three tiers of puzzles, kit contents, placement guidance and November beta class times.' % (n, L['ages'], L['builds'])),
        css=css(), n=n, ages=L['ages'], builds=esc(L['builds']), mins=sch['lesson_minutes'], weeks=sch['weeks'], seats=g['seats'],
        per=sch['price']['per_lesson'], tot=sch['price']['total'], blurb=esc(L['blurb']), note=note, cards=cards,
        kit=''.join('<li>%s</li>' % esc(k) for k in L['kit']), home=''.join('<li>%s</li>' % esc(k) for k in L['home']),
        ptag=esc(p['tag']), pbig=esc(p['big']), pq=esc(p['q']), pa=esc(p['a']),
        placement=placement_block(L), sched=schedule_block(L, sch), gid=g['id'], index=level_index_cards(n), syl=syl)


def main():
    lessons = json.load(open(os.path.join(HERE, 'data', 'level_lessons.json'), encoding='utf-8'))
    sch = json.load(open(os.path.join(HERE, 'data', 'beta_schedule.json'), encoding='utf-8'))
    os.makedirs(OUT, exist_ok=True)
    for L in LEVELS:
        assert len(lessons[str(L['n'])]) == 10
        open(os.path.join(OUT, L['slug'] + '.html'), 'w', encoding='utf-8').write(page(L, lessons[str(L['n'])], sch))
        print('wrote level_pages/%s.html' % L['slug'])


if __name__ == '__main__':
    main()
