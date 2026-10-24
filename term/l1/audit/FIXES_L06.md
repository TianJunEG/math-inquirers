# Fixes for Lesson 6 after the independent workbook audit (22 Oct 2026)

Audit: `audit/WORKBOOK_AUDIT_L06.md`. Files changed: `lessons/l06.json`, `verify/l06_checks.py`, rebuilt `out/l06/`, `AUDIT_L06.md`. Validator 17 pass, 0 warn, 0 FAIL; 357 answer checks; workbook 6 pages, fill 93, 84, 87, 84, 96% (kit 91%).

| # | Sev | Audit finding | What was done |
|---|---|---|---|
| 1 | Medium | Investigation had no writing space | Fixed by the template (4 lines, commit 2379b77); checked on the rebuilt page 5. |
| 2 | Medium | E3 31 + 28 beyond P1 in the exit ticket | E3 is now "Mei is on 52. She jumps forward 2 tens, then hops forward 3." with blanks for 72 and 75 (the split is given). Checks, key, slide answers updated. 31 + 28 removed from the exit ticket. |
| 3 | Medium | T1, T2 no frame to draw on | T1 and T2 now have answer frames: a) Jump: 34 + ___ = ___, b) Hop: ___ + ___ = ___, c) So 34 + 25 = ___ (same for 68 - 24). No bare lines. |
| 4 | Medium | Go further mostly Think harder | G1 is now open: find two different routes from 7 to 97 with jumps of 10 or 20. G2 keeps fewest jumps and adds b) why 4 jumps are not enough. G3 ends on 69 with an unknown hop and asks for the one equal jump of 4 tens. Checks rewritten for open and multi-part items. |
| 5 | Low | S6 gave the answer away, "Right or Wrong" unprinted | a) is "Is Ben correct? Circle Yes or No." (printed choices); c) is "Ben added 2 ___ by mistake. He should add 2 ___." (answer ones, tens). |
| 6 | Low | Sneak-peek Q1 same as S1 | S1 now shows 2 bundles and 7 singles (27, answer 37); sneak-peek stays 26 to 36. |
| 7 | Low | Three tens-pictures with no link | Page 1 hint says "A bundle of 10 is a bar in your kit"; S2 asks for tall bars. S1 stays as a bundle picture. |
| 8 | Low | Commands, page 2 no instruction line | "Fill in a to c" kept only where the parts are blanks or one circle; page 2 instruction line needs a template field (`hint_p2` does not exist): left, listed below. |
| 9 | Low | Investigation range open | Text says "start numbers from 0 to 50"; key lists 0, 10, 20, 30, 40 or 50 itself; the circle was changed to "Write Yes or No." |
| 10 | Low | Long stems | T3 now "Both frogs start on 12. ..." (shorter); G3 shortened. S2 is about 25 words, kept on purpose to teach the tall-bar drawing. |
| 11 | Low | Generic page-3 hint | `hint_p3` set for this lesson; `hint_p1` also set. |
| 12 | Low | Look-back print too small | Template (b_print.py): not edited. |
| 13 | Low | Mi holds a calculator | Owner-chosen image: report only. |
| 14 | Low | Key heading orphan (end of key p2) | Template: not edited; still present on key page 2. |
| 15 | Low | Siti always makes the mistake | S6 now Ben (workbook, slides, script, key). |
| - | Draw warnings | S2 and S7 over 25 strokes (template warning) | S2 now draws 3 + 4 + 2 = 9 strokes (tall bars); S7 about 10; `draw_strokes` set. Validator 0 WARN. |
| - | Owner decisions | Beyond-P1 statement, no MOE claim | Tutor guide strand note and parent summary now say plainly that Term 1 goes beyond the school P1 syllabus on purpose; no MOE-aligned claim. Start here stays inside P1, Think harder and Go further carry the stronger arithmetic. |
| - | Fill | Page 2 was 81% | S5 got a second working line: 84%. |

Not fixed (shared template or tool, for the owner): look-back type size and "I am still stuck" line (finding 12); key heading kept with its box (14); page-2 instruction line (no `hint_p2` field); the Mi calculator image (13); the fixed sneak-peek answer wording on key page 3 is now plain "36".
