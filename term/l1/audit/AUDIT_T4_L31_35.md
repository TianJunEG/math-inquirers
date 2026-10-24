# Independent audit: Level 1 Term 4, Lessons 31 to 35 (Term 4 Lessons 1 to 5)

Auditor: independent (did not write these). Report only: no lesson, tool or output file was changed.
Method: followed `AUDIT_T3_BRIEF.txt`, `AUDIT_T2_BRIEF.txt` (they are `.txt` files) and `AUDIT_BRIEF.txt` / `AUDIT2_BRIEF.txt`. Read `docs/terms/owner_decisions.md`, `WORDING_GUIDE.md`, preflight sections 1, 4, 5, 8. Every workbook item was solved by me from the built PDFs (zoomed renders at 200 to 300 dpi where pictures were small) and then compared with the answer key; the lesson JSON was used only to cross-check counts and hand-offs. All slides were rendered (pdftoppm) and looked at; each online practice was run in Chromium (Playwright, phone width 390 px, local server): every item type was answered right and wrong, pictures checked, external requests counted (none, no page errors). B&W was simulated on L35 patterns only (Book 7 is not built into `outputs/print/term`, see X1).

Severity: High = wrong, unanswerable or unusable; Medium = ambiguous, misleading, impractical, inconsistent; Low = polish.

## Verdicts

| Lesson | Title | Verdict | High | Medium | Low |
|---|---|---|---|---|---|
| 31 | Half and Quarter | yes after listed fixes | 1 | 3 | 5 |
| 32 | Build the Figure | yes after listed fixes | 0 | 4 | 5 |
| 33 | Copy on the Grid | yes after listed fixes | 0 | 4 | 4 |
| 34 | Cubes and Views | yes after listed fixes | 0 | 6 | 4 |
| 35 | Spot It | yes after listed fixes (fix the High first; local, small) | 1 | 3 | 5 |

Maths: every printed workbook answer, key line, tutor-guide answer, home answer and practice answer I solved is correct (list at the end). No wrong key found. The problems are usability, picture scale, ambiguity, reuse of class numbers and one broken online item.

What passes everywhere: 90-minute model (scripted time 63:48 to 68:04 quick, about 78 slow, standing 5-minute buffer); beyond-syllabus item named and labelled (Same Half, Different Shape; Every Triangle; Count the Routes; Fold Twice, Punch Once; Shadow Match) at Think harder or Go further only, tutor guide and parent page say "past the school Primary 1 syllabus on purpose"; no MOE-aligned, GEP, SASMO, price, "Challenge" or "stretch" wording on child or parent pages; recording notice is said BEFORE the recording starts (L31 0:50 notice, 1:07 start; L32 0:34/0:51; L33 and L34 0:34/0:51; L35 0:32/0:50) and children's first names are avoided afterwards; no "hold paper to the camera" instruction (every guide says nobody holds anything up); photo route is the business WhatsApp only, kept 90 days (matches `website/privacy.html`); Mi is the no-calculator pose (holding a book) on every slide; no end-of-term check; no `$20`; "Term 4 • Lesson N" on workbook, home, parent and slides; hand-offs 30 to 31, 31 to 32, 32 to 33, 33 to 34, 34 to 35, 35 to 36 are true against the next lesson's materials and kit (checked counts: L31 kit 10 pieces; L32 20 pieces on two pages; L33 grid page not cut; L34 4 squares; L35 12 cards; L36 8 people / Book 8). Online practice for all five has no network calls, pictures render, ordered and multi-answer marking is not used in these five (number, choice, fields and selfcheck only); wrong answers get a neutral retry, then the worked steps.

---

## Lesson 31 Half and Quarter

Maths solved from the PDF: S1 A yes, B no, C yes; S2 4, quarter; S4 2, 4; S5 shape 2, shape 3; T2 4, 2; T3 T F T F; G1 4, 4, 4, No; G2 half circle, triangle; G3 12, 6; E1 quarter; E2 2; E3 No. Key matches.

### High
1. **Kit shapes are about one third of the stated size.** `out/l31/L31_Kit_Pages.pdf` p1 and Workbook p6: circles and squares measure about 28 mm across (111 px at 100 dpi on A4); the lesson JSON, preflight section 1 and the guide say about 9 cm (`tools/figs3.py fold_shapes d_mm=95` is not honoured; the figure is scaled down). Explore folds a circle twice and lays two quarters on a half: a 28 mm circle gives 14 mm quarters, too small for a 6-year-old to fold edge to edge. The 2 long rectangles are 35 x 20 mm strips with 3 faint lines (preflight asked for a 4 x 2 grid rectangle). About 40 percent of the page is empty, so there is room. Fix: render at 90 mm (two per row, two kit pages, or cut count per page lowered).

### Medium
2. Workbook p5 Investigation: "First: Fold a paper square in half. Open it. How many parts? Write the number." has no answer box (two empty squares and four lines). The key says "2 parts". Add a box.
3. Workbook p6 kit: the three "faint lines" on the long rectangles are light blue and will vanish in B&W printing; cut-line gaps between the cells are 3 to 8 mm (rule 6 mm).
4. Deck slide 19 (s-m5-ans) answer text "2 parts are bigger than 4 parts of the same circle" is wrong in words (a part of 2 is bigger than a part of 4). Guide timing line also says "papers to the camera 30 s" (see X2).

### Low
5. Workbook p5 look-back: options wrap ("something else", "I was not stuck", "asking a question", "I would like to pass" orphaned on their own lines). Same in all five lessons (X3).
6. Workbook G2 option "half circle" wraps onto two lines so it reads as "half" and "circle" (four words for three options). Same layout bug in L32 S5(c) and L34 E3.
7. Workbook p1 S3 and p2 S6: tidy but p2 is about 20 percent empty; slide pages `s-ws1`, `s-ws2` cards touch the footer line.
8. Parent summary: "These are Primary 1 shapes ideas" (grammar). Guide section 1: "tests four statements, and tests four statements" (duplicate phrase).
9. Home practice Q3 and Q4 ("a rectangle has 12 small squares", "a big square has 16 small squares") have no picture; home sheets cannot carry figures (X4). Kit sentence "We use them again" is only half true (L32 reuses one paper square).

---

## Lesson 32 Build the Figure

Solved: S1 4 squares, 3 triangles, 1 circle, 1 more; S3 boat 2 triangles + 2 squares (fewest triangles is 2: each slanted end needs one); S4 4, 3, 12; S5 rectangle, circle, half circle; T1 line across the roof then 2 lines through the middle; T2 5, 6, 3; T3 8 (4 small + 4 big); G1 6, 3; G2 T F T F (I checked that the staircase cannot be tiled by three 2-square rectangles; 2 rectangles + 2 squares works); E1 7; E2 Yes; E3 3. Key matches. Kit: squares are 30 mm (correct), triangles are half squares, rectangle is 2 squares: contract met.

### Medium
1. Workbook p3 T2 ("Count each kind of shape ... fill in the table"): the box with 4 squares in a 2 x 2 block also contains a big square, and the other box is a rectangle made of 2 squares. After the "Every Triangle" idea a child can reasonably count 7 squares or write "rectangle". Key says 6. Show the 2 x 2 block with a gap between squares or ask "small squares".
2. Workbook p2 S5: three words are circled but the sentence is split ("2 squares make a ____ . Circle one."): the dangling full stop, "Fill in the blanks. Circle one word each time" mixes two answer styles (WORDING_GUIDE 16), and (c) "half circle" wraps (reads as 4 options).
3. Deck slide 17 (s-m1 "2 shapes make 1 shape"): the tutor asks "What shape do 2 squares make?" while the slide already prints "2 SQUARES make a rectangle", "2 HALF CIRCLES make a circle" with the finished pictures. Answer shown while asking (known pattern). Reveal on the next slide.
4. Workbook p5 Investigation: the drawing box (about 50 mm high) is too small for "draw each shape you find";. Also deck workbook slides s-ws2: the boat picture is a few millimetres wide (illegible).

### Low
5. Kit p7 about 40 percent empty; kit p6 and p7 cut cells 3 to 6 mm apart.
6. Home practice Q3, Q4 no picture; Q5 "Practice from earlier: Term 2 Lesson 2" uses the strip idea with no strip.
7. Guide timing line "papers to the camera 30 s" (X2). Look-back wrap (X3).
8. Practice t3 and c4 are fine; variants plural-safe (checked all 12 + 4 + 5 + 4 combinations).
9. Kit text "We use them again" is false: no later lesson uses the pieces (hand-off 33 says "keep the shape pieces in their envelope" but L33 does not use them).

---

## Lesson 33 Copy on the Grid

Solved: S1 3 across, 3 up (L is 4 dots tall, 3 dots wide); S2 2 right, 2 up; S3 path 4 right, 1 up; S4 B (A has a shorter stem, C a wider bar and off-centre stem); S5 3 right, 2 up; S6 T F T; T1 RRRU plus URRR, RURR, RRUR = 4; T2 RRUU, RURU, RUUR (+ the three starting U) = 6; T3 9 and 3, 15 and 5; G1 4 / 3, 6, 10 / 10; G2 3, 2, 6; E1 4 right, 1 up; E2 5 right, 4 up; E3 No, 5. Key matches. Reading-order and glyph risks do not apply (no multiplication).

### Medium
1. Kit page (Workbook p6 and `L33_Kit_Pages.pdf`): the three 4 x 4 route grids are printed in one row with only a slightly wider gap (31 vs 54 px) and no boxes or labels, so a child cannot tell where grid 1 ends and grid 2 begins; the two copy grids are also adjacent. Add a frame and number each grid.
2. Workbook p5: the Investigation grid and the Exit E1 grid have dot spacing of about 5 mm (S and E markers ring 3 mm). A 6-year-old cannot count steps on them or draw a route; "Count the steps in each route: ____ and ____" has no room. Enlarge to the kit scale (13 mm).
3. Deck slide s-exit E1 and the workbook slides: grid thumbnails are about 4 px per dot (unreadable at 1080p). The exit slide cannot be read as a question; draw the grid on the slide at full width.
4. Beyond puzzle "Count the Routes" is the name in the guide and parent page, but nothing on the child page (T1, T2, G1, G2) carries the name, unlike L31, L32, L34, L35 which print the name. Add it to T1.

### Low
5. Workbook G3: sentence "B is [] right and [] up from A. C is ..." breaks mid-phrase across lines; E3 says "A child draws a copy" (fine per D18) but the cast name Ravi appears in T3 only. G1 answer boxes overlap the cell borders in the top row.
6. Deck: "Right, up, right, up" caption under the walked line does not match the instruction "2 right, 2 up, 1 right, 1 up"; slide "4 right, 2 up" introduces "4 left, 2 down" (left and down are not otherwise taught in Start here; practice t3 also uses "2 left"). The "Say where to go" slides show the answer in the title of the next slide, which is acceptable.
7. Home Q3 packs two questions ("Is it 9 steps long? Circle Yes or No. It is __ steps long."): WORDING_GUIDE 4 and 18 want (a) and (b).
8. Guide timing line "papers to the camera 30 s" (X2).

---

## Lesson 34 Cubes and Views

Solved with checks: S1 5 cubes; S2 3 visible, 1 hidden; S3 B (see 1); S4 top row 1, 3 and bottom row 1, 1 (6 cubes); S5 line across the middle; S6 7; T1 missing 2 (total 6 forces it), cannot see 1; T2 2 holes, second (the fold is on the left edge of the folded strip, so the opened holes are symmetric: option 2); T3 hole 1 step on the other side; G1 4, third (fourth picture, 2 x 2); G2 front right 2, hidden 1; G3 any four of 1 to 3 summing to 7; E1 4; E2 6; E3 down the middle. Key matches.

### Medium
1. **S3 ("Which top view matches this stack?") depends on an unstated convention.** The isometric picture is drawn with the far corner = back-left, right cell = back-right, left cell = front-left, near corner = front-right (`figs3.py cube_stack`: x = (c - r) w, y = (c + r) h). The tall stack sits at the left cell of the diamond; options A (back-left) and B (front-left) both have it "on the left". Nothing a child can see says that the left cell is in the front row. "The back stacks go in the top row" does not tell them which diamond cells are back. Two defensible answers for a child. The same mapping is needed in S4, T1, G2. Teach it (a drawn "stand here" arrow) or draw the stack from the front, or print the numbers on the picture.
2. **Cube pictures are tiny.** S1 stack about 19 mm wide, S2 about 15 mm, E1 (exit) about 11 mm for 4 cubes with edges only 3 to 4 mm. Counting a hidden cube in a 11 mm isometric picture is not realistic for a 6-year-old. Same in the deck: sneak-peek, Explore and "The top view" thumbnails are 8 percent of the slide width; deck workbook slides show them smaller still. Enlarge to 40 mm or more (the figure is vector, there is room).
3. **Class and workbook reuse the same numbers (known failure pattern 3).** Explore "6 blocks, 5 shown, 1 hidden" = T1 "6 cubes, you can see 5, cannot see 1"; class top view "1, 1 / 3, 1 = 6" = S4 "1, 3 / 1, 1 = 6"; class "Fold once, punch once: the fold is on the left, one hole" has the same wording as T2 and the same answer. Change one set.
4. Workbook p3 T2 and p4 G1: the three option pictures carry no "first / second / third" labels; the folded paper (first picture) looks like a fourth option. Label the options 1, 2, 3 or A, B, C beneath.
5. Kit p6: four 88 mm squares with no centre mark (preflight asked for one); neighbouring dashed edges only 3 mm apart (rule 6 mm). "We use them again" is false (hand-off says not needed again).
6. Practice plural bug: t2 variant "One hole is 1 steps from the fold line"; c3 variant "1 cubes in the front stack" (guard "1 step", "1 cube").

### Low
7. T3 dot grid spacing 5.6 mm: a hole drawn on it is hard to place; E3 options wrap ("down the middle / across the middle").
8. Slide "Check page" fine; guide timing "papers to the camera 30 s" (X2); look-back wrap (X3).
9. Home Q4 "one hole ... one hole is 3 steps" confusing wording (two senses of "one hole"); no pictures on home sheet (X4).
10. Parent page and guide agree that real punching is not done (pencil dots only): good.

---

## Lesson 35 Spot It

Solved: S1 size, number, turn; S2 Yes, No; S3 C, pattern (dots among stripes); S4 1 more; S5 3 differences, tile 1 same (tile 2 number, tile 3 size, tile 4 turn); S6 A and D (B has stripes, C is a triangle); T1 C, number; T2 C (3 circles of the size of the 3 squares; D is the small-size distractor); T3 circle, 10; G1 B (a quarter turn of the L; A is the mirror, C has 5 squares, D is a T); G2 D, B; E1 pattern; E2 C; E3 2. Key matches.

### High
1. **Online practice, Think harder item 3 ("Look across, then look down. Which tile is the missing piece?", `out/l35/practice/data/t4l35.json` id `t3`) cannot be answered.** The SVG is 244 x 356 and shows the 2 x 2 matrix plus ONE unlabelled tile; the four answer choices A, B, C, D appear only as text radio buttons with no pictures (confirmed in Chromium: the picture contains a single "?" and no A to D labels). The key answer is "B". A child cannot choose. Fix: render the four option tiles with letters in the figure (as item c3 does) or switch to a "set" of pictures.

### Medium
2. Tiny tiles and labels (workbook p1 S3, S6; p3 T1, G2; p5 E2): tiles 11 to 14 mm, letters A to E about 2 to 3 mm. A hatched tile versus a dotted tile at 11 mm is hard for a 6-year-old to tell and must survive B&W: in my 1-bit simulation the pink fills disappear (white) and only stripes and dots remain, so "plain versus pink" would not be a cue (the lesson does not rely on it, good, but check the real B&W conversion; Book 7 is not built yet, X1). Enlarge the tiles to 20 mm and the letters to 5 mm.
3. Kit cards (Workbook p6): the three sets differ by kind of object (cookie among apples, spider among ladybirds, jar among cups), not by one of the five features the lesson teaches (shape, number, size, pattern, turn); the guide's Explore asks "what is different" and children will say "it is a cookie", which does not train "one feature at a time". Make the cards the lesson's tiles (same object, one feature changed).
4. Workbook p2 page instruction "Count the differences. Tick each tile that is different." does not fit S4 (count apples) or S6 (write two tile letters); nothing is ticked. Also S5 asks "There are __ differences" where the tile count and the feature count agree only because each different tile differs in exactly one thing: say "tiles that are different".

### Low
5. Home Q3 is a spot-the-difference question with no picture (words only); Q2 "There is [] more star" fixed singular.
6. Kit text "We use them again" is false (hand-off: pair cards not needed again).
7. Deck workbook slides: pictures are 4 to 8 mm wide; slide `s-exit` E1 to E3 tiles unreadable.
8. Guide timing line "papers to the camera 30 s" (X2); look-back wrap (X3).
9. Overlap: "odd one out" and a repeating pattern also appear in the holiday course (Logic Lab, Pattern Inquiry); concept spiral only, no reused item or number found by text search.

---

## Cross-lesson findings (X)

X1 (Medium). Book 7 (L31 to 35) is not yet assembled into `outputs/print/term` or `outputs/print/bw/term` (only Books 1 to 4 exist), so the printed black and white result of these workbooks, kit cut pages and the "every page starts on a right-hand page" layout cannot be checked. Do a B&W render check before release (pink fills and light-blue faint lines are the risks).

X2 (Medium). All five tutor guides still print the timing assumption "papers to the camera 30 s" (L31 to 35, section 2, last paragraph), although the lesson text says nobody holds paper to the camera. The owner rule is no paper to the camera; the wording is stale (`tools/b_guide.py`, already on the Term 3 fix list).

X3 (Low). Look-back box wraps in all five workbooks and on the slides (options orphaned, "I would like to pass" alone).

X4 (Low). Home practice sheets carry no pictures, so questions about shapes, grids, stacks and tiles (L31 Q3, Q4; L32 Q3, Q4; L33 Q1; L34 Q1; L35 Q1, Q3) are word-only.

X5 (Low). Kit boilerplate "We use them again" appears on the kits of L31, L32, L34 and L35; later hand-offs say the pieces are not needed (L34, L35) or do not use them (L32).

X6 (Low). Slides: many slides leave 50 to 60 percent of the screen empty with small pictures; workbook-page slides show pictures at 4 to 8 mm (legibility at 1080p).

X7 (Low). Practice rewind items (`r1`, `r2`) are copies of Term 3 Lesson 1 to 5 items, one per lesson; fine, but they are the same sentence as the earlier lesson's items (checked by text search), so a child who did the earlier practice sees them again.

## Owner-decision checklist (all five lessons)

| Rule | L31 | L32 | L33 | L34 | L35 |
|---|---|---|---|---|---|
| 90 minutes with timing model, 5 min buffer, no part over in slow class | pass | pass | pass | pass | pass |
| Beyond-syllabus item present, named, Think harder or Go further | pass | pass | pass (name not on child page) | pass | pass |
| No end-of-term check, no Challenge Quest content | pass | pass | pass | pass | pass |
| Originals only (no contest text); 7-word overlap not found | pass | pass | pass | pass | pass |
| No MOE, GEP, SASMO claims, no prices | pass | pass | pass | pass | pass |
| Recording notice before recording | pass | pass | pass | pass | pass |
| No paper held to the camera (lesson text) | pass | pass | pass | pass | pass (X2 stale line) |
| Hand-off to next lesson true | pass | pass | pass | pass | pass |
| Mi without calculator | pass | pass | pass | pass | pass |
| Kit pieces exist and counts match | 10, but 28 mm | 20 ok | not cut ok | 4 ok | 12 ok |
| B&W readable (no colour-only cue) | pass | pass | pass | pass | tiles small, check |

## Recommended fix order

1. L35 practice `t3` unanswerable (High). 2. L31 kit scale (High). 3. L34 S3 convention, picture scale, number reuse (Medium). 4. L33 kit grid labels and the tiny Investigation/exit grids. 5. L32 T2 and s-m1 answer shown while asking. 6. L35 kit cards by feature and tile size. 7. X1 build Book 7 and check B&W. 8. X2 guide timing line. 9. Low items.
