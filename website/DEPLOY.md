# Deploying the Math Inquirers site (Cloudflare Pages)

The site is static: `website/dist/` is the whole thing. Rebuild first:

    cd website && python3 lp_build.py && python3 build_site.py --base https://YOUR-DOMAIN

## Step 1: private preview (now)
1. Create a free Cloudflare account. Dashboard > Workers & Pages > Create > Pages > Connect to Git.
2. Pick the `math-inquirers` repo and branch `claude/great-fermi-1hv4vc` (later: main).
3. Build command: `cd website && python3 lp_build.py && python3 build_site.py`. Output directory: `website/dist`. (Or skip the build and commit `website/dist`, which is already tracked: build command empty, output `website/dist`.)
4. You get a `https://<project>.pages.dev` preview URL. Protect it: Zero Trust > Access > Applications > add the `*.pages.dev` project, allow only your and Jasmine's emails.

## Step 2: go public
Do all of these first:
- Replace the `to confirm` WhatsApp number and email (CONFIG in `lp_build.py`).
- Fill the bracketed placeholders in `terms.html` / `privacy.html`, have a lawyer review, remove the draft banner.
- Pages > Custom domains > add your domain. Remove the Access rule from the public site. Rebuild with `--base https://YOUR-DOMAIN`.
- `build_site.py` prints a "To confirm before launch" list; it must be empty.
