#!/usr/bin/env python3
"""Reading-load and wording lint from term/l1/WORDING_GUIDE.md (thresholds per level in config/levels.json -> lint).
Checks every child-facing text (stems, parts, hints, learn page) and, more leniently, explanations (parent-facing):
  * sentence length (max / mean alphabetic words), number of sentences in a stem, very long words
  * banned words (candy, eraser, compensation, represent, determine, respectively, bigger/biggest, 'work out')
  * money: '50c' is wrong (50¢), no $1.50 style at Level 1, no S$ / price words anywhere (prices are on hold)
  * quantities written as number words ('two apples'), claims (MOE, GEP, SASMO, PSLE, gifted, syllabus, Olympiad)
  * every stem/part has a command or question word; names outside the cast are listed for review
    python3 extension/verify/wording_lint.py [--level 1]       exit 1 on any ERROR (warnings do not fail)
"""
import argparse, glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import EXT   # noqa: E402

BANNED = r'\b(candy|eraser|compensation|represent|represents|determine|respectively|bigger|biggest|work out)\b'
CLAIM = r'\b(MOE|GEP|SASMO|PSLE|gifted|olympiad|syllabus|endorsed|approved)\b'
PRICE = r'(S\$|\bprice\b|\bprices\b|\bUSD\b|\bsale\b)'
NUMWORD = r'\b(two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)\s+(?!and\b|or\b|more\b|less\b|times\b|of\b|each\b)[a-z]+'
COMMAND = r"\b(fill|write|circle|draw|count|add|subtract|find|complete|tick|how|what|which|who|is|will|can|do|does|show|list|make|put|pick|use|look|read|try|keep|check|take|start|hop|go|think|share|choose|count)\b"
CAST = {'Ali', 'Mei', 'Siti', 'Ben', 'Kumar', 'Aisha', 'Wei', 'Ravi', 'Jenny', 'Lily', 'Jamie', 'Ray', 'Amelia', 'Jason', 'Mi', 'Step', 'Triangle', 'Jar', 'Bag', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Level', 'Unit',
        'Start', 'Think', 'Go', 'Check', 'Learn', 'Hint', 'Answer', 'Count', 'Fill', 'Circle', 'Write', 'Try', 'Why', 'Up', 'Down', 'True', 'False', 'Yes', 'No', 'Look', 'Add', 'Both', 'Mei', 'Holiday', 'Program', 'Math', 'Inquirers', 'Extension', 'Workbook', 'Printed', 'Use', 'Read', 'Fix', 'Tips', 'Well', 'Missed'}


def plain(t):
    t = re.sub(r'\{circ:([^}]*)\}', lambda m: ' '.join(m.group(1).split('|')), t)
    return t.replace('{b}', ' ').replace('{l}', ' ')


def sentences(t):
    return [x.strip() for x in re.split(r'(?<=[.?!])\s+|\n', plain(t)) if x.strip()]


def awords(s):
    return re.findall(r"[A-Za-z][A-Za-z']*", s)


def lint_text(where, text, lv, lim, kind, errs, warns):
    ss = sentences(text)
    cap = lim['max_sentence_words'] + (6 if kind == 'explain' else 0)
    mean_cap = lim['mean_sentence_words'] + (3 if kind == 'explain' else 0)
    counts = [len(awords(s)) for s in ss]
    counts_nz = [c for c in counts if c >= 3]   # fragments such as '___ stickers' do not count
    for s, c in zip(ss, counts):
        if c > cap:
            errs.append(f'{where}: sentence has {c} words (max {cap}): "{s[:60]}"')
    if kind in ('stem', 'hint') and counts_nz and sum(counts_nz) / len(counts_nz) > mean_cap:
        errs.append(f'{where}: mean sentence length {sum(counts_nz) / len(counts_nz):.1f} > {mean_cap}')
    if kind == 'stem' and len([c for c in counts if c >= 3]) > lim['max_stem_sentences'] + 1:
        errs.append(f'{where}: {len(ss)} sentences in a stem (max {lim["max_stem_sentences"]} before the question)')
    for w in awords(plain(text)):
        if len(w) >= lim['long_word_letters']:
            warns.append(f'{where}: long word "{w}"')
    for pat, msg in ((BANNED, 'banned word'), (CLAIM, 'claim word'), (PRICE, 'price/commerce word')):
        m = re.search(pat, text, re.I if pat != CLAIM else 0)
        if m:
            errs.append(f'{where}: {msg} "{m.group(0)}"')
    if re.search(r'\b\d+c\b', text):
        errs.append(f'{where}: cents written "c": use the ¢ sign')
    if lv == '1' and re.search(r'\$\d+\.\d\d', text):
        errs.append(f'{where}: decimal money not used at Level 1')
    if lv == '1' and re.search(r'\b\d{1,3},\d{3}\b', text):
        errs.append(f'{where}: comma in number')
    m = re.search(NUMWORD, plain(text))
    if m and kind != 'explain':
        errs.append(f'{where}: quantity written as a word: "{m.group(0)}"')
    if kind == 'stem' and not re.search(COMMAND, plain(text), re.I):
        warns.append(f'{where}: no command or question word found')
    for w in re.findall(r'(?<![.?!]\s)(?<!^)\b[A-Z][a-z]+\b', plain(text)):
        if w not in CAST:
            warns.append(f'{where}: capitalised word "{w}" not in the cast list (check it is a name or a label)')


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--level', type=int, default=1)
    a = ap.parse_args()
    cfg = json.load(open(os.path.join(EXT, 'config', 'levels.json')))['levels'][str(a.level)]
    lim = cfg['lint']; lv = str(a.level)
    errs, warns, n = [], [], 0
    for f in sorted(glob.glob(os.path.join(EXT, 'data', f'l{a.level}_u*.json'))):
        u = json.load(open(f, encoding='utf-8'))
        L = u['learn']
        texts = [(u['id'] + ' goal', u['goal'], 'explain'), (u['id'] + ' intro', L['intro'], 'explain'), (u['id'] + ' example', L['example']['problem'], 'stem'),
                 (u['id'] + ' example answer', L['example']['answer'], 'stem')]
        texts += [(f'{u["id"]} step {i + 1}', s, 'stem') for i, s in enumerate(L['example']['steps'])]
        texts += [(f'{u["id"]} how-to {i + 1}', s, 'stem') for i, s in enumerate(L['howto']['steps'])]
        tr = L['try']; texts += [(tr['id'], tr['text'], 'stem'), (tr['id'] + ' why', tr['explanation'], 'explain')]
        for it in u['items']:
            texts.append((it['id'], it['text'], 'stem'))
            for p in it.get('parts', []):
                texts.append((f'{it["id"]}({p["label"]})', p['text'], 'part'))
            if it.get('hint'):
                texts.append((it['id'] + ' hint', it['hint'], 'hint'))
            texts.append((it['id'] + ' why', it['explanation'], 'explain'))
        for where, t, kind in texts:
            n += 1
            lint_text(where, t, lv, lim, kind, errs, warns)
    print(f'{n} texts linted')
    for w in sorted(set(warns)): print('WARN', w)
    for e in errs: print('ERROR', e)
    print('OK' if not errs else f'{len(errs)} error(s)')
    sys.exit(1 if errs else 0)


if __name__ == '__main__':
    main()
