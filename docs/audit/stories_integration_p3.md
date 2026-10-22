# Mathematician stories: Level 3 integration

Source: `docs/stories/final_p3.json` (10 lessons, one person each). Nothing committed or published.

## Data
- `p3/stories.json` (new): per lesson name, years, country, who, deck story (shortened to 79-98 words, still true, legends kept labelled), workbook blurb (2 sentences), link, try-it, answer, accuracy note. Lessons 1, 2, 7, 8 were shortened from 104/123/102/114 words; the others are unchanged.
- `docs/audit/stories_verify_p3.py` (new): checks every try-it answer in Python. All 10 pass (5 has two checks): L1 11,23,47,95,191; L2 A=5,B=1 only; L3 nines rod; L4 20 pearls; L5 23 and 17; L6 3/4 > 2/3; L7 25 > 24; L8 120 degrees; L9 6 hours, 1461 days; L10 Ana knight, Ben knave.

## Decks (split/p3l1..p3l10)
- `rebuild/p3_stories.py` (new), called from each `rebuild/gen_p3lK.py` right after `p3_gifted.add`. Adds slide `p3lK-story`, "Story break: <name>", directly after the brain-break slide and before the worksheet. Tag "STORY BREAK / 2 MIN", country and years line, story at 34 px, optional "TRY IT" card at 32 px. Speaker notes: skip instruction, who, link to the lesson, answer (tutor only), accuracy note. The brain-break slide notes now mention the optional story. Each deck gains 1 slide (28 to 31 slides).
- Regenerated with gen script then `levels/restyle.py`, then `levels/normfoot.py 3`. `rebuild/preview.py`: no OVERFLOW on any slide; lowest content on a story slide ends at y 880 (footer at about 990); notes 750-1073 characters.

## Tutor guide (`p3/guide.js`)
- Brain break section, every lesson: "Story break (optional, 2 minutes): ..." with the person, link and try-it, anyone may pass, no cold-calling, nothing marked, and "Skip it if you are short of time". Legend and uncertainty notes appear as a DO line, tutor only.
- Answer key, every lesson: "Story break try-it" line.
- New page "Level 3 stories: mathematicians" before the Progress tracker: table (lesson, person, country, years, link) plus a notes-on-accuracy list.
- Guide 83 to 93 pages. Checked pages 12 and 89-90 visually.

## Workbook (`p3/workbook_html.js`)
- "Story corner (optional)" box (name, 2-sentence blurb, Try it, dotted answer line, no answer) at the bottom of each lesson's Go further page. Page 2 of Start here was too full: placing it there pushed pages onto new sheets in L2, L4, L7, L8, and on Think harder L8 overflowed. Go further pages have room. Workbook stays 58 pages; checked pages 6, 21, 26, 41, 51 visually.

## Kept
Safeguarding wording and the Start here / Think harder / Go further / Investigation names are untouched.

## Left / notes
- `levels/build_level.sh 3` also regenerated the weekly PDFs zip, Weekly Dose and `levels/scheme.py p3`, which rewrote `outputs/schemes/Math_Inquirers_P3_Scheme_of_Work.pdf`. The P4 scheme pdf and `rebuild/p4_fix.py`, `p5_gaps.py` show as modified in git, but not from this work (another job running in the same tree).
- Story slides are not yet published to Claude Slides; `outputs/` copies of the P3 workbook and guide are not refreshed (only `p3/`).
- Time plan unchanged: the story sits inside the 35-40 brain break (movement about 3 minutes, story about 2). Lesson 6 and 9 stories say exact dates are unknown; L4 and L8 contain a labelled legend. The L2 link (letter puzzles) is our own, as noted in the guide.
- Parent-facing documents (weekly dose, taster) do not mention the stories.
