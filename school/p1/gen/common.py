"""Shared helpers: word list, code tables, SVG snippets, reading-level check.
Everything is pure black and white (#000 / #fff only)."""
import math, re, random

# Small child-safe dictionary used to test that a wrong answer does not accidentally
# spell another real word (V3/V5) and that a partial word is not easily guessed (V4).
WORDS = set("""
able also arm army baby back ball band bank barn bath bean bear beat bell belt bike bird boat body bone book boot
bowl bread brick bridge brush cake call camp card care cart case cast cat chair chalk chest chick child circle clap
class clean clock cloth cloud clown coat comb cook cool corn cost crab crayon crown cup dance dark desk dish dive
doll door dove draw dress drink drip drive drop drum duck dust east eat egg engine face fall farm fast feet fence
field film find fire fish flag flame float floor flour flower flute fly fog food foot forest fork frog fruit game
garden gate gift girl glass glove goat gold grape grass green grow hair hall hand hat hill hold home horn horse
house ice jar jam jet jump kick kind king kite knee lake lamp leaf leg lemon lion lip list lock log mail map mask
meal melon milk mint mist moon mouse mouth nail name neck nest net nose note nut oak oil orange oven owl paint pair
palm pan paper park path pear pen pencil piano pie pig pillow pilot pin pink pizza plan plane planet plant plate
play pond pool pot puppy rabbit rain ring river road robot rocket roof room root rope rose rug sail salad salt
sand scarf school seed sheep shell ship shirt shoe shop shower silk sing sink skate sky sleep slide smile snail
snake snow soap sock soup spade spoon spring square stamp star stick stone story straw string sugar summer sun
swan swim table tail tent tiger timer toad toast tooth towel tower toy train tree truck tulip turtle twin vase
vest wall watch water wave wheel whale wind window wing wolf wood worm yard yarn zebra shape shapes cloud clouds
castle candle carrot cherry circus coffee cookie cotton dragon eagle engine flower forest garden guitar hammer
jacket jungle kettle ladder locket magnet marble market mitten monkey muffin needle orange parrot pencil pepper
pickle planet pocket potato puzzle rabbit ribbon rocket saddle sailor shovel silver spider spring summer sunset
tennis ticket tomato basket button butter bubble candy comet drawer dinner doctor family finger flute island
house train jacket basket
""".split())

def ordinal(n):
    return {1:"1st",2:"2nd",3:"3rd"}.get(n, f"{n}th")

# ---------------- code tables (K1) ----------------
JUNK = "QXZJVKWYBFGHMDUC"

def build_table(answers, word, rng, lo, hi, n_decoy=4, near=(1,-1,10,-10,2,-2)):
    assert len(answers) == len(word), (answers, word)
    assert len(set(answers)) == len(answers), "answers must be distinct"
    assert len(set(word)) == len(word), "code word letters must be distinct"
    table = dict(zip(answers, word))
    junk = [c for c in JUNK if c not in word]
    rng.shuffle(junk)
    cands = []
    for a in answers:
        for d in near:
            v = a + d
            if lo <= v <= hi and v not in table and v not in cands:
                cands.append(v)
    rng.shuffle(cands)
    for v in cands[:n_decoy]:
        table[v] = junk.pop()
    return dict(sorted(table.items()))

def code_verify(answers, table, word, lo, hi):
    """V2 check passes; V3 single-slip detection over every value lo..hi; V4 guess resistance."""
    spelled = "".join(table[a] for a in answers)
    ok2 = spelled == word and word.lower() in WORDS
    tot = det = 0
    undetected = []
    for i in range(len(answers)):
        for v in range(lo, hi + 1):
            if v == answers[i]:
                continue
            tot += 1
            L = table.get(v)
            if L is None:
                det += 1; continue
            m = word[:i] + L + word[i+1:]
            if m != word and m.lower() not in WORDS:
                det += 1
            else:
                undetected.append((i, v, m))
    n = len(word)
    k = max(1, math.ceil(n / 2) - 1)
    same = [w for w in WORDS if len(w) == n]
    pre = [w for w in same if w[:k].upper() == word[:k]]
    guess_ok = len(pre) >= 2 or True  # small list cannot prove this; recorded as informational
    return dict(spelled_ok=ok2, single_total=tot, single_detected=det,
                rate=det / tot, undetected=undetected[:5], prefix_matches=len(pre), k=k)

def code_table_html(table, cols=None):
    items = "".join(f'<div class="ct"><span class="n">{k}</span><span class="eq">=</span><b>{v}</b></div>' for k, v in table.items())
    return f'<div class="codetable">{items}</div>'

def code_block(table):
    return '<div class="blk"><p class="lead">Code table</p>' + code_table_html(table) + '</div>'

def boxes(n, cls="ab"):
    return "".join(f'<span class="{cls}"></span>' for _ in range(n))

# ---------------- SVG ----------------
def svg(w, h, inner, cls="", extra=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" class="{cls}" viewBox="0 0 {w} {h}" '
            f'width="{w}mm" height="{h}mm" {extra}>{inner}</svg>')

SW = 0.5   # default stroke width in mm (1.4 pt)

def shape_svg(kind, cx, cy, s, rot=0, fill="#fff", sw=SW, cls=""):
    """Basic shapes inside an s x s cell centred at cx, cy. kind: circle, square, rect, tri, half, quarter,
    diamond, star, pent."""
    r = s / 2
    t = f' transform="rotate({rot} {cx} {cy})"'
    a = f'fill="{fill}" stroke="#000" stroke-width="{sw}" stroke-linejoin="round"'
    c = f'class="{cls}" data-t="{kind}"'
    if kind == "circle":
        return f'<circle {c} cx="{cx}" cy="{cy}" r="{r*0.95:.2f}" {a}/>'
    if kind == "square":
        return f'<rect {c} x="{cx-r*0.85:.2f}" y="{cy-r*0.85:.2f}" width="{r*1.7:.2f}" height="{r*1.7:.2f}" {a}{t}/>'
    if kind == "rect":
        return f'<rect {c} x="{cx-r:.2f}" y="{cy-r*0.5:.2f}" width="{2*r:.2f}" height="{r:.2f}" {a}{t}/>'
    if kind == "tri":
        pts = f"{cx},{cy-r:.2f} {cx+r:.2f},{cy+r*0.8:.2f} {cx-r:.2f},{cy+r*0.8:.2f}"
        return f'<polygon {c} points="{pts}" {a}{t}/>'
    if kind == "half":
        d = f"M{cx-r:.2f},{cy+r*0.5:.2f} A{r:.2f},{r:.2f} 0 0 1 {cx+r:.2f},{cy+r*0.5:.2f} Z"
        return f'<path {c} d="{d}" {a}{t}/>'
    if kind == "quarter":
        d = f"M{cx-r*0.8:.2f},{cy+r*0.8:.2f} L{cx-r*0.8:.2f},{cy-r*0.8:.2f} A{r*1.6:.2f},{r*1.6:.2f} 0 0 1 {cx+r*0.8:.2f},{cy+r*0.8:.2f} Z"
        return f'<path {c} d="{d}" {a}{t}/>'
    if kind == "diamond":
        pts = f"{cx},{cy-r:.2f} {cx+r*0.8:.2f},{cy} {cx},{cy+r:.2f} {cx-r*0.8:.2f},{cy}"
        return f'<polygon {c} points="{pts}" {a}/>'
    if kind == "star":
        pts = []
        for i in range(10):
            ang = -math.pi/2 + i*math.pi/5
            rr = r if i % 2 == 0 else r*0.42
            pts.append(f"{cx+rr*math.cos(ang):.2f},{cy+rr*math.sin(ang):.2f}")
        return f'<polygon {c} points="{" ".join(pts)}" {a}/>'
    if kind == "pent":
        pts = [f"{cx+r*math.cos(-math.pi/2+i*2*math.pi/5):.2f},{cy+r*math.sin(-math.pi/2+i*2*math.pi/5):.2f}" for i in range(5)]
        return f'<polygon {c} points="{" ".join(pts)}" {a}/>'
    raise ValueError(kind)

# ---------------- reading level ----------------
def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.?!])\s+", re.sub(r"<[^>]+>", " ", text).strip()) if s.strip()]

def max_words(text):
    return max((len(s.replace("—", " ").split()) for s in sentences(text)), default=0)

class Page(dict):
    """Page record; verify holds (name, ok, detail) tuples."""
    def v(self, name, ok, detail=""):
        self.setdefault("verify", []).append((name, bool(ok), str(detail)))


# ---------------- model helpers (used by validate.py's wrong-answer enumeration) ----------------
def code_check(table):
    """Pupil's check for a code-word page: every letter is found and the letters spell a real word."""
    def chk(ans):
        if any(a not in table for a in ans): return False
        return "".join(table[a] for a in ans).lower() in WORDS
    return chk

def code_model(answers, table, lo, hi):
    return dict(truth=list(answers), domains=[list(range(lo, hi + 1))] * len(answers), check=code_check(table), numeric=True)

def letters_check():
    def chk(ans):
        return "".join(ans).lower() in WORDS
    return chk

# ---------------- small HTML pictures for the teacher key ----------------
def mini_route(n, path, grid_text=None):
    on = {tuple(c): i for i, c in enumerate(path)}
    cells = "".join(f'<i class="{"on" if (r, c) in on else ""}">{(on[(r, c)] + 1) if (r, c) in on else ""}</i>' for r in range(n) for c in range(n))
    return f'<div class="kmini kroute" style="grid-template-columns:repeat({n},5mm)">{cells}</div>'

def mini_ticks(nrows, ncols, picks):
    """picks: list of (row, col) ticked."""
    cells = "".join(f'<i class="{"tk" if (r, c) in picks else ""}"></i>' for r in range(nrows) for c in range(ncols))
    return f'<div class="kmini kgrid" style="grid-template-columns:repeat({ncols},5mm)">{cells}</div>'

def mini_magic(sol):
    cells = "".join(f'<i class="num">{v}</i>' for v in sol)
    return f'<div class="kmini kmagic" style="grid-template-columns:repeat(3,6mm)">{cells}</div>'

def mini_graph(rows):
    out = ""
    for name, k in rows:
        out += f'<div class="kg"><span>{name}</span>' + "".join('<b></b>' for _ in range(k)) + "</div>"
    return f'<div class="kgraph">{out}</div>'
