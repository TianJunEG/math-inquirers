"""One-off retrofit (RETROFIT-NOW, 23 Oct 2026): add one Think harder item to lessons 7, 8, 10, 15, 17 for the thin
non-routine spots (work backwards, three-number number sentences, true/false about equal groups). Idempotent."""
import json, os
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(n):
    p = os.path.join(HERE, 'lessons', 'l%02d.json' % n)
    s = open(p, encoding='utf-8').read()
    d = json.loads(s)
    ind = 2 if json.dumps(d, indent=2, ensure_ascii=False) in (s, s.rstrip('\n')) else 1
    return p, d, ind, s.endswith('\n')

def save(p, d, ind, nl):
    open(p, 'w', encoding='utf-8').write(json.dumps(d, indent=ind, ensure_ascii=False) + ('\n' if nl else ''))

def add(n, item, move, stuck):
    p, d, ind, nl = load(n)
    if any(q['id'] == item['id'] for q in d['tiers']['think']):
        return
    d['tiers']['think'].append(item)
    d['contest_moves'].append(move)
    for seg in d['script']['segments']:
        for ln in seg.get('lines', []):
            if ln.get('k') == 'STUCK' and (ln['text'].startswith('Think harder') or ln['text'].startswith('Q')):
                ln['text'] += (' ' if ln['text'].startswith('Think harder') else ' Think harder ') + stuck
                break
        else:
            continue
        break
    else:
        raise SystemExit('no STUCK Think harder line in %d' % n)
    save(p, d, ind, nl)

P = lambda l, t, a, v: {'l': l, 'text': t, 'ans': a, 'val': v}

add(7, {
    'id': 'T5', 'page': 3, 'tier': 'think',
    'text': 'Mei had some beads. She gave away 23 beads. Now Mei has 45 beads. How many beads did Mei have at first?',
    'parts': [P('', 'Mei had ___ beads at first.', '68', 68)],
    'answer': '68 beads (45 + 23 = 68)',
    'val': [68],
    'hint': 'Mei gave 23 beads away and still has 45. Draw the beads she gave away next to the beads she kept. Put them together.',
    'solution': 'Mei gave away 23 beads and has 45 left. The beads she gave away and the beads she kept were all her beads at first. 45 + 23 = 68. Check: 68 take away 23 is 45.',
    'mistakes': ['Taking away: writing 45 - 23 = 22.', 'Writing 45 (the beads she has now).', 'Adding the tens and ones wrongly (45 + 23 = 58 or 78).'],
    'mins': 4, 'lines': 2},
    'work backwards: a take-away story with the start unknown (T5)',
    'T5: draw the beads she gave away and the beads she kept, then put them together.')

add(8, {
    'id': 'T5', 'page': 3, 'tier': 'think',
    'text': 'Use the three numbers 6, 9 and 15. The biggest number, 15, is the whole. Fill in the number sentences.',
    'parts': [P('a', '6 + 9 = ___', '15', 15),
              P('b', '9 + ___ = 15', '6', 6),
              P('c', '15 - 6 = ___', '9', 9),
              P('d', '15 - ___ = 6', '9', 9),
              dict(P('e', 'Ali writes 9 - 6 = 15. Is it true? Circle Yes or No.', 'No', 'No'), choices=['Yes', 'No'])],
    'answer': '15, 6, 9, 9, No (9 - 6 = 3; the whole, 15, goes first in a take-away)',
    'val': [15, 6, 9, 9, 'No'],
    'hint': 'Two small numbers make the big one: 6 and 9 make 15. To take away, start at the big number, 15.',
    'solution': '6 + 9 = 15. 9 + 6 = 15, so the blank in (b) is 6. Taking one part from the whole leaves the other part: 15 - 6 = 9 and 15 - 9 = 6, so the blank in (d) is 9. Ali is not right: 9 - 6 = 3, not 15. The whole, 15, is the number you start from when you take away.',
    'mistakes': ['Writing 9 in (b) because 9 is in the line.', 'Writing 6 in (d) because 6 is on the right.', 'Saying Yes to (e) because the same three numbers are used.'],
    'mins': 5, 'lines': 0},
    'three numbers, four true number sentences: the whole and its two parts (T5)',
    'T5: say the whole and the two parts. Two parts make the whole; take a part from the whole to find the other part.')

add(10, {
    'id': 'T5', 'page': 3, 'tier': 'think',
    'text': 'Lily had some stamps. She gave 8 stamps to Ravi. Then her aunt gave her 5 stamps. Now Lily has 20 stamps. Go backwards from 20 to find how many stamps Lily had at first.',
    'parts': [P('a', 'Before her aunt gave her 5 stamps, Lily had ___ stamps.', '15', 15),
              P('b', 'At first Lily had ___ stamps.', '23', 23)],
    'answer': '15 stamps, then 23 stamps at first (20 - 5 = 15, 15 + 8 = 23)',
    'val': [15, 23],
    'hint': 'Start at 20, the end of the story. Undo the last step first: her aunt gave her 5, so take 5 away. Then undo the step before it.',
    'solution': 'The last step was gaining 5, so before it Lily had 20 - 5 = 15. The first step was giving away 8, so before it Lily had 15 + 8 = 23. Check by going forwards: 23 - 8 = 15, then 15 + 5 = 20.',
    'mistakes': ['Adding 8 and 5 to 20 (33).', 'Doing both steps the same way, for example 20 - 5 - 8 = 7.', 'Undoing the steps in the story order instead of backwards.'],
    'mins': 4, 'lines': 2},
    'work backwards: a two-step "at first" story, one operation per step (T5)',
    'T5: start at the end of the story and undo the last step first.')

add(15, {
    'id': 'T5', 'page': 3, 'tier': 'think',
    'text': 'Mei has 15 apples. She puts them equally onto plates, with none left over. Is each sentence true or false?',
    'parts': [],
    'tf': [{'s': 'She can use 3 plates.'}, {'s': 'She can use 4 plates.'}, {'s': 'She can use 5 plates.'}],
    'lines': 0,
    'answer': 'True, False, True (3 plates of 5, 4 plates leave 3 over, 5 plates of 3)',
    'val': ['True', 'False', 'True'],
    'hint': 'Count in jumps of the number of plates, or deal the apples out one at a time. Does the count land on 15?',
    'solution': '3 plates: 3 groups of 5 is 15, so true. 4 plates: 4, 8, 12, 16 jumps over 15 (3 groups of 4 is 12 and 3 are left over), so false. 5 plates: 5 groups of 3 is 15, so true.',
    'mistakes': ['Saying true for 4 plates because 4 is a small number.', 'Not checking that nothing is left over.'],
    'mins': 4},
    'true or false about equal groups: can 15 be put equally onto 3, 4 or 5 plates? (T5)',
    'T5: deal the apples onto the plates, or count in jumps. Is there any left over?')

add(17, {
    'id': 'T5', 'page': 3, 'tier': 'think',
    'text': 'Kumar has 16 marbles. He shares them equally among children, with none left over. Is each sentence true or false?',
    'parts': [P('', 'If Kumar shares 16 marbles among 3 children, ___ marbles are left over.', '1', 1)],
    'tf': [{'s': 'He can share them among 3 children.'}, {'s': 'He can share them among 4 children.'}, {'s': 'He can share them among 6 children.'}],
    'lines': 0,
    'answer': 'False, True, False; 1 marble is left over when 16 are shared among 3 children',
    'val': ['False', 'True', 'False', 1],
    'hint': 'Deal the marbles out one at a time to the children, or count in jumps: 3, 6, 9 ... Does the count land on 16?',
    'solution': 'Among 3 children each gets 5, which uses 15 marbles, and 1 is left over, so false. Among 4 children each gets 4, because 4 groups of 4 is 16, so true. Among 6 children each gets 2, which uses 12 marbles, and 4 are left over, so false.',
    'mistakes': ['Saying true because the marbles can be shared "nearly" equally.', 'Forgetting that none may be left over.'],
    'mins': 4},
    'true or false about sharing equally: can 16 be shared among 3, 4 or 6 with none left over? (T5)',
    'T5: deal the marbles out one at a time. If any are left over, the sentence is false.')
print('ok')
