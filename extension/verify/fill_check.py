#!/usr/bin/env python3
"""Page-fill and overflow gate, from the report written by tools/build.py (measured in the browser BEFORE the leftover space is shared out):
every unit page must be at least 85 percent full and no page may overflow. Front/back matter pages (cover, welcome, contents, progress, certificate,
answers) are exempt from the 85 percent rule but never from the overflow rule.
    python3 extension/verify/fill_check.py [--level 1]
"""
import argparse, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ap = argparse.ArgumentParser(); ap.add_argument('--level', type=int, default=1); a = ap.parse_args()
rep = json.load(open(os.path.join(ROOT, 'outputs', 'extension', f'L{a.level}', 'build_report.json')))
bad = 0
for m in rep['pages']:
    if m['edition'] != 'print' or m['fill'] is None:
        continue
    flag = ''
    if m['over']:
        flag = 'OVERFLOW'
    elif not m['exempt'] and m['fill'] < 0.85:
        flag = 'UNDER 85%'
    bad += bool(flag)
    print(f'{m["no"]:3d} {m["label"]:<42s} fill {m["fill"]:.2f} {"(exempt)" if m["exempt"] else ""} {flag}')
print('OK' if not bad else f'{bad} page(s) failed')
sys.exit(1 if bad else 0)
