# Final fixes, Level 1 Term 2 (Lessons 11 to 20)

Fix pass of 23 Oct 2026 against `FINAL_AUDIT_T2.md`, finishing the partial edits left by the container restart. Lessons 11 to 20 rebuilt with `bash term/l1/build.sh NN`. Full validator summary lines after the final rebuild (`validate.py NN`, built files included):

| Lesson | Summary |
|---|---|
| 11 | 26 pass, 4 warn, 0 FAIL |
| 12 | 26 pass, 4 warn, 0 FAIL |
| 13 | 26 pass, 1 warn, 0 FAIL |
| 14 | 26 pass, 1 warn, 0 FAIL |
| 15 | 27 pass, 2 warn, 0 FAIL |
| 16 | 27 pass, 1 warn, 0 FAIL |
| 17 | 27 pass, 0 warn, 0 FAIL |
| 18 | 27 pass, 0 warn, 0 FAIL |
| 19 | 27 pass, 3 warn, 0 FAIL |
| 20 | 28 pass, 3 warn, 0 FAIL |

Warnings are slow-class OVER flags absorbed by the buffer and kit-page fill; none is new. Not touched: shared tools (`term/l1/tools/*`, runner, schema, `print/`), Term 1 and Term 3 lessons, website, `school/`.

## High

| # | Finding | Action |
|---|---|---|
| 1 | L11 and L17 outputs carry Mi with the calculator | Both lessons now build (see 2). All ten lessons rebuilt; embedded Mi is the no-calculator image. **Open, not mine:** the print books (`print/make_term_books.py`) must be rebuilt from these outputs. |
| 2 | Validator FAIL (catalogue overlap) blocked the L11 and L17 builds | Cleared by the earlier wording of the two items and the Term 1 copy-check fix; `validate.py 11` and `17` are 0 FAIL and both built. |

## Medium

| # | Finding | Action |
|---|---|---|
| 3 | L20 Quest tutor notes Gate 6 part answers | Part answers are 15 and 11 (S1 part answer fixed too). Checked on the built `L20_Quest_Tutor_Notes.pdf`: "(a) ... = 15; (b) ... = 11". |
| 4 | Recording notice said after recording starts (L13, L14, L17-L20) | All ten lessons now use the same opening: greet the whole group, say the Term 1 recording notice, then "Start the recording now", then the Term 1 microphone and no-paper line. Wording identical to the Term 1 lines ("any voice that is not muted", "You may keep your microphone and camera off", "Cameras can be on or off, as you like", "Nobody holds paper up to the camera"). Tutor-prep lines and notes say notice first, recording second, no first names once it runs. |
| 5 | Recording statement missing on parent pages L13-L20 | One identical sentence on every parent page (L11-L20) in the Next lesson box: "The recording has the tutor, the shared screen and any voice that is not muted; your child may mute and keep the camera off. To have your child muted, tell us when you register. The link is private to your group's families: please do not share it." This matches `website/privacy.html` (mute route at registration, private link for the group's families). The retention sentence was left to the privacy page to keep the parent page on one sheet. |
| 6 | Mixed lesson numbering | All lesson data now reads "Term 2 Lesson N" (hand-offs, notes, parent pages; no bare "Lesson 1x" for a Term 2 lesson, and "Term 1 Lesson N" for Term 1 references). Workbook and kit headers read "Term 2 • Lesson N". **Open, not mine:** Book 3 and 4 covers and contents (print tool) and the L10 goodbye slide and L10 parent text ("Term 2 starts with Lesson 11") in Term 1. Quest tutor notes list gates by overall id ("L13") next to "Term 2 Lesson 3"; left (tutor only, `quest_build.py`). |
| 7 | Book 4 contents row for L17 blank | L17 `workbook.header` is now "Division: sharing and grouping" (one line), so the contents parser can read it. Book itself to be rebuilt by the print owner. Clipped note on contents page 2 is a print-tool item. |
| 8 | Two ways to get the workbook | All hand-offs and parent pages say "Your Term 2 Lesson N workbook" (from the issued book) and the parent Next box says "A missing workbook page: your tutor sends a PDF to print at 100%". The kit-page "print on its own sheet" note is printed by the shared tool: open. |
| 9 | Start here modelled longer than allotted (L11, L12) | Not cut. The timing notes state it plainly (L11 18 of 17 minutes, L12 about 18 of 16.5; Think harder, Go further and the Investigation are for early finishers and home, and the page says so). The flex buffer absorbs it. To be settled with a first live class. |
| 10 | L14 S3 chart tiny, page 3 crowded | S3 is now a 2 x 10 table with 64 px cells and 40 px numerals; page 3 frames no longer touch (viewed, pages 1 and 3). T3(c) shortened to "Circle one." and the claim stems shortened. |
| 11 | L15 parent page lacks the beyond item; L14 exception | L15 parent summary names the 60-marble Go further item as beyond the school range; L14 states that the whole lesson is Primary 2 on purpose (owner default 3). |
| 12 | L19 shape cards are words | Kit page 7 is now 15 drawn shapes (three each of circle, square, triangle, heart, star; coloured, dashed cut lines). Materials and kit text say "drawn shapes, each big enough for 3 counters". Viewed. |
| 13 | L17 S1 hint says 12; G1 stem says (a) and (b) | Hint says 8; stem says (a), (b) and (c). G1(c) answer line lengthened to six blanks (viewed on page 4). |

## Low (cheap ones done)

| # | Action |
|---|---|
| 14 | Left: L16 Go further uses two tables, as delivered. |
| 15 | L14 G3 changed to 4 + 8 (not the class pair). |
| 16 | Not mine: cover tagline is a shared template line. |
| 17 | L13 tutor prep no longer says the syllabus check is pending; `moe.note` records the desk check. |
| 18 | Tutor prep "Children video" typo already corrected ("Children's video is excluded") in L19, L20. |
| 19 | L14 `next_materials` now names the Term 2 Lesson 5 workbook. |
| 20 | L17 G1(c) answer line lengthened (see 13). |
| 21 | Look-back type size is a shared template matter: open. |
| 22 | Slow-class OVER on mini parts stays inside the buffer (validator warns only). |

## Parent pages kept to one sheet

Adding the identical recording sentence pushed six parent pages onto a second sheet (validator FAIL, build refused). Fixed by shortening the Next box (dropped "no timers, no scores" and the retention sentence), the next-materials lists (removed "(from your printed term book)" and the "pencil, rubber and paper" line) and a few word-box lines in L14, L17, L18. All ten parent pages are one page.

## Needs a shared-tool or owner step (list)

1. Rebuild `outputs/print` Books 3 and 4 (`print/make_term_books.py`): new Mi in L11 and L17, "Term 2 Lesson N" on covers and contents, L17 contents row, clipped note on contents page 2.
2. Term 1 L10: goodbye slide and parent text still say "Lesson 11" for the first Term 2 lesson.
3. `tools/b_print.py`: kit-page note "print on its own sheet" is wrong for the bound book; look-back type size; cover tagline.
4. Owner: whether Term 2 recordings keep the "cameras and names are not recorded" line, which privacy.html still marks "[Confirm the platform setting before the first lesson]" (left off the parent pages for that reason).
