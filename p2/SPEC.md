# Math Inquirers P2 Holiday Program — content spec

**Who:** children finishing Primary 2 (going into P3 in 2027), age 8. Online-first, live video, groups of up to 8.
**Format:** 10 lessons × 90 minutes over 5 weeks (2 a week), same routine as the P1 program.
**Approach:** enrichment, non-routine puzzles, on topics chosen to complement the P2 school year. Slogan: "Notice it. Test it. Explain why."

## The 10 lessons
| n | Week | Title | Topic (syllabus tag) | Puzzle focus |
|---|---|---|---|---|
| 1 | 1A | Digit Detectives | Numbers to 1000 | place value, digit-card puzzles (biggest/smallest, how many numbers), patterns on a 1000 chart |
| 2 | 1B | Missing Digit Mysteries | Addition and subtraction within 1000 | missing digits in 3-digit sums, balance equations, magic squares/triangles with bigger numbers |
| 3 | 2A | Legs, Wheels and Arrays | Multiplication and division (tables 2, 3, 4, 5, 10) | arrays, legs and wheels (how many of each), equal groups, sharing with leftovers |
| 4 | 2B | Pattern Machines | Patterns with multiplication | far places in repeating patterns using groups, growing patterns with a rule, tables |
| 5 | 3A | Mystery Number Machines | Working backwards (two steps, + − × ÷) | number machines, before-and-after stories, bar models |
| 6 | 3B | Market Day | Money (dollars and cents) | pay exactly, fewest coins and notes, change, budgets ("is there enough?") |
| 7 | 4A | Fair Shares | Fractions | halves, thirds, quarters; compare; add like fractions within one whole; fair sharing |
| 8 | 4B | Shape Builders | 2D and 3D shapes | semicircles/quarter circles, composing shapes, counting cubes in stacks, nets, hidden shapes |
| 9 | 5A | Measure Masters | Length, mass, volume, time | balance-scale puzzles, pouring (jug) puzzles, ribbons end to end, time to 5 minutes and durations |
| 10 | 5B | Challenge Day | Mixed (incl. picture graphs with scales, logic) | how to start a puzzle: draw it, list it, make a table; logic grid; picture graph with a key |

## P2 level rules
- Children know: numbers to 1000; + and − within 1000; × and ÷ facts of the 2, 3, 4, 5 and 10 tables (so × and ÷ ARE allowed, within those tables); fractions with denominators up to 12, comparing unit and like fractions, adding/subtracting like fractions within one whole; money in dollars and cents ($2.35); m, cm, kg, g, ℓ; time to 5 minutes, a.m./p.m.; picture graphs with a key; semicircle, quarter circle; cube, cuboid, cone, cylinder.
- Do NOT use: the 6, 7, 8, 9 tables; long multiplication or long division; decimals other than money; negative numbers; numbers above 1000.
- Every answer must be worked out and checked; puzzles with "find all" must list every case; logic puzzles must have exactly one solution.
- Plain English for 8-year-olds. Singapore context (names like Ali, Mei, Ravi, Siti, Ben; $ and ¢; hawker, MRT, HDB are fine).
- Teaching examples on slides must NOT give away the workbook answers: use a parallel example.

## Files each lesson writer produces
1. `p2/content/lN.js` (N = 1..10), a CommonJS module:
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
2. `rebuild/gen_p2lN.py` writing the slide deck to `split/p2lN/project/` (deck.json + slides/*.html), built with `rebuild/slidekit.py` exactly like the approved P1 generators `rebuild/gen_l2.py`, `gen_l5.py`, `gen_l6.py` (read them). Slide ids `p2lN-…`. deck.json: copy the shape of `split/l6/project/deck.json` (v, createdOnFiles, lists, title "Math Inquirers P2: Lesson N – <Title>", order, cover, sections, faces, designSystems []). About 24–27 slides: title (notes: objective, materials, online set-up, time plan), warm1 (game), warm2 (quick questions, click answers), explore1 (what to do, with a small SVG picture), explore2 (talk about it), teach + worked examples (steps revealed on click) + "your turn" slides, key idea (mistakes in notes only), break, ws1 preview, ws1ans (check together), short teach-before slides for page-2 question types, ws2 preview, ws2ans, stretch (3 NEW items with answers in notes), challenge (2 items), chdiag (an SVG "see it" diagram of the two challenge items, no answers), chwalk (walk-through), talk, exit. Timings follow the 90-minute routine (title notes give the plan).
   Slide rules: 1920×1080, one `<section>` per file, inline styles only, padding 128px, footer at bottom:64px, nothing below y 920 except the footer, ≤ 200 elements, no font under 24px, pinned (position:absolute) children only for build-in reveals and fixed layout; notes in one `<aside>` last (≤ 4000 chars). SVGs get an aria-label. Never use the ✗ character (it looks like ×); write "not this one" instead.
3. Render with `python3 rebuild/preview.py split/p2lN/project <outdir>` (outdir under the scratchpad), fix OVERFLOW and visible overlaps once.

Do not edit any shared file (hp/*, rebuild/slidekit.py, other lessons). Do not commit, push or publish.
