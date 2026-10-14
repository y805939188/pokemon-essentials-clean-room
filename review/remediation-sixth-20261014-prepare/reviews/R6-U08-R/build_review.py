#!/usr/bin/env python3
"""Serialize the independent manual judgments after fixed-source semantic reading."""
import datetime, hashlib, json, pathlib, subprocess

OWN=pathlib.Path(__file__).resolve().parent
REPO=OWN.parents[3]
ROOT='review/remediation-sixth-20261014-prepare/'
P='f34eb57fbd2dba4184ac2b6ab1ed7ca26e41062a'
PRE='469a268b92daed7b4d28d7fd0da75520cbb7228f'
def git(*args): return subprocess.check_output(['git',*args],cwd=REPO)
def ident(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
packet=json.loads(git('show',P+':'+ROOT+'candidates/R6-U08/evidence/id-evidence.json'))
contract=json.loads(git('show',PRE+':'+ROOT+'contracts/R6-U08.json'))
verification=json.loads((OWN/'fixed-verification.json').read_text())
readback=json.loads((OWN/'candidate-remote-readback.json').read_text())
assert readback['result']=='REMOTE_FULL_READBACK_MATCH' and readback['payload_count']==15
reasons=[
 '空槽可容纳2，普通添加完成数量后真返回；调用侧随后仍使用请求数2。',
 '唯一槽余量1先写999，未分配的1导致假；返回假跳过自动排序，调用侧无返回值分支，消息2。',
 '唯一槽已满，无法分配而假返回；调用侧仍进入数量1消息。',
 '列表非USE或空选择不进入；显式BACK0被数量正门挡住。消息失败不撤写；无限口袋另扩槽；填包直入、重要1与普通3不变。',
 '转移先完成，随后一次refresh依次地图事件和公共事件，最后清假再真返回；按这次调用计算增量。',
 '另一转移支也在同一末尾refresh会合，依赖正常时结果相同。',
 '直接置标记没有refresh调用；后续消息可miniupdate，所以只在消息更新之前断言真，而非整个效果返回前。',
 '选择取消在释放和转移前假返回；E2异常会停止后续公共事件和末尾清标记，已有E1及转移/释放保留。',
 '合格新请求由F9按住置真，后段停止条件通过即消费；call_debug先清标记再其它调用。',
 '消息标志检查早于新输入和已有调用消费，本次无新请求；不作永久结论。',
 '解释器门只包新输入分支；旧标记假时无可供后段消费的调试请求。',
 '自动移动门仅冰滑/上瀑/下瀑三状态；不是角色强制路线标记。该门真且旧标记假时无本次调试请求。',
 '输入使用elsif互斥链；早支内部拒绝不会再检测F9。',
 '新F9请求不要求停止，消费要求停止；旧标记正常保留到下一合格更新，松键不取消它。',
 '停止后先检查暂停菜单再debug；新输入的解释器/自动移动门不包后段旧请求消费。暂停本身未清debug，不推其它菜单效果无副作用。',
 '调试假只阻止新置位；先清旧请求后音效抛错不存在恢复写入，不能保证整姿/菜单到达。',
 '零差量是所有标志和I/O之前的返回，缓冲空态不变。',
 '非零符号/绝对值格式化后经共同门回显、追加、调用flush；正常I/O前提。',
 '普通日志和非零差量在共同门不通过时不接受、也不调用各自自动flush。',
 '人工缓冲只是已有状态；零值返回无清空写入，真假标志不影响此早退。',
 '显式flush写文件条件含两标志和非空，正常结束的清空在门外；与零早退不同。',
 '文件开/写异常早于清空语句；只保证已回显和追加前缀，零差量不会进入此I/O。',
 '合法非空返回短路默认确认和建议过程，先赋Bert后变更消息。',
 'Ada首片段长度3严格小于10，首字母处理后返回；查性别不决定输出。',
 '同一用户名与上限保持，只改性别仍走同一活动分支，备用随机代码不参与。',
 '等长不通过首条件；数字尾删除后8字符通过。第二例等长再回完整名小写其余后截10。正常空字符串回退仍空、不能等同异常。',
 '拒默认短路类型查询；两实际命名模式分别ESC空返回与BACK删字，不继承统一旧名返回。',
 '类型/用户名处理在赋名前，失败不到新赋名保证；赋名后消息失败没有回滚。只用假想字符串，不访问真实用户名。'
]
assert len(reasons)==28
facts=[
 '入口忽略普通添加真假，容量不足可能部分写入；反馈数量是请求数。',
 '两转移分支会合到同步事件刷新；地图事件后公共事件，最后清标记再真返回。',
 '消息公共门、新输入门、互斥检测与已有请求消费分期；F9是按住。',
 '零差量早于共同门/I/O返回，人工缓冲保留；显式flush门外清空独立。',
 '调用侧查/传性别，活动建议名不消费它，首片段与完整名的处理分支不同。'
]
counter=[
 'WP27已有部分添加不能决定这个具体消费者的请求数量消息；正文和向量补的是这个脱节。',
 '目标装配已有刷新不能替代末尾同步调用。原condition的效果返回时真并非一般成立；候选正确限直接动作后且消息更新前。',
 '地图其它门已有共享合同仍须在具体入口新请求/消费分期。角色强制路线WAIT不是自动移动三状态门，独立WP12对照未被改写。',
 '接受消息后刷新可宽泛理解，但零值独立早退必须限定共同门充分性；候选保留其余通道原规则。',
 '按性别取可只指传参，候选仍保留传参并限定实际来源；不能用设施音节规则代替活动建议名。'
]
spans=[[[124,125],[287,287]],[[60,61],[72,72]],[[33,44]],[[235,239]],[[107,110]]]
catalog_spans=[[48,51],[52,55],[56,63],[64,69],[70,75]]
hist=[
 'R1 R03数量0、R2 C010/DG-M11及R5填包向量保持；WP27普通/全有全无分开、WP17显式取消0。',
 'R1 R02返回关闭/先清理、100次落点与转移载具正常合同保持；WP11/13事件刷新新接合。',
 'R3 WP11/12/13与R4/R5末端输入精确范围保持，自动移动三状态不扩大成强制路线，迷你更新不进入末端分发。',
 'R1 R13双门/逐次输出/显式flush门外清空/异常报告不变；WP51评分消费者差量0不保证有日志。',
 'R2 C013单角色失败前提未改；WP17取消分模式与WP24初始建议名同源规则保持，设施随机名称不改。'
]
records=[]
for i,(author,original) in enumerate(zip(packet['records'],contract['scope_contracts'])):
    vs=[]
    for v in author['acceptance_and_regression']['vectors']:
        number=int(v['id'].split('-')[-1])
        vs.append(dict(id=v['id'],catalog_line=47+number,input_and_observation=v['input_and_observation'],candidate_expected=v['source_static_expected'],independent_reason=reasons[number-1],verdict='PASS_SOURCE_STATIC',evidence_level='DERIVED_VECTOR',reference_execution='NOT_EXECUTED',source_locations=original['bidirectional_evidence']['source']))
    records.append(dict(id=author['id'],verdict='PASS',minimum_required_repairs=[],
      identity_and_verdict=dict(classification='required',severity=original['identity_and_verdict']['severity'],root_cause_key=author['id'],aliases=[],contract_pointer='/scope_contracts/'+str(i),subject_commit=P,subject_candidate_tree=readback['directory_tree'],formal_accepted=False,closed=False),
      bidirectional_evidence=dict(source_locations=original['bidirectional_evidence']['source'],source_fresh_full_read=True,source_fact=facts[i],necessary_consumers='Fresh fixed source and formal join ranges in read-events.jsonl; source modes/blob/tree verified in fixed-verification.json',primary_mirror_spans=spans[i],catalog_spans=catalog_spans[i],original_non_proposer_evidence=author['bidirectional_evidence']['original_non_proposer_evidence'],negative_scope='The two fixed whole texts, six specified source files and named necessary consumers; no dynamic/native absence claim.'),
      premises_and_counterexample=dict(original_complete_contract='contracts/R6-U08.json /scope_contracts/'+str(i),input_domain=original['premises_and_counterexample']['input_domain'],ordinary_control=original['premises_and_counterexample']['ordinary_control'],counterexample=original['premises_and_counterexample']['minimal_counterexample'],failure_cancel_partial_commit=original['premises_and_counterexample']['failure_cancel_partial_commit'],current_qualifications=counter[i],execution='SOURCE_STATIC_NOT_EXECUTED'),
      minimum_revision_contract=dict(original_minimum=original['minimum_revision_contract']['rule'],actual_revised_source_fact=facts[i],body_and_catalog_coherent=True,preserved_scope=original['minimum_revision_contract']['preserve_correct_scope'],source_unmodified=True,compatibility_policy_selected=False),
      acceptance_and_regression=dict(original_conditions=original['acceptance_and_regression']['conditions_and_vectors'],independent_vectors=vs,history_assessment=hist[i],all_condition_disposition='PASS_FINITE_SOURCE_STATIC_WITH_STATED_QUALIFICATIONS',not_run=['reference','independent full model','native host','Demo','physical input','real save'],old_pass_transferred=False),
      independent_adjudication=dict(reviewer='R6-U08-R',non_author_in_this_task=True,author_task_as_delegated='01a13ab3-0896-703d-be8b-f711f0c7c01b',strongest_counterargument_and_assessment=counter[i],verdict='PASS',actual_configuration_echo='UNVERIFIED',new_reference_execution=0),
      dependencies_and_receivers=dict(primary_batch='R6-U08',original_domain_dependencies=original['dependencies_and_receivers']['original_dependencies'],author_blocking_interbatch_edges=[],receiver='R6-I',receiver_thread_as_supplied='01a13a93-d1da-71e4-a488-63b8524f503d',shared_conflicts=['R6-U06:catalog','R6-U07:catalog','R6-U09:wp72+catalog'],state='CANDIDATE_PASS_ONLY',remaining_gates=['unique-writer actual integration','shared full-file non-author review at actual integrated hashes','direct/transitive interface acceptance','precise historical regression at actual integration','formal acceptance','CLOSED registration'])) )
result=dict(schema='r6-u08-r.independent-seven-groups.v1',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),verdict='CANDIDATE_PASS',records=records,required_ids=contract['required_ids'],candidate_subject=readback,semantic_evidence_level='SOURCE_STATIC + DERIVED_VECTOR, NOT_EXECUTED',formal_accepted=False,closed=False,report='report.md',repair_count=0)
(OWN/'semantic-review.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
events=[json.loads(l) for l in (OWN/'read-events.jsonl').read_text().splitlines()]
execution=dict(schema='r6-u08-r.provenance.v1',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),logical_id='R6-U08-R',canonical_role='/root',task_uuid='UNVERIFIED',parent_source_thread_reference='01a10d94-84b9-759e-aa1d-edb0d9b6d0e2',requested=dict(model='gpt-6.1-sol',effort='ultra',tier='default',speed='default',Fast=False),effective=dict(model='UNVERIFIED',effort='UNVERIFIED',tier='UNVERIFIED',speed='UNVERIFIED'),execution_environment='ccarenv_b64_Y2NhcmVudl8wMTZlOWI2YTdiYWM4MTkxOWMxZDg1YWViMTNiNDYxOQ',cwd=str(REPO),report_branch='codex/remediation-sixth-r6-u08-review-20261014',own_write_directory=str(OWN),structured_read_capture_first_utc=events[0]['started_utc'],task_start_utc='NOT_CAPTURED_SEPARATELY',cli_model_task_launched=False,additional_agents=0,reference_execution=0,independent_full_model_execution=0,native_host_execution=0,Demo_execution=0,physical_input=0,real_save=0,real_username_read=False,early_metadata='Earlier commands retain platform echo but not a separate local stdout/stderr/UTC capture; do not reconstruct launch identity.',attempts_retained=[dict(action='cat-file/show fixed prepare and author publication before fetch',exit=128,scope='fixed objects absent locally; subsequent ordinary fetch succeeded'),dict(action='rg guessed WP12 filename',exit=2,scope='wrong filename; corrected fixed path read'),dict(action='read_fixed TextEntry 605..805',exit=1,scope='range assertion before display; fixed full payload has786 lines; corrected 605..786 read'),dict(action='oversize tool output',scope='contract/prompt metadata, combined diff, original/source and activation dumps truncated; task semantic ranges reread; unrelated activation identity arrays not claimed fully semantic')],automatic_approval_rejections=0,state='CANDIDATE_PASS_REPORT_PREPARED',integrated_pass=False,formal_accepted=False,closed=False)
(OWN/'execution-status.json').write_text(json.dumps(execution,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verdict=result['verdict'],ids=len(records),vector_rows=sum(len(r['acceptance_and_regression']['independent_vectors']) for r in records),repair_count=0),ensure_ascii=False))
