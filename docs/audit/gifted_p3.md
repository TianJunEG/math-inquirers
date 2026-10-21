# Gifted-style audit: Math Inquirers P3 (ages 8-10, finishing P3)

Audit of all 10 lessons against the owner's tier principle and the 12-criterion rubric in `docs/gifted_research.md` section 2. Marketing language comes from section 3 of the same note. The audit describes the content as it stood **before** the rework (git HEAD of `p3/content/l1.js` to `l10.js`, `rebuild/gen_p3l*.py`); what was changed is in `docs/audit/gifted_fixes_p3.md`. No item was marked compliant to be kind: a Core item counts as a violation if it needs the lesson's formal method, a bare unexplained term or notation, or has no concrete entry route.

## How the audit was done

- **Tier principle (owner).** Core must be approachable by a child who has not yet learnt the topic (objects, drawing, counting, guess-and-check, patterns, skills from the level below, no unexplained vocabulary). Think Harder needs the idea taught in the lesson, in a new setting. Challenge needs mastery of the topic plus extension (multi-step, generalise, justify, combine, open-ended, posing, what-if).
- **What was classified.** Every item in the question bank (Core C1-C6, Think Harder T1-T8/9 = bank "stretch", Challenge X1-X9), every question on the printed workbook core pages (W1-W6/7) and the slide-only Think Harder items on the lesson decks (S1-S3, Lessons 5 to 8). Think Harder T1-T4 and Challenge X7-X9 are the items that print on the workbook Think Harder pages; slide Challenge items are copies of bank items, so they are not counted twice. Star ("if time") worksheet parts are counted with their question.
- **Compliance %** = items classed compliant / items audited, per lesson, before the rework. Violations carry a one-line reason below.
- **Rubric** scores are 0/1/2 per criterion, with the bands from the research note: 20-24 genuinely depth-oriented ("gifted-style"), 12-19 enrichment-flavoured with gaps ("partly"), under 12 mainly ordinary tuition or drill ("mainly enrichment / practice"). The bands are the research note's suggestion, not from a source. The rubric measures design features, not outcomes or who is taught.
- **Scores are before the rework** except where the "after" column says otherwise. After the rework only two criteria move: 6 (the challenge ladder, because every tier now complies) and 9 (problem posing, one printed prompt per lesson).

## 1. Summary table

| L | Title | Topic | Items audited | Violations | Tier compliance (before) | Tier compliance (after rework) | Rubric /24 (before) | Rubric /24 (after) | Verdict (before) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Number Sleuths | Numbers to 10 000 | 29 | 5 | 83% | 100% | 16 | 18 | partly |
| 2 | Cryptarithm Crackers | Addition and subtraction | 29 | 5 | 83% | 100% | 15 | 17 | partly |
| 3 | Times Table Treasure | Tables of 6, 7, 8, 9 | 29 | 5 | 83% | 100% | 17 | 19 | partly |
| 4 | Model Makers | Word problems (bar models) | 30 | 8 | 73% | 100% | 16 | 18 | partly |
| 5 | Remainder Riddles | Division | 32 | 5 | 84% | 100% | 16 | 18 | partly |
| 6 | Fraction Walls | Fractions | 33 | 9 | 73% | 100% | 15 | 17 | partly |
| 7 | Area Architects | Area and perimeter | 32 | 10 | 69% | 100% | 17 | 19 | partly |
| 8 | Angle and Line Detectives | Angles, perpendicular and parallel lines | 32 | 12 | 62% | 100% | 14 | 16 | partly |
| 9 | Measure and Money Masters | Length, mass, volume, money, time | 30 | 5 | 83% | 100% | 15 | 17 | partly |
| 10 | Challenge Day | Mixed: bar graphs, logic | 29 | 5 | 83% | 100% | 16 | 18 | partly |
| | **Level** | | **305** | **69** | **77%** | 100% | **15.7 mean** | **17.7 mean** | **partly** |

"After rework" compliance is my own re-audit of the replaced items against the same test, not an independent check. Every numeric answer in new or changed items was verified in Python (see the fixes file).

## 2. Overall verdict for the level

**Partly gifted-style.** P3 is a well-organised enrichment programme with several genuinely gifted-style habits, but it is not yet a depth-oriented series. Rubric totals before the rework run from 14 to 17 out of 24 (mean 15.7); the best lessons (3 and 7) are at 17 and 17, the weakest (8) at 14. After the rework the level reaches 16 to 19 (mean 17.7), which is still in the 12-19 band, so the honest label stays "enrichment-flavoured with gaps".

What is genuinely strong:
- **Low floor, high ceiling starts (criterion 1 = 2 in all ten lessons).** Every lesson opens with a hands-on explore any child can start (cards, cubes, counters, folding, squares, a $20 planner) and names an extension for early finishers.
- **Justification and generalisation (criteria 3 and 4 = 2 in most lessons).** "How do you know you have ALL of them?", "does it always work?", Ravi's and Mei's wrong claims, last-digit and remainder patterns.
- **Extension within the syllabus (criterion 12 = 2 in nine lessons).** New ideas (invariants, cycles, last-digit patterns, logic) come through P3 content; nothing is pulled in from P4.

What was wrong before the rework (tier principle):
- 69 of 305 items (23%) broke the tier principle, in every lesson. Three recurring patterns: (a) **Core items that need the lesson's method or an undefined term** (bare symbol items in Lessons 6 and 9, "perimeter"/"right angle" with no definition in Lessons 7 and 8, bare "work out 35 / 4" in Lesson 5); (b) **Think Harder items that were Core recall** (Lessons 3, 8, 10); (c) **Challenge items that were one more step of Think Harder or a worksheet repeat** (all ten lessons, worst in Lessons 4, 6, 7, 8, 10).

What the rubric says is still missing (the three biggest gaps):
1. **Creativity and problem posing (criterion 9: 0 in seven lessons, 1 in three before the rework; 1-2 after).** Before the rework the only "write your own" prompts were extension notes in Lessons 4, 9 and 10 that never printed. There is now one printed posing prompt per Challenge page, but one prompt per lesson is still "occasional", not a habit.
2. **Reflection and pacing (criteria 10 and 11: 1 everywhere).** The workbook has a check step in worked examples but never asks the child to record the strategy, what was hard or what to try next (only Lesson 10's "which start helped?" talk question), and there is no pre-check or compacting: every group follows the same slide sequence, with star items as the only flexibility.
3. **Depth over speed and several solution paths (criteria 2 and 5: 1 nearly everywhere, 2 only in Lessons 3, 7, 10 for criterion 5).** Each lesson teaches one method and expects a 5-7 question page in about 30 minutes; success is still finishing the page. Contrasting methods appear only in notes.

## 3. Marketing language that is safe for P3

From `docs/gifted_research.md` section 3, restricted to what the P3 materials actually do:

**Safe, and supported by what is in the lessons**
- "A maths enrichment programme for curious, capable children finishing Primary 3, focused on reasoning and problem solving."
- "Inspired by approaches used in gifted and talented education: low-floor, high-ceiling tasks, Polya-style heuristics (draw a picture, make a list, look for a pattern, work backwards, check) and mathematical habits of mind (listing in order, spotting patterns, testing claims)." Name only the frameworks used; do not imply endorsement.
- "Open-ended investigations with room to go further, whatever your child's starting point." (true for the ten explore tasks)
- "We emphasise explaining why, testing a claim, and learning from mistakes." (true: Ravi/Mei error-analysis prompts, "how do you know?" routine)
- "Extends thinking within Primary 3 topics" (not "ahead of the syllabus"): criterion 12 is 2 in nine of ten lessons.
- "Tiered Think Harder and Challenge pages" is now accurate after the rework (it was not before: several Challenge items were Think Harder items).
- "Designed for children who enjoy thinking hard about maths."

**Not safe yet for P3**
- "Not a drill programme" or "depth over speed": criterion 2 is 1 in every lesson (a 5-7 question page in 30 minutes). Say it only after the pages are cut or a long-think-time slot is added.
- "Small groups with differentiated challenge": tiers are on the pages, but pacing is lockstep (criterion 11 = 1); say "tiered pages", not "differentiated groups".
- Anything about creativity or children inventing problems as a core feature: one prompt per lesson only.

**Never claim (all levels)**
- That it identifies, tests, certifies or "reveals" giftedness; that it is, replaces, prepares for or guarantees entry to the MOE Gifted Education Programme (P3 is the year of the MOE identification exercise, so be especially careful not to imply GEP screening preparation); that it is endorsed by MOE or NIE.
- "Gifted programme" or "for gifted children" as a descriptor of the children; prefer "gifted-education-inspired" and explain in one sentence.
- Guaranteed scores, olympiad or competition results, or that it "accelerates" learning; research-backed outcomes for this programme; suitability for every child (say who it suits and welcome placement conversations).

## 4. Lesson by lesson

Item ids: C = Core (bank), T = Think Harder (bank "stretch"; T1-T4 print on the workbook Think Harder page), X = Challenge (X7-X9 print on the workbook Challenge page), W = worksheet question on the printed core pages, S = slide-only Think Harder item. "ok" = compliant. A violation is followed by its reason.

### Lesson 1: Number Sleuths (Numbers to 10 000)

Tier compliance before: **24/29 = 83%** (5 violations). Rubric: **16/24 before, 18/24 after the rework**. Verdict: **partly**.

- **Core, question bank (C1-C6):** ok: C3, C4, C5, C6. **C1 violation**: 'thousands' used with no place value chart or concrete starter. **C2 violation**: asks the value of a digit with no chart, so it assumes place value vocabulary.
- **Think Harder, question bank (T1-T8; T1-T4 on the workbook):** ok: T1, T2, T3, T4, T5, T6, T7, T8.
- **Challenge, question bank (X1-X9; X7-X9 on the workbook):** ok: X1, X2, X3, X5, X6, X8, X9. **X4 violation**: same method as T5 (smallest number with a digit sum) with a bigger sum: one step repeated. **X7 violation**: repeats workbook Q6 (digit sum 3) with sum 4; only the count changes, no extension.
- **Workbook core pages (W1-W6):** ok: W1, W2, W3, W5, W6. **W4 violation**: renaming '15 hundreds' needs the idea of the lesson; no blocks or drawing hint.

| # | Rubric criterion | Score | Evidence |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Explore: 4 cards, every number 4000 to 6000; 'finished early' = all 24 numbers. |
| 2 | Depth over speed | 1 | Worksheet 6 questions in 30 min (2 are star items) plus 2 Think Harder pages; pace set by the page. |
| 3 | Abstraction and generalisation | 2 | Q3 jumps pattern, 'digits add to 3' counts 1, 3, 6 and the 24 = 6 x 4 idea move from cases toward a rule. |
| 4 | Justification | 2 | Q1e, Q4c, 'how do you know you have ALL?' ask for reasons. |
| 5 | Multiple solution paths | 1 | One taught heuristic (fix the first digit, list in order); no contrasting method on slides. |
| 6 | Challenge ladder inside the lesson | 1 (2 after rework) | Tiers exist (Core page, T1-T4, X7-X9, stars) but C1/C2/W4 had no entry and X4/X7 were repeats. |
| 7 | Student-led inquiry and discussion | 2 | Predict-first, partner work, talk time with 'is 0357 a 4-digit number?'; mini-lesson is tutor-led. |
| 8 | Complexity and context | 1 | Pure number puzzles; only a thin 'Mei says' wrapper. |
| 9 | Creativity and problem posing | 0 (1 after rework) | No make-up-your-own task in print (before fix). |
| 10 | Metacognition and reflection | 1 | 'Check' step in each worked example, but children do not record strategy or difficulty. |
| 11 | Pacing flexibility and compacting | 1 | Fixed 90-minute slide sequence; star items for early finishers only. |
| 12 | Extension beyond syllabus, not acceleration | 2 | Place value to 10 000 explored through puzzles; nothing from P4. |
| | **Total** | **16/24** (18/24 after) | |

**Gifted-style strengths**
- Open explore with digit cards (all 4-digit numbers between 4000 and 6000, closest to 5000); any child can start and 'all 24' is a named extension.
- 'List in order and prove you have them all' is a real proof-flavoured habit; Mei's 0357 claim is a good counterexample prompt.

**Gaps**
- No problem posing and no reflection anywhere in the workbook before the fix; Core C1/C2 and workbook Q4 assumed the vocabulary.
- Challenge X4 and X7 repeated Think Harder and workbook items with bigger numbers.

### Lesson 2: Cryptarithm Crackers (Addition and subtraction)

Tier compliance before: **24/29 = 83%** (5 violations). Rubric: **15/24 before, 17/24 after the rework**. Verdict: **partly**.

- **Core, question bank (C1-C6):** ok: C3, C4, C5, C6. **C1 violation**: needs the 'make 4000, then take 1 away' shortcut, which only the lesson teaches. **C2 violation**: subtraction across zeros with no entry route (no number line or count-up).
- **Think Harder, question bank (T1-T8; T1-T4 on the workbook):** ok: T1, T2, T3, T4, T5, T7, T8. **T6 violation**: applies the named 9999 trick directly: practice, not a new setting.
- **Challenge, question bank (X1-X9; X7-X9 on the workbook):** ok: X1, X2, X4, X5, X6, X7, X8, X9. **X3 violation**: two reverse operations only; no puzzle structure or extension.
- **Workbook core pages (W1-W6):** ok: W1, W2, W3, W4, W5. **W6 violation**: three-shape carry puzzle (Think Harder level) on the core page with no star or scaffold.

| # | Rubric criterion | Score | Evidence |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Explore: make a sum with cards 1 to 9; 'finished early': add the digits of the answer (always 18). |
| 2 | Depth over speed | 1 | 6 questions on 2 pages plus Think Harder pages; timed pairs then alone. |
| 3 | Abstraction and generalisation | 2 | 9999 pattern ('why no carrying?'), magic-square opposite pairs and 'digits always add to 18' ask for a rule. |
| 4 | Justification | 2 | Q5b, Q6b, 'how can a puzzle have only one answer?' ask why. |
| 5 | Multiple solution paths | 1 | Notes mention guess and check as an alternative to the column method only once. |
| 6 | Challenge ladder inside the lesson | 1 (2 after rework) | Ladder visible, but C1/C2/T6/X3/W6 broke it (shortcut, formal algorithm, practice, reverse arithmetic, Think Harder puzzle on the core page). |
| 7 | Student-led inquiry and discussion | 1 | Talk moves are planned but 3 'teach before page' slides are tutor-led. |
| 8 | Complexity and context | 1 | Cryptarithms have interacting variables but no real-world or cross-subject link. |
| 9 | Creativity and problem posing | 0 (1 after rework) | None in print before the fix. |
| 10 | Metacognition and reflection | 1 | Worked examples end with a check; no recording by the child. |
| 11 | Pacing flexibility and compacting | 1 | Fixed sequence; 'if time' star item only. |
| 12 | Extension beyond syllabus, not acceleration | 2 | Same grade content explored as puzzles. |
| | **Total** | **15/24** (17/24 after) | |

**Gifted-style strengths**
- Cryptarithms, magic squares and number pyramids are genuine puzzle structures with unique answers; the 9999 pattern asks WHY there is no carrying.
- Explore ends on a conjecture (digit sum of the answer is always 18) that children can test.

**Gaps**
- One taught method (start at the ones); alternatives appear only as a note ('if children prefer guess and check').
- Core items C1, C2 used the lesson's shortcut or the formal algorithm with no way in; X3 was a trivial reverse-operation item.

### Lesson 3: Times Table Treasure (Tables of 6, 7, 8, 9)

Tier compliance before: **24/29 = 83%** (5 violations). Rubric: **17/24 before, 19/24 after the rework**. Verdict: **partly**.

- **Core, question bank (C1-C6):** ok: C1, C2, C4, C5, C6. **C3 violation**: bare 7 x [ ] = 63: pure recall of the table, no skip-counting route.
- **Think Harder, question bank (T1-T8; T1-T4 on the workbook):** ok: T1, T2, T3, T4, T6, T7. **T5 violation**: two single recalled facts (7 x 8, 6 x 9): Core level. **T8 violation**: two recall questions (6 x 8, 7 x 9): Core level.
- **Challenge, question bank (X1-X9; X7-X9 on the workbook):** ok: X1, X2, X3, X5, X7, X8, X9. **X4 violation**: repeat of X2 on the 7 table (last digits again). **X6 violation**: list six products of pairs: no extension.
- **Workbook core pages (W1-W6):** ok: W1, W2, W3, W4, W5, W6.

| # | Rubric criterion | Score | Evidence |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Explore: last-digit circles for the 6s, 4s, 8s; 'finished early': try the 7s. |
| 2 | Depth over speed | 1 | 6 questions plus Think Harder pages; whole page expected in 30 minutes. |
| 3 | Abstraction and generalisation | 2 | 9s digit pattern, last-digit cycles and 'every 6s answer is even because 6 = 3 pairs' are generalisations. |
| 4 | Justification | 2 | Q1b, Q2b, Q5c and 'why is it even?' in talk time. |
| 5 | Multiple solution paths | 2 | Q3 splits 7 x 8 two ways; slides show 'two ways' to use known facts. |
| 6 | Challenge ladder inside the lesson | 1 (2 after rework) | Ladder visible but T5, T8, X4, X6 were recall or repeats and C3 was bare recall. |
| 7 | Student-led inquiry and discussion | 2 | Discovery explore, partner questions; share question compares 6s and 7s. |
| 8 | Complexity and context | 1 | Mostly pure number patterns; arrays and chairs add a little context. |
| 9 | Creativity and problem posing | 0 (1 after rework) | None before the fix. |
| 10 | Metacognition and reflection | 1 | Check in worked examples; no child reflection. |
| 11 | Pacing flexibility and compacting | 1 | Fixed sequence. |
| 12 | Extension beyond syllabus, not acceleration | 2 | Patterns inside the tables, not next year's content. |
| | **Total** | **17/24** (19/24 after) | |

**Gifted-style strengths**
- Last-digit circles turn tables into patterns children can see; 'why is every 6s answer even' asks for an explanation, not a fact.
- Several 'use last digits only' items generalise (9^4, 7^8) rather than calculate.

**Gaps**
- Core C3 was bare recall; two of the Think Harder items (T5, T8) and X6 were recall-level, so the ladder was flat in the middle.
- No posing; the 'make a riddle' idea exists only implicitly.

### Lesson 4: Model Makers (Word problems (bar models))

Tier compliance before: **22/30 = 73%** (8 violations). Rubric: **16/24 before, 18/24 after the rework**. Verdict: **partly**.

- **Core, question bank (C1-C6):** ok: C2, C3, C4, C5, C6. **C1 violation**: asks for a 'part-whole model' without saying what that is.
- **Think Harder, question bank (T1-T9; T1-T4 on the workbook):** ok: T1, T2, T3, T4, T5, T6, T7, T8, T9.
- **Challenge, question bank (X1-X9; X7-X9 on the workbook):** ok: X3, X5, X6, X7, X9. **X1 violation**: one before-and-after model, same structure as T7. **X2 violation**: one 'take away the extra' step, same as T3 and T8. **X4 violation**: same structure as T2 and T7 with '4 times'. **X8 violation**: the 'pair' trick is T4 (sum and difference): one step.
- **Workbook core pages (W1-W6):** ok: W1, W2, W6. **W3 violation**: 'units' used with no explanation outside the picture. **W4 violation**: needs the total-and-difference model; no entry route or hint. **W5 violation**: equalising (give half the difference) is a Think Harder idea with no guess-and-check route.

| # | Rubric criterion | Score | Evidence |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Cube towers (20 cubes, 4 more / 3 times) then bars; any child can start. |
| 2 | Depth over speed | 1 | 6 questions with models; drawing slows the pace usefully but the page is still the goal. |
| 3 | Abstraction and generalisation | 2 | 'The difference stays the same' and 'give half the difference' are general statements to explain. |
| 4 | Justification | 2 | Q5b (Ravi's mistake), Q6c, 'how can a model check your answer?'. |
| 5 | Multiple solution paths | 1 | One taught model; guess and check appears only as a hint ladder item. |
| 6 | Challenge ladder inside the lesson | 1 (2 after rework) | Ladder visible, but C1, X1, X2, X4, X8 and W3-W5 were off-tier (shared with T level or no entry). |
| 7 | Student-led inquiry and discussion | 1 | Towers and talk time give children the first word; mini-lesson is a model demonstration. |
| 8 | Complexity and context | 1 | Contexts are thin (stickers, beads, money). |
| 9 | Creativity and problem posing | 1 (2 after rework) | Extension note 'write your own before-and-after story' (not printed). |
| 10 | Metacognition and reflection | 1 | 'Check' step in each example; no reflection. |
| 11 | Pacing flexibility and compacting | 1 | Fixed sequence. |
| 12 | Extension beyond syllabus, not acceleration | 2 | Standard bar-model heuristics at P3 level. |
| | **Total** | **16/24** (18/24 after) | |

**Gifted-style strengths**
- Cube towers first, bars second: concrete to pictorial before the heuristic; 'the difference stays the same' is a genuine invariant to explain.
- Ladder of problem types (part-whole, comparison, units, total-and-difference, give-to-equalise, same-amount-added) is well sequenced.

**Gaps**
- Contexts are thin (stickers, beads); several Challenge items were Think Harder level, so Challenge was not much harder than Think Harder.
- Worksheet Q4 to Q6 had no way in for a child who has not met the model method.

### Lesson 5: Remainder Riddles (Division)

Tier compliance before: **27/32 = 84%** (5 violations). Rubric: **16/24 before, 18/24 after the rework**. Verdict: **partly**.

- **Core, question bank (C1-C6):** ok: C3, C4, C5, C6. **C1 violation**: bare 'work out 35 / 4, write the remainder': notation not explained, no objects. **C2 violation**: same as C1 with 58 / 7.
- **Think Harder, question bank (T1-T8; T1-T4 on the workbook):** ok: T1, T2, T3, T4, T5, T6, T7. **T8 violation**: same as C4/C5 (pens, one more): no new idea.
- **Challenge, question bank (X1-X9; X7-X9 on the workbook):** ok: X1, X2, X4, X5, X6, X7, X9. **X3 violation**: same cycle idea as T6 (50th shape): letters instead of shapes. **X8 violation**: same cycle idea again (Monday + 100 days): one division step.
- **Workbook core pages (W1-W6):** ok: W1, W2, W3, W4, W5, W6.
- **Slide-only Think Harder items (S1-S3):** ok: S1, S2, S3.

| # | Rubric criterion | Score | Evidence |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Explore: 25 counters in groups of 2 to 6, table of leftovers; 'finished early': 49 counters. |
| 2 | Depth over speed | 1 | 6 questions plus Think Harder pages; 'if time' party-table item. |
| 3 | Abstraction and generalisation | 2 | 'Remainder < divisor', the list-and-test method and 'find ALL' ask for rules and completeness. |
| 4 | Justification | 2 | Q1c (Ben's error), Q4b, Q5 and the minibus question ask why. |
| 5 | Multiple solution paths | 1 | Counters or a times-table fact (hints); slides show 'two ways' once. |
| 6 | Challenge ladder inside the lesson | 1 (2 after rework) | Ladder visible, but C1/C2 were bare notation and T8/X3/X8 repeated lower items. |
| 7 | Student-led inquiry and discussion | 2 | Counters, table, partner talk; share question is about the divisor. |
| 8 | Complexity and context | 1 | Packing, buses, seats: thin real-world coating. |
| 9 | Creativity and problem posing | 0 (1 after rework) | None before the fix. |
| 10 | Metacognition and reflection | 1 | Check steps; no reflection. |
| 11 | Pacing flexibility and compacting | 1 | Fixed sequence. |
| 12 | Extension beyond syllabus, not acceleration | 2 | Division with remainders explored through riddles. |
| | **Total** | **16/24** (18/24 after) | |

**Gifted-style strengths**
- Counters explore with a table; 'why can the remainder never be as big as the divisor' is a good generalisation question.
- Find-all items (X6, X7) and the 'what to do with the leftover' contexts make the remainder mean something.

**Gaps**
- Core C1/C2 were bare notation; the cycle idea (T6, X3, X8) appeared three times, so Challenge repeated Think Harder.
- Only the extension prompt mentions making a riddle; nothing in the workbook.

### Lesson 6: Fraction Walls (Fractions)

Tier compliance before: **24/33 = 73%** (9 violations). Rubric: **15/24 before, 17/24 after the rework**. Verdict: **partly**.

- **Core, question bank (C1-C6):** ok: C2, C5. **C1 violation**: bare 1/2 = ?/10: equivalence in symbols, no picture. **C3 violation**: bare 2/9 + 5/9: fraction addition in symbols, no picture. **C4 violation**: bare 1 - 3/8: no picture. **C6 violation**: bare 2/5 = ?/10: symbols only.
- **Think Harder, question bank (T1-T8; T1-T4 on the workbook):** ok: T1, T2, T3, T5, T6, T7, T8. **T4 violation**: writing two equal fractions is one taught step (Core level).
- **Challenge, question bank (X1-X9; X7-X9 on the workbook):** ok: X1, X2, X3, X6, X7, X8. **X4 violation**: one step of related-fraction addition (T2 level). **X5 violation**: workbook Q7 with different end points. **X9 violation**: one comparison and one subtraction (T1 level).
- **Workbook core pages (W1-W7):** ok: W1, W2, W3, W4, W5, W6. **W7 violation**: find-all puzzle (Think Harder level) on the core page with no star or hint.
- **Slide-only Think Harder items (S1-S3):** ok: S1, S2, S3.

| # | Rubric criterion | Score | Evidence |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Explore: fold a fraction wall; test if eighths cover a third; 'finished early': three pieces that make a half. |
| 2 | Depth over speed | 1 | 7 questions on 2 pages: the most items per page in the level. |
| 3 | Abstraction and generalisation | 2 | Q1d (top and bottom multiplied) and Q6 (partners that make one whole) lead to rules. |
| 4 | Justification | 2 | Q1d, Q2, Q3, talk question '1/3 + 1/3 is not 2/6'. |
| 5 | Multiple solution paths | 1 | Slides show the wall and a number line; bar-model route only in notes. |
| 6 | Challenge ladder inside the lesson | 1 (2 after rework) | Ladder visible, but four Core items were bare symbols and T4/X4/X5/X9/W7 were off-tier. |
| 7 | Student-led inquiry and discussion | 1 | Folding and 'why is 1/8 smaller than 1/6' discussion; slides are tutor-led. |
| 8 | Complexity and context | 1 | Fractions of one bar; Ravi's fence and a few word contexts. |
| 9 | Creativity and problem posing | 0 (1 after rework) | None before the fix. |
| 10 | Metacognition and reflection | 1 | Check steps; no reflection. |
| 11 | Pacing flexibility and compacting | 1 | Fixed sequence. |
| 12 | Extension beyond syllabus, not acceleration | 2 | Equivalence, comparing and adding stay inside the P3 limits. |
| | **Total** | **15/24** (17/24 after) | |

**Gifted-style strengths**
- Folding a fraction wall is hands-on and the 'why is 1/8 smaller than 1/6' share question targets the classic misconception.
- Several Challenge items need comparison strategies (use 1/2, same tops) rather than only common denominators.

**Gaps**
- Four of six Core items were bare symbols, so a child who has not met fractions had no picture to work from.
- Challenge X4, X5 and X9 were one step of the taught method; the worksheet page 2 had a Think Harder item (Q7) with no star.

### Lesson 7: Area Architects (Area and perimeter)

Tier compliance before: **22/32 = 69%** (10 violations). Rubric: **17/24 before, 19/24 after the rework**. Verdict: **partly**.

- **Core, question bank (C1-C6):** ok: C6. **C1 violation**: 'perimeter' used as a bare word; no definition or picture. **C2 violation**: 'area' in cm2 as a bare word; no covering picture. **C3 violation**: 'perimeter' as a bare word. **C4 violation**: 'area' and 'perimeter' as bare words. **C5 violation**: 'area' and 'perimeter' as bare words.
- **Think Harder, question bank (T1-T8; T1-T4 on the workbook):** ok: T1, T2, T3, T4, T5, T6, T7, T8.
- **Challenge, question bank (X1-X9; X7-X9 on the workbook):** ok: X2, X3, X4, X8, X9. **X1 violation**: repeats workbook Q2 (18 m of fence) with 24 cm. **X5 violation**: repeats the slide Stretch 3 and T8 (draw figures with a given perimeter). **X6 violation**: area 36, length 4 times breadth: one guess-and-check step (T level). **X7 violation**: repeat of X2 with 3 squares in a row.
- **Workbook core pages (W1-W6):** ok: W1, W2, W3, W5, W6. **W4 violation**: missing sides then area and perimeter of an L: no entry route or hint.
- **Slide-only Think Harder items (S1-S3):** ok: S1, S2, S3.

| # | Rubric criterion | Score | Evidence |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Explore: all rectangles from 12 squares; 'finished early': perimeter 20 from 12 squares? |
| 2 | Depth over speed | 1 | 6 questions plus Think Harder pages. |
| 3 | Abstraction and generalisation | 2 | 'Same perimeter, different area', 'push the steps out' and the cut-corner items are general. |
| 4 | Justification | 2 | Q5c, Q6c, share question ('must they have the same area?'). |
| 5 | Multiple solution paths | 2 | Q4 key shows two ways (split into rectangles or push out); slides show 'two ways'. |
| 6 | Challenge ladder inside the lesson | 1 (2 after rework) | Ladder visible, but all five Core items used bare words, X1/X5/X6/X7 were repeats and W4 had no way in. |
| 7 | Student-led inquiry and discussion | 2 | Squares and fence explore, talk time on 'does pushing out always work?'. |
| 8 | Complexity and context | 1 | Gardens and fences: thin real-world coating. |
| 9 | Creativity and problem posing | 0 (1 after rework) | None before the fix. |
| 10 | Metacognition and reflection | 1 | Check steps; no reflection. |
| 11 | Pacing flexibility and compacting | 1 | Fixed sequence. |
| 12 | Extension beyond syllabus, not acceleration | 2 | Grade content with new ideas (invariants). |
| | **Total** | **17/24** (19/24 after) | |

**Gifted-style strengths**
- Explore (every rectangle from 12 squares) leads to 'same perimeter, different area' as a discovery; Q6 asks what happens to the perimeter when a square is added.
- 'Push out the steps' and cut-out-corner items give a reason why a perimeter stays the same.

**Gaps**
- Every Core item used 'area' and 'perimeter' as bare words; Challenge X1, X5, X6, X7 repeated the worksheet or Think Harder.
- The best idea (same perimeter, different area) is never asked as a 'does it always work' generalisation in the printed pages.

### Lesson 8: Angle and Line Detectives (Angles, perpendicular and parallel lines)

Tier compliance before: **20/32 = 62%** (12 violations). Rubric: **14/24 before, 16/24 after the rework**. Verdict: **partly**.

- **Core, question bank (C1-C6):** ok: C6. **C1 violation**: 'right angle' used with no definition. **C2 violation**: 'right angle' used with no definition. **C3 violation**: 'right angle' used with no definition. **C4 violation**: 'parallel' used with no definition. **C5 violation**: 'right angle' used with no definition.
- **Think Harder, question bank (T1-T8; T1-T4 on the workbook):** ok: T1, T2, T4, T5, T6, T7. **T3 violation**: 3 and 9 o'clock repeats C2: Core level. **T8 violation**: pairs in a rectangle repeat T1 and T4.
- **Challenge, question bank (X1-X9; X7-X9 on the workbook):** ok: X1, X3, X6, X7, X8, X9. **X2 violation**: quarter turns of the minute hand: Core level. **X4 violation**: letter F repeats T6 (letter E). **X5 violation**: list the pairs in E repeats worksheet Q4(b).
- **Workbook core pages (W1-W6):** ok: W1, W2, W3, W5, W6. **W4 violation**: parallel and perpendicular used on the page before they are defined.
- **Slide-only Think Harder items (S1-S3):** ok: S1, S2. **S3 violation**: the 5-line fan repeats worksheet Q3(a).

| # | Rubric criterion | Score | Evidence |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Explore: fold a right-angle checker and hunt for angles. |
| 2 | Depth over speed | 1 | 6 questions plus Think Harder pages. |
| 3 | Abstraction and generalisation | 1 | The 5 + 4 + 3 + 2 + 1 angle count gives a pattern; little else is generalised. |
| 4 | Justification | 1 | Q4b and the 'longer arms' share question; few 'why' prompts on the pages. |
| 5 | Multiple solution paths | 1 | One taught way per question. |
| 6 | Challenge ladder inside the lesson | 1 (2 after rework) | Ladder visible, but five Core items, T3, T8, S3, X2, X4, X5 and W4 were off-tier. |
| 7 | Student-led inquiry and discussion | 2 | Folding hunt and 'is a longer arm a bigger angle?' discussion. |
| 8 | Complexity and context | 1 | Letters, windows, clocks: thin context. |
| 9 | Creativity and problem posing | 0 (1 after rework) | None before the fix. |
| 10 | Metacognition and reflection | 1 | Check steps; no reflection. |
| 11 | Pacing flexibility and compacting | 1 | Fixed sequence. |
| 12 | Extension beyond syllabus, not acceleration | 2 | Grade content (no protractor). |
| | **Total** | **14/24** (16/24 after) | |

**Gifted-style strengths**
- Hands-on right-angle checker; counting angles by a pattern (5+4+3+2+1) and the 'is a bigger arm a bigger angle' share question are strong.
- X6 and X9 are real conjecture tasks (can a 6-sided shape have 6 right angles?).

**Gaps**
- Vocabulary (right angle, parallel, perpendicular) used before it is defined on the page; Think Harder T3, T8 and Challenge X2, X4, X5 repeated lower tiers or the worksheet.
- Lowest rubric total of the level: mostly counting and drawing; few 'why' prompts.

### Lesson 9: Measure and Money Masters (Length, mass, volume, money, time)

Tier compliance before: **25/30 = 83%** (5 violations). Rubric: **15/24 before, 17/24 after the rework**. Verdict: **partly**.

- **Core, question bank (C1-C6):** ok: C4, C6. **C1 violation**: bare 2 m 45 cm = ___ cm with no unit relation given. **C2 violation**: bare 3060 g = ___ kg ___ g with no unit relation given. **C3 violation**: compound-unit subtraction with no relation or hint. **C5 violation**: 24-hour time with no rule given.
- **Think Harder, question bank (T1-T9; T1-T4 on the workbook):** ok: T1, T2, T3, T4, T5, T6, T7, T8, T9.
- **Challenge, question bank (X1-X9; X7-X9 on the workbook):** ok: X1, X2, X4, X5, X6, X7, X8, X9. **X3 violation**: two-step money problem but only one idea (T level).
- **Workbook core pages (W1-W6):** ok: W1, W2, W3, W4, W5, W6.

| # | Rubric criterion | Score | Evidence |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Party planner ($20, many answers, 'can you spend EXACTLY $20?'). |
| 2 | Depth over speed | 1 | Worksheet already trimmed to 12 core parts + 3 'if time' parts, but still one page of conversions and times. |
| 3 | Abstraction and generalisation | 1 | Units trick 1 and trick 2 are methods more than generalisations; no 'does it always work?' prompts. |
| 4 | Justification | 2 | Q2b and Q4b ask for an explanation; the rest is calculation. |
| 5 | Multiple solution paths | 1 | Hints 'change to cents, or add dollars first'; timeline vs 24-hour arithmetic. |
| 6 | Challenge ladder inside the lesson | 1 (2 after rework) | Ladder visible, but four Core items had no unit relation or rule printed and X3 was one idea. |
| 7 | Student-led inquiry and discussion | 1 | Planner and talk questions; tutor-led conversions. |
| 8 | Complexity and context | 2 | Budgets, timetables and a clock puzzle: several interacting variables. |
| 9 | Creativity and problem posing | 1 (2 after rework) | Extension note 'plan a real outing' (not printed). |
| 10 | Metacognition and reflection | 1 | Check steps; no reflection. |
| 11 | Pacing flexibility and compacting | 1 | Fixed sequence. |
| 12 | Extension beyond syllabus, not acceleration | 1 | Mostly syllabus content in context, little beyond it. |
| | **Total** | **15/24** (17/24 after) | |

**Gifted-style strengths**
- The party planner explore ($20, 250 ml each, 'can you spend EXACTLY $20?') is the richest open task in the level: several variables, many answers.
- Ben's '1 kg 30 g = 130 g' and Siti's '17:00 is 7 p.m.' are good error-analysis prompts; the clock-fast and weighing puzzles in Challenge are real reasoning.

**Gaps**
- Core conversions had no unit relation printed with them; the lesson is mostly syllabus practice in context, so extension beyond the syllabus is the weakest in the level.
- Only one open, many-answer task (the planner); the rest are single-answer calculations.

### Lesson 10: Challenge Day (Mixed: bar graphs, logic)

Tier compliance before: **24/29 = 83%** (5 violations). Rubric: **16/24 before, 18/24 after the rework**. Verdict: **partly**.

- **Core, question bank (C1-C6):** ok: C1, C2, C3, C4, C5, C6.
- **Think Harder, question bank (T1-T8; T1-T4 on the workbook):** ok: T2, T3, T4, T5, T6, T7, T8. **T1 violation**: queue count repeats workbook Q3(a).
- **Challenge, question bank (X1-X9; X7-X9 on the workbook):** ok: X2, X3, X7, X8, X9. **X1 violation**: bar-model chain of three: Lesson 4 Think Harder level. **X4 violation**: list nine 2-digit numbers: a trivial list. **X5 violation**: same 'take away the extras' bar-model idea as X1 and X9. **X6 violation**: coin puzzle repeats Lesson 9 T5 (guess and check).
- **Workbook core pages (W1-W6):** ok: W1, W2, W3, W4, W5, W6.

| # | Rubric criterion | Score | Evidence |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Two stations with 'how did you START?'; 'finished early': make a puzzle card. |
| 2 | Depth over speed | 1 | Stations of about 7 minutes each; timed. |
| 3 | Abstraction and generalisation | 1 | Queue rule, matchstick table and logic grid support some generalising; less than other lessons. |
| 4 | Justification | 1 | Few 'explain' prompts on the pages; 'which start helped?' in talk. |
| 5 | Multiple solution paths | 2 | Explicitly 'draw it, list it or make a table'; slides contrast starts. |
| 6 | Challenge ladder inside the lesson | 1 (2 after rework) | Ladder visible, but T1, X1, X4, X5, X6 were repeats. |
| 7 | Student-led inquiry and discussion | 2 | Stations and 'teach a puzzle to the group' share. |
| 8 | Complexity and context | 1 | Mixed topics, but each station is separate. |
| 9 | Creativity and problem posing | 1 (2 after rework) | Extension note 'write your own logic puzzle' (not printed). |
| 10 | Metacognition and reflection | 1 | 'Which start helped you most?' is the only reflection in the level. |
| 11 | Pacing flexibility and compacting | 1 | Fixed sequence. |
| 12 | Extension beyond syllabus, not acceleration | 2 | All inside P3 content. |
| | **Total** | **16/24** (18/24 after) | |

**Gifted-style strengths**
- Stations and a 'how did you START?' routine teach heuristics (draw it, list it, make a table, logic grid) rather than topics.
- X2, X3, X7 (squares of any size, handshakes, the truth-teller) are classic gifted-style problems; the extension asks children to write a logic puzzle.

**Gaps**
- Core is fine, but five Think Harder or Challenge items repeated a worksheet or another lesson's idea; no explicit reflection beyond the 'which start helped?' talk question.
- Little cross-topic complexity: stations are separate rather than combined.

## 5. Level-wide notes

- **Core vs worksheet.** The worksheet pages are practice after a "teach before the page" slide, so they are closer to Core than to Think Harder. Where a worksheet question still needs the lesson's method (L1 Q4, L4 Q3-Q5, L7 Q4, L8 Q4) it was counted as a violation and given a hint or a definition rather than rewritten, to protect the page counts.
- **Star items.** The "if time" parts (L1 Q5b and Q6, L3 Q6, L5 Q6, L7 Q6, L8 Q5c, L9 Q3b and Q6) are Think Harder level by design; they are counted as compliant because they are optional and labelled. L2 Q6 and L6 Q7 were unlabelled and counted as violations.
- **Inclusion check (research note).** Not assessed: the lessons do not say how a child with reduced writing or extra-time needs could show the reasoning (a gap against the 2e suggestion in the research note).
- **Not assessed.** Whether the 90-minute plan can in fact be delivered with the longer Core items; the Question Bank PDF grew from 21 to 28 pages because Core items and posing prompts are longer.
