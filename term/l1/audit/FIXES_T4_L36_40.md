# Fixes for the Term 4 audit, Lessons 36 to 40

Source: `AUDIT_T4_L36_40.md`, `TOOLS_FIXES_T3_T4.md`, `FINAL_FIXES_T3.md`. Files changed: `lessons/l36.json` to `l40.json`, `verify/l36_checks.py`, `l37_checks.py`, `l40_checks.py`, and one line of `tools/figs3.py` (graph mat `cell` key, see M4).
Rebuilt with `bash term/l1/build.sh NN` for 36 to 40 only. `validate.py NN`: 0 FAIL for 36, 37, 38, 39 and 40. Looked at after rebuild: L37 workbook (all pages) and kit page, L40 Quest Log (4 pages), L40 tutor notes and parent note text, decks (L36 s-sneak, s-rem1, L38 s-sneak, L39 s-m1).

Status: FIXED / NOT FIXED (reason).

## High
None in the audit.

## Medium
| Id | Status |
|---|---|
| M1 Books 5 to 8 not built | NOT FIXED here. It is a print-pipeline job (`make_term_books.py`, `make_bw_print.py`), outside lesson files. Still to do before release: build Book 8 and check L36 S6 and the yellow squares in black and white. |
| M2 L36 sneak-peek "8 squares" | FIXED. Item, deck slide, key, "Back to the sneak-peek", guide and script now say "How many small squares are in the picture?" and the answer "8 small squares"; notes say the grid also holds bigger squares that are counted later. Verify script updated. |
| M3 Quest gates reuse lesson numbers (L38 M3, L40) | FIXED. Gate 1: rectangle of 3 rows of 3 squares (9). Gate 5: a new 5-dot picture with 7 lines (pentagon plus 2 inside lines, nothing crosses) and 3 boxes of 5 pencils (15). Gate 6: new picture, flowers, Ali 4 pictures and Mei 7, each picture 2 (8 flowers; 6 more). Gate 7: tower 6, 10, 14 with 4 more each row (row 5 is 22). Script READ lines, tutor notes, answers and mistakes follow. Checked by script: no gate's numbers equal any item text in lessons 31 to 39. The L40 verify script recomputes all new gates. The tutor-note claim about fresh numbers is now true. |
| M4 L37 graph mat vertical | FIXED. The mat is now 5 rows of 8 squares (one row for each kind, like every graph in the lesson); slides, guide, workbook kit page, materials and the Mi example (`orient` rows) say "one row for each kind"; "turn the mat on its side" removed. The stray bars were already removed by the tools fix. Needed one tool line: `figs3.py` now passes `cell` to `graph_mat` (the lesson uses 56 so 8 columns and the key box fit the page). Also made S1's picture table a little smaller (84) so S3 stays on page 1 after the bigger icons from the tools fix. |
| M5 L39 parent page promises a PDF | FIXED. L39 parent "next" now reads "If anything is missing or damaged, message us on WhatsApp." The L40 grown-up note uses the same line. No family-facing page of L36 to L40 promises a PDF or a resend; the draft policy appears only in tutor-only notes (guides, tutor_prep, Quest tutor notes). Found outside my scope: `lessons/l35.json` (parent page, line about "Book 8 not here? ... we will send a PDF straight away") still promises a PDF. Owner of L35 must reword it. |
| M6 "Quest Log in an envelope" | FIXED. L39 parent page, hand-off, goodbye line, L40 guide, tutor notes and grown-up note now say to keep "those 4 pages" closed. "Print at 100%" was removed from `b_quest.py` by the tools fix; confirmed absent from the rebuilt Quest Log. |
| M7 s-quest1 recorded before the pause | FIXED. L40 script: the recording cue is spoken, then "Pause the recording now", then the Quest slide and the Quest introduction. Nothing of the Quest is recorded. The work segment starts with "The recording is on again, for the workbook." The guide chapter note (generated) is now true. |
| M8 Gate 4, gate 1 picture, gate 3 fold | FIXED. Gate 4: tiles A, B and D are 2 triangles, C is 2 circles (same number, same size, same pattern), so only the shape differs; answer C and shape; tiles drawn larger. Gate 1: the picture is a plain circle (the 4 parts are no longer given away). Gate 3: the paper is shown with its dashed fold line, beside the folded paper with the hole; text and script say so. |

## Low
| Id | Status |
|---|---|
| L1 L36 optional slide differs from workbook E3 | NOT FIXED. Correct maths; note only. |
| L2 L36 kit asks for 8 paper people | NOT FIXED. Note only, as the audit says. |
| L3 L37 tally marks | NOT FIXED. Already flagged as an activity in the guide. |
| L4 L37 guide beyond item (4 lollies vs mints, toffees, gums) | NOT FIXED. Not found as a separate guide string; the beyond items in the data are mints, toffees and gums. |
| L5 L38 workbook labels S1 to S6 vs "questions 1 to 3" | NOT FIXED. Not changed in this pass. |
| L6 L39 PLAY MONEY caption, T4 order, "14 - 5", kit card, deck slide 6 table | PARTLY. Deck slide s-m1 (table of 7 tools) overflowed the slide: table size reduced to 84 so "Steps" and "Work backwards" fit. The other items are not changed. |
| L7 L40: S2 "tick" with no boxes; "nobody sees your ticks"; S5(b) wording; look-back claims | FIXED for S2 (now "Circle one in each row. This is for you and your grown-up. Your tutor only sees it if you choose to share it.", script and hint follow) and S5 (b and c now say "your answer to part a / part b"). NOT FIXED: exit ticket page "at the end of the lesson" (text is in `b_print.py`, shared); Quest tutor notes first line "one from each lesson of the year" (text is in `b_quest.py`, shared). |
| L8 Quest Log answer lines about 2 cm | NOT FIXED. Layout is in `b_check.py`, shared. |
| L9 deck workbook-page thumbnails | NOT FIXED. Shared `b_deck.py`. |
| Deck overflows seen in the build (L36 s-rem1, L38 s-sneak) | FIXED by drawing the picture one size smaller (size s). |
| L10 | Passed in the audit. |

## Owner-decision checks after the fixes
90 minutes (L40 script 70:19, slow class 82:41, work part within its 15 minutes); no "hold paper to the camera"; recording notice before recording (restart line added); Quest rules unchanged (20 minutes, game, no scores); originals only.
