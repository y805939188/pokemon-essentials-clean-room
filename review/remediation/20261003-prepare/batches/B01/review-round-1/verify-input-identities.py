import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path('/workspace/pokemon-essentials-clean-room')
REF = Path('/workspace/reference-r-b01-independent')
REPORT = Path('/workspace/r-b01-original-report')
CANDIDATE = 'c7e30a1197083e86315d735fcfde5e31574d935a'
PRE0 = '8f3a811855fc43b5fe5eb7809931b4e1749200de'
PREVIOUS = 'e6f14de7d0d9600ce0e058c1bd05b9348f7a06d3'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
BASE = 'e1e01bb18d824931e54f182dd61af5a9f908ba85'
FINAL_REPORT = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
REF_SHA = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
P = 'review/remediation/20261003-prepare/batches/B01/'
R = 'review/global-independent-review/2026-10-03-fd82a639/'

def git(*args, root=ROOT):
    return subprocess.check_output(['git', *args], cwd=root)

def read_at(sha, path):
    return git('show', f'{sha}:{path}')

def sha256(value):
    return hashlib.sha256(value).hexdigest()

def record(path, sha=CANDIDATE):
    value = read_at(sha, path)
    return {'path': path, 'git_blob': git('rev-parse', f'{sha}:{path}').decode().strip(),
            'sha256': sha256(value), 'bytes': len(value), 'lines': len(value.splitlines())}

checks = []

def check(name, condition, evidence):
    checks.append({'check': name, 'result': 'PASS' if condition else 'FAIL', 'evidence': evidence})

manifest = json.loads(read_at(CANDIDATE, P + 'author-v2/candidate-manifest.json'))
formal = [x['path'] for x in manifest['formal_files']]
batch = json.loads(read_at(PLAN, 'review/remediation-20261003-prepare/batches.json'))[0]
check('candidate and previous parent identities',
      git('rev-parse', CANDIDATE+'^').decode().strip() == PREVIOUS and
      git('rev-parse', PREVIOUS+'^').decode().strip() == PRE0 and
      git('rev-parse', PRE0+'^').decode().strip() == PLAN,
      {'candidate': CANDIDATE, 'parent': PREVIOUS, 'complete_diff_base': PRE0, 'plan': PLAN})
check('formal scope exactly original six plus two authorized originals',
      formal == batch['write_paths'] + ['specs/kernel/wp04-pbs-lifecycle.md', 'specs/kernel/wp05-events-extensions-plugins.md'], formal)
changes = git('diff', '--name-status', PRE0, CANDIDATE).decode().splitlines()
formal_changes = [x.split('\t')[1] for x in changes if not x.split('\t')[1].startswith(P)]
allowed_records = {P+'scope-amendment-01.md'}
allowed_records.update(P+'author/'+x.name for x in (ROOT/P/'author').iterdir() if x.is_file())
allowed_records.update(P+'author-v2/'+x.name for x in (ROOT/P/'author-v2').iterdir() if x.is_file())
check('full candidate changes only eight formal paths and B01 author records',
      set(formal_changes) == set(formal) and len(changes) == 38 and
      all(x.split('\t')[1] in set(formal)|allowed_records for x in changes) and
      all(x.startswith('A\t') for x in changes if x.split('\t')[1] in allowed_records), changes)
formal_identities = [record(x) for x in formal]
errors = []
for expected, actual in zip(manifest['formal_files'], formal_identities):
    if not (expected['candidate_git_blob'] == actual['git_blob'] and expected['candidate_sha256'] == actual['sha256'] and expected['bytes'] == actual['bytes'] and
            expected['complete_review_base_blob'] == record(actual['path'], PRE0)['git_blob'] and
            expected['previous_candidate_blob'] == record(actual['path'], PREVIOUS)['git_blob']):
        errors.append(actual['path'])
check('independent formal identities match author manifest at all three commits', not errors, {'mismatches': errors, 'files': 8})
full_patch = git('diff', PRE0, CANDIDATE, '--', *formal)
incremental = git('diff', PREVIOUS, CANDIDATE, '--', *formal)
check('complete and incremental patches equal independent Git diff bytes',
      full_patch == read_at(CANDIDATE, P+'author-v2/formal-diff.patch') and
      incremental == read_at(CANDIDATE, P+'author-v2/incremental-formal-diff.patch') and
      sha256(full_patch) == manifest['complete_formal_diff_sha256'] and
      sha256(incremental) == manifest['incremental_formal_diff_sha256'],
      {'complete_sha256': sha256(full_patch), 'complete_bytes': len(full_patch), 'incremental_sha256': sha256(incremental), 'incremental_bytes': len(incremental)})
rec_err = []
for expected in manifest['author_record_content_hashes']:
    actual = record(expected['path'])
    if expected['sha256'] != actual['sha256'] or expected['bytes'] != actual['bytes']:
        rec_err.append(expected['path'])
check('manifest enumerated new record content hashes', not rec_err, {'count': len(manifest['author_record_content_hashes']), 'mismatches': rec_err})
immutable_err = []
for expected in manifest['immutable_v1_author_records']:
    path = expected['path']
    actual = record(path)
    if read_at(CANDIDATE, path) != read_at(PREVIOUS, path) or any(actual[k] != expected[k] for k in ['git_blob','sha256','bytes']):
        immutable_err.append(path)
check('sixteen old author records unchanged byte for byte', not immutable_err, {'count':16, 'mismatches': immutable_err})
check('six final formal files unchanged in appended candidate',
      all(read_at(CANDIDATE,x)==read_at(PREVIOUS,x) for x in formal[:6]), {'files':formal[:6]})
pre0_paths = ['review/remediation/20261003-prepare/'+n for n in ['global-premises.json','model-request-receipts.json','finding-ledger.tsv','PRE0-handoff.md']]
check('four PRE0 records unchanged', all(read_at(PRE0,p)==read_at(CANDIDATE,p) for p in pre0_paths), [record(x,PRE0) for x in pre0_paths])
plan_changes = git('diff','--name-status',BASE,PLAN).decode().splitlines()
check('plan adds preparation records only; original formal content unchanged',
      len(plan_changes)==46 and all(x.startswith('A\treview/remediation-20261003-prepare/') for x in plan_changes) and
      not git('diff','--name-only',BASE,PLAN,'--','AGENTS.md','specs','deliverables','audit','planning'), {'added_plan_paths':len(plan_changes)})
check('PRE0 adds only four freeze records',
      set(git('diff','--name-only',PLAN,PRE0).decode().splitlines())==set(pre0_paths), pre0_paths)
check('public registers and historical reports are not changed by candidate',
      not git('diff','--name-only',PRE0,CANDIDATE,'--','AGENTS.md','audit','planning','review/global-independent-review','review/wp80-delivery-2026-10-03','review/wp80-batch-02-review-2026-10-03','review/gr001-gr003-review-2026-10-01','deliverables/final-specification-set/README.md','deliverables/final-specification-set/scope-statement.md','deliverables/final-specification-set/test-catalog/README.md'), 'Git path equality; central state not approved or closed')
canonical=json.loads((REPORT/R/'findings.json').read_text())
if isinstance(canonical,dict): canonical=canonical['findings']
all_by_id={x['id']:x for x in canonical}
ids=batch['contribution_finding_ids']
original={i:all_by_id[i] for i in ids}
author_original=json.loads(read_at(CANDIDATE,P+'author/original-findings.json'))
check('all fourteen full author objects equal independently fetched canonical objects',
      {x['id']:x for x in author_original}==original, {'ids':ids,'canonical_commit':FINAL_REPORT,'canonical_findings_blob':git('rev-parse',FINAL_REPORT+':'+R+'findings.json').decode().strip()})
acceptance=json.loads(read_at(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json'))
accept_err=[]
for i in ids:
    for key,val in acceptance[i].items():
        if key in original[i] and original[i][key]!=val: accept_err.append([i,key])
check('acceptance overlapping effective fields equal canonical original objects',not accept_err,{'mismatches':accept_err,'count':14})
required=[x for x in canonical if x['required_revision']]
check('canonical required counts retain original priorities', len(canonical)==233 and len(required)==229 and sum(x['priority']=='P2' for x in required)==200 and sum(x['priority']=='P3' for x in required)==29, {'canonical':len(canonical),'required':len(required),'nonrequired':len(canonical)-len(required),'P2':sum(x['priority']=='P2' for x in required),'P3':sum(x['priority']=='P3' for x in required)})
ledger=list(csv.DictReader(read_at(CANDIDATE,'review/remediation/20261003-prepare/finding-ledger.tsv').decode().splitlines(),delimiter='\t'))
check('PRE0 ledger all required IDs remain OPEN',len(ledger)==229 and {x['finding_id'] for x in ledger}=={x['id'] for x in required} and all(x['canonical_state']=='OPEN' for x in ledger),{'rows':len(ledger)})
responses=json.loads(read_at(CANDIDATE,P+'author-v2/finding-responses.json'))['responses']
old_responses=json.loads(read_at(CANDIDATE,P+'author/finding-responses.json'))['responses']
changed_responses=[a['finding_id'] for a,b in zip(responses,old_responses) if a!=b]
check('fourteen responses and exactly seven primary responsibilities; canonical state OPEN',
      [x['finding_id'] for x in responses]==ids and [x['finding_id'] for x in responses if x['primary_in_B01']]==batch['primary_finding_ids'] and all(x['canonical_state']=='OPEN' for x in responses),{'contributions':14,'primary':7})
check('only authorized four-ID response objects updated',set(changed_responses)=={'GIR-FD82-A001','GIR-FD82-A002','GIR-FD82-A004','GIR-FD82-A009'},changed_responses)
refs=json.loads(read_at(CANDIDATE,P+'author/reading-leaf-references.json'))
values={x['leaf']:x['value'] for x in map(json.loads,read_at(CANDIDATE,P+'author/reading-leaf-values.jsonl').decode().splitlines())}
leaf_err=[]
for item in refs:
    val=original
    for part in item['path'].split('/'):
        val=val[int(part)] if isinstance(val,list) else val[part]
    if val!=values[item['leaf']]: leaf_err.append(item['path'])
check('author lossless leaf records resolve against independent original objects',not leaf_err,{'occurrences':len(refs),'unique_values':len(values),'mismatches':leaf_err})
vectors=json.loads(read_at(CANDIDATE,P+'author-v2/static-vectors.json'))
old_vectors=json.loads(read_at(CANDIDATE,P+'author/static-vectors.json'))
check('final static objects and exact character vectors unchanged from old candidate',vectors['test_rows']==old_vectors['test_rows'] and vectors['exact_A001_strings']==old_vectors['exact_A001_strings'],{'rows':len(vectors['test_rows'])})
vector_err=[]
for row in vectors['test_rows']:
    line=read_at(CANDIDATE,row['path']).decode().splitlines()[row['line']-1]
    parts=[x.strip() for x in line.split('|')[1:-1]]
    if parts!=[row['test_id'],row['input_and_premises'],row['expected_static_result']] or row['execution']!='NOT_EXECUTED_STATIC_DERIVATION': vector_err.append(row['test_id'])
for row in vectors['source_spec_synchronization']:
    line=read_at(CANDIDATE,row['path']).decode().splitlines()[row['line']-1]
    if line!=row['literal_row'] or row['execution']!='NOT_EXECUTED_STATIC_DERIVATION': vector_err.append(row['scene'])
check('31 final and 11 original static row objects resolve to frozen candidate exact text',not vector_err,{'final':len(vectors['test_rows']),'original':len(vectors['source_spec_synchronization']),'mismatches':vector_err})
def table_rows(path,sha):
    rows={}
    for line in read_at(sha,path).decode().splitlines():
        m=re.match(r'^\| ([A-Z]{2}\d+) \|',line)
        if m:
            if m[1] in rows: raise ValueError('duplicate '+m[1])
            rows[m[1]]=line
    return rows
old={};new={}
for p in formal[4:6]:
    old.update(table_rows(p,PRE0));new.update(table_rows(p,CANDIDATE))
added=sorted(set(new)-set(old)); changed=sorted(x for x in old if new.get(x)!=old[x])
check('20 new catalog IDs, three old edits, none deleted',set(added)=={'KC06','KR13',*['KL'+str(x) for x in range(19,33)],*['EP'+str(x) for x in range(18,22)]} and changed==['EP07','EP08','KL10'] and not set(old)-set(new),{'new_ids':added,'changed_existing':changed,'total_rows':len(new)})
check('shared WP05–10 test file all non-EP rows unchanged',all(v==new[k] for k,v in old.items() if k[:2] not in {'KC','KR','KL','EP'}),'TM/IO/DP/LZ/SV/MG rows compared byte for byte')
exact=vectors['exact_A001_strings']
prefix=chr(0x5c)+chr(0x22)
check('A001 inputs have one real slash/quote per endpoint and ASCII comma',exact['input_exhausted']==prefix+'Alpha,Beta'+prefix and exact['input_with_tail']==prefix+'Alpha,Beta'+prefix+',Other' and exact['expected_exhausted_flags']==[prefix+'Alpha,Beta'+prefix] and exact['expected_with_tail_flags']==['Alpha,Beta','Other'],{'input_exhausted_codepoints':[f'U+{ord(c):04X}' for c in exact['input_exhausted']], 'execution':'text validation only'})
allowed_sections={formal[6]:['### 3.1','### 4.2','### 9.2'],formal[7]:['### 5.1','### 5.2','### 6.2','### 6.3','### 9.2']}
section_checks=[]
for p,allowed in allowed_sections.items():
    old_lines=read_at(PRE0,p).decode().splitlines(); new_lines=read_at(CANDIDATE,p).decode().splitlines()
    def sections(lines):
        chunks={};heading='PREAMBLE'
        for line in lines:
            if line.startswith('##'):heading=line
            chunks.setdefault(heading,[]).append(line)
        return chunks
    a=sections(old_lines);b=sections(new_lines)
    changed_sec=[h for h in set(a)|set(b) if a.get(h)!=b.get(h)]
    section_checks.append({'path':p,'changed_sections':sorted(changed_sec)})
    check('original-spec changed sections bounded: '+p,all(any(h.startswith(x) for x in allowed) for h in changed_sec),changed_sec)
    old12=next(i for i,line in enumerate(old_lines) if line.startswith('## 12.'))
    new12=next(i for i,line in enumerate(new_lines) if line.startswith('## 12.'))
    check('original-spec head and §12 historical paragraphs unchanged: '+p,old_lines[:14]==new_lines[:14] and old_lines[old12:]==new_lines[new12:], 'historical approval not evidence of current candidate')
json_errors=[]; json_paths=[]
def scenes(path, sha):
    result={}
    in_scene=False
    for line in read_at(sha,path).decode().splitlines():
        if line.startswith('### 9.2'): in_scene=True
        elif line.startswith('##') and in_scene: in_scene=False
        if in_scene and line.startswith('| ') and not line.startswith('| ---'):
            key=line.split('|')[1].strip()
            if key!='场景':result[key]=line
    return result
scene_changes=[]
for p in formal[6:]:
    a=scenes(p,PRE0);b=scenes(p,CANDIDATE)
    renames={'引号文本（奇数个引号）':'引号文本（合并耗尽／有独立尾值）'} if p==formal[6] else {'依赖版本不足':'依赖版本不足（有／无 Link）'}
    normalized_a={renames.get(k,k):v for k,v in a.items()}
    scene_changes.append({'path':p,'old_count':len(a),'new_count':len(b),'added':sorted(set(b)-set(normalized_a)), 'changed':sorted(k for k,v in normalized_a.items() if b.get(k)!=v), 'deleted':sorted(set(normalized_a)-set(b)), 'existing_row_renames':renames})
check('original scenes add exactly six; change four old rows and delete none',sum(len(x['added']) for x in scene_changes)==6 and sum(len(x['changed']) for x in scene_changes)==4 and not any(x['deleted'] for x in scene_changes),scene_changes)
for p in formal[6:]:
    a=scenes(p,PRE0);b=scenes(p,CANDIDATE)
    controls=[k for k in a if ('引号文本' in k and ('非末' in k or '末字段' in k or '普通未' in k))]
    check('existing correct quote controls unchanged: '+p, all(a[k]==b[k] for k in controls), controls)
original_wp05=read_at(CANDIDATE,formal[7]).decode()
guard='`getPluginOrder:541` 只检查**解析后的 scripts 值**是否为假。因此：**作者省略 Scripts 行不会缺少该键**（默认数组兜底，目录有脚本即自动收集，无脚本则为空列表，均不触发 541 行错误）'
check('correct original false-value/empty-list guard retained',
      guard in original_wp05 and guard in read_at(PRE0,formal[7]).decode(), 'original rule already correct; no broad empty-length normalization')
registry=json.loads(read_at(CANDIDATE,P+'author-v2/registry-proposals.json'))
check('registration proposals remain proposals and all canonical IDs OPEN',registry['state']=='PROPOSED_PENDING_ULTRA' and registry['canonical_state']=='OPEN' and registry['sole_writer']=='A-REG' and [x['finding_id'] for x in registry['entries']]==ids,{'canonical_state':registry['canonical_state'],'state':registry['state'],'sole_writer':registry['sole_writer']})
response_test_ids={t for x in responses for t in x['static_test_ids']}
check('response and synchronization references resolve to catalog IDs',response_test_ids <= set(new) and all(x['corresponding_final_test_id'] in new for x in vectors['source_spec_synchronization']),{'response_test_ids':sorted(response_test_ids)})
seven=['creature-rpg/wp68-triple-triad.md','user-interface/wp68-duel.md','user-interface/wp69-slot-machine.md','user-interface/wp69-slot-reels.md','user-interface/wp70-mining.md','user-interface/wp71-tile-puzzles.md','pokemon-rules/wp69-voltorb-layouts.md']
nav=[]
for rel in seven:
    path='deliverables/final-specification-set/'+rel
    text=read_at(CANDIDATE,path).decode()
    old_target=(ROOT/path).parent/'../../audit/source-traceability.md'
    corrected_target=(ROOT/path).parent/'../../../audit/source-traceability.md'
    nav.append({'path':path,'unchanged':read_at(CANDIDATE,path)==read_at(PRE0,path),'old_link_present':'../../audit/source-traceability.md' in text,'old_target_exists':old_target.exists(),'corrected_target_exists':corrected_target.exists()})
check('known seven broken audit links remain unchanged and proposal target resolves',all(x['unchanged'] and x['old_link_present'] and not x['old_target_exists'] and x['corrected_target_exists'] for x in nav),nav)
for p in sorted(allowed_records):
    if p.endswith('.json'):
        json_paths.append(p)
        try:json.loads(read_at(CANDIDATE,p))
        except Exception as exc:json_errors.append([p,str(exc)])
check('all author and amendment JSON records parse structurally',not json_errors,{'count':len(json_paths),'errors':json_errors})
whitespace = subprocess.run(['git','diff','--check',PRE0,CANDIDATE,'--',*formal],cwd=ROOT,capture_output=True,text=True)
check('complete formal diff whitespace check',whitespace.returncode==0,whitespace.stdout+whitespace.stderr)
check('fresh independently fetched reference fixed and clean',git('rev-parse','HEAD',root=REF).decode().strip()==REF_SHA and not git('status','--porcelain',root=REF) and str(REF).startswith(str(ROOT))==False,{'directory':str(REF),'commit':git('rev-parse','HEAD',root=REF).decode().strip(),'tree':git('rev-parse','HEAD^{tree}',root=REF).decode().strip(),'origin':git('remote','get-url','origin',root=REF).decode().strip()})
remote=git('ls-remote','origin','refs/heads/main','refs/heads/remediation/20261003-prepare/batch-B01','refs/heads/remediation/20261003-prepare/review-B01-1').decode().splitlines()
remote_dict={line.split('\t')[1]:line.split('\t')[0] for line in remote}
check('remote candidate and main identities at reviewer verification time',remote_dict.get('refs/heads/main')==BASE and remote_dict.get('refs/heads/remediation/20261003-prepare/batch-B01')==CANDIDATE,remote_dict)
output={'reviewer':'R-B01','candidate_commit':CANDIDATE,'complete_diff_base':PRE0,'original_report_commit':FINAL_REPORT,'kind':'independent text/JSON/Git/hash checks only; no behavioral execution','checks':checks,'formal_files':formal_identities,'full_candidate_name_status':changes,'check_development_notes':['§12 heading was initially assumed literally; actual heading located by section prefix before final check.','Scene labels A001 and A009 rename existing rows; initial label-only comparison counted renames as deletion/addition. Corrected two explicit mappings; six new scenes and four changed rows independently confirmed.','Original WP05 uses Chinese 假, not literal English false; checked preserved actual guard substring. These were reviewer checker assumptions, not candidate defects.'],'runtime_observations':0,'proven_demo_event_chains':0,'reference_programs_executed':0,'static_vectors_executed':0,'status':'PASS' if all(x['result']=='PASS' for x in checks) else 'FAIL'}
Path('/tmp/r-b01-independent-validation.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':output['status'],'checks':len(checks),'failed':[x for x in checks if x['result']=='FAIL']},ensure_ascii=False,indent=2))
