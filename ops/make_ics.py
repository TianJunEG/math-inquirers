#!/usr/bin/env python3
"""Write one .ics calendar file per beta group (10 lessons each).

Reads website/data/beta_schedule.json (the single source of the schedule).
Output: ops/out/ics/<group id>_math_inquirers_beta.ics, plus
all_groups_tutor.ics (every session, for the tutor's own calendar).

Each lesson: Asia/Singapore time, 90 minutes, reminders 1 day and 1 hour before,
Google Meet link placeholder (replace with the real link per group).

Meet links: pass --meet L1A=https://meet.google.com/xxx-xxxx-xxx (repeatable) or
put {"L1A": "https://meet.google.com/..."} in ops/meet_links.json.
Re-run after the schedule changes. Event UIDs are stable, and SEQUENCE comes from
--sequence, so a re-sent file UPDATES the parent's events instead of duplicating them.
"""
import argparse, json, sys
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEDULE = ROOT / "website" / "data" / "beta_schedule.json"
OUT = ROOT / "ops" / "out" / "ics"
PLACEHOLDER = "[Google Meet link to be added]"
PRODID = "-//Math Inquirers//Beta calendar//EN"

VTIMEZONE = [
    "BEGIN:VTIMEZONE", "TZID:Asia/Singapore",
    "BEGIN:STANDARD", "DTSTART:19700101T000000",
    "TZOFFSETFROM:+0800", "TZOFFSETTO:+0800", "TZNAME:+08", "END:STANDARD",
    "END:VTIMEZONE",
]


BS = chr(92)


def esc(s):
    return (s.replace(BS, BS + BS).replace(";", BS + ";").replace(",", BS + ",")
            .replace(chr(10), BS + "n"))


def fold(line):
    """RFC 5545 folding at 75 octets."""
    b = line.encode("utf-8")
    if len(b) <= 75:
        return line
    out, cur = [], b""
    for ch in line:
        cb = ch.encode("utf-8")
        limit = 75 if not out else 74
        if len(cur) + len(cb) > limit:
            out.append(cur.decode("utf-8")); cur = b""
        cur += cb
    out.append(cur.decode("utf-8"))
    return "\r\n ".join(out)


def dt(date, hhmm):
    return datetime.strptime(f"{date} {hhmm}", "%Y-%m-%d %H:%M")


def fmt(d):
    return d.strftime("%Y%m%dT%H%M%S")


def alarm(trigger, text):
    return ["BEGIN:VALARM", "ACTION:DISPLAY", f"DESCRIPTION:{esc(text)}",
            f"TRIGGER:{trigger}", "END:VALARM"]


def event(g, lesson, meet, stamp, sequence):
    start, end = dt(lesson["date"], lesson["start"]), dt(lesson["date"], lesson["end"])
    link = meet or PLACEHOLDER
    n = lesson["n"]
    desc = [
        f"Math Inquirers, {g['name']}, lesson {n} of 10 (90 minutes, Singapore time).",
        f"Join on Google Meet: {link}",
        "Have ready: the workbook, a pencil and a rubber, and a few sheets of blank private paper.",
        "Your child may keep the camera off and may stay muted. Please do not hold paper up to the camera.",
        "If you cannot make it: tell us on WhatsApp +65 9880 5962. The lesson is recorded.",
    ]
    if lesson.get("moved"):
        desc.insert(1, "This lesson is moved because Fri 25 Dec is a public holiday.")
    lines = [
        "BEGIN:VEVENT",
        f"UID:mathinquirers-{g['id']}-L{n:02d}-{lesson['date']}@mathinquirers",
        f"DTSTAMP:{stamp}",
        f"SEQUENCE:{sequence}",
        f"DTSTART;TZID=Asia/Singapore:{fmt(start)}",
        f"DTEND;TZID=Asia/Singapore:{fmt(end)}",
        "SUMMARY:" + esc("Math Inquirers " + g["name"] + ": lesson " + str(n) + " of 10"),
        "DESCRIPTION:" + esc(chr(10).join(desc)),
        f"LOCATION:{esc('Google Meet (online)')}",
        "STATUS:CONFIRMED", "TRANSP:OPAQUE",
    ]
    if meet:
        lines.append(f"URL:{meet}")
    lines += alarm("-P1D", f"Tomorrow: Math Inquirers lesson {n} of 10")
    lines += alarm("-PT1H", f"In 1 hour: Math Inquirers lesson {n} of 10")
    lines.append("END:VEVENT")
    return lines


def calendar(name, events):
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", f"PRODID:{PRODID}", "CALSCALE:GREGORIAN",
             "METHOD:PUBLISH", f"X-WR-CALNAME:{esc(name)}", "X-WR-TIMEZONE:Asia/Singapore"]
    lines += VTIMEZONE
    for e in events:
        lines += e
    lines.append("END:VCALENDAR")
    return "\r\n".join(fold(l) for l in lines) + "\r\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--meet", action="append", default=[], metavar="ID=URL")
    ap.add_argument("--sequence", type=int, default=0, help="raise by 1 when re-sending changed files")
    ap.add_argument("--out", default=str(OUT))
    a = ap.parse_args(argv)
    data = json.loads(SCHEDULE.read_text())
    meets = {}
    mf = ROOT / "ops" / "meet_links.json"
    if mf.exists():
        meets.update(json.loads(mf.read_text()))
    for m in a.meet:
        k, _, v = m.partition("="); meets[k] = v
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    stamp = "20261023T000000Z"  # fixed so output is reproducible
    allev = []
    for g in data["groups"]:
        evs = [event(g, l, meets.get(g["id"]), stamp, a.sequence) for l in g["lessons"]]
        allev += evs
        p = out / f"{g['id']}_math_inquirers_beta.ics"
        p.write_bytes(calendar(f"Math Inquirers {g['name']}", evs).encode("utf-8"))
        print(p.relative_to(ROOT) if p.is_relative_to(ROOT) else p, len(evs), "events")
    p = out / "all_groups_tutor.ics"
    p.write_bytes(calendar("Math Inquirers beta, all groups (tutor)", allev).encode("utf-8"))
    print(p.name, len(allev), "events")


if __name__ == "__main__":
    sys.exit(main())
