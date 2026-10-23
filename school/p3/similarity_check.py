#!/usr/bin/env python3
"""Similarity check of the Primary 3 booklets against the private sources (gitignored: docs/books/private_* and docs/sasmo/private_*).
Reads the printed text of the pupil PDFs and the keys, and reports ONLY counts and page codes (never private text):
  1. shared runs of 7 or more words (words lower-cased, punctuation and numerals kept as written);
  2. same scenario with the same numbers: a printed sentence whose multiset of numbers (two or more numbers) equals that of a private sentence
     that also shares at least three content words;
  3. same structure: a printed sentence whose template (numbers replaced by N, names replaced by NAME) equals a private sentence's template
     with at least 8 words.
Usage: python3 similarity_check.py [--out out]   Exit code 1 if any hit. Writes out/similarity_report.txt (counts only)."""
import os, re, sys, glob, subprocess, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "out")
if "--out" in sys.argv: OUT = sys.argv[sys.argv.index("--out") + 1]

def toks(s): return re.findall(r"[a-z0-9$.:¢÷×ℓ]+", s.lower())
NAMES = {"ali", "mei", "siti", "ben", "kumar", "aisha", "wei", "ravi", "jenny", "lily", "hana", "tom", "zara", "amir", "priya", "daniel", "john", "mary", "peter", "sam", "ann", "tim", "jane", "raj", "mary", "alice", "bob"}
STOP = set("the a an of and to in is are was were it its he she they his her their how many much what which does do did has have had with for on at by from that this as be or if then than more less each all".split())
def template(t):
    out = []
    for w in t:
        if re.fullmatch(r"[$]?\d[\d.:,]*", w): out.append("N")
        elif w in NAMES: out.append("NAME")
        else: out.append(w)
    return tuple(out)
def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.?!])\s+|\n{2,}", text) if len(s.split()) >= 4]

private = []
for pat in ("docs/books/private_*/*", "docs/books/private_*.md", "docs/sasmo/private_*.md"):
    private += [f for f in glob.glob(os.path.join(ROOT, pat)) if os.path.isfile(f) and f.endswith((".md", ".txt"))]
if not private:
    print("no private sources found (they are gitignored): nothing to compare"); sys.exit(0)
ptext = [open(f, errors="ignore").read() for f in private]
shingles = set(); nums = collections.defaultdict(list); temps = set()
for tx in ptext:
    for ln in tx.splitlines():
        t = toks(ln)
        for i in range(len(t) - 6): shingles.add(tuple(t[i:i + 7]))
    for s in sentences(tx):
        t = toks(s)
        nm = tuple(sorted(w for w in t if re.fullmatch(r"\d[\d.:,]*", w)))
        if len(nm) >= 2: nums[nm].append({w for w in t if w not in STOP and not re.fullmatch(r"[$]?\d[\d.:,]*", w)})
        if len(t) >= 8: temps.add(template(t))

rep = []; total = 0
for k in ("S1", "S2"):
    for kind in ("Puzzles", "Answer_Key"):
        f = os.path.join(OUT, f"P3_{k}_{kind}.pdf")
        if not os.path.exists(f): continue
        pages = subprocess.run(["pdftotext", "-layout", f, "-"], capture_output=True, text=True).stdout.split("\f")
        for pi, pg in enumerate(pages, 1):
            if not pg.strip(): continue
            flat = re.sub(r"[ \t]+", " ", pg)
            sh = 0
            for ln in flat.split("\n"):
                t = toks(ln)
                for i in range(len(t) - 6):
                    if tuple(t[i:i + 7]) in shingles: sh += 1
            # sentences of the page (lines joined)
            sn = 0; st = 0
            for s in sentences(re.sub(r"\s*\n\s*", " ", flat)):
                t = toks(s)
                nm = tuple(sorted(w for w in t if re.fullmatch(r"\d[\d.:,]*", w)))
                words = {w for w in t if w not in STOP and not re.fullmatch(r"[$]?\d[\d.:,]*", w)}
                if len(nm) >= 2 and nm in nums and any(len(words & pw) >= 3 for pw in nums[nm]): sn += 1
                if len(t) >= 8 and template(t) in temps: st += 1
            total += sh + sn + st
            if sh or sn or st: rep.append(f"{k} {kind} page {pi}: 7-word runs {sh}, same numbers and 3 shared words {sn}, same template {st}")
txt = f"Private sources compared: {len(private)} files (names not printed). Pupil pages and keys of both booklets.\nHits: {total}\n" + "\n".join(rep) + "\n"
open(os.path.join(OUT, "similarity_report.txt"), "w").write(txt)
print(txt)
sys.exit(1 if total else 0)
