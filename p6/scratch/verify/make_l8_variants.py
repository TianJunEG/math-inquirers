#!/usr/bin/env python3
"""Test-only copies of the Lesson 8 answer file with other shifts (the file itself always starts with shift 3),
to run the machine with spaces and with a negative shift (a negative shift tests mod with negative numbers).
Usage: python3 make_l8_variants.py <outdir>"""
import sys, os, json, zipfile
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'answers', 'L8_Code_Machine_ANSWER.sb3')
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
for shift in (16, -4, 26):
    zin = zipfile.ZipFile(src)
    pj = json.loads(zin.read('project.json'))
    sp = [t for t in pj['targets'] if not t['isStage']][0]
    done = False
    for b in sp['blocks'].values():
        if isinstance(b, dict) and b['opcode'] == 'data_setvariableto' and b['fields']['VARIABLE'][0] == 'shift' and not done:
            b['inputs']['VALUE'] = [1, [10, str(shift)]]; done = True
    assert done
    name = 'L8_shift_%s.sb3' % str(shift).replace('-', 'minus')
    with zipfile.ZipFile(os.path.join(out, name), 'w', zipfile.ZIP_DEFLATED) as zo:
        for i in zin.infolist():
            zo.writestr(i.filename, json.dumps(pj, separators=(',', ':'), ensure_ascii=False) if i.filename == 'project.json' else zin.read(i.filename))
    print(name)
