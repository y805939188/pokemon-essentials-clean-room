from pathlib import Path
import json,hashlib,datetime,shutil,subprocess
root=Path(__file__).resolve().parents[1];repo=root.parents[2]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def write(p,x):
 f=root/p;f.parent.mkdir(parents=True,exist_ok=True);f.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def load(p):return json.loads((root/p).read_text())
h=root/'tasks/history_current';hist=json.loads((h/'subshards.json').read_text())
write('delegation/history-subshards.snapshot.json',hist)
shutil.copyfile(h/'recover_transport.py',root/'delegation/helpers/recover_transport.py')
jobs=[]
for s in hist['shards']:
 name=s['id'].lower().replace('-','_');read=json.loads(Path(s['readset_path']).read_text())
 read.update(primary_task=name,write_root=str(root/'tasks'/name),recovery_tool=str(root/'delegation/helpers/recover_transport.py'))
 read['recovery_tool_write_note']='Read whole helper; copy into this task own write root (TASK is __file__ parent); restore only into fresh absent directory. Restored evidence is never executed.'
 write('delegation/readsets/'+name+'.json',read)
 prompt=Path(s['prompt_path']).read_text().replace(str(h/'contract.md'),str(root/'inputs/eighth-global-review-prompt.md')).replace(s['readset_path'],str(root/'delegation/readsets'/f'{name}.json'))
 prompt+='\n正式独占写集已赋为 `'+str(root/'tasks'/name)+'`。实际平台ID由真实启动回显填写，未知UNVERIFIED。技能在 `'+str(root/'inputs/review-SKILL.md')+'`。恢复helper在 `'+str(root/'delegation/helpers/recover_transport.py')+'`，先全文读懂，再复制到任务独占目录；TASK自动取自身父目录。所有7个原历史commit与15份关键原载荷已由history_current在隔离bare成功fetch并核身份，旧LOCAL_MISSING已解除，不把本地缓存条件冒作材料limit。新的环境可按精确SHA在自身隔离bare普通fetch。原文件/proposal/证据只读，UPDATE_NOT_STARTED。\n'
 (root/'delegation/prompts'/f'{name}.md').write_text(prompt)
 jobs.append({'id':name,'scope':s['scope'],'prompt':'delegation/prompts/'+name+'.md','readset':'delegation/readsets/'+name+'.json','write_set':'tasks/'+name+'/','input_rows':len(read['files']),'input_bytes_with_versions':s['input_decoded_bytes_with_versions'],'state':'NO_ACTUAL_START_RECEIPT_IN_COORDINATOR','requested':s['requested_configuration']})
write('delegation/third-wave.json',{'schema':'gr8-third-wave/v2','utc':now,'additional_jobs':jobs,'additional_count':4,'previous_dispatchable_count':21,'all_dispatchable_count':25,'input_availability_validation':'tasks/history_current/dispatch-validation.json','semantic_status':'Only actual read ledgers grant semantic credit; dispatch is not completion','update_started':False})
snap=root/'evidence/proposal-snapshots';snap.mkdir(parents=True,exist_ok=True)
proposals=[]
for name in ['kernel_review','combat_review','history_current','world_topology_audit','ui_navigation_audit','pbs_world_record_audit']:
 p=root/'tasks'/name/('findings.json' if name in ['kernel_review','combat_review','history_current'] else 'proposals.json')
 if not p.exists():continue
 raw=p.read_bytes();x=json.loads(raw);sha=hashlib.sha256(raw).hexdigest();target=snap/(name+'-'+sha+'.json');target.write_bytes(raw)
 items=x if isinstance(x,list) else x.get('records',x.get('proposals',x.get('findings',[])))
 for item in items:proposals.append({'origin_task':name,'immutable_proposal_snapshot':str(target.relative_to(root)),'snapshot_sha256':sha,'record':item,'root_status':'WAIT_ROOT_FINAL_CANONICAL_ADJUDICATION'})
cp=root/'tasks/creature_review/proposals/GR8-CRE-001.v2.json'
if cp.exists():
 raw=cp.read_bytes();sha=hashlib.sha256(raw).hexdigest();target=snap/('creature_review-'+sha+'.json');target.write_bytes(raw)
 proposals.append({'origin_task':'creature_review','immutable_proposal_snapshot':str(target.relative_to(root)),'snapshot_sha256':sha,'record':json.loads(raw),'root_status':'INDEPENDENT_RECOMMENDATION_RECEIVED_WAIT_ROOT_CANONICAL_ADJUDICATION','independent_review':'tasks/combat_review/adjudications-creature.json'})
write('findings.json',{'schema':'gr8-findings/v3','utc':now,'proposals':proposals,'adjudicated_required':[],'required_count':None,'required_count_reason':'Whole review and root final canonical adjudication are incomplete; no NO_REQUIRED_UPDATE conclusion','independent_receptions':['tasks/counter_kernel_first/adjudications.json','tasks/combat_review/adjudications-creature.json'],'root_partial_counterreview':'coverage/root-counterreview-notes.json','update_started':False})
completed=['inventory_denominator','history_current','kernel_review','combat_review','creature_review','counter_kernel_first']
running=['preflight_resources','counter_combat_first','coverage_acceptance_audit','world_topology_audit','ui_navigation_audit','pbs_world_record_audit']
state=load('progress.json');state.update(utc=now,status='RUNNING',semantic_completion='INCOMPLETE_NO_GLOBAL_PASS',pending_external_dispatchable_jobs=25,actual_spawned_child_contexts=12,actual_contexts_including_root=13,actual_active_collaboration_contexts_including_root=7)
state['tasks']={n:{'platform_entry':'/root/'+n,'process_status':'COMPLETED' if n in completed else 'RUNNING','semantic_status':'SCOPED_OUTPUT_WITH_OPEN_JOINS' if n in completed else 'IN_PROGRESS','outputs':'tasks/'+n,'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'Fast off'},'actual':dict.fromkeys(['model','effort','tier','speed'],'UNVERIFIED')} for n in completed+running}
state['external_cloud_start_receipts']='UNVERIFIED; no receipt in this coordinator. Planned count does not assert service capacity or external process state.'
state['proposal_count_at_snapshot']=len(proposals);state['behavior_executions']={'reference_observation':0,'host_demo':0,'native_media':0,'independent_numeric_model_exploration_processes':1,'numeric_model_verification_credit':0}
state['report_metadata_corrections_pending']=[{'task':'counter_kernel_first','path':'reading-ledger.json','requested_range':[595,633],'actual_source_EOF':624,'action':'Preserve request, qualify actual read595-624; no additional reading credit; author followup pending slot.'}]
state['cloud_input_package']={'library_file_id':'libfile_4b51216024e48191b2cf3166a331583d','bytes':16531493,'sha256':'6a2b23bd78ba13effe19dd00fc26c268edb9ac53a4927eb1ea13412db6e2511e','status':'NOT_MATERIALIZED_DNS_FAILURE','needed':'Exact same ZIP on independent Git branch fixed commit/path, or a working supported Library workspace transfer','cloud_prompt_status':'UNREAD; original full contract read; publisher states section4-end identical'}
write('progress.json',state)
status='''# 第八轮全局 review 进行状态

完整审查尚未完成，当前没有全局 PASS。`UPDATE_NOT_STARTED`。

B8固定为fd1df570cad987dc3852a3b958f03916e317f7fe，tree751dfde81048c81390f89a65ca1d1a565ba8e1ca，formal tree f292698cdd4a8e725525a9be6dc34b75faaf151e；R固定8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/tree7589c800b61ba13a13040ed0d686979b80a84fd0。正式文件、R、main、原tag没有修改。报告分支的合法后继不替代B8。

完整库存R432（44906485bytes）、formal131（4364108bytes），各路径主责0遗漏/0重复。四planning已全文读并冻结87WP计划行、113Feature、18领域。395条声明知识依赖不是运行接口全集。原manifest的纯历史索引按用途处置；有效后继事实/资格仍需按精确来源接收。

当前已结束的六个实际上下文交付了限定成果：库存、历史恢复与资格、kernel、combat核心、creature-A、kernel独立反证。kernel13formal/77初始源、CORE6formal/16源、CRE-A7formal/11primary源全文读均有台账；它们明确仍有复合clause、其它数据、消费者和跨域未接收。不同任务重叠读取不能相加冒作全局唯一已读数。

正在运行预检/二进制、combat独立反证、全分母接收审计、世界拓扑、UI导航与PBS-world全记录六任务。加root实际7个并发，当前工具容量7；没有人为增加更低并发上限。全部实际上下文请求gpt-6.1-sol/ultra/default普速/Fast off，实际无回显字段逐项UNVERIFIED。CLI已测因只读app-server初始化失败，新增CLI上下文0。

完整可派发合同：delegation/first-wave.json 17项，second-wave.json新增creature四片，third-wave.json新增历史四片，共25项。每项有完整prompt、逐载荷身份读集及独占写集。计划不等于实际启动；本协调者没有这些外部会话的启动回执。主线程可按实际服务容量代建，不重复创建已具名实际任务。新世界/UI/PBS实际审者在各自独立目录贡献相应部分，旧domain角色名不授语义接收。

独立反证已经对kernel三提案与CRE一提案给出有限建议，root最终canonical去重/分类尚未完成。kernel002撤回WP02/KC05充分示例的错误指控，只保留穷尽启动门的精确范围。CORE两提案、world拓扑失败前缀、PBS数据断言、UI保存取消强断言等仍分别审查，不能把疑点数或建议数当最终必修数。

严格覆盖审计发现现有reverse矩阵许多行没有事实link，方法/行/分号片段都不是最终atomic分母。所有已有FULL_READ、STRUCTURE_PARSED、库存身份核验、推导与业务观察分列；未读与未接收不能改成材料limit。controller1666与媒体/字体/messages等仍有真实可审未读。counter_kernel_first一条范围上限超过EOF正在作原请求/实际范围元数据更正，不因此凭空新增阅读或撤回其它有证实读。

新参考/游戏/完整宿主/媒体观察0；CRE一过程Python数值探索exit0而缺开始UTC，保持探索1、业务验证信用0，原L14缺口不倒填。全部未实际运行的向量NOT_EXECUTED。静态工具运行与真实I/O另列，不冒充宿主等价。

材料访问障碍仅具名保留：Library云端ZIP 16531493bytes/SHA2566a2b23bd78ba13effe19dd00fc26c268edb9ac53a4927eb1ea13412db6e2511e未能通过官方helper下载（DNS失败），因此CLOUD-READ-FIRST/new cloud prompt/readiness/final binding/131MB recovery map尚未在此环境完整读。已请求固定Git commit/path替代。原完整36653bytes合同已全文读并核SHA；skill3598bytes同样已读核。R7/R6旧Git对象本地缺失已在隔离bare成功恢复7commit/15关键载荷，原假材料阻塞解除，剩余是真未读。

初始分工检查点7478d8daf357d569ac12bea211b4b5f257861930已普通push，54文件/916631bytes完整隔离远端读回通过；这是传输验证而非语义批准。最终语义core、最终完整整改handoff和全量完成验收尚未达到。报告本身可以修正/补齐；正式整改没有启动。
'''
(root/'status-report.md').write_text(status)
selected=[];local_only=[]
for f in root.rglob('*'):
 if not f.is_file() or f.is_symlink():continue
 rel=f.relative_to(root);parts=rel.parts
 if parts[0] in ['inputs','delegation','publication'] or len(parts)==1 or rel.as_posix()=='coverage/root-counterreview-notes.json' or parts[:2]==('evidence','proposal-snapshots'):
  if f.name=='checkpoint-selection.json':continue
  selected.append(f);continue
 if len(parts)>2 and parts[0]=='tasks' and parts[1] in completed+['reference_metadata']:
  if any(s=='object-cache.git' or s.startswith(('recovered-','readset-materialized-')) or s=='__pycache__' for s in parts[2:-1]):
   local_only.append(str(rel));continue
  selected.append(f)
for f in selected:
 if f.suffix=='.json':json.loads(f.read_bytes())
rows=[{'path':str(f.relative_to(repo)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in sorted(selected)]
write('publication/checkpoint-selection.json',{'schema':'gr8-checkpoint-selection/v1','utc':now,'selected_files_except_this_selection':rows,'count':len(rows),'bytes':sum(x['bytes'] for x in rows),'local_only_cached_inputs':local_only,'exclusion_reason':'Nested bare repository and exact historical input byte caches are reproducible from fixed objects/transport and excluded; recovery receipts preserve identities. No local source/caches removed.','semantic_core_status':'NOT_FROZEN','update_started':False})
selected.append(root/'publication/checkpoint-selection.json')
subprocess.run(['git','-C',str(repo),'add','--']+[str(f.relative_to(repo)) for f in selected],check=True)
staged=subprocess.check_output(['git','-C',str(repo),'diff','--cached','--name-only','-z']).split(b'\0')
prefix=str(root.relative_to(repo))+'/'
assert all(not p or p.decode().startswith(prefix) for p in staged)
print(json.dumps({'selected_report_files':len(selected),'bytes':sum(f.stat().st_size for f in selected),'proposals_at_snapshot':len(proposals),'dispatchable_planned':25,'local_only_cached_input_files':len(local_only),'all_selected_json_valid':True},ensure_ascii=False))
