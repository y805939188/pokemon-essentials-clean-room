"""New read-only Git/document bookkeeping; never executes reference behavior."""
import sys, json, subprocess, hashlib, pathlib

OUT = pathlib.Path(__file__).parent
ACT = 'd48197f365c39925f795c1d325988c0d74e59979'
ORIGINAL = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
IDS = ['GIR-FD82-002', 'GIR-FD82-003', 'GIR-FD82-C003', 'GIR-FD82-C007'] + ['GIR-FD82-C%03d' % n for n in [86,87,88,89,91,92,93,94,95,97,98,99,100,101,102,103,104,105,106]] + ['WP80-INTAKE-R01']

def show(sha, path, reference=False):
    cmd = ['git']
    if reference:
        cmd += ['-C', sys.argv[7]]
    return subprocess.check_output(cmd + ['show', sha + ':' + path])

def delivery(kind, identity, interval, count):
    with (OUT / 'delivery-log.jsonl').open('a') as f:
        f.write(json.dumps({'kind':kind,'identity':identity,'offered_interval':interval,'characters':count,'semantic_completion':'must be assessed from actual returned output; no automatic reading assertion'})+'\n')

def primary():
    units=[]; seen={}; mappings=[]; keys={}
    for sha,path in [(ORIGINAL,'review/global-independent-review/2026-10-03-fd82a639/findings.json'),(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json')]:
        raw=show(sha,path); data=json.loads(raw)
        records=[(str(n),v) for n,v in enumerate(data) if v.get('id') in IDS] if isinstance(data,list) else [(k,v) for k,v in data.items() if k in IDS]
        for ptr,record in records:
            defs=[]
            def walk(v,p):
                encoded=json.dumps(v,ensure_ascii=False,separators=(',',':'))
                key=(type(v).__name__,encoded)
                if isinstance(v,(dict,list,str)) and (not isinstance(v,str) or len(v)>35):
                    if key in seen:
                        ident=seen[key]
                    else:
                        ident='V'+str(len(seen));seen[key]=ident
                        if isinstance(v,dict):shape={('K'+str(keys.setdefault(k,len(keys)))):walk(z,p+'/'+k.replace('~','~0').replace('/','~1')) for k,z in v.items()}
                        elif isinstance(v,list):shape=[walk(z,p+'/'+str(n)) for n,z in enumerate(v)]
                        else:shape=v
                        defs.append(ident+'='+json.dumps(shape,ensure_ascii=False,separators=(',',':')))
                    mappings.append({'sha':sha,'path':path,'pointer':p,'value_id':ident,'sha256':hashlib.sha256(encoded.encode()).hexdigest()})
                    return '@'+ident
                return v
            shape=walk(record,'/'+ptr)
            units.append('\nINPUT '+sha+':'+path+'#/'+ptr+'\n'+'\n'.join(defs)+'\nSTRUCTURE '+json.dumps(shape,ensure_ascii=False,separators=(',',':'))+'\n')
    (OUT/'primary-exact-value-map.json').write_text(json.dumps({'method':'exact scalar equality only; containers, key order, list order and all occurrences retained at fixed original Git pointers','mappings':mappings},ensure_ascii=False,indent=2)+'\n')
    return 'KEY_DICTIONARY '+json.dumps({'K'+str(v):k for k,v in keys.items()},ensure_ascii=False,separators=(',',':'))+'\n'+''.join(units)

if sys.argv[1]=='primary':
    text=primary(); start=int(sys.argv[2]);end=int(sys.argv[3]);print('TOTAL_CHARACTERS',len(text),'SLICE',start,end);print(text[start:end]);delivery('primary-exact-value-view','ORIGINAL+PLAN', [start,min(end,len(text))],len(text[start:end]))
elif sys.argv[1]=='lines':
    sha,path,start,end=sys.argv[2:6];start=int(start);end=int(end);ref=len(sys.argv)>6 and sys.argv[6]=='reference'
    raw=show(sha,path,ref);lines=raw.decode().splitlines();print('INPUT',sha+':'+path,'sha256',hashlib.sha256(raw).hexdigest(),'TOTAL_LINES',len(lines),'RANGE',start,min(end,len(lines)))
    text='\n'.join(str(n)+': '+line for n,line in enumerate(lines,1) if start<=n<=end);print(text);delivery('reference-lines' if ref else 'document-lines',sha+':'+path,[start,min(end,len(lines))],len(text))
