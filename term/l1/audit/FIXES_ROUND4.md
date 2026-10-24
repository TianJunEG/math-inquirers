# Fixes after final audit round 4 (Level 1 term books 1-8)

Date 24 Oct 2026, branch claude/great-fermi-1hv4vc. Source: `AUDIT_FINAL_ROUND4.md`. Owner-accepted L1-SIZES-OK (Quest tool rows, in-figure text, draw clocks about 31 mm) was not re-opened.
All 40 lessons rebuilt (`build.sh NN`), 24 colour books (`print/make_term_books.py`) and 24 B&W books (`print/make_bw_print.py`, `print/check_bw.py`) regenerated. `validate.py`: 0 FAIL on all 40 lessons. Page counts unchanged and even (workbooks 46/44/46/46/42/44/48/42, keys 22/32/22/30/22/32/22/32, home packs 12/14/12/14/12/14/12/14); contents numbers are generated from the real page positions, keys included.

## Closed / not closed

| Item | Status | What was done |
|---|---|---|
| M1 L23 exit script and note | Closed | `l23.json`: read-aloud E3 is now the book's "The class ends at 5 o'clock ... Which clock shows when it started? Circle A, B or C."; check line "E1: 7:30. E2: option 3, 2:30. E3: clock A."; `s-exitans` note "7:30; option 3, 2:30; clock A (4:30)"; E1 part answer 7:30. |
| M2 L36 guide E2 | Closed | `l36.json` script reads the bridges and buses wording (answer 9). |
| M3 L23 s-ws1 clipped | Closed | New optional slide block key `vw` (picture width in px) in `b_deck.py`; L23 s-ws1 uses 190, content now ends well inside 1080 px, "LAYOUT slide overflows" gone. L36 s-ws2 (vw 270) no longer touches the footer. Same fix applied to other overflowing slides found in the build logs: L21 s-ws1, s-ws2, s-exit; L22 s-exit; L25 s-ws2; L26 s-ws1; L33 s-ws1 (S3 was cut off); L34 s-ws1, s-ws2, s-exit. All messages gone. **Open:** L9 s-m4 still reports bottom 1056 px (21 px into the footer band, not cut off). |
| M4 L40 holiday frame | Closed | New frame "two things, one is twice the other, list every pair": s-m2 (12 stickers on two pages, 4 and 8), s-m3 (friend wrote 8 and 10 for 18 shells; right answer 6 and 12), G1 (15 shells in two jars, 5 and 10, table with "Twice the red"), G3 model answer (6 cakes, 2 and 4), online c2 (jars 9 to 21, twice as many), beyond text, scripts, notes, keys. Hand-solved, verify oracles rewritten (`l40_checks.py`). Also fixed a stale `tutor_prep` answer line (it said G1 5 and 7, G2 2 and 3 and 7; now G1 5 and 10, G2 No, 3, 8 and 12). |
| M5 home-pack question text | Closed | All 40 sheets now print question text at 12.5 pt or more (31 sheets 12.5, 9 sheets 13.1; measured on the book PDFs). Home levels t2/t3 no longer shrink the type, new level t4 compresses spacing instead; intro sentence shortened. Home intro paragraph is still small (8.1 to 10.2 pt on the crowded sheets; not enlarged). |
| M5 "After question N you may choose" line | Partly | 17.7 px (12.5 pt) on 29 pages, 11.7 on 3, 10.6 on 7 pages whose page 1 is squeezed (tight levels fall back to 15 px). Minimum now 10.6 pt (unchanged on those pages). |
| M5 tool-of-the-day box | Partly | Definition, "Also useful", "I used it" 11.3 pt on most lessons (was 9.9); 9.9 pt on the squeezed pages. Choose-one label 8.5 to 10.4. |
| M5 look-back box | Partly | Prompts 10.8 pt (was 8.5 to 9.4), yes / not yet 10.8, intro and footer 10.4. On 9 squeezed pages (Book 5 pp7, 15, 23, 39; Book 6 pp7, 37; Book 7 pp29, 37; Book 8 p37) it stays at the old sizes: prompts 9.0 to 9.4, footer labels and "pass" 8.0 to 8.5 pt. True minimum 8.0 pt. |
| M5 tool chips (Book 6 p33, Book 8 pp25, 33, 36) | Closed | Names 10.4 pt (was 9.6), wrapped on two or three lines inside their cells, checked on the pages. |
| M5 Quest page 1 | Not closed | Builder tries 17.7 / 16.8 / 16.0 px and keeps the largest that stays at 4 pages; page 1 is 99 % full on Books 2, 4, 6, 8, so none fits: instruction 11.6, intro box 12.4 unchanged (no overflow introduced). |
| Low L39 H5 = L13 H3 | Closed | L39 H5 is now "The moon is 6. The star is 2 more than the moon. What is the moon + the star?" (14), still a Picture Equations rewind. |
| Low L23 H4 = L29 H2 frame | Closed | L23 H4: Kumar reads 4:00 pm to 4:30 pm, Aisha reads for the same time from 6:00 pm, stops 6:30 pm. |
| Low L11 T1 and online t1 (total 10) | Closed | New structure and total: 11 children, Ravi 2nd from the back, 4 between Lily and Ravi, Lily is 5th from the front (Kumar says 6th); online t1 template n 10-13, b 2-4, c 2-4, oracle rewritten. |
| Low L21 G3 (b) options | Closed | Options with 5 or more words go on their own line (`yn long` in `b_print.py`). |
| Low online grammar | Closed | Runner filter `{x\|pl_noun}` (1 sticker, 2 stickers; child/children). Applied to L14 c5, L17 t1 and t2, L20 g3, L21 c3, L22 c2, L26 g1, L33 t3. |
| Low developer wording / "Lessons 1 and 9" | Closed | "Quest v2:" (L10), "the page generator draws only a few figure types" (L20) reworded; L30 strand "Choosing a tool" now maps to Term 3 Lesson 10. Keys re-read: no hits. |
| Low reason lines longer | Partly | A second writing line added at L17 T2 and L20 T1, T2. L6 T1 to T4 left at one line: a second line spills the page (builder rejected it). B2 p21 T1 already has two lines. |
| Low L23 G1 "straight after" | Not closed | Not in this task's list. |
| Low L36 E3 box touches look-back (Book 8 p7) | Not checked | Not in this task's list. |
| Lows L6 online pictures beyond 80 variants, B&W dither of Quest header bands, L10 H4 third copy, L12 five "move some" items | Not closed | Not in this task's list. |
| Pre-existing tight pages | Note | Squeezed pages keep older, smaller type; fixing them needs content cuts. |
