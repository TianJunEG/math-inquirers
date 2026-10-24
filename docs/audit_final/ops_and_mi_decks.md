# Independent audit: operations kit and Mi in the holiday decks (23 Oct 2026)

Auditor did not build these. Report only; nothing was fixed. Branch `claude/great-fermi-1hv4vc`.

## Summary

| Severity | Count | Headline |
|---|---|---|
| High | 1 | Mi is missing from all 30 Level 1 to 3 decks in the repo (`split/`); the 30 live decks still have her, so the next republish or rebuild from `split/` would remove her |
| Medium | 3 | Mi clips the "Today we will" text on 22 Level 1 to 3 title slides; Level 5 look-back Mi touches the yellow notice; message templates state recording scope as fact before it is tested |
| Low | 9 | See below |

Operations kit: all 60 lessons are correct. No blocking findings.

## Part 1. Operations kit

### Verified clean
- 60 lessons in six group files plus `all_groups_tutor.ics` (60). All parse with `icalendar` 7.3.0. 60 unique UIDs. Each is 90 minutes, `DTSTART;TZID=Asia/Singapore`, weekday matches the date, alarms at -1 day and -1 hour. `python3 ops/test_ics.py` reports ALL OK. Regenerating with `ops/make_ics.py` gives byte-identical output.
- Cross-check against `docs/schedule/beta_schedule.md` and `website/data/beta_schedule.json`, done separately from the test script:
  - L1 Tue/Fri 09:00, L2 10:45, L3 13:15, L4 15:00.
  - L5 Fri 16:45 and Sun 16:15; Fri 25 Dec moves to Wed 23 Dec; lesson 10 is Sun 27 Dec.
  - L6 Thu 18:15 and Sat 18:45, first lesson Thu 26 Nov, last Sat 26 Dec.
  - L1 to L4 week 5 Friday moves to Thu 24 Dec at the usual time.
  - First lessons are Tue 24, Thu 26 and Fri 27 Nov.
- Nothing falls on Fri 25 Dec. No other Singapore public holiday falls between 24 Nov and 27 Dec 2026. `no_lessons_on` is `["2026-12-25"]`.
- No prices in any ops file (the `.ics` files, PDFs, `.docx` files, `docs/ops`). `S$` appears nowhere. The JSON price stays out of the kit. No NRIC, address or child names. The only phone number is the business WhatsApp +65 9880 5962.
- Message templates: plain wording, no MOE, GEP or SASMO claims, no scores or comparisons. Only the tutor agreement mentions MOE, GEP and SASMO, in a prohibition (clause 7.3), which is right.
- Tutor agreement: the first line says "DRAFT FOR LAWYER REVIEW", "Not signed, not legal advice, not to be used until a Singapore lawyer has reviewed it". Open items are bracketed. Clause 3.3 matches owner decision 9 (no paper to the camera).
- All 10 PDF files (reports L1 to L6, make-up note, add-to-calendar, tutor notes, observation sheet at 2 pages) were rendered to PNG and viewed. No clipping, no overflow, no empty pages. Report lesson titles match `website/data/level_lessons.json`. The 6 `.docx` files open and carry the same text.
- Make-up note and `website/terms.html` agree (no refund for a missed lesson, recording, later class if a seat is free).

### Findings

**Medium, M1. Templates and the make-up note state recording scope as fact.**
- Where: `docs/ops/message_templates.md` template 6 ("not cameras or names"), `ops/out/makeup_note_parents.pdf` "What is in a recording", tutor agreement 3.6.
- Why: `docs/ops/launch_checklist.md` schedules the Meet recording test only on Wed 4 Nov ("check what is recorded"). Parents would be told something unverified. Suggest wording the claim as true only after that test, or flagging it as "confirm after test".

**Low, L1. Placeholder list is incomplete.**
- Where: `docs/ops/message_templates.md` header.
- Missing from the list: [time], [date], [__] working days, [Reference], [PayNow number / UEN], [old date/time], [new date/time], [Link or just reply], [one specific, kind observation], [attach L[Level]A file], [Parcel policy: owner to confirm].
- In the make-up note PDF, "[X days: owner to confirm]" sits in parent text.

**Low, L2. `.ics` files carry the placeholder "[Google Meet link to be added]".**
- No `URL:` field until the owner adds `ops/meet_links.json` and reruns.
- The parent guide says "each one lists the Google Meet link", which is true only after that step. The checklist covers this on Tue 17 Nov.
- Template 13 says an updated file "replaces the old one automatically". That needs `--sequence` raised. Google Calendar import can still duplicate. Worth a plain caution.

**Low, L3. Tutor agreement states one legal conclusion as fact.**
- Where: "Employment status", "The clauses below work either way, but tax, CPF, leave, insurance and notice differ".
- Also: 5.1 assignment and 10.2 immediate termination are drafted as operative terms without bracketing (acceptable for a draft; the lawyer note covers it).
- The only draft marker is the top status line. No per-page marker or watermark, and the signature block is live. Suggest a "DRAFT" footer so a printed copy cannot be mistaken.
- Clause 3.10 and the NRIC/FIN last-4 field are flagged for the lawyer. The PDPC advice on collecting NRIC fragments should be raised.

**Low, L4. Launch checklist names a personal-looking email.**
- `docs/ops/launch_checklist.md` Tue 27 Oct row prints "pypteltd@gmail.com". It is labelled a placeholder. The company UEN and the business WhatsApp number are public business data, so no finding there.

**Low, L5. The observation sheet uses the Level 1 budget (2/6/4/14/10/4/32/7/6/3/2) for every level.**
- The sheet says to overwrite per level, so this is a note only.

**Low, L6. Report PDF for Level 6 offers "Continue to the next term at Level 6 (Level 7 is not offered)".**
- That is internal wording on a parent-facing page. Level 1 to 5 forms say "Move up to Level N+1". Consider a plainer sentence.

## Part 2. Mi in the 60 holiday decks

Method: static scan of all 60 `split/*` decks (slide ids, pose, blob id versus `mascot/blob_ids.json`), then Chromium (Playwright, `/opt/pw-browsers/chromium`, 1920x1080) renders of every Mi slide (181 slides). A bounding-box test of the Mi image against all non-aside text and filled boxes. Contact sheets were viewed for L1 lessons 1, 5, 10; L2 lessons 1, 5, 10; L3 lessons 1, 6, 10; and L4, L5 and L6 lessons 1 or 2, 3 or 5 or 6, 7, 10. The poses sheet was viewed. For Level 1 to 3 I applied `levels/mi_deco.py` to a scratch copy, because the repo has no Mi there (see H1). No repo files were changed.

### Verified clean
- Level 4 to 6 (30 decks, repo): Mi is on exactly 3 slides each (title hello_wave, brain break stretch, last slide goodbye_wave; lesson 10 title uses map). No Mi on exit or question slides. Blob ids all match `mascot/blob_ids.json`. No overlap with text on any L4 to L6 title, break or last slide. Sizes are 170, 160 and 150 px with reduced opacity.
- No calculator: the poses (hello, stretch, goodbye, map, trophy) hold nothing but a map or trophies. No "calculator" word on any Mi slide.
- Poses are correct for the slide. The module itself works: re-running it on a scratch copy restores Mi on all 30 Level 1 to 3 decks in 3 slides each (4 for L1 lesson 10 with the trophy).
- Phone width: a landscape phone (about 844 px wide) shows Mi at 100 px (L1 to L3) and 66 to 75 px (L4 to L6), which is legible. A portrait phone (390 px) shows her at about 47 px, or 30 to 35 px and partly faded for L4 to L6. She is readable as a dolphin but not as an expression. Decorative only, so Low.
- Decision 9 wording: the decks contain no instruction to hold paper to the camera. "Nothing is held up to the camera" and "Never ask a child to hold a page or box to the camera" appear in the speaker notes of 20 to 40 decks per phrase. All 60 look-back slides carry the "I am still stuck" box. The two notes in `split/l1/project/slides/l1-try1.html` and `l5-try1.html` are prohibitions. This is consistent with `docs/terms/owner_decisions.md` item 9.
- `docs/audit/mi_in_decks_L1_3.md` and `mi_in_decks_L4_6.md` are accurate about the module and the poses. They are not accurate about the current repo state for L1 to L3 (H1).

### Findings

**High, H1. Level 1 to 3 repo decks no longer contain Mi.**
- Scope: `split/l1` to `l10`, `split/p2l1` to `p2l10`, `split/p3l1` to `p3l10` (30 decks, 0 `data-mi` images).
- Cause: commit `f24c7de` (23 Oct 06:28, "WIP checkpoint"; it added `levels/_restyle_head_tmp.py`, which is not in the tree now) removed the `<img data-mi>` lines from every Level 1 to 3 title, break and reflect slide. Mi was added in `b923990` (06:25). The restyle changes in `f24c7de` appear to have rewritten those slides without calling `mi_deco`.
- The 30 published decks still show Mi, e.g. live `l1-break` at artifact 3bJhBJ37ZoAfsuDo4LgWeH. So the repo and the live decks disagree. The next republish from `split/` removes her, which breaks owner decision 9 on Mi.
- `docs/audit/mi_in_decks_L1_3.md` ("republished in place") is now out of step with the repo.
- Suggested check: run `python3 levels/mi_deco.py split/<deck>` for each of the 30 decks and commit. It is idempotent and the blob ids are all present.

**Medium, M2. Mi covers the "Today we will" sentence on Level 1 to 3 title slides (22 slides).**
- `mi_deco.put()` adds `margin-right:150px` to the card only for Levels 4 to 6. At Level 1 to 3 Mi is 230 px and sits over the card's lower right.
- Measured text overlap: L1 l3, l5, l6 and l7; L1 l8 and l10; L2 lessons 3 and 10 (p2l3 and p2l10 map); L3 lessons 1, 3, 4, 6, 7, 8, 9 and 10 are all affected at 3 to 65 px.
- Visible clipping: "…using a|", "…making th|", "…list every number i|", "…explain our thinking" with the map covering the full stop. Lesson 10 uses the map pose, which is wider (222 px) and covers the last words.
- Also: the L1 look-back (l1, l2, l3, l8, l9, l10 reflect) has Mi over the "asking a question" tickbox label (9 x 17 px). The earlier audit note says "re-test clean" for L1 to L3, so this was either lost with H1 or was not tested at Level 1 and 2.
- Fix idea: apply the same card margin as Levels 4 to 6 to all levels, or shrink Mi to 170 px on titles.

**Medium, M3. Level 5 look-back: Mi touches the yellow privacy notice.**
- All 10 `split/p5l*/…-reflect.html`: the Mi box (1783, 942, 93x120) overlaps the yellow "Your tutor may read this privately…" strip by 61 x 34 px at its right end. The slide shows the strip running into her.
- Levels 4 and 6 are clear.

**Low, L7. Lesson 10 decks have extra Mi slides beyond "title, break, last".**
- L1 l10 has Mi on title (map), break, reflect (goodbye) and end (trophy). This is by design in the module docs, but it is two figures within two slides. All the other lesson 10 decks (L2 to L6) get map on the title and goodbye on the end slide.

**Low, L8. Level 1 lesson 1 title (l1-title.html).**
- It carries two identical "2-4 MIN" pills stacked on the "?" cloud, and a duplicated speaker-note sentence ("Parents cut out and tape the number strip before the lesson" twice). The same duplicate sentence is in `l1-explore1` and `l3-warm2`. Not Mi, but introduced in the same commit as H1.

**Low, L9. The title pill "x MIN" sits on the decorative "?" cloud in Level 1 titles (e.g. "0-2 MIN" over the "?").**
- Pre-existing, noted by the earlier agent.

**Low, L10. Level 4 break slides ("Then back to our seats on time") and Level 6 look-back lines collide with the footer or with a hidden text row in my renderer.**
- Seen in `p4l1-break`, `p4l5-break`, `p4l10-break`, and in `p6l2-reflect` and `p6l6-reflect`, where "I am still stuck…" overprints a "Write it in the Looking back box…" line.
- It could be an artefact of my wrapper (a plain 1920x1080 box). Not caused by Mi. Worth a check in the real Slides renderer.

**Low, L11. The look-back slides at Levels 1 and 2 overflow below 1080 px in my renderer ("Next time I will try…" cut off).**
- Same caveat as L10.

## Files
- `ops/make_ics.py`, `ops/test_ics.py`, `ops/make_docs.py`, `ops/out/*`, `docs/ops/*`
- `levels/mi_deco.py`, `levels/restyle.py`, `mascot/blob_ids.json`, `mascot/poses_small/`
- `docs/audit/mi_in_decks_L1_3.md`, `docs/audit/mi_in_decks_L4_6.md`
