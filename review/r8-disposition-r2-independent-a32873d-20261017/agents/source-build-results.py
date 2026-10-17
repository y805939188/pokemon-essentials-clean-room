#!/usr/bin/env python3
"""Build attributed source supplemental report; no feature-domain verdict transfer."""
import collections
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
sys.dont_write_bytecode=True
ROOT=Path('/workspace/r8-disposition-r2-review')
OUT=ROOT/'review/r8-disposition-r2-independent-a32873d-20261017/agents'
INV=ROOT/'planning/implementation-routing/r8-20261017'
C='a32873d2860b15d9f5e27727db8f131f4ec433b6'
P='8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8'
OLD='review/r8-disposition-r1-independent-5666b7b-20261017/'
def g(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def sha(x):return hashlib.sha256(x).hexdigest()
def read(name):return json.loads((OUT/name).read_text())
def identity(commit,path):
    data=g('show',commit+':'+path)
    return {'commit':commit,'path':path,'bytes':len(data),'sha256':sha(data),'git_blob':g('rev-parse',commit+':'+path).decode().strip()}
def save(name,value):(OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
e=read('source-machine-evidence.json');loc=read('source-locator-recheck.json')
m=json.loads((INV/'routing-manifest.json').read_text())
prior=[]
for fn in ['REPORT.md','findings.json','finding-results.json','feature-results.json','reading-coverage.json','root-findings.json']:
    raw=g('show',P+':'+OLD+fn)
    record={'identity':identity(P,OLD+fn),'consumption':'FULL_REPORT_SEMANTIC_READING' if fn=='REPORT.md' else 'FULL_JSON_STRUCTURAL_RECONCILIATION; relevant ROOT-TOOL rows semantically read; no unallocated domain verdict transfer'}
    if fn.endswith('.json'):
        obj=json.loads(raw)
        record['complete_top_level_structure']={k:len(v) if isinstance(v,(list,dict)) else v for k,v in obj.items()}
    prior.append(record)
save('source-prior-reconciliation.json',prior)

ledger={}
for old,new,name in [('fd1df570cad987dc3852a3b958f03916e317f7fe','908273093e1f6b27fc58249417675dd62d146224','B8-to-908'),('908273093e1f6b27fc58249417675dd62d146224','49a558f7d5498680ba88d532f3815e07d7844459','908-to-49'),('49a558f7d5498680ba88d532f3815e07d7844459','0eee6d141f33758eda34bd8ebad94a3e2b617f5a','49-to-U06')]:
    patch=g('diff','--no-ext-diff','--unified=3',old,new,'--','deliverables/final-specification-set/')
    if name=='B8-to-908':(OUT/'source-diff-B8-to-908.patch').write_bytes(patch)
    path=None
    for line in patch.decode().splitlines():
        if line.startswith('+++ b/'):
            path=line[6:]
            ledger.setdefault(path,{'path':path,'fresh_diff_reads':[],'full_document_read':False,'credit':'All added/deleted/context lines and headers freshly semantically read; unchanged body not claimed as newly reread.'})
        elif line.startswith('@@ '):
            h=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',line)
            if h:
                a,n,b,k=map(int,[h[1],h[2] or 1,h[3],h[4] or 1])
                ledger[path]['fresh_diff_reads'].append({'old_commit':old,'new_commit':new,'old_range':[a,a+n-1],'new_range':[b,b+k-1],'patch':f'source-diff-{name}.patch'})
for path,item in ledger.items():
    item['identities']=[identity(c,path) for c in ['fd1df570cad987dc3852a3b958f03916e317f7fe','908273093e1f6b27fc58249417675dd62d146224','49a558f7d5498680ba88d532f3815e07d7844459','0eee6d141f33758eda34bd8ebad94a3e2b617f5a']]
extra=[('creature-rpg/wp33-daycare-and-breeding-session.md',107,158),('pokemon-rules/wp34-inheritance-and-offspring.md',22,51),('combat-requirements/wp51-ai-action-selection-and-skill.md',132,151),('user-interface/wp65-title-load-options-pause-and-pc.md',148,176),('user-interface/wp65-title-load-options-pause-and-pc.md',206,233)]
extras=[{'identity':identity('0eee6d141f33758eda34bd8ebad94a3e2b617f5a','deliverables/final-specification-set/'+p),'fresh_ranges':[[a,b]],'consumption':'FRESH_COMPLETE_RANGE_SEMANTIC_READ; consumer qualification only'} for p,a,b in extra]
semantic=[
 '初始化/人数与实际席位、失败前缀归2/7；命令/优先序归9/13；UI请求与失败入口归677/686。新子节细化现有职责，不产生新的承载功能。',
 '15个作者身份是397固定目录，137继承，214兼容先行门与508亲本角色真实消费；META20字段责任导航适合保留。',
 '主档→单备份删除与下次主档门是451失败恢复、446保存和642标题入口的交接；部分删除失败不回滚。',
 'Z/M组接2/7/9/13，EV组接456/204/29；分类与静态向量分母保持，不把21个测试ID新造为功能。',
 'Conversion直接目标贡献归92，普通User0候选是否进入归76；不把贡献NOT_ENTERED当整候选固定100。',
 'H2聚合下方删除/系统装配两组；445/446/449/451/439/642为真实启动、持久、迁移、语言及UI消费者。',
 'KER001五例只消费451/446/642的有序删除、前缀与标题回返；没有新增独立文件I/O功能。',
 'KER002区分旧序列适配449、空性装配445、有效性/递归备份451、语言439与标题642；身份/后验门完整。',
 'ST01–05归456模板存储、204普通非Shadow分配和29成长同步；默认非内部设施早门与道具/Shadow排除保留。',
 '七个Slot图像角色归699，game/core查找440与资源352；固定背景等不被批量翻译。',
 '空身份提示/转轮路径分别归703/354，已完成财务前缀归702；32×32普通fallback与更早空名失败不能合并。',
 '当前图的范围门/容器集合归325，按ID取图与全局引用区别归323；有限滚屏静态夹具不新造相机或保存功能。',
 '摆放阶段异常后同容器抑制归325/323；同实例重建326与通知首次异常409为明确交界，没有保证恢复。',
 '直接119主矩阵336、外层推进335和主文镜像339准确；不套101预读或移动路线体系。',
 'H2只聚合六静态族的现有消费者；子标题分组保持具体用途，无新增运行功能。',
 'PBS051文本Dungeon标记归生成输入346/临时图查询323；文本已知不提高编译、资源、Demo和运行资格。',
 'NP01–05归生命周期325、获取323、重建326与通知409；外层捕获继续前提和成功/入口前后失败分开。',
 'RP01–05归325/323，RP06条件保存446，RP07正常读档326/445及更早面板642；不称真实存档往返。',
 'JT01–06归330普通移动/跳跃计时，645菜单和647快捷是明确待同步入口；UI65缺口仍PENDING，不授U04接受。',
 'CE117子携父当前编号并绑定建立时当前图归338，矩阵336与主文339同步；不新造保存功能。',
 'LB命中/缺目标/末尾/重复及后继失败归336/335/339；入口前门与已分派缺目标分开，未执行资格保持。'
]
assert len(semantic)==len(e['heading_results'])==21
headings=[]
for h,reason in zip(e['heading_results'],semantic):
    item=dict(h)
    item.update(verdict='PASS_PROPOSED_MAPPING_SEMANTICS_ONLY',reason=reason,source_qualification=('RECEIPT_BOUND_ACCEPTED_SOURCE_PROPOSAL_NOT_APPLIED' if h['kind']=='ACCEPTED_PROPOSAL_ONLY' else 'PENDING_U04_NOT_ACCEPTED_PROPOSAL_NOT_APPLIED'),new_feature_required=False,classification_acceptance_granted=False)
    headings.append(item)
findings=[
 {'id':'SOURCE-R2-001','severity':'P2','verdict':'FAIL_TOOL_ACCEPTANCE_IDENTITY_FACET','title':'接受事件只约束旧actual身份，可把同路径后继未接受字节当作已接受来源',
  'candidate_locations':[{'path':'planning/implementation-routing/r8-20261017/routing.py','line':257},{'path':'planning/implementation-routing/r8-20261017/routing.py','line':278},{'path':'planning/implementation-routing/r8-20261017/routing.py','line':332},{'path':'planning/implementation-routing/r8-20261017/revisions/r2/tools/backfill-accepted-sources.py','line':131},{'path':'planning/implementation-routing/r8-20261017/revisions/r2/tools/backfill-accepted-sources.py','line':171}],
  'reproduction':'python review/r8-disposition-r2-independent-a32873d-20261017/agents/source-audit.py; isolated Git descendant of908 adds one sentence to accepted WP04 L196. Recompute actual identities/locators, retain exact old receipt/registry. routing.errors returns []. No apply executed.',
  'expected':'A later changed accepted path must require a new exact accepted target identity or explicit receipt-bound section-delta qualification.',
  'actual':'Event target matches old accepted commit, ancestry passes, current changed bytes need only a nonempty relevant accepted_event. Unaccepted blob92a99ce3 is accepted under d895aa9d receipt.',
  'evidence':['source-stale-receipt-probe.json','source-fixture-command-io.json','source-audit.py'],
  'required_fix':'Validate each changed current document against the accepted target identities whose bytes still apply at the exact current snapshot; do not use path membership/ancestry as accepted-content identity. Shared U01/U04 consumers require explicit source-scope and pending-batch handling. Add stale-receipt descendant regression.',
  'current_candidate_impact':'Real908 and all33 target bytes in0eee match their receipts; no observed candidate data mismatch. The future source gate code is unsound. Do not reclassify736 functional rows.',
  'historical_relation':'Additional mechanically enforceable receipt-current identity facet related to ROOT-TOOL-02; original known-batch/event existence PASS is retained as historical. Root decides aggregate old-group disposition.'},
 {'id':'SOURCE-R2-002','severity':'P3','verdict':'FAIL_FUTURE_COVERAGE_SCHEMA_PIPELINE','title':'backfill继承1776个null理由，输出不满足新current coverage schema',
  'candidate_locations':[{'path':'planning/implementation-routing/r8-20261017/revisions/r2/tools/backfill-accepted-sources.py','line':186},{'path':'planning/implementation-routing/r8-20261017/revisions/r2/tools/backfill-accepted-sources.py','line':227},{'path':'planning/implementation-routing/r8-20261017/revisions/r2/tools/backfill-accepted-sources.py','line':235},{'path':'planning/implementation-routing/r8-20261017/current-section-coverage.schema.json','line':121}],
  'reproduction':'python review/r8-disposition-r2-independent-a32873d-20261017/agents/source-null-reason-probe.py. Build inherited sections with exact backfill get/default expressions; validate synthetic908 current relation against fixed new schema.',
  'expected':'Backfill-generated current sections satisfy their declared schema before applying the source switch.',
  'actual':'1776 historical metadata_reason keys are explicitly null. dict.get(default) preserves null; schema requires a nonempty string. Independent schema check returns1776 type errors. prepare validates only manifest/historical coverage, so misses these future output errors.',
  'evidence':['source-coverage-null-reason-summary.json','source-null-reason-probe.py','source-coverage-null-reason-probe.json'],
  'required_fix':'Either model functional-mapping null reasons intentionally in current schema or normalize them to meaningful strings in backfill. Validate complete prospective current coverage before any core writes; retain historical coverage unchanged. Add a schema round-trip regression.',
  'current_candidate_impact':'Current source switch is correctly blocked before writes; no real current-section-coverage exists. This is independently demonstrated future output incompatibility, not a claim that current2704 full checks ran or failed.'},
 {'id':'SOURCE-R2-003','severity':'P3','verdict':'FAIL_CURRENT_COVERAGE_MAPPING_GUARD','title':'任意行为标题可用ALL_FORMAL_FEATURES标签逃过空消费者拒绝',
  'candidate_locations':[{'path':'planning/implementation-routing/r8-20261017/revisions/r2/tools/current-coverage-check.py','line':45},{'path':'planning/implementation-routing/r8-20261017/current-section-coverage.schema.json','line':117}],
  'reproduction':'python review/r8-disposition-r2-independent-a32873d-20261017/agents/source-coverage-probe.py. Synthetic908 section table normalizes the separate null-reason issue; baseline[]. Clear both consumer arrays for WP39 chapter4 and set coverage_scope=ALL_FORMAL_FEATURES; check returns[].',
  'expected':'Global-governance scope exemptions apply only to explicitly qualified governance documents/headings; ordinary behavior headings need actual existing consumers.',
  'actual':'The special literal exempts any section from nonempty feature/metadata mappings; schema permits arbitrary coverage_scope strings and check has no path/class qualification. This is a structural blank-mapping hole, not a request to automate consumer relevance.',
  'evidence':['source-coverage-scope-probe.json','source-coverage-probe.py'],
  'required_fix':'Constrain ALL_FORMAL_FEATURES to the fixed governance-document identities or explicitly approved governing headings; require nonempty resolved refs elsewhere. Add an ordinary behavior-heading negative fixture using the exemption literal.',
  'current_candidate_impact':'Actual21 proposed heading mappings have consumers and no observed abuse. Do not convert this guard finding into failures for the39 consumer features or736 classifications.'}
]
result={'schema_version':'r2-independent-source-supplement.v1','candidate_commit':C,'reviewer':'/root/r2_source_pipeline','scope':'Cumulative source preparation, source qualification,21 new heading consumer proposals and future tool code; no allocated original feature-domain rows',
 'configuration':{k:'UNVERIFIED_NOT_EXPOSED' for k in ['model','effort','service_tier','speed','Fast','cloud_task_uuid']},
 'old_feature_results':[],'active_feature_results':[],'retired_metadata_results':[],'issue_results':[],'original_group_results':[],
 'row_allocation_boundary':'Parent explicitly assigned no domain old-ID table. Functional/group totals are reconciled by root and domain reviewers; this supplement adds no duplicate acceptance vote.',
 'source_current_state':loc,'receipt_target_checks':{k:e[k] for k in ['target_count','all_target_identities_match','all_accepted_target_bytes_preserved_in_0eee','actual_write_set_extensions','unaccepted_changed_paths']},
 'source_heading_counts':e['heading_counts'],'removed_headings':e['removed_headings'],'source_heading_results':headings,
 'heading_hash_convention_note':'All21 source evidence hashes are title-only; current locator/schema heading hashes are raw Markdown lines including newline. Both independently recomputed; this is not reported as a normative locator defect.',
 'reading_ledger':list(ledger.values()),'extra_consumer_reading':extras,'prior_structural_reconciliation':'source-prior-reconciliation.json',
 'reading_qualification':'All source patches added/deleted/context/header text was freshly read without truncation credit;21 new source bodies fully present in those patches. No fresh131-document全文 claim, no transfer of upstream full/telemetry or old unallocated feature verdicts.',
 'incidental_cache_cleanup':'Two exploratory importlib calls initially generated ignored routing/backfill CPython caches under author tree. Both exact cache files and then-empty cache directories were removed. Candidate source/data bytes were unchanged; all retained deliverables are source-* review files and disposable Git fixture is in /tmp.',
 'tool_execution_qualification':{'author7_current_commands':'Not repeated here; root independently replays. Source preparation I/O input/tool hashes verified.','five_author_accepted_binding_fixtures':'NOT_EXECUTED_AWAITING_U04','actual2704_full_current_coverage_check':'NOT_EXECUTED_AWAITING_U04','source_prepare_or_apply_run_on_author_tree':False,'independent_checks':'Read-only Git/JSON/Markdown and isolated synthetic static fixtures only','business_reference_host_prototype_runs':0},
 'source_guard_verdict':'PASS_CURRENT_PREPARATION_QUALIFICATION_AND_ACTUAL_U04_REFUSAL; not future tool completeness PASS',
 'ui65_boundary':{'accepted':'U01 §3.1 startup empty-data/language gate and§4.1 ordinaryNo persistence distinction only','pending':'U04 §6.1/§8.1 ordinary motion versus jump timer definition and receiver synchronization; FR645/647 proposal remains pending','fresh_current_ranges':[[148,176],[206,233]],'whole_file_acceptance_transfer':False},
 'new_findings':findings,'conclusion':'Source identity intake/21 proposed consumers/current-vs-prepared boundaries are supported. Three independently reproducible future source-tool defects require root disposition; legitimate unswitched U04 state is not a functional-classification failure.'}
save('source-results.json',result)
table='\n'.join('| '+str(i+1)+' | '+h['title']+' | '+', '.join(h['feature_refs']+h['metadata_refs'])+' | '+('accepted-source建议' if h['kind']=='ACCEPTED_PROPOSAL_ONLY' else 'pending-U04建议')+' | '+h['reason']+' |' for i,h in enumerate(headings))
findtext='\n\n'.join('### '+f['id']+'（'+f['severity']+'）'+f['title']+'\n\n'+f['actual']+'\n\n复现：`'+f['reproduction']+'`\n\n必要修正：'+f['required_fix']+'\n\n当前影响：'+f['current_candidate_impact']+'\n\n代码：'+', '.join('`'+x['path']+':'+str(x['line'])+'`' for x in f['candidate_locations'])+'。证据：'+', '.join('['+x+']('+x+')' for x in f['evidence'])+'。' for f in findings)
report=f'''# R2来源接收与后继工具独立补充审查

固定候选 `{C}`。当前908的真实来源数据没有发现回执身份失配，21个新增标题的现有消费者建议均有具体语义依据。发现三项可复现的后继来源工具缺陷，不能预授这些代码PASS。它们不摊派为736个功能分类FAIL；U04尚未接受、未切换的真实阶段本身不是本轮分类失败。

## 已核事实与资格

累计8批回执的33目标bytes/SHA256/blob全部与固定Git相等；这些目标在0eee中仍同字节。R8-U07为非正式正文overlay，未制造新功能。实际写集比原计划增加6份正式文档：U09的WP26、WP23附表、WP31、WP34、WP66-A，以及U06的WP58；不能从旧计划未列写集推为不受接受门约束。当前清单仍只有908/U02/U03，独立重算736active、191绑定=17接受+174待核。

从Git重算131文档历史/908均2683标题，0eee为2704；新增21、删除0。11个accepted-source标题只形成准备建议，另10个U04标题为pending建议。完整读908→49的713行/112106 bytes及49→0eee的361行/57082 bytes全部增删/上下文和文件/hunk头，证据与Git diff逐字节一致；另读B8→908两处单行改动。21新章完整正文均在这些新鲜diff读集中，另完整读WP33兼容、WP34亲本角色、WP51候选以及UI65§6/§8指定范围。未宣称131篇全量新鲜全文阅读。

`prepared-source-backfill.json`的736个locator及49个changed-unit ID已独立重算全相等；没有将它们当当前应用。真实作者prepare/apply I/O中的3核心输入hash和工具hash与候选相等，apply因6个纯U04文件缺正式接受被拒且核心不变。未发布或要求U04回执。

UI65的U01只接收§3.1/§4.1；实际§6.1仍写玩家未移动/静止，§8.1仅回指§6.1，未绑定WP12的普通移动/跳跃计时定义。对应645/647仍为明确待同步消费者；U01整文件身份不转授U04义务。当前拒绝门保持正确。

## 三项工具发现

{findtext}

## 21个新增标题的逐项建议

以下PASS仅表示建议的语义消费者合理；没有应用locator，没有授pending源接受，也没有给目标兼容、实现或原型PASS。

| # | 标题 | 现有消费者 | 资格 | 独立判断 |
| --- | --- | --- | --- | --- |
{table}

## 工具约束与未执行项

backfill能核receipt目标本身的固定身份、旧事件兼容、正式文档索引、行映射歧义、保全source/plan/retired以及未接受路径/未映射新标题。其机械行对齐不是语义证明。current coverage能拒绝标题身份/顺序缺失、无效消费者ID、事件导航不等与缺新标题显式声明；新schema负责对象字段类型，但上述空映射豁免仍可绕过。accepted-binding-regressions的5项只针对扩展门遗漏、回执域外文档、部分共享事件、无关事件和清空已变源接受；不含本次旧回执后继字节探针，且它从真实扩展/共享应用基线取样，当前908不具备该基线。

作者5项扩展/共享绑定回归和真实current2704全量检查仍为`NOT_EXECUTED_AWAITING_U04`。本补充分工没有运行这些后继完整验收；独立函数/JSON-schema/Git夹具只证明三个具体结构缺口。第一个coverage夹具构造曾因可选字段缺失而失败；补默认后暴露1776个null-schema错误，随后为隔离ALL_FORMAL探针显式归一null。失败与后继结果分开留证，没有给失败输入PASS。接受来源证据中的21个heading hash为标题字符串hash，规范current locator用整行hash；两种已分别核清，未误报为locator身份失真。

原ROOT-TOOL-02的历史PASS针对当时已知batch/event存在、固定绑定与可解析范围；新receipt-current身份facet作为同根扩展单列，是否重开原组交root统一裁定。此补充未分配旧ID表，未继承或重复投票给旧721/736/33裁定。完整机器结果见[source-results.json](source-results.json)，逐输入/读集身份见[source-machine-evidence.json](source-machine-evidence.json)及[source-prior-reconciliation.json](source-prior-reconciliation.json)。

本分工保留交付仅为本review的source-*工件；两次早期探索importlib曾生成作者目录下忽略的routing/backfill Python缓存，已逐文件删除并清理空缓存目录，候选源码/数据字节未改。Git变异夹具位于`/tmp/r8-r2-source-fixture-a32873d.git`，原对象库只作只读alternates，没有修改作者formal/reference/history/main或运行Ruby/游戏/业务模型/宿主/Showdown原型。真实model、effort、tier、speed、Fast与云UUID无权威echo，逐字段UNVERIFIED；这是一个审查的分工，不是新增独立接受票。
'''
(OUT/'source-report.md').write_text(report)
print(json.dumps({'heading_results':len(headings),'source_diff_documents':len(ledger),'extra_consumer_ranges':len(extras),'new_findings':[(f['id'],f['severity']) for f in findings],'outputs':['source-report.md','source-results.json']},ensure_ascii=False))
