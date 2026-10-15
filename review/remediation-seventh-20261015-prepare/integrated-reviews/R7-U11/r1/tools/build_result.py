"""Materialize this context's manually assessed actual-integration result."""
import datetime
import hashlib
import json
from pathlib import Path

ROOT = Path('/workspace/r7-ir-R7-U11')
INP = ROOT / 'actual-input'
OUT = Path(__file__).resolve().parent.parent
MI = '45c80832a41c1b56dcd7e9d93497758cbb7721de'
FI = '13d76ba61838b13925ba9d41f58a6b047564d926'
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
P = 'deliverables/final-specification-set/'
WP = P + 'demo-dx/wp75-project-conversion-and-authoring-tools.md'
DX = P + 'test-catalog/demo-dx-wp72-73-74-75-76-77.md'
def read(p): return json.loads(p.read_bytes())
def write(name, obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def ident(content):
    return {'bytes':len(content),'sha256':hashlib.sha256(content).hexdigest(),
            'git_blob':hashlib.sha1(f'blob {len(content)}\0'.encode()+content).hexdigest()}
def actual_identity(path): return {'commit':MI,'path':path,**ident((INP/'actual'/path).read_bytes())}
def span(path,start,end):
    lines=(INP/'actual'/path).read_bytes().splitlines(keepends=True)
    start_byte=sum(map(len,lines[:start-1])); content=b''.join(lines[start-1:end])
    return {'commit':MI,'path':path,'lines_one_based_inclusive':[start,end],
            'byte_offsets_zero_based_half_open':[start_byte,start_byte+len(content)],**ident(content)}
def vector(key,premise,reason,source,location):
    return {'id':key,'premise':premise,'independent_static_reason':reason,
            'source':source,'actual_locator':location,
            'content_conclusion':'SUPPORTED_SCOPED_STATIC','behavior_execution':'NOT_EXECUTED'}

byte_audit=read(OUT/'input-byte-audit.json')
journal=read(INP/'integration/applied-clauses.json')
clauses=read(OUT/'clause-reconstruction.json')
context=read(OUT/'context-observation.json')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
contract=read(ROOT/'original/dispatch/delegation/contracts/R7-U11.json')
primary=[x.relative_to(INP/'actual').as_posix() for x in (INP/'actual').rglob('*') if x.is_file()]
assert len(primary)==14

# These explanations were assessed against the newly read source and MI content.
m16=[
 ('C01-M16-ONE','固定R唯一Main；兼容未加密宿主已进入，目录可枚举、唯一A.rb可读且正常，无覆写。','Main末尾直接发出发现调用；被选A进入读/求值请求。WP75把它从停用集合移出，仍不承诺宿主成功。','decoded Main L20–49',WP+':445'),
 ('C01-M16-ORDER','根A.rb与可见子目录B.rb均可读，先行脚本正常返回。','本层文件排序后先处理，再排序递归可见子目录；A先于B，无新的调度或启动保证。','decoded Main L20–46',WP+':344–359,445'),
 ('C01-M16-SKIPS','只给a.txt与.hidden/B.rb；另给隐藏普通.hidden.rb作为区别对照。','非rb普通文件及点目录被过滤；点开头普通rb仍可入选。候选跳过不使包围的Main失活。','decoded Main L20–46',WP+':344–359,445; '+DX+':351'),
 ('C01-M16-PREFIX','A已正常返回，B随后读失败或求值失败，C在后；无外部救援重入。','读发生在局部求值保护前；求值分支也可抛出，C无必达保证。前定义/已达副作用不全局撤回。','decoded Main L20–46',WP+':344–359,445; '+DX+':353'),
 ('R7-M16-L05','普通被捕获求值错误，消息改写尝试结束后的实际长度分别899/900；900例日志写入成功。','899再抛原错误；900先覆盖日志后发固定说明。实际改写未改消息时按实际长度；写日志失败不保证固定说明。','decoded Main L3–18,L32–41',WP+':344–359; '+DX+':352–353'),
 ('M16-CANCEL','同一条件Main入口，没有工具提取/合并入口混入。','没有UI确认/取消；两作者脚本的数量守卫不能成为此加载入口的取消或回滚门。','decoded Main complete L1–49',WP+':344–359,445'),
 ('M16-SCRIPT-ERROR','分别为脚本错误族、普通错误与读取/日志阶段失败。','脚本错误族改共同错误类别并保留消息；普通错误用实际长度分层；读取/日志失败不被偷并成保证恢复。','decoded Main complete L1–49',WP+':344–359; '+DX+':352–353'),
 ('M16-WP08-CONSUMER','普通归档与恰一节归档分别，所需源/事件依赖可读；只核文本收集，不调用它。','归档全部节均扫；仅长度1额外遍历Data/Scripts列举的文件，收集路径不含求值。这与loader按rb选择不同，不能互相认证宿主执行。','Intl_Messages.rb L7–189; loose Main L1–60',P+'generic-kernel/wp08-localization.md:100–108; '+WP+':344–359'),
]
m16vectors=[vector(*x) for x in m16]
aliases={'R7-M16-L01':'C01-M16-ONE','R7-M16-L02':'C01-M16-ORDER','R7-M16-L03':'C01-M16-SKIPS','R7-M16-L04':'C01-M16-PREFIX',
         'U07-L01':'C01-M16-ORDER','U07-L02':'R7-M16-L05','U07-L03':'M16-SCRIPT-ERROR'}
for alias,target in aliases.items():
    orig=next(x for x in m16vectors if x['id']==target)
    m16vectors.append({**orig,'id':alias,'same_static_case_as':target,
                      'qualification':'原别名/历史向量分别保留；相同推理不计为额外运行'})
for item in m16vectors:
    if item['id']=='U07-L01':
        item['premise']='可读根目录.hidden.rb/a.rb/b.RB与可见z/c.rb、隐藏目录.hidden/d.rb，全部正常；另空目录。'
        item['independent_static_reason']='普通文件单独排序得到.hidden.rb→a.rb→b.RB，随后递归z/c.rb；点目录跳过，隐藏普通rb不跳过。空目录无内容动作，递归无显式深度上限。'
    if item['id']=='U07-L03':
        item['premise']='前文件成功；后文件分别读失败、脚本错误族、普通错误、日志写失败；还有未到后续文件。'
        item['independent_static_reason']='读失败在局部求值保护之前；脚本错误改共同类别并保消息，普通错误按实际长度，日志失败不保证固定说明。先前定义保留，未到文件不执行，无整体回滚。'
for key,premise,reason,source,line in [
 ('CV-M26','归档5、恰10与11节；结构节/空节/既有散文件；正常写入前提。','提取<10拒绝，10/11放行；清树、编号/转义/删除CR、忽略空普通正文、备份后单节loader次序保持。','scripts_extract.rb complete L1–183',225),
 ('CV-M27','旧归档9/10/11；另单根脚本连续合并、深目录、空目录、实体名及大写后缀独立例。','合并>10拒绝，9/10允许；重新聚合丢弃旧节，文件先于目录、递归无明确深度上限，直接覆盖不备份。单节产物再跑仍允许、ID重新生成；命名不保证互逆。','scripts_combine.rb complete L1–183',226),
 ('B20-C024','可读11节档案、旧树/备份B0；清树成功后首个非空脚本打开失败；另原无备份例及9/10反向控制。','失败时旧树已清、原归档未改、备份阶段未到；后续写/备份/loader失败各保已达前缀，无全局回滚。相同11节combine在数量门拒绝。','scripts_extract/combine complete L1–183',329),
]:m16vectors.append(vector(key,premise,reason,source,DX+':'+str(line)))

ext_reasons=[
 '0x401415/0x401449的宽高入参分别840×240和800×176；后继三个独立查询不受Script成功条件包围。',
 '0x40147b/0x4014ac分别请求840×144和800×72，Script缺席跳到此目标仍可到达。',
 '0x4014de/0x40150f分别请求840×164和800×92，前两缺席不排除此分支，是所需最小反例。',
 '0x40155f/0x401593请求840×444和800×372，0x4015b0/0x4015d0给id1/id2位置25,392与150,392；0x15保持尺寸。',
 '四次外框查询按顺序独立分支；单次空句柄跳过本目标，全空仍进入等待/标记复核。',
 '外框尺寸请求先行；EDIT查询只用首个结果。缺EDIT跳过其尺寸调用但到达下一目标；Batch随后按钮分支不依赖EDIT。',
 'Batch的两个按钮各自有空句柄检查；缺一不抑制另一，均与EDIT是否存在独立。',
 '十个尺寸/定位调用之后均未检查返回值；假返回本身不阻断后续。0x16保持位置/z序/激活，0x15保持尺寸/z序/激活；请求无撤回不等于真实几何已改变。',
 '标记由区分大小写的两个子串检查决定；本反例无其它合格标记。目标查询采用表列#32770与英文标题入参；没有进程ID所有权关联。',
 '互斥辅助把重复183结果关闭句柄并返回0，调用者只测0而停止；创建失败−1仍可到标记门，退出清理明确排除0/−1。',
 '整轮后Sleep入参150，再检查标记；消失走退出并只关闭有效句柄，保持走下一轮。没有恢复几何或业务取消/文件事务；周期无实测。',
 'Interpreter L120–195是构造诊断建议的路径，未发出启动工具/修复脚本调用。CV-M29文档范围及R6 L07未被新表替换。',
]
cat=(INP/'actual'/DX).read_text().splitlines()
ext=[]
for i,reason in enumerate(ext_reasons,1):
    key=f'R7-U11-EXT-{i:02}'
    matches=[(n,line) for n,line in enumerate(cat,1) if line.startswith('| '+key+' |')]
    assert len(matches)==1
    line_no,row=matches[0]; cells=[x.strip() for x in row.split('|')]
    ext.append({**vector(key,cells[2],reason,'extendtext fixed bounded business/entry/data/imports; Interpreter L120–195',DX+':'+str(line_no)),
                'actual_expected_text':cells[3],
                'global_premises':'固定R；兼容查询/尺寸接口、正常到业务入口；除具名门反例外有单一合格标记、无重复互斥、所需句柄在本轮稳定且无外部改写；正常依赖，除所设失败外正常。'})
rawbase=ROOT/'original/evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs'
root_original=read(rawbase/'e0c5ebb227169d6a24ca470630bdc0c22f4ea8f8a70a89951fae64546dde22ae.raw')
c06=read(rawbase/'c8497e269bd91b3ead5289adfc6f7718abe22ba649f2365ae4408b2d6ed0acab.raw')['challenges'][2]
old_et=[]
mapping=[['01','02','03','04','05'],['09'],['03','06'],['04','07'],['10','11']]
for original,checks in zip(root_original['records'][22]['original_proposal']['regression_vectors'],mapping):
    old_et.append({**original,'binding':'fixed root /records/22/original_proposal/regression_vectors',
                   'premise_qualification':'Only original C06 narrowed entry/host/query premises; no actual Windows run',
                   'independent_static_reason':'本次重新核对相应请求与分支，见'+','.join('R7-U11-EXT-'+x for x in checks),
                   'content_conclusion':'SUPPORTED_SCOPED_STATIC','behavior_execution':'NOT_EXECUTED'})
acceptance=[]
for i,text in enumerate(c06['acceptance'],1):
    acceptance.append({'id':f'C06-ACCEPT-{i:02}','original_criterion':text,
                       'actual_scope':WP+':389–409; '+DX+':392–409',
                       'independent_static_reason':['十个静态调用入参及标志逐一核对，全部限请求。','初始标记/互斥0与−1分层控制流已核。','四外框、EDIT、两按钮和假返回守卫没有混同。','外框先发请求，缺EDIT仍可到后继。','等待后门重验、有效句柄关闭，无几何恢复或进程owner推断。','Interpreter仅诊断，原文档/CV-M29、R6 L07、WP74格式边界保留。'][i-1],
                       'content_conclusion':'SUPPORTED_SCOPED_STATIC','behavior_execution':'NOT_EXECUTED'})

shared=[]
for path,group,note in [
 ('audit/source-traceability.md','CG01','五批精确增量均保留：U13三行来源、U11静态补充、U12单导航字段、U01/U02有序EOF追加；旧批准身份保留。'),
 (DX,'CG03','当前仅U11新增EXT12行及说明；完整B前缀不变，U01条件目标无写、U10未来贡献未合入。'),
 ('planning/feature-matrix.md','CG07','U13 F05-02 Pending、U11 F18-04备注、U12历史导航行和U01/U02 EOF贡献完整；旧阶段由root接收尾注限定。')]:
    shared.append({'group':group,'path':path,'actual_identity':actual_identity(path),
                   'receiver':'R7-I sole integrator','assessment':note,
                   'this_context_result':'U11兼容与完整保留的有限复核完成；其它ID不授新语义PASS',
                   'root_next_gate':'接收本结果并登记当前语义/共享/依赖/历史责任，之后分别决定ACCEPTED与CLOSED'})
later=[
 {'gate':'R7-I actual-result receipt','state':'OPEN','scope':'Receive this exact result commit/tree and its U11 semantic/shared/dependency/historical responsibility'},
 {'gate':'formal ACCEPTED','state':'NOT_PERFORMED_BY_THIS_REVIEW','owner':'R7-I'},
 {'gate':'CLOSED','state':'OPEN_SEPARATE_DECISION','owner':'R7-I','qualification':'No invented host-run or unrelated-batch dependency for finite static closure'},
 {'gate':'runtime/broader compatibility','state':'UNVERIFIED_NOT_EXECUTED','scope':'Archive host entry; actual Windows API returns/geometry/timing/ownership/autostart/CRT remainder; optional/policy and wider/global dependencies not settled'},
]
records=[
 {'record_id':'GR7-M16-001','verdict':'PASS_SCOPED_ACTUAL_INTEGRATION',
  'minimum_contract':'仅修WP75 §16-6停用分类；保留§12.4条件请求与§18宿主未知，不扩写为启动成功。',
  'actual_files':[actual_identity(WP)],'actual_clauses':[span(WP,445,445),span(WP,344,359),span(WP,454,460)],
  'independent_counterproof':[{'hypothesis':'旧§12.4已正确，所以§16停用枚举不构成问题。','assessment':'§16的源活动分类与旧正面合同相冲突；实际445行已单独列条件入口。'},
                              {'hypothesis':'安全解码或WP08收集可证明真实加载成功。','assessment':'均只为静态/工具事实；兼容未加密宿主进入、可读及先前依赖正常仍是前提。'}],
  'vectors':m16vectors,
  'direct_consumers':['固定R archive Main全部49行、extract/combine各183行、loose Main全部60行；未执行。','实际WP75§12.1–12.4/16/18；WP08§6.1及新读Intl收集L7–189。'],
  'transitive_consumers':['WP77§1/§3/§7/§9只提供作者工作流与Demo证据层分离；不是启动证明。','共享DX旧CV/B20/U07向量；audit/matrix同步引用。'],
  'record_scheduling_edges':{'direct':[],'transitive':[],'qualification':'原七组无具名排程边，不等于领域/全局无依赖'},
  'historical_reception':'本次有限静态重读R7-M16-L01–L05、C01四例、U07-L01–03、CV-M26/M27与B20-C024；旧全局PASS不转签。',
  'conditional_specs_demo':'未触发根明确维护/同步条件；MI历史specs/demo与B相同，全文读其历史不解包/不执行标签，不把历史状态冒作当前primary。',
  'remaining_gates':later},
 {'record_id':'GR7-M17-002','verdict':'PASS_SCOPED_ACTUAL_INTEGRATION',
  'minimum_contract':'固定旧工具四目标/按钮请求、独立缺席、0/−1、假返回继续与退出前缀；保留文档与运行未知。',
  'actual_files':[actual_identity(p) for p in [WP,DX,'audit/source-traceability.md','planning/feature-matrix.md']],
  'actual_clauses':[span(WP,389,409),span(WP,16,20),span(WP,50,50),span(WP,452,452),span(DX,392,409),span('audit/source-traceability.md',1489,1490),span('planning/feature-matrix.md',259,259)],
  'independent_counterproof':[{'hypothesis':'说明书两目标足以概括固定程序。','assessment':'静态业务路径另有独立Comment/Batch及按钮请求；原文档事实留史，新表只补有界请求。'},
                              {'hypothesis':'前两框缺席/无EDIT/API返回假会阻断之后所有处理。','assessment':'新读分支逐项否定，Batch两按钮也独立。'},
                              {'hypothesis':'mutex创建失败−1与重复结果0是同一停止分支。','assessment':'调用方仅测试0，−1可继续至标记门且不作为有效句柄关闭。'},
                              {'hypothesis':'所读请求证明效果、精确周期、owner或自动启动。','assessment':'所有返回未检查；标记仅存在性，150仅等待入参，Interpreter仅诊断；相应R6 L07仍未知。'}],
  'vectors':ext,'original_regression_vectors':old_et,'original_acceptance':acceptance,
  'direct_consumers':['固定extendtext.exe业务[1692,2764)、数据[3072,3348)、入口[1561,1684)及导入；extendtext.txt全文4行；Interpreter L120–195。','实际WP75§14与§1/§3.2/§17；DX EXT01–12、原CV-M29。'],
  'transitive_consumers':['WP74§18及全稿保证animmaker/.anm与文字扩展请求分开；R6 final-delivery全文尤其L07/L14。','audit T-WP75-01与matrix F18-04传播来源及资格；WP77作者工具入口/Demo分离。'],
  'record_scheduling_edges':{'direct':[],'transitive':[],'qualification':'不推定域依赖完成；root政策与更广宿主支持另门。'},
  'shared_receivers':shared,
  'historical_reception':'TOOL-ET01–05、C06六验收和12新向量已按具名前提静态重核；CV-M29及B全目录前缀、旧批准身份、R6 L07、WP74所有既有格式边界保持。',
  'conditional_specs_demo':'历史稿全文读且保持B原字节；无维护条件接收，未修改或要求扩大写集。',
  'remaining_gates':later},
]
write('per-id.json',{'schema':'r7.u11.independent-actual-integration-review.r1.v1','utc':now,
                    'reviewer_context':context,'MI':MI,'MI_tree':byte_audit['pins'][MI],
                    'MI_formal_tree':byte_audit['MI_formal_tree'],'FI':FI,'FI_tree':byte_audit['pins'][FI],
                    'records':records,'blocking_findings':[],
                    'verdict_scope':'Two original narrowed mandatory IDs only; no other-ID/global/runtime equivalence certificate',
                    'ACCEPTED':False,'CLOSED':False,
                    'all_behavior_vectors':'NOT_EXECUTED',
                    'new_REFERENCE_OBSERVATION_independent_complete_model_reference_program_host_Demo_native_media_real_save_replay':0,
                    'L01_L14':'RETAINED','old56_92':'ORIGINAL_SCOPED_HISTORY_ONLY','denominator':{'required_items':27,'batches':13},
                    'effective_configuration':dict.fromkeys(['model','effort','tier','speed'],'UNVERIFIED')})

read_ledger=[]
for path in sorted(primary):
    data=(INP/'actual'/path).read_bytes()
    read_ledger.append({**actual_identity(path),'complete_content_read':True,
                       'physical_lines':len(data.splitlines()),
                       'qualification':'全文本次实读；仅U11最小合同、相关消费者与共享保留获本次有限判断，其它语义不重授PASS'})
write('content-review-progress.json',{'schema':'r7.u11.actual-content-read-ledger.v1','recorded_utc':now,
                                    'mandatory_primary_files':read_ledger,
                                    'additional_project_read':{'path':'wp77-demo-evidence-and-capability-coverage.md','commit':MI,'lines_read':[[1,48],[149,196]],'purpose':'作者工具/真实Demo层级与缺口'},
                                    'new_reference_read':{'Intl_Messages.rb':[[1,190]],'purpose':'档案文本收集不同于求值'},
                                    'all_reference_execution':'NOT_EXECUTED'})
final_delivery=read(INP/'actual/review/remediation-sixth-20261014-prepare/completion/final-delivery.json')
write('retained-limits.json',{'source':actual_identity('review/remediation-sixth-20261014-prepare/completion/final-delivery.json'),
                            'original_limits':final_delivery['remaining_outside_mandatory_scope']['limit'],
                            'historical_execution_only':final_delivery['execution_qualifications']['historical_Ruby_attempts'],
                            'this_review_new_executions':0,'configuration':'UNVERIFIED',
                            'qualification':'全部原有限边界保留；历史18尝试不是18成功行为测试，本次未重跑；H14局部也不回填'})
write('review-input-receipt.json',{'schema':'r7.u11.actual-review-input-receipt.r1.v1','utc':now,
 'reviewer_context':context,
 'requested_configuration':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'normal; Fast forbidden'},
 'effective_configuration':context['effective_configuration'],
 'pins':byte_audit['pins'],'fixed_B':B,'fixed_B_formal_tree':byte_audit['fixed_B_formal_tree'],
 'MI':MI,'MI_formal_tree':byte_audit['MI_formal_tree'],'FI':FI,
 'reference':{'repository':'Maruno17/pokemon-essentials','commit':R,'tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','qualification':'有界固定只读快照，不认证整参考树或宿主'},
 'dispatch':{'commit':'c64774c60d91e522cb515ef71e3e9d4ea6b4712c','path':'review/remediation-seventh-20261015-prepare/integration/wave2/v1/dispatch/R7-U11-R7IR.md','full_read':True,'AI_auxiliaries':0},
 'original_contract':{'commit':'f622356f3beb9e84ea8cff9db07c7fb382565d3f','path':'review/remediation-seventh-20261015-prepare/delegation/contracts/R7-U11.json',**ident((ROOT/'original/dispatch/delegation/contracts/R7-U11.json').read_bytes()),'complete_seven_groups_read':True},
 'restoration':{'bootstrap_commit':'658488c81f1f3181a488298ab27850c8af951d73','tool_guide_and_both_plans_read_before_execution':True,
    'original':{'files':28,'bytes':6312155,'destination':str(ROOT/'original')},
    'actual':{'files':190,'bytes':6931357,'destination':str(INP),'plan_identity':ident((ROOT/'actual-plans/R7-U11.json').read_bytes())},
    'supplement':'binding-supplement-receipt.json (4 exact raw objects,385887 bytes); consumer-supplement-receipt.json (fixed Intl and MI WP77)',
    'complete_input_file_identities':'input-byte-audit.json',
    'qualification':'两恢复均本容器实际执行，不假设共享目录；未取80MB交接/全core；未执行参考或候选程序'},
 'mandatory_actual_full_content_read':read_ledger,
 'source_reading':{'archive':'594全部惰性tokens及49行Main，压缩[29,590)，1197字节；无Ruby反序列化/eval',
   'extract_combine':'两文件各183行全文','loose_Main':'60行全文',
   'native':'业务0x40129c–0x4016cc、入口0x401219–0x401293、数据[3072,3348)、PE/import；CRT余部未读不认证',
   'extendtext_doc':'4行全文','Interpreter':'本次至少L1–240（所需120–195完整）','Intl':'新补取完整身份，只读L1–190收集消费者'},
 'original_counterproof':'C01/C06 challenges/2完整、原root记录20/22与C01 received原提案、normalized两项verification/dependencies及L01–L14；12合同+217normalized原切片/pointer/canonical本次匹配',
 'candidate_qualification':{'author_files_restored_and_Git_compared':57,'candidate_review_files_restored_and_Git_compared':65,
   'author_report_per_ID_changes_vectors_and_failures_read':True,
   'candidate_reviewer_report_per_ID_checks_and_input_qualifications_read':True,
   'scripts':'仅作证据文本/身份，不运行；本次没有执行作者/候选审者工具来产生判决',
   'semantic_PASS':'NOT_INHERITED'},
 'shared':{'complete_current_files':[actual_identity(p) for p in ['audit/source-traceability.md',DX,'planning/feature-matrix.md']],
           'approval_binding':'shared-approval-audit.json; four peer reports/eligibility plus per-ID/receipt exact identities and relevant shared scopes',
           '56_hunk_reconstruction':'clause-reconstruction.json; 23 exact targets plus one errata with only3 declared root stage-field changes; no semantic peer PASS',
           'engine_UI':'all56-hunk reconstruction includes U01/U13 engine and U02/U08 UI compositions mechanically; outside U11 primary-target semantic certificate',
           'prior_accepted_five':'input-byte-audit.json; exact prior MI bytes preserved; five full current files read for U11 compatibility, no re-signature of their source behavior',
           'U03_U07_U10':'procedural WAIT/unintegrated, not treated as absent domain dependencies'},
 'skills':byte_audit['skills'],
 'phase_qualification':{'SOURCE_STATIC':'本次手工控制流/条款/消费者审读','DERIVED_VECTOR':'全部NOT_EXECUTED','TOOL_VALIDATION':'恢复、hash/Git、JSON绑定、惰性解码、逐hunk、运输','REFERENCE_OBSERVATION':0,'independent_complete_model':0,'reference_program':0,'host_Demo_native_media_real_save_replay':0},
 'log_qualification':{'durable_wrapper':'logs/001 onward: true argv/PID/UTC/stdout/stderr/exit; only explicitly wrapped commands have these separate records',
    'early_reads':'侦察/fetch/合同与内容分块读取在平台I/O；未另存每命令UTC/PID/分离流，不补造。初始无xxd127、Git对象未到128及不存在.agents的查找资格保留。',
    'new_failed_checks':['003缺固定candidate Git对象，抓取固定对象后004通过','006误假定新errata在B存在，按明确新增路径修正工具，007通过','008/009原绑定审计缺具体原载荷；010定向恢复后011通过'],
    'historical_failures':'作者003/006失败、候选审者早期403/128/2/KeyError、U01旧FAIL及其它共享报告操作资格均保留，不回写为成功'},
 'limits':'retained-limits.json；L01–L14、旧56/92原范围和27项/13批保持，optional7/facet2/no-required1/policy2未采用',
 'write_authority':{'branch':'codex/r7-ir-u11-20261015-r1','base':B,'prefix':'review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U11/r1/','candidate_formal_main_tag_modified':False},
 'remaining_gates':later,'ACCEPTED':False,'CLOSED':False,
 'publication':'实际结果commit/tree和最终全文件远端响应体回读由提交后真实工具结果在最终回传绑定，manifest自身不填递归自hash'})
print(json.dumps({'verdicts':{x['record_id']:x['verdict'] for x in records},'vectors':{x['record_id']:len(x['vectors']) for x in records},'mandatory_full_reads':len(read_ledger)},ensure_ascii=False))
