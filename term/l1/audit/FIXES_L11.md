# Fix pass, Lesson 11 (Term 2, 22 Oct 2026)

Sources: WORKBOOK_AUDIT_L11, GUIDE_DECK_AUDIT_L11, HOME_PARENT_PRACTICE_AUDIT_L11. Validator 0 FAIL; 86 answer checks; workbook 6 pages, fills 99/99/98/93/98%, home 2 pages, parent 1 page; timing 90.

## Workbook audit
| # | Action |
|---|---|
| 1 G1 "between" | Now "next to Ali and next to Mei" and "next to Ben and next to Ali"; mistakes, hint, checks updated |
| 2 Investigation room | `draw: true` (box plus lines); "Line 4:" removed (11) |
| 3 S2 small boxes | Line of 7 (was 8): boxes larger; S1 shrunk to 90% to keep page 1 whole. Boxes are still about 8 mm: template needs a box size option |
| 4 number cards unused | Used in Explore round 2 (number card 6 vs place cards; "4th card, how many in the row"); script, slide, verify updated |
| 5 round table | Labels are seat numbers only (names are in the stem), so nothing is clipped. Table still 175 px wide: template CSS |
| 6 FRONT runs into name | First child renamed Ali (S1, warm-up slide, script) |
| 7 "behind" | S1 statement 3 is "Lily is at the back." |
| 8 T2 labels | Place labels removed; names only |
| 9 G2, G3 drawing | Drawing boxes added |
| 10 timing claim | Notes say Think harder is for early finishers and home |
| 12 S3/T1 | Blanks in both parts of S3; T1(b) spacing fine |
| 13, 14 look-back boxes, footer 5.8 mm | Template (not edited) |

## Guide and deck audit
| # | Action |
|---|---|
| 1 answers on slides | Reveal blocks: Explore 2 cards, m6, m7 (answer slides added); m2 split into question and check slide; m3 caption no longer gives the count; Explore 3 picture has no place labels |
| 2 gallery look-around | Fingers after each call; notes say the gallery shows faces and fingers only |
| 3 mic contradiction | One routine: mic off; "on three" is said quietly to your own room; to share, unmute then mute |
| 4 timing | Dropped "after 9" question and the take-away-three step; Explore 13, Mini 11; slow class 85:10; note says the buffer is used at 30 s per question |
| 5 public finger count | Removed; note says nobody shows scores |
| 6 previews cost time | Kept (T1, T2 need them for tier honesty) but each is a question then a reveal; tutor told to just say answers if late |
| 7 L10 hand-off | NOT fixed here (another agent owns `l10.json`). The Lesson 10 goodbye (script, last segment) and its `parent.next_materials` still list the OLD materials, "about ten counters, a pencil and paper". Lesson 11 needs: ten small things of any kind for a row, a coin or button, a paper to write FRONT on, the printed Lesson 11 workbook with its kit page (place and number cards) cut out by a grown-up (no printer: twenty paper scraps, 1st to 10th and 1 to 10), a pencil and paper. L11 tutor_prep already says tell parents a week before |
| 8 FRONT/name | As workbook 6 |
| 9, 10 thumbnails, m1 colours | Template (not edited) |
| 11 break line | "The last move was the fifth. What was it? Jump once." |
| 12, 13 | Investigation text; term line now "Over this term ..." |
| 14 catch-up L12 | Instruction removed |
| 15 tutor load | Added to tutor_prep and NOTE |

## Home, parent, online
| # | Action |
|---|---|
| 1 link | Parent "next": tutor sends the practice link on lesson day (no URL on printed pages) |
| 2 t3 ordered | Question says "smallest first"; runner refusal text still says "blank": template |
| 3 answers on back of sheet | Template (home_html) |
| 4 recording sentence | "private to the families in your child's group" |
| 5 H4/H5 drawing room | Template (home sheet has fixed lines) |
| 6 steps | t1, g1, g2, t2, c4 steps use derived numbers |
| 7 pictures | c4 and t2 now draw the line (t2 rings both children) |
| 8 aria label | Not changed (template) |
| 9 "type 3" | c1, c4 ask "Type the place, like 3rd." |
| 10 H1, H2 | Reworded; title "Who Is Where?: practice at home" is template |
| 11 footer | Template |

## Template or other-lesson needs
line_up/box size option; round_table width CSS; look-back box size; footer margin; home sheet drawing box and answers on a separate sheet; home title format; runner ordered-list message; aria label of figures; Lesson 10 hand-off materials.

## Cut-out audit follow-up (23 Oct 2026, lesson-level rows of CUTOUT_AUDIT.md)
| Row | Action |
|---|---|
| F13 / hand-off L11 -> L12 | `parent.next_materials`, the spoken goodbye and the s-end slide now say: the strips page is cut into 11 strips and two are cut after 6 cells before the lesson; nobody cuts during the lesson; counters dropped (Lesson 12 no longer uses them) |
| F16 line of 13 | G2 is drawn only: hint and kit intro say the cards stop at 10th. Card size (28 x 19 mm) is a kit-tool matter (not edited) |
| T10 no printer | materials and tutor_prep: write 1st to 10th and 1 to 10 on twenty paper scraps |
| T7 / F11 | The standard kit note (batch 5) now carries the grown-up cuts and envelope lines; tutor_prep says print the kit page on its own sheet |
| F21 L10 -> L11 hand-off | Not in this file: `l10.json` (see row 7 above) |
Rebuilt: validator 0 FAIL, workbook 6 pages (fills 99/99/98/93/98%), parent 1 page 96%.
