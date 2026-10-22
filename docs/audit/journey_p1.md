# Student journey review: Math Inquirers Level P1 (ages 6-8)

Scope: read-only review. Sources read in full: `hp/lessons.js`, `hp/scripts.js`, `hp/guide.js`, `hp/workbook.js`, `hp/qbank.json`, `hp/gaps.json` (the new check / investigation / look-back items), the built workbook PDF (`hp/Math_Inquirers_P1_Student_Workbook_Designed.pdf`, 48 pages, several pages viewed), the lesson slides actually used in delivery (`split/l1..l10/project/slides/*.html`, about 26 slides per lesson, text dumped and read; the older `deck/project/slides` set has no warm-up-check or look-back slides and is NOT what the guide describes), `diag/content/p1.json`, `diag/build_diag.py`, and the built `outputs/diagnostics/Math_Inquirers_P1_Placement_Check.pdf`. Rubric `docs/gifted_research.md` and `docs/levels_and_placement.md` were read for the NRICH low-threshold / high-ceiling idea and the placement rule.

Method and honesty note: this is a desk simulation. No child was observed. The three personas (below) and every score are my judgement from the text of the slides, scripts and pages; the diagnostic percentages come from per-question success probabilities that I assumed (stated in section 2b) and are for comparing rules, not predicting real children. Arithmetic was checked in Python (`docs/audit/journey_p1.py`, run with `python3 -I docs/audit/journey_p1.py`).

Personas:
- LOW "Lia", 6-7, struggles with school maths, slow reader, counts on fingers, not yet fluent with bonds to 10 or skip counting in 3s/4s, discouraged by being wrong in public.
- MIDDLE "Max", 7, meets school expectations, reads simple sentences with effort, bonds to 10 mostly secure, needs some support.
- HIGH "Zoe", 7 (or a strong 6), fluent within 20, reads well, fast, bored by repetition, rushes.

Score key (1-5, 5 best): P = can participate from minute 1; D = difficulty fit (3 = just right; below 3 usually too hard, and I say so; "easy" is marked); F = fun/interest; C = confidence/self-esteem; M = motivation; S = social/online experience. Score strings read "P D F C M S (mean)".

Lesson clock used by the slides: 0-5 game, 5-7 quick questions, 7-10 Warm-up check, 10-25 Explore (pairs), 25-35 Mini-lesson (4-7 slides), 35-40 break, 40-53 worksheet page 1 (pairs), 53-58 check + a second teaching burst, 58-68 page 2 (alone), 68-72 check, 72-80 talk, 80-88 exit ticket, 88-90 look-back.

---

## PART 1: Student journey, lessons 1 to 10

### Lesson 1: Count with the Frog (number patterns; the child's very first lesson)

| Persona | Scores | Evidence and flagged moments |
|---|---|---|
| LOW | P4 D2 F3 C2 M3 S3 (2.83) | Stomp-and-whisper (slide `l1-warm1`) has no wrong answer, so Lia joins in minute 1. Then `l1-warmcheck` at minute 7-10: Q2 "12 is the 2nd number and 18 is the 3rd. What is the 1st?" asks her to find a rule and step backwards, before any rule has been taught, answered on a whiteboard shown on a count of three. First public miss of her first lesson. Explore slide `l1-explore1` says "Make a number strip from 0 to 50": that is 51 numerals to write before any maths, and the printed kit only has 0-20 strips (workbook p46). Skip counting in 4s was not in the warm-up. Page 2 Q4 (two lists to 50) is about 35 numerals in a 10-minute solo slot; Q4b "What do you notice?" needs "they all end in 0" reasoning. |
| MIDDLE | P5 D3 F4 C3 M4 S4 (3.83) | Frog story and the thumbs-up prediction (`l1-explore1` script: "Will they ever land on the same number?") give purpose. Three quick whiteboard tries (`l1-try1`, `l1-try2`) are well paced. Q4 uses the whole solo page; Q5 table is fine. |
| HIGH | P5 D2 F4 C3 M3 S3 (3.33) | Too easy until minute 40: stomp counting in 2s/5s/3s, check Q1, then `l1-teach1`, `l1-we1`, `l1-we2` re-teach exactly what the check just showed Zoe knows (about 10 minutes of waiting for the group). Fast track starts only at minute 40 and she must "Ask your tutor" to start. The real thinking is on the Think Harder / Challenge pages: C1 (1, 2, 4, 7, 11, 16, 8th term), C3 (make your own two patterns) are good. |

### Lesson 2: Number Bond Inquiry

| Persona | Scores | Evidence and flagged moments |
|---|---|---|
| LOW | P4 D2 F3 C3 M3 S3 (3.00) | Explore (`l2-explore1`: ten-frame, two colours, "keep going until you think you have found them all") is a true low-threshold task. Page 1 Q1 (five blanks, "use a ten-frame") is a guaranteed win in the first 5 minutes. But check Q2 "True or false: 7 + 5 = 6 + 6. How do you know?" is a 50% guess for a child who cannot yet say why. Page 2 packs Q4 (five "=" parts and an explanation), Q5 magic triangle (sums 9, then 10), Q6 and a "Think harder" part into 10 solo minutes. The magic triangle has no entry point for Lia except trial and error; the hint "put the big numbers in the corners" is only on the `l2-teachpage2` slide shown at 56-58. |
| MIDDLE | P5 D3 F4 C3 M3 S4 (3.67) | Listing bonds in order shows a visible pattern (Q2b). "=" as a see-saw is memorable. Page 2 has about 9 answer slots, so Max finishes Q4 and part of Q5. |
| HIGH | P5 D2 F3 C4 M3 S3 (3.33) | Bonds of 10 and 20 are recall. The "=" items and magic triangle are real thinking but only from minute 58 unless fast tracked. C1-C3 and the odd/even investigation ("Mei says: when two numbers make 10 they are both odd or both even") are excellent, but they sit at the very end. |

### Lesson 3: Let's Plan the Fruit Party (picture graphs)

| Persona | Scores | Evidence and flagged moments |
|---|---|---|
| LOW | P5 D3 F5 C4 M4 S4 (4.17) | Sticky-dot vote (`l3-warm1`): one choice, nobody can be wrong. Online it asks a 6-year-old to type a fruit name in chat (a reading/typing hurdle; a spoken or thumbs vote would be safer). Page 1 Q1-Q2 (most, fewest) are immediate wins. Q7 "What else should the teacher think about?" accepts any sensible idea. The hard part is in the mini-lesson: `l3-teach2`, `l3-try2`, `l3-try3` (keys of 2 and 3, "the key is lost"). |
| MIDDLE | P5 D4 F5 C4 M4 S4 (4.33) | Real purpose (plan the party), a graph made from their own vote, Part B own-group tally. Best-fitting lesson. |
| HIGH | P5 D2 F4 C4 M3 S4 (3.67) | Reading dots is trivial. First real thinking is `l3-try3` and T1-T4 (key of 2), C3 "banana wins by exactly 2, then find a second graph". Part B (group vote) sits on the solo page but needs the group, so a fast-tracked child skips it. |

### Lesson 4: Pattern Inquiry

| Persona | Scores | Evidence and flagged moments |
|---|---|---|
| LOW | P5 D3 F4 C3 M3 S3 (3.50) | Clap-snap-stomp (`l4-warm1`) and straw triangles (`l4-explore1`) are concrete. Lowest reading load of the level (core page about 120 prose words). But "count in 3s to find where a core ends" (`l4-teach1`, `l4-we1`) assumes fluent counting in 3s, introduced once in Lesson 1. Q3c "Why does he need only that many more sticks? (Look at the picture.)" asks for a spoken or written explanation of a shared side. Q4 (15 sticks, work backwards) is the stuck point. Needs 21 straws or lolly sticks per pair at home. |
| MIDDLE | P5 D4 F4 C4 M4 S4 (4.17) | Predict-then-test with straws; the core idea lands. |
| HIGH | P5 D2 F3 C3 M3 S3 (3.17) | "Place 30" and "10 triangles" are answered in seconds. First real puzzle is C1 (47 beads, how many green) or the investigation "Mei says place 30 is the same as place 3", both late. Weakest HIGH cell. |

### Lesson 5: Mystery Number (working backwards)

| Persona | Scores | Evidence and flagged moments |
|---|---|---|
| LOW | P4 D2 F3 C2 M3 S3 (2.83) | Explore cup game (`l5-explore1`: hide counters, add 5 loose, partner works backwards, lift the cup to check) is the best self-checking activity in the level. But check Q2 "take away 2, then add 7, I get 12" is a two-step reversal before it is taught; the mini-lesson (`l5-we2`) teaches two-step undo in the same 10 minutes as machines. At 54-58 three more new ideas arrive (`l5-teachbar` more/fewer bars, `l5-teachq1`, `l5-teachq2` queue counting) minutes before the solo page. Page 2 Q3 is three comparative sentences ("5 more than Ali", "6 fewer than Mei") with four sub-parts; Q4b says "(Careful: Draw it!)", which reads as a trap warning. |
| MIDDLE | P5 D3 F4 C3 M4 S4 (3.83) | "Think of a number" magic gives purpose; IN/OUT vocabulary arrives via three slides. |
| HIGH | P5 D3 F4 C4 M4 S3 (3.83) | Queue trap (16 vs 15), two-step reversals, C2 snail puzzle (reaches the top on day 4, checked) are real. Quick questions 1-2 are trivial. |

### Lesson 6: Coin Combos (money)

| Persona | Scores | Evidence and flagged moments |
|---|---|---|
| LOW | P3 D1 F2 C1 M2 S2 (1.83) | The warm-up shop (`l6-warm1`) runs from 65 cents up to a $65 scooter and $12/$25 items with notes, so a child who has not met dollars is excluded in minute 1. Objects must be cut from workbook pp43-44 at home, otherwise Lia has nothing to hold. Check Q1 asks which of three amounts a 20c+10c+5c purse can pay (three parses); Q2 "exactly 3 coins" has not been taught. The mini-lesson crams four skills into 10 minutes (all ways, fewest coins, exactly-N coins, notes). Printed page 2 begins at Q2 "Think harder! Find ALL the ways to make 30c" (6 ways, 6 lines to write) even though slide `l6-ws1` tells pairs to do Q1 and Q2 on page 1: it is a core item labelled "Think harder". Q1 has five table rows but only four ways exist ("Row E is spare" appears only in the tutor key), so a child who has found every way still sees an empty row. Solo page has Q3 85c, Q4 explain, Q5 dollars ($65 bicycle and $8 helmet). The exit ticket "exactly 3 coins that make 40c" ends the lesson on another hard item. |
| MIDDLE | P4 D2 F3 C2 M3 S3 (2.83) | Too hard in volume: money in cents, notes, change and exact-N coins in one lesson. |
| HIGH | P5 D3 F5 C4 M4 S4 (4.17) | The best-fitting lesson for Zoe: find all the ways, fewest coins, "why can't 35c be made with two coins?", T1-T4, C2 (sweets and biscuits making 90c). |

### Lesson 7: Shape Safari

| Persona | Scores | Evidence and flagged moments |
|---|---|---|
| LOW | P4 D3 F4 C3 M3 S3 (3.33) | Shape hunt (`l7-warm1`) and fold-and-cut (`l7-explore1`) are physical wins; Q2's table is pre-filled for circle and triangle (a good scaffold). Hard moments: `l7-we1` teaches the 3 by 3 grid = 14 squares in the mini-lesson, and the exit ticket asks that same 14 at minute 80-88, so a child who says "9" ends the lesson wrong. The house picture is about 5 cm wide. Paper square plus scissors on camera needed at home. |
| MIDDLE | P5 D3 F5 C4 M4 S4 (4.17) | Sides = corners discovery (Q2) is a real "notice it" moment. |
| HIGH | P5 D3 F5 C4 M4 S3 (4.00) | Hidden squares and triangles are a good puzzle; solo Q6 (5 squares) is easy; T3 and C1 (triangles 3, 6, 10 ...) are better. |

### Lesson 8: Logic Lab

| Persona | Scores | Evidence and flagged moments |
|---|---|---|
| LOW | P3 D2 F3 C2 M3 S3 (2.67) | Guess-my-number (`l8-warm1`) is open and safe; odd-one-out (Q6, talk slide) has "more than one correct answer", which is very safe. But page 2 is four different puzzle types in 10 solo minutes: Q3 grid with a double-negative clue ("Ali does not have a cat or a dog"), Q4 four-child line-up, Q5 three riddles ("My digits add up to 5" with "digits" unexplained), Q6. Highest reading load of the level (core page about 280 prose words by my count). The two-loop picture needs "less than 6", "odd", "even" at once (odd/even defined only in a tip line). Check Q1 is a four-name ordering chain. Buttons and string loops needed at home (small objects only with a grown-up). |
| MIDDLE | P4 D3 F4 C3 M4 S4 (3.67) | Grid ticks and crosses give a clear method; page 2 is too much. |
| HIGH | P5 D3 F5 C4 M4 S4 (4.17) | Logic grids, riddles, C1 secret number, the "list all orders" investigation: a strong fit. |

### Lesson 9: Measure It!

| Persona | Scores | Evidence and flagged moments |
|---|---|---|
| LOW | P4 D2 F4 C3 M3 S3 (3.17) | Measuring her own pencil, book and shoe with a guess first (no wrong guesses) is engaging. But every child needs a cm ruler, cube strips, paper clips and erasers at home. Check Q1 (ribbon from 4 cm to 11 cm) comes before the ruler is taught. Q2 has a "Difference (guess and measure)" column that is never explained to a child. Q4 unit conversion (1 clip = 2 erasers, both directions) is more advanced than the lesson label suggests. Q6 asks about positions on a ruler in words with no ruler on the page. Highest prose load (about 290 words) and Q3b has a 27-word hint. |
| MIDDLE | P5 D3 F4 C3 M4 S4 (3.83) | Hand-span comparison ("whose hand is bigger?") is a lovely, concrete reason for equal units. |
| HIGH | P5 D3 F4 C4 M4 S3 (3.83) | Investigation "a shorter unit gives a bigger number; what about half a cube?" is excellent. Q1, Q4, Q5 are quick. |

### Lesson 10: Challenge Day

| Persona | Scores | Evidence and flagged moments |
|---|---|---|
| LOW | P3 D2 F3 C3 M4 S2 (2.83) | The mental-maths relay (`l10-warm1`) is a public chain of recall questions from all nine lessons; the script itself has to say "give a wrong answer a gentle 'try again', not a groan", which shows the risk. The tutor assigns each pair a puzzle card; online the card is pasted into the room chat (reading from chat), swapped at minute 20, and each pair reports back in 30 seconds. Page 2 is a nine-question review. Positives: "how to start a puzzle: draw it, list it, make a table" (`l10-teach1`) is explicit strategy teaching, and the close gives every child a certificate and "one specific thing they did well". |
| MIDDLE | P4 D3 F4 C4 M4 S3 (3.67) | Good consolidation; the report-back is the stress point. |
| HIGH | P5 D3 F5 C4 M5 S4 (4.33) | Puzzle cards, Q9 and C3 (change ONE thing in a puzzle and say how the answer changes), teach-it-in-two-sentences. Strongest cell. |

### Summary heatmap (mean of the six scores)

| Lesson | LOW | MIDDLE | HIGH |
|---|---|---|---|
| 1 Frog / patterns | 2.83 | 3.83 | 3.33 |
| 2 Number bonds | 3.00 | 3.67 | 3.33 |
| 3 Fruit party / graphs | 4.17 | 4.33 | 3.67 |
| 4 Pattern inquiry | 3.50 | 4.17 | 3.17 |
| 5 Mystery number | 2.83 | 3.83 | 3.83 |
| 6 Coin combos | 1.83 | 2.83 | 4.17 |
| 7 Shape safari | 3.33 | 4.17 | 4.00 |
| 8 Logic lab | 2.67 | 3.67 | 4.17 |
| 9 Measure it | 3.17 | 3.83 | 3.83 |
| 10 Challenge day | 2.83 | 3.67 | 4.33 |
| Level mean | 3.02 | 3.80 | 3.78 |

Level mean by dimension (P, D, F, C, M, S): LOW 3.9, 2.2, 3.4, 2.6, 3.1, 2.9. MIDDLE 4.7, 3.1, 4.1, 3.3, 3.8, 3.8. HIGH 5.0, 2.6, 4.2, 3.8, 3.7, 3.4. The headline is difficulty fit and confidence for Lia (2.2 and 2.6) and difficulty fit for Zoe (2.6, "too easy" in lessons 1-4). Participation is good for everyone because the openings are inclusive.

### The 5 weakest lesson-persona cells, with fixes

1. L6 LOW (1.83). Fixes:
   - Slide `l6-warm1`: cut to three price tags in cents only ("Eraser 65c", "Pencil 80c", "Sticker 30c") and add the line "Any way that pays exactly is a good way. Then we look for a way with fewer coins." Move $3, $12, $25, $65 to the optional dollars section.
   - `gaps.json` L6 check Q1 replace with: "Ben has a 20c coin, a 10c coin and a 5c coin. Can he pay 25c exactly?" Q2 replace with: "Show one way to make 15c. Can you find a different way?" (the lesson's whole idea, and a child can win with 10c+5c or 5c+5c+5c; fast-track test: "found both and can say why").
   - Workbook Q2 (`hp/workbook.js`, L6): change text to "Find ALL the ways to make 25c using 20c, 10c and 5c coins. Start with the biggest coin. (Hint: there are 4.)" Verified: 25c with 20/10/5 has exactly 4 ways and it is the worked example on `l6-we1`, so it is a guaranteed win. Move the current 30c (6 ways, verified) to Think Harder as T5. Remove "Think harder!" from the core page.
   - Put the page break before Q3, not before Q2, so page 1 = Q1+Q2 as slide `l6-ws1` says.
   - Add under the Q1 table, in italics: "You may not need every row." (Row E is spare because only 4 ways exist.)
   - Move the dollars strand (Q5, `l6-teachnotes`, `l6-trynotes`) out of the core; keep it on Think Harder. Cut "pay in dollars with notes up to $100" from the lesson objective.
2. L8 LOW (2.67). Fixes:
   - Page 2: label Q5 and Q6 "If you have time" and keep only Q3, Q4 as core.
   - Q3 grid: pre-print crosses in Ali/cat and Ali/dog with the line "We crossed these two for you because of Clue 1."
   - Q5: keep (a) only on the core page (move (b), (c) to Think Harder). Reword (c): "I have 2 digits. When I add my two digits I get 5. I am less than 20."
   - Check Q1 (`gaps.json` L8): replace the four-name chain with "Ben is shorter than Cara. Cara is shorter than Dev. Who is in the middle?"
   - Tip line before the two-loop picture: "Odd numbers end in 1, 3, 5, 7 or 9. Even numbers end in 0, 2, 4, 6 or 8" is already there; put it in a boxed strip, not a one-line italic.
3. L1 LOW (2.83). Fixes:
   - Kit: add a printed 0-50 number strip (two rows of 0-25 and 26-50, or one long strip) to the Inquirer Kit page, and change `l1-explore1` to "Take your number strip. Frog 1 hops in 4s ..." (no writing of 51 numbers).
   - Page 2 Q4: change to "Ali counts in 2s from 2 up to 30. Mei counts in 5s from 5 up to 30. Write both lists first." (answer 10, 20, 30; the "they all end in 0" reasoning still works) and edit slide `l1-ws2ans` Q4a to "10, 20, 30". Keep the 50 version as T-item.
   - Check Q2 (`gaps.json` L1): replace with "A pattern goes 6, 12, 18. What number comes next? How do you know?" and keep the bunny question as Q1. Tutor line before the check (all lessons, see section on new items).
4. L5 LOW (2.83). Fixes:
   - Check Q2: replace "I take away 2, then I add 7" with "I think of a number. I add 3. Then I add 4. I get 12. What is my number?"
   - Page 2 Q3: split into two steps: "Ali has 8 marbles. Mei has 5 more than Ali. (a) How many marbles does Mei have? ____  Ben has 6 fewer than Mei. (b) How many marbles does Ben have? ____" then (c) and (d) as now, with (d) starred.
   - Q4b: delete "Careful:", write "Draw the children as circles first."
   - Move `l5-teachbar` ahead of page 1 or drop it for the first sitting; do not add three ideas in 54-58.
5. L6 MIDDLE (2.83). The same L6 changes remove most of this; additionally make Q3(b) "exactly 6 coins" starred.

Tie at 2.83: L10 LOW. Fix: replace the relay (`l10-warm1`) with a no-turn-taking version: "Everybody writes the answer on a whiteboard; there is no passing round", and let pairs choose a card rather than the tutor assigning one; add the SAY line "It is fine to report back one thing you tried, not the answer."

### The 3 strongest cells and why

1. L3 MIDDLE (4.33) and L3 LOW (4.17): the opening is a vote with no wrong answer, the objects are the children's own data, the first worksheet questions are quick wins, and the open questions (Q7, Part B) accept any sensible idea. This is the closest the level comes to low threshold, high ceiling.
2. L10 HIGH (4.33): puzzle cards, create-your-own and "change one thing" are open-ended with a visible ceiling.
3. (Next on the list, at 4.17: L4 MIDDLE, L6 HIGH, L7 MIDDLE, L8 HIGH.) Lia's single best cell is L3 (4.17): copy its structure into L6 and L8.

### Checks of the new items

Warm-up check (minutes 7-10, two questions on the key idea, whiteboards shown on three). Findings:
- It is asked BEFORE Explore and the Mini-lesson, so it tests the lesson's key idea before it is taught (L1 Q2 rule from two terms, L5 Q2 two-step undo, L6 exactly 3 coins, L9 ruler 4 to 11 cm, L7 corners to sides). The guide says "it is not a test", but it decides who is fast-tracked, so it is a pre-test with a hidden stake.
- Nothing in the script frames it as new. The SAY line is only: "Two questions on your whiteboard. Write your answer and how you know. Show me on three." Recommended wording for all ten lessons: "These two are sneak-peek puzzles. You have not been taught this yet, so a guess is a great start. Write your answer, and draw or write how you tried it. Show me on three; I will only read out the boards I want to talk about."
- Online, with 8 thumbnails, a child sees a wrong board held up by Lia. Public board-show is the most exposed moment in the lesson for a low-confidence child and comes in the first 10 minutes.
- Guide line "Quietly note who got both right and gave a reason" is a fair idea but 8 children, 2 questions each, one minute per question leaves very little time to read reasons; expect mostly "answer right/wrong" judgements. Two-question screens are noisy: a 50% guess (L2 true/false) passes both with 25% probability for a child who knows nothing.

Fast track. Findings:
- The script (`guide.js` 55-56) says "Nobody is labelled: tell a child privately" but the workbook prints a 45-word box on page 1 of EVERY lesson: "Fast track. Got both warm-up check questions right and can say why? Ask your tutor. You may go straight to the Think Harder and Challenge pages ... Come back to the group for talk time." Every child therefore reads the criterion, so a child who got it wrong knows exactly what happened. It is also 45 words of reading before the first question for a 6-year-old.
- "Ask your tutor" makes the child self-select; a shy strong child will not ask, and a child who guessed right will.
- The Challenge header reads "Challenge (for strong thinkers)", a second label.
- Pairs: the guide says children start in pairs, but a fast-tracked child leaves the pair at minute 40 and no instruction says what happens to the partner. The partner may be left alone with a pair task, or the fast-tracked child may be a high child who was helping.
- Recommended replacement for the box: "Choice time. Your tutor may ask you to start on the Think Harder page. If you finish a page early, go to Think Harder. Always come back for talk time." Remove the "Got both ... right" criterion from child-facing pages (keep it in the tutor guide). Replace the Challenge header with "Challenge pages: try one any time." Form pairs by track (silently) so both partners move together.

Open investigation (last item on each Challenge page). Findings: well designed ("Is it always true?", "What if we change...?", Mei/Ben make claims that the child tests); the claims are attributed to a named character, which normalises being wrong. The model answers are correct (checked: 11 pairs of 10 and 21 of 20 all same parity; 6 orders of 3 children, 4 with "Ali is not first"; 5 shapes from 4 squares; totals 18-30 for the 3-number jump). Concerns: they sit at the end of page 4 of each lesson, so a LOW or MIDDLE child will never see them unless the family uses them at home, and the card header prints "No.?" instead of a number (cosmetic bug seen on printed page 6 and 24). Reading load is 30-66 words per task, which is fine only for a strong reader.

Reflection ("What was hard?", minutes 88-90; box at the foot of core page 2). Is it safe for a low-confidence child? Mostly yes:
- Good: "There are no right answers", strategy words (counters or objects / drawing it / asking someone / trying again), a three-face "It felt" scale, never graded, and praise for strategy, not speed.
- Risks: (1) one minute is not enough to read about 43 words and tick three rows after 88 minutes; a slow reader will not finish, which makes the safe box feel like a test. (2) "I got unstuck by ..." presumes the child got unstuck; a child who did not has no honest tick. Add "I was not stuck" and "I am still stuck" options. (3) The script says "Ask one or two children to share one line": a direct ask to Lia "what was hard?" is exposing. Say "Who would like to tell us one thing that helped them?" and ask only volunteers. (4) "Mark S, D or H" in the tracker and "if D or H, two minutes of catch-up at the start of the next lesson": D means "correct but cannot explain yet" and H "needs help"; catch-up in front of the group would make the label visible. Do catch-up in a breakout room.

### Level-wide patterns

- Pacing. Minutes 0-40 are tutor-led: the Mini-lesson has 4-7 slides in 10 minutes (about 1.4 minutes per slide), including 2-3 "your turn" whiteboards; there is a second teaching burst at 52-58 that introduces new ideas right before the solo page (L5 bars and queues, L6 fewest coins and notes, L9 unit conversion). The solo page (58-68) holds 4-10 answer slots (median about 7, my count) plus explanation lines in 10 minutes, about 85 seconds per slot including writing. Pages: L9 has the most slots (10), L1 the fewest but 35 numerals to write.
- Stamina. After the single 5-minute break at 35-40, there are 50 minutes of seated, mostly sedentary work with one 1-minute stretch at minute 68. The Talk time is 8 minutes (script: "ask two or three children"; routine table: "each child unmutes in turn", which is inconsistent: 8 children at one minute each is 8 minutes of listening for 6-year-olds) and the exit ticket gets 8 minutes for one question.
- Reading load. Core pages carry roughly 120 (L4) to 290 (L9) words of prose by my count (a lower bound), with Flesch-Kincaid grade 1-3.5 because sentences are short, but comparatives ("3 cubes shorter than Mei's"), "exactly", "fewest", "digits", "altogether" are the real load. The longest single item is 28 words (L9). Think Harder / Challenge pages are 90-200 words. The guide tells the tutor to read only the lesson title aloud at minute 40; reading each question aloud is left to the pairs, so the weakest reader depends on a partner. Recommended: add "Tutor reads Q1 and Q2 aloud, then pairs read the rest" to the minute-40 instruction.
- Guaranteed win in the first 10 minutes of the worksheet for Lia. Yes in 7 of 10 lessons (L1 Q1 skip-counting blanks, L2 Q1 bonds, L3 Q1-2, L4 Q1, L7 Q1, L9 Q1a, L10 Q1), partly in L5 (needs the undo idea) and L8 (Q1a is easy but Q1c is a four-clue chain), and effectively no in L6 (Q1 table with a spare row; Q2 on the same page in the PDF).
- Wait time for Zoe. Minutes 0-40 are largely pitched at the middle: warm-up easy for 7 of 10 minutes, then the Mini-lesson re-teaches what the check just showed she knew. Estimated 15-20 of the first 40 minutes are low-challenge for a child who passes the check; plus the solo-page check/teaching burst at 53-58, talk (8) and exit (8) bring the total to roughly 30-35 of 90 minutes. This is the level's biggest "bored" risk; HIGH scores 2 on difficulty fit in L1-L4.
- Pairs and groups. Pair formation is not specified anywhere. Online, breakout-room pairs with a 6-year-old who cannot yet read the instruction have nobody to ask; the tutor "circulates" between up to four rooms. "Tutor checks one or two answers each" in the online column means about 75 seconds of tutor time per child over the solo page.
- Materials and home load. The online workbook must be printed (48 pages, with cut-outs on pp43-47) and held up to the camera; L4 needs 21 straws or lolly sticks per pair, L5 paper cups, L7 scissors, L8 string loops and buttons (small objects), L9 a cm ruler, paper clips and erasers. A child without these cannot take part in the Explore, which is half the lesson. Low-income or low-support households are likeliest to be the LOW persona.
- What works well and should be kept: inclusive openings; explicit "stuck? draw it, list it, make a table"; errors attributed to Mei/Ali/Ben ("Mei/Ben says ...", 7 times in the sources); strategy-based praise instructions; wait 10 seconds; the Look-back; the certificate with one specific praise.
- Exit tickets: L6 ("40c with exactly three coins") and L7 ("squares in a 3 by 3 grid = 14") are too hard to end a lesson on; L1-L5, L8-L9 are accessible.

---

## PART 2: Diagnostic check (diag/content/p1.json, 12 questions, 30 minutes)

### (a) True skill demand and fairness

School-year labels below are from memory of the Singapore primary syllabus and are not verified against the current MOE document.

| # | Question | True skill demand | Fair for 6-8 / P1? |
|---|---|---|---|
| W1 | What comes just after 14? | counting on within 20 | Fair (K2). |
| W2 | Which is bigger, 17 or 12? | compare within 20 | Fair (K2). |
| W3 | 6 sweets + 3 more | add within 10 (the label says "within 20", it is within 10) | Fair; duplicates M1. |
| W4 | Shape with 3 sides | name a triangle | Fair (K1). |
| M1 | 7 and ? make 10 | bond to 10 | Fair; the lesson 2 prerequisite. |
| M2 | 5, 10, 15, ? | skip count in 5s | Fair if 5s were met in K2; a child who only knows 2s and 10s may miss. |
| M3 | 40 cents + 30 cents | tens addition in a money context; needs "cents" | Fair for P1 Term 2+; a 6-year-old in K2 may not know the cent as a unit. |
| M4 | 5 like apples, 3 bananas, 2 grapes: how many more apples than grapes? | comparison "how many more" from a sentence, with a distractor; 17 words, no picture although the skill is labelled "Reading graphs" | Skill (difference) fair; reading load highest in the main set. |
| M5 | Pen 8 cubes, ruler 12: how many longer? | difference within 20 | Fair. |
| M6 | Ali taller than Ben, Ben taller than Cai: shortest? | transitive ordering | Fair; good question. |
| S1 | Two numbers add to 10, one is 4 more | sum-and-difference puzzle by guess-and-check | Hard for 6-8 (P3 heuristic); fine as a stretch. |
| S2 | 5 coins, 10c and 5c, total 40c | two-unknown guess-and-check (unique answer 3 and 2, verified) | Hard; fine as a stretch. |

Findings: (1) The diagnostic checks number sense and basic reading; it does not test what makes lessons hard: reading a ruler (L9), counting in 2s/3s/4s (L1, L4), "=" as balance (L2), odd/even (L8), dollars (L6), working backwards (L5), multi-sentence problems (L5, L9). (2) The cover says "Covers Primary 1 topics" but the lessons use P1 topics at P2-P3 depth (common multiples of 4 and 5, bonds of 20, notes to $50, reading a ruler from 3 cm, 14 squares in a 3 by 3 grid, logic grids). A child who gets 6 of 6 may still meet L5, L6 and L8 as hard (the LOW and MIDDLE heatmap rows). (3) The sheet has no pictures although the lessons are picture- and diagram-based (M4 is called graphs but has none). (4) Child-facing reading: the instruction says "Read a question aloud if they ask"; a 6-year-old who cannot read well does not ask. Q12 is 20 words and Q5 17 words (a readability formula means little on one-line items; the comparatives, "exactly" and the 3-item list are what a young reader trips on).

### (b) Six profiles: results and placement

Assumed per-question success (my assumptions): Strong 6-8 7yo: warm 99%, main 95/97/90/80/90/90, stretch 50/35. Typical 7yo: warm 95-98, main 85/85/65/50/60/70, stretch 12/6. Weak 7yo: warm 75-90, main 45/50/15/10/20/40, stretch 2/1. Younger strong 6yo: warm 98, main 90/90/35/55/65/80 (cents unfamiliar), stretch 20/8. Older weak 8yo: warm 95-98, main 70/70/50/35/45/55, stretch 6/3. Rusher 7yo, typical ability: warm 80-90, main 65/65/40/25/30/50, stretch 5/3. Outcomes under the CURRENT printed rule (6-8 join; 4-5 join with support, tutor chat first if warm-up 2 or less; 0-3 taster plus chat; 8/8 with 4/4 may try P2):

| Profile | Expected warm / main / stretch | Result shares | Right level (against lessons) | Verdict |
|---|---|---|---|---|
| Strong-for-age | 4.0 / 5.4 / 0.9 | join 71%, try P2 9%, "support" 20% | P1, with fast track (or P2 check if 8) | Mostly right; 20% wrongly told "support" |
| Typical-for-age | 3.9 / 4.2 / 0.2 | support 61%, taster + chat 23%, join 15% | P1 plain join | Wrong for about 84% |
| Weak-for-age | 3.3 / 1.8 / 0.0 | taster + chat 94% | P1 with support or K2-style readiness first | Right |
| Younger and strong (6) | 3.9 / 4.2 / 0.3 | support 63%, taster + chat 20%, join 16% | P1; expect support at cents (L6) and ruler (L9) | Mostly right, partly for the wrong reason (cents) |
| Older and weak (8) | 3.9 / 3.3 / 0.1 | taster + chat 55%, support 41%, join 3% | P1 (lowest level; reads and writes well) | Over-cautious |
| Guesser/rusher | 3.4 / 2.8 / 0.1 | taster + chat 72%, support 24%, join 1% | P1 plain join | Wrong; paper cannot show rushing |

Score-out-of-8 distribution for the typical profile (%): 0:0, 1:1, 2:5, 3:17, 4:32, 5:30, 6:13, 7:2, 8:0. Sensitivity: if the typical child is stronger (main about 85% each) the current rule gives join 44%, support 51%, taster 4%. Either way, fewer than half of ordinary children get an unqualified "join".

### (c) Cut scores, luck and the level below

- Effective scale: the two stretch questions are almost never answered by a typical child (6% and 12% in my assumption, about 0.2 marks). The "6 to 8" band therefore needs a perfect score on the six main questions, or 5 plus a stretch. For a child who answers each main question correctly with probability p: p=0.9 gives 6/6 53% of the time; p=0.8 gives 26%; p=0.7 gives 12% (and 26% of such children score 3 or less, i.e. are told "taster"); p=0.6 gives 5%. Even in the most favourable model (all 8 items equally hard) a child with p=0.7 gets "join" only 55% of the time, "support" 39%, "taster" 6%.
- One question moves a child across a band edge (6 to 5, 4 to 3), so a single careless slip in 12 questions changes the advice. This is acceptable for a guide, not for a message that says "expect support" or "we suggest a taster first".
- Lucky placement is not the risk: pure blind guessing (M6 is 1/3, numeric answers about 1/10) gets 4 or more of the 6 main questions about 0.3% of the time. Unlucky or careless placement is.
- Warm-up vs level below: W1, W2, W4 and W3 are genuinely K2 (the repo has a K2 readiness check). They hardly discriminate: expected warm-up is 3.9/4 for strong, typical and older-weak children and 3.3/4 for the weak child, so the "warm-up 2 or less" rule fires for at most 3% of any profile. W3 (6+3) and M1 (7+3) test the same skill.
- P1 has no level below. The program and `build_diag.py` map "one level down" to "a tutor chat and the free taster", but the generated page also says "Starting one level down means more success", which does not exist for P1.

### (d) Parent result page and tutor key: wording that could discourage

(Quoted from the built PDF.)
- "4 or 5: Join Ages 6-8 (P1), and expect some support." Under my model 61% of typical 7-year-olds see this line; it reads as "your child is behind".
- "If the warm-up score is 2 or less, a tutor chat and the free taster first may be the more comfortable start." Fragment, reads as incomplete advice.
- "0 to 3: We suggest a tutor chat and the free taster first." Same fragment; no explanation of what the taster is for.
- "Not yet? That is useful to know, not a failure. Starting one level down means more success and more joy in class." The word "failure" plants the idea; "one level down" is wrong for P1.
- "Your child has the foundations and will be well challenged." Could scare a parent of a 6-year-old.
- The child sheet gives no warning that "Brain stretchers" are hard on purpose; a 6-year-old who cannot do Q11-Q12 may stop trying.
- The answer key (page 3) and result page are in the same PDF as the child's question pages; a parent can see the answers, and the instruction "Read a question aloud if they ask, but do not help with the maths" is easily broken.
- The key header says "Accept equivalent forms (for example $2.05 and 2.05)", copied from an upper-level sheet and irrelevant to P1.
- Key "Watch for" cues ("Note if the child ... says 'pyramid'") are written for a tutor, but the parent marks at home.

### (e) Recommended changes (exact text)

1. Cut scores. Judge on the six main questions; stretch only unlocks the P2 check. Simulated with the assumptions above: typical child 67% join (+7% try P2), 25% support, 1% taster; strong child 98% join; weak child 6% join, 45% support, 50% taster. Parent page rows:
   - "4, 5 or 6 of the 6 main questions: Join Ages 6-8 (P1). Most children who meet school expectations score here. In class every child gets time to think and help when stuck."
   - "2 or 3 of 6: Join Ages 6-8 (P1) after a 10-minute chat with a tutor and the free taster lesson, so we can see how your child likes to work."
   - "0 or 1 of 6: We suggest the free taster and a chat first. Many children are simply not ready yet, and we would like to help you choose a good starting point."
   - "Brain stretchers (Q11-Q12) do not change the level. If your child gets one or both right and scored 5 or 6 on the main questions, you can also try the Ages 7-9 (P2) check."
   (If the simple 8-mark version is kept, use 5-8 join, 3-4 join with a chat, 0-2 taster first; simulation: typical child 45% join, 49% support, 6% taster.)
2. Child sheet intro (replace "Read a question aloud if they ask"): "Read every question aloud to your child. Reading is not what we are testing. Say 'Try your best, or skip it' if they are stuck. Brain stretchers are hard on purpose: it is fine to skip them."
3. Q4 (replace the sentence with a tiny graph): "Apples: 5 dots. Bananas: 3 dots. Grapes: 2 dots. How many more dots does Apples have than Grapes?" (draw the dots as circles in the PDF). Same answer 3; removes 17 words and tests graph reading.
4. W3 (duplicates M1): replace "I have 6 sweets. I get 3 more. How many sweets now?" with "Count in 2s: 2, 4, 6, __, __." (answer 8, 10; skill "Counting in 2s", needed in L1).
5. Key header: delete "(for example $2.05 and 2.05)"; split the tutor key and the result page into a separate "For the tutor" PDF so the child's file has no answers.
6. Result page "Not yet?" box: "Not yet? Every child starts somewhere. A short chat and a free taster lesson let us find the right start. Your child can join at any time." Delete "failure" and "one level down" for P1.
7. Tutor-key wording for rushing: add to the instructions "If your child answers very quickly, ask them to check one answer by drawing it", since rushing cannot otherwise be seen on paper.
8. Add one question that tests a lesson demand: replace S1 (two numbers adding to 10, 4 more) with "Look at the ruler: the pencil starts at 2 and ends at 7. How long is the pencil?" (add a small ruler graphic) as a stretch item; keep S2 as the harder stretch. Rationale: ruler offset is the L9 stumbling block.
9. Cross-check with the lessons: because 6 of 6 does not prove readiness for L5, L6 and L8, add to the result page for the 6-8 band: "In lessons your child will meet money to $50, reading a ruler and logic puzzles. We start slowly and help every child."

Arithmetic verified in Python: S1 (3 and 7) and S2 (3 ten-cent and 2 five-cent) are unique; L6 ways to make 20c, 25c, 30c with 20/10/5 are 4, 4 and 6; 3 by 3 grid has 14 squares (4 by 2 has 11, 4 by 3 has 20); orders of three children 6 (4 with "Ali is not first"); only 20 and 40 are common multiples of 4 and 5 up to 50; with 1-6 in the magic triangle the working side totals are 9, 10, 11 and 12 only (13 is impossible, as the key says); 3rd-from-front and 3rd-from-back gives a queue of 5; snail on a 9 cm wall climbs out on day 4.

---

## Summary (10 lines)

1. Verdicts by persona: LOW (Lia) 3.0/5, struggles on difficulty and confidence, with L6 (1.8), L8 (2.7), L1, L5, L10 (2.8) as the cells to fix; MIDDLE (Max) 3.8/5, good except L6 (2.8); HIGH (Zoe) 3.8/5, bored in L1-L4 (2.6 on difficulty fit), delighted in L6, L8, L10.
2. Top fix 1: stop the Warm-up check being a public pre-test (frame it as "sneak-peek puzzles"; keep boards private) and delete the child-facing "Got both ... right" fast-track criterion and the "Challenge (for strong thinkers)" header.
3. Top fix 2: lighten L6 (cents only in the warm-up, Q2 = 25c with 4 ways, dollars moved out, page break and spare-row notes fixed) and L8 page 2 (two core tasks, a pre-crossed grid).
4. Top fix 3: cap solo page 2 at about 5 answer slots and keep new teaching out of minutes 53-58; protect Lia's L1 start (print a 0-50 strip; shorten Q4 to 30).
5. Top fix 4: give Zoe something real before minute 40 (a standing "puzzle of the lesson" from minute 10, and let a passing child skip the Mini-lesson re-teach).
6. Top fix 5: diagnostic bands: judge on the 6 main questions and soften the parent text; stretch only unlocks the P2 check; remove "failure" and "one level down".
7. Level-wide: a 90-minute online lesson with one 5-minute break, 50 minutes seated, 8-minute turn-taking talk and heavy home materials is the biggest structural risk for ages 6-8.
8. Reading load: 120-290 prose words per core page; the weakest reader depends on a partner; have the tutor read Q1-Q2 aloud and shorten the 45-word fast-track box.
9. Keep: inclusive openings, "Mei says" error framing, strategy praise, the look-back (make it optional to share and add "I was not stuck"), certificate with specific praise.
10. Does the diagnostic place children correctly? Mostly: it separates the strong from the weak, but as printed it tells about 84% of typical 7-year-olds to "expect support" or take a taster, and it cannot see rushing; the band change above fixes most of that, and the K2/P1 gap needs a plain-language route for weak starters.

Files: this report `docs/audit/journey_p1.md`, helper `docs/audit/journey_p1.py` (reading-load counts, diagnostic simulation, arithmetic checks, heatmap).
