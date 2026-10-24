# Round 2 audit: Level 2 Extension Workbook (self-study, with answers)

Audited 23 Oct 2026 by a model in a fresh session, desk review only (no child tested). Branch `claude/great-fermi-1hv4vc`. Nothing in the book, data, tools or notes was edited; this file is the only change. Round 1 is `AUDIT.md`; the fixes are in `AUDIT_NOTES.md` and `PROGRESS.md`.

## Verdict
**Nearly ready to sell: one more small text-only round, then yes.** All round-1 High items are closed except that the holiday-overlap check turned up near-copies that remain or are new (below). No answer is wrong (every new or changed item re-solved by hand, all agree with the key). The Welcome page, "Beyond Level 2" badges, wide boxes for numbers, contents and answer page numbers, and 100 pages are all correct. What stops a plain "yes":

1. **New near-copy of a holiday item in the new Unit 9 Learn page** (worked example 2 is the holiday "lesson starts at 4:50 pm and lasts 25 minutes" with new hour and am).
2. **U3 T01 (bicycles and tricycles) is almost word for word the holiday item** (not flagged in round 1; the same standard that replaced U5 C03 applies).
3. **U4 T01 (new frog item)** reuses the holiday frog frame and the number 30 ("Will it land on ... 30?").
4. **"DRAFT licence text, for owner and lawyer approval. Not final." is still printed on p2** of both editions.
5. Word answers (banana, mango, swimming, tennis, chess) sit in the small 16 mm boxes (Low to Medium).

Items 1 to 3 are rewrites of one or two sentences; answers can be kept (suggestions in section 4). Items 4 and 5 are one-line fixes. A child trial is still needed for pace and the clock page.

## 1. How I worked (honest)
- **Edition files.** The print BW PDF is image only (1-bit CCITT, 600 ppi, 100 pages, A4). I read the text from `build_extras/*_Print_BW_vector.pdf` (the build source of the print file) and from the colour PDF text. After removing line-wrap differences the only differences between them are the licence line ("printed book" / "soft copy") and the footer layout. I then **looked at the actual print pages** (rendered at 110 dpi; zooms at 200 to 250 dpi where marked): pp. 3, 22z, 28, 31, 36, 37z, 39, 42, 43, 44, 46, 48, 49z, 50, 51, 52, 55, 56, 57z, 59, 60, 62z, 63z, 64, 65, 67, 72, 73, 77. Not viewed as images: pp. 14 to 18 (Unit 2), 19, 23 to 26, 29, 30, 32 to 35, 38, 40, 41, 45, 47, 53, 54, 58, 61, 66, 68 to 71, 74 to 76 (read as text; their figures were unchanged since round 1 apart from the items named below).
- **Round-1 diff.** I diffed every `extension/data/l2_u*.json` item against the audited commit `c494f19` field by field (ignoring the `{b}` to `{bw}` box change) so that no changed item was missed. Changed items are listed in section 3.
- **Hand solving.** All new and changed items were solved cold from the printed wording and figure, then compared with the printed answer and the Why line. I did not use the `l2_uNN_checks.py` as a source. Afterwards, for the gates only: `run_checks --level 2` (497 answers, OK), `wording_lint` (0 errors), `dup_check` (OK, REVIEW list only), `fill_check` (OK), `build_report.json` (no page over, 100 + 100 pages). 1-bit check: every image in the print file is `ccitt` 600 ppi.
- **Overlap check.** My own scan (not `dup_check.py`): all 1,372 text strings of `p2/content/l1..l10.js` against every item stem, parts and the Learn examples, by shared 5-word runs after masking numbers, then read by hand. Results in section 5.
- Not testable here: what a 7-year-old does with the Learn pages; handwriting size.

## 2. Round-1 High and Medium: closed or not
| Round 1 | Status | Evidence |
|---|---|---|
| H1 rulers sentence on Welcome (print and soft copy) | **Closed** | p3 has no rulers sentence; the soft copy "Print at 100 percent" line is gone; grep of both editions finds no "ruler" except U6 S05(a) "A ruler costs 70¢" |
| H1 "Beyond Level 1" labels | **Closed** | 12 badges, all "Beyond Level 2: ..." (pp. 11, 18, 25, 32, 39, 46, 53, 59, 60 twice, 67, 74), none in Start here; Welcome says "Beyond Level 2 is ahead of school. You may skip it." |
| H1 duplicate "Beyond:" stem word | **Closed** | removed in U3 G01, U5 G01, U6 G01, U7 G01, U8 T01, U8 G01, U9 G01, U10 G01 |
| H2 repeats of holiday items | **Mostly closed** (see 5) | U4 S01, U4 T03, U5 G04, U5 C03, U2 G04, U8 G01, U8 T02, U5 S06 replaced and no longer share a story or frame. U4 T01 and U4 S01 are still frame-close; new problems found (section 4) |
| H3 Learn pages U7, U8, U9 | **Closed with small gaps** | section 6 |
| M1 second readings | **Closed** | U3 T02(d) "All 6 may be hens"; U3 G04 "2 by 12 and 12 by 2 are different"; U4 S03(b) "The 6th E"; U10 S08 "Write fractions in sixths"; U10 C04 and U7 C04 "in twelfths"; U3 S01 "(either order)"; U6 S10 "(any order)"; U5 S05 key says which row; U9 S06 rewritten in three steps |
| M2 U2 G02 Why letters | **Closed** | (a) 495 and 693, (b) 9, (c) 495 |
| M3 weak Whys | **Closed** | U2 S01 (names the digit), S09, S11, S06 ("may have forgotten"), U3 S06 now give the method |
| M4 answer-giving hints and "coin" | **Closed** | U2 T01 hint "Which numbers are used in 2 sides?"; U8 T01 hint "Fold in your head..."; "$1 coins", "coins of 10¢" |
| M5 tier honesty (move U2 S02, U6 S04) | **Not done, deferred by author** | acceptable; child trial decides |
| M6 9 to 11 Start here items | **Accepted** | page budget |
| M7 wide boxes | **Closed for numbers** | section 7; word answers still narrow |
| M8 figures | **Closed** | U3 S04 redrawn (section 3); white backing on the hatched "3" (U5 S08) and "27" (U9 S08) checked at 220 dpi |
| M9 pace wording | **Not done, deferred** | "20 to 25 minutes" unchanged; needs the child trial |

## 3. Hand-solved new and changed items (all agree with the key)
Format: my answer, then note. "Why" read for each; all say what the key says.

**Replaced items**
- **U4 S01** (p28) count back in 5s from 60, 55, 50: 45, 40, 35. Frame is still "Count ... in Ns. Fill in the next numbers" (see 5, Low).
- **U4 T01** (p31) frog hops 3, 1, 3, 1 from 0: lands 3, 4, 7, 8, 11, 12 ...: 27 Yes (24 + 3), 30 No, 40 Yes. Correct. Frame problem in section 4.
- **U4 T03** (p31) train, engine 2 children, carriage 5, table 2, 7, 12: 4 carriages 22, 8 carriages 42, 37 children 7 carriages (35 / 5). Correct. Story is new. (The numbers 4, 6, 8 ... 22 reappear in S10, see 5.)
- **U5 S06** (p36) tokens: 3 give 11, 6 give 17: 2 each, bonus 5, 10 tokens give 25. Correct; the "fair machine" story is new and there is no other fit.
- **U5 G04** (p39) A: x2, +3; B: -5, x3; final 36: OUT of A 17, IN to A 7 (checked 7, 14, 17, 12, 36). Correct. Machine figure is small (about 100 mm) but the numbers read in 1 bit.
- **U5 C03** (p40) doubles then +9 = 25: 8. Correct.
- **U2 G04** (p18) Mei +198 equals Ali 900 - 102 = 798: 600; Ravi +299 equals 1000 - 201 = 799: 500. Correct, unique.
- **U8 G01** (p60) cans in a triangle: 6 rows bottom row 6, 6 rows 21, 8 rows 36. Correct.
- **U8 T02** (p59) strip of 5 stamps: pieces of 1: 5, of 2: 4, of 3: 3, of 4 or 5: 3, all 15. Correct. (Two boxes in (d): 3 then 15.)
- **U3 S04** (p22) 3 dogs 12 legs, 2 ducks 4 legs, all 16. Redrawn animals are separate, each leg set countable (dog 4, duck 2) at 220 dpi; the label no longer touches the legs. **Closed.**

**Rewritten second-reading and wording items**: U3 T02(d) Yes (6 hens, 12 legs); U3 G04 6; U3 S07(a) 7; U4 S03(b) 28; U6 S04(b) 3 and 1; U10 S08 3/6, 3/6, 300; U10 C04 7/12; U7 C04 4/12; U9 S06 (a) 3, (b) 2, (c) 6 (8 - 2); U1 S06(a) "From your list" 851, 158; U2 S01 4 and 9, 4 and 4, 4 and 3 (digits all re-derived from the printed sums 244 + 359, 448 + 426, 465 + 238); U2 S02, S09, S11, G02 unchanged answers, Whys correct.

**New Learn pages** (full text and figures read): U7 (pizza bar 3/8, number line 3/4, Try 7/10 correct), U8 (grid 2 by 2 = 5, stack of 6 cubes, Try 8 correct), U9 (melon = 3 plums = 150 g, clock 8:50 + 25 min = 9:15 am, Try 100 correct).

**Unchanged but re-solved because they sit on changed pages** (U9 S01 to S11, T01 to T03, G01 to G04, C01 to C04; U8 S04 to S10, T01, T03, G02, G04; U7 S01 to S09, T01, T03, G01, G02, G04): 9 clocks and keys: 4:35, 8:50, 11:15; am, pm, pm, am; 4:15 pm, 40, 4:40 pm; 1 h 30; lemon 50, apple 150; g, cm, kg, l; 58, 139, 25; 3000, 2 kg 500 g, 1250; 235, 1 m 80, 370; 4 pours, 10 l; plum 100, pear 400; jugs (2, 7) then 4; tour 95 minutes, ends 10:50 am; 15:45, 6:10 pm, 8:05 pm; cup 200, box 400; clock gains: 11:12 am and 12:00; stack counts 6, 6, 10; nets A yes, B yes, C no, D no; triangles 3, 2, 1, 6 and 6, 6, 12; painted 8, 24, 24, 8; rectangles 18; fractions 2/5 and 3/5, 6/8 and 2/8, 5/12 and 7/12; and so on. All match.

## 4. Remaining findings
### Must fix before sale (small)
**R1. U9 Learn worked example 2 is a near-copy of a holiday item.** Printed: "A lesson starts at 8:50 am and lasts 25 minutes. When does it end?" Holiday (`l9.js`): "A lesson starts at 4:50 pm and lasts 25 minutes. What time does it end?" Same sentence frame, same minutes (50 and 25). It is also the same time as clock B in Start here 1 (8:50), so the Learn page gives away part of S01. Fix: new story and a new time on the clock, for example "A concert starts at 7:55 pm and lasts 30 minutes" (7:55 to 8:00 is 5 minutes, 25 more, ends 8:25 pm; clock figure `h 7, m 55`). Avoid "film" (S03 uses it). Net zero in space.

**R2. U3 T01 (p24) is almost the holiday item.** Printed: "A shop has bicycles (2 wheels) and tricycles (3 wheels), at least 1 of each. There are 21 wheels altogether. Find ALL the ways." Holiday (`l3.js`): "A shop has some bicycles (2 wheels) and some tricycles (3 wheels), at least one of each. There are 17 wheels altogether. Find ALL the ways. Start with 1 tricycle ..." This was not in round 1 and is the closest frame in the whole book to a holiday item. Fix: a new story and the same numbers, e.g. "A yard has scooters (2 wheels) and trikes (3 wheels) ..."; keeping 21, the table and the key. (Round 1's standard replaced U5 C03 for a frame that was only a little closer.)

**R3. U4 T01 (p31, new) reuses the holiday frog frame and the number 30.** Printed: "A frog starts at 0. It hops 3, then 1 ... Will it land on 27? ... on 30? ... on 40?" Holiday (`l4.js`): "A frog starts at 1 and jumps 4 each time ... Will it land on 37? Will it land on 30? Explain." The mechanism (alternate 3 and 1) is new, the frame is not. Cheapest fix: change the animal and replace 30 by 26 (answer stays No: the landings are 24, 27, 28 ..., so 26 is skipped; edit the Why to say so).

**R4. Licence draft line.** p2 (both editions): "DRAFT licence text, for owner and lawyer approval. Not final." (round-1 Low 5, not fixed). Remove before packaging.

### Should fix (Low to Medium)
**R5. Word answers in 16 mm boxes.** U10 S07 (banana, mango, apple), U10 T01 (tennis, chess, art, swimming), U6 S09 (Car and Top). "swimming" is 8 letters and will not fit a 7-year-old's handwriting. Use the wide box or ask for the first letter. All number, money, fraction and decimal answers are in the wide box: closed.

**R6. U5 G03 (p39)** now has only one ruled line (about 120 mm) for the child's riddle; the example riddle is about 60 characters. The "Check going forwards" row was removed to save space. Fine for a short riddle, tight for a 7-year-old; give it 2 lines if the page allows.

**R7. Learn examples repeat Start here answers.** Besides R1 (U9 clock B): worked example 2 of U8 (the stack, 6 cubes) has the same shape and count as stack B in S05 (6). Change one dimension (for example heights 3 and 1, 8 cubes), or the example shows B's answer.

**R8. Remaining Low items from round 1 (author declined, shared template):** Contents p4 prints each unit title twice; Welcome step 3 says "Stuck? Find the hint" (Start here and Check yourself have no hints); cover and About say "Ages 7-9"; certificate trophy plaque still carries pseudo-text. None blocks sale; the DRAFT line (R4) does.

**R9. Welcome page fits by 1.3 mm** (fill 0.995; the last box ends just above the footer). It does not overflow and nothing is cut, but any extra word in `levels.json` will push it over. Note for whoever edits the Welcome note.

**R10. Small text points.** U9 S06(b) "Pour the 3 l in. It needs [ ] l more." does not say into which jug (the 5 l jug, from the 8 l jug); "It needs" makes it clear enough. U7 S08(b): a lone full stop after the box on its own line. U4 S01: the first answer box is followed by a comma at the end of the line and the other two boxes wrap (readable). U9 S03(c) (find the start time) needs counting back, which the Learn page does not show.

## 5. Overlap with the holiday program (frame by frame)
No shared 7-word run (dup_check agrees). My 5-word scan and reading of the nearest hits:

**New or changed items: acceptable.** U5 S06, U5 G04, U5 C03, U4 T03, U8 G01, U8 T02, U2 G04, U9 S06 (the jug item shares only "pour into the ... jug until it is full" with the holiday jug solution), U8 G02 (painted cube, 4 by 4 by 4 with four counts, holiday asks the no-paint count of 3 by 3 by 3: same idea, different size and questions).
**Frame-close, to fix:** R1, R2, R3 above. **U4 S01** now "Count back in 5s. Fill in the next numbers. 60, 55, 50" against the holiday "Count in 4s. Fill in the next three numbers: 4, 8, 12". Different direction and numbers, but the same short stock frame; Low (change to "Count on in 6s from 6" if you want zero similarity).
**Same type, new numbers (round 1 accepted; listed so the owner can decide):** U10 T03 (same Mei and Ali savings story as holiday `l10.js`, including "Mei ... first has more than Ali on day"; the highest 5-word overlap, 10 shared runs), U7 T02 (quarter then half of the rest; holiday half then half), U7 G03 (fair-share cake story), U6 S04 (every way to pay $7; holiday $10), U6 T02 (two prices, 7 things, spends exactly; holiday pens and books), U6 T03 ("costs $4 more than a puzzle"), U3 S05 and U3 T03 (ducks and rabbits swap; number between 30 and 50 with groups of 3, 4 and 5), U9 T01 and T02, U9 S11 (bucket), U1 digit cards.
**One that was not noticed before: U4 S10 (towers 4, 6, 8 ... tower 10 has 22; tower 8 has 18)** has the same numbers as the holiday Q5 (tables seat 4, 6, 8; 22 children for 10 tables). Same sequence and the same 10th term. Medium to Low; change the start (for example 5, 7, 9).
Private sources: no 7-word run (dup_check). No SASMO, MOE, GEP, price or test-result wording in either PDF (grep).

## 6. Learn pages: can a child start the first Start here items alone?
- **Unit 7 (p48): yes.** Equal parts, naming, "same bottom number: add the tops", "7/7 = 1" (S03) and a number line cut in 4 (S09, cut in 8). The fraction wall (S04) is read from the picture; nothing else is needed. S01 to S03 are fully covered.
- **Unit 8 (p55): yes.** Solids box now has cube, cylinder, cone and sphere (S01, S07, C01); half and quarter circle sides in the intro (S02); square count in a 2 by 2 grid (S04, Try); stack of 6 cubes counted row by row (S05). Small gap: S03(a) "quarter circles make 1 half circle" is not stated (2 quarters = half, 4 = whole); a child with no prior idea guesses from the figure.
- **Unit 9 (p62): mostly yes.** It now shows a balance (S05), a clock with minutes and an elapsed-time example (S03, S04), am and pm, "1 kg = 1000 g, 1 m = 100 cm" (S09, S10) and "long hand on 7 means 35 minutes". Gaps: S01 (reading clocks) is taught by one fact and one clock; the rule for where the short hand sits between two numbers and counting in 5s round the face are not stated, and a child with no clock at school will struggle with clock A (4:35). Jugs (S06) have no worked example; S06 itself gives each pour, so a child can follow it. S03(c) counts back and the page only counts on. None of these makes the page unusable; the round-1 concern is closed, but the clock fact is the thing a child trial must watch.

## 7. Layout and print checks
- **Page count 100** in both editions (even). **Contents** (6, 13, 20, 27, 34, 41, 48, 55, 62, 69, 76, 77, 79) and **answer start pages** (80, 82, 84, 86, 88, 90, 92, 94, 96, 98) match the PDF: I read each Learn it page and the answer headings "Unit N" on pp. 80 to 98. The pace plan numbers match the unit pages. The answers divider is p79 as Welcome says.
- **Welcome (p3):** no rulers sentence, no overflow (see R9 for the margin). The "Beyond" line sits in the grown-up box. Colour and print Welcome text identical.
- **"Beyond Level 2" badge:** printed at the top right of the item box, 8 pt, readable in 1 bit, does not touch the stem.
- **Wide boxes:** money, fraction, decimal and 4-digit answers use the wide box (about 25 mm): U6 S01 (b)(c), S02, S05(b), S06 (a)(c), S07, T03, G01, G02(b); U7 S06, S07, S08, S09, T01, T02, T03, C04; U9 S09(c) (1250), S10; U10 S08, S09, C04. I checked every part whose key has 5 or more characters, a decimal or a fraction: all are wide except the word answers in R5. 10.80, 27.40, 12/12, 9/12, 7/12, 1250 would fit.
- **1-bit legibility** of changed pages: hatched cubes and fractions, the stacks, clocks (hands and numerals; clock B's hand tip touches "10" but reads), balance and scale figures, the 8 mm nets, machine strip (U5 G04, small but readable), U3 S04 animals, white-backed hatched digits: legible. The print file has no grey (CCITT 1 bit); `bw_check.py` as in round 1 was not re-run on the image (the gates in `build_report.json` pass).
- **Soft copy:** text identical to print apart from the licence line; colour figure pages were not viewed.

## 8. Ranked list for round 3
1. U9 Learn worked example 2 (R1): new story and time.
2. U3 T01 reword (R2).
3. U4 T01: new animal and 26 for 30 (R3).
4. Remove the DRAFT licence line on p2 (R4).
5. Wide box for word answers in U10 S07, T01 and U6 S09 (R5).
6. U4 S10 start numbers (Section 5) and U4 S01 frame (optional).
7. U5 G03 second line; U8 Learn stack different from S05 B (R6, R7).
8. Child trial: clock page U9 p63, stack counting U8 p57, pace of sessions 1 and 3, whether 16 mm boxes are used for money.
