# Student journey review: Math Inquirers P6 (ages 11-13, maths + coding bridge)

Date 2026-10-22. Read-only review. Files written: this report and `docs/audit/journey_p6.py` (heatmap means, answer checks and placement probabilities; run with `python3 -I docs/audit/journey_p6.py`).

## 0. Method, scale and limits (read first)

- **What I read:** `docs/gifted_research.md`, `docs/levels_and_placement.md`, `p6/SPEC.md`, all ten `p6/content/lN.js` (lesson, script, deck, qbank, workbook, plus `gaps.json`: warm-up check, open investigation, reflection line), `p6/workbook_html.js`, `diag/content/p6.json`, `diag/build_diag.py`, and the printed P6 placement PDF. I parsed all 281 P6 slides (`split/p6l1..10`) for minute labels and word counts, read the full text and speaker notes of the check, warm-up, explore, set-up, teaching, worksheet, stretch, challenge, talk, exit, reflect and showcase slides for L1, L3, L5, L6, L7, L8 and L10 (and the check and reflect slides of the rest), and rendered workbook pages 3, 5, 6 and 7 (L1, L2) to see what a child actually sees. The earlier `audit_p6.md` covered correctness; I did not repeat it, but my own checks of the diagnostic answers all passed (Part 2).
- **These are simulations, not observations.** No child used the material. Every score is my judgement from the text. The diagnostic probabilities in Part 2 rest on per-question success rates that I estimated (stated in the script); treat them as scenarios, not data.
- **Scale deviation:** the brief says "5 best" and also "3 = just right" for difficulty fit. A mean of six scores needs one direction, so **I score fit 5 = just right** and write **H (too hard)** or **E (too easy)** in the note.
- **Score order everywhere:** P = can participate, D = difficulty fit, F = fun and interest, C = confidence and self-esteem, M = motivation, S = social/online experience.
- **Persona definitions used.** LOW: post-PSLE, school maths is hard, slow reader and writer, shaky multiplication and division facts, has done only a little Scratch at school, discouraged easily. MID: typical, knows Scratch basics, needs support on new ideas. HIGH: fast, may code already, bored by repetition, rushes.
- **Things I could not check:** the Scratch editor itself (no starter `.sb3` files exist anywhere in the repo, so I could not open or test them); the MOE syllabus (school-year placements below are my belief, to verify); how a real tutor spends the minutes.
- **Verified against MOE syllabus (Oct 2025):** the school-year placements in this file were checked against the PDF. Two are wrong as written: warm-up W4 (speed) is not P6 school content, because "speed" is in no primary year (rate is P5, p. 41); and W2 (discount) is a **P5** topic (Percentage 1.4, p. 41), not P6. The simulated "wrong about 1 time in 5" for a pre-PSLE P5 child therefore rests on W2 and W4 being harder than the syllabus makes them for that child; treat that figure as overstated. Other placements (percentage change and finding the whole P6, p. 43; average P6, p. 44) hold. Full list: `docs/moe/verification_report.md`.

## 1. Part 1: lesson-by-lesson journey

### 1.1 Heatmap (mean of the six scores; computed in `journey_p6.py`)

| Lesson | LOW | MID | HIGH | Lesson mean |
|---|---|---|---|---|
| 1 Code the Pattern | 2.67 | 3.67 | 3.83 | 3.39 |
| 2 Prime Hunters | 2.50 | 3.50 | 4.00 | 3.33 |
| 3 Below Zero | 3.33 | 4.17 | 3.83 | 3.78 |
| 4 Algebra Machines | 2.50 | 3.67 | 4.00 | 3.39 |
| 5 Every Possible Way | 3.00 | 4.00 | 4.17 | 3.72 |
| 6 Fair or Unfair? | 3.00 | 4.33 | 4.33 | 3.89 |
| 7 Turtle Geometry | **2.17** | 3.50 | 4.33 | 3.33 |
| 8 Secret Codes | 3.00 | 4.17 | **4.50** | 3.89 |
| 9 Data Detectives | 3.33 | 4.17 | 3.33 | 3.61 |
| 10 Showcase Challenge | 2.33 | 3.50 | 4.17 | 3.33 |
| **Level mean** | **2.78** | **3.87** | **4.05** | |

Level mean by dimension (P / D / F / C / M / S): LOW 3.3 / 2.2 / 3.4 / 2.4 / 3.0 / 2.4; MID 4.2 / 3.4 / 4.3 / 3.5 / 4.1 / 3.7; HIGH 4.9 / 3.1 / 4.4 / 4.0 / 4.3 / 3.6.

**Reading the pattern:** the programme is fun for everybody (fun 3.4 to 4.4) and the low-floor entries mostly work, but the LOW child scores worst on difficulty fit, confidence and social experience in every lesson, and HIGH scores worst on fit (3.1), because 13 to 17 minutes a lesson are whole-group teaching and 5 minutes are check-together.

### 1.2 Per-lesson notes (three lines each, then the moments that go wrong)

#### Lesson 1: Code the Pattern
| | P D F C M S | Evidence |
|---|---|---|
| LOW | 3 2 3 3 3 2 | Win: wb p3 Q1 hands over cell 1 and 7, 10, 13, 16 is pattern-copying. Lost: the Warm-up check (min 2 to 5, taxi $3 + $2/km for 20 km) tests the lesson's new skill before it is taught and boards go up together; `warm1` "Next!" race is typed in chat; wb Q2 is 4 sequences x 3 answers (incl. 0.5n) in `ws1` 44-54. (H) |
| MID | 4 4 4 3 4 3 | `explore1` "predict pattern 100, do not build it" is a real hook; `we1` steps revealed after a prediction; `try1` a-c on whiteboards; check Q1 is 50/50, a public wobble that recovers. |
| HIGH | 5 3 4 4 4 3 | Passes the check, gets the private "start on Think Harder at minute 40", but first sits through `teach1`/`we1`/`try1` (25-35) on 3n + 2 that the table already showed at min 12, then works about 30 min alone; Think Harder and Challenge fit (E for core, right for Challenge 6 "in BOTH sequences"). |

Moments: low child at min 2 (check) feels stupid; at min 56-59 (`teachtrace`, `teachplan`, `teachbug`, three teaching slides inside the worksheet block) everyone waits and then the page-2 time shrinks to 13 min.

#### Lesson 2: Prime Hunters
| | P D F C M S | Evidence |
|---|---|---|
| LOW | 3 2 3 2 3 2 | Win: sieve on the 1-100 grid (`explore1`) is tactile and certain. Lost: `warm1` "first pair to say them all wins the card" needs 24 and 30 factor pairs fast; check Q1 uses "prime" before it is taught; `we3` adds mod + if + counter in about 3 min; ws2 has Q3-Q6 (about 35 answers) in `ws2` 61-72; exit asks "Is 133 prime?" which needs 133 ÷ 7 = 19 in the head. (H) |
| MID | 4 3 4 3 4 3 | The "91 looks prime but is 7 x 13" reveal (`teach1`) and Goldbach pairs are good; the grid must be hand-drawn if not printed (`lesson.online` assumes a print); wb Q5(a) "every number to 50 with exactly 3 factors" is a grind. |
| HIGH | 5 3 4 4 4 4 | "Why stop at 7?" (`explore2`), Think Harder 3 (100 as two primes) and the "Ali: two primes never add to a prime" investigation are the best items in the level; the 25-35 teach on factor pairs is known to him. |

#### Lesson 3: Below Zero
| | P D F C M S | Evidence |
|---|---|---|
| LOW | 4 3 4 3 3 3 | Best-pitched lesson: `warm1` five cities ("Nine is bigger than seven, so which is colder?") invites a wrong-then-right argument; ws1 is paper-only; Q1 reading A, B, C off the line is a first-3-minute win; Q6 "find Siti's bug" normalises error. Lost: check Q1 (freezer -18 to fridge 4) is public; Scratch minus key trap (slides use U+2212, a pasted minus is rejected, `lesson.online`); Q4(e)(f) double negatives. (slightly H) |
| MID | 5 4 4 4 4 4 | Number line + "split the jump at 0" + "a - b is the jump from b to a" are clear; every question has a context (Harbin, lift, diver). |
| HIGH | 5 3 4 4 4 3 | Core is E; Q4(e)(f) and Think Harder 1-4 fit. The printed Challenge 7 (qbank item 9: "no level 0, do not use a number line with 0") contradicts wb Q6 two pages earlier ("0 = ground floor"): a justified argument in a lesson about not being confused. |

#### Lesson 4: Algebra Machines
| | P D F C M S | Evidence |
|---|---|---|
| LOW | 3 2 3 2 3 2 | `warm1` tutor-as-machine is safe (call any number). Lost: `explore1` needs nested operator blocks (answer * 3) + 2 built in Scratch, then the partner "writes the rule using as few IN numbers as possible"; wb Q1 (find 3n + 3 or 5n - 2 from a table; (c) steps IN by 2) has no one-step warm entry; Q7 number trick needs (n + 5) x 2 = 2n + 10. (H) |
| MID | 4 3 4 3 4 4 | Guess-my-rule in breakout rooms with screen share is fun; Q2 "same steps, different order" is an aha; backwards-then-check is taught step by step (`we2`, `try2`). |
| HIGH | 5 3 4 4 4 4 | Rule-finding is instant (E); Q7 trick, Think Harder 3 (both machines agree) and the "find all machines" investigation fit; 25-35 teach is waiting. |

#### Lesson 5: Every Possible Way
| | P D F C M S | Evidence |
|---|---|---|
| LOW | 3 2 4 3 3 3 | Win: bubble tea list on paper (`explore1`); Q5 grid "left + below" addition is mechanical and doable. Lost: `warm1` "pages 15 to 40" race; the starter "Every Order" `.sb3` must be loaded from chat and a second repeat dragged inside the first; Q1(c) "fewest extra shorts for at least 40 outfits"; ws2 Q4-Q6 about 25 answers in 11 min (`ws2` 61-72). (H) |
| MID | 4 3 5 4 4 4 | Handshakes "is 5 x 5 right?" is the high point; fix-first-choice listing makes the multiplication rule obvious; the nested-loop trace (Q3) is the one hard moment. |
| HIGH | 5 3 5 4 4 4 | Handshake program with `a < b`, grid routes (discovers the add-up pattern), Think Harder 2-3 (3-digit numbers, a six-team league). Core is E. |

#### Lesson 6: Fair or Unfair?
| | P D F C M S | Evidence |
|---|---|---|
| LOW | 4 2 4 2 3 3 | Win: Dice Race (`explore1`) is a real game with a surprise; Q1(a) 3/8. Lost: probability is new (lesson note says so); `warmIntro` "you have 20 seconds per card"; Q1(d) "362 reds: is my program wrong?" needs "random is not exact"; Q3(b)(c) adding counters to reach 1/2 and 1/5 is algebra in disguise; Q4 is a 21-cell table plus 4 sub-questions. (H) |
| MID | 5 4 5 4 4 4 | Predict, play, pool the group tallies, explain with 36 outcomes is the best arc in the level; "Mei: 7 heads in 10" is a good talk question. |
| HIGH | 5 3 5 4 5 4 | Difference Game fairness, "two outcomes is always fair" investigation: genuinely puzzling. Core is E, saved by the fast track. |

#### Lesson 7: Turtle Geometry
| | P D F C M S | Evidence |
|---|---|---|
| LOW | 2 1 3 2 3 2 | Lost early: `setup` (10-11 min, 125 words: Pen extension, 4 set-up blocks, x:-50 y:100, move sizes, the clockwise arrow); "Turtle says" standing on camera; wb page 1 opens with a paragraph of set-up plus a 6-row table with new words (turn, inside angle, total turning); ws2 Q3-Q5 is a 9-row trace, a 10-cell table and "360 x times round / points" (about 45 answers in 17 min). Typing 60 for the triangle is a designed safe surprise. (very H) |
| MID | 3 3 4 3 4 4 | Drawing is satisfying; "predict then run" for pentagon and hexagon; heavy vocabulary but `teachstar`, `we3` help; ws2 is tight. |
| HIGH | 4 4 5 4 5 4 | Stars and the rosette are the program's most visual maths; the printed Challenge 5 ("design your own star, p and k share no common factor") is excellent. |

#### Lesson 8: Secret Codes
| | P D F C M S | Evidence |
|---|---|---|
| LOW | 4 2 4 2 3 3 | Win: `warm1` clock jumps (everyone answers on boards); code-strip explore is mechanical spy-fun; wb opens with a printed A-Z number strip. Lost: Q1(b)(c)(f) need 41 mod 12, 4 - 9 + 12 and 100 mod 26 mentally; Q2(b) decode with wrap; Q4 crack = decode 25 letters; the Scratch cipher needs the `.sb3` "alphabet" starter; longest wb text of the level (452 words, incl. a 10-line Python corner). (H) |
| MID | 4 3 5 4 5 4 | "What happens at X, Y, Z?" discovery; Q4 "which 3-letter word appears twice -> THE" is a true detective moment; "shift 26 does nothing" talk. |
| HIGH | 5 4 5 4 5 4 | Best fit of any cell: Q4 crack, Think Harder 4 ("decode BYFFI, shift 20"), printed Challenge 5 ("write a message and explain how a friend could crack it") and 7 (jumps of 5 vs 4 on a clock), the investigation "two shifts that sum to 26", ROT13. |

#### Lesson 9: Data Detectives
| | P D F C M S | Evidence |
|---|---|---|
| LOW | 4 4 3 3 3 3 | Familiar PSLE content: Q1 (4, 7, 2, 8, 9 -> 6) is a sure win and the first 10 min are comfortable. Risk: `script.hook[0]` "even your PSLE results come with averages" lands on a child who has just had results. Q4 154 ÷ 7 needs division; lists in Scratch are new. |
| MID | 5 4 4 4 4 4 | Quick-eye estimate; the misleading mean in Q4 ($22 vs median $15) is a good aha; trace table and Q6 blanks manageable. |
| HIGH | 5 2 3 4 3 3 | Core is revision (mean, total = mean x n): `warm2`, `we1`, `we2`, ws1 Q1-Q3 are done in the head (E). Value is only median/mode, lists and Challenge "mean of 1 to 99". Highest boredom risk in the level. |

#### Lesson 10: Showcase Challenge
| | P D F C M S | Evidence |
|---|---|---|
| LOW | 3 2 3 2 3 1 | Cold-called relay at min 0 ("name someone else": L2 factor tree, L4 backwards machine, L8 "3 o'clock + 20 hours"); team points tallied "in the chat or on the board" (`explore1` notes); Q1-Q3 are 15 answers in 12 min; showcase puts the child in front of 7 peers with "two stars and a wish". Wins: "a working copy of one starter with one change is full marks", plan-only presenters allowed, the certificate. |
| MID | 4 3 4 3 4 3 | Challenge round with check/reason points gives structure; starter + one twist is a sensible target; 3 min is doable but the "wish" adds mild pressure. |
| HIGH | 5 3 5 4 5 3 | Building and presenting his own puzzle is the draw. But after presenting he waits up to 20 min as audience (`showcase` 62-87) and 8 x (3 min + 20 s) = 26.7 min does not fit the 25-min slot. |

### 1.3 The new items: warm-up check, fast track, open investigation, reflection

**Warm-up check (`check` slide, all 10 lessons).**
- It is a **pre-test of the lesson's own new skill** (L1 taxi 2 x 20 + 3 before the nth term is taught; L2 "is 31 prime"; L4 "write the cost for n GB"). Most children cannot do it, in front of the group, within the first 5 minutes of every lesson. The tutor note "read every board before you say who is right" is good practice but online the boards are held to the camera so all 8 see every wrong answer.
- Timing collision: the check is "minutes 2 to 5", but `warm1` is labelled 0-5 and `warm2` 5-10; the note says "play the game for about 3 minutes and ask only the first three quick questions". L10 has a 5-minute warm-up with the check inside it. The tutor will cut the game or rush the check.

**Fast track: does it label or embarrass? Partly, yes, though the tutor-side design is careful.**
- Good: the tutor message is private; the note says "never say advanced or top group", "do not record this as a mark", "you can move any time", everyone joins Talk time and exit.
- Not good: (1) every lesson's first worksheet page prints a criterion in the header (`workbook_html.js`, `FASTPTR`): "Warm-up check: both right and can explain why? Fast track: go to the Think Harder pages." A child who got it wrong is reading, in print, that they did not qualify. (2) The Think Harder page opens with a green box "FAST TRACK. Did you get BOTH Warm-up check questions right AND explain why?". (3) The second Think Harder page is headed **"Challenge (for strong thinkers)"**: a label on the page. (4) The tutor says "some of you will start on a different page today, it changes every lesson", but the check sorts by prior knowledge of the new topic, so it will be the same children most weeks. (5) The fast-track child works about 30 min solo on the hardest material with no check-together slot: `stretch`, `challenge`, `chdiag`, `chwalk` have no minute label in any lesson (L9 `challenge` says 62-75, overlapping `ws2` and `ws2ans`), and the tutor is teaching the main pages.

**Open investigation: good tasks, hidden.** Examples are low-floor (L3 "find all pairs from a list", L5 "50 cents in 5c/10c/20c coins", L4 "find all the machines"). But it is the last box on the second Think Harder page, in no slide, with 3 answer lines, no sharing slot, and the same page as the "for strong thinkers" label. Only the fast-track child reaches it, nobody discusses it.

**Reflection ("What was hard?"): safe in intent, with six faults.** Intent is right: private ("Nobody marks this"), share optional, "pass is fine", strategy praise, never read out without consent. Faults:
1. **Typo in every lesson:** the notes say `say "you you drew a number line, ..."` (slides `p6lN-reflect` and `p6/guide.js` line 158 add "you" before `reflectEx`, which already starts with "you"). A tutor reading it aloud says "you you".
2. The box is on the **last page of the lesson, the Think Harder page headed "Challenge (for strong thinkers)"**: the page a low child has not opened.
3. It runs at minute 88 "while you collect the exit tickets": the tutor is busy.
4. Stems are all about hardness. A discouraged child writes "everything" or "I'm bad at maths" and the notes give no reply.
5. Sharing 2-3 children for one sentence tends to pick the confident.
6. There is no stem for success.

### 1.4 Concrete moments flagged

| # | Lesson, where | Who | Flag | Fix |
|---|---|---|---|---|
| 1 | All, `check` min 2-5 | LOW, MID | feel stupid: new-skill puzzle, boards up together | send answer and reason by private chat; tutor reveals only after |
| 2 | All, wb page-1 header | LOW | labelled: prints the fast-track criterion | delete the header text (see weak cell fixes) |
| 3 | All, wb "Challenge (for strong thinkers)" | LOW, MID | labelled | rename |
| 4 | All, `reflect` notes | tutor | "you you" typo | drop "you " in the template |
| 5 | L1 `warm1`, L2 `warm1`, L5 `warm1`, L9 `warm1` | LOW | rushed: "first team", "teams race", "closest gets a point" | no race wording |
| 6 | L6 `warmIntro` | LOW | time pressure: "20 seconds per card" | "take as long as you need; point to the line first" |
| 7 | L2 exit (a) "Is 133 prime?" | LOW | lost: 133 ÷ 7 in the head | use 111 (3 x 37) |
| 8 | L2 ws2 (35 answers, 11 min), L5 ws2 (25), L6 ws2 (Q4 21 cells), L7 ws1/ws2 (45) | LOW | rushed | cut core by about a third, move the rest to Think Harder |
| 9 | L3 `lesson.online` minus sign | LOW | lost: a pasted minus is rejected, the child thinks they are wrong | tutor says it out loud at min 10, and on the slide: "Type the minus key. Do not copy-paste." |
| 10 | L3 printed Challenge 7 (qbank item 9) vs wb Q6 | HIGH | confusion: level 0 or not | prefix the challenge: "In some Singapore buildings there is no level 0. (Q6 on page 2 uses 0 for the ground floor.)" |
| 11 | L4 `explore1` nested operator blocks | LOW | lost: drag-drop of reporter blocks | send a pre-built "Machine" project, child edits two numbers |
| 12 | L5, L8, L9, L10 `.sb3` starters loaded "File, Load from your computer" | LOW | lost, left out: file must reach each child (chat file share), none exist in repo | ship files + 1 page "How to load" |
| 13 | L7 `setup` slide, 125 words | LOW | lost: reading load, unexplained notation | split; see weak cell 1 |
| 14 | L7 `warm1` "Turtle says" standing | LOW, MID | left out, embarrassed on camera | "stand or use your arm" |
| 15 | L8 Q4 crack 25 letters | LOW | rushed | give the shift once the word is found, decode only the first word in core |
| 16 | L9 hook[0] "even your PSLE results" | LOW | discouraged | delete the phrase |
| 17 | L9 core | HIGH | bored, waiting: 25-40 teach is PSLE revision | skip to the median/mode and list code; fast-track by exit ticket of L8 |
| 18 | L10 `warm1` cold call by name | LOW | feel stupid | "ask someone who has not had a turn, or say pass" |
| 19 | L10 team tally in chat | LOW | feel stupid | tally on the team's own page |
| 20 | L10 showcase 62-87 | HIGH, all | waiting: audience for up to 20 min; 26.7 min needed for 8 | two half-groups; see weak cell 2 |
| 21 | All, `stretch`/`challenge`/`chwalk` no time slot | HIGH | waiting with no feedback | add a minute label (72-75, replacing the `ws2ans` check for the fast track) |
| 22 | All, open investigation | HIGH, MID | left out | move to Talk time (see 1.5) |
| 23 | L7, L8, L9 workbook Python corner | LOW | lost: wall of code in a box on page 2 | keep; add "optional, for children who already code" (the text says optional; make it visibly secondary: grey, smaller) |
| 24 | L1 `try1` c "7n - 6" | LOW | prior skill: 7 times table to 28 and a "take away" rule | fine (taught), keep |

### 1.5 The five weakest lesson-persona cells, with fixes

Ties: L2-LOW and L4-LOW are both 2.50; ordered by severity.

**1. L7 LOW (2.17).** Too many new words and set-up steps, then too many answers.
- `p6l7-setup` slide: replace the 125-word slide with: "Step 1. Click the blue Add Extension button (bottom left) and pick Pen. Step 2. Build these 4 blocks and keep them at the top of EVERY drawing." Move the stage-size explanation and the "sizes that fit" list to the notes; show the size on each slide where it is used.
- Tutor sends a `Turtle start.sb3` that already contains the 4 set-up blocks (children load it).
- wb page 1: add a 3-line box at the top: "**turn** = how far the turtle swings at a corner. **inside angle** = the angle inside the shape at that corner. **total turning** = all the turns added up."
- wb Q3: pre-fill the first 3 rows of the 9-row trace ("The first 3 rows are done for you"). wb Q4: keep the 5-point row filled, the 9-point row as core, and move the 20-point row to Think Harder.
- `warm1` "Turtle says": "Stand up, or sit and use your arm as the turtle's nose."

**2. L10 LOW (2.33).** Cold calls, public scoring, a showcase with no exit ramp.
- `warm1` notes: "Read card L1 and name a child" becomes "Read card L1 and ask for a volunteer; the child who answers asks the next card and invites someone who has not had a turn. 'Pass' is always fine, and the next person helps."
- `explore1`: "Keep a team tally in the chat or on the board" becomes "Each team keeps its own score on page 1. Show it only if your team wants to."
- `showcase`: audience feedback "two stars and a wish" becomes "two stars and a question"; tutor posts stars first. Run it as **two rounds of 4** with the audience's job set (write one question for each presenter), so nobody waits more than 12 minutes and 8 x 3 min 20 s is no longer squeezed into 25 min. Add: "You can show a screenshot and I will run your file."
- Q1 to Q3 of the challenge round: cut Q3 to parts (a) to (d); (e)(f) are Think Harder.

**3. L2 LOW (2.50).** Racing, a heavy new idea set, an exit that needs mental division.
- `warm1` notes and slide: "First pair to say them all wins the card" becomes "With your partner, find every factor pair for each card. A point for each pair you can explain."
- check Q1 (L2 `gaps.json` `check[0]`): add "(A prime has exactly two factors.)" before the question.
- Exit ticket (`l2.js` `exit.q`): "(a) Is 133 prime? Show your test." becomes "(a) Is 111 prime? Show your test." with key "No. 1 + 1 + 1 = 3, so 3 divides it: 111 = 3 × 37." Add an optional "(c) Is 133 prime?" for those who want it.
- wb Q5(a): "All the numbers from 1 to 50" becomes "All the numbers from 1 to 30 with exactly 3 factors (4, 9, 25 expected)"; keep 50 for Think Harder.

**4. L4 LOW (2.50).** No one-step entry to rule-finding; reporter-block building; the algebra trick.
- wb Q1: add a new first row (a): "IN 1, 2, 3, 4 give OUT 4, 5, 6, 7. Rule: OUT = n + ___. OUT for IN 10 = ___." and re-letter the rest. (c) (steps IN by 2) gets: "Careful: IN goes up by 2 here, so OUT goes up by 2 x the number."
- `explore1`: tutor sends a pre-built `Machine.sb3`; instruction becomes "Change the 3 and the 2 to numbers of your own."
- wb Q7(b): pre-fill the first three boxes ("n → n + 5 → 2n + 10 → ___ → ___ → ___").

**5. L1 LOW (2.67).** The first lesson sets the tone and begins with a pre-test.
- `check` slide notes: "Everyone writes the answer AND one reason on a whiteboard ... Hold up together" becomes "Everyone sends their answer and one reason to the tutor by private chat. Do not read wrong answers aloud. Reveal the answers, then say: 'Both of these are what we learn today.'"
- `warm1`: "First team to say the next two terms wins a point" becomes "Type the next two terms in the chat. One point for every rule you spot."
- wb Q2: keep (a) (b) as core; (c) (d) move to Think Harder.

**Level-wide fixes that move all five:**
- Delete the printed header text on every first wb page: replace `FASTPTR` with "**Think Harder pages:** start here when you finish early or whenever you feel ready."
- Think Harder FAST TRACK box: "FAST TRACK. Did you get BOTH ... AND explain why?" becomes "**Starting here today?** Your tutor may ask you to. You can also start here when you finish the main pages. You can go back to the main pages at any time."
- "Challenge (for strong thinkers)" becomes "**Challenge**".
- Reflection: move the "What was hard?" box from the Think Harder page to the bottom of the second core worksheet page; fix "you you"; add a fourth stem "**One thing I did well today was ...**"; add to the notes: "If a child writes 'everything' or 'I'm bad at maths', say: 'Thank you for telling me. Let's find one small thing that worked today.' and point to a specific item they got right."
- Move the open investigation to Talk time: replace the Talk-time question on one lesson in two with the investigation so it is shared; on Think Harder page 1, add: "**Choose one:** Stretch 1 to 4, or the Open investigation."

### 1.6 The three strongest cells (with the shared reason)

1. **L8 HIGH (4.50).** Cracking a code from "which 3-letter word appears twice" is a real puzzle; Challenge items are open and discovered, not given.
2. **L6 MID and L6 HIGH (4.33 each).** Predict, play, pool the group's tallies, explain with 36 outcomes. Surprise, not error; the "fair?" question is genuinely arguable.
3. **L7 HIGH (4.33), tied.** Drawing stars and rosettes, and a rule he can discover (turn = 360 x k / p).
Common to all: the child predicts first, then something happens on screen that confirms or contradicts, and "explain why" has a concrete thing to explain.

### 1.7 Level-wide patterns

- **Pacing.** Whole-group teaching (teach, worked example, try, key slides) is 13 to 17 minutes a lesson; worksheet 23 to 27 minutes (L10: 37); check-together 5 minutes; plus 7 minutes of teach slides sit inside the worksheet block. The core worksheets carry roughly 35 to 45 answers on L2, L5, L6, L7 (earlier audit's count; I agree after reading the pages), so the LOW child is "rushed" by design in about 4 lessons, and the HIGH child is waiting through the same slides.
- **Reading load.** Sentence length is fine: slides are 40 to 140 words, wb core pages 240 to 450 words, Think Harder items 13 to 25 words. The load is **notation and vocabulary**: n, 3n + 2, mod, inside/turn/point angle, "total turning", "times round", item i of list. L7, L8, L4 are worst. L8 and L9 have the heaviest wb text because of the Python corner.
- **Wait time for HIGH.** About 13 to 17 min of teach slides on ideas he often has, 5 min check-together, 7 min talk; fast track fixes some of it but moves the problem to 30 unsupported minutes with no feedback slot and an investigation nobody discusses. L9 is worst (core is PSLE revision).
- **Guaranteed win in the first 10 minutes of the worksheet (LOW)?** Yes in L1 (Q1 table), L3 (Q1 read the line), L5 (Q1a 12), L6 (Q1a 3/8), L8 (Q1a 8 + 7), L9 (Q1 total and mean). Partly in L2 (Q1 31 and 1 are easy, 28 and 51 are not, and 1 is a trap). **No** in L4 (Q1 needs the rule from a table), L7 (page opens with set-up plus a 5-row table in new words), L10 (challenge round Q1 is a hexagon rule). So 6 of 10 yes, 1 partly, 3 no.
- **Competition and public answers.** Race or points wording in `warm1` of L1, L2, L5, L9 and L10's team tally; "hold up together" every lesson; `warmIntro` timer in L6. For a child who is anxious about being wrong, the set of public moments is dense in the first 10 minutes.
- **Scratch dependency.** The SPEC says a 10-minute Scratch warm-up video or handout is sent before lesson 1. I found none in `p6/`, `outputs/` or the Program Guide. The starters for L5 (`Every Order`), L8 (`alphabet` list), L9 (`data` list) and L10 (A to D) exist only as slide drawings (earlier audit item 7 says the tutor must build them). A child with little Scratch cannot take part in the min 10-25 explore in L1, L4, L5, L7. Participation (P) for LOW averages 3.3, among LOW's better scores, because the maths entries are low-floor, but "can use the tool" is the unmeasured hidden prerequisite.
- **Strategy feedback.** Mostly good: "praise the strategy, not the speed"; named characters (Ali, Ben, Mei) who are wrong in a way worth examining; "find the bug" items; sentence starters in Talk time. This is the best feature for confidence and is why LOW confidence is 2.4, not 1.5.

## 2. Part 2: the diagnostic check

### 2.1 (a) True skill demand and fairness of each question

Source: `diag/content/p6.json`; answers re-derived in `journey_p6.py` (all 12 correct; S2 checked by enumeration: 12 even numbers out of 24 three-digit arrangements). School-year placement is my belief of the MOE syllabus (verify).

| # | Question | Skill and steps | Believed school year | Fair for 11-13? | Notes |
|---|---|---|---|---|---|
| W1 | 2 1/2 - 3/4 | regroup or convert, 2 steps | P4-P5 | yes | clear; "fraction or mixed number" answer form is explicit |
| W2 | $60, 25% off | percentage of a quantity, subtract, 2 steps | P5; discount P6 | yes | also in the P5 programme (P5 L7) |
| W3 | triangle 52, 63 | 180 - 115, 1 fact, 2 subtractions | P4-P5 | yes | easiest item; P5 programme L8 |
| W4 | 135 km in 1 h 30 min | speed: convert 1 h 30 to 1.5, divide by a decimal | P6 | **no for a pre-PSLE 11-year-old** | speed is P6 school content and not in the P5 programme (P5 L6 is "rate"); hardest warm-up |
| C1 | doubles, +5, output 31 | work backwards, 2 steps | P5-P6 heuristic | yes | taught in L4 |
| C2 | primes between 30 and 50 | needs the word "prime" and a scan of 20 numbers, test 3 and 7 (49) | not primary (believed) | **only with the term defined** | tests exposure; about 3 min |
| C3 | -4, +9, -12 | negative numbers across zero | not primary (believed) | yes, context helps | taught in L3 |
| C4 | NOT green, 4 R 3 B 5 G | probability, 2 steps | not primary | **only if the term is defined** | "picked at random", "probability" undefined |
| C5 | "mean" of 5 numbers | total = mean x n, missing value | P5-P6 as "average" | **vocabulary gate** | Singapore pupils use "average"; word "mean" is secondary |
| C6 | 10 o'clock + 17 hours | elapsed time and wrap | P3-P4 time, mod idea | yes | clear; traps 27 and 5 |
| S1 | robot, 6 x 90 clockwise | quarter turns, compass | P4 | yes but not a stretch | 25% guessable (N, E, S, W); many strong children get it in 20 s |
| S2 | 3-digit even from 1-4, no repeats | systematic listing or 2 x 3 x 2 | not primary | yes, a good discriminator | taught in L5 |

**The central finding:** the 8 scored questions map one-to-one to lessons 2 to 9 (C1 L4, C2 L2, C3 L3, C4 L6, C5 L9, C6 L8, S1 L7, S2 L5). The diagnostic's own "Skills covered" list on the parent page confirms it. A child who scores 0-3 is a child to whom the lessons will be new, which is exactly who the lessons are written for. The scored part measures **prior exposure to what we teach**, not readiness to learn it. Meanwhile the real readiness skills (times-table and division fluency, simplifying fractions, a letter standing for a number, reading a short block program) are barely tested, and Scratch is not tested at all.

**Are the warm-ups "from the level below"? Not consistently.** Comparing with the P4 and P5 diagnostics: P4's warm-up is P3 content, P5's is P3-P4 content, P6's is P4-P6 content (W4 speed is P6). The ladder drifts upward by one year at P6. W2 and W3 map to the P5 programme; W1 is plausible; W4 is not in it.

### 2.2 (b) Six profiles through the diagnostic

Assumed per-question success rates are in `journey_p6.py` (`PROF`). Independent-question model (exact), with the current rule: 6-8 join; 4-5 join with support, or P5 if warm-up is 2 or less; 0-3 P5.

| Profile | E(warm-up /4) | E(main+stretch /8) | P(6-8) | P(4-5) | P(0-3) | P(P5 suggested) | Right level for the lessons? |
|---|---|---|---|---|---|---|---|
| Strong for age (12, post-PSLE) | 3.8 | 6.5 | 0.83 | 0.16 | 0.005 | 0.01 | Yes: P6. Only 15% reach 8/8 with 4/4, and there is **no level above P6**, so the "try the level up" line is absent from the P6 page (correctly), leaving the strongest child no next step. |
| Typical for age (12, post-PSLE) | 3.3 | 3.9 | 0.11 | 0.50 | **0.40** | **0.47** | **Wrong half the time.** The typical child is who the lessons target; the rule sends 47% of them to P5. With shared day-to-day noise it is worse (0.42 down). |
| Weak for age (12, post-PSLE) | 1.5 | 1.5 | 0.00 | 0.04 | 0.96 | 0.99 | Placement P5 is "defensible but not clearly right": P5 is a school-syllabus programme (areas, volume, rate, percentage, angles) a post-PSLE child has just sat; this child would struggle in L1, L2, L4, L7 (LOW persona mean 2.78) but would also be patronised in P5. The offer needs a third path (taster plus tutor chat). |
| Younger strong (11, P5, pre-PSLE) | 2.9 | 5.4 | 0.47 | 0.46 | 0.08 | 0.21 | **Wrong about 1 time in 5**, because W4 (speed) and W2 (discount) are P6 school topics, so 30% of them score 2 or less in warm-up. |
| Older weak (13, Sec 1) | 2.1 | 2.6 | 0.01 | 0.22 | 0.77 | 0.92 | The offered level, "Ages 10-12", is **outside his age band**, repeats P5 content he did at 10, and he may feel it as an insult. P6 with support is the better fit (he has seen negatives and primes at Sec 1). Wrong. |
| Rusher (capable, falls for traps) | 3.0 | 3.2 | 0.05 | 0.36 | 0.60 | 0.69 | Wrong: each question's "common error" in the tutor key (26, 7, 5/12, 27, 24, 39/49) is exactly the careless slip. He is placed as weak. |
| Pure guesser | 0.1 | 0.6 | 0.00 | 0.00 | 1.00 | 1.00 | Right: guessing cannot pass (P(4 or more of 8 by guessing) is 0.1%; the only guessable item is S1 at 25%). |

I am explicit that these rates are my estimates; the point they make does not depend on the exact numbers: the typical child sits right at the 4/5 vs 3 boundary.

### 2.3 (c) Cut scores: how reliable are 8 questions?

For a child with a fixed chance p on each of the 8 scored questions (exact, `journey_p6.py`):

| p | P(6-8) | P(4-5) | P(0-3) |
|---|---|---|---|
| 0.50 | 0.145 | 0.492 | 0.363 |
| 0.60 | 0.315 | 0.511 | 0.174 |
| 0.70 | 0.552 | 0.390 | 0.058 |
| 0.75 | 0.679 | 0.294 | 0.027 |
| 0.80 | 0.797 | 0.193 | 0.010 |
| 0.90 | 0.962 | 0.038 | 0.000 |

- A child who truly answers 75% of such questions (expected 6/8) lands **below the join line 32%** of the time and in the "down" band 2.7%. A child at 60% reaches "well challenged" 31.5% of the time by luck and "down" 17.4% by bad luck. The standard deviation of an 8-item score is about 1.4 marks and each band is only 2 or 3 marks wide, so **one question moves the recommendation**, and 3 vs 4 is a switch from "we suggest Ages 10-12" to "join P6".
- The 8/8 route to "try the level up" needs all 8; at p = 0.9 only 43% of such children get 8/8 (0.9^8). For P6 there is no level up anyway.
- The rule ignores the warm-up in the 6-8 band (a child with 6/8 and 0/4 warm-up is told "has the foundations and will be well challenged"), and the 4-5 band uses warm-up only as "2 or less". The warm-up is the better readiness signal and the main part the worse one, and the rule weights them in the opposite order.
- `docs/levels_and_placement.md` uses percentages (70% / 40-69% / under 40% / 90%); with 8 questions these equal the page's 6-8 / 4-5 / 0-3 / 8, so they agree, but the doc's "try one level up at 90%+" has no P6 target.

### 2.4 (d) Wording on the parent result page, tutor key and child sheet

Things that can discourage a child or parent:
1. **"Not yet?"** box (`build_diag.py` line with `<b>Not yet?</b>`): "That is useful to know, not a failure. Starting one level down means more success and more joy in class." It introduces the word "failure" and implies the child would otherwise have little success. For a parent of a post-PSLE child, "one level down" is "Ages 10-12 (P5)", a programme for children two years younger: easy to read as "behind".
2. **0 to 3 row:** "We suggest Ages 10-12 (P5)" offers no route other than down, with no mention of a tutor chat or taster for this level, although P1 has such a route.
3. **"Skills covered"** lists Primes, Negative numbers, Probability... on the parent page without saying these are what the lessons teach. A parent who sees them next to a low score reads a list of gaps.
4. **No reassurance on the child sheet** that some questions use new ideas ("How it works" says only "answer on their own... skip it"). A post-PSLE child meeting "prime", "probability" and "mean" with no warning can feel they should know them.
5. **The answer key is page 3 of the same PDF as the child pages**, headed "For the tutor or parent": if a parent prints the file, the answers print too. Its example "$2.05 and 2.05" is copied from another level.
6. **The page does not mention that half the programme is coding**, nor test it: a parent cannot judge fit.
7. Child-sheet header: "For children after the PSLE. Open to a year either side": a pre-PSLE 11-year-old reads it as not for them.
8. Positives: "You make the final choice" and "change level free of charge before lesson 1" are on the page; the "Common error" column in the key is useful and not shown to the child.

### 2.5 (e) Recommended changes (exact text)

**1. Make the scored questions self-contained, so the cut score measures reasoning, not exposure.**
- C2 becomes: "A prime number has exactly two factors: 1 and itself. For example, 7 is prime, but 9 is not (its factors are 1, 3 and 9). How many prime numbers are there between 30 and 50?" (answer 5 unchanged).
- C4 becomes: "A bag has 4 red, 3 blue and 5 green marbles. One marble is picked without looking. The chance (probability) of picking blue is 3 out of 12, written 3/12. What is the probability that it is NOT green? Give a fraction in simplest form." (answer 7/12).
- C5 becomes: "The average of 5 numbers is 12. Four of the numbers are 8, 10, 15 and 11. What is the fifth number?" (answer 16).
- S1 (robot, 6 turns) becomes a real stretch that also tests the L1 skill: "The pattern 4, 7, 10, 13, ... carries on. What is the 50th number? Explain how you worked it out." (answer 151, checked.)
- W4 becomes an item from the level below: "A rectangle has a perimeter of 36 cm and a length of 11 cm. What is its area in square cm?" (answer 77, already used in the P5 diagnostic and not P6 content) **or**, if keeping rate: "A tap fills 12 litres in 4 minutes. How many litres does it fill in 10 minutes?" (answer 30).

**2. Test the real prerequisites in the warm-up** (these four replace W1-W4 if the above two are not wanted):
- W1 "Write every factor of 24." (1, 2, 3, 4, 6, 8, 12, 24; L2 and L8.)
- W2 "Write 6/36 in its simplest form." (1/6; L6 and L9.)
- W3 "Two angles of a triangle are 52 and 63 degrees. What is the third angle?" (65; L7.)
- W4 "Read the code. set n to 5, then repeat 4 times: change n by 3. Then say n. What does it say?" (17, checked; the code is shown as three blocks. This gives the tutor a coding-readiness signal, to plan support, not to exclude.)

**3. New child-sheet reassurance, under "How it works":** "Some of these questions use ideas you may not have met yet. That is fine: we are working out where to start, not marking you."

**4. New placement table (parent page), replacing the current three rows:**

| Warm-up marks | What it suggests |
|---|---|
| 3 or 4 | Join **Ages 11-13 (P6)**. Your child has what they need to start. |
| 2 | Join **Ages 11-13 (P6)** and ask your tutor about a short catch-up chat before lesson 1. |
| 0 or 1 | Let's talk. We suggest the free taster and a tutor chat first. **Ages 10-12 (P5)** is also an option if your child is 12 or younger. |

and a second line for the main questions, with no level change: "**Main + stretch 6 to 8:** you will find some ideas familiar. Think Harder pages will suit your child. **3 to 5:** a good mix of familiar and new. **0 to 2:** most ideas will be new, which is what the lessons are for."

Replace the two boxes "Strong?" and "Not yet?" with one: "**This is a guide, not a grade.** Ask your tutor for a chat if you are unsure."

Retitle "Skills covered" as "**Ideas we explore in the lessons** (most children meet some of these for the first time)". Remove the "8 of 8 and 4 of 4, try the level up" line for P6 (already absent) and add: "If your child finds all of this easy, ask your tutor about the Challenge pages."

Under this proposed rule (warm-up decides; main+stretch only sets the note) my scenario model gives: strong 99% join; typical 86% join, 13% catch-up chat, 1.5% taster; younger strong 70% join; older weak 32% join, 40% catch-up, 28% taster. The typical child is no longer sent down by an exposure test. (`journey_p6.py`, last block; rates are my estimates.)

**5. Split the PDF** into a child sheet (pages 1-2) and a tutor/parent file (pages 3-4) so answers are not in the file the child sees. Replace the key's "$2.05 and 2.05" with "for example 1.75 and 1 3/4 do not both count here: the question asks for a fraction or mixed number".
**6. Add a time note** to "How it works": "There is no timer. About 30 minutes is plenty; stop when your child is tired." (12 questions in 30 min is 2.5 min each; the item C2 alone can take 3.)

## 3. Ten-line summary

1. **LOW (2.78/5):** at risk in L7 (2.17), L10 (2.33), L2, L4 (2.50) and L1 (2.67); fit, confidence and social experience are the weak dimensions (2.2, 2.4, 2.4); wins exist (L3, L6 Dice Race, L9 Q1) and strategy-based feedback is the best protection.
2. **MID (3.87/5):** well served everywhere; weakest L2, L7, L10 (3.50), mostly pace.
3. **HIGH (4.05/5):** engaged by L6-L8; weakest L9 (3.33, PSLE revision) and the 25-35 teach block everywhere; the fast track gives 30 min without feedback.
4. **Top 5 fixes:** (a) rewrite the diagnostic so the scored questions are self-contained and warm-up drives the rule; (b) remove public labels: private check answers, delete the printed fast-track criterion, rename "Challenge (for strong thinkers)", fix "you you", move the reflection box; (c) cut core worksheets by a third in L2, L5, L6, L7 and give the Think Harder items, the investigation and the check a minute label; (d) ship the starter `.sb3` files and a pre-lesson Scratch handout (none exist), pre-build the L7 set-up; (e) L9 hook ("PSLE results"), L10 relay, team tally and showcase structure.
5. **Does the diagnostic place children correctly? Mostly no.** It sends about 47% of typical children (in my scenario) to P5 and about 1 in 5 strong 11-year-olds, because its 8 scored items are a one-to-one pre-test of lessons 2-9.
6. It handles guessers well (P(pass by guessing) is about 0.1%).
7. Strong 12-year-olds are placed correctly (83% join), but have no next step above P6.
8. Weak and older-weak children are steered "down" to a school-syllabus programme for 10 to 12-year-olds that repeats content they have already sat; they need a taster and tutor-chat route.
9. Eight questions are too few for a hard cut: a child with a true 75% rate misses the join line 32% of the time; use the warm-up (readiness) to decide and the main part only for a note.
10. Candid verdict: the lessons are good and children like them (fun 3.4-4.4); the weak points are the entry gate, public labelling, over-full worksheets for slower children, and a Scratch dependency that nothing in the repo supplies.
