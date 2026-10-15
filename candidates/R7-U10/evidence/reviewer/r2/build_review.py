"""Assemble this review's independently assessed results and exact input receipts."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess

OUT = Path(__file__).resolve().parent
CTX = Path('/workspace/r7-context/R7-U10-reviewer')
BOOT = Path('/workspace/r7-review-bootstrap/R7-U10-r2')
CAND = Path('/workspace/r7-review-input/R7-U10-r2-583330fb69935ff6b2eb32ca11ede6c23bde5ecd')
AUTHOR = CAND/'candidate/candidates/R7-U10/evidence/author'
now = datetime.datetime.now(datetime.timezone.utc).isoformat()

def ident(data):
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}

def save(name, data):
    (OUT/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

ids = ['GR7-M15-001','GR7-M15-002','GR7-M17-001']
freeze = json.loads((BOOT/'candidate-input.json').read_text())
verification = json.loads((OUT/'input-verification.json').read_text())
author = json.loads((AUTHOR/'per-id.json').read_text())
norm = json.loads((CTX/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/normalized-record-candidates.json').read_text())
limits = json.loads((CTX/'evidence/tasks/R7-C17/limits-and-alias-reception.json').read_text())
contract = json.loads((CTX/'dispatch/delegation/contracts/R7-U10.json').read_text())

reason_sets = [
    [
        '浏览调用资源选择；BACK只写回尺寸；主菜单只重定位已绑资源。合法1/2可加载且不同、3首缺、无自有阴影、无额外重载才得1/2/假。',
        '无索引改变，不发生资源重选，BACK保初始1/1/假。',
        '尺寸页入口先重新选择物种资源，按恢复登记1重新绑定。',
        'USE在变值时置确认真并返回假，留当前项；没有本次文件写入。',
        'ACTION变值确认并返回前进标志；后续页效果只按实际到达前缀。',
        'BACK没有清确认标志的赋值，原真保真；旧改动仍控制总保存询问。',
        '坐标BACK写回原坐标且调用位置刷新；不能将其正确规则删除。',
        '资源/控件/输入依赖异常不符合正常返回前提，不承诺资源回滚或最终重画。',
        'BACK本身不持久化；无确认改动正常关闭走档案重载，原真另走保存选择；PBS后段失败保持原边界。'
    ],
    [
        '原selected0小于新长度2，保留有效0；Load取得A0。',
        '原selected0保留，Rename取得A0的名字；正常子窗前提保持。',
        '原selected0有效，Delete只替换0，长度2且1不变。',
        '原selected1小于新长度2，保留有效1；Load取得A1。',
        '原selected1有效，Rename读取A1；没有nil条件。',
        '原selected1有效，Delete只替换1，长度2且0不变。',
        '旧2缩容后置新长度2，窗口不自动钳入；Load先绑空/可释放旧图，再在属性读取失败，非失败无痕。',
        '同一独立原2无导航例，Rename参数为空，在读取名字时失败；宿主呈现未知。',
        '独立Delete Yes写索引2恰接末尾，长度3、旧0/1保留、无空洞。',
        '独立Delete No不执行替换，已缩容长度2保留。',
        '实际方向导航分支按项目数取模；恢复有效成员后才使用正常动作规则。',
        '列表BACK没有逆Resize步骤；外层Save决定落盘，正常Exit才清集合缓存，不保证异常回滚。'
    ],
    [
        'Main的计数为0分支请求高192，宽960；循环后仍到命名保存请求，实际空画布结果未知。',
        'Main全pattern计数6计算两行高384，原索引5算得槽原点0,192；保序。',
        '目标矩形取槽原点+96−w/96−h、宽高乘2；56×68得40,28,112,136，非源裁剪坐标平移。',
        'File.Exists为假跳到同一个索引递增点；原1仍槽1，目标232,28,112,136；前段正常可到保存。',
        '解析读取x后IsNullOrEmpty直接进入整图标记，y/width/height转换分支不被执行。',
        '整个输入解析先于输出；每动画保存后才迭代后项，EH仅请求清理，没有总回滚；条件必须是A确已保存成功。',
        '无参帮助后读ENTER再返回，有参只读取args[0]；无业务取消门。',
        '缺路径与构造读取器的IOException处理分别请求诊断及Exit1；不能扩为所有异常。',
        '非空x路径依次调用非负整数助手；小于0才拒绝，完整输入解析返回前没有图像输出。',
        '非负检查用<0，0通过；后续Rectangle.IsEmpty及库行为单列未知。',
        '整数助手EH只抓FormatException，指定非数字格式例请求诊断和Exit1。',
        '缺值交整数转换，不在本地宣称同于指定FormatException；当前输入集合尚未返回输出循环。',
        '超32位转换错误不由仅FormatException的catch统一捕获；实际诊断/恢复未知。',
        'XML catch的格式串引用{2}而只有两实参，不能承诺诊断成功或返回清单；解析前缀不等于保存前缀。',
        'LoadImage检查alpha，非alpha才副本及左上颜色透明请求，释放原图；不保证真实像素/编码。',
        '全部已读方法没有96上限校验；该数值为文档建议，不补理想化拒绝或钳制。',
        '存在性为真后才LoadImage，其错误不沿缺文件跳转；无正常保存/后项完成保证。'
    ]
]
evidence = [
    ['logs/007-shadow-source.stdout','logs/010-wp73-body-a.stdout','logs/011-wp73-body-b.stdout','logs/017-catalog-b.stdout','logs/022-original-vectors-dependencies.stdout','logs/033-original-proposals.stdout'],
    ['logs/008-animation-source.stdout','logs/009-window-consumers.stdout','logs/013-wp74-body-b.stdout','logs/018-catalog-c.stdout','logs/022-original-vectors-dependencies.stdout','logs/031-history-minimum-and-regression.stdout','logs/032-regression-source.stdout'],
    ['logs/006-current-cil.stdout','logs/008-animation-source.stdout','logs/015-wp74-body-d.stdout','logs/021-catalog-f.stdout','logs/024-trace-and-matrix.stdout','logs/027-wp77-boundary.stdout','logs/028-old-primary-boundary.stdout']
]
records=[]
for num,index in enumerate([19,27,21]):
    original = norm['records'][index]
    a = author['records'][num]
    assert a['record_id'] == ids[num]
    assert len(a['candidate_vectors']) == len(reason_sets[num])
    assessment=[]
    for target,reason in zip(a['candidate_vectors'],reason_sets[num]):
        assessment.append({'id':target['id'],'input':target['premise'],
                           'candidate_expected_static':target['expected_static'],
                           'independent_content_judgment':'CONSISTENT_WITH_ORIGINAL_NARROW_CONTRACT',
                           'independent_reason':reason,'evidence':evidence[num],
                           'behavior_execution':'NOT_EXECUTED'})
    records.append({'record_id':ids[num],'verdict':'PASS_SCOPED_CANDIDATE',
                    'candidate_commit':freeze['candidate_commit'],'candidate_tree':freeze['candidate_tree'],
                    'freeze_commit':'aa369555b0e8b6c8b077f964b54ed63d3b924f26',
                    'candidate_mirrors':[m for m in verification['mirrors'] if (num==0 and ('wp73-b' in m['target'] or '/test-catalog/' in m['target'])) or (num==1 and '/test-catalog/' in m['target']) or (num==2 and 'wp73-b' not in m['target'])],
                    'original_complete_seven_groups':next(x['complete_seven_groups'] for x in contract['original_full_contracts'] if x['record_id']==ids[num]),
                    'original_verification_preserved':original['groups']['verification'],
                    'original_dependencies_preserved':original['groups']['dependencies'],
                    'independent_vector_assessments':assessment,
                    'source_and_consumer_evidence':evidence[num],
                    'scope_and_preservation_explanation':'report.md corresponding record paragraphs and CG01/CG02/CG03/CG07 table; exact full-file diff in independent-mirror-diffs.patch',
                    'candidate_input_or_independence_blockers':[],
                    'later_gates':['R7-I clause reception/integration preserving shared contributions','exact historical dedup and consumer/regression reception','new independent R7-IR of actual cumulative integration','formal acceptance then closure by R7-I'],
                    'effective_configuration':{k:'UNVERIFIED' for k in ['model','effort','service_tier','speed']},
                    'integrated_PASS':False,'ACCEPTED':False,'CLOSED':False})
save('per-id.json',{'schema':'r7.u10.r2.independent-per-id.v1','utc':now,'reviewer_thread':os.environ['CODEX_THREAD_ID'],
                    'verdict':'PASS_SCOPED_CANDIDATE','records':records,'denominator':{'required':27,'batches':13},
                    'L01_L14':limits,'new_behavior_or_reference_observations':0})

recovery_dir=OUT/'recovery';recovery_dir.mkdir(exist_ok=True)
copies=[]
sources=[Path('/workspace/r7-bootstrap/R7-U10-reviewer/tools/restore_container_context.py'),
         Path('/workspace/r7-bootstrap/R7-U10-reviewer/recovery/batches/R7-U10.json'),
         Path('/workspace/r7-bootstrap/R7-U10-reviewer/review-rechecks/R7-U10/r2/reviewer-dispatch.md'),
         *CTX.glob('recovery-receipt-*.json'),*CAND.glob('recovery-receipt-*.json')]
for source in sources:
    label=source.name
    if source.parent==CTX:label='original-'+label
    elif source.parent==CAND:label='candidate-'+label
    dest=recovery_dir/label
    shutil.copyfile(source,dest)
    copies.append({'source':str(source),'delivered_path':str(dest.relative_to(OUT)),**ident(source.read_bytes())})
for rel in ['candidate-input.json','candidate-restore/R7-U10.json','remote-readback.json']:
    dest=recovery_dir/('freeze-'+rel.replace('/','-'))
    shutil.copyfile(BOOT/rel,dest)
    copies.append({'source':str(BOOT/rel),'delivered_path':str(dest.relative_to(OUT)),**ident(dest.read_bytes())})
save('review-input-receipt.json',{
    'schema':'r7.u10.r2.actual-review-input-receipt.v1','utc':now,
    'actual_identity':{'thread_id':os.environ['CODEX_THREAD_ID'],'session_id':os.environ['CODEX_SESSION_ID'],
                      'container_session':os.environ['CODEX_CAAS_SESSION_ID'],'context_role':'/root',
                      'delegating_source_thread_id':'01a13f49-a154-7054-9b04-ce31f924d01c',
                      'author_external_thread':freeze['author_task_id'],
                      'author_internal_identity':'UNVERIFIED_NO_TOOL_RETURN; original qualification preserved',
                      'old_r1_thread':'01a13ff0-e65d-7523-8410-0864772dd034','new_AI_agents_or_tasks':0,
                      'model_process_pid':'UNVERIFIED_NOT_EXPOSED','tool_pid_qualification':'runner PIDs only in logs; not model PID'},
    'requested_configuration':{'model':'gpt-6.1-sol','effort':'ultra','service_tier':'default','speed':'normal; Fast forbidden'},
    'effective_configuration':{k:'UNVERIFIED' for k in ['model','effort','service_tier','speed']},
    'authentication_or_quota_queries':0,'private_model_stream_published':False,
    'dispatch_commit':'c64774c60d91e522cb515ef71e3e9d4ea6b4712c','dispatch_tree':'a1ca6722bfeb35fa8ad53074fa29658b32ac154e',
    'freeze_commit':'aa369555b0e8b6c8b077f964b54ed63d3b924f26','freeze_tree':'08bd0f362c74ef7645b5bbd70b557489c122ae29',
    'candidate_commit':freeze['candidate_commit'],'candidate_tree':freeze['candidate_tree'],
    'fixed_B':freeze['fixed_B'],'baseline_root_tree':'84f79ec6e772aacbf3a464fde68cdc5a280e2950',
    'baseline_formal_tree':'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c',
    'candidate_files':verification['candidate_files'],'original_restore_files':verification['original_restore_files'],
    'original_restore_counts':{'files':39,'bytes':6796155},'candidate_restore_counts':{'files':61,'bytes':1050546},
    'unique_raw_bindings':len(verification['raw_member_bindings']),'supplement_files':json.loads((OUT/'supplement-recovery.json').read_text())['files'],
    'copied_recovery_evidence':copies,'old_r1_preservation':json.loads((OUT/'old-r1-reception.json').read_text()),
    'old_r1_eligibility':'WAIT_INPUT_OR_INDEPENDENCE; NOT_WAIVED; old content PASS not migrated',
    'execution':{'reference_program':0,'target_CIL':0,'independent_complete_behavior_model':0,'host':0,'Demo':0,'native_media':0,'real_save_replay':0,'REFERENCE_OBSERVATION':0,'behavior_vectors':'NOT_EXECUTED','static_decoder_tool':'EXECUTED: all 15 methods / 11 EH; does not evaluate target'},
    'L01_L14':'RETAINED with exact original limits in per-id.json','old56_92':'UNCHANGED',
    'logs_qualification':'001 onward real separated tool I/O; initial platform exploration not retrospectively re-created. One exec-server disconnect recovered same container. 037 shallow label corrected explicitly in038.',
    'candidate_input_or_independence_blockers':[],
    'unmet_later_gates':freeze['unmet_dependencies'][1:],
    'scope':'candidates/R7-U10/evidence/reviewer/r2/ only','branch':'codex/r7-u10-reviewer-20261015-r2',
    'integrated_PASS':False,'ACCEPTED':False,'CLOSED':False,
    'self_binding':'Final output commit/tree and exhaustive remote readback are returned outside their own committed bytes.'})
print(json.dumps({'records':len(records),'independent_vector_assessments':sum(len(r['independent_vector_assessments']) for r in records),'recovery_evidence_copies':len(copies),'new_AI_tasks':0,'qualification':'ASSEMBLY_ONLY; reasoning independently written in report/per-id'},ensure_ascii=False))
