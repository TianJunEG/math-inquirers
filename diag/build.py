import re,json,shutil,os,sys
sys.path.insert(0,'.')
import panels,explore
S='/tmp/claude-0/-home-claude/2972495b-87c0-5185-98d8-712902f3b1b5/scratchpad/'
for n in list(range(1,11))+['6s']:
    src=S+f'split_bak/l{n}/project';dst=S+f'split/l{n}/project'
    shutil.rmtree(dst,ignore_errors=True);shutil.copytree(src,dst)
    k=int(str(n).rstrip('s'))
    fn=f'{dst}/slides/l{k}-explore1.html';h=open(fn).read()
    pat=re.compile(r'<p style="border:3px dashed[^>]*>Picture:[^<]*</p>')
    assert pat.search(h),(n,'no placeholder')
    h=h.replace('padding:128px 128px 160px','padding:72px 128px 100px',1).replace('padding:36px 40px;display:flex;flex-direction:column;gap:14px','padding:22px 40px;display:flex;flex-direction:column;gap:8px',1).replace('font-size:36px;font-weight:600;padding-left:48px;display:flex;flex-direction:column;gap:10px','font-size:32px;font-weight:600;padding-left:48px;display:flex;flex-direction:column;gap:6px',1).replace('gap:28px">','gap:20px">',1)
    h=pat.sub('<div style="background:#FFFFFF;border-radius:24px;padding:10px 20px">'+explore.EX[k]()+'</div>',h)
    open(fn,'w').write(h)
    if n=='6s': continue
    a,b,ca,cb=panels.CH[k]
    sid=f'l{k}-chdiag'
    card=lambda svg,cap: f'<div style="background:#FFFFFF;border-radius:24px;padding:20px 24px;display:flex;flex-direction:column;gap:10px;flex:1;min-width:0"><p style="font-size:28px;font-weight:700;color:#1F7A6F">{cap}</p>{svg}</div>'
    html=f'''<section id="{sid}" data-transition="fade" style="background:#FFF9EC;color:#1B2A49;font-family:'Nunito Sans', Arial, sans-serif;padding:96px 128px 140px;display:flex;flex-direction:column;gap:24px">
<p style="position:absolute;right:128px;top:48px;font-size:28px;font-weight:700;letter-spacing:2px;color:#1F7A6F">65–80 MIN</p>
<h2 style="font-family:'Fredoka', Arial, sans-serif;font-size:60px;font-weight:600;line-height:1.1">Challenge: see it</h2>
<div style="display:flex;gap:32px;align-items:flex-start">{card(a(),ca)}{card(b(),cb)}</div>
<p style="position:absolute;left:128px;bottom:48px;width:1400px;font-size:24px;color:#5B6785">Math Inquirers Holiday Program  •  Notice it. Test it. Explain why.</p>
<aside>Show after pairs have tried the Challenge, or if they are stuck. The diagrams show the problem, not the answer. Ask: What do you notice? What do we know? What do we not know yet? Can you draw it? Answers are in the Challenge slide notes.</aside>
</section>'''
    open(f'{dst}/slides/{sid}.html','w').write(html)
    d=json.load(open(f'{dst}/deck.json'));o=d['order'];i=o.index(f'l{k}-challenge');o.insert(i+1,sid)
    json.dump(d,open(f'{dst}/deck.json','w'),indent=1)
print('built')
