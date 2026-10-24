# Independent audit: Level 1 Extension Workbook pilot (self-study, with answers)

Audited 23 Oct 2026, desk review by a model (no child tested). Files: `outputs/extension/L1/*Print_BW.pdf` and `*Soft_Copy_Colour.pdf` (96 pages each). No lessons or units were edited.

## Method and coverage (honest)
- All 96 pages of both PDFs rendered at 80 dpi; all 96 print pages read as text; about 50 print pages inspected visually (1-12, 13-16, 21-26, 27-48, 49-72, 77-80); the colour PDF was inspected on 4 pages (cover, unit 3, 6, 8) against 1-bit threshold renders of the print pages. Answer pages 81-96 read as text only.
- Every item (about 250 questions, 403 answers) solved independently by hand; counts and sets re-checked by brute force (65 cent 4-coin sets, 40/70/80 cent 3-coin sets, 5c/10c coin counts, 4/3-cube cuts, $38 fewest notes, 18 divisors, 4x4 Latin square uniqueness, outside-both-loops numbers). Result: **0 wrong answers, 0 ambiguous items, all "Why" lines correct** (three are clumsy: U8 GF2, U9 Q5, U7 Q7).
- Originality: 7-word check of the whole colour PDF text against `hp/qbank.json`, `lessons.js`, `workbook.js`, `scripts.js`: 35 shared 7-grams, all number runs ("3 7 11 15 19 23 27") or stock phrases ("a triangle has 3 sides and 3 corners"). No copied item. Type match to holiday Level 1 is good: units 1-10 follow holiday lessons 1-10 in order.
- Instruments: gifted rubric (12 criteria, 0-2, `docs/gifted_research.md`) and journey scores (P D F C M S, 1-5, `docs/audit/journey_p1.md`).

## Scores
Rubric /24 (criterion 7 student-led discussion is structurally 0 for a self-study book and was not counted against it; 5 multiple methods and 9 problem posing are 0 in every unit, there is no "make your own" item anywhere).

| Unit | Rubric | Verdict |
|---|---|---|
| 1 Number patterns | 15 | Ready (minor: hints) |
| 2 Number bonds | 14 | Ready (minor: hints) |
| 3 Picture graphs | 14 | Minor fixes (small icons, drawing not taught) |
| 4 Repeating and growing patterns | 14 | Minor fixes to rework (no growing-pattern worked example) |
| 5 Working backwards | 15 | Minor fixes (writing space) |
| 6 Money | 14 | Minor fixes |
| 7 2D shapes | 14 | Minor fixes (shape names not taught) |
| 8 Logic and sorting | 16 | Rework of Learn it (Venn, even/odd, Latin square untaught) |
| 9 Length | 14 | Minor fixes |
| 10 Mixed puzzles | 13 | Minor fixes |

Level mean 14.3/24 (holiday Level 1 re-audit: 15.8 after rework, 19.8 raw in the re-score). Verdict band: enrichment-flavoured. Journey (whole book, no tutor): child 6-7 reading with a parent P4 D3 F3 C4 M3 S2 (social not applicable); child 7-8 solo, holiday graduate P4 D3 F3 C3 M3 S2; strong child P5 D2 F3 C4 M3: Start here too easy, Go further good; Think harder only 3 items.

## Findings

### High
1. **Placeholders printed in the book (p2).** "Email: [business email, owner to add]. Registered office: [address, owner to add]." Licence wording is the owner/lawyer DRAFT; the UEN is unverified here. Fix: owner supplies both, lawyer approves licence text, then rebuild. Blocks sale.
2. **Unit 8 Learn it (p55) teaches only logic grids.** Venn loops (Q6, Q7, TH2), the 4x4 Latin square (GF2) and "said counting in 4s" have no worked example; even and odd are defined inside Q5 (wording guide rule 24: do not teach inside a question). A solo child cannot start Q6-Q7. Fix: second worked example (sort into two loops, and the middle), an "odd and even" box on the learn page, one worked Latin square row in the GF hint.
3. **Unit 7 shape names never taught (p48-54).** Start here Q1, Q4, TH3 and Check yourself Q1 need pentagon, hexagon, octagon; Learn it defines only "pentagon" in the Try line. Names are also beyond the P1 list (rule 25: keep in Think harder). Fix: names table (3, 4, 5, 6, 8 sides) in Learn it, or move Q1 and Q4(c) to Think harder.
4. **Unit 4 Learn it (p27) has only a repeating-pattern worked example.** The goal also promises growing patterns, yet Q11-13, TH2, TH3, GF1, GF2, Check Q3-Q4 (11 items) rely on it. Fix: add a second worked example (tower or straws with a table: day, number, "add 2").

### Medium
5. **Pace plan not realistic for session 3 (p5).** Think harder, Go further and Check yourself (pages 10-12: 6 multi-step challenge items, 4 check items, look-back) in 20-25 minutes for age 6-8. Fix: four sessions per week or make Go further a "weekend page"; say so on p3 and p5.
6. **Hints.** Upside-down 9.5 pt, wrapped to two lines read in reverse order (e.g. p10, p25). Some give the answer away: U4 GF3 lists "Stars are in places 2, 4, 6 ... Cs are in places 3, 6, 9", U9 GF3 gives the full try, U1 TH3 gives the method outright. Fix: 11 pt, one line, shorter; keep the first hint nudge-only.
7. **Tiers not honest in places.** Start here (9-14 items per unit) contains Think-harder types: U8 Q6-Q7 Venn, Q9 three-clue grid, U6 Q11 list every way, U3 Q4 sampling. Some Think harder items are no harder than Start here: U9 TH3, U5 TH3 (same as Q10-Q11), U3 TH2, U10 TH2. Fix: swap those; Think harder has only 3 items per unit.
8. **Writing space.** U5 GF3 has lines for Day 1-3 but the answer needs 5 days; U9 Q3 ordering line (about 4 cm) too short for four numbers; U8 Q8 answer lines short. Fix: add lines or a table.
9. **Figures too small for age 6-8.** Picture graph icons about 3 mm (U3 Q1, Q5, Q8), about 2 mm book icons in U3 Check yourself; logic grids cells about 5 mm (U8 p55); Venn numbers "3 7 / 9" and "2 4 / 6" run together (read as 37 and 24, p57). Fix: scale up about 1.5x; commas between numbers.
10. **Print file is not the project B&W pipeline format.** PDF is vector plus 8-bit RGB images for Mi (235 ppi, dithered), not 1-bit 600 dpi (`docs/printing/README_bw.md`). B&W legibility itself is good: no colour dependence; Venn loops become solid and dashed; coins and notes distinguished by borders; hatched tapes; cookies become black dots. Fix: run through `print/make_bw_print.py`, printer proof.
11. **Mi on the cover is about 35 percent of the page** (rule: small, few). Three uses (cover, welcome, certificate) is fine; no speech, no numbers, no calculator.

### Low
12. Header names differ from contents (Unit 1 "Hops and rules" vs "Number patterns"); the book never names which Holiday Lesson each unit follows, and "Holiday Program" is undefined for a buyer who did not attend (owner decision of 23 Oct).
13. Learn it Try lines do not match the worked example: U9 (worked: ruler; Try: cube subtraction), U10 (worked: growing plant; Try: count in 4s, trivial).
14. Grammar: U7 Q1 "Shape A is a [pentagon ...]" and "Shape C is an [pentagon ...]" (a/an wrong for options); fix "Shape A is:".
15. U9 Q5 "measure a pencil" has no pencil drawn; its Why ("a gap hides cubes") is vague. U8 GF2 Why ("Column 3 already has a 4, so row 1 ends with 3 and 4") is muddled although the puzzle is unique.
16. Rulers are drawn at true size (1 cm = 10 mm) only if printed at 100 percent; no note says so. Add "Print at actual size".
17. Answers section: "tear along the dashed line" cannot work with the divider on a double-sided sheet whose back is also answers; the margin dash prints on blank page 78. Say "keep the answer pages in an envelope".
18. Even is defined by last digit (U8) and by "shared into 2 equal groups" (U10 Why): use one.
19. Welcome page reading load (about 130 words) is for the parent; add a 3-line child version with icons.

## Checks that passed
No price; no MOE, GEP or SASMO text; no "tutor" or class dependence; wording per `WORDING_GUIDE.md` mostly met (money 50 cent style with the cent sign, "rubber", Add/Subtract, "How many more", a/b parts); contents and answer page numbers all correct; 96 pages, even count, answers from p80; tier labels neutral; answers include a Why for every item; Check yourself plus score rule plus Look back in every unit; B&W conversion loses nothing.

## Ranked top 10
1. Printed placeholders and draft licence (H1). 2. Unit 8 Learn it (H2). 3. Unit 7 names (H3). 4. Unit 4 growing-pattern example (H4). 5. Session 3 pace (M5). 6. Hints size and over-giving (M6). 7. Figure and digit size (M9). 8. Tier swaps (M7). 9. Writing space (M8). 10. Print pipeline and Mi cover size (M10, M11).

## Overall verdict for selling to parents
**Not ready yet; strong content, fix and re-audit.** Maths is correct and original, B&W works, no price. After fixes 1-6 (about one working day) it is sellable. Needs a child trial for pace and reading load, which this review cannot replace.
