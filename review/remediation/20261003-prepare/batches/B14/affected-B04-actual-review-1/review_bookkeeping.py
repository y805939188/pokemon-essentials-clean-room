"""New static document bookkeeping only. Does not execute reviewed programs."""
import sys, json, hashlib, subprocess, pathlib, csv, io, gzip
ROOT = pathlib.Path(__file__).parent
ACT = 'd48197f365c39925f795c1d325988c0d74e59979'
ORIGINAL = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
PRE = '1e6b11a47370f1c7c4659a32443fc1afda597bac'
IDS = ['GIR-FD82-002','GIR-FD82-003','GIR-FD82-C003','GIR-FD82-C007'] + ['GIR-FD82-C%03d' % i for i in [86,87,88,89,91,92,93,94,95,97,98,99,100,101,102,103,104,105,106]] + ['WP80-INTAKE-R01']
def get(commit, path):
    return subprocess.check_output(['git','show',commit+':'+path])
def document(raw,path):
    if path.endswith('.json'): return json.loads(raw)
    if path.endswith('.jsonl'): return [json.loads(l) for l in raw.splitlines() if l]
    if path.endswith('.tsv'):
        def expand(x):
            if isinstance(x,dict): return {k:expand(v) for k,v in x.items()}
            if isinstance(x,list): return [expand(v) for v in x]
            if isinstance(x,str) and x.lstrip().startswith(('{','[')):
                try: decoded=json.loads(x)
                except (ValueError,TypeError): return x
                if isinstance(decoded,(dict,list)):
                    return {'$encoded_string_sha256':hashlib.sha256(x.encode()).hexdigest(),'$decoded':expand(decoded)}
            return x
        parsed=list(csv.reader(io.StringIO(raw.decode()),delimiter='\t'))
        return {'schema':parsed[0],'rows':[{k:expand(v) for k,v in zip(parsed[0],r)} for r in parsed[1:]]}
    return {'lines':raw.decode().splitlines(keepends=True)}
def write(name, value):
    (ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def artifact_bytes(name):
    p=ROOT/name
    if p.exists():return p.read_bytes()
    return gzip.decompress((ROOT/(name+'.gz')).read_bytes())
def event(value):
    with (ROOT/'reading-events.jsonl').open('a') as f:
        f.write(json.dumps(value,ensure_ascii=False)+'\n')
def at(value, selector):
    for key in selector: value=value[key]
    return value
def build(name, inputs):
    values=[]; seen={}; structures=[]; bindings=[]
    def walk(x,c,p,s):
        if isinstance(x,dict):
            return {'type':'object','members':[[k,walk(v,c,p,s+[k])] for k,v in x.items()]}
        if isinstance(x,list):
            return {'type':'array','items':[walk(v,c,p,s+[i]) for i,v in enumerate(x)]}
        typ=type(x).__name__; encoded=json.dumps([typ,x],ensure_ascii=False).encode(); digest=hashlib.sha256(encoded).hexdigest()
        if digest not in seen:
            seen[digest]=len(values);values.append({'type':typ,'sha256':digest,'occurrences':[]})
        n=seen[digest];values[n]['occurrences'].append({'commit':c,'path':p,'selector':s})
        return {'value':n}
    for c,p,selector in inputs:
        raw=get(c,p);x=document(raw,p);selected=at(x,selector)
        structures.append({'commit':c,'path':p,'selector':selector,'structure':walk(selected,c,p,selector)})
        bindings.append({'commit':c,'path':p,'blob':subprocess.check_output(['git','rev-parse',c+':'+p]).decode().strip(),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)})
    write(name+'-map.json',{'inputs':bindings,'structures':structures,'values':values,'reconstruction':'Exact typed scalar values replayed from fixed Git commit/path/selector; object member and array order retained. No copied private provenance.'})
    print(name,'inputs',len(inputs),'unique typed values',len(values))
def consume(name,start,end):
    m=json.loads(artifact_bytes(name+'-map.json'));cache={}
    prev=None
    for i in range(start,min(end,len(m['values']))):
        r=m['values'][i];o=r['occurrences'][0];k=(o['commit'],o['path'])
        if k not in cache: cache[k]=document(get(*k),o['path'])
        x=at(cache[k],o['selector']);digest=hashlib.sha256(json.dumps([type(x).__name__,x],ensure_ascii=False).encode()).hexdigest()
        assert digest==r['sha256']
        if k!=prev: print('CONTEXT',*k);prev=k
        print(i,json.dumps(o['selector'],ensure_ascii=False,separators=(',',':')),json.dumps(x,ensure_ascii=False))
    event({'mode':'typed-values-delivered','map':name+'-map.json','range':[start,min(end,len(m['values']))],'not_a_reading_certificate':True})
if __name__=='__main__':
    cmd=sys.argv[1]
    if cmd=='primary':
        p='review/global-independent-review/2026-10-03-fd82a639/findings.json';x=json.loads(get(ORIGINAL,p))
        inp=[(ORIGINAL,p,[i]) for i,r in enumerate(x) if r['id'] in IDS]
        a='review/remediation-20261003-prepare/finding-acceptance.json';inp += [(PLAN,a,[i]) for i in IDS]
        build('primary',inp)
    elif cmd=='audit':
        inventory=json.loads((ROOT/'stream-inventory.json').read_text())['predecessor']['inventory']
        build('audit',[(ACT,r['path'],[]) for r in inventory])
    elif cmd=='values': consume(sys.argv[2],int(sys.argv[3]),int(sys.argv[4]))
    elif cmd=='text':
        c,p,start,end=sys.argv[2],sys.argv[3],int(sys.argv[4]),int(sys.argv[5]);raw=get(c,p);ls=raw.decode().splitlines()
        print('INPUT',c,p,'TOTAL',len(ls),'RANGE',start,min(end,len(ls)))
        for i in range(start-1,min(end,len(ls))): print(str(i+1)+': '+ls[i])
        event({'mode':'text-delivered','commit':c,'path':p,'range':[start,min(end,len(ls))],'total_lines':len(ls),'sha256':hashlib.sha256(raw).hexdigest(),'not_a_reading_certificate':True})
