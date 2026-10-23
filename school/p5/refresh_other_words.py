import subprocess,glob,re,json
R='/home/user/math-inquirers/school/'
J=R+'p5/gen/other_levels_words.json'
ws=set(json.load(open(J)))
for l in ['p1','p2','p3','p4','p6']:
    for f in glob.glob(R+f'{l}/out/*Answer_Key*.pdf'):
        t=subprocess.run(['pdftotext','-layout',f,'-'],capture_output=True,text=True).stdout
        ws|={w.lower() for w in re.findall(r'(?:[Cc]ode word|Word|WORD)s?:? +([A-Z]{4,9})\b',t)}
json.dump(sorted(ws),open(J,'w'))
print(len(ws),'melody' in ws)
