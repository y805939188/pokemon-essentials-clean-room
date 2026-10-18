#!/usr/bin/env python3
"""Exhaustive mechanical original-pointer/value/identity verification; no source behavior."""
from pathlib import Path
import collections,datetime,gzip,hashlib,json,re
OUT=Path(__file__).resolve().parent;RR=OUT.parents[2]
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def load(n):return json.loads((OUT/n).read_bytes())
def put(n,d):
 with (OUT/n).open('w') as f:json.dump(d,f,ensure_ascii=False,separators=(',',':'));f.write('\n')
def resolve(d,p):
 for k in p.split('/')[1:]:
  k=k.replace('~1','/').replace('~0','~');d=d[int(k)] if isinstance(d,list) else d[k]
 return d
idx=load('index.json');inp=load('inputs.json');val=load('validation.json')
fixed={}
for kind,name in [('reference','reference-inventory.json'),('formal','formal-inventory.json')]:
 for x in json.loads((RR/'tasks/inventory_denominator'/name).read_bytes()):fixed[(kind,x['path'])]=x
assert len(idx['rows'])==563 and len({(x['kind'],x['path']) for x in idx['rows']})==563
for x in idx['rows']:
 f=fixed[(x['kind'],x['path'])]
 for k,v in x['fixed_identity'].items():assert v==f[k],(x['path'],k)
 assert x['semantic_PASS'] is None and x['individual_FULL_granted'] is False
assert sum('resource_root_guard'in x for x in idx['rows'])==18

input_checks=[];drift=[]
for rec in inp['inputs']:
 p=RR/rec['path'];raw=p.read_bytes() if p.exists() else b''
 matches=len(raw)==rec['bytes'] and sha(raw)==rec['sha256']
 x={'path':rec['path'],'matches_current_bytes_SHA':matches,'expected_sha256':rec['sha256'],'actual_sha256':sha(raw),'expected_bytes':rec['bytes'],'actual_bytes':len(raw)}
 if not matches:drift.append(x)
 input_checks.append(x)
allowed_registry_history={x['sha256'] for x in inp.get('registry_snapshot_chain',[]) if x['role']=='BUILDER_SNAPSHOT'}
unresolved_drift=[x for x in drift if not (x['path']=='adjudication/root-primary-task-final-registry.v1.json' and x['expected_sha256'] in allowed_registry_history)]
drift_paths={x['path'] for x in unresolved_drift}

with gzip.open(OUT/'candidate-details.json.gz','rt',encoding='utf-8') as f:detail=json.load(f)
by=collections.defaultdict(list)
for i,row in enumerate(detail['rows']):
 assert (row['kind'],row['path'])==(idx['rows'][i]['kind'],idx['rows'][i]['path'])
 for c in row['candidate_groups']:by[c['artifact']].append((row,c))
joins=load('nested-ledger-joins.json')['joins']
for c in joins:by[c['artifact']].append((c,c))
checks=collections.Counter();errors=[]
def same_path(v,path,kind):
 if not isinstance(v,str):return False
 if v==path:return True
 for base in ['/workspace/pokemon-essentials/','/workspace/pokemon-essentials-clean-room/','/workspace/pokemon-essentials-clean-room/reference/pokemon-essentials/']:
  if v.startswith(base):v=v[len(base):];break
 if v.startswith('./'):v=v[2:]
 if v.split('#',1)[0]==path:return True
 return bool(re.fullmatch(re.escape(path)+r':L?\d+(?:[-–]\d+)?',v))
for artifact,entries in by.items():
 if artifact in drift_paths:
  checks['groups_preserved_but_current_input_drift_unknown']+=len(entries);continue
 try:d=json.loads((RR/artifact).read_bytes())
 except Exception as e:errors.append({'artifact':artifact,'error':str(e)});continue
 for row,c in entries:
  for p in c['path_pointers']:
   try:
    v=resolve(d,p);assert same_path(v,row['path'],row['kind']),(v,row['path']);checks['exact_original_path_pointers']+=1
   except Exception as e:errors.append({'artifact':artifact,'pointer':p,'type':'PATH','error':str(e)})
  for name in ['reader_fields_original','status_fields_original','range_and_qualification_fields_original','identity_fields_original']:
   for x in c.get(name,[]):
    try:
     v=resolve(d,x['pointer'])
     if x.get('value')=='NOT_INLINED_SEE_EXACT_ORIGINAL_POINTER':
      raw=json.dumps(v,ensure_ascii=False,separators=(',',':'));assert len(raw.encode())==x['original_value_json_bytes'];checks['large_original_pointer_only_fields']+=1
     else:assert v==x['value'];checks['exact_original_'+name]+=1
    except Exception as e:errors.append({'artifact':artifact,'pointer':x['pointer'],'type':name,'error':str(e)})
  checks['candidate_detail_groups']+=1

def expand(s):
 yield from s['exact']
 for p in s['indexed_runs']:
  for a,b in p['inclusive_index_runs']:
   for i in range(a,b+1):yield p['prefix']+str(i)+p['suffix']
artifactmap={x['id']:x['path'] for x in idx['artifacts']}
for i,row in enumerate(idx['rows']):
 rawgroups=detail['rows'][i]['candidate_groups']
 for c in row['candidate_groups']:
  artifact=artifactmap[c['artifact_id']];sel=c['exact_detail']
  if sel['artifact']=='nested-ledger-joins.json':matched=[x for x in joins if x['kind']==row['kind'] and x['path']==row['path'] and x['artifact']==artifact]
  else:matched=[x for x in rawgroups if x['artifact']==artifact and x['pointer_kind_only']==c['pointer_kind_only']]
  assert matched,(row['path'],artifact,c['pointer_kind_only'])
  checks['exact_compact_detail_selectors']+=1
  if 'path_pointer_set'in c:
   expected={p for x in matched for p in x['path_pointers']}
   actual=set(expand(c['path_pointer_set']));assert actual==expected
   checks['lossless_compact_path_pointer_sets']+=1
  for task in c['root_receipt_tasks']:assert inp['root_receipts'][task]['exact_current_match']

# Preserve the original330-file COM-MOVE final manifest exactly; no new main-file edits are permitted.
manifest=RR/'tasks/com_move/exact-manifest.current.json';m=json.loads(manifest.read_bytes())
def member_rows(v):
 if isinstance(v,dict):
  if 'path'in v and 'bytes'in v and 'sha256'in v:yield v
  for x in v.values():yield from member_rows(x)
 elif isinstance(v,list):
  for x in v:yield from member_rows(x)
old=[]
for r in member_rows(m):
 p=Path(r['path']);attempts=[p] if p.is_absolute() else [RR/'tasks/com_move'/p,RR/p]
 p=next((x for x in attempts if x.exists()),None)
 if p is None:errors.append({'type':'OLD_MANIFEST_PATH','path':r['path']});continue
 raw=p.read_bytes();ok=len(raw)==r['bytes'] and sha(raw)==r['sha256'];old.append({'path':r['path'],'matches':ok})
 if not ok:errors.append({'type':'OLD_MANIFEST_CHANGED','path':r['path']})

out={'schema':'gr8-mechanical-membership-final-verification/v1','start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':0 if not errors else 1,'fixed_R':432,'fixed_F':131,'unique_paths':563,'binary_guard':18,'builder_registry':val['registry_entries'],'current_finish_registry':val['current_registry_entries'],'current_receipts_exact':val['current_exact_receipts'],'input_identity_checks':len(input_checks),'historical_registry_snapshot_drift_preserved':len(drift)-len(unresolved_drift),'unresolved_current_input_drift':unresolved_drift,'pointer_checks':dict(checks),'errors':errors,'old_COM_MOVE_manifest_identity':{'bytes':manifest.stat().st_size,'sha256':sha(manifest.read_bytes())},'old_COM_MOVE_manifest_members_checked':len(old),'old_COM_MOVE_all_members_unchanged':all(x['matches'] for x in old),'new_contexts':0,'new_votes':0,'new_semantic_reading_credit':0,'business_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
put('mechanical-verification.json',out);put('input-currentness.json',{'checks':input_checks,'drift_qualification':'Recorded22registry snapshot is historical;23 successor separately bound. Other drift is UNKNOWN and never source reading/semantic credit.'})
if unresolved_drift:
 for row in idx['rows']:
  for c in row['candidate_groups']:
   if artifactmap[c['artifact_id']] in drift_paths:c['current_input_drift_qualification']='OLD_RECORDED_IDENTITY_DOES_NOT_MATCH_CURRENT_INPUT; POINTER_CANDIDATE_UNKNOWN_UNTIL_RECOVERED'
 put('index.json',idx)
val['mechanical_final_verification']='mechanical-verification.json';val['mechanical_final_errors']=len(errors);val['unresolved_current_input_drift']=len(unresolved_drift);val['old_330_manifest_members_unchanged']=all(x['matches'] for x in old);put('validation.json',val)
print(json.dumps(out,ensure_ascii=False))
assert not errors,errors[:3]

