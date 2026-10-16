"""Freeze four non-overlapping semantic contract packets; generation grants no read credit."""
import pathlib,json,hashlib,subprocess,re,datetime
T=pathlib.Path(__file__).resolve().parents[1];O=T/'continuation';P=T.parents[1];repo=T.parents[4];R=pathlib.Path('/workspace/pokemon-essentials')
C0='ab5b6b416d1f833490772fdecacf1cd8be815d65';TARGET='a96ec67a948e3fc86b25ad407cd977b6752e2d77';B='fd1df570cad987dc3852a3b958f03916e317f7fe';RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def load(p):return json.loads(p.read_text())
def save(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def ident(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
def binding(p):return dict(path=str(p.relative_to(T)),mode='100644',**ident(p.read_bytes()))
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
D=load(T/'decoded-index.json')['roles'];frozen=json.loads(subprocess.check_output(['git','-C',str(repo),'show',C0+':'+str((T/'frozen-denominator.json').relative_to(repo))]));case_index=json.loads(subprocess.check_output(['git','-C',str(repo),'show',C0+':'+str((T/'case-index.json').relative_to(repo))]))['rows'];claims=load(T/'inputs/interface-and-edge-claims.json');recovered=load(T/'recovery-manifest.json')
mapb={'A':[1,2,4,5],'B':[6,7,8],'C':[3,9,10,11,12],'D':[13,14]}
owner={c['id']:k for c in frozen['contracts'] for k,nums in mapb.items() if int(c['batch'][-2:]) in nums}
assert len(owner)==56
current={}
for n in range(19,23):
 p=T/f'recovered/recovered-r6-cases-current/tasks/R7-H{n}/assigned-14-current-reception.json'
 for i,x in enumerate(load(p)['records']):current[x['id']]=dict(payload=binding(p),pointer='/records/'+str(i),whole_record=x)
assert len(current)==56
original={}
for n in range(23,37):
 p=T/D[n]['decoded_path'];x=load(p)
 for i,c in enumerate(x['scope_contracts']):original[c['id']]=dict(role=n,payload=binding(p),original_input=D[n]['input'],pointer='/scope_contracts/'+str(i),whole_contract=c,batch_root_fields={k:v for k,v in x.items() if k!='scope_contracts'})
optional_owner={'R6-CM-FB-01':'A','R6-UI-PARTY-003':'C','UI-ST-002':'C','GR6-F-003':'D','GR6-F-G001':'D','R6-D-FONT-C01':'D','R6-D-PBS-C08':'D','R6-C-P02':'A','R6-UI-PARTY-004':'C'}
semantic_owner=dict(owner,**optional_owner)
full_role_owner={6:'D',7:'A',8:'B',16:'A',17:'B',19:'B',20:'A',21:'D',22:'C',39:'D',40:'D',41:'D',42:'D',43:'D',45:'D',47:'D',48:'D',50:'D',52:'D',54:'D',56:'D',58:'D'}
# For keyed shared containers: all per-ID values go to the unique ID owner; all remaining root/common values have one coordinator owner D.
shared_specs={0:['unique_required_result_map','closed_batch_map'],1:['required'],2:['tasks'],3:['batches'],4:['items'],5:['edges','per_id','qualified_joint_interfaces'],18:['@list'],37:['records'],38:['normative_records','optional_records','no_required_revision_records','batch_contracts','manual_entry_prompts'],44:['EXACT_ALIAS_OF_ROLE38'],46:['per_id'],49:['records'],51:['ids'],53:['rows'],55:['per_id'],57:['per_id'],59:['per56']}
common_ownership=dict(schema='r8-reception-semantic-field-ownership/v1',frozen_support_commit=C0,target_commit=TARGET,contract_owner=owner,nonmandatory_owner=optional_owner,whole_role_owner={str(k):v for k,v in full_role_owner.items()},contract_role_owner={str(n):next(k for k,nums in mapb.items() if n-22 in nums) for n in range(23,37)},contract_batch_root_owner='Same as contract_role_owner, not common root D.',shared_role_rule='All complete per-ID/per-batch objects and their complete nested values belong to their canonical owner; exact keyed arrays listed below. Every unmatched root, metadata, common stage, common instruction or effective business field belongs to D. No value is silently excluded. Names/locators alone never confer reading.',shared_roles={str(k):dict(keyed_arrays=v,common_root_owner='D') for k,v in shared_specs.items()},exact_aliases={str(i):i-9 for i in range(9,16)},role44_alias=38,interfaces_owner='D',generated_views_owner='D for identity/alias proof; per-contract business text remains assigned to canonical owner. If any view contains new effective text not proven an exact alias, D must read it or explicitly leave it OPEN.',two_version_rule='Roles7/16 and8/17 have different current bytes and must not be replaced by a diff or old credit. Exact same-byte spans may be associated only after proof within the actual reader context.',closure='Root task final requires all four actual non-author results plus complete common residual and all three interfaces; no task-final signed by a packet.')
save(O/'semantic-ownership.json',common_ownership)
# Full original instructions, no summaries or generated omissions.
common='''# 四包共同完整合同\n\n这是剩余有效语义接收，不是整改。父线程实际派发中给出的本包冻结提交必须先固定；本文件不写自身未来commit/tree。以下原始完整指令均适用，包内具体独占写集和完整所辖对象优先限定分工范围，不改变任何正确语义/证据门。禁止自行spawn。请求gpt-6.1-sol/ultra/default普速/Fast off；实际无回显字段UNVERIFIED。必须实际不同于目标作者01a143b2-d42d-7797-8bbe-c60266de7007；读取CODEX_THREAD_ID可记录真实不同context，角色名不算。\n\n支持快照P0固定ab5b6b416d1f833490772fdecacf1cd8be815d65；原目标C固定a96ec67a948e3fc86b25ad407cd977b6752e2d77；B8/R固定见下全文。P0中的1364输入/76848323B、60角色/52gzip对象已独立恢复核验。按readset精确mode/blob/bytes/SHA复用已有惰性文件，缺失时只恢复所需准确对象到自有独占写集；不要再次下载整个仓库或新写大回执来充当阅读。旧脚本/游戏不运行。恢复文件、generated view、hash、exit0、旧PASS均reading0。\n\n每个所辖canonical ID的完整七组、原提案、父前提、所有case完整本体及独立差异、正常/取消/失败/异常/部分提交、全部参数/default/枚举、必要定义/调用者/接收者、当前B8正反条款均须实际呈现并读懂。原行范围仅定位下界，必要方法要读到完整结束行/条件。可作经重构相等核验的无损精确别名；不能把业务文字按identity/type-purpose删除。输入/输出截断保留并补读。\n\n所有原历史错误、FAIL/WAIT、撤销、反证、后继clarifier按原时点保留。没有默认caller不能免读定义，也不把内部工具自动变未来API。每疑似缺口必须给最强现跨篇已覆盖/NO_REQUIRED/out-of-scope解释；旧required、optional、Float、policy、limit、no-required分列。不得重开第七轮27、选择用户policy、实施整改、合并main或自行签B8全局PASS。新行为未执行NOT_EXECUTED，宿主/媒体限制与可得未读分别列。\n\n每对象/字段记录原始身份、读片/实际回显、完整当前含义、R/B8定位、消费者接合、判断与剩余。首批输出frozen-denominator.json、reading-ledger.json、reception-ledger.json、interfaces.json、proposal-counters.json、report.md。本任务需实际的非目标作者独立结果；任何此前同行结论只能作待审输入。P0中F002实读与此次新增K002实读仅是具名支持；不能省略新读者自己必要的完整值与消费者。\n\n历史actual五组A/B/C/D/E与本续接包A/B/C/D是不同命名空间。旧formal_review_primary_groups不得当成本包owner；例如历史Arena接收组B的C002/SE001在本续接包A，U14的历史A→C跨本包D与C。

共同接合：D负责三个接口收口；A/B/C同时给所辖贡献的完整producer事实和精确B8/source身份，D必须真正读取所有必要producer贡献后才能签consumer。允许跨包必要只读交界，但一个canonical ID只在owner包计数。不得等待无关包才推进可独立部分。接口最终门如确实缺必要结果保持OPEN；所有结果由父线程最终汇总。\n\nD独占共同残余：各共享JSON未匹配到唯一ID/批次的全部有效root/common值，五实际原报告和5c完整阶段资格、原始中文handoff的共同文字/指令及所有未证精确别名的新语义、发布身份类型用途、三接口、最终全四包累计接合。D不能凭这个角色名继承其它包实读。A独占两版matrix全文及政策；B独占两版audit全文与Float；C独占PARTY004完整NO_REQUIRED；八optional按semantic-ownership逐ID归属。角色9–15同字节别名0–6、44别名38须核精确身份，信用一次。\n\n完成必须给精确已完整接收/必要未接收/真实不可得限制和实际配置/执行；任一所辖必要对象欠缺则INCOMPLETE。只普通commit/push父派发的包分支和自有目录，不强推、不改main/tag或其它包。远端完整回读新增/变更载荷一次，核文件集合/mode/blob/bytes/SHA/tree；复用未变输入身份，不递归大回执。最终包结果只能READY_FOR_PARENT_RECEPTION或INCOMPLETE，父主审独占task-final。\n\n'''
for title,path in [('原完整全局prompt',T/'inputs/eighth-global-review-prompt.md'),('原完整专用接收prompt',T/'inputs/receive_external_h_r6_effective_contracts.md'),('完整AGENTS',T/'inputs/AGENTS.md'),('完整review-SKILL',T/'inputs/review-SKILL.md'),('原完整恢复helper（只读理解，禁止原样执行预置路径）',T/'recovered/inputs/recover_transport.py')]:
 common+='\n\n---\n\n## '+title+'\n\n'+path.read_text()+'\n'
(O/'COMMON.full.md').write_text(common)
manifest=[]
edge_owner={}
for e in claims['edges']:
 m=re.match(r'R6-U(\d\d)',e['from'])
 k=next((k for k,v in mapb.items() if m and int(m[1]) in v),'D');edge_owner[e['index']]=k
for k,nums in mapb.items():
 ids=[c['id'] for c in frozen['contracts'] if owner[c['id']]==k];selected=[dict(id=i,original=original[i],current=current[i],prior_reader_state='FULL_SEVEN_GROUP_AND_7_CASES_READ_BUT_TASK_RECEPTION_OPEN' if i=='GR6-F-002' else 'UNREAD_AT_P0') for i in ids]
 crows=[x for x in case_index if x['parent_id'] in ids];unread_ids=[i for i in ids if i!='GR6-F-002'];unread_cases=[x for x in crows if x['reading_status']=='UNREAD']
 support_roles=set([original[i]['role'] for i in ids])|{0,1,2,3,4,5,18,37,38,44,46,49,51,53,55,57,59}|{n for n,v in full_role_owner.items() if v==k}
 role_bind=[dict(role=n,decoded=binding(T/D[n]['decoded_path']),original_input=D[n]['input'],primary_scope='WHOLE_CURRENT_EFFECTIVE_CONTENT' if full_role_owner.get(n)==k else 'Complete own ID/batch objects and necessary common premises; common root owner D, unrelated IDs belong their unique owners') for n in sorted(support_roles)]
 optional=[x for x in load(T/D[18]['decoded_path']) if optional_owner[x['id']]==k]
 paths=set()
 def paths_in(x):
  if isinstance(x,dict):
   for a,v in x.items():
    if a=='path' and isinstance(v,str) and (v.startswith('reference/pokemon-essentials/') or v.startswith('Data/') or v.startswith('deliverables/final-specification-set/')):paths.add(v)
    else:paths_in(v)
  elif isinstance(x,list):
   for v in x:paths_in(v)
 for x in selected:paths_in(x['original']['whole_contract']);paths_in(x['current']['whole_record'])
 source_bind=[]
 for path in sorted(paths):
  isr=path.startswith('reference/pokemon-essentials/') or path.startswith('Data/');q=path.removeprefix('reference/pokemon-essentials/');rr=R if isr else repo;cc=RC if isr else B
  p=subprocess.run(['git','-C',str(rr),'show',cc+':'+q],capture_output=True)
  source_bind.append(dict(repository='y805939188/pokemon-essentials' if isr else 'y805939188/pokemon-essentials-clean-room',commit=cc,path=q,mode='100644',identity=ident(p.stdout) if p.returncode==0 else None,status='AVAILABLE_FIXED_BYTES' if p.returncode==0 else 'MISSING_NEEDS_NAMED_RESOLUTION',initial_locator_not_full_unit_certificate=True))
 cross=[]
 if k=='D':cross=['GR6-C-002','R6-CM-SE-001','R6-DX-COMP-002']
 rs=dict(schema='r8-effective-contract-continuation-complete-readset/v1',id='R8-HR6-PACK-'+k,source_contract_commit='40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232',support_snapshot_commit=C0,target_commit=TARGET,target_checkout_tree='b96beef6b5c613648f0246b80c275ee4b1cc0eef',target_task_tree='13da8f32ed027e052c2097ae2dd10e59c2e33233',frozen_B8=B,frozen_R=RC,original_readset=binding(T/'inputs/readset.complete.json'),verified_recovery=binding(T/'recovery-manifest.json'),decoded_index=binding(T/'decoded-index.json'),semantic_ownership=binding(O/'semantic-ownership.json'),primary_contracts=selected,primary_ids=ids,unread_at_P0_ids=unread_ids,case_object_index=crows,unread_at_P0_case_index=unread_cases,optional_complete_original_records=optional,nonmandatory_assignment=dict(Float_facet='B',policies='A',limits='D',no_required='C'),input_roles=role_bind,source_and_B8_readset=source_bind,edge_assignment=[dict(pointer='/edges/'+str(e['index']),whole_edge=e) for e in claims['edges'] if edge_owner[e['index']]==k],edge_reception_gate='Reading full edge fields does not independently satisfy underlying per-ID/shared consumer evidence; receive all required complete producer contributions first.',interfaces=claims['joint_interfaces'] if k=='D' else [],cross_boundary_complete_contracts=[dict(id=i,original=original[i],current=current[i],purpose='Necessary boundary support only; primary owner remains '+owner[i]) for i in cross],exclusive_write_set=str(T.relative_to(repo))+'/continuation/receptions/pack-'+k+'/',branch='codex/r8-receive-h-r6-pack-'+k.lower()+'-20261016',shared_sources_read_only=True,spawn_authorized=False,UPDATE_NOT_STARTED=True,counts=dict(primary_contracts=len(ids),unread_at_P0_contracts=len(unread_ids),cases=len(crows),unread_at_P0_cases=len(unread_cases),edges=len([v for v in edge_owner.values() if v==k]),interfaces=3 if k=='D' else 0),generation_semantic_credit=0)
 p=O/'readsets'/('pack-'+k+'.complete.json');save(p,rs)
 text=f'''# 非作者有效语义续接包 {k}\n\n本包唯一主责批次：{', '.join('R6-U%02d'%n for n in nums)}。唯一canonical集合：{', '.join(ids)}。\n\n本包主责{len(ids)}合同/{len(crows)}完整cases，其中P0快照尚未全文{len(unread_ids)}合同/{len(unread_cases)}cases；F002已有有界读取只在D保留为独立的收口责任，不新增第57根因。完整原合同/完整父前提及完整case对象均在 `readsets/pack-{k}.complete.json` 内嵌；JSON所有字段须读，不能只读本段列表。\n\n唯一写集：`{rs['exclusive_write_set']}`；专用分支 `{rs['branch']}`，仅普通发布自身目录。当前父接收器/其它包/主审目录一律只读。必须先完整读该readset、本prompt全部共同合同及 `semantic-ownership.json`；再冻结本包每个语义对象/完整字段用途，逐项实读接收。\n\n边主责索引：{', '.join(str(e['index']) for e in claims['edges'] if edge_owner[e['index']]==k)}。边的全字段已内嵌，须核原阶段、有限static/process门和必要真实producer/consumer；不将“SATISFIED”字段或byte恢复当本轮接受。\n\n'''
 if k=='D':text+='''三个接口均由D负责最后完整接合：F002 E→D；Arena V004 E→B，明确Disabled身份前门和Charge清理与recharge不同；U14 A→C，原始默认/编译/查找键/图片/语言/缓存/反写/存储逐层区分。必要跨包完整合同已作为只读boundary support内嵌；全部相应源/当前B8完整必要条款必须真实读到位。共同root字段和原报告的后继资格未读时保持OPEN，不等无关结果才推进。\n\n'''
 else:text+='''向D交付本包每个相关producer事实及精确R/B8/消费者、读片、前提、正常/取消/失败/部分提交及未决；必要消费者不可只给标题或locator。若与另外包同根因，只给唯一owner加接收关系，不重计canonical。\n\n'''
 (O/'prompts').mkdir(exist_ok=True);(O/'prompts'/('pack-'+k+'.full.md')).write_text(text+common)
 manifest.append(dict(id=rs['id'],packet=k,batches=nums,primary_ids=ids,counts=rs['counts'],prompt=binding(O/'prompts'/('pack-'+k+'.full.md')),readset=binding(p),exclusive_write_set=rs['exclusive_write_set'],branch=rs['branch'],state='FROZEN_NOT_DISPATCHED',actual_reviewer_uuid='UNVERIFIED_NOT_CREATED_BY_THIS_AGENT'))
assert sum(x['counts']['primary_contracts'] for x in manifest)==56
assert sum(x['counts']['unread_at_P0_contracts'] for x in manifest)==55
assert sum(x['counts']['cases'] for x in manifest)==351
assert sum(x['counts']['unread_at_P0_cases'] for x in manifest)==344
assert sum(x['counts']['edges'] for x in manifest)==110
assert len({i for x in manifest for i in x['primary_ids']})==56
save(O/'dispatch-manifest.json',dict(schema='r8-effective-contract-four-packet-dispatch/v1',recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),support_snapshot_commit=C0,target_commit=TARGET,task_final_state='INCOMPLETE_UNTIL_REAL_NONAUTHOR_RESULTS_AND_ALL_COMMON_INTERFACES_RECEIVED',packets=manifest,exact_nonoverlap=True,primary_total=56,unread_contract_total_at_P0=55,case_total=351,unread_case_total_at_P0=344,edge_total=110,interface_total=3,spawned_here=0,dispatched_here=0,parent_must_supply_immutable_packet_freeze_commit=True,common_ownership=binding(O/'semantic-ownership.json'),full_common_prompt=binding(O/'COMMON.full.md'),aggregation_rules=['Each canonical root has exactly one primary owner; boundary reads do not add roots.','Preserve case identities as owner/record/case pointers, not only repeated human IDs.','Combine actual complete object/field scopes and exact aliases; no sum of file/case/terminal populations as PASS denominator.','A/B/C producer contributions and D consumers must really be read; unreceived dependencies remain named OPEN.','All common residual fields/whole reports assigned in semantic-ownership; no unassigned business value is treated as identity.','Only parent can sign final task; packet READY is not B8 global PASS or NO_REQUIRED_UPDATE.','P0 snapshot unread counts are frozen intake. Later continuation evidence is separately dated; never silently remove a packet obligation because a prior reader supplied a note.']))
print(json.dumps(dict(packets=[dict(id=x['id'],counts=x['counts']) for x in manifest],spawned=0,dispatched=0,semantic_credit_from_generation=0),ensure_ascii=False))
