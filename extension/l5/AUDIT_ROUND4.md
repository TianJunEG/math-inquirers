# Independent audit, round 4: Level 5 Extension Workbook

Audited 23 Oct 2026 by a fourth model in a fresh session. Report only: nothing in the book, data, builders or tools was edited, nothing was pushed, no PR. The only file written is this one.

Checked: `outputs/extension/L5/` print (100 pp, 1-bit 600 dpi), print vector (100 pp), soft copy (now **100 pp**), `build_report.json` (0 problems, soft 100, print 100, 0 B/W failures); `extension/data/l5_u01..u10.json` diffed against commit 4587e5d (the data audited in round 3) to HEAD d7b67a6; holiday text `p5/content/*.js`; `README.md`, `PROGRESS.md`, `AUDIT_ROUND3.md`.

## Method

- **Diff.** Item by item between 4587e5d and HEAD: **17 data entries changed** (listed in the table). `extension/tools` has no change since round 3. Everything else is unchanged.
- **Hand solving from the printed page** (print PDF, not the data): every changed item solved by hand, then compared with key and Why. `run_checks.py --level 5`: 417 answers OK.
- **Whys, all 244, both editions.** Print vector and soft copy answer pages (pp. 80-100) parsed: Why text equals the explanation of the item in that position for **244 of 244 in each edition**; the printed Answer equals the data answer for 244 of 244; the printed "page N" equals unit start + item page for 244 of 244, and for 242 the question text was found on exactly that page of the PDF (the other 2, U4 C03 and U5 C01, are figure-led and were checked on the page images). Print and soft text differ only in the licence sentence ("printed book" / "soft copy") and in where the page number sits in the text stream.
- **Contents and answer pages.** Unit starts 6, 13, 20, 27, 34, 41, 48, 55, 62, 69 each carry "Learn it" and the right unit; progress 76, certificate 77, answers 79; unit answers start 80, 82, 84, 86, 88, 90, 92, 94, 96, 98 (each shows the right unit heading); pace plan pages agree; the answers run to p. 100 in both editions (U10 Check 3 and 4 on p. 100). Identical in print and soft.
- **Frames.** Each changed item compared with holiday P5 content by search on nouns and numbers, then the named items read in full (l2.js 63/165, l3.js, l4.js 33/87/100/147-151, l5.js 119/149/152, l7.js 43/63/79/99-118, l8.js 155/180-199, l9.js).
- **Pages.** All changed pages rendered at 110 dpi from the 1-bit file (pp. 23, 28, 29, 30, 33, 38, 39, 45, 51, 52, 53, 55, 56, 57, 61, 62, 72); 300 dpi crops of the changed figures (pp. 28, 29, 33 x2, 38, 56, 57, 61).
- **Not done:** no child trial, no printer proof, soft copy compared as text only.

## Verdict

**Not yet sell-ready: three items still reuse holiday content (one is the holiday's own triangle), plus one stale README line. About 1 hour of data edits and a rebuild. Everything else is ready.**

Good: 0 wrong keys, 0 ambiguous items among the changes; all 244 Whys, answers and page references match in both editions; contents, answer page numbers, pace plan, 100 pages in both editions, print/soft parity; 1-bit legibility of every changed figure is fine; the round-3 M2, M3, M5 items and S2 to S4, S6 are fixed. The new items are mostly fresh. What blocks "new story and new frame, no shared key numbers" is below (N1 to N3).

## Per-item table (all changed entries)

Maths = hand solved from the page, agrees with key and Why unless stated.

| Item | Change | Maths / key / Why | Frame vs holiday P5 | Status |
|---|---|---|---|---|
| U3 S12 | shirt 1/5, shoes $36, 1/2 left | 1 - 1/5 - 1/2 = 3/10 = $36, 1/10 = $12, $120 (check 24 + 36 + 60) right; Why right | **Shares the key numbers of holiday l2.js Q5 (lines 63, 165): "Ravi spent 2/5 on a game and 1/2 of the remainder on a book, $36 left", 10 units, 1 unit = $12, answer $120.** Same story family (money on goods), same $36, $12, $120. Frame (given amount is a middle part) is different | **Too close (N3)** |
| U4 S01 | (a) 15, 15, base 18, h 12; (b) base 25, sides 15 and 20, h 12 | (a) 108, (b) 150 right (9-12-15 and 9-12-15 / 16-12-20 checks); Why right; figure clean at 300 dpi ("12 cm" crosses the slant with a halo gap, readable) | (a) new. **(b) is the 15-20-25 triangle of holiday l4.js 151 (stretch: right-angled 15, 20, 25, "height when 25 is the base", 12 cm, area 150).** Same triangle, same height 12, same area 150, the question just gives the 12 now | **Too close (N1)** |
| U4 S06 | parallelogram 16 by 9, E on DC, (a) triangle, (b) how many times | (a) 72, (b) 144 / 72 = 2 right; figure shows dashed height 9 and right angle, "9 cm" sits on hatch with halo, readable | Holiday has a rectangle 14 by 9 (63 cm2, l4.js 100). Different shape and numbers; skeleton "E on the top side, triangle on the base" is the same, and U4 S04 on the previous page is the same skeleton with a rectangle | **Fixed** (Low: S04 and S06 twin skeleton) |
| U4 S09 | 1.2 m by 80 cm, then cm2, then m2 | (a) 120 cm, (b) 4800, (c) 0.48 right; Why right | no holiday unit-conversion triangle (searched) | **Fixed** |
| U4 C01 | label "6 cm" moved | 16 base, slants 10, h 6: 48 right | answer 48 no longer equals S01(a) (108) | **Fixed**; "6 cm" still sits on the right slant with a halo gap (readable) |
| U4 C03 | hatch removed from the triangle | rectangle 60 + triangle 12 = 72 right | n/a | **Fixed**: the dashed height is now visible at 1-bit; "4 cm" at the apex reads as the height |
| U5 T03 | wall splits tank 20 + 40, water 24 deep, wall lifted | 20 x 40 x 24 = 19 200; 60 x 40 = 2400; 8 cm right; Why right; hint fine | new story. Method (water spread over the joined floor) and the numbers 24 and **answer 8 cm are those of holiday l5.js 152** (container A 24 high, spreads, 8 cm). Also the previous item on the same page (T02) is the same pooling idea | Low-Med (N5); figure: dashed back edges cross the water, readable |
| U5 G03 | cube B is 8 times cube A, A edge 5 | 125 x 8 = 1000, edge 10 right | different story. Cube volume 125 / edge 5 is a holiday warm-up (l5.js 119). Very easy for a Go further page (2 steps, no tricks) | **Fixed** (Low: too easy, N6) |
| U6 T03 | fuel 9 and 12 l per 100 km, 200 km, 19.5 l | 18 l if all open, 1.5 short, +3 per 100 km in town, 50 km (150 x 0.09 + 50 x 0.12 = 19.5) right | none (searched fuel, km, per 100 km) | **Fixed** |
| U7 S13 | 30%, 28 pages, 35% left | 28 pages = 35%, 80 pages right | holiday has 40%/25% of remainder and tank 40% to 70%; new frame | **Fixed** |
| U7 T03 | 10% service charge in $275 | 275 / 110 x 10 = $25 right | **Same frame as holiday l7.js 116 ("$109, GST included, how much GST"): total includes an added percentage, find the added part, unit 1% = whole dollars.** Story (restaurant) and numbers new, no GST | Low-Med (N4): story new, frame not |
| U7 G01 | bike $200, two rises of 10% | $220, $242, 42/200 = 21% right | **Holiday l7.js 43, 63 and 79 is the same $200 bicycle, up 10%, then 10% of the NEW price ($200, $220, then $198).** Same story, same numbers, only the second step is up instead of down. Also same hint idea as U7 T01 (coat $200, 10% then 20%) on the page before | **Too close (N2)** |
| U7 G02 | salt water 400 g, 5% to 8% | salt 20 g, 8% = 20 g so 250 g, 150 g boiled away right | no holiday salt or boiling item (searched) | **Fixed** (Low: G03 on the same page is also a "part that does not change" item) |
| U8 C01 | OD halves AOC, COB 70, find DOC | AOC 110, DOC 55 right; figure measures 70 and 55 (C at 110 deg, D at 55 deg) and is clean at 300 dpi | "3 times, 45 and 135" is gone. Bisecting phrase is in holiday l8.js 193 (triangle, different figure); answer 55 appears in two holiday warm-ups (l8.js 155) | **Fixed** (Low) |
| U8 Learn (Reasons) | equilateral line and clearer trapezium line; intro reshuffled | text reads right ("the 2 angles on one slanting side add to 180"); Try 54: 180 - 108 = 72 right | n/a | **Fixed** |
| U8 S01, S05 | brief says "labels fixed" | **No data or tool change since round 3.** S01 (p. 56): the arc is one circle round O, (a) (b) (c) are clear of it but cannot be matched to arcs; S05 (p. 57) is unchanged | n/a | **Not changed** (Low, still S5 of round 3; README does not claim it) |
| U9 Learn | marks line reworded | "costs its marks plus the penalty" true; cars and bikes example 5 vehicles, 14 wheels: 10 wheels, 4 short, 2 cars right | n/a | **Fixed** |
| U10 S12 | wording | tens digit t has t choices of ones digit: 1 + ... + 9 = 45 right; wording clear | n/a | **Fixed** |

## Whys, answers, pages (re-check after the soft copy went from 99 to 100 pages)

| Check | Print vector | Soft copy |
|---|---|---|
| Why equals the data explanation, in order | 244 / 244 | 244 / 244 |
| Printed answer equals the data answer | 244 / 244 | 244 / 244 |
| Printed "page N" equals unit start + item page | 244 / 244 | 244 / 244 |
| Question text found on that page of the PDF | 242 / 244 (2 by image) | 242 / 244 (2 by image) |
| Unit answer pages 80 to 98 as on the Contents | yes | yes |
| Pages | 100 (p. 78 blank) | 100 (p. 78 blank) |

The earlier soft copy of 99 pages lost p. 100; both editions are now the same length and layout.

## Must fix before sale

- **N1. U4 S01(b)** is the holiday's 15-20-25 triangle with height 12 and area 150. Change (b) to a triangle that is not 15-20-25 (for example height 15 with slants 17 and 25: base 8 + 20 = 28, area 210). Rederive key 150, the Why, and the figure labels.
- **N2. U7 G01** is the holiday's $200 bicycle with +10%, with $220 as the first step. Change the object and numbers (for example a $60 game console up 25% then 20%: $75, $90, 50%; or a population of 800 up 50% then 10%) and rewrite the Why, hint, Beyond label if needed.
- **N3. U3 S12** has the holiday's $36, 10 units, $12 unit and $120 total. Change the numbers (for example shirt 1/4, $30 shoes, 1/3 left, whole = 1 - 1/4 - 1/3 = 5/12 = $30: 1/12 = $6, $72) and the Why.
- **N7. README line 72** says "soft copy 99"; the soft copy is 100 pages (README and PROGRESS "Resume" line say 99; PROGRESS round-3 line is right). README line 50 ("items whose story, question and numbers matched a holiday item were replaced") is true only after N1 to N3.

## Should fix (Low)

- **N4.** U7 T03 keeps the holiday frame (added percentage in a total, find the added part). If the owner policy needs a new frame: give the food cost and ask for the total, or give the charge and ask for the food cost with a rate that is not 10%.
- **N5.** U5 T03 shares the answer 8 cm and the depth 24 with holiday l5.js 152, and its method (spread over the joined floor) with T02 on the same page. Change the water depth or the part lengths so the answer is not 8 (for example parts 20 cm and 40 cm, depth 18: 18 x 20 x 40 / 2400 = 6).
- **N6.** U5 G03 is very easy for a Go further page; consider 27 times and edge 4 (answer 12), or ask for the surface area ratio.
- **N8.** U4 S04 and S06 are the same figure skeleton on adjacent pages; U7 T01 and G01 share the hint idea. Low.
- **N9.** U8 S01 arcs run together; label placement not improved (as in round 3 S5).

## Other checks

| Check | Result |
|---|---|
| README round-3 section | True: S01 18 and 25, S06 16 by 9, S09 m and cm, G03 cubes, T03 wall, U6 T03 fuel, U7 S13, T03, G01, G02, U8 C01, U3 S12, Check yourself 3 no hatch, equilateral and trapezium lines, marks line, "greater than". README Beyond table matches the 15 Beyond badges (U2 G1, G4; U7 T2, T3, G1, G2 ...). |
| README other lines | Line 72 "soft copy 99" is false (N7). Line 106 (round 2 section) still says U7 T03 is the 9% GST item; it is history, superseded by round 3. |
| Beyond badges | 15 in the PDF (was 14: U7 G02 "Boiling away" added), all in README, none in Start here. |
| Welcome, cover, plaque, certificate | unchanged and right; "with new numbers and stories" is true except N1 to N3. |
| 1-bit zoom (changed pages) | Legible, lines continuous, no moire: U4 S01, S06, C01, C03; U5 T03; U8 C01. Small halo gaps where labels cross lines (S01, C01, S06) are readable. |
| Known leftovers | "DRAFT licence text, for owner and lawyer approval" on p. 2 and the temporary contact email (owner decisions). |

## Note on the working tree

`git status` shows modified files under `term/l1/` that are not mine and were not touched. Nothing in `extension/`, `outputs/` or `p5/` was edited; the only file written is this one.
