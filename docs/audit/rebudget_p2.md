# Re-budget pass, Primary 2 (Level N=2): every lesson fits 90 minutes live online

*Applies `docs/audit/timing_p2.md` (sections 6 to 8). Single source of the minutes: `rebuild/p2budget.py` (part budgets and slide windows) -> `p2/budget.json` (read by `p2/guide.js` and the tutor console timer) -> `rebuild/p2gaps.py` `apply()` (slide pills, speaker-note `Minutes a to b`, title-slide time plan). Edit minutes only in `p2budget.py`, then run `python3 rebuild/p2budget.py`.*

## Result

| Lesson | Old budget sum | New budget sum | Audit predicted need (central) | Re-run model: fast / **central** / slow | Old as-scripted (time-boxed, central) |
|---|--:|--:|--:|---|--:|
| 1 Digit Detectives | 90 | 90 | 81 | 70.8 / **80.4** / 90.8 | 98.5 |
| 2 Missing Digit Mysteries | 90 | 90 | 79 | 69.0 / **78.4** / 88.4 | 101.8 |
| 3 Legs, Wheels and Arrays | 90 | 90 | 82 | 71.5 / **81.3** / 92.0 | 104.0 |
| 4 Pattern Machines | 90 | 90 | 79 | 69.1 / **78.6** / 88.9 | 96.8 |
| 5 Mystery Number Machines | 90 | 90 | 83 | 71.7 / **81.6** / 92.3 | 98.8 |
| 6 Market Day | 90 | 90 | 85 | 73.0 / **83.5** / 94.6 | 103.3 |
| 7 Fair Shares | 90 | 90 | 84 | 72.6 / **82.6** / 93.3 | 104.7 |
| 8 Shape Builders | 90 | 90 | 80 | 69.3 / **79.0** / 89.4 | 106.9 |
| 9 Measure Masters | 90 | 90 | 77 | 67.2 / **76.6** / 86.7 | 110.1 |
| 10 Challenge Day | 90 | 90 | 83 | 72.4 / **82.4** / 93.1 | 106.7 |

Re-run: `python3 -I docs/audit/timing_p2.py --rebudget` (new mode, added to the audit model: it reads the rebuilt decks, clears the FIX entries that dropped/merged/added slides because the decks now already carry those changes, and checks `p2/budget.json` against `final_budget()`). Every lesson is 0.6 to 1.8 minutes below the audit prediction (the shortened SAY lines and the merged slides are slightly cheaper than the audit assumed). The only part flagged OVER by 0.25 minutes or more is Looking back (needs 2.3 of 2.0, the same -0.3 the audit reports); there is a 3 to 5 minute named Flex block on top. The slow-tutor case still overruns 90 minutes by up to 4.6 minutes in L3, L5, L6, L7 and L10 (as in the audit, section 7); the Flex block and the page-2 rule are the cover.

## Page counts (re-measured)

- Student workbook: **66 pages**, per lesson 5/4/4/4/4/6/5/5/5/4 (L1..L10) plus 20 front and back pages. The committed PDF (64 pages) was stale; rebuilding the unchanged HEAD sources gives 66, so the re-budget changes no page count (stars replace words in the same lines; the only new lines are the split of L4 Q3(a)/(b), which stays on its page).
- Tutor guide: 107 pages (was 101): the extra pages are the new Flex segment, the take-home and late-rule paragraphs and the extra REC line per lesson; no restriction was given for the guide.
- Weekly PDFs, question bank, email pack, taster, one-pager: rebuilt (`levels/build_level.sh 2`, `levels/mkextras.py 2`, self-check OK). `rebuild/preview.py` on all 10 decks: no slide overflows.

## Level-wide changes (all ten lessons)

- Part budgets as the audit: Opening 1.5, Sneak-peek 4.5, Warm-up 4.5, Explore 13, Brain break 3, check-together 2.5 + 2.5, Talk 5, Exit 5, Looking back 2, Closing 1.5, a named **Flex (spare time)** block after check-together page 2 (3 min; 5 in L4, 4.5 in L9, 4 in L10). Flex is never taken from the exit ticket, looking back or the stamp.
- Sneak-peek: `common.preSay` is now 28 words; child work 45 s and 90 s (`docs/audit/mk_gaps_p2.py` regenerates `p2/gaps.json`; the generator was already out of sync by one word in L8 note text and I kept the json wording).
- Warm-up: the slide shows only the two quick questions that are asked (guide table questions 1 and 3; 2, 4, 5 spare). Games trimmed per lesson (see below).
- Explore: kit on the desk at minute 0 (30-second check, opening message, title-slide notes); one round of breakout rooms with an auto-timer (60 s in, 60 s out; pair work 5.5 min, 4.5 in L10); `goexp` slide merged into `explore1` as a one-line Go further box at the foot (no slide of its own); "how do you know" on debrief question 2 only.
- Slide pills and speaker notes carry the new minutes on every slide; optional slides (Think harder, Go further, its picture and walk-through, L5 teachthree) show **Optional, if you finish early** and no clock time; they are listed in `optional_slides`.
- Take-home stars: each moved sub-item is printed with a star and the words `take-home` (orange), stays Core, keeps its answer on the check-together slide marked take-home, and the answer key in the guide is unchanged. A tutor rule is printed in the guide worksheet segment and in each `ws2` slide note: at the start of page 2, if the clock is more than 2 minutes late, drop the last Core question of page 2 to take-home; never shorten talk time, exit ticket, looking back or closing.
- Talk time: 90 seconds in pairs, two volunteers, one question (second questions removed from scripts, slides, notes). Exit ticket: slips held up one at a time, answer on the next click, about 2 minutes of child work. Brain break notes: three minutes (two of movement, one for water).
- Guide: routine table, every `seg()` time (read from `budget.json`, including the Lesson 10 variants), sneak-peek and closing titles, explore timing paragraph, key-slide minute, worksheet minutes, new Flex segment, "Take-home stars" and late-rule paragraph, REC lines.
- Source inconsistencies fixed: L2 `key` tag (35 MIN), L10 `reflect` label (85-87), L3 deck `ws2` text (Q7).

## Per lesson

### Lesson 1: Digit Detectives

| New minutes | Part | Old budget | New budget |
|---|---|--:|--:|
| 0-1.5 | Opening | 1 | 1.5 |
| 1.5-6 | Sneak-peek puzzles | 3 | 4.5 |
| 6-10.5 | Warm-up | 4 | 4.5 |
| 10.5-23.5 | Explore | 12 | 13 |
| 23.5-35.5 | Mini-lesson | 12 | 12 |
| 35.5-38.5 | Brain break | 4 | 3 |
| 38.5-52.5 | Worksheet page 1 (pairs) | 14 | 14 |
| 52.5-55 | Check together, page 1 | 2 | 2.5 |
| 55-59.5 | Short teaching | 5 | 4.5 |
| 59.5-71 | Worksheet page 2 (alone) | 12 | 11.5 |
| 71-73.5 | Check together, page 2 | 3 | 2.5 |
| 73.5-76.5 | Flex (spare time) | - | 3 |
| 76.5-81.5 | Talk time | 8 | 5 |
| 81.5-86.5 | Exit ticket | 7 | 5 |
| 86.5-88.5 | Looking back | 2 | 2 |
| 88.5-90 | Closing and stamps | 1 | 1.5 |

Cut or moved: Warm-up: 2 rounds, quick questions 1 and 3. try1 items a, b (c dropped). Dropped slide: teachcount (goes with the take-home). Take-home stars: page 2 Q4(b) and the whole of Q5. Talk time: one question (the 'second question if time' line removed). ws1ans/ws2ans: answer lines only.

### Lesson 2: Missing Digit Mysteries

| New minutes | Part | Old budget | New budget |
|---|---|--:|--:|
| 0-1.5 | Opening | 1 | 1.5 |
| 1.5-6 | Sneak-peek puzzles | 3 | 4.5 |
| 6-10.5 | Warm-up | 4 | 4.5 |
| 10.5-23.5 | Explore | 12 | 13 |
| 23.5-35.5 | Mini-lesson | 12 | 12 |
| 35.5-38.5 | Brain break | 4 | 3 |
| 38.5-52.5 | Worksheet page 1 (pairs) | 14 | 14 |
| 52.5-55 | Check together, page 1 | 2 | 2.5 |
| 55-59.5 | Short teaching | 5 | 4.5 |
| 59.5-71 | Worksheet page 2 (alone) | 12 | 11.5 |
| 71-73.5 | Check together, page 2 | 3 | 2.5 |
| 73.5-76.5 | Flex (spare time) | - | 3 |
| 76.5-81.5 | Talk time | 8 | 5 |
| 81.5-86.5 | Exit ticket | 7 | 5 |
| 86.5-88.5 | Looking back | 2 | 2 |
| 88.5-90 | Closing and stamps | 1 | 1.5 |

Cut or moved: Mini-lesson: we2 merged into teach1 (one slide: start at the ones; subtraction turned round into an addition, SAY paragraphs kept), try3 deleted, try1 items a, b, try2 item a. Warm-up: 3 calls (65, 370, 125), questions 1 and 3. Dropped slide: teachtri (goes with Q5). Take-home stars: line under Q1 (check by adding), Q3 c and d, whole of Q5 (magic triangle). key slide pill corrected (35 MIN -> 34.5-35.5).

### Lesson 3: Legs, Wheels and Arrays

| New minutes | Part | Old budget | New budget |
|---|---|--:|--:|
| 0-1.5 | Opening | 1 | 1.5 |
| 1.5-6 | Sneak-peek puzzles | 3 | 4.5 |
| 6-10.5 | Warm-up | 4 | 4.5 |
| 10.5-23.5 | Explore | 12 | 13 |
| 23.5-35.5 | Mini-lesson | 12 | 12 |
| 35.5-38.5 | Brain break | 4 | 3 |
| 38.5-52.5 | Worksheet page 1 (pairs) | 14 | 14 |
| 52.5-55 | Check together, page 1 | 2 | 2.5 |
| 55-59.5 | Short teaching | 5 | 4.5 |
| 59.5-71 | Worksheet page 2 (alone) | 12 | 11.5 |
| 71-73.5 | Check together, page 2 | 3 | 2.5 |
| 73.5-76.5 | Flex (spare time) | - | 3 |
| 76.5-81.5 | Talk time | 8 | 5 |
| 81.5-86.5 | Exit ticket | 7 | 5 |
| 86.5-88.5 | Looking back | 2 | 2 |
| 88.5-90 | Closing and stamps | 1 | 1.5 |

Cut or moved: Warm-up: 3 picture cards (cars, hens, bicycles) counted in 2s and 4s, questions 1 and 3. Mini-lesson: try1 deleted, try2 items a, b. Teaching block: try3 deleted. Exit ticket: 2 minutes of child work. Deck ws2 text no longer mentions Q7 (Go further 7). No Core item moves: all six fit.

### Lesson 4: Pattern Machines

| New minutes | Part | Old budget | New budget |
|---|---|--:|--:|
| 0-1.5 | Opening | 1 | 1.5 |
| 1.5-6 | Sneak-peek puzzles | 3 | 4.5 |
| 6-10.5 | Warm-up | 4 | 4.5 |
| 10.5-23.5 | Explore | 12 | 13 |
| 23.5-35.5 | Mini-lesson | 12 | 12 |
| 35.5-38.5 | Brain break | 4 | 3 |
| 38.5-52.5 | Worksheet page 1 (pairs) | 14 | 14 |
| 52.5-55 | Check together, page 1 | 2 | 2.5 |
| 55-57.5 | Short teaching | 5 | 2.5 |
| 57.5-69 | Worksheet page 2 (alone) | 12 | 11.5 |
| 69-71.5 | Check together, page 2 | 3 | 2.5 |
| 71.5-76.5 | Flex (spare time) | - | 5 |
| 76.5-81.5 | Talk time | 8 | 5 |
| 81.5-86.5 | Exit ticket | 7 | 5 |
| 86.5-88.5 | Looking back | 2 | 2 |
| 88.5-90 | Closing and stamps | 1 | 1.5 |

Cut or moved: teachtimes and teachgrow moved into the mini-lesson after teachcount; teaching block keeps only teachboth (2.5 min); try2 deleted. Warm-up: 90 s of rhythm, questions 1 and 3. Take-home stars: page 1 Q2(c), Q3(b); page 2 Q4(d), Q5(d). Talk time: the second question dropped (kept only as a note for a pair that finishes early). Flex 5 min.

### Lesson 5: Mystery Number Machines

| New minutes | Part | Old budget | New budget |
|---|---|--:|--:|
| 0-1.5 | Opening | 1 | 1.5 |
| 1.5-6 | Sneak-peek puzzles | 3 | 4.5 |
| 6-10.5 | Warm-up | 4 | 4.5 |
| 10.5-23.5 | Explore | 12 | 13 |
| 23.5-35.5 | Mini-lesson | 12 | 12 |
| 35.5-38.5 | Brain break | 4 | 3 |
| 38.5-41 | Worksheet teach slide | 2 | 2.5 |
| 41-52.5 | Worksheet page 1 (pairs) | 12 | 11.5 |
| 52.5-55 | Check together, page 1 | 2 | 2.5 |
| 55-59.5 | Short teaching | 5 | 4.5 |
| 59.5-71 | Worksheet page 2 (alone) | 12 | 11.5 |
| 71-73.5 | Check together, page 2 | 3 | 2.5 |
| 73.5-76.5 | Flex (spare time) | - | 3 |
| 76.5-81.5 | Talk time | 8 | 5 |
| 81.5-86.5 | Exit ticket | 7 | 5 |
| 86.5-88.5 | Looking back | 2 | 2 |
| 88.5-90 | Closing and stamps | 1 | 1.5 |

Cut or moved: Warm-up: 3 rounds, questions 1 and 3. Explore: setup step 4 and debrief question 3 (does order matter) dropped (teachorder slide and Q5 cover it); pairs 5.5 min. Mini-lesson: try1 item a only, try2 items a, b. Take-home star: page 1 Q1(d). teachthree is optional (no clock time).

### Lesson 6: Market Day

| New minutes | Part | Old budget | New budget |
|---|---|--:|--:|
| 0-1.5 | Opening | 1 | 1.5 |
| 1.5-6 | Sneak-peek puzzles | 3 | 4.5 |
| 6-10.5 | Warm-up | 4 | 4.5 |
| 10.5-23.5 | Explore | 12 | 13 |
| 23.5-35.5 | Mini-lesson | 12 | 12 |
| 35.5-38.5 | Brain break | 4 | 3 |
| 38.5-41 | Worksheet teach slide | 2 | 2.5 |
| 41-52.5 | Worksheet page 1 (pairs) | 12 | 11.5 |
| 52.5-55 | Check together, page 1 | 2 | 2.5 |
| 55-59.5 | Short teaching | 5 | 4.5 |
| 59.5-71 | Worksheet page 2 (alone) | 12 | 11.5 |
| 71-73.5 | Check together, page 2 | 3 | 2.5 |
| 73.5-76.5 | Flex (spare time) | - | 3 |
| 76.5-81.5 | Talk time | 8 | 5 |
| 81.5-86.5 | Exit ticket | 7 | 5 |
| 86.5-88.5 | Looking back | 2 | 2 |
| 88.5-90 | Closing and stamps | 1 | 1.5 |

Cut or moved: Warm-up: two price tags (85c and $57.20), questions 1 and 3. Explore: kit (play money) cut out before the lesson; pair task = find the three $10 baskets and say how they know there are no more; debrief unchanged (3 questions). Mini-lesson: try1 item a, try2 items a, b. Take-home stars: last row of Q1 (bicycle $76), Q2(b), Q3(b), Q4(b). teachchange and teachenough no longer discuss the cut parts (fewest notes, all pairs).

### Lesson 7: Fair Shares

| New minutes | Part | Old budget | New budget |
|---|---|--:|--:|
| 0-1.5 | Opening | 1 | 1.5 |
| 1.5-6 | Sneak-peek puzzles | 3 | 4.5 |
| 6-10.5 | Warm-up | 4 | 4.5 |
| 10.5-23.5 | Explore | 12 | 13 |
| 23.5-35.5 | Mini-lesson | 12 | 12 |
| 35.5-38.5 | Brain break | 4 | 3 |
| 38.5-52.5 | Worksheet page 1 (pairs) | 14 | 14 |
| 52.5-55 | Check together, page 1 | 2 | 2.5 |
| 55-59.5 | Short teaching | 5 | 4.5 |
| 59.5-71 | Worksheet page 2 (alone) | 12 | 11.5 |
| 71-73.5 | Check together, page 2 | 3 | 2.5 |
| 73.5-76.5 | Flex (spare time) | - | 3 |
| 76.5-81.5 | Talk time | 8 | 5 |
| 81.5-86.5 | Exit ticket | 7 | 5 |
| 86.5-88.5 | Looking back | 2 | 2 |
| 88.5-90 | Closing and stamps | 1 | 1.5 |

Cut or moved: Warm-up: 4 of 6 snacks, questions 1 and 3. Explore: 3 strips folded (halves, quarters, eighths), fraction written on one part of each, strips cut before the lesson, debrief questions 1 and 2; 'fold a strip into 3' moved to the Go further box (gaps.json whatif for L7 changed) and take-home. Mini-lesson: we3 merged into we2, try1 and try2 items a, b. Teaching block: tryadd deleted. Take-home stars: Q1(a) explanation, Q4(d) and Q4(e).

### Lesson 8: Shape Builders

| New minutes | Part | Old budget | New budget |
|---|---|--:|--:|
| 0-1.5 | Opening | 1 | 1.5 |
| 1.5-6 | Sneak-peek puzzles | 3 | 4.5 |
| 6-10.5 | Warm-up | 4 | 4.5 |
| 10.5-23.5 | Explore | 12 | 13 |
| 23.5-35.5 | Mini-lesson | 12 | 12 |
| 35.5-38.5 | Brain break | 4 | 3 |
| 38.5-52.5 | Worksheet page 1 (pairs) | 14 | 14 |
| 52.5-55 | Check together, page 1 | 2 | 2.5 |
| 55-59.5 | Short teaching | 5 | 4.5 |
| 59.5-71 | Worksheet page 2 (alone) | 12 | 11.5 |
| 71-73.5 | Check together, page 2 | 3 | 2.5 |
| 73.5-76.5 | Flex (spare time) | - | 3 |
| 76.5-81.5 | Talk time | 8 | 5 |
| 81.5-86.5 | Exit ticket | 7 | 5 |
| 86.5-88.5 | Looking back | 2 | 2 |
| 88.5-90 | Closing and stamps | 1 | 1.5 |

Cut or moved: Warm-up: 4 of 6 solids, questions 1 and 3. Explore: the two paper circles cut before the lesson (kit message), pairs 5.5 min. Mini-lesson: we3 (triangles) deleted and goes home with Q2(b); try1 and try2 items a, b. Teaching block: trycube and trynet deleted. Nets A-D cut out beforehand. Take-home stars: Q1(c), Q2(b), Q4(b).

### Lesson 9: Measure Masters

| New minutes | Part | Old budget | New budget |
|---|---|--:|--:|
| 0-1.5 | Opening | 1 | 1.5 |
| 1.5-6 | Sneak-peek puzzles | 3 | 4.5 |
| 6-10.5 | Warm-up | 4 | 4.5 |
| 10.5-23.5 | Explore | 12 | 13 |
| 23.5-34 | Mini-lesson | 12 | 10.5 |
| 34-37 | Brain break | 4 | 3 |
| 37-51 | Worksheet page 1 (pairs) | 14 | 14 |
| 51-53.5 | Check together, page 1 | 2 | 2.5 |
| 53.5-58 | Short teaching | 5 | 4.5 |
| 58-69.5 | Worksheet page 2 (alone) | 12 | 11.5 |
| 69.5-72 | Check together, page 2 | 3 | 2.5 |
| 72-76.5 | Flex (spare time) | - | 4.5 |
| 76.5-81.5 | Talk time | 8 | 5 |
| 81.5-86.5 | Exit ticket | 7 | 5 |
| 86.5-88.5 | Looking back | 2 | 2 |
| 88.5-90 | Closing and stamps | 1 | 1.5 |

Cut or moved: Warm-up: 3 of 6 prompts (door, rice, brushing teeth), questions 1 and 3. Explore: balance hung and tested before the lesson, glue stick only (spoon is a take-home), pairs 5.5 min. Mini-lesson 10.5 min: try1 items a, b, try2 deleted, we2 said from the SAY lines. Teaching block: teachlen and trytime deleted. Take-home stars: Q2(b), Q4(b), Q5(c). Flex 4.5 min.

### Lesson 10: Challenge Day

| New minutes | Part | Old budget | New budget |
|---|---|--:|--:|
| 0-1.5 | Opening | 1 | 1.5 |
| 1.5-6 | Sneak-peek puzzles | 3 | 4.5 |
| 6-10.5 | Warm-up | 4 | 4.5 |
| 10.5-23.5 | Explore | 12 | 13 |
| 23.5-33.5 | Mini-lesson | 12 | 10 |
| 33.5-36.5 | Brain break | 4 | 3 |
| 36.5-39 | Worksheet teach slide | 2 | 2.5 |
| 39-51 | Worksheet page 1 (pairs) | 12 | 12 |
| 51-53.5 | Check together, page 1 | 2 | 2.5 |
| 53.5-57 | Short teaching | 5 | 3.5 |
| 57-68.5 | Worksheet page 2 (alone) | 12 | 11.5 |
| 68.5-71 | Check together, page 2 | 3 | 2.5 |
| 71-75 | Flex (spare time) | - | 4 |
| 75-80 | Talk time | 8 | 5 |
| 80-85 | Exit ticket | 5 | 5 |
| 85-87 | Looking back | 2 | 2 |
| 87-90 | Certificates and closing | 3 | 3 |

Cut or moved: Warm-up: 3 relay cards (digits, change, fractions), questions 1 and 3. Explore: the four station cards on ONE slide (card1-4 merged into 'cards'), pairs take two cards, 4.5 min of pair work; debrief keeps all three questions. Mini-lesson 10 min: teach1 and try1 deleted, try2 items a, b, we1-we3 and key stay. Take-home star: page 1 Q3 (coins table). Exit ticket 2 min of child work, certificates 3 min, reflect label corrected (85-87). Flex 4 min.

## Not applied, or applied differently

- **reccues.js (shared, not edited):** its `mins()` reads the first two integers of a range, so half-minute ranges such as `10.5-23.5` would be read as `5-23`. `p2/guide.js` therefore passes the cue a whole-minute range (`0-N`, N rounded from the real duration), so the REC lines say "about 5 minutes" for the 4.5-minute sneak-peek and "about 13 minutes" for the explore. The guide still prints the exact half-minute range. The lead may want `mins()` to accept decimals.
- **Flex has no slide:** it is a guide segment and a part in `budget.json` only (a spare block, no content to show).
- **Slides that "go with" a take-home** (L1 teachcount, L2 teachtri, L4/L9 teachlen, L8 we3) are removed from the deck (as asked) and are not posted anywhere else; their idea is in the check-together notes. Posting them with the weekly email would be a separate job.
- **Pairs and breakout rooms for the worksheet** are unchanged (main room); the audit notes +3 min per lesson if rooms are used there.
- **Workbook star for L7 Q4(d), (e):** the sums are inside one picture, so the star and words are in the question line plus a small star beside d and e in the figure.
- The audit remains a desk model: re-time L1, L4 and L9 live and re-set `PLAN` in `rebuild/p2budget.py`.
- Shared-file issues for the lead: `levels/reccues.js` decimals (above); `docs/audit/timing_p2.py` was extended (new `--rebudget` mode, L10 mini slice) and its as-scripted `--summary` and `--fixed` modes no longer run on the re-budgeted decks (they reference deleted slides).
- Other agents are editing P3-P6 and `docs/audit/timing_p6.py` in the same working tree; none of those files were touched by this pass. Nothing was committed.
