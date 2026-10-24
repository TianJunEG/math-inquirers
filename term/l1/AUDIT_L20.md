# Self-audit: Level 1 Term 2 Lesson 10 (Choose Your Tool, with Mi's Challenge Quest)

New lesson written 23 Oct 2026 (night) for the X10 consolidation (plan `docs/pedagogy/lesson_x10_consolidation_plan.md`, Term 2). It replaces the old lesson 20 content (Find One First moved to lesson 19). Rubric: `docs/audit/reaudit_p1.md`. The old audit of Find One First is now `AUDIT_L19.md`.

## Automatic checklist (validator, build of 23 Oct 2026)

| Criterion | Result | Evidence |
|---|---|---|
| Schema, identity (term 2, lesson 20, lesson_in_term 10, key t2l20) | PASS | validate.py 20: 0 FAIL |
| Every answer recomputed independently | PASS | `verify/l20_checks.py`: queue places by listing, "I think of a number" by trying every number forwards, prices by trying every price, picture equation by trying every pair, every Quest gate and the cave |
| Online practice | PASS | 10 items (5 core, 3 stretch, 3 challenge incl. one self-check), template variants verified by expression, oracle and runner JavaScript |
| Timing | PASS with warnings | 90 minutes; Quest at minutes 35 to 55; slow-class need 86 of 90; slow-class OVER warnings on opening, explore, mini, work (the buffer absorbs it); remember loose |
| Real PDF checks | PASS | workbook 6 pages, parent 1 page, home 1 page, Quest Log 4 pages, Quest Tutor Notes 9 pages, grown-up note 1 page |
| B&W | PASS | workbook and Quest Log through `print/make_bw_print.convert_pdf` and `check_bw`: 0 non-grey |

## Judgement lines (author)

- Job: no new idea. Remember = toolbox page of six tools with pictures and three tiny uses; Sneak-peek = two puzzles that want different tools, no tool named; Explore = tool market (six problem cards, nobody solves, two cards have two good tools); Mini = one problem solved with two tools, checked a third way, then "Wait. Try a tool. Try a smaller case. Ask." on a stuck problem.
- Tiers: Start here 6 items, one or two steps, fresh numbers, each with "Tool I used" and "I checked" (tool names fade after Think harder). Think harder 4 (same problem with a second tool and which was quicker; backwards with a forward check; queue counting with both ends; numbers two counting lists share). Go further 3 (price of one in two shops, three-step puzzle reversed, picture equation with a sum and a product). Investigation: write a problem for a tool, with an easy first step.
- Beyond Primary 1, named in `moe.note`, `beyond` and the parent text: choose-and-justify a tool, second tool, queue counting with both ends, common numbers of two counting lists, three-step reverse, two-shop price of one, sum-and-product picture equation. Non-routine types named: queue counting, "I think of a number", odd/even claim, price of one first, shapes as numbers.
- Quest v2: `tool_row: "term"` (six tools met by Term 2), six tagged gates (11+12, 13, 14+16, 15+17, 18, 19) and two mixed gates (7, 8), cave with a "because" line, new privacy line, no tool named in any gate (checked in verify). Gate pages 1/2/3/4 give a 4-page log (3 pages overflowed by 3% of a page).
- Wording guide: story first, command last, fixed question words, numerals, boxes for single digits; no MOE/GEP/SASMO claims; no price; Mi shown without a calculator.
- Known gaps: the tool cards kit page heading is hard-coded "cuts out all 15" in the shared figure (15 cards are supplied: 7 tool cards incl. "In my head", 8 problem cards, two blank). Tool icons for Act it out and Spot the pattern reuse existing pictures (person, steps) because no dedicated figure icon exists. No child has taken this lesson; run it with a real group before Term 2 starts.
