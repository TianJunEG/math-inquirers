# Fix pass, Term 3 Lesson 1 (lesson 21, What Time Is It?)

Changed: `lessons/l21.json`, `verify/l21_checks.py` (158 checks), `AUDIT_L21.md`, `out/l21/`. Validator 0 FAIL, leak check clean; workbook fill 100/90/99/96/99%, kit page 64%; parts 4/6/4/12/10/4/30/6/6/3/5 = 90; script 68:41, slow class 81:18, no part OVER. Not touched: shared tools, `l20.json`, other lessons.

Source audits: `WORKBOOK_AUDIT_L21.md` (W), `GUIDE_DECK_AUDIT_L21.md` (G), `HOME_PARENT_PRACTICE_AUDIT_L21.md` (H).

| Finding | Action |
|---|---|
| W1 / G6 / H3 Lesson 20 hand-off says "print it" and "clock optional" | Not mine (owned by the Term 2 fix agent). Reported in `FINAL_FIXES_T3.md`: `l20.json` `parent.next_materials`, `s-end`, goodbye SAY and `tutor_prep` must say: your Term 3 book, cut out the 6 clock hands, keep the $1 tokens. `tutor_prep` here still tells the tutor to message families. Validator WARN stays until L20 is edited |
| W2 clock kit page size, hands, outlines, "a hour", clipped line | Shared tool (`tools/figs3.py clock_kit`). Listed in `FINAL_FIXES_T3.md`. In lesson data: the kit intro and `kit_contract` are unchanged and true (2 faces, 6 hands, at most 2 faces and 2 pairs used) |
| W3 / W4 / W11 time answer boxes 10 mm, exit clocks 20 mm, exit ticket on page 5 | Boxes and the half-page exit layout are template: listed. In data: the E2 drawing face is 46 (was 44) and E1 stays 50, as far as page 5 can hold (sizes 54 and 62 spilled the look-back onto a 7th page, tried and reverted) |
| W5 T3 statement 2 not decidable from the picture | Replaced by "The short hand has passed the 4." (True). T3 is now False, True, True; key, hint, solution, mistakes and `verify/l21_checks.py` updated |
| W6 / G2 kit hands do not creep, discovery cannot happen | Explore round 2 rewritten: tutor demonstrates on their own clock, children move the long hand to the 6 then slide the short hand half way from the 12 to the 1 ("our paper hands are loose"); slide titles, list, notes, script DO and WORK lines changed on `s-explore2` and `s-explore2-ans`. Page 3 hint now carries the quarter gloss only (the creep is taught in class and on the Investigation page) |
| W7 / G4 Start here minutes | Page 1 now 10:00, page 2 9:00 in the script; windows moved (Explore 12, Mini-lesson 10, brain break at 36 to 40, Workbook 40 to 70) so the slow class fits (29:29 of 30:00); "about 16 minutes" is now "about 18" everywhere; `spare_time` rule says minute 40 |
| W8 repeated times inside the workbook | E1 now 6:00 and 6:30 (was 7:00 = S5 Ben), E2 half past 5 (was half past 8 = T2 answer); the optional slide is half past 1 (a wrong S3 option, nobody's answer). `verify` checks E2 text, hands and "short hand is shorter" |
| W9 / G10 mirror idea never shown; skip order names a preview that does not exist | New SAY in the choice part: a mirror swaps left and right (a hand on the 3 points to the 9 in the mirror; up and down stay). Skip order now: "drop the optional slide and the Spare-time menu" |
| W10 "quarter past" has no gloss on the page | Page 3 instruction line: "Quarter past means 15 minutes past." |
| W12 / G12 Mi calculator | Rebuild: the no-calculator Mi is used |
| W13 draw items do not say which hand is shorter | S2 and E2 end with "The short hand is shorter." (also in the READ lines and verify) |
| G1 recording notice after recording starts; scripts disagree | Opening reordered as in Lesson 20 and Term 1: greet each child by first name, hello, notice, "Start the recording now. Do not use children's first names", REC, microphone routine ("Microphone off until I ask you to speak ... Nobody holds paper up to the camera"). `tutor_prep`, the opening NOTE and the title slide note agree |
| G3 quarter past and quarter to taught to the whole class | Slide `s-m4-ans` and the mini-lesson SAY now give only minutes (5:15 is 15 minutes past 5, 5:45 is 45 minutes past 5); the quarter words appear first on page 3 with a one-line gloss |
| G5 tutor cannot see the hands | Explore NOTE: say the time on three, then show the hour with fingers (a fist for 11, two fists for 12), thumb when the clock is set |
| G7 footers collide with cards on s-ws1, s-ws2; G8 small clocks on s-exit | Deck layout (shared builder): listed |
| G9 optional slide mislabelled | Retitled "Optional: half past 1", a different time, no tier label |
| G11 "papers to the camera 30 s" in the guide timing line | Printed by `tools/b_guide.py`: listed |
| G13, G14 | Not changed: look-back wording is the shared template; the microphone routine is the standard Term 2 wording |
| H1 online c5 base card unanswerable | Base question is now "Half past 7. Write the time in digits." |
| H2 parent page: recording statement and private-link line missing | `parent.next` now has the online link (please do not share it), what the recording holds and that a child may mute and keep the camera off (kept short: a longer text pushed the page to two pages; the template adds "Missed a lesson?") |
| H4 c1 and c2 share variants | Not changed: adding an item needs a runner/schema decision; the three Start here ideas are different tasks (read, choose, count) |
| H5 "1 fives make 5" | Step now "Count {n} steps of 5. You reach {ans}." |
| H6 t1 step wrong at :45 | Step now "The hour is the number the short hand has passed." (true for :15 and :45) |
| H7 / H8 "4-5-6" dashes, digit message | Runner: listed |
| H9 home H5 | Not changed (optional) |
| H10 g3 has no worked picture | Added a worked example to "How to check it": real 4 o'clock shows 8 in the mirror |
| (H1 home) H1 repeated S6 | Home H1 is now "The long hand is on the 6. Is it o'clock or half past?" |
| Other: `s-title` note and time plan | Updated to the new part times |

Numbering: every header reads "Term 3 . Lesson 1"; next lesson is "Term 3 Lesson 2". Money: none in this lesson. No quarter times at Start here (checked in `verify`).
