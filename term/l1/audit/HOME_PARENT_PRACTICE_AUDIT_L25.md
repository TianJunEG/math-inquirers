# Home practice, parent summary and online practice audit: Level 1 Term 3 Lesson 25 (Price Tags: Compare and Choose)

Role HOME_PARENT_PRACTICE. Files audited: `out/l25/L25_Home_Practice.pdf` (1 page), `L25_Home_Answers.pdf` (1 page), `L25_Parent_Summary.pdf` (1 page, 451 words), and `out/l25/practice/` (key `t3l25`, runner version 2, 11 items: 5 Start here, 3 Think harder, 3 Go further; 10 templated, 4 with a picture). Source: `lessons/l25.json`. Read first: `AUDIT2_BRIEF.txt`, `AUDIT_T3_BRIEF.txt`, owner decisions (Term 2 defaults 7 and 9, the 23 Oct entries), `TERM_WIDE_AUDIT.md`, the L23 audit of this role, `website/privacy.html`, `docs/books/p1_school_paper_patterns.md` (money).

## Verdict: Ready after minor fixes

Home maths, parent page and printed layout are right, and the online practice marks every answer correctly (typed `$9`, spaces and leading zeros accepted; words refused kindly), every picture matches its question in the 100 or so variants tried, there are no network calls, no script errors and no overflow at phone or laptop width. The defects are all small: a child page that sends five text-only questions about price tags, the "Term 1 Lesson 5" label on a Term 3 sheet, no Term in the runner header, worked solutions of the generated variants that omit the numbers they are explaining, the word "dearest" in an online stem, and no rewind items online (noted in the brief). Counts: High 0, Medium 1, Low 7.

## Method

- Printed pieces rendered at 70 dpi and text extracted; all five home questions solved independently: H1 18 - 12 = 6; H2 4 + 10 = 14; H3 8 + 7 = 15 and Mei has $15, so Yes; H4 pencil case 7 and bag 13 (7 + 13 = 20, gap 6); H5 37 + 6 = 43. All match the answer page. Answers are on a separate sheet, so a double-sided print never shows them behind the questions.
- Online practice served over HTTP and driven in Playwright (Chromium) at 390 x 800 and 1280 x 800. Every tier and item opened (Start here 5, Think harder 3, Go further 3). By script: every static item answered wrong (`999`), then right; the written slips (25, 2, 33, 25, 17, 8, 26, 43) each return their own message; typed `$9`, `09`, ` 9 `, `9 dollars` are accepted; `nine` gets "Please type the answer with number digits, like 54."; both options of each choice item marked right and wrong correctly; the self-check item shows the checking steps. Then 30 "Try a similar one" rounds on each templated item (10 items): the question text was scanned for raw placeholders, "undefined", double full stops and "1 dollars"-type plurals (0 found), the picture label compared with the numbers in the question (c1 bar model labels and c2 and c3 tag labels agree in every variant), and the "answer shown" after two wrong tries compared with the arithmetic (all agree: for example c1 18 - 8 = 10, g1 34 take away 14 leaves 20, pie 10).
- Variant ranges are safe: c1 a 12 to 19, b 3 to 9 (gap 3 to 16); c3 price 11 to 19 (change 1 to 9, never zero); c5 needs 3 to 10 against a book 13 to 18; t1 dearest 40 to 48, cheapest 11 to 17; t2 uses even totals so the halves are whole; g1 total always 2p + d; t3 the yes or no uses an integer test that is correct at equality (total equals the budget gives Yes).
- Page source: `index.html` and `practice.js` hold no answers; the answers sit in `data/t3l25.json`, which any browser can fetch (shared by every lesson and runner version; noted, not blamed). External requests: none. Console errors: none. Horizontal overflow: none at either width. Keyboard: the answer box has focus on load and Enter checks.
- Rewind: the online set has no rewind item (n - 10 is lesson 15, equal groups); the home sheet's H5 is the n - 20 rewind (Term 1 Lesson 5, make a ten). Noted per the brief.
- Ordered and multi-answer marking: this lesson has no `fields`, `set` or `multi` item (its listing task, T4 of the workbook, is not online), so there is nothing to refuse in a wrong order; see finding 6.

## A. Printed pieces

| Item | Finding |
|---|---|
| Home maths | All five correct. H1 to H3 Start here (a money gap, a total, enough money), H4 Think harder (total and difference, answered by guess and check), H5 earlier practice. Plain wording, "$____" blanks, no hints in stems; H3 asks "I know because ___" as the school papers do. H1 repeats the S6 structure; H3 has an exact fit ($15 and $15) so a child who thinks "enough" needs more than the total could answer No: the answer page says "exactly $15, so she has enough" |
| Can a parent help without teaching differently? | Yes. The sheet says "use your price tags and play money", "a grown-up may read the questions aloud", "wrong answers are fine". The answers page uses class words ("count up from 12 to 18", "altogether means add", "try $7 for the pencil case") |
| Pictures | None. A lesson about price tags sends home five text-only questions; a tag or a number line would help H1 and H4 (finding 3) |
| Parent summary | One page, 451 words; "What we did" about 70 words, plain English. Words list explains costs more, how much more, altogether, change, exactly. "Please do not teach 'always take away'; counting up from the smaller price is the method" is the do-not-teach line. Beyond-P1 statement honest and specific ("Finding two prices from their total and how much more one costs (The Hidden Price), and three prices from clues, go past the school Primary 1 syllabus on purpose"); the Think harder items that are also beyond P1 (exact amounts, change from $50) are in the guide statement but not on the parent page (finding 4). No MOE-aligned, GEP or SASMO claim. Hand-off box is true: tags and money in their envelope, nothing new to cut, Book 6 in the house. The WhatsApp number and the 90-day retention appear once and agree with `privacy.html` |
| Recording statement on the parent page | One sentence: "Missed a lesson? Every lesson is recorded; your tutor will share a private link with enrolled families." It does not say what is recorded (the tutor, the shared screen and any unmuted voice) or that a parent may ask for a child to be muted, both of which `privacy.html` promises and the L11 and L12 pages said (finding 5) |
| Print layout | A4, left margin about 14 mm (the bound edge), answers on a separate page, header and footer clear. The home sheet is about 90% full; the parent page is full, two-column |

## B. Online practice

Item types: `number` (c1, c2, c3, c5, t1, t2, g1, g2), `choice` (c4, t3), `selfcheck` (g3). Tier counts and order follow the lesson: Start here compare, total, change, how much more money; Think harder the dearest minus the cheapest, a total and a gap, is a budget enough; Go further the hidden price, a $100 change story and a self-made puzzle. Wording is plain and matches the workbook. Hints name the idea, not the answer ("Count up from 8 to 17. Go to 10 first."). Wrong-answer feedback is neutral ("Not yet. Try once more.", then the hint, then "Let us look at it together" with the answer and steps on the second wrong try); no scores, timers or streaks. Typed answers: spaces, a dollar sign, a leading zero and a trailing unit are all handled; words are refused with an instruction. Two lines sit under every first wrong answer ("Not yet. Try once more." and "Not quite yet. Have another go."): redundant but harmless.

## Findings

| # | Sev | Location | Evidence | Suggested fix |
|---|---|---|---|---|
| 1 | Medium | Online t2, t3, g1, g2 worked solutions (all variants) | The generated steps omit the numbers: t2 "3 and the cup price make 10" (the cup price, 7, is never shown), t3 "12 and 11 make the total. Compare the total with $25. Enough only if the total is not more than $25." (the total, 23, is never shown), g1 "34 take away 14 leaves two equal prices" (20 never shown), g2 "38 and 24 make the total" (62 never shown). A child who gets a variant wrong is told the answer but not the working that would teach it | Add derived values (`cup`, `total`, `half`, `spent`) to each template and name them in the steps |
| 2 | Low | Online t1 stem and parent page words | "How much more does the dearest cost than the cheapest?" and "the dearer one": "dearest" is not P1 paper wording, and the workbook says "costs the most" | Use "costs the most" and "costs the least" in the online item and the parent words list |
| 3 | Low | Home sheet | Five text-only questions for a price-tag lesson; the pictures that carry the idea (tags, a number line) are absent | Add one tag picture to H1 and a strip to H4; wording unchanged |
| 4 | Low | Parent page | The beyond-P1 sentence names The Hidden Price and three prices from clues only; the guide also lists change from $50 and exact amounts | Reuse the guide's sentence in full |
| 5 | Low | Parent page | One-sentence recording statement; no "any voice that is unmuted" and no "ask us if you prefer your child muted"; `privacy.html` promises the mute route | Reuse the L11 wording |
| 6 | Low | Online set against preflight section 13 | The GC T item (which two tags cost exactly this much) and the LIST T item (three prices for $14) have no online counterpart; the only exact-amount idea online is t3 (is it enough). The runner has `set` and ordered types (used in L26) that would fit | Add a `set` item "Which two tags cost exactly $11?" with a templated pair |
| 7 | Low | Runner header | "Level 1 · Lesson 5 · Which costs more, and how much more": no "Term 3" while family pages say "Term 3 • Lesson 5" | Add the term to the sub line (runner change, backward compatible) |
| 8 | Low | Home H5 label | "Practice from earlier: Term 1 Lesson 5" is printed on a Term 3 child sheet; a child who joined at Lesson 21 has no Term 1 Lesson 5; the question is self-contained | Drop the lesson reference from the child page and keep it in the key |

Counts: High 0, Medium 1, Low 7. (c2 shows one tag, the pen, although the stem has a pen and a rubber: Low, folded into finding 3 of the printed set: show both tags.)

## What passed

Every answer in the printed and online sets is correct; picture and question agree in all variants; typed answers with a dollar sign, a leading zero or spaces are accepted; no network calls, tracking or external fonts (fonts are local); keyboard focus and tab order are sensible; the page works at 390 px with no overflow; the written slips (25, 2, 33, 17, 26, 43) catch exactly the errors listed in the key's "Watch for". Parent page: one page, plain, no overclaim, true hand-off.

## Instrument summary

| Instrument | Result |
|---|---|
| Home sheet maths | 5 / 5 correct |
| Online items | 11 / 11 correct; about 190 variants checked by script (30 rounds x 10 templates, duplicates included), 0 placeholder, plural or picture mismatches |
| Parent summary against the brief (plain English, word limit, no overclaim, beyond-P1 statement, what to say and not to say, hand-off true, privacy consistent) | 5 of 6 PASS (recording sentence thin, finding 5; beyond statement partial, finding 4) |
| Online runner (marking, kind feedback, no leaks, keyboard, pictures) | 5 of 6 PASS (variant solutions omit the working, finding 1; the answer data sit in a fetchable file shared by all lessons) |
