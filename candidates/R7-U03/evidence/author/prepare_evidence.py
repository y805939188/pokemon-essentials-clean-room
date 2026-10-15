"""Package author-only evidence and exact identities, without acceptance claims."""
import datetime
import difflib
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BOOT = Path('/workspace/r7-bootstrap/R7-U03-author')
CTX = Path('/workspace/r7-context/R7-U03-author')
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
BRANCH = 'codex/r7-u03-author-20261015-wave1'

def identity(data):
    return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
                git_blob_content_id=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())

def write(name,value):
    (HERE/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

contract = json.loads((BOOT/'delegation/contracts/R7-U03.json').read_bytes())
normalized = json.loads((CTX/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/normalized-record-candidates.json').read_bytes())
validation = json.loads((HERE/'validation.json').read_bytes())
scopes = {r['path']:r['changes'] for r in validation['files']}
mirrors=[]
for row in contract['paths']:
    old=subprocess.check_output(['git','show',B+':'+row['path']],cwd=ROOT)
    if row['classification']!='required':
        continue
    path=ROOT/row['candidate_path'];new=path.read_bytes()
    offsets=[]
    for tag,a,b,c,d in difflib.SequenceMatcher(None,old.splitlines(True),new.splitlines(True),autojunk=False).get_opcodes():
        if tag=='equal':continue
        offsets.append(dict(kind=tag,original_byte_offsets=[sum(map(len,old.splitlines(True)[:a])),sum(map(len,old.splitlines(True)[:b]))],
                            candidate_byte_offsets=[sum(map(len,new.splitlines(True)[:c])),sum(map(len,new.splitlines(True)[:d]))]))
    mirrors.append(dict(original_path=row['path'],candidate_path=row['candidate_path'],classification=row['classification'],
                        record_ids=sorted({s['record_id'] for s in row['scopes']}),original_commit=B,
                        original_B=identity(old),new=identity(new),line_scopes=scopes[row['candidate_path']],byte_scopes=offsets,
                        merge_instruction='R7-I serial clause integration only; never overwrite other batches with this full mirror.'))

context=dict(role='R7-U03 author',status='CANDIDATE_READY_NOT_REVIEWED',
    source_parent_thread_id='01a13f49-a154-7054-9b04-ce31f924d01c',
    source_parent_is_current_task_id=False,current_platform_task_id='NOT_EXPOSED',current_platform_context_id='NOT_EXPOSED',
    actual_environment_id='ccarenv_b64_Y2NhcmVudl85MzA2NTk5Yjk1NTg4MTkxOTE5NjEwOTEzNWRmOTdhZg',
    checkout=str(ROOT),branch=BRANCH,fixed_B=B,fixed_B_tree=subprocess.check_output(['git','rev-parse',B+'^{tree}'],cwd=ROOT).decode().strip(),
    fetched_dispatch_commit='6ec1d09e9c470954964d72761c83a760ef4f0364',
    full_contract_commit='f622356f3beb9e84ea8cff9db07c7fb382565d3f',recovery_tool_plan_commit='658488c81f1f3181a488298ab27850c8af951d73',
    fixed_reference_commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',
    reference_full_tree_verified_here=False,reference_qualification='Selected file snapshots only, not complete checkout or host certification.',
    request=dict(model='gpt-6.1-sol',reasoning_effort='xhigh',service_tier='default',speed='normal; Fast prohibited'),
    actual_effective_configuration=dict(model='UNVERIFIED',reasoning_effort='UNVERIFIED',service_tier='UNVERIFIED',speed='UNVERIFIED'),
    actual_configuration_reason='No authoritative effective configuration return in exposed tools; requested argv or author identity is not proof.',
    process_id_evidence='commands/*.json wrapper_pid and process_pid identify real Python/git processes only; no model process PID asserted.',
    no_child_author_or_reviewer_created=True,no_Mac_operations=True,utc_packaged=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    initial_observations=dict(HEAD=B,branch='work',status_clean=True,unique_output_branch_local_and_remote_absent=True,
        qualification='Observed initial exec stdout, not a backfilled timestamped file; current checks separately logged.'),
    progress_denominator=dict(items=27,batches=13,modified=False),limits='L01-L14 retained; old 56/92 boundaries unchanged')
write('context-and-configuration.json',context)
records=[]
for i,rec in [(6,contract['original_full_contracts'][0]),(7,contract['original_full_contracts'][1])]:
    is_m05=i==6
    catalog=ROOT/('candidates/R7-U03/deliverables/final-specification-set/test-catalog/'+('engine-overworld-wp11-15-59-60.md' if is_m05 else 'engine-overworld-wp16.md'))
    prefix='R7-BP' if is_m05 else 'R7-CAM'
    vectors=[]
    for line in catalog.read_text().splitlines():
        if line.startswith('| '+prefix):
            fields=[x.strip() for x in line.split('|')[1:-1]]
            vectors.append(dict(id=fields[0],given=fields[1],expected=fields[2],
                phase='DERIVED_VECTOR from named SOURCE_STATIC reads',execution='NOT_EXECUTED',
                result='EXPECTATION_DOCUMENTED; NO_BEHAVIOR_RUN_RESULT',source_catalog=str(catalog.relative_to(ROOT))))
    c04=normalized['records'][i]['groups']['verification']['acceptance_items']['value']
    mapping=({'C04-BP-A':['R7-BP01','R7-BP03'],'C04-BP-B':['R7-BP02'],
              'C04-BP-C':['R7-BP04','R7-BP05'],'C04-BP-D':['R7-BP06'],
              'C04-BP-E':['R7-BP07','R7-BP08']} if is_m05 else
             {'C04-CAM-A':['R7-CAM01'],'C04-CAM-B':['R7-CAM02'],'C04-CAM-C':['R7-CAM03'],'C04-CAM-D':['R7-CAM04']})
    m=dict(id=rec['record_id'],priority=rec['severity'],author_state='CANDIDATE_READY_NOT_REVIEWED',
           independent_candidate_review='PENDING_R7-I_CANDIDATE_INPUT_AND_DIFFERENT_ACTUAL_CONTEXT_ULTRA_REVIEW',
           integrated_review='NOT_STARTED',accepted=False,closed=False,
           minimum_contract=rec['complete_seven_groups']['三_最小修订_正确保留'],
           read_set='read-set.json#/required_read_set filtered by record_id',
           write_set=[r for r in mirrors if rec['record_id'] in r['record_ids']],
           vectors=vectors,original_c04_acceptance=c04,acceptance_to_candidate_vector_map=mapping,
           normal_cancel_failure_partial_commit=(
               dict(normal=['R7-BP01','R7-BP02'],precompletion='R7-BP03',no_new_chain=['R7-BP04','R7-BP05'],
                    forced_route='R7-BP06',failure='R7-BP07 two independent injected failures',
                    partial_commit='bump count at creation; movement cleared before general consumer; global counter before player consumer',
                    cancellation='R7-BP08 no completion opportunity, no added cancel API') if is_m05 else
               dict(normal=['R7-CAM01','R7-CAM02','R7-CAM03','R7-CAM04'],cancellation='Blocked/no movement is outside the counterexample; unchanged movement rules.',
                    failure='Normal resource/update premises excluded failure; assert actual prefix only.',
                    partial_commit='Player position changed with camera held is normal dual state, not rollback/transaction failure.')),
           preserved_scope_checks='validation.json documents exact unchanged non-target clauses/table rows; author-only TOOL_VALIDATION.',
           dependencies=normalized['records'][i]['groups']['dependencies'],
           remaining_open=['R7-I exact identity/scope reception and candidate-input.json',
                'Different actual context ultra candidate review','CG04/CG05 serial clause reception where applicable',
                'R7-I formal integration and fresh R7-IR review','Direct/transitive domain and historical reception gates; no automatic closure'],
           execution_counts=dict(reference_observation=0,independent_full_model=0,game_host=0,Demo=0,native_media=0,real_save_replay=0),
           limits='L01-L14 unchanged; original NOT_EXECUTED not rewritten by identity/tool checks')
    if is_m05:
        m['original_BP01_BP08_map']={f'GR7-M05-BP{n:02}':f'R7-BP{n:02}' for n in range(1,9)}
        m['passive_catalog_mirrors']=[f'R7-FP{n:02}' for n in range(1,9)]
        m['conditional_wp06']={'adopted':False,'reason':'B §4.1 correctly guards forced/interpreter paths and separates distance from step count; no concrete contradiction requiring same-record sync.','fixed_B_identity':identity(subprocess.check_output(['git','show',B+':deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md'],cwd=ROOT))}
    else:
        m['historical_relation']='GR3-M03-001 WR01 premise residual; row1320 consulted; GR3-CAM06–08 and WP16 body unchanged; full historical closure not re-signed.'
    records.append(m)
write('per-id.json',dict(schema='r7-u03-author-per-id.v1',status='CANDIDATE_READY_NOT_REVIEWED',records=records,
    tool_result='TOOL_VALIDATION only; SOURCE_STATIC author reading and DERIVED_VECTOR expectations, no independent PASS.'))

report='''# R7-U03 作者候选

状态：**CANDIDATE_READY_NOT_REVIEWED**。仅提交GR7-M05-001、GR7-M06-001的隔离候选，未正式接受或关闭任何问题。进度分母仍为27项/13批；旧56/92、L01–L14均保持。

## 固定输入与身份

已从origin的codex/remediation-seventh-20261015-cloud取回并确认派发提交6ec1d09e9c470954964d72761c83a760ef4f0364，完整读取该提交R7-U03-author.md及f622356f3beb9e84ea8cff9db07c7fb382565d3f的原七组/原入口。恢复工具和本批清单固定于658488c81f1f3181a488298ab27850c8af951d73，均先阅读再执行。

本独立容器实际恢复34文件/6,088,763字节并核bytes/SHA256/Git blob，resume全部复用匹配字节。原始提案、完整非作者C04两记录、根接收及全部149个具名JSON成员的offset/原字节SHA/JSON pointer/规范化SHA均另核。定向补取4个具体绑定输入（两个收到的提案、source/formal inventory）及12,802字节successor delta；没有读取80MB Manifest或扫描完整core索引。见input-verification.json、恢复回执、read-set.json。参考仅为固定R的所选只读快照，不冒称完整Git树/运行认证。

项目AGENTS.md全文已读；本容器/workspace/.agents为空、项目及固定提交没有.agents/skills，已如实登记缺失，没有伪称应用技能。真实环境ID、父来源线程与当前task/context未暴露的区别见context-and-configuration.json。作者请求gpt-6.1-sol/xhigh/default/普通速度；实际model、effort、tier、speed逐项UNVERIFIED。普通进程PID/UTC不充当模型认证；未创建子作者/reviewer，也未操作用户Mac。

## 本批变化与scope

- WP12：§4.1区分碰撞创建/完成及普通位移的开始/完成；创建不增全局步数/距离或发离格通知，正常完成可经一般通知进入合格玩家链；§8补失败/无完成更新的实际前缀，导航同步。
- WP61：§2/§3.1登记合格碰撞完成来源，保留强制路线、解释器、冰瀑自动运动、消费者中断及逐项次序；§11仅同步本批导航。
- 移动目录：限定MV01/MV02，新增R7-BP01–08，分别覆盖返回/完成、普通通行、完成前、触碰成功、失败对角、合法路线WAIT、一般/玩家消费者失败、无完成机会。
- 被动目录：新增对应R7-FP01–08；旧FP01–35、毒伤默认关闭、空寄养自身周期、非玩家受阻与MR02规则均保留。
- WP16目录：只修WR01的有效显示坐标实际增加128子像素输入及前后独立量化，并增加R7-CAM01–04小图、居中大图、右边缘与手动在途卷动对照。WP16正文及GR3-CAM06–08保持原字节。

只生成5份从B原字节建立的完整镜像；WP06算法与守卫正确，没有具体矛盾，不采用条件同步。不修改formal/reference/公共台账、main或tag。精确原B/新bytes/SHA/blob、行/字节范围与读写集见artifact-manifest.json及per-id.json；candidate.diff供逐条整合，不能用镜像覆盖其它批次贡献。

## 验证资格与尚待接收

validate-final-mirrors完成有界目录/差异位置/旧表行保持/新链接逻辑目标/JSON检查。共1,016个非目标旧表行保持原文（含表头/分隔行，数字不是行为案例分母）。该结果仅TOOL_VALIDATION，作者静态读源与纸面向量不作为独立PASS。所有新增行为向量仍NOT_EXECUTED；REFERENCE_OBSERVATION、独立完整模型、游戏宿主、Demo、native媒体与真实存档回放各0。失败/取消/部分提交按per-id.json分别登记，未把退出0提升为业务成功。

校验过程中第一次递归身份检查发现批清单外4个具体可读绑定，按精确C2对象定向恢复后149成员全部匹配；未把可读材料伪标limit。目录校验器先后因行号清单偏移、未排除本来就需修改的碰撞表行而退出1，修正校验器后通过；这些真实失败日志保留，不曾执行参考程序。初始侦察与内容读取仅有平台tool I/O，未另存逐命令UTC/stdout/stderr；不补造旧时间。后续commands/保存分离的可发布命令I/O、UTC、PID、退出，参考源正文不复制入公共证据，私有模型流不推送。

无作者前置批次阻塞；依赖仍OPEN：R7-I接收实际候选身份/scope并生成candidate-input.json，不同实际context的ultra审者复核，CG04（本批与U01/U13的移动目录）及CG05（本批与U09的被动目录）由R7-I串行按条款整合，再由新R7-IR审实际整合字节。WP12/WP61/WP06/Repel消费者与历史MR02、GR3-M03-001关系仍需最终接收，不自行宣称已满足全部直接/传递依赖或全历史回归。候选PASS、整合PASS、ACCEPTED、CLOSED分开。

## 传输与冻结约定

唯一成果分支codex/r7-u03-author-20261015-wave1，从固定B e646432c644dec04d306842cc5a559a29c718fbc创建。与B差异仅candidates/R7-U03/；只普通提交/普通push该分支。全部新文件进入提交。发布后按固定结果commit逐新文件完整HTTP远端读回并比较bytes/SHA/blob，另读远端branch及commit/tree。允许将首个候选内容提交的发布/读回回执提交为同分支后继证据；最终commit/tree及最终全量读回在最终交接中包外绑定，避免提交内自引用哈希。完成后冻结，停止写入，等待R7-I派发的ultra复审。
'''
(HERE/'report.md').write_text(report)

inventory=[]
for path in sorted((ROOT/'candidates/R7-U03').rglob('*')):
    if path.is_file() and path.name!='artifact-manifest.json':
        inventory.append(dict(path=str(path.relative_to(ROOT)),**identity(path.read_bytes())))
write('artifact-manifest.json',dict(schema='r7-u03-candidate-artifacts.v1',status='CANDIDATE_READY_NOT_REVIEWED',
    branch=BRANCH,base_commit=B,base_tree=context['fixed_B_tree'],mirrors=mirrors,
    exact_write_roots=['candidates/R7-U03/deliverables/final-specification-set/ (five listed mirrors only)',
                       'candidates/R7-U03/evidence/author/'],
    conditional_wp06_adopted=False,evidence_and_mirror_inventory=inventory,
    inventory_qualification='Exact file identities at packaging. This manifest excludes itself to avoid hash recursion. Later publication-only receipts/logs are bound by final Git commit/tree and remote readback; mirror entries remain authoritative.',
    required_open_gates=['R7-I reception','Independent ultra candidate review','Serial clause integration','Fresh R7-IR integrated review','Domain and historical reception'],
    original_read_set='read-set.json',stage='TOOL_VALIDATION',semantic_PASS=False))
print(json.dumps(dict(status='CANDIDATE_READY_NOT_REVIEWED',mirrors=len(mirrors),inventory_files=len(inventory),configuration='UNVERIFIED',behavior_execution=0)))
