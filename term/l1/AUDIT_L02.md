# Self-audit: Level 1 Term 1 Lesson 2 (Number Words and the Number Line)

Desk audit by the author (a model); no child has used this lesson. The table below is generated from the validator of the last build. Rubric: `docs/audit/reaudit_p1.md` instruments A and tier compliance, `AUTHORING.md` checklist.

## Automatic checklist

| Criterion | Result | Evidence |
|---|---|---|
| Schema valid (JSON Schema + key checks) | PASS | schema: all top-level keys present |
| Every answer verified independently (verify/lNN_checks.py) | PASS | verify: 448 answer checks by independent script passed (term/l1/verify/l02_checks.py) |
| Online practice variants verified (expression, oracle, runner JS) | PASS | practice: 166 template variants verified three ways (expression, brute-force oracle, runner JavaScript calc) |
| Timing: parts sum to 90, no part OVER, buffer, slow-class | PASS | timing: 11 parts, contiguous, sum = 90 minutes exactly |
| Slides and script linked (each slide once, in its part) | PASS | link: 30 slides each shown exactly once, all question ids resolve |
| Tier counts and completeness (answer, hint, solution, mistakes) | PASS | tiers: counts, completeness (answer, hint, worked solution, mistakes), exit 3, home 5 |
| Neutral labels, no overclaims, no private chat | PASS | wording: no banned labels or claims in child and parent text |
| Recording cues short, with child action | PASS | rec: 11 cues, each at most 26 words, each with an action line |
| Spare-time menu present | PASS | spare: 3 spare-time activities, 11 optional minutes (not in the 90 sum), rules present |
| No copied contest text | PASS | copy: no 7-word overlap with docs/sasmo analysis/solution notes or docs/books (originals only) |
| Mascot used modestly | PASS | mascot: Mi on 4 slides, short friendly lines only |
| Workbook page fill (model) | PASS | pages: workbook page fill 88%, 95%, 87%, 86%, 95% (kit page excluded) |
| Real PDF page count and fill | PASS | outputs: Workbook PDF 7 pages, fill (measured on the PDF) 88%, 96%, 87%, 86%, 95%, 82%, 83% |
| No template leak (other lesson titles, Lesson 1 text) | PASS | template leak: no other lesson title or stray Lesson 1 text in the built files |

Timing: script 74.7 min of 90, slow-class 88.6 min. Workbook fill (model): 88%, 95%, 87%, 86%, 95%. Validator after the fix pass: 17 pass, 0 warn, 0 FAIL.

## Judgement lines (author)

- Tier principle: PASS. Start here is counting, one before/after, reading words, tens marks (8 questions, 19 min). Think harder holds nearer ten (beyond Primary 1, informal), numbers between two marks, a halfway clue puzzle and reaching 100. Go further holds missing marks, two frogs meeting, make-your-own line.
- Age-appropriateness: PASS with caveat. One idea (every number has a spot and a name); cards and a frog before symbols; the tutor reads every question. Number-word writing is limited to copying two words from a bank. Printed number lines are small at 310 px; the large lines are on slides.
- Joining cold: PASS. Warm-up covers counting on and back, one more or less, tens and ones and counting in tens; only counting to 20 is assumed.
- Safeguarding: PASS. Main room only, papers shown once together, no private chat, cards cut by a grown-up, volunteers first.
- Pictures and pages: PASS. All 30 slides, 7 workbook pages, guide cover, home and parent pages viewed. Guide cover title is overlapped by Mi on long titles (template).

## Instrument A (gifted-style, 0 to 2 each)

1 Low floor, high ceiling: 2 Ladder from filling a gap to a clue puzzle and make-your-own.
2 Depth over speed: 2 Hop counting, nearer by counting not guessing.
3 Generalise: 2 Rule for the ones digit decides nearer ten (Investigation); meeting in the middle.
4 Justify: 2 Talk question, T1, S8 spot the mistake.
5 Multiple paths: 1 Count hops, use cards, or read the line.
6 Challenge ladder: 2 Three tiers plus investigation.
7 Student-led inquiry: 1 Cards and frog are hands-on but tutor-led.
8 Complexity / context: 1 Frogs and number words only.
9 Problem posing: 2 G3 and online g4 make your own line.
10 Metacognition: 1 Look-back only.
11 Pacing / compacting: 1 Choice after page 1, lockstep deck.
12 Extension, not acceleration: 2 Halfway and equal jumps extend, no new topic.

Total: 19 / 24 (author). Independent auditor scored 17/24; after the fix pass the re-score is below.

## Known limits

- Never trialled with children; times and difficulty are modelled.
- Nearer ten is beyond Primary 1 (rounding is Primary 4); the syllabus check for this new-topic lesson is still open.
- Investigation page now has 4 writing lines (template fix 2379b77); no table of 41 to 49, children write on the lines or spare paper.
- Kit pages are number cards (square ones cards, wide tens cards, no circles); families without a printer use 11 paper squares.

## Fix pass (22 Oct 2026), re-score of the independent audit (instrument A)

Independent auditor's 17/24 re-scored by the fix author (a model, not independent): 4 justify 1 to 2 (T1 and T3 now have writing lines, S8 has Yes/No printed); 2 depth 1 (unchanged, 8 + 4 + 3 items); 5, 7, 8, 11 unchanged at 1; 12 extension 1 (nearer ten stays informal). Re-score about 18/24. Tier compliance 15/15 (T4 replaced by a new idea: hopping 2 at a time and landing on 100, not counting on by 1). Start here still 8 items; not shortened (19 modelled minutes). Details in `audit/FIXES_L02.md`.

Owner decision of 22 Oct 2026 applied: tutor guide (strand note and prep list) and parent summary now say that Term 1 goes beyond the school Primary 1 syllabus on purpose; nothing says MOE-aligned.

Open: (1) syllabus check for the new-topic lesson (number-line scale, nearer ten) still with the owner or a tutor; (2) Start here still long (S4 and S5 involve reading and writing number words); (3) no table for the Investigation (template); (4) the T-page numbered line is not printed (children use their cards, frog or a drawing); (5) home sheet prints ___ not boxes (template).

## Update (second fix pass, 22 Oct 2026)

Machine state: validate 02 = 18 pass, 2 WARN (opening 1:58 of 3:00 and exit 4:04 of 6:00 are loose, explained), 0 FAIL; 448 answer checks, 221 practice variants; leak check clean. Script 74:40, slow 88:27. Workbook 7 pages (88, 96, 87, 86, 90, 82, 83%), home 2, parent 1. All pages, key, home, parent and changed slides viewed. Changes in `audit/FIXES2_L02.md`. Opening now 3 minutes, Explore 15, to fit the recording, muting and camera statement.
