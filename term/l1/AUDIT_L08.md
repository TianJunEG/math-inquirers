# Self-audit: Level 1 Term 1 Lesson 8 (Balance and Swap)

Self-audit by the author (a model); no child has used this lesson. Table generated from the validator; judgements written after viewing every page and slide.

## Automatic checklist

| Criterion | Result | Evidence |
|---|---|---|
| Schema valid (JSON Schema + key checks) | PASS | schema: all top-level keys present |
| Every answer verified independently (verify/lNN_checks.py) | PASS | verify: 2612 answer checks by independent script passed (term/l1/verify/l08_checks.py) |
| Online practice variants verified (expression, oracle, runner JS) | PASS | practice: 324 template variants verified three ways (expression, brute-force oracle, runner JavaScript calc) |
| Timing: parts sum to 90, no part OVER, buffer, slow-class | PASS | timing: 11 parts, contiguous, sum = 90 minutes exactly |
| Slides and script linked (each slide once, in its part) | PASS | link: 29 slides each shown exactly once, all question ids resolve |
| Tier counts and completeness (answer, hint, solution, mistakes) | PASS | tiers: counts, completeness (answer, hint, worked solution, mistakes), exit 3, home 5 |
| Neutral labels, no overclaims, no private chat | PASS | wording: no banned labels or claims in child and parent text |
| Recording cues short, with child action | PASS | rec: 11 cues, each at most 26 words, each with an action line |
| Spare-time menu present | PASS | spare: 3 spare-time activities, 11 optional minutes (not in the 90 sum), rules present |
| No copied contest text | PASS | copy: no 7-word overlap with docs/sasmo analysis/solution notes or docs/books (originals only) |
| Mascot used modestly | PASS | mascot: Mi on 4 slides, short friendly lines only |
| Workbook page fill (model) | PASS | pages: workbook page fill 92%, 90%, 84%, 86%, 100% (kit page excluded) |
| Real PDF page count and fill | PASS | outputs: Workbook PDF 6 pages, fill (measured on the PDF) 92%, 90%, 84%, 86%, 100%, 91% |
| No template leak (other lesson titles, Lesson 1 text) | PASS | template leak: no other lesson title or stray Lesson 1 text in the built files |

Timing: script 72.4 min of 90, slow-class 85.7 min. Workbook fill (model): 92%, 90%, 84%, 86%, 100%. Home sheet 2 pages, parent page 1 page. Re-audited after the fix pass of 22 Oct 2026 (see audit/FIXES_L08.md); the independent audit (audit/WORKBOOK_AUDIT_L08.md) scored 17/24 before the fixes.

## Judgement lines (author)

- Tier principle: PASS after fix pass. Start here no longer asks for a written reason (S3 now Yes/No plus a missing number, rule 25). Start here is plates-and-blanks work with small numbers and tens (S5 and S7 go beyond the school Primary 1 range on purpose, per the owner decision of 22 Oct 2026; both are approachable by finding the total or moving a tens bar); spotting equal sums without adding and compensation (49 + 26 = 50 + 25) are at Think harder only; Go further has a two-blank chain, a pairs puzzle and a stickers story.
- Age-appropriateness: PASS with caveat. One idea (give and take), objects first, all questions read aloud. The Think harder items T2 and T4 and the G2 pairs puzzle are the hardest for a 6-year-old reader.
- Joining cold: PASS. The warm-up re-teaches bonds to 10 and 20 and the meaning of =; no carrying is needed; no earlier Term 1 lesson is assumed.
- Safeguarding: PASS. Main room only, papers to the camera once, no private chat, look-back never collected; checked in script, slides and guide.
- Pictures and pages: PASS. Every workbook, key, home and parent page and every slide viewed; no overflow, Mi does not overlap text. Slides are sparse (lower third empty) as in the pilot.

## Instrument A (gifted-style, 0 to 2 each)

1 Low floor, high ceiling: 2, plates and small numbers to Go further chain;
2 Depth over speed: 2, how do you know and talk question, no speed;
3 Generalise: 2, Investigation: when the total stays the same;
4 Justify: 2, Think harder T1, T4 and talk ask for reasons;
5 Multiple paths: 1, plates, counting or moving numbers;
6 Challenge ladder: 2, S, T, G ladder with easier links online;
7 Student-led inquiry: 1, hands-on rounds but tutor-led;
8 Complexity / context: 1, two stories only;
9 Problem posing: 1, spare menu and online g4 only;
10 Metacognition: 2, look-back and exit;
11 Pacing / compacting: 1, choice after page 1, lockstep deck;
12 Extension, not acceleration: 2, optional what-do-you-notice, depth not speed;

Re-score after fixes (independent rubric, strict): 1 low floor/high ceiling 2; 2 depth over speed 1 (Start here is now about 19 minutes modelled, S3 reason removed, still near the ceiling); 3 generalise 2; 4 justify 2; 5 multiple paths 1; 6 challenge ladder 2; 7 student-led 1; 8 context 1; 9 problem posing 1 (G2 still open pairs only); 10 metacognition 2; 11 pacing 1; 12 extension not acceleration 1 (G3 now has a reversed unknown, Kumar, so it is more than S6 with bigger numbers).

Total: 17 / 24 (independent auditor, before fixes) -> 18 / 24 (author re-score; the auditor has not re-run). Tier compliance: S3 (written reason) and G3 (thin) fixed; S7 stays a boundary case, kept in Start here on purpose with a hint that offers two routes. Estimated 13/14 strict, S7 partial.

## Known limits

- Never trialled with children; times and difficulty are modelled.
- Compensation is beyond Primary 1 and its placement at Think harder needs owner or tutor confirmation.
- Blanks are boxes (single numbers) or lines (words), never letters. Investigation has 4 ruled lines on page 5.
- Open: no plate or balance picture exists in the shared figure tools (template gap, audit finding 5); S2 still asks the child to draw the right plate with no left plate printed. Needs a new figure type in tools/svg.py (owner or template owner).
- Open: the kit page is still tens bars and ones squares; its intro now says it helps S5 and S7 and that the plates are real plates. A plates kit would need a template change.
- Open: the Mi mascot on page 1 appears to hold a calculator (shared asset, finding 12).
- Term 1 goes beyond the school Primary 1 syllabus on purpose (owner decision, 22 Oct 2026): said plainly in the tutor guide strand note and the parent summary; no MOE-aligned claim anywhere.

## Second fix pass, 22 Oct 2026

Changes are listed in `audit/FIXES2_L08.md`. Re-checked: validator 0 FAIL; 2612 answer checks; 324 practice variants; ordered marking on online item g1 tested in a browser (right order accepted, swapped order refused with a clear message); slow-class script 87:50 (workbook overrun covered by the flex buffer and stated in the guide); workbook fill 92, 90, 84, 86, 94%; parent page one page. Start here S5 now stays with whole tens; compensation is only at Think harder. No paper is held up to the camera. No child has used the lesson; times are modelled.
