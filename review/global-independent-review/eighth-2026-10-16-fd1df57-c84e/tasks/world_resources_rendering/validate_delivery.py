import json,hashlib,datetime,subprocess
from pathlib import Path
D=Path(__file__).parent;R=Path('/workspace/pokemon-essentials');C=Path('/workspace/pokemon-essentials-clean-room')
start=datetime.datetime.now(datetime.timezone.utc).isoformat();errors=[];checks=[];commands=[]
def get(p):return json.loads((D/p).read_text())
def ck(name,condition,detail=None):
 checks.append({'check':name,'passed':bool(condition),'detail':detail})
 if not condition:errors.append(name)
def cmd(repo,argv):
 t=datetime.datetime.now(datetime.timezone.utc).isoformat();q=subprocess.run(argv,cwd=repo,text=True,capture_output=True)
 commands.append({'argv':argv,'cwd':str(repo),'start_utc':t,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'underlying_exit':q.returncode,'stdout':q.stdout,'stderr':q.stderr});return q
for n in ['progress.json','identities.json','reading-ledger.json','forward-mapping.json','reverse-mapping.json','interfaces.json','proposals.json','review.md']:ck('deliverable_exists:'+n,(D/n).is_file())
ident=get('identities.json');led=get('reading-ledger.json');f=get('forward-mapping.json');v=get('reverse-mapping.json');body=get('body-reverse-mapping.json')
for x in get('frozen-v1/manifest.json')['files']:
 b=(D/x['path']).read_bytes();ck('frozen_sha:'+x['path'],len(b)==x['bytes'] and hashlib.sha256(b).hexdigest()==x['sha256'] and (D/x['frozen_path']).read_bytes()==b)
ck('primary_28R4F_full',led['primary_reference_full']==28 and led['primary_formal_full']==4 and led['primary_partial']==led['primary_unread']==0)
ck('catalog_complete_205',len(v['vectors'])==205 and not v['pending_vectors'])
ck('catalog_atoms_unique_822',len({a['id'] for x in v['vectors'] for a in x['assertions']})==822)
ck('body_693_plus_data288',sum(len(x['atomic_assertions']) for x in body['clauses'])==693 and body['separate_data_atoms']==288)
ck('source_1282',sum(len(x['assertions']) for x in f['units'])+get('weather-shared-facts.json')['atomic_fact_count']==1282)
ck('source_ids_unique',len({a['id'] for x in f['units'] for a in x['assertions']})==sum(len(x['assertions']) for x in f['units']))
known={x['unit_id'] for x in f['units']}
known.update(x['unit_id'] for x in get('world-facts.received.json')['objects'])
known.update(x['id'] for x in get('ui-facts.received.json')['objects'])
aliases={'WRR-WEATHER':'weather-shared-facts.json','UI-EVO-LAST-BACK-01':'evolution-last-back.received.json'}
known.update(aliases)
missing=sorted({s for x in v['vectors'] for s in x['source_units'] if s not in known})
ck('vector_source_refs_resolve',not missing,missing)
bmissing=sorted({s for x in body['clauses'] for s in x['source_units'] if s not in known})
ck('body_source_refs_resolve',not bmissing,bmissing)
ck('identity_problems_empty',not ident['identity_problems'])
bad_ranges=[{'path':x['path'],'range':[a,b],'file_end':x['complete_file_lines']} for x in led['files'] for a,b in x['continuous_read_ranges'] if not (1<=a<=b<=x['complete_file_lines'])]
ck('actual_read_ranges_within_file',not bad_ranges,bad_ranges)
ck('all_actual_frozen_blobs_match',all(x.get('matches_git_blob') is True for x in ident['files']))
ck('business_not_executed',get('progress.json')['business_execution']=='NOT_EXECUTED' and get('proposals.json')['candidate_count']==0)
q=cmd(R,['git','rev-parse','HEAD']);ck('R_head_frozen',q.returncode==0 and q.stdout.strip()==ident['R'])
q=cmd(R,['git','diff','--exit-code',ident['R'],'--']);ck('R_tracked_unchanged',q.returncode==0)
q=cmd(C,['git','diff','--exit-code',ident['B8'],'--','deliverables/final-specification-set']);ck('formal_tracked_unchanged',q.returncode==0)
q=cmd(C,['git','rev-parse','HEAD:deliverables/final-specification-set']);ck('current_report_formal_tree_frozen',q.returncode==0 and q.stdout.strip()==ident['formal_tree'])
ck('evolution_snapshot_sha',hashlib.sha256((D/'evolution-last-back.received.json').read_bytes()).hexdigest()=='310b5936448a2060e632e0ed87d8694b7dbe308f01934f12028a6d3c70a984d0')
(D/'mapping-resolution.json').write_text(json.dumps({'aliases':aliases,'known_source_unit_count':len(known),'qualification':'Identity/navigation resolution only, not semantic proof; peer facts retain original reviewer and qualifications.'},ensure_ascii=False,indent=2)+'\n')
end=datetime.datetime.now(datetime.timezone.utc).isoformat()
o={'kind':'STATIC_DELIVERY_VALIDATION_ONLY','start_utc':start,'end_utc':end,'checks':checks,'commands':commands,'errors':errors,'result':'PASS_STATIC_DELIVERY_CHECKS' if not errors else 'FAILED_STATIC_DELIVERY_CHECKS','business_execution':'NOT_EXECUTED','reference_behavior_runs':0,'model_behavior_runs':0,'host_runs':0}
(D/'final-validation.json').write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result':o['result'],'errors':errors,'checks':len(checks),'end_utc':end}))
raise SystemExit(1 if errors else 0)
