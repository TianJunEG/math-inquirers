# Self-audit: Level 1 Term 1 Lesson 4 (The 100 Square Explorer)

Author-completed audit; the automatic table comes from `tools/audit.py` and the judgement lines are the author own. Rubric: `docs/audit/reaudit_p1.md` instruments A and tier compliance, `AUTHORING.md` checklist.

## Automatic checklist

| Criterion | Result | Evidence |
|---|---|---|
| Schema valid (JSON Schema + key checks) | PASS | schema: all top-level keys present |
| Every answer verified independently (verify/lNN_checks.py) | PASS | verify: 789 answer checks by independent script passed (term/l1/verify/l04_checks.py) |
| Online practice variants verified (expression, oracle, runner JS) | PASS | practice: 88 template variants verified three ways (expression, brute-force oracle, runner JavaScript calc) |
| Timing: parts sum to 90, no part OVER, buffer, slow-class | PASS | timing: 11 parts, contiguous, sum = 90 minutes exactly |
| Slides and script linked (each slide once, in its part) | PASS | link: 31 slides each shown exactly once, all question ids resolve |
| Tier counts and completeness (answer, hint, solution, mistakes) | PASS | tiers: counts, completeness (answer, hint, worked solution, mistakes), exit 3, home 5 |
| Neutral labels, no overclaims, no private chat | PASS | wording: no banned labels or claims in child and parent text |
| Recording cues short, with child action | PASS | rec: 11 cues, each at most 26 words, each with an action line |
| Spare-time menu present | PASS | spare: 3 spare-time activities, 11 optional minutes (not in the 90 sum), rules present |
| No copied contest text | PASS | copy: no 7-word overlap with docs/sasmo analysis/solution notes or docs/books (originals only) |
| Mascot used modestly | PASS | mascot: Mi on 4 slides, short friendly lines only |
| Workbook page fill (model) | PASS | pages: workbook page fill 98%, 91%, 96%, 89%, 101% (kit page excluded) |
| Real PDF page count and fill | PASS | outputs: Workbook PDF 6 pages, fill (measured on the PDF) 98%, 91%, 96%, 90%, 91%, 84% |
| No template leak (other lesson titles, Lesson 1 text) | PASS | template leak: no other lesson title or stray Lesson 1 text in the built files |

Timing: script 73.2 min of 90, slow-class 86.9 min. Workbook fill (model): 98%, 91%, 96%, 89%, 101%. Re-checked after the fix pass of 22 Oct 2026 (see audit/FIXES_L04.md).

## Judgement lines (author)

- Tier principle (Start here approachable and not contest-style; Think harder = taught idea in a new setting; Go further = mastery plus extension): PASS. Start here is colouring, continuing counts, filling a patch and one spot-the-mistake with no written reason (about 17 min). Think harder holds rows-down, a trail, the growing-gap sequence and 2s-and-5s overlap. Go further has sum-of-two-before (rule no longer told, found from the chain), two mixed lists and the block-diagonal claim with a second block to test.
- Age-appropriateness for 6 to 8 (reading load, one new idea, objects before symbols): PASS. Counters on the printed square come before any writing; one idea (across adds 1, down adds 10); questions are short and read aloud. Weakest: G1 to G3 are still wordy for age 6; the written reasons now sit in Think harder and Go further only (S6 and E3 are circle or one blank).
- Joining cold (Remember warm-up covers every prerequisite): PASS. Warm-up teaches 10s, 5s and 2s with hands and pairs, plus 29 then 30; the square prints every number. Stated as the safest lesson to miss.
- Safeguarding and privacy consistent between script, slides and guide: PASS. Main room only, papers to camera once, no private chat, counters not near the mouth, look-back never read out.
- Pictures and pages viewed at readable size, nothing clipped or overlapping: PASS. All 31 slides, 6 workbook pages, key, home sheet and parent page viewed. Colouring squares are unshaded and answerable. Squares on page 1 are small (about 8 mm cells); title slide Mi bubble clear after shortening the slide title.

## Instrument A (gifted-style, 0 to 2 each)

1 Low floor, high ceiling: 2. floor is counting and colouring, ceiling is the block-diagonal claim and the 3s investigation;
2 Depth over speed: 2. explore rounds and prediction questions before any rule;
3 Generalise: 2. G3 always-true claim, Investigation 3s repeat every 3 rows;
4 Justify: 2. S6, E3 and the talk question ask for reasons;
5 Multiple paths: 1. counters or colouring, but one main path;
6 Challenge ladder: 2. S, T, G ladder plus investigation with easy first step;
7 Student-led inquiry: 1. explore is hands-on but tutor-called;
8 Complexity / context: 1. calendar link only at home;
9 Problem posing: 0 on the printed workbook (independent auditor: nothing asks the child to make a pattern); 1 if the home M2 and online g4 puzzle are counted;
10 Metacognition: 2. look-back, how do you know, spot the mistake;
11 Pacing / compacting: 1. free choice of pages but lockstep deck;
12 Extension, not acceleration: 2. optional what-if square with 5 per row, no new content;

Total: 17 / 24 on the printed workbook alone (independent auditor 17; my own count after the fixes 17 to 18, because G1 now asks the child to find the rule). Not raised, to stay honest.

## Known limits

- Never trialled with children; times and difficulty are modelled. Lesson-specific: counting in 3s and growing-gap sequences go beyond Primary 1 and sit in optional or Think harder items; page 1 squares are small for colouring; the 5 per row slide is the only link to calendars.

## Fix pass, 22 Oct 2026 (independent audit WORKBOOK_AUDIT_L04.md)

Re-scored after the fixes (independent rubric items I can judge from the built PDFs): page count 6 as designed, every page 84% or more full (98, 91, 96, 90, 91, kit 84); validator 17 checks 0 WARN 0 FAIL; leak check clean; 789 answer checks. Tier compliance, strict: S6 and E3 no longer ask for a written reason (rule 25), G1 is no longer told its rule, so the three partial items of the audit are closed (13 of 16 became 16 of 16 by my reading). Opened: tutor-guide strand note and parent summary now state plainly that Term 1 goes beyond the school Primary 1 syllabus on purpose; no MOE-aligned claim anywhere.

Still open (all template or tool, not edited here): answer-part labels print "a" and "b" without brackets (rule 18 wants (a), (b)); blanks are about 14 mm and cannot be widened per lesson; the Look-back box on page 5 uses small type and wraps its tick options unevenly; the key prints "Watch for" mistakes joined as "...;" with a stray full stop; S1 and S2 100-square cells stay at 46 px because page 1 is 98% full. Never trialled with children.

## Update (second fix pass, 22 Oct 2026)

Machine state: validate 04 = 18 pass, 1 WARN (page 5 estimate 105%; the real PDF is 6 pages, fills 98, 91, 96, 90, 91, 84%), 0 FAIL; 789 answer checks, 88 practice variants; leak check clean. Script 74:03, slow class 87:46. Home 2 pages, parent 1. All pages, key, home, parent and changed slides viewed. Details in `audit/FIXES2_L04.md`.

## Update (final fix pass, 23 Oct 2026)

Fixes from `audit/FINAL_AUDIT_T1.md` are listed in `audit/FINAL_FIXES_T1.md`. Rebuilt; validator 0 FAIL. This lesson: opening recording and camera script identical to Lessons 1 to 10 (no paper held to the camera), parent summary workload line, "Harder puzzles" and "Find" wording.
