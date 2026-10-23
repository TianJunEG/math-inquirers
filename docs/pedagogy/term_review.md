# Term program: pedagogy review

Read-only review, 23 Oct 2026, branch `claude/great-fermi-1hv4vc`. Nothing in lessons, plans, books or tools was edited. This file and `docs/pedagogy/term_parent_outcomes_draft.md` are the only outputs.

**Question from the owner:** rationalise what we do. What can a child DO at the end of each 10-lesson block and at the end of the year, and how does it help them? Candidate learning spine: (1) a toolbox of named strategies the child can choose, (2) giving a reason, (3) checking and persistence.

**How to read the evidence in this file.** Level 1 findings come from the 40 built lesson files (`term/l1/lessons/l01.json` to `l40.json`, outputs in `term/l1/out/`). Levels 2 to 6 findings come from the year plans (`docs/terms/level_N_year_plan.md`) and, for Levels 2 to 5, the pre-flights (`docs/terms/l2_preflight.md` to `l5_preflight.md`); no Level 2 to 6 lesson is written, so everything there is a design intention, not a delivered lesson. Level 6 has no pre-flight. Nothing here has been tested with children. "Outcome" statements are design targets, not measured results.

---

## 0. Headline findings

1. **The toolbox is promised but not built.** The Level 1 plan says problem solving is "taught as a few named moves ... recorded on a growing Inquirer's toolbox page" (`level_1_year_plan.md`, section 1). No built lesson file mentions a toolbox before Lesson 38 (a hand-off line to Lesson 39) and Lesson 39; the pre-flight confirms "the Inquirer's toolbox page promised by the plan does not exist in any built lesson" (`l1_term3_term4_preflight.md`, finding 8 and D10). In Lessons 1 to 37 the strategies are used but hardly named: a word count over the 40 lesson files (child and tutor text together) finds "guess and check" in 3 lessons (25, 26, 39), "make a table" in 3 (27, 28, 39) and "work backwards" in 8 (24, 25, 28, 31, 37 to 40). Lesson 39 then names seven tools in one 90-minute lesson. The Level 2 plan promises that "every lesson names the move used" (`level_2_year_plan.md`, section 1); Level 1 does not do this.
2. **The "explain" habit is the strongest part of the design.** Every one of the 40 Level 1 lessons has a 6-minute Talk part, and 31 of the 40 prompts are "someone says X, is that right, how could we check?" with the same sentence starter "I think ... because ..." in 39 lessons. This is consistent, age-appropriate and cheap to run. Its weakness is that it is oral, volunteers-first, and the tutor has no structure for recording who reasoned how.
3. **The look-back is generic.** All 40 lessons end with the same 3-minute tick box (hardest, helped, next). The "helped" list is the only recurring strategy vocabulary a child sees, and it holds "drawing it" (20 lessons), "I asked for help" (14), "checking my answer" (12), "trying again" (11). It is not the toolbox. Checking is taught as a lesson only in Lesson 7 (add back), 14, 29 and 39 to 40.
4. **The strategy-rich items live where the live lesson gives them least time.** In Level 1 the Think harder, Go further and Investigation pages hold 305 of the 675 written items in the year and carry every non-routine and beyond-syllabus item (owner decisions of 23 Oct), but the live script gives "choice time" a median of 200 seconds (range 30 to 300 seconds; Lesson 40 has none). Pages 3 to 5 are, in practice, home work. The 34 live minutes that carry the thinking are Sneak-peek, Explore, Mini-lesson and Talk.
5. **Block-ending lessons are also content lessons.** Lessons 10, 20 and 30 (Level 1) introduce a new idea (Story Steps, Find One First, Calendar Detective) in only 27 to 28 live minutes because the Challenge Quest takes 20. The Level 3 and 4 pre-flights say the same of their lessons x.10 (`l3_preflight.md` finding 4, `l4_preflight.md` finding 5).
6. **"No holiday reuse" is true by title and false by item.** The pre-flights rate 75 of the 160 Level 2 to 5 term lessons as HIGH (Heavy) overlap with a holiday lesson in strand and kinds of item (L2 17, L3 20, L4 19, L5 19). At Level 1, Lessons 11, 24 to 26, 28, 36 and 40 repeat item types that are in the holiday question bank (`hp/qbank.json`). A holiday graduate meets the same idea twice a year at the same demand.
7. **Several topics repeat across levels with no change in demand.** Divisibility by digit sum appears in Levels 3, 4, 5 and 6; cube stacks and views in eight lessons across all six levels; logic grids in six; mirror and fold in five; "misleading graph scale" in three. Some of this is a healthy spiral; some is repeat (section 7).
8. **Tool coverage is uneven.** In Level 1: list-every-case spirals well (Lessons 3, 15, 17, 26, 33, 36, 40); find-the-pattern spirals (4, 16, 28, 30, 35); guess-and-check exists only in Lessons 24 to 26 and 39; "act it out" is used (the words appear in Lessons 10 to 12; Lessons 17 and 34 do it unnamed) and is missing from the seven tools of Lesson 39; "try a simpler case" is never taught at Level 1. The type matrices in the plans show the same thinness for guess-and-check, table and ways at every level (section 6).
9. **The Challenge Quest observes content recall at Start here level, not strategy choice.** Its 8 gates are "a fresh example of the Start here idea of its lesson" (`term/l1/tools/b_quest.py`), each tagged to a lesson, so a child can open a gate by recalling that lesson's method. It does ask for "how they started" in the tutor notes and has claim-checking gates (Lessons 20, 30, 40), but it cannot show tool choice or persistence (section 9).
10. **Levels do not build on one another by skill, by design.** Because places open every term and every lesson re-teaches what it needs in a 6-minute warm-up, Level N+1 never assumes Level N. Topics climb (fractions, bar model, tables); strategy sophistication does not accumulate except by convention (section 7).
11. **Evidence that this improves school marks: none, and none should be claimed.** What exists is a description of what school papers ask (section 10). The strongest transfer argument is also the least served: from Primary 3 the papers stop naming the heuristic in the question, so the child must choose a tool alone; Level 1 trains choosing in exactly one lesson.
12. **Plan hygiene.** The Level 3 plan's "Non-routine assignments" section is Level 5 text (`l3_preflight.md` finding 1); the Level 2 to 6 plans still describe a 25 to 30 minute 10-question check that the owner replaced with the Quest; the Level 6 plan's Terms 3 and 4 collide with the PSLE for children who are in Primary 6 (plan open question 1). Section 12 lists these.

---

## 1. One job each: the term program and the holiday program

### 1.1 What each does today

| | Holiday program | Term program |
|---|---|---|
| Shape | 5 weeks, 10 lessons of 90 minutes, groups of up to 8, six levels (`hp/lessons.js`, `p2` to `p6/content`) | 40 lessons a year per level, four blocks of 10, each ending in Mi's Challenge Quest (lesson 10, 20, 30, 40) |
| Stated purpose | A "standalone foundation course" (`level_N_year_plan.md` section 3 of each plan) | The year arc "Notice it, Test it, Explain why, then Choose and create" (`level_1_year_plan.md` section 1) |
| Content | The same strands as the school year, ten lessons, a Puzzle Day at the end. The Level 1 Puzzle Day already teaches "draw it, list it in order, make a table. Then check and explain" (`hp/lessons.js`, lesson 10, `mini`) | Same strands, Start here at or above the school level, Think harder with contest-style items, Go further beyond the syllabus; non-routine types named in every lesson (owner decision, 23 Oct) |
| Gifted-style design score | Auditor's rubric (`docs/gifted_research.md` section 2): Level 1 mean 13.3/24 before rework and 15.8/24 after ("partly gifted-style", `docs/audit/gifted_p1.md`) | Not scored. Reviewer's reading of Level 1 against the same rubric: about 15 to 17/24 (section 3.3), a judgement, not a measurement |
| Follow-on | Extension workbooks (10 units that follow the 10 holiday lessons, self-study; owner decision 23 Oct) | Next term, next level |

So today the two products differ in length and calendar, not in job. Both cover the school strands, both use the same three tiers and the same 90-minute routine, and both name contest-style moves.

### 1.2 Proposed jobs (one each)

- **Holiday program: "Try it."** A short, self-contained course that gives a family a real first experience of thinking-first maths in a small online group, sets the routine (think before help, explain, check), meets the first four tools (draw it, list it, make a table, work backwards: the Level 1 course already names three of these at Puzzle Day and has a working-backwards lesson), and shows which level suits the child. It does not promise a toolbox. Its self-study follow-on is the extension workbook.
- **Term program: "Build it."** A year-long sequence that names the toolbox, spirals each tool through four blocks (introduced, practised, applied, chosen independently), turns explaining into a ladder, and makes checking and staying power an explicit habit. Each block ends with a Quest that looks for the habits, not only the content.
- **Extension workbook: "Keep going alone."** Unchanged: the holiday graduate who does not enrol.

### 1.3 Where they overlap or repeat

**Level 1 (checked against `hp/lessons.js` and `hp/qbank.json`; column "Overlap with holiday L1" in the table in section 3).**

| Term lesson | Holiday lesson | Kind of overlap |
|---|---|---|
| 11 Who Is Where? | Logic Lab; question bank "6th from the front and 6th from the back" | Same item type (term Think harder: "5th from the front and 5th from the back") |
| 24, 25, 26 Dollars and Change, Price Tags, The School Shop | Coin Combos; Puzzle Day Coins card "Make 45¢ with exactly 3 coins"; question bank "pay exactly", "fewest coins", "find every set" | Same topic and item type, new numbers |
| 27 Fill the Grid | Logic Lab mini-lesson ("one tick in each row and column") | Same topic |
| 28 Make a Table | Pattern Inquiry; Puzzle Day "5, 8, 11, 14 ... 10th number"; question bank "10th pattern", "exactly 30 sticks" | Same topic and item type (term: 100th picture, "31 sticks") |
| 36 Count Everything | question bank "How many squares in a grid 3 long and 2 high" | Same item type |
| 37, 38 Graphs | Let's Plan the Fruit Party (picture graphs) | Same topic, deeper (key of 2 and 3) |
| 40 Inquirers' Showcase | Puzzle Day "write a puzzle for next year's group"; question bank "coin puzzle with exactly one answer" | Same item type |
| 39 Toolbox | Puzzle Day mini-lesson: draw it, list it, make a table, check and explain | Same idea (term version names seven tools) |

**Levels 2 to 5** (pre-flight ratings, `Holiday overlap` per lesson in `l2_preflight.md` and `l4_preflight.md`, and the "Holiday no-repeat register" in `l3_preflight.md` and `l5_preflight.md`): HIGH or Heavy in 17, 20, 19 and 19 lessons; MEDIUM in 11, 12, 8 and 10. Examples: Level 2 Lesson 1 repeats holiday digit cards, digit sums and the digit 3 from 300 to 399 (replaced in the pre-flight); Level 4 Lessons 22 and 23 are "nearly total" overlap with holiday Lessons 6 and 7. The pre-flights already bar the holiday numbers and items from the term lessons, so the repeat is of idea and problem type, not of the exact item. Level 6 has no pre-flight, so item overlap there is unchecked.

**What to do (proposal, compatible with owner decisions of 22 Oct that Term 1 is new and holiday topics return in warm-ups only).**

1. Judge "new" by the thinking demand, not only by the item bank. Give every term lesson two fields in the tutor guide: **Tool focus** (which tool is introduced, practised, applied or chosen) and **Explain rung** (section 2.4). A term lesson that shares a strand with a holiday lesson must differ in at least one of these two fields.
2. For the 75 HIGH-overlap lessons at Levels 2 to 5 and the Level 1 lessons above, either move the demand (a new tool, a higher explain rung) or merge and reorder (section 8). This also gives the holiday graduate in Term 1 an honest welcome line: "You met this tool in the holiday; today we give it a name."
3. Keep the holiday course as the front door. Do not add a "toolbox" to it, so that the term program has something real to add.

---

## 2. The learning spine: a proposed improvement

### 2.1 Reading the candidate spine

The three strands are right, and they are what the research note supports as design sources (Polya's understand, plan, carry out, look back; NRICH low-floor high-ceiling tasks with justification central; habits of mind: `docs/gifted_research.md` section 1.4). Four changes are proposed.

1. **Split strand 3.** "Checking" and "persistence" are different skills with different teaching. Checking is a method (reread, another method, estimate, test the claim with an example). Persistence is a response to being stuck. Keep both in the same strand but teach and observe them separately.
2. **Make "choosing" explicit inside strand 1.** Having tools is probably not the skill the papers reward; choosing one unaided is (an inference from section 2.3). The Quest should look for it.
3. **Add a ladder to strand 2** so that "give a reason" means something different at age 6 and at age 12.
4. **Fold problem posing into strand 2 as its top rung** (the plans already end each year with "write a puzzle with one answer": Level 1 Lesson 40, Level 2 T4.8, Level 5 Lesson 38). Do not add a fourth strand.

### 2.2 The toolbox: names, schedule and level ladder

Child-facing names are short and the same at every level. The MOE syllabus pages we hold do not list named heuristics (they name Polya's four steps, metacognition and attitudes: `docs/moe/syllabus_by_level.md` line 14), so these names are our own, consistent with the hints the Primary 2 papers print ("Hint: Make a Table", "Working backwards", "Draw a timeline": `docs/books/p2_school_paper_patterns.md` finding 5).

| Tool (child's words) | Candidate list item | Level 1 schedule (block: lessons) | Added at higher levels |
|---|---|---|---|
| **Draw it** (picture, line, strip) | draw it | Introduce B1 (1, 2, 9); practise B2 (12, 15, 18); apply B4 (31, 32); choose (39) | Bar model (L2 onward); before-and-after (L3); diagrams for angles and tanks (L5) |
| **Act it out** | act it out | Name in B1 Lesson 10 (counters, "read twice, act it"); practise 11, 17; apply 34 (fold) | Track transfers with counters (L2); simulate (L6) |
| **Find the pattern** | find the pattern | Introduce B1 (4); practise B2 (16); apply B3 (28, 30), B4 (35) | Gaps of the gaps (L2, L3); nth term (L4 to L6) |
| **List every case** | list every case | Introduce B1 (3); practise B2 (15, 17); apply B3 (26), B4 (33, 36) | Tree and multiplication principle (L3, L4); constraints (L6) |
| **Make a table** | make a table | Introduce B2 (20 find one first, as a table); practise B3 (28); apply B4 (32, 36, 37) | Ratio table (L2); two-way table (L4); spreadsheet (L6) |
| **Work backwards** | work backwards | Introduce B2 (12, 18 name it); practise B3 (23, 24); apply B4 (31, 37, 38) | Fraction of the rest backwards (L4, L5); invariants (L6) |
| **Guess and check, then improve** | guess and check | Introduce B2 (a new light item in 12 or 19); practise B3 (24 to 26); apply B4 (a new Think harder item in 33 or 36) | Suppose and compare (L4, L5) |
| **Try a simpler case** | try a simpler case | Introduce B4 (33: grid 1 by 1, 2 by 1, 2 by 2 before 3 by 2; 36: handshakes among 2, 3, 4) | Solve a smaller problem (L4 4.4); small cases for proof (L5, L6) |

Eight tools for six-to-eight-year-olds is a lot; the schedule introduces two per block, so a child holds two or three at any time, and the toolbox card (below) shows only the tools introduced so far. "Find one first" and "steps" in Lesson 39's present seven are methods inside Draw it and Make a table, not separate tools.

**Rules for naming (cheap, no new lessons).**
- Tool badge: the slide where a tool is first used shows its name and a small picture; the child's workbook look-back replaces the generic "helped" list with the tools introduced so far (tick the tool you used) plus "I checked" and "I asked".
- Use the tutor-side `skill` field that every Level 1 lesson file already has (for example "Systematic cases" in Lesson 3): it is not printed in the workbook, parent summary or tutor guide (checked in the Lesson 3 outputs). Make it a required "Tool focus" field (tool and role I, P, A or C) and print it.
- A one-page, cut-out toolbox card per term in the printed book, so a child who joins mid-year gets the tools introduced so far in the first lesson (compatible with "any term can be a first term").
- Fade the hint: name the tool at Start here and Think harder; do not name it at Go further or in the Quest (matches the Primary 2 papers, which name it, and Primary 3 to 6, which do not: `p3_school_paper_patterns.md` finding 7, `p4_school_paper_patterns.md` finding 9, `p5_school_paper_patterns.md` finding 9).

### 2.3 What the school papers say about the spine

From the question catalogues (`docs/books/p1` to `p6_non_routine_catalogue.md`; counts describe the papers the owner supplied, not the country, and recording rules differ by level, so only the direction is meaningful):

| Level | Papers read | Non-routine items recorded | Per paper |
|---|---|---|---|
| P1 | 78 | 268 | 3.4 |
| P2 | about 138 | 556 | about 4.0 |
| P3 | 197 | 1098 | about 5.6 |
| P4 | 111 labels | 807 | about 7.3 |
| P5 | 166 labels | 2279 | about 13.7 |
| P6 | 138 | 3078 | about 22 |

Three points follow.
1. The share of questions that need a tool and not only a procedure grows steeply with level. Strategy teaching matters more as the child gets older, not less.
2. The papers name the heuristic at Primary 2 and almost stop naming it from Primary 3 (two stems with "draw a timeline" or "study the model" in the Primary 3 set). The skill school asks for from Primary 3 on is therefore choosing the tool alone.
3. Reasons are asked for explicitly in the Primary 6 papers of 2026 ("trapezium because FE is not parallel to GH": `p6_school_paper_patterns.md` finding 2) and error analysis ("explain Bala's mistake") appears in Primary 3 in 2024 (`p3_school_paper_patterns.md` finding 10). Strand 2 has direct school relevance.

### 2.4 The explain ladder (strand 2)

| Rung | What the child does | Typical level and lessons |
|---|---|---|
| 1 Say what I did | "First I ... then I ..." | Level 1 all blocks |
| 2 Say why it works, with objects or a picture | "I know because" with counters, strips, the number line | Level 1 (Talk part), Level 2 |
| 3 Test a claim | Try an example; find one that breaks it ("one test is not a proof": Level 1 Lesson 14) | Level 1 Block 2 on; Level 2 T3.9; Level 3 to 5 |
| 4 Give a reason that covers every case | "It always works because ..." in one written sentence | Level 4 to 6 (Level 5 Lessons 26, 35, 38; Level 6 Lesson 36) |
| 5 Pose and defend | Write a problem with one answer and show why | Level 1 Lesson 40; Level 5 Lesson 38; Level 6 capstones |

The existing Talk part already runs rungs 2 and 3 in Level 1. What is missing is (a) naming the rung so tutors can aim and parents can see it, and (b) a written one-line reason from Level 2 (the papers want it by Primary 6).

### 2.5 Checking and staying power (strand 3)

**Look back (method):** (1) reread the question, (2) use another method or the inverse (add back, count up), (3) ask "does the answer make sense?" with "about" (estimation, taught as the idea, not the word "round"), (4) check a claim with an example, (5) check someone else's working. Level 1 teaches (2) in Lesson 7, (4) in Lesson 14, (5) in Lessons 29 and 40, (2) again in Lesson 39. Proposal: add a named "check" tick to every lesson's look-back and rehearse (3) in Block 2.

**Staying power (response to stuck):** a fixed stuck routine in child words: "Wait. Try a tool. Try a smaller case. Ask." The tutor script already says "wait 10 seconds before helping" and children can tick "I am still stuck" for a private route; the proposal adds the routine to the toolbox card. The research on productive struggle is **UNVERIFIED** in this repository (`docs/gifted_research.md` section 1.4: only a conference abstract was opened), so persistence is a design choice and a thing to observe, not an evidence claim.

---

## 3. Level 1: all 40 lessons

Source: the 40 lesson files, `docs/terms/level_1_year_plan.md` section 8.1 (non-routine types), `docs/terms/l1_term3_term4_preflight.md` section 1 (named beyond items), `hp/lessons.js` and `hp/qbank.json` (holiday overlap).

### 3.1 The 40 lessons

Notes on the columns.
- **Main strategy trained** is the reviewer's reading of what the child actually does, not a label printed in the lesson. Strategy names are rare in the lesson text (section 0, finding 1).
- **Non-routine type** is the plan's assignment (codes: LOG logical, CMP compare, BACK work backwards, CTX unfamiliar context, LIST systematic list, EXP explain or true-false, GC guess and check, PAT pattern, DIAG draw a model, MULTI multi-step, TAB table, EQ make equal, WAYS how many ways, CHAL build from clues; T = Think harder, G = Go further; never Start here).
- **Explain-it moment** is the lesson's Talk question (6 minutes: 40 s think, 60 s talk to the grown-up, 90 s share, volunteers first, a pass is always fine; Quest lessons 4 minutes, Lesson 40 14 minutes).
- **Look-back** is the 3-minute tick box in every lesson; the column shows only a lesson-specific check beyond it.
- **Problems** are Start here / Think harder / Go further + 1 Investigation; every lesson also has 3 exit-ticket items and a Sneak-peek of 2 puzzles (not counted).
- **Think time**: live minutes = Sneak-peek 4 + Explore + Mini-lesson + Talk; own-work minutes = the workbook part. Within the own-work part, Think harder, Go further and the Investigation get a "choice time" of a median 200 seconds. In Quest lessons the Quest (20 minutes) sits outside both numbers.
- **Beyond-syllabus item** is the lesson's named stretch item at Think harder or Go further (owner rule of 23 Oct).
- Holiday overlap compares topics and the Puzzle Day and Logic Lab text of `hp/lessons.js` and keyword matches in `hp/qbank.json`; it is not an item-by-item check.



**Term 1 "Notice it" (lessons 1-10)**

| # | Lesson | Big idea | Main strategy trained | Non-routine type (tier) | Explain-it moment (Talk) | Look-back (beyond the box) | Problems Start/Think/Go+Inv; exit | Think time: live min / own-work min | Beyond-syllabus item | Overlap with holiday L1 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Bundles and Singles | A number is tens and ones | Draw it (bundles, tens and ones); split a number | LOG T, CTX T | Is 40 the same as 4? Show with bundles | box only | 7/4/3+1; exit 3 | 34 / 28 | Open a bundle: 5 tens 14 ones = 6 tens 4 ones (T/G) | none (holiday has no place value) |
| 2 | Number Words and the Number Line | Every number has a place and a name | Draw it / act it out (frog hops on a line); meet in the middle | LOG G, DIAG G | Are fourteen and forty the same number? | box only | 8/4/3+1; exit 3 | 35 / 28 | Which ten is nearer (informal rounding); equal jumps of 3; two frogs meet | echo: frog hops (holiday L1) |
| 3 | Digit Cards | The order of the digits changes the number | List every case (systematic) | LIST T, LOG T | Smallest card on the left always gives the smallest number? Test 3,8 and 0,5 | box only | 8/4/3+1; exit 3 | 35 / 28 | 3 cards make 6 three-digit numbers (G2c) | none |
| 4 | The 100 Square Explorer | Patterns live in rows and columns | Find the pattern (gap grows; sum of two before) | PAT T, LIST G | Does counting in fives make one column like tens? | box only | 6/4/3+1; exit 3 | 34 / 28 | Growing-gap, add-the-last-two, interleaved sequences | same topic: skip counting 2s,5s,10s (holiday L1, L4) |
| 5 | Make-a-Ten Adding | Make tens first | Make friendly numbers (fill a ten first); choose which to move | LIST T | Mei moves 2, Ali moves 4: are both right? | explain why the total does not change | 7/4/3+1; exit 3 | 35 / 28 | Crossing tens, sums above 40, six numbers making 100 | echo: bonds to 10 and 20 (holiday L2) |
| 6 | Tens Jump, Ones Hop | Add and take away tens without carrying | Chunk (tens jump, ones hop); fewest jumps (light guess and check) | GC G, BACK T | Jump 2 tens and the ones digit changes: right? | box only | 7/4/3+1; exit 3 | 36 / 28 | Split a 2-digit step; two jump sizes, fewest jumps | none |
| 7 | Take Away, Count Up | The difference is a gap | Choose a method (take away or count up); check by adding back | CMP T, EXP G | Whose way is quicker for 52-49 and why? | check a take-away by adding back | 7/4/3+1; exit 3 | 36 / 28 | 2-digit minus 2-digit crossing a ten; the gap stays the same | echo: undo/more-fewer (holiday L5) |
| 8 | Balance and Swap | Adjust one side, adjust the other | Keep it equal (give and take) | EQ T, EXP T | Add 1 to both numbers: is 7+5 still 10? | box only | 7/4/3+1; exit 3 | 36 / 28 | Compensation 49+26 = 50+25 | echo: bonds (holiday L2) |
| 9 | Draw and Measure | Be exact to the nearest centimetre | Draw it exactly; add the pieces of a path | DIAG T, CMP T | Why might two children measure 15 cm and 16 cm? | how can we check a measurement | 6/3/3+1; exit 3 | 34 / 28 | Nearest cm; line starting at another mark; bent path | same topic, deeper: cubes and ruler (holiday L9) |
| 10 | Story Steps: Read It Twice (Quest lesson) | One operation per step | Read twice; one step at a time (act it out with counters) | MULTI T, CMP T, CTX T | Ali has 5 fewer than Siti's 20; Ravi says 25: agree? | check each step against what is left (T4 impossible story) | 6/4/3+1; exit 3 | 28 / 24 | Impossible story; three-step story | echo: more/fewer stories (holiday L5) |


**Term 2 "Test it" (11-20)**

| # | Lesson | Big idea | Main strategy trained | Non-routine type (tier) | Explain-it moment (Talk) | Look-back (beyond the box) | Problems Start/Think/Go+Inv; exit | Think time: live min / own-work min | Beyond-syllabus item | Overlap with holiday L1 |
|---|---|---|---|---|---|---|---|---|---|---|
| 11 | Who Is Where? | A place in a line has a name, and we can count it from either end | Draw the line / act it out; count both ends | LOG T, DIAG T | Ali is 2nd and also 6th: how? | box only | 7/4/3+1; exit 3 | 34 / 28 | Count a line from two places (8+8-1); round-table seating | echo: Logic Lab ordering; same item type: '6th from front and back' (hp/qbank.json) |
| 12 | Bar Strips: More and Fewer | A strip shows the story: a longer strip is more, and the extra part is the gap | Draw a model (strip) | CMP T, EQ T, BACK T | Same-length strips for 12 and 20: a good picture? | box only | 7/3/3+1; exit 3 | 35 / 28 | Sum and difference; make equal by moving some | echo: bar-model thinking (holiday L5) |
| 13 | Doubles and Near Doubles | Double, then adjust by one | Use a known fact (double, then adjust by 1) | EQ G | Mei: 1 more than double 7; Ali: 1 less than double 8: both right? | box only | 6/4/3+1; exit 3 | 37 / 28 | Double 35; five almost-equal numbers | echo: bonds (holiday L2) |
| 14 | Odd + Odd: Always, Sometimes, Never | One test is not a proof | Test a claim with examples (conjecture, counterexample) | EXP T | 3+5=8, so odd+odd is always even: is one test enough? | one test is not a proof | 6/4/3+1; exit 3 | 37 / 28 | Odd/even rules (a Primary 2 idea) | none (holiday has no odd/even) |
| 15 | Equal Groups | Same-size groups can be counted fast | Draw it (array, groups); list the ways | WAYS G, EXP T | 2 groups of 5 vs 5 groups of 2: same total? How sure? | box only | 6/4/3+1; exit 3 | 36 / 28 | Multiplication within 40; list ways to make equal groups of 24 | none (holiday has no multiplication) |
| 16 | Skip-Count Tables | Tables are skip counts, and the last digits show a pattern | Find the pattern (skip counts, last digits) | LIST T, PAT T | A number is in the 5s if it ends in 5 or 0: test? | box only | 6/3/3+1; exit 3 | 36 / 28 | Tables 3 and 4; numbers in two tables (common multiples) | echo: skip counting (holiday L1) |
| 17 | Sharing and Grouping | Share equally, or put into groups | Act it out (share with counters); list every case | CTX T, WAYS G | 12 shared among 3 and 12 in groups of 3 both give 4: always? | box only | 7/4/3+1; exit 3 | 35 / 30 | Division sign, left-overs; every number of friends that share 18 | none |
| 18 | Times Stories | Draw equal strips, then solve | Draw a model (equal strips) | DIAG T, EQ T, MULTI G, BACK T | Does 'twice as many' mean 2 more? | box only | 6/4/3+1; exit 3 | 35 / 30 | Twice/3 times as many with a transfer or a total | none |
| 19 | Picture Equations | A shape is a hidden number, and the same shape is always the same number | Substitute (a shape is a number); take one line from another | CTX T, EXP T | circle+circle=12, so three circles = 18: right? | check the answer in every line | 7/3/3+1; exit 3 | 34 / 30 | Symbol equations, subtract one line from another | echo: number machine rule (holiday L5) |
| 20 | Find One First (Quest lesson) | Find one, then find many | Find one first (unit), then scale; table | MULTI T, CMP G | 3 books $12, so 6 books $24: right? check | box only | 6/4/3+1; exit 3 | 27 / 25 | Price of one; compare unit prices in two shops | none |


**Term 3 "Explain why" (21-30)**

| # | Lesson | Big idea | Main strategy trained | Non-routine type (tier) | Explain-it moment (Talk) | Look-back (beyond the box) | Problems Start/Think/Go+Inv; exit | Think time: live min / own-work min | Beyond-syllabus item | Overlap with holiday L1 |
|---|---|---|---|---|---|---|---|---|---|---|
| 21 | What Time Is It? | The clock counts in 5s: the short hand names the hour and the long hand counts the minutes | Count in 5s on a scale; draw / reflect | CTX G, LOG G | Long hand on 12 is always 12 o'clock? | box only | 6/3/3+1; exit 3 | 32 / 30 | Mirror Clock (a clock seen in a mirror) | none (no time in holiday) |
| 22 | Five Minutes at a Time | Minutes live between the hours: each number the long hand passes is 5 more minutes | Chunk time (to the next hour, then the rest) | CMP G, CTX T | Long hand on the 2 is 2 minutes past? | box only | 6/4/3+1; exit 3 | 34 / 30 | Chunk the Gap (duration by chunks) | none |
| 23 | Time Passes | Time can be added: one hour later, half an hour later | Work backwards (find the start); draw a timeline | BACK T, MULTI G, CTX T | Half an hour after 7:30: 8:00 or 8:30? | box only | 6/4/3+1; exit 3 | 32 / 32 | Find the Start (reverse a duration) | none |
| 24 | Dollars and Change | Coins and notes make an amount in different ways, and change is what we count up | Guess and check; list the ways; work backwards (paid, change) | GC T, BACK T | Is a 50c coin worth more than a $1 coin? | box only | 6/4/3+1; exit 3 | 32 / 32 | Fewest Notes and Coins | same topic and item type: Coin Combos (holiday L6; qbank 'fewest coins', 'every set') |
| 25 | Price Tags: Compare and Choose | Which costs more, and by how much? The difference is the gap. | Guess and check; compare (the gap); choose numbers to a total | CMP T, GC T, LIST T, CHAL G | Top $5 more than kite, or kite $5 more than top? | use a number line to show who is right | 6/4/3+1; exit 3 | 32 / 32 | The Hidden Price (sum and difference) | same topic: Coin Combos (holiday L6) |
| 26 | The School Shop | Make a plan that fits a budget, and list every way to be sure. | List every way (systematic) with a completeness check | WAYS T, LIST T | Pen then book vs book then pen: a different way? | is this list complete? check for repeats | 6/4/3+1; exit 3 | 32 / 32 | Exactly $20 with two prices | same topic and item type: coins 'exactly' (holiday L6, Puzzle Day Coins card) |
| 27 | Fill the Grid | Each row and each column has one of each, so every empty box has a reason | Eliminate (logic grid) | LOG T | Fill every box from the row alone, never the column? | check every row and every column | 5/3/3+1; exit 3 | 32 / 32 | Four by Four grid | same topic: Logic Lab grid (holiday L8 mini-lesson: one tick per row and column) |
| 28 | Make a Table | A table finds a far-away picture without drawing every one | Make a table; find the pattern; work backwards from a total | TAB T, PAT T, BACK G | 5 triangles need 15 sticks (5x3): test with strips | box only | 5/3/3+1; exit 3 | 32 / 32 | Picture 100: 100th picture from a rule in words | same topic and item type: growing patterns, 10th term, 'exactly 30 sticks' (holiday L4, Puzzle Day, qbank) |
| 29 | Spot the Mistake | Check with a different method; a wrong answer leaves a clue | Check a second way; find the wrong step | EXP T, CMP T, LIST G | 45+28=63 again gives 63: must it be right? | the lesson IS look-back: add back, estimate, second method | 6/4/3+1; exit 3 | 32 / 32 | Does It Make Sense? (estimate with 'about') | echo: Puzzle Day 'check and explain' |
| 30 | Calendar Detective (Quest lesson) | Days and weeks go round in a cycle of 7 | Find the pattern (cycle of 7); count on | CTX T, PAT G, LOG G | 10 days after Monday: Thursday or Tuesday? | box only | 6/4/3+1; exit 3 | 27 / 25 | Hundred Days Later (14 weeks and 2 days) | none |


**Term 4 "Choose and create" (31-40)**

| # | Lesson | Big idea | Main strategy trained | Non-routine type (tier) | Explain-it moment (Talk) | Look-back (beyond the box) | Problems Start/Think/Go+Inv; exit | Think time: live min / own-work min | Beyond-syllabus item | Overlap with holiday L1 |
|---|---|---|---|---|---|---|---|---|---|---|
| 31 | Half and Quarter | A half is one of 2 equal parts and a quarter is one of 4 equal parts, whatever the shape | Draw it (cut in several ways); work backwards from a quarter | DIAG T, LOG G | Any 2 parts of a shape are halves? | box only | 6/3/3+1; exit 3 | 32 / 30 | Same Half, Different Shape (equal area) | echo: Shape Safari (holiday L7) |
| 32 | Build the Figure | Make big shapes from small shapes, and find the small shapes inside a big one | Split / draw it with a ruler; table of shape counts; list | TAB T, DIAG T, LIST G | 2 triangles always make a square? | box only | 5/3/3+1; exit 3 | 34 / 30 | Every Triangle (count hidden triangles) | same topic: Shape Safari (holiday L7) |
| 33 | Copy on the Grid | A grid lets us say exactly where things are and copy them exactly | List every route; try small grids first (implicit simpler case) | WAYS T, PAT T | 3 right then 2 up vs 2 up then 3 right: same dot? same steps? | box only | 6/3/3+1; exit 3 | 32 / 32 | Count the Routes (counting paths) | none |
| 34 | Cubes and Views | The same thing looks different from the top, from the front and when it is folded | Act it out (fold and punch); visualise | LOG T, CTX G | 6 cubes seen = 6 in the stack? | box only | 6/3/3+1; exit 3 | 32 / 32 | Fold Twice, Punch Once; hidden cube | none |
| 35 | Spot It | Compare one feature at a time | Compare one feature at a time (observe); find the pattern | LOG T, EXP G, PAT T | 'They are not the same': is that enough? Be exact | box only | 6/3/3+1; exit 3 | 32 / 32 | Shadow Match (turn is not flip) | echo: odd one out (holiday L8) |
| 36 | Count Everything | Count with a system, so you miss none and count none twice | List every case + make a table (implicit simpler case: 2, 3, 4 children) | WAYS T, TAB T, LIST T | 4 friends each shake 3 hands, so 4x3 handshakes? | box only | 6/4/3+1; exit 3 | 32 / 32 | Handshake Party (3+2+1) | same item type: 'squares in a grid' counts (hp/qbank.json) |
| 37 | Make Your Own Graph | Ask a question, sort the answers, then picture the answer | Make a table (tally) then a graph; work backwards from a total | TAB T, CHAL G, BACK T | Pet-shop graph: do we know which pet children like best? | box only | 6/3/3+1; exit 3 | 32 / 32 | One Picture Is Two (key of 2, half picture) | same topic, deeper: Fruit Party picture graphs (holiday L3) |
| 38 | Graph Detectives | Scales save space, and a graph can answer some questions and not others | Read critically; work backwards from a total | CMP T, BACK T, CHAL G | 21 books; bars 6 and 9, so third is 8: check | box only | 6/3/3+1; exit 3 | 32 / 32 | Missing Bar (key of 3) | same topic: picture graphs (holiday L3) |
| 39 | The Problem-Solving Toolbox | Pick the tool that fits the problem, then check the answer a second way | Choose the tool: strip, table, list, draw it, work backwards, find one first, steps; check a second way | BACK T, GC T, EQ G, DIAG T, TAB T | Amelia twice Wei, 24 together: 24/2=12, so Wei 12? Check a second way | check a second way (Two Roads, One Answer) | 6/4/3+1; exit 3 | 33 / 31 | Two Roads, One Answer | same idea: Puzzle Day mini-lesson 'draw it, list it, make a table, check and explain' (holiday L10) |
| 40 | Inquirers' Showcase (Quest lesson) | Teach what you found: a good puzzle has one answer and a check | Explain and teach; pose a puzzle; check a friend's puzzle | CHAL G, EXP G | Teach one favourite idea in a minute (frame) | write a puzzle with one answer and check it | 6/3/3+1; exit 3 | 37 / 15 | Puzzle With a Proof | same item type: 'make up your own puzzle with exactly one answer' (holiday L6 qbank, L10 extension) |


### 3.2 What the Level 1 table shows

1. **Load.** 675 written items a year: 250 Start here, 145 Think harder, 120 Go further, 40 Investigations, 120 exit-ticket items; 15 to 19 per lesson. Start here is 5 to 8 items in about 17 to 19 minutes (about 2.5 minutes each), which is a sensible pace for ages 6 to 8.
2. **Time shape of the 90 minutes.** Live inquiry (Sneak-peek, Explore, Mini-lesson, Talk) is 32 to 37 minutes in ordinary lessons, 27 to 28 in Lessons 10, 20, 30 and 37 in Lesson 40. Own-work is 28 to 32 minutes in ordinary lessons (24 or 25 in Quest lessons, 15 in Lesson 40). Think harder, Go further and the Investigation are "choose any time" with a median 200 seconds in class; the rest is home. For the strategy spine this means a child meets a tool in the Explore and Mini-lesson, tries it on Start here, and meets the hard, choose-your-tool problems mostly without a tutor.
3. **Explain is uniform and healthy.** 31 of 40 Talk prompts test a claim ("is that right, how could we check?"), all with the same starter. The Terms 2 and 3 slogans ("Test it", "Explain why") are not visible in the Talk part: the prompt type is the same in every term.
4. **Strategy naming is late.** The strategies a child uses in Terms 1 to 3 are not named. Draw it appears on the look-back list; the first lessons that say "guess and check", "make a table" or "work backwards" are 24 to 28, and the first with a named toolbox is 39.
5. **Look-back.** A lesson-specific checking task beyond the box appears in 12 lessons (5, 7, 9, 10, 14, 19, 25, 26, 27, 29, 39, 40; the reviewer's reading of the Talk and Think harder items). In the other 28 lessons the look-back is the tick box alone. The tick box asks what was hard and what helped; it does not ask "which tool did you use?" or "did you check?".
6. **Beyond-syllabus items are good strategy carriers** (Count the Routes, Handshake Party, Exactly $20, Two Roads One Answer, Puzzle With a Proof), but they are at Think harder or Go further and therefore mostly at home. Strategy value is higher in the Explore and Mini-lesson than the plan assumes.
7. **Level 1 Term 1 goes beyond the school syllabus on purpose** (owner decision, 22 Oct, stronger arithmetic with scaffolding). From a depth-versus-acceleration view (`docs/gifted_research.md` criterion 12, "new ideas explored through grade-appropriate content rather than pulling in next year's procedures") this is partly acceleration: two-digit subtraction across a ten (Lesson 7), odd and even (Lesson 14, a Primary 2 topic), tables of 3 and 4 (Lesson 16), division with left-overs (Lesson 17). The lessons keep it honest by labelling it for tutors and parents; the research note's guidance is to prefer depth.
8. **Holiday overlap is highest where the topic is a thinking topic** (coins, patterns, logic grids, graphs), which is where the term lessons were meant to add the most.

### 3.3 Reviewer's rubric reading of Level 1 (12 criteria of `docs/gifted_research.md`, 0 to 2; judgement, not measurement)

| # | Criterion | Score | Why |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Every lesson has 5 to 8 Start here items, 3 Think harder, 3 Go further and an Investigation with an easy first step |
| 2 | Depth over speed | 1 | 15 to 19 items a lesson; the 200-second choice window gives hard items little supported time |
| 3 | Abstraction and generalisation | 1 | Rule-finding is present (4, 16, 28, 30, 40); few "does it always work?" prompts beyond Lesson 14 |
| 4 | Justification | 1 to 2 | Talk part in all 40; oral, volunteers first, no record of who reasoned |
| 5 | Multiple solution paths | 1 | Explicit in 7 and 39; otherwise the tutor shows alternatives |
| 6 | Challenge ladder | 2 | Four tiers, anyone may choose, no finisher labels |
| 7 | Student-led inquiry | 1 | Pair talk and volunteer sharing; group of 8 online |
| 8 | Real or cross-subject context | 1 | Time, money, calendar, graphs; thin elsewhere |
| 9 | Creativity and problem posing | 1 | "Make a puzzle" Go further items in many lessons; Lesson 40 |
| 10 | Metacognition | 1 | A generic tick box in all 40; named tools only from 39 |
| 11 | Pacing flexibility | 1 to 2 | Choice time and an optional Go further slide; no pre-check |
| 12 | Extension without pure acceleration | 1 | Section 3.2, point 7 |
| | Total | about 15 to 17/24 | "Partly gifted-style" band; the largest gains are in criteria 2, 3, 5, 10 |

---

## 4. Levels 2 to 6 at plan level

Every lesson at these levels is planned on the Level 1 template: 90 minutes in 11 parts, 5 to 7 Start here, 3 to 5 Think harder, exactly 3 Go further and an Investigation (`l2_preflight.md` section 0.1, `l3_preflight.md` section 0.1, `l4_preflight.md` section 0.1, `l5_preflight.md` section 0.1), a Talk part, an exit ticket and a look-back, so per-lesson problem counts and think time equal Level 1's, except that lessons 10, 20, 30 and 40 give 19 minutes of Explore plus Mini-lesson (`l3_preflight.md` finding 4, `l4_preflight.md` finding 5). The tables below therefore show what differs by lesson: the main strategy or skill, the non-routine types (tier T = Think harder, G = Go further), an explain or check hook, the named beyond-syllabus item and the holiday overlap.

How the tables were built. Title, big idea and skill come from section 2 of each year plan. Non-routine types come from each plan's "Non-routine assignments" section, except Level 3, which uses the rebuilt section 4.1 of `l3_preflight.md` because the plan's own section is Level 5 text. The explain or check hook is the first EXP (explain, true or false) or LOG item in that assignment, or the plan's skill when it names checking or proving. The named beyond item is the pre-flight's "Beyond (named)" puzzle (Levels 2 to 5); for Level 6 it is the plan's own label. Holiday overlap is the pre-flight rating (HIGH or Heavy: same strand and same kinds of item; MEDIUM; LOW; NONE); for Level 6 only warm-ups are planned and items are not checked. A blank explain hook means the plan names no explain item for that lesson. All entries are plans, not delivered lessons.


### Level 2 (plan level, 40 lessons)

**Level 2, Term 1 (lessons 1-10)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L2 |
|---|---|---|---|---|---|---|---|
| 1 | Where Does It Live? | A number has a place on a line | Reading a scale, organised listing | LOG T, LIST T, CTX G | LOG T: find the number from clues (even/odd, tens twice the ones, between); no zero first | "Halfway Numbers" | HIGH (pre-flight) |
| 2 | Mind Maths Moves | Split a number to make a friendly sum | Splitting, spotting pairs | BACK T, EQ T, LIST G |  | "Pairs Add Up" | MEDIUM (pre-flight) |
| 3 | Share It or Group It? | Division is sharing or grouping | Sharing and grouping, choosing the step | CTX T, EXP T, MULTI G | EXP T: true or false: bags of 4, bags of 5, 6 friends, none left | "Fair for Everyone" | HIGH (pre-flight) |
| 4 | Chart Patterns | A chart shows the rule at a glance | Spot the rule, predict | PAT T, LIST G, LOG T | LOG T: odd numbers between two limits: count both ends | "Round and Round" | HIGH (pre-flight) |
| 5 | Shop Bills and Change | A bill is a sum of dollars and cents | Totalling, counting on | BACK T, GC T, CTX G |  | "Best Buy" | HIGH (pre-flight) |
| 6 | Cut It Equally | Equal parts, whatever the shape | Fair parts, comparing by a picture | LIST T, EXP T, EQ G | EXP T: which picture does not show a half or a third, and why | "Quarter the L" | HIGH (pre-flight) |
| 7 | Shape Splitters | Cut one shape into others | Visualising, organised counting | DIAG T, TAB T, LIST G |  | "Tilted Squares" | HIGH (pre-flight) |
| 8 | Read the Scale | Work out what one tick is worth | Reading scales, checking | DIAG T, CMP T, DIAG G | skill: Reading scales, checking | "Between the Ticks" | MEDIUM (pre-flight) |
| 9 | Story Detectives | Read twice, then pick the first step | Reading, choosing the step | CMP T, MULTI T, BACK T |  | "The Missing Middle" | HIGH (pre-flight) |
| 10 | Posts, Gaps and Queues (Quest lesson) | Count the gaps, not the posts | Gaps versus items, drawing it | DIAG T, CTX G, LOG T | LOG T: queue positions: where is the third child from the back | "Circle of Posts" | MEDIUM (pre-flight) |

**Level 2, Term 2 (lessons 11-20)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L2 |
|---|---|---|---|---|---|---|---|
| 11 | Graphs That Talk | A graph answers some questions and not others | Reading data critically | EXP T, TAB T, CHAL G | EXP T: true or false statements read from a graph with a key of 4 | "Graph From Clues" | MEDIUM (pre-flight) |
| 12 | Odd, Even, Fair | Even means pairs, no leftover | Conjecture and test | EQ T, EXP T, LOG T | EXP T: always, sometimes, never about odd and even sums | "Odd Staircase" | LOW (pre-flight) |
| 13 | Jumps, Gaps and Columns | Subtraction is a gap; columns are place value | Representing a process | BACK T, CMP T, EXP G | EXP G: which step of a column sum is wrong, and why | "The 495 Trick" | HIGH (pre-flight) |
| 14 | Bar Model Stories | One bar can hold the whole story | Representing | CMP T, CMP G, DIAG T, EQ G |  | "Doubling Bars" | HIGH (pre-flight) |
| 15 | Clock Detectives | A day is cut into hours and minutes | Chunking time | BACK T, CTX T, CMP G |  | "Past Midnight" | HIGH (pre-flight) |
| 16 | Table Tricks | Tables connect: 4 is double 2 | Using structure | TAB T, EXP T, PAT G | EXP T: is 8 x 3 the same as 3 x 8; is it the same as 8 + 3 | "Double Double Double" | MEDIUM (pre-flight) |
| 17 | Find All the Ways | Organise so you miss none | Systematic listing, worst case | WAYS T, WAYS G, LIST T |  | "Be Sure" | MEDIUM (pre-flight) |
| 18 | Who Is Who? | Clues rule things out | Deduction | LOG T, LOG G, EXP G | EXP G: which clue was not needed | "The Number Ring" | HIGH (pre-flight) |
| 19 | Track It | Follow what moves, not just what is | Tracking, deduction | EQ T, BACK T, CTX T |  | "I Know My Hat" | LOW (pre-flight) |
| 20 | Puzzle Lab 2 (Quest lesson) | Return, mix and make your own | Choosing a strategy | GC G, CHAL G, MULTI T |  | "Puzzle Maker" | HIGH (pre-flight) |

**Level 2, Term 3 (lessons 21-30)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L2 |
|---|---|---|---|---|---|---|---|
| 21 | Gaps That Grow | The rule can itself have a rule | Pattern of patterns | PAT T, TAB T, PAT G |  | "Triangle Numbers" | MEDIUM (pre-flight) |
| 22 | Fractions on the Line | Fractions live between 0 and 1 | Comparing by a model | LIST T, EQ T, EXP T, CMP G | EXP T: which fraction is wrong on the line, and why | "Closer to Half" | HIGH (pre-flight) |
| 23 | Shape Equations | Same shape, same value | Substitution | EQ T, CTX T, MULTI G |  | "Three Scales" | HIGH (pre-flight) |
| 24 | Estimate Like a Scientist | A good guess is checked | Estimation, checking | CTX T, MULTI T, CMP G | skill: Estimation, checking | "How Many Beans?" | LOW (pre-flight) |
| 25 | Spot the Solid | Every solid has a name and a view | Visualising | LOG T, TAB T, LIST G | LOG T: I am a solid: clues about faces and rolling | "Most and Fewest" | HIGH (pre-flight) |
| 26 | Tiles, Turns and Symmetry | Patterns repeat by flipping and turning | Describing change | PAT T, EXP T, DIAG G | EXP T: odd one out and why | "Letters in the Mirror" | NONE (pre-flight) |
| 27 | Two-Step Bar Models | Two bars, one question | Modelling | CMP T, MULTI T, DIAG T |  | "Always the Same Gap" | HIGH (pre-flight) |
| 28 | Longer Chains | A long story is short steps | Chaining steps, checking each | MULTI T, CTX T, BACK G, CMP G | skill: Chaining steps, checking each | "Five Links" | MEDIUM (pre-flight) |
| 29 | Always, Sometimes, Never | One counterexample beats a hundred examples | Justifying | EXP T, EXP G, LOG T | EXP T: find the counterexample | "Product Parity" | LOW (pre-flight) |
| 30 | Robot Recipes (Quest lesson) | A recipe must be exact | Algorithmic thinking | BACK T, LOG G, PAT T | LOG G: what does the robot do first | "Shortest Recipe" | NONE (pre-flight) |

**Level 2, Term 4 (lessons 31-40)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L2 |
|---|---|---|---|---|---|---|---|
| 31 | Chance and Fair Games | Some things are likelier | Predict, test, compare | WAYS T, EXP T, TAB G | EXP T: is the game fair, true or false | "Which Total Wins?" | NONE (pre-flight) |
| 32 | Tables Bridge | Build new facts from known ones | Decomposing | TAB T, GC G, EXP T | EXP T: 8 x 3 and 3 x 8, 6 x 4 and 4 x 6 | "Nine Pattern" | LOW (pre-flight) |
| 33 | Halves and Quarters of Things | Part of a whole, then part of an amount | Fair sharing, model | CTX T, EQ T, LIST G |  | "Half Then a Third" | MEDIUM (pre-flight) |
| 34 | Big Numbers Expedition | A thousand is ten hundreds | Place value | LIST T, LOG T, CHAL G | LOG T: number clue puzzle with even, odd and twice as many | "Four Card Count" | HIGH (pre-flight) |
| 35 | Calendar and Timetable Puzzles | Time repeats in cycles | Cycles, scheduling | CTX T, BACK T, CMP G |  | "Same Date, Next Year" | LOW (pre-flight) |
| 36 | Grid Treasure Hunt | Words can name places | Spatial language | WAYS G, PAT T, LOG T | LOG T: where is the treasure from three clues | "How Many Routes?" | NONE (pre-flight) |
| 37 | Spot the Mistake | A good solver finds the error | Look-back | EXP T, BACK G, CHAL G | EXP T: find the wrong step and say why | "Nine Check" | LOW (pre-flight) |
| 38 | Problem Posers | Making a problem shows you know it | Creating | CHAL G, MULTI G, CMP T |  | "Puzzle Doctor" | LOW (pre-flight) |
| 39 | Look Again | Look closely, then check | Visualising, checking | LOG T, PAT T, DIAG G | LOG T: mirror, turn and shadow clues | "Cube Nets" | MEDIUM (pre-flight) |
| 40 | Year Challenge Day (Quest lesson) | Show what you can do | Selecting a strategy | MULTI T, GC T, CHAL G, WAYS G |  | "Showcase Puzzle" | MEDIUM (pre-flight) |


### Level 3 (plan level, 40 lessons)

**Level 3, Term 1 (lessons 1-10)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L3 |
|---|---|---|---|---|---|---|---|
| 1 | Number Lines to 10 000 | Every number has a place on a line, and the line tells you what is nearby | Representing, estimating | LOG T, EXP T, PAT G | EXP T: true, false or not possible to tell about points on a line | "Halfway House" | MEDIUM (pre-flight) |
| 2 | Write It Down, Check It | A written method is a tidy record of what the numbers did | Error analysis | BACK T, EXP T, LOG G | EXP T: find the slip in a worked column (V2.3) | "Mirror Subtraction" | HIGH (pre-flight) |
| 3 | Multiply by Splitting | A hard product is two easy ones added | Connecting representations | MULTI T, EXP T, TAB T, CMP T | EXP T: 6 x 48 = 6 x 50 - 6 x 2 | "Product Detective" | HIGH (pre-flight) |
| 4 | Divide It Up | Dividing is sharing out the biggest pieces first | Working backwards, checking | GC T, EXP T, BACK T, LOG G | EXP T: true, false or not possible to tell about bags of 54 (V4.3) | "Smallest and Biggest" | HIGH (pre-flight) |
| 5 | Mental Maths Moves | Numbers can be bent to make easy sums, and a long list can be paired | Flexible decomposing | LIST T, EQ T, PAT G |  | "Pair It Up" | LOW (pre-flight) |
| 6 | The Hidden Question | A two-step story hides a question you must answer first | Representing, planning | CMP T, MULTI T, BACK T, LOG G | LOG G: a story that cannot work (V6.5) | "Story That Cannot Work" | HIGH (pre-flight) |
| 7 | Fractions on the Number Line | Every fraction has a place, and many names | Generalising | EQ T, EXP T, LOG G | EXP T: same point on the line (V7.1) | "Between Neighbours" | HIGH (pre-flight) |
| 8 | Dollars and Cents | Cents are just hundredths of a dollar | Estimating, checking | CTX T, LIST T, GC T, WAYS G | skill: Estimating, checking | "Exactly the Total" | MEDIUM (pre-flight) |
| 9 | Time Detectives | Time is a number line that loops | Modelling with a number line | CTX T, BACK T, BACK G, CMP G |  | "Wrong Watch" | HIGH (pre-flight) |
| 10 | Price per Piece (added) (Quest lesson) | If you know the price of several, you can find the price of one | Representing, dividing | CMP T, CTX T, TAB T, BACK T, CTX G |  | "Free Pen Price" | MEDIUM (pre-flight) |

**Level 3, Term 2 (lessons 11-20)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L3 |
|---|---|---|---|---|---|---|---|
| 11 | Length and Distance | A km is a thousand metres, and you can feel it | Estimating, reasonableness | DIAG T, GEO T, CMP T, MULTI G, DIAG G | skill: Estimating, reasonableness | "Count the Gaps" | MEDIUM (pre-flight) |
| 12 | Mass and Volume | Heavy and full are measured with the same kind of scale | Unit sense | DIAG T, MULTI T, BACK T, CMP T, DIAG G |  | "Weighing Twice" | HIGH (pre-flight) |
| 13 | Fences and Floors | Area counts squares, perimeter walks the edge, and they change independently | Representing, testing | GEO T, EXP T, GEO G | EXP T: statements about two figures | "One Side Longer" | HIGH (pre-flight) |
| 14 | Cut, Slide, Count | Moving a piece does not change its area | Decomposing | GEO T, EXP T, LIST G, MULTI G | EXP T: same area? | "Half-Square Puzzle" | HIGH (pre-flight) |
| 15 | Lines and Corners | A right angle is a ruler for every other angle | Visualising, classifying | LOG T, LIST T, EXP G | EXP G: a counterexample about crossing lines (Beyond item: V15.1) | "Crossroads Count" | HIGH (pre-flight) |
| 16 | Bar Graphs that Tell Stories | A graph's scale decides what you notice | Interpreting, questioning | EXP T, CMP T, EQ T, CHAL G | EXP T: true, false or not possible to tell from a graph (V16.3) | "The Missing Scale" | MEDIUM (pre-flight) |
| 17 | Patterns That Grow | Look at the gaps, then the gaps of the gaps | Pattern to rule | PAT T, LOG T, PAT G | LOG T: two-number sign from four examples (V17.3) | "Where Two Patterns Meet" | MEDIUM (pre-flight) |
| 18 | Balance and Swap | Equal means "same on both sides", so symbols can be swapped | Substitution | DIAG T, CMP T, EQ T, EQ G |  | "Heaviest to Lightest" | MEDIUM (pre-flight) |
| 19 | Cube Stacks and Views (added) | A solid can be read from above and from the front | Visualising | LOG T, DIAG T, LIST G | LOG T: match the views | "Fewest and Most" | NONE (pre-flight) |
| 20 | The Class Shop (project) (Quest lesson) | A realistic problem needs several skills at once | Modelling, communicating | CMP T, MULTI T, GC T, BACK G, WAYS G | skill: Modelling, communicating | "Best Plan Proof" | MEDIUM (pre-flight) |

**Level 3, Term 3 (lessons 21-30)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L3 |
|---|---|---|---|---|---|---|---|
| 21 | Fold, Flip, Mirror | Some changes keep the shape and some do not | Visualising, predicting | LOG T, EXP T, PAT G | EXP T: statements about mirror images | "Fold Three Times" | NONE (pre-flight) |
| 22 | Picture Patterns (added) | Every feature of a picture runs its own cycle | Pattern to rule, visualising | PAT T, LOG T, CHAL G | LOG T: combine-and-remove grid (V22.2) | "Hidden Rule Grid" | LOW (pre-flight) |
| 23 | Turns and Corners | Angles measure turning | Reasoning from motion | LOG T, LIST T, CTX G | LOG T: sequence of turns (V23.1) | "Turning Robot" | HIGH (pre-flight) |
| 24 | Model Makers: Times As Many | A group can be "3 units" | Representing | CMP T, DIAG T, MULTI T, CMP G |  | "Three in a Chain" | HIGH (pre-flight) |
| 25 | Before and After | When something is added or removed, the model changes in a visible way | Working backwards | BACK T, EQ T, EQ G |  | "Gap After the Gift" | HIGH (pre-flight) |
| 26 | Magic Totals | When a number belongs to several lines, it counts several times | Reasoning from constraints | LOG T, LOG G, CHAL G | LOG T: plus shape (V26.2), the 3 by 3 square (V26.3) | "Which Totals Are Impossible" | MEDIUM (pre-flight) |
| 27 | Fractions Everywhere | Fractions belong to measures, not only pictures | Applying | CTX T, MULTI T, CMP G, EQ G |  | "Half of a Dozen" | MEDIUM (pre-flight) |
| 28 | Jugs, Scales and Balances | Unequal containers can still measure | Planning | BACK T, DIAG T, GC G, DIAG G |  | "Fewest Moves" | HIGH (pre-flight) |
| 29 | Who Sat Where? | Clues eliminate, they never guess | Elimination | LOG T, EXP T, LOG G, EXP G | EXP T: true, false or not possible to tell (V29.3) | "Is It the Only Answer?" | HIGH (pre-flight) |
| 30 | The Playground Plan (project) (Quest lesson) | Constraints make design a puzzle | Optimising, communicating | GEO T, MULTI T, CMP T, CHAL G | skill: Optimising, communicating | "Biggest Playground" | MEDIUM (pre-flight) |

**Level 3, Term 4 (lessons 31-40)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L3 |
|---|---|---|---|---|---|---|---|
| 31 | Factors, Multiples and Tests | Every number is a rectangle in waiting, and its digits can tell you about the 3s | Systematic listing | LOG T, EXP T, PAT G | EXP T: statements about the 6s table | "Three Factors Only" | HIGH (pre-flight) |
| 32 | Cycles and Remainders | A cycle repeats, so the remainder tells where you land | Generalising | LOG T, PAT T, GC G | LOG T: weekday after 95 days, multiples in a range, 4s or 6s (V32.3, V32.2, V32.1) | "Last Digit Loop" | HIGH (pre-flight) |
| 33 | Counting Carefully | A list that is organised cannot miss one | Systematic counting | WAYS T, LIST T, DIAG G |  | "Count the Rectangles" | HIGH (pre-flight) |
| 34 | Counting Digits and Pages | Count by place, not by number | Systematic counting | LOG T, LIST T, CHAL G | LOG T: nth number with only even digits (V34.1) | "Pages from Digits" | HIGH (pre-flight) |
| 35 | Timetable Puzzles | Try both orders, then compare | Modelling with a number line | BACK T, MULTI T, TAB T, CMP G, CTX G |  | "Both Orders" | HIGH (pre-flight) |
| 36 | Target Practice | Operations are tools; brackets say which goes first | Experimenting | GC T, EQ T, LOG G | LOG G: every number 1 to 10 (V36.1) | "Make Every Number" | NONE (pre-flight) |
| 37 | Most for the Least | When there is a fixed supply, a bigger first digit wins | Optimising | GC T, CTX T, WAYS G |  | "Most for the Least" | LOW (pre-flight) |
| 38 | Contest Lab | A calm method beats rushing | Strategy, checking | LOG T, EXP T, MULTI T, CHAL G, CMP G | EXP T: find the error | "Possible or Impossible" | MEDIUM (pre-flight) |
| 39 | Problem-Solving Studio (added) | Choose the move before you pick up the pencil | Strategy | POSE T, EXP T, POSE G | EXP T: find the mistake (V39.1) | "Neighbour Sums" | NONE (pre-flight) |
| 40 | Mathematicians' Fair (showcase) (Quest lesson) | Posing a good problem is harder than solving one | Communicating | POSE T, POSE G, CHAL G, WAYS G | skill: Communicating | "Puzzle With a Proof" | NONE (pre-flight) |


### Level 4 (plan level, 40 lessons)

**Level 4, Term 1 (lessons 1-10)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L4 |
|---|---|---|---|---|---|---|---|
| 1 | Across the Zeros | Regrouping is place value at work | Estimate, then check | EQ G, LIST T, LOG T | LOG T: digit-card riddle | "Close Neighbours" | HIGH (pre-flight) |
| 2 | Multiply It Many Ways | A product can be split, rounded or doubled | Choose a strategy | MULTI T, CTX G, EQ T |  | "Product Bounds" | LOW (pre-flight) |
| 3 | Divisibility Detectives | Multiples have patterns you can test | Test, then prove | LOG T, CTX T, EXP T, EXP G | EXP T: always, sometimes, never about multiples | "Swap and Subtract" | HIGH (pre-flight) |
| 4 | Fraction Walls (was 2.4) | Same amount, different names | Use a model | LIST T, EXP T, CMP G | EXP T: which fraction is greater, with a reason | "Split a Fraction" | MED (pre-flight) |
| 5 | Fractions and Decimals Are Twins | Tenths and hundredths have two writings | Say it two ways | LIST T, PAT G, LOG T | LOG T: decimal digit riddle | "Eighths" | MED (pre-flight) |
| 6 | Lines That Behave (was 3.1) | Perpendicular and parallel are rules | Draw, then check | EXP T, LOG T, GEO G | EXP T: shape properties: not true of both squares and rectangles | "Diagonal Detectives" | NONE (pre-flight) |
| 7 | Sort It Out (was 4.2) | Two ways to sort | Eliminate | TAB T, LOG T, CHAL G | LOG T: logic puzzle with 3 people | "Four Friends, Four Clubs" | LOW (pre-flight) |
| 8 | Share It Out | Division is fair sharing with leftovers | Interpret the remainder | GC T, CTX T, BACK G, POSE G |  | "Biggest and Smallest Left-Overs" | LOW (pre-flight) |
| 9 | Count by Size (added) | Count each size, then add | Count systematically | PAT T, GEO G, TAB T |  | "Triangles Everywhere" | LOW (pre-flight) |
| 10 | Challenge Day 1 and Term 1 check (Quest lesson) | Choose a way in | Choose a move | GC T, BACK T, MULTI G, CHAL G |  | "Four Numbers, Three Hints" | HIGH (pre-flight) |

**Level 4, Term 2 (lessons 11-20)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L4 |
|---|---|---|---|---|---|---|---|
| 11 | The Area Model of Multiplying | Break a product into rectangles | Estimate, then check | EQ T, LOG T, EXP G | EXP G: which step of a worked product is wrong | "Two Answers" | LOW (pre-flight) |
| 12 | Remainder Riddles | What is left tells you the cycle | Spot the cycle | PAT T, LOG T, CTX G | LOG T: number with two remainder conditions | "One Short Every Time" | HIGH (pre-flight) |
| 13 | Bar Model Builder I | A picture holds the whole story | Draw a model | EQ T, CMP T, CMP G, EQ G |  | "Same in the End" | HIGH (pre-flight) |
| 14 | Fractions with Different Names (new; the walls went to 1.4) | Make the denominators match | Common denominator | LIST T, DIAG T, MULTI G |  | "One in Three Pieces" | HIGH (pre-flight) |
| 15 | What Is Left? | Fraction of what remains | Work backwards | BACK T, MULTI T, BACK G |  | "Every Day a Third" | HIGH (pre-flight) |
| 16 | Mixed Numbers on the Line | Count in pieces past the whole | Number line as tool | PAT T, CMP G, BACK T |  | "Half-Step Magic Square" | HIGH (pre-flight) |
| 17 | Decimals in Money and Measures | Same number, new unit | Convert, then compare | CTX T, CTX G, EQ T, DIAG T, DIAG G |  | "Unit Switch" | HIGH (pre-flight) |
| 18 | Decimals Times and Shares | A tenth of a tenth | Check by estimating | EQ G, MULTI T, LIST G | skill: Check by estimating | "A Tenth of a Tenth" | MED (pre-flight) |
| 19 | When Division Doesn't Come Out Even (added) | Keep dividing, then round sensibly | Round for a purpose | LIST T, CTX T, POSE G |  | "Never-Ending Decimals" | LOW (pre-flight) |
| 20 | Challenge Day 2 and Term 2 check (Quest lesson) | Models and backward thinking | Choose a model | MULTI T, EQ T, CHAL G |  | "Two Clues, Two Answers" | HIGH (pre-flight) |

**Level 4, Term 3 (lessons 21-30)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L4 |
|---|---|---|---|---|---|---|---|
| 21 | Solids and Their Nets (new; Lines That Behave went to 1.6) | Build, then flatten | Mental rotation | EXP T, TAB T, DIAG G | EXP T: which piece must be removed for a net | "Euler's Check" | HIGH (pre-flight) |
| 22 | Angle Detectives | Angles measure turning | Estimate, then check | BACK T, GEO T, LOG G | LOG G: two clock hands | "Triangle Total" | HIGH (pre-flight) |
| 23 | Rectangle Rules | Fix one thing, vary another | Find all | GEO T, LIST T, GC G |  | "Squares Win" | HIGH (pre-flight) |
| 24 | Frames and Paths | Subtract the hole | Subtract the missing | GEO T, CTX T, DIAG G |  | "Border Count" | HIGH (pre-flight) |
| 25 | Cut and Rebuild | Area does not change | Visualise | GEO T, EXP T, GEO G | EXP T: same area or same perimeter, true or false | "Where Did the Square Go?" | MED (pre-flight) |
| 26 | Mirror Patterns | Reflect about a line | Visual check | EXP T, PAT T, DIAG G | EXP T: how many lines of symmetry, and why | "Turn It Half" | HIGH (pre-flight) |
| 27 | Cube Stacks and Views | See it from every side | Mental rotation | TAB T, LOG G, EXP T | EXP T: which view cannot be right | "Most and Fewest" | MED (pre-flight) |
| 28 | Time Travellers | Time is a number line | Draw a timeline | BACK T, TAB T, CTX G |  | "Flight Time" | LOW (pre-flight) |
| 29 | Shape Studio: Hidden Lengths (added, a problem-solving studio) | Label every piece | Label, then compare | GEO T, CTX T, CHAL G |  | "Pinwheel Square" | MED (pre-flight) |
| 30 | Challenge Day 3 and Term 3 check (Quest lesson) | Paths and picture reasoning | Choose a view | LOG T, GEO G, CHAL G | LOG T: route through a map | "Seven Bridges" | NONE (pre-flight) |

**Level 4, Term 4 (lessons 31-40)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L4 |
|---|---|---|---|---|---|---|---|
| 31 | Data Detectives: Line Graphs | A graph can be read and misread | Read, then question | TAB T, EXP T, CHAL G | EXP T: spot a misleading scale | "Fill the Gap" | HIGH (pre-flight) |
| 32 | Pie Charts (new; Sort It Out went to 1.7) | The whole circle is the whole | Fraction of the whole | CHAL T, CMP T, EXP G | EXP G: which statement is true, false or not possible to tell | "Angle of a Sector" | NONE (pre-flight) |
| 33 | Patterns and Rules in Words | Find the rule | Look for a pattern | PAT T, TAB T, PAT G |  | "Gauss's Trick" | MED (pre-flight) |
| 34 | Solve a Smaller Problem | Try 3 before 100 | Solve a smaller case | PAT T, LOG G, CTX G | LOG G: pages facing each other | "Handshake Triangle" | LOW (pre-flight) |
| 35 | Make a Systematic List | Do not miss one | List in order | WAYS T, WAYS G, LIST T |  | "Fair Spinner Game" | LOW (pre-flight) |
| 36 | Working Backwards | Undo the story | Reverse operations | BACK T, BACK G, EQ T |  | "Mirror Number" | HIGH (pre-flight) |
| 37 | Suppose and Compare | Make them all the same | Suppose, compare | GC T, GC G, EQ G |  | "Balance Chain Order" | HIGH (pre-flight) |
| 38 | Looking Ahead to P5 | A taste of next year | Link ideas | DIAG T, POSE G, CMP G |  | "Cubes in a Box" | LOW (pre-flight) |
| 39 | Count Place by Place (added) | Count each place, then multiply | Count by place | LIST T, WAYS G, LOG G | LOG G: number clues with place value | "How Fast Factorials Grow" | MED (pre-flight) |
| 40 | Year-End Challenge and Term 4 check (Quest lesson) | Show what you can do | Choose a move | MULTI T, GC T, CHAL G, EQ G |  | "Pose a Puzzle" | HIGH (pre-flight) |


### Level 5 (plan level, 40 lessons)

**Level 5, Term 1 (lessons 1-10)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L5 |
|---|---|---|---|---|---|---|---|
| 1 | Shifting Places | Multiplying by 10 moves every digit one place | Predict, then check | LIST T, EQ T, POSE G | skill: Predict, then check | "Cross Out a Digit" | HIGH (pre-flight) |
| 2 | Factor Finders | Factors and multiples explain why a calculation works | List systematically; test divisibility | LIST T, LIST G, LOG T, EXP G | EXP G: find a counterexample to a claim about multiples | "Locker Parade" | MEDIUM (pre-flight) |
| 3 | Smart Calculation | Rearranging a calculation keeps its value; the order is a rule | Rearrange, then calculate | EXP T, LOG T, POSE G | EXP T: choose or write one expression for a shopping story, then find the change | "Bracket Bonanza" | HIGH (pre-flight) |
| 4 | Mixed Numbers and Sharing | A fraction is a division, and a share can be a mixed number | Regroup wholes and parts | MULTI T, CTX T, EQ G |  | "Halves Forever" | HIGH (pre-flight) |
| 5 | Fractions of Fractions | "Of" means times, and a fraction of a fraction is a smaller part | Draw it, then multiply | MULTI T, BACK G, EQ T |  | "Half-Way Squares" | HIGH (pre-flight) |
| 6 | Decimal Sense | A decimal is a fraction written in tenths | Convert between forms | EQ G, CMP T, LIST T, POSE T |  | "Never-Ending Decimals" | LOW (pre-flight) |
| 7 | Boxed-In Triangles | Enclose a triangle in a rectangle, then subtract what you added | Enclose and subtract | GEO T, GEO G, CHAL G, EXP T | EXP T: true, false or not possible to tell: triangles with equal heights | "Dots Inside, Dots on the Edge" | HIGH (pre-flight) |
| 8 | Angles and Triangle Families | The name of a triangle tells you its angles | State the fact, then use it | GEO T, GEO G, LOG T, EXP G | EXP G: circle "is" or "is not" a parallelogram, with a reason | "Five-Point Star" | HIGH (pre-flight) |
| 9 | Two Groups and the Overlap | Count the overlap once | Draw a Venn diagram, count once | CMP T, TAB T, MULTI G, LOG T | LOG T: who is where: order from clues | "Squeeze the Overlap" | LOW (pre-flight) |
| 10 | Term 1 Review and Challenge (Quest lesson) | Choose the right start, then explain why | Choose a heuristic | EQ T, BACK T, CHAL G, LOG G, PAT T | LOG G: a four-person ordering puzzle | "Exactly One" | MEDIUM (pre-flight) |

**Level 5, Term 2 (lessons 11-20)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L5 |
|---|---|---|---|---|---|---|---|
| 11 | Solid Views and Dice | A solid can be seen from the top, front and side, and turned in the mind | Visualise and check | DIAG T, LIST G, LOG T | LOG T: dice: which faces touch, which view cannot be right | "Hidden Cubes" | MEDIUM (pre-flight) |
| 12 | Boxes and Bricks | Volume counts layers of unit cubes | List without repeats | LIST T, WAYS G, EQ T |  | "Least Wrapping" | HIGH (pre-flight) |
| 13 | Tank Tales | Water keeps its volume when the container changes | Model with a diagram | BACK T, DIAG G, CTX T |  | "Stepped Tank" | HIGH (pre-flight) |
| 14 | Decimal Measures | Units are a ruler for decimals | Estimate and check | CTX T, TAB T, POSE G | skill: Estimate and check | "Rounding Rattle" | LOW (pre-flight) |
| 15 | Cut and Rearrange | Cut a shape up and the area stays the same | Dissect and rearrange | GEO G, EXP T, CHAL T | EXP T: true, false or not possible to tell: parallelogram and rectangle on the same base | "Midpoint Squares" | MEDIUM (pre-flight) |
| 16 | Rate and Working Together | A rate says how much per one, and rates add | Scale up and down; add the rates | CTX T, CTX G, TAB T, GC T |  | "Three Painters" | HIGH (pre-flight) |
| 17 | Fair Shares | Average is levelling out | Compensate | CMP G, CHAL T, TAB T, EXP G | EXP G: two groups combined: why the average is not the middle | "Merging Classes" | NONE (pre-flight) |
| 18 | Graph Stories | A graph is a short story about change | Read, then argue | TAB G, CHAL T, EXP T, TAB T | EXP T: spot a misleading axis | "Same Data, Two Stories" | NONE (pre-flight) |
| 19 | Isometric Builders | Build it, draw it, turn it | Build, draw, check from another side | DIAG T, LIST G, DIAG G | skill: Build, draw, check from another side | "Complete the Cuboid" | NONE (pre-flight) |
| 20 | Term 2 Review and Challenge (Quest lesson) | Measures combine in real problems | Choose a heuristic | CTX T, GEO G, EQ G |  | "Pour and Measure" | MEDIUM (pre-flight) |

**Level 5, Term 3 (lessons 21-30)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L5 |
|---|---|---|---|---|---|---|---|
| 21 | Percent Sense | Percent means out of 100 | Convert, then compare | POSE T, EXP T, TAB T, LOG T | EXP T: 25% of 80 and 80% of 25: equal? explain | "Percent of Percent" | HIGH (pre-flight) |
| 22 | Shop Smart | The best deal needs a calculation, not a feeling | Compare two ways | CTX T, MULTI T, GS T, WAYS T, CTX G |  | "Tax on Tax" | HIGH (pre-flight) |
| 23 | One Number as a Percent of Another | The "whole" is the number after "of" | Name the whole | MULTI G, LOG T, BACK G | LOG T: true, false or not possible to tell: 52% of the cars are red | "Juice Mix" | HIGH (pre-flight) |
| 24 | Unequal Parts | Each part is a number of units | Build a unit model | EQ T, EQ G, CMP G |  | "Shared Part" | HIGH (pre-flight) |
| 25 | Balance and Undo | Do the same to both sides | Undo, then check | BACK G, GC T, EXP T, EQ T | EXP T: find the error in a worked solution | "Odd Coin Out" | HIGH (pre-flight) |
| 26 | Number Stories | A pattern is a rule you can prove | Look at the gaps; prove it, not just see it | PAT T, PAT G, TAB T | skill: Look at the gaps; prove it, not just see it | "Not Always Doubling" | HIGH (pre-flight) |
| 27 | Count Without Counting | Order the list so nothing is missed or doubled | List systematically; count by size | WAYS T, WAYS G, LIST T |  | "Triangles Hiding" | HIGH (pre-flight) |
| 28 | Supposition Studio | Suppose everything is one kind, then adjust | Suppose, then adjust | GC T, GC G, WAYS T, WAYS G |  | "Nugget Numbers" | HIGH (pre-flight) |
| 29 | Money Grows | Interest is a percent of the money, paid every year | Compare two plans by calculation | CTX T, MULTI T, GS T, POSE G |  | "Doubling Money" | LOW (pre-flight) |
| 30 | Term 3 Review and Challenge (Quest lesson) | Percent, parts and patterns together | Choose a heuristic | MULTI T, GC T, CHAL G, PAT T |  | "Cheapest Ten" | MEDIUM (pre-flight) |

**Level 5, Term 4 (lessons 31-40)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L5 |
|---|---|---|---|---|---|---|---|
| 31 | Angles in Shapes | Split a polygon into triangles | Decompose | GEO T, LOG T, CHAL T | LOG T: true, false or not possible to tell: angle statements | "Turtle Walk" | MEDIUM (pre-flight) |
| 32 | Triangles and Quadrilaterals | Properties sort shapes into families | Classify and counter-example | EXP T, DIAG T, LOG T, GEO G | EXP T: always, sometimes or never: parallelogram, rhombus, trapezium | "Diagonal Detective" | HIGH (pre-flight) |
| 33 | Clocks and Calendars | Time repeats in cycles | Use the cycle | BACK T, TAB T, PAT G, CTX G |  | "How Often Do the Hands Meet" | LOW (pre-flight) |
| 34 | Logic Grids and Digit Puzzles | Eliminate until one answer is left | Eliminate; work column by column | LOG T, LOG G, EXP T | EXP T: find the error in a digit puzzle solution | "Digit Detective" | MEDIUM (pre-flight) |
| 35 | Odd, Even, Remainders and Extremes | Parity is an invariant, and the extreme case sets a limit | Prove it cannot be; try the extreme | LOG T, LIST G, EXP T | EXP T: counterexample for a claim about remainders | "In the Dark" | LOW (pre-flight) |
| 36 | Working Backwards | Undo from the end | Undo, then check | BACK T, BACK G, EQ G | skill: Undo, then check | "Doubling Swap" | HIGH (pre-flight) |
| 37 | The Long Question | Long questions are short ones joined together | Split into parts | MULTI T, EQ G, CTX G |  | "Which Third Side?" | MEDIUM (pre-flight) |
| 38 | Children Set the Problem | If you can write one, you understand it | Pose and defend | POSE T, CHAL G, EXP T | EXP T: find the error in a classmate's solution | "Prove It Unique" | MEDIUM (pre-flight) |
| 39 | Colouring, Cycles and Choices | Try a plan, then prove no smaller plan works | Build a plan, then prove it is the least | WAYS T, PAT T, LIST G | skill: Build a plan, then prove it is the least | "Ten Circles" | LOW (pre-flight) |
| 40 | Year Showcase (Quest lesson) | What would you tell a friend starting this year? | Reflect and explain | EXP T, POSE G, CHAL G | EXP T: choose a move for a mixed set and say why | "Puzzle With a Proof" | NONE (pre-flight) |


### Level 6 (plan level, 40 lessons)

**Level 6, Term 1 (lessons 1-10)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L6 |
|---|---|---|---|---|---|---|---|
| 1 | Big and Small Numbers | place value tells you how big | Estimating | LIST T, CTX G, EXP T | EXP T: "correct to 1 decimal place": say which digit decides | plan label: rounding intervals are contest-style | warm-up only (plan s3); items not checked |
| 2 | Fractions on the Number Line | every fraction has a home | Comparing | CMP T, LOG T, EQ G | LOG T: true, false or not possible to tell about fractions on a line |  | warm-up only (plan s3); items not checked |
| 3 | Three Names for One Number | fraction, decimal, percent | Translating | CMP T, EXP T, TAB G | EXP T: which is greater, 3/8 or 0.37 or 38%, and how you know | plan label: fractions that end and fractions that repeat (not in primary | warm-up only (plan s3); items not checked |
| 4 | Number Shortcuts | spot the structure | Seeing structure | CMP T, EXP T, LOG G | EXP T: a bracket item such as 7 x (54 - 24 / 6) + 4, with the order written out | plan label: pairing sums and "multiply by 999" are contest-style | warm-up only (plan s3); items not checked |
| 5 | Divisibility Detectives | the digits can tell you the factors | Using structure | LIST T, LOG T, LIST G | LOG T: six factors and 3 is one: multiple of 3, even, less than 10? | plan label: digit-sum tests for 3 and 9, "45 means 5 and 9" (enrichment, contest-style | warm-up only (plan s3); items not checked |
| 6 | Rules That Look Back | the next term depends on the last | Generalising | PAT T, PAT G |  | plan label: sequences are P1-P4, the rest enrichment | warm-up only (plan s3); items not checked |
| 7 | Area and Perimeter Puzzles | the same fence, a different field | Comparing measures | CHAL T, CHAL G, EXP T | EXP T: perimeter of a figure in terms of p |  | warm-up only (plan s3); items not checked |
| 8 | Fractions of a Quantity | draw the bar, then work backwards | Modelling with bars | BACK T, EQ G |  |  | warm-up only (plan s3); items not checked |
| 9 | Tiling, Bounds and Overlaps (added) | an area count can prove it is impossible | Bounding | GEO T, LIST T, CHAL G |  | plan label: bounds are contest-style, not in primary | warm-up only (plan s3); items not checked |
| 10 | Term 1 Studio (Quest lesson) | build a number toy | Choosing a move | GC T, LOG T, CHAL G | LOG T: a three-statement true, false or not possible table about a result |  | warm-up only (plan s3); items not checked |

**Level 6, Term 2 (lessons 11-20)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L6 |
|---|---|---|---|---|---|---|---|
| 11 | Ratio Recipes | parts, not amounts | Modelling with bars | EQ T, EQ G, LOG T, TAB T | LOG T: ratio statements read from a bar graph: true, false or not possible | plan label: Sec 1 ratio | warm-up only (plan s3); items not checked |
| 12 | Fractions of Fractions | area models, then nested and telescoping | Visualising | EQ G, BACK T, CMP T |  |  | warm-up only (plan s3); items not checked |
| 13 | Percent Change Detective | up 20 then down 20 | Spotting hidden wholes | BACK T, EQ T, CTX T, GS T, TAB T |  | plan label: repeated change is beyond primary | warm-up only (plan s3); items not checked |
| 14 | Rates, Work and Trains |  | Comparing change | CTX T, EQ G, CTX G |  | plan label: **kept as owner-approved enrichment, labelled a secondary-school preview** because rate or | warm-up only (plan s3); items not checked |
| 15 | Circles and Pi | measure it, then estimate it | Estimating | GEO T, GEO G, PAT T |  |  | warm-up only (plan s3); items not checked |
| 16 | Volume, Nets and Views | cubes in boxes | Seeing in 3D | DIAG T, DIAG G, GEO T |  | plan label: inverse problems P6), nets (P4), surface area (not in primary | warm-up only (plan s3); items not checked |
| 17 | Angle Chasing (and clock hands) |  | Chaining deductions | GEO T, LOG T, EXP G | EXP G: circle the words: "is isosceles because ..." | plan label: parallel-line angles not in primary | warm-up only (plan s3); items not checked |
| 18 | Symmetry and Transformations |  | Visualising change | CHAL T, LOG T, DIAG G | LOG T: how many of these shapes have at least one line of symmetry | plan label: secondary | warm-up only (plan s3); items not checked |
| 19 | Mixtures, Fair Shares and Best Buys (added) | track the total first | Tracking a total | WAYS T, CTX T, EQ T |  |  | warm-up only (plan s3); items not checked |
| 20 | Scale Models and Same-Height Triangles (Quest lesson) | lengths, areas, volumes | Synthesising | CHAL T, EQ T, GEO G |  |  | warm-up only (plan s3); items not checked |

**Level 6, Term 3 (lessons 21-30)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L6 |
|---|---|---|---|---|---|---|---|
| 21 | Letters and Brackets | area models and shortcuts | Generalising | EXP T, EXP G | EXP T: stamps at n cents paid with $5: change in terms of n | plan label: expand is Sec 1 | warm-up only (plan s3); items not checked |
| 22 | Equations on a Balance |  | Keeping it balanced | EXP T, EQ T, GC G | EXP T: a letter for a child's age: ages in two years, total given | plan label: both sides Sec 1-2 | warm-up only (plan s3); items not checked |
| 23 | At Least, At Most |  | Describing a set | LIST T, WAYS T, LOG G | LOG G: the least number that satisfies two conditions | plan label: Inequalities, number-line solution sets, integer solutions (Sec 1 | warm-up only (plan s3); items not checked |
| 24 | Maps with Numbers |  | Linking algebra and geometry | LOG T, LOG G, TAB T | LOG T: face north, turn 135 clockwise then 225 anti-clockwise | plan label: Coordinates, four quadrants (Sec 1 | warm-up only (plan s3); items not checked |
| 25 | Straight-Line Stories |  | Reading a graph | TAB T, TAB G, CTX T |  | plan label: Linear graphs from tables, gradient as rate, intersection (Sec 1-2 | warm-up only (plan s3); items not checked |
| 26 | Powers and Roots |  | Seeing growth | LIST G, PAT T, LOG T | LOG T: a square number between two limits | plan label: Squares, cubes, powers, square roots of perfect squares (Sec 1 | warm-up only (plan s3); items not checked |
| 27 | Factors, HCF, LCM and Trailing Zeros |  | Using structure | LIST T, LIST G |  | plan label: the HCF/LCM names and prime factorisation are not in primary | warm-up only (plan s3); items not checked |
| 28 | Binary and Twenty Questions |  | Representing | LOG T, LOG G, GC G | LOG T: twenty questions: what is the best first question |  | warm-up only (plan s3); items not checked |
| 29 | Reachable Numbers and Rule Grids (added) | what can you make, and what is the rule? | Finding the rule | CMP T, PAT T, CHAL G |  | plan label: Number pyramids and picture-rule grids, consecutive sums of positive whole numbers, calcul | warm-up only (plan s3); items not checked |
| 30 | Term 3 Studio (Quest lesson) | build a puzzle maker | Choosing a move | LOG T, BACK T, CHAL G | LOG T: order four runners from clues |  | warm-up only (plan s3); items not checked |

**Level 6, Term 4 (lessons 31-40)**

| # | Lesson | Big idea | Main strategy / skill (plan) | Non-routine types (tier) | Explain / check hook (plan) | Beyond-syllabus item | Overlap with holiday L6 |
|---|---|---|---|---|---|---|---|
| 31 | Statistics That Mislead |  | Critical reading | CMP T, CMP G, TAB T, LOG T | LOG T: a three-statement true, false or not possible table from a bar graph |  | warm-up only (plan s3); items not checked |
| 32 | Scatter and Spreadsheets |  | Questioning data | TAB T, CMP G, LOG G | LOG G: two things move together: what can and cannot be said | plan label: Scatter plots, correlation vs cause (Sec 2-3 | warm-up only (plan s3); items not checked |
| 33 | Two-Stage Chance |  | Predict then simulate | WAYS T, WAYS G, LOG T | LOG T: is the game fair: true, false or not possible to tell | plan label: Tree diagrams, independent events, expected value (Sec 2 | warm-up only (plan s3); items not checked |
| 34 | Counting with Constraints |  | Systematic counting | WAYS T, LIST G, GC T |  | plan label: Arrangements, selections, counting figures by size (triangles, rectangles), rearrangements | warm-up only (plan s3); items not checked |
| 35 | Patterns That Grow |  | Recursion | PAT T, PAT G, EXP G | EXP G: write the nth term and the figure with a given perimeter |  | warm-up only (plan s3); items not checked |
| 36 | Logic, Proof and Digit Puzzles |  | Proving | LOG T, LIST T, EXP G | EXP G: is the sum of three consecutive numbers always a multiple of 3? | plan label: Hong Kong enrichment | warm-up only (plan s3); items not checked |
| 37 | Olympiad-Style Workshop |  | Choosing a strategy | GC T, GC G, BACK T, WAYS G, CMP G |  |  | warm-up only (plan s3); items not checked |
| 38 | Seeing Solids (added) | rotate it in your head | Seeing in 3D | DIAG T, DIAG G |  | plan label: not in primary | warm-up only (plan s3); items not checked |
| 39 | Capstone 1 | Plan and Prototype | Planning | EXP T, CHAL G, LOG T | EXP T: explain why a test result fits your rule |  | warm-up only (plan s3); items not checked |
| 40 | Capstone 2 (Quest lesson) | Test, Explain, Present | Explaining | EXP T, CHAL G, CMP T | EXP T: explain why it works in one sentence |  | warm-up only (plan s3); items not checked |

---

## 5. "At the end of these 10 lessons your child can ..."

Each statement is traceable to the lessons in brackets (global numbers 1 to 40 within the level). These are design targets taken from the lesson objectives (Level 1) or the plan tables (Levels 2 to 6). They say what the lessons teach and give practice in, for a child who attends most of the block. They are not measured outcomes and not promises, and none is a statement about any exam. "Beyond the school year" items are marked (B) and are stretch, not the expected outcome. A mid-year joiner will have the statements for the blocks they attend.

### Level 1 (ages 6-8, Primary 1)

**Block 1, Notice it (lessons 1-10)**
1. I can show a two-digit number as bundles of ten and singles, read and write it, find it on a 0 to 100 line, and say the number before and after, even across a ten. (1, 2)
2. I can list every number that fits a clue with digit cards and say why a card cannot go first if it is 0. (3)
3. I can find and continue a number pattern on the 100 square, and say the rule even when the gap grows. (4)
4. I can add and take away within 100 by making a ten, jumping tens and hopping ones, or counting up the gap; I can pick the quicker way and check by adding back. (5, 6, 7)
5. I can say that = means "the same amount" and use give and take to keep a total the same, and say why. (8)
6. I can draw and measure a line to the nearest centimetre, and read a two-step story twice and write one number sentence for each step. (9, 10)

**Block 2, Test it (11-20)**
1. I can say a place from 1st to 10th, count it from the front or the back, and work out how many children are in a line or between two places. (11)
2. I can draw strips for a story with more, fewer, twice as many or a total, and find the gap, the total or an equal share. (12, 18)
3. I can use a double to add two close numbers (7 + 8) quickly. (13)
4. I can test a claim with an example, find an example that breaks it, and say that one example is not enough. (14, 15, 16, 17, 18, 19, 20 Talk prompts)
5. I can make equal groups, count in 2s, 3s, 4s, 5s and 10s, share equally and group equally, and write the multiplication. (15, 16, 17)
6. I can find the number a shape stands for in a picture equation, and the price of one from the price of a group. (19, 20)

**Block 3, Explain why (21-30)**
1. I can tell the time to 5 minutes with am or pm, find the time half an hour or an hour later, and find the start from the finish. (21, 22, 23)
2. I can count money in dollars and cents, find change, say how much more one price is than another, and pick coins for an exact amount. (24, 25)
3. I can list every way to spend an exact amount and check that no way is missing or repeated. (26)
4. I can solve a small grid puzzle by ruling things out, and check every row and column. (27)
5. I can make a table to find a far-away picture in a growing pattern (the 20th, the 100th) and work back from a total. (28)
6. I can check a sum a second way, find the one wrong step and say why, and use a calendar's 7-day cycle. (29, 30)

**Block 4, Choose and create (31-40)**
1. I can say a half and a quarter of a shape, and say why two halves can look different but be the same size; I can find shapes in a figure and count them with a table. (31, 32)
2. I can copy on a grid and count the routes by listing them in order. (33)
3. I can picture a fold, a view from above and a hidden cube, and say which feature of two pictures differs. (34, 35)
4. I can count every way (outfits, handshakes) without missing or doubling any. (36)
5. I can make and read a picture graph, including one where a picture stands for 2 or 3, and say what a graph cannot tell me. (37, 38)
6. I can choose a tool for a problem, solve it two ways, check that they agree, write a puzzle with one answer and check a friend's. (39, 40)

**Year-end (Level 1).** I can start a short problem with a picture, objects, a list, a table or a pattern, choose between them, say why my answer must be right with an example, and check it a second way. I can add and take away within 100, tell the time, count money and read a picture graph. (Lessons 1-40; the strategy statements rest on 3, 4, 14, 24-26, 28, 29, 33, 36, 39, 40.)

### Level 2 (ages 7-9, Primary 2; plan level)

**Block 1, Notice it (1-10)**
1. I can put a three-digit number on a line, say it in words and find the number halfway between two others. (1)
2. I can add and take away in my head by splitting numbers and pairing friendly ones. (2)
3. I can share and group equally, say what a left-over means, and count the sharer as one of the people. (3)
4. I can find the rule in a chart and use it to predict. (4)
5. I can work out a shop bill in dollars and cents and the change. (5)
6. I can name equal parts (halves, thirds, quarters) in any shape, split a figure and count the shapes by size, and read a scale where only some ticks are numbered. (6, 7, 8)

**Block 2, Test it (11-20)**
1. I can read a graph with a key and say what the graph cannot tell. (11)
2. I can test a claim about odd and even numbers with many examples. (12)
3. I can show subtraction as a gap, explain why regrouping works, and draw a bar for a story. (13, 14)
4. I can read a clock to the minute, find how long something took and when it started. (15)
5. I can build the 4s table from the 2s and list every way to do something so none is missed. (16, 17)
6. I can use clues to rule things out, follow what moves in a story, and choose a tool for a mixed set. (18, 19, 20)

**Block 3, Explain why (21-30)**
1. I can find the rule behind a pattern whose gaps grow. (21)
2. I can place and compare fractions on a line and add like fractions. (22)
3. I can find the value of each shape in a picture equation. (23)
4. I can estimate with a benchmark (1 metre, 1 kilogram, 1 litre) and then check. (24)
5. I can name solids, say how a stack looks from above and the front, and describe how a tile pattern changes or is symmetrical. (25, 26)
6. I can solve two-step and long stories by drawing bars; find an example that breaks a claim and say why a true claim is always true; write exact steps with a loop and fix the bug (B). (27, 28, 29, 30)

**Block 4, Create and connect (31-40)**
1. I can tally a game, say which result is likelier and whether the game is fair (B). (31)
2. I can build harder times-table facts from ones I know (B) and find a fraction of an amount. (32, 33)
3. I can read, write and compare four-digit numbers (B), read a timetable and follow weekday cycles. (34, 35)
4. I can give and follow directions on a grid. (36)
5. I can find the wrong step in a worked answer and say why, and write a problem that has exactly one answer. (37, 38)
6. I can check a picture after a turn or mirror, and choose a tool on a mixed set. (39, 40)

**Year-end (Level 2).** I can choose a tool (draw, list, table, work backwards) for an unfamiliar problem, say why in a sentence, and check it. I can work with three-digit numbers, money in dollars and cents, time to the minute, simple fractions and bars.

### Level 3 (ages 8-10, Primary 3; plan level)

**Block 1, Number, calculation and everyday tools (1-10)**
1. I can place numbers to 10 000 on a line and say what is nearby. (1)
2. I can add and subtract with a written method, estimate first, and find the slip in a worked sum. (2)
3. I can multiply by splitting (an area picture) and divide with a remainder, deciding whether to round up. (3, 4)
4. I can bend numbers to make easy sums and pair numbers in a long list (B). (5)
5. I can find the hidden question in a two-step story and draw a strip for it. (6)
6. I can compare and add fractions on a line, count money in dollars and cents, read time to the minute, and find the price of one. (7, 8, 9, 10)

**Block 2, Measurement, shape, data and patterns (11-20)**
1. I can estimate with benchmarks and convert lengths, mass and volume. (11, 12)
2. I can tell area from perimeter, show that one can change while the other stays, and find an area by cutting and sliding. (13, 14)
3. I can draw perpendicular and parallel lines with a set square. (15)
4. I can read and draw bar graphs with different scales and spot a misleading scale. (16)
5. I can find the rule of a pattern whose gaps grow and an operator rule from examples (B). (17)
6. I can swap symbols in picture equations and draw a cube stack from above and the front (B); I can plan a shop to a budget. (18, 19, 20)

**Block 3, Space, modelling and reasoning (21-30)**
1. I can predict a fold-and-cut and check a mirror image one feature at a time (B). (21)
2. I can find a missing picture by naming each feature's own cycle (B), and describe a turn. (22, 23)
3. I can draw "times as many" and before-and-after bars and work backwards. (24, 25)
4. I can reason about a number that counts in several lines (magic totals) (B). (26)
5. I can find fractions of lengths, time and money, and solve a pouring puzzle (B). (27, 28)
6. I can rule things out in a logic grid and plan within a budget or perimeter. (29, 30)

**Block 4, Structure, counting and showcase (31-40)**
1. I can list factors and multiples and use the digit-sum test for 3 (B). (31)
2. I can use remainders to find where a cycle lands. (32)
3. I can count outfits, posts and gaps, and handshakes without missing any (B); count digits by place (B). (33, 34)
4. I can plan a timetable by trying both orders. (35)
5. I can reach a target with brackets and guess, check and improve under a limit (B). (36, 37)
6. I can choose a move before I pick up the pencil and say what I rejected; I can write a problem and present it. (38, 39, 40)

**Year-end (Level 3).** I can choose among draw it, list it, table, pattern, work backwards and cases for an unlabelled problem, explain a step in writing, and check an answer by estimating.

### Level 4 (ages 9-11, Primary 4; plan level; lesson 1.1 = 1, 4.10 = 40)

**Block 1, Number first (1-10)**
1. I can add and subtract across zeros and estimate first. (1)
2. I can multiply in several ways (split, round and adjust, double and halve) and choose one. (2)
3. I can test divisibility by 2, 3, 5, 6, 9 and 10 and say why the test works for 3 and 9 (B). (3)
4. I can build a fraction wall, find equivalent fractions and compare. (4)
5. I can write a fraction and a decimal as each other (tenths, hundredths, quarters). (5)
6. I can draw perpendicular and parallel lines, sort with a two-way table, divide with a remainder and decide what the remainder means, and count shapes by size. (6, 7, 8, 9)

**Block 2, Number in depth (11-20)**
1. I can multiply with the area model, estimate first, and solve letter-digit sums (B). (11)
2. I can use remainders in cycles (B). (12)
3. I can draw a bar model and change one bar to see what changes. (13)
4. I can add and subtract fractions with different bottoms and a fraction of what is left. (14, 15)
5. I can add and subtract mixed numbers on a line and use decimals in money and measures. (16, 17)
6. I can multiply and divide decimals by a whole number and round a division sensibly for a purpose. (18, 19)

**Block 3, Shape, space and measure (21-30)**
1. I can match a solid to its net and say which six-square shapes fold into a cube. (21)
2. I can estimate, measure and draw angles in degrees. (22)
3. I can find all rectangles with a given area and say which has the smallest perimeter. (23)
4. I can find area and perimeter of figures with a hole by subtracting, and by cutting and rebuilding. (24, 25)
5. I can find lines of symmetry and complete a figure; I can draw views of a cube stack (B). (26, 27)
6. I can draw a timeline for duration and label every piece in a hidden-lengths puzzle. (28, 29)

**Block 4, Data, moves and the road to Primary 5 (31-40)**
1. I can read a line graph, spot a misleading scale, and read a pie chart as fractions of a whole. (31, 32)
2. I can find the rule of a pattern in words and add by pairing (B). (33)
3. I can solve a smaller problem first, make a systematic list, and work backwards. (34, 35, 36)
4. I can suppose and compare. (37)
5. I can count by place (B) and preview next year's ideas (B). (38, 39)
6. I can choose a model or move for a mixed problem and set up an open problem alone. (40)

**Year-end (Level 4).** I can name and use the tools of the year (smaller problem, list, backwards, suppose and compare, model), estimate before and check after, and give a reason in a sentence.

### Level 5 (ages 10-12, Primary 5; plan level)

**Block 1, Number and fractions (1-10)**
1. I can read, compare and round numbers to ten million, and multiply and divide by 10, 100 and 1000 by shifting digits, and say why "add a zero" is not the reason. (1)
2. I can list factors and multiples, test divisibility, and count multiples in a range (B). (2)
3. I can use the order of operations and regroup a calculation to make it easier. (3)
4. I can write a share as a mixed number, and add and subtract mixed numbers. (4)
5. I can multiply fractions by drawing, and decimals. (5, 6)
6. I can find the area of a triangle (including a tilted one by boxing in), use triangle angle facts, count an overlap once (B), and choose a heuristic from a menu. (7, 8, 9, 10)

**Block 2, Measure and make (11-20)**
1. I can read a solid from the top, front and side and solve dice and painted-cube puzzles (B). (11)
2. I can find volume and the new water level after pouring. (12, 13)
3. I can work with decimals in measures and cut a shape to find its area. (14, 15)
4. I can find a rate, add rates (a tap and a leak) and find an average (a labelled preview). (16, 17)
5. I can read a graph as a story and spot a misleading axis. (18)
6. I can build and draw a cuboid on dot paper and choose a heuristic on a mixed set. (19, 20)

**Block 3, Parts, percent and pattern (21-30)**
1. I can find a percent of a quantity, a discount, GST and interest, and name the whole in "x as a percent of y". (21, 22, 23, 29)
2. I can build a unit model for unequal parts (ratio is a preview). (24)
3. I can undo from the end and keep a balance. (25)
4. I can find a rule from the gaps and gaps of the gaps and say why the pattern must continue (B). (26)
5. I can list and count without missing any and suppose-then-adjust (B). (27, 28)
6. I can choose a heuristic on a mixed set. (30)

**Block 4, Shape, logic and strategy (31-40)**
1. I can find the angle sum of a polygon and sort quadrilaterals, using always, sometimes or never with a counterexample (B). (31, 32)
2. I can use cycles for clocks and calendars (B). (33)
3. I can rule out in logic grids and digit puzzles (B), prove that something cannot happen, and try the extreme case (B). (34, 35)
4. I can work backwards through fractions and percents and break a long question into parts. (36, 37)
5. I can pose a problem, show it has exactly one answer, and find the least using a plan and a proof (B). (38, 39)
6. I can explain which move I chose and why. (40)

**Year-end (Level 5).** I can choose among about eight tools for a problem I have not seen, break a long problem into parts, give a one-sentence reason, and check an answer by estimating.

### Level 6 (ages 11-13, maths and coding bridge; plan level)

**Block 1, Build the number toolkit (1-10)**
1. I can compare numbers with decimals, round, and find the smallest or largest number that rounds to a value. (1)
2. I can order fractions, convert among fractions, decimals and percents, and see when a decimal repeats (B). (2, 3)
3. I can use shortcuts and divisibility tests and say why they work (B). (4, 5)
4. I can find a rule that looks back to the last term (B). (6)
5. I can compare area and perimeter, take a fraction of a quantity with a bar and work backwards. (7, 8)
6. I can use an area count to prove something is impossible (B) and change a small program and predict its output. (9, 10)

**Block 2, Scale and compare (11-20)**
1. I can share in a ratio with bars and say what stays the same when the same amount is added to both parts. (11)
2. I can multiply and divide fractions by picture. (12)
3. I can find percent change and the original after a discount, and see that +20% then -20% is not back to start. (13)
4. I can combine rates (taps, workers); speed is a labelled enrichment. (14)
5. I can find circumference and area of circles, volume of a cuboid, and chase angles with a reason. (15, 16, 17)
6. I can reflect, rotate and translate (B), track a total in a mixture (B), and say how scaling changes length, area and volume. (18, 19, 20)

**Block 3, Say it for every case (21-30)**
1. I can expand and factor with area models, and test whether two expressions are always equal. (21)
2. I can solve a balance equation, including unknowns on both sides (B), and solve and list integer solutions of an inequality (B). (22, 23)
3. I can plot points, read a straight-line graph and say when two plans cost the same (B). (24, 25)
4. I can work with powers and last digits (B), HCF and LCM (B), and binary (B). (26, 27, 28)
5. I can find which totals are reachable and why (B). (29)
6. I can build and explain a small puzzle-maker program (B). (30)

**Block 4, What can we trust? (31-40)**
1. I can find averages, spot an outlier and read a misleading chart; I can say correlation is not cause (B). (31, 32)
2. I can list outcomes of two stages, predict and simulate a chance game (B). (33)
3. I can count arrangements and shapes by size (B) and use a recursive rule. (34, 35)
4. I can use a counterexample and a parity argument, and give a reason for a digit puzzle (B). (36)
5. I can choose among work backwards, supposition, pigeonhole and worst case (B), and picture a rotated solid. (37, 38)
6. I can plan, build, test and present a project and explain why it works. (39, 40)

**Year-end (Level 6).** I can pick a tool for an unfamiliar problem, justify it, test it by hand and with a small program, and explain why the result is true.

**Level 6 caution.** Level 6 Terms 3 and 4 are largely next-year (secondary 1) content taught early (algebra, inequalities, linear graphs, powers, binary, scatter, tree diagrams). That is its declared job as a bridge, but it is acceleration, not depth (research note criterion 12), and the plan asks (open question 1) whether children in Primary 6 can attend Terms 3 and 4 around the PSLE. The "I can" statements above should be offered only with that framing.

---

## 6. How the strategies spiral across the four blocks

### 6.1 Level 1 (built lessons; lessons in brackets; I = introduced, P = practised, A = applied in a new setting, C = chosen without being named)

| Tool | Block 1 (1-10) | Block 2 (11-20) | Block 3 (21-30) | Block 4 (31-40) | Verdict |
|---|---|---|---|---|---|
| Draw it | I (1, 2, 9) | P (11, 12, 15, 18) | no DIAG item (clocks, coins and calendars carry the work) | A (31, 32, 34), C (39) | Present all year; the only tool on every look-back list; named once, at 39. Gap in Block 3 |
| Act it out | I (10) | P (11, 12, 17) | none | A (34, fold and punch) | Never named; not among Lesson 39's seven tools |
| Find the pattern | I (4) | P (16) | A (28, 30) | A (33, 35) | Good thread; absent from Lesson 39's seven |
| List every case | I (3) | P (15, 17) | A (26) | A (33, 36), C (40) | Best spiral in the year |
| Make a table | none | light (15, 20) | I (28) | A (32, 36, 37), C (39) | First named in Block 3; no table item in Blocks 1 and 2 beyond "fill the table" |
| Work backwards | light (6) | light (12, 18) | I (23, 24), A (28) | A (31, 37, 38), C (39) | Not named until Block 3; earlier items are unlabelled |
| Guess and check | light (6) | none | I (24, 25), P (26) | C (39) | Three lessons plus one; dropped in Block 4 |
| Try a simpler case | none | none | none | implicit (33, 36) | **Never taught**; not in Lesson 39 |
| Check / look back | P (7) | P (14, 19) | A (29) | A (39, 40) | Spiral exists; look-back box is generic |
| Explain / test a claim | Talk part in all 40 lessons | | | | Strongest strand; the rung is never named |

**Introduced but never revisited (Level 1):** "act it out" after Lesson 34; "guess and check" after Lesson 26 except in Lesson 39; "try a simpler case" (never introduced); the strip (Lessons 12, 18) is revisited only in 25 (the hidden price) and 39.

### 6.2 Levels 1 to 6: lessons per block that carry each tool-type (plan level)

Counts are lessons per block (Block 1/2/3/4) that carry the type at Think harder or Go further in the plan's non-routine assignment (Level 3 from the rebuilt section 4.1 of its pre-flight). They show presence, not quality.

| Tool-type | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 | Level 6 |
|---|---|---|---|---|---|---|
| Draw it (DIAG) | 2/2/0/3 | 3/1/2/1 | 0/4/2/1 | 0/2/3/1 | 0/3/0/1 | 0/2/0/1 |
| Pattern (PAT) | 1/1/2/2 | 1/1/3/2 | 2/1/2/2 | 2/2/1/2 | 1/0/2/2 | 1/1/2/1 |
| Work backwards (BACK) | 1/2/3/3 | 3/3/2/2 | 5/2/2/1 | 2/2/2/1 | 2/1/2/2 | 1/2/1/1 |
| List / ways (LIST, WAYS) | 3/3/3/3 | 5/1/2/5 | 2/4/1/4 | 3/3/1/2 | 3/3/3/2 | 3/1/3/4 |
| Table (TAB) | 0/0/1/4 | 1/2/2/2 | 2/0/0/1 | 2/0/3/2 | 1/4/2/1 | 1/2/2/2 |
| Guess and check (GC) | 1/0/2/1 | 1/1/0/2 | 2/1/1/3 | 2/0/1/2 | 0/1/3/0 | 1/0/2/2 |
| Make equal (EQ) | 1/3/0/1 | 2/3/2/1 | 2/2/2/1 | 2/5/0/3 | 5/2/2/2 | 2/6/1/0 |
| Explain, true or false (EXP) | 2/3/1/2 | 2/5/3/3 | 5/4/2/3 | 3/1/4/2 | 4/3/2/5 | 4/1/2/4 |
| Pose, build from clues (CHAL, POSE) | 0/0/1/3 | 0/2/0/4 | 0/1/3/4 | 3/2/2/4 | 5/4/3/3 | 3/2/2/2 |

Gaps worth fixing at plan level: table is absent from Blocks 1 and 2 at Level 1, Blocks 2 and 3 at Level 3 and Block 2 at Level 4; guess and check is absent from Block 2 at Levels 1 and 4, Block 3 at Level 2, and from Blocks 1 and 4 at Level 5; draw it is absent from Block 1 at Levels 3 to 6 (where it matters most for a mid-year joiner); pattern is absent from Block 2 at Level 5. Neither "act it out" nor "try a simpler case" is a type in any plan, so the matrix cannot see them: "try a smaller case" appears in the Level 2 toolkit card text, Level 4 lesson 4.4 and Level 6 Term 1 text only.

Which plans promise named tools. All six do. Level 1: "one new move a term ... recorded on a growing Inquirer's toolbox page" (section 1). Level 2: a toolkit card that gains one move a term, "every lesson names the move used" (section 1). Level 3: "a ladder of named moves ... each lesson names one move and the tutor guide shows it" (section 1, principle 3). Level 4: "one problem move per lesson is named out loud", with Term 4 teaching smaller problem, list, backwards, suppose and compare as lessons 34 to 37 (section 1, principle 3). Level 5: "built one tool at a time", every Review lesson asks the child to choose a move. Level 6: moves introduced informally in Term 1, named in Term 2, free choice in Term 4. So the design intention is a thread from lesson 1 at every level.

The risk is delivery, and Level 1 shows it. The thread was promised and is missing from Lessons 1 to 37, because (a) the lesson file has a tutor-side `skill` field (for example "Systematic cases" in Lesson 3) but it is not printed in the workbook, parent summary or tutor guide (checked in the Lesson 3 outputs), (b) the pre-flight field order for Levels 3 to 5 (`l3_preflight.md` section 1.0) has "Beyond (named)" and "Non-routine work" fields but no "Tool focus" field, and (c) the look-back vocabulary is generic. Proposal: add a required "Tool focus" field (tool, role I/P/A/C) to the lesson schema and validator, print it on the guide and the child's slide, and let the look-back list the tools. This is the single cheapest change in the review.

---

## 7. Progression across levels: does Level N+1 build on Level N?

**By topic: yes.** Fractions climb from equal parts (L1 31, L2 6) to a number line (L2 22, L3 7), walls and common denominators (L4), products and quotients (L5 4-5, L6 12). The strip becomes the bar model (L1 12, 18; L2 14, 27; L3 6, 24; L4 13, 15; L5 24; L6 8, 11). Tables climb from skip counts (L1 16) to derived facts (L2 16, L3 3).

**By skill: no, by design.** Every lesson restates what it needs in a six-minute warm-up and places open each term (owner decisions 1 and 4), so Level N+1 never assumes Level N and strategy sophistication does not accumulate unless the child was there. The ladder of tools in content does exist (L1 strips and lists; L2 adds smaller case; L4 adds suppose and compare; L5 adds extreme cases and parity; L6 adds pigeonhole, invariants and proof) but is nowhere written down as a ladder. Proposal: write it down (section 2.2), carry a toolbox card per term, and put a one-line "tools met so far" in each parent report.

**Repeats where demand does not change** (each should be a spiral with a rising rung or a merge):

| Topic | Where it appears | Comment |
|---|---|---|
| Digit-sum divisibility tests | L3 31, L4 1.3, L5 2, L6 5 (plus holiday L4 H1 and L6) | Four term lessons at four levels. Suggested ladder: L3 tiles and arrays only; L4 the test (rung 2); L5 use it (count multiples in a range, missing digit); L6 prove why the test works |
| Cube stacks and views | L1 34, L2 25, L3 19, L4 27, L5 11 and 19, L6 16 and 38 | Eight lessons; the plans call the paper evidence thin. One per level at most, or two at L5 |
| Logic grids and Latin squares | L1 27, L2 18, L3 29, L4 7, L5 34, L6 36 | Six; add a changing demand (uniqueness proof at L5, L6) or keep three |
| Mirror, fold, symmetry | L1 21, L2 39, L3 21, L4 26, L5 32 | Five; L1 mirror clock, L2 mirror clocks and digits, L3 fold-and-cut: merge L2 39 and L3 21 |
| Misleading graph scale | L3 16, L4 31, L5 18, L6 31 | Four |
| Counting digits and pages | L3 34, L4 39, L5 27 (and holiday L9) | Three |
| Pairing sums (first plus last) | L2 2, L3 5, L4 33, L5 26, L6 4 | Five |
| Clock-hand angles | L3 23, L4 22, L5 33, L6 17 | Four |
| Odd and even claims | L1 14, L2 12 and 29, L5 35, L6 36 | L2 12 repeats L1 14 at the same demand |
| Tables 6 to 9 | L2 32 (preview), L3 3 | Preview then teach |
| Brackets and order of operations | L3 36 (preview), L5 3 (taught; the L3 plan also cites L4 1.2 as overlapping) | Preview then teach |
| Titles repeated | "Fractions on the Number Line" at L3 7 and L6 2; "Divisibility Detectives" at L4 3 and L6 5; "Fractions of Fractions" at L5 5 and L6 12; "Mental Maths Moves" at L2 2 and L3 5 | Check that each pair differs in demand |

The Level 1 template also carries a risk for Level 2: a child who did Level 1 Terms 2 to 4 meets Level 2's Block 2 (odd and even, graph keys, bars, clock, logic grids, mirrors) at nearly the same demand.

---

## 8. Lessons that do not earn their place

Verdicts are proposals for the owner. "Cut" means drop the lesson and spend the slot elsewhere; "merge" means fold the best item into a neighbour; "replace" means keep the slot, change the aim. A recurring replacement is a **tool lesson** (act it out, try a simpler case, guess and check then improve) because no plan teaches these as threads.

| Level and lesson | Verdict | Reason (evidence) |
|---|---|---|
| L1 13 Doubles and Near Doubles | merge into 5, free the slot for a tool lesson | Doubles within 20 are inside Primary 1; the plan flagged it a new topic; the strategy (rearrange to a friendly sum) is Lesson 5's; only one non-routine item (EQ G) |
| L1 27 Fill the Grid | replace (guess and check, then improve) | Latin square repeats at L2 18, L3 29, L5 34, L6 36 and in holiday Logic Lab; plan open question 10 calls Lessons 27 and 35 thin-evidence; guess and check has only 4 lessons |
| L1 34 and 35 (Cubes and Views, Spot It) | merge into one spatial lesson; spend the slot on "try a simpler case" | Plan open question 10 and pre-flight risk 8 call visual perception partly a practice effect; no school-paper evidence for stacks or folds |
| L1 10, 20, 30 (Story Steps, Find One First, Calendar Detective) | reorder: make x.0 a choose-the-tool lesson with the Quest and move the content into the previous slots | Each carries a new idea in 27 to 28 live minutes; Story Steps and Find One First are high value and deserve a full lesson |
| L1 39 Toolbox | re-balance, do not remove | Seven tools in one lesson; naming should start in Block 1 (section 2.2) |
| L2 T1.10 Posts, Gaps and Queues | demote to a Think harder strand of T2.7; x.10 becomes a consolidation lesson | Plan says nothing later needs it; duplicates L1 11, then L3 33 and L5 27 |
| L2 T2.2 Odd, Even, Fair | change aim (rung 3 to rung 4: why) | Repeats L1 14 at the same demand |
| L2 T3.10 Robot Recipes | replace with a tool lesson | Plan: "nothing later needs it", beyond MOE; pre-flight: no paper evidence |
| L2 T4.2 Tables Bridge, T4.4 Big Numbers Expedition | replace | Previews of Level 3 Lessons 3 and 1 (acceleration, not depth) |
| L2 T4.9 Look Again | merge with T3.6 Tiles, Turns and Symmetry | Mirror clocks repeat L1 21; L3 21 is almost the same |
| L3 36 Target Practice | cut, send brackets to L5 3 | Preview of Primary 5; overlaps L4 2 and L5 3 |
| L3 23 Turns and Corners | replace | The pre-flight calls it the weakest lesson (the "no degrees" rule leaves little to measure; owner-swap option D4) |
| L3 21 Fold, Flip, Mirror | merge with L2 39 | Duplicate |
| L3 34 Counting Digits and Pages | cut or merge | Thin evidence; repeats L4 39 and L5 27; near-copies SASMO items (pre-flight replaced them) |
| L3 38 Contest Lab | recast | The plan's "section A and B approach" is exam technique; the research note says a competition-drill series is test preparation, not depth work |
| L4 4.8 Looking Ahead to P5 | replace with a tool lesson | A preview; no paper evidence; research note criterion 12 |
| L4 4.9 Count Place by Place, 1.9 Count by Size | merge 1.9 into 4.4 Solve a Smaller Problem; cut 4.9 | No paper evidence for either; 4.9 is the third counting-digits lesson across levels |
| L4 3.5 Cut and Rebuild | merge with L3 14 Cut, Slide, Count | Same dissection idea two levels apart |
| L5 35 Odd, Even, Remainders and Extremes | split: parity with L34; pigeonhole to L6 37 | Too full (owner KIV: lesson 35 may be too full; pre-flight finding 10 "still the most overloaded"), no paper evidence. The owner's other KIV, merging 31 and 32 (Angles in Shapes, Triangles and Quadrilaterals), is left alone: the plan keeps both on purpose and this review has no stronger reason to cut them |
| L5 39 Colouring, Cycles and Choices | replace | Pre-flight: "the thinnest" lesson, with a named swap candidate |
| L6 18 Symmetry and Transformations | merge with L3 21/L4 26 spiral or replace | No paper evidence; fifth symmetry lesson across levels |
| L6 Block 3 as a whole | decide deliberately | Next-year content taught early (see section 5, Level 6 caution) |

---

## 9. How the Challenge Quest assesses the strategies, honestly

**What it is (built for Level 1: `term/l1/tools/b_quest.py`, Quest data in `l10.json`, `l20.json`, `l30.json`, `l40.json`).** Twenty minutes after the break, eight gates and an optional "secret cave", each gate "a fresh example of the Start here idea of its lesson", played with a quest partner on private paper, no score, no timer, no ranking; the tutor writes private notes and one line to the parent.

**What it does well.**
- It is low stakes and fits the owner's rules (no score, no word test, no ranking, photos returned to the business WhatsApp only).
- The tutor notes ask the right process questions: "How they started: counters, a clock face, coins, drawing, or in their head", "Where they paused or turned to their partner and what helped".
- Gates 7 and 8 test claim-checking: Level 1 Lesson 20 gate 7 ("Ben says the heart is 8"), Lesson 30 gate 7 ("a child writes 49 + 38 = 77", is it right?), Lesson 40 gate 8 ("I think of a number ... my number is 7"). These are the rung-3 and check items of the spine.
- The cave item is unseen and joins two ideas (money and listing: "exactly $14 with $2 and $5 notes"): the nearest thing to a transfer item.

**What it cannot show.**
1. **Tool choice.** Each gate is tagged to a lesson ("Lesson 29" on the answer sheet), so recalling the lesson's method is enough. Nothing asks "which tool did you choose, and why?". The sheet does not carry the tool names, because the tools are not named in Blocks 1 to 3.
2. **Persistence.** Two and a half minutes a gate, a recording paused during the Quest, and a photo of the finished page. A tutor sees the end product, not the struggle.
3. **Growth.** One snapshot per block, no start-of-block baseline, and the privacy checklist forbids any "tally, not even in your own notes".
4. **Reasoning in the child's words.** Most gates have numeric answers; the reasoning rung is visible in two gates per Quest at most.
5. **At Levels 2 to 6 the plans still describe a different thing**: a 10-question, 25 to 30 minute check (`level_2_year_plan.md` section 5, `level_6_year_plan.md` section 5), with a final "Explain" question. That text is superseded by the Quest (`l3_preflight.md` finding 4, `l4_preflight.md` finding 5, `l5_preflight.md` finding 2) and should be rewritten before Level 2 is built.

**Quest v2, within the owner's rules (no scores, no tests, no rankings).**
- Keep 8 gates and the optional cave. Make **two** gates unlabelled "mixed gates" with no lesson tag, and put on the child's sheet a row of the tool pictures introduced so far; the child ticks the one they used (tick, not mark).
- Add a "Did I check?" tick on the Quest Log, the same tick as the lesson look-back.
- Make the cave a **choose-the-tool** problem with a "because" line (rung 2 to 3).
- Extend the tutor notes with four prompts in words: tool chosen without a prompt, how they checked, a reason in their own words, what they did at the stuck moment. These are descriptions, not counts.
- Report to the parent in tool words ("Mei chose to list every way and checked that none was missing"), not content tallies.
- Be honest in the parent note: it shows what the child did that day, not a measure of the year.

---

## 10. How it helps the child: honest evidence strength

| Claim | What supports it | Strength | Say it? |
|---|---|---|---|
| The program practises what school papers ask beyond routine sums (picture, list, table, work backwards, compare, true or false) | The six question catalogues: 8,000 plus items from about 830 papers, 14 to 16 types, per-level counts in section 2.3; the school papers themselves name some heuristics at Primary 2 and stop at Primary 3 | Descriptive and moderate: a documented match to what the papers ask; the sample is the owner's folders, not the country, and classification is the analyst's | Yes: "tasks like those in school papers", never "will raise marks" |
| It improves school maths marks | Nothing in the repository measures it. The Level 1 plan itself says school practice outpaces the program on speed, written methods and reading load; the Level 6 plan says "not a goal of this program" for PSLE problem solving | None | No |
| It builds the habit of explaining and checking | Design: a Talk part in all 40 Level 1 lessons, the claim-test prompt, sneak-peek revisit, add-back and mistake lessons; Polya's look-back and NRICH justification are design sources (`docs/gifted_research.md` 1.4: secondary sources, no outcome data for this program) | Design-level only. Not observed in children. | "We practise explaining and checking in every lesson", not "your child will" |
| It improves confidence or enjoyment | No data. Design features that support safe risk-taking: passing always allowed, private paper, no scores shown, tiers anyone may choose (the NIE review describes a non-judgmental environment as a feature of gifted education: REACT 1998, secondary) | Intent only | "Designed so a child can try without being compared." Do not claim that it builds confidence |
| It prepares the child for harder problems later (transfer) | Heuristics-based instruction is standard practice and the Polya framework is widely used; this repository did not open an outcome study. The research note rates productive struggle UNVERIFIED and the gifted-programme evidence small: Steenbergen-Hu and Moon (2011), g = 0.18 on achievement, confidence interval includes zero (abstract only) | Weak and indirect | "Learning ways to start a hard problem", not "prepares for" |
| It is gifted education | The research note: no. "Enrichment-flavoured, partly gifted-style"; the holiday audit mean was 13.3 and 15.8/24 | n/a | No. Use the safe language in `docs/gifted_research.md` section 3 |

Do not claim GEP, MOE or SASMO outcomes, rankings or exam results anywhere. Nothing in this file is evidence for such a claim.

---

## 11. A simple way a tutor and parent can tell it worked

This is observation, not assessment. It respects the owner's rules: no test, no marks shown to children, no ranking, private paper, tutor notes private.

### 11.1 Start-of-term and end-of-term mini-check (tutor only, ten minutes, not announced as a check)

- **Start:** in the first lesson a child attends, use the existing 4-minute Sneak-peek for three unseen puzzles, one per kind: a story that a picture or objects solve, a "how many ways" puzzle, and a claim to test. Level 1 example set (to be scripted and verified before use): *Mei has 9 stickers, Ali has 5 more than Mei; they put all the stickers in one box: how many?* (23); *Ravi has 2 hats and 3 scarves: how many different pairs can he wear?* (6); *Siti says: if I add 1 to a number, I always get an odd number. Is Siti right?* (no: 4 + 1 = 5 but 3 + 1 = 4). Let any method be used.
- **End:** the same three kinds, new numbers, as two of the Quest's mixed gates (section 9).
- The free 30-minute placement check (`docs/levels_and_placement.md`) is a content check scored out of 10 for placement. It does not show strategy growth and should not be reused as a before-and-after for the toolbox.

### 11.2 Four observation prompts (describe in words, once per child per block)

1. **How did they start?** Picture, objects, list, table, pattern, "in my head"; named a tool or not.
2. **Did they check?** Prompted, partly, on their own; which check (second method, add back, estimate, example).
3. **What reason did they give?** Which rung (section 2.4), in their own words.
4. **What did they do when stuck?** Waited, tried another tool, asked, gave up; how long they stayed with it.

A three-word scale is optional and is **an owner decision** because the Quest privacy checklist rules out scores and tallies: *with help, with a prompt, on their own*. Used per habit across the year for one child, it shows direction without ranking children. If the owner prefers, use words only.

### 11.3 Parent report lines (replacing the generic `term_line`)

The built lessons carry one boilerplate term line per term (for example Term 1: "Your child is learning to see numbers as tens and ones, to notice patterns and to say why."), repeated in every lesson. Proposed lines name the habits and one observed example:
- "This block [Name] used [tool] to start problems, and chose it without a prompt in [n] of the [m] lessons we watched" (replace the counts with "often", "sometimes", "starting to").
- "[Name] explained why in their own words, for example: [quote]."
- "[Name] checked by [method]. A next step at home is [prompt]."
- "In Mi's Challenge Quest [Name] [specific thing seen]. This shows what [Name] did that day, not a score."

Home prompts that already exist in each lesson (`parent.ask`) are the right ones: "How do you know?", "How can you check your answer?", "Which is quicker here, and why?". Add a fourth: "Which tool did you pick first, and why?"

### 11.4 What "it worked" would look like at the end of Level 1, in observable terms

Not a promise, not a pass mark: the child names at least three tools; picks one for an unseen puzzle without being told which; gives a reason with an example; checks a result a second way when asked; and stays with a hard item past the first stuck moment. A tutor note that says this in words for most of a group over two terms is the strongest honest evidence this program can produce for itself. Because groups are up to 8, any count is anecdotal; do not publish percentages or compare groups.

---

## 12. Decisions and fixes for the owner

**Decisions**
1. Adopt the toolbox spine (section 2) and the tool schedule (2.2): yes or no. This needs a one-page card and a look-back change, not new lessons, plus about four replacement lessons per level (section 8).
2. Should lesson x.0 become a choose-the-tool consolidation lesson that hosts the Quest (section 8), moving the new ideas of Level 1 Lessons 10, 20, 30 into earlier slots?
3. Is a three-word independence scale allowed in private tutor notes (11.2), given the "no tally" rule?
4. Level 1 Term 1: keep the stronger-arithmetic decision, or move some of Lessons 7, 14, 16, 17 to Think harder only (research note criterion 12)?
5. Level 6 intake and Terms 3 and 4 around the PSLE (plan open question 1), and whether Term 3 is a bridge or an acceleration block.
6. The holiday course: confirm that the toolbox stays out of it (section 1.2) and that the "Try it" job is acceptable.

**Data fixes found**
- `docs/terms/level_3_year_plan.md` lines 274 to 394 are Level 5 text (`l3_preflight.md` finding 1, section 4 rebuilds it).
- `docs/terms/level_{2,3,4,5,6}_year_plan.md` section 5 still describe a 25 to 30 minute 10-question check; `level_1_year_plan.md` section 5 also lists "10 questions" per term. The Quest replaced them.
- The Level 1 plan's "Inquirer's toolbox page" does not exist (pre-flight finding 8).
- `docs/terms/owner_decisions.md` "Open" list is stale for the resolved items (its own correction section says so).
- All Level 1 `term_line` fields are boilerplate (see 11.3).

---

## Sources read

`docs/gifted_research.md`; `docs/levels_and_placement.md`; `docs/terms/owner_decisions.md`; `docs/terms/level_1_year_plan.md` to `level_6_year_plan.md`; `docs/terms/l1_term2_preflight.md` (headings only), `l1_term3_term4_preflight.md`, `l2_preflight.md` to `l5_preflight.md` (headline findings, per-lesson beyond items and holiday overlap, registers); `docs/books/p1` to `p6_non_routine_catalogue.md` and `_school_paper_patterns.md` (headings, counts, hint and reason findings); `docs/moe/syllabus_by_level.md` (line 14); `docs/holiday_readiness.md`; `docs/audit/gifted_p1.md`; `hp/lessons.js`, `hp/qbank.json`; `term/l1/lessons/l01.json` to `l40.json`, `term/l1/tools/b_quest.py`, `term/l1/AUTHORING.md`. Not read in full: the Level 2 to 5 pre-flight lesson specs (parsed for beyond items and overlap ratings only), the Level 6 plan's coding strands, the holiday decks, the Level 1 audits.

**Limits.** No child has taken these lessons. The overlap with the holiday course is a keyword and topic comparison at Level 1 and the pre-flights' own ratings at Levels 2 to 5. Non-routine counts depend on the analyst's classification and on what each paper happened to include. The rubric reading in 3.3 is a judgement.
