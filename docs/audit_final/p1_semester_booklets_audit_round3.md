# Independent re-audit, round 3: Primary 1 early-finisher booklets, Semester 1 and Semester 2

Auditor: fresh independent checker, 23 Oct 2026, branch `claude/great-fermi-1hv4vc` (commit 061c951). Only this report was added. Scope: only what round 2 changed. `validate.py` was not run (it can rewrite `school/p1`); everything below was read from the PDFs in `school/p1/out`.

Method: each changed page rendered at 130 dpi (viewed), 300 dpi (measured) and 100 and 150 dpi 1-bit (`pdftoppm -mono`); every page solved by hand from the image, then compared with the key text (`pdftotext` of the answer-key PDFs) and with the code table printed on the page. Code words tested against my own dictionary (web2 + gcide + wordfreq top 150 000): all anagrams, and every single-slot change to any letter in that page's own table (a superset of any wrong answer), plus leaving one box blank.

## Verdicts

| Booklet | Verdict |
|---|---|
| Semester 1 | READY for printing once the owner items (cover publisher line, licence wording and term for a lawyer) are settled. No High or Medium findings. |
| Semester 2 | READY for printing once the same owner items are settled. One Medium (S2-01 code-table letters touch the box edges), advised not blocking. |

## 1. Hand-solve of the changed pages (all agree with key and table)

| Page | My answer from the image | Key | Result |
|---|---|---|---|
| S1-04 (P1-12) | 17 parts: circle 4 (R), ellipse 4 (R), roof top 3 (Y), roof halves 4 + 4 (R, R), round-top halves 7 + 7 (G, G), tall rectangle 8 (O), windows 3 (Y), 8 (O), 3 (Y), door 7 (G), 8 (O), 8 (O), base 6, 6, 6 (B). Tally Y3 R4 B3 G3 O4. | same | agrees. Doorknob is gone from the door (viewed at 130 dpi and in 1-bit). Marks agree: dot on 3 orange parts only, star on 2 green, square on 2 yellow, triangle on 2 red, plus on 3 blue, crescent on 2 red. Unique. |
| S1-01 (P1-25) | boats 7, balls 10, cats 15 (full ten frame + 5), 6 - 5 = 1 more, 5 - 2 = 3 fewer: C L O T H = CLOTH | same | unique |
| S1-10 (P1-21) | 6, 5, 12, 2, 3, 14: M O N K E Y | same (key shows 3 + 3 = 6 etc.) | unique; table has 8 boxes (0, 1, 2, 3, 5, 6, 12, 14) |
| S1-20 (P1-13) | 4 x 4 = 16, 3 x 2 = 6, 3 x 3 = 9, 4 x 3 = 12, 2 x 5 = 10, 4 x 2 = 8: N U M B E R | same | unique |
| S2-01 (P1-03) | 8 / 2 = 4, 12 in 2s = 6, 16 / 2 = 8, 6 in 2s = 3, 6 / 3 = 2, 10 in 2s = 5: S H A D O W | same | object counts verified by eye (8, 12, 16, 6, 6, 10) |
| S2-02 (P1-39) | 12 / 2 = 6, 14 / 2 = 7, 8 / 4 = 2, 8 apples between 2 children = 4, 9 stars among 3 = 3, 10 in 2s = 5: S P O N G E | same | unique; "The sharer gets a share too." is an instruction at the top |
| S2-04 (P1-05) | 3 x 4 = 12, 3 groups of 2 = 6, 3 x ? = 15 so 5, ? x 4 = 8 so 2, 3 groups of 3 = 9, 2 x 2 = 4: S Q U A R E | same | each picture has the right count (12, 6, 15, 8, 9, 4); unique |
| S2-11 (P1-28) | 70c = 50 + 20 = 2 coins, 35c = 20 + 10 + 5 = 3, 45 / 5 = 9, 40 / 10 = 4, purses 20c, 30c, 25c, 50c so 1 tick: S T A M P | same | unique |
| S2-20 (P1-22) | 43 then 35; 16 then 14; 4 then 7; 14 then 13; 85 then 83; 12 then 9. Last boxes 35, 14, 7, 13, 83, 9: G U I T A R | same | unique. Instruction "Code table: use the last box." is present. A pupil who uses story 4's first box (14 = U) gets GUIUAR, not a word. |

## 2. Code words

- Every code word is a real word and has exactly one arrangement: the only anagram in my dictionary is UGARIT for GUITAR (obscure, not a word a child would form). No anagram exists for the other seven.
- Single wrong letter (any letter from that page's own table in any slot): no word on any page. The only hits are rare or name forms: STAMM and STAPP (S2-11, zipf about 2, not common words). Not a risk.
- Leaving one box blank (no letter) gives a word in two cases: MONEY from MONKEY (S1-10, 5 letters) and CLOT from CLOTH (S1-01, 4 letters). See L2.
- Each wrong-operation answer I tried (for example S1-10 story 4: 6 + 4 = 10, no letter; S2-04 3 x 4 read as 3 + 4 = 7 gives X) gives a letter string that is not a word.

## 3. Object size (300 dpi pixel measurement, bounding boxes)

Every counted picture measures 8.0 mm or more in both directions: apples 8.0 x 9.0, stars 8.1 x 8.1, balls 8.1 x 8.1, cats 8.5 x 8.0, drums 8.2 x 8.0, boats 8.9 x 8.0, flowers 8.0 x 10.4 (S1-10), car 12.4 x 8.1 and bird 12.7 x 8.0 (S2-02 facts). Smaller things measured (7.4 to 7.7 mm) are the question-number circles, not counted objects. The claim "at least 8 mm in both directions" is true, but with no margin (several are 8.0 to 8.1). No counted object is clipped by its box or page edge.

## 4. Findings

### High
None.

### Medium

**M1. S2-01 (P1-03): code-table letters still touch the box edges.** Nine boxes: the "11" touches the left edge and the "L" the right edge of box 9; the digits of "2", "5" and "9" touch the left border and the neighbour gap is under 1 mm. All still readable, but the round-2 report says letters no longer touch edges. S1-10 (eight boxes) is now clean; S1-20 ("10", "12", "16", "N") and S2-04 are tight but inside; S2-11 and S2-20 are fine. Fix: drop the decoy 9 = P or 11 = L from S2-01 (eight boxes), or reduce the digit size.

### Low

**L1. Dashed grouping rings overlap the next picture (S2-01 rows 2, 4, 6).** The ring around the first two drums or stars touches the third. Counts still read correctly; widen the gap by 1 mm if the page is regenerated.

**L2. Blank-box words.** A pupil who leaves a box empty because a wrong answer had no letter reads MONEY (S1-10) or CLOT (S1-01) in the remaining boxes. The notes' claim "the wrong operation never spells the word" holds for a filled box only. Add "every box gets a letter" to the notes, or ignore.

**L3. S1-04 small marks are small.** The star and crescent marks are about 2.5 to 3 mm and the crescent at the foot of the left circle sits close to the edge; the 1-bit render keeps all of them intact.

**L4. Contents lists codes and titles only.** No page numbers exist for pupil pages other than the footer code; the key says "KEY page n of N". Nothing to fix; stated for the check item.

## 5. Front matter, footers and structure

- Pupil footers (all 20 pages of each booklet): "(c) 2026 Preciouslyours Pte Ltd. Photocopy licence. School (write name): ____ only. Not for resale." with the page code on the right.
- Licence page: "Licensed to: ____ (one school, one campus)", and the notes sentence "The school name is written on the line marked School (write name) at the foot of each page, by hand or when the booklet is made." matches the footer. Final line "(c) 2026 Preciouslyours Pte Ltd." Registered office "66 Tannery Ln, Singapore 347805" is present in both booklets. The MOE not-affiliated sentence is on the licence page.
- DRAFT: cover, licence heading, teacher notes in both booklets; both keys carry DRAFT on page 1 (the key text shows DRAFT twice). Pupil pages carry none (correct).
- Contact email pypteltd@gmail.com is on cover, licence, notes and each key. Cover publisher line remains "[Publisher line: wording to be confirmed by the owner]": owner item.
- Key pages read "KEY page n of 10" (S1) and "of 9" (S2), each with the "Teacher answer key: not for pupils, not for resale" line and the (c) line; the S1 key has 10 entries after the front note, S2 has 9.
- Page counts: Puzzles 20 and 20, FrontMatter 5 and 5, Complete Pack 25 and 25, Key 10 and 9.
- Contents rows match the footer codes (S1-01 P1-25 ... S1-20 P1-13); syllabus coverage lists unchanged since round 2.

## 6. Photocopy (1-bit)

All 15 changed pupil pages are pure black and white (no colour pixels). `pdftoppm -mono` renders show no ink loss (mono ink is 1 to 27 percent more than the threshold render; no missing strokes). S1-04 viewed in 1-bit: every part, the thick answer lines, the marks and the check strip are intact.

## 7. Remaining owner items (not defects)

Cover publisher line; licence wording and term (lawyer); the one-school licence line "Licensed to" versus the footer line (both exist and agree in meaning); pupil trial of P1-39 star level and the P1-31 trap.
