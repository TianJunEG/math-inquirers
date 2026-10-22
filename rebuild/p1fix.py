"""Helpers used only by the Primary 1 generators (gen_l1.py .. gen_l10.py) for the P1 audit fixes.

Everything here is idempotent: running a generator twice gives the same slides.
Run order in a generator: write the generated slides, then call finish(D, n, times, ...).
"""
import os, re, glob

LAB = re.compile(r'(position:absolute;right:128px;top:\d+px;[^">]*letter-spacing:2px;[^>]*>)([^<]*)(</p>)')
OPTIONAL = 'Your choice'
FINISHED_OLD = 'Finished early? Stretch and Challenge come next.'
FINISHED_NEW = 'Want more? You may choose Think harder T1 in your workbook.'
CHIP_MARK = 'Stand up and stretch'


def _path(D, sid):
    return os.path.join(D, 'slides', sid + '.html')


def _read(D, sid):
    f = _path(D, sid)
    return open(f).read() if os.path.exists(f) else None


def _write(D, sid, s):
    open(_path(D, sid), 'w').write(s)


def relabel(D, sid, label):
    """Set the clock label (top right pill) of a slide; also fix 'Minutes A to B' in its speaker notes."""
    s = _read(D, sid)
    if s is None:
        print('p1fix: missing slide', sid); return
    m = LAB.search(s)
    if not m:
        print('p1fix: no time pill on', sid); return
    s = s[:m.start(2)] + label + s[m.end(2):]
    mm = re.match(r'(\d+)–(\d+) MIN$', label)
    if mm and '<aside>' in s:
        head, tail = s.split('<aside>', 1)
        tail = re.sub(r'Minutes \d+ to \d+', 'Minutes %s to %s' % (mm.group(1), mm.group(2)), tail, count=1)
        s = head + '<aside>' + tail
    _write(D, sid, s)


def patch(D, sid, pairs, must=True):
    """Replace text in one slide. A pair whose new text is already present is skipped (idempotent)."""
    s = _read(D, sid)
    if s is None:
        print('p1fix: missing slide', sid); return
    for old, new in pairs:
        if old in s:
            s = s.replace(old, new)
        elif new not in s and must:
            print('p1fix: text not found in', sid, ':', old[:70])
    _write(D, sid, s)


def sub_all(D, pairs):
    """Replace text in every slide of the deck (pairs that are not present are ignored)."""
    for f in glob.glob(os.path.join(D, 'slides', '*.html')):
        s = open(f).read(); t = s
        for old, new in pairs:
            t = t.replace(old, new)
        if t != s:
            open(f, 'w').write(t)


def stretch_chip(D, sid):
    """Add the 'stand up and stretch' reminder (audit 27) to a check-together slide."""
    s = _read(D, sid)
    if s is None or CHIP_MARK in s:
        return
    chip = ('<p style="position:absolute;right:128px;bottom:52px;font-size:26px;font-weight:800;color:#1B2A49;background:#FFC93C;'
            'border-radius:999px;padding:8px 24px">Stand up and stretch first!</p>\n')
    mark = '<p style="position:absolute;left:128px;bottom:64px'
    if mark in s:
        s = s.replace(mark, chip + mark, 1)
    note = ' First, everyone stands up and stretches for about a minute (reach up high, touch your toes, shake out your hands) so there is some movement before talk time.'
    s = s.replace('</aside>', note + '</aside>', 1)
    _write(D, sid, s)


def finish(D, n, times, optional=('stretch', 'challenge', 'chdiag', 'chwalk')):
    """Apply the shared P1 timing scheme to deck l<n>.

    times: {slide id: 'A–B MIN' or any label} for the slides whose clock label changes in this lesson.
    Shared rules (audit issues 8, 9, 27, 28):
      - page-2 check-together slide is 68–72, talk time is 72–80, exit ticket stays 80–90
      - stretch / challenge slides have no clock time ('Optional: if you finish early')
      - the 'finished early' tip points to Think Harder T1
      - the check-together slide for page 2 carries a stand-up-and-stretch reminder
      - the title slide's time plan matches
    """
    p = 'l%d-' % n
    for sid, label in times.items():
        relabel(D, sid, label)
    relabel(D, p + 'ws2ans', '68–72 MIN')
    relabel(D, p + 'talk', '72–80 MIN')
    for k in optional:
        relabel(D, p + k, OPTIONAL)
    stretch_chip(D, p + 'ws2ans')
    sub_all(D, [(FINISHED_OLD, FINISHED_NEW)])
    t = _read(D, p + 'title')
    if t is not None:
        t2 = re.sub(r'worksheet 40 to 70( with [^.]*?)?, talk time 70 to 80, exit ticket 80 to 90\.',
                    lambda m: 'worksheet 40 to 72%s (the last 4 minutes check page 2, after a 1-minute stand-up stretch), talk time 72 to 80, exit ticket 80 to 90. Think harder, Go further and the Investigation are for every child to choose, any time or at home.' % (m.group(1) or ''), t)
        if t2 == t and 'worksheet 40 to 72' not in t:
            print('p1fix: title time plan not found in', p + 'title')
        _write(D, p + 'title', t2)
