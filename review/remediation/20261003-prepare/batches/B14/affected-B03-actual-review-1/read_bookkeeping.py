"""New read-only object/document bookkeeping. Never imports or runs reviewed programs."""
import subprocess, json, hashlib, pathlib, re, sys
OUT = pathlib.Path(__file__).parent
ACT = 'd48197f365c39925f795c1d325988c0d74e59979'
PRE = '1e6b11a47370f1c7c4659a32443fc1afda597bac'
ORIG = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
B14 = ['GIR-FD82-002','GIR-FD82-003','GIR-FD82-C003','GIR-FD82-C007'] + ['GIR-FD82-C%03d'%n for n in [86,87,88,89,91,92,93,94,95,97,98,99,100,101,102,103,104,105,106]] + ['WP80-INTAKE-R01']
B03 = ['GIR-FD82-002','GIR-FD82-C003','GIR-FD82-C007'] + ['GIR-FD82-C%03d'%n for n in list(range(35,55))+[67,94,95]] + ['WP80-INTAKE-R01']
def blob(c,p): return subprocess.check_output(['git','show',c+':'+p])
def save(p,o): (OUT/p).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def identity(c,p,b):
    return {'commit':c,'path':p,'blob':subprocess.check_output(['git','rev-parse',c+':'+p]).decode().strip(),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'lines':len(b.splitlines())}
def pack(name,objects):
    vals=[]; lookup={}; contexts=[]; structures=[]
    def walk(v,loc):
        if isinstance(v,dict):return {'object':[[k,walk(x,loc+'/'+k.replace('~','~0').replace('/','~1'))] for k,x in v.items()]}
        if isinstance(v,list):return {'array':[walk(x,loc+'/'+str(i)) for i,x in enumerate(v)]}
        key=json.dumps([type(v).__name__,v],ensure_ascii=False,separators=(',',':'))
        if key not in lookup:lookup[key]=len(vals);vals.append(v);contexts.append([])
        i=lookup[key];contexts[i].append(loc);return {'value':i,'type':type(v).__name__}
    for ident,v in objects:structures.append({'identity':ident,'structure':walk(v,ident['commit']+':'+ident['path'])})
    save(name+'-lossless-map.json',{'values':vals,'contexts':contexts,'documents':structures})
    def pure(v):
        if not isinstance(v,str):return True
        return bool(re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}|(?:GIR-FD82-|WP80-|RUN-|R-B14-|B14-)[A-Za-z0-9-]+',v)) or (not re.search(r'\s',v) and ('/' in v or re.fullmatch(r'[A-Za-z0-9_.:@#§|+-]+',v)))
    text=[]
    for i,v in enumerate(vals):
        if not pure(v):text.append(str(i)+' '+contexts[i][0]+'\n'+json.dumps(v,ensure_ascii=False))
    (OUT/(name+'-semantic.txt')).write_text('\n\n'.join(text)+'\n')
    print(name,'documents',len(objects),'unique values',len(vals),'semantic entries',len(text),'semantic chars',sum(map(len,text)))
if __name__=='__main__':
    if sys.argv[1]=='primary':
        objs=[];ids=set(B14+B03)
        for c,p in [(ORIG,'review/global-independent-review/2026-10-03-fd82a639/findings.json'),(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json')]:
            b=blob(c,p);o=json.loads(b)
            if isinstance(o,list):o={str(i):v for i,v in enumerate(o) if v.get('id') in ids}
            else:o={k:v for k,v in o.items() if k in ids}
            objs.append((identity(c,p,b),o))
        for p in ['root/adjudication-log.json','root/extension-adjudications.json']:
            p='review/global-independent-review/2026-10-03-fd82a639/'+p;b=blob(ORIG,p);o=json.loads(b)
            rows=[v for v in o['adjudications'] if any(i in json.dumps(v,ensure_ascii=False) for i in ids)]
            objs.append((identity(ORIG,p,b),{**{k:v for k,v in o.items() if k!='adjudications'},'adjudications':rows}))
        pack('primary-controls',objs)
    elif sys.argv[1]=='slice':
        name,start,end=sys.argv[2],int(sys.argv[3]),int(sys.argv[4]);lines=(OUT/(name+'-semantic.txt')).read_text().splitlines()
        print('TOTAL LINES',len(lines),'RANGE',start,end)
        for i in range(start-1,min(end,len(lines))):print(str(i+1)+': '+lines[i])
