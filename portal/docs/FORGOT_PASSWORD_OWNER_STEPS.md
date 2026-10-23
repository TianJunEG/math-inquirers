# Forgot-password: what the owner sets up in Supabase

The portal now has a "Forgot password?" link. It only works once you do the steps below in Supabase. Nothing here needs code or secrets. Allow about 10 minutes.

## How it works for a parent
1. On the Log in tab the parent clicks "Forgot password?" and types their email.
2. They always see the same message ("If that email has an account, a reset link is on its way"), whether or not the email exists. This protects other people's privacy.
3. They open the email, click the link, and land on the portal at a "Choose a new password" page.
4. They type a new password twice (at least 8 characters) and are logged in.

The Magic link tab still works as before.

## Step 1. Tell Supabase which addresses are allowed
Supabase only sends people back to addresses you list. If the address is missing, the reset link will send parents to the wrong place.

1. Open supabase.com and sign in. Open your Math Inquirers project.
2. In the left menu click **Authentication**, then **URL Configuration**.
3. **Site URL**: type the main address of the website, for example `https://math-inquirers.pypteltd.workers.dev` (later, your final domain).
4. Under **Redirect URLs** click **Add URL** and add each portal address, including the slash at the end:
   - `https://math-inquirers.pypteltd.workers.dev/portal/`
   - later, when you have your own domain: `https://YOUR-FINAL-DOMAIN/portal/`
5. Click **Save**.

Keep the old workers.dev address in the list until the final domain is live and tested.

## Step 2. Check the "Reset password" email wording
1. Authentication, then **Emails** (some versions: **Email Templates**).
2. Open **Reset Password**.
3. Read the subject and text. Plain, friendly wording is best, for example: "Reset your Math Inquirers password" and "Click the link below to choose a new password. If you did not ask for this, you can ignore this email."
4. Leave the link part (`{{ .ConfirmationURL }}`) exactly as it is. If it is deleted, the link stops working.
5. Click **Save**.

## Step 3. Check that emails really get sent
Supabase's built-in sender is only for testing and sends very few emails per hour. Before real parents use this, set up your own sender: Authentication, **SMTP Settings** (or Emails, then SMTP), turn on custom SMTP and fill in the details from your email provider. Ask your email provider if you are unsure what to enter. Do not share those details in chat or in the repo.

## Step 4. Try it yourself
1. Open the portal in a private/incognito window.
2. Click **Forgot password?**, enter your own email, and send.
3. Check your inbox and spam folder (can take a minute or two).
4. Click the link. You should see "Choose a new password". Set one and check you land in the portal logged in.
5. Log out and log in with the new password.

## If something goes wrong
- **No email arrives:** check spam; check Step 3 (sending limit or SMTP details); check the email address is the one used to sign up. The portal will show the same message either way.
- **The link opens the wrong page or says the link is invalid or expired:** the portal address is probably missing from Redirect URLs (Step 1), or the link is old. Links are single-use and expire; request a new one.
- **"Too many tries":** wait a few minutes. Supabase limits how often emails can be sent.
- **A parent is stuck:** they can use the Magic link tab, or message you on WhatsApp.

Not tested here: the real Supabase emails and redirect. Automated tests use a stand-in for Supabase, so Step 4 is the real check.
