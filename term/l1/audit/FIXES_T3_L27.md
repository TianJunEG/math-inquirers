# Fix pass, Term 3 Lesson 7 (lesson 27, Fill the Grid)

Against `WORKBOOK_AUDIT_L27.md` (WB), `GUIDE_DECK_AUDIT_L27.md` (GD) and `HOME_PARENT_PRACTICE_AUDIT_L27.md` (HP). Rebuilt with `bash term/l1/build.sh 27`: validator 28 pass, 0 FAIL (verify script extended, 208 checks); parts sum to 90, none over (script 68:36, slow 81:08); workbook fills 95, 99, 96, 92, 100% (kit page 83%, 6 pages as designed); home 99%; parent 97%; template leak clean; no slide overflow. Viewed: all 6 workbook pages, the 3 key pages, home sheet, parent page, slides s-m2, s-m3, s-m5, s-ws2, s-ws2b, exit. Not touched: shared tools, `l20.json`, other lessons.

| Finding | Action |
|---|---|
| WB 1 kit mat 2 loses a column (Medium) | Shared tool (`figs3.grid_tiles` table width). Not fixable in lesson data. Listed in FINAL_FIXES_T3.md. Go further does not need the mat. |
| WB 2 tile cut lines 2.7 mm apart (Medium) | Shared tool. Kit intro now carries the "no printer or no cutting" line (nine small things on a drawn 3 by 3 grid). Listed. |
| WB 3 Investigation (Medium) | Brackets were printed as text: the first step is now "Row 1 is 1 3 2. Row 2 is 3 2 1. Write row 3: ____ ____ ____" and its grid has a 2 in the middle (it is one of the four, and the text gives it as the first one). "A turned grid is a different grid" settles the count (answer 4); the answer key and the mistake line no longer say a turned grid is the same; four lines are for four grids written row by row; look-for rewritten (the 2s lie on one of two diagonals). A drawing box and a grid picture were tried and spilled the look-back onto a seventh page. |
| WB 4 / HP 2 online g1 steps wrong (Medium) | Steps rewritten as the audit proposed (row 3 first box is 2; row 2 has a 4 so a is not 4; column 1 has 3 and 2 so a is 1 or 4, so 1); the verify script checks each fact. |
| WB 5 / GD 1 / HP 3 `l20.json` hand-off (Medium) | `l20.json` is owned by the Term 2 fix agent: not edited. Mismatch reported: it must say a grown-up cuts out the 6 clock hands and the $1 tokens are kept (see FINAL_FIXES_T3.md item 1). |
| WB 6 S4 words only (Medium) | S4 is now a picture of a 3 by 3 grid (rows correct; columns 1 and 3 repeat), different from every class grid; text, hint, script READ, slide note and checker updated. s-ws2 then overflowed, so question 5 has its own slide (s-ws2b, 29 slides). |
| WB 7 S5 and G3 same step (Low) | G3 now asks (a) how many boxes in a 5 by 5 grid (25) and (b) how many hold a 4 or a 5 (10); key, tutor prep, checker updated. Online g2 now asks how many boxes hold a 1, a 2 or a 3 (3n) with a "rows and columns" sentence (also removes the "A 8 by 8" slip, HP 9). |
| WB 8 G1, G2 small grids, "?" meaning (Low) | Print size of grid figures is fixed by the shared template (`.vis.md`). In G2 the boxes that are not asked are now blank and the text says so; "?" no longer means two things. |
| WB 9 T2, T3 text only (Low) | T3 picture was added and removed: it spilled page 3 onto a new page. T2 unchanged. Not done (page full). |
| WB 10 look-back wrap (Low) | Shared template. Listed. |
| WB 11 / "We use them again" (Low) | Printed by `b_print.py` (shared). Parent page now says the tiles are not needed again; listed. |
| WB 12 / GD 11 "about 16 minutes" (Low) | Now "about 15" in `timing.notes` and the Work NOTE (6.0 + 8.5 = 14.5). |
| WB 13 / HP 6 term line (Low) | "Your child is learning to give a reason for each step." |
| GD 2 s-m4 question singular (Medium) | Slide has two bad columns; the ASK and note now say "Which columns have two of the same?" The workbook S4 grid is a different picture. |
| GD 3 s-m2 column as a bullet list (Medium) | A one-column picture prints at full slide width (overflows); a table overflows the column. The list now reads "top box: ?", "middle box: circle", "bottom box: triangle", so the stack is clear. Partly done. |
| GD 4 s-m3 label "a" too small (Medium) | Slide is now a grid plus a card "BOX a IS THE MIDDLE BOX / Its row has a square. Its column has a circle." so the box is named in large type; the tiny "a" label remains (panel label size is fixed in `figs3.panel`). |
| GD 5 s-menu versus guide M1 (Medium) | Slide row now "Row right, column right? Test it with the same row three times." (the guide's M1, which is true). |
| GD 6 Explore camera (Low) | Added: tilting the camera to the table is allowed, a face need not be in view, nothing is held up to the camera. |
| GD 7 REC cue before DO (Low) | Opening now follows the Term 1 fix (FINAL_FIXES_T1 finding 4 and the Lesson 24 opening): REC, three SAY lines (cameras on or off; recording statement "any voice that is not muted"; "Microphone off until I ask you to speak ... Nobody holds paper up to the camera"), the story line, then DO "Greet the whole group warmly. Do not use children's first names on the recording." Tutor prep matches. |
| GD 8 "papers to the camera 30 s" (Low) | Printed by `tools/b_guide.py` (shared). Listed. |
| GD 9 s-m5 pill overlaps footer (Low) | Pill removed; the note tells the tutor to say "on your paper". |
| GD 10 E2 options not on the slide (Low) | Not changed: options are read aloud and the slide stays on the short question form (shared `qs` block). |
| HP 1 H3, H4 words only (Medium) | The print tool has no pictures for home items (shared). Both questions now start with "Draw a 3 by 3 (4 by 4) grid of boxes." Listed for a tool picture. |
| HP 4 rewind items (Low) | Runner (shared). |
| HP 5 recording sentence on parent page (Low) | Added "The recording has the tutor, the shared screen and any voice that is unmuted. Please do not share the link." |
| HP 7 picture alt text (Low) | Shared figure tool. |
| HP 8 c4 up to 6 by 6, no picture (Low) | n limited to 3, 4 or 5. |
| HP 10 parent try-at-home (Low) | "use mat 1 from your kit page, or draw a 3 by 3 grid". |
| Hand-off to Lesson 28 | Checked against `l28.json`: strip page, 14 paper strips, no matches or toothpicks: consistent. Quest gate for this lesson is in Lesson 30 (not edited): its grid must differ from every grid here (the checker lists them). |

## Shared-tool needs (for FINAL_FIXES_T3.md)
1. `figs3.grid_tiles`: mat 2 draws 3 columns and a stump (width); tile cut lines 2.7 mm apart (rule 6 mm).
2. `b_print.py`: "We use them again" is wrong for the grid tiles; home items have no picture slot (H3, H4 need a small grid); look-back wraps; `b_guide.py` "papers to the camera 30 s".
3. `b_deck.py`: a single-column panel is drawn at the full slide width, so a column picture cannot be shown; panel label size is fixed (box labels are small); rows of `qs` with grid pictures overflow when three are on one slide.
4. `l20.json` hand-off (Term 2 owner).
