# Independent workbook audit: Level 1 Term 1 Lesson 6, Tens Jump, Ones Hop

Auditor: independent desk review (a model), no child observed. Files read: `out/l06/L06_Workbook.pdf` (6 pages, every page rendered with pdftoppm and viewed), `L06_Workbook_Answer_Key.pdf` (3 pages, all viewed), `lessons/l06.json` (tiers, exit, sneak-peek, timing, materials), the author self-audit `AUDIT_L06.md`, the guides and project instruments listed in `AUDIT_BRIEF.txt`. Nothing was edited.

## Verdict: Ready after minor fixes

No wrong maths, no unanswerable item, no safeguarding problem. Four Medium issues (a missing writing space, an exit ticket item beyond P1, a drawing task with no number line, a Go further tier that is mostly Think harder).

## Instruments and scores

- Instrument A, gifted-style rubric (`docs/gifted_research.md` section 2, as used in `docs/audit/reaudit_p1.md` 1A): 12 criteria x 0-2, **max 24**. Scored on what a child holds in the printed workbook (the author's 20/24 counts tutor-script and online features too). Score **14/24**: 1 low floor/high ceiling 2; 2 depth 1; 3 generalise 2 (T3, Investigation); 4 justify 1 (only S6 and T3c ask why; the Investigation has no space); 5 multiple paths 1; 6 ladder 1; 7 inquiry 1; 8 context 1; 9 problem posing 0 (no make-up item in the workbook); 10 metacognition 2 (printed look-back); 11 compacting 1 (one choice line); 12 extension not acceleration 1 (2-digit +/- 2-digit is next-year content, correctly kept in Think harder).
- Tier-compliance check (reaudit 1A definition: Start here approachable untaught, Think harder = taught idea in a new setting, Go further = mastery + extension): Start 7/7 compliant (S3, S4 need the lesson words "jump/hop"; the Remember warm-up covers them), Think 4/4, Go 1/3 (G1 and G3 are Think-level). **12/14 = 86%**, against the author's claimed 100%.
- Instrument B (student journey, personas) not used: it needs the live slides and script; this audit is of the printed workbook and key.
- AUTHORING rubric points 12, 14, 16 spot-checked from the PDFs (see findings).

## A. Maths correctness
All 14 questions, the 3 exit questions and the Investigation were solved independently: S1 36; S2 54; S3 33, 63, 81, 67; S4 24, 38, 55, 69; S5 38; S6 wrong, 65, tens; S7 56; T1 59; T2 44; T3 46, 46, yes; T4 48; G1 9 jumps; G2 5 jumps (four of 20 + one of 10; 4 jumps reach at most 87); G3 25, 55, 45, 65, 69; E 76, 44 and 71, 59. All match the key. Pictures match text (S1 shows 2 bundles and 6 singles = 26). No ambiguity found except Investigation wording (finding 9).

## B. Syllabus fit (MOE P1: 2-digit plus ones without renaming, 2-digit plus tens, within 100)
Start here S1 to S7 are inside P1. T1 (34 + 25), T2 (68 - 24), G3 are 2-digit +/- 2-digit: beyond P1, correctly at Think harder / Go further. **E3 (31 + 28) is the same beyond-P1 skill in the exit ticket** (finding 2).

## Findings

| # | Sev | Page / Q | Evidence | Suggested fix |
|---|---|---|---|---|
| 1 | Medium | p5 Investigation "Jump road" | The page prints "Write every number you land on", "Write what you notice", yet there is **no writing line or box at all**. The builder auto-fits the Investigation lines after the exit ticket and look-back and chose 0 (`b_print.page_fill`, `_inv_lines`). The author's note says "one line"; the PDF has none. A child cannot record the task. | Give the Investigation 4 lines (shrink the look-back or move the exit ticket to its own half page), or make the builder fail when `_inv_lines` is 0. |
| 2 | Medium | p5 E3 "31 + 28" | 2-digit + 2-digit is beyond P1 and is the lesson's Think harder skill (T1). WORDING_GUIDE rule 25 keeps such items out of exit tickets. A child who only mastered Start here cannot show it. Key itself lists "Writing 39" as a common mistake. | Replace with a Start-level split (e.g. 52 + 7 or 36 + 20 + 3 as one hop and one jump) and keep 31 + 28 as a spare Think harder item. |
| 3 | Medium | p3 T1, T2 | "Show your jumps and hops on the lines" gives only 2 dotted writing lines. S7 gives a drawing box for a number line; T1/T2 give nothing to draw on, and the page hint says "make a table". A 6-year-old has no start dot or line to hang arcs on, so most will write only the answer. | Print a blank number line strip (or a start dot) in each box, or change the command to "Write each jump and hop" with a frame (34 + __ = __, then __ + __ = __). |
| 4 | Medium | p4 G1, G3 | G1 (count in tens 7 to 97, 9 numbers) uses the holiday skill of counting in tens and is easier than T1, T2. G3 is four one-step moves with a written list: Think-level. Only G2 (fewest jumps, with a "why 4 is not enough" argument) meets "mastery + extension". Go further is not really different from Think harder. | Swap G1 for an open item ("Make a jump route from 7 to 97 using 10s and 20s. Find two different routes") and make G3 end with an unknown move ("You land on 69. What was the last hop?"). |
| 5 | Low | p2 S6 (c) | "Siti added 2 ones. She should add 2 ___." states the error and leaves only the word "tens", so (a) and (c) give the answer away (rule 4, 19, 24). Also "Circle Right or Wrong" has no printed options and rule 19 uses Yes/No (L07 S6 uses Yes/No: inconsistent across lessons). | Make (c) "Siti added 2 ___ . She should add 2 ___." or drop it; use "Is Siti correct? Circle Yes or No." |
| 6 | Low | p1 S1 vs sneak-peek | Sneak-peek Q1 (key p3) is the same item as S1 (Mei's sticks plus one bundle, 36). | Change the numbers in one of them. |
| 7 | Low | p1 S1, S5; kit p6 | Three tens-pictures: stick bundles (S1, S2), boxes of 10 pencils (S5), bars (kit, hints "think of the tens as bars"). Children must switch model with no link. | Use bars and squares in S1 as L07 does, or add one line linking bundle = bar. |
| 8 | Low | commands | "Fill in a to c" / "Fill in a and b" where (a) is a circle or a list (S6, G1 to G3) and not blanks; S4 "Jump or hop." is not a command; page 2 and page 4 start with no instruction line (p2 has none). Guide rule 14 wants "Fill in the blanks." and a clear first instruction on each page. | Use "Fill in the blanks." only when all parts are blanks; give p2 a one-line instruction ("Jump or hop: use bars, your kit or a drawing"). |
| 9 | Low | p5 Investigation | "Which start numbers can land on 50?" is open on range: 50 itself and 0 count; key lists only 0, 10, 20, 30, 40. Also 2 tasks plus a long stem (about 45 words) before writing. | Say "Start numbers from 0 to 50" and key "0, 10, 20, 30, 40, 50". |
| 10 | Low | p3 T3; p4 G3, p1 S2 | Four fact sentences before the command (T3, 29 words), five commands in a row (G3, 26 words), S2 25 words; rule 1 says at most three short sentences. Tutor reads aloud, but children read ahead. | Split T3 into Frog A / Frog B lines; show G3's moves as a list. |
| 11 | Low | p3 header | Page-3 intro "Use objects, draw a picture or make a table. Then write how you know." is the generic default: no table is relevant and only T3 asks for a reason. | Set `hint_p3` for this lesson (as L07 does). |
| 12 | Low | p5 look-back | Look-back print is about 7 pt with small checkboxes; "I am still stuck" sits under "Next time I will try". Hard for a 6-year-old to read alone. | Enlarge to at least 9 pt and move "I am still stuck / I would like to pass" to a line of their own. |
| 13 | Low | p1 corner (all lessons) | Mi holds a calculator, but AUTHORING says the program does not show or rely on the calculator, and this lesson teaches mental calculation. The image is owner-chosen, so report only. | Crop or tell the owner; low priority. |
| 14 | Low | Key p2-3 | "Investigation (page 5): Jump road" heading is the last line of key p2; its answer starts p3. | Keep heading with its box. |
| 15 | Low | cast (H) | Siti is the child who makes the mistake in L06 S6, L07 S6 and L08 S3. Repeated, it becomes a pattern. | Rotate the name (Ben, Ravi, Mei). |

## C/F. Tier and pedagogy notes
- Start here is a good ladder: concrete (S1, S2), symbolic jump (S3, S4), story (S5), error (S6), draw (S7). Sum of `mins` 19, inside the 28-minute workbook slot with page 3 available.
- Think harder is new setting and fair (T3 order does not matter is a good idea). T1/T2 are the lesson's own worked examples; honestly "Think" because 2-digit + 2-digit is new.
- Exit ticket matches objectives 1 to 3, not 4 (drawing); acceptable. Misconceptions are well targeted (ones vs tens, hopping the wrong way).
- No problem posing in the workbook; Go further has nothing for a child who finishes G1 to G3 quickly except the Investigation without space.

## D. Wording against the guide
Mostly good: command first, (a)/(b), Singapore English, no brands. Remaining items: findings 5, 8, 10, 11. Answer frames end with a noun/unit and a full stop (rule 16 satisfied).

## E. Layout
Pages 1 to 4 are clean: 8 mm answer lines, large type, boxes 22 to 27 mm high (S2 asks for 5 bundles and 4 singles in a box about 22 mm tall: tight). Pages 3, 4 end about 8% blank, fine. Page 5 is crowded (finding 1, 12). Kit page printable: 9 bars and 20 squares, cell about 15 mm, clear dashed cut lines; instruction text small. The kit has 9 bars, enough for 97 and all Start items.

## G/H. Safeguarding, inclusion, consistency
No ranking, no ability labels (Start here / Think harder / Go further only), look-back says "Nobody reads it out" and allows a pass; exit "on your own". Consistent with L07 on boxes, blanks and frames. Finding 15 for cast; finding 13 for mascot.
