# Fixes applied for the P2 audit (docs/audit/audit_p2.md)

Nothing committed or published. Shared files (rebuild/slidekit.py, hp/*, levels/*) were NOT edited.

## Retimed 90-minute plan (issue 4, all lessons)
warm-up 0-8 (warm1 0-5, warm2 5-8); explore 8-20 (explore2 talk 14-20); teaching 20-32; brain break 32-36; page 1 36-50 (Lessons 5, 6, 10 have a short teach slide first, 36-38); check 50-52; short teaching 52-57; page 2 57-69; check 69-72; talk 72-80; exit 80-90 (Lesson 10: 80-88 + certificates 88-90). Applied to every slide label and "Minutes a to b" note in rebuild/gen_p2l1..10.py, the title-slide time plans, the break notes ("Four minutes"), p2/guide.js (routine table, per-lesson scripts, "Prepare" list).

## Per issue
- 1 applied. L10: four station-card slides (p2l10-card1..4, checked cards from the audit), explore1 and notes rewritten (one card per breakout pair, 3 min, swap), materials/online/explore text, new `deck.stationCards` printed in the tutor guide. Answers re-verified in Python (50; Ali cat/Cai dog; exactly 2 coin ways; 3/8).
- 2 applied. L8: kit page "Cube nets" (nets A-F, dashed cut / solid fold) in p2/kit.js; workbook Q5 (dice net) deleted (it stays as Think Harder challenge 9); Q4 = cut out and fold; Q3 wording replaced; key, slides (ws2, ws2ans, teachnet, trynet, title notes) updated. Nets A,C,E fold and Q4b has exactly 4 places: verified by a cube-rolling simulation. Stack C kept on page 2.
- 3 applied. L5: Q6 moved to Think Harder (now stretch item 4, prints on the workbook), old "26 marbles" stretch item removed, Q1-Q5 kept, Q2b hint kept; teachthree slide moved after ws2ans as an early-finisher slide; page-2 slot is now 12 minutes.
- 4 applied (see plan above).
- 5 applied. L2 Q5 tiles centred under both triangles with caption, new text and (a)/(b) wording. Triangle totals checked (corners 110-130 for 390, 140-160 for 420).
- 6 applied. L9 clock: hour hand navy short thick, minute hand red long thin ending at the marks, numerals moved outside the ring, legend caption, Q5 hint; kit clock hands recoloured to match.
- 7 applied. L6 warm-up: 60c / 85c, answer 25c (content and slide).
- 8 applied. L3: Q6 table widened to rows 2-10 plus stop sentence; tricycle redrawn with two side-by-side rear wheels; Q7a accepted wording in key. Q6 and Q7 answers re-checked.
- 9 applied. L1 stretch item and teachchart slide reworded (directly below/above; 505, 491, 306, 271 re-checked).
- 10 applied with one deviation. L10 Q6 replaced by towers of cubes, but with 4, 8, 12 cubes (Tower 8 = 32, 36 cubes = Tower 9) instead of 3, 6, 9, because the audit's version (Tower 10, adds 3) would duplicate the Lesson 4 challenge towers item. Key, ws2, ws2ans, teachgrow notes updated.
- 11 applied. L1 brain break rewritten (digit cards in a row, swap, show on camera), slide and content.
- 12 applied without touching hp/kit.js: p2/kit.js adds a "Two spare $1 coins" block (8 in total), lists contents, "keep spare coins"; digit cards label now "Lessons 1 and 10". The "cube strips" page is relabelled as paper strips of numbered squares (Lesson 9).
- 13 applied. L7 Q6 hint added; notes/key say equivalent fractions are P3 and shown with bars only; qbank challenge item and slide notes flagged.
- 14 applied. L9 materials/online: two cups/bottles, rice or sand, tape marks at 3 and 5, ruler-on-pencil backup (content and title notes).
- 15 applied. L2 stretch eggs: 260 in the afternoon, answer 300 (905 - 605).
- 16 partly applied. Removed the forced page breaks before Q4 in L1 and L2; L2 is 3 pages (was 4), L1 stays at 3. L9 and L10 stayed at 2 pages after the changes (Q3 table 4 rows, smaller figures). Workbook is 52 pages.
- 17 applied. L8 qbank core[3] reworded ("ALL sizes").
- 18 applied. L4 Q6 uses 1 to 36; key updated (12 and 9 numbers; both 12, 24, 36 re-checked).
- 19 applied. L7 key note that F is the hardest.
- 20 applied differently: parent_pack_level.py unpacks exactly 3 fields, so the "Before class" list is appended to the tip text in p2/parent_side.json for each lesson.
- 21 skipped (Low, design change: splitting p2l9-we2 and p2l5-teachrule; no defect).
- 22 nothing to do.
- Per-lesson notes also applied: L2 Q3d wording "Explain how you know without adding"; L3 title notes and lesson.mini say not to write remainders as "r".

## Files changed
p2/content/l1,l2,l3,l4,l5,l6,l7,l8,l9,l10.js; p2/kit.js; p2/guide.js; p2/parent_side.json; rebuild/gen_p2l1..gen_p2l10.py. Regenerated: p2l1..p2l10 (all ten deck keys), restyled with levels/restyle.py, then `bash levels/build_level.sh 2` (workbook 52 pages, tutor guide 63, weekly dose 24). Slide counts: 25,26,26,25,26,26,27,27,26,31. No slide overflows, no font under 24px, no slide over 200 elements.
