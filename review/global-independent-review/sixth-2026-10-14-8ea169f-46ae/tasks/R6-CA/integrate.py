"""Assemble reviewed records; continuity/binding checks are not semantic PASS.
Inputs are the explicitly named task artifacts and fixed git objects. Reads
reference/formal bytes only. Writes final matrices/proof/findings only below O.
No source, model, old review tools, network, or real game is executed here.
"""
import csv,json,re,hashlib,subprocess
from pathlib import Path
W=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
O=Path(__file__).resolve().parent
S=O/'subtasks'
D=json.loads((O/'structural-denominator.json').read_text())
def jsonl(p):return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]
def csvrows(p):return list(csv.DictReader(p.open()))
def writejl(name,rows):(O/name).write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
core=jsonl(O/'forward-core.jsonl')
af=csvrows(S/'effects-a/forward-matrix.csv')
bf=json.loads((S/'effects-b/forward-matrix.json').read_text())
cf=jsonl(S/'effects-c/forward-matrix.jsonl')
forward=[];unmapped=[]
for file in D['source_files']:
    path=file['path']
    for u in file['units']:
        refs=[]
        for n,r in enumerate(core,1):
            if r['source']['path']==path and r['source']['start']==u['start']:refs.append({'artifact':'forward-core.jsonl','row':n,'assessment':r})
        for n,r in enumerate(af,1):
            if r['path']==path and int(r['line'])==u['start']:refs.append({'artifact':'subtasks/effects-a/forward-matrix.csv','row':n,'assessment':r})
        for n,r in enumerate(bf,1):
            if r['path']==path and r['start']==u['start']:refs.append({'artifact':'subtasks/effects-b/forward-matrix.json','row':n,'assessment':r})
        for n,r in enumerate(cf,1):
            if r['source']['path']==path and r['source']['start']==u['start']:refs.append({'artifact':'subtasks/effects-c/forward-matrix.jsonl','row':n,'assessment':r})
        row={'source':{'path':path,'start':u['start'],'end_envelope':u['envelope_end']},'unit':u['unit'],
             'explicit_semantic_records':refs,'status':'MANUAL_RECORDS_ATTACHED_NOT_BLANKET_PASS' if refs else 'BLOCKING_UNMAPPED'}
        forward.append(row)
        if not refs:unmapped.append(row['source'])
writejl('forward-matrix.jsonl',forward)

# Each catalog case keeps actual new derivation, not a blanket table grade.
vectors={}
for filename in ['vectors-core.tsv','vectors-core-extra.tsv']:
    for n,r in enumerate(csv.DictReader((O/filename).open(),delimiter='\t'),2):
        vectors.setdefault(int(r['catalog_line']),[]).append({'artifact':filename,'row':n,'assessment':r})
catalog='deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md'
catlines=(W/catalog).read_text().splitlines()
ids={};series=None
for n,line in enumerate(catlines,1):
    m=re.match(r'## (AB|AI|AE|BE|CE)[：:]',line)
    if m:series=m[1]
    m=re.match(r'\| ([A-Z]\d+[bcd]?) \|',line)
    if m:ids[series+'-'+m[1]]=n
for n,line in enumerate((S/'effects-a/vector-review.md').read_text().splitlines(),1):
    m=re.match(r'\| ((?:AE|BE|CE)-[A-Z]\d+[bcd]?) \|',line)
    if m:vectors.setdefault(ids[m[1]],[]).append({'artifact':'subtasks/effects-a/vector-review.md','row':n,'assessment':line})
for n,r in enumerate(json.loads((S/'effects-b/vector-matrix.json').read_text()),1):
    vectors.setdefault(r['line'],[]).append({'artifact':'subtasks/effects-b/vector-matrix.json','row':n,'assessment':r})
for n,r in enumerate(jsonl(S/'effects-c/catalog-matrix.jsonl'),1):
    if r['status']=='SOURCE_STATIC_DERIVED_VECTOR_CHECKED_WITH_NAMED_PRECONDITIONS':
        vectors.setdefault(r['line'],[]).append({'artifact':'subtasks/effects-c/catalog-matrix.jsonl','row':n,'assessment':r})
catalog_rows=[];cat_missing=[]
for identity,n in ids.items():
    owned=not identity.startswith('AB-')
    refs=vectors.get(n,[])
    row={'id':identity,'path':catalog,'line':n,'owned_ai_case':owned,'derivation_records':refs,
         'status':('READ_OUTSIDE_AI_SEMANTIC_SCOPE' if not owned else ('LOCAL_VECTOR_ASSESSED_WITH_PRECONDITIONS' if refs else 'BLOCKING_UNMAPPED_AI_VECTOR'))}
    catalog_rows.append(row)
    if owned and not refs:cat_missing.append(row)
writejl('catalog-matrix.jsonl',catalog_rows)

ar=csvrows(S/'effects-a/reverse-matrix.csv')
br=json.loads((S/'effects-b/reverse-matrix.json').read_text())
cr=jsonl(S/'effects-c/reverse-matrix.jsonl')
rr=jsonl(O/'reverse-core.jsonl')
data=jsonl(O/'data-check.jsonl')
short_files={
 'AC':'wp52-a-evaluation-coverage-and-data.md','AM':'wp52-a-generic-numerical-and-status-evaluation.md',
 'BC':'wp52-b-effect-coverage.md','BM':'wp52-b-field-damage-healing-and-target-evaluation.md',
 'CC':'wp52-c-item-control-coverage-and-data.md','CM':'wp52-c-items-calling-and-control-evaluation.md'}
manual={}
for i,r in enumerate(csv.DictReader((O/'reverse-supplement.tsv').open(),delimiter='\t'),2):
    path=catalog if r['file']=='TC' else 'deliverables/final-specification-set/combat-requirements/'+short_files[r['file']]
    manual[(path,int(r['line']))]={'artifact':'reverse-supplement.tsv','row':i,'assessment':r}
reverse=[];pending=[]
for block in D['formal_blocks']:
    path,n=block['path'],block['start_line'];refs=[];source_refs=[]
    for i,r in enumerate(rr,1):
        if r['path']==path and r['start_line']==n:refs.append({'artifact':'reverse-core.jsonl','row':i,'assessment':r})
    for i,r in enumerate(ar,1):
        if r['formal_path']==path and int(r['start_line'])==n and (r['state'].startswith('OWNED_') or r['state'].startswith('PROPOSED_')):
            refs.append({'artifact':'subtasks/effects-a/reverse-matrix.csv','row':i,'assessment':r})
    for i,r in enumerate(br,1):
        if r['formal']==path and r['line']==n:refs.append({'artifact':'subtasks/effects-b/reverse-matrix.json','row':i,'assessment':r})
    for i,r in enumerate(cr,1):
        if r['clause']['path']==path and r['clause']['line']==n:refs.append({'artifact':'subtasks/effects-c/reverse-matrix.jsonl','row':i,'assessment':r})
    for i,r in enumerate(core,1):
        if any(q['path']==path and q['start']<=n<=q['end'] for q in r['formal']):
            source_refs.append({'artifact':'forward-core.jsonl','row':i,'fact':r['fact'],'source':r['source'],'consumer':r['necessary_consumer']})
    for i,r in enumerate(data,1):
        if r['formal']['path']==path and r['formal']['line']==n:refs.append({'artifact':'data-check.jsonl','row':i,'assessment':r,'scope':'literal binding only;manual consumer in core facts'})
    if path==catalog:
        for r in catalog_rows:
            if r['line']==n:refs.append({'artifact':'catalog-matrix.jsonl','case':r['id'],'assessment':r})
    if (path,n) in manual:refs.append(manual[(path,n)])
    text=(W/path).read_text().splitlines()[n-1]
    if refs or source_refs:status='EXPLICIT_REVIEW_RECORDS_ATTACHED_NOT_BLANKET_PASS'
    elif text.startswith('#') or text=='---' or text.startswith('| ---') or (text.startswith('|') and ('身份' in text or '位置/修正' in text or 'ID |' in text or '族 |' in text or '效果 |' in text or '状态 |' in text or '默认值 |' in text or '数据组 |' in text or '数据 |' in text or '项 |' in text)):
        status='DOCUMENT_STRUCTURE_NO_BEHAVIOR_ASSERTION'
    elif n in [3,5] or text.startswith('- 上游') or text.startswith('- 下游') or text.startswith('- 保留'):
        status='DOCUMENT_PROVENANCE_DEPENDENCY_OR_RESERVED_SCOPE_NO_DYNAMIC_CLAIM'
    else:status='NEEDS_EXPLICIT_MANUAL_RESOLUTION'
    row={**block,'status':status,'explicit_clause_records':refs,'core_source_fact_records':source_refs}
    reverse.append(row)
    if status=='NEEDS_EXPLICIT_MANUAL_RESOLUTION':pending.append({'path':path,'line':n,'id':block['id'],'text':text})
writejl('reverse-matrix.jsonl',reverse)
writejl('reverse-pending.jsonl',pending)

# The three proposals retain author status; parent is a non-proposer reviewer.
proposals=json.loads((S/'effects-b/findings.json').read_text())
proposals+=json.loads((S/'effects-a/findings.json').read_text())['proposals']
for p in proposals:
    p['nonproposer_review']={'reviewer':'R6-CA parent','artifact':'nonproposer-rebuttals.md','opinion':'BEHAVIOR_PATH_NOT_REFUTED_OR_LOCATOR_CONFIRMED_WITH_NARROW_SCOPE','final_classification':'EXTERNAL_ROOT_DECISION_REQUIRED'}
(O/'findings.json').write_text(json.dumps(proposals,ensure_ascii=False,indent=2)+'\n')

# Physical range continuity and frozen input byte checks remain separate.
ledgers=[O/'reading-ledger.jsonl']+[S/q/'reading-ledger.jsonl' for q in ['effects-a','effects-b','effects-c']]
entries=[]
for lp in ledgers:
    for r in jsonl(lp):
        if isinstance(r.get('start'),int) and isinstance(r.get('end'),int) and r.get('log') and r.get('path'):
            entries.append((lp,r))
paths=[r['path'] for r in D['source_files']]+sorted(set(r['path'] for r in D['formal_blocks']))+['AGENTS.md']
proof=[]
for path in paths:
    raw=(W/path).read_bytes();length=len(raw.decode('utf-8-sig').splitlines());covered=set();origin=[]
    for lp,r in entries:
        if r['path']==path:
            covered.update(range(r['start'],r['end']+1));origin.append({'ledger':str(lp.relative_to(O)),'range':[r['start'],r['end']],'log':r['log']})
    if path.startswith('reference/'):
        frozen=subprocess.check_output(['git','-C',str(W/'reference/pokemon-essentials'),'show','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:'+path[len('reference/pokemon-essentials/'):]])
    else:frozen=subprocess.check_output(['git','-C',str(W),'show','8ea169fbd0f33f378b5d732fd6bea59e854e04a6:'+path])
    proof.append({'path':path,'lines':length,'unread_lines':[i for i in range(1,length+1) if i not in covered],
        'sha256':hashlib.sha256(raw).hexdigest(),'fixed_bytes_match':raw==frozen,'reading_evidence':origin,
        'scope':'PHYSICAL_RANGE_AND_INPUT_BINDING_ONLY_NOT_SEMANTIC_PASS'})
(O/'coverage-proof.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
summary={'primary_source_files':20,'primary_source_lines':sum(r['lines'] for r in D['source_files']),
 'canonical_source_units':len(forward),'semantic_unmapped_units':unmapped,'formal_files':len(set(r['path'] for r in D['formal_blocks'])),
 'formal_blocks':len(reverse),'formal_pending_manual':pending,
 'catalog_cases':len(catalog_rows),'owned_ai_cases':sum(x['owned_ai_case'] for x in catalog_rows),'unmapped_ai_vectors':cat_missing,
 'readable_unread_lines':sum(len(x['unread_lines']) for x in proof),'input_drift':[x['path'] for x in proof if not x['fixed_bytes_match']],
 'new_proposals':len(proposals),'independent_existing_rebuttal':'GR6-C-001','not_a_semantic_pass_from_automation':True}
(O/'integration-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ['formal_pending_manual']},ensure_ascii=False))
print('formal_pending_count',len(pending))
for r in pending: print(json.dumps({k:v for k,v in r.items() if k!='text'},ensure_ascii=False))
