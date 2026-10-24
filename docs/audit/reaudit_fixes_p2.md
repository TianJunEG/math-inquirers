# Level 2 (P2) fix pass after the re-audit (`reaudit_p2.md`)

Date 2026-10-22. Content and wording only. Nothing committed. Not edited: `diag/*`, `levels/*.py|js`, `rebuild/slidekit.py`, `hp/*`, `website/*`, `docs/levels_and_placement.md`. Every new or changed numeric answer was checked in Python (brute force for each "find all" or "only one" claim); the script is in the session scratchpad, not in the repo.

## 1. Safeguarding regression (private chat)

| Where | Old | New |
|---|---|---|
| `p2/gaps.json` `common.preSay` (read into all 10 lesson scripts in the Tutor Guide) and its generator `docs/audit/mk_gaps_p2.py` | "Show your answer on your own paper to your tutor only, or send it in private chat." | "Write your answer on your own paper. When your tutor says so, hold it to the camera at the same moment as everyone else, or show it to your tutor only. Never send answers by private chat or message." |
| `p2/guide.js` routine table, warm-up row | "Answers on own paper held to the tutor, by private chat, or by thumbs." | "Answers on own paper held to the camera at the same moment, or shown to the tutor only; or thumbs. Never by private chat or message." |
| `p2/guide.js` routine table, talk-time row | "Quiet children can be invited by private chat beforehand." | "Quiet children can be invited, with a parent nearby, by a quick word in the open session; never by private chat or message." |

The slide notes (`p2gaps.precheck`) already used the paper rule, so no slide text needed a change. Checked in the rebuilt Tutor Guide text and the 10 rebuilt decks: the only remaining "private chat" is the "never" wording.

## 2. Entry point for L2 Q5 and L9 Q3 (answers unchanged)

| Item | Old | New |
|---|---|---|
| L2 Q5 magic triangle (a), side total 390 | empty triangle, hint "try 110 and 120 as two corners" | 110 and 120 are printed in two corner circles. Text: "First: what goes between them? Then fill in all the circles." Answer unchanged (corners 110, 120, 130; between 160, 140, 150). Brute force: with corners 110 and 120 fixed, the third corner is forced to be 130. Triangle (b) (side 420) is still printed unlabelled as before. |
| L9 Q3 jug table, 4 l in the 5 l jug | only "Start" and step 1 filled, 5 blank rows | Steps 1 to 3 filled ("pour the 5 l jug into the 3 l jug", "empty the 3 l jug"), so the child begins with 2 l in the 5 l jug. Text adds "act it out with two cups of different sizes, or draw the jugs. Where can that 2 l go?". 4 blank rows left (steps 4 to 7). Key unchanged (6 steps; shortest, checked by search earlier). Deck slide `p2l9-ws2` text updated. |

## 3. Think Harder items that were Core items with new numbers (printed items 1 to 4 = `qbank.stretch[0..3]`)

14 of the 17 flat items replaced (3 left, see below). Each new item needs the taught idea in a new setting (a claim to test, an error to find, a twist, a parity argument, a table comparison).

| Lesson, item | Old | New | Verified |
|---|---|---|---|
| L1 TH1 | cards 1, 5, 8: list all 3-digit numbers | cards 2, 6, 9: list every number bigger than 500, and say how you know all are found | 629, 692, 926, 962 |
| L1 TH3 | 3 hundreds, 14 tens, 6 ones = 446 | Ali has 46 ten-blocks, Siti 3 hundred-blocks and 15 ten-blocks: who has more, by how much | 460 v 450, Ali by 10 |
| L2 TH2 | `5A7 + B48 = 905` | `5[ ] + [ ]7 + 38 = 132` (three addends, carry of 2) | only 57 + 37 + 38 |
| L2 TH3 | `7A1 - B58 = 263` | Mei did 523 - 267 = 266 and checks 266 + 267 = 533: find the mistake | 256; 533 is not 523 |
| L2 TH4 | `538 + 199 = 540 + A` | true or false without working out both sides: 346 + 199 = 345 + 200; 270 + 130 = 260 + 150; 618 + 99 = 600 + 117 | T, F, T |
| L3 TH2 | 9 hens and goats, 24 legs (the lesson's swap method again) | 9 animals; Mei counts 25 legs, Siti 26; only one can be right; who and how many | 26: 5 hens, 4 goats; 25 impossible (odd) |
| L4 TH2 | A, B, B, C pattern, 25th letter | beads R R B G repeating; "the 30th bead is blue", is she right; which places to 30 are green | 30th is red; green at 4, 8 ... 28 |
| L5 TH2 | spent $15, dad gave $10, now $42 | spent $15, dad gave him as much as he had left, now $42 (undo a doubling) | $36 |
| L7 TH2 | ribbon of 9 pieces, 4 + 3 used | "3/8 of a pizza is more than 3/5 because 8 is bigger than 5": right? draw two bars | no; 3/5 > 3/8 |
| L7 TH3 | 2/7 + ? = 1 | Siti says 3/8 + 2/8 = 5/16: find the error and the right answer | 5/8 |
| L8 TH2 | squares in a 3 by 2 grid (8) | rectangles (squares count) in a 2 by 2 grid, counted by size | 9 (4 + 2 + 2 + 1) |
| L9 TH1 | 20 m rope into 4 pieces, 3 cuts | 2 apples + 1 lemon balance a pomelo; a pomelo balances 5 lemons: how many lemons balance 1 apple, and a pomelo + an apple | 2 lemons; 7 lemons |
| L10 TH2 | 3-digit numbers with digit sum 3 | Mei saves $3, $6, $9 ...; Ali saves $10 a day; table; first day Mei has more in total | day 6 ($63 v $60) |
| L10 TH4 | 5, 9, 13, 17 ...: 10th number (41) | will 49 be in the pattern; will 50; how do you know | 49 yes (48 + 1), 50 no |

Left alone from the re-audit's flat list (3 of 17): L3 S3 (34 marbles shared by 4), L4 S3 (yellow beads in the first 18) and L6 S2 ($10 with $5, $2 and $1 notes: a listing task, kept because a list in order IS the lesson's idea and it is a good task).

Page fit: the new L3, L4 and L5 items were first too long and pushed Think Harder question 4 onto an extra page; they were shortened, and the workbook is back to 64 pages.

## 4. Printed Go further items that were weak

| Lesson, item | Old | New |
|---|---|---|
| L3 Q5 (bank C7) | trikes and cars, 30 wheels, find all (swap table again) | 12 bicycles/tricycles: "Mei says Ravi could count any number from 24 to 36. Right? Could he count 37? Why can he count 25 wheels but never 25 legs on 12 hens and goats?" Answer: yes, every number 24 to 36, each in exactly one way (a swap adds 1 wheel); hens and goats only give even totals 24 ... 48. |
| L6 Q6 (bank C8) | 8 sweets/lollipops, $1 (swap table again) | 8 things, at least one of each (5 cents and 20 cents): Mei says $1.00, Siti says $1.50; find ALL amounts; what do you notice and why. Amounts 55c, 70c, 85c, $1, $1.15, $1.30, $1.45 (step 15c); $1.50 impossible. |
| L7 Q6 and Q7 (bank C8, C9) | fold a strip three times (1/8); half of a half | bank C1 (three children share 10 cake pieces, all different: 4 ways) and bank C2 (a fraction with 1 on top between 1/7 and 1/4: 1/5, 1/6). Done by swapping their positions in `qbank.challenge`, so no item was lost; the two old one-step items are now bank-only C1 and C2. |
| L8 Q7 (bank C9) | dice: opposite faces add to 7 | 3 by 3 by 3 painted cube: how many small cubes have paint on 3, 2, 1 and 0 faces (check they make 27), then the unpainted count for 4 by 4 by 4. Answers 8, 12, 6, 1; and 8. Brute-forced. |

## 5. Problem posing on the printed Go further page

One short "Make up your own:" prompt plus 2 dotted lines at the foot of the Go further page in all 10 lessons (`POSE` in `p2/workbook_html.js`). It fits in every lesson without adding a page (workbook still 64 pages). Prompts: L1 riddle with one answer; L2 two-box missing-digit sum with one answer; L3 "how many of each" puzzle with one answer; L4 pattern of 4 shapes and a question about the 30th shape; L5 before-and-after story ending with 40; L6 coin puzzle about paying exactly $1; L7 fair-sharing story, cake of 8 pieces, 3 children; L8 cube stack of exactly 20 cubes; L9 jug puzzle checked by a table; L10 puzzle for next year's group. Not added to slides or the Tutor Guide answer keys (open tasks, no single answer).

## 6. Consistency

- Slide "Think harder" now shows the SAME items as the printed page in all 10 lessons. New `think(K)` in `rebuild/p2gaps.py` reads `qbank.stretch` from `p2/data.js` (via node), so slides, printed page, Question Bank and Tutor Guide can no longer drift. The slide has room for items 1 to 3 only (4 long items overflow 1080 px); a line says "Question 4 is on your Think harder page", and the speaker notes carry all four questions and answers. L7 shows stacked fractions as the rest of that deck does; L2 shows yellow boxes.
- "Looking back" location: slide notes (`p2gaps.reflect`), `gaps.json` refSay and `docs/audit/mk_gaps_p2.py`, and `guide.js` (routine table and Investigation line) now say the box is on the page "Before you go: Investigation and Looking back" after worksheet page 2, not "the last core page".
- L10 reflect slide label is now 85-87 MIN (was 87-89 MIN); other lessons stay 87-89.

## 7. MOE wording (Level 2 only)

- Boxes not letters for unknown numbers: all of L2 (workbook text, tutor script, mini-lesson slides, try-it slides, exit ticket in `l2.js`, `gen_p2l2.py`), the L10 warm-up card "3A5 + 214 = 579" (now `3[ ]5 + 214 = 579`) and its note. Bank items use `[ ]` (the same text convention as `{box}` elsewhere); two or more boxes are told apart by place ("tens box", "first box"). Left on purpose: "Box A, Box B, Box C" (names of three boxes of marbles, now written "Box A + Box B" in the figure and notes), the pattern letters A, B, B, C (L4), "Box A/B/C" pens (L5) and net names A to F (L8): these are labels, not unknown numbers.
- am/pm: "a.m." and "p.m." replaced by "am" and "pm" in `l9.js`, `l10.js`, `gen_p2l9.py`, `gen_p2l10.py` (about 100 places; the sentence-ending full stop was kept where the next word starts a new sentence).
- Half circle: "semicircle" replaced by "half circle" in `l8.js`, `gen_p2l8.py`, `gen_p2l10.py`, `l10.js`, `gaps.json` (L8 and L10 sneak-peek and go-further), `parent_side.json`. The L8 teach slide says once "a half circle (some people call it a semicircle)".
- numerator/denominator: L7 never uses either word (it says "bottom number" and "top number"), so nothing to change.

## Not fixed, and why

- `diag/content/p2.json` has "Accept 4:15 with or without p.m." and the diagnostic still prints "5?" for a hidden digit and "a.m./p.m." style wording in places. Lead to change (shared files).
- L4 bank Challenge C1 (lights every 3 and 5 seconds): seconds are a P3 idea, and the item is a re-skin of Core Q6. Bank-only, not printed, not in the 7 requested fixes; left as is.
- L2 Q5 triangle (b) (side 420) is still printed with no question line next to it (it is Think harder 1); left because a (b) line would add text to a full page.
- L3 Think Harder 3, L4 Think Harder 3 and L6 Think Harder 2 are still Core-style (see section 3).
- Slide "Go further" (Challenge) items are not printed items in L5, L6 and L8 (the printed Go further are bank C7 to C9; those decks show other bank challenge items). The audit named only the Think harder mismatch, so only that was made identical.
- L9 core Q5 (clocks, am/pm and elapsed time in one item) and L1 core Q1 b, c (regrouping with no scaffold) are core-page items flagged by the re-audit but not in this pass's list.
- Reading load, page-2 solo time and pacing: skipped as instructed (timing audit).

## Rebuild and page counts

Decks: `python3 rebuild/gen_p2l1..10.py`, then `python3 levels/restyle.py split/p2lK` for K = 1 to 10 (no overflow in the preview check of the changed slides). Printed: `bash levels/build_level.sh 2`; extras: `python3 levels/mkextras.py 2` (self-check OK).

| File | Before this pass (HEAD) | Now |
|---|---|---|
| Student Workbook | 64 | 64 |
| Tutor Guide | 100 | 101 (the 1 page is mostly longer lesson text; the guide also carries the lead's recording-cue change) |
| Weekly Dose of Thinking | 24 | 25 |
| Question Bank | 27 | 27 |
| Weekly Email Pack | 12 | 12 |
| Free Taster | 5 | 5 |
| What Learners Get | 1 | 1 |

Workbook pages per lesson unchanged: L1 6, L2 6, L3 5, L4 5, L5 5, L6 5, L7 5, L8 6, L9 6, L10 5 (plus cover, journal, 7 kit pages, certificate).
