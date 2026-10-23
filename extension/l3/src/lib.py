"""Authoring helpers for the Level 3 unit generators (extension/l3/src/uNN.py write extension/data/l3_uNN.json)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'data')


def A(value, text=None, **kw):
    """answer: value = list of strings (one per blank) or one value."""
    if not isinstance(value, (list, tuple)):
        value = [value]
    value = [str(v) for v in value]
    d = {'value': value, 'text': text if text is not None else ', '.join(value)}
    d.update(kw)
    return d


def P(label, text, ans):
    return {'label': label, 'text': text, 'answer': ans}


class Unit:
    def __init__(self, n, title, topic, goal, **kw):
        self.u = {'schema_version': 1, 'level': 3, 'unit': n, 'id': f'L3U{n:02d}', 'title': title, 'topic': topic, 'holiday_lesson': n, 'goal': goal}
        self.u.update(kw)
        self.n = n
        self.items = []
        self.cnt = {'S': 0, 'T': 0, 'G': 0, 'C': 0}

    def learn(self, intro, example, howto, try_, **extra):
        tr = dict(try_)
        tr['id'] = f'L3U{self.n:02d}-L01'
        self.u['learn'] = dict({'intro': intro, 'example': example, 'howto': howto, 'try': tr}, **extra)

    def add(self, letter, page, text, ans=None, why='', parts=None, **kw):
        self.cnt[letter] += 1
        tier = {'S': 'start', 'T': 'think', 'G': 'go', 'C': 'quiz'}[letter]
        it = {'id': f'L3U{self.n:02d}-{letter}{self.cnt[letter]:02d}', 'tier': tier}
        if letter != 'C':
            it['page'] = page
        else:
            it['page'] = 6
        it['text'] = text
        if parts:
            it['parts'] = parts
        else:
            it['answer'] = ans
        it['explanation'] = why
        it.update(kw)
        self.items.append(it)
        return it['id']

    def S(self, page, text, ans=None, why='', parts=None, **kw):
        return self.add('S', page, text, ans, why, parts, **kw)

    def T(self, text, ans=None, why='', parts=None, **kw):
        return self.add('T', 4, text, ans, why, parts, **kw)

    def G(self, text, ans=None, why='', parts=None, **kw):
        return self.add('G', 5, text, ans, why, parts, **kw)

    def C(self, text, ans=None, why='', parts=None, **kw):
        return self.add('C', 6, text, ans, why, parts, **kw)

    def save(self):
        self.u['items'] = self.items
        for k in ('snug',):
            pass
        path = os.path.join(DATA, f'l3_u{self.n:02d}.json')
        json.dump(self.u, open(path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
        c = {t: sum(1 for i in self.items if i['tier'] == t) for t in ('start', 'think', 'go', 'quiz')}
        pages = {p: sum(1 for i in self.items if i['tier'] == 'start' and i['page'] == p) for p in (1, 2, 3)}
        print(path, c, 'start per page', pages)
