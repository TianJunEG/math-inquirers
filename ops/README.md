# Operations kit (beta launch)

| What | File | How |
|---|---|---|
| Calendar invites (.ics per group, 10 lessons, reminders 1 day and 1 hour, Singapore time) | `ops/out/ics/*.ics` | `python3 ops/make_ics.py [--meet L1A=<link>] [--sequence N]`; test: `python3 ops/test_ics.py` (needs `pip install icalendar`). Meet links can also go in `ops/meet_links.json`. |
| Parent "add to calendar" page, make-up note, end-of-program reports L1 to L6 (PDF and .docx), tutor notes, observation sheet | `ops/out/*.pdf`, `ops/out/*.docx` | `python3 ops/make_docs.py` |
| Tutor agreement draft, WhatsApp message pack, launch checklist | `docs/ops/` | edit by hand |

Source of the schedule: `website/data/beta_schedule.json`. After a schedule change, rerun `make_ics.py` with `--sequence` one higher so calendars update.
