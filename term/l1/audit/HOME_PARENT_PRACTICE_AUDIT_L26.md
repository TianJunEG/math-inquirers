# Home practice, parent summary and online practice audit: Level 1 Term 3 Lesson 26 (The School Shop)

Role HOME_PARENT_PRACTICE. Files audited: `out/l26/L26_Home_Practice.pdf` (1 page), `L26_Home_Answers.pdf` (1 page), `L26_Parent_Summary.pdf` (1 page, 438 words), and `out/l26/practice/` (key `t3l26`, runner version 2, 11 items: 5 Start here, 3 Think harder, 3 Go further; 10 templated, 2 with a picture). Source: `lessons/l26.json`. Read first: `AUDIT2_BRIEF.txt`, `AUDIT_T3_BRIEF.txt`, owner decisions (Term 2 defaults 7 and 9, the 23 Oct entries), `TERM_WIDE_AUDIT.md`, the L23 and L25 audits of this role, `website/privacy.html`, `docs/books/p1_school_paper_patterns.md` (money).

## Verdict: Ready after minor fixes

Home maths, parent page and printed layout are right. The online practice marks every static answer correctly, shows pictures that match, makes no network calls, has no script errors and no overflow at phone or laptop width, and all variants I generated have correct answers. Two defects are visible to a child: the `how many two-dollar notes` variants print "1 two-dollar notes" and sometimes start with "0 five-dollar notes" or "$2", and the `how many ways` variant for $20 gives a hint that stops one step short of the answer. The lesson's core activity (list every way) has no list-type or ordered item online, so wrong orders cannot be tested and a child can guess the count. Counts: High 0, Medium 2, Low 6.

## Method

- Printed pieces rendered at 70 dpi and text extracted; all five home questions solved independently: H1 3 + 4 = 7 < 10: Yes; H2 5 x $3 = 15; H3 20 - (8 + 5) = 7; H4 $18 with $2 and $5 notes: nine $2 notes, or two $5 and four $2 (one $5 leaves 13, three $5 leave 3); H5 86 - 40 = 46 and 86 - 4 = 82. All match the answer page. Answers are on a separate sheet, so a double-sided print never shows them behind the questions.
- Online practice served over HTTP and driven in Playwright (Chromium) at 390 x 800 and 1280 x 800. Every tier and item opened. By script: each static item answered wrong (`999`) then right; the written slips (1, 34, 7, 23, 23, 7, 9, 32 and the others) each return their own message; typed `$11`, `$6`, `$21`, `$3`, `$27`, `$2`, `$4`, `$18` are accepted; both options of the choice items mark correctly; the self-check item shows the checking steps. Then 30 "Try a similar one" rounds on the templated items: question text was scanned for raw placeholders, "undefined", double full stops and "1 dollars"-type plurals, picture labels were compared with the numbers in the question, and the answer shown after two wrong tries was compared with the arithmetic (all agree). The `how many ways` template was also recomputed by brute force for each of its five totals ($10, $12, $16, $18, $20): 2, 2, 2, 2 and 3 ways; the template answer `t // 10 + 1` agrees.
- Variant ranges are safe: c1 a 3 to 9, b 2 to 9; c2 price 11 to 18 (left 2 to 9); c3 price 2 to 9 (cost 6 to 27); c4 total 5 to 15 with an integer test that is right at equality; c5 needs 6 to 11 against a book 12 to 16; t1 total under 30 against a $50 note; g1 pads 1 to 3, stickers 3 to 6 (the pair is unique for any total); g2 4 pens at $3 to $9.
- Page source: `index.html` and `practice.js` hold no answers; the answers sit in `data/t3l26.json`, which any browser can fetch (shared by every lesson and runner version; noted, not blamed). External requests: none. Console errors: none. Horizontal overflow: none at either width. Keyboard: the answer box has focus on load and Enter checks.
- Rewind: the online set has no rewind item (n - 10 is lesson 16, tables); the home sheet's H5 is the n - 20 rewind (Term 1 Lesson 6, jump and hop). Noted per the brief.
- Ordered and multi-answer marking: no `fields`, `set` or `multi` item exists in this lesson; the runner supports `set` with `ordered` (used in other lessons) but the lesson uses a count (t2) and a single number (t3, g1) instead, so wrong orders are not tested here (finding 3).

## A. Printed pieces

| Item | Finding |
|---|---|
| Home maths | All five correct. H1 to H3 Start here (enough, equal items, money left), H4 Think harder (every way to pay $18 with two kinds of note, two blanks per way), H5 earlier practice. Plain wording, "$____" blanks, no hints in stems; H1 asks "I know because ___" as the school papers do. H4 lists the two ways in the answer as "0 five-dollar and 9 two-dollar; 2 five-dollar and 4 two-dollar" without saying that the two ways may be given in either order (Low, finding 7) |
| Can a parent help without teaching differently? | Yes. The sheet says "use your price tags and play money", "a grown-up may read the questions aloud", "wrong answers are fine". The answers page uses class words ("no $5 notes", "one $5 note leaves $13", "count up from 13 to 20") |
| Pictures | None. Money questions without a note or a tag; a table frame for H4 would help (finding 6) |
| Parent summary | One page, 438 words; "What we did" about 70 words, plain English. Words list explains budget, exactly, enough, left and "a way". "Please do not teach a rule; going in order is the method" is the do-not-teach line (a rule and a method in one sentence: Low). Beyond-P1 statement honest and specific ("Listing every way to spend exactly $20, and paying $20 with three kinds of note, go past the school Primary 1 syllabus on purpose") with the P1 part stated as well. No MOE-aligned, GEP or SASMO claim. Hand-off box: tiles page (page 6 of your book, see finding 5), tags and money for the Quest, coloured pencil optional. The WhatsApp number and the 90-day retention appear once and agree with `privacy.html` |
| Recording statement on the parent page | One sentence: "Missed a lesson? Every lesson is recorded; your tutor will share a private link with enrolled families." No "any voice that is unmuted" and no mute route (`privacy.html` offers one); the L11 and L12 pages had both (finding 4) |
| Print layout | A4, left margin about 14 mm (the bound edge), answers on a separate page, header and footer clear. The home sheet is about 88% full; the parent page is full, two-column |

## B. Online practice

Item types: `number` (c1, c2, c3, c5, t1, t2, t3, g1, g2), `choice` (c4), `selfcheck` (g3). Tier counts and order follow the lesson: Start here total, left, equal items, enough, how much more; Think harder three items and change from $50, how many ways to pay, how many two-dollar notes with a known number of five-dollar notes; Go further 7 things, change from $50, and an own puzzle. Wording is plain and matches the workbook (the static items repeat workbook S2, S3, S5, S4, T3 and G2 almost word for word, so a child who did the workbook meets them twice before any variant). Hints name the idea, not the answer. Wrong-answer feedback is neutral ("Not yet. Try once more." then the hint, then "Let us look at it together" with the answer and steps on the second wrong try); no scores, timers or streaks. Typed answers: spaces, a dollar sign, a leading zero and a trailing unit are handled; words are refused with an instruction. Two lines sit under every first wrong answer ("Not yet. Try once more." and "Not quite yet. Have another go."): redundant but harmless.

## Findings

| # | Sev | Location | Evidence | Suggested fix |
|---|---|---|---|---|
| 1 | Medium | Online t3 variants ("Try a similar one") | The template picks 0, 2 or 4 five-dollar notes and 1 to 6 two-dollar notes. Seen in a run of 30: "Ali pays exactly $2 with 0 five-dollar notes and some two-dollar notes. How many two-dollar notes?" (answer 1; a pointless question); the shown solution prints "The rest is 1 two-dollar notes." (a plural slip, the pattern the preflight lists as seen in "1 hours", "1 stickers"); the solution steps never show the value of the five-dollar notes ("2 five-dollar notes are the first part. Take that away from 12.") | Draw b from 1, 2, 3 and k from 2 to 6 so the plural is always right; add a derived value `five` (5 times b) to the steps ("2 five-dollar notes are $10. 12 take away 10 is 2.") |
| 2 | Medium | Online t2 variants (`how many ways`) | Hint: "Go in order: no $5 notes, then one, then two, then three." For the $20 variant there are 3 ways and the third needs four $5 notes (four $5 notes and no $2 notes). A child who follows the hint stops at three $5 notes, finds 2 ways, and is told "Not yet"; the solution steps ("Try each number of $5 notes in order") never list the ways | Make the hint "Go in order: no $5 notes, one, two, and so on until the notes are too much" and show the ways in the steps; or drop $20 from the template |
| 3 | Low | Online set against preflight section 13 | WAYS T and LIST T have no list-type online item: the count of ways (t2) can be guessed (answers 2 or 3) and "is this list complete" (workbook T2) has no online form; the runner has `set` and `ordered` types for exactly this | Add a `set` item "Pay exactly $12 with $2 and $5 notes. Type the number of $5 notes in each way" (answers 0 and 2) with a wrong-order and a missing-way message |
| 4 | Low | Parent page | One-sentence recording statement; no "any voice that is unmuted" and no mute route; `privacy.html` promises one | Reuse the L11 wording |
| 5 | Low | Parent page and slide 30 | "The grid-tile page (page 6 of your book)": workbook footers number pages 1 to 6 inside each lesson, and a bound term book has more pages | "page 6 of your Lesson 7 workbook" |
| 6 | Low | Home sheet and online c1 | Five text-only home questions in a money lesson; online c1 states a ruler and a glue stick but draws only the ruler tag | Add the second tag to the c1 picture; one note picture beside H4 |
| 7 | Low | Home answers H4 | "0 five-dollar and 9 two-dollar; 2 five-dollar and 4 two-dollar": nothing says that the two ways may be written in either order, which is the lesson's own message | "Either order" in the answer page |
| 8 | Low | Online c5 slip and c4 steps | c5 slip: "The question asks how much more money he needs" (Aisha is she); c4 step "Compare the total with 10" has no $ sign; runner header "Level 1 · Lesson 6 · Plan within a budget and list every way" has no "Term 3" (family pages say "Term 3 • Lesson 6") | Say "she", "$10", and add the term to the sub line (runner change, backward compatible) |

Counts: High 0, Medium 2, Low 6.

## What passed

Every answer in the printed and online sets is correct (about 190 variants checked by script); picture and question agree (c1 and c2 tags show the right item and price in every variant); typed answers with a dollar sign, a leading zero or spaces are accepted; no network calls, tracking or external fonts (fonts are local); keyboard focus and tab order are sensible; the page works at 390 px with no overflow; the written slips catch the errors in the key's "Watch for" (adding the amounts for "left", the cost of one ruler for three, the total for the change). Parent page: one page, plain, no overclaim, beyond-P1 statement with both halves, true hand-off apart from the page wording.

## Instrument summary

| Instrument | Result |
|---|---|
| Home sheet maths | 5 / 5 correct |
| Online items | 11 / 11 correct; about 190 variants checked by script, 0 wrong answers, 0 picture mismatches, 1 plural slip pattern (t3), 1 misleading hint (t2 at $20) |
| Parent summary against the brief (plain English, word limit, no overclaim, beyond-P1 statement, what to say and not to say, hand-off true, privacy consistent) | 5 of 6 PASS (recording sentence thin, finding 4; hand-off page wording, finding 5) |
| Online runner (marking, ordered boxes, kind feedback, no leaks, keyboard, pictures) | 4 of 6 PASS (no ordered or list item to test wrong orders, finding 3; variant text defects, findings 1 and 2; the answer data sit in a fetchable file shared by all lessons) |
