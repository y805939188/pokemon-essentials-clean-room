"""Independent frozen-object identities and structural denominators; no semantic pass."""
from pathlib import Path
import collections, hashlib, json, re, subprocess

BASE=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT=Path(__file__).resolve().parent
ROOT=BASE/'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae'
MAIN='8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REF=BASE/'reference/pokemon-essentials'
def git(repo,*args):return subprocess.check_output(['git','-C',str(repo),*args])
def entries(repo,rev,path=None):
    args=['ls-tree','-rz',rev]
    if path:args+=['--',path]
    result=[]
    for row in git(repo,*args).split(b'\0'):
        if not row:continue
        header,p=row.split(b'\t',1);mode,kind,blob=header.decode().split()
        result.append({'path':p.decode(),'mode':mode,'kind':kind,'blob':blob})
    return result
def save(name,data):
    (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def audit_inventory(file,repo,rev,prefix=None):
    rows=json.loads((ROOT/'inventory'/file).read_text())
    actual={r['path']:r for r in entries(repo,rev,prefix) if r['kind']=='blob'}
    problems=[]; ids=[]
    for r in rows:
        a=actual.get(r['path'])
        if not a:problems.append({'path':r['path'],'reason':'not in fixed object'});continue
        b=git(repo,'cat-file','blob',a['blob'])
        expect={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':a['blob'],'mode':a['mode'],'commit':rev}
        mismatches={k:[r.get(k),v] for k,v in expect.items() if r.get(k)!=v}
        if r.get('type')=='text' and r.get('lines')!=len(b.splitlines()):mismatches['lines']=[r.get('lines'),len(b.splitlines())]
        if mismatches:problems.append({'path':r['path'],'mismatches':mismatches})
        ids.append({'path':r['path'],**expect,'review':'inventory_only; identities do not establish semantic coverage'})
    extra=sorted(set(actual)-{r['path'] for r in rows})
    duplicates=[p for p,n in collections.Counter(r['path'] for r in rows).items() if n>1]
    return {'root_inventory':file,'fixed_count':len(actual),'root_count':len(rows),'missing':extra,'duplicates':duplicates,'problems':problems,'identities':ids}

ra=audit_inventory('reference.json',REF,RC)
fa=audit_inventory('formal131.json',BASE,MAIN,'deliverables/final-specification-set')
save('reference-inventory-countercheck.json',ra);save('formal-inventory-countercheck.json',fa)
formal={r['path']:r for r in fa['identities']}
blocks=json.loads((ROOT/'inventory/formal-block-denominator.json').read_text())
by=collections.defaultdict(list)
for r in blocks:by[r['path']].append(r)
errors=[];records=[]
for path in formal:
    lines=git(BASE,'show',MAIN+':'+path).decode('utf-8-sig').splitlines()
    coverage=collections.Counter()
    for r in by[path]:
        for ln in range(r['start_line'],r['end_line']+1):coverage[ln]+=1
    missing=[i for i,l in enumerate(lines,1) if l.strip() and coverage[i]==0]
    duplicate=[i for i,n in coverage.items() if n!=1]
    blank=[i for i in coverage if 0<i<=len(lines) and not lines[i-1].strip()]
    bad=[i for i in coverage if i<=0 or i>len(lines)]
    records.append({'path':path,'nonblank_lines':sum(bool(l.strip()) for l in lines),'block_count':len(by[path]),'missing_nonblank':missing,'overlap_lines':duplicate,'covered_blank':blank,'out_of_bounds':bad})
    if missing or duplicate or blank or bad:errors.append(records[-1])
unknown=sorted(set(by)-set(formal))
save('formal-block-countercheck.json',{'kind':'structural_read','root_blocks':len(blocks),'root_id_duplicates':[p for p,n in collections.Counter(r['id'] for r in blocks).items() if n>1],'unknown_paths':unknown,'errors':errors,'records':records,'scope':'finite Markdown blocks, including headers/separators/history; not a count of behavioral requirements'})

specrows=[r for r in entries(BASE,MAIN,'specs') if r['kind']=='blob']
body={Path(p).name:p for p in formal if '/test-catalog/' not in p and Path(p).name not in ('README.md','scope-statement.md')}
audit=git(BASE,'show',MAIN+':audit/source-traceability.md').decode().splitlines()
heading='';loc={}
for i,l in enumerate(audit,1):
    if l.startswith('### T-'):heading=l[4:]
    if l.startswith('| 批准输入 |'):
        for p in re.findall(r'`(specs/[^`]+\.md)`',l):loc[p]={'trace_clause':heading,'input_line':i}
maps=[]
for r in specrows:
    name=Path(r['path']).name
    if name=='wp16-pre-battle-transitions-appendix.md':name='wp16-pre-battle-transitions.md'
    if r['path'].endswith('wp01-baseline-and-evidence-scope.md'):
        target='deliverables/final-specification-set/scope-statement.md';purpose='retained evidence-scope input; no independent game body'
    elif r['path'].endswith('wp02-settings-inventory-appendix.md'):
        target=body['wp02-rule-configuration-and-data-variants.md'];purpose='retained audit inventory; dictionary carried by formal WP02, not a separate gameplay contract'
    else:
        target=body.get(name);purpose='original author specification; current primary game contract is mapped formal body'
    b=git(BASE,'cat-file','blob',r['blob'])
    maps.append({'source':r['path'],'source_blob':r['blob'],'source_sha256':hashlib.sha256(b).hexdigest(),'source_bytes':len(b),'source_lines':len(b.splitlines()),'inspection':'inventory_only/full structural identity; no original gameplay semantic re-pass','primary':target,'purpose':purpose,**loc.get(r['path'],{}),'mapping_status':'mapped' if target else 'missing'})
save('specs113-primary-matrix.json',maps)
save('primary113-reverse.json',[{'primary':p,'original_inputs':[r['source'] for r in maps if r['primary']==p],'review':'structural relation only'} for p in sorted(formal)])

ws=[r for r in entries(BASE,MAIN) if r['kind']=='blob']
for r in ws:
    p=r['path']
    if p.startswith('deliverables/final-specification-set/'):kind='primary_formal'
    elif p in ('planning/coverage.md','planning/feature-matrix.md','audit/source-traceability.md'):kind='effective_current_supplement'
    elif p.startswith('specs/'):kind='original_spec_secondary_input'
    elif p.startswith('review/'):kind='historical_review_or_current_registration_evidence; stage qualification required'
    elif p.startswith('analysis/inventory/'):kind='generated_or_generator_inventory; structural evidence only'
    elif p.startswith(('analysis/','planning/')):kind='reconnaissance_planning_navigation; not independent gameplay requirements'
    else:kind='administrative_project_metadata; not gameplay requirements'
    r.update(identity_commit=MAIN,type_disposition=kind,semantic_status='not_inferred_from_identity')
save('workspace-types-full.json',ws)
counts={'reference':ra['fixed_count'],'formal':fa['fixed_count'],'formal_bodies':len(body),'formal_blocks':len(blocks),'specs_original':len(specrows),'mapped_originals':sum(r['primary'] is not None for r in maps),'originals_without_primary':[r['source'] for r in maps if not r['primary']],'formal_body_without_original':[p for p in body.values() if p not in {r['primary'] for r in maps}],'originals_without_trace_input':[r['source'] for r in maps if 'input_line' not in r],'workspace':len(ws),'workspace_types':dict(collections.Counter(r['type_disposition'] for r in ws)),'current_supplement_paths':3,'secondary_original_paths':113,'effective_available_supplement_path_units':116,'added_independent_game_requirement_denominator':0,'inventory_problems':len(ra['problems'])+len(fa['problems']),'block_problems':len(errors)+len(unknown)}
save('structural-summary.json',counts)
print(json.dumps(counts,ensure_ascii=False))
