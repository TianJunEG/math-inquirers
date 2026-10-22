# Two 101 word-problem workbooks (Grade 1 and Grade 2): what they test and how Levels 1 and 2 prepare for them

Analysis only. No lesson file or term plan was changed. The workbooks are commercial and copyrighted, so no problem text is reproduced here: a problem is referred to by book and question number (G1-Q23 is Book 1, Question 23) and by a short skill tag. Original practice problems with the same structures are in `docs/books/word_problems_g1_g2_original_draft.md`. My per-question tags, my own answer check and a few reading notes are in the git-ignored `docs/books/private_word_problems_notes.md`.

## 0. Short findings

- **Both books are school-style practice, not contest preparation.** Their problems are built from the same few structures (join, compare, take parts from a whole, change, equal groups, sharing, money) stacked two to five steps deep. Almost nothing needs a topic the school syllabus has not taught. The challenge is reading the story and choosing the order of steps.
- **Book 1 (Grade 1, 101 problems) stays inside Primary 1 numbers.** Everything is within 100. Only 3 problems go past the P1 outcomes (G1-Q32, Q90, Q95, all a larger division or product). 19 of 101 are one-step; the other 82 need two or more steps. 23 are money stories. About 36 use multiplication or division.
- **Book 2 (Grade 2, 101 problems) stays inside Primary 2 numbers except for the 6 to 9 tables.** Numbers stay under 1000 (largest 867). 9 problems go past P2: eight need a fact from the 6, 7, 8 or 9 tables (G2-Q18, 42, 49, 54, 64, 85, 86, 101) and one uses a fraction with denominator 13 (G2-Q62). Only G2-Q5 is a one-step problem. About 60 of 101 need three or more operations. 31 are money problems.
- **The two books teach different methods.** Book 1's printed solutions (19 of 41 solution pages read) use pictures, counting on and back along a number line, number bonds (make ten, split into tens and ones), repeated addition and a drawn check. They did not show a bar model on any page I read, although the cover and preface advertise bar models (as an online download that is not in the file). Book 2's solutions (25 of 40 pages read) draw a bar model at Step 1 for most problems and use column addition and subtraction with regrouping, plus a guess-and-check table (G2-Q45) and a table for a growing pattern (G2-Q98).
- **Level 1 is prepared for almost every type, mostly in Term 2 and Term 3 of the term plan, not in the holiday course.** The one real gap is practice, not content: no lesson works through multi-step stories within 100 as such. 31 of 101 problems are "take several parts from a whole", "group totals, then compare" or change stories (section 5). Smaller gaps: reading traps (who is in the group), and price or size of one from a group.
- **Level 2 is prepared for almost every type** (T1.3, T1.5, T2.4, T3.3, T3.7). The gaps are the length of the chains (about 60 problems need three or more operations and the plan stops at two-step), unit price or unit amount, and corner and queue counting. Three types the book treats as ordinary school problems sit only in Go further in our plan: sum and difference, "times as many" with a total, and transfers.
- **Overlap with the SASMO gaps is small.** Neither book would help a child practise any of the Grade 2 gaps (changing-step sequences, pairing sums, calendar, visual perception, worst case, constraint grids), and for Grade 1 it helps only two-digit arithmetic and multiplication facts. It practises the types Levels 1 and 2 already prepare well: bar-model stories, working backwards, money and equal groups. Section 7 gives the counts.
- **Verdict for the owner:** these books are good home practice for what Levels 1 and 2 already teach, and a good source of the reading-and-structure habit, but they do not close any SASMO gap. Use the original drafts for practice and do not copy from the books.

## 1. What was analysed, and how far to trust it

- Two scanned PDFs of Singapore Asia Publishers' "101 Must-Know Challenging Maths Word Problems", Book 1 (81 PDF pages) and Book 2 (80 PDF pages), "New Edition 2019". Each has a cover, preface, contents, 101 questions on 34 printed pages (with blank working space and an answer line), and step-by-step solutions on 41 printed pages (S1 to S41). The pages are images with no text layer, so I read each page as an image.
- I read **every question page** of both books. I read **19 of the 41 solution pages of Book 1** (S1 to S4, S10 to S13, S22, S23, S25, S26, S32 to S34, S38 to S41) and **25 of the 40 solution pages of Book 2** (S1, S8 to S11, S16 to S30, S37 to S41). The inventory of methods in sections 2.4 and 3.4 rests on those pages. An unread page could use a method I did not see. The online downloads that the books mention (bar-model introductions) are not in the files.
- I worked every problem myself and compared my answer with the printed solution on every solution page I read; all agreed. I did not compare the answers on the unread pages. My answers are in the private notes.
- Categories are my single-coder judgement. Each problem is filed under one main structure, so counts are indicative. "Steps" means the number of arithmetic operations on the shortest route, my estimate. The books list their own sections by operation (contents in sections 2.1 and 3.1); the structure tables are mine.
- The books say they follow the current Primary Mathematics syllabus and, in the preface, to collect problems that students often meet in tests and examinations. I have not checked that claim against any school paper. I flag content past the MOE level using `docs/moe/syllabus_by_level.md` (2021 syllabus, PDF pages as printed there).
- Level 1 plan and Level 2 plan were read as they stood in the working tree. The Level 2 plan was being revised by another agent at the same time, so its lesson codes (T1.5 and so on) may move. Nothing here edits either plan.
- Tiers: S = Start here, T = Think harder, G = Go further, as in the term plans.

## 2. Book 1 (Grade 1)

### 2.1 How the book is organised (its own contents)

| Questions | Learning objective in the contents | Count |
|---|---|---|
| 1-14 | Addition within 100 | 14 |
| 15-26 | Subtraction within 100 | 12 |
| 27-30 | Multiplication | 4 |
| 31-34 | Division | 4 |
| 35-70 | Addition and subtraction within 100 | 36 |
| 71-76 | Addition and multiplication within 100 | 6 |
| 77-80 | Addition and division within 100 | 4 |
| 81-90 | Subtraction and multiplication within 100 | 10 |
| 91-94 | Subtraction and division within 100 | 4 |
| 95-97 | Multiplication and division within 100 | 3 |
| 98-101 | Two-part word problems (two operations) | 4 |

The sections are by operation, not by story structure, so one section holds several structures (the 36 problems of 35-70 hold most of the structures below).

### 2.2 Catalogue by structure (101 problems)

| Type (structure) | Count | Questions | Note |
|---|---|---|---|
| Join: total of 2 to 3 groups | 5 | 1, 4, 9-11 | Largest sums use three addends. |
| Compare (more/fewer than), find the other, then total | 8 | 2, 6, 12, 13, 46, 55, 67, 68 | Q12 reverses the wording ("fewer than" the other child). |
| Compare chain of three, or compare plus a given total | 4 | 8, 48, 65, 66 |  |
| One-step take away, gap or change | 5 | 15, 18, 24-26 |  |
| Part-whole: take several parts from one total, find the last | 15 | 17, 35-37, 44, 47, 49, 50, 52, 54, 56, 59, 62-64 | The commonest type: 15% of the book. |
| Combine two groups, then take some away | 4 | 40, 45, 51, 61 |  |
| Group totals, then compare (how many more) | 8 | 20, 21, 23, 38, 39, 43, 57, 60 |  |
| Change story, start and end (forward) | 3 | 53, 69, 70 |  |
| Change story, hidden start (backwards) | 5 | 3, 5, 7, 41, 58 |  |
| Abstract number puzzles | 4 | 16, 19, 22, 42 | Words only ("a number", "the bigger number"). |
| Equal groups, one step (x) | 4 | 27-30 |  |
| Sharing or grouping, one step (division) | 4 | 31-34 |  |
| Equal groups plus add or take away | 14 | 71-76, 81, 82, 84-89 | Second commonest. |
| Unit from a group (price of one, size of one), then more | 6 | 14, 80, 83, 90, 96, 97 | Q14 first finds a price by taking away. |
| Share or group plus another step | 6 | 77-79, 91, 92, 95 | Q77 counts the sharer as well as 2 friends. |
| Make equal by a transfer | 2 | 93, 94 | Half of the gap. |
| Two-part questions (a)(b) | 4 | 98-101 | Part (b) reuses part (a). |

Money is a setting, not a structure: 23 problems are money stories (G1-Q13, 14, 23-26, 34, 59, 62, 64-67, 80, 83, 85, 86, 90, 91, 95, 97, 99, 100). Cents appear only in Q66, Q90 and Q95; the rest are whole dollars.

### 2.3 The difficulty ladder the book uses

- **Numbers.** Everything is within 100. Products stay within 40 except G1-Q90 (3 groups of 30 cents), and quotients within 20 except G1-Q32 (32 divided by 4) and Q95 (40 cents divided into 20-cent coins).
- **Operations.** One operation first (add, then subtract, then multiply, then divide: Q1 to Q34), then mixes. Inside the 36-problem add and subtract block the stories lengthen from "a total minus two parts" (Q35 to Q37) to three-event money chains (Q64 to Q66). The × and ÷ mixes (Q71 to Q97) put one group step before or after one add or subtract step.
- **Steps.** 19 problems are one-step (Q1, Q7, Q15 to Q19, Q22, Q24 to Q34); 82 take two or more; about 15 take three (for example Q8, Q48, Q64, Q75, Q91). The last four problems are two-part questions in which part (b) uses part (a).
- **What makes a problem "challenging" here is the story, not the number.** Moves that recur: a hidden quantity that must be found first (the other person's amount in a compare story; the group of people in a sharing story); "the rest" or "at first" (a hidden start or part); two comparisons in a row (Q8, Q65, Q66); a unit cost found before a total (Q80, Q83, Q90).
- **Reading traps** (each is a likely wrong answer): Q12 gives a "fewer than" sentence whose answer is the other child's larger number; Q14 gives the larger price and asks for the smaller; Q52 gives the same amount to each of two friends, which is two removals; Q77 shares with 2 friends, so three people share; Q88 gives away 6 boxes, not 6 tarts. Vocabulary: "a dozen" (Q33, explained in the solution), "a week" (Q28), "such" (Q14, Q96).

### 2.4 Heuristics and models taught (from the 19 solution pages read)

- **Draw it and count** (Q1, Q2, Q4, Q5, Q27 to Q36): a picture of the objects, circled in groups, then counted. This is the first of two "Method" lines for the early problems.
- **Number bonds.** Almost every addition and subtraction is written as a bond tree: split one number into tens and ones, make a ten, then add the tens. This is the make-a-ten and split-into-tens-and-ones method taught in Level 1 Lessons 10, 13 and 14.
- **Counting on and counting back** with arrows along a number line (+10, +10, +1 ...), for adding or subtracting a 2-digit number or a number near a ten (Q2, Q3, Q62, Q66).
- **Repeated addition** for multiplication (Q27 to Q30, Q81 to Q86), and grouping a drawn set into equal groups for division (Q31 to Q34, Q93 to Q96). Division is also checked as "2 groups of 3 = 6" (Q93, Q94).
- **One operation per step.** Every solution is cut into Step 1, Step 2 and so on, each naming its operation. This is the book's real heuristic: split the story into one-operation steps.
- **Check with a diagram** (Q93 step 3) and **draw a table** (Q28, the seven days of the week).
- No bar model appeared on any Book 1 solution page I read. The cover says "solve mathematics problems using bar models" and the contents mark three blocks (Q1 to Q14, Q15 to Q26, Q95 to Q97) with an online-resource icon (the page of Q15 offers a "comparison model" download), but the printed solutions use pictures and bonds. The 2021 syllabus does not name bar models (`syllabus_by_level.md`).

## 3. Book 2 (Grade 2)

### 3.1 How the book is organised (its own contents)

| Questions | Learning objective in the contents | Count |
|---|---|---|
| 1-3 | Addition within 1000 | 3 |
| 4-6 | Subtraction within 1000 | 3 |
| 7-8 | Multiplication and division of 2 and 3 | 2 |
| 9-53 | Word problems (2 or more operations) | 45 |
| 54-55 | Length | 2 |
| 56-59 | Mass | 4 |
| 60-62 | Fractions | 3 |
| 63-64 | Volume | 2 |
| 65-95 | Money | 31 |
| 96-98 | Time | 3 |
| 99-101 | Two-part word problems | 3 |

The contents label is looser than the content. "Multiplication and division of 2 and 3" is followed at once by problems that use 4, 5, 8, 9 and 10 (the P2 syllabus includes 2, 3, 4, 5 and 10). "Time" (Q96 to Q98) contains two age problems and a growing-pattern problem; there is no clock-reading problem in the book (the only time problem is the hours from 1 pm to 10 pm in Q86, filed under Money). Length, mass and volume problems (Q54 to Q59, Q63, Q64) are the same bar-model structures in a measure setting.

### 3.2 Catalogue by structure (101 problems)

| Type (structure) | Count | Questions | Note |
|---|---|---|---|
| Change story, one hidden amount, 3-digit | 13 | 2, 4, 6, 11, 27, 29, 32, 33, 35, 36, 68, 74, 78 | Start, middle or end is hidden; 6 of 13 use a 3-digit number. |
| Part-whole, join or missing part (3-digit) | 5 | 3, 5, 15, 16, 34 |  |
| Compare, find the other, then total or remainder | 6 | 1, 14, 22, 23, 31, 59 |  |
| Compare chain of three (total or one end) | 6 | 19, 24, 37, 43, 55, 63 |  |
| Sum and difference; 'times as many' with a total | 5 | 7, 39, 53, 81, 95 |  |
| Make equal by a transfer | 3 | 28, 44, 50 |  |
| Equal groups, one or two kinds, join or compare | 9 | 9, 18, 30, 41, 42, 51, 88, 89, 94 |  |
| Equal groups, then change (x then add or take away) | 12 | 10, 12, 13, 17, 46, 56, 64, 75, 77, 84, 87, 90 |  |
| Share equally plus another step (division) | 12 | 8, 20, 25, 38, 40, 47-49, 52, 57, 58, 92 | Q8 and Q25 count the sharer as well as 2 friends. |
| Money: change in notes | 5 | 70-72, 91, 93 | Change paid in two-dollar notes, often after a five or ten. |
| Unit price or unit amount, then many | 8 | 54, 65, 67, 69, 80, 83, 85, 86 | Q86 is an hourly rate (1 pm to 10 pm). |
| Exchange: 'as much as' equivalences | 2 | 73, 79 | Q73, Q79; Q101 is the same idea with a total. |
| Compare, then multiply (per-item difference) | 3 | 66, 76, 82 |  |
| Fractions of a whole from pieces | 3 | 60-62 | Q62 has denominator 13. |
| Corners and fence-post (square field) | 1 | 26 |  |
| Bundle with a free item | 1 | 21 |  |
| Guess and check with two kinds | 1 | 45 | The only problem solved with a named table heuristic. |
| Ages (gap stays the same) | 2 | 96, 97 | Only two, both direct. |
| Growing daily amount until a total | 1 | 98 |  |
| Two-part questions (a)(b) | 3 | 99-101 |  |

Steps and size: only Q5 is one-step. By my count about 60 of 101 need three or more operations and about 20 need four or more (for example Q19, Q31, Q41, Q43, Q76, Q98, Q101). About 26 problems use a number of 100 or more in the text. Money (the book's own section) is 31 problems, all whole dollars; no decimal money appears.

### 3.3 The difficulty ladder the book uses

- **Numbers.** Add and subtract to 3 digits first (Q1 to Q6), then the later problems mix 2-digit and 3-digit numbers (about 26 of the 101 have a number of 100 or more); the largest is 867 (Q34). Products come from the 2, 3, 4, 5 and 10 tables except the eight listed in section 6.
- **Structure.** The book opens with join, compare and a hidden start in a single story, then moves in Q9 to Q53 to two and three structures chained (a compare, then a total, then a sale). From Q54 the same structures appear in measure settings. Money (Q65 to Q95) is the longest block: it starts with unit and group prices (Q65 to Q69), then change in notes (Q70 to Q72), then several items on one bill (Q73 to Q90), and finishes with change, a shared cost and a sum-and-difference gift (Q91 to Q95). The three two-part questions close the book.
- **What rises** is the number of steps (2 to 5), the size of the numbers (to 3 digits) and the hidden link: "as much as" equivalences (Q73, Q79), "twice" and "thrice" with a total (Q39, Q53), a transfer plus a given total (Q44, Q50), a group price "N for $M" (Q65) and a discount on every item (Q66).
- **Reading traps**: sharing "with 2 friends" (3 people) in Q8 and Q25; the child in the middle of a queue (Q89); a free item for every set of bags (Q21); a corner tree counted once (Q26); a sale price that applies to each of two items (Q66); Q37 gives the larger of two days.

### 3.4 Heuristics and models taught (from the 25 solution pages read)

- **Draw a model** is the first or second step in 46 of the 58 problems whose solutions I read (Q1, Q2, Q23 to Q25, Q27 to Q31, Q40, Q43, Q44, Q47 to Q50, Q52 to Q63, Q65, Q66, Q68 to Q70, Q72 to Q76, Q93 to Q97, Q99, Q101): a bar model with the known parts labelled and a bracket and a question mark on the unknown. The bar forms used are part-whole (one bar split into labelled parts), comparison (two bars, the difference marked), "times as many" (one bar cut into equal units, Q53), equal-unit bars for groups and prices (Q69, Q70, Q94) and before-and-after bars for a transfer (Q28, Q44).
- **Guess and check with a table** (Q45, apple and chocolate pies): start with equal numbers, compute the total each time, adjust.
- **Make a table of a growing pattern** (Q98) and **draw a diagram** for space (Q26, labelled "spatial visualisation"; Q71 draws the notes).
- **Methods for arithmetic**: column addition and subtraction with and without regrouping are shown for every 2-digit or 3-digit calculation (Q1 to Q6 and after); number bonds and counting on or back remain for smaller numbers (Q27, Q66, Q68); "mental calculation" is the label for easy facts; division is written as "4 x 7 = 28" in a thought bubble beside "28 / 7 = 4".
- **One operation per step**, labelled Step 1, Step 2 and so on, as in Book 1.
- Also noticed: Book 2 solutions never name "work backwards" or "guess and check" except in Q45; the backwards stories (Q2, Q12, Q27, Q29, Q35) are drawn as a bar with the end value given, and undone from the end.

## 4. How the two books fit together

- Book 1 teaches the structures with pictures and number bonds, mostly one structure per problem. Book 2 returns to the same structures with larger numbers, more links in each chain and a bar model.
- Several Book 2 types are Book 1 types with one more link: a compare problem with a total (Book 1 Q8, Q48, Q65 and Book 2 Q19, Q24, Q43); a sharing problem with a second division (Book 1 Q77 to Q79 and Book 2 Q8, Q25); a transfer (Book 1 Q93, Q94 and Book 2 Q28, Q44, Q50).
- New in Book 2: "times as many" with a total (Q7, Q39, Q53), sum and difference (Q81, Q95), "as much as" equivalences (Q73, Q79, Q101), fractions of a whole (Q60 to Q62), ages (Q96, Q97), a guess-and-check table (Q45), a growing pattern (Q98), corners and queues (Q26, Q89), and 3-digit arithmetic in every block.

## 5. How Level 1 maps to Book 1

Level 1 sources: the ten holiday lessons (`hp/lessons.js`) and the term plan `docs/terms/level_1_year_plan.md` (plan only, no lessons written). Holiday lessons that matter here: L2 number bonds, L4 patterns, L5 working backwards (more/fewer, mystery number), L6 coin combinations. The holiday course never taught 2-digit adding and taking away, multiplication or division (the term plan says so). The Level 1 term plan adds Lessons 10 to 18 (tens and ones, make-a-ten, take away and count up, bar strips) in Term 2, Lessons 19 to 22 (equal groups, tables, sharing and grouping, times stories) and 25 and 26 (dollars, change, the school shop) in Term 3.

| Type (count) | What Level 1 has | Tier | Verdict |
|---|---|---|---|
| Join 2 or 3 groups (5, plus part of most) | Holiday L2 bonds; Lesson 10 bundles; Lesson 13 make-a-ten (T: add four numbers by finding tens) | S for two numbers, T for three | Prepared. Fluency drill is left to school, as the plan states. |
| One-step take away, gap, change (5), and subtraction inside every story | Lesson 14 (take away, count up) | S | Prepared. |
| Compare, find the other, then total (8) | Holiday L5 (more/fewer, sum and difference); Lesson 17 (S: how many more; T: total and difference) | S; T when the wording is reversed (G1-Q12, Q14) | Prepared. The reversed wording is not named in Lesson 17. |
| Compare chain, or compare with a total (4) | Lesson 17 T and G; Lesson 35 toolbox | T; G with a total | Partly prepared: a chain of three is not named. |
| Part-whole, several parts, find the last (15) | Holiday L2 bonds; Lesson 14. No lesson names "total minus several parts" as a story | S for two parts, T for three | **Gap (small, practice not content)**: the commonest type has no lesson of its own. |
| Combine two groups then take away, and change forward (7) | Lessons 13, 14, 17 | T | Prepared. |
| Group totals, then compare (8) | Lesson 17 T (total and difference given) | T | Partly prepared: "add inside each group, then compare" is not named. |
| Change story, hidden start (5) | Holiday L5 and Lesson 4 (S: one step; T: two steps in the right order) | S for one event, T for two | Well prepared. |
| Abstract number puzzles (4) | Lessons 2, 4, 15 | S, T | Prepared; the words "subtracted from" and "the bigger number" are new. |
| Equal groups and sharing, one step (8) | Lessons 19 to 21 (Term 3); holiday course none | S | Prepared by the plan. |
| Equal groups plus add or take away (14) | Lesson 19, Lesson 22 (T: two-step with a total) | S for one group, T for two kinds, G for a hidden start (G1-Q75) | Prepared. |
| Share or group plus another step (6) | Lessons 21 and 22 | T | Prepared. "Who is in the group" (G1-Q77) is a reading trap the plan does not name. |
| Price or size of one from a group (6) | Lessons 19 to 22 and 26 touch it; none says "find one first" | T | **Gap (small)**: a new move, divide to get one, then multiply. |
| Make equal by a transfer (2) | Lesson 17 Go further ("after giving 3, they are equal") | The book treats it as ordinary: T would fit | Prepared; the plan tier is higher than the book's. |
| Money stories (23 of 101) | Lessons 25, 26; holiday L6 | S, T | Prepared. The plan's money is mostly coin and note puzzles; the book uses money as the setting for the structures above. |
| Two-part questions (4) | None | S | Format only. |

**Real gaps for Level 1 (all small, and all about practice, not new topics):**

1. **Multi-step stories within 100 as such.** 31 of 101 problems are "take several parts from a whole" (15), "group totals, then compare" (8) or change stories (8). Lessons 17 and 35 reach them; no lesson practises reading a story, choosing the first step and writing one operation per step, which is what the book drills.
2. **Reading traps.** Who is in the group, which unit is given (boxes or items), reversed "fewer than". Nothing in the plan names a "read it twice" routine.
3. **Price or size of one from a group** (6 problems).
4. **Speed and accuracy of 2-digit regrouping.** The plan already says school will practise this more than we do.
5. **Vocabulary**: "a dozen", "a week", "such", "in the end".
6. **For a holiday-only child**, most of the book is out of reach: the holiday course has no 2-digit arithmetic, multiplication or division. This is a fact about the holiday course, not a gap in the term plan.

**Beyond the MOE Primary 1 level** (`syllabus_by_level.md`, P1 pp. 31 to 32): only three problems, all in size, not in topic: G1-Q32 (32 divided by 4; P1 division is within 20), G1-Q90 (3 groups of 30; P1 multiplication is within 40) and G1-Q95 (40 divided into 20-cent coins). Model drawing is not named in the syllabus. Everything else (add and subtract within 100, multiplication within 40, money to $100) is P1.

## 6. How Level 2 maps to Book 2

Level 2 sources: the ten holiday lessons (`p2/SPEC.md`, `p2/content/l1.js` to `l10.js`; L2 add and take away within 1000, L3 equal groups, L5 working backwards with before-and-after bars, L6 money, L7 fractions) and the term plan `docs/terms/level_2_year_plan.md` (plan only; revised after the SASMO review). Plan codes such as T3.7 are Term 3 lesson 7.

| Type (count) | What Level 2 has | Tier | Verdict |
|---|---|---|---|
| Change story, one hidden amount, 3-digit (13) | T1.2 (3-digit sums), T1.5 (undo, before-and-after bars), T2.3 (jumps, columns); holiday L2 and L5 | S for one event, T for three-digit numbers or two events | Well prepared. Written 3-digit fluency is taught for understanding (plan, gaps). |
| Part-whole, join or missing part (5) | T2.4 (S: bar for one fact) | S | Prepared. |
| Compare, find the other, then total (6) and compare chain of three (6) | T2.4 (T: more/fewer, two groups); T3.7 (T: compare then total); holiday L5 (three children with extras) | T; G with a total | Prepared. |
| Sum and difference; "times as many" with a total (5) | Holiday L2 (boxes A, B, C from pair totals), holiday L5; T3.7 Go further ("times as many") | G in the plan; the book uses it as ordinary school work | Prepared. **Tier mismatch**: the plan keeps these in Go further. A one-step sum-and-difference card would fit Think harder. |
| Make equal by a transfer (3) | T3.7 Go further (transfers); holiday L5 | G | Prepared. |
| Equal groups, one or two kinds (9); groups then change (12) | T1.3, holiday L3; T1.5; T3.7 | S for one group, T for two kinds or a hidden start | Prepared. |
| Share equally plus another step (12) | T1.3, holiday L3 (sharing with leftovers) and L5 | T | Prepared. "Who is in the group" (G2-Q8, Q25) is not named in the plan. |
| Money: change in notes (5) | T1.6 Market Day (change by counting on; no $20 note); holiday L6 | T; G with two kinds of note | Prepared. |
| Unit price or unit amount, then many (8) | T2.6 fact families; T3.7 money contexts; holiday L3 equal groups. No lesson says "find one first" | T | **Gap (small)**. |
| Exchange: "as much as" (2, plus G2-Q101) | T3.3 Shape Equations (exchange chains, new in the revision) | T | Prepared. |
| Compare, then multiply (3) | T3.7 | T | Prepared. |
| Fractions of a whole from pieces (3) | T1.7, T3.2 (like fractions, add and subtract within one whole) | S, T | Prepared. G2-Q62 is a denominator 13 (P2 goes to 12). |
| Ages (2) | T3.7 T (new) | T | Prepared; the book's two are the easy forms. |
| Guess and check, two kinds (1) | Holiday L3 hens-and-goats table; T1.3 Go further; toolkit card (T2) | The book teaches it to everyone; T | Prepared. |
| Growing amounts until a total (1) | T1.4, T3.1 | T | Prepared. |
| Corners, queues, free items (Q26, Q89, Q21) | Holiday L9 ribbons and rope; no lesson on counting ends or the person themselves | T | **Gap (small)**: the plan lists fence-post contexts as "candidate practice only". |
| Three to five steps in one problem (about 60 of 101 need 3 or more) | T3.7 stops at two-step; T4.9 is two-step | G | **Gap**: the book chains three to five steps with a model; the plan does not. |

**Real gaps for Level 2:**

1. **Longer chains.** About 60 problems need three or more operations and about 20 need four or more. Level 2 teaches models and two-step stories, but nothing asks a child to hold four or five links; the plan's longest chain is T3.7 "two bars, one question".
2. **Unit price or unit amount** (8 problems): a group price "N for $M", or "4 notebooks cost $20, how much for 7?". The plan has equal groups and tables but no "find one first".
3. **Corner, end and "count yourself" problems** (G2-Q26, Q89, and the free-item rule in Q21), a new context of the fence-post idea.
4. **Reading traps** ("with 2 friends" is 3 people; a discount on every item).
5. **Tiers**: sum and difference, "times as many" with a total and transfers are ordinary school work in Book 2 but Go further in our plan. That is a placement choice, not a content gap.
6. **Method mismatch** (not a gap): the book shows the written column method for every calculation; the plan teaches it for understanding and says school will drill it.

**Beyond the MOE Primary 2 level** (`syllabus_by_level.md`, P2 pp. 33 to 34): nine of 101 problems.
- Tables 6 to 9 (P3, p. 35), eight problems: G2-Q18 (9 x 8), Q42 (8 x 6), Q49 (6 x 9), Q54 (28 divided by 7), Q64 (8 x 7), Q85 (32 divided by 8), Q86 (8 x 9), Q101 (14 divided by 7). Level 2 keeps to 2, 3, 4, 5 and 10; these should not be copied into the program.
- A fraction with denominator 13 (G2-Q62); P2 fractions go to denominator 12.
- Within P2: all numbers are under 1000, all money is whole dollars (decimal money is P2 but the book does not use it), mass in g and kg, length in cm and volume in litres.

## 7. Overlap with the SASMO gaps already found

Counts for the contests come from `g1_analysis.md` (4 papers, 100 problems) and `g2_analysis.md` (7 papers, 160 problems); they are not recounted here.

**SASMO Grade 1 gaps (`g1_analysis.md`, section 4)**

| SASMO Grade 1 gap | Does Book 1 or Book 2 help? |
|---|---|
| 1. Place value and digit puzzles (14 of 100) | No problem. The Book 1 solutions use tens-and-ones bonds as a method, which supports the idea but is not a puzzle. |
| 2. Two-digit arithmetic and multi-term sums (13) | Yes, partly. 62 of Book 1's problems use only addition and subtraction within 100, most with regrouping and up to three addends (Q1 to Q26 and Q35 to Q70). It does not teach compensation (38 + 25 = 36 + 27) or four-addend sums. |
| 3. Sequences with changing steps (10) | No. (Book 2 Q98 is a growing amount until a total; it is the only pattern problem.) |
| 4. Visual perception and 3D (14) | No. |
| 5. Time and calendar (7) | No. No clock problem in either book; G1-Q28 (days in a week) and G2-Q86 (hours) are the only time items. |
| 6. Symbol equations and multiplication facts (about 11) | Multiplication facts, yes: about 36 problems in Book 1 use × or ÷ within 40 and most of Book 2's use the 2, 3, 4, 5, 10 tables. Symbol equations, no. Book 2's "as much as" problems (Q73, Q79, Q101) are the nearest. |

By type: the SASMO Grade 1 types that the books practise are bar-model word problems (7 of 100), multiplication and division facts as the main skill (2) and money (1): **10 problems**, or 23 if the 13 computation items are counted as practised by the arithmetic in the books.

**SASMO Grade 2 gaps (`g2_analysis.md`, section 5 and addendum 7.6)**

| SASMO Grade 2 gap or extension | Does Book 1 or Book 2 help? |
|---|---|
| 1. Sequences with a changing rule (8) | No. |
| 2. Pairing sums (7) | No. The solutions add two numbers by making a ten; they never pair a list. |
| 3. Age problems (7) | Slightly. G2-Q96 (an age in 5 years) and Q97 (twice as old, two years ago) are direct forms. Neither is "when I was your age" or a total of two ages some years on. |
| 4. Calendar and day-of-week arithmetic (7) | No. |
| 5. Visual perception, shadows, mirrors (7) | No. |
| 6. Worst case (3) and rate or doing things together (2) | No for worst case. Rate, partly: unit price (G2-Q54, Q65, Q69, Q85) is the same rate idea, but "more helpers, less time" is absent. |
| 7. 3D rotation (1 to 2) and constraint grids (3) | No. |
| Extensions: logic forms (11), counting routes and points, letter-digit sums (5), moving patterns, triangular growth | No. |
| Extension: picture and symbol equations (12) | Partly: "as much as" exchange problems (G2-Q73, Q79, Q101) are the same substitution idea in a shopping story. |
| Extension: ratio and leftover bar models | Partly: "times as many" and "twice" with a total (Q7, Q39, Q53) and sum and difference (Q81, Q95); not the leftover-in-both-shares forms. |

By type, using the Grade 2 type counts (addendum 7.3): bar-model word problems 11, working backwards 3 and money 2 are strongly practised by the books (16 of 160, 10%). Adding the partial overlaps (legs and heads 3, fence-post and positions 7, ages 7) gives 33 of 160 (21%). None of the 7 gaps is closed.

**Reading of this.** The books and the SASMO analyses agree on the types Levels 1 and 2 already prepare well. They share the bar-model structure. The contests' hard parts (patterns, pairing, calendar, perception, worst case, grids) do not appear in a school-style workbook at all. So the books are good practice for the "Start here" and "Think harder" material and for reading stories, and they are not a route into the SASMO gaps.

## 8. Recommendations

- Do not change any Start here line because of these books. Both are inside the MOE levels except in twelve items (three in Book 1, nine in Book 2, listed in sections 5 and 6).
- If the owner wants to answer the small gaps, keep them as optional Think harder or Go further cards: a multi-step story routine for Level 1 beside Lesson 17 (part-whole with several parts, group totals then compare, one operation per step); a "find one first" card for Level 1 Lesson 21 or 22 and Level 2 T3.7; a corners-and-queues card for Level 2 beside the ribbon work; and one longer (four-link) bar-model story at the end of Level 2 Term 3. None of these needs a new lesson.
- Consider tier placement: sum and difference and one-step transfers appear as ordinary school problems in Book 2 (Level 2) and Book 1 (Level 1). Our plans keep them in Go further; a one-step version could sit in Think harder. The owner decides.
- Do not claim these books as SASMO preparation. They are practice for the school problem types that Levels 1 and 2 already teach.
- Original practice for 12 Level 1 types and 15 Level 2 types is in `docs/books/word_problems_g1_g2_original_draft.md` (3 problems per type, answers and solutions checked by script). Check them with a tutor before use, as with the SASMO drafts.
- Do not copy from the books or paste their problems into any workbook, slide or practice page. The structures above are a reading of the books; the words and numbers are theirs.

## 9. Evidence-thin notes

- Two books, one coder. Types with 1 to 3 problems (corners, free item, guess and check, ages, growing pattern) are "occasionally seen", not "tested".
- I read 19 of 41 and 25 of 40 solution pages. Heuristic counts are from those pages.
- Step counts and "about 60", "about 36" are my estimates of the shortest route and are indicative.
- Some problems allow another reading. G1-Q63 asks for two groups in a three-group total (I read it as 80 minus the middle group). G2-Q37 gives the larger of two days (I read it as 146 pages on Sunday and 134 on Monday, so a book of 356 pages). G2-Q89 counts the child in the queue (I read it as 6 children). G2-Q21 "for every 4 bags" is read as 3 free pears for 12 bags. None changes a catalogue count.
- Neither book gives a time limit, a mark scheme or a stated age range, so I make no claim about school exam level beyond the syllabus checks in sections 5 and 6.
