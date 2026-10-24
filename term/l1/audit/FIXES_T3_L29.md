# Fix pass, Term 3 Lesson 9 (lesson 29, Spot the Mistake)

Against `WORKBOOK_AUDIT_L29.md`, `GUIDE_DECK_AUDIT_L29.md` and `HOME_PARENT_PRACTICE_AUDIT_L29.md`. Rebuilt with `bash term/l1/build.sh 29`: validator 22 pass, 0 FAIL (verify: independent checks extended for every changed number); parts sum to 90, no part OVER (script 67:40, slow 79:54); workbook fills 94, 99, 97, 94, 99% (kit page 69%, by design); home 99%, parent page 1 page 99%. Viewed: all 6 workbook pages, key, home sheet, parent page, slides 9, 10, 24, 29.

| Finding | Action |
|---|---|
| WB 1 T1 two defensible answers | Stem now says "Step 1 takes away 30 on purpose, because 29 is close to 30. That is a good first step." so only step 2 can be wrong; key solution and "watch for" rewritten. |
| WB 2 / GD 4 S5 repeats Mini-lesson prices; E1 turns Talk sum; G3 example repeats Investigation | S5 is now bag $7, cup $5, child says $10 (answer $12); E1 is now 82 - 47 = 45 (check 45 + 47 = 92, No); G3 example is 38 + 15 = 43. Script, slide notes, tutor prep, key, verify registry updated; checker asserts no shared numbers with the class examples. |
| WB 3 kit cut cells 3.3-4.3 mm apart, pale labels, 50% empty | NOT fixable in lesson data: the card positions, gaps and RIGHT/WRONG label colour are fixed in `tools/figs3.py mistake_cards()` (only the card texts come from the lesson). Shared-tool need (see FINAL_FIXES_T3.md): gaps of at least 6 mm, black labels. Kit intro now carries the "No cards? Write each sum on a small piece of paper" fallback. |
| WB 4 black and white print build | Shared tool (print pipeline); listed for FINAL_FIXES_T3.md. No question depends on colour (verified). |
| WB 5 / GD 2 L20 hand-off (clock optional, no cut-out hands or tokens) | `l20.json` is owned by the Term 2 fix agent: not edited. Mismatch reported: it should say "a grown-up cuts out the 6 clock hands; keep the $1 tokens". |
| WB 6 Investigation slot | "34 - 19 = ____ . Is it right? Yes or No." now has a blank and a Yes/No; the writing lines are chosen by the tool (4). |
| WB 7 T1/T3 "say why" and drawing box | Not changed: pages 3 and 4 are 94-99% full; a new line would push content onto a new page. T1 now explains why step 1 is allowed, which removes the need. |
| WB 8 / GD 3 timing 17 vs 18.5 | Per-question estimates trimmed (S2 3, S4 2.5, S5 2.5) so Start here is about 17 (page 1 about 9, page 2 about 8); page slots 9:00 and 8:20; choice time 3:20. Note in `timing.notes` updated. |
| WB 9 "We use them again" | Printed by `tools/b_print.py` (shared). Listed. |
| WB 10 look-back wrap | Shared template. Listed. |
| WB 11 G1 "Watch for" | Not present in the current key text (no change needed). |
| GD 1 your-turn warm-up answers missing | Chant and NOTE now give 50, 73 and 9:00. |
| GD 5 Explore recap gives Talk question away | Third bullet of `s-explore3` removed; the recap SAY and the note no longer state the "same way again" idea, so Talk time is a real question. |
| GD 6 Explore round 1 too tight | Round 1 150 s to 180 s; recap question 55 s to 40 s (explore 9:06, slow 10:49 of 11:00). A full 3:30 would put a slow class OVER; the guide's skip order and the flex buffer cover the rest. |
| GD 7, 8 small slide thumbnails | Template (`tools/b_deck.py qs_block`); listed. |
| GD 9 "Teach it back" answer line | Not changed (menu text; Low). |
| GD 10 "ones were swapped" | Now "6 take away 4 was done instead of 4 take away 6" in the table, script and notes. |
| GD 11 REC cue order, "papers to the camera 30 s" | Cue order is the shared Term 1/2 pattern; the clause is printed by `tools/b_guide.py` (shared). Listed. |
| HP 1 online static items repeat workbook | c3 (39 + 24 = 53), c4 (58 + 15, step 1 wrong), t2 (48 + 41 = 189), t3 (Mei 36, 7 fewer), g2 (63 - 29) are new; template ranges changed so no variant reproduces a workbook item; verify script updated. |
| HP 2 c3 variant over 100 | a range changed (57 removed); checker asserts a + b <= 99. |
| HP 3 parent beyond statement, no "do not teach rounding" | `beyond.parent` now names the estimate and the column-sum digit and says "say about and near, not rounding". |
| HP 4 H1 blank | Longer line; the blank now sits on its own line. |
| HP 5 H2 clock picture | Not added (Low; sheet 99% full). |
| HP 6 recording statement on parent page | Added "The recording link is private: please do not share it." in `parent.next` (a longer sentence made the page spill; the tool-printed "Every lesson is recorded" stays). |
| HP 7 rewind items, HP 8 online header "Lesson 9" without term, HP 9 slips | Runner/shared (header, rewind); variant slips left. Listed. |
| Hand-off wording | `parent.next_materials`, goodbye line and tutor prep now say: calendar page torn out with the 7 day cards cut by a grown-up, Quest Log closed in an envelope, a quest partner; matches `l30.json` materials (checker enforced). |

## Shared-tool needs (for FINAL_FIXES_T3.md)
1. `tools/figs3.py mistake_cards`: 6 mm cell gaps, black RIGHT/WRONG labels (mat labels pale blue-grey).
2. Black and white print build of workbooks (owner request).
3. `tools/b_print.py` kit text "We use them again" is wrong for kits not reused (cards of L29, day cards of L30).
4. `tools/b_guide.py`: remove "papers to the camera 30 s" from the timing assumptions.
5. Deck `qs` blocks: question tables are thumbnails beside large text (L29 slide 22).
6. Online practice page subtitle lacks the term; no rewind items.
7. Look-back box wraps badly.
8. `l20.json` hand-off to Term 3 (clock optional; cut-out clock hands; $1 tokens): owner is the Term 2 fix agent.
