"""Independent document-only Git reading/reuse bookkeeping."""
import subprocess,json,re,hashlib,pathlib,sys,csv,io,gzip
from read_documents import OUT,ACT,PRE,ORIG,PLAN,show,primary_supplement,formal_pool,pool,record
OLDREPORT='9d03b7a7a12f1cdaaa7eb999050d9d5812780f51'
ROOT='review/remediation/20261003-prepare/batches/B14/'
def corpus():
    seeds,seedocc,_=pool(primary_supplement())
    seed={json.dumps(v,ensure_ascii=False,separators=(',',':')):seedocc[i][0] for i,v in enumerate(seeds)}
    fv,fo,_=formal_pool()
    for i,v in enumerate(fv):
        seed[json.dumps(v,ensure_ascii=False)]=fo[i][0]
        for sign in ['+','-',' ']:seed[json.dumps(sign+v,ensure_ascii=False)]={'exact_signed_body_reuse':fo[i][0],'sign':sign}
    for p in ['deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md','deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md','deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md']:
        for i,v in enumerate(show(ACT,p).decode().splitlines(),1):
            seed[json.dumps(v,ensure_ascii=False)]=ACT+':'+p+':'+str(i)
            for sign in ['+','-',' ']:seed[json.dumps(sign+v,ensure_ascii=False)]={'exact_signed_body_reuse':ACT+':'+p+':'+str(i),'sign':sign}
    inv=json.loads((OUT/'diff-inventories.json').read_text())['predecessor']
    paths=[f['header'][13:].split(' b/')[0] for f in inv['files']]
    docs=[]
    for p in paths:
        if p.startswith(('specs/','deliverables/final-specification-set/engine-overworld/','deliverables/final-specification-set/pokemon-rules/')) or p in ['deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md','deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md']:continue
        docs.append((ACT,p))
    # Complete preceding report including all mapping/control/limitation files; never run its programs.
    for p in subprocess.check_output(['git','ls-tree','-r','--name-only',OLDREPORT,ROOT+'affected-B02-actual-review-1']).decode().splitlines():docs.append((OLDREPORT,p))
    values=[];lookup={};occ=[];structures=[];identities=[]
    def walk(v,c):
        if isinstance(v,dict):return {'o':[[k,walk(x,c+'/'+k.replace('~','~0').replace('/','~1'))] for k,x in v.items()]}
        if isinstance(v,list):return {'a':[walk(x,c+'/'+str(i)) for i,x in enumerate(v)]}
        s=json.dumps(v,ensure_ascii=False,separators=(',',':'))
        if s in seed:return {'r':seed[s]}
        if isinstance(v,str) and v.lstrip().startswith(('{','[')):
            try:
                decoded=json.loads(v)
                return {'encoded_json_string_sha256':hashlib.sha256(v.encode()).hexdigest(),'exact_string_pointer':c,'decoded_structure':walk(decoded,c+'/decoded-json')}
            except json.JSONDecodeError:pass
        if s not in lookup:lookup[s]=len(values);values.append(v);occ.append([])
        i=lookup[s];occ[i].append(c);return {'v':i}
    for rev,p in docs:
        data=show(rev,p);identities.append({'commit':rev,'path':p,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'lines':len(data.splitlines())})
        if p.endswith('.json'):
            obj=json.loads(data);s=walk(obj,rev+':'+p+'#')
        elif p.endswith('.jsonl'):
            obj=[json.loads(l) for l in data.decode().splitlines() if l];s=walk(obj,rev+':'+p+'#line-record')
        else:
            if rev==ACT and not p.startswith(ROOT):
                # Existing public files: retain every complete unfiltered hunk, not unrelated unchanged history.
                diff=subprocess.check_output(['git','diff','--no-ext-diff','--no-textconv','--no-renames','--binary','--full-index','--no-color',PRE,ACT,'--',p]).decode().splitlines()
                if p.endswith('.tsv'):
                    obj=[]
                    for i,l in enumerate(diff):
                        if l[:1] in ['+','-',' '] and '\t' in l and not l.startswith(('+++','---')):
                            columns=next(csv.reader([l[1:]],delimiter='\t'))
                            obj.append({'signed_tsv_raw_sha256':hashlib.sha256(l.encode()).hexdigest(),'exact_raw_diff_line':i,'sign':l[:1],'columns':columns})
                        else:obj.append(l)
                else:obj=diff
            else:obj=data.decode().splitlines()
            s=walk(obj,rev+':'+p+'#line')
        structures.append({'commit':rev,'path':p,'structure':s})
    return values,occ,structures,identities
def mechanical(v):
    if not isinstance(v,str):return True
    if re.fullmatch(r'[0-9a-f]{7,64}|[0-9]+(?:\.[0-9]+)?',v):return True
    if re.match(r'^[0-9a-f]{8,40}[:/]',v) and '\n' not in v:return True
    if v.startswith('/') and '\n' not in v:return True
    if re.match(r'^(?:review|specs|planning|audit|deliverables|reference|Data|PBS|Graphics|Audio|agents|root)/',v) and '\n' not in v:return True
    if re.fullmatch(r'[A-Z][A-Z0-9_-]*[0-9][A-Z0-9_-]*',v):return True
    if not re.search(r'\s',v) and v.count('/')>=2 and not v.startswith(('http:','https:')):return True
    if re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]*:[0-9]+',v):return True
    if re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]*:[0-9a-f]{7,64}',v):return True
    if re.fullmatch(r'(?:[A-Za-z0-9_.-]+/)+[A-Za-z0-9_.-]+',v):return True
    if re.match(r'^[AMD]\t(?:review|specs|deliverables|planning|audit)/',v):return True
    if v.startswith(('diff --git ','index ','--- a/','+++ b/','--- /dev/null','new file mode ')):return True
    if re.fullmatch(r'@@ -[0-9,]+ \+[0-9,]+ @@',v):return True
    if re.fullmatch(r'[0-9;,\-–— ]+',v):return True
    return False
if __name__=='__main__':
    vals,occ,struct,identities=corpus();sem=[i for i,v in enumerate(vals) if not mechanical(v)]
    print('CORPUS files',len(struct),'unique scalars',len(vals),'non-mechanical strings',len(sem),'string bytes',sum(len(vals[i].encode()) for i in sem))
    mode=sys.argv[1]
    if mode=='inventory':
        manifest={'reconstruction':'Ordered typed original object/array/line structures retained. Resolve unique values at exact first Git pointer; every occurrence retained. Mechanical identities are separate from semantic reading. Original Git objects retain exact values; raw private provenance is not copied.', 'identities':identities,'structures':struct,'values':[{'index':i,'type':type(v).__name__,'sha256':hashlib.sha256(json.dumps(v,ensure_ascii=False,separators=(',',':')).encode()).hexdigest(),'mechanical':mechanical(v),'occurrences':occ[i]} for i,v in enumerate(vals)],'semantic_indices':sem}
        (OUT/'audit-exact-reuse-map.json').write_text(json.dumps(manifest,ensure_ascii=False,separators=(',',':'))+'\n')
        for i in sem[:12]:print(i,occ[i][0],json.dumps(vals[i],ensure_ascii=False))
    elif mode=='freeze-map':
        manifest={'version':2,'reconstruction':'Exact fixed Git values and ordered native structures retained; encoded JSON strings and signed TSV columns have exact raw identities plus lossless decoded structures. Reuse is only exact typed value/body reuse. No semantic completion is implied by this map.', 'identities':identities,'structures':struct,'values':[{'index':i,'type':type(v).__name__,'sha256':hashlib.sha256(json.dumps(v,ensure_ascii=False,separators=(',',':')).encode()).hexdigest(),'mechanical':mechanical(v),'occurrences':occ[i]} for i,v in enumerate(vals)],'semantic_indices':sem}
        target=OUT/'audit-exact-reuse-map-v2.json.gz'
        with gzip.open(target,'wt',encoding='utf-8',compresslevel=6) as f:json.dump(manifest,f,ensure_ascii=False,separators=(',',':'))
        with (OUT/'audit-semantic-index.json').open('w') as f:json.dump({'version':2,'map':target.name,'semantic_indices':sem,'total':len(sem),'values_total':len(vals)},f)
        print('Frozen compressed exact map',target.name,'bytes',target.stat().st_size)
    elif mode=='read':
        start,end=map(int,sys.argv[2:4])
        for n in range(start,min(end,len(sem))):
            i=sem[n];print('S'+str(n),'V'+str(i),occ[i][0],json.dumps(vals[i],ensure_ascii=False))
        record({'kind':'audit_semantic_value_delivery','semantic_index_range_half_open':[start,min(end,len(sem))],'total':len(sem),'status':'delivered_requires_model_inspection','map':'audit-exact-reuse-map.json'})
    elif mode=='sample':
        for n in [100,200,400,800,1600,3000,6000,10000]:
            if n<len(sem):
                i=sem[n];print(n,i,occ[i][0],repr(vals[i]))
    elif mode=='gate':
        path=ROOT+'integration-stage-1/actual-request-B02.json'
        selected=[]
        for i in sem:
            contexts=[c for c in occ[i] if c.startswith(ACT+':'+path+'#')]
            if contexts:selected.append((i,contexts[0]))
        print('GATE complete novel semantic values',len(selected))
        for i,c in selected:print('V'+str(i),c.split('#')[-1],json.dumps(vals[i],ensure_ascii=False))
        record({'kind':'complete_gate_novel_semantic_delivery','path':path,'indices':[i for i,c in selected],'status':'delivered_requires_model_inspection'})
    elif mode=='group':
        pattern=sys.argv[2];start,end=map(int,sys.argv[3:5]);selected=[]
        for i in sem:
            contexts=[c for c in occ[i] if re.search(pattern,c)]
            if contexts:selected.append((i,contexts[0]))
        print('GROUP',pattern,'complete novel semantic values',len(selected))
        for n in range(start,min(end,len(selected))):
            i,c=selected[n];print('G'+str(n),'V'+str(i),c.split('#')[-1],json.dumps(vals[i],ensure_ascii=False))
        record({'kind':'audit_group_semantic_delivery','pattern':pattern,'group_range_half_open':[start,min(end,len(selected))],'total':len(selected),'value_hashes':[hashlib.sha256(json.dumps(vals[i],ensure_ascii=False,separators=(',',':')).encode()).hexdigest() for i,c in selected[start:end]],'status':'delivered_requires_model_inspection'})
    elif mode=='remaining':
        # Already-confirmed complete literal bodies and integration meanings can be reused exactly.
        completed={e['commit']+':'+e['path'] for e in [json.loads(l) for l in (OUT/'delivery-log.jsonl').read_text().splitlines()] if e.get('kind')=='line_delivery' and e.get('range_inclusive')==[1,e.get('total_lines')]}
        selected=[]
        for i in sem:
            if any('/B14/integration-stage-1/' in c or c.split('#')[0] in completed for c in occ[i]):continue
            selected.append(i)
        start,end=map(int,sys.argv[2:4]);print('REMAINING distinct semantic values',len(selected),'bytes',sum(len(vals[i].encode()) for i in selected))
        for n in range(start,min(end,len(selected))):
            i=selected[n];print('R'+str(n),'V'+str(i),occ[i][0].split('#')[-1],json.dumps(vals[i],ensure_ascii=False))
        record({'kind':'audit_remaining_semantic_delivery','range_half_open':[start,min(end,len(selected))],'total':len(selected),'value_hashes':[hashlib.sha256(json.dumps(vals[i],ensure_ascii=False,separators=(',',':')).encode()).hexdigest() for i in selected[start:end]],'status':'delivered_requires_model_inspection'})
