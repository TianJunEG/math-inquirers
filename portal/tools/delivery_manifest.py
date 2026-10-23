#!/usr/bin/env python3
"""Delivery manifest tool.  portal/data/delivery_manifest.json maps  "<product_id>:<format>"  ->  R2 key, version, sha256 of the repository file.

  python3 portal/tools/delivery_manifest.py check            # verify every entry whose source file exists; exit 1 on mismatch or bad shape
  python3 portal/tools/delivery_manifest.py check --strict   # also fail when a source file is missing (use before uploading)
  python3 portal/tools/delivery_manifest.py update           # recompute sha256 and bytes from the files (after you rebuilt a PDF); bump "version" and r2_key yourself
  python3 portal/tools/delivery_manifest.py list-upload      # tab-separated: r2_key<TAB>source<TAB>sha256 (used by upload_files.sh)

Rules: r2_key = files/<product>/<version>/<filename> (a new version gets a NEW key, so old links keep serving the file the buyer paid for);
the filename is plain ASCII; sources live inside the repository. No secrets here: the manifest is bundled into the Cloudflare Function.
"""
import hashlib, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MANIFEST = os.path.join(ROOT, 'portal', 'data', 'delivery_manifest.json')
KEY_RE = re.compile(r'^[a-z0-9][a-z0-9._-]{0,79}:(pdf|zip|other)$')
R2_RE = re.compile(r'^files/[a-z0-9][a-z0-9._-]*/v[0-9][0-9a-z._-]*/[A-Za-z0-9._-]{1,120}$')

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()

def load():
    with open(MANIFEST, encoding='utf-8') as f:
        return json.load(f)

def shape_errors(m):
    errs = []
    if m.get('schema') != 1: errs.append('schema must be 1')
    if not re.match(r'^[a-z0-9][a-z0-9-]{2,62}$', str(m.get('bucket', ''))): errs.append('bucket name missing or invalid')
    seen = {}
    for k, e in (m.get('files') or {}).items():
        if not KEY_RE.match(k): errs.append(f'{k}: key must look like product-id:pdf')
        for f in ('title', 'source', 'r2_key', 'filename', 'version'):
            if not e.get(f): errs.append(f'{k}: missing {f}')
        if e.get('r2_key') and not R2_RE.match(e['r2_key']): errs.append(f"{k}: r2_key {e['r2_key']!r} must be files/<product>/v<version>/<name>")
        if e.get('r2_key') and e.get('filename') and not e['r2_key'].endswith('/' + e['filename']): errs.append(f'{k}: r2_key must end with the filename')
        if e.get('r2_key') in seen: errs.append(f"{k}: r2_key also used by {seen[e['r2_key']]}")
        seen[e.get('r2_key')] = k
        src = e.get('source', '')
        if os.path.isabs(src) or '..' in src.split('/'): errs.append(f'{k}: source must be a relative path inside the repository')
        if e.get('sha256') and not re.match(r'^[0-9a-f]{64}$', e['sha256']): errs.append(f'{k}: sha256 malformed')
    return errs

def main(argv):
    cmd = argv[1] if len(argv) > 1 else 'check'
    m = load()
    errs = shape_errors(m)
    files = m.get('files') or {}
    if cmd == 'check':
        strict = '--strict' in argv
        ok = missing = 0
        for k, e in files.items():
            p = os.path.join(ROOT, e.get('source', ''))
            if not os.path.isfile(p):
                missing += 1
                (errs.append if strict else print)(f'{k}: source file not built yet: {e.get("source")}' if not strict else f'{k}: source file missing: {e.get("source")}')
                continue
            actual = sha256(p)
            if actual != e.get('sha256'): errs.append(f'{k}: sha256 differs from {e["source"]} (file changed: run "update", bump version + r2_key, re-upload)')
            elif os.path.getsize(p) != e.get('bytes'): errs.append(f'{k}: byte size differs')
            else: ok += 1
        print(f'{ok} entries match their files, {missing} not built yet, {len(errs)} problems')
        for x in errs: print('  PROBLEM:', x)
        return 1 if errs else 0
    if cmd == 'update':
        if errs: print('\n'.join(errs)); return 1
        for k, e in files.items():
            p = os.path.join(ROOT, e['source'])
            if os.path.isfile(p):
                e['sha256'], e['bytes'] = sha256(p), os.path.getsize(p)
        with open(MANIFEST, 'w', encoding='utf-8') as f:
            json.dump(m, f, indent=1, ensure_ascii=False); f.write('\n')
        print('manifest updated'); return 0
    if cmd == 'list-upload':
        if errs: sys.stderr.write('\n'.join(errs) + '\n'); return 1
        for k, e in files.items():
            if os.path.isfile(os.path.join(ROOT, e['source'])): print(f"{e['r2_key']}\t{e['source']}\t{e['sha256']}")
        return 0
    print(__doc__); return 2

if __name__ == '__main__':
    sys.exit(main(sys.argv))
