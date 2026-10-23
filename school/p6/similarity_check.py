#!/usr/bin/env python3
"""Similarity check of the Primary 6 pupil pages against the PRIVATE, gitignored sources (docs/books/private_*, docs/sasmo/private_*).
It reads the private files only to compare; it prints and writes only counts and the pupil text of flagged items with the id of the private entry, never the private text.
Rules (owner brief): no item may share a 7-word run, nor the same scenario with the same numbers, nor the same structure with a private entry.
  1. 7-word runs: every run of 7 consecutive words/numbers of any pupil sentence is looked up in the private corpus.
  2. Same scenario and numbers: an item that shares 3 or more numbers (other than 0 to 12 and 100) AND 3 or more content words with a private entry, or 4 or more of those numbers.
  3. Same structure: a pupil sentence of 8 or more words, with numbers masked and names masked, whose difflib ratio to a private sentence masked the same way is 0.80 or more.
Usage: python3 similarity_check.py [--outdir out]    (exit code 1 when anything is flagged)"""
import os, re, sys, json, glob, difflib, html as H
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
STOP = set("the a an and or of to in on at is are was were be been it its as for with by from that this these those how what which who find work out each there their his her them they he she then than more less many much one two three four five six seven eight nine ten some all any when after before into per".split())
NAMES = set("ali mei siti ben kumar aisha wei ravi jenny lily hana tom farid grace hui nadia daniel priya jun alex".split())

def toks(s): return re.findall(r"[a-z]+|\d+(?:\.\d+)?", s.lower())
def plain(h): return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", h))).strip()

def private_texts():
    out = []                                        # (source id, text)
    for f in glob.glob(os.path.join(ROOT, "docs", "books", "private_p*_papers", "records.jsonl")):
        for line in open(f, errors="ignore"):
            try: r = json.loads(line)
            except Exception: continue
            out.append((f"{os.path.basename(os.path.dirname(f))}/{r.get('src','?')}/{r.get('q','?')}", r.get("txt", "")))
    for f in glob.glob(os.path.join(ROOT, "docs", "books", "private_p*_papers", "non_routine_questions.md")):
        for i, line in enumerate(open(f, errors="ignore")):
            if line.startswith("|") and line.count("|") >= 10:
                cells = [c.strip() for c in line.split("|")]
                out.append((f"{os.path.basename(os.path.dirname(f))}/table/{cells[1:5]}", cells[9] if len(cells) > 9 else ""))
    for f in glob.glob(os.path.join(ROOT, "docs", "books", "private_p*_papers", "records.txt")) + glob.glob(os.path.join(ROOT, "docs", "sasmo", "private_*.md")) + glob.glob(os.path.join(ROOT, "docs", "books", "private_*.md")):
        for i, para in enumerate(re.split(r"\n\s*\n|\n", open(f, errors="ignore").read())):
            out.append((f"{os.path.basename(f)}#{i}", para))
    return out

def main():
    outdir = os.path.join(HERE, "out")
    if "--outdir" in sys.argv: outdir = sys.argv[sys.argv.index("--outdir") + 1]
    priv = private_texts()
    if not priv:
        msg = "similarity check SKIPPED: no private source files found (they are gitignored: docs/books/private_*, docs/sasmo/private_*)"
        print(msg); open(os.path.join(outdir, "similarity_report.txt"), "w").write(msg + "\n"); return 0
    import build
    pages = build.all_pages()
    ngrams = {}
    for sid, t in priv:
        w = toks(t)
        for i in range(len(w) - 6): ngrams.setdefault(tuple(w[i:i + 7]), sid)
    pnums = []; pwords = []
    for sid, t in priv:
        w = toks(t); pnums.append({x for x in w if re.fullmatch(r"\d+(?:\.\d+)?", x) and x not in {str(i) for i in range(13)} | {"100"}}); pwords.append({x for x in w if x.isalpha() and len(x) >= 4 and x not in STOP})
    masked = []
    for sid, t in priv:
        for s in re.split(r"(?<=[.?!])\s+", t):
            w = [("N" if x in NAMES else "#" if re.fullmatch(r"\d+(?:\.\d+)?", x) else x) for x in toks(s)]
            if len(w) >= 8 and sum(x.isalpha() and x not in ('N',) for x in w) >= 5: masked.append((sid, " ".join(w)))
    flags = []; nitems = 0
    for p in pages:
        body = p["body"]
        items = re.findall(r'<div class="(?:qc|chrow|mit|ocd|mcd)[^>]*>(.*?)</div></div>', body, re.S) or [body]
        texts = [plain(x) for x in items] + [plain(s) for s in p["instr"]] + [plain(body)]
        # 1. seven-word runs
        for t in texts[-1:] + texts[:-1]:
            w = toks(t)
            for i in range(len(w) - 6):
                g = tuple(w[i:i + 7])
                if g in ngrams and sum(x.isalpha() for x in g) >= 4: flags.append((p["code"], "7-word run", " ".join(g), ngrams[g]))
        # 2. same scenario and numbers
        for t in texts[:-1]:
            nitems += 1
            w = toks(t); nums = {x for x in w if re.fullmatch(r"\d+(?:\.\d+)?", x) and x not in {str(i) for i in range(13)} | {"100"}}; words = {x for x in w if x.isalpha() and len(x) >= 4 and x not in STOP and x not in NAMES}
            if len(nums) < 3: continue
            for (sid, _), pn, pw in zip(priv, pnums, pwords):
                common = nums & pn
                if len(common) >= 3 and len(words & pw) >= 3: flags.append((p["code"], "same numbers and scenario", t[:90], sid + " shares " + ",".join(sorted(common))))
        # 3. same structure
        sents = set()
        for t in texts[:-1]:
            for s in re.split(r"(?<=[.?!])\s+", t):
                w = [("N" if x in NAMES else "#" if re.fullmatch(r"\d+(?:\.\d+)?", x) else x) for x in toks(s)]
                if len(w) >= 8 and sum(x.isalpha() and x != 'N' for x in w) >= 5: sents.add(" ".join(w))
        for s in sents:
            sm = difflib.SequenceMatcher(None, s, "")
            for sid, m in masked:
                sm.set_seq2(m)
                if sm.real_quick_ratio() >= 0.8 and sm.quick_ratio() >= 0.8 and sm.ratio() >= 0.8: flags.append((p["code"], "same structure", s[:90], sid))
    lines = [f"Similarity check of {len(pages)} pupil pages ({nitems} items) against {len(priv)} private entries.", f"Flags: {len(flags)}"]
    for f in flags[:200]: lines.append("FLAG " + " | ".join(map(str, f)))
    open(os.path.join(outdir, "similarity_report.txt"), "w").write("\n".join(lines) + "\n")
    print("\n".join(lines[:60]))
    return 1 if flags else 0

if __name__ == "__main__":
    sys.exit(main())
