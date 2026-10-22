#!/usr/bin/env python3
"""Build every output for one lesson:  python3 term/l1/tools/build.py 01   (validates first; stops on any FAIL)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate
from common import *  # noqa
import b_deck, b_guide, b_print, b_practice
from playwright.sync_api import sync_playwright

def main():
    num = sys.argv[1] if len(sys.argv) > 1 else '01'
    d = validate.check_all(num, built=False)
    for f in validate.WARNS: print('WARN ', f)
    if validate.FAILS:
        for f in validate.FAILS: print('FAIL ', f)
        sys.exit('validation failed: nothing built')
    print('validated:', len(validate.PASSES), 'checks passed')
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        probs = b_deck.build_deck(d, b)
        b_guide.build_guide(d, b)
        b_print.build_print(d, b)
        b.close()
    b_practice.build_practice(d)
    validate.FAILS.clear(); validate.check_outputs(d); validate.check_foreign(d)
    for f in validate.FAILS: print('FAIL ', f)
    for p in validate.PASSES[-3:]: print('PASS ', p)
    if validate.FAILS: sys.exit(1)
    for p in probs: print('LAYOUT', p)
    print('built', os.path.join(OUT, f'l{d["_num"]}'))
    sys.exit(1 if probs else 0)

if __name__ == '__main__':
    main()
