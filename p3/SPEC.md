# Math Inquirers P3 Holiday Program — content spec

**Who:** children finishing Primary 3 (going into P4 in 2027), age 9. Online-first, live video, groups of up to 8.
**Format:** 10 lessons × 90 minutes over 5 weeks (2 a week), same routine as the P1 program.
**Approach:** enrichment, non-routine puzzles and heuristics, on topics chosen to complement the P3 school year. Slogan: "Notice it. Test it. Explain why."
Syllabus source: Tampines North Primary 2026 P3 scheme of work (numbers to 10 000; + −; money; tables of 6, 7, 8, 9; × ÷; word problems; bar graphs; angles; perpendicular and parallel lines; fractions; length, mass and volume; area and perimeter; time).

## The 10 lessons
| n | Week | Title | Topic (syllabus tag) | Puzzle focus |
|---|---|---|---|---|
| 1 | 1A | Number Sleuths | Numbers to 10 000 | digit puzzles with conditions, place value, number patterns, biggest/smallest |
| 2 | 1B | Cryptarithm Crackers | Addition and subtraction | missing digits in 4-digit sums, magic squares, digit-sum puzzles |
| 3 | 2A | Times Table Treasure | Tables of 6, 7, 8, 9 | patterns inside the tables, multiplication grid puzzles, arrays, last-digit patterns |
| 4 | 2B | Model Makers | Word problems | bar models: part-whole, comparison, before-and-after, two-step |
| 5 | 3A | Remainder Riddles | Division | sharing with remainders, "what number am I" with remainders, grouping puzzles |
| 6 | 3B | Fraction Walls | Fractions | equivalent fractions, comparing, adding like and related fractions within one whole |
| 7 | 4A | Area Architects | Area and perimeter | same perimeter different area, figures made of squares and rectangles, square-grid puzzles |
| 8 | 4B | Angle and Line Detectives | Angles, perpendicular and parallel lines | counting angles, right angles in shapes, finding parallel and perpendicular lines in figures |
| 9 | 5A | Measure and Money Masters | Length, mass, volume, money, time | compound units, budgets, durations and the 24-hour clock |
| 10 | 5B | Challenge Day | Mixed (incl. bar graphs, logic) | how to start a puzzle: draw it, list it, make a table; logic grid; reading a bar graph |

## P3 level rules
- Children know: numbers to 10 000; + and − within 10 000; all multiplication tables to 10 × 10; multiplying up to 3 digits by 1 digit and dividing up to 3 digits by 1 digit (with remainders); fractions: equivalent fractions, comparing and ordering, adding and subtracting like and related fractions within one whole; money in dollars and cents; m, cm, km, kg, g, ℓ, ml (compound units like 2 m 35 cm); area and perimeter of squares, rectangles and figures made of them (cm², m²); right angles and comparing angles (no protractor yet); perpendicular and parallel lines; bar graphs; time in hours and minutes, durations, the 24-hour clock.
- Do NOT use: decimals other than money; multiplying by 2-digit numbers; long division by 2-digit numbers; fractions of a set; mixed numbers; percentages; ratio; negative numbers; algebra letters.
- Every answer must be worked out and checked; puzzles with "find all" must list every case; logic puzzles must have exactly one solution.
- Plain English. Singapore context (names like Ali, Mei, Ravi, Siti, Ben; $ and ¢; hawker, MRT, HDB are fine).
- Teaching examples on slides must NOT give away the workbook answers: use a parallel example.

## Files each lesson writer produces
1. `p3/content/lN.js` (N = 1..10), a CommonJS module:
```js
module.exports = {
  lesson: { n, week, session:'A'|'B', title, topic, objective, skills, materials, online,
            warmup, explore, mini, share, exit:{q,a}, mistakes:[3 strings], extension,
            key:[['Q1','answer'], ...] },          // same fields as hp/lessons.js entries; key matches the workbook
  script: { hook:[], warmIntro:[], predict:[], exploreHints:[], think:[], circulate:[], hints:[], talk:[], talkAns:'', close:[] },
                                                   // same fields as hp/scripts.js entries
  deck:   { today, warmGame, warmQs:[[q,a],…4-5], expSetup:[4 steps], expPic, expAsk:[[q,a]×3],
            mini1:{head, body:[], ans}, mini2:{head, body:[], ans}, keyHead:'Key idea: …', keyBig, keySmall, brk },
                                                   // same fields as deck/data.js entries (the tutor guide reads them); mini1/mini2 = the two main worked examples
  qbank:  { core:[6 {q,a}], stretch:[8 {q,a}], challenge:[9 {q,a}] },
                                                   // stretch[0..3] and the LAST 3 challenge items print on the workbook's Think Harder pages
  workbook: H => [ ...html strings ]               // the lesson's 2 worksheet pages (5 to 7 questions); the builder adds the lesson header before it and the Think Harder pages after it
};
```
   Workbook helpers `H` (same as hp/common_html.js): `H.q(n, text, {pb, before, keepNext})`, `H.sub(letter, text)`, `H.ans(label?)`, `H.lines(n)` (array — spread it), `H.p(text, {after})`, `H.tbl(widths, rows)`, `H.row(cells)`, `H.cell(text, width, {bold, fill:'D9D9D9'|'EDEDED', h})`, `H.gap(n)`, and `H.fig(svgString)` for an inline SVG drawing (viewBox width about 600, navy #1B2A49 lines, fills from #FFC93C #DDEBF7 #1F7A6F #D64545 #FFFFFF, Arial/Fredoka text ≥ 14px). Start page 2 with `{pb:true, before:0}` on its first question. Widths for tbl sum to 9900. Look at hp/workbook_html.js (lessons 6 and 9) for the style of questions and how answer lines are given.
2. `rebuild/gen_p3lN.py` writing the slide deck to `split/p3lN/project/` (deck.json + slides/*.html), built with `rebuild/slidekit.py` exactly like the approved P1 generators `rebuild/gen_l2.py`, `gen_l5.py`, `gen_l6.py` (read them). Slide ids `p3lN-…`. deck.json: copy the shape of `split/l6/project/deck.json` (v, createdOnFiles, lists, title "Math Inquirers P3: Lesson N – <Title>", order, cover, sections, faces, designSystems []). About 24–27 slides: title (notes: objective, materials, online set-up, time plan), warm1 (game), warm2 (quick questions, click answers), explore1 (what to do, with a small SVG picture), explore2 (talk about it), teach + worked examples (steps revealed on click) + "your turn" slides, key idea (mistakes in notes only), break, ws1 preview, ws1ans (check together), short teach-before slides for page-2 question types, ws2 preview, ws2ans, stretch (3 NEW items with answers in notes), challenge (2 items), chdiag (an SVG "see it" diagram of the two challenge items, no answers), chwalk (walk-through), talk, exit. Timings follow the 90-minute routine (title notes give the plan).
   Slide rules: 1920×1080, one `<section>` per file, inline styles only, padding 128px, footer at bottom:64px, nothing below y 920 except the footer, ≤ 200 elements, no font under 24px, pinned (position:absolute) children only for build-in reveals and fixed layout; notes in one `<aside>` last (≤ 4000 chars). SVGs get an aria-label. Never use the ✗ character (it looks like ×); write "not this one" instead.
3. Render with `python3 rebuild/preview.py split/p3lN/project <outdir>` (outdir under the scratchpad), fix OVERFLOW and visible overlaps once.

Do not edit any shared file (hp/*, rebuild/slidekit.py, other lessons). Do not commit, push or publish.
