"""DRAFT, NOT PUBLISHED. Builds the prototype FREE PREVIEW CLASS deck for Level 3 (ages 8-10), 60 minutes.
Output: split/preview_l3/project/deck.json + project/slides/*.html (same structure as split/l6s, the 60-minute trial deck).
Writes slides in the PRE-restyle form; then run:  python3 levels/restyle.py split/preview_l3   (twice; the second run changes 0 files).
Mi (title / break / last slide only) is added here with mi_deco.put() and a PENDING placeholder image (no asset is uploaded or published).
Run:  python3 split/preview_l3/gen_preview_l3.py
"""
import os, json, html, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'levels'))
import mi_deco
OUT = os.path.join(HERE, 'project'); SL = os.path.join(OUT, 'slides')
K = 'pv3'
FOOT = 'DRAFT, NOT PUBLISHED  •  Math Inquirers free preview class, Level 3  •  Notice it. Test it. Explain why.'
LIGHT = "background:#FFF9EC;color:#1B2A49;font-family:'Nunito Sans', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;gap:28px"
NAVY = "background:#1B2A49;color:#FFF9EC;font-family:'Nunito Sans', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px"
TEAL = "background:#1F7A6F;color:#FFF9EC;font-family:'Nunito Sans', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px"
CARD = "background:#FFFFFF;border-radius:24px;padding:36px 40px;display:flex;flex-direction:column;gap:14px"
E = html.escape
def p(t, size=38, w=600, extra=''): return f'<p style="font-size:{size}px;font-weight:{w};{extra}">{t}</p>'
def card(*inner, extra=''): return f'<div style="{CARD};{extra}">' + ''.join(inner) + '</div>'
def label(t, bg='#1F7A6F', fg='#FFF9EC'): return f'<p style="align-self:flex-start;background:{bg};color:{fg};border-radius:999px;padding:8px 24px;font-size:28px;font-weight:700">{t}</p>'
def reveal(inner): return f'<div data-build-in="pop" style="background:#FFC93C;border-radius:20px;padding:18px 26px;display:flex;flex-direction:column;gap:8px">{inner}</div>'
def light(sid, pill, title, body, notes):
    return (f'<section id="{sid}" data-transition="fade" style="{LIGHT}">\n'
      f'<p style="position:absolute;right:128px;top:64px;font-size:28px;font-weight:700;letter-spacing:2px;color:#1F7A6F">{pill} MIN</p>\n'
      f'<h2 style="font-family:\'Fredoka\', Arial, sans-serif;font-size:68px;font-weight:600;line-height:1.1">{title}</h2>{body}\n'
      f'<p style="position:absolute;left:128px;bottom:64px;width:1500px;font-size:24px;color:#5B6785">{FOOT}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def dark(sid, kind, head, body, notes):
    st = NAVY if kind == 'navy' else TEAL; sub = '#B7C3DD' if kind == 'navy' else '#D7EFEA'
    return (f'<section id="{sid}" data-transition="fade" style="{st}">\n{head}{body}\n'
      f'<p style="position:absolute;left:128px;bottom:64px;width:1500px;font-size:24px;color:{sub}">{FOOT}</p>\n<aside>{E(notes)}</aside>\n</section>\n')

def machine(rows):
    """rows: list of (y, [labels]) -> boxes joined by arrows"""
    out = '<svg viewBox="0 0 1600 330" xmlns="http://www.w3.org/2000/svg" style="width:1600px;height:330px" role="img" aria-label="Number machine going forward, then undone backwards">'
    for y, labs, col in rows:
        x = 20
        for i, t in enumerate(labs):
            w = 230
            out += f'<rect x="{x}" y="{y}" width="{w}" height="110" rx="22" fill="{col[i]}" stroke="#1B2A49" stroke-width="5"/>'
            out += f'<text x="{x+w/2}" y="{y+72}" font-size="52" font-weight="800" text-anchor="middle" fill="#1B2A49" font-family="Fredoka, Arial">{t}</text>'
            if i < len(labs) - 1:
                out += f'<path d="M{x+w+14} {y+55} L{x+w+110} {y+55}" stroke="#1B2A49" stroke-width="7" fill="none"/><path d="M{x+w+110} {y+55} l-24 -16 m24 16 l-24 16" stroke="#1B2A49" stroke-width="7" fill="none" stroke-linecap="round"/>'
            x += w + 130
    return out + '</svg>'

S = []   # (id, html)
add = lambda sid, h: S.append((f'{K}-{sid}', h))

# 1 title (0-2)
add('title', dark(f'{K}-title', 'navy',
  '<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:#FFC93C">FREE PREVIEW CLASS  •  AGES 8-10  •  0–2 MIN</p>'
  '<h1 style="font-family:\'Fredoka\', Arial, sans-serif;font-size:128px;font-weight:600;line-height:1.05">The Mystery Number</h1>'
  '<p style="font-size:44px;color:#C9D4EC">Work backwards to find a hidden number</p>',
  '<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:#FFC93C">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">Crack mystery-number puzzles by undoing the steps, one at a time, and explain why it works. Answer in the chat box.</p></div>'
  '<p style="font-size:30px;font-weight:700;color:#FFC93C">DRAFT, NOT PUBLISHED. Prototype for owner review.</p>',
  'DRAFT, NOT PUBLISHED. Minutes 0 to 2. Waiting room is open from T-10; admit only parents with a registered name (see tutor SOP docs/owner_kit/preview_class_sop.md). Welcome by first name only. Say: Hello, I am [tutor first name]. This is a free preview lesson for children aged about 8 to 10, with a grown-up next to you. Today is a taste of how we teach: we notice, test and explain. Today there are no workbooks, only this screen and the chat box. Say once: this class is NOT recorded, and children cameras and microphones stay off (design section 4: no recording at all). Keep the pace warm and brisk.'))

# 2 rules (2-4)
add('rules', light(f'{K}-rules', '2–4', 'How we answer today',
  card(label('IN THE CHAT BOX'),
       p('Type your <b>first name or a nickname</b> and your answer. Never your surname, school, address or phone.', 38),
       p('We wait, then reveal together. A wrong answer is a good clue. Nobody is marked.', 34, 600, 'color:#3B4A6B'))
  + card(p('Cameras and microphones stay <b>off</b> for children. Grown-ups: please sit with your child, and no screenshots or recordings.', 36),
         p('Emoji votes: 👍 means A, ❤️ means B, 😮 means C.', 36)),
  'Minutes 2 to 4. Read the three rules aloud. Practice once: Type your nickname and a 👍 in the chat. Thank everyone by first name from the chat only. Chat is host-controlled: only the host and co-host read it aloud; delete any message with personal details at once and remind kindly. If a child is not typing, a parent may type for them. No child is asked to speak.'))

# 3 warm-up (4-9) rotating teaser
add('warm', light(f'{K}-warm', '4–9', 'Warm-up of the week',
  label('CHANGES EVERY WEEK  •  FROM THE DAILY TEASERS', '#FFC93C', '#1B2A49')
  + card(p('A train leaves at 7:48 and arrives at 9:15. How many minutes is the journey?', 46, 700),
         p('Type your answer in the chat. Think first: 7:48 to the next whole hour is how many minutes?', 32, 600, 'color:#3B4A6B'))
  + reveal(p('87 minutes.  7:48 to 8:00 is 12, 8:00 to 9:00 is 60, 9:00 to 9:15 is 15.  12 + 60 + 15 = 87.', 36, 800)),
  'Minutes 4 to 9. THIS SLIDE ROTATES WEEKLY: replace the puzzle with that week\'s Level 3 daily teaser from website/teasers (this example is the L3 teaser for 1 Nov, answer 87, verified in the teaser bank). The rest of the lesson never changes. Give 90 seconds of silent thinking, then read answers from the chat by first name, with no right or wrong said about a name. Click to reveal. Ask: who counted on to the next whole hour first? Show of hands by emoji 👍.'))

# 4 notice (9-14)
add('notice', light(f'{K}-notice', '9–14', 'Notice it: I am thinking of a number',
  card(label('MYSTERY NUMBER'),
       p('I think of a number. I <b>multiply it by 4</b>. Then I <b>add 6</b>. My answer is <b>38</b>.', 46, 700),
       p('What number am I thinking of? Type your guess in the chat.', 36, 600, 'color:#3B4A6B'))
  + card(p('Which is easier: guess and check, or something cleverer? Vote: 👍 guess and check   ❤️ something cleverer.', 34)),
  'Minutes 9 to 14. Read the puzzle slowly twice. Collect guesses for 60 seconds. Read three guesses aloud by first name and check each one on the board (a guess of 5 gives 26, too small; 10 gives 46, too big). Do not reveal 8 yet. Run the emoji vote. Say: guessing works, but let us find a way that always works.'))

# 5 test (14-19)
add('test', light(f'{K}-test', '14–19', 'Test it: guess and check, or undo?',
  card(label('TEST'),
       '<table style="font-size:38px;border-collapse:collapse"><tr><th style="text-align:left;padding:6px 24px">My guess</th><th style="text-align:left;padding:6px 24px">× 4</th><th style="text-align:left;padding:6px 24px">+ 6</th><th style="text-align:left;padding:6px 24px">Is it 38?</th></tr>'
       '<tr><td style="padding:6px 24px">5</td><td style="padding:6px 24px">20</td><td style="padding:6px 24px">26</td><td style="padding:6px 24px">too small</td></tr>'
       '<tr><td style="padding:6px 24px">10</td><td style="padding:6px 24px">40</td><td style="padding:6px 24px">46</td><td style="padding:6px 24px">too big</td></tr>'
       '<tr style="background:#FFC93C"><td style="padding:6px 24px"><b>8</b></td><td style="padding:6px 24px">32</td><td style="padding:6px 24px">38</td><td style="padding:6px 24px"><b>yes!</b></td></tr></table>')
  + card(p('Now the clever way: <b>undo</b> the steps. 38 − 6 = 32.  32 ÷ 4 = 8.', 42, 700),
         p('Why does it work? Subtracting undoes adding. Dividing undoes multiplying.', 34, 600, 'color:#3B4A6B')),
  'Minutes 14 to 19. Fill the table together; reveal row 3 with a click. Then show the undo way. Ask in chat: what undoes + 6? What undoes × 4? Type your words. Accept "minus 6", "take away 6", "divide by 4". Praise explanations, not speed.'))

# 6 key idea (19-23)
add('key', light(f'{K}-key', '19–23', 'Key idea: undo in reverse order',
  card(machine([(10, ['?', '× 4', '+ 6', '38'], ['#FFFFFF', '#E6F2EC', '#E6F2EC', '#FFFFFF']),
                (190, ['38', '− 6', '÷ 4', '8'], ['#FFFFFF', '#FFF3CC', '#FFF3CC', '#FFC93C'])]))
  + card(p('Go <b>backwards</b>: last step first, and use the opposite each time.', 42, 700),
         p('Check by going forward again: 8 × 4 = 32, 32 + 6 = 38. ✓', 34, 600, 'color:#3B4A6B')),
  'Minutes 19 to 23. Top row is the forward machine (start with the mystery number, times 4, plus 6, gives 38). Bottom row is the undo machine: start at 38, take away 6, divide by 4, and arrive at 8. The last step forward is the first step undone. Say the key idea together. The check step is part of the habit: always put the answer back in.'))

# 7 try 1 (23-28)
add('try1', light(f'{K}-try1', '23–28', 'Your turn: puzzle 1',
  card(label('TRY IT'), p('I think of a number. I <b>multiply it by 3</b>. Then I <b>add 5</b>. My answer is <b>26</b>.', 46, 700),
       p('Undo it, then type your number in the chat. Then check it by going forward.', 34, 600, 'color:#3B4A6B'))
  + reveal(p('26 − 5 = 21,  21 ÷ 3 = 7.  Check: 7 × 3 = 21, 21 + 5 = 26. ✓   The number is 7.', 38, 800)),
  'Minutes 23 to 28. Two minutes of quiet working on own paper at home (their own scrap paper, nothing is collected). Read answers from the chat by first name. Reveal. Answer: 7. Common slip: dividing 26 by 3 first (not a whole number: a clue that the order is wrong). Ask: who noticed 26 does not divide by 3? Emoji 👍.'))

# 8 break (28-31)
add('break', dark(f'{K}-break', 'teal',
  '<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:#FFC93C">28–31 MIN</p><h2 style="font-family:\'Fredoka\', Arial, sans-serif;font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>',
  '<p style="font-size:48px;font-weight:600">Stand up, stretch up high, and take three slow breaths.</p><p style="font-size:36px;color:#D7EFEA">Then a sip of water. Back in 3 minutes.</p>',
  'Minutes 28 to 31. Three minutes. Keep the screen on this slide. Host: use the pause to admit nobody new (the room is closed after minute 10, SOP) and to delete any chat messages with personal details.'))

# 9 spot the mistake (31-36)
add('spot', light(f'{K}-spot', '31–36', 'Spot the mistake',
  card(label('ANA\'S PUZZLE'), p('I think of a number. I <b>multiply by 5</b>. Then I <b>subtract 4</b>. My answer is <b>41</b>.', 40, 700),
       p('Ana wrote:  41 ÷ 5 …  hmm, it does not come out evenly. So she wrote  41 − 4 = 37.', 32, 600, 'color:#3B4A6B'), extra='padding:24px 40px')
  + card(p('What went wrong? Vote:', 34, 700),
         p('👍  A: She undid the steps in the wrong order.', 32), p('❤️  B: She subtracted 4 again, but subtracting is undone by adding.', 32), p('😮  C: Nothing is wrong.', 32))
  + reveal(p('Both A and B are true! Right way: 41 + 4 = 45,  45 ÷ 5 = 9.  Check: 9 × 5 = 45, 45 − 4 = 41. ✓', 30, 800)),
  'Minutes 31 to 36. Poll by emoji (or by typing A, B or C). Expect a split between A and B: celebrate that both are true (she started with the wrong step, then used the wrong opposite). Read two reasons from the chat. Answer 9. This slide teaches that mistakes are useful clues. Do not name any child as having made this mistake.'))

# 10 try 2 (36-42)
add('try2', light(f'{K}-try2', '36–42', 'Your turn: puzzle 2',
  card(label('TRY IT'), p('I think of a number. I <b>add 9</b>. Then I <b>multiply by 5</b>. My answer is <b>70</b>.', 46, 700),
       p('Which step do you undo first? Type your number in the chat.', 34, 600, 'color:#3B4A6B'))
  + reveal(p('Undo the last step first: 70 ÷ 5 = 14.  Then 14 − 9 = 5.  Check: 5 + 9 = 14, 14 × 5 = 70. ✓   The number is 5.', 36, 800)),
  'Minutes 36 to 42. Quiet working 2 minutes. The order is different from puzzle 1 (add first, multiply last), so undoing starts with divide. Read answers from the chat. Answer: 5. Ask: how did you know to divide first? Type your reason.'))

# 11 challenge (42-48)
add('challenge', light(f'{K}-challenge', '42–48', 'Go further: a three-step mystery',
  card(label('CHALLENGE', '#FFC93C', '#1B2A49'), p('I think of a number. I <b>double it</b>. I <b>add 7</b>. Then I <b>multiply by 3</b>. My answer is <b>57</b>.', 44, 700),
       p('Type your number. Brave extra: could my answer ever be 39 if I multiply by 4 and add 6? Type yes or no, and why.', 32, 600, 'color:#3B4A6B'))
  + reveal(p('57 ÷ 3 = 19.  19 − 7 = 12.  12 ÷ 2 = 6.  Check: 6 × 2 = 12, 12 + 7 = 19, 19 × 3 = 57. ✓', 34, 800))
  + reveal(p('Extra: 39 − 6 = 33, and 33 ÷ 4 is not a whole number, so no whole number works.', 32, 700)),
  'Minutes 42 to 48. Give 3 minutes. Many will not finish: say that is fine, the aim is to find a way in. Reveal the first answer (6) at minute 46, then the extra (no whole number: 33 is not in the 4 times table) at 47. Praise anyone who explains why in chat. Never rank. These are original puzzles for this class; keep them out of the daily teaser bank.'))

# 12 recap (48-50)
add('recap', light(f'{K}-recap', '48–50', 'What we did today',
  card(label('NOTICE IT'), p('We spotted a hidden number behind steps.', 38),
       label('TEST IT'), p('We tried guesses, then found a way that always works.', 38),
       label('EXPLAIN WHY'), p('We used opposites, in reverse order, and checked at the end.', 38)),
  'Minutes 48 to 50. Ask three children by chat: type one word you remember. Read three words aloud.'))

# 13 what a class is like (50-53) offer 1
add('class', light(f'{K}-class', '50–53', 'If you would like more',
  card(label('OUR CLASSES'),
       p('Live online in small groups of up to 8 children, with a tutor.', 38), p('Ten lessons of 90 minutes. Hands-on, with a printed workbook posted to your home.', 38),
       p('Every lesson has the same four steps you saw today: notice, test, check, explain.', 38))
  + card(p('Not sure which level? Our free Placement Check helps you pick. You decide, and you can change level before lesson 1.', 34, 600, 'color:#3B4A6B')),
  'Minutes 50 to 53. Offer segment, part 1. Soft and honest: no countdown, no scarcity, no pressure, no comparison with other children, no claims about exams or schools. Say: This was a taste. Our regular classes are longer and use workbooks; if it was not for you, that is completely fine. Do not mention prices if the owner has not published them (prices on hold); say details are on the website. [Owner to confirm the exact wording before use.]'))

# 14 next step (53-55) offer 2
add('offer', light(f'{K}-offer', '53–55', 'Your next step, if you want one',
  card(label('GROWN-UPS ONLY'),
       p('Book a <b>free trial class</b> or ask a question: [registration page link; domain to be decided].', 38),
       p('Or reply to our message after today. We will only message you if you tick the box on the registration form, and you can say STOP at any time.', 34, 600, 'color:#3B4A6B'))
  + card(p('Children: you do not need to do anything. You were great today.', 38, 700)),
  'Minutes 53 to 55. Offer segment, part 2. Address the parents, not the children. The page/link is typed into the chat by the host, never spoken as a short link to an unknown domain. Say there is no obligation; that the preview can only be attended once per child in six months; the trial class and next steps are the same for everybody. Do not push. Take questions in chat, answer the general ones aloud, say private ones will be answered by email or WhatsApp.'))

# 15 take-home (55-58)
add('takehome', light(f'{K}-takehome', '55–58', 'Take-home: free practice page',
  card(label('FREE, NO LOGIN, NOTHING SAVED'), p('A one-page <b>Mystery Number</b> practice sheet with answers and worked solutions.', 42, 700),
       p('[Link: /practice/sample/l3/ to be built; the host pastes it in the chat at the end.]', 34, 600, 'color:#3B4A6B'))
  + card(p('Try two puzzles with someone at home. Can you make up a mystery number for them?', 38)),
  'Minutes 55 to 58. Paste the link in the chat. The sample page is open, stores nothing, has no timer or score (see design section 3.8). Ask: type one thing you will tell someone at home. Read a few.'))

# 16 end (58-60) not a question slide
add('end', dark(f'{K}-end', 'navy',
  '<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:#FFC93C">58–60 MIN</p><h2 style="font-family:\'Fredoka\', Arial, sans-serif;font-size:110px;font-weight:600;line-height:1.05">Thank you!</h2>',
  '<p style="font-size:44px;font-weight:600;max-width:1300px">Great thinking today. Notice it. Test it. Explain why.</p><p style="font-size:32px;color:#C9D4EC">Grown-ups: we will close the room now. Please leave when you are ready.</p>',
  'Minutes 58 to 60. Say goodbye. Host closes the meeting for everyone (End meeting for all), then ticks attendance sheet and notes numbers (SOP). No recordings were started. Stay 5 minutes for private questions only if a second adult (co-host) is present.'))

def main():
    os.makedirs(SL, exist_ok=True)
    order = []
    for sid, h in S:
        order.append(sid)
        h = h if h.endswith('\n') else h + '\n'
        open(os.path.join(SL, sid + '.html'), 'w', encoding='utf-8').write(h)
    # Mi: title, break, last only (same rule and placement as levels/mi_deco.py); PENDING placeholder, no uploaded asset.
    plan = {order[0]: 'hello_wave', [i for i in order if i.endswith('-break')][0]: 'stretch', order[-1]: 'goodbye_wave'}
    for sid, pose in plan.items():
        f = os.path.join(SL, sid + '.html'); a = open(f, encoding='utf-8').read()
        open(f, 'w', encoding='utf-8').write(mi_deco.put(a, pose, '3', f'/_blob/PENDING-{pose}', sid))
    deck = {"v": 4, "createdOnFiles": {"v": 1, "at": "2026-10-24T12:00:00Z"}, "lists": "css",
            "title": "DRAFT, NOT PUBLISHED: Math Inquirers free preview class, Level 3 (60 minutes)",
            "order": order, "cover": order[0],
            "sections": {"s1": {"description": "Welcome and warm-up of the week", "start": order[0]},
                         "s2": {"description": "Notice, test, key idea, try", "start": f'{K}-notice'},
                         "s3": {"description": "Break, spot the mistake, try, challenge, recap", "start": f'{K}-break'},
                         "s4": {"description": "Offer, take-home, goodbye", "start": f'{K}-class'}},
            "faces": {"fredoka": {"family": "Fredoka", "href": "https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap"},
                      "nunito-sans": {"family": "Nunito Sans", "href": "https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap"}},
            "designSystems": []}
    json.dump(deck, open(os.path.join(OUT, 'deck.json'), 'w'), indent=1)
    print(len(order), 'slides')
if __name__ == '__main__': main()
