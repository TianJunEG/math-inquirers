# Fix pass, Term 3 Lesson 4 (lesson 24, Dollars and Change)

Changed: `lessons/l24.json`, `verify/l24_checks.py` (187 checks pass), `AUDIT_L24.md`, `out/l24/`. Validator 0 FAIL (29 pass, 2 WARN: kit pages 49% and 47% are short by design); leak check clean; workbook 5 pages fill 100/96/88/96/99% plus 2 kit pages; home sheet 94%; parent page 91%; parts 2/6/4/11/11/4/32/6/6/3/5 = 90; script 68:12, slow class 80:44, no part over (mini 10:53 of 11:00). Not touched: shared tools (kit builder, money figure, runner), other lessons.

Source audits: `WORKBOOK_AUDIT_L24.md` (W), `GUIDE_DECK_AUDIT_L24.md` (G), `HOME_PARENT_PRACTICE_AUDIT_L24.md` (H).

| Finding | Action |
|---|---|
| W5 / G1 Mi holds a calculator | Rebuilt with the no-calculator Mi (workbook page 1, parent page; deck and guide rebuilt) |
| W1 kit pieces small, cut lines 1.5 mm apart, pages 35% and 30% full, no "no printer" line | The kit page is built by the shared `play_money` kit (tools): not edited, listed below. Data side: the lesson already says "no printer or no cutting? small pieces of paper with the value written on each" in the materials list and tutor_prep |
| W2 / W12 same coin at different sizes; T4 sets differ in size | T4 sets now have an explicit equal size (90) so the three rows scale together; S3 coin set to size 30. One coin scale across all figures is a shared-tool change: listed. Set B still sits lower than A and C (baseline) in the print: tool |
| W3 / G2 tasks and class lines need ten 5¢ and ten 10¢ coins; kit holds 4 and 6 | S3 now reads "Count in 10s, then in 5s." (counting, no coins needed; the key hint says the same). Mini-lesson "Check it on your table, ten ten-cent coins" became "count in tens to a hundred on your fingers; you do not need ten coins", the WORK line likewise; the `s-m3` slide shows the $1 and two 50¢ coins only while asking. The sneak-peek puzzle 2 ("10 ten-cent coins") is a puzzle on paper, not a task on the table, and is kept |
| W4 missing non-routine type (work backwards: paid and change given, find the price) | T3 is now "Siti buys a pencil. She pays with a one-dollar coin and gets 40¢ change. (a) A one-dollar coin is worth ____¢. (b) The pencil costs ____¢." (100¢, 60¢); hint, solution, mistakes, `verify` updated. "work backwards" added to `contest_moves`; the Think harder rows in `moe.note`, the `s-choice` slide and the tutor guide note name it. Forward change from a $1 coin stays in G3, in the online set (t1) and in Home Practice (H2 and H3 are forward change from $5 and $10) |
| W6 pages 3 and 4 not marked "for home too" | Both intro lines end "Not finished? This page is for home too." |
| W7 Investigation space and look-back layout | Not changed: page 5 is 99% full; a table strip would spill the look-back. Look-back layout is a shared tool: listed. The key already says "do not mark a child down for stopping at one way" |
| W8 S4 blank repeats the stem number | "I circled the ____¢ coin and the ____¢ coin." (50¢ and 5¢, either order); key and `verify` updated |
| W9 key S5 slip cannot arise | "Circling the $1 coin because it is a coin (the value is the number on the piece, not its shape)." |
| W10 D1 wording in the guide (reproduction rules unchecked) | Removed from the tutor-facing text (`moe.note`, slide 1 note); `moe.note` now says only that owner decision D1 is open before the first printing. **Owner step:** decide D1 before the first paid book |
| W11 key G1 slip "Writing 12" | "Writing 9 (seven $10 notes, a $2 note and a $1 coin, without the $50 note)." |
| G2 `s-m3` shows the answer while asking | `reveal` on the ten-coin picture (the caption was dropped); the builder's `s-m3-ans` slide shows the ten coins after the question. `verify` reads the answer slide; the tutor_prep line names `s-m3` |
| G3 money rows tiny on the workbook slides | `s-ws1` and `s-ws2` now show the money large (Q1, Q2, Q4) with each question as plain text; Q5 and Q6 are read aloud from the slide text. The exit slide (E1) keeps the shared `qs` layout; the tutor reads each amount aloud (tutor_prep says so) |
| G4 `s-opt` pictures the 4-coin answer | A tray of 3 five-cent, 3 ten-cent, 3 twenty-cent and 2 fifty-cent coins; note updated |
| G6 "papers to the camera 30 s" in the guide | Printed by `tools/b_guide.py` (shared): listed |
| G7 recording notice order | Opening in the final Term 1 order and words (hello with "Cameras can be on or off, as you like"; recording sentence with "keep your microphone and camera off"; microphone line with "Nobody holds paper up to the camera"; DO "Greet the whole group warmly. Do not use children's first names on the recording."); `tutor_prep` matches |
| G8 `s-m1` coins drawn in ascending size under "not the size" | Not changed: the figure scales with value; the tutor line already says the number tells the value and the S5 question tests it |
| G9 no "lay your coins out by value" step | Not added: the warm-up already has the children order four coins by the number; adding a step would take the slow-class mini over its minutes |
| G10 tokens in the L21 and L22 hand-offs | Not mine (other lessons): a one-line addition "keep the $1 tokens" is needed in `l21.json` and `l22.json`; reported |
| G11, G12 | No change needed (audit says fine) |
| H1 online t3 ordered item has a redundant second number | Now a single-number item "How many 10¢ coins do you need?" (answer 3) with two slips (2 and 5); `verify` updated |
| H2 home sheet has no pictures | Not done: the sheet is 94% full and each question already names its coins |
| H3 parent page invites real coins without a safety line | "put some play money on the table (real coins only with a grown-up beside you; small coins stay on the table, away from little ones)" |
| H4 online c3 "A toy costs $3" shows a ball | "A ball costs $..." in the item and its template |
| H5 thin recording sentence | `parent.next` adds what is recorded, that the child may mute and keep the camera off, and that the link is private and not to be shared |
| H6 runner header, H7 shown-answer wording, H8 slips for every g1 variant | Runner (shared): listed |
| Copy check against the reference papers | H1 reworded ("a 10¢ coin and a 5¢ coin. How much does he have in all?") to clear a 7-word overlap with `non_routine_questions.md` |

Money: no "50c" on any child or parent page (the figure specs use "50c" internally and print 50¢; the tutor lines say "never 50c"). Numbering: "Term 3 • Lesson 4" on workbook, key, home and parent headers (viewed). Hand-off from lesson 23 is true (29 pieces, the $1 tokens, the clock) and the hand-off to lesson 25 (12 price tags, play money in its envelope) was checked against `l25.json`.

## Needs a shared-tool, runner or owner step

1. `play_money` kit (`tools`): coins and notes at the contract size (about 20 to 24 mm coins, 60 x 30 mm notes), 6 mm between cut lines, "no printer" line on the page, one denomination per row.
2. `money` figure: one coin scale across every picture; align the three sets of T4 on one baseline; a size option on the `qs` slide row.
3. `tools/b_guide.py`: remove "papers to the camera 30 s". `tools/b_print.py`: look-back check boxes wrap raggedly; the rewind label names "Term 1 Lesson 4" on the child sheet.
4. Runner: slips for every g1 variant, the unit in the shown answer ("35¢", "$2"), "Term 3" in the sub line.
5. `l21.json` and `l22.json` hand-offs: add "keep the $1 tokens from Term 2".
6. Owner: decision D1 (play-money reproduction) before the first paid book.
7. Quest gate C3 (`l30.json`) repeats 50¢, 20¢, 20¢, 5¢ and a $7 toy paid with $10, which the lesson keeps out of its own pages; suggest other numbers for the gate.
