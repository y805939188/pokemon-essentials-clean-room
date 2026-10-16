"""Assemble this reader's reports from its own receipts; no reference execution."""
from pathlib import Path
import collections, datetime, hashlib, json, os, subprocess

T = Path(__file__).resolve().parent
REPO = Path('/workspace/pokemon-essentials-clean-room')
PREFIX = T.relative_to(REPO).as_posix()
PARENT = T.parent.parent
BASE = '1b46a33526f086241c765b700155c5406a86f65e'
CONTRACT = '64cfde5aa3f6b25adc7291b2c2e880d87baf1ebd'
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
C2 = '4580645dfbfec4a3c7ccbad56ae293cc619b0d25'
TARGET = '967b90fac83a6b0c3313087d8871312b4eac18b9'
CONTEXT = '01a1448b-49c1-72b6-b6ed-c8a724535018'
assert os.environ.get('CODEX_THREAD_ID') == CONTEXT
UTC = datetime.datetime.now(datetime.timezone.utc).isoformat()

def load(n): return json.loads((T/n).read_text())
def write(n, x): (T/n).write_text(json.dumps(x, ensure_ascii=False, indent=2)+'\n')
def enc(x): return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
def sha(x): return hashlib.sha256(x).hexdigest()
def git(*args): return subprocess.check_output(['git',*args],cwd=REPO)
def identity(b):
    return dict(bytes=len(b),sha256=sha(b),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
def runs(seq):
    out=[]
    for i in sorted(set(seq)):
        if out and i==out[-1][1]+1: out[-1][1]=i
        else: out.append([i,i])
    return out

assert git('branch','--show-current').decode().strip() == 'codex/r8-c2-reception-b-20261016'
judgments=load('judgments.json')['records']
indices=[13,14,17,18,19,20,21,22,23,24]
assert [x['index'] for x in judgments] == indices
canonical=load('.work/originals/0')['records']
proposals=load('.work/originals/1')['records']
recovery=load('recovery.json')
originals={x['input']['index']:x for x in recovery['original_files']}
displays=load('display-state.json')
acks={x['label']:x for x in displays['read']}
ds=load('source-displays.json')
bs=load('binary-displays.json')
locators=load('required-locators.json')

fixed=dict(contract=CONTRACT,parent_successor=BASE,B8=B8,R=R,C2=C2,external_target=TARGET,B8_tree='751dfde81048c81390f89a65ca1d1a565ba8e1ca',B8_formal_tree='f292698cdd4a8e725525a9be6dc34b75faaf151e',R_tree='7589c800b61ba13a13040ed0d686979b80a84fd0',C2_tree='1f4375e2a51801ed62bc143c1d51f70296fa52f3',external_target_tree='5ce79942a5171ed0508282dd3a4917481a4c1324',external_task_tree='4438ac6b91b12751e361ca3a21ecd03c1f54b231')
configuration=dict(requested_model='gpt-6.1-sol',requested_effort='ultra',requested_tier='default',requested_speed='normal',requested_fast=False,**{f'effective_{x}':'UNVERIFIED' for x in ['model','effort','tier','speed','fast']})
boundary=dict(reader_context=CONTEXT,external_original_author='01a143b2-b02d-7094-808b-a4e9de51301b',parent_receiver='01a14465-f204-7783-a526-9b43e91ea005',distinct_context=True,subagents_spawned=0,new_behavior_executions=0,source_program_executions=0,independent_full_models_executed=0,host_demo_native_media_real_save_replay_executions=0,evidence_types=['SOURCE_STATIC','BINARY_STATIC','DERIVED_VECTOR','TOOL_VALIDATION'],configuration=configuration,authority='READY_FOR_PARENT_RECEPTION is this partition recommendation, not global PASS/ACCEPTED/CLOSED; root canonical/signature/dedup remain parent duties')
write('review-boundaries.json',dict(schema='r8.B.boundaries.v1',fixed=fixed,**boundary,write_set=PREFIX+'/',reference_read_only=True,formal_specs_changed=False,remediation_started=False,optional_or_policy_selected=False,merge_main=False,force_push=False,tags_changed=False,publication='Ordinary commit/push authorized. Exact remote receipt follows in publication.json.'))

instruction_paths=[
 'AGENTS.md',
 str(PARENT.relative_to(REPO)/'contract/global-prompt.md'),
 str(PARENT.relative_to(REPO)/'contract/task-prompt.md'),
 str(PARENT.relative_to(REPO)/'contract/readset.json'),
 str(PARENT.relative_to(REPO)/'contract/AGENTS.md'),
 str(PARENT.relative_to(REPO)/'contract/review-SKILL.md'),
 str(PARENT.relative_to(REPO)/'continuation-v2/manifest.json'),
 str(PARENT.relative_to(REPO)/'continuation-v2/B.prompt.md'),
 str(PARENT.relative_to(REPO)/'continuation-v2/B.complete.json')]
instruction_reads=[]
for p in instruction_paths:
    try: b=git('show',CONTRACT+':'+p)
    except subprocess.CalledProcessError:
        if p.endswith('readset.full.json'):
            p=p.replace('readset.full.json','readset.json');b=git('show',CONTRACT+':'+p)
        else: raise
    instruction_reads.append(dict(commit=CONTRACT,path=p,**identity(b),purpose='Full instructions/inventory read at start; inventory/transport is not semantic body credit',read_extent='WHOLE',reader=CONTEXT))

source_files=[]
for (c,p),rs in __import__('itertools').groupby(sorted(ds,key=lambda z:(z['commit'],z['path'])),key=lambda z:(z['commit'],z['path'])):
    rr=list(rs);seen=set()
    for x in rr: seen.update(range(x['lines'][0],x['lines'][1]+1))
    n=rr[0]['file_lines']
    source_files.append(dict(commit=c,path=p,bytes=rr[0]['bytes'],sha256=rr[0]['sha256'],git_blob=rr[0]['git_blob'],file_lines=n,actually_displayed_line_union=runs(seen),whole_file_displayed=len(seen)==n,purposes=list(dict.fromkeys(x['purpose'] for x in rr)),credit='Human source reading in stated finite interfaces; outside B business is text-consistency only; display alone never proves approval'))
formal=[x for x in source_files if x['commit']==B8 and x['path'].startswith('deliverables/')]
assert len(formal)==28 and all(x['whole_file_displayed'] for x in formal)

range_checks=[]
for obj in locators:
    for kind in ['required_source_locators','formal_locators']:
        for z in obj[kind]:
            p=z['path'];s=z['scope'];rr=s.get('ranges',([s['lines']] if 'lines' in s else []))
            seen=set()
            for d in ds:
                if d['path']==p:seen.update(range(d['lines'][0],d['lines'][1]+1))
            if p=='scripts_combine.rb':
                assert load('exact-source-dedup.json')['actual_bytes_equal'];seen.update(range(1,182))
            missing=[]
            for lo,hi in rr: missing.extend(sorted(set(range(lo,hi+1))-seen))
            assert not missing,(obj['id'],p,missing)
            range_checks.append(dict(id=obj['id'],kind=kind,path=p,original_scope=s,all_required_lines_covered=not missing,disposition='Binary independently decoded; see binary-displays and interfaces' if 'byte_offsets' in s else ('B7 exact navigation body reconstructed from wholly read B8 plus completely read navigation-diff; all old destinations independently enumerated' if obj['id']=='GR7-M19-001' else 'Actual continuous definition/ranges read; exact same scripts_combine prefix expressly deduplicated')))

method_reads=[x for x in bs if x['path']=='animmaker.exe']
assert sorted({x['displayed_method'] for x in method_reads})==list(range(1,16))
methods=method_reads[0]['methods']
assert len(methods)==15 and sum(x['instructions'] for x in methods)==743 and sum(len(x['eh']) for x in methods)==11

read_objects=[]
receptions=[]
interfaces=[]
counters=[]
b8views=load('.work/originals/100')
for j,loc in zip(judgments,locators):
    i=j['index'];a=canonical[i];p=proposals[i];assert j['id']==a['id']==loc['id']
    loc=dict(loc,fully_received_is_frozen_parent_precontinuation_field=True,current_B_reader_fully_received=True,current_B_disposition='See this reception-ledger and unread.json; original parent false is retained as historical input, not current unread')
    ca=acks['c13a' if i==13 else f'c{i}'];pa=acks[f'p{i}']
    assert ca['object_sha256']==sha(enc(a)) and pa['object_sha256']==sha(enc(p))
    assert set(ca['shown'])==set(range(ca['parts'])) and set(pa['shown'])==set(range(pa['parts']))
    assert p['id']==a['id'] and a['root_original_record']['canonical_member_sha256']==pa['object_sha256']
    groups=[dict(name=k,pointer=f'/records/{i}/groups/{k}',sha256=sha(enc(v)),entire_current_value_read=True,judgment='Full meaning, premises/defaults/enumerations, ordinary/cancel/failure/partial examples, counter and history received; independently joined in judgments.json#'+j['id']) for k,v in a['groups'].items()]
    assert len(groups)==7
    reads=[]
    for num,ack in [(0,ca),(1,pa)]:
        x=originals[num]
        reads.append(dict(C2=C2,original_path=x['input']['path'],file_identity=x['decoded'],pointer=f'/records/{i}',object_sha256=ack['object_sha256'],display_receipt=ack,all_members_and_nested_values=True,typed_refs='display-state.json typed_identity retains exact pointer/digest; target bodies get separate full-record/source reads, never credit from locator',whole_original_proposal_and_independent_counter=num==1))
    read_objects.append(dict(id=a['id'],index=i,reads=reads,seven_groups=groups,outer_fields=[dict(field=k,sha256=sha(enc(v)),read=True) for k,v in a.items()],field_binding_groups='Complete bindings read at canonical original_field_binding_groups; immutable identity only where typed, full underlying proposal and counter read separately',qualifications='file99 scope originating at original15/16/18, full relevant top qualifications and this exact record; acknowledged qualifications display',current_source_join='interfaces.json#'+a['id']))
    history=[]
    for path,v in b8views.items():
        for key in ['issues','records']:
            for n,r in enumerate(v.get(key,[])):
                if r.get('id')==a['id']:
                    # Original pointers are resolved against the fixed file, not this filtered view.
                    raw=json.loads(git('show',B8+':'+path))
                    actual=[(z,r0) for z,r0 in enumerate(raw.get(key,[])) if r0.get('id')==a['id']]
                    assert len(actual)==1
                    z,r0=actual[0]
                    history.append(dict(commit=B8,path=path,pointer=f'/{key}/{z}',member_sha256=sha(enc(r0)),read='Full selected record in acknowledged b8receptions view',state=r0.get('state',r0.get('scope'))))
    assert len(history)==(0 if i==23 else 3)
    receptions.append(dict(id=a['id'],index=i,frozen_original_identity=dict(classification=a['classification'],severity_proposed=p.get('severity_proposed'),severity_final=a['severity'],aliases=a['aliases'],canonical_root_id=a['canonical_root_id'],status=a['status'],finding_status_at_frozen_root=a['finding_status_at_frozen_root'],original_proposal_status=p['status'],root_original_record=a['root_original_record'],primary_batch=a['primary_batch']),current_all_fields_received=True,entire_seven_groups_received=True,entire_original_and_counter_received=True,purpose_original_indices=[0,1,15,16,18],b8_history=history,independent_judgment=j,source_and_formal_locators=loc,real_finite_unread=[],recommendation='READY_FOR_PARENT_RECEPTION',authority_boundary='Does not change original statuses or grant new global/host/source-family approval'))
    interfaces.append(dict(id=a['id'],producer_caller_consumer=j['producer_caller_consumer'],complete_frozen_required_source_ranges=loc['required_source_locators'],current_formal_locators=loc['formal_locators'],independent_current_join=j['current_formal_join'],normal=j['normal'],cancel_failure_partial=j['cancel_failure_partial'],examples_and_regression=j['examples_and_regression'],source_extent_receipts='reading-ledger.json#/source_files and source-displays.json',extra_finite_context='Exact full functions/callers and current shared text in receipts, no unsampled name-based acceptance',remaining=j['retained']))
    counters.append(dict(id=a['id'],scope='All frozen current values and complete seven groups/original proposal/counter, with necessary source/consumer and B8 text',actual_counter_reader=CONTEXT,distinct_from_original_and_parent=True,strongest_NO_REQUIRED_or_already_covered_counter=j['strongest_counter'],evidence='Complete source and current clause join in interfaces.json; original counter read in reading-ledger.json',recommendation=j['outcome'],new_required_proposed=False,root_final_signoff_pending=True))

write('reading-ledger.json',dict(schema='r8.B.reading-ledger.v1',utc=UTC,fixed=fixed,reader=boundary,instruction_reads=instruction_reads,transport=dict(all_target_files=45,all_original_inputs=25,receipt='recovery.json',identity_only_no_blanket_semantic_credit=True,original_purposes_in_this_partition=[0,1,15,16,18],all_other_scope_dispositions='Parent owns transport/common final signatures, A/C own their assigned canonical, D owns 29 remaining original input purposes; no inheritance of parent PASS'),objects=read_objects,shared_auxiliary_reads=[acks[x] for x in ['qualifications','fontroot','b8receptions','retainedlimits']],source_files=source_files,formal_shared_full_file_count=len(formal),formal_shared_whole_read_basis='All 28 files completely displayed/read including truncation supplements in failure-and-corrections.json. Whole-file consistency is separate from source business approval outside B.',required_locator_checks=range_checks,binary=dict(receipts='binary-displays.json',loader=bs[0],animmaker_methods=methods,method_count=15,instruction_count=743,eh_count=11,native=bs[-1],runtime='NOT_EXECUTED'),exact_dedup='exact-source-dedup.json',historical_navigation='link-validation.json and navigation-diff.json',display_pending_disposition={'c13':'Obsolete initial five-part rendering shown only part0. No full-read credit; same canonical13 was fully read in c13a with exact-value dedup and p13. No assigned object remains unread.'}))
write('reception-ledger.json',dict(schema='r8.B.reception-ledger.v1',utc=UTC,scope='Partition B only, fixed contract and B8, no sampling',state='READY_FOR_PARENT_RECEPTION',canonical_denominator=10,whole_objects_received=10,historical_required=9,optional_same_root=1,new_required=0,records=receptions,unread='unread.json',authority=boundary['authority']))
write('interfaces.json',dict(schema='r8.B.interfaces.v1',fixed=fixed,records=interfaces,shared_text_scope='28 related formal files wholly read for consistency; necessary B functions/callers/consumers actually read, broader behavior is not signed',history_scope='Nine B required records in three B8 projections fully read plus six batch/five shared receiver qualifications. Three adjacent issue bodies read for context only; no added denominator or source approval.'))
write('proposal-counters.json',dict(schema='r8.B.proposal-counters.v1',counter_reader=CONTEXT,new_required_findings=[],records=counters,independence='Actual thread ID is different from target author and parent. User prohibits subagents; no role-name relabeling or invented model configuration. Root retains final adjudication.'))
write('unread.json',dict(schema='r8.B.unread.v1',assigned_canonical=10,assigned_original_purpose_indices=[0,1,15,16,18],assigned_semantic_objects_unread=[],assigned_finite_source_or_consumer_unread=[],assigned_current_formal_or_history_unread=[],available_but_unread_inside_assigned_scope=[],broad_reference_not_claimed='No full global/native/host audit; all files/ranges beyond finite B joins remain their assigned reviewer or host obligations, never disguised as B runtime limits',out_of_partition=['A twelve canonical records','C eleven canonical records','D twenty-nine original input purposes','Parent reserved objects already completed at1b46; root canonical/dedup/common final signature still parent responsibility'],historical_context_only=['M09-001','M15-002','H08'],retained_limits=['L01–L14 as original limited closure, specifically L06/L07 tool/host, L08 font effects, L10/L14 evidence/scope qualification read here','Effective model/effort/tier/speed/Fast UNVERIFIED','All newly derived behavior NOT_EXECUTED; reference/full independent model/host/Demo/native-media/real-save/replay runs0','Original WAIT/FAIL/process violations stay historical; future compatibility policies and optional adoption unselected'],publication='Complete semantic scope; ordinary publication and own-increment remote receipt recorded separately. Parent integration and main-review final judgment remain.'))
write('frozen-denominator.json',dict(schema='r8.B.denominators.v1',B=dict(canonical=10,seven_groups=70,historical_required=9,optional=1,new_required=0),C2_global=dict(canonical=37,groups=259,nonmandatory_records=31,nonmandatory_split='8 optional +1 FLOAT +7 policy +14 limit +1 no-required; not a PASS denominator'),old_global='27 required/13 batches, R6 56 and R5 92 retain original scoped closure',formal='131 files/17 catalog families unchanged',adoption='NONE',authority='Do not combine purpose, transport, classification, historical closure or partition recommendations into one PASS denominator.'))
write('progress.json',dict(schema='r8.c2.reception.B.progress.v1',state='READY_FOR_PARENT_RECEPTION',reader_context=CONTEXT,**fixed,canonical_denominator=10,required_historical_records=9,optional_alias_records=1,complete_original_record_and_embedded_counter_reads=10,remaining_semantic=[],remaining_publication='publication.json and final commit exact fetch readback',new_behavior_executions=0,subagents_spawned=0,configuration=configuration))
write('validation.json',dict(schema='r8.B.validation.v1',utc=UTC,result='PASS_TOOL_VALIDATION_ONLY',exact_target_files=45,originals_dual_identity=25,canonical_full_record_and_original_hash_joins=10,seven_groups=70,all_required_line_scopes_covered=True,formal_whole_file_count=28,animmaker=dict(methods=15,instructions=743,exception_handlers=11),navigation=dict(B7_local=136,B7_resolved=126,B7_missing_occurrences=10,B7_missing_targets=4,B8_local=126,B8_resolved=126,historical_target_identity_matches=4),behavior='NOT_EXECUTED',readiness='Semantic review completed manually, not inferred from these mechanical checks',publication='pending exact own-increment readback'))

table='\n'.join('| '+j['id']+' | '+canonical[j['index']]['classification']+'/'+canonical[j['index']]['severity']+' | '+('同R6可选根，未选择' if j['index']==23 else 'B8已覆盖原窄必修')+' |' for j in judgments)
sections='\n\n'.join('### '+j['id']+'\n\n'+j['meaning']+'\n\n'+j['producer_caller_consumer']+'\n\n'+j['normal']+' '+j['cancel_failure_partial']+'\n\n'+j['examples_and_regression']+'\n\n当前接合：'+'；'.join(j['current_formal_join'])+'。\n\n最强反证与本次结论：'+j['strongest_counter']+'\n\n保留：'+'；'.join(j['retained'])+'。' for j in judgments)
report=f'''# 第八轮 C2 剩余接收 B 组独立报告

状态：**READY_FOR_PARENT_RECEPTION**。本组冻结十条canonical、完整七组70组、十份完整原提案与独立反证已接收；九条为B8已经覆盖的原窄必修，一条为未选择的旧同根optional。新增必修 **0**，本组可得未读、必要定义/消费者未读、当前条款/具名历史未读 **0**。这只是B组独立建议，父接收及主审保留全局去重、根签字与最终裁决。

合同 `{CONTRACT}`；父后继 `{BASE}`；唯一外部目标 `{TARGET}`。B8 `{B8}`，R `{R}`，C2 `{C2}`，树和逐文件身份见[读取台账](reading-ledger.json)、[恢复凭据](recovery.json)及[边界](review-boundaries.json)。独占分支 `codex/r8-c2-reception-b-20261016`，唯一写集本B目录。

实际审读context `{CONTEXT}`，不同于原作者和父接收者。未spawn；有效model/effort/tier/speed/Fast全部UNVERIFIED。全部新行为NOT_EXECUTED；未执行恢复旧脚本、参考游戏、exe、宿主或参考转译模型。自有恢复、惰性解码、链接及Git检查只记TOOL_VALIDATION。

| canonical | 原分类/终裁级别 | 本次独立建议 |
| --- | --- | --- |
{table}

## 全量接收与用途

完整读取原全局/任务prompt、AGENTS、clean-document-revision技能、45文件readset、continuation manifest/B.prompt/B.complete。全部45目标文件和25原始输入惰性恢复并核mode/blob/bytes/SHA/集合；该运输不授正文批准。本组原用途索引仅0、1、15、16、18：每条所有外层值、完整原提案/反证、七组、字段绑定及其共同资格均实读。不可由原UPDATE_NOT_STARTED、PENDING或作者结论推导B8现状。

通过精确值去重读取重复内容；所有typed locator/pointer只作身份，目标正文另读。[display-state](display-state.json)保留实际show/ack、原值/显示摘要及所有映射，[views](views/)保留本次显示；c13旧部分显示无全读信用，由完整c13a+p13取代。完整范围及正文理解见[逐条接收](reception-ledger.json)、[接口](interfaces.json)、[最强反证](proposal-counters.json)。必要源定义均读到结束及真实caller/consumer，28份相关共享正式文档/目录全文一致性审读；非本B业务条款不因整篇文本读取获得源批准。

B8三投影的本组九条、六批次和共享接收限定全部读完；连带M09/M15-002/H08仅为上下文。保留U07/U10原AI-helper资格WAIT、U10/U12旧partial WAIT、U06流程裁决和后继明确结论，各版本不相互涂改。最终接收总段只覆盖原窄静态必修，矩阵/追溯旧候选时点不改写。未重复父1b46已完成的保留对象与全局根签字工作。

## 逐条实质核验

{sections}

## 真实剩余与发布

[精确未读处置](unread.json)内本组有限语义未读为空。A/C其他canonical、D原用途和父全局最终签字属于其各自责任；本报告不宣布37条、31分类或全部131份全局PASS。37/259、31非必修、旧27/13与56/92保持原分母；字体同根别名不重复计数，不选择optional/policy，不重开旧27。

L01–L14、工具/宿主/字体像素及较宽原生桥、未来兼容政策持续保留；可得有限源已读，不能把未运行和未读混为一谈。解码只支持静态请求和给定前提推导，不保证XML/图像库、Windows窗口、图形/字体、真实战斗、Demo或存档回放成功。

[验证](validation.json)仅核运输、范围/身份及内部一致性；[失败与勘误](failure-and-corrections.json)保留真实失败、截断与补读，不把机械成功当语义批准。授权的普通commit/push只包含B目录，发布精确提交/逐文件mode/blob/bytes/SHA/集合及远端回读见[publication.json](publication.json)。最终发布tip在最终回复提供，不递归把自己的提交ID写入自身。未改正式规格、未整改、未合并main。
'''
(T/'report.md').write_text(report)
print(json.dumps(dict(state='READY_FOR_PARENT_RECEPTION',records=10,groups=70,formal_files=28,source_files=len(source_files),source_displays=len(ds),required_locator_checks=len(range_checks),methods=15,new_required=0),ensure_ascii=False))
