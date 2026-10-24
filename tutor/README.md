# Tutor console

The tutor runs a lesson from two devices that stay in sync:

- **Laptop: lesson screen** (`/screen.html?lesson=p4l3`). Shows the slide and a running timer for the current part. This is the window the tutor shares in the video call. It never receives speaker notes or answers.
- **Phone: remote** (`/remote.html`). The tutor types the 4-letter code shown on the lesson screen. The phone shows the clock, the notes for the current slide, the SAY / DO / IF STUCK lines for the current part, and buttons for next, back, start or pause, +1 minute, skip optional slide, next part and a big timer.

The laptop owns the clock and the slide. The phone only sends commands, so if the phone drops out the lesson keeps running (arrow keys, space, `F` for the big timer, `H` to hide the code).

## Run it

    cd tutor && npm install
    python3 build_data.py          # builds data/ for Levels 1 to 6 (or: build_data.py 4) from the decks, scripts and budget.json
    node server.js                 # http://localhost:8787

## Privacy rules built in

- The screen loads `/data/<lesson>.public.json` only. Speaker notes are stripped from the slide before it is shown.
- Notes and answers (`<lesson>.notes.json`) are served to the remote only. In production they sit behind the tutor login.
- The phone code is hidden on the shared screen as soon as a phone connects, and a room accepts at most two remotes.
- The lesson screen shows "Share this window only" until `H` is pressed.

## Production

Static files plus a WebSocket room relay (`server.js` is the reference for the protocol). Planned: Cloudflare Pages and a Durable Object for the rooms, with the tutor area behind Cloudflare Access (tutors invited by email). `TUTOR_KEY` is a development guard for the notes endpoint only.

## Status

Prototype. Part budgets are read from `hp/budget.json` (Level 1) and `pN/budget.json` (Levels 2 to 6), the same files the tutor guides use, so half-minute parts (7.5 min) work. All six levels are built (60 lessons). The SAY / DO lines come from the lesson scripts; the guide's full per-part wording will replace them once the guide generator exports it.
