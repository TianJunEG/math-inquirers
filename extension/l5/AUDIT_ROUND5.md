# Independent audit, round 5: Level 5 Extension Workbook

Audited 23 Oct 2026, fresh session, branch claude/great-fermi-1hv4vc, HEAD 311b707. Report only: nothing in the book, data, tools or docs was edited; no push, no PR. This file is the only thing written.

Checked: `outputs/extension/L5/` print (100 pp, 1-bit 600 dpi), print vector (100 pp), soft copy (99 pp), `build_report.json` (0 problems, soft 99, print 100, 0 B/W failures); `extension/data/l5_u01..u10.json` diffed against d7b67a6 (the data audited in round 4) to HEAD; holiday text `p3/content`, `p4/content`, `p5/content`; `README.md`, `PROGRESS.md`, `AUDIT_ROUND4.md`. `run_checks.py --level 5`: 417 answers OK.

## Diff since round 4 (d7b67a6 to HEAD)

Data files changed: `l5_u03` (1 item), `l5_u04` (1), `l5_u05` (1), `l5_u07` (1), `l5_u08` (2 figures, label geometry only). Verify scripts changed to match (u03, u04, u05, u07). `extension/tools`: **no change** (see note on the "keep flag" below). Docs: PROGRESS.md (round-4 line), README.md (line 72, soft 99). u01, u02, u06, u09, u10 unchanged. So 6 changed entries: U3 S12, U4 S01, U5 T03, U7 G01, U8 S01, U8 S05.

## Per-item table

Maths = hand solved from the page (print PDF), then compared with the key and the Why on the answer page.

| Item | Change | Hand solution | Key / Why | Frame vs holiday P3/P4/P5 | Status |
|---|---|---|---|---|---|
| U3 S12 (p. 23, no. 12) | Mei: 3/10 on a toy, $27 on stickers, 1/4 left, started with $60 | 1 - 3/10 - 1/4 = 9/20 = $27; 1/20 = $3; 20 units = $60. Check: toy $18, stickers $27, left $15, total $60 | Key $60 right. Why "Toy 3/10 and left 1/4 make 11/20. So the $27 stickers are 9/20. 1/20 = $3, so $60" right and matches the question | Round-4 problem ($36, $12 unit, $120, Ravi 2/5 game) is gone. Read p5 l2.js 63/165 and l3.js 53/66/81/95/101/127, p4 l3.js 146, p3 l4.js 70/139. New numbers 3/10, 1/4, $27, $60 do not form a holiday item. Residue: **Mei with $27 is the "$27 left" of holiday l3.js 66 and 81 (Mei, 2/5 bag, 1/2 of remainder, $90)**, which is the same lesson this unit follows; the holiday $60 is a different item (l3.js 95, Siti). Frame differs (here the middle part is given and the rest is a fraction of the whole) | **Fixed** (Low: shared name and $27 with l3.js 66/81; if wanted, change $27 and the whole, e.g. $45 stickers, 1/4 left, $100) |
| U4 S01 (p. 28, no. 1) | (b) now base 36, height 20, slants 25 and 29, area 360; figure mm 2.5 to 1.8 | (a) 1/2 x 18 x 12 = 108. (b) 1/2 x 36 x 20 = 360. Geometry check: foot splits 36 into 15 + 21 (25 squared minus 20 squared = 225, 29 squared minus 20 squared = 441), so the labelled slants 25 and 29 are consistent with base 36 and height 20 | Keys 108 and 360 right. Why "(b) 1/2 x 36 x 20 = 360" right | Holiday triangles read in l4.js (13-14-15, 5-12-13, 15-20-25 at 151/206, 12-16-20 at 136/195, 11 with 13 and 20 at 115, 9-8-17) and p4 l7.js: no 25-29-36 triangle, no area 360, no height 20 with a 36 base. The holiday 15-20-25 triangle (area 150) is gone | **Fixed** (N1 closed). Low: slants 25 and 29 are not quite "the 20-21-29 triple" visible to a child; fine |
| U5 T03 (p. 38, no. 3) | water 18 cm deep, answer 6 cm | 20 x 40 x 18 = 14 400 cm3; joined floor 60 x 40 = 2400; 14 400 / 2400 = 6 cm | Key 6 cm right. Why "Water 20 x 40 x 18 = 14 400 cm3 ... 6 cm" right; hint unchanged and fine | Holiday l5.js 152 (container A 24 high, answer 8) no longer shares depth or answer. Holiday l5.js 61/62/186 has a different tank (50 x 30 x 40) with water 18 cm deep, a volume-and-litres question, so only the figure 18 repeats. No holiday item with a divider wall (searched wall, divid, partition, spreads) | **Fixed** (N5 closed). Low: T02 on the same page (tank A 24 cm deep, pour into B) is the same pooling idea; verify script comment now says `depth < 18` (correct) |
| U7 G01 (p. 53, no. 1) | school choir of 40 singers up 25%, a year later the new number up another 20%; (a) singers now, (b) total rise as % of 40 | 40 + 10 = 50; 50 + 10 = 60 singers. Rise 20 out of 40 = 50% | Keys 60 and 50 right. Why "(a) 40 + 10 = 50, then 50 + 10 = 60. (b) 20 out of 40 = 50%" right; hint "Take the second rise from the new number" right | The $200 bicycle (l7.js 43/63/79) is gone; $220/$242/21% gone. Remaining closeness: **holiday l7.js 48 (extension: "raises every price by 25%, then 20% off", try $40, $100, $64) and l7.js 138-141 (Siti, $80 up 25% then down 20%)** use the same 25% and 20% pair, with 40 as one of the starting values. Direction (up then up), object and answers differ | **Fixed** (N2 closed). Low: same percentage pair and "percentage of the new amount" frame as the 25%/20% holiday items; a 20% then 10% pair would remove it. Hint idea still shared with U7 T01 (page before) |
| U8 S01 (p. 56, no. 1) | labels (a), (b), (c) moved (tr 40 to 58 and 62) | not changed in maths: AOC = 60, BOC = 120, BOD = 60 (BOC twice AOC, AOC + BOC = 180) | unchanged, right | none | **Label placement improved, readable.** At 300 dpi 1-bit each label sits clear of the arc and lines, next to its own sector ((a) upper right, (b) upper left, (c) lower left), so matching works by position. The three arcs still read as one circle round O (no break between sectors), but nothing is hidden. Low |
| U8 S05 (p. 57, no. 5) | labels (a), (b) at the B and C corners (r 24 to 26, tr 40 to 56) | not changed: B = 110, C = 70 | unchanged, right | none | **Regression, must fix (N10).** The two labels now land on top of each other in the middle of the parallelogram: the page shows "(c(b)" in both editions, (a) is hidden under (b), and neither can be matched to a corner. Previously (b) and (a) were stacked and separate. Cause: BC is only about 20 mm long and `tr` 56 for both corners puts both labels at the same spot. Fix: move (a) next to B (or give B and C different `tr`) and re-check at 300 dpi |

## Things the brief said that I could not confirm

- "small_labels 'keep' flag": there is no such flag in `extension/tools` (grep `small_labels`, `keep`), and `extension/tools` has no commit since the round-4 audit. The S01/S05 change is just new `r` and `tr` numbers in `l5_u08.json`. It works for S01 and fails for S05. PROGRESS.md (round-4 line) says "labels really spaced (keep flag)": that sentence is not accurate for S05.
- U8 S08 (p. 57, no. 8): "(d)" is crossed by the angle arc and tick marks near C. Not changed this round, readable, Low.

## Scale and 1-bit legibility, U4 S01

At 1.8 mm per unit: (a) base 18 = 32 mm, (b) base 36 = 65 mm, height 20 = 36 mm. Measured on the 150 dpi page and the 300 dpi crop: base ratio 2:1 and heights 12:20 hold; the two triangles fit side by side in the figure area with a clear gap; lines are continuous, dashes and right-angle marks clear, "25 cm", "29 cm", "20 cm", "36 cm" legible (halo gap where "25 cm" and "29 cm" touch the slants). "12 cm" and "15 cm" in (a) still touch the right slant with a halo gap (as in round 4). Larger text than in round 4 would not hurt (labels about 9 pt in the small triangle), but it reads. **Pass.**

## Soft copy 99 pages: by design

Page-by-page text of print vector against soft copy, pages 1 to 99: identical apart from the licence line ("printed book" / "soft copy") and where the page number sits in the text stream (left or right of the footer). Print page 100 is an empty page (no text; the 40 dpi render is pure white, no footer, no page number); the soft copy has no page 100. Content ends on p. 99 in both (answers for U10 Check yourself 1 to 4 on p. 99; the cover is page 1, p. 78 is a blank page inside both). So the soft copy lacks only the closing blank page that pads the print book to 100 (even). Round 4 had the answers run to p. 100; they now end on p. 99 because the Why lines changed by about a line. No section moved: unit starts and unit answer starts are unchanged. build_report.json says soft 99, print 100, consistent with README line 72, PROGRESS line 21 and the new PROGRESS line.

## Contents, answer pages, Whys

| Check | Print vector | Soft copy |
|---|---|---|
| Contents page 4: unit starts 6, 13, 20, 27, 34, 41, 48, 55, 62, 69 and "answers on page" 80, 82, 84, 86, 88, 90, 92, 94, 96, 98; progress 76, certificate 77, answers 79 | right | right |
| Each unit start page carries "Learn it" and the right unit title | 10 / 10 | 10 / 10 |
| Each unit answer page (80 to 98) shows the right unit title | 10 / 10 | 10 / 10 |
| Pace plan page numbers (page 5) agree with the units | yes | yes |
| Why on the answer page equals the data explanation, in book order | 244 / 244 | 244 / 244 |
| "page N" printed with each answer equals unit start + item page (U1 S06, S07 and U8 S12 have wrapped answers and were read by eye: pages 8, 8, 58 right) | 244 / 244 | 244 / 244 |
| Printed answer line of the 5 changed items | U3 S12 $60 (checked on p. 85 area), U4 S01 "(a) 108 (b) 360" p. 28, U5 T03 "6 cm" p. 38, U7 G01 and U8 S01/S05 as before | same |

Whys of the five changed items were read in full against the printed questions: all match. No stale Why remains (searched for 2/5, $36, $120, bike, 25 cm, 150, 24 cm, 8 cm in the answer pages: none from the old versions).

## Stale documentation (small)

- **README line 111** (round-3 section) still says "unit 4 S01 (triangles 18 by 12 and 25 by 12)"; the item is now 18 by 12 and 36 by 20. README line 103 and 112 are history and fine. README line 50 says "After three audit rounds"; there are now four (PROGRESS has the round-4 line). The README Beyond table is unchanged and still right (G01 keeps "Two rises in a row").
- PROGRESS "Resume" line says print 100, soft 99: correct.

## Verdict

**Not yet sell-ready, one small fix away.** All five content items from round 4 (U4 S01(b), U7 G01, U3 S12, U5 T03, plus the N7 page-count line) are fixed: keys and Whys are right, no key numbers are shared with the holiday items that were flagged (the 15-20-25 triangle, the $200 bicycle, the $36/$120 item, the 8 cm tank answer). Contents, answer pages, pace plan, 244 of 244 Whys and page references, print/soft parity (99 + one blank page) all pass.

What blocks:

1. **N10, U8 S05 (page 57, no. 5): labels (a) and (b) overprint** ("(c(b)"), so (a) cannot be read. This is new in this build (caused by the `tr` 40 to 56 change) and is in both editions. About 10 minutes: separate the two `tr` values, rebuild, check at 300 dpi.
2. README line 111 (U4 S01 numbers) and "three audit rounds" in line 50 are stale. 2 minutes.

Optional (Low, no sale impact): U3 S12 Mei and $27 repeat the holiday l3.js 66/81 numbers (different item); U7 G01 uses the same 25% and 20% pair as the holiday l7.js 48/141 items; U8 S01 arcs look like one circle; U8 S08 "(d)" is crossed by the arc; U5 T03 and T02 share the pooling idea; U7 T03 (added service charge) is still the holiday's total-includes-percentage frame (round-4 N4, not changed, Low).

Not done: no child trial, no printer proof, soft copy compared as text and a spot render (p. 57) only, real-world checks (licence text, contact email) left to the owner.
