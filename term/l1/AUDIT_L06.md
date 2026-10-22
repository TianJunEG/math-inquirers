# Self-audit: Level 1 Term 1 Lesson 6 (Tens Jump, Ones Hop)

Desk audit by the author (a model); no child has used this lesson. Machine checks: `python3 term/l1/tools/validate.py 06` (19 pass, 0 warn, 0 FAIL). Real-PDF check: workbook 6 pages (fill 96%, 99%, 98%, 90%, 92%, kit page 89%), home sheet 2 pages, parent page 1 page.

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
| 10 | No overclaims | PASS | validator; strand label tutor-only |
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

## Known limits and template issues (not failures)

- **New-topic lesson**: the syllabus placement (mental 2-digit plus or minus tens or ones without renaming, 2.7) must be checked by the owner or a tutor.
- **No number-line picture type** in `tools/svg.py`. Worked around with "jump strips" in the slide data (a numrow whose yellow tiles are landing numbers and white tiles are the jumps), kit pictures, and children drawing their own number lines in the draw boxes. A real `number_line` visual (arcs between marks) would be much clearer for this lesson.
- Template text hard-coded to Lesson 1 in `tools/b_print.py`: home sheet title "Bundles and Singles: practice at home" and "draw bundles"; parent page "Lesson 1" and big "1", and the quote suffix "Ten singles tie into one bundle."; workbook header strand "Whole numbers: tens and ones"; page 3 hint "open a bundle". Guide text "Clock checks: minute 14" assumes a 4-minute opening (this lesson's sneak-peek ends at minute 12).
- Investigation writing space on page 5 is one line (template); children may use spare paper.
- Slides use less than half the 1920x1080 canvas on several mini-lesson slides (same as Lesson 1).
- Never trialled with children; times and difficulty are modelled.
