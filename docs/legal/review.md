# Legal self-review: Math Inquirers (Preciouslyours Pte Ltd, UEN 201507566K)

Prepared 23 Oct 2026 for the owner, who asked: "do we really need the lawyer, can you help me review".

**Read this first.** This is a structured self-review by an AI assistant that is not a lawyer. It does not replace legal advice and gives no assurance that the business complies with any law. It reads our own documents against public Singapore sources found by web search on 23 Oct 2026. Many of those sources are law-firm summaries or older PDPC guidance, and some pages could not be opened. Anything marked **verify** must be checked on the official page (or with the regulator) before you rely on it.

**What was reviewed (working tree at commit 61e0848):** `website/terms.html`, `website/privacy.html`, `website/mi_signup.html` (registration and "Request another time" consent texts), `website/referral.html` (referral rules, prototype), `portal/supabase/schema.sql` (consents, deletion), `portal/supabase/interest_requests.sql`, `portal/supabase/stripe_migration.sql`, `portal/public/app.js` and `common.js` (consent texts and versions), `docs/terms/owner_decisions.md`, `website/DEPLOY.md`, `portal/README.md`.

**Moving target.** Another agent is editing the payment wording in terms.html and privacy.html (HitPay to Stripe). At the time of this review those two files had no uncommitted changes and still said HitPay in terms s3 and s7 and in privacy "Who can see it". Check the issue list against the final text; the replacement wording below already says Stripe.

---

## 1. Do we need a lawyer?

### 1.1 The straight answer

**Some of this you must do yourself, lawyer or not, and you can start today. A lawyer is not legally required to open, but a small fixed-fee review of about six items is worth paying for before you take real money from real families.**

The reasoning:

- The Personal Data Protection Act 2012 (PDPA) applies to Preciouslyours Pte Ltd from the first registration, however small it is. No lawyer is needed to comply with it. The failures most likely to hurt are operational: no named Data Protection Officer contact, notices that say things you do not actually do, no breach plan, data kept forever. A lawyer would not fix those for you; you must run them.
- The risky documents are the terms (limit of liability, refunds, referral cash-out) and anything that touches children's images and voices on recordings. Those involve legal judgement (what a court or the Competition and Consumer Commission of Singapore would call fair or reasonable), not just checklists.
- You are charging a deposit-style fee (S$250 beta, larger terms later, instalments planned) to parents of children. The cost of a wrong clause is mainly reputational and a refund fight, but the Unfair Contract Terms Act and the Consumer Protection (Fair Trading) Act (CPFTA) can make a clause unenforceable or, in the CPFTA case, bring regulator action.
- One item may be decisive and is not a drafting question at all: **whether a Ministry of Education registration is needed for the classes** (see 1.4). Ask the regulator, free, this week.

### 1.2 What the law requires regardless of a lawyer: PDPA from day one

Source status: PDPC pages and guidelines below were found by search on 23 Oct 2026. The PDPC key-concepts guidelines are mostly dated 2017 to 2019; the PDPA was amended with effect from 1 Feb 2021 (breach notification, higher penalties). Penalty ceilings are summarised just below the table. Verify the current text on pdpc.gov.sg.

| # | Obligation | What it means for us | To-do (owner) |
|---|---|---|---|
| 1 | Consent, purpose limitation, notification | Tell people why each item of personal data is collected, used and disclosed, and get consent (or rely on an exception, for example the data is necessary to perform the contract) before collecting. Do not make consent a condition of service beyond what is reasonable to provide the service. | Keep the consent boxes; fix the gaps in sections 2 and 4 below; keep the privacy notice true. |
| 2 | Children and minors | PDPC guidance (Advisory Guidelines, Chapter 8 of the Selected Topics guidelines, and the March 2024 guidelines on children's personal data in the digital environment) says a minor aged 13 or older would typically be able to consent for themselves, but only if the notice is understandable to them; for a child under 13 the organisation should get consent from a parent or guardian. The 2024 guidelines treat a "child" as under 18 and cover online services likely to be accessed by children, including tech-aided learning. Not legally binding, but the PDPC is likely to read the PDPA consistently with them. | Keep parent-gives-consent for all levels. Level 6 is ages 11 to 13, so the line "We teach children under 13" is not accurate (see P4). Do not collect directly from children: the child login collects a display name and a PIN only; keep it that way. |
| 3 | Data Protection Officer | Designate at least one person responsible for PDPA compliance and make the business contact information of at least one DPO publicly available. PDPC's homepage said that from 1 Dec 2024 DPO registration on ACRA BizFile+ was unavailable until further notice and a PDPC online form was "to be made available soon". **Verify the current method.** | Name a DPO (it can be you or Jasmine); publish a business email or the business WhatsApp, not a personal Gmail (see P1). Register the DPO with PDPC by the current method. |
| 4 | Purposes and notice | Say what you collect and why. | Update the notice per section 2 (portal data, WhatsApp, payments, hosting). |
| 5 | Access and correction | On request, give a person their data (and information on how it was used or disclosed in the past year; verify) and correct errors. PDPC guidance: respond as soon as reasonably possible, and if you cannot do so within 30 days, tell the person in writing within that time when you will. | Write a one-page procedure: who receives requests (the DPO contact), verify identity (parent of the enrolled child), 30-day clock, a short log of requests. The `delete_my_data()` portal function covers erasure of the login. |
| 6 | Accuracy | Make reasonable efforts to keep data correct, especially if used to decide about the person or disclosed to others (the printer and courier get addresses). | Let parents correct the address before the print run; stop the dispatch list after the cut-off. |
| 7 | Protection | Reasonable security for data you hold, including data held by providers for you (Supabase, Google, WhatsApp, Stripe, Cloudflare). | Two-factor authentication on Google, Supabase, Cloudflare, Stripe and the business WhatsApp (already in portal/README.md); restrict Drive sharing; short list of who has admin; written tutor confidentiality terms. |
| 8 | Retention limitation | Stop keeping personal data when the purpose is no longer served and no legal or business need remains. The PDPA has no fixed period. PDPC guidance (Key Concepts, 2019 revision): archiving or restricting access still counts as retaining. | Set and apply the decided periods (section 3); actually delete: put a dated reminder in your calendar. |
| 9 | Transfer limitation | Before sending personal data overseas, take appropriate steps to ensure the recipient gives comparable protection (typically a contract with the provider, or consent after giving a written summary of how it will be protected). Google, Stripe and Cloudflare process outside Singapore; Supabase should be set to the Singapore region (portal/README says pick Singapore; **confirm in the dashboard**). | Name the providers and countries in the notice (suggested wording P5). Keep the provider data-processing terms you accepted on file (a folder with PDFs or links). Check each provider's current terms; do not rely on this summary. |
| 10 | Data breach notification | Since 1 Feb 2021: assess a suspected breach quickly; notify PDPC if it is likely to cause significant harm or involves 500 or more individuals; PDPC notification no later than 3 calendar days after you assess it is notifiable; tell affected individuals as soon as practicable if significant harm is likely. Weekends and public holidays count. Sources disagree on exactly when the clock starts (discovery or assessment): **verify** and, if in doubt, act on discovery. | One-page breach plan (section 4, item 12). Include "wrong parent sees another child's work" and "lost phone with the business WhatsApp". |
| 11 | Accountability | Be able to show what you decided and when. | Keep this review, the data map (section 3) and the checklist (section 4) in the repo; date each update. |
| 12 | Do Not Call and spam rules | The Do Not Call (DNC) provisions cover marketing voice calls, texts and faxes to Singapore numbers on the DNC Registry, unless you have clear and unambiguous consent. Commercial email in bulk falls under the Spam Control Act. A secondary source says messages sent only through instant-messaging apps such as WhatsApp are outside both regimes (**verify**), but PDPA consent for the use of the number still applies. | The registration page promises "Free weekly puzzles by email" (mi_signup.html). That is not covered by any consent box and the privacy notice says "no marketing". Decide (section 6, D5) and add a consent and unsubscribe if it is marketing. |

Penalties, so the stakes are clear: the 2020 amendments raised the maximum financial penalty to the greater of 10% of annual turnover (for turnover above S$10m, per one summary) or S$1m. For a business our size the realistic risks are a PDPC directions order, a public decision and parent trust, not a headline fine; **verify** the current figures.

### 1.3 What a self-review can cover (this document)

- Reading our terms and notice against the PDPA obligations and the text of the consent boxes and the database.
- Spotting inconsistencies between what the notice says and what the system or the website does.
- Producing ready-to-paste wording and a data map.
- A checklist of PDPA operational tasks.
- A list of the questions only you can answer (section 6).

It cannot tell you whether a clause would be enforced or whether a regulator would accept your reading. It does not replace advice.

### 1.4 Regulatory registration: ask the regulator, do not guess

**Ministry of Education.** MOE's "Register a private school" page (last updated 14 Jan 2025, as shown in search results) says a private school must register its school, courses and teachers if it offers education for 10 or more persons, and that this includes tuition and enrichment centres that teach subjects taught in mainstream schools. A 2026 consultant guide says a centre teaching fewer than 10 may fall outside the rule but advises confirming with MOE. We did not find anything on how online-only classes, groups of up to 8, or a total of more than 10 students across groups are treated. Math Inquirers teaches maths (a mainstream subject) to children, in groups of 8 or fewer, but across several groups and levels. **Verify with MOE** (via the MOE private education page or GoBusiness) before taking fees: do not assume exemption because each group is 8 or fewer. A GoBusiness guide titled "Notification for Private Tuition Enrichment" exists but could not be opened (403); read it.

**Private Education Act 2009 / SkillsFuture / Committee for Private Education (CPE) "EDUCATION registration".** That Act covers private education institutions offering mainly post-secondary and certain other courses. Whether it touches a primary-age maths enrichment business is **not established here: verify with the regulator**.

**CaseTrust.** A search found CaseTrust as the Consumers Association of Singapore's voluntary accreditation (eight schemes, as of the search) with prepayment protection; it did not show an education or tuition scheme. Not required. If you want a trust badge later, ask CASE whether any scheme fits. **Verify.**

### 1.5 Where a lawyer's review is worth paying for

| # | Item | Why a lawyer, not a self-review | Notes |
|---|---|---|---|
| L1 | Limit of liability and indemnity (terms s13, still bracketed) | The Unfair Contract Terms Act 1977 (Singapore Statutes Online, 2020 Rev Ed) section 2(1): you cannot exclude or restrict liability for death or personal injury caused by negligence, by contract term or notice. Section 2(2) and the other sections: other exclusions bind only if reasonable (UCTA s 11 test; I could not open the statute text, **verify**). These sections apply to business liability, and for a consumer on our standard terms the "dealing as consumer / written standard terms" provisions bite (verify s 3 and s 6). Our terms are written standard terms for consumers. A cap that is too aggressive may be struck down, and wording that tries to exclude statutory implied terms for goods (the workbook) is restricted. | A lawyer can calibrate a cap (for example fees paid for the cycle) and word it so it survives the reasonableness test. Scissors and cut-out kits at home are the physical-injury hook. |
| L2 | Refund and cancellation clauses vs the CPFTA | CPFTA (unfair practices; also Part 3 on goods that do not conform to the contract, the "Lemon Law", verify section numbers) cannot be contracted out of. A blanket "beta non-refundable" is not per se unfair (government statements say prepayment packages are not necessarily unfair), but clarity, prominence, instalment liability if the child withdraws, and what happens when we change times or cancel need judgement. | Instalment liability after withdrawal is the biggest gap (issue T6). |
| L3 | Children recording and safeguarding | Recording children's voices and possibly faces on Google Meet, retention, sharing the link with other families, tutor conduct, background checks, reporting duties. Whether the notice matches what Meet actually records (P6) can be tested by you; what duty of care and what promises to make is legal judgement. | Include the tutor agreement (confidentiality, no personal recordings, no private contact). |
| L4 | IP and copyright licence of workbooks | terms s12 is a short personal-use clause. Not covered: who owns children's drawings and answers we photograph, the licence if we later quote or show work (feedback quotes only today), third-party content or font licences inside our books, and the later school photocopy licence. | Also check we have the right to use any image or font in the books (separate from this review). |
| L5 | Referral credits and cash-out (terms s6, referral.html) | The Payment Services Act risk is probably low if credits are closed-loop (usable only with us). MAS says common loyalty points may be "limited purpose" e-money and not regulated, case by case, and I found no source on referral credits specifically. **Cash-out for tutors** at 3 credits per S$1 is different: it looks like remuneration (employment status, tax, possible PSA/consumer issues) rather than a marketing credit. Also: marketing rules if referrers message friends, and tracking friends' data. | Ask the lawyer to confirm closed-loop treatment and the tutor cash-out structure (maybe better as a plain fee). |
| L6 | Terms for school licences later (puzzle books, B2B) | Different contract: licence scope, photocopy rights, invoicing, liability, data (usually no personal data). Not needed now. | Defer. |

**Rough scope for a fixed-fee limited review.** Terms and privacy review (about 15 pages in total), one round of comments, one revision; a short call; a one-page tutor agreement; a referral credit clause; written confirmation on the MOE registration question if the lawyer will give it (otherwise MOE does). Ask for a quote capped at a fixed fee in advance; I cannot estimate the fee reliably, so I give none. The lawyer brief in section 5 is written so the scope stays that small.

---

## 2. Clause-by-clause issue list

Severity: **High** = fix before taking payment or public launch. **Medium** = fix before launch if feasible. **Low** = tidy. "Settled?" says whether the owner's decisions already recorded in `docs/terms/owner_decisions.md` (or the standing facts you gave) settle the item.

### 2.1 terms.html

**T1. Draft banner** (Low)
Quote: "Draft, not yet reviewed by a lawyer. Items [in brackets] need your decision. Remove this note before sharing."
Problem: public draft banner, `build_site.py` also prints a "to confirm" list that must be empty before public build (DEPLOY.md).
Fix: remove the banner after the brackets are settled and, if you decide against a lawyer, replace with a version/date line: "Version terms-2026-10, effective [date]". The version string stored with each portal consent (`terms-2026-10b-draft` in portal/public/common.js) must be bumped to match.
Settled? Not a decision issue.

**T2. s1 registered address** (Medium)
Quote: "(UEN 201507566K, [registered address, to update later])"
Problem: a parent should be able to identify and contact the business; the address is on the ACRA register anyway. UEN is settled.
Replacement: "Preciouslyours Pte Ltd (UEN 201507566K), registered office: [address as shown on ACRA BizFile], business WhatsApp +65 9880 5962, email [business email]."
Settled? UEN and WhatsApp yes; address and email: owner must supply (D1, D2).

**T3. s3 payment gateway** (Medium; the other agent is on this)
Quote: "(From the regular program, payment will be online through HitPay, by card or PayNow.)" and in s7 "payment is online through HitPay."
Problem: decision is Stripe replacing HitPay (also named in privacy and in `stripe_migration.sql`, not yet applied). Stripe availability of PayNow: **verify**.
Replacement: "From the regular program, payment will be online through Stripe, by card [or PayNow, if enabled]. We do not see or store your card number; Stripe does."
Settled? Gateway yes; methods: owner to confirm (D6).

**T4. s3 parcel policy and consumer rights** (Medium)
Quote: "tell us on WhatsApp within 7 days of the first lesson (or of delivery, if later). We reprint and resend it once at no cost ... [Parcel policy: draft default for a lawyer to confirm]"
Problem: a 7-day reporting window and "once" may be read as limiting rights for faulty goods. Goods that do not conform to the contract carry statutory rights (CPFTA Part 3 repair, replace, price reduction or refund; verify limitation periods) that cannot be excluded in a consumer contract. Also nothing on who bears loss in transit.
Replacement: add after the sentence: "This does not affect any right you have under Singapore law, including for goods that are faulty or do not match what we described. The risk of loss or damage in the post passes to you when the parcel is delivered to the address you gave us."
Settled? "Included in beta fee" is decided; the 7-day / once window is a default for the lawyer or for you to keep (D7).

**T5. s3 "Cost" bracket** (Low)
Quote: "[Owner to confirm who pays printing and postage; default: included in the beta fee]"
Fix: decided (owner_decisions.md, 23 Oct "beta workbook is POSTED": included in the S$250 fee unless the owner decides otherwise). Remove the bracket if you confirm.
Settled? Yes by default.

**T6. s5 refunds: beta and withdrawal** (High)
Quote: "The beta fee is not refundable, including once the workbook has been printed or posted." and for the regular program "No refund. Your child may move the remaining lessons to a later cycle ..."
Problems:
 1. Matches your decisions (beta non-refundable; regular program one month's notice, none after the course starts). The substance is a business choice and not unlawful in itself. The risk is presentation and the cases the table does not cover.
 2. **Instalments.** Section 7(b) lets parents pay in three instalments but nothing says whether the second and third are still owed if the child withdraws after lesson 1. "No refund" plus an unclear instalment plan invites a dispute. Under the CPFTA, taking money for services you cannot or will not provide, or terms that are misleading, are problems; an unclear obligation to keep paying is the sort of thing a regulator or CASE would read against the business.
 3. **We change the times** (s2: "we may adjust lessons, times or materials") but the beta is non-refundable even if the new time does not suit a family. A fair reading expects an exit.
 4. **We remove a child for serious conduct:** refund "not applicable to the beta". Keeping a family's money after we exclude their child is the sort of clause that fails a reasonableness test.
 5. **Consent withdrawal** (privacy "Your rights") says "we will refund the lessons not yet held" if the parent withdraws recording or children's-work consent, which contradicts "beta fee not refundable". Pick one rule (D3).
Replacement, add under the table:
"**Instalments.** If you chose to pay in instalments, the instalment plan is a way of paying the full term fee. If your child withdraws after the term has started, the instalments that fall due after the withdrawal [are still payable / are not payable] (see the table above for what is refunded). We will not charge any instalment after you have given us notice under this section where the table says you get a refund."
"**If we change your group's times by more than [30] minutes or move to another day** and the new time does not suit you, tell us within 7 days and we will move you to another group if a seat is free, or refund the lessons not yet held (including in the beta)."
"**If we remove your child from a lesson group** for a reason in section 10, we refund the lessons not yet held (including in the beta), unless the conduct was by you."
"**If you withdraw your agreement to recording or to keeping your child's work** (see the privacy notice), your child cannot join a recorded group, and we refund the lessons not yet held."
Settled? The refund rules themselves yes. Instalment treatment, the time-change exit, the beta exit on removal and the consent-withdrawal refund: owner decisions D3, D4.

**T7. s5 "We cancel a lesson or a group"** (Low)
Quote: "We reschedule. If we cannot, we refund every lesson not held (this includes the beta)."
Fine; keep. Add "within 14 days" (already stated below the table).

**T8. s6 Referral credits** (Medium; lawyer item L5)
Quote: "Referral rewards are paid as credits, not cash. ... Tutors may exchange credits for cash at 3 credits for S$1, in blocks of 30 credits. [Confirm after the beta]"
Problems:
 1. Internal contradiction: "not cash" then cash for tutors.
 2. No rules on expiry, fraud, self-referral, whether credits are clawed back if the referred family gets a refund, whether credits are personal and non-transferable, or what happens on account deletion. The prototype (`website/referral.html`, localStorage only, left out of the site build) has a 60-day referral window and one voucher value; none of that is in the terms.
 3. Cash to tutors: treat as remuneration, not a "referral credit" (tax and employment question), see L5.
 4. Data: the referral system will hold the referrer's and the referred family's name and email; the privacy notice does not mention it.
Replacement:
"**Referral credits.** If a family you refer enrols and pays, you receive credits as described on the referral page. One credit takes S$1 off a later fee. Credits have no cash value, cannot be transferred, expire [12] months after they are earned, cannot be used for the November beta, and are cancelled if the referred family receives a refund. Referring yourself or someone in your own household does not earn credits. We may refuse or cancel credits obtained by misuse. [Tutor cash-out wording: to be settled with the lawyer.]"
Settled? Credit value (S$1 per credit) and 3-credits-for-S$1 cash-out are in the terms as written but marked "Confirm after the beta". Expiry, claw-back and tutor cash-out: not decided (D8).

**T9. s7 term-time bracketed fee** (Low)
Quote: "[S$ per term]", "[Instalment amounts, for example 30% / 30% / 40%]"
Fix: decide price (owner_decisions.md "Open": term price and website still says S$65 a lesson, S$650 for 10). The 5% full-term discount is decided; instalment timing (start, after lesson 3, after lesson 6) is decided; amounts are not.
Settled? Partly (discount and timing yes; price and amounts no) (D9).

**T10. s7 "Missed lessons" and "Holiday courses"** (Low)
Quote: "There are no refunds for skipped lessons."
OK and matches decisions (recordings available, same-lesson later seat if free). Add the length of time recordings stay available (see P7).

**T11. s9 "A parent or guardian nearby"** (Low)
Fine. Add the consent of the adult nearby to be heard on the recording: "Anyone who speaks in the lesson may be heard on the recording."

**T12. s10 Safety and conduct** (Medium)
Quote: "The tutor does not send private messages to children. Check-ins and invitations go to the whole group or to the parent."
Problem: this is a promise and part of the safeguarding case (L3); it must be true and enforced. No statement of tutor screening. Do not claim background checks unless they are done (nothing in the repo shows they are; **verify** what screening the law expects for private tutors, none was found).
Fix: keep only if the tutor agreement says so. Add "Tutors teach through the approved platform only and never ask a child for personal contact details." Add a complaints line: "If you have a concern about a lesson, contact [business email / WhatsApp]. We will reply within [3] working days."
Settled? The policy is in the tutor materials; tutor agreement not yet (D10).

**T13. s11 Recording, children's work and your data** (Medium)
Quote: "Lessons are recorded so that a child who misses a lesson can catch up. We also keep photos of your child's work ..."
Problem: depends on P5/P6. "You agree to it when you register" is fine as a pointer but consent must be separate from the terms checkbox, which it is.
Fix: align with privacy after P6.

**T14. s12 Materials and recordings** (Low)
Add: "Do not share recordings or links with anyone outside your child's group; recordings may include other children's voices." Lawyer item L4 for the licence form.

**T15. s13 Our responsibility** (High)
Quote: "We will take reasonable care in running the beta. We are not responsible for problems outside our control ... [Liability wording to be settled with your lawyer]"
Problem: no liability clause yet (that is safer than a bad one). Do not copy an overseas template cap. Death or personal injury caused by negligence cannot be excluded (UCTA s 2(1)); other limits must be reasonable (verify s 11).
Replacement (paste, then ask the lawyer to confirm):
"We will take reasonable care in running the lessons and keeping your data safe. Nothing in these terms limits or excludes our liability for death or personal injury caused by our negligence, for fraud, or for anything else that cannot be limited by law, or any right you have under Singapore consumer law. Subject to that, if we are at fault, our total liability to you for any one term is limited to the fees you have paid for that term, and we are not liable for loss that we could not reasonably have foreseen. We are not responsible for problems outside our control, such as your internet connection or the video platform being down; if a lesson cannot be held for that reason, section 5 applies."
Settled? No (D11). Need a decision on the cap; a lawyer should confirm (L1).

**T16. s14 Changes, governing law, contact** (Low)
Quote: "If we change these terms we will tell you before they apply to you. ... Questions: WhatsApp +65 9880 5962."
Add: "A change does not reduce what you have already paid for." Add a business email. Add: "Only you and we have rights under this agreement (the Contracts (Rights of Third Parties) Act does not apply)" (Low; lawyer to confirm). Add the Singapore courts.

**T17. Missing clauses** (Medium to Low)
- Seat release for unpaid seats: "If we have not received payment by [date/time before the first lesson], we may give the seat to another child."
- Who the contracting parent is: "You confirm you are the child's parent or legal guardian and at least 18 years old."
- Complaints and dispute route (CASE mediation): "If we cannot resolve a complaint, you may approach the Consumers Association of Singapore (CASE)." (Optional, good practice.)
Settled? No (D10).

### 2.2 privacy.html

**P1. Draft banner and DPO contact** (High)
Quote: "Contact our data protection contact: Jasmine Hon, [pypteltd@gmail.com, to be changed later]."
Problem: a personal-looking Gmail address as the public DPO contact, still marked "to be changed". The PDPA requires business contact information of at least one DPO to be public, and the DPO must be designated. Your decisions fix the business WhatsApp; they do not fix an email.
Replacement: "Data protection contact (our Data Protection Officer): Jasmine Hon, [business email], or WhatsApp +65 9880 5962 (message only; please do not send NRIC or card details)."
Settled? Name yes (Jasmine Hon is in the draft; confirm), WhatsApp yes, email: owner (D1, D2).

**P2. Who we are** (Medium)
Problem: the privacy notice does not state the legal entity, UEN or address; it says "Preciouslyours Pte Ltd (Math Inquirers)" in the sub-head only.
Replacement (add at the top): "This notice is from Preciouslyours Pte Ltd (UEN 201507566K), trading as Math Inquirers, [registered office]. We are the organisation responsible for the personal data described here."

**P3. What we collect: missing categories** (High)
Quote: table "What we collect, and why" (parent contact, delivery, child's name, level, age, recordings, work photos, feedback, timing request).
Problems: the notice omits data that the system actually holds:
 1. **Portal data** (`parents`, `children`, `enrolments`, `payments`, `consents`, `practice_attempts`, `schema.sql`): login email, child display name and level, hashed PIN, family code, enrolment and group, payment reference and status, consent records with version and time, practice answers when used.
 2. **Payments**: PayNow reference now; Stripe later (card data held by Stripe, we keep a reference and status).
 3. **WhatsApp conversations** (parent messages, registration message with child's name and delivery address, photos of the child's end-of-term check sent by parents) held on the business WhatsApp; WhatsApp's own processing.
 4. **Website technical data**: hosting on Cloudflare (server logs, IP addresses) and the Cloudflare Functions that handle payments. Fonts are self-hosted (build_site.py strips Google Fonts), so no third-party tracking was found; verify that no analytics are added.
 5. **Referral data**, if the referral page goes live.
Replacement rows to add:
 - "Portal account: your email, name and phone; your child's display name and level; a PIN (stored scrambled, never in plain text); a family code | To run your account, show your child's place and let your child open the practice area."
 - "Enrolment and payment records: group, status, payment reference, amount, date paid, and your agreements with the version and time | To confirm your seat, take payment, handle refunds and prove what you agreed. Card details are entered on Stripe's page and never reach us."
 - "WhatsApp messages and photos you send us (for example a photo of your child's work) | To reply to you and to give feedback. Send photos only to the business WhatsApp +65 9880 5962."
 - "Website visit data (IP address and technical logs) kept by our hosting provider | To keep the site working and secure."
Settled? Facts are from the system; owner confirms there is nothing else (D12).

**P4. "We teach children under 13"** (Low)
Quote: "We teach children under 13, so we ask a parent or guardian to agree for them."
Problem: Level 6 is "Ages 11-13"; the statement is not literally true.
Replacement: "Our learners are children, so we ask a parent or guardian to agree for them. A parent or guardian registers every child; children do not register themselves."

**P5. Overseas providers and transfer limitation** (Medium)
Quote: "They may store data outside Singapore. We choose providers that protect personal data to a standard comparable to the PDPA. Online payments from the regular program are handled by HitPay ..."
Problem: vague on where, on whom, and on the basis of protection; still names HitPay. The transfer limitation obligation expects you to take appropriate steps to ensure comparable protection (a contract with the provider; or, if relying on consent, a written summary of how the data will be protected, per PDPC guidance as reported in search results; verify). Naming the providers and the country is good practice.
Replacement:
"We use these providers to run the program. Some process or store data outside Singapore, for example in the United States or Europe. We rely on their data-processing terms, which require them to protect personal data to a standard comparable to the PDPA.
 - Google (Google Meet for lessons; Google Drive for recordings and files).
 - Supabase (database for accounts, enrolments and requests; hosted in [Singapore region, confirm]).
 - Stripe (online payments; card details are entered on Stripe's page and are not stored by us).
 - WhatsApp (messages and photos).
 - Cloudflare (website hosting and payment functions).
 - Our printer and courier ([names once chosen]) receive only your delivery details."
Settled? Providers yes (your list); Supabase region and printer/courier names: owner (D12, D13).

**P6. Recording: accuracy of "cameras are not included"** (High)
Quote: "We record the tutor and the shared lesson screen. Children's cameras are not included in the recording, and children's names are not shown. [Confirm the platform setting before the first lesson]"
Problem: this is a factual claim about what Google Meet records. Meet recordings typically follow the active speaker and shared screen; a child's face or name label could appear when their tile is shown, depending on settings. **Test this** with a trial recording (children's accounts on, camera on, someone speaks) before the first lesson; if cameras can appear, the statement is false and consent given on it may be challenged.
Replacement if the test shows a child's tile can appear:
"We record the tutor, the shared screen and anyone's voice that is unmuted. If a child's camera is on while they speak, they may appear in the recording. Children may mute themselves and keep cameras off, and we ask them to. Names shown on screen are first names only. Please tell us when you register if you do not want your child to appear or be heard."
Settled? Partly. The standing decision (owner_decisions.md, item 9 in the 22-23 Oct defaults) says the recording statement is "the tutor, the shared screen and anyone's voice that is unmuted are recorded; children may mute and keep cameras off", which is the safe form. The notice should use that wording (D14).

**P7. Retention table** (Medium)
Quotes: "Lesson recordings: 30 days after your group's last lesson"; "Registration and payment records: 7 years, as required for business and tax records"; "Delivery name, address and phone: [Deleted within 90 days after the program ends ...]"; timing requests "[12 months ...]".
Problems:
 1. **"7 years, as required"** may overstate the legal requirement. Tax and company record rules are commonly cited as 5 years in Singapore (IRAS and the Companies Act; **verify**) and the contract claim limitation period is 6 years (Limitation Act; verify). 7 years can be justified as a prudent business choice, but "as required" is a statement of law. Reword.
 2. **Recording access.** Terms promise recordings (catch-up, "can still watch the recordings of lessons already held") but no end date; privacy says 30 days after the last lesson. Say the same in both places.
 3. **Delivery address 90 days after the program ends** is long: the parcel arrives before lesson 1, the report window ends 7 days after the first lesson. Retention limitation asks you to stop when the purpose is done. Consider 30 days after delivery is confirmed and the report window has closed. Your decision is 90 days (default), which is not unlawful if justified (resends, disputes), but be ready to explain it.
 4. **WhatsApp chats and photos** have no retention stated (the standing decision is that photos come back only via the business WhatsApp). 90 days after the program ends for photos matches the privacy table; apply it to WhatsApp too.
 5. **Portal records** after deletion: payment and consent rows are kept anonymised "for the retention period in the privacy notice" (schema.sql comment on delete_my_data). Say so in the notice: "If you delete your account we keep payment and agreement records without your name, email or phone for 7 years."
Replacement rows:
 - "Registration, enrolment, payment and agreement records | 7 years, which covers the tax and company record periods and the time limit for legal claims."
 - "Photos and messages on WhatsApp | deleted 90 days after the program ends."
 - "Delivery name, address and phone | until [90] days after the program ends (so that we can resend a lost parcel), then deleted; sooner if you ask once the parcel has arrived."
Settled? Periods are your decisions (7 years, 12 months, 90 days default). The WhatsApp period and the 30-day delivery alternative are not (D15).

**P8. Who can see it: tutor and staff access, Drive links** (Medium)
Quote: "Recordings: only the enrolled families of the same group, through a private link."
Problem: a link that "anyone with the link can open" can be forwarded; Drive can restrict to named accounts. That is an operational promise.
Fix: share recordings to named email accounts or with a link that expires, and keep a short log. Or reword: "through a private link which you must not share."
Settled? Operational choice (D16).

**P9. Consent bundling and "improve the lessons"** (Medium)
Quote: "Photos of your child's work, answers ... To give your child feedback, show you how they are doing and improve the lessons." and consent text "Children's work (needed)".
Problem: PDPA does not allow requiring consent for more than is reasonable to provide the service. Recording for catch-up and feedback is arguably necessary for the service; "improve the lessons" is arguably not. Not a flaw today (you only keep the data, you do not publish it) but state it clearly.
Fix: split purposes: "(a) needed: give your child feedback and a progress note; (b) optional: use anonymised examples to improve the lessons." The portal's `feedback_quotes` consent already is optional; you could add a second optional type, which needs a schema change (`consents.consent_type` check list), so do it only if you want it.
Settled? No (D17, low priority).

**P10. Registration consent evidence** (Medium)
Quote (mi_signup.html): the five required boxes, and the WhatsApp message ends "Consents: contact, terms, recording, child's work, delivery details".
Problem: the consent evidence is a typed line in a WhatsApp message with no privacy-notice version; the portal records consent rows with version and time (consents table), the WhatsApp route does not. If the portal does not go live for the beta, the evidence is a chat message only.
Fix: add a version string to the WhatsApp message, for example "Consents (privacy-2026-10, terms-2026-10): ..." (edit mi_signup.html build, not done here). Keep the chat message (screenshot or export) for the retention period.
Settled? No (D18).

**P11. Delivery consent covers printer and courier but not the registration chat** (Low)
Quote: "I agree to Math Inquirers ... giving my delivery name, address and phone number to our printer and courier, only to print and deliver my child's workbook."
Problem: the notice says the printer and courier get delivery details only; make sure the dispatch list given to the printer does not also include the child's name or level unless needed (printed workbooks may have the child's name). The notice says "child's level" is given too. Keep what the notice says. Names of printer and courier are still bracketed.

**P12. Weekly puzzle emails** (Medium)
Quote (mi_signup.html, "You get"): "Free weekly puzzles by email". The "Request another time" consent says "No marketing" and the notice says nothing about a mailing list.
Problem: either a service benefit (then say you use the registration email for it, and describe in the notice) or marketing (then consent, sender identification and an unsubscribe are needed; Spam Control Act for bulk commercial email; DNC does not cover email; verify).
Replacement (if kept as part of the service): add to the table: "Parent email | To send the weekly note and puzzles that come with your child's place. Each email has an unsubscribe link. We do not use your email for other marketing without asking." Add an optional tick box for puzzles for anyone who is not enrolled.
Settled? No (D5).

**P13. Your rights** (Low)
Quote: "We will reply within 30 days."
Fine and in line with PDPC guidance (respond as soon as reasonably possible, and tell the person in writing within 30 days if you need longer). Add: "You may also complain to the Personal Data Protection Commission (pdpc.gov.sg)." Add: "If you ask us to delete your account, we delete your login, your name, email and phone and your children's profiles; we keep payment and agreement records without those details for 7 years." (matches `delete_my_data()`).

**P14. Keeping it safe** (Medium)
Quote: "Our tutors agree to keep children's data confidential and not to make their own recordings or photos."
Problem: only true if a written agreement exists. There is none in the repo.
Fix: either put a one-page tutor confidentiality and conduct agreement in place before the first lesson, or change the sentence to "Our tutors are required to ...". Replace "we will tell you and the authorities as the law requires" with: "If a breach of personal data is likely to cause you significant harm, we will tell you and the Personal Data Protection Commission as the law requires, within the legal time limits."
Settled? No; a tutor agreement is a to-do (D10).

**P15. Wording used on the registration form** (Low)
Item 4 and 6 contain "[Retention and wording: draft default]" brackets. They match the portal and the website forms except that the portal's CONSENT_TEXT does not contain the delivery or timing items (portal does not collect delivery details yet, per build_site.py's todo list). Keep the wording in sync (portal/public/app.js CONSENT_TEXT is "copied from privacy.html"); when privacy.html changes, bump `VERSIONS.terms` and `.privacy` in `portal/public/common.js` and `CONSENT_VERSION` in `website/interest_ui.py`.

---

## 3. Data map

Retention shows the **decided** period (owner_decisions.md and the standing instructions) or the draft default. Lawful basis in Singapore terms: consent (express, from the parent), deemed consent (necessary to perform the contract, PDPA 2020 amendments, verify), or a legal obligation. Where I say "contract" the realistic basis is deemed consent for contract performance plus express consent in the form.

| Data | Where collected / held | Purpose | Basis | Provider and location | Retention | Who can access |
|---|---|---|---|---|---|---|
| Parent account (email, name, phone, family code) | Portal sign-up (`parents`) | Account, contact, payment, refunds | Consent (contact box) and contract | Supabase (Singapore region, **confirm**), Cloudflare | Account life; on deletion name, email, phone are stripped; payment and consent rows kept 7 years | Owner/admin (RLS), parent (own rows) |
| Child profile (display name, level, PIN hash) | Portal (`children`) | Place in group, child practice login | Parent consent (childs_work) | Supabase | Until parent deletes the child or the account | Owner/admin, parent; child sees own area |
| Practice answers | Portal (`practice_attempts`, future) | Feedback, practice | Parent consent (childs_work) | Supabase | 90 days after program ends (draft; **not yet stated for the portal; decide**) | Owner/admin, parent |
| Consents | Portal `consents` (append-only) and the WhatsApp message | Evidence | Legal need to prove consent | Supabase; WhatsApp chat | 7 years | Owner/admin |
| Enrolments (group, status) | Portal `enrolments`; WhatsApp registration message in beta | Run the class | Contract | Supabase; WhatsApp | 7 years | Owner/admin, parent |
| Payments (reference, amount, status; Stripe ids once live) | Portal `payments`; PayNow manual list; Stripe | Take payment, refunds, accounts | Contract; tax/company records | Supabase; Stripe (outside Singapore, **verify entity and location**); the bank for PayNow | 7 years (state the reason as in P7) | Owner/admin; Stripe |
| Card details | Stripe checkout only | Payment | n/a (never reaches us) | Stripe | Stripe's retention | Stripe |
| Interest requests (first name, WhatsApp or email, level, age band, times, note) | Public form -> Supabase `interest_requests`, or WhatsApp fallback | Plan new class times, contact about them | Express consent (itConsent) | Supabase; WhatsApp in fallback | 12 months (`expires_at`), then purge button | Admin only (no table privileges for anon) |
| Delivery name, address, postal code, phone | Registration form -> WhatsApp message (portal does not collect yet) | Print and post workbook | Express consent (delivery box) | WhatsApp; printer and courier (names tbd) | 90 days after program ends (default); consider 30 days after delivery | Owner/staff preparing the dispatch list; printer; courier |
| Lesson recordings | Google Meet -> Google Drive | Catch-up for absent children | Express consent (recording box) | Google (outside Singapore) | 30 days after last lesson (privacy.html); align the terms | Owner/tutor; enrolled families of the group via link |
| Photos of children's work (and end-of-term check) | Parent sends to business WhatsApp +65 9880 5962 | Feedback, parent report, next-term advice | Express consent (childs_work) | WhatsApp (Meta); phone backups, if any | 90 days after program ends (privacy.html); not yet stated for the chat | Owner and tutors using the business number; no personal phones (decision) |
| Progress notes | Tutor notes (location to confirm: Drive?) | Parent report line | Consent (childs_work) | Google Drive (confirm) | 90 days after program ends | Owner/tutor |
| WhatsApp chats (parent messages) | Business WhatsApp | Customer service, class admin | Consent (contact) | WhatsApp | Not yet stated; propose delete 90 days after program ends | Owner and tutors |
| Feedback form | Form | Improve the program | Consent (optional quote box) | Tbd (form tool?) | Kept without the child's name | Owner |
| Website logs | Cloudflare | Security, operation | Legitimate need | Cloudflare | Cloudflare's | Cloudflare |
| Referral accounts (prototype) | `referral.html`, browser localStorage only; not in site build | Credits | Consent | Browser only today | n/a until live | n/a until live |

Gaps to confirm: where progress notes and the feedback form live; whether tutors use their own Google accounts; who has Drive and WhatsApp admin; whether the business WhatsApp is on one phone with cloud backups.

---

## 4. PDPA readiness checklist (status as of 23 Oct 2026)

Status: Done / Partly / Not done / Verify.

| # | Item | Status | What is needed |
|---|---|---|---|
| 1 | Designate a DPO | Partly | Jasmine Hon is named in the draft; confirm she accepts the role in writing (a short note in the repo). |
| 2 | Publish DPO business contact | Not done | Business email or WhatsApp in the notice (P1). Register with PDPC by the current method (verify). |
| 3 | Privacy notice published, true, versioned | Partly | Draft banner on; HitPay/Stripe; missing categories (P3). Bump version strings (common.js, interest_ui.py) after editing. |
| 4 | Purposes stated and limited | Partly | P3, P9, P12. |
| 5 | Consent wording for parents | Partly | Good boxes exist (registration form, portal, interest form); evidence on the WhatsApp route lacks version (P10). |
| 6 | Parental consent for children | Done in design | Parent registers; children do not sign up. Fix the "under 13" line (P4). |
| 7 | Consent for recording and children's work | Partly | Wording exists; recording statement must be tested (P6). |
| 8 | Withdrawal of consent process | Partly | Stated in the notice; define what happens: stop recording the child, refund rule (T6), who handles it, 30 days. |
| 9 | Access and correction process | Not done | One-page procedure and a request log; identity check. |
| 10 | Accuracy: address corrections before print run | Not done | Cut-off date and a last check message. |
| 11 | Protection: 2FA, access list, device security | Partly | portal/README lists 2FA for Supabase, Cloudflare and HitPay (now Stripe). Add Google and WhatsApp. Business phone lock and no personal phones for photos (decision). |
| 12 | Breach plan (assess, 3 calendar days to PDPC if notifiable, tell parents) | Not done | One page with phone numbers and who decides; template message. |
| 13 | Retention schedule applied | Partly | Periods decided; implement deletion calendar; the interest purge button exists; a purge for expired recordings and photos does not. |
| 14 | Retention wording in notice vs terms vs system | Partly | P7. |
| 15 | Overseas transfer notice (Google, Supabase, Stripe, WhatsApp, Cloudflare) | Partly | Naming and basis (P5); keep provider terms on file; confirm Supabase region. |
| 16 | Vendor/processor terms on file | Not done | Save links/PDFs to the processor terms for Google, Supabase, Stripe, Cloudflare. For the printer and courier: a short written undertaking (use only to print/deliver, delete after) as the notice promises. |
| 17 | Tutor confidentiality and conduct agreement | Not done | One page (P14). |
| 18 | Marketing/Do Not Call/spam | Verify | Decide weekly emails (P12). No bulk messages should be sent to anyone without a clear opt-in. |
| 19 | NRIC | Done | Not collected; keep it that way (PDPC NRIC advisory guidelines; verify). |
| 20 | Data minimisation of forms | Done | Interest form: first name, age band; child's name not collected; delivery fields only on request. |
| 21 | Delete-my-data function | Done (design) | `delete_my_data()` in schema.sql; not yet tested live. |
| 22 | Regulator registration question (MOE) | Not done | Ask MOE (see 1.4). |
| 23 | Remove draft banners and brackets | Not done | `build_site.py` "to confirm" list must be empty. |

---

## 5. One-page lawyer brief (send this if you decide to engage a lawyer)

> **Subject: Fixed-fee limited review for a small online maths enrichment business**
>
> **Client.** Preciouslyours Pte Ltd (UEN 201507566K), trading as Math Inquirers. Contact: Jasmine Hon, [email], WhatsApp +65 9880 5962.
>
> **Business.** Live online maths enrichment for children (about ages 6 to 13), taught by tutors on Google Meet in groups of up to 8, 90-minute lessons. A November 2026 beta (10 lessons, S$250 per child) and a term-time program from 2027. A printed workbook is posted to the family's Singapore home (beta). Sessions are recorded for absent children. Parents register; children do not. Data is held in Supabase, Google Drive and WhatsApp; online payments by Stripe from launch, PayNow by hand during the beta.
>
> **What we have done.** A self-review (docs/legal/review.md, attached) against the PDPA and Singapore consumer law. We have drafted terms and a privacy notice and are putting the PDPA operational items in place ourselves. We are NOT asking you to redo these.
>
> **Please review, fixed fee, one round of comments and one revision:**
> 1. Terms section 13 (liability) and any indemnity: advise on a cap that meets the Unfair Contract Terms Act reasonableness test for consumer dealings, and the death or personal injury carve-out.
> 2. Terms section 5 and 7 (refunds, cancellation, instalments, changes to times, removal of a child): advise on enforceability and the Consumer Protection (Fair Trading) Act, and on the instalment-after-withdrawal point.
> 3. Terms section 3 (workbook posted; parcel policy): consumer rights for goods that do not conform; risk of loss in the post.
> 4. Recording and safeguarding (terms sections 10 and 11, privacy notice): whether our wording about recording children's voices and possibly faces is adequate, and a one-page tutor agreement (confidentiality, no personal recordings, no private contact, data handling).
> 5. IP: section 12 licence of workbooks and recordings; ownership of children's work we photograph.
> 6. Referral credits (terms section 6): whether closed-loop credits raise any Payment Services Act or marketing issue, and how to structure any cash-out for tutors.
>
> **Out of scope (we handle):** PDPA operational tasks (DPO, breach plan, retention schedule, access procedure), website copy.
>
> **Questions for a one-line written answer (if you can give them):**
> - Do we need to register with MOE (private tuition or enrichment, groups of up to 8 but more than 10 children across groups, online only)? If you cannot advise, tell us whom to ask.
> - Is the Private Education Act relevant?
>
> **Documents attached:** website/terms.html, website/privacy.html, docs/legal/review.md (this review), docs/terms/owner_decisions.md (extracts on fees, refunds, retention).
>
> **Timing:** before we open paid registrations; please quote a fixed fee and turnaround.

---

## 6. Owner decisions still needed

Settled already (do not re-ask): UEN 201507566K; refund rules (one month's notice for the regular program, none once it starts, beta non-refundable); no make-ups, recordings available, later same-lesson seat if free; retention 7 years (records), 12 months (timing requests), 90 days (delivery addresses, default); providers Google Meet, Google Drive, WhatsApp, Supabase, payment gateway Stripe replacing HitPay; photos returned only via the business WhatsApp +65 9880 5962; beta printed workbook posted and included in the fee; 5% full-term discount; instalments timing.

| # | Decision | Recommended default |
|---|---|---|
| D1 | A business email for the DPO and for contact (not a personal Gmail) | Create a business address and use it in both notices |
| D2 | Registered address to show in terms and privacy | As on ACRA |
| D3 | Refund rule on consent withdrawal and on removal of a child, for the beta | Refund lessons not yet held in both cases (fair, defensible) |
| D4 | Instalments: after withdrawal, are later instalments owed? Exit if we change times? | Not owed after a refundable withdrawal; owed if after the start (matches "no refund once started"); give an exit if we change times materially |
| D5 | Weekly puzzle emails: service or marketing? | Part of the service for enrolled families with unsubscribe; separate opt-in for anyone else |
| D6 | Stripe methods at launch (card, PayNow?) | Confirm in Stripe dashboard (verify) |
| D7 | Parcel policy: 7-day reporting window, resend once | Keep; add the "does not affect your legal rights" line |
| D8 | Referral credits: expiry, clawback on refund, tutor cash-out structure | 12-month expiry; claw back on refund; ask the lawyer (L5) |
| D9 | Term price, instalment amounts, register-by date | Open; the register-by date is also needed in `beta_schedule.json` |
| D10 | Tutor agreement, complaints contact, unpaid seat release, what screening you do | Write the one-page agreement before lesson 1 |
| D11 | Liability cap: yes/no and amount | Cap at fees paid for the term, with the carve-outs in T15 (lawyer to confirm) |
| D12 | Anything else collected (progress notes where? feedback form tool? analytics?) | Confirm nothing beyond the data map |
| D13 | Supabase region; printer and courier names | Singapore region; fill names once chosen |
| D14 | Recording statement wording after a trial recording | Use "tutor, shared screen and unmuted voices; cameras off; may appear if a camera is on" |
| D15 | Retention for WhatsApp chats and portal practice answers; delivery address 30 vs 90 days | 90 days after the program ends for chats and practice answers; consider 30 days after delivery for addresses |
| D16 | How recordings are shared (named accounts vs link) | Named accounts or expiring link |
| D17 | Split the optional "improve the lessons" use from the needed feedback use | Later; low priority |
| D18 | Add version strings to the WhatsApp registration message | Yes |
| D19 | Ask MOE whether registration is needed; keep the answer in writing | Do this week, free |
| D20 | Use a lawyer or not | See 1.1: do the self-fixes, then pay for the six-item fixed-fee review |

---

## Sources

All searches run 23 Oct 2026. Primary sources are named; secondary sources are marked. Verify against the official pages.

- PDPC, Advisory Guidelines on the PDPA for Children's Personal Data in the Digital Environment, 28 Mar 2024 (PDPC PDF; summarised by Bird & Bird, Rajah & Tann, CMS, Norton Rose Fulbright; secondary summaries). https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/advisory-guidelines/advisory-guidelines-on-the-pdpa-for-children's-personal-data-in-the-digital-environment_mar24.pdf
- PDPC Advisory Guidelines on the PDPA for Selected Topics, Chapter 8 (minors; age 13), 9 Oct 2019: https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Advisory-Guidelines/AG-on-Selected-Topics/Chapter-8-9-Oct-2019.pdf
- PDPC, Register Your Data Protection Officer (DPO); homepage notice that BizFile+ DPO registration was unavailable from 1 Dec 2024: https://pdpc.gov.sg/overview-of-pdpa/data-protection/business-owner/data-protection-officers (page could not be opened directly; content from search summary)
- PDPA data breach notification, effective 1 Feb 2021: PwC and law-firm summaries (secondary): https://www.pwc.com/sg/en/personal-data-protection/assets/pdpa-updates-202011.pdf and https://www.dataprotectionreport.com/2021/02/amendments-to-the-personal-data-protection-act-in-force
- PDPC Advisory Guidelines on Key Concepts, Transfer Limitation (ch 19, 2017) and Retention Limitation (ch 18, 9 Oct 2019): https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Advisory-Guidelines/AG-on-Key-Concepts/Chapter-18-9-Oct-2019.pdf and https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Advisory-Guidelines/the-transfer-limitation-obligation---ch-19-(270717).pdf
- PDPC Advisory Guidelines on Key Concepts, Chapter 15 (access and correction), 9 Oct 2019: https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Advisory-Guidelines/AG-on-Key-Concepts/Chapter-15-9-Oct-2019.pdf
- PDPC, Do Not Call Registry and your business: https://pdpc.gov.sg/Overview-of-PDPA/Do-Not-Call-Registry/Business-Owner/Do-Not-Call-Registry-and-Your-Business
- Unfair Contract Terms Act 1977 (2020 Rev Ed), Singapore Statutes Online: https://sso.agc.gov.sg/Act/396 (statute text not opened; section 2 as reported in search results)
- Consumer Protection (Fair Trading) Act 2003, Singapore Statutes Online / MTI advisory: https://www.mti.gov.sg/resources/laws-and-regulations/general-advisory-on-amendments-to-the-consumer-protection-fair-trading-act-and-hire-purchase-act ; CCS FAQ: https://www.ccs.gov.sg/resources/faqs/consumer-protection/
- MOE, Register a private school (last updated 14 Jan 2025 per search result): https://www.moe.gov.sg/private-education/register-school (page not opened directly)
- Private Education Act 2009 and Private Education (Exemption) Order 2013: https://sso.agc.gov.sg/Act/PEA2009 (not read in detail)
- CASE CaseTrust: https://www.case.org.sg/casetrust/about-us/
- MAS payment services FAQs (loyalty points, limited purpose e-money): https://www.mas.gov.sg/contact-us/faqs/payments-faqs/payments-service-licensing-faqs
