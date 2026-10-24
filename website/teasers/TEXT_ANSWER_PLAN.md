# Plan for text answers (audit round 5, condition C6; round 6 update in section 6)

Sections 1 to 5 are the round-5 plan with the round-5 counts. **Section 6 is the round-6 update**: the counts now (Nov and Dec, 61 days: L1 8, L2 9, L3 4, L4 6, L5 4, L6 4), the asks that are coded, the January allocation and the gate in the verifier.

Written 24 Oct 2026 for `website/teasers/`. Nothing here is released: it is the plan and the small amount of data and page support that the plan needs. The Jan to Oct puzzles are **not** written yet.

## 1. The problem in numbers

AUDIT_ROUND5 section 7 and condition C6: at present only 4 to 7 puzzles per level in 61 days have a word, a name or a letter as the answer. A year of 365 days at that rate gives 24 to 42 text answers per level, and in round 5 the count fell at some levels because the cluster fixes (C3) replaced several "who", "which way" and "which shape" puzzles by other kinds (Level 3 and Level 5 would have lost the most; three replacements, `L3-cuboidclue`, `L3-sixodds` and `L4-badgerow`, were made on purpose as text-answer puzzles to keep the counts near where they were). The owner wants about 40 or more text-answer puzzles per level over the year (three or four a month), so that "type a number" is not the only thing a child ever does.

| Level | Text-answer puzzles in Nov and Dec 2026 (61 days) | Projected in 365 days | Plan |
|---|---|---|---|
| 1 | 6 | 36 | use all seven text-capable sub-structures (+1) |
| 2 | 5 | 30 | +1 a quarter |
| 3 | 4 | 24 | +2 sub-structures |
| 4 | 4 | 24 | +3 sub-structures |
| 5 | 3 | 18 | +5 sub-structures |
| 6 | 3 | 18 | +4 sub-structures |

The verifier prints the live numbers in the "Text answers per level" table of `batches/STRUCTURE_REPORT.md` and a WARNING for every level below 40 a year. A warning does not fail a run: the released months are not wrong, they are just behind the plan.

## 2. What limits the number: the repeat rules

* Every text answer counts as an answer of "10 or more": it may be the answer of **one** puzzle per level in the whole year (names, shape names, words). A closed set is the binding constraint: there are only 4 compass words and 2 answers "odd" and "even".
* At Levels 3 to 6 a sub-structure may be used once per calendar quarter, so one text-capable sub-structure supplies **4** puzzles a year. At Levels 1 and 2 (gap of 60 days) it supplies **6**.

So 40 text answers a year need **10 text-capable sub-structures at each of Levels 3 to 6**, or **7 at Levels 1 and 2**. Today (sub-structures that can give a word as the answer, taken from `taxonomy.json`):

| Level | Text-capable sub-structures now | Puzzles a year they can give | Short of 40 by |
|---|---|---|---|
| 1 | 7: ranking by a story (`logic_order.rank`), who has what (`logic_match`), the bigger share (`fractions.unit_compare`), name the shape, facing and turning, a repeating pattern, am and pm (the latest time) | 42 | 0 |
| 2 | 8: the same seven plus odd or even | 48 | 0 |
| 3 | 8: ranking, matching, who is telling the truth (`logic_truth`), the bigger share, name the shape, facing and turning, odd or even, am and pm | 32 | 8 (2 sub-structures) |
| 4 | 7: ranking, matching, truth, turning, a repeating pattern, odd or even, am and pm | 28 | 12 (3 sub-structures) |
| 5 | 5: ranking, matching, truth, turning, odd or even | 20 | 20 (5 sub-structures) |
| 6 | 6: ranking, matching, truth, turning, odd or even, a decoded word | 24 | 16 (4 sub-structures) |

Two cautions that keep the count honest:

1. A sub-structure at several levels must keep a different story and a different sentence frame at each level (owner ruling C3 of round 5). "Who is telling the truth" at Level 4 and again at Level 6 is two different puzzles, not the same puzzle with other names.
2. Closed sets (the compass, odd or even, the letters A to D, shop A to C, the days of the week) are capped like single digits: each value at most **3** times a level a year. `verify_bank.py` will get that cap when the first closed-set puzzle of 2027 is written (today the compass and odd or even are used at most 3 times a year per level by hand).

## 3. How to reach 40 honestly

**Choice answers.** The wording lists the options and the child types the word or the letter: "(A) north (B) east (C) south (D) west". This is the honest way to ask for a word where spelling is not what is being tested, and it makes the closed-set puzzles possible (a shape, a shop, a direction). Rules: the options are written in the question, the answer is one of them, three options at least, the wrong answers are the other options (so the page can say which one was wrong), the options are never ordered so that the first or the last is always right (a count of the position of the right option over a month will be added to the verifier before the first choice puzzle is written).

**Word answers with an accepted list.** The answer is a name or a word; the data lists every spelling and article that counts as right (`accept`: "quarter-circle", "a quarter circle"; the page already accepts capital letters, a full stop, "It is ...", "The answer is ...", "on Sunday", the name without its space, and since round 5 a short sentence round the name, "Farid plays cricket", as long as the other options are not in it and there is no "not").

**More sub-structures that give a word.** These are the ten asks to add, each as a new ask of a kind that already has a solver and an independent checker, or as a small new kind with both:

| Ask | Answer | Levels | Needs |
|---|---|---|---|
| who has the most or the least in a table of named children (`stats`, ask `who`) | a name | 1 to 5 | new ask in `kinds.py` and `brute.py`, a sample |
| which shop is cheaper, A, B or C (`best_deal`, ask `shop`) | a letter | 1 to 5 | new ask, lettered choices |
| who has more after a gift (`word_problems.compare_amounts`, ask `who`) | a name | 1 to 6 | new ask |
| which day of the week, n days later (a weekday kind; the "borrow a book" frame is retired, a new frame) | a day | 3 to 6 | new sub-structure `calendar.day_of_week`, closed set of 7 |
| which colour or which name is in a cell of a latin square (`logic_grid.latin_square`, ask `name`) | a word | 1 to 5 | new ask |
| which place is on the shortest route (`networks.shortest_route`, ask `via`) | a place name | 2 to 6 | new ask |
| which bag gives the better chance, A or B (`probability`) | a letter | 6 | new sub-structure |
| what does the program print, "even" or "odd" (`programs.branching`) | a word | 6 | new ask |
| what kind of triangle or quadrilateral is it (by its sides or angles) | a word | 3 to 6 | new sub-structure `shapes.classify`, MOE P3 to P5 cite |
| which is heavier or longer after changing units, A or B | a letter | 3 to 6 | new sub-structure |

With them the capacity a year becomes: Level 3 gets +2 (40), Level 4 +3 (40), Level 5 +5 (40), Level 6 +4 (40), Levels 1 and 2 stay above 40. The names come from a pool of 60 or more Singapore names (Chinese, Malay, Indian, Eurasian) with each name used as an answer once per level a year; the pool is the `NAMES` set of `verify_bank.py` (about 70 words) and is enlarged when the first batch of 2027 is written.

**Do not** turn a numeric puzzle into a text one just to meet the count: if the ask is "how many", the answer stays a number. A choice question must have one correct option that a child can find by working, not by guessing among three.

## 4. What exists after round 5 (data and page support)

| Where | What |
|---|---|
| `defs_common.P(..., choices=[...], labels=True, accept=[...], w=[...])` | the options of a choice question and whether the wording letters them (A), (B), (C) ...; `build_bank.py` keeps them in `bank.json` (`choices`, `labels`) and uses the other options as the listed wrong answers |
| `verify_bank.py` | `choice_problems`: every option is written in the question, the answer is one of them, three options at least, and every letter (A) ... is in the question; a **Text answers per level** table and a WARNING per level below 40 a year |
| `teaser_html.compact` | exports `ch` (the options), `l` (lettered), `o` (the other options, so that a sentence round the right name is accepted and a sentence with a wrong name is not), `dt` and `mo` (a date answer: "the 25th", "13 December") |
| `teasers.js` | accepts the letter of a lettered option ("c", "(C)", "option C"); a short sentence round a name; and for numbers the words ("nineteen", "twenty-one", "one hundred and five", "two thirds", "five and a half"), "the 25th", "on the 13th of December", and "5½" |
| `test_check.js` (143 checks, negatives included), `test_site.py`, `--selftest` | the accepted and the rejected wordings, in Node and in Chromium, and the choice rules |

Nothing in this list changes what a visitor sees until January: no puzzle of November or December uses `choices`.

## 5. Schedule

1. **January batch (2027):** at least 3 text-answer puzzles per level, at least one of them a choice question (Levels 1 to 4) and one from a new ask of section 3. Write the new asks first (solver, checker, sample, taxonomy line with its cite), then the puzzles.
2. **February to April:** the remaining new asks; by the end of April every level has 10 text-capable sub-structures (7 at Levels 1 and 2).
3. **Every month:** the verifier's "Text answers per level" table must show at least 3 text answers in the month at every level; a month below that is not released.
4. **Before the last batch:** a count of the position of the right option in choice questions (about even over A, B, C, D) and of each closed-set value (at most 3 a level a year).
5. **Independent check:** every new text-answer puzzle is hand-solved by someone other than the author, in the same sample as the numeric ones (15 a level, new items first).

## 6. Round 6 (AUDIT_ROUND6 G4, condition 5 of the round-6 brief): the asks are coded, January is gated

Written 24 Oct 2026. The January to October puzzles are still not written, so this section is the plan and the checks, not a batch.

**Coded (solver in `kinds_r4.py`, independent checker in `brute_r4.py`, worked instances in `samples_r4.py`, taxonomy line with its MOE cite, proved by `verify_bank.py --selftest`):**

| Ask (kind) | Sub-structure | Levels | Answer |
|---|---|---|---|
| who has the most, the least or the second most in a short table (`table_who`) | `graphs.who_has_most` | 1 to 5 | a name |
| which of three shops is cheapest (`shop_choice`) | `money.cheaper_shop` | 2 to 5 | `Shop A`, `Shop B` or `Shop C` |
| who has more after gifts, winnings and spending (`gift_who`) | `word_problems.who_has_more` | 1 to 6 | a name |
| which place is passed first (or last) on the shortest route (`route_via`) | `networks.first_stop` | 2 to 6 | a place name |
| what kind of triangle: by its sides or by two of its angles (`classify_triangle`) | `shapes.classify_triangle` | 3 to 6 | a word |
| which of three amounts written in different ways is the heaviest or the lightest (`unit_heavier`) | `measurement.heavier_after_units` | 3 to 6 | a letter |
| which of three rates is the fastest (`rate_compare`) | `rate.compare_rates` | 5 | a name |

That is at least two new text-answer asks at every level (Level 1: 2, Level 2: 4, Levels 3 and 4: 6 each, Level 5: 7, Level 6: 4), on top of the older text-capable sub-structures. Ten puzzles of the released Nov and Dec bank use them (`L1-craneboard`, `L1-marbleswap`, `L2-quizscores`, `L2-markershops`, `L2-schoolwalks`, `L2-cardgame`, `L4-moneypurse`, `L4-parkpaths`, `L5-snailrace`, `L6-islandroutes`): they replace puzzles that were above or below their level, or that were the second copy of a frame, and they give Levels 1 and 2 the text answers that the rotation needs for January.

**Text-capable sub-structures per level after round 6** (the count a year needs is 10 at Levels 3 to 6 and 7 at Levels 1 and 2, because a sub-structure returns four times a year at Levels 3 to 6 and six times at Levels 1 and 2): Level 1 9, Level 2 12, Level 3 14, Level 4 13, Level 5 12, Level 6 10. Level 6 has the thinnest margin (10 for a need of 10).

**January allocation (plan).** From January a month is gated by `verify_bank.py` (below): at least 3 text answers at every level, 4 at Levels 5 and 6.

| Level | Need in January | Where they come from |
|---|---|---|
| 1 | 3 | fixed by the 61-day rotation (the Nov puzzle of the same day): `batches/YEAR_PLAN.md` proves at least 4 text answers in every calendar month of the year at Levels 1 and 2 (the order of the released days was changed so that the text puzzles are spread: `build_bank.py order()`) |
| 2 | 3 | the same, at least 4 in every month |
| 3 | 3 | choose 3 of: `graphs.who_has_most`, `money.cheaper_shop`, `networks.first_stop`, `shapes.classify_triangle`, `measurement.heavier_after_units`, `word_problems.who_has_more`, `logic_truth.truth_tellers`, `spatial.turns_facing`, `fractions.unit_compare` (none of them used in Nov or Dec at Level 3) |
| 4 | 3 | choose 3 of: `graphs.who_has_most`, `money.cheaper_shop`, `shapes.classify_triangle`, `measurement.heavier_after_units`, `number_properties.odd_even_rule`, `spatial.turns_facing` |
| 5 | 4 | choose 4 of: `graphs.who_has_most`, `money.cheaper_shop`, `networks.first_stop`, `shapes.classify_triangle`, `measurement.heavier_after_units`, `word_problems.who_has_more`, `logic_truth.truth_tellers`, `spatial.turns_facing` |
| 6 | 4 | choose 4 of: `measurement.heavier_after_units` (decimal form, P5 cite), `logic_truth.truth_tellers`, `shapes.classify_triangle` (angles of a triangle), `word_problems.who_has_more`, `number_properties.odd_even_rule`, `spatial.turns_facing` |

A text-capable sub-structure used in December must wait 30 days (a December sub-structure on 20 December is free again on 19 January). The new asks are free of that wait at Levels 3 to 6 because Nov and Dec do not use them (except `networks.first_stop` at Levels 4 and 6, `rate.compare_rates` and `money.cheaper_shop` where Level 2 and Level 5 have one).

**What the verifier checks now.**

* `text_min_per_month` in `taxonomy.json` (3, and 4 at Levels 5 and 6) is a **FAIL**, not a warning, for every month that is verified except November and December (`text_gate_months_exempt`): "L5: only 3 text-answer puzzles in month 01, the gate from January is 4".
* A text answer is an answer value like any other: the same word may not be the answer twice within 60 days at Levels 3 to 6 (ANSWER-WINDOW), so a closed set of four words supplies at most four answers in a window of 60 days.
* The choice rules of section 4 hold for every asks of this table that lists its options (`choice_problems`).
* A month named on the command line that is not released yet (`verify_bank.py 01`) is checked as a **draft** against every released month and the other drafts, with all structure, frame and answer-window rules.

**Still to do before the first 2027 batch:** the position of the right option among A, B, C (an even spread over a month) is not counted yet; it is only needed for the lettered `unit_heavier` puzzles and will be added when the first one is written.
