# Independent workbook audit: Level 1 Term 1 Lesson 8 (Balance and Swap)

Auditor: independent model review (desk review, no child observed). Read: `L08_Workbook.pdf` (6 pages) and `L08_Workbook_Answer_Key.pdf` (3 pages), every page rendered with pdftoppm and viewed; text extracted with pdftotext; `lessons/l08.json` for tiers, minutes, materials. Every question was solved independently and all key answers were re-computed in Python. The author's self-audit (`AUDIT_L08.md`, 19/24) was read only after the pages. Nothing was edited.

Instruments used (same as `docs/audit/reaudit_p1.md`): A = gifted-style rubric, 12 criteria x 0-2, max 24; tier compliance (strict: a "partial" counts as a violation); B = student journey, three personas x six scores 1-5, shown as the mean per persona (max 5).

## Verdict: Ready after minor fixes

Maths is correct throughout and the tiers are mostly honest. The fixes are one ambiguous question, one missing answer slot, an Investigation with no writing space, and the lack of any plate/balance picture.

| Instrument | Score |
|---|---|
| A, gifted-style rubric | 17 / 24 (author: 19). Strictly lower on criteria 2 (Start here sits at the 20-minute ceiling), 9, 12 |
| Tier compliance (14 printed S/T/G items) | 11 / 14 = 79% strict (S3, S7, G3 partial) |
| B, journey mean (LOW / MIDDLE / HIGH) | 3.2 / 3.8 / 3.7 |
| Maths | 0 wrong, 0 unanswerable; 1 ambiguous blank (S3b), 1 ambiguous Investigation step |

Instrument A by criterion: 1 low floor/high ceiling 2; 2 depth over speed 1; 3 generalise 2 (Investigation: total stays the same); 4 justify 2 (T1, talk); 5 multiple paths 1; 6 challenge ladder 2; 7 student-led 1; 8 complexity/context 1; 9 problem posing 1 (G2 open pairs only); 10 metacognition 2; 11 pacing/compacting 1; 12 extension not acceleration 1 (compensation is beyond P1; correctly held at Think harder, but S5 to S7 already lean on the same move).

Instrument B (one line each): LOW 3.2: plates and small numbers give a win in S1/S2 but S4's "Give 1 across" and S7's shift of ten are hard with no picture. MIDDLE 3.8: S1 to S6 are a good ladder; S7 and T-items need class explanation. HIGH 3.7: T2 and G1 are interesting; G3 is S6 with bigger numbers.

## A. Maths (all questions solved independently)

All keyed answers are right: S1 4,5,3,2; S2 1 more button; S3 No (blank 4); S4 6,7,8; S5 10,10,4,9; S6 5; S7 45; T1 Mei (both 65); T2 SAME, SAME, RIGHT (43/43, 73/73, 41/44); T3 25 then 75; T4 No, change 19 to 15 (unique); G1 27 and 17 (all 47); G2 first blank = second + 4 (key says also 4 and 0, correct); G3 15 and 20 (total 45); E1 4; E2 Yes; E3 2; sneak-peek 10 beads, 4. No picture/text mismatch is possible because there are no pictures (see finding 5).

## B. Syllabus fit

"=" as balance and adding within 100 are P1. Compensation (49 + 26 = 50 + 25, T3, T4) is beyond P1 (plan and `moe.note` say so) and is correctly kept to Think harder. Nothing else is beyond P1. S5 to S7 move a ten between addends (20 + 30 = 40 + []): approachable by working out the totals, so acceptable in Start here, but S7 is the nearest to the taught technique.

## C. Tier check

- S1, S2, S4, S5, S6, E1 to E3: compliant (object or arithmetic route available, no taught method needed).
- S3 (partial): asks for a written reason ("I know because") in Start here, against WORDING_GUIDE rule 25 (say-why prompts are enrichment).
- S7 (partial): the only Start here item where the move is a ten (12 to 2); closest to the Think harder technique.
- T1 to T4: taught idea in new setting; correct. T3 is the first use of give-and-take to simplify a sum.
- G1 to G3: G1 (chain of equal sums) and G2 (open pairs) are real extension. G3 (partial) is S6 with larger numbers and two children: mastery but thin extension.
- No contest-style item in Start here.

## D. Numbered findings

| # | Sev | Page / Q | Evidence | Suggested fix |
|---|---|---|---|---|
| 1 | Medium | p1 S3 (b) | Stem "Siti says 6 + 3 = 5 + 9. Check the right side." has no blank, yet (b) says "The missing number is [ ]". Which number is missing is not stated; "Check the right side" is a hint in the stem (rule 18); (c) asks a written reason in Start here (rule 25). Stem also states the wrong working (rule 19). | "Siti writes 6 + 3 = 5 + 9. (a) Is it balanced? Circle Yes or No. (b) Fill in the missing number: 6 + 3 = 5 + [ ]." Move "I know because" to Think harder or the talk. |
| 2 | Medium | p4 G2 | "Write 3 different pairs" but only one pair row (a) is printed, then "(b) I notice ___" and three lines. Answer slots for two of the three pairs are missing. | Print rows (a), (b), (c) of "___ + 5 = 9 + ___", then "(d) I notice ___." |
| 3 | Medium | p5 Investigation | No writing space at all: the child is asked to "write what you did to the numbers", try two numbers with three changes and say "by how much", with no lines, boxes or table. (Author lists "one line" as a known limit; there is none.) | Add a small table (start numbers / change / new total) or 4 lines; or say "Use your spare paper". |
| 4 | Medium | p5 Investigation, first step | "Add: 6 + 4, then 7 + 3, then 7 + 5. Which total is not 10? Write what you did to the numbers." The totals are 10, 10, 12 so "which is not 10" is clear (7 + 5), but "what you did to the numbers" has no referent (nothing was done), and the answer key gives no answer for this first step. | "(a) Which total is not 10? (b) From 6 + 4 to 7 + 3, one number goes up 1. What does the other do?" Add both answers to the key. |
| 5 | Medium | whole workbook | The lesson model is two plates (LEFT/RIGHT), but no page prints a plate or balance. S2 says "left plate" with nothing drawn; a child at home or a child who forgot the class model sees only symbols. | Print two plate outlines with the left plate already filled in S2; add a small picture to S1 and S4. |
| 6 | Low | p2 S4 | "Give 1 across from the 7 to the 5" is teaching inside the question (rule 24) and "across" is unexplained jargon; (a) to (c) repeat the move. | "7 + 5 = 12. Fill in the missing numbers." with counters 7 and 5 and a one-word label, "Move 1."; or drop the instruction and keep the pattern. |
| 7 | Low | p2 S7, p3 T3/T4, p4 G1/G2/G3 | The same job (one missing number) uses a clear 36 px box in S1, S4, S5, E1, E3 and a dashed line in S7, T3, T4, G1, G2 (rule 16: box for one missing number, line for words/units). S7 also has a spare answer line. | Use the box everywhere a single number is missing; keep the line for "stickers" etc. |
| 8 | Low | p1 S3a, p2 S6, p3 T1, T4a, p5 E2 | "Circle Yes or No" / "Circle Mei or Ali" prints no choice shapes. The end-of-term check prints oval Yes/No buttons, so the style differs inside the same term. | Print oval Yes / No (and Mei / Ali) buttons as in L10 check Q7b. |
| 9 | Low | p3 intro | "Use your plates, draw a picture, or look at how the numbers moved." The last clause is a method hint (rules 18, 24) given before any question; it names the technique the page tests. | "Use your plates or draw a picture. Then write how you know." |
| 10 | Low | p4 G3 | Same structure as S6 with bigger numbers and two children; only a second target and the 45 total are new. | Add a third child, or ask "Who has the most in the pocket?", or reverse the unknown (give the pocket, ask the page). |
| 11 | Low | p6 kit page | Tens bars and ones squares are printed as an "optional help" but no printed question refers to them, while the lesson model (plates) has no kit. A grown-up cuts a full page for optional use. | Replace by a plates kit (two plate outlines marked LEFT and RIGHT, 20 counters) or state which questions use bars. |
| 12 | Low | all workbooks, p1 corner | Mi holds what looks like a calculator; AUTHORING.md says never show or rely on the calculator. Asset-level, shared by every lesson. | Owner to confirm the asset; no change to this lesson. |
| 13 | Low | p2, p4 | Both pages end about 12 to 25% empty (p4). Acceptable, but the validator target is 85%. | Use the space for findings 2, 3 and 5. |

## E. Layout and usability (6-year-old)

Fonts, contrast and the box/line sizes are good; drawing box in S2 is large; nothing is cut off; every page starts with a clear instruction line; the page-1 corner mascot does not take writing space; kit page is printable (cut-out grid fits one page). Problems: findings 2, 3, 5, 7, 8.

## F. Pedagogy

Progression S1 to S6 is sound (swap, move one, move tens, story, check a claim). Start here is modelled at 19.5 minutes of a 28-minute workbook part, at the ceiling for a middle child with the choice-after-3 instruction: fine, but there is no slack for a slow writer. Think harder vs Go further differ properly (reasoning without adding vs chains and open pairs). The exit ticket (E1 to E3) matches the objective exactly. Misconceptions are targeted in the key ("Watch for": writing the total, moving both numbers the same way).

## G. Safeguarding and inclusion

No labels such as gifted/weak; "Start here / Think harder / Go further" only; look-back says "no right answers, you can pass, nobody reads it out"; names Mei, Siti, Ben, Ali, Ravi are mixed and consistent; no ranking. Pass.

## H. Consistency with other lessons

Command words match L09 and L10 ("Fill in the missing numbers", "Circle"). Box/blank style is inconsistent inside the lesson (finding 7) and Yes/No style differs from the check (finding 8). Mascot use matches (page 1 corner only).
