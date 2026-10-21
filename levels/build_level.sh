#!/bin/bash
# Build all printed materials for a finished level:  bash levels/build_level.sh 4
set -e
N=$1; R=/home/claude/math-inquirers; cd $R
python3 levels/normfoot.py $N
(cd p$N && node workbook_html.js && python3 wb_pdf.py && node guide.js)
(cd hp && python3 docx2pdf_designed.py ../p$N/P${N}_Holiday_Program_Guide.docx ../p$N/Math_Inquirers_P${N}_Tutor_Guide.pdf "Math Inquirers P$N Tutor Guide" "Holiday program for the Primary $N level" "Math Inquirers P$N • Tutor guide")
(cd hp && python3 weekly_level.py ../p$N/Math_Inquirers_P${N}_Student_Workbook_Designed.pdf ../p$N/Math_Inquirers_P${N}_Tutor_Guide.pdf ../p$N/Math_Inquirers_P${N}_Weekly_PDFs.zip && python3 parent_pack_level.py p$N)
python3 levels/scheme.py p$N
for f in p$N/*.pdf; do python3 -c "from pypdf import PdfReader;import sys;print(sys.argv[1],len(PdfReader(sys.argv[1]).pages))" $f; done
