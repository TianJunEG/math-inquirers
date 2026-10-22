#!/usr/bin/env python3
"""Math Inquirers P6: generate the Scratch 3 starter (.sb3) and answer-key projects.

Run:  python3 p6/scratch/build_sb3.py
Writes p6/scratch/starters/*.sb3 and p6/scratch/answers/*_ANSWER.sb3.
Everything is our own artwork (simple SVG shapes); no Scratch assets are copied.
Standard library only.
"""
import hashlib, json, os, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
TYPE = {'n': 4, 'p': 5, 'w': 6, 'i': 7, 'a': 8, 's': 10}   # primitive type codes in project.json


class Blk:
    def __init__(self, i): self.id = i


class V:  # a variable reporter
    def __init__(self, name): self.name = name


class Target:
    """Builds the block dictionary of one sprite, with parent/next links."""

    def __init__(self, proj, prefix):
        self.proj, self.prefix, self.n, self.blocks = proj, prefix, 0, {}
        self.nextx, self.nexty = 20, 20

    # --- low level ---
    def _id(self):
        self.n += 1
        return '%s%03d' % (self.prefix, self.n)

    def _enc(self, kind, val, host):
        t = TYPE.get(kind, 10)
        if isinstance(val, Blk):
            self.blocks[val.id]['parent'] = host
            return [3, val.id, [t, '']] if kind != 'c' else [2, val.id]
        if isinstance(val, V):
            return [3, [12, val.name, self.proj.vid(val.name)], [t, '']]
        return [1, [t, str(val)]]

    def b(self, op, inputs=None, fields=None, subs=None):
        i = self._id()
        blk = {'opcode': op, 'next': None, 'parent': None, 'inputs': {}, 'fields': fields or {},
               'shadow': False, 'topLevel': False}
        self.blocks[i] = blk
        for k, (kind, val) in (inputs or {}).items():
            if val is None:
                continue
            blk['inputs'][k] = self._enc(kind, val, i)
        for k, body in (subs or {}).items():
            first = self.stack(body, i)
            if first:
                blk['inputs'][k] = [2, first]
        return Blk(i)

    def stack(self, body, parent=None):
        body = [x for x in body if x is not None]
        prev = None
        for blk in body:
            d = self.blocks[blk.id]
            if prev is None:
                d['parent'] = parent
            else:
                d['parent'] = prev.id
                self.blocks[prev.id]['next'] = blk.id
            prev = blk
        return body[0].id if body else None

    def script(self, hat, body, x=None, y=None):
        first = self.stack([hat] + list(body))
        d = self.blocks[first]
        d['topLevel'], d['parent'] = True, None
        d['x'], d['y'] = (x if x is not None else self.nextx), (y if y is not None else self.nexty)
        self.nexty += 60 + 46 * (len(body) + 1) + 40 * sum(1 for _ in body)
        if self.nexty > 600:
            self.nexty = 20
            self.nextx += 420

    # --- blocks ---
    def flag(self): return self.b('event_whenflagclicked')
    def key(self, k): return self.b('event_whenkeypressed', fields={'KEY_OPTION': [k, None]})
    def repeat(self, n, body): return self.b('control_repeat', {'TIMES': ('w', n)}, subs={'SUBSTACK': body})
    def until(self, cond, body): return self.b('control_repeat_until', {'CONDITION': ('c', cond)}, subs={'SUBSTACK': body})
    def if_(self, cond, body): return self.b('control_if', {'CONDITION': ('c', cond)}, subs={'SUBSTACK': body})
    def ifelse(self, cond, a, b): return self.b('control_if_else', {'CONDITION': ('c', cond)}, subs={'SUBSTACK': a, 'SUBSTACK2': b})
    def wait(self, s): return self.b('control_wait', {'DURATION': ('p', s)})
    def setv(self, name, val): return self.b('data_setvariableto', {'VALUE': ('s', val)}, {'VARIABLE': [name, self.proj.vid(name)]})
    def chg(self, name, val): return self.b('data_changevariableby', {'VALUE': ('n', val)}, {'VARIABLE': [name, self.proj.vid(name)]})
    def say(self, m): return self.b('looks_say', {'MESSAGE': ('s', m)})
    def sayfor(self, m, s): return self.b('looks_sayforsecs', {'MESSAGE': ('s', m), 'SECS': ('n', s)})
    def ask(self, q): return self.b('sensing_askandwait', {'QUESTION': ('s', q)})
    def answer(self): return self.b('sensing_answer')
    def add(self, a, c): return self.b('operator_add', {'NUM1': ('n', a), 'NUM2': ('n', c)})
    def sub(self, a, c): return self.b('operator_subtract', {'NUM1': ('n', a), 'NUM2': ('n', c)})
    def mul(self, a, c): return self.b('operator_multiply', {'NUM1': ('n', a), 'NUM2': ('n', c)})
    def div(self, a, c): return self.b('operator_divide', {'NUM1': ('n', a), 'NUM2': ('n', c)})
    def mod(self, a, c): return self.b('operator_mod', {'NUM1': ('n', a), 'NUM2': ('n', c)})
    def rnd(self, a, c): return self.b('operator_random', {'FROM': ('n', a), 'TO': ('n', c)})
    def eq(self, a, c): return self.b('operator_equals', {'OPERAND1': ('s', a), 'OPERAND2': ('s', c)})
    def gt(self, a, c): return self.b('operator_gt', {'OPERAND1': ('s', a), 'OPERAND2': ('s', c)})
    def lt(self, a, c): return self.b('operator_lt', {'OPERAND1': ('s', a), 'OPERAND2': ('s', c)})
    def join(self, a, c): return self.b('operator_join', {'STRING1': ('s', a), 'STRING2': ('s', c)})
    def letter(self, i, s): return self.b('operator_letter_of', {'LETTER': ('w', i), 'STRING': ('s', s)})
    def length(self, s): return self.b('operator_length', {'STRING': ('s', s)})
    def goto(self, x, y): return self.b('motion_gotoxy', {'X': ('n', x), 'Y': ('n', y)})
    def move(self, n): return self.b('motion_movesteps', {'STEPS': ('n', n)})
    def turnr(self, d): return self.b('motion_turnright', {'DEGREES': ('n', d)})
    def point(self, d): return self.b('motion_pointindirection', {'DIRECTION': ('a', d)})
    def xpos(self): return self.b('motion_xposition')
    def changex(self, d): return self.b('motion_changexby', {'DX': ('n', d)})
    def pendown(self): return self.b('pen_penDown')
    def erase(self): return self.b('pen_clear')
    def lst(self, name): return {'LIST': [name, self.proj.lid(name)]}
    def addto(self, item, name): return self.b('data_addtolist', {'ITEM': ('s', item)}, self.lst(name))
    def delall(self, name): return self.b('data_deletealloflist', None, self.lst(name))
    def itemof(self, i, name): return self.b('data_itemoflist', {'INDEX': ('i', i)}, self.lst(name))
    def itemnum(self, item, name): return self.b('data_itemnumoflist', {'ITEM': ('s', item)}, self.lst(name))
    def lenlist(self, name): return self.b('data_lengthoflist', None, self.lst(name))


def svg_friend():
    return ('<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">'
            '<circle cx="24" cy="24" r="21" fill="#FFD23F" stroke="#1B2A49" stroke-width="3"/>'
            '<circle cx="17" cy="19" r="3.5" fill="#1B2A49"/><circle cx="31" cy="19" r="3.5" fill="#1B2A49"/>'
            '<path d="M14 29 Q24 39 34 29" fill="none" stroke="#1B2A49" stroke-width="3" stroke-linecap="round"/></svg>')


def svg_arrow():
    return ('<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="30" height="24" viewBox="0 0 30 24">'
            '<polygon points="2,2 28,12 2,22 8,12" fill="#1F9E89" stroke="#1B2A49" stroke-width="2" stroke-linejoin="round"/></svg>')


def svg_blank():
    return ('<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">'
            '<rect width="480" height="360" fill="#FFFFFF"/></svg>')


def svg_numberline():
    s = ['<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">',
         '<rect width="480" height="360" fill="#FFFFFF"/>',
         '<line x1="0" y1="180" x2="480" y2="180" stroke="#1B2A49" stroke-width="3"/>']
    for v in range(-240, 241, 40):
        x = v + 240
        h = 14 if v % 120 == 0 else 8
        s.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#1B2A49" stroke-width="2"/>' % (x, 180 - h, x, 180 + h))
        if v % 120 == 0:
            s.append('<text x="%d" y="215" font-size="18" font-family="Sans Serif" text-anchor="middle" fill="#1B2A49">%d</text>' % (x, v))
    s.append('</svg>')
    return ''.join(s)


class Proj:
    def __init__(self, name):
        self.name, self.vars, self.lists, self.assets = name, {}, {}, {}
        self.monitors, self.extensions = [], []
        self.sprite_art, self.back_art = 'friend', svg_blank
        self.sprite = Target(self, 's')
        self.x, self.y, self.direction = 0, 0, 90

    def vid(self, name):
        if name not in self.vars:
            self.vars[name] = ['var%02d' % (len(self.vars) + 1), 0]
        return self.vars[name][0]

    def lid(self, name):
        if name not in self.lists:
            self.lists[name] = ['lst%02d' % (len(self.lists) + 1), []]
        return self.lists[name][0]

    def var(self, name, init=0, show=False, xy=(5, 5)):
        self.vid(name)
        self.vars[name][1] = init
        if show:
            self.monitors.append({'id': self.vars[name][0], 'mode': 'default', 'opcode': 'data_variable',
                                  'params': {'VARIABLE': name}, 'spriteName': None, 'value': init, 'width': 0,
                                  'height': 0, 'x': xy[0], 'y': xy[1], 'visible': True, 'sliderMin': 0,
                                  'sliderMax': 100, 'isDiscrete': True})

    def lst(self, name, items=(), show=True, xy=(330, 5), size=(145, 220)):
        self.lid(name)
        self.lists[name][1] = list(items)
        if show:
            self.monitors.append({'id': self.lists[name][0], 'mode': 'list', 'opcode': 'data_listcontents',
                                  'params': {'LIST': name}, 'spriteName': None, 'value': list(items),
                                  'width': size[0], 'height': size[1], 'x': xy[0], 'y': xy[1], 'visible': True})

    def asset(self, svg):
        data = svg.encode('utf-8')
        md5 = hashlib.md5(data).hexdigest()
        self.assets[md5 + '.svg'] = data
        return md5

    def costume(self, svg, name, cx, cy):
        md5 = self.asset(svg)
        return {'assetId': md5, 'name': name, 'md5ext': md5 + '.svg', 'dataFormat': 'svg',
                'bitmapResolution': 1, 'rotationCenterX': cx, 'rotationCenterY': cy}

    def project_json(self):
        stage_costume = self.costume(self.back_art(), 'backdrop1', 240, 180)
        if self.sprite_art == 'arrow':
            sc, nm = self.costume(svg_arrow(), 'arrow', 15, 12), 'Turtle'
        else:
            sc, nm = self.costume(svg_friend(), 'friend', 24, 24), 'Friend'
        stage = {'isStage': True, 'name': 'Stage',
                 'variables': {v[0]: [k, v[1]] for k, v in self.vars.items()},
                 'lists': {v[0]: [k, v[1]] for k, v in self.lists.items()},
                 'broadcasts': {}, 'blocks': {}, 'comments': {}, 'currentCostume': 0,
                 'costumes': [stage_costume], 'sounds': [], 'volume': 100, 'layerOrder': 0, 'tempo': 60,
                 'videoTransparency': 50, 'videoState': 'on', 'textToSpeechLanguage': None}
        sprite = {'isStage': False, 'name': nm, 'variables': {}, 'lists': {}, 'broadcasts': {},
                  'blocks': self.sprite.blocks, 'comments': {}, 'currentCostume': 0, 'costumes': [sc],
                  'sounds': [], 'volume': 100, 'layerOrder': 1, 'visible': True, 'x': self.x, 'y': self.y,
                  'size': 100, 'direction': self.direction, 'draggable': False, 'rotationStyle': 'all around'}
        return {'targets': [stage, sprite], 'monitors': self.monitors, 'extensions': self.extensions,
                'meta': {'semver': '3.0.0', 'vm': '0.2.0', 'agent': 'Math Inquirers P6 starter generator'}}

    def save(self, path):
        pj = self.project_json()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
            for fn, data in sorted(self.assets.items()):
                zi = zipfile.ZipInfo(fn, (2026, 1, 1, 0, 0, 0)); zi.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(zi, data)
            zi = zipfile.ZipInfo('project.json', (2026, 1, 1, 0, 0, 0)); zi.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(zi, json.dumps(pj, separators=(',', ':'), ensure_ascii=False))


# ------------------------------------------------------------------ lessons
# Each function returns a Proj. solved=False is the child's starter, True is the tutor answer key.

def l1(solved):
    p = Proj('L1'); S = p.sprite
    p.var('term', 0, True)
    body = [S.setv('term', 5), S.repeat(99, [S.chg('term', 3)] if solved else []), S.say(V('term'))]
    S.script(S.flag(), body)
    if solved:  # extension: say the position and the term; stop at the first term over 1000
        p.var('pos', 0, True, (5, 30))
        S.script(S.key('e'), [S.setv('term', 5), S.setv('pos', 1),
                              S.until(S.gt(V('term'), 1000), [S.chg('term', 3), S.chg('pos', 1)]),
                              S.say(S.join(S.join('term ', V('pos')), S.join(' is ', V('term'))))])
    return p


def l2(solved):
    p = Proj('L2'); S = p.sprite
    p.var('n', 0, True); p.var('d', 0, True, (5, 30)); p.var('count', 0, True, (5, 55))
    loop = [S.if_(S.eq(S.mod(V('n'), V('d')), 0), [S.chg('count', 1)]), S.chg('d', 1)] if solved else []
    tail = ([S.ifelse(S.eq(V('count'), 2), [S.say(S.join(V('n'), ' is prime'))],
                      [S.say(S.join(V('n'), ' is not prime'))])] if solved else [S.say(V('count'))])
    S.script(S.flag(), [S.setv('n', 15), S.setv('count', 0), S.setv('d', 1), S.repeat(V('n'), loop)] + tail)
    return p


def l3(solved):
    p = Proj('L3'); S = p.sprite; p.back_art = svg_numberline
    p.var('temp', 0, True)
    S.script(S.key('space'), [S.goto(0, 0)] + ([S.changex(100), S.changex(-250)] if solved else []) + [S.say(S.xpos())])
    inner = [S.chg('temp', -3), S.sayfor(V('temp'), 1)] if solved else []
    S.script(S.flag(), [S.setv('temp', 5), S.repeat(6, inner)])
    return p


def l4(solved):
    p = Proj('L4'); S = p.sprite
    p.var('out', 0, True)
    rule = S.add(S.mul(S.answer(), 3), 2) if solved else S.answer()
    S.script(S.flag(), [S.ask('IN?'), S.setv('out', rule), S.say(V('out'))])
    if solved:  # extension search programs
        p.var('n', 0, True, (5, 30))
        S.script(S.key('s'), [S.setv('n', 1), S.until(S.eq(S.sub(S.mul(8, V('n')), 5), 91), [S.chg('n', 1)]), S.say(V('n'))])
        S.script(S.key('n'), [S.setv('n', 1), S.until(S.eq(S.add(S.mul(V('n'), V('n')), V('n')), 90), [S.chg('n', 1)]), S.say(V('n'))])
    return p


def l5(solved):
    p = Proj('L5'); S = p.sprite
    p.var('a', 0, True); p.var('b', 0, True, (5, 30))
    if solved:
        S.script(S.flag(), [S.setv('a', 1), S.repeat(3, [S.setv('b', 1),
                 S.repeat(2, [S.sayfor(S.join(V('a'), V('b')), 1), S.chg('b', 1)]), S.chg('a', 1)])])
    else:
        S.script(S.flag(), [S.setv('a', 1), S.repeat(3, [S.sayfor(V('a'), 1), S.chg('a', 1)])])
    return p


def l6(solved):
    p = Proj('L6'); S = p.sprite
    p.var('heads', 0, True); p.var('a', 0, True, (5, 30)); p.var('b', 0, True, (5, 55)); p.var('doubles', 0, True, (5, 80))
    S.script(S.flag(), [S.setv('heads', 0),
                        S.repeat(1000, [S.if_(S.eq(S.rnd(1, 2), 1), [S.chg('heads', 1)])]), S.say(V('heads'))])
    S.script(S.key('d'), [S.setv('a', S.rnd(1, 6)), S.setv('b', S.rnd(1, 6)), S.say(S.add(V('a'), V('b')))])
    if solved:
        S.script(S.key('p'), [S.setv('doubles', 0),
                              S.repeat(1000, [S.setv('a', S.rnd(1, 6)), S.setv('b', S.rnd(1, 6)),
                                              S.if_(S.eq(V('a'), V('b')), [S.chg('doubles', 1)])]),
                              S.say(V('doubles'))])
    return p


def l7(solved):
    p = Proj('L7'); S = p.sprite; p.sprite_art = 'arrow'; p.extensions = ['pen']
    p.x, p.y = -50, 100

    def setup(): return [S.erase(), S.goto(-50, 100), S.point(90), S.pendown()]

    def shape(hat, sides, turn, side=100):
        S.script(hat, setup() + [S.repeat(sides, [S.move(side), S.turnr(turn)])])
    if solved:
        shape(S.flag(), 4, 90)
        shape(S.key('t'), 3, 120); shape(S.key('h'), 6, 60); shape(S.key('p'), 5, 72)
        shape(S.key('s'), 5, 144)
    else:
        S.script(S.flag(), setup())
    return p


ALPHA = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def l8(solved):
    p = Proj('L8'); S = p.sprite
    p.lst('alphabet', ALPHA)
    for nm, i in [('shift', 3), ('code', ''), ('i', 1), ('n', 0), ('m', 0)]:
        p.var(nm, i, nm in ('shift', 'code'), (5, 5 if nm == 'shift' else 30))
    let = lambda: S.letter(V('i'), S.answer())
    cipher = ([S.setv('n', S.sub(S.itemnum(let(), 'alphabet'), 1)),
               S.setv('m', S.mod(S.add(V('n'), V('shift')), 26)),
               S.setv('code', S.join(V('code'), S.itemof(S.add(V('m'), 1), 'alphabet')))] if solved else [])
    loop = S.repeat(S.length(S.answer()), [
        S.ifelse(S.gt(S.itemnum(let(), 'alphabet'), 0), cipher,
                 [S.setv('code', S.join(V('code'), let()))]),
        S.chg('i', 1)])
    S.script(S.flag(), [S.setv('shift', 3), S.ask('Type a message in CAPITAL letters'), S.setv('code', ''),
                        S.setv('i', 1), loop, S.say(V('code'))])
    if solved:  # extension: crack button, every decoding shift 1..25
        p.var('msg', '', False); p.var('s', 1, False)
        l2_ = lambda: S.letter(V('i'), V('msg'))
        decode = S.repeat(S.length(V('msg')), [
            S.ifelse(S.gt(S.itemnum(l2_(), 'alphabet'), 0),
                     [S.setv('n', S.sub(S.itemnum(l2_(), 'alphabet'), 1)),
                      S.setv('m', S.mod(S.add(S.sub(V('n'), V('s')), 26), 26)),
                      S.setv('code', S.join(V('code'), S.itemof(S.add(V('m'), 1), 'alphabet')))],
                     [S.setv('code', S.join(V('code'), l2_()))]),
            S.chg('i', 1)])
        S.script(S.key('k'), [S.ask('Type a coded message in CAPITAL letters'), S.setv('msg', S.answer()),
                              S.setv('s', 1),
                              S.repeat(25, [S.setv('code', ''), S.setv('i', 1), decode,
                                            S.sayfor(S.join(S.join('shift ', V('s')), S.join(': ', V('code'))), 1),
                                            S.chg('s', 1)])])
    return p


def l9(solved):
    p = Proj('L9'); S = p.sprite
    p.lst('data', [5, 9, 6, 12] if solved else [])
    p.var('total', 0, True); p.var('i', 0, True, (5, 30))
    inner = [S.chg('total', S.itemof(V('i'), 'data')), S.chg('i', 1)] if solved else []
    S.script(S.flag(), [S.setv('total', 0), S.setv('i', 1), S.repeat(S.lenlist('data'), inner),
                        S.say(S.div(V('total'), S.lenlist('data')))])
    if solved:  # extension: largest value
        p.var('max', 0, True, (5, 55))
        S.script(S.key('m'), [S.setv('max', S.itemof(1, 'data')), S.setv('i', 1),
                              S.repeat(S.lenlist('data'), [S.if_(S.gt(S.itemof(V('i'), 'data'), V('max')),
                                                                 [S.setv('max', S.itemof(V('i'), 'data'))]),
                                                           S.chg('i', 1)]),
                              S.say(V('max'))])
    return p


def l10a(solved):
    p = Proj('L10A'); S = p.sprite
    p.var('n', 0, False); p.var('out', 0, True)
    hi, mulv, off = (50, 4, -1) if solved else (20, 3, 4)
    rule = S.add(S.mul(V('n'), mulv), off) if off >= 0 else S.sub(S.mul(V('n'), mulv), -off)
    S.script(S.flag(), [S.setv('n', S.rnd(1, hi)), S.setv('out', rule),
                        S.sayfor(S.join('OUT is ', V('out')), 2), S.ask('What was n?'),
                        S.ifelse(S.eq(S.answer(), V('n')), [S.sayfor('Correct!', 2)],
                                 [S.sayfor(S.join('No, n was ', V('n')), 2)])])
    return p


def l10b(solved):
    p = Proj('L10B'); S = p.sprite
    p.var('n', 0, True); p.var('d', 0, False); p.var('count', 0, True, (5, 30))
    if not solved:
        S.script(S.flag(), [S.ask('Which number?'), S.setv('n', S.answer()), S.setv('count', 0), S.setv('d', 1),
                            S.repeat(V('n'), [S.if_(S.eq(S.mod(V('n'), V('d')), 0), [S.chg('count', 1)]), S.chg('d', 1)]),
                            S.ifelse(S.eq(V('count'), 2), [S.say(S.join(V('n'), ' is prime'))],
                                     [S.say(S.join(V('n'), ' is not prime'))])])
    else:  # twist: how many primes up to 30?
        p.var('primes', 0, True, (5, 55))
        S.script(S.flag(), [S.setv('primes', 0), S.setv('n', 2),
                            S.repeat(29, [S.setv('count', 0), S.setv('d', 1),
                                          S.repeat(V('n'), [S.if_(S.eq(S.mod(V('n'), V('d')), 0), [S.chg('count', 1)]), S.chg('d', 1)]),
                                          S.if_(S.eq(V('count'), 2), [S.chg('primes', 1)]),
                                          S.chg('n', 1)]),
                            S.say(S.join('Primes up to 30: ', V('primes')))])
    return p


def l10c(solved):
    p = Proj('L10C'); S = p.sprite
    p.var('a', 0, False); p.var('b', 0, False); p.var('sevens', 0, True); p.var('target', 7, True, (5, 30))
    tgt = V('target') if solved else 7
    S.script(S.flag(), [S.setv('target', 8) if solved else None, S.setv('sevens', 0),
                        S.repeat(1000, [S.setv('a', S.rnd(1, 6)), S.setv('b', S.rnd(1, 6)),
                                        S.if_(S.eq(S.add(V('a'), V('b')), tgt), [S.chg('sevens', 1)])]),
                        S.say(V('sevens'))])
    return p


DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def l10d(solved):
    p = Proj('L10D'); S = p.sprite
    p.var('hour', 0, True); p.var('jump', 0, True, (5, 30))
    if not solved:
        S.script(S.flag(), [S.ask('Start hour (1 to 12)?'), S.setv('hour', S.answer()),
                            S.ask('Jump how many hours?'), S.setv('jump', S.answer()),
                            S.setv('hour', S.mod(S.add(V('hour'), V('jump')), 12)),
                            S.if_(S.eq(V('hour'), 0), [S.setv('hour', 12)]),
                            S.say(S.join('The clock shows ', V('hour')))])
    else:  # twist: Day Jumper (mod 7 and a list of day names)
        p.lst('days', DAYS, True)
        p.var('today', 0, True, (5, 55))
        S.script(S.flag(), [S.ask('Today is day number (1 = Monday, 7 = Sunday)?'), S.setv('today', S.answer()),
                            S.ask('Jump how many days?'), S.setv('jump', S.answer()),
                            S.setv('hour', S.mod(S.add(S.sub(V('today'), 1), V('jump')), 7)),
                            S.say(S.join('That day is ', S.itemof(S.add(V('hour'), 1), 'days')))])
    return p


FILES = [('L1_Sequence_Tester', l1), ('L2_Prime_Checker', l2), ('L3_Below_Zero', l3), ('L4_Function_Machine', l4),
         ('L5_Every_Order', l5), ('L6_Chance_Lab', l6), ('L7_Turtle_Start', l7), ('L8_Code_Machine', l8),
         ('L9_Mean_Machine', l9), ('L10A_Mystery_Machine', l10a), ('L10B_Prime_or_Not', l10b),
         ('L10C_Lucky_Seven', l10c), ('L10D_Clock_Jumper', l10d)]


def build_all(root=HERE):
    out = []
    for name, fn in FILES:
        fn(False).save(os.path.join(root, 'starters', name + '.sb3'))
        fn(True).save(os.path.join(root, 'answers', name + '_ANSWER.sb3'))
        out.append(name)
    # one bundle of the child starters only, for emailing to families (never includes the answer keys)
    with zipfile.ZipFile(os.path.join(root, 'P6_Scratch_Starters_for_families.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
        for name, _ in FILES:
            zi = zipfile.ZipInfo(name + '.sb3', (2026, 1, 1, 0, 0, 0)); zi.compress_type = zipfile.ZIP_DEFLATED
            with open(os.path.join(root, 'starters', name + '.sb3'), 'rb') as fh:
                z.writestr(zi, fh.read())
    return out


if __name__ == '__main__':
    print('built', len(build_all()), 'starters and answer keys')
