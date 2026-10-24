# Home practice, parent summary and online practice audit: Level 1 Term 2 Lesson 14 (Odd + Odd: Always, Sometimes, Never)

Role HOME_PARENT_PRACTICE. Files audited: `out/l14/L14_Home_Practice.pdf` (2 pages), `L14_Parent_Summary.pdf` (1 page), `out/l14/practice/` (key `t2l14`, runner version 2, 14 items, 10 templated). Source data `lessons/l14.json`. Read first: owner decisions (Term 2 defaults 7 and 9), `TERM_WIDE_AUDIT.md`, `HOME_PARENT_PRACTICE_AUDIT_L09.md` (shared runner findings R1 to R12 not repeated), and the L13 audit of this role (same runner, same print template).

## Verdict: Ready after minor fixes

Sums, pictures and marking are right (ordered list answers refuse a wrong order; "Odd/Even" choices work; no network calls). Faults: the numbering clash in the parent page, a home sheet whose lettered parts run together, a "blanks" message on a list answer that has no blanks, and templates whose answers never vary.

Counts: lesson-specific 0 High, 3 Medium, 7 Low. Shared runner and print items: as L13 (unchanged).

## Method

- Home sheet and parent summary rendered at 60 and 100 dpi, text extracted, margins measured (left 13.9 mm, right 14.8 mm, top 14.4 mm, footer 6.3 mm), all five home answers solved (Even, Odd, Even; 1; 6, 8; 11 odd and 16 even; open).
- Online practice served over HTTP and driven in Playwright 1.56 (Chromium) at 390x800 and 1280x800. Every item opened; number items: wrong twice, then right in 6 typed forms (`1`, ` 1 `, `01`, `1 counters`, `1.0`, `twelve`, empty); choice items: wrong then right; the **ordered list** item c6 tried with `2, 4, 6, 8, 10`, `2 4 6 8 10`, `10, 8, 6, 4, 2`, `4, 2, 6, 8, 10`, `2, 4, 6, 8`, `2, 4, 6, 8, 10, 99`, `2,4,6,8,10.`; self-check g4. External requests (none), console errors (none), horizontal overflow (none), `file://` (fails with the tutor message).
- Pictures: c2 has 10 variants (n = 4 to 13); counted: n pairs-and-ring counters, ring present exactly when n is odd (4 and 6 have no ring circle; 5 has 6 circles = 5 counters + ring); no variant lacks a picture.
- Templates re-derived: c1 `n % 2` over [even, odd] (even for even n, odd for odd n); c4 same for two-digit n; c5 and c2 `n % 2`; c6 `multiples(2, lim)` ordered; t1 `(a + b) % 2` where a and b are both odd; t3 `n % 2` over [yes, no] (even n gives yes); t4 `(a + b) % 2`; g1 `(a + b + c) % 2`; g2 `lim // 2`. All correct. Placeholders filled; plural wording fine ("1 counters are left over" never appears: the step text "{ans} counters are left over" gives "1 counters are left over" when n is odd, see L14-8).
- Page source: no answers in `index.html` or the DOM; no external URL in `practice.js`.

## A. Printed pieces

| Item | Finding |
|---|---|
| Home maths | All five correct. H1 to H3 Start here (odd/even by pairs, a story, the even digits), H4 Think harder (parity of two sums), H5 Go further (open: two odd numbers adding to 20 and to 30). Wording plain; no hint in stems. |
| Can a parent help without teaching differently | Yes: counters in pairs, "is one left over?". The sheet does not say what not to teach (see L14-6). |
| Parent summary | 83-word summary (under 90), plain English, no "MOE-aligned", GEP or SASMO claim. "Odd and even numbers are Primary 2 work at school, so this whole lesson goes beyond Primary 1 on purpose, always with counters" is honest and specific. WhatsApp number and 90 days match `privacy.html`. |
| Consistency with lesson | Words, questions and try-at-home items match the guide and deck. The "Words we used" list defines "claim" as "something we say is true, and then test", which is muddled (a claim may be false). |
| Print | A4, two pages, answers on page 2 (good). Left margin 13.9 mm = no binding gutter; footer 6.3 mm from the bottom edge. |

## B. Lesson-specific findings

| # | Sev | Where | Evidence | Fix |
|---|---|---|---|---|
| L14-1 | Medium | Parent summary heading and "Next lesson" | Page shows "Lesson 4 ... for parents" but says "Lesson 15: Equal Groups" as next, while the workbook and slides say Lesson 4 and the next workbook says "Lesson 5". The guide says "Lesson 14". | One numbering scheme in all family-facing pages. |
| L14-2 | Medium | Home sheet Q1 and Q4 | Q1 reads "Pair up counters. Write Odd or Even. (a) 8 ____ (b) 15 ____ (c) 20" and the (c) blank drops to the next line on its own; Q4 runs "(a) 5 + 6 = ____ Odd or Even (b) 7 + 9 = ____ Odd or Even" across two lines with "Odd or Even" detached from the blank it belongs to. The child cannot tell which blank is for (c). Known template limit (FIXES2_L06 "home sheet cannot put parts on separate lines"). | Let the home sheet break between (a), (b), (c); or give each part its own line. |
| L14-3 | Medium | Online c6 (and every ordered/list item) | A child who types `4, 2, 6, 8, 10` is told "Those are the right numbers, but check which one goes in each blank." There are no blanks in a count-in-twos list. The message belongs to the fields type. Wrong orders are refused (good) but the feedback is confusing for a 6-year-old. | Message for `ordered` list items: "These are the right numbers but the order is not right. Count in 2s from the start." |
| L14-4 | Low | Online t1, t4, g1 templates | All variants have the same answer: t1 a and b are odd, so `(a+b)%2` is always even; t4 `(a+b)%2` with odd a and b is always 0; g1 three odd numbers is always odd. A child who learns "odd + odd = even" and presses "even" always passes; "Try a similar one" never tests the opposite case. Contrast t3 (n varies). | Mix odd and even addends (a in 2 to 13, b in 2 to 13). |
| L14-5 | Low | Online c1 template | Options `["even","odd"]` and 18 values: the answer is correct but the option order after shuffling is random: fine. For single-step items the first wrong answer shows the authored slip only for the base number (7); variants give "Not quite yet" (shared R11). | Generate slips. |
| L14-6 | Low | Parent summary | No "please do not teach ..." line (Term 1 L06 had one). A parent may teach "divide by 2". | "Please do not use dividing or halving: pairs and left-over counters are enough." |
| L14-7 | Low | Parent summary, Try at home 3 | "Swap and make a mistake on purpose for them to find." is ambiguous (who swaps, who makes the mistake). | "Say a wrong reason on purpose (e.g. 'odd plus odd is odd because both are odd') and ask your child to find the problem." |
| L14-8 | Low | Online c2 steps | Step "{ans} counters are left over" is correct for 0 and 1 only as "0 counters" and "1 counters" (the base item says "1 counter is left over"; the templated step prints "1 counters are left over"). | Use "{ans} left over". |
| L14-9 | Low | Home sheet H3 | "The last digits of even numbers are 0, 2, 4, [] and []" asks the child to recall a fact the parent page prints in "Words we used". | Fine; optional: hide it on the parent page. |
| L14-10 | Low | Home H5 key | Key shows "15 + 15 = 30"; two equal odd numbers are allowed ("Write two odd numbers"), but a parent may think the same number twice is wrong. | Add "the same number twice is fine". |

## C. Online runner checks (Playwright results)

| Check | Result |
|---|---|
| Opens at 390 and 1280 px | Yes, no horizontal scroll, text 18 px. |
| Pictures | c2 pictures render for all 10 variants; counted correctly with the ring on odd numbers only. The single picture item here is the only figure in the lesson; the other 13 items are text only, so "pair up counters" for c1, c3, c4, t1 to t4 is mental or with real counters. |
| Typed numbers | `1`, ` 1 `, `01`, `1 counters`, `1.0` accepted; `1 2`-type (two numbers) gets "Please type just the answer number." for single-number items; `twelve` gets "Please type the answer with number digits, like 54."; empty gets "Type or choose an answer first. It is fine to guess." Kind and neutral. |
| Ordered / list marking | c6 accepts `2, 4, 6, 8, 10`, `2 4 6 8 10`, `2,4,6,8,10.`; refuses `10, 8, 6, 4, 2` and `4, 2, 6, 8, 10` (right numbers, wrong order: message L14-3), `2, 4, 6, 8` ("Those fit. Are there more? Keep looking.") and `2, 4, 6, 8, 10, 99` ("Some of these fit, but one does not."). Marking is right; only one message is off. |
| Choice items | Options shuffled; wrong then right works; odd/even and always/sometimes/never; yes/no for "Can you make n by adding two odd numbers?" correct for 10 variants. |
| Wrong answers | First wrong: "Not yet. Try once more." plus authored slip or generic; second wrong shows answer and steps; no score, no timer, neutral. |
| Network and privacy | 8 same-origin requests; no tracking, no cookies; `localStorage` for progress. |
| Keyboard | Enter submits; focus returns to BODY after Check (shared R4). |
| Answer leak | None in the page source; data file holds answers (shared R9). |

## D. Home timing and fit

"About 15 minutes": H1 (3 words), H2 (1 number), H3 (2 digits), H4 (2 sums plus 2 words) and H5 (4 numbers) is about 10 to 12 minutes for a middle child. Three tiers in the same order as the workbook. H4 and H1 reuse class types (S2, T1), good for practice; H5 is a real open task.

## E. What is good

Beyond-P1 statement honest; "one test is not a proof" in plain English for parents; neutral feedback; the ordered-list marking works; every picture item is correct; no timers or scores; stuck route is the grown-up's WhatsApp photo with the 90-day statement matching the privacy page.
