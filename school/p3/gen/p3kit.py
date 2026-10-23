"""Primary 3 helpers on top of kit.py: number formatting, the standard code-word page, lettered choice rows, ordering cards,
matching rows, 4-column vertical sums. Everything is black and white. Independent solvers live in each page module."""
import random, re, itertools, html as _html
from .common import *
from .kit import *

STRAND_WN = "Number and Algebra - Whole Numbers"
STRAND_AS = "Number and Algebra - Addition and Subtraction"
STRAND_MD = "Number and Algebra - Multiplication and Division"
STRAND_FR = "Number and Algebra - Fractions"
STRAND_MO = "Number and Algebra - Money"
STRAND_ME = "Measurement and Geometry - Measurement"
STRAND_AP = "Measurement and Geometry - Area and Perimeter"
STRAND_GE = "Measurement and Geometry - Geometry"
STRAND_ST = "Statistics - Bar Graphs"
INSTR_CODE = "Use the code table."
PEOPLE = ["Ali", "Mei", "Siti", "Ben", "Kumar", "Aisha", "Wei", "Ravi", "Jenny", "Lily", "Hana", "Tom", "Zara", "Amir", "Priya", "Daniel"]

def N(n):
    """a whole number as printed: 4-digit numbers without a space (1234), 5 digits or more with a space (10 000)"""
    s = str(n)
    if len(s) <= 4: return s
    return s[:-3] + " " + s[-3:]

def unN(s):
    return int(s.replace(" ", "").replace(" ", ""))

def money(c):
    """cents -> $x.xx"""
    return f"${c // 100}.{c % 100:02d}"

def unmoney(s):
    d, c = s.lstrip("$").split("."); return int(d) * 100 + int(c)

def distinct(xs): return len(set(xs)) == len(xs)

# ---------------------------------------------------------------------------------------------------- the standard code-word page
def code_items_page(no, seed, title, tier, topic, strand, syll, oc, ptype, instr, items_html, answers, table, word, lo, hi, key_answers, note,
                    domain=None, fmt=str, ps=False, pre_body="", mech=None, plain=None, cols=None):
    body = pre_body + items_html + table_block(table, fmt, cols)
    P = new_page(no, seed, title, tier, topic, strand, syll, oc, ptype, mech or f"K1 code word ({len(word)} letters)", instr, body, key_answers,
                 f"Code word: {word}", note, check_boxes=len(word), ps=ps)
    finish_code(P, answers, table, word, lo, hi, domain, plain)
    P["facts"] = " ".join(str(v) for v in table) + " " + " ".join(str(a) for a in answers)
    return P

def find_table(no, n, ans, rng, lo, hi, pool, n_decoy=3, tries=80, domain=None):
    res = code_table_any(no, n, ans, rng, lo, hi, n_decoy=n_decoy, tries=tries, pool=pool, domain=domain)
    return res

# ---------------------------------------------------------------------------------------------------- vertical sums, up to 4 digits
def digs(x, width=None):
    s = str(x)
    if width: s = s.rjust(width)
    return "".join('<i class="ab"></i>' if ch == "?" else ("<i></i>" if ch == " " else f"<i>{ch}</i>") for ch in s)

def vsum4(top, bot, op, res=None, width=4, answer_box=True):
    """a vertical sum: numbers right-aligned in `width` columns; '?' in a number marks a missing digit (an answer box); res=None draws a wide answer box"""
    cols = f"7mm repeat({width},9mm)"
    last = (f'<div class="vr" style="grid-template-columns:{cols}"><em></em>{digs(res, width)}</div>' if res is not None
            else (f'<div class="vr vans" style="grid-template-columns:7mm 1fr"><em></em><span class="ab w4"></span></div>' if answer_box else ""))
    return (f'<div class="vsum" style="grid-template-columns:{cols}"><div class="vr" style="grid-template-columns:{cols}"><em></em>{digs(top, width)}</div>'
            f'<div class="vr" style="grid-template-columns:{cols}"><em>{op}</em>{digs(bot, width)}</div><div class="vrule"></div>{last}</div>')

def parse_vsum4(h):
    """independent reader: rows of digits ('?' = box) and the operator"""
    rows = re.findall(r'<div class="vr"[^>]*>(.*?)</div>', h)
    def num(r): return "".join("?" if t.startswith('<i class="ab"') else t[3:-4] for t in re.findall(r"<i[^>]*>[^<]*</i>", r)).strip()
    op = re.search(r"<em>(.*?)</em>", rows[1]).group(1)
    return [num(r) for r in rows[:3] if r.strip()], op

# ---------------------------------------------------------------------------------------------------- lettered choices
def letter_rows(rng, word, n_opts, tries=800):
    """rows[i] = [right letter, wrong letters ...]; no other way of choosing one option in every row spells a word of the large list"""
    return choice_letters(rng, word, n_opts, tries)

def choice_check_ok(word, rows):
    return not choice_other_words(word, rows)

def lettered_choice_page(no, seed, title, tier, topic, strand, syll, oc, ptype, instr, rows_spec, n_opts, key_answers, note, word_len=6,
                         rng=None, pre_html="", ps=False, extra_check=None, row_cls=""):
    """rows_spec: list of dict(q=html, opts=[html,...] (the first is right), solve=callable(optionsHTML list)->index of right) shuffled here.
    Returns (P, info). The right option of row i carries letter word[i]; others carry decoy letters; the pupil writes the letters in the boxes."""
    rng = rng or random.Random(seed)
    for _ in range(40):
        cand = word_candidates(no, word_len)
        if not cand: raise RuntimeError("no word")
        word = cand[rng.randrange(0, min(5, len(cand)))]
        try:
            rows = letter_rows(rng, word, n_opts)
            break
        except RuntimeError:
            continue
    CLAIMED[no] = word
    out = []; pos = []
    for i, spec in enumerate(rows_spec):
        order = list(range(n_opts)); rng.shuffle(order)
        pos.append(order.index(0))
        opts = "".join(f'<span class="opt">{spec["opts"][j]}<i class="cl">{rows[i][j]}</i></span>' for j in order)
        out.append(f'<div class="crow2 {row_cls}"><span class="no">{i+1}</span><div class="cq2">{spec["q"]}</div><div class="copts">{opts}</div></div>')
    body = pre_html + '<div class="crows2">' + "".join(out) + '</div>'
    P = new_page(no, seed, title, tier, topic, strand, syll, oc, ptype, f"K1 the letter of the right choice in each row spells a word ({word_len} letters, {n_opts - 1} decoy letters in each row)",
                 instr, body, key_answers, f"Word: {word}", note, check="Write the letters in order. Do they spell a word?", check_boxes=word_len, ps=ps,
                 mech_plain=f"Word from the letters of the right choices ({word_len} letters)")
    P["rows_letters"] = rows
    P["word"] = word
    other = choice_other_words(word, rows)
    P.v(f"V3 none of the other {n_opts ** word_len - 1} ways to choose one option in every row spells a word (large word list)", not other, other[:3])
    P.v("V3d the word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()], anagrams(word))
    P["model"] = dict(truth=list(word), domains=[list(r) for r in rows], check=letters_check(), numeric=False)
    P["cv"] = dict(rate=1.0, single_total=word_len * (n_opts - 1), single_detected=word_len * (n_opts - 1))
    P["facts"] = ""
    return P

def read_choice_rows(body):
    """independent reader of a lettered-choice body: for each row the question html and the list of (option html, letter)"""
    rows = []
    for m in re.finditer(r'<div class="crow2[^"]*"><span class="no">\d+</span><div class="cq2">(.*?)</div><div class="copts">(.*?)</div></div>(?=<div class="crow2|</div>$|</div><)', body, re.S):
        q, o = m.group(1), m.group(2)
        opts = re.findall(r'<span class="opt">(.*?)<i class="cl">(\w)</i></span>', o, re.S)
        rows.append((q, opts))
    return rows

def solve_letters(word_rows_solver, body):
    """apply a solver(question_html, [option_html...]) -> index to every printed row and return the letters of the chosen options"""
    out = ""
    for q, opts in read_choice_rows(body):
        j = word_rows_solver(q, [o[0] for o in opts]); out += opts[j][1]
    return out

# ---------------------------------------------------------------------------------------------------- ordering cards
def order_page(no, seed, title, tier, topic, strand, syll, oc, ptype, instr, setA, setB, labelA, labelB, keyA, keyB, key_answers, note, rng=None, mk=("logic",)):
    """two sets of three cards, each card a letter; the pupil writes the letters in the order asked, set A then set B, six boxes.
    setA / setB: lists of (card_html, value) already in the RIGHT order (value is only used for the key); words = letters."""
    raise NotImplementedError
