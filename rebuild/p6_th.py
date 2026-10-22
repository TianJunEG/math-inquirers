"""Think harder items for the P6 slides: read from the SAME th array the printed workbook uses (p6/data.js: lessons[n-1].th)."""
import json,os,subprocess
_H=os.path.dirname(os.path.abspath(__file__))
def get(n):
    js="process.stdout.write(JSON.stringify(require(process.argv[1]).lessons[%d].th))"%(n-1)
    out=subprocess.run(['node','-e',js,os.path.abspath(os.path.join(_H,'..','p6','data.js'))],capture_output=True,text=True,check=True).stdout
    return json.loads(out)
def pairs(n): return [(f'{i+1}.',x['q']) for i,x in enumerate(get(n))]
def answers(n): return 'Answers (the same four questions as the printed Think harder page): '+' '.join(f'{i+1}) {x["a"]}' for i,x in enumerate(get(n)))
