# Self-audit: Level 1 Term 1 Lesson 6 (Tens Jump, Ones Hop)

Desk audit by the author (a model); no child has used this lesson. Machine checks (after the fix pass of 22 Oct 2026): `python3 term/l1/tools/validate.py 06` 17 pass, 0 warn, 0 FAIL; 357 answer checks; 1788 practice variants. Real-PDF check: workbook 6 pages (fill 93%, 84%, 87%, 84%, 96%, kit page 91%), home sheet 2 pages (93%, 43%), parent page 1 page (95%).

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | Schema valid | PASS | validator |
| 2 | Every answer verified independently | PASS | 331 checks in `verify/l06_checks.py`: every sum is recomputed by walking the number path one step at a time; every jump strip and sum tile on a slide is re-added |
| 3 | Online practice variants verified | PASS | 1788 variants: expression = brute-force walk or breadth-first search = runner JavaScript; every variant also asserts no hop passes a ten (no renaming) |
| 4 | Timing sums to 90, no part OVER | PASS | script needs 74:28; slow-class 88:22; opening 2 min, Explore 16 min |
| 5 | Timing realistic for ages 6-8 | PASS with caveat | modelled, not stopwatch. Start here needs about 19 min for a middle child (7 questions); page 2 is longer than its 9-minute slot, covered by the check slides |
| 6 | Tier principle | PASS | Start here: jump (tens) and hop (ones) separately, one draw-it number line. Think harder: jump then hop, take away, order does not matter (frogs), undo. Go further: 7 to 97 jumps, fewest jumps with 10 and 20, a chain. No contest move at Start here |
| 7 | Neutral labels, nothing named publicly | PASS | validator; choice slide and page 1 line |
| 8 | Sneak-peek access plus thinking, unmarked, papers once | PASS | slide 5, script |
| 9 | No private chat; safeguarding | PASS | no breakout rooms; movement break has a safe-space line |
| 10 | No overclaims | PASS | validator; strand label tutor-only; tutor guide and parent page now say Term 1 goes beyond the school Primary 1 syllabus on purpose, no MOE-aligned claim |
| 11 | Ruler only if the child has one | PASS | not needed; parent and home mention "a ruler helps" only |
| 12 | Materials home-findable | PASS | the Lesson 1 kit cut-outs; nothing to buy |
| 13 | Recording cues short, with child action | PASS | 11 cues |
| 14 | Joining cold | PASS | Remember re-teaches counting in tens from any number, tens and ones, counting on ones, all with bars and squares; Lesson 6 flagged as hard to miss |
| 15 | No copied contest text | PASS | validator |
| 16 | Layout | PASS | 32 slides, no overflow, no Mi overlap reported; all 6 workbook pages, deck, guide, key, home sheet and parent page viewed |
| 17 | Printed answers separate | PASS | key is its own PDF |
| 18 | Reading load | PASS | no string over 40 words |

## Instrument A (gifted-style, 0 to 2 each)

1 low floor high ceiling 2; 2 depth over speed 2; 3 generalise 2 (jumps never change the ones digit; Investigation Jump road); 4 justify 2 (S6, T3, talk); 5 multiple paths 2 (kit, number line, jump first or hop first); 6 challenge ladder 2; 7 student-led inquiry 1; 8 complexity/context 1; 9 problem posing 1 (spare-time M2 and online g4 only); 10 metacognition 2; 11 pacing/compacting 1; 12 extension not acceleration 2. **Total 20/24.**

## Fix pass, 22 Oct 2026 (after the independent audit)

Independent audit (`audit/WORKBOOK_AUDIT_L06.md`) scored the printed workbook 14/24 on the gifted rubric and 12/14 (86%) on tier compliance. After the fixes, re-scored by the fixer (a model, desk review, same rubric):
- Gifted rubric, workbook only: 4 justify 1 to 2 (S6, T3c, G2b, Investigation); 5 multiple paths 1 to 2 (G1 asks for two different routes); 9 problem posing 0 to 1 (G1 "a different way" is open, but there is still no make-up item); others unchanged. **17/24**, an estimate.
- Tier compliance: Start 7/7, Think 4/4, Go 2/3 clear and G1 borderline (open route-finding with two jump sizes, no longer a plain count in tens): **13/14 (93%)**, honestly judged.
- Start here now stays inside P1 mental calculation (jump and hop, no 2-digit + 2-digit); the exit ticket has no beyond-P1 item (E3 is jump 2 tens then hop 3 from 52).
- Open items: template and tool issues listed in `audit/FIXES_L06.md` (page 2 has no instruction line, look-back print size, key heading orphan, Mi calculator, Circle wording on the Investigation); no child has used the lesson.

## Known limits

- **New-topic lesson**: the syllabus placement (mental 2-digit plus or minus tens or ones, no renaming, 2.7) must be checked by the owner or a tutor.
- Rebuilt on template commit 8bce095: jump pictures now use `svg.number_line` (mini-lesson, explore, sneak-peek answer, optional slide); `workbook.kits` is the base-ten page (same as Lesson 1); template leak check passes; the home sheet was shortened back to 2 pages. Checks now 346, validator 0 FAIL, 0 WARN. Workbook fill 97, 100, 100, 91, 93%, kit 91%.
- The two small number lines on the "Hop: ones" slide are small (two columns).
- Investigation writing space on page 5 is now 4 lines (template commit 2379b77).
- Never trialled with children; times and difficulty are modelled.
