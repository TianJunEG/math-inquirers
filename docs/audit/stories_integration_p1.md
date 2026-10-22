# Math Inquirers Level 1 (p1): mathematician stories integrated

Date 2026-10-22. Source: docs/stories/final_p1.json. Nothing committed or published. Other levels, levels/*, hp/parent_pack*.py and hp/qbank.py not touched.

## Changes
- New data file `hp/stories_p1.json`: per lesson name, short place, country, years, 66-80 word child version of the story, 2-sentence workbook blurb, link, try-it q/a, confidence, legend flag.
- Decks: new module `rebuild/p1stories.py`, called at the end of `rebuild/gen_l1.py` to `gen_l10.py` (after p1round2, so it survives regeneration). Adds slide `lK-story` "Story break: <name>" straight after `lK-break` (37-39 MIN, optional, "we can skip it"). Story in 40px text, person/place/years card, try-it card (click to show), answer and link only in the speaker notes, skip instruction in the notes. The break slide notes gain one sentence pointing to it. Legends: Euler (cats example is ours) and Ramanujan (taxi 1729 is a story Hardy told himself) are labelled on the slide.
- Tutor script: `hp/scripts.js` gets a `story` line per lesson ("Story break (optional, 2 minutes): ... SKIP: ..."), printed in `hp/guide.js` at the 35-40 Brain break.
- Workbook: "Story corner" box (blurb, try-it, "My answer" line, no answer) at the bottom of each Choose-then-look-back page (`hp/workbook_html.js`, `hp/workbook.js`). Placing it on the Start here pages overflowed 8 lessons, so it sits on the Choose page.
- Answer key: `hp/guide.js` adds a "Story break try-it" row in each lesson key.
- Guide: new "Mathematician stories" page (lesson, person, country, years, link) before the Progress tracker.
- Safeguarding wording and the Start here / Think harder / Go further names are unchanged.

## Rebuilt
Decks 1-10 (`python3 rebuild/gen_lK.py` then `python3 levels/restyle.py split/lK`); workbook HTML/PDF (58 pages, unchanged) and DOCX (61 pages, unchanged); tutor guide DOCX/PDF (75 -> 83 pages); weekly PDFs zip. Copies in outputs/workbook and outputs/designed.
Checks: `python3 docs/audit/verify_stories_p1.py` (all try-it answers computed, story word counts, answer not on slide); `rebuild/preview.py` shows no overflow on any story slide; the 10 Choose pages were viewed (box fits, no clipping); guide stories page and a brain-break page viewed.

## Left / notes
- No pictures on the slides (picture ideas in final_p1.json not drawn). Easy to add later.
- Newton years shown as 1642-1727 (source JSON said 1640s-1727). Check the date against your preferred style (1642 or 1643).
- Scheme of Work and Question Bank not rebuilt (no content change). The guide grew by 8 pages, mostly the extra script paragraph per lesson.
- Stories are not in qbank.json; the Weekly Dose is unaffected.
- Published Claude Slides decks need republishing from split/l1 to l10 (lead's step).
- Confidence "medium" stories (Neurath, Newton, Kepler's year detail aside, Euler, Al-Biruni, Ramanujan) are worth a human fact-check before families see them.
