"""Reconcile already read evidence. No reference execution; writes only this task."""
from pathlib import Path
from collections import Counter,defaultdict
import datetime,gzip,hashlib,json,re,shutil,subprocess
T=Path(__file__).resolve().parents[1]
C=T.parents[4]
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
B8='fd1df570cad987dc3852a3b958f03916e317f7fe'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
CHECKPOINT='38e78d05acacd800ddb159ddcbd5949dc0d76b9e'
CAT=json.loads((T/'payload-catalog.json').read_text())['rows']
def dump(n,v):
 p=T/n;assert T in p.parents;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def get(i):
 b=gzip.decompress((T/CAT[i]['decoded_object']).read_bytes())
 try:return json.loads(b)
 except ValueError:return b.decode()
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
# Keep the exact earlier reading state as a historical checkpoint, not current debt.
oldnames=['progress.json','reading-ledger.json','purpose-dispositions.json','history-current-acceptance.json','findings.json','unread.json','terminal-reading-ledger.jsonl.gz','report.md']
S=T/'continued/checkpoint-38e78d'
if not S.exists():
 S.mkdir()
 for n in oldnames:shutil.copyfile(T/n,S/n)
ledgers=sorted((T/'continued').glob('reading-ledger-0*.json'))
accept=[]
for p in sorted((T/'continued').glob('U*-current-acceptance.json')):
 d=json.loads(p.read_text());accept.extend(dict(x,batch=p.name[:3],evidence=str(p.relative_to(T))) for x in d['contracts'])
assert len(accept)==56 and len({x['id'] for x in accept})==56
assert sum(json.loads(p.read_text())['case_units'] for p in (T/'continued').glob('U*-current-acceptance.json'))==351
# Explicit identity-only pointer dispositions. The original values remain lossless.
inv=defaultdict(set);whole=defaultdict(set)
for folder in ['global','global-v2','global-v4']:
 for x in json.loads(gzip.decompress((T/f'continued/{folder}/identity-inventory.json.gz').read_bytes())):
  m=re.match(r'row(\d+)#(.*)',x['ref'])
  if not m:continue
  row=int(m[1]);ptr=m[2]
  if '/$semantic_fields' in ptr:continue
  if x.get('purpose','').startswith('EXACT_OBJECT_IDENTITY_FIELDS_ONLY'):
   for k in x['value']:inv[row].add(ptr+'/'+k.replace('~','~0').replace('/','~1'))
  else:whole[row].add(ptr)
contracts=json.loads((T/'continued/compact-contract-view-index.json').read_text())
pathrows={r['input']['path']:r['row'] for r in CAT}
for x in contracts['identity_dispositions']:
 path,ptr=x['pointer'].split('#',1)
 if path in pathrows:whole[pathrows[path]].add(ptr)
# Exact whole-payload aliases preserve both version roles; no old PASS transfer.
alias={9:0,10:1,11:2,12:3,13:4,14:5,15:6,44:38}
old=json.loads((S/'reading-ledger.json').read_text())
old_full=set(old['full_read_rows'])
counts=Counter();perrow=defaultdict(Counter)
with gzip.open(S/'terminal-reading-ledger.jsonl.gz','rt') as src,gzip.open(T/'terminal-reading-ledger.jsonl.gz','wt',encoding='utf-8') as dst:
 for line in src:
  x=json.loads(line);row=x['row'];base=alias.get(row,row);ptr=x['pointer']
  prefixes=whole[base]|inv[base]
  ancestor=ptr
  admin=x['status']=='INVENTORY_ONLY_IDENTITY'
  while not admin:
   if ancestor in prefixes:admin=True;break
   if '/' not in ancestor:break
   ancestor=ancestor.rsplit('/',1)[0]
  if admin:status='PURPOSE_DISPOSED_IDENTITY_ONLY_NO_SEMANTIC_CREDIT'
  elif row in alias:status='EXACT_SAME_TASK_PAYLOAD_READING_ASSOCIATION'
  elif row in old_full:status='DIRECT_FULL_READ_RETAINED'
  else:status='FULL_EFFECTIVE_TEXT_READ_WITH_LOSSLESS_ALIASES'
  x.update(status=status,reader='/root',reading_state_evidence='continued/reading-ledger-001..025 plus exact view indices',main_reception='PENDING_MAIN_REVIEW')
  counts[status]+=1;perrow[row][status]+=1
  dst.write(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n')
assert sum(counts.values())==626398
entries=[]
for r in CAT:
 i=r['row'];purpose='FULL_EFFECTIVE_SEMANTIC_TEXT_READ; pure identities separately disposed'
 if i in alias:purpose='EXACT_IDENTICAL_SAME_TASK_ALIAS_OF_ROW_'+str(alias[i])
 entries.append({'row':i,'input':r['input'],'payload_recovery':r['decoded_object'],'reader':'/root','actual_platform_uuid':'UNVERIFIED','recorded_utc':NOW,'individual_original_read_utc':'UNVERIFIED_NOT_BACKFILLED','reading':purpose,'full_effective_semantics_read':True,'physical_repeated_identity_bytes_human_reread_claimed':False,'terminal_or_line_count':sum(perrow[i].values()),'terminal_or_line_status_counts':dict(perrow[i]),'scope_evidence':'continued/reading-ledger-001..025; lossless view indices and template-proofs','source_or_current_formal_approval_from_payload_reading':False,'main_reception':'PENDING_MAIN_REVIEW'})
dump('reading-ledger.json',{'schema':'r8.external-r6-reading-ledger.v2','recorded_utc':NOW,'reader':'/root','requested':old['requested'],'actual_model':'UNVERIFIED','actual_effort':'UNVERIFIED','actual_tier':'UNVERIFIED','actual_speed':'UNVERIFIED','actual_fast':'UNVERIFIED','actual_platform_uuid':'UNVERIFIED','historical_checkpoint':{'commit':CHECKPOINT,'preserved_in':'continued/checkpoint-38e78d','old_full_rows':17,'old_incomplete_rows':43},'rule':'All current effective rules/premises/proposals/cases/consumers/states/receivers were actually read. Exact content aliases and reversible templates preserve every novel semantic value. Pure identity inventories have purpose disposition and zero game semantic credit; no search/hash/parser or old PASS substitutes reading. Terminal counts are structural, not behavioral requirements.','payload_roles':60,'unique_decoded_objects':52,'decoded_bytes_with_role_multiplicity':44241376,'full_effective_roles':60,'unread_effective_roles':0,'same_task_exact_payload_alias_rows':alias,'terminal_or_line_status_counts':dict(counts),'terminal_denominator':sum(counts.values()),'continuation_ledgers':[{'path':str(p.relative_to(T)),'sha256':h(p)} for p in ledgers],'entries':entries,'main_reception':'PENDING_MAIN_REVIEW','new_behavior_execution':'NOT_EXECUTED'})
dis=[]
for e in entries:
 i=e['row'];dis.append({'row':i,'commit':e['input']['commit'],'path':e['input']['path'],'bytes':e['input']['bytes'],'sha256':e['input']['sha256'],'git_blob':e['input']['git_blob'],'mode':e['input']['mode'],'purpose':e['input']['purpose'],'reading':e['reading'],'effective_semantics_exempted':False,'identity_only_pointers':sorted(whole[alias.get(i,i)]|inv[alias.get(i,i)]),'main_reception':'PENDING_MAIN_REVIEW','raw_identity_source':'payload-catalog.json','semantic_approval_from_identity':False})
dump('purpose-dispositions.json',{'schema':'r8.external-r6-purpose-dispositions.v2','recorded_utc':NOW,'entries':dis,'historical_identity_only':'Source432/formal131/supplement116/full remote byte lists/exact block identifiers are historical identity or reading-scope records. All their semantic reading qualifications were read, but no fresh whole-R or whole-formal game approval inherited. Embedded actual65 contracts and original proposals fully read separately.','identity_values_lossless_indices':['continued/compact-contract-view-index.json','continued/global/identity-inventory.json.gz','continued/global-v2/identity-inventory.json.gz','continued/global-v4/identity-inventory.json.gz'],'unread_current_effective_semantics':0})
history=json.loads((S/'history-current-acceptance.json').read_text());history['schema']='r8.external-r6-history-current-acceptance.v2';history['recorded_utc']=NOW;history['state']='ASSIGNED_EFFECTIVE_CONTRACT_STATIC_REVIEW_COMPLETE_PENDING_MAIN_RECEPTION'
for g in history['groups']:g['original_structured_verdict_full_read']=True;g['fresh_source_and_B8_scope']='See56 per-ID independent bounded static notes; not full global B8 approval'
history['phase_chain'][1]['structured_original_full_read']=True
for ph in history['phase_chain'][2:]:
 ph['stage_projections_full_read']=True;ph['independent_full_stage_payload_read']=False;ph['qualification']='Exact stage identity and effective projections in row1/4/5/46 read. No claim of newly rereading every file of stage commit.'
history['nonmandatory']='All8 optional original proposals/seven groups,1 no-required original proposal/seven groups,7policy records,1Float facet and14limits full effective text read; exact named prior-reader field association retained as corroboration only. None reclassified or selected.'
history['current_independent_contracts']=accept
history['current_cases']={'body_denominator':351,'full_body_read':351,'conditional_static_review':351,'new_execution':0,'main_received':0,'source':'four recovered assigned-14-current-reception.json; continued batch ledgers'}
history['joint_interfaces'][0]['fresh_read_result']='Positive-only add cap; zero/raw-negative bypass it. Separate final validity bounds and exact-size focus; nil/[] return identity. WP54/WP66A consumers read, no extra required ID.'
history['joint_interfaces'][1]['fresh_read_result']='Successful third-round recharge2→EOR1 survives winner cancellation and blocks following action until its tail0; replaced loser resets. Disable identity and Charge cleanup remain distinct earlier gates.'
history['joint_interfaces'][2]['fresh_read_result']='Raw defaults/schema/header/friendship/Flags and language key/image/cache consumers checked with separate write/read/save points; compile/cache success does not imply new cache or host/media success.'
for j in history['joint_interfaces']:j['local_independent_bounded_static_review']='SUPPORTED_IN_STATED_PREMISES';j['main_received']=False
history['H10_process_deviation']='H10-PROCESS-DEVIATION-001 retained: old auxiliary3 spawns/2 followups not completion authority; this task spawn0.'
history['main_final_reception']='PENDING_MAIN_REVIEW';history['current_global_B8_PASS']=False
history['remaining_assigned_semantic_unread']=0
history['historical_failures_preserved']=True
dump('history-current-acceptance.json',history)
#110 original gates are process/finite-static meanings, not 110 gameplay scenarios.
dep=get(5);kinds=Counter(e['kind'] for e in dep['edges']);edge_rows=[]
for e in dep['edges']:
 edge_rows.append({'index':e['index'],'from':e['from'],'to':e['to'],'kind':e['kind'],'original':e,'fresh_read':'FULL_EFFECTIVE_EDGE_FIELDS_READ','adjudication':'ORIGINAL_FINITE_STATIC_OR_PROCESS_SCOPE_CONFIRMED; no configuration/runtime certificate','basis':'All14 complete seven-group contracts, all56 current independent source/B8 notes, all351 case bodies, row1/4/5 complete effective fields, actual-five originals and5c original','main_reception':'PENDING_MAIN_REVIEW'})
dump('continued/current-dependency-and-interface-review.json',{'schema':'r8.external-r6-dependency-current.v1','recorded_utc':NOW,'B8':B8,'R':R,'edge_denominator':110,'full_effective_read':110,'locally_reviewed_finite_scope':110,'main_received':0,'kinds':dict(kinds),'original_5c_gate_state':'108 satisfied +2 future owner events; b7 formal acceptance and4df closure distinct later events, not retroactive5c authority','joint_interfaces':history['joint_interfaces'],'per_id_notes':accept,'edges':edge_rows,'new_behavior_execution':'NOT_EXECUTED','current_global_PASS':False})
# Retain named prior reading exactly; fresh full reading supersedes its old unread remainder.
f=T/'named-field-reception.json';named=json.loads(f.read_text());named['fresh_full_effective_read_successor']={'recorded_utc':NOW,'reader':'/root','original_proposals_read':9,'original_proposal_denominator':9,'source':'continued/reading-ledger-023-nonmandatory-C17.json','main_reception':'PENDING_MAIN_REVIEW','does_not_inherit_prior_PASS':True};dump('named-field-reception.json',named)
dump('unread.json',{'schema':'r8.external-r6-unread.v2','recorded_utc':NOW,'state':'ASSIGNED_AVAILABLE_EFFECTIVE_SEMANTIC_READING_COMPLETE_PENDING_MAIN_RECEPTION','actual_material_or_permission_blocker':False,'available_effective_payload_roles_unread':0,'complete_contracts':{'denominator':56,'seven_groups_and_original_proposals_read':56,'unread':0,'local_independent_conditional_static_review':56,'main_not_received':56},'cases':{'denominator':351,'full_case_bodies_read':351,'unread':0,'conditional_static_review':351,'main_not_received':351},'dependencies':{'denominator':110,'effective_full_fields_read':110,'unread':0,'local_finite_static_or_process_review':110,'main_not_received':110},'joint_interfaces':{'denominator':3,'local_necessary_consumers_reviewed':3,'unread':0,'main_not_received':3},'pure_admin_identity_purpose_disposition':dict(counts),'main_not_received_is_not_unread':True,'outside_scope_unverified':['No new full R432/formal131 approval; bounded consumer ranges recorded rather than full-file claims.','Host/Demo/native/media/input/audio/real save/replay and full independent behavior model not executed.','Actual model/effort/tier/speed/Fast/platform UUID UNVERIFIED.','No new binary re-decode, full native registration bridge or old3703 remote payload reread claimed.','Original b7/4df effective projections and identities reviewed, not every original commit payload.','Main independent counter/adjudication/final reception remains pending.'],'new_behavior_execution':'NOT_EXECUTED','update_status':'UPDATE_NOT_STARTED'})
dump('findings.json',{'schema':'r8.external-r6-findings.v2','recorded_utc':NOW,'proposed':[],'confirmed_required':[],'verdict':'NO_NEW_REQUIRED_PROPOSAL_IN_COMPLETED_ASSIGNED_FINITE_STATIC_SCOPE','NO_REQUIRED_UPDATE':False,'NO_REQUIRED_UPDATE_scope_note':'Global no-required-update/final adjudication is reserved to main reviewer; zero proposed findings is not a B8 global PASS.','independent_counter_review':'PENDING_MAIN_REVIEW','current_source_approval':'56 bounded source-contract-case chains supported in stated premises; no blanket shared-file/global approval','negative_hypotheses_retained':['F002 WP66-A later receiver condition is not a candidate allowlist defect.','U13 oldFAIL remains for its old object; repair and actual receiver stages distinct.','AN-M09 current premise and Debug WP72§5.3 navigation are corrected at B8; do not inherit old GR7 findings.','party004 old stale-command hypothesis refuted; nonmandatory records not automatically mandatory.','False/null/pending old nested phase fields do not override explicit later b7/4df events.'],'main_final_reception':'PENDING_MAIN_REVIEW','update_status':'UPDATE_NOT_STARTED'})
p=json.loads((S/'progress.json').read_text());p.update(schema='r8.external-r6-progress.v2',updated_utc=NOW,recorded_utc=NOW,task_state='ASSIGNED_REVIEW_COMPLETE_PUBLICATION_PENDING',status='COMPLETE_ASSIGNED_STATIC_REVIEW_PENDING_PUBLICATION',semantic_state='FULL_ASSIGNED_FINITE_STATIC_REVIEW_COMPLETE',publication_state='FINAL_CORE_NOT_YET_FROZEN',current_batch='FINAL_PUBLICATION',remaining_blocker='No actual material/permission blocker; main independent reception pending, host/configuration unverified separately.',continuation_ledgers=[str(x.relative_to(T)) for x in ledgers]);p['denominators'].update(full_effective_read_rows=60,not_full_effective_read_rows=0,direct_full_read_unique_payloads='NOT_PHYSICAL_BYTE_REREAD_METRIC; lossless semantic views and identity-purpose dispositions',full_read_rows_including_identity_associations=60,not_full_read_rows=0,edge_evidence_and_consumers_locally_reviewed=110,edge_evidence_and_consumers_accepted_by_main=0,joint_interfaces_locally_reviewed=3,B8_joint_source_acceptances_by_main=0);p['denominators'].pop('edge_evidence_and_consumers_accepted',None);p['denominators'].pop('B8_joint_source_acceptances',None);dump('progress.json',p)
report='''# H-R6-EFFECTIVE-CONTRACTS 第八轮独立审查结果

获派有限范围的可得有效语义审读已完成，未提出新的必修发现。状态为 `ASSIGNED_FINITE_STATIC_REVIEW_COMPLETE / PENDING_MAIN_REVIEW`；主审独立反证与最终接收尚未发生，本报告不签 B8 全局 PASS 或全局 `NO_REQUIRED_UPDATE`。未整改，`UPDATE_NOT_STARTED`。

固定合同 `30cfed0996003b6ebf4b5c51cc04f31ca9255440` 下的任务 prompt、readset、完整全局 prompt、skill、AGENTS、恢复 helper 均已全文读取，原输入身份见 `input-verification.json`。最新用户授权仅替代原独占目录及禁提交要求：唯一写集是本报告目录，唯一分支 `codex/r8-external-h-r6-effective-contracts-20261016`，允许 commit 与普通 push 自身证据；未启动子任务，未改正式规格、R、main/tag、公共台账或他人目录。

实际项目 `/workspace/pokemon-essentials-clean-room`，R `/workspace/pokemon-essentials`。B8 commit/tree 为 `fd1df570cad987dc3852a3b958f03916e317f7fe` / `751dfde81048c81390f89a65ca1d1a565ba8e1ca`，formal tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`；R commit/tree 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `7589c800b61ba13a13040ed0d686979b80a84fd0`。历史本机绝对路径仅映射到上述云端路径，不冒称相同环境。

| 分母 | 本任务完成 | 主审未接收 |
| --- | --- | --- |
| 60载荷角色，52不同decoded对象，44,241,376字节 | 60有效语义全文或精确同轮别名；纯身份用途处置另列 | 本报告整体待接收 |
| 56合同、14批、逐项七组及完整原提案 | 56逐项实读及有条件独立静态源—B8—消费者核对 | 56 |
| 351案例，四原实际接收载荷 | 351本体全文及逐项有限静态核对（86/88/88/89） | 351 |
| 110依赖边 | 110完整有效字段及原有限静态/过程门含义核对 | 110 |
| 3联合接口 | F002 E→D、Arena V004 E→B、U14 A→C必要消费者核对 | 3 |
| 九补充双版本 | 七对同字节精确关联；matrix/audit两对后继均全文有效语义审读 | 本报告待接收 |
| 五实际原报告与structured verdict、5c原报告/verdict | 均全文有效语义审读，A11/B9/C19/D9/E8唯一56 | 本报告待接收 |
| 非必修与历史 | 8optional、1no-required完整原提案/七组；Float1、policy7、limits14分列全文 | 不选择、不升级必修 |

完整过程证据在 `continued/reading-ledger-001..025`，每批独立结论在 `continued/U01-current-acceptance.json` 至 `U14-current-acceptance.json`。这些记录包含固定源/当前正式身份、实际全文或连续区间、正常对照、失败/取消前缀、必要消费者和原有正确控制；必要局部 join 不冒称整个大文件或全部432参考/131正式文件新审通过。`reading-ledger.json`、逐pointer的 `terminal-reading-ledger.jsonl.gz` 与 `purpose-dispositions.json` 给出全部60角色的当前处置。626,398终值/空容器/文本行仅是结构分母。未将 hash、恢复、搜索、生成视图或机械检查记为语义 PASS。

大型材料采用无损精确别名与经重构相等检查的模板显示；所有新语义值均实际呈现审读。纯对象身份、完整远端身份数组和精确块编号库存保留原值及pointer，只授用途/运输身份处置，不给游戏语义或执行信用。`continued/global*`索引中的生成时点UNREAD只表示生成不授信用，其后实际阅读以001–025台账及最终总台账为准。38e78d阶段的旧未读台账完整保存在 `continued/checkpoint-38e78d/`，不抹去早先未完成状态，也不把它当当前剩余债。

五实际内容签名固定86bbc/formal ebbe；5c只核当时有限登记资格，accepted0/CLOSED0/OPEN56、108已满足边与两个未来过程门。b7随后正式接受56，4df随后关闭56。三者不是一个事件；旧false/null/PENDING字段保留其生成时点。b7/4df准确身份及有效投影已读，未声称把这些历史提交的全部文件重新阅读。`history-current-acceptance.json` 与 `continued/current-dependency-and-interface-review.json` 分别保存历史资格和本轮有限接收分析。

F002正数才限制新增，零/原始负数绕过新增上限；最终有效人数检查、等值后焦点、nil/[]返回是不同观察点。Arena存活未替换胜者的回复期2→普通尾1→取消后1与落败补位重置分别核定。U14原始字段、查找键、图像/语言、缓存/反写及存储消费者逐层保留，未把编译成功写成缓存已刷新或媒体已成功。共同接收不增加第57项。

U13准确旧FAIL `3ef4854ef43eac92fd1dc57350e4cf6aa160082b` 与修后PASS `411b563309a4e642e628dcf8289e36c6fe3fd37f` 原报告已完整恢复、实读：旧对象删除SF30-d/e正确控制及错误R5路径说明等问题保持；修后恢复控制、纠正定位和证明强度，与后续D/E实际接收分别登记。F002后置接口是允许的整合门，不是候选写集缺陷。B8的AN-M09前提和WP72§5.3导航已修正，不能继承旧GR7发现。party004原支持假说与最终反证并存，最终撤销范围不扩张。历史H10辅助spawn违例及INC-R6-001均保留；本任务spawn为0。

可得本任务有效语义未读为0，真实材料/权限阻塞为0。主审尚未接收与未读严格分列。剩余未知：原生/动态桥、媒体/地图/完整宿主与Demo、实际输入/声音/像素、真实存读档/录像和完整独立模型；本任务新增行为执行全部0 / `NOT_EXECUTED`，没有重跑旧执行脚本或新解码二进制。请求gpt-6.1-sol/ultra/default普速/Fast关闭；实际model/effort/tier/speed/Fast及平台UUID均 `UNVERIFIED`，/root仅路由名。历史18次Ruby仍为12已知exit0、4非0、2未知，17进入定义/1未载入，含无效及重复，不算18成功。

发布仅普通推送本专用分支，逐新增及保留的本任务载荷完整远端回读、mode/blob/bytes/SHA256/路径/tree对齐后才登记成功。旧fetch失败/中断及后继成功均保留。阅读实际UTC未独立捕获者仍 `UNVERIFIED_NOT_BACKFILLED`，台账生成UTC不倒填原始阅读时间。最终C/P、tree与报告目录身份由实际外部发布回执及最终响应绑定，不递归自哈希。
'''
(T/'report.md').write_text(report)
print(json.dumps({'effective_read_rows':60,'structural_units':sum(counts.values()),'statuses':counts,'contracts':56,'cases':351,'edges':110,'interfaces':3,'main_received':0},ensure_ascii=False))
