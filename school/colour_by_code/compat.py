#!/usr/bin/env python3
"""Which picture can take which topic bank? Tries every picture x bank x tier (seed 7) and prints a Markdown table:
the smallest text size used (mm) or '-' when some region is too small for any question of that bank.
   python3 compat.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from sheet import make_sheet
from banks import BANKS
from pictures import PICTURES

def main():
    head = "| picture | " + " | ".join(f"{b} {t}★" for b in BANKS for t in (1, 2)) + " |"
    rows = [head, "|---|" + "---|" * (len(BANKS) * 2)]
    ok = tot = 0
    for pn in PICTURES:
        cells = []
        for bn in BANKS:
            for t in (1, 2):
                tot += 1
                try:
                    sh = make_sheet(dict(id="X", picture=pn, bank=bn, tier=t, seed=7))
                    cells.append(f"{min(i['place']['f'] for i in sh['items'].values()):.1f}"); ok += 1
                except Exception:
                    cells.append("-")
        rows.append(f"| {pn} | " + " | ".join(cells) + " |")
    rows.append(f"\n{ok} of {tot} picture, topic and tier combinations build.")
    return "\n".join(rows)

if __name__ == "__main__":
    print(main())
