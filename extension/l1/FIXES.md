# Level 1 Extension Workbook: fixes after the independent audit (AUDIT.md, 23 Oct 2026)

Done 23 Oct 2026. Gates: `extension/verify_all.sh 1` (answers, duplicates, wording, build, B&W, page fill). Every page changed below was rendered and viewed in both editions. 402 answers independently checked (403 before: three replaced items changed their number of parts).

## High
**H1 Placeholders and draft licence (p2): NOT changed.** Needs the owner (business email, registered office, lawyer-approved licence, UEN check). The bracketed placeholders and the DRAFT wording stay as they were. Blocks sale.

**H2 Unit 8 Learn it: fixed.** Learn it now has Worked example 1 (logic grid), Worked example 2 (sort 2 to 9 into "even" and "more than 6": the middle, the only-one-loop numbers and the outside), a "How to use grids and loops" box and an "Odd and even" box (also says what counting in 4s means). Q5 no longer teaches even and odd inside the question. The Latin-square row is shown in the Go further 2 hint (a different row, "3, 1, _, 4", so the puzzle is not given away). Page is tighter (`tight`, 16.2 px type, figures beside the steps) to fit on one page.

**H3 Unit 7 shape names: fixed.** "Shape names" figure in Learn it (triangle, square, pentagon, hexagon, octagon with number of sides). Q1, Q4, TH3 and Check Q1 kept. Try line no longer defines "pentagon" inside the question.

**H4 Unit 4 growing patterns: fixed.** Worked example 2: marbles, day 1 to 5, table with "+5" steps. The two examples sit side by side on the page.

## Medium
**M5 Pace.** Go further is a weekend page. Session 3 is now Think harder and Check yourself. Said on p3 (Welcome, grown-up list and the label list), p5 (new "Weekend page" column and text) and on every Go further banner. Plan doc updated.

**M6 Hints.** All 60 hints rewritten: 11 pt (was 9.5), one line, full width, at most 68 characters. Rewritten to nudge, not tell: U4 GF3 no longer lists the places, U9 GF3 no longer gives the first try, U1 TH3 no longer gives the method, U2 GF2, U4 GF2 and others shortened. The build fails if a hint wraps, and wording_lint fails over 68 characters. Hints stay upside down (D10).

**M7 Tiers.** Swapped (content exchanged, ids and checks moved with it): U3 Q4 (sampling) with TH2 (30 votes); U6 Q11 (list every way) with TH3 (two toys for $15); U8 Q6 (Venn sort) with TH3 (five friends in order). Replaced by new, harder items (new checks written): U5 TH3 (Ali gives 4 stickers to Mei, both have 10: find the starts; the old queue item repeated Q10-Q11), U9 TH3 (pencil and crayon marks on a ruler, three steps), U10 TH2 (stickers on the sides of shapes: sides, then cost). Not swapped: U8 Q7 and Q9 (Venn "wrong place", three-clue grid): after the H2 fix both are taught directly, so they are fair Start here items. U3 TH2 and the rest of the audit list are handled by the swaps above.

**M8 Writing space.** U5 GF3 has lines for Day 1 to Day 5. New `{ll}` long line (96 mm) used for every answer line that holds 3 or more numbers or names (U2 GF4, U6 GF3, U7 Q5, U8 Q3/Q5, U9 Q3, U10 Q8/TH2); the normal line grew from 46 to 56 mm. Working rows added where pages needed filling (U1 TH3, U6 Q11, U8 Q6, Q8).

**M9 Figures.** Measured icon size was 5.7 to 6.2 mm (audit said 3 mm): picture-graph scale raised by about 15 to 25 percent on U3 Learn, Q1, Q5, Q8, TH1, GF1; Check yourself graph 66 to 76 mm wide (icon 5 to 6 mm). Larger was not possible without moving items off their pages (pages are 86 to 100 percent full). Logic grids 8.6 to 9.2 mm cells in practice, 8 to 9 mm in Learn it; Venn loops 100 mm wide with 31-unit numbers and commas ("3, 7," / "9"), no more "37". Not done: the full 1.5x.

**M10 Print pipeline.** `build.py` now converts the native print PDF with `print/make_bw_print.py` (1-bit, 600 dpi, CCITT G4) and runs `print/check_bw.py`; `verify_all.sh` runs the check too. `Print_BW.pdf` is the 1-bit file for the printer; `Print_BW_vector.pdf` is its native vector source. A printer proof is still needed (owner).

**M11 Mi on the cover.** 90 mm to 52 mm tall (about 35 to 20 percent of the page height).

## Low
12. Contents and the pace plan show the unit title used in the page header (Hops and rules ...) and the topic; each unit names "follows Holiday Program Lesson N"; Welcome says what the Holiday Program is ("our school-holiday maths course") and that it need not have been joined. The owner decision about the wording "Holiday Program" itself is not touched.
13. U9 Try is now a ruler item (like the worked example); U10 Try is a growing plant in tiles (like the worked example).
14. U7 Q1 parts read "Shape A is:" (no a/an).
15. U9 Q5 now draws the pencil above the two rows, text and Why rewritten. U8 GF2 Why rewritten step by step (column 1, then row 1, then row 4).
16. "Real size when printed at 100%" under the Unit 9 Learn it ruler (soft copy) and a line in the grown-up list on Welcome.
17. No tear line, no margin dash, no tear note: the divider says to print the answer pages on their own and keep them in an envelope, or cover them. Page 78 is blank again.
18. Even and odd are defined once, by last digit; U10 Q9 Why uses it.
19. Welcome has a 3-line "For you" box with the label icons; the old five-step child box is removed. The Tips box became one line to make room.

## Not changed, and why
- High 1: owner (see above).
- No "make your own" item (rubric criteria 5 and 9): content decision, not a defect fix.
- Learn it intro text overlaps the top of the "Worked example" tab on some pages (existing layout, 1 mm); not touched because the pages have no spare height.
- Child trial and cold-read re-audit of the changed units still to do. Items now in Think harder are unchecked for difficulty by a child.
