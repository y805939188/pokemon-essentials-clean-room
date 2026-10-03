"""Read-only final audit of extractor-owned text, identities and diff reconstruction.

Prints results; does not write files or execute reference source.
"""
from pathlib import Path
import csv, hashlib, json, re, subprocess
from urllib.parse import unquote

ROOT=Path(__file__).resolve().parents[3]
D=ROOT/'review/wp22-wp23-wp32-delivery-2026-09-30'
O=D/'revision-v2'
C=ROOT/'review/wp22-wp23-wp32-review-2026-09-30'
COMMIT='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
errors=[]
cache={}

def identity(p):
    p=p.resolve()
    if p not in cache:
        b=p.read_bytes();cache[p]={'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
    return cache[p]

def verify(path,expected,label):
    p=ROOT/path
    actual=identity(p) if p.is_file() else None
    if actual!={k:expected[k] for k in ['sha256','bytes']}:
        errors.append({'check':label,'path':str(path),'expected':expected,'actual':actual})

pat=re.compile(r'^\| `([^`]+)`(.*?)\| `([a-f0-9]{8})` \| `([a-f0-9]{64})` \| ([\d,]+) \|$',re.M)
manifest=(ROOT/'planning/review-manifest-2026-09-19.md').read_text().split('## 2.')[0]
mr=[]
for path,annotation,short,sha,size in pat.findall(manifest):
    r={'path':path,'sha256':sha,'bytes':int(size.replace(',',''))};mr.append(r)
    verify(path,r,'manifest identity')
    if short!=sha[:8]:errors.append({'check':'manifest short label','path':path})
tsv_path=ROOT/'review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv'
tr=[]
for line in tsv_path.read_text().splitlines():
    if not line or line.startswith('#'):continue
    sha,size,path=line.split('\t');r={'path':path,'sha256':sha,'bytes':int(size)};tr.append(r);verify(path,r,'TSV identity')
for rows,label in [(mr,'manifest'),(tr,'TSV')]:
    paths=[r['path'] for r in rows]
    if len(paths)!=len(set(paths)):errors.append({'check':'duplicates','catalog':label})
frozen=json.loads((C/'input-manifest.json').read_text())
base_m={x['path'] for x in frozen['manifest_rows']};base_t={x['path'] for x in frozen['delivery_rows']}
now_m={x['path'] for x in mr};now_t={x['path'] for x in tr}
if not base_m<=now_m or not base_t<=now_t:errors.append({'check':'catalog deleted old rows'})
if now_m-now_t!=base_m-base_t or now_t-now_m!=base_t-base_m:errors.append({'check':'catalog set relationship changed'})

packages=[json.loads((D/f'wp{n}-fixed.json').read_text()) for n in [22,23,32]]
binding_count=0
for p in packages:
    if p['status']!=('ReviewPending' if p['package']=='WP23' else 'Reviewed'):errors.append({'check':'new status','package':p['package']})
    for a in p['artifacts']:verify(a['path'],a,'fixed package')
    main=(ROOT/p['artifacts'][0]['path']).read_text()
    scenes=re.findall(r'^\| (W\d{2}) \|',main,re.M)
    if scenes!=p['scenarios']:errors.append({'check':'scenario IDs','package':p['package']})
    for b in p['bindings']:
        binding_count+=1;verify(b['sender'],b,'dependency binding')
        if b['sha256'] not in main or f'{b["bytes"]:,}' not in main:
            errors.append({'check':'inline binding missing','sender':b['sender'],'receiver':b['receiver']})
    if any(x['expected']!=x['actual'] for x in p['static_checks']):errors.append({'check':'fixed arithmetic/set check','package':p['package']})
    for a in p['artifacts']:
        txt=(ROOT/a['path']).read_text()
        if re.search(r'^```(?:ruby|typescript|javascript|python)',txt,re.M):errors.append({'check':'source code fence','path':a['path']})
        if not txt.splitlines()[2].startswith('状态：**'+p['status']):errors.append({'check':'current header status','path':a['path']})

current_self=json.loads((D/'self-checks.json').read_text())
current_boundary=json.loads((D/'boundary-checks.json').read_text())
for pkg in current_self['packages']:
    for row in pkg['artifacts']:verify(row['path'],row,'current self artifact')
for row in current_boundary['bindings']:verify(row['sender'],row,'current boundary')
for parent,key in [(current_self,'source_identity_file'),(current_self,'matrix'),(current_self,'revision_checks'),(current_boundary,'matrix'),(current_boundary,'new_observations')]:
    row=parent[key];verify(row['path'],row,'current audit binding')
if current_self['total_scenarios']!=109 or current_boundary['binding_count']!=46:errors.append({'check':'current counts'})
for n in [22,23,32]:
    orig=json.loads((C/'input-snapshot'/str((D/f'wp{n}-fixed.json').relative_to(ROOT))).read_text())
    cur=json.loads((D/f'wp{n}-fixed.json').read_text())
    if cur['review_history'][0]['artifacts']!=orig['artifacts']:errors.append({'check':'reviewed artifact history','package':n})
# Approved WP31 change is one old body row plus the explicit maintenance note.
wp31='specs/pokemon-rules/wp31-basic-evolution.md'
old31=(C/'input-snapshot'/wp31).read_text();new31=(ROOT/wp31).read_text()
new31body=new31.split('\n2026-09-30 WP32-N01单点行为摘要同步：',1)[0]
oldline=old31.splitlines()[113];newlines=[l for l in new31body.splitlines() if l.startswith('| `BattleDealCriticalHit` |')]
if len(newlines)!=1 or old31.replace(oldline,newlines[0],1)!=new31body:errors.append({'check':'WP31 exceeded N01 one-line scope'})
for name in ['wp22-transformation-data.md','wp32-context-inputs-and-scenarios.md']:
    path='specs/pokemon-rules/'+name
    oldrows=[l for l in (C/'input-snapshot'/path).read_text().splitlines() if l.startswith('|')]
    newrows=[l for l in (ROOT/path).read_text().splitlines() if l.startswith('|')]
    if oldrows!=newrows:errors.append({'check':'accepted data tables changed','path':path})

def reconstruct(base,diff):
    lines=base.splitlines(True);parts=diff.splitlines(True);out=[];cursor=0;i=2;hunks=0
    while i<len(parts):
        m=re.match(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',parts[i])
        if not m:raise ValueError('bad hunk header '+parts[i])
        start=int(m[1]);pos=max(start-1,0);oldcount=int(m[2]) if m[2] is not None else 1;newcount=int(m[4]) if m[4] is not None else 1
        if pos<cursor:raise ValueError('overlap')
        out.extend(lines[cursor:pos]);cursor=pos;i+=1;removed=added=0;hunks+=1
        while i<len(parts) and not parts[i].startswith('@@'):
            mark=parts[i][0];value=parts[i][1:]
            if mark in ' -':
                if cursor>=len(lines) or lines[cursor]!=value:raise ValueError('base mismatch')
                cursor+=1;removed+=1
            if mark in ' +':out.append(value);added+=1
            if mark not in ' +-':raise ValueError('unexpected diff marker')
            i+=1
        if (removed,added)!=(oldcount,newcount):raise ValueError('hunk counts')
    out.extend(lines[cursor:]);return ''.join(out),hunks

diffs=json.loads((O/'diff-bindings.json').read_text())['diffs'];diff_result=[]
for x in diffs:
    verify(x['path'],x,'diff identity');verify(x['base']['path'],x['base'],'diff base');verify(x['target']['path'],x['target'],'diff final target')
    try:
        rebuilt,n=reconstruct((ROOT/x['base']['path']).read_text(),(ROOT/x['path']).read_text())
        ok=rebuilt.encode()==(ROOT/x['target']['path']).read_bytes()
        if not ok:errors.append({'check':'diff reconstruction','path':x['path']})
        diff_result.append({'path':x['path'],'hunks':n,'exact':ok})
    except Exception as e:errors.append({'check':'diff reconstruction','path':x['path'],'error':str(e)})

whitelist=json.loads((O/'change-whitelist.json').read_text());allowed=set(whitelist['existing_allowed'])
baseline=list(csv.DictReader((O/'preexisting-files.tsv').open(),delimiter='\t'))
changed=[]
for x in baseline:
    path=x['path'];p=ROOT/path
    cur=identity(p) if p.is_file() else None
    expected={'sha256':x['sha256'],'bytes':int(x['bytes'])}
    if cur!=expected:
        changed.append(path)
        if path not in allowed:errors.append({'check':'unexpected preexisting change','path':path})
before_paths={x['path'] for x in baseline};new=[]
for p in ROOT.rglob('*'):
    rel=p.relative_to(ROOT)
    if not p.is_file() or '.git' in rel.parts:continue
    name=str(rel)
    if name in before_paths:continue
    new.append(name)
    if not (any(name.startswith(prefix) for prefix in whitelist['new_allowed_prefixes']) or name in whitelist['new_allowed_exact']):errors.append({'check':'unexpected new file; inspect independent-work applicability without rollback','path':name})
fixed_changed=[]
for x in frozen['inputs']:
    verify(str((C/'input-snapshot'/x['path']).relative_to(ROOT)),x,'876 fixed snapshot')
    if identity(ROOT/x['path'])!={k:x[k] for k in ['sha256','bytes']}:
        fixed_changed.append(x['path'])
        if x['path'] not in allowed:errors.append({'check':'unexpected 876 input change','path':x['path']})
if set(fixed_changed)!=set(changed):errors.append({'check':'876 vs workspace change set differs'})

json_paths={r['path'] for r in mr if r['path'].endswith('.json')}
for path in json_paths:
    try:json.loads((ROOT/path).read_text())
    except Exception as e:errors.append({'check':'JSON parse','path':path,'error':str(e)})
markdown=list((ROOT/'specs').rglob('*.md'))+[ROOT/'planning/feature-matrix.md']+list(D.glob('*.md'))+[C/'revision-response.md']
link_count=0
for p in markdown:
    txt=p.read_text()
    for target in re.findall(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)',txt):
        if target.startswith(('http:','https:','mailto:','#','codex:')):continue
        target=unquote(target.split('#',1)[0]).strip('<>');target=re.sub(r':\d+$','',target)
        if not target:continue
        link_count+=1
        if not (p.parent/target).exists():errors.append({'check':'missing Markdown link','file':str(p.relative_to(ROOT)),'target':target})

source=json.loads((D/'source-identities.json').read_text())
for x in source['sources']:verify(x['path'],x,'source identity')
refhead=subprocess.check_output(['git','-C',str(ROOT/'reference/pokemon-essentials'),'rev-parse','HEAD'],text=True).strip()
refstatus=subprocess.check_output(['git','-C',str(ROOT/'reference/pokemon-essentials'),'status','--porcelain'],text=True)
if refhead!=COMMIT or refstatus:errors.append({'check':'reference baseline or status','HEAD':refhead,'status':refstatus})


historical_diffs=[]
for x in json.loads((D/'diff-bindings.json').read_text())['diffs']:
    verify(x['path'],x,'old diff original')
    verify(x['base']['path'],x['base'],'old diff base snapshot')
    old_target=C/'input-snapshot'/x['target']['path']
    rebuilt,n=reconstruct((ROOT/x['base']['path']).read_text(),(ROOT/x['path']).read_text())
    ok=rebuilt.encode()==old_target.read_bytes()
    if not ok:errors.append({'check':'historical diff target reconstruction','path':x['path']})
    historical_diffs.append({'path':x['path'],'exact_to_first_review_snapshot':ok})

result={'date':'2026-09-30','role':'extractor limited-revision read-only final integrity check; not independent approval',
 'all_checks_passed':not errors,'errors':errors,'manifest_rows':len(mr),'main_TSV_rows':len(tr),
 'old_manifest_rows_retained':len(base_m),'old_TSV_rows_retained':len(base_t),
 'new_package_artifacts':sum(len(p['artifacts']) for p in packages),'scenario_counts':{p['package']:len(p['scenarios']) for p in packages},
 'bindings_checked':binding_count,'reviewed_v1_history_checked':6,
 'registered_JSON':len(json_paths),'Markdown_relative_links':link_count,'diff_reconstruction':diff_result,'historical_diff_reconstruction':historical_diffs,
 'preexisting_files':len(baseline),'expected_changed_existing':sorted(changed),'new_files':sorted(new),
 'frozen_876_changed_only_whitelist':sorted(fixed_changed),'closure_snapshots_checked':len(frozen['inputs']),
 'protected_preexisting_unchanged':len(baseline)-len(changed),
 'historical_scope':'All preexisting reviewer originals, prior response/diff originals and snapshots unchanged, verified against preexisting-files.tsv; fixed prior snapshot identities were additionally checked in preflight.',
 'source_files_checked':source['count'],'source_commit_blobs_equal':all(x['matches_commit_blob'] for x in source['sources']),
 'reference':{'HEAD':refhead,'ordinary_git_status':refstatus},
 'state':'WP22/WP32 scoped Reviewed after independent first review; WP23 R01–R03 revised v2 ReviewPending; WP31 N01 authorized one-point sync; N02 runtime retained.',
 'execution':'Own text/hash/set/JSON/diff and fixed arithmetic only; no reference/game/UI/network execution, no agents/tasks/messages/commit/push.',
 'self_hash_policy':'This result contains no hash of itself or containing manifest/TSV. After registration rerun read-only and compare identical output; includes the current result file identity.'}
print(json.dumps(result,ensure_ascii=False,indent=2))
