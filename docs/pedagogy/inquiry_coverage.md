# Inquiry habit coverage audit (Levels 1-6, holiday and term)

Read-only audit, 24 Oct 2026, branch `claude/great-fermi-1hv4vc`. Companion to `docs/pedagogy/inquiry_skills_explicit.md` (the six habits: Notice, Wonder, Try, Check, Explain, Look back). Nothing outside this file was changed. Website and marketing text is listed in section 7 and not edited.

## 1. Headline findings

1. **No lesson names any of the six habits as habits.** The only inquiry language in the lesson material is the slogan "Notice it. Test it. Explain why." (3 of the 6), the term rules "Notice it / Test it / Explain why / Mistakes help us", the talk-time sentence starters ("I noticed that ...", "I tested it by ...", "I know because ...", on 56 of 60 holiday talk slides) and the Toolbox Card tools. Wonder and Look back appear in no slogan, no badge and no tagged question. The website describes **four** habits (section 7), which is a third framework.
2. **Explain and Try are already strong and need only labelling.** Explain is strong in 46 and ok in 13 of 60 holiday lessons, and strong in 27 of 40 L1 term lessons (talk slide with a "why" question, "How do you know?" in nearly every guide, "I know because ..." starters). Try is ubiquitous (every Start-here page invites a try or a guess).
3. **Look back is the thinnest habit in the holiday course.** Every holiday lesson has the same spine look-back page (3 routine questions plus "Tool I used"), but only 4 of 60 lessons have anything beyond that template (a tutor prompt such as "what was the hardest bug you fixed today?"). The recorded-viewer lines ask "what was hardest, and what will you try next time?" in 31 guides only. None asks "What would I change?" as a look-back question (the phrase occurs once, in a term L39 tutor note about something else). In term L1 the look-back box (hardest / helped / next options, written per lesson) exists in all 40 lessons, so Look back is ok everywhere and strong in 5.
4. **Wonder is the rarest habit in both programmes.** Holiday: it is a core (non-optional) habit in 7 of 60 lessons; in 20 more it appears only in optional Go further / Investigation items ("Make up your own ...", "What if ...?"), and in 31 it is a single slide or tutor "What if" or prediction. Term L1: core in 3 of 40; in the rest the only Wonder is the optional spare-time menu item "Make a puzzle for your grown-up" (shown to children only if the class is ahead) or one "What if?" card in 12 lessons.
5. **Check is strong only where there is a named investigation.** "Is it always true?" is a workbook Investigation in 18 holiday lessons (optional page) and an optional spare-time item ("Is it always true?" or a close variant) in 33 of 40 term L1 lessons. Elsewhere Check means "check by adding back" inside a worked example. The spine look-back question "Can I check it another way?" is a tick box in all lessons.
6. **Notice is weak in both programmes.** Holiday: strong in 8, ok in 18, weak in 34. Term L1: strong in 2, ok in 13, weak or none in 25. "What did we notice?" is a real slide in only 25 term lessons; most Notice prompts sit in optional Investigations ("What do you notice?").
7. **Term material exists only for Level 1** (`term/l1/lessons/l01.json` to `l40.json`). Levels 2-6 have year plans (`docs/terms/level_N_year_plan.md`) but no lesson text, so they cannot be audited; section 6.12 gives the rules to build habits in from lesson 1.
8. **Term arcs conflict with "each term has all six".** `docs/terms/level_1_year_plan.md` line 33 and `docs/pedagogy/term_parent_outcomes_draft.md` name Term 1 "Notice it", Term 2 "Test it", Term 3 "Explain why", Term 4 "Choose and create". Keep these as the emphasis of the year if wanted, but rename them (for example "Term 1 emphasis") so no term reads as practising only one habit.

## 2. Method and limits

**Sources read, per lesson.** Holiday, for each of the 60 lessons: slide text and speaker notes (`split/l1..l10` for Level 1, `split/pNlK` for Levels 2-6, order from each `deck.json`); printed workbook text (`hp/workbook_body.html`, `pN/workbook_body.html`, split by lesson badge, so Start here / Think harder / Go further / Investigation / Look back); tutor guide text (`hp/Math_Inquirers_P1_Tutor_Guide.html`, `pN/Math_Inquirers_PN_Tutor_Guide.html`) and the console script `tutor/data/pNlK.notes.json`; online items (`practice/holiday/pN/NN/lesson.py` as built to `dist/data/pNlNN.json`, the `q` and `src` text and item type). Term L1: all 40 `term/l1/lessons/lNN.json` (slides and notes, tiers, sneak-peek, exit, look-back, home practice, talk, script SAY/ASK/DO lines, spare-time menu, online items). `levels/spine.json` supplies the shared look-back, tool and script wording.

**How a habit was judged.** I looked for the habit as a prompt to the child or tutor, from the lesson's own wording, not from titles: for example "What do you notice?" (Notice), "What if ...?" / "Make up your own ..." (Wonder), "Try ..." / "Guess first" / "test it" (Try), "Is it always true?" / "check by adding" / "test a second case" (Check), "Why ...?" / "How do you know?" / "explain" / "I know because" (Explain), "hardest" / "what helped" / "look back" (Look back). Lines that are the same in many lessons (template text) were separated from lesson-specific text, and the tool-of-the-day names, tool definitions, the slogan, objective and "skills" lines and answer keys were ignored. Tutor-side evidence counts only quoted or scripted prompts.

**Where.** S = slide (child-facing text), W = printed workbook, O = online practice item, G = tutor guide (guide text, console script, speaker notes). `+opt:` lists places where the habit appears only in optional material (slide marked optional, Think harder, Go further, Investigation, non-core online item, term spare-time menu).

**Strength.**
- **strong**: lesson-specific prompt on the slides AND in the workbook/online, plus a tutor prompt.
- **ok**: lesson-specific in both child-facing places, or in one child-facing place plus a tutor prompt.
- **weak**: one place only, optional material only, or only the shared template line (for example the spine look-back page, or a sentence starter).
- **none**: nothing found.
Strength measures how explicitly the habit is prompted today, not how well it works with children.

**Limits.** The first pass is automated phrase detection over about 100 lessons; I then read the output for about ten lessons in full (holiday 1.1, 1.5, 1.6, 1.9, 2.5, 3.2, 4.6, 6.10; term 3 and 12, plus the term look-back, talk and spare-time structures) and tightened the rules until those readings matched. Expect individual cells to be out by one grade. Gaps and the focus assignment are robust to that; the tag suggestions in section 6 are first candidates to confirm when editing. The scratch scripts and raw hit lists were kept outside the repo (in /dev/shm) and are not committed.

## 3. What every lesson already has (shared template)

| Template element | Where | Habit it supports | Reach |
|---|---|---|---|
| Look-back page: "Did I answer ...?", "Does my answer make sense?", "Can I check it another way?", "Tool I used", stuck/pass boxes (spine.json `lookback`) | slide, workbook, guide | Look back (routine), Check (tick box) | 60 of 60 holiday, 40 of 40 term |
| Term look-back box: hardest / helped / next options written per lesson | workbook p5, slide `s-look` | Look back | 40 of 40 term L1 |
| Talk time with sentence starters "I noticed that ...", "I tested it by ...", "I know because ..." | slide | Notice, Try, Explain | 56 of 60 holiday |
| Talk and explain slide with a lesson-specific "Why?" question and "I think ... because ..." | slide, guide | Explain | 39 of 40 term L1 |
| Explore and sneak-peek: guess first, "Guessing is welcome" | slide, guide | Try, Wonder (prediction) | all lessons |
| Investigation page ("Is it always true?" in many) | workbook, online | Check, Notice, Explain | all holiday lessons (optional page) |
| Tool of the day / Toolbox Card | slide, workbook, guide | tool names, not the habits | all lessons |
| Optional spare-time menu: Teach it back, Make a puzzle for your grown-up, Is it always true? | slide `s-menu`, guide | Explain, Wonder, Check | 38 / 40 / 33 of 40 term L1; shown only if the class is ahead |
| Slogan "Notice it. Test it. Explain why." and, in term, the four inquirer rules | title slide, mascot, guide | Notice, Try, Explain | all |

## 4. Coverage tables

Cell = strength, then where (S slide, W workbook, O online, G guide), then `+opt:` places that are optional-only. Titles are from `levels/spine.json` (holiday) and the lesson JSON (term).

### 4.1 Holiday Level 1 (P1, ages 6-8)

| Lesson | Notice | Wonder | Try | Check | Explain | Look back |
|---|---|---|---|---|---|---|
| 1.1 Count with the Frog | strong SOG +opt:W | weak SG +opt:WO | ok SG | ok SWG | ok SG +opt:WO | weak W |
| 1.2 Number Bond Inquiry | ok SG | weak SG +opt:WO | weak SG +opt:WO | weak SWG +opt:O | strong SOG +opt:W | weak W |
| 1.3 Let's Plan the Fruit Party | ok SG +opt:O | weak SOG +opt:W | weak S +opt:WO | weak SW | strong SOG +opt:W | weak W |
| 1.4 Pattern Inquiry | weak SOG +opt:W | ok SG +opt:WO | ok SG | weak SW +opt:O | strong SOG +opt:W | weak W |
| 1.5 Mystery Number | weak S | weak SG | ok SG +opt:WO | strong SWOG | ok SG +opt:WO | weak W |
| 1.6 Coin Combos | weak S | weak SG +opt:WO | ok SG +opt:W | strong SWOG | strong SOG +opt:W | weak W |
| 1.7 Shape Safari | strong SOG +opt:W | weak SG +opt:G | weak S +opt:WO | weak SWG | ok SG +opt:WO | weak W |
| 1.8 Logic Lab | weak S +opt:WO | weak SG +opt:WO | weak S +opt:O | ok SWG | strong SOG +opt:W | weak W |
| 1.9 Measure It! | weak S +opt:O | weak SG +opt:WO | strong SOG +opt:W | ok SWG +opt:O | strong SOG +opt:W | weak W |
| 1.10 Puzzle Day | ok SG +opt:WO | ok SOG +opt:W | strong SOG +opt:W | ok SWOG | strong SOG +opt:W | ok SWG |

### 4.2 Holiday Level 2 (P2, ages 7-9)

| Lesson | Notice | Wonder | Try | Check | Explain | Look back |
|---|---|---|---|---|---|---|
| 2.1 Digit Detectives | weak S +opt:WO | weak G +opt:O | ok SWG | weak SW | strong SWOG | weak W |
| 2.2 Missing Digit Mysteries | strong SWG +opt:O | weak G +opt:O | strong SWOG | strong SWOG | strong SWOG | weak W |
| 2.3 Legs, Wheels and Arrays | ok SWG +opt:O | weak SG +opt:O | strong SWG +opt:O | strong SWG | strong SWOG | weak WG |
| 2.4 Pattern Machines | ok SWO | weak SG +opt:WO | weak SG +opt:O | weak SWG | strong SWOG | weak W |
| 2.5 Mystery Number Machines | weak SW +opt:O | weak S +opt:O | strong SWG +opt:O | strong SWOG | strong SWG +opt:O | weak W |
| 2.6 Market Day | weak S +opt:WO | weak SG +opt:O | weak SG | weak SW | strong SWOG | weak W |
| 2.7 Fair Shares | weak SWOG | weak G +opt:O | weak SG | ok SWG | strong SWOG | weak W |
| 2.8 Shape Builders | ok SG | weak G +opt:O | weak S +opt:WO | ok SWG | ok SWOG | weak W |
| 2.9 Measure Masters | weak SG | weak +opt:O | ok SG | ok SWG +opt:O | strong SWOG | weak W |
| 2.10 Puzzle Day | ok SW +opt:O | weak S +opt:O | ok SWG +opt:O | ok SWOG | ok SG +opt:WO | ok SWG |

### 4.3 Holiday Level 3 (P3, ages 8-10)

| Lesson | Notice | Wonder | Try | Check | Explain | Look back |
|---|---|---|---|---|---|---|
| 3.1 Number Sleuths | weak SWOG | weak G +opt:WO | ok SG | ok SWG +opt:O | strong SWOG | weak W |
| 3.2 Cryptarithm Crackers | ok SWOG | weak G +opt:WO | strong SWOG | ok SWOG | strong SWOG | weak W |
| 3.3 Times Table Treasure | ok SOG +opt:W | weak S +opt:WO | strong SWOG | ok SWG +opt:O | strong SWOG | weak W |
| 3.4 Model Makers | strong SWOG | none | weak SG | weak SWG | strong SWOG | weak W |
| 3.5 Remainder Riddles | ok SG +opt:O | weak G +opt:WO | strong SWOG | weak SWG +opt:O | ok SG +opt:WO | weak W |
| 3.6 Fraction Walls | ok SWOG | weak +opt:SWO | ok SG +opt:WO | ok SWG +opt:O | ok SG +opt:WO | weak W |
| 3.7 Area Architects | weak SO +opt:W | weak S +opt:WO | weak SG | weak WOG | strong SWOG | weak W |
| 3.8 Angle and Line Detectives | strong SWOG | weak G +opt:WO | strong SWG | strong SWOG | strong SWOG | weak W |
| 3.9 Measure and Money Masters | weak SOG +opt:W | weak G +opt:WO | ok SG | weak SWG +opt:O | strong SWOG | weak W |
| 3.10 Puzzle Day | ok SG +opt:WOG | weak G +opt:WO | weak SG +opt:W | weak SW | strong SWG +opt:O | weak SWG |

### 4.4 Holiday Level 4 (P4, ages 9-11)

| Lesson | Notice | Wonder | Try | Check | Explain | Look back |
|---|---|---|---|---|---|---|
| 4.1 Factor Hunters | weak SWO | weak SG +opt:WO | strong SWOG | ok SWOG | strong SWOG | weak W +opt:S |
| 4.2 Big Number Puzzles | weak SWO | weak +opt:WO | strong SWOG | ok SWO | strong SWOG | weak W |
| 4.3 Operation Detectives | ok SWO | weak SG +opt:WO | strong SWOG | strong SWOG | ok SG +opt:WO | weak W +opt:O |
| 4.4 Fraction Frontier | weak SWO | weak S +opt:WO | weak SG +opt:WO | weak SW | strong SWOG | weak SWG |
| 4.5 Decimal Detectives | weak SWOG +opt:G | weak SG +opt:WO | weak SG | ok SWG | strong SWOG | weak W |
| 4.6 Angle Turns | weak SO +opt:W | weak SG +opt:WO | ok SG | ok SWG | weak S +opt:WO | weak WG +opt:O |
| 4.7 Area Architects II | ok SO | weak SG +opt:WO | ok SG | ok SWG +opt:O | strong SWOG | weak W |
| 4.8 Symmetry and Nets | weak S +opt:O | weak SG +opt:WO | ok SG +opt:WO | weak SWG +opt:O | strong SWOG | weak W |
| 4.9 Data Detectives | weak S +opt:W | weak G +opt:W | ok SG | ok SWG | strong SWOG | weak W |
| 4.10 Puzzle Day | weak +opt:WO | weak SG +opt:WO | strong SWG +opt:O | strong SWG +opt:O | ok SG +opt:WO | ok SWG |

### 4.5 Holiday Level 5 (P5, ages 10-12)

| Lesson | Notice | Wonder | Try | Check | Explain | Look back |
|---|---|---|---|---|---|---|
| 5.1 Million Puzzles | weak SG +opt:WO | weak +opt:SWO | strong SWOG | strong SWOG | ok SG +opt:WO | weak W |
| 5.2 Fraction Feats | ok SWOG | weak WOG | strong SWOG | weak WG +opt:O | strong SWOG | weak W |
| 5.3 Before and After | strong SWOG | weak G +opt:WO | strong SWOG | weak SWG | strong SWOG | weak WG |
| 5.4 Triangle Areas | weak O +opt:SW | weak G +opt:WO | ok SG +opt:WO | ok SWG +opt:O | strong SWOG | weak W |
| 5.5 Volume Vault | weak SO | weak G +opt:SWO | ok SG | strong SWOG | strong SWOG | weak W |
| 5.6 Rate Racers | weak SG +opt:WO | weak SG +opt:WO | ok SG | ok SWG +opt:O | ok SG +opt:WO | weak W |
| 5.7 Percentage Puzzles | weak SO | weak SG +opt:WO | ok SG +opt:WO | weak SW +opt:O | strong SWOG | weak W |
| 5.8 Angle Chasers | ok SOG +opt:W | weak SG +opt:WO | ok SG +opt:O | weak SWG | strong SWOG | weak WG |
| 5.9 Pattern Generalisers | strong SWOG | weak G +opt:SWO | ok SG | strong SWOG | strong SWOG | weak W |
| 5.10 Challenge Day | weak SO +opt:W | weak SG +opt:WO | strong SWOG | strong SWOG | strong SWOG | weak WG |

### 4.6 Holiday Level 6 (P6, ages 11-13)

| Lesson | Notice | Wonder | Try | Check | Explain | Look back |
|---|---|---|---|---|---|---|
| 6.1 Code the Pattern | ok SG | ok SWO | ok SG | strong SWOG | strong SWOG | weak W |
| 6.2 Prime Hunters | weak SWO | weak SWOG | strong SWOG | ok SWO | strong SWOG | weak W |
| 6.3 Below Zero | weak SW +opt:O | weak SG +opt:WO | strong SWG +opt:O | ok SWG +opt:O | ok SG | weak W |
| 6.4 Algebra Machines | weak SO +opt:W | weak SWOG | ok SWO | strong SWOG | strong SWOG | weak W |
| 6.5 Every Possible Way | weak S +opt:O | ok SWG +opt:O | strong SOG | ok SWO | strong SWG +opt:O | weak W |
| 6.6 Fair or Unfair? | weak SO | weak SWOG | ok SG | ok SWOG | ok SWO | weak W |
| 6.7 Turtle Geometry | weak SWO | ok SWOG | ok SWO | ok SWOG | strong SWOG | weak W |
| 6.8 Secret Codes | ok SWO | weak SG +opt:WO | strong SWG +opt:O | strong SWOG | strong SWOG | weak SW |
| 6.9 Data Detectives | strong SOG | ok SWOG | ok SG +opt:O | strong SWOG | strong SWOG | weak W |
| 6.10 Showcase Challenge | weak SO | ok SWOG | strong SWG | ok SWO | strong SWOG | ok SWG |

### 4.7 Term 1, Level 1 (term/l1, lessons 1-10)

| Lesson | Notice | Wonder | Try | Check | Explain | Look back |
|---|---|---|---|---|---|---|
| T1 L1 Bundles and Singles | ok SG +opt:WO | ok SG | ok SG +opt:W | strong SOG +opt:W | strong SWG | ok SW |
| T1 L2 Number Words and the Number Line | ok OG +opt:W | weak SG +opt:WO | ok SG | weak SG +opt:O | strong SWG | ok SW |
| T1 L3 Digit Cards | weak SOG +opt:W | ok SG +opt:O | strong SWG | ok SG +opt:O | strong SWG +opt:O | ok SW |
| T1 L4 The 100 Square Explorer | ok SG +opt:WO | weak SG | weak G +opt:W | ok SWG +opt:O | strong SWG | ok SW |
| T1 L5 Make-a-Ten Adding | ok SG +opt:W | weak SG | ok SG +opt:WO | ok SG +opt:O | strong SWG | ok SW |
| T1 L6 Tens Jump, Ones Hop | strong SWG | weak S +opt:O | weak G +opt:W | weak SG +opt:WO | strong SWG | ok SW |
| T1 L7 Take Away, Count Up | ok OG +opt:SWG | weak S +opt:O | weak G +opt:W | ok SWOG | strong SWG +opt:O | ok SW |
| T1 L8 Balance and Swap | ok SG +opt:WO | weak S +opt:O | weak G +opt:WO | weak SG +opt:O | strong SWG | strong SWG |
| T1 L9 Draw and Measure | weak G +opt:W | weak SG | strong SWG | weak SWG +opt:O | strong SWG | ok SW |
| T1 L10 Story Steps: Read It Twice | ok SG +opt:W | weak SW +opt:O | ok SG +opt:W | weak SG +opt:O | ok SG | ok SWG |

### 4.8 Term 2, Level 1 (term/l1, lessons 11-20)

| Lesson | Notice | Wonder | Try | Check | Explain | Look back |
|---|---|---|---|---|---|---|
| T2 L11 Who Is Where? | weak WG | weak SW +opt:O | ok SG | weak SWG +opt:O | ok WOG | ok SW |
| T2 L12 Bar Strips: More and Fewer | weak SG +opt:W | weak SW +opt:O | ok SG +opt:W | weak SWG +opt:O | strong SWG | ok SW |
| T2 L13 Picture Equations | weak WG | weak S | weak G +opt:W | strong SWG | weak SG +opt:W | ok SW |
| T2 L14 Odd + Odd: Always, Sometimes, Never | ok SG +opt:W | weak S | strong SOG +opt:W | ok SG | ok SG +opt:W | ok SW |
| T2 L15 Equal Groups | ok SWOG | weak S | strong SWG | weak SWG +opt:O | weak SW | ok SW |
| T2 L16 Skip-Count Tables | ok SG +opt:W | weak S | strong SWG | weak SG +opt:WO | weak SWG +opt:O | ok SW |
| T2 L17 Sharing and Grouping | weak OG +opt:W | weak S | ok SG +opt:WO | strong SWOG | strong SWOG | ok SW |
| T2 L18 Times Stories | weak G +opt:W | weak SG +opt:O | ok WG | weak SG +opt:O | weak SWG | ok SW |
| T2 L19 Find One First | weak WG | weak S | weak G | ok SG | weak SG +opt:WO | ok SWG |
| T2 L20 Choose Your Tool | weak WG | weak SW | strong SWG | strong SWOG | strong SWOG | ok SWOG |

### 4.9 Term 3, Level 1 (term/l1, lessons 21-30)

| Lesson | Notice | Wonder | Try | Check | Explain | Look back |
|---|---|---|---|---|---|---|
| T3 L21 What Time Is It? | weak WG | weak S | ok SG | ok SG | ok SOG +opt:W | ok SW |
| T3 L22 Five Minutes at a Time | weak G | weak S | weak G | ok SG | ok SG +opt:W | ok SW |
| T3 L23 Time Passes | ok SG +opt:O | weak S | weak G +opt:S | ok SWG +opt:O | strong SWG +opt:O | ok SW |
| T3 L24 Dollars and Change | weak G +opt:S | weak S | weak G +opt:SWO | strong SWG +opt:O | strong SWG | ok SW |
| T3 L25 Price Tags: Compare and Choose | ok SOG +opt:W | weak S | weak G +opt:SWO | weak SG +opt:O | strong SWG | ok SW |
| T3 L26 The School Shop | weak WOG | weak S +opt:O | weak G +opt:SWO | strong SWG +opt:O | strong SWG | ok SW |
| T3 L27 Calendar Detective | weak G | weak S | weak G +opt:S | weak SG +opt:O | strong SWG | strong SWG |
| T3 L28 Make a Table | weak G +opt:W | weak S | ok SG | weak SWG | strong SWG | strong SWG |
| T3 L29 Spot the Mistake | weak G +opt:O | weak S | weak G +opt:SW | strong SWOG | ok SWG | ok SW |
| T3 L30 Tool Detectives | weak SG | weak S | strong SWG +opt:O | ok SWG +opt:O | strong SWG | ok SWOG |

### 4.10 Term 4, Level 1 (term/l1, lessons 31-40)

| Lesson | Notice | Wonder | Try | Check | Explain | Look back |
|---|---|---|---|---|---|---|
| T4 L31 Half and Quarter | weak G +opt:W | weak S | strong SWG +opt:O | weak SWG +opt:O | strong SWG | strong SWG |
| T4 L32 Build the Figure | ok SWG | weak S | strong SWOG | ok SWG +opt:O | weak SG +opt:W | ok SW |
| T4 L33 Copy on the Grid | weak G | weak S | weak G | weak SG +opt:O | strong SWG +opt:O | ok SW |
| T4 L34 Cubes and Views | weak OG | weak SG | weak G +opt:W | weak SG | strong SWG +opt:O | ok SW |
| T4 L35 Spot It | strong SWOG | weak S | weak G | ok SWOG | strong SWG | ok SW |
| T4 L36 Count Everything | weak +opt:W | weak S | ok SG | weak SG +opt:O | ok SG +opt:W | ok SW |
| T4 L37 Make Your Own Graph | weak G | weak SG | weak G | ok SWG | strong SWG +opt:O | ok SW |
| T4 L38 Graph Detectives | none | weak S | ok SG +opt:W | weak SWG | strong SWOG | ok SWG |
| T4 L39 The Problem-Solving Toolbox | weak S | weak S | weak +opt:SW | strong SWOG | strong SWG | ok SWOG |
| T4 L40 Inquirers' Showcase | weak G | ok SG +opt:O | strong SWOG | strong SWOG | strong SWG +opt:O | strong SWG |

### 4.11 Levels 2-6 term material

Not written yet. `term/` contains only `l1`; Levels 2-6 have year plans only (`docs/terms/level_2_year_plan.md` to `level_6_year_plan.md`, `docs/terms/levels_2_6_term_build_plan.md`). Nothing to audit. Apply section 5 when those lessons are authored: put the habit field in `term/l1/schema/lesson.schema.json` (or its Level 2-6 equivalent) so a lesson cannot validate without a focus habit.

## 5. Gaps

### 5.1 Strength by habit

| Habit | Holiday (60): strong / ok / weak / none | Term L1 (40): strong / ok / weak / none |
|---|---|---|
| Notice | 8 / 18 / 34 / 0 | 2 / 13 / 24 / 1 |
| Wonder | 0 / 7 / 52 / 1 | 0 / 3 / 37 / 0 |
| Try | 22 / 25 / 13 / 0 | 10 / 12 / 18 / 0 |
| Check | 16 / 26 / 18 / 0 | 9 / 13 / 18 / 0 |
| Explain | 46 / 13 / 1 / 0 | 27 / 7 / 6 / 0 |
| Look back | 0 / 4 / 56 / 0 | 5 / 35 / 0 / 0 |

What "weak" means in practice:

| Habit | Holiday weak = optional-only / one channel / template only | Term L1 weak = optional-only / one channel / template only |
|---|---|---|
| Notice | 19 / 12 / 3 | 1 / 20 / 3 |
| Wonder | 20 / 31 / 1 | 3 / 11 / 23 |
| Try | 2 / 11 / 0 | 1 / 17 / 0 |
| Check | 6 / 11 / 1 | 0 / 18 / 0 |
| Explain | 0 / 1 / 0 | 1 / 5 / 0 |
| Look back | 3 / 4 / 49 | 0 / 0 / 0 |

### 5.2 Habits rarely or never explicit

- **Look back (holiday):** a routine answer-check, not reflection. Nothing asks what was learned or what to change. Fix with one tagged line (section 6).
- **Wonder (both):** present mainly as optional items. A child who does only Start here never makes a question or a "what if" in most lessons.
- **Notice (both):** relies on the optional Investigation or on one tutor question. Few core workbook lines say "What do you notice?".
- **Check (term L1 and holiday):** strong when a lesson has an "always true?" task; otherwise only "check by adding". No lesson asks the child to test a second case in core work except where it is the topic.
- **Terms emphasise one habit in their names** (Notice it, Test it, Explain why, Choose and create), which hides the rest.

### 5.3 Lessons with the least explicit habit practice

No lesson has *no* trace of any habit; the lowest are those with four or more habits graded weak or none:

Holiday: 1.2 Number Bond Inquiry (Wonder, Try, Check, Look back); 1.3 Let's Plan the Fruit Party (Wonder, Try, Check, Look back); 1.7 Shape Safari (Wonder, Try, Check, Look back); 1.8 Logic Lab (Notice, Wonder, Try, Look back); 2.1 Digit Detectives (Notice, Wonder, Check, Look back); 2.4 Pattern Machines (Wonder, Try, Check, Look back); 2.6 Market Day (Notice, Wonder, Try, Check, Look back); 2.7 Fair Shares (Notice, Wonder, Try, Look back); 3.4 Model Makers (Wonder, Try, Check, Look back); 3.7 Area Architects (Notice, Wonder, Try, Check, Look back); 3.9 Measure and Money Masters (Notice, Wonder, Check, Look back); 3.10 Puzzle Day (Wonder, Try, Check, Look back); 4.4 Fraction Frontier (Notice, Wonder, Try, Check, Look back); 4.5 Decimal Detectives (Notice, Wonder, Try, Look back); 4.6 Angle Turns (Notice, Wonder, Explain, Look back); 4.8 Symmetry and Nets (Notice, Wonder, Check, Look back); 5.7 Percentage Puzzles (Notice, Wonder, Check, Look back).

Term L1: L13 Picture Equations (Notice, Wonder, Try, Explain); L18 Times Stories (Notice, Wonder, Check, Explain); L19 Find One First (Notice, Wonder, Try, Explain); L27 Calendar Detective (Notice, Wonder, Try, Check); L33 Copy on the Grid (Notice, Wonder, Try, Check); L34 Cubes and Views (Notice, Wonder, Try, Check).

Lessons that already practise five or six habits at ok or better (candidates to model the badge and tagged-question format on): holiday 1.10, 2.10, 6.1, 6.9, 6.10; term L1 L1, L3, L5, L14, L40.

## 6. Proposed focus-habit assignment and smallest additions

**Rules used.** One focus habit per lesson (supporting habit optional, at most one). Every holiday level has all six habits within its ten lessons; each habit is the focus of exactly 10 of the 60 holiday lessons; each term of L1 has all six within its ten lessons and each habit is focus of 6 or 7 of the 40 term lessons. The last lesson of each holiday level and of each term (the choose-the-tool / Quest lesson) is Look back. Look back is never the first lesson and never directly beside another Look back. No habit is the focus of two consecutive lessons. Within those rules the assignment minimises the work: it picks the habit each lesson already practises best (cost 0 for strong, 1 ok, 2 weak, 3 none), so the weak habits land where the content already gives them a foothold.

**Standard package for every lesson** (not repeated in the rows): (a) habit badge, same icon every time, on the opening slide and on the look-back slide; (b) one front-page guide line: "Focus habit: X. Teaching move: ..." with the scripted prompt and the rule "do not give the answer first"; (c) a report field for the habit practised and one observed example. The table rows list only what is lesson-specific: the existing workbook line, online item and tutor prompt to tag, or the single line to add.

**Wording to add when a line is missing** (band A wording; shorten for Levels 1-2, add "how do you know" for Levels 5-6):

| Habit | Child line (workbook or online self-check) | Tutor prompt (guide) |
|---|---|---|
| Notice | Notice it: What do you see? What stays the same? What changes? | "What do you see? What stays the same, what changes?" |
| Wonder | Wonder: What if...? Write one question of your own. | "What could we ask? What if we changed one thing?" |
| Try | Try it: test one example (or a smaller case) before you decide. | "Pick one example and test it. What happens?" |
| Check | Check it: test a second case. Does it always work? | "Will it work with a different number? Test it." |
| Explain | Explain: write one sentence. I know because ... | "How do you know? Tell it as if you were teaching a friend." |
| Look back | Look back: What did I learn? What would I change next time? | "What did you learn? What would you do differently next time?" |

Tag candidates below are the best existing match found automatically; confirm them against the page when editing. "core" means the line sits on Start here (or equivalent), not on an optional page.

### 6.1 Balance check

| Level | Notice | Wonder | Try | Check | Explain | Look back |
|---|---|---|---|---|---|---|
| Holiday 1 | 2 | 2 | 1 | 1 | 2 | 2 |
| Holiday 2 | 2 | 2 | 1 | 2 | 1 | 2 |
| Holiday 3 | 2 | 2 | 2 | 1 | 2 | 1 |
| Holiday 4 | 1 | 1 | 2 | 2 | 2 | 2 |
| Holiday 5 | 2 | 1 | 2 | 2 | 2 | 1 |
| Holiday 6 | 1 | 2 | 2 | 2 | 1 | 2 |
| **Holiday total** | 10 | 10 | 10 | 10 | 10 | 10 |
| Term 1 (L1) | 2 | 1 | 1 | 2 | 2 | 2 |
| Term 2 (L1) | 1 | 2 | 2 | 2 | 2 | 1 |
| Term 3 (L1) | 2 | 2 | 1 | 2 | 1 | 2 |
| Term 4 (L1) | 2 | 1 | 2 | 1 | 2 | 2 |
| **Term L1 total** | 7 | 6 | 6 | 7 | 7 | 7 |

### 6.2 Holiday Level 1 (P1, ages 6-8)

| Lesson | Focus | Now (focus habit) | Smallest addition beyond the standard package |
|---|---|---|---|
| 1.1 Count with the Frog | Notice | strong SOG +opt:W | W: move/tag optional Q4 "What do you notice about these numbers?" and add one core line ("Notice it: What do you see? What stays the same? What changes?"); O: tag item 4(b); G: script "Our job is to notice the rule, test it with a counter, check our answ…" |
| 1.2 Number Bond Inquiry | Explain | strong SOG +opt:W | W: move/tag optional Q6 "Why do you think it works?" and add one core line ("Explain: write one sentence. I know because ..."); O: tag item 4(e) and add a self-check "explain" follow-up; G: script "How do you know?" |
| 1.3 Let's Plan the Fruit Party | Look back | weak W | W: add one core line "Look back: What did I learn? What would I change next time?"; O: add the habit prompt to core self-check item 6(b); G: add scripted prompt "What did you learn? What would you do differently next time?" |
| 1.4 Pattern Inquiry | Wonder | ok SG +opt:WO | W: move/tag optional Q8 "Draw your own pattern of 3 shapes that repeats (f…" and add one core line ("Wonder: What if...? Write one question of your own."); O: add the habit prompt to core self-check item 4(d); G: script "What if I had 23 sticks?" |
| 1.5 Mystery Number | Check | strong SWOG | W: move/tag optional Q5 "Investigation: Is it always true?" and add one core line ("Check it: test a second case. Does it always work?"); O: tag item 2(a) and add a self-check "explain" follow-up; G: script "How can you check your answer by going forwards?" |
| 1.6 Coin Combos | Wonder | weak SG +opt:WO | W: move/tag optional Q6 "Investigation: What if we take a coin away?" and add one core line ("Wonder: What if...? Write one question of your own."); O: add the habit prompt to core self-check item 1; G: add scripted prompt "What could we ask? What if we changed one thing?" |
| 1.7 Shape Safari | Notice | strong SOG +opt:W | W: move/tag optional Q3 "What do you notice about the number of sides and…" and add one core line ("Notice it: What do you see? What stays the same? What changes?"); O: tag item 2(a); G: script "What do you notice?" |
| 1.8 Logic Lab | Explain | strong SOG +opt:W | W: move/tag optional Q2 "Why are they in the middle?" and add one core line ("Explain: write one sentence. I know because ..."); O: tag item 2(b); G: script "Why was it good?" |
| 1.9 Measure It! | Try | strong SOG +opt:W | W: move/tag optional Q6 "Guess: if a unit is half as long as a cube, what…" and add one core line ("Try it: test one example (or a smaller case) before you decide."); O: tag item 2; G: script "Let me try three objects." |
| 1.10 Puzzle Day | Look back | ok SWG | W: add one core line "Look back: What did I learn? What would I change next time?"; O: add the habit prompt to core self-check item 9; G: script "Which do you think will be hardest?" |

### 6.3 Holiday Level 2 (P2, ages 7-9)

| Lesson | Focus | Now (focus habit) | Smallest addition beyond the standard package |
|---|---|---|---|
| 2.1 Digit Detectives | Wonder | weak G +opt:O | W: add one core line "Wonder: What if...? Write one question of your own."; O: add the habit prompt to core self-check item 3(b); G: add scripted prompt "What could we ask? What if we changed one thing?" |
| 2.2 Missing Digit Mysteries | Notice | strong SWG +opt:O | W: tag Q6 "What do you notice?"; O: add the habit prompt to core self-check item 1 (check); G: script "What changes?" |
| 2.3 Legs, Wheels and Arrays | Try | strong SWG +opt:O | W: tag Q6 "Try 2 rows, 3 rows, 4 rows and so on."; O: add the habit prompt to core self-check item 2(c); G: script "Write a guess." |
| 2.4 Pattern Machines | Notice | ok SWO | W: tag Q6 "Both say: ______________ What do you notice?"; O: tag item 6(c) notice; G: add scripted prompt "What do you see? What stays the same, what changes?" |
| 2.5 Mystery Number Machines | Check | strong SWOG | W: tag Q5 "Do the two machines always give the same answer?"; O: tag item 5(c) and add a self-check "explain" follow-up; G: script "Now I test it on the other pair: 4 × 2 = 8, 8 + 5 = 13." |
| 2.6 Market Day | Look back | weak W | W: add one core line "Look back: What did I learn? What would I change next time?"; O: add the habit prompt to core self-check item 1(a) notes and coins; G: add scripted prompt "What did you learn? What would you do differently next time?" |
| 2.7 Fair Shares | Explain | strong SWOG | W: tag Q6 "Why not?"; O: tag item 1(a); G: script "How do you know?" |
| 2.8 Shape Builders | Wonder | weak G +opt:O | W: add one core line "Wonder: What if...? Write one question of your own."; O: add the habit prompt to core self-check item 1(c) show how; G: script "What if he had 1 half circle and 2 quarter circles?" |
| 2.9 Measure Masters | Check | ok SWG +opt:O | W: move/tag optional Q7 "Check it by writing every pour in a table." and add one core line ("Check it: test a second case. Does it always work?"); O: add the habit prompt to core self-check item 1(c) show how; G: script "I write every pour in a table so I can check it." |
| 2.10 Puzzle Day | Look back | ok SWG | W: add one core line "Look back: What did I learn? What would I change next time?"; O: add the habit prompt to core self-check item 1(b) draw; G: script "Which one will be hardest?" |

### 6.4 Holiday Level 3 (P3, ages 8-10)

| Lesson | Focus | Now (focus habit) | Smallest addition beyond the standard package |
|---|---|---|---|
| 3.1 Number Sleuths | Explain | strong SWOG | W: tag Q1 "Why is (d) the closest?"; O: tag item 1(e) and add a self-check "explain" follow-up; G: script "Why there?" |
| 3.2 Cryptarithm Crackers | Try | strong SWOG | W: tag Q2 "Guess, check, then improve."; O: tag item 2(c) and add a self-check "explain" follow-up; G: script "Try 1 and 2 in the hundreds." |
| 3.3 Times Table Treasure | Wonder | weak S +opt:WO | W: move/tag optional Q5 "Make up your own riddle: "I am a 2-digit number i…" and add one core line ("Wonder: What if...? Write one question of your own."); O: add the habit prompt to core self-check item 1(b) why; G: add scripted prompt "What could we ask? What if we changed one thing?" |
| 3.4 Model Makers | Notice | strong SWOG | W: tag Q6 "What do you notice?"; O: tag item 6(c) and add a self-check "explain" follow-up; G: script "What stays the same in this story: the total or the difference?" |
| 3.5 Remainder Riddles | Try | strong SWOG | W: tag Q4 "Make a list, then test each number."; O: tag item 4(a) list and add a self-check "explain" follow-up; G: script "Write a guess." |
| 3.6 Fraction Walls | Check | ok SWG +opt:O | W: move/tag optional Q5 "Check it, then swap with a partner." and add one core line ("Check it: test a second case. Does it always work?"); O: add one core self-check item; G: script "Inquirers check that a comparison is fair." |
| 3.7 Area Architects | Wonder | weak S +opt:WO | W: move/tag optional Q7 "Investigation: What if we change it?" and add one core line ("Wonder: What if...? Write one question of your own."); O: add the habit prompt to core self-check item 6(c) explain; G: add scripted prompt "What could we ask? What if we changed one thing?" |
| 3.8 Angle and Line Detectives | Notice | strong SWOG | W: tag Q4 "Parallel lines never meet and stay the same distance apart,…"; O: tag item 4 (letter E) and add a self-check "explain" follow-up; G: script "The two upright lines of H stay the same distance apart." |
| 3.9 Measure and Money Masters | Explain | strong SWOG | W: tag Q2 "Ben says, “1 kg 30 g is the same as 130 g.” Explain his mis…"; O: tag item 2(b) and add a self-check "explain" follow-up; G: script "how do you know?" |
| 3.10 Puzzle Day | Look back | weak SWG | W: add one core line "Look back: What did I learn? What would I change next time?"; O: add the habit prompt to core self-check item 1(c); G: add scripted prompt "What did you learn? What would you do differently next time?" |

### 6.5 Holiday Level 4 (P4, ages 9-11)

| Lesson | Focus | Now (focus habit) | Smallest addition beyond the standard package |
|---|---|---|---|
| 4.1 Factor Hunters | Wonder | weak SG +opt:WO | W: move/tag optional Q6 "What if we change ...?" and add one core line ("Wonder: What if...? Write one question of your own."); O: add the habit prompt to core self-check item 1(c) why; G: add scripted prompt "What could we ask? What if we changed one thing?" |
| 4.2 Big Number Puzzles | Try | strong SWOG | W: tag Q1 "Try next, if you have time: 9049 → ________ ________ ______…"; O: tag item 1 (try next) 9049 and add a self-check "explain" follow-up; G: script "Which clue gives you the fewest numbers to try?" |
| 4.3 Operation Detectives | Check | strong SWOG | W: tag Q4 "Check it going forwards."; O: tag item 4(b); G: script "Let me check by doing it in the right order: 8 × 5 − 3 = 37." |
| 4.4 Fraction Frontier | Explain | strong SWOG | W: tag Q8 "Why?"; O: tag item 4(c) how you know; G: script "How do you know?" |
| 4.5 Decimal Detectives | Look back | weak W | W: add one core line "Look back: What did I learn? What would I change next time?"; O: add the habit prompt to core self-check item 2(b); G: add scripted prompt "What did you learn? What would you do differently next time?" |
| 4.6 Angle Turns | Try | ok SG | W: add one core line "Try it: test one example (or a smaller case) before you decide."; O: add the habit prompt to core self-check item 1; G: script "Write down your guess before you try." |
| 4.7 Area Architects II | Notice | ok SO | W: add one core line "Notice it: What do you see? What stays the same? What changes?"; O: tag item 5(c); G: add scripted prompt "What do you see? What stays the same, what changes?" |
| 4.8 Symmetry and Nets | Explain | strong SWOG | W: tag Q3 "In net (b), how did you find the number opposite 1?"; O: tag item 3(c); G: script "Then tell me where the fold line goes: up and down, or across?" |
| 4.9 Data Detectives | Check | ok SWG | W: add one core line "Check it: test a second case. Does it always work?"; O: add the habit prompt to core self-check item 1(d); G: script "How can you check your missing number?" |
| 4.10 Puzzle Day | Look back | ok SWG | W: add one core line "Look back: What did I learn? What would I change next time?"; O: add one core self-check item; G: script "Which one do you think will be hardest?" |

### 6.6 Holiday Level 5 (P5, ages 10-12)

| Lesson | Focus | Now (focus habit) | Smallest addition beyond the standard package |
|---|---|---|---|
| 5.1 Million Puzzles | Check | strong SWOG | W: tag Q3 "Then check every clue."; O: tag item 3(a) and add a self-check "explain" follow-up; G: script "Then I follow the other clues one by one and check every clue at the…" |
| 5.2 Fraction Feats | Try | strong SWOG | W: tag Q4 "The smallest sum: ______________________ Did you test both…"; O: tag item 6(b) and add a self-check "explain" follow-up; G: script "what could you try first?" |
| 5.3 Before and After | Notice | strong SWOG | W: tag the line "First ask: what stays the same?"; O: tag item 4(a) and add a self-check "explain" follow-up; G: script "Predict again: total or difference, which one stays the same?" |
| 5.4 Triangle Areas | Explain | strong SWOG | W: tag Q2 "Explain why the two triangles have the same area."; O: tag item 2(c); G: script "How do you know?" |
| 5.5 Volume Vault | Check | strong SWOG | W: add one core line "Check it: test a second case. Does it always work?"; O: tag item 5 check; G: script "Ali says a 1000 cm³ stone always makes the water rise 1 cm." |
| 5.6 Rate Racers | Try | ok SG | W: add one core line "Try it: test one example (or a smaller case) before you decide."; O: add one core self-check item; G: script "what could you try first?" |
| 5.7 Percentage Puzzles | Wonder | weak SG +opt:WO | W: move/tag optional QB3 "Make up a price that goes up by a percentage and…" and add one core line ("Wonder: What if...? Write one question of your own."); O: add the habit prompt to core self-check item 1(a); G: add scripted prompt "What could we ask? What if we changed one thing?" |
| 5.8 Angle Chasers | Explain | strong SWOG | W: tag Q3 "Write each reason in words."; O: tag item 3(b) and add a self-check "explain" follow-up; G: script "How did you decide?" |
| 5.9 Pattern Generalisers | Notice | strong SWOG | W: tag the line "A growing pattern: find what stays the same and what grows…"; O: tag item 1(d) why; G: script "What do you notice about 1, 4, 9, 16, 25?" |
| 5.10 Challenge Day | Look back | weak WG | W: add one core line "Look back: What did I learn? What would I change next time?"; O: add the habit prompt to core self-check item 3 (check); G: script "Which one do you think will be the hardest?" |

### 6.7 Holiday Level 6 (P6, ages 11-13)

| Lesson | Focus | Now (focus habit) | Smallest addition beyond the standard package |
|---|---|---|---|
| 6.1 Code the Pattern | Wonder | ok SWO | W: tag Q6 "What if we change the shape?"; O: add the habit prompt to core self-check item 1(a) why; G: add scripted prompt "What could we ask? What if we changed one thing?" |
| 6.2 Prime Hunters | Explain | strong SWOG | W: tag Q6 "Why?"; O: tag item 3(b) and add a self-check "explain" follow-up; G: script "How do you know you have found every factor?" |
| 6.3 Below Zero | Try | strong SWG +opt:O | W: tag Q7 "Then try again with a − b = 3."; O: add one core self-check item; G: script "Write your prediction before you test it." |
| 6.4 Algebra Machines | Check | strong SWOG | W: tag Q3 "Then check by going forwards."; O: tag item 2(c) explain; G: script "Did you check your rule on every pair, not just the first?" |
| 6.5 Every Possible Way | Try | strong SOG | W: add one core line "Try it: test one example (or a smaller case) before you decide."; O: tag item 6(b) what; G: script "Before you list them, write your guess: how many different orders?" |
| 6.6 Fair or Unfair? | Look back | weak W | W: add one core line "Look back: What did I learn? What would I change next time?"; O: add the habit prompt to core self-check item 1(d) explain; G: add scripted prompt "What did you learn? What would you do differently next time?" |
| 6.7 Turtle Geometry | Wonder | ok SWOG | W: tag Q10 "What if the turn changes?"; O: add the habit prompt to core self-check item 1(a); G: add scripted prompt "What could we ask? What if we changed one thing?" |
| 6.8 Secret Codes | Check | strong SWOG | W: tag Q5 "Which shift (not 0), used twice, always gives back the orig…"; O: tag item 5(d) and add a self-check "explain" follow-up; G: script "How can you check your code?" |
| 6.9 Data Detectives | Notice | strong SOG | W: add one core line "Notice it: What do you see? What stays the same? What changes?"; O: tag item 3(a) predict and add a self-check "explain" follow-up; G: script "Before you calculate: will the mean go up, go down or stay the same?" |
| 6.10 Showcase Challenge | Look back | ok SWG | W: add one core line "Look back: What did I learn? What would I change next time?"; O: add the habit prompt to core self-check item 4(c) why; G: script "Which one do you think will be hardest?" |

### 6.8 Term 1, Level 1

| Lesson | Focus | Now (focus habit) | Smallest addition beyond the standard package |
|---|---|---|---|
| T1 L1 Bundles and Singles | Check | strong SOG +opt:W | W: move/tag optional T3 "Then check the tens digit of each." and add one core line ("Check it: test a second case. Does it always work?"); O: tag item c5 and add a self-check explain follow-up; G: script "I will tell you what it should look like, so you can check your own b…" |
| T1 L2 Number Words and the Number Line | Notice | ok OG +opt:W | W: move/tag optional I1 "A child who tests several numbers by counting hop…" and add one core line ("Notice it: What do you see? What stays the same? What changes?"); O: tag item c4 and add a self-check explain follow-up; G: script "What did you notice?" |
| T1 L3 Digit Cards | Wonder | ok SG +opt:O | W: add one core line "Wonder: What if...? Write one question of your own."; O: add one core self-check item; G: script "If you finish, try the what-if card: what if one card is 0?" |
| T1 L4 The 100 Square Explorer | Look back | ok SW | W: look-back box already asks hardest/helped/next; add one 'what I would change' tick; O: add one core self-check item; G: add scripted prompt "What did you learn? What would you do differently next time?" |
| T1 L5 Make-a-Ten Adding | Explain | strong SWG | W: tag sneak-peek q2 "Then write how you know."; O: add one core self-check item; G: script "Tell me: how many did you move, and how many are left outside?" |
| T1 L6 Tens Jump, Ones Hop | Notice | strong SWG | W: tag home practice 5 "(b) What stays the same?"; O: add one core self-check item; G: script "What stays the same every time?" |
| T1 L7 Take Away, Count Up | Check | ok SWOG | W: add one core line "Check it: test a second case. Does it always work?"; O: add one core self-check item; G: script "Nobody holds paper up to the camera: children keep their own answer a…" |
| T1 L8 Balance and Swap | Explain | strong SWG | W: tag sneak-peek q2 "Write how you know."; O: add one core self-check item; G: script "How do you know the plates match?" |
| T1 L9 Draw and Measure | Try | strong SWG | W: tag S3 "Write your guess first."; O: add one core self-check item; G: script "How close was your guess?" |
| T1 L10 Story Steps: Read It Twice | Look back | ok SWG | W: look-back box already asks hardest/helped/next; add one 'what I would change' tick; O: add one core self-check item; G: add scripted prompt "What did you learn? What would you do differently next time?" |

### 6.9 Term 2, Level 1

| Lesson | Focus | Now (focus habit) | Smallest addition beyond the standard package |
|---|---|---|---|
| T2 L11 Who Is Where? | Wonder | weak SW +opt:O | W: look-back box already asks hardest/helped/next; add one 'what I would change' tick; O: add one core self-check item; G: add scripted prompt "What could we ask? What if we changed one thing?" |
| T2 L12 Bar Strips: More and Fewer | Explain | strong SWG | W: tag home practice 4 "Write: I know because ..."; O: add one core self-check item; G: script "Why, or why not?" |
| T2 L13 Picture Equations | Check | strong SWG | W: tag page hint "Check your answer in the line."; O: add one core self-check item; G: script "Think harder: use two lines about the same shapes (take one line from…" |
| T2 L14 Odd + Odd: Always, Sometimes, Never | Try | strong SOG +opt:W | W: move/tag optional T1 "Test it." and add one core line ("Try it: test one example (or a smaller case) before you decide."); O: tag item c3 and add a self-check explain follow-up; G: script "We test a claim: is a sum always odd, sometimes odd or never odd?" |
| T2 L15 Equal Groups | Notice | ok SWOG | W: move/tag optional I1 "A child who builds several arrays, writes a × sen…" and add one core line ("Notice it: What do you see? What stays the same? What changes?"); O: add one core self-check item; G: script "What do you notice about the total?" |
| T2 L16 Skip-Count Tables | Try | strong SWG | W: tag warm-up "Term 2 Lessons 5 to 8 build on one another (groups, tables,…"; O: add one core self-check item; G: script "How could we test it?" |
| T2 L17 Sharing and Grouping | Explain | strong SWOG | W: tag S7 "Ask: does the story tell me how many friends, or how many a…"; O: tag item c4 and add a self-check explain follow-up; G: script "Q7: does the story say how many friends, or how many in each box?" |
| T2 L18 Times Stories | Wonder | weak SG +opt:O | W: add one core line "Wonder: What if...? Write one question of your own."; O: add one core self-check item; G: script "What if Ali gave away 6 pens instead of finding 6 more?" |
| T2 L19 Find One First | Check | ok SG | W: add one core line "Check it: test a second case. Does it always work?"; O: add one core self-check item; G: script "Check by putting the cost of one back: 5 groups of $3 is $15." |
| T2 L20 Choose Your Tool | Look back | ok SWOG | W: look-back box already asks hardest/helped/next; add one 'what I would change' tick; O: add one core self-check item; G: add scripted prompt "What did you learn? What would you do differently next time?" |

### 6.10 Term 3, Level 1

| Lesson | Focus | Now (focus habit) | Smallest addition beyond the standard package |
|---|---|---|---|
| T3 L21 What Time Is It? | Try | ok SG | W: add one core line "Try it: test one example (or a smaller case) before you decide."; O: add one core self-check item; G: script "Go further (Hands Detective): count the long hand on by some numbers,…" |
| T3 L22 Five Minutes at a Time | Wonder | weak S | W: add one core line "Wonder: What if...? Write one question of your own."; O: add one core self-check item; G: add scripted prompt "What could we ask? What if we changed one thing?" |
| T3 L23 Time Passes | Notice | ok SG +opt:O | W: add one core line "Notice it: What do you see? What stays the same? What changes?"; O: add one core self-check item; G: script "What did you notice?" |
| T3 L24 Dollars and Change | Check | strong SWG +opt:O | W: tag page hint "Use your play money to check your answer."; O: add one core self-check item; G: script "How could we check with our coins?" |
| T3 L25 Price Tags: Compare and Choose | Notice | ok SOG +opt:W | W: move/tag optional I1 "A child who picks a tag and counts up 4 to see if…" and add one core line ("Notice it: What do you see? What stays the same? What changes?"); O: add one core self-check item; G: script "What did you notice?" |
| T3 L26 The School Shop | Wonder | weak S +opt:O | W: add one core line "Wonder: What if...? Write one question of your own."; O: add one core self-check item; G: add scripted prompt "What could we ask? What if we changed one thing?" |
| T3 L27 Calendar Detective | Look back | strong SWG | W: tag E3 "The next time he swims is the ____ th."; O: add one core self-check item; G: script "The next time he swims is the blank th." |
| T3 L28 Make a Table | Explain | strong SWG | W: tag sneak-peek q2 "I know because ___."; O: add one core self-check item; G: script "How do you know?" |
| T3 L29 Spot the Mistake | Check | strong SWOG | W: tag S3 "Check each step on its own."; O: add one core self-check item; G: script "How did you check it?" |
| T3 L30 Tool Detectives | Look back | ok SWOG | W: look-back box already asks hardest/helped/next; add one 'what I would change' tick; O: add one core self-check item; G: add scripted prompt "What did you learn? What would you do differently next time?" |

### 6.11 Term 4, Level 1

| Lesson | Focus | Now (focus habit) | Smallest addition beyond the standard package |
|---|---|---|---|
| T4 L31 Half and Quarter | Try | strong SWG +opt:O | W: tag warm-up "Try not to miss this lesson: Build the Figure uses a square…"; O: add one core self-check item; G: script "Test it with your circle." |
| T4 L32 Build the Figure | Notice | ok SWG | W: add one core line "Notice it: What do you see? What stays the same? What changes?"; O: add one core self-check item; G: script "What 2 shapes do you see?" |
| T4 L33 Copy on the Grid | Look back | ok SW | W: look-back box already asks hardest/helped/next; add one 'what I would change' tick; O: add one core self-check item; G: add scripted prompt "What did you learn? What would you do differently next time?" |
| T4 L34 Cubes and Views | Explain | strong SWG +opt:O | W: tag S4 "Write how many cubes are in each stack on the top view."; O: add one core self-check item; G: script "Count the cubes in a picture and say how many cannot be seen when the…" |
| T4 L35 Spot It | Notice | strong SWOG | W: tag S1 "What is different in each tile?"; O: tag item c2 and add a self-check explain follow-up; G: script "What is different?" |
| T4 L36 Count Everything | Try | ok SG | W: add one core line "Try it: test one example (or a smaller case) before you decide."; O: add one core self-check item; G: script "We try every arm move with every leg move." |
| T4 L37 Make Your Own Graph | Wonder | weak SG | W: add one core line "Wonder: What if...? Write one question of your own."; O: add one core self-check item; G: script "Today we ask a question, sort the answers and picture them." |
| T4 L38 Graph Detectives | Explain | strong SWOG | W: tag sneak-peek q2 "I know because ___."; O: add one core self-check item; G: script "How do you know?" |
| T4 L39 The Problem-Solving Toolbox | Check | strong SWOG | W: tag page hint "Check your answer."; O: tag item r1 and add a self-check explain follow-up; G: script "Look at the whole story, and check the answer a second way." |
| T4 L40 Inquirers' Showcase | Look back | strong SWG | W: tag S1 "Look back at your year books."; O: add one core self-check item; G: script "Look back over the year together in a minute (the OUR YEAR card)." |

### 6.12 Levels 2-6 term lessons (to be written)

Use the same pattern: ten lessons per term, each habit at least once, Look back on lesson 10 (Quest), no habit in two consecutive lessons, each habit 6-7 times a year. A ready slot sequence for any term (rotate by two each term so the extra habits differ): `Notice, Explain, Wonder, Check, Try, Notice, Explain, Wonder, Check, Look back` for Term 1; shift each habit one place for Term 2, and so on.

## 7. Website and marketing text that claims inquiry-skill outcomes

`website/dist` was not touched or read. Sources are listed first; each source page is generated into a checked-in HTML copy (`lp_build.py` -> `mi_signup.html`, `level_pages.py` -> `level_pages/ages-*.html`, `hub/qa.py` -> `hub/parent_questions.html`), so edit the source and rebuild. Nothing here has been edited. Wording follows `docs/pedagogy/inquiry_skills_explicit.md` section 3 (process-based: "practise", "every lesson includes"; no "will learn" or "is how thinking grows"). The lawyer sees the final wording before anything is published.

**Structural mismatch first.** The home page presents "Four habits of a young mathematician" (Notice the pattern, Test it with objects, Check your answer, Explain why) and says "every lesson follows the same four steps". The design now has six habits, with Wonder and Look back missing from the four. Level pages and the parent FAQ repeat the four-step line. Replace the four cards by the six habits once the badges exist; until then keep the wording below general.

| # | File and line (source -> generated copy) | Current text | Why it is an outcome or process claim | Suggested process-based wording |
|---|---|---|---|---|
| 1 | `website/lp_build.py:44` -> `mi_signup.html:281` | "Four habits of a young mathematician. Every lesson follows the same four steps, so children learn how to think, not just what to write." | Outcome ("learn how to think") and a four-habit framework that does not match the six. | "Habits of a young mathematician. Every lesson practises six inquiry habits: noticing, wondering, trying, checking, explaining and looking back. Children practise how to think as well as what to write." |
| 2 | `lp_build.py:45-48` -> `mi_signup.html:282-285` | Cards 1 to 4: Notice the pattern / Test it with objects / Check your answer / Explain why. | Lists four habits only; no Wonder, no Look back. | Show six cards: Notice ("What do I see?"), Wonder ("What could I ask?"), Try ("Let me test it"), Check ("Does it always work?"), Explain ("Here is why"), Look back ("What did I learn?"). |
| 3 | `lp_build.py:48` -> `mi_signup.html:285` | "Say or draw why it works. This is where learning sticks." | Outcome claim about retention. | "Say or draw why it works. Children practise explaining in every lesson." |
| 4 | `lp_build.py:52-53` -> `mi_signup.html:289-290` | "Open investigations: Find every way, spot the pattern, make up your own puzzle, and ask 'what if?'." and "Explain and look back: Children say why it works, try a second method, and note what was hard." | Describes activities, but states them for every lesson. Wonder ("make up", "what if") is optional in most lessons today (section 5.2); "try a second method" is not in every lesson. | Keep once Wonder and Look back are in every lesson (section 6). Until then: "Open investigations: many lessons include finding every way, spotting a pattern, making up a puzzle or asking 'what if?'. Each lesson ends with a look-back where children note what was hard and what helped." |
| 5 | `lp_build.py:55` -> `mi_signup.html:292` | "Frameworks that inspire the design include ... Pólya's problem-solving steps and mathematical habits of mind." | Fine as inspiration; avoid implying the six habits are those frameworks. | No change; after the six habits are published add: "The six Math Inquirers habits are our own working set." |
| 6 | `lp_build.py:62`, `lp_build.py:178` (replace) -> `mi_signup.html:299`; `level_pages.py:274` -> `level_pages/ages-*.html:289` | "In class, the answer is only half the job. Children then explain how they know, and hear other ways of seeing the same puzzle. That is where the thinking grows." | Outcome ("thinking grows"). The source string at `lp_build.py:62` says "Hearing three different ways is how thinking grows", replaced at build time by line 178. | "In class, the answer is only half the job. Children explain how they know and hear other ways of seeing the same puzzle. Explaining is one of the habits we practise in every lesson." Also remove the stale source string at `lp_build.py:62` so the replace at line 178 is not needed. |
| 7 | `level_pages.py:264` -> `level_pages/ages-*.html:279` | "The 10 lessons: What your child learns ... Each lesson follows the same four steps: notice the pattern, test it, check the answer, explain why." | Heading promises learning; four steps, as above. | "The 10 lessons: What your child works on ... Each lesson practises the inquiry habits: noticing, wondering, trying, checking, explaining and looking back." |
| 8 | `level_pages.py:266-269` -> `level_pages/ages-*.html:281-284` | "Think harder: Questions that ask for more than one step, a full list of possibilities, or a reason." / "Go further: Open challenges with room to explore, where the aim is to find a way in and explain it." | Process description; acceptable. | No change. |
| 9 | `website/hub/qa.py:67` -> `hub/parent_questions.html:5, 266` | "Each 90-minute lesson follows the four Inquirer steps: notice the pattern, test it with objects, check the answer, explain why." | Four-step claim, as above. | "Every lesson practises six inquiry habits: noticing, wondering, trying, checking, explaining and looking back." |
| 10 | `hub/qa.py:39` -> `hub/parent_questions.html:5, 257` | "Ask 'How do you know?' every time, including when the answer is right. Children quickly learn that the reason matters." | Outcome ("quickly learn"). | "Ask 'How do you know?' every time, including when the answer is right. This gives your child regular practice at giving a reason." |
| 11 | `hub/qa.py:48` -> `hub/parent_questions.html:5, 260` | "Make it safe to be stuck: struggling a little is how thinking grows." | Outcome-style generalisation. | "Make it safe to be stuck: being stuck for a little while is a normal part of working on a puzzle." |
| 12 | `hub/qa.py:59` -> `hub/parent_questions.html:5, 263` | "... the goal is curiosity and persistence. Watch for signs your child is ready: enjoys puzzles, explains reasons, and keeps trying when stuck." | "Goal is curiosity and persistence" reads as a promised trait. | "... the aim is to give children practice at wondering and at keeping going. Signs your child may enjoy these: ..." |
| 13 | `hub/qa.py:52` -> `hub/parent_questions.html:5, 261` | "... uses ideas from approaches common in gifted education (depth, reasoning and explaining why) and extends thinking beyond the school syllabus ..." | "Extends thinking" is an outcome; gifted-education link is already hedged. | "... uses depth, reasoning and explaining why, which are common in enrichment approaches, and goes beyond the school syllabus without racing ahead." |
| 14 | `website/lp_build.py:38`, `level_pages.py:260`, `build_site.py:61`, `shop_build.py:181`, generated copies (`mi_signup.html:275`, `level_pages/ages-*.html:275`, `shop/shop.html:324`) | Slogan "Notice it. Test it. Explain why." | Slogan only names three of the six habits; not an outcome claim. | Keep as the slogan. Add the full set on the habits section once published; do not describe the slogan as "the three habits". |
| 15 | `website/lp_build.py:60` -> `mi_signup.html:297` | "Notes on where your child is ready to be stretched further" | Not about inquiry skills; the tutor note should record the habit practised (section 6 package). | "A note after each lesson: the inquiry habits we practised and one thing your child said or did." (Evidence, not a grade, per the design.) |
| 16 | `docs/pedagogy/holiday_parent_outcomes_draft.md:43` | "Children are asked 'how do you know?' often, and learn to test an idea before they trust it." | Outcome ("learn to"). | "Children are asked 'how do you know?' often, and practise testing an idea before they trust it." |
| 17 | `docs/pedagogy/holiday_parent_outcomes_draft.md:111` | "Your child will also learn eight simple tools for starting a problem ..." | "will learn". | "Your child will also practise using eight simple tools for starting a problem ..." |
| 18 | `docs/pedagogy/holiday_parent_outcomes_draft.md:15, 30, 45, 60, 75, 90` | "By the end, your child will practise being able to say: I can ..." | Hedged with "practise"; the "I can" lists still read as end-state skills. | Keep the stem; where an item names a habit, reword as "I practise ..." (for example "I practise checking by going forwards"). |
| 19 | `docs/pedagogy/term_parent_outcomes_draft.md:31, 82, 257, 299` | "Children learn to test an idea, not just to give an answer." / "Children learn how to check an idea." / "They learn to prove that something cannot happen ..." / "Children learn to write a rule with letters so that it covers every case." | Outcome ("learn to") for inquiry skills. | "Children practise testing an idea, not just giving an answer." / "Children practise checking an idea." / "They practise showing that something cannot happen ..." / "Children practise writing a rule with letters that covers every case." |
| 20 | `docs/pedagogy/term_parent_outcomes_draft.md:19, 30, 41, 52, 70, 81, 92, 103` (and `docs/terms/level_1_year_plan.md:33, 46, 63, 80`) | Term headings "Notice it", "Test it", "Explain why", "Choose and create". | Tells a parent each term teaches one habit; conflicts with all six every term. | "Term 1 emphasis: noticing how numbers work" (and so on), with the line "Every term practises all six inquiry habits." |
| 21 | `docs/pedagogy/term_parent_outcomes_draft.md:13` | "every lesson has time to think before help, a chat where children give reasons ... and a look-back where children say what was hard and what helped." | Process wording, already good. Accurate for term L1 (talk slide in 39 of 40, look-back box in 40 of 40). | No change. Reuse as the model sentence for the website. |

Not claims, checked and left alone: `website/terms.html` and `privacy.html` (no inquiry-skill text beyond "We do not promise any exam result"), `website/data/*.json`, `weekly_dose_online.html` (prompts such as "How do you know ...?"), `syllabus/index.html` (tier definitions: process wording). Internal tutor-guide text (`hp/guide.js:28`, "Focus: Thinking skills ...") is not marketing copy.

## 8. Suggested next steps

1. Owner confirms the six habit names and the focus assignment in section 6 (swap lessons freely; keep the balance table).
2. Add `focus_habit` (and optional `support_habit`) to `levels/spine.json` per lesson and to the term lesson schema, so badge, guide line and report field are generated from one place.
3. Do the tag-only edits first (lessons graded strong or ok in their focus habit: badge, guide line, tag existing line), then the line-adding edits for Wonder, Look back and Notice.
4. Re-run this audit with the same method (section 2) and compare strength counts; then reword the website claims in section 7 after the lawyer has seen them.
