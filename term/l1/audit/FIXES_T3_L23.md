# Fix pass, Term 3 Lesson 3 (lesson 23, Time Passes)

Changed: `lessons/l23.json`, `verify/l23_checks.py` (200 checks pass), `AUDIT_L23.md`, `out/l23/`. Validator 0 FAIL and 0 WARN (28 checks, built files included), leak check clean; workbook 5 pages, fill 97/92/92/90/99%; home sheet 99%; parent page 92%; parts 2/6/4/11/11/4/32/6/6/3/5 = 90; script 68:54, slow class 81:30, no part over. Not touched: shared tools, `l20.json`, other lessons.

Source audits: `WORKBOOK_AUDIT_L23.md` (W), `GUIDE_DECK_AUDIT_L23.md` (G), `HOME_PARENT_PRACTICE_AUDIT_L23.md` (H).

| Finding | Action |
|---|---|
| W1 / G1 Mi holds a calculator | Rebuilt: workbook page 1, deck, guide and parent page now use the no-calculator Mi (viewed page 1 and the parent page) |
| W2 clock hands at half past, minute-hand tip covers the numeral, one colour | The figure is a shared tool (`tools/figs3.py`): not edited, listed below. Data fix: S4 clocks enlarged (size 90) so the hour hand is easier to tell from the minute hand; checked at 70 dpi that B (6:30) is readable |
| W3 Investigation too small, "First:" has no blank | "First" now ends "It is ____ pm."; 4 ruled lines kept. A time-line strip and a drawing box were tried and removed: either spilled the look-back onto a sixth page or printed unreadable labels (the figure shrinks to a thumbnail on page 5). The look-back layout (ragged check boxes) is a shared tool: listed |
| W4 no time line in Start here | Not done: page 1 is 97% full and a line would spill; the time line is taught on `s-m2` and `s-m3` and used in G1. Low |
| W5 / page headers do not say pages 3 and 4 are for home | Added "Not finished? This page is for home too." to the page 3 and page 4 intro lines |
| W6 T2b (9:45 and half an hour) is a new step | Kept at Think harder on purpose: it is the taught idea (half an hour later, the hour changes) in a new setting (a quarter-time start); the hint now scaffolds it ("count on 15 minutes to the next hour, then 15 more"). Beyond-P1 statement already names quarter-time starts |
| W7 key "Watch for" lines wrong on S3 and S6 | S3: "Writing 8:30 (the start) or 9:00 (half an hour instead of 1 hour)"; S6: "Writing 8:00 for reading (the start) or 9:00 for painting (the start)" |
| W8 / G4 / H (term chain) L20 hand-off still says "print it a week before" and "a toy or real clock (optional)" | **Not mine** (`l20.json` is owned by the Term 2 fix agent). Needed in `l20.json` `parent.next_materials`, `s-end`, goodbye SAY and `tutor_prep`: the Term 3 book, the 6 clock hands cut out by a grown-up, keep the $1 tokens |
| W9 G2b "1 hour and half an hour" | "Another day the film is longer: 1 hour, then half an hour more." |
| W10 T4 stem repeats "shows" | "The table shows the zoo shows this afternoon." |
| W11 key Investigation count | `look_for` now says any order is fine and the count is for the tutor, not to be asked |
| W12 S1 empty clock face | Not changed (face guides are a shared figure); the key already accepts "short hand on 9, long hand on 12" |
| G2 clocks small on slides 13, 17, 19 | `s-m4` now shows four larger clocks (`size m`); question 4 and question 5 each have their own slide (`s-ws2`, new `s-ws2c`) with the script lines split to match. `s-ws1` keeps the `qs` layout (shared; one clock per question) and the tutor reads the times aloud, as `tutor_prep` says |
| G3 `s-menu` "why the hour changes at half past" | "Show a toy why half an hour after half past 5 is 6 o'clock." |
| G5 `s-choice` says "Quarter times" | "Starts at 4:15 and 9:45, going back, a zoo timetable" |
| G6 "papers to the camera 30 s" in the guide timing line | Printed by `tools/b_guide.py` (shared): listed |
| G7 notice order (recording starts, then notice) | Opening now in the exact final Term 1 order and words (hello with "Cameras can be on or off, as you like"; recording sentence with "keep your microphone and camera off"; microphone line with "Nobody holds paper up to the camera"; DO "Greet the whole group warmly. Do not use children's first names on the recording."); `tutor_prep` greeting line matches. The order of notice and recording is the owner's call for all of Term 3 |
| G8 `s-opt` repeats G3's structure | Both games end at 8:30 and children write each start time as well as who started first |
| G9, G10 warm-up tweaks (ten jump, highlight 6 and 12) | Not done: low value, the `numrow` and `number_line` figures have no highlight option |
| G11 "tilt the camera" | `tutor_prep` says to tilt to the table, not the room |
| Own review: Talk time model answer ("8:30 is a whole hour after 7:30") is the answer to E1 (start 7:30, 1 hour) | E1 is now 6:30 and 1 hour (answer 7:30); E3 is now a film that ended at 10:30 pm (answer 9:30 pm). `verify/l23_checks.py` pair registry and E checks updated; the pair check still shows no workbook or exit pair repeats a class pair |
| H1, H2 online `fields` item: shown answer "The answer is The film ends at 4 : 00.." and no slips | Runner (shared): listed |
| H3 online c5 slip says "quarter of an hour" | "15 minutes is half of half an hour. Half an hour is 30 minutes." |
| H4 Enter in the second box, H7 "Term 3" in the runner header, H8 phone wrap | Runner (shared): listed |
| H5 home sheet text only | Not done: the sheet is 99% full |
| H6 thin recording sentence on the parent page | `parent.next` now adds that the recording has the tutor, the shared screen and any voice that is not muted, that the child may mute and keep the camera off, and that the link is private and not to be shared |
| H9 "Practice from earlier: Term 1 Lesson 3" on the child sheet | Printed by `tools/b_print.py` from `rewind_of` (shared; the verify script pins the value): listed |

Money: no "50c" in this lesson. Numbering: "Term 3 • Lesson 3" on the workbook, key, home and parent headers (viewed). Quarter times: none in Start here and none on child pages except the Think harder 4:15 and 9:45 as digits.

## Needs a shared-tool, runner or owner step

1. `tools/figs3.py` clock figure: draw the minute hand so it does not cover its numeral, make the hour hand shorter or a second shade, keep the two hands apart at half past.
2. `tools/b_guide.py`: remove "papers to the camera 30 s" from the timing assumptions.
3. `tools/b_print.py`: a rewind label that does not name a term lesson on the child sheet; the look-back check boxes wrap raggedly on page 5.
4. Runner: no stray capital and double full stop in the shown answer of a `fields` item; slips for `fields` items; Enter in every box; "Term 3" in the sub line; keep the frame and the two boxes on one row at 390 px.
5. Slides: a `qs` slide shows each question's figure as a thumbnail; a size option on `qs` would make the question 1 to 3 slide readable.
6. `l20.json` hand-off (above).
7. Mi's Challenge Quest gate C2 (`l30.json`) uses 2:30 with half an hour and 5:15 and 1 hour: the lesson keeps those numbers out of its own pages, but the gate repeats a Think harder idea; suggest 5:30 for the gate.
