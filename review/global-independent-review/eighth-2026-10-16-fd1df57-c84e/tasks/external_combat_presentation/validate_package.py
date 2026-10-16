"""Mechanical integrity validation. It never supplies semantic review credit."""
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

HERE=Path(__file__).resolve().parent
SPEC=Path('/workspace/pokemon-essentials-clean-room')
REF=Path('/workspace/pokemon-essentials')
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
B='fd1df570cad987dc3852a3b958f03916e317f7fe'
I='30cfed0996003b6ebf4b5c51cc04f31ca9255440'
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def git(repo,*args):return subprocess.check_output(['git',*args],cwd=repo)
errors=[]
required=['progress.json','identities.json','reading-ledger.json','forward-mapping.json','reverse-mapping.json','interfaces.json','proposals.json','review.md']
for p in required:
    if not (HERE/p).is_file():errors.append('missing '+p)
json_files=[]
for p in sorted(HERE.rglob('*.json')):
    if '.git' in p.parts:continue
    json.loads(p.read_text());json_files.append(str(p.relative_to(HERE)))
ledger=json.loads((HERE/'reading-ledger.json').read_text())
checked=[]
for f in ledger['primary']+ledger['dependency']:
    repo=Path(f['repo']);frozen=git(repo,'show',f['commit']+':'+f['path']);actual=(repo/f['path']).read_bytes()
    if actual!=frozen or sha(frozen)!=f['sha256'] or len(frozen)!=f['bytes']:errors.append('identity '+f['path'])
    if git(repo,'rev-parse',f['commit']+':'+f['path']).decode().strip()!=f['git_blob']:errors.append('blob '+f['path'])
    if f['semantic_status']=='FULL_READ':
        seen=set()
        for a,b in f['read_intervals']:seen.update(range(a,b+1))
        if not set(range(1,len(frozen.splitlines())+1)).issubset(seen):errors.append('read interval '+f['path'])
    checked.append({'path':f['path'],'sha256':sha(frozen),'bytes':len(frozen),'matches_frozen':actual==frozen})
base='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/'
copies={
 'combat_presentation.md':'delegation/prompts/combat_presentation.md',
 'combat_presentation.json':'delegation/readsets/combat_presentation.json',
 'combat_review.json':'delegation/readsets/combat_review.json',
 'ui_full.json':'delegation/readsets/ui_full.json',
 'eighth-global-review-prompt.md':'inputs/eighth-global-review-prompt.md',
 'review-SKILL.md':'inputs/review-SKILL.md'}
copy_results=[]
for name,path in copies.items():
    a=(HERE/'inputs'/name).read_bytes();b=git(SPEC,'show',I+':'+base+path)
    copy_results.append({'copy':'inputs/'+name,'fixed_path':base+path,'bytes':len(a),'sha256':sha(a),'exact_bytes':a==b})
    if a!=b:errors.append('input copy '+name)
facts=json.loads((HERE/'forward-mapping.json').read_text())['facts'];ids={x['id'] for x in facts}
for row in json.loads((HERE/'reverse-mapping.json').read_text())['clauses']:
    for key in row['source_groups']:
        if key not in ids:errors.append('unknown source '+key)
if len(facts)!=79:errors.append('source group count')
atomic=json.loads((HERE/'atomic-assertions.json').read_text())
field_ids=[]; field_count=0; scalar_count=0
for name,count,width in [('release-variance-fields',16,14),('capture-variance-fields',16,17)]:
    table=json.loads((HERE/(name+'.json')).read_text())
    if len(table['records'])!=count:errors.append('table rows '+name)
    for row in table['records']:
        if len(row['fields'])!=width or [f['index'] for f in row['fields']]!=list(range(width)):errors.append('table fields '+name)
        for f in row['fields']:
            field_ids.append(f['id']);field_count+=1;scalar_count+=f['scalar_leaves']
            if not f['consumer_range'] or not f['formal_disposition']:errors.append('unmapped table field '+f['id'])
color=json.loads((HERE/'ball-color-fields.json').read_text())
if len(color['records'])!=16:errors.append('color rows')
field_ids.extend(x['id'] for x in color['records'])
manual_ids=[a['id'] for a in atomic['assertions']]
all_assertion_ids=manual_ids+field_ids
if len(set(all_assertion_ids))!=len(all_assertion_ids):errors.append('duplicate assertion identity')
if len(all_assertion_ids)!=atomic['atomic_assertion_denominator'] or len(all_assertion_ids)!=1045:errors.append('atomic assertion count')
if field_count!=496 or scalar_count!=1200:errors.append('finite table denominator')
for f in facts:
    own=[a['id'] for a in atomic['assertions'] if a['group']==f['id']]
    if not own or own!=f['atomic_assertion_ids']:errors.append('source atomic binding '+f['id'])
for a in atomic['assertions']:
    if a['group'] not in ids or not a['premise'] or not a['consumer'] or not a['formal_links']:errors.append('incomplete assertion '+a['id'])
reverse=json.loads((HERE/'reverse-mapping.json').read_text())
if reverse['primary_formal_files']!=0 or reverse['atomic_clause_denominator']!=0:errors.append('primary formal denominator')
if len(reverse['selected_interface_assertions'])!=20:errors.append('selected interface count')
contribution=json.loads((HERE/'bounded-contributions.json').read_text())
provider=json.loads(git(SPEC,'show',I+':review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/world_resources_rendering/forward-mapping.json'))
for row in contribution['payloads']:
    if row!=next(x for x in provider['units'] if x['unit_id']==row['unit_id']):errors.append('provider binding '+row['unit_id'])
if sum(len(x['assertions']) for x in contribution['payloads'])!=66:errors.append('provider bounded denominator')
for f in ledger['primary']:
    covered=[]
    for u in f['units']:covered.extend(range(u['range'][0],u['range'][1]+1))
    if covered!=list(range(1,f['lines']+1)):errors.append('noncontiguous structures '+f['path'])
limits='review/remediation-sixth-20261014-prepare/inputs/limit-records.json'
original=git(SPEC,'show','9aa72bc99a4cf52c8fb9cad8a637a963341388b0:'+limits)
current=git(SPEC,'show',B+':'+limits)
limit_result={'original_commit':'9aa72bc99a4cf52c8fb9cad8a637a963341388b0','B8':B,'path':limits,'original_sha256':sha(original),'B8_sha256':sha(current),'same_bytes':original==current,'full_records_read':14,'inherited_semantic_pass':False}
refs_before=git(REF,'status','--porcelain=v1','--untracked-files=all').decode()
if refs_before:errors.append('reference dirty')
allowed=str(HERE.relative_to(SPEC))+'/'
changed=set(git(SPEC,'diff','--name-only',I).decode().splitlines())
changed.update(git(SPEC,'ls-files','--others','--exclude-standard').decode().splitlines())
outside=sorted(p for p in changed if not p.startswith(allowed))
if outside:errors.append('write set violation '+str(outside))
result={'start_utc':started,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mechanical_integrity':'PASS' if not errors else 'FAIL',
        'semantic_review_pass':False,'errors':errors,'required_files':required,'json_files':json_files,'verified_read_file_identities':checked,
        'input_copies':copy_results,'R6_limit_identity':limit_result,'reference_status':refs_before,
        'write_set_checked':allowed,'outside_write_set':outside,
        'mapping_checks':{'primary_groups':len(facts),'manual_assertions':len(manual_ids),'typed_fields':len(field_ids),'assertions':len(all_assertion_ids),'table_scalar_leaves':scalar_count,'color_scalar_leaves':48,'selected_reverse_interfaces':20,'bounded_provider_assertions':66},
        'behavior_executions':{'reference':0,'independent_model':0,'full_host':0,'native_media':0,'save_replay':0},'behavior_status':'NOT_EXECUTED'}
(HERE/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'mechanical_integrity':result['mechanical_integrity'],'errors':errors,'verified_read_files':len(checked),'copied_inputs':len(copy_results),'semantic_review_pass':False},ensure_ascii=False))
raise SystemExit(bool(errors))
