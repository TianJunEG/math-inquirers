# Cut-out and kit audit, Level 1 Terms 1 and 2 (Lessons 1 to 20)

Final check made at commit **205a431** on branch `claude/great-fermi-1hv4vc`. HEAD moved during the audit (78dbcab at start; 872a2e4 added the combined term books; c88a46f fixed L18, b8681ff fixed the L17 hand-off, 1034483 fixed L16). I re-read the kit text of L16, L17 and L18 at 205a431: they are the final versions and F13 is resolved. L11-L15, L19 and L20 JSON were unchanged from the start of the audit to the end. The `outputs/print/term/` books were built at 872a2e4 and are not rebuilt after the L16-L18 fixes (re-run `print/make_term_books.py`).

Scope: `workbook.kits` for every lesson, the rendered kit pages (page 6, and page 7 for L2, L3, L15, viewed as images), the lesson scripts, workbook questions, tutor guide, parent summary and home sheet text about materials, `parent.next_materials` (the hand-off), and `print/make_term_books.py` with the books it produces. No lesson, tool or out file was edited.

Ratings: **Ready** = a family can use it as printed. **Minor fixes** = usable, small text or layout changes. **Rework** = a child or grown-up will hit a wall in the lesson as written.

---

## 1. Summary table

"Needed" is what the script and workbook questions actually use. "Supplied" is what the kit page prints.

| L | Kit page(s) | Needed | Supplied | Verdict |
|---|---|---|---|---|
| 1 | tens bars + ones squares | up to 7 bars, up to 14 squares (build 58, 70; open a bundle: 4 tens 12 ones) | 9 bars, 20 squares | Minor fixes (F8, F9, F10, F11) |
| 2 | ones cards 0-10; tens cards 0-100 (2 pages) | 11 + 11 cards | 11 + 11 | Minor fixes (F14 row is 63 cm) |
| 3 | bars + squares (again); digit cards 2 x 0-9 | 20 digit cards; bars/squares for 2-digit builds | 20 cards; 9 bars, 20 squares | Minor fixes (F8, F15) |
| 4 | numbered 100 square, no cutting | 1 square, about 12 counters | 1 | Ready (F5, F20) |
| 5 | bars + squares (again) | up to 5 bars, 14 squares | 9 / 20 | Minor fixes (F8) |
| 6 | bars + squares (again) | up to 9 bars (guide: no more than 9 bars and 20 squares) | 9 / 20 | Minor fixes (F8) |
| 7 | bars + squares (again) | bars to 8, squares to 19 (57 take 28) | 9 / 20 | Minor fixes (F8) |
| 8 | bars + squares (again), optional | S5, S7 tens only | 9 / 20 | Minor fixes (F8, F9) |
| 9 | none | ruler, 10 clips | n/a | Minor fixes (F7, F12) |
| 10 | bars + squares (again) | only the squares, as counters (about 20) | 9 bars unused, 20 squares | Minor fixes (F8, F9) |
| 11 | place cards 1st-10th, number cards 1-10 | 10 + 10; G2 uses a line of 13 | 10 + 10 | Minor fixes (F16) |
| 12 | 8 strips of 10 cells (4 yellow, 4 blue) | up to 9 strips of cells in one question (S3 85, T3 86, G2 90 cells), 45-52 cells of one colour, a 6-cell piece | 80 cells, 40 per colour, no 6-cell piece | **Rework** (F1) |
| 13 | 4 ten-frames + 20 counters (10 red, 10 yellow) | up to 10 red + 10 yellow | 10 + 10 | Minor fixes (F17) |
| 14 | number cards 1-20 | 20 cards + about 20 counters | 20 cards, no counters | Minor fixes (F6, F18) |
| 15 | groups mat (6 plates); array mat 5 x 8, no cutting | 4 plates, arrays up to 2 x 6 | 6 plates, 40 squares | Ready (F5, F19) |
| 16 | 100 square, no cutting | 1 | 1 | Ready (F5, F20) |
| 17 | groups mat (6 plates), no cutting | 4 to 5 plates | 6 | Ready (F5) |
| 18 | 10 strips of 10 cells | 3 strips, 3 pre-cut at 6 cells, other models up to 26 cells | 100 cells | Ready (F13 fixed in c88a46f) |
| 19 | 4 ten-frames + 20 counters; shape cards are NOT on the page | up to 16 counters; **5 shapes** (circle, square, triangle, heart, star), up to 3 copies of one shape | 20 counters; grown-up draws 4 shape cards, no star | **Rework** (F2) |
| 20 | 20 round $1 tokens | up to 28 (T1 $28, T2 $24, G2 $20) | 20 | Minor fixes (F3) |

Counts: **2 Rework** (L12, L19), **13 Minor fixes**, **4 Ready** (L4, L15, L16, L17), and L18 (Ready after c88a46f). 19 of 20 lessons have a kit; L9 has none.

---

## 2. Findings

### High

**F1. L12: the strips cannot make the lengths the lesson uses.**
Location: `l12.json` workbook.kits (`unit_strips`, rows 8, cells 10); S3, S6, T3, G2; script warm-up 3 (s-rem3).
Evidence: the page prints 8 strips = 80 cells, alternating yellow (4 strips, 40 cells) and light blue (4 strips, 40 cells). The lesson models two people as two bars: S3 Siti 34 + Dev 51 = 85 cells, T3 Ravi 52 + Wei 34 = 86, G2 Ali 20 + Ben 30 + Mei 40 = 90 ten-cell strips. All exceed 80. S6 Wei 45 and S3 Dev 51, T3 Ravi 52 and G1 52 each exceed the 40 cells of one colour, so "one colour per person" fails. The warm-up says "three strips of 10 and one strip of 6": a 6-cell piece does not exist, and the guide and safeguarding line say children do not use scissors. The kit intro says "Cut a strip to any length at a dotted line", which tells a grown-up to cut but not when or to what length.
Fix: print 12 strips (6 + 6, or add a second kit page) so 90 cells exist; say strips of ten are for building and big numbers are drawn; add "cut two strips after 6 cells and two after 4 cells before the lesson" to the parent hand-off (L11 `next_materials`) and the kit intro, as the L18 edit now does; state in the workbook hints which questions are draw-only.

**F2. L19: the shape cards are not in the kit, the list omits the star, and one of each is not enough.**
Location: `l19.json` materials.child ("4 small pieces of paper ... circle, square, triangle, heart"), S4, T2, G1, G2, script explore.
Evidence: the star appears in S4, T2, G1, G2 and about 31 times in the script, but only four cards are listed. The script says "12 counters on two heart cards" and "three circle cards", "share 15 between three stars": up to three copies of the same shape. A grown-up must draw about 9 cards by hand before a lesson, from instructions that list only four. The kit page instead spends half a sheet on four ten-frames that the script barely uses (one guide line, "children may lay counters on a ten-frame").
Fix: replace the four ten-frames with a cut-out sheet of shape cards (circle, square, triangle, heart, star, three of each, large enough to hold 6 counters), keep the 20 counters, and update the materials and L18 hand-off to say "cut out the shape cards".

**F3 (High for the PDF route, solved in the books). Duplex printing makes the kit page the back of page 5.**
Location: all per-lesson workbook PDFs; `tutor_prep` in every lesson ("print workbook pages 1 to 6"); parent pages.
Evidence: every Workbook PDF has 6 pages (7 for L2, L3, L15), A4. No lesson text says "print single-sided". Printed double-sided, page 6 (the kit) is the reverse of page 5, which holds the Investigation, the **Exit ticket** and the look-back (checked on L1 p5). Cutting the kit page then destroys the exit ticket, or the exit ticket is lost before the lesson. The only single-sided request in the repo is in other levels' email text (`hp/mk_pack.py`, `levels/mkextras.py`). Ink show-through is also likely on 80 gsm paper.
The books (`print/make_term_books.py`) fix this properly: every kit page sits on a front page with a blank back, a tear line and a 12 mm mirrored gutter (checked: Book 1 page 9 is the L1 kit, page 10 blank).
Fix: add "print the kit page on its own sheet, or one side only" to the tutor_prep line, the parent materials and the kit-page intro; or export a one-sided kit-only PDF per lesson. In the books: make the lesson text match (F4).

**F4. L9 in the books: the real-size ruler pictures are printed at 94.3%.**
Location: `print/make_term_books.py` (`content_scale` 0.9429 in `term_books_spec.json`); `l09.json` S4, S6, T2, T3, G2 and notes ("the ruler picture is printed at real size ... print at 100%").
Evidence: the book scales every page by (W - 12 mm gutter) / W = 0.9429. A 10 cm ruler picture becomes 9.43 cm, so a child laying their own ruler beside it sees the marks drift apart (8 cm lands at 7.5 cm). The lesson tells the family to print at 100% and "check by laying your own ruler next to the picture". The same shrink applies to kit pieces (bars, cards, tokens are 6% smaller than the sizes in F9 and F14), and to the L10 check if it were bound.
Fix: either do not shrink pages with real-size content (L9 pages 2-4, L10 check) and instead shift them, or remove the "real size" claims and the lay-your-ruler instruction for books and use a printed ruler with a scale note.

### Medium

**F5. Book kit pages that must NOT be cut carry "TEAR OUT here ... then cut out the pieces".**
Location: `gutter_mark()` in `make_term_books.py`; applied to every page whose header says "Kit": L4 (book p37), L15 (two pages), L16, L17.
Evidence: the L4 kit page (seen at p37) says "No cutting is needed" and the lesson says "kept flat", but the margin note says to cut out the pieces. Tearing out the 100 square is harmless; the wording is wrong and the contents page also says "then cut out the pieces".
Fix: give non-cut kit pages a different margin note ("Tear out if you like. Do not cut."), or suppress the stamp for `hundred`, `groups_mat`, `array_mat`.

**F6. Families are never told to tear the page out first, and lessons say "printed workbook".**
Location: tutor_prep, materials.child, parent `next_materials` in all kit lessons.
Evidence: all text still says "print workbook pages 1 to 6, cut out the kit page". Owner decisions (de9a383, cc37b47) say printed workbooks are given on payment, so most families hold a spiral book. The book's contents page explains tearing, but the lesson-level instructions do not.
Fix: one agreed sentence in `common.py` for kit lessons: "Tear out the kit page along the dashed line (the back is blank), then a grown-up cuts out the pieces."

**F7. L9: the only lesson with no kit depends on a ruler the family may not have.**
Location: `l09.json` materials ("No ruler? Tell your tutor before the lesson"), notes.
Evidence: a printed ruler is avoided on purpose, but families without a ruler get no working option. The check in L10 also needs a ruler and is printed at 100%.
Fix: provide a one-sided cut-out strip with a 15 cm centimetre scale on the L8 kit page or in the L8 `next_materials`, with a note to check it against 100% (see F4), or add a household fallback (a ruler drawn on squared paper, graph-paper 1 cm squares).

**F8. Seven identical tens-bar pages (L1, L3, L5, L6, L7, L8, L10); only some say to reuse.**
Location: workbook.kits (type `base_ten`) in those lessons; `parent.next_materials`.
Evidence: 9 bars + 20 squares are printed seven times (Book 1: pages 9, 27, 45; Book 2: pages 9, 17, 25, 39). Only L6 and L8 say "the kit from Lesson 1"; L5's hand-off says "earlier pieces can be reused"; L2->L3, L4->L5, L9->L10 say "cut out" with no reuse hint. L7 hand-off omits the kit completely. A family following the text cuts 7 x 29 = 203 pieces. The cut pieces carry no lesson label, so spare sets mix.
Fix: print it once (L1) and say "keep it all term" in L1, L3 to L10; in later lessons keep the page for spares only; change wording to "your bars and squares from Lesson 1".

**F9. Bar cells and one-squares are different sizes.**
Location: `svg.py` `kit_page_svg` (bar cell 62 x 54 units, square 56 x 56).
Evidence: on the rendered page a bar cell is about 15.1 x 13.2 mm, a square about 14.0 x 14.0 mm. Ten squares in a row (140 mm) do not match one bar (151 mm), which undercuts the lesson idea "a bar is ten squares".
Fix: draw all cells as the same square (for example 14 x 14 mm).

**F10. Cut lines too close; many fiddly cuts.**
Location: base_ten page; `cards`, `ten_frame` kits.
Evidence: adjacent bars have dashed cut lines about 2 mm apart (at 150 dpi: two dashed lines 8 px apart), so a grown-up cuts a sliver or one bar's border. The 20 ones squares have 2.4 mm channels. L13/L19 counters are 12 mm discs with dashed circles about 2 mm apart, 20 per page, round. L20 tokens are 34 mm discs about 2.5 mm apart. Cutting 20 circles by hand takes minutes and the discs are very small for the child to pick up.
Fix: leave at least 6 mm between cut lines; make counters 18-20 mm squares with rounded corners, or print them as a tear-off strip of ten; consider a single shared "counters" page.

**F11. Pieces are not stored or labelled (storage advice patchy).**
Location: kit intros and parent pages.
Evidence: "keep them in an envelope" appears in L1, L2, L3, L5, L6, L7, L8, L14 (and L19 hand-off). It is missing from L4 (not needed), L10, L11, L12, L13, L18, L20. No lesson says "write your name on the envelope" or "keep the pieces for later lessons". L11 cards (28 x 19 mm), L13/L19 counters and L14 cards are small and easy to lose.
Fix: one line in every cut-out kit intro: "Keep the pieces in an envelope with your name; we use them again."

**F12. L9 (and the term) tutor text points at a page 6 that does not exist.**
Location: `l09.json` materials.child ("page 6 is not used"), tutor_prep.
Evidence: the L9 workbook has 5 pages (`pdfinfo`); a family told "page 6 is not used" may search for a missing page.
Fix: delete the clause.

**F13. L18: the parent-facing text did not say which strips to cut after 6 cells (FIXED in c88a46f and b8681ff).**
Location: `l18.json` kit pages and materials; tutor_prep.
Evidence (version audited first): tutor_prep says "cut three of them after 6 cells" but the kit intro and child materials said only "cut ... at a dotted line" and the Explore round needs the 6-cell pieces. The fix now says "cut the page into ten strips (cut between the strips, not between the cells) and cut three of them after 6 cells. Nobody cuts during the lesson", which resolves it. L17's hand-off now carries the same sentence. L12 still needs it (F1).
Fix: repeat the sentence for L12 (and L11's hand-off).

**F14. L2: tens cards in one row are about 63 cm.**
Location: `l2` kit page 2 (wide cards 57 x 40 mm); script "put the 11 tens cards in a row".
Evidence: 11 x 57 mm = 63 cm plus gaps, wider than a typical school desk or a laptop shelf. The ones row (43 mm cards) is 47 cm.
Fix: make tens cards 40 x 40 mm so the row is 44 cm, or tell the child to use two rows.

**F15. L3 digit cards: 6 and 9 are not marked.**
Location: L3 kit page 2 (also L2, L11, L14 number cards).
Evidence: a child can turn a 6 into a 9. Cards have no dot or underline. The two sets are identical, so cards 4-4, 7-7 work, which is good.
Fix: underline 6 and 9 (small bar under the digit), and in L14 under 6, 9, 16, 19.

**F16. L11 cards are small and one card short for G2.**
Location: `l11.json` kit (cards 28 x 19 mm); G2 "a line has 13 children"; script places cards under toys, cups or shoes.
Evidence: 28 x 19 mm place cards under real objects (cups, shoes) are tiny, and the line of 13 in G2 needs 11th to 13th. The same 1-10 numerals are now printed on three kits (L2, L11, L14). The L10 -> L11 hand-off also omits them (F21).
Fix: 40 x 28 mm cards and 12 or 13 cards, or say G2 is drawn only.

**F17. L13: tiny red and yellow counters, colour carries the meaning.**
Location: L13, L19 `ten_frame` kit.
Evidence: 12 mm discs (11 mm in the book) whose only difference is red versus yellow; the script names them by colour. In grey-scale the pair is about 117 vs 201 (distinguishable but pale), and red/yellow is not ideal for children with colour-vision difference. Go further uses "double 35" and a five-number sum, which 20 counters cannot show.
Fix: print R and Y letters or a ring/dot on the red counters; larger counters.

**F18. L14: counters are needed but not supplied, and the hand-off names the wrong lesson.**
Location: `l14.json` materials ("or the counters from the Lesson 3 kit page"), script (20 counters to pair).
Evidence: "Lesson 3" means Term 2 Lesson 3 (L13), but to a family "Lesson 3" is the Term 1 digit-card lesson. The 20 cards need no counters; pairing needs about 20 counters.
Fix: say "the red and yellow counters from the Doubles lesson (Lesson 13)" and add "keep them".

### Low

**F19. L15 mats: plates are labelled in very pale grey-blue.** The plate numbers 1-6 and inner rings are about #B7C4D9 and vanish in black-and-white. T4 asks for 12 groups of 1 (needs 12 plates; the mat has 6) and the array mat is 8 wide (12 in one row does not fit). L15 G3 24 sweets exceed the 20-counter list. Fix: say these are drawn.

**F20. L4 and L16 100 squares are the same page; "100" is set in a smaller font.** Both pages show the 100 at about 70% the size of the other numbers (seen on both). Families are not told to keep the L4 square for L16, and a coloured L4 square cannot be reused. No alternative if there is no printer (draw a 10 x 10 grid; use a calendar or a hundred-chart book).

**F21. Hand-off gaps, kit not mentioned.** See section 4.

**F22. Page footer is 5 mm from the bottom edge.** The footer text sits about 15 pt (5.3 mm) above the page edge, which some home printers clip (many need 6.35 mm). Content margins are about 14 mm left and right, fine for printing, but the unbound single-lesson PDF has no gutter for punching (hole punch removes 12-15 mm).

**F23. Two page numbers on a book kit page.** The page footer says "Page 6" and the book adds "- 9 -". The lesson text refers to "page 6", which matches the footer only.

**F24. L10 kit intro lacks "a grown-up".** It reads "Cut these out first. The squares make good counters." Every other kit page says "A grown-up cuts these out". Only the squares (about 20) are used; the nine bars are cut for nothing.

**F25. L3 kit page 1 (bars) is a duplicate of L1.** Covered by F8; the 7-page L3 workbook is an unnecessary extra sheet.

**F26. Paper weight.** No text says anything about paper weight; the quote file asks for 100-120 gsm. Cards and counters cut from 80 gsm paper curl and blow off the table. Suggest: "stick the kit page to thin card, or use thicker paper if you can" and say that thin paper is fine for one lesson.

---

## 3. Shared-template findings (apply to every kit page)

| # | Finding | Evidence | Suggested fix |
|---|---|---|---|
| T1 | Kit page is always the **last** page(s) of the workbook | p6 (p7); in the book also at the end of each lesson | Tell the family where it is in the lesson text; for non-cut pages (L4, L15, L16, L17) the child flips to the back during the lesson: consider printing the 100 square on the page itself or as a fold-out |
| T2 | Kit page keeps the header, Name/Date band and footer | The cut-out zone starts about 90 mm down the sheet; pieces occupy 50 to 90% of the page. L11, L13, L14, L19, L20 leave 40 to 60% blank | Use the blank area for the pieces' spares or a "keep for later" box; remove the Name/Date band on pages that are cut up |
| T3 | Cut-line style | Dashed grey #777, about 1.6 px; strips use dotted verticals over solid cell lines | Fine in colour and black-and-white; make verticals on strips scissor marks outside the strip only |
| T4 | Kit pages use the lesson background grid | Faint blue grid on every page; uses ink, no effect on black-and-white | Optional: drop the grid on kit pages to save ink |
| T5 | Colour reliance | Bars light blue (L 232) and squares pale yellow (L 240) differ by shape and border only; strips yellow (L 201) vs blue (L 232) are weak in grey; counters red (L 117) vs yellow (L 201) | Add shape/letter coding (R/Y; two-pattern strips) |
| T6 | No Mi artwork, ordinal/number labels are correct | Checked: 0-10, 0-100, 0-9 twice, 1st-10th, 1-10, 1-20 correct; no number errors found on any kit page | None |
| T7 | Safety line is in the guide, not the parent page | `scissors` appears in the guide for L2, L3, L7, L12, L18 only; no parent page, home sheet or workbook says "children do not use scissors" or "keep the cut pieces from younger children" for the kit (try-at-home lines say it for small things in general) | Add to the kit intro and to the parent `next_materials` box: "A grown-up cuts. Keep pieces from little brothers and sisters." |
| T8 | Grown-up cutting load | 20 to 29 pieces per page; 7 base-ten pages = 203 pieces; strips and circles are the slow ones | Reduce with F8, F10 |
| T9 | Book binding | Books use a 12 mm mirrored gutter and kit pages on fronts with blank backs (good); all pages are scaled to 94.3% | See F3, F4; keep the tear line (and perforation) away from content |
| T10 | Alternative for families without a printer | Present for L1, L2, L3, L7, L9 (ask the tutor), L12, L13, L18, L19, L20; partial for L5 (ten-frame only); **absent for L4, L6, L8, L10, L11, L14, L16** | Add one line each: write 1-20 on scraps (L11, L14); draw a 10 x 10 grid or use a calendar (L4, L16); real plates (L15, L17, already the main option) |

---

## 4. Hand-off truth: does the previous lesson's `next_materials` say "cut / prepare"?

| Previous -> next | Says cut / prepare the kit? | Note |
|---|---|---|
| L1 -> L2 | Yes ("cards cut out from the two kit pages") | OK |
| L2 -> L3 | Yes (digit cards, bars and squares, cut out) | Repeats L1 bars (F8) |
| L3 -> L4 | Yes (100 square, no cutting) | OK |
| L4 -> L5 | Yes (kit page cut out) | No reuse hint |
| L5 -> L6 | Yes ("earlier pieces can be reused") | Best wording |
| L6 -> L7 | Yes (envelope) | OK |
| L7 -> L8 | **No** | L8's kit page is not mentioned |
| L8 -> L9 | n/a | Ruler: yes |
| L9 -> L10 | **No** | L10 "cut these out first" is not in the hand-off (counters mentioned) |
| L10 -> L11 | **No, High** | Hand-off is "about 10 counters" and the Term 2 start date. No place/number cards, no coin, no FRONT paper, across a term break. Add them |
| L11 -> L12 | Yes ("strips page already cut out") | Does not say which lengths (F1) |
| L12 -> L13 | Yes (counters cut out) | OK |
| L13 -> L14 | Yes (cards cut out) | OK |
| L14 -> L15 | Prints only (nothing to cut) | OK; L15 itself says print the kit pages |
| L15 -> L16 | Yes (print, 100 square) | OK |
| L16 -> L17 | Yes, fixed in 1034483 ("it has a groups mat") | OK |
| L17 -> L18 | Yes, fixed in b8681ff (ten strips, three cut after 6 cells) | OK |
| L18 -> L19 | Yes (counters; shape cards drawn) | Star missing (F2) |
| L19 -> L20 | Yes (tokens cut out) | OK |

L10 -> L11 is the one a family will actually miss: the child arrives to a lesson built on cards that nobody asked to be cut.

---

## 5. Reuse across lessons

| Item | Where | Reuse advice given? | Recommendation |
|---|---|---|---|
| Tens bars + ones squares | L1, L3, L5, L6, L7, L8, L10 (7 pages) | Only L5, L6, L8 | Print once; "keep all term" (F8) |
| Number cards 0-10 / 1-10 / 1-20 / digits | L2, L3, L11, L14 | None | Say L11 1-10 can come from L2's ones cards; L14 1-20 reuses L11 plus 11-20 |
| Red/yellow counters + ten-frames | L13, L19 | L14 mentions "Lesson 3" counters (wrong) | L19: "use your L13 counters"; one print |
| Strips | L12 (8), L18 (10) | None | L18 says "use L12 strips plus 2 more" or print 12 on both |
| 100 square | L4, L16 | None | Keep L4 blank copy; colour L16 only |
| Groups mat | L15, L17 | None | Identical page; reuse |
| $1 tokens | L20 only | n/a | Could reuse L13/L19 counters |

---

## 6. Lessons with no kit

Only **L9** (Draw and Measure) has no kit. A cut-out centimetre strip would help (F7) but printing at 100% is fragile (F4). L10 has a kit page but uses only its squares. No other lesson lacks a kit. Lessons where a kit would help but none exists: L2 (number-word cards for the "number words" half of the lesson: the lesson is oral only), and a "shape cards" page for L19 (F2).

---

## 7. Alternatives for families who cannot print

Documented in the lesson text for L1 (bundles), L2 (11 paper squares), L3 (20 scraps), L7 (copy the sums), L9 (tell the tutor about the ruler), L12 and L18 (draw boxes), L13 (two kinds of small things), L19 (cups, paper), L20 (counters, beans or buttons). **Not documented**: L4 and L16 (100 square), L5 (bars), L6, L8, L10, L11 (place cards), L14 (cards); the mats in L15 and L17 are replaceable by plates and are fine. Easy household substitutes to add: a calendar or a hundred chart; two rows of five boxes drawn on paper for a ten-frame; torn paper squares for cards.

---

## 8. What I did not check

I did not open the answer-key books beyond page counts, the home packs, or the L10/L20 check files (not kit pages). Pages were viewed as images at 60-150 dpi; no physical print was made, so cut widths are measured from the PDF, not paper.
