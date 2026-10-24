# Independent audit: Level 1 term books 1-4 (lessons 1-20)

Date 23 Oct 2026, branch claude/great-fermi-1hv4vc. Audit only: nothing edited except this file, nothing pushed.
Audited from the 24 PDFs (colour and B&W, workbook / key / home pack, Books 1-4) in `outputs/print/term/` and `outputs/print/bw/term/`. Text extracted with pdftotext, every workbook page rendered and looked at (2-up at 90 dpi, zooms at 150-300 dpi on figures, 600 dpi 1-bit crops on B&W chips). Lesson JSON was opened only to locate the source of the one High.

## Verdict
Content is in good shape. **Every workbook question in Books 1-4 (Start here, Think harder, Go further, investigations, exit tickets, Quest gates and secret caves) and every home-pack item was solved by hand and matches the Key PDFs. No wrong answer found.** Page counts are even and match `term_books_spec.json` (46/44/46/46 workbooks, 22/32/22/30 keys, 12/14/12/14 home); kit pages sit on front pages with blank backs; B&W page counts equal colour.
One High (family-facing instruction wrong, Book 4 Quest page count), a handful of Mediums (one misleading figure, two layout defects, one garbled sentence, one key slip, shrunk text on 14 pages), and Lows. Not print-blocking except the High, which is a text fix in `l20.json` and a rebuild of Book 4 key and home pack.

## Highs
**H1. Book 4 Quest: parent note and tutor notes say the Quest Log has 3 pages; the printed log is 4 pages ("Page 1 of 4" ... "Page 4 of 4", workbook pp 43-46).** Book 4 home pack (Quest note: "It has 3 pages", "photo of each of the 3 pages") and Book 4 key (Quest Tutor Notes section 2.1 "L20_Quest_Log.pdf, 3 pages", section 3.1 "each of the 3 pages") are wrong. A family following it never photographs page 4 (Gate 8 and the secret cave), and the tutor notes' own timing lists four pages. Book 2's note says 4 correctly. Source: `term/l1/lessons/l20.json` lines ~866, 3764, 3772, 3823, 3833 (RETROFIT_REPORT fixed only "next_materials"). Fix: 3 to 4 in those five strings, rebuild Book 4 key, home pack (colour and B&W) and the L20 guide/parent PDFs.

## Mediums
- **M1. Book 2 L9 G2 snail figure misleads.** The "snail's way forward" is one stretched bar from 4 to 13 with the shell drawn at about 7.6 (over the 7-8 labels) and antennae at 13. Question (a) asks where the snail is after crawling back 5 (answer 8). The picture shows a shell almost at the answer and does not show a snail at 13. Redraw with the snail at 13 (or no shell on the bar).
- **M2. Book 1 L4 G3 layout.** Text is squeezed into a 40 mm column beside the 4-square block; "Yes / No" floats mid-sentence ("Are the two [Yes] [No] totals the same? Circle Yes or No."), same in (e). Reading order broken for a 7-year-old.
- **M3. Book 4 L9 Think harder instruction is garbled:** "A dozen is 12. Such cups are cups the same." (T3 then says "6 such cups"). Also stray line on L10 Think harder: "Many answers are right where it says Choose." (no item says Choose). Reword both.
- **M4. Book 4 Key, L9 Investigation "Look for": "A child who finds $3 for both packs"**; the answer given just above is $4 each. Typo in the key.
- **M5. Text shrunk to fit.** Question text is 13.1 pt on most pages but 10.6 pt (about 19% smaller) on 14 workbook pages: Book 2 pp 5, 19, 21, 35; Book 3 pp 3, 4, 22, 23, 37, 38, 39; Book 4 pp 13, 37, 39 (these are the pages that took the retrofit items or five-item layouts: L6, L8 Think harder, L10 pages; L1, L3, L5 in Book 3; L7 and L10 in Book 4). Legible, but small for ages 6-8 and uneven page to page. Consider moving one item per page.
- **M6. Figures that are tiny.** Book 1 L3 S3 (Mei's bars and squares, cells about 3 mm) and L5 S4 (bars about 3 mm; the "+" between ten-frames in L5 S1 is a dot); Book 2 L6 T3 frog lines (labels about 5 pt), L8 S1/S6 balance tiles (about 5 pt "9 red", "6 blue"); Book 3 L1 S3 and T2 (children about 3.5 mm, "FRONT" about 5 pt). Counting 10 tiny children or 8 tiny squares is possible but error-prone at 7.
- **M7. Book 2 L6 G1 number line** has no "10" and no "100" label (suppressed next to the 7 and 97 tiles). The question is about jumps of 10 and 20.
- **M8. Quest, parent-note wording:** Book 2 and Book 4 notes say the term "goes beyond the school Primary 1 syllabus on purpose ... a few gates may be new", but the tutor notes say every gate is Start here level. Soften or drop for the Quest note.
- **M9. Similarity (see section 5).** Stock frames also found in the holiday program question bank: Book 3 L1 T1 and home 4 ("Mei is 5th from the front and 5th from the back ... how many children?") and L1 home 5 ("Ali is in the middle, Ben ..."); Book 4 L6 home 4 / G1 ("Which numbers up to 20 are in both the 2s and the 5s", "numbers in both the 4s and the 5s"). Short, generic, no 7-word runs; fine for stock types, but vary if the owner wants zero overlap. Book 2 L10 T2 (queue, 6 in front and 4 behind) and the Quest secret caves remain the TERMCHECK "too close" items (deferred after 6 Nov by owner).

## Lows
- Book 3 L3 T3, G1, G3 and home 5 use "x" ("x means groups of", circle x circle = 25) two lessons before Equal Groups (L5) introduces it; stated in-page, but is above the lesson's own content.
- Book 2 L10 T5 and Book 4 L10 T1: the item says the method ("Go backwards from 20 ...", "Make a table ... Draw a strip") and scaffolds each step, so the Think harder tier is partly answered. Book 3 L5 G2 (c) "Use part (a)", Book 2 L7 T1 number line show the method. Acceptable as scaffolds; note for tier design.
- Book 4 L7 G1 (c): answer area is three dashed lines of different lengths (looks like a layout glitch).
- Book 4 Quest p3 header "Circle Yes or No where you see it" (Gate 6 has none). Quest tutor notes (Book 4) contain a developer sentence ("the page generator draws only a few figure types") and tag gates with absolute lesson numbers (L11 ... L19) beside term-local ones.
- Book 3 L4 and Book 4 L10 kit and Book 1 L1, L3, L5 / Book 2 repeat the same tens-bar kit page up to 5 times per term (paper only).
- Reading load: investigations (e.g. Book 1 L3, L7) run 45-65 words in 4-5 sentences; optional, tutor reads them. Book 1 L2 G2 and Book 3 L1 G2/T4 need two readings by design (ordinal places), acceptable.
- Quest Book 2/4 tool row is about 5.5 pt (names), see section 4.
- Timing: lessons 3, 6, 9 slow-class totals 89:50 to 89:56 (little margin); modelled only.
- Contents of Book 1 mentions the Toolbox Card; Books 2-4 do not, and no workbook lesson page points to it. Only the tool chip names it by tool. Not an error, per owner decision CARD-BOOK1.

## What was checked and found OK
- **Answers:** all workbook items, 20 exit tickets, 4 Quest logs' gates and secret caves (Book 2: 39, 67/44, 83, 12/42, 82/43, 6/20, 6 cm/10 cm, 42, 9; Book 4: 5/16, No/6, even/20, 24/6, 20/13, $4/$20, 8/No, 6/16, No/10), home packs (all 40 items). Figures that carry answers were verified against the key: L1 S1 (26), E1 (48); L3 S3 (38); L5 S1; L6 S1 (27, picture shows 7 singles); L9 rulers (S4 13/9, S6 7, T2 7, T3 12.7/9.3 so 13/9; rulers are exactly 1:1, 10.00 mm per cm); Book 3 line pictures (S1, S4-S7, T2, T3, G1 round table), bar strips (all drawn to scale), picture equations (all 14 unique solutions check, G2 unique), odd/even pairs, equal-groups pictures; Book 4 strips (S3 strip 2 is the only equal one), all cost strips, number lines.
- **Cross-lesson pointers:** the term-local "Term 2 Lesson N" pointers in the Book 4 Quest notes (1, 2, 3, 4, 5, 6, 7, 8, 9) all match the slot map. Contents pages list correct start pages.
- **Kit pages:** Book 1 9/17/19/27/29/37/45, Book 2 9/17/25/39, Book 3 9/17/25/27/35/43/45, Book 4 9/17/25/33/41: all front pages, blank backs; shape cards 15 (3 each), tokens 30 (lesson needs at most 28), ten-frames and R/Y counters (letters survive B&W), strips, tool and problem cards (7 tools, 8 problems incl. 2 blank). Quest print bar measures 99.9 mm outer.
- **Key and home pack vs workbook:** order, item numbers and tiers match in all four books; no extra or missing item.
- **DIAGRAM_FIXES.md** is not "closed": its Not-done list still names L06 T1/T2/T4 number lines and L10 story steps. In these books: Book 2 L6 T1, T2, T4 still have no line (acceptable, text items), L10 story steps still text-only. No wrong figure found among those.
- **B&W (1-bit, 600 dpi):** tool names on the L10 (Book 2 p33) and L20 (Book 4 p35) chips are legible at native 600 dpi (6 names, icons distinct; the dotted circle of Spot the pattern and the dots of List every way read). Look-back icons (about 7 mm) read. Hatched/greyed 100-square, R/Y counters, strip kit pages distinguish by label or pattern. Risk is only photocopy-of-a-print (not testable here).
- **Timing (validator, slow class):** L1 88:10, L2 88:58, L3 89:50, L4 88:15, L5 86:48, L6 89:54, L7 88:49, L8 88:28, L9 89:56, **L10 86:52 (matches report)**, L11 85:33, L12 86:27, L13 80:25, L14 84:19, L15 83:08, L16 82:46, L17 85:40, L18 84:31, L19 82:24, L20 85:44. All plausible and under 90:00.

## Per-lesson findings (book / lesson)
| Book-Lesson | Answers | Findings |
|---|---|---|
| B1 L1 | OK | tiny exit figure only (M6 minor) |
| B1 L2 | OK | none |
| B1 L3 | OK | S3 bars tiny (M6); investigation long (Low) |
| B1 L4 | OK | G3 layout (M2) |
| B1 L5 | OK | S1 "+" dot, S4 bars tiny (M6) |
| B2 L6 | OK | G1 line labels missing (M7); T3 labels tiny; Think page 10.6 pt (M5) |
| B2 L7 | OK | T5 plums OK; none else |
| B2 L8 | OK | balance tile labels tiny; pages 19/21 at 10.6 pt (M5) |
| B2 L9 | OK | G2 snail misleads (M1) |
| B2 L10 | OK | T2 queue similarity (TERMCHECK); T5 scaffold (Low); chip legible |
| B2 Quest | OK | parent note "beyond syllabus" (M8) |
| B3 L1 | OK | tiny children S3/T2 (M6); 10.6 pt pages (M5); stock frames (M9) |
| B3 L2 | OK | bars to true scale (fine) |
| B3 L3 | OK | "x" before L5 (Low); 10.6 pt pages |
| B3 L4 | OK | none |
| B3 L5 | OK | G2(c) hint (Low); 10.6 pt pages |
| B4 L6 | OK | stock frame in G1/home 4 (M9) |
| B4 L7 | OK | G1(c) answer lines (Low); Think page 10.6 pt |
| B4 L8 | OK | none |
| B4 L9 | OK | garbled "Such cups" (M3); key $3/$4 slip (M4) |
| B4 L10 | OK | stray "where it says Choose" (M3); T1 pre-printed table (Low); chip legible |
| B4 Quest | OK | **3 vs 4 pages (H1)**, "where you see it", dev sentence (Low), parent-note (M8) |

## What I could not check
- The loose Toolbox Card PDF (`outputs/kit/..._Toolbox_Card_A_6-8_PRINT_BW.pdf`) and the separate L10/L20 Quest Log and parent-note PDFs (only the copies inside the books).
- Printing: no physical print, so no real 1:1 ruler check on paper, no photocopy test, and no check of trim/cut-out behaviour on kit pages.
- Online practice (runner), slides, guide decks and tutor guides (out of scope); timing totals are the validator's modelled seconds, not a timed lesson.
- Similarity was a 6-word-run test against `hp/` text only (35 files, PDFs of holiday books as extracted text from html/json/md); the private source files used by TERMCHECK were not re-run, so closeness to private lists is not re-assessed beyond the TERMCHECK table.
- Child comprehension: wording judged against WORDING_GUIDE and reading load by eye, not with children.
