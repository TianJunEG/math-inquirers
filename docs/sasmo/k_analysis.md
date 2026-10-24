# SEAMO Paper K (Kindergarten 1 and 2) sample: what it tests and how the K2 readiness check, the taster and Level 1 prepare for it

Analysis only. No lesson or check files were changed. SEAMO (Southeast Asian Mathematical Olympiad) is a **different organiser from SASMO**: the SASMO Grade 1 and Grade 2 analyses (`g1_analysis.md`, `g2_analysis.md`) are not evidence for this paper, and I have not merged counts. Contest problems are referred to by question number (for example Q7 is 2023 Question 7) and by a short skill tag. The question details, my answers and my confidence are in the git-ignored private file `docs/sasmo/private_solution_notes_k.md`.

## 1. What was analysed, and how far to trust it (evidence is thin)

- The file is a **16-page sample** of a book: "Math Olympiad, International Competition Preparation, Paper K SEAMO 2023-2024 + SEAMO X 2024-2025, Kindergarten 1 and 2" (ages 4 to 6; copyright TCIMO and Singapore Asia Publishers, new edition 2025). Pages 1 to 5 are covers, copyright, contents and a promotional page; page 6 is the paper's front page; **pages 7 to 16 are Questions 1 to 10 of SEAMO Paper K 2023, one question per page.** That is all.
- The contents page lists four papers (SEAMO Paper K 2023 and 2024, SEAMO X Paper K 2024 and 2025), each 16 booklet pages, with 1 to 2 pages of solutions. **None of that was supplied.** If a full paper is 16 pages with a cover, it has about 15 questions, but I have only seen the first 10 and do not know if later questions are written answers (the printed instructions mention a "Section A" with options and a "Section B" with an answer box).
- As printed: every one of the 10 problems is multiple choice with **3 options**; "marks are not deducted for incorrect answers"; no calculator. A guess is right one time in three, so a raw score on this kind of paper overstates what a child can do.
- **Ten problems is far too few to give frequencies.** The counts below describe this sample only. I solved all ten (no solutions were supplied). Seven answers I am confident of; Q1 and Q6 I am fairly sure of; **Q9's rule I could not determine** (see the private file). Categories are my judgement.
- The paper is a competition-preparation paper for 4 to 6 year olds. It is a stretch paper. It is not a statement of what Singapore K2 children usually know.

## 2. Catalogue: all ten problems

| Q | Type | Thinking move | Reading and number load | Tag |
|---|---|---|---|---|
| Q1 | 3D: count the cubes in a picture of a stack, after one worked example (a flat 2 by 2 gives 4) | Notice that a cube must sit on something, so a hidden cube has to be counted | Picture only; numbers 4, 5, 6 | Spatial |
| Q2 | Number sequence where each term is the sum of the two before it | Find the rule from the first terms | Numbers to 9 | Sequence |
| Q3 | Pieces made by straight cuts across a circle, after two worked examples | Count regions; see that a new cut that crosses the old ones makes more pieces | Picture only; numbers 6, 7, 8 | Spatial |
| Q4 | Shapes stand for numbers: two sums, then add the two shapes | Find each shape from its own sum, then add | Numbers to 12; symbols + and = | Equation |
| Q5 | Pictures stand for numbers: two sums that share the same two pictures | Add the two sums (or compare them) to see "one of each" | Numbers to 18; symbols | Equation |
| Q6 | Which circular piece completes a patch of a brick wall | Match colours and positions along the edge of the hole | Picture only | Visual |
| Q7 | Counting in 4s along a chain of coloured circles, find the number in the last circle | Number the circles, find the step, count to the 11th | Numbers to 48 | Sequence |
| Q8 | An unknown number is doubled, 4 is added, 1 is taken away, the answer is 27 | Undo the steps in reverse order | Numbers to 27; the symbol × | Equation |
| Q9 | A sequence of three line-and-symbol figures; choose the next | Find what changes from figure to figure (rule not determined by me) | Picture only | Visual |
| Q10 | A grid of lettered boxes in columns, some filled, one "?" | Find the rule that takes each letter to the next in a column (it wraps round a cycle of seven letters) | Letters A to G | Sequence |

**Frequency by type (this sample only):**

| Type | Problems | Count |
|---|---|---|
| Spatial and visual (cube count, cuts, piece-fitting, figure sequence) | Q1, Q3, Q6, Q9 | 4 |
| Sequences and rules (sum of two before, count in 4s, letter cycle) | Q2, Q7, Q10 | 3 |
| Equations with unknowns (two shape sums, two picture sums, reverse chain) | Q4, Q5, Q8 | 3 |
| Word problems, money, measurement, 2D shape names, counting objects to 20 | none | 0 |

Format notes: Q1, Q3, Q4 and Q5 give a worked example or a first line and ask for the next ("learn the rule from the example"). Four of the ten (Q1, Q3, Q6, Q9) need almost no reading, which suits non-readers. The number range is 1 to 48 and the symbol × appears in Q8.

## 3. Difficulty band as the paper presents it

The sample shows no marks and no sections, so I can only judge by position and content. The first three questions (a cube count, a sequence, cuts) are the most approachable. Q4 and Q5 need two-line reasoning. Q7 needs counting to 44 and finding the 11th circle. Q8 needs ×2 and three steps; **multiplication is Primary 2 in Singapore**, so a typical 5 or 6 year old would meet this only through doubling. Q10 is the hardest in my view: a wrap-around rule on letters.

## 4. How the K2 readiness check, the taster and Level 1 map to it

The K2 readiness check (`k2/k2.py`) is 12 oral items, one child at a time, 24 marks: counting and reading numbers to 20, writing 6, 12, 19, counting on and back, more and less, partitions of 7, small add and take-away stories within 10, a 3-apple story with "how did you work it out", a red-red-blue pattern, 2-4-6, and shape names. It decides who joins a Level 1 (Primary 1) group. The free taster (`taster/gen.py`) is a parent pack of puzzles for Primary 1 children: frog-jump rules (+3, +5, +4, missing terms, two frogs together), making 10, balance sums and a magic triangle. Level 1 lessons: L1 skip counting and rules; L2 number bonds and "="; L3 picture graphs; L4 repeating and growing patterns; L5 working backwards; L6 coins; L7 2D shapes and counting; L8 logic and sorting; L9 length in cubes; L10 mixed. Tiers: Start here, Think harder, Go further.

| Q | K2 check item | Taster | Level 1 lessons and tiers | What would be needed | Verdict |
|---|---|---|---|---|---|
| Q1 cube count | None (item 12 only names shapes) | None | None. L9 uses cubes only as a unit of length | A new strand: build, count hidden cubes, tower plans | **Real gap** |
| Q2 sum of two before | Items 10 and 11 (patterns, +2) | Set 1: constant-step rules | L1 and L4: constant steps only (the Grade 1 analysis found the same gap) | One new idea: "add the two before" | **Extension needed** |
| Q3 pieces from cuts | None | None | L7: fold and cut a square, triangles in a square. No counting of pieces from cuts | Cut paper or draw cookies and count | **Extension needed** |
| Q4 shapes in sums | Items 8 and 9 (add stories) | Set 2: 10 = 6 + __, balance sums | L2: missing addends; Think harder "4 + __ + 3 = 10", "__ + 6 + 6 = 20", "A + A + 4 = 20" | Only the habit of reading a shape as "a number I don't know yet" | **Prepared** (a Level 1 child who has done L2) |
| Q5 pictures in two sums | None | None | L2 Think harder: one unknown in one line. No two-line substitution | Learn to compare two sums | **Extension needed** |
| Q6 fit the piece | None | None | None | Practice with matching and jigsaws | **Real gap**, mostly a practice effect |
| Q7 count in 4s to the 11th | Item 4 (count on), item 11 (+2) | Set 1: frog jumps | L1: counting in 4s, "will he say 39", shared counts; L4 far places | Numbers to 44 (the check stops at 20) | **Prepared** apart from the number range |
| Q8 undo ×2, +4, −1 | None (items 8 are forward) | None | L5: undo one step (Start here) and two steps (Think harder), with + and − only | The idea of "double" | **Partly prepared** |
| Q9 figure sequence | None | None | None | Unknown: I could not find the rule | **Cannot judge**, probably a gap |
| Q10 letter cycle | None | None | L4 far places use multiples of a core length; no wrap-around with a changing step | A new strand | **Real gap** |

Tally (my judgement, 10 problems): prepared 2 (Q4, Q7), partly or extension 4 (Q2, Q3, Q5, Q8), real gap 3 (Q1, Q6, Q10), cannot judge 1 (Q9).

Other observations:
- The check and the paper measure different things. The check measures Primary 1 entry skills (counting, bonds, small stories). The paper contains no counting-to-20 or number-recognition item at all; it is made of thinking items. A child can pass the check comfortably and fail most of this paper, and the reverse.
- The check stops at 20 and the paper goes to 48. Reading, ordering and counting across the "tens" (29, 30, 31) is not checked anywhere.
- "Ready with support" in the check promises a **K2 Starter Pack** (numbers to 20, writing numbers, bonds to 10, coins). I found the pack named in `k2/k2.py` and `k2/k2.html` only; no file for it is in the repository. If it is built, it is the natural place for the extension items.
- The check's override rule ("22 or more and explains reasons well: offer Go further early") is the one place where these paper types could be used, as a short unscored "strong child" mini-set.
- Level 2 is not relevant to this paper (ages 4 to 6); the Level 2 analysis is in `g2_analysis.md`.

## 5. Gaps in order of size

1. **Spatial work with real cubes and paper** (Q1, Q3, plus Q6 and Q9 as pure visual items). Nothing in the check, the taster or Level 1 prepares it.
2. **Numbers from 20 to 50** (reading, ordering, counting across a ten). Q7 shows the range; the check stops at 20.
3. **Two-line picture equations** and "undo with doubling" (Q5, Q8). One-line unknowns are well prepared (Q4).
4. **Sequences with a rule that is not a constant step** (Q2, Q10).

## 6. Recommendations

- Do not use this paper's problems to score readiness. The 3-option guessing, no negative marking and unsolved format make scores unreliable, and the content is a stretch for age 4 to 6.
- If the owner wants a "strong child" extension to the K2 check, use a few of the drafts in `docs/sasmo/k_original_problems_draft.md` after item 12, unscored, with objects, and keep Start here and the scoring bands unchanged. Say in the parent message only what the child did, not a rank.
- If a K2 Starter Pack is built, include numbers to 50 and a short set of "tower plan" and "fold and cut" activities.
- Do not claim SEAMO preparation or results for K2 or Level 1.
- Before deciding anything: get the rest of the 2023 paper, the 2024 paper and the two SEAMO X papers with their solutions, and see a few K2 children try Q1 to Q8 with counters.
- Original drafts (about 3 per type, with answers) are in `docs/sasmo/k_original_problems_draft.md` (draft, not yet in the program). Check them with a tutor before use.
