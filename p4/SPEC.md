# Math Inquirers P4 Holiday Program — content spec

**Who:** children finishing Primary 4 (going into P5 in 2027), age 10. Online-first, live video, groups of up to 8.
**Format:** 10 lessons × 90 minutes over 5 weeks (2 a week), same routine as the P1 program.
**Approach:** enrichment, non-routine puzzles and heuristics, tagged to the P4 syllabus. Slogan: "Notice it. Test it. Explain why."
Syllabus source: Tampines North Primary 2026 P4 scheme of work (numbers to 100 000; factors and multiples; four operations; tables and line graphs; fractions; angles; rectangles and squares; decimals and their four operations; area and perimeter; nets; symmetry).

## The 10 lessons
| n | Week | Title | Topic (syllabus tag) | Puzzle focus |
|---|---|---|---|---|
| 1 | 1A | Factor Hunters | Factors and multiples | common multiples (when do buses meet again), factor pairs, numbers with exactly 3 factors, multiple-based logic |
| 2 | 1B | Big Number Puzzles | Numbers to 100 000 | rounding and estimating puzzles, digit conditions, number patterns |
| 3 | 2A | Operation Detectives | Four operations | missing operations and brackets to hit a target, order of operations, number-chain puzzles |
| 4 | 2B | Fraction Frontier | Fractions | improper fractions and mixed numbers, fraction of a set, comparing with unlike denominators, fraction models |
| 5 | 3A | Decimal Detectives | Decimals | ordering and rounding decimals to 3 places, decimal number lines, money and measurement puzzles |
| 6 | 3B | Angle Turns | Angles | measuring and estimating angles, turns on the 8-point compass, angles on a clock face, angles in squares and rectangles |
| 7 | 4A | Area Architects II | Area and perimeter, rectangles and squares | composite figures, fixed area with largest and smallest perimeter, cutting and rearranging rectangles |
| 8 | 4B | Symmetry and Nets | Symmetry, nets | completing symmetric figures, lines of symmetry, which nets fold into a cube, opposite faces on a dice net |
| 9 | 5A | Data Detectives | Tables and line graphs | reading trends, missing values, comparing two lines, spotting a misleading graph |
| 10 | 5B | Challenge Day | Mixed heuristics | guess and check, supposition (heads and legs), working backwards, logic; competition-style problems |

## P4 level rules
- Children know: numbers to 100 000; factors, multiples, common factors and common multiples; four operations including multiplying up to 4 digits by 2 digits and dividing up to 4 digits by 1 digit; order of operations; fractions: mixed numbers, improper fractions, fraction of a set, adding and subtracting fractions with denominators up to 12; decimals to 3 places and the four operations with a decimal and a 1-digit whole number; measuring angles with a protractor; 8-point compass; properties of rectangles and squares; area and perimeter of composite rectilinear figures; line symmetry; nets of cubes and cuboids; tables and line graphs.
- Do NOT use: percentages; ratio; algebra letters; speed; area of triangles; negative numbers; numbers above 100 000.
- Every answer must be worked out and checked; puzzles with "find all" must list every case; logic puzzles must have exactly one solution.
- Plain English. Singapore context (names like Ali, Mei, Ravi, Siti, Ben; $ and ¢; hawker, MRT, HDB are fine).
- Teaching examples on slides must NOT give away the workbook answers: use a parallel example.

## Files each lesson writer produces
1. `p4/content/lN.js` (N = 1..10), a CommonJS module:
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
2. `rebuild/gen_p4lN.py` writing the slide deck to `split/p4lN/project/` (deck.json + slides/*.html), built with `rebuild/slidekit.py` exactly like the approved P1 generators `rebuild/gen_l2.py`, `gen_l5.py`, `gen_l6.py` (read them). Slide ids `p4lN-…`. deck.json: copy the shape of `split/l6/project/deck.json` (v, createdOnFiles, lists, title "Math Inquirers P4: Lesson N – <Title>", order, cover, sections, faces, designSystems []). About 24–27 slides: title (notes: objective, materials, online set-up, time plan), warm1 (game), warm2 (quick questions, click answers), explore1 (what to do, with a small SVG picture), explore2 (talk about it), teach + worked examples (steps revealed on click) + "your turn" slides, key idea (mistakes in notes only), break, ws1 preview, ws1ans (check together), short teach-before slides for page-2 question types, ws2 preview, ws2ans, stretch (3 NEW items with answers in notes), challenge (2 items), chdiag (an SVG "see it" diagram of the two challenge items, no answers), chwalk (walk-through), talk, exit. Timings follow the 90-minute routine (title notes give the plan).
   Slide rules: 1920×1080, one `<section>` per file, inline styles only, padding 128px, footer at bottom:64px, nothing below y 920 except the footer, ≤ 200 elements, no font under 24px, pinned (position:absolute) children only for build-in reveals and fixed layout; notes in one `<aside>` last (≤ 4000 chars). SVGs get an aria-label. Never use the ✗ character (it looks like ×); write "not this one" instead.
3. Render with `python3 rebuild/preview.py split/p4lN/project <outdir>` (outdir under the scratchpad), fix OVERFLOW and visible overlaps once.

Do not edit any shared file (hp/*, rebuild/slidekit.py, other lessons). Do not commit, push or publish.
