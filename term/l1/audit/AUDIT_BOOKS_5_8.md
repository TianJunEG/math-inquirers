# Audit: Level 1 Books 5-8 (Term 3 and Term 4), independent

Auditor: independent (not the builder). Date 23 Oct 2026. Branch claude/great-fermi-1hv4vc. Read-only on lessons, books and tools; only this file written.
Files audited: outputs/print/term and outputs/print/bw/term (Workbook, AnswerKey_TUTOR, HomePack for Books 5-8; 24 PDFs). Colour and B&W page counts are identical.

## Verdicts
| Book | Verdict |
|---|---|
| Book 5 (L21-25) | READY. No wrong answers. Medium/Low polish only. |
| Book 6 (L26-30) | READY, with one Medium Quest Log wording fix advised (Gate 6). |
| Book 7 (L31-35) | READY, with Medium kit/figure polish advised (L35 pair cards, L35 pattern fills). |
| Book 8 (L36-40) | READY. Low items only. |

No High items found. No wrong or ambiguous answer key entry found.

## 1. Answers (all 20 lessons)
- I read and solved every workbook question (Start here, Think harder, Go further, Investigation, exit tickets E1-E3, 100 home-practice items, Quest gates 1-8 and secret caves of both Quest Logs), well over 25 percent.
- I also checked figures against answers: clocks (hand positions), coin and note kits, calendars (1st = Wednesday in L30, ring on 6th and 3rd), route grids, cube stacks (hidden-cube counts for L34 S2, T1, G2 agree with the isometric drawing), fold and punch, picture graphs, tally marks, bar models, shadow match (L35 G1: B is the only rotation of the L).
- Brute-forced the Latin-square items: L27 G1 and G2 each have exactly one solution, matching the key (G1 empty boxes 4,1,2,1,4,3,1; G2 a,b,c = 3,4,2). L27 T1 unique. L27 I1 = 4 grids correct.
- Checked all "how many ways" items by enumeration: L24 G1/G2/I1, L25 T4/I1, L26 T1/T2/G1/I1 (6 ways), L33 routes (4, 6, 10, 3x2=6), L36 pairs, L39 T4. All match.
- Printed answer keys match the lesson data: every question answer string was found in the key PDF text for Books 5-8 (0 misses).
- No answer error. Source-data only (not printed): L23 E1 and E3 `parts[].ans` fields say 8:30 and 6:30 pm while `answer` (printed) says 7:30 and 9:30 pm. Low, fix before any tool reuses part answers.

## 2. Findings (severity, file, page)
Page numbers are the PDF page index (printed number is the same).

Medium
1. Book 7 Workbook p47 (L35 kit "pair cards"): the cards say "2 suns", "5 suns", "big", "small", "striped", "dotted" but every card shows one identical plain sun. Words and picture disagree (WORDING_GUIDE rule 5). Draw the real count, size and pattern, or drop the sun art.
2. Book 7 Workbook p42 (L35 S6) and p41, 43, 44, 45 (S1, S3, T1, G2, E1, E3): pattern fills (stripes, dots) are low-resolution bitmaps, faint and pixelated at about 10 mm tile size. In S6 the two "same" tiles A and D show different visible dot counts because the dot pattern is not anchored to each tile, so identical tiles look different. B&W (p42) is readable but rough. Anchor the pattern per tile and raise resolution.
3. Book 6 Workbook p42 (Quest Log gate 6) and key p25: text says "Triangles in a row use 3, 5 and 7 sticks", picture shows 2 triangles (5 sticks), question (a) "The next picture uses __ sticks" expects 9. A child may answer 7. Show the 4th picture's predecessor or reword ("After 7 sticks the next row uses").
4. B&W Book 5 p35-38 (L25 S2, T2, G1), Book 8 p25, p28 (L39 S1, G1, G2): bar-model numbers (about 2 mm) sit on a dithered grey fill and are hard to read in 1-bit. Use a white label box or lighter fill for B&W. Same small size in colour.
5. Contents pages of Books 2, 4, 6, 8 list lessons only; the 4-page Quest Log (Book 6 pp 41-44, Book 8 pp 39-42) and the Quest note on the cover back are not listed, although the grown-up note tells families to find the Quest Log. Add "Mi's Challenge Quest, page 41" (and 39 for Book 8).

Low
6. Book 6 and Book 2 end with two blank pages (Book 6 pp 45-46); builder already noted (owner decision). Book 4 one blank.
7. Book 8 B&W p9 (paper people kit): the blue and purple people both print solid black; red and red/green hatches are close. No lesson text depends on colour, so Low. Differentiate patterns.
8. Book 5 p3 (L21 S3): extra word row "Clock (1) Clock (2) Clock (3)" under the clocks duplicates the (1)(2)(3) labels and is misaligned with the clocks.
9. Book 5 p13 (L22 T4): "The ___ show is on" does not say a show runs until the next starts; Seals 11:25 is not used. Add "until the next show starts".
10. Book 6 p6 (L26 G1): table has 7 rows for 6 ways (one spare row, "Find every way" may suggest 7). Make it 6 rows or say "one row is spare".
11. Book 7 p36 (L34 G1 option C): four holes are drawn near the corners; for a hole at (0.7, 0.6) of the folded sheet the true unfolded positions are closer to the centre. Answer still correct; positions not exact.
12. Book 7 p21 (L32 kit) and L32 G1 key: "no piece covers more than 2 squares" is true only for the kit supplied; fine, but a child with a 3-long strip could do better. Say "with your kit rectangles".
13. Book 7 p11 and similar tiles: L32 T2 figure tiles about 12 mm with 4 mm shapes and a tiny table heading font. Known class of issue (DIAGRAM_AUDIT section 8); not re-listed beyond this note.
14. Cover (p1 of all 24 files): teal band runs to the right paper edge but has a 12 mm left margin. Home printers cannot print edge to edge, so a white strip or shrink will result. Same in Books 1-4.
15. L22/L23 use "am"/"pm"; WORDING_GUIDE rule 15 writes "a.m."/"p.m." Cosmetic, consistent across the books.
16. B&W PDFs have no text layer (pure 1-bit images, 600 dpi). Expected for print; noted for accessibility.

Known and not re-listed (see DIAGRAM_AUDIT.md): red-dot icons in L37/L38 graphs, triangle sticks not drawn in L28 T1/T2, L35 "Picture/Tile" labels missing on figures, home sheets with no diagrams, tiny coin/clock sets, no ruler drop-lines.

## 3. Layout, every 5th page and all pages
- Viewed every workbook page of Books 5-8 in colour and the 5th-page set (5, 10, 15 ... plus kit and Quest pages) in B&W, and sample key and home-pack pages. No clipped text, no overflow, no overlapping blocks found.
- Automated edge check on all 24 PDFs (4 mm band): ink only on the cover band; all inner pages clear of the trim.
- B&W: every page of all 24 files is a single 1-bit gray image (CCITT, 600 dpi), no colour. Blank pages and order identical to colour (Book 5: 10 blanks, Book 6: 11, Book 7: 13, Book 8: 8).
- Kit pages: every kit page is on an odd page with a truly blank back (confirmed in colour and B&W): Book 5 pp 9, 17, 31, 33, 41; Book 6 pp 15, 23, 31, 39; Book 7 pp 9, 11, 13, 21, 23, 31, 39, 47; Book 8 pp 9, 17, 31. Counts match the builder (5, 4, 8, 3). Coin kit count (16) and note kit (13), price tags (9+3), strips (14), people (8), tool/problem cards (7+8) all match their captions.
- Grey collisions: yellow versus white shading in L31 and L36 prints as a clear dither; tile shapes in L27 are told apart by shape. Only the paper-people pair (item 7) collides.

## 4. Rules
- Text search of all 12 colour PDFs (B&W identical content): no MOE, Ministry, SASMO, Olympiad, price, S$, quote, fee, tuition. "GEP" appears only in a tutor prohibition ("no prediction about ... GEP"). No camera hold-up instruction: only "never held up to the camera" (Quest rules) and parent photo route, which is the owner-approved private route (owner_decisions item 9).
- Parcel sentence appears word for word in the Book 6 and Book 8 home packs (Quest grown-up notes). Books 5 and 7 contain no parcel line, which is correct (the L35 line is in the separate parent summary, not in the books).
- Contact email pypteltd@gmail.com is not printed anywhere in Books 1-8 (no contact line exists). Nothing wrong; add only if a contact page is wanted.
- Mi has no calculator: cover and lesson Mi are the no-calculator image in all four books (seen on pages). "Calculator" appears only as "Not allowed" in the Quest rules.
- Home pack Book 6/8 Quest note says the content "goes past the school Primary 1 syllabus" (Book 6 home pack p13, Book 8 equivalent). Not a MOE claim by name but a curriculum claim; Low, consider "goes beyond what we practised" instead.
- Even page counts and kit blank backs: pass.
- Wording guide: no breaches that change the maths; items 1, 5 and 12 above are the guide-related ones.

## 5. Consistency of front and back matter
- Cover, "Contents" and "Kit pages (cut-outs)" box are identical in design across Books 1-8; "Term N, Lessons 1 to 5 / 6 to 10" numbering correct on all covers. Contents page numbers for all 8 workbooks match the real first page of each lesson (checked by script: all OK).
- Headers say "Term 3 - Lesson N" with N from 1 to 10 within the term; footers carry the printed page number.
- Quest Logs: Book 6 pp 41-44 and Book 8 pp 39-42, 4 pages, gate answers in each key (page 25 to 26 block) all correct (Book 6 gates: 4:35 am; 3:00 and 6:30; 95 and 3; ruler, $3, $4 and $6; triangle; 9 and 11; No and 87; Monday and 10; secret cave 2 ways. Book 8: 4, quarter, 9; 3 and 3; 6 and 2; C and shape; 7 and 15; 8 and 6; Table and 22; No and 8; 25 and 75).

## 6. Books 1-4 re-check
Page counts match the build report: Book 1 workbook/key/home pack 46/22/12, Book 2 46/30/14, Book 3 44/22/12, Book 4 48/28/14, identical in colour and B&W. All even. Contents numbers correct. Contents text wrapping fix (kit line) is in place.

## 7. Checks not done
Did not view every answer-key and home-pack page of Books 6-8 as images (text content checked by script and read); did not solve the L29 kit mistake cards against a key (cards 45+28=63, 84-6=82, 53-20=73, 17+5=21 are wrong as printed; the other four are right, which fits "some right, some wrong").
