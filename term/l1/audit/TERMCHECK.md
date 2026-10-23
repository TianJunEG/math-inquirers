# TERMCHECK: originality audit of the 40 Level 1 term lessons

Scope: term/l1/lessons/l01.json to l40.json (workbook items, home sheets, online practice, exit tickets, Quest gates, slides and script examples) against the private sources on this machine. Audit only: no lesson, tool or book was edited. No private source text appears in this file; sources are cited by opaque entry code (for example "P1-BACK-09" is the entry with that code in the P1 non-routine list) and described in generic terms.

## 1. Method

Sources read (all gitignored): docs/books/private_p1_papers to private_p6_papers (non-routine question lists, records, papers, notes, helper scripts), docs/books/private_word_problems_notes.md, docs/sasmo/private_solution_notes_k and g1 to g6 (these hold answers and method lines only, no question stems), 44 files in all. The extension/hp texts were used for context only.

1. **Run overlap.** Every string of 5 words or more in each lesson (22,279 strings: all item texts, parts, hints, solutions, slide blocks and notes, script lines, tutor and parent text) was lower-cased, stripped of punctuation and tested against every private file for (a) a shared 7-word run, (b) a shared 7-word run with digits masked ("same sentence, new numbers" skeleton), and (c) a shared 5-word run with at least 4 content words. The tokenising follows extension/verify/dup_check.py (copied logic, original file untouched).
2. **Similarity pass.** 4,780 question-like strings were compared with all 8,744 private questions by content-word overlap (names, stop words and numbers removed, light stemming), and every item with high overlap was read side by side. This catches reworded versions that the run test misses.
3. **Reading pass.** Every tier item (start, think, go, investigation), exit item, home item, online item, Quest gate, talk and sneak-peek question of all 40 lessons was read (1,541 item units; plus 1,262 slides scanned by method 1) and compared with the full P1 non-routine list (268 entries), the P2 list (556 entries) and, by keyword and similarity, the P3 to P6 lists and the SASMO notes. Non-routine types were read in every lesson (work backwards, guess and check, make equal, how many ways, true or false, logic, pattern, clue numbers); the unflagged sample per term was well over 10 items (listed in section 5).
4. **Verdicts per item:** original / generic stock phrase / **review** (RV: same scenario or same structure as a private entry, wording and numbers differ, a person should decide) / **too close** (TC: same scenario and same structure, only numbers or surface nouns changed) / identical.

Note on the helper scripts: 78 of the 97 strings that share a 7-word run are echoes of the worked examples in the project's own private helper scripts (verify_catalogue_examples.py in each private_pN folder), which hold the author's own catalogue examples ("CE" below). They were not treated as school text. Outside those scripts no 7-word run from a real source was found except 19 short stock fragments (see 2). If any of those catalogue examples were modelled on a school question, the CE items inherit that closeness; the 7-word and similarity passes found no such trace.

## 2. Counts

| Check | Result |
|---|---|
| Strings scanned for runs | 22,279 |
| Strings with a shared 7-word run | 97 (76 distinct lesson/item ids) |
| ... of which only in own catalogue-example scripts (CE) | 78 |
| ... of which in real source files | 19, all generic stock fragments (instruction wording, "how many ... altogether", number lists) except 1 (L23 script, see table) |
| Digit-masked 7-word skeleton hits | 152 strings, all stock skeletons ("# stickers, how many more...") |
| 5-word content hits | 61 strings, all stock or catalogue echoes |
| Item units read in full | 1,541 (556 tier, 509 online, 200 home, 120 exit, 36 Quest, 80 sneak-peek, 40 talk) |
| Judged **too close** (TC) | **18 items** in 6 lessons (L10, L21, L23, L24, L28, L36) |
| Judged **review** (RV) | **60 items** in 23 lessons |
| Identical to a private text | 0 |
| Stock "I think of a number, add n, get m" frame | about 25 items (L10, L20, L30, L39, L40), not rated individually: the frame is a stock form in the P1 and P2 lists (including one with the same small addend); the lessons use it as a warm-up. Recommend varying it (see section 4). |

Lesson verdicts: **rewrite 6** (L10, L21, L23, L24, L28, L36), **review 18** (L03, L04, L09, L11, L12, L13, L15, L18, L20, L22, L25, L26, L29, L30, L34, L38, L39, L40), **clear 16** (L01, L02, L05, L06, L07, L08, L14, L16, L17, L19, L27, L31, L32, L33, L35, L37).

Worst lessons: **L23** (6 TC, 5 RV: the whole find-the-start and duration bank follows the school patterns), **L21** (4 TC: mirror clock), **L36** (3 TC: clothing-pair counting), then L10, L24 (2 TC each) and L28 (1 TC in a workbook item plus 2 RV).

## 3. Table of every too-close (TC) and review (RV) item

Source codes: P1-xxx and P2-/P3- refer to the entry in that level's private list or records; SASMO-K/G2 to the private SASMO notes. "Generic" explanations are in my own words.

### 3.1 Too close (rewrite recommended)

| Lesson | Tier | Item id | Verdict | What the closeness is |
|---|---|---|---|---|
| L23 | exit | E3 (and the tutor read-out of E3 in script segment 8, the only real-source 7-word run) | TC | Same scenario (a TV or film programme), same structure (end time and a one-hour length given, find the start time), only the clock time changed. Matches the P2 time entry for a programme ending at a stated time and P1-BACK-23, P1-BACK-29. |
| L23 | think | T3 (both parts) | TC | Same structure as P1-BACK-23 and P1-BACK-29: an activity stops at a stated time after half an hour or one hour, find when it began; only the activity and times differ. |
| L23 | go | G1 | TC | Two-stage backwards trip (1 hour then half an hour, end time given, find both starts) with the same two durations and the same question pair as the P2 two-stage cooking-then-bath entry; only the activities differ. |
| L23 | home | H4 | TC | Same as G1 with new end time. |
| L23 | online | g1 | TC | Same as G1. |
| L23 | online | t3 | TC | Same as T3 (ended at a stated hour, lasted half an hour, find start). |
| L24 | think | T3 | TC | Same scenario and structure as P1-BACK-09 and P1-BACK-17: pays with a one-dollar coin, receives a stated number of cents back, find the price; only the item and the cents changed. |
| L24 | online | t1 | TC | Same structure as the P2 money entry (one-dollar coin, a price in cents, how many cents change); only the item and numbers changed. |
| L28 | start | S2 | TC | A ratio table "for every a of one thing there are b of another", ask for the first quantity given 10 of the second. Same wording form, same table task and same given number as P1-TAB-02, P1-TAB-03 and the P2 sweets-and-lollipops table entry; only the objects (beads) and the pair a:b changed. |
| L36 | think | T2 | TC | Pairing each top with each pair of shorts, count outfits: same scenario and structure as the P3 shirts-and-pants outfit entry (also the catalogue-style form); only the counts changed. |
| L36 | home | H2 | TC | Pairing shirts with caps; uses the same two counts (3 and 4) as the P3 outfit entry, only the second garment changed. |
| L36 | online | c5 | TC | Pairing hats with scarves, same structure. |
| L10 | think | T2 | TC | A line with a stated number of children in front of and behind the child, count the line (the child is the trap): same scenario and structure as P2 (queue with children in front and classmates behind, count the queue) and P1-DIAG-03 (queue position and people behind). Numbers differ and the P2 version adds a late joiner. |
| L10 | online | t2 | TC | Same as T2. |
| L21 | go | G1, G2 | TC | A wall clock seen in a mirror, find the real time. Same scenario, same structure and the same reasoning line ("a mirror swaps left and right") as the SASMO G2 2017 Q4 mirror-clock entry; only the times differ (o'clock and half past). |
| L21 | online | g1, t3 | TC | Same as G1 and G2. |

18 items in total.

### 3.2 Review (a person should decide; no mandatory change)

| Lesson | Item ids | Verdict | What the closeness is |
|---|---|---|---|
| L03 | G2 (part c), online g2; also the moe note | RV | How many different numbers can 3 (or 4) cards make: same task as P3 (all 3-digit numbers from 3 cards, answer 6) and P2 (cards, how many ways). The lesson itself flags it as beyond syllabus. A standard type; keep only if the card set and framing are distinctive. |
| L04 | G1, online g1 | RV | Each term is the sum of the previous two: the rule used in several SASMO items (K Q2, G2 2014 Q3, 2015 Q6). Different start numbers. |
| L09 | G1, online g1 | RV | A length cut into 3 pieces, two stated, find the third: structure of a P2 rope entry, with an extra "3 longer" step. |
| L10 | S5, online t3, online g3, Quest optional, slide s-m5 | RV | Compare-then-total (X has n, Y has k more, how many altogether) shares objects with P1-CMP-13 and a P2 marbles entry; queue-count variants (same family as T2). Generic Singapore comparison structure. |
| L11 | S4, S6, E3, H3 | RV | Ordinal clue forms ("second", "right behind", "between ... and ...") follow P1-LOG-27 and P1-LOG-51; very basic. |
| L12 | T2, online t2, H5 | RV | Give some so both have the same: P1 EQ entries and a P2 transfer entry; generic make-equal. |
| L13 | H4 (and the investigation) | RV | Two lines of shape sums, find one shape: the SASMO K Q5 type (weighted sums of two symbols); different values. |
| L15 | G1, online g1, H5 | RV | Wheels of vehicles times a count: scenario of P1-CTX-24 (three-wheeled vehicles) and a P2 legs-times-count entry. H5 (tricycles and bikes) is closest. |
| L18 | T4, online t4 | RV | "Twice as many, then gives some so they have the same": P3 catalogue-style transfer item; generic make-equal with a multiple. |
| L20 | T1, T2, G2 | RV | T1: saving a fixed amount each period to reach a target (P2 saving-per-day entries). T2, G2: undo a chain of double, add and take away (SASMO K Q8, G2 2017 Q15). Generic reverse chain. |
| L21 | G3, online g2, online g3 | RV | Rest of the mirror-clock family (same source as the TC items); will be removed with them. |
| L22 | G3, online g2 | RV | A duration across the hour with a start time that coincides with the P2 art-class entry; the type is a syllabus staple. Change the start time. |
| L23 | S3, T1, H3, online t1, online t2 | RV | Start time plus half hour or one hour, find the end, in a reading or painting setting; the same scenario family as the P2 story-book entry. Fine type, but see recommendation. |
| L25 | T4, H4, online t4 | RV | T4: spend exactly an amount on two (or three) of five tags (P1-GC entries for two items totalling an amount). H4, t4: pay with notes, receive change, find price (P1-BACK-10, P1-BACK-16, P3 two-note change entry). Generic. |
| L26 | S1, E1, G3 | RV | Which two tags make an exact amount (P1-GC-16, P1-GC-18 and P2 two-item entries). Generic, but the type recurs in L25, L26, L30. |
| L28 | H2, H4 | RV | H2: second ratio table (same type as S2). H4: squares in a row use 4, 7, 10 sticks: the sequence and scenario of the P2 stick-pattern entry (the numbers are forced by the shape). |
| L29 | S4, H2 | RV | Starts reading, reads for 1 hour, a child misreads the end: the time family of L23. |
| L30 | S3, H2, T4, C8 | RV | S3, H2: two tags make an exact amount. T4, C8: N coins of two values make a stated total, how many of each (P2 coins entries and the P3 coin-count entry); L39 and L40 repeat the type. |
| L34 | S2, online c5 | RV | A tower with a cube hidden behind a taller tower, count the hidden cubes: scenario of SASMO K Q1; the totals 4 and 5 coincide with that item's example and answer. |
| L36 | E2 | RV | Hat-and-scarf boxes: same family as the TC pairing items. |
| L38 | S1, S2 | RV | Picture graph of books read by four children, "who read the same number": P2 graph entry stem. A stock reading question; change the context. |
| L39 | T4, H4, online t3, H2 | RV | Coin-count total (see L30); H2: a table of sticks growing by a fixed number per picture (a P2 day-table entry with the same step of 4). |
| L40 | C4 | RV | Coin-count gate (see L30). |

60 items in total.

### 3.3 Own-catalogue echoes (CE): informational, not counted above

These items repeat worked examples that live in the project's private catalogue scripts, with the same or similar numbers. They are not school text, but the catalogue is private, so the lesson wording and the catalogue example should not drift apart unnoticed: L10/L11/L20/L39 position-in-a-line (front and back positions), L33 routes on a grid (T1, T2, H4, online t1, g1, g2, spare-time M2), L34 fold-and-punch holes (G1, online g1, slide s-opt, beyond note) and top view of cubes (S6, E2), L36 handshakes (T1, G1, online t1) and counting squares, L26 pay exactly with two note types (T2, H4, online t2, t3), L40 friend's puzzle with a wrong answer (G2, H2, online t2, C8), L39 and L18 "times as many then give" (G1, L18 T4), L39 T4 coin count, L04 T3 growing gaps, L39 slide s-opt on cuts and pieces. No action needed unless the owner finds the catalogue examples themselves were traced from a paper.

## 4. Recommended rewrites (new context and structure only)

- **L23 (rewrite most of the find-the-start bank).** Drop TV, film, swim, play and read as the setting and drop end times such as the top of the hour or half past with a one-hour or half-hour length in the same form. Replace the "ended at ..., lasted ..., find the start" items with: (a) a strip of two coloured blocks (one hour, half an hour) laid end to end under two clocks, where the child writes the missing clock; (b) "which clock is half an hour before this one" picture choices; (c) a school-day timetable where one row has a missing start and the child reads the neighbouring rows. Replace the two-stage bus-and-walk trip with a three-block plan fitted exactly into a window (already the investigation) and vary the clock times away from the round values used in the school lists. Keep the forward items (start plus length) but change the settings (oven, bus, library visit) and mix of clocks and times.
- **L24.** Replace "pay with a one-dollar coin, get cents back, find the price" with a coin-set puzzle: show a price tag and two coin sets, ask which set gives exactly the right change for a stated payment, or give the coins in a till and ask which payments are possible. For the online t1, use a different payment piece (a 50-cent coin or a two-dollar note) and a different question (how many coins of one kind make the change).
- **L28 S2 (and H2).** Replace the "for every a ... there are b ..." table with a growing picture in which the table has two columns that come from a visible rule, for example rows of beads or flags where each new row adds a fixed set of each colour, and ask for the total or the missing row; or use a price-per-item table. Avoid the "given the second quantity, find the first" form of the ratio entries.
- **L36.** Replace clothing pairs with a structure the lists do not use: flags with two stripes of different colours chosen from three colours (ordered pairs, no repeats), or two-scoop combinations from three flavours where the scoops differ; keep one conventional pairing item only if the numbers and objects are changed (not 3 and 4, not shirts, caps, tops or hats).
- **L10 T2 / online t2.** Replace the line of children with a train, a row of stairs, or a shelf of books where the child's own place must be counted: for example "a carriage is 4 from the engine and 3 from the end", or books on a shelf with a gap and a bookend. Keep the "count yourself too" lesson, drop the queue scenario.
- **L21.** Replace the mirror clock with a different reasoning about hands: for example a clock whose two hands were swapped by mistake (the short hand on the 6 and the long hand on the 12, what time was it meant to show), or a clock seen from the back of a see-through card where the child decides which times still read correctly. G3 and the online mirror items go with the rewrite.
- **Review band.** Prefer a small change over a rewrite: vary the object and the numbers; in L25, L26 and L30 keep one "two tags make an exact amount" item per lesson and change the others (three tags, or "which tag can she not buy"); in the coin-count family (L30, L39, L40) keep one lesson with 5-cent and 10-cent coins and move the others to a different guess-and-check object (legs, wheels or pages) so the form is not repeated; L22 G3 move the start away from the coinciding time; L38 S1 change the graph context from books read; L34 S2 and online c5 change the totals so they do not match the source example; L03 G2 part c keep only if wanted as the one beyond-syllabus item.
- **"Think of a number" frame (L10, L20, L30, L39, L40).** Leave one per lesson and vary the story frame (a box that gains counters, a coin purse) in the rest.

## 5. Unflagged non-routine sample checked against the non-routine lists

Read and compared with the P1, P2 and P3 lists (and the SASMO notes); no scenario overlap found beyond the table above.

- Term 1: L01 G3 (ways to write 30), L01 T3 (clue number), L02 G2 (two hoppers meet), L02 T3 (halfway clue), L03 T3 and T4, L04 G2 (mixed lists), L05 G1 and G3 (change one number, six numbers make 100), L06 G1 and G2 (jump routes, fewest jumps), L07 G3 (same difference), L08 G2 and G3 (equal-sum pairs, page and pocket), L09 G3 (path of different lengths), L10 G2 and G3 (write the story, three-person shells).
- Term 2: L11 G1 (round table seats), L11 G3 (race order), L12 G1 and G2 (two shelves, three children), L13 G1 to G3, L14 T1, T3, T4 and G2 (always, sometimes, never), L15 G3 (ways to group 24), L16 G1 and G3, L17 G1 and G3 (friends who can share, keep some), L18 G1 and G3, L19 G1 and G3 (two shops), L20 G3 and T4 (two counting lists).
- Term 3: L22 T4 (show times), L24 G1 and G2 (fewest notes, different amounts), L25 G1 and G2 (hidden price, three prices), L26 T1 and G2 (table of ways, seven things), L27 G1 to G3 (100 days later, Wednesdays), L28 G1 to G3 (100th picture, work back), L29 G1 and G2 (estimate, one wrong digit), L30 T3 (pets logic), G2, G3.
- Term 4: L31 G1 to G3 (same half, different shape), L32 G1 and G2 (fewest pieces), L33 G1 to G3 (corner counts, passing a corner), L34 G2 and G3, T3 (fold then hole), L35 G1 and G2 (shadow match, one thing at a time), L36 G2 and G3 (squares of every size, roads), L37 G2 (stickers), L38 G1 and G2 (key and total), L39 G2 and G3 (make equal, growing days), L40 T3, G1, G3 (unique answer, list of pairs).

## 6. Limits

Some private entries are picture items whose stems are only summarised; the SASMO notes hold no stems. Where a lesson item is picture-led the comparison used the written stem only. The similarity pass cannot see a pure picture overlap. Verdicts RV and TC are judgements; the owner's call on borderline items (L03 G2c, L28 H4, the stock frame) is expected.

Scratch scripts (not committed): /tmp/claude-0/-home-user-math-inquirers/6d6b173e-8eda-5fdf-9c4d-af677bceddc6/scratchpad/chk.py (run overlap) and sim.py (similarity pass).
