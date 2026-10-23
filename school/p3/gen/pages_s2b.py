"""Semester 2, pages P3-26 to P3-29: time.
P3-26 Seconds; P3-27 The 24-Hour Clock (lettered choice); P3-28 Start, Finish, How Long (lettered choice); P3-29 Time Detective."""
import random, re, itertools, math
from .common import *
from .kit import *
from .p3kit import *
from . import art3 as A3
from . import art2 as A2

def ampm(mins):
    """minutes since midnight -> '7:45 am' (no full stops)"""
    h, m = divmod(mins % 1440, 60)
    suf = "am" if h < 12 else "pm"
    h12 = h % 12 or 12
    return f"{h12}:{m:02d} {suf}"

def unampm(s):
    m = re.fullmatch(r"(\d+):(\d\d) (am|pm)", s)
    h, mi = int(m.group(1)) % 12, int(m.group(2))
    return (h + (12 if m.group(3) == "pm" else 0)) * 60 + mi

def h24(mins):
    h, m = divmod(mins % 1440, 60); return f"{h:02d}{m:02d} h"

def unh24(s):
    m = re.fullmatch(r"(\d\d)(\d\d) h", s); return int(m.group(1)) * 60 + int(m.group(2))

def hm_text(d):
    h, m = divmod(d, 60)
    return (f"{h} h " if h else "") + (f"{m} min" if m else "").strip()

def un_hm(s):
    m = re.fullmatch(r"(?:(\d+) h)? ?(?:(\d+) min)?", s.strip())
    return int(m.group(1) or 0) * 60 + int(m.group(2) or 0)

# =============================================================================== P3-26 Seconds
def page26():
    rng = random.Random(4626)
    while True:
        s1, s2 = rng.sample(range(5, 60, 5), 2)
        a3 = (rng.randint(1, 3), rng.randrange(5, 60, 5))
        n4 = rng.randint(3, 6)
        a5 = (rng.randint(2, 4), rng.randrange(10, 60, 10))
        n6 = rng.randint(3, 6) * 60
        items = [dict(k="dial", s=s1, ans=s1), dict(k="dial1", s=s2, ans=60 + s2), dict(k="conv", m=a3[0], s=a3[1], ans=a3[0] * 60 + a3[1]),
                 dict(k="inmin", n=n4, ans=n4 * 60), dict(k="song", m=a5[0], s=a5[1], ans=a5[0] * 60 + a5[1], nm=rng.choice(PEOPLE)), dict(k="mins", n=n6, ans=n6 // 60)]
        rng.shuffle(items); items.sort(key=lambda it: not it["k"].startswith("dial")); ans = [it["ans"] for it in items]
        if not distinct(ans) or max(ans) > 600: continue
        pool = set()
        for it in items:
            a = it["ans"]; pool |= {a + 10, a - 10, a + 60, a - 60, a + 5, a - 5}
            if it["k"] in ("conv", "song"): pool |= {it["m"] * 100 + it["s"], it["m"] + it["s"]}
            if it["k"] == "inmin": pool |= {it["n"], it["n"] * 100}
            if it["k"] == "mins": pool |= {it["n"] // 10, it["n"] - 60}
        pool = sorted(x for x in pool if x not in ans and 0 < x <= 600)
        res = find_table(26, 6, ans, rng, 0, 600, pool, n_decoy=3, tries=60)
        if res: word, table = res; break
    cards = []; texts = []; svgs = []
    for i, it in enumerate(items):
        k = it["k"]
        if k in ("dial", "dial1"):
            s = A3.stopwatch_svg(it["s"]); svgs.append(s)
            t = "The hand shows the seconds." if k == "dial" else "The stopwatch has run for 1 minute and the hand is here. How many seconds in all?"
            texts.append(t)
            cards.append(qcard(i + 1, '<div class="dial">' + s + f'</div><p class="cap">{t}</p>', '<span class="ab w3"></span> <b>s</b>', cls="pos"))
        else:
            svgs.append(None)
            if k == "conv": t = f"How many seconds are in {it['m']} min {it['s']} s?"
            elif k == "inmin": t = f"How many seconds are in {it['n']} minutes?"
            elif k == "song": t = f"{it['nm']}'s song lasts {it['m']} min {it['s']} s. How many seconds is that?"
            else: t = f"How many minutes are {it['n']} seconds?"
            texts.append(t)
            unit = "min" if k == "mins" else "s"
            cards.append(qcard(i + 1, f"<p>{t}</p>", f'<span class="ab w3"></span> <b>{unit}</b>'))
    unitfmt = {a: ("min" if it["k"] == "mins" else "s") for it, a in zip(items, ans)}
    P = code_items_page(26, 4626, "Seconds", 1, "Time: seconds, minutes and seconds", STRAND_ME,
        "2.1 (measuring time in seconds)", ["TI2.1"], "Code-breaker (stopwatch)",
        ["Read the stopwatch or work out each answer.", "Write the answer in the box.", INSTR_CODE],
        qgrid(cards[:2], 2, "sw") + '<div style="height:3mm"></div>' + qgrid(cards[2:], 2), ans, table, word, 0, 600,
        "; ".join(f"{i+1}) {a} {unitfmt[a]}" for i, a in enumerate(ans)),
        "Two stopwatch faces (a seconds hand, a mark every second and a number every 5 seconds; the second also says that one minute has passed), a minutes-and-seconds measure changed to seconds, the number of seconds in some minutes, a story, and seconds changed to minutes. The decoy letters stand for reading the wrong mark, writing a minute as a hundred seconds, or adding the minutes to the seconds. A real stopwatch is not possible on paper. A box left blank gives no letter and the check cannot see it.")
    solved = []; si = 0
    for it, t in zip(items, texts):
        k = it["k"]
        if k in ("dial", "dial1"): v = A3.read_stopwatch(svgs[items.index(it)]); solved.append(v if k == "dial" else 60 + v)
        elif k == "conv": m_, s_ = re.search(r"in (\d+) min (\d+) s", t).groups(); solved.append(int(m_) * 60 + int(s_))
        elif k == "inmin": solved.append(int(re.search(r"in (\d+) minutes", t).group(1)) * 60)
        elif k == "song": m_, s_ = re.search(r"lasts (\d+) min (\d+) s", t).groups(); solved.append(int(m_) * 60 + int(s_))
        else: solved.append(int(re.search(r"are (\d+) seconds", t).group(1)) // 60)
    P.v("V1 independent solver (stopwatch needle angle and printed words read back) equals the key", solved == ans, solved)
    P.v("V7 seconds within 600; stopwatch readings on a numbered 5-second mark", max(ans) <= 600 and all(it["s"] % 5 == 0 for it in items if it["k"].startswith("dial")))
    return P

# =============================================================================== P3-27 The 24-Hour Clock (lettered choice)
def page27():
    rng = random.Random(4727)
    while True:
        times = []
        kinds = ["clock", "d12", "d24", "clock", "d12"]
        rng.shuffle(kinds)
        for kd in kinds:
            h = rng.choice([x for x in range(1, 24) if x not in (12, 0)]); m = rng.choice([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 0, 12, 18, 24, 36, 48, 54])
            times.append(h * 60 + m)
        if len(set(times)) < 5 or len({t // 60 % 12 for t in times}) < 5: continue
        break
    specs = []
    for kd, t in zip(kinds, times):
        h, m = divmod(t, 60); pm = h >= 12
        if kd in ("clock", "d12"):
            opts = [h24(t), h24(t - 720 if pm else t + 720), h24(t + 120 if h < 22 else t - 120)]
        else:
            opts = [ampm(t), ampm(t - 720 if pm else t + 720), ampm(t + 120 if h < 22 else t - 120)]
        if kd == "clock":
            hh = h % 12 or 12
            q = f'<div class="clk30">{A2.clock_svg(hh, m)}</div><span class="qs">{"in the morning" if not pm else "in the afternoon or evening"}</span>'
        elif kd == "d12": q = f'<p class="qb">{ampm(t)}</p><span class="qs">Write in the 24-hour clock.</span>'
        else: q = f'<p class="qb">{h24(t)}</p><span class="qs">Write in the 12-hour clock.</span>'
        specs.append(dict(q=q, opts=[f'<b class="on">{o}</b>' for o in opts], kind=kd, t=t, right=opts[0]))
    # the d24 rows: the stem is the 24-hour time, options 12-hour
    P = lettered_choice_page(27, 4727, "The 24-Hour Clock", 1, "Time: the 24-hour clock", STRAND_ME,
        "2.3 (24-hour clock)", ["TI2.3"], "Lettered choice (24-hour clock)",
        ["Match each time to the same time written another way.", "Circle the letter of the right choice.", "Write the five letters in the boxes."],
        specs, 3, "; ".join(f"{i+1}) {ampm(s['t'])} = {h24(s['t'])}" for i, s in enumerate(specs)),
        "Five rows: two analogue clocks (with the part of the day written beside them), two times in the 12-hour clock to write in the 24-hour clock and one 24-hour time to write in the 12-hour clock. In the 24-hour clock the day is counted from midnight and every time is written with four digits and the letter h. The wrong choices are the same time in the other half of the day, the hour and the minutes swapped, or a time ten minutes or two hours away. The letters of the right choices, read down the rows, spell the word. Every other way of choosing was tested against a very large word list: none spells a word. A box left blank gives no letter and the check cannot see it.",
        word_len=5, rng=rng, row_cls="clockrow")
    P["check_boxes"] = 5
    def solver(q, opts):
        o = [re.search(r">([^<]*)<", x).group(1) for x in opts]
        if "clk30" in q:
            h_, m_ = A2.read_clock(q); pm = "afternoon" in q
            mins = (h_ % 12 + (12 if pm else 0)) * 60 + m_
            return [unh24(x) if x.endswith(" h") else unampm(x) for x in o].index(mins)
        m1 = re.search(r'class="qb">([^<]*)<', q).group(1)
        if m1.endswith(" h"): mins = unh24(m1)
        else: mins = unampm(m1)
        return [unh24(x) if x.endswith(" h") else unampm(x) for x in o].index(mins)
    got = solve_letters(solver, P["body"])
    P.v("V1 independent solver (clock hands read from the drawing, times converted) gets the word", got == P["word"], got)
    P.v("V7 times are on the 24-hour clock, 0100 h to 2359 h, none at noon", all(60 <= s["t"] < 1440 and s["t"] != 720 for s in specs))
    return P

# =============================================================================== P3-28 Start, Finish, How Long (lettered choice)
def page28():
    rng = random.Random(4828)
    while True:
        rows = []
        kinds = ["finish", "start", "dur", "finish", "dur", "start"]
        rng.shuffle(kinds)
        for kd in kinds:
            t1 = rng.randrange(6 * 60 + 5, 17 * 60, 5); d = rng.choice([35, 40, 45, 50, 55, 65, 70, 85, 95, 105, 110, 125, 135, 140]); t2 = t1 + d
            nm = rng.choice(PEOPLE); th = rng.choice(["film", "concert", "match", "lesson", "class", "show"])
            rows.append(dict(k=kd, t1=t1, d=d, t2=t2, nm=nm, th=th))
        if len({(r["t1"], r["d"]) for r in rows}) < 6: continue
        break
    specs = []
    for r in rows:
        if r["k"] == "finish":
            q = f"<p>The {r['th']} starts at {ampm(r['t1'])} and lasts {hm_text(r['d'])}. At what time does it end?</p>"
            right = ampm(r["t2"]); wrongs = [ampm(r["t2"] + 40 if (r["t1"] % 60 + r["d"] % 60) >= 60 else r["t2"] - 40), ampm(r["t2"] - 60)]
        elif r["k"] == "start":
            q = f"<p>{r['nm']}'s {r['th']} ends at {ampm(r['t2'])}. It lasts {hm_text(r['d'])}. At what time did it start?</p>"
            right = ampm(r["t1"]); wrongs = [ampm(r["t2"] + r["d"]), ampm(r["t1"] + 40 if r["t1"] % 60 < 20 else r["t1"] - 40)]
        else:
            q = f"<p>A {r['th']} starts at {ampm(r['t1'])} and ends at {ampm(r['t2'])}. How long is it?</p>"
            right = hm_text(r["d"]); wrongs = [hm_text(r["d"] + 40 if r["d"] % 60 < 20 else r["d"] - 40), hm_text(r["d"] + 60 if r["d"] < 100 else r["d"] - 10)]
        wrongs = [w for w in dict.fromkeys(wrongs) if w != right]
        k = 0
        while len(wrongs) < 2:
            k += 10
            cand = hm_text(r["d"] + k) if r["k"] == "dur" else ampm((r["t2"] if r["k"] == "finish" else r["t1"]) + k)
            if cand != right and cand not in wrongs: wrongs.append(cand)
        specs.append(dict(q=q, opts=[f'<b class="on">{right}</b>'] + [f'<b class="on">{w}</b>' for w in wrongs[:2]], row=r, right=right))
    P = lettered_choice_page(28, 4828, "Start and Finish", 2, "Time: start, finish and how long it takes", STRAND_ME,
        "2.2 (finding the starting time, finishing time or duration given the other two quantities)", ["TI2.2"], "Lettered choice (start, finish, duration)",
        ["Find the time or how long.", "Circle the letter of the right choice.", "Write the six letters in the boxes."],
        specs, 3, "; ".join(f"{i+1}) {s['right']}" for i, s in enumerate(specs)),
        "Six stories: two ask when something ends (start and how long), two ask when it started (end and how long) and two ask how long it took (start and end). Times are written with am and pm; some go past the hour, some go past noon. The wrong choices are the usual slips: counting a hundred minutes in an hour, adding where the story takes away, and a time out by an hour or by forty minutes. The letters of the right choices, read down the rows, spell the word. Every other way of choosing was tested against a very large word list: none spells a word. A box left blank gives no letter and the check cannot see it.",
        rng=rng, row_cls="sfrow")
    def solver(q, opts):
        o = [re.search(r">([^<]*)<", x).group(1) for x in opts]
        t = re.sub(r"<[^>]+>", "", q)
        times = [unampm(x) for x in re.findall(r"\d+:\d\d (?:am|pm)", t)]
        if "How long" in t:
            return o.index(hm_text(times[1] - times[0]))
        d = un_hm(re.search(r"(?:lasts|It lasts) (.+?)\. At", t).group(1))
        if "At what time does it end" in t: return o.index(ampm(times[0] + d))
        return o.index(ampm(times[0] - d))
    got = solve_letters(solver, P["body"])
    P.v("V1 independent solver (times and lengths read back from the printed story) gets the word", got == P["word"], got)
    P.v("V7 every duration is under 3 hours and every time is between 6:00 am and 8:00 pm", all(r["d"] < 180 and 360 <= r["t1"] and r["t2"] <= 20 * 60 for r in rows))
    P.v("V1b the three choices in a row are different", all(len({re.search(r">([^<]*)<", o).group(1) for o in s["opts"]}) == 3 for s in specs))
    return P

# =============================================================================== P3-29 Time Detective
def page29():
    rng = random.Random(4929)
    while True:
        a_d = rng.randrange(8 * 60, 9 * 60, 5); a_dur = rng.choice([70, 85, 95, 105]); a_a = a_d + a_dur
        b_d = a_a + rng.choice([55, 70, 80, 95]); b_dur = rng.choice([65, 75, 80, 100]); b_a = b_d + b_dur
        c_d = rng.randrange(13 * 60, 15 * 60, 5); c_dur = rng.choice([115, 125, 135, 145]); c_a = c_d + c_dur
        d_a = rng.randrange(9 * 60, 11 * 60, 5); d_dur = rng.choice([140, 155, 165, 100]); d_d = d_a - d_dur
        e_d = rng.randrange(18 * 60 + 10, 20 * 60, 5); e_dur = rng.choice([150, 170, 185, 205]); e_a = e_d + e_dur      # same day: no journey crosses midnight (audit L4)
        wait = b_d - a_a
        items = [("dur", "A", a_dur, "min"), ("dur", "B", b_dur, "min"), ("arr", "C", c_a, "h"), ("dep", "D", d_d, "h"), ("dur", "E", e_dur, "min"), ("wait", "AB", wait, "min")]
        tm = lambda m: ((m // 60) % 24) * 100 + m % 60
        ans = [a_dur, b_dur, tm(c_a), tm(d_d), e_dur, wait]
        if not distinct(ans) or any(v >= 400 for v in (a_dur, b_dur, e_dur, wait)): continue
        timeset = {tm(c_a), tm(d_d)}
        pool = set()
        for v in (a_dur, b_dur, e_dur, wait): pool |= {v + 10, v - 10, v + 40, v - 40, v + 60, v - 60, v - 20, v + 20}
        for m_ in (c_a, d_d): pool |= {tm(m_ + 40), tm(m_ - 40), tm(m_ + 60), tm(m_ - 60), tm(m_) + 40 if tm(m_) % 100 < 20 else tm(m_) - 40}
        pool = sorted(x for x in pool if x not in ans and 0 < x < 2360 and (x < 400 or x % 100 < 60))
        res = find_table(29, 6, ans, rng, 0, 2359, pool, n_decoy=3, tries=12)
        if res: word, table = res; break
    fmtv = lambda v: f"{v:04d} h" if (v in timeset or v >= 400) else f"{v} min"
    t24 = lambda m: f"{(m // 60) % 24:02d}{m % 60:02d}"
    rows_t = (f'<tr><td>A</td><td>{t24(a_d)} h</td><td>{t24(a_a)} h</td></tr><tr><td>B</td><td>{t24(b_d)} h</td><td>{t24(b_a)} h</td></tr>'
              f'<tr><td>E</td><td>{t24(e_d)} h</td><td>{t24(e_a)} h</td></tr>')
    table_html = f'<table class="tt"><tr><th>Bus</th><th>Leaves</th><th>Arrives</th></tr>{rows_t}</table>'
    qs = [f"How many minutes does Bus A take?", f"How many minutes does Bus B take?",
          f"Bus C leaves at {t24(c_d)} h. The journey takes {hm_text(c_dur)}. At what time does it arrive?",
          f"Bus D arrives at {t24(d_a)} h. The journey takes {hm_text(d_dur)}. At what time did it leave?",
          f"How many minutes does Bus E take?", f"Bus B leaves after Bus A arrives. How many minutes is the wait?"]
    cards = [qcard(i + 1, f"<p>{q}</p>", f'<span class="ab w4"></span> <b>{"h" if i in (2, 3) else "min"}</b>') for i, q in enumerate(qs)]
    pre = f'<div class="blk"><p class="lead">The 24-hour clock timetable. Times are four digits, for example 0915 h.</p>{table_html}</div>'
    P = code_items_page(29, 4929, "Time Detective", 2, "Time: the 24-hour clock, start, finish and how long", STRAND_ME,
        "2.2, 2.3 (starting time, finishing time or duration; 24-hour clock)", ["TI2.2", "TI2.3"], "Code-breaker (timetable)",
        ["Use the timetable and the questions.", "Write each answer in the box.", INSTR_CODE],
        qgrid(cards, 2), ans, table, word, 0, 2359,
        "; ".join(f"{i+1}) {fmtv(a)}" for i, a in enumerate(ans)),
        "A timetable of buses in the 24-hour clock (four digits, with h). Questions: how long three journeys take, when a journey that leaves at a given time and takes a given time arrives, when a journey that arrives at a given time and takes a given time left, and the wait between two buses. Answers that are times are written with four digits (a leading zero for the early hours); answers that are lengths are in minutes. The decoy letters stand for counting a hundred minutes in an hour, or for an hour out. A box left blank gives no letter and the check cannot see it.",
        pre_body=pre, fmt=fmtv, domain=None)
    P["instr"] = ["Use the timetable and the questions.", "Write each answer in the box. A time has four digits.", INSTR_CODE]
    tt = {}
    for row in re.findall(r"<tr><td>(\w)</td><td>(\d{4}) h</td><td>(\d{4}) h", P["body"]): tt[row[0]] = (int(row[1][:2]) * 60 + int(row[1][2:]), int(row[2][:2]) * 60 + int(row[2][2:]))
    solved = []
    for q in qs:
        m = re.match(r"How many minutes does Bus (\w) take\?", q)
        if m: d, a = tt[m.group(1)]; solved.append((a - d) % 1440); continue
        if "wait" in q: solved.append(tt["B"][0] - tt["A"][1]); continue
        m = re.match(r"Bus C leaves at (\d\d)(\d\d) h\. The journey takes (.*?)\. At what time does it arrive", q)
        if m: solved.append(((int(m.group(1)) * 60 + int(m.group(2)) + un_hm(m.group(3))) // 60 % 24) * 100 + (int(m.group(1)) * 60 + int(m.group(2)) + un_hm(m.group(3))) % 60); continue
        m = re.match(r"Bus D arrives at (\d\d)(\d\d) h\. The journey takes (.*?)\. At what time did it leave", q)
        t = int(m.group(1)) * 60 + int(m.group(2)) - un_hm(m.group(3)); solved.append((t // 60) * 100 + t % 60)
    P.v("V1 independent solver (timetable and questions read back, clock arithmetic done in minutes) equals the key", solved == ans, solved)
    P.v("V7 times are real times of the 24-hour clock; the six answers are all different; no journey is longer than 4 hours", max(x for x in [a_dur, b_dur, c_dur, d_dur, e_dur]) <= 240 and distinct(ans))
    return P

PAGES = [page26, page27, page28, page29]
