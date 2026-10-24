# Plan for text answers (audit round 5, condition C6)

Written 24 Oct 2026 for `website/teasers/`. Nothing here is released: it is the plan and the small amount of data and page support that the plan needs. The Jan to Oct puzzles are **not** written yet.

## 1. The problem in numbers

AUDIT_ROUND5 section 7 and condition C6: at present only 4 to 7 puzzles per level in 61 days have a word, a name or a letter as the answer. A year of 365 days at that rate gives 24 to 42 text answers per level, and in round 5 the count fell at some levels because the cluster fixes (C3) replaced several "who", "which way" and "which shape" puzzles by other kinds. The owner wants about 40 or more text-answer puzzles per level over the year (three or four a month), so that "type a number" is not the only thing a child ever does.

| Level | Text-answer puzzles in Nov and Dec 2026 (61 days) | Projected in 365 days | Plan |
|---|---|---|---|
| 1 | 7 | 42 | keep the rate |
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
