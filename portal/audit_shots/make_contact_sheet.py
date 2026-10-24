#!/usr/bin/env python3
"""Builds portal/audit_shots/portal_screens.pdf (one page per screen, with captions) from the PNGs and shots.json written by audit_frontend.py."""
import json, os
from PIL import Image
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
HERE = os.path.dirname(os.path.abspath(__file__))
shots = json.load(open(os.path.join(HERE, 'shots.json')))
tags = []
for s in shots:
    if s['tag'] not in [t for t, _ in tags]: tags.append((s['tag'], s['caption']))
tags.sort()
W, H = landscape(A4)
c = canvas.Canvas(os.path.join(HERE, 'portal_screens.pdf'), pagesize=(W, H))
c.setTitle('Portal screens (audit round 1)')
def find(tag, w, scheme):
    for s in shots:
        if s['tag'] == tag and s['w'] == w and s['scheme'] == scheme: return os.path.join(HERE, s['file'])
c.setFont('Helvetica-Bold', 20); c.drawString(40, H - 80, 'Math Inquirers portal screens: audit round 1')
c.setFont('Helvetica', 11)
for i, t in enumerate(['Mocked-Supabase Playwright harness, TEST data only. Nothing deployed.', 'Each page: 375px light, 375px dark, 1100px light (tall pages are cropped to the top, see the full PNGs).', 'Files: portal/audit_shots/NN_name_WIDTH_light|dark.png. Findings: docs/audit_final/portal_ui_audit_round1.md']): c.drawString(40, H - 110 - 16 * i, t)
c.showPage()
for tag, cap in tags:
    c.setFont('Helvetica-Bold', 13); c.drawString(30, H - 30, tag)
    c.setFont('Helvetica', 9.5)
    words, line, y = cap.split(), '', H - 46
    for wd in words:
        if c.stringWidth(line + ' ' + wd, 'Helvetica', 9.5) > W - 60: c.drawString(30, y, line); y -= 12; line = wd
        else: line = (line + ' ' + wd).strip()
    c.drawString(30, y, line)
    top = y - 14; boxh = top - 24
    x = 30
    for w, scheme, label in ((375, 'light', '375px light'), (375, 'dark', '375px dark'), (1100, 'light', '1100px light')):
        f = find(tag, w, scheme)
        if not f: continue
        im = Image.open(f).convert('RGB'); iw, ih = im.size
        cropped = False
        maxh = iw * (2.1 if w == 375 else 1.0)
        if ih > maxh: im = im.crop((0, 0, iw, int(maxh))); ih = int(maxh); cropped = True
        bw = (W - 60 - 20) * (0.27 if w == 375 else 0.46)
        sc = min(bw / iw, boxh / ih); dw, dh = iw * sc, ih * sc
        c.drawImage(ImageReader(im), x, top - dh, dw, dh)
        c.setFont('Helvetica', 8); c.drawString(x, top - dh - 10, label + (' (top part)' if cropped else ''))
        x += dw + 10
    c.showPage()
c.save(); print('pdf pages:', len(tags) + 1)
