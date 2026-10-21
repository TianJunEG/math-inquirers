#!/bin/bash
cd "$(dirname "$0")"
NODE_PATH=$(npm root -g) node "$1.js" || exit 1
f=$2
python3 /mnt/skills/public/docx/scripts/office/soffice.py --headless --convert-to pdf $f.docx >/dev/null 2>&1
echo $f $(pdfinfo $f.pdf | grep Pages)
rm -f ${3}-*.jpg
pdftoppm -jpeg -r 55 $f.pdf $3
python3 -I - $3 <<'PY'
import sys,glob
from PIL import Image
pre=sys.argv[1]
fs=sorted(glob.glob(pre+'-*.jpg')); ims=[Image.open(f) for f in fs]
w,h=ims[0].size; cols=6
for part in range(0,len(ims),12):
    chunk=ims[part:part+12]; rows=(len(chunk)+cols-1)//cols
    sheet=Image.new('RGB',(w*cols,h*rows),'white')
    for i,im in enumerate(chunk): sheet.paste(im,((i%cols)*w,(i//cols)*h))
    sheet.save(f'{pre}_sheet{part//12+1}.jpg')
print(len(ims),'pages')
PY
