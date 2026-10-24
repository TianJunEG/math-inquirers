# Level 1 extension units 3 and 4: author notes

Units: `extension/data/l1_u03.json` (Picture graphs, holiday lesson 3) and `l1_u04.json` (Repeating and growing patterns, holiday lesson 4). Independent checks: `extension/verify/l1_u03_checks.py`, `l1_u04_checks.py` (every answer recomputed; stick counts from the drawn edges). New figure types: `extension/tools/figs_l1_u03_u04.py` (picture_graph, shape_row, stick_rows, towers, tally), hooked into `figs.render` by a small plugin loader (any `tools/figs_*.py` with a `FIGS` table).

## Type map (extension item type -> holiday type, new numbers and contexts)
Unit 3: read most/fewest/same/how many more/altogether (holiday Q1-Q5); true-false from a graph; "what can a small vote tell us" (Q6-Q7, as a Yes/No/We cannot tell choice); draw a row from a difference or total clue (holiday Part B and stretch); scale 2 with half pictures and comparing keys (holiday stretch, new keys 2 and 5); build a graph from clues (catalogue EX-CHAL-1/2 style, new numbers).
Unit 4: next shape; far place by counting in the core (holiday Q1-Q6, new cores: star/heart/heart, dark/dark/white, M N O, clap/clap/stomp, sun/moon/moon); places of one shape (2, 5, 8 ...); how many of a shape in the first N; growing towers (new context, +3); sticks in a row of triangles (holiday Q7 skeleton, other counts and questions); beads/stickers adding 2 or 3 a day.

## Beyond Level 1 items (printed label, Think harder / Go further only)
U3: T01 Keys bigger than 1; T03 Comparing two keys; G01 Build a graph from clues. U4: G01 Jumps that grow (1, 2, 4, 7, 11); G02 Two ways to build (separate triangles 3n sticks against a shared row 2n+1); G03 Two patterns together (star above a C).

## Choices made
- Start here has 10 items (unit 3) and 13 (unit 4), not 13 to 14: with the large type and the graph/figure pictures more items overflow a page (the build gate fails over 100 percent). Go further has 3 items in each unit. Fill range 0.85 to 1.0 on every page.
- Picture graphs are 1 picture = 1 in Start here (as in the P1 school-paper pattern); keys of 2 and 5 only in Think harder.
- Check yourself quiz items are single-line stems; the quiz graph item has no "Working" line (small edit in `render.py`: an item with a figure gets no working row), so the page fits.
- Shaded versus empty beads: "dark" and "white" beads (solid black or empty in both editions). Cookie pictures print as solid black discs in the B&W edition (the project recolour rule for small yellow circles).
- Figure scale: 0.14 mm per drawing unit for read-only graphs (about 5.6 mm pictures), 0.15 to 0.17 for graphs a child draws in.
