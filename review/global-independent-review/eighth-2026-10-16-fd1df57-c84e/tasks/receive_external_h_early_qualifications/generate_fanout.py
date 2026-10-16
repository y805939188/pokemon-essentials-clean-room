"""Freeze complete finite reception contracts; generated views grant no reading credit."""
from pathlib import Path
import json,gzip,hashlib,datetime,re,subprocess,collections,copy
T=Path(__file__).resolve().parent; F=T/'delegation/fanout-v1'; ROOT=T.parents[1]; REPO=T.parents[4]
BASE='ab44ee8c5ffd53ded7d5bc37ae6f15e6ed3ba8d8'; TARGET='11c057d9aed330c16312470f80f13d180f8e1e65'; B8='fd1df570cad987dc3852a3b958f03916e317f7fe'; R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
AUTHOR='01a143b2-fc07-7339-ab2f-055dba6bc023'; UTC=datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(x):return (json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def write(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def pointer(x,p):
 for k in p.split('/')[1:]:
  k=k.replace('~1','/').replace('~0','~');x=x[int(k)]if isinstance(x,list)else x[k]
 return x
def esc(k):return str(k).replace('~','~0').replace('/','~1')
H=json.loads((T/'.transport/originals/tasks/R7-H12/earlier-round-qualification-full.json').read_text()); D=H['R5']['original_and_current_percheck_value_dictionary']; RECORDS=H['R5']['current_root']['records']
ORIGINALS=json.loads((F/'evidence/original-r5-input-identities.json').read_text())['files']; ORIGINAL_BY_KEY={}
for x in ORIGINALS:
 raw=gzip.decompress((T/x['transport']['path']).read_bytes());ORIGINAL_BY_KEY[(x['original']['commit'],x['original']['path'])]=json.loads(raw)
parts=[{'id':'early_r1_r4','title':'R1–R4完整历史资格与执行限定','range':None,'history':['EH-HISTORY-01','EH-HISTORY-02','EH-HISTORY-03','EH-HISTORY-04','EH-HISTORY-09'],'extra':'R1全部100trace/113input、83authority用途、5勘误/9纠正/8阶段；R2全部229原控制资格/21批/341贡献及308/33范围；R3全部23/76及两排除；R4全部17/76、B5 16/75+partial和完整Summary有限后继；H05执行限定。'},
 {'id':'r5_u01_u02','title':'R5-U01/U02完整48合同与294检查','range':(0,48),'history':['EH-HISTORY-05(所分配48项贡献)'],'extra':'R5-U01的34项与U02的14项；原事实、反例、410native中的本域条件、294原schema及当前/接受绑定全部保留。'},
 {'id':'r5_u03_u06_core','title':'R5-U03/U04/U05及U06主体32合同与196检查','range':(48,80),'history':['EH-HISTORY-05(所分配32项贡献)','EH-HISTORY-07','EH-HISTORY-08(动作/显示事实，不独签aggregate)','EH-HISTORY-12(本域接口)'],'extra':'U03全部11、U04全部7、U05的1项、U06前13项。包含U03旧FAIL/有限后继及Summary/Party/瓶子/消费的完整必要定义与消费者。'},
 {'id':'r5_tail_shared_policy','title':'R5尾部12合同/78检查及共享资格、非必修和政策','range':(80,92),'history':['EH-HISTORY-05(全局资格+本域12项)','EH-HISTORY-06','EH-HISTORY-08(aggregate阶段)','EH-HISTORY-10','EH-HISTORY-11','EH-HISTORY-12(本域接口)'],'extra':'U06剩余5项M11及U07全部7项；原14非必修、13limit、6policy、M11-005 facets；R5 shared21/dependency18/solewriters85/contributions262与6行政/3纠正、唯一激活及原失败/后继资格。全局逐事实握手等待对应producer收据，不等待无关范围。'}]
owner={r['id']:p['id']for p in parts if p['range']for r in RECORDS[slice(*p['range'])]};assert len(owner)==92
# One availability catalogue, not a mandatory full-system review list.
indexes=[]
for repo,c,prefix,kind in [(Path('/workspace/pokemon-essentials'),R,'','R_AVAILABLE_CONTEXT'),(REPO,B8,'deliverables/final-specification-set','B8_FORMAL_AVAILABLE_CONTEXT')]:
 listing=subprocess.check_output(['git','-C',str(repo),'ls-tree','-r','-z',c]+(['--',prefix]if prefix else[]));files=[]
 for row in listing.split(b'\0'):
  if not row:continue
  meta,path=row.split(b'\t',1);mode,typ,oid=meta.decode().split();path=path.decode()
  if typ!='blob':continue
  b=subprocess.check_output(['git','-C',str(repo),'cat-file','blob',oid]);files.append({'path':path,'mode':mode,'git_blob':oid,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
 indexes.append({'repository':str(repo),'commit':c,'type':kind,'files':files,'purpose':'可用性/完整文件身份索引；只有本任务事实要求的完整定义/调用者/条款进入实质读集，不因此全审432或131。','semantic_credit':0})
indexb=dump({'schema':'gr8.h-early-fanout.availability-index/v1','indexes':indexes});indexz=gzip.compress(indexb,mtime=0);(F/'shared/available-R-B8-files.json.gz').write_bytes(indexz)
# Proof-backed common vocabulary and all field-purpose rules, not a leaf-value denominator.
common={'schema':'gr8.h-early-fanout.common-premises/v1','fixed':{'contract':'40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232','previous_reception':BASE,'target':TARGET,'target_tree':'2fcef25ee9903bd7e28dec21f6fc2d970c221f77','target_task_tree':'bb0cb15506d2abc9e6b84abe1391048776de6997','B8':B8,'R':R},'semantic_unit_definition':'主单位为有完整前提/事实/普通与失败/取消/部分提交/验收/保留范围/消费者的历史控制合同、criterion、共享接口事实、非必修记录或政策记录。V/N去重值与180833行政叶只作恢复/关联，不作验收人口。','complete_record_rule':'每个主单位完整字段及值须读取；所有七组/八节、反向条款、参数/default/枚举、案例预期与必要接口不能删成locator。可无损合并完全同值且用途/语境确同的字段，精确关联保留。','pure_identity_rule':'commit/tree/path/blob/mode/bytes/SHA、传输压缩别名、无业务值的结构索引可按完整类型/用途处置并机械核全集合；不要求逐个hash字符串人工阅读或增加新criterion。带事实/例子/状态/接受资格的值仍是业务意义。','dictionary_rule':'expanded记录只递归解析原R5字典的精确D引用，保存raw记录、源指针与所有绑定。解析/生成信用0；同值别名的不同上下文不能自动签。','routing_rule':'不得仅因键名original_actual_text/source_bindings/lines/label或old_*就自动行政化。有当前有效业务意义须完整读取或给精确同值接收；无关旧底层正文按原有限用途路由，不无界重审。','state_rule':'owner接受、candidate/actual PASS、正式ACCEPTED、关闭候选、唯一激活各自绑定；旧FAIL/WAIT/MISMATCH保留原时点；不重开第七轮27或借旧PASS免本轮接收。','source_rule':'先完整定义/方法结束行和条件，再必要caller/receiver及B8完整相关条款；无默认caller不豁免定义，也不自动成为未来必备API；未接producer不能整签consumer。','execution_rule':'本任务行为初始NOT_EXECUTED/新增0；只做必要惰性恢复/静态核验，禁止盲跑恢复旧脚本或游戏；材料/宿主限制与可得未读分开。','independence_rule':'真实不同于目标原作者'+AUTHOR+'；角色名/任务号/续turn不创造独立性，实际参数无权威回显逐项UNVERIFIED。不得自行spawn。','mandatory_clarifiers':['shared/mandatory-policy-clarifier.v1.json','source previous reception findings.json#RECEPTION-H-EARLY-EVIDENCE-001','source previous reception evidence/historical-five-identities.json(新身份，原UNVERIFIED保留)'],'common_context_is_not_blanket_reception':True,'UPDATE_NOT_STARTED':True}
write(F/'common-premises.json',common)
fullglobal=(T/'contract/eighth-global-review-prompt.md').read_text(); agents=(T/'contract/AGENTS.md').read_text();skill=(T/'contract/review-SKILL.md').read_text();parent=(T/'contract/receive_external_h_early_qualifications.md').read_text()
base_prefix=str(T.relative_to(REPO))
oldpayloadrows=json.loads((T/'evidence/original-recovery.json').read_text())['files']
common_paths=['report.md','reception-ledger.json','interfaces.json','findings.json','evidence/historical-five-identities.json','inputs/target/report.md','inputs/target/completion-scope.json','inputs/target/unread.json','inputs/target/purpose-dispositions.json','inputs/target/history-current-acceptance-records.json','inputs/target/consumer-review.json','inputs/target/consumer-reads/manifest.json','inputs/target/semantic-atlas/association-transport.json','inputs/target/semantic-atlas/associations.json.gz','contract/receive_external_h_early_qualifications.complete.json']
def basefile(rel,purpose):
 b=subprocess.check_output(['git','show',BASE+':'+base_prefix+'/'+rel]);return {'carrier_commit':BASE,'repository':'y805939188/pokemon-essentials-clean-room','path':base_prefix+'/'+rel,'relative_to_previous_task':rel,'mode':'100644',**ident(b),'purpose':purpose}
def newfile(p,purpose):
 return {'carrier_commit_binding':'主线程实际派发的本合同包含commit(最终回显固定SHA)，禁止分支未来HEAD','path':str(p.relative_to(REPO)),'relative_to_fanout':str(p.relative_to(F))if p.is_relative_to(F)else None,'relative_to_task':str(p.relative_to(T)),'mode':'100644',**ident(p.read_bytes()),'purpose':purpose}
# Shared field grammar is context only; full owned records carry every field and value.
binding_files=['semantic-atlas/schema-unit-bindings.txt','semantic-atlas/nested-reason-bindings.txt','semantic-atlas/semantic-context-schema.txt']
for p in parts:
 pid=p['id'];S=F/'shards'/pid;S.mkdir(parents=True,exist_ok=True);ids=[]if p['range']is None else [r['id']for r in RECORDS[slice(*p['range'])]];wanted=set(ids); bindings=[];usedD=set()
 def expand(x,srcptr,stack=()):
  if isinstance(x,str)and x in D:
   assert x not in stack;usedD.add(x);bindings.append({'occurrence':srcptr,'dictionary_pointer':'/R5/original_and_current_percheck_value_dictionary/'+x,'original_reference':x,'resolved_value_sha256':ident(dump(D[x]))['sha256']});return expand(D[x],srcptr,stack+(x,))
  if isinstance(x,dict):return {k:expand(v,srcptr+'/'+esc(k),stack)for k,v in x.items()}
  if isinstance(x,list):return [expand(v,srcptr+'/'+str(i),stack)for i,v in enumerate(x)]
  return x
 units=[]
 if not ids:
  for k in ['R1','R2','R3_R4']:
   v=H[k];units.append({'source_logical_path':'tasks/R7-H12/earlier-round-qualification-full.json','pointer':'/'+k,'raw_complete_object':v,'expanded_complete_object':v})
  other={k:v for k,v in H.items()if k not in ('R1','R2','R3_R4','R5','preserved_special_history')};units.append({'source_logical_path':'tasks/R7-H12/earlier-round-qualification-full.json','pointer':'/ (non-R5 remaining root fields)','raw_complete_object':other,'expanded_complete_object':other})
 else:
  for i,r in enumerate(RECORDS):
   if r['id']not in wanted:continue
   ptr='/R5/current_root/records/'+str(i);units.append({'primary_id':r['id'],'source_logical_path':'tasks/R7-H12/earlier-round-qualification-full.json','pointer':ptr,'raw_complete_object':r,'expanded_complete_object':expand(r,ptr)})
  for key,rs in [('full_scope_records',H['R5']['full_scope_records']),('root_original_scope0_3',H['R5']['root_original_scope0_3']),('original_scope_and_check_reads/scope/records',H['R5']['original_scope_and_check_reads']['scope']['records']),('original_scope_and_check_reads/checks/records',H['R5']['original_scope_and_check_reads']['checks']['records'])]:
   for i,r in enumerate(rs):
    if r.get('id')not in wanted:continue
    ptr='/R5/'+key+'/'+str(i);units.append({'primary_id':r['id'],'source_logical_path':'tasks/R7-H12/earlier-round-qualification-full.json','pointer':ptr,'raw_complete_object':r,'expanded_complete_object':expand(r,ptr)})
  # Complete original task-packet finding and original criterion object, without field whitelists.
  for r in RECORDS:
   if r['id']not in wanted:continue
   refs=[('original_packet_finding',r['scope_source'])]+[('original_criterion',u['original_source'])for u in r['schema_units']]
   for role,ref in refs:
    raw=ORIGINAL_BY_KEY[(ref['commit'],ref['path'])];v=pointer(raw,ref['pointer']);units.append({'primary_id':r['id'],'role':role,'source_commit':ref['commit'],'source_path':ref['path'],'pointer':ref['pointer'],'raw_complete_object':v,'expanded_complete_object':v})
 if ids:
  needed_original_keys={(u['source_commit'],u['source_path'])for u in units if 'source_commit'in u and 'source_path'in u}
  if pid=='r5_tail_shared_policy':needed_original_keys|={k for k in ORIGINAL_BY_KEY if '/R5-U08/'in k[1] or '/registration/'in k[1]}
  for key in sorted(needed_original_keys):
   origin=ORIGINAL_BY_KEY[key]
   if isinstance(origin,dict):
    context={k:v for k,v in origin.items()if k not in ('findings','criteria','records')}
    units.append({'role':'COMPLETE_ORIGINAL_HEADER_COUNTERCHAIN_EVIDENCE_POOL_CONTEXT_NOT_SECOND_PRIMARY','source_commit':key[0],'source_path':key[1],'pointer':'/ (complete fields except primary findings/criteria/records already selected)','raw_complete_object':context,'expanded_complete_object':context})
 if pid=='r5_tail_shared_policy':
  globalfields={k:v for k,v in H['R5']['current_root'].items()if k!='records'};units.append({'role':'global_R5_qualified_state_and_receptions','source_logical_path':'tasks/R7-H12/earlier-round-qualification-full.json','pointer':'/R5/current_root (excluding records; primary records uniquely owned)','raw_complete_object':globalfields,'expanded_complete_object':globalfields})
  extra={'scope_check_task_and_reading_qualifications':{k:{kk:vv for kk,vv in v.items()if kk!='records'}if isinstance(v,dict)else v for k,v in H['R5']['original_scope_and_check_reads'].items()},'source_input_identities':H['R5']['scope_input_identities'],'preserved_special_history':H['preserved_special_history']};units.append({'role':'global_qualification_history_and_nonmandatory','raw_complete_object':extra,'expanded_complete_object':extra})
 # Selected exact field bindings and full record selectors are proof locators, not more criteria.
 ownbind=[]
 for rel in binding_files:
  lines=(T/'inputs/target'/rel).read_text().splitlines(True)
  for i,line in enumerate(lines,1):
   matches=re.findall(r'(?:GR5-)?((?:M\d{2}|JXN)-\d{3})',line);mentioned={('GR5-'+m)for m in matches};primary=next((owner[x]for x in sorted(mentioned)if x in owner),None)
   if (primary==pid)or(pid=='r5_tail_shared_policy'and not primary):ownbind.append({'file':rel,'line':i,'exact_text':line,'role':'complete_binding_or_structure_context_not_new_criterion','mentions':sorted(mentioned)})
 view={'schema':'gr8.h-early-fanout.complete-record-view/v1','id':pid,'credit':'NO_READING_CREDIT_FROM_GENERATION','primary_R5_ids':ids,'owned_complete_objects':units,'dictionary_bindings':bindings,'dictionary_entries_for_own_occurrences':{k:D[k]for k in sorted(usedD)},'assigned_binding_context':ownbind,'all_fields_retained':True,'scope':p['extra']}
 raw=dump(view);z=gzip.compress(raw,mtime=0);vp=S/'complete-records.json.gz';vp.write_bytes(z)
 extra_paths=[]
 if pid=='early_r1_r4':extra_paths=['inputs/target/purpose-field-view.json','inputs/target/purpose-field-associations.json','inputs/target/inputs/parent-reading-ledger.json']
 if pid=='r5_u03_u06_core':extra_paths=['inputs/target/originals/r5-u03-actual-fail.md','inputs/target/originals/r5-u03-limited.md','inputs/target/semantic-atlas/nested-reason-bindings.txt']
 if pid=='r5_tail_shared_policy':extra_paths=['inputs/target/originals/r5-u08-candidate-fail.md','inputs/target/originals/r5-u08-actual.md','inputs/target/originals/r5-u08-final.md','inputs/target/originals/sc-u07-001-erratum.json','inputs/target/originals/r5-quarantined-scope.json','inputs/target/originals/r5-limits-and-missing-materials.md','inputs/target/originals/r5-activation-receipt.json','inputs/target/activation-selector-validation.json','inputs/target/qualifier-projection.json','inputs/target/nonmandatory-reads/associations.json','inputs/target/nonmandatory-reads/anchor-semantic-addendum.txt','inputs/target/nonmandatory-reads/manifest.json','inputs/target/nonmandatory-reads/original-source.json','inputs/target/nonmandatory-reads/limits-source.json']+['inputs/target/nonmandatory-reads/chunk-%02d.txt'%i for i in range(1,8)]+['inputs/target/'+x for x in binding_files]
 payloads=[basefile(x,'当前有限接收/作者声明/精确身份上下文或本域完整原裁决；不是整个文件自动实读或验收人口')for x in common_paths+extra_paths]
 for x in oldpayloadrows:
  payloads.append(basefile(x['transport_local_path'],'精确原H载荷惰性gzip；本任务只读所分配完整对象，原解码身份必须核验')|{'decoded_identity':{k:x['input'][k]for k in ['bytes','sha256','git_blob']},'logical_path':x['input']['logical_path']})
 batches={r['current_scope_qualification']['batch']for r in RECORDS if r['id']in wanted}
 for x in ORIGINALS:
  path=x['original']['path'];include=any('/'+b+'/'in path for b in batches)or(pid=='r5_tail_shared_policy'and('/R5-U08/'in path or '/registration/'in path))
  if include:payloads.append(newfile(T/x['transport']['path'],'原始完整合同/criterion可恢复证据；按本任务ID精确指针读，非整批身份免审')|{'decoded_identity':x['decoded'],'original_identity':x['original']})
 for path in [F/'restore_fanout_inputs.py',F/'common-premises.json',F/'shared/mandatory-policy-clarifier.v1.json',F/'shared/policy6.exact.json',F/'shared/available-R-B8-files.json.gz',T/'evidence/followup-policy-review.json']:
  payloads.append(newfile(path,'共同前提/强制clarifier/恢复helper/可用性索引；可用性索引不扩成全系统必读')|({'decoded_identity':ident(indexb)}if path==F/'shared/available-R-B8-files.json.gz'else{}))
 payloads.append(newfile(vp,'无损完整对象视图，raw和expanded均可恢复；完整字段用途需实际阅读')|{'decoded_identity':ident(raw)})
 # Domain source/spec paths are exact frozen lookup candidates, never a closed whitelist.
 candidatepaths=set()
 def collect(x):
  if isinstance(x,str)and(x.startswith('Data/')or x.startswith('PBS/')or x.startswith('deliverables/final-specification-set/')):
   if '\n'not in x and len(x)<260:candidatepaths.add(x.split('#')[0])
  elif isinstance(x,dict):
   for v in x.values():collect(v)
  elif isinstance(x,list):
   for v in x:collect(v)
 for u in units:collect(u['expanded_complete_object'])
 candidates=[]
 for idx in indexes:
  for x in idx['files']:
   if x['path']in candidatepaths:candidates.append(dict(x,commit=idx['commit'],role='necessary_definition_consumer_candidate; actual complete ranges must be established'))
 semantic_sets=[]
 if pid=='early_r1_r4':
  for label,ptr,rows,idkey in [('R1 trace qualification','/R1/qualification/records',H['R1']['qualification']['records'],'record_id'),('R1 input purpose qualification','/R1/qualification/per_input_use_records',H['R1']['qualification']['per_input_use_records'],'id'),('R2 controls qualification','/R2/qualification/per_control',H['R2']['qualification']['per_control'],'id'),('R3/R4 original finite controls','/R3_R4/qualification/records',H['R3_R4']['qualification']['records'],'id')]:
   semantic_sets.append({'kind':label,'count':len(rows),'units':[{'id':r[idkey],'source_pointer':ptr+'/'+str(i),'complete_record_in_view':True}for i,r in enumerate(rows)],'population_is_not_new_finding_count':True})
  semantic_sets.extend([{'kind':'R1 identity errata','count':5,'source_pointer':'/R1/qualification/identity_errata'},{'kind':'R1 approval/import corrections','count':9,'source_pointer':'/R1/qualification/historical_approval_corrections'},{'kind':'R1 stage contracts','count':8,'source_pointer':'/R1/qualification/stage_contracts'},{'kind':'R3 excluded records','count':2,'source_pointer':'/R3_R4/qualification/excluded_R3'},{'kind':'R4 later Summary residue','source_pointer':'/R3_R4/qualification/later_summary_residue'},{'kind':'H05 execution qualifications','logical_sources':['tasks/R7-H05/execution-qualification.json','tasks/R7-H05/report.md'],'not_new_execution':True}])
 if pid=='r5_tail_shared_policy':
  semantic_sets=[{'kind':'R5 original nonmandatory records','count':14,'source':'inputs/target/originals/r5-quarantined-scope.json','unit_ids':[x['id']for x in json.loads((T/'inputs/target/completion-scope.json').read_text())['nonmandatory_original_dispositions']]},{'kind':'R5 historical limits','count':13,'unit_ids':['L%02d'%i for i in range(1,14)]},{'kind':'R5 compatibility policy records','count':6,'unit_ids':[x['id']for x in H['R5']['current_root']['policy6']['decisions']]},{'kind':'shared finite reception contracts','count':21,'units':[{'id':r['receipt_id'],'source_pointer':'/R5/current_root/shared21/receipts/'+str(i)}for i,r in enumerate(H['R5']['current_root']['shared21']['receipts'])]},{'kind':'dependency finite handshakes','count':18,'source_pointer':'/R5/current_root/dependency18/edges'},{'kind':'typed global writer/contribution/state purpose','population':'85writer paths,262contributions,6administrative,3corrections retain separate units; no new source behavior requirements','source_pointer':'/R5/current_root (global non-record fields)'}]
 criteria=[u['criterion_id']for r in RECORDS if r['id']in wanted for u in r['schema_units']]
 readset={'schema':'gr8.h-early-fanout.complete-readset/v1','id':pid,'utc':UTC,'immutable_source':common['fixed'],'original_author_actual_context':AUTHOR,'primary_semantic_population':{'other_complete_semantic_sets':semantic_sets,'R5_ids':ids,'R5_criteria':criteria,'R5_record_count':len(ids),'R5_criterion_count':len(criteria),'earlier_historical_population':p['extra']if not ids else None,'history_records_for_limited_reception':p['history'],'not_semantic_population':'V/N独有值、hash字符串、JSON叶、文件和绑定行不作为额外验收条件。'},'exact_payloads':payloads,'necessary_initial_R_B8_file_identities':candidates,'lookup_index_not_full_review':{'path':'shared/available-R-B8-files.json.gz','R_commit':R,'B8_commit':B8},'exclusive_write_set':base_prefix+'/receivers/fanout-v1/'+pid+'/','suggested_dedicated_output_branch':'codex/r8-h-early-'+pid.replace('_','-')+'-20261016','git_coordination':'本次协调线程保持原分支。新上下文由主线程实际派发；若共享工作树只写独占目录、由唯一整合写者commit/push，若隔离checkout由主线程在派发时采用上述专用分支。不得并发写同一Git索引、不得改main/tag或强推。','required_outputs':['progress.json','frozen-units.json','reading-ledger.json','reception-ledger.json','interfaces.json','findings.json','report.md','unreceived.json'],'counterproof_scope':'每个疑似缺口给最强已有覆盖/no-required/合理out-of-scope解释；提出者不能唯一作最终反证/根裁决；不擅自整改。','availability':'完整原始值均可按精确字节恢复，不能把可得未读写成limit；发现真实缺失具名继续其它独立部分。','all_payloads_hashable_without_self_commit':'新合同文件由本清单原始bytes/SHA/blob约束；其包含Git commit由父实际派发固定，不读分支未来HEAD。','UPDATE_NOT_STARTED':True}
 write(S/'readset.json',readset)
 header=f'''# 完整独立有限接收合同：{p['title']}

你是主线程实际新建或复用的真实非目标作者接收context；必须不同于目标作者 `{AUTHOR}`。不得自行spawn。当前协调线程没有启动本合同，你仅在主线程实际派发后执行。

唯一任务ID `{pid}`。冻结目标为 `{TARGET}`，checkout tree `2fcef25ee9903bd7e28dec21f6fc2d970c221f77`，任务tree `bb0cb15506d2abc9e6b84abe1391048776de6997`。原接收检查点 `{BASE}`；原始用户合同 `40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232`。实际派发消息必须给本合同的准确包含commit；缺这一外部固定绑定时仍可按下列固定源只读准备，不能改用同名分支未来HEAD。

先完整读本prompt（下文内含原接收prompt、完整全局prompt、AGENTS和skill）与同目录 `readset.json`，再读 `../../common-premises.json` 和强制 `../../shared/mandatory-policy-clarifier.v1.json`。其readset SHA256为 `{hashlib.sha256((S/'readset.json').read_bytes()).hexdigest()}`。恢复工具先全文读懂，只在自己的独占写集中新建无symlink隔离目标；旧脚本/游戏不运行。生成视图、解码、hash、exit0信用0。

## 本合同唯一实质范围

{p['extra']}

R5 primary ID集合（若空，只有上列R1–R4/执行范围）：{', '.join(ids) if ids else '无R5 primary记录'}。

恢复helper为 `../../restore_fanout_inputs.py`，必须先全文读懂；它仅从已核固定Git对象取blob并做有界gzip恢复，写入本独占目录，绝不执行恢复材料。普通fetch由你在自身隔离bare完成，不能用分支未来HEAD。

本合同拥有 {len(ids)} 个完整R5合同与 {len(criteria)} 个原schema检查（逐ID在readset），不是按V/N字符串重新造验收。每个primary完整原事实、前提、普通对照、反例、失败/取消/部分提交、七组/八节、反向clause、参数/default/枚举、完整case预期、保留/验收/同步和必要消费者都须实际接收。已有完整对象视图可用于无损连续阅读，必须校验raw/expanded和字典关联，不能只读其导航或只读字段名。

纯身份和无业务值的传输/结构字段按完整类型、集合、用途处理；不逐hash字符串增加“人工通过”。业务意义即使在 `original_actual_text` 或旧路由下也不能跳过。B/C/D跨用同一字典值只复用精确字节，不自动授另一个语境的事实批准。

## 独占写集、依赖与完成规则

唯一写集：`{readset['exclusive_write_set']}`。本合同目录、公共分母、原作者目录、其它receiver目录、正式/planning/audit/R/main/tag只读。实际路径按云端checkout映射，不能假设Mac路径。

{readset['git_coordination']}

其它shard的primary集合禁止重签或改写。可读取相邻producer/receiver作为本域必要上下文，标明 `CONTEXT_ONLY`、主责ID和精确依赖。已读消费者不代表未读producer已接。共享字段/状态的语义由tail shard审读，逐producer贡献分别由各primary shard签，最终协调者核完整接合；共享依赖只阻塞相关事实。所有可独立部分持续完成，不等无关任务。

{('本任务可独立起步；不等待R5 producer。' if pid=='early_r1_r4' else '本任务可独立读完所有本域合同和必要定义，末端跨域握手引用实际非作者收据，不能用任务名或角色名代替签名。')}

逐单位输出完整当前有效意义、固定R/B8定位、实际非截断读片/输出身份、消费者接合、判定理由、未决和原字节身份。所列8份输出必须包含精确已完整接收、必要未接收、不可得材料限制，二者分开。没有剩余必需对象才可给 `READY_FOR_COORDINATOR_CONSOLIDATION`；涉及尚未收到producer的接口单列OPEN，不得给whole interface签名。整H任务的 `READY_FOR_ROOT_TASK_FINAL_ACCEPTANCE`、canonical及全局task-final只由根主审处理。

保留原FAIL/WAIT/MISMATCH/退出未知/后继clarifier。新发现只提案，不自封required；给最强不需修订解释。特别是RECEPTION-H-EARLY-POLICY-002（UTIL-03末尾LF）是旧policy事实限定候选，未来政策仍未决，不因发现它就改B8或重开历史92/第七轮27。

请求gpt-6.1-sol/ultra/default普速/Fast off；真实无回显逐项UNVERIFIED。行为初始NOT_EXECUTED/新增0，UPDATE_NOT_STARTED。写集保护、执行安全和下文原全文合同全部适用；原prompt中更宽全系统范围按本合同唯一primary与必要接口限定，不能把本task扩成重审全系统。

---
## 内嵌：原固定接收任务完整prompt

{parent}
---
## 内嵌：完整全局prompt

{fullglobal}
---
## 内嵌：适用AGENTS全文

{agents}
---
## 内嵌：review-SKILL全文

{skill}
'''
 (S/'prompt.md').write_text(header)
 p['primary_R5_ids']=ids;p['primary_R5_criteria']=criteria;p['exclusive_write_set']=readset['exclusive_write_set'];p['readset_identity']=ident((S/'readset.json').read_bytes());p['prompt_identity']=ident((S/'prompt.md').read_bytes());p['complete_view_encoded_identity']=ident(z);p['complete_view_decoded_identity']=ident(raw);p['binding_occurrences_not_new_requirements']=len(bindings);p['original_complete_object_count_not_new_control_count']=len(units);p['necessary_initial_file_candidates']=len(candidates)
 write(S/'manifest.json',{'schema':'gr8.h-early-fanout.shard/v1',**p,'reading_credit':0,'started':False})
# Explicit aggregation, including every R5 criterion once, without administrative leaf expansion.
criteria=[u['criterion_id']for r in RECORDS for u in r['schema_units']];assert len(criteria)==568 and len(set(criteria))==568
assert set(owner)=={r['id']for r in RECORDS};assert sum(len(p['primary_R5_criteria'])for p in parts)==568
aggregation={'schema':'gr8.h-early-fanout.aggregation/v1','utc':UTC,'status':'FROZEN_NOT_STARTED','coordinator_context':'01a14466-375e-775a-8f34-5cfb2471003d','target_author_context':AUTHOR,'target_commit':TARGET,'fixed_previous_reception':BASE,'source_contract':'40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232','shards':parts,'coverage_proof':{'R5_primary_exact_union':92,'R5_primary_overlap':0,'schema_exact_union':568,'schema_overlap':0,'split_counts':[(p['id'],len(p['primary_R5_ids']),len(p['primary_R5_criteria']))for p in parts]},'global_metadata_primary':'r5_tail_shared_policy','earlier_history_primary':'early_r1_r4','shared_protocol':[{'producer_id':r['id'],'primary':owner[r['id']],'receiver':'r5_tail_shared_policy','binding':'历史全局shared21/dependency18中与该producer有关的具体scope/当前接收事实；不是整批PASS'}for r in RECORDS],'acceptance_rules':['分别核实际context非目标作者，固定输入/完整合同/独占写集及每个单位真实非截断阅读。','R5每ID及其原criterion只一个primary；同值/相同文件/旧PASS不是额外审者或新要求。','每条record完整意义与必要R/B8定义/消费者实际到位；有原始字段未接收不能用part completion遮盖。','共享21、18依赖与scope/producer逐事实对接；不以四个任务状态代替实际接口接收。','A所辖R1–R4/执行及D所辖非必修/policy/limit分别保持原人口和原未来选择，不自动采用。','EVIDENCE-001和POLICY-002均需要真正非提出者的独立理由；未判定不自动变B8required或PASS。','全部精确未接收差集为0、全部必要交界闭合后，根才可考虑task-final；材料/宿主限制不替代可得未读。','普通发布/远端全字节回读单独验收，不授semantic credit；UPDATE_NOT_STARTED。'],'remaining_semantic_denominator':'四个完整对象集合及其完整字段/有限接口；6769 V与908 N是定位和去重指标，不能要求人为逐原子造验收。','parallel_first_wave':[p['id']for p in parts],'actual_new_contexts_started':0,'root_final_signed':False,'UPDATE_NOT_STARTED':True}
write(F/'aggregation.json',aggregation)
write(F/'evidence/generation-validation.json',{'utc':UTC,'mechanical_only':True,'R5_92_partition_exact':True,'R5_568_criterion_partition_exact':True,'original_r5_inputs_identity_count':18,'original_r5_decoded_bytes':10050868,'source_availability_file_counts':[(x['type'],len(x['files']))for x in indexes],'generated_shards':[(p['id'],p['prompt_identity'],p['readset_identity'],p['complete_view_encoded_identity'],p['complete_view_decoded_identity'])for p in parts],'no_semantic_reading_credit_from_generation':True,'new_contexts_started':0})
print(json.dumps({'shards':[(p['id'],len(p['primary_R5_ids']),len(p['primary_R5_criteria']),p['complete_view_decoded_identity']['bytes'])for p in parts],'status':'FROZEN_NOT_STARTED','semantic_credit':0},ensure_ascii=False))
