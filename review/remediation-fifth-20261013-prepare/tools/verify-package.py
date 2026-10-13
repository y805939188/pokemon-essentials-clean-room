#!/usr/bin/env python3
"""Offline, bounded checks of the frozen dispatch contracts and package identities."""
import collections, hashlib, json, re, subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[1];repo=root.parents[1]
def read(p):return json.loads((root/p).read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
checks={};errors=[]
def check(name,value):checks[name]=bool(value);errors.extend([] if value else [name])
m=read('frozen-input/cloud-fifth-update-handoff-manifest.json');plan=m['batch_plan'];batches=plan['batches'];owners={x['path']:x for x in m['shared_owners']['files']}; ledger=read('registration/initial-ledger.json');dispatch=read('dispatch.json')
packets={b['id']:read('contracts/'+b['id']+'/task-packet.json') for b in batches}
fs=[f for b in batches for f in packets[b['id']]['findings']]
check('92_unique_required',len(fs)==len({f['id'] for f in fs})==92 and all(f['disposition']=='required' for f in fs))
check('51_P2_41_P3',collections.Counter(f['severity'] for f in fs)=={'P2':51,'P3':41})
check('unique_ID_batch_and_exact_permissions',all(set(b['finding_ids'])=={f['id'] for f in packets[b['id']]['findings']} and all(f['batch_owner']==b['id'] for f in packets[b['id']]['findings']) for b in batches))
check('85_unique_path_owners_21_shared',len(owners)==85 and sum(x['writer']=='R5-I' for x in owners.values())==21)
check('semantic_writers_correct',all(all(owners[p]['writer']==b['id'] for p in b['direct_writer_files']) and all(owners[p]['writer']=='R5-I' for p in b['shared_fragments_for_single_writer']) for b in batches))
check('candidate_prefixes_disjoint',len({read('contracts/'+b['id']+'/contract.json')['author_live_write_allowlist'][0] for b in batches})==8)
check('all_individual_contract_fields_preserved',all(all(k in f for k in ['preconditions','minimal_counterexample','normal_case','failure_or_boundary_case','acceptance_criteria','source_anchors','spec_anchors','history_links','review_resolution']) for f in fs))
check('each_ID_has_precise_write_permission',all(f['id'] in plan['finding_file_permissions'] and bool(plan['finding_file_permissions'][f['id']]) for f in fs))
check('ledger_OPEN92_stage_counts_zero',len(ledger['findings'])==92 and all(x['status']=='OPEN_REQUIRED' and not any(x[k] for k in ['candidate_PASS','actual_bytes_PASS','formal_accepted','final_CLOSED']) for x in ledger['findings']))
check('role_slots_unassigned_and_echo_unverified',all(not x['assigned'] and x['real_task_id'] is None and x['actual_echo']=='UNVERIFIED' for x in read('registration/role-slots.json')))
check('seven_author_ready_and_seven_reviewers_wait_candidate',dispatch['author_slots_ready']==7 and dispatch['candidate_reviewer_slots']==7 and dispatch['candidate_verdicts_ready']==0)
q=read('registration/quarantined-scope.json');check('7_optional_7_no_required_6_policies',collections.Counter(f['disposition'] for f in q['findings'])=={'optional':7,'no_required_revision':7} and len(q['policy']['decisions'])==6)
# Exact immutable full-record equality against structured canonical payload, if original available locally.
original={f['id']:f for f in read('frozen-input/findings.json')['findings']};check('all_92_full_records_exact',all(f==original[f['id']] for f in fs))
indeg={b['id']:0 for b in batches}; adj={k:[] for k in indeg}
for a,b in plan['dependency_edges']:indeg[b]+=1;adj[a].append(b)
queue=[k for k,v in indeg.items() if v==0];order=[]
while queue:
 a=queue.pop(0);order.append(a)
 for b in adj[a]:
  indeg[b]-=1
  if indeg[b]==0:queue.append(b)
check('18_dependency_edges_acyclic',len(plan['dependency_edges'])==18 and len(order)==8)
r=read('verification/full-structural-reading.json');raw=(root/'frozen-input/cloud-fifth-update-handoff-prompt.md').read_bytes();last=0
for s in r['segments']:
 check('chunk_identity_'+str(s['byte_start']),s['byte_start']==last and sha(raw[s['byte_start']:s['byte_end_exclusive']])==s['sha256']);last=s['byte_end_exclusive']
check('whole_handoff_covered_without_gaps',last==len(raw)==2293718 and len([s for s in r['segments'] if re.match(r'^### GR5-',s['title'])])==106)
check('13_named_limits',len(re.findall(r'^\| L\d\d ',(root/'frozen-input/limits-and-missing-materials.md').read_text(),re.M))==13)
# Local package links: output future directories are code spans, never fake deliverables.
broken=[]
for p in root.rglob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if target.startswith(('http:','https:','#')):continue
  if not (p.parent/target.split('#')[0]).exists():broken.append(str(p.relative_to(root))+':'+target)
check('all_local_navigation_links_resolve',not broken)
# Frozen manifest excludes itself, this validation result, and post-commit publication proof.
manifest=root/'packet-manifest.json'
if manifest.exists():
 for row in read('packet-manifest.json')['files']:
  p=root/row['path'];b=p.read_bytes();check('packet_identity_'+row['path'],len(b)==row['bytes'] and sha(b)==row['sha256'] and hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_blob'])
# Current formal subtree must remain B5 during preparation; no source code is executed.
formal=subprocess.check_output(['git','rev-parse','HEAD:deliverables/final-specification-set'],cwd=repo).decode().strip()
check('preparation_formal_tree_B5',formal==m['formal_baseline']['formal_tree'])
result={'schema':'r5.package-validation.v1','passed':not errors,'checks':{k:v for k,v in checks.items() if not k.startswith(('chunk_identity_','packet_identity_'))},'bounded_chunk_identity_checks':sum(k.startswith('chunk_identity_') for k in checks),'packet_identity_checks':sum(k.startswith('packet_identity_') for k in checks),'errors':errors,'broken_links':broken,'topological_order':order,'evidence_level':'TOOL_VALIDATION','new_behavior_execution':0}
print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(0 if result['passed'] else 1)
