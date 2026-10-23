"""Data checks on the schedule/interest sources (no browser needed).
Run: python3 website/tests/slots_data_test.py
Owner decisions 23 Oct 2026: late 2027 options (Thu 7:30pm, Sun 7:15pm) are Levels 5 and 6 only;
Sunday 2:00pm is not available; reserve week-5 lessons for R1-R3 move to Wed 23 Dec."""
import json, pathlib
R = pathlib.Path(__file__).resolve().parents[2]
slots = {s['id']: s for s in json.load(open(R/'website/data/interest_slots.json'))['slots']}
assert slots['T27-THU-1930']['levels'] == [5, 6] and slots['T27-SUN-1915']['levels'] == [5, 6]
for s in slots.values():
    for x in s['sessions']:
        assert not (x['day'] == 'Sun' and x['start'] < '14:15' and not s.get('window')), s['id']  # church/lunch/2pm
        assert not (x['day'] == 'Sun' and x['start'] == '14:00'), s['id']
assert 'R4' not in slots and slots['R4B']['levels'] == [5, 6]
res = {r['id']: r for r in json.load(open(R/'docs/schedule/beta_reserved.json'))['reserved']}
assert 'R4' not in res and res['R4B']['pair'][1][:2] == ['Sun', '18:00']
for k in ('R1', 'R2', 'R3'):
    assert res[k]['week5']['date'] == '2026-12-23' and res[k]['week5']['thu_24_dec_lesson_moves_to'][0] == 'Wed'
print('slots_data_test OK')
