# Fix pass, Term 3 Lesson 10 (lesson 30, Calendar Detective and Mi's Challenge Quest)

Against `WORKBOOK_AUDIT_L30.md`, `GUIDE_DECK_AUDIT_L30.md` and `HOME_PARENT_PRACTICE_AUDIT_L30.md`. Rebuilt with `bash term/l1/build.sh 30`: validator 22 pass, 0 warn, 0 FAIL (verify: 219+ independent checks, new ones for each change); script 69:42 of 90, slow class 82:14, no part OVER; real workbook PDF fills 95, 82, 88, 89, 93% (kit page 76%); Quest Log 4 pages, tutor notes 7, grown-up note 1; home 91%, parent 92%. Viewed: all workbook pages, Quest Log, grown-up note, parent page, slides 3, 10, 24, 26.

| Finding | Action |
|---|---|
| WB 1 / GD 3 S3(b) is the Explore example | S3(b) now 4 days later (Saturday); key, script, slide notes, tutor prep, checker (registry now holds both S3 items). |
| WB 2 / GD 6 / HP 2 Quest grown-up note is the Term 2 note | Rewritten for Term 3: no "odd and even / 3 and 4 tables"; beyond statement names reading a clock to 5 minutes with am and pm and the growing stick pattern; the Quest Log is in the Term 3 book (no printing), the Term 2 marbles example replaced by "Mei counted coins in tens and fives" (also in the one-line examples and the notes-sheet prompts); "Owner decisions" and the "build.sh" sentence removed from tutor-facing text. Checker asserts the old wording is gone. |
| WB 2 footer "Print at 100% (actual size)" | NOT fixable here: hard-coded in `tools/b_quest.py` (line 173). Shared-tool need. `child_footer` data is ignored. |
| WB 3 / HP 3 T4, G2 and the Investigation read off the month page | T4 and G2 now print only the first week row (`week: 0`), so 18th, 25th, 8/15/22/29 and the 31st must be reasoned with 7s, not read. The Investigation prints no picture. |
| WB 4 / GD 9 colour as the only clue, black and white | "The yellow day" now "the day with a ring round it" (S5, gate 8, six slides, script); the month figures carry a ring (`mark`) as well as the yellow; "the green child" is "the child with a ring round them". A pure black and white print build is a shared print tool need (owner request). |
| WB 5 / GD 2 "nobody sees your answers" | Opening SAY, Quest Log "Mi says" and slide texts now: "Your answers are private: only your grown-up and your tutor may see them." Sneak-peek lines now say "your paper is not collected" (true: sneak papers are not photographed). The checker rejects the old claim. |
| WB 6 S1 answers in the row above, "Thursday" clipped | The Mon..Sun header is gone; S1 is two rows of full names in order (no abbreviation row, 4 columns, nothing clipped). |
| WB 7 / HP / GD Quest stick picture merged, small coins and month figures | Drawing code in `tools/figs3.py` / `figs2.py`: shared-tool need (separate sticks, coins 14 mm, month cells). |
| WB 8 / GD 1 split of Start here | Slides, READ lines, answer slides, STUCK and notes now: page 1 = S1 to S4, page 2 = S5 and S6 (matches the printed book); the page 1 box says "After question 4" (`choice_after` 4). Slots: page 1 9:30, page 2 6:00, choice 90 s. Start here estimate corrected to "about 17 minutes" (S1 2, S4 2.5). |
| WB 9 "We use them again", fallback not on page | Fallback ("No cards? Write the 7 days on 7 small pieces of paper.") added to the kit intro. The "We use them again" sentence and the 3 to 4 mm cut gaps are printed by shared tools: need (gaps 6 mm). |
| WB 10 L20 hand-off | `l20.json` is owned by the Term 2 fix agent: not edited. Mismatch reported: it still says the clock is "(optional)" and does not say to cut the 6 clock hands or keep the $1 tokens. |
| WB 11 coins 6 pt, month 45 mm | Shared figure sizes (need listed). |
| WB 12 / GD 11 gate 8 labelled "Process skills; Addition and Subtraction" | Gate 8 now sits in the Time strand. "Lessons 29 to 29" and the "Term 2" examples: examples replaced; "Lessons 29 to 29" is printed by `tools/b_quest.py` line 127 for a one-lesson strand: shared-tool need. |
| WB 13 exit ticket heading, look-back wrap | Printed by `tools/b_print.py` (shared). Listed. |
| GD 4 Quest pace, no slow-class slack | Not changed: the Quest keeps its 20-minute slot by owner decision; slow class 19:49 of 20:00 and the notes already let a child finish in the first minutes of the workbook. |
| GD 5 workbook slide thumbnails | Template `qs` blocks (shared). The re-split gives S1 to S4 four compact rows; S5 month page unchanged. |
| GD 7 pause announcement | New SAY line before "Pause the recording now": "The recording pauses now for Mi's Challenge Quest, and starts again for the workbook." |
| GD 10 REC cue order, "papers to the camera 30 s" | Shared Term 1/2 pattern and `tools/b_guide.py`: listed. |
| GD 12 stuck child helped "next term" | Not changed: needs an owner decision on a follow-up route (a promise to message families would be a new privacy statement). |
| HP 1 ordinals "2th", "22th" | Templates c1, t1, g1 use `{a\|ord}` and `{ans\|ord}`; c1 asks "which date? Write the number" (no "___ th"); checker rejects any `{x}th`. |
| HP 1 / online static items repeat workbook | c3 is Thursday + 2, t2 "one day after the day before yesterday" from Tuesday, g2 is 50 days after Tuesday; verified. |
| HP 3 calendar pictures online | Runner has no calendar figure for items: shared-tool need. |
| HP 5, 7 parent summary | Added: one photo of each of the 4 pages to the business WhatsApp today; "The recording link is private: please do not share it" (Term 1 wording; the tool's "Missed a lesson" sentence stays). Beyond statement now also names a fortnight and every Wednesday, and says days of the week are not a listed Primary 1 topic. |
| HP 6 home sheet month page | Not added (home sheet is 91% full); H2 hint already allows a calendar from the house. |
| HP 9 rewind items, HP 10 online subtitle without the term | Runner/shared. Listed. |
| Found while viewing | The warm-up line-up highlighted the 2nd child while the script and key ask for the 3rd: fixed (`highlight: [3]`, line-up places count from 1), checker corrected. |

## Shared-tool and owner needs (for FINAL_FIXES_T3.md)
1. `tools/b_quest.py`: Quest Log footer "Print at 100% (actual size)" (line 173) and "Lessons 29 to 29" (line 127).
2. Black and white print build of workbooks and the Quest Log (owner request).
3. `tools/figs3.py`: separate sticks in `stick_pattern`; larger coins and month cells; `mistake_cards` and `calendar_cards` cut gaps of 6 mm.
4. `tools/b_print.py`: "We use them again" kit sentence; exit ticket heading; two-column look-back.
5. `tools/b_guide.py`: remove "papers to the camera 30 s".
6. Deck `qs` blocks: question tables are thumbnails.
7. Runner: term in the page subtitle, rewind items, a calendar picture for items.
8. `l20.json` hand-off to Term 3 (clock optional; cut-out clock hands; $1 tokens): owner is the Term 2 fix agent.
9. Owner: how a stuck child is helped between terms.
