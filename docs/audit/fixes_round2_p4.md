# P4 round-2 fixes (from docs/audit/reaudit/reaudit_p4.md)

Not committed, not published. Only P4 files were changed. Shared files (levels/mkextras.py, levels/scheme.py, levels/build_level.sh, hp/*, rebuild/slidekit.py) were not edited.
Rebuilt: all 10 decks (gen_p4l1..10.py, then `python3 levels/restyle.py split/p4lN`), then `bash levels/build_level.sh 4` (workbook PDF, tutor guide docx and PDF, weekly PDFs, weekly dose, scheme).
Workbook is now 61 pages (was 64): the three spill pages are gone. Tutor guide 82 pages. Weekly dose 25.
All changed answers are checked in `docs/audit/verify_fixes_round2_p4.py` (passes). Slide geometry was compared with the pre-fix decks (commit 85c14a6) for all 285 slides: only L6 teachclock and teachrobot changed, both now shorter, none overflow, no notes over 4000 characters.

## Fixes

| Finding | Fix | Files |
|---|---|---|
| N1 L2 stretch note "61 357" | Now "best above 60 000 is 71 359, which is 11 359 above, so 59 731 wins" (59 731 is 269 below 60 000; checked by brute force over all 120 arrangements of 1, 3, 5, 7, 9) | rebuild/gen_p4l2.py |
| N2 "Think harder Qx" in challenge-slide notes | "Go further Qx" in L1, L2, L3, L4, L7, L9, L10. Q numbers re-checked against the printed Go further page (Q5 to Q7) and the slide items: all match | rebuild/gen_p4l1,2,3,4,7,9,10.py |
| N3 two Go further questions in explore notes | The old "Go further (on the slide), for any child who wants it: ..." sentence is removed in every lesson; only the new GO FURTHER sentence remains (asserted in the build) | rebuild/p4_fix.py |
| N4 "After question 3" on L6 and L9 | New field `chooseAfter: 2` in the L6 and L9 gaps. It drives the printed page-1 line, the ws1 slide, the title time plan, the sneak-peek and CHOOSING notes and both tutor-guide paragraphs. Other lessons stay at 3 | p4/content/l6.js, l9.js, p4/workbook_html.js, p4/guide.js, rebuild/p4_fix.py |
| N5 page spill (L1 Q6, L2 Q3, L6 Q2) | L1: Q5 table rows 130 to 60, Q6 steps merged into one block. L2: table rows 50 to 40, "Try next" and Q2a lines merged. L6: page-1 figures smaller, table rows 90 to 56. Every lesson is now exactly 2 core pages. New test `rebuild/p4_pagecheck.py` fails if any lesson has a third core page or lacks "Page 1" / "Page 2 is on your own" | p4/content/l1.js, l2.js, l6.js, rebuild/p4_pagecheck.py |
| N5 "Page 1/Page 2" vs footer numbers | Printed line now reads "Page 1: Start here." (page 2 already says "Page 2 is on your own"). ws1 slide notes tell the tutor to say "the page with the lesson title" and "the page that says Page 2 is on your own", not a footer number | p4/workbook_html.js, rebuild/p4_fix.py |
| N6 safeguarding | Paper-to-camera practice kept as is. Removed every "private chat / DM / private message / message a child privately / direct message" phrase from the slide notes and the tutor guide (slides, guide checked: 0 matches). Added no channel. See "Left" below for one word |  rebuild/p4_fix.py, p4/guide.js |
| N7 L3 Q5 and Q7 on OPTIONAL slides | trytrick is now a timed, unmarked 1-minute demo (55 to 56); the bar model is 56 to 58. teachchain (Q7, a "choice" question) is ON DEMAND after page 2 starts, and the Q7 page now carries the hint ("two neighbours known? work backwards; gaps in the middle? guess the 2nd number, test, adjust"), so it can be done without the slide | rebuild/gen_p4l3.py, p4/content/l3.js |
| N8 L5 warm-up | "Play 3 rounds" replaced by "Play ONE round only (target 5), about 2 minutes", rounds 2 and 3 for take-home | rebuild/gen_p4l5.py |
| N9 headings "?." and "!." | The Investigation heading adds a full stop only if it does not already end in ? ! or . (L7 and L9 fixed) | p4/workbook_html.js |
| N9 L9 Investigation (b) overlaps Go further Q7 | (b) is now "write TWO TRUE headlines about 50 then 100: one that sounds big, one that sounds small"; (c) asks which headline to trust and what to ask the newspaper to add. No scale-choosing left in the Investigation (that stays in Go further Q7). Intro and model answer rewritten | p4/content/l9.js |
| N10 dense teach block L4, L5, L7 | Now two taught ideas in five minutes, the third is an ON DEMAND slide shown only if a child chooses that choice question (L4 Q6 find ALL; L5 Q6 mass puzzle, and the Think harder Q4 mystery decimal slide; L7 Q6 frame). L4 53 to 55 compare, 55 to 57 whole from a part, 57 to 58 optional check; L5 53 to 55 closest to a target, 55 to 58 bar model; L7 53 to 55 staircases, 55 to 57 cut and move, 57 to 58 optional check. L7 try3 (c) changed so it no longer practises the on-demand idea. Title notes and tutor guide explain ON DEMAND | rebuild/gen_p4l4,5,7.py, rebuild/p4_fix.py, p4/guide.js |
| N10 L6 teachclock 6 degrees per minute | Step 4 and the 6:05 to 6:20 answer removed from the slide, notes say only whole clock spaces are used today. tryclock (c) is now "angle at 1 o'clock" (30). Think harder S3 answer now says 7 jumps of 5 minutes at 30 each (210), no 6-per-minute formula. Objective text (content, title slide, guide) no longer mentions the minute hand or working backwards | rebuild/gen_p4l6.py, p4/content/l6.js |
| L6 page 2 has 10 sub-parts | Now 6: Q3 a b (4 and 7 o'clock), Q4 a b (Ali W+90 cw = N, Mei SW 135 acw = E), Q5 one angle (90 - 58 = 32; figure now shows the rectangle only), Q6 robot (SW). Key, ws2 and ws2ans slides, teachrect and teachrobot slides (work-backwards block removed) and the guide key updated | p4/content/l6.js, rebuild/gen_p4l6.py |
| L5 2 d.p. rounding in core | The only core item was the optional mini-lesson slide try2 (a): now "Round 5.38 to 1 decimal place" = 5.4. Objective says 2 d.p. rounding is only in Go further | rebuild/gen_p4l5.py, p4/content/l5.js |
| N11 L10 timeline | End slide note now "Minutes 89 to 90" (label 89 to 90; exit 85 to 87, reflect 87 to 89 unchanged). "Think harder Q5 and Q6" now "Go further" | rebuild/gen_p4l10.py |

## Left, and why

- Safeguarding wording "Children show their answers PRIVATELY: written on their own paper and held to the camera ..." stays in the sneak-peek notes. It describes the existing paper-to-camera practice (kept as asked) and contains no private message or chat wording. N6's contradiction (everyone at once vs tutor only) is therefore unchanged.
- tutor guide "Setting up online" still says children may "take a photo and send it through the approved channel". That is older wording about the approved parent channel, not new, and I did not add or remove any channel. Worth a policy decision (it sits oddly beside "do not take photos").
- L6 items taken off page 2 (Q3c "both o'clock times with 30", Q4c "NE to S smallest turn", Q4d "Ravi works backwards", Q5b "square cut in three, 90-15-48 = 27") are not in the question bank. Not added, to keep the bank's printed order and the shared Question Bank build unchanged. Easy to add as bank items if wanted.
- Bank items not printed anywhere but still using the removed ideas: L6 stretch S8 ("minute hand turns 150 degrees ... 6 degrees every minute") and L5 challenge C0 (rounding to 2 d.p., Go further size). Left because they are bank-only and the 2 d.p. one is meant to be Go further.
- The L6 deck's own Stretch and Challenge slides (separate from the printed Think harder and Go further pages) were not changed; their notes carry no Q numbers.
- Journey and gifted scores (C2, C5, C7 at 1) are design limits, not defects. Not touched.
- Other lessons: no content change beyond the shared notes fixes above (L8 only gets the explore-note and page-line fixes).

## Shared-file issues (not edited)

1. `levels/mkextras.py` line 113 still says "inspired by research-based approaches used in gifted education"; the marketing text still uses "Think Harder / Challenge" names (N12). Decide whether to keep or soften.
2. `levels/build_level.sh` does not run a pagination check. `python3 rebuild/p4_pagecheck.py` (takes an optional PDF path) can be added after the workbook step; the same idea would work for P1 to P3 and P5, P6 with their own labels.
3. `rebuild/slidekit.py` / `hp/` untouched. Other agents committed my in-progress P4 files inside their WIP commits (ee6b3fd and earlier); I made no commit.

## Files changed
p4/content/l1.js, l2.js (layout only), l3.js, l5.js, l6.js, l9.js; p4/workbook_html.js; p4/guide.js; rebuild/p4_fix.py; rebuild/gen_p4l1.py, gen_p4l2.py, gen_p4l3.py, gen_p4l4.py, gen_p4l5.py, gen_p4l6.py, gen_p4l7.py, gen_p4l9.py, gen_p4l10.py; new rebuild/p4_pagecheck.py and docs/audit/verify_fixes_round2_p4.py. Regenerated: split/p4l1 to split/p4l10, p4 workbook (HTML, PDF), tutor guide (docx, html, PDF), weekly PDFs zip, weekly dose, scheme.
