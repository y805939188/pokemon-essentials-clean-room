"""New static document/JSON/diff reading bookkeeping, never a behavior verifier."""
import sys, json, subprocess, pathlib, hashlib, re, functools, csv, io

OUT = pathlib.Path(__file__).parent
ACT = 'd48197f365c39925f795c1d325988c0d74e59979'
BASE = '1e6b11a47370f1c7c4659a32443fc1afda597bac'
C3 = 'c06db6cd964188b3c693a9b7820e3a8aaffe0b04'
ORIG = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
G = 'review/remediation/20261003-prepare/batches/B14/integration-stage-1/'

@functools.lru_cache(None)
def show(sha, path, reference=False):
    cmd = ['git']
    if reference:
        cmd += ['-C', sys.argv[-1]]
    return subprocess.check_output(cmd + ['show', sha + ':' + path])

@functools.lru_cache(None)
def parsed_json(sha,path):
    if path.endswith('.tsv'): return document_tsv(show(sha,path))
    return [json.loads(l) for l in show(sha,path).splitlines() if l.strip()] if path.endswith('.jsonl') else json.loads(show(sha,path))

def document_tsv(raw):
    rows=list(csv.reader(io.StringIO(raw.decode()),delimiter='\t'))
    header=rows[0];records=[]
    for row in rows[1:]:
        assert len(row)==len(header)
        record={}
        for key,value in zip(header,row):
            if value.startswith(('{','[')):
                try: decoded=json.loads(value)
                except json.JSONDecodeError: decoded=None
                if decoded is not None:
                    record[key]={'original_document_JSON_string_sha256':digest(value),'decoded_document_JSON':decoded};continue
            record[key]=value
        records.append(record)
    return {'ordered_column_names':header,'ordered_records':records}

def digest(v):
    return hashlib.sha256(json.dumps(v, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()

def safe_pointer(pointer):
    # Exact original pointers remain recoverable from ordinal traversal and fixed inputs.
    if any(x in pointer for x in ['/'+'Users'+'/', '/'+'private'+'/', '@']) or re.search(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}',pointer,re.I):
        return 'private-selector-sha256:' + hashlib.sha256(pointer.encode()).hexdigest()
    return pointer

def display_private_identity(text):
    # Replace identity-only private provenance substrings; retain all surrounding meaning.
    pattern = '/' + 'Users' + r'/[^\s\"\']+|/' + 'private' + r'/(?:tmp|var)/[^\s\"\']+|/' + 'tmp' + r'/[^\s\"\']+'
    text = re.sub(pattern, lambda m: '<PRIVATE_PATH_SHA256_' + hashlib.sha256(m[0].encode()).hexdigest()[:16] + '>', text)
    text = re.sub(r'\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b', lambda m: '<PRIVATE_UUID_SHA256_' + hashlib.sha256(m[0].encode()).hexdigest()[:16] + '>', text, flags=re.I)
    return text

def seeds(exclude_phase=None):
    result = set()
    # These complete main control objects were actually consumed in turn 1.
    ids = {v['id'] for v in json.loads((OUT/'contribution-dispositions.json').read_text())['dispositions']}
    def all_values(v):
        if isinstance(v, dict):
            for z in v.values(): all_values(z)
        elif isinstance(v, list):
            for z in v: all_values(z)
        elif isinstance(v, str): result.add(('str', v))
    a = json.loads(show(ORIG, 'review/global-independent-review/2026-10-03-fd82a639/findings.json'))
    b = json.loads(show(PLAN, 'review/remediation-20261003-prepare/finding-acceptance.json'))
    for v in a:
        if v['id'] in ids: all_values(v)
    for k in ids: all_values(b[k])
    # Literal delivered source/document lines. Known truncations were supplemented;
    # incomplete compact/diff displays are not seeded. Only helper line deliveries apply.
    snapshot=OUT/((exclude_phase or 'generic')+'-seed-deliveries.json')
    if not snapshot.exists(): snapshot.write_text(json.dumps([json.loads(l) for l in (OUT/'delivery-log.jsonl').read_text().splitlines()],separators=(',',':'))+'\n')
    for d in json.loads(snapshot.read_text()):
        if d['kind'] not in ['document-lines', 'reference-lines']: continue
        sha, path = d['identity'].split(':', 1)
        ls = show(sha, path, d['kind']=='reference-lines').decode().splitlines()
        lo, hi = d['offered_interval']
        for n in range(lo, hi+1): result.add(('str', ls[n-1]))
    done=OUT/'semantic-consumption.json'
    if done.exists():
        frozen=OUT/((exclude_phase or 'generic')+'-seed-phases.json')
        if not frozen.exists():frozen.write_text(json.dumps([ph for ph,record in json.loads(done.read_text()).items() if isinstance(record,dict) and (record.get('semantic_values_actually_consumed') or record.get('consumed_ranges'))])+'\n')
        for ph,record in json.loads(done.read_text()).items():
            if ph not in json.loads(frozen.read_text()):continue
            if ph==exclude_phase or not isinstance(record,dict) or not (record.get('semantic_values_actually_consumed') or record.get('consumed_ranges')): continue
            mapping=json.loads((OUT/(ph+'-complete-context-map.json')).read_text())
            for item in mapping['semantic_pool']:
                if record.get('consumed_ranges') and not any(lo<=item['id']<hi for lo,hi in record['consumed_ranges']):continue
                c=item['first_context'];inp=mapping['inputs'][c['input']]
                if inp.get('role')=='FORMAL_UNFILTERED_HUNK':
                    data=subprocess.check_output(['git','diff','--no-ext-diff','--no-textconv','--no-renames','--binary','--full-index','--no-color',BASE,ACT,'--',inp['path']]).decode().splitlines()
                    value=data[c['ordinal'][0]-1][1:]
                elif c['key']=='literal_line': value=show(inp['sha'],inp['path'],inp['sha']==REF).decode().splitlines()[c['ordinal'][0]-1]
                else:
                    value=parsed_json(inp['sha'],inp['path'])
                    for n in c['ordinal']: value=list(value.values())[n] if isinstance(value,dict) else value[n]
                if isinstance(value,str): result.add(('str',value))
    return result


@functools.lru_cache(None)
def known_paths():
    paths=set()
    for sha in [ACT, BASE, C3, ORIG, PLAN]:
        paths.update(subprocess.check_output(['git','ls-tree','-r','--name-only',sha],text=True).splitlines())
    paths.update(subprocess.check_output(['git','-C',sys.argv[-1],'ls-tree','-r','--name-only',REF],text=True).splitlines())
    return paths

def pure_identity(s, key):
    # Only complete identity/selector grammar; mixed prose is retained.
    if re.fullmatch(r'(?:[A-Za-z_-]+:)?(?:V|S|T|N|L|J|D|K)?[0-9]+',s) and key.lower() in ['unique_value_id','value_ref','value_id','node_id','literal_id','string_id','reference','ref','id']: return True
    if re.fullmatch(r'(?:[0-9a-f]{40}:)?(?:review|deliverables|specs|audit|planning|Data|PBS|Graphics|Audio)/[^\n]+',s) and not re.search(r'\s(?:is|was|supports|means|because|not|preserved|requires|and|then|the|retained|verified|should|with)\b',s,re.I):
        if any(s==p or s.startswith(p) and re.fullmatch(r'[#/0-9A-Za-z_~:.,-]*',s[len(p):]) for p in known_paths()): return True
    if (key.lower() in ['location','at','first','occurrence','source_locator'] or '/pointers/' in key) and (s.startswith('/') or re.match(r'[0-9a-f]{40}:',s)) and not re.search(r'\s',s): return True

    # A mixed selector/path plus prose is never dropped.
    if re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', s, re.I): return True
    if key.lower() in ['pointer','selector','first_selector','original_selector','acceptance_selector','json_pointer','occurrence_pointer','node_id','value_id','literal_id','string_id','source_pointer','object_pointer'] and not re.search(r'\s', s): return True
    if key.lower() in ['path','file','source_path','report_path','repository_path','logical_path','directory','full_report_directory']:
        if s.split('#',1)[0] in known_paths(): return True
        if s.endswith('/') and any(p.startswith(s) for p in known_paths()): return True
    if re.fullmatch(r'(?:V|S|T|N|L|J|D|K)\d+|[\$@#](?:V|S|T|N|L|J|D|K)?\d+', s) and key.lower() in ['ref','reference','value','id','value_id','node','literal','text','string']: return True
    return False

def make(phase):
    seen = seeds(phase); pool=[]; lookup={}; occurrences=[]; structures=[]; inputs=[]; pure=0; reused=0
    def add(v, inp, ptr, key, context, ordinal):
        nonlocal pure, reused
        typ=type(v).__name__; token=(typ, v if not isinstance(v,(dict,list)) else digest(v))
        if not isinstance(v,str):
            normalized=re.sub(r'/[0-9]+(?=/|$)','/[]',ptr)
            token=token+(normalized,)
        mechanical_number = isinstance(v,(int,float)) and not isinstance(v,bool) and (key.lower() in ['bytes','utf8_bytes','characters','value_index','value_id','unique_value_id','node_id','literal_id','index','n','v','$value','line','c2_line','c3_line','base_line','start_line','end_line','line_count'] or any(w in ptr.split('/') for w in ['lines','pointers','ordinal','occurrences','ranges','source_lines','diff_lines','line_numbers','range','interval']))
        audit_document=inputs[inp]['path'].rsplit('/',1)[-1] if inp<len(inputs) else ''
        audit_mode=phase=='audit' or phase.startswith('preceding-')
        generated_map=audit_mode and any(t in audit_document for t in ['value-map','mapping','dedup','payload-map','read-map','deduplication','evidence-identities'])
        generated_map_primitive=generated_map and not isinstance(v,str) and (key.lower() in ['id','value','scalar','literal','count','n','v','unit','end','start','length','total','index','value_index','value_id'] or any(t in ptr.split('/') for t in ['shape','structure','structures','roots','ordered_trees','leaves','values','scalars','occurrences','mapping','leaf_mapping','ranges','lines','locators','entries']))
        audit_selector = audit_mode and isinstance(v,str) and not re.search(r'\s',v) and (any(w in ptr.split('/') for w in ['mapping','pointers','selectors','occurrence_locations','leaf_mapping','occurrences','locations']) and '/' in v or key.lower() in ['value_ref','mapped_value_id','$value'] and re.fullmatch(r'[\w:-]+',v) or re.fullmatch(r'[0-9a-f]{8,64}',v,re.I) and (key.lower() in ['sha','commit','hash','blob','ref','reference','$value','value_id'] or key.lower().endswith(('_sha','_hash','_sha256','_commit'))))
        audit_catalog_identity = audit_mode and isinstance(v,str) and key.lower() in ['id','finding_id','test_id','canonical_id','contribution_id','raw_id','record_key','first_selector','first_locator'] and (re.fullmatch(r'[A-Z][A-Za-z0-9_.-]*[0-9][A-Za-z0-9_.-]*',v) is not None or v.startswith('B14/') and not re.search(r'\s',v))
        audit_time_identity = audit_mode and isinstance(v,str) and key.lower() in ['recorded_utc','time','timestamp','recorded_at','utc'] and re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9:.+-]+(?:Z)?',v) is not None
        audit_hunk_identity = audit_mode and isinstance(v,str) and (key=='header' and re.fullmatch(r'@@ -[0-9]+(?:,[0-9]+)? \+[0-9]+(?:,[0-9]+)? @@',v) is not None or key=='path_header' and v.startswith('a/') and ' b/' in v and v[2:].split(' b/',1)[0] in known_paths() and v.split(' b/',1)[1] in known_paths())
        audit_path_identity = audit_mode and isinstance(v,str) and ((re.fullmatch(r'[AMD]\t[^\n]+',v) is not None and v[2:] in known_paths()) or re.fullmatch(r'(?:ORIGINAL|ACCEPTANCE):/[^\s]+',v) is not None)
        audit_mechanical = audit_catalog_identity or audit_time_identity or audit_hunk_identity or audit_path_identity or generated_map_primitive or audit_selector or audit_mode and (isinstance(v,str) and (re.fullmatch(r'(?:[0-9a-f]{40}:)?(?:findings\.json|finding-acceptance\.json|review/|deliverables/|specs/)[^\s]+',v) or re.fullmatch(r'(?:control|evidence|payload|original|acceptance|scalar|text|line|node|value):[0-9]+',v) or key.lower() in ['type','kind','tag'] and v in ['str','string','bool','int','dict','list','object','array','null','float'] or re.fullmatch(r'(?:V|S|T|N|L|J|D|K|v|value|literal|leaf)[0-9]+',v)) or isinstance(v,(int,float)) and not isinstance(v,bool) and (key.lower() in ['id','unit','patch_line','planned_index','total_lines','diff_bytes','diff_line','c3_diff_line','base_diff_line'] or any(w in ptr.split('/') for w in ['occurrence_locations','leaf_mapping','mapping','range','ranges','structure','structures','roots','shape','references','unique_values','row_evidence','line_mapping','selected_match_lines','displayed_ranges','remaining_unread_ranges','value_identities','unique_value_identities','pointer_value_index','remaining_unique_value_indices','already_read_value_indices','value_indices','range_zero_based_half_open'])))
        if audit_mechanical or mechanical_number or isinstance(v,str) and (pure_identity(v,key) or (any(w in ptr.split('/') for w in ['pointers','selectors','locations','first_occurrences']) and not re.search(r'\s',v))):
            pure += 1; mode='MECHANICAL_IDENTITY'; sid=None
        elif token in seen:
            reused += 1; mode='EXACT_OWN_CONSUMED_VALUE_REUSE'; sid=None
        else:
            if token not in lookup:
                lookup[token]=len(pool);pool.append({'type':typ,'value':v,'first_context':{'input':inp,'pointer':safe_pointer(ptr),'key':safe_pointer(key),'record_context':{k:display_private_identity(str(z)) if isinstance(z,str) else z for k,z in context.items()},'ordinal':ordinal}})
            sid=lookup[token];mode='SEMANTIC_POOL'
        occurrences.append({'input':inp,'pointer':safe_pointer(ptr),'ordinal':ordinal,'type':typ,'key':safe_pointer(key),'mode':mode,'semantic_id':sid,'sha256':digest(v),'context':{k:{'type':type(z).__name__,'sha256':digest(z)} for k,z in context.items()}})
        return digest(v)
    def traverse(v, inp, ptr='', context=None, ordinal=()):
        context=context or {}
        if isinstance(v,dict):
            context={**context, **{k:z for k,z in v.items() if k in ['id','finding_id','raw_id','owner','role','record_key','contribution_id','batch','classification','scope'] and isinstance(z,(str,int,bool)) and len(str(z))<100}}
            children=[]
            for n,(k,z) in enumerate(v.items()): children.append([{'key_sha256':digest(k),'key':safe_pointer(k) if safe_pointer(k)==k else None},traverse(z,inp,ptr+'/'+k.replace('~','~0').replace('/','~1'),context,ordinal+(n,))])
            structures.append({'input':inp,'ordinal':ordinal,'type':'dict','ordered_children':children,'sha256':digest(v)})
        elif isinstance(v,list):
            children=[traverse(z,inp,ptr+'/'+str(n),context,ordinal+(n,)) for n,z in enumerate(v)]
            structures.append({'input':inp,'ordinal':ordinal,'type':'list','ordered_children':children,'sha256':digest(v)})
        else:
            return add(v,inp,ptr,ptr.rsplit('/',1)[-1],context,ordinal)
        return digest(v)
    if phase=='formal':
        paths=json.loads((OUT/'formal-diff-reading-map.json').read_text())['paths']
        selections=[(ACT,p,None) for p in paths]
        # Read all original removed/context lines for the same12 exact paths.
        for p in paths:
            raw=subprocess.check_output(['git','diff','--no-ext-diff','--no-textconv','--no-renames','--binary','--full-index','--no-color',BASE,ACT,'--',p])
            inp=len(inputs);inputs.append({'sha':ACT,'path':p,'role':'FORMAL_UNFILTERED_HUNK','raw_diff_sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)})
            for n,l in enumerate(raw.decode().splitlines(),1):
                if l.startswith(('diff --git','index ','--- ','+++ ','@@','new file mode','old mode','new mode')): continue
                if l[:1] in ['+','-',' ']: add(l[1:],inp,'/diff-line/'+str(n),l[:1],{'diff_prefix':l[:1]},(n,))
    elif phase=='audit':
        selections=[(ACT,p['path'],None) for p in json.loads((OUT/'diff-inventories.json').read_text())[0]['paths'] if p['path'].startswith('review/remediation/20261003-prepare/batches/B14/')]
    else:
        selections=json.loads((OUT/(phase+'-selection.json')).read_text())
        selections=[(v['sha'],v['path'],v.get('selectors'),v.get('line_ranges')) for v in selections]
    for selection in selections:
        sha,path,selectors=selection[:3]; line_ranges=selection[3] if len(selection)>3 else None
        raw=show(sha,path,sha==REF);inp=len(inputs);inputs.append({'sha':sha,'path':path,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'selectors':selectors,'line_ranges':line_ranges,'role':phase})
        if phase=='public' and path.endswith('.tsv'):
            traverse(document_tsv(raw),inp)
            inputs[inp]['format']='ORDERED_TSV_DOCUMENT_CELLS_WITH_EXACT_EMBEDDED_JSON_STRING_IDENTITIES'
        elif path.endswith('.jsonl') and (phase=='audit' or phase.startswith('preceding-')):
            # Document JSONL only; ordered records, original raw hash and line order preserved.
            traverse(parsed_json(sha,path),inp)
            inputs[inp]['format']='NDJSON_ORDERED_DOCUMENT_RECORDS'
        elif path.endswith('.json'):
            duplicate=[]
            def hook(pairs):
                keys=[p[0] for p in pairs]
                if len(set(keys))!=len(keys): duplicate.append(keys)
                return dict(pairs)
            v=json.loads(raw,object_pairs_hook=hook)
            if duplicate: raise ValueError('Duplicate JSON keys require literal supplement: '+path)
            if selectors:
                for selector in selectors:
                    z=v;ordinals=[]
                    for k in selector.lstrip('/').split('/'):
                        k=k.replace('~1','/').replace('~0','~'); n=int(k) if isinstance(z,list) else list(z).index(k);ordinals.append(n);z=z[n] if isinstance(z,list) else z[k]
                    traverse(z,inp,selector,ordinal=tuple(ordinals))
            else: traverse(v,inp)
        else:
            for n,l in enumerate(raw.decode().splitlines(),1):
                if not line_ranges or any(lo<=n<=hi for lo,hi in line_ranges):add(l,inp,'/line/'+str(n),'literal_line',{},(n,))
    # Store exact-source contexts, ordered typed structure and hash-addressed leaves,
    # never duplicate private provenance, source fragments or old prompts in artifacts.
    pub={'phase':phase,'inputs':inputs,'semantic_pool':[{'id':n,'type':v['type'],'sha256':digest(v['value']),'first_context':v['first_context']} for n,v in enumerate(pool)],'occurrences':occurrences,'structures':structures,'pure_identity_occurrences':pure,'exact_own_consumed_reuses':reused,'reconstruction':'Ordered child hashes and typed leaf source/ordinal references reconstruct the complete selected original AST/text. Raw bytes stay bound to Git objects; no behavior execution or automatic semantic-read credit.'}
    (OUT/(phase+'-complete-context-map.json')).write_text(json.dumps(pub,ensure_ascii=False,separators=(',',':'))+'\n')
    return pool,pub

if __name__=='__main__':
    phase=sys.argv[1];pool,pub=make(phase)
    start=int(sys.argv[2]);budget=int(sys.argv[3]);idx=start;items=[];size=0
    while idx<len(pool):
        x=pool[idx];ct=x['first_context'];s='S'+str(idx)+' I'+str(ct['input'])+' '+ct['pointer']+' '+ct['key']+' '+json.dumps(ct['record_context'],ensure_ascii=False,separators=(',',':'))+' = '+json.dumps(x['value'],ensure_ascii=False,separators=(',',':'))
        if items and size+len(s)>budget: break
        if not items and len(s)>budget:
            off=int(sys.argv[4]) if len(sys.argv)>5 else 0;frag=s[off:off+budget];items.append(display_private_identity(frag));size=len(frag);print('LONG_VALUE',idx,'CHAR_RANGE',off,min(off+budget,len(s)),'TOTAL',len(s));idx+=int(off+budget>=len(s));break
        items.append(display_private_identity(s));size+=len(s);idx+=1
    print('PHASE',phase,'SEMANTIC_VALUES',len(pool),'RANGE',start,idx,'CHARS',size,'INPUTS',len(pub['inputs']),'STRUCTURES',len(pub['structures']),'MECHANICAL_IDENTITIES',pub['pure_identity_occurrences'],'EXACT_REUSES',pub['exact_own_consumed_reuses'])
    print('\n'.join(items))
    with (OUT/'continuation-delivery.jsonl').open('a') as f: f.write(json.dumps({'phase':phase,'semantic_pool_range':[start,idx],'characters':size,'inputs':len(pub['inputs']),'semantic_read':'Offered only; actual output/truncation must be assessed.'})+'\n')
