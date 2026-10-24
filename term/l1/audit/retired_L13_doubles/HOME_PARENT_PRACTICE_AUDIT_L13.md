# Home practice, parent summary and online practice audit: Level 1 Term 2 Lesson 13 (Doubles and Near Doubles)

Role HOME_PARENT_PRACTICE. Files audited: `out/l13/L13_Home_Practice.pdf` (2 pages), `L13_Parent_Summary.pdf` (1 page), `out/l13/practice/` (key `t2l13`, runner version 2, 14 items, 11 templated). Source data `lessons/l13.json`. Read first: owner decisions (incl. Term 2 defaults 7 and 9), `TERM_WIDE_AUDIT.md`, `HOME_PARENT_PRACTICE_AUDIT_L09.md` (shared runner findings R1 to R12 are not repeated unless changed).

## Verdict: Ready after minor fixes

Maths right, pictures render and are correct for every variant, typed answers are handled sensibly, no network calls, no leaks in the page. The remaining problems are numbering, layout of the home sheet and two items that use pictures the online page does not show.

Counts: lesson-specific 0 High, 3 Medium, 6 Low. Shared runner (same file in all lessons, md5 identical in L09, L13, L14, L20): see section C.

## Method

- Home sheet and parent summary rendered at 60 and 100 dpi, text extracted, ink margins measured from pixels (left 13.9 mm, right 14.8 mm, top 14.4 mm, footer 6.3 mm from the bottom edge), all five home answers re-solved (8, 12, 16; 14; 40, 80; 13, 19; 35).
- Online practice: `out/` served over HTTP, driven with Playwright 1.56 (Chromium) at 390x800 (phone) and 1280x800 (laptop). Every item of every tier opened; for number items: wrong answer twice (reveal), then the right answer typed as `12`, ` 12 `, `012`, `12 counters`, `12.0`, `1 2`, `twelve`, empty. For choice items: wrong then right. For the field item (domino): right, swapped boxes, one wrong, blank. Self-check item exercised. External requests logged (none), console errors (none), horizontal overflow (none at either width), `file://` open (fails with the "ask your tutor" message: the page needs a web server).
- Pictures: for the two picture items (c1 counters in ten-frames, c6 domino) all 8 and 9 variants counted from the SVG: red and yellow counters equal n for c1 n = 2 to 9, pips equal 2a for c6 a = 1 to 9; no variant lacks a picture.
- Templates re-derived independently: c1 and c2 `n+n`, c3 `t+t` (t = 10n), c5 `n+n`, c6 `a, a, a+a`, t1 `a + (a+1)`, t2 `a + (a-1)`, t4, g1 five terms (m+1, m-1) = 5m, g2 (m-1) + m + (m+1) = 3m, g3 double n for n in 12, 15, 16, 24, 25, 35, 45: all correct. No unfilled placeholder or singular/plural error seen.
- Page source: `index.html` has no answers; `practice.js` has no external URL, no storage other than a local progress flag, no tracking. The answers sit in `data/t2l13.json` (static; same as Term 1 R9).

## A. Printed pieces

| Item | Finding |
|---|---|
| Home maths | All five correct. H1 to H3 Start here (doubles, a story, tens doubles); H4 near doubles at Think harder; H5 at Go further (7 + 8 + 7 + 6 + 7 = 35). Wording plain; no hint in stems; units fine. |
| Parent can help without teaching differently | Yes: "wait 10 seconds", "which double helps?", counters. The page does not say what not to teach (see P5). |
| Parent summary | 80-word summary (under 90). Plain English; no "MOE-aligned", GEP or SASMO claim; the beyond-P1 statement is specific ("doubling a number like 35 and adding five almost-equal numbers go beyond school on purpose, in Go further only"). The 90-day photo retention and the business WhatsApp number match `privacy.html` (photos of work 90 days after the programme ends). |
| Consistency with lesson | Words, questions and try-at-home items match the deck and guide. |
| Print layout | A4, two pages; answers on their own page (good). Margins 14 to 15 mm left and right: no extra left margin for binding (see P4). |

## B. Lesson-specific findings

| # | Sev | Where | Evidence | Fix |
|---|---|---|---|---|
| P1 | Medium | Parent summary headings and "Next lesson" | The page head shows the lesson number "3" (Term 2, lesson 3) but says "Next lesson: Lesson 14: Odd + Odd" and the "Have ready" list says "The Lesson 14 workbook". Workbook and deck call it Lesson 4. A parent holding a workbook labelled "Lesson 4" is told to prepare "Lesson 14". | One numbering scheme (recommend "Lesson 4" in family-facing text). |
| P2 | Medium | Home sheet Q1 and Q4 (layout) | Several lettered parts run on in one paragraph and wrap awkwardly: "(a) Double 4 is [] (b) Double 6 is [][]. (c) / Double 8 is [][]" with (c) cut across a line; Q4 "(a) 6 + 7 = [][] (b) 9 + 10 = [][]" on one line with no gap. WORDING_GUIDE says one part per line ((a)/(b) on separate lines). Known limitation "home sheet cannot put parts on separate lines" from FIXES2_L06. | Template fix: allow line breaks between parts on the home sheet. |
| P3 | Medium | Online items c2, c3, c1 hints | c2 "What is double 7?" hint "Fill the first frame to ten, then count the rest" and c3 "Think of 2 tens and 2 tens" refer to a frame or bars that are not shown (only c1 and c6 have pictures). A child cannot "fill the first frame" on a screen with no frame. | Add the existing ten_frame/bars figure to c2 and c3, or reword to "use counters at home". |
| P4 | Low | Print | Left margin 13.9 mm equals the right margin; a punched or stapled left edge loses text near the margin. Footer is 6.3 mm from the page bottom, inside the unprintable band of many home printers. | Add a 5 mm gutter on the left and lift the footer to 9 mm (template). |
| P5 | Low | Parent summary | No "please do not ..." line: Term 1 L06 added "please do not teach the column method". Here a parent could teach "double and add 2" for near doubles or halving. | Add "please do not teach adding 2 to a double; the trick is 1 more or 1 less". |
| P6 | Low | Parent summary, term line | "Your child is learning to draw a story, to use groups and sharing, and to test a claim with an example" is the Term 2 line (plan), unrelated to this week's doubles; the weekly line is on the sheet's "report_line" only. Fine, but the page itself gives no reason for the Term 2 sentence. | Optional: lead with the weekly line. |
| P7 | Low | Online t1 to t4 variant slips | Variants have `slips: []`, so only the authored numbers get specific feedback (e.g. 14 for 7 + 8); a child who writes the double gets the generic "Not quite yet". (Shared R11.) | Generate slips (double, double + 2) in the template. |
| P8 | Low | Online c1 and c6 pictures | c1 shows only one ten-frame per colour, so double 9 (9 red + 9 yellow) fills each frame to 9: correct. Pictures render at phone width without scroll. No fault found; c6 domino ignores a/b order (a = b always), so ordered marking cannot be tested by this lesson. | None. |
| P9 | Low | Home sheet H3 | Needs "Double 20 is []" two boxes each: fine; the number of boxes again reveals two digits (see workbook finding 6). | As the workbook. |

## C. Online runner checks (Playwright results)

| Check | Result |
|---|---|
| Opens at 390 px and 1280 px | Yes; no horizontal scroll; tier buttons and 6 numbered dots wrap cleanly; text 18 px. |
| Pictures render | c1 (all 8 variants) and c6 (all 9 variants) show; correct counts; `role=img` with aria-label on the SVG. |
| Typed numbers | `12`, ` 12 `, `012`, `12 counters`, `12.0` accepted; `1 2` gives "Please type just the answer number." (kind, does not use a try); `twelve` gives "Please type the answer with number digits, like 54." (the example 54 is unrelated to a doubles question but neutral); empty gives "Type or choose an answer first. It is fine to guess." |
| Wrong answers | First wrong: "Not yet. Try once more." with the authored slip message where the typed number matches one (slips exist in the data, e.g. 14 for 7 + 8; the browser run used 999 and 998, which correctly got the generic message); second wrong shows "Let us look at it together. The answer is ..." with steps. Tone neutral, no scores, no timer. |
| Multi-field marking | Domino c6: right accepted; swapped boxes (4, 4, 8 is symmetric, so this lesson cannot expose a swap bug); one wrong box gives "Look again at the boxes with a red edge"; blank gives "Type a number in every box". |
| Ordered and list answers | None in this lesson (no set item). Tested in L14. |
| Choice | Options shuffled per page load; wrong then right works; correct option is not always first. |
| Network and privacy | 8 requests, all same origin (page, css, fonts, data); no tracking, no cookies; progress kept in `localStorage` (wrapped in try/catch). |
| Keyboard | Enter submits; after Check the focus moves to BODY (re-render drops focus: shared R4); dots and options reachable by Tab. |
| Offline `file://` | Shows "This practice link is not complete. Please ask your tutor for the right link." (needs hosting; shared R1). |
| Answer leak | None in `index.html` or the DOM before checking; answers only in the data JSON (shared R9). |

## D. Home-practice timing and fit

"About 15 minutes": five items with 7 boxes of writing and one two-line working space is about 10 to 12 minutes for a middle child (H5 up to 5 on its own). Fine. Home practice keeps the three tiers in the same order as the workbook. The sheet repeats class examples (H2 is S5 with a different number; H4 uses 6 + 7 and 9 + 10 from the class slides), so it practises the method but not transfer: acceptable for home.

## E. What is good

Neutral feedback; every variant has a picture where a picture is needed; variants stay within P1 numbers except the Go further set (double 35 and 45 only at "Go further"); a self-check item (g4) lets the child make near doubles; no timers or scores.
