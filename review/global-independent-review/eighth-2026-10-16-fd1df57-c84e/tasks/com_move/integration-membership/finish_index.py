#!/usr/bin/env python3
"""Compact mechanical member navigation and add exact original nested-ledger joins."""
from pathlib import Path
import collections,datetime,hashlib,json,re,gzip
OUT=Path(__file__).resolve().parent;RR=OUT.parents[2]
def sha(b):return hashlib.sha256(b).hexdigest()
def get(n):return json.loads((OUT/n).read_bytes())
def put(n,d):
 with (OUT/n).open('w') as f:json.dump(d,f,ensure_ascii=False,separators=(',',':'));f.write('\n')
idx=get('index.json');inp=get('inputs.json');val=get('validation.json');un=get('unmatched.json')
newjoins=[]
def original(n,role='ORIGINAL_NESTED_LEDGER_JOIN_METADATA_ONLY'):
 p=RR/n;raw=p.read_bytes();rec={'path':n,'bytes':len(raw),'sha256':sha(raw),'roles':[role]}
 old=next((x for x in inp['inputs'] if x['path']==n),None)
 if old:
  assert old['sha256']==rec['sha256'] and old['bytes']==rec['bytes']
  if role not in old['roles']:old['roles'].append(role)
 else:inp['inputs'].append(rec)
 return json.loads(raw)

# Current successor registry is an additional observed input; preserve prior22 snapshot identity.
regpath=RR/'adjudication/root-primary-task-final-registry.v1.json';regraw=regpath.read_bytes();currentreg=json.loads(regraw)
inp['registry_snapshot_chain']=[{'sha256':inp['registry_snapshot_sha256'],'count':val['registry_entries'],'role':'BUILDER_SNAPSHOT'},{'sha256':sha(regraw),'bytes':len(regraw),'count':len(currentreg['accepted']),'role':'CURRENT_FINISH_SUCCESSOR','observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}]
if sha(regraw)!=inp['registry_snapshot_sha256']:inp['inputs'].append({'path':str(regpath.relative_to(RR)),'bytes':len(regraw),'sha256':sha(regraw),'roles':['CURRENT_REGISTRY_SUCCESSOR_IDENTITY'],'observation_revision':'FINISH_SUCCESSOR'})
for i,x in enumerate(currentreg['accepted']):
 p=RR/x['receipt']['path'];raw=p.read_bytes();assert len(raw)==x['receipt']['bytes'] and sha(raw)==x['receipt']['sha256']
 inp['root_receipts'][x['task']]={'registry_pointer':'/accepted/'+str(i),'expected':x['receipt'],'exact_current_match':True,'status_original':x['status'],'registry_revision':'CURRENT_FINISH_SUCCESSOR'}
 original(x['receipt']['path'],'EXACT_CURRENT_FINISH_ROOT_TASK_RECEIPT')
val['current_registry_entries']=len(currentreg['accepted']);val['current_exact_receipts']=len(currentreg['accepted']);val['current_registry_sha256']=sha(regraw)
def match_id(identity,fixed):
 checks=[]
 for k,f in [('bytes','bytes'),('sha256','sha256'),('blob','git_blob'),('git_blob','git_blob'),('commit','commit')]:
  if k in identity:checks.append(identity[k]==fixed[f])
 return bool(checks) and all(checks)
def rawfield(p,v):return {'pointer':p,'value':v}
rows={(r['kind'],r['path']):r for r in idx['rows']}
def receipt(task):
 x=inp['root_receipts'][task]
 assert x['exact_current_match']
 return {'task':task,'registry_pointer':x['registry_pointer'],'receipt_path':x['expected']['path'],'inputs_pointer':'/root_receipts/'+task,'exact_current_match':True}
def addjoin(row,c):
 row['candidate_groups'].append(c);row['mapping_status']='EXPLICIT_READING_ENTRY_AND_CURRENT_TASK_RECEIPT_CANDIDATE';newjoins.append({'kind':row['kind'],'path':row['path'],**c})
cb=original('tasks/creature_b/reading-ledger.json')
for i,x in enumerate(cb['initial']):
 ident=x['identity'];key=(ident.get('group'),ident['path'])
 if key not in rows:continue
 row=rows[key]
 assert match_id(ident,row['fixed_identity'])
 rp='/initial/'+str(i)
 fields=[rawfield(rp+'/identity/read_status',ident['read_status']),rawfield(rp+'/own_full_read',x['own_full_read']),rawfield(rp+'/semantic_disposition',x['semantic_disposition'])]
 ranges=[rawfield(rp+'/continuous_displays/'+str(j)+'/range',op['range']) for j,op in enumerate(x['continuous_displays'])]
 addjoin(row,{'artifact':'tasks/creature_b/reading-ledger.json','pointer_kind_only':'EXPLICIT_NESTED_PATH_READING_ENTRY_CANDIDATE','path_pointers':[rp+'/identity/path'],'reader_fields_original':[rawfield(rp+'/reviewer',x['reviewer'])],'status_fields_original':fields,'range_and_qualification_fields_original':ranges,'exact_current_root_receipts':[receipt('creature_b')],'qualification':'Original nested identity.read_status and complete continuous_displays; no FULL inheritance from task-final. Root CRE-B receipt scope and mandatory false/nil/mail companion remain applicable.','local_identity_statuses_original_candidates':['EXPLICIT_LOCAL_VALUES_MATCH']})

# UI root receipt explicitly accepts original 7R/6F minigame team; bind the exact original provider ledger through parent reception.
ur=original('tasks/ui_full/minigames-reception.json')
um=original('tasks/ui_minigames/reading-ledger.json')
for b in ur['bindings']:
 if b.get('relative_path') in ['identities.json','reading-ledger.json','forward-mapping.json','reverse-mapping.json']:
  p=Path(b['path']);raw=p.read_bytes();assert len(raw)==b['bytes'] and sha(raw)==b['sha256']
  original(str(p.relative_to(RR)),'EXACT_PARENT_MINIGAME_RECEIPT_BOUND_METADATA_ONLY')
ui=original('tasks/ui_full/reading-ledger.v3.json')
peerpaths={x['identity_path'] for x in ui['records'] if x.get('peer_reader')=='/root/ui_minigames'}
for i,x in enumerate(um['full_read_payloads']):
 if x['path'] not in peerpaths:continue
 kind='formal' if x['path'].startswith('deliverables/') else 'reference'
 row=rows[(kind,x['path'])];rp='/full_read_payloads/'+str(i)
 addjoin(row,{'artifact':'tasks/ui_minigames/reading-ledger.json','pointer_kind_only':'EXPLICIT_ORIGINAL_TEAM_READING_ENTRY_CANDIDATE','path_pointers':[rp+'/path'],'reader_fields_original':[rawfield('/reader',um['reader'])],'status_fields_original':[rawfield(rp+'/read_status',x['read_status'])],'range_and_qualification_fields_original':[rawfield(rp+'/read_ranges',x['read_ranges']),rawfield(rp+'/unread_ranges',x['unread_ranges'])],'exact_current_root_receipts':[receipt('ui_full')],'original_parent_binding':{'artifact':'tasks/ui_full/minigames-reception.json','pointer':'/bindings','parent_ledger':'tasks/ui_full/reading-ledger.v3.json','peer_reader_value':'/root/ui_minigames','root_receipt_scope_pointer':'/accepted_primary/actual_minigame_team_F'},'qualification':'Original actual provider source/formal FULL remains /root/ui_minigames; parent owns finite meaning reception, not provider FULL transfer. Exact parent-bound ledger/identities/forward/reverse hashes checked.','local_identity_statuses_original_candidates':['EXACT_PARENT_BOUND_LEDGER_IDENTITY_CANDIDATE']})

if 'reference_metadata' in inp['root_receipts']:
 rm=original('tasks/reference_metadata_completion/reading-ledger.json')
 for n in ['identities.json','forward-mapping.json','reverse-mapping.json','completion-manifest.json']:original('tasks/reference_metadata_completion/'+n)
 for i,x in enumerate(rm['files']):
  row=rows[('reference',x['path'])];assert x['identity_sha256']==row['fixed_identity']['sha256'];rp='/files/'+str(i)
  addjoin(row,{'artifact':'tasks/reference_metadata_completion/reading-ledger.json','pointer_kind_only':'EXPLICIT_METADATA_RECOVERY_READING_ENTRY_CANDIDATE','path_pointers':[rp+'/path'],'reader_fields_original':[rawfield(rp+'/actual_reader',x['actual_reader'])],'status_fields_original':[rawfield(rp+'/status',x['status'])],'range_and_qualification_fields_original':[rawfield(rp+'/read_intervals',x['read_intervals']),rawfield(rp+'/unread_intervals',x['unread_intervals']),rawfield(rp+'/purpose',x['purpose'])],'exact_current_root_receipts':[receipt('reference_metadata')],'qualification':'New actual metadata recovery actor, original failed launcher unchanged. Exact current23 receipt with typed-purpose qualifications; no game/runtime contract or parent FULL transfer.','local_identity_statuses_original_candidates':['EXPLICIT_LOCAL_SHA_MATCH']})

# New mandatory companion is bound by exact parent-provided identity only, without new semantic reception.
q='adjudication/mandatory-creb-item-false-nil-and-mail-consumer-qualification.v1.json'
raw=(RR/q).read_bytes();assert len(raw)==6198 and sha(raw)=='5971c3a621d8032f7b4f5dfb5ad739994a2110a003b3aa58884d84c13d0f74ef'
original(q,'PARENT_MANDATORY_CRE_B_COMPANION_IDENTITY_ONLY_NO_NEW_SEMANTIC_RECEIPT')
put('nested-ledger-joins.json',{'schema':'gr8-original-nested-ledger-membership-joins/v1','scope':'Mechanical exact original field/pointer/hash joins only;0new source reading/independent votes.','joins':newjoins,'mandatory_companion':q})

# Keep complete first-stage candidate detail archive plus exact supplementary joins, avoiding redundant identities in index.
artifact_ids={p:'A'+str(i+1).zfill(4) for i,p in enumerate(sorted({c['artifact'] for r in idx['rows'] for c in r['candidate_groups']}))}
artifact_table=[{'id':a,'path':p,'input_identity_pointer':'/inputs/'+str(next(i for i,x in enumerate(inp['inputs']) if x['path']==p))} for p,a in artifact_ids.items()]
def values(cs):
 out={}
 for x in cs:
  v=x.get('value','NOT_INLINED_SEE_EXACT_ORIGINAL_POINTER');out[json.dumps(v,ensure_ascii=False,sort_keys=True)]=v
 return list(out.values())
for ri,row in enumerate(idx['rows']):
 compact=[]
 for c in row['candidate_groups']:
  artifact=c['artifact'];typ=c['pointer_kind_only'];nested=typ.startswith('EXPLICIT_')
  # Main compact file points to a complete lossless original-pointer archive or precise supplementary join.
  detail={'artifact':'nested-ledger-joins.json','exact_path_and_artifact_filter':{'kind':row['kind'],'path':row['path'],'artifact':artifact}} if typ in ['EXPLICIT_NESTED_PATH_READING_ENTRY_CANDIDATE','EXPLICIT_ORIGINAL_TEAM_READING_ENTRY_CANDIDATE','EXPLICIT_METADATA_RECOVERY_READING_ENTRY_CANDIDATE'] else {'artifact':'candidate-details.json.gz','row_pointer':'/rows/'+str(ri),'exact_candidate_property_filter':{'artifact':artifact,'pointer_kind_only':typ}}
  z={'artifact_id':artifact_ids[artifact],'pointer_kind_only':typ,'exact_detail':detail,'reader_values_original':values(c.get('reader_fields_original',[])),'status_values_original':values(c.get('status_fields_original',[])),'root_receipt_tasks':[x['task'] for x in c.get('exact_current_root_receipts',[])],'identity_statuses_original_candidates':c.get('local_identity_statuses_original_candidates',[])}
  if nested:
   z['path_pointer_set']=c.get('path_pointer_set',{'exact':c.get('path_pointers',[]),'indexed_runs':[]})
   z['reader_fields_original']=c.get('reader_fields_original',[]);z['status_fields_original']=c.get('status_fields_original',[]);z['range_and_qualification_fields_original']=c.get('range_and_qualification_fields_original',[])
  compact.append(z)
 row['candidate_groups']=compact
 row['semantic_PASS']=None;row['individual_FULL_granted']=False

metadata=original('delegation/readsets/reference_metadata.json','ORIGINAL_FIVE_METADATA_PRIMARY_MEMBERSHIP_ONLY')
metadata_paths=set()
def paths(v):
 if isinstance(v,dict):
  if v.get('path') in {r['path'] for r in idx['rows']}:metadata_paths.add(v['path'])
  for x in v.values():paths(x)
 elif isinstance(v,list):
  for x in v:paths(x)
paths(metadata)
assert len(metadata_paths)==5
guard=[]
for row in idx['rows']:
 reasons=[]
 if row['mapping_status']!='EXPLICIT_READING_ENTRY_AND_CURRENT_TASK_RECEIPT_CANDIDATE':reasons.append('NO_SUCH_EXPLICIT_READING_ENTRY_AND_CURRENT_RECEIPT_CANDIDATE')
 if row['kind']=='reference' and row['path'] in metadata_paths:
  row['primary_scope_guard']='Original reference_metadata launcher failed/no actual output, unchanged. Distinct new /root/reference_metadata_completion recovery and exact current23 receipt bound separately; original root/source reader credit remains its real actor.'
  if 'reference_metadata' not in inp['root_receipts']:reasons.append('REFERENCE_METADATA_CURRENT_PRIMARY_RECOVERY_RECEIPT_PENDING')
 if 'parent_requested_primary_qualification' in row:reasons.append('FORMAL_SHARED_ORIGINAL_WHOLE_READING_EXISTS_CURRENT_TASK_FINAL_NOT_SIGNED')
 if reasons:guard.append({'kind':row['kind'],'path':row['path'],'reasons':reasons,'disposition':'EXACT_CURRENT_PRIMARY_MAPPING_UNKNOWN_NOT_MATERIAL_LIMIT'})
idx['schema']='gr8-fixed-path-evidence-pointer-candidates/v3';idx['artifacts']=artifact_table
idx['detail_resolution']='Exact original JSON pointers are retained in candidate-details.json.gz and supplementary nested-ledger-joins.json. Main file groups exact pointer candidates only; original fields and qualifications are never promoted to semantic PASS or individual FULL.'
idx['root_receipts_input']='inputs.json#/root_receipts'
put('index.json',idx);put('inputs.json',inp);put('unmatched.json',{'schema':'gr8-mechanical-unmatched-current-primary/v3','rows':guard,'qualification':'Mechanical/current-primary qualification gaps only; does not negate original actual reading or claim semantic failure.'})
val.update({'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'input_artifacts':len(inp['inputs']),'supplementary_nested_joins':len(newjoins),'unmatched_paths':len(guard),'unmatched_kind_counts':dict(collections.Counter(x['kind'] for x in guard)),'compact_artifacts':len(artifact_table),'all_563_fixed_paths_retained':len(idx['rows'])==563,'primary_metadata_missing_receipt_guarded':len(metadata_paths)==5,'new_contexts':0,'new_votes':0,'new_semantic_reading_credit':0,'business_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True})
put('validation.json',val)
report=f'''# 固定路径证据指针候选表\n\n仅整合现有结构化字段；新增 context、独立票、语义阅读信用均为 0。固定 R432/F131 共 563 个唯一路径；当前 registry{len(currentreg['accepted'])} 份收据已按 bytes/SHA 精确核对，先前22构建快照身份另保留。此表不冻结全局分母、不签全局、不授语义 PASS 或个人 FULL。\n\n`index.json` 逐路径指向原 reader 字段、原 FULL/PARTIAL/finite/byte-association 状态及范围、原输入身份、候选 root task-final 收据。完整原始 JSON 指针/字段保存在 `candidate-details.json.gz`；`nested-ledger-joins.json` 补 CRE-B 嵌套连续读账、UI 真正 minigame reader 及 metadata 实际新恢复者的精确原绑定，未把原团队 FULL 转为父个人 FULL。目录、manifest、mapper作者、行政身份和原文件读账分开；路径出现或标签不构成批准。\n\n`unmatched.json` 目前 {len(guard)} 个具名路径。3 个 shared formal 保原 root451行全文信用和18有限组/3OPEN接口/task-final未签资格；5 metadata 已绑定第23份实际恢复收据，原 FAILED launcher 未改。其它可用具名原读账未因整外域未签自动算缺读；各外域整体正式批准仍留 root。所有缺映射保 UNKNOWN，未改为 material limit。\n\n18 个原 binary 均附 root 可读 resource 收据与真实原读者/可读总体/opaque native 边界指针，仅保实际可读程序、字段及有限机器码窗口，不声称全 binary/machinecode FULL。旧历史、原 inventory UNREAD 和当前事实同时保真；forward/reverse 行数不作原子分母。\n\n`inputs.json` 为输入 bytes/SHA 及收据/绑定；`links.json` 为字面导航；`three-shared-formal-priority.json` 为父专项核查；`validation.json` 与最终机械检查记录成员及指针验证。5 个 `.json` 原投影实际含多 JSON 对象的 schema 不匹配保原异常，不作为材料 limit 或语义失败。\n\n业务 NOT_EXECUTED；UPDATE_NOT_STARTED。实际 model/effort/tier/speed/Fast/UUID 均 UNVERIFIED。原 COM-MOVE 330 清单和所有已签主件未改；本次只写 integration-membership。\n'''
(OUT/'report.md').write_text(report)
print(json.dumps({'paths':len(idx['rows']),'current_receipts':val['exact_current_receipts'],'unmatched':guard,'nested_joins':len(newjoins),'compact_index_bytes':(OUT/'index.json').stat().st_size},ensure_ascii=False))

