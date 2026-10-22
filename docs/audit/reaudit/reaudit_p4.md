# Math Inquirers P4 (ages 9-11): RE-AUDIT after the fix passes

Repo read-only; nothing written there. Sources: p4/content/l1..l10.js, p4/workbook_html.js, built workbook PDF (64 pages), decks split/p4l1..p4l10 (slides + notes). Working tree appeared stable (no file changed mid-read).
Baselines: audit_p4.md (53e1fd1), gifted_p4.md (after-fix column), journey_p4.md.

## 1. Content audit (same method: every answer recomputed)

### 1.1 Answer check
Python brute force (verify.py, scratchpad) plus hand recomputation of every key, question bank, gaps (check, invest, reflect, go2, cap), exit ticket and slide stretch/challenge answer for L1-L10. No wrong numeric answer in the workbook, the bank or the sneak-peek puzzles. L10 confirmed by code: 14x15=210, 18x19=342, 19x20=380, 23x24=552; $4/$7 for $50 gives only (9,2) and (2,6); 7 goats; 11 cars; 4 spiders, 65 legs impossible; 14 chickens and 6 goats; 32 stickers; Ben 10; Mei 12; 18 in queue; ring toss impossible 1, 2, 4, 7; 19 numbers with a 7; 91 and 63 riddles; 1?2?3?4?5?6=7 has exactly two sign sets.
One WRONG number found, in a teacher note (below, N1).

### 1.2 Verdict on the 18 baseline findings
| # | Finding | Verdict |
|---|---|---|
| 1 | L7/L8 workbook ran to 4 pages (Q3, Q6 stranded) | FIXED (2 core pages + Investigation + Think harder + Go further) |
| 2 | L6 clock / Q5c diagram unclear | FIXED |
| 3 | L6 page 2 packs 10 sub-parts | PARTLY: solo cap line added ("aim for ..."), still 10 sub-parts |
| 4-8 | L1-L5 Core items at Think-harder level, Q5b trick explain, L4 page 2 overload etc. | FIXED (4,5,6,7,8 reworded or moved to Think harder/Go further) |
| 9 | L5 2 d.p. rounding probably P5 | PARTLY: out of core, still in optional slide `try2` and Go further items |
| 10-13 | L8 Q4 key text, L8 easy last item, L9 gridline mismatch, L10 grid easy | FIXED |
| 14 | L1 Q4 with 10 and 15 | NOT FIXED (intentional, unchanged) |
| 15, 16 | Misc. slide/workbook mismatches | FIXED |
| 17 | p2 comments in code | FIXED (no p2 references remain) |
| 18 | Informational | unchanged |
Count before: 13 not-ok items open in baseline text (18 issues; 2 lessons OK, 7 minor fix, 1 rework). After: fixed 14, partly 2, not fixed 1, informational 1. Lesson verdicts after: OK 3 (L7, L8, L10), minor fix 7 (L1-L6, L9), rework 0.

### 1.3 New problems introduced by the fix passes (exact location, fix)
- N1 (WRONG VALUE, L2 slide `stretch` notes): "best above 60 000 is 61 357". 6 is not among cards 1,3,5,7,9. Correct: 71 359 (11 359 above 60 000) vs 59 731 (269 below). Answer 59 731 itself is right. Fix: edit note.
- N2 Label drift: challenge-slide notes in L1, L2, L3, L4, L7, L9 (and L10) say "These are Think harder Qx and Qy" but the printed page is "Go further". Fix: replace with "Go further".
- N3 Duplicate Go further in explore slide notes: L4, L6, L7, L8, L9 hold the old Go further text and the new "GO FURTHER (on the slide from minute 8 ...)". Tutor sees two different questions. Fix: delete the old sentence.
- N4 L6 and L9: page 1 and `ws1` slide print "After question 3 you may choose" but page 1 has only Q1-Q2 (L6 p31ff, L9 p48ff). Fix: "After question 2". L10 checked: correct (Q1-Q3).
- N5 Page spill: L1 Q6 alone on p5, L2 Q3 alone on p10, L6 Q2 on p31. Slides still say "Page 1/Page 2" and the footer prints workbook page numbers (53, 54...). Fix: shrink spacing, or say "Page 1" by lesson not footer; add a pagination test to build.
- N6 Sneak-peek camera rule: "hold it to the camera ... only your tutor looks" cannot be enforced in a group call; notes contradict (everyone at the same moment vs tutor only). Fix: ask children to show it privately by raising a hand, tutor says "peek", children show via chat-free hold-up to the tutor only is impossible; use "write it, keep it, I will ask who wants to share" and drop the hold-up. Safeguarding-consistent (no private messages to children).
- N7 L3 Q5 and Q7 rely on slides marked OPTIONAL (`trytrick`, `teachchain`); a tutor that skips them leaves the worksheet untaught. Fix: unmark or move content to the mini-lesson.
- N8 L5 warm-up note: "one short round, about 2 minutes" but "Play 3 rounds". Fix: one number.
- N9 Investigation headings: double full stop "?." and "!." on L7 p38 and L9 p48. L9 Investigation (b) overlaps Go further Q7. Fix punctuation; swap L9 invest (b).
- N10 Teach-before-page-2 block still dense in L4, L5, L7 (3 ideas in 5 minutes). L6 `teachclock` still teaches 6 degrees per minute (clock, beyond P4 core).
- N11 L10 notes: timeline says end slide "Minutes 88 to 90" but slide label 89-90; reflect 87-89, exit 85-87 consistent otherwise. L10 challenge note says "Think harder Q5 and Q6" (Go further).
- N12 Marketing wording in levels/mkextras.py still says "inspired by research-based approaches used in gifted education" (line 113), flagged earlier; not changed. Keep or soften deliberately.

## 2. Gifted-style rubric (12 criteria, 0/1/2, max 24)
What changed in the fix pass and how it moves the rubric:
- C10 Metacognition: Looking back reflection (did well / hardest / what helped / still stuck / pass) in every lesson: 1 to 2.
- C9 Creativity/problem posing: Investigation page with find-all and "what if" variants (L10 also Q7 make your own puzzle): 1 to 2 where the Investigation has a change-the-condition part (L1-L5, L7, L8, L10). L6 (partition find-all, no what-if) and L9 (invest overlaps Go further Q7) stay 1.
- C11 Pacing flexibility: working "choose" line after the page-1 core plus Think harder/Go further/Investigation: 1 to 2 where the line is correct (L1-L5, L7, L8, L10). L6 and L9 stay 1 (N4).
- No change: C2 depth over speed (fixed clock, pages still 2 core + 5 to 7 items), C7 student-led (teach block still tutor-led). No criterion dropped.
| Lesson | Before (post-gifted-rework) | After | Delta |
|---|---|---|---|
| L1 Factor Hunters | 16 | 19 | +3 improved |
| L2 Big Number Puzzles | 14 | 17 | +3 |
| L3 Operation Detectives | 14 | 17 | +3 |
| L4 Fraction Frontier | 14 | 17 | +3 |
| L5 Decimal Detectives | 13 | 16 | +3 |
| L6 Angle Turns | 12 | 13 | +1 |
| L7 Area Architects II | 17 | 20 | +3 (top band) |
| L8 Symmetry and Nets | 15 | 18 | +3 |
| L9 Data Detectives | 14 | 15 | +1 |
| L10 Challenge Day | 16 | 18 | +2 |
Mean 14.5 to 17.0 (range 12-17 to 13-20). Bands: only L7 reaches 20-24; nine lessons 12-19. Level remains "enrichment with depth features", not fully gifted-style: C2, C7 and C5 (one taught path) are still 1. Caveat: C9 and C11 gains were scored from the printed Investigation and choose line; they depend on tutors actually using them (nothing forces it).
Remaining gaps: C7 (teach block tutor-led), C2 (fixed clock), C5 (L1-L9 teach one method; only L10 names several), C8 thin real-world coating.

## 3. Student journey (Part 1 method; 1-5; difficulty fit 5 = just right)
Per-lesson mean of the six scores, before to after.
| Lesson | LOW | MIDDLE | HIGH |
|---|---|---|---|
| L1 | 2.83 to 3.50 (+0.67) | 3.83 to 4.00 (+0.17) | 3.83 to 4.17 (+0.33) |
| L2 | 2.50 to 3.17 (+0.67) | 3.67 to 3.83 (+0.17) | 3.83 to 4.17 (+0.33) |
| L3 | 2.17 to 3.00 (+0.83) | 3.50 to 3.67 (+0.17) | 4.00 to 4.33 (+0.33) |
| L4 | 3.00 to 3.50 (+0.50) | 3.67 to 3.83 (+0.17) | 3.67 to 4.00 (+0.33) |
| L5 | 2.17 to 3.00 (+0.83) | 3.33 to 3.50 (+0.17) | 3.83 to 4.17 (+0.33) |
| L6 | 3.50 to 3.67 (+0.17) | 4.00 to 4.00 (0) | 3.33 to 3.50 (+0.17) |
| L7 | 3.17 to 3.50 (+0.33) | 3.83 to 4.00 (+0.17) | 3.83 to 4.17 (+0.33) |
| L8 | 4.00 to 4.17 (+0.17) | 4.17 to 4.33 (+0.17) | 4.00 to 4.33 (+0.33) |
| L9 | 3.33 to 3.50 (+0.17) | 3.67 to 3.83 (+0.17) | 3.00 to 3.17 (+0.17) |
| L10 | 3.00 to 3.50 (+0.50) | 4.00 to 4.17 (+0.17) | 4.67 to 4.67 (0) |
| Level mean | 2.97 to 3.45 (+0.48) | 3.77 to 3.92 (+0.15) | 3.80 to 4.07 (+0.27) |
Dropped: none at lesson level. Same: L6 MIDDLE, L10 HIGH (ceiling).
Why scores moved (criterion level): sneak-peek puzzles removed the cold check: LOW participate +1 and confidence +1 in L1, L2, L3, L5 (the weakest baseline lessons). Looking back with "pass" allowed: motivation +0.5 across personas. Investigation and Go further: HIGH motivation +1, fit +0.5 (the baseline "starts at min 34" complaint is eased, HIGH can pick Investigation at minute 34 under the choose line, but only after Q3). Offsets: LOW social/online -0.5 where the hold-up-to-camera rule exposes a wrong or blank slip (N6); LOW difficulty fit unmoved in L3, L5, L6.
Newly introduced problems for children: N6 (public camera hold-up), N4 (instruction points to a question that does not exist, LOW/MIDDLE confused), N5 (one lone question on its own page looks like an afterthought, also feels like missing homework), Looking back asks writing from LOW children who finished late (88-90 min, after 3 pages), reflection time can be crowded out (L10 only 2 min and certificates after).
Five weakest cells (persona, lesson, criterion) with fix:
1. LOW, L5, difficulty fit 2: decimals plus 2 d.p. rounding in Go further/optional; move rounding to Go further only, give a 10-square grid on the page.
2. LOW, L3, participate/difficulty 2-3: Q5 trick and Q7 chain depend on OPTIONAL slides (N7); promote slides, cut one question type from page 2.
3. LOW, L6, difficulty fit 2-3: page 2 has 10 sub-parts and 6 degrees per minute; cut to 6 sub-parts, drop the clock formula.
4. HIGH, L9, motivation 3: Investigation (b) duplicates Go further Q7 and the page is data-reading only; replace with a "design a survey that tricks the reader" task.
5. LOW, L2, social/online 2-3: five-digit rounding plus a hold-up-to-camera slip (N6) plus Q3 alone on p10 (N5); remove hold-up and fix spill.
Three strongest cells: HIGH L10 motivation 5 (ring-toss Investigation with find-all plus "make your own puzzle with one answer" Q7); LOW L8 participate/fun 5 (nets and folding are hands-on, low floor, now with the safe sneak-peek); MIDDLE L8 confidence 4-5 (worked examples plus a clean two-page core).
Level-wide patterns: (a) fix passes helped LOW most (+0.48) because the cold check was the worst moment; (b) HIGH children still wait until minute 34 or after Q3 to reach the best material, so L9 and L6 stay lowest; (c) the numerals-heavy lessons (L3, L5, L6) are still hardest for LOW; (d) tutor-notes consistency (N2, N3, N4) is now the main risk to delivery, not the content.

## 4. Priority fix list
1. N1 (wrong value in L2 note) and N4 (label "After question 3" in L6, L9).
2. N6 remove the camera hold-up; use "write it, keep it, volunteers share" (safeguarding-aligned).
3. N5 pagination, N2/N3 notes cleanup, N7 L3 optional slides, N8 L5 rounds.
4. L6 page 2 and L5 rounding (LOW weakest cells).
5. L9 Investigation (b).

## 10-line summary
1. Audit-1 baseline: 2 lessons OK, 7 minor fix, 1 rework; 18 issues. After: 3 OK (L7, L8, L10), 7 minor fix, 0 rework.
2. Issue verdicts: fixed 14, partly fixed 2 (#3, #9), not fixed 1 (#14), informational 1 (#18).
3. New problems found: 12 (one wrong value: L2 stretch note 61 357 should be 71 359; no wrong workbook answers).
4. Biggest new risks: "After question 3" in L6/L9, Go further label drift in notes, camera hold-up rule.
5. Gifted mean: 14.5 to 17.0 of 24 (L7 20, L1 19; L6 13 lowest); no lesson dropped.
6. Gifted gains came from C10 reflection (+1), C9 Investigation (+1), C11 choose line (+1); C2, C5, C7 unchanged at 1.
7. Journey LOW: 2.97 to 3.45 (+0.48); biggest gains L3 and L5 (+0.83).
8. Journey MIDDLE: 3.77 to 3.92 (+0.15).
9. Journey HIGH: 3.80 to 4.07 (+0.27); L9 HIGH still lowest at 3.17.
10. Weakest cells: LOW L5, L3, L6, L2 and HIGH L9; strongest: HIGH L10 motivation, LOW L8, MIDDLE L8.
