# Self-audit: Level 1 Term 4 Lesson 9 (Lesson 39, The Problem-Solving Toolbox)

Self-audit written by the author from the validator results of the last build. Rubric: `docs/audit/reaudit_p1.md` instruments A and tier compliance, `AUTHORING.md` checklist.

## Automatic checklist

| Criterion | Result | Evidence |
|---|---|---|
| Schema valid (JSON Schema + key checks) | PASS | schema: all top-level keys present; passes `schema/lesson.schema.json` |
| Every answer verified independently (verify/lNN_checks.py) | PASS | 214 checks: every story solved by SEARCH (every whole number tried, and exactly one answer kept: sneak-peek 2, Explore cards 1 to 8, Mini-lesson 2 to 5, S1 to S5, T1 to T4, G1 to G3, E1 to E3, home 1 to 5); strips read from their drawn lengths; tables rebuilt by adding the step row by row; the 3 pairs of coins and fruits built by taking every pair once; the line length found by trying every length (exactly one); the kit (7 tool cards, 8 problem cards, labels of at most 33 characters) checked against the kit contract; class numbers registered and shown to differ from every workbook, exit and home item |
| Online practice variants verified (expression, oracle, runner JS) | PASS | 206 template variants verified three ways |
| Timing: parts sum to 90, no part OVER, buffer, slow-class | PASS | script 69:21 of 90:00, slow-class 81:48; no part over in either model (Mini-lesson 11:53 of 12:00, Explore 10:47 of 11:00, Remember 5:53 of 6:00 in the slow class) |
| Slides and script linked (each slide once, in its part) | PASS | 34 slides each shown exactly once |
| Tier counts and completeness | PASS | Start here 6, Think harder 4, Go further 3, exit 3, home 5 |
| Neutral labels, no overclaims, no private chat | PASS | no banned labels or claims |
| Recording cues short, with child action | PASS | 11 cues, at most 26 words |
| Spare-time menu present | PASS | 3 activities (11 optional minutes, not in the 90) |
| No copied contest text | PASS | no 7-word overlap with the external sources (the first draft of the online "times as many" items overlapped a Primary 3 paper by 7 words and was reworded) |
| Mascot used modestly | PASS | Mi on 4 slides, short lines with no numbers |
| Real PDF page count and fill | PASS | workbook 6 pages (page 6 is the kit): 92, 95, 97, 98, 97 percent and 86 percent for the kit; home sheet 1 page (96 percent), home answers 1 page, parent page 1 page (96 percent), key 3 pages |
| Kit contract | PASS | 7 tool cards supplied, 7 used; 8 problem cards supplied, 8 used (Explore); kit page also printed as `L39_Kit_Pages.pdf` |
| Beyond item | PASS | Two Roads, One Answer at G1 (3 times as many with a total, a strip checked by a table of tries), named in `moe.note` and `beyond`, never at Start here |
| No template leak | PASS | checked on the built files; the next lesson is named only as "Inquirers' Showcase and Mi's Challenge Quest" |

## Judgement lines (author)

- Tier principle: PASS. Start here is six questions that each NAME their tool (strip, one step at a time, table, work backwards, find one first, list) with numbers within 100 and money in cents; nothing in it is contest-style. Think harder is where the tool is no longer named: choose among three tools for a find-one-first story (T1, the one question that asks for the tool by name), work backwards from a change (T2), draw the line (T3), and guess and check with a table of tries (T4). Go further is Two Roads, One Answer (G1, beyond Primary 1 on purpose), make three amounts equal (G2) and a growing pattern with the sentence frame "I used ___ because ___" (G3). The exit ticket asks for a tool by name once (E1, three options of which only one fits) and otherwise stays at Start here level.
- Age-appropriateness for 6 to 8: PASS with a limit. One idea: pick the tool the story needs, then check a second way. Objects first: the eight problem cards and the seven tool cards are laid on the table before any worked example, and the Mini-lesson re-teaches each tool with a picture. The limit: this is a lesson about choosing, so there is more to read than in a number lesson; the tutor reads every question aloud and Start here stems are one or two short sentences.
- Joining cold: PASS, and marked NOT safe to miss (the Quest has a gate on choosing a tool). The warm-up re-teaches strips, finding one first and working backwards, the three tools a story needs most; the seven tool names are taught in Explore.
- Safeguarding and privacy consistent: PASS. Small paper cards stay on the table and nobody cuts during the lesson; nothing is held to the camera; no private chat; made-up names and numbers only; the work-backwards movement is a slow turn of the arms and nobody walks backwards; the WhatsApp number appears only on the grown-up page; the recording sentence matches the Term 1 fix (FINAL_FIXES_T1). The tutor_prep line on printing and postage follows the owner decision of 23 Oct 2026 (included in the program fee; draft parcel policy marked owner to confirm; delivery details deleted 30 days after delivery) because the Quest Log the next lesson needs is in Book 8.
- Pictures and pages viewed at readable size: PASS with limits. All 6 workbook pages, the key (3 pages), home sheet, home answers, parent page, the kit page and all 34 slides were viewed. Changes made after viewing: the first strip in S1 and the table figures were too small and were enlarged; the Think harder choice words were cut from four to three so they fit one line; the Go further table of tries was moved into the sentence of G1(b) because the two small figures side by side were unreadable; the slide tables were enlarged; the parent page first spilled onto a second page and was shortened. The "PLAY MONEY" label under the coins in S6 is large next to the small coins (a shared-tool size choice).

## Instrument A (gifted-style, 0 to 2 each)

1 Low floor, high ceiling: 2 (a named tool at Start here to a two-road solution with 3 times as many); 2 Depth over speed: 2 (every question ends in a check); 3 Generalise: 2 (what the story gives and asks picks the tool, whatever the numbers); 4 Justify: 2 ("I used ___ because ___", the Talk question, the Explore reasons); 5 Multiple paths: 2 (the lesson is about two tools for one problem, in Explore and in G1); 6 Challenge ladder: 2; 7 Student-led inquiry: 1 (the Investigation); 8 Complexity / context: 1; 9 Problem posing: 2 (the Investigation asks the child to write a problem for a tool; spare-time menu); 10 Metacognition: 2 (choosing, naming and checking the tool); 11 Pacing / compacting: 1; 12 Extension, not acceleration: 2.

Total: 21 / 24

## Known limits

- Never trialled with children; times and difficulty are modelled. No Primary 1 paper sets "choose the tool"; the stories themselves (change, equal groups, a pattern table, a line, pairs of coins) are school-level and the tool choice, make equal and two roads are beyond the papers, so the wording is unverified.
- More than one tool can fit most problems. The workbook asks for a tool only where one tool clearly fits and the other options clearly do not (T1, E1); Explore and the Talk question take any tool with a good reason.
- The shared `tool_cards` kit prints a problem card on one line (about 33 characters fit); the problem cards therefore carry short labels and the tutor reads the whole problem aloud. A kit that wraps long text would let the cards carry the full problem (a shared-tool note for the report).
- Hand-offs: Lesson 38's `next_materials` names the 15 cards (checked by the verify script). This lesson's hand-off to Lesson 40 names the Quest Log (Book 8), a quest partner, a favourite page and plain paper, and says nothing about a Lesson 1; Lesson 40's opening statement is written to match.

## X10 change note (23 Oct 2026, night)
Re-validated and rebuilt after the Terms 3 and 4 consolidation (owner decisions RETIRE-YES, X10-BEFORE, L39-YES); see `term/l1/audit/X10_TERM34_HANDOFF.md`. The earlier audit above was written before the change and is not re-scored.
