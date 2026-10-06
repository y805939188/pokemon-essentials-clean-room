"""New frozen document/hash/structure bookkeeping. Never reference behavior execution."""
import json,pathlib,sys,re,subprocess,hashlib,collections,functools
import complete_reader as c
P=pathlib.Path(__file__).parent
done=json.loads((P/'semantic-consumption.json').read_text())
phases=[k for k,v in done.items() if isinstance(v,dict) and v.get('semantic_values_actually_consumed')]
known=c.known_paths()
@functools.lru_cache(None)
def strict_identity(s,key=''):
    if re.fullmatch(r'[0-9a-f]{8,64}',s,re.I):return True
    if re.fullmatch(r'(?:V|S|T|N|L|J|D|K|v|value|literal|leaf|control|evidence|payload|original|acceptance|scalar|text|line|node):?\d+',s):return True
    if s in known or s.endswith('/') and any(p.startswith(s) for p in known):return True
    for p in known:
        if s.startswith(p) and re.fullmatch(r'[#/0-9A-Za-z_~:.,-]*',s[len(p):]):return True
    # JSON pointers and ASCII identifiers carry structure/identity, never prose.
    if s.startswith('/') and re.fullmatch(r'[/0-9A-Za-z_~:$.,@# -]+',s):return True
    if re.fullmatch(r'(?:ORIGINAL|ACCEPTANCE):/[/0-9A-Za-z_~:.,-]+',s):return True
    if re.fullmatch(r'[A-Z][A-Za-z0-9_.-]*[0-9][A-Za-z0-9_.-]*',s):return True
    if re.fullmatch(r'B14/[A-Z0-9_.-]+',s):return True
    if re.fullmatch(r'\d{4}-\d{2}-\d{2}T[0-9:.+Z-]+',s):return True
    if s in ['str','string','bool','int','dict','list','object','array','null','float']:return True
    if key=='header' and re.fullmatch(r'@@ -\d+(?:,\d+)? \+\d+(?:,\d+)? @@',s):return True
    if key=='path_header' and s.startswith('a/') and ' b/' in s and s[2:].split(' b/',1)[0] in known and s.split(' b/',1)[1] in known:return True
    if re.fullmatch(r'[AMD]\t[^\n]+',s) and s[2:] in known:return True
    return False
def parsed(raw,path):
    duplicate=[]
    def hook(pairs):
        ks=[x[0] for x in pairs]
        if len(ks)!=len(set(ks)):duplicate.append(ks)
        return dict(pairs)
    if path.endswith('.tsv'):
        import csv,io
        for row in csv.reader(io.StringIO(raw.decode()),delimiter='\t'):
            for cell in row:
                if cell.startswith(('{','[')):
                    try:json.loads(cell,object_pairs_hook=hook)
                    except json.JSONDecodeError:pass
        v=c.document_tsv(raw)
    elif path.endswith('.jsonl'):v=[json.loads(x,object_pairs_hook=hook) for x in raw.splitlines() if x.strip()]
    else:v=json.loads(raw,object_pairs_hook=hook)
    assert not duplicate,('duplicate document keys',path)
    return v
summary=[];supp_inputs=[];supp_pool=[];supp_seen={};supp_occ=[];semantic_hashes={};reuse_records=[]
ids={x['id'] for x in json.loads((P/'contribution-dispositions.json').read_text())['dispositions']}
def primary_tokens(v,sha,path,ordinal=()):
    if isinstance(v,dict):
        for n,x in enumerate(v.values()):primary_tokens(x,sha,path,ordinal+(n,))
    elif isinstance(v,list):
        for n,x in enumerate(v):primary_tokens(x,sha,path,ordinal+(n,))
    elif isinstance(v,str):semantic_hashes.setdefault(('str',c.digest(v)),{'phase':'primary-48-complete-controls','commit':sha,'path':path,'ordinal':list(ordinal)})
op='review/global-independent-review/2026-10-03-fd82a639/findings.json';ap='review/remediation-20261003-prepare/finding-acceptance.json'
for n,x in enumerate(json.loads(c.show(c.ORIG,op))):
    if x['id'] in ids:primary_tokens(x,c.ORIG,op,(n,))
a=json.loads(c.show(c.PLAN,ap))
for n,(k,x) in enumerate(a.items()):
    if k in ids:primary_tokens(x,c.PLAN,ap,(n,))
for n,d in enumerate([json.loads(l) for l in (P/'delivery-log.jsonl').read_text().splitlines()]):
    if d['kind'] not in ['document-lines','reference-lines']:continue
    sha,path=d['identity'].split(':',1);ls=c.show(sha,path,sha==c.REF).decode().splitlines();lo,hi=d['offered_interval']
    for line in range(lo,min(hi,len(ls))+1):semantic_hashes.setdefault(('str',c.digest(ls[line-1])),{'phase':'literal-delivery-with-completed-truncation-supplements','delivery_index':n,'commit':sha,'path':path,'line':line})
for ph in phases:
    m=json.loads((P/(ph+'-complete-context-map.json')).read_text())
    exemptfile=P/(ph+'-display-mechanical-exemptions.json')
    exemptions={x['semantic_id'] for x in json.loads(exemptfile.read_text())['exemptions']} if exemptfile.exists() else set()
    reusefile=P/(ph+'-display-exact-reuse.json')
    display_reuse={x['semantic_id'] for x in json.loads(reusefile.read_text())['reuses']} if reusefile.exists() else set()
    # Gather all genuinely consumed native semantic tokens (including later supplements).
    for z in m['semantic_pool']:
        if z['id'] not in exemptions|display_reuse:
            semantic_hashes.setdefault((z['type'],z['sha256']),{'phase':ph,'semantic_id':z['id'],'context':z['first_context']})
    del m
def supplement(v,inp,ordinal,pointer,key,reason,iskey=False):
    h=c.digest(v);tok=(type(v).__name__,h)
    if tok in semantic_hashes:return
    if tok not in supp_seen:
        supp_seen[tok]=len(supp_pool)
        supp_pool.append({'id':len(supp_pool),'type':type(v).__name__,'sha256':h,'first_context':{'input':inp,'pointer':c.safe_pointer(pointer),'key':c.safe_pointer(key),'ordinal':list(ordinal),'record_context':{'classification_reason':reason}},'dictionary_key':iskey})
    supp_occ.append({'input':inp,'ordinal':list(ordinal),'dictionary_key':iskey,'sha256':h,'semantic_id':supp_seen[tok],'reason':reason})
for ph in phases:
    print('VERIFY',ph,flush=True)
    m=json.loads((P/(ph+'-complete-context-map.json')).read_text());occ=m['occurrences'];struct=m['structures'];oi=0;si=0;reuses=0;mechs=0;whole=0;empty_ranges=[]
    pool={z['id']:z for z in m['semantic_pool']}
    for ii,inp in enumerate(m['inputs']):
        if inp.get('role')=='FORMAL_UNFILTERED_HUNK':
            raw=subprocess.check_output(['git','diff','--no-ext-diff','--no-textconv','--no-renames','--binary','--full-index','--no-color',c.BASE,c.ACT,'--',inp['path']]);assert hashlib.sha256(raw).hexdigest()==inp['raw_diff_sha256'];assert len(raw)==inp['bytes']
        else:
            raw=c.show(inp['sha'],inp['path'],inp['sha']==c.REF);assert hashlib.sha256(raw).hexdigest()==inp['sha256'];assert len(raw)==inp['bytes']
        spi=len(supp_inputs);supp_inputs.append(inp)
        def leaf(v,ordinal,pointer,key):
            global oi,reuses,mechs
            z=occ[oi];oi+=1
            assert z['input']==ii and z['ordinal']==list(ordinal) and z['type']==type(v).__name__ and z['sha256']==c.digest(v),(ph,ii,ordinal)
            if z['mode']=='SEMANTIC_POOL':assert pool[z['semantic_id']]['sha256']==z['sha256']
            if z['mode']=='EXACT_OWN_CONSUMED_VALUE_REUSE':
                reuses+=1
                target=semantic_hashes.get((z['type'],z['sha256']))
                if target:reuse_records.append({'phase':ph,'input':ii,'ordinal':list(ordinal),'type':z['type'],'sha256':z['sha256'],'target':target})
                elif isinstance(v,str):supplement(v,spi,ordinal,pointer,key,'Reuse token requires independently consumed literal/control seed supplement')
            if z['mode']=='MECHANICAL_IDENTITY':
                mechs+=1
                if isinstance(v,str) and not strict_identity(v,key):supplement(v,spi,ordinal,pointer,key,'Conservative mechanical-classification supplement including mixed prose')
                elif not isinstance(v,str) and key.lower() in ['value','scalar','literal','count','total'] and not any(t in pointer.split('/') for t in ['ranges','lines','ordinal','interval','structures','shape','occurrences','mapping','references']):supplement(v,spi,ordinal,pointer,key,'Generated scalar can carry substantive value; consume independently')
            return c.digest(v)
        def walk(v,ordinal=(),pointer=''):
            global si
            if isinstance(v,dict):
                children=[]
                for n,(k,x) in enumerate(v.items()):
                    if not re.fullmatch(r'[A-Za-z_][0-9A-Za-z_.:$@#/-]{0,150}',k) and not strict_identity(k):supplement(k,spi,ordinal+(n,),pointer,k,'Substantive dictionary-key meaning',True)
                    children.append([{'key_sha256':c.digest(k),'key':c.safe_pointer(k) if c.safe_pointer(k)==k else None},walk(x,ordinal+(n,),pointer+'/'+k.replace('~','~0').replace('/','~1'))])
                expected={'input':ii,'ordinal':list(ordinal),'type':'dict','ordered_children':children,'sha256':c.digest(v)}
            elif isinstance(v,list):expected={'input':ii,'ordinal':list(ordinal),'type':'list','ordered_children':[walk(x,ordinal+(n,),pointer+'/'+str(n)) for n,x in enumerate(v)],'sha256':c.digest(v)}
            else:return leaf(v,ordinal,pointer,pointer.rsplit('/',1)[-1])
            assert struct[si]==expected,(ph,ii,ordinal,'structure');si+=1;return c.digest(v)
        if inp.get('role')=='FORMAL_UNFILTERED_HUNK':
            for n,l in enumerate(raw.decode().splitlines(),1):
                if l.startswith(('diff --git','index ','--- ','+++ ','@@','new file mode','old mode','new mode')):continue
                if l[:1] in ['+','-',' ']:leaf(l[1:],(n,),'/diff-line/'+str(n),l[:1])
        elif inp['path'].endswith(('.json','.jsonl')) or inp.get('format')=='ORDERED_TSV_DOCUMENT_CELLS_WITH_EXACT_EMBEDDED_JSON_STRING_IDENTITIES':
            v=parsed(raw,inp['path']);sels=inp.get('selectors')
            if sels:
                for sel in sels:
                    x=v;ordinal=[]
                    for k in sel.lstrip('/').split('/'):
                        k=k.replace('~1','/').replace('~0','~');n=int(k) if isinstance(x,list) else list(x).index(k);ordinal.append(n);x=x[n] if isinstance(x,list) else x[k]
                    walk(x,tuple(ordinal),sel)
            else:walk(v);whole+=1
        else:
            ls=raw.decode().splitlines();ranges=inp.get('line_ranges')
            if ranges:
                empty_ranges.extend({'input':ii,'range':z,'actual_lines':len(ls)} for z in ranges if z[0]>len(ls))
            else:whole+=1
            for n,l in enumerate(ls,1):
                if not ranges or any(lo<=n<=hi for lo,hi in ranges):leaf(l,(n,),'/line/'+str(n),'literal_line')
    assert oi==len(occ) and si==len(struct),(ph,oi,len(occ),si,len(struct))
    summary.append({'phase':ph,'inputs':len(m['inputs']),'verified_occurrences':oi,'verified_ordered_structures':si,'mechanical_occurrences':mechs,'exact_reuses':reuses,'whole_inputs':whole,'empty_selected_ranges':empty_ranges,'raw_and_structure_verified':True,'semantic_credit':'Separate explicit consumption; verification alone gives none'})
    del m
(P/'reading-reconstruction-verification.json').write_text(json.dumps({'reviewed_ACT':c.ACT,'results':summary,'duplicate_document_JSON_keys':0,'claim':'Mechanical identity, selected occurrence/order/type and complete container relationships verified; no behavior execution.'},ensure_ascii=False,indent=2)+'\n')
(P/'classification-supplement-complete-context-map.json').write_text(json.dumps({'phase':'classification-supplement','inputs':supp_inputs,'semantic_pool':supp_pool,'occurrences':supp_occ,'structures':[],'reconstruction':'Every conservative supplement exact native input/ordinal/type/hash; dictionary keys explicitly identified. All original contexts retained in governing phase maps.'},ensure_ascii=False,separators=(',',':'))+'\n')
(P/'exact-consumed-reuse-targets.json').write_text(json.dumps({'reviewed_ACT':c.ACT,'reuses':reuse_records,'basis':'Exact typed hash target in actually consumed primary/source/formal/audit values; initial frozen phase/delivery seed lists preserve creation context. No writer proof transfer or future temporal certificate.'},separators=(',',':'))+'\n')
print('COMPLETE',len(summary),'SUPPLEMENT_VALUES',len(supp_pool),'SUPPLEMENT_CONTEXTS',len(supp_occ),'REUSE_TARGETS',len(reuse_records),flush=True)
