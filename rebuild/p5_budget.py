"""Level 5 re-budget (docs/audit/timing_p5.md sections 6 and 7, applied in docs/audit/rebudget_p5.md): the ONE place where the minute plan of the ten P5 lessons lives.

  python3 rebuild/p5_budget.py     writes p5/budget.json (read by p5/guide.js for every seg() time and by the tutor console timer)
  BUD[n]['parts']     part budgets (title, start, end) on the lesson clock; every lesson sums to exactly 90 (zero-length parts are left out)
  BUD[n]['slides']    clock time of every slide in the group flow: {slide id without the 'p5lN-' prefix: (start, end)}
  BUD[n]['optional']  slides that carry no clock time ("Optional, if you finish early"): not in the tutor timer
  BUD[n]['cut']       slides taken out of the deck by this pass (never in the deck order again)
  Used by rebuild/p5_gaps.py (time pills, 'Minutes a to b' notes and the title-slide time plan of every slide, run at the end of
  each gen_p5lK.py) and by p5/guide.js.  The generators' own literals ('9-14 MIN', 'Minutes 9 to 14.') are OLD clock times and are
  overwritten there: change minutes in THIS file only.

Part budgets are the audit's proposal (section 7 table).  Exit/reflect/close is split: reflection 2.5 (75 seconds of writing plus the slide),
close 1 (the stamp is typed in the chat, goodbye), exit ticket = the rest; Lesson 10: close = certificates, 12 seconds each, 3.5.
Buffer = what the audit leaves (1 to 5 minutes), always the last part, always unscripted: the lesson is allowed to eat it.
"""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
OPT_PILL = 'Optional, if you finish early'
PARTS = ['Opening', 'Sneak-peek puzzles', 'Warm-up', 'Explore', 'Mini-lesson', 'Brain break', 'Worksheet page 1 (pairs)', 'Check page 1',
         'Short teaching before page 2', 'Worksheet page 2 (alone)', 'Check page 2', 'Talk time', 'Exit ticket, reflection and close', 'Buffer (floating time)']
KEYS = ['open', 'sneak', 'warm', 'explore', 'mini', 'brk', 'p1', 'chk1', 'teach', 'p2', 'chk2', 'talk', 'exit', 'buffer']
OPTIONAL = ['stretch', 'stretch2', 'stretch3', 'gofurther', 'gofurther2', 'gofurther3', 'challenge', 'chdiag', 'chwalk', 'teachchange', 'teachdeal']

def fmt(x):
    return ('%g' % x)

# audit section 7, one row per lesson, in KEYS order
B = {
 1: [2, 4.5, 6, 14, 11, 4.5, 14.5, 4, 3, 8, 3, 5.5, 8, 2],
 2: [2, 4.5, 6.5, 14, 11, 4, 15.5, 4, 1.5, 8, 3, 5.5, 8, 2.5],
 3: [2, 4.5, 6.5, 13.5, 12, 4, 14, 3.5, 1.5, 8, 2, 5.5, 9.5, 3.5],
 4: [2, 4.5, 6, 13, 11, 4.5, 12.5, 3.5, 3, 10, 3, 5.5, 7, 4.5],
 5: [3.5, 4.5, 6.5, 13.5, 12, 4.5, 15, 3.5, 0, 7, 2, 5.5, 8.5, 4],
 6: [2, 4, 6, 14, 12.5, 4, 14.5, 4, 1.5, 9, 3, 5.5, 8.5, 1.5],
 7: [2, 4.5, 5.5, 12.5, 11, 4.5, 14, 3.5, 1.5, 11.5, 3, 5.5, 9, 2],
 8: [2, 4, 6, 12.5, 12, 4.5, 13, 3.5, 3, 7.5, 3, 5.5, 8.5, 5],
 9: [2, 4.5, 5.5, 13.5, 11.5, 4, 14, 4, 3.5, 9, 3, 5.5, 9, 1],
 10: [2, 4.5, 6.5, 14.5, 10.5, 4, 13.5, 3, 2, 7.5, 3, 5.5, 10.5, 3],
}
# how each part is shared between its slides (minutes); a part with several slides must add up to its budget
WARM = {1: 3, 2: 3, 3: 3, 4: 2.5, 5: 3, 6: 2.5, 7: 2.5, 8: 2.5, 9: 2.5, 10: 3.5}          # warm1 (the one game round); warm2 gets the rest
EXPLORE2 = 4                                                                             # explore2 (regroup, two questions, guesses); explore1 gets the rest
MINI = {
 1: [('teach1', 2.5), ('try1', 1), ('we1', 2.5), ('try2', 1.5), ('we2', 2.5), ('key', 1)],
 2: [('teach1', 2), ('try1', 1), ('we1', 2.5), ('try2', 1.5), ('we2', 2.5), ('key', 1.5)],
 3: [('teach1', 2.5), ('try1', 2.5), ('teach2', 2.5), ('try2', 2.5), ('key', 2)],
 4: [('teach1', 2.5), ('try1', 1), ('teach2', 2.5), ('teach3', 2), ('try2', 1.5), ('key', 1.5)],
 5: [('teach1', 2.5), ('we1', 2), ('try1', 2), ('we2', 2), ('try2', 2), ('key', 1.5)],
 6: [('teach1', 2), ('we1', 2), ('try1', 1.5), ('teachfree', 2), ('we2', 2), ('try2', 1.5), ('key', 1.5)],
 7: [('teach1', 2), ('we1', 2), ('try1', 1.5), ('we2', 2), ('try2', 2), ('key', 1.5)],
 8: [('teach1', 2), ('we1', 2), ('try1', 1.5), ('teachshapes', 2), ('we2', 2), ('try2', 1.5), ('key', 1)],
 9: [('teach1', 2), ('try1', 1.5), ('we1', 2.5), ('try2', 1.5), ('we2', 2.5), ('key', 1.5)],
 10: [('teach1', 1.5), ('we1', 1.5), ('try1', 1.5), ('we2', 2), ('we3', 2), ('key', 2)],
}
TEACH = {   # the page-2 teaching slides that stay in class (the others were cut or moved to the take-home pack)
 1: [('teachest', 1.5), ('teachbrackets', 1.5)], 2: [('teachback', 1.5)], 3: [('teachdiff', 1.5)], 4: [('teachtake', 1.5), ('teachsame', 1.5)],
 5: [], 6: [('teachplans', 1.5)], 7: [('teachrem', 1.5)], 8: [('teachchain', 1.5), ('teachcombo', 1.5)],
 9: [('teachgs', 2), ('teachsup', 1.5)], 10: [('teachsq', 2)],
}
CUT = {   # slides taken out of the deck (audit section 6); their questions go to take-home
 1: ['trybrackets', 'teachfind'], 2: ['teachpattern', 'teachboth'], 3: ['trydiff', 'teachone'], 4: ['teachsplit'],
 5: ['teachlist', 'teachpaint', 'teachpour'], 6: ['teachpark'], 7: ['teachtable'], 8: ['teachcases'], 9: ['try3', 'teachmarks'],
 10: ['try2', 'teachliar', 'teachage'],
}
CLOSE = {n: (3.5 if n == 10 else 1) for n in B}
REFLECT = 2.5

def build(n):
    v = dict(zip(KEYS, B[n])); parts = []; sl = {}; t = 0.0
    for key, title in zip(KEYS, PARTS):
        d = v[key]; s = t
        if key == 'open': sl['title'] = (t, t + d)
        elif key == 'sneak': sl['check'] = (t, t + d)
        elif key == 'warm': sl['warm1'] = (t, t + WARM[n]); sl['warm2'] = (t + WARM[n], t + d)
        elif key == 'explore': sl['explore1'] = (t, t + d - EXPLORE2); sl['explore2'] = (t + d - EXPLORE2, t + d)
        elif key == 'mini':
            u = t
            for sid, m in MINI[n]: sl[sid] = (u, u + m); u += m
            assert abs(u - (t + d)) < 1e-9, (n, 'mini', u - t, d)
        elif key == 'brk': sl['break'] = (t, t + d)
        elif key == 'p1': sl['ws1'] = (t, t + d)
        elif key == 'chk1': sl['ws1ans'] = (t, t + d)
        elif key == 'teach':
            u = t
            for sid, m in TEACH[n]: sl[sid] = (u, u + m); u += m
            assert abs(u - (t + d)) < 1e-9, (n, 'teach', u - t, d)
        elif key == 'p2': sl['ws2'] = (t, t + d)
        elif key == 'chk2': sl['ws2ans'] = (t, t + d)
        elif key == 'talk': sl['talk'] = (t, t + d)
        elif key == 'exit':
            r = REFLECT; c = CLOSE[n]; e = d - r - c
            sl['exit'] = (t, t + e); sl['reflect'] = (t + e, t + e + r)
            if n == 10: sl['end'] = (t + e + r, t + d)     # certificates slide (its id has no lesson prefix)
        t += d
        if d > 0: parts.append((title, s, t))
    assert abs(t - 90) < 1e-9, (n, t)
    return dict(parts=parts, slides=sl, optional=OPTIONAL, cut=CUT[n])

BUD = {n: build(n) for n in B}

def pill(n, sid):
    a, b = BUD[n]['slides'][sid]
    return fmt(a) + '–' + fmt(b) + ' MIN'

def part(n, title):
    """(start, end) of the part whose title starts with `title`"""
    for t, s, e in BUD[n]['parts']:
        if t.startswith(title): return s, e

def optional_in_deck(n):
    """the optional slides actually present in the deck of lesson n (deck order), or the whole OPTIONAL list when the deck is not built yet"""
    dj = os.path.join(H, '..', 'split', f'p5l{n}', 'project', 'deck.json')
    if not os.path.exists(dj): return list(BUD[n]['optional'])
    order = json.load(open(dj, encoding='utf8'))['order']
    return [x.split('-', 1)[1] for x in order if x.startswith(f'p5l{n}-') and x.split('-', 1)[1] in BUD[n]['optional']]

def write_json(path=None):
    out = {'lessons': {str(n): {'parts': [{'title': t, 'start': s, 'end': e} for t, s, e in b['parts']],
                                'optional_slides': [f'p5l{n}-{x}' for x in optional_in_deck(n)]} for n, b in BUD.items()}}
    path = path or os.path.join(H, '..', 'p5', 'budget.json')
    json.dump(out, open(path, 'w'), indent=1, ensure_ascii=False)
    return out

if __name__ == '__main__':
    write_json(); print('p5/budget.json written')
