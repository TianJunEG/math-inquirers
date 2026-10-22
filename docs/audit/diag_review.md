# Independent review: Level 1-6 placement diagnostics

Scope: outputs/diagnostics/Math_Inquirers_Level{1..6}_Placement_Check.pdf and _Tutor_Key.pdf, plus diag/content/p{1..6}.json. Read-only review. All 72 questions were recomputed independently (by hand and in Python), and every PDF page was rasterised and viewed.

Question numbering below uses the child-sheet numbers: Q1-4 warm-up, Q5-10 main, Q11-12 stretch.

## Headline

- **Answers:** all 72 key answers are correct. No wrong, ambiguous or multi-answer question was found. There are a few answer-format and mark-scheme wording inconsistencies (section 1).
- **Layout:** every child sheet is 3 pages. Nothing is clipped. No unicode box or shape symbols are used as unknowns (the only non-ASCII character in any PDF is the bullet "•" in the subtitle line). The Level 1 dot graph and the ruler both render correctly.
- **Placement:** most simulated children land sensibly. The weak spots are Level 5 (the main set is hard for an average child) and Level 6 (too easy, so a child a year below can pass), plus the usual overlap with the lower level's warm-up.
- **Naming:** the "Level N" naming is consistent in footers and on the result page. It does not appear on page 1 or in the key title, and Level 6's subtitle breaks the pattern (section 4).

## 1. Answer verification

### All answers confirmed correct

| Level | Answers confirmed |
|---|---|
| 1 | 15; 17; 8,10; triangle; 3; 20; 70c; 3; 4; Cai; 5 cm; 3x10c + 2x5c (the only solution of x+y=5, 10x+5y=40) |
| 2 | 74; 49,58,85; 7; 75; circle (position 10 = 2 mod 4); 4 (54+27=81); 24; 4:15 p.m.; $2.05; 3/4; 7; Ali (Siti rabbit, Ben dog, Mei fish, Ali cat) |
| 3 | 85; 177; 32; 8; 8 (287+358=645); 36; 3 (52=7x7+3); 9; 36 cm2; 4:35 p.m.; 7; 9 (3 first digits x 3 second digits) |
| 4 | 63; 8; 42 sq cm; 3654; 1,2,3,6,9,18; 49,000; 26; 4 2/5; 6.55 m; 7 cm; 36 (the multiples of 12 in range are 36 and 48; only 36 has digit sum 9); 36 (Cara 12, Ben 36) |
| 5 | 1/2; 0.4; 36; 77 (width 7); 4,400,000; 60 (2/5 x 3/5 x ... left = 2/5 of total = $24); 5; 10 (60,000 cm3 = 60 L); 6; 65; 101 (n squared + 1); 162 (Ben 54, Ali 162) |
| 6 | 1,2,3,4,6,8,12,24; 1/6; 65; 17; 13; 5 (31,37,41,43,47); -7; 7/12; 16; 3; 151; 12 |

### Wording and format issues in the key

All are low severity. None changes an answer.

1. **L2 Q6 ("5? + 27 = 81. The ? hides one digit").**
   - The unknown digit uses "?", the same character as question punctuation, so "5?" can read as a question rather than "5 then a hidden digit".
   - Suggested fix: use an underscore, as L3 Q5 does ("5 _ + 27 = 81").
2. **L4 Q8, key says "Accept 22/5 for the mark".**
   - The question says "Write your answer as a mixed number".
   - Decide one rule. Either remove the leniency or change the question to "mixed number or improper fraction".
3. **Units.**
   - L4 F3 (Q3) says "Write your answer with units", but the key says to give the mark if the unit is missing.
   - L3 Q9 has the same pattern, but its question does not ask for units, so that one is consistent.
   - Suggested fix: remove "Write your answer with units" from L4 Q3, or make units required.
4. **L6 Q11 (stretch) says "Explain how you worked it out".**
   - The key says "accept any clear method", so it is unclear whether the explanation is marked.
   - The answer box is the same one line as every other question.
   - Suggested fix: "Say how you worked it out (not marked)", or drop the request.
5. **L6 Q4 key says "Not a mark against the child".**
   - The question is scored (1 of 4 warm-up marks), so the note reads as contradictory.
   - Suggested fix: "A wrong answer here only tells us what support to plan."
6. **L5 Q6 and Q8 say "(Not scored: how did you start? Write one line or draw a quick picture.)".**
   - These are scored questions, so "Not scored" is confusing.
   - The answer box is a single line, with no room to draw.
   - Suggested fix: "Your working is not marked. Show it on scrap paper if you like." Alternatively, add a larger working box.
7. **Generic key header on all six keys.**
   - "Accept equivalent forms (for example 2.05 and $2.05)" is irrelevant on L1, L3, L4, L5 and L6.
   - Suggested fix: make the example level-specific or drop it.
8. **L4 Q11 puts the stretch reassurance inside the question text.**
   - Result: "(Brain stretchers are hard on purpose... Try one!) I am a number...", and "What number am I?" orphans "I?" on its own line.
   - L2 Q11 does the same ("These last two are tricky on purpose...").
   - Every other level uses only the section subtitle.
   - Suggested fix: remove the parentheses from the question text, since the subtitle already says it.
9. **L5 key, Q8 "common errors" column.** It lists "adding the dimensions", but "converting to litres" is the real step. Minor.

## 2. Age-appropriateness and differentiation

### Per-level notes

- **L1:** age-appropriate. Q8 (dot graph), Q10 (ordering) and Q6 (counting in 5s) are very easy. Even a pre-P1 child can score 4 or more, which is acceptable for the entry level.
- **L2:** appropriate. Q6 (missing digit, needs 81 - 27 with regrouping) and Q8 (time) are the real discriminators.
- **L3:** appropriate. Q9 (area of a rectangle) is also the L4 warm-up skill (L4 Q3). This overlap is by design but dilutes the signal. Q8 (equivalent fractions) likewise appears as L4 Q2.
- **L4:** appropriate, with one flag.
  - Q7 (12 + 6 x 3 - 4) tests order of operations. Not every school teaches this at P4, so children who have not met it are penalised, not just weak ones.
  - Q10 (perimeter 36, length 11) reappears **verbatim** as L5 Q4 (warm-up), where it also asks for the area. This is a content duplication across levels.
- **L5:** the hardest main set.
  - Q6 is a two-step fraction-of-remainder problem.
  - Q8 combines volume, unit conversion and rate.
  - Q7 needs the triangle formula.
  - An average P5 child can easily lose Q6, Q7 and Q8 and land on 3.
- **L6:**
  - The content (number machine, primes, negatives, probability, mean, clock arithmetic) mostly sits at upper-primary level, which feels easy for a child who is after the PSLE.
  - Q8 defines probability inside the question, and Q6 defines prime inside the question. A bright child who has not been taught either can still answer them. This is good for fairness but weakens a "taught the topic" signal.

### Simulated children

W = warm-up score out of 4. M = main score out of 6. S = stretch score out of 2.

**Level 1**

| Child | Pattern | W | M | S | Placement | Sensible? |
|---|---|---|---|---|---|---|
| Mia | all correct, S1 right | 4 | 6 | 1 | Join; try Level 2 check | Yes |
| Ben | misses Q9 (12 - 8) | 4 | 5 | 0 | Join | Yes |
| Zoe (P2) | all correct | 4 | 6 | 2 | Join; try Level 2 check | Yes. The stretch flag does its job. |
| Sam | Q5 and Q10 only | 3 | 2 | 0 | Chat + taster | Yes |
| Ali (pre-P1) | Q5, Q8, Q10 | 4 | 3 | 0 | Chat + taster | Yes |
| Kai | misses Q7 only | 4 | 5 | 1 | Join | Yes |

**Level 2**

| Child | Pattern | W | M | S | Placement | Sensible? |
|---|---|---|---|---|---|---|
| Mia | all correct | 4 | 6 | 1 | Join | Yes |
| Ben | misses Q6, Q9 | 3 | 4 | 0 | Join | Yes |
| Zoe (P3) | all correct | 4 | 6 | 2 | Join; try Level 3 check | Yes |
| Sam | Q10 only | 2 | 1 | 0 | Level 1 | Yes |
| Ali (P1) | Q5, Q6 right; fractions, time and cubes not taught | 4 | 2 | 0 | Chat + taster | Yes |
| Kai | Q5, Q6, Q7, Q9 right; misses Q8, Q10 | 3 | 4 | 1 | Join | Yes. The time and fractions gaps are masked by the other four. |

**Level 3**

| Child | Pattern | W | M | S | Placement | Sensible? |
|---|---|---|---|---|---|---|
| Mia | all correct | 4 | 6 | 1 | Join | Yes |
| Ben | misses Q7, Q9 | 3 | 4 | 0 | Join | Yes |
| Zoe (P4) | all correct | 4 | 6 | 2 | Join; try Level 4 check | Yes |
| Sam | Q10 only | 2 | 1 | 0 | Level 2 | Yes |
| Ali (P2) | Q5, Q10 | 3 | 2 | 0 | Chat + taster | Yes |
| Kai | misses Q7 (7 times table), Q8 | 4 | 4 | 0 | Join | Plausible, but the child has not met division with remainder or equivalent fractions. A tutor chat would be better, but the 4-6 rule overrides it. |

**Level 4**

| Child | Pattern | W | M | S | Placement | Sensible? |
|---|---|---|---|---|---|---|
| Mia | all correct | 4 | 6 | 1 | Join | Yes |
| Ben | misses Q7 (50), Q8 | 3 | 4 | 0 | Join | Yes |
| Zoe (P5) | all correct | 4 | 6 | 2 | Join; try Level 5 check | Yes |
| Sam | Q6 only | 2 | 1 | 0 | Level 3 | Yes |
| Ali (P3) | Q6, Q10 | 3 | 2 | 0 | Chat + taster | Yes |
| Kai | Q5, Q6, Q9 (factors are defined in the question); misses Q7, Q8, Q10 | 3 | 3 | 0 | Chat + taster | Yes |

**Level 5**

| Child | Pattern | W | M | S | Placement | Sensible? |
|---|---|---|---|---|---|---|
| Mia | misses Q8 | 4 | 5 | 1 | Join | Yes |
| Ben | Q5, Q9, Q10 right; Q6, Q7, Q8 wrong | 3 | 3 | 0 | Chat + taster | Borderline. An average P5 child is routed to a chat, which suggests the main set is slightly hard. |
| Zoe (P6) | all correct | 4 | 6 | 2 | Join; try Level 6 check | Yes |
| Sam | Q5 only | 2 | 1 | 0 | Level 4 | Yes |
| Ali (P4) | Q5, Q9 | 3 | 2 | 0 | Chat + taster | Yes |
| Kai | Q5, Q9, Q10 | 3 | 3 | 0 | Chat + taster | Yes |

**Level 6**

| Child | Pattern | W | M | S | Placement | Sensible? |
|---|---|---|---|---|---|---|
| Mia | all correct | 4 | 6 | 1 | Join | Yes |
| Ben | misses Q8 | 3 | 5 | 0 | Join | Yes |
| Zoe | all correct | 4 | 6 | 2 | Join | Yes, but there is no "try higher" route. This is the top level, so only the "Think harder pages" flag exists. |
| Sam | Q5, Q9 | 2 | 2 | 0 | Chat + taster | Yes |
| Ali (P5) | Q5, Q6, Q9, Q10 | 3 | 4 | 0 | Join | Questionable. A child a year below passes. Negatives and probability are the only real filters, and Q8 explains probability in the question. |
| Kai | Q5, Q6, Q7, Q9, Q10 | 3 | 5 | 1 | Join | Plausible. Tutor chat may be warranted but the 4-6 rule overrides it. |

### Differentiation findings

- **Level 6 is the weakest.** Q5, Q9 and Q10 are within reach of a P5 child, so a child a year below can reach 4. Suggested fix: swap Q9 (average) or Q5 for a harder item such as a two-step ratio or a simple algebra equation.
- **Level 5 is slightly too hard** for an average on-level child. Suggested fix: replace Q8 (volume + rate + unit conversion in one) with a simpler volume question, or give the conversion step in the question.
- **Kai (bright but untaught)** often scores at or above the join threshold on L2, L3 and L6 because definitions are given in the question. The sheets do not flag this, so the tutor relies on the "not learnt yet" tick. The sheet's "Ticked not learnt yet: ___" count is the only signal. The placement rule does not use it.
- **Warm-up has no effect in the 4-6 row.** A child with M 4-6 and W 0-2 is still told to join. This is rare but should be covered (for example, a sentence in the tutor guide).
- **0-1 row at Level 1** has no lower level, so it correctly says "chat with a tutor and the free taster". No fix needed.

## 3. Wording and visuals

- **Tone:** no discouraging language found. The sheets use "friendly check, not a test", "tick not learnt yet and move on", "Found it hard? That is useful to know", "hard on purpose", and "a confident start matters more than a fast one". All positive.
- **Unknown symbols:**
  - No unicode boxes or shapes anywhere. The only non-ASCII character is "•".
  - Blanks use "__" (L1 Q3), "_" (L3 Q5) and "?" (L2 Q6, L3 Q8, L4 Q2). The "?" in L2 Q6 is the only one open to confusion (section 1, issue 1).
- **L1 Q8 dot graph:** renders correctly. Three rows with 5, 3 and 2 red dots, and labels are legible. The labels (Apples, Bananas, Grapes) are small but readable.
- **L1 Q11 ruler:** renders correctly. The pencil body spans exactly 2 to 7, the tip extends slightly past 7, and tick labels 0-10 are present. The tip beyond 7 could confuse a child, who might read "8". Suggested fix: draw the pencil with a flat end.
- **Clipping and layout:** no text clipped on any page. All six child sheets are exactly 3 pages. Page 1 and page 2 have noticeable white space at the bottom (acceptable). The result page wraps "before lesson / 1." with a lone "1." on its own line at L2-L6; at L1 it is fine. Suggested fix: use a non-breaking space or reword.
- **Tutor keys:** L1 is 1 page; L2-L6 are 2 pages. No clipping.

## 4. "Level N" naming

- **Consistent:** page footers on all six sheets ("Math Inquirers Level N placement check (Ages X-Y)"), the result-page rows ("Ages X-Y (Level N)") and the file names.
- **Inconsistent or missing:**
  1. Page 1 heading shows only "Ages X-Y". "Level N" never appears on the first page, so a parent holding page 1 does not see the level name.
  2. The tutor key title says "Answer key: Ages X-Y", without the Level.
  3. The page 1 subtitle: L1-L5 say "Covers Primary N topics". L6 says "For children after the PSLE". The levels doc (docs/levels_and_placement.md, line 10) does say P6 is "after PSLE", so this is accurate but inconsistent with the other five. Suggested fix: "Covers Primary 6 topics (for children after the PSLE)".
  4. L6 "Skills covered" lists "Turns and coding with loops" and "Clock arithmetic and codes". The sheet has no turns question, so "Turns" and "codes" are over-claims. It also lists topics in a different style (capitalised, semicolons) from L1-L2 (lowercase).
  5. L4 alone says "About 40 minutes" (the others say 30) and adds an exclusions note on page 3. This is fine but inconsistent.

## 5. Suggested fixes (priority)

1. L6: strengthen the main six (replace Q9 and/or Q5) so a child a year below does not reach the join band. Review the "Skills covered" list.
2. L5: soften Q8 (volume + rate + conversion), and reword the "(Not scored...)" notes on Q6 and Q8.
3. L4 Q7: confirm order-of-operations is in the programme's P4 scheme, or add a bracket-free hint.
4. L4 Q10 / L5 Q4: remove the verbatim repeat of the 36 cm perimeter, 11 cm length rectangle.
5. L2 Q6: replace "5?" with "5 _".
6. Resolve the unit and mixed-number leniency contradictions (L4 Q3, L4 Q8) and the L6 Q4 and Q11 key wording.
7. Remove the in-question stretch reassurance from L2 Q11 and L4 Q11.
8. Add "Level N" to page 1 and to the tutor key title, and standardise the L6 subtitle.
9. Optional: add one line on how to use the "not learnt yet" count and the warm-up score when main score is 4-6.
