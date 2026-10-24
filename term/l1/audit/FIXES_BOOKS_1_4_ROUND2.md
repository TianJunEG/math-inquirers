# Fixes after the Books 1-4 round 2 audit (24 Oct 2026)

Source: `AUDIT_BOOKS_1_4_ROUND2.md`. Scope: Level 1 term pipeline for lessons 1-20 (`term/l1/lessons`, `tools/b_print.py`, `b_quest.py`, `spine_term.py`, `verify/`), rebuilt: all 20 lessons, the 12 colour books (`print/make_term_books.py`), the 12 B&W books (`print/make_bw_print.py`), `validate.py` on every lesson (0 FAIL), `print/check_bw.py` (all 24 term B&W files ok). Page counts unchanged: workbooks 46/44/46/46, keys 22/32/22/30, home packs 12/14/12/14, all even; contents page numbers re-checked against the first page of each lesson (workbooks 3/11/21/31/39, 3/11/19/27/33, 3/11/19/29/37, 3/11/19/27/35).

| Finding | Status | What was done |
|---|---|---|
| H1 Book 1 p23 (L3 Think harder) T3/T4 no writing space | CLOSED | New `side` layout in `b_print.qbox`: the digit cards sit on the left, the answer lines on the right. T1/T2 parts moved beside their cards (saves height), T3 and T4 now have 2 writing lines each (T4 also keeps "There are ___ numbers"). The page now fits without any tightening level. |
| M1 "In my head" in Quest Tutor Notes of Keys 2 and 4 | CLOSED | `b_quest.py` now says "No tool". 0 matches for "In my head" in all 8 keys. |
| M2 text sizes | CLOSED where the layout allows, minima stated below | Exit-ticket stems 17.7 px (12.5 pt printed), True/False table cells and the "Put a tick" line 17.7 px, the italic instruction line stays 17.7 px even on the tightest levels (was 15.5), the last tightening level no longer shrinks question text (was 15 px). Chips and Quest rows: see below. |
| M3 writing lines for the written reason: B2 p5, B2 p21, B4 p13, B4 p37 | CLOSED | New `why` row (label + writing line, 24 px, kept on every tightening level) and `reason` flag. B2 p5 (L6): T1-T4 each "How do you know?" and the instruction shortened to one line so the page fits. B2 p21 (L8): T1 (b) "I know because:" with two lines (page had 20 mm free). B4 p13 (L17): T2 "How do you know?", instruction now says "Then write how you know". B4 p37 (L20): T1 and T2 "I chose it because". |
| M4 home intro collides with the "No.1" tab (12 sheets) | CLOSED | Intro paragraph keeps 24 px clearance on every home tightening level (`.page.hm.hm>p.hint.hint`). All 25 home sheets still one page (L29 sheet is 100 % full, the fullest). |
| M5 B1 home p9 (L4 No.2) mini-grid showed 68 | CLOSED | The whole bottom row of the mini-grid is "?" (67, 68, 69 hidden). Also fixed: the figure now sits beside the text on the right like the other home figures (a `h100` grid rule was pulling it above "Start here"). |
| M6 Similarity, NEW story AND NEW frame (hand-solved, keys, online twins, parent line and `verify/` oracles updated) | CLOSED (see detail) | |
| M6a B2 L10 T2 (red book, 5 left 3 right) | CLOSED | Now "A tin has 36 crayons. Siti takes out 10. Jamie takes out the same number as Siti. How many are left?" 36-10 = 26, 26-10 = 16. (Also fixes a stale part answer "11" that disagreed with the key answer 9.) Online twin t2 and parent try-home line replaced the same way. No longer shares 5/3/9 with the Quest cave. |
| M6b B3 L1 T1 and home H4 | CLOSED | T1: "Lily is 4th from the front. Ravi is 3rd from the back. There are 3 children between them", Kumar says 7: No, 3 + 1 + 3 + 1 + 2 = 10 = 4 + 3 + 3. Home H4: "Ravi is 7th in the line. 3 children in front of him go home. Which place now?" 4th. Online twin replaced (template a + b + c). |
| M6c B3 L2 T2 | CLOSED | "Kumar has 31 coins. He gives 5 to Aisha. They then have the same number. How many did Aisha have at first?" 31-5 = 26, 26-5 = 21 (bar picture to scale, arrow "5"). Online twin t2 replaced. The mini-lesson worked example (Ali 30, Mei 18, tutor-only script and slide) is unchanged: OPEN, see below. |
| M6d B2 L7 T5 | CLOSED | "A baker bakes 82 buns. At closing time 57 are left. How many were sold?" count up 3 + 20 + 2 = 25; script line for T5 updated. |
| M6e B2 L10 T5 | CLOSED | "Ravi has 40 stamps. He gives some to Mei. Then he buys 6 more. Now he has 31. Go backwards: how many did he give?" 31-6 = 25, 40-25 = 15 (brute-force oracle in `verify/l10_checks.py`). |
| M6f B2 home L10 H4 | CLOSED | "Ravi has 12 points. He has 5 fewer than Aisha. Aisha has 3 more than Kumar. Kumar?" 12+5 = 17, 17-3 = 14. |
| M7 L10 slide notes, Explore timing | CLOSED | Slide notes of rounds 1-3 now say about 45 to 50 seconds of working time (about 2 minutes with the reads, thumbs up and answer), matching the script (50/45/50 s). |

## Measured minima in the rebuilt books (PyMuPDF, printed points, colour PDFs; B&W has the same pages)

| Item | Before | Now |
|---|---|---|
| Exit-ticket stems, all lessons | 12.0 | 12.5 |
| True/False statement cells (B3, B4) | 11.3 | 12.5 |
| Italic instruction lines on the tier pages | 11.0 | 12.5 (13.1 where not tightened) |
| L10 and L20 tool-name chip (B2 p33, B4 p35) | 6.1 (the earlier report said 6.5) | 12.6 |
| Quest tool row, Book 2 (5 names + No tool, page 1 is 99 % full) | 9.0 | 9.1: the largest size that keeps the four designed pages (12.5 px already pushes gate 2 onto a new page) |
| Quest tool row, Book 4 (7 names + No tool) | 7.9 | 13.3 (wraps to two lines) |
| Quest instruction lines pp 2-4 | 11.6 | 13.3; page 1 stays 11.6 (page full) |

Still below 12.5 pt and not changed (text inside figures and small chrome): table and graph labels drawn inside figures 10.7 to 11.3 pt ("Groups | In each | Total", "Jumps of 5", "Sweets | Friends", price-tag and strip labels 10.7-11.3), line-up and top-view labels (FRONT, names) 11.0-11.4, balance tile labels 7.0, bar labels, the Quest "Page N of 4" tag 11.2, the Quest page 1 intro box 12.4 and instruction 11.6, "Tool I used" look-back rows 8.5, "Look back" heading 11.8, chip definition and "also useful" lines 9.9, Toolbox kit text 9-10.

## Not closed / owner calls
- The tutor-only teaching example in the L12 mini-lesson (script and slide "Ali has 30 stickers and Mei has 18, gives some so they have the same") and the sneak-peek puzzle still use the transfer frame the audit matched; only the workbook item and its online twin were replaced.
- B3 L11 online item "t1" and old home H5 ("Ali is in the middle ... Ben") were not in the brief; round 1 M9 remains.
- Quest Log page 1 (both books) is full, so its tool row and instruction line cannot grow without a fifth page. Only a layout change (a smaller Mi box or figure) would allow it.
- All Lows of the audit (doubled "because", pill buttons, key wording, small figures, kit repeats) were not in the brief and are unchanged.
- No physical print proof, no photocopy test.
