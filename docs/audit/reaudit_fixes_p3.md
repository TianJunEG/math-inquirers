# Level 3 (P3) re-audit fix pass: what changed

Scope: content and wording only, Level 3 sources (`p3/content/l1..l10.js`, `p3/guide.js`, `p3/workbook_html.js`, `p3/gifted.json`, `p3/SPEC.md`, `rebuild/gen_p3l*.py`, `rebuild/p3_gifted.py`). Not committed. Every changed numeric answer was recomputed in Python (see "Checks").

## 1. Tier failures (11 items)

| Item | Old | New |
|---|---|---|
| L1 Q6 (if time) digit sum 3 | blank 3-row table | Hint (3 counters in 4 places, thousands place needs 1); first row pre-filled (3000). Still "(if time)". Key unchanged (10 numbers) |
| L2 Q6 (if time) AB+AB+AB=CAB | "try 0 and 5 in the ones column" | guess-and-check entry: "Try AB = 40: 3 x 40 = 120, does not end in 40; try 10, 20, 30 ..." and "same letter, same digit: a code puzzle". Key unchanged (50, 150) |
| L3 Q4 (if time) grid puzzle | six unknown row/column numbers | first row number (7) given; hint "56 / 7 = ?, 81 = 9 x 9". Key unchanged (rows 7, 9, 6; columns 8, 6, 9). Slide preview text updated |
| L3 Q6 (if time) number riddle | hint: list the 8s yourself | the 2-digit numbers in the 8 times table are printed; child circles those also in the 6 table. Key unchanged (24, 48, 72, 96; 48) |
| L5 Q6 (if time) tables and children | table with first column | added hint "each table adds 6 and 7; look for the column where both rows match". Key unchanged (5 tables, 35) |
| L10 Q6 (if time) 3-digit odd riddle | none | hint lists the digit sets with no 0 summing to 6 (1,1,4 / 1,2,3 / 2,2,2). Key text fixed: it said "ones digit is 1, 3 or 5" (answers 411, 321, 213 are right, wording was wrong) |
| L6 Q4 six sums with unlike denominators | no link to the wall | fraction wall named in the question with a worked example (1/2 + 1/4 = 2/4 + 1/4 = 3/4) |
| Bank L2 T5 (digit sum 30) | smallest/greatest 4-digit number, digit sum 30 | Think harder item on the lesson's idea: zoo, 6000 visitors in 3 days, Monday 1874, Tuesday +650, Wednesday? Answer 1602 (check by adding) |
| Bank L3 X6 (sweets 40-60, 6 and 9) | one list-and-test step | fewer than 100 sweets, shared among 6, 9 AND 4 friends, find ALL, "what do you notice, why?". Answer 36 and 72 (36 apart) |
| Bank L5 X2 (chocolates 30-50) | same list-and-test as Think harder s7 | 30 to 100 chocolates, shared by 2, 3, 4, 6, and remainder 2 when shared by 5. Answer 72 (brute-forced) |
| Bank L7 X4 (square 20 cm) | three routine steps | find perimeter AND area of the big square and explain why the perimeter doubles but the area is 4 times. Answer 40 cm, 100 cm2 |

Honest limit: the seven Start-here "(if time)" items are now scaffolded (entry route, pre-filled starts, hints) and keep the "(if time)" label; they were not moved to Think harder. A strict reader may still see L1 Q6 and L3 Q6 as Think-harder demand with an entry route, not Core.

## 2. Online safeguards
- Look-back box (workbook and look-back slide): "I am still stuck (my tutor will check in with me)" -> "I am still stuck (I can ask a grown-up)". Guide and slide notes now say the tutor does not see the page: tell children they can show it to a grown-up at home or tell the tutor at the start of next lesson; next lesson, in the open session, invite anyone who wants another look (volunteers, hand signal or chat, no private messages).
- Breakout pairs visited: guide routine table, safeguarding bullet, explore script (visit each room at least once in minutes 10-15, about 1 minute per room), worksheet script (visit each room at least once in minutes 40-52) and the explore slide notes of every lesson. Within the existing part budgets; no times changed.

## 3. Lesson 10 timer
Two 7-minute stations kept (15 minutes for the part unchanged). Wording now: "the timer is a guide, not a race", "there is no rush", "a pair may pass on a station", "write the answer, or how far you got", tutor note "do not count down aloud, praise the thinking not the speed", "visit every breakout room". Changed in `l10.js` (online, explore, expSetup), `gen_p3l10.py` (notes, slide bullets, online line).

## 4. Overclaim wording
- `guide.js` Level row: "Children finishing Primary 3 (ages 9 to 10), going into P4" -> "Children aged 8 to 10 who are in or have finished Primary 3 maths". Title line "for children finishing Primary 3" left as describing the school year.
- `p3/SPEC.md` "children finishing Primary 3, age 9" -> "children aged 8 to 10 who are in or have finished Primary 3".
- No "covers P3" claim exists in `p3/`. No "Challenge" heading or "challenge session" invite exists in `p3/`.

## 5. MOE wording (Level 3 only)
- L2: single unknown digits now boxes: exit ticket (text, slide picture and key), bank Core c3 and c4 (4A27, 8A50 -> box), pyramid s3 (no A, B, C; "empty bricks"). Letters kept only for multi-letter code puzzles, each now says "each letter is one digit"; the Q6 slide says "same letter, same digit ... a code puzzle". Answers unchanged.
- am/pm: all "a.m."/"p.m." -> "am"/"pm" in L9 (content, slides, gifted.json sneak-peek).
- L7: "breadth" -> "width" (content, bank, slides).
- Not applied: numerator/denominator (L6 does not use or teach the words, so none added); half circle (no semicircle in Level 3).

## 6. Not fixed here (for the lead; shared files)
- Weekly Dose heading "Challenge" and "keep the weekend for the Challenge questions": `hp/parent_pack_level.py` line 14 and 43.
- "challenge session in the next holiday" invite: `levels/mkextras.py` line 210 (Email Pack).
- "(finishing P3)" and ages: `levels/mkextras.py` lines 49-50 (Question Bank, Taster, Email Pack x6, What Learners Get) and `levels/scheme.py` line 10 ("children finishing Primary 3").
- Orphan slide files `p3l9-teachlist.html`, `p3l9-try2.html` in `split/p3l9` are not in the deck order and still show "a.m."; harmless.
- Pacing/redesign items skipped as instructed.

## Checks (Python)
Brute-forced: digit sum 3 four-digit numbers = 10; 2-digit numbers divisible by 6 and 8 = 24, 48, 72, 96 (digit sum 12: 48); grid 56/7 = 8, 81 = 9 x 9, 48/8 = 6; table rows 6t+5 vs 7t equal at t = 5 (35); AB x 3 ends in AB only for 50; odd 3-digit numbers, no 0, digit sum 6, hundreds > tens: 213, 321, 411; zoo 6000 - 1874 - 2524 = 1602; numbers below 100 divisible by 6, 9 and 4: 36, 72; multiples of 12 between 30 and 100 with remainder 2 on 5: 72; big square 10 cm side, perimeter 40, area 100.

## Build and page counts
Decks regenerated (`gen_p3l1..10`, `restyle`), `build_level.sh 3`, `mkextras.py 3`.
- Student workbook: 58 pages (unchanged; five pages per lesson). Note a pitfall: an added standalone paragraph in L6 Q4 pushed pages in other lessons, so the worked example sits inside the question text instead; L2, L5 hints were shortened to avoid a spill.
- Tutor Guide: 93 pages (92 before this pass; recording cues were already in; added breakout and look-back text).
- Weekly Dose: 25. Question Bank 29, Weekly Email Pack 12, Free Taster 5, What Learners Get 1 (all as built by `mkextras.py 3`, self-check OK).
