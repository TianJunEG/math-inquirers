# Level 6 Scratch starter files

Scratch 3 projects for the P6 lessons (ages 11 to 13, "maths + coding bridge").
Everything here is our own artwork and our own scripts; no Scratch assets are copied.

| Lesson | Starter (give to children) | Answer key (tutor only) | What the child does |
|---|---|---|---|
| 1 Sequences | `starters/L1_Sequence_Tester.sb3` | `answers/L1_Sequence_Tester_ANSWER.sb3` | Add `change term by 3` inside `repeat 99`. Says 302. Answer key also has the extension (press E: "term 333 is 1001"). |
| 2 Primes | `starters/L2_Prime_Checker.sb3` | `answers/L2_Prime_Checker_ANSWER.sb3` | Add `if n mod d = 0 then change count by 1` and `change d by 1` in `repeat n`. 15 gives count 4, not prime. |
| 3 Negative numbers | `starters/L3_Below_Zero.sb3` | `answers/L3_Below_Zero_ANSWER.sb3` | Backdrop is a number line. Space bar script: add `change x by 100`, `change x by -250` (x = -150). Green flag: thermometer, add `change temp by -3` and `say temp for 1 seconds` (last number -13). |
| 4 Expressions and equations | `starters/L4_Function_Machine.sb3` | `answers/L4_Function_Machine_ANSWER.sb3` | Change `set out to answer` into `(answer * 3) + 2`. Answer key also has the search programs (press S: 8n - 5 = 91 gives 12; press N: n x n + n = 90 gives 9). |
| 5 Counting | `starters/L5_Every_Order.sb3` | `answers/L5_Every_Order_ANSWER.sb3` | One loop says the teas 1, 2, 3. Nest a second loop for toppings: says 11, 12, 21, 22, 31, 32. |
| 6 Probability | `starters/L6_Chance_Lab.sb3` | `answers/L6_Chance_Lab_ANSWER.sb3` | Starter already has the coin program (green flag, 1000 flips) and a two-dice roller (D key). Answer key adds the doubles program (P key, about 167). |
| 7 Angles in polygons | `starters/L7_Turtle_Start.sb3` | `answers/L7_Turtle_Start_ANSWER.sb3` | Pen extension added, the 4 set-up blocks in place (erase all, go to x -50 y 100, point in direction 90, pen down). Child adds `repeat 4 [move 100, turn right 90]`, then triangle and hexagon. Answer key: square (flag), triangle (T), hexagon (H), pentagon (P), 5-point star (S). |
| 8 Clock arithmetic and codes | `starters/L8_Code_Machine.sb3` | `answers/L8_Code_Machine_ANSWER.sb3` | List `alphabet` (A to Z) and the whole loop are built. Child adds the three cipher blocks inside the `if`. MATH IS FUN with shift 3 gives PDWK LV IXQ. Answer key also has a crack button (K key, every shift 1 to 25). |
| 9 Averages | `starters/L9_Mean_Machine.sb3` | `answers/L9_Mean_Machine_ANSWER.sb3` | Empty list `data`; child types numbers into the list, adds `change total by (item i of data)` and `change i by 1` in the loop. Answer key has 5, 9, 6, 12 (mean 8) and a largest-value script (M key). |
| 10 Showcase, starter A | `starters/L10A_Mystery_Machine.sb3` | `answers/L10A_Mystery_Machine_ANSWER.sb3` | Working starter: picks n (1 to 20), shows 3n + 4, checks the guess. Answer key = a sample twist (4n - 1, n up to 50). |
| 10 starter B | `starters/L10B_Prime_or_Not.sb3` | `answers/L10B_Prime_or_Not_ANSWER.sb3` | Working starter: counts factors of a number, says prime or not. Answer key twist: counts the primes up to 30 (10). |
| 10 starter C | `starters/L10C_Lucky_Seven.sb3` | `answers/L10C_Lucky_Seven_ANSWER.sb3` | Working starter: two dice, 1000 rolls, counts 7s (about 167). Answer key twist: counts 8s (about 139). |
| 10 starter D | `starters/L10D_Clock_Jumper.sb3` | `answers/L10D_Clock_Jumper_ANSWER.sb3` | Working starter: start hour plus jump, mod 12 (9 + 5 gives 2). Answer key twist: Day Jumper with a list of weekdays and mod 7 (Thursday + 45 days is Sunday). |

Lesson 10 has no written spec for starter D in the lesson files, so "Clock Jumper" was designed to match the mod 12 idea of Lesson 8. Change it if the tutor team wants something different.

`P6_Scratch_Starters_for_families.zip` holds the 13 child starters only (never the answer keys).

## How a child opens a file

1. Save the `.sb3` file somewhere easy to find (Downloads or Desktop). Do not unzip it.
2. Go to scratch.mit.edu and click **Create** (or open the Scratch app on a laptop).
3. Click **File**, then **Load from your computer**, pick the file.
4. Press the green flag (or the key named in the table). The tutor says what to add.

Keys: the keys in the table (space, D, E, ...) only start scripts when the stage or script area has been clicked; click the stage first if nothing happens.

## How to pass the files to families

- Send the lesson's starter file (or the zip) with the workbook one week before, through the approved channel only (the same channel as the workbook PDF). Attach the file, do not send a link to a shared Scratch project.
- The workbook page 1 header of each lesson names the file ("Scratch file: ...").
- Keep `answers/` with the tutors. Never send it to families.
- Tutors can still build the programs live on a shared screen, as the lesson plans describe; the files are a shortcut and a backup, and help children who fall behind.

## Scratch account steps that are NOT required

- No Scratch account, no sign in, no "Share" button, no remixing and no project link.
- Children never upload to Scratch or publish anything. Nothing leaves their computer.
- Saving is optional: File, Save to your computer.
- No Scratch extensions need to be added by the child (the Pen extension in Lesson 7 is already in the file).

## Making and checking the files

- `build_sb3.py` creates all files (`python3 p6/scratch/build_sb3.py`, standard library only). Edit it, not the `.sb3` files.
- `verify/check_structure.py` checks every project: zip opens, assets match their md5, every block link resolves, no orphan blocks, variables and lists declared, opcodes known.
- `verify/vm_check.js` loads every file in the official `scratch-vm` (npm `scratch-vm@5.0.300`, `scratch-storage`) with no browser and runs it: 39 checks of the expected answers (for example -13, 302, PDWK LV IXQ, mean 8). Run with `NODE_PATH=<folder with node_modules> node p6/scratch/verify/vm_check.js` (it takes about a minute because of `say for 1 seconds`).
- Not done: the files have not been opened in the Scratch editor in a browser (no GUI available). Costume images are plain SVG and only seen by the VM loader, not rendered. If Scratch ever rejects a file, rebuild it with the script and tell the owner.
