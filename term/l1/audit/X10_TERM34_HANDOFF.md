# X10 Terms 3 and 4: hand-off to the books job

23 Oct 2026 (night). Owner decisions applied: RETIRE-YES (Fill the Grid retired), X10-BEFORE, L39-YES. Nothing pushed; books, specs, kit sources and decks NOT rebuilt by this job. `term/l1/out/` is git-ignored: the lesson JSON, `verify/` scripts and `AUDIT_L*.md` are the committed record. Quest v2 itself is described in `X10_QUEST_HANDOFF.md`.

## What changed in the lessons
| Lesson | Change |
|---|---|
| 26 The School Shop | Next-lesson card, closing SAY line, parent `next` and `next_materials`, tutor_prep: now Calendar Detective (calendar page torn out, 7 day cards cut out). Price tags and play money still kept for the Quest. `verify/l26_checks.py` hand-off check updated. |
| 27 Calendar Detective (was Fill the Grid) | The old Lesson 30 content moved here (`id l1-t3-07`, lesson_in_term 7, practice key `t3l27`), Quest removed, ordinary skeleton (Explore 12, Mini 10, Workbook 32, Talk 6, live exit ticket 6, Look-back 2, Flex 6), `calendar_cards` kit now in Book 6 lesson 7. Fill the Grid is retired (its elimination idea survives as Think harder T3 in lesson 30, solved with a table). `verify/l27_checks.py` is new (from the old l30 checks). |
| 29 Spot the Mistake | Next-lesson card, closing line, parent `next` and `next_materials`, tutor_prep: now Tool Detectives and the Quest (Quest Log closed, quest partner, tool-card page with 7 tool cards cut out). |
| 30 Tool Detectives (NEW) | Choose-the-tool consolidation lesson hosting Quest v2 (`tool_row: "term"`, 7 tools). Quest gates: 1 clock/am-pm/half hour (21 to 23), 2 coins and change (24), 3 prices (25 and 26), 4 calendar (27), 5 sticks (28), 6 wrong sum (29), 7 and 8 mixed gates (money at first; five and ten cent coins), cave with `because`. Quest Log 4 pages, `quest_map` false. Start here has a tool line and an I checked tick; Think harder names tools; Go further names none; Investigation writes a problem for a tool. Originals only. `verify/l30_checks.py` is new. |
| 39 Problem-Solving Toolbox | Rebalanced to the eight card names (Strip and Draw it become Draw it; Steps becomes Act it out; Table becomes Make a table (and Spot the pattern); List becomes List every way; Find one first becomes Try something simpler; Guess and check is now named, problem card 7 changed to a coin problem). Kit is now a `cards` page of 8 tool cards and 8 problem cards (was `tool_cards`, 7 + 8). |
| 40 Inquirers' Showcase | Reframed: Quest v2 (`tool_row: "term"`, 8 tools), gates 4 (new coin gate) and 7 (tower pattern, tool names removed) are mixed gates, cave `because`; Remember shows the whole toolbox; Showcase frame adds "my tool and why, and a check"; Start here S4 to S6 get a tool line and tick. Quest Log 4 pages (page 2 is 75% full). Lessons 35 and 39 are no longer visited by a tagged gate. |

Earlier Books 5 to 8 audit fixes (L35 pair cards and tiles, bar-model white pills, Quest gate 6 sticks) are untouched: no L35 file, no figure tool and no stick figure was edited.

## What the books job must change
1. **Book 6 (lessons 26 to 30).** Composition changes: lesson 27 workbook is now the calendar lesson (5 pages + the `calendar_cards` kit page; the grid-tile kit is gone); lesson 30 is Tool Detectives (5 pages + a tool-card kit page, `cards` type, 7 cards; the old calendar kit leaves lesson 30); Quest Log L30 (4 pages, 7-tool row); Quest Tutor Notes L30 now 9 pages (about 7 before); Quest Parent Note 1 page. Re-read real page counts and the even-page rule after the build.
2. **Book 8 (lessons 36 to 40).** Lesson 39 kit page is a different kit type (cards; page count still one kit page), lesson 40 Quest Log 4 pages (8-tool row) and Quest Tutor Notes 10 pages (about 7 before).
3. **Kit pages and kit list.** Book 6: swap `grid_tiles` for `calendar_cards` at lesson 27 and add the tool-card page at lesson 30; Book 8: lesson 39 cards page. The Inquirer Kit A5 toolbox card is the picture version of the same eight names.
4. **Quest Logs, answer keys, home packs.** Regenerate `L30_Quest_Log`, `L40_Quest_Log`, both Quest Tutor Notes (new gate tags: mixed gates 7 and 8 in L30, 4 and 7 in L40; answer-sheet tags "Lesson 27" for the calendar gate), both Quest Parent Notes, `L27` and `L30` answer keys, Home Practice and Home Answers (L27 and L30 home sheets swap), Parent Summaries for 26, 27, 29, 30, 39, 40. Online practice ids: `t3l27` (Calendar Detective, same items as the old `t3l30`), `t3l30` (new items), `t4l39` (items renamed), `t4l40` (rewind items r1 and r2 now point to Term 3 Lesson 7).
5. **Deck.** Decks for 26, 27, 29, 30, 39, 40 and the guide PDFs.
6. **B&W.** Not checked here (books are not rebuilt): run `check_bw.py` on Books 6 and 8. The tool pills use the stroke icons from `levels/spine_icons` (ink on white).
7. **Print quote.** `outputs/print/term/term_books_spec.json` and `docs/printing/quote_request.md`: key-book pages for Books 6 and 8 grow with the longer Quest Tutor Notes.

## Open points for later jobs
- `term/l1/spine_term.json` rows for lessons 27, 29 and 30 are out of date (27 is no longer Fill the Grid, 30 is no longer Calendar Detective); set 27 to pattern with act it out, 30 to choose, and update titles. The spine routine (`apply_spine_term.py`) has not been applied to these lessons yet; the Start here tool line in lessons 30 and 40 is the lesson-level version of the "tool I used" tick.
- `verify/l39_checks.py` and `verify/l40_checks.py` used to compare the home rewind item (H5) with the text in lessons 19 and 20 as built on 23 Oct. The Term 2 rebuild reworded those items, so the checks now verify only the arithmetic; confirm the H5 rewind source text with the Term 2 lesson owner.
- Lesson 40 tool row has 8 pills per gate and lesson 30 has 7: small print; trial the Quest pace and readability.
- Lessons 35 and 39 have no tagged Quest gate any more (mixed gates carry the tool habit).
- `build.sh` of any lesson rewrites `school/p1/out/validation_report.txt` and `verification.json` (the validator copy check touches the P1 school pack); those were restored and not committed.
- Slide `s-ws1` of lesson 26 reports a layout overflow warning in the deck build (it was there before this job).
