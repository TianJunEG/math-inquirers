# Holiday online practice: shared builder and runner

Build and test one lesson (any level key `p1` to `p6`, lesson 1 to 6):

    python3 practice/holiday/build_holiday.py p1 1
    python3 practice/holiday/test_holiday.py p1 1

The shared files are `practice/ext/public/sheet.js` (page runner), `practice/submit/mark.js` (server marking, same reading rules as the runner in one shared block),
`build_holiday.py`, `hlib.py`, `test_holiday.py` and `practice/submit/make_keys.py`. Lesson files (`pN/NN/lesson.py`) only describe questions.

## Go-live switch for sending answers to the tutor (SUBMIT-TO-TUTOR)

Sending is OFF by default. It is switched on in ONE place: build with `MI_SUBMIT_ENDPOINT=<url>` set.

    MI_SUBMIT_ENDPOINT=https://example.invalid/hol-send python3 practice/holiday/build_holiday.py p1 1

The page then also needs a child session token (portal sign-in). With both present the footer changes and the "I checked / I got it / Not yet" ticks show on self-check
questions. Without the endpoint or without a token nothing is sent.

The footer sentences are the constants `FOOT_OFF` ("Your answers stay on this device.") and `FOOT_ON` ("Your answers, and what you write in the explanation boxes, are sent to your tutor
so they can help you.") at the top of `build_holiday.py`; the builder writes them into every page as `window.MI_FOOT`, and `sheet.js` shows the true one. Change the wording there only.

**The footer (privacy) wording needs the owner's and a lawyer's sign-off before go-live.** Nothing here has been approved: the sentences describe what the code does, they are not legal advice.
`test_holiday.py` (section 2d) builds with an endpoint and checks that the footer then says the answers are sent to your tutor and that the ticks show, and that without the endpoint they do not.

## Item flags and lesson fields added in week 3

- `label` on an item: the short nav button text. A label that is long or cryptic (contains `?`, a digit-letter-digit such as `8c4`, or is longer than 12 characters) is shown as its number only
  (`Inv 8c4 yes?` shows `Inv 8c`, `G5 any no.?` shows `G5`); the full label and the printed number are in the button's accessible name. Visible text always starts the accessible name and every name is unique.
  Take-home questions show `TH`.
- A title repeated by the question text (`Take-home. Take-home (...)`, `Make up your own. Make up your own: ...`) is shown once by the runner; no lesson change needed.
- `VARIANTS[id]['tpl']['fig']`: an SVG template with the same `{name}` places as the question, drawn for the variant ("Try a similar one"). Or `VARIANTS[id]['fig'] = fn(env) -> svg` (at most 600 combinations, stored as `tpl.figs`).
  If a variant has no figure the first question's picture is hidden while the variant is shown; `tpl['paper'] = True` adds "Draw it on paper if it helps." only where that is needed.
- `accept_prefix=False` (text items): do not ignore "It is ...", "It will be ...", "The answer is ..." before the answer (default: ignored). A list of strings adds more lead-ins.
- Number items accept a unit and up to two more plain words after the number ("27 liters of water", "35 cents change") unless `unit=False`; "$0.35" is never read as 35 cents.
- Shared reading of text answers: "a is equal to b" for "a = b"; "A and B and D" for "A, B, D" (single letters, numbers or fractions only); "1 out of 4" for 1/4 when the item has `equiv_frac` (or type `fraction`);
  "angle AOC = 90" and "∠AOC = 90°" before an angle number (not with `unit=False`).
