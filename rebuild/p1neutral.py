"""P1 fix pass (student journey review): neutral page names, private sneak-peek puzzles, short safe look-back,
talk-time passing, a Go further what-if from the explore stage, minute labels, and the lesson-specific weak-cell fixes.
Call apply(D, n) as the LAST step of gen_lK.py (after p1fix.finish).  Idempotent: safe to run twice."""
import os, re, json, glob
from slidekit import *
import p1fix

CARD_X = 'border:2px solid #DCE4F0;box-shadow:0 6px 18px rgba(27,42,73,0.08);'

SUBS = [
    ('Think Harder', 'Think harder'),
    ('Optional: if you finish early', 'Your choice'),
    ('Finished early? Start Think harder T1 in your workbook, or try the Stretch slide.', 'Want more? You may choose Think harder T1 in your workbook.'),
    ('Think harder and Challenge are for early finishers or home.', 'Think harder, Go further and the Investigation are for every child to choose, any time or at home. Nobody is told which page they should be on.'),
    ('Think harder, Challenge and the Open investigation are for early finishers, home, or children on the fast track.', 'Think harder, Go further and the Investigation are in every workbook: choose them any time.'),
    ('Think harder, Challenge and the Open investigation are for early finishers or home.', 'Think harder, Go further and the Investigation are in every workbook: choose them any time.'),
    (' (minutes 7 to 10 are the Warm-up check, which decides who starts the worksheet on the Think harder page)', ' (game 0 to 5, quick questions 5 to 7, sneak-peek puzzles 7 to 10)'),
    ('then a one-minute look-back (What was hard?) 88 to 90', 'then a two-minute look-back 88 to 90'),
    ('the 3-minute Warm-up check follows on the next slide', 'the 3-minute sneak-peek puzzles follow on the next slide'),
    ('A quick game, quick questions and a 3-minute Warm-up check', 'A quick game, quick questions and 3 minutes of sneak-peek puzzles'),
    ('One question, then a stamp, then a one-minute look-back: what was hard?', 'One question, then a stamp, then a two-minute look-back (you can pass)'),
    ('Optional teaching for early finishers, before', 'Optional teaching for any pair that chooses Think harder, before'),
    ('(Stretch and Challenge)', '(Think harder and Go further)'),
    ('The stretch asks the same question', 'The Think harder slide asks the same question'),
    ('Pairs talk for 2 minutes, then share. Praise the reasons, not only the answers.', 'Pairs talk for 2 minutes. Then ask for volunteers first ("Who would like to share?"), never call a child by name to answer, and say that passing is always fine. No tallies and no rankings. Praise the reasons, not only the answers.'),
    ('Sentence starters:', 'Sentence starters (you can always pass):'),
    ('Online: type your fruit in the chat.', 'Online: when the tutor points to a fruit, give a thumbs up. No typing needed.'),
    ('(online: type it in chat)', '(online: a thumbs up when the tutor points to a fruit)'),
    ('Use as few as you can.', 'How few can we use together?'),
    ('as few questions as they can', 'as few questions as they can together'),
    ('Your pair gets ONE card for 10 minutes. Then swap cards with another pair for 4 minutes.', 'Your pair chooses ONE card for 10 minutes. Then you may swap with another pair for 4 minutes.'),
    ('Your pair gets ONE card for 10 minutes. Then swap with another pair for 4 minutes.', 'Your pair chooses ONE card for 10 minutes. Then you may swap with another pair for 4 minutes.'),
    ('Online: one card per breakout room; each pair reports back in 30 seconds.', 'Online: each pair chooses a card from the workbook page. Reporting back is optional: say one thing you tried, not the answer.'),
    ('online, one card per breakout room', 'online, each pair chooses a card'),
    ('Each pair reports back in 30 seconds.', 'Reporting back is optional: one thing you tried, not the answer.'),
    ('Keep report-backs to 30 seconds each; shorten them if time is tight.', 'Report-backs are optional and short: one thing you tried, not the answer. Ask for volunteers.'),
    ('Mental maths relay. The tutor asks a quick question from each lesson and passes it round the group.', 'Whiteboard round. The tutor asks a quick question from each lesson. Everybody writes the answer at the same time. No passing round and nobody on the spot.'),
    ('Mental maths relay: a chain of quick questions from all 9 lessons passed around the group.', 'Whiteboard round: quick questions from the 9 lessons. Everybody writes the answer at the same time. No passing round, nobody on the spot.'),
    # ---- re-audit fix pass: no boards or paper held up in front of the group or to the camera (private-paper rule); no "Challenge" label ----
    ('Children write on whiteboards and say the answer together on three.', 'Children write on their own paper or whiteboard. Nobody holds a board or paper up in front of the group or to the camera: face to face, each child keeps the paper low so only the tutor sees it; online, children say answers together on three or use fingers.'),
    ('Write it, say the answer together on three, then click.', 'Children write on their own paper and say the answer together on three (online: nothing is held up to the camera). Never ask for boards or paper held up in front of the group or to the camera. Then click.'),
    ('Children write the answer on whiteboards, then click.', 'Children write the answer on their own paper and say it together on three, then click.'),
    ('Whiteboards, then click.', 'Own paper; say the answer together on three, then click.'),
    ('Whiteboards again.', 'Own paper again, ticked against the answer slide.'),
    ('Whiteboards. ', 'Own paper, ticked against the answer slide. '),
    ('Whiteboard round.', 'Whiteboard round (boards stay low or on the desk; nobody holds a board or paper up in front of the group or to the camera).'),
    ('take answers on whiteboards, then click', 'take answers on each child\'s own paper (ticked against the answer slide), then click'),
    ('Your turn: whiteboards, then click.', 'Your turn: write it on your own paper, then click.'),
    ('Your turn: whiteboards', 'Your turn: write it'),
    ('Your turn: children count on whiteboards, then click', 'Your turn: children count on their own paper (ticked against the answer slide), then click'),
    ('Then whiteboards for the &quot;your turn&quot; and click for 7.', 'Then children write the &quot;your turn&quot; answer on their own paper (ticked against the answer slide) and click for 7.'),
    ('after children try it on whiteboards.', 'after children try it on their own paper (ticked against the answer slide).'),
    ('Draw it on your whiteboard.', 'Draw it on your own paper.'),
    ('Draw a grid on your whiteboard.', 'Draw a grid on your own paper.'),
    ('Ask a child to show the part that sticks out on their bars for a.', 'Ask for a volunteer (never a named child) to show the part that sticks out on their bars for a, or show it yourself.'),
    ('Ask a child who got b right to explain the order out loud.', 'Ask for a volunteer to explain the order out loud (never pick a named child).'),
    ('Answers are in the Challenge slide notes', 'Answers are in the Go further slide notes'),
    ('Show after pairs have tried the Challenge,', 'Show after pairs have tried Go further,'),
    ('Note who needs a short catch-up next lesson.', 'Note who may need a short catch-up next lesson (never in front of the group).'),
]

WHATIF = {
    1: 'What if frog 3 jumps in 10s from 0? Which numbers do frog 1 (4s) and frog 3 both land on?',
    2: 'What if we use 12 counters? Make 12 with two colours in as many ways as you can. What do you notice?',
    3: 'What if one picture stood for 2 children? Draw the class vote again. What changes? What stays the same?',
    4: 'What if you build 10 triangles? Predict the number of sticks, then test your idea.',
    5: 'What if you add 5 and then take away 2 before you tell your partner the total? Can they still find your number?',
    6: 'What if we want 30¢ instead? How many ways can you find? How will you know you have them all?',
    7: 'What if you cut the paper square straight across the middle instead? What shapes do you get? Can you make a new shape from the pieces?',
    8: 'What if you make a new rule and sort again? Which things go in the middle now?',
    9: 'What if you measure the same book with a paper clip instead of cubes? Guess first: a bigger or a smaller number?',
    10: 'What if you change ONE thing on your card? What changes in the answer?',
}
WHATIF_NOTE = ' Go further (what-if) is on this slide from the start: any pair may choose it at any time, so nobody waits. The tutor does not choose who and does not announce it. Answers: '
WHATIF_ANS = {
    1: '20 and 40 (frog 1 lands on 4, 8, ... 48; frog 3 on 10, 20, 30, 40, 50).',
    2: '7 different pairs if 3 + 9 and 9 + 3 count as the same: 0 + 12, 1 + 11, 2 + 10, 3 + 9, 4 + 8, 5 + 7, 6 + 6. The first number goes up by 1 as the second goes down by 1.',
    3: 'Half as many pictures. The key must say 1 picture = 2 children. The winner and the total stay the same. A count that is odd needs half a picture.',
    4: '21 sticks (3, 5, 7, ... add 2 each time).',
    5: 'Yes: add 5 and take away 2 is the same as add 3, so undo it with take away 3. Open: accept any reasoning that undoes both steps.',
    6: '6 ways: 20+10; 20+5+5; 10+10+10; 10+10+5+5; 10+5+5+5+5; six 5¢. Start with the biggest coin and work down.',
    7: 'Two equal rectangles. Put together they can make the square again, a long rectangle or a step shape. Open: accept any correct shape and name.',
    8: 'Open. Check the child can say the two rules and why the middle things follow both.',
    9: 'A bigger number (a shorter unit needs more of them). Open: accept any measured numbers if the shorter unit has the bigger count.',
    10: 'Open. Check the new puzzle can be solved and the child links the change to the new answer.',
}


def _p(D, sid): return os.path.join(D, 'slides', sid + '.html')
def _r(D, sid):
    f = _p(D, sid); return open(f).read() if os.path.exists(f) else None
def _w(D, sid, s): open(_p(D, sid), 'w').write(s)


def pill(D, sid, label, dark=False):
    """Add a minute label to a slide that has none."""
    s = _r(D, sid)
    if s is None or label in s: return
    if dark:
        tag = f'<p style="position:absolute;right:128px;top:64px;font-size:28px;font-weight:700;letter-spacing:2px;color:#FFC93C">{label}</p>\n'
    else:
        tag = f'<p style="position:absolute;right:128px;top:52px;font-size:26px;font-weight:800;letter-spacing:2px;color:#1F7A6F;background:#FFFFFF;border:2px solid #1F7A6F;border-radius:999px;padding:6px 22px">{label}</p>\n'
    # insert after the decoration (if any), before the first heading or paragraph
    m = re.search(r'<(h1|h2|p)\b', s[s.index('>', s.index('<section')):])
    i = s.index('>', s.index('<section')) + 1
    # skip leading deco divs
    j = i
    while True:
        k = s.find('<', j)
        if s.startswith('<div data-deco', k) or (s.startswith('<div style="position:absolute;left:0;top:0;width:1920px', k)):
            e = s.index('</div>', k)
            # nested svg inside bubbles: find the end of the outer div
            depth = 0; pos = k
            for mm in re.finditer(r'<div\b|</div>', s[k:]):
                depth += 1 if mm.group(0).startswith('<div') else -1
                if depth == 0: e = k + mm.end(); break
            j = e
            continue
        break
    s = s[:j] + '\n' + tag + s[j:]
    _w(D, sid, s)


def set_order(D, order_fix):
    dj = os.path.join(D, 'deck.json'); deck = json.load(open(dj)); o = deck['order']
    order_fix(o); json.dump(deck, open(dj, 'w'), indent=1, ensure_ascii=False)


def add_whatif(D, n):
    sid = 'l%d-explore1' % n; s = _r(D, sid)
    if s is None or 'Go further: your choice' in s: return
    inner = chip('Go further: your choice, any time', YEL, NAVY, 22) + p(WHATIF[n], 30, 600)
    cardh = card(inner, WHITE, CARD_X + 'margin-top:4px;padding:16px 30px;gap:8px')
    mark = '<p style="position:absolute;left:128px;bottom:64px'
    s = s.replace(mark, cardh + '\n' + mark, 1)
    s = s.replace('</aside>', WHATIF_NOTE + WHATIF_ANS[n] + '</aside>', 1)
    _w(D, sid, s)


def ws_note(D, n):
    sid = 'l%d-ws1' % n; s = _r(D, sid)
    if s is None or 'read questions 1 and 2 aloud' in s: return
    add = (' At minute 40 read questions 1 and 2 aloud, then pairs read the rest. The workbook says: "After question 3 you may choose: carry on, or try Think harder." '
           'Never announce who is on which page and never name a child in front of the group; invite the WHOLE group at once, for example: "When you have finished Start here, you can choose Think harder, Go further or the Investigation." Do not split a pair unless both children agree.')
    s = s.replace('</aside>', add + '</aside>', 1); _w(D, sid, s)


def talk_fix(D, n):
    sid = 'l%d-talk' % n; s = _r(D, sid)
    if s is None: return
    if 'passing is always fine' not in s:
        s = s.replace('</aside>', ' Volunteers first: "Who would like to share? You can pass." Never call a child by name. No tallies and no rankings.</aside>', 1)
    _w(D, sid, s)


def apply(D, n):
    p_ = 'l%d-' % n
    # global wording
    p1fix.sub_all(D, SUBS)
    # slide titles
    for sid, old, new in ((p_ + 'stretch', '>Stretch</h2>', '>Think harder</h2>'), (p_ + 'challenge', '>Challenge</h2>', '>Go further</h2>'),
                          (p_ + 'chwalk', 'Challenge: talk it through', 'Go further: talk it through'), (p_ + 'chdiag', 'Challenge: see it', 'Go further: see it')):
        p1fix.patch(D, sid, [(old, new)], must=False)
    # warm-up check slide notes are rebuilt by p1gaps.build; make sure the h2 says sneak-peek
    # minute labels for slides that lack one
    pill(D, p_ + 'title', '0–2 MIN', dark=True)
    if n == 1:
        pill(D, 'routine', '0–2 MIN'); pill(D, 'rules', '0–2 MIN')
    pill(D, p_ + 'end', '90 MIN', dark=True)
    add_whatif(D, n); ws_note(D, n); talk_fix(D, n)
    globals()['fix_l%d' % n](D)
    reaudit(D, n)
    # replace stale 'Open investigation' wording
    p1fix.sub_all(D, [('Open investigation', 'Investigation')])


# ---------------------------------------------------------------- lesson-specific fixes
def fix_l1(D):
    p1fix.patch(D, 'l1-explore1', [('Make a number strip from 0 to 50.', 'Take your number strip (0 to 50). It is in your Inquirer Kit.')], must=False)
    p1fix.patch(D, 'l1-ws2', [('up to 50. Which numbers do both say?', 'up to 30. Which numbers do both say?')], must=False)
    p1fix.patch(D, 'l1-ws2ans', [('>10, 20, 30, 40, 50<', '>10, 20, 30<')], must=False)
    p1fix.patch(D, 'l1-ws2ans', [('Q4b: numbers we say', 'Q4b (up to 30 here; the 50 version is Think harder T4): numbers we say')], must=False)
    p1fix.patch(D, 'l1-chwalk', [], must=False)


def fix_l2(D):
    p1fix.patch(D, 'l2-ws2', [('Magic triangle. Think about which numbers go in the corners.', 'Magic triangle. Every corner counts in two sides: think about which numbers go in the corners.'),
                              ('Q6</span>  Two numbers.', 'Q6</span>  Two numbers (if you have time).')], must=False)
    # re-audit fix pass: the corners 1, 2, 3 are given in Q5 (Core approachable untaught); choosing the corners is part (b), if you have time
    p1fix.patch(D, 'l2-ws2', [('Magic triangle. Every corner counts in two sides: think about which numbers go in the corners.', 'Magic triangle. Sides of 9: the corners 1, 2, 3 are given, so find the numbers between them. (If you have time: sides of 10, you choose the corners.)')], must=False)
    p1fix.patch(D, 'l2-teachpage2', [('On the worksheet the target is 9: ask "Small sides... so which numbers should go in the corners?" but do not tell them.', 'On the worksheet the target is 9 and the corners 1, 2, 3 are given, so children only find the numbers between them. Part (b), if you have time, is sides of 10 with the corners to choose: ask "Small sides... so which numbers should go in the corners?" but do not tell them.')], must=False)
    p1fix.patch(D, 'l2-ws2ans', [('Q5: small sides need small corners, so 1, 2, 3 go in the corners for 9.', 'Q5: the corners 1, 2, 3 are given for 9 (small sides need small corners).')], must=False)


def fix_l3(D):
    pass


def fix_l4(D):
    p1fix.patch(D, 'l4-ws2', [('Q8</span>  Ben has 15 sticks. How many triangles can he make?', 'Q8</span>  If you have time: Ben has 15 sticks. How many triangles can he make?')], must=False)


def fix_l5(D):
    # one new idea at a time: bar pictures move ahead of page 1; only the queue idea is left before page 2
    def fx(o):
        for k in ('teachbar',):
            sid = 'l5-' + k
            if sid in o: o.remove(sid)
        o.insert(o.index('l5-teachm') + 1, 'l5-teachbar')
    set_order(D, fx)
    for sid, lab in (('l5-teachm', '40–42 MIN'), ('l5-teachbar', '42–44 MIN'), ('l5-ws1', '44–52 MIN'), ('l5-ws1ans', '52–54 MIN'), ('l5-teachq1', '54–56 MIN'), ('l5-teachq2', '56–58 MIN')):
        p1fix.relabel(D, sid, lab)
    p1fix.patch(D, 'l5-teachbar', [('Teach before worksheet page 2', 'Teach now, before page 1, so that minutes 54 to 58 only have the queue idea (bars are used again in Q3 on page 2)')], must=False)
    p1fix.patch(D, 'l5-ws1', [('For Q1c (two steps) check that pairs undo the last step first.', 'For Q1c (two steps) the workbook says "Try a number and check it", so pairs may guess and check with counters; then show undoing the last step first.')], must=False)
    p1fix.patch(D, 'l5-ws1', [('Number machines. Find the rule from every pair, then fill the gaps.', 'Number machines. Find the rule from every pair, then fill the gaps. (If you have time: OUT 30 means IN what?)')], must=False)
    p1fix.patch(D, 'l5-ws2', [('Marble puzzle. Draw a bar for each child.', 'Marble puzzle. Colour the boxes: one box for each marble. (Part d is if you have time.)')], must=False)


def fix_l6(D):
    # warm-up: three price tags in cents only
    tags = [('Eraser', '65¢', '50¢ + 10¢ + 5¢  (3 coins)'), ('Pencil', '80¢', '50¢ + 20¢ + 10¢  (3 coins)'), ('Sticker', '30¢', '20¢ + 10¢  (2 coins)')]
    body = h2('Warm-up: the Money Shop') + chip('Pay exactly with your coins. Any way that pays exactly is a good way.', TEAL, CREAM, 28)
    for i, (nm, pr, ans) in enumerate(tags):
        body += (f'<div style="display:flex;gap:24px;align-items:stretch"><div style="flex:1;background:{WHITE};border-radius:24px;padding:24px 34px;{CARD_X}"><p style="font-size:48px;font-weight:800">{E(nm)}  <span style="color:{TEAL}">{E(pr)}</span></p></div>'
                 f'<div data-build-in="pop" style="width:700px;flex:none;background:{YEL};border-radius:20px;padding:18px 26px;display:flex;align-items:center"><p style="font-size:36px;font-weight:800">{E(ans)}</p></div></div>')
    body += p('Then look for a way with fewer coins. Can you?', 36, 600, MUTED)
    notes = ('Minutes 0 to 5. Money Shop, cents only. Hand out play coins (5¢, 10¢, 20¢, 50¢). Point to one item at a time: "The pencil costs 80¢. Pay exactly with your coins." Any way that pays exactly is a good way. Then ask: "Can you find a way with fewer coins?" '
             'Do not ask who used the fewest. Click to show one way with the fewest coins: Eraser 65¢ = 50¢ + 10¢ + 5¢ (3 coins). Pencil 80¢ = 50¢ + 20¢ + 10¢ (3 coins). Sticker 30¢ = 20¢ + 10¢ (2 coins). Dollars are not needed today: they are on the Think harder page.')
    _w(D, 'l6-warm1', sec('l6-warm1', '0–5 MIN', body, notes))
    _w(D, 'l6-ws1', ws_preview('l6-ws1', '40–52 MIN', 'Worksheet page 1: with your partner',
        [('Q1', 'Ways to make 20¢. Fill in the table, biggest coin first. (You may not need every row.)'), ('Q2', 'All the ways to make 25¢. Start with the biggest coin. There are 4.')],
        'Use play coins on the table, then write the way down.',
        'Minutes 40 to 52. Read questions 1 and 2 aloud. Walk around. Ask "How do you know you have them all?" Check that pairs work in order. Q1 has only 4 ways, so row E stays empty: that is fine. Q2 is the worked example from the Mini-lesson (25¢, 4 ways).'))
    _w(D, 'l6-ws1ans', check_slide('l6-ws1ans', '52–54 MIN', 'Page 1: check together',
        [('Q1', '4 ways: 20 / 10+10 / 10+5+5 / 5+5+5+5.  Fewest: one 20¢.  Most: four 5¢.'), ('Q2', '4 ways: 20+5, 10+10+5, 10+5+5+5, five 5¢')],
        'Click after pairs explain. Q1c: "We started with the biggest coin and went one fewer each time until there were none." Q2: the same table as the worked example. Thirty cents (6 ways) is on the Think harder page (T4).'))
    _w(D, 'l6-ws2', ws_preview('l6-ws2', '58–68 MIN', 'Worksheet page 2: on your own',
        [('Q3', '85¢ with the fewest coins. (If you have time: a way with exactly 6 coins.)'), ('Q4', 'Can 35¢ be made with 2 coins? Explain.'), ('Q5–Q6', 'Count the money: how much does Ali have? How much does Mei have?')],
        'Want more? You may choose Think harder T1 in your workbook.',
        'Children work alone. Q5 and Q6 are short "count the money" items (Ali 20¢ + 10¢ + 5¢ = 35¢; Mei 20¢ + 20¢ + 5¢ = 45¢). Note who may need a short catch-up next lesson. Dollars are now on the Think harder page (T5), not on this page.'))
    _w(D, 'l6-ws2ans', check_slide('l6-ws2ans', '68–72 MIN', 'Page 2: check together',
        [('Q3', '4 coins: 50 + 20 + 10 + 5.  6 coins: e.g. 50 + 10 + 10 + 5 + 5 + 5'), ('Q4', 'No: two coins make 10, 15, 20, 25, 30, 40, 55, 60, 70 or 100'), ('Q5, Q6', 'Q5: 35¢.   Q6: 45¢.')],
        'Click after a child explains. Q5: 20, 30, 35. Q6: 20 + 20 = 40, then 45. Think harder T3 (Sam): six 10¢ = 60¢; each swap to a 20¢ adds 10¢; 30¢ more means 3 swaps.'))
    p1fix.stretch_chip(D, 'l6-ws2ans')
    p1fix.relabel(D, 'l6-teachfew', '54–58 MIN')
    for sid in ('l6-teachnotes', 'l6-trynotes'): p1fix.relabel(D, sid, 'Optional, if you finish early')
    p1fix.patch(D, 'l6-teachnotes', [('Teach before worksheet page 2 (Q5 uses dollars).', 'Optional: dollars are now Think harder T5.')], must=False)
    p1fix.patch(D, 'l6-exit', [('Make 40¢ using exactly three coins from 5¢, 10¢, 20¢, 50¢.', 'Show one way to make 30¢ with 20¢, 10¢ and 5¢ coins.'),
                               ('Answer: 20¢ + 10¢ + 10¢.', 'Answer: any correct way, for example 20¢ + 10¢, or 10¢ + 10¢ + 10¢, or 20¢ + 5¢ + 5¢.')], must=False)


def fix_l7(D):
    body = h2('Exit ticket')
    inner = chip('EXIT TICKET', TEAL, CREAM, 28) + p('A shape has 6 sides. How many corners does it have? What is the shape called?', 46, 600)
    body += card(inner, WHITE, CARD_X) + card(p('Write your answer on a slip of paper. Tick it when your tutor shows the answer. Then collect your stamp in your inquiry journal.', 34, 500), WHITE, CARD_X)
    notes = ('Minutes 80 to 88. Answer: 6 corners; it is a hexagon (the same number of corners as sides). This replaces the 14-squares grid, which is a hard ending for the lesson. '
             'Extension: how many squares are in a 3 by 3 grid? (14: 9 + 4 + 1).')
    _w(D, 'l7-exit', sec('l7-exit', '80–88 MIN', body, notes))


def fix_l8(D):
    _w(D, 'l8-ws2', ws_preview('l8-ws2', '58–68 MIN', 'Worksheet page 2: on your own',
        [('Q3', 'Pets grid. Each child has a different pet. Two boxes are crossed for you (Clue 1). Tick where it fits, cross where it cannot.'), ('Q4', 'Line-up. Draw 4 circles. Put in the sure ones first.'),
         ('Q5', 'If you have time: a number riddle.'), ('Q6', 'If you have time: odd one out. Find a reason, then a second reason.')],
        'Want more? You may choose Think harder T1 in your workbook.',
        'Children work alone. Q3 says each child has a DIFFERENT pet: read that sentence aloud before they start; the two crosses for Clue 1 are printed. In Q4, "in front of" means somewhere in front, not always right in front. Q5 and Q6 are "if you have time"; the other two riddles are on Think harder T5. Note who may need a short catch-up next lesson.'))
    _w(D, 'l8-ws2ans', check_slide('l8-ws2ans', '68–72 MIN', 'Page 2: check together',
        [('Q3', 'Ali: fish.    Mei: cat.    Ben: dog.'), ('Q4', '1st Mei,   2nd Ali,   3rd Ben,   4th Sam'), ('Q5', 'a) 15   (Think harder T5: 30 and 14)'), ('Q6', '11: we do not say it counting in 3s.  Or 6: the only even number.')],
        'Click each answer after a child explains. Q3: Ali has no cat and no dog, so fish. Mei has no dog, and the fish is taken, so cat. Ben has the dog. Q4: Mei is 1st; Ali is in front of Ben and Ben is in front of Sam, so the order of the last three is Ali, Ben, Sam. Q5a: between 10 and 20, odd, in the 5s: 15. Think harder T5: a) 30 (20 and 40 are not between 20 and 40); b) 14 (1 + 4 = 5, less than 20). Q6: also accept "11 is the only number with 2 digits".'))
    p1fix.stretch_chip(D, 'l8-ws2ans')
    


def fix_l9(D):
    p1fix.patch(D, 'l9-ws1', [('Find the difference between your guess and the measure.', 'Write how far off your guess was.'),
                              ('The "difference" column is the gap between guess and measure', 'The "How far off my guess was" column is the gap between guess and measure')], must=False)
    p1fix.patch(D, 'l9-ws2', [('Q4</span>  Clips and erasers', 'Q4</span>  If you have time: clips and erasers'),
                              ('Use your ruler: a pencil from 0 to 12 cm, a crayon from 3 to 8 cm', 'Use the ruler picture (or your ruler): a pencil from 0 to 12 cm, a crayon from 3 to 8 cm')], must=False)
    p1fix.patch(D, 'l9-ws2', [('Q3</span>  Hand spans. Measure the desk with big paper clips, then small cubes: which needs fewer?', 'Q3</span>  Hand spans. Measure one line with paper clips, then with cubes: which unit gives the bigger number?')], must=False)


def fix_l10(D):
    body = h2('Warm-up: Puzzle Day') + chip('Whiteboard round: everybody writes at the same time. No passing round.', TEAL, CREAM, 28)
    body += card(p('Quick questions from our nine lessons.', 44, 700) + p('Write your answer on a whiteboard or paper. Not sure? Guess or draw it.', 36, 600, MUTED), WHITE, CARD_X)
    qs = [('Count in 5s: 5, 10, 15, __', '20'), ('10 = 4 + __', '6'), ('Pay 15¢ with two coins', '10¢ + 5¢'), ('What shape has 3 sides?', 'Triangle'), ('I think of a number, add 2 and get 9. My number?', '7')]
    inner = ''.join(f'<div style="display:flex;gap:20px;align-items:center"><p style="font-size:36px;font-weight:600;flex:1">{E(a)}</p><div data-build-in="pop" style="background:{YEL};border-radius:16px;padding:8px 22px"><p style="font-size:34px;font-weight:800">{E(b)}</p></div></div>' for a, b in qs)
    body += card(inner, WHITE, CARD_X)
    notes = ('Minutes 0 to 5. Whiteboard round. Say: "Everybody writes the answer at the same time. There is no passing round and nobody is put on the spot. If you are not sure, write a guess or draw it." '
             'Ask one question at a time, give thinking time, then click to show the answer to everyone. If answers differ, say "Different ideas are a good thing to talk about." Never groan at a wrong answer. Answers: 20; 6; 10¢ + 5¢ (or 5¢ + 5¢ + 5¢ is three coins); triangle; 7.')
    _w(D, 'l10-warm1', sec('l10-warm1', '0–5 MIN', body, notes))
    p1fix.sub_all(D, [('Pairs get ONE card for 10 minutes', 'Each pair chooses ONE card for 10 minutes')])


def reaudit(D, n):
    """Re-audit fix pass: Core items approachable untaught (tips, pictures, starters); slide text matches the workbook."""
    if n == 6:
        p1fix.patch(D, 'l6-ws2', [('85¢ with the fewest coins. (If you have time: a way with exactly 6 coins.)', '85¢ with the fewest coins. Use play coins: pay 85¢ any way you can, then try fewer coins. (If you have time: a way with exactly 6 coins.)')], must=False)
    if n == 9:
        p1fix.patch(D, 'l9-ws2', [('Hand spans. Measure one line with paper clips, then with cubes: which unit gives the bigger number?', 'Hand spans. Look at the picture of two bars: Ali 6 spans, Mei 8 spans for the same desk. Whose hand span is longer? How do you know?'),
                                   ('If you have time: clips and erasers, both ways. Draw the bars and count in groups.', 'If you have time: clips and erasers, both ways (1 clip = 2 erasers). Draw it or count in 2s.')], must=False)
    if n == 10:
        p1fix.patch(D, 'l10-ws2', [('Mystery number. Draw the machine and go backwards.', 'Mystery number (if you have time). Try a number and check it, or draw the machine and go backwards.')], must=False)
    if n == 7:
        for sid in ('l7-challenge', 'l7-chwalk'):
            p1fix.patch(D, sid, [('(add 2, 3, 4, 5, 6 each time)', '(the number added grows by 1 each time: +3, +4, +5, +6)')], must=False)
