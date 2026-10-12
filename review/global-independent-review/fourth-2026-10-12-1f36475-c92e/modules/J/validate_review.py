"""Artifact integrity/anchor validation only; never executes reference mechanics."""
import pathlib,json,collections,datetime
H=pathlib.Path(__file__).resolve().parent
ROOT=H.parents[4]; SHARED=H.parents[1]
SRC=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
load=lambda p:json.loads(p.read_text())
errors=[]; checks=[]
def check(ok,label):
 checks.append({'check':label,'passed':bool(ok)})
 if not ok:errors.append(label)
required=['report.md','junctions.json','shared-capabilities.json','findings.json','execution.json','progress.md']
check(all((H/x).is_file() and (H/x).stat().st_size for x in required),'six required nonempty artifacts')
j=load(H/'junctions.json'); f=load(H/'findings.json'); e=load(H/'execution.json'); sc=load(H/'shared-capabilities.json')
check(all(x['schema_version']=='1.0' for x in [j,f,e,sc]),'schema version 1.0')
check([x['id'] for x in j['records']]==[f'GR4-J{i:02d}' for i in range(1,15)],'14 stable consecutive junction IDs')
check(all(r['status'] in {'supported','partial','missing','unresolved','not_reviewed'} for r in j['records']),'junction status enumeration')
required_fields=['producers','state_writes','consumers','preconditions','configuration','reviewed','not_reviewed','material_availability','source_anchors','spec_anchors','conclusion','historical_junction_ids']
check(all(all(r.get(k) for k in required_fields) for r in j['records']),'all chains have producer/state/consumer/scope/material/anchors')
check(all(set(r['boundaries'])=={'normal','failure','cancellation','repetition','ordering'} for r in j['records']),'normal/failure/cancel/repeat/order boundaries in every chain')
check(all(r['execution_status']=='NOT_EXECUTED' and all(v['status']=='NOT_EXECUTED' for v in r['vectors']) for r in j['records']),'all behavior and vectors NOT_EXECUTED')
formal={x['path'] for x in load(ROOT/'delivery/2026-10-12/formal-identities.json')['records']}
reads=load(H/'read-log.json'); cover=collections.defaultdict(set)
for x in reads:
 for a,b in x['ranges']:cover[(x['kind'],x['path'])].update(range(a,b+1))
anchors=0
for r in j['records']:
 for kind,key in [('source','source_anchors'),('spec','spec_anchors')]:
  for a in r[key]:
   anchors+=1
   p=(SRC if kind=='source' else ROOT)/a['path']; ok=p.is_file()
   if not ok:errors.append(f'{r["id"]}: missing anchor {a["path"]}');continue
   n=len(p.read_text().splitlines())
   if kind=='spec' and a['path'] not in formal:errors.append(f'{r["id"]}: spec not formal131')
   for lo,hi in a['line_ranges']:
    if not 1<=lo<=hi<=n:errors.append(f'{r["id"]}: bad range {a["path"]}:{lo}-{hi}')
    if set(range(lo,hi+1))-cover[(kind,a['path'])]:errors.append(f'{r["id"]}: range not covered by bounded read log {a["path"]}:{lo}-{hi}')
check(not [x for x in errors if 'anchor' in x or 'range' in x or 'formal131' in x],f'{anchors} source/spec anchors exist, in bounds, directly read; specs in formal131')
nav=load(SHARED/'evidence/junction-navigation.json')['records']; hist=j['historical_coverage']
check(len(hist)==80 and [x['id'] for x in hist]==[x['id'] for x in nav],'54+8+18 exact history navigation ID/order retained')
check(all(x['retained_normal_scope']==y['normal'] and x['retained_failure_and_boundary_scope']==y['failure_and_boundary'] and x['original_identity']==y['original_identity'] and x['original_pointer']==y['original_pointer'] and x['original_object_sha256']==y['original_object_sha256'] and x['accepted_successor_binding']==y['accepted_successor_binding'] for x,y in zip(hist,nav)),'history exact qualified text and immutable bindings preserved')
check(all(x['status']=='not_reviewed' and x['does_not_promote_whole_historical_scope'] for x in hist),'no historical whole-row fresh PASS')
check(not f['findings'] and f['new_substantive_findings_count']==0,'no new findings or allocated GR4-J-001')
frozen={x['path'] for x in load(SHARED/'tasks/J-input-identities.json')['files']}
for link in f['existing_finding_links']:
 mod=link['id'].split('-')[1]; path=f'modules/{mod}/findings.json'
 check(path in frozen and mod!='M11',f'{link["id"]} comes from sealed input, not M11')
 if path in frozen:check(link['id'] in {x['id'] for x in load(SHARED/path)['findings']},f'{link["id"]} exists; linked not recounted')
check(e['thread_id']==load(SHARED/'tasks/J-launch.json')['thread_id'] and e['actual_model_echo']=='UNVERIFIED','launch thread preserved and actual model UNVERIFIED')
check(all(v=='NOT_EXECUTED' for v in e['execution'].values()),'no implied reference execution')
ce=load(H/'candidate-counterevidence.json')
check(ce['scope_file_count']==131 and set(ce['scope_files'])==formal and ce['result']=='REJECTED_ALREADY_SUPPORTED_IN_B','candidate full131 counterevidence rejected; no false new absence claim')
check(all(isinstance(x['main_identity']['single_primary_owner'],str) and x['main_identity']['single_primary_owner'] in formal for x in sc['records']),'each shared capability has one formal primary owner')
check(len({x['id'] for x in sc['records']})==len(sc['records']),'shared IDs unique')
check(j['records'][3]['legacy_control_projection']['id']=='GIR-FD82-A053' and j['records'][3]['legacy_control_projection']['status']=='supported','A053 only bounded hatching projection retained')
result={'schema_version':'1.0','kind':'TOOL_VALIDATION','status':'PASS' if not errors else 'FAIL','checks':checks,'errors':errors,'record_counts':dict(collections.Counter(r['status'] for r in j['records'])),'source_spec_anchor_count':anchors,'shared_capability_count':len(sc['records']),'historical_record_count':len(hist),'behavioral_execution':'NOT_EXECUTED','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'limitation':'Structure, anchor readability/read-log coverage and bindings only; no semantic proof by this script and no mechanics execution.'}
(H/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['checks']},ensure_ascii=False))
if errors:raise SystemExit(1)
