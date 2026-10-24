# Level 1 Extension Workbook: fixes after the independent audit (AUDIT.md, 23 Oct 2026)

Done 23 Oct 2026. `extension/verify_all.sh 1` passed to the end (402 answers independently checked, 403 before because replaced items changed their number of parts; duplicates; wording; build; B&W on the vector and the 1-bit file; `print/check_bw.py`; page fill, no overflow). Pages viewed as images: Welcome, contents, pace plan, divider, Unit 3 (all), Unit 4 Learn it and Start here 1, Unit 5 Think harder and Go further, Unit 6 Start here 3 and Think harder, Unit 7 Learn it, Unit 8 (all), Unit 9 Learn it, Start here 1 to 3, Think harder and Go further, Unit 10 Think harder and Go further, and answer pages 91 and 93. Most were seen in the colour soft copy, the rest in the 1-bit print file. Not individually viewed: Unit 1 and 2 pages (hints only changed), Unit 4 Start here 2 and 3, Unit 5 Learn it, other Check yourself pages, the other answer pages.

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

**M10 Print pipeline.** `build.py` now converts the native print PDF with `print/make_bw_print.py` (1-bit, 600 dpi, CCITT G4) and runs `print/check_bw.py`; `verify_all.sh` runs the check too. `Print_BW.pdf` is the 1-bit file for the printer (96 pages, 12 MB; check_bw: 0 non-grey pixels); `Print_BW_vector.pdf` is its native vector source. A printer proof is still needed (owner).

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


---

# Fixes after re-audit 2 (AUDIT_2.md), 23 Oct 2026

Rebuilt (colour soft copy, native vector print, 1-bit Print_BW via print/make_bw_print.py). The books are now 98 pages (were 96): the answers are set larger and take 20 pages. `extension/verify_all.sh 1` ran to the end: ALL GATES PASSED (402 answers independently checked, duplicates, wording, build, B&W vector and 1-bit, check_bw, fill and overflow). Pages viewed as images: colour 2, 3, 4, 5, 6, 13, 20, 27, 34, 36, 37, 41, 48, 52, 55, 57, 66, 69, 71, 79, 80, 93, 98; print (1-bit) 3, 48, 55, 57, 79, 80. Not viewed: the other unit pages (only checked by the fill and overflow gates).

## Done
- **High 1 (page-2 placeholders, draft licence): NOT touched.** Still needs the owner. The only change on p2 is L2 below.
- **M1 Self-study versus grown-ups.** Answer pages no longer say "for grown-ups" (header now "check your work"; contents line likewise). Divider (p79) is written to the child: try first, check here, read the Why, ask someone to read it with you, cover the answers with a folded sheet while you work (the envelope and "print on their own" sentence is gone, as it cannot be done with a bound copy). Welcome: child box says "look at the answers at the back. Read the Why if you got one wrong"; grown-up box says it is a self-study book and that a helper may read the Why with a slow reader. Every answer now starts with a bold "Answer:" line, then "Why:", and carries the page of its question (for example "page 57"). Answer type raised from 10.8 to 11.6 pt (answer line 12 pt). Check yourself "What next" says "with a helper" instead of "with a grown-up". Not done: there is no detachable or sealed answer section; the cover-with-paper advice is the only way to hide them.
- **M2 Unit 8 Q8(b).** The question now reads "How many numbers are said in 4s but not in 3s?" and the key stays 4. The Why lists them (4, 8, 16, 20) and then checks 6 - 2 = 4. Re-verified: the item check counts the multiples of 4 up to 24 that are not multiples of 3 (4 of them), and my own brute force gives [12, 24] and [4, 8, 16, 20].
- **M3 Figure text and Unit 8 density.** `figs.render` now raises every figure font so it prints at 10 pt or more (`MIN_PT`). Measured on the PDF: no text smaller than 10 pt remains in any figure; the only text under 10 pt is the page footer (9 pt) and the "Beyond Level 1" label (9 pt), which are not figures. The "Try" badge is 10 pt (was 8.5). Unit 8 Learn it: the two worked examples are now side by side (`pair`), figures a little larger, grid and loop labels 10 pt or more. The page still holds all of: two worked examples, the two boxes, Try. Unit 7 Learn it: the "Shape names" box is wider so names and "N sides" are 10 pt. Unit 4 Learn it: the growing-pattern table is 74 mm so it is not shrunk. Picture graphs with long row names (for example Wednesday) get a wider label column.
- **Tab overlap** (pp. 6, 13, 20, 34, 41, 48, 69): fixed in `ext.css` (extra space between the intro line and the Worked example box), checked on pp. 6, 13, 20, 34, 41, 48. Not individually viewed: p69 has the same rule.
- **L17** answer wording: done under M1 above.
- **L2** soft-copy wording in the print edition: p2 says "This printed book is licensed to the buyer" in print (soft copy unchanged); p3 print has "The rulers in Unit 9 are printed at real size" in place of "Printing the soft copy? Print at 100 percent".
- **L3** hints that gave the method rewritten (U1 TH3, U4 GF3, U6 TH1, U7 TH2, U10 TH3); wording lint clean. U6 TH1 hint now covers both sets (with and without 50c).
- **L5** "Draw ..." answer rows (U5 Q10 and Q11, U9 TH1, U10 Q8) are now a dashed blank strip 16 mm tall instead of one rule. Not done: U3 Q7 drawing boxes (7.5 mm) are unchanged.
- **L6** U7 TH3(a) reads "The other is:" (no "a octagon").
- **L7** U3 Q5 Why says "stickers"; U5 Q7(b) key is "IN 13, OUT 13, OUT 19".
- **L8** Contents lists Welcome (p3) and My pace plan (p5). The print file still has no text layer (the vector file keeps it).
- **L9** U6 Learn it intro now says notes are $2, $5 and $10 and that every way is found by listing in a table.

## Not changed (needs a decision or is content work)
- High 1 (owner). L4 tier overlap (U1 TH1, U4 TH3, U10 TH3) and the missing "make your own" item (L10): content decisions. U3 Q7 drawing box size. A child trial and a printer proof are still needed.
