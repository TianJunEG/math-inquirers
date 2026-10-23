"""Clean-and-modern restyle for generated slides, with a per-level accent and 'inquiry bubble' decoration.
Usage: python3 levels/restyle.py split/p2l1 [...]   (idempotent; safe to run after regenerating a deck; level taken from the folder name)."""
import sys,os,re,glob
ACC={'1':('#1F7A6F','#14574F'),'2':('#2A7DC9','#1B5A94'),'3':('#3E8E41','#2B6A2E'),'4':('#7B4FB5','#5A3787'),'5':('#D9662B','#A84A1B'),'6':('#C2386B','#8F2551')}
def level_of(path):
    k=os.path.basename(path.rstrip('/'))
    m=re.match(r'p(\d)l',k); return m.group(1) if m else '1'
def bar(a):
    return ('<div data-deco="bar" style="position:absolute;left:0;top:0;width:1920px;height:18px;display:flex">'
            f'<div style="flex:5;background:#1B2A49"></div><div style="flex:3;background:{a}"></div><div style="flex:1;background:#FFC93C"></div></div>')
def bubbles(kind,a):
    fill=a if kind=='navy' else 'rgba(255,255,255,0.22)'
    return ('<div data-deco="bubbles" style="position:absolute;left:0;top:0;width:1920px;height:1080px;overflow:hidden">'
     '<svg width="1920" height="1080" viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" style="position:absolute;left:0;top:0">'
     f'<g transform="translate(1920,0) scale(0.72) translate(-1920,0)"><g><path d="M1500 80 C1420 80 1380 150 1410 210 C1340 230 1330 330 1410 360 C1400 440 1500 480 1570 430 C1630 480 1760 470 1790 390 C1880 380 1900 280 1840 230 C1880 150 1810 70 1730 100 C1690 40 1560 40 1500 80 Z" fill="{fill}"/>'
     '</g>'
     '<text x="1610" y="340" font-size="250" font-weight="800" text-anchor="middle" fill="#FFF9EC" font-family="Fredoka, Arial, sans-serif">?</text>'
     '<g transform="translate(-590,-680)"><path d="M1640 800 Q1640 740 1700 740 L1800 740 Q1860 740 1860 800 L1860 850 Q1860 910 1800 910 L1740 910 L1690 960 L1700 910 Q1640 910 1640 850 Z" fill="#FFC93C"/>'
     '<text x="1750" y="868" font-size="120" font-weight="800" text-anchor="middle" fill="#1B2A49" font-family="Fredoka, Arial, sans-serif">!</text></g></g></svg></div>')
OLDB=re.compile(r'<div data-deco="bubbles".*?</svg></div>',re.S)
OLD=re.compile(r'<div style="position:absolute;left:0;top:0;width:1920px;height:1080px;overflow:hidden"><div style="position:absolute;right:-180px.*?</div></div>',re.S)
def fix(s,lv):
    a,ad=ACC[lv]
    m=re.search(r'<section ([^>]*)style="([^"]*)"',s)
    if not m: return s
    if 'data-theme="modern"' not in s and 'data-theme="modern2"' not in s:
        st=m.group(2)
        if 'background:#1B2A49' in st: kind='navy'
        elif 'background:#1F7A6F' in st or 'linear-gradient(135deg,#1F7A6F' in st: kind='teal'
        else: kind='light'
        if kind=='light': st=st.replace('background:#FFF9EC','background:#F3F6FB')
        elif kind=='navy': st=st.replace('background:#1B2A49','background:linear-gradient(135deg,#1B2A49 0%,#101B33 100%)')
        else: st=st.replace('background:#1F7A6F','background:linear-gradient(135deg,#1F7A6F 0%,#14574F 100%)')
        st+=';position:relative;overflow:hidden'
        s=s.replace(m.group(0),f'<section {m.group(1)}data-theme="modern2" style="{st}"',1)
        i=s.index('>',s.index('data-theme="modern2"'))+1
        s=s[:i]+'\n'+(bar('#1F7A6F') if kind=='light' else bubbles(kind,'#1F7A6F'))+s[i:]
        if kind=='light':
            s=s.replace('background:#FFFFFF;','background:#FFFFFF;border:2px solid #DCE4F0;box-shadow:0 6px 18px rgba(27,42,73,0.08);')
            s=re.sub(r'(<h2 style=")',r'\1border-left:14px solid #1F7A6F;padding-left:28px;',s)
            s=s.replace('right:128px;top:64px;font-size:28px;font-weight:700;letter-spacing:2px;color:#1F7A6F','right:128px;top:52px;font-size:26px;font-weight:800;letter-spacing:2px;color:#1F7A6F;background:#FFFFFF;border:2px solid #1F7A6F;border-radius:999px;padding:6px 22px')
    elif 'data-theme="modern2"' in s and OLDB.search(s) and 'cx="1360"' in s:
        kind='navy' if 'background:linear-gradient(135deg,#1B2A49' in s else 'teal'
        s=OLDB.sub(lambda _:bubbles(kind,'#1F7A6F' if lv!='1' else '#1F7A6F'),s,count=1)
    elif 'data-theme="modern"' in s:   # upgrade v1 (circles) -> v2 (bubbles)
        s=s.replace('data-theme="modern"','data-theme="modern2"',1)
        if OLD.search(s):
            kind='navy' if 'background:linear-gradient(135deg,#1B2A49' in s else 'teal'
            s=OLD.sub(lambda _:bubbles(kind,'#1F7A6F'),s,count=1)
    return s.replace('#1F7A6F',a).replace('#14574F',ad) if lv!='1' else s
for d in sys.argv[1:]:
    n=0;lv=level_of(d)
    for f in glob.glob(os.path.join(d,'project','slides','*.html')):
        a=open(f).read(); b=fix(a,lv)
        if a!=b: open(f,'w').write(b); n+=1
    try:
        sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import mi_deco; n+=mi_deco.apply(d)   # Mi the dolphin (levels 1-3), idempotent
    except ImportError: pass
    print(d,n)
