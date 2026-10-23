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
    twins: list = field(default_factory=list)        # (ids, symbol): regions that carry the same small black mark and must share one colour
    symmetric: bool = False
    blurb: str = ""
    mirror_pairs: list = field(default_factory=list)

    def by_id(self): return {r.id: r for r in self.regions}
    def obstacles(self): return [g for _, g in self.decor if g is not None]
    def boxes(self, rid):
        return labelbox.find_boxes(self.by_id()[rid].geom, self.obstacles())

# ---------------------------------------------------------------- twin marks
# A twin set is two to four regions that carry the same small solid-black mark and must be coloured alike. It is the second
# self-check of a picture that is not symmetric (and of the loose parts of a symmetric one): a pupil who swaps the colours of
# two parts breaks the match of both marks. Marks are placed by the library (never by hand) away from the label.
SYMBOLS = ["triangle", "square", "star", "cross", "circle", "moon"]      # P1 shape names only (no diamond or hexagon: not on the Primary 1 shape list)
def symbol_points(name, cx=0.0, cy=0.0, s=1.0):
    """polygon points of a mark of half-size s centred on (cx, cy)"""
    if name == "triangle": pts = [(0, -1.15), (-1.05, 0.8), (1.05, 0.8)]
    elif name == "square": pts = [(-0.85, -0.85), (0.85, -0.85), (0.85, 0.85), (-0.85, 0.85)]
    elif name == "circle":
        import math
        pts = [(1.05 * math.cos(i * math.pi / 8), 1.05 * math.sin(i * math.pi / 8)) for i in range(16)]
    elif name == "moon":
        from shapely.geometry import Point
        m = Point(0, 0).buffer(1.15, 24).difference(Point(0.6, 0).buffer(0.95, 24))
        pts = [(x - 0.2, y) for x, y in list(m.exterior.coords)[:-1]]
    elif name == "star":
        import math
        pts = [((1.2 if i % 2 == 0 else 0.5) * math.cos(-math.pi / 2 + i * math.pi / 5), (1.2 if i % 2 == 0 else 0.5) * math.sin(-math.pi / 2 + i * math.pi / 5)) for i in range(10)]
    elif name == "cross": pts = [(-0.38, -1.1), (0.38, -1.1), (0.38, -0.38), (1.1, -0.38), (1.1, 0.38), (0.38, 0.38), (0.38, 1.1), (-0.38, 1.1), (-0.38, 0.38), (-1.1, 0.38), (-1.1, -0.38), (-0.38, -0.38)]
    else: raise KeyError(name)
    return [(cx + x * s, cy + y * s) for x, y in pts]
def symbol_svg(name, cx, cy, s=1.9):
    return '<polygon points="%s" fill="#000"/>' % " ".join(f"{x:.2f},{y:.2f}" for x, y in symbol_points(name, cx, cy, s))

def place_marker(geom, obstacles, s=1.9):
    """a point inside `geom` for a mark of half-size s: clear of the outline, and where it takes the least room from the label boxes
    the region could hold (every box height counts, so tall pictures such as a clock still fit); ties go to the point nearest the outline"""
    import numpy as np
    from shapely.geometry import Point
    boxes = labelbox.find_boxes(geom, obstacles)
    pad = s * 1.25 + 0.4
    inner = geom.buffer(-(s * 1.25 + 1.6))
    if inner.is_empty: inner = geom.buffer(-(s * 1.25 + 0.6))
    minx, miny, maxx, maxy = inner.bounds
    cands = [(x, y) for x in np.arange(minx, maxx + 0.01, 1.0) for y in np.arange(miny, maxy + 0.01, 1.0) if inner.contains(Point(x, y))]
    for o in obstacles: cands = [c for c in cands if o.distance(Point(*c)) > s * 1.25 + 1.0]
    if not cands: raise ValueError("no room for a mark")
    def penalty(c):
        p = 0.0
        for cx, cy, w, h in boxes:
            if abs(c[0] - cx) < w / 2 + pad and abs(c[1] - cy) < h / 2 + pad: p += (h / 12.0) * (1.0 if h >= 12 else 0.5)
        return p
    return min(cands, key=lambda c: (round(penalty(c), 2), round(geom.boundary.distance(Point(*c)) / 2.0), -c[1]))

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
    def twin(self, ids):
        """the regions in `ids` get the same small mark and must be coloured alike"""
        self.pic.twins.append((list(ids), SYMBOLS[len(self.pic.twins)])); return self
    def done(self):
        pic = self.pic; by = pic.by_id()
        for ids, name in pic.twins:
            for rid in ids:
                obs = pic.obstacles()
                x, y = place_marker(by[rid].geom, obs)
                pic.decor.append((symbol_svg(name, x, y), Point(x, y).buffer(1.9 * 1.25)))
        return pic

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
    b.pair("planet", C(18.5, 34, 17))                 # planet and moon are mirror images of each other
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
    b.twin(["tail_up", "tail_dn"]).twin(["fin_top", "fin_bot"]).twin(["bubble_1", "bubble_2", "bubble_3"]).twin(["sand_1", "sand_2", "sand_3"])
    b.twin(["scale_1a", "scale_3b"]).twin(["scale_1b", "scale_3a"])
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
    b.twin(["roof_l", "roof_r"]).twin(["window_l", "window_r"]).twin(["crown_top", "crown_bot"]).twin(["grass_1", "grass_2", "grass_3"])
    b.twin(["wall_ll", "wall_mid", "wall_rr"]).twin(["sun", "cloud"])
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
    """a waffle cone (about 38% of the height, narrow, point down) under two round scoops that overlap a little (about 58%), with a wavy drip edge"""
    b = Builder("icecream", "Ice Cream", symmetric=True, blurb="a tall narrow cone under two round scoops with a drip edge, and four pairs of circles")
    sc1 = C(90, 42, 33)
    sc2 = C(90, 88, 35) | C(68, 120, 8.5) | C(90, 124, 9.5) | C(112, 120, 8.5)           # second scoop with three drips
    cone = P((56, 118), (124, 118), (90, 199)) - sc2 - sc1
    b.add("scoop1", sc1)
    b.pair("scoop2", ((sc2 - sc1) & R(0, 0, AXIS, 200)))
    b.add("cone_top", cone & R(0, 0, 180, 148))
    b.add("cone_bottom", cone & R(0, 148, 180, 200))
    for k, y in enumerate((24, 76, 128, 176)): b.pair("ball%d" % k, C(24, y, 20))
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
    b.twin(["belly_1", "belly_2"])
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
    b.twin(["hull_1", "hull_2", "hull_3"]).twin(["wave_1", "wave_3"]).twin(["cloud_1", "cloud_2"]).twin(["jib_top", "jib_bot"]).twin(["sail_a", "sail_b"])
    return b.done()

# ---------------------------------------------------------------- castle (symmetric)
@picture
def castle():
    b = Builder("castle", "Castle", symmetric=True, blurb="castle with two towers, a keep with a flag, double doors, clouds and a lawn")
    b.pair("cloud", E(24, 18, 22, 12))
    b.pair("tower_roof", P((0, 80), (52, 80), (26, 40)))
    b.pair("tower_a", R(0, 80, 52, 112))
    b.pair("tower_b", R(0, 112, 52, 144))
    b.pair("tower_c", R(0, 144, 52, 176))
    b.add("keep_roof", P((56, 80), (124, 80), (90, 32)))
    b.pair("keep_a", R(52, 80, AXIS, 112))
    b.add("keep_b", R(52, 112, 128, 140))
    b.pair("door", R(52, 140, AXIS, 176))
    b.add("lawn", R(0, 176, 180, 200))
    b.decor('<path d="M90,32 L90,10" stroke="#000" stroke-width="0.9" fill="none"/><path d="M90,10 L110,16 L90,22 Z" fill="#000"/>', R(88, 8, 112, 32))
    b.decor('<circle cx="84" cy="158" r="2.2" fill="#000"/><circle cx="96" cy="158" r="2.2" fill="#000"/>', C(84, 158, 2.2).union(C(96, 158, 2.2)))
    return b.done()

# ---------------------------------------------------------------- car (not symmetric)
@picture
def car():
    b = Builder("car", "Car", blurb="car with two windows, three body parts, two wheels, sun, clouds and a road")
    wheels = C(46, 146, 24).union(C(134, 146, 24))
    b.add("sun", C(24, 24, 18.5))
    b.add("cloud_1", E(84, 20, 24, 13))
    b.add("cloud_2", E(150, 24, 24, 13))
    b.add("window_1", P((46, 96), (91, 96), (91, 50), (68, 50)))
    b.add("window_2", P((91, 96), (138, 96), (116, 50), (91, 50)))
    body = R(8, 96, 172, 148) - wheels
    b.add("body_a", body & R(0, 0, 62, 200))
    b.add("body_b", body & R(62, 0, 118, 200))
    b.add("body_c", body & R(118, 0, 200, 200))
    b.add("wheel_1", C(46, 146, 24))
    b.add("wheel_2", C(134, 146, 24))
    for i, (x0, x1) in enumerate([(0, 60), (60, 120), (120, 180)]):
        b.add(f"road_{i + 1}", R(x0, 174, x1, 200) - wheels)
    b.twin(["wheel_1", "wheel_2"]).twin(["window_1", "window_2"]).twin(["cloud_1", "cloud_2"]).twin(["road_1", "road_2", "road_3"]).twin(["body_a", "body_c"])
    return b.done()

# ---------------------------------------------------------------- elephant, front view (symmetric)
@picture
def elephant():
    b = Builder("elephant", "Elephant", symmetric=True, blurb="elephant face with two big ears, a trunk, two eyes, clouds and ground")
    head = E(90, 80, 46, 50)
    trunk = P((68, 124), (112, 124), (106, 170), (74, 170))
    ear = E(26, 88, 26, 50) - head
    b.pair("ear", ear)
    b.pair("head_up", head & R(0, 0, AXIS, 62))
    b.pair("head_mid", head & R(0, 62, AXIS, 100))
    b.pair("head_low", (head & R(0, 100, AXIS, 200)) - trunk)
    b.add("trunk", trunk - head)
    b.pair("cloud", E(22, 16, 20, 11))
    b.pair("ground", R(0, 174, 60, 200))
    b.add("ground_m", R(60, 174, 120, 200))
    b.decor('<circle cx="70" cy="70" r="3" fill="#000"/><circle cx="110" cy="70" r="3" fill="#000"/>', None)
    return b.done()

# ---------------------------------------------------------------- dinosaur (not symmetric)
@picture
def dinosaur():
    b = Builder("dinosaur", "Dinosaur", blurb="long-necked dinosaur with a four-part body, two legs, a tail, sun, cloud and ground")
    body = E(96, 118, 52, 34)
    b.add("head", C(28, 38, 22))
    b.add("neck_up", P((4, 60), (52, 60), (58, 90), (12, 90)))
    b.add("neck_low", P((12, 90), (58, 90), (70, 118), (16, 118)) - body)
    b.add("body_ul", body & R(0, 0, 96, 118))
    b.add("body_ur", body & R(96, 0, 200, 118))
    b.add("body_ll", body & R(0, 118, 96, 200))
    b.add("body_lr", body & R(96, 118, 200, 200))
    b.add("tail", P((140, 110), (180, 90), (180, 160), (140, 150)) - body)
    b.add("leg_1", R(52, 100, 90, 178) - body)
    b.add("leg_2", R(102, 100, 140, 178) - body)
    for i, (x0, x1) in enumerate([(0, 60), (60, 120), (120, 180)]):
        b.add(f"ground_{i + 1}", R(x0, 180, x1, 200))
    b.add("sun", C(150, 28, 20))
    b.add("cloud", E(92, 26, 26, 14))
    b.decor('<circle cx="38" cy="28" r="2.8" fill="#000"/>', C(38, 28, 2.8))
    b.twin(["leg_1", "leg_2"]).twin(["neck_up", "neck_low"]).twin(["ground_1", "ground_2", "ground_3"]).twin(["body_ul", "body_lr"]).twin(["body_ur", "body_ll"]).twin(["sun", "cloud"])
    return b.done()

# ---------------------------------------------------------------- Primary 4 pictures: big parts, so that longer questions fit (added in the school/p4 copy)
@picture
def bus():
    b = Builder("bus", "Bus", blurb="bus with three roof parts, four windows, three body parts, two wheels, a sun and three strips of road")
    wheels = C(46, 150, 21).union(C(134, 150, 21))
    b.add("sun", C(24, 22, 19.5))
    for i, (x0, x1) in enumerate([(8, 62), (62, 118), (118, 172)]):
        b.add(f"roof_{i + 1}", R(x0, 44, x1, 66))
    for i, (x0, x1) in enumerate([(8, 52), (52, 90), (90, 130), (130, 172)]):
        b.add(f"window_{i + 1}", R(x0, 66, x1, 106))
    body = R(8, 106, 172, 150) - wheels
    for i, (x0, x1) in enumerate([(8, 62), (62, 118), (118, 172)]):
        b.add(f"body_{i + 1}", body & R(x0, 0, x1, 200))
    b.add("wheel_1", C(46, 150, 21)); b.add("wheel_2", C(134, 150, 21))
    for i, (x0, x1) in enumerate([(0, 60), (60, 120), (120, 180)]):
        b.add(f"road_{i + 1}", R(x0, 174, x1, 200) - wheels)
    b.twin(["wheel_1", "wheel_2", "sun"]).twin(["roof_1", "roof_3"]).twin(["window_1", "window_4", "roof_2"]).twin(["window_2", "window_3", "body_2"]).twin(["body_1", "body_3"]).twin(["road_1", "road_2", "road_3"])
    return b.done()

@picture
def lorry():
    b = Builder("lorry", "Lorry", blurb="lorry with a container of six parts, a cab with a window, three wheels, a sun and three strips of road")
    wheels = C(34, 152, 20).union(C(92, 152, 20)).union(C(150, 152, 20))
    b.add("sun", C(150, 24, 19.5))
    cont = R(6, 40, 124, 132)
    for j, (y0, y1) in enumerate([(40, 86), (86, 132)]):
        for i, (x0, x1) in enumerate([(6, 45), (45, 85), (85, 124)]):
            b.add(f"box_{j + 1}{i + 1}", R(x0, y0, x1, y1))
    b.add("cab_window", P((132, 62), (168, 62), (168, 88), (132, 88)))
    b.add("cab_body", (P((128, 54), (172, 54), (172, 132), (128, 132)) - P((132, 62), (168, 62), (168, 88), (132, 88))))
    b.add("wheel_1", C(34, 152, 20)); b.add("wheel_2", C(92, 152, 20)); b.add("wheel_3", C(150, 152, 20))
    for i, (x0, x1) in enumerate([(0, 60), (60, 120), (120, 180)]):
        b.add(f"road_{i + 1}", R(x0, 176, x1, 200) - wheels)
    b.twin(["wheel_1", "wheel_3", "sun"]).twin(["wheel_2", "cab_body"]).twin(["box_11", "box_23"]).twin(["box_13", "box_21"]).twin(["box_12", "box_22", "cab_window"]).twin(["road_1", "road_2", "road_3"])
    return b.done()

@picture
def ferry():
    b = Builder("ferry", "Ferry", blurb="ferry with a funnel, a bridge, two decks of windows, a hull in three parts, a sun and three waves")
    b.add("sun", C(24, 24, 19.5))
    b.add("funnel", R(70, 36, 110, 62))
    b.add("bridge", R(52, 62, 128, 92))
    for i, (x0, x1) in enumerate([(14, 62), (62, 118), (118, 166)]):
        b.add(f"deck_{i + 1}", R(x0, 92, x1, 124))
    hull = P((8, 124), (172, 124), (150, 160), (30, 160))
    for i, xr in enumerate([(0, 64), (64, 116), (116, 200)]):
        b.add(f"hull_{i + 1}", hull & R(xr[0], 0, xr[1], 200))
    for i, (y0, y1) in enumerate([(164, 178), (178, 190)]):
        pass
    for i, (x0, x1) in enumerate([(0, 60), (60, 120), (120, 180)]):
        b.add(f"wave_{i + 1}", R(x0, 164, x1, 200))
    b.twin(["sun", "funnel"]).twin(["bridge", "deck_2"]).twin(["deck_1", "deck_3"]).twin(["hull_1", "hull_3"]).twin(["hull_2", "wave_2"]).twin(["wave_1", "wave_3"])
    return b.done()
