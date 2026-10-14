#!/usr/bin/env python3
"""Record author evidence and bounded historical identities, never execute R."""
import json,hashlib,datetime,subprocess
from pathlib import Path
E=Path(__file__).resolve().parent
B=E.parents[2]
REPO=B.parents[1]
C=json.loads((B/'contracts/R6-U05.json').read_text())
def write(name,obj): (E/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def ident(b): return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def canon(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def ptr(obj,p):
 for key in p.strip('/').split('/'):
  key=key.replace('~1','/').replace('~0','~')
  obj=obj[int(key)] if isinstance(obj,list) else obj[key]
 return obj
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
ledger=[json.loads(x) for x in (E/'reading-ledger.jsonl').read_text().splitlines()]
wp='deliverables/final-specification-set/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md'
if not any(x['kind']=='formal' and x['path']==wp and x['range']==[1,105] for x in ledger):
 b=(REPO/wp).read_bytes()
 ledger.append({'utc':'NOT_CAPTURED','recorded_utc':now,'kind':'formal','path':wp,'commit':C['frozen_main'],'identity':ident(b),'range':[1,105],'line_count':len(b.splitlines()),'level':'SOURCE_STATIC','emitted_complete_range':True,'receipt':'Earlier complete direct tool read before read.py was created; timestamp not reconstructed.'})
(E/'reading-ledger.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in ledger))
extra=json.loads((E/'additional-readset.json').read_text())
for x in extra:
 x['read_ranges']=[r['range'] for r in ledger if r['kind']=='source' and r['path']==x['path']]
 assert x['read_ranges']
 x.pop('read_range',None)
write('additional-readset.json',extra)
# Exact qualification containers only, recovered whole payloads for identity/JSON pointers.
bind=json.loads((E/'historical-input-bindings.json').read_text())
scopes=json.loads((E/'selected-historical-scopes.json').read_text())
loaded={};files=[]
for p,v in bind['files'].items():
 local=Path('/tmp/r6-u05-'+Path(p).name);raw=local.read_bytes()
 assert ident(raw)=={k:v[k] for k in ['bytes','sha256','git_blob']}
 loaded[p]=json.loads(raw)
 files.append({'commit':v['commit'],'path':p,**ident(raw),'level':'TOOL_VALIDATION','result':'EXACT_PAYLOAD_IDENTITY','semantic_read':'41 selected qualification containers only; not all multi-MB records'})
checked=[]
for selected,original in zip(scopes,bind['selected_records']):
 v=selected['bound_identity'];got=ptr(loaded[v['path']],v['pointer'])
 assert got==selected['qualification'] and canon(got)==v['record_sha256']
 frozen=original['frozen_record'];assert canon(ptr(loaded[frozen['path']],frozen['pointer']))==frozen['record_sha256']
 checked.append({'id':selected['id'],'record_key':selected['record_key'],'owner':selected['owner'],'binding':v,'result':'EXACT_RECORD_AND_QUALIFICATION_IDENTITY','semantic_disposition':'AUTHOR_READ_QUALIFIED_SCOPE_ONLY_NO_VERDICT_TRANSFER'})
write('historical-verification.json',{'utc':now,'level':'TOOL_VALIDATION','files':files,'records':checked,'full_containers_read':41,'read_index_ranges':[[0,4],[5,8],[9,9],[10,12],[13,17],[18,22],[23,28],[29,34],[35,40]],'read_utc':'NOT_CAPTURED','partial_output_recovery':'Truncated first 0–9 output was supplemented by complete 5–8 read; all selected containers finally emitted in full.','boundary':'Path association is a navigation aid. Only current behavior/span qualified scope is compared; no whole-ID, R1–R5 or runtime reapproval.'})
ivs=json.loads((E/'input-validation.json').read_text())['evidence']
receipts=[]
for v in ivs:
 p=B/v['local_path'];b=p.read_bytes();assert ident(b)=={k:v[k] for k in ['bytes','sha256','git_blob']}
 receipts.append({'evidence_id':v['evidence_id'],'commit':v['commit'],'path':v['path'],'local_path':v['local_path'],'identity':ident(b),'semantic_read':'FULL_ORIGINAL_COUNTEREVIDENCE','utc':'NOT_CAPTURED','verdict':'NO_NEW_INDEPENDENT_REVIEW','scope':'Original counter evidence scope retained; unrelated FB/C records are read-only context, not new author IDs.'})
covered=[]
for p in C['candidate_formal_paths']:
 b=(REPO/p).read_bytes();n=len(b.splitlines());ranges=[x['range'] for x in ledger if x['kind']=='formal' and x['path']==p]
 assert set(range(1,n+1))<=set(k for a,z in ranges for k in range(a,z+1))
 covered.append({'path':p,'identity':ident(b),'complete_lines':n,'full_read_ranges':ranges,'result':'COMPLETE_FORMAL_READ'})
for x in C['scope_contracts']:
 for v in x['bidirectional_evidence']['source']:
  p=v['payload_identity']['path'];loc=v['locator'];a,z=loc.get('range',[loc.get('start'),loc.get('end')])
  assert set(range(a,z+1))<=set(k for r in ledger if r['kind']=='source' and r['path']==p for k in range(r['range'][0],r['range'][1]+1))
write('reading-completion.json',{'utc':now,'prompt':json.loads((E/'execution-snapshot.json').read_text())['prompt_read'],'contract':{'path':'contracts/R6-U05.json','identity':ident((B/'contracts/R6-U05.json').read_bytes()),'read':'FULL; embedded JSON and standalone contract checked equal'},'formal':covered,'source':'All four contract source locator ranges covered by complete emitted reader ranges. Full files only where ledger spans cover whole file.','counterevidence':receipts,'historical':'R6-H 55-line report, R1–R3 and R4–R5 reports fully read; selected 41 bound qualification containers fully read; 38 legacy relation rows, 33 current R5 rows and 3 own WP40 R4 projected paths read. Multi-MB history payloads parsed for identity and exact selected pointers; no whole-history semantic-read claim.','execution':{'reference':0,'behavior_model':0,'host_demo':0},'configuration_actual':'UNVERIFIED'})
V=json.loads((E/'validation-results.json').read_text())
files=V['candidate_files']; by={x['formal_path'].split('final-specification-set/')[1]:x for x in files}
plans={
'R6-CM-SE-001':{
 'rule':'Charge 在完整尾正值递减，另在实际到达行动末清理时恰1清0、2保留；清理早于号令/舞者，与招式属性及实际伤害成功无关。',
 'paths':['pokemon-rules/wp44-statuses-stat-stages-and-immunities.md','pokemon-rules/wp44-effect-coverage.md','combat-requirements/wp40-commands-obedience-and-action-order.md','test-catalog/pokemon-rules-wp43-44-46-48-50.md'],
 'clauses':['WP44 §4、K02、§8','WP40 §5.2 步18','WP44覆盖 K02'],'vectors':['SS43','SS44','SS45','SS46','SS47'],
 'counter':'1 在首次普通电招后清0，后来合法号令不再读取Charge因子2；不是普通尾递减就足够。',
 'controls':'建立2同一行动保留、完整尾2→1、非电/落空仍到清理则1→0。实际消费时才要求最近普通/最近使用为THUNDERBOLT。',
 'failure':'清理写点前故障不补完成；写0后故障保留0，先前伤害/PP/历史不回滚。',
 'consumers':'WP43伤害倍数与WP42尾递减正文原本正确，已只读；WP40顺序、WP44建立/时效/覆盖和新目录同步。号令普通入口/真实PP资格保持。',
 'history':'R5 JXN/调用普通PP与历史前缀、R2 B09普通动作历史与B11调用规则保留；既有SS与MA/SB行原样。'},
'R6-CM-SE-002':{
 'rule':'牙类实际进入内部且概率正时，异常资格先于该异常内部抽取；畏缩另抽，精神力在提交时拒，不能撤销抽取。',
 'paths':['pokemon-rules/wp44-statuses-stat-stages-and-immunities.md','pokemon-rules/wp44-effect-coverage.md','test-catalog/pokemon-rules-wp43-44-46-48-50.md'],
 'clauses':['WP44 §6 牙类行','WP44覆盖 状态目录入口'],'vectors':['SS48','SS49','SS50','SS51','SS52'],
 'counter':'THUNDERFANG对当前电目标，异常资格拒，不消费5；畏缩消费5命中，仅1次内部抽取，99留后继。',
 'controls':'可麻目标抽5并提交、再抽99不畏缩；加精神力仍抽5但拒畏缩；替身/内部0/普通外层强行或鳞粉分别界定。LUMBERRY提交/治愈/消费发生在后续畏缩抽取之前。',
 'failure':'外层未进入不造内部抽取；内部0只是假定已到入口的条件化向量，不宣称普通外层可跨同一鳞粉。先前伤害/PP/历史和即时治疗前缀保持。',
 'consumers':'WP43概率修正及外层101已只读，未把内外抽取合并；WP44资格、畏缩提交、覆盖和新目录同步，即时治愈/物品消费读取固定R消费者。',
 'history':'R2 B10完整65升降表与SS38–42、R5 M07/M08域内限定及所有旧异常/能力向量保留；不改总效果数。'},
'R6-CM-SE-003':{
 'rule':'睡眠/冰冻条款队伍扫描只加在专用入口；精神转移直接通用查询仍受其它免疫/场地/目标前门；目标提交及反应后才治疗用户。',
 'paths':['pokemon-rules/wp44-statuses-stat-stages-and-immunities.md','pokemon-rules/wp44-effect-coverage.md','combat-requirements/wp47-a-move-attributes-targeting-and-calling.md','test-catalog/pokemon-rules-wp43-44-46-48-50.md'],
 'clauses':['WP44 §3.2、§6 精神转移行','WP47-A §6.1 梦话候选','WP44覆盖 状态目录入口'],'vectors':['SS53','SS54','SS55','SS56','SS57','SS58','SS59'],
 'counter':'合法真睡U的普通梦话外壳2→1/PP5→4，再特殊调用唯一合格精神转移；T同侧已有真睡后备，专用睡眠条款拒而通用转移可提交新时长3。',
 'controls':'专用条款拒；移除已有后备睡眠两入口均过；电场仍拒通用；CHESTOBERRY先目标提交/治疗/消费，再治疗U。原精神转移槽PP10保持。',
 'failure':'目标状态及外壳递减/PP已写而反应尚未正常返回时，不补用户治疗；冰冻SS59只证明已到入口差异，不声称普通冻结用户能发动。',
 'consumers':'WP47-A梦话池/选择/特殊调用必要桥梁补写，其它候选门原样；WP40跳后段状态门、PP与历史已只读并保持；状态写持久副本和即时治疗/物品消费链固定R读取。',
 'history':'R2 B09条款键/消费者包装限定、B11调用/PP、R5原调用与状态记录限定保留；SleepTalk旧资格段只加有界消费者句，不删除原文。'},
'R6-CM-CALL-01':{
 'rule':'初次非幽灵CURSE用User空列表；普通整招前门后PROTEAN/LIBERO改幽灵时清预选重新构造对手，后期不再重定向，后续目标成功门仍可拒。',
 'paths':['combat-requirements/wp47-a-move-attributes-targeting-and-calling.md','combat-requirements/wp47-b-switching-control-and-item-changes.md','combat-requirements/wp40-commands-obedience-and-action-order.md','combat-requirements/wp49-ability-phase-triggers.md','test-catalog/combat-requirements-wp47-ab.md'],
 'clauses':['WP47-A §5.1','WP47-B §3.1 Curse行','WP40 §5.2 步14','WP49 PROTEAN/LIBERO行'],'vectors':['MA-T11','MA-T12','MA-T13','MA-T14','MA-T15','MA-T16'],
 'counter':'L普通双打：U纯WATER有效PROTEAN/CURSE/HP101，FOLLOWME席1而重建固定席3；晚变GHOST后施咒席3，PP4/HP51，未再吸到席1。',
 'controls':'只改起始GHOST则初次正常重定向席1；只移有效PROTEAN则自身速−1攻防+1/无HP代价；只饱和三项则整招拒在改类型之前。',
 'failure':'只改席3已咒则晚目标拒但PP/历史/GHOST已提交；施咒后HP写前故障保持咒真/HP101，不补HP51/后继；写后故障保留已扣前缀。',
 'consumers':'同步WP40时序、WP47-A构造/重定向、WP47-B最终目标/HP顺序、WP49类型转换与目录。默认Gen8及GENGAR/SkillSwap/Soak状态取得仅作合法夹具依据，不执行获取链。',
 'history':'R2 B11/B019当前动态类别与实际列表长度区别、起始幽灵正常跟我来、广域战力反向边界保持；MA-T07–10类型稳定前提原样；R5不授同轮错误恢复。'}
}
groupkeys=['identity_and_verdict','bidirectional_evidence','premises_and_counterexample','minimum_revision_contract','acceptance_and_regression','independent_adjudication','dependencies_and_receivers']
results=[]
for i,x in enumerate(C['scope_contracts']):
 plan=plans[x['id']]
 notes={
 'identity_and_verdict':{'author_status':'SPECIFICATION_REVISED_STATIC_EVIDENCE_READY','severity':'P2_REQUIRED_SCOPE_UNCHANGED','candidate_pass':'NOT_AUTHORED_PENDING_INDEPENDENT_ULTRA'},
 'bidirectional_evidence':{'clauses':plan['clauses'],'candidate_payloads':[by[p] for p in plan['paths']],'source_reads':'reading-ledger.jsonl (all required source locator ranges covered)','necessary_consumers':plan['consumers'],'original_negative_and_counter_evidence':'reading-completion.json; fixed records retained, no broader negative-search claim'},
 'premises_and_counterexample':{'complete_fixture_and_preconditions':'New catalog rows and common C/F/P/L premises in candidate payload; original frozen input_domain below retained','minimal_counterexample':plan['counter'],'ordinary_controls':plan['controls'],'failure_cancel_partial_commit':plan['failure'],'levels':{'source':'SOURCE_STATIC','vectors':'DERIVED_VECTOR_NOT_EXECUTED','tools':'TOOL_VALIDATION','isolated_reference':0,'independent_behavior_model':0,'host_demo':0}},
 'minimum_revision_contract':{'implemented_rule':plan['rule'],'paths':[by[p]['candidate_path'] for p in plan['paths']],'scope':'Only eight allowlisted mirrors and own evidence; original correct clauses/rows kept; no engine implementation'},
 'acceptance_and_regression':{'vectors':plan['vectors'],'tool_result':'validation-results.json: 429 finite identity/text/preservation checks, not gameplay execution','historical_scope':plan['history'],'historical_evidence':['historical-verification.json','historical-relations.json','legacy-qualified-relations.json','r4-qualified-relations.json'],'disposition':'AUTHOR_STATIC_MATCH_TO_REQUIRED_MINIMUM; independent candidate verdict and integrated acceptance pending'},
 'independent_adjudication':{'original_non_proposer_adjudication':'Frozen accepted proposal/counterevidence below is preserved as input only','new_candidate_reviewer':'PENDING_NON_AUTHOR_R6-U05-R_ultra','self_signed_independent_pass':False},
 'dependencies_and_receivers':{'blocking_author_dependencies':[],'unresolved_semantic_blockers':[],'integration_receiver_thread':'01a13a93-d1da-71e4-a488-63b8524f503d','shared_formal_write':'Sole integrator after isolated candidate review; no direct formal/public-ledger writes','review_requirement':'Parent appoints independent ultra reviewer after candidate publication','actual_configuration':'UNVERIFIED; requested gpt-6.1-sol/xhigh/default; no model-proving CLI or extra agent'}
 }
 results.append({'id':x['id'],'original_scope_contract_binding':{'path':'contracts/R6-U05.json','pointer':f'/scope_contracts/{i}','canonical_sha256':canon(x)},'seven_groups':{k:{'frozen_input':x[k],'author_evidence':notes[k]} for k in groupkeys}})
write('author-results.json',{'logical_id':'R6-U05-A','utc':now,'state':'AUTHOR_CANDIDATE_READY_FOR_NON_AUTHOR_REVIEW','prepare_commit':'469a268b92daed7b4d28d7fd0da75520cbb7228f','formal_main':C['frozen_main'],'reference_R':C['frozen_reference'],'requested_configuration':C['author'],'actual_configuration':'UNVERIFIED','per_id':results,'remaining':{'semantic_blockers':[],'independent_ultra_review':'PENDING_PARENT_ASSIGNMENT','formal_integrated_acceptance':'NOT_REQUESTED_FROM_AUTHOR','reference_model_host_execution':0}})
print(json.dumps({'reading':'8 full formal files; all contract R locators; 7 full counters; 41 historical qualification containers','historical_record_hashes_verified':len(checked),'per_id_seven_groups':len(results),'tool_checks':len(V['checks']),'execution_reference_model_host':0},ensure_ascii=False))
