"""Independent answer evaluator for the printed question text (Colour by Code).

verify.py does not trust a bank's own `holds` lambda or its `answer`: this module re-solves every question from what is
printed on the page, that is the text lines (the blank is the box character) plus, for questions that carry a picture, what
a reader would decode from that picture (art `meta`: clock hand angles, ruler ends, coin values, dots, graph rows, ...).

    solve(lines, meta=None, instr="", kind=None) -> (value, rule_name)       raises Unparsed when no rule understands the text
    matches(value, answer) -> bool

Value types: int (plain numbers; money in cents unless kind == "dollars"), (hour, minute) for times, (n, unit) for measures,
(numerator, denominator) for fractions (as written, not reduced).
Every question form of every bank must be understood by a rule here; a form that no rule understands fails verify.py,
so a new form needs a new rule (a regular expression on the joined text and a function). Nothing here imports a bank."""
import math, re
from fractions import Fraction

B = "□"                           # the blank box (qcore.BOX)
CENT = "¢"

class Unparsed(Exception): pass
NOT_ME = object()                       # a rule that matched the words but not the picture type returns this

# ------------------------------------------------------------------ helpers
def norm(lines):
    t = " ".join(lines).replace("⟦", "").replace("⟧", "")
    t = re.sub(r"⟨\s*([^|⟩]+?)\s*\|\s*([^⟩]+?)\s*⟩", r"\1/\2", t)      # stacked fraction  <a|b>  ->  a/b
    return re.sub(r"\s+", " ", t).strip()
def I(s): return int(s)
def ints(s): return [int(x) for x in re.findall(r"\d+", s)]
def hmin(h, m): return ((h - 1) % 12 + 1, m % 60)
def minutes_of(t): return (t[0] % 12) * 60 + t[1]
def add_minutes(t, d):
    tot = (minutes_of(t) + d) % 720
    return (tot // 60 or 12, tot % 60)
def exact_div(n, d): return n // d if d and n % d == 0 else None

ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENSW = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
def words_to_int(s):
    total = 0
    for w in re.split(r"[\s-]+", s.lower().replace(" and ", " ")):
        if w == "hundred": total *= 100
        elif w in ONES: total += ONES.index(w)
        elif w in TENSW: total += TENSW[w]
        elif w: raise Unparsed(s)
    return total

# ------------------------------------------------------------------ what a reader decodes from a picture
def read_clock(meta):
    m = round(meta["minute_angle"] / 6.0) % 60
    h = round((meta["hour_angle"] - m * 0.5) / 30.0) % 12 or 12
    return (h, m)
CORNERS = {"triangle": 3, "square": 4, "rectangle": 4, "circle": 0, "semicircle": 2, "quarter": 3}
SIDES = {"triangle": 3, "square": 4, "rectangle": 4, "circle": 0, "semicircle": 1, "quarter": 2}
FLAT = {"cube": 6, "cuboid": 6, "cylinder": 2, "cone": 1, "sphere": 0}
CURVED = {"cube": 0, "cuboid": 0, "cylinder": 1, "cone": 1, "sphere": 1}
def plural(w): return w[:-1] if w.endswith("s") else w

# ------------------------------------------------------------------ equations with a blank (numbers, money, units)
UNITS = "cm|m|kg|g|l|min"
def _factor(unit):
    return {"cm": 1, "m": 100, "g": 1, "kg": 1000, "l": 1, "min": 1}[unit]

def solve_equation(text):
    """'35c + $1.20 = BOX', '1 m - 95 cm = BOX cm', '4 x BOX = 20' ... -> (value, unit); unit is None, a measure unit,
    'money-cents' or 'money-dollars' (the value is then in the blank's own unit). The equation must be linear in the blank."""
    t = text.replace("−", "-").replace("×", "*").replace("÷", "/")
    if t.count("=") != 1: raise Unparsed(text)
    bm = re.search(r"(\$)?" + B + r"(" + CENT + r"| ?(?:" + UNITS + r")\b)?", t)
    if not bm: raise Unparsed(text)
    money = ("$" in t) or (CENT in t)
    if bm.group(1): bunit, bfac = "money-dollars", 100
    elif bm.group(2) and bm.group(2).strip() == CENT: bunit, bfac = "money-cents", 1
    elif bm.group(2): bunit = bm.group(2).strip(); bfac = _factor(bunit)
    elif money: bunit, bfac = "money-dollars", 100                         # a bare blank beside dollar amounts is in dollars
    else: bunit, bfac = None, 1
    def conv(m):
        s = m.group(0)
        if B in s: return "V"
        if s.startswith("$"): return 'F("%s")' % (Fraction(s[1:]) * 100)
        if s.endswith(CENT): return 'F("%s")' % s[:-1]
        um = re.fullmatch(r"(\d+(?:\.\d+)?)\s?(" + UNITS + ")", s)
        if um: return 'F("%s")' % (Fraction(um.group(1)) * _factor(um.group(2)))
        if bunit in ("cm", "m", "g", "kg", "l", "min") and "*" not in t and "/" not in t: return 'F("%s")' % (Fraction(s) * bfac)     # bare numbers are in the blank's unit
        return 'F("%s")' % s
    expr = re.sub(r"\$" + B + r"|" + B + r"(?:" + CENT + r"| ?(?:" + UNITS + r")\b)?|\$\d+(?:\.\d+)?|\d+(?:\.\d+)?\s?(?:" + UNITS + r")\b|\d+" + CENT + r"|\d+(?:\.\d+)?", conv, t)
    if not re.fullmatch(r'[V0-9F"+\-*/()=. ]*', expr): raise Unparsed(text)
    l, r = expr.split("=")
    def f(v):
        g = {"F": Fraction, "V": Fraction(v) * bfac, "__builtins__": {}}
        return eval(l, g) - eval(r, g)
    b0 = f(0); b1 = f(1) - b0
    if b1 == 0: raise Unparsed(text)
    return -b0 / b1, bunit

# ------------------------------------------------------------------ sequences
def solve_sequence(items, rule_step=None, rule_back=None):
    known = [(i, int(x)) for i, x in enumerate(items) if x != B]
    pos = [i for i, x in enumerate(items) if x == B]
    if len(pos) != 1 or len(known) < 2: raise Unparsed(str(items))
    (i0, v0), (i1, v1) = known[0], known[1]
    d = Fraction(v1 - v0, i1 - i0)
    if d.denominator != 1 or d == 0: return None
    for i, v in known:
        if v - v0 != d * (i - i0): return None
    if rule_step is not None and abs(d) != rule_step: return None
    if rule_back is not None and (d < 0) != rule_back: return None
    return int(v0 + d * (pos[0] - i0))
def split_list(s): return [x.strip() for x in s.split(",")]

# ------------------------------------------------------------------ rules (regular expression on the joined text -> function(match, ctx))
RULES = []
def R(pattern):
    rx = re.compile(pattern)
    def deco(fn): RULES.append((rx, fn)); return fn
    return deco
NUM = r"(?:\d+|" + B + ")"
LIST = r"(?:\d+|" + B + r")(?:, (?:\d+|" + B + r"))+"
MONEY = r"(\$\d+(?:\.\d\d)?|\d+" + CENT + ")"
def cents(tok): return int(Fraction(tok[1:]) * 100) if tok.startswith("$") else int(tok[:-1])
def meta_is(c, *kinds): return c["meta"] is not None and c["meta"].get("kind") in kinds

# ---- additive phrases
@R(r"(\d+) more than (\d+) is " + B)
def more_than(m, c): return I(m[1]) + I(m[2])
@R(r"(\d+) (?:fewer|less) than (\d+) is " + B)
def fewer_than(m, c): return I(m[2]) - I(m[1])
@R(r"(\d+) and (\d+) make " + B)
def and_make(m, c): return I(m[1]) + I(m[2])
@R(r"(\d+) and " + B + r" make (\d+)")
def and_missing_make(m, c): return I(m[2]) - I(m[1])
@R(r"(\d+) take away (\d+) is " + B)
def take_away(m, c): return I(m[1]) - I(m[2])
@R(r"Add (\d+) to (\d+)\. " + B)
def add_to(m, c): return I(m[1]) + I(m[2])
@R(r"The sum of (\d+) and (\d+) is " + B)
def sum_of(m, c): return I(m[1]) + I(m[2])
@R(r"Sold (\d+), then (\d+)\. Altogether " + B)
def sold_then(m, c): return I(m[1]) + I(m[2])
@R(r"Sold (\d+)\. Left (\d+)\. At first: " + B)
def at_first(m, c): return I(m[1]) + I(m[2])
@R(r"Subtract (\d+) from (\d+): " + B)
def subtract_from(m, c): return I(m[2]) - I(m[1])
@R(r"Difference between (\d+) and (\d+): " + B)
def difference_between(m, c): return abs(I(m[1]) - I(m[2]))
@R(r"Had (\d+)\. Gave (\d+)\. Left " + B)
def had_gave(m, c): return I(m[1]) - I(m[2])
@R(r"Ann has (\d+), (\d+) more than Jane\. Jane: " + B)
def jane(m, c): return I(m[1]) - I(m[2])

# ---- place value (P1)
@R(r"How many tens in (\d+)\? " + B)
def how_many_tens(m, c): return I(m[1]) // 10
@R(r"How many ones in (\d+)\? " + B)
def how_many_ones(m, c): return I(m[1]) % 10
@R(r"(\d+) = " + B + r" tens (?:1 one|(\d+) ones)")
def n_eq_tens(m, c):
    n = I(m[1]); o = I(m[2]) if m[2] else 1
    return (n - o) // 10 if (n - o) % 10 == 0 else None
@R(r"(\d+) \+ (\d+) = " + B + r" tens (?:1 one|(\d+) ones)")
def expanded_to_tens(m, c):
    o = I(m[3]) if m[3] else 1
    return I(m[1]) // 10 if I(m[2]) == o and I(m[1]) % 10 == 0 else None
@R(r"(\d+) = (?:1 ten|(\d+) tens) " + B + " ones")
def n_eq_tens_ones(m, c): return I(m[1]) - 10 * (I(m[2]) if m[2] else 1)
@R(r"(\d+) more than (\d+): tens digit " + B)
def tens_digit_more(m, c): return (I(m[2]) + I(m[1])) // 10
@R(r"(\d+) less than (\d+): tens digit " + B)
def tens_digit_less(m, c): return (I(m[2]) - I(m[1])) // 10

# ---- comparing
def amounts(s): return [cents(x) if (x.startswith("$") or x.endswith(CENT)) else int(x) for x in re.findall(r"\$\d+(?:\.\d+)?|\d+" + CENT + r"|\d+", s)]
@R(r"Greatest: ([\d$.¢ ]+)")
def greatest(m, c): v = amounts(m[1]); return max(v) if len(set(v)) == len(v) else None
@R(r"Smallest: ([\d$.¢ ]+)")
def smallest(m, c): v = amounts(m[1]); return min(v) if len(set(v)) == len(v) else None
@R(r"Middle number: ([\d ]+)")
def middle(m, c): return sorted(ints(m[1]))[1]
@R(r"Between (\d+) and (\d+) is " + B)
def between(m, c): return I(m[1]) + 1 if I(m[2]) - I(m[1]) == 2 else None
@R(r"(\d+) more than (\d+), then 1 more: " + B)
def more_then_more(m, c): return I(m[2]) + I(m[1]) + 1
@R(r"(\d+) less than (\d+), then 1 more: " + B)
def less_then_more(m, c): return I(m[2]) - I(m[1]) + 1

# ---- patterns
@R(r"(?:(Count back in|Count in) (\d+)s: )?(" + LIST + ")")
def pattern_seq(m, c):
    items = split_list(m[3])
    return solve_sequence(items, I(m[2]), m[1] == "Count back in") if m[1] else solve_sequence(items)
@R(r"\+(\d+): (" + LIST + ")")
def pattern_rule(m, c): return solve_sequence(split_list(m[2]), I(m[1]), False)
@R(r"Count on in (\d+)s: (" + LIST + ")")
def count_on(m, c): return solve_sequence(split_list(m[2]), I(m[1]), False)
@R(r"Start at (\d+)\. Count on 4 times in (\d+)s: " + B)
def start_count(m, c): return I(m[1]) + 4 * I(m[2])
@R(r"Which does not belong\? ((?:\d+, )+\d+)")
def not_belong(m, c):
    """the list is a skip-counting sequence with one wrong term: find every (step, start) that fits exactly n-1 positions"""
    t = [int(x) for x in split_list(m[1])]; n = len(t); odd = set()
    steps = {abs(t[j] - t[i]) // (j - i) for i in range(n) for j in range(i + 1, n) if (t[j] - t[i]) % (j - i) == 0 and t[j] != t[i]}
    for s_ in steps:
        for j in range(n):
            x0 = t[j] - s_ * j
            bad = [i for i in range(n) if t[i] != x0 + s_ * i]
            if len(bad) == 1: odd.add(t[bad[0]])
    return odd.pop() if len(odd) == 1 else None

# ---- odd and even
def after(kind, n): p = 1 if kind == "odd" else 0; return n + 1 if (n + 1) % 2 == p else n + 2
def before(kind, n): p = 1 if kind == "odd" else 0; return n - 1 if (n - 1) % 2 == p else n - 2
@R(r"The (odd|even) number just after (\d+) is " + B)
def oe_after(m, c): return after(m[1], I(m[2]))
@R(r"The (odd|even) number just before (\d+) is " + B)
def oe_before(m, c): return before(m[1], I(m[2]))
@R(r"(Odd|Even) after (\d+): " + B)
def oe_after1(m, c): return after(m[1].lower(), I(m[2]))
@R(r"(Odd|Even) before (\d+): " + B)
def oe_before1(m, c): return before(m[1].lower(), I(m[2]))
@R(r"Smallest (odd|even) number greater than (\d+): " + B)
def oe_small(m, c): return after(m[1], I(m[2]))
@R(r"Greatest (odd|even) number less than (\d+): " + B)
def oe_great(m, c): return before(m[1], I(m[2]))
@R(r"Which is (odd|even)\? ([\d ]+)")
def oe_which(m, c):
    ok = [x for x in ints(m[2]) if x % 2 == (1 if m[1] == "odd" else 0)]
    return ok[0] if len(ok) == 1 else None
@R(r"The (odd|even) number between (\d+) and (\d+): " + B)
def oe_between(m, c):
    ok = [x for x in range(I(m[2]) + 1, I(m[3])) if x % 2 == (1 if m[1] == "odd" else 0)]
    return ok[0] if len(ok) == 1 else None
@R(r"(Odd|Even) numbers: (" + LIST + ")")
def oe_seq(m, c):
    r = solve_sequence(split_list(m[2]))
    return r if r is not None and r % 2 == (1 if m[1] == "Odd" else 0) else None

# ---- numbers to 1000
@R(r"(\d+) hundreds? (\d+) tens(?: (\d+) ones)? = " + B)
def expanded(m, c): return 100 * I(m[1]) + 10 * I(m[2]) + (I(m[3]) if m[3] else 0)
@R(r"((?:[a-z]+ hundred)(?: and [a-z -]+)?) = " + B)
def words(m, c): return words_to_int(m[1])

# ---- multiplication and division
@R(r"(\d+) groups of (\d+) is " + B)
def groups_of(m, c): return I(m[1]) * I(m[2])
@R(r"Multiply (\d+) by (\d+)\. " + B)
def multiply(m, c): return I(m[1]) * I(m[2])
@R(r"(\d+) bags, (\d+) in each\. Altogether " + B)
def bags(m, c): return I(m[1]) * I(m[2])
@R(r"A has (\d+)\. B has (\d+) times as many\. B: " + B)
def times_as_many(m, c): return I(m[1]) * I(m[2])
@R(r"Share (\d+) sweets equally among (\d+) children\. Each: " + B)
def share(m, c): return exact_div(I(m[1]), I(m[2]))
@R(r"(\d+) pencils, (\d+) in a box\. Boxes: " + B)
def boxes(m, c): return exact_div(I(m[1]), I(m[2]))
@R(r"Divide (\d+) apples into (\d+) equal groups: " + B)
def divide_into(m, c): return exact_div(I(m[1]), I(m[2]))
@R(r"Mia shares (\d+) stickers with her (\d+) friends\. Each person: " + B)
def mia(m, c): return exact_div(I(m[1]), I(m[2]) + 1)
@R(r"(\d+) cookies, (\d+) each\. Most friends: " + B)
def cookies(m, c): return exact_div(I(m[1]), I(m[2]))
@R(r"(\d+) × (\d+) = (\d+) so (.* = " + B + ")")
def related_facts(m, c):
    return solve_equation(m[4]) if I(m[1]) * I(m[2]) == I(m[3]) else None

# ---- money
@R(r"I have (\d+)" + CENT + r"\. I get (\d+)" + CENT + r" more\. Now " + B + CENT)
def i_have_cents(m, c): return I(m[1]) + I(m[2])
@R(r"Ann has (\d+)" + CENT + r"\. Ben has (\d+)" + CENT + r" fewer\. Ben: " + B + CENT)
def ben_fewer_cents(m, c): return I(m[1]) - I(m[2])
@R(r"Ann has \$(\d+)\. Ben has \$(\d+) more\. Ben has \$" + B)
def ben_more_dollars(m, c): return I(m[1]) + I(m[2])
@R(r"A toy costs \$(\d+)\. A ball costs \$(\d+)\. Both cost \$" + B)
def toy_ball(m, c): return I(m[1]) + I(m[2])
@R(r"Ann has \$(\d+)\. Tom has \$(\d+) fewer\. Tom: \$" + B)
def tom_fewer(m, c): return I(m[1]) - I(m[2])
@R(r"Cost " + MONEY + r"\. Paid \$(\d+)\. Change: \$?" + B + CENT + "?")
def change(m, c): return 100 * I(m[2]) - cents(m[1])
@R(r"Pen " + MONEY + r", ruler " + MONEY + r"\. Both: \$?" + B + CENT + "?")
def pen_ruler(m, c): return cents(m[1]) + cents(m[2])
@R(r"Ann has " + MONEY + r"\. Ben has " + MONEY + r" more\. Ben has \$?" + B + CENT + "?")
def ben_more(m, c): return cents(m[1]) + cents(m[2])
@R(r"(\d+)" + CENT + r" and " + B + CENT + r" make \$1")
def make_dollar(m, c): return 100 - I(m[1])
@R(MONEY + r" = " + B + CENT)
def to_cents(m, c): return cents(m[1])
@R(r"(\d+)" + CENT + r" = \$" + B)
def to_dollars(m, c): return I(m[1])                          # cents; the blank is written in dollars (0.65) and compared as cents

# ---- time
@R(r"(?:Which time is |Say the time: |Match the time: |Time: )?(\d{1,2}):(\d\d)(?: is which time\? " + B + r"| is the same as which time\?| Which key time\?|\?)?")
def digital_time(m, c): return hmin(I(m[1]), I(m[2]))
@R(r"It is (\d+) o'clock\. (1 hour|Half an hour) (later|before): " + B)
def shift_oclock(m, c): return add_minutes((I(m[1]), 0), (60 if m[2] == "1 hour" else 30) * (1 if m[3] == "later" else -1))
@R(r"It is half past (\d+)\. (1 hour|Half an hour) (later|before): " + B)
def shift_half(m, c): return add_minutes((I(m[1]), 30), (60 if m[2] == "1 hour" else 30) * (1 if m[3] == "later" else -1))
@R(r"It is (\d{1,2}):(\d\d)\. (\d+) hours? later: " + B)
def hours_later(m, c): return add_minutes((I(m[1]), I(m[2])), 60 * I(m[3]))
@R(r"It is (\d{1,2}):(\d\d)\. (\d+) minutes later: " + B)
def minutes_later(m, c): return add_minutes((I(m[1]), I(m[2])), I(m[3]))
@R(r"It is (\d{1,2}):(\d\d)\. (\d+) minutes before: " + B)
def minutes_before(m, c): return add_minutes((I(m[1]), I(m[2])), -I(m[3]))
@R(r"(\d+) minutes past (\d+) is " + B)
def minutes_past(m, c): return hmin(I(m[2]), I(m[1]))
@R(r"(\d+) minutes to (\d+) is " + B)
def minutes_to(m, c): return hmin(I(m[2]) - 1, 60 - I(m[1]))
@R(r"Which time is (\d+) minutes past (\d+)\?")
def which_past(m, c): return hmin(I(m[2]), I(m[1]))
@R(r"(\d+) h(?:ours?)?(?: (\d+) min(?:utes)?)? = " + B + r"(?: min)?")
def to_minutes(m, c): return 60 * I(m[1]) + (I(m[2]) if m[2] else 0)
@R(r"(\d{1,2}):(\d\d)(?: am)? to (\d{1,2}):(\d\d)(?: am)?(?:: | = | takes )" + B + " min")
def duration(m, c): return (minutes_of((I(m[3]), I(m[4]))) - minutes_of((I(m[1]), I(m[2])))) % 720
@R(r"A film starts at (\d{1,2}):(\d\d) and ends at (\d{1,2}):(\d\d)\. It lasts " + B + " min")
def film(m, c): return (minutes_of((I(m[3]), I(m[4]))) - minutes_of((I(m[1]), I(m[2])))) % 720

# ---- length and measures
@R(r"Pencil: (\d+) cm Pen is (\d+) cm longer\. Pen: " + B + " cm")
def pen_longer(m, c): return (I(m[1]) + I(m[2]), "cm")
@R(r"Line A: (\d+) cm B is (\d+) cm shorter\. Line B: " + B + " cm")
def line_shorter(m, c): return (I(m[1]) - I(m[2]), "cm")
@R(r"A ribbon is (\d+) cm\. (\d+) cm is cut off\. Left: " + B + " cm")
def ribbon(m, c): return (I(m[1]) - I(m[2]), "cm")
@R(r"Rice (\d+) kg, flour (\d+) kg\. Together: " + B + " kg")
def rice_flour(m, c): return (I(m[1]) + I(m[2]), "kg")
@R(r"Melon (\d+) kg\. Pumpkin is (\d+) kg lighter\. Pumpkin: " + B + " kg")
def melon(m, c): return (I(m[1]) - I(m[2]), "kg")
@R(r"A pail holds (\d+) l\. (\d+) l is poured out\. Left: " + B + " l")
def pail(m, c): return (I(m[1]) - I(m[2]), "l")
@R(r"(\d+) l is shared into (\d+) equal tanks: " + B + " l")
def tanks(m, c):
    q = exact_div(I(m[1]), I(m[2])); return (q, "l") if q is not None else None
@R(r"Each one: " + B + r" (kg|g)")
def balance_each(m, c):
    if not meta_is(c, "balance"): return NOT_ME
    return (exact_div(c["meta"]["total"], c["meta"]["n"]), m[1])

# ---- shapes: P1 corners, P2 surfaces and sides
@R(r"(?:(How many corners in all\?|Corners:|Corners\?|Straight sides:|Straight sides\?|How many straight sides in all\?|Corners \+ sides:|Corners \+ sides\?|Corners and sides in all\?|Corners and sides:) ?)?" + B + "?")
def p1_shapes(m, c):
    if not meta_is(c, "shapes"): return NOT_ME
    kinds = c["meta"]["kinds"]; s = m[1] or ""
    if "+" in s or "and sides" in s: w = "both"
    elif "ides" in s: w = "sides"
    elif "orner" in s: w = "corners"
    else:                                                   # a bare blank: the instruction line says what to count
        ins = c["instr"].lower()
        w = "both" if "corners and the straight sides" in ins else ("sides" if "straight sides" in ins and "corners" not in ins else "corners")
    return sum({"corners": CORNERS, "sides": SIDES}[w][k] if w != "both" else CORNERS[k] + SIDES[k] for k in kinds)
@R(r"(Flat|Curved) surfaces: " + B)
def surfaces(m, c):
    if not meta_is(c, "solids") or len(c["meta"]["kinds"]) != 1: return NOT_ME
    k = c["meta"]["kinds"][0]
    return FLAT[k] if m[1] == "Flat" else CURVED[k]
@R(r"Flat surfaces in all: " + B)
def surfaces_all(m, c):
    if not meta_is(c, "solids"): return NOT_ME
    return sum(FLAT[k] for k in c["meta"]["kinds"])
@R(r"Flat surfaces ([a-z]+): " + B)
def flat_short(m, c): return FLAT.get(m[1])
@R(r"A ([a-z]+) has " + B + r" flat surfaces?")
def flat_words(m, c): return FLAT.get(m[1])
@R(r"A ([a-z]+) has " + B + r" curved surfaces?")
def curved_words(m, c): return CURVED.get(m[1])
@R(r"A ([a-z]+) has " + B + r" straight sides")
def sides_words(m, c): return SIDES.get(m[1])
@R(r"Sides of a ([a-z]+): " + B)
def sides_short(m, c): return SIDES.get(m[1])
@R(r"([a-z]+) \+ ([a-z]+): " + B + " flat surfaces")
def two_solids(m, c): return FLAT[m[1]] + FLAT[m[2]] if m[1] in FLAT and m[2] in FLAT else None
@R(r"([a-z]+(?: \+ [a-z]+)*) = " + B + " flat")
def solids_line(m, c):
    ks = m[1].split(" + ")
    return sum(FLAT[k] for k in ks) if all(k in FLAT for k in ks) else None
@R(r"Straight sides in all: " + B)
def sides_all(m, c):
    if not meta_is(c, "shapes_row"): return NOT_ME
    return sum(SIDES[k] for k in c["meta"]["kinds"])
@R(r"How many ([a-z]+)\? " + B)
def count_shapes(m, c):
    if not meta_is(c, "shapes_row"): return NOT_ME
    return c["meta"]["kinds"].count(plural(m[1]))
@R(r"Pattern of (\d+) shapes\. How many ([a-z]+)\? " + B)
def pattern_count(m, c):
    if not meta_is(c, "pattern_row"): return NOT_ME
    seq = c["meta"]["seq"]; half = len(seq) // 2; unit = seq[:half]
    if seq[:half] != seq[half:] or I(m[1]) % len(unit): return None
    return unit.count(plural(m[2])) * (I(m[1]) // len(unit))

# ---- fractions (stacked fractions arrive as a/b)
FR = r"(\d+)/(\d+)"
FB = B + "/" + B
@R(r"(Shaded|Not shaded): " + FB)
def frac_shaded(m, c):
    if not meta_is(c, "fraction"): return NOT_ME
    k = c["meta"]
    return (k["shaded"], k["parts"]) if m[1] == "Shaded" else (k["parts"] - k["shaded"], k["parts"])
@R(FB)
def frac_art_only(m, c):
    if not meta_is(c, "fraction"): return NOT_ME
    return (c["meta"]["shaded"], c["meta"]["parts"])
@R(r"(\d+) of (\d+) equal parts is " + FB)
def frac_words(m, c): return (I(m[1]), I(m[2]))
@R(FR + r" and " + FB + r" make 1 whole")
def frac_whole(m, c): return (I(m[2]) - I(m[1]), I(m[2]))
@R(FR + r" \+ " + FR + " = " + FB)
def frac_add(m, c): return (I(m[1]) + I(m[3]), I(m[2])) if m[2] == m[4] else None
@R(FR + r" [−-] " + FR + " = " + FB)
def frac_sub(m, c): return (I(m[1]) - I(m[3]), I(m[2])) if m[2] == m[4] else None
@R(r"Which is (greater|smaller): " + FR + r" or " + FR + r"\?")
def frac_compare(m, c):
    a, b = Fraction(I(m[2]), I(m[3])), Fraction(I(m[4]), I(m[5]))
    if a == b: return None
    return (I(m[2]), I(m[3])) if (max(a, b) if m[1] == "greater" else min(a, b)) == a else (I(m[4]), I(m[5]))

# ---- picture graphs and tally
def _rows(c): return dict((lab.lower(), n) for lab, n in c["meta"]["rows"])
@R(r"How many ([a-z]+)\? " + B)
def graph_read(m, c):
    if not meta_is(c, "picgraph"): return NOT_ME
    rows = _rows(c)
    return rows[m[1]] * c["meta"]["key"] if m[1] in rows else None
@R(r"How many (more|fewer) ([a-z]+) than ([a-z]+)\? " + B)
def graph_more(m, c):
    if not meta_is(c, "picgraph"): return NOT_ME
    rows = _rows(c)
    if m[2] not in rows or m[3] not in rows: return None
    d = (rows[m[2]] - rows[m[3]]) * c["meta"]["key"]
    return d if m[1] == "more" else -d
@R(r"How many ([a-z]+) and ([a-z]+)\? " + B)
def graph_two(m, c):
    if not meta_is(c, "picgraph"): return NOT_ME
    rows = _rows(c)
    return (rows[m[1]] + rows[m[2]]) * c["meta"]["key"] if m[1] in rows and m[2] in rows else None
@R(r"How many in all\? " + B)
def graph_total(m, c):
    if not meta_is(c, "picgraph"): return NOT_ME
    return sum(n for _, n in c["meta"]["rows"]) * c["meta"]["key"]
@R(r"Tally marks: " + B)
def tally_marks(m, c):
    if not meta_is(c, "tally"): return NOT_ME
    return c["meta"]["n"]

# ---- pictures that carry the whole question (the text is only a blank or a caption)
@R(r"(?:What time is it\?|What number\?|How much\?|How much money\?|How long\?|How many dots\?|How many dots in all\?|Tally marks:)? ?(?:\$)?" + B + "?" + CENT + "?(?: cm)?")
def picture_only(m, c):
    k = c["meta"]
    if k is None: return NOT_ME
    kind = k.get("kind")
    if kind == "clock": return read_clock(k)
    if kind in ("coins", "notes", "cash"): return sum(k["values"])
    if kind == "ruler": return (k["end"] - k["start"], "cm")
    if kind == "blocks": return 100 * k["h"] + 10 * k["t"] + k["o"]
    if kind == "array": return k["rows"] * k["cols"]
    if kind == "groups": return k["n"] * k["per"]
    if kind == "tally": return k["n"]
    if kind == "picgraph" and len(k["rows"]) == 1: return k["rows"][0][1] * k["key"]
    if kind == "solids": return sum(FLAT[x] for x in k["kinds"])
    if kind == "shapes_row": return sum(SIDES[x] for x in k["kinds"])
    if kind == "shapes": return _p1_shapes_bare(c)
    return NOT_ME
def _p1_shapes_bare(c):
    ins = c["instr"].lower()
    w = "both" if "corners and the straight sides" in ins else ("sides" if "straight sides" in ins and "corners" not in ins else "corners")
    return sum((CORNERS[k] + SIDES[k]) if w == "both" else (SIDES if w == "sides" else CORNERS)[k] for k in c["meta"]["kinds"])

# ------------------------------------------------------------------ entry points
def solve(lines, meta=None, instr="", kind=None):
    """-> (value, rule name). `kind` == "dollars" when a money answer is stored in whole dollars (cents otherwise)."""
    t = norm(lines)
    ctx = dict(meta=meta, instr=instr, kind=kind)
    for rx, fn in RULES:
        m = rx.fullmatch(t)
        if not m: continue
        r = fn(m, ctx)
        if r is NOT_ME: continue
        return _finish(r, kind), fn.__name__
    if B in t and "=" in t:
        try: return _finish(solve_equation(t), kind), "equation"
        except Unparsed: pass
    raise Unparsed(t)

def _finish(r, kind):
    if isinstance(r, tuple) and len(r) == 2 and (r[1] is None or (isinstance(r[1], str) and not isinstance(r[0], str))) and (isinstance(r[0], (int, Fraction))):
        v, unit = r
        if isinstance(v, Fraction): v = int(v) if v.denominator == 1 else v
        if unit == "money-cents": cents_ = v
        elif unit == "money-dollars": cents_ = v * 100
        else: return (v, unit) if unit else v
        if isinstance(cents_, Fraction) and cents_.denominator == 1: cents_ = int(cents_)
        if kind == "dollars": return cents_ // 100 if cents_ % 100 == 0 else None
        return cents_
    if isinstance(r, Fraction): return int(r) if r.denominator == 1 else r
    return r

def matches(res, ans):
    """does the independently solved value equal the key value `ans`?"""
    if res is None: return False
    if isinstance(ans, tuple) and len(ans) == 2 and isinstance(ans[1], str):          # measure (n, unit)
        return isinstance(res, tuple) and tuple(res) == ans
    if isinstance(res, tuple) and len(res) == 2 and isinstance(res[1], str) and isinstance(ans, int):     # P1 length: the unit is implied
        return res[0] == ans
    return res == ans
