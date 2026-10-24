# Level 6 Scratch files: checked in the real Scratch editor (23 Oct 2026)

Scope: the 7-point editor check in `docs/audit/fixes_p6.md` and the 13 starter and 13 answer `.sb3` files in `p6/scratch/`. Before today the files had only been checked with `scratch-vm` in node (no browser). Today they were loaded and run in the **real Scratch 3 editor** (https://scratch.mit.edu/projects/editor/, the production build, no sign-in) in headless Chromium (Playwright 1.56, Chromium 141), the way a child opens them: File, Load from your computer. Nothing here uses a mock.

**Result: all 26 files load, draw every block, and give the expected answers when run. 7 of 7 checks pass. No file needed fixing.** Four stale notes in the deck generators that said "no .sb3 exists in the repository" were corrected (section 6).

Scripts (all in `p6/scratch/verify/`, written today, re-runnable): `editor_check.js`, `l7_sizes_check.js` + `make_l7_sizes.py`, `editor_facts.js`, `make_l8_variants.py` + `cases_l8_variants.js`; earlier `check_structure.py` and `vm_check.js` re-run too. Raw results: `docs/audit/scratch_check_p6/*.json`; screenshots in the same folder.

## 1. The 7-point editor check

| # | Check (from fixes_p6.md) | Result | Evidence |
|---|---|---|---|
| 1 | Hat block reads "when [flag] clicked" | Pass. Shown as "when (green flag icon) clicked"; our slides write "when green flag clicked", which names the icon, as the tutor cheat sheet already says. | `palette/palette_Events.png`; every file's editor screenshot |
| 2 | Turn blocks show arrow icons (clockwise and anticlockwise), not "right" and "left" | Pass. `turn ↻ 15 degrees` and `turn ↺ 15 degrees` with arrow icons. Our `turn ↻` matches the first one. | `palette/palette_Motion.png` |
| 3 | Names `item # of ( ) in [list]`, `item ( ) of [list]`, `length of [list]`; `item # of` is not case sensitive | Pass. Palette text: "item (1) of [alphabet]", "item # of (thing) in [alphabet]", "length of [alphabet]". In the editor's runtime `item # of` finds "c" and "C" both at 3, and a space at 0. | `editor_facts.json` (palette list, `vm.itemNumUpper/Lower/Space`) |
| 4 | Sensing is light blue (ask and wait, answer) | Pass. Sensing blocks are `#5cb1d6` (light blue). | `palette/palette_Sensing.png`, `editor_facts.json` |
| 5 | List blocks are red-orange (Variables palette) | Pass. List blocks `#ff661a` (red-orange) sit under Variables, variable blocks `#ff8c1a` (orange). | `palette/palette_Variables.png`, `editor_facts.json` |
| 6 | `( ) mod ( )` with a negative number returns a non-negative result | Pass. -4 mod 26 = 22, -1 mod 26 = 25 in the editor's own operator block; and the whole L8 machine run with shift -4 turns CODE into YKZA and "A B" into "W X". | `editor_facts.json` (`vm.mod`), `l8_variants_results.json` |
| 7 | Sprite fencing at the stage edge for the L7 sizes; L8 machine with spaces | Pass, see sections 3 and 4. | `l7_sizes_results.json`, `stage_drawings/` |

## 2. Every file, static check (`editor_check_results.json`)

For each of the 26 files, after loading in the editor: all block opcodes listed and checked against the editor's runtime (`_primitives` and `_hats`; menus and shadows excluded); every variable, list and broadcast reference resolves; every non-shadow block of the sprite is drawn in the workspace (`undrawn` = 0); no two scripts overlap on screen (`overlaps` = 0); sprite is on the stage; costumes load.

* 26 of 26 files loaded with no error dialog; 0 unknown opcodes, 0 undeclared variables or lists, 0 undrawn blocks, 0 overlapping scripts.
* 34 different opcodes are used in all: `control_if, control_if_else, control_repeat, control_repeat_until, data_changevariableby, data_itemnumoflist, data_itemoflist, data_lengthoflist, data_setvariableto, event_whenflagclicked, event_whenkeypressed, looks_say, looks_sayforsecs, motion_changexby, motion_gotoxy, motion_movesteps, motion_pointindirection, motion_turnright, motion_xposition, operator_add, operator_divide, operator_equals, operator_gt, operator_join, operator_length, operator_letter_of, operator_mod, operator_multiply, operator_random, operator_subtract, pen_clear, pen_penDown, sensing_answer, sensing_askandwait`. All exist in the editor.
* Sprite start positions: every file starts at (0, 0) facing 90 except the two L7 files, which start at (-50, 100) facing 90 with the Pen extension loaded, as the lesson says.
* Lists: `alphabet` has 26 items in both L8 files; `data` is empty in the L9 starter and has 4 items in the answer; `days` has 7 in L10D answer.
* Also `check_structure.py`: 26 files, 0 problems. Block counts per file are in the JSON (for example L8 answer 66 blocks, 2 scripts).

## 3. Lesson 7 drawings (stage size, fencing): `l7_sizes_results.json`

A test-only project (`make_l7_sizes.py`, not given to children) runs every drawing the L7 slides, workbook and Think harder items use, each from the standard set-up (erase all, go to x: -50 y: 100, point in direction 90, pen down), in the editor, pressing its key. For each, the editor's final position and the min and max x and y reached (sampled every 2 ms while it ran) were compared with a turtle simulation, and checked against the 480 x 360 stage (x from -240 to 240, y from -180 to 180).

21 of 21 drawings pass: the triangle (move 100), square, pentagon, hexagon (move 100), octagon, 9-gon and 10-gon (move 80), 12-gon and 15-gon (move 50), 24-gon (move 30), 36-gon (move 10), Ben's nonagon (turn 120), the 5-point star (move 150, turn 144), the Q3 program (9 x move 150, turn 80), the 9-point star (move 120, turn 160), the 20-point star (move 100, turn 54), the 10-point star (move 150, turn 108), the 8-point star (move 100, turn 135), Ali's pentagon (turn 108, correctly does not close), the hexagon trial with turn 120, and the rosette (12 x square plus turn 30) started from x: 0 y: 0. Each ends exactly where the maths says, and all stay on the stage (largest reach: 24-gon x from -149 to 79, rosette -137 to 137), so the editor never fenced a sprite or clipped a line. Screenshots of the stage for the hexagon, three stars and the rosette: `stage_drawings/`. This confirms the earlier hand simulation in `fixes_p6.md` (12 sides at move 80 and the rosette from the standard start do not fit; the lessons do not use them).

## 4. Behaviour: 39 runs in the editor (`editor_check_results.json`, `l8_variants_results.json`)

Each case opens a fresh editor with the file, clicks the green flag (or clicks the stage and presses the key), types the answers into the question box, waits until the project stops, and checks what the sprite said and the variables. All 39 cases of `cases.js` pass, including: L1 302 and "term 333 is 1001"; L2 "15 is not prime" with count 4; L3 -150 and the thermometer -13; L4 7 gives 23, search 12 and 9; L5 1, 2, 3 then 11, 12, 21, 22, 31, 32; L6 coin about 500 heads, dice 2 to 12, doubles about 167; L7 all five answer drawings come home to (-50, 100); L8 MATH IS FUN gives PDWK LV IXQ, XYZ gives ABC, the crack button lists all 25 shifts; L9 mean 8 and largest 12; L10 A to D starters and twists (3n + 4, 91 not prime, 97 prime, about 167 sevens, 9 + 5 gives 2, Thursday + 45 days is Sunday).

**L8 machine with spaces and shifts** (test copies from `make_l8_variants.py`, since the shipped file always starts with shift 3): MYNO SC PEX with shift 16 gives **CODE IS FUN**; PIZZA gives FYPPQ; shift 26 returns MATH IS FUN unchanged; shift -4 (negative mod) turns CODE into YKZA and "A B" into "W X" (the space is kept). Same as the Python results recorded in `fixes_p6.md`.

## 5. What this did not cover

* Costume art was only seen as screenshots (plain SVG shapes, they render).
* The Scratch desktop app and tablets were not tested; the checks are the web editor in Chromium. Scratch changes its editor now and then: re-run `editor_check.js` before the first lesson and after any Scratch update.
* The 7-point check also said "icons": the block drawings in our slides and workbooks are simplified (flat colours, no icons); the lessons say so ("find blocks by the category name on the left, not by colour"), and the actual colours are now recorded above (Events yellow `#ffbf00`, Control `#ffab19`, Sensing `#5cb1d6`, Operators `#59c059`, Motion `#4c97ff`, Looks `#9966ff`, Variables `#ff8c1a`, lists `#ff661a`).
* No child has used the files.

## 6. Changes made because of the check

* Nothing in the 26 `.sb3` files needed changing (`build_sb3.py` output is identical to the files in the repository; the families zip holds the 13 starters, byte for byte).
* Stale text fixed in four deck generators (`rebuild/gen_p6l4.py`, `gen_p6l5.py`, `gen_p6l7.py`, `gen_p6l8.py`): "no .sb3 exists in the repository" and "build the starter once" now name the real files (`L4_Function_Machine.sb3`, `L5_Every_Order.sb3`, `L7_Turtle_Start.sb3`, `L8_Code_Machine.sb3`). Decks, guide, and print outputs were rebuilt (see `final_fixes_p5_p6.md`).
* `p6/scratch/README.md` updated: the "not opened in the editor" caveat is replaced by how to re-run these checks.
