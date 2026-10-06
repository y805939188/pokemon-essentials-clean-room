"""New read-only Git document bookkeeping; never executes inspected programs."""
import subprocess, json, hashlib, pathlib, sys
OUT = pathlib.Path(__file__).parent
ACT = 'd48197f365c39925f795c1d325988c0d74e59979'
PRE = '1e6b11a47370f1c7c4659a32443fc1afda597bac'
ORIG = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
def show(rev, path):
    return subprocess.check_output(['git', 'show', rev + ':' + path])
def record(event):
    with (OUT / 'delivery-log.jsonl').open('a') as f:
        f.write(json.dumps(event, ensure_ascii=False) + '\n')
def primary():
    reg = json.loads(show(ACT, 'review/remediation/20261003-prepare/batches/B14/integration-stage-1/finding-registration.json'))
    ids = [x['id'] for x in reg['dispositions']]
    original_path = 'review/global-independent-review/2026-10-03-fd82a639/findings.json'
    plan_path = 'review/remediation-20261003-prepare/finding-acceptance.json'
    original = json.loads(show(ORIG, original_path))
    accepted = json.loads(show(PLAN, plan_path))
    docs = [(ORIG, original_path, '/'+str(i), x) for i,x in enumerate(original) if x['id'] in ids]
    docs += [(PLAN, plan_path, '/'+k, accepted[k]) for k in ids]
    return docs
def pool(docs):
    values=[]; lookup={}; occurrences=[]; structures=[]
    def walk(v, context):
        if isinstance(v, dict):
            return {'object': [[k,walk(x,context+'/'+k.replace('~','~0').replace('/','~1'))] for k,x in v.items()]}
        if isinstance(v, list):
            return {'array': [walk(x,context+'/'+str(i)) for i,x in enumerate(v)]}
        key=json.dumps(v,ensure_ascii=False,separators=(',',':'))
        if key not in lookup:
            lookup[key]=len(values);values.append(v);occurrences.append([])
        i=lookup[key];occurrences[i].append(context);return {'value':i}
    for rev,path,pointer,v in docs:
        structures.append({'commit':rev,'path':path,'pointer':pointer,'structure':walk(v,rev+':'+path+'#'+pointer)})
    return values,occurrences,structures
def formal_pool():
    inventories=json.loads((OUT/'diff-inventories.json').read_text())['predecessor']
    paths=[f['header'][13:].split(' b/')[0] for f in inventories['files'] if f['header'][13:].startswith(('specs/','deliverables/final-specification-set/engine-overworld/','deliverables/final-specification-set/pokemon-rules/','deliverables/final-specification-set/test-catalog/engine-overworld-wp','deliverables/final-specification-set/test-catalog/pokemon-rules-wp'))]
    seedpaths=['deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md','deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md','deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md']
    seen={line:rev+':'+p+':'+str(i) for rev in [ACT] for p in seedpaths for i,line in enumerate(show(rev,p).decode().splitlines(),1)}
    values=[];occurrences=[];lookup={};mapping=[]
    for p in paths:
        diff=subprocess.check_output(['git','diff','--no-ext-diff','--no-textconv','--binary','--full-index','--no-color','--find-renames','--unified=3',PRE,ACT,'--',p]).decode().splitlines()
        entries=[]
        for i,line in enumerate(diff,1):
            if line[:1] in ['+','-',' '] and not line.startswith(('+++','---')):
                value=line[1:];context=p+':diff-line-'+str(i)+':'+line[:1]
                if value in seen: entries.append({'sign':line[:1],'exact_reuse':seen[value]})
                else:
                    if value not in lookup:lookup[value]=len(values);values.append(value);occurrences.append([])
                    n=lookup[value];occurrences[n].append(context);entries.append({'sign':line[:1],'new_value':n})
            else:entries.append({'header':line})
        mapping.append({'path':p,'ordered_diff_lines':entries})
    return values,occurrences,mapping
def primary_supplement():
    docs=primary();root='review/global-independent-review/2026-10-03-fd82a639/'
    wanted={x[3]['id'] for x in docs if x[0]==ORIG}
    wanted.update(['RUN-C-001','RUN-C-003','RUN-C-006','RUN-C-007','RUN-C-090'])
    for rev,path,pointer,obj in docs:
        if rev==ORIG:
            wanted.update(x['raw_id'] for x in obj.get('raw_reports',[]) if 'raw_id' in x)
    for p,key in [('root/adjudication-log.json','adjudications'),('root/extension-adjudications.json','adjudications'),('agents/A/X-A-C05-RECHECK/recheck.json','rechecks'),('agents/B/X-B-C06-RECHECK/findings-review.json','items')]:
        d=json.loads(show(ORIG,root+p))
        docs.append((ORIG,root+p,'/metadata',{k:v for k,v in d.items() if k!=key}))
        items=d[key]
        iterator=items.items() if isinstance(items,dict) else enumerate(items)
        for i,x in iterator:
            text=json.dumps(x,ensure_ascii=False)
            if any(w in text for w in wanted):docs.append((ORIG,root+p,'/'+key+'/'+str(i),x))
    p='review/remediation/20261003-prepare/batches/B02/integration-stage-1/finding-registration.json'
    docs.append((PRE,p,'',json.loads(show(PRE,p))))
    return docs
if __name__ == '__main__':
    mode=sys.argv[1]
    if mode=='primary':
        vals,occ,struct=pool(primary());start=int(sys.argv[2]);end=int(sys.argv[3])
        if start==0:
            mapping={'reconstruction':'Resolve each typed value at its exact first Git JSON pointer. Reuse retains every occurrence and ordered object/array structure. No scalar omissions.',
                     'structures':struct,'values':[{'index':i,'sha256':hashlib.sha256(json.dumps(v,ensure_ascii=False,separators=(',',':')).encode()).hexdigest(),'type':type(v).__name__,'occurrences':occ[i]} for i,v in enumerate(vals)]}
            (OUT/'primary-exact-value-map.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')
        print('VALUES',len(vals),'serialized bytes',sum(len(json.dumps(v,ensure_ascii=False)) for v in vals))
        for i in range(start,min(end,len(vals))):
            print(i,occ[i][0].split('#')[-1],json.dumps(vals[i],ensure_ascii=False))
        record({'kind':'primary_value_delivery','range_half_open':[start,min(end,len(vals))],'total':len(vals),'status':'delivered_requires_model_inspection','map':'primary-exact-value-map.json'})
    elif mode=='lines':
        rev,path=sys.argv[2:4];start,end=map(int,sys.argv[4:6]);data=show(rev,path);lines=data.decode().splitlines()
        print(rev,path,'total_lines',len(lines),'sha256',hashlib.sha256(data).hexdigest())
        for i in range(start-1,min(end,len(lines))):print(str(i+1)+': '+lines[i])
        record({'kind':'line_delivery','commit':rev,'path':path,'range_inclusive':[start,min(end,len(lines))],'total_lines':len(lines),'sha256':hashlib.sha256(data).hexdigest(),'status':'delivered_requires_model_inspection'})
    elif mode=='formal':
        vals,occ,struct=formal_pool();start,end=map(int,sys.argv[2:4])
        if start==0:
            (OUT/'formal-exact-reuse-map.json').write_text(json.dumps({'maps':struct,'values':[{'index':i,'sha256':hashlib.sha256(v.encode()).hexdigest(),'occurrences':occ[i]} for i,v in enumerate(vals)]},ensure_ascii=False,indent=2)+'\n')
        print('FORMAL new distinct lines',len(vals),'bytes',sum(len(v.encode()) for v in vals))
        for i in range(start,min(end,len(vals))):print(i,occ[i][0],vals[i])
        record({'kind':'formal_distinct_line_delivery','range_half_open':[start,min(end,len(vals))],'total':len(vals),'status':'delivered_requires_model_inspection','map':'formal-exact-reuse-map.json'})
    elif mode=='source':
        root,path=sys.argv[2:4];start,end=map(int,sys.argv[4:6]);rev='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
        data=subprocess.check_output(['git','-C',root,'show',rev+':'+path]);lines=data.decode().splitlines()
        print('REFERENCE',rev,path,'total_lines',len(lines),'sha256',hashlib.sha256(data).hexdigest())
        for i in range(start-1,min(end,len(lines))):print(str(i+1)+': '+lines[i])
        record({'kind':'source_line_delivery','repository':'reference/pokemon-essentials','commit':rev,'path':path,'range_inclusive':[start,min(end,len(lines))],'total_lines':len(lines),'sha256':hashlib.sha256(data).hexdigest(),'status':'delivered_requires_model_inspection','executed':False})
    elif mode=='supplement':
        vals,occ,struct=pool(primary_supplement());start,end=map(int,sys.argv[2:4])
        if start==1446:
            (OUT/'primary-supplement-v2-exact-map.json').write_text(json.dumps({'structures':struct,'values':[{'index':i,'type':type(v).__name__,'sha256':hashlib.sha256(json.dumps(v,ensure_ascii=False,separators=(',',':')).encode()).hexdigest(),'occurrences':occ[i]} for i,v in enumerate(vals)]},ensure_ascii=False,indent=2)+'\n')
        print('SUPPLEMENT total unique',len(vals),'new bytes',sum(len(json.dumps(v,ensure_ascii=False)) for v in vals[1446:]))
        for i in range(start,min(end,len(vals))):print(i,occ[i][0].split('#')[-1],json.dumps(vals[i],ensure_ascii=False))
        record({'kind':'primary_supplement_value_delivery','range_half_open':[start,min(end,len(vals))],'total':len(vals),'status':'delivered_requires_model_inspection'})
