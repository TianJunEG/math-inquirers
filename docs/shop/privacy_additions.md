# Privacy additions for soft-copy delivery (DRAFT note for privacy.html, not applied)

`website/privacy.html` is being edited by others, so this is a note, not an edit. Paste into the privacy notice in the draft bracket style once it is free, then bump the privacy version (`MI.VERSIONS` in `portal/public/common.js`) and have the lawyer review.

**What we collect when you buy a download.** Your email address (from the payment page) and your order, so we can send your download link, let you download again, and keep our records. We do not use tracking pixels in these emails. When a download link is opened we record the time, the order number and a scrambled (hashed) form of the connection address to limit abuse; we do not record your name or email in that log.

**How long we keep it.**
- Purchase records, including your email address and what you bought: [7 years] (owner's records decision; the lawyer to confirm the period and what part may be anonymised sooner).
- Download logs: [90 days].
- The download link itself stops working after [14 days] or [5] downloads.

**Who handles it for us.**
- Stripe, to take payment (already named in the notice).
- Resend, to send the email with your link (the email address and the message pass through Resend; [data may be processed outside Singapore]).
- Cloudflare, which stores the PDF files (R2) and runs the download page. The files are private; they are not stored with your personal details.
- Supabase, where order records are kept (already named).

**Licence line used in the email** (also draft for the lawyer): "These files are for your own family's personal use. Please do not share, resell or upload them."

Checks for the lawyer: transfers outside Singapore for Resend and Cloudflare; the 7 year period (the repo's `docs/terms/owner_decisions.md` does not contain a 7 year entry that I could find, so confirm it is recorded there); whether buyers must be told that the PDF files may carry an order reference (watermarking is NOT enabled, so today they do not).
