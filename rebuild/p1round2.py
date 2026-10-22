"""P1 round-2 fixes from the re-audit (docs/audit/reaudit/reaudit_p1.md).
Call apply(D, n) as the LAST step of gen_lK.py (after p1neutral.apply).  Idempotent: safe to run twice.
Every replacement is applied to the final slide HTML, so it works for generated and for static slides.
Each tuple is (old, new); both the plain and the HTML-escaped spelling of old are tried."""
import os, re, glob, html

# --- wording used for the Your-turn / whiteboard slides (no public boards) ---
WB = ('Children write on whiteboards or paper, and may show their tutor on camera or keep it to share if they want.')

ALL = [
    ('Children write on whiteboards and hold them up together.', WB),
    ('Whiteboards up together, then click.', WB + ' Then click.'),
    ('Whiteboards, then click.', WB + ' Then click.'),
    ('<aside>Whiteboards again.', '<aside>' + WB),
    ('<aside>Whiteboards.', '<aside>' + WB),
    ('After question 3 you may choose', 'When you finish this page you may choose'),
    ('(thumbs and chat)', '(thumbs up, no typing needed)'),
    ('There are no private chat messages. ', ''),
    ('; never a direct message)', ')'),
    ('my tutor will come and help', 'my tutor will look at this after class'),
]

PER = {
    2: [
        ('Each corner is on TWO sides: use the big numbers 4, 5, 6 in the corners.',
         'Each corner is on TWO sides. 12 is a big total, so big corners: 4, 5, 6.'),
        ('here the target is 12, so the BIG numbers go in the corners. On the worksheet the target is 9: ask "Small sides... so which numbers should go in the corners?" but do not tell them.',
         'here the total is 12, a big total, so the BIG numbers go in the corners. On the worksheet the totals are 9 and 10, which are small: ask "Small totals... so which numbers should go in the corners?" but do not tell them. The hint on the worksheet page says the same thing.'),
    ],
    3: [
        ('font-size="24" font-weight="700" fill="#1B2A49" text-anchor="end" font-family="Nunito Sans, Arial, sans-serif">Pear<',
         'font-size="20" font-weight="700" fill="#1B2A49" text-anchor="end" font-family="Nunito Sans, Arial, sans-serif">Watermelon<'),
    ],
    6: [
        ('(3) Stopping at the first set in Think harder T2 instead', '(3) Stopping at the first set in Think harder T1 instead'),
        ('before Think harder T2 (ALL the sets of 4 coins worth 70¢)', 'before Think harder T1 (ALL the sets of 4 coins worth 70¢)'),
        ('Think harder T3 (Sam)', 'Think harder T2 (Sam)'),
    ],
    7: [
        ('c) hexagon', 'c) triangle'),
    ],
    9: [
        ('a) 10 erasers   b) 6 clips', 'a) 18 erasers   b) 5 clips'),
        ('Q4a: 5 clips, each 2 erasers: 2, 4, 6, 8, 10. Q4b: 12 erasers in groups of 2: 2, 4, 6, 8, 10, 12 is 6 groups, so 6 clips.',
         'Q4a: 6 clips, each 3 erasers: 3, 6, 9, 12, 15, 18. Q4b: 15 erasers in groups of 3: 3, 6, 9, 12, 15 is 5 groups, so 5 clips.'),
        ('Q4: the worksheet says 1 clip = 2 erasers (not 3 as in our teaching), so check children use groups of 2.',
         'Q4: 1 clip = 3 erasers, as in the teaching, so check children count in groups of 3.'),
    ],
    10: [
        ('Q5b: counting only the 3 small triangles', 'Q5b: counting only the 2 small triangles'),
    ],
}


def _variants(s):
    out = [s, html.escape(s), html.escape(s, quote=False), s.replace('"', '&quot;')]
    seen = []
    for v in out:
        if v not in seen: seen.append(v)
    return seen


def _sub(text, old, new):
    for vo, vn in zip(_variants(old), _variants(new)):
        if vo in text:
            text = text.replace(vo, vn)
    return text


def apply(D, n):
    pairs = ALL + PER.get(n, [])
    for f in glob.glob(os.path.join(D, 'slides', '*.html')):
        s = open(f).read(); t = s
        for old, new in pairs:
            t = _sub(t, old, new)
        t = re.sub(r'(\bcan together)( together)+', r'\1', t)
        if t != s:
            open(f, 'w').write(t)
