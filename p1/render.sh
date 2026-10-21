#!/bin/bash
cd "$(dirname "$0")"
NODE_PATH=$(npm root -g) node build.js || exit 1
for f in P1_Enrichment_Worksheets P1_Teacher_Guide_and_Answer_Key; do
  python3 /mnt/skills/public/docx/scripts/office/soffice.py --headless --convert-to pdf $f.docx >/dev/null 2>&1
  echo $f $(pdfinfo $f.pdf | grep Pages)
done
rm -f pg-*.jpg gd-*.jpg
pdftoppm -jpeg -r 60 P1_Enrichment_Worksheets.pdf pg
pdftoppm -jpeg -r 60 P1_Teacher_Guide_and_Answer_Key.pdf gd
python3 -I - <<'PY'
from PIL import Image
import glob
for pre in ('pg','gd'):
    fs=sorted(glob.glob(pre+'-*.jpg')); ims=[Image.open(f) for f in fs]
    w,h=ims[0].size; cols=4; rows=(len(ims)+cols-1)//cols
    sheet=Image.new('RGB',(w*cols,h*rows),'white')
    for i,im in enumerate(ims): sheet.paste(im,((i%cols)*w,(i//cols)*h))
    sheet.save(pre+'_sheet.jpg')
PY
