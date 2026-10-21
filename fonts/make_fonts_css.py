"""Write fonts.css pointing at the locally installed Fredoka and Nunito Sans files.
Run once per machine:  cd fonts && npm install && python3 make_fonts_css.py"""
import os
F=os.path.join(os.path.dirname(os.path.abspath(__file__)),'node_modules','@fontsource')
r=[]
for w in (400,500,600,700): r.append("@font-face{font-family:'Fredoka';font-weight:%d;src:url('file://%s/fredoka/files/fredoka-latin-%d-normal.woff2') format('woff2')}"%(w,F,w))
for w in (400,600,700,800): r.append("@font-face{font-family:'Nunito Sans';font-weight:%d;src:url('file://%s/nunito-sans/files/nunito-sans-latin-%d-normal.woff2') format('woff2')}"%(w,F,w))
r.append("@font-face{font-family:'Nunito Sans';font-style:italic;font-weight:400;src:url('file://%s/nunito-sans/files/nunito-sans-latin-400-italic.woff2') format('woff2')}"%F)
open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'fonts.css'),'w').write('\n'.join(r))
print('fonts.css written')
