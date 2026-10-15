"""Package author observations and explicit unexecuted/pending gates."""
import difflib
import json
from pathlib import Path
from build_candidate import B, H, R, ROOT, OUT, EVID, ERRATA, git, identity, dump

def main():
    mirrors=json.loads((EVID/'mirror-identities.json').read_bytes())
    contract=json.loads((EVID/'frozen-contract.json').read_bytes())
    diffs=[]
    for row in mirrors['files']:
        p=row['path']; before=git('show',B+':'+p) if row['baseline'].get('exists',True) else b''
        diffs.extend(difflib.unified_diff(before.decode().splitlines(True),(OUT/p).read_text().splitlines(True),fromfile='B/'+p,tofile='candidates/R7-U12/'+p))
    (EVID/'complete-mirror-diff.patch').write_text(''.join(diffs))
    records=[]
    for c in contract['original_full_contracts']:
        rid=c['record_id']; seven=c['complete_seven_groups']; m19=rid=='GR7-M19-001'
        vectors=[]
        def vector(id,stage,result,detail,execution='NOT_EXECUTED'):
            vectors.append({'id':id,'stage':stage,'result':result,'detail':detail,'behavior_execution':execution})
        if m19:
            vector('C01-M19-MISSING','TOOL_VALIDATION','OBSERVED_BY_AUTHOR_TOOL','Exact B 136 inline local destinations;126 resolve;10 missing/four unique targets. Candidate126 local resolve;10 immutable hrefs/four target identities. No browser/fragment/all131 audit.')
            vector('C01-M19-DIRECTORY','TOOL_VALIDATION','OBSERVED_BY_AUTHOR_TOOL','README user-interface/ is an extant Git-tree directory; old012 error11/5+exit1 and013 corrected10/4+exit0 preserved byte-for-byte.')
            vector('C01-M19-FAMILY','TOOL_VALIDATION','OBSERVED_BY_AUTHOR_TOOL','All17 catalog family destinations plus README:7/CURRENT-DELIVERY:5/delivery README:7 controls resolve. No global relative-depth change.')
            vector('C01-M19-RECOVER','TOOL_VALIDATION','EXACT_IMMUTABLE_BYTES_VERIFIED','Four files restored via fixed raw URLs with bytes/SHA/blob verified; README read, JSON identities/structure only; no semantic approval transfer. Local H Git object absent; git show requires H objects or identity-matched archive.')
            for id,detail in [('M19-NAV-01','All ten original targets replaced by same exact immutable four-file set; offline prerequisite explicit.'),('M19-NAV-02','Four historical byte/SHA/blob identities in mirror-identities.json agree with fixed plan and received C01 originals.'),('M19-NAV-03','Reverse navigation changes and remove named note reproduces B bytes exactly for all three full mirrors; formal131 and17 families preserved.'),('M19-NAV-04','Root/control routes unchanged; historical current/candidate/actual/closing scopes and old states retained.')]:
                vector(id,'TOOL_VALIDATION','AUTHOR_SCOPE_CHECK_SATISFIED',detail)
            paths={'normal':'126 local links and17 families resolve; four immutable historical identities available in restored snapshots.',
                'cancel':'Read-only navigation has no domain cancellation; abandoning navigation mutates no project/game state.',
                'failure':'At B missing relative href cannot display its target; absent historical Git object/archive also prevents offline git show. Raw transport success does not certify browser presentation.',
                'partial_commit':'No domain/file-save transaction in navigation audit; adjacent working routes do not substitute for missing candidate trace. Author Git publication is a separate transport operation.'}
        else:
            for id,detail in [('H08-NAV-01','Author static check: errata maps original item42 label§5.2 to WP72§5.3 line124; future non-author opening remains PENDING.'),('H08-NAV-02','Only matrix553 and audit1828 current labels change; both point to same named errata; old sync-input item42 remains historical§5.2. All other bytes/states unchanged.'),('H08-NAV-03','Entire WP72/WP27/DG catalog files byte-identical to B, including§5.2 and§5.3.'),('H08-NAV-05','Each six-mirror output has actual bytes/SHA/blob; model/config/runtime certificates not inferred.')]:
                vector(id,'TOOL_VALIDATION','AUTHOR_SCOPE_CHECK_SATISFIED',detail)
            derived=[('H08-NAV-04-normal1','Valid registered item; one available slot,max999,initial0,request1; add/message normal: add1,true; auto-sort only if configured; message requests1.'),
                ('H08-NAV-04-list-cancel','List cancellation: no add and no giving message.'),
                ('H08-NAV-04-quantity0','Quantity cancel/BACK returns0: no add and no giving message.'),
                ('DG-U08-01','Valid POTION,one finite slot,max999,initial0,request2; normal dependencies: add2,true,message2.'),
                ('DG-U08-02','Same premise,initial998,request2: add1 to999,false,skip successful-add sorting; normal add return then feedback uses requested2;1 added remains.'),
                ('DG-U08-03','Same premise,initial999,request1: add0,false,message requested1 after normal return; no successful-add sorting.'),
                ('DG-U08-04-list-cancel','Independent list cancel and quantity0 retain above no-add/no-message behavior.'),
                ('DG-U08-04-message-failure','Add succeeds/partially writes then message fails: reached writes retained; normal feedback/cleanup not guaranteed.'),
                ('DG-U08-04-infinite-pocket','Independent existing999 in infinite pocket,request1: may create another slot and add1; configured successful sorting only after true.'),
                ('DG-U08-04-fill-bag-control','Separate fill-bag path selecting3: important item remains1,ordinary3; existing capacity/skip rules unchanged.'),
                ('H08-NAV-04-zero-capacity','Finite zero room: no capacity precheck at Debug caller; add can returnfalse with zero added; normal return still messages requested quantity.'),
                ('H08-NAV-04-add-failure','If add raises after reached writes, later giving message is not reached; no promise of rollback, normal cleanup or host final presentation.')]
            for id,detail in derived: vector(id,'SOURCE_STATIC + DERIVED_VECTOR','STATIC_EXPECTATION_RECHECKED_ONLY',detail)
            paths={'normal':'Valid item/capacity/dependencies permit requested1; successful sort remains conditional.',
                'cancel':'List cancel or quantity0: no add/no giving message.',
                'failure':'Add failure or later message failure preserves reached writes; no guaranteed normal feedback/cleanup; finite zero room may returnfalse yet caller gives request-count message.',
                'partial_commit':'Finite one-slot initial998,max999,request2 may retain add1 and false,skip success sorting,then request-count2 feedback; not an all-or-nothing failure.'}
        write=[p for p in contract['paths'] if any(s['record_id']==rid for s in p['scopes'])]
        records.append({'record_id':rid,'status':'CANDIDATE_READY_NOT_REVIEWED','classification':'required',
            'scope_contract_commit':'f622356f3beb9e84ea8cff9db07c7fb382565d3f',
            'minimum_contract':seven['三_最小修订_正确保留']['最小行为合同'],
            'preserved_scope':seven['三_最小修订_正确保留']['正确保留范围'],
            'read_set':seven['六_依赖接收_精确读写集']['读取义务'],
            'read_qualification':'Full baseline mirror bytes processed for identity/diff. The three M19 entry files and the named source/current clauses read. Whole audit/matrix byte ranges are identity/reversal checks, not a claim of unrelated clause semantic review.',
            'write_set':write,'conditional_writes':[],'vectors':vectors,'state_paths':paths,
            'unmet_dependencies':['Different actual context ultra candidate review after R7-I freezes candidate-input.json',
                'R7-I shared clause integration and CG01/CG07 conflict reception',
                'New R7-IR actual-integration review and R7-I acceptance/closure gates',
                'Historical/domain consumers in original contract remain pending; no record-to-record scheduling edge invented'],
            'direct_author_blocking_edges':[],'candidate_PASS':False,'integration_PASS':False,'ACCEPTED':False,'CLOSED':False,
            'runtime':{'reference':0,'independent_complete_model':0,'host':0,'Demo':0,'native_media':0,'real_save_replay':0},
            'effective_configuration':'UNVERIFIED'})
    dump(EVID/'per-id.json',{'schema':'r7.u12.author-per-id.v1','status':'CANDIDATE_READY_NOT_REVIEWED',
        'baseline':B,'publication_dispatch':'6ec1d09e9c470954964d72761c83a760ef4f0364',
        'progress_denominator':{'required_records':27,'batches':13,'this_candidate_records':2,'accepted_by_author':0,'closed_by_author':0},
        'L01_L14':'RETAINED','old56_and92':'UNCHANGED_ORIGINAL_SCOPES','records':records})
    report='''# R7-U12 作者交接

状态：**CANDIDATE_READY_NOT_REVIEWED**。本角色只产生两项必修的六个隔离镜像和本目录证据；未创建作者/reviewer子任务，未修改正式规格、公共台账、旧证据或reference，未签发独立PASS、ACCEPTED或CLOSED。

固定派发：`6ec1d09e9c470954964d72761c83a760ef4f0364` 的全文 `review/remediation-seventh-20261015-prepare/delegation/parallel-dispatch/authors/R7-U12-author.md`；全文七组合同固定于 `f622356f3beb9e84ea8cff9db07c7fb382565d3f`。作者分支仅 `codex/r7-u12-author-20261015-wave1`，从 B `e646432c644dec04d306842cc5a559a29c718fbc` 创建；B根tree `84f79ec6e772aacbf3a464fde68cdc5a280e2950`、正式131 tree `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`。最终commit/tree由提交和远端读回在包外绑定，不编造未来自哈希。

GR7-M19-001：三份完整镜像仅替换原L14/L16十个href并加同一具名历史检索说明，指向 H `e58486178e746273fb6fab55df00722807f1dc44` 的四个原作者候选文件。保留历史正文和候选/actual/关闭身份；不以actual替代candidate。离线git show明确要求已有H对象或匹配档案。本容器只有有界历史快照，不假定历史Git对象存在。四文件的实际bytes/SHA256/blob见 `mirror-identities.json`；原始HTTP恢复回执保留，浏览器、anchor及全131正文链接审读未执行。

GR7-H08-001：新增候选 `review/remediation-seventh-20261015-prepare/current-navigation-errata.json`，携带原 `WP72 §5.2／WP27`、新 `WP72 §5.3／WP27`、B sync-input完整身份及`/items/42/actual_clause_label`、固定R两文件身份/范围、WP72全文及加道具条款行身份。仅对当前导航产生未来优先关系；候选matrix553/audit1828同步新标签和具名勘误引用。R6冻结sync-input、接受/CLOSED及回执保持；WP72/WP27及DG-U08-01–04原字节保持。

本容器按已完整阅读的恢复工具/清单独立取得26文件、7,587,353字节；resume重核26文件均为精确字节复用、无HTTP。12个合同原载荷切片另核原bytes/SHA。为保留旧11/5失败证据，按明确logical_path定向读取C2 payload-index并恢复C01旧012/013的JSON/stdout/stderr及M19-link-check，共7文件84,951字节；未扫描完整core载荷、未读取80MB Manifest、未执行旧脚本。恢复身份与语义验收分开。

作者工具核验：B三文件136个本地inline目的地中126可解析、10处/4目标缺失；候选126本地目的地全可解析，另外10个固定H地址覆盖同4目标。有效user-interface目录作为对照，17测试族与根README:7/CURRENT-DELIVERY:5/第六轮README:7正常链接保留。反向剔除十处href修改及三条具名说明，可逐字节重建三份B原件；矩阵和审计分别只改553/1828一行，状态列不变。正式131目录没有任何差异；冻结R6子树身份及工作区/索引差分另记 `history-preservation.json`。

正常1、原DG正常2、列表取消、数量0、998请求2部分入1/false/请求数反馈/不成功排序、999请求1、零容量、无限口袋、填包对照以及添加/后段消息失败全部按 `per-id.json` 分项静态重核。SOURCE_STATIC与DERIVED_VECTOR分开，所有行为向量保持NOT_EXECUTED；参考、完整独立模型、游戏宿主、Demo、native媒体、真实保存/回放新执行均0。源码只读，未复制源码结构为框架规格。

实际上下文资格见 `actual-context.json`：委派来源thread已给定，当前平台task/context/model-PID没有有效回显，均不冒充已验证。请求gpt-6.1-sol/xhigh/default普通速度、禁Fast；实际model/effort/tier/speed逐项UNVERIFIED，不探查认证或额度。项目AGENTS全文已读；项目和工作区无适用`.agents/skills`文件，未应用无关FastAPI技能。

失败与日志：`logs/002-build` exit1源于作者工具错误地假定本地已有H Git对象，诊断保存在003；改为核已恢复的不可变快照后004/008/011通过。原失败未覆盖或升格。完整staged whitespace检查013 exit2只报告精确补丁的空白上下文和旧历史stdout末尾空格；这些证据字节不清洗。014限定检查exit0，六镜像另行检查；公开日志中的原始空格也保持。最初侦察/阅读命令在平台工具I/O可见，缺单独文件化UTC/stdout/stderr，明确保留该流程缺口；001起的新日志是后继实际命令，不回填早期时间。未读取/发布私有模型流。公开命令I/O与真实退出按logs逐项保存；补丁/工具成功仅TOOL_VALIDATION。

无作者前置阻塞边。仍OPEN/待办：R7-I按完整候选差异与身份生成candidate-input；不同实际context的ultra候选复审；CG01/CG07共享消费者及R7-I逐条串行整合；新R7-IR实际整合复审；后续唯一接受/关闭及具体历史回归接收。候选PASS、整合PASS、ACCEPTED、CLOSED均未发生。27项/13批分母、L01–L14和旧56/92有限关闭边界保持。

交付包括六个完整镜像、`per-id.json`、`artifact-manifest.json`、`mirror-identities.json`、`complete-mirror-diff.patch`、验证/恢复回执及公开工具日志。artifact-manifest逐文件列出原B/新bytes/SHA/blob；自身不填自哈希。先发布候选，随后只提交新增发布回执和最终清单，六镜像不变；最后整体commit/tree和逐新文件远端读回由包外真实工具回执绑定，避免自引用。只普通推送唯一分支；全部发布完成即停止写入，等待父会话安排ultra复审。
'''
    (EVID/'report.md').write_text(report)
    print(json.dumps({'status':'AUTHOR_REPORT_AND_PER_ID_PACKAGED','records':len(records),'mirrors':6,'behavior_vectors_execution':'NOT_EXECUTED'}))

if __name__=='__main__':
    main()
