# Put the level into every deck footer:  python3 levels/normfoot.py 3   (run after any gen_pN*.py)
import sys, glob
N = sys.argv[1]
old = 'Math Inquirers Holiday Program  •  Notice it. Test it. Explain why.'
new = f'Math Inquirers P{N} Holiday Program  •  Notice it. Test it. Explain why.'
c = 0
for f in glob.glob(f'split/p{N}l*/project/slides/*.html'):
    s = open(f).read()
    if old in s: open(f, 'w').write(s.replace(old, new)); c += 1
print('footers fixed:', c)
