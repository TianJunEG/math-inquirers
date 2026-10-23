# Round-3 independent audit: Primary 2 early-finisher booklets, Semester 1 and Semester 2

Auditor: independent (not the builder). Date: 23 Oct 2026. Branch `claude/great-fermi-1hv4vc`, HEAD `8db135f`. Nothing was edited, pushed or PR'd; only this report was added.
Subject: `school/p2/out/P2_S1_*` and `P2_S2_*` (Puzzles 20 pp, FrontMatter 5 pp, Complete_Pack 25 pp, Answer_Key 11 / 9 pp). Compared with `docs/audit_final/p2_semester_booklets_audit_round2.md` and the "Audit round 2" section of `docs/school_books/p2_semester_booklets_build_report.md`.

Method. Changed pages were rendered from the PDFs (90 dpi colour; 150 dpi 1-bit; a 1 px "heavy toner" erosion on the coin page) and **solved by hand from the image before the key was read**. Clock hands on P2-29 were also measured from pixel positions. Code words were tested against about 113 000 words (wordfreq top 150 000 plus the builder's own list, 4 to 7 letters).

## Verdict

| Booklet | Verdict |
|---|---|
| Semester 1 | **Print-ready as to content, pending lawyer approval of the licence wording.** No new finding. |
| Semester 2 | **Print-ready as to content, pending lawyer approval of the licence wording.** All three new or changed pages solve and agree with the key; no second word; no Primary 3 duration outcome remains. |

No High, no Medium. Both stay DRAFT by the owner's rule (P2-LAWYER-WAIT: nothing is printed or sold until the lawyer approves the wording; coin and note art still to be compared with real money; no pupil trial or real photocopier test yet). The remaining items are Low (section 6).

## 1. Hand-solve of the changed pages (from the image, then compared with the key)

0 wrong, 0 unsolvable, 0 with two answers.

| Page | My answer from the image | Result |
|---|---|---|
| S2-12 P2-29 Match the Times | Clocks read, hour hand and minute hand measured from pixels: A 4:06 (hour 123 deg, minute 33 deg), W 7:16 (219 deg, 95 deg), O 10:34 (315 deg, 205 deg), S 9:32 (284 deg, 192 deg), H 10:26 (314 deg, 155 deg), D 6:12 (about 186 deg, 74 deg). Times in order 9:32 S, 10:26 H, 4:06 A, 6:12 D, 10:34 O, 7:16 W: **SHADOW**. The close pairs (10:26 / 10:34, same hour) differ by about 50 deg on the minute hand, clearly separable. | agree |
| S2-13 P2-31 Time Detective | Art 45 (B); Science 1 h 25 = 85 (A); Maths 35 + Reading 65 = 100 (N); Drawing 11:10, so 10 min past the hour (D); lessons starting before 10:00 = Art and Science = 2 (I); Music 1 h 25, so 25 over 1 h (T): **BANDIT**. The timetable is self-consistent (no overlaps). | agree |
| S2-20 P2-40 Colour the Butterfly (money) | Left top: 35c and 65c make $1 = 65 R; $0.65 = 65 R; $0.35 = 35 Y; greatest of $2.50 $0.65 $1.35 = 250 O. Right top: 5c + 60c = 65 R; smallest of $0.65 $1.35 $1.85 = 65 R; $2.50 = 250 O; 65c and 35c make $1 = 35 Y. Bottom left: 245 + 5 = 250 O; Ann 70 + 115 = 185 G; 110 + 25 = 135 B. Bottom right: 190 + 60 = 250 O; 45 + 140 = 185 G; greatest of $1.35 $0.35 $0.65 = 135 B. Tally Y2 R4 B2 G2 O4 equals the strip, and every left/right pair (6 pairs plus the two lower wings) is the same colour. | agree |
| S2-01 P2-06 (new coins) | $2.65, $1.85, $2.90, $6.15, $10.25, $2.45: S A I L O R | agree |
| S2-04 P2-24 (new coins) | purses S 2.10, P 1.15, C 1.40, U 2.20, A 3.00, M 1.70; so 1.40 C, 3.00 A, 1.70 M, 1.15 P, 2.20 U, 2.10 S: CAMPUS | agree |
| S2-11 P2-30 (time, unchanged, re-solved) | 210 T, 4 O, 180 N, 30 G, 85 U, 5 E: TONGUE | agree |
| S1-02 P2-38 Rocket (9 mm boxes) | 250 R x2, 120 Y x3, 340 B x4, 470 G x4, 560 O x2; wings both G, circles both B | agree, strip true |
| S1-17 P2-39 House (9 mm boxes) | B 35 x4, G 40 x3, R 28 x3, O 45 x3, Y 24 x4; marks: moon B,B; triangle B,B; star G,G; square R,R; dot O,O,O; plus Y,Y,Y | agree, strip true |

P2-33 (S2-15) changed only in the key text; page not re-solved this round (round 2 solved COBALT).

## 2. Code words

- **SHADOW (P2-29):** all 720 orderings of its six clock letters: no other word. All 6^6 letter strings made from the six clock letters were tested too (this includes using one clock for two times): the only real words are made with repeated letters (WHOOSH, SWOOSH, HOWDAH, DOODAD and similar), which need at least three wrong matches and a repeated clock; recorded as information only, the claim is single slips and rearrangements.
- **BANDIT (P2-31):** all 720 orderings of its letters: no other word. Single slip, any letter: BANDIE and PANDIT are the only hits and neither can be produced from the page (E and P are not on it). Single slip using only the letters in the page's code table (I G D X T B A N): **0 real words.**
- **P2-40 (colouring):** a colour-by-code page, so the check is the tally and the left/right symmetry, not a word. The five colour values (35, 65, 135, 185, 250) are all different from every other answer on the page, so no part can take a second colour by mistake except by a wrong sum. The tally (Y2 R4 B2 G2 O4) plus the symmetry rule reject a single wrong answer: any one wrong part lands on a colour that breaks the tally, and no two parts can swap and still keep the pairs equal unless both are wrong in the same way. Not exhaustively machine-tested by me; hand-checked for each part.
- All 32 code words are still distinct (SHADOW and BANDIT are new to the set; none repeats another page's word).

## 3. No Primary 3 outcome left (durations from start and finish times)

Searched the pupil PDFs, answer keys and front matter for start, finish, end, duration, how long, until, later, ago, elapsed, interval and any am/pm range. Findings: **none left.**
- P2-31: every question reads a given duration or start time (changing h and min to minutes, adding two given durations, minutes past the hour of a start time, counting start times before 10 am, minutes over 1 h). No question needs an end time or a duration to be found from two clock times. The key teacher note says so in plain words.
- P2-29: reading clocks to the minute and matching only.
- P2-07, P2-30: read a clock; convert h and min to minutes and back.
- P2-40: now money only (no time sheet). The old "1 h 30 min = ?" unit gap is gone.
- S1: no time content at all. S2-05 (P2-08 Metres) asks for lengths of bars that start at an arrow (length, not time).
- Wording only (Low, L-G): the S2 teacher note says P2-31 practises "durations"; that word is true (given durations) but could be read as the old outcome. Suggest "lengths of lessons given in hours and minutes".

## 4. Key against the pupil pages

Read the S2 key for P2-06, 24, 29, 31, 33, 40 and the P2-40 key picture, and compared with my solves: all answers, code words and colours match (P2-40 key picture: R R / Y O O Y / O O / G G / B B). The P2-33 key now reads "size and colour: C; shape and colour: O; shape and colour: B; shape and size: A; shape and colour: L; turn: T" and the note no longer mentions half circles. `school/p2/README.md` no longer says "Colour the Dinosaur". The word "dinosaur" is in no PDF. Pack text equals FrontMatter + Puzzles text for both booklets. Page counts 20 / 5 / 25 / 11 and 9. `validation_report.txt`: 747 checks, 0 failed.

## 5. Photocopy (1-bit) checks of the changed pages

- **Coins (S2-01, S2-04):** no inner ring on any coin. At 150 dpi 1-bit every numeral, symbol, "cents" and "dollar" and both notes read. With a 1 px heavy-toner erosion (simulated) the numerals, sun, boat, flower, star and leaf stay clear; the small word "cents" and "dollar" fill in on the 5, 10 and 20 cent coins but each coin is still identified by its numeral (L-H). The old problem (word touching a ring) is closed.
- **Clocks (P2-29):** 1-bit at 150 dpi: tick marks, numerals and the thick hour hand versus thin minute hand are all distinct.
- **P2-31:** table, boxes and code table clear.
- **P2-40, P2-38, P2-39:** boxes measure about 9 mm and hold three digits; the text, the five key boxes, the marks (house) and the check strip are clear and no label is cut. The small text "5c + 60c =" in the butterfly's top-right cell is the smallest on the page but reads at 1-bit.

## 6. Front matter against docs/terms/owner_decisions.md

Checked in both FrontMatter PDFs and both packs: annual licence ("This is an annual licence: it covers one school year and is renewable"); publisher line "Preciouslyours Pte Ltd, trading as Math Inquirers" on the cover; registered office 66 Tannery Ln, Singapore 347805 on the licence page; DRAFT banners on the cover, licence, teacher notes and key ("KEY page n of N"); (c) 2026 Preciouslyours Pte Ltd; contact pypteltd@gmail.com marked as temporary; licence wording marked "to be approved by a lawyer". **The "Not affiliated with or endorsed by the Ministry of Education, Singapore." sentence is on the cover (9 pt, below the publisher line, fully on the page, legible) and is gone from the licence page, as decided (P2-NOTAFFIL-FRONT).** The licence page keeps only "The mathematics syllabus is published by the Ministry of Education, Singapore.", a statement of fact, not an endorsement. No "MOE-aligned", SASMO, price or "aligned" wording in any pupil page, key or front matter (searched). No price.

## 7. Remaining items

All Low. None blocks printing once the lawyer and owner items are cleared.

- **L-F (owner, unchanged).** Lawyer approval of the licence wording (P2-LAWYER-WAIT); comparing coin and note art with real money; a pupil trial; a real photocopier test with a light and a heavy-ink machine (use S1-18, S2-01, S2-04).
- **L-G.** Reword "durations" in the S2 teacher note (section 3).
- **L-H.** Under heavy toner the small words "cents" and "dollar" can fill in. Numerals carry the meaning, so no answer changes. A line in the teacher notes ("use a normal toner setting for the coin pages") or 0.3 mm larger text would remove the risk.
- **L-I.** The S1 and S2 teacher notes say each code word has "one way only" of being spelt. That is true for rearrangements and single slips (tested) but not for three or more simultaneous errors (e.g. P2-29 with one clock used twice can spell WHOOSH). The notes already say two wrong answers at once were not all tested; the phrase "answers in the wrong boxes never make another word" could add "one or two".
- **L-J.** `git status` shows unrelated uncommitted changes under `extension/` and `outputs/extension/L4`; not part of P2 and not touched.

Items found fine and unchanged since round 2: the instructions on S1-05 and S1-13, the house and rocket colour keys, the fraction gaps on P2-15, and the money page layout.
