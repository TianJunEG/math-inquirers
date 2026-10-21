"""Clean-and-modern restyle for generated slides. Usage: python3 levels/restyle.py split/p2l1 [...]  (idempotent; marks sections with data-theme="modern")."""
import sys,os,re,glob
BAR=('<div style="position:absolute;left:0;top:0;width:1920px;height:18px;display:flex">'
     '<div style="flex:5;background:#1B2A49"></div><div style="flex:3;background:#1F7A6F"></div><div style="flex:1;background:#FFC93C"></div></div>')
def deco_dark(bg):
    return ('<div style="position:absolute;left:0;top:0;width:1920px;height:1080px;overflow:hidden"><div style="position:absolute;right:-180px;top:-180px;width:720px;height:720px;border-radius:50%%;background:%s;opacity:0.9"></div>'
            '<div style="position:absolute;right:140px;bottom:-120px;width:300px;height:300px;border-radius:50%%;background:#FFC93C;opacity:0.9"></div></div>')%('#1F7A6F' if bg=='navy' else '#2B9486')
def fix(s):
    if 'data-theme="modern"' in s: return s
    m=re.search(r'<section ([^>]*)style="([^"]*)"',s)
    if not m: return s
    st=m.group(2)
    if 'background:#1B2A49' in st: kind='navy'
    elif 'background:#1F7A6F' in st: kind='teal'
    else: kind='light'
    if kind=='light':
        st=st.replace('background:#FFF9EC','background:#F3F6FB')
    elif kind=='navy':
        st=st.replace('background:#1B2A49','background:linear-gradient(135deg,#1B2A49 0%,#101B33 100%)')
    else:
        st=st.replace('background:#1F7A6F','background:linear-gradient(135deg,#1F7A6F 0%,#14574F 100%)')
    st+=';position:relative;overflow:hidden'
    new='<section %sdata-theme="modern" style="%s">'%(m.group(1),st)
    s=s[:m.start()]+new+s[m.end():] if False else s.replace(m.group(0),new[:-1],1)
    # insert decoration right after the opening tag
    i=s.index('>',s.index('data-theme="modern"'))+1
    s=s[:i]+'\n'+(BAR if kind=='light' else deco_dark(kind))+s[i:]
    if kind=='light':
        # white cards get a soft border and shadow
        s=s.replace('background:#FFFFFF;','background:#FFFFFF;border:2px solid #DCE4F0;box-shadow:0 6px 18px rgba(27,42,73,0.08);')
        # headings get a teal accent bar
        s=re.sub(r'(<h2 style=")',r'\1border-left:14px solid #1F7A6F;padding-left:28px;',s)
        s=s.replace('right:128px;top:64px;font-size:28px;font-weight:700;letter-spacing:2px;color:#1F7A6F','right:128px;top:52px;font-size:26px;font-weight:800;letter-spacing:2px;color:#1F7A6F;background:#FFFFFF;border:2px solid #1F7A6F;border-radius:999px;padding:6px 22px')
    return s
for d in sys.argv[1:]:
    n=0
    for f in glob.glob(os.path.join(d,'project','slides','*.html')):
        a=open(f).read(); b=fix(a)
        if a!=b: open(f,'w').write(b); n+=1
    print(d,n)
