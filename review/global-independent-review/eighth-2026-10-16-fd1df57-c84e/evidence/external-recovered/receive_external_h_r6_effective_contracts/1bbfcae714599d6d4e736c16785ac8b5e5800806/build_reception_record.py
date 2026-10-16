"""Maintain explicit read versus acceptance records. Generation gives no reading credit."""
import pathlib,json,hashlib,datetime,subprocess,collections
T=pathlib.Path(__file__).resolve().parent;P=T.parents[1];R=T/'recovered'
def load(p):return json.loads(p.read_text())
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def digest(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
def ident(repo,c,p):
 b=subprocess.check_output(['git','-C',str(repo),'show',c+':'+p]);return dict(repository=str(repo),commit=c,path=p,**digest(b))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
D=load(T/'decoded-index.json');M=load(T/'recovery-manifest.json');frozen=load(T/'frozen-denominator.json')
contracts=[]
for n in range(23,37):
 role=D['roles'][n];d=load(T/role['decoded_path'])
 for j,x in enumerate(d['scope_contracts']):
  contracts.append(dict(id=x['id'],batch=d['id'],role=n,pointer='/scope_contracts/'+str(j),seven_groups=list(x),original_full_proposal_present='original_full_proposal' in x,full_object_identity=digest(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()),source_path=role['decoded_path'],original_input=role['input'],reading_status='FULL_SEVEN_GROUP_AND_ORIGINAL_READ' if x['id']=='GR6-F-002' else 'UNREAD',reception_status='PENDING_FULL_TASK_RECEPTION',source_join='BOUNDED_SOURCE_B8_CONSUMER_VERIFIED' if x['id']=='GR6-F-002' else 'NOT_REVIEWED'))
assert len(contracts)==len({x['id'] for x in contracts})==56
assert {x['id'] for x in contracts}==set(frozen['contract_ids'])
cases=[]
for n in range(19,23):
 p=R/f'recovered-r6-cases-current/tasks/R7-H{n}/assigned-14-current-reception.json';d=load(p)
 for j,rec in enumerate(d['records']):
  case_field='case_receptions' if n==19 else 'cases'
  for k,c in enumerate(rec[case_field]):
   key=f'R7-H{n}/records/{j}/{case_field}/{k}'
   cases.append(dict(key=key,parent_id=rec.get('id',rec.get('canonical_R6_id',rec.get('original_id'))),case_id=c.get('case_id',c.get('original_case_id',c.get('id'))),payload=str(p.relative_to(T)),pointer=f'/records/{j}/{case_field}/{k}',complete_case_identity=digest(json.dumps(c,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()),reading_status='FULL_CASE_READ_AND_BOUNDED_SOURCE_B8_CHECKED' if n==19 and j==5 else 'UNREAD',reception_status='PENDING_FULL_TASK_RECEPTION'))
assert len(cases)==351
assert len([x for x in cases if x['reading_status']!='UNREAD'])==7
role_notes={
6:'56/14候选、A11/B9/C19/D9/E8 actual、5c登记资格、b7接受与4df关闭是不同事件；110边为有限静态/过程门，非110运行。原执行缺陷/计数与非必修分类保留。原事件证据尚未全部独核。',
19:'AN007一般N逐次Float端点位级精度为P3 optional facet；默认控制点必修独立，不要求保留旧浮点实现、不证明像素。',
20:'BAG-04 false哨兵、UTIL-03文本域、UTIL-05有序对称差、UTIL-11常量哨兵、UTIL-12隐式回调上下文、UTIL-13温度舍入及GR6-POL-001三旧剖面均未选择；事实、未来兼容及原生选择分列。源锚未全重读。',
21:'L01地图工程、L02图像音频、L03宿主、L04原生CFG/选择、L05GPU、L06.NET图像输出、L07Windows API、L08字体渲染、L09合成、L10原生载入/译文质量、L11无界扩展、L12真实外部状态、L13元资料、L14历史执行元数据分别保持；不豁免可得未读。',
22:'完整原支持假说、普通对照、最小反例及最终相反裁决并存；最终NO_REQUIRED撤销旧Entry0跨loop遗留假说，未授全版本宿主证明。本次只读取裁决链；独立执行0。',
39:'原R6 56必修39P2/17P3、8optional/1no-required/Float另1，7policy/14limits及14批/110边有独立分母；旧R1–R5层次、INC-R6-001、历史18次尝试资格保留；作者全量覆盖声称不转本轮批准。',
40:'原14限度及恢复条件全文读取，INC-R6-001曾越界的事实不能被当前位置不存在抹去；可读材料缺读不列宿主limit。',
41:'O5/K2/CA1/F5/UI5合计18Ruby尝试，12exit0/4非0/2未知，17进入原定义/1未加载；无效Purifyv2、F重复、caught异常及tee退出分别保留；Fraction/PE/SF2解析不等行为执行。',
42:'65规范裁决/56required/8optional/1no-required、Float另1，原432/131/116/38093库存、18执行和INC事件是R6原范围摘要；全表逐56标题不授逐项原事实接收。',
47:'H10原A/B/C/D及E/5c接收是历史资格阅读，source/formal新全文0；曾spawn3并续轮2违背当时限制，根补读不能回写过程合规；原阶段false/null/pending保持。',
56:'E actual仅86bbc/formal ebbe的8项有限内容PASS；F002候选后置WP66-A门在actual具名解除。SF30 d/e、R5错误路径与工具证明强度更正保留；配置未知，public sync deferred，未接受/关闭。八项源未全部本轮独核。',
58:'5c原报告只核d353冻结登记与依赖资格；accepted0/CLOSED0/OPEN56、108静态门及2未来过程门明确。A11/B9/C19/D9/E8签名及公共表指针等不是本次新源审读；b7/4df后继需另核。',
57:'E机器裁决8项和receiver_delta明确content-only，configuration_qualified_acceptance/global/formal/CLOSED均false；后继公共登记门不能由此省略。'
}
full=set(role_notes);alias={15:6};ledger=load(T/'reading-ledger.json');entries=[]
for role in D['roles']:
 n=role['row'];entry=dict(row=n,input_identity=role['input'],decoded_path=role['decoded_path'],decoded_identity_verified=True,credit='UNREAD',full_role_read=False,complete_role_reception=False)
 if n in full:entry.update(credit='FULL_TEXT_OR_FULL_JSON_VALUE_READ',full_role_read=True,meaning=role_notes[n],display_evidence='本会话相应ROLE全文平台工具回显；原始独立UTC/stdout本地未捕获，不倒填。精确可重放值为decoded_path。',scope='历史事实/作者声称的完整阅读，不等其所有外指源、clause、消费者均独立核验。')
 elif n in alias:entry.update(credit='EXACT_SAME_TASK_CONTENT_ALIAS',full_role_read=True,alias_of=alias[n],meaning=role_notes[alias[n]],display_evidence='decoded SHA/bytes/blob完全一致；同一上下文role6全文信用只计一次。')
 elif n==35:entry.update(credit='PARTIAL_ROLE_FULL_ONE_CONTRACT_READ',full_role_read=False,read_pointer='/scope_contracts/1',meaning='F002完整七组/原提案与7案例已读；同载荷其余7合同未读，整个角色未接收。',display_evidence='完整scope_contracts[1]平台回显与inputs/F002-current-record.lossless-view.json')
 elif n==37:entry.update(credit='PARTIAL_ROLE_ONE_CURRENT_RECORD_READ',read_pointer='/records/5',meaning='仅GR6-F-002记录读取；其它55未读。')
 entries.append(entry)
ledger.update(status='INCOMPLETE',recorded_utc=now,entries=entries,full_roles_read_or_same_task_alias=len(full)+len(alias),full_unique_decoded_objects_read=len(full),complete_roles_received=0,full_contracts_read=1,bounded_case_bodies_read_and_source_checked=7,complete_contracts_received=0,complete_cases_received=0,complete_edges_received=0,complete_interfaces_received=0,behavior_execution='NOT_EXECUTED',new_reference_behavior_executions=0,limitations_do_not_include_unread=True,reading_time='Individual original reading UTC UNVERIFIED_NOT_BACKFILLED; recorded_utc is ledger generation only',truncated_displays=[dict(scope='initial combined prompt+readset',result='TRUNCATED_NO_FULL_SEMANTIC_CREDIT',repair='Task prompt and global prompt reread whole separately; readset identity fields fully mechanically validated, no game semantic credit'),dict(scope='combined roles6/19/21/39/40/41/42',result='middle truncated',repair='Roles39/40/41 separately reread whole; others whole appeared'),dict(scope='F002 H19 full pretty display',result='one middle section truncated',repair='All7 complete cases and complete remainder redisplayed with exact identical source-unit aliases; reconstruction equals original')])
save(T/'reading-ledger.json',ledger)
files=load(P/'delegation/readsets/receive_external_h_r6_effective_contracts.complete.json')
save(T/'readset-field-disposition.json',dict(schema='r8-readset-identity-purpose/v1',input=ident(P.parents[2],'40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232',str((P/'delegation/readsets/receive_external_h_r6_effective_contracts.complete.json').relative_to(P.parents[2]))),row_count=len(files['files']),fields={k:'Exact transport identity/path/purpose instruction: all values parsed, used in complete set/mode/blob/bytes/SHA validation. Not business semantic approval.' for k in files['files'][0]},all_rows_individually_verified=True,evidence='recovery-manifest.json',semantic_credit=0))
save(T/'case-index.json',dict(schema='r8-exact-case-denominator/v1',count=len(cases),by_owner=dict(collections.Counter(x['key'].split('/')[0] for x in cases)),rows=cases,generation_grants_reading_credit=False))
frozen.update(status='FROZEN_IDENTITY_AND_STRUCTURE_ONLY',recorded_utc=now,contracts=contracts,cases_index='case-index.json',verified=dict(input_files=M['count'],input_bytes=M['bytes'],target_checkout_tree=M['checkout_tree'],target_task_tree=M['target_task_tree'],decoded_roles=60,decoded_unique=52,decoded_role_bytes=D['bytes_with_roles'],contracts=56,cases=351),field_purpose_rule='All seven groups and original full proposal remain semantic. Identity/location fields get exact identity disposition only. Unread business values remain UNREAD, never typed away.')
save(T/'frozen-denominator.json',frozen)
rec=load(T/'reception-ledger.json');rec.update(status='INCOMPLETE',recorded_utc=now,payloads=entries,contracts=contracts,cases=cases,edges=[dict(index=x['index'],from_=x['from'],to=x['to'],kind=x['kind'],payload='recovered/continued/current-dependency-and-interface-review.json',pointer='/edges/'+str(i),reading_status='ONE_SCHEMA_EXAMPLE_ONLY' if i==0 else 'UNREAD',reception_status='UNRECEIVED') for i,x in enumerate(load(T/'inputs/interface-and-edge-claims.json')['edges'])],complete_role_reception=0,complete_contract_reception=0,complete_case_reception=0,complete_edge_reception=0,task_final_signoff='RESERVED_TO_PARENT')
save(T/'reception-ledger.json',rec)
print(json.dumps(dict(full_roles_read=ledger['full_roles_read_or_same_task_alias'],unique_full=ledger['full_unique_decoded_objects_read'],contracts=56,cases=351,case_read=7,full_contract_read=1,acceptance=0)))
