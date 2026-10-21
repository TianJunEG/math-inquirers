# Math Inquirers

Primary 1 maths holiday program by Preciouslyours Pte Ltd, Singapore.
Slogan: **Notice it. Test it. Explain why.**

This repository holds the source files that build every program document, plus copies of the finished files.

## Finished files (`outputs/`)

| Folder | What is in it |
|---|---|
| `outputs/workbook/` | Student workbook: designed PDF (A + D style) and the Word version |
| `outputs/designed/` | Tutor guide, question bank, parent practice pack, Lesson 6 trial, readiness tracker, weekly email pack, What Learners Get, weekly PDFs (zip), free taster, K2 readiness check, lesson review |
| `outputs/brand/` | Workbook style options, mascot sketches |
| `outputs/older/` | Earlier versions kept for reference |

## Source folders

| Folder | Builds |
|---|---|
| `hp/` | Workbook, tutor guide, question bank, Lesson 6 trial, weekly email pack, readiness tracker; lesson content lives in `lessons.js`, `scripts.js`, `qbank.json` |
| `deck/` | Slide content data (`data.js`), also read by the tutor guide |
| `split/` | The 10 published lesson decks and the 60-minute trial deck (`project/deck.json` + `project/slides/*.html`) |
| `diag/` | Diagram slides added to the decks |
| `taster/` | Free taster PDF for parents |
| `k2/` | K2 readiness check |
| `wbstyles/` | Workbook style mock-ups |
| `mascot/` | Mascot sketches (placeholders until a designer draws the final) |
| `website/` | Website prototype (`referral.html`), sign-up page (`mi_signup.html`, built by `lp_build.py`), parent questions hub (`hub/`) |
| `review/` | Lesson pitch and slide review (markdown) |
| `p1/` | Older enrichment worksheet set |

## Rebuilding

One-time setup (Node, Python 3, Playwright with Chromium, python-docx, docx for Node):

```bash
cd fonts && npm install && python3 make_fonts_css.py && cd ..
npm install -g docx
```

Common builds (run inside `hp/`):

```bash
# Student workbook, designed PDF
NODE_PATH=$(npm root -g) node workbook_html.js && python3 wb_pdf.py

# Word versions
NODE_PATH=$(npm root -g) node workbook.js     # workbook .docx
NODE_PATH=$(npm root -g) node guide.js        # tutor guide .docx
NODE_PATH=$(npm root -g) node trial6.js       # Lesson 6 trial .docx

# Parent practice pack (A + D style PDF, from qbank.json)
python3 parent_pack.py

# Weekly student and tutor PDFs (zip), sliced from the designed workbook and tutor guide
python3 weekly.py

# Any Word file -> designed PDF
python3 docx2pdf_designed.py <file.docx> <out.pdf> "<Title>" "<Subtitle>" "<Footer text>"
```

Other builds: `python3 taster/gen.py && python3 taster/pdf.py` (run in `taster/`), `python3 k2/k2.py` (in `k2/`), `python3 lp_build.py` (in `website/`), `python3 build.py` (in `website/hub/`).

## Published pages (private until shared)

- Lesson decks 1 to 10 and the Lesson 6 trial deck are Claude Slides artifacts; their sources are in `split/`.
- Website prototype, sign-up page and parent questions hub are Claude artifacts; their sources are in `website/`.

## Open items

See the "To-do list" section in the Math Inquirers: All Documents doc.
