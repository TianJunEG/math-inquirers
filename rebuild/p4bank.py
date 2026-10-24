"""Helper for the Level 4 slide generators: read the Think harder items from the lesson source, so the
slide shows exactly the same four questions (and answers in the notes) as the printed Think harder page.
The printed page is the first four items of qbank.stretch (see p4/workbook_html.js)."""
import json, os, subprocess

R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def _bank(n):
    code = "const c=require('%s/p4/content/l%d.js');console.log(JSON.stringify(c.qbank))" % (R, n)
    return json.loads(subprocess.run(['node', '-e', code], capture_output=True, text=True, check=True).stdout)


def th_items(n):
    """[('1.', question), ...] for the four printed Think harder items."""
    return [(f'{i + 1}.', x['q']) for i, x in enumerate(_bank(n)['stretch'][:4])]


def th_notes(n):
    """Answers text for the slide notes, taken from the same four items."""
    return 'Answers (same four questions as the printed Think harder page): ' + ' '.join(
        f'{i + 1}) {x["a"]}' for i, x in enumerate(_bank(n)['stretch'][:4]))


def go_further(n):
    """[(printed number, question)] for the three printed Go further items (last three Challenge items, numbered 5 to 7)."""
    return [(i + 5, x['q']) for i, x in enumerate(_bank(n)['challenge'][-3:])]


def gf_numbers(n, texts):
    """For each slide Challenge question text (in slide order), the printed Go further number it matches (by its first 40 characters)."""
    gf = go_further(n)
    out = []
    for t in texts:
        hit = [num for num, q in gf if q[:40] == t[:40]]
        out.append(hit[0] if hit else None)
    return out
