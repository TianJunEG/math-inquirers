// Cues for children who watch the recording of a live lesson. Shared by hp/guide.js and pN/guide.js.
//   cue(title, time, lesson) -> { say, action }   (time is a range like "12.5–14 min"; half minutes are kept)
//     say    = one short line the tutor says to the camera at the start of that part ("recording voice")
//     action = what the child watching later does in that part (used in the chapter table)
// Durations come from the segment's time range, so the "about N minutes" always matches the script.

// Length of the segment in minutes, to the nearest half minute, from a range such as "4–10 min" or "12.5–14 min".
const mins = (time) => {
  const m = /(\d+(?:\.\d+)?)\s*[–-]\s*(\d+(?:\.\d+)?)/.exec(time);
  return m ? Math.max(1, Math.round((+m[2] - +m[1]) * 2) / 2) : null;
};
const WORD = { 1: 'a minute', 1.5: 'a minute and a half', 0.5: 'half a minute' };
const about = (n) => {
  if (!n) return 'a few minutes';
  if (WORD[n]) return 'about ' + WORD[n];
  return 'about ' + (n % 1 ? Math.floor(n) + ' and a half minutes' : n + ' minutes');
};

const kind = (title) => {
  const s = title.toLowerCase();
  if (/sneak/.test(s)) return 'sneak';
  if (/opening/.test(s)) return 'opening';
  if (/warm/.test(s)) return 'warm';
  if (/explore/.test(s)) return 'explore';
  if (/mini-lesson/.test(s)) return 'mini';
  if (/brain break/.test(s)) return 'break';
  if (/worksheet|workbook/.test(s)) return 'work';
  if (/talk time/.test(s)) return 'talk';
  if (/exit/.test(s)) return 'exit';
  if (/look/.test(s)) return 'look';
  if (/clos|certific/.test(s)) return 'close';
  return 'other';
};

// Each "say" line is about 20 words (under ten seconds), friendly, one idea.
const CUES = {
  opening: (n) => ({
    say: 'Hello! Before you press play, get a pencil, paper, your workbook and the materials on the slide. Pause or rewind any time.',
    action: 'Gather your workbook, pencil, paper and the materials on the slide. Press play when ready.'
  }),
  sneak: (n) => ({
    say: 'Pause now and try the puzzles on your own paper for ' + about(n) + '. Guessing is fine. Press play for the answers.',
    action: 'Pause. Try the puzzles on your own paper (' + about(n) + '). Guessing is fine. Press play for the answers.'
  }),
  warm: (n) => ({
    say: 'Join in! Say or write each answer before I do. Pause the video if you need longer.',
    action: 'Play along. Say or write each answer before the video does. Pause if you need longer.'
  }),
  explore: (n) => ({
    say: 'Pause now. Try this with your objects, and a grown-up if you can, for ' + about(n) + '. Press play when you have an answer.',
    action: 'Pause. Try the explore task with your objects, with someone at home if you can (' + about(n) + '). Write down what you notice.'
  }),
  mini: (n) => ({
    say: 'Keep watching and copy the examples onto your paper. Missed a step? Rewind. You will try some yourself soon.',
    action: 'Keep watching. Copy the worked examples. Rewind any step you missed.'
  }),
  break: (n) => ({
    say: 'Movement break! Stand up and join in. The video keeps going.',
    action: 'Stand up and join the brain break.'
  }),
  work: (n) => ({
    say: 'Pause and do your workbook, starting at Start here on page 1, for ' + about(n) + '. Press play to check your work.',
    action: 'Pause. Do the workbook, starting with Start here on page 1 (' + about(n) + '). Press play for each checking part and mark in a different colour.'
  }),
  talk: (n) => ({
    say: 'Pause. Tell a grown-up your answer to the talk question, and why you think so. Then press play.',
    action: 'Pause. Explain your answer to someone at home, with a reason. Then play.'
  }),
  exit: (n) => ({
    say: 'Pause and do the exit ticket on your own, without looking back. Then press play to check it.',
    action: 'Pause. Do the exit ticket on your own, then play to check it.'
  }),
  look: (n) => ({
    say: 'Pause for ' + about(n) + ' and fill in your looking-back page: what was hardest, and what will you try next time?',
    action: 'Pause. Fill in the looking-back page.'
  }),
  close: (n) => ({
    say: 'Well done! Show your journal and workbook to a grown-up and tell them one thing you found out.',
    action: 'Show your journal and workbook to a grown-up. Tell them one thing you found out.'
  }),
  other: (n) => ({
    say: 'Pause or rewind whenever you need to.',
    action: 'Pause or rewind whenever you need to.'
  })
};

const cue = (title, time, lesson) => CUES[kind(title)](mins(time));

// Short rules for the front of the guide (used by every guide.js).
const RULES = {
  why: 'Every live lesson is recorded so that a child who misses it can still catch up. A child watching alone cannot ask you a question, so the recording needs spoken cues, visible timers and quiet working time.',
  voice: [
    'Say the short REC line at the start of each part, once, to the camera, in a friendly “recording voice”. Keep it under ten seconds. The children in the live room will simply hear it as a routine.',
    'Say the workbook page and question number aloud every time, and read each question out loud as well as showing it.',
    'Put a countdown timer or a clock slide on screen while children work, and say “the timer is running” so the recording shows how long to pause.',
    'Repeat a child’s answer in your own words before you respond, so it is clear on the recording without relying on their voice.',
    'Do not talk through the working time. Silence is fine; the child watching later pauses the video anyway.',
    'Show the answer slides clearly and read each answer aloud, so a child can mark their own work.'
  ],
  privacy: [
    'Only record on the approved platform, and only with parent consent given at registration. Do not make your own recordings or photos.',
    'Record the tutor and the shared screen only. Turn off or exclude the other children’s video in the recording (use active-speaker or screen-only recording), and keep children’s names off the screen.',
    'Do not read out a child’s name together with a right or wrong answer. Do not show a child’s page to the camera in the recording.',
    'Share the recording only through a private link to enrolled families, and delete it when the program ends, or after the period the parents agreed to.',
    'Tell the group at the start of each lesson that it is being recorded and what is recorded. A parent or child who does not wish to be in it can keep the camera off.'
  ],
  upload: [
    'Add a chapter marker at each time in the chapter list at the end of the lesson, so a child can jump to the part they need.',
    'Turn on captions if the platform offers them.',
    'Put the workbook page numbers and the materials list in the description of the recording.'
  ]
};

module.exports = { cue, kind, mins, RULES };
