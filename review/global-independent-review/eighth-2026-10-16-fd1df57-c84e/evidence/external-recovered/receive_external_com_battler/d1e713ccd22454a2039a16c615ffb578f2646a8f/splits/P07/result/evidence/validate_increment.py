"""Validate only receiver-group-3 result artifacts. No source/game execution."""
import hashlib,json,subprocess
from pathlib import Path
REPO=Path(__file__).resolve().parents[9]
REL=Path('review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/receive_external_com_battler/splits')
BASE=REPO/REL; IDS=['P07','P08','P09','P10']; FIXED='02c8206651676effe40ff9a33dbb70998b79c1b1'
OUT=BASE/'P07/result/evidence/increment-validation.json'
def git(*args):return subprocess.check_output(['git','-C',str(REPO),*args])
def get(p):return json.loads(p.read_text())
assert (REPO/'AGENTS.md').is_file(),REPO
counts={};children=set();reverse=set();payload=[]
for sid in IDS:
 d=get(BASE/sid/'readset.json');p=BASE/sid/'result';f=get(p/'frozen-denominator.json');r=get(p/'reception-ledger.json');i=get(p/'interfaces.json')
 assert f['user_fixed_contract']==FIXED
 assert f['source_child_ids']==d['primary_child_ids'] and f['assigned_reverse_child_ids']==d['assigned_reverse_child_ids']
 assert len(set(d['primary_child_ids']))==len(d['primary_child_ids']) and len(set(d['assigned_reverse_child_ids']))==len(d['assigned_reverse_child_ids'])
 assert not(children&set(d['primary_child_ids'])) and not(reverse&set(d['assigned_reverse_child_ids']))
 children.update(d['primary_child_ids']);reverse.update(d['assigned_reverse_child_ids'])
 assert [c['original'] for c in r['compounds']]==d['primary_compounds']
 originals={x['id']:x for c in d['primary_compounds'] for x in c['children']}
 assert {x['id'] for x in r['source_children']}==set(originals)
 for x in r['source_children']:
  assert x['original']==originals[x['id']] and x['receiver_rationale'] and x['source_not_runtime']=='NOT_EXECUTED'
  assert x['original_assertion_changed'] is False
 originals_r={x['id']:x for g in d['complete_required_formal_group_objects'] for x in g['subassertions'] if x['id'] in d['assigned_reverse_child_ids']}
 assert {x['id'] for x in r['assigned_reverse_children']}==set(originals_r)
 for x in r['assigned_reverse_children']:
  assert x['original']==originals_r[x['id']] and x['receiver_rationale']
 assert len({x['receiver_rationale'] for x in r['source_children']})==len(r['source_children'])
 expected=[x for x in d['full_interfaces']['interfaces'] if set(x['local_compound_ids'])&set(f['compound_ids'])]
 assert [x['original'] for x in i['interfaces']]==expected
 for x in i['interfaces']:
  assert set(x['receiver_local_compound_ids'])==set(x['original']['local_compound_ids'])&set(f['compound_ids'])
  assert x['parent_interface_status']=='OPEN_FOR_OTHER_PRODUCERS_AND_PARENT_JOIN'
 assert r['new_required']==[] and r['new_optional']==[] and not r['unresolved_local_semantic_objects']
 assert r['execution']=='NOT_EXECUTED' and r['global_task_final']=='NOT_SIGNED'
 for name in ['frozen-denominator.json','reading-ledger.json','reception-ledger.json','interfaces.json','proposal-counters.json','report.md']:
  assert (p/name).is_file()
  if name.endswith('.json'): get(p/name)
 counts[sid]=f['denominator']
 for file in sorted(p.rglob('*')):
  if not file.is_file() or file==OUT or file.name=='publication.json':continue
  b=file.read_bytes()
  if file.suffix=='.json':json.loads(b)
  payload.append({'path':str(file.relative_to(REPO)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()})
assert len(children)==183 and len(reverse)==36 and sum(c['compounds'] for c in counts.values())==27
shared=BASE/'P07/result/evidence';a=get(shared/'actual-reading-evidence.json');m=get(shared/'necessary-consumers.json')
assert len(a['mandatory_units'])==31 and all(x['actual_text_equal_local_fixed_object'] for x in a['mandatory_units'])
assert len(m['objects'])==13 and m['additional_mandatory_context']['id']=='RX-HANDLER'
assert get(shared/'original-interface-context.json')['original']==get(BASE/'P07/readset.json')['full_interfaces']
assert len(get(shared/'reused-target-input-identities.json'))==10
nav=get(shared/'identity-navigation-reading.json');assert len(nav['rows'])==184 and nav['reversible_join_equal_all_184_original_objects']
restored=[]
for row,path in zip(nav['rows'],nav['path_purpose_rows']):
 eid,g,blob,n,sha,lines,local=row;rr,cc,tt,mode=nav['groups'][g];assert eid==path['evidence_id']
 x=dict(repo=rr,commit=cc,workspace_tree=tt,path=path['path'],blob=blob,git_mode=mode,bytes=n,sha256=sha,line_count=lines,evidence_id=eid,purpose=path['purpose'])
 if local!='ABSENT':x['local_bytes_equal_frozen_object']=local
 restored.append(x)
assert restored==get(BASE/'P07/readset.json')['full_identity_index']['files']
assert a['runtime_executions']==0
# The starting tree was clean. Every current delta must stay in one authorized result/.
changed=set(git('diff','--name-only',FIXED).decode().splitlines())|set(git('ls-files','--others','--exclude-standard').decode().splitlines())
allowed=[str(REL/s/'result')+'/' for s in IDS]
assert changed and all(any(x.startswith(prefix) for prefix in allowed) for x in changed),changed
assert git('rev-parse','--abbrev-ref','HEAD').decode().strip()=='codex/r8-battler-reception-group-3-20261016'
report={'schema':'r8-g3-increment-validation/v1','result':'PASS','fixed_contract':FIXED,'per_split':counts,'union':{'compounds':27,'source_children':183,'assigned_reverse_children':36,'primary_source_files':4,'primary_source_lines':1778},'checks':['All original compound/child/reverse values equal fixed readset objects','183 source and 36 reverse IDs complete, unique and pairwise disjoint','183 distinct receiver rationales and 36 assigned reverse rationales present','All locally applicable interface objects and local intersections retained','13 bounded required consumers plus mandatory Handler, 31 exact-unit equality checks','All JSON parsed; all six required deliverables present per split','Only four authorized result/ directories changed; exact exclusive branch checked','No source/game/legacy script executed; no formal/source changes'], 'payload_manifest_excluding_this_receipt_and_publication':payload,'execution':'MECHANICAL_OWN_INCREMENT_ONLY','business_execution':'NOT_EXECUTED','global_acceptance':'NOT_SIGNED'}
OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result':'PASS','payload_files':len(payload),'split_counts':counts,'changed_paths':len(changed),'business_execution':'NOT_EXECUTED'},ensure_ascii=False))
