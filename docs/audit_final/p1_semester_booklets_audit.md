# Independent audit: Primary 1 early-finisher booklets, Semester 1 and Semester 2

Auditor: independent (not the builder). Date: 23 Oct 2026. Branch `claude/great-fermi-1hv4vc`.
Subject: `school/p1/out/P1_S1_*` and `P1_S2_*` (Puzzles 20 pp, FrontMatter 5 pp, Complete_Pack 25 pp, Answer_Key 10 / 9 pp). Nothing in the pages, generators, keys or other docs was edited; only this report was added.

Method: every one of the 40 puzzle pages was rendered from the PDF (110 dpi, with 200 to 220 dpi crops where counting, clock reading or grid reading needed it) and solved by hand from the image, then compared with the answer key. This covers 100% of the pages, including the six the builder did not hand-solve (P1-24, 26, 30, 31, 32, 34) and every code-word page. Code words were checked with my own dictionaries (python `english-words` web2 + gcide, plus the 150 000 most frequent words of `wordfreq`: about 351 000 entries, a different and larger list than the builder's 129 000). The syllabus was read from pages 31 and 32 of the supplied PDF. Photocopy behaviour was tested by greyscale histogram, colour scan and 1-bit threshold renders.

## Verdicts

| Booklet | Verdict |
|---|---|
| Semester 1 | NOT ready for printing. Content and answers are correct, but fix H1 (P1-12 answer-box confusion) and H2 (outcome 2D Shapes 1.2 is claimed but not practised), then the Medium items, then re-render. |
| Semester 2 | Content ready. NOT yet printable for a school only because of the owner placeholders (H3) and a short list of Medium and Low edits. No wrong, ambiguous or unsolvable puzzle found. |

## Hand-solve results (all 40 pages)

All 40 pages solved from the rendered image: **40 agree with the key, 0 wrong, 0 unsolvable.** One page has a genuine reading ambiguity of the layout (P1-12, H1). Two pages rest on a judgement or convention (P1-30, P1-38 wording) and are listed as Medium or Low.

| Page | My answer | Key | Notes |
|---|---|---|---|
| S1-01 P1-25 | 8, 10, 16, 4 more, 7 fewer: CLOTH | same | agree. Objects about 5 mm (M1) |
| S1-02 P1-01 | tally Y3 R4 B2 G4 O2, mirror parts match | same | agree |
| S1-03 P1-24 | route (1,1) (1,2) (2,2) (2,3) (1,3) (1,4) (2,4) (3,4), 8 boxes | same | agree. Both dead ends exist (thirty-one 1st; fourth 3rd) and neither continues. Route is unique |
| S1-04 P1-12 | corners 4,4,3,7,3,3,8,... tally Y3 R4 B3 G3 O4 | same | agree only if the small square is read as the answer box (H1) |
| S1-05 P1-19 | rect 2, tri 4, circle 5, half 3, quarter 1 = 15: BUILD | same | agree |
| S1-06 P1-07 | Jenny, Aisha, Ali, Ravi, Lily: ENJOY | same | unique |
| S1-07 P1-08 | route 8 boxes, only (3,3) 8+4 is an extra dead end | same | unique |
| S1-08 P1-37 | 3, 5, 10, 3, 3, 7, loop closes | same | unique |
| S1-09 P1-10 | 9 7 4 8 5 16: COUSIN | same | agree |
| S1-10 P1-21 | 13 2 11 7 5 10: MONKEY | same | agree |
| S1-11 P1-09 | 4 9 2 / 3 5 7 / 8 1 6 | same | forced and unique |
| S1-12 P1-38 | Ali 20, Mei 8, Siti 7, Ben 5, Kumar 19: GLORY | same | unique. Clue 4 wording is terse (M5) |
| S1-13 P1-02 | 66 85 36 56 26: JUICE | same | each riddle unique |
| S1-14 P1-04 | 99, 12, 88, 63, 78: FRUIT | same | unique |
| S1-15 P1-26 | 43, 76, 70, 44, 9, 15: PEANUT | same | agree |
| S1-16 P1-33 | rect 4, sq 6, tri 1, half 2, quarter 3 = 16: TRUNK | same | agree. A square is also a rectangle, see L5 |
| S1-17 P1-34 | F, R, O, G (right half options B, C, B, C): FROG | same | each correct option verified edge by edge at 220 dpi; the wrong options each differ by one added square, one missing notch or one mirrored triangle |
| S1-18 P1-31 | 11, 2, 9, 3, 10, 6 cm: BLANK | same | strip lengths measured from pixels at 10 mm per cm: agree |
| S1-19 P1-17 | 4 5 3 2 7 8: LENGTH | same | agree |
| S1-20 P1-13 | 15 12 24 16 8 18: NUMBER | same | agree |
| S2-01 P1-03 | 6 4 3 2 8 5: SHADOW | same | agree |
| S2-02 P1-39 | 2 6 8 3 4 5: SPONGE | same | agree, relies on a small note (M4) |
| S2-03 P1-14 | tally Y2 R3 B3 G3 O2, mirror parts match | same | agree |
| S2-04 P1-05 | 8 5 9 4 10 20: SQUARE | same | agree |
| S2-05 P1-40 | F F T F T T: TEACUP | same | agree |
| S2-06 P1-11 | 21 81 94 30 17 88: FAMILY | same | agree |
| S2-07 P1-23 | 32 65 6 40 9 48: DONKEY | same | agree |
| S2-08 P1-32 | draw 3, 2, 12 cm; bars 6, 4, 8 cm: STRING | same | bar ends read from pixels at 10 mm per cm: agree |
| S2-09 P1-06 | 8:00 4:00 9:00 1:30 11:30 2:30: SECOND | same | agree (clocks read at 200 dpi) |
| S2-10 P1-15 | 80 60 40 25 95: PIANO | same | agree |
| S2-11 P1-28 | 2, 3, 7, 8, 4 ticks (purses 2, 3, 5, 6): STAMP | same | agree |
| S2-12 P1-16 | pen 12, book 15, ball 5, kite 8, cup 7, total 17: FROZEN | same | unique |
| S2-13 P1-27 | 9+13, 8+24, 16+18: MAGNET | same | each amount has exactly one pair |
| S2-14 P1-18 | 9:10, 1:55, 2:30, 11:55, 12:00: CLIMB | same | agree (hand positions checked by angle) |
| S2-15 P1-30 | route (4,2) (4,1) (3,1) (2,1) (2,2) (2,3) (2,4) (1,4), 8 boxes | same | unique. 1:30 pm recess is judged not sensible by the generator, see L3 |
| S2-16 P1-29 | 1 h, 30 min, 12:15, 2:05, 8:15, 12:10: SAILOR | same | agree |
| S2-17 P1-35 | Cat, Fish, 5, 9, 6, 26: TURKEY | same | agree |
| S2-18 P1-20 | 5 4 9 6 3, Orange, 2, total 27, 9+2 = 11 | same | unique |
| S2-19 P1-36 | 5 4 5 3 6, Kite, 2, total 23, 6+2 = 8 | same | unique |
| S2-20 P1-22 | 43/35, 16/14, 4/7, 14/13, 85/83, 12/9: GUITAR | same | agree |

## Code words (item 2)

Every code word has exactly one arrangement that is a real word, and no wrong placement spells a common word. Tests run with my own dictionaries:

- Anagrams of every code-word letter set (all 22 code-breaker pages): only `LENGHT` (S1-19), `SOLARI` (S2-16) and `UGARIT` (S2-20) appear in the large lists, all obscure or names. None is a normal word.
- Every ordered choice of letters on the logic pages (S1-06 ENJOY 720 choices, S1-12 GLORY 720, S1-14 FRUIT 720, S1-18 BLANK 720, S2-13 MAGNET 720, S2-12 FROZEN 480, S2-05 TEACUP 64, S1-17 FROG 81): no common word. Only proper names (`EOWYN` on S1-06, `PUTRI` on S1-14), which a 6-year-old will not meet.
- Every single wrong answer (one slip, any other letter on that page's code table): one hit, `SIRING` on S2-08 (STRING with T replaced by I, that is a 2 cm line drawn as 6 cm), see L1. `JAILOR` (S2-16, SAILOR with S replaced by J) appears when the pupil writes a clock time (10:15) in a "how long does it last" box, an unlikely slip, see L1.
- Two slips on the same page can reach common words: CLOCK and TOOTH (S1-01), BLIMP (S2-14), WIRING, TIRING, SIZING, SKIING (S2-08), RECORD (S2-09), STAYS (S2-11), TURRET and TUCKER (S2-17), RUBBER, MEMBER, BUMMER (S1-20), LAZILY (S2-06). The booklets only claim that single slips and rearrangements are tested, so this is information, not a defect (L1).

## Findings

### High

**H1. S1-04 (P1-12) Colour the House: answer box and small square are confusable.** Parts show shapes plus a small empty box. The box is about 5.5 mm and the drawn squares are 5.5 to 10 mm, so a pupil can read the box as a square. Some parts carry "Corners: [box]", some "Corners?" with no box, and some no label at all (roof top, top-left circle, door, base strip, mid-left and mid-right rooms, lower half of the round window). Two defensible readings give different numbers of corners (for example roof top: triangle 3, or triangle plus square 7). The tally strip detects the mistake but the pupil cannot tell which reading is wanted. Fix: the same label "Corners:" and the same large (about 10 mm), thick-bordered answer box in every part, placed away from the shapes; shapes at least 10 mm; remove the "Corners?" variant.

**H2. 2D Shapes 1.2 "forming different 2D figures" is claimed but not practised (S1-16 P1-33).** The contents table of Semester 1 and the key list 1.2 against S1-16 (and the build report says all 32 outcome lines are exercised). On the page the pupil is given a finished figure and counts the pieces; nobody forms a figure. That is 1.3. Fix either way: change the S1-16 tag to 1.1 and 1.3 and say in the coverage table that 1.2 is not covered, or add a task where the pupil forms a figure (for example "cover this outline with these 5 pieces" or "draw a figure that uses 2 squares and 1 triangle" with a check of the piece count). Also correct the build report statement.

**H3. Placeholders that stop a school print (owner items, listed so none is missed).** Every pupil page prints "(c) 2026 Preciouslyours Pte Ltd" as final while the licence page says "[entity name and year: owner to confirm]". The licence page says the school name "is set when the booklet is made", but every footer prints a blank "(school name)" line. Cover publisher line, licence wording, term, registered office are placeholders. The Answer Key has no DRAFT stamp and no contact email (cover, licence and teacher notes do). Before any school receives a copy: confirm entity and year, decide blank line versus school name (and make the licence sentence agree), add the DRAFT stamp to the key until approved.

### Medium

**M1. Counting objects are small (all counted pages).** Measured at 150 dpi: balloons 5.1 x 6.3 mm, apples 4.7 to 6.4 mm, balls 5.8 mm, stars 5.6 mm, kites 4.9 mm wide, cars and flowers smaller. Pages: S1-01 (P1-25), S1-10 (P1-21), S1-20 (P1-13), S2-01 (P1-03), S2-02 (P1-39), S2-04 (P1-05), S2-20 (P1-22). The builder note says "objects drawn large"; none is 8 mm. They are objects, not dots (good) and the counts are right, but 6 and 7 year olds will miscount at 5 mm when touching a pencil to each. Fix: at least 8 mm objects where the count is the task (S1-01 items 1 to 3, S2-01, S2-04 arrays); fewer per row is acceptable.

**M2. S1-17 (P1-34) Finish the Figure: grid cells are 6 mm.** Too small for a 6 or 7 year old with a pencil, and diagonals across a 6 mm square are hard. Use 9 to 10 mm cells (a 6 x 4 grid at 10 mm is 60 x 40 mm; put the three printed options in a row below the copy grids if width is short). The matching check itself is sound (see hand-solve) but it does not see the drawing; the owner accepted that. Keep "Cover: every puzzle checks itself" in mind: for P1-34 and P1-32 the pupil's drawing is not checked (see M7).

**M3. S2-11 (P1-28) Fewest Coins: coins in the purses are too small.** The 5 cent coins in the purses are about 6 to 8 mm and the word "cents" on them is about 1.5 mm high, not legible on a photocopy; the 5 cent and 10 cent coins are hard to tell apart. The coins on S2-10 (about 12 to 17 mm) are fine. Enlarge the purse coins or put two purses per row only.

**M4. S2-02 (P1-39) sharer rule is hidden.** "The sharer gets a share too." is a small bold line under the code table, far from the stories. Items 1 and 2 ("Ben and 2 friends share...", "Siti shares them equally with 2 friends... each child") need it; "shares with 2 friends" reads as 2 people to many adults. Move it to the instruction block at the top. This page is tagged one star but needs this idea; consider two stars (S2-03 Colour the Ice Cream, simple counting patterns, is tagged two stars; the star split is worth a second look in the pupil trial).

**M5. S1-12 (P1-38) clue 4 is elliptical.** "Kumar gives Ben 7: the same." Write "Kumar gives 7 stickers to Ben. Then they have the same number." A 6 year old, and a teacher reading it quickly, can mis-parse the colon. The puzzle itself is unique and correct.

**M6. Teacher notes contradict the page for the loop (S1-08 P1-37).** Semester 1 teacher notes say the loop check is that "the top numbers must add to the printed total". The page prints no total (strip: "Go round the loop. Do the numbers joined by = match?"). Delete that clause. Semester 1 "Problem solving" sentence also mentions "fewest coins", which is not in Semester 1; use a sentence that matches the pages of that booklet.

**M7. Self-check claim versus pages that cannot see a drawing.** Cover and notes say "Every puzzle checks itself". S2-08 (P1-32) draws a line the page cannot see; S1-17 (P1-34) copies on a grid the page cannot see. Both give a letter check that tests reading and matching, not the drawing. Say so once in the teacher notes ("on two pages the pupil's own drawing is checked by the teacher at a glance"), and change the cover line to "Almost every puzzle checks itself" or drop it. Syllabus outcomes Length 1.4 (drawing) and 2D Shapes 1.4 (copying) are only partly evidenced by a pupil's page for this reason.

**M8. S1-04 and other colour pages for pencil and photocopier use.** The pupil page for the three colour pages (S1-02, S1-04, S2-03) says only "Colour the part with that colour". The pencil-only option exists only in the teacher notes. Add one line on the page ("No crayons? Write Y, R, B, G or O in the part") and check each part has space for a letter (the small strips on S1-02 and the roof of S1-04 are tight). Also add in the teacher notes that dark crayon on a photocopy hides the number in the part: use light colours.

**M9. S2-15 (P1-30) and 12 am / 12 pm.** The unit uses "12:00 pm lunch" (noon, correct) as START and "12:00 am lunch" (midnight) as a distractor. The am and pm outcome is Time 2.2; the 12 am and 12 pm convention is a known trap for P1. If a teacher disputes it, the pupil loses nothing (both routes end the same), but safer to avoid 12:00 am and 12:00 pm altogether (use 12:30 pm only where needed, or 11:30 am).

### Low

**L1. Information on the word test.** Single slip `SIRING` (S2-08) and `JAILOR` (S2-16) spell dictionary words (see Code words). Neither slip is a plausible child error for the question asked, but the teacher notes say "no wrong answer spells a word". Soften to "no wrong arrangement, and no single wrong answer in the usual slips". Double slips can spell common words (list above).

**L2. S1-04 hexagon and diamond marks.** The small identification marks include a hexagon and a diamond (also in the check strip). They are only marks, but hexagon and rhombus are beyond Primary 1 shape names (the syllabus lists rectangle, square, triangle, circle, half circle, quarter circle). Use circle, star, triangle, cross, square, moon.

**L3. S2-15 (P1-30) "1:30 pm recess".** The generator treats it as not sensible; schools with an afternoon session could treat it as fine. It is a dead end either way, so the answer is unchanged, but change to "1:30 pm play outside" or a clearly wrong event to remove the doubt. The key's "teacher should glance at the eight events" can then go.

**L4. S1-02 (P1-01) tag.** Key tags Whole Numbers 1.1 (counting a set) and 1.2. The page asks only tens and ones (1.2). Drop 1.1. S1-12 (P1-38) amounts are numbers, not objects: 1.5 (comparing numbers) fits better than 1.4. S2-12 and S2-13 tag "dollars up to $100" for price puzzles; acceptable.

**L5. Squares and rectangles (S1-16 P1-33).** The page counts squares and rectangles separately, and a square is a rectangle. A well-taught child may answer 10 rectangles. The page total check (16) and the code word catch it, but a one-line instruction "Count squares and rectangles as different kinds here" would remove the question.

**L6. Offset strips.** S1-18, S1-19 and S2-08 start strips at 1 to 4 on the ruler (a bold arrow and tick show the start); the Primary 1 outcome is measuring in cm, and starting away from 0 is a small extension (the builder says so). All three pages also include strips from 0, so rulers do not all start at 0. Keep, but name the extension in the teacher notes. On S1-18 the 10 cm strip (K) ends at 12 and looks longest while the decoy T is 11 cm; this is a good trap but a pupil trial should confirm it is fair for 1 star.

**L7. Clock hand tips touch numerals (S2-14 clocks 2 and 4, minute hand on 5; clock 5 minute hand on 12; S2-09 clock 1 and 3).** Readable, but on a 1-bit copy the numeral is crossed by the hand. Stop the minute hand 1 mm short of the numerals.

**L8. Layout nits.** S1-08 labels "tile 3" and "tile 6" touch the circles below them. S2-12 "How to use the grid" box sits 1 mm under the price pills. S1-11 diagonal total icons are about 8 mm.

**L9. S2 Answer Key footer example.** The Semester 2 key quotes "S1-07 (P1-08)" as the footer example; use "S2-07 (P1-23)". Neither key prints page numbers; add "Key page n of N".

**L10. Coin art.** Coins are original line drawings with a small picture (boat on 50 cents, flower on 20, star on 10, leaf on 5) and true size proportions. The owner said inspired-by, not copies. The owner should compare the 50 cent boat and 20 cent flower with the real coins once before print to confirm they are not close copies.

**L11. Home-bank overlap (V9).** A 6-word shingle check against the repository home lessons found only stock phrases ("my ones digit is 6", "how many on each plate", "groups of 4, how many groups", "count each kind of shape in"). The riddles and numbers are not repeated (the home riddle is "tens digit more than 3, ones digit 6, between 30 and 50"). No action beyond a glance.

## Syllabus check (item 3)

Read against pages 31 and 32 of the PDF (updated Oct 2025).

- Every page tag in both keys uses the PDF's own wording and numbering, with these exceptions: S1-16 claims 1.2 that the page does not practise (H2); S1-02 adds 1.1 (L4); S1-12 uses 1.4 where 1.5 fits (L4).
- Nothing beyond Primary 1 was found: no pentagon or hexagon figures (hexagon and diamond only as small marks on S1-04, L2); time only to 5 minutes (all clock times multiples of 5: 8:10, 1:25, 11:25, 4:45, 7:45, 11:15, 2:35 and so on); durations only 1 h or 30 min; written methods only on S2-07 (algorithms for adding and subtracting, which the syllabus lists as 2.6) with no renaming; multiplication products within 25 (limit 40); division within 20; money cents up to 95 and dollars up to $34; numbers within 100; ordinals to 10th on S1-03 and to 5th on S1-06; no division sign, no fractions beyond half circle and quarter circle as shapes.
- Outcomes not or only partly covered by a pupil page: 2D Shapes 1.2 (forming figures: not practised, H2); Length 1.4 (drawing a line: only a letter at the end mark, M7); 2D Shapes 1.4 (copying: the pupil's copy is not seen, M2, M7); Time 2.3 (h and min): one page only (S2-16). All other 28 outcome lines are practised by at least one page.

## Layout (item 4)

Every page was viewed at full page. No clipped objects, no overflowing text, no objects drawn as bare dots (all counted things are apples, balloons, fish, stars and so on). Rulers are true scale (10.0 mm per cm measured on the render), start at the arrow and not always at 0, and the 0 mark sits inside the ruler frame. Coins carry the word "cents" and the answer boxes carry the cent sign. Picture-graph faces are drawn smiley faces in 15 mm cells (one face = one child). Findings are M1, M2, M3, L7, L8 and H1. Grid cell sizes: P1-34 cells 6 mm (M2); magic square cells 22 mm; sticker and price grids about 16 mm; graph cells 15 mm.

## Photocopy (item 5)

- All 40 puzzle pages are pure black and white: no coloured pixels (scan at 60 dpi found zero), and the grey levels are only anti-aliasing at 89, 165 and 223 with no flat grey fill. 1-bit renders at 150 dpi keep every line, including the 1 mm ruler ticks, the 6 mm grid lines and the hatching on the strips (viewed on P1-34 and P1-17). The builder's measured 1-bit ink loss is 11 to 13% for the puzzle pages (greyscale edge pixels only).
- Colour-by-code pages (S1-02, S1-04, S2-03) are usable with crayon. With pencil they work only through the teacher note (M8); dark crayon will hide the numbers in the parts.
- Front matter and key lose 29 to 34% ink at 1-bit (the builder allowed 35%); they were viewed at 1-bit and stay legible, but the key is small type. Photocopy the key at 100%.

## Front matter, key and footers (item 6)

- Footer codes (`S1-07 (P1-08)` style): all 40 pages have the same code in the top pill and the footer; the contents table, the key entry and the page agree for every page in both booklets (checked by script). The Complete Pack equals front matter plus puzzles page for page (text identical).
- Cover: title "Early Finisher Puzzles, Primary 1, Semester N, Terms ..." with DRAFT box and contact `pypteltd@gmail.com`; no price anywhere; no MOE logo or crest; no Mi. Licence page and teacher notes carry the same email and DRAFT stamps. The key has neither (H3). Star counts are 10 and 10 in both booklets and match the contents table.
- Teacher notes: see M6, M7, M8, H3. The claim "A script tried every single wrong answer and every wrong arrangement on every page. Each check rejected at least 95%" is consistent with my tests for single slips; it does not cover double slips (L1).
- Answer key tags: consistent with the pages, see Syllabus check.

### Recommendation on "Not affiliated with or endorsed by the Ministry of Education, Singapore."

Keep it, but only on the licence/copyright page (not on the cover, not on the pupil pages) and have the lawyer confirm the wording. Reasons: the owner's "no MOE claims" rule is about claims (endorsed, approved, aligned-by, logo). A disclaimer makes no claim; it removes a false impression that a school buyer could get from a booklet that cites the syllabus by page number and outcome code. The key already has to name the syllabus (its tags are the product feature), so the sentence adds almost no extra exposure. If the owner wants no mention of the Ministry in any front matter at all, the neutral replacement is "Independent publication. The Primary Mathematics Syllabus is published by the Ministry of Education, Singapore." It must also not be extended to the sales line ("MOE aligned" stays forbidden). The build already confines the sentence to the licence page, which is the right place.

## Originality (item 7)

Text of all 40 pages was compared with the 31 uploaded papers and books (SASMO, school papers, 101 Challenging Math Word Problems and the syllabus) with 6-word windows: the only hits are the syllabus shape list and counting sequences ("1 2 3 4 5 6") and the generic phrase "groups of 3, how many groups". No problem, context, name sequence or number set is copied. Puzzle types (code word, route, magic square, logic grid, picture graph) are generic forms. No copied school or contest text found.

## Not checked

No real photocopier test, no pupil trial, no check of rendering in a different PDF reader.

## Priority list for the builder

1. H1 P1-12 labels and boxes. 2. H2 tag or task for 2D Shapes 1.2. 3. M1 object sizes, M2 P1-34 cell size, M3 P1-28 coins. 4. M4, M5, M6 wording and teacher-note fixes, M7 cover claim, M8 pencil line. 5. H3 owner placeholders, DRAFT on the key. 6. Low items as time allows.
