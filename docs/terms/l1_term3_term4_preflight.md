# Level 1 Terms 3 and 4 pre-flight (lessons 21 to 40, ages 6 to 8, Primary 1)

Status: planning only, written 23 Oct 2026. No lesson, tool, template or output file was edited. Terms 1 and 2 (lessons 01 to 20) are built, audited and fixed under `term/l1/`. This document tells the people who will write Terms 3 and 4 what each lesson is, what the templates must learn first, what went wrong in Terms 1 and 2, which decisions the owner must make, and in which order to build.

Sources read: `docs/terms/level_1_year_plan.md` (Term 3 and 4 rows, revision section, coverage matrix, SASMO table, section 5 check table), `docs/terms/owner_decisions.md` (every entry, including the late 22 Oct entries: Mi's Challenge Quest replaces the end-of-term check, printed workbooks come with payment as 5-lesson books, extension workbooks are a separate product), `docs/moe/syllabus_by_level.md` (P1 pp. 31 to 32, P2 pp. 33 to 34, P3 pp. 35 to 36, P4 p. 37, P5 p. 42, heuristics pp. 13 to 14), `docs/sasmo/g1_analysis.md` and `g1_original_problems_draft.md`, `docs/books/word_problems_g1_g2_analysis.md` and `word_problems_g1_g2_original_draft.md`, `docs/books/school_paper_wording_patterns.md`, `docs/terms/l1_term2_preflight.md` (the model for this file), `docs/terms/level_2_year_plan.md` (overlap check only), `term/l1/AUTHORING.md`, `WORDING_GUIDE.md`, `audit/TERM_WIDE_AUDIT.md`, `audit/CUTOUT_AUDIT.md`, `audit/FIXES_L11` to `FIXES_L20`, `FIXES3_L19`, `FIXES3_L20`, the finished lesson files `l11` to `l20` (identity, tiers, kits, `parent.next_materials`, `challenge_quest`), `tools/figs2.py`, `svg.py`, `b_quest.py`, and `print/make_term_books.py`.

Numbers quoted as "verified" (mirror clock times, route counts, handshakes, square counts, stick patterns, Latin squares, fewest notes, ways to spend exactly an amount, weekday cycles) were recomputed by brute force in a scratch script during this pre-flight. The lesson authors must still write their own `verify/lNN_checks.py`; nothing here replaces it.

## 0. Headline findings

1. **Nine of the ten Term 3 lessons and eight of the ten Term 4 lessons need a figure type or icon that does not exist.** The Term 2 engine (`figs2.py`) has objects, groups, array, line_up, round_table, bar_model, table, picture_equation, two-colour ten_frame and domino; `svg.py` has bundles, scatter, number_line, hundred, seq, ruler and plates. Nothing draws a clock, money, a calendar, a shape with fold lines, a dot or square grid with routes, cube stacks, a fold-and-punch square, a spot-the-difference panel, a handshake network, a picture graph or a growing stick pattern (section 3). Time (4 lessons) and money (3 lessons) are the two chains that block the most.
2. **Every lesson now needs a NAMED beyond-syllabus puzzle** (owner brief, 23 Oct; section 1.0). All 20 specs below carry one, placed at Think harder or Go further and never at Start here. Terms 1 and 2 already carry most of these under `contest_moves`; a one-field retrofit is proposed (decision D7).
3. **Kits are the weakest layer, and Terms 3 and 4 are kit-heavy** (clock hands, play money, price tags, grid tiles, strips, cards, shape pieces, paper squares, people). The cut-out audit found two Reworks (L12 strips, L19 shape cards) because piece counts were never checked against the tasks. This file fixes the supplied count and the maximum a task may use for every kit (section 4) and proposes a build-time check ("kit contract", T2).
4. **The hand-off chain is the second weakest layer.** The Term 1 audit found 7 of 9 "pencil and paper only" lines false; the cut-out audit found L10 to L11 missed. The current L20 hand-off (the Term 3 start) is already wrong for two reasons: it says "print it a week before" although workbooks now come as printed books with payment, and it says a toy clock is optional although Lesson 21 needs a cut-out clock (section 5).
5. **Money has a legal and a factual trap.** Singapore has no $20 note, so "fewest notes for $73" in the plan must read "fewest notes and coins" (5 pieces: $50, $10, $10, $2, $1, verified). Printing banknote and coin pictures may fall under reproduction rules; I have not checked them (D1).
6. **There is no Primary 1 school paper behind our wording for time, money, shapes or graphs.** The only P1 paper studied is the multiplication quiz; the P2 paper has one clock item, one money item and one picture graph. Time, money, shape and graph wording is therefore a guess until the owner supplies P1 papers on those topics (D22). This is the largest risk to the wording review.
7. **Mid-year entry is the real risk of Term 3.** A June holiday graduate enters at Lesson 21 (owner decision 4) with the holiday course only: no 2-digit sums, no strips, no multiplication. Lessons 25, 26, 28 and 29 use all three. Start here must stay within $20 and within tens bars or a number line, with the Remember re-teaching it (section 9, risk 2).
8. **The "Inquirer's toolbox" page promised by the plan does not exist in any built lesson** (no lesson file mentions it). Lesson 39 cannot "pick a tool from the toolbox" unless it teaches the seven tools itself (D10).
9. **Estimate:** about 172 agent-hours for the 20 lessons including wording review, independent audit, fix pass and two term-wide audits, about 135 hours of template engineering (about 112 if optional items are deferred). Term 2 took about 6.5 hours wall clock from pre-flight to the end of the first fix pass with parallel agents (17:06 to 23:29 on 22 Oct); the same process for Terms 3 and 4 is about 4 to 5 working days with the engineering staged as in section 11.

## 0.1 Assumptions made (change them if wrong)

- Files are `term/l1/lessons/l21.json` to `l40.json`; `term` is 3 for 21 to 30 and 4 for 31 to 40; `lesson_in_term` is 1 to 10; `id` is `l1-t3-NN` and `l1-t4-NN`; practice keys `t3l21` to `t4l40`. Family pages print "Term 3 • Lesson 4", never "Lesson 24 of 10". Taglines: Term 3 "Explain why", Term 4 "Choose and create" (the plan's year arc). The leak check allows "Lesson 1" only where `lesson_in_term` is 1, so L21, L31 and the "next lesson" of L30 and L40 must read "the first lesson of Term 4" and so on.
- Same 11-part 90-minute timing, tier rules, Mi the dolphin, private-paper safeguarding, spare-time menu, 6-minute Remember with three items, beyond-P1 statement in the guide and parent page, and no "MOE-aligned", "SASMO" or "GEP" on any child or parent page.
- Stronger-arithmetic decision stands: Start here may go past P1, but every Start here item is approachable with scaffolding. In Term 3 and 4 the arithmetic is light; the stretch is in time (L22, L23), money (L25, L26), graphs (L38) and the whole of L34.
- Tier counts as built: Start here 5 to 7, Think harder 3 to 4, Go further exactly 3, Investigation on page 5. The workbook model is 6 pages with the kit as page 6, a one-sided `LNN_Kit_Pages.pdf`, a home sheet of 5 items with separate answers, a one-page parent summary.
- Names: Mei, Ali, Ben, Siti, Ravi, Kumar, Aisha, Wei, Jenny, Lily, Jamie, Ray, Amelia. Wrong working is attributed to "a child" or "a child in another class", not to a cast name (Term 1 audit: a real child of that name may be in the group). Spread the actor role across the cast.
- Money is written $5, 50c or 50 cents. Never $0.50 or $1.50 (decimal notation is P2, p. 33) and never an amount that mixes dollars and cents.
- Fractions are words only (half, quarter). No 1/2, 1/4 (P2, p. 33).
- Time is written 4:10, with a.m. and p.m.; times are said "ten past four", "quarter to five".

## 1. Lesson specs

### 1.0 Field order, and the named beyond-syllabus item

Every spec uses this order: big idea, strand and page refs, objective, prerequisites, Remember warm-up (three items, re-taught with objects), Start here / Think harder / Go further outline with question counts, the **Beyond (named)** item, number ranges, home materials, kit with piece counts, figures and pictures, misconceptions, template needs (codes from sections 3 and 4).

**The Beyond (named) rule (proposed).** One puzzle per lesson, with a name (a puzzle title the child sees, such as "Mirror Clock"), placed at Think harder or Go further, never Start here; the tutor guide and parent page say in one line which syllabus level it belongs to ("Primary 3 idea"), with no "MOE-aligned" wording; it is original (no 7-word overlap); it is in `contest_moves` today, so only a new tutor-only field `beyond: {name, where, level_note, item_id}` is added (T1). It is not labelled "Challenge" or "Stretch" on a child page (banned words; "Challenge Quest" stays the only use). In the Quest the optional secret cave is the place for an unseen beyond puzzle (section 6).

Sources for beyond items: the SASMO gaps (time and calendar, perception, constraint grids, counting ways, symbol items), the books gaps (price of one, sum and difference), and the P2 to P4 outcomes in `syllabus_by_level.md`. No contest text is copied; where a draft in `g1_original_problems_draft.md` was the idea, the context and numbers here differ and the author must still pass the 7-word overlap check.

---

## Term 3: Explain why (lessons 21 to 30)

### Lesson 21. What Time Is It?

- **Big idea.** The clock counts in 5s: the short hand names the hour and the long hand counts the minutes.
- **Strand.** MOE P1 Measurement, Time 2.1, tell time to 5 minutes (p. 32). The holiday course never touched time. Contest tag (tutor only): clock reading (SASMO time and calendar, 7 of 100 papers).
- **Objective.** Read and set a clock for o'clock and half past; know the long hand at 12 means o'clock and at 6 means half past; count minutes in 5s round the face. Think harder: quarter past and quarter to. Go further: a clock seen in a mirror.
- **Prerequisites.** Lesson 4 (count in 5s on the 100 square; holiday Frog). Lesson 2 (numbers in order along a line, here bent into a ring).
- **Remember (6 min).** (1) Count in 5s to 60 on a line, one clap per 5. (2) Say 1 to 12 round a ring (which comes after 12?) on the kit clock. (3) "Half" is two equal parts: share 6 counters between 2 plates (Lesson 8, re-taught).
- **Start here (6 questions).** Read three o'clock clocks and write 7:00; read two half-past clocks and write 7:30; draw the hands for 4 o'clock on a printed face (drawing box); match a clock to a written time; "Which hand is the hour hand? Circle it"; one story with a choice of clocks ("The bus leaves at 8 o'clock. Circle the clock."). No quarter times.
- **Think harder (4).** Quarter past and quarter to ("the long hand points to 3; count in 5s: 15 minutes past"); hour-hand trap at half past (hand between 5 and 6 is 5:30, not 6:30); write 3:45 as "quarter to 4"; True/False on four clock statements.
- **Go further (3).** **Beyond (named): "Mirror Clock".** Lily sees the clock on the wall in the bathroom mirror. In the mirror it shows 4 o'clock: what time is it really? (8 o'clock, verified: the mirror time is 12:00 minus the real time.) Then a half-past case (mirror shows half past 9, really half past 2). Level note: reflection is not in P1; line symmetry is P4 (p. 39). Keep to o'clock and half past in Level 1 (Level 2 plan T4.9 returns to mirror clocks and digits, which is the intended spiral).
- **Gaps closed.** SASMO gap 5 (time and calendar). No school-paper evidence for P1 time wording (D22).
- **Numbers.** Hours 1 to 12; minute marks to 60; Start here only :00 and :30; Think harder :15 and :45.
- **Home materials.** The cut-out clock from the kit; a real or toy clock if there is one; pencil. No-printer fallback: a paper plate with 1 to 12 written round the edge and two strips of card for hands.
- **Kit (NK1, one page, 6 pieces to cut).** 2 clock faces (13 cm across, 1 to 12 large, minute ticks with the 5s darker; the faces are not cut), 3 hour hands (6 cm, short and wide) and 3 minute hands (8.5 cm, long and thin), each with a dot at the end that goes on the centre dot. Tasks use at most 2 faces and 2 pairs of hands at once (L23 before and after clocks; mirror pair in G); the third pair is a spare. Hands are loose, no fastener (a pin is sharp). Printed note: "Keep the clock all term (Lessons 21, 22, 23, 30)."
- **Figures.** `clock` (N1) with hour and minute hands, hidden hands, 5s labels; `table` for match-up; small objects for the bus story.
- **Misconceptions.** Hour and minute hands swapped; "the 6 means 6 minutes"; half past 5 read as 6:30; reading the hour hand by the nearer number; writing 7:3 or 7:30 as "seven thirty past"; o'clock read from the hour hand only.
- **Needs.** N1, NK1, N4 (bus icon), R6 (time answer), T4, T1, T2.

### Lesson 22. Five Minutes at a Time (new topic)

- **Big idea.** Minutes live between the hours: each step round the face is 5 minutes.
- **Strand.** MOE P1 Time 2.1 (to 5 minutes), 2.2 (a.m. and p.m.), 2.3 (h and min) (p. 32). Flagged "new topic" in the plan (split from the old What Time lesson). Contest tag: clock chunks.
- **Objective.** Read and write times to 5 minutes (4:10, 7:25, 9:50), say them ("ten past four", "20 to ten"), set them, choose a.m. or p.m. for a daily event, read "1 h 20 min". Go further: how many minutes between two times by chunks.
- **Prerequisites.** Lesson 21 (hands, 5s, o'clock, half past, quarter times). Lesson 5 (make a ten: "chunk to the next hour" is the same move). Lesson 2 (number line).
- **Remember (6 min).** (1) Count 5s round the clock to 60 and say how many steps make an hour (12). (2) Read 4:15 and 4:45 (Lesson 21, re-taught on the kit clock). (3) 50 and 10 make 60 (bonds to 10 by tens, Lesson 5 spiral).
- **Start here (6).** Read clocks at 5-minute times and write them; draw the minute hand for 3:20; "how many minutes past the hour? Count in 5s"; set the kit clock and write; a table of clock, digital time and words (`table`); one choice-of-clocks story. All :05 steps, no durations.
- **Think harder (4).** a.m. or p.m. for six daily events (Circle a.m. or p.m.: breakfast 7:00, lunch 12:30, bedtime 8:00); "1 h 20 min" read as one hour and twenty minutes; the hour-hand trap at :50 (3:50 is ten to four, hand near 4); which clock is 5 minutes later?
- **Go further (3).** **Beyond (named): "Chunk the Gap".** Mi starts to swim at 3:10 and stops at 4:05: how many minutes? Chunk to the next hour (50), then add 5: 55 (verified). Second case 2:45 to 3:20 is 35. Level note: finding a duration is P3 (p. 36, 2.2); converting hours and minutes is P2 (p. 34).
- **Gaps closed.** Time chunks (SASMO time 7 of 100); the plan's am/pm and h/min items.
- **Numbers.** 1:00 to 12:55 in 5-minute steps; durations in Go further at most 90 minutes.
- **Home materials.** The L21 clock (keep it); a real clock; pencil.
- **Kit (one small page, 8 cards to cut).** 8 event cards (picture and word: breakfast, school bus, lunch, homework, tea, bath, story, bed; 4 are a.m. events and 4 p.m.) and a two-pocket a.m./p.m. mat (no cutting). Tasks use at most 8 cards.
- **Figures.** `clock`, `time_line` (N2: a number line with times as tick labels and +minutes arcs), sun and moon icons (N4), `table`.
- **Misconceptions.** Reading the minute hand number as minutes (2 read as 2); 3:50 read as "ten past three" (the hour name changes with "to"); 4:5 for 4:05; "p.m. is night"; 12 noon is p.m.; counting the start tick as the first step.
- **Needs.** N1, N2, N4, NK1 (reuse), NK12 (event cards), R6.

### Lesson 23. Time Passes

- **Big idea.** Time can be added: one hour later, half an hour later.
- **Strand.** MOE P1 Time 2.4, durations of 1 hour or half an hour (p. 32). Start, finish and duration in general are P3 (p. 36). Contest tag: durations crossing noon; find the start.
- **Objective.** Find the time 1 hour or half an hour after a start; say how long between two clocks that are 1 hour or half an hour apart; Think harder: starts on the half hour and the quarter; Go further: a time that crosses noon, and finding the start.
- **Prerequisites.** Lessons 21 and 22 (read a clock to 5 minutes). Lesson 6 (a tens jump and a ones hop on a line is an hour jump and a half-hour hop). Lesson 7 (a difference is a gap, count up).
- **Remember (6 min).** (1) Read a clock to 5 minutes. (2) Jumps of +10 then +5 on a number line (Lesson 6, re-taught). (3) 12 jumps of 5 minutes make 1 hour; 6 jumps make half an hour.
- **Start here (6).** One hour later (set the kit clock, draw the hands, write the time: 3:00 to 4:00); half an hour later from o'clock (3:00 to 3:30); "The film starts at 4 o'clock and lasts 1 hour. It ends at ___"; two clocks one hour apart ("How long?"); a start-and-end table; a time line with the jump drawn.
- **Think harder (4).** Start at 2:30, 1 hour later (3:30), half an hour later (3:00, the hour changes); start at 4:15, half an hour later (4:45); start at 9:45, half an hour later (10:15, passes the hour).
- **Go further (3).** **Beyond (named): "Find the Start".** The ride lasts 1 hour and then Ravi walks for half an hour; he gets home at 4:00. When did the ride start? (2:30.) Also a film from 11:30 a.m. for 1 hour ends at 12:30 p.m. (crossing noon); a film from 4:15 for 1 hour and half an hour ends 5:45. Level note: finding a start from a finish and a duration is P3 (p. 36).
- **Gaps closed.** Time chunks and durations (SASMO time).
- **Numbers.** 5-minute starts; durations 30 and 60 minutes (90 only in Go further); inside one day.
- **Home materials.** The L21 clock; pencil.
- **Kit.** None new. Reuses NK1 (2 faces, 2 pairs of hands needed). The hand-off to L23 must say "keep your clock".
- **Figures.** `clock` pairs (before and after), `time_line` with arcs, `table` (start, lasts, ends).
- **Misconceptions.** Adding 1 to the minutes (3:31); half an hour after 3:30 written 3:60; 12:30 plus 1 hour written 13:30 (the 24-hour clock is P3); mixing "half an hour" with "half past"; counting the starting hour; a.m. and p.m. flip at noon forgotten.
- **Needs.** N1, N2, N4, R6.

### Lesson 24. Dollars and Change

- **Big idea.** Notes and coins make a dollar and more, and the same amount can be made in different ways.
- **Strand.** MOE P1 Money: count money in cents up to $1 and dollars up to $100 (p. 31). Decimal notation ($1.50) is P2 (p. 33): not used. Contest tag: fewest pieces.
- **Objective.** Name coins (5c, 10c, 20c, 50c, $1) and notes ($2, $5, $10, $50) by value; count a handful of mixed pieces; make an amount two ways; give change by counting up. Think harder: pay for two items. Go further: fewest pieces.
- **Prerequisites.** Lesson 4 (count in 5s and 10s). Lesson 5 (make a ten). Lesson 7 (count up for a gap). Lesson 20 (whole dollars, $1 tokens). Holiday coin combos (spiral only).
- **Remember (6 min).** (1) Count in 5s and 10s to 100. (2) Order four coins from least to most with the kit (20c, 5c, 50c, 10c). (3) 10 ten-cent coins make a dollar (100c); a $1 token is a $1 coin.
- **Start here (7).** Count mixed coins to 100c (50c, 20c, 20c, 5c is 95c); make 50c two ways; count notes ($5, $5, $2 is $12); "Which is worth more, a $2 note or a $1 coin?"; change from $5 for a $3 toy by counting up; keep cents and dollars apart (no mixed amounts). Notes within $20, cents within 100c.
- **Think harder (4).** Pay for two items ($3 and $5, pay $10, change $2); "All the ways to make 50c with 10c and 20c coins" (3 ways: five 10c; three 10c and one 20c; one 10c and two 20c, verified); change from $50 for a $37 toy.
- **Go further (3).** **Beyond (named): "Fewest Notes and Coins".** What is the fewest number of notes and coins that make $73? ($50, $10, $10, $2, $1: 5 pieces, verified; note there is no $20 note.) Also: pay $50 for a $37 toy and get the change in the fewest pieces ($10, $2, $1: 3). Level note: optimising a way to pay is not a syllabus item; money to $100 is P1.
- **Gaps closed.** Books: money stories (23 of 101). Plan: the whole money strand (the holiday course has coins only).
- **Numbers.** Cents to 100c; dollars to $20 at Start here, to $100 at Think harder and Go further. Whole dollars only.
- **Home materials.** The play money from the kit; the $1 tokens from Term 2 Lesson 10 (or 5 counters); real coins only if a grown-up is present (small things; keep from younger children).
- **Kit (NK2, two pages, 29 new pieces to cut).** Coins as rounded squares 24 mm: 4 x 5c, 6 x 10c, 4 x 20c, 2 x 50c (16). Notes 70 x 35 mm: 5 x $2, 4 x $5, 3 x $10, 1 x $50 (13). $1 coins come from the 30 tokens of Term 2 Lesson 10. Task maxima (the contract): 5c x 2, 10c x 5, 20c x 3, 50c x 2; $2 x 5, $5 x 4, $10 x 3, $50 x 1, $1 x 5. Pieces are labelled by value and differ in shape and shade, not colour alone. Stylised play money, not facsimile (D1). Hand-off line: "Keep the money all term (Lessons 24, 25, 26, 30)."
- **Figures.** `money` row (N5), `price_tag` (N5), `number_line` with a $ prefix for counting up, `table`.
- **Misconceptions.** A bigger coin is worth more; 50c is more than $1 because 50 is more than 1; counting each piece as 1; adding cents to dollars; "$2" as two notes; change given as the amount paid; a missing unit.
- **Needs.** N5, NK2, N4, R7 (money answer formats), D1.

### Lesson 25. Price Tags: Compare and Choose (new topic)

- **Big idea.** Which costs more, and by how much? The difference is the gap.
- **Strand.** MOE P1 Money (dollars up to $100, p. 31) with add and subtract within 100 (p. 31). Flagged "new topic". Books: money stories are 23 of 101 problems; compare and sum-and-difference types.
- **Objective.** Compare two or three prices (cheaper, cheapest, costs more), find how much more by counting up or with strips, find the total of two items, find change from $10, $20 or $50. Think harder: three prices, and a total with a difference. Go further: buy two things and find the change.
- **Prerequisites.** Lesson 24 (dollars, play money). Lesson 7 (count up for the gap). Lesson 12 (two strips and the gap bracket). Lesson 10 (read it twice, one operation per step). Lesson 3 (order numbers).
- **Remember (6 min).** (1) Which is greater, 36 or 63 (tens bars, Lesson 3). (2) The gap between 28 and 35 by counting up (Lesson 7). (3) Draw two strips for "Ali has 8 and Mei has 3" and bracket the gap (Lesson 12, taught again; this is the plan's strip warm-up).
- **Start here (6).** Compare two price tags ("Circle the cheaper one"); "How much more does the book cost than the pen?" (gap, within $20); the total of two items; the cheapest of three tags (order); change from $10 for a $7 item; one story with a strip. Prices $1 to $19.
- **Think harder (4).** Three prices: the difference between the dearest and the cheapest; a total and a difference ("A pen and a ruler cost $14 together; the ruler costs $4 more. How much is the pen?" Pen $5, ruler $9, verified); change from $50 for a $27 item; "Is $30 enough for a $18 book and a $15 toy? Circle Yes or No."
- **Go further (3).** **Beyond (named): "The Hidden Price".** A cake costs $12 more than a pie. A cake and a pie cost $52 together. How much does the cake cost? ($32; the pie is $20, verified.) Also: Mei has $100, buys a bag for $27 and a hat for $16, and finds her change ($57). Level note: sum and difference with a strip is ordinary Book 2 work and Level 2 Go further; it is beyond P1.
- **Gaps closed.** Books gap: multi-step money stories; "how much more" reading traps (the cheaper or the dearer). The plan's price-compare lesson (flagged new).
- **Numbers.** Start here within $20; Think harder within $50; Go further within $100; whole dollars.
- **Home materials.** The L24 play money (keep it); the price tags from the kit; pencil.
- **Kit (NK3, one page, 12 tags to cut).** 12 price tags (50 x 28 mm): 9 printed with an item picture and a price ($2 to $27), 3 blank for the child to write a price. Tasks use at most 4 tags at once and the Explore uses 6. The play money from Lesson 24 is reused.
- **Figures.** `price_tag` (N5), `bar_model` compare with $ labels (exists), `number_line` with a $ prefix, `table`.
- **Misconceptions.** The bigger number of items must be dearer; subtracting to find a total; reporting the gap as the price; "cheaper" and "dearer" swapped; 2-digit subtraction slips; forgetting the unit; the first digit decides the order.
- **Needs.** N5, NK3, N4 (item icons), R7.

### Lesson 26. The School Shop

- **Big idea.** Make a plan that fits a budget, and list every way to be sure.
- **Strand.** MOE P1 Money applied (p. 31). Contest tag: spend exactly an amount; listing all ways (SASMO counting ways, 5 of 100).
- **Objective.** Choose items to fit a budget, find the total and the change, and list all the ways in a table without repeating one or missing one. Think harder: three items; all the ways to spend exactly $20. Go further: all the ways with three prices.
- **Prerequisites.** Lessons 24 and 25. Lesson 16 (a table of facts). Lesson 17 (all the ways to share 12). Lesson 3 (every number from the cards: start with a rule). Lesson 15 (repeated addition for 3 pens at $4).
- **Remember (6 min).** (1) Add two prices to make $10 (3 and 7; Lesson 5). (2) 3 pens at $4 each, repeated addition (Lesson 15, re-taught). (3) List every pair of whole numbers that make 6, starting at 1 (1 and 5, 2 and 4, 3 and 3): a rule for listing.
- **Start here (6).** Pick two items from a tag board whose total is exactly $10 (prices $2 to $8); the total of two items; change from $10; "Can Ali buy a $6 and a $5 with $10? Circle Yes or No"; the cost of 3 of one item. Budgets $10 and $20.
- **Think harder (4).** **Beyond (named): "Exactly $20".** Pens cost $4 and books cost $6. List all the ways to spend exactly $20: 5 pens, or 2 pens and 2 books (verified, 2 ways). A table with a row for each way and a check for repeats; three items and the change; "Is this list complete? Circle Yes or No." Level note: systematic listing of ways is contest-style (SASMO), not a syllabus outcome; it sits at Think harder by owner decision 6.
- **Go further (3).** All the ways to spend exactly $20 on $2, $5 and $10 items (6 ways, zero of an item allowed, verified: two $10; one $10 and two $5; four $5; five $2 and one $10; five $2 and two $5; ten $2). A second budget with two prices. Write your own "exactly" puzzle for a partner.
- **Gaps closed.** Counting ways (SASMO 5 of 100); reading "exactly".
- **Numbers.** Budgets $10 and $20; prices $2 to $10; at most 10 of any item.
- **Home materials.** The play money and price tags (keep both); pencil.
- **Kit.** None new. Reuses NK2 and NK3: tasks lay out at most $10 x 2, $5 x 4 and $2 x 5 and 6 tags; a way with more than five $2 notes is written, not laid out. A shop board and a ways table are printed on the workbook pages, not as a kit.
- **Figures.** `price_tag`, `table` (rows of ways with boxes), item icons (N4).
- **Misconceptions.** Stopping at the first way; the same way written in two orders counted twice; "0 books" not allowed as a way; assuming all the money must be spent when the question says change; changing the prices; mixing "exactly" and "about".
- **Needs.** N5, N4, `table` (exists), R7.

### Lesson 27. Fill the Grid (new topic)

- **Big idea.** Each row and each column has one of each, so every empty cell has a reason.
- **Strand.** Not in MOE P1. SASMO constraint grids (3 of 100, all Section B, 4 marks each). Thin evidence: the plan and the pre-flight call this the safest lesson to skip; open question 10 asks whether it deserves a full lesson (D13). Holiday Logic Lab grid (spiral only).
- **Objective.** Complete a 3 by 3 grid with three kinds of picture so each row and column has each kind once, and say why a cell must be that picture. Think harder: a grid with only two clues. Go further: a 4 by 4 grid with digit clues.
- **Prerequisites.** Lesson 8 (balance, one side decides the other: elimination in a small way). Lesson 11 (deduce a place from clues). Lesson 3 (systematic cases). Holiday Logic Lab.
- **Remember (6 min).** (1) A row has a circle and a square: which kind is missing? (3 cards). (2) Digits 1 to 4: which is missing from 1, 3, 4? (3) A rule said aloud: "one of each in every row".
- **Start here (6).** A 3 by 3 grid with one empty cell in each row; a grid with six cells filled and a choice "I know because the row has... / the column has..." (multiple choice, not a written reason, rule 25); a check "Is this row correct? Circle Yes or No". Three kinds of picture only.
- **Think harder (4).** A 3 by 3 grid with two clues (verified: with the top-left a circle and the centre a square there is exactly one grid); "Is this grid correct? Circle Yes or No" with a repeat hidden in a column; "How many cells could be a star here? Write 0, 1 or 2."
- **Go further (3).** **Beyond (named): "Four by Four".** A 4 by 4 grid, digits 1 to 4, one of each in every row and column, with four digits given (verified: four well-placed clues give a single grid; the author must prove uniqueness by brute force). Also the same with 2 by 2 boxes. Level note: this is a logic puzzle, not a syllabus topic.
- **Gaps closed.** SASMO gap: constraint grids (thin evidence, no promise).
- **Numbers.** Three symbols (Start here, Think harder); digits 1 to 4 (Go further).
- **Home materials.** The tile set from the kit; a pencil. Fallback: nine small things of three kinds (buttons, coins, pasta).
- **Kit (NK4, one page, 16 tiles to cut).** Two printed mats (3 by 3, 4 by 4; no cutting) and 16 square tiles of 22 mm: 4 symbols (circle, square, triangle, star) x 4, each also printed with a digit 1 to 4 so the same tiles serve both grids. A 3 by 3 task uses 9 tiles (3 symbols x 3); the 4 by 4 task uses all 16. Symbols differ by pattern as well as shade.
- **Figures.** `table` with thick 2 by 2 box lines and picture cells (N7), symbols reused from `picture_equation`.
- **Misconceptions.** Checking the row but not the column; guess and rub out; inventing a "diagonal rule"; filling the same order in every row; repeating a digit in the 4 by 4.
- **Needs.** N7, NK4, symbols (exist).

### Lesson 28. Make a Table (new topic)

- **Big idea.** A table finds the 20th picture without drawing 20.
- **Strand.** MOE P1 number-sequence patterns (1.6, p. 31); shape patterns are P2 (p. 34). Move: make a table. Holiday growing sticks (spiral only). Contest tag: growing patterns with a rule.
- **Objective.** Build a growing stick pattern, fill a table of pictures and sticks, find the next terms, then the 10th and 20th from the table. Go further: work back from a total of sticks.
- **Prerequisites.** Lesson 4 (a sequence with a growing gap). Lesson 13 (double a number). Lesson 16 (count in 2s). Lesson 12 (a strip shows equal steps).
- **Remember (6 min).** (1) Count in 2s from 3 (3, 5, 7, 9). (2) Double 6 and double 7 (Lesson 13). (3) Make a two-row table "pictures / sticks" and fill one row from a drawing of 1, 2 and 3 triangles.
- **Start here (6).** Count the sticks in 1, 2, 3 triangles in a row (3, 5, 7); fill a table for 1 to 5; "How many sticks for 5 triangles?" (11); a square pattern (4, 7, 10) and the next term (13); "How many more sticks each time?"
- **Think harder (4).** The 10th and 20th term from the table (21 and 41 sticks, verified; the rule "double the triangles and add 1" in words); "Can 20 sticks make a row of triangles? Circle Yes or No." (No: every number of sticks in this pattern is odd, which links to Lesson 14); a table with a mistake.
- **Go further (3).** **Beyond (named): "Picture 100".** How many sticks for 100 triangles in a row? (201.) Also 100 squares in a row (301); and "31 sticks make how many triangles?" (15) and "37 sticks make how many squares?" (12), all verified. Level note: finding the 100th term from a rule is P4/P5 pattern thinking; letters for an unknown are P6 (p. 43), so the rule is said in words only.
- **Gaps closed.** The plan's growing-pattern lesson; SASMO number sequences (10 of 100) in a new form.
- **Numbers.** Up to 5 pictures drawn, up to 20 by the table, 100 only at Go further.
- **Home materials.** 14 paper strips from the kit (never matches or toothpicks); pencil. Fallback: draw the sticks.
- **Kit (NK13, one page, 14 strips to cut).** 14 short strips (60 x 8 mm). A task builds at most 5 triangles (11 strips) or 4 squares (13 strips); the table tasks are drawn.
- **Figures.** `stick_pattern` (N8: triangles or squares in a row, n pictures, hide the last), `table`.
- **Misconceptions.** 5 triangles as 5 x 3 = 15 sticks (shared sticks counted twice); "double" without the +1; an off-by-one in the table; trying to count 20 pictures one by one; testing the rule on one case only.
- **Needs.** N8, NK13, `table`.

### Lesson 29. Spot the Mistake (new topic)

- **Big idea.** Check with a different method; a wrong answer leaves a clue.
- **Strand.** Not an MOE content item: error analysis across adding, taking away, time and money. Process strand, reasoning and communicating (pp. 13 to 14). Contest tag: none.
- **Objective.** Find the one wrong step in a worked sum, say what the right step is, and check an answer by a different method (adding back, counting up, "about" what size). Go further: write a wrong answer for a partner.
- **Prerequisites.** Lesson 7 (check a take away by adding back). Lesson 10 (one operation per step). Lesson 6 (tens jump). Lessons 23 to 26 for the clock and money contexts.
- **Remember (6 min).** (1) Check 30 - 12 = 18 by adding 18 + 12 (Lesson 7). (2) 34 + 20 by a tens jump (Lesson 6). (3) One hour later than 3:30 (Lesson 23, re-taught).
- **Start here (6).** Six worked sums, each with exactly one wrong step, as multiple choice on the steps ("Which step is wrong? (1) (2) (3)"); "Is the answer right? Circle Yes or No. Check by adding back." One clock item and one money item. Within 100.
- **Think harder (4).** Say which step is wrong and write the right answer; two ways to check the same sum; "A child in another class says 45 + 38 = 73. Is that right? How could you check?"; a wrong time-after-an-hour.
- **Go further (3).** **Beyond (named): "Does It Make Sense?"** Which answer cannot be right without working it out: 49 + 38 = 117 (about 50 + 40 = 90, so 117 is too big; the answer is 87, verified). Level note: estimating and rounding are P4 (p. 37, 1.5): the lesson says "about" and "near", never "round". Then: write a wrong sum for your partner, with the mistake on one step.
- **Gaps closed.** Books gap: reading and checking; cross-strand reasoning (plan).
- **Numbers.** Within 100; times to 5 minutes; dollars within $50.
- **Home materials.** The 8 mistake cards; pencil.
- **Kit (NK5, one page, 8 cards to cut).** 8 worked-sum cards (4 right, 4 with one mistake) and a two-pocket mat RIGHT / WRONG (no cutting). The Explore sorts all 8.
- **Figures.** `steps` lines (exist), `number_line`, `table`; no new figure.
- **Naming.** Wrong working is "a child" or "a child in another class" (Term 1 audit; D18).
- **Misconceptions.** A neat answer must be right; checking by redoing the same way; fixing the wrong step but not the steps after it; thinking a mistake is a failure; changing the question.
- **Needs.** NK5, T1.

### Lesson 30. Calendar Detective (added), and Mi's Challenge Quest

- **Big idea.** Days and weeks go round in a cycle of 7.
- **Strand.** Time: days of the week and weeks. Not a listed MOE P1 outcome (P1 Time 2.1 to 2.4 are clock items, p. 32); flagged for tutor review. Contest tag: day-of-week cycles (SASMO time and calendar, at Think harder by owner decision 6).
- **Objective.** Put the days in order, say the day 3 days after or before a day, read dates on a month page (a week after the 5th), and use a week as a unit. Think harder: "two days after the day before yesterday"; the 10th day from Monday. Go further: dates on the same weekday.
- **Prerequisites.** Lesson 11 (1st to 10th). Lesson 16 (count in equal jumps). Lesson 21 (a cycle, the 12 on a clock). Lesson 28 (a table).
- **Remember (6 min).** (1) Jumps of 7 along a calendar row from 3 (3, 10, 17). (2) 1st to 10th (Lesson 11, re-taught). (3) The day cards in order, Monday to Sunday.
- **Start here (5).** Days in order; the day before Wednesday; 3 days after Friday (Monday); "how many days in a week"; a week after the 5th on the month page.
- **Think harder (3).** "Today is Friday. Two days after the day before yesterday is ___" (today: Friday); the 10th day from Monday, counting Monday as day 1 (Wednesday, verified); a fortnight is 14 days.
- **Go further (3).** **Beyond (named): "Hundred Days Later".** Today is Monday. What day is it 100 days later? (Wednesday: 14 weeks and 2 days, verified.) Also: which dates in a month starting on a Wednesday fall on Wednesdays (1, 8, 15, 22, 29) and "the date three weeks after the 6th" (27th). Level note: dividing by 7 with a left-over is P3 (remainder, p. 35).
- **Gaps closed.** SASMO time and calendar; vocabulary "a week", "a fortnight" (books gap, vocabulary).
- **Numbers.** Weeks up to 4; "days later" up to 10 at Think harder, 100 at Go further.
- **Quest in this lesson.** Mi's Challenge Quest takes minutes 35 to 55 straight after the brain break (as in Lesson 20). Explore 10 and Mini-lesson 9 minutes; Start here workbook 25 minutes; pages 3 to 5 are for home; the exit ticket is not done live. See section 6 for the gates.
- **Home materials.** A calendar page of the current month (or the kit page); the day cards; the Quest Log kept closed in its envelope; a quest partner; pencil.
- **Kit (NK14, one page, 7 cards to cut).** A month page for a 31-day month that starts on a Wednesday (no cutting; no real year or public holidays) and 7 day cards (Monday to Sunday). The Quest needs no kit; the clock and money from earlier lessons are optional aids, not required.
- **Figures.** `calendar` (N6: month grid, highlighted days, hidden cells, week strip).
- **Misconceptions.** Counting today as day 1 in "3 days after"; Sunday to Monday not wrapping; "a week later" as 8 days (inclusive counting); "fortnight"; confusing date and weekday; "the day after tomorrow".
- **Needs.** N6, NK14, Quest builder (T5), `table`.

---

## Term 4: Choose and create (lessons 31 to 40)

### Lesson 31. Half and Quarter

- **Big idea.** Equal parts: a half is one of two equal parts and a quarter is one of four, whatever the shape.
- **Strand.** MOE P1 2D Shapes: half circle and quarter circle (1.1, p. 32). Fractions as numbers, notation and comparison are P2 (p. 33), so only words and shapes here. Holiday shape names (spiral only).
- **Objective.** Fold a circle into halves and then quarters; say whether a shape is cut into equal parts; name a half circle and a quarter circle; show two halves make a whole and four quarters make a whole. Think harder: halves of a square in several ways. Go further: are all halves the same shape?
- **Prerequisites.** Lesson 17 (share equally between 2). Lesson 14 (an odd number cannot be shared into two equal parts). Lesson 13 (a double). Lesson 8 (two plates with the same amount).
- **Remember (6 min).** (1) Share 8 counters between 2 plates; both plates must match (Lesson 8). (2) Name a circle, a square, a rectangle and a triangle and count the sides (holiday shapes). (3) Fold a paper square so the edges meet; open it and trace the fold.
- **Start here (6).** "Is this circle cut into halves? Circle Yes or No" (three pictures, one with unequal parts); colour half of a circle and a quarter of another; ring the half circle and the quarter circle among shapes; "How many quarters make a whole circle?" (4); fold-and-draw: draw the fold line on a printed square. Words only; no 1/2 notation (D16).
- **Think harder (4).** Halves of a square in three ways (vertical, horizontal, diagonal) and check each by folding; "Which cut makes quarters? Circle the picture"; a square cut into two unequal parts called "halves" (True or False); two halves of a circle placed together.
- **Go further (3).** **Beyond (named): "Same Half, Different Shape".** A rectangle 4 squares wide and 2 high is cut into two halves in three ways (down the middle, along the middle, in a staircase). Are the two halves the same shape? Do they have the same number of squares? (4 squares each in every case, verified.) Level note: equal area in different shapes is a P2 and P3 fraction and area idea (pp. 33 and 36).
- **Gaps closed.** The plan's half/quarter lesson; MOE 2D shapes 1.1.
- **Numbers.** Wholes of 2 and 4 parts only; grids of 8 squares or fewer.
- **Home materials.** Paper circles and squares from the kit (a grown-up cuts them; children only fold); a pencil; crayon.
- **Kit (NK6, one page, 10 pieces to cut).** 4 circles (9 cm), 4 squares (9 cm) and 2 grid rectangles (4 by 2 squares of 2 cm). The Explore folds 2 circles (one to fold in half and again, one kept whole to compare); Think harder uses 3 squares for three ways; Go further uses the 2 grid rectangles with colouring in the workbook, so the spare square and spare circle are the buffer. Nobody cuts in the lesson.
- **Figures.** `shapes2d` (N9: circle, half circle, quarter circle, square, rectangle, triangle with fold lines, shading and equal-part marks), `grid` (N10) for counting squares.
- **Misconceptions.** Any two parts are halves; four parts are quarters even if unequal; a fold line that does not pass through the middle; the half circle drawn as a circle with a line; "half" means the left side; fractions are written 1/2 (not taught here).
- **Needs.** N9, N10, NK6.

### Lesson 32. Build the Figure

- **Big idea.** Make big shapes from small shapes, and find the small shapes inside a big one.
- **Strand.** MOE P1 2D Shapes: form figures from shapes (1.2) and identify the shapes in a figure (1.3), p. 32. Contest tag: counting figures (SASMO, 6 of 100: squares, triangles, parts).
- **Objective.** Build a picture (house, boat, robot) from given pieces; name and count the shapes in a figure by kind; two small shapes can make a bigger one (two triangles make a square). Think harder: count every triangle in a figure. Go further: the same figure with the fewest pieces.
- **Prerequisites.** Lesson 31 (a square cut along its diagonal gives two triangles; a half circle). Lesson 15 (rows of equal squares). Holiday shape names. Lesson 36 is later and not needed.
- **Remember (6 min).** (1) Name the shape by its sides and corners. (2) Fold a square along its diagonal and name the two shapes (Lesson 31, re-taught). (3) Count the squares in a 2 by 3 rectangle by rows.
- **Start here (6).** Build a house from 4 given pieces and draw it; name the shapes in a figure (how many triangles, rectangles, circles); two triangles make one ___; "Which shapes make this boat? Colour them"; a figure on a grid to be counted.
- **Think harder (4).** **Beyond (named): "Every Triangle".** A triangle with 2 lines from the top to the bottom edge: how many triangles are there in all? (6: three thin ones, two made of two, one whole, verified; with 3 lines it is 10.) Level note: counting hidden and overlapping shapes is not a P1 outcome; identifying the shapes in a figure is. Also count the rectangles in a window picture; the odd shape out in a figure.
- **Go further (3).** Make a 2 by 3 rectangle (6 by 9 cm) from squares and rectangles with the fewest pieces (3: three 3 by 6 rectangles, against 6 squares; verified); a four-line triangle (10 triangles); write a figure for a partner to count.
- **Gaps closed.** SASMO counting figures (6 of 100); MOE 1.2 and 1.3.
- **Numbers.** Up to 12 pieces in a figure; triangle counts up to 10.
- **Home materials.** The piece set from the kit; pencil.
- **Kit (NK7, one page, 20 pieces to cut).** On a 3 cm unit: 6 squares (3 cm), 3 rectangles (3 by 6 cm), 6 triangles (half a 3 cm square), 2 half circles (6 cm across), 2 quarter circles (3 cm radius), 1 circle (3 cm). Contract: Start here tasks use at most 6 pieces of at most 4 kinds (house: 1 rectangle, 1 triangle, 2 squares); the Go further 2 by 3 task uses the 3 rectangles or up to 6 squares. The author fills the "used by" column against the final tasks.
- **Figures.** `shapes2d` composed figures (N9), `grid` (N10).
- **Misconceptions.** Counting only the small triangles; counting one triangle twice; a rectangle that is not a square called a square; a shape upside down is not that shape; not seeing the shape made of two pieces.
- **Needs.** N9, N10, NK7.

### Lesson 33. Copy on the Grid

- **Big idea.** A grid lets us say exactly where things are and copy them exactly.
- **Strand.** MOE P1 2D Shapes: copy figures on a dot or square grid (1.4, p. 32). Coordinates are not in the syllabus anywhere (docs note); here only "2 right, 1 up". Contest tag: counting routes (SASMO counting ways).
- **Objective.** Copy a figure on a dot grid, describe a move as "2 right, 1 up", follow directions, and count routes that only go right or up. Go further: routes on a larger grid by adding.
- **Prerequisites.** Lesson 2 (a number line, moves right). Lesson 6 (a jump). Lesson 15 (rows and columns). Lesson 11 (position words).
- **Remember (6 min).** (1) Rows and columns of an array (Lesson 15, re-taught). (2) Put a counter on a grid and move it "right 2, up 1". (3) Copy a three-line shape by counting dots across.
- **Start here (6).** Copy a figure on a dot grid (count dots: "2 across, 1 down"); the move from A to B ("___ right, ___ up"); follow the directions and draw the line; "Which copy is exactly the same? Circle the picture"; fill the missing corner of a rectangle.
- **Think harder (4).** **Beyond (named): "Count the Routes".** A counter goes from the bottom left to the top right of a grid, moving only right or up. A grid 2 across and 1 up has 3 routes; 2 across and 2 up has 6 (verified). Level note: counting paths is SASMO counting ways, not a syllabus topic. Also directions with a turn.
- **Go further (3).** Routes on a 3 across, 2 up grid (10) and 3 across, 3 up (20), by writing at each corner the number of ways to reach it (add the two corners before it, verified); a route that must pass a given corner.
- **Gaps closed.** MOE 1.4; SASMO counting ways (routes).
- **Numbers.** Grids up to 4 by 4 dots for copying; route grids up to 3 by 3 squares.
- **Home materials.** A counter; pencil; a ruler only if the child has one.
- **Kit (NK9, one page, no cutting).** A mat with 3 route grids and 2 copy grids; the counter is any button from home.
- **Figures.** `grid` (N10: dot or square grid, a figure to copy, route arrows, a blank right half to copy into, counts at corners).
- **Misconceptions.** Counting dots instead of steps ("2 right" is 3 dots); copying by eye; left and right swapped; diagonal moves; counting a route twice; missing a route.
- **Needs.** N10, NK9, R8.

### Lesson 34. Cubes and Views

- **Big idea.** The same thing looks different from the top, from the front and when it is folded.
- **Strand.** Not in MOE P1. 3-D shapes are P2 (p. 34); drawing cubes on an isometric grid is P5 (p. 42). SASMO spatial moves (cube stacks, top view, paper folding, 6 of 100, all Section A). Fold once and punch is Think harder by owner decision 6.
- **Objective.** Build a stack of cubes from a picture and count all the cubes including the hidden one; read a top view as a square grid of numbers; fold a paper once, mark one hole, and say where the holes are when it is opened. Go further: fold twice.
- **Prerequisites.** Lesson 15 (rows of squares). Lesson 13 (doubling). Lesson 11 (front, behind, between).
- **Remember (6 min).** (1) Count the squares in a 2 by 3 array by rows. (2) Double 1, 2 and 4 (Lesson 13). (3) Stack 3 blocks and say which one you cannot see.
- **Start here (6).** Build from a picture of a stack of 5 cubes and count them; "How many cubes can you not see?"; match a stack to its top view; colour the top view of a row of 3 stacks; fold a printed square once along a line and draw where the fold is.
- **Think harder (4).** The top view as numbers (each square shows how many cubes are in that stack); fold once and mark one hole: how many holes when it is opened? (2); where are they? (Same distance from the fold, verified by folding in the lesson.)
- **Go further (3).** **Beyond (named): "Fold Twice, Punch Once".** A square is folded in half, then in half again, and one hole is punched through all the layers: how many holes when it is opened? (4, verified: each fold doubles the layers.) Also a stack with a hidden cube (a 2 by 2 base with heights 3, 1, 2, 2 has 8 cubes). Level note: not in the syllabus.
- **Gaps closed.** SASMO gap 4 (visual perception and 3-D), partly.
- **Numbers.** Base grid at most 3 by 3; stack height at most 3; at most 12 cubes.
- **Home materials.** 12 small blocks of the same size (building bricks or dice), 4 sheets of square paper (from the kit), a pencil to mark holes (no real punching). **No blocks at home**: the fallback is drawn stacks and the top-view grid with counters (D14).
- **Kit (NK6 type, one page, 4 squares).** 4 paper squares (10 cm) with a faint centre mark. Tasks use at most 3 squares (fold once, fold twice, one try-again) and 1 spare.
- **Figures.** `cube_stack` (N11), `fold_punch` (N12).
- **Misconceptions.** Not counting the hidden cube; counting faces, not cubes; a top view drawn as a picture instead of numbers; one hole after one fold; the hole on the fold line; the hole moved when unfolded.
- **Needs.** N11, N12, NK6, D14, D15.

### Lesson 35. Spot It: Same, Different, Missing (added)

- **Big idea.** Compare one feature at a time.
- **Strand.** Not in MOE P1. SASMO visual perception (8 of 100, all Section A). The analysis calls this thin evidence and partly a practice effect; no promise of contest results (D13). Plan note: warm-up revisits cube and cm measuring.
- **Objective.** Find the differences between two pictures one feature at a time (number, colour, size, turn); find the odd one out and say which feature differs; find the missing piece of a pattern tile. Go further: make your own odd one out.
- **Prerequisites.** Lesson 32 (shapes and their sides). Lesson 14 (pairs). Holiday cm measuring (spiral).
- **Remember (6 min).** (1) Compare two lines by laying squares along them. (2) Name four features: colour, size, number, turn. (3) Find what changed between two rows of counters.
- **Start here (6).** Spot 3 differences between two pictures, one feature each; "What is different? Circle number, colour, size or turn"; same or different (Circle Yes or No); count the differences.
- **Think harder (4).** Odd one out among five shapes (say which feature); the missing piece of a 2 by 2 tile pattern (four options); a shadow that matches a shape (no turning yet); "Which two are the same picture turned?"
- **Go further (3).** **Beyond (named): "Shadow Match".** Which shadow belongs to the shape when the shape is turned? Choose from four. Level note: turning shapes is P2 (shape patterns by orientation, p. 34). Also: build an odd one out for a partner and write the feature.
- **Gaps closed.** SASMO gap 4 (perception); practice-effect caveat stated to the owner.
- **Numbers.** Pictures of at most 6 objects; tile patterns of 2 by 2.
- **Home materials.** The pair cards; a pencil; the ones squares from Term 1 or any squares of the same size.
- **Kit (NK8, one page, 12 cards to cut).** 12 cards in 3 sets of 4: in each set three cards are the same and one differs in one feature. Tasks use all 12 in Explore (3 rounds of 4).
- **Figures.** `panel` (N13): spot-the-difference pairs, odd one out rows, tile with a missing piece, shadow and turn options, built from shape primitives with turns; objects icons.
- **Misconceptions.** Comparing everything at once; seeing a turn as a different shape; flip (mirror) mistaken for a turn; guessing; "looks different" is not "is different"; position differences missed.
- **Needs.** N13, NK8, N4.

### Lesson 36. Count Everything

- **Big idea.** Count with a system so you miss none and count none twice.
- **Strand.** Cross-strand counting of figures, ways and routes (SASMO, 6 + 5 of 100). Not an MOE P1 item.
- **Objective.** Count the squares in a 2 by 2 grid by size (5), count handshakes in a group of 4 by pairing (6), count outfits from two lists (3 tops and 2 pairs of shorts: 6), and count routes with two stages. Go further: group of 5 or 6, two-stage routes.
- **Prerequisites.** Lesson 15 (groups of; arrays). Lesson 5 (4 + 3 + 2 + 1 by making tens). Lesson 33 (routes). Lesson 32 (counting figures). Lesson 26 (list without repeats).
- **Remember (6 min).** (1) Count dots in a 3 by 4 array by rows. (2) Add 4 + 3 + 2 + 1 by making tens (Lesson 5). (3) List the pairs of 3 children: Ali-Mei, Ali-Ben, Mei-Ben.
- **Start here (6).** Count the squares in a 2 by 2 grid (sizes 1 and 2: 5); list outfits from 2 tops and 2 shorts in a table (4); count the paths in a small map; how many pairs from 3 children (3).
- **Think harder (4).** **Beyond (named): "Handshake Party".** Four children each shake hands once with every other child. How many handshakes? (6, verified.) Draw dots joined by lines; the pairing sum 3 + 2 + 1. Also: 3 tops and 2 shorts (6 outfits). Level note: pairing sums are contest-style (SASMO and owner decision 6), not syllabus; the table (groups of) is P1.
- **Go further (3).** Five children (10) and six children (15), verified; squares in a 3 by 3 grid (14, verified); a two-stage map with a direct path (2 paths, then 4 paths, plus 1 direct, makes 9 routes).
- **Gaps closed.** SASMO counting ways and counting figures.
- **Numbers.** Groups of 3 to 6; grids up to 3 by 3; counts to 20.
- **Home materials.** Paper people from the kit, or six coins; pencil.
- **Kit (NK15, one page, 8 people to cut).** 8 paper people in varied shapes (repeat of the Term 2 Lesson 1 strip so that a new joiner does not need the old one). Tasks use at most 6.
- **Figures.** `network` (N14: n dots in a ring with lines), `grid` squares highlighted (N10), `table`.
- **Misconceptions.** Counting A-B and B-A as two handshakes (4 x 3 = 12); leaving out the last person; counting only the 1 by 1 squares; adding where multiplying is meant; listing with no rule; ignoring the direct path.
- **Needs.** N14, N10, NK15.

### Lesson 37. Make Your Own Graph (new topic)

- **Big idea.** Ask a question, sort the answers, then picture the answer.
- **Strand.** MOE P1 Statistics: read and interpret picture graphs (p. 32). Collecting, sorting and drawing a graph is the plan's reading and is flagged (the outcome says read and interpret); tally marks are not named; scales are P2 (p. 34). Holiday picture graph (spiral only).
- **Objective.** Sort a mixed set into kinds, count with tally marks, draw a picture graph with 1 picture = 1, answer how many and how many more. Think harder: choose a question the data can answer. Go further: draw with 1 picture = 2.
- **Prerequisites.** Lesson 3 (compare two sets). Lesson 7 (a difference is a gap). Lesson 16 (count in 2s). Holiday picture graphs.
- **Remember (6 min).** (1) Read a 1-to-1 picture graph: how many more? (2) Count in 2s to 20. (3) Sort 10 objects by colour into piles.
- **Start here (6).** Sort 12 pictured objects into 3 kinds (circle, count, tally); draw the picture graph with a title and a key; "How many more ___ than ___?"; "How many in all?"; "Which has the fewest?" Data are made up (Mi asked 12 dolphins) or counted from the child's own household set, never a class poll (D17).
- **Think harder (4).** Which question can this sorted set answer? (multiple choice); the graph with a title missing; tally to graph; a graph with one picture shown in the wrong column.
- **Go further (3).** **Beyond (named): "One Picture Is Two".** Draw the graph with 1 picture = 2 for 8 apples, 6 pears and 4 plums (4, 3, 2 pictures); what do you do with 7? (half a picture.) Level note: picture graphs with a scale are P2 (p. 34).
- **Gaps closed.** The plan's data-collection lesson; MOE picture graphs.
- **Numbers.** Up to 4 kinds; counts up to 10 at Start here; up to 12 at Go further.
- **Home materials.** 12 to 20 things to sort from around the house (spoons, socks, shoes, buttons; not food), coloured pencils.
- **Kit (NK10, one page, no cutting).** A graph mat with 5 columns and 8 rows and a key box. No tiles: the child draws or colours small pictures.
- **Figures.** `picture_graph` (N15: columns or rows of icons, key "each picture = n", half pictures, tally, hidden cells), `table`.
- **Misconceptions.** Pictures of different sizes or with gaps; no title or key; counting the pictures for the number when the key says 2; starting at different baselines; a question with only one answer; mixing kinds in one column.
- **Needs.** N15, NK10, N4.

### Lesson 38. Graph Detectives

- **Big idea.** Scales save space, and a graph can answer some questions and not others.
- **Strand.** MOE P1 picture graphs (read and interpret, p. 32). Scales are P2 (p. 34), so Think harder and Go further go past P1. Critical reading.
- **Objective.** Read a 1-to-1 graph (most, fewest, how many more, in all); read a graph where each picture means 2; find a missing bar from a total. Go further: say what a graph cannot tell us.
- **Prerequisites.** Lesson 37 (draw a graph). Lesson 16 (count in 2s and 3s). Lesson 7 (a gap).
- **Remember (6 min).** (1) Read a 1-to-1 graph. (2) Count in 2s and 3s along a number line. (3) 4 pictures, each worth 2, are 8: draw the 2 beside each picture.
- **Start here (6).** Read a 1-to-1 graph: most, fewest, how many more, in all; True/False on a graph; a sentence frame with the total.
- **Think harder (4).** Each picture means 2: "How many ___?" for four kinds; the difference between two bars; "Mi counted 10 shells: how many pictures?" (5).
- **Go further (3).** **Beyond (named): "Missing Bar".** Each picture means 3. There are 21 books in all. Two bars show 6 and 3 books. How many pictures does the third bar need? (4, since 21 - 9 = 12, verified.) Also: which question can this graph not answer? (the colour of a pupil's shirt, not in the data). Level note: scales are P2; the Level 2 plan keeps keys of 2, 3 or 5 only.
- **Gaps closed.** MOE picture graphs; critical reading (plan).
- **Numbers.** Keys of 1, 2 and 3 only; totals within 30.
- **Home materials.** Coloured pencils only.
- **Kit.** None.
- **Figures.** `picture_graph` with hidden bars, keys of 1, 2 and 3, half pictures only at Go further.
- **Misconceptions.** Reading each picture as 1; the longest bar is the biggest number whatever the key; forgetting the key; the total taken from one bar; half a picture read as 1.
- **Needs.** N15.

### Lesson 39. The Problem-Solving Toolbox

- **Big idea.** Pick the tool that fits the problem.
- **Strand.** Mixed (processes and heuristics, pp. 13 to 14). Tools from Terms 1 to 3: draw it, list it, one step at a time, a strip, find one first, work backwards, make a table. The plan says the tools are recorded on a growing "Inquirer's toolbox" page; no built lesson has that page, so this lesson teaches all seven itself (D10).
- **Objective.** Match a problem to a tool, solve it with the tool, and say why. Think harder: the tool is not named. Go further: solve one problem two ways and check that they agree.
- **Prerequisites.** Lesson 10 (one step at a time), Lesson 12 and 18 (strips), Lesson 20 (find one first), Lesson 26 (list it), Lesson 28 (make a table), Lesson 29 (check with another method), Lesson 4 (draw it).
- **Remember (6 min).** (1) Draw two strips for "8 and 3". (2) 3 pens cost $12: how much is one? (Lesson 20, re-taught). (3) "I think of a number, add 5, get 12": work backwards (Lesson 10, holiday spiral).
- **Start here (6).** "Use a strip" and the story, solve; "Make a table" for a growing pattern; "Work backwards" for a number story; the tool is named every time. Within 100.
- **Think harder (4).** Choose the tool (multiple choice: Strip, Table, List, Work backwards); a problem with two good tools; explain with a sentence frame "I used ___ because ___".
- **Go further (3).** **Beyond (named): "Two Roads, One Answer".** Jo has 3 times as many stickers as Kit. Together they have 36. How many does Jo have? Solve it with a strip (27) and check it with a table of tries (Kit 9, Jo 27, verified); then say why both give the same answer. Level note: times as many with a total was Level 1 Go further in Lesson 18; here the new part is checking by a second method.
- **Gaps closed.** The plan's synthesis lesson; problem-solving heuristics (pp. 13 to 14).
- **Numbers.** Within 100; times table facts within 40.
- **Home materials.** The tool cards; pencil.
- **Kit (NK11, one page, 15 cards to cut).** 7 tool cards (one for each tool, with a small picture) and 8 problem cards. The Explore sorts the 8 problem cards under the 7 tool cards (two problems share a tool).
- **Figures.** `bar_model`, `table`, `number_line` (exist); tool icons (N4).
- **Misconceptions.** Choosing the tool by a keyword ("more" so add); using a tool for show and not for the answer; giving up after the first try; mixing "find one first" with ordinary times; not saying why.
- **Needs.** NK11, N4.

### Lesson 40. Inquirers' Showcase, and Mi's Challenge Quest

- **Big idea.** Teach what you found.
- **Strand.** Look back over the year; communicating (pp. 13 to 14). The Quest of the year.
- **Objective.** Choose a favourite idea or puzzle from the year and teach it to the group in about a minute (a pass is always allowed); write a puzzle with an answer. Go further: write a puzzle with a rule and a proof.
- **Prerequisites.** None: it is a look-back. A child who joins here does the Quest and the showcase on the ideas they know.
- **Remember (6 min).** Three "I remember" picks from the year, led by the tutor: a pattern, a way to add, a shape or a story (volunteers; no one is put on the spot).
- **Start here (5).** Show a favourite (page, picture or puzzle) and say one thing about it, using a sentence frame; sort four year-cards into "I know it well / I am learning it". Not marked.
- **Think harder (3).** Write a puzzle with an answer for a new Level 1 child; swap with a partner and solve.
- **Go further (3).** **Beyond (named): "Puzzle With a Proof".** Write a puzzle that has a rule, solve it, and show why the answer must be right (draw it, list every case, or check a second way). The author gives a check list: unique answer, checked twice, no copied puzzle.
- **Quest in this lesson.** Minutes 35 to 55 after the brain break; the showcase follows (about 20 minutes, volunteers only); the workbook is light and the exit ticket is not live. See section 6.
- **Numbers.** Within 100.
- **Home materials.** One favourite page from the year book; plain paper; the Quest Log in its envelope; a quest partner; pencil.
- **Kit.** None.
- **Figures.** None new; a puzzle-writing page with a drawing box and ruled lines.
- **Safeguarding.** Showing work is voluntary; no "best", no ranking, no votes; puzzles are shared inside the group only unless a grown-up agrees (D9).
- **Misconceptions.** A puzzle with two answers; the writer cannot solve it; copying a puzzle from the book; unclear wording; thinking a harder puzzle is better.
- **Needs.** T5 (Quest builder), puzzle page layout, parent report line.

---

## 2. Terms 3 and 4 at a glance

Waves are explained in section 11. "Existing tools" means the lesson could be written today with `figs2.py`, `svg.py` and the existing kits.

### Term 3

| # | Title | Wave | Blocking template items | Beyond (named) | Safest to skip? |
|---|---|---|---|---|---|
| 21 | What Time Is It? | B (pilot for clocks) | N1, NK1, R6, T4 | Mirror Clock | No, 22 and 23 build on it |
| 22 | Five Minutes at a Time | B | N1, N2, N4, NK12 | Chunk the Gap | No |
| 23 | Time Passes | B | N1, N2 | Find the Start | Fairly safe |
| 24 | Dollars and Change | C (pilot for money) | N5, NK2, R7, D1 | Fewest Notes and Coins | No, 25 and 26 build on it |
| 25 | Price Tags | C | N5, NK3 | The Hidden Price | No |
| 26 | The School Shop | C | N5, N4 | Exactly $20 | Fairly safe |
| 27 | Fill the Grid | A (existing tools plus N7) | N7, NK4 | Four by Four | Yes (plan note) |
| 28 | Make a Table | B | N8, NK13 | Picture 100 | Fairly safe |
| 29 | Spot the Mistake | A (existing tools) | NK5 | Does It Make Sense? | Fairly safe |
| 30 | Calendar Detective + Quest | D | N6, NK14, T5 | Hundred Days Later | No (holds the Quest) |

### Term 4

| # | Title | Wave | Blocking template items | Beyond (named) | Safest to skip? |
|---|---|---|---|---|---|
| 31 | Half and Quarter | E2 (pilot for shapes) | N9, N10, NK6 | Same Half, Different Shape | No |
| 32 | Build the Figure | E2 | N9, N10, NK7 | Every Triangle | Fairly safe |
| 33 | Copy on the Grid | E2 | N10, NK9, R8 | Count the Routes | Fairly safe |
| 34 | Cubes and Views | E4 | N11, N12, NK6 | Fold Twice, Punch Once | Fairly safe |
| 35 | Spot It | E4 | N13, NK8 | Shadow Match | Yes (plan note) |
| 36 | Count Everything | E3 | N14, N10, NK15 | Handshake Party | No |
| 37 | Make Your Own Graph | E3 | N15, NK10 | One Picture Is Two | No, 38 builds on it |
| 38 | Graph Detectives | E3 | N15 | Missing Bar | Fairly safe |
| 39 | The Problem-Solving Toolbox | E1 (existing tools) | NK11, N4 | Two Roads, One Answer | No |
| 40 | Inquirers' Showcase + Quest | E5 | T5 | Puzzle With a Proof | No (holds the Quest) |

## 3. New template capabilities Terms 3 and 4 need

Codes: **N** figure or icon, **NK** kit page, **R** online runner, **T** term-level tool. Hours are template-engineer estimates, not measured.

### 3.1 What already exists (checked in the working tree on 23 Oct; `figs2.py`, `svg.py`, `b_quest.py` have uncommitted edits by another agent, so the list reflects the working tree, not HEAD)

Figures: `bundles`, `scatter`, `ten_frame` (one- and two-colour, ring and dash), `ten_to_bundle`, `number_line` (marks, hide, jumps, highlight, width), `hundred` (shade, shade2, hide, mark, outline, arrows, zero), `seq`, `ruler`, `plates`, `objects` (32 icons: child1 to child6, apple, cookie, sweet, sticker, ball, marble, pencil, pen, book, cup, plate, bag, jar, flower, fish, bird, spider, ladybird, bike, car, counter, counter_red, counter_yellow, coin, dot, square), `groups`, `array`, `line_up`, `round_table`, `bar_model` (compare, part_whole, units, transfer), `table` (text, boxes, `()`, `[ ]`, icons), `picture_equation` (circle, square, triangle, star, heart, diamond), `domino`. Kits: `base_ten`, `ten_frame`, `plates`, `hundred`, `hundred_square`, `number_strip`, `cards` (text labels, optional round), `shapes` (circle, square, triangle, rect, star, heart; dashed cut lines, size 70), `number_line`, `groups_mat`, `unit_strips`, `array_mat`, `people`. Question forms: `visuals`, `tf`, `mcq`, `steps`, `draw`, `choices`, tokens `___`, `[]`, `[2]`, `()`, `[ ]`, `{eq}`. Runner v2: `fig`, `fields`, `ordered`, templated choice, `multiples`/`common`/`divisors`, `{n|ord}`, `{n|word}`. Quest builder: AUTHORING batch 3 says `b_check` (which `b_quest` reuses for question layout) takes any registered figure type in `visual`/`visuals`, so the L20 note "the page generator draws only a few figure types" should no longer hold; T5 confirms it with a clock gate.

Reusable without new work in Terms 3 and 4: `table` for Latin grids, ways tables and start/end tables; `bar_model` for money strips; `steps` for worked sums; `picture_equation` symbols for grid tiles; `objects` for event and item rows; `number_line` for counting up (needs only a label prefix, N2).

### 3.2 Figures and icons (new)

| Code | Item | Lessons | Spec in one line | Hours |
|---|---|---|---|---|
| N1 | `clock` | 21, 22, 23, 30, Quest | Analog face; `h`, `m`; hour hand placed at h + m/60 (the picture must not lie); long thin minute hand and short wide hour hand, different in length and width so they read in grey; 5s labels optional; `hide_hands`, `sector` shading, `mirror`; pairs through `visuals`; a `digital` readout ("4:35", a.m./p.m.). | 6 |
| N2 | Labelled number line | 22, 23, 24, 25, 30 | Extend `number_line` with a `labels` map (tick to text, for "3:00"), a `prefix` ("$") and arcs labelled "+30 min". | 3 |
| N4 | Icons batch 2 | 22, 23, 25, 26, 35, 36, 37, 39 | About 22 icons: sun, moon, bed, bus, house, school, shop, bath, bag, rubber, ruler, glue, shell, spoon, sock, shoe, button, and 7 tool icons (strip, table, list, draw, backwards arrow, find-one, steps). Navy outline, one fill, no glyphs. | 5 |
| N5 | `money`, `price_tag` | 24, 25, 26, 30, 39, Quest | Coins (rounded squares 5c, 10c, 20c, 50c, $1) and notes ($2, $5, $10, $50, rectangles) that differ in shape, size and label, not colour alone; "PLAY MONEY" mark; not facsimile (D1). `price_tag` is a tag with an item icon, a price and `hide_price`. | 7 |
| N6 | `calendar` | 30, Quest | Month grid with weekday headers, a start weekday, highlighted days, hidden cells and a week strip; no year, no real holidays. | 3 |
| N7 | `table` box lines | 27 | `box_lines` for thick 2 by 2 boxes; picture cells at large size. | 1.5 |
| N8 | `stick_pattern` | 28 | Triangles or squares in a row, n pictures, `hide_last`; sticks drawn as lines (never matchsticks in text). | 3 |
| N9 | `shapes2d` | 31, 32, 35 | Circle, half circle, quarter circle, square, rectangle, triangle with fold or split lines, shading, "equal part" marks, and composed figures (house, boat) from positions. | 8 |
| N10 | `grid` | 31, 32, 33, 36 | Dot grid or square grid, a polygon from vertices, a blank half to copy into, route arrows, start and end markers, counts written at corners, squares highlighted for counting. | 6 |
| N11 | `cube_stack` | 34, Quest | Isometric stack on a base up to 3 by 3, heights up to 3, with a numbered top view; a simpler front and top view mode. | 8 (3 if only views) |
| N12 | `fold_punch` | 34, Quest | A square with fold lines, the folded state, hole marks, and the unfolded answer in the key only. | 5 |
| N13 | `panel` | 35, Quest | A scene generator from shape primitives with number, colour, size and turn, giving spot-the-difference pairs, odd one out rows, a tile with a missing piece, and shadow options. | 8 |
| N14 | `network` | 36 | n dots on a ring with optional lines (handshakes). | 2 |
| N15 | `picture_graph` | 37, 38, Quest | Rows or columns of icons, a key "each picture = n", half pictures, tally marks, hidden cells; a title field. | 5 |
| | **Total** | | | **70.5** |

### 3.3 Kit pages (new)

| Code | Kit | Lessons | Hours |
|---|---|---|---|
| NK1 | `clock_kit`: 2 faces, 3 hour hands, 3 minute hands | 21, 22, 23, 30 | 3 |
| NK2 | `play_money`: 16 coins, 13 notes on 2 pages | 24, 25, 26, 30 | 5 |
| NK3 | `price_tags`: 12 tags (3 blank) | 25, 26 | 2 |
| NK4 | `grid_tiles`: 16 tiles (symbol and digit) and two mats | 27 | 2 |
| NK5 | `mistake_cards`: 8 cards and a two-pocket mat | 29 | 1 |
| NK6 | `fold_shapes`: circles, squares, grid rectangles at 9 to 10 cm | 31, 34 | 2 |
| NK7 | `shape_pieces`: 20 pieces on a 3 cm unit | 32 | 3 |
| NK8 | `pair_cards`: 12 cards in 3 sets | 35 | 2 |
| NK9 | `grid_mat`: 3 route grids and 2 copy grids | 33 | 1 |
| NK10 | `graph_mat`: 5 columns by 8 rows with a key box | 37 | 1 |
| NK11 | `tool_cards`: 7 tool cards and 8 problem cards | 39 | 1.5 |
| NK12 | `event_cards`: 8 cards and an a.m./p.m. mat | 22 | 1.5 |
| NK13 | `stick_strips`: 14 short strips | 28 | 1 |
| NK14 | `calendar_cards`: a month page and 7 day cards | 30 | 2 |
| NK15 | `people` (reprint, 8 people) | 36 | 0.5 |
| | **Total** | | **28** |

### 3.4 Runner and term-level tools (new)

| Code | Item | Lessons | Hours |
|---|---|---|---|
| R6 | Time answers: a fields frame "[h] : [mm]" with a leading-zero display, and words ("quarter past") as a choice | 21, 22, 23, 30 | 3 |
| R7 | Money formats: `$` before, `c` after, "$1" never "1 dollars", a no-mixed-amounts guard | 24, 25, 26 | 2 |
| R8 | Registered figures usable in `fig` with variables (`clock`, `grid`, `picture_graph`, `money`), 80-variant cap kept | 21 to 26, 33, 37, 38 | 3 |
| RW | Rewind sets: assemble items from earlier lessons by id into a mixed set (section 7) | all | 3 |
| T1 | `beyond` field: guide line, parent line, validator (named, not Start here, original) | all | 3 |
| T2 | Kit contract check: `materials.kit_pieces` lists each piece, supplied count, maximum used by a task, used-by ids; the verify script asserts supplied >= max used | all kit lessons | 4 |
| T3 | Hand-off checker: compares `parent.next_materials` of lesson n with `materials.child` and `workbook.kits` of lesson n+1 (kit names, cut words, keep words); one standard sentence for tearing a page from a book | all | 4 |
| T4 | Term 3 and 4 parameters (taglines, `t3l`/`t4l` keys, leak check keyed on `lesson_in_term`, "first lesson of Term 4") | all | 1 |
| T5 | Quest builder for Terms 3 and 4: figures in gates, a year version for Lesson 40, banned words kept | 30, 40 | 3 |
| T6 | `print/make_term_books.py` runs `--first 1 --last 40`; Books 5 to 8 spec and page counts | all | 1 |
| T7 | Home sheet rewind slot (section 7): `home_practice[].rewind_of` and answers | all | 4 |
| T8 | Terms 3 and 4 author brief (copy of `LESSON2_BRIEF.txt` plus this file) and a wording brief for time, money, shape and graph questions | all | 3 |
| T9 | Retrofit: L20 hand-off, `beyond` on L1 to L20, the "tear out" sentence in L1 to L20 hand-offs | 1 to 20 | 3 |
| | **Total (R and T)** | | **37** |

Totals: figures 70.5 + kits 28 + R and T 37 = **135.5 hours** if everything is built. Deferrable without blocking a lesson (about 23.5 hours): N11 isometric mode (-5, keep views), N13 shadow and turn options (-4), NK8 (-2), N6 extras (-1), N12 second fold (-1), NK15 (-0.5), R8 (-3), RW (-3), T7 (-4). That leaves about **112 hours**.

## 4. Kit contracts: supplied pieces against the most a task may use

The cut-out audit (F1, F2) found two Reworks because the kit never matched the tasks. Each row is the contract the lesson author signs: `supplied` is what the page prints; `max used` is the most any one task may use; the verify script asserts it (T2). "Cut" is the number of pieces a grown-up cuts. Nobody cuts in the lesson. Every kit page carries the standard note: one side only or its own sheet, a grown-up cuts, pieces in an envelope with the child's name, tear out along the dashed line (the back is blank).

| L | Kit | Supplied | Max used by a task | Cut | Reuse and notes |
|---|---|---|---|---|---|
| 21 | Clock | 2 faces, 3 + 3 hands | 2 faces, 2 + 2 hands (Lesson 23 pair; mirror pair) | 6 | Keep all term (21, 22, 23, 30). Loose hands, no fastener (D4) |
| 22 | Event cards | 8 cards, 1 mat | 8 | 8 | 4 a.m. and 4 p.m. events |
| 23 | none | reuse clock | 2 faces | 0 | Hand-off must say "keep your clock" |
| 24 | Play money | coins 5c x 4, 10c x 6, 20c x 4, 50c x 2; notes $2 x 5, $5 x 4, $10 x 3, $50 x 1; $1 x 12 from the Term 2 Lesson 10 tokens | 5c x 2, 10c x 5, 20c x 3, 50c x 2; $2 x 5, $5 x 4, $10 x 3, $50 x 1, $1 x 5 | 29 | Two pages. Keep all term (24, 25, 26, 30). Stylised (D1). If the $1 tokens are lost: 5 counters |
| 25 | Price tags | 12 (9 priced, 3 blank) | 4 at once; Explore 6 | 12 | Reuse money |
| 26 | none | reuse money and tags | $10 x 2, $5 x 4, $2 x 5, 6 tags; a way with more than five $2 is written | 0 | |
| 27 | Grid tiles | 16 tiles (4 symbols x 4, each with a digit), 2 mats | 9 (3 by 3) then 16 (4 by 4) | 16 | Mats not cut |
| 28 | Stick strips | 14 | 13 (4 squares) | 14 | Never matches or toothpicks |
| 29 | Mistake cards | 8 cards, 1 mat | 8 | 8 | 4 right, 4 wrong |
| 30 | Calendar | month page (31 days, starts Wednesday), 7 day cards | 7 | 7 | The month page is not cut |
| 31 | Fold shapes | 4 circles, 4 squares, 2 grid rectangles | 2 circles, 3 squares, 2 rectangles | 10 | Children fold only |
| 32 | Shape pieces | 6 squares, 3 rectangles, 6 triangles, 2 half circles, 2 quarter circles, 1 circle | house 6 pieces; Go further 3 rectangles or 6 squares | 20 | The author fills "used by" |
| 33 | Grid mat | 3 route grids, 2 copy grids, a counter from home | 1 counter | 0 | One side, no cutting |
| 34 | Fold squares | 4 squares (10 cm) | 3 | 4 | Marks in pencil, no punching |
| 35 | Pair cards | 12 (3 sets of 4) | 12 | 12 | |
| 36 | People | 8 | 6 (a group of 6: 15 handshakes) | 8 | Reprint, not a reuse |
| 37 | Graph mat | 1 mat | 1 | 0 | Pictures are drawn |
| 38 | none | | | 0 | |
| 39 | Tool and problem cards | 7 + 8 | 15 | 15 | |
| 40 | none | | | 0 | |

Cut per book: Book 5 (21 to 25) 55; Book 6 (26 to 30) 45; Book 7 (31 to 35) 46; Book 8 (36 to 40) 23. The Term 1 audit objected to 203 pieces in one term (F8, T8); Term 3 is about 100 and Term 4 about 69. Lesson 24 (29 pieces on two pages) and Lesson 32 (20) are the heavy ones: print on card if the owner agrees (D21), and keep the "alternative if there is no printer" line on every page (paper scraps, a paper plate for the clock, coins from a purse for play money, buttons for tiles).

Rules carried over from the cut-out audit: cut lines at least 6 mm apart (F10); counters and tiles are squares with rounded corners, not small discs; colour never carries the meaning alone (T5; tiles, coins and notes differ by shape and label); digits that can be turned (6, 9) are underlined if used; the kit is the last page and also printed as a one-sided `LNN_Kit_Pages.pdf`; the kit page says which later lessons reuse it; a "no printer" fallback is written for every kit (T10 in the audit).

Estimated page counts per book (workbook only, 5 pages per lesson plus kit pages, a Quest Log of 3 pages in Books 6 and 8, a cover and contents, and a blank pad so each lesson starts on a right-hand page): Book 5 about 36 pages, Book 6 about 38, Book 7 about 36, Book 8 about 36. These are estimates from the Term 2 pattern; `term_books_spec.json` gives the true counts after a build.

## 5. Hand-off materials chain

The rule from the Term 1 and cut-out audits: `parent.next_materials` of lesson n is true only if it lists everything lesson n+1 needs that a family has to prepare: the book (given on payment), any kit page to cut, anything kept from earlier, anything to find at home. Under the owner's decision (printed workbooks come with payment as 5-lesson books) the wording changes from "print the workbook" to "your next workbook is in your book; tear out the kit page along the dashed line, then a grown-up cuts out the pieces". Books: Book 5 = lessons 21 to 25, Book 6 = 26 to 30, Book 7 = 31 to 35, Book 8 = 36 to 40.

| From to | What the family must have ready | Keep from before | Check and hazard |
|---|---|---|---|
| **20 to 21** (term break) | Book 5; the Lesson 21 clock page: a grown-up cuts out the 6 hands; pencil; a real clock if there is one | The $1 tokens from Lesson 20 (needed in Lesson 24) | **The current L20 text is wrong.** It says "print it a week before" and "a toy or real clock, if you have one (optional)". It must say: your Term 3 book, cut out the 6 clock hands, keep the $1 tokens. Edit `l20.json` (`parent.next_materials`, `s-end`, the goodbye SAY line, `tutor_prep`) before Term 3 starts (T9) |
| 21 to 22 | Event cards page cut (8) | The clock | |
| 22 to 23 | Nothing new | The clock | "Keep your clock" |
| 23 to 24 | The money pages cut (29 pieces, two pages) and the $1 tokens | The clock (later needed again in Lesson 30) | The heaviest cutting of Term 3; give a week's notice |
| 24 to 25 | Price tags page cut (12) | The money | |
| 25 to 26 | Nothing new; Book 6 is in the house | Money and tags | If Book 6 arrives later (D11) this hand-off fails |
| 26 to 27 | Grid tiles cut (16); coloured pencil optional | | Fallback: nine small things of three kinds |
| 27 to 28 | Stick strips cut (14) | | No matches or toothpicks |
| 28 to 29 | Mistake cards cut (8) | | |
| 29 to 30 | The Quest Log (3 pages) closed in its envelope; a quest partner; calendar page; 7 day cards cut | Clock and money (optional aids) | Same rule as L19 to L20: the Quest Log is never opened before the lesson |
| **30 to 31** (term break) | Book 7; the Lesson 31 fold shapes cut (10 pieces); coloured pencil; the Term 4 start date from the tutor | | New term, new book |
| 31 to 32 | Shape pieces cut (20) | | |
| 32 to 33 | Nothing to cut; a button for the counter | | |
| 33 to 34 | 12 small blocks of one size; the 4 fold squares cut | | Fallback if no blocks (D14) |
| 34 to 35 | Pair cards cut (12) | | |
| 35 to 36 | Book 8; 8 paper people cut | | The book boundary falls here: if Book 8 comes with a later instalment it must be posted before Lesson 35 (D11) |
| 36 to 37 | 12 to 20 things from the house to sort (not food); coloured pencils | | |
| 37 to 38 | Nothing new | | |
| 38 to 39 | Tool and problem cards cut (15) | | |
| 39 to 40 | The Quest Log (3 pages) closed in its envelope; a quest partner; a favourite page from the year; plain paper | | |
| 40 to next | The tutor sends the Level 2 or next-term placement note; no materials list is printed here | | Not a lesson file concern |

## 6. Mi's Challenge Quest in lessons 30 and 40

The Term 2 Quest (Lesson 20) is the model: 20 minutes at minutes 35 to 55 straight after the brain break; 8 short gates and one optional secret cave; a quest partner; private paper; no score, no mark, no ranking, no visible timer, no "test" or "exam" on any child or parent page; the tutor keeps private notes for the parent line and next-term advice; Explore 10, Mini-lesson 9, Start here workbook 25, Talk 4, Look-back 2, Flex 4; the exit ticket is an optional item at home. Three files per Quest: `LNN_Quest_Log.pdf`, `LNN_Quest_Tutor_Notes.pdf`, `LNN_Quest_Parent_Note.pdf`, built by `b_quest.py` from a `challenge_quest` block. The Quest Log sits in the book (Book 6 for Lesson 30, Book 8 for Lesson 40), the tutor notes in the answer-key book, the grown-up note in the home pack.

**Gates for the Term 3 Quest (Lesson 30).** Every lesson of the term is visited by exactly one gate: gate 1 for lessons 21 and 22, gate 4 for lessons 25 and 26.

| Gate | Lesson | Item (all at Start here level; answers verified) | Figure |
|---|---|---|---|
| 1 | 21, 22 | A clock shows 4:35. Write the time. Then: breakfast at 7:00, circle a.m. or p.m. | `clock` |
| 2 | 23 | A film starts at 2:30 and lasts half an hour. It ends at 3:00. And 1 hour after 5:15 is 6:15. | `clock` pair |
| 3 | 24 | Count the coins: 50c, 20c, 20c, 5c is 95c. Pay $10 for a $7 toy: change $3. | `money` |
| 4 | 25, 26 | A pen costs $6 and a ruler costs $9: which costs more, and by how much ($3)? Two items that cost exactly $10: $4 and $6. | `price_tag` |
| 5 | 27 | A 3 by 3 grid with five cells filled: what goes in the shaded cell? | `table` |
| 6 | 28 | Triangles in a row use 3, 5, 7 sticks. Next: 9. Sticks for 5 triangles: 11. | `stick_pattern` |
| 7 | 29 | "49 + 38 = 77". Right or wrong (wrong)? The right answer is 87. | none |
| 8 | 30 | Today is Friday. Three days later is Monday. | `calendar` |
| Cave (optional) | beyond | An unseen puzzle that joins two moves, for example exactly $14 with $2 and $5 notes (2 ways: seven $2; two $2 and two $5, verified) | `money` |

**Gates for the Year Quest (Lesson 40).**

| Gate | Lesson | Item | Figure |
|---|---|---|---|
| 1 | 31, 32 | A circle is folded in half and in half again: how many equal parts (4)? What is each part called (a quarter)? | `shapes2d` |
| 2 | 33 | A counter moves 2 right and 1 up: which dot? A grid 2 across and 1 up has how many routes (3)? | `grid` |
| 3 | 34 | A stack picture: how many cubes in all? A paper is folded once and one hole is punched: how many holes (2)? | `cube_stack`, `fold_punch` |
| 4 | 35 | Circle the odd one out and say which feature differs (number, colour, size or turn). | `panel` |
| 5 | 36 | Four children shake hands once with each other: 6 handshakes. Squares in a 2 by 2 grid: 5. | `network`, `grid` |
| 6 | 37, 38 | Each picture means 2 and the bar has 5 pictures: how many (10)? How many more than the shorter bar? | `picture_graph` |
| 7 | 39 | Which tool fits this story? Circle Strip, Table or Work backwards. Solve it. | none |
| 8 | 40 | Solve a puzzle a friend wrote (a printed sample) and check it a second way. | none |
| Cave (optional) | beyond | An unseen mixed puzzle from the year (a time or money piece joined to a pattern) | one figure |

Quest rules for authors: wording from the Quest check (`BAN_FAMILY` in `b_quest.py`); the Quest is never shortened first in a slow class (the skip order in L20 says so); the cave is the only place for a puzzle the children have not met; one item per part; the Quest Log may now carry the Term 3 and 4 figures (T5), which Lesson 20's Quest Log did not; the Quest and the Look-back must not both run live in a slow class; the recording is paused for the Quest and the make-up child does the Quest before watching the recording (L20 `rec_pause_say`). Lessons 30 and 40 each lose 20 minutes, so Explore and Mini-lesson are shortened and the Start here workbook becomes 25 minutes with pages 3 to 5 for home.

## 7. Spiral review across the year

The Term 1 term-wide audit (F4) found no spiral review: warm-ups re-taught only what the lesson needed, home and online practice were current-lesson only, so a Lesson 2 idea was next tested six weeks later. Terms 3 and 4 are the first chance to fix this, and the owner asked for review across the year. Three layers, none of which adds minutes to the 90:

1. **Home sheet slot 5 is "Mi's rewind" (T7).** One item from lesson n - 20, with its answer on the separate answer sheet, so every Term 1 and Term 2 lesson is revisited once in Terms 3 and 4. Items are copied from the earlier lesson's home or online bank by id (RW), not rewritten.
2. **Online practice ends with two rewind items from lesson n - 10** (a second visit to Term 2 in Term 3, and to Term 3 in Term 4).
3. **The Quest cave and the Remember warm-up.** The cave is an unseen puzzle that joins two moves; one Remember item per lesson may be a spiral item when the prerequisite allows (marked below).

| Lesson | Home rewind (n - 20) | Online rewind (n - 10) | Lesson | Home rewind (n - 20) | Online rewind (n - 10) |
|---|---|---|---|---|---|
| 21 | 1 tens and ones | 11 ordinals | 31 | 11 ordinals | 21 clock |
| 22 | 2 number line | 12 strips | 32 | 12 strips | 22 5-minute clock |
| 23 | 3 digit cards | 13 doubles | 33 | 13 doubles | 23 time later |
| 24 | 4 hundred square | 14 odd or even | 34 | 14 odd or even | 24 coins and notes |
| 25 | 5 make a ten | 15 equal groups | 35 | 15 equal groups | 25 compare prices |
| 26 | 6 tens jump | 16 tables | 36 | 16 tables | 26 the shop |
| 27 | 7 count up | 17 sharing | 37 | 17 sharing | 27 grid |
| 28 | 8 balance | 18 times stories | 38 | 18 times stories | 28 table |
| 29 | 9 compare two lengths (drawn, no ruler needed) | 19 picture equations | 39 | 19 picture equations | 29 spot the mistake |
| 30 | 10 story steps | 20 find one first | 40 | 20 find one first | 30 calendar |

**Spiral threads (plan, section 1), now with the lessons that carry them.**

| Thread | Term 1 | Term 2 | Term 3 | Term 4 |
|---|---|---|---|---|
| Rules and patterns | 4 (100 square, growing gaps) | 16 (tables) | 28 (a table finds the 20th) | 33, 36 (grid paths, counting) |
| Balance and "=" | 8 (balance and swap) | 19 (picture equations) | 29 (check with another method) | 39 (the toolbox) |
| Listing every case | 3 (digit cards) | 17 (all ways to share) | 26 (exactly $20) | 36 (count everything) |
| Strips and finding one | 10 (read it twice) | 12, 18, 20 (strips; find one first) | 25 (the hidden price) | 39 (two roads, one answer) |
| Reading a scale | 2, 9 (line, ruler) | 16 (jumps) | 21, 22 (clock) | 38 (graph key) |

**Remember warm-ups that spiral (three items each; the first two serve the lesson, the third may be a spiral).** 21: 5s count (Term 1 Lesson 4). 22: bonds to 60 (Lesson 5). 23: tens jump and ones hop (Lesson 6). 24: count up (Lesson 7). 25: strips (Lesson 12). 26: repeated addition (Lesson 15). 27: a missing one in a row (Lesson 11). 28: doubles (Lesson 13). 29: adding back (Lesson 7). 30: ordinals (Lesson 11). 31: share between two (Lesson 8, 17). 32: arrays (Lesson 15). 33: rows and columns (Lesson 15). 34: doubling (Lesson 13). 35: pairs (Lesson 14). 36: make tens (Lesson 5). 37: count in 2s (Lesson 16). 38: count in 3s (Lesson 16). 39: one step at a time (Lesson 10). 40: tutor-led picks.

## 8. Known failure patterns from Terms 1 and 2: author checklist

Read from `TERM_WIDE_AUDIT`, `CUTOUT_AUDIT` and `FIXES_L11` to `FIXES_L20`. Each line is something the Term 2 fix passes repaired more than once, so the Term 3 and 4 authors should not write it in the first place.

1. **Kit counts do not match tasks** (L12 strips, L19 shape cards, L20 tokens, L13 counters). Fixed by the kit contract (section 4, T2).
2. **Hand-offs are false** ("pencil and paper only", missing kit, "Lesson 3" meaning two things). Section 5 and T3.
3. **Workbook questions repeat class numbers** (WB1 in L15 to L20). Rule: no Start here or Think harder number is used in Explore, Mini-lesson, the sneak-peek or the Quest; the verify script asserts it.
4. **Answers printed on the slide while the question is asked** (G1 in every Term 2 deck audit). Use `reveal` blocks and answer slides; read the question before the answer appears; `Explore` pictures never carry the count.
5. **Family pages use the global number** ("Lesson 14", "Lesson 1 of 10"). Use "Term 3 Lesson 4"; the leak check rejects "Lesson 1" outside `lesson_in_term` 1; the next lesson of L30 is "the first lesson of Term 4".
6. **Start here is too long for 28 workbook minutes** (L10, L15 to L20: 15.5 to 19 minutes). Five or six Start here items, page 1 about 8 minutes, page 2 about 9, choice 3 minutes; say on the page that Think harder and Go further are for home.
7. **Keys that accept only one order** (3 x 4 / 4 x 3). In Terms 3 and 4: "ten past four" or 4:10; the ways in L26 in any order; the route lists in L33.
8. **Recording and camera script**: greet by name first, then start recording, then notice; "so I can see you"; no papers held to the camera; ticks, not stars or colours; the mic routine ("mic off, say it on three, unmute to share") the same in every lesson; the make-up child's route.
9. **"I am still stuck" route**: the look-back page the grown-up photographs to the business WhatsApp; no number on slides or in recordings.
10. **Parent page**: a "do not teach" line ("do not teach 'clockwise' as a rule", "do not chant the days"), a words list that explains each new term, a "when stuck" line, the beyond-P1 statement, and the term line.
11. **Runner variants**: "1 hours", "1 stickers", "1 cousins", double full stop, raw placeholders in frames. Guard variable ranges (hours 2 to 12, counts 2 or more), add a plural guard, and verify all variants three ways.
12. **Investigation page overflow**: a drawing box, 4 lines, an easy first step; tables did not fit page 5 in four lessons.
13. **Small pictures on the workbook**: thumbnails of tables, number lines and strips were too small. Give `size` and column width for N1, N9, N10, N15 in the first build.
14. **Wrong working attached to cast names.** "A child" or "a child in another class" (D18).
15. **Children cutting** with scissors in the lesson: a grown-up cuts beforehand; "nobody cuts during the lesson" in materials, notes and safeguarding.
16. **Contest label on a child page**; `contest_where` names the tiers; the word "Challenge" appears only in "Mi's Challenge Quest".
17. **Colour or glyph reliance**: red and yellow counters; stars as marks; symbols that read the same in grey.
18. **Slow-class overrun**: no part OVER in the slow-class model; in Lessons 30 and 40 the Quest is never the part that shrinks.
19. **Mi's calculator image** (owner artwork, flagged by every audit; the builders switch to `mi_dolphin_nocalc.png` when supplied).

## 9. Risks

1. **Tier honesty.** Likeliest repeats from Terms 1 and 2: a quarter-to time or an hour that changes (L23 half an hour after 3:30) at Start here; a two-step money change in Lesson 25 Start here; a written reason in Lesson 29 Start here; a "how many routes" item in Lesson 33 Start here. Keep Start here to P1 content; every beyond puzzle is Think harder or Go further.
2. **Mid-year joiners.** A June holiday graduate enters at Lesson 21 with the holiday course only (owner decision 4): no 2-digit sums, strips or times tables. Lessons 25, 26, 28 and 29 use all three. Rules: Start here money within $20 with tens bars and a number line; the Remember re-teaches counting up and strips; "safe to miss" notes are honest (the clock chain 21 to 23, the money chain 24 to 26, the graph pair 37 and 38 are not); trial the Term 3 start with one cold joiner before launch (D23).
3. **No P1 paper behind the wording of time, money, shapes or graphs.** The only P1 paper studied is a multiplication quiz. School words for "half past", "quarter to", "How much change?", "half circle", "key" are guesses until the owner supplies P1 papers on those topics (D22). Run the wording review against `school_paper_wording_patterns.md` as usual, but mark every time, money, shape and graph item "wording unverified" until then.
4. **Money**: legal reproduction question (D1); Singapore has no $20 note (D3); no decimals, no mixed amounts (D2); play money must not be mistaken for real money; $1 tokens from Lesson 20 may be lost over the term break.
5. **Clock figure honesty.** The hour hand must sit at h + m/60. A clock that draws the hour hand on the number at 4:35 teaches the wrong reading. The validator should render N1 for 12 sample times and assert the angle.
6. **Cutting load** (section 4): 29 pieces in Lesson 24, 20 in Lesson 32, 16 in Lesson 27; the audit's complaint was 203 pieces in one term. Mitigation: card stock, fewer pieces, an envelope per lesson, "a grown-up cuts a week before".
7. **Blocks at home (L34).** 12 same-size blocks may not exist in every house; the fallback is drawn stacks and a counted top view. If the owner prefers, make cubes the Explore only and keep Start here drawn (D14).
8. **Cube and fold figures are the costliest engineering** (N11 isometric 8 h, N12 5 h, N13 8 h) for lessons the plan itself calls thin evidence (SASMO visual perception is partly a practice effect). Keep Lessons 34 and 35 late in the build and cut N11 to views if time is short (D13, D15).
9. **Beyond puzzles may overload.** Twenty named beyond items in addition to Think harder and Go further; the audit rule "3 to 5 Think harder, exactly 3 Go further" stands, so the beyond item takes one of those slots, not an extra one. Nothing beyond appears in the exit ticket or the home sheet slots 1 to 4.
10. **Level 2 overlap.** Mirror clocks (Level 2 T4.9), weekday cycles (T4.5), find the start (T2.5 Go further), picture-graph scales (T2.1) and halves (T1.6) all return in Level 2. The Level 1 versions are the simpler first visit (o'clock and half past mirrors only; days only; scale 2 and 3 only). Accepted spiral (D19).
11. **Cold-joining the Quest.** A child who joins at Lesson 30 or 40 has not met earlier gates; every gate is Start here level for its own lesson and "pass" is always allowed (Lesson 20 wording).
12. **Terms 3 and 4 vocabulary the child must read**: "quarter to", "a.m.", "change", "cheaper", "equal parts", "key", "handshake". The tutor reads every question aloud; words are defined in the parent page word list.
13. **The plan's asked-for-but-missing page**: the Inquirer's toolbox (D10).
14. **Safeguarding in Lesson 40**: children present on camera; voluntary, pass allowed, no ranking, no votes, no "best", nothing shared outside the group without a grown-up's agreement (D9); presentations are recorded under the existing recording statement.
15. **Print and post.** Four books of about 36 pages; Books 6 and 8 contain a Quest Log (kept closed). Posting both books of a term with the first payment avoids a missing book in mid-term (D11); the cost is the print and post of a book a family may not complete.
16. **Authoring documents are Term 2 specific.** `AUTHORING.md` has a "Term 2 (lessons 11 to 20)" section and `LESSON2_BRIEF.txt`; a Terms 3 and 4 brief must exist before agents start (T8).
17. **Parallel agents on shared files.** Same rule as Term 2: only the template owner edits `svg.py`, `figs2.py`, `validate.py`, `b_*.py`; lesson agents write only `lNN.json`, `verify/lNN_checks.py`, `AUDIT_LNN.md` and `out/lNN/`. New figures go into a new file `figs3.py` (appended to `figs2.render`), so lesson and engineering work do not collide.

## 10. Decisions the owner must make (defaults I chose are marked [Default])

None is irreversible. Changing a default after the build costs time, as noted.

- **D1. Play money pictures.** [Default] Stylised play money (rounded squares for coins, plain rectangles for notes, "PLAY MONEY" printed, not facsimile of any real note or coin). Ask whether the owner wants real designs; I have not checked Singapore's rules on reproducing notes and coins, so someone must check them before any realistic image is printed.
- **D2. Cents.** [Default] Write 50c or 50 cents; dollars and cents are never mixed in one amount; no $1.50. (Decimal notation is P2.)
- **D3. Denominations.** [Default] Coins 5c, 10c, 20c, 50c, $1; notes $2, $5, $10, $50 (and $100 only if a question needs it); no $20 note; "fewest notes and coins" for $73 (5 pieces).
- **D4. Clock hands.** [Default] Loose cut-out hands, no pin or fastener; a real clock is encouraged. Alternative: ask families to fix hands with a paper fastener (sharp point).
- **D5. Time words.** [Default] Say and write both forms: 4:10 and "ten past four"; "quarter past", "half past", "quarter to" at Start here and Think harder; "twenty to" and "ten to" only from Lesson 22. No "o'clock" for non-hour times.
- **D6. Lesson 30 is a calendar lesson, but days of the week are not a listed MOE P1 outcome.** [Default] Keep it as the plan's added lesson, flagged for tutor review.
- **D7. Beyond field.** [Default] Add the tutor-only `beyond` field to every lesson (20 now; Terms 1 and 2 retrofitted with metadata only, using the existing `contest_moves`). Not recorded in `owner_decisions.md` yet: please confirm so it can be recorded.
- **D8. Quest gates.** [Default] The mapping in section 6, eight gates and a cave; the cave holds an unseen beyond puzzle; the Quest Log may carry figures.
- **D9. Lesson 40 puzzles.** [Default] Shared inside the group only; no compiled book; a grown-up must agree before any child's puzzle leaves the group.
- **D10. Toolbox page.** [Default] No retro page in Terms 1 and 2; Lesson 39 teaches the seven tools itself with 7 cards. Alternative: a one-page toolbox in each Term 2 and Term 3 workbook (T9).
- **D11. Books and payments.** [Default] Both 5-lesson books of a term are given with the first payment (including the first instalment); a mid-term joiner receives the full book and the books for the lessons still to come; hand-off lines say "your book".
- **D12. When to build.** [Default] Build Term 3 now; start Term 4 template work in parallel, but write Term 4 lessons only after the first tutor trial of Term 1 reports timing (the audit's main uncertainty), then run one fix sweep across all 40.
- **D13. Thin-evidence lessons 27 and 35.** [Default] Keep as planned; each is marked "safest to skip" and may be swapped by a tutor.
- **D14. Blocks for Lesson 34.** [Default] List "12 small blocks" as home materials with a drawn fallback; Start here items work from pictures.
- **D15. Cube drawing.** [Default] Isometric stacks limited to 3 by 3, heights up to 3. Alternative: front and top views only (saves about 5 hours, loses the hidden-cube item).
- **D16. Fractions.** [Default] Words only; no 1/2 or 1/4 anywhere in Level 1.
- **D17. Lesson 37 data.** [Default] Made-up or household data; no live class poll and no counts by child.
- **D18. Names for wrong working.** [Default] "A child" or "a child in another class"; error-spotter role never given to a cast name.
- **D19. Level 2 overlap** (mirror clocks, weekday cycles, find the start, graph scales). [Default] Accept as a spiral; Level 1 keeps the simpler form.
- **D20. Calendar page.** [Default] A generic 31-day month starting on a Wednesday, no year, no public holidays.
- **D21. Paper and print.** [Default] Print kit pages on the same paper; recommend thicker paper in the kit note. Alternative: print the Lesson 24 money and Lesson 32 pieces on 120 gsm card.
- **D22. P1 papers.** Please supply (or point to) one Primary 1 paper or quiz on each of time, money, 2D shapes and picture graphs. [Default] Write with the P2 paper's patterns and mark the items "wording unverified".
- **D23. Cold-join trial.** [Default] Test Lesson 21 and Lesson 25 with one child who has done only the holiday course, before Term 3 launch.
- **D24. Quest slot in Lessons 30 and 40.** [Default] Minutes 35 to 55 after the brain break, as in Lesson 20 (the owner left placement to the assistant: after the break unless told otherwise).

## 11. Build order, effort and cost estimate

### 11.1 Dependencies in the content

- Clock chain 21, 22, 23 (one figure, one kit); money chain 24, 25, 26 (one figure, one kit); graph pair 37, 38; shapes 31, 32, 33 (N9, N10); counting 33, 36 (N10); Lesson 30 needs the answers of 21 to 29 fixed before its Quest; Lesson 40 needs 31 to 39 fixed.
- Lesson 39 uses words from 12, 18, 20, 26, 28, 29; its wording must match those lessons' fixed wording ("find one first", "strip", "table").
- Lesson 8 (balance) and Lesson 29 share "check by another method"; Lesson 29 and Lesson 39 share the "two roads" language.
- The plan says a lesson must not assume the previous one except through Remember, so the chains are a build-order and wording-consistency dependency, not a content one.

### 11.2 Waves

**Sprint A (day 0, one engineer, about half a day):** T4 term parameters, T1 `beyond`, T2 kit contract, N2 labelled number line, N4 icons batch 1 (sun, moon, bus, bed, items), N1 clock, NK1, R6; then write **Lesson 21** (pilot for Term 3 conventions). Other engineers start N5, NK2 and N7 immediately.
**Wave A (existing tools, can start on day 0):** Lesson 27 (needs only N7), Lesson 29 (needs NK5), Lesson 39 (existing figures plus NK11).
**Wave B:** Lessons 22, 23 (after 21's first build), Lesson 28 (N8, NK13).
**Wave C:** Lesson 24 (money pilot, after D1 is decided), then 25 and 26 in parallel.
**Wave D:** Lesson 30 and its Quest (T5, N6, NK14) after 21 to 29 have passed their fix pass.
**Audit and fix for Term 3**, then the Term 3 term-wide audit (guide and deck, home and parent, runner), as for Terms 1 and 2.
**Sprint C (Term 4 template):** N9, N10, NK6, NK7, NK9, R8 first (shapes and grid), then N14, N15, NK10, then N13, N12, N11, NK8.
**Wave E1:** Lesson 39 (if not done), E2: Lesson 31 (pilot for shapes), then 32 and 33; E3: Lessons 36, 37 then 38; E4: Lessons 34 and 35 (heaviest figures); E5: Lesson 40 and its Quest.
**Audit and fix for Term 4**, term-wide audit, then one 40-lesson consistency sweep (rewind items, hand-offs, beyond table, books).

Which can be written first with the existing tools: Lesson 29, Lesson 39, Lesson 27 (with N7), Lesson 40 (no figures). Lessons 21 to 26 and 30 cannot start without N1, N2, N5 or N6. Lessons 31 to 38 cannot start without N9, N10, N14 or N15.

### 11.3 Effort (agent-hours, not measured)

Per-lesson figures include write (data, checks, build, view every page), wording review, independent audit, fix pass. Term 2 evidence for scale: 76 estimated for ten lessons plus 8 for term-wide work, and about 6.5 hours of wall clock from pre-flight (17:06) to the end of the first fix pass (23:29), with template foundations done first (19:15) and three template batches in between.

| Lesson | Write and build | Wording | Audit | Fix | Total | Why |
|---|---|---|---|---|---|---|
| 21 | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 | First clock, pilot of Term 3 |
| 22 | 4.0 | 0.7 | 1.0 | 1.3 | 7.0 | Time line, am/pm |
| 23 | 3.5 | 0.5 | 1.0 | 1.0 | 6.0 | Reuses 21 and 22 |
| 24 | 5.0 | 0.7 | 1.2 | 1.6 | 8.5 | Money pictures, cutting load, D1 |
| 25 | 4.0 | 0.7 | 1.0 | 1.3 | 7.0 | Compare and sum-and-difference |
| 26 | 4.0 | 0.7 | 1.0 | 1.3 | 7.0 | Listing ways, verify scripts |
| 27 | 3.5 | 0.5 | 1.0 | 1.0 | 6.0 | Existing figures, unique-solution check |
| 28 | 4.0 | 0.5 | 1.0 | 1.5 | 7.0 | Stick figure, off-by-one risks |
| 29 | 3.5 | 0.7 | 1.0 | 1.3 | 6.5 | Reasoning wording is the main risk |
| 30 | 5.0 + 4.0 Quest | 0.7 | 1.5 | 1.8 | 13.0 | Quest, calendar, shortened lesson body |
| **Term 3** | | | | | **75.5** | |
| 31 | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 | Pilot for shapes |
| 32 | 5.0 | 0.7 | 1.0 | 1.3 | 8.0 | 20-piece kit, counting figures |
| 33 | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 | Grid and routes |
| 34 | 5.5 | 0.7 | 1.2 | 1.6 | 9.0 | Cubes and folds |
| 35 | 5.0 | 0.7 | 1.2 | 1.6 | 8.5 | Panel generator |
| 36 | 4.0 | 0.5 | 1.0 | 1.5 | 7.0 | Counting, copy checks |
| 37 | 4.0 | 0.7 | 1.0 | 1.3 | 7.0 | Picture graph |
| 38 | 3.5 | 0.5 | 1.0 | 1.0 | 6.0 | Reuses 37 |
| 39 | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 | Mixed problems, new wording |
| 40 | 4.5 + 4.0 Quest | 0.7 | 1.5 | 1.8 | 12.5 | Year Quest, showcase |
| **Term 4** | | | | | **80.5** | |
| **Both terms** | | | | | **156** | plus about 16 for two term-wide second-round audits: **about 172** |

Template engineering (section 3): figures 70.5, kits 28, runner and term tools 37, **135.5 hours** if everything is built, **about 112** with the deferrals listed there. Not in these numbers: the owner's P1 paper search (D22), the legal check (D1), a tutor trial per term, and the cold-joiner trial; allow another 15 to 20 hours of owner and tutor time.

**Cost to the owner in practical terms.** About 172 plus 112 to 135 agent-hours, about 285 to 310 in all. At the Term 2 pace (eight to ten writing agents and three engineers working in parallel) that is about 4 to 5 working days from the start of Sprint A to a fully audited Term 3 and Term 4, of which about 1 day is template engineering before the first lesson can be built (Term 2: 2 hours of foundations were enough for the pilot lesson, but Term 3 needs clock and money first). If template work is done serially before any lesson starts, add about 1 more day. Printing is unchanged in kind from Terms 1 and 2: four more 5-lesson books (about 36 pages each, estimate), two Quest Logs, and 100 to 170 more pieces for a grown-up to cut per term.

## 12. What was not checked

- No lesson, tool or output file was run, built or validated; the figure inventory was read from the working tree, which holds uncommitted edits to `figs2.py`, `svg.py`, `b_*.py` and `validate.py` made by another agent.
- Hours are estimates from the Term 2 documents and commit times, not measurements.
- MOE placements come from `docs/moe/syllabus_by_level.md` (P1 pp. 31 to 32). I did not find "days of the week" or "calendar" among the P1 outcomes; I have flagged this rather than concluded it, because the summary may omit sub-items.
- I did not check Singapore's rules on reproducing banknotes and coins, nor any real Primary 1 paper on time, money, shapes or graphs.
- The brief's statement that "every lesson should contain something beyond the school syllabus for challenge" is implemented here as the named beyond item (section 1.0); it was not found in `owner_decisions.md` at the time of writing.
- The Level 2 plan was read only to check overlaps.
