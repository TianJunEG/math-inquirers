# Math Inquirers P5 Holiday Program — content spec

**Who:** children finishing Primary 5 Standard Mathematics (going into P6 in 2027), age 11. Online-first, live video, groups of up to 8.
**Format:** 10 lessons × 90 minutes over 5 weeks (2 a week), same routine as the P1 program.
**Approach:** enrichment, non-routine problems and heuristics (the kind that stretch strong P5 children, in the spirit of competition maths), on topics chosen to complement the P5 school year. Slogan: "Notice it. Test it. Explain why."
Syllabus source: Tampines North Primary 2026 P5 Standard Mathematics scheme of work (numbers to 10 million; four operations; fraction and division; four operations of fractions; area of triangle; volume; decimals; rate; percentage; angles; properties of triangles; parallelogram, rhombus and trapezium).

## The 10 lessons
| n | Week | Title | Topic (syllabus tag) | Puzzle focus |
|---|---|---|---|---|
| 1 | 1A | Million Puzzles | Numbers to 10 million, four operations | estimation, target numbers with brackets, digit and place-value conditions |
| 2 | 1B | Fraction Feats | Four operations of fractions, fraction and division | unit-fraction puzzles, fraction of a remainder, sharing problems, fraction patterns |
| 3 | 2A | Before and After | Fraction word problems | units and parts with models: before-and-after, constant total, constant difference |
| 4 | 2B | Triangle Areas | Area of triangle | triangles in composite figures, same base and same height, shaded-area puzzles |
| 5 | 3A | Volume Vault | Volume | cuboids and unit cubes, water-level rise, painted-cube puzzles, tank filling |
| 6 | 3B | Rate Racers | Rate | rates per unit, taps and printers, comparing better buys, combined rates kept simple |
| 7 | 4A | Percentage Puzzles | Percentage | discounts, GST, percentage increase and decrease traps, percentage of a remainder |
| 8 | 4B | Angle Chasers | Angles, triangles and quadrilaterals | unknown angles in triangles, parallelograms, rhombuses and trapeziums; angle-chase chains with reasons |
| 9 | 5A | Pattern Generalisers | Patterns and number sense | growing patterns, the nth term described in words, supposition, guess and check with tables |
| 10 | 5B | Challenge Day | Mixed heuristics | competition-style problems, logic, working backwards, choosing a heuristic and explaining it |

## P5 level rules
- Children know: numbers to 10 million; four operations and order of operations with brackets; fraction and division; adding, subtracting, multiplying and dividing fractions (dividing a whole number by a whole number to get a fraction is P5; dividing a proper fraction by a whole number is a P6 skill, so label it a preview); area of triangles and composite figures; volume of cubes and cuboids, liquids in ml and ℓ; decimals and the four operations with them; rate; percentage (of a quantity, discount, GST, increase and decrease); angles on a straight line, at a point, vertically opposite; angle properties of triangles (sum 180°, isosceles, equilateral, right-angled), parallelogram, rhombus and trapezium.
- Do NOT use: algebra with letters (that is P6); speed; circles; pie charts; negative numbers. Ratio notation is avoided (it appears in some P5 schemes of work, but this program does not teach it). Percentage increase or decrease and finding the whole from a percentage are P6: keep them off the Core pages and label them as a P6 preview.
- Every answer must be worked out and checked; puzzles with "find all" must list every case; logic puzzles must have exactly one solution.
- Plain English. Singapore context (names like Ali, Mei, Ravi, Siti, Ben; $ and ¢; hawker, MRT, HDB are fine).
- Teaching examples on slides must NOT give away the workbook answers: use a parallel example.

## Files each lesson writer produces
1. `p5/content/lN.js` (N = 1..10), a CommonJS module:
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
2. `rebuild/gen_p5lN.py` writing the slide deck to `split/p5lN/project/` (deck.json + slides/*.html), built with `rebuild/slidekit.py` exactly like the approved P1 generators `rebuild/gen_l2.py`, `gen_l5.py`, `gen_l6.py` (read them). Slide ids `p5lN-…`. deck.json: copy the shape of `split/l6/project/deck.json` (v, createdOnFiles, lists, title "Math Inquirers P5: Lesson N – <Title>", order, cover, sections, faces, designSystems []). About 24–27 slides: title (notes: objective, materials, online set-up, time plan), warm1 (game), warm2 (quick questions, click answers), explore1 (what to do, with a small SVG picture), explore2 (talk about it), teach + worked examples (steps revealed on click) + "your turn" slides, key idea (mistakes in notes only), break, ws1 preview, ws1ans (check together), short teach-before slides for page-2 question types, ws2 preview, ws2ans, stretch (3 NEW items with answers in notes), challenge (2 items), chdiag (an SVG "see it" diagram of the two challenge items, no answers), chwalk (walk-through), talk, exit. Timings follow the 90-minute routine (title notes give the plan).
   Slide rules: 1920×1080, one `<section>` per file, inline styles only, padding 128px, footer at bottom:64px, nothing below y 920 except the footer, ≤ 200 elements, no font under 24px, pinned (position:absolute) children only for build-in reveals and fixed layout; notes in one `<aside>` last (≤ 4000 chars). SVGs get an aria-label. Never use the ✗ character (it looks like ×); write "not this one" instead.
3. Render with `python3 rebuild/preview.py split/p5lN/project <outdir>` (outdir under the scratchpad), fix OVERFLOW and visible overlaps once.

Do not edit any shared file (hp/*, rebuild/slidekit.py, other lessons). Do not commit, push or publish.
