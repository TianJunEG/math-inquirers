# Second fix pass, Lesson 8 (Balance and Swap), 22 Oct 2026

Inputs: `audit/GUIDE_DECK_AUDIT_L08.md`, `audit/HOME_PARENT_PRACTICE_AUDIT_L08.md`, L8 rows of `audit/TERM_WIDE_AUDIT.md` (F19), `FIXES_L08.md`, owner decisions. Files changed: `lessons/l08.json`, `verify/l08_checks.py`, `out/l08/`, `AUDIT_L08.md`. Validator 0 FAIL (18 pass, 1 estimate warning), 2612 answer checks, 324 practice variants; leak check clean; slow-class script 87:50 (workbook 30:45 of 28, covered by the flex buffer, stated in the guide); workbook fill 92, 90, 84, 86, 94% (kit 91%), home 99%, parent 99%.

**Ordered marking confirmed (browser test on `out/l08/practice`, item g1):** `27, 17` and `27 and 17` are marked right; `17, 27` is marked not yet with "Those are the right numbers, but check which one goes in each blank" (the wrong-order bug L08-1 is fixed); `27, 17, 5` and `abc` are not accepted. Remaining wrinkle (runner, shared): a single number such as `27` still gets "Those fit. Are there more?"; the question now says "There are two blanks. Type both numbers in order".

| Finding | Sev | Action |
|---|---|---|
| G1, F7 hold-ups to camera | Med | Sneak-peek and exit hold-ups removed (keep your paper; tick your own ticket; fingers for how many right); explore "show their plates" is now a thumbs up. |
| G2 camera shows page and plates | Med | The greeting no longer asks to see page, plates and hands; nothing is shown to the camera. |
| G4 workbook timing | Med | Check slides read only when most have stopped writing; slow class 87:50, workbook overrun and the flex buffer stated in the guide; page 2 slide says "About 9 minutes". |
| G5 s-ws2 omits numbers | Med | s-ws2 prints every part; the script now reads the numbers of all page 1 and page 2 questions and the exit ticket. |
| G6 journal, tracker | Med | Removed; "show your ticket to a grown-up"; fingers, no per-child tracker. |
| G7 goodbye before optional items | Med | Next-lesson line is spoken on the end slide; "Goodbye" is the last line, after any optional slide. |
| G8, G10 timer slide, ruler | Low | No timer slide; "About N minutes"; goodbye and end slide now say "if you have no ruler, tell your tutor" and list clips and things to measure. |
| G12 named wrong working | Low | Talk slide and script say "a child says". |
| F6, F8, F9, F2 shared | Med | Recording statement, microphone routine, no first names, WhatsApp "still stuck" route, no shared room, parent `next_materials` for Lesson 9 (ruler, clips, things to measure, print at 100%). |
| F19 tier drift | Med | S5 (c) and (d) are now whole tens only (40 + 20 = 30 + [], 30 + 30 = 20 + []); the one-for-one shifts stay at Think harder (T3). Lesson 6 named as helpful before S5 and S7. Checks and key updated. |
| L08-1, L08-2 | High, Med | Ordered marking confirmed (above); question reworded. |
| L08-3, L08-7 | Low | H5 "Write all the sums you can find. Many answers are right."; try-at-home 1 is one pile on each plate (7 and 5). |
| L08-5 | Low | c5 is now a different Start here item (8 + 6 = 9 + ___). |
| L08-6 | Low | Shuffle is in the runner. |
| F29, P2 | Low, Med | Beyond-Primary-1 reminder in tutor prep; "do not teach the column method yet". |

Not fixed (shared files): "I am still stuck (my tutor will come and help)" on the look-back; guide sneak-peek line "Papers are shown to the camera once, together"; slide font sizes; Mi calculator image; home-sheet separate ruled line plus box (L08-4); the estimated "page 5 overflows (106%)" warning (built PDF 94%); the runner's "Are there more?" message for a partial set answer; no Term 1 console; the guide's slow-class flag never shows OVER.
