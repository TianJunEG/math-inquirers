# DRAFT, NOT PUBLISHED: free preview class deck, Level 3 (ages 8-10), 60 minutes

Prototype for `docs/preview_class_design.md` (section 3). Not uploaded to Claude Slides, not shown to anyone, not linked from the website.

- `gen_preview_l3.py` writes `project/deck.json` and `project/slides/*.html` (16 slides, same structure as `split/l6s`, the 60-minute trial deck). Re-run it, then `python3 levels/restyle.py split/preview_l3` twice (the second run changes 0 files).
- Mi (title, break, last slide only) carries a `/_blob/PENDING-<pose>` placeholder image: no asset has been uploaded. `levels/mi_deco.py` does not touch this deck (folder name does not match its key pattern), so the placeholders stay until a publish step supplies real blob ids.
- Slide 3 ("Warm-up of the week") is the only slide that changes from week to week. It takes one Level 3 puzzle from the daily teaser bank.
- All answers were worked by hand: (8, 7, 9, 5, 6 and 87) were checked by a script and by hand; see design section 3.9.
