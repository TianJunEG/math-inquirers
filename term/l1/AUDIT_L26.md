# Self-audit: Level 1 Term 3 Lesson 6 (The School Shop)

Table from the validator results of the final build (`python3 term/l1/tools/validate.py 26`, built files included); judgement lines written by the author after viewing every output. Rubric: `docs/audit/reaudit_p1.md` instruments A and tier compliance, `AUTHORING.md` checklist.

## Automatic checklist

| Criterion | Result | Evidence |
|---|---|---|
| Schema valid (JSON Schema + key checks) | PASS | schema: all top-level keys present; passes `schema/lesson.schema.json` |
| Every answer verified independently (verify/lNN_checks.py) | PASS | 242 checks: totals and change recounted one dollar at a time; every "exactly" and "ways" claim listed by brute force over all counts of each item (2 pairs for $12, 2 ways for $10, $12, $16, $18 and for pens and books, 6 ways for $20 with three notes, 1 way for 7 things, $1 and $3 not payable); class items kept apart from workbook items, the Quest gate and the Quest cave idea |
| Online practice variants verified (expression, oracle, runner JS) | PASS | 202 template variants verified three ways |
| Timing: parts sum to 90, no part OVER, buffer, slow-class | PASS | 2+6+4+11+11+4+32+6+6+3+5 = 90; scripted need 65:32, slow-class 77:25, no part OVER in either model |
| Slides and script linked | PASS | 34 slides each shown exactly once; answers on their own slides |
| Tier counts and completeness | PASS | Start here 6, Think harder 4, Go further 3, exit 3, home 5 |
| Neutral labels, no overclaims, no private chat | PASS | wording check clean |
| Recording cues short, with child action | PASS | 11 cues |
| Spare-time menu present | PASS | 3 activities, 11 optional minutes |
| No copied contest text | PASS | no 7-word overlap |
| Mascot used modestly | PASS | 4 slides, no numbers |
| Beyond item named and not at Start here | PASS | Exactly $20 at T1 and G1 |
| Kit contract and hand-off | PASS | no new kit page; most tags at once 6 (Explore), $2 notes 5 of 5, $5 notes 2 of 4; Lesson 25 hands off the tags and money with nothing new to cut; this lesson's `next_materials` names the 16 grid tiles (matches Lesson 27's kit) |
| Real PDF page count and fill | PASS | Workbook 5 pages, fill 95%, 96%, 94%, 89%, 95%; home sheet 1 page, answers 1, parent page 1 (99%) |
| No template leak | PASS | none |

Validator: 0 FAIL, 0 WARN.

## Judgement lines (author)

- Tier principle: PASS. Start here (6, about 18 modelled minutes, money within $20): which two of four tags cost exactly $10 (the Primary 1 "which two items" form), a total, money left, is $10 enough and how much more, the cost of 3 equal items, a had-spent-left table. Think harder (4): every way to spend exactly $20 on pens and books with a table by number of books, is a list complete, three items and change from $50, true or false on ways. Go further (3) is beyond Primary 1 on purpose: every way to pay $20 with three kinds of note (6 ways), 7 things for an exact total, writing an exactly-puzzle. Beyond item "Exactly $20" is named in `moe.note`, `beyond`, guide, parent page and tutor prep.
- Age-appropriateness: PASS. One idea (a plan that fits, listed in order). Explore is hands-on with tags and notes; the listing method is shown (cheapest first, biggest note first) before any written table. Every question is read aloud. Whole dollars, no $20 note.
- Joining cold: PASS. Warm-up makes 10 on a ten-frame, adds three equal prices, lists pairs in order. `safe_to_miss` true with a Quest-gate caveat.
- Safeguarding and privacy: PASS. Main room, nothing held to the camera, tick-your-own-work, WhatsApp route only on the parent page; the wrong claim in Talk belongs to "one child" and "another child"; seated option in the clap-and-stamp break.
- Pictures and pages: PASS. Viewed all 5 workbook pages, key, home sheet, parent page and the slides. Fixes while viewing: parent page spilled (text trimmed), mini and remember over the slow-class limit (examples and waits trimmed), tag sizes lowered so slides do not overflow.

## Instrument A (0 to 2 each)

1 Low floor, high ceiling: 2. Two tags for $10 at the floor; every way with three kinds of note at the ceiling.
2 Depth over speed: 2. Explore finds the pairs by hand before any method is named.
3 Generalise: 2. "Go in order and check what is left" is used for tags, for notes and for pens and books.
4 Justify: 2. "How do you know you have them all", Talk on same way in a different order, is the list complete.
5 Multiple paths: 1. Tags, notes, a table, counting up.
6 Challenge ladder: 2. Start here, Think harder, Go further, Investigation, optional slide, menu.
7 Student-led inquiry: 1. Children find the pairs and ways; the table is modelled.
8 Complexity / context: 1. Shop contexts only.
9 Problem posing: 2. G3 and spare-time M2 and online g3 ask for a puzzle for a partner.
10 Metacognition: 1. Check by adding, tick own work, look-back.
11 Pacing / compacting: 1. Choice page after Start here.
12 Extension, not acceleration: 2. Same idea deepened; nothing the next lesson needs is taught.

Total: 19 / 24

## Known limits

- Never trialled with children; times and difficulty are modelled. Mini-lesson slow-class need is 10:47 of 11:00 (tightest part): cut the total-then-change example first (skip order).
- Wording unverified against a Primary 1 paper: all-ways and true or false on ways (T1, T4, G1), 7 things (G2). The "which two items" form is school level.
- The Quest cave idea in the pre-flight ($14 with $2 and $5 notes) is kept out of this lesson on purpose; if the Quest author changes the cave this lesson is unaffected.
- A way that needs six or ten $2 notes cannot be laid out with the 5 two-dollar notes of the kit: the lesson says to write it (guide, slide notes).
- Page 3 and 4 tables use many answer boxes (G1 has 15); the boxes are 36 px and fit, but a small child may need the grown-up to rule the table on spare paper.
