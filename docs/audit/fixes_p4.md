# Fixes applied for the P4 audit (docs/audit/audit_p4.md)

Nothing was published and nothing was committed. Shared files (rebuild/slidekit.py, hp/*, levels/*) were NOT edited. Only p4 content, p4 builders and the p4 generators were changed.

Final workbook: `p4/Math_Inquirers_P4_Student_Workbook_Designed.pdf` is 47 pages (was 51). Lesson 7 core = 2 pages (pp. 27-28, was 4), Lesson 8 core = 2 pages (pp. 31-32, was 4), every other lesson still 2 core pages + 2 Think Harder pages. Page counts confirmed from the rendered PDF.

## Status per issue

| # | Status | What was done |
|---|---|---|
| 1 | Applied (adapted) | L7 and L8 now print on 2 pages each. The audit's size cuts alone were not enough (measured: page 1 still 125 css px too long), so in addition to the listed shrinks the figure and the question parts are set side by side for L7 Q1, Q4, Q6 and L8 Q2 (new `side()` helper inside l7.js / l8.js, no shared CSS changed). L7: q1Svg c 20 to 16 with tight viewBox (and the two "? cm" labels no longer collide), table rows h 60 to 44, blankGrid 4 rows to 3, Q1b answer lines merged, q6Svg c 14 to 12, Q6c blank line removed, Q2/Q3 wording shortened. L8: q1Svg ph 96 to 84, q2Svg c 44 to 36, q6Grid c 30 to 26, plus dice nets c 36 to 30, q4 c 22 to 20, q5 c 30 to 26, the Q4 instruction moved inside the Q4 box, Q6 stem shortened. The fallback "move Q3 to page 2 / Q6 to Think Harder" was NOT needed (it would not have fitted anyway). |
| 2 | Applied | New 90-minute clock in all 10 decks: warm-up 0-5, quick questions 5-8, explore 8-13 + 13-18 (both slides kept, time budget merged), teaching 18-30 (key slide 29-30), brain break 30-34, page 1 34-50, check 50-53, page-2 pre-teach 53-58, page 2 58-76, check 76-80, talk 80-85, exit 85-90 (L10: exit 85-88, end slide 88-90). Slide pill labels and the "Minutes a to b" start of every slide note were rewritten, title-slide "Time plan" notes rewritten (also says Challenge/Think Harder are early-finisher and take-home, and the 2-minute breakout-room transition), Challenge/stretch slides labelled "Early finishers / take-home", brain-break notes say four minutes. Challenge and Talk no longer overlap. L6 teachfan (before page 1) is 34-36 and its page 1 is 36-50. Not done: the teaching block was not cut to 4 slides; instead every "Your turn" slide is labelled "OPTIONAL" and the block is time-boxed (12 min). Pre-teach blocks still have 3 to 5 slides in 5 minutes (the "your turn" ones optional). Also updated p4/guide.js (routine table and minute-by-minute headings) and p4/workbook_html.js (Think Harder page now says "Do these when you finish early, or take them home"). |
| 3 | Applied | L6. A: Q3d deleted (it is stretch item 3), Q6b moved to Think Harder stretch 4 (verified: exactly 2 pairs); key, ws2 and ws2-answer slides updated; teachclock slide marks the minute-hand idea "Think Harder". B: Q5 figure displayed about 30 percent larger, "a" and "58 degrees" moved off the line, angle c arc enlarged with the label outside the overlap; stem now says the overlap is 30 degrees and c is the whole angle covered by both squares (key 150 unchanged). C: challenge item 9 rewritten as in the audit, answer 20 unchanged, with a new small figure (`overlapFig`, an optional `fig` field in qbank items that p4/workbook_html.js prints on the Think Harder page). |
| 4 | Applied | L1 Q2 stem now says 2 rows of 20 and 20 rows of 2 are different ways to plant; ws1 slide note updated. |
| 5 | Applied | L1 exit ticket (lesson.exit and exit slide + notes): factors of 28 and smallest common multiple of 6 and 9 (18). L1 stretch 1: factors of 72 (12 factors). L10 exit ticket (data, slide, notes): 12 heads and 34 legs, 5 goats. |
| 6 | Applied | L1 Q5c hint added. L2 Q4a simplified (answer 47 621, unique) and Q2b starred with a "(A star means a bit harder)" note; ws2-answer note updated. L3 Q5b replaced by a fill-in scaffold (number, 7, 7); the open "explain why" is now Think Harder stretch 4; key and ws2-answer slide updated. L4 Q7 moved to Think Harder stretch 4, workbook page 2 is Q4-Q6, key/deck/slides updated. L5 Q7 starred. |
| 7 | Applied | L9 juiceSvg `step: 10` to `step: 5` (labels still every 10). |
| 8 | Applied | Swaps: L2 [0]<->[4], L3 [0]<->[4], L4 [0]<->[6], L5 [0]<->[5], L9 [0]<->[6], L8 challenge [8]<->[4]. (L3, L4, L6 additionally insert the moved item as printed stretch 4, pushing the old item 4 to the end of the bank.) |
| 9 | Applied | L5 core item 4 is now "Round 7.46 to 1 decimal place" (7.5). |
| 10 | Applied | L4: `p4l4-teachcompare` split into two slides (tools 1+2; new `p4l4-teachcompare2` with tool 3 and a "which tool?" card); `p4l4-teachfind` keeps only the find-ALL example (full width), "Who am I?" moved to Think Harder with Q7. Neither slide is over 74 elements any more. |
| 11 | Applied | L8 key Q4 rewritten as in the audit. |
| 12 | Applied | L8 Q5 answer line uses unlabelled "(a) ___ (b) ___ (c) ___ (d) ___"; the lone "c" under Q3 removed (unlabelled sentence "In net (b) ..."). |
| 13 | Applied | L1 Q1a "every box". |
| 14 | Skipped | Audit recommends leaving as is (10 and 15 are 2-digit). |
| 15 | Applied | L1 challenge[5] rewritten ("exactly 4 factors and is odd"; same answers). |
| 16 | Applied | L2 `p4l2-we1` notes explain the approximately-equal sign. |
| 17 | Applied | Comments in p4/data.js and p4/workbook_html.js now say p4. |
| 18 | Skipped | Informational (coverage gaps for the parent pitch); no content change. Also skipped: the 2.4 "materials to prepare per lesson" note. Applied from 2.4: L6 Q1 ruler sentence, L6 warm-up mirror/clockwise note, L10 Q1a "consecutive numbers (next-door numbers)", breakout transition in every title-slide note. |

## Numeric re-verification (Python, `scratchpad/verify_p4fix.py`, all assertions pass)
28 has 6 factors listed correctly and lcm(6,9)=18; 72 has the 12 listed factors; odd numbers 20 to 40 with exactly 4 factors are 21, 27, 33, 35, 39; 40 trees in rows (at least 2 by 2) = 6 ways; L2 Q4a (new wording) has the unique answer 47 621; 55 555 is the only same-digit number rounding to 60 000; number trick always 7 (blanks: number, 7, 7); 2 340 / 5 = 468; L4 Q7 unique 17/6 and 7/4 > 1 5/8; 7.46 to 1 d.p. = 7.5; digits for 3.[ ]5 < 3.42 are 0 to 3; L6 150 and 20 degrees, and the N-to-W robot pairs are exactly (45 cw, 135 acw) and (90 cw, 180); 4A/4B girls both 34; 12 heads 34 legs = 5 goats; L7 area 48 unchanged.

## Files changed
- Content: p4/content/l1.js, l2.js, l3.js, l4.js, l5.js, l6.js, l7.js, l8.js, l9.js, l10.js
- Builders: p4/workbook_html.js (Think Harder wording, optional `fig`), p4/guide.js (clock), p4/data.js (comment)
- Generators: rebuild/gen_p4l1.py to gen_p4l10.py (clock, labels, notes, slides listed above)
- Generated and rebuilt: split/p4l1 to split/p4l10 (all 10 decks regenerated, then `python3 levels/restyle.py split/p4lN` on each); `bash levels/build_level.sh 4` run last (workbook, tutor guide docx/pdf, weekly dose, weekly PDFs zip, parent pack, scheme).

## Regenerated deck keys
p4l1, p4l2, p4l3, p4l4 (28 slides, +1), p4l5, p4l6, p4l7, p4l8, p4l9, p4l10. Slide checker (no font under 24 px, at most 200 elements, notes under 4000 chars): no new findings; the remaining flags on title/break backgrounds and the L8 we1/we2 and L9 graph slides existed before.
