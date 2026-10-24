# X10 Term 2: hand-off to the books job (and others)

23 Oct 2026 (night). Implements Term 2 of `docs/pedagogy/lesson_x10_consolidation_plan.md` (owner: RETIRE-YES for Doubles and Near Doubles, X10-BEFORE). Lesson files l01..l40 and the 40-lesson total are unchanged. Books NOT rebuilt, nothing pushed. Built and validated (0 FAIL): lessons 12, 13, 18, 19, 20.

## Slot map now
| File | Content | Source |
|---|---|---|
| l12 | Bar Strips (unchanged); next-lesson card, closing line, parent next and next_materials now say Picture Equations (counters page 6, shape cards page 7, 30 counters, 2 cups) | hand-off only |
| l13 | **Picture Equations** (id l1-t2-03, key t2l13) | old l19. Doubles absorbed: warm-up asks 7 + 8 as 1 more than 7 + 7; Start here Q3 part b (8 + 9) and new Q6 (ten-frame, double 7 and 1 more). Start here is now 6 items (old S4 three stars and S7 sweets bags dropped so pages 1 and 2 do not spill). Doubles lesson retired; its files are in `audit/retired_L13_doubles/` |
| l18 | Times Stories (unchanged); next card, closing line, parent next and next_materials now say Find One First (tokens page 6, shop items) | hand-off only |
| l19 | **Find One First** (id l1-t2-09, key t2l19) | old l20, Quest removed, ordinary skeleton (Explore 12, Mini 12, Workbook 30, Talk 6, live exit ticket 6, Look-back 3, Flex 5), new Explore round 4 and Mini "check it" slide; kit still the $1 tokens page; next card points to Choose Your Tool and the Quest |
| l20 | **Choose Your Tool** (new; id l1-t2-10, key t2l20), hosts the Quest | new |

## What the books job must change
1. **Book 3** (lessons 11 to 15): l13 is Picture Equations now. Kit pages: ten-frames (page 6) and shape cards (page 7) stay in Book 3 (they come with Picture Equations); the Doubles dominoes/ten-frame kit is gone. Workbook 7 pages (5 plus 2 kits), as before for Book 3 only if the old Doubles lesson had 7; re-read the real page count from `out/l13/L13_Workbook.pdf`.
2. **Book 4** (lessons 16 to 20): l19 workbook is Find One First (6 pages incl. the tokens kit); l20 workbook is Choose Your Tool (6 pages incl. the tool cards kit page: 15 cards). Book 4 loses the shape cards kit and keeps tokens. Quest Log for l20 is **4 pages** (was 3: the tool row adds about 14 mm per gate; 3 pages overflowed by about 3% of a page). That is +1 sheet-side in Book 4 (check even page count); Quest Tutor Notes are 9 pages (was 7). Loose `L20_Quest_Log.pdf`, `L20_Quest_Parent_Note.pdf` are regenerated.
3. **Quest answer key**: l20 gate tags are now [11,12], 13, [14,16], [15,17], 18, 19, mixed, mixed (gate 8 hats and scarves, gate 7 number puzzle). Home answers: l13, l19 home sheets and answers moved with their lessons (build ordering by lesson number).
4. **Online practice ids**: `t2l13` (Picture Equations, formerly `t2l19`), `t2l19` (Find One First, formerly `t2l20`), `t2l20` (Choose Your Tool, new). Any index of practice sets must change.
5. Quote page counts (`outputs/print/term/term_books_spec.json`, `docs/printing/quote_request.md`): Books 3 and 4 re-measured after rebuild.
6. Rebuild l12, l18 parent summaries, guides and decks (hand-off lines), already built here.

## Other lesson files that mention renumbered content (not mine; for their owners)
- l08 (line 44 of the JSON): "Term 2 Lesson 9 (Picture Equations) builds on balance" should say Term 2 Lesson 3.
- l23 and l24 (several lines): "$1 tokens from Term 2 Lesson 10" should say Term 2 Lesson 9 (Find One First holds the tokens page). l20's goodbye and parent page already say Lesson 9.
- `term/l1/spine_term.json` rows 13, 19, 20 still describe Doubles, Picture Equations and Find One First in the old slots; the strategy-card applier (`apply_spine_term.py`) will put the wrong tool of the day on the moved lessons until they are updated. Suggested: 13 Picture Equations (main guess or backwards, also list), 19 Find One First (draw, table), 20 choose (tool row of six).
- Kit/hand-off checker: l14 `materials` mentions "counters from the Term 2 Lesson 3 kit page": still true (Picture Equations kit has the counters page).
- Lesson 13 Think harder T2 and Go further G1 use a times line before Equal Groups (Term 2 Lesson 5); the warm-up shows groups of and the times sign; flagged in `joining_cold.note`.
- `docs/terms/level_1_year_plan.md`, `docs/pedagogy/lesson_x10_consolidation_plan.md` and parent outcomes still list the old slot titles for Term 2.

## Known gaps
- Shared figure `tool_cards` prints the heading "a grown-up cuts out all 15" (hard-coded); l20 supplies exactly 15 (7 tool cards incl. "In my head", 8 problem cards, two blank), so it is correct.
- No dedicated tool icons for Act it out and Spot the pattern in the figure set (person and steps pictures reused). The spine icons in `levels/spine_icons` are used by the Quest Log tool row.
- Per-lesson audit files: old l19 and l20 audits were renamed to l13 and l19 with a "re-audit pending" banner; `AUDIT_L20.md` is new. Workbook, home and wording audits for 13, 19, 20 are not re-run.
- Lesson 13 Start here is shorter (about 15 minutes) so choice time grows; l12/l18 changes are hand-off lines only.
