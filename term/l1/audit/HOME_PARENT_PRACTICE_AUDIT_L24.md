# Home practice, parent summary and online practice audit: Level 1 Term 3 Lesson 24 (Dollars and Change)

Role HOME_PARENT_PRACTICE. Files audited: `out/l24/L24_Home_Practice.pdf` (1 page), `L24_Home_Answers.pdf` (1 page), `L24_Parent_Summary.pdf` (1 page), and `out/l24/practice/` (key `t3l24`, runner version 2, 11 items: 5 Start here, 3 Think harder, 3 Go further; 7 templated, 5 with a drawn picture per variant). Source: `lessons/l24.json`. Read first: `AUDIT2_BRIEF.txt`, `AUDIT_T3_BRIEF.txt`, owner decisions (Term 2 defaults 7, 9; the 23 Oct entries), `TERM_WIDE_AUDIT.md`, the L20 audit of this role, `website/privacy.html`, `docs/books/p1_school_paper_patterns.md` (money).

## Verdict: Ready after minor fixes

Home maths, parent page and print layout are right, and the online practice is sound: every item marks correctly, the ordered two-number item refuses a wrong order, every picture in 42 variants agrees with its question, the "fewest pieces" answers of all eleven variant amounts match an independent dynamic-programming check, there are no network calls and no overflow at phone or laptop width. The faults are small: one ordered item (t3) has a redundant second number and gives misleading feedback to the answer a child would naturally type ("3"), the home sheet has no pictures although the lesson is about pictures of money, and the parent page invites real coins on the table without the supervision line the guide carries.

Counts: High 0, Medium 1, Low 7.

## Method

- Printed pieces rendered at 80 dpi, text extracted, all five home answers solved independently: H1 two 20¢, one 10¢, one 5¢ = 55¢; H2 $5 - $2: $3; H3 $3 + $2 = $5, change from $10: $5; H4 fewest notes and coins for $46 with $1, $2, $5, $10, $50: $10 x 4, $5, $1 = 6 pieces (brute-forced: no 5-piece way exists); H5 50, 55, 60, 65 after 40, 45, 50 (the key lists "55, 60, 65"). All match the answer page, which is a separate sheet (a double-sided print never shows answers behind the questions).
- Online practice served over HTTP and driven in Playwright 1.56 (Chromium) at 390 x 800 and 1280 x 800. Every tier and item opened. Marking by script: c1 `35`, `35¢`, `35c`, `35 cents`, `35.0` right, `3` slip ("3 is how many coins there are"), `thirty-five` "Please type the answer with number digits, like 54."; c2 `17`, `$17`, `17 dollars` right, `3` slip; c3 `2` and `$2` right, `5` and `8` slips; c4 `4` and `$4` right, `10` and `16` slips; c5 choice: `the $2 note` right, `the $1 coin` slip ("The value is the number on the piece, not its size"); t1 `40`, `40¢` right, `60` and `160` slips; t2 `1`, `$1` right, `9` and `6` slips; t3 (ordered set) `3, 1` and `3 1` right, `1, 3` and `1 3` refused with "Those are the right numbers, but not in the right order. Check the order.", `31` refused, `3,1,0` and `2, 1` "Some of these fit, but one does not", a single `3` gets "Those fit. Are there more? Keep looking." (finding 1); g1 `5` and `5 pieces` right, `7` slip, `4` generic; g2 `7` right, `8` and `3` slips, `seven` refused kindly; g3 self-check shows the checking steps even when the box is empty. The same wrong answer twice gets "That is the same answer as before. Read the hint and try a different one." Two different wrong answers show the worked solution. Keyboard: the first box has focus on load, Enter checks. External requests: none. Console errors: none. Horizontal overflow: none at either width.
- Pictures and variants: 42 distinct "Try a similar one" questions taken on c1, c2, c3, c4, t1, t2 and g1 (about 40 variants each for c1 and c2). For each, the displayed money in the SVG was summed and compared with the independent answer (c1 coins to cents, c2 notes to dollars), the price tag was compared with the price in the stem (c3, c4, t1), and the answer was typed and marked "Yes": 0 mismatches. g1 variants ($13, 17, 28, 36, 43, 46, 58, 64, 73, 77, 89) were checked against a dynamic-programming "fewest pieces" answer: all agree (greedy is optimal for 1, 2, 5, 10, 50). Whole and positive everywhere; the c3 and c4 variants never give negative change.
- Page source: `index.html` and `practice.js` hold no answers or external URL; the answers sit in `data/t3l24.json`, fetchable by any browser (shared with every lesson).
- No rewind items in the online runner (brief: note). The home sheet's H5 is the rewind ("Practice from earlier: Term 1 Lesson 4", count in 5s).

## A. Printed pieces

| Item | Finding |
|---|---|
| Home maths | All five correct. H1 and H2 Start here, H3 Think harder, H4 Go further (fewest pieces; "There is no $20 note." is in the stem), H5 earlier practice. Money notation exactly as the school-paper file (50¢-style signs, `$` before dollars, blank carries the unit `____¢` and `$____`). Plain wording, no hints in stems. H1 is a words-only picture of coins ("two 20¢ coins, one 10¢ coin and one 5¢ coin") |
| Can a parent help without teaching differently? | Yes. "Use your play money"; the answers page uses the class words ("start with the biggest", "count up from $2 to $5") and says "wait 10 seconds, then suggest drawing it" |
| Pictures | None on the home sheet (finding 2) |
| Parent summary | One page, 435 words in total, "What we did" about 70 words, plain English. Words list (value, change, count up, cents and dollars with "$1 is 100¢"). The do-not-teach line is specific and right: "Please do not teach decimal money such as $1.50: we write cents and dollars apart." The beyond-P1 statement is honest and specific: "Listing every way to make an amount, how many different amounts three pieces can make, and the fewest notes and coins for $73 go past the school Primary 1 syllabus on purpose." No MOE-aligned, GEP or SASMO claim. Have-ready box is true: price-tag page cut (12 tags), play money and tokens in the envelope. The "when stuck" paragraph states the WhatsApp number once and the 90-day photo retention, consistent with `privacy.html` |
| Recording statement on the parent page | The same one sentence as L1, L22, L23 ("Every lesson is recorded; your tutor will share a private link with enrolled families"); no statement of what is recorded and no "do not share the link" (L11 had both) (finding 5) |
| "Try at home" | "Purse game: put some coins on the table. Count them together" and "Shop game: pick a price and pay with a note". Nothing about supervising small coins (guide: real coins only with a grown-up present, away from younger children) (finding 3) |
| Print layout | A4, left margin 14 mm for the bound edge, answers on a separate page, header and footer clear; the home sheet is about 90% full |

## B. Online practice

Item types: `number` (c1 to c5 except c5, t1, t2, g1, g2), `choice` (c5), `set` with `ordered: true` (t3), `selfcheck` (g3). The tier counts and order follow the lesson: Start here is counting coins and notes and change from $5 and $10, Think harder is change from a $1 coin, two prices and the 50¢ ways, Go further is fewest pieces, the number of amounts and a self-made shop puzzle. Wording is plain and matches the workbook's. Hints name the idea (count up from the price to the money paid), not the answer. Feedback is neutral and kind; after two different wrong answers the worked steps appear ("Let us look at it together"). The shown line is "The answer is 35." (no unit) and for t3 "The answer is 3, 1." followed by the step "The answer is 3 and 1." (slightly inconsistent, Low). No timers, scores or streaks.

Typed answers: `35`, `35¢`, `35c`, `35 cents`, `$17`, `17 dollars`, `35.0` all accepted; words are refused with an instruction; an answer with two numbers in a single-number item ("3, 1" in c1) asks for just the number.

## Findings

| # | Sev | Location | Evidence | Suggested fix |
|---|---|---|---|---|
| 1 | Medium | Online t3 (ordered set) | "Make 50¢ with one 20¢ coin and some 10¢ coins. Type the number of 10¢ coins, then the number of 20¢ coins." The stem gives the 20¢ count (one), so the second number is redundant; the natural answer `3` gets "Those fit. Are there more? Keep looking." (the "list" message), which points the child to look for more ways when there is one; the "ordered" mechanic tests nothing. (The wrong order `1, 3` is refused correctly.) | Ask for one number, "How many 10¢ coins?", or drop the "one 20¢ coin" clue and ask for both numbers for the two ways in a 2-box fields item (3 and 1; 1 and 2 in either row) |
| 2 | Low | Home sheet | Five text-only questions about money; coins and notes are described in words (H1) | Add a small money row to H1 and H2 (the figure engine already draws it) |
| 3 | Low | Parent page, "Try at home" | Real coins are invited without the guide's safety line | "Use play money or coins with a grown-up beside you; small coins stay on the table, away from little ones." |
| 4 | Low | Online c3 | Question says "A toy costs $3" but the tag is a ball | Say "A ball costs $3" or use a tag called "toy" |
| 5 | Low | Parent page | One-sentence recording statement, no "do not share the link" | Reuse the L11 sentences |
| 6 | Low | Runner header | "Level 1 · Lesson 4 · ..." has no "Term 3" (family pages say "Term 3 • Lesson 4") | Add the term to the sub line |
| 7 | Low | Runner, shown answers | "The answer is 35." has no unit; t3 prints "3, 1" then "3 and 1" | Print the unit (35¢, $2) and build the t3 sentence once |
| 8 | Low | Online g1 variants | Only the $73 base has a slip ("Try a bigger piece first"); the other ten amounts get "Not quite yet. Have another go." | Compute the slip for every variant (the "7" slip is the all-$10 greedy count) |

## What passed

Every answer in the printed and online sets is correct; picture and question agree in all variants; the fewest-pieces item is verified against an independent method for each amount; wrong orders are refused; typed units and spaces are accepted; no network calls, tracking or external fonts; the page is usable at 390 px and keyboard-friendly (first box focused, Enter checks, tab order fine). Parent page: one page, plain, true hand-off, honest beyond-P1 statement, a specific do-not-teach line.

## Instrument summary

| Instrument | Result |
|---|---|
| Home sheet maths | 5 / 5 correct |
| Online items | 11 / 11 correct; 42 variant questions picture-checked and answer-checked, 0 mismatches; 11 fewest-piece amounts verified |
| Parent summary against the brief (plain English, word limit, no overclaim, beyond-P1 statement, what to say / not say, hand-off true, privacy consistent) | 5 of 6 PASS (recording sentence thin, finding 5) |
| Online runner (marking, ordered boxes, kind feedback, no leaks, keyboard) | 6 of 6 PASS on behaviour; the ordered item's design is finding 1; answers in a fetchable data file are shared by all lessons |
