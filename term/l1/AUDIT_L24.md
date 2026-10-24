# Self-audit: Level 1 Term 3 Lesson 4 (Dollars and Change)

Table from the final validator run (`python3 term/l1/tools/validate.py 24`, built files included); judgement lines written by the author after viewing the outputs. Rubric: `docs/audit/reaudit_p1.md` instruments A and tier compliance, `AUTHORING.md` checklist.

## Automatic checklist

| Criterion | Result | Evidence |
|---|---|---|
| Schema valid | PASS | schema: all keys present, passes `lesson.schema.json` |
| Every answer verified independently | PASS | verify: 187 checks (money in whole cents; ways and fewest-pieces by brute force and dynamic programming; kit pages read back from the kit builder) |
| Online practice variants verified | PASS | 63 template variants verified three ways |
| Timing | PASS | 2+6+4+11+11+4+32+6+6+3+5 = 90; scripted 68:12, slow-class 80:44; no part OVER (mini 10:53 of 11:00 slow-class) |
| Slides and script linked | PASS | 28 slides each shown once |
| Tier counts and completeness | PASS | Start here 6, Think harder 4, Go further 3, exit 3, home 5 |
| Neutral labels, no overclaims, no private chat | PASS | no banned wording |
| Recording cues | PASS | 11 cues, at most 26 words |
| Spare-time menu | PASS | 3 activities, 11 optional minutes |
| No copied text | PASS | no 7-word overlap (a Set A / Set C phrase from the P1 paper notes was reworded) |
| Mascot | PASS | Mi on 4 slides |
| Beyond item | PASS | Fewest Notes and Coins at G1, G2 |
| Kit contract and hand-off | PASS | 16 coins + 13 notes printed and counted from the kit builder; supplied covers the most any task uses; $1 coins are the 30 Term 2 tokens; `next_materials` names the 12 price tags, the money and the tokens |
| Real PDF page count and fill | PASS with warning | Workbook 5 pages + 2 kit pages: 100%, 96%, 88%, 96%, 99%; kit pages 49% and 47% (short by design, a kit page is not held to the fill rule); home 1 page, parent 1 page |
| Template leak | PASS | none |

Validator: 0 FAIL, 2 WARN (the two kit pages are short).

## Judgement lines (author)

- Tier principle: PASS. Start here (6, about 17 modelled minutes): count coins within 100 cents and notes within $30, swap a coin for coins, circle coins for 55 cents, which is worth more ($2 note or $1 coin), change from $5 by counting up; all Primary 1 and stated so. Think harder (4): two things and change from $10, a $1 coin and change in cents ($1 = 100 cents, the one allowed mix), every way to make 50 cents with 10 and 20 cent coins (listing puzzle, 3 ways), sets A to C (more coins is not more money). Go further (3) is beyond Primary 1 on purpose: fewest notes and coins for $73 and for $13 change, how many amounts three pieces make (7), a small shop. The beyond item is named and said plainly to families.
- Age-appropriateness: PASS. One idea (value, biggest first, count up for change); Explore is 11 minutes with play money before any written work; the tutor reads every question; no decimal money, no 50c, no mixed amounts.
- Joining cold: PASS. Warm-up counts in 5s and 10s, orders four coins, counts up on a line. `safe_to_miss` false (the next two lessons and the Quest use the money).
- Safeguarding and privacy: PASS. Main room only, no paper to the camera, tick your own work, WhatsApp route only on the parent page, play money small-parts line, real coins only with a grown-up, no cutting in the lesson, seated option in the hop break. The wrong claim in Talk time is "a child".
- Pictures and pages: PASS with limits. Viewed workbook pages 1 to 5 and the kit pages, deck contact sheets, home and parent pages. Fixes while viewing: a single coin or note printed as large as the page (sizes set), page 3 and page 5 spilled (tags and some pictures dropped, labels shortened), one Mini slide overflowed (fixed).

## Instrument A (0 to 2 each)

1 Low floor, high ceiling: 2 (count four coins; fewest pieces for $73). 2 Depth over speed: 2 (Explore 11 minutes with real pieces). 3 Generalise: 1 (more coins is not more money, in T4 and the menu). 4 Justify: 2 (sneak "I know because", Talk, T4). 5 Multiple paths: 2 (count on, count up on a line, swap coins). 6 Challenge ladder: 2. 7 Student-led inquiry: 1. 8 Complexity / context: 1. 9 Problem posing: 1 (M2, online g3). 10 Metacognition: 1. 11 Pacing: 1. 12 Extension, not acceleration: 2.

Total: 18 / 24

## Known limits

- Never trialled with children; times are modelled.
- Heaviest cutting of the term (29 pieces on 2 pages); the hand-off from Lesson 3 asks for a week's notice. If the Term 2 tokens are lost, 5 counters stand in.
- Single-piece pictures are scaled small in print and the slide question rows show workbook thumbnails; the READ lines state every amount. A template change (cap a money figure's width by piece count) would remove the manual sizes.
- The play money is stylised and marked PLAY MONEY; the rules on reproducing real notes and coins have not been checked (decision D1).
- Quest gate 3 (50c, 20c, 20c, 5c; $7 toy paid with $10) is avoided in all class and workbook numbers, checked in verify. Its "50c" should read 50¢ on child pages.
- Online practice has no rewind items (the runner cannot assemble them yet); g1 has no picture; the 12-tag hand-off to Lesson 25 depends on that author's kit.

## Fix pass (Term 3, 23 Oct 2026)

After the three independent audits (`audit/WORKBOOK_AUDIT_L24.md`, `GUIDE_DECK_AUDIT_L24.md`, `HOME_PARENT_PRACTICE_AUDIT_L24.md`) the Medium findings that sit in lesson data were fixed; see `audit/FIXES_T3_L24.md`. What changed in the scores: the missing non-routine type (work backwards, paid and change given, find the price) is now Think harder T3, and `contest_moves` and `moe.note` name it; the answer to "how many ten-cent coins make a dollar" is no longer on the slide while it is asked (`reveal`); the optional slide no longer pictures the 4-coin answer; the S3 task no longer implies ten 5-cent coins that the kit does not hold; the opening, camera and microphone wording follow the final Term 1 text; the online t3 is a one-number item. Validator 0 FAIL (29 pass, 2 WARN: the two kit pages are short by design); script 68:12, slow class 80:44, mini 10:53 of 11:00. Still open and not in lesson data: kit piece size and cut-line gaps, one coin scale across figures (`FINAL_FIXES_T3.md`, shared tools); the owner decision on play-money reproduction (D1).
