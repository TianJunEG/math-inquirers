# Independent audit, round 1: daily website teasers (Nov and Dec 2026 batches)

Auditor: independent reviewer (did not write or run the builder's checks as evidence; reproduced them as a cross-check only).
Date of audit: 24 Oct 2026. Branch `claude/great-fermi-1hv4vc` at commit 62f85b4 (working tree clean before this file).
Scope: `website/teasers` (366 puzzles, 6 levels x 61 days), `teasers.js`, page wiring, preview, owner decisions
TEASER-DAILY-GO, TEASERS-365-MONTHLY, TEASERS-PER-LEVEL. Nothing under `website/dist` was touched; all builds were in scratch folders.

## Verdict

**Not ready to release as it stands. Correctness, engineering and privacy pass; originality and "new frame" do not.**

| Area | Result |
|---|---|
| 1. Maths correctness (84 hand-solved from the question text only) | **Pass**: 84 of 84 agree with the stored answer; every one has a single answer; explanations correct and kind except two typos |
| 2. Level fit, reading load, wording | **Pass with fixes** (one brand name, 2-cent coins, some topics beyond the level page's own list) |
| 3. Originality and frames | **Fail (High)**: December is largely November with new numbers; several near-copies of holiday, extension and the level pages' own sample puzzles |
| 4. Browser behaviour | **Pass** with Medium/Low items (light-mode contrast of the hint, late-fetch rule, focus after "Show me how") |
| 5. Flag off = byte-identical; dist untouched | **Pass** |
| 6. Privacy | **Pass** (0 cookies, 0 storage, 0 third-party requests) |
| 7. Feb 29 and Jan-Oct plan | **Pass on mechanics**; plan needs a structure budget before 1,830 more puzzles are written |

Severity counts: High 2, Medium 9, Low 12.

## 1. Hand-solved sample

I chose 14 puzzles per level (84 in all), each of a different maths kind within its level, 49 from November and 35 from December,
and solved each from the question text (and the code or grid shown) before looking at the bank. Then I compared with the stored answer
and read the hint and the worked explanation. I also read all 366 questions and re-derived the large majority of the remaining
answers (all of Levels 3 to 6 and most of Levels 1 and 2) while reading. No disagreement was found.

| Level | Sampled (kinds) | Agree | Notes |
|---|---|---|---|
| 1 | ribbon share, week of stickers (sum), count back, race order, football time, sticker chain, cards 307, think-of-a-number, outfits, 8 cents in coins, beads, lesson weekday, lamp/pot loop, queue | 14/14 | |
| 2 | cards 604, sticker book sum, pencil boxes, which term, lift (highest floor), netball pairs, digit sum 8, secret number, birthday weekday, 3rd Saturday, carpet hole, stamp sets, pattern machine, sum and difference | 14/14 | |
| 3 | tables for 47, magic square, kuih change, tile arrays, tank 5/6, common multiple, consecutive houses, aunt ages, divide-by-3, bakery, squares in 3x3, remainder riddle, postage sets, straight-line angle | 14/14 | postage: see L-3 below |
| 4 | laps decimal, brackets, A-B-C cryptarithm, coach time 24-hour, group sizes, rectangles in 3x3, mean, noticeboard border, painted cube, quiz goal, mixed-number sum, tile figures, puddle routes, pages of a book | 14/14 | |
| 5 | arrangements of 1123, who knocked the pot (logic), 50 cents in coins, give-ten ratio, jacket 15% off, order of ages, fish tank depth, remainder triple, staircase sum 1..60, cuboid cubes, house area, survey percentages, speed, bathtub leak | 14/14 | |
| 6 | six factors, four coins, hidden cubes, marbles ratio, phone plan, octagon diagonals, up 20% then down 20%, freezer, nested loop, turtle, 8-unit tiling, reversed number x4, term of a sequence, shift cipher | 14/14 | |

Uniqueness: for the logic, counting and coin items I enumerated the cases myself (for example "Exactly two tell the truth" gives only
Ravi; 12 sets for fifty cents; 13 tilings of 8 units; 36 rectangles in a 3 by 3 grid; 8 routes round the puddle). Each has exactly one answer under
the reading the question gives. Worked explanations: all arithmetic correct; tone is kind ("Not yet", "Now ask: how do you know?").

Findings in this section:

- **M-1 (Medium)** Two worked explanations print "years years": `L3-aunt` (12-13: "In 6 years years, Aisha will be 12...") and `L4-grandpa` (12-21: "In 5 years years Hui Min will be 9..."). The template of the `age_times` kind adds "years" twice. Children see this after a correct answer. Fix the template; add a doubled-word check to `verify_bank.py` (my scan of all text found only these two).
- **L-1 (Low)** `L6-sixfactors` hint "Try 12, 16 and 18" and `L6-eightfactors` hint "Try 16, 20 and 24" list the answer among three candidates, so the puzzle reduces to counting factors of three numbers. Use "Try some small numbers and list their factors" instead.
- **L-2 (Low)** `L3-postage` (12-08, "many 5-cent stamps and many 2-cent stamps ... how many different sets") answer 2 counts the set of seven 2-cent stamps (no 5-cent stamp). A child who reads "sets of 5-cent and 2-cent stamps" as needing both gets 1. Same wording risk in `L1-coins8`. Add "(you may use only one kind)" or rephrase.
- **L-3 (Low)** `L4-symmetry2` (12-11) counts an isosceles triangle as 1 line, a kite as 1 and a rhombus as 2. An equilateral triangle is also isosceles under some definitions and a rhombus is a kite under others. A kite is not in the MOE primary syllabus. Say "an isosceles triangle with exactly two equal sides" and drop or define "kite".
- **L-4 (Low)** `L3-round350` (11-16, "from 1 cent upwards round to 350 cents") relies on half-up rounding (345 rounds to 350); say so in the question.

## 2. Level fit, reading load, wording

Reading load (words per question, mean / max): L1 24 / 36, L2 25 / 39, L3 27 / 50, L4 27 / 49, L5 27 / 46, L6 28 / 53; mean sentence length 7.8 (L1) to 9.9 (L6) words,
long words per question 0.3 (L1) to 0.7 (L4). Appropriate for the bands; the longest items (the "each say one thing" logic puzzles, 43 to 53 words) are the heaviest and
are fine for L5/L6, a stretch at L3/L4 (`L4-fourliars`, 49 words, four speakers).

Names (197 mentions): Chinese 67, Malay 52, Indian 48, other 30 (Ben, Daniel, Sam). Balanced and inclusive. No pictures anywhere, no coin or note images (money is words and numbers).
Singapore spelling and settings correct throughout (metres, litres, colour, Mum, Aunty, hawker centre, HDB, MRT, kopitiam, GST 9%, Primary 5). No scary, violent or demeaning content found.

Findings:

- **M-2 (Medium) Brand name.** `L1-toast` (11-18) says "A cup of Milo" (a trademark). The rule is no brand names. Use "a cup of chocolate drink". ("Kaya toast", "kuih", "teh", "bubble tea", "Merlion", "Sentosa" are generic dishes or places, fine.)
- **M-3 (Medium) Coins that do not exist.** Singapore has no 2-cent coin (and 1-cent coins are no longer in everyday use). `L1-coins8` (5, 2, 1 cent), `L1-sixcents` (2 and 1 cent), `L2-stampsets` and `L3-postage` (2-cent stamps) use them. Use 5, 10, 20 and 50 cents only (as `L2-coins30`, `L3-coins40`, `L5-fiftycents` already do).
- **M-4 (Medium) Content above the level page's own list.** Checked against the level pages' blurbs and `docs/moe/syllabus_by_level.md` (the MOE file says ratio is P6, order of operations and angles on a line are P5, mean is P6, median, mode, probability, negative numbers, primes and hexagon/pentagon angles are not in the primary syllabus at all):
  - L3: angles on a straight line (`L3-straightline`, P5 topic) on an "Ages 8-10, builds on Primary 3" page whose list does not mention angles.
  - L4: median and mode (`L4-plants`, `L4-shoesize`), the interior angle of a regular hexagon (`L4-hexagontile`), triangle angle sums and isosceles (`L4-isosceles`, `L4-trianglecorner`): not on the L4 page list ("factors and multiples, five-digit numbers, order of operations, decimals, angles and data") beyond "angles and data" and P4 angle measurement.
  - L5: ratio is 7 of 61 puzzles (11%) and percentage 9; ratio is not in the L5 page list ("numbers to 10 million, fractions, area of a triangle, volume, rate, percentage and angles"). Interior angles of a regular pentagon (108) and octagon (135) need a polygon-angle idea the primary syllabus does not teach.
  - L6 matches its page list (sequences, primes, negative numbers, algebra, counting, probability, codes). L1 and L2 are within band, with a few (`L1-football` 90 minutes, `L1-coins8` three coin kinds) at the top of Ages 6-8.
  Since the levels are three-year age bands this can be intended stretch, but the owner should confirm the policy "up to one school year above the page list" or trim the items above.
- **L-5 (Low)** Blame wording: the "who broke / took / emptied it" logic puzzles name a child as the culprit (L3 vase Mei Ling, L4 cake Siti, L5 pot Ravi, L6 window Nurul, L6 jar Ben). Not unkind in itself, but 3 of 5 culprits have Malay or Indian names. Prefer neutral framing ("who has the key?") or rotate.
- **L-6 (Low)** `L6-wintercities` (12-09) and the 12-09 "winter morning" are temperate-climate framings; harmless, but "a cold city" would match the Singapore setting used elsewhere.

## 3. Originality, frames and repeated structures

### 3a. Similarity read (my own method, independent of `verify_bank.py`)

I indexed 3,321 files (9.6 million words: holiday banks and lesson files p1 to p6 and hp, term lessons, all extension workbooks, the school booklets in `school/`,
docs/books and docs/sasmo including the private source files, practice, review, taster) and compared every teaser question two ways: (i) shared 6-word runs after masking digits,
(ii) closeness of the question to every question string in those files (content words, names and numbers removed). 33 teasers score 0.6 or more and 63 score 0.5 or more on (ii)
(by level: L1 8/16, L2 3/7, L3 10/17, L4 7/8, L5 4/11, L6 1/4 at the 0.6 / 0.5 thresholds). Most are generic stems ("a film starts at ... and ends at ..."). The ones I regard as copying the structure,
not just the stem, are:

**H-2 (High) Near-copies, same story or same numbers, only parameters changed** (rewrite each with a new story and a new structure):

| Teaser | Source | Why it is a copy |
|---|---|---|
| `L3-riddle21` (12-01) "number from 20 to 30, divide by 4 remainder 1, divide by 6 remainder 3" | The **Ages 8-10 level page's own sample puzzle** and the P3 holiday tutor guide: "between 20 and 30, divided by 4 remainder 3, divided by 6 remainder 5" | Same range, same two divisors, same wording shape. It is also what a visitor with JavaScript off sees. |
| `L4-riddle52` (11-29) | same P3 holiday item | Same skeleton ("I am a number between..., divide by..., remainder..."). |
| `L1-marbles` (11-10) "Ben has 12 marbles. Aisha has 5 more than Ben. Hui Min has 3 fewer than Aisha..." | `hp/qbank.py` (Level 1 holiday): "Ali has 8 marbles. Mei has 5 more than Ali. Ben has 6 fewer than Mei..." | Same story (marbles), same chain, same "5 more". |
| `L3-uncle` (11-04) "Ben is 7 ... his uncle is 31 ... twice as old" | `extension/data/l3_u04.json`: "Ravi is 7 years old. His father is 35 years old ... twice as old" | Same level, same age 7, same "twice", only 35 to 31. The kind recurs: L3 11-04, 12-13; L4 11-28, 12-21; L5 11-02 (and extension L5U03 and a sasmo draft). |
| `L6-dice10` (12-25) "Two fair dice are rolled and their numbers are added... total of 10 or more" | `p6/content/l10.js` (holiday): "Two dice are rolled and the numbers are added. What is the probability that the total is 10 or more?" | Same question. |

**M-5 (Medium) Close to our own drafts or to catalogue examples** (policy "new story AND new frame" applies to our own material too):
`L4-cube3` (11-12) and `L6-cube5edges` (12-19) against the catalogue example "A 3 by 3 by 3 cube is painted on all faces and cut into 27 small cubes... exactly 2 painted faces" (`docs/books/private_p6_papers/verify_catalogue_examples.py`, derived from an external paper);
`L1-queue` (11-22) is the sasmo Grade 2 item "Mei is 4th from the front and 6th from the back" with 6th and 4th swapped, and `L2-lunchqueue`, `L2-busline` repeat the same queue structure;
`L1-lamps` (11-21) is the book draft "path 60 m, lamp post at each end and one every 10 m" at 20 m and 5 m;
`L5-giveten` (11-30) is the sasmo Grade 5 item "Ben and Siti have stamps in the ratio 5:3. Ben gives Siti 12 stamps and then they have the same number";
`L2-digitsum8` and `L3-sumten` reuse the P2/P6 holiday stem "How many 3-digit numbers have digits that add up to 5?" with 2 digits (and they are the same item twice, across L2 and L3);
`L5-moresticker`, `L5-boysgirls` against `p5/qbank_skills.json`; `L3-spentfrac`, `L3-allowance`, `L3-lunchmoney` against `extension/data/l5_u07.json` and `l5_u10.json`;
`L2-num6`, `L1-think8`, `L2-think9` against the extension and sasmo "I think of a number" items; `L1-parcel` is the P6 holiday "Today is Monday... 10 days" item.

**M-6 (Medium) The wording test is looser than the extension standard.** `verify_bank.py` fails only on a shared run of 9 words; the extension checker (`extension/verify/dup_check.py`) fails on 7 and uses a stock-phrase list.
The 54 listed 7 to 8 word "stems" in November alone would be FAILs under the extension rule unless added to `stock_phrases.txt`. None of the listed stems is a copied sentence, so this is a process gap, not a copying finding. It also does not look at structure at all, which is how the High items above passed. Add a masked-skeleton check (digits and names replaced, 6-word runs against all sources, plus the seven fixed website puzzles) and review its list per batch.

### 3b. Is "at most 5 uses of one maths kind per month" an acceptable reading of "frame"?

**No, not as the only rule.** What I verified: the claim is true (largest count of one kind in a month is 5, `L5` pct in December; most months 2 to 4), story-frame ids are unique per level, and neighbouring days differ.
But the owner policy elsewhere is "new story AND new frame", and the data show the second half is not met:

**H-1 (High) December is November re-parameterised.** For each level, the share of puzzles whose maths kind also occurs in the other month:

| Level | Nov puzzles with a Dec twin kind | Dec puzzles with a Nov twin kind | Kinds in both months / total kinds |
|---|---|---|---|
| 1 | 28 of 30 | 30 of 31 | 22 / 25 |
| 2 | 27 of 30 | 30 of 31 | 25 / 29 |
| 3 | 23 of 30 | 24 of 31 | 22 / 36 |
| 4 | 24 of 30 | 28 of 31 | 19 / 28 |
| 5 | 21 of 30 | 27 of 31 | 16 / 29 |
| 6 | 30 of 30 | 30 of 31 | 23 / 24 |

A child who does the puzzle for two months meets the same structure again with a new story: Level 6 has 23 kinds in 61 days, and every November puzzle has a December twin
(nested loop 4 vs 6, turtle 25 steps/45 degrees vs 12 steps/60 degrees, "add to make equal" ratio, reversed-number x4 vs x9, shift cipher 5 vs 3, polygon diagonals octagon vs 12-gon, tribonacci stairs 6 vs 7, anagram PUZZLE vs BANANA...).
Projected over a year: 25 to 36 kinds per level for 366 days is about 10 to 15 returns of each kind per level, and the "at most 5 per month" rule permits that. This is a policy decision for the owner (one question: "Is the same maths idea with a new story acceptable once or twice a month, all year?"). My recommendation: require a new structure, not only a new story, within a level for at least 60 days, cap one kind (and each sub-structure such as reverse percentage, successive percentage, equalising a ratio) at 3 per level per quarter, and have `verify_bank.py` enforce it across released months, not only story ids.

**M-7 (Medium) Repeated structures within a month and within a level across months** (the same level; story changes, structure and often numbers do not):

- Same numbers or answer reused: L1 11-19 and 12-09 (squares of sticks: 4 sticks then 7 sticks, only 4 vs 6 squares asked; and 12-13 triangles repeat the pattern at L1, L2 11-23 and L3 12-17); L6 11-21 and 12-01 (the same nested loop, 4 vs 6); L4 11-01 and 11-08 (the same five marks, 72, 85, 64, 91, 88, used forwards and backwards in one month); L5 11-03 and 12-06 (tap and leak, both with a 5 L a minute leak); L5 11-23 and 12-17 (tank depth, both 8 cm); L2 11-03 and 12-29 (grid with a 2 by 2 corner removed); L1 11-21 and 12-19 (posts at both ends, answer 5; and 12-31 circle with answer 5).
- Same structure, different story: L2 11-06 / 12-26 / L1 11-22 queues; L2 11-26 / 12-22 pairs (and L1 11-04); L2 11-04 / 12-31 lift floors (and L1 11-02, 12-23); L3 11-28 / 12-24 weighing fruit; L3 11-29 / 12-18 grid routes; L3 11-25 / 12-02 days ahead; L4 11-18 / 12-31 and L6 11-26 / 12-26 grid routes with one blocked point (L6 12-26 is the L4 puddle puzzle with other numbers); L4 11-20 / 12-03 factor counts; L4 11-25 / 12-05 greatest common factor; L4 11-27 / 12-29 meeting times (same as the Ages 9-11 page sample, "two lighthouses flash every 6 and 9 seconds"); L4 painted cube 11-12 / 12-23 (+ L5 11-17, L6 11-03, 12-19); L5 percentages (9): reverse percentage 11-20 / 12-01, "percentage of" 11-25 / 12-11, discount 11-09 / 12-18, successive change 11-04 / 12-24 (+ L6 11-22 / 12-15); L5 ratio (7): find the total from one part 11-28 / 12-12, make equal 11-30 / 12-16, share 11-15 / 12-03; L5 speed 11-07 / 12-23; L5 mean with one removed 11-16 / 12-08; L6 probability (8): two dice total 11-12 / 12-25, coin tosses 11-25 / 12-20, without replacement 11-28 / 12-17; L6 binary (3), primes and factor counts (7), turtle (2), cipher (2), nested loop (2), program trace (2), term of a sequence 11-14 / 12-22 (and 12-24).
- Fraction sequences ("spends 1/3, then 1/4 of what is left") occur in L2 (2), L3 (2), L5 (1), as does the Ages 10-12 page sample ("1/3 then 1/4") and extension L5U07.
- Cross-level same item: `L2-digitsum8` and `L3-sumten`; the sticks-triangles row at L1, L2 and L3; palindromes at L3 (3-digit) and L4 (4-digit) 12-01.
- Per-month cap check: confirmed at most 5 per month (L5 pct, December); 4 for L6 prob and L5 ratio in November, so the stated rule holds.

## 4. Browser behaviour (Playwright + Chromium, PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers; scratch build `MI_TEASERS=1 ... build_site.py --out <scratch>`; the preview file also tested)

My own tests, then a cross-check with the builder's `test_site.py` on the same scratch build (392 checks, 0 failed, reproduced).

Pass:
- **Date rollover.** 10 browser time zones (Singapore, Los Angeles, Kiritimati UTC+14, Pago Pago UTC-11, London, Kolkata, Auckland, Lord Howe, St John's, UTC) at 30 Nov 23:59:59 SGT, 1 Dec 00:00:00 SGT, 31 Dec 23:59:59, 1 Jan 00:00:00, 30 Nov 23:59:59 UTC (= 1 Dec 07:59 SGT), on Level 1 and Level 6: the puzzle id and date always equal the Singapore date's bank entry (or the fallback pool when no batch). The date label ("Puzzle for Tue 1 Dec") is the Singapore date. A page left open and focused across midnight keeps the old puzzle (no timers, by design) and switches to the new day on the next focus or visibility event; verified.
- **Fetch failure.** Aborted, 404, 200 with an HTML body, malformed JSON, `[]`, `null`, a month missing the key: each falls back to a pool puzzle with no blank box, no error shown. Script injection in a puzzle string is rendered as text (textContent). JavaScript off: the fixed puzzle remains on the home page and level pages.
- **Answer formats.** For all 366 puzzles: the shown form and the plain answer are accepted; every integer from -30 to max(400, 4 x answer + 50) other than the answer is rejected; decimals near the answer, answers with a digit appended or prepended, and "answer + junk unit" are rejected; text puzzles reject unrelated words. Hand-picked cases: `5`, ` 5 `, `5 cm`, `5cm`, `5 CM`, `5.0`, `5.` accepted; `5 m`, `50`, `4.9`, `5 5`, `5 apples` rejected. Money `1.60`, `$1.60`, `1.6`, `S$1.60` accepted, `160`, `1,60`, `1.50` rejected. Fractions `3 4/5`, `19/5`, `3.8`, `3 4/5 L` accepted; `3 8/10` and `10/32` give "write it in its simplest form"; wrong unit rejected. Thousands `1,830`, `1 830` accepted, `1.830` rejected. `-6`, unicode minus handled.
- **Layout.** All 366 puzzles at 390 px: no horizontal page scroll and nothing outside the box; 320 px and increased text spacing: no scroll. Code and grid blocks scroll inside their box. Buttons 47 and 44 px high, input 16 px font (no iOS zoom). Screenshots read: tidy at 390 and 1280 px, light and dark.
- **Preview** (`outputs/owner_review/teasers_preview/index.html`): 0 script errors, 0 external requests, date and level selector matches the bank on 30 cases at both widths. It carries the answer key: not under `website/dist`, not deployed by `wrangler.jsonc` (assets directory is `website/dist`).
- **Keyboard and screen reader.** Tab reaches the input, "Check" and "Show me how" in order; Enter submits; a visible 3 px outline on each; the input has `aria-label="Your answer"`; `#pzMsg` is `role=status aria-live=polite` and empty until used; the section keeps its `h2`.

Findings:
- **M-8 (Medium) Contrast of the hint (light mode).** The "Not yet. Hint: ..." text is `#D64545` on `#F8DEDE`, contrast 3.44:1 (WCAG AA needs 4.5:1 for 16 px text); the correct-answer box (`#1F7A6F` on `#DCEFEA`) is 4.32:1. These hold the hint and the worked explanation, the most important text for a child who is stuck. Dark mode passes (5.04:1). Darken the two text colours (for example `#A82D2D` and `#17655B`) or set the body colour inside the boxes. Everything else measured is 5.35:1 or better.
- **M-9 (Medium) Late or failed fetch gives different children different puzzles.** The fetch is abandoned after 2.5 s and the page then shows a November pool puzzle for the whole visit, even if the month file arrives a second later (tested with a 3.5 s delay: it stays on the pool puzzle). The label still says "Puzzle for Sat 5 Dec", so the claim "every visitor sees the same puzzle that day" fails for slow connections. Accept the late reply when it arrives (re-render only if the child has not typed) or raise the limit; and show nothing about a date that the puzzle does not belong to. (Also: the Cloudflare cache is 1 h for month files, fine.)
- **L-7 (Low)** After "Show me how" the button is removed and focus falls to the page body; move focus to the message or keep the button. The `aria-label` on the `<pre>` code block is not reliably announced; use `role="group"` or a visible caption. The input has only a placeholder-and-`aria-label` (no visible label).
- **L-8 (Low) Correct answers not recognised** and answered with "Not yet. Hint": `21st` and `21 st` for a date question (`L2-saturday`), `0.96` for a percentage, `on Sunday`, `junhao`, a unicode fraction slash (`3 4⁄5`), `+7`, `1 h 30 min` for a minutes question. At least add ordinal suffixes and "on". A child who knows the answer should not read "Not yet".
- **L-9 (Low)** No way to see help before a first wrong attempt (design choice, noted by the author). Consider a "Need a hint?" button for a shy child.
- **L-10 (Low)** A request for the next month's file returns 404 on every page load when a month is not released (console error, one wasted request). Harmless; skip the fetch when the month is not in the released list the page already knows.
- **L-11 (Low)** The device clock decides the day. A device with a wrong date shows a puzzle for that wrong date; acceptable for a teaser.
- Whole month's puzzles and answers are in each month JSON (visible in source). Fine for a teaser; not a finding.

## 5. Flag off and dist

- In a scratch copy of the repo, with no `MI_TEASERS` and `site_enabled` absent: `lp_build.py` and `level_pages.py` reproduce `website/mi_signup.html` and all six `website/level_pages/*.html` **byte for byte** (`cmp` equal). `build_site.py --out <scratch>` then equals the committed `website/dist` (`diff -rq`: no differences, no `teasers/` folder, no `/teasers/*` header).
- `git diff HEAD origin/claude/great-fermi-1hv4vc -- website` is empty; `git status` clean; nothing was written under `website/dist`. The branch had two newer WIP commits on origin (dd2f935, 8dd2371) that do not touch `website/teasers` or `website/dist`.
- With `MI_TEASERS=1`: 12 month files (176 KB), a `/teasers/*` cache header, the CSP already allows the same-origin fetch and inline script (`connect-src 'self'`, `script-src 'self' 'unsafe-inline'`).
- **L-12 (Low) Docs mismatch.** `README.md` says `site_enabled` is `false` in `manifest.json`; the key is absent (it works because absence means off). Also, TEASER-DAILY-GO said "current fixed puzzle stays as fallback"; the build uses a November pool as the fallback and the fixed puzzle only when JavaScript is off. Reasonable, but record it as an owner decision.

## 6. Privacy

On the home page and Levels 3 and 6, after typing wrong and right answers and pressing "Show me how": `document.cookie` empty, no localStorage, sessionStorage, IndexedDB, Cache storage or service worker; context cookies empty; the only requests are the page's own and `/teasers/L<n>-<MM>.json` on the same origin (0 third-party hosts); no console errors with a released month. Nothing is sent when an answer is typed.

## 7. Feb 29 and the Jan to Oct plan

- 29 Feb: `build_bank.py` has `DAYS_IN['02'] = 29`, so a February batch gets a 29 Feb entry for every level (366 per level, 2,196 in all; the owner said 365, so record that the extra is the leap-day spare). `teasers.js` keys by `MM-DD`, so 29 Feb 2028 (SGT) selects `02-29`; in 2027 and other non-leap years the entry is never shown and 28 Feb is followed by 1 Mar with no gap (tested: 28 Feb 2027 23:59:59 SGT then 1 Mar). Until February exists, 29 Feb 2028 shows a pool puzzle (tested).
- Plan: 305 puzzles per level remain (366 - 61), 1,830 in all; January must pass its own audit before 31 Dec 2026 (68 days from today), then about one batch a month. Until a month is released, visitors get the November pool by day number, so the same 30 puzzles repeat from 1 Jan; acceptable only as a stopgap.
- Because the bank recycles by calendar date, every child sees the identical puzzle on the same date next year. State this to the owner (the manifest note says "the year recycles").
- Before writing Jan to Oct: settle the frame policy (H-1), fix the near-copy list (H-2), add the skeleton check and the cross-month structure budget to `verify_bank.py`, and make each batch's independent audit start from a list of every kind and sub-structure already used per level.

## Findings list (for the fix round)

| ID | Severity | Item |
|---|---|---|
| H-1 | High | December re-uses November's maths structures; "frame = story" reading fails "new story AND new frame"; needs owner decision and a structure budget |
| H-2 | High | Near-copies: `L3-riddle21` and `L4-riddle52` (level page sample and P3 holiday), `L1-marbles` (hp qbank), `L3-uncle` (extension L3U04), `L6-dice10` (P6 holiday) |
| M-1 | Medium | "years years" typo in `L3-aunt` and `L4-grandpa` explanations |
| M-2 | Medium | Brand name "Milo" in `L1-toast` |
| M-3 | Medium | 2-cent coins and stamps do not exist in Singapore (`L1-coins8`, `L1-sixcents`, `L2-stampsets`, `L3-postage`) |
| M-4 | Medium | Topics above the level page lists and the MOE syllabus (L3 angles on a line; L4 median, mode, hexagon angle; L5 ratio 11%, polygon angles) |
| M-5 | Medium | Close to our own drafts, catalogue and extension items (list in 3a) |
| M-6 | Medium | 9-word fail threshold weaker than the extension 7-word rule; no structure check |
| M-7 | Medium | Repeated structures and identical numbers inside a level across months (list in 3b) |
| M-8 | Medium | Light-mode contrast of hint 3.44:1 and correct box 4.32:1 |
| M-9 | Medium | Fetch abandoned after 2.5 s: slow visitors get a pool puzzle all visit with a date label that does not match |
| L-1 to L-4 | Low | Hints naming the answer (sixfactors, eightfactors); postage and coins "sets" ambiguity; symmetry definitions; rounding half-up |
| L-5, L-6 | Low | Blame wording and who is the culprit; winter city |
| L-7 to L-11 | Low | Focus after "Show me how"; `aria-label` on `pre`; unrecognised correct formats (21st, 0.96, on Sunday); no early hint; 404 per page load for unreleased months; device clock |
| L-12 | Low | README says `site_enabled: false` but the key is absent; fixed-puzzle fallback differs from TEASER-DAILY-GO wording |

Not found: any wrong answer, any non-unique answer in the sample, any cookie or storage, any third-party request, any change to `website/dist`, any coin or note image, any American spelling, any scary content.
