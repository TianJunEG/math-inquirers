# Level 1 Extension Workbook: fixes after the diagram audit (docs/audit_final/diagrams_extension_p1.md), 23 Oct 2026

Welcome page, Unit 1 Q7/Q8 and the contact email were done earlier (0998df9) and are not touched. Existing figure helpers only; no new figure library. Two small option additions to existing helpers (below) and one layout key.

`extension/verify_all.sh 1`: ALL GATES PASSED (answers, duplicates, wording, build, B&W vector and 1-bit, check_bw, fill/overflow). No overflow PROBLEM lines remain. Both books are 98 pages (even); contents and answer page numbers unchanged. Every changed page was viewed in the 1-bit print file; most were also viewed in colour. Answers and Why lines were not changed (every figure only shows what the text already says; the verify checks still pass).

## Tool changes
- `render.py` / `ext.css`: item key `figright` puts the figure beside the question text (saves height).
- `figs.py` `dot_boxes`: option `layout: "ell"` (steps of 1, 3, 5, 7 blocks, equal frames, a None count is a dashed frame).
- `figs_l1_u03_u04.py`: `stick_rows` options `mark` (number in each triangle) and `lab`; `towers` option `frame` (open top, no grid); half picture is now a closed half with a solid edge.
- `figs_l1_u05_u06.py`: note sizes differ more.

## D faults fixed
- p32 G2: Mei's row is 3 triangles, each numbered 1 to 3, drawn larger (Ravi's too).
- p30 Q12: Tower 4 frame is open at the top, no grid, 13 blocks tall (answer is 11).
- p17 T1: 7 empty rows (answer 6); T3 now has 4 lines (answer 3). p45 T3: 5 rows (answer 3). p45 T1: 4 set lines (answer 2). Think harder pages of Units 2 and 6 use `snug` spacing to fit.
- Learn it overflow (pp. 6, 13, 20, 48, 69): figure widths trimmed (U1, U2, U7, U10); U3 worked example uses a side layout and larger symbols (Try graph also larger). p20 and p69 no longer touch the footer. Pages 6 and 69 sit within 0.5 mm of full: a later change to those pages must trim something.
- p8 Q9: blocks drawn as steps (L shapes, 1, 3, 5) with a dashed Step 4 frame of the same size.
- p24 T1: half face is a clear closed half (also in the key).
- p42 Q2: notes now clearly different sizes, bigger.
- p53 G1 shapes about 20 mm (were 13); p54 C3 picture larger; p59 T1 logic grid 74 mm (matches Q9); p71 Q7 shapes about 20 mm.

## Top-15 diagram items done (existing helpers)
- 5: p35 Q1, Q3, Q5 and p38 T1 as chains with a "?" start (answers still found by the child).
- 6: p36 Q9 lift as a chain (down 4, up 6).
- 7: p37 Q10, Q11 queue rows with numbered places (Kumar 6th, Aisha 5th); p56 Q2, Q3 queue rows.
- 8: p56 Q1 and p71 Q8 ladders (oldest to youngest) with `draw`; p57 Q6 bars of 5 to 9 sweets.
- 9: p63 Q2 bars (tape 13, strip 8); p66 T2 nested clip, pen, bag bars.
- 10: p72 Q12 and p73 T3 chains; p71 Q8 ladder.
- 11: p28 Q5 (C C S row of ten places), p29 Q11 and p31 T3 (day tables with "+2" and "?" steps).
- 12: p15 Q8 shelf (2 rows of 10), p46 G2 bar for the $50 note.

## Not done, and why
- p39 G3 well (12 steps): page 39 is full and no existing helper draws a step well.
- p63 Q4, p64 Q6, p65 Q14 (bars), p72 Q13 bar: pages are at 99 to 100 percent; a bar there made the page overflow, so they were removed again.
- p18 G1, G2 (two stacks, jars), p9 Q12 jar and coin table, p56 Q4 / p57 height bars: no space (p18 99 percent) or no existing helper (jar with coins by day).
- p9 Q13 number strip (cells already about 9 mm, no start marker), p11 G1 triangle dots, p27 worked example 2 arcs: Low, left.
- Items 13 to 15 (P1 puzzle pack, P1-05/06/18/03/13, colour-by-code CBC-13): outside the Extension Workbook; need the P1 generators.
- Not asked, left: option circles for every "Circle ..." item; all B items; Q7/Q9 shapes still below the audit's 30 mm; spare-row rule not checked by a script.
