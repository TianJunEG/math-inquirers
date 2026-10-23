#!/usr/bin/env python3
"""Run schema validation and the independent per-item answer checks. Exit 1 on any mismatch.

    python3 extension/verify/run_checks.py            # every extension/data/lN_uXX.json that exists
    python3 extension/verify/run_checks.py --level 1
Rules: every item and every part with an answer must have a check function in verify/lN_uXX_checks.py (CHECKS[id] returns a value
list, or {part_label: value list}); the check recomputes the answer, it does not read the JSON. A missing check is a failure.
"""
import argparse, glob, importlib.util, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import EXT, norm   # noqa: E402

TIERS = {'start', 'think', 'go', 'quiz'}


def blanks(item_or_part, figure=None):
    n = 0
    t = item_or_part.get('text', '')
    n += len(re.findall(r'\{b\}|\{l\}|\{circ:', t))
    return n


def fig_blanks(fig):
    if not fig:
        return 0
    if fig['type'] == 'tiles':
        return sum(1 for v in fig['items'] if v is None)
    if fig['type'] == 'bonds':
        return sum(1 for d in fig['items'] for k in ('whole', 'a', 'b') if d.get(k) is None)
    return 0


def schema(unit, errs):
    ids = set()
    pre = unit['id']
    for k in ('title', 'topic', 'goal', 'learn', 'items'):
        if k not in unit:
            errs.append(f'{pre}: missing {k}')
    ex = unit['learn']['example']
    for k in ('problem', 'steps', 'answer'):
        if not ex.get(k):
            errs.append(f'{pre}: learn.example.{k} missing')
    tr = unit['learn']['try']
    tr_items = [dict(tr, tier='start')]
    seen = {'start': 0, 'think': 0, 'go': 0, 'quiz': 0}
    for it in tr_items + unit['items']:
        i = it['id']
        if i in ids:
            errs.append(f'{i}: duplicate id')
        ids.add(i)
        if not i.startswith(pre + '-'):
            errs.append(f'{i}: id must start with {pre}-')
        if it['tier'] not in TIERS:
            errs.append(f'{i}: bad tier')
        if not it.get('explanation'):
            errs.append(f'{i}: explanation missing')
        if it['tier'] in ('think', 'go') and not it.get('hint'):
            errs.append(f'{i}: hint missing (Think harder / Go further)')
        if i != tr['id']:
            seen[it['tier']] += 1
            exp = {'start': 'S', 'think': 'T', 'go': 'G', 'quiz': 'C'}[it['tier']]
            if not re.fullmatch(pre + '-' + exp + r'\d\d', i):
                errs.append(f'{i}: id does not match tier {it["tier"]}')
        parts = it.get('parts')
        answers = [(None, it.get('answer'), it)] if not parts else [(p['label'], p.get('answer'), p) for p in parts]
        if parts and it.get('answer'):
            errs.append(f'{i}: both answer and parts')
        for lab, a, holder in answers:
            if not a or 'value' not in a or not a.get('text'):
                errs.append(f'{i}/{lab}: answer.value or answer.text missing')
                continue
            if not a.get('list'):
                exp_n = blanks(holder) + (fig_blanks(it.get('figure')) if not parts else 0)
                if exp_n and exp_n != len(a['value']):
                    errs.append(f'{i}/{lab}: {exp_n} blanks but {len(a["value"])} answer values (set "list": true if intended)')
        if it['tier'] != 'quiz' and it.get('page') not in (1, 2, 3, 4, 5, 6, None) and i != tr['id']:
            errs.append(f'{i}: bad page')
    return ids


def load_checks(level, unit):
    p = os.path.join(HERE, f'l{level}_u{unit:02d}_checks.py')
    if not os.path.exists(p):
        return None
    spec = importlib.util.spec_from_file_location(f'l{level}_u{unit:02d}_checks', p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.CHECKS


def run(files):
    errs, n_checked = [], 0
    for f in files:
        unit = json.load(open(f, encoding='utf-8'))
        ids = schema(unit, errs)
        checks = load_checks(unit['level'], unit['unit'])
        if checks is None:
            errs.append(f'{unit["id"]}: no checks file'); continue
        allitems = [dict(unit['learn']['try'], tier='start')] + unit['items']
        for it in allitems:
            i = it['id']
            if i not in checks:
                errs.append(f'{i}: NO CHECK FUNCTION'); continue
            try:
                got = checks[i]()
            except AssertionError as e:
                errs.append(f'{i}: check assertion failed {e}'); continue
            parts = it.get('parts')
            if parts:
                if not isinstance(got, dict):
                    errs.append(f'{i}: check must return a dict for an item with parts'); continue
                for p in parts:
                    n_checked += 1
                    if p['label'] not in got:
                        errs.append(f'{i}/{p["label"]}: no checked value'); continue
                    if sorted_if_list(norm(got[p['label']]), p) != sorted_if_list(norm(p['answer']['value']), p):
                        errs.append(f'{i}/{p["label"]}: MISMATCH computed {got[p["label"]]} vs book {p["answer"]["value"]}')
                extra = set(got) - {p['label'] for p in parts}
                if extra:
                    errs.append(f'{i}: check returns unknown parts {extra}')
            else:
                n_checked += 1
                if isinstance(got, dict):
                    errs.append(f'{i}: check returned a dict for an item without parts'); continue
                if norm(got) != norm(it['answer']['value']):
                    errs.append(f'{i}: MISMATCH computed {got} vs book {it["answer"]["value"]}')
        unknown = set(checks) - ids
        if unknown:
            errs.append(f'{unit["id"]}: checks for unknown ids {sorted(unknown)}')
    return errs, n_checked


def sorted_if_list(v, holder):
    return sorted(v) if holder['answer'].get('unordered') else v


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--level', type=int, default=0)
    a = ap.parse_args()
    pat = f'l{a.level}_u*.json' if a.level else 'l*_u*.json'
    files = sorted(glob.glob(os.path.join(EXT, 'data', pat)))
    errs, n = run(files)
    print(f'{len(files)} unit file(s), {n} answers independently checked')
    for e in errs:
        print('FAIL', e)
    print('OK' if not errs else f'{len(errs)} problem(s)')
    sys.exit(1 if errs else 0)
