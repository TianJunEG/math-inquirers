# Weekly Family Check-in: Google Form build sheet

Status: DRAFT for owner approval. Nothing is built or sent. This sheet only tells you what to type into Google Forms and Google Sheets yourself. Design reference: `docs/product/weekly_checkin_test.md`.

Owner decisions applied: the test runs through Google Forms (not WhatsApp); the weekly puzzle consent is shown below for your approval; contact email is `pypteltd@gmail.com` (to be changed later); data is deleted 30 days after the test ends.

---

## 0. Consent wording for approval (DRAFT, lawyer check pending)

```
+--------------------------------------------------------------------------+
| DRAFT: please approve or change. Not yet checked by a lawyer.            |
|                                                                          |
| Math Inquirers Weekly Family Check-in: what you agree to                 |
|                                                                          |
| WHAT WE COLLECT. Your first name; your email or WhatsApp number; and     |
| your child's age band (for example 8 to 10). Each week you will send     |
| one number: your child's total screen time from your phone's own         |
| report. We never ask for your child's name, and please do not send       |
| screenshots.                                                             |
|                                                                          |
| WHY. Only to write you a short reply each week (this week against last   |
| week) and to decide whether a tool like this is worth building.          |
|                                                                          |
| HOW LONG. We delete everything about you 30 days after the test ends,    |
| unless you choose to continue.                                           |
|                                                                          |
| STOPPING. You can stop at any time by messaging us. We delete your data  |
| within 7 days and confirm.                                               |
|                                                                          |
| SHARING. We do not share your data with anyone. Google stores the form   |
| answers for us, and only the owner of Math Inquirers can see them.       |
|                                                                          |
| WHAT THIS IS NOT. This is awareness only. We make no health or           |
| screen-time-harm claims and we do not say how much screen time is right. |
|                                                                          |
| Contact: pypteltd@gmail.com (Math Inquirers, Preciouslyours Pte Ltd)     |
|                                                                          |
| [ ] Required: I agree to the above, and I am the parent or guardian.     |
|                                                                          |
| [ ] Optional: Please also send me a free 5-minute puzzle for my child    |
|     each week, in my weekly reply, by the email or WhatsApp number I     |
|     gave. I can say "stop" at any time.                                  |
+--------------------------------------------------------------------------+
```

Notes for you (not shown to parents):
- The optional puzzle tick is separate. If it is not ticked, the weekly reply has the numbers and trend only, with no puzzle.
- Still undecided in `docs/legal/review.md` (item D5, P12): whether weekly puzzles count as service or marketing. This wording treats them as a separate optional opt-in with a stop option, which is the safer reading.

### Lawyer-check notes (done by Claude against `docs/legal/review.md` and `website/privacy.html`; not legal advice)

The consent text above matches the test design (section 5 of the test doc). Mismatches with the live privacy page that you should fix before launch:

1. `website/privacy.html` has no section for the check-in. Add a row to "What we collect" (parent first name, email or WhatsApp number, child age band, weekly total, optional note), a row to "How long we keep it" ("30 days after the test ends, unless you choose to continue"), and the wording for the two ticks.
2. The privacy page says "No marketing" for the timing-request form and says nothing about a mailing list. The puzzle tick needs its own line there (review item P12/D5).
3. The page says "We do not sell personal data or use it for advertising" but never says plainly "we do not share it with anyone". The check-in text does say this. Add the same plain sentence, with "except providers that store it for us (Google)".
4. The page names Google Drive and Meet, Supabase and WhatsApp as providers. Google Forms and Google Sheets must be added, with "may store data outside Singapore" (PDPA transfer limitation, review item 9).
5. Withdrawal: the page promises a reply within 30 days; the check-in promises deletion within 7 days. Both can be true, but keep 7 days in the form text only if you will really do it.
6. Contact: the page lists Jasmine Hon with `pypteltd@gmail.com`, marked "to be changed later". The review (P1) says a personal-looking Gmail is not a good public data protection contact. When you change the email, change it in the privacy page, both forms, and this sheet.
7. "Unless you choose to continue": the privacy page needs a line saying that continuing means you will ask again for agreement for the new period.
8. Retention differs by product (12 months for timing requests, 30 days after the test for the check-in). That is fine, but the privacy page must list each separately.
9. Age band labels in the test design (6-8, 8-10, 10-13) overlap at 8 and 10. Suggest "6 to 7, 8 to 9, 10 to 13" so a parent can pick only one; the form below uses the design's labels with a note, your choice.

---

## 1. FORM A: one-time sign-up and consent

Create at forms.google.com, blank form.

**Title (exact):** `Math Inquirers Weekly Family Check-in: sign-up`

**Description (exact):**
```
Thank you for joining our 6-week test. Each week you send one number from your phone's built-in screen-time report (2 minutes) and we reply with a short note. Please read the box below, then fill in the form. No child names, no screenshots. Questions: pypteltd@gmail.com
```

### Questions (in this order)

| # | Question text (exact) | Type | Required | Options / settings |
|---|---|---|---|---|
| 1 | Your first name | Short answer | Yes | None. |
| 2 | How should we reach you? | Multiple choice | Yes | `Email` / `WhatsApp` |
| 3 | Your email address or WhatsApp number | Short answer | Yes | Help text: "Include the country code for WhatsApp, for example +65 ...". No validation (it can be either). |
| 4 | Your child's age band | Multiple choice | Yes | `6 to 8` / `8 to 10` / `10 to 13` (see note 9 above about overlap) |
| 5 | Please read | Add a "Title and description" block (not a question) | n/a | Paste the consent text from the box in section 0, from "WHAT WE COLLECT" to "Contact". |
| 6 | I agree to the above, and I am the parent or guardian of the child. | Checkboxes (one option: `I agree`) | Yes | Required means they cannot submit without ticking. |
| 7 | Optional: please also send me a free 5-minute puzzle for my child each week, in my weekly reply, by the email or WhatsApp number I gave. I can say "stop" at any time. | Checkboxes (one option: `Yes, please send the weekly puzzle`) | No | Leave unticked by default (Google Forms never pre-ticks). |

Do not add any question asking for the child's name, school, a photo or a screenshot.

**Confirmation message (Settings, Presentation, Confirmation message), exact:**
```
Thank you! You are signed up. We will message you within 1 day with your family code (for example F07) and the link to the weekly check-in. To stop at any time, message pypteltd@gmail.com with the word "stop". We will delete your data within 7 days and confirm. Your data is deleted 30 days after the test ends unless you choose to continue.
```
Turn off "Show link to submit another response" (Presentation settings) so people do not sign up twice by accident.

**After each sign-up (owner step):** give the family a code (F01, F02, ...) in the Sheet and message it to them yourself. Keep the codes unrelated to the child's name.

---

## 2. FORM B: weekly check-in

**Title (exact):** `Math Inquirers Weekly Family Check-in`

**Description (exact):**
```
Takes 2 minutes. Please send last week's total screen time for your child, from your own phone's built-in report. Please use the same measure every week (total for the week). No child's name and no screenshots, please. Your data is used only to write your reply, is not shared, and is deleted 30 days after the test ends. To stop, message pypteltd@gmail.com.
```

### Questions

| # | Question text (exact) | Type | Required | Validation / options |
|---|---|---|---|---|
| 1 | Week number | Multiple choice | Yes | `1` `2` `3` `4` `5` `6` (multiple choice avoids typing mistakes) |
| 2 | Your family code (given to you when you signed up) | Short answer | Yes | Response validation: Text, Contains, `F`; error text "Please enter the code we sent you, for example F07". |
| 3 | Last week's total: hours | Short answer | Yes | Response validation: Number, Whole number? use "Number, Between 0 and 168"; error text "Numbers only, for example 17". |
| 4 | Last week's total: minutes | Short answer | Yes | Number, Between 0 and 59; error text "Numbers only, 0 to 59". Enter 0 if none. |
| 5 | Your child's age band | Multiple choice | Yes | `6 to 8` / `8 to 10` / `10 to 13` |
| 6 | Optional: one line about the week (for example "exam week" or "holiday") | Short answer | No | Optional: Text, Maximum character count, 140. Help text: "Please do not write your child's name." |
| 7 | Optional: did your child try the puzzle? | Multiple choice | No | `Yes` / `No` / `We did not get a puzzle` |
| 8 | Optional, last week only: would you keep doing this check-in? | Multiple choice | No | `Yes` / `No` / `Not sure` (feeds a success measure in the test design) |

Question 3 help text is shown under it. Add this "where to find the number" text as the question 3 description (exact):

```
Where to find the number (menu names may differ: check on your device)
iPhone: Settings, then Screen Time, then See All Activity (or tap the device name). Choose the weekly view / "Last Week" and read the total. If your child has their own device in Family Sharing, you can look from your own phone.
Android: Settings, then Digital Wellbeing and parental controls, or the Family Link app for a supervised child. Open the dashboard, pick the device, and read the weekly total. If you only see a daily average, multiply by 7 and enter that, the same way every week.
Always use the same measure each week.
```

Add this confirmation message (exact): `Thank you! We will reply within 24 hours. To stop, message pypteltd@gmail.com.`

Do not collect emails in this form (see settings).

---

## 3. Settings to choose in Google Forms

Do this for both forms (Settings tab, gear icon).

| Setting | Choice | Why |
|---|---|---|
| Collect email addresses | Off for both. (Form A already asks for contact in a question; Form B uses the family code.) | Less data kept. |
| Limit to 1 response | Off | Parents send a response every week; this setting would also force a Google sign-in. |
| Restrict to users in your organisation (Workspace) | No | Parents are outside your account. Anyone with the link can answer. |
| Allow response editing | Off | Keeps the record simple. |
| Show link to submit another response | Off in Form A; fine to leave on in Form B. | |
| Respondents see summary charts | Off | |
| Notifications | Responses tab, three dots, "Get email notifications for new responses": optional, owner only. | |

**Who can see responses:** only you, the owner. Do not use "Add collaborators" and do not share the Sheet. In the Sheet, Share must show "Restricted" and only your own Google account. Do not share the form's edit link. Turn on 2-step verification on the Google account (review item 7).

**Link responses to a Google Sheet:** Form, Responses tab, "Link to Sheets", "Create a new spreadsheet". Create one Sheet per form, named `Check-in test SIGN-UP responses` and `Check-in test WEEKLY responses`. Columns Google creates:

- Form A Sheet: `Timestamp`, `Your first name`, `How should we reach you?`, `Your email address or WhatsApp number`, `Your child's age band`, `I agree...`, `Optional: please also send me...`. Add by hand: column H `family_code`, column I `withdrawn` (Y or blank).
- Form B Sheet (tab "Form responses 1"): `Timestamp`, `Week number`, `Your family code`, `hours`, `minutes`, `age band`, `Optional one line`, `puzzle?`, `would you keep doing this?`. (Column order follows question order; shorten the headers by hand if you like, but do not delete the columns.)

**Close the form after the test:** open the form, Responses tab, switch "Accepting responses" off. Optional message: "This test has finished. Thank you!" Do this in week 7 (6 weeks plus a slack week); note the date as the TEST END DATE. Set a calendar reminder for TEST END DATE plus 30 days to delete everything.

**How to delete responses (on or before the 30-day date, or within 7 days of a "stop"):**
1. One family: in the Sheet, right-click the row number, "Delete row", for every row with that family code in both Sheets. In the form's Responses tab, Individual view, use the bin icon on that response too (the form keeps its own copy).
2. Everybody: in the form, Responses tab, three dots, "Delete all responses". Then in each Sheet, select rows 2 to the end, right-click, "Delete rows". Then delete the Sheet files and the forms: Google Drive, right-click, Remove, then Trash, "Delete forever". Also delete the Summary/Calc tabs (they are in the Sheet).
3. Message each family: "Your check-in data has been deleted." Interview notes: change to family code only within the same 30 days.
4. Google also keeps version history; deleting the file permanently removes it.

---

## 4. Response Sheet layout and formulas

Use the WEEKLY Sheet. Keep "Form responses 1" untouched (Google writes there). Add three more tabs: `Calc`, `Families`, `Summary`.

### Tab `Families`
Copy from the SIGN-UP Sheet by hand, or paste: column A `family_code`, B `first_name`, C `contact`, D `age_band`, E `puzzle_opt_in` (Y/N), F `withdrawn`. Rows 2 down, one per family. Only family_code is needed by formulas.

### Tab `Calc` (one row per response; fill row 2 down as new responses arrive)

Row 1 headers: `family_code | week | total_h | prev_total_h | change_h | change_pct | trend | puzzle_tried`

| Cell (row 2) | Formula |
|---|---|
| A2 family_code | `='Form responses 1'!C2` |
| B2 week | `='Form responses 1'!B2` |
| C2 total_h | `='Form responses 1'!D2+'Form responses 1'!E2/60` |
| D2 prev_total_h | `=IF(COUNTIFS($A$2:$A,A2,$B$2:$B,B2-1)=0,"",SUMIFS($C$2:$C,$A$2:$A,A2,$B$2:$B,B2-1))` |
| E2 change_h | `=IF(D2="","",C2-D2)` |
| F2 change_pct | `=IF(OR(D2="",D2=0),"",E2/D2)` (format as percent) |
| G2 trend | `=IF(F2="","",IF(ABS(F2)<0.05,"About the same as last week",IF(F2>0,"A bit higher than last week","A bit lower than last week")))` |
| H2 puzzle_tried | `='Form responses 1'!H2` |

Select B-to-H of row 2 and drag the blue handle down; do this each week. If a family sends the same week twice, delete the older row in "Form responses 1" and the matching Calc row, otherwise totals double count. Week 1 has no previous week (the cells stay empty); ask for the week before in your reply instead.

To show hours and minutes: `=INT(C2)&" h "&ROUND((C2-INT(C2))*60)&" m"`.

### Tab `Summary`

Per-family table, rows 2 to 21 (up to 20 families). Row 1 headers in A to F: `family_code | sent_week1 | weeks_of_first_4 | in_week4 | puzzle_weeks | active`.

| Cell (row 2) | Formula |
|---|---|
| A2 | `=Families!A2` |
| B2 | `=IF(A2="","",IF(COUNTIFS(Calc!$A:$A,A2,Calc!$B:$B,1)>0,1,0))` |
| C2 | `=IF(A2="","",SUMPRODUCT((COUNTIFS(Calc!$A:$A,A2,Calc!$B:$B,{1,2,3,4})>0)*1))` |
| D2 | `=IF(A2="","",IF(COUNTIFS(Calc!$A:$A,A2,Calc!$B:$B,4)>0,1,0))` |
| E2 | `=IF(A2="","",COUNTIFS(Calc!$A:$A,A2,Calc!$H:$H,"Yes"))` |

Drag B2:E2 down to row 21.

Overall block (column H labels, I values, J result). Thresholds from the test design:

| Row | H: measure | I: value | J: status |
|---|---|---|---|
| 2 | n (families who sent week 1; judge only if 10 or more) | `=SUM(B2:B21)` | `=IF(I2>=10,"n ok","n under 10: signal only")` |
| 3 | Submitted at least 3 of first 4 weeks (success 60%, weak 40%) | `=IF($I$2=0,"",COUNTIFS(B2:B21,1,C2:C21,">=3")/$I$2)` | `=IF(I3="","",IF(I3>=0.6,"Success",IF(I3>=0.4,"Weak","Failure")))` |
| 4 | Still submitting in week 4 (success 50%, weak 30%) | `=IF($I$2=0,"",COUNTIFS(B2:B21,1,D2:D21,1)/$I$2)` | `=IF(I4="","",IF(I4>=0.5,"Success",IF(I4>=0.3,"Weak","Failure")))` |
| 5 | Tried the puzzle in 2 or more weeks (success 50%, weak 30%) | `=IF($I$2=0,"",COUNTIFS(B2:B21,1,E2:E21,">=2")/$I$2)` | `=IF(I5="","",IF(I5>=0.5,"Success",IF(I5>=0.3,"Weak","Failure")))` |
| 6 | Would keep doing this (yes share; success 60%, weak 40%) | `=IFERROR(COUNTIFS('Form responses 1'!I:I,"Yes")/COUNTA('Form responses 1'!I2:I),"")` | `=IF(I6="","",IF(I6>=0.6,"Success",IF(I6>=0.4,"Weak","Failure")))` |
| 7 | Named one concrete change (from interviews; type number of families, then share is calculated; success 40%, weak 20%) | type count in L7; `=IF($I$2=0,"",L7/$I$2)` | `=IF(I7="","",IF(I7>=0.4,"Success",IF(I7>=0.2,"Weak","Failure")))` |
| 8 | Would pay or recommend, score 8 or more (interview; type count in L8; success 30%, weak 15%) | `=IF($I$2=0,"",L8/$I$2)` | `=IF(I8="","",IF(I8>=0.3,"Success",IF(I8>=0.15,"Weak","Failure")))` |

Rows 7 and 8 take typed counts from the interview in cells L7 and L8 (label them "interview count"). Remember the test design: with n this small, treat numbers as signals and let interviews outweigh the table.

Decision cell: `=COUNTIF(J3:J8,"Success")&" of 6 success, "&COUNTIF(J3:J8,"Failure")&" failure"`. Compare with section 7 of the test design (build a prototype if 4 or more success and none fail; stop if 3 or more fail).

---

## 5. Weekly reply template

Draft from the Calc tab, send yourself (nothing is sent automatically). Reply within 24 hours, by the contact method the family chose.

```
Hi [first name], thanks for this week's check-in.
This week: [X h Y m]. Last week: [X h Y m]. [About N% more / less / about the same.]
[Trend line from Calc column G, one neutral sentence.]
One small idea (optional): [one item from the suggestion bank, or "Nothing to change; thanks for tracking."]
[ONLY if puzzle tick = Yes] 5-minute puzzle for your child (ages [band]): [puzzle from the test doc, week [n]]
Answer at the bottom, no pressure to finish. Next check-in: Sunday.
Answer: [answer]
To stop at any time, just reply "stop".
```

Rules: no health or screen-time-harm claims, no "too much" labels, never shaming. Claude can draft each family's reply from the Calc tab if you paste in the row; you read, edit and send. Week 1: no comparison; thank them and ask for the week before if they have it. The puzzles and the suggestion bank are in `docs/product/weekly_checkin_test.md`, section 3.

---

## 6. Owner checklist (in order)

1. Approve or edit the consent box in section 0 (and say yes or no to the weekly puzzle tick).
2. Build Form A and Form B from sections 1 and 2; choose the settings in section 3.
3. Submit one test response in each form yourself, check the Sheet columns, delete the test rows.
4. Update `website/privacy.html` per the lawyer-check notes (items 1 to 8), then send it for the small lawyer review in `docs/legal/review.md`.
5. Only then invite families. Set the calendar reminders: test end date, and end date plus 30 days for deletion.
