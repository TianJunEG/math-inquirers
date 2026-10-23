# Independent re-audit, round 2: Primary 1 early-finisher booklets, Semester 1 and Semester 2

Auditor: independent re-auditor, 23 Oct 2026, branch `claude/great-fermi-1hv4vc`. Only this report was added; nothing else was edited.
Subject: `school/p1/out/P1_S1_*` and `P1_S2_*` after the builder's round-1 fixes (commit 346b18d). `validate.py` was run: 781 checks, 0 failed (it left `school/p1` unchanged).

Method: every changed page was rendered (110 to 300 dpi, plus 150 dpi 1-bit renders) and solved by hand from the image, then compared with the key. Changed pages: S1-01, 02, 04, 10, 12, 16, 17, 20 and S2-01, 02, 03, 04, 11, 15, 20. Code words were tested with my own dictionary (web2 + gcide + wordfreq top 150 000, about 352 000 entries) for anagrams, every single slip, every double slip, and, for BUDGIE and FROG, every fill of the page's own code table or option letters. Object sizes were measured from 300 dpi pixels. Syllabus text was read from p.31 to 32 of the supplied PDF.

## Verdicts

| Booklet | Verdict |
|---|---|
| Semester 1 | NOT ready. Fix H1 (S1-04 doorknob dot contradicts the printed check) and M1 (S1-10 code table overflow), then it is ready for printing once the owner placeholders are filled. |
| Semester 2 | READY for printing once the owner placeholders (entity, year, publisher, registered office, licence wording) are filled. Fixes M2, M3 and L items are advised, not blocking. (M2 says counted apples are below 8 mm; if you hold to 8 mm as a hard rule, S2-04 and S2-01 need a re-draw first.) |

## 1. Hand-solve of every changed page (all agree with the key)

| Page | My answer | Key | Notes |
|---|---|---|---|
| S1-01 (P1-25) | 8, 10, 16, 6 more, 1 fewer: CLOTH | same | unique |
| S1-02 (P1-01) | tally Y3 R4 B2 G4 O2, all 6 mirror pairs match | same | agree; ok |
| S1-04 (P1-12) | roof 3, circle 4, ellipse 4, roof halves 4+4, windows 7+7, rooms 3, 8, 3, 7(door), 8, 8, tall 8, base 6+6+6; tally Y3 R4 B3 G3 O4 | same | answers agree, but see H1 |
| S1-10 (P1-21) | 3, 13, 14, 7, 9, 5: MONKEY | same | agree; see M1 for table |
| S1-12 (P1-38) | Ben 5, Siti 7, Mei 8, Kumar 19, Ali 20: GLORY | same | unique, clue 4 now clear |
| S1-16 (P1-33) | rect 4, square 6, triangle 2, half 1, quarter 5 = 18; small arch = rectangle + half circle (E): BUDGIE | same | agree; unique |
| S1-17 (P1-34) | F, R, O, G (checked edge by edge at 200 dpi) | same | each wrong option differs by an extra triangle, an extra horizontal, or a missing top; unique |
| S1-20 (P1-13) | 12, 16, 10, 9, 8, 15: NUMBER | same | agree |
| S2-01 (P1-03) | 7, 6, 3, 2, 4, 5: SHADOW | same | counts of objects verified (14, 12, 9, 8, 8, 10) |
| S2-02 (P1-39) | 3, 8, 4, 6, 5, 2: SPONGE | same | "The sharer gets a share too" now at the top; ok |
| S2-03 (P1-14) | tally Y2 R3 B3 G3 O2, all 5 mirror pairs match | same | agree |
| S2-04 (P1-05) | 4, 15, 12, 2, 6, 16: SQUARE | same | agree |
| S2-11 (P1-28) | 2, 3, 9, 4, 1 (only purse 2 holds 30c): STAMP | same | unique |
| S2-15 (P1-30) | (2,1) (1,1) (1,2) (1,3) (1,4) (2,4) (3,4) (4,4), 8 boxes | same | unique; no dead end reaches FINISH; no 12:00 or 12:30 left |
| S2-20 (P1-22) | 43/35, 16/14, 4/7, 14/13, 85/83, 12/9: GUITAR | same | agree; see L1 |

Code words (my dictionary): no anagram of any code word is a word (only LENGHT, UGARIT, obscure). BUDGIE has exactly one arrangement and no single slip that is a common word (only the variant BUDDIE if D is written for G; that slip also breaks the "add to 18" check). All 3^4 FROG option picks: only FROG (and the abbreviation HRSG, not a word). The pupil can also pick N or K for the small figure: BUDGIN and BUDGIK are not words. Double slips on other pages give common words (TOOTH, QUILL, MEMBER, BUMPER and so on); the notes now say two wrong answers were not all tested, which is true.

## 2. Findings

### High

**H1. S1-04 (P1-12): the door carries a black dot that looks exactly like the "same small mark" dot, but the door must be coloured differently.** The three dot-marked rooms (mid-top, lower-left, lower-right) all answer 8 (orange). The door (triangle + square = 7, green) has a black round dot at its right edge. That dot is the doorknob (a decoration in `cbc_vendor/pictures.py`, `house`, `<circle cx="69" cy="152" ...>`) and is the same size and shape as the printed dot in the check strip. The strip says "Parts with the same small mark have the same colour" and shows a dot. A pupil with the right answers sees four dot parts, three orange and one green, so the correct page fails the pupil's own check. Since round 1 the hexagon and diamond were removed, so the dot became a twin mark. Change: remove the doorknob decor, or move it clear and make it a ring, or give the twin dot set a different symbol. Re-run `validate.py`.

### Medium

**M1. S1-10 (P1-21): code table of nine boxes overflows.** Boxes for 11, 13 and 14 are too narrow: the letters C, O and N touch or cross the box edge and the next box. Still readable, but it is the one page where a letter reads as belonging to the neighbour. Remove one decoy (eight boxes, as on the other pages) or allow two rows. Tight but acceptable: S2-01 (nine boxes, letters touch the edge), S1-20, S2-04, S2-11 (letters touch the right border; L2).

**M2. Counted objects are still mostly under 8 mm; the build report's "8 to 10 mm" is the cell pitch, not the picture.** Measured glyphs: S2-04 apples 5.8 x 6.5 mm (all 28 counted apples), S1-01 apples 6.3 x 6.9, S1-20 and S2-01 apples 6.5 x 7.4 and 6.3 x 7.0, kites 5.6 wide, balloons 4.8 to 5.9 wide by 8 to 9 high, fish 8 x 4.7, S2-04 stars 7.4 x 7.0, S2-01 stars 7.9 x 7.5, S1-20 stars about 8.3. They are better than round 1 (5 mm) and the counts are small and spaced, so counting is feasible, but the claim in the report and the owner's 8 mm rule are not met for apples, balloons and fish. Either draw apples and balloons at about 8 mm wide (3 to 4 apples per row still fits), or change the report and teacher note to "about 6 to 8 mm". Not an answer risk.

**M3. S1-16 (P1-33) 1.2 is tested only as recognition.** The pupil picks which two printed pieces make an outline; the three sets are sound and the answer is unique, but no figure is formed or drawn. It is a genuine, if light, test of "forming different 2D figures" (they must know that a half circle sits on a rectangle). The build report's "all 32 outcomes covered" is true and the tag text matches the PDF word for word, so no change is needed; if you want it stronger, add "draw it" in a later edition. See section 3.

### Low

**L1. S2-20 (P1-22): the page never says which answer gets a letter.** Instruction: "Write the answer to each step. Use the code table." Only the last box of each story is in the table, except story 4 where both 14 (first box) and 13 (last box) are in it (14 also answers story 2's last box). A pupil who uses the first box of story 4 gets GUIUAR, which fails the word check, so it is caught, but add "Use the code table for the last box of each story" to be clear.

**L2. Tight code tables.** See M1.

**L3. Residual single-slip hits in my larger dictionary:** BUDDIE (S1-16), STAPP and STAMM (S2-11, names). None is a common word. The notes say "about 129 000 words"; fine.

**L4. Licence sentence versus footer.** The licence page says "The school name shown on each page is set when the booklet is made"; the footer prints a blank line "Photocopy licence: ____ (school name) only". The sentence should say "is written on each page" until a named build exists. Owner item.

**L5. Page counts.** 20 / 5 / 25 and keys 10 (S1) and 9 (S2) are as stated. 25 and 9 are odd; pupil pages are single-sided, so this only matters if the front matter or the S2 key is printed double sided (one blank back). Not a defect.

**L6. S2 teacher note on Measure and Draw.** Confirm the S2 notes say the check does not see the drawn line (the S1 notes say it for Finish the Figure; the S2 key page does).

## 3. Syllabus (p.31 to 32 of the supplied PDF)

Tag texts in the key and contents match the PDF wording exactly (for example 1.2 "forming different 2D figures with rectangle, square, triangle, half circle, quarter circle"; 1.3 "identifying the 2D shapes that make up a given figure"). S1-16 is tagged 1.1, 1.2, 1.3, S1-17 tagged 1.4. I counted the outcome lines on both contents pages: S1 covers 22, S2 covers 10 others, together all 32 with none missing, so the coverage claim holds. S1-02 no longer tagged 1.1; S1-12 tagged 1.5: both fine.

## 4. Front matter

- Contents table and footers agree for all 40 pages (code, title, stars; key order identical).
- Key pages read "KEY page n of 10" and "n of 9"; the S2 footer example is now S2-07 (P1-23).
- DRAFT stamps: cover, licence, teacher notes and both keys. Contact email pypteltd@gmail.com on cover, licence, notes, keys. No price anywhere. MOE sentence is on the licence page only (`validate.py` enforces it; I checked the text).
- Cover wording "Almost every puzzle checks itself" is true (S1-17 and S2-08 cannot see the drawing and the notes say so).
- Owner items still open: "© 2026 Preciouslyours Pte Ltd. [entity name and year: owner to confirm]" on the licence page, "[Publisher line ...]" on the cover, registered office, licence term and wording.

## 5. Loosened `validate.py` thresholds

I measured the 1-bit renders at 150 dpi. Front matter ink loss is 11 to 30 percent (limit 32), keys 21 to 35 percent. Pupil pages are 3 to 13 percent (limit 25, untouched). The loss comes from anti-aliased small black text on pure white counting as grey ink in the grey render but not in the 1-bit render; I viewed the 1-bit render of a key page and a front matter page and all text is crisp and complete. Flat grey blocks per page on keys are 12 to 95 (one page 189) and sit on dense small text. No real problem is hidden. The relaxation is acceptable. Keep the limits per page type as set, and the pupil-page limits strict (they would have caught a real fault).

## 6. Photocopy and legibility

1-bit renders of the changed pupil pages are intact (S1-04 and S2-11 viewed). Smallest text is the word "cents" on 5c and 10c purse coins (about 1.5 mm): decorative, the numeral carries the value. No clipped text found on any changed page. S1-17 grid cells are 9 mm.
