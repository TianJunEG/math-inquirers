# Math Inquirers P6 Post-PSLE Program — content spec (maths + coding bridge)

**Who:** children who have just finished the PSLE (P6, age 12), going into Secondary 1 in 2027. Online-first, live video, groups of up to 8. Each child needs a laptop or desktop (a tablet works for Scratch but is slower).
**Format:** 10 lessons × 90 minutes over 5 weeks (2 a week), same routine as the P1 program, but the Explore and Workbook parts often happen at the computer.
**Approach:** enrichment that bridges to Secondary 1 maths, with every lesson's puzzle also explored in code. No exam drilling: they have just finished the PSLE. Slogan: "Notice it. Test it. Explain why." In this program "test it" often means "test it in code".
**Coding environment:** Scratch 3 (free, in the browser at scratch.mit.edu; many children met block coding in school). Every lesson also gives an optional Python version of the same task (10 to 20 lines) for children who already know Python. Draw code blocks on slides and in the workbook as our own simple coloured block shapes in SVG (rounded rectangles with the block text, e.g. "repeat 10", "change n by 3", "say n"), never Scratch's logo or the cat sprite.

## The 10 lessons
| n | Week | Title | Maths (Sec 1 bridge) | Coding idea | Puzzle focus |
|---|---|---|---|---|---|
| 1 | 1A | Code the Pattern | Sequences and the nth term | loops and a variable | growing patterns, predicting the 100th term, checking it in code |
| 2 | 1B | Prime Hunters | Primes, factors, prime factorisation | if, mod (remainder), a counter | sieve by hand, a prime checker, Goldbach pairs, numbers with exactly 3 factors |
| 3 | 2A | Below Zero | Negative numbers | a sprite moving on a number line, variables that go below 0 | temperatures, lifts and sea level, adding and subtracting negatives on a line |
| 4 | 2B | Algebra Machines | Expressions and simple equations | input, a rule, output (functions) | guess my rule, function machines run backwards, writing the rule with a letter |
| 5 | 3A | Every Possible Way | Counting (combinatorics) | nested loops that list every case | handshakes, routes on a grid, outfits, how many numbers from digit cards |
| 6 | 3B | Fair or Unfair? | Probability | random numbers, running a game 1000 times | dice and spinner games, is a game fair, comparing results with what we expect |
| 7 | 4A | Turtle Geometry | Angles in polygons | pen drawing with turns | regular polygons, the 360° turn idea, star polygons, predicting the turn angle |
| 8 | 4B | Secret Codes | Clock (modular) arithmetic | lists and letters, mod | Caesar ciphers, cracking a code, clock arithmetic puzzles |
| 9 | 5A | Data Detectives | Averages and data | lists, adding up, mean | mean, what changes the mean, misleading averages, collecting class data |
| 10 | 5B | Showcase Challenge | Mixed | each child builds and shares a small puzzle program | a mixed maths challenge round, then a 3-minute showcase of their program |

## P6 level rules
- Children know all of primary maths: whole numbers, fractions, decimals, percentage, ratio, rate and speed, simple algebra with one letter (expressions and simple equations), average, angles, circles, area and volume, pie charts.
- Secondary 1 ideas are introduced gently and concretely: negative numbers, primes and prime factorisation, sequences and the nth term, simple equations with a letter. No index notation beyond squares, no surds, no formal proofs.
- Coding stays small: each program is under about 15 blocks (or 20 lines of Python). The maths comes first; code is the way we test and extend it.
- Every answer must be worked out and checked; "find all" puzzles must list every case; probability claims must be correct (state what we expect and why a simulation varies).
- Plain English for 12-year-olds. Singapore context is fine.
- Teaching examples on slides must NOT give away the workbook answers: use a parallel example.
- Workbook pages mix maths questions with "predict what this code does", "trace the code in a table" and "plan your code" boxes; children write on paper even though they code on screen.

## Files each lesson writer produces
1. `p6/content/lN.js` (N = 1..10), a CommonJS module:
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
2. `rebuild/gen_p6lN.py` writing the slide deck to `split/p6lN/project/` (deck.json + slides/*.html), built with `rebuild/slidekit.py` exactly like the approved P1 generators `rebuild/gen_l2.py`, `gen_l5.py`, `gen_l6.py` (read them). Slide ids `p6lN-…`. deck.json: copy the shape of `split/l6/project/deck.json` (v, createdOnFiles, lists, title "Math Inquirers P6: Lesson N – <Title>", order, cover, sections, faces, designSystems []). About 24–27 slides: title (notes: objective, materials, online set-up, time plan), warm1 (game), warm2 (quick questions, click answers), explore1 (what to do, with a small SVG picture), explore2 (talk about it), teach + worked examples (steps revealed on click) + "your turn" slides, key idea (mistakes in notes only), break, ws1 preview, ws1ans (check together), short teach-before slides for page-2 question types, ws2 preview, ws2ans, stretch (3 NEW items with answers in notes), challenge (2 items), chdiag (an SVG "see it" diagram of the two challenge items, no answers), chwalk (walk-through), talk, exit. Timings follow the 90-minute routine (title notes give the plan).
   Slide rules: 1920×1080, one `<section>` per file, inline styles only, padding 128px, footer at bottom:64px, nothing below y 920 except the footer, ≤ 200 elements, no font under 24px, pinned (position:absolute) children only for build-in reveals and fixed layout; notes in one `<aside>` last (≤ 4000 chars). SVGs get an aria-label. Never use the ✗ character (it looks like ×); write "not this one" instead.
3. Render with `python3 rebuild/preview.py split/p6lN/project <outdir>` (outdir under the scratchpad), fix OVERFLOW and visible overlaps once.

Do not edit any shared file (hp/*, rebuild/slidekit.py, other lessons). Do not commit, push or publish.
