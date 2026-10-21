import sys,glob,subprocess,os
from PIL import Image
pdf,pre=sys.argv[1],sys.argv[2]; cols=int(sys.argv[3]) if len(sys.argv)>3 else 8
for f in glob.glob(pre+'-*.jpg'): os.remove(f)
subprocess.run(['pdftoppm','-jpeg','-r','28',pdf,pre])
fs=sorted(glob.glob(pre+'-*.jpg')); ims=[Image.open(f) for f in fs]; w,h=ims[0].size
rows=(len(ims)+cols-1)//cols; S=Image.new('RGB',(w*cols,h*rows),'white')
for i,a in enumerate(ims): S.paste(a,((i%cols)*w,(i//cols)*h))
S.save(pre+'_sheet.jpg'); print(len(ims),S.size)
