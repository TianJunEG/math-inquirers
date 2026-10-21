# Fixes applied to the P5 program (from docs/audit/gifted_p5.md)

Date: 2026-10-22. Edited the SOURCE only: p5/content/l1.js to l10.js (question banks and workbook pages) and rebuild/gen_p5l1.py (one slide item). Nothing was committed or published. No shared file was changed (rebuild/slidekit.py, hp/*, levels/*, p5/workbook_html.js, p5/guide.js, p5/data.js are untouched).

## What was done, in one paragraph
Every Core bank item that needed the lesson's formal method was rewritten as a concrete, pictorial, cut-and-fold, counting or guess-and-check item (or the needed fact is now stated in the item); under-level Think Harder items were swapped down to Core or replaced; one-step Challenge items were replaced by extensions, "find all" items, "what if" items or a problem-posing item (every lesson now has one open-ended "make up your own" item in the Challenge bank); workbook questions that had no way in got a one-line "Start here" scaffold or a printed hint. Answer keys were not changed because no worksheet answer changed. All new or changed numbers were verified in Python (exact fractions and brute force); "find all" and "only one answer" claims were brute-forced.

Totals: 36 Core bank items rewritten (L1 2, L2 6, L3 3, L4 6, L5 6, L6 3, L7 4, L8 6; L9 and L10 none needed), 7 Think Harder items replaced (L1 2, L4 2, L5 1, L6 2) and 1 relabelled (L2), 18 Challenge items replaced or extended (one per violation found), 11 workbook scaffolds added (L1, L2 x2, L3 x2, L5, L6, L8 x2, L10 x2). L4, L7 and L9 workbook pages needed no change.

## Verification (Python, exact arithmetic or exhaustive search)
L1: one pair of brackets on 2 + 3 x 4 + 5 gives 19, 25, 29 (29 is the maximum); every bracketing of 1 + 2 x 3 + 4 x 5 + 6 has maximum 231; riddle 6 953 487 and workbook riddle 7 253 609 are unique; digits 1 to 1000 = 2893 and 1 to 1 000 000 = 5 888 896; new sample riddle gives exactly one number, 5 437 209 (all 7-digit numbers searched); cards 1, 2, 5, 6, 7, 8, 9 closest to 7 000 000 is 6 987 521 (12 479 away; best above 7 125 689); 2, 3, 5, 7 reach 29, 31 and 100 (43 is not reachable, so it is not used). L2: 3/4 as three different unit fractions has exactly 3 ways (1/2 + 1/5 + 1/20, 1/2 + 1/6 + 1/12, 1/3 + 1/4 + 1/6); 1 as three has exactly 1 way; 2/3 as two has 1 way; 5/12 as two has 2 ways; cards 1, 3, 5, 7 smallest positive difference 8/35; tank 54, 36, 24, 16 litres; 1/2 x 2/3 x ... x 9/10 = 1/10. L3: counters 18 and 6, total 24: eight exact-multiple outcomes (smaller number divides 24 and is under 12); sample story 60 and 48 gives 36 and 72 after the gift. L4: 13-14-15 triangle area 84 and heights 12, 11.2, 12.92; DEF = 22.5 cm2 in the sample puzzle; ADF - FCE = 16 cm2; (60 cm2) rectangle checks. L5: cuboids from 64 cubes = 7, from 12 cubes as rectangles = 3, painted 3 by 4 by 5: 8, 24, 22, 6 inside; 11.5 cm tank answer; 1000 cm3 stone on 500 cm2 raises 2 cm. L6: eggs minimum $9.60 (1 box of 10 and 3 of 6); car park $9.50; phone plans equal at 100 minutes; pens at Y $12 vs X $16; dripping tap 216 litres. L7: sample trap $60 to $90 to $45; 24/40 = 60%; GST $1.80. L8: isosceles cases (50, 50, 80) and (40, 70, 70) only; clock and pizza angles. L9: spiders and beetles totals are the 21 even numbers 120 to 160; 100th digit is 5; 26 x 27 = 702; 342 digits in 1 to 150; 30 squares in a 4 by 4 grid. L10: 60 rectangles in a 3 by 4 grid (20 squares); tank 120 litres, 60 after adding, 45 after letting out 1/4 (3/8 of the tank); coins puzzle unique (3, 6, 16); chairs puzzle unique; hawker logic grid unique.

## Per lesson: what changed (old item -> new item, tier moved)

### Lesson 1: Million Puzzles
| Where | Old | New | Tier change |
|---|---|---|---|
| Bank Core C4 | 2 750 000 ÷ 1000 | Digit cards 0 to 6: make the greatest and the smallest 7-digit number (hands-on, promoted from Think Harder S8) | S8 moved up to Core |
| Bank Core C5 | 48 − 6 × (3 + 4) | Pen-shop story: 6 packs of 3 red and 4 blue pens from 48 pens (counters allowed); the number sentence appears only in the answer | stays Core, now concrete |
| Think Harder S6 (also on the Stretch slide, item 2) | $250 a week to reach $1 000 000 | Use 2, 3, 5, 7 once each with + − × ÷ and brackets to make 29, 31, 100 (verified by exhaustive search; 43 is not reachable, so it is not used) | replaced, same tier |
| Think Harder S8 | smallest and greatest 7-digit number, digits all different | Digits 1, 2, 5, 6, 7, 8, 9 once each: the number closest to 7 000 000 (6 987 521, 12 479 below; best above is 7 125 689) | replaced, tests "both sides" |
| Challenge H1 | How many 7-digit numbers are there? (9 000 000) | Problem posing: make up your own 5-clue digit riddle with exactly one answer, swap with a partner. Sample riddle checked over all 7-digit numbers: only 5 437 209 fits | replaced (problem posing) |
| Workbook Q3 | Six-clue riddle with no starting point | Added a "START HERE" line inside the clue box: Clue 2 means the number starts 7 2 or 7 3, try both with Clue 3 (to keep two pages, Q1(a) and the Q2 stem were shortened and the place-value table rows lowered from 110 to 80). Answer unchanged (7 253 609, unique, verified) | scaffold added |

### Lesson 2: Fraction Feats
| Where | Old | New | Tier change |
|---|---|---|---|
| Bank Core C1 to C6 | formal items (7 ÷ 9; 2/3 + 3/4; 5/6 − 1/4; 3/5 of 15; 2/3 × 9/10; 3/5 × 1/2 + 1/10) | Picture and object items: 3 chocolate bars among 4 friends; 1/2 + 1/4 of a pizza; 12-slice pizza with 1/3 and 1/4 eaten; 3/5 of 15 with dots; half of half a cake; compare 3/4 and 2/3 with two bars | Core now low floor |
| Think Harder S6 | rope 3/4 m cut into 3 | same, labelled "(Preview of P6)" and "draw a bar" | label |
| Challenge H4 | 2/3 of 3/4 vs 3/4 of 2/3 | Problem posing: make up your own fraction-of-a-remainder story, swap and check, then change one fraction and say what changes | replaced |
| Challenge H6 | Mei Monday and Tuesday (same model as the worked example) | Write 3/4 as three DIFFERENT unit fractions, find all and explain why you have all of them. Exactly three ways, brute-forced: 1/2 + 1/5 + 1/20, 1/2 + 1/6 + 1/12, 1/3 + 1/4 + 1/6 | replaced |
| Challenge H9 (printed Think Harder Q7) | tank, 1/3 out three times, 16 left | Same tank, three parts: (a) 54 L, (b) after how many hours is less than half left (2), (c) how much was let out by then (30 L) | extended |
| Workbook Q2 | no entry point | "Start here: take away 1/2 (then 1/3, 1/4 …) and see what is left; is the top number 1?" | scaffold added |
| Workbook Q5 | blank model box | "Start here" line: bar in 5 equal parts, 2 parts spent, cut so that half of the rest is easy; model box shortened (760 to 520), Q1(d) and Q6 stems shortened to keep two pages | scaffold added |

### Lesson 3: Before and After
| Where | Old | New | Tier change |
|---|---|---|---|
| Bank Core C1 | baker 2/5 and 1/3 of the rest | Counters: Ali 18, Mei 6, Ali gives 4; totals before and after (24 and 24) | replaced (baker item dropped: it duplicated Think Harder S1) |
| Bank Core C2 | Ben 10, father 38, when is Ben half his age | Ages in 5 years, and the age difference now and then (28 and 28) | replaced |
| Bank Core C6 | Mei and Siti spend $18 and $42, then 1/3 | Jar of 24 red and 12 blue beads, 12 more red added: blue is 1/3 then 1/4, blue did not change | replaced |
| Challenge H1 | $180 shared 1/3, 1/4 of rest | Problem posing: make up your own before-and-after story with a fraction in the After; sample story (108 stickers, Ali gives 24, then 1/2) gives 60, verified | replaced |
| Challenge H2 | Mei spends $12, 1/2, $8 | Ali 18 and Mei 6: list ALL ways in which one child has an exact whole-number multiple of the other after giving. Eight ways, brute-forced (smaller number divides 24 and is less than 12) | replaced |
| Workbook Q1 | empty bar | "Start here: guess $60, work out the rest, too much or too little compared with $36?" | scaffold added |
| Workbook Q4 | opens with a concept question | "Start here: try a gift of $10 each, is Ali's money 2/3 of Ravi's?" | scaffold added |

### Lesson 4: Triangle Areas
| Where | Old | New | Tier change |
|---|---|---|---|
| Bank Core C1 to C6 | formula items (12 and 5; 8-15-17; 36 and 8; diagonal; square; 14 and 9) | Cut, fold and draw items on grid paper: rectangle 6 by 4 on the diagonal (12); square 8 with a point on the top side (32); right-angled 4 by 3 turned into a rectangle (6); rectangle 5 by 4 with a moving point (10, does not change); two halves of a 6 by 5 rectangle (30); shade a triangle in an 8 by 3 grid rectangle (12) | Core now needs no formula |
| Think Harder S3 (printed Q3) | square 10, triangle on one side (50) | Triangle and square with the same area, find the triangle's height (8 cm) | S3 old moved down to Core; H3 old promoted to Think Harder |
| Think Harder S8 | base 7.5, height 4 | Ali and Mei, double the area, base 5 (height 24) (promoted from Challenge H6) | replaced |
| Challenge H1 | ABC 60, D the middle of BC | Problem posing: make up your own shaded-area puzzle, solve it two ways, swap. Sample 10 by 6 rectangle: DEF = 22.5 cm2 (exact area checked) | replaced |
| Challenge H3 | triangle and square, same area | "What if": base times 3, base times 3 and height half, base times 4 keeps the area if the height is a quarter, say a rule in words (90, 45, 1.25 cm) | replaced (no algebra letters used) |
| Challenge H6 | Ali and Mei | 13-14-15 triangle: area 84 cm2 from the 12 cm height, then the height on the 15 cm side 11.2 cm, and why it is shorter | replaced |

### Lesson 5: Volume Vault
| Where | Old | New | Tier change |
|---|---|---|---|
| Bank Core C1 to C6 | formula items (cuboid 9 by 4 by 5; 6-cm cube; half-full tank; reverse formula; 2 litres more; stone raises 2 cm) | Concrete items with cubes and layers: build a 3 by 2 by 2 box (12); flat rectangles from 12 cubes (3 ways); water layers in a 10 by 10 tank (300, 1000 = 1 litre); dice in a 5 by 4 by 3 box (60); 12 cubes into a 4 by 3 tank (rise 1 cm); litres to cm³ and ml | Core now hands-on |
| Think Harder S8 | 10-cm cube cut into 2-cm cubes (125) | Tank 50 by 20, water 8 cm, 3 litres poured in, then a 500 cm³ stone: 11.5 cm | replaced |
| Challenge H5 | hollow 5 by 5 by 5 cube (98) | Problem posing: make up your own tank puzzle with a stone, swap, and say what changes if the base is twice as wide (sample: 1000 cm³ stone in a 25 by 20 base raises the water 2 cm; 1 cm if the base is doubled) | replaced |
| Workbook Q3 | no entry point | "Start here: think of the water as 18 layers of cubes; the bottom layer is 50 by 30; 1000 cm³ = 1 litre" | scaffold added |

### Lesson 6: Rate Racers
| Where | Old | New | Tier change |
|---|---|---|---|
| Bank Core C1 | 5 kg flour $8.50 | 4 apples cost $2: 8, 12 and 1 apple (table allowed): $4, $6, 50¢ | easier |
| Bank Core C3 | 4 rolls $3.40 or 6 rolls $4.98 | Pack A 3 pens $2 or Pack B 6 pens $5, with the hint "buy A twice for 6 pens" | easier |
| Bank Core C5 | taps 10 and 14, 192 litres | Taps 2 and 3 litres a minute: litres after 1, 2, 5 minutes and the time for 20 litres | easier (adds the rates by repeated adding) |
| Think Harder S6 | Ali's weekly wages | Shop X 80¢ a pen vs shop Y "4 for $3.00 plus 1 free": 20 pens, Y cheaper by $4 | replaced |
| Think Harder S8 | petrol 8 litres per 100 km | Dripping tap, 5 ml every 2 seconds, litres in a day: 216 | replaced |
| Challenge H6 | Ravi and Siti reading | Problem posing: make up a better-buy puzzle where the biggest pack is not the best buy; sample 6 for $3.00 / 10 for $5.50 / 12 for $7.20 | replaced |
| Workbook Q5 | car park, no first step | "Start here: how long is 9.40 a.m. to 1.15 p.m.? Count the first hour, then the half hours or parts left" | scaffold added |

### Lesson 7: Percentage Puzzles
| Where | Old | New | Tier change |
|---|---|---|---|
| Bank Core C1 | 10% and 15% of $360 | Hundred-square with 35 shaded: percentage shaded and not shaded (35%, 65%) | easier, pictorial |
| Bank Core C2 | 20% discount on $45 | "Percent means out of 100": 50% of $80, then 25% (half of it) and 10% (a tenth): $40, $20, $8 | easier, built from halves |
| Bank Core C3 | 9% GST on $30 | $50 book with 10% (one tenth) off: $5 off, pay $45 | easier |
| Bank Core C6 | 21 of 60 seats as a percentage | Notebook $20 with 9% GST, given "1% of $20 is 20¢": GST $1.80, pay $21.80 | replaced (a scaffolded GST item) |
| Challenge H1 | $100 up 20% then down 20% (the explore with new numbers) | Problem posing: make up your own percentage trap (sample: $60 up 50% then down 50% gives $45, 25% less), swap with a partner, change the percentages | replaced |

### Lesson 8: Angle Chasers
| Where | Old | New | Tier change |
|---|---|---|---|
| Bank Core C1 to C6 | straight line 127°; angles at a point; triangle 48° and 67°; isosceles top angle 30°; parallelogram 70°; rhombus 124° | Hands-on and given-fact items: tear a triangle's corners (180°); straight line with "180°" stated (53°); pizza cut in 8 (45°); draw and measure a 48° / 67° triangle (about 65°, sum 180°); fold a 90° corner twice (45°, 22.5°); tear the corners of a four-sided shape (360°) | Core now discovered or stated |
| Challenge H2 | fourth angle of a four-sided shape (70°) | Problem posing: make up your own angle-chase puzzle that needs at least three steps, with a reason for every step; sample (parallelogram ABCD with DA = DE) gives EAB = 62° | replaced |
| Workbook Q1 | no facts on the page | Hint line: a straight line is 180°, a full turn 360°, opposite angles are equal | scaffold added |
| Workbook Q2 | shape facts only on page 2 | Hint line: parallelogram, rhombus and trapezium facts | scaffold added |

### Lesson 9: Pattern Generalisers
Core, Think Harder and the workbook pages already complied (checked item by item); no change to them.
| Where | Old | New | Tier change |
|---|---|---|---|
| Challenge H2 | triangles use 99 sticks, which figure | Problem posing: make up your own growing pattern, draw three figures, write the rule in words and two questions (figure 50, which figure uses exactly 100); sample triangles pattern: figure 50 has 101 sticks and no figure has 100 (sticks are always odd) | replaced |
| Challenge H4 | spiders and beetles, 136 legs | Same creatures, new questions: legs with 8 spiders (136), list ALL possible totals (every even number 120 to 160, 21 totals, brute-forced), why 135 is impossible, how many spiders for 148 (14) | extended (generalise and justify) |

### Lesson 10: Challenge Day
Core, Think Harder and most of the workbook already complied; no change to them.
| Where | Old | New | Tier change |
|---|---|---|---|
| Challenge H3 | Ali, Ben and Mei share 76 stickers (one bar model) | Rectangles of ALL sizes in the 3 by 4 grid of Question 4: 60 (by size, and checked by choosing 2 of 5 vertical and 2 of 4 horizontal lines; brute-forced) | replaced (extends Q4's counting by size) |
| Challenge H5 | 2-digit number, digits add to 11, swap +27 | Problem posing: make up your own four-people logic puzzle with exactly ONE answer and say which clue can be removed | replaced |
| Challenge H7 (printed Q5) | tank 1/3 to 1/2 after 20 litres | Same tank, then 1/4 of the water let out: 45 litres, 3/8 of the tank | extended (two stages) |
| Workbook Q1 | no first step | "Start here: write the steps in order, then undo the LAST step first" | scaffold added |
| Workbook Q3 | no entry | "Start here: draw Mei's money as 4 equal units; how many units is 3/4 of Mei's? where does the $10 go?" | scaffold added |

## Regenerated decks
Only rebuild/gen_p5l1.py changed (the Stretch slide's second item and its answer note), so only deck **p5l1** was regenerated (python3 rebuild/gen_p5l1.py, then python3 levels/restyle.py split/p5l1): 26 slides. The preview check shows one overflow, p5l1-explore1, which also existed before (see docs/audit/fixes_p5.md, restyle decoration, not caused by this change). Decks p5l2 to p5l10 were not regenerated: their slide items are either unchanged (L2, L4 to L10 slides print their own items or bank items that were not edited) or are not printed on slides at all. The slides' answer notes, workbook keys, tutor script notes and the parent packs are consistent: no worksheet answer changed, and the bank-derived pages (tutor guide, weekly dose, question bank, weekly email pack, free taster) were rebuilt from the new bank.

## Build and page counts
Commands run: bash levels/build_level.sh 5, then python3 levels/mkextras.py 5 (self-check: OK).
* Student workbook: **47 pages** (unchanged). Every lesson is 2 worksheet pages + 2 Think Harder pages. The first build after the edits was 52 pages (L1, L2, L5 and L10 spilled onto a third worksheet page); the scaffolds were shortened and merged into the stems, and a few row heights and one dotted answer line were trimmed until all ten lessons were back to 2 worksheet pages (re-measured by reading the page text of the final PDF).
* Tutor guide 69 pages (was 68; the longer bank answers add a page). Weekly dose 26 pages (was 25). Weekly PDFs zip rebuilt.
* Question bank 28 pages, weekly email pack 12, free taster 5, What Learners Get 1.

## Notes for the lead
* L4, L5 and L8 Core items now use grid paper, cubes or dice, paper folding and tearing, and (L8 Core 4) a protractor. All of these are already on those lessons' printed materials lists.
* The slide-only Stretch and Challenge items (L3 to L10) were audited and were all compliant, so none were rewritten.
* Remaining structural gaps (not fixable by item edits): no printed reflection prompt outside L10, posing items live in the bank only, fixed 90-minute routine. See the three gaps in docs/audit/gifted_p5.md section 2.
