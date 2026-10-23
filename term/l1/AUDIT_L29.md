# Self-audit: Level 1 Term 3 Lesson 9 (Spot the Mistake)

Self-audit written by the author from the validator results of the last build. Rubric: `docs/audit/reaudit_p1.md` instruments A and tier compliance, `AUTHORING.md` checklist.

## Automatic checklist

| Criterion | Result | Evidence |
|---|---|---|
| Schema valid (JSON Schema + key checks) | PASS | schema: all top-level keys present |
| Every answer verified independently (verify/lNN_checks.py) | PASS | verify: 475 answer checks by independent script passed (term/l1/verify/l29_checks.py) |
| Online practice variants verified (expression, oracle, runner JS) | PASS | practice: 238 template variants verified three ways (expression, brute-force oracle, runner JavaScript calc) |
| Timing: parts sum to 90, no part OVER, buffer, slow-class | PASS | timing: 11 parts, contiguous, sum = 90 minutes exactly |
| Slides and script linked (each slide once, in its part) | PASS | link: 34 slides each shown exactly once, all question ids resolve |
| Tier counts and completeness (answer, hint, solution, mistakes) | PASS | tiers: counts, completeness (answer, hint, worked solution, mistakes), exit 3, home 5 |
| Neutral labels, no overclaims, no private chat | PASS | wording: no banned labels or claims in child and parent text |
| Recording cues short, with child action | PASS | rec: 11 cues, each at most 26 words, each with an action line |
| Spare-time menu present | PASS | spare: 3 spare-time activities, 11 optional minutes (not in the 90 sum), rules present |
| No copied contest text | PASS | copy: no 7-word overlap with docs/sasmo analysis/solution notes or docs/books (originals only) |
| Mascot used modestly | PASS | mascot: Mi on 4 slides, short friendly lines only |
| Workbook page fill (model) | PASS | pages: workbook page fill (measured on the built PDF) 94%, 99%, 94%, 94%, 99% (kit pages excluded) |
| Real PDF page count and fill | PASS with warning | outputs: Workbook page 6 is 69% full (target at least 85%) |
| No template leak (other lesson titles, Lesson 1 text) | PASS | template leak: no other lesson title or stray Lesson 1 text in the built files |

Timing: script 67.4 min of 90, slow-class 79.6 min. Workbook fill (measured on the PDF): 94%, 99%, 94%, 94%, 99%.

## Judgement lines (author)

- Tier principle (Start here approachable and not contest-style; Think harder = taught idea in a new setting; Go further = mastery plus extension): PASS. Start here is add back, one wrong step, o'clock and half past, a total within $13 and four true or false sums, all within 100 with the check part given as a fill-in. Think harder holds the error-analysis moves (compensation step, two ways to check, a wrong fewer-than sum, a time that cannot be shown); Go further holds the beyond item (estimating) and a wrong digit in a column sum.
- Age-appropriateness for 6 to 8 (reading load, one new idea, objects before symbols): PASS. One idea (check a second way). Objects first: 8 cards, a clock, a number line. Stems are 1 to 3 short sentences; the tutor reads every question. Wrong working is never given a name.
- Joining cold (Remember warm-up covers every prerequisite): PASS. Adding back, a tens jump and one hour later are re-taught with a picture; a child with only the holiday course can follow. Safe to miss is stated (fairly safe; Quest gate 7 depends on it).
- Safeguarding and privacy consistent between script, slides and guide: PASS. No papers or cards held to the camera, no private chat, look-back never collected, WhatsApp number only in the grown-up pages, wrong working only to 'a child in another class'.
- Pictures and pages viewed at readable size, nothing clipped or overlapping: PASS. Viewed all 6 workbook pages, key, home sheet, parent page and every slide at reduced size. Kit page 6 is short by design (69 percent). Slide text is small on question slides, as in the other Term 3 decks.

## Instrument A (gifted-style, 0 to 2 each)

1 Low floor, high ceiling: 2 - cards and add back at the floor; estimating and column-sum errors above;
2 Depth over speed: 2 - one idea, two ways to check;
3 Generalise: 2 - the same lost ten in three sums (Investigation);
4 Justify: 2 - how do you know prompts and the Talk question;
5 Multiple paths: 2 - add back, take away, number line, clock;
6 Challenge ladder: 2 - Start, Think, Go, Investigation;
7 Student-led inquiry: 1 - children choose pages; Explore asks what the size of a mistake tells us;
8 Complexity / context: 1 - time and money stories, but short;
9 Problem posing: 2 - G3 and the spare-time puzzle write a sum with one mistake;
10 Metacognition: 2 - checking a check; look-back;
11 Pacing / compacting: 1 - flex buffer and skip order; no compacting path;
12 Extension, not acceleration: 2 - beyond item is a new way of thinking, not later content;

Total: 21 / 24

## Known limits

- Never trialled with children; times and difficulty are modelled. Wording unverified against Primary 1 papers for 'check by a different way' (no paper evidence). Time items are o'clock and half past only, as the papers show. Estimating is beyond Primary 1 and is flagged on the parent page.

## Fix pass (Term 3 independent audits)

See `audit/FIXES_T3_L29.md`. After the fix pass: validator 22 pass, 0 FAIL; script 67:40 of 90, slow class 79:54; workbook page fill 94, 99, 97, 94, 99% (kit page 69%); T1 made unambiguous, S5 and E1 and the G3 example no longer reuse class numbers, online static items replaced, hand-off to Lesson 30 aligned. Open: kit page spacing and labels, black and white build, L20 hand-off (shared tools or other owner).
