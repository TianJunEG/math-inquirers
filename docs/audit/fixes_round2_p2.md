# Round 2 fixes: Math Inquirers Level 2 (p2), from reaudit_p2.md

Not committed or pushed. Other levels, hp/ and shared files (levels/mkextras.py, levels/scheme.py) were not edited.

## Fixes

1. **"Private chat" wording (safeguarding).**
   - p2/guide.js routine table: the warm-up row now says answers are shown on camera or kept to share, and that nothing is sent by private message. The talk-time row now invites the whole group (pass allowed), with quiet children welcome in the open session with a parent nearby, never singled out.
   - p2/gaps.json common.preSay (read aloud by the tutor, guide.js ~108): rewritten as "show your answer on your own paper to your tutor on camera, or keep it to share if you want; the tutor invites the whole group to ask in the open session; a parent can stay nearby". The paper-to-camera practice in preDo is unchanged.
   - Also fixed in docs/audit/mk_gaps_p2.py, so re-running it does not bring the old text back.
   - guide.js line ~59 (Setting up online): removed the "take a photo and send it through the approved channel" line. Now: the child may show their page on camera or keep it, and no photos of children's work are sent either way.
   - Tutor Guide PDF and Word guide were rebuilt. There are 0 "private chat" mentions and 0 "photo and send" mentions in the PDF, and 0 "private chat" in the docx.
2. **Looking back (reaudit 1.4 #2).**
   - The box is now framed as for the child.
   - A paper tick cannot be seen live, so the tutor reads journals at the next lesson while stamping.
   - If a child ticked "still stuck", the next open session starts with a whole-group invitation with a parent nearby, never one child, never by message or photo, and with no public tallies.
   - Changed in gaps.json refSay and refDo, the tick text in workbook_html.js and rebuild/p2gaps.py ("my tutor will read this at the next lesson"), and the guide.js safeguarding bullet.
3. **Investigation slot and debrief (#3).**
   - Talk time is now 72-77 and a new Investigation share runs 77-80.
   - There is a new slide p2lK-invest in all 10 decks. The setting shows first, each lettered part and the easy first step are click-revealed, and the model answer is in the notes (volunteers only, pass allowed, no tallies, take-home if nobody has started).
   - Guide: the routine table has a new 77-80 row, plus a new "Investigation share" segment with the model answer. Title-slide time plans and talk-slide labels and notes were updated.
4. **Dense slides (#21).**
   - Sneak-peek puzzles are split into one question per slide (precheck 1-2 min, precheck2 2-4 min). The text is shorter, and the question box was narrowed so it no longer touches the answer box.
   - The Go further slide is split into one item per slide (challenge, challenge2).
   - Explore go-further slide text trimmed.
   - Investigation slides use click-revealed parts.
   - Decks went from 28-35 to 31-37 slides each. The build script asserts the deck order matches the slide files.
5. **Pagination (#16).** Rendered all 64 workbook pages at low resolution. No question box is split across pages. The existing qwrap/qbox break-inside:avoid already handles it, so no code change was needed. L2 workbook page 8 and the Lesson 2 page 10 magic-square page were checked at higher resolution and are not clipped.
6. **"Hold up" wording.**
   - The exact phrase "(hold up together)" does not appear in any p2 source. It is in p3 and p6 gens, which I left alone.
   - The collective hold-ups in p2 are changed to "show your tutor on camera or keep it to share if you want". Edited in content/l2, l3, l4, l5, l9 and rebuild/gen_p2l2, l3, l4, l5, l9 (including the L9 warm-up "Show me on three").
7. **Pairs unsupervised (#6).** The guide now says to visit every breakout room by minute 47.

## Files changed (p2)

- p2/guide.js
- p2/gaps.json
- p2/workbook_html.js
- p2/content/l2.js, l3.js, l4.js, l5.js, l9.js
- rebuild/p2gaps.py
- rebuild/gen_p2l2.py, gen_p2l3.py, gen_p2l4.py, gen_p2l5.py, gen_p2l9.py
- docs/audit/mk_gaps_p2.py
- split/p2l1..p2l10 (regenerated, then restyled with levels/restyle.py)
- p2/ outputs: Workbook PDF, Tutor Guide PDF and HTML, P2_Holiday_Program_Guide.docx, Weekly PDFs zip, Weekly Dose PDF
- outputs/schemes/Math_Inquirers_P2_Scheme_of_Work.pdf (rebuilt by build_level.sh)

## Verification

- No answers changed. I re-checked the L1 Investigation figures: 10 mirror numbers from 200 to 299 and 90 from 100 to 999.
- New slides were rendered at 1920x1080. No element crosses the footer line, and no overlaps on the new slides.

## Left, and why

- Shared and other-level files carry the same wording; I did not touch them:
  - hp/guide.js line 56 has "private chat".
  - levels/mklevel.py copies p2/guide.js into p3-p6, so those guides still contain the old "private chat" and "take a photo" text until regenerated.
  - rebuild/gen_p3l3.py and rebuild/gen_p6l3.py contain "hold up together".
  - levels/scheme.py regenerated outputs/schemes P6 as a side effect of the build. That file shows as modified, though I did not edit it.
- outputs/designed/ copies for P2 (Question Bank, Weekly Email Pack and others) were not republished here.
- Gifted lift (compare-methods and spot-the-error items) and the per-lesson journey weak cells (L9-LOW jug strip, L2-LOW Q5 to Go further, L5 read-aloud, L8 cut-out nets, L10 room visits) are content additions, not defects. They are not done.
- The five tight page-2 lessons (L2, L3, L5, L8, L9) are not re-timed.
- Challenge slide 2 reuses the heading "Go further", with the item number shown in the card.
