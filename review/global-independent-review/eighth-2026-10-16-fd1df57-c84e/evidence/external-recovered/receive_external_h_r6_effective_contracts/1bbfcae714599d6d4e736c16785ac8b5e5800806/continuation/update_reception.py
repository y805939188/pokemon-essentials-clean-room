"""Record only the concrete additional reading performed in this context."""
import pathlib,json,subprocess,hashlib,datetime,collections
T=pathlib.Path(__file__).resolve().parents[1];O=T/'continuation';repo=T.parents[4];R=pathlib.Path('/workspace/pokemon-essentials');B='fd1df570cad987dc3852a3b958f03916e317f7fe';RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def load(p):return json.loads(p.read_text())
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def identity(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
roles=load(T/'decoded-index.json')['roles'];original=load(T/roles[23]['decoded_path'])['scope_contracts'][1];current_doc=T/'recovered/recovered-r6-cases-current/tasks/R7-H19/assigned-14-current-reception.json';current=load(current_doc)['records'][13];assert original['id']==current['id']=='GR6-K-002'
sources=[('R','Data/Scripts/001_Technical/001_Debugging/004_Validation.rb',[[1,31]]),('R','Data/Scripts/014_Pokemon/005_Pokemon_Owner.rb',[[1,73]]),('R','Data/Scripts/014_Pokemon/001_Pokemon.rb',[[838,849],[1159,1227]]),('R','Data/Scripts/015_Trainers and player/001_Trainer.rb',[[1,9],[169,194]]),('R','Data/Scripts/015_Trainers and player/004_Player.rb',[[1,14]]),('B','deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md',[[164,179],[242,261],[340,355]]),('B','deliverables/final-specification-set/test-catalog/creature-rpg-wp18-20-24-25-26.md',[[22,48]])]
source_rows=[]
for which,path,ranges in sources:
 rr=R if which=='R' else repo;c=RC if which=='R' else B;b=subprocess.check_output(['git','-C',str(rr),'show',c+':'+path]);assert b==(rr/path).read_bytes()
 source_rows.append(dict(repository=str(rr),commit=c,path=path,mode='100644',**identity(b),actual_read_ranges=ranges,whole_file_read=path.endswith('004_Validation.rb') or path.endswith('005_Pokemon_Owner.rb'),reading_evidence='本续轮对应cat/sed平台回显；独立原始阅读UTC未另捕获，不倒填。'))
facts=[dict(id='K002-01',meaning='校验先消费以参数值为键的条件集合，普通同值键后项条件保留；非String名字若与后项Integer性别/语言相同，可能不再检查String；不是任意错型都绕过。',ordinary='(0,Valid,0,2)正常接受；(0,0,0,2)/(1,0,0,2)存整数名0',counter='(1,0,1,2)与(0,0,1,2)均拒，只有与前项id同值不能遮蔽后写String条件',scope='普通整数/文本，无自定义hash/equality、插件或额外输入验证'),dict(id='K002-02',meaning='构造器先完整校验后四字段赋值；条件仍检查且失败时尚未赋四字段。单字段name写入独立校验，在变更前拒0并保留Valid；正常写New成功。',cancel='无交互取消入口；不新增统一事务或真实存档保证'),dict(id='K002-03',meaning='个体完整创建方法接收已有Owner对象时按原引用使用，不递归校验其内部name；整个创建其它依赖成功/返回前提单独保留，不签畸形值任意下游。owner=也只校验Owner身份。'),dict(id='K002-04',meaning='外来构造language省略默认2，直接构造给3保3；训练家现有language7由new_from_trainer复制，不因UI或宿主语言重新映射。Trainer初始化读取宿主是另一步。',scope='只保固定参数/读取顺序，不新运行宿主映射或名字界面/PBS输入。')]
save(O/'K002-independent-reception.json',dict(schema='r8-k002-additional-bounded-reading/v1',status='COMPLETE_CONTRACT_AND_FOUR_CASE_BODIES_READ_BOUNDED_SOURCE_B8_JOIN_VERIFIED',whole_original_contract=original,whole_current_record=current,sources=source_rows,facts=facts,strongest_no_required='B8 WP18§6.1/§9及CI29–31完整保留同值构造例外、前项/后项区别、写入失败前缀和未来兼容未决；不能按R6旧全称失败句提出新必修。正常输入域和直接畸形构造例外并存。',future_policy='NOT_SELECTED',behavior_execution='NOT_EXECUTED',historic_execution='原R6-K tee0不是Ruby底层退出；未捕获UTC/patch不倒填；原R6-O独立执行不补齐R6-K元数据。本次未重跑原脚本。',complete_task_reception=False,remaining_history='A原实际完整报告/structured verdict与全部共同阶段/必要反证原件仍需按包A/D收齐，不能用本定向核对替整个task-final。',new_formal_required_proposal=False))
edge_role=load(T/roles[5]['decoded_path']);edges=edge_role['edges'];views=O/'edge-reading';edge_rows=[]
for e in edges:
 i=e['index'];group='candidate' if i<28 else 'shared' if i<107 else 'actual' if i==107 else 'accept' if i==108 else 'closed'
 reason={'candidate':'完整读取候选作者→非作者和非作者→唯一整合者门；候选接收不同正式接受。原候选与报告身份只作具名身份库存，不授其中业务通过。','shared':'完整读取该批到具名正式文件的贡献接收门，blocking_closure真/author假；mode明确变更贡献或只读/基线镜像。仍欠实际贡献的完整业务接收，不能凭identity升格。','actual':'完整读取五actual固定组共同门：56唯一ID、配置certificate false；不是新增一次全局语义审查。五原报告/56事实未齐，当前接受仍OPEN。','accept':'完整读取5c仅有限登记资格，b7真实accepted56/CLOSED0事件另列；不是运行或配置证书；本次不冒签原全部依赖满足。','closed':'完整读取b7接受后最后CLOSED登记门与准确时点/56原合同scope；该过程门不把未知宿主/可得未读关闭。'}[group]
 edge_rows.append(dict(index=i,whole_original=e,display='continuation/edge-reading/edges-%02d.jsonl'%(i//28),line_in_display=i%28+1,reading='FULL_EFFECTIVE_EDGE_FIELDS_READ_WITH_EXACT_TYPED_IDENTITY_DISPOSITION',semantic_meaning_and_limit=reason,underlying_identity_recovery='Original candidate/actual nested IDs are exact claims preserved in the alias inventory; not freshly fetched per-candidate source evidence.',complete_semantic_reception='OPEN_UNTIL_COMPLETE_PRODUCER_SHARED_FACTS_AND_STAGES_RECEIVED'))
save(O/'edge-reading/reading-ledger.json',dict(schema='r8-110-edge-field-reading/v1',reader='01a14466-155c-72ec-8a9a-e5ecde63f004',original_role=5,edge_count=110,read_full_effective_fields=110,complete_edges_received=0,identity_alias_definition='exact-identities.json',pure_identity_fields_purpose='每个alias的原完整值/pointer可逆保存；仅分类/身份用途处置，不作旧候选新远端恢复或游戏语义批准。',outer_author_claims='display-legend.json，所有110相同fresh_read/adjudication/basis/main_reception值已全文读，不继承其作者自验结论。',ranges=[dict(display='edges-%02d.jsonl'%j,index_range=[j*28,min(109,j*28+27)],full_platform_display=True,truncated=False) for j in range(4)],rows=edge_rows))
# Current cumulative states; initial P0 snapshot remains recoverable at its immutable commit.
reading=load(T/'reading-ledger.json');reading['full_contracts_read']=2;reading['bounded_case_bodies_read_and_source_checked']=11;reading['full_edge_fields_read']=110;reading['continuation_evidence']=['continuation/K002-independent-reception.json','continuation/edge-reading/reading-ledger.json'];reading['current_status']='INCOMPLETE';reading['updated_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
for e in reading['entries']:
 if e['row']==23:e.update(credit='PARTIAL_ROLE_FULL_K002_CONTRACT_READ',read_pointer='/scope_contracts/1',meaning='K002完整七组/原提案与4完整case及必要R/B8实际新核；同载荷其它2合同未读。')
 if e['row'] in [5,14]:e.update(credit='PARTIAL_ROLE_ALL110_EDGE_FIELDS_READ',read_pointer='/edges',meaning='110边全部有效字段已实际读；56 per_id及其它root未全文，整个角色不计完成。')
 if e['row']==37:e.update(credit='PARTIAL_ROLE_TWO_CURRENT_RECORDS_READ',read_pointers=['/records/5','/records/13'],meaning='F002与K002两条完整当前记录已读；其它54未读。')
save(T/'reading-ledger.json',reading)
rec=load(T/'reception-ledger.json')
for c in rec['contracts']:
 if c['id']=='GR6-K-002':c.update(reading_status='FULL_SEVEN_GROUP_AND_ORIGINAL_READ',source_join='BOUNDED_SOURCE_B8_CONSUMER_VERIFIED')
for c in rec['cases']:
 if c['parent_id']=='GR6-K-002':c['reading_status']='FULL_CASE_READ_AND_BOUNDED_SOURCE_B8_CHECKED'
for e in rec['edges']:e['reading_status']='FULL_EFFECTIVE_EDGE_FIELDS_READ_WITH_EXACT_TYPED_IDENTITY_DISPOSITION';e['reading_evidence']='continuation/edge-reading/reading-ledger.json#/rows/'+str(e['index'])
rec['payloads']=reading['entries'];rec['updated_utc']=reading['updated_utc'];save(T/'reception-ledger.json',rec)
ci=load(T/'case-index.json')
for c in ci['rows']:
 if c['parent_id']=='GR6-K-002':c['reading_status']='FULL_CASE_READ_AND_BOUNDED_SOURCE_B8_CHECKED'
save(T/'case-index.json',ci)
fd=load(T/'frozen-denominator.json')
for c in fd['contracts']:
 if c['id']=='GR6-K-002':c.update(reading_status='FULL_SEVEN_GROUP_AND_ORIGINAL_READ',source_join='BOUNDED_SOURCE_B8_CONSUMER_VERIFIED')
fd['denominator_frozen_identity_unchanged']=True;save(T/'frozen-denominator.json',fd)
remaining=load(T/'remaining-work.json');remaining['full_contract_read_remaining']=[c for c in rec['contracts'] if c['reading_status']=='UNREAD'];remaining['full_case_read_remaining']=[c for c in rec['cases'] if c['reading_status']=='UNREAD'];remaining['full_edges_read_remaining']=[];remaining['edge_underlying_reception_remaining']=rec['edges'];remaining['full_role_read_remaining']=[dict(row=e['row'],path=e['decoded_path'],input=e['input_identity'],current_credit=e['credit'],read_pointer=e.get('read_pointer')) for e in reading['entries'] if not e['full_role_read']];remaining['continuation_packets']='continuation/dispatch-manifest.json';remaining['snapshot_counts_note']='Dispatch packets freeze P0 unread55/344; latest local additional K002 reading gives54/340. Packet responsibility is unchanged; generation never grants credit.';save(T/'remaining-work.json',remaining)
fail=load(T/'tool-failures.json');new=dict(tool='continuation K002 source location search',observed_exit='rg error in compound command; individual final shell exit0 does not cancel it',error='Assumed Data/Scripts/013_Trainer directory does not exist',action='Used rg --files and found fixed 015_Trainers and player; read exact relevant definitions after recovery',source='platform output',actual_original_utc='UNVERIFIED_NOT_BACKFILLED')
if new not in fail:fail.append(new)
save(T/'tool-failures.json',fail)
print(json.dumps(dict(cumulative_contracts_full_read=2,cumulative_cases_full_read=11,all_edge_fields_read=110,complete_reception=0,remaining_contracts_full_read=len(remaining['full_contract_read_remaining']),remaining_cases_full_read=len(remaining['full_case_read_remaining'])),ensure_ascii=False))
