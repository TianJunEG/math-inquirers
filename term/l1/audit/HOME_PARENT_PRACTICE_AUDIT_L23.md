# Home practice, parent summary and online practice audit: Level 1 Term 3 Lesson 23 (Time Passes)

Role HOME_PARENT_PRACTICE. Files audited: `out/l23/L23_Home_Practice.pdf` (1 page), `L23_Home_Answers.pdf` (1 page), `L23_Parent_Summary.pdf` (1 page), and `out/l23/practice/` (key `t3l23`, runner version 2, 11 items: 5 Start here, 3 Think harder, 3 Go further; 7 templated with a clock picture or a drawn variant). Source: `lessons/l23.json`. Read first: `AUDIT2_BRIEF.txt`, `AUDIT_T3_BRIEF.txt`, owner decisions (Term 2 defaults 7, 9; the 23 Oct entries), `TERM_WIDE_AUDIT.md`, the L20 audit of this role, `website/privacy.html`, `docs/books/p1_school_paper_patterns.md` (time).

## Verdict: Ready after minor fixes

Home maths, parent page and the printed layout are right. The online practice marks every answer correctly (including the ordered two-box time answers: swapped boxes are refused), every clock picture matches its question in all 62 variants tried, there are no network calls, no overflow at phone or laptop width and no script errors. Two defects are visible to every child who gets a fields item wrong twice: the shown answer reads "The answer is The film ends at 4 : 00.." (capital T, double full stop; a Term 2 pattern listed in the pre-flight as already seen), and the eight multi-box items carry no slips, so the usual errors (4:30 for 1 hour, 5:60) get only "look again at the boxes with a red edge".

Counts: High 0, Medium 2, Low 7.

## Method

- Printed pieces rendered at 80 dpi, text extracted, all five home answers solved independently: H1 9:30 am plus 1 hour is 10:30 am; H2 5 o'clock plus half an hour is 5:30; H3 3:45 pm plus half an hour is 4:15 pm; H4 bus ride 1 hour then walk half an hour, home 9:00 pm, so the walk began 8:30 pm and the ride 7:30 pm; H5 17, 27, 70, 72. All match the answer page. Answers are on a separate sheet, so a double-sided print never shows them behind the questions.
- Online practice served over HTTP (`python -m http.server`) and driven in Playwright 1.56 (Chromium) at 390 x 800 and 1280 x 800. Every tier and item opened (Start here 5, Think harder 3, Go further 3). Marking by script: c1 `4` + `00` right, `4` + `0` right (leading zero optional), `00` + `4` (swapped) refused with red edges, `4` + `30` and `5` + `00` refused; c2 `5`+`30` right, `30`+`5` refused; c3 `3`+`30` right, `3`+`3` and `4`+`30` refused; t1 `5`+`00` right, `5`+`30` and `4`+`60` refused; t2 `3`+`45` right, `4`+`15` refused; t3 `5`+`30` right, `5`+`60` and `6`+`30` refused; g1 `3`+`30` right, `4`+`30` and `3`+`00` refused; c4 choice right/wrong; c5 `30` and `30 minutes` right, `60` and `15` get a slip, `half an hour` and `thirty` get "Please type the answer with number digits, like 54."; g2 `90` and `90 minutes` right, `60` and `130` slips, `1h30` "Please type just the answer number."; g3 self-check shows the checking steps. Keyboard: the first box has focus on load and Enter in the first box checks (Enter in the second box does nothing, finding 4). External requests: none. Console errors: none. Horizontal overflow: none at either width.
- Pictures: 62 "Try a similar one" variants taken on c1, c2, c3, t1, t2, t3; for each the `aria-label` ("clock showing 3:00") was compared with the time in the question text and the hour-hand and minute-hand angles of the SVG were recomputed from the two hand lines: 0 mismatches. Variant ranges are safe (c1 h 1 to 10, c2 h 1 to 11, c3 h 1 to 10 so the answer is never "13:30", t1 h 1 to 10, t2 h 1 to 11, t3 h 2 to 11, g1 h 3 to 11 so the start never goes below 1:30); the pm in g1 is correct; plural and number forms are fine (no "1 hours").
- Page source: `index.html` and `practice.js` hold no answers; the answers sit in `data/t3l23.json` which any browser can fetch (as for every lesson; a child who reads the file sees the answers: shared with all runner versions, noted not blamed).
- No rewind items in the online runner (brief: note). The home sheet's H5 is the rewind ("Practice from earlier: Term 1 Lesson 3", ordering 72, 27, 70, 17).

## A. Printed pieces

| Item | Finding |
|---|---|
| Home maths | All five correct. H1 and H2 Start here (an hour and a half hour from o'clock or half past), H3 Think harder (a quarter-time start; digits only, no quarter words), H4 Go further (two-stage trip backwards), H5 earlier practice. Plain wording, units after the blank (am, pm), no hints in stems. The H1 blank "ends at ____ am" and H3 "stops at ____ pm" follow the school-paper pattern |
| Can a parent help without teaching differently? | Yes. The sheet says "use a real clock or your cut-out clock", "a grown-up may read the questions aloud", "wrong answers are fine". The answers page explains each step in the same words as class ("one hour later is the next hour with the same minutes") |
| Pictures | None. A lesson about reading clocks sends home five text-only questions (finding 5) |
| Parent summary | One page, 460 words in total; "What we did" is about 60 words; plain English. Words list (later, lasts, half an hour, am and pm). "Please do not teach a rule such as 'add 60' or 'clockwise'" is the do-not-teach line the pre-flight asked for. Beyond-P1 statement is honest and specific: "Quarter-time starts, and Find the Start (a trip in two stages, and a film that crosses noon), go past the school Primary 1 syllabus on purpose." No MOE-aligned, GEP or SASMO claim. Hand-off box is true: both play-money pages cut out (29 pieces), the $1 tokens from Term 2, the clock, "allow a week". The WhatsApp number and the 90-day retention appear once, in the "when stuck" paragraph, and agree with `privacy.html` (photos of work 90 days after the program ends) |
| Recording statement on the parent page | One sentence: "Missed a lesson? Every lesson is recorded; your tutor will share a private link with enrolled families." It does not say what is recorded (tutor, shared screen, unmuted voices) or that the link must not be shared; the Lesson 11 parent page had both. Consistent with L1, L22 and L24, thinner than L11 (finding 6) |
| Print layout | A4, left margin about 14 mm (the bound edge), answers on a separate page, header and footer clear. The home sheet is full to the last question (about 92% full) |

## B. Online practice

Item types: `fields` (c1 to c3, t1 to t3, g1: a "h : mm" pair), `choice` (c4), `number` (c5, g2), `selfcheck` (g3). The tier counts and the order (c1 to c5, t1 to t3, g1 to g3) follow the lesson: Start here is o'clock and half past, Think harder is quarter-time and count-back, Go further is the two-stage trip, 90 minutes and a self-made puzzle. Wording is plain and matches the workbook ("The film starts at 3 o'clock and lasts 1 hour. What time does it end?"). Hints name the idea, not the answer. Wrong-answer feedback is neutral ("Not yet. Try once more." then the hint, then on the second wrong answer "Let us look at it together" with the answer and the worked steps), no scores, no timers, no streaks.

Typed answers: spaces, a leading zero (`04`), `00` or `0` in the minutes box, a dollar-style prefix and a trailing unit are all handled; words are refused kindly with an instruction. The minutes box accepts `0` or `00` and the display pads to `00`. An hour-and-minute pair typed into the first box (`4:00`) reads as the number 4 then 0 and is judged by field, not by the pair: a child who types the whole time in the first box gets "Type a number in every box" (kind). 

## Findings

| # | Sev | Location | Evidence | Suggested fix |
|---|---|---|---|---|
| 1 | Medium | Online, every `fields` item after two wrong answers (c1 to c3, t1 to t3, g1) | The shown answer reads "The answer is The film ends at 4 : 00.." (capital T mid-sentence, then two full stops): `'The answer is ' + show(...) + '.'` with a frame that already ends in a full stop. Reproduced for c1 (screenshot text copied from the page) | For `fields`, show "The answer is 4 : 00." by building it from the field values, or drop the trailing '.' when the frame ends in one (runner change; version and keep backward compatible) |
| 2 | Medium | Online, `slips: []` on all 8 `fields` items | A child who types 4 : 30 for "1 hour later" or 5 : 60 for "half an hour later" gets only "Look again at the boxes with a red edge." The key lists these exact errors; the number items (c5, g2) have slips, the time items (the lesson's point) have none | Support slips for `fields` (a slip is an ordered pair) and add: c1 `4:30` "Half an hour is not 1 hour: the long hand stays on the 12"; c2/t1 `x:60` "There are no 60 minutes on the clock: the hour changes"; g1 `4:30` and `3:00` |
| 3 | Low | c5 slip | "15 minutes is a quarter of an hour." The word quarter is tutor-only vocabulary on a Start here item (patterns file; guide) | "15 minutes is half of half an hour. Half an hour is 30 minutes." |
| 4 | Low | Runner keyboard | Enter checks only from the first box of a two-box item; Enter in the minutes box does nothing (tested) | Attach the Enter listener to every input in `#ans` |
| 5 | Low | Home sheet | Five text-only questions for a lesson about clock faces; no clock pictures or time line | Add two small clocks (H1, H3) or a blank time line strip for H4; the question wording would not change |
| 6 | Low | Parent page | One-sentence recording statement; no "please do not share the recording link" (present in L11) | Reuse the L11 sentences |
| 7 | Low | Runner header | "Level 1 · Lesson 3 · One hour and half an hour later": no "Term 3" (family pages say "Term 3 • Lesson 3") | Add the term to the sub line |
| 8 | Low | Phone width (390 px) | On a fields item the clock is large, the two boxes wrap on to two lines and the colon sits alone ("[ ] :" then "[ ] ."), so a child must scroll to see the boxes below the picture | Put the frame in a nowrap row, or shrink the picture to 50% height on phones |
| 9 | Low | Home practice H5 label | "Practice from earlier: Term 1 Lesson 3" printed on a Term 3 child sheet; a child who joined at Lesson 21 has no Term 1 Lesson 3. The question is self-contained so no harm; the label may worry a parent | Drop the lesson reference from the child page and keep it in the key |

## What passed

Every answer in the printed and online sets is correct; picture and question agree in all variants; the ordered boxes refuse a wrong order; typed answers with units or spaces are accepted; no network calls, tracking or external fonts (fonts are local); keyboard focus and tab order are sensible; the page is usable at 390 px; dark mode keeps the figures on a white panel. Parent page: one page, plain, no overclaim, true hand-off.

## Instrument summary

| Instrument | Result |
|---|---|
| Home sheet maths | 5 / 5 correct |
| Online items | 11 / 11 correct; 62 variants picture-checked, 0 mismatches |
| Parent summary against the brief (plain English, word limit, no overclaim, beyond-P1 statement, what to say / not say, hand-off true, privacy consistent) | 5 of 6 PASS (recording sentence thin, finding 6) |
| Online runner (marking, ordered boxes, kind feedback, no leaks, keyboard) | 5 of 6 PASS (Enter in second box, finding 4; the answer text sits in a fetchable data file, shared by all lessons) |
