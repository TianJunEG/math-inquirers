# Fixes after the Books 5-8 round 3 audit (24 Oct 2026)

Source: `AUDIT_BOOKS_5_8_ROUND3.md` (no High). Lessons 21-40 rebuilt (colour, B&W, keys, home packs), `validate.py` 0 FAIL on all 40 lessons, `check_bw.py` ok on all 24 term B&W files. Page counts unchanged: workbooks 42/44/48/42, keys 22/32/22/32, home 12/14/12/14, all even; contents numbers match the first page of each lesson.

| Finding | Status | What was done |
|---|---|---|
| M1 "In my head" in Book 6 and Book 8 key p24 | CLOSED | Fixed in `b_quest.py` (shared with Books 2 and 4). 0 matches in all 8 keys. |
| M2 absolute lesson numbers in the keys' group-advice and parent-line tables (pp30-31) | CLOSED | `b_quest.lesson_range()`: "Term 3 Lessons 1, 2, 3 and 7", "Term 3 Lessons 4 to 6", "Term 3 Lesson 8" and so on, term-local in every Quest tutor note (Books 2, 4, 6, 8). Non-consecutive lessons are listed, no longer shown as a false range. Books 1-4 keys checked: only "Lesson 10" of the lesson being described remains (term-local). |
| M3 text size (exit stems, True/False tables) | CLOSED, minima stated | Same treatment as Books 1-4: exit stems 12.5 pt (was 12.0), True/False cells 12.5 pt (was 11.3), instruction lines 12.5 to 13.1 pt (was 11.0). Remaining below 12.5 pt: text inside SVG tables and graphs, 10.7 to 11.3 pt (for example "Job, Starts, Lasts, Ends" 11.3, graph labels 10.7-11.8, "Statement" gone); the L30, L39 and L40 tool chips are 9.6 pt (7 and 8 names have to wrap); Quest tool rows 7.9 pt (Book 6, page 1 is full) and 8.9 pt (Book 8, raised from 7.9 as far as four pages allow); Quest page 1 instruction 11.6. |
| M4 small clocks | PARTLY CLOSED | Draw clocks enlarged: L21 E2 (58 to 100) and Start here S2 (70 to 90), L22 E3 (58 to 100) and S3 (62 to 95), L22 S2 80, L30 S1 55 to 80, L21 E1 70 and L22 E1 70 (read-only). The draw clocks in E2 (Book 5 p7) and E3 (p15) are now about 31 mm across in the book (were 22 to 25 mm), not 35 to 40 mm: the page also carries the Investigation lines and the look-back box and has no more room (the fit loop would shrink figures). L23 E3 is now three small clocks (see M8). Home clocks (26 mm) not changed. |
| M5 Book 7 write and draw space | CLOSED | `draw_h` keeps a drawing box at a fixed height on every tightening level: L32 G3 135 px (about 36 mm, was 15 mm), L35 G3 95 px (about 25 mm, was 12 mm). L33 T1 (a) and T2 (a): three route blanks of 40 mm each on their own line (were 17 to 22 mm). |
| M6 L28 S2 and S3 "The last column is spare" | CLOSED | "You may use the last column." |
| M7 L21 G2 and G3 (b) give away (a) | CLOSED | G2 (b): "The time is ___ ." (6:20). G3 (b): "At half past 5, where is the short hand? Circle one: on the 5 / between the 5 and the 6 / on the 6." Verify checks and keys updated. |
| M8 similarity, NEW story AND NEW frame (hand-solved, keys, oracles in `verify/`, online twins where one existed) | CLOSED | |
| L40 G2 | CLOSED | "A pattern starts at 4 and goes up by 4. The numbers are 4, 7, 10, 13. Is the puzzle right?" No; goes up by 3; a pattern up by 4 is 4, 8, 12. Online twin t2 replaced. |
| L40 home H2 | CLOSED | "My number is between 20 and 30. My ones digit is 3 more than my tens digit." 25 (unique). |
| L36 T3 | CLOSED | Dominoes on a 2 by 3 board: 4 lie along a row, 3 stand up, 7 places (brute-force oracle). Tutor-prep answer line updated. |
| L36 E2 | CLOSED | "3 bridges and 3 buses, each box is one way home": 9 ways (table 3 by 3, bridge rows, bus columns). |
| L39 T3 | CLOSED | "Mei is on stair 7. Ali is 2 stairs below. Ben is 1 stair below Ali." Ali 5, Ben 4 (draw box kept). |
| L23 G1 | CLOSED | Morning plan: story half an hour, then PE 1 hour, PE ends 10:45 am, Siti says story time started 9:45 am: No; PE 9:45 am; story 9:15 am. |
| L23 E3 | CLOSED | "The class ends at 5 o'clock. It lasted half an hour. Which clock shows when it started?" three clocks A 4:30, B 5:30, C 4:00: A. |
| L23 H4 | CLOSED | Bus to the zoo arrived 10:30 am, trip half an hour, Ali says it left at 11:00 am: No; 10:00 am. |
| L1 L28 key T3 stale "16" | CLOSED | "Choosing 5 because 17 is the number that comes after the wrong one." |
| L2 L34 G2 key cube position | CLOSED | "the bottom cube of the tall stack at the back on the left, behind the cubes in front of it" (answer 1 unchanged). |
| L3 L40 Quest gate 3 cue | CLOSED | "Some cubes may be hidden." in the printed text and in the spoken line. |
| L4 Book 6 Quest gate 3 tags | CLOSED | The three tags ($4, $5, $6) are now named inside part (c) itself. |
| L9 duplicate home item L33 H5 and L39 H5 | CLOSED | L39 H5 is now the Term 2 Lesson 3 item "The heart is 4. What is heart + heart + heart?" (12); L33 H5 keeps the cup item. |

## Not closed
- Chip names on L30, L39 and L40 are 9.6 pt and the Quest tool rows 7.9 pt (Book 6) and 8.9 pt (Book 8), see M3. Audit Lows L8 (home sheets repeat the hand positions in words), L10 to L13 (round 1 and 2 Lows, small figures, hard words, the unasked 10:15 box on the L23 G1 time line) were not in the coordinator's list and are unchanged.
- Online practice twins that were not flagged still use the old frames: L23 online g1/t3 (backwards from an end time), L36 online c5, L40 online g1/g2 (add up to N, N more than the other).
- Owner call remains for the stock "Some are 5-cent coins and some are 10-cent coins" family (sub-7-word runs).
- No printed proof (stipple fills, 1-bit legibility, 6 to 10 pt chip names).
