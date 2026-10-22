# Student journey review: Math Inquirers P5 (ages 10-12)

Date: 2026-10-22. Read-only review. Nothing in the repo was edited except this file and `docs/audit/journey_p5.py` (the helper that prints every number quoted here: `python3 -I docs/audit/journey_p5.py`).

Sources read: `docs/gifted_research.md` (rubric), `docs/levels_and_placement.md`, `p5/SPEC.md`, `p5/content/l1..l10.js`, `p5/content/gaps.js`, `p5/data.js`, `p5/workbook_html.js`, `p5/guide.js`, the built slide decks (`split/p5l1..p5l10/project/slides/*.html`, titles/notes/check/reflect/ws/stretch slides), the printed workbook text (57 pages), `diag/content/p5.json` (plus p4.json and p6.json for neighbouring levels), `diag/build_diag.py`. Every lesson's workbook pages 1-2, Think Harder pages, Challenge page, Open Investigation and reflection were rendered to text and read in full.

## How to read the scores

* No children were observed. The scores are my judgement from walking the real artefacts minute by minute. The personas:
  * **LOW**: finishing P5 at roughly 40-50% in school maths; unreliable on fractions of a quantity, unlike fractions and decimal division; reads slowly; gives up quickly if the first thing fails.
  * **MIDDLE**: roughly 65-70% in school; fine on routine items, needs worked examples, works well in pairs.
  * **HIGH**: top of the class; finishes first; bored by repetition; may rush and not check.
* Scores are 1-5, 5 best, in the order **Participate / Fit / Fun / Confidence / Motivation / Social-online**.
* **Fit** is reported as the brief asks: 3 = just right, 1-2 = too hard, 4-5 = too easy. For the heatmap means only, Fit is converted to "fit quality" (3 becomes 5, 2 or 4 becomes 3, 1 or 5 becomes 1) so that a perfect fit raises the mean instead of lowering it.
* Timetable used for "minute by minute" is the one printed in every deck's title-slide notes: check 0-3, warm-up 3-9, explore 9-21, teaching 21-33, break 33-37, worksheet page 1 (pairs) 37-49, check together 49-51, teaching before page 2 51-57, page 2 (alone) 57-72, check together 72-76, talk 76-82, exit ticket and reflection 82-90.

## Heatmap (mean of the six scores)

| Lesson | LOW | MIDDLE | HIGH | Lesson mean |
|---|---|---|---|---|
| 1 Million Puzzles | 3.00 | 4.17 | 3.50 | 3.56 |
| 2 Fraction Feats | **2.67** | 4.00 | 3.67 | 3.44 |
| 3 Before and After | **2.00** | 3.17 | 4.00 | 3.06 |
| 4 Triangle Areas | 3.50 | **4.50** | 3.67 | 3.89 |
| 5 Volume Vault | 3.00 | 4.17 | 3.83 | 3.67 |
| 6 Rate Racers | **2.17** | 3.67 | 3.83 | 3.22 |
| 7 Percentage Puzzles | 3.50 | **4.67** | 3.83 | 4.00 |
| 8 Angle Chasers | **2.83** | 4.00 | 4.00 | 3.61 |
| 9 Pattern Generalisers | 3.33 | 4.17 | **4.33** | 3.94 |
| 10 Challenge Day | **3.00** | 4.17 | 4.33 | 3.83 |
| **Level mean** | **2.90** | **4.07** | **3.90** | 3.62 |

Per dimension, level means (Participate / Fit quality / Fun / Confidence / Motivation / Social):
LOW 3.2 / 2.6 / 3.5 / 2.8 / 2.7 / 2.6. MIDDLE 4.1 / 4.6 / 4.3 / 3.7 / 3.9 / 3.8. HIGH 4.5 / 3.4 / 4.2 / 4.2 / 4.1 / 3.0.
The LOW child's weak columns are Fit, Confidence, Motivation and Social. The HIGH child's weak columns are Fit (too easy for the first 37 minutes) and Social (the fast track puts them alone).

## Part 1: lesson by lesson

Each lesson: scores for L(ow) / M(iddle) / H(igh), one evidence line per persona, and the moments flagged.

### Lesson 1: Million Puzzles

| | LOW | MID | HIGH |
|---|---|---|---|
| Participate | 3 | 4 | 5 |
| Fit | 2 (too hard from ws1 Q3) | 3 | 4 (too easy until ws1 Q3) |
| Fun | 3 | 4 | 3 |
| Confidence | 3 | 4 | 4 |
| Motivation | 3 | 4 | 3 |
| Social/online | 3 | 4 | 3 |

* **LOW**: Million Maker (slide `p5l1-warm1`, place digits in seven boxes, nothing to get wrong) and ws1 Q1(a)(b) are safe wins; but check Q1 "closest to 7000" (slide `p5l1-check`) needs "test both sides", which is only taught at minutes 21-33, so a likely 7369 held up at minute 2 with no "why"; ws1 Q3 is a six-clue riddle of about 80 words and ws2 Q6 is "find ALL" with digit sum 9, neither finishable in 12 and 15 minutes.
* **MID**: check answered on the second thought; explore (million seconds, `expSetup` 4 steps) gives a real "wow" (11.6 days); Q3 and Q6 are a good stretch, Q4 and Q5(a-c) are comfortable.
* **HIGH**: both check items right, yet the Fast track box (workbook page 1) only opens at minute 37, so minutes 3-37 are warm-up questions like "4 560 000 ÷ 1000" and a teaching sequence on ideas already shown in the check; Q1, Q4 take about 2 minutes each; Think Harder S1 ("how many 7-digit numbers have digits that add to 2") is where they finally think.

Flags
* Minute 0-3, LOW: a problem about an idea that has not been taught, hands up together on whiteboards (see "new items" below).
* Minute 9-21, LOW: 3600 × 24 is multi-digit; the materials list allows a calculator "for the explore only" but the online set-up never says every child has one.
* Minute 37-49, LOW: Q3 has six clues and the instruction "Start with the clue that fixes the most digits" (a reasoning strategy the child may not follow); a pair of two weak children has nothing to do once stuck.
* Minute 57-72, LOW: Q6 alone. No partner, no tutor time (tutor has 8 children), "write the range first" is a hint, not an entry point.
* Reading: 306 words on pages 1-2.

### Lesson 2: Fraction Feats

| | LOW | MID | HIGH |
|---|---|---|---|
| Participate | 3 | 4 | 4 |
| Fit | 2 (too hard) | 3 | 4 (too easy in core) |
| Fun | 3 | 4 | 4 |
| Confidence | 2 | 3 | 4 |
| Motivation | 2 | 4 | 4 |
| Social/online | 3 | 4 | 3 |

* **LOW**: pizza explore (3 paper pizzas among 4) is a true low floor and ws1 Q1(a) "5 pizzas among 8" is a guaranteed win with the reminder "a ÷ b = a/b" printed; but check Q2 (slide `p5l2-check`) asks for a bar and a fraction of the remainder at minute 1, and every trial in ws1 Q2 needs an unlike-fraction subtraction (7/10 − 1/2, 9/20 − 1/4, 3/8 − 1/3) that she cannot do fluently, in 12 minutes for three questions.
* **MID**: Face-off, explore and Q3 (bar for 240 stickers) are reachable; Q2(c) "find TWO ways for 3/8" and Q4(c) "predict the sum to 1/90" stretch but do not break.
* **HIGH**: Egyptian-fraction search, the telescoping sum (Q4, Investigation, Challenge Q5) are the best ideas in the level; still 34 minutes before the fast track opens.

Flags
* Minute 3-6, LOW: Face-off asks for a reason "without common denominators" after the one-finger vote; a guessed finger plus "why?" is exposed.
* ws1 Q1(c), LOW: "In which group does each child get more? 2/3 or 3/5" cannot be done without the common denominator the warm-up just banned.
* ws1 Q1(b), LOW: 9/4 m has no instruction whether to give 2 1/4 or an improper fraction.
* Q1(d) is marked "(stretch)" inside page 1, a visible rung inside the core page (good for HIGH, mildly pointed for LOW).
* Reading: 287 words.

### Lesson 3: Before and After

| | LOW | MID | HIGH |
|---|---|---|---|
| Participate | 2 | 3 | 4 |
| Fit | 1 (far too hard) | 2 (too hard) | 3 |
| Fun | 3 | 3 | 4 |
| Confidence | 2 | 3 | 4 |
| Motivation | 2 | 3 | 4 |
| Social/online | 2 | 4 | 3 |

* **LOW**: the counter-swap explore (Ali 18, Mei 6, table of Ali/Mei/total/difference) is excellent and concrete, but the check at minute 0 is an age problem ("3 times as old", slide `p5l3-check`) and the warm-up "What's left?" jar needs three fractions of a remainder in a row (120 to 90 to 60 to 10); ws1 Q1 asks the hardest sub-question first, (a) "what fraction of his money did he spend on the pen?" (1/6, a fraction of a remainder), with no easy opener; ws2 Q5 uses "blue is 2 out of every 5", never taught.
* **MID**: this is the one lesson where MIDDLE is also too stretched (Fit 2). Bar models with before/after plus a fraction is a P5/P6 heuristic; Q2 ("3/4 as many") and Q5 are where she is lost.
* **HIGH**: engaged and well fitted; the constant total / constant difference / constant amount triage is a real idea, the investigation "for which totals can Ali end with exactly twice as many" is a good generaliser.

Flags
* Minute 0-3, LOW: check C1 is 28 words with a 3-times relation and a "what stays the same?" prompt before any teaching.
* Minute 3-9, LOW: the warm-up script warns "Careful: read whether the card says of the whole jar or of what is left", i.e. a reading trap built into the game.
* ws1 Q1(a), LOW: no guaranteed win in the first 10 minutes of the worksheet (the "Start here: guess $60" line comes after (a) and is the better entry).
* ws2 Q3, Q4: "Ali must give me 20 marbles" and "Ali wants to give Ben some"; unexplained give/receive language for a slow reader (380 words on pages 1-2).

### Lesson 4: Triangle Areas

| | LOW | MID | HIGH |
|---|---|---|---|
| Participate | 4 | 5 | 4 |
| Fit | 2 (too hard on Q3-Q4) | 3 | 4 |
| Fun | 4 | 5 | 4 |
| Confidence | 4 | 4 | 4 |
| Motivation | 3 | 4 | 4 |
| Social/online | 3 | 4 | 3 |

* **LOW**: Half-or-not thumbs vote (`p5l4-warm1`) has no reading; cutting an 8 by 6 rectangle and covering the triangle with the two leftover pieces is understandable by sight; ws1 Q1(a) 1/2 × 8 × 6 = 24 is a quick win and Q1(d) "which lengths did you NOT need?" is strategy praise built into the item; the cliff is Q3 (two triangles, two heights) and Q4 (three subtractions) on page 2.
* **MID**: the best-fitting core lesson; Q2 "explain why both triangles have the same area" is a satisfying "aha".
* **HIGH**: Investigation (all right triangles of area 6 cm², then the line of possible top corners) and Challenge Q6 (two squares, always half the big square) are the strongest tasks for HIGH in the level.

Flags
* The page-1 drawings are "to scale" but slanted sides (13 cm, 15 cm, 17 cm) sit next to the height; a LOW child may multiply 8 × 10 in Q1(a) because the longest side is labelled; the "height outside the triangle" in Q1(c) is unexplained notation (dashed line).
* Explore needs grid paper, ruler and scissors at home (set-up says so in the guide, the weekly parent message should repeat it).
* Zero "Start here" hints on the core pages (only L4 and L7 have none).

### Lesson 5: Volume Vault

| | LOW | MID | HIGH |
|---|---|---|---|
| Participate | 3 | 4 | 5 |
| Fit | 2 (too hard) | 3 | 4 |
| Fun | 4 | 5 | 4 |
| Confidence | 3 | 4 | 4 |
| Motivation | 3 | 4 | 4 |
| Social/online | 2 | 3 | 3 |

* **LOW**: the 24-cube explore ("how many different cuboids, how do you know you have all") is a classic low-floor task and the stone-in-the-box demonstration is a strong hook; but the warm-up is a "Missing Edge Race" (`p5l5-warm1`, "teams race to find the third edge and say the division"), the check Q2 (water rise when a 10 cm cube sinks) is the hardest idea of the lesson at minute 0, ws1 Q3 needs 50 × 30 × 18 = 27 000 by hand, and ws2 Q5 (painted 4 × 4 × 4 cube) needs 3D visualisation.
* **MID**: strong; Q2 (all cuboids of 36) and Q4 (five cubes in a tank) are the right size.
* **HIGH**: painted-cube counting and the water-level rise are enjoyable; Investigation (boxes of 48 and 64 cubes, a prime gives one box) is a fine generaliser.

Flags
* Minute 3-6, LOW and Social: the word "race", plus shouting a team name and a division, pushes speed; a slow child is not heard.
* Minute 9: the explore needs 24 cm cubes; the online note says "dice, Lego or squared-paper drawings", which is workable but not the same experience.
* Notation: "cm³", "ℓ", "breadth" in the cuboid items against "wide" in the tank items; ℓ is never explained.
* Reading: 402 words on pages 1-2, the second highest.

### Lesson 6: Rate Racers

| | LOW | MID | HIGH |
|---|---|---|---|
| Participate | 3 | 4 | 5 |
| Fit | 1 (far too hard) | 2 (too hard) | 4 |
| Fun | 3 | 4 | 4 |
| Confidence | 2 | 3 | 4 |
| Motivation | 2 | 4 | 4 |
| Social/online | 2 | 4 | 3 |

* **LOW**: ws1 Q1 (rate table, 48 bottles in 3 minutes) is a win, but the warm-up "Better Buy Showdown" asks the child to point and then prove with a price of one (`$2.40 ÷ 3`, `$3.80 ÷ 5` are decimal divisions), the check C2 compares 18 ÷ 15 with 25 ÷ 20 (1.2 against 1.25), Q2 needs 73¢ (`$2.92 ÷ 4`), and ws2 Q5 (the car park, 9.40 a.m. to 1.15 p.m., "60 cents for every half hour or part of a half hour") combines clock time across noon, a tariff rule in words and a first-hour exception.
* **MID**: Q1, Q3, Q4(a) fine; Q2(c) (exactly 20 cans, whole packs) and Q5 hurt.
* **HIGH**: printers working together, a leak taking the rate away and candle/phone-plan questions are well pitched; the "3 cats, 3 fish, 3 minutes" challenge is a classic.

Flags
* ws2 Q5: the longest stem on the page with a time-after-noon subtraction. Highest risk of "I am stupid" for a slow reader.
* Q2(c): "He may buy from more than one shop, but only whole packs. Find one way": a search with no starting structure.
* The warm-up game, the check and the explore all lean on decimals ($2.40 ÷ 3, 1.2 against 1.25) before the lesson has taught a way to handle them.

### Lesson 7: Percentage Puzzles

| | LOW | MID | HIGH |
|---|---|---|---|
| Participate | 4 | 5 | 5 |
| Fit | 2 (too hard) | 3 | 4 |
| Fun | 4 | 5 | 4 |
| Confidence | 3 | 4 | 4 |
| Motivation | 4 | 5 | 4 |
| Social/online | 3 | 4 | 3 |

* **LOW**: Hundred-square snap has a low floor (count the shaded squares), "up 10% then down 10% on a $200 bicycle" is a mystery that every child can start (10% of 200 is 20), and ws1 Q1's table uses the 10%, 5%, 1% building blocks that the worked example teaches; the strain comes with decimals ($48.60 in the check, $11.52 in Q2(b)) and two-step flows in Q3-Q5.
* **MID**: the best lesson of the level for relevance (discounts and GST in Singapore shops) and for the "percentage of WHAT?" refrain.
* **HIGH**: Investigation (does the order of two discounts matter) is a real conjecture-test task; Think Harder Q1 and Challenge Q5 are P6 previews and are labelled as such, which protects everyone.

Flags
* Two extra teaching slides (`p5l7-teachchange`, `p5l7-teachdeal`, P6 percentage change and "buy 2 get 1 free") sit after `ws2ans` and have no slot in the printed timetable (talk time starts at minute 76); the notes say "for children who go on to the Think Harder page", i.e. teaching delivered to a subset in a group session.
* Check C1 (60 → 54 → 48.60) needs a decimal subtraction at minute 0 for a child who is not fluent with 10% of 54.

### Lesson 8: Angle Chasers

| | LOW | MID | HIGH |
|---|---|---|---|
| Participate | 3 | 4 | 4 |
| Fit | 2 (too hard) | 3 | 4 |
| Fun | 3 | 4 | 5 |
| Confidence | 3 | 4 | 5 |
| Motivation | 2 | 3 | 4 |
| Social/online | 3 | 4 | 3 |

* **LOW**: Guess-the-angle with a paper corner and a fold is friendly and ws1 Q1(a) "180° − 68°" is a clear win; but every task asks for "angle BOC", "AB = AD", "PQ = PR" notation (never explained, just used), check C1 and C2 at minute 0 both require writing a reason, C2 needs "adjacent angles of a parallelogram add to 180°" and "3 times" together, and pages 1-2 have the highest reading load of the level (425 words and 3 figures on Q2).
* **MID**: Q3 helps with "write the reason only for (b) and (d)" and the reason letters A-F in Q2; Q4 (six sub-parts) and Q5 (find every case) are heavy but possible.
* **HIGH**: the detective framing, Think Harder S4 (square and equilateral triangle, 15°), Challenge Q6 (150°) and the angle-in-tens Investigation are among the most satisfying items; Confidence 5.

Flags
* Minute 0-3, LOW: "Give the reason for each step" is a new genre of answer, asked before a single reason has been modelled.
* Q2: "Write each angle fact you use" with six letter codes A-F but no sentence frame ("Angle B = 108° because ...").
* Page 1 never says what "angle BOC" means (vertex in the middle).

### Lesson 9: Pattern Generalisers

| | LOW | MID | HIGH |
|---|---|---|---|
| Participate | 4 | 4 | 5 |
| Fit | 2 (too hard) | 3 | 4 |
| Fun | 4 | 4 | 5 |
| Confidence | 3 | 4 | 5 |
| Motivation | 3 | 4 | 5 |
| Social/online | 3 | 4 | 3 |

* **LOW**: high fives (8 children, dots and lines, a table) is a social, kinesthetic, low-floor explore; the check items (3, 7, 11 dots; figure 10; the figure with 99 dots) can be solved by continuing the list, so they are fair at minute 0; ws1 Q1(a) (chairs for 4 and 5 tables) is a win; ws2 Q4 and Q5 are suppositions ("suppose all 30 coins are 20¢"), the jargon "supposition" and a two-step logic that she will not follow alone.
* **MID**: Q3 (guess and check with a table) is the sweet spot; Q4-Q5 are tough but the "Hint: suppose he got them all correct first" gives a handle.
* **HIGH**: Investigation (sum of the first n odd numbers, L-shaped borders) and Challenge Q5 (diamonds, 61) are the best "generalise and prove" in the level.

Flags
* Warm-up "Guess My Rule": "the first child to say the rule in words wins the round" is a speed contest.
* Check slides describe the dot patterns in words only (no picture), a known gap in the P5 close-gaps note.
* Q5(b) "Why must she be wrong?" (80 is not 100 minus a multiple of 7) is a hard explanation for a child writing in a second language.

### Lesson 10: Challenge Day

| | LOW | MID | HIGH |
|---|---|---|---|
| Participate | 3 | 4 | 4 |
| Fit | 2 (too hard) | 3 | 3 |
| Fun | 4 | 5 | 5 |
| Confidence | 3 | 4 | 4 |
| Motivation | 3 | 4 | 5 |
| Social/online | 2 | 3 | 3 |

* **LOW**: the "Puzzle menu" (choose 2 of 4 cards, including the 20 = sum, 6 = difference card) is the only real choice in the programme and it works; the logic grid (Q2) is a win; but the first worksheet question is the hardest (Q1, three steps of working backwards with a fraction, a $12 spend and "half of what was left"), Q3 ("Ravi has $10 more than 3/4 of Mei's") follows, and the warm-up "Mix-up relay" is a cold-call across all nine lessons.
* **MID**: a good synthesis day.
* **HIGH**: the best ceiling in the level (staircase and Fibonacci, Challenge Q7 logic chair puzzle).

Flags
* Minute 3-9, LOW: the relay (read a card, say a child's name, that child answers and names the next) can land a lesson-6 question on the child who never got lesson 6; and some children may never be named.
* Minute 76-82: "Pick one puzzle and teach it in two sentences" is spoken, public and has no sentence frame.
* Minute 82-90: exit ticket plus certificates compete for the last 8 minutes (certificates 88-90); the reflection has no slot.
* Vocabulary: "heuristic" and "logic grid" are used as labels on the key-idea slide.

## Part 1 summary

### The 5 weakest lesson-persona cells, with fixes

1. **Lesson 3, LOW (2.00).** Too hard, public at minute 0, no easy first item.
   * Check C1 (slide `p5l3-check`; source `p5/content/gaps.js`, lesson 3, `check[0]`): replace "Ben is 8 and his father is 32. How old will Ben be when his father is 3 times as old as Ben? What stays the same as they get older?" with "Ben is 8 and his father is 32. (a) How old is Ben's father when Ben is 12? (b) How much older than Ben is his father now? How much older when Ben is 12?" (answers 36; 24; 24). Same idea, a guaranteed first success.
   * Workbook p.13 (L3 ws1), Q1: put a new first part: "(a) Try $60 first. The book costs $____, the pen costs $____, and $____ is left." (20, 10, 30). Move "What fraction of his money did he spend on the pen?" to the last part, marked "(stretch)".
   * ws2 Q5: replace "After: blue is 2 out of every 5" with "After: the box has 5 equal parts. 3 parts are red and 2 parts are blue. Draw the 5 parts."
   * Warm-up jar: keep the first two cards on the slide and move the third card (5/6 of what is left) to the tutor's extension.
2. **Lesson 6, LOW (2.17).** Decimal divisions and a long tariff stem.
   * Warm-up pair 1 (`deck.warmGame`): replace "3 for $2.40, or 5 for $3.80" with "4 pens for $2.00, or 10 pens for $4.00" (50¢ and 40¢); keep the juice and egg pairs for the tutor to use if the group is ready.
   * Check C2: replace "Ali reads 18 pages in 15 minutes. Mei reads 25 pages in 20 minutes." with "Ali reads 12 pages in 4 minutes. Mei reads 20 pages in 5 minutes. Who reads faster? How can you be sure?" (3 against 4 pages a minute; whole numbers).
   * ws1 Q2: add "Start here: Shop A, 6 cans for $4.20, so 1 can costs $4.20 ÷ 6 = ____¢."
   * ws2 Q5: replace "Start here: how long is 9.40 a.m. to 1.15 p.m.? Count the first hour, then count the half hours" with a printed time line: "9.40 | 10.40 first hour | 11.10 | 11.40 | 12.10 | 12.40 | 1.10 | 1.40. Circle the half-hours Ali's car is in the car park. Count them."
3. **Lesson 2, LOW (2.67).** Unlike-fraction subtraction on every trial.
   * ws1 Q2: add "Start here: 7/10 − 1/2. Write 1/2 as tenths: 1/2 = ____/10. So 7/10 − 1/2 = ____/10 = 1/____."
   * ws1 Q1(b): add "(a fraction or a mixed number is fine)" after "Each piece is ____ m long."
   * ws1 Q1(c): add the hint "How much of a whole pizza is each child short of? Compare the two shortfalls." (the printed key already offers this route), which removes the need for a common denominator.
   * Check C2 (`p5l2-check`): add a printed empty bar cut in 3 equal parts next to the question, with "Use the bar".
4. **Lesson 8, LOW (2.83).** Notation and reason-writing.
   * Page 1 header: add one line "Angle BOC means the angle at O between the lines OB and OC."
   * Q2: add a sentence frame under the hint: "Write like this: angle B = 108° because neighbours in a parallelogram add to 180°."
   * Check C2: replace "In parallelogram ABCD, angle A is 3 times angle B. Find angle A. Give your reason." with "Two straight lines cross. One of the four angles is 38°. Find the angle next to it. Say which angle fact you used." (142°, angles on a straight line). Keep the parallelogram question for Think Harder.
5. **Lesson 10, LOW (3.00, tied with Lessons 1 and 5).**
   * Swap Q1 and Q2 on page 1 so the logic grid is first; the backwards-fraction question becomes Q3 ("Start here" line kept).
   * Mix-up relay (script `warmIntro`): add "You may say 'pass' once. Choose a colour: green is a quick one, orange is a think-about-it one. I will name every child once before anyone is named twice."
   * Talk-time frame: add "Say: I started by ____. I know it is right because ____."
   * Same cell family, near-ties at 3.00: Lesson 1 LOW (replace check C1 with "Cards 3, 6, 7 and 9. Make one 4-digit number as close to 7000 as you can. Try a number that starts with 7 and one that starts with 6. Which is closer?" so the both-sides idea is a question, not a hidden requirement) and Lesson 5 LOW (rename the "Missing Edge Race" warm-up "Missing Edge Match", teams write answers and show them together, nobody shouts; and add "Draw the tank and shade the water" to check C2).

### The 3 strongest cells

1. **Lesson 7, MIDDLE (4.67)**: relevance (discounts, GST), the "why is it $2 less?" surprise, a scaffold (10%, 5%, 1%), and a dominant refrain ("percentage of WHAT?").
2. **Lesson 4, MIDDLE (4.50)**: paper-cutting explore, visual items, one clear formula, the "which lengths did you NOT need?" strategy item.
3. **Lesson 9, HIGH (4.33, tied with Lesson 10 HIGH)**: the L-shaped border picture for the odd numbers, diamonds, supposition; the HIGH child finally gets a task where explaining why is the point.

### Level-wide patterns

1. **One timetable for ten very different lessons.** Pages 1 and 2 get 12 and 15 minutes (27 minutes) for six to nine multi-part items, while "check together" gets 2 minutes after page 1 and 4 after page 2 (6 minutes). Three-part questions cannot be checked in 2 minutes; the LOW child sees an answer with no understanding.
2. **Two timetables disagree.** The tutor guide (`p5/guide.js`) schedules: check 2-5, explore 10-25, mini-lesson 25-35, worksheet 40-70 (pairs 40-52, alone 52-62, stretch 62-70), talk 70-80, exit 80-90. The decks schedule: explore 9-21, teaching 21-33, ws1 37-49, teaching 51-57, ws2 57-72, talk 76-82. The guide has no "teaching before page 2" block and gives page 2 only 10 minutes alone.
3. **Reading load.** Pages 1-2 range from 260 words (L7) to 425 (L8); L5 (402), L3 (380), L6 (380), L10 (376) are the next heaviest. Check questions run 13-36 words (L10 C1 is the longest at 36). A slow reader carries 1.5 to 2 times the load of the MIDDLE child.
4. **Wait time for the HIGH child.** If the child passes the check, about 25 of 90 minutes are low-demand (3 min quick questions, about 8 min of the worked examples, 2 + 3 min answer checks, about 5 min teaching before page 2, about 4 min waiting at the end). The fast track does not start until minute 37, so it never compacts the first 34 minutes. The HIGH child's Fit is 4 (too easy) in every lesson except L10 (3).
5. **Guaranteed win for the LOW child in the first 10 minutes of the worksheet.** Eight of ten lessons open with an approachable first sub-question (L1 Q1(a), L2 Q1(a), L4 Q1(a), L5 Q1(a), L6 Q1(a), L7 Q1 10% row, L8 Q1(a), L9 Q1(a)). Lessons 3 and 10 do not (their first item is the hardest). Page 1 usually ends with its hardest item (L1 Q3 riddle, L2 Q3, L8 Q3) so the win is followed by a wall.
6. **Page 2 is alone, with no hint scaffolding of equal strength.** "Start here" lines appear 0-3 times per lesson on the worksheets (L4 and L7 have none). The LOW child is isolated for the 15 hardest minutes.
7. **Labels.** The words "Think Harder", "For early finishers" (slide title on every stretch and challenge slide), "Challenge (for strong thinkers)" (printed banner on every Challenge page) and "Fast track" (printed on page 1 of every lesson) sort children by speed and ability vocabulary. "Think Harder" implies that pages 1-2 need less thought.
8. **Strategy-based feedback and normalised struggle are real strengths.** Scripts say "Praise strategy, not speed", "Wait 10 seconds", "never record scores", "a wrong answer gets a friendly try again, never a groan". Mistakes appear in the notes only, not on the slide. That language is not enough to remove the structural problems above.
9. **Pairs.** The guide says "pairs go to breakout rooms" but never says how pairs are made or what happens when a fast-track child leaves, which strands their partner.
10. **The LOW child is the weak spot of the level (mean 2.90).** Five of ten lesson cells are at or below 3.0. MIDDLE (4.07) and HIGH (3.90) are well served.

## Verdict on the four new items

**Warm-up check.**
* The check is placed at minute 0-3, before the key idea is taught, on questions that ask for an explanation ("Say why you tested the way you did"; "Draw a bar"; "Give your reason"). In 10 lessons the LOW child meets a problem on an untaught idea in the first 90 seconds, with a whiteboard to hold up in front of up to seven others. Intended as "a check for you, not a test", but the child cannot know that.
* "Ask one child per question 'How do you know?'" does not say which child. If the tutor picks a child who held up a wrong answer, it is public.
* The slide says (verbatim, every lesson): "Everyone does the check. Then some of us start on page 1 and some start on the Think Harder pages. Both are good choices, and you can swap." At minute 0 the child reads that the check will sort them.

**Fast track.**
* It labels. The workbook prints on every page 1 an orange dashed box: "Fast track. Got BOTH Warm-up check questions right and can explain why? Your tutor may send you straight to the Think Harder pages ... It is a choice of starting place, not a label". Telling a child it is not a label is a label. A child who did not get both right reads "Got BOTH ... right" every lesson.
* It does not compact. The fast-track child starts the Think Harder pages at minute 37, after warm-up, explore, mini-lesson and the break (the script says "while the group works page 1").
* It strands partners and makes a permanent two-tier: with 8 children, the same 1-3 go to a breakout room or the chat page numbers each time.
* Nothing equivalent exists for the child who needs more support.

**Open investigation.**
* Good tasks (the best items in the level; types: what-if, is-it-always-true, find-all). But they sit on page 5 of each lesson, after page 2, Think Harder and Challenge. Only fast-track children reach them. The LOW child, who would gain most from a low-pressure open task, never sees one.
* Part (a) is approachable in 8 of 10 (L1 (a) needs 7-digit comparisons for four targets and L2 (a) needs unlike-fraction subtraction, so those two are not low-floor for LOW).
* Space: 7 answer lines for three parts, shared with the reflection box on the same page.

**Reflection ("What was hard?").**
* Mostly safe: the prompts "The hardest part was ...", "I got unstuck by ...", "Next time I will try ..." normalise difficulty; the heading says "(just for you: nobody marks this)"; the script says never grade, praise strategy, read aloud only volunteers.
* Four weaknesses for a low-confidence child:
  1. The "I got unstuck by" boxes (picture, list/table, simpler number, partner, estimate) all presume the child did get unstuck; there is no "I am still stuck, and I will tell my tutor" option.
  2. "Nobody marks this" conflicts with the script "Read a few later to plan the next lesson" and the tutor tracker (S/D/H with a catch-up). Do not say "nobody" if the tutor reads it.
  3. It comes last, after the exit ticket, at minute 89, for one minute: the item that gets cut if anything runs over, and it asks a slow writer for three written lines.
  4. It sits on page 5 (the investigation page), so a child who has never turned to that page has to find it.

### Exact fixes for the new items

* `check` slide line: replace "Everyone does the check. Then some of us start on page 1 and some start on the Think Harder pages. Both are good choices, and you can swap." with "Everyone does the check. At the break you choose your start: page 1 with a partner, or the Think Harder pages. Both are good. You can swap at any time."
* Script `check`: replace "Children write the answer on a whiteboard and hold it up together" with "Children write the answer on a whiteboard, keep it face-down, and when you call their name turn it to the camera only for you (or type it in a private chat to you). Ask a volunteer, or a child you saw get it right, to say how they know."
* Workbook box (`workbook_html.js` `fast()`): replace the text with "Choose your start. Page 1 with a partner, or the Think Harder pages (page 3). Your tutor can help you choose. You can swap whenever you like." and delete "Got BOTH Warm-up check questions right".
* Banner: replace "Challenge (for strong thinkers)" with "Challenge (a puzzle to chew on)"; slide title "For early finishers" with "More puzzles".
* Scheduling: move the choice to minute 37 for everyone (menu of page 1 with partner, or Think Harder; the tutor helps children who need help choosing) and invite the whole group to do Investigation part (a) in pairs during talk time (76-82).
* Reflection: add a sixth drawn tick box "I am still stuck. I will tell my tutor." (drawn bordered shape, not a glyph); change the heading note to "(just for you. Your tutor may read it to plan the next lesson, but it is never marked.)"; allow answering by voice or one emoji in chat; give it 2 minutes by trimming the exit ticket slot to 82-88.

## Part 2: diagnostic check

### (a) True skill demand per question

Source for school-year placement: MOE-school pages cited at the end; where a page did not settle a point I say so.

| Q | Question (short) | Answer (verified) | True skill demand | Fair for age 10-12 finishing P5? |
|---|---|---|---|---|
| W1 | 5/6 − 1/3, simplest form | 1/2 | Convert 1/3 to 6ths (related denominators), subtract, simplify (3/6). 3 steps. | Yes. P4-level: P4 lists addition and subtraction of fractions. The skill tag "unlike fractions" overstates it (3 divides 6). |
| W2 | 2.4 m cut into 6 | 0.4 | Divide a one-decimal number by a whole number, keep place value. | Yes. P4 lists the four operations with decimals. |
| W3 | 24 × 35 | 840 | Two-digit by two-digit multiplication. | Yes, but it belongs to P3-P4. At P5 almost everyone gets it. It tells the tutor nothing. |
| W4 | Perimeter 36, length 11, area | 77 | Two-step: width 7, then area. | Yes. P4 lists "unknown sides of rectangles" and perimeter/area of composite figures. This is the P4 diagnostic core question (36 and 11, "how wide") with one more step. |
| M1 | Round 4 386 512 to nearest 100 000 | 4 400 000 | Place-value of the hundred-thousands, round up on 8. | Mostly. P4 teaches rounding to 10, 100, 1000 up to 100 000; the P5 handbook I could read does not mention rounding. A transfer, not an unfair item. |
| M2 | Sam 2/5, then 1/3 of remainder, $24 left | 60 | Fraction of a remainder, three steps, bar model. | Yes, standard P5 paper-2 item. Hard for the average child. |
| M3 | Triangle area 40, base 16 | 5 | Reverse the formula. | Yes (P5 area of triangle). |
| M4 | Tank 50 × 30 × 40, 6 ℓ/min | 10 | Volume, unit conversion (given), rate. Three steps. | Yes (P5 volume and rate). Hard for the average child. |
| M5 | 60% of 40, then 25% | 6 | Percentage of a quantity twice. | Yes (P5 percentage). |
| M6 | Quadrilateral angles 90, 110, 75 | 85 | Needs the fact "angles in any quadrilateral add to 360°". | **No.** The P5 handbook lists angles on a line and at a point, vertically opposite angles, triangle sums, and angles in parallelogram, rhombus and trapezium, and states unknown angles are found "without drawing additional lines", and says nothing about a general quadrilateral sum. Lesson 8's explore is where this program teaches it. It measures exposure, not ability. |
| S1 | 2, 5, 10, 17, 26 ... the 10th | 101 | Second-difference pattern or n² + 1; or continue five more steps. | Competition-style. Fair as a stretch; solvable by persistence (continue the differences 11, 13, 15, 17, 19). |
| S2 | Ali 3 times as many as Ben; gives 18; now twice | 162 | Before-after with a changing ratio. | A P6 heuristic. Very hard; fair only as a stretch. |

Additional design findings
* Every item is a closed numeric answer. The program's own brand ("Notice it. Test it. Explain why") and the lesson checks ask for reasons; the diagnostic measures none of that.
* Nothing tests reading stamina or willingness to draw a model; there is one bar-model item (M2) whose bar is optional.
* 30 minutes for 12 items with several three-step ones is tight for a careful child; the sheet gives no guidance about what to do when time ends.

### (b) Six profiles

Per-item chances are my assumptions (listed in the helper script), set from how hard each item is and what each child has been taught. Results are exact calculations from those assumptions, not simulations. Placement shown by the current rule (6-8 of 8 join; 4-5 join with support, or one level down if warm-up is 2 or less; 0-3 one level down; 8/8 with 4/4 may try the level up).

| Profile | Expected warm-up / main / stretch | Most likely result (score of 8) | Placement by current rule | Right level against what the lessons demand? |
|---|---|---|---|---|
| **Strong for age** (P5, about 11, top 15%) | 3.9 / 5.3 / 1.0 | 6 (35%), 7 (33%), 8 (11%) | P5 69%, P5 with support 20%, P5 and "try P6 check" 10%, P4 1% | **Yes.** Journey score for HIGH is 3.9; needs the Think Harder pages. The 20% "with support" label is unneeded but harmless. |
| **Typical for age** (P5, about 11) | 3.2 / 3.5 / 0.2 | 3 (27%), 4 (30%), 5 (19%) | **P4 43%**, P5 with support 41%, P5 with support or P4 8%, P5 7% | **Mostly wrong.** Journey MIDDLE is 4.07 (fit 3 except L3, L6). P5 is the right level; 43% are told to go down. |
| **Weak for age** (P5, about 11) | 2.1 / 1.6 / 0.0 | 1 (33%), 2 (33%) | P4 95% | **Yes.** Journey LOW mean is 2.90, with L3 at 2.00 and L6 at 2.17. |
| **Younger and strong** (9-10, finished P4) | 3.8 / 2.7 / 0.4 | 3 (32%), 4 (23%), 2 (23%) | P4 64%, P5 with support 33%, P5 3% | **Probably wrong.** Warm-up is 3.8/4: foundations are fine. The missing marks are on M3-M6, which are content the P5 lessons themselves teach (the L4, L5, L7 explores build triangle area, volume, 10%/5%/1% from scratch). Needs a chat, not an automatic step down. |
| **Older and weak** (12, past P5) | 2.3 / 2.5 / 0.1 | 2-3 (31%, 30%) | P4 79%, P5 with support or P4 11% | **Right on maths, awkward on age.** P4's band is 9-11, and the child is 12. |
| **Guesser / rusher** (typical ability, falls in the listed traps) | 2.5 / 2.3 / 0.1 | 2 (31%), 3 (28%) | P4 82% | **Wrong-ish.** Every main item has a listed "common error" (14, 10, 2.5, 90, 180) that a rusher falls into. The lessons are exactly about checking and estimating. The score cannot tell "cannot" from "did not check". |

Pure guessing on open answers cannot place anyone. At a 2% chance per item, the chance of 6 or more correct is about 2 in a billion; at 5% it is 4 in 10 million. Wrong calls come from honest noise and syllabus exposure, not luck.

### (c) Cut scores and the warm-up

**Noise at the cut.** For a child with a fixed chance p of getting each of 8 items right (an optimistic model: a tired or anxious child misses many together, which makes real results worse):

| True p per item | P(6-8 join) | P(4-5 support) | P(0-3 down) | Same band on two sittings |
|---|---|---|---|---|
| 0.4 | 5% | 36% | 59% | 48% |
| 0.5 | 15% | 49% | 36% | 40% |
| 0.6 | 32% | 51% | 17% | 39% |
| 0.65 | 43% | 47% | 11% | 41% |
| 0.7 | 55% | 39% | 6% | 46% |
| 0.75 | 68% | 29% | 3% | 55% |
| 0.8 | 80% | 19% | 1% | 67% |
| 0.9 | 96% | 4% | 0% | 93% |

* The standard error is about 1.4 marks for children in the middle, while the "support" band is 2 marks wide. A child exactly at the 6/8 line (p = 0.75) is told "join" 68% of the time, "support" 29% of the time, and "down" 3%. A child who is truly average-to-weak (p = 0.5) still hears "join" 15% of the time.
* The two stretch items count in the 8 yet few children get them (assumed 18% and 7% for the typical child), so 6/8 effectively demands 6/6 on the main section for most children. A typical child's expected score is 3.7 of 8.
* The "try the level up" route needs 8/8 and 4/4: about 10% of strong children can reach it. The levels doc says "90%+", which for 8 items is the same thing as 8/8.
* The warm-up score is used only in the middle band, and only to choose between P5 and P4. A child with 0-3 and 4/4 on the warm-up (the younger strong child) is not given the same nuance.

**Are the four warm-up questions truly from the level below?** Partly.
* The P4 diagnostic (`diag/content/p4.json`) has these core items: round 48,572, 12 + 6 × 3 − 4, 2 3/5 + 1 4/5, 3.7 + 2.85, rectangle perimeter 36 and length 11 (answer 7). So the P5 warm-up is above the P4 core, not at it: W1 needs unlike denominators, W2 divides decimals, W3 is two-digit by two-digit.
* W4 reuses the P4 core question's numbers (36 and 11) and adds the area step, so a child who sat the P4 check will have seen it.
* W3 is P3-P4, so it is not a useful filter.
* None of the four tests what the P5 lessons rely on: a fraction of a quantity (L2, L3, L10), a bar model, or 10% by dividing by 10 (L7).

### (d) Wording of the parent result page and tutor key

Quoted from `diag/build_diag.py`.
* "Add up the marks, then find your row." The parent marks, so the first reading of a "0-3" row is by the parent in front of the child.
* **"Not yet? That is useful to know, not a failure."** The word "failure" is put into the parent's head by the page itself. Replace (see (e)).
* **"We suggest Ages 9-11 (P4). The ideas build step by step, and a confident start matters more than a fast one."** It reads as "your child is not confident", and is shown even when the warm-up was 3 or 4 of 4.
* "Strong? ... A child who finds this easy will enjoy the challenge questions in class." Fine, but it hands a parent of a 6/8 child an argument for "my child is strong".
* "6 to 8: ... Your child has the foundations and will be well challenged." is shown to a child who may have scored 0/4 on the warm-up (not possible to rule out).
* The child sheet says "If they are stuck, say 'Try your best, or skip it', and move on." but never says the last two questions ("Brain stretchers") are meant to be very hard and that many children skip them. A child meeting questions 11 and 12 without that line may feel stupid.
* No time guidance (no "stop at 30 minutes; unanswered counts as zero").
* Answer key page: "Watch for: common error: ..." is neutral but is read by the parent; add a parent line not to mark in front of the child. The example "Accept equivalent forms (for example $2.05 and 2.05)" is a money example that the P5 items never use.
* Key: M1's "4400000 (4,400,000)" does not accept "4.4 million".
* The key prints in the same PDF as the child's pages (pages 3-4), so a child can turn to the answers.

### (e) Recommended changes (exact text)

Questions
1. **Replace M6** with an in-syllabus angle item.
   * Text: "In triangle ABC, AB = AC and angle BAC = 50 degrees. What is angle ABC, in degrees?"
   * Answer: 65. Watch for: 130 (forgot to share the rest between two equal angles) or 50.
   * Skill: "Angles in an isosceles triangle". Change the topics line "Angles in quadrilaterals" to "Angles in triangles".
2. **Replace W3** (24 × 35) with a prerequisite the lessons rely on.
   * Text: "What is 3/4 of 48?" Answer: 36. Watch for: 12 (divided by 4 only) or 192 (multiplied). Skill: "Fraction of a set".
3. **Keep S1 and S2**, but make them unscored for placement and label the sheet: "Brain stretchers. These are meant to be tricky. Many children skip some. Skipping is fine."
4. **Add an unscored line** under M2 and M4: "How did you start? Write one line or draw a quick picture." The tutor reads it in the chat and uses it for the 3-5 band.
5. **Child sheet intro:** add "There are 12 questions and about 30 minutes. Stop when time is up; questions you did not reach count as zero. If you finish early, check each answer a second way."

Cut scores
* Score placement on the main section (out of 6); the stretch questions only add a "challenge-ready" flag:
  * 5 to 6 of 6: join Ages 10-12 (P5). If 6 of 6, warm-up 4 of 4 and at least one stretch right: also offer the free P6 check.
  * 3 to 4 of 6: join P5 with support. If the warm-up is 2 or less: recommend P4 or a chat.
  * 0 to 2 of 6: P4. **Exception:** if the warm-up is 3 or 4, offer a free 10-minute tutor chat before recommending P4 (the child may simply not have been taught this year's content).
* Effect of the proposed rule plus the new M6 under the same assumptions: typical child P4 falls from 43% to 2% (P5 26%, with support 49%, chat 12%, support or P4 10%); younger strong child P4 falls from 64% to 0 (support 54%, chat 39%, P5 6%); weak child still goes to P4 or chat (P4 47%, chat 26%, support or P4 16%, support 9%, P5 1%); strong child stays at P5 (52% P5, 40% with the try-P6 flag, 7% support).
* The stretch questions still add information (the try-P6 offer), but they no longer move a typical child across a line.

Parent result page text
* Replace "Strong? Choose the level that fits the score, not the school year. A child who finds this easy will enjoy the challenge questions in class." with "A high score? Choose the level that fits the score, not the school year. The Think Harder pages in class give a strong child plenty to chew on."
* Replace "Not yet? That is useful to know, not a failure. Starting one level down means more success and more joy in class." with "A lower score? A score is one snapshot on one day. It tells us where to start. Starting one level down means your child meets ideas they can already half-do, which builds confidence quickly. If you are unsure, book a free 10-minute chat with us before you decide."
* Replace the 0 to 3 row text "We suggest Ages 9-11 (P4). The ideas build step by step, and a confident start matters more than a fast one." with "Ages 9-11 (P4) is likely to be the more comfortable start, because the ideas build step by step. If the warm-up score was 3 or 4, or your child was tired or distracted today, book a free 10-minute chat with us before you decide."
* Replace the 6 to 8 row ending "Your child has the foundations and will be well challenged." with "Your child is ready for the pace of this level."
* Add under the table: "Please do not mark in front of your child, and please do not compare answers with the key while they watch. Say 'Let's look at that together in class' rather than 'that's wrong'."
* Key page: move it to a separate "tutor and parent" PDF; replace "Accept equivalent forms (for example $2.05 and 2.05)" with "Accept equivalent forms (for example 4 400 000 and 4,400,000, or 4.4 million, or 0.4 and 2/5)."

## 10-line summary

1. LOW (mean 2.90): served poorly. Lessons 3 and 6 are too hard with no easy opening, the check at minute 0 and the Fast track box expose her every lesson, and page 2 is a 15-minute solo wall; the low floor in the explores (pizzas, counters, cubes, paper triangles) is real and should be protected.
2. MIDDLE (mean 4.07): served well; Lesson 7 (4.67) and Lesson 4 (4.50) are the best cells. Only Lesson 3 is too hard for her.
3. HIGH (mean 3.90): served well in task quality (investigations, Think Harder) but about 25 of 90 minutes are low-demand, and the fast track starts only at minute 37 and isolates her.
4. Fix 1: make the choice of start a menu at minute 37 for everyone; rename "Fast track", "Challenge (for strong thinkers)" and "For early finishers"; make the check private (face-down or private chat).
5. Fix 2: rewrite the entry points for the LOW child in L3 and L6 (check C1/C2, warm-up pair, Q1 order, Start-here lines) and give L2, L8, L10 the scaffolds listed above.
6. Fix 3: reconcile the two timetables and give check-together 4 minutes after page 1; give the reflection 2 minutes and add an "I am still stuck" tick box.
7. Fix 4: invite the whole group to Investigation part (a) in talk time so the open tasks are not reserved for already-secure children.
8. Fix 5: replace diagnostic M6 (quadrilateral sum, out of the P5 syllabus) and W3 (too easy), unscore the stretch pair, and base placement on the main 6.
9. Diagnostic verdict: **mostly**. It puts strong children (P5) and clearly weak children (P4) in the right place, but about 43% of typical children and 64% of younger, strong children are told "go down" by my assumed profiles, and the 8-item cut is too noisy to bear that weight (a child exactly on the 6/8 line is told "join" only 68% of the time).
10. The free level change before lesson 1 and the parent's final say protect families, but only if the result page stops saying "failure" and sends borderline children to a chat instead of an automatic step down.

## Sources for school-year claims

* Shuqun Primary School, P5 Mathematics Handbook (MOE school page): https://www.shuqunpri.moe.edu.sg/files/P5_Mathematics_Handbook.pdf. Read via fetch: lists P5 decimals (by 10, 100, 1000), fractions, percentage, area of triangle, volume, rate, angles, properties of isosceles/equilateral/right-angled triangles and parallelogram/rhombus/trapezium; does not list ratio, rounding or a general quadrilateral angle sum.
* Tao Nan School, Curriculum Information 2024 P4 Mathematics: https://taonan.moe.edu.sg/files/Partners/For%20Parents/Curriculum_Information_2024_P4_Mathematics.pdf. Read via fetch: P4 fractions (addition and subtraction), decimals (four operations), rounding to 10/100/1000 up to 100 000, unknown sides of rectangles. It does not say whether the fractions are related or unlike.
* The MOE syllabus pages themselves could not be opened in this session, so school-year claims rest on these two school documents and on `p5/SPEC.md`.
