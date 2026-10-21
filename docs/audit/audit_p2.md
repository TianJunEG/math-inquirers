# Audit: Math Inquirers P2 Holiday Program (suitability and difficulty)

Scope: `p2/content/l1.js` to `l10.js`, `p2/data.js`, `p2/kit.js`, the rendered `p2/Math_Inquirers_P2_Student_Workbook_Designed.pdf`, and all 261 slides in `split/p2l1` to `split/p2l10`. Audience: children aged 8 to 9 finishing Primary 2, online, groups of 8, 10 lessons of 90 minutes, leading into P3.
Read-only audit. No content file was edited and nothing was committed.

## 1. Method (what was actually checked)

- Every answer in every `lesson.key`, `qbank` (core, stretch, challenge), deck example, slide "your turn" and slide notes was recomputed. "Find all" items and logic items were brute-forced in Python (digit-card lists, digit-sum counts, coin sets, sub-set sums, jug-pouring BFS, magic square/triangle totals, cube-net folding by rolling a cube, 3-digit missing-digit sums). Figures were checked by rendering the workbook PDF and reading the SVG source.
- Result: **no wrong final answer was found** in the keys, the question bank, or the slides. All "exactly one solution" claims hold. The issues below are about ambiguity, a few figures, level and difficulty, timing, missing materials, and one syllabus-rule slip.
- Syllabus reference: MOE P2 and P3 Mathematics handbooks (shuqunpri.moe.edu.sg P2_Math_Handbook_2025 and P3_Math_Handbook_2025). P2 lists: numbers to 1000, add/subtract, multiply/divide within the tables, shapes (cube, cuboid, cone, cylinder, sphere; semicircle, quarter circle), time, picture graphs with scales, fractions (part of a whole, compare unit and like fractions, add/subtract like fractions within one whole, denominators up to 12). P3 lists: division with remainder, equivalent fractions, money in decimal notation, duration of time, tables of 6 to 9. Nets are not in either handbook.
- Program rules in `p2/SPEC.md` (no 6 to 9 tables, nothing above 1000, no decimals except money) are respected everywhere. No "✗" character anywhere, no slide font under 24px (261 slides scanned), no slide over 200 elements.

## 2. Summary table

| Lesson | Verdict | One-line reason |
|---|---|---|
| 1 Digit Detectives | minor fix | On syllabus and well pitched. Fix "just below/above" wording, the "Human number" break (cannot be done online) and a tight page-2 time slot. |
| 2 Missing Digit Mysteries | minor fix | On syllabus. Magic-triangle figure (Q5) misleads; the workbook runs to 4 pages with big blank areas; Q5 and Q6 are heavy for a 7-minute slot; one stretch item has a coincidental answer. |
| 3 Legs, Wheels and Arrays | minor fix | Good lesson. Division with remainder is P3 content (acceptable, but label it); Q6 table too short; tricycle picture shows 2 wheels; page-2 slot far too short for Q4 to Q7. |
| 4 Pattern Machines | minor fix | Pitched well. Q6 asks for two long lists; Q5 is repeated verbatim in lesson 10; page 2 is tight. |
| 5 Mystery Number Machines | needs rework | Heaviest reading and reasoning load of the program; only 6 minutes for Q3 to Q6 (four multi-step problems); Q2b rule-finding and "unknown equal bar" problems exceed core. |
| 6 Market Day | minor fix | Handles the P2 money rule well. One warm-up question breaks its own "dollars only or cents only" rule; play-money supply too small for Q2; page 2 tight. |
| 7 Fair Shares | minor fix | Squarely on syllabus. Q6 and one slide use equivalent fractions (1/4 = 2/8), a P3 idea; shape F in Q1 is a hard judgement. |
| 8 Shape Builders | needs rework | Cube nets (Q4, Q5) and hidden-cube stack C are well above P2; kit has no net cut-outs although the lesson says there are; four teaching slides in 6 minutes. |
| 9 Measure Masters | minor fix | Content right for the level. Clock figure is hard to read and its hand colours contradict the paper clock in the kit; jug puzzles need props; page-2 slot far too short. |
| 10 Challenge Day | needs rework | The 15-minute "Explore" depends on four station cards that exist nowhere in the deck, workbook or kit. Q6 repeats lesson 4 Q5. |

Cross-cutting: the "Worksheet page 2" slot is 6 to 8 minutes in nine of ten lessons (see section 4). That is the biggest delivery risk in the program.

## 3. Numbered issues, ranked by severity

### High

**1. Lesson 10: Explore has no content (blocking).**
Files: `p2/content/l10.js` (`lesson.explore`, `deck.expSetup`, `materials`), slide `split/p2l10/project/slides/p2l10-explore1.html`, `p2/kit.js`.
Problem: The explore (10 to 25 minutes) says "Four station cards: a picture graph, a logic grid, a coin puzzle and a fraction strip", and `materials` lists "Puzzle cards for 4 stations". The slide only shows an icon picture. No card text exists in the deck, the workbook, the kit or the tutor guide. A tutor cannot run this, and 8-year-olds in breakout rooms cannot read an icon.
Fix: add one slide per card (or a kit page) with these checked cards:
- Card 1 (picture graph): "Each ● stands for 5 books. Monday ●●●, Tuesday ●●●●●, Wednesday ●●. How many books were read on these 3 days?" Answer 50 (10 pictures x 5).
- Card 2 (logic grid): "Ali, Ben and Cai each have one pet: a cat, a dog or a fish. Ben has the fish. Ali does not have the dog. Who has the cat?" Answer: Ali has the cat, Cai the dog.
- Card 3 (coins): "Make 70¢ with exactly 4 coins. You can use 5¢, 10¢, 20¢ and 50¢ coins. Find all the ways." Answer 2 ways: 50¢ + 10¢ + 5¢ + 5¢, and 20¢ + 20¢ + 20¢ + 10¢ (brute-forced).
- Card 4 (fraction strip): "A strip is cut into 8 equal parts. 3 parts are red and 2 parts are blue. What fraction is NOT coloured?" Answer 3/8.
Also change the plan to "one card per breakout pair, 3 minutes each, then swap on the slide" because a tutor cannot visit four physical stations online.

**2. Lesson 8: Page 2 is above the level, kit has no nets.**
Files: `l8.js` Q4, Q5 (and `lesson.online`: "nets are printed from the back of the workbook"), `p2/kit.js`.
Problem: Folding six hexomino nets in the head (Q4) and the dice-net numbering (Q5) are not P2 content (nets are not in the MOE P1 to P3 handbooks); mentally folding 2-2-2, 1-4-1 and 4-row nets is routinely hard for P4 children. `kit.js` has no net cut-outs, and its "Paper cube strips" page is labelled Lesson 9 but is a strip of numbered cells, not cubes or nets. Slide time for cubes + nets teaching is 52 to 58 (4 slides in 6 minutes), then 9 minutes for Q3 to Q5.
Fix: (a) add a kit page with the six nets A to F (cut-out, same size as the figure) and say "Cut out each net and try folding it". (b) Delete workbook Q5 (dice net). Its idea is already on the Think Harder page as challenge[8] ("1, 2, 3 on a dice, what is hidden?"). (c) Keep Q4 as "Cut out and fold, then circle the ones that make a cube" (answer A, C, E, verified by simulation; Q4b has exactly four valid places, also verified). (d) In Q3, replace "and there are no gaps at the back" with "Every cube is on the table or sits on top of another cube. Stack A is only 1 cube deep." (the phrase "no gaps at the back" is not clear to an 8-year-old). Stack C (answer 14) stays but belongs in a Think Harder spot if time is short.

**3. Lesson 5: too heavy for the slot, several items above core.**
Files: `l5.js` workbook Q2b, Q5, Q6; slide timings.
Problem: 367 workbook words (the most in the program); Page 2 (62 to 68, 6 minutes) holds Q3 (before-and-after bars), Q4 (equal bars, an unknown part), Q5 (four sub-questions about order) and Q6 (three-person take-away-extras problem). Q2b asks children to find "x a number then + a number" from two pairs, which is guess-and-test algebra. Core bank items [3] and [4] (two-step reverse) are the whole point of the lesson, so they are not "almost every child" items on the first day.
Fix: keep Q1 to Q5. Move Q6 to Think Harder and swap out stretch[5] (Ali and Ben, 26 marbles), which is the same idea in smaller numbers. Keep Q2b but add the hint line already on the slide: "Try ×2, ×3, ×4 with IN 2. Test the answer with IN 5" (it is already in Q2b; keep it). Re-time per section 4.

**4. Page-2 slot is too short in nine lessons (see section 4 table).**
All `split/p2lN/project/slides/p2lN-ws2.html` and the title-slide notes. Fix: use the re-time in section 4. Without it, children will not finish page 2 and the check-together slide will be rushed or skipped.

### Medium

**5. Lesson 2 Q5: figure suggests only 3 numbers per triangle.**
File: `l2.js` (lines 50 to 55 and the `H.q(5, ...)` text). The six number tiles are spaced evenly across the whole figure, so three sit under triangle (a) and three under triangle (b). The text says "Use the numbers ... once each in each triangle", but the picture implies each triangle uses its own three numbers.
Fix: centre the six tiles in one row under both triangles with a caption "Number tiles: use all six in EACH triangle", and replace the text with: "Magic triangles. Put the numbers 110, 120, 130, 140, 150 and 160 in the circles, once each, so every side has the same total. Do it for (a) and then (b)." Change (a) to: "(a) Each side adds up to 390. Write the numbers in the circles. Which numbers are in the corners? ____".

**6. Lesson 9: clock figure and paper clock disagree, hands hard to tell apart.**
Files: `l9.js` Q5 clock SVG; `p2/kit.js` `clock()`.
In Q5 the hour hand is short, thick and navy and the minute hand is red. In the kit's paper clock the hour hand is red and 150 long and the minute hand is teal and 200 long. A child who cuts out the clock will learn red = hour, then meet red = minute. In clock B the red minute hand also covers the numeral 10 and the hour hand sits almost on the 5 (4:50), so many children will write 5:50.
Fix: use the same colours in both (hour = navy, short and thick; minute = red, long and thin, ending just inside the numerals); add the caption "short thick hand = hour, long red hand = minute"; draw the minute hand to the minute marks, not through the numerals. Add to the Q5 line: "Hint: the hour hand is almost on the 5. Is it 4 o'clock or 5 o'clock?".

**7. Lesson 6: warm-up breaks the program's own money rule.**
File: `l6.js` `deck.warmQs[4]` and slide `p2l6-warm2`: "You have $4.60. A book costs $5. How much more do you need? 40¢". The title notes say P2 adds and subtracts money in dollars only or cents only (consistent with P3 listing "money in decimal notation" as new).
Fix: replace with "You have 60¢. A sticker costs 85¢. How much more do you need?" Answer 25¢.

**8. Lesson 3: Q6 table too short, Q7 tricycle picture.**
File: `l3.js`.
- Q6 gives a table of 5 columns (2 to 6 rows) but all the ways need rows up to 10 unless the child spots the pairing. Fix: widen to 9 columns (2 to 10), or add the sentence "Stop when the number of rows is bigger than the number of chairs in each row."
- Q7: the tricycle drawing shows two wheels in side view, but its caption says "3 wheels". Redraw with three visible wheels (two rear wheels offset), or draw it in front view.
- Q7a ("How do you know you have found them all?") is asked on the core page. The key's proof (odd/even) is above level. Accept: "I tried 0, 1, 2, 3, 4, 5 tricycles in order; 6 tricycles is already 18 wheels." Add that wording to the key.

**9. Lesson 1 wording: "just below / just above".**
Files: `l1.js` qbank stretch[7] and slide `p2l1-teachchart`. "Which number is just below 495?" can be read as 494. Replace with: "On a 1000 chart with rows of 10, which number is directly below 495 (one square down)? Which number is directly above 501 (one square up)?" Answers unchanged: 505 and 491. On the slide: "Which number is directly below 296? Directly above 281?" (306 and 271).

**10. Lesson 10 Q6 repeats lesson 4 Q5.**
Files: `l10.js` Q6, key, slide `p2l10-ws2ans`. Both are square tables pushed together (4, 6, 8; 6 tables = 14; 20 people = 9 tables). A review lesson should test the skill in a new setting. Replace Q6 with: "Ben builds towers with cubes. Tower 1 has 3 cubes, Tower 2 has 6 cubes, Tower 3 has 9 cubes. (a) How many cubes are in Tower 8? (b) Which tower has 30 cubes?" Table 1 to 6 as before. Answers: 24 cubes; Tower 10. Update key and `ws2ans` slide.

**11. Brain break lesson 1 cannot be done online.**
File: `l1.js` (and slide `p2l1-break`): "Three children stand as hundreds, tens and ones". Replace with: "Each child puts three digit cards in a row (hundreds, tens, ones). The tutor calls 'swap the hundreds and the tens' or 'swap the tens and the ones'. Show your new number on camera. Is it bigger or smaller?"

**12. Lesson 6: play money too small.**
`p2/kit.js` reuses `hp/kit.js` `notes()`: six $1 coins, four $2, four $5, four $10, two $50; coins: seven 5¢, seven 10¢, six 20¢, five 50¢. Q2's all-$1 way needs eight $1 coins. Add two more $1 coins (eight in total) and say in the kit text "keep spare coins". Also the kit title says digit cards are for "Lessons 1 and 2"; lesson 2 no longer uses them, lesson 10 does (Q2). Change to "Lessons 1 and 10".

**13. Lesson 7: equivalent fractions (P3) used on the core page.**
Files: `l7.js` Q6, slide `p2l7-teachsame`, qbank challenge[4], [5]. Using 1/4 = 2/8 is a P3 topic. It is acceptable because the bars are lined up and the explanation is visual, but it should be marked as a stretch of the syllabus. Fix: keep Q6, but add the line "Hint: fold or line up the bars; one quarter covers two eighths" to Q6, and say in the lesson notes "equivalent fractions are P3 and are shown only with bars; do not write 1/4 = 2/8 as a rule."

**14. Lesson 9: jug puzzles and balance lab need real props.**
Files: `l9.js` Q2, Q3; `lesson.materials`. Q2b needs 4 pours and Q3 needs 4 more rows. Without containers, 8-year-olds cannot "pour". Add to the materials: "two cups or bottles of different size and a jug of water (or dry rice), marked with tape at 3 and 5 units", and use rice or sand rather than water for online. The coat-hanger balance (explore) needs a hanger, two paper cups, string, glue stick, spoon, 20¢ coins; offer the backup "ruler balanced on a pencil".

### Low

**15. Lesson 2 stretch[3] (eggs): coincidental answer.**
`l2.js` qbank stretch[3]. Morning sales = afternoon sales = 280, so a child who writes "280" without working looks right. Replace with: "A shop had 905 eggs. It sold some in the morning and 260 in the afternoon. 345 eggs were left. How many eggs were sold in the morning?" Answer: 300 (345 + 260 = 605; 905 - 605 = 300).

**16. Workbook pagination wastes pages.**
Lesson 1 is 3 pages (Q3 alone on page 4); lesson 2 is 4 pages (page 9 holds only Q3 with a large blank grid; Q6 alone on page 11). The spec says 2 worksheet pages. Fix: remove the forced page break before Q4 in L2 and reduce the lines under Q3d; target 2 pages per lesson (lesson 1 can stay at 3 only if Q3 moves to page 3).

**17. Lesson 8 qbank core[3].**
"How many squares are in a grid 2 squares long and 2 squares high? 5" is a trap for a "core" item (most children say 4). Move it to stretch, or reword: "How many squares of ALL sizes are in a 2 by 2 grid? (Small ones and one big one.)".

**18. Lesson 4 Q6 writing load.**
"Which numbers from 1 to 40 do they BOTH say?" needs 13 + 10 written numbers. Use "from 1 to 36" (12 and 9 numbers); both-say list 12, 24, 36 is unchanged. Update the key (Ali ends 36, Mei ends 36).

**19. Lesson 7 Q1 shape F.**
The triangle cut into 4 equal triangles with the shaded one inverted is correct (quarters) but children judge by looks; many will mark it as unequal. Keep it, but add to the key note: "F is the hardest: all four small triangles are the same size". Optionally swap F for a 2 by 2 grid in a different arrangement.

**20. Materials and tutor-prep not in kit.**
Lesson 5 explore uses "× cards" and "+/− cards" (not in kit). Lesson 1 uses "a 1000 chart page" (not in kit). Lesson 4 needs 9 red/blue cubes. Lesson 8 needs scissors and paper circles. Lesson 9 needs coat-hanger balance (issue 14). Add a one-page "prepare at home" list per lesson to the parent side (`p2/parent_side.json`).

**21. Dense slides.**
Word counts (visible text, excluding notes): p2l9-we2 143, p2l2-chwalk 135, p2l5-teachrule 132, p2l1-teachriddle 128, p2l9-chwalk 122, p2l8-chwalk 115, p2l8-teachnet 114. Most are steps revealed on click and tutor-read, which is fine, but p2l9-we2 (jug table plus rules plus picture) and p2l5-teachrule are worth splitting into two slides.

**22. Lesson 6 qbank / slides.**
No further issue. The rule "no $20 note" is correct for Singapore and is repeated on the worksheet, key slide and talk slide.

## 4. Timing (is 90 minutes realistic?)

Times are read from the slide labels (the same pattern is in all ten title-slide notes).

| Lesson | Slides | Workbook (qs / pages) | Page 1 slot | Page 2 slot | Realistic? |
|---|---|---|---|---|---|
| 1 | 25 | 6 / 3 | 12 min (Q1 to Q3) | 7 min (Q4 to Q6, about 8 parts) | Tight |
| 2 | 26 | 6 / 4 | 12 min | 7 min (square, 2 triangles, model) | Too short; 3 puzzles in 7 min |
| 3 | 26 | 7 / 2 | 12 min | 7 min (Q4 to Q7 with a table and "find all") | Too short |
| 4 | 25 | 6 / 2 | 12 min | 7 min | Tight |
| 5 | 26 | 6 / 2 | 13 min | 6 min (four multi-step problems) | Too short |
| 6 | 26 | 6 / 2 | 12 min | 7 min (Q3 to Q6) | Tight to too short |
| 7 | 27 | 6 / 2 | 10 min (6 shapes, 3 questions) | 10 min | OK, page 1 tight |
| 8 | 27 | 5 / 2 | 10 min | 9 min (stacks, 6 nets, dice net) | Too short |
| 9 | 26 | 5 / 2 | 12 min (two jug puzzles) | 7 min (jug table, ribbons, clocks) | Too short |
| 10 | 27 | 6 / 2 | 11 min | 8 min | Tight |

Why: independent work is only 19 to 26 minutes of the 90, while each lesson also has 3 to 4 mini-teaching blocks (54 to 60) and two check-together slides. Warm-up (10) and explore (15) take 25 minutes before any teaching.

Proposed re-time for all lessons (changes only the labels and notes; no slide needs rebuilding):
warm-up 0 to 8 (cut warm2 to 3 minutes); explore 8 to 20 (explore2 talk shortened to 6 minutes); teaching 20 to 32; break 32 to 36 (4 minutes); worksheet page 1 36 to 50; check 50 to 52; short teaching 52 to 57; worksheet page 2 57 to 69; check 69 to 72; talk 72 to 80; exit 80 to 90. This gives page 2 about 12 minutes (up from 7) at the cost of explore, warm-up and talk time.

Lessons 5 and 8 need the content changes in issues 2 and 3 in addition to the re-time.

## 5. Per-lesson notes (a) to (f)

### Lesson 1: Digit Detectives (numbers to 1000)
(a) On syllabus (place value, count on/back in 1s, 10s, 100s, 1000 chart). Making all numbers from digit cards is enrichment but within number sense. 15 tens regrouping (Q1b) is a slight stretch, done well.
(b) Core Q1, Q2, Q4, Q5 are doable by almost every child. Q3 (zero) and Q6b (digits sum to 3) are a stretch. Think Harder: stretch[0 to 3] good; challenge Q5 (smallest total from six cards), Q6 (does a count-by-5s sequence say 500 / 998) and Q7 (how many 3s from 300 to 399, answer 120) are for strong thinkers and well chosen.
(c) Reading load light (321 workbook words, longest line 27 words). Riddles are two to three clues: fine.
(d) All answers correct. Only ambiguity: "just below / just above" (issue 9).
(e) Tight; see section 4. Explore (15 minutes for 6 numbers) is generous and can be cut to 10.
(f) Human-number break (issue 11). Digit cards cut at home before class: fine.

### Lesson 2: Missing Digit Mysteries (add and subtract within 1000)
(a) On syllabus (3-digit add/subtract with regrouping). "Balance the equation" (Q3) is within P2 number sense. Magic triangles and the "two numbers from total and difference" model (Q6, a P4 model-method topic) are enrichment; both are taught on slides before use.
(b) Q1, Q2, Q3 core. Q4 (magic square) is doable by most. Q5 (magic triangles) and Q6 are a stretch on the core page. Think Harder: stretch[0 to 3] fine; challenge Q5 (find all ways with 10 solutions), Q6 (three boxes, three pair totals) and Q7 (smallest difference = 47) are strong-thinker items; Q6 is the hardest in the program (a three-unknown puzzle).
(c) Lightest reading in the program (242 words). "Explain WITHOUT working out both sides" (Q3d) is abstract language: shorten to "Explain how you know without adding."
(d) All correct. Figure issue in Q5 (issue 5). Stretch[3] coincidence (issue 15).
(e) Four workbook pages and 7 minutes for page 2: too short.
(f) Magic triangle figure (issue 5).

### Lesson 3: Legs, Wheels and Arrays (multiplication and division)
(a) Arrays, tables 2, 3, 4, 5, 10, equal groups: core P2. "Sharing with leftovers" (Q4, Q5 and three slides) is division with remainder, a P3 topic; it is the natural lead-in, but the title notes should say "do not write remainders as 'r'". Hens-and-goats swap table is a P3/P4 heuristic, well scaffolded.
(b) Q1, Q2, Q3, Q4, Q5 core; Q6 (find all arrays for 20) a stretch; Q7 (17 wheels, find all) labelled Challenge. Think Harder: stretch fine; challenge[7] (two remainder conditions) is hard but correct and unique (27).
(c) 291 words; the long lines (39 words) are Q3 and Q7 problem setups: acceptable.
(d) All correct and unique. Q6 table length and Q7 tricycle picture (issue 8).
(e) Page 2 has four questions in 7 minutes: too short.
(f) Counters and cups at home; fine.

### Lesson 4: Pattern Machines (patterns with multiplication)
(a) Repeating patterns and number patterns with the 2, 3, 4, 5, 10 tables: well within P2 number patterns.
(b) Core Q1, Q2, Q4, Q5. Q3 (bead string, labelled Challenge) is a reasonable stretch. Think Harder strong.
(c) Moderate (289 words). Fine.
(d) All correct (including Q1d: 12 circles; Q2c: 7 Ts; Q5c: 9 tables).
(e) Tight.
(f) Q1 and Q2 are numbered by place and children need to draw group lines: the slide says "Draw a line after each group of 5", good. Q5 is repeated in lesson 10 (issue 10).

### Lesson 5: Mystery Number Machines (working backwards)
(a) Two-step "undo" problems with + - x / and before-and-after bars are P3 level in the MOE sequence; here taught from first principles. Reasonably just beyond.
(b) Core Q1, Q3 are doable. Q2b, Q4, Q5d, Q6 are a stretch. Challenge[5] (x + 10 = 3x) is algebra by trial: strong thinkers only.
(c) Highest load (367 words, longest line 37, bank average 25 words per question, max 46 words). Stories are two to four sentences.
(d) All correct. Common wrong answers are named in the notes: good.
(e) Page 2 slot 6 minutes. Too short.
(f) Fine online. Needs the issue 3 fix.

### Lesson 6: Market Day (money)
(a) On syllabus (reading and counting dollars and cents, conversion, change by counting on). Adding mixed amounts is correctly avoided (P3). Only the warm-up slip (issue 7).
(b) Q1, Q3, Q5a are core. Q2 (7 ways) is a good stretch; Q4b, Q6 (find all) a stretch. Think Harder strong: challenge[8] (15 different amounts from $1, $2, $5, $10) and challenge[2] are for strong thinkers.
(c) 295 words; lots of prices: fine.
(d) All correct. Q2 has 8 rows for 7 ways (the key says row H is spare): fine, but tell the tutor to say "you may not need every row".
(e) Tight on page 2.
(f) Play money supply (issue 12).

### Lesson 7: Fair Shares (fractions)
(a) On syllabus (equal parts, shaded and unshaded, compare unit and like fractions, add like fractions within one whole, denominators to 12). Only equivalence (issue 13) is beyond.
(b) Q1 to Q5 core; Q6 and Q3c stretch. Think Harder good; challenge[8] ("half of a half") is a nice strong-thinker item.
(c) Light, but Q3c and Q6 are long (48 words in one line: reduce).
(d) All correct. All shaded drawings are built from equal parts by construction (checked in `l7.js`).
(e) Page 1 tight (10 minutes for 11 sub-items), page 2 OK.
(f) Paper strips are needed for the explore (kit has fraction strips).

### Lesson 8: Shape Builders (2D and 3D shapes)
(a) Semicircles, quarter circles and 3D solids are P2. Counting every square and every triangle, hidden-cube counting and nets are beyond P2.
(b) Q1 and Q2 (with their scaffolds) are doable. Q3 stack C (14 cubes) and Q4/Q5 nets are Think Harder level on a core page.
(c) Lowest word count (215), because the load is spatial, not verbal.
(d) All correct (nets verified by simulation: A, C, E fold; B, D, F do not; Q4b has exactly 4 valid places).
(e) Too short for page 2.
(f) Isometric cube drawings (Q3) are hard on a screen; consider real cubes (the lesson already suggests 12 per child).

### Lesson 9: Measure Masters (length, mass, volume, time)
(a) Units, balance reasoning, ribbons, time to 5 minutes and durations. Durations over the hour (Q5c: 10:45 to 12:10) are P3 wording but done by counting on. Jug puzzles are enrichment.
(b) Q1 (balance swaps), Q4 and Q5 are core; Q2 and Q3 (jugs) are a stretch (BFS minimum: 2 pours for 2 l, 4 for 1 l, 4 more from (1,5) for 4 l). Challenge[6] (3 l and 7 l jug, 5 l, minimum 8 steps) is for strong thinkers only.
(c) 308 words; Q1 stories moderate; the longest line is 44 words (Q3 setup): acceptable.
(d) All correct.
(e) Page 2 too short.
(f) Clock figure and kit clock colours (issue 6), props for jug puzzles (issue 14).

### Lesson 10: Challenge Day (mixed puzzles)
(a) Mixed review of lessons 1 to 9, picture graph with scale 5 (on syllabus), logic grid (enrichment).
(b) Q1, Q2, Q3, Q5 core. Q4 (logic grid with 3 clues) is a reasonable stretch. Challenge[8] (hawker dishes, 7 dishes, $25) is a good strong-thinker item.
(c) Light and varied (278 words).
(d) All correct and unique (logic grid solved by elimination: Siti walk, Ben MRT, Mei bus, Ali car).
(e) Only if the explore is rebuilt (issue 1).
(f) Station cards (issue 1); a relay that passes a name in a breakout-free class is fine.

## 6. What is good and should not change

- Level discipline: no 6 to 9 tables, no number above 1000, no mixed-amount money columns, no decimals other than money.
- The "parallel example" rule: slide worked examples never give away workbook answers (checked in all ten lessons).
- Every "find all" and logic item has exactly one verified solution; mistakes lists in the lesson notes match the real errors seen at this age.
- Slides: all fonts at least 24px, reveal-on-click answers, a "see it" diagram and a walk-through for each pair of challenge items.
