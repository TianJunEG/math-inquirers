# Audit fixes: finding -> action (school/p1, 23 Oct 2026)

Source: `AUDIT.md` (28 findings). Owner instruction of 23 Oct: colour-by-code pages replace the weak mark-by-answer pages P1-12 and P1-14. "Fixed" means rebuilt, validated (322 checks, 0 failed) and the page viewed.

## New page set
P1-01, P1-12 and P1-14 are now colour-by-code pages (CBC, pupils colour the printed outline with their own crayons): Rocket (place value, 1 star), House (corners of shapes, 1 star), Ice Cream (counting in 2s, 5s, 10s, 2 stars). Generator and banks copied unchanged from `school/colour_by_code` (commit ebff080) into `cbc_vendor/`; the old P1-01 rods page, the two mark-by-answer pages and their code were removed. Tiers stay 10 and 10.

## High
| Finding | Action |
|---|---|
| F1 P1-04 and P1-16 check passes 120/120 | Letter on every number or price; the letters read in order must spell HOUSE (P1-04) or BASKET (P1-16, with a total letter from a code table). 119/119 wrong arrangements rejected. Enumerated in `validate.py`. |
| F2 P1-12 and P1-14 slip detection 72 to 76% | Pages replaced by colour-by-code: every wrong value is rejected by the key or the colour tally (150/150, 204/204, 1200/1200). |
| F3 P1-14 used the division sign | Page replaced; validate.py fails on the sign in any printed text. |
| F4 P1-20 circular check | The total (24) is no longer a clue; three difference clues fix every row; the total is only the check. |
| F5 no logic-grid how-to | P1-04 and P1-16 carry a printed cross-and-tick example box. |

## Medium
| Finding | Action |
|---|---|
| F6 tier labels | P1-06 is now the two-star shape-riddle page; P1-07 two stars; P1-19 one star; stars rule in teacher notes. |
| F7 key errors ($5 vs $2, decoy lists) | Decoy numbers generated from page data; validate.py checks every number of 11 or more in a note exists on the page or in its answers. |
| F8 P1-01 rods | Page replaced by the Rocket colour-by-code page. |
| F9 P1-03 labels | Rows labelled number / letter and aligned. |
| F10 strand balance | Shapes 1 to 3 pages, multiplication-share page removed, add/subtract 5 to 4; mix listed in README. Multiplication is now 1 page (open question 8). |
| F11 "80c" | Key uses 80¢; validate.py fails on `\d+c`. |
| F12 P1-02 layout | Clues kept on one line. |
| F13 P1-09 words and boxes | "across" / "down" wording; boxes at least 12 mm (checked). |
| F14 P1-06 | Page replaced (shape riddles); START and FINISH labels on P1-08 inside the box. |
| F15 P1-13 labels | Boxes labelled bags, dots, total. |
| F16 P1-17 | Labels moved off the border, ticks lightened, "print at 100%" in notes. |
| F17 P1-18 | Hands never closer than 25 degrees; "What is the time 1 hour later?" wording; two-step noted. |
| F18 key thumbnails | Small solved picture on each entry; entries packed; full answer page for each colour-by-code page. |
| F19 teacher notes | Time per page, when to use, what to do if a check fails, star rule, photocopying added. |

## Low
| Finding | Action |
|---|---|
| F20 wording | "Find the value of", "Arrange..." frames; hints reworded. |
| F21 P1-07 empty half | Layout rebalanced. |
| F22 workload | 36-sum page gone; colour pages take longer (stated in the teacher notes). |
| F23 licence line | Left as placeholders (open questions 2, 9); blank school field in the master, `--school` fills it. |
| F24 alignment wording | Key keeps plain syllabus-edition reference only; no claim on pupil pages (validate.py). |
| F25 maze check | P1-08 check counts the boxes (10) and every box must make 12; 240/240 rejected. |
| F26 key jargon | K-codes and "tri/pent" removed from the key. |
| F27 odd prices | P1-16 prices changed (pen $12, book $15, ball $5, kite $8, cup $7). |
| F28 unverified outcome numbers | Checked against the P1 ranges of `docs/moe/syllabus_by_level.md` by validate.py; still to be checked against the syllabus PDF (open). |

## Left open
Pupil trial, real photocopier test with crayons, V9 non-copy comparison, larger word list, cover/licence/teacher-note wording (placeholders kept), and multiplication at one page.
