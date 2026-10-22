# Self-audit: Level 1 Term 1 Lesson 1 (Bundles and Singles)

Desk audit by the author (a model); no child has used this lesson. Rubric: the project's holiday-lesson audits (`docs/audit/audit_p1.md`, `reaudit_p1.md` instruments A and tier compliance, `timing_p1.md`, `fixpass_brief_template.txt`). Machine checks: `python3 term/l1/tools/validate.py 01` (15 pass, 0 FAIL; 1 warning explained below).

## Pass/fail checklist

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | Schema valid (JSON Schema + key checks) | PASS | validator |
| 2 | Every answer verified independently | PASS | 60 checks in `verify/l01_checks.py` (sticks counted, numbers enumerated, all 90 digit swaps) |
| 3 | Online practice variants verified | PASS | 225 variants: expression = brute-force oracle = runner JavaScript `calc`. Found and fixed a runner limit: `//` only works as the whole expression (`n//10+1` failed in the browser), now `derive` + `w+1` |
| 4 | Timing sums to exactly 90; no part OVER | PASS | 11 parts, 0-90; script needs 73:10; slow-class 86:54 |
| 5 | Timing is realistic for ages 6-8 | PASS with caveat | model, not stopwatch (speech 120 wpm, 25 s per slide, 30 s per question). Start here needs about 14.5 min for a middle child; a slower child may finish page 1 and part of page 2. No breakout rooms |
| 6 | Tier principle | PASS | Start here: build, count, write, spot a mistake (approachable, explored in class). Think harder: opening a bundle (5 tens 14 ones), digit-clue puzzle, equal-claim. Go further: compare after opening, two-step shop, count the ways. No contest-style item at Start here |
| 7 | Neutral labels, nothing named publicly | PASS | validator bans Core/Challenge/Stretch/etc.; whole-group invitations; choice line on page 1 |
| 8 | Sneak-peek: access Q + thinking Q, unmarked, papers shown once | PASS | slide 7, script lines, guide |
| 9 | No private chat; safeguarding block | PASS | script, guide, notes; Lesson 1 has no breakout rooms |
| 10 | No overclaims (MOE-aligned, GEP, SASMO prep) | PASS | validator on child and parent text; strand label is tutor-only |
| 11 | Ruler only if child has one | PASS | Lesson 1 needs none |
| 12 | Materials home-findable | PASS | paper clips, pasta, buttons, hair ties; kit page cut out by a grown-up |
| 13 | Recording cues short, with child action | PASS | 11 cues, at most 26 words |
| 14 | Joining cold | PASS | Remember covers counting in tens, bonds to 10, ten and some more; needs only counting to 20 |
| 15 | No copied contest text | PASS | no 7-word overlap with SASMO analysis/notes or books; all problems original |
| 16 | Layout | PASS | 31 slides, no overflow reported; workbook 6 pages; guide 18 pages; home 2; parent 1 (all viewed) |
| 17 | Printed answers separate | PASS | key is its own PDF |
| 18 | Reading load | WARN | the home Q5 and the sneak-peek puzzle 2 are longer than 40 words or near it. The tutor reads every question aloud in class; home Q5 is for a grown-up to read |

## Instrument A (gifted-style, 0 to 2 each)

1 low floor high ceiling 2; 2 depth over speed 2; 3 generalise 2 (Investigation swap the digits, G3 count the ways); 4 justify 2 (S6, T4, talk question); 5 multiple paths 1 (opening a bundle versus recounting, only one contrast); 6 challenge ladder 2; 7 student-led inquiry 1 (explore is hands-on but tutor-led rounds); 8 complexity/context 1; 9 problem posing 1 (what-if card and online G4 only; no make-your-own in the workbook); 10 metacognition 2; 11 pacing/compacting 1 (choice after Q3, but a lockstep deck); 12 extension not acceleration 2 (the hundred only as an optional teaser). **Total 19/24**, level mean of the holiday course was 19.8. Honest gaps: 5, 7, 8, 9, 11 are the same weak spots the holiday audits found.

## Known limits (not failures)

- Never trialled with children; times and difficulty are modelled.
- The hardest item for a 6-year-old reader is S6 (spot the mistake, one sentence to write). The tutor reads it aloud; a spoken answer is acceptable.
- Workbook is lesson-specific pages; there is no term cover or journal page yet (belongs to a term pack).
- Slide text is 34 to 44 px on a 1920 canvas: readable, with spare space; decks could use larger pictures.
- MOE strand sub-clauses are not cited by number (plan note: label only).

## Update (workbook fill and spare-time menu)

- Workbook: larger writing space (lines 8 mm, drawing boxes 105 px, 18.5 px text); Start here page 2 gained S7 (Ali 6 tens, Mei 6 ones; guide, slides, script timing, key and answer checks updated). Page fill now 99%, 100%, 96%, 92%, 94% (kit page excluded), PDF still 6 pages. Investigation writing space on page 5 is small (one line); children may use spare paper.
- Spare-time menu added (3 activities, 11 optional minutes, not in the 90 sum), optional menu slide, guide section 3b. Script now needs 74:22, slow class 88:19.
