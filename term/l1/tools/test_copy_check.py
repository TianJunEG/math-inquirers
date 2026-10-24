"""Tests for the copy-check source selection. Run: python3 term/l1/tools/test_copy_check.py"""
import os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate

PHRASE = 'mei keeps seven blue pebbles beside nine green shells today'  # 10 words, invented


def mk(root, rel, text):
    p = os.path.join(root, rel); os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w').write(text)


def overlap(root, own_text):
    own = validate.shingles(validate.std_strip(own_text))
    return [f for f, t in validate.external_sources(root) if own & validate.shingles(validate.std_strip(t))]


with tempfile.TemporaryDirectory() as r:
    mk(r, 'docs/books/p1_non_routine_catalogue.md', 'Our catalogue: ' + PHRASE)
    mk(r, 'docs/books/p2_non_routine_catalogue.md', PHRASE)
    mk(r, 'docs/sasmo/g1_original_problems_draft.md', PHRASE)
    mk(r, 'docs/books/word_problems_g1_g2_original_draft.md', PHRASE)
    assert overlap(r, PHRASE) == [], 'own catalogues/drafts must not count as external'
    mk(r, 'docs/books/private_p1_papers/non_routine_questions.md', 'Q3. ' + ' '.join(PHRASE.split()[:8]) + ' ok')  # 8-word overlap
    assert overlap(r, PHRASE) == ['docs/books/private_p1_papers/non_routine_questions.md'], 'private extract overlap must be caught'
    mk(r, 'docs/sasmo/private_solution_notes_g1.md', ' '.join(PHRASE.split()[2:9]))  # exactly 7 words
    assert len(overlap(r, PHRASE)) == 2
print('ok: catalogue overlap passes, 8-word overlap with a private extract fails')
