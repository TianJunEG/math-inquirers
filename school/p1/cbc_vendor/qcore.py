"""Question core shared by every level: Q (one question), EQ and SEM (builders), Tier and Bank.
A bank knows nothing about pictures: it makes one question for any wanted answer.
Each bank has, per tier (1 = one star, 2 = two stars): five key values (the answers that map to the five colours),
a domain of every value a pupil could plausibly write, and several question forms that differ in layout.
A Q carries the printed lines, the teacher lines, and `holds(v)` that says whether value v answers the question.
Level files (banks_p1.py, banks_p2.py, ...) import from here and from art.py; nothing else is needed to add a level."""
import re
from dataclasses import dataclass, field
from decimal import Decimal

BOX = "□"
FBOX = "⟨□|□⟩"                    # a stacked fraction with two blanks (numerator over denominator)
def FRAC(a, b): return f"⟨{a}|{b}⟩"                 # a stacked fraction printed in a text line
def AFRAC(a, b): return f"⟨⟦{a}⟧|⟦{b}⟧⟩"           # the same with its numbers as teacher answers
MINUS = "−"
TIMES = "×"
DIVIDE = "÷"

@dataclass
class Q:
    lines: list                       # printed lines; BOX marks a blank
    holds: object                     # v -> bool   (true for the intended answer and for no other value of the domain)
    sol: list = None                  # teacher lines with the answer in place (filled by the bank)
    art: object = None                # art.Art or None
    layout: str = "stack"             # 'stack' (art above the text) or 'row' (art left, text right)
    form: str = ""
    eq: list = field(default_factory=list)   # printed equation lines that the verifier re-evaluates from the text
    eq_money: bool = False            # equation lines are in money notation ($1.20, 65¢; the blank is in cents)
    a_text: str = None                # the answer as printed in the teacher page
    extra: object = None              # optional callable(answer) -> bool: bank-specific independent check (e.g. decode the picture)
    sig: object = None                # what the exercise IS (e.g. ("mult", 3, 5), ("div", 12, 2)); two questions of one sheet with the same sig are the same exercise however they are worded

def mark(s, a_text):
    if FBOX in s and "/" in a_text:                  # a fraction answer "n/d" fills the two blanks of the stacked box
        n, d = a_text.split("/"); return s.replace(FBOX, AFRAC(n, d), 1)
    return s.replace(BOX, "⟦" + a_text + "⟧", 1) if BOX in s else s

_code = {}
def _compile(line, money):
    k = (line, money)
    if k in _code: return _code[k]
    t = line.replace(BOX, "(v)").replace(MINUS, "-").replace(TIMES, "*").replace(DIVIDE, "/")
    if money:
        t = re.sub(r"\$(\d+(?:\.\d+)?)", lambda m: f"({int(Decimal(m.group(1)) * 100)})", t)
        t = re.sub(r"(\d+)¢", r"(\1)", t).replace("(v)¢", "(v)")
    else:
        t = t.replace("¢", "").replace("$", "").replace("cm", "")
    if not re.fullmatch(r"[0-9v+\-*/() =.]+", t): raise ValueError(line)
    l, r = t.split("=")
    _code[k] = (compile(l.strip(), "<eq>", "eval"), compile(r.strip(), "<eq>", "eval"))
    return _code[k]

def eq_eval(line, v, money=False):
    """does the printed equation hold when the blank holds v?"""
    l, r = _compile(line, money)
    g = {"v": v}
    return eval(l, g) == eval(r, g)

def EQ(lines, a, a_text=None, money=False, **kw):
    """question whose answer is found by solving the equation line(s) that contain a blank"""
    lines = list(lines)
    eqs = [l for l in lines if BOX in l and "=" in l]
    if len(lines) > 1 and not all(BOX in l and "=" in l for l in lines):
        eqs = [" ".join(lines)]                     # one equation printed over two lines
    assert eqs, lines
    q = Q(lines, lambda v, eqs=eqs, m=money: all(eq_eval(l, v, m) for l in eqs), eq=eqs, eq_money=money, **kw)
    at = a_text if a_text is not None else str(a)
    q.a_text = at
    q.sol = [mark(l, at) for l in lines]
    return q

def SEM(lines, holds, a_text, **kw):
    q = Q(list(lines), holds, **kw)
    q.a_text = a_text
    q.sol = [mark(l, a_text) for l in lines]
    return q

@dataclass
class Tier:
    key: list
    domain: list
    forms: list
    disp: object = str
    instr: str = None                 # overrides the bank's instruction line for this tier
    kind: str = None                  # 'dollars' when a money key is stored in whole dollars (textcheck.py); None = cents or plain numbers
    maxuse: dict = None               # optional {key value: most regions of one sheet that can hold it} where a value has few distinct exercises

@dataclass
class Bank:
    id: str
    title: str                 # words used in the worksheet title
    topic: str                 # inventory topic name
    instr: str
    tiers: dict
    topic_by_tier: dict = None         # optional more exact topic name per tier
    parts: list = None                 # optional [(phrase, predicate(form_name, answer))]: the footer tag then names only what a sheet really contains
    prefix: str = ""                   # footer tag text before the phrases, e.g. "Fractions: "

    def topic_for(self, tier): return (self.topic_by_tier or {}).get(tier, self.topic)
    def topic_used(self, tier, used):
        """footer tag of one worksheet; `used` is a list of (form_name, answer) of its questions. Without `parts` this is the plain topic name."""
        if not self.parts: return self.topic_for(tier)
        said = [p for p, pred in self.parts if any(pred(f, a) for f, a in used)]
        return self.prefix + ", ".join(said) if said else self.topic_for(tier)

def T(key, domain, forms, disp=str, instr=None, kind=None, maxuse=None):
    return Tier(list(key), list(domain), forms, disp, instr, kind, maxuse)
