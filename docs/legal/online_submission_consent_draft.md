# Online practice: consent lines and privacy page additions (DRAFT)

Status: **draft for the owner and a lawyer. Nothing here is applied** to `website/privacy.html`, `website/terms.html`, `portal/public/app.js` or `portal/public/common.js` (`MI.VERSIONS`). I am not a lawyer. Bracketed items need a decision. Design and reasons: `docs/online_submission_design.md`. Question to the lawyer: question 11 in `docs/owner_kit/lawyer_email_draft.md`.

Why a new consent and not the existing "Children's work" line: the existing line (portal `childs_work`, privacy page item 5) says we keep "photos of my child's work, practice answers and short progress notes". It does not say that answers typed into an online workbook are sent to us, re-marked by us, turned into reports for tutors and for the parent, and (for extension book families) that no live-lesson recording is involved. A parent who only bought a book should not have to agree to lesson recording.

## 1. Which consent applies to which family

| Consent type (portal `consent_type`) | Live group family (holiday or term) | Extension book, online (or both), no group | Extension book, workbook only (posted) |
|---|---|---|---|
| `contact` (existing) | needed | needed | needed |
| `terms` (existing) | needed | needed | needed |
| `recording` (existing) | needed | **not asked** | **not asked** |
| `childs_work` (existing) | needed | **not asked** | **not asked** |
| `online_practice` (NEW) | needed to send answers online | needed | not asked |
| `book_delivery` (NEW) | not asked (the registration form handles delivery of the beta workbook) | needed only if a posted book is chosen (workbook or both) | needed |
| `marketing_contact` (NEW, optional) | optional | optional | optional |
| `feedback_quotes` (existing, optional) | optional | optional | optional |

UI change needed in `portal/public/app.js` (not done): the "Agreements" card currently says the first four "are needed to join a live recorded group" and `requiredOk()` blocks enrolling and shows "Save the four needed agreements first". Split the card into three blocks: **For everyone** (contact, terms), **If your child uses online practice** (online_practice), **Only for live group classes** (recording, childs_work), and **Optional** (marketing_contact, feedback_quotes). `requiredOk()` is then used for enrolling only; buying a book checks the new needs in `create_ext_order()` (done in the SQL draft). Nothing is pre-ticked.

## 2. The exact consent lines (draft)

**Online practice (`online_practice`, needed to send answers online):**

> I am the parent or legal guardian of this child. I agree that when my child presses "Submit" on an online practice page, Math Inquirers (Preciouslyours Pte Ltd) receives my child's answers, marks them again on our server, and keeps them with my child's profile (first name or nickname and level) to make practice reports for me and, if my child is in one of our groups, for my child's tutor. We do not use my child's answers for advertising. We keep them for 12 months after the last submission, or until 90 days after my child's online access ends, whichever is sooner, and then delete them. I can ask to see, correct or delete them, or withdraw this agreement, at any time. [Retention: owner decision, lawyer to confirm]

**Explanation boxes (part of the `online_practice` line; DRAFT, owner and lawyer to approve, NOT yet in `portal/public/common.js` or the practice-page footer):**

> Some practice questions have a box where my child may type a few words to explain their thinking. If my child types something there and presses "Submit", Math Inquirers keeps those words (at most 500 characters per question) with the answers, and only my child's tutor, the owner and I can read them. They are not shown to other families and are deleted with the answers. My child does not have to write anything.

The database keeps the text only for self-checked and open questions (never for a marked answer or a paper-only task), never shows it back to the child, and deletes it with the submission (12 months / 90 days, "delete practice answers", "delete my data"). Because a child can type anything, the footer wording on the practice pages ("Your answers are sent to your tutor...") must be reviewed together with this line before the pages go live: **flagged for owner sign-off.** The client footer wording has not been changed.

**Book delivery (`book_delivery`, needed to post a printed book):**

> I agree that Math Inquirers (Preciouslyours Pte Ltd) may give my delivery name, Singapore address, postal code and phone number to its printer and courier, only to print and deliver the book I ordered, and will delete them 30 days after the parcel is confirmed delivered. [Same wording as the existing workbook delivery line in the registration form; printer and courier names to be added]

**Messages about trial classes (`marketing_contact`, optional, never ticked for you):**

> [Optional] I agree that Math Inquirers may contact me by email or WhatsApp to suggest a free trial class or a next book, including a suggestion based on how my child did in the online practice. I can say stop at any time and we will stop. I do not have to agree to use the online practice or to ask for a trial class.

(Registered mobile numbers: if we send marketing by SMS or WhatsApp to a Singapore number, the Do Not Call rules of the PDPA apply. Ask the lawyer whether this consent line, which is clear and in writing, is enough, and whether the Do Not Call Registry must also be checked. See question 11.)

## 3. Additions to the privacy page (draft, for `website/privacy.html`)

**Under "What we collect, and why", add a row:**

> **Online practice answers.** If your child uses an online practice page and presses "Submit": the answers they typed or chose, which questions they skipped, the mark our server works out for each answer, which question set they did and when we received it, and (for questions done on paper) whether your child ticked "I got it", "I checked it" or "not yet". Linked to your child's first name or nickname and level. We do **not** collect what your child writes in open or "do it on paper" boxes, a photo, school, or NRIC. We do not time your child. *Why:* to give your child and you feedback, to let a tutor see what to teach next, and to improve our materials.

**Under "Who can see it", add:**

> * Online practice answers and reports: you (the parent); the owner of Math Inquirers; and, if your child is in one of our groups, that group's tutor. Other families never see them. Our database and hosting providers store them: Supabase (database) [region: owner to confirm; Singapore is the aim] and Cloudflare (the website and the page that receives the answers, which runs at data centres near the child, so answers pass through servers outside Singapore). Stripe handles online payments for book orders. These providers may store or process data outside Singapore; we choose providers that protect personal data to a standard comparable to the PDPA.
> * We use practice results to suggest a next step to **you** inside your own report. We send you messages about trial classes or other books only if you tick the optional message agreement, or if you ask for a trial class. We never use a child's answers to compare children or to show them to another family.

**Under "How long we keep it", add rows:**

| Data | Kept for |
|---|---|
| Online practice answers and reports | [12 months after the last submission, or 90 days after your child's online access ends (refund or removal) or after the program ends, whichever is sooner; then deleted. A default for the owner and a lawyer to confirm] |
| Book orders (what was bought, for which child, date, amount) | 7 years, as business and tax records (no delivery details) |
| Delivery name, address and phone for a posted book | [30 days after the parcel is confirmed delivered, then deleted; same as the workbook delivery rule] |
| Trial class requests | [12 months after you send the request, or sooner if you ask] |
| Sign-in sessions for the practice page | 4 hours; then unusable, removed within 7 days |

**Under "Your rights", add:** you can ask us to delete your child's practice answers without closing the account (also a button in the portal: `delete_child_practice`), and you can withdraw the online practice agreement; from then on new answers are not sent, and the page keeps working on your child's own device only.

**Under "Wording used on the registration form"**, add the three new lines of section 2 as items, and change the heading note "Children's work" so it says it applies to live group families (the sentence on practice answers there stays; it refers to answers given in live lessons).

**Under "Why you are reading this"**, add: "Families who only buy a book are not joining a live group, so the recording and children's work agreements do not apply to them."

## 4. Terms page (for the owner and lawyer)

`website/terms.html` is about the live program (refunds, groups, instalments). Extension book orders need their own short terms: what is sold (printed book, online practice for one child, or both), one purchase is for one named child and cannot be shared with a sibling, online access period [stated or "for as long as we offer the page"], refunds (the portal draft revokes online access on refund), returns of printed books, and no promise of any school result. Not drafted here beyond this list.

## 5. Deletion process (suggested)

1. **A parent asks to delete a child's practice answers:** the portal button calls `delete_child_practice(child)` (deletes submissions, per-question rows and sign-in sessions). Done at once.
2. **A parent withdraws the online practice agreement:** the new consent row stops sending at once. Existing answers stay until deleted by (1), by the retention rule, or by request: say so in the confirmation.
3. **A parent closes the account:** the existing `delete_my_data()` deletes the children, and the new tables are linked with `ON DELETE CASCADE`, so submissions and sessions go too (tested). Orders are kept as anonymised purchase records (a purchase for a child who no longer exists); the address was already cleared 30 days after delivery.
4. **Refund or revoked access:** online access stops; past answers are deleted 90 days later by `admin_purge_expired_practice()`.
5. **Owner routine (monthly, or pg_cron):** `admin_purge_expired_practice()`, `admin_clear_delivered_addresses()`, and for a finished group `admin_purge_practice_for_group(group, date)`.
6. **Access or correction requests:** the owner runs the parent's own report (`practice_child_detail`) and sends it; reply within 30 days as the privacy page promises.
7. **A suspected breach:** the existing breach plan applies; notify PDPC and affected parents for a notifiable breach.
