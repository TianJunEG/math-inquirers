#!/usr/bin/env python3
"""Structural check of every .sb3 in starters/ and answers/ (standard library only).
Checks: zip opens; project.json parses; asset md5s match; every block link (parent/next/inputs/fields)
resolves; no orphan blocks; variable/list ids declared; opcodes in the allowed set; sb3 shapes of inputs."""
import glob, hashlib, json, os, sys, zipfile
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
OPS = set('''event_whenflagclicked event_whenkeypressed control_repeat control_repeat_until control_if control_if_else control_wait
data_setvariableto data_changevariableby data_addtolist data_deletealloflist data_itemoflist data_itemnumoflist data_lengthoflist
looks_say looks_sayforsecs sensing_askandwait sensing_answer operator_add operator_subtract operator_multiply operator_divide
operator_mod operator_random operator_equals operator_gt operator_lt operator_join operator_letter_of operator_length
motion_gotoxy motion_movesteps motion_turnright motion_pointindirection motion_xposition motion_changexby pen_penDown pen_clear'''.split())
errs = []
def err(f, m): errs.append(f + ': ' + m)
files = sorted(glob.glob(HERE + '/starters/*.sb3') + glob.glob(HERE + '/answers/*.sb3'))
for f in files:
    n = os.path.basename(f)
    try:
        z = zipfile.ZipFile(f); assert z.testzip() is None
        pj = json.loads(z.read('project.json'))
    except Exception as e:
        err(n, 'cannot open: %s' % e); continue
    names = set(z.namelist())
    allvars, alllists = {}, {}
    for t in pj['targets']:
        for c in t['costumes']:
            if c['md5ext'] not in names: err(n, 'missing asset ' + c['md5ext'])
            elif hashlib.md5(z.read(c['md5ext'])).hexdigest() != c['assetId']: err(n, 'md5 mismatch ' + c['md5ext'])
        allvars.update(t['variables']); alllists.update(t['lists'])
    if sum(t['isStage'] for t in pj['targets']) != 1 or not pj['targets'][0]['isStage']: err(n, 'stage must be first and unique')
    for t in pj['targets']:
        B = t['blocks']; seen = set()
        def ref(v, host):
            if isinstance(v, str):
                if v not in B: err(n, 'dangling ref %s from %s' % (v, host)); return
                if B[v]['parent'] != host: err(n, 'parent of %s is %s, expected %s' % (v, B[v]['parent'], host))
                seen.add(v)
        for i, b in B.items():
            if b['opcode'] not in OPS: err(n, 'unknown opcode ' + b['opcode'])
            if b['next'] is not None:
                ref(b['next'], i)
                if B.get(b['next'], {}).get('parent') != i: err(n, 'next/parent mismatch at ' + i)
            for k, inp in b['inputs'].items():
                if not isinstance(inp, list) or inp[0] not in (1, 2, 3): err(n, 'bad input %s.%s' % (i, k)); continue
                for item in inp[1:]:
                    if isinstance(item, str): ref(item, i)
                    elif isinstance(item, list) and item and item[0] == 12:
                        if item[2] not in allvars or allvars[item[2]][0] != item[1]: err(n, 'bad var ref %s' % item)
                    elif isinstance(item, list) and not (4 <= item[0] <= 13): err(n, 'bad primitive %s' % item)
            for k, fl in b['fields'].items():
                if k in ('VARIABLE',) and (fl[1] not in allvars or allvars[fl[1]][0] != fl[0]): err(n, 'bad VARIABLE field %s' % fl)
                if k == 'LIST' and (fl[1] not in alllists or alllists[fl[1]][0] != fl[0]): err(n, 'bad LIST field %s' % fl)
                if k == 'KEY_OPTION' and not fl[0]: err(n, 'empty key')
            if b['topLevel']:
                seen.add(i)
                if b['parent'] is not None: err(n, 'top block has parent ' + i)
                if not b['opcode'].startswith('event_'): err(n, 'top-level block is not a hat: ' + i)
            else:
                if b['parent'] is None: err(n, 'orphan block ' + i)
        if set(B) - seen: err(n, 'unreachable blocks %s' % sorted(set(B) - seen))
        # cycle check along next
        for i in B:
            s, c = set(), i
            while c:
                if c in s: err(n, 'cycle at ' + i); break
                s.add(c); c = B[c]['next']
print('%d files checked, %d problems' % (len(files), len(errs)))
for e in errs: print(' ', e)
sys.exit(1 if errs else 0)
