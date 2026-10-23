"""Picture library: outline pictures made of closed regions on a 180 x 200 mm canvas.
A picture says nothing about questions; any picture can take any topic bank.
Add a picture: write a function that returns a Picture and decorate it with @picture (see README)."""
from dataclasses import dataclass, field
from shapely.geometry import Point, Polygon
from geom import *
import labelbox

@dataclass
class Region:
    id: str
    geom: object
    partner: str = None                    # mirror partner id (must be the same colour)

@dataclass
class Picture:
    id: str
    title: str
    regions: list
    decor: list = field(default_factory=list)        # (svg fragment, shapely geometry used as an obstacle for labels)
    groups: list = field(default_factory=list)       # (ids, sentence): regions that must share one colour
    subsets: list = field(default_factory=list)      # (ids, "the N scales"): a counted subset check, e.g. exactly 2 red scales
    symmetric: bool = False
    blurb: str = ""
    mirror_pairs: list = field(default_factory=list)

    def by_id(self): return {r.id: r for r in self.regions}
    def obstacles(self): return [g for _, g in self.decor if g is not None]
    def boxes(self, rid):
        return labelbox.find_boxes(self.by_id()[rid].geom, self.obstacles())

PICTURES = {}
def picture(fn):
    PICTURES[fn.__name__] = fn
    return fn

class Builder:
    def __init__(self, id, title, symmetric=False, blurb=""):
        self.pic = Picture(id, title, [], symmetric=symmetric, blurb=blurb)
    def add(self, rid, geom):
        self.pic.regions.append(Region(rid, clean(geom))); return self
    def pair(self, rid, geom_left, sentence=None):
        """left region and its mirror image on the right; both must be the same colour"""
        l, r = rid + "_l", rid + "_r"
        self.pic.regions.append(Region(l, clean(geom_left), r))
        self.pic.regions.append(Region(r, clean(mir(geom_left)), l))
        self.pic.mirror_pairs.append((l, r))
        return self
    def decor(self, svg, geom=None):
        self.pic.decor.append((svg, geom)); return self
    def group(self, ids, sentence): self.pic.groups.append((ids, sentence)); return self
    def subset(self, ids, template): self.pic.subsets.append((ids, template)); return self
    def done(self): return self.pic

# ---------------------------------------------------------------- rocket
@picture
def rocket():
    b = Builder("rocket", "Rocket", symmetric=True, blurb="rocket with fins, window, flame, planet and moon")
    body = R(36, 45, 144, 135)
    window = C(90, 90, 20)
    b.pair("nose", E(90, 45, 54, 45) & R(0, 0, AXIS, 45))
    b.pair("top", R(36, 45, AXIS, 70))
    b.pair("mid", R(36, 70, AXIS, 110) - window)
    b.add("window", window)
    b.pair("bot", R(36, 110, AXIS, 135))
    b.pair("fin", P((36, 92), (2, 126), (2, 168), (36, 140)))
    b.add("base", P((52, 135), (128, 135), (122, 152), (58, 152)))
    b.add("flame", P((58, 152), (122, 152), (90, 200)))
    b.add("planet", C(18.5, 34, 17))
    b.add("moon", C(161.5, 34, 17))
    return b.done()

# ---------------------------------------------------------------- fish (not symmetric)
@picture
def fish():
    b = Builder("fish", "Fish", blurb="a fish with six scales, a two-part tail, two fins, three bubbles and the sea floor")
    body = E(70, 106, 60, 46)
    scales = []
    for ci, (x0, x1) in enumerate([(10, 50), (50, 90), (90, 130)]):
        for ri, (y0, y1) in enumerate([(50, 106), (106, 160)]):
            rid = f"scale_{ci + 1}{'ab'[ri]}"; scales.append(rid)
            b.add(rid, body & R(x0, y0, x1, y1))
    b.add("tail_up", P((124, 106), (178, 56), (178, 106)) - body)
    b.add("tail_dn", P((124, 106), (178, 106), (178, 156)) - body)
    b.add("fin_top", P((26, 72), (120, 72), (102, 26), (44, 26)) - body)
    b.add("fin_bot", P((40, 140), (110, 140), (96, 180), (54, 180)) - body)
    b.add("bubble_1", C(20, 28, 17.5))
    b.add("bubble_2", C(122, 22, 17.5))
    b.add("bubble_3", C(160, 24, 17.5))
    for i, (x0, x1) in enumerate([(0, 60), (60, 120), (120, 180)]):
        b.add(f"sand_{i + 1}", R(x0, 183, x1, 200))
    b.decor('<circle cx="25" cy="82" r="3.2" fill="#000"/>', C(25, 82, 3.2))
    b.group(["tail_up", "tail_dn"], "the two parts of the tail")
    b.group(["fin_top", "fin_bot"], "the two fins")
    b.subset(scales, "The fish has {n} scales. Exactly {c} of them {are} {colour}.")
    return b.done()

# ---------------------------------------------------------------- house with tree (not symmetric)
@picture
def house():
    b = Builder("house", "House", blurb="a house with roof, windows and door, a big tree, sun, cloud and grass")
    b.add("sun", C(24, 22, 18.5))
    b.add("cloud", E(124, 22, 28, 15))
    roof = P((58, 30), (112, 96), (4, 96))
    b.add("roof_top", roof & R(0, 0, 180, 66))
    b.add("roof_l", roof & R(0, 66, 58, 96))
    b.add("roof_r", roof & R(58, 66, 180, 96))
    b.add("window_l", R(4, 96, 40, 136))
    b.add("wall_ll", R(4, 136, 40, 176))
    b.add("wall_mid", R(40, 96, 76, 126))
    b.add("door", R(40, 126, 76, 176))
    b.add("window_r", R(76, 96, 112, 136))
    b.add("wall_rr", R(76, 136, 112, 176))
    b.add("crown_top", C(148, 70, 29) & R(0, 0, 180, 70))
    b.add("crown_bot", C(148, 70, 29) & R(0, 70, 180, 200))
    b.add("trunk", R(131, 99, 165, 176))
    for i, (x0, x1) in enumerate([(0, 60), (60, 120), (120, 180)]):
        b.add(f"grass_{i + 1}", R(x0, 176, x1, 200))
    b.group(["roof_l", "roof_r"], "the two sides of the roof")
    b.group(["window_l", "window_r"], "the two windows")
    b.group(["crown_top", "crown_bot"], "the top and bottom of the tree top")
    b.subset(["wall_ll", "wall_mid", "wall_rr", "door", "window_l", "window_r"], "The house has {n} wall and window parts. Exactly {c} {are} {colour}.")
    b.decor('<circle cx="69" cy="152" r="2.2" fill="#000"/>', C(69, 152, 2.2))
    return b.done()

# ---------------------------------------------------------------- butterfly (symmetric)
@picture
def butterfly():
    b = Builder("butterfly", "Butterfly", symmetric=True, blurb="butterfly with four-part wings and a body with feelers")
    up = smooth([(86, 90), (84, 50), (70, 20), (40, 6), (12, 14), (3, 42), (14, 76), (42, 96), (72, 98)])
    lo = smooth([(86, 96), (60, 100), (32, 110), (16, 134), (20, 168), (46, 188), (72, 178), (86, 146)])
    lo = lo - up
    b.pair("up_tip", up & R(0, 0, 46, 54))
    b.pair("up_in", up & R(46, 0, 90, 54))
    b.pair("up_out", up & R(0, 54, 46, 120))
    b.pair("up_low", up & R(46, 54, 90, 120))
    b.pair("lo_1", lo & R(0, 0, 90, 130))
    b.pair("lo_2", lo & R(0, 130, 90, 160))
    b.pair("lo_3", lo & R(0, 160, 90, 200))
    body = E(90, 100, 3.6, 62)
    b.decor('<ellipse cx="90" cy="100" rx="3.6" ry="62" fill="#000"/><circle cx="90" cy="32" r="5.5" fill="#000"/>'
            '<path d="M88,28 C84,14 80,8 72,4 M92,28 C96,14 100,8 108,4" fill="none" stroke="#000" stroke-width="0.9" stroke-linecap="round"/>', body)
    return b.done()

# ---------------------------------------------------------------- ice-cream cone (symmetric)
@picture
def icecream():
    b = Builder("icecream", "Ice Cream", symmetric=True, blurb="two scoops on a cone with a cherry, two diamonds and two circles")
    cherry = C(90, 20, 17.5)
    cone = P((31, 142), (149, 142), (90, 199))
    s1 = E(90, 70, 44, 33) - cherry
    s2 = E(90, 114, 64, 30) - E(90, 70, 44, 33) - cone
    b.add("cherry", cherry)
    b.pair("scoop1", s1 & R(0, 0, AXIS, 200))
    b.pair("scoop2", s2 & R(0, 0, AXIS, 200))
    b.pair("cone_a", cone & R(0, 0, AXIS, 168))
    b.add("cone_b", cone & R(0, 168, 180, 200))
    b.pair("diamond", P((26, 12), (51, 34), (26, 56), (1, 34)))
    b.pair("ball", C(26, 172, 20))
    return b.done()

# ---------------------------------------------------------------- owl (symmetric)
@picture
def owl():
    b = Builder("owl", "Owl", symmetric=True, blurb="owl with ear tufts, big eyes, beak, wings, tummy and a branch")
    head = E(90, 80, 66, 42)
    tuft = P((16, 62), (30, 6), (80, 40))
    eye = C(50, 82, 21)
    beak = P((90, 84), (116, 106), (90, 130), (64, 106))
    body = E(90, 140, 66, 44)
    branch = R(0, 178, 180, 200)
    b.pair("tuft", tuft)
    b.pair("eye", eye)
    b.add("beak", beak)
    headhalf = (head & R(0, 0, AXIS, 200))
    b.pair("head", headhalf - eye - tuft - beak - mir(tuft))
    b.pair("wing", (body - head - branch - beak) & R(0, 0, 64, 200))
    belly = (body - head - branch - beak) & R(64, 0, 116, 200)
    b.add("belly_1", belly & R(0, 0, 200, 150))
    b.add("belly_2", belly & R(0, 150, 200, 200))
    b.pair("branch", R(0, 178, 60, 200))
    b.add("branch_m", R(60, 178, 120, 200))
    return b.done()

# ---------------------------------------------------------------- sailboat (not symmetric)
@picture
def sailboat():
    b = Builder("sailboat", "Sailboat", blurb="sailboat with two sails, a jib, a hull, sun, clouds, waves and a hill")
    b.add("sun", C(24, 24, 18.5))
    b.add("cloud_1", E(152, 20, 24, 13))
    b.add("cloud_2", E(22, 62, 20, 12))
    b.add("sail_a", P((52, 20), (98, 20), (98, 72), (44, 72)))
    b.add("sail_b", P((44, 72), (98, 72), (98, 126), (28, 126)))
    jib = P((106, 24), (106, 126), (172, 126))
    b.add("jib_top", jib & R(0, 0, 200, 90))
    b.add("jib_bot", jib & R(0, 90, 200, 200))
    hull = P((6, 130), (172, 130), (150, 170), (28, 170))
    for i, (x0, x1) in enumerate([(0, 62), (62, 118), (118, 180)]):
        b.add(f"hull_{i + 1}", hull & R(x0, 0, x1, 200))
    water = R(0, 150, 180, 200) - hull
    b.add("wave_1", water & R(0, 0, 64, 200))
    b.add("wave_2", water & R(64, 0, 122, 200))
    b.add("wave_3", water & R(122, 0, 180, 200))
    b.decor('<path d="M100,6 L100,130" stroke="#000" stroke-width="0.9" fill="none"/><path d="M100,6 L122,13 L100,20 Z" fill="#000"/>', None)
    b.group(["hull_1", "hull_2", "hull_3"], "the three parts of the boat")
    b.subset(["sail_a", "sail_b", "jib_top", "jib_bot"], "The boat has {n} sails. Exactly {c} {are} {colour}.")
    return b.done()
