# Home practice, parent summary and online practice audit: Level 1 Term 3 Lesson 30 (Calendar Detective, and Mi's Challenge Quest)

Role HOME_PARENT_PRACTICE. Files audited: `out/l30/L30_Home_Practice.pdf` (1 page), `L30_Home_Answers.pdf` (1 page), `L30_Parent_Summary.pdf` (1 page), `L30_Quest_Parent_Note.pdf` (1 page, the grown-up note for the Quest), and `out/l30/practice/` (key `t3l30`, 11 items: 5 Start here, 3 Think harder, 3 Go further; 6 templated, 0 with a picture, 1 self-check). Source: `lessons/l30.json`. Read first: `AUDIT2_BRIEF.txt`, `AUDIT_T3_BRIEF.txt`, owner decisions, `TERM_WIDE_AUDIT.md`, `website/privacy.html`, `docs/books/p1_school_paper_patterns.md`, the L20 Quest parent note (the model), and the L29 audit of this role.

## Verdict: Ready after minor fixes

The home maths, the answer page and the parent summary are right and plain, and the online practice runs cleanly: every item marks correctly, every templated answer (about 35 variants) is computed correctly, there are no external requests and no overflow at phone or laptop width. The faults that matter: the Quest grown-up note is the Term 2 note with the term number changed (it states a false beyond-P1 list and tells families to print a log that is in their book), the online practice prints wrong ordinal endings ("the 2th", "the 3th", "the 21th", "the 22th", "the 23th") in three item families, three online items repeat workbook items, there are no pictures although the lesson is about the calendar, the parent summary does not say how to send the Quest photos, and there are no rewind items.

Counts: High 0, Medium 4, Low 6.

## Method

- Home sheet, answer page, parent summary and Quest note rendered at 70 to 80 dpi and text extracted. All five home answers solved independently: H1 Wednesday plus 4 is Sunday; H2 the 1st and the 8th are Wednesdays, so the 10th is a Friday; H3 14 + 7 = 21 and 14 + 14 = 28; H4 Saturday plus 9 is Monday (7 days is Saturday, 2 more is Monday); H5 36 + 10 - 4 = 42 (Term 1 Lesson 10 rewind). All match the answer sheet; the answers are on a separate page, so a double-sided print never shows them behind the questions.
- Online practice served over HTTP and driven in Playwright 1.56 (Chromium) at 390 x 800 and 1280 x 800. Every tier and item opened and screenshotted. Templated items (c1, c2, c5, t1, t3, g1) were varied with "Try a similar one" after two wrong answers: 9 c1, 3 c2, 5 c5, 8 t1, 2 t3 and 8 g1 distinct variants (every value in the template ranges is reached); the shown answer of each was compared with an independent computation (a + 7; 7 w; s + 21; a + 14; 14 w; (31 - a) div 7 + 1): 0 wrong answers. The ordinal endings in the question text and the worked steps were checked for every variant: 12 wrong endings found (finding 1). Typed-answer handling on the shared runner is as in L28 and L29 (digits only; "seventy" asks for number digits; two numbers asks for just the answer number). Choice options are shuffled on every load. No ordered or multi-answer item exists in this lesson, so "wrong order refused" does not apply. Keyboard: the first box has focus on load; Enter checks. External requests: none. Console errors: none.
- Pictures: none. The lesson is about a calendar and the online set has no calendar, no clock and no table: a month page would help every c and t item (finding 3). The "pictures render" check is therefore vacuous for this lesson.
- Page source: `index.html` and `practice.js` hold no answers or external URL; the answers sit in `data/t3l30.json`, fetchable by any browser (shared with every lesson).

## A. Printed pieces

| Item | Finding |
|---|---|
| Home maths | All five correct. H1 to H3 Start here (days later counting on from tomorrow, a date on the month page, a week and a fortnight after a date), H4 Think harder (9 days later, with "I know because"), H5 earlier practice (Term 1 Lesson 10, a two-step sticker story). Plain wording, no cast name on wrong working (there is none), units on the line. H2 says "the month page in your book" (the kit page: true; no month page is printed on the home sheet, so a family that has lost it needs a calendar from the house, which the hint line allows) |
| Can a parent help without teaching differently? | Yes. The answer page uses the class words ("count on from tomorrow: Thursday 1, Friday 2 ...", "7 days later is Saturday again") and says "wait 10 seconds, then suggest drawing it" |
| Pictures | None on the home sheet: H2 and H3 need the month page; the sheet does not print one (Low, finding 6) |
| Parent summary | One page, plain English. Words list (week, fortnight, days later, date, the day before). The "when stuck" line is good: "Asking 'What is tomorrow?' works better than giving the answer. Please do not chant the days; say them calmly." The beyond statement names only "finding the day 100 days later, using whole weeks and the days left over, goes past the school Primary 1 syllabus on purpose"; the lesson file also marks a fortnight, "two days after the day before yesterday" and every Wednesday of a month as beyond. It says days of the week are not a listed Primary 1 outcome nowhere (the tutor guide says so): a parent could assume the calendar is Primary 1. No MOE-aligned, GEP or SASMO claim. The parent summary says "We also played Mi's Challenge Quest ... your tutor then sends one line", but does not say that the family photographs the four pages the same day or where to send them (that is in the separate Quest note: finding 5) |
| "Try at home" | (1) "Look at a calendar. Ask: what day is it 3 days later? Count on from tomorrow." (2) "Pick a date. Ask: what date is a week later? Look straight down one row." (3) "Today is Monday. What day is it 10 days later? Use a whole week first." (answer Thursday). All three work for a parent with a real calendar |
| Recording statement on the parent page | "Missed a lesson? Every lesson is recorded; your tutor will share a private link with enrolled families." No statement of what is recorded and no "do not share the link"; the parent summary does not say that the Quest is not recorded and is played at the make-up slot (Low, finding 7) |
| When your child is stuck | The WhatsApp number appears once with the 90-day retention, consistent with `privacy.html` |
| Term line | "Your child is learning to give a reason, and to read time and money in real life." On the last lesson of the term and a calendar lesson: acceptable but generic |
| Numbering | "Level 1 • Term 3 • Lesson 10 • For parents": correct; "Next term, the first lesson of Term 4: Half and Quarter": correct, no global number |
| Have ready for next lesson | "Your Term 4 book (Book 7): tear out the fold-shapes page ... a grown-up cuts out the 10 fold shapes; a coloured pencil; pencil, rubber and paper": matches preflight section 5; the Lesson 31 file does not exist yet, so the two sides cannot be compared |
| Print layout | A4, left margin 14 mm for the bound edge, answers on a separate page, header and footer clear; the home sheet is about 85% full |

## B. Quest grown-up note (`L30_Quest_Parent_Note.pdf`)

| Check | Finding |
|---|---|
| Model | A word-for-word copy of the Term 2 note (`L20_Quest_Parent_Note.pdf`) with "Term 3" for "Term 2" and "4 pages" for "3 pages" |
| Beyond statement | "Term 3 goes beyond the school Primary 1 syllabus on purpose (odd and even numbers, the 3 and 4 tables, and stories about groups), so a few gates may be new." False for Term 3: the gates are clocks to 5 minutes, am and pm, coins and change, prices, a grid, a stick pattern, a checked sum and a calendar. A parent reading it would expect gates on multiplication tables (finding 2) |
| Where the Quest Log is | "We send you this note and the Quest Log a week before. Print the Quest Log at 100% ... It has 4 pages. No printer? Tell us a week before and we will find another way." The Lesson 29 hand-off, the guide, `materials` and the lesson file all say the Quest Log is in the Term 3 book; the printed book has no need of a printer (finding 2) |
| Photo route | "ONE clear photo of each of the 4 pages ... to the program's business WhatsApp, +65 9880 5962 ... not to a tutor's own phone, not to the class chat, and never through a child ... We keep the photos for 90 days after the program ends, then delete them, as our privacy notice says." WhatsApp-only: correct and consistent with `privacy.html`; "WhatsApp is a messaging service run by another company" is an honest disclosure |
| Privacy of the Quest | "nothing is added up, there is no league table and nobody is compared"; "your child's paper, photos and note are treated as private: we never show them to other children or families". Good. But the Quest Log itself says "nobody sees your answers" while this note asks for photos of every page to be read by the tutor (finding 4) |
| Words | No "test", "exam", "score", "mark" (negatives only), "rank" or "grade" on the note; it says "It is a game" and "If you would rather not play the quest, tell us: that is fine." |
| The example line | "In Mi's Challenge Quest, Mei drew a strip to find how many more marbles one child had." A Term 2 behaviour; no Term 3 gate has strips or marbles (Low, finding 8) |
| Recording | "The quest is not on the recording, but your child can play it at the make-up slot, before watching the recording": correct and matches the guide; there is no sentence saying that the lesson recording is paused during the Quest |

## C. Online practice

| Item | Result |
|---|---|
| c1 (a week after the {a}th) | Correct for every a (2, 3, 5, 8, 9, 11, 14, 16, 20); **wrong ordinal endings**: "the 2th", "the 3th", "the 21th" (a = 14) and "the 23th" (a = 16) in the question, the worked steps and the answer line; the blank "___ th" is fine |
| c2 (days in w weeks) | Correct for w = 2, 3, 4; plain |
| c3 (Tuesday plus 3), c4 (after Sunday) | Static, correct; **c3 is workbook S3(a)** (finding 1) |
| c5 (count in 7s) | Correct for every s |
| t1 (Ben swims every 7 days, his 3rd swim) | Correct for every a (1 to 9); **wrong ordinals**: "the 1th", "the 2th", "the 3th", "the 22th" (a = 8), "the 23th" (a = 9) |
| t2 (two days after the day before yesterday) | Static, correct (Thursday); **identical to workbook T1(a)** |
| t3 (2 or 3 fortnights) | Correct |
| g1 (Mondays in a 31-day month) | Correct for every a (1 to 7: 5, 5, 5, 4, 4, 4, 4); **wrong ordinals** "the 1th", "the 2th", "the 3th" |
| g2 (100 days after Monday) | Static, correct (Wednesday); **identical to workbook G1(b)** |
| g3 (make your own puzzle) | Self-check; the steps appear after the child writes; fine |
| Rewind items | None: "runner rewind items absent" (brief). H5 on the home sheet is the rewind (Low, finding 9) |
| Accessibility | All controls labelled; the first box has focus; radios carry the option text; no pictures so no alt text is needed; a calendar picture would need one |
| Kind feedback | Neutral and short ("Not yet. Try once more.", "Let us look at it together."); no scores, no timers; wrong variants have no slip lines (Low) |
| Answers in the page | Static JSON, as for every lesson (Low, shared) |
| Page header | "Level 1 · Lesson 10 · Days, weeks and dates": no term (it reads as Term 1 Lesson 10, a different lesson) (Low, finding 10) |

## Findings

| # | Sev | Location | Evidence | Suggested fix |
|---|---|---|---|---|
| 1 | Medium | Online c1, t1, g1 templates | The template text uses `{a}th` instead of the ordinal formatter, so 12 variants print "the 1th", "the 2th", "the 3th", "the 21th", "the 22th" or "the 23th" in the question and the steps (the runner has an `ord` formatter that gives 1st, 2nd, 3rd, 21st, 22nd, 23rd) | Use `{a\|ord}` and `{ans\|ord}` in the three templates and re-verify all variants; also check the static "Ben swims on the 4th" |
| 2 | Medium | `L30_Quest_Parent_Note.pdf` | Beyond statement lists "odd and even numbers, the 3 and 4 tables, and stories about groups" (Term 2); tells families to print the Quest Log that is in the book; example line is Term 2 (a strip, marbles) | Rewrite for Term 3: "Clocks to 5 minutes, am and pm, coins and change, a growing pattern, checking a sum and a calendar go past the school Primary 1 syllabus on purpose, so a few gates may be new"; "Your Quest Log is in your Term 3 book: keep it closed in an envelope until the tutor says to open it"; a Term 3 example |
| 3 | Medium | Online set (no pictures) | A calendar lesson with no month page, clock or table; all items are text; c1, t1 and g1 ask about dates without showing them | Add a calendar picture (the made-up month) to c1, g1 and one c item |
| 4 | Medium | Quest Log "Mi says" and Quest note | The Log says "nobody sees your answers"; the note asks for photos of all four pages to be read by the tutor | Say "your answers are private: your grown-up and your tutor may see them" on the Log, the slides and the note |
| 5 | Low | Parent summary | Does not say that the family photographs the four Quest pages the same day and sends them to the business WhatsApp (only the separate Quest note does) | One line under "Try at home" or "Next lesson": "Mi's Challenge Quest: please send one photo of each page to the business WhatsApp today, as in the Quest note" |
| 6 | Low | Home sheet H2, H3 | Both need a month page; none printed | Print a small month page on the home sheet or say "use a calendar from the house" in the sheet's first line |
| 7 | Low | Parent summary footer | "Every lesson is recorded; your tutor will share a private link with enrolled families." No statement of what is recorded, no "please do not share the link", no note that the Quest is not recorded | Use the corrected wording and add "The Quest is played at the make-up slot before the recording is watched" |
| 8 | Low | Quest note example | "Mei drew a strip to find how many more marbles one child had" is not a Term 3 gate | "Mei counted coins in tens and fives" |
| 9 | Low | Online set | No rewind items | Add two items from earlier lessons at the end |
| 10 | Low | Online page subtitle | "Level 1 · Lesson 10" has no term | "Level 1 · Term 3 · Lesson 10" |

Counts: High 0, Medium 4, Low 6.
