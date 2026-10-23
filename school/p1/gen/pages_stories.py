"""New pages: story problems (N01 Story Sums P1-21, N02 Two-Step Stories P1-22, N11 Share and Group Stories P1-39, N12 True or False Groups P1-40)."""
import random, itertools, re
from .common import *
from . import art
from .art import row_svg, count_objs, NAMES as OBJN

PEOPLE = ["Ali", "Mei", "Siti", "Ben", "Kumar", "Aisha", "Wei", "Ravi", "Jenny", "Lily"]

def finish_code(P, answers, table, word, lo, hi, domain=None, plain="Code word (6 letters)"):
    """the standard record every code-word page keeps: V2/V3/V3c/V3d/V4 and the model for validate.py's enumeration"""
    cv = code_verify(answers, table, word, lo, hi, domain)
    code_checks(P, cv, word)
    P["cv"] = cv
    P["model"] = code_model(answers, table, lo, hi, domain)
    P["mech_plain"] = plain
    return cv

def plain_text(h): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()

# ---------------------------------------------------------------- N01 Story Sums (P1-21)
ADD_V = {"apple": "picks", "flower": "picks", "star": "finds", "ball": "gets", "sweet": "gets", "bird": "gets", "fish": "gets", "balloon": "buys", "car": "gets", "kite": "buys"}
SUB_V = {"apple": "eats", "sweet": "eats", "flower": "gives away", "star": "loses", "ball": "loses", "bird": "gives away", "fish": "gives away", "balloon": "gives away", "car": "gives away", "kite": "loses"}

def story_text(kind, a, b, N, M, pl, obj):
    if kind == "add":   return [f"{N} has {a} {pl}.", f"{N} {ADD_V[obj]} {b} more.", "How many now?"]
    if kind == "sub":   return [f"{N} has {a} {pl}.", f"{N} {SUB_V[obj]} {b}.", "How many are left?"]
    if kind == "more":  return [f"{N} has {a} {pl}.", f"{M} has {b} more than {N}.", f"How many does {M} have?"]
    if kind == "fewer": return [f"{N} has {a} {pl}.", f"{N} has {b} fewer than {M}.", f"How many does {M} have?"]
    if kind == "diff":  return [f"{N} has {a} {pl}.", f"{M} has {b}.", f"How many more does {N} have?"]
    if kind == "total": return [f"{N} has {a} {pl}.", f"{M} has {b}.", "How many in all?"]

def solve_story(lines):
    """independent solver: reads the printed sentences only (no access to the generator's kind)"""
    t = " ".join(lines)
    nums = [int(x) for x in re.findall(r"\d+", t)]
    a, b = nums[0], nums[1]
    names = re.findall(r"\b([A-Z][a-z]+) (?:has|gets|picks|finds|buys|eats|loses|gives)", t)
    if "fewer than" in t:                                  # X has b fewer than Y; the question asks about Y: Y = X + b
        x = re.search(r"(\w+) has \d+ fewer than (\w+)", lines[1]); q = re.search(r"does (\w+) have", lines[2])
        return a + b if q.group(1) == x.group(2) else a - b
    if "more than" in t:                                   # Y has b more than X; the question asks about Y
        y = re.search(r"(\w+) has \d+ more than (\w+)", lines[1]); q = re.search(r"does (\w+) have", lines[2])
        return a + b if q.group(1) == y.group(1) else a - b
    if "How many more" in t: return a - b
    if "in all" in t: return a + b
    if re.search(r"\b(eats|loses|gives away)\b", lines[1]): return a - b
    if re.search(r"\b(gets|picks|finds|buys)\b", lines[1]): return a + b
    raise ValueError(lines)

def story_card(no, lines, pics, ans_html, below=False):
    ps = "".join(f'<p class="st">{html_escape(l)}</p>' for l in lines)
    if below:
        return (f'<div class="story"><div class="sh"><span class="no">{no}</span><div class="stx">{ps}</div></div>'
                f'<div class="sp">{"".join(pics)}</div><div class="sa below">{ans_html}</div></div>')
    return (f'<div class="story"><div class="sh"><span class="no">{no}</span><div class="stx">{ps}</div><div class="sa">{ans_html}</div></div>'
            f'<div class="sp">{"".join(pics)}</div></div>')

def html_escape(s): return s.replace("&", "&amp;").replace("<", "&lt;")

def page21():
    rng = random.Random(2101)
    word = "MONKEY"
    kinds = ["add", "sub", "more", "fewer", "diff", "total"]
    objs = ["apple", "bird", "star", "fish", "balloon", "sweet", "flower", "ball", "car", "kite"]
    while True:
        rng.shuffle(kinds); items = []
        names = rng.sample(PEOPLE, 6)
        o = rng.sample(objs, 6)
        for i, kd in enumerate(kinds):
            if kd == "add": a = rng.randint(4, 12); b = rng.randint(2, min(8, 20 - a))
            elif kd == "sub": a = rng.randint(7, 12); b = rng.randint(2, a - 2)
            elif kd in ("more", "fewer"): a = rng.randint(3, 10); b = rng.randint(2, 7)
            elif kd == "diff": a = rng.randint(6, 10); b = rng.randint(2, a - 2)
            else: a = rng.randint(3, 9); b = rng.randint(3, 9)
            N = names[i]; M = rng.choice([x for x in PEOPLE if x != N])
            items.append(dict(kind=kd, a=a, b=b, N=N, M=M, obj=o[i]))
        ans = []
        for it in items:
            ans.append({"add": it["a"] + it["b"], "sub": it["a"] - it["b"], "more": it["a"] + it["b"], "fewer": it["a"] + it["b"], "diff": it["a"] - it["b"], "total": it["a"] + it["b"]}[it["kind"]])
        two = [it for it in items if it["kind"] in ("diff", "total")]
        big = sum(1 for it in items if (it["a"] + it["b"] > 12 if it["kind"] in ("diff", "total") else it["a"] > 12))
        if len(set(ans)) != 6 or min(ans) < 2 or max(ans) > 20 or big > 1: continue
        wrong = set()
        for it in items:
            wrong |= {it["a"] + it["b"], it["a"] - it["b"]}
        wrong = sorted(w for w in wrong if 0 <= w <= 20 and w not in ans)
        table = make_code_table(ans, word, rng, 0, 20, n_decoy=5, near=(1, -1, 2, -2, 10, -10), tries=80, pool=wrong)
        if table: break
    cards = []; texts = []; picobjs = []
    for i, it in enumerate(items):
        pl = OBJN[it["obj"]][1]
        lines = story_text(it["kind"], it["a"], it["b"], it["N"], it["M"], pl, it["obj"]); texts.append(lines)
        s1, _, _ = row_svg(it["obj"], it["a"], size=5.6, pitch=6.2)
        pics = [s1]; cnt = [it["a"]]
        if it["kind"] in ("diff", "total"):
            s2, _, _ = row_svg(it["obj"], it["b"], size=5.6, pitch=6.2); pics.append(s2); cnt.append(it["b"])
        picobjs.append(pics)
        cards.append(story_card(i + 1, lines, pics, '<span class="ab"></span>'))
    body = f'<div class="stories">{"".join(cards)}</div>{code_block(table)}'
    kd_names = {"add": "adds", "sub": "takes away", "more": "has more than", "fewer": "has fewer than (the reversal)", "diff": "how many more", "total": "in all"}
    P = Page(no=21, title="Story Sums", tier=2, topic="Add and take away stories within 20",
             strand="Number and Algebra - Whole Numbers", syll="2.1, 2.2, 2.7 (concepts of addition and subtraction, +, - and =, mental calculation within 20)",
             ptype="Code-breaker (stories)", mech="K1 code word (6 letters)",
             instr=["Read each story.", "Write how many.", "Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=6,
             key=dict(answers=", ".join(f"{i+1}) {it['a']} {'-' if ans[i] == it['a'] - it['b'] else '+'} {it['b']} = {ans[i]}" for i, it in enumerate(items)), check_result=f"Code word: {word}"),
             note=("Six short stories within 20, each with a picture of the first group. The pupil chooses add or take away from the story. "
                   "One story says 'fewer than' about the other child: the child asked about has more, so the answer is an addition. Where possible the table decoys are the answers a pupil gets by using the wrong operation, "
                   "and any other value has no letter at all, so the wrong operation never spells the word. The stories use more than and fewer than and 'how many more'."),
             seed=2101)
    solved = [solve_story(l) for l in texts]
    P.v("V1 independent solver reads the printed sentences back and equals the key", solved == ans, solved)
    P.v("V1b the picture shows the first group: objects counted in the drawing equal the first number in the text", all(count_objs(pics[0]).get(it["obj"]) == it["a"] and (len(pics) == 1 or count_objs(pics[1]).get(it["obj"]) == it["b"]) for pics, it in zip(picobjs, items)))
    P.v("V1c answers distinct and within 20", len(set(ans)) == 6 and max(ans) <= 20)
    P.v("V7 at most one picture shows more than 12 objects", sum(1 for it in items if (it['a'] + it['b'] if it['kind'] in ('diff', 'total') else it['a']) > 12) <= 1)
    finish_code(P, ans, table, word, 0, 20)
    return P


# ---------------------------------------------------------------- N02 Two-Step Stories (P1-22)
PLUS = r"\b(gets|picks|finds|buys|more)\b"; MINUS = r"\b(eats|loses|gives away|gave away)\b"

def solve_two(lines):
    """independent solver for one two-step story, reading the printed sentences only; returns (step 1 answer, final answer)"""
    t = " ".join(lines)
    if lines[0].startswith("Fact:"):
        w = int(re.search(r"has (\d+) wheels", lines[0]).group(1)); n = int(re.search(r"sees (\d+) ", lines[1]).group(1)); c = int(re.search(r"^(\d+) wheels", lines[2]).group(1))
        return w * n, w * n - c
    if "had some" in lines[0]:
        b = int(re.search(r"away (\d+)", lines[1]).group(1)); a = int(re.search(r"has (\d+)", lines[2]).group(1)); c = int(re.search(r"gets (\d+) more", lines[3]).group(1))
        return a + b, a + c
    a = int(re.search(r"has (\d+)", lines[0]).group(1))
    v = a; steps = []
    for l in lines[1:]:
        n = int(re.search(r"\d+", l).group(1) if False else re.search(r"\d+", l).group(0))
        v = v + n if re.search(PLUS, l) else v - n if re.search(MINUS, l) else None
        steps.append(v)
    return steps[0], steps[1]

def page22():
    rng = random.Random(2202)
    word = "GUITAR"
    objs = ["apple", "bird", "star", "fish", "balloon", "sweet", "flower", "ball", "car", "kite"]
    stick = "stickers"
    while True:
        names = rng.sample(PEOPLE, 6); o = rng.sample(objs, 6); items = []
        # 0 forward within 20 (add then take away), 1 forward within 20 (take away then add), 2 at first within 20, 3 at first within 100, 4 printed fact, 5 forward within 100
        a = rng.randint(5, 10); b = rng.randint(2, 7); c = rng.randint(2, min(8, a + b - 1))
        items.append(dict(k="fwd", N=names[0], pl=OBJN[o[0]][1], obj=o[0], v1=ADD_V[o[0]], v2=SUB_V[o[0]], a=a, b=b, c=c, s1=a + b, fin=a + b - c))
        a = rng.randint(9, 16); b = rng.randint(2, 6); c = rng.randint(2, 6)
        items.append(dict(k="fwd", N=names[1], pl=OBJN[o[1]][1], obj=o[1], v1=SUB_V[o[1]], v2=ADD_V[o[1]], a=a, b=b, c=c, s1=a - b, fin=a - b + c))
        a = rng.randint(6, 10); b = rng.randint(3, 8); c = rng.randint(2, 6)
        items.append(dict(k="back", N=names[2], pl=OBJN[o[2]][1], obj=o[2], a=a, b=b, c=c, s1=a + b, fin=a + c))
        a = rng.randint(2, 5) * 10 + rng.randint(1, 5); b = rng.randint(1, 3) * 10; c = rng.randint(1, 4)
        items.append(dict(k="back", N=names[3], pl="stickers", obj=None, a=a, b=b, c=c, s1=a + b, fin=a + c))
        t = rng.randint(3, 5); c = rng.randint(2, 5)
        items.append(dict(k="fact", N=names[4], t=t, c=c, s1=3 * t, fin=3 * t - c))
        a = rng.randint(3, 6) * 10 + rng.randint(1, 5); b = rng.randint(1, 3) * 10; c = rng.randint(1, 4)
        items.append(dict(k="fwd", N=names[5], pl="stickers", obj=None, a=a, b=b, c=c, s1=a + b, fin=a + b - c, v1="gets", v2="gives away"))
        rng.shuffle(items)
        if any(it["k"] != "fact" and it["b"] == it["c"] for it in items): continue
        ans = [it["fin"] for it in items]
        if len(set(ans)) != 6 or min(ans) < 1 or max(ans) > 99: continue
        table = make_code_table(ans, word, rng, 1, 100, n_decoy=5, near=(1, -1, 10, -10, 2, -2), tries=80)
        if table: break
    cards = []; texts = []
    for i, it in enumerate(items):
        N = it["N"]
        if it["k"] == "fwd":
            lines = [f"{N} has {it['a']} {it['pl']}.", f"{N} {it['v1']} {it['b']}" + (" more." if it["v1"] in ADD_V.values() or it["v1"] == "gets" else "."), f"Then {N} {it['v2']} {it['c']}" + (" more." if it["v2"] in ADD_V.values() or it["v2"] == "gets" else ".")]
            lab = ("step 1", "step 2")
        elif it["k"] == "back":
            lines = [f"{N} had some {it['pl']}.", f"{N} gave away {it['b']}.", f"Now {N} has {it['a']}.", f"Then {N} gets {it['c']} more."]
            lab = ("at first", "at the end")
        else:
            lines = ["Fact: 1 tricycle has 3 wheels.", f"{N} sees {it['t']} tricycles.", f"{it['c']} wheels are broken.".replace(" are", " are"), ]
            lab = ("all the wheels", "wheels that work")
        texts.append(lines)
        pics = []
        if it["k"] == "fwd" and it.get("obj"):
            s1, _, _ = row_svg(it["obj"], it["a"], size=5.2, pitch=5.8); pics = [s1]
        if it["k"] == "fact":
            pics = []
        boxes = "".join(f'<span class="lbx"><span class="ab"></span><small>{l}</small></span>' for l in lab)
        cards.append(story_card(i + 1, lines, pics, boxes, below=True))
    body = f'<div class="stories">{"".join(cards)}</div>{code_block(table)}'
    P = Page(no=22, title="Two-Step Stories", tier=2, topic="Two-step stories: add, take away, work backwards",
             strand="Number and Algebra - Whole Numbers", syll="2.1, 2.2, 2.5, 2.7 (two-step stories within 100: problem solving, work backwards, a printed fact)",
             ptype="Code-breaker (two-step stories)", mech="K1 code word (6 letters) + K7 put the answer back",
             instr=["Read each story.", "Write the answer to each step.", "Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=6,
             key=dict(answers=", ".join(f"{i+1}) {it['s1']} then {it['fin']}" for i, it in enumerate(items)), check_result=f"Code word: {word}"),
             note=("Six stories with two boxes each. The second box (the end answer) is the one looked up in the code table. Two stories say 'at first': the pupil starts from the number now and works backwards. "
                   "One story has a printed fact (1 tricycle has 3 wheels) so a pupil is not stopped by a fact they may not know. Two stories use tens (no renaming). "
                   "The first box is not looked up in the table; a wrong first answer almost always makes the end answer wrong. Pupils can put the end answer back into the story to check it makes sense."),
             seed=2202)
    solved = [solve_two(l) for l in texts]
    P.v("V1 independent solver reads the printed sentences back: step answers and end answers equal the key", solved == [(it["s1"], it["fin"]) for it in items], solved)
    P.v("V1b end answers distinct, within 100", len(set(ans)) == 6 and max(ans) <= 99)
    def no_renaming(it):
        if it["k"] == "fact" or it["a"] <= 20: return True
        if it["k"] == "fwd": return it["s1"] % 10 >= it["c"] and it["b"] % 10 == 0
        return it["a"] % 10 + it["c"] < 10 and it["b"] % 10 == 0
    P.v("V1c the stories within 100 use tens and ones with no renaming", all(no_renaming(it) for it in items))
    P.v("V1d two stories ask 'at first' and one has a printed fact", sum(it["k"] == "back" for it in items) == 2 and sum(it["k"] == "fact" for it in items) == 1)
    finish_code(P, ans, table, word, 1, 100)
    P["facts"] = "3 100"
    return P

PAGES = [page21, page22]
