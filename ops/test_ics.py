#!/usr/bin/env python3
"""Parse every generated .ics with the `icalendar` package and check it against
website/data/beta_schedule.json.  Run: python3 ops/test_ics.py  (pip install icalendar)"""
import json, sys
from datetime import timedelta
from pathlib import Path
from icalendar import Calendar

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "website/data/beta_schedule.json").read_text())
bad = []


def check(c, msg):
    if not c:
        bad.append(msg)


for g in data["groups"]:
    p = ROOT / "ops/out/ics" / f"{g['id']}_math_inquirers_beta.ics"
    cal = Calendar.from_ical(p.read_bytes())
    evs = [e for e in cal.walk("VEVENT")]
    check(len(evs) == 10 == len(g["lessons"]), f"{g['id']}: event count {len(evs)}")
    uids = {str(e["UID"]) for e in evs}
    check(len(uids) == 10, f"{g['id']}: UIDs not unique")
    for e, l in zip(sorted(evs, key=lambda e: e["DTSTART"].dt), g["lessons"]):
        s, en = e["DTSTART"].dt, e["DTEND"].dt
        check(str(s.tzinfo) in ("Asia/Singapore", "+08") or s.utcoffset() == timedelta(hours=8), f"{g['id']} L{l['n']} tz {s.tzinfo}")
        check(s.strftime("%Y-%m-%d %H:%M") == f"{l['date']} {l['start']}", f"{g['id']} L{l['n']} start {s}")
        check(en - s == timedelta(minutes=90), f"{g['id']} L{l['n']} length")
        check(s.strftime("%a") == l["day"], f"{g['id']} L{l['n']} weekday {s:%a} vs {l['day']}")
        check(s.strftime("%m-%d") != "12-25", f"{g['id']} lesson on 25 Dec")
        trig = sorted(a["TRIGGER"].dt for a in e.walk("VALARM"))
        check(trig == [timedelta(days=-1), timedelta(hours=-1)], f"{g['id']} L{l['n']} alarms {trig}")
        check("Meet" in str(e["DESCRIPTION"]), f"{g['id']} L{l['n']} no Meet text")
        check(bool(l.get("moved")) == ("public holiday" in str(e["DESCRIPTION"])), f"{g['id']} L{l['n']} moved note")
    moved = [e["DTSTART"].dt.strftime("%a %d %b") for e in evs if "public holiday" in str(e["DESCRIPTION"])]
    check(len(moved) == (1 if g.get("week5_exception") else 0), f"{g['id']} moved lessons {moved}")
    print(g["id"], "ok" if not bad else "FAIL", moved)

al = Calendar.from_ical((ROOT / "ops/out/ics/all_groups_tutor.ics").read_bytes())
check(len(list(al.walk("VEVENT"))) == 10 * len(data["groups"]), "tutor file count")
if bad:
    print("\n".join(bad)); sys.exit(1)
print("ALL OK:", len(data["groups"]), "groups x 10 lessons, 1-day and 1-hour reminders, Singapore time")
