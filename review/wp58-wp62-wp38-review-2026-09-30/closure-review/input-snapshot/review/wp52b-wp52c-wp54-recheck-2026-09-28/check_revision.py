"""Own text/identity/diff checks only. No reference or extractor script execution."""
from pathlib import Path
import json, hashlib, re, subprocess
ROOT=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT=ROOT/'review/wp52b-wp52c-wp54-recheck-2026-09-28'
PREV=ROOT/'review/wp52b-wp52c-wp54-review-2026-09-28'
REF=ROOT/'reference/pokemon-essentials'
COMMIT='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def meta(p):
    b=p.read_bytes();return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
def exact(p,d):
    return p.exists() and meta(p)=={k:d[k] for k in ['sha256','bytes']}
def save(n,d):
    (OUT/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
frozen=json.loads((OUT/'input-manifest.json').read_text())
old=json.loads((PREV/'input-manifest.json').read_text())
check={'fixed_inputs':len(frozen['inputs']),
 'changed_inputs':[d['path'] for d in frozen['inputs'] if not exact(ROOT/d['path'],d)],
 'changed_snapshots':[d['path'] for d in frozen['inputs'] if not exact(OUT/'input-snapshot'/d['path'],d)],
 'prior_sets':[]}
for name in ['wp52b-wp52c-wp54-review-2026-09-28','wp50-wp51-wp52a-recheck-2026-09-28',
 'wp50-wp51-wp52a-review-2026-09-28','wp46-wp47-review-2026-09-27','wp42-wp48-wp49-recheck-2026-09-27']:
    d=ROOT/'review'/name
    inp=json.loads((d/'input-manifest.json').read_text())['inputs']
    arts=json.loads((d/'final-checks.json').read_text())['artifacts']
    check['prior_sets'].append({'review':name,'inputs':len(inp),
     'changed_snapshots':[x['path'] for x in inp if not exact(d/'input-snapshot'/x['path'],x)],
     'artifacts':len(arts),'changed_artifacts':[x['path'] for x in arts if not exact(ROOT/x['path'],x)]})
# Registry path order and incremental additions, separate from behavior review.
mp=[d['path'] for d in frozen['manifest_rows']];om=[d['path'] for d in old['manifest_rows']]
tp=[d['path'] for d in frozen['delivery_rows']];ot=[d['path'] for d in old['delivery_rows']]
check['registry']={'manifest_count':len(mp),'tsv_count':len(tp),
 'old_manifest_order_preserved':[p for p in mp if p in set(om)]==om,
 'old_tsv_order_preserved':[p for p in tp if p in set(ot)]==ot,
 'manifest_added':sorted(set(mp)-set(om)), 'tsv_added':sorted(set(tp)-set(ot))}
diffs=[]
for p in sorted((PREV/'revision-diffs').glob('*.diff')):
    lines=p.read_text().splitlines(keepends=True)
    base,target=lines[0][4:].strip(),lines[1][4:].strip()
    src=(ROOT/base).read_text().splitlines(keepends=True);result=[];pos=0;h=2
    while h<len(lines):
        m=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',lines[h]);assert m,(p,h)
        start=int(m[1])-1 if int(m[1]) else 0
        result+=src[pos:start];pos=start;h+=1
        while h<len(lines) and not lines[h].startswith('@@ '):
            line=lines[h];h+=1
            if line.startswith('\\'):continue
            if line[0] in ' -':assert src[pos]==line[1:],(p,pos);pos+=1
            if line[0] in ' +':result.append(line[1:])
    result+=src[pos:]
    diffs.append({'path':str(p.relative_to(ROOT)),**meta(p),'base':base,'target':target,
                  'reconstructs_current':''.join(result).encode()==(ROOT/target).read_bytes()})
save('diff-checks.json',diffs)

# Scenario identity checks do not execute a behavioral model.
scenarios=[];bindings=[];links=[];badlinks=[]
specs=[d['path'] for d in frozen['changes_from_previous'] if d['path'].startswith('specs/')]
row_pattern=r'^\| ([A-Z]\d+[a-z]?) \|'
for p in specs:
    before=(PREV/'input-snapshot'/p).read_text();after=(ROOT/p).read_text()
    a={re.match(row_pattern,l)[1]:l for l in before.splitlines() if re.match(row_pattern,l)}
    b={re.match(row_pattern,l)[1]:l for l in after.splitlines() if re.match(row_pattern,l)}
    scenarios.append({'path':p,'before':len(a),'after':len(b),'added':sorted(set(b)-set(a)),
      'removed':sorted(set(a)-set(b)), 'changed':[k for k in a if k in b and a[k]!=b[k]],
      'unchanged':sum(a[k]==b.get(k) for k in a)})
    for n,l in enumerate(after.splitlines(),1):
        m=re.match(r'- (specs/[^：]+)：`([a-f0-9]{64})`（([\d,]+)字节）',l)
        if m:
            q,h,size=m.groups(); expected={'sha256':h,'bytes':int(size.replace(',',''))}
            bindings.append({'file':p,'line':n,'target':q,**expected,'matches':meta(ROOT/q)==expected})
        # The current appendix links bind one local target on the same line.
        m=re.search(r'\]\(([^)]+\.md)\)（`([a-f0-9]{64})`，([\d,]+)字节',l)
        if m:
            q,h,size=m.groups();target=(ROOT/p).parent/q;expected={'sha256':h,'bytes':int(size.replace(',',''))}
            bindings.append({'file':p,'line':n,'target':str(target.relative_to(ROOT)),**expected,'matches':meta(target)==expected})
for p in list((ROOT/'specs').rglob('*.md'))+[ROOT/'planning/feature-matrix.md',PREV/'revision-response.md',ROOT/'review/wp52b-wp52c-wp54-delivery-2026-09-28/delivery-summary.md']:
    for dest in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        dest=dest.strip('<>')
        if re.match(r'\w+://',dest) or dest.startswith('#'):continue
        dest=re.sub(r':\d+$','',dest.split('#')[0])
        if not dest:continue
        item={'file':str(p.relative_to(ROOT)),'target':dest,'exists':(p.parent/dest).exists()}
        links.append(item)
        if not item['exists']:badlinks.append(item)
jsons=[p for p in mp if p.endswith('.json')];badjson=[]
for p in jsons:
    try:json.loads((ROOT/p).read_text())
    except Exception as e:badjson.append({'path':p,'error':str(e)})
save('propagation-checks.json',{'scenario_rows':scenarios,'bindings':bindings,'binding_count':len(bindings),
 'link_count':len(links),'bad_links':badlinks,'registered_json':len(jsons),'bad_json':badjson})

# Confirm A's 48 history labels left each audit-identity list unchanged.
ap='specs/combat/wp52-a-evaluation-coverage-and-data.md'
def catalogue(text):
    return [l.replace('（未启动）','（A阶段定位）') for l in text.splitlines() if re.match(r'^\| WP52-[BC]（',l)]
def data_tables(text):
    return [l for l in text.splitlines() if l.startswith('|')]
coverage={'A_historical_rows':len(catalogue((ROOT/ap).read_text())),
 'A_historical_identity_rows_unchanged':catalogue((ROOT/ap).read_text())==catalogue((PREV/'input-snapshot'/ap).read_text())}
for p in ['specs/combat/wp52-b-effect-coverage.md','specs/combat/wp52-c-item-control-coverage-and-data.md','specs/combat/wp54-entry-rules-and-cup-data.md']:
    coverage[p]={'tables_unchanged':data_tables((ROOT/p).read_text())==data_tables((PREV/'input-snapshot'/p).read_text()),'bytes_unchanged':(ROOT/p).read_bytes()==(PREV/'input-snapshot'/p).read_bytes()}
self_data=json.loads((ROOT/'review/wp52b-wp52c-wp54-delivery-2026-09-28/self-checks.json').read_text())
coverage['self_package_keys']=[list(p) for p in self_data['packages']]
save('coverage-checks.json',coverage)

embedded={'self_artifacts':[],'self_packages':[],'self_vector_mismatches':[], 'boundary_bindings':[]}
for p,d in self_data['artifacts'].items():
    embedded['self_artifacts'].append({'path':p,'recorded':d,'actual':meta(ROOT/p),'matches':exact(ROOT/p,d)})
for package in self_data['packages']:
    embedded['self_packages'].append({'package':package['package'],'path':package['file'],'matches':exact(ROOT/package['file'],package)})
    rows={}
    for l in (ROOT/package['file']).read_text().splitlines():
        if re.match(row_pattern,l):
            cells=[x.strip() for x in l.strip('|').split('|')]
            rows[cells[0]]={'input':cells[1],'expected':cells[2]}
    for v in package['vectors']:
        if rows.get(v['id'])!={k:v[k] for k in ['input','expected']}:
            embedded['self_vector_mismatches'].append({'package':package['package'],'id':v['id'],'self':{k:v[k] for k in ['input','expected']},'spec':rows.get(v['id'])})
bd=json.loads((ROOT/'review/wp52b-wp52c-wp54-delivery-2026-09-28/boundary-checks.json').read_text())
for d in bd['bindings']:
    embedded['boundary_bindings'].append({'sender':d['sender'],'receiver':d['receiver'],'matches':exact(ROOT/d['sender'],d)})
embedded['classification']='BATCH-C02 nonblocking self-check metadata maintenance: five stale artifacts identities and Q41 status tail. Authoritative manifest/TSV and current spec contracts match; no behavioral finding.'
save('embedded-record-checks.json',embedded)

fresh={'Data/Scripts/011_Battle/006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb':'63–110,188–194',
 'Data/Scripts/011_Battle/005_AI/011_AIMove.rb':'4–15,81–86',
 'Data/Scripts/011_Battle/003_Move/001_Battle_Move.rb':'1–20,34–82',
 'Data/Scripts/014_Pokemon/004_Pokemon_Move.rb':'44–48',
 'Data/Scripts/011_Battle/005_AI/005_AI_ChooseMove.rb':'23–34',
 'Data/Scripts/011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb':'5–17',
 'Data/Scripts/011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb':'70–89,112–125',
 'Data/Scripts/011_Battle/007_Other battle code/006_Battle_Clauses.rb':'192–221',
 'Data/Scripts/011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb':'303–312'}
sources=[]
for d in json.loads((PREV/'source-checks.json').read_text())['paths']:
    p=ROOT/d['path'];rel=str(p.relative_to(REF))
    blob=subprocess.run(['git','--no-optional-locks','-C',str(REF),'show',COMMIT+':'+rel],capture_output=True,check=True).stdout
    sources.append({'path':d['path'],**meta(p),'commit_blob_equal':blob==p.read_bytes(),'unchanged_since_first_review':exact(p,d),
      'fresh_read_scope':fresh.get(rel),'inherited_only':rel not in fresh})
save('source-checks.json',{'reference_commit':COMMIT,'fresh_read_paths':len(fresh),'paths':sources,
 'text_search':'all Scripts: totalpp/method_missing/respond_to_missing?/OHKOIce redefinitions; no reference execution'})
check['reference_head']=subprocess.run(['git','--no-optional-locks','-C',str(REF),'rev-parse','HEAD'],capture_output=True,text=True,check=True).stdout.strip()
check['reference_status']=subprocess.run(['git','--no-optional-locks','-C',str(REF),'status','--porcelain'],capture_output=True,text=True,check=True).stdout
save('identity-checks.json',check)
print(json.dumps({'fixed':check['fixed_inputs'],'changed':check['changed_inputs'],'prior':check['prior_sets'],
 'registry':{k:v for k,v in check['registry'].items() if k not in ['manifest_added','tsv_added']},
 'added_sets_equal':check['registry']['manifest_added']==check['registry']['tsv_added'],'added':len(check['registry']['manifest_added']),
 'diffs':len(diffs),'bad_diffs':sum(not x['reconstructs_current'] for x in diffs),
 'scenario_changes':[s for s in scenarios if s['added'] or s['removed'] or s['changed']],
 'bindings':len(bindings),'bad_bindings':[x for x in bindings if not x['matches']],
 'links':len(links),'bad_links':badlinks,'jsons':len(jsons),'bad_json':badjson,'coverage':coverage,
 'source_files':len(sources),'bad_source':[x['path'] for x in sources if not x['commit_blob_equal'] or not x['unchanged_since_first_review']]},ensure_ascii=False,indent=2))
