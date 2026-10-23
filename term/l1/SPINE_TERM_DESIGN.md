# Spine for the term lessons: design (Level 1, lessons 1 to 40)

Phase A design, 23 Oct 2026. Branch `claude/great-fermi-1hv4vc`. Nothing in `lessons/*.json`, `b_print.py`, `b_guide.py`, `b_deck.py`, `validate.py`, books or `out/` has been changed. New files only: `term/l1/spine_term.json`, `term/l1/tools/spine_term.py`, `term/l1/tools/apply_spine_term.py` (dry run by default; not applied) and this note. Owner decision: SPINE-TERM-NOW (add the strategy card and the common look-back to the 40 Level 1 term lessons, as already done for the holiday program). Sources read: `docs/pedagogy/spine_routine_spec.md`, `spine_routine_build_notes.md`, `toolbox_card_notes.md`, `levels/spine.json`, `levels/spine_wb.js`, `spine_guide.js`, `spine_deco.py`, `term_review.md` sections 2, 6 and 8, `lesson_x10_consolidation_plan.md`, `AUTHORING.md`, `b_print.py`, `b_guide.py`, `b_deck.py`, `common.py`, `validate.py` and all 40 lesson files.

How the numbers below were obtained (so they can be trusted, and repeated): I copied `term/l1` to a scratch folder, applied the patch there, and ran the real builders (`b_print.build_print`, `b_deck.build_deck`, `b_guide.build_guide`) for all 40 lessons, once unpatched and once patched, in the same environment. "Measured" means that. The scratch copy was a snapshot taken while the diagram agent was still editing, so the timing columns are a snapshot too: the patch recomputes every timing decision when it runs.

## 1. The design in eight lines

1. One data file chooses the tool: `term/l1/spine_term.json` (main tool, up to two "also useful", role I/P/A/C, one-line reason, per lesson). Wording of names, definitions and the three look-back questions stays only in `levels/spine.json` (band A, ages 6 to 8).
2. Each lesson file gets a `spine` object and a few script lines marked `"spine"`; the builders read it. A lesson without `spine` builds exactly as before.
3. Workbook: a tool chip under the name line on the Start here page (beside Mi, about 11 mm), and the common look-back box (three questions, "Tool I used" row, stuck and pass) in place of the old tick box on the last page.
4. Tutor guide: a "Tool of the day" row, a small toolbox box, the Opening SAY and DO, one Talk question, and the three look-back questions with the same stuck route as today.
5. Deck: a "TODAY'S TOOL" pill on the title slide and a rebuilt Look-back slide. No new slide, no minute changes.
6. Tutor timing stays 90 minutes: no part minutes change; the new lines are added only where the script still fits (the patch tests each lesson with `common.py` and picks the richest variant that fits).
7. Tools are shown only as they are met, by term (Term 1 four, Term 2 six, Term 3 seven, Term 4 eight), as the consolidation plan says. Lessons 10, 20, 30, 40 (and 39) show "Choose one": no single tool.
8. Phase B is one command (`apply_spine_term.py --apply`), then validate, build, look, rebuild the books. All 40 workbooks built to their designed page counts in the measured run.

## 2. Where each piece lives

| Piece | File | Status |
|---|---|---|
| Tool names, band A definitions, look-back questions, labels | `levels/spine.json` | unchanged, single source |
| The choice for each of the 40 lessons, tools met by term, compact-chip list, term look-back and Opening/Talk wording | `term/l1/spine_term.json` | new |
| Chip, look-back box, deck pill, guide row (no wording of their own) | `term/l1/tools/spine_term.py` | new |
| Patch: lesson files, 4 tools, schema, AUTHORING note | `term/l1/tools/apply_spine_term.py` | new, dry run by default |
| Hooks | `b_print.py`, `b_guide.py`, `b_deck.py`, `validate.py` | edited in Phase B by the patch |

The patch touches only: `lessons/l01.json` to `l40.json`, `tools/b_print.py`, `b_guide.py`, `b_deck.py`, `validate.py`, `schema/lesson.schema.json`, `AUTHORING.md`. It uses text anchors, not line numbers, and reports "ANCHOR MISSING" instead of guessing. Dry run today: 46 files would change. Applied twice in the scratch copy: the second run reports 0 files would change.

## 3. Tool of the day, lesson by lesson

How chosen: for each lesson I read the Start here items, the Explore and Mini-lesson slide titles, the Talk question, Think harder and Go further, and the look-back "what helped" list, and picked what the children do most in Start here and Explore. "Also useful" is something the lesson really uses (at most two). Both must be tools already met in that term (Term 1: Draw it, Act it out, Spot the pattern, List every way; Term 2 adds Make a table and Work backwards; Term 3 adds Guess and check; Term 4 adds Try something simpler). I did not copy the holiday mapping. Role: I = first main use, P = practised (Terms 1 and 2), A = applied (Terms 3 and 4), C = child chooses.

Counts as main tool: Draw it 7, Act it out 7, Spot the pattern 6, List every way 4, Make a table 4, Work backwards 4, Guess and check 2, Try something simpler 1, Choose one 5 (lessons 10, 20, 30, 39, 40).

| L | Lesson | Tool of the day (role) | Also useful | Why (tutor line) |
|---|---|---|---|---|
| 1 | Bundles and Singles | Act it out (I) | Draw it | Children bundle real sticks first; Start here then asks them to draw bundles and singles. |
| 2 | Number Words and the Number Line | Draw it (I) | Act it out | Every Start here item sits on a number line, and the frog hops are acted out before they are drawn. |
| 3 | Digit Cards | List every way (I) | Act it out | Children make every number from two cards in order, then three cards, then four, moving the kit cards. |
| 4 | The 100 Square Explorer | Spot the pattern (I) | Act it out | Colouring 10s, 5s and 2s shows what repeats and what grows; a counter moves down the square. |
| 5 | Make-a-Ten Adding | Act it out (P) | Draw it | Counters move on ten-frames to fill a ten; children draw the dots and ring the ten. |
| 6 | Tens Jump, Ones Hop | Spot the pattern (P) | Draw it | Each jump of ten changes the tens digit and keeps the ones; the Investigation asks if the jumps land on 50. |
| 7 | Take Away, Count Up | Draw it (P) | Act it out | Bars and a number line show the gap; children also take away and count up with real bars and squares. |
| 8 | Balance and Swap | Act it out (P) | Draw it | Children move real small things between two plates and see what stays equal. |
| 9 | Draw and Measure | Draw it (P) | Act it out | Every task is drawn to size (a 7 cm line, a bent path); children measure real things first. |
| 10 | Story Steps: Read It Twice | Choose one | - | Choose-the-tool lesson (consolidation plan): the child picks one of the four tools met in Term 1 for each story. |
| 11 | Who Is Where? | Act it out (P) | Draw it | Children stand toys in a line and touch each place; Think harder and Go further are drawn. |
| 12 | Bar Strips: More and Fewer | Draw it (P) | Work backwards | The strip is the picture of the story; sum-and-difference items are solved by undoing the gap. |
| 13 | Doubles and Near Doubles | Spot the pattern (P) | Act it out | Each near double is one more or one less than a double; counters show the extra one. |
| 14 | Odd + Odd: Always, Sometimes, Never | Act it out (P) | Spot the pattern | Counters in pairs show why odd and even behave as they do; then children test many sums. |
| 15 | Equal Groups | Make a table (I) | Draw it, List every way | Groups, number in each group and total go in a table; plates are drawn and ways to group 12 are listed. |
| 16 | Skip-Count Tables | Spot the pattern (P) | Act it out | Last digits of the 2s, 5s and 10s repeat; a counter hops along the line as the frog. |
| 17 | Sharing and Grouping | Act it out (P) | List every way | Children deal counters onto plates; Go further lists every number of friends that share 12. |
| 18 | Times Stories | Draw it (P) | Work backwards | Equal strips show 'twice as many'; the hidden-unit items are solved by undoing the total. |
| 19 | Picture Equations | Work backwards (I) | List every way | Start from the total and undo to find each shape; the Investigation lists the pairs that fit a line. |
| 20 | Find One First | Choose one | - | Choose-the-tool lesson (consolidation plan, Tool Market): the child picks one of the six tools met by Term 2. |
| 21 | What Time Is It? | Spot the pattern (A) | Act it out | The long hand counts in 5s round the face; the kit clock is set and moved by hand. |
| 22 | Five Minutes at a Time | Draw it (A) | Spot the pattern | Hands and 5-minute steps are drawn on a clock and a time line; counting in 5s is the helper. |
| 23 | Time Passes | Work backwards (A) | Draw it | From the end time, count back to find the start; a time line shows the jumps. |
| 24 | Dollars and Change | List every way (A) | Guess and check, Work backwards | Children list the ways to make an amount, try sets for the fewest coins, and find a price from change. |
| 25 | Price Tags: Compare and Choose | Guess and check (I) | Draw it | Try two tags, check the total or the gap, then try again; strips show how much more. |
| 26 | The School Shop | List every way (A) | Make a table | Every way to spend exactly $20 is listed in order, with a row for each number of books. |
| 27 | Fill the Grid | Guess and check (A) | Act it out | Place a tile, check its row and column, and change it if it breaks a rule. |
| 28 | Make a Table | Make a table (A) | Spot the pattern, Work backwards | A table of sticks per picture finds the 10th picture; Go further works back from a total. |
| 29 | Spot the Mistake | Work backwards (A) | - | Add back, or take away, to check a sum; the wrong step is found by undoing the working. |
| 30 | Calendar Detective | Choose one | - | Choose-the-tool lesson (consolidation plan, Tool Detectives): the child picks one of the seven tools met by Term 3. |
| 31 | Half and Quarter | Draw it (A) | Work backwards | Children cut and colour shapes in equal parts; from one quarter they work back to the whole. |
| 32 | Build the Figure | Make a table (A) | Draw it | Shapes in a figure are counted by kind into a table; a ruler splits a figure into its shapes. |
| 33 | Copy on the Grid | List every way (A) | Try something simpler | Routes are listed in order so none is missed; the 3 by 1 and 2 by 2 grids come before bigger ones. |
| 34 | Cubes and Views | Act it out (A) | Draw it | Children build the stack and fold and punch real paper; top views are drawn. |
| 35 | Spot It | Spot the pattern (A) | Act it out | Tiles repeat and a missing piece follows the pattern; cards are turned and compared by hand. |
| 36 | Count Everything | Try something simpler (I) | List every way, Make a table | Handshakes among 2, 3, then 4 children, and squares in 1 by 1 then 2 by 2 grids, show how the count grows. |
| 37 | Make Your Own Graph | Make a table (A) | Work backwards | Tally marks go into a table before the graph; a missing bar comes from the total. |
| 38 | Graph Detectives | Work backwards (A) | Draw it | A missing bar is the total take away the bars you know; graphs are drawn from clues. |
| 39 | The Problem-Solving Toolbox | Choose one | - | Teaches how to choose a tool. Its tool cards still use the lesson's own seven names; the plan rebalances them to the eight card names. |
| 40 | Inquirers' Showcase | Choose one | - | Choose-the-tool lesson with the Showcase and the Quest: children teach their favourite idea and pick the tool that fits. |

**Where this follows `term_review.md` 2.2 and where it does not (and why).**
- Follows: Spot the pattern introduced in 4 and practised in 16, applied 21 and 35; List every way introduced in 3, applied 24, 26, 33; Draw it in 2, 9, 12, 18, 31; Work backwards named in 12 and 18 (as "also"), main in 19, 23, 29, 38; Guess and check main in 25 and 27 (Term 3 only, as the plan says); Make a table main in 28, 32, 37.
- Differs: Act it out is introduced in Lesson 1 (not 10) and Make a table in Lesson 15 (not 20), because 10 and 20 are now choose-the-tool lessons. Work backwards main starts at 19 (not 12) because Term 1 and early Term 2 hold only the plan's tool sets. Try something simpler is the main tool in one lesson only (36, handshakes among 2, 3, 4 children); it is "also" in 33. Guess and check has no main lesson in Term 4 (term review gap, left as it is: the plan says do not add a guess-and-check lesson).
- Honest limits: Draw it and Act it out are the base tools and dominate Terms 1 and 2. List every way is main in only 4 lessons although it is "also" in 5 more. If the owner wants a stronger Try something simpler thread, the candidates for a main swap are 33 and 5; the cost is that Lesson 36 then shows List every way.

**Choose lessons.** 10, 20, 30, 40 per decision 2. Lesson 39 (The Problem-Solving Toolbox) is also marked "choose" because its whole job is picking the tool (the plan makes it "the lesson that teaches how to choose"). The owner may give 39 a single tool instead. In a choose lesson the chip is a row of the tools met so far with an "I chose" tick under each; no tool of the day.

## 4. What changes in the pipeline, output by output

### 4.1 Workbook (`b_print.py`): four small hooks and one CSS block

- **Import:** `import spine_term as SPT` after `import svg`.
- **Strategy chip on the Start here page.** In `hdr()` the line that returns the header with Mi (`head[i:] + f'</div>{img}</div>'`) becomes `head[i:] + SPT.wb_chip(d, compact) + f'</div>{img}</div>'`. Only page 1 calls `hdr(..., mi=True)`, so only page 1 gets it. The chip sits in the left column under the Name and Date line, beside Mi (Mi is 22 mm tall; the name line plus a two-row chip is about 22 mm, so the page grows by about nothing). Two rows, about 11 mm: icon 10 mm, "TOOL OF THE DAY", tool name in Fredoka 13 pt, tick box "I used it", then the band A definition and "Also useful: ..." at 9 pt. Border 0.5 mm navy, white fill, no tint. Five lessons (11, 15, 19, 31, 37) use a one-row compact chip (icon, name, tick, "also"; about 9 mm, no definition) because their page 1 was already full; this is `spine.chip = "compact"`, set from `chip_compact_lessons`.
- **Tool row on page 1 in a choose lesson:** the chip is the row of tool icons met so far, each with a tick "I chose" (about 15 mm).
- **"Tool I used" look-back replacing the generic tick box.** One line before `if wb(d, 'exit_page', False):` in `workbook_html()`: `look = SPT.wb_lookback(d) or look`. The old `.lbk` box (Something I did well, hardest part, what helped me, next time I will try, stuck and pass) is replaced by one box of the same width on the last page: heading "Look back" and the intro "Pick one problem from today. There are no right answers. You can pass. Nobody reads it out."; question 1 "Did I answer the question?" and question 2 "Does my answer make sense?" with yes and not yet ticks; question 3 "Can I check it another way?" with "draw or write one word" and a dotted line; the "Tool I used" row (icons with tick boxes: the tools met so far, 4 to 8); then "I am still stuck (my grown-up will photograph this page for my tutor)" and "pass". The stuck words are the existing ones, so the WhatsApp route is unchanged.
- **CSS:** `SPT.CSS` is added after `{EXTRA}` in the workbook `<style>`. It makes the new box follow the builder's own tightening classes (`tight`, `tight2`, `tight3`), as the old box did. Without this the box does not shrink on a full page and 3 lessons spill (found in the first experiment).
- **Home sheet:** `home_html()` intro paragraph gets one sentence: "The tool of the day was Draw it. Draw a picture or a bar of what the story says." (choose lessons: "In the lesson you chose your own tool. Which tool will you use today?"). Cost about one line; the existing `hm t1..t3` loop absorbs it.
- **Not changed:** key, parent summary, kit pages, Quest Log (`b_quest.py` is being changed by the consolidation work: it should read the same `tools_met` list so the Quest tool row and the look-back row match).

### 4.2 Tutor guide (`b_guide.py`) and the script lines (lesson files)

`b_guide.py`: import; one `rows.insert(1, SPT.guide_row(d))` so "At a glance" gets a **Tool of the day** row (name, role, definition, also, the one-line reason); one box before "Before the lesson" with the tools met so far (band A words, today's marked) and the three look-back questions; and the Look-back paragraph (section 4) is replaced by the three prompts, the Tool I used row and the stuck route.

Script lines (added to the lesson files by the patch, each marked `"spine"`, so the timing check counts them):
- **Opening:** SAY "Today's tool is {name}. {definition}" and DO (4 s) "Point at the tool on page 1 of the workbook." In a choose lesson: "Today you choose the tool." and "Point at the row of tools on page 1 of the workbook."
- **Talk:** ASK "Where did you use {name} today?" (10 s answer window) and a NOTE "Listen for the tool being named, not the answer. Volunteers first, a pass is always fine." In a choose lesson the ask is a NOTE only (no modelled time).
- **Look-back:** the SAY line is replaced by the common words (55 words, about 28 s): "Pick one problem from today. Did I answer the question? Does my answer make sense? Can I check it another way? Tick, write one word, or pass. If you tick I am still stuck, ask your grown-up to photograph this page after class and send it to our business WhatsApp. Then we will help you." The WORK line becomes "Children fill in the look-back box on page 5. Nobody reads theirs out. Praise a check you saw, not speed." and its seconds are raised to the most that keeps the slow-class case inside the part (never below today's value, at most 120 s). The speaker note of the Look-back slide is rewritten the same way (the row names "Something I did well" and "Next time I will try" are removed).
- **Lesson 1 only:** a NOTE "Eight tools: see your Toolbox card ..." and a `tutor_prep` line about the card (section 4.6).

### 4.3 Tutor timing: stays 90 minutes

No `timing.parts` value changes, so slide minute badges, recording chapters, the guide timing table and the 90 sum are untouched. The patch builds up to five variants per lesson and takes the richest one that passes the same tests as `validate.check_timing` (every part fits its minutes, scripted need at most 86 minutes, slow class at most 90 minutes): (a) Opening SAY and DO plus the Talk ASK, (b) the same with the Talk question as a NOTE, (c) SAY only, (d) notes only, (e) as a last resort notes only and the children's look-back time cut in 5-second steps (not below 80 seconds). If the Opening is full it puts the same two lines at the start of Remember (these lines are then marked `remember`). Result in the snapshot: the full variant (a) fits in 37 lessons; (b) in 1 (Lesson 3); (d) notes only in 2 (Lessons 6 and 9; for Lesson 9 the children's look-back time is also cut from 100 to 95 seconds, otherwise the slow-class total is 1 to 2 seconds over 90 minutes); and in 18 lessons the two lines sit at the start of Remember because the Opening is full. Six lessons get one new advisory warning ("slow class over the part; the buffer absorbs it"), no new FAIL. Where only a reduced variant fits (Lessons 3, 6 and 9) the tutor still sees the line as a note; if the owner wants the full line there, a human must trim about 10 to 25 seconds elsewhere in that lesson (the repeated 25-second greeting DO is the obvious candidate). The look-back box is a different shape from the old one but the same time.

### 4.4 Deck (`b_deck.py`)

- Title slide: a "TODAY'S TOOL" pill (cream icon, name) at the bottom left (y 946 to 1016). The lowest content on the 40 title slides ends at y 910, and the footer text is at y 1030, so nothing moves; Mi and her bubble are on the right. In a choose lesson the pill shows the tools met so far.
- Look-back slide: `lookback(d)` returns the new body: three prompts at 50 px with yes and not yet, the Tool I used row, stuck and pass. Same card width limit (1560 px) so Mi stays clear. No timer label (AUTHORING: no timers shown as races).
- No new slide, no change to `deck.json` order or slide minutes. Measured: all 40 decks build with the same problems as before (5 existing overflows on workbook slides in lessons 9, 21, 23, 25, 26 that have nothing to do with this change) and no new overlap.

### 4.5 Online practice

No change. The runner has no look-back and does not name tools; a "tool" line on the practice page would need a runner change and is not worth it now.

### 4.6 Kit and Toolbox card

The A5 Toolbox Card for ages 6 to 8 exists (`outputs/kit/Math_Inquirers_Toolbox_Card_A_6-8_PRINT_BW.pdf` and `_SCREEN_colour.pdf`); it shows all eight tools. The term program has no Inquirer Kit, so the Lesson 1 note says "Eight tools: see your Toolbox card" (not "Inquirer Kit card") and the `tutor_prep` line tells the tutor to print one A5 card per child or send the PDF with the welcome message. Decision for the owner: ship it with Book 1 (a loose A5 card, listed in `docs/printing/quote_request.md` as one per child per enrolment) or as a PDF only. One mismatch to know about: lessons show four tools in Term 1, the card shows eight. Either say so in the tutor note (done for Lesson 1) or make a Term 1 card of four (not built).

## 5. JSON fields added

- `spine` (new top-level object in each lesson, placed after `skill`): `main` (a tool id or `choose`), `also` (0 to 2 ids), `role` (I, P, A, C), `reason` (one line, tutor only), optional `chip` (`compact`). Declared in `schema/lesson.schema.json`; not in `REQ_TOP` (a lesson without it still builds).
- `script.segments[].lines[]`: new lines carry `"spine": "opening" | "remember" | "talk"`. The rewritten look-back SAY and WORK lines carry `"spine": "look"`. The marker is how the patch stays idempotent.
- Changed text (no new keys): the look-back SAY and WORK lines; the Look-back slide `note`; Lesson 1 `tutor_prep`.
- Not changed: `look_back.hardest/helped/next` stay in the files (the validator still reads them; no output prints them for a lesson with `spine`). Remove them in a later clean-up.
- `term/l1/spine_term.json` keys: `lessons` (the 40 rows), `tools_met`, `chip_compact_lessons`, `look_back`, `script`, `choose_lessons`.
- `validate.py`: new `check_spine` (valid ids, at most two also, tools within the term's set, equal to `spine_term.json`, look-back words present, a warning if there is no Opening line).

## 6. How the look-back reads today (all 40 lessons)

- Workbook, deck and guide all print the same four rows in every lesson: **Something I did well** (write or draw one thing), **The hardest part was ...** (4 or 5 lesson-specific ticks, last "something else"), **What helped me** (4 or 5 lesson-specific ticks, mostly "drawing it", "trying again", "I asked for help", "I was not stuck"), **Next time I will try** (3 or 4 ticks such as "drawing it", "using objects", "checking my answer", "asking a question"), then "I am still stuck (my grown-up will photograph this page for my tutor)" and "I would like to pass". The lists are in `look_back.hardest/helped/next`; the three lists differ per lesson, the rows do not.
- Script: one SAY and one WORK line (35 to 100 s) in each lesson, in six near-identical wordings (21 + 7 + 6 + 4 + 1 + 1 lessons, differing only in quotation marks and the stuck sentence). It says "Tick what was hard and what helped you. Write or draw one thing you did well. If you like, tick one thing to try next time. You can pass. Nobody reads it out." and then the stuck route: the photo and business WhatsApp in 33 lessons, "show your grown-up" in the other 7 (an older wording that does not match the workbook line; the new SAY makes all 40 the same).
- Slide note: "Three minutes ..." (36 lessons) or "Two minutes ..." (4 quest lessons), "Children tick or write the look-back box on page 5", and "The Next time I will try row is optional" (36 lessons).
- Nothing asks "which tool did you use" or "did you check"; the term review finding is exactly this.
- What is lost: the tutor no longer sees "the hardest part" or "something I did well". Same trade as holiday decision D3. The exit-ticket answers and the Talk part remain the signals. The "Next time I will try" nudge at the start of the next lesson goes; the new "Where did you use {tool}?" question replaces it.

## 7. Page-count and fit risk, measured

Rules that matter: pages per lesson must not change (the books start each lesson on a right-hand page and pad with blanks; a lesson that gains or loses a page changes the contents numbers, the number of blank pages, the sheets and `term_books_spec.json`, and invalidates quotes); the page-fill rules of `AUTHORING.md` point 14 apply.

Summary of the measured run (patched against unpatched, same environment):
- **Workbook pages: 40 of 40 built to the designed page count** (the same as unpatched). Unpatched: 40 of 40 as well. With the two-row chip alone 5 lessons overflowed (11, 15, 19, 31, 37); the compact chip fixes those 5. With a look-back box that ignored the tightening classes 3 more spilled (18, 34, 35); the CSS fixes them.
- **Last page** (Investigation, exit ticket, look-back) gets easier: pages at maximum tightening fall from 22 to 2 lessons.
- **Page 1 has no spare tightening in 13 lessons** (8, 11, 15, 19, 21, 23, 26, 31, 33, 34, 35, 37, 38); 11 were already at the limit unpatched and 21, 26 are new. They pass, but any later content change on their page 1 can cost a page. Watch list for Phase B.
- **Home sheet:** all 40 stay one page; 12 sheets needed one more tightening step (lessons 2, 3, 4, 7, 11, 14, 15, 16, 17, 21, 29, 34); lessons 15 and 29 are now at the last step (t3).
- **Tutor guide:** +16 pages over 40 guides (largest +2, in lessons 35, 37, 38).
- **Deck:** 0 new problems.

Per lesson (page counts are designed / built; "t0 to t3" is the builder's tightening class on that page, 0 = none, 3 = the most; fill = how full the page is):

| L | Pages designed / built | Chip | Page 1 fill and tightening, before > after | Last page, before > after | Home sheet tightening | Script lines added | Guide pages |
|---|---|---|---|---|---|---|---|
| 1 | 6 / 6 | two-row | 0.93 t1 > 0.95 t1 | 0.94 t2 > 0.95 t1 | t1 > t1 | SAY+DO, ASK in Remember | 20 > 20 |
| 2 | 7 / 7 | two-row | 0.93 t0 > 0.95 t0 | 0.99 t1 > 0.93 t1 | t0 > t1 | SAY+DO, ASK in Opening | 21 > 21 |
| 3 | 7 / 7 | two-row | 0.91 t0 > 0.94 t0 | 0.98 t2 > 0.96 t1 | t1 > t2 | SAY+DO, note in Remember | 20 > 20 |
| 4 | 6 / 6 | two-row | 0.97 t2 > 0.99 t2 | 0.93 t2 > 0.96 t1 | t1 > t2 | SAY+DO, ASK in Opening | 20 > 20 |
| 5 | 6 / 6 | two-row | 0.96 t0 > 0.90 t1 | 0.99 t3 > 0.96 t2 | t1 > t1 | SAY+DO, ASK in Opening | 20 > 20 |
| 6 | 6 / 6 | two-row | 0.93 t1 > 0.95 t1 | 0.94 t3 > 0.91 t2 | t2 > t2 | notes only in Opening | 20 > 20 |
| 7 | 6 / 6 | two-row | 0.90 t0 > 0.92 t0 | 0.99 t2 > 0.99 t1 | t0 > t1 | SAY+DO, ASK in Remember | 20 > 20 |
| 8 | 6 / 6 | two-row | 0.98 t3 > 1.00 t3 | 0.93 t3 > 0.90 t2 | t1 > t1 | SAY+DO, ASK in Remember | 21 > 21 |
| 9 | 5 / 5 | two-row | 0.84 t0 > 0.86 t0 | 0.99 t3 > 0.96 t2 | t1 > t1 | notes only, look-back 95 s in Opening | 20 > 20 |
| 10 | 6 / 6 | choose row | 0.96 t0 > 0.91 t1 | 0.90 t2 > 0.95 t1 | t1 > t1 | SAY+DO, ASK in Opening | 23 > 23 |
| 11 | 6 / 6 | compact | 0.99 t3 > 1.00 t3 | 0.97 t3 > 0.91 t2 | t0 > t1 | SAY+DO, ASK in Opening | 22 > 23 |
| 12 | 6 / 6 | two-row | 0.96 t1 > 0.96 t2 | 0.99 t2 > 0.93 t2 | t1 > t1 | SAY+DO, ASK in Remember | 21 > 21 |
| 13 | 6 / 6 | two-row | 0.95 t2 > 0.98 t2 | 0.97 t3 > 0.94 t2 | t2 > t2 | SAY+DO, ASK in Remember +1 warn (talk slow class) | 21 > 21 |
| 14 | 6 / 6 | two-row | 0.95 t0 > 0.97 t0 | 0.98 t2 > 0.98 t1 | t1 > t2 | SAY+DO, ASK in Remember +1 warn (talk slow class) | 21 > 21 |
| 15 | 7 / 7 | compact | 0.98 t3 > 0.99 t3 | 0.97 t3 > 0.96 t2 | t2 > t3 | SAY+DO, ASK in Remember | 20 > 20 |
| 16 | 6 / 6 | two-row | 0.96 t2 > 0.98 t2 | 0.97 t3 > 0.96 t2 | t0 > t1 | SAY+DO, ASK in Remember +1 warn (talk slow class) | 18 > 18 |
| 17 | 6 / 6 | two-row | 0.91 t0 > 0.94 t0 | 0.99 t2 > 0.96 t2 | t1 > t2 | SAY+DO, ASK in Remember +1 warn (talk slow class) | 22 > 22 |
| 18 | 6 / 6 | two-row | 0.95 t1 > 0.95 t2 | 0.99 t3 > 1.00 t2 | t2 > t2 | SAY+DO, ASK in Remember | 21 > 21 |
| 19 | 7 / 7 | compact | 0.99 t3 > 1.00 t3 | 0.99 t3 > 0.96 t2 | t1 > t1 | SAY+DO, ASK in Remember +1 warn (talk slow class) | 21 > 21 |
| 20 | 6 / 6 | choose row | 0.96 t1 > 0.99 t1 | 0.96 t2 > 0.98 t1 | t0 > t0 | SAY+DO, ASK in Remember | 21 > 21 |
| 21 | 6 / 6 | two-row | 0.99 t2 > 0.98 t3 | 0.98 t2 > 0.95 t2 | t1 > t2 | SAY+DO, ASK in Opening | 22 > 22 |
| 22 | 6 / 6 | two-row | 0.97 t2 > 0.99 t2 | 0.99 t2 > 0.94 t2 | t1 > t1 | SAY+DO, ASK in Opening | 22 > 22 |
| 23 | 5 / 5 | two-row | 0.93 t3 > 0.95 t3 | 0.96 t3 > 0.93 t2 | t0 > t0 | SAY+DO, ASK in Opening | 21 > 21 |
| 24 | 7 / 7 | two-row | 0.94 t1 > 0.95 t2 | 1.00 t3 > 0.97 t2 | t1 > t1 | SAY+DO, ASK in Opening | 20 > 21 |
| 25 | 6 / 6 | two-row | 0.96 t1 > 0.95 t2 | 0.96 t3 > 0.93 t2 | t1 > t1 | SAY+DO, ASK in Remember | 23 > 23 |
| 26 | 5 / 5 | two-row | 0.95 t2 > 0.94 t3 | 0.93 t2 > 0.90 t2 | t2 > t2 | SAY+DO, ASK in Remember | 21 > 22 |
| 27 | 6 / 6 | two-row | 0.96 t0 > 0.94 t1 | 1.00 t2 > 0.93 t2 | t1 > t1 | SAY+DO, ASK in Opening | 20 > 21 |
| 28 | 6 / 6 | two-row | 0.85 t0 > 0.87 t0 | 0.95 t3 > 0.92 t2 | t1 > t1 | SAY+DO, ASK in Opening | 19 > 20 |
| 29 | 6 / 6 | two-row | 0.94 t0 > 0.97 t0 | 0.96 t3 > 0.93 t2 | t2 > t3 | SAY+DO, ASK in Remember | 21 > 22 |
| 30 | 6 / 6 | choose row | 0.95 t0 > 0.98 t0 | 0.93 t2 > 0.98 t1 | t1 > t1 | SAY+DO, ASK in Opening | 22 > 23 |
| 31 | 8 / 8 | compact | 1.00 t3 > 1.00 t3 | 0.99 t3 > 0.94 t2 | t0 > t0 | SAY+DO, ASK in Opening | 23 > 23 |
| 32 | 7 / 7 | two-row | 0.93 t1 > 0.95 t1 | 0.96 t3 > 0.91 t2 | t1 > t1 | SAY+DO, ASK in Opening +1 warn (opening slow class) | 23 > 23 |
| 33 | 6 / 6 | two-row | 0.97 t3 > 0.99 t3 | 0.98 t3 > 0.95 t2 | t1 > t1 | SAY+DO, ASK in Remember | 21 > 22 |
| 34 | 6 / 6 | two-row | 0.93 t3 > 0.95 t3 | 0.98 t3 > 0.93 t3 | t1 > t2 | SAY+DO, ASK in Opening | 21 > 22 |
| 35 | 6 / 6 | two-row | 0.97 t3 > 0.99 t3 | 0.99 t3 > 0.95 t3 | t2 > t2 | SAY+DO, ASK in Opening | 20 > 22 |
| 36 | 6 / 6 | two-row | 0.94 t0 > 0.96 t0 | 0.97 t3 > 0.96 t2 | t1 > t1 | SAY+DO, ASK in Opening | 20 > 21 |
| 37 | 6 / 6 | compact | 0.99 t3 > 1.00 t3 | 0.95 t3 > 0.96 t2 | t1 > t1 | SAY+DO, ASK in Remember | 20 > 22 |
| 38 | 5 / 5 | two-row | 0.94 t3 > 0.96 t3 | 0.95 t2 > 0.90 t2 | t2 > t2 | SAY+DO, ASK in Opening | 20 > 22 |
| 39 | 6 / 6 | choose row | 0.92 t1 > 0.95 t1 | 0.86 t2 > 0.90 t1 | t1 > t1 | SAY+DO, ASK in Opening | 23 > 23 |
| 40 | 5 / 5 | choose row | 0.92 t0 > 0.94 t0 | 0.96 t2 > 0.96 t1 | t1 > t1 | SAY+DO, ASK in Opening | 23 > 23 |

Books (workbook kind, from `outputs/print/term/term_books_spec.json` as read before other agents rebuilt some books; none should change because no lesson changes length): Book 1 (Term 1, lessons 1-5) 46 print pages, 23 sheets, 12 blank; Book 2 (6-10) 44, 22, 9; Book 3 (Term 2, 1-5) 44, 22, 11; Book 4 (6-10) 48, 24, 12; Book 5 (Term 3, 1-5) 42, 21, 10; Book 6 (6-10) 44, 22, 9; Book 7 (Term 4, 1-5) 48, 24, 13; Book 8 (6-10) 42, 21, 8. Every lesson starts on a right-hand page, so an odd lesson (5 or 7 pages) is followed by a blank; the counts above stay the same only while every lesson keeps its designed page count, which the measured run shows. `make_term_books.py` must still be re-run because page contents change; the contents page numbers come out the same.

Anomaly to clear before Phase B: the built `out/l36/L36_Workbook.pdf` in the repo has 7 pages against 6 designed (an orphan page). It is not caused by this change (unpatched builds give 6) but means `out/` is not a clean baseline.

## 8. Black and white

The term books go through `print/make_bw_print.py` (1-bit, 600 dpi) after `make_term_books.py`; the new elements are ink on white, no tint, no colour-only cue.
- Icons are 3-unit strokes. The holiday notes tested legibility at 10 mm; the chip icon is 10 mm, but the look-back "Tool I used" icons are 7 mm (8 mm when four to six tools are shown). Risk: the dotted outline circle of Spot the pattern and the small dots of List every way may fill in at 7 mm. Check at 100 percent in the B&W PDF for lessons with eight icons (Term 4); if they fail, drop the icon size or the intro line before touching anything else.
- Tick boxes 3.6 to 4 mm with a 0.5 mm border and the 0.4 mm dotted line are navy, so they convert to solid black. The old box used a cream fill and a grey dotted line (`#8A94AD`, a mid-tone, converted to a stipple); both go away, which helps.
- The chip sits beside Mi's colour image: no change from today.
- Run `python3 print/make_bw_print.py --only L1_T` then `python3 print/check_bw.py` on the term books (non-grey pixels 0, light-tint cells below the fail level) and look at the first and last page of 6 lessons at 100 percent: 1, 7, 15, 24, 33, 36 (one per band of risk) plus a choose lesson.
- The deck and guide are screen products; no B&W issue.

## 9. Order of work and effort (Phase B)

Prerequisites: the diagram agent has finished (`audit/DIAGRAM_FIXES.md`), the consolidation work on lessons 10, 20, 30 is committed (the patch must read their final script and timing; lesson 10 is already being rewritten in the working tree), and `git status` is clean for `term/l1`.

| Step | Work | Hands-on | Machine wait |
|---|---|---|---|
| B1 | `apply_spine_term.py` dry run; read the diff and the NEEDS HUMAN list; `--apply`; run again (0 files) | 30 min | none |
| B2 | `validate.py NN` for 40 lessons (needs 0 FAIL and the `spine` PASS) | 10 min | 25 min, 4 in parallel |
| B3 | `bash term/l1/build.sh NN` for 40 lessons, 4 in parallel; lessons 10, 20, 30, 40 also build the Quest | 20 min | about 35 min |
| B4 | Fix-ups: compact chip list if a lesson gains a page (expected 0 to 3); manual trims in the lessons that got a reduced variant (about 10 min each); Lesson 7 wording; `audit/` lines | 1.5 h | rebuilds |
| B5 | Look: page 1 and last page of every lesson as contact sheets (4 sheets at 70 dpi, then 8 at readable size), 12 decks (title and Look-back), 6 guides, 6 home sheets | 1.5 h | none |
| B6 | `print/make_term_books.py`, `make_bw_print.py --only L1_T`, `check_bw.py`; confirm `term_books_spec.json` unchanged; `quote_request.md` unchanged | 20 min | 30 min |
| B7 | Records: `owner_decisions.md` line, `DIAGRAM_FIXES`-style log `audit/SPINE_TERM_LOG.md`, commit | 20 min | none |

Total: about 4.5 hours hands-on and 1.5 hours of waiting. Add 1 to 2 hours if the owner wants Lesson 39's tool cards rebuilt on the eight names now, and 1 hour for a Term 1 card of four tools. Terms 2 to 4 first is possible (the patch takes `--lessons 11-40`) but one release of all 40 is simpler to check.

## 10. Risks, and decisions for the owner

1. **Consolidation overlap.** Lessons 10, 20, 30, 40 are being rebuilt as choose-the-tool lessons with their own Quest tool row. The two tool rows (Quest Log and look-back) must come from the same `tools_met` list; and the titles in `spine_term.json` for 20 and 30 are informational and will be stale when those lessons change. Apply the spine after the consolidation, not before.
2. **Lesson 39's tool cards** still use the lesson's seven own names and pictures (strip, table, list, draw, work backwards, find one first, steps; `t_*` icons). Two toolboxes in one year is the failure this change is meant to remove. The consolidation plan rebalances the wording; the tool-card kit page and its slides need the eight names (not in this patch).
3. **The word "tool"** is now the program's word for the eight strategies. Lesson 7 uses it 17 times for "take away" and "count up" ("Choose your tool"). The patch lists such lessons ("WORDING BY HAND") and does not edit them. Change Lesson 7 to "way" before release.
4. **Reduced variants.** In a few lessons the script is too full for the full line (the patch says which). Owner choice: accept a note in place of a spoken line, or trim time elsewhere.
5. **Opening line in Remember** (18 of 40 lessons): the line is the same, but a tutor looking for it in "Opening" will find it at the start of Remember. Alternative: lengthen Opening by a minute from Explore (changes every minute badge: not recommended).
6. **Retiring "something I did well / hardest part / next time"** (D3 of the holiday spine, applied here). Say yes or ask for one row to stay.
7. **Tools met by term** differs from the holiday look-back (always eight). It follows the consolidation plan and the term review, and it also makes the icons bigger in Terms 1 and 2.
8. **Toolbox card**: ship with Book 1 or send as PDF (4.6).
9. **Claims.** No result promises; "your child will practise" only on any parent text. The parent summary is not changed in this patch; one optional line ("this lesson's tool") could be added to `parent.try_home`, not recommended now.
10. **Try something simpler** has one main lesson (36). That is a content gap of the year, not something the routine can fix.

## What I could not verify

- Timing is the repository's model (`common.py`: 120 words a minute, fixed seconds for children), not a stopwatch; the Opening line, the Talk question and the look-back were never timed with children.
- The black-and-white conversion was not run (Phase A builds in a scratch folder only); 7 mm icons need the 100 percent check in section 8.
- Page counts come from the real builders but in a scratch copy made while other agents were editing lessons 9, 10, 13, 19, 26, 27; the patch recomputes timing at run time, and Phase B must rebuild and re-check pages.
- Whether tutors prefer the tool line in Opening or Remember, and whether a six-to-eight-year-old holds four icons in Term 1 as the plan hopes, are for the first live lessons to show.

## Files in this change

New: `term/l1/spine_term.json`, `term/l1/tools/spine_term.py`, `term/l1/tools/apply_spine_term.py`, `term/l1/SPINE_TERM_DESIGN.md`.
Not changed in Phase A: every existing file.
Commands: `python3 term/l1/tools/apply_spine_term.py` (dry run), `--apply`, `--lessons 1,2,7`, `--only json` or `--only tools`, `--quiet`.
